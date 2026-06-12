from __future__ import annotations

import hashlib
import json
import math
import random
import time
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_jsonl, write_json
from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES
from core.neural_abr.features import flatten_candidate_features, flatten_context_features
from core.phase45_v3.constants import (
    MEDIA_PROFILE_ID,
    QH_TARGET_ID,
    REWARD_VERSION,
    TRAINING_DATA_FILENAME,
    TRAINING_ROLE,
    VALIDATION_DATA_FILENAME,
    VALIDATION_ROLE,
)
from core.phase45_v3.validation import validate_phase45_v3_dataset_dir


PHASE45_V3_QH_SCORER_MODEL_KEY = "phase45_v3_qh_scorer"
QH_SCORER_MODEL_CONFIG_SCHEMA_ID = "phase45_v3_qh_scorer_model_config_v1"
QH_SCORER_TRAINING_REPORT_SCHEMA_ID = "phase45_v3_qh_scorer_training_report_v1"
QH_SCORER_CHECKPOINT_SCHEMA_ID = "phase45_v3_qh_scorer_checkpoint_v1"

QH_SCORER_MODEL_FILENAME = "modelo_phase45_v3_qh_scorer.pt"
QH_SCORER_MODEL_CONFIG_FILENAME = "configuracion_phase45_v3_qh_scorer.json"
QH_SCORER_NORMALIZATION_FILENAME = "normalizacion_phase45_v3_qh_scorer.json"
QH_SCORER_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_phase45_v3_qh_scorer.json"


class Phase45V3QhScorerTrainingError(ValueError):
    """Raised when Phase 4-5 v3 Q_H scorer training cannot proceed safely."""


@dataclass(frozen=True)
class QhScorerTrainingProfile:
    name: str
    epochs: int
    batch_size: int
    learning_rate: float
    hidden_sizes: tuple[int, ...]
    max_training_samples: int | None
    max_validation_samples: int | None
    ce_loss_weight: float = 0.45
    q_value_loss_weight: float = 1.0
    pairwise_rank_loss_weight: float = 0.0
    pairwise_margin_scale: float = 1.0
    pairwise_q_gap_cap: float = 4.0
    high_capacity_action0_tolerance: float = 0.05
    mean_regret_tolerance: float = 0.35
    top1_accuracy_floor: float = 0.50
    seed: int = 450901

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "learning_rate": self.learning_rate,
            "hidden_sizes": list(self.hidden_sizes),
            "max_training_samples": self.max_training_samples,
            "max_validation_samples": self.max_validation_samples,
            "ce_loss_weight": self.ce_loss_weight,
            "q_value_loss_weight": self.q_value_loss_weight,
            "pairwise_rank_loss_weight": self.pairwise_rank_loss_weight,
            "pairwise_margin_scale": self.pairwise_margin_scale,
            "pairwise_q_gap_cap": self.pairwise_q_gap_cap,
            "high_capacity_action0_tolerance": self.high_capacity_action0_tolerance,
            "mean_regret_tolerance": self.mean_regret_tolerance,
            "top1_accuracy_floor": self.top1_accuracy_floor,
            "seed": self.seed,
        }


QH_SCORER_TRAINING_PROFILES: dict[str, QhScorerTrainingProfile] = {
    "smoke": QhScorerTrainingProfile(
        name="smoke",
        epochs=1,
        batch_size=64,
        learning_rate=1.0e-3,
        hidden_sizes=(64, 32),
        max_training_samples=512,
        max_validation_samples=256,
        mean_regret_tolerance=999.0,
        top1_accuracy_floor=0.20,
        seed=450911,
    ),
    "pilot": QhScorerTrainingProfile(
        name="pilot",
        epochs=12,
        batch_size=512,
        learning_rate=5.0e-4,
        hidden_sizes=(192, 96, 48),
        max_training_samples=None,
        max_validation_samples=None,
        seed=450921,
    ),
    "pilot_plus": QhScorerTrainingProfile(
        name="pilot_plus",
        epochs=28,
        batch_size=512,
        learning_rate=2.5e-4,
        hidden_sizes=(256, 128, 64),
        max_training_samples=None,
        max_validation_samples=None,
        ce_loss_weight=0.35,
        q_value_loss_weight=1.35,
        mean_regret_tolerance=0.35,
        top1_accuracy_floor=0.55,
        seed=450922,
    ),
    "pilot_rank": QhScorerTrainingProfile(
        name="pilot_rank",
        epochs=28,
        batch_size=512,
        learning_rate=2.5e-4,
        hidden_sizes=(256, 128, 64),
        max_training_samples=None,
        max_validation_samples=None,
        ce_loss_weight=0.25,
        q_value_loss_weight=0.80,
        pairwise_rank_loss_weight=1.10,
        pairwise_margin_scale=1.0,
        pairwise_q_gap_cap=4.0,
        mean_regret_tolerance=0.35,
        top1_accuracy_floor=0.55,
        seed=450923,
    ),
    "full_v1": QhScorerTrainingProfile(
        name="full_v1",
        epochs=28,
        batch_size=1024,
        learning_rate=3.0e-4,
        hidden_sizes=(256, 128, 64),
        max_training_samples=None,
        max_validation_samples=None,
        mean_regret_tolerance=0.25,
        top1_accuracy_floor=0.58,
        seed=450931,
    ),
}


