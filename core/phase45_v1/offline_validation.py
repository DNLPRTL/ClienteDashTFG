from __future__ import annotations

import hashlib
import json
import math
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Mapping, Sequence

import torch

from core.evaluation.qoe import DEFAULT_LINEAR_REBUFFER_WEIGHT
from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, write_json, write_jsonl
from core.phase45_v1.constants import (
    DATA_FILENAMES,
    MEDIA_PROFILE_ID,
    OFFLINE_VALIDATION_PREDICTIONS_FILENAME,
    OFFLINE_VALIDATION_REPORT_FILENAME,
    OFFLINE_VALIDATION_REPORT_SCHEMA_ID,
    REWARD_VERSION,
    SPBC_CHECKPOINT_SCHEMA_ID,
    SPBC_MODEL_FILENAME,
    SPC_CHECKPOINT_SCHEMA_ID,
    SPC_MODEL_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.phase45_v1.spbc_training import CANDIDATE_FEATURES, SCALAR_FEATURES, SEQUENCE_FEATURES, SpbcAbrV1Policy
from core.phase45_v1.spc_training import SpcAbrV1Predictor
from core.phase45_v1.validation import validate_phase45_v1_dataset_dir


class Phase45OfflineValidationError(ValueError):
    """Raised when Phase 4-5 v1 offline model validation cannot proceed safely."""


@dataclass(frozen=True)
class OfflineValidationProfile:
    name: str
    max_validation_samples: int | None
    batch_size: int
    seed: int

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "max_validation_samples": self.max_validation_samples,
            "batch_size": self.batch_size,
            "seed": self.seed,
        }


OFFLINE_VALIDATION_PROFILES: dict[str, OfflineValidationProfile] = {
    "smoke": OfflineValidationProfile(name="smoke", max_validation_samples=512, batch_size=256, seed=450611),
    "pilot": OfflineValidationProfile(name="pilot", max_validation_samples=8000, batch_size=1024, seed=450621),
    "full_v1": OfflineValidationProfile(name="full_v1", max_validation_samples=None, batch_size=2048, seed=450631),
}


@dataclass(frozen=True)
class GuardDecision:
    action: int
    guard_applied: bool
    downshift_levels: int
    fallback_lowest_valid: bool
    proposed_risk: float
    selected_risk: float

    def to_json(self) -> dict[str, object]:
        return {
            "action": self.action,
            "guard_applied": self.guard_applied,
            "downshift_levels": self.downshift_levels,
            "fallback_lowest_valid": self.fallback_lowest_valid,
            "proposed_risk": self.proposed_risk,
            "selected_risk": self.selected_risk,
        }


@dataclass(frozen=True)
class OfflineExample:
    sample_id: str
    sequence: tuple[tuple[float, float], ...]
    scalars: tuple[float, ...]
    candidates: tuple[tuple[float, ...], ...]
    action_mask: tuple[bool, ...]
    oracle_action: int
    risk_targets: tuple[float, ...]
    rebuffer_s_by_action: tuple[float, ...]
    bitrate_bps_by_action: tuple[float, ...]
    previous_bitrate_bps: float
    throughput_bucket: str
    synthetic: bool


@dataclass(frozen=True)
class LoadedSpbcRuntime:
    model: SpbcAbrV1Policy
    normalization: Mapping[str, object]
    checkpoint: Mapping[str, object]


@dataclass(frozen=True)
class LoadedSpcRuntime:
    model: SpcAbrV1Predictor
    normalization: Mapping[str, object]
    checkpoint: Mapping[str, object]


def profile_by_name(name: str) -> OfflineValidationProfile:
    key = str(name).strip()
    if key not in OFFLINE_VALIDATION_PROFILES:
        raise Phase45OfflineValidationError("unknown offline validation profile: {0}".format(name))
    return OFFLINE_VALIDATION_PROFILES[key]


