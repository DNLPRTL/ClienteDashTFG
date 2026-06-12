from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import prepare_output_dir, write_json, write_jsonl
from core.neural_abr.features import audit_feature_payload, build_candidate_features, build_context_features, build_feature_schema
from core.phase45_v1.dataset import load_trace_window
from core.phase45_v1.normalization import build_train_only_normalization
from core.phase45_v1.paths import PathRewriteRule, resolve_external_trace_path
from core.phase45_v1.sampling import build_sampling_artifacts
from core.phase45_v3.abr_closed_loop_env import (
    PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    AbrClosedLoopEnv,
    default_phase45_v3_ladder,
)
from core.phase45_v3.constants import (
    DATA_FILENAMES,
    DATA_ROLES,
    DATASET_SCHEMA_ID,
    FEATURE_SCHEMA_ID,
    FEATURE_SCHEMA_FILENAME,
    LEAKAGE_AUDIT_FILENAME,
    LEAKAGE_AUDIT_SCHEMA_ID,
    MEDIA_PROFILE_ID,
    NORMALIZATION_SCHEMA_ID,
    NORMALIZATION_STATS_FILENAME,
    PHASE45_V3_PHASE,
    QH_AUDIT_FILENAME,
    QH_AUDIT_SCHEMA_ID,
    QH_TARGET_ID,
    REQUIRED_DATASET_FILES,
    REWARD_VERSION,
    ROLLOUT_POLICIES,
    ROLLOUT_QH_MINUS_ONE,
    ROLLOUT_QH_ORACLE,
    ROLLOUT_QH_PLUS_ONE,
    ROLLOUT_STARTUP_CONSERVATIVE,
    SAMPLE_SCHEMA_ID,
    SAMPLING_AUDIT_FILENAME,
    SAMPLING_PLAN_FILENAME,
    SUMMARY_FILENAME,
    TARGET_SCHEMA_FILENAME,
    TARGET_SCHEMA_ID,
    TRAINING_ROLE,
    VALIDATION_ROLE,
    no_benchmark_policy,
)
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.qh_oracle import PHASE45_V3_QH_ORACLE_ID, QhOracleConfig, evaluate_qh_actions, qh_oracle_card
from core.trace_replay.loader import LoadedTrace
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel


class Phase45V3DatasetBuildError(ValueError):
    """Raised when the Phase 4-5 v3 Q_H dataset cannot be built safely."""