@dataclass(frozen=True)
class QhScorerNormalization:
    schema_id: str
    context_mean: tuple[float, ...]
    context_std: tuple[float, ...]
    candidate_mean: tuple[float, ...]
    candidate_std: tuple[float, ...]
    q_value_mean: float
    q_value_std: float
    fitted_on_data_role: str = TRAINING_ROLE

    def to_json(self) -> dict[str, object]:
        return {
            "schema_id": "phase45_v3_qh_scorer_normalization_v1",
            "fitted_on_data_role": self.fitted_on_data_role,
            "context_feature_names": list(CONTEXT_VECTOR_NAMES),
            "candidate_feature_names": list(CANDIDATE_VECTOR_NAMES),
            "context_mean": list(self.context_mean),
            "context_std": list(self.context_std),
            "candidate_mean": list(self.candidate_mean),
            "candidate_std": list(self.candidate_std),
            "q_value_mean": self.q_value_mean,
            "q_value_std": self.q_value_std,
        }


class Phase45V3QhScorer(nn.Module):
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
        self.scorer = nn.Sequential(*layers)

    def forward(self, context: torch.Tensor, candidates: torch.Tensor, action_mask: torch.Tensor) -> torch.Tensor:
        if context.ndim != 2 or candidates.ndim != 3 or action_mask.ndim != 2:
            raise Phase45V3QhScorerTrainingError("invalid Q_H scorer tensor ranks")
        if context.shape[0] != candidates.shape[0] or action_mask.shape != candidates.shape[:2]:
            raise Phase45V3QhScorerTrainingError("Q_H scorer tensor dimensions do not align")
        batch, candidate_count, _ = candidates.shape
        expanded_context = context.unsqueeze(1).expand(batch, candidate_count, context.shape[1])
        scorer_input = torch.cat([expanded_context, candidates], dim=2)
        raw = self.scorer(scorer_input.reshape(batch * candidate_count, -1)).reshape(batch, candidate_count)
        return raw.masked_fill(~action_mask.to(dtype=torch.bool, device=raw.device), -1.0e9)

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": QH_SCORER_MODEL_CONFIG_SCHEMA_ID,
            "model_key": PHASE45_V3_QH_SCORER_MODEL_KEY,
            "model_type": "shared_mlp_qh_candidate_scorer",
            "context_dim": self.context_dim,
            "candidate_dim": self.candidate_dim,
            "hidden_sizes": list(self.hidden_sizes),
            "controller_registered": False,
        }


def training_profile_by_name(name: str) -> QhScorerTrainingProfile:
    key = str(name).strip()
    if key not in QH_SCORER_TRAINING_PROFILES:
        raise Phase45V3QhScorerTrainingError("unknown Q_H scorer training profile: {0}".format(name))
    return QH_SCORER_TRAINING_PROFILES[key]


