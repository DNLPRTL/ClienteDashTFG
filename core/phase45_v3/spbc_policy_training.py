from __future__ import annotations

import hashlib
import json
import math
import random
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, write_json
from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES
from core.neural_abr.features import flatten_candidate_features, flatten_context_features
from core.phase45_v3.closedloop_spbc_spc_dataset import (
    SPBC_SPC_LEAKAGE_AUDIT_FILENAME,
    SPBC_SPC_SUMMARY_FILENAME,
    SPBC_SPC_TARGET_AUDIT_FILENAME,
    SPBC_SPC_TRAINING_DATA_FILENAME,
    SPBC_SPC_VALIDATION_DATA_FILENAME,
    SPBC_POLICY_TARGET_ID,
    SPC_CRITIC_TARGET_ID,
)
from core.phase45_v3.constants import MEDIA_PROFILE_ID, REWARD_VERSION, TRAINING_ROLE, VALIDATION_ROLE


PHASE45_V3_SPBC_POLICY_MODEL_KEY = "phase45_v3_spbc_policy"
SPBC_POLICY_CHECKPOINT_SCHEMA_ID = "phase45_v3_spbc_policy_checkpoint_v1"
SPBC_POLICY_MODEL_CONFIG_SCHEMA_ID = "phase45_v3_spbc_policy_model_config_v1"
SPBC_POLICY_NORMALIZATION_SCHEMA_ID = "phase45_v3_spbc_policy_normalization_v1"
SPBC_POLICY_TRAINING_REPORT_SCHEMA_ID = "phase45_v3_spbc_policy_training_report_v1"

SPBC_POLICY_MODEL_FILENAME = "modelo_phase45_v3_spbc_policy.pt"
SPBC_POLICY_MODEL_CONFIG_FILENAME = "configuracion_phase45_v3_spbc_policy.json"
SPBC_POLICY_NORMALIZATION_FILENAME = "normalizacion_phase45_v3_spbc_policy.json"
SPBC_POLICY_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_phase45_v3_spbc_policy.json"


class Phase45V3SpbcPolicyTrainingError(ValueError):
    """Raised when Phase45 v3 SPBC policy training cannot proceed safely."""


@dataclass(frozen=True)
class SpbcPolicyTrainingProfile:
    name: str
    epochs: int
    batch_size: int
    learning_rate: float
    hidden_sizes: tuple[int, ...]
    max_training_samples: int | None
    max_validation_samples: int | None
    soft_ce_loss_weight: float = 1.0
    hard_ce_loss_weight: float = 0.20
    expected_regret_loss_weight: float = 1.20
    tail_regret_loss_weight: float = 0.80
    tail_regret_fraction: float = 0.25
    structured_margin_loss_weight: float = 0.75
    structured_margin_scale: float = 0.55
    structured_margin_gap_cap: float = 8.0
    catastrophic_prob_loss_weight: float = 0.80
    sample_weight_max: float = 4.0
    high_capacity_action0_tolerance: float = 0.05
    mean_regret_tolerance: float = 0.35
    top1_accuracy_floor: float = 0.55
    catastrophic_action_tolerance: float = 0.04
    seed: int = 453001

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "learning_rate": self.learning_rate,
            "hidden_sizes": list(self.hidden_sizes),
            "max_training_samples": self.max_training_samples,
            "max_validation_samples": self.max_validation_samples,
            "soft_ce_loss_weight": self.soft_ce_loss_weight,
            "hard_ce_loss_weight": self.hard_ce_loss_weight,
            "expected_regret_loss_weight": self.expected_regret_loss_weight,
            "tail_regret_loss_weight": self.tail_regret_loss_weight,
            "tail_regret_fraction": self.tail_regret_fraction,
            "structured_margin_loss_weight": self.structured_margin_loss_weight,
            "structured_margin_scale": self.structured_margin_scale,
            "structured_margin_gap_cap": self.structured_margin_gap_cap,
            "catastrophic_prob_loss_weight": self.catastrophic_prob_loss_weight,
            "sample_weight_max": self.sample_weight_max,
            "high_capacity_action0_tolerance": self.high_capacity_action0_tolerance,
            "mean_regret_tolerance": self.mean_regret_tolerance,
            "top1_accuracy_floor": self.top1_accuracy_floor,
            "catastrophic_action_tolerance": self.catastrophic_action_tolerance,
            "seed": self.seed,
        }