def build_phase45_v3_qh_dataset(
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
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 Q_H dataset")
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
    qh_events: list[Mapping[str, object]] = []
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
                    window_samples, window_events = _samples_for_window_rollout(
                        window=window,
                        data_role=data_role,
                        loaded_trace=loaded_trace,
                        ladder=ladder,
                        qh_config=qh_config,
                        rollout_policy=rollout_policy,
                    )
                    samples_by_role[data_role].extend(window_samples)
                    qh_events.extend(window_events)
            except Exception as exc:  # noqa: BLE001 - skipped windows are audited and must not be silent.
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
        raise Phase45V3DatasetBuildError(
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
    qh_audit = _build_qh_audit(qh_config, qh_events, ladder.max_bitrate_bps / 1000.0)
    normalization = dict(build_train_only_normalization(samples_by_role[TRAINING_ROLE]))
    normalization["schema_id"] = NORMALIZATION_SCHEMA_ID
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
        qh_config=qh_config,
        leakage_audit=leakage_audit,
        qh_audit=qh_audit,
    )

    write_json(output_path / SUMMARY_FILENAME, summary)
    write_json(output_path / SAMPLING_PLAN_FILENAME, _phase45_v3_sampling_payload(plan))
    write_json(output_path / SAMPLING_AUDIT_FILENAME, _phase45_v3_sampling_payload(sampling_audit))
    write_json(output_path / FEATURE_SCHEMA_FILENAME, _build_feature_schema())
    write_json(output_path / TARGET_SCHEMA_FILENAME, _build_target_schema())
    write_json(output_path / LEAKAGE_AUDIT_FILENAME, leakage_audit)
    write_json(output_path / NORMALIZATION_STATS_FILENAME, normalization)
    write_json(output_path / QH_AUDIT_FILENAME, qh_audit)

    status = "PASS" if leakage_audit["status"] == "PASS" and qh_audit["status"] == "PASS" else "REVIEW"
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


def load_phase3_manifest(path: object) -> Mapping[str, object]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_default_phase45_v3_trace_path_rewrites(tfg_root: object) -> tuple[PathRewriteRule, ...]:
    root = Path(tfg_root).expanduser()
    return (
        PathRewriteRule("/home/daniel/TFG", str(root)),
        PathRewriteRule("/home/danie/TFG", str(root)),
        PathRewriteRule("C:/Users/danie/Documents/TFG", str(root)),
        PathRewriteRule("C:\\Users\\danie\\Documents\\TFG", str(root)),
    )


def resolve_phase45_v3_trace_path(raw_path: object, rules: Sequence[PathRewriteRule]) -> Path:
    return resolve_external_trace_path(raw_path, rules)


def _samples_for_window_rollout(
    *,
    window: Mapping[str, object],
    data_role: str,
    loaded_trace: LoadedTrace,
    ladder,
    qh_config: QhOracleConfig,
    rollout_policy: str,
) -> tuple[list[Mapping[str, object]], list[Mapping[str, object]]]:
    network_model = TraceDrivenNetworkModel(loaded_trace, end_policy=END_POLICY_LOOP, max_loops=5)
    env = AbrClosedLoopEnv(ladder=ladder, network_model=network_model)
    samples: list[Mapping[str, object]] = []
    qh_events: list[Mapping[str, object]] = []
    while not env.done:
        state = env.state
        action_mask = env.action_mask()
        context = build_context_features(state, ladder)
        candidates = build_candidate_features(ladder, state.segment_index, float(context["last_bitrate_bps"]))
        feature_audit = audit_feature_payload(context, candidates)
        if not feature_audit["passed"]:
            raise Phase45V3DatasetBuildError(
                "{0}: feature payload failed audit: {1}".format(window.get("window_id"), feature_audit["errors"])
            )

        qh_decision = evaluate_qh_actions(state, ladder, network_model, qh_config)
        rollout_action = _select_rollout_action(
            qh_action=int(qh_decision.action),
            action_mask=action_mask,
            rollout_policy=rollout_policy,
            segment_index=int(state.segment_index),
            buffer_s=float(state.buffer_s),
        )
        step = env.step(rollout_action)
        best_value = _qh_value_for_action(qh_decision, int(qh_decision.action))
        last_throughput_kbps = (
            float(state.throughput_history_bps[-1]) / 1000.0 if state.throughput_history_bps else 0.0
        )
        sample = {
            "schema_id": SAMPLE_SCHEMA_ID,
            "sample_id": "{0}__{1}__segment_{2:04d}".format(
                window["window_id"],
                rollout_policy,
                state.segment_index,
            ),
            "data_role": data_role,
            "model_inputs": {
                "context": dict(context),
                "candidates": [dict(candidate) for candidate in candidates],
                "action_mask": [bool(value) for value in action_mask],
            },
            "qh_targets": {
                "target_id": QH_TARGET_ID,
                "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
                "qoe_formula_version": REWARD_VERSION,
                "selected_action": int(qh_decision.action),
                "selected_q_h_reward_n": float(best_value.q_h_reward_n),
                "selected_best_sequence": list(best_value.best_sequence),
                "action_values": [_json_action_value(row) for row in qh_decision.action_values],
                "fallback_used": bool(qh_decision.fallback_used),
                "reason": qh_decision.reason,
                "future_information_is_target_only": True,
            },
            "audit": {
                "feature_audit": feature_audit,
                "closed_loop_environment": _closed_loop_environment_contract(ladder),
                "rollout_policy": rollout_policy,
                "rollout_action": int(rollout_action),
                "rollout_step": {
                    "action": int(step.action),
                    "download_time_s": round(float(step.download_time_s), 6),
                    "rebuffer_s": round(float(step.rebuffer_s), 6),
                    "buffer_s_before": round(float(step.buffer_s_before), 6),
                    "buffer_s_after": round(float(step.buffer_s_after), 6),
                    "measured_throughput_bps": round(float(step.measured_throughput_bps), 6),
                },
                "rollout_action_is_model_target": False,
            },
            "metadata": _sample_metadata(window, data_role, state.segment_index, rollout_policy),
        }
        _validate_sample(sample, expected_role=data_role)
        samples.append(sample)
        qh_events.append(
            {
                "data_role": data_role,
                "rollout_policy": rollout_policy,
                "qh_action": int(qh_decision.action),
                "rollout_action": int(rollout_action),
                "fallback_used": bool(qh_decision.fallback_used),
                "q_h_reward_n": float(best_value.q_h_reward_n),
                "buffer_s": float(state.buffer_s),
                "segment_index": int(state.segment_index),
                "last_throughput_kbps": float(last_throughput_kbps),
                "high_capacity_safe_state": _is_high_capacity_safe_state(
                    state_buffer_s=float(state.buffer_s),
                    last_throughput_kbps=float(last_throughput_kbps),
                    max_ladder_bitrate_kbps=float(ladder.max_bitrate_bps) / 1000.0,
                ),
            }
        )
    return samples, qh_events


def _validate_sample(sample: Mapping[str, object], *, expected_role: str) -> None:
    if sample.get("schema_id") != SAMPLE_SCHEMA_ID:
        raise Phase45V3DatasetBuildError("unexpected sample schema_id")
    if sample.get("data_role") != expected_role:
        raise Phase45V3DatasetBuildError("sample data_role mismatch")
    model_inputs = sample.get("model_inputs")
    if not isinstance(model_inputs, Mapping):
        raise Phase45V3DatasetBuildError("sample model_inputs must be an object")
    context = model_inputs.get("context")
    candidates = model_inputs.get("candidates")
    action_mask = model_inputs.get("action_mask")
    if not isinstance(context, Mapping) or not isinstance(candidates, list) or not isinstance(action_mask, list):
        raise Phase45V3DatasetBuildError("sample model_inputs has invalid shape")
    feature_audit = audit_feature_payload(context, candidates)
    if not feature_audit["passed"]:
        raise Phase45V3DatasetBuildError("sample model_inputs failed feature audit")
    qh_targets = sample.get("qh_targets")
    if not isinstance(qh_targets, Mapping):
        raise Phase45V3DatasetBuildError("sample qh_targets must be an object")
    if qh_targets.get("target_id") != QH_TARGET_ID:
        raise Phase45V3DatasetBuildError("sample qh_targets target_id mismatch")
    selected_action = int(qh_targets.get("selected_action", -1))
    if selected_action < 0 or selected_action >= len(action_mask):
        raise Phase45V3DatasetBuildError("sample qh target action outside action mask")
    if not bool(action_mask[selected_action]):
        raise Phase45V3DatasetBuildError("sample qh target action is masked")
    if len(qh_targets.get("action_values", [])) != len(candidates):  # type: ignore[arg-type]
        raise Phase45V3DatasetBuildError("sample qh action_values length mismatch")


def _build_summary(
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
    qh_audit: Mapping[str, object],
) -> Mapping[str, object]:
    return {
        "schema_id": DATASET_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v3 closed-loop Q_H dataset for ABR scorer/planner training",
        "phase": PHASE45_V3_PHASE,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "source_plan_schema_id": plan.get("schema_id"),
        "phase45_v1_sampler_reused_for_balanced_trace_windows": True,
        "media_profile_id": MEDIA_PROFILE_ID,
        "content_ladder": dict(ladder_manifest),
        "files": {filename: filename for filename in DATA_FILENAMES.values()},
        "required_files": list(REQUIRED_DATASET_FILES),
        "generation_window_counts": dict(generation_window_counts),
        "sample_counts": {role: len(samples_by_role[role]) for role in DATA_ROLES},
        "qh_oracle_policy": qh_oracle_card(qh_config),
        "qh_target_source": PHASE45_V3_QH_ORACLE_ID,
        "rollout_policy_role": "state_coverage_only_not_primary_target",
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "normalization_fitted_on": TRAINING_ROLE,
        "closed_loop_client_parity": _closed_loop_environment_contract_from_manifest(ladder_manifest),
        "trace_path_rewrites": [rule.to_json() for rule in path_rewrites],
        "resolved_path_examples": list(resolved_path_examples),
        "skipped_windows": list(skipped_windows),
        "leakage_audit_status": leakage_audit.get("status"),
        "qh_audit_status": qh_audit.get("status"),
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
                errors.append("leakage_group selected in multiple roles: {0}".format(group))
            source_split = str(metadata["source_split"])
            if source_split == "eval":
                errors.append("eval split used in sample: {0}".format(sample["sample_id"]))
            by_source_split[source_split] += 1
            by_synthetic[str(bool(metadata.get("synthetic")))] += 1
            by_rollout_policy[str(metadata.get("rollout_policy"))] += 1
    return {
        "schema_id": LEAKAGE_AUDIT_SCHEMA_ID,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "trace_level_roles_disjoint": not errors,
        "leakage_group_roles_disjoint": not errors,
        "eval_split_used": False,
        "metadata_fields_are_model_features": False,
        "future_throughput_as_feature": False,
        "qh_action_as_feature": False,
        "rollout_action_as_feature": False,
        "legacy_dry_runs_used": False,
        "skipped_window_count": len(skipped_windows),
        "sample_counts_by_source_split": dict(sorted(by_source_split.items())),
        "sample_counts_by_synthetic": dict(sorted(by_synthetic.items())),
        "sample_counts_by_rollout_policy": dict(sorted(by_rollout_policy.items())),
    }


def _build_qh_audit(
    qh_config: QhOracleConfig,
    qh_events: Sequence[Mapping[str, object]],
    max_ladder_bitrate_kbps: float,
) -> Mapping[str, object]:
    by_role: dict[str, Counter[str]] = defaultdict(Counter)
    by_rollout: Counter[str] = Counter()
    target_action_counts: Counter[str] = Counter()
    rollout_action_counts: Counter[str] = Counter()
    fallback_count = 0
    rewards = []
    high_capacity_events = []
    for event in qh_events:
        role = str(event["data_role"])
        action = str(event["qh_action"])
        by_role[role][action] += 1
        target_action_counts[action] += 1
        rollout_action_counts[str(event["rollout_action"])] += 1
        by_rollout[str(event["rollout_policy"])] += 1
        fallback_count += 1 if event.get("fallback_used") is True else 0
        rewards.append(float(event.get("q_h_reward_n", 0.0)))
        if event.get("high_capacity_safe_state") is True:
            high_capacity_events.append(event)

    high_capacity_action0 = sum(1 for event in high_capacity_events if int(event.get("qh_action", -1)) == 0)
    high_capacity_action0_rate = _ratio(high_capacity_action0, len(high_capacity_events))
    action0_rate = _ratio(int(target_action_counts.get("0", 0)), len(qh_events))
    errors = []
    if fallback_count:
        errors.append("qh_oracle_fallback_count_nonzero")
    if high_capacity_events and high_capacity_action0_rate > 0.05:
        errors.append("qh_high_capacity_safe_action0_rate_too_high")

    return {
        "schema_id": QH_AUDIT_SCHEMA_ID,
        "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "config": qh_config.to_json(),
        "sample_count": len(qh_events),
        "fallback_count": fallback_count,
        "fallback_fraction": round(_ratio(fallback_count, len(qh_events)), 6),
        "target_action_distribution": dict(sorted(target_action_counts.items())),
        "target_action_distribution_by_role": {
            role: dict(sorted(counter.items())) for role, counter in sorted(by_role.items())
        },
        "rollout_action_distribution": dict(sorted(rollout_action_counts.items())),
        "rollout_policy_distribution": dict(sorted(by_rollout.items())),
        "target_action0_rate": round(action0_rate, 6),
        "high_capacity_safe_state_count": len(high_capacity_events),
        "high_capacity_safe_target_action0_rate": round(high_capacity_action0_rate, 6),
        "max_ladder_bitrate_kbps": float(max_ladder_bitrate_kbps),
        "q_h_reward_mean": round(sum(rewards) / float(len(rewards)), 6) if rewards else 0.0,
        "uses_future_information": True,
        "future_information_is_target_only": True,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        **no_benchmark_policy(),
    }


def _build_feature_schema() -> Mapping[str, object]:
    schema = dict(build_feature_schema())
    schema["schema_id"] = FEATURE_SCHEMA_ID
    schema["human_readable_name"] = "Features visibles por el modelo Phase45 v3 Q_H"
    return schema


def _build_target_schema() -> Mapping[str, object]:
    return {
        "schema_id": TARGET_SCHEMA_ID,
        "target_id": QH_TARGET_ID,
        "oracle_policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "target_fields": [
            "selected_action",
            "selected_q_h_reward_n",
            "selected_best_sequence",
            "action_values",
            "future_information_is_target_only",
        ],
        "action_value_fields": [
            "action",
            "feasible",
            "q_h_reward_n",
            "first_step_reward_n",
            "total_rebuffer_s",
            "switch_count",
            "best_sequence",
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


def _phase45_v3_sampling_payload(payload: Mapping[str, object]) -> Mapping[str, object]:
    updated = dict(payload)
    updated["used_by_phase45_v3_dataset"] = True
    updated["phase45_v3_dataset_schema_id"] = DATASET_SCHEMA_ID
    updated["model_feature_fields"] = []
    updated["metadata_fields_are_model_features"] = False
    return updated


def _closed_loop_environment_contract(ladder) -> Mapping[str, object]:
    return _closed_loop_environment_contract_from_manifest(ladder.to_manifest())


def _closed_loop_environment_contract_from_manifest(ladder_manifest: Mapping[str, object]) -> Mapping[str, object]:
    return {
        "parity_scope": "ABR decision dynamics used by the client and Phase 6 trace replay",
        "not_reproduced": ["HTTP server process", "GStreamer media pipeline", "OS scheduling jitter"],
        "segment_duration_s": float(ladder_manifest["segment_duration_s"]),
        "segment_count": int(ladder_manifest["segment_count"]),
        "max_buffer_s": float(ladder_manifest["max_buffer_s"]),
        "representation_bitrates_bps": list(ladder_manifest["bitrates_bps"]),
        "buffer_update": "max(buffer_s - download_time_s, 0) + segment_duration_s capped at max_buffer_s",
        "rebuffer_update": "max(download_time_s - buffer_s, 0)",
        "reward": "bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps",
        "qoe_formula_version": REWARD_VERSION,
        "network_source": "TraceDrivenNetworkModel over normalized throughput_kbps windows",
        "controller_visible_inputs_match_runtime_feature_builder": True,
    }


def _rollout_policy_for_index(index: int) -> str:
    return ROLLOUT_POLICIES[int(index) % len(ROLLOUT_POLICIES)]


def _select_rollout_action(
    *,
    qh_action: int,
    action_mask: Sequence[bool],
    rollout_policy: str,
    segment_index: int,
    buffer_s: float,
) -> int:
    if rollout_policy == ROLLOUT_QH_ORACLE:
        return _nearest_valid_action(qh_action, action_mask)
    if rollout_policy == ROLLOUT_QH_MINUS_ONE:
        return _nearest_valid_action(qh_action - 1, action_mask)
    if rollout_policy == ROLLOUT_QH_PLUS_ONE:
        return _nearest_valid_action(qh_action + 1, action_mask)
    if rollout_policy == ROLLOUT_STARTUP_CONSERVATIVE:
        if int(segment_index) < 3 or float(buffer_s) < 8.0:
            return _nearest_valid_action(min(qh_action, 1), action_mask)
        return _nearest_valid_action(qh_action, action_mask)
    raise Phase45V3DatasetBuildError("unknown rollout policy: {0}".format(rollout_policy))


def _nearest_valid_action(action: int, action_mask: Sequence[bool]) -> int:
    valid = [index for index, allowed in enumerate(action_mask) if allowed]
    if not valid:
        raise Phase45V3DatasetBuildError("action mask has no valid action")
    clipped = max(min(int(action), max(valid)), min(valid))
    if clipped in valid:
        return clipped
    return min(valid, key=lambda value: abs(value - clipped))


def _qh_value_for_action(decision, action: int):
    for value in decision.action_values:
        if int(value.action) == int(action):
            return value
    raise Phase45V3DatasetBuildError("Q_H decision has no value for action {0}".format(action))


def _json_action_value(row) -> Mapping[str, object]:
    return {
        "action": int(row.action),
        "feasible": bool(row.feasible),
        "q_h_reward_n": _json_float(row.q_h_reward_n),
        "first_step_reward_n": _json_float(row.first_step_reward_n),
        "total_rebuffer_s": _json_float(row.total_rebuffer_s),
        "switch_count": int(row.switch_count),
        "best_sequence": list(row.best_sequence),
        "horizon_segments_evaluated": int(row.horizon_segments_evaluated),
        "evaluated_sequence_count": int(row.evaluated_sequence_count),
        "reason": row.reason,
    }


def _json_float(value: object) -> float | None:
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _is_high_capacity_safe_state(
    *,
    state_buffer_s: float,
    last_throughput_kbps: float,
    max_ladder_bitrate_kbps: float,
) -> bool:
    return float(state_buffer_s) >= 8.0 and float(last_throughput_kbps) >= 2.0 * float(max_ladder_bitrate_kbps)


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _limited_windows(raw_windows: object, limit: int | None) -> list[Mapping[str, object]]:
    if not isinstance(raw_windows, list):
        raise Phase45V3DatasetBuildError("sampling plan windows must be a list")
    windows = []
    for index, window in enumerate(raw_windows):
        if not isinstance(window, Mapping):
            raise Phase45V3DatasetBuildError("window {0} must be an object".format(index))
        windows.append(window)
    if limit is not None:
        return windows[: int(limit)]
    return windows


def read_csv_rows(path: object) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle)]
