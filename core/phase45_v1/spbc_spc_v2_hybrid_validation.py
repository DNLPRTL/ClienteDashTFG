from __future__ import annotations

import hashlib
import math
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Mapping, Sequence

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, write_json
from core.phase45_v1.constants import MEDIA_PROFILE_ID, REWARD_VERSION, VALIDATION_ROLE
from core.phase45_v1.preference_dataset_v2 import V2_DATA_FILENAMES, validate_phase45_v2_dataset_dir
from core.phase45_v1.spbc_v2_dpo_training import (
    FOCUS_THROUGHPUT_BUCKET,
    SPBC_V2_DPO_MODEL_KEY,
    SpbcV2DpoExample,
    _PolicyMetricTotals,
    examples_to_tensors,
    load_spbc_v2_dpo_examples,
)
from core.phase45_v1.spc_v2_reward_risk_training import (
    SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID,
    SPC_V2_REWARD_RISK_MODEL_KEY,
    SpcAbrV2RewardRiskScorer,
    SpcV2RewardRiskTrainingError,
    _PredictionMetricTotals,
    _load_torch_mapping,
    _normalization_from_payload,
    _prediction_metrics,
    _reference_model_and_normalization,
    resolve_torch_device,
)


SPBC_SPC_V2_HYBRID_VALIDATION_REPORT_FILENAME = "reporte_validacion_spbc_spc_v2_hybrid_offline.json"


@dataclass(frozen=True)
class SpbcSpcV2HybridValidationProfile:
    name: str
    batch_size: int
    max_validation_samples: int | None


SPBC_SPC_V2_HYBRID_VALIDATION_PROFILES: dict[str, SpbcSpcV2HybridValidationProfile] = {
    "smoke": SpbcSpcV2HybridValidationProfile(name="smoke", batch_size=64, max_validation_samples=256),
    "pilot": SpbcSpcV2HybridValidationProfile(name="pilot", batch_size=1024, max_validation_samples=12000),
    "full": SpbcSpcV2HybridValidationProfile(name="full", batch_size=1024, max_validation_samples=None),
}


class SpbcSpcV2HybridValidationError(ValueError):
    """Raised when offline SPBC+SPC hybrid validation cannot proceed safely."""


def hybrid_profile_by_name(name: str) -> SpbcSpcV2HybridValidationProfile:
    if name not in SPBC_SPC_V2_HYBRID_VALIDATION_PROFILES:
        raise SpbcSpcV2HybridValidationError("unknown hybrid validation profile: {0}".format(name))
    return SPBC_SPC_V2_HYBRID_VALIDATION_PROFILES[name]


