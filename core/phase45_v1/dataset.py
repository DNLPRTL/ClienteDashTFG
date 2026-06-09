from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import prepare_output_dir, write_json, write_jsonl
from core.neural_abr.content_ladder import default_training_ladder
from core.neural_abr.features import build_candidate_features, build_context_features
from core.neural_abr.hybrid_teacher import ClassicControllerTeacher
from core.neural_abr.replay_environment import TraceReplayEnvironment
from core.phase45_v1.constants import (
    CLASSIC_AUDIT_CONTROLLERS,
    DATA_FILENAMES,
    DATA_ROLES,
    DATASET_SCHEMA_ID,
    LEAKAGE_AUDIT_FILENAME,
    LEAKAGE_AUDIT_SCHEMA_ID,
    MEDIA_PROFILE_ID,
    NORMALIZATION_STATS_FILENAME,
    ORACLE_AUDIT_FILENAME,
    ORACLE_AUDIT_SCHEMA_ID,
    ORACLE_POLICY_ID,
    PHASE45_V1_PHASE,
    REWARD_VERSION,
    SAMPLE_SCHEMA_ID,
    SAMPLING_AUDIT_FILENAME,
    SAMPLING_PLAN_FILENAME,
    SPC_TARGET_ID,
    SPBC_TARGET_ID,
    SUMMARY_FILENAME,
    TARGET_SCHEMA_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
    FEATURE_SCHEMA_FILENAME,
    no_benchmark_policy,
)
from core.phase45_v1.normalization import build_train_only_normalization
from core.phase45_v1.oracle import (
    OracleConfig,
    linear_reward_for_state,
    oracle_policy_card,
    select_oracle_action,
    simulate_step_from_state,
)
from core.phase45_v1.paths import PathRewriteRule, resolve_external_trace_path
from core.phase45_v1.profiles import DatasetProfile
from core.phase45_v1.sample_schema import build_model_input_schema, build_target_schema, validate_sample
from core.phase45_v1.sampling import build_sampling_artifacts
from core.trace_replay.loader import LoadedTrace, TraceLoadError, load_normalized_trace_rows
from core.trace_replay.network_model import TraceReplayError


class Phase45DatasetBuildError(ValueError):
    """Raised when the Phase 4-5 v1 dataset cannot be built safely."""