SPBC_POLICY_TRAINING_PROFILES: dict[str, SpbcPolicyTrainingProfile] = {
    "smoke": SpbcPolicyTrainingProfile(
        name="smoke",
        epochs=1,
        batch_size=64,
        learning_rate=1.0e-3,
        hidden_sizes=(64, 32),
        max_training_samples=512,
        max_validation_samples=256,
        mean_regret_tolerance=999.0,
        top1_accuracy_floor=0.10,
        catastrophic_action_tolerance=1.0,
        seed=453011,
    ),
    "pilot_from_full_v1": SpbcPolicyTrainingProfile(
        name="pilot_from_full_v1",
        epochs=24,
        batch_size=2048,
        learning_rate=3.0e-4,
        hidden_sizes=(384, 192, 96),
        max_training_samples=160_000,
        max_validation_samples=40_000,
        seed=453001,
    ),
    "full_v1": SpbcPolicyTrainingProfile(
        name="full_v1",
        epochs=48,
        batch_size=4096,
        learning_rate=2.5e-4,
        hidden_sizes=(384, 192, 96),
        max_training_samples=None,
        max_validation_samples=None,
        soft_ce_loss_weight=1.0,
        hard_ce_loss_weight=0.15,
        expected_regret_loss_weight=1.35,
        tail_regret_loss_weight=0.90,
        structured_margin_loss_weight=0.80,
        catastrophic_prob_loss_weight=0.90,
        seed=453101,
    ),
}


@dataclass(frozen=True)
class SpbcPolicyNormalization:
    schema_id: str
    context_mean: tuple[float, ...]
    context_std: tuple[float, ...]
    candidate_mean: tuple[float, ...]
    candidate_std: tuple[float, ...]
    fitted_on_data_role: str = TRAINING_ROLE

    def to_json(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "fitted_on_data_role": self.fitted_on_data_role,
            "context_feature_names": list(CONTEXT_VECTOR_NAMES),
            "candidate_feature_names": list(CANDIDATE_VECTOR_NAMES),
            "context_mean": list(self.context_mean),
            "context_std": list(self.context_std),
            "candidate_mean": list(self.candidate_mean),
            "candidate_std": list(self.candidate_std),
        }


@dataclass(frozen=True)
class SpbcPolicyArrays:
    context: tuple[float, ...]
    candidates: tuple[tuple[float, ...], ...]
    action_mask: tuple[bool, ...]
    selected_action: int
    soft_targets: tuple[float, ...]
    q_h_regret_n: tuple[float, ...]
    catastrophic_mask: tuple[bool, ...]
    high_capacity_safe: bool
    sample_weight: float


class Phase45V3SpbcPolicy(nn.Module):
    def __init__(self, context_dim: int, candidate_dim: int, hidden_sizes: Sequence[int]) -> None:
        super().__init__()
        self.context_dim = int(context_dim)
        self.candidate_dim = int(candidate_dim)
        self.hidden_sizes = tuple(int(value) for value in hidden_sizes)
        layers: list[nn.Module] = []
        width = self.context_dim + self.candidate_dim
        for hidden in self.hidden_sizes:
            layers.append(nn.Linear(width, int(hidden)))
            layers.append(nn.ReLU())
            width = int(hidden)
        layers.append(nn.Linear(width, 1))
        self.policy = nn.Sequential(*layers)

    def forward(self, context: torch.Tensor, candidates: torch.Tensor, action_mask: torch.Tensor) -> torch.Tensor:
        if context.ndim != 2 or candidates.ndim != 3 or action_mask.ndim != 2:
            raise Phase45V3SpbcPolicyTrainingError("invalid SPBC policy tensor ranks")
        if context.shape[0] != candidates.shape[0] or action_mask.shape != candidates.shape[:2]:
            raise Phase45V3SpbcPolicyTrainingError("SPBC policy tensor dimensions do not align")
        batch, candidate_count, _ = candidates.shape
        expanded_context = context.unsqueeze(1).expand(batch, candidate_count, context.shape[1])
        policy_input = torch.cat([expanded_context, candidates], dim=2)
        raw = self.policy(policy_input.reshape(batch * candidate_count, -1)).reshape(batch, candidate_count)
        return raw.masked_fill(~action_mask.to(dtype=torch.bool, device=raw.device), -1.0e9)

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": SPBC_POLICY_MODEL_CONFIG_SCHEMA_ID,
            "model_key": PHASE45_V3_SPBC_POLICY_MODEL_KEY,
            "model_type": "shared_mlp_candidate_policy",
            "context_dim": self.context_dim,
            "candidate_dim": self.candidate_dim,
            "hidden_sizes": list(self.hidden_sizes),
            "controller_registered": False,
        }


def spbc_policy_training_profile_by_name(name: str) -> SpbcPolicyTrainingProfile:
    key = str(name).strip()
    if key not in SPBC_POLICY_TRAINING_PROFILES:
        raise Phase45V3SpbcPolicyTrainingError("unknown SPBC policy training profile: {0}".format(name))
    return SPBC_POLICY_TRAINING_PROFILES[key]


