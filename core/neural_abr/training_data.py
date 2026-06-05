from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.action_mask import build_action_mask
from core.neural_abr.artifacts import prepare_output_dir, read_json, write_json, write_jsonl
from core.neural_abr.constants import (
    DATA_FILENAMES,
    DEFAULT_REPRESENTATION_KBPS,
    FEATURE_SCHEMA_FILENAME,
    LABEL_SCHEMA_FILENAME,
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_TRAINING_DATA_SCHEMA_ID,
    PRIMARY_TEACHER,
    REQUIRED_TRAINING_DATA_FILES,
    REWARD_VERSION,
    TRAINING_DATA_SUMMARY_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.neural_abr.content_ladder import default_training_ladder
from core.neural_abr.features import build_candidate_features, build_context_features, build_feature_schema
from core.neural_abr.hybrid_teacher import ClassicControllerTeacher, HybridTeacherError, qoe_linear_reward_for_replay_step
from core.neural_abr.normalization import FeatureNormalizer
from core.neural_abr.replay_environment import TraceReplayEnvironment
from core.neural_abr.sample_schema import build_label_schema, validate_sample
from core.trace_replay.loader import LoadedTrace, TraceLoadError, load_normalized_trace_rows
from core.trace_replay.network_model import TraceReplayError


class TrainingDataBuildError(ValueError):
    """Raised when Phase 4 training data cannot be generated."""


def build_phase4_training_data_from_plan(
    plan: Mapping[str, object],
    output_dir: object,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = DEFAULT_REPRESENTATION_KBPS,
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase4 training data")
    _validate_plan_for_data_build(plan)
    training_windows = _limited_windows(plan["training_windows"], max_training_windows)  # type: ignore[arg-type]
    validation_windows = _limited_windows(plan["validation_windows"], max_validation_windows)  # type: ignore[arg-type]
    segment_duration_s = float(plan["primary_segment_duration_s"])
    segment_count = int(round(float(plan["sampling_policy"]["window_duration_s"]) / segment_duration_s))  # type: ignore[index]
    ladder = default_training_ladder(
        segment_duration_s=segment_duration_s,
        segment_count=segment_count,
        representation_kbps=representation_kbps,
    )
    teacher = ClassicControllerTeacher(PRIMARY_TEACHER)

    samples_by_role: dict[str, list[Mapping[str, object]]] = {TRAINING_ROLE: [], VALIDATION_ROLE: []}
    skipped_windows = []
    for data_role, windows in ((TRAINING_ROLE, training_windows), (VALIDATION_ROLE, validation_windows)):
        for window in windows:
            try:
                loaded_trace = load_trace_window(window)
                samples_by_role[data_role].extend(_samples_for_window(window, data_role, loaded_trace, ladder, teacher))
            except (OSError, TraceLoadError, TraceReplayError, TrainingDataBuildError, HybridTeacherError) as exc:
                skipped_windows.append(
                    {
                        "window_id": str(window.get("window_id")),
                        "data_role": data_role,
                        "trace_id": str(window.get("trace_id")),
                        "reason": type(exc).__name__,
                        "message": str(exc),
                    }
                )

    for data_role, filename in DATA_FILENAMES.items():
        write_jsonl(output_path / filename, samples_by_role[data_role])

    normalizer = FeatureNormalizer.fit_training_only(samples_by_role[TRAINING_ROLE])
    leakage_audit = _build_leakage_audit(samples_by_role, skipped_windows)
    summary = _build_summary(
        output_path=output_path,
        plan=plan,
        ladder_manifest=ladder.to_manifest(),
        samples_by_role=samples_by_role,
        selected_window_counts={TRAINING_ROLE: len(training_windows), VALIDATION_ROLE: len(validation_windows)},
        skipped_windows=skipped_windows,
    )
    write_json(output_path / TRAINING_DATA_SUMMARY_FILENAME, summary)
    write_json(output_path / FEATURE_SCHEMA_FILENAME, build_feature_schema())
    write_json(output_path / LABEL_SCHEMA_FILENAME, build_label_schema())
    write_json(output_path / LEAKAGE_AUDIT_FILENAME, leakage_audit)
    write_json(output_path / NORMALIZATION_STATS_FILENAME, normalizer.stats.to_json())
    return {
        "status": "PASS",
        "output_dir": str(output_path),
        "sample_counts": {role: len(samples_by_role[role]) for role in (TRAINING_ROLE, VALIDATION_ROLE)},
        "skipped_window_count": len(skipped_windows),
        "summary": summary,
    }


def build_phase4_training_data_from_plan_file(
    plan_path: object,
    output_dir: object,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = DEFAULT_REPRESENTATION_KBPS,
) -> Mapping[str, object]:
    plan = read_json(plan_path)
    return build_phase4_training_data_from_plan(
        plan,
        output_dir=output_dir,
        overwrite=overwrite,
        max_training_windows=max_training_windows,
        max_validation_windows=max_validation_windows,
        representation_kbps=representation_kbps,
    )


def load_trace_window(window: Mapping[str, object]) -> LoadedTrace:
    path = Path(str(window["normalized_trace_path"]))
    window_start_s = float(window["window_start_s"])
    window_end_s = float(window["window_end_s"])
    rows = []
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        accumulated_start_s = 0.0
        for raw_row in reader:
            row_duration_s = float(raw_row["duration_s"])
            row_start = accumulated_start_s
            row_end = row_start + row_duration_s
            accumulated_start_s = row_end
            overlap_start = max(row_start, window_start_s)
            overlap_end = min(row_end, window_end_s)
            if overlap_end <= overlap_start:
                continue
            rows.append(
                {
                    "timestamp_s": overlap_start - window_start_s,
                    "duration_s": overlap_end - overlap_start,
                    "throughput_kbps": float(raw_row["throughput_kbps"]),
                }
            )
    if not rows:
        raise TrainingDataBuildError("{0}: no rows overlap selected trace window".format(window.get("window_id")))
    return load_normalized_trace_rows(rows, trace_id=str(window["window_id"]))


def _samples_for_window(
    window: Mapping[str, object],
    data_role: str,
    loaded_trace: LoadedTrace,
    ladder,
    teacher,
) -> tuple[Mapping[str, object], ...]:
    env = TraceReplayEnvironment(loaded_trace, ladder)
    samples = []
    while not env.done:
        state = env.state
        action_mask = build_action_mask(ladder, state.segment_index)
        context = build_context_features(state, ladder)
        candidates = build_candidate_features(ladder, state.segment_index, float(context["last_bitrate_bps"]))
        decision = teacher.select_action(state, ladder, action_mask)
        step = env.step(decision.representation_index)
        sample = {
            "schema_id": PHASE4_TRAINING_DATA_SCHEMA_ID,
            "sample_id": "{0}__segment_{1:04d}".format(window["window_id"], state.segment_index),
            "data_role": data_role,
            "context_features": dict(context),
            "candidate_features": [dict(candidate) for candidate in candidates],
            "action_mask": list(action_mask),
            "label": {
                "teacher_action": int(decision.representation_index),
                "teacher_policy": decision.teacher_policy,
                "teacher_reward_n": qoe_linear_reward_for_replay_step(
                    state,
                    ladder,
                    decision.representation_index,
                    step.rebuffer_s,
                ),
                "reward_version": REWARD_VERSION,
                "diagnostic_only": True,
                "reason": decision.reason,
            },
            "metadata": _sample_metadata(window, data_role, state.segment_index),
        }
        validate_sample(sample, expected_role=data_role)
        samples.append(sample)
    return tuple(samples)


def _sample_metadata(window: Mapping[str, object], data_role: str, segment_index: int) -> Mapping[str, object]:
    return {
        "data_role": data_role,
        "window_id": str(window["window_id"]),
        "trace_id": str(window["trace_id"]),
        "dataset_id": str(window["dataset_id"]),
        "semantics": str(window["semantics"]),
        "source_split": str(window["source_split"]),
        "group_id": str(window["group_id"]),
        "leakage_group": str(window["leakage_group"]),
        "window_start_s": float(window["window_start_s"]),
        "window_end_s": float(window["window_end_s"]),
        "segment_index": int(segment_index),
        "synthetic": bool(window.get("synthetic") is True),
        "network_condition": str(window.get("network_condition", "unknown")),
        "metadata_is_model_input": False,
    }


def _build_summary(
    output_path: Path,
    plan: Mapping[str, object],
    ladder_manifest: Mapping[str, object],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    selected_window_counts: Mapping[str, int],
    skipped_windows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    return {
        "schema_id": PHASE4_TRAINING_DATA_SCHEMA_ID,
        "human_readable_name": "Datos offline para entrenar NeuralABR-Lite mas adelante",
        "phase": "phase4bcd_datos_y_prueba_rapida_offline",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_plan_schema_id": plan.get("schema_id"),
        "source_plan_phase": plan.get("phase"),
        "output_dir": str(output_path),
        "files": {filename: filename for filename in REQUIRED_TRAINING_DATA_FILES},
        "content_ladder": dict(ladder_manifest),
        "selected_window_counts": dict(selected_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in (TRAINING_ROLE, VALIDATION_ROLE)},
        "label_teacher": PRIMARY_TEACHER,
        "label_teacher_source": "phase2_controller_real_en_replay_offline",
        "label_teacher_controller_module": "core.controller.robust_mpc.RobustMpcController",
        "label_teacher_adapter": "core.neural_abr.hybrid_teacher.ClassicControllerTeacher",
        "reward_version": REWARD_VERSION,
        "normalization_fitted_on": "training samples only",
        "metadata_fields_are_model_features": False,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": False,
        "formal_ia_training_performed": False,
        "candidate_model_created": False,
        "skipped_windows": list(skipped_windows),
    }


def _build_leakage_audit(
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    errors = []
    label_counts: Counter[str] = Counter()
    for role, samples in samples_by_role.items():
        for sample in samples:
            metadata = sample["metadata"]
            trace_id = str(metadata["trace_id"])
            previous_trace_role = trace_roles.setdefault(trace_id, role)
            if previous_trace_role != role:
                errors.append("trace_id selected in multiple data roles: {0}".format(trace_id))
            group = str(metadata["leakage_group"])
            previous_group_role = leakage_group_roles.setdefault(group, role)
            if previous_group_role != role:
                errors.append("leakage_group selected in multiple data roles: {0}".format(group))
            label_counts[str(sample["label"]["teacher_action"])] += 1
    return {
        "schema_id": "phase4_auditoria_no_contaminacion_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "teacher_action_as_feature": False,
        "legacy_dry_runs_used": False,
        "skipped_window_count": len(skipped_windows),
        "label_distribution": dict(sorted(label_counts.items())),
    }


def _validate_plan_for_data_build(plan: Mapping[str, object]) -> None:
    if plan.get("schema_id") != "phase4_training_trace_plan_v1":
        raise TrainingDataBuildError("plan must be a Phase 4A training trace plan")
    if plan.get("benchmark_performed") is not False or plan.get("ia_training_performed") is not False:
        raise TrainingDataBuildError("source plan must not be benchmark or IA training output")
    for field in ("training_windows", "validation_windows", "primary_segment_duration_s", "sampling_policy"):
        if field not in plan:
            raise TrainingDataBuildError("source plan missing {0}".format(field))


def _limited_windows(raw_windows: object, limit: int | None) -> list[Mapping[str, object]]:
    if not isinstance(raw_windows, list):
        raise TrainingDataBuildError("plan windows must be a list")
    windows = []
    for index, window in enumerate(raw_windows):
        if not isinstance(window, Mapping):
            raise TrainingDataBuildError("window {0} must be an object".format(index))
        windows.append(window)
    if limit is not None:
        return windows[: int(limit)]
    return windows