def train_phase45_v3_qh_scorer(
    dataset_dir: object,
    output_dir: object,
    profile: QhScorerTrainingProfile,
    *,
    overwrite: bool = False,
    device: str | None = None,
) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(dataset_dir, purpose="phase45_v3 Q_H dataset")
    validation = validate_phase45_v3_dataset_dir(data_dir)
    if validation["status"] != "PASS":
        raise Phase45V3QhScorerTrainingError("dataset validation failed: {0}".format(validation["errors"]))
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 Q_H scorer training")
    _seed_everything(profile.seed)
    active_device = _resolve_device(device)

    train_examples = load_qh_scorer_examples(data_dir / TRAINING_DATA_FILENAME, TRAINING_ROLE, profile.max_training_samples)
    validation_examples = load_qh_scorer_examples(
        data_dir / VALIDATION_DATA_FILENAME,
        VALIDATION_ROLE,
        profile.max_validation_samples,
    )
    normalization = fit_qh_scorer_normalization(train_examples)
    train_tensors = examples_to_tensors(train_examples, normalization)
    validation_tensors = examples_to_tensors(validation_examples, normalization)
    model = Phase45V3QhScorer(
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
    best_score = math.inf
    started = time.time()
    for epoch in range(1, int(profile.epochs) + 1):
        model.train()
        train_losses = []
        for batch in train_loader:
            batch = tuple(tensor.to(active_device) for tensor in batch)
            loss, loss_parts = _loss_for_batch(model, batch, profile)
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            train_losses.append(float(loss.detach().cpu()))
        validation_metrics = evaluate_qh_scorer(model, validation_tensors, normalization, active_device)
        epoch_record = {
            "epoch": epoch,
            "train_loss_mean": round(sum(train_losses) / float(len(train_losses)), 6) if train_losses else 0.0,
            "validation": validation_metrics,
        }
        epochs.append(epoch_record)
        selection_score = _selection_score(validation_metrics, profile)
        if selection_score < best_score:
            best_score = selection_score
            best_state = {key: value.detach().cpu() for key, value in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    final_validation = evaluate_qh_scorer(model, validation_tensors, normalization, active_device)
    gates = _evaluate_training_gates(final_validation, profile)
    checkpoint = {
        "schema_id": QH_SCORER_CHECKPOINT_SCHEMA_ID,
        "model_key": PHASE45_V3_QH_SCORER_MODEL_KEY,
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "model_config": model.config(),
        "normalization": normalization.to_json(),
        "model_state_dict": model.state_dict(),
        "profile": profile.to_json(),
        "dataset_dir": str(data_dir),
    }
    model_path = output_path / QH_SCORER_MODEL_FILENAME
    torch.save(checkpoint, model_path)
    model_config = dict(model.config())
    normalization_json = normalization.to_json()
    report = {
        "schema_id": QH_SCORER_TRAINING_REPORT_SCHEMA_ID,
        "status": "PASS" if not gates["failed"] else "REVIEW",
        "model_key": PHASE45_V3_QH_SCORER_MODEL_KEY,
        "dataset_dir": str(data_dir),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "device": str(active_device),
        "train_sample_count": len(train_examples),
        "validation_sample_count": len(validation_examples),
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
    write_json(output_path / QH_SCORER_MODEL_CONFIG_FILENAME, model_config)
    write_json(output_path / QH_SCORER_NORMALIZATION_FILENAME, normalization_json)
    write_json(output_path / QH_SCORER_TRAINING_REPORT_FILENAME, report)
    return report


def load_qh_scorer_examples(path: object, role: str, limit: int | None = None) -> tuple[Mapping[str, object], ...]:
    rows = list(read_jsonl(path))
    output = []
    for row in rows:
        if row.get("data_role") != role:
            raise Phase45V3QhScorerTrainingError("{0}: data_role mismatch".format(row.get("sample_id")))
        _sample_to_arrays(row)
        output.append(row)
        if limit is not None and len(output) >= int(limit):
            break
    if not output:
        raise Phase45V3QhScorerTrainingError("no Q_H scorer examples loaded from {0}".format(path))
    return tuple(output)


def fit_qh_scorer_normalization(examples: Sequence[Mapping[str, object]]) -> QhScorerNormalization:
    contexts = []
    candidates = []
    q_values = []
    for example in examples:
        context, candidate_rows, _mask, q_row, _selected, _high = _sample_to_arrays(example)
        contexts.append(context)
        candidates.extend(candidate_rows)
        q_values.extend(value for value, valid in zip(q_row, _mask) if valid and math.isfinite(value))
    context_mean, context_std = _mean_std_rows(contexts)
    candidate_mean, candidate_std = _mean_std_rows(candidates)
    q_mean, q_std = _mean_std(q_values)
    return QhScorerNormalization(
        schema_id="phase45_v3_qh_scorer_normalization_v1",
        context_mean=context_mean,
        context_std=context_std,
        candidate_mean=candidate_mean,
        candidate_std=candidate_std,
        q_value_mean=float(q_mean),
        q_value_std=float(q_std),
    )


def examples_to_tensors(
    examples: Sequence[Mapping[str, object]],
    normalization: QhScorerNormalization,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    contexts = []
    candidates = []
    masks = []
    q_values = []
    selected = []
    high_capacity = []
    for example in examples:
        context, candidate_rows, mask, q_row, selected_action, high_capacity_state = _sample_to_arrays(example)
        contexts.append(_normalize_vector(context, normalization.context_mean, normalization.context_std))
        candidates.append(
            [_normalize_vector(row, normalization.candidate_mean, normalization.candidate_std) for row in candidate_rows]
        )
        masks.append([1.0 if value else 0.0 for value in mask])
        q_values.append([(value - normalization.q_value_mean) / normalization.q_value_std for value in q_row])
        selected.append(int(selected_action))
        high_capacity.append(1.0 if high_capacity_state else 0.0)
    return (
        torch.tensor(contexts, dtype=torch.float32),
        torch.tensor(candidates, dtype=torch.float32),
        torch.tensor(masks, dtype=torch.bool),
        torch.tensor(q_values, dtype=torch.float32),
        torch.tensor(selected, dtype=torch.long),
        torch.tensor(high_capacity, dtype=torch.float32),
    )


def evaluate_qh_scorer(
    model: Phase45V3QhScorer,
    tensors: tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor],
    normalization: QhScorerNormalization,
    device: torch.device,
) -> Mapping[str, object]:
    model.eval()
    context, candidates, masks, q_values_norm, selected, high_capacity = tuple(tensor.to(device) for tensor in tensors)
    with torch.no_grad():
        scores = model(context, candidates, masks)
        predicted = torch.argmax(scores, dim=1)
    q_values = q_values_norm * float(normalization.q_value_std) + float(normalization.q_value_mean)
    best_q = torch.gather(q_values, 1, selected.unsqueeze(1)).squeeze(1)
    predicted_q = torch.gather(q_values, 1, predicted.unsqueeze(1)).squeeze(1)
    regret = torch.clamp(best_q - predicted_q, min=0.0)
    accuracy = (predicted == selected).to(dtype=torch.float32)
    high_mask = high_capacity > 0.5
    predicted_cpu = predicted.detach().cpu().tolist()
    selected_cpu = selected.detach().cpu().tolist()
    return {
        "sample_count": int(selected.shape[0]),
        "top1_accuracy": round(float(accuracy.mean().detach().cpu()), 6),
        "mean_regret_q_h": round(float(regret.mean().detach().cpu()), 6),
        "p95_regret_q_h": round(_quantile(regret.detach().cpu().tolist(), 0.95), 6),
        "predicted_action_distribution": _histogram(predicted_cpu),
        "target_action_distribution": _histogram(selected_cpu),
        "predicted_action0_rate": round(_ratio(sum(1 for item in predicted_cpu if int(item) == 0), len(predicted_cpu)), 6),
        "target_action0_rate": round(_ratio(sum(1 for item in selected_cpu if int(item) == 0), len(selected_cpu)), 6),
        "high_capacity_safe_state_count": int(high_mask.sum().detach().cpu()),
        "high_capacity_predicted_action0_rate": round(
            float(((predicted == 0) & high_mask).sum().detach().cpu()) / float(max(int(high_mask.sum().detach().cpu()), 1)),
            6,
        ),
    }


def _loss_for_batch(
    model: Phase45V3QhScorer,
    batch: Sequence[torch.Tensor],
    profile: QhScorerTrainingProfile,
) -> tuple[torch.Tensor, Mapping[str, float]]:
    context, candidates, masks, q_values, selected, _high_capacity = batch
    scores = model(context, candidates, masks)
    ce_loss = F.cross_entropy(scores, selected)
    valid = masks.to(dtype=torch.bool)
    q_value_loss = F.smooth_l1_loss(scores[valid], q_values[valid])
    pairwise_rank_loss = _pairwise_qh_rank_loss(scores, q_values, valid, selected, profile)
    loss = (
        float(profile.ce_loss_weight) * ce_loss
        + float(profile.q_value_loss_weight) * q_value_loss
        + float(profile.pairwise_rank_loss_weight) * pairwise_rank_loss
    )
    return loss, {
        "ce_loss": float(ce_loss.detach().cpu()),
        "q_value_loss": float(q_value_loss.detach().cpu()),
        "pairwise_rank_loss": float(pairwise_rank_loss.detach().cpu()),
    }


def _pairwise_qh_rank_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    selected: torch.Tensor,
    profile: QhScorerTrainingProfile,
) -> torch.Tensor:
    if float(profile.pairwise_rank_loss_weight) <= 0.0:
        return scores.new_tensor(0.0)
    action_indices = torch.arange(scores.shape[1], device=scores.device).unsqueeze(0)
    selected_column = selected.unsqueeze(1)
    negative_mask = valid & (action_indices != selected_column)
    if not bool(negative_mask.any().detach().cpu()):
        return scores.new_tensor(0.0)
    selected_scores = torch.gather(scores, 1, selected_column)
    selected_q = torch.gather(q_values, 1, selected_column)
    q_gap = torch.clamp(selected_q - q_values, min=0.0, max=float(profile.pairwise_q_gap_cap))
    margin = float(profile.pairwise_margin_scale) * q_gap
    score_gap = selected_scores - scores
    return F.relu(margin - score_gap)[negative_mask].mean()


def _sample_to_arrays(
    sample: Mapping[str, object],
) -> tuple[tuple[float, ...], tuple[tuple[float, ...], ...], tuple[bool, ...], tuple[float, ...], int, bool]:
    model_inputs = sample["model_inputs"]  # type: ignore[index]
    qh_targets = sample["qh_targets"]  # type: ignore[index]
    if not isinstance(model_inputs, Mapping) or not isinstance(qh_targets, Mapping):
        raise Phase45V3QhScorerTrainingError("invalid Q_H scorer sample shape")
    context_mapping = model_inputs["context"]  # type: ignore[index]
    candidates_raw = model_inputs["candidates"]  # type: ignore[index]
    action_mask_raw = model_inputs["action_mask"]  # type: ignore[index]
    if qh_targets.get("target_id") != QH_TARGET_ID:
        raise Phase45V3QhScorerTrainingError("unexpected Q_H target id")
    context = flatten_context_features(context_mapping)  # type: ignore[arg-type]
    candidates = tuple(flatten_candidate_features(candidate) for candidate in candidates_raw)  # type: ignore[arg-type]
    ladder_action_mask = tuple(bool(value) for value in action_mask_raw)  # type: ignore[arg-type]
    q_by_action: dict[int, float | None] = {}
    for item in qh_targets["action_values"]:  # type: ignore[index]
        if not isinstance(item, Mapping):
            raise Phase45V3QhScorerTrainingError("invalid Q_H action value row")
        q_by_action[int(item["action"])] = _optional_finite_float(item.get("q_h_reward_n"))
    q_values = tuple(
        q_by_action[index] if q_by_action.get(index) is not None else -1.0e9
        for index in range(len(candidates))
    )
    action_mask = tuple(
        bool(ladder_action_mask[index]) and q_by_action.get(index) is not None
        for index in range(len(candidates))
    )
    selected_action = int(qh_targets["selected_action"])
    if selected_action < 0 or selected_action >= len(action_mask) or not action_mask[selected_action]:
        raise Phase45V3QhScorerTrainingError("selected Q_H action is invalid under mask")
    high_capacity = float(context[-7]) >= 8.0 and float(context[4]) >= 2.0 * 4_300_000.0
    return context, candidates, action_mask, q_values, selected_action, bool(high_capacity)


def _evaluate_training_gates(metrics: Mapping[str, object], profile: QhScorerTrainingProfile) -> Mapping[str, object]:
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
    }
    failed = [name for name, gate in gates.items() if not gate["passed"]]
    return {"failed": failed, "gates": gates}


def _selection_score(metrics: Mapping[str, object], profile: QhScorerTrainingProfile) -> float:
    return (
        float(metrics["mean_regret_q_h"])
        + 0.25 * (1.0 - float(metrics["top1_accuracy"]))
        + 2.0 * max(float(metrics["high_capacity_predicted_action0_rate"]) - profile.high_capacity_action0_tolerance, 0.0)
    )


def _resolve_device(device: str | None) -> torch.device:
    if device:
        return torch.device(device)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _seed_everything(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed))


