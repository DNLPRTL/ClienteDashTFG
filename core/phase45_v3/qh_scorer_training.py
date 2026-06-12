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
from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES, DEFAULT_CONTEXT_HISTORY_LENGTH
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
    model_architecture: str = "shared_mlp_qh_candidate_scorer"
    history_gru_hidden_size: int = 64
    ce_loss_weight: float = 0.45
    q_value_loss_weight: float = 1.0
    pairwise_rank_loss_weight: float = 0.0
    pairwise_margin_scale: float = 1.0
    pairwise_q_gap_cap: float = 4.0
    pairwise_use_denormalized_q_gap: bool = False
    soft_q_kl_loss_weight: float = 0.0
    q_softmax_temperature: float = 1.0
    expected_regret_loss_weight: float = 0.0
    tail_regret_loss_weight: float = 0.0
    tail_regret_fraction: float = 0.20
    advantage_huber_loss_weight: float = 0.0
    advantage_scale: float = 1.0
    top_vs_bad_margin_loss_weight: float = 0.0
    top_vs_bad_regret_threshold: float = 0.50
    top_vs_bad_margin_scale: float = 1.0
    top_vs_bad_gap_cap: float = 4.0
    structured_cost_hinge_loss_weight: float = 0.0
    structured_cost_margin_scale: float = 0.55
    structured_cost_gap_cap: float = 8.0
    catastrophic_prob_loss_weight: float = 0.0
    catastrophic_regret_threshold: float = 2.0
    catastrophic_regret_cap: float = 20.0
    catastrophic_regret_power: float = 1.50
    slice_weight_throughput_2_5: float = 0.0
    slice_weight_buffer_0_4: float = 0.0
    slice_weight_buffer_4_16: float = 0.0
    slice_weight_buffer_16_32: float = 0.0
    slice_weight_rollout_qh_plus_one: float = 0.0
    slice_weight_max_regret_5: float = 0.0
    slice_weight_max_regret_20: float = 0.0
    slice_weight_max: float = 5.0
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
            "model_architecture": self.model_architecture,
            "history_gru_hidden_size": self.history_gru_hidden_size,
            "ce_loss_weight": self.ce_loss_weight,
            "q_value_loss_weight": self.q_value_loss_weight,
            "pairwise_rank_loss_weight": self.pairwise_rank_loss_weight,
            "pairwise_margin_scale": self.pairwise_margin_scale,
            "pairwise_q_gap_cap": self.pairwise_q_gap_cap,
            "pairwise_use_denormalized_q_gap": self.pairwise_use_denormalized_q_gap,
            "soft_q_kl_loss_weight": self.soft_q_kl_loss_weight,
            "q_softmax_temperature": self.q_softmax_temperature,
            "expected_regret_loss_weight": self.expected_regret_loss_weight,
            "tail_regret_loss_weight": self.tail_regret_loss_weight,
            "tail_regret_fraction": self.tail_regret_fraction,
            "advantage_huber_loss_weight": self.advantage_huber_loss_weight,
            "advantage_scale": self.advantage_scale,
            "top_vs_bad_margin_loss_weight": self.top_vs_bad_margin_loss_weight,
            "top_vs_bad_regret_threshold": self.top_vs_bad_regret_threshold,
            "top_vs_bad_margin_scale": self.top_vs_bad_margin_scale,
            "top_vs_bad_gap_cap": self.top_vs_bad_gap_cap,
            "structured_cost_hinge_loss_weight": self.structured_cost_hinge_loss_weight,
            "structured_cost_margin_scale": self.structured_cost_margin_scale,
            "structured_cost_gap_cap": self.structured_cost_gap_cap,
            "catastrophic_prob_loss_weight": self.catastrophic_prob_loss_weight,
            "catastrophic_regret_threshold": self.catastrophic_regret_threshold,
            "catastrophic_regret_cap": self.catastrophic_regret_cap,
            "catastrophic_regret_power": self.catastrophic_regret_power,
            "slice_weight_throughput_2_5": self.slice_weight_throughput_2_5,
            "slice_weight_buffer_0_4": self.slice_weight_buffer_0_4,
            "slice_weight_buffer_4_16": self.slice_weight_buffer_4_16,
            "slice_weight_buffer_16_32": self.slice_weight_buffer_16_32,
            "slice_weight_rollout_qh_plus_one": self.slice_weight_rollout_qh_plus_one,
            "slice_weight_max_regret_5": self.slice_weight_max_regret_5,
            "slice_weight_max_regret_20": self.slice_weight_max_regret_20,
            "slice_weight_max": self.slice_weight_max,
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
    "pilot_adv_regret_v1": QhScorerTrainingProfile(
        name="pilot_adv_regret_v1",
        epochs=40,
        batch_size=512,
        learning_rate=1.8e-4,
        hidden_sizes=(384, 192, 96),
        max_training_samples=None,
        max_validation_samples=None,
        ce_loss_weight=0.08,
        q_value_loss_weight=0.0,
        pairwise_rank_loss_weight=0.70,
        pairwise_margin_scale=0.60,
        pairwise_q_gap_cap=5.0,
        pairwise_use_denormalized_q_gap=True,
        soft_q_kl_loss_weight=1.20,
        q_softmax_temperature=0.35,
        expected_regret_loss_weight=1.60,
        tail_regret_loss_weight=0.90,
        tail_regret_fraction=0.25,
        advantage_huber_loss_weight=0.45,
        advantage_scale=1.0,
        top_vs_bad_margin_loss_weight=1.20,
        top_vs_bad_regret_threshold=0.50,
        top_vs_bad_margin_scale=0.45,
        top_vs_bad_gap_cap=5.0,
        mean_regret_tolerance=0.35,
        top1_accuracy_floor=0.55,
        seed=450924,
    ),
    "pilot_adv_regret_gru_v1": QhScorerTrainingProfile(
        name="pilot_adv_regret_gru_v1",
        epochs=44,
        batch_size=512,
        learning_rate=1.5e-4,
        hidden_sizes=(384, 192, 96),
        max_training_samples=None,
        max_validation_samples=None,
        model_architecture="gru_candidate_qh_scorer",
        history_gru_hidden_size=96,
        ce_loss_weight=0.08,
        q_value_loss_weight=0.0,
        pairwise_rank_loss_weight=0.70,
        pairwise_margin_scale=0.60,
        pairwise_q_gap_cap=5.0,
        pairwise_use_denormalized_q_gap=True,
        soft_q_kl_loss_weight=1.20,
        q_softmax_temperature=0.35,
        expected_regret_loss_weight=1.60,
        tail_regret_loss_weight=0.90,
        tail_regret_fraction=0.25,
        advantage_huber_loss_weight=0.45,
        advantage_scale=1.0,
        top_vs_bad_margin_loss_weight=1.20,
        top_vs_bad_regret_threshold=0.50,
        top_vs_bad_margin_scale=0.45,
        top_vs_bad_gap_cap=5.0,
        mean_regret_tolerance=0.35,
        top1_accuracy_floor=0.55,
        seed=450925,
    ),
    "pilot_adv_regret_hardneg_v1": QhScorerTrainingProfile(
        name="pilot_adv_regret_hardneg_v1",
        epochs=48,
        batch_size=512,
        learning_rate=1.4e-4,
        hidden_sizes=(384, 192, 96),
        max_training_samples=None,
        max_validation_samples=None,
        ce_loss_weight=0.05,
        q_value_loss_weight=0.0,
        pairwise_rank_loss_weight=0.50,
        pairwise_margin_scale=0.55,
        pairwise_q_gap_cap=8.0,
        pairwise_use_denormalized_q_gap=True,
        soft_q_kl_loss_weight=1.00,
        q_softmax_temperature=0.30,
        expected_regret_loss_weight=1.20,
        tail_regret_loss_weight=1.25,
        tail_regret_fraction=0.30,
        advantage_huber_loss_weight=0.30,
        advantage_scale=1.0,
        top_vs_bad_margin_loss_weight=1.40,
        top_vs_bad_regret_threshold=0.50,
        top_vs_bad_margin_scale=0.55,
        top_vs_bad_gap_cap=8.0,
        structured_cost_hinge_loss_weight=2.00,
        structured_cost_margin_scale=0.55,
        structured_cost_gap_cap=8.0,
        catastrophic_prob_loss_weight=2.40,
        catastrophic_regret_threshold=2.0,
        catastrophic_regret_cap=20.0,
        catastrophic_regret_power=1.50,
        slice_weight_throughput_2_5=1.25,
        slice_weight_buffer_0_4=1.10,
        slice_weight_buffer_4_16=0.90,
        slice_weight_buffer_16_32=0.35,
        slice_weight_rollout_qh_plus_one=1.00,
        slice_weight_max_regret_5=1.25,
        slice_weight_max_regret_20=1.50,
        slice_weight_max=5.0,
        mean_regret_tolerance=0.35,
        top1_accuracy_floor=0.55,
        seed=450926,
    ),
    "pilot_adv_regret_hardneg_v2": QhScorerTrainingProfile(
        name="pilot_adv_regret_hardneg_v2",
        epochs=44,
        batch_size=512,
        learning_rate=1.6e-4,
        hidden_sizes=(384, 192, 96),
        max_training_samples=None,
        max_validation_samples=None,
        ce_loss_weight=0.06,
        q_value_loss_weight=0.0,
        pairwise_rank_loss_weight=0.60,
        pairwise_margin_scale=0.55,
        pairwise_q_gap_cap=6.0,
        pairwise_use_denormalized_q_gap=True,
        soft_q_kl_loss_weight=1.05,
        q_softmax_temperature=0.32,
        expected_regret_loss_weight=1.45,
        tail_regret_loss_weight=1.00,
        tail_regret_fraction=0.25,
        advantage_huber_loss_weight=0.35,
        advantage_scale=1.0,
        top_vs_bad_margin_loss_weight=1.25,
        top_vs_bad_regret_threshold=0.50,
        top_vs_bad_margin_scale=0.50,
        top_vs_bad_gap_cap=6.0,
        structured_cost_hinge_loss_weight=0.75,
        structured_cost_margin_scale=0.35,
        structured_cost_gap_cap=6.0,
        catastrophic_prob_loss_weight=0.85,
        catastrophic_regret_threshold=5.0,
        catastrophic_regret_cap=20.0,
        catastrophic_regret_power=1.00,
        slice_weight_throughput_2_5=0.35,
        slice_weight_buffer_0_4=0.70,
        slice_weight_buffer_4_16=0.45,
        slice_weight_buffer_16_32=0.0,
        slice_weight_rollout_qh_plus_one=0.35,
        slice_weight_max_regret_5=0.60,
        slice_weight_max_regret_20=0.80,
        slice_weight_max=3.0,
        mean_regret_tolerance=0.35,
        top1_accuracy_floor=0.55,
        seed=450927,
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


class Phase45V3TemporalGruQhScorer(nn.Module):
    def __init__(
        self,
        context_dim: int,
        candidate_dim: int,
        hidden_sizes: Sequence[int],
        history_gru_hidden_size: int,
        history_length: int = DEFAULT_CONTEXT_HISTORY_LENGTH,
    ) -> None:
        super().__init__()
        self.context_dim = int(context_dim)
        self.candidate_dim = int(candidate_dim)
        self.hidden_sizes = tuple(int(value) for value in hidden_sizes)
        self.history_length = int(history_length)
        self.history_gru_hidden_size = int(history_gru_hidden_size)
        history_width = 2 * self.history_length
        if self.context_dim <= history_width:
            raise Phase45V3QhScorerTrainingError("context_dim must include history and scalar features")
        self.scalar_dim = self.context_dim - history_width
        self.history_gru = nn.GRU(
            input_size=2,
            hidden_size=self.history_gru_hidden_size,
            batch_first=True,
        )
        layers: list[nn.Module] = []
        width = self.history_gru_hidden_size + self.scalar_dim + self.candidate_dim
        for hidden in self.hidden_sizes:
            layers.append(nn.Linear(width, int(hidden)))
            layers.append(nn.ReLU())
            width = int(hidden)
        layers.append(nn.Linear(width, 1))
        self.scorer = nn.Sequential(*layers)

    def forward(self, context: torch.Tensor, candidates: torch.Tensor, action_mask: torch.Tensor) -> torch.Tensor:
        if context.ndim != 2 or candidates.ndim != 3 or action_mask.ndim != 2:
            raise Phase45V3QhScorerTrainingError("invalid temporal Q_H scorer tensor ranks")
        if context.shape[0] != candidates.shape[0] or action_mask.shape != candidates.shape[:2]:
            raise Phase45V3QhScorerTrainingError("temporal Q_H scorer tensor dimensions do not align")
        if context.shape[1] != self.context_dim or candidates.shape[2] != self.candidate_dim:
            raise Phase45V3QhScorerTrainingError("temporal Q_H scorer feature dimensions do not align")
        batch, candidate_count, _ = candidates.shape
        throughput_history = context[:, : self.history_length]
        download_time_history = context[:, self.history_length : 2 * self.history_length]
        scalars = context[:, 2 * self.history_length :]
        history = torch.stack((throughput_history, download_time_history), dim=2)
        _history_output, hidden = self.history_gru(history)
        history_embedding = hidden[-1]
        state_embedding = torch.cat((history_embedding, scalars), dim=1)
        expanded_state = state_embedding.unsqueeze(1).expand(batch, candidate_count, state_embedding.shape[1])
        scorer_input = torch.cat((expanded_state, candidates), dim=2)
        raw = self.scorer(scorer_input.reshape(batch * candidate_count, -1)).reshape(batch, candidate_count)
        return raw.masked_fill(~action_mask.to(dtype=torch.bool, device=raw.device), -1.0e9)

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": QH_SCORER_MODEL_CONFIG_SCHEMA_ID,
            "model_key": PHASE45_V3_QH_SCORER_MODEL_KEY,
            "model_type": "gru_candidate_qh_scorer",
            "context_dim": self.context_dim,
            "candidate_dim": self.candidate_dim,
            "history_length": self.history_length,
            "history_gru_hidden_size": self.history_gru_hidden_size,
            "scalar_dim": self.scalar_dim,
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
    train_tensors = examples_to_tensors(train_examples, normalization, sample_weight_profile=profile)
    validation_tensors = examples_to_tensors(validation_examples, normalization)
    model = _build_qh_scorer_model(profile).to(active_device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(profile.learning_rate), weight_decay=1.0e-5)
    train_loader = DataLoader(
        TensorDataset(*train_tensors),
        batch_size=int(profile.batch_size),
        shuffle=True,
        generator=torch.Generator().manual_seed(int(profile.seed)),
    )

    epochs = []
    best_state = None
    best_score: tuple[float, float, float, float] | None = None
    started = time.time()
    for epoch in range(1, int(profile.epochs) + 1):
        model.train()
        train_losses = []
        train_loss_parts: dict[str, float] = {}
        for batch in train_loader:
            batch = tuple(tensor.to(active_device) for tensor in batch)
            loss, loss_parts = _loss_for_batch(model, batch, profile, normalization)
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            train_losses.append(float(loss.detach().cpu()))
            for name, value in loss_parts.items():
                train_loss_parts[name] = train_loss_parts.get(name, 0.0) + float(value)
        validation_metrics = evaluate_qh_scorer(
            model,
            validation_tensors,
            normalization,
            active_device,
            examples=validation_examples,
            profile=profile,
        )
        epoch_record = {
            "epoch": epoch,
            "train_loss_mean": round(sum(train_losses) / float(len(train_losses)), 6) if train_losses else 0.0,
            "train_loss_components": {
                name: round(value / float(max(len(train_losses), 1)), 6) for name, value in sorted(train_loss_parts.items())
            },
            "validation": validation_metrics,
        }
        epochs.append(epoch_record)
        selection_score = _selection_score(validation_metrics, profile)
        if best_score is None or selection_score < best_score:
            best_score = selection_score
            best_state = {key: value.detach().cpu() for key, value in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    final_validation = evaluate_qh_scorer(
        model,
        validation_tensors,
        normalization,
        active_device,
        examples=validation_examples,
        profile=profile,
    )
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
        "training_sample_weight_summary": _sample_weight_summary(train_tensors[-1]),
        "sample_weight_metadata_used_as_model_input": False,
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
    sample_weight_profile: QhScorerTrainingProfile | None = None,
) -> tuple[torch.Tensor, ...]:
    contexts = []
    candidates = []
    masks = []
    q_values = []
    selected = []
    high_capacity = []
    sample_weights = []
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
        if sample_weight_profile is not None:
            sample_weights.append(_sample_weight_for_example(example, sample_weight_profile))
    tensors: tuple[torch.Tensor, ...] = (
        torch.tensor(contexts, dtype=torch.float32),
        torch.tensor(candidates, dtype=torch.float32),
        torch.tensor(masks, dtype=torch.bool),
        torch.tensor(q_values, dtype=torch.float32),
        torch.tensor(selected, dtype=torch.long),
        torch.tensor(high_capacity, dtype=torch.float32),
    )
    if sample_weight_profile is None:
        return tensors
    return tensors + (torch.tensor(sample_weights, dtype=torch.float32),)


def _build_qh_scorer_model(profile: QhScorerTrainingProfile) -> nn.Module:
    if profile.model_architecture == "shared_mlp_qh_candidate_scorer":
        return Phase45V3QhScorer(
            context_dim=len(CONTEXT_VECTOR_NAMES),
            candidate_dim=len(CANDIDATE_VECTOR_NAMES),
            hidden_sizes=profile.hidden_sizes,
        )
    if profile.model_architecture == "gru_candidate_qh_scorer":
        return Phase45V3TemporalGruQhScorer(
            context_dim=len(CONTEXT_VECTOR_NAMES),
            candidate_dim=len(CANDIDATE_VECTOR_NAMES),
            hidden_sizes=profile.hidden_sizes,
            history_gru_hidden_size=profile.history_gru_hidden_size,
        )
    raise Phase45V3QhScorerTrainingError("unknown Q_H scorer architecture: {0}".format(profile.model_architecture))


def evaluate_qh_scorer(
    model: nn.Module,
    tensors: tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor],
    normalization: QhScorerNormalization,
    device: torch.device,
    *,
    examples: Sequence[Mapping[str, object]] | None = None,
    profile: QhScorerTrainingProfile | None = None,
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
    regret_cpu = regret.detach().cpu().tolist()
    metrics: dict[str, object] = {
        "sample_count": int(selected.shape[0]),
        "top1_accuracy": round(float(accuracy.mean().detach().cpu()), 6),
        "mean_regret_q_h": round(float(regret.mean().detach().cpu()), 6),
        "p95_regret_q_h": round(_quantile(regret_cpu, 0.95), 6),
        "regret_gt_0_5_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 0.5), len(regret_cpu)), 6),
        "regret_gt_1_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 1.0), len(regret_cpu)), 6),
        "regret_gt_2_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 2.0), len(regret_cpu)), 6),
        "regret_gt_5_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 5.0), len(regret_cpu)), 6),
        "regret_gt_20_0_rate": round(_ratio(sum(1 for value in regret_cpu if float(value) > 20.0), len(regret_cpu)), 6),
        "predicted_action_distribution": _histogram(predicted_cpu),
        "target_action_distribution": _histogram(selected_cpu),
        "mean_regret_by_target_action": _mean_by_action(regret_cpu, selected_cpu),
        "mean_regret_by_predicted_action": _mean_by_action(regret_cpu, predicted_cpu),
        "confusion_target_predicted": _confusion_matrix(selected_cpu, predicted_cpu),
        "predicted_action0_rate": round(_ratio(sum(1 for item in predicted_cpu if int(item) == 0), len(predicted_cpu)), 6),
        "target_action0_rate": round(_ratio(sum(1 for item in selected_cpu if int(item) == 0), len(selected_cpu)), 6),
        "high_capacity_safe_state_count": int(high_mask.sum().detach().cpu()),
        "high_capacity_predicted_action0_rate": round(
            float(((predicted == 0) & high_mask).sum().detach().cpu()) / float(max(int(high_mask.sum().detach().cpu()), 1)),
            6,
        ),
    }
    if profile is not None:
        hard_negative_violation = _top_hard_negative_violation(scores, q_values, masks, profile)
        hard_cpu = hard_negative_violation.detach().cpu().tolist()
        metrics["top_hard_negative_violation_mean"] = round(sum(float(value) for value in hard_cpu) / float(len(hard_cpu)), 6)
        metrics["top_hard_negative_violation_p95"] = round(_quantile(hard_cpu, 0.95), 6)
    if examples is not None:
        metrics.update(_slice_regret_metrics(regret_cpu, examples))
    return metrics


def _loss_for_batch(
    model: nn.Module,
    batch: Sequence[torch.Tensor],
    profile: QhScorerTrainingProfile,
    normalization: QhScorerNormalization | None = None,
) -> tuple[torch.Tensor, Mapping[str, float]]:
    context, candidates, masks, q_values_norm, selected, _high_capacity, *optional = batch
    sample_weight = optional[0] if optional else None
    scores = model(context, candidates, masks)
    ce_loss = F.cross_entropy(scores, selected)
    valid = masks.to(dtype=torch.bool)
    q_values = _denormalize_q_values(q_values_norm, normalization)
    q_value_loss = (
        F.smooth_l1_loss(scores[valid], q_values_norm[valid])
        if float(profile.q_value_loss_weight) > 0.0
        else scores.new_tensor(0.0)
    )
    pairwise_q_values = q_values if profile.pairwise_use_denormalized_q_gap else q_values_norm
    pairwise_rank_loss = _pairwise_qh_rank_loss(scores, pairwise_q_values, valid, selected, profile)
    soft_q_kl_loss = _soft_q_kl_loss(scores, q_values, valid, profile)
    expected_regret_loss, per_sample_expected_regret = _expected_regret_loss(
        scores,
        q_values,
        valid,
        profile,
        sample_weight,
    )
    tail_regret_loss = _tail_regret_loss(per_sample_expected_regret, profile, sample_weight)
    advantage_huber_loss = _advantage_huber_loss(scores, q_values, valid, profile)
    top_vs_bad_margin_loss = _top_vs_bad_margin_loss(scores, q_values, valid, profile)
    structured_cost_hinge_loss, hard_negative_violation = _structured_cost_hinge_loss(
        scores,
        q_values,
        valid,
        profile,
        sample_weight,
    )
    catastrophic_prob_loss = _catastrophic_prob_loss(scores, q_values, valid, profile, sample_weight)
    loss = (
        float(profile.ce_loss_weight) * ce_loss
        + float(profile.q_value_loss_weight) * q_value_loss
        + float(profile.pairwise_rank_loss_weight) * pairwise_rank_loss
        + float(profile.soft_q_kl_loss_weight) * soft_q_kl_loss
        + float(profile.expected_regret_loss_weight) * expected_regret_loss
        + float(profile.tail_regret_loss_weight) * tail_regret_loss
        + float(profile.advantage_huber_loss_weight) * advantage_huber_loss
        + float(profile.top_vs_bad_margin_loss_weight) * top_vs_bad_margin_loss
        + float(profile.structured_cost_hinge_loss_weight) * structured_cost_hinge_loss
        + float(profile.catastrophic_prob_loss_weight) * catastrophic_prob_loss
    )
    return loss, {
        "ce_loss": float(ce_loss.detach().cpu()),
        "q_value_loss": float(q_value_loss.detach().cpu()),
        "pairwise_rank_loss": float(pairwise_rank_loss.detach().cpu()),
        "soft_q_kl_loss": float(soft_q_kl_loss.detach().cpu()),
        "expected_regret_loss": float(expected_regret_loss.detach().cpu()),
        "weighted_expected_regret_loss": float(expected_regret_loss.detach().cpu()),
        "tail_regret_loss": float(tail_regret_loss.detach().cpu()),
        "weighted_tail_regret_loss": float(tail_regret_loss.detach().cpu()),
        "advantage_huber_loss": float(advantage_huber_loss.detach().cpu()),
        "top_vs_bad_margin_loss": float(top_vs_bad_margin_loss.detach().cpu()),
        "structured_cost_hinge_loss": float(structured_cost_hinge_loss.detach().cpu()),
        "catastrophic_prob_loss": float(catastrophic_prob_loss.detach().cpu()),
        "sample_weight_mean": float(
            sample_weight.detach().mean().cpu() if sample_weight is not None else scores.new_tensor(1.0).cpu()
        ),
        "sample_weight_p95": _tensor_quantile(sample_weight.detach(), 0.95) if sample_weight is not None else 1.0,
        "top_hard_negative_violation_mean": float(hard_negative_violation.detach().mean().cpu()),
        "top_hard_negative_violation_p95": _tensor_quantile(hard_negative_violation.detach(), 0.95),
    }


def _denormalize_q_values(q_values_norm: torch.Tensor, normalization: QhScorerNormalization | None) -> torch.Tensor:
    if normalization is None:
        return q_values_norm
    return q_values_norm * float(normalization.q_value_std) + float(normalization.q_value_mean)


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


def _soft_q_kl_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
) -> torch.Tensor:
    if float(profile.soft_q_kl_loss_weight) <= 0.0:
        return scores.new_tensor(0.0)
    target_probs = _soft_q_target_probs(q_values, valid, float(profile.q_softmax_temperature))
    pred_log_probs = F.log_softmax(scores.masked_fill(~valid, -1.0e9), dim=1)
    target_log_probs = torch.log(torch.clamp(target_probs, min=1.0e-12))
    kl_by_sample = (target_probs * (target_log_probs - pred_log_probs)).masked_fill(~valid, 0.0).sum(dim=1)
    return kl_by_sample.mean()


