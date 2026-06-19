from __future__ import annotations

import math
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Mapping, Sequence

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, read_jsonl, write_json, write_jsonl
from core.neural_abr.features import build_context_features, flatten_context_features, reject_forbidden_model_inputs
from core.phase45_v1.dataset import load_trace_window
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.sampling import build_sampling_artifacts
from core.phase45_v3.abr_closed_loop_env import (
    PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    AbrClosedLoopEnv,
    default_phase45_v3_ladder,
)
from core.phase45_v3.constants import (
    MEDIA_PROFILE_ID,
    PHASE45_V3_PHASE,
    REWARD_VERSION,
    TRAINING_ROLE,
    VALIDATION_ROLE,
    no_benchmark_policy,
)
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.trace_replay.loader import LoadedTrace
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel


THROUGHPUT_QUANTILE_DATASET_SCHEMA_ID = "phase45_v3_throughput_quantile_dataset_v1"
THROUGHPUT_QUANTILE_SAMPLE_SCHEMA_ID = "phase45_v3_throughput_quantile_sample_v1"
THROUGHPUT_QUANTILE_TARGET_ID = "phase45_v3_future_throughput_log_ratio_quantiles_v1"
THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_SCHEMA_ID = "phase45_v3_throughput_quantile_no_contamination_audit_v1"
THROUGHPUT_QUANTILE_TARGET_SCHEMA_ID = "phase45_v3_throughput_quantile_targets_schema_v1"

THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME = "datos_entrenamiento_phase45_v3_throughput_quantile.jsonl"
THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME = "datos_validacion_phase45_v3_throughput_quantile.jsonl"
THROUGHPUT_QUANTILE_SUMMARY_FILENAME = "resumen_dataset_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_SAMPLING_PLAN_FILENAME = "plan_muestreo_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_SAMPLING_AUDIT_FILENAME = "auditoria_muestreo_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_TARGET_SCHEMA_FILENAME = "esquema_targets_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion_phase45_v3_throughput_quantile.json"

THROUGHPUT_QUANTILE_DATA_FILENAMES = {
    TRAINING_ROLE: THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME,
    VALIDATION_ROLE: THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME,
}
THROUGHPUT_QUANTILE_REQUIRED_DATASET_FILES = (
    THROUGHPUT_QUANTILE_SUMMARY_FILENAME,
    THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME,
    THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME,
    THROUGHPUT_QUANTILE_SAMPLING_PLAN_FILENAME,
    THROUGHPUT_QUANTILE_SAMPLING_AUDIT_FILENAME,
    THROUGHPUT_QUANTILE_TARGET_SCHEMA_FILENAME,
    THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME,
)

DEFAULT_THROUGHPUT_QUANTILES = (0.10, 0.25, 0.50, 0.75)
DEFAULT_THROUGHPUT_QUANTILE_HORIZON = 5
DEFAULT_BASE_THROUGHPUT_EPS_BPS = 1.0
DEFAULT_STARTUP_BASE_THROUGHPUT_BPS = 300_000.0

ROLLOUT_ROBUST_RATE = "robust_rate"
ROLLOUT_RATE_UP = "rate_up"
ROLLOUT_BUFFER_SAFE = "buffer_safe"
ROLLOUT_CYCLIC = "cyclic"
THROUGHPUT_QUANTILE_ROLLOUT_POLICIES = (
    ROLLOUT_ROBUST_RATE,
    ROLLOUT_RATE_UP,
    ROLLOUT_BUFFER_SAFE,
    ROLLOUT_CYCLIC,
)


class Phase45V3ThroughputQuantileDatasetError(ValueError):
    """Raised when the throughput-quantile dataset cannot be built safely."""