def _mean_std_rows(rows: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], tuple[float, ...]]:
    if not rows:
        raise Phase45V3QhScorerTrainingError("normalization rows must not be empty")
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
    clean = [float(value) for value in values if math.isfinite(float(value))]
    if not clean:
        raise Phase45V3QhScorerTrainingError("normalization values must not be empty")
    mean = sum(clean) / float(len(clean))
    variance = sum((value - mean) ** 2 for value in clean) / float(len(clean))
    std = math.sqrt(max(variance, 0.0))
    return float(mean), float(std if std > 1.0e-9 else 1.0)


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> list[float]:
    return [(float(value) - float(mean[index])) / float(std[index]) for index, value in enumerate(values)]


def _optional_finite_float(value: object) -> float | None:
    if value is None:
        return None
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError) as exc:
        raise Phase45V3QhScorerTrainingError("Q_H value must be finite") from exc
    if not math.isfinite(parsed):
        raise Phase45V3QhScorerTrainingError("Q_H value must be finite")
    return parsed


def _histogram(values: Sequence[int]) -> dict[str, int]:
    return dict(sorted(Counter(str(int(value)) for value in values).items()))


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _quantile(values: Sequence[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(float(value) for value in values)
    index = min(max(int(round(float(q) * (len(ordered) - 1))), 0), len(ordered) - 1)
    return ordered[index]


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
