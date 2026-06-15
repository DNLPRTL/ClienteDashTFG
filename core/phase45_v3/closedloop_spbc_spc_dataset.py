from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, read_jsonl, write_json, write_jsonl
from core.neural_abr.features import audit_feature_payload, build_feature_schema
from core.phase45_v1.dataset import load_trace_window
from core.phase45_v1.normalization import build_train_only_normalization
from core.phase45_v1.paths import PathRewriteRule, resolve_external_trace_path
from core.phase45_v1.sampling import build_sampling_artifacts
from core.phase45_v3.abr_closed_loop_env import PHASE45_V3_DEFAULT_MAX_BUFFER_S, default_phase45_v3_ladder
from core.phase45_v3.constants import (
    DATA_ROLES,
    MEDIA_PROFILE_ID,
    NORMALIZATION_SCHEMA_ID,
    REWARD_VERSION,
    TRAINING_ROLE,
    VALIDATION_ROLE,
    no_benchmark_policy,
)
from core.phase45_v3.dataset import (
    _closed_loop_environment_contract_from_manifest,
    _limited_windows,
    _rollout_policy_for_index,
    _samples_for_window_rollout,
)
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.qh_oracle import PHASE45_V3_QH_ORACLE_ID, QhOracleConfig, qh_oracle_card


SPBC_SPC_DATASET_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_dataset_v1"
SPBC_SPC_SAMPLE_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_sample_v1"
SPBC_POLICY_TARGET_ID = "phase45_v3_closedloop_spbc_policy_targets_v1"
SPC_CRITIC_TARGET_ID = "phase45_v3_closedloop_spc_critic_targets_v1"
SPBC_SPC_FEATURE_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_model_inputs_schema_v1"
SPBC_SPC_TARGET_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_targets_schema_v1"
SPBC_SPC_LEAKAGE_AUDIT_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_no_contamination_audit_v1"
SPBC_SPC_TARGET_AUDIT_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_target_audit_v1"
SPBC_SPC_NORMALIZATION_SCHEMA_ID = "phase45_v3_closedloop_spbc_spc_normalization_stats_v1"

SPBC_SPC_PHASE = "fase_4_5_v3_closedloop_spbc_spc_dataset"
SPBC_SPC_TRAINING_DATA_FILENAME = "datos_entrenamiento_phase45_v3_closedloop_spbc_spc.jsonl"
SPBC_SPC_VALIDATION_DATA_FILENAME = "datos_validacion_phase45_v3_closedloop_spbc_spc.jsonl"
SPBC_SPC_SUMMARY_FILENAME = "resumen_dataset_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_SAMPLING_PLAN_FILENAME = "plan_muestreo_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_SAMPLING_AUDIT_FILENAME = "auditoria_muestreo_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_FEATURE_SCHEMA_FILENAME = "esquema_model_inputs_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_TARGET_SCHEMA_FILENAME = "esquema_targets_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_NORMALIZATION_STATS_FILENAME = "estadisticas_normalizacion_train_only_phase45_v3_closedloop_spbc_spc.json"
SPBC_SPC_TARGET_AUDIT_FILENAME = "auditoria_targets_phase45_v3_closedloop_spbc_spc.json"

SPBC_SPC_DATA_FILENAMES = {
    TRAINING_ROLE: SPBC_SPC_TRAINING_DATA_FILENAME,
    VALIDATION_ROLE: SPBC_SPC_VALIDATION_DATA_FILENAME,
}
SPBC_SPC_REQUIRED_DATASET_FILES = (
    SPBC_SPC_SUMMARY_FILENAME,
    SPBC_SPC_TRAINING_DATA_FILENAME,
    SPBC_SPC_VALIDATION_DATA_FILENAME,
    SPBC_SPC_SAMPLING_PLAN_FILENAME,
    SPBC_SPC_SAMPLING_AUDIT_FILENAME,
    SPBC_SPC_FEATURE_SCHEMA_FILENAME,
    SPBC_SPC_TARGET_SCHEMA_FILENAME,
    SPBC_SPC_LEAKAGE_AUDIT_FILENAME,
    SPBC_SPC_NORMALIZATION_STATS_FILENAME,
    SPBC_SPC_TARGET_AUDIT_FILENAME,
)

SOFT_POLICY_TEMPERATURE = 0.35
SAFE_REGRET_N = 0.35
CATASTROPHIC_REGRET_N = 2.0
RISK_REGRET_CAP_N = 4.0
RISK_REBUFFER_CAP_S = 4.0


class Phase45V3ClosedLoopSpbcSpcDatasetError(ValueError):
    """Raised when the closed-loop SPBC/SPC dataset cannot be built safely."""