def _soft_q_target_probs(q_values: torch.Tensor, valid: torch.Tensor, temperature: float) -> torch.Tensor:
    tau = max(float(temperature), 1.0e-6)
    q_best = _masked_max(q_values, valid).unsqueeze(1)
    advantage = torch.where(valid, q_values - q_best, torch.zeros_like(q_values))
    target_logits = (advantage / tau).masked_fill(~valid, -1.0e9)
    return F.softmax(target_logits, dim=1).masked_fill(~valid, 0.0)


def _expected_regret_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
    sample_weight: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
    if float(profile.expected_regret_loss_weight) <= 0.0 and float(profile.tail_regret_loss_weight) <= 0.0:
        empty = scores.new_tensor(0.0)
        return empty, scores.new_zeros(scores.shape[0])
    q_best = _masked_max(q_values, valid).unsqueeze(1)
    regret = torch.clamp(q_best - q_values, min=0.0).masked_fill(~valid, 0.0)
    pred_probs = F.softmax(scores.masked_fill(~valid, -1.0e9), dim=1).masked_fill(~valid, 0.0)
    per_sample = (pred_probs * regret).sum(dim=1)
    return _weighted_mean(per_sample, sample_weight), per_sample


def _tail_regret_loss(
    per_sample_expected_regret: torch.Tensor,
    profile: QhScorerTrainingProfile,
    sample_weight: torch.Tensor | None = None,
) -> torch.Tensor:
    if float(profile.tail_regret_loss_weight) <= 0.0:
        return per_sample_expected_regret.new_tensor(0.0)
    if per_sample_expected_regret.numel() == 0:
        return per_sample_expected_regret.new_tensor(0.0)
    fraction = min(max(float(profile.tail_regret_fraction), 0.0), 1.0)
    if fraction <= 0.0:
        return per_sample_expected_regret.new_tensor(0.0)
    top_count = max(int(math.ceil(float(per_sample_expected_regret.numel()) * fraction)), 1)
    top = torch.topk(per_sample_expected_regret, k=top_count, largest=True)
    if sample_weight is None:
        return top.values.mean()
    return _weighted_mean(top.values, sample_weight.gather(0, top.indices))