def validate_spbc_spc_v2_hybrid_offline(
    dataset_dir: object,
    spbc_checkpoint: object,
    spc_checkpoint: object,
    output_dir: object,
    *,
    profile: SpbcSpcV2HybridValidationProfile,
    overwrite: bool = False,
    device: str = "auto",
    batch_size: int | None = None,
    max_validation_samples: int | None | str = "profile",
    validate_dataset: bool = True,
    risk_threshold: float = 0.50,
    rebuffer_threshold_s: float = 0.10,
    rerank_top_k: int = 2,
    utility_regret_tolerance: float = 0.002,
    over_aggressive_tolerance: float = 0.0,
    rebuffer_regret_tolerance: float = 0.0,
    risk_brier_gate: float = 0.02,
    risk_false_negative_gate: float = 0.005,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
) -> Mapping[str, object]:
    _validate_hybrid_args(
        risk_threshold=risk_threshold,
        rebuffer_threshold_s=rebuffer_threshold_s,
        rerank_top_k=rerank_top_k,
        utility_regret_tolerance=utility_regret_tolerance,
        over_aggressive_tolerance=over_aggressive_tolerance,
        rebuffer_regret_tolerance=rebuffer_regret_tolerance,
        risk_brier_gate=risk_brier_gate,
        risk_false_negative_gate=risk_false_negative_gate,
    )
    started = time.monotonic()
    _emit_progress(progress_callback, "preparing", "Preparando validacion offline SPBC+SPC v2")
    data_path = ensure_existing_dir(dataset_dir, purpose="phase45_v2 preference dataset")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v2 SPBC+SPC hybrid validation")
    if validate_dataset:
        _emit_progress(progress_callback, "validating_dataset", "Validando dataset phase45_v2")
        dataset_validation = validate_phase45_v2_dataset_dir(data_path)
    else:
        dataset_validation = {"status": "SKIPPED", "dataset_dir": str(data_path)}

    active_batch_size = int(batch_size if batch_size is not None else profile.batch_size)
    validation_limit = _resolve_limit(max_validation_samples, profile.max_validation_samples)
    if active_batch_size <= 0:
        raise SpbcSpcV2HybridValidationError("batch_size must be positive")
    selected_device = resolve_torch_device(device)
    _emit_progress(
        progress_callback,
        "loading_examples",
        "Cargando muestras de validacion DAgger-2",
        validation_limit=validation_limit,
        device_used=str(selected_device),
    )
    examples = load_spbc_v2_dpo_examples(
        data_path / V2_DATA_FILENAMES[VALIDATION_ROLE],
        VALIDATION_ROLE,
        limit=validation_limit,
    )
    if not examples:
        raise SpbcSpcV2HybridValidationError("hybrid validation requires validation examples")

    spbc_path = Path(spbc_checkpoint).expanduser()
    spc_path = Path(spc_checkpoint).expanduser()
    if not spbc_path.is_file():
        raise SpbcSpcV2HybridValidationError("SPBC checkpoint does not exist: {0}".format(spbc_path))
    if not spc_path.is_file():
        raise SpbcSpcV2HybridValidationError("SPC checkpoint does not exist: {0}".format(spc_path))

    _emit_progress(progress_callback, "loading_checkpoints", "Cargando checkpoints SPBC y SPC")
    spbc_payload = _load_torch_mapping(spbc_path)
    spbc_model, spbc_normalization = _reference_model_and_normalization(spbc_payload, spbc_path)
    spc_payload = _load_torch_mapping(spc_path)
    spc_model, spc_normalization = _spc_model_and_normalization(spc_payload, spc_path)
    spbc_model = spbc_model.to(selected_device)
    spc_model = spc_model.to(selected_device)

    spbc_tensors = examples_to_tensors(examples, spbc_normalization)
    spc_tensors = examples_to_tensors(examples, spc_normalization)
    index_loader = DataLoader(TensorDataset(torch.arange(len(examples), dtype=torch.long)), batch_size=active_batch_size)

    _emit_progress(
        progress_callback,
        "validation_started",
        "Evaluando modos SPBC only, SPC only, veto y top-k rerank",
        validation_samples=len(examples),
        batches=len(index_loader),
    )
    results = _evaluate_hybrid_modes(
        spbc_model=spbc_model,
        spc_model=spc_model,
        spbc_tensors=spbc_tensors,
        spc_tensors=spc_tensors,
        index_loader=index_loader,
        device=selected_device,
        examples=examples,
        risk_threshold=risk_threshold,
        rebuffer_threshold_s=rebuffer_threshold_s,
        rerank_top_k=rerank_top_k,
        progress_callback=progress_callback,
    )

    mode_metrics = results["mode_metrics"]
    prediction_metrics = results["spc_prediction_metrics"]
    gates = {
        mode: _hybrid_gate(
            mode_metrics[mode],
            mode_metrics["spbc_only"],
            prediction_metrics,
            utility_regret_tolerance=utility_regret_tolerance,
            over_aggressive_tolerance=over_aggressive_tolerance,
            rebuffer_regret_tolerance=rebuffer_regret_tolerance,
            risk_brier_gate=risk_brier_gate,
            risk_false_negative_gate=risk_false_negative_gate,
        )
        for mode in ("spbc_spc_veto_only", "spbc_spc_topk_rerank")
    }

    report_path = output_path / SPBC_SPC_V2_HYBRID_VALIDATION_REPORT_FILENAME
    duration_s = time.monotonic() - started
    report = {
        "schema_id": "phase45_v2_spbc_spc_hybrid_offline_validation_report_v1",
        "human_readable_name": "Validacion offline hibrida SPBC v2 + SPC v2",
        "phase": "fase_4_5_v1_spbc_spc_v2_hybrid_offline_validation",
        "status": "PASS",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "dataset_dir": str(data_path),
        "dataset_validation": dict(dataset_validation),
        "output_dir": str(output_path),
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "profile": {
            "name": profile.name,
            "batch_size": active_batch_size,
            "max_validation_samples": validation_limit,
        },
        "device_requested": str(device),
        "device_used": str(selected_device),
        "sample_counts_used": {VALIDATION_ROLE: len(examples)},
        "spbc_checkpoint": str(spbc_path),
        "spbc_checkpoint_sha256": _sha256_file(spbc_path),
        "spbc_model_key": str(spbc_payload.get("model_key")),
        "spc_checkpoint": str(spc_path),
        "spc_checkpoint_sha256": _sha256_file(spc_path),
        "spc_model_key": str(spc_payload.get("model_key")),
        "hybrid_policy_design": {
            "spbc_role": "driver_policy_decisor",
            "spc_role": "per_action_predictive_critic",
            "spc_only_reward_only_is_diagnostic": True,
            "veto_only": "SPC can keep or downshift the SPBC action when predicted risk/rebuffer exceeds thresholds",
            "topk_rerank": "SPC reranks only inside the SPBC top-k support after risk/rebuffer filtering",
            "risk_threshold": float(risk_threshold),
            "rebuffer_threshold_s": float(rebuffer_threshold_s),
            "rerank_top_k": int(rerank_top_k),
        },
        "mode_metrics": mode_metrics,
        "mode_deltas_vs_spbc_only": {
            mode: _mode_delta(mode_metrics[mode], mode_metrics["spbc_only"])
            for mode in ("spc_only_reward", "spbc_spc_veto_only", "spbc_spc_topk_rerank")
        },
        "spc_prediction_metrics": prediction_metrics,
        "hybrid_gates": gates,
        "hybrid_candidate_gate_passed": any(bool(gate["passed"]) for gate in gates.values()),
        "validation_duration_s": duration_s,
        "artifacts": {"validation_report": str(report_path)},
        "normalization_fitted_on": "training_split_from_checkpoints",
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
        "preference_fields_are_model_features": False,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": False,
        "formal_ia_training_performed": False,
        "candidate_model_created": False,
        "checkpoint_written": False,
        "bundle_exported": False,
        "controller_registered": False,
        "controller_integrated": False,
        "qoe_improvement_claimed": False,
        "sota_claimed": False,
        "real_world_generalization_claimed": False,
    }
    write_json(report_path, report)
    _emit_progress(
        progress_callback,
        "finished",
        "Validacion offline SPBC+SPC v2 finalizada",
        validation_duration_s=duration_s,
        output_dir=str(output_path),
        hybrid_candidate_gate_passed=report["hybrid_candidate_gate_passed"],
    )
    return report