def validate_spbc_spc_offline(
    dataset_dir: object,
    spbc_checkpoint: object,
    spc_checkpoint: object,
    output_dir: object,
    *,
    profile: OfflineValidationProfile,
    overwrite: bool = False,
    device: str = "auto",
    risk_threshold: float = 0.50,
    batch_size: int | None = None,
    max_validation_samples: int | None | str = "profile",
    validate_dataset: bool = True,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
) -> Mapping[str, object]:
    _validate_threshold(risk_threshold)
    started = time.monotonic()
    _emit_progress(progress_callback, "preparing", "Preparando validacion offline spbc+spc")
    dataset_path = ensure_existing_dir(dataset_dir, purpose="phase45_v1 dataset")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v1 offline validation")
    if validate_dataset:
        _emit_progress(progress_callback, "validating_dataset", "Validando dataset phase45_v1")
        dataset_validation = validate_phase45_v1_dataset_dir(dataset_path)
    else:
        dataset_validation = {"status": "SKIPPED", "dataset_dir": str(dataset_path)}

    selected_device = resolve_torch_device(device)
    active_batch_size = int(batch_size if batch_size is not None else profile.batch_size)
    if active_batch_size <= 0:
        raise Phase45OfflineValidationError("batch_size must be positive")
    sample_limit = _resolve_limit(max_validation_samples, profile.max_validation_samples)
    _emit_progress(
        progress_callback,
        "loading_artifacts",
        "Cargando checkpoints y muestras",
        device_used=str(selected_device),
        validation_limit=sample_limit,
    )
    spbc_runtime = load_spbc_runtime(spbc_checkpoint, selected_device)
    spc_runtime = load_spc_runtime(spc_checkpoint, selected_device)
    examples = load_offline_examples(
        dataset_path / DATA_FILENAMES[VALIDATION_ROLE],
        limit=sample_limit,
    )
    if not examples:
        raise Phase45OfflineValidationError("offline validation requires validation examples")
    _emit_progress(progress_callback, "examples_loaded", "Muestras cargadas", validation_samples=len(examples))

    aggregators = {
        "spbc_only": _VariantMetricTotals(),
        "spbc_spc_guard": _VariantMetricTotals(),
        "oracle_reference": _VariantMetricTotals(),
    }
    bucket_aggregators: dict[str, dict[str, _VariantMetricTotals]] = defaultdict(
        lambda: {
            "spbc_only": _VariantMetricTotals(),
            "spbc_spc_guard": _VariantMetricTotals(),
            "oracle_reference": _VariantMetricTotals(),
        }
    )
    guard_totals = _GuardMetricTotals()
    prediction_rows = []
    batch_count = int(math.ceil(len(examples) / float(active_batch_size)))
    with torch.no_grad():
        for batch_index, start_index in enumerate(range(0, len(examples), active_batch_size), start=1):
            batch_examples = examples[start_index : start_index + active_batch_size]
            spbc_batch = _examples_to_model_tensors(batch_examples, spbc_runtime.normalization, selected_device)
            spc_batch = _examples_to_model_tensors(batch_examples, spc_runtime.normalization, selected_device)
            spbc_logits = spbc_runtime.model(*spbc_batch)["action_logits"].detach().cpu()
            spc_outputs = spc_runtime.model(*spc_batch)
            spc_risk = torch.sigmoid(spc_outputs["risk_logits"]).detach().cpu()
            top2 = torch.topk(spbc_logits, k=min(2, spbc_logits.shape[1]), dim=1).indices.tolist()
            spbc_actions = torch.argmax(spbc_logits, dim=1).tolist()

            for row_offset, example in enumerate(batch_examples):
                spbc_action = int(spbc_actions[row_offset])
                risk_scores = tuple(float(value) for value in spc_risk[row_offset].tolist())
                guard = apply_spc_guard(
                    proposed_action=spbc_action,
                    action_mask=example.action_mask,
                    risk_scores=risk_scores,
                    risk_threshold=risk_threshold,
                )
                top2_hit = int(example.oracle_action) in [int(value) for value in top2[row_offset]]
                observations = {
                    "spbc_only": _build_observation(
                        example=example,
                        variant="spbc_only",
                        action=spbc_action,
                        top2_hit=top2_hit,
                        spc_risk_score=risk_scores[spbc_action],
                    ),
                    "spbc_spc_guard": _build_observation(
                        example=example,
                        variant="spbc_spc_guard",
                        action=guard.action,
                        top2_hit=top2_hit,
                        spc_risk_score=risk_scores[guard.action],
                        guard=guard,
                    ),
                    "oracle_reference": _build_observation(
                        example=example,
                        variant="oracle_reference",
                        action=example.oracle_action,
                        top2_hit=True,
                        spc_risk_score=risk_scores[example.oracle_action],
                    ),
                }
                for variant, observation in observations.items():
                    aggregators[variant].add(observation)
                    bucket_aggregators[example.throughput_bucket][variant].add(observation)
                guard_totals.add(guard)
                prediction_rows.append(
                    {
                        "sample_id": example.sample_id,
                        "throughput_bucket": example.throughput_bucket,
                        "synthetic": example.synthetic,
                        "oracle_action": int(example.oracle_action),
                        "spbc_action": int(spbc_action),
                        "guarded_action": int(guard.action),
                        "guard_applied": bool(guard.guard_applied),
                        "guard_downshift_levels": int(guard.downshift_levels),
                        "spbc_action_spc_risk": round(float(risk_scores[spbc_action]), 6),
                        "guarded_action_spc_risk": round(float(risk_scores[guard.action]), 6),
                    }
                )
            if batch_index == 1 or batch_index == batch_count or batch_index % max(1, batch_count // 20) == 0:
                _emit_progress(
                    progress_callback,
                    "validation_batch",
                    "Validando batches",
                    batch=batch_index,
                    batches=batch_count,
                )

    metrics = {variant: aggregator.to_json() for variant, aggregator in aggregators.items()}
    by_bucket = {
        bucket: {variant: totals.to_json() for variant, totals in sorted(variant_totals.items())}
        for bucket, variant_totals in sorted(bucket_aggregators.items())
    }
    comparison = _build_comparison(metrics)
    offline_gate = _build_offline_gate(metrics, by_bucket, comparison)
    predictions_path = output_path / OFFLINE_VALIDATION_PREDICTIONS_FILENAME
    report_path = output_path / OFFLINE_VALIDATION_REPORT_FILENAME
    write_jsonl(predictions_path, prediction_rows)
    duration_s = time.monotonic() - started
    report = {
        "schema_id": OFFLINE_VALIDATION_REPORT_SCHEMA_ID,
        "human_readable_name": "Validacion offline conjunta spbc_abr_v1 + spc_abr_v1",
        "phase": "fase_4_5_v1_bloque6_validacion_offline_conjunta",
        "status": "PASS",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "dataset_dir": str(dataset_path),
        "dataset_validation": dict(dataset_validation),
        "output_dir": str(output_path),
        "spbc_checkpoint": str(Path(spbc_checkpoint).expanduser()),
        "spc_checkpoint": str(Path(spc_checkpoint).expanduser()),
        "spbc_checkpoint_sha256": _sha256_file(Path(spbc_checkpoint).expanduser()),
        "spc_checkpoint_sha256": _sha256_file(Path(spc_checkpoint).expanduser()),
        "profile": profile.to_json(),
        "device_requested": str(device),
        "device_used": str(selected_device),
        "batch_size": active_batch_size,
        "sample_counts_used": {VALIDATION_ROLE: len(examples)},
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "risk_threshold": float(risk_threshold),
        "variants": ["spbc_only", "spbc_spc_guard", "oracle_reference"],
        "metrics": metrics,
        "by_throughput_bucket": by_bucket,
        "guard_metrics": guard_totals.to_json(),
        "comparison": comparison,
        "offline_gate": offline_gate,
        "validation_duration_s": duration_s,
        "artifacts": {
            "validation_report": str(report_path),
            "predictions_jsonl": str(predictions_path),
            "predictions_jsonl_sha256": _sha256_file(predictions_path),
        },
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
        "classic_audit_fields_are_model_features": False,
        "spbc_checkpoint_used": True,
        "spc_checkpoint_used": True,
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
        "phase6_executed": False,
        "qoe_improvement_claimed": False,
        "sota_claimed": False,
        "real_world_generalization_claimed": False,
    }
    write_json(report_path, report)
    _emit_progress(
        progress_callback,
        "finished",
        "Validacion offline spbc+spc finalizada",
        validation_duration_s=duration_s,
        output_dir=str(output_path),
        offline_gate_status=offline_gate["status"],
    )
    return report


def load_spbc_runtime(path: object, device: torch.device) -> LoadedSpbcRuntime:
    checkpoint = _load_checkpoint(path, expected_schema_id=SPBC_CHECKPOINT_SCHEMA_ID, expected_key="spbc_abr_v1")
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
        raise Phase45OfflineValidationError("spbc checkpoint missing model_state_dict")
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return LoadedSpbcRuntime(model=model, normalization=_require_mapping(checkpoint.get("normalization"), "spbc normalization"), checkpoint=checkpoint)


def load_spc_runtime(path: object, device: torch.device) -> LoadedSpcRuntime:
    checkpoint = _load_checkpoint(path, expected_schema_id=SPC_CHECKPOINT_SCHEMA_ID, expected_key="spc_abr_v1")
    config = _require_mapping(checkpoint.get("model_config"), "spc model_config")
    model = SpcAbrV1Predictor(
        history_hidden_size=int(config["history_hidden_size"]),
        state_hidden_size=int(config["state_hidden_size"]),
        candidate_hidden_size=int(config["candidate_hidden_size"]),
        shared_hidden_size=int(config["shared_hidden_size"]),
        dropout=float(config["dropout"]),
    )
    state_dict = checkpoint.get("model_state_dict")
    if not isinstance(state_dict, Mapping):
        raise Phase45OfflineValidationError("spc checkpoint missing model_state_dict")
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return LoadedSpcRuntime(model=model, normalization=_require_mapping(checkpoint.get("normalization"), "spc normalization"), checkpoint=checkpoint)


def apply_spc_guard(
    *,
    proposed_action: int,
    action_mask: Sequence[bool],
    risk_scores: Sequence[float],
    risk_threshold: float = 0.50,
) -> GuardDecision:
    _validate_threshold(risk_threshold)
    if proposed_action < 0 or proposed_action >= len(action_mask):
        proposed_action = _lowest_valid_action(action_mask)
    proposed_risk = float(risk_scores[proposed_action]) if proposed_action < len(risk_scores) else 1.0
    if bool(action_mask[proposed_action]) and proposed_risk < float(risk_threshold):
        return GuardDecision(
            action=int(proposed_action),
            guard_applied=False,
            downshift_levels=0,
            fallback_lowest_valid=False,
            proposed_risk=proposed_risk,
            selected_risk=proposed_risk,
        )
    for action in range(int(proposed_action), -1, -1):
        if bool(action_mask[action]) and float(risk_scores[action]) < float(risk_threshold):
            return GuardDecision(
                action=int(action),
                guard_applied=True,
                downshift_levels=max(int(proposed_action) - int(action), 0),
                fallback_lowest_valid=False,
                proposed_risk=proposed_risk,
                selected_risk=float(risk_scores[action]),
            )
    fallback = _lowest_valid_action(action_mask)
    return GuardDecision(
        action=int(fallback),
        guard_applied=True,
        downshift_levels=max(int(proposed_action) - int(fallback), 0),
        fallback_lowest_valid=True,
        proposed_risk=proposed_risk,
        selected_risk=float(risk_scores[fallback]) if fallback < len(risk_scores) else 1.0,
    )


def load_offline_examples(path: object, limit: int | None = None) -> tuple[OfflineExample, ...]:
    examples = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                raw = json.loads(text)
            except json.JSONDecodeError as exc:
                raise Phase45OfflineValidationError("{0}: invalid JSONL line {1}".format(path, line_number)) from exc
            examples.append(_example_from_sample(raw, line_number))
            if limit is not None and len(examples) >= int(limit):
                break
    return tuple(examples)


def resolve_torch_device(requested: str) -> torch.device:
    key = str(requested).strip().lower()
    if key == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if key == "cuda" and not torch.cuda.is_available():
        raise Phase45OfflineValidationError("CUDA/ROCm device requested but torch.cuda.is_available() is false")
    if key not in {"cpu", "cuda"}:
        raise Phase45OfflineValidationError("device must be cpu, cuda or auto")
    return torch.device(key)


def _build_observation(
    *,
    example: OfflineExample,
    variant: str,
    action: int,
    top2_hit: bool,
    spc_risk_score: float,
    guard: GuardDecision | None = None,
) -> Mapping[str, object]:
    valid = 0 <= int(action) < len(example.action_mask) and bool(example.action_mask[int(action)])
    selected = int(action) if valid else _lowest_valid_action(example.action_mask)
    previous_bitrate = float(example.previous_bitrate_bps)
    bitrate_bps = float(example.bitrate_bps_by_action[selected])
    rebuffer_s = float(example.rebuffer_s_by_action[selected])
    smoothness_mbps = abs(bitrate_bps - previous_bitrate) / 1_000_000.0 if previous_bitrate > 0.0 else 0.0
    reward_n = bitrate_bps / 1_000_000.0 - DEFAULT_LINEAR_REBUFFER_WEIGHT * rebuffer_s - smoothness_mbps
    delta = selected - int(example.oracle_action)
    return {
        "variant": variant,
        "oracle_action": int(example.oracle_action),
        "action": int(selected),
        "valid_action": bool(valid),
        "top1_hit": int(selected) == int(example.oracle_action),
        "top2_hit": bool(top2_hit),
        "action_delta": int(delta),
        "over_aggressive": int(delta) > 0,
        "under_aggressive": int(delta) < 0,
        "spc_predicted_risk": float(spc_risk_score),
        "target_rebuffer_risk": float(example.risk_targets[selected]),
        "estimated_rebuffer_s": rebuffer_s,
        "estimated_reward_n": float(reward_n),
        "bitrate_kbps": bitrate_bps / 1000.0,
        "smoothness_mbps": smoothness_mbps,
        "guard_applied": bool(guard.guard_applied) if guard else False,
        "guard_downshift_levels": int(guard.downshift_levels) if guard else 0,
        "guard_fallback_lowest_valid": bool(guard.fallback_lowest_valid) if guard else False,
    }


@dataclass
class _VariantMetricTotals:
    weight: int = 0
    action_counts: Counter[str] | None = None
    target_counts: Counter[str] | None = None
    true_positive: Counter[str] | None = None
    false_positive: Counter[str] | None = None
    false_negative: Counter[str] | None = None
    top1: int = 0
    top2: int = 0
    invalid: int = 0
    over: int = 0
    under: int = 0
    action_sum: float = 0.0
    action_delta_sum: float = 0.0
    spc_risk_sum: float = 0.0
    target_risk_sum: float = 0.0
    rebuffer_sum: float = 0.0
    reward_sum: float = 0.0
    bitrate_sum: float = 0.0
    smoothness_sum: float = 0.0
    guard_applied_count: int = 0
    guard_downshift_sum: float = 0.0
    guard_fallback_count: int = 0

    def __post_init__(self) -> None:
        self.action_counts = Counter()
        self.target_counts = Counter()
        self.true_positive = Counter()
        self.false_positive = Counter()
        self.false_negative = Counter()

    def add(self, observation: Mapping[str, object]) -> None:
        self.weight += 1
        action = int(observation["action"])
        target = int(observation["oracle_action"])
        action_key = str(action)
        target_key = str(target)
        self.action_counts[action_key] += 1
        self.target_counts[target_key] += 1
        if bool(observation["top1_hit"]):
            self.top1 += 1
            self.true_positive[target_key] += 1
        else:
            self.false_positive[action_key] += 1
            self.false_negative[target_key] += 1
        if bool(observation["top2_hit"]):
            self.top2 += 1
        if not bool(observation["valid_action"]):
            self.invalid += 1
        if bool(observation["over_aggressive"]):
            self.over += 1
        if bool(observation["under_aggressive"]):
            self.under += 1
        self.action_sum += float(action)
        self.action_delta_sum += float(observation["action_delta"])
        self.spc_risk_sum += float(observation["spc_predicted_risk"])
        self.target_risk_sum += float(observation["target_rebuffer_risk"])
        self.rebuffer_sum += float(observation["estimated_rebuffer_s"])
        self.reward_sum += float(observation["estimated_reward_n"])
        self.bitrate_sum += float(observation["bitrate_kbps"])
        self.smoothness_sum += float(observation["smoothness_mbps"])
        if bool(observation["guard_applied"]):
            self.guard_applied_count += 1
            self.guard_downshift_sum += float(observation["guard_downshift_levels"])
        if bool(observation["guard_fallback_lowest_valid"]):
            self.guard_fallback_count += 1

    def to_json(self) -> dict[str, object]:
        denominator = max(float(self.weight), 1.0)
        class_keys = sorted(set(self.action_counts) | set(self.target_counts), key=lambda value: int(value))
        recalls = []
        f1_values = []
        for key in class_keys:
            tp = float(self.true_positive[key])
            fp = float(self.false_positive[key])
            fn = float(self.false_negative[key])
            if key in self.target_counts:
                recalls.append(tp / max(tp + fn, 1.0))
            denom = 2.0 * tp + fp + fn
            f1_values.append((2.0 * tp / denom) if denom > 0.0 else 0.0)
        guard_denominator = max(float(self.guard_applied_count), 1.0)
        return {
            "sample_count": int(self.weight),
            "top1_accuracy": round(float(self.top1) / denominator, 6),
            "top2_accuracy": round(float(self.top2) / denominator, 6),
            "balanced_accuracy": round(sum(recalls) / float(len(recalls) or 1), 6),
            "macro_f1": round(sum(f1_values) / float(len(f1_values) or 1), 6),
            "invalid_action_rate": round(float(self.invalid) / denominator, 6),
            "mean_action": round(self.action_sum / denominator, 6),
            "mean_action_delta_vs_oracle": round(self.action_delta_sum / denominator, 6),
            "over_aggressive_rate": round(float(self.over) / denominator, 6),
            "under_aggressive_rate": round(float(self.under) / denominator, 6),
            "spc_predicted_risk_mean": round(self.spc_risk_sum / denominator, 6),
            "target_rebuffer_risk_rate": round(self.target_risk_sum / denominator, 6),
            "estimated_rebuffer_s_mean": round(self.rebuffer_sum / denominator, 6),
            "estimated_reward_n_mean": round(self.reward_sum / denominator, 6),
            "bitrate_kbps_mean": round(self.bitrate_sum / denominator, 6),
            "smoothness_mbps_mean": round(self.smoothness_sum / denominator, 6),
            "action_distribution": {key: int(self.action_counts.get(key, 0)) for key in class_keys},
            "oracle_action_distribution": {key: int(self.target_counts.get(key, 0)) for key in class_keys},
            "guard_activation_rate": round(float(self.guard_applied_count) / denominator, 6),
            "guard_downshift_mean_when_applied": round(self.guard_downshift_sum / guard_denominator, 6),
            "guard_fallback_lowest_valid_rate": round(float(self.guard_fallback_count) / denominator, 6),
        }


@dataclass
class _GuardMetricTotals:
    weight: int = 0
    applied: int = 0
    fallback: int = 0
    downshift_sum: float = 0.0
    proposed_risk_sum: float = 0.0
    selected_risk_sum: float = 0.0

    def add(self, guard: GuardDecision) -> None:
        self.weight += 1
        if guard.guard_applied:
            self.applied += 1
            self.downshift_sum += float(guard.downshift_levels)
        if guard.fallback_lowest_valid:
            self.fallback += 1
        self.proposed_risk_sum += float(guard.proposed_risk)
        self.selected_risk_sum += float(guard.selected_risk)

    def to_json(self) -> dict[str, object]:
        denominator = max(float(self.weight), 1.0)
        applied_denominator = max(float(self.applied), 1.0)
        return {
            "sample_count": int(self.weight),
            "guard_activation_rate": round(float(self.applied) / denominator, 6),
            "guard_fallback_lowest_valid_rate": round(float(self.fallback) / denominator, 6),
            "downshift_mean_when_applied": round(self.downshift_sum / applied_denominator, 6),
            "proposed_risk_mean": round(self.proposed_risk_sum / denominator, 6),
            "selected_risk_mean": round(self.selected_risk_sum / denominator, 6),
            "selected_minus_proposed_risk_mean": round((self.selected_risk_sum - self.proposed_risk_sum) / denominator, 6),
        }


def _build_comparison(metrics: Mapping[str, Mapping[str, object]]) -> Mapping[str, object]:
    spbc = metrics["spbc_only"]
    guard = metrics["spbc_spc_guard"]
    return {
        "guard_minus_spbc": {
            "target_rebuffer_risk_rate": _delta(guard, spbc, "target_rebuffer_risk_rate"),
            "estimated_rebuffer_s_mean": _delta(guard, spbc, "estimated_rebuffer_s_mean"),
            "estimated_reward_n_mean": _delta(guard, spbc, "estimated_reward_n_mean"),
            "bitrate_kbps_mean": _delta(guard, spbc, "bitrate_kbps_mean"),
            "mean_action": _delta(guard, spbc, "mean_action"),
            "top1_accuracy": _delta(guard, spbc, "top1_accuracy"),
        },
        "guard_bitrate_retention_ratio": round(
            float(guard["bitrate_kbps_mean"]) / max(float(spbc["bitrate_kbps_mean"]), 1.0),
            6,
        ),
    }


def _build_offline_gate(
    metrics: Mapping[str, Mapping[str, object]],
    by_bucket: Mapping[str, Mapping[str, Mapping[str, object]]],
    comparison: Mapping[str, object],
) -> Mapping[str, object]:
    guard = metrics["spbc_spc_guard"]
    spbc = metrics["spbc_only"]
    deltas = _require_mapping(comparison["guard_minus_spbc"], "guard_minus_spbc")
    checks = {
        "invalid_action_rate_zero": float(guard["invalid_action_rate"]) == 0.0,
        "guard_does_not_increase_target_risk": float(deltas["target_rebuffer_risk_rate"]) <= 0.005,
        "guard_does_not_increase_rebuffer_s": float(deltas["estimated_rebuffer_s_mean"]) <= 0.02,
        "bitrate_retention_not_too_low": float(comparison["guard_bitrate_retention_ratio"]) >= 0.85,
        "top1_not_collapsed": float(guard["top1_accuracy"]) >= max(float(spbc["top1_accuracy"]) - 0.05, 0.0),
        "low_buckets_not_clearly_worse": _low_buckets_not_worse(by_bucket),
    }
    failed = [name for name, passed in checks.items() if not passed]
    status = "review_ready" if not failed else "needs_adjustment"
    recommendation = _recommend_next_step(checks, by_bucket, comparison)
    return {
        "status": status,
        "checks": checks,
        "failed_checks": failed,
        "recommendation": recommendation,
        "export_or_integration_authorized": False,
        "qoe_improvement_claim_authorized": False,
        "requires_human_review": True,
    }


def _recommend_next_step(
    checks: Mapping[str, bool],
    by_bucket: Mapping[str, Mapping[str, Mapping[str, object]]],
    comparison: Mapping[str, object],
) -> str:
    if checks["invalid_action_rate_zero"] is False:
        return "fix_validation_or_action_mask_before_any_retraining"
    if checks["bitrate_retention_not_too_low"] is False:
        return "tune_spc_guard_threshold_or_rules_before_retraining"
    if checks["low_buckets_not_clearly_worse"] is False:
        return "inspect_low_bucket_policy_and_consider_spbc_or_spc_retraining"
    deltas = _require_mapping(comparison["guard_minus_spbc"], "guard_minus_spbc")
    if float(deltas["target_rebuffer_risk_rate"]) > 0.005 or float(deltas["estimated_rebuffer_s_mean"]) > 0.02:
        return "inspect_spc_risk_calibration_before_export"
    return "candidate_for_export_design_review_not_formal_approval"


def _low_buckets_not_worse(by_bucket: Mapping[str, Mapping[str, Mapping[str, object]]]) -> bool:
    for bucket in ("lte_1_mbps", "1_2_mbps", "2_5_mbps"):
        if bucket not in by_bucket:
            continue
        spbc = by_bucket[bucket]["spbc_only"]
        guard = by_bucket[bucket]["spbc_spc_guard"]
        if float(guard["target_rebuffer_risk_rate"]) > float(spbc["target_rebuffer_risk_rate"]) + 0.01:
            return False
        if float(guard["estimated_rebuffer_s_mean"]) > float(spbc["estimated_rebuffer_s_mean"]) + 0.03:
            return False
    return True


def _examples_to_model_tensors(
    examples: Sequence[OfflineExample],
    normalization: Mapping[str, object],
    device: torch.device,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    sequence_mean = _numeric_tuple(normalization.get("sequence_mean"), "sequence_mean")
    sequence_std = _numeric_tuple(normalization.get("sequence_std"), "sequence_std")
    scalar_mean = _numeric_tuple(normalization.get("scalar_mean"), "scalar_mean")
    scalar_std = _numeric_tuple(normalization.get("scalar_std"), "scalar_std")
    candidate_mean = _numeric_tuple(normalization.get("candidate_mean"), "candidate_mean")
    candidate_std = _numeric_tuple(normalization.get("candidate_std"), "candidate_std")
    max_candidates = max(len(example.candidates) for example in examples)
    sequences = []
    scalars = []
    candidates = []
    masks = []
    for example in examples:
        sequences.append(_normalize_matrix(example.sequence, sequence_mean, sequence_std))
        scalars.append(_normalize_vector(example.scalars, scalar_mean, scalar_std))
        candidate_rows = [_normalize_vector(candidate, candidate_mean, candidate_std) for candidate in example.candidates]
        mask = [bool(value) for value in example.action_mask]
        while len(candidate_rows) < max_candidates:
            candidate_rows.append([0.0 for _ in CANDIDATE_FEATURES])
            mask.append(False)
        candidates.append(candidate_rows)
        masks.append(mask)
    return (
        torch.tensor(sequences, dtype=torch.float32, device=device),
        torch.tensor(scalars, dtype=torch.float32, device=device),
        torch.tensor(candidates, dtype=torch.float32, device=device),
        torch.tensor(masks, dtype=torch.bool, device=device),
    )


def _example_from_sample(sample: Mapping[str, object], line_number: int) -> OfflineExample:
    model_inputs = _require_mapping(sample.get("model_inputs"), "model_inputs")
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidates_raw = model_inputs.get("candidates")
    action_mask_raw = model_inputs.get("action_mask")
    if not isinstance(candidates_raw, list) or not isinstance(action_mask_raw, list):
        raise Phase45OfflineValidationError("line {0}: candidates/action_mask must be lists".format(line_number))
    spbc_targets = _require_mapping(sample.get("spbc_targets"), "spbc_targets")
    oracle_action = spbc_targets.get("oracle_action")
    if isinstance(oracle_action, bool) or not isinstance(oracle_action, int):
        raise Phase45OfflineValidationError("line {0}: oracle_action must be an integer".format(line_number))
    spc_targets = _require_mapping(sample.get("spc_targets"), "spc_targets")
    per_candidate = spc_targets.get("per_candidate_download_risk")
    if not isinstance(per_candidate, list):
        raise Phase45OfflineValidationError("line {0}: per_candidate_download_risk must be a list".format(line_number))
    sequence = _sequence_from_context(context)
    scalars = tuple(_finite_number(context.get(name), name) for name in SCALAR_FEATURES)
    candidates = tuple(
        tuple(_finite_number(_require_mapping(candidate, "candidate").get(name), name) for name in CANDIDATE_FEATURES)
        for candidate in candidates_raw
    )
    action_mask = tuple(bool(value) for value in action_mask_raw)
    risks = []
    rebuffer = []
    for index, item in enumerate(per_candidate):
        mapping = _require_mapping(item, "risk candidate {0}".format(index))
        risks.append(1.0 if _finite_number(mapping.get("rebuffer_risk"), "rebuffer_risk") >= 0.5 else 0.0)
        estimated_rebuffer = mapping.get("estimated_rebuffer_s")
        rebuffer.append(0.0 if estimated_rebuffer is None else max(_finite_number(estimated_rebuffer, "estimated_rebuffer_s"), 0.0))
    if len(candidates) != len(action_mask) or len(candidates) != len(risks):
        raise Phase45OfflineValidationError("line {0}: candidates, mask and risk lengths differ".format(line_number))
    if int(oracle_action) < 0 or int(oracle_action) >= len(candidates):
        raise Phase45OfflineValidationError("line {0}: oracle_action outside candidate range".format(line_number))
    metadata = _require_mapping(sample.get("metadata"), "metadata")
    return OfflineExample(
        sample_id=str(sample.get("sample_id", "line_{0}".format(line_number))),
        sequence=sequence,
        scalars=scalars,
        candidates=candidates,
        action_mask=action_mask,
        oracle_action=int(oracle_action),
        risk_targets=tuple(risks),
        rebuffer_s_by_action=tuple(rebuffer),
        bitrate_bps_by_action=tuple(float(candidate[2]) for candidate in candidates),
        previous_bitrate_bps=_finite_number(context.get("last_bitrate_bps"), "last_bitrate_bps"),
        throughput_bucket=str(metadata.get("throughput_bucket", "unknown")),
        synthetic=bool(metadata.get("synthetic") is True),
    )


def _sequence_from_context(context: Mapping[str, object]) -> tuple[tuple[float, float], ...]:
    throughput = _numeric_sequence(context.get("throughput_history_bps"), "throughput_history_bps")
    download = _numeric_sequence(context.get("download_time_history_s"), "download_time_history_s")
    if len(throughput) != len(download):
        raise Phase45OfflineValidationError("history feature lengths differ")
    return tuple((throughput[index], download[index]) for index in range(len(throughput)))


def _load_checkpoint(path: object, *, expected_schema_id: str, expected_key: str) -> Mapping[str, object]:
    checkpoint_path = Path(path).expanduser()
    if not checkpoint_path.is_file():
        raise Phase45OfflineValidationError("checkpoint does not exist: {0}".format(checkpoint_path))
    try:
        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
    if not isinstance(checkpoint, Mapping):
        raise Phase45OfflineValidationError("checkpoint must contain a mapping: {0}".format(checkpoint_path))
    if checkpoint.get("schema_id") != expected_schema_id:
        raise Phase45OfflineValidationError("checkpoint schema_id mismatch: {0}".format(checkpoint_path))
    if checkpoint.get("model_key") != expected_key:
        raise Phase45OfflineValidationError("checkpoint model_key mismatch: {0}".format(checkpoint_path))
    return checkpoint


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise Phase45OfflineValidationError("{0} must be an object".format(name))
    return value


def _numeric_sequence(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise Phase45OfflineValidationError("{0} must be a sequence".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _numeric_tuple(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise Phase45OfflineValidationError("{0} must be a numeric list".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _finite_number(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise Phase45OfflineValidationError("{0} must be numeric".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise Phase45OfflineValidationError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(parsed):
        raise Phase45OfflineValidationError("{0} must be finite".format(name))
    return parsed


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> list[float]:
    if len(values) != len(mean) or len(mean) != len(std):
        raise Phase45OfflineValidationError("normalization vector width mismatch")
    return [(float(value) - float(mean[index])) / max(float(std[index]), 1.0e-12) for index, value in enumerate(values)]


def _normalize_matrix(
    values: Sequence[Sequence[float]],
    mean: Sequence[float],
    std: Sequence[float],
) -> list[list[float]]:
    return [_normalize_vector(row, mean, std) for row in values]


def _lowest_valid_action(action_mask: Sequence[bool]) -> int:
    for index, value in enumerate(action_mask):
        if bool(value):
            return int(index)
    raise Phase45OfflineValidationError("action_mask has no valid action")


def _validate_threshold(value: float) -> None:
    numeric = float(value)
    if not math.isfinite(numeric) or numeric <= 0.0 or numeric >= 1.0:
        raise Phase45OfflineValidationError("risk_threshold must be finite and between 0 and 1")


def _resolve_limit(value: int | None | str, profile_value: int | None) -> int | None:
    if value == "profile":
        return profile_value
    if value is None:
        return None
    return int(value)


def _delta(left: Mapping[str, object], right: Mapping[str, object], key: str) -> float:
    return round(float(left[key]) - float(right[key]), 6)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _emit_progress(
    callback: Callable[[Mapping[str, object]], None] | None,
    event: str,
    message: str,
    **fields: object,
) -> None:
    if callback is None:
        return
    callback({"event": event, "message": message, **fields})