def build_phase45_v3_throughput_quantile_dataset(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: Phase45V3DatasetProfile,
    *,
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = (300, 750, 1200, 1850, 2850, 4300),
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
    horizon_segments: int = DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    quantiles: Sequence[float] = DEFAULT_THROUGHPUT_QUANTILES,
    ladder_factory: Callable[[float, int], object] | None = None,
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 throughput quantile dataset")
    clean_quantiles = _validate_quantiles(quantiles)
    if int(horizon_segments) <= 0:
        raise Phase45V3ThroughputQuantileDatasetError("horizon_segments must be positive")

    sampling = build_sampling_artifacts(phase3_manifest, profile, source_manifest_path=source_manifest_path)
    plan = dict(sampling["plan"])  # type: ignore[arg-type]
    sampling_audit = dict(sampling["audit"])  # type: ignore[arg-type]
    training_windows = _limited_windows(plan["training_windows"], max_training_windows)  # type: ignore[index]
    validation_windows = _limited_windows(plan["validation_windows"], max_validation_windows)  # type: ignore[index]
    segment_duration_s = float(plan["sampling_policy"]["segment_duration_s"])  # type: ignore[index]
    segment_count = int(plan["segment_count_per_window"])
    if ladder_factory is not None:
        # Línea MPC Prudente: ladder fiel con tamaños reales (VBR) del medio.
        ladder = ladder_factory(segment_duration_s, segment_count)
        representation_kbps = tuple(int(bitrate) // 1000 for bitrate in ladder.bitrates_bps)
    else:
        ladder = default_phase45_v3_ladder(
            segment_duration_s=segment_duration_s,
            segment_count=segment_count,
            representation_kbps=representation_kbps,
            max_buffer_s=PHASE45_V3_DEFAULT_MAX_BUFFER_S,
        )
    ladder_manifest = ladder.to_manifest() if hasattr(ladder, "to_manifest") else {}
    segment_size_source = str(ladder_manifest.get("segment_size_source", "bitrate_times_duration_bytes"))
    faithful_media_profile_id = ladder_manifest.get("media_profile_id")

    samples_by_role: dict[str, list[Mapping[str, object]]] = {TRAINING_ROLE: [], VALIDATION_ROLE: []}
    skipped_windows: list[Mapping[str, object]] = []
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
                for rollout_index in range(int(profile.rollouts_per_window)):
                    rollout_policy = THROUGHPUT_QUANTILE_ROLLOUT_POLICIES[
                        int(rollout_index) % len(THROUGHPUT_QUANTILE_ROLLOUT_POLICIES)
                    ]
                    samples_by_role[data_role].extend(
                        _samples_for_window_rollout(
                            window=window,
                            data_role=data_role,
                            loaded_trace=loaded_trace,
                            ladder=ladder,
                            rollout_policy=rollout_policy,
                            horizon_segments=int(horizon_segments),
                            quantiles=clean_quantiles,
                        )
                    )
            except Exception as exc:  # noqa: BLE001 - skipped windows are audited.
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
        raise Phase45V3ThroughputQuantileDatasetError(
            "dataset generation produced empty training or validation samples; skipped_window_count={0}".format(
                len(skipped_windows)
            )
        )

    for data_role, filename in THROUGHPUT_QUANTILE_DATA_FILENAMES.items():
        write_jsonl(output_path / filename, samples_by_role[data_role])

    generation_window_counts = {
        TRAINING_ROLE: len(training_windows),
        VALIDATION_ROLE: len(validation_windows),
    }
    leakage_audit = _build_leakage_audit(samples_by_role, skipped_windows)
    summary = _build_summary(
        output_path=output_path,
        profile=profile,
        plan=plan,
        generation_window_counts=generation_window_counts,
        samples_by_role=samples_by_role,
        skipped_windows=skipped_windows,
        path_rewrites=trace_path_rewrites,
        resolved_path_examples=resolved_path_examples,
        representation_kbps=representation_kbps,
        horizon_segments=int(horizon_segments),
        quantiles=clean_quantiles,
        leakage_audit=leakage_audit,
        segment_size_source=segment_size_source,
        media_profile_id_override=faithful_media_profile_id,
    )

    write_json(output_path / THROUGHPUT_QUANTILE_SUMMARY_FILENAME, summary)
    write_json(output_path / THROUGHPUT_QUANTILE_SAMPLING_PLAN_FILENAME, _sampling_payload(plan))
    write_json(output_path / THROUGHPUT_QUANTILE_SAMPLING_AUDIT_FILENAME, _sampling_payload(sampling_audit))
    write_json(output_path / THROUGHPUT_QUANTILE_TARGET_SCHEMA_FILENAME, _build_target_schema(int(horizon_segments), clean_quantiles))
    write_json(output_path / THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME, leakage_audit)

    status = "PASS" if leakage_audit["status"] == "PASS" else "REVIEW"
    return {
        "status": status,
        "output_dir": str(output_path),
        "profile": profile.name,
        "sample_counts": {role: len(samples_by_role[role]) for role in THROUGHPUT_QUANTILE_DATA_FILENAMES},
        "generation_window_counts": generation_window_counts,
        "skipped_window_count": len(skipped_windows),
        "benchmark_performed": False,
        "ia_training_performed": False,
        "summary": summary,
    }


def validate_phase45_v3_throughput_quantile_dataset_dir(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase45_v3 throughput quantile dataset")
    errors = []
    missing = [filename for filename in THROUGHPUT_QUANTILE_REQUIRED_DATASET_FILES if not (data_dir / filename).is_file()]
    errors.extend("missing required file: {0}".format(filename) for filename in missing)
    if missing:
        return _validation_result(data_dir, errors, 0, 0)

    summary = read_json(data_dir / THROUGHPUT_QUANTILE_SUMMARY_FILENAME)
    if summary.get("schema_id") != THROUGHPUT_QUANTILE_DATASET_SCHEMA_ID:
        errors.append("unexpected throughput quantile dataset schema_id")
    if summary.get("benchmark_performed") is not False:
        errors.append("summary benchmark_performed must be false")
    if summary.get("metadata_fields_are_model_features") is not False:
        errors.append("summary metadata_fields_are_model_features must be false")
    if summary.get("future_fields_are_model_features") is not False:
        errors.append("summary future_fields_are_model_features must be false")
    if int(summary.get("horizon_segments", 0)) <= 0:
        errors.append("summary horizon_segments must be positive")

    training_rows = list(read_jsonl(data_dir / THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME))
    validation_rows = list(read_jsonl(data_dir / THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME))
    if not training_rows:
        errors.append("training data is empty")
    if not validation_rows:
        errors.append("validation data is empty")
    errors.extend(_sample_errors(training_rows, TRAINING_ROLE))
    errors.extend(_sample_errors(validation_rows, VALIDATION_ROLE))

    leakage = read_json(data_dir / THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME)
    if leakage.get("status") != "PASS":
        errors.append("leakage audit status is not PASS")
    if leakage.get("metadata_fields_are_model_features") is not False:
        errors.append("leakage audit metadata_fields_are_model_features must be false")
    if leakage.get("eval_split_used") is not False:
        errors.append("leakage audit eval_split_used must be false")
    if leakage.get("future_throughput_as_feature") is not False:
        errors.append("leakage audit future_throughput_as_feature must be false")

    return _validation_result(data_dir, errors, len(training_rows), len(validation_rows))


def _samples_for_window_rollout(
    *,
    window: Mapping[str, object],
    data_role: str,
    loaded_trace: LoadedTrace,
    ladder,
    rollout_policy: str,
    horizon_segments: int,
    quantiles: Sequence[float],
) -> list[Mapping[str, object]]:
    network_model = TraceDrivenNetworkModel(loaded_trace, end_policy=END_POLICY_LOOP, max_loops=5)
    env = AbrClosedLoopEnv(ladder=ladder, network_model=network_model)
    samples: list[Mapping[str, object]] = []
    while not env.done:
        state = env.state
        context = dict(build_context_features(state, ladder))
        reject_forbidden_model_inputs(context)
        flatten_context_features(context)
        target = _build_target(
            loaded_trace=loaded_trace,
            network_time_s=float(state.network_time_s),
            throughput_history_bps=state.throughput_history_bps,
            segment_duration_s=float(ladder.segment_duration_s),
            horizon_segments=int(horizon_segments),
            quantiles=quantiles,
        )
        action = _select_rollout_action(
            rollout_policy=rollout_policy,
            segment_index=int(state.segment_index),
            buffer_s=float(state.buffer_s),
            throughput_history_bps=state.throughput_history_bps,
            ladder=ladder,
        )
        step = env.step(action)
        sample = {
            "schema_id": THROUGHPUT_QUANTILE_SAMPLE_SCHEMA_ID,
            "sample_id": "{0}__{1}__segment_{2:04d}".format(window["window_id"], rollout_policy, state.segment_index),
            "data_role": data_role,
            "model_inputs": {
                "context": context,
            },
            "throughput_quantile_targets": target,
            "audit": {
                "closed_loop_environment": {
                    "segment_duration_s": float(ladder.segment_duration_s),
                    "segment_count": int(ladder.segment_count),
                    "max_buffer_s": float(ladder.max_buffer_s),
                    "qoe_formula_version": REWARD_VERSION,
                },
                "rollout_policy": rollout_policy,
                "rollout_action": int(action),
                "rollout_action_is_model_target": False,
                "rollout_step": {
                    "action": int(step.action),
                    "download_time_s": round(float(step.download_time_s), 6),
                    "rebuffer_s": round(float(step.rebuffer_s), 6),
                    "buffer_s_before": round(float(step.buffer_s_before), 6),
                    "buffer_s_after": round(float(step.buffer_s_after), 6),
                    "measured_throughput_bps": round(float(step.measured_throughput_bps), 6),
                },
            },
            "metadata": _sample_metadata(window, data_role, state.segment_index, rollout_policy),
        }
        _validate_sample(sample, expected_role=data_role)
        samples.append(sample)
    return samples


def _build_target(
    *,
    loaded_trace: LoadedTrace,
    network_time_s: float,
    throughput_history_bps: Sequence[float],
    segment_duration_s: float,
    horizon_segments: int,
    quantiles: Sequence[float],
) -> Mapping[str, object]:
    base_tp = harmonic_mean_bps(throughput_history_bps, default_bps=DEFAULT_STARTUP_BASE_THROUGHPUT_BPS)
    future_bps_by_horizon = []
    target_log_ratio_by_horizon = []
    for horizon_index in range(int(horizon_segments)):
        start_s = float(network_time_s) + float(horizon_index) * float(segment_duration_s)
        future_bps = _future_weighted_mean_bps(loaded_trace, start_s, float(segment_duration_s))
        future_bps_by_horizon.append(round(future_bps, 6))
        target_log_ratio_by_horizon.append(
            round(math.log((future_bps + DEFAULT_BASE_THROUGHPUT_EPS_BPS) / (base_tp + DEFAULT_BASE_THROUGHPUT_EPS_BPS)), 9)
        )
    return {
        "target_id": THROUGHPUT_QUANTILE_TARGET_ID,
        "qoe_formula_version": REWARD_VERSION,
        "horizon_segments": int(horizon_segments),
        "quantiles": [float(value) for value in quantiles],
        "base_throughput_bps": round(float(base_tp), 6),
        "future_throughput_bps_by_horizon": future_bps_by_horizon,
        "target_log_ratio_by_horizon": target_log_ratio_by_horizon,
        "future_information_is_target_only": True,
    }


def harmonic_mean_bps(values: Sequence[float], *, default_bps: float = DEFAULT_STARTUP_BASE_THROUGHPUT_BPS) -> float:
    clean = [float(value) for value in values if math.isfinite(float(value)) and float(value) > 0.0]
    if not clean:
        return float(default_bps)
    denominator = sum(1.0 / max(value, DEFAULT_BASE_THROUGHPUT_EPS_BPS) for value in clean)
    return float(len(clean)) / max(denominator, 1.0e-12)


def _future_weighted_mean_bps(loaded_trace: LoadedTrace, start_time_s: float, duration_s: float) -> float:
    values = _weighted_future_values(loaded_trace, start_time_s, duration_s)
    if not values:
        return max(float(loaded_trace.throughput_mean_kbps), 0.0) * 1000.0
    total_weight = sum(weight for _value, weight in values)
    return sum(value * weight for value, weight in values) / max(total_weight, 1.0e-9)


def _weighted_future_values(loaded_trace: LoadedTrace, start_time_s: float, horizon_s: float) -> list[tuple[float, float]]:
    duration_s = max(float(loaded_trace.duration_s), 1.0e-9)
    remaining_s = max(float(horizon_s), 0.0)
    cursor_s = max(float(start_time_s), 0.0)
    values: list[tuple[float, float]] = []
    while remaining_s > 1.0e-9:
        local_start = cursor_s % duration_s
        local_remaining = min(remaining_s, duration_s - local_start)
        local_end = local_start + local_remaining
        for sample in loaded_trace.samples:
            sample_start = float(sample.timestamp_s)
            sample_end = sample_start + float(sample.duration_s)
            overlap_start = max(sample_start, local_start)
            overlap_end = min(sample_end, local_end)
            if overlap_end > overlap_start:
                values.append((max(float(sample.throughput_kbps), 0.0) * 1000.0, overlap_end - overlap_start))
        cursor_s += local_remaining
        remaining_s -= local_remaining
    return values


def _select_rollout_action(
    *,
    rollout_policy: str,
    segment_index: int,
    buffer_s: float,
    throughput_history_bps: Sequence[float],
    ladder,
) -> int:
    if rollout_policy == ROLLOUT_CYCLIC:
        return int(segment_index) % int(ladder.representation_count)
    base_tp = harmonic_mean_bps(throughput_history_bps)
    safe_bps = 0.85 * base_tp
    floor_action = _floor_bitrate_to_action(safe_bps, ladder)
    if rollout_policy == ROLLOUT_RATE_UP:
        return min(floor_action + 1, ladder.representation_count - 1) if float(buffer_s) >= 8.0 else floor_action
    if rollout_policy == ROLLOUT_BUFFER_SAFE:
        if float(buffer_s) < 4.0:
            return 0
        if float(buffer_s) < 8.0:
            return min(floor_action, 1)
        return floor_action
    if rollout_policy == ROLLOUT_ROBUST_RATE:
        return floor_action
    raise Phase45V3ThroughputQuantileDatasetError("unknown rollout policy: {0}".format(rollout_policy))


def _floor_bitrate_to_action(target_bps: float, ladder) -> int:
    action = 0
    for index, bitrate_bps in enumerate(ladder.bitrates_bps):
        if float(target_bps) >= float(bitrate_bps):
            action = int(index)
    return max(0, min(action, ladder.representation_count - 1))


def _validate_sample(sample: Mapping[str, object], *, expected_role: str) -> None:
    if sample.get("schema_id") != THROUGHPUT_QUANTILE_SAMPLE_SCHEMA_ID:
        raise Phase45V3ThroughputQuantileDatasetError("unexpected sample schema_id")
    if sample.get("data_role") != expected_role:
        raise Phase45V3ThroughputQuantileDatasetError("sample data_role mismatch")
    model_inputs = sample.get("model_inputs")
    if not isinstance(model_inputs, Mapping):
        raise Phase45V3ThroughputQuantileDatasetError("sample model_inputs must be an object")
    context = model_inputs.get("context")
    if not isinstance(context, Mapping):
        raise Phase45V3ThroughputQuantileDatasetError("sample context must be an object")
    reject_forbidden_model_inputs(context)
    flatten_context_features(context)
    targets = sample.get("throughput_quantile_targets")
    if not isinstance(targets, Mapping):
        raise Phase45V3ThroughputQuantileDatasetError("sample throughput_quantile_targets must be an object")
    if targets.get("target_id") != THROUGHPUT_QUANTILE_TARGET_ID:
        raise Phase45V3ThroughputQuantileDatasetError("unexpected throughput quantile target_id")
    if targets.get("future_information_is_target_only") is not True:
        raise Phase45V3ThroughputQuantileDatasetError("future throughput must be target-only")
    horizon = int(targets.get("horizon_segments", 0))
    if horizon <= 0:
        raise Phase45V3ThroughputQuantileDatasetError("horizon_segments must be positive")
    if len(targets.get("future_throughput_bps_by_horizon", [])) != horizon:  # type: ignore[arg-type]
        raise Phase45V3ThroughputQuantileDatasetError("future throughput target length mismatch")
    if len(targets.get("target_log_ratio_by_horizon", [])) != horizon:  # type: ignore[arg-type]
        raise Phase45V3ThroughputQuantileDatasetError("target log ratio length mismatch")


def _sample_errors(rows: Sequence[Mapping[str, object]], expected_role: str) -> list[str]:
    errors = []
    for index, sample in enumerate(rows[:50]):
        try:
            _validate_sample(sample, expected_role=expected_role)
        except Exception as exc:  # noqa: BLE001 - validation reports all sample shape issues.
            errors.append("{0}[{1}]: {2}".format(expected_role, index, exc))
        metadata = sample.get("metadata")
        if not isinstance(metadata, Mapping) or metadata.get("metadata_is_model_input") is not False:
            errors.append("{0}[{1}]: metadata boundary missing".format(expected_role, index))
    return errors


def _build_leakage_audit(
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    errors = []
    by_source_split: Counter[str] = Counter()
    by_rollout_policy: Counter[str] = Counter()
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
                errors.append("leakage_group selected across roles: {0}".format(group))
            source_split = str(metadata["source_split"])
            if source_split == "eval":
                errors.append("eval split used in sample: {0}".format(sample["sample_id"]))
            by_source_split[source_split] += 1
            by_rollout_policy[str(metadata.get("rollout_policy"))] += 1
    return {
        "schema_id": THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_SCHEMA_ID,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "qh_action_as_feature": False,
        "oracle_action_as_feature": False,
        "rollout_action_as_feature": False,
        "legacy_dry_runs_used": False,
        "skipped_window_count": len(skipped_windows),
        "sample_counts_by_source_split": dict(sorted(by_source_split.items())),
        "sample_counts_by_rollout_policy": dict(sorted(by_rollout_policy.items())),
    }


def _build_summary(
    *,
    output_path: Path,
    profile: Phase45V3DatasetProfile,
    plan: Mapping[str, object],
    generation_window_counts: Mapping[str, int],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
    path_rewrites: Sequence[PathRewriteRule],
    resolved_path_examples: Sequence[Mapping[str, object]],
    representation_kbps: Sequence[int],
    horizon_segments: int,
    quantiles: Sequence[float],
    leakage_audit: Mapping[str, object],
    segment_size_source: str = "bitrate_times_duration_bytes",
    media_profile_id_override: object | None = None,
) -> Mapping[str, object]:
    return {
        "schema_id": THROUGHPUT_QUANTILE_DATASET_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v3 throughput-quantile dataset for Neural MPC",
        "phase": PHASE45_V3_PHASE,
        "line_status": "qh_scorer_not_controller_driver_neural_mpc_candidate",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "source_plan_schema_id": plan.get("schema_id"),
        "media_profile_id": str(media_profile_id_override) if media_profile_id_override else MEDIA_PROFILE_ID,
        "segment_size_source": segment_size_source,
        "representation_kbps": [int(value) for value in representation_kbps],
        "segment_duration_s": float(plan["sampling_policy"]["segment_duration_s"]),  # type: ignore[index]
        "segment_count": int(plan["segment_count_per_window"]),
        "max_buffer_s": PHASE45_V3_DEFAULT_MAX_BUFFER_S,
        "horizon_segments": int(horizon_segments),
        "quantiles": [float(value) for value in quantiles],
        "target_source": "future normalized trace throughput, target-only",
        "model_inputs_source": "runtime-visible context features only",
        "files": {filename: filename for filename in THROUGHPUT_QUANTILE_DATA_FILENAMES.values()},
        "required_files": list(THROUGHPUT_QUANTILE_REQUIRED_DATASET_FILES),
        "generation_window_counts": dict(generation_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in THROUGHPUT_QUANTILE_DATA_FILENAMES},
        "rollout_policy_role": "state_coverage_only_not_model_target",
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "normalization_fitted_on": TRAINING_ROLE,
        "trace_path_rewrites": [rule.to_json() for rule in path_rewrites],
        "resolved_path_examples": list(resolved_path_examples),
        "skipped_windows": list(skipped_windows),
        "leakage_audit_status": leakage_audit.get("status"),
        **no_benchmark_policy(),
    }


def _build_target_schema(horizon_segments: int, quantiles: Sequence[float]) -> Mapping[str, object]:
    return {
        "schema_id": THROUGHPUT_QUANTILE_TARGET_SCHEMA_ID,
        "target_id": THROUGHPUT_QUANTILE_TARGET_ID,
        "qoe_formula_version": REWARD_VERSION,
        "horizon_segments": int(horizon_segments),
        "quantiles": [float(value) for value in quantiles],
        "target_fields": [
            "base_throughput_bps",
            "future_throughput_bps_by_horizon",
            "target_log_ratio_by_horizon",
            "future_information_is_target_only",
        ],
        "model_must_not_use_target_fields_as_inputs": True,
    }


def _sample_metadata(
    window: Mapping[str, object],
    data_role: str,
    segment_index: int,
    rollout_policy: str,
) -> Mapping[str, object]:
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
        "rollout_policy": rollout_policy,
        "synthetic": bool(window.get("synthetic") is True),
        "throughput_bucket": str(window.get("throughput_bucket", "")),
        "variability_bucket": str(window.get("variability_bucket", "")),
        "network_condition": str(window.get("network_condition", "unknown")),
    }


def _sampling_payload(payload: Mapping[str, object]) -> Mapping[str, object]:
    updated = dict(payload)
    updated["used_by_phase45_v3_throughput_quantile_dataset"] = True
    updated["model_feature_fields"] = []
    updated["metadata_fields_are_model_features"] = False
    return updated


def _validation_result(
    data_dir: Path,
    errors: list[str],
    training_sample_count: int,
    validation_sample_count: int,
) -> Mapping[str, object]:
    return {
        "status": "PASS" if not errors else "FAIL",
        "dataset_dir": str(data_dir),
        "errors": errors,
        "training_sample_count": int(training_sample_count),
        "validation_sample_count": int(validation_sample_count),
    }


def _validate_quantiles(values: Sequence[float]) -> tuple[float, ...]:
    quantiles = tuple(float(value) for value in values)
    if not quantiles:
        raise Phase45V3ThroughputQuantileDatasetError("quantiles must not be empty")
    if any(not math.isfinite(value) or value <= 0.0 or value >= 1.0 for value in quantiles):
        raise Phase45V3ThroughputQuantileDatasetError("quantiles must be finite values in (0, 1)")
    if tuple(sorted(quantiles)) != quantiles:
        raise Phase45V3ThroughputQuantileDatasetError("quantiles must be sorted")
    return quantiles


def _limited_windows(raw_windows: object, limit: int | None) -> list[Mapping[str, object]]:
    if not isinstance(raw_windows, list):
        raise Phase45V3ThroughputQuantileDatasetError("sampling plan windows must be a list")
    windows = []
    for index, window in enumerate(raw_windows):
        if not isinstance(window, Mapping):
            raise Phase45V3ThroughputQuantileDatasetError("window {0} must be an object".format(index))
        windows.append(window)
    if limit is not None:
        return windows[: int(limit)]
    return windows
