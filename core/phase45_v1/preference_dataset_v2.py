from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import torch

from core.neural_abr.action_mask import lowest_valid_action
from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, read_jsonl, write_json, write_jsonl
from core.neural_abr.content_ladder import default_training_ladder
from core.neural_abr.features import build_candidate_features, build_context_features
from core.neural_abr.replay_environment import TraceReplayEnvironment
from core.phase45_v1.constants import (
    DATA_ROLES,
    MEDIA_PROFILE_ID,
    ORACLE_POLICY_ID,
    PHASE45_V1_PHASE,
    REWARD_VERSION,
    SPBC_CHECKPOINT_SCHEMA_ID,
    TRAINING_ROLE,
    VALIDATION_ROLE,
    no_benchmark_policy,
)
from core.phase45_v1.dataset import _limited_windows, load_trace_window
from core.phase45_v1.normalization import build_train_only_normalization
from core.phase45_v1.oracle import OracleConfig, linear_reward_for_state, select_oracle_action, simulate_step_from_state
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.profiles import DatasetProfile
from core.phase45_v1.sample_schema import Phase45SampleSchemaError, reject_forbidden_model_inputs
from core.phase45_v1.sampling import build_sampling_artifacts
from core.phase45_v1.spbc_training import CANDIDATE_FEATURES, SCALAR_FEATURES, SEQUENCE_FEATURES, SpbcAbrV1Policy


PHASE45_V2_PHASE = "fase_4_5_v1_bloque7a_dataset_v2_preference_onpolicy"
V2_DATASET_SCHEMA_ID = "phase45_v2_preference_onpolicy_dataset_v1"
V2_DAGGER2_DATASET_SCHEMA_ID = "phase45_v2_preference_onpolicy_dagger2_dataset_v1"
V2_SAMPLE_SCHEMA_ID = "phase45_v2_preference_onpolicy_sample_v1"
V2_TARGET_SCHEMA_ID = "phase45_v2_preference_onpolicy_targets_v1"
V2_LEAKAGE_AUDIT_SCHEMA_ID = "phase45_v2_no_contamination_audit_v1"
V2_PREFERENCE_AUDIT_SCHEMA_ID = "phase45_v2_preference_audit_v1"
SUPPORTED_V2_DATASET_SCHEMA_IDS = frozenset((V2_DATASET_SCHEMA_ID, V2_DAGGER2_DATASET_SCHEMA_ID))

V2_TRAINING_DATA_FILENAME = "datos_entrenamiento_preference_onpolicy_v2.jsonl"
V2_VALIDATION_DATA_FILENAME = "datos_validacion_preference_onpolicy_v2.jsonl"
V2_SUMMARY_FILENAME = "resumen_dataset_phase45_v2.json"
V2_SAMPLING_PLAN_FILENAME = "plan_muestreo_phase45_v2.json"
V2_SAMPLING_AUDIT_FILENAME = "auditoria_muestreo_phase45_v2.json"
V2_FEATURE_SCHEMA_FILENAME = "esquema_model_inputs_phase45_v2.json"
V2_TARGET_SCHEMA_FILENAME = "esquema_targets_phase45_v2.json"
V2_LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion_phase45_v2.json"
V2_NORMALIZATION_STATS_FILENAME = "estadisticas_normalizacion_train_only_phase45_v2.json"
V2_PREFERENCE_AUDIT_FILENAME = "auditoria_preferencias_phase45_v2.json"

V2_DATA_FILENAMES = {
    TRAINING_ROLE: V2_TRAINING_DATA_FILENAME,
    VALIDATION_ROLE: V2_VALIDATION_DATA_FILENAME,
}
V2_REQUIRED_DATASET_FILES = (
    V2_SUMMARY_FILENAME,
    V2_TRAINING_DATA_FILENAME,
    V2_VALIDATION_DATA_FILENAME,
    V2_SAMPLING_PLAN_FILENAME,
    V2_SAMPLING_AUDIT_FILENAME,
    V2_FEATURE_SCHEMA_FILENAME,
    V2_TARGET_SCHEMA_FILENAME,
    V2_LEAKAGE_AUDIT_FILENAME,
    V2_NORMALIZATION_STATS_FILENAME,
    V2_PREFERENCE_AUDIT_FILENAME,
)
ROLLOUT_ORACLE = "oracle_rollout"
ROLLOUT_SPBC = "spbc_v1_on_policy"
ROLLOUT_SPBC_V2_DPO = "spbc_v2_dpo_on_policy"
ROLLOUT_SOURCES = (ROLLOUT_ORACLE, ROLLOUT_SPBC, ROLLOUT_SPBC_V2_DPO)

SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID = "phase45_v2_spbc_dpo_checkpoint_v1"
SPBC_V2_DPO_MODEL_KEY = "spbc_abr_v2_dpo"

UNDER_AGGRESSIVE_QOE_GAP_THRESHOLD = 0.25
UNNECESSARY_SWITCH_SMOOTHNESS_THRESHOLD_MBPS = 0.45
UNNECESSARY_SWITCH_QOE_GAP_THRESHOLD = 0.10
REWARD_TIE_QOE_GAP_THRESHOLD = 0.10


class Phase45V2DatasetBuildError(ValueError):
    """Raised when the Phase 4-5 v2 preference dataset cannot be built safely."""


class Phase45V2DatasetValidationError(ValueError):
    """Raised when a Phase 4-5 v2 dataset directory violates its contract."""


@dataclass(frozen=True)
class LoadedRolloutPolicy:
    model: torch.nn.Module
    normalization: Mapping[str, object]
    checkpoint_path: Path
    checkpoint_sha256: str
    device: torch.device
    model_key: str
    rollout_source: str