def _advantage_huber_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
) -> torch.Tensor:
    if float(profile.advantage_huber_loss_weight) <= 0.0:
        return scores.new_tensor(0.0)
    q_best = _masked_max(q_values, valid).unsqueeze(1)
    advantage = torch.where(valid, q_values - q_best, torch.zeros_like(q_values))
    advantage = advantage / max(float(profile.advantage_scale), 1.0e-6)
    centered_scores = scores - _masked_mean(scores, valid).unsqueeze(1)
    centered_advantage = advantage - _masked_mean(advantage, valid).unsqueeze(1)
    return F.smooth_l1_loss(centered_scores[valid], centered_advantage[valid])


def _top_vs_bad_margin_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
) -> torch.Tensor:
    if float(profile.top_vs_bad_margin_loss_weight) <= 0.0:
        return scores.new_tensor(0.0)
    q_masked = q_values.masked_fill(~valid, -torch.inf)
    best_idx = torch.argmax(q_masked, dim=1).unsqueeze(1)
    best_scores = torch.gather(scores, 1, best_idx)
    q_best = torch.gather(q_values, 1, best_idx)
    regret = torch.clamp(q_best - q_values, min=0.0).masked_fill(~valid, 0.0)
    bad_mask = valid & (regret >= float(profile.top_vs_bad_regret_threshold))
    if not bool(bad_mask.any().detach().cpu()):
        return scores.new_tensor(0.0)
    capped_regret = torch.clamp(regret, max=float(profile.top_vs_bad_gap_cap))
    margin = capped_regret * float(profile.top_vs_bad_margin_scale)
    score_gap = best_scores - scores
    raw = F.softplus(margin - score_gap)
    weights = capped_regret / max(float(profile.top_vs_bad_gap_cap), 1.0e-6)
    weighted = raw[bad_mask] * weights[bad_mask]
    denominator = torch.clamp(weights[bad_mask].sum(), min=1.0e-6)
    return weighted.sum() / denominator