def train_phase45_v3_spbc_policy(
    dataset_dir: object,
    output_dir: object,
    profile: SpbcPolicyTrainingProfile,
    *,
    overwrite: bool = False,
    device: str | None = None,
) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(dataset_dir, purpose="phase45_v3 closed-loop SPBC/SPC dataset")
    dataset_validation = validate_spbc_policy_dataset_for_training(data_dir)
    if dataset_validation["status"] != "PASS":
        raise Phase45V3SpbcPolicyTrainingError("dataset validation failed: {0}".format(dataset_validation["errors"]))
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 SPBC policy training")
    _seed_everything(profile.seed)
    active_device = _resolve_device(device)

    train_examples = load_spbc_policy_examples(
        data_dir / SPBC_SPC_TRAINING_DATA_FILENAME,
        TRAINING_ROLE,
        profile.max_training_samples,
        seed=profile.seed,
    )
    validation_examples = load_spbc_policy_examples(
        data_dir / SPBC_SPC_VALIDATION_DATA_FILENAME,
        VALIDATION_ROLE,
        profile.max_validation_samples,
        seed=profile.seed + 17,
    )
    normalization = fit_spbc_policy_normalization(train_examples)
    train_tensors = spbc_policy_examples_to_tensors(train_examples, normalization)
    validation_tensors = spbc_policy_examples_to_tensors(validation_examples, normalization)

    model = Phase45V3SpbcPolicy(
        context_dim=len(CONTEXT_VECTOR_NAMES),
        candidate_dim=len(CANDIDATE_VECTOR_NAMES),
        hidden_sizes=profile.hidden_sizes,
    ).to(active_device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(profile.learning_rate), weight_decay=1.0e-5)
    train_loader = DataLoader(
        TensorDataset(*train_tensors),
        batch_size=int(profile.batch_size),
        shuffle=True,
        generator=torch.Generator().manual_seed(int(profile.seed)),
    )

    epochs = []
    best_state = None
    best_score: tuple[float, float, float, float, float] | None = None
    started = time.time()
    for epoch in range(1, int(profile.epochs) + 1):
        model.train()
        train_losses = []
        train_parts: dict[str, float] = {}
        for batch in train_loader:
            batch = tuple(tensor.to(active_device) for tensor in batch)
            loss, parts = _loss_for_batch(model, batch, profile)
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            train_losses.append(float(loss.detach().cpu()))
            for name, value in parts.items():
                train_parts[name] = train_parts.get(name, 0.0) + float(value)
        validation_metrics = evaluate_spbc_policy(model, validation_tensors, active_device)
        epoch_record = {
            "epoch": epoch,
            "train_loss_mean": round(sum(train_losses) / float(len(train_losses)), 6) if train_losses else 0.0,
            "train_loss_components": {
                name: round(value / float(max(len(train_losses), 1)), 6) for name, value in sorted(train_parts.items())
            },
            "validation": validation_metrics,
        }
        epochs.append(epoch_record)
        score = _selection_score(validation_metrics, profile)
        if best_score is None or score < best_score:
            best_score = score
            best_state = {key: value.detach().cpu() for key, value in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    final_validation = evaluate_spbc_policy(model, validation_tensors, active_device)
    gates = _evaluate_training_gates(final_validation, profile)
    checkpoint = {
        "schema_id": SPBC_POLICY_CHECKPOINT_SCHEMA_ID,
        "model_key": PHASE45_V3_SPBC_POLICY_MODEL_KEY,
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "model_config": model.config(),
        "normalization": normalization.to_json(),
        "model_state_dict": model.state_dict(),
        "profile": profile.to_json(),
        "dataset_dir": str(data_dir),
    }
    model_path = output_path / SPBC_POLICY_MODEL_FILENAME
    torch.save(checkpoint, model_path)
    report = {
        "schema_id": SPBC_POLICY_TRAINING_REPORT_SCHEMA_ID,
        "status": "PASS" if not gates["failed"] else "REVIEW",
        "model_key": PHASE45_V3_SPBC_POLICY_MODEL_KEY,
        "dataset_dir": str(data_dir),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "device": str(active_device),
        "train_sample_count": len(train_examples),
        "validation_sample_count": len(validation_examples),
        "training_sample_weight_summary": _sample_weight_summary(train_tensors[-1]),
        "sample_weight_metadata_used_as_model_input": False,
        "dataset_validation": dataset_validation,
        "epochs": epochs,
        "final_validation": final_validation,
        "gates": gates,
        "model_path": str(model_path),
        "model_sha256": _sha256_file(model_path),
        "elapsed_s": round(time.time() - started, 3),
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "candidate_model_created": True,
        "controller_integrated": False,
        "qoe_claims_authorized": False,
    }
    write_json(output_path / SPBC_POLICY_MODEL_CONFIG_FILENAME, dict(model.config()))
    write_json(output_path / SPBC_POLICY_NORMALIZATION_FILENAME, normalization.to_json())
    write_json(output_path / SPBC_POLICY_TRAINING_REPORT_FILENAME, report)
    return report


def validate_spbc_policy_dataset_for_training(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase45_v3 closed-loop SPBC/SPC dataset")
    errors = []
    for filename in (
        SPBC_SPC_SUMMARY_FILENAME,
        SPBC_SPC_LEAKAGE_AUDIT_FILENAME,
        SPBC_SPC_TARGET_AUDIT_FILENAME,
        SPBC_SPC_TRAINING_DATA_FILENAME,
        SPBC_SPC_VALIDATION_DATA_FILENAME,
    ):
        if not (data_dir / filename).is_file():
            errors.append("missing required file: {0}".format(filename))
    if errors:
        return {"status": "FAIL", "dataset_dir": str(data_dir), "errors": errors}

    summary = read_json(data_dir / SPBC_SPC_SUMMARY_FILENAME)
    leakage = read_json(data_dir / SPBC_SPC_LEAKAGE_AUDIT_FILENAME)
    target_audit = read_json(data_dir / SPBC_SPC_TARGET_AUDIT_FILENAME)
    content_ladder = summary.get("content_ladder", {}) if isinstance(summary.get("content_ladder"), Mapping) else {}
    if float(content_ladder.get("max_buffer_s", 0.0)) != 60.0:
        errors.append("content_ladder max_buffer_s must be 60.0")
    if leakage.get("status") != "PASS":
        errors.append("leakage audit status is not PASS")
    if target_audit.get("status") != "PASS":
        errors.append("target audit status is not PASS")
    if target_audit.get("future_information_is_target_only") is not True:
        errors.append("targets must mark future information as target-only")
    errors.extend(_peek_sample_errors(data_dir / SPBC_SPC_TRAINING_DATA_FILENAME, TRAINING_ROLE))
    errors.extend(_peek_sample_errors(data_dir / SPBC_SPC_VALIDATION_DATA_FILENAME, VALIDATION_ROLE))
    return {
        "status": "PASS" if not errors else "FAIL",
        "dataset_dir": str(data_dir),
        "errors": errors,
        "summary_sample_counts": summary.get("sample_counts", {}),
        "target_action_distribution": target_audit.get("policy_target_distribution", {}),
        "high_capacity_safe_target_action0_rate": target_audit.get("high_capacity_safe_target_action0_rate"),
    }


def load_spbc_policy_examples(
    path: object,
    role: str,
    limit: int | None,
    *,
    seed: int,
) -> tuple[SpbcPolicyArrays, ...]:
    rng = random.Random(int(seed))
    reservoir: list[SpbcPolicyArrays] = []
    seen = 0
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                row = json.loads(text)
            except json.JSONDecodeError as exc:
                raise Phase45V3SpbcPolicyTrainingError("{0}: invalid JSONL line {1}".format(path, line_number)) from exc
            if row.get("data_role") != role:
                raise Phase45V3SpbcPolicyTrainingError("{0}: data_role mismatch".format(row.get("sample_id")))
            arrays = _sample_to_arrays(row)
            seen += 1
            if limit is None:
                reservoir.append(arrays)
            elif len(reservoir) < int(limit):
                reservoir.append(arrays)
            else:
                index = rng.randint(0, seen - 1)
                if index < int(limit):
                    reservoir[index] = arrays
    if not reservoir:
        raise Phase45V3SpbcPolicyTrainingError("no SPBC policy examples loaded from {0}".format(path))
    return tuple(reservoir)


def fit_spbc_policy_normalization(examples: Sequence[SpbcPolicyArrays]) -> SpbcPolicyNormalization:
    contexts = [example.context for example in examples]
    candidates = [candidate for example in examples for candidate in example.candidates]
    context_mean, context_std = _mean_std_rows(contexts)
    candidate_mean, candidate_std = _mean_std_rows(candidates)
    return SpbcPolicyNormalization(
        schema_id=SPBC_POLICY_NORMALIZATION_SCHEMA_ID,
        context_mean=context_mean,
        context_std=context_std,
        candidate_mean=candidate_mean,
        candidate_std=candidate_std,
    )


def spbc_policy_examples_to_tensors(
    examples: Sequence[SpbcPolicyArrays],
    normalization: SpbcPolicyNormalization,
) -> tuple[torch.Tensor, ...]:
    contexts = []
    candidates = []
    masks = []
    selected = []
    soft_targets = []
    regrets = []
    catastrophic = []
    high_capacity = []
    sample_weights = []
    for example in examples:
        contexts.append(_normalize_vector(example.context, normalization.context_mean, normalization.context_std))
        candidates.append(
            [_normalize_vector(row, normalization.candidate_mean, normalization.candidate_std) for row in example.candidates]
        )
        masks.append([bool(value) for value in example.action_mask])
        selected.append(int(example.selected_action))
        soft_targets.append([float(value) for value in example.soft_targets])
        regrets.append([float(value) for value in example.q_h_regret_n])
        catastrophic.append([bool(value) for value in example.catastrophic_mask])
        high_capacity.append(1.0 if example.high_capacity_safe else 0.0)
        sample_weights.append(float(example.sample_weight))
    return (
        torch.tensor(contexts, dtype=torch.float32),
        torch.tensor(candidates, dtype=torch.float32),
        torch.tensor(masks, dtype=torch.bool),
        torch.tensor(selected, dtype=torch.long),
        torch.tensor(soft_targets, dtype=torch.float32),
        torch.tensor(regrets, dtype=torch.float32),
        torch.tensor(catastrophic, dtype=torch.bool),
        torch.tensor(high_capacity, dtype=torch.float32),
        torch.tensor(sample_weights, dtype=torch.float32),
    )


def evaluate_spbc_policy(
    model: nn.Module,
    tensors: tuple[torch.Tensor, ...],
    device: torch.device,
) -> Mapping[str, object]:
    model.eval()
    context, candidates, masks, selected, _soft, regrets, catastrophic, high_capacity, _weights = (
        tensor.to(device) for tensor in tensors
    )
    with torch.no_grad():
        logits = model(context, candidates, masks)
        predicted = torch.argmax(logits, dim=1)
        probs = F.softmax(logits.masked_fill(~masks, -1.0e9), dim=1).masked_fill(~masks, 0.0)
    predicted_regret = torch.gather(regrets, 1, predicted.unsqueeze(1)).squeeze(1)
    predicted_catastrophic = torch.gather(catastrophic.to(dtype=torch.float32), 1, predicted.unsqueeze(1)).squeeze(1)
    expected_regret = (probs * regrets.masked_fill(~masks, 0.0)).sum(dim=1)
    accuracy = (predicted == selected).to(dtype=torch.float32)
    high_mask = high_capacity > 0.5
    predicted_cpu = predicted.detach().cpu().tolist()
    selected_cpu = selected.detach().cpu().tolist()
    regret_cpu = predicted_regret.detach().cpu().tolist()
    expected_cpu = expected_regret.detach().cpu().tolist()
    cat_cpu = predicted_catastrophic.detach().cpu().tolist()
    high_count = int(high_mask.sum().detach().cpu())
    return {
        "sample_count": int(selected.shape[0]),
        "top1_accuracy": round(float(accuracy.mean().detach().cpu()), 6),
        "mean_regret_q_h": round(float(predicted_regret.mean().detach().cpu()), 6),
        "p95_regret_q_h": round(_quantile(regret_cpu, 0.95), 6),
        "expected_regret_mean": round(sum(float(value) for value in expected_cpu) / float(len(expected_cpu)), 6),
        "expected_regret_p95": round(_quantile(expected_cpu, 0.95), 6),
        "regret_gt_0_5_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 0.5), len(regret_cpu)), 6),
        "regret_gt_1_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 1.0), len(regret_cpu)), 6),
        "regret_gt_2_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 2.0), len(regret_cpu)), 6),
        "regret_gt_5_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 5.0), len(regret_cpu)), 6),
        "catastrophic_predicted_rate": round(_ratio(sum(1 for value in cat_cpu if float(value) > 0.5), len(cat_cpu)), 6),
        "predicted_action_distribution": _histogram(predicted_cpu),
        "target_action_distribution": _histogram(selected_cpu),
        "mean_regret_by_predicted_action": _mean_by_action(regret_cpu, predicted_cpu),
        "mean_regret_by_target_action": _mean_by_action(regret_cpu, selected_cpu),
        "predicted_action0_rate": round(_ratio(sum(1 for item in predicted_cpu if int(item) == 0), len(predicted_cpu)), 6),
        "target_action0_rate": round(_ratio(sum(1 for item in selected_cpu if int(item) == 0), len(selected_cpu)), 6),
        "high_capacity_safe_state_count": high_count,
        "high_capacity_predicted_action0_rate": round(
            float(((predicted == 0) & high_mask).sum().detach().cpu()) / float(max(high_count, 1)),
            6,
        ),
    }


def _loss_for_batch(
    model: nn.Module,
    batch: Sequence[torch.Tensor],
    profile: SpbcPolicyTrainingProfile,
) -> tuple[torch.Tensor, Mapping[str, float]]:
    context, candidates, masks, selected, soft_targets, regrets, catastrophic, _high, sample_weight = batch
    logits = model(context, candidates, masks)
    valid = masks.to(dtype=torch.bool)
    soft_targets = _renormalize_targets(soft_targets, valid)
    log_probs = F.log_softmax(logits.masked_fill(~valid, -1.0e9), dim=1)
    probs = F.softmax(logits.masked_fill(~valid, -1.0e9), dim=1).masked_fill(~valid, 0.0)
    soft_ce_per_sample = -(soft_targets * log_probs).masked_fill(~valid, 0.0).sum(dim=1)
    hard_ce_per_sample = F.cross_entropy(logits, selected, reduction="none")
    expected_regret_per_sample = (probs * regrets.masked_fill(~valid, 0.0)).sum(dim=1)
    tail_regret_loss = _tail_mean(expected_regret_per_sample, sample_weight, float(profile.tail_regret_fraction))
    margin_loss, margin_per_sample = _structured_margin_loss(logits, regrets, valid, selected, profile, sample_weight)
    catastrophic_per_sample = (probs * catastrophic.to(dtype=probs.dtype)).masked_fill(~valid, 0.0).sum(dim=1)
    soft_ce = _weighted_mean(soft_ce_per_sample, sample_weight)
    hard_ce = _weighted_mean(hard_ce_per_sample, sample_weight)
    expected_regret = _weighted_mean(expected_regret_per_sample, sample_weight)
    catastrophic_prob = _weighted_mean(catastrophic_per_sample, sample_weight)
    loss = (
        float(profile.soft_ce_loss_weight) * soft_ce
        + float(profile.hard_ce_loss_weight) * hard_ce
        + float(profile.expected_regret_loss_weight) * expected_regret
        + float(profile.tail_regret_loss_weight) * tail_regret_loss
        + float(profile.structured_margin_loss_weight) * margin_loss
        + float(profile.catastrophic_prob_loss_weight) * catastrophic_prob
    )
    return loss, {
        "soft_ce_loss": float(soft_ce.detach().cpu()),
        "hard_ce_loss": float(hard_ce.detach().cpu()),
        "expected_regret_loss": float(expected_regret.detach().cpu()),
        "tail_regret_loss": float(tail_regret_loss.detach().cpu()),
        "structured_margin_loss": float(margin_loss.detach().cpu()),
        "catastrophic_prob_loss": float(catastrophic_prob.detach().cpu()),
        "sample_weight_mean": float(sample_weight.detach().mean().cpu()),
        "sample_weight_p95": _tensor_quantile(sample_weight.detach(), 0.95),
        "structured_margin_per_sample_p95": _tensor_quantile(margin_per_sample.detach(), 0.95),
    }


def _sample_to_arrays(sample: Mapping[str, object]) -> SpbcPolicyArrays:
    model_inputs = _require_mapping(sample.get("model_inputs"), "model_inputs")
    policy_targets = _require_mapping(sample.get("spbc_policy_targets"), "spbc_policy_targets")
    critic_targets = _require_mapping(sample.get("spc_critic_targets"), "spc_critic_targets")
    if policy_targets.get("target_id") != SPBC_POLICY_TARGET_ID:
        raise Phase45V3SpbcPolicyTrainingError("unexpected SPBC policy target id")
    if critic_targets.get("target_id") != SPC_CRITIC_TARGET_ID:
        raise Phase45V3SpbcPolicyTrainingError("unexpected SPC critic target id")
    context_mapping = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidate_rows = _require_list(model_inputs.get("candidates"), "model_inputs.candidates")
    action_mask = tuple(bool(value) for value in _require_list(model_inputs.get("action_mask"), "model_inputs.action_mask"))
    context = flatten_context_features(context_mapping)
    candidates = tuple(flatten_candidate_features(candidate) for candidate in candidate_rows)  # type: ignore[arg-type]
    selected = int(policy_targets.get("selected_action", -1))
    soft_targets_raw = tuple(float(value) for value in _require_list(policy_targets.get("soft_action_weights"), "soft"))
    critic_values = _require_list(critic_targets.get("action_values"), "critic action_values")
    regrets_by_action: dict[int, float] = {}
    catastrophic_by_action: dict[int, bool] = {}
    for item in critic_values:
        row = _require_mapping(item, "critic action_value")
        action = int(row.get("action", -1))
        regret = _optional_finite_float(row.get("q_h_regret_n"))
        regrets_by_action[action] = 1.0e6 if regret is None else max(float(regret), 0.0)
        catastrophic_by_action[action] = bool(row.get("is_catastrophic_regret_2"))
    regrets = tuple(regrets_by_action.get(index, 1.0e6) for index in range(len(candidates)))
    catastrophic = tuple(catastrophic_by_action.get(index, True) for index in range(len(candidates)))
    if len(soft_targets_raw) != len(candidates) or len(action_mask) != len(candidates):
        raise Phase45V3SpbcPolicyTrainingError("SPBC policy sample action width mismatch")
    if selected < 0 or selected >= len(action_mask) or not action_mask[selected]:
        raise Phase45V3SpbcPolicyTrainingError("selected SPBC action is invalid under mask")
    high_capacity = float(context[10]) >= 8.0 and float(context[4]) >= 2.0 * 4_300_000.0
    return SpbcPolicyArrays(
        context=context,
        candidates=candidates,
        action_mask=action_mask,
        selected_action=selected,
        soft_targets=_normalize_probabilities(soft_targets_raw, action_mask),
        q_h_regret_n=regrets,
        catastrophic_mask=catastrophic,
        high_capacity_safe=bool(high_capacity),
        sample_weight=_sample_weight_from_arrays(regrets, context, sample),
    )


def _sample_weight_from_arrays(regrets: Sequence[float], context: Sequence[float], sample: Mapping[str, object]) -> float:
    max_regret = max(float(value) for value in regrets if math.isfinite(float(value)))
    weight = 1.0
    if max_regret >= 2.0:
        weight += 0.35
    if max_regret >= 5.0:
        weight += 0.45
    buffer_s = float(context[10])
    if 0.0 <= buffer_s < 4.0:
        weight += 0.25
    metadata = sample.get("metadata", {})
    if isinstance(metadata, Mapping) and str(metadata.get("throughput_bucket")) == "2_5_mbps":
        weight += 0.25
    return min(weight, 4.0)


def _peek_sample_errors(path: Path, role: str, limit: int = 20) -> list[str]:
    errors = []
    with path.open("r", encoding="utf-8") as handle:
        for index, line in enumerate(handle):
            if index >= limit:
                break
            try:
                row = json.loads(line)
                if row.get("data_role") != role:
                    errors.append("{0}[{1}]: data_role mismatch".format(role, index))
                _sample_to_arrays(row)
            except Exception as exc:  # noqa: BLE001 - validation must report compactly.
                errors.append("{0}[{1}]: {2}".format(role, index, exc))
    return errors


def _evaluate_training_gates(metrics: Mapping[str, object], profile: SpbcPolicyTrainingProfile) -> Mapping[str, object]:
    gates = {
        "top1_accuracy_floor": {
            "passed": float(metrics["top1_accuracy"]) >= float(profile.top1_accuracy_floor),
            "observed": metrics["top1_accuracy"],
            "threshold": ">= {0}".format(profile.top1_accuracy_floor),
        },
        "mean_regret_q_h": {
            "passed": float(metrics["mean_regret_q_h"]) <= float(profile.mean_regret_tolerance),
            "observed": metrics["mean_regret_q_h"],
            "threshold": "<= {0}".format(profile.mean_regret_tolerance),
        },
        "high_capacity_predicted_action0_rate": {
            "passed": float(metrics["high_capacity_predicted_action0_rate"]) <= float(profile.high_capacity_action0_tolerance),
            "observed": metrics["high_capacity_predicted_action0_rate"],
            "threshold": "<= {0}".format(profile.high_capacity_action0_tolerance),
        },
        "catastrophic_predicted_rate": {
            "passed": float(metrics["catastrophic_predicted_rate"]) <= float(profile.catastrophic_action_tolerance),
            "observed": metrics["catastrophic_predicted_rate"],
            "threshold": "<= {0}".format(profile.catastrophic_action_tolerance),
        },
    }
    failed = [name for name, gate in gates.items() if not gate["passed"]]
    return {"failed": failed, "gates": gates}


def _selection_score(metrics: Mapping[str, object], profile: SpbcPolicyTrainingProfile) -> tuple[float, float, float, float, float]:
    anti_collapse_excess = max(
        float(metrics["high_capacity_predicted_action0_rate"]) - float(profile.high_capacity_action0_tolerance),
        0.0,
    )
    catastrophic_excess = max(
        float(metrics["catastrophic_predicted_rate"]) - float(profile.catastrophic_action_tolerance),
        0.0,
    )
    return (
        float(metrics["mean_regret_q_h"]),
        float(metrics["regret_gt_2_0_rate"]),
        float(metrics["p95_regret_q_h"]),
        anti_collapse_excess,
        catastrophic_excess - float(metrics["top1_accuracy"]),
    )


def _structured_margin_loss(
    logits: torch.Tensor,
    regrets: torch.Tensor,
    valid: torch.Tensor,
    selected: torch.Tensor,
    profile: SpbcPolicyTrainingProfile,
    sample_weight: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
    selected_scores = torch.gather(logits, 1, selected.unsqueeze(1))
    selected_regret = torch.gather(regrets, 1, selected.unsqueeze(1))
    excess_regret = torch.clamp(regrets - selected_regret, min=0.0, max=float(profile.structured_margin_gap_cap))
    margins = excess_regret * float(profile.structured_margin_scale)
    violations = F.relu(logits - selected_scores + margins).masked_fill(~valid, 0.0)
    action_indices = torch.arange(logits.shape[1], device=logits.device).unsqueeze(0)
    violations = violations.masked_fill(action_indices == selected.unsqueeze(1), 0.0)
    per_sample = violations.max(dim=1).values
    return _weighted_mean(per_sample, sample_weight), per_sample


def _renormalize_targets(targets: torch.Tensor, valid: torch.Tensor) -> torch.Tensor:
    clean = targets.masked_fill(~valid, 0.0)
    total = clean.sum(dim=1, keepdim=True)
    fallback = valid.to(dtype=targets.dtype) / valid.to(dtype=targets.dtype).sum(dim=1, keepdim=True).clamp_min(1.0)
    return torch.where(total > 0.0, clean / total.clamp_min(1.0e-12), fallback)


def _tail_mean(values: torch.Tensor, sample_weight: torch.Tensor, fraction: float) -> torch.Tensor:
    fraction = min(max(float(fraction), 0.0), 1.0)
    if fraction <= 0.0 or values.numel() == 0:
        return values.new_tensor(0.0)
    count = max(int(math.ceil(float(values.numel()) * fraction)), 1)
    top = torch.topk(values, k=count, largest=True)
    return _weighted_mean(top.values, sample_weight.gather(0, top.indices))


def _weighted_mean(values: torch.Tensor, sample_weight: torch.Tensor | None = None) -> torch.Tensor:
    if sample_weight is None:
        return values.mean()
    weights = sample_weight.to(device=values.device, dtype=values.dtype)
    return (values * weights).sum() / weights.sum().clamp_min(1.0e-6)


def _normalize_probabilities(values: Sequence[float], action_mask: Sequence[bool]) -> tuple[float, ...]:
    clean = [max(float(value), 0.0) if bool(mask) else 0.0 for value, mask in zip(values, action_mask)]
    total = sum(clean)
    if total <= 0.0:
        valid_count = sum(1 for value in action_mask if value)
        return tuple((1.0 / float(valid_count)) if mask else 0.0 for mask in action_mask)
    return tuple(float(value) / float(total) for value in clean)


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> tuple[float, ...]:
    return tuple((float(value) - float(mu)) / max(float(sigma), 1.0e-6) for value, mu, sigma in zip(values, mean, std))


def _mean_std_rows(rows: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], tuple[float, ...]]:
    if not rows:
        raise Phase45V3SpbcPolicyTrainingError("normalization rows must not be empty")
    width = len(rows[0])
    columns = [[float(row[index]) for row in rows] for index in range(width)]
    means = []
    stds = []
    for column in columns:
        mean, std = _mean_std(column)
        means.append(mean)
        stds.append(std)
    return tuple(means), tuple(stds)


def _mean_std(values: Sequence[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 1.0
    mean = sum(float(value) for value in values) / float(len(values))
    variance = sum((float(value) - mean) ** 2 for value in values) / float(len(values))
    return float(mean), max(math.sqrt(max(variance, 0.0)), 1.0e-6)


def _sample_weight_summary(weights: torch.Tensor) -> Mapping[str, object]:
    values = weights.detach().cpu().flatten().tolist()
    return {
        "count": len(values),
        "mean": round(sum(float(value) for value in values) / float(len(values)), 6) if values else 0.0,
        "max": round(max(float(value) for value in values), 6) if values else 0.0,
        "p95": round(_quantile(values, 0.95), 6),
        "metadata_used_as_model_input": False,
    }


def _histogram(values: Iterable[int]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        key = str(int(value))
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def _mean_by_action(values: Sequence[float], actions: Sequence[int]) -> dict[str, float]:
    grouped: dict[int, list[float]] = {}
    for value, action in zip(values, actions):
        grouped.setdefault(int(action), []).append(float(value))
    return {str(action): round(sum(items) / float(len(items)), 6) for action, items in sorted(grouped.items())}


def _quantile(values: Sequence[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(float(value) for value in values)
    index = min(max(int(round(float(q) * (len(ordered) - 1))), 0), len(ordered) - 1)
    return ordered[index]


def _tensor_quantile(values: torch.Tensor, q: float) -> float:
    if values.numel() == 0:
        return 0.0
    clean = values.detach().flatten().to("cpu", dtype=torch.float32)
    ordered = torch.sort(clean).values
    index = min(max(int(round(float(q) * (int(ordered.numel()) - 1))), 0), int(ordered.numel()) - 1)
    return float(ordered[index])


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise Phase45V3SpbcPolicyTrainingError("{0} must be object".format(name))
    return value


def _require_list(value: object, name: str) -> list[object]:
    if not isinstance(value, list):
        raise Phase45V3SpbcPolicyTrainingError("{0} must be list".format(name))
    return value


def _optional_finite_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def _resolve_device(device: str | None) -> torch.device:
    if device and str(device).strip().lower() not in {"auto", "default"}:
        return torch.device(device)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _seed_everything(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