def build_phase45_v2_dataset(
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
    spbc_checkpoint: object | None = None,
    extra_policy_rollout_checkpoint: object | None = None,
    extra_policy_rollout_source: str = ROLLOUT_SPBC_V2_DPO,
    dataset_schema_id: str = V2_DATASET_SCHEMA_ID,
    allow_oracle_only_full: bool = False,
    device: str = "auto",
) -> Mapping[str, object]:
    if dataset_schema_id not in SUPPORTED_V2_DATASET_SCHEMA_IDS:
        raise Phase45V2DatasetBuildError("unsupported v2 dataset schema_id: {0}".format(dataset_schema_id))
    if extra_policy_rollout_source not in ROLLOUT_SOURCES or extra_policy_rollout_source == ROLLOUT_ORACLE:
        raise Phase45V2DatasetBuildError("invalid extra policy rollout_source: {0}".format(extra_policy_rollout_source))
    spbc_runtime = _load_optional_spbc_runtime(
        spbc_checkpoint,
        profile=profile,
        allow_oracle_only_full=allow_oracle_only_full,
        device=device,
    )
    extra_policy_runtime = _load_optional_v2_dpo_runtime(
        extra_policy_rollout_checkpoint,
        rollout_source=extra_policy_rollout_source,
        device=device,
    )
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v2 preference dataset")
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
                samples_by_role[data_role].extend(
                    _samples_for_window(
                        window=window,
                        data_role=data_role,
                        loaded_trace=loaded_trace,
                        ladder=ladder,
                        oracle_config=oracle_config,
                        rollout_source=ROLLOUT_ORACLE,
                        policy_runtime=None,
                    )
                )
                if spbc_runtime is not None:
                    samples_by_role[data_role].extend(
                        _samples_for_window(
                            window=window,
                            data_role=data_role,
                            loaded_trace=loaded_trace,
                            ladder=ladder,
                            oracle_config=oracle_config,
                            rollout_source=ROLLOUT_SPBC,
                            policy_runtime=spbc_runtime,
                        )
                    )
                if extra_policy_runtime is not None:
                    samples_by_role[data_role].extend(
                        _samples_for_window(
                            window=window,
                            data_role=data_role,
                            loaded_trace=loaded_trace,
                            ladder=ladder,
                            oracle_config=oracle_config,
                            rollout_source=extra_policy_runtime.rollout_source,
                            policy_runtime=extra_policy_runtime,
                        )
                    )
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
        raise Phase45V2DatasetBuildError(
            "v2 generation produced empty training or validation samples; skipped_window_count={0}".format(
                len(skipped_windows)
            )
        )

    for data_role, filename in V2_DATA_FILENAMES.items():
        write_jsonl(output_path / filename, samples_by_role[data_role])

    generation_window_counts = {
        TRAINING_ROLE: len(training_windows),
        VALIDATION_ROLE: len(validation_windows),
    }
    normalization = build_train_only_normalization(samples_by_role[TRAINING_ROLE])
    leakage_audit = _build_leakage_audit(samples_by_role, skipped_windows)
    preference_audit = _build_preference_audit(samples_by_role)
    summary = _build_summary(
        output_path=output_path,
        profile=profile,
        plan=plan,
        generation_window_counts=generation_window_counts,
        samples_by_role=samples_by_role,
        skipped_windows=skipped_windows,
        path_rewrites=trace_path_rewrites,
        resolved_path_examples=resolved_path_examples,
        spbc_runtime=spbc_runtime,
        extra_policy_runtime=extra_policy_runtime,
        dataset_schema_id=dataset_schema_id,
        allow_oracle_only_full=allow_oracle_only_full,
        ladder_manifest=ladder.to_manifest(),
    )

    write_json(output_path / V2_SUMMARY_FILENAME, summary)
    write_json(output_path / V2_SAMPLING_PLAN_FILENAME, plan)
    write_json(output_path / V2_SAMPLING_AUDIT_FILENAME, sampling_audit)
    write_json(output_path / V2_FEATURE_SCHEMA_FILENAME, _build_feature_schema())
    write_json(output_path / V2_TARGET_SCHEMA_FILENAME, _build_target_schema())
    write_json(output_path / V2_LEAKAGE_AUDIT_FILENAME, leakage_audit)
    write_json(output_path / V2_NORMALIZATION_STATS_FILENAME, normalization)
    write_json(output_path / V2_PREFERENCE_AUDIT_FILENAME, preference_audit)

    return {
        "status": "PASS",
        "output_dir": str(output_path),
        "profile": profile.name,
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "generation_window_counts": generation_window_counts,
        "rollout_sources": sorted(preference_audit["sample_counts_by_rollout_source"]),
        "spbc_on_policy_enabled": spbc_runtime is not None,
        "extra_policy_on_policy_enabled": extra_policy_runtime is not None,
        "spbc_v2_dpo_on_policy_enabled": extra_policy_runtime is not None
        and extra_policy_runtime.model_key == SPBC_V2_DPO_MODEL_KEY,
        "skipped_window_count": len(skipped_windows),
        "benchmark_performed": False,
        "ia_training_performed": False,
        "summary": summary,
    }