def build_phase45_v3_closedloop_spbc_spc_dataset(
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
) -> Mapping[str, object]:
    """Build a closed-loop policy/critic dataset from Phase 3 trace windows.

    The generator reuses the Phase45 v3 client-parity environment and Q_H oracle
    as a target factory, but writes a separate SPBC/SPC schema so the new line is
    not tied to old Phase45 v1/v2 SPBC artifacts.
    """

    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 closed-loop SPBC/SPC dataset")
    sampling = build_sampling_artifacts(phase3_manifest, profile, source_manifest_path=source_manifest_path)
    plan = dict(sampling["plan"])  # type: ignore[arg-type]
    sampling_audit = dict(sampling["audit"])  # type: ignore[arg-type]
    training_windows = _limited_windows(plan["training_windows"], max_training_windows)  # type: ignore[index]
    validation_windows = _limited_windows(plan["validation_windows"], max_validation_windows)  # type: ignore[index]
    segment_duration_s = float(plan["sampling_policy"]["segment_duration_s"])  # type: ignore[index]
    segment_count = int(plan["segment_count_per_window"])
    ladder = default_phase45_v3_ladder(
        segment_duration_s=segment_duration_s,
        segment_count=segment_count,
        representation_kbps=representation_kbps,
        max_buffer_s=PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    )
    qh_config = QhOracleConfig(
        horizon_segments=int(profile.qh_horizon_segments),
        beam_width=int(profile.qh_beam_width),
    )

    samples_by_role: dict[str, list[Mapping[str, object]]] = {TRAINING_ROLE: [], VALIDATION_ROLE: []}
    skipped_windows: list[Mapping[str, object]] = []
    target_events: list[Mapping[str, object]] = []
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
                    rollout_policy = _rollout_policy_for_index(rollout_index)
                    qh_samples, qh_events = _samples_for_window_rollout(
                        window=window,
                        data_role=data_role,
                        loaded_trace=loaded_trace,
                        ladder=ladder,
                        qh_config=qh_config,
                        rollout_policy=rollout_policy,
                    )
                    transformed = [_transform_qh_sample(sample) for sample in qh_samples]
                    for sample in transformed:
                        _validate_spbc_spc_sample(sample, expected_role=data_role)
                    samples_by_role[data_role].extend(transformed)
                    target_events.extend(qh_events)
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
        raise Phase45V3ClosedLoopSpbcSpcDatasetError(
            "dataset generation produced empty training or validation samples; skipped_window_count={0}".format(
                len(skipped_windows)
            )
        )

    for data_role, filename in SPBC_SPC_DATA_FILENAMES.items():
        write_jsonl(output_path / filename, samples_by_role[data_role])

    generation_window_counts = {
        TRAINING_ROLE: len(training_windows),
        VALIDATION_ROLE: len(validation_windows),
    }
    leakage_audit = _build_spbc_spc_leakage_audit(samples_by_role, skipped_windows)
    target_audit = _build_spbc_spc_target_audit(target_events, samples_by_role, ladder.max_bitrate_bps / 1000.0)
    normalization = dict(build_train_only_normalization(samples_by_role[TRAINING_ROLE]))
    normalization["schema_id"] = SPBC_SPC_NORMALIZATION_SCHEMA_ID
    normalization["source_schema_id"] = NORMALIZATION_SCHEMA_ID
    summary = _build_spbc_spc_summary(
        output_path=output_path,
        profile=profile,
        plan=plan,
        ladder_manifest=ladder.to_manifest(),
        generation_window_counts=generation_window_counts,
        samples_by_role=samples_by_role,
        skipped_windows=skipped_windows,
        path_rewrites=trace_path_rewrites,
        resolved_path_examples=resolved_path_examples,
        qh_config=qh_config,
        leakage_audit=leakage_audit,
        target_audit=target_audit,
    )

    write_json(output_path / SPBC_SPC_SUMMARY_FILENAME, summary)
    write_json(output_path / SPBC_SPC_SAMPLING_PLAN_FILENAME, _spbc_spc_sampling_payload(plan))
    write_json(output_path / SPBC_SPC_SAMPLING_AUDIT_FILENAME, _spbc_spc_sampling_payload(sampling_audit))
    write_json(output_path / SPBC_SPC_FEATURE_SCHEMA_FILENAME, _build_spbc_spc_feature_schema())
    write_json(output_path / SPBC_SPC_TARGET_SCHEMA_FILENAME, _build_spbc_spc_target_schema())
    write_json(output_path / SPBC_SPC_LEAKAGE_AUDIT_FILENAME, leakage_audit)
    write_json(output_path / SPBC_SPC_NORMALIZATION_STATS_FILENAME, normalization)
    write_json(output_path / SPBC_SPC_TARGET_AUDIT_FILENAME, target_audit)

    status = "PASS" if leakage_audit["status"] == "PASS" and target_audit["status"] == "PASS" else "REVIEW"
    return {
        "status": status,
        "output_dir": str(output_path),
        "profile": profile.name,
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "generation_window_counts": generation_window_counts,
        "skipped_window_count": len(skipped_windows),
        "benchmark_performed": False,
        "ia_training_performed": False,
        "summary": summary,
    }