def _structured_cost_hinge_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
    sample_weight: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor]:
    if float(profile.structured_cost_hinge_loss_weight) <= 0.0:
        zeros = scores.new_zeros(scores.shape[0])
        return scores.new_tensor(0.0), zeros
    q_masked = q_values.masked_fill(~valid, -torch.inf)
    best_idx = torch.argmax(q_masked, dim=1).unsqueeze(1)
    action_indices = torch.arange(scores.shape[1], device=scores.device).unsqueeze(0)
    negative_mask = valid & (action_indices != best_idx)
    if not bool(negative_mask.any().detach().cpu()):
        zeros = scores.new_zeros(scores.shape[0])
        return scores.new_tensor(0.0), zeros

    best_scores = torch.gather(scores, 1, best_idx)
    q_best = torch.gather(q_values, 1, best_idx)
    regret = torch.clamp(q_best - q_values, min=0.0).masked_fill(~valid, 0.0)
    capped_regret = torch.clamp(regret, max=float(profile.structured_cost_gap_cap))
    margin = capped_regret * float(profile.structured_cost_margin_scale)
    violation = scores - best_scores + margin
    relu_violation = F.relu(violation).masked_fill(~negative_mask, 0.0)
    per_sample = relu_violation.max(dim=1).values
    return _weighted_mean(per_sample, sample_weight), per_sample