def validate_phase45_v2_dataset_dir(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase45_v2 preference dataset")
    missing_files = [filename for filename in V2_REQUIRED_DATASET_FILES if not (data_dir / filename).is_file()]
    if missing_files:
        raise Phase45V2DatasetValidationError("missing required v2 dataset files: {0}".format(", ".join(missing_files)))

    summary = read_json(data_dir / V2_SUMMARY_FILENAME)
    if summary.get("schema_id") not in SUPPORTED_V2_DATASET_SCHEMA_IDS:
        raise Phase45V2DatasetValidationError("unexpected v2 dataset summary schema_id")
    _assert_no_benchmark(summary)

    validation_errors: list[str] = []
    sample_counts: dict[str, int] = {}
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    rollout_counts: Counter[str] = Counter()
    pair_source_counts: Counter[str] = Counter()
    error_label_counts: Counter[str] = Counter()
    source_split_counts: Counter[str] = Counter()

    for role in DATA_ROLES:
        rows = read_jsonl(data_dir / V2_DATA_FILENAMES[role])
        sample_counts[role] = len(rows)
        if not rows:
            validation_errors.append("{0} JSONL is empty".format(role))
        for index, sample in enumerate(rows, start=1):
            try:
                validate_v2_sample(sample, expected_role=role)
            except Phase45V2DatasetValidationError as exc:
                validation_errors.append("{0} row {1}: {2}".format(role, index, exc))
                continue
            metadata = _require_mapping(sample["metadata"], "metadata")
            trace_id = str(metadata["trace_id"])
            previous_trace_role = trace_roles.setdefault(trace_id, role)
            if previous_trace_role != role:
                validation_errors.append("trace_id appears in multiple roles: {0}".format(trace_id))
            leakage_group = str(metadata["leakage_group"])
            previous_group_role = leakage_group_roles.setdefault(leakage_group, role)
            if previous_group_role != role:
                validation_errors.append("leakage_group appears in multiple roles: {0}".format(leakage_group))
            source_split = str(metadata["source_split"])
            if source_split == "eval":
                validation_errors.append("eval source split appears in sample: {0}".format(sample["sample_id"]))
            source_split_counts[source_split] += 1
            rollout_counts[str(sample["rollout_source"])] += 1
            for pair in sample["preference_pairs"]:
                pair_source_counts[str(pair["preference_source"])] += 1
            for outcome in sample["per_action_outcomes"]:
                if outcome.get("over_aggressive_rebuffer") is True:
                    error_label_counts["over_aggressive_rebuffer"] += 1
                if outcome.get("under_aggressive_qoe_loss") is True:
                    error_label_counts["under_aggressive_qoe_loss"] += 1
                if outcome.get("unnecessary_switch") is True:
                    error_label_counts["unnecessary_switch"] += 1

    leakage_audit = read_json(data_dir / V2_LEAKAGE_AUDIT_FILENAME)
    normalization = read_json(data_dir / V2_NORMALIZATION_STATS_FILENAME)
    preference_audit = read_json(data_dir / V2_PREFERENCE_AUDIT_FILENAME)
    if leakage_audit.get("status") != "PASS":
        validation_errors.append("v2 leakage audit status is not PASS")
    if normalization.get("fitted_on_data_role") != TRAINING_ROLE:
        validation_errors.append("v2 normalization is not fitted on training only")
    if preference_audit.get("status") != "PASS":
        validation_errors.append("v2 preference audit status is not PASS")

    expected_counts = summary.get("sample_counts")
    if isinstance(expected_counts, Mapping):
        for role, count in sample_counts.items():
            if int(expected_counts.get(role, -1)) != count:
                validation_errors.append("{0} sample count mismatch with v2 summary".format(role))

    if validation_errors:
        raise Phase45V2DatasetValidationError("; ".join(validation_errors[:10]))

    return {
        "status": "PASS",
        "dataset_dir": str(data_dir),
        "schema_id": str(summary.get("schema_id")),
        "sample_counts": sample_counts,
        "rollout_source_counts": dict(sorted(rollout_counts.items())),
        "preference_pair_source_counts": dict(sorted(pair_source_counts.items())),
        "error_label_counts": dict(sorted(error_label_counts.items())),
        "source_split_counts": dict(sorted(source_split_counts.items())),
        "training_role": TRAINING_ROLE,
        "validation_role": VALIDATION_ROLE,
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_action_as_feature": False,
        **no_benchmark_policy(),
    }


def validate_v2_sample(sample: Mapping[str, object], expected_role: str | None = None) -> None:
    if sample.get("schema_id") != V2_SAMPLE_SCHEMA_ID:
        raise Phase45V2DatasetValidationError("unexpected v2 sample schema_id")
    if expected_role is not None and sample.get("data_role") != expected_role:
        raise Phase45V2DatasetValidationError("v2 sample data_role mismatch")
    for field in (
        "sample_id",
        "data_role",
        "rollout_source",
        "state_origin_action",
        "model_inputs",
        "target_id",
        "oracle_action",
        "best_immediate_action",
        "oracle_vs_immediate_disagreement",
        "per_action_outcomes",
        "preference_pairs",
        "metadata",
    ):
        if field not in sample:
            raise Phase45V2DatasetValidationError("v2 sample missing {0}".format(field))
    if sample.get("target_id") != V2_TARGET_SCHEMA_ID:
        raise Phase45V2DatasetValidationError("v2 target_id mismatch")
    rollout_source = str(sample["rollout_source"])
    if rollout_source not in ROLLOUT_SOURCES:
        raise Phase45V2DatasetValidationError("invalid rollout_source")

    model_inputs = _require_mapping(sample["model_inputs"], "model_inputs")
    try:
        reject_forbidden_model_inputs(model_inputs)
    except Phase45SampleSchemaError as exc:
        raise Phase45V2DatasetValidationError(str(exc)) from exc
    candidates = model_inputs.get("candidates")
    action_mask = model_inputs.get("action_mask")
    if not isinstance(candidates, list) or not candidates:
        raise Phase45V2DatasetValidationError("model_inputs.candidates must be a non-empty list")
    if not isinstance(action_mask, list) or len(action_mask) != len(candidates):
        raise Phase45V2DatasetValidationError("action_mask length must match candidates")
    if not any(bool(value) for value in action_mask):
        raise Phase45V2DatasetValidationError("action_mask must contain a valid action")

    outcomes = sample["per_action_outcomes"]
    if not isinstance(outcomes, list) or len(outcomes) != len(candidates):
        raise Phase45V2DatasetValidationError("per_action_outcomes length must match candidates")
    oracle_action = _finite_int(sample["oracle_action"], "oracle_action")
    best_immediate_action = _finite_int(sample["best_immediate_action"], "best_immediate_action")
    if not _action_valid(oracle_action, action_mask):
        raise Phase45V2DatasetValidationError("oracle_action is not valid")
    if not _action_valid(best_immediate_action, action_mask):
        raise Phase45V2DatasetValidationError("best_immediate_action is not valid")

    valid_actions: set[int] = set()
    for index, outcome in enumerate(outcomes):
        mapping = _require_mapping(outcome, "per_action_outcomes[{0}]".format(index))
        action = _finite_int(mapping.get("action"), "outcome action")
        if action != index:
            raise Phase45V2DatasetValidationError("outcome action must be aligned with candidate index")
        if bool(mapping.get("valid_action")):
            valid_actions.add(action)
            for name in ("reward_n", "qoe_gap", "estimated_rebuffer_s", "smoothness_mbps", "bitrate_kbps"):
                _finite_float(mapping.get(name), name)
            if float(mapping["qoe_gap"]) < -1e-9:
                raise Phase45V2DatasetValidationError("qoe_gap must be non-negative")

    pairs = sample["preference_pairs"]
    if not isinstance(pairs, list) or not pairs:
        raise Phase45V2DatasetValidationError("preference_pairs must be a non-empty list")
    for index, pair in enumerate(pairs):
        mapping = _require_mapping(pair, "preference_pairs[{0}]".format(index))
        preferred = _finite_int(mapping.get("preferred_action"), "preferred_action")
        rejected = _finite_int(mapping.get("rejected_action"), "rejected_action")
        if preferred == rejected:
            raise Phase45V2DatasetValidationError("preference pair has identical actions")
        if preferred not in valid_actions or rejected not in valid_actions:
            raise Phase45V2DatasetValidationError("preference pair references invalid action")
        _finite_float(mapping.get("reward_gap"), "pair reward_gap")
        _finite_float(mapping.get("qoe_gap"), "pair qoe_gap")
        if not str(mapping.get("preference_source", "")).strip():
            raise Phase45V2DatasetValidationError("preference_source must not be empty")

    metadata = _require_mapping(sample["metadata"], "metadata")
    if metadata.get("metadata_is_model_input") is not False:
        raise Phase45V2DatasetValidationError("metadata_is_model_input must be false")
    if str(metadata.get("source_split")) == "eval":
        raise Phase45V2DatasetValidationError("eval split sample is forbidden")


def _samples_for_window(
    *,
    window: Mapping[str, object],
    data_role: str,
    loaded_trace,
    ladder,
    oracle_config: OracleConfig,
    rollout_source: str,
    policy_runtime: LoadedRolloutPolicy | None,
) -> list[Mapping[str, object]]:
    env = TraceReplayEnvironment(loaded_trace, ladder)
    samples: list[Mapping[str, object]] = []
    state_origin_action: int | None = None
    while not env.done:
        state = env.state
        action_mask = env.action_mask()
        context = build_context_features(state, ladder)
        candidates = build_candidate_features(ladder, state.segment_index, float(context["last_bitrate_bps"]))
        model_inputs = {
            "context": dict(context),
            "candidates": [dict(candidate) for candidate in candidates],
            "action_mask": [bool(value) for value in action_mask],
        }
        policy_action = _select_policy_action(policy_runtime, model_inputs) if policy_runtime is not None else None
        oracle_decision = select_oracle_action(state, ladder, env.network_model, oracle_config)
        per_action_outcomes = _build_per_action_outcomes(
            state=state,
            ladder=ladder,
            network_model=env.network_model,
            action_mask=action_mask,
            oracle_action=oracle_decision.action,
        )
        best_immediate_action = _best_immediate_action(per_action_outcomes)
        preference_pairs = _build_preference_pairs(
            outcomes=per_action_outcomes,
            oracle_action=oracle_decision.action,
            best_immediate_action=best_immediate_action,
            policy_action=policy_action,
            rollout_source=rollout_source,
        )
        selected_action = int(oracle_decision.action if rollout_source == ROLLOUT_ORACLE else policy_action)
        if not _action_valid(selected_action, action_mask):
            selected_action = lowest_valid_action(action_mask)
        step = env.step(selected_action)
        sample = {
            "schema_id": V2_SAMPLE_SCHEMA_ID,
            "sample_id": "{0}__{1}__segment_{2:04d}".format(window["window_id"], rollout_source, state.segment_index),
            "data_role": data_role,
            "rollout_source": rollout_source,
            "state_origin_action": state_origin_action,
            "model_inputs": model_inputs,
            "target_id": V2_TARGET_SCHEMA_ID,
            "qoe_formula_version": REWARD_VERSION,
            "oracle_policy_id": ORACLE_POLICY_ID,
            "oracle_action": int(oracle_decision.action),
            "oracle_horizon_reward_n": float(oracle_decision.horizon_reward_n),
            "oracle_first_step_reward_n": float(oracle_decision.first_step_reward_n),
            "oracle_best_sequence": list(oracle_decision.best_sequence),
            "best_immediate_action": int(best_immediate_action),
            "oracle_vs_immediate_disagreement": int(oracle_decision.action) != int(best_immediate_action),
            "spbc_policy_action": policy_action if rollout_source == ROLLOUT_SPBC else None,
            "rollout_policy_action": policy_action,
            "rollout_policy_model_key": policy_runtime.model_key if policy_runtime is not None else None,
            "per_action_outcomes": per_action_outcomes,
            "preference_pairs": preference_pairs,
            "audit": {
                "rollout_selected_action": int(selected_action),
                "oracle": oracle_decision.to_json(),
                "selected_step": {
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
        validate_v2_sample(sample, expected_role=data_role)
        samples.append(sample)
        state_origin_action = int(selected_action)
    return samples


def _build_per_action_outcomes(
    *,
    state,
    ladder,
    network_model,
    action_mask: Sequence[bool],
    oracle_action: int,
) -> list[Mapping[str, object]]:
    raw_outcomes: list[dict[str, object]] = []
    valid_rewards = []
    for action, allowed in enumerate(action_mask):
        bitrate_kbps = float(ladder.bitrate_bps(action)) / 1000.0
        previous_bitrate_bps = float(ladder.bitrate_bps(state.last_representation_index)) if state.last_representation_index >= 0 else 0.0
        smoothness_mbps = abs(float(ladder.bitrate_bps(action)) - previous_bitrate_bps) / 1_000_000.0 if previous_bitrate_bps > 0.0 else 0.0
        if not allowed:
            raw_outcomes.append(
                {
                    "action": int(action),
                    "valid_action": False,
                    "bitrate_kbps": round(bitrate_kbps, 6),
                    "reward_n": None,
                    "qoe_gap": None,
                    "oracle_immediate_reward_gap": None,
                    "estimated_download_time_s": None,
                    "estimated_rebuffer_s": None,
                    "smoothness_mbps": round(smoothness_mbps, 6),
                    "over_aggressive_rebuffer": False,
                    "under_aggressive_qoe_loss": False,
                    "unnecessary_switch": False,
                }
            )
            continue
        next_state, step = simulate_step_from_state(state, ladder, network_model, action)
        reward_n = linear_reward_for_state(state, ladder, action, step.rebuffer_s)
        raw = {
            "action": int(action),
            "valid_action": True,
            "bitrate_kbps": round(bitrate_kbps, 6),
            "reward_n": round(float(reward_n), 6),
            "qoe_gap": 0.0,
            "oracle_immediate_reward_gap": 0.0,
            "estimated_download_time_s": round(float(step.download_time_s), 6),
            "estimated_rebuffer_s": round(float(step.rebuffer_s), 6),
            "smoothness_mbps": round(float(smoothness_mbps), 6),
            "next_buffer_s": round(float(next_state.buffer_s), 6),
        }
        raw_outcomes.append(raw)
        valid_rewards.append((int(action), float(reward_n)))
    if not valid_rewards:
        raise Phase45V2DatasetBuildError("cannot build action surface with no valid rewards")
    best_reward = max(reward for _action, reward in valid_rewards)
    oracle_reward = _reward_for_action(raw_outcomes, oracle_action)
    for outcome in raw_outcomes:
        if outcome.get("valid_action") is not True:
            continue
        action = int(outcome["action"])
        reward = float(outcome["reward_n"])
        qoe_gap = max(best_reward - reward, 0.0)
        outcome["qoe_gap"] = round(qoe_gap, 6)
        outcome["oracle_immediate_reward_gap"] = round(float(oracle_reward) - reward, 6)
        outcome["over_aggressive_rebuffer"] = bool(action > int(oracle_action) and float(outcome["estimated_rebuffer_s"]) > 0.0)
        outcome["under_aggressive_qoe_loss"] = bool(
            action < int(oracle_action) and qoe_gap > UNDER_AGGRESSIVE_QOE_GAP_THRESHOLD
        )
        outcome["unnecessary_switch"] = bool(
            float(outcome["smoothness_mbps"]) >= UNNECESSARY_SWITCH_SMOOTHNESS_THRESHOLD_MBPS
            and qoe_gap <= UNNECESSARY_SWITCH_QOE_GAP_THRESHOLD
        )
    return raw_outcomes


def _build_preference_pairs(
    *,
    outcomes: Sequence[Mapping[str, object]],
    oracle_action: int,
    best_immediate_action: int,
    policy_action: int | None,
    rollout_source: str,
) -> list[Mapping[str, object]]:
    pairs: list[Mapping[str, object]] = []
    seen: set[tuple[str, int, int]] = set()

    def add(source: str, preferred: int, rejected: int) -> None:
        if preferred == rejected or not _outcome_valid(outcomes, preferred) or not _outcome_valid(outcomes, rejected):
            return
        key = (source, int(preferred), int(rejected))
        if key in seen:
            return
        seen.add(key)
        preferred_reward = _reward_for_action(outcomes, preferred)
        rejected_reward = _reward_for_action(outcomes, rejected)
        rejected_gap = _qoe_gap_for_action(outcomes, rejected)
        pairs.append(
            {
                "preference_source": source,
                "preferred_action": int(preferred),
                "rejected_action": int(rejected),
                "reward_gap": round(float(preferred_reward) - float(rejected_reward), 6),
                "qoe_gap": round(float(rejected_gap), 6),
            }
        )

    if policy_action is not None and int(policy_action) != int(oracle_action):
        source = "oracle_vs_spbc_policy" if rollout_source == ROLLOUT_SPBC else "oracle_vs_rollout_policy"
        add(source, int(oracle_action), int(policy_action))

    valid = [outcome for outcome in outcomes if outcome.get("valid_action") is True]
    if valid:
        best = max(valid, key=lambda item: (float(item["reward_n"]), -float(item["estimated_rebuffer_s"]), -float(item["smoothness_mbps"]), -int(item["action"])))
        worst = min(valid, key=lambda item: (float(item["reward_n"]), -float(item["estimated_rebuffer_s"]), -float(item["smoothness_mbps"]), -int(item["action"])))
        add("best_reward_vs_worst_valid", int(best["action"]), int(worst["action"]))

    safe = [item for item in valid if float(item["estimated_rebuffer_s"]) <= 0.0]
    rebuffer = [item for item in valid if float(item["estimated_rebuffer_s"]) > 0.0]
    if safe and rebuffer:
        preferred = max(safe, key=lambda item: float(item["reward_n"]))
        rejected = min(rebuffer, key=lambda item: float(item["reward_n"]))
        add("safe_vs_rebuffer", int(preferred["action"]), int(rejected["action"]))

    over_aggressive = [item for item in valid if item.get("over_aggressive_rebuffer") is True]
    if over_aggressive:
        rejected = min(over_aggressive, key=lambda item: float(item["reward_n"]))
        add("best_reward_vs_over_aggressive", int(best_immediate_action), int(rejected["action"]))

    close_reward = [item for item in valid if float(item["qoe_gap"]) <= REWARD_TIE_QOE_GAP_THRESHOLD]
    if len(close_reward) >= 2:
        smoothest = min(close_reward, key=lambda item: (float(item["smoothness_mbps"]), -float(item["reward_n"]), int(item["action"])))
        roughest = max(close_reward, key=lambda item: (float(item["smoothness_mbps"]), -float(item["reward_n"]), int(item["action"])))
        add("smoothness_tiebreak_when_reward_close", int(smoothest["action"]), int(roughest["action"]))

    if not pairs and valid:
        fallback = int(valid[0]["action"])
        for item in valid[1:]:
            if int(item["action"]) != fallback:
                add("fallback_valid_distinction", fallback, int(item["action"]))
                break
    return pairs


def _best_immediate_action(outcomes: Sequence[Mapping[str, object]]) -> int:
    valid = [outcome for outcome in outcomes if outcome.get("valid_action") is True]
    if not valid:
        raise Phase45V2DatasetBuildError("cannot select best immediate action with no valid outcomes")
    best = max(
        valid,
        key=lambda item: (
            float(item["reward_n"]),
            -float(item["estimated_rebuffer_s"]),
            -float(item["smoothness_mbps"]),
            -int(item["action"]),
        ),
    )
    return int(best["action"])


def _load_optional_spbc_runtime(
    path: object | None,
    *,
    profile: DatasetProfile,
    allow_oracle_only_full: bool,
    device: str,
) -> LoadedRolloutPolicy | None:
    if path is None:
        if profile.name == "full_v1" and not allow_oracle_only_full:
            raise Phase45V2DatasetBuildError("full_v1 requires --spbc-checkpoint or --allow-oracle-only-full")
        return None
    checkpoint_path = Path(path).expanduser()
    if not checkpoint_path.is_file():
        if profile.name == "full_v1" and not allow_oracle_only_full:
            raise Phase45V2DatasetBuildError(
                "full_v1 requires an existing spbc_v1 checkpoint; missing: {0}".format(checkpoint_path)
            )
        return None
    selected_device = _resolve_torch_device(device)
    try:
        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
    if not isinstance(checkpoint, Mapping):
        raise Phase45V2DatasetBuildError("spbc checkpoint must contain a mapping: {0}".format(checkpoint_path))
    if checkpoint.get("schema_id") != SPBC_CHECKPOINT_SCHEMA_ID or checkpoint.get("model_key") != "spbc_abr_v1":
        raise Phase45V2DatasetBuildError("spbc checkpoint schema/model_key mismatch: {0}".format(checkpoint_path))
    config = _require_mapping(checkpoint.get("model_config"), "spbc model_config")
    model = SpbcAbrV1Policy(
        history_hidden_size=int(config["history_hidden_size"]),
        state_hidden_size=int(config["state_hidden_size"]),
        candidate_hidden_size=int(config["candidate_hidden_size"]),
        shared_hidden_size=int(config["shared_hidden_size"]),
        dropout=float(config["dropout"]),
    )
    state_dict = checkpoint.get("model_state_dict")
    if not isinstance(state_dict, Mapping):
        raise Phase45V2DatasetBuildError("spbc checkpoint missing model_state_dict")
    model.load_state_dict(state_dict)
    model.to(selected_device)
    model.eval()
    normalization = _require_mapping(checkpoint.get("normalization"), "spbc normalization")
    return LoadedRolloutPolicy(
        model=model,
        normalization=normalization,
        checkpoint_path=checkpoint_path,
        checkpoint_sha256=_sha256_file(checkpoint_path),
        device=selected_device,
        model_key="spbc_abr_v1",
        rollout_source=ROLLOUT_SPBC,
    )


def _load_optional_v2_dpo_runtime(
    path: object | None,
    *,
    rollout_source: str,
    device: str,
) -> LoadedRolloutPolicy | None:
    if path is None:
        return None
    checkpoint_path = Path(path).expanduser()
    if not checkpoint_path.is_file():
        raise Phase45V2DatasetBuildError("extra policy rollout checkpoint is missing: {0}".format(checkpoint_path))
    selected_device = _resolve_torch_device(device)
    try:
        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
    if not isinstance(checkpoint, Mapping):
        raise Phase45V2DatasetBuildError("extra policy checkpoint must contain a mapping: {0}".format(checkpoint_path))
    if checkpoint.get("schema_id") != SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID or checkpoint.get("model_key") != SPBC_V2_DPO_MODEL_KEY:
        raise Phase45V2DatasetBuildError("extra policy checkpoint schema/model_key mismatch: {0}".format(checkpoint_path))

    from core.phase45_v1.spbc_v2_dpo_training import SpbcAbrV2DpoPolicy

    config = _require_mapping(checkpoint.get("model_config"), "extra policy model_config")
    model = SpbcAbrV2DpoPolicy(
        history_hidden_size=int(config["history_hidden_size"]),
        state_hidden_size=int(config["state_hidden_size"]),
        candidate_hidden_size=int(config["candidate_hidden_size"]),
        shared_hidden_size=int(config["shared_hidden_size"]),
        dropout=float(config["dropout"]),
        decision_reward_fusion_weight=float(config.get("decision_reward_fusion_weight", 0.12)),
        decision_rebuffer_fusion_weight=float(config.get("decision_rebuffer_fusion_weight", 0.30)),
        decision_risk_fusion_weight=float(config.get("decision_risk_fusion_weight", 0.18)),
        rebuffer_prediction_cap_s=float(config.get("rebuffer_prediction_cap_s", 4.0)),
    )
    state_dict = checkpoint.get("model_state_dict")
    if not isinstance(state_dict, Mapping):
        raise Phase45V2DatasetBuildError("extra policy checkpoint missing model_state_dict")
    model.load_state_dict(state_dict)
    model.to(selected_device)
    model.eval()
    normalization = _require_mapping(checkpoint.get("normalization"), "extra policy normalization")
    return LoadedRolloutPolicy(
        model=model,
        normalization=normalization,
        checkpoint_path=checkpoint_path,
        checkpoint_sha256=_sha256_file(checkpoint_path),
        device=selected_device,
        model_key=SPBC_V2_DPO_MODEL_KEY,
        rollout_source=rollout_source,
    )


def _select_policy_action(runtime: LoadedRolloutPolicy | None, model_inputs: Mapping[str, object]) -> int | None:
    if runtime is None:
        return None
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidates_raw = model_inputs.get("candidates")
    action_mask_raw = model_inputs.get("action_mask")
    if not isinstance(candidates_raw, list) or not isinstance(action_mask_raw, list):
        raise Phase45V2DatasetBuildError("policy rollout inference requires candidates and action_mask lists")
    sequence = _sequence_from_context(context)
    scalars = tuple(_finite_float(context.get(name), name) for name in SCALAR_FEATURES)
    candidates = tuple(
        tuple(_finite_float(_require_mapping(candidate, "candidate").get(name), name) for name in CANDIDATE_FEATURES)
        for candidate in candidates_raw
    )
    action_mask = tuple(bool(value) for value in action_mask_raw)
    normalization = runtime.normalization
    tensors = (
        torch.tensor([_normalize_matrix(sequence, normalization["sequence_mean"], normalization["sequence_std"])], dtype=torch.float32, device=runtime.device),
        torch.tensor([_normalize_vector(scalars, normalization["scalar_mean"], normalization["scalar_std"])], dtype=torch.float32, device=runtime.device),
        torch.tensor([[_normalize_vector(candidate, normalization["candidate_mean"], normalization["candidate_std"]) for candidate in candidates]], dtype=torch.float32, device=runtime.device),
        torch.tensor([action_mask], dtype=torch.bool, device=runtime.device),
    )
    with torch.no_grad():
        logits = runtime.model(*tensors)["action_logits"]
        action = int(torch.argmax(logits, dim=1).detach().cpu().item())
    return action if _action_valid(action, action_mask) else lowest_valid_action(action_mask)


def _build_feature_schema() -> Mapping[str, object]:
    from core.phase45_v1.sample_schema import build_model_input_schema

    schema = dict(build_model_input_schema())
    schema["schema_id"] = "phase45_v2_model_inputs_schema_v1"
    schema["human_readable_name"] = "Phase 4-5 v2 safe model inputs for preference/on-policy dataset"
    return schema


def _build_target_schema() -> Mapping[str, object]:
    return {
        "schema_id": V2_TARGET_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v2 preference/on-policy targets",
        "qoe_formula_version": REWARD_VERSION,
        "oracle_policy_id": ORACLE_POLICY_ID,
        "target_fields": [
            "oracle_action",
            "best_immediate_action",
            "oracle_vs_immediate_disagreement",
            "per_action_outcomes",
            "preference_pairs",
        ],
        "per_action_outcome_fields": [
            "reward_n",
            "qoe_gap",
            "oracle_immediate_reward_gap",
            "estimated_rebuffer_s",
            "smoothness_mbps",
            "bitrate_kbps",
            "valid_action",
        ],
        "preference_pair_sources": [
            "oracle_vs_spbc_policy",
            "oracle_vs_rollout_policy",
            "best_reward_vs_worst_valid",
            "safe_vs_rebuffer",
            "best_reward_vs_over_aggressive",
            "smoothness_tiebreak_when_reward_close",
        ],
        "diagnostic_error_thresholds": {
            "under_aggressive_qoe_gap_threshold": UNDER_AGGRESSIVE_QOE_GAP_THRESHOLD,
            "unnecessary_switch_smoothness_threshold_mbps": UNNECESSARY_SWITCH_SMOOTHNESS_THRESHOLD_MBPS,
            "unnecessary_switch_qoe_gap_threshold": UNNECESSARY_SWITCH_QOE_GAP_THRESHOLD,
            "reward_tie_qoe_gap_threshold": REWARD_TIE_QOE_GAP_THRESHOLD,
        },
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
    }


def _build_summary(
    *,
    output_path: Path,
    profile: DatasetProfile,
    plan: Mapping[str, object],
    generation_window_counts: Mapping[str, int],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
    path_rewrites: Sequence[PathRewriteRule],
    resolved_path_examples: Sequence[Mapping[str, object]],
    spbc_runtime: LoadedRolloutPolicy | None,
    extra_policy_runtime: LoadedRolloutPolicy | None,
    dataset_schema_id: str,
    allow_oracle_only_full: bool,
    ladder_manifest: Mapping[str, object],
) -> Mapping[str, object]:
    rollout_counts = Counter(str(sample["rollout_source"]) for samples in samples_by_role.values() for sample in samples)
    policy_rollouts = [
        {
            "rollout_source": runtime.rollout_source,
            "model_key": runtime.model_key,
            "checkpoint": str(runtime.checkpoint_path),
            "checkpoint_sha256": runtime.checkpoint_sha256,
        }
        for runtime in (spbc_runtime, extra_policy_runtime)
        if runtime is not None
    ]
    return {
        "schema_id": dataset_schema_id,
        "human_readable_name": "Phase 4-5 v2 preference/on-policy dataset for ABR candidates",
        "phase": PHASE45_V2_PHASE,
        "parent_phase": PHASE45_V1_PHASE,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "source_plan_schema_id": plan.get("schema_id"),
        "media_profile_id": MEDIA_PROFILE_ID,
        "content_ladder": dict(ladder_manifest),
        "files": {filename: filename for filename in V2_DATA_FILENAMES.values()},
        "required_files": list(V2_REQUIRED_DATASET_FILES),
        "generation_window_counts": dict(generation_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "sample_counts_by_rollout_source": dict(sorted(rollout_counts.items())),
        "spbc_on_policy_enabled": spbc_runtime is not None,
        "spbc_checkpoint": str(spbc_runtime.checkpoint_path) if spbc_runtime is not None else None,
        "spbc_checkpoint_sha256": spbc_runtime.checkpoint_sha256 if spbc_runtime is not None else None,
        "extra_policy_on_policy_enabled": extra_policy_runtime is not None,
        "spbc_v2_dpo_on_policy_enabled": extra_policy_runtime is not None
        and extra_policy_runtime.model_key == SPBC_V2_DPO_MODEL_KEY,
        "policy_rollouts": policy_rollouts,
        "dagger_iteration": 2 if extra_policy_runtime is not None else 1,
        "allow_oracle_only_full": bool(allow_oracle_only_full),
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
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
    by_rollout: Counter[str] = Counter()
    by_synthetic: Counter[str] = Counter()
    for role, samples in samples_by_role.items():
        for sample in samples:
            metadata = _require_mapping(sample["metadata"], "metadata")
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
                errors.append("eval split used in v2 sample: {0}".format(sample["sample_id"]))
            by_source_split[source_split] += 1
            by_rollout[str(sample["rollout_source"])] += 1
            by_synthetic[str(bool(metadata.get("synthetic")))] += 1
    return {
        "schema_id": V2_LEAKAGE_AUDIT_SCHEMA_ID,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "oracle_action_as_feature": False,
        "spbc_policy_action_as_feature": False,
        "rollout_policy_action_as_feature": False,
        "skipped_window_count": len(skipped_windows),
        "sample_counts_by_source_split": dict(sorted(by_source_split.items())),
        "sample_counts_by_rollout_source": dict(sorted(by_rollout.items())),
        "sample_counts_by_synthetic": dict(sorted(by_synthetic.items())),
    }


def _build_preference_audit(samples_by_role: Mapping[str, Sequence[Mapping[str, object]]]) -> Mapping[str, object]:
    by_role: dict[str, int] = {}
    by_rollout: Counter[str] = Counter()
    by_bucket: Counter[str] = Counter()
    by_pair_source: Counter[str] = Counter()
    by_error_label: Counter[str] = Counter()
    pair_count = 0
    samples_without_pairs = 0
    for role, samples in samples_by_role.items():
        by_role[role] = len(samples)
        for sample in samples:
            by_rollout[str(sample["rollout_source"])] += 1
            metadata = _require_mapping(sample["metadata"], "metadata")
            by_bucket[str(metadata.get("throughput_bucket", "unknown"))] += 1
            pairs = sample["preference_pairs"]
            if not pairs:
                samples_without_pairs += 1
            for pair in pairs:
                pair_count += 1
                by_pair_source[str(pair["preference_source"])] += 1
            for outcome in sample["per_action_outcomes"]:
                if outcome.get("over_aggressive_rebuffer") is True:
                    by_error_label["over_aggressive_rebuffer"] += 1
                if outcome.get("under_aggressive_qoe_loss") is True:
                    by_error_label["under_aggressive_qoe_loss"] += 1
                if outcome.get("unnecessary_switch") is True:
                    by_error_label["unnecessary_switch"] += 1
    errors = []
    if pair_count <= 0:
        errors.append("no preference pairs generated")
    if samples_without_pairs:
        errors.append("samples without preference pairs: {0}".format(samples_without_pairs))
    return {
        "schema_id": V2_PREFERENCE_AUDIT_SCHEMA_ID,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "sample_counts_by_role": dict(sorted(by_role.items())),
        "sample_counts_by_rollout_source": dict(sorted(by_rollout.items())),
        "sample_counts_by_throughput_bucket": dict(sorted(by_bucket.items())),
        "preference_pair_count": pair_count,
        "preference_pair_counts_by_source": dict(sorted(by_pair_source.items())),
        "diagnostic_error_label_counts": dict(sorted(by_error_label.items())),
        "metadata_fields_are_model_features": False,
        "target_fields_are_model_features": False,
        **no_benchmark_policy(),
    }


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


def _sequence_from_context(context: Mapping[str, object]) -> tuple[tuple[float, float], ...]:
    throughput = _numeric_sequence(context.get(SEQUENCE_FEATURES[0]), SEQUENCE_FEATURES[0])
    download = _numeric_sequence(context.get(SEQUENCE_FEATURES[1]), SEQUENCE_FEATURES[1])
    if len(throughput) != len(download):
        raise Phase45V2DatasetBuildError("history feature lengths differ")
    return tuple((throughput[index], download[index]) for index in range(len(throughput)))


def _numeric_sequence(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise Phase45V2DatasetBuildError("{0} must be a sequence".format(name))
    return tuple(_finite_float(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _normalize_vector(values: Sequence[float], mean: object, std: object) -> list[float]:
    mean_values = _numeric_tuple(mean, "normalization mean")
    std_values = _numeric_tuple(std, "normalization std")
    if len(values) != len(mean_values) or len(mean_values) != len(std_values):
        raise Phase45V2DatasetBuildError("normalization vector width mismatch")
    return [(float(value) - mean_values[index]) / max(std_values[index], 1.0e-12) for index, value in enumerate(values)]


def _normalize_matrix(values: Sequence[Sequence[float]], mean: object, std: object) -> list[list[float]]:
    return [_normalize_vector(row, mean, std) for row in values]


def _numeric_tuple(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise Phase45V2DatasetBuildError("{0} must be a numeric list".format(name))
    return tuple(_finite_float(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _outcome_valid(outcomes: Sequence[Mapping[str, object]], action: int) -> bool:
    return 0 <= int(action) < len(outcomes) and outcomes[int(action)].get("valid_action") is True


def _reward_for_action(outcomes: Sequence[Mapping[str, object]], action: int) -> float:
    if not _outcome_valid(outcomes, action):
        raise Phase45V2DatasetBuildError("cannot read reward for invalid action: {0}".format(action))
    return _finite_float(outcomes[int(action)].get("reward_n"), "reward_n")


def _qoe_gap_for_action(outcomes: Sequence[Mapping[str, object]], action: int) -> float:
    if not _outcome_valid(outcomes, action):
        raise Phase45V2DatasetBuildError("cannot read qoe_gap for invalid action: {0}".format(action))
    return _finite_float(outcomes[int(action)].get("qoe_gap"), "qoe_gap")


def _action_valid(action: int, action_mask: Sequence[object]) -> bool:
    return 0 <= int(action) < len(action_mask) and bool(action_mask[int(action)])


def _finite_int(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise Phase45V2DatasetValidationError("{0} must be an integer".format(name))
    return int(value)


def _finite_float(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise Phase45V2DatasetValidationError("{0} must be numeric".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise Phase45V2DatasetValidationError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(parsed):
        raise Phase45V2DatasetValidationError("{0} must be finite".format(name))
    return parsed


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise Phase45V2DatasetValidationError("{0} must be an object".format(name))
    return value


def _resolve_torch_device(requested: str) -> torch.device:
    key = str(requested).strip().lower()
    if key == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if key == "cuda" and not torch.cuda.is_available():
        raise Phase45V2DatasetBuildError("CUDA/ROCm device requested but torch.cuda.is_available() is false")
    if key not in {"cpu", "cuda"}:
        raise Phase45V2DatasetBuildError("device must be cpu, cuda or auto")
    return torch.device(key)


def _assert_no_benchmark(mapping: Mapping[str, object]) -> None:
    for flag, expected in no_benchmark_policy().items():
        if mapping.get(flag) is not expected:
            raise Phase45V2DatasetValidationError("{0} must be {1}".format(flag, expected))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_phase3_manifest(path: object) -> Mapping[str, object]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)
