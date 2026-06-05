from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import prepare_output_dir, read_json, write_json, write_jsonl
from core.neural_abr.constants import (
    DATA_FILENAMES,
    DEFAULT_REPRESENTATION_KBPS,
    FEATURE_SCHEMA_FILENAME,
    HYBRID_SOURCE_TEACHERS,
    HYBRID_TEACHER,
    LABEL_SCHEMA_FILENAME,
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_TRAINING_DATA_SCHEMA_ID,
    REQUIRED_TRAINING_DATA_FILES,
    REWARD_VERSION,
    TRAINING_DATA_SUMMARY_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.neural_abr.content_ladder import default_training_ladder
from core.neural_abr.features import build_feature_schema
from core.neural_abr.hybrid_teacher import (
    HybridTeacherError,
    build_hybrid_label_for_draft,
    hybrid_selection_audit,
    select_hybrid_teacher_for_window,
)
from core.neural_abr.normalization import FeatureNormalizer
from core.neural_abr.sample_schema import build_label_schema, validate_sample
from core.neural_abr.training_data import TrainingDataBuildError, load_trace_window
from core.neural_abr.training_data_validation import validate_phase4_training_data_dir
from core.trace_replay.loader import TraceLoadError
from core.trace_replay.network_model import TraceReplayError


HYBRID_TEACHER_AUDIT_FILENAME = "auditoria_teacher_hibrido.json"


def build_phase4_hybrid_teacher_data_from_plan(
    plan: Mapping[str, object],
    output_dir: object,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = (),
    source_teacher_names: Sequence[str] = HYBRID_SOURCE_TEACHERS,
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase4 hybrid teacher training data")
    _validate_plan_for_hybrid_build(plan)
    training_windows = _limited_windows(plan["training_windows"], max_training_windows)  # type: ignore[arg-type]
    validation_windows = _limited_windows(plan["validation_windows"], max_validation_windows)  # type: ignore[arg-type]
    active_representation_kbps = tuple(representation_kbps) if representation_kbps else None
    segment_duration_s = float(plan["primary_segment_duration_s"])
    segment_count = int(round(float(plan["sampling_policy"]["window_duration_s"]) / segment_duration_s))  # type: ignore[index]
    ladder = default_training_ladder(
        segment_duration_s=segment_duration_s,
        segment_count=segment_count,
        representation_kbps=active_representation_kbps or DEFAULT_REPRESENTATION_KBPS,
    )

    samples_by_role: dict[str, list[Mapping[str, object]]] = {TRAINING_ROLE: [], VALIDATION_ROLE: []}
    skipped_windows = []
    selection_audits_by_role: dict[str, list[Mapping[str, object]]] = {TRAINING_ROLE: [], VALIDATION_ROLE: []}
    for data_role, windows in ((TRAINING_ROLE, training_windows), (VALIDATION_ROLE, validation_windows)):
        for window in windows:
            try:
                loaded_trace = load_trace_window(window)
                samples, audit = _samples_for_hybrid_window(
                    window=window,
                    data_role=data_role,
                    loaded_trace=loaded_trace,
                    ladder=ladder,
                    source_teacher_names=source_teacher_names,
                )
                samples_by_role[data_role].extend(samples)
                selection_audits_by_role[data_role].append(audit)
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
    leakage_audit = _build_hybrid_leakage_audit(samples_by_role, skipped_windows)
    hybrid_audit = _build_hybrid_teacher_audit(selection_audits_by_role, skipped_windows, source_teacher_names)
    summary = _build_hybrid_summary(
        output_path=output_path,
        plan=plan,
        ladder_manifest=ladder.to_manifest(),
        samples_by_role=samples_by_role,
        selected_window_counts={TRAINING_ROLE: len(training_windows), VALIDATION_ROLE: len(validation_windows)},
        skipped_windows=skipped_windows,
        hybrid_audit=hybrid_audit,
        source_teacher_names=source_teacher_names,
    )
    write_json(output_path / TRAINING_DATA_SUMMARY_FILENAME, summary)
    write_json(output_path / FEATURE_SCHEMA_FILENAME, build_feature_schema())
    write_json(
        output_path / LABEL_SCHEMA_FILENAME,
        build_label_schema(
            teacher_policy=HYBRID_TEACHER,
            human_readable_name="Labels generados por teacher hibrido sin VMAF",
            extra_label_fields=(
                "hybrid_source_teacher",
                "teacher_selection_scope",
                "teacher_window_qoe_mean",
                "teacher_window_qoe_sum",
            ),
        ),
    )
    write_json(output_path / LEAKAGE_AUDIT_FILENAME, leakage_audit)
    write_json(output_path / NORMALIZATION_STATS_FILENAME, normalizer.stats.to_json())
    write_json(output_path / HYBRID_TEACHER_AUDIT_FILENAME, hybrid_audit)
    return {
        "status": "PASS",
        "output_dir": str(output_path),
        "sample_counts": {role: len(samples_by_role[role]) for role in (TRAINING_ROLE, VALIDATION_ROLE)},
        "skipped_window_count": len(skipped_windows),
        "hybrid_teacher_winner_counts": hybrid_audit["winner_counts"],
        "summary": summary,
    }


def build_phase4_hybrid_teacher_data_from_plan_file(
    plan_path: object,
    output_dir: object,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = (),
    source_teacher_names: Sequence[str] = HYBRID_SOURCE_TEACHERS,
) -> Mapping[str, object]:
    return build_phase4_hybrid_teacher_data_from_plan(
        read_json(plan_path),
        output_dir=output_dir,
        overwrite=overwrite,
        max_training_windows=max_training_windows,
        max_validation_windows=max_validation_windows,
        representation_kbps=representation_kbps,
        source_teacher_names=source_teacher_names,
    )


def validate_phase4_hybrid_teacher_data_dir(path: object) -> Mapping[str, object]:
    report = validate_phase4_training_data_dir(path, allowed_teacher_policies=(HYBRID_TEACHER,))
    data_dir = Path(report["data_dir"])
    summary = read_json(data_dir / TRAINING_DATA_SUMMARY_FILENAME)
    if summary.get("label_teacher") != HYBRID_TEACHER:
        raise TrainingDataBuildError("hybrid data summary must declare teacher_hibrido")
    if summary.get("vmaf_used") is not False:
        raise TrainingDataBuildError("Phase 4H Nivel 1 must not use VMAF")
    if summary.get("teacher_selection_for_training_labels") is not True:
        raise TrainingDataBuildError("hybrid teacher selection flag must be true")
    audit_path = data_dir / HYBRID_TEACHER_AUDIT_FILENAME
    if not audit_path.is_file():
        raise TrainingDataBuildError("missing hybrid teacher audit")
    audit = read_json(audit_path)
    if audit.get("status") != "PASS":
        raise TrainingDataBuildError("hybrid teacher audit did not pass")
    return {
        **dict(report),
        "hybrid_teacher_audit": str(audit_path),
        "hybrid_teacher_winner_counts": dict(audit.get("winner_counts", {})),
    }


def _samples_for_hybrid_window(
    window: Mapping[str, object],
    data_role: str,
    loaded_trace,
    ladder,
    source_teacher_names: Sequence[str],
) -> tuple[tuple[Mapping[str, object], ...], Mapping[str, object]]:
    selection = select_hybrid_teacher_for_window(loaded_trace, ladder, source_teacher_names=source_teacher_names)
    samples = []
    for draft in selection.winner.samples:
        sample = {
            "schema_id": PHASE4_TRAINING_DATA_SCHEMA_ID,
            "sample_id": "{0}__segment_{1:04d}".format(window["window_id"], draft.segment_index),
            "data_role": data_role,
            "context_features": dict(draft.context_features),
            "candidate_features": [dict(candidate) for candidate in draft.candidate_features],
            "action_mask": list(draft.action_mask),
            "label": build_hybrid_label_for_draft(draft, selection),
            "metadata": _hybrid_sample_metadata(window, data_role, draft.segment_index, selection.winner.source_teacher),
        }
        validate_sample(sample, expected_role=data_role, allowed_teacher_policies=(HYBRID_TEACHER,))
        samples.append(sample)
    audit = {
        "window_id": str(window["window_id"]),
        "trace_id": str(window["trace_id"]),
        "data_role": data_role,
        **dict(hybrid_selection_audit(selection)),
    }
    return tuple(samples), audit


def _hybrid_sample_metadata(
    window: Mapping[str, object],
    data_role: str,
    segment_index: int,
    hybrid_source_teacher: str,
) -> Mapping[str, object]:
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
        "hybrid_source_teacher": str(hybrid_source_teacher),
        "metadata_is_model_input": False,
    }


def _build_hybrid_summary(
    output_path: Path,
    plan: Mapping[str, object],
    ladder_manifest: Mapping[str, object],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    selected_window_counts: Mapping[str, int],
    skipped_windows: Sequence[Mapping[str, object]],
    hybrid_audit: Mapping[str, object],
    source_teacher_names: Sequence[str],
) -> Mapping[str, object]:
    return {
        "schema_id": PHASE4_TRAINING_DATA_SCHEMA_ID,
        "human_readable_name": "Datos offline para entrenar NeuralABR-Lite con teacher hibrido sin VMAF",
        "phase": "phase4h_datos_teacher_hibrido_sin_vmaf",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_plan_schema_id": plan.get("schema_id"),
        "source_plan_phase": plan.get("phase"),
        "output_dir": str(output_path),
        "files": {
            **{filename: filename for filename in REQUIRED_TRAINING_DATA_FILES},
            HYBRID_TEACHER_AUDIT_FILENAME: HYBRID_TEACHER_AUDIT_FILENAME,
        },
        "content_ladder": dict(ladder_manifest),
        "selected_window_counts": dict(selected_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in (TRAINING_ROLE, VALIDATION_ROLE)},
        "label_teacher": HYBRID_TEACHER,
        "hybrid_source_teachers": [str(name) for name in source_teacher_names],
        "hybrid_teacher_winner_counts": dict(hybrid_audit.get("winner_counts", {})),
        "teacher_selection_policy": (
            "Simular cada controller clasico en la ventana completa y seleccionar la trayectoria "
            "con mayor qoe_linear_v1; la seleccion solo genera labels offline."
        ),
        "teacher_selection_for_training_labels": True,
        "teacher_selection_uses_future_only_for_offline_labels": True,
        "vmaf_used": False,
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


def _build_hybrid_leakage_audit(
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    errors = []
    label_counts: Counter[str] = Counter()
    source_teacher_counts: Counter[str] = Counter()
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
            label_counts[str(sample["label"]["teacher_action"])] += 1  # type: ignore[index]
            source_teacher_counts[str(sample["label"].get("hybrid_source_teacher", "unknown"))] += 1  # type: ignore[union-attr]
    return {
        "schema_id": "phase4_auditoria_no_contaminacion_teacher_hibrido_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "future_qoe_as_feature": False,
        "teacher_selection_future_used_only_for_labels": True,
        "teacher_action_as_feature": False,
        "legacy_dry_runs_used": False,
        "skipped_window_count": len(skipped_windows),
        "label_distribution": dict(sorted(label_counts.items())),
        "hybrid_source_teacher_sample_distribution": dict(sorted(source_teacher_counts.items())),
    }


def _build_hybrid_teacher_audit(
    selection_audits_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
    source_teacher_names: Sequence[str],
) -> Mapping[str, object]:
    winner_counts: Counter[str] = Counter()
    failure_counts: Counter[str] = Counter()
    windows_by_role = {}
    for role, audits in selection_audits_by_role.items():
        windows_by_role[role] = len(audits)
        for audit in audits:
            winner_counts[str(audit.get("winner", "unknown"))] += 1
            for failure in audit.get("failed_teachers", []):  # type: ignore[union-attr]
                if isinstance(failure, Mapping):
                    failure_counts[str(failure.get("source_teacher", "unknown"))] += 1
    return {
        "schema_id": "phase4_auditoria_teacher_hibrido_v1",
        "human_readable_name": "Auditoria del teacher hibrido sin VMAF",
        "status": "PASS",
        "source_teachers": [str(name) for name in source_teacher_names],
        "selection_metric": "qoe_linear_v1_mean",
        "vmaf_used": False,
        "outputs_are_benchmark_results": False,
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "teacher_selection_for_training_labels": True,
        "windows_by_role": windows_by_role,
        "winner_counts": dict(sorted(winner_counts.items())),
        "failed_teacher_counts": dict(sorted(failure_counts.items())),
        "skipped_window_count": len(skipped_windows),
        "selection_preview": {
            role: list(audits[: min(5, len(audits))])
            for role, audits in selection_audits_by_role.items()
        },
    }


def _validate_plan_for_hybrid_build(plan: Mapping[str, object]) -> None:
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