class _ModeAccumulator:
    def __init__(self) -> None:
        self.global_totals = _PolicyMetricTotals()
        self.by_bucket: dict[str, _PolicyMetricTotals] = defaultdict(_PolicyMetricTotals)
        self.by_rollout_source: dict[str, _PolicyMetricTotals] = defaultdict(_PolicyMetricTotals)
        self.interventions = 0
        self.useful_interventions = 0

    def add(
        self,
        observation: Mapping[str, object],
        example: SpbcV2DpoExample,
        *,
        spbc_action: int,
        selected_action: int,
    ) -> None:
        self.global_totals.add_observations((observation,), {}, 1)
        self.by_bucket[example.throughput_bucket].add_observations((observation,), {}, 1)
        self.by_rollout_source[example.rollout_source].add_observations((observation,), {}, 1)
        if int(selected_action) != int(spbc_action):
            self.interventions += 1
            if _is_useful_intervention(example, spbc_action=spbc_action, selected_action=selected_action):
                self.useful_interventions += 1

    def to_json(self) -> dict[str, object]:
        payload = self.global_totals.to_json(include_losses=False)
        sample_count = max(float(payload.get("sample_count", 0)), 1.0)
        intervention_rate = float(self.interventions) / sample_count
        useful_intervention_rate = float(self.useful_interventions) / max(float(self.interventions), 1.0)
        by_bucket = {key: value.to_json(include_losses=False) for key, value in sorted(self.by_bucket.items())}
        focus = by_bucket.get(FOCUS_THROUGHPUT_BUCKET)
        if focus is None:
            focus = {"sample_count": 0, "bucket_present": False}
        else:
            focus = {**focus, "bucket_present": True}
        payload.update(
            {
                "intervention_count": int(self.interventions),
                "intervention_rate": round(intervention_rate, 6),
                "useful_intervention_count": int(self.useful_interventions),
                "useful_intervention_rate": round(useful_intervention_rate, 6),
                "by_throughput_bucket": by_bucket,
                "focus_2_5_mbps": focus,
                "by_rollout_source": {
                    key: value.to_json(include_losses=False) for key, value in sorted(self.by_rollout_source.items())
                },
            }
        )
        return payload