def _catastrophic_prob_loss(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
    sample_weight: torch.Tensor | None = None,
) -> torch.Tensor:
    if float(profile.catastrophic_prob_loss_weight) <= 0.0:
        return scores.new_tensor(0.0)
    q_best = _masked_max(q_values, valid).unsqueeze(1)
    regret = torch.clamp(q_best - q_values, min=0.0).masked_fill(~valid, 0.0)
    bad_mask = valid & (regret >= float(profile.catastrophic_regret_threshold))
    if not bool(bad_mask.any().detach().cpu()):
        return scores.new_tensor(0.0)

    pred_probs = F.softmax(scores.masked_fill(~valid, -1.0e9), dim=1).masked_fill(~valid, 0.0)
    cap = max(float(profile.catastrophic_regret_cap), 1.0e-6)
    power = max(float(profile.catastrophic_regret_power), 0.0)
    cat_weight = torch.pow(torch.clamp(regret, max=cap) / cap, power)
    per_sample = (pred_probs * bad_mask.to(dtype=scores.dtype) * cat_weight).sum(dim=1)
    return _weighted_mean(per_sample, sample_weight)


def _top_hard_negative_violation(
    scores: torch.Tensor,
    q_values: torch.Tensor,
    valid: torch.Tensor,
    profile: QhScorerTrainingProfile,
) -> torch.Tensor:
    _loss, per_sample = _structured_cost_hinge_loss(scores, q_values, valid, profile, None)
    return per_sample