def validate_phase45_v3_closedloop_spbc_spc_dataset_dir(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase45_v3 closed-loop SPBC/SPC dataset")
    errors = []
    missing = [filename for filename in SPBC_SPC_REQUIRED_DATASET_FILES if not (data_dir / filename).is_file()]
    errors.extend("missing required file: {0}".format(filename) for filename in missing)
    if missing:
        return _validation_result(data_dir, errors, 0, 0)

    summary = read_json(data_dir / SPBC_SPC_SUMMARY_FILENAME)
    if summary.get("schema_id") != SPBC_SPC_DATASET_SCHEMA_ID:
        errors.append("unexpected dataset summary schema_id")
    if summary.get("benchmark_performed") is not False:
        errors.append("summary benchmark_performed must be false")
    if summary.get("metadata_fields_are_model_features") is not False:
        errors.append("summary metadata_fields_are_model_features must be false")
    if summary.get("future_fields_are_model_features") is not False:
        errors.append("summary future_fields_are_model_features must be false")
    if summary.get("neural_mpc_line_modified") is not False:
        errors.append("summary neural_mpc_line_modified must be false")
    content_ladder = summary.get("content_ladder")
    if not isinstance(content_ladder, Mapping) or float(content_ladder.get("max_buffer_s", 0.0)) != 60.0:
        errors.append("content_ladder max_buffer_s must be 60.0 for Phase45 v3")

    training_rows = list(read_jsonl(data_dir / SPBC_SPC_TRAINING_DATA_FILENAME))
    validation_rows = list(read_jsonl(data_dir / SPBC_SPC_VALIDATION_DATA_FILENAME))
    if not training_rows:
        errors.append("training data is empty")
    if not validation_rows:
        errors.append("validation data is empty")
    errors.extend(_sample_errors(training_rows, TRAINING_ROLE))
    errors.extend(_sample_errors(validation_rows, VALIDATION_ROLE))

    leakage = read_json(data_dir / SPBC_SPC_LEAKAGE_AUDIT_FILENAME)
    if leakage.get("status") != "PASS":
        errors.append("leakage audit status is not PASS")
    if leakage.get("metadata_fields_are_model_features") is not False:
        errors.append("leakage audit metadata_fields_are_model_features must be false")
    if leakage.get("eval_split_used") is not False:
        errors.append("leakage audit eval_split_used must be false")

    target_audit = read_json(data_dir / SPBC_SPC_TARGET_AUDIT_FILENAME)
    if target_audit.get("status") != "PASS":
        errors.append("target audit status is not PASS: {0}".format(target_audit.get("errors")))
    if target_audit.get("future_information_is_target_only") is not True:
        errors.append("target audit must mark future information as target-only")

    return _validation_result(data_dir, errors, len(training_rows), len(validation_rows))


def summarize_phase45_v3_closedloop_spbc_spc_dataset(dataset_dir: object) -> Mapping[str, object]:
    root = Path(dataset_dir).expanduser()
    validation = validate_phase45_v3_closedloop_spbc_spc_dataset_dir(root)
    summary = read_json(root / SPBC_SPC_SUMMARY_FILENAME)
    leakage = read_json(root / SPBC_SPC_LEAKAGE_AUDIT_FILENAME)
    target_audit = read_json(root / SPBC_SPC_TARGET_AUDIT_FILENAME)
    profile = summary.get("profile", {}) if isinstance(summary.get("profile"), Mapping) else {}
    content_ladder = summary.get("content_ladder", {}) if isinstance(summary.get("content_ladder"), Mapping) else {}
    return {
        "status": "PASS"
        if validation["status"] == "PASS" and leakage.get("status") == "PASS" and target_audit.get("status") == "PASS"
        else "FAIL",
        "dataset_dir": str(root),
        "profile": profile.get("name") if isinstance(profile, Mapping) else "",
        "rollouts_per_window": profile.get("rollouts_per_window") if isinstance(profile, Mapping) else None,
        "sample_counts": summary.get("sample_counts", {}),
        "generation_window_counts": summary.get("generation_window_counts", {}),
        "max_buffer_s": content_ladder.get("max_buffer_s") if isinstance(content_ladder, Mapping) else None,
        "validation_status": validation["status"],
        "leakage_status": leakage.get("status"),
        "target_status": target_audit.get("status"),
        "skipped_window_count": len(summary.get("skipped_windows", [])) if isinstance(summary.get("skipped_windows"), list) else None,
        "fallback_count": target_audit.get("fallback_count"),
        "target_action0_rate": target_audit.get("target_action0_rate"),
        "high_capacity_safe_state_count": target_audit.get("high_capacity_safe_state_count"),
        "high_capacity_safe_target_action0_rate": target_audit.get("high_capacity_safe_target_action0_rate"),
        "policy_target_distribution": target_audit.get("policy_target_distribution", {}),
        "rollout_policy_distribution": target_audit.get("rollout_policy_distribution", {}),
        "safe_action_presence_rate": target_audit.get("safe_action_presence_rate"),
        "catastrophic_action_fraction": target_audit.get("catastrophic_action_fraction"),
        "mean_best_q_h_reward_n": target_audit.get("mean_best_q_h_reward_n"),
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
    }


def load_phase3_manifest(path: object) -> Mapping[str, object]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_default_phase45_v3_closedloop_spbc_spc_trace_path_rewrites(tfg_root: object) -> tuple[PathRewriteRule, ...]:
    root = Path(tfg_root).expanduser()
    return (
        PathRewriteRule("/home/daniel/TFG", str(root)),
        PathRewriteRule("/home/danie/TFG", str(root)),
        PathRewriteRule("C:/Users/danie/Documents/TFG", str(root)),
        PathRewriteRule("C:\\Users\\danie\\Documents\\TFG", str(root)),
    )


def resolve_phase45_v3_closedloop_spbc_spc_trace_path(raw_path: object, rules: Sequence[PathRewriteRule]) -> Path:
    return resolve_external_trace_path(raw_path, rules)


def _transform_qh_sample(qh_sample: Mapping[str, object]) -> Mapping[str, object]:
    qh_targets = _require_mapping(qh_sample.get("qh_targets"), "qh_targets")
    model_inputs = _require_mapping(qh_sample.get("model_inputs"), "model_inputs")
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidates = _require_list(model_inputs.get("candidates"), "model_inputs.candidates")
    action_mask = [bool(value) for value in _require_list(model_inputs.get("action_mask"), "model_inputs.action_mask")]
    action_values = _require_list(qh_targets.get("action_values"), "qh_targets.action_values")
    selected_action = int(qh_targets.get("selected_action", -1))
    selected_value = _value_for_action(action_values, selected_action)
    best_q = _finite_float(selected_value.get("q_h_reward_n"), "selected_q_h_reward_n")
    augmented_values = [
        _build_augmented_action_value(value, candidates, context, best_q, selected_action)
        for value in action_values
    ]
    soft_weights = _soft_policy_weights(augmented_values)
    policy_targets = {
        "target_id": SPBC_POLICY_TARGET_ID,
        "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "selected_action": selected_action,
        "selected_q_h_reward_n": round(best_q, 6),
        "selected_best_sequence": list(selected_value.get("best_sequence", [])),
        "one_hot_action": [1.0 if index == selected_action else 0.0 for index in range(len(action_values))],
        "soft_action_weights": soft_weights,
        "q_h_regret_by_action_n": [value["q_h_regret_n"] for value in augmented_values],
        "action_mask": action_mask,
        "future_information_is_target_only": True,
    }
    critic_targets = {
        "target_id": SPC_CRITIC_TARGET_ID,
        "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "best_action": selected_action,
        "best_q_h_reward_n": round(best_q, 6),
        "action_values": augmented_values,
        "risk_definition_id": "bounded_0_1_from_qh_regret_and_horizon_rebuffer_v1",
        "safe_regret_n": SAFE_REGRET_N,
        "catastrophic_regret_n": CATASTROPHIC_REGRET_N,
        "future_information_is_target_only": True,
    }
    audit = dict(_require_mapping(qh_sample.get("audit"), "audit"))
    audit.update(
        {
            "source_qh_sample_schema_id": qh_sample.get("schema_id"),
            "source_qh_sample_id": qh_sample.get("sample_id"),
            "source_qh_targets_target_id": qh_targets.get("target_id"),
            "source_qh_oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
            "policy_targets_are_model_inputs": False,
            "critic_targets_are_model_inputs": False,
            "future_information_is_target_only": True,
            "neural_mpc_line_modified": False,
        }
    )
    metadata = dict(_require_mapping(qh_sample.get("metadata"), "metadata"))
    metadata["source_qh_sample_id"] = str(qh_sample.get("sample_id"))
    metadata["metadata_is_model_input"] = False
    sample = {
        "schema_id": SPBC_SPC_SAMPLE_SCHEMA_ID,
        "sample_id": "spbc_spc__{0}".format(qh_sample.get("sample_id")),
        "data_role": qh_sample.get("data_role"),
        "model_inputs": model_inputs,
        "spbc_policy_targets": policy_targets,
        "spc_critic_targets": critic_targets,
        "audit": audit,
        "metadata": metadata,
    }
    return sample


def _build_augmented_action_value(
    value: object,
    candidates: Sequence[object],
    context: Mapping[str, object],
    best_q: float,
    selected_action: int,
) -> Mapping[str, object]:
    row = _require_mapping(value, "action_value")
    action = int(row.get("action", -1))
    feasible = bool(row.get("feasible"))
    candidate = _require_mapping(candidates[action], "candidate") if 0 <= action < len(candidates) else {}
    q_h = _optional_finite_float(row.get("q_h_reward_n"))
    first_reward = _optional_finite_float(row.get("first_step_reward_n"))
    total_rebuffer = _optional_finite_float(row.get("total_rebuffer_s"))
    candidate_bitrate_bps = _optional_finite_float(candidate.get("candidate_bitrate_bps")) or 0.0
    last_bitrate_bps = _optional_finite_float(context.get("last_bitrate_bps")) or 0.0
    first_quality_mbps = candidate_bitrate_bps / 1_000_000.0
    first_smoothness_mbps = (
        abs(candidate_bitrate_bps - last_bitrate_bps) / 1_000_000.0
        if last_bitrate_bps > 0.0
        else 0.0
    )
    first_rebuffer = _derive_first_step_rebuffer_s(first_quality_mbps, first_smoothness_mbps, first_reward)
    regret = None if q_h is None else round(max(float(best_q) - float(q_h), 0.0), 6)
    target_risk = _target_risk(regret, total_rebuffer) if feasible else 1.0
    return {
        "action": action,
        "feasible": feasible,
        "q_h_reward_n": _round_optional(q_h),
        "first_step_reward_n": _round_optional(first_reward),
        "first_step_quality_mbps": round(first_quality_mbps, 6),
        "first_step_smoothness_mbps": round(max(first_smoothness_mbps, 0.0), 6),
        "first_step_rebuffer_s": _round_optional(first_rebuffer),
        "total_rebuffer_s": _round_optional(total_rebuffer),
        "q_h_regret_n": regret,
        "q_h_advantage_n": None if q_h is None else round(float(q_h) - float(best_q), 6),
        "target_risk": round(float(target_risk), 6),
        "switch_count": int(row.get("switch_count", 0)),
        "best_sequence": list(row.get("best_sequence", [])),
        "horizon_segments_evaluated": int(row.get("horizon_segments_evaluated", 0)),
        "evaluated_sequence_count": int(row.get("evaluated_sequence_count", 0)),
        "is_best_action": action == int(selected_action),
        "is_safe_regret_0_35": bool(feasible and regret is not None and float(regret) <= SAFE_REGRET_N),
        "is_catastrophic_regret_2": bool((not feasible) or (regret is not None and float(regret) >= CATASTROPHIC_REGRET_N)),
        "reason": str(row.get("reason", "")),
    }


def _build_spbc_spc_summary(
    *,
    output_path: Path,
    profile: Phase45V3DatasetProfile,
    plan: Mapping[str, object],
    ladder_manifest: Mapping[str, object],
    generation_window_counts: Mapping[str, int],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
    path_rewrites: Sequence[PathRewriteRule],
    resolved_path_examples: Sequence[Mapping[str, object]],
    qh_config: QhOracleConfig,
    leakage_audit: Mapping[str, object],
    target_audit: Mapping[str, object],
) -> Mapping[str, object]:
    return {
        "schema_id": SPBC_SPC_DATASET_SCHEMA_ID,
        "human_readable_name": "Phase45 v3 closed-loop SPBC/SPC policy and critic dataset",
        "phase": SPBC_SPC_PHASE,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "source_plan_schema_id": plan.get("schema_id"),
        "phase45_v1_sampler_reused_for_balanced_trace_windows": True,
        "source_qh_oracle_used_as_label_factory": True,
        "source_qh_oracle_policy": qh_oracle_card(qh_config),
        "media_profile_id": MEDIA_PROFILE_ID,
        "content_ladder": dict(ladder_manifest),
        "files": {filename: filename for filename in SPBC_SPC_DATA_FILENAMES.values()},
        "required_files": list(SPBC_SPC_REQUIRED_DATASET_FILES),
        "generation_window_counts": dict(generation_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "policy_target_id": SPBC_POLICY_TARGET_ID,
        "critic_target_id": SPC_CRITIC_TARGET_ID,
        "rollout_policy_role": "state_coverage_only_not_primary_target",
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "target_fields_are_model_features": False,
        "normalization_fitted_on": TRAINING_ROLE,
        "closed_loop_client_parity": _closed_loop_environment_contract_from_manifest(ladder_manifest),
        "neural_mpc_line_modified": False,
        "trace_path_rewrites": [rule.to_json() for rule in path_rewrites],
        "resolved_path_examples": list(resolved_path_examples),
        "skipped_windows": list(skipped_windows),
        "leakage_audit_status": leakage_audit.get("status"),
        "target_audit_status": target_audit.get("status"),
        **no_benchmark_policy(),
    }


def _build_spbc_spc_leakage_audit(
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    skipped_windows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    errors = []
    by_source_split: Counter[str] = Counter()
    by_synthetic: Counter[str] = Counter()
    by_rollout_policy: Counter[str] = Counter()
    for role, samples in samples_by_role.items():
        for sample in samples:
            metadata = _require_mapping(sample.get("metadata"), "metadata")
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
            by_rollout_policy[str(metadata.get("rollout_policy"))] += 1
    return {
        "schema_id": SPBC_SPC_LEAKAGE_AUDIT_SCHEMA_ID,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "qh_action_as_feature": False,
        "rollout_action_as_feature": False,
        "policy_target_as_feature": False,
        "critic_target_as_feature": False,
        "legacy_spbc_v1_v2_dataset_used": False,
        "neural_mpc_artifacts_used": False,
        "skipped_window_count": len(skipped_windows),
        "sample_counts_by_source_split": dict(sorted(by_source_split.items())),
        "sample_counts_by_synthetic": dict(sorted(by_synthetic.items())),
        "sample_counts_by_rollout_policy": dict(sorted(by_rollout_policy.items())),
    }


def _build_spbc_spc_target_audit(
    target_events: Sequence[Mapping[str, object]],
    samples_by_role: Mapping[str, Sequence[Mapping[str, object]]],
    max_ladder_bitrate_kbps: float,
) -> Mapping[str, object]:
    by_role: dict[str, Counter[str]] = defaultdict(Counter)
    policy_counts: Counter[str] = Counter()
    rollout_counts: Counter[str] = Counter()
    high_capacity_events = []
    fallback_count = 0
    best_rewards = []
    safe_sample_count = 0
    action_value_count = 0
    catastrophic_count = 0
    errors = []

    for event in target_events:
        role = str(event["data_role"])
        action = str(event["qh_action"])
        by_role[role][action] += 1
        policy_counts[action] += 1
        rollout_counts[str(event["rollout_policy"])] += 1
        fallback_count += 1 if event.get("fallback_used") is True else 0
        best_rewards.append(float(event.get("q_h_reward_n", 0.0)))
        if event.get("high_capacity_safe_state") is True:
            high_capacity_events.append(event)

    for samples in samples_by_role.values():
        for sample in samples:
            critic = _require_mapping(sample.get("spc_critic_targets"), "spc_critic_targets")
            values = _require_list(critic.get("action_values"), "spc_critic_targets.action_values")
            has_safe = False
            for value in values:
                row = _require_mapping(value, "action_value")
                action_value_count += 1
                if row.get("is_safe_regret_0_35") is True:
                    has_safe = True
                if row.get("is_catastrophic_regret_2") is True:
                    catastrophic_count += 1
            safe_sample_count += 1 if has_safe else 0

    high_capacity_action0 = sum(1 for event in high_capacity_events if int(event.get("qh_action", -1)) == 0)
    high_capacity_action0_rate = _ratio(high_capacity_action0, len(high_capacity_events))
    target_action0_rate = _ratio(int(policy_counts.get("0", 0)), len(target_events))
    if fallback_count:
        errors.append("qh_oracle_fallback_count_nonzero")
    if high_capacity_events and high_capacity_action0_rate > 0.05:
        errors.append("high_capacity_safe_target_action0_rate_too_high")
    if safe_sample_count != sum(len(samples) for samples in samples_by_role.values()):
        errors.append("sample_without_safe_regret_action")

    return {
        "schema_id": SPBC_SPC_TARGET_AUDIT_SCHEMA_ID,
        "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "policy_target_id": SPBC_POLICY_TARGET_ID,
        "critic_target_id": SPC_CRITIC_TARGET_ID,
        "sample_count": len(target_events),
        "fallback_count": fallback_count,
        "fallback_fraction": round(_ratio(fallback_count, len(target_events)), 6),
        "policy_target_distribution": dict(sorted(policy_counts.items())),
        "policy_target_distribution_by_role": {
            role: dict(sorted(counter.items())) for role, counter in sorted(by_role.items())
        },
        "rollout_policy_distribution": dict(sorted(rollout_counts.items())),
        "target_action0_rate": round(target_action0_rate, 6),
        "high_capacity_safe_state_count": len(high_capacity_events),
        "high_capacity_safe_target_action0_rate": round(high_capacity_action0_rate, 6),
        "max_ladder_bitrate_kbps": float(max_ladder_bitrate_kbps),
        "safe_action_presence_rate": round(_ratio(safe_sample_count, len(target_events)), 6),
        "catastrophic_action_fraction": round(_ratio(catastrophic_count, action_value_count), 6),
        "mean_best_q_h_reward_n": round(sum(best_rewards) / float(len(best_rewards)), 6) if best_rewards else 0.0,
        "uses_future_information": True,
        "future_information_is_target_only": True,
        "metadata_fields_are_model_features": False,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        **no_benchmark_policy(),
    }


def _build_spbc_spc_feature_schema() -> Mapping[str, object]:
    schema = dict(build_feature_schema())
    schema["schema_id"] = SPBC_SPC_FEATURE_SCHEMA_ID
    schema["human_readable_name"] = "Features visibles por SPBC/SPC Phase45 v3 closed-loop"
    schema["metadata_fields_are_model_features"] = False
    schema["target_fields_are_model_features"] = False
    return schema


def _build_spbc_spc_target_schema() -> Mapping[str, object]:
    return {
        "schema_id": SPBC_SPC_TARGET_SCHEMA_ID,
        "policy_target_id": SPBC_POLICY_TARGET_ID,
        "critic_target_id": SPC_CRITIC_TARGET_ID,
        "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "policy_target_fields": [
            "selected_action",
            "selected_q_h_reward_n",
            "selected_best_sequence",
            "one_hot_action",
            "soft_action_weights",
            "q_h_regret_by_action_n",
            "action_mask",
            "future_information_is_target_only",
        ],
        "critic_target_fields": [
            "best_action",
            "best_q_h_reward_n",
            "action_values",
            "target_risk",
            "safe_regret_n",
            "catastrophic_regret_n",
            "future_information_is_target_only",
        ],
        "action_value_fields": [
            "action",
            "feasible",
            "q_h_reward_n",
            "first_step_reward_n",
            "first_step_quality_mbps",
            "first_step_smoothness_mbps",
            "first_step_rebuffer_s",
            "total_rebuffer_s",
            "q_h_regret_n",
            "q_h_advantage_n",
            "target_risk",
            "is_safe_regret_0_35",
            "is_catastrophic_regret_2",
            "best_sequence",
        ],
        "model_must_not_use_target_fields_as_inputs": True,
        "future_information_is_target_only": True,
        "risk_definition": {
            "id": "bounded_0_1_from_qh_regret_and_horizon_rebuffer_v1",
            "regret_component_cap_n": RISK_REGRET_CAP_N,
            "rebuffer_component_cap_s": RISK_REBUFFER_CAP_S,
            "formula": "0.65*clip(q_h_regret_n/cap_n,0,1)+0.35*clip(total_rebuffer_s/cap_s,0,1)",
        },
    }


def _spbc_spc_sampling_payload(payload: Mapping[str, object]) -> Mapping[str, object]:
    updated = dict(payload)
    updated["used_by_phase45_v3_closedloop_spbc_spc_dataset"] = True
    updated["phase45_v3_dataset_schema_id"] = SPBC_SPC_DATASET_SCHEMA_ID
    updated["model_feature_fields"] = []
    updated["metadata_fields_are_model_features"] = False
    updated["target_fields_are_model_features"] = False
    return updated


def _validate_spbc_spc_sample(sample: Mapping[str, object], *, expected_role: str) -> None:
    errors = _sample_errors([sample], expected_role)
    if errors:
        raise Phase45V3ClosedLoopSpbcSpcDatasetError(errors[0])


def _sample_errors(rows: Sequence[Mapping[str, object]], expected_role: str) -> list[str]:
    errors = []
    for index, sample in enumerate(rows[:50]):
        prefix = "{0}[{1}]".format(expected_role, index)
        if sample.get("schema_id") != SPBC_SPC_SAMPLE_SCHEMA_ID:
            errors.append("{0}: unexpected sample schema_id".format(prefix))
        if sample.get("data_role") != expected_role:
            errors.append("{0}: data_role mismatch".format(prefix))
        model_inputs = sample.get("model_inputs")
        if not isinstance(model_inputs, Mapping):
            errors.append("{0}: model_inputs must be object".format(prefix))
            continue
        context = model_inputs.get("context")
        candidates = model_inputs.get("candidates")
        action_mask = model_inputs.get("action_mask")
        if not isinstance(context, Mapping) or not isinstance(candidates, list) or not isinstance(action_mask, list):
            errors.append("{0}: invalid model_inputs shape".format(prefix))
            continue
        feature_audit = audit_feature_payload(context, candidates)
        if not feature_audit["passed"]:
            errors.append("{0}: feature audit failed: {1}".format(prefix, feature_audit["errors"]))
        policy = sample.get("spbc_policy_targets")
        critic = sample.get("spc_critic_targets")
        if not isinstance(policy, Mapping) or not isinstance(critic, Mapping):
            errors.append("{0}: missing policy or critic targets".format(prefix))
            continue
        if policy.get("future_information_is_target_only") is not True:
            errors.append("{0}: policy future information must be target-only".format(prefix))
        if critic.get("future_information_is_target_only") is not True:
            errors.append("{0}: critic future information must be target-only".format(prefix))
        selected_action = int(policy.get("selected_action", -1))
        if selected_action < 0 or selected_action >= len(action_mask) or not action_mask[selected_action]:
            errors.append("{0}: selected_action invalid or masked".format(prefix))
        if int(critic.get("best_action", -1)) != selected_action:
            errors.append("{0}: policy and critic best action mismatch".format(prefix))
        action_values = critic.get("action_values")
        if not isinstance(action_values, list) or len(action_values) != len(candidates):
            errors.append("{0}: critic action_values length mismatch".format(prefix))
        soft_weights = policy.get("soft_action_weights")
        if not isinstance(soft_weights, list) or len(soft_weights) != len(candidates):
            errors.append("{0}: policy soft_action_weights length mismatch".format(prefix))
        elif abs(sum(float(value) for value in soft_weights) - 1.0) > 1.0e-5:
            errors.append("{0}: policy soft_action_weights must sum to one".format(prefix))
        metadata = sample.get("metadata")
        if not isinstance(metadata, Mapping) or metadata.get("metadata_is_model_input") is not False:
            errors.append("{0}: metadata boundary missing".format(prefix))
        audit = sample.get("audit")
        if not isinstance(audit, Mapping) or audit.get("neural_mpc_line_modified") is not False:
            errors.append("{0}: neural_mpc_line_modified boundary missing".format(prefix))
    return errors


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


def _soft_policy_weights(action_values: Sequence[Mapping[str, object]]) -> list[float]:
    logits = []
    for value in action_values:
        q_h = _optional_finite_float(value.get("q_h_reward_n"))
        logits.append(None if q_h is None else float(q_h) / SOFT_POLICY_TEMPERATURE)
    finite_logits = [value for value in logits if value is not None]
    if not finite_logits:
        return [1.0 / float(len(action_values)) for _ in action_values]
    maximum = max(finite_logits)
    weights = [0.0 if value is None else math.exp(float(value) - maximum) for value in logits]
    total = sum(weights)
    if total <= 0.0:
        return [1.0 / float(len(action_values)) for _ in action_values]
    return [round(float(value) / float(total), 9) for value in weights]


def _target_risk(regret: float | None, total_rebuffer_s: float | None) -> float:
    regret_component = 1.0 if regret is None else min(max(float(regret) / RISK_REGRET_CAP_N, 0.0), 1.0)
    rebuffer_component = (
        0.0
        if total_rebuffer_s is None
        else min(max(float(total_rebuffer_s) / RISK_REBUFFER_CAP_S, 0.0), 1.0)
    )
    return 0.65 * regret_component + 0.35 * rebuffer_component


def _derive_first_step_rebuffer_s(
    quality_mbps: float,
    smoothness_mbps: float,
    first_reward_n: float | None,
) -> float | None:
    if first_reward_n is None:
        return None
    rebuffer = (float(quality_mbps) - float(smoothness_mbps) - float(first_reward_n)) / 4.3
    return max(0.0, rebuffer)


def _value_for_action(action_values: Sequence[object], action: int) -> Mapping[str, object]:
    for value in action_values:
        row = _require_mapping(value, "action_value")
        if int(row.get("action", -1)) == int(action):
            return row
    raise Phase45V3ClosedLoopSpbcSpcDatasetError("missing action value for action {0}".format(action))


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise Phase45V3ClosedLoopSpbcSpcDatasetError("{0} must be an object".format(name))
    return value


def _require_list(value: object, name: str) -> list[object]:
    if not isinstance(value, list):
        raise Phase45V3ClosedLoopSpbcSpcDatasetError("{0} must be a list".format(name))
    return value


def _finite_float(value: object, name: str) -> float:
    parsed = _optional_finite_float(value)
    if parsed is None:
        raise Phase45V3ClosedLoopSpbcSpcDatasetError("{0} must be finite".format(name))
    return parsed


def _optional_finite_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _round_optional(value: float | None) -> float | None:
    return None if value is None else round(float(value), 6)


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0