def _evaluate_hybrid_modes(
    *,
    spbc_model: nn.Module,
    spc_model: nn.Module,
    spbc_tensors: Sequence[torch.Tensor],
    spc_tensors: Sequence[torch.Tensor],
    index_loader: DataLoader,
    device: torch.device,
    examples: Sequence[SpbcV2DpoExample],
    risk_threshold: float,
    rebuffer_threshold_s: float,
    rerank_top_k: int,
    progress_callback: Callable[[Mapping[str, object]], None] | None,
) -> dict[str, object]:
    spbc_model.eval()
    spc_model.eval()
    accumulators = {
        "spbc_only": _ModeAccumulator(),
        "spc_only_reward": _ModeAccumulator(),
        "spbc_spc_veto_only": _ModeAccumulator(),
        "spbc_spc_topk_rerank": _ModeAccumulator(),
    }
    prediction_totals = _PredictionMetricTotals()
    with torch.no_grad():
        for batch_number, (indices,) in enumerate(index_loader, start=1):
            batch_indices = indices.to(dtype=torch.long)
            spbc_batch = _batch_from_tensors(spbc_tensors, batch_indices, device)
            spc_batch = _batch_from_tensors(spc_tensors, batch_indices, device)
            spbc_outputs = spbc_model(spbc_batch[0], spbc_batch[1], spbc_batch[2], spbc_batch[3])
            spc_outputs = spc_model(spc_batch[0], spc_batch[1], spc_batch[2], spc_batch[3])
            prediction_totals.add(_prediction_metrics(spc_outputs, spc_batch), int(batch_indices.shape[0]))

            spbc_scores_rows = spbc_outputs["action_logits"].detach().cpu().tolist()
            reward_rows = spc_outputs["predicted_reward_n_by_action"].detach().cpu().tolist()
            rebuffer_rows = spc_outputs["predicted_rebuffer_s_by_action"].detach().cpu().tolist()
            risk_rows = torch.sigmoid(spc_outputs["predicted_target_risk_logits_by_action"]).detach().cpu().tolist()
            for row_offset, example_index in enumerate(batch_indices.detach().cpu().tolist()):
                example = examples[int(example_index)]
                mask = list(example.action_mask)
                spbc_scores = [float(value) for value in spbc_scores_rows[row_offset]]
                spc_reward_scores = [float(value) for value in reward_rows[row_offset]]
                spc_rebuffer = [float(value) for value in rebuffer_rows[row_offset]]
                spc_risk = [float(value) for value in risk_rows[row_offset]]
                spbc_action = _argmax_valid(spbc_scores, mask)
                decisions = {
                    "spbc_only": (spbc_action, spbc_scores),
                    "spc_only_reward": (_argmax_valid(spc_reward_scores, mask), spc_reward_scores),
                    "spbc_spc_veto_only": (
                        _select_veto_only(
                            spbc_action=spbc_action,
                            mask=mask,
                            reward_scores=spc_reward_scores,
                            rebuffer_s=spc_rebuffer,
                            risk_probs=spc_risk,
                            risk_threshold=risk_threshold,
                            rebuffer_threshold_s=rebuffer_threshold_s,
                        ),
                        spc_reward_scores,
                    ),
                    "spbc_spc_topk_rerank": (
                        _select_topk_rerank(
                            spbc_action=spbc_action,
                            spbc_scores=spbc_scores,
                            mask=mask,
                            reward_scores=spc_reward_scores,
                            rebuffer_s=spc_rebuffer,
                            risk_probs=spc_risk,
                            risk_threshold=risk_threshold,
                            rebuffer_threshold_s=rebuffer_threshold_s,
                            rerank_top_k=rerank_top_k,
                        ),
                        spc_reward_scores,
                    ),
                }
                for mode, (selected_action, decision_scores) in decisions.items():
                    observation = _observation_for_action(example, selected_action, decision_scores)
                    accumulators[mode].add(
                        observation,
                        example,
                        spbc_action=spbc_action,
                        selected_action=selected_action,
                    )
            if batch_number == 1 or batch_number == len(index_loader) or batch_number % max(1, len(index_loader) // 20) == 0:
                _emit_progress(
                    progress_callback,
                    "validation_batch",
                    "Validando batches SPBC+SPC v2",
                    batch=batch_number,
                    batches=len(index_loader),
                )
    return {
        "mode_metrics": {key: accumulator.to_json() for key, accumulator in accumulators.items()},
        "spc_prediction_metrics": prediction_totals.to_json(),
    }


def _spc_model_and_normalization(
    payload: Mapping[str, object],
    path: Path,
) -> tuple[nn.Module, object]:
    if payload.get("schema_id") != SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID:
        raise SpbcSpcV2HybridValidationError("unsupported SPC checkpoint schema: {0}".format(path))
    if str(payload.get("model_key")) != SPC_V2_REWARD_RISK_MODEL_KEY:
        raise SpbcSpcV2HybridValidationError("unsupported SPC model key: {0}".format(path))
    config = payload.get("model_config")
    state_dict = payload.get("model_state_dict")
    if not isinstance(config, Mapping):
        raise SpbcSpcV2HybridValidationError("SPC checkpoint missing model_config: {0}".format(path))
    if not isinstance(state_dict, Mapping):
        raise SpbcSpcV2HybridValidationError("SPC checkpoint missing model_state_dict: {0}".format(path))
    model = SpcAbrV2RewardRiskScorer(
        history_hidden_size=int(config["history_hidden_size"]),
        state_hidden_size=int(config["state_hidden_size"]),
        candidate_hidden_size=int(config["candidate_hidden_size"]),
        shared_hidden_size=int(config["shared_hidden_size"]),
        dropout=float(config["dropout"]),
        score_rebuffer_weight=float(config.get("score_rebuffer_weight", 0.0)),
        score_risk_weight=float(config.get("score_risk_weight", 0.0)),
        score_smoothness_weight=float(config.get("score_smoothness_weight", 0.0)),
        score_qoe_gap_weight=float(config.get("score_qoe_gap_weight", 0.0)),
    )
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    return model, _normalization_from_payload(payload, path)


def _select_veto_only(
    *,
    spbc_action: int,
    mask: Sequence[bool],
    reward_scores: Sequence[float],
    rebuffer_s: Sequence[float],
    risk_probs: Sequence[float],
    risk_threshold: float,
    rebuffer_threshold_s: float,
) -> int:
    if _is_safe_action(spbc_action, rebuffer_s, risk_probs, risk_threshold, rebuffer_threshold_s):
        return int(spbc_action)
    lower_or_equal = [index for index, valid in enumerate(mask) if bool(valid) and index <= int(spbc_action)]
    safe_lower = [
        index
        for index in lower_or_equal
        if _is_safe_action(index, rebuffer_s, risk_probs, risk_threshold, rebuffer_threshold_s)
    ]
    if safe_lower:
        return max(safe_lower, key=lambda index: (float(reward_scores[index]), index))
    if lower_or_equal:
        return min(lower_or_equal, key=lambda index: (float(risk_probs[index]), float(rebuffer_s[index]), -float(reward_scores[index])))
    return int(spbc_action)


def _select_topk_rerank(
    *,
    spbc_action: int,
    spbc_scores: Sequence[float],
    mask: Sequence[bool],
    reward_scores: Sequence[float],
    rebuffer_s: Sequence[float],
    risk_probs: Sequence[float],
    risk_threshold: float,
    rebuffer_threshold_s: float,
    rerank_top_k: int,
) -> int:
    topk = _topk_valid(spbc_scores, mask, rerank_top_k)
    safe_topk = [
        index
        for index in topk
        if _is_safe_action(index, rebuffer_s, risk_probs, risk_threshold, rebuffer_threshold_s)
    ]
    if safe_topk:
        return max(safe_topk, key=lambda index: (float(reward_scores[index]), index))
    return int(spbc_action)


def _is_safe_action(
    action: int,
    rebuffer_s: Sequence[float],
    risk_probs: Sequence[float],
    risk_threshold: float,
    rebuffer_threshold_s: float,
) -> bool:
    return float(risk_probs[action]) <= float(risk_threshold) and float(rebuffer_s[action]) <= float(rebuffer_threshold_s)


def _observation_for_action(
    example: SpbcV2DpoExample,
    action: int,
    decision_scores: Sequence[float],
) -> Mapping[str, object]:
    action = int(action)
    oracle_action = int(example.oracle_action)
    best_immediate_action = int(example.best_immediate_action)
    top2 = _topk_valid(decision_scores, example.action_mask, 2)
    pair_total = 0
    pair_correct = 0
    for pair in example.pairs:
        pair_total += 1
        if float(decision_scores[pair.preferred_action]) >= float(decision_scores[pair.rejected_action]):
            pair_correct += 1
    return {
        "oracle_action": oracle_action,
        "best_immediate_action": best_immediate_action,
        "predicted_action": action,
        "top2_hit": oracle_action in top2,
        "valid_prediction": bool(example.action_mask[action]) if action < len(example.action_mask) else False,
        "predicted_qoe_gap": float(example.qoe_gap_by_action[action]),
        "predicted_rebuffer_s": float(example.rebuffer_s_by_action[action]),
        "predicted_reward_n": float(example.reward_by_action[action]),
        "predicted_bitrate_kbps": float(example.bitrate_kbps_by_action[action]),
        "predicted_smoothness_mbps": float(example.smoothness_mbps_by_action[action]),
        "predicted_target_risk": float(example.target_risk_by_action[action]),
        "oracle_reward_n": float(example.reward_by_action[oracle_action]),
        "oracle_rebuffer_s": float(example.rebuffer_s_by_action[oracle_action]),
        "oracle_bitrate_kbps": float(example.bitrate_kbps_by_action[oracle_action]),
        "oracle_smoothness_mbps": float(example.smoothness_mbps_by_action[oracle_action]),
        "oracle_target_risk": float(example.target_risk_by_action[oracle_action]),
        "best_immediate_reward_n": float(example.reward_by_action[best_immediate_action]),
        "best_immediate_rebuffer_s": float(example.rebuffer_s_by_action[best_immediate_action]),
        "pair_total": pair_total,
        "pair_correct": pair_correct,
    }


def _is_useful_intervention(
    example: SpbcV2DpoExample,
    *,
    spbc_action: int,
    selected_action: int,
) -> bool:
    spbc_over = bool(example.over_aggressive_action_by_action[spbc_action])
    selected_over = bool(example.over_aggressive_action_by_action[selected_action])
    if spbc_over and not selected_over:
        return True
    return float(example.rebuffer_s_by_action[selected_action]) < float(example.rebuffer_s_by_action[spbc_action])


def _hybrid_gate(
    metrics: Mapping[str, object],
    baseline: Mapping[str, object],
    prediction_metrics: Mapping[str, object],
    *,
    utility_regret_tolerance: float,
    over_aggressive_tolerance: float,
    rebuffer_regret_tolerance: float,
    risk_brier_gate: float,
    risk_false_negative_gate: float,
) -> Mapping[str, object]:
    contexts = {
        "global": (metrics, baseline),
        "focus_2_5_mbps": (
            metrics.get("focus_2_5_mbps", {}),
            baseline.get("focus_2_5_mbps", {}),
        ),
        "spbc_v2_dpo_on_policy": (
            _rollout_source(metrics, "spbc_v2_dpo_on_policy"),
            _rollout_source(baseline, "spbc_v2_dpo_on_policy"),
        ),
    }
    checks: dict[str, object] = {}
    passed = True
    for name, (current, reference) in contexts.items():
        if not isinstance(current, Mapping) or not isinstance(reference, Mapping):
            checks[name] = {"present": False, "passed": True}
            continue
        if int(current.get("sample_count", 0) or 0) <= 0 or int(reference.get("sample_count", 0) or 0) <= 0:
            checks[name] = {"present": False, "passed": True}
            continue
        delta = _critical_delta(current, reference)
        context_passed = (
            float(delta["over_aggressive_rate_vs_oracle"]) <= float(over_aggressive_tolerance)
            and float(delta["selected_rebuffer_regret_vs_best_immediate_mean"]) <= float(rebuffer_regret_tolerance)
            and float(delta["selected_utility_regret_vs_best_immediate_mean"]) <= float(utility_regret_tolerance)
        )
        checks[name] = {"present": True, "passed": context_passed, "delta_vs_spbc_only": delta}
        passed = passed and context_passed
    risk_check = {
        "risk_brier": float(prediction_metrics.get("risk_brier", math.inf)),
        "risk_false_negative_rate": float(prediction_metrics.get("risk_false_negative_rate", math.inf)),
        "risk_brier_gate": float(risk_brier_gate),
        "risk_false_negative_gate": float(risk_false_negative_gate),
    }
    risk_passed = (
        risk_check["risk_brier"] <= float(risk_brier_gate)
        and risk_check["risk_false_negative_rate"] <= float(risk_false_negative_gate)
    )
    return {
        "passed": bool(passed and risk_passed),
        "checks": checks,
        "risk_calibration": {**risk_check, "passed": bool(risk_passed)},
        "criteria": {
            "utility_regret_tolerance": float(utility_regret_tolerance),
            "over_aggressive_tolerance": float(over_aggressive_tolerance),
            "rebuffer_regret_tolerance": float(rebuffer_regret_tolerance),
        },
    }


def _mode_delta(metrics: Mapping[str, object], baseline: Mapping[str, object]) -> Mapping[str, object]:
    return {
        "global": _critical_delta(metrics, baseline),
        "focus_2_5_mbps": _critical_delta(
            metrics.get("focus_2_5_mbps", {}),
            baseline.get("focus_2_5_mbps", {}),
        ),
        "spbc_v2_dpo_on_policy": _critical_delta(
            _rollout_source(metrics, "spbc_v2_dpo_on_policy"),
            _rollout_source(baseline, "spbc_v2_dpo_on_policy"),
        ),
    }


def _critical_delta(metrics: object, baseline: object) -> Mapping[str, float | None]:
    keys = (
        "selected_utility_regret_vs_best_immediate_mean",
        "selected_rebuffer_regret_vs_best_immediate_mean",
        "over_aggressive_rate_vs_oracle",
        "under_aggressive_rate_vs_oracle",
        "predicted_target_risk_rate",
        "predicted_rebuffer_s_mean",
        "predicted_reward_n_mean",
    )
    if not isinstance(metrics, Mapping) or not isinstance(baseline, Mapping):
        return {key: None for key in keys}
    result: dict[str, float | None] = {}
    for key in keys:
        if key in metrics and key in baseline:
            result[key] = round(float(metrics[key]) - float(baseline[key]), 9)
        else:
            result[key] = None
    return result


def _rollout_source(metrics: Mapping[str, object], source: str) -> Mapping[str, object]:
    by_source = metrics.get("by_rollout_source", {})
    if isinstance(by_source, Mapping):
        source_metrics = by_source.get(source, {})
        if isinstance(source_metrics, Mapping):
            return source_metrics
    return {}


def _argmax_valid(scores: Sequence[float], mask: Sequence[bool]) -> int:
    valid = [index for index, enabled in enumerate(mask) if bool(enabled)]
    if not valid:
        raise SpbcSpcV2HybridValidationError("sample has no valid actions")
    return max(valid, key=lambda index: (float(scores[index]), index))


def _topk_valid(scores: Sequence[float], mask: Sequence[bool], k: int) -> list[int]:
    valid = [index for index, enabled in enumerate(mask) if bool(enabled)]
    ranked = sorted(valid, key=lambda index: (float(scores[index]), index), reverse=True)
    return ranked[: max(1, int(k))]


def _batch_from_tensors(
    tensors: Sequence[torch.Tensor],
    indices: torch.Tensor,
    device: torch.device,
) -> tuple[torch.Tensor, ...]:
    return tuple(tensor.index_select(0, indices).to(device) for tensor in tensors)


def _resolve_limit(value: int | None | str, profile_value: int | None) -> int | None:
    if value == "profile":
        return profile_value
    if value is None:
        return None
    return int(value)


def _validate_hybrid_args(
    *,
    risk_threshold: float,
    rebuffer_threshold_s: float,
    rerank_top_k: int,
    utility_regret_tolerance: float,
    over_aggressive_tolerance: float,
    rebuffer_regret_tolerance: float,
    risk_brier_gate: float,
    risk_false_negative_gate: float,
) -> None:
    for name, value in (
        ("risk_threshold", risk_threshold),
        ("rebuffer_threshold_s", rebuffer_threshold_s),
        ("utility_regret_tolerance", utility_regret_tolerance),
        ("over_aggressive_tolerance", over_aggressive_tolerance),
        ("rebuffer_regret_tolerance", rebuffer_regret_tolerance),
        ("risk_brier_gate", risk_brier_gate),
        ("risk_false_negative_gate", risk_false_negative_gate),
    ):
        if not math.isfinite(float(value)):
            raise SpbcSpcV2HybridValidationError("{0} must be finite".format(name))
    if not 0.0 <= float(risk_threshold) <= 1.0:
        raise SpbcSpcV2HybridValidationError("risk_threshold must be in [0, 1]")
    if float(rebuffer_threshold_s) < 0.0:
        raise SpbcSpcV2HybridValidationError("rebuffer_threshold_s must be non-negative")
    if int(rerank_top_k) < 1:
        raise SpbcSpcV2HybridValidationError("rerank_top_k must be >= 1")


def _emit_progress(
    callback: Callable[[Mapping[str, object]], None] | None,
    event: str,
    message: str,
    **fields: object,
) -> None:
    if callback is None:
        return
    payload = {"event": event, "message": message}
    payload.update(fields)
    callback(payload)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