def _masked_max(values: torch.Tensor, valid: torch.Tensor) -> torch.Tensor:
    return values.masked_fill(~valid, -torch.inf).max(dim=1).values


def _masked_mean(values: torch.Tensor, valid: torch.Tensor) -> torch.Tensor:
    clean_values = values.masked_fill(~valid, 0.0)
    counts = valid.to(dtype=values.dtype).sum(dim=1).clamp_min(1.0)
    return clean_values.sum(dim=1) / counts


def _weighted_mean(values: torch.Tensor, sample_weight: torch.Tensor | None = None) -> torch.Tensor:
    if sample_weight is None:
        return values.mean()
    weights = sample_weight.to(device=values.device, dtype=values.dtype)
    denominator = torch.clamp(weights.sum(), min=1.0e-6)
    return (values * weights).sum() / denominator


def _tensor_quantile(values: torch.Tensor, q: float) -> float:
    if values.numel() == 0:
        return 0.0
    clean = values.detach().flatten().to("cpu", dtype=torch.float32)
    ordered = torch.sort(clean).values
    index = min(max(int(round(float(q) * (int(ordered.numel()) - 1))), 0), int(ordered.numel()) - 1)
    return float(ordered[index])


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


def _sample_weight_for_example(sample: Mapping[str, object], profile: QhScorerTrainingProfile) -> float:
    weight = 1.0
    metadata = sample.get("metadata", {})
    model_inputs = sample.get("model_inputs", {})
    context = model_inputs.get("context", {}) if isinstance(model_inputs, Mapping) else {}

    if isinstance(metadata, Mapping) and str(metadata.get("throughput_bucket")) == "2_5_mbps":
        weight += float(profile.slice_weight_throughput_2_5)

    buffer_s = _mapping_float(context, "buffer_s")
    if buffer_s is not None:
        if 0.0 <= buffer_s < 4.0:
            weight += float(profile.slice_weight_buffer_0_4)
        elif 4.0 <= buffer_s < 16.0:
            weight += float(profile.slice_weight_buffer_4_16)
        elif 16.0 <= buffer_s < 32.0:
            weight += float(profile.slice_weight_buffer_16_32)

    if isinstance(metadata, Mapping) and str(metadata.get("rollout_policy")) == "qh_plus_one":
        weight += float(profile.slice_weight_rollout_qh_plus_one)

    max_regret = _max_valid_qh_regret(sample)
    if max_regret >= 5.0:
        weight += float(profile.slice_weight_max_regret_5)
    if max_regret >= 20.0:
        weight += float(profile.slice_weight_max_regret_20)

    upper = max(float(profile.slice_weight_max), 1.0)
    return float(min(max(weight, 1.0), upper))