def build_phase45_v1_dataset(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: DatasetProfile,
    *,
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = (300, 750, 1200, 1850, 2850, 4300),
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v1 dataset")
    sampling = build_sampling_artifacts(phase3_manifest, profile, source_manifest_path=source_manifest_path)
    plan = sampling["plan"]
    sampling_audit = sampling["audit"]
    training_windows = _limited_windows(plan["training_windows"], max_training_windows)  # type: ignore[index]
    validation_windows = _limited_windows(plan["validation_windows"], max_validation_windows)  # type: ignore[index]
    segment_duration_s = float(plan["sampling_policy"]["segment_duration_s"])  # type: ignore[index]
    segment_count = int(plan["segment_count_per_window"])
    ladder = default_training_ladder(
        segment_duration_s=segment_duration_s,
        segment_count=segment_count,
        representation_kbps=representation_kbps,
        max_buffer_s=20.0,
    )
    oracle_config = OracleConfig(
        horizon_segments=profile.oracle_horizon_segments,
        beam_width=profile.oracle_beam_width,
    )

    samples_by_role: dict[str, list[Mapping[str, object]]] = {TRAINING_ROLE: [], VALIDATION_ROLE: []}
    skipped_windows: list[Mapping[str, object]] = []
    oracle_events: list[Mapping[str, object]] = []
    resolved_path_examples: list[Mapping[str, object]] = []

    for data_role, windows in ((TRAINING_ROLE, training_windows), (VALIDATION_ROLE, validation_windows)):
        for window in windows:
            try:
                loaded_trace, resolved_trace_path = load_trace_window(window, trace_path_rewrites)
                if len(resolved_path_examples) < 8:
                    resolved_path_examples.append(
                        {
                            "window_id": str(window["window_id"]),
                            "raw_normalized_trace_path": str(window["normalized_trace_path"]),
                            "resolved_normalized_trace_path": str(resolved_trace_path),
                        }
                    )
                window_samples, window_oracle_events = _samples_for_window(
                    window=window,
                    data_role=data_role,
                    loaded_trace=loaded_trace,
                    ladder=ladder,
                    oracle_config=oracle_config,
                    future_horizon_segments=profile.future_horizon_segments,
                )
                samples_by_role[data_role].extend(window_samples)
                oracle_events.extend(window_oracle_events)
            except Exception as exc:  # noqa: BLE001 - skipped windows are audited so generation can continue.
                skipped_windows.append(
                    {
                        "window_id": str(window.get("window_id")),
                        "data_role": data_role,
                        "trace_id": str(window.get("trace_id")),
                        "reason": type(exc).__name__,
                        "message": str(exc),
                    }
                )

    if not samples_by_role[TRAINING_ROLE] or not samples_by_role[VALIDATION_ROLE]:
        raise Phase45DatasetBuildError(
            "dataset generation produced empty training or validation samples; skipped_window_count={0}".format(
                len(skipped_windows)
            )
        )

    for data_role, filename in DATA_FILENAMES.items():
        write_jsonl(output_path / filename, samples_by_role[data_role])

    generation_window_counts = {
        TRAINING_ROLE: len(training_windows),
        VALIDATION_ROLE: len(validation_windows),
    }
    leakage_audit = _build_leakage_audit(samples_by_role, skipped_windows)
    oracle_audit = _build_oracle_audit(oracle_config, oracle_events)
    normalization = build_train_only_normalization(samples_by_role[TRAINING_ROLE])
    summary = _build_summary(
        output_path=output_path,
        profile=profile,
        plan=plan,
        ladder_manifest=ladder.to_manifest(),
        generation_window_counts=generation_window_counts,
        samples_by_role=samples_by_role,
        skipped_windows=skipped_windows,
        path_rewrites=trace_path_rewrites,
        resolved_path_examples=resolved_path_examples,
    )

    write_json(output_path / SUMMARY_FILENAME, summary)
    write_json(output_path / SAMPLING_PLAN_FILENAME, plan)
    write_json(output_path / SAMPLING_AUDIT_FILENAME, sampling_audit)
    write_json(output_path / FEATURE_SCHEMA_FILENAME, build_model_input_schema())
    write_json(output_path / TARGET_SCHEMA_FILENAME, build_target_schema())
    write_json(output_path / LEAKAGE_AUDIT_FILENAME, leakage_audit)
    write_json(output_path / NORMALIZATION_STATS_FILENAME, normalization)
    write_json(output_path / ORACLE_AUDIT_FILENAME, oracle_audit)

    return {
        "status": "PASS",
        "output_dir": str(output_path),
        "profile": profile.name,
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "generation_window_counts": generation_window_counts,
        "skipped_window_count": len(skipped_windows),
        "benchmark_performed": False,
        "ia_training_performed": False,
        "summary": summary,
    }


def load_trace_window(
    window: Mapping[str, object],
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
) -> tuple[LoadedTrace, Path]:
    path = resolve_external_trace_path(window["normalized_trace_path"], trace_path_rewrites)
    window_start_s = float(window["window_start_s"])
    window_end_s = float(window["window_end_s"])
    rows = []
    try:
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
    except OSError as exc:
        raise Phase45DatasetBuildError("cannot read normalized trace window: {0}".format(path)) from exc
    if not rows:
        raise Phase45DatasetBuildError("{0}: no rows overlap selected trace window".format(window.get("window_id")))
    try:
        return load_normalized_trace_rows(rows, trace_id=str(window["window_id"])), path
    except TraceLoadError as exc:
        raise Phase45DatasetBuildError(str(exc)) from exc


def _samples_for_window(
    *,
    window: Mapping[str, object],
    data_role: str,
    loaded_trace: LoadedTrace,
    ladder,
    oracle_config: OracleConfig,
    future_horizon_segments: int,
) -> tuple[list[Mapping[str, object]], list[Mapping[str, object]]]:
    env = TraceReplayEnvironment(loaded_trace, ladder)
    classic_teachers = {name: ClassicControllerTeacher(name) for name in CLASSIC_AUDIT_CONTROLLERS}
    samples: list[Mapping[str, object]] = []
    oracle_events: list[Mapping[str, object]] = []
    while not env.done:
        state = env.state
        action_mask = env.action_mask()
        context = build_context_features(state, ladder)
        candidates = build_candidate_features(ladder, state.segment_index, float(context["last_bitrate_bps"]))
        oracle_decision = select_oracle_action(state, ladder, env.network_model, oracle_config)
        spc_targets = _build_spc_targets(
            loaded_trace=loaded_trace,
            state=state,
            ladder=ladder,
            candidates=candidates,
            network_model=env.network_model,
            future_horizon_segments=future_horizon_segments,
        )
        audit = _build_audit(
            state=state,
            ladder=ladder,
            network_model=env.network_model,
            action_mask=action_mask,
            classic_teachers=classic_teachers,
            oracle_decision=oracle_decision.to_json(),
        )
        step = env.step(oracle_decision.action)
        sample = {
            "schema_id": SAMPLE_SCHEMA_ID,
            "sample_id": "{0}__segment_{1:04d}".format(window["window_id"], state.segment_index),
            "data_role": data_role,
            "model_inputs": {
                "context": dict(context),
                "candidates": [dict(candidate) for candidate in candidates],
                "action_mask": [bool(value) for value in action_mask],
            },
            "spc_targets": spc_targets,
            "spbc_targets": {
                "target_id": SPBC_TARGET_ID,
                "oracle_policy_id": ORACLE_POLICY_ID,
                "qoe_formula_version": REWARD_VERSION,
                "oracle_action": int(oracle_decision.action),
                "oracle_horizon_reward_n": float(oracle_decision.horizon_reward_n),
                "oracle_first_step_reward_n": float(oracle_decision.first_step_reward_n),
                "oracle_best_sequence": list(oracle_decision.best_sequence),
                "oracle_horizon_segments_evaluated": int(oracle_decision.horizon_segments_evaluated),
                "oracle_beam_width": int(oracle_decision.beam_width),
                "oracle_reason": oracle_decision.reason,
                "oracle_fallback_used": bool(oracle_decision.fallback_used),
            },
            "audit": {
                **audit,
                "selected_oracle_step": {
                    "action": int(step.action),
                    "download_time_s": round(float(step.download_time_s), 6),
                    "rebuffer_s": round(float(step.rebuffer_s), 6),
                    "buffer_s_before": round(float(step.buffer_s_before), 6),
                    "buffer_s_after": round(float(step.buffer_s_after), 6),
                    "measured_throughput_bps": round(float(step.measured_throughput_bps), 6),
                },
            },
            "metadata": _sample_metadata(window, data_role, state.segment_index),
        }
        validate_sample(sample, expected_role=data_role)
        samples.append(sample)
        oracle_events.append(
            {
                "data_role": data_role,
                "action": oracle_decision.action,
                "fallback_used": oracle_decision.fallback_used,
                "horizon_reward_n": oracle_decision.horizon_reward_n,
            }
        )
    return samples, oracle_events


def _build_spc_targets(
    *,
    loaded_trace: LoadedTrace,
    state,
    ladder,
    candidates: Sequence[Mapping[str, object]],
    network_model,
    future_horizon_segments: int,
) -> Mapping[str, object]:
    horizon_s = float(future_horizon_segments) * float(ladder.segment_duration_s)
    future_stats = _future_throughput_stats(loaded_trace, state.playback_time_s, horizon_s)
    per_candidate = []
    for candidate in candidates:
        representation_index = int(float(candidate["candidate_representation_index"]))
        try:
            _next_state, step = simulate_step_from_state(state, ladder, network_model, representation_index)
            estimated_rebuffer_s = float(step.rebuffer_s)
            per_candidate.append(
                {
                    "representation_index": representation_index,
                    "bitrate_kbps": round(float(ladder.bitrate_bps(representation_index)) / 1000.0, 6),
                    "estimated_download_time_s": round(float(step.download_time_s), 6),
                    "estimated_rebuffer_s": round(estimated_rebuffer_s, 6),
                    "rebuffer_risk": 1.0 if estimated_rebuffer_s > 0.0 else 0.0,
                    "download_estimate_error": False,
                }
            )
        except TraceReplayError as exc:
            per_candidate.append(
                {
                    "representation_index": representation_index,
                    "bitrate_kbps": round(float(ladder.bitrate_bps(representation_index)) / 1000.0, 6),
                    "estimated_download_time_s": None,
                    "estimated_rebuffer_s": None,
                    "rebuffer_risk": 1.0,
                    "download_estimate_error": True,
                    "download_estimate_error_type": type(exc).__name__,
                }
            )
    return {
        "target_id": SPC_TARGET_ID,
        "future_horizon_segments": int(future_horizon_segments),
        "future_horizon_s": round(horizon_s, 6),
        "future_throughput_kbps": future_stats,
        "conservative_capacity_kbps": round(
            min(float(future_stats["p25"]), float(future_stats["p50"]) * 0.85),
            6,
        ),
        "per_candidate_download_risk": per_candidate,
        "future_information_is_target_only": True,
    }


def _build_audit(
    *,
    state,
    ladder,
    network_model,
    action_mask: Sequence[bool],
    classic_teachers: Mapping[str, ClassicControllerTeacher],
    oracle_decision: Mapping[str, object],
) -> Mapping[str, object]:
    classic = []
    for name, teacher in classic_teachers.items():
        try:
            decision = teacher.select_action(state, ladder, action_mask)
            _next_state, step = simulate_step_from_state(state, ladder, network_model, decision.representation_index)
            classic.append(
                {
                    "controller": name,
                    "action": int(decision.representation_index),
                    "reward_n": round(
                        linear_reward_for_state(state, ladder, decision.representation_index, step.rebuffer_s),
                        6,
                    ),
                    "estimated_rebuffer_s": round(float(step.rebuffer_s), 6),
                    "reason": decision.reason,
                    "failed": False,
                }
            )
        except Exception as exc:  # noqa: BLE001 - controller audit failures must not hide oracle labels.
            classic.append(
                {
                    "controller": name,
                    "failed": True,
                    "reason": type(exc).__name__,
                    "message": str(exc),
                }
            )
    return {
        "oracle": dict(oracle_decision),
        "classic_controllers": classic,
        "classic_controllers_are_audit_only": True,
        "classic_controllers_are_primary_teacher": False,
    }


def _future_throughput_stats(loaded_trace: LoadedTrace, start_time_s: float, horizon_s: float) -> Mapping[str, object]:
    values = _weighted_future_values(loaded_trace, start_time_s, horizon_s)
    if not values:
        value = max(float(loaded_trace.throughput_mean_kbps), 0.0)
        values = [(value, float(horizon_s))]
    total_weight = sum(weight for _value, weight in values)
    weighted_mean = sum(value * weight for value, weight in values) / max(total_weight, 1e-9)
    raw_values = [value for value, _weight in values]
    return {
        "min": round(min(raw_values), 6),
        "p10": round(_weighted_quantile(values, 0.10), 6),
        "p25": round(_weighted_quantile(values, 0.25), 6),
        "p50": round(_weighted_quantile(values, 0.50), 6),
        "mean": round(weighted_mean, 6),
        "max": round(max(raw_values), 6),
    }


def _weighted_future_values(loaded_trace: LoadedTrace, start_time_s: float, horizon_s: float) -> list[tuple[float, float]]:
    duration_s = max(float(loaded_trace.duration_s), 1e-9)
    remaining_s = max(float(horizon_s), 0.0)
    cursor_s = max(float(start_time_s), 0.0)
    values: list[tuple[float, float]] = []
    while remaining_s > 1e-9:
        local_start = cursor_s % duration_s
        local_remaining = min(remaining_s, duration_s - local_start)
        local_end = local_start + local_remaining
        for sample in loaded_trace.samples:
            sample_start = float(sample.timestamp_s)
            sample_end = sample_start + float(sample.duration_s)
            overlap_start = max(sample_start, local_start)
            overlap_end = min(sample_end, local_end)
            if overlap_end > overlap_start:
                values.append((max(float(sample.throughput_kbps), 0.0), overlap_end - overlap_start))
        cursor_s += local_remaining
        remaining_s -= local_remaining
    return values


def _weighted_quantile(values: Sequence[tuple[float, float]], quantile: float) -> float:
    ordered = sorted((float(value), max(float(weight), 0.0)) for value, weight in values)
    total = sum(weight for _value, weight in ordered)
    if total <= 0.0:
        return ordered[0][0] if ordered else 0.0
    threshold = float(quantile) * total
    cumulative = 0.0
    for value, weight in ordered:
        cumulative += weight
        if cumulative >= threshold:
            return value
    return ordered[-1][0]


def _sample_metadata(window: Mapping[str, object], data_role: str, segment_index: int) -> Mapping[str, object]:
    return {
        "metadata_is_model_input": False,
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
        "throughput_bucket": str(window.get("throughput_bucket", "")),
        "variability_bucket": str(window.get("variability_bucket", "")),
        "network_condition": str(window.get("network_condition", "unknown")),
    }


def _build_summary(
    *,
    output_path: Path,
    profile: DatasetProfile,
    plan: Mapping[str, object],
    ladder_manifest: Mapping[str, object],
    generation_window_counts: Mapping[str, int],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
    path_rewrites: Sequence[PathRewriteRule],
    resolved_path_examples: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    return {
        "schema_id": DATASET_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v1 offline dataset for SPC/SPBC ABR candidates",
        "phase": PHASE45_V1_PHASE,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "source_plan_schema_id": plan.get("schema_id"),
        "media_profile_id": MEDIA_PROFILE_ID,
        "content_ladder": dict(ladder_manifest),
        "files": {filename: filename for filename in DATA_FILENAMES.values()},
        "required_files": [
            SUMMARY_FILENAME,
            SAMPLING_PLAN_FILENAME,
            SAMPLING_AUDIT_FILENAME,
            FEATURE_SCHEMA_FILENAME,
            TARGET_SCHEMA_FILENAME,
            LEAKAGE_AUDIT_FILENAME,
            NORMALIZATION_STATS_FILENAME,
            ORACLE_AUDIT_FILENAME,
        ],
        "generation_window_counts": dict(generation_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "oracle_policy": oracle_policy_card(
            OracleConfig(profile.oracle_horizon_segments, profile.oracle_beam_width)
        ),
        "spc_target_source": "future trace replay labels, target-only",
        "spbc_target_source": ORACLE_POLICY_ID,
        "classic_controllers_role": "audit_only_not_primary_teacher",
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "normalization_fitted_on": TRAINING_ROLE,
        "trace_path_rewrites": [rule.to_json() for rule in path_rewrites],
        "resolved_path_examples": list(resolved_path_examples),
        "skipped_windows": list(skipped_windows),
        **no_benchmark_policy(),
    }


def _build_leakage_audit(
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    errors = []
    by_source_split: Counter[str] = Counter()
    by_synthetic: Counter[str] = Counter()
    for role, samples in samples_by_role.items():
        for sample in samples:
            metadata = sample["metadata"]
            trace_id = str(metadata["trace_id"])
            previous_trace_role = trace_roles.setdefault(trace_id, role)
            if previous_trace_role != role:
                errors.append("trace_id selected in multiple roles: {0}".format(trace_id))
            group = str(metadata["leakage_group"])
            previous_group_role = leakage_group_roles.setdefault(group, role)
            if previous_group_role != role:
                errors.append("leakage_group selected in multiple roles: {0}".format(group))
            source_split = str(metadata["source_split"])
            if source_split == "eval":
                errors.append("eval split used in sample: {0}".format(sample["sample_id"]))
            by_source_split[source_split] += 1
            by_synthetic[str(bool(metadata.get("synthetic")))] += 1
    return {
        "schema_id": LEAKAGE_AUDIT_SCHEMA_ID,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "oracle_action_as_feature": False,
        "classic_controller_action_as_feature": False,
        "legacy_dry_runs_used": False,
        "skipped_window_count": len(skipped_windows),
        "sample_counts_by_source_split": dict(sorted(by_source_split.items())),
        "sample_counts_by_synthetic": dict(sorted(by_synthetic.items())),
    }


def _build_oracle_audit(
    oracle_config: OracleConfig,
    oracle_events: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    by_role: dict[str, Counter[str]] = defaultdict(Counter)
    action_counts: Counter[str] = Counter()
    fallback_count = 0
    rewards = []
    for event in oracle_events:
        role = str(event["data_role"])
        action = str(event["action"])
        by_role[role][action] += 1
        action_counts[action] += 1
        fallback_count += 1 if event.get("fallback_used") is True else 0
        rewards.append(float(event.get("horizon_reward_n", 0.0)))
    return {
        "schema_id": ORACLE_AUDIT_SCHEMA_ID,
        "oracle_policy_id": ORACLE_POLICY_ID,
        "qoe_formula_version": REWARD_VERSION,
        "config": oracle_config.to_json(),
        "sample_count": len(oracle_events),
        "fallback_count": fallback_count,
        "fallback_fraction": round(float(fallback_count) / float(len(oracle_events)), 6) if oracle_events else 0.0,
        "action_distribution": dict(sorted(action_counts.items())),
        "action_distribution_by_role": {role: dict(sorted(counter.items())) for role, counter in sorted(by_role.items())},
        "horizon_reward_mean": round(sum(rewards) / float(len(rewards)), 6) if rewards else 0.0,
        "uses_future_information": True,
        "future_information_is_target_only": True,
        **no_benchmark_policy(),
    }


def _limited_windows(raw_windows: object, limit: int | None) -> list[Mapping[str, object]]:
    if not isinstance(raw_windows, list):
        raise Phase45DatasetBuildError("sampling plan windows must be a list")
    windows = []
    for index, window in enumerate(raw_windows):
        if not isinstance(window, Mapping):
            raise Phase45DatasetBuildError("window {0} must be an object".format(index))
        windows.append(window)
    if limit is not None:
        return windows[: int(limit)]
    return windows


def load_phase3_manifest(path: object) -> Mapping[str, object]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)