def _max_valid_qh_regret(sample: Mapping[str, object]) -> float:
    qh_targets = sample.get("qh_targets", {})
    if not isinstance(qh_targets, Mapping):
        return 0.0
    q_values = []
    for item in qh_targets.get("action_values", []):  # type: ignore[union-attr]
        if isinstance(item, Mapping):
            value = item.get("q_h_reward_n")
            if value is not None:
                q_values.append(_optional_finite_float(value))
    clean = [float(value) for value in q_values if value is not None and math.isfinite(float(value))]
    if len(clean) < 2:
        return 0.0
    return float(max(clean) - min(clean))


def _mapping_float(mapping: object, key: str) -> float | None:
    if not isinstance(mapping, Mapping):
        return None
    value = mapping.get(key)
    if value is None:
        return None
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


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


def _selection_score(metrics: Mapping[str, object], profile: QhScorerTrainingProfile) -> tuple[float, ...]:
    anti_collapse_excess = max(
        float(metrics["high_capacity_predicted_action0_rate"]) - profile.high_capacity_action0_tolerance,
        0.0,
    )
    return (
        float(metrics["mean_regret_q_h"]),
        float(metrics.get("regret_gt_2_0_rate", 0.0)),
        float(metrics["p95_regret_q_h"]),
        -float(metrics["top1_accuracy"]),
        anti_collapse_excess,
    )


def _resolve_device(device: str | None) -> torch.device:
    if device and str(device).strip().lower() not in {"auto", "default"}:
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


def _mean_by_action(values: Sequence[float], actions: Sequence[int]) -> dict[str, float]:
    totals: dict[int, float] = {}
    counts: dict[int, int] = {}
    for value, action in zip(values, actions):
        key = int(action)
        totals[key] = totals.get(key, 0.0) + float(value)
        counts[key] = counts.get(key, 0) + 1
    return {str(key): round(totals[key] / float(counts[key]), 6) for key in sorted(totals)}


def _confusion_matrix(targets: Sequence[int], predictions: Sequence[int]) -> dict[str, dict[str, int]]:
    matrix: dict[int, Counter[str]] = {}
    for target, prediction in zip(targets, predictions):
        target_key = int(target)
        if target_key not in matrix:
            matrix[target_key] = Counter()
        matrix[target_key][str(int(prediction))] += 1
    return {str(target): dict(sorted(counter.items())) for target, counter in sorted(matrix.items())}


def _slice_regret_metrics(regrets: Sequence[float], examples: Sequence[Mapping[str, object]]) -> Mapping[str, object]:
    if len(regrets) != len(examples):
        return {}
    buffer_groups: dict[str, list[float]] = {}
    throughput_groups: dict[str, list[float]] = {}
    rollout_groups: dict[str, list[float]] = {}
    for regret, example in zip(regrets, examples):
        metadata = example.get("metadata", {})
        model_inputs = example.get("model_inputs", {})
        context = model_inputs.get("context", {}) if isinstance(model_inputs, Mapping) else {}
        buffer_bucket = _buffer_bucket(_mapping_float(context, "buffer_s"))
        throughput_bucket = str(metadata.get("throughput_bucket")) if isinstance(metadata, Mapping) else "unknown"
        rollout_policy = str(metadata.get("rollout_policy")) if isinstance(metadata, Mapping) else "unknown"
        buffer_groups.setdefault(buffer_bucket, []).append(float(regret))
        throughput_groups.setdefault(throughput_bucket, []).append(float(regret))
        rollout_groups.setdefault(rollout_policy, []).append(float(regret))
    return {
        "mean_regret_q_h_by_buffer_bucket": _mean_mapping(buffer_groups),
        "mean_regret_q_h_by_throughput_bucket": _mean_mapping(throughput_groups),
        "mean_regret_q_h_by_rollout_policy": _mean_mapping(rollout_groups),
        "regret_summary_by_buffer_bucket": _summary_mapping(buffer_groups),
        "regret_summary_by_throughput_bucket": _summary_mapping(throughput_groups),
        "regret_summary_by_rollout_policy": _summary_mapping(rollout_groups),
    }


def _mean_mapping(groups: Mapping[str, Sequence[float]]) -> dict[str, float]:
    return {
        key: round(sum(float(value) for value in values) / float(len(values)), 6)
        for key, values in sorted(groups.items())
        if values
    }


def _summary_mapping(groups: Mapping[str, Sequence[float]]) -> dict[str, Mapping[str, object]]:
    output = {}
    for key, values in sorted(groups.items()):
        clean = [float(value) for value in values]
        output[key] = {
            "count": len(clean),
            "mean_regret_q_h": round(sum(clean) / float(len(clean)), 6) if clean else 0.0,
            "p95_regret_q_h": round(_quantile(clean, 0.95), 6),
            "regret_gt_2_0_rate": round(_ratio(sum(1 for value in clean if value > 2.0), len(clean)), 6),
        }
    return output


def _buffer_bucket(buffer_s: float | None) -> str:
    if buffer_s is None:
        return "unknown"
    if buffer_s < 4.0:
        return "00_04s"
    if buffer_s < 8.0:
        return "04_08s"
    if buffer_s < 16.0:
        return "08_16s"
    if buffer_s < 32.0:
        return "16_32s"
    return "32s_plus"


def _sample_weight_summary(weights: torch.Tensor) -> Mapping[str, object]:
    clean = weights.detach().flatten().to("cpu", dtype=torch.float32).tolist()
    return {
        "count": len(clean),
        "mean": round(sum(float(value) for value in clean) / float(len(clean)), 6) if clean else 0.0,
        "p95": round(_quantile(clean, 0.95), 6),
        "max": round(max(float(value) for value in clean), 6) if clean else 0.0,
        "metadata_used_as_model_input": False,
    }


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
