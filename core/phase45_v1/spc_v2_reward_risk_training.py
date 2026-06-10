from __future__ import annotations

import hashlib
import json
import math
import random
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, write_json
from core.phase45_v1.constants import (
    MEDIA_PROFILE_ID,
    REWARD_VERSION,
    SPBC_CHECKPOINT_SCHEMA_ID,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.phase45_v1.preference_dataset_v2 import V2_DATA_FILENAMES, validate_phase45_v2_dataset_dir
from core.phase45_v1.spbc_training import (
    CANDIDATE_FEATURES,
    SCALAR_FEATURES,
    SEQUENCE_FEATURES,
    SpbcAbrV1Policy,
)
from core.phase45_v1.spbc_v2_dpo_training import (
    FOCUS_THROUGHPUT_BUCKET,
    MODEL_INPUT_KEYS,
    SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
    SPBC_V2_DPO_MODEL_KEY,
    SpbcAbrV2DpoPolicy,
    SpbcV2DpoExample,
    SpbcV2DpoTrainingError,
    examples_to_tensors,
    load_spbc_v2_dpo_examples,
    _PolicyMetricTotals,
    _policy_observations,
)


SPC_V2_REWARD_RISK_MODEL_KEY = "spc_abr_v2_reward_risk"
SPC_V2_REWARD_RISK_MODEL_CONFIG_SCHEMA_ID = "phase45_v2_spc_reward_risk_model_config_v1"
SPC_V2_REWARD_RISK_TRAINING_REPORT_SCHEMA_ID = "phase45_v2_spc_reward_risk_training_report_v1"
SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID = "phase45_v2_spc_reward_risk_checkpoint_v1"

SPC_V2_REWARD_RISK_MODEL_FILENAME = "modelo_spc_abr_v2_reward_risk.pt"
SPC_V2_REWARD_RISK_MODEL_CONFIG_FILENAME = "configuracion_spc_abr_v2_reward_risk.json"
SPC_V2_REWARD_RISK_NORMALIZATION_FILENAME = "normalizacion_spc_abr_v2_reward_risk.json"
SPC_V2_REWARD_RISK_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_spc_abr_v2_reward_risk.json"

REBUFFER_PREDICTION_CAP_S = 4.0
QOE_GAP_PREDICTION_CAP = 8.0
SMOOTHNESS_PREDICTION_CAP_MBPS = 5.0
_LOSS_METRIC_NAMES = (
    "loss",
    "best_immediate_ce_loss",
    "pairwise_score_loss",
    "reward_loss",
    "rebuffer_loss",
    "qoe_gap_loss",
    "smoothness_loss",
    "risk_loss",
    "over_aggressive_score_probability_loss",
    "safe_utility_rank_loss",
)


class SpcV2RewardRiskTrainingError(ValueError):
    """Raised when spc_abr_v2_reward_risk offline training cannot proceed safely."""


@dataclass(frozen=True)
class SpcV2RewardRiskTrainingProfile:
    name: str
    epochs: int
    batch_size: int
    learning_rate: float
    max_training_samples: int | None
    max_validation_samples: int | None
    history_hidden_size: int
    state_hidden_size: int
    candidate_hidden_size: int
    shared_hidden_size: int
    dropout: float
    best_immediate_ce_loss_weight: float = 0.20
    pairwise_score_loss_weight: float = 0.35
    reward_loss_weight: float = 1.00
    rebuffer_loss_weight: float = 0.85
    qoe_gap_loss_weight: float = 0.65
    smoothness_loss_weight: float = 0.25
    risk_loss_weight: float = 0.85
    score_rebuffer_weight: float = 4.30
    score_risk_weight: float = 0.60
    score_smoothness_weight: float = 0.20
    score_qoe_gap_weight: float = 0.35
    pairwise_margin_scale: float = 0.15
    risk_positive_weight: float = 2.00
    focus_bucket_sample_weight: float = 1.55
    severe_error_sample_weight: float = 1.35
    safe_vs_rebuffer_pair_weight: float = 1.35
    over_aggressive_rebuffer_action_weight: float = 2.10
    over_aggressive_score_loss_weight: float = 0.0
    safe_utility_rank_loss_weight: float = 0.0
    safe_utility_margin: float = 0.20
    max_pair_weight: float = 6.0
    selection_focus_weight: float = 1.25
    selection_rebuffer_weight: float = 4.30
    selection_over_aggressive_weight: float = 0.35
    selection_invalid_weight: float = 10.0
    selection_prediction_loss_weight: float = 0.04
    seed: int = 450801

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "learning_rate": self.learning_rate,
            "max_training_samples": self.max_training_samples,
            "max_validation_samples": self.max_validation_samples,
            "history_hidden_size": self.history_hidden_size,
            "state_hidden_size": self.state_hidden_size,
            "candidate_hidden_size": self.candidate_hidden_size,
            "shared_hidden_size": self.shared_hidden_size,
            "dropout": self.dropout,
            "best_immediate_ce_loss_weight": self.best_immediate_ce_loss_weight,
            "pairwise_score_loss_weight": self.pairwise_score_loss_weight,
            "reward_loss_weight": self.reward_loss_weight,
            "rebuffer_loss_weight": self.rebuffer_loss_weight,
            "qoe_gap_loss_weight": self.qoe_gap_loss_weight,
            "smoothness_loss_weight": self.smoothness_loss_weight,
            "risk_loss_weight": self.risk_loss_weight,
            "score_rebuffer_weight": self.score_rebuffer_weight,
            "score_risk_weight": self.score_risk_weight,
            "score_smoothness_weight": self.score_smoothness_weight,
            "score_qoe_gap_weight": self.score_qoe_gap_weight,
            "pairwise_margin_scale": self.pairwise_margin_scale,
            "risk_positive_weight": self.risk_positive_weight,
            "focus_bucket_sample_weight": self.focus_bucket_sample_weight,
            "severe_error_sample_weight": self.severe_error_sample_weight,
            "safe_vs_rebuffer_pair_weight": self.safe_vs_rebuffer_pair_weight,
            "over_aggressive_rebuffer_action_weight": self.over_aggressive_rebuffer_action_weight,
            "over_aggressive_score_loss_weight": self.over_aggressive_score_loss_weight,
            "safe_utility_rank_loss_weight": self.safe_utility_rank_loss_weight,
            "safe_utility_margin": self.safe_utility_margin,
            "max_pair_weight": self.max_pair_weight,
            "selection_focus_weight": self.selection_focus_weight,
            "selection_rebuffer_weight": self.selection_rebuffer_weight,
            "selection_over_aggressive_weight": self.selection_over_aggressive_weight,
            "selection_invalid_weight": self.selection_invalid_weight,
            "selection_prediction_loss_weight": self.selection_prediction_loss_weight,
            "seed": self.seed,
        }


SPC_V2_REWARD_RISK_TRAINING_PROFILES: dict[str, SpcV2RewardRiskTrainingProfile] = {
    "smoke": SpcV2RewardRiskTrainingProfile(
        name="smoke",
        epochs=1,
        batch_size=64,
        learning_rate=1.0e-3,
        max_training_samples=512,
        max_validation_samples=256,
        history_hidden_size=32,
        state_hidden_size=32,
        candidate_hidden_size=24,
        shared_hidden_size=64,
        dropout=0.0,
        seed=450811,
    ),
    "pilot": SpcV2RewardRiskTrainingProfile(
        name="pilot",
        epochs=12,
        batch_size=512,
        learning_rate=6.0e-4,
        max_training_samples=50000,
        max_validation_samples=12000,
        history_hidden_size=128,
        state_hidden_size=96,
        candidate_hidden_size=48,
        shared_hidden_size=192,
        dropout=0.08,
        seed=450821,
    ),
    "full_v1": SpcV2RewardRiskTrainingProfile(
        name="full_v1",
        epochs=36,
        batch_size=1024,
        learning_rate=4.0e-4,
        max_training_samples=None,
        max_validation_samples=None,
        history_hidden_size=128,
        state_hidden_size=96,
        candidate_hidden_size=48,
        shared_hidden_size=192,
        dropout=0.10,
        seed=450831,
    ),
}


@dataclass(frozen=True)
class SpcV2RewardRiskNormalizationStats:
    schema_id: str
    fitted_on_data_role: str
    source: str
    sequence_mean: tuple[float, float]
    sequence_std: tuple[float, float]
    scalar_mean: tuple[float, ...]
    scalar_std: tuple[float, ...]
    candidate_mean: tuple[float, ...]
    candidate_std: tuple[float, ...]
    sample_count: int
    candidate_row_count: int
    source_checkpoint: str | None = None

    def to_json(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "fitted_on_data_role": self.fitted_on_data_role,
            "source": self.source,
            "source_checkpoint": self.source_checkpoint,
            "sequence_features": list(SEQUENCE_FEATURES),
            "scalar_features": list(SCALAR_FEATURES),
            "candidate_features": list(CANDIDATE_FEATURES),
            "sequence_mean": list(self.sequence_mean),
            "sequence_std": list(self.sequence_std),
            "scalar_mean": list(self.scalar_mean),
            "scalar_std": list(self.scalar_std),
            "candidate_mean": list(self.candidate_mean),
            "candidate_std": list(self.candidate_std),
            "sample_count": self.sample_count,
            "candidate_row_count": self.candidate_row_count,
            "metadata_fields_used": False,
            "future_fields_used_as_inputs": False,
            "oracle_fields_used_as_inputs": False,
            "preference_targets_used_as_inputs": False,
            "validation_used": False,
        }


class SpcAbrV2RewardRiskScorer(SpbcAbrV1Policy):
    def __init__(
        self,
        *,
        sequence_dim: int = 2,
        scalar_dim: int = len(SCALAR_FEATURES),
        candidate_dim: int = len(CANDIDATE_FEATURES),
        history_hidden_size: int = 128,
        state_hidden_size: int = 96,
        candidate_hidden_size: int = 48,
        shared_hidden_size: int = 192,
        dropout: float = 0.10,
        score_rebuffer_weight: float = 4.30,
        score_risk_weight: float = 0.60,
        score_smoothness_weight: float = 0.20,
        score_qoe_gap_weight: float = 0.35,
        rebuffer_prediction_cap_s: float = REBUFFER_PREDICTION_CAP_S,
        qoe_gap_prediction_cap: float = QOE_GAP_PREDICTION_CAP,
        smoothness_prediction_cap_mbps: float = SMOOTHNESS_PREDICTION_CAP_MBPS,
    ) -> None:
        super().__init__(
            sequence_dim=sequence_dim,
            scalar_dim=scalar_dim,
            candidate_dim=candidate_dim,
            history_hidden_size=history_hidden_size,
            state_hidden_size=state_hidden_size,
            candidate_hidden_size=candidate_hidden_size,
            shared_hidden_size=shared_hidden_size,
            dropout=dropout,
        )
        self.score_rebuffer_weight = float(score_rebuffer_weight)
        self.score_risk_weight = float(score_risk_weight)
        self.score_smoothness_weight = float(score_smoothness_weight)
        self.score_qoe_gap_weight = float(score_qoe_gap_weight)
        self.rebuffer_prediction_cap_s = float(rebuffer_prediction_cap_s)
        self.qoe_gap_prediction_cap = float(qoe_gap_prediction_cap)
        self.smoothness_prediction_cap_mbps = float(smoothness_prediction_cap_mbps)
        head_input_dim = self.shared_hidden_size + self.candidate_hidden_size
        self.reward_head = self._regression_head(head_input_dim)
        self.rebuffer_head = self._regression_head(head_input_dim)
        self.qoe_gap_head = self._regression_head(head_input_dim)
        self.smoothness_head = self._regression_head(head_input_dim)
        self.risk_head = self._regression_head(head_input_dim)

    def _regression_head(self, input_dim: int) -> nn.Sequential:
        return nn.Sequential(
            nn.Linear(input_dim, self.shared_hidden_size),
            nn.ReLU(),
            nn.Dropout(self.dropout),
            nn.Linear(self.shared_hidden_size, 1),
        )

    def forward(
        self,
        sequence: torch.Tensor,
        scalars: torch.Tensor,
        candidates: torch.Tensor,
        action_mask: torch.Tensor,
    ) -> Mapping[str, torch.Tensor]:
        if sequence.ndim != 3 or sequence.shape[2] != self.sequence_dim:
            raise SpcV2RewardRiskTrainingError("sequence must have shape [batch, history, sequence_dim]")
        if scalars.ndim != 2 or scalars.shape[1] != self.scalar_dim:
            raise SpcV2RewardRiskTrainingError("scalars must have shape [batch, scalar_dim]")
        if candidates.ndim != 3 or candidates.shape[2] != self.candidate_dim:
            raise SpcV2RewardRiskTrainingError("candidates must have shape [batch, candidates, candidate_dim]")
        if action_mask.shape != candidates.shape[:2]:
            raise SpcV2RewardRiskTrainingError("action_mask shape must match candidate rows")

        _history_output, hidden = self.history_encoder(sequence)
        history_vector = hidden[-1]
        state_vector = self.state_encoder(scalars)
        shared = self.shared(torch.cat([history_vector, state_vector], dim=1))

        batch_size, candidate_count, _ = candidates.shape
        candidate_vectors = self.candidate_encoder(candidates)
        expanded_shared = shared.unsqueeze(1).expand(batch_size, candidate_count, self.shared_hidden_size)
        joint = torch.cat([expanded_shared, candidate_vectors], dim=2)

        reward = self.reward_head(joint).squeeze(2)
        rebuffer_norm = torch.sigmoid(self.rebuffer_head(joint).squeeze(2))
        qoe_gap_norm = torch.sigmoid(self.qoe_gap_head(joint).squeeze(2))
        smoothness_norm = torch.sigmoid(self.smoothness_head(joint).squeeze(2))
        risk_logits = self.risk_head(joint).squeeze(2)
        risk_probability = torch.sigmoid(risk_logits)
        rebuffer_s = rebuffer_norm * max(float(self.rebuffer_prediction_cap_s), 1.0e-6)
        qoe_gap = qoe_gap_norm * max(float(self.qoe_gap_prediction_cap), 1.0e-6)
        smoothness_mbps = smoothness_norm * max(float(self.smoothness_prediction_cap_mbps), 1.0e-6)
        action_scores = (
            reward
            - float(self.score_rebuffer_weight) * rebuffer_s
            - float(self.score_risk_weight) * risk_probability
            - float(self.score_smoothness_weight) * smoothness_mbps
            - float(self.score_qoe_gap_weight) * qoe_gap
        )
        mask = action_mask.to(dtype=torch.bool, device=action_scores.device)
        return {
            "action_scores": action_scores.masked_fill(~mask, -1.0e9),
            "action_logits": action_scores.masked_fill(~mask, -1.0e9),
            "predicted_reward_n_by_action": reward.masked_fill(~mask, 0.0),
            "predicted_rebuffer_s_by_action": rebuffer_s.masked_fill(~mask, 0.0),
            "predicted_qoe_gap_by_action": qoe_gap.masked_fill(~mask, 0.0),
            "predicted_smoothness_mbps_by_action": smoothness_mbps.masked_fill(~mask, 0.0),
            "predicted_target_risk_logits_by_action": risk_logits.masked_fill(~mask, -1.0e9),
        }

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": SPC_V2_REWARD_RISK_MODEL_CONFIG_SCHEMA_ID,
            "model_key": SPC_V2_REWARD_RISK_MODEL_KEY,
            "model_family": "Safe Predictive Control ABR v2 Reward/Risk",
            "model_type": "gru_candidate_per_action_reward_risk_scorer",
            "sequence_features": list(SEQUENCE_FEATURES),
            "scalar_features": list(SCALAR_FEATURES),
            "candidate_features": list(CANDIDATE_FEATURES),
            "target": "phase45_v2 per_action_outcomes",
            "forward_input_contract": {
                "allowed_model_input_keys": sorted(MODEL_INPUT_KEYS),
                "allowed_context_keys": sorted(SEQUENCE_FEATURES + SCALAR_FEATURES),
                "allowed_candidate_keys": sorted(CANDIDATE_FEATURES),
                "preference_pairs_used_as_inputs": False,
                "per_action_outcomes_used_as_inputs": False,
                "qoe_gap_used_as_input": False,
                "reward_n_used_as_input": False,
                "rollout_source_used_as_input": False,
                "metadata_used_as_input": False,
            },
            "sequence_dim": self.sequence_dim,
            "scalar_dim": self.scalar_dim,
            "candidate_dim": self.candidate_dim,
            "history_hidden_size": self.history_hidden_size,
            "state_hidden_size": self.state_hidden_size,
            "candidate_hidden_size": self.candidate_hidden_size,
            "shared_hidden_size": self.shared_hidden_size,
            "dropout": self.dropout,
            "prediction_heads": {
                "reward_n_by_action": True,
                "estimated_rebuffer_s_by_action": True,
                "qoe_gap_by_action": True,
                "smoothness_mbps_by_action": True,
                "target_risk_logits_by_action": True,
                "targets_used_only_for_training": True,
            },
            "decision_score": {
                "formula": "reward - rebuffer_weight*rebuffer_s - risk_weight*risk_probability - smoothness_weight*smoothness_mbps - qoe_gap_weight*qoe_gap",
                "score_rebuffer_weight": self.score_rebuffer_weight,
                "score_risk_weight": self.score_risk_weight,
                "score_smoothness_weight": self.score_smoothness_weight,
                "score_qoe_gap_weight": self.score_qoe_gap_weight,
            },
            "rebuffer_prediction_cap_s": self.rebuffer_prediction_cap_s,
            "qoe_gap_prediction_cap": self.qoe_gap_prediction_cap,
            "smoothness_prediction_cap_mbps": self.smoothness_prediction_cap_mbps,
            "controller_registered": False,
            "bundle_exported": False,
        }


def profile_by_name(name: str) -> SpcV2RewardRiskTrainingProfile:
    key = str(name).strip()
    if key not in SPC_V2_REWARD_RISK_TRAINING_PROFILES:
        raise SpcV2RewardRiskTrainingError("unknown spc_abr_v2_reward_risk profile: {0}".format(name))
    return SPC_V2_REWARD_RISK_TRAINING_PROFILES[key]


def train_spc_abr_v2_reward_risk(
    dataset_dir: object,
    output_dir: object,
    *,
    profile: SpcV2RewardRiskTrainingProfile,
    overwrite: bool = False,
    device: str = "auto",
    epochs: int | None = None,
    batch_size: int | None = None,
    learning_rate: float | None = None,
    max_training_samples: int | None | str = "profile",
    max_validation_samples: int | None | str = "profile",
    validate_dataset: bool = True,
    reference_policy_checkpoint: object | None = None,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
) -> Mapping[str, object]:
    _emit_progress(progress_callback, "preparing", "Preparando entrenamiento spc_abr_v2_reward_risk")
    data_path = ensure_existing_dir(dataset_dir, purpose="phase45_v2 preference dataset")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="spc_abr_v2_reward_risk model")
    if validate_dataset:
        _emit_progress(progress_callback, "validating_dataset", "Validando dataset phase45_v2")
        dataset_validation = validate_phase45_v2_dataset_dir(data_path)
    else:
        dataset_validation = {"status": "SKIPPED", "dataset_dir": str(data_path)}

    active_epochs = int(epochs if epochs is not None else profile.epochs)
    active_batch_size = int(batch_size if batch_size is not None else profile.batch_size)
    active_learning_rate = float(learning_rate if learning_rate is not None else profile.learning_rate)
    train_limit = _resolve_limit(max_training_samples, profile.max_training_samples)
    val_limit = _resolve_limit(max_validation_samples, profile.max_validation_samples)
    _validate_training_args(active_epochs, active_batch_size, active_learning_rate, train_limit, val_limit)

    selected_device = resolve_torch_device(device)
    set_training_seed(profile.seed)
    started = time.monotonic()
    _emit_progress(
        progress_callback,
        "loading_examples",
        "Cargando muestras v2 JSONL",
        device_used=str(selected_device),
        training_limit=train_limit,
        validation_limit=val_limit,
    )
    training_examples = _load_examples_for_scorer(data_path / V2_DATA_FILENAMES[TRAINING_ROLE], TRAINING_ROLE, train_limit, profile)
    validation_examples = _load_examples_for_scorer(
        data_path / V2_DATA_FILENAMES[VALIDATION_ROLE],
        VALIDATION_ROLE,
        val_limit,
        profile,
    )
    if not training_examples or not validation_examples:
        raise SpcV2RewardRiskTrainingError("spc_abr_v2_reward_risk training requires training and validation examples")
    _emit_progress(
        progress_callback,
        "examples_loaded",
        "Muestras v2 cargadas",
        training_samples=len(training_examples),
        validation_samples=len(validation_examples),
    )

    normalization = fit_spc_v2_reward_risk_normalization(training_examples)
    train_tensors = examples_to_tensors(training_examples, normalization)
    validation_tensors = examples_to_tensors(validation_examples, normalization)
    model = SpcAbrV2RewardRiskScorer(
        history_hidden_size=profile.history_hidden_size,
        state_hidden_size=profile.state_hidden_size,
        candidate_hidden_size=profile.candidate_hidden_size,
        shared_hidden_size=profile.shared_hidden_size,
        dropout=profile.dropout,
        score_rebuffer_weight=profile.score_rebuffer_weight,
        score_risk_weight=profile.score_risk_weight,
        score_smoothness_weight=profile.score_smoothness_weight,
        score_qoe_gap_weight=profile.score_qoe_gap_weight,
    ).to(selected_device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=active_learning_rate)
    generator = torch.Generator()
    generator.manual_seed(profile.seed)
    train_loader = DataLoader(TensorDataset(*train_tensors), batch_size=active_batch_size, shuffle=True, generator=generator)
    train_eval_loader = DataLoader(TensorDataset(*train_tensors), batch_size=active_batch_size, shuffle=False)
    validation_loader = DataLoader(TensorDataset(*validation_tensors), batch_size=active_batch_size, shuffle=False)

    epoch_reports = []
    best_validation_loss = math.inf
    best_validation_selection_score = math.inf
    best_state_dict = None
    best_epoch = 0
    for epoch in range(1, active_epochs + 1):
        epoch_started = time.monotonic()
        _emit_progress(
            progress_callback,
            "epoch_started",
            "Iniciando epoca spc_v2_reward_risk",
            epoch=epoch,
            epochs=active_epochs,
            train_batches=len(train_loader),
        )
        train_metrics = _run_epoch(
            model,
            train_loader,
            device=selected_device,
            optimizer=optimizer,
            profile=profile,
            progress_callback=progress_callback,
            epoch=epoch,
            epochs=active_epochs,
        )
        _emit_progress(
            progress_callback,
            "epoch_validation_started",
            "Validando epoca spc_v2_reward_risk",
            epoch=epoch,
            epochs=active_epochs,
            validation_batches=len(validation_loader),
        )
        validation_metrics = evaluate_spc_v2_reward_risk_model(
            model,
            validation_loader,
            device=selected_device,
            profile=profile,
            examples=validation_examples,
        )
        selection_score = _selection_score(validation_metrics, profile)
        epoch_report = {
            "epoch": epoch,
            "training_loss": train_metrics["loss"],
            "training_reward_loss": train_metrics["reward_loss"],
            "training_rebuffer_loss": train_metrics["rebuffer_loss"],
            "training_qoe_gap_loss": train_metrics["qoe_gap_loss"],
            "training_smoothness_loss": train_metrics["smoothness_loss"],
            "training_risk_loss": train_metrics["risk_loss"],
            "training_over_aggressive_score_probability_loss": train_metrics["over_aggressive_score_probability_loss"],
            "training_safe_utility_rank_loss": train_metrics["safe_utility_rank_loss"],
            "validation_loss": validation_metrics["loss"],
            "validation_reward_mae": validation_metrics["reward_mae"],
            "validation_rebuffer_mae_s": validation_metrics["rebuffer_mae_s"],
            "validation_qoe_gap_mae": validation_metrics["qoe_gap_mae"],
            "validation_risk_brier": validation_metrics["risk_brier"],
            "validation_over_aggressive_score_probability_loss": validation_metrics[
                "over_aggressive_score_probability_loss"
            ],
            "validation_safe_utility_rank_loss": validation_metrics["safe_utility_rank_loss"],
            "validation_selected_utility_regret_vs_best_immediate_mean": validation_metrics[
                "selected_utility_regret_vs_best_immediate_mean"
            ],
            "validation_selected_rebuffer_regret_vs_best_immediate_mean": validation_metrics[
                "selected_rebuffer_regret_vs_best_immediate_mean"
            ],
            "validation_selection_score": selection_score,
        }
        epoch_reports.append(epoch_report)
        best_validation_loss = min(best_validation_loss, float(validation_metrics["loss"]))
        is_best = float(selection_score) < best_validation_selection_score
        if is_best:
            best_validation_selection_score = float(selection_score)
            best_epoch = epoch
            best_state_dict = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}
        _emit_progress(
            progress_callback,
            "epoch_finished",
            "Epoca spc_v2_reward_risk completada",
            epoch=epoch,
            epochs=active_epochs,
            epoch_duration_s=time.monotonic() - epoch_started,
            training_loss=train_metrics["loss"],
            validation_loss=validation_metrics["loss"],
            validation_reward_mae=validation_metrics["reward_mae"],
            validation_rebuffer_mae_s=validation_metrics["rebuffer_mae_s"],
            validation_risk_brier=validation_metrics["risk_brier"],
            validation_utility_regret=validation_metrics["selected_utility_regret_vs_best_immediate_mean"],
            validation_rebuffer_regret=validation_metrics["selected_rebuffer_regret_vs_best_immediate_mean"],
            validation_selection_score=selection_score,
            best_epoch=best_epoch,
            best_so_far=is_best,
        )

    if best_state_dict is not None:
        model.load_state_dict(best_state_dict)
    _emit_progress(progress_callback, "final_evaluation_started", "Calculando metricas finales spc_v2_reward_risk")
    final_training_metrics = evaluate_spc_v2_reward_risk_model(
        model,
        train_eval_loader,
        device=selected_device,
        profile=profile,
        examples=training_examples,
    )
    final_validation_metrics = evaluate_spc_v2_reward_risk_model(
        model,
        validation_loader,
        device=selected_device,
        profile=profile,
        examples=validation_examples,
    )
    reference_comparison = _evaluate_reference_policy_if_available(
        reference_policy_checkpoint,
        validation_examples=validation_examples,
        batch_size=active_batch_size,
        device=selected_device,
        scorer_validation_metrics=final_validation_metrics,
        progress_callback=progress_callback,
    )

    model_config = dict(model.config())
    normalization_payload = normalization.to_json()
    checkpoint_path = output_path / SPC_V2_REWARD_RISK_MODEL_FILENAME
    config_path = output_path / SPC_V2_REWARD_RISK_MODEL_CONFIG_FILENAME
    normalization_path = output_path / SPC_V2_REWARD_RISK_NORMALIZATION_FILENAME
    report_path = output_path / SPC_V2_REWARD_RISK_TRAINING_REPORT_FILENAME
    checkpoint = {
        "schema_id": SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID,
        "model_key": SPC_V2_REWARD_RISK_MODEL_KEY,
        "model_state_dict": model.state_dict(),
        "model_config": model_config,
        "normalization": normalization_payload,
        "training_profile": profile.to_json(),
        "best_epoch": best_epoch,
        "best_validation_selection_score": best_validation_selection_score,
        "best_validation_loss_seen": best_validation_loss,
        "device_used": str(selected_device),
        "controller_registered": False,
        "bundle_exported": False,
    }
    torch.save(checkpoint, checkpoint_path)
    write_json(config_path, model_config)
    write_json(normalization_path, normalization_payload)
    duration_s = time.monotonic() - started
    report = {
        "schema_id": SPC_V2_REWARD_RISK_TRAINING_REPORT_SCHEMA_ID,
        "human_readable_name": "Entrenamiento offline de spc_abr_v2_reward_risk",
        "phase": "fase_4_5_v1_bloque7c_entrenamiento_spc_abr_v2_reward_risk",
        "status": "PASS",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "dataset_dir": str(data_path),
        "dataset_validation": dict(dataset_validation),
        "output_dir": str(output_path),
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "profile": profile.to_json(),
        "device_requested": str(device),
        "device_used": str(selected_device),
        "seed": int(profile.seed),
        "epochs": active_epochs,
        "batch_size": active_batch_size,
        "learning_rate": active_learning_rate,
        "sample_counts_used": {
            TRAINING_ROLE: len(training_examples),
            VALIDATION_ROLE: len(validation_examples),
        },
        "best_epoch": best_epoch,
        "best_validation_selection_score": best_validation_selection_score,
        "best_validation_loss_seen": best_validation_loss,
        "checkpoint_selection": {
            "criterion": "validation_selection_score",
            "lower_is_better": True,
            "uses_eval_split": False,
            "focus_throughput_bucket": FOCUS_THROUGHPUT_BUCKET,
        },
        "epoch_reports": epoch_reports,
        "training_metrics": final_training_metrics,
        "validation_metrics": final_validation_metrics,
        "reference_policy_comparison": reference_comparison,
        "training_duration_s": duration_s,
        "model_config": model_config,
        "loss_design": {
            "primary_targets": [
                "reward_n_by_action",
                "estimated_rebuffer_s_by_action",
                "qoe_gap_by_action",
                "smoothness_mbps_by_action",
                "target_risk_by_action",
            ],
            "best_immediate_ce_anchor": "best_immediate_action",
            "pairwise_score_loss": "preference_pairs enforce scorer(preferred) > scorer(rejected)",
            "sample_weights_include_focus_bucket_and_severe_errors": True,
            "pair_weights_normalized_and_capped": True,
            "risk_positive_weight": profile.risk_positive_weight,
            "over_aggressive_score_probability_loss": "expected_softmax_score_mass_on_actions_marked_over_aggressive_rebuffer",
            "over_aggressive_score_loss_weight": profile.over_aggressive_score_loss_weight,
            "safe_utility_rank_loss": "margin_ranking_best_reward_action_inside_valid_non_over_aggressive_action_set",
            "safe_utility_rank_loss_weight": profile.safe_utility_rank_loss_weight,
            "safe_utility_margin": profile.safe_utility_margin,
            "focus_throughput_bucket": FOCUS_THROUGHPUT_BUCKET,
            "checkpoint_selected_by": "validation_selection_score_aligned_with_regret_rebuffer_focus_bucket_prediction_error",
        },
        "artifacts": {
            "checkpoint": str(checkpoint_path),
            "checkpoint_sha256": _sha256_file(checkpoint_path),
            "model_config": str(config_path),
            "normalization": str(normalization_path),
            "training_report": str(report_path),
        },
        "normalization_fitted_on": TRAINING_ROLE,
        "normalization_source": normalization_payload["source"],
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
        "preference_fields_are_model_features": False,
        "per_action_outcomes_are_model_features": False,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": True,
        "formal_ia_training_performed": True,
        "candidate_model_created": True,
        "checkpoint_written": True,
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
        "Entrenamiento spc_abr_v2_reward_risk finalizado",
        training_duration_s=duration_s,
        output_dir=str(output_path),
        best_epoch=best_epoch,
    )
    return report


def fit_spc_v2_reward_risk_normalization(
    examples: Sequence[SpbcV2DpoExample],
) -> SpcV2RewardRiskNormalizationStats:
    if not examples:
        raise SpcV2RewardRiskTrainingError("normalization requires training examples")
    sequence_rows = [step for example in examples for step in example.sequence]
    scalar_rows = [example.scalars for example in examples]
    candidate_rows = [candidate for example in examples for candidate in example.candidates]
    return SpcV2RewardRiskNormalizationStats(
        schema_id="phase45_v2_spc_reward_risk_normalization_v1",
        fitted_on_data_role=TRAINING_ROLE,
        source="phase45_v2_training_samples",
        sequence_mean=_column_means(sequence_rows),
        sequence_std=_column_stds(sequence_rows),
        scalar_mean=_column_means(scalar_rows),
        scalar_std=_column_stds(scalar_rows),
        candidate_mean=_column_means(candidate_rows),
        candidate_std=_column_stds(candidate_rows),
        sample_count=len(examples),
        candidate_row_count=len(candidate_rows),
    )


def evaluate_spc_v2_reward_risk_model(
    model: SpcAbrV2RewardRiskScorer,
    loader: DataLoader,
    *,
    device: torch.device,
    profile: SpcV2RewardRiskTrainingProfile,
    examples: Sequence[SpbcV2DpoExample],
) -> Mapping[str, object]:
    model.eval()
    totals = _ScorerMetricTotals()
    by_bucket: dict[str, _ScorerMetricTotals] = defaultdict(_ScorerMetricTotals)
    by_rollout: dict[str, _ScorerMetricTotals] = defaultdict(_ScorerMetricTotals)
    by_synthetic: dict[str, _ScorerMetricTotals] = defaultdict(_ScorerMetricTotals)
    start_index = 0
    with torch.no_grad():
        for batch in loader:
            moved = _move_batch(batch, device)
            outputs = model(moved[0], moved[1], moved[2], moved[3])
            losses = _loss_components(outputs, moved, profile)
            observations = _policy_observations(outputs, moved)
            prediction_metrics = _prediction_metrics(outputs, moved)
            batch_size = int(moved[0].shape[0])
            totals.add(observations, prediction_metrics, losses, batch_size)
            for row_offset, observation in enumerate(observations):
                example = examples[start_index + row_offset]
                single_outputs = {name: value[row_offset : row_offset + 1] for name, value in outputs.items()}
                single_batch = tuple(value[row_offset : row_offset + 1] for value in moved)
                single_prediction = _prediction_metrics(single_outputs, single_batch)
                by_bucket[example.throughput_bucket].add((observation,), single_prediction, {}, 1)
                by_rollout[example.rollout_source].add((observation,), single_prediction, {}, 1)
                by_synthetic["synthetic" if example.synthetic else "real"].add((observation,), single_prediction, {}, 1)
            start_index += batch_size
    model.train()
    by_bucket_payload = {
        bucket: metrics.to_json(include_losses=False)
        for bucket, metrics in sorted(by_bucket.items())
    }
    focus_metrics = by_bucket_payload.get(FOCUS_THROUGHPUT_BUCKET)
    if focus_metrics is None:
        focus_metrics = {"sample_count": 0, "bucket_present": False}
    else:
        focus_metrics = {**focus_metrics, "bucket_present": True}
    return {
        **totals.to_json(),
        "by_throughput_bucket": by_bucket_payload,
        "focus_2_5_mbps": focus_metrics,
        "by_rollout_source": {
            rollout: metrics.to_json(include_losses=False)
            for rollout, metrics in sorted(by_rollout.items())
        },
        "by_synthetic_source": {
            source: metrics.to_json(include_losses=False)
            for source, metrics in sorted(by_synthetic.items())
        },
    }


def resolve_torch_device(requested: str) -> torch.device:
    key = str(requested).strip().lower()
    if key == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if key == "cuda" and not torch.cuda.is_available():
        raise SpcV2RewardRiskTrainingError("CUDA/ROCm device requested but torch.cuda.is_available() is false")
    if key not in {"cpu", "cuda"}:
        raise SpcV2RewardRiskTrainingError("device must be cpu, cuda or auto")
    return torch.device(key)


def set_training_seed(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed))


def _load_examples_for_scorer(
    path: Path,
    data_role: str,
    limit: int | None,
    profile: SpcV2RewardRiskTrainingProfile,
) -> tuple[SpbcV2DpoExample, ...]:
    try:
        return load_spbc_v2_dpo_examples(
            path,
            data_role,
            limit=limit,
            max_pair_weight=profile.max_pair_weight,
            focus_bucket_sample_weight=profile.focus_bucket_sample_weight,
            severe_error_sample_weight=profile.severe_error_sample_weight,
            safe_vs_rebuffer_pair_weight=profile.safe_vs_rebuffer_pair_weight,
            over_aggressive_rebuffer_action_weight=profile.over_aggressive_rebuffer_action_weight,
            rebuffer_loss_cap_s=REBUFFER_PREDICTION_CAP_S,
        )
    except SpbcV2DpoTrainingError as exc:
        raise SpcV2RewardRiskTrainingError(str(exc)) from exc


def _run_epoch(
    model: SpcAbrV2RewardRiskScorer,
    loader: DataLoader,
    *,
    device: torch.device,
    optimizer: torch.optim.Optimizer,
    profile: SpcV2RewardRiskTrainingProfile,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
    epoch: int | None = None,
    epochs: int | None = None,
) -> Mapping[str, float]:
    model.train()
    totals = _LossTotals()
    total_batches = len(loader)
    progress_every = _progress_batch_interval(total_batches)
    epoch_started = time.monotonic()
    for batch_index, batch in enumerate(loader, start=1):
        moved = _move_batch(batch, device)
        optimizer.zero_grad()
        outputs = model(moved[0], moved[1], moved[2], moved[3])
        losses = _loss_components(outputs, moved, profile)
        losses["loss_tensor"].backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
        optimizer.step()
        batch_size = int(moved[0].shape[0])
        totals.add(losses, batch_size)
        if batch_index == 1 or batch_index == total_batches or batch_index % progress_every == 0:
            elapsed_s = time.monotonic() - epoch_started
            estimated_total_s = elapsed_s * float(total_batches) / float(batch_index)
            _emit_progress(
                progress_callback,
                "training_batch",
                "Entrenando batches spc_v2_reward_risk",
                epoch=epoch,
                epochs=epochs,
                batch=batch_index,
                batches=total_batches,
                elapsed_s=elapsed_s,
                eta_s=max(estimated_total_s - elapsed_s, 0.0),
                loss=float(losses["loss"].detach().cpu().item()),
            )
    return totals.to_json()


def _loss_components(
    outputs: Mapping[str, torch.Tensor],
    batch: Sequence[torch.Tensor],
    profile: SpcV2RewardRiskTrainingProfile,
) -> dict[str, torch.Tensor]:
    scores = outputs["action_scores"]
    mask = batch[3].to(dtype=torch.bool)
    best_labels = batch[5]
    qoe_gaps = batch[6]
    rebuffer_s = batch[7]
    rewards = batch[8]
    smoothness = batch[10]
    target_risks = batch[11]
    sample_weights = batch[12]
    pair_preferred = batch[13]
    pair_rejected = batch[14]
    pair_weights = batch[15]
    pair_reward_gaps = batch[16]
    pair_mask = batch[17].to(dtype=torch.bool)
    over_aggressive_actions = batch[19] if len(batch) > 19 else torch.zeros_like(rebuffer_s, dtype=torch.bool)
    best_immediate_ce_loss = _masked_weighted_cross_entropy(scores, best_labels, mask, sample_weights)
    pairwise_score_loss = _pairwise_score_loss(
        scores,
        pair_preferred,
        pair_rejected,
        pair_weights,
        pair_reward_gaps,
        pair_mask,
        margin_scale=profile.pairwise_margin_scale,
    )
    reward_loss = _masked_weighted_smooth_l1(outputs["predicted_reward_n_by_action"], rewards, mask, sample_weights)
    rebuffer_loss = _masked_weighted_smooth_l1(
        outputs["predicted_rebuffer_s_by_action"] / REBUFFER_PREDICTION_CAP_S,
        torch.clamp(rebuffer_s, min=0.0, max=REBUFFER_PREDICTION_CAP_S) / REBUFFER_PREDICTION_CAP_S,
        mask,
        sample_weights,
    )
    qoe_gap_loss = _masked_weighted_smooth_l1(
        outputs["predicted_qoe_gap_by_action"] / QOE_GAP_PREDICTION_CAP,
        torch.clamp(qoe_gaps, min=0.0, max=QOE_GAP_PREDICTION_CAP) / QOE_GAP_PREDICTION_CAP,
        mask,
        sample_weights,
    )
    smoothness_loss = _masked_weighted_smooth_l1(
        outputs["predicted_smoothness_mbps_by_action"] / SMOOTHNESS_PREDICTION_CAP_MBPS,
        torch.clamp(smoothness, min=0.0, max=SMOOTHNESS_PREDICTION_CAP_MBPS) / SMOOTHNESS_PREDICTION_CAP_MBPS,
        mask,
        sample_weights,
    )
    risk_loss = _masked_weighted_binary_cross_entropy(
        outputs["predicted_target_risk_logits_by_action"],
        target_risks,
        mask,
        sample_weights,
        positive_weight=profile.risk_positive_weight,
    )
    over_aggressive_score_probability_loss = _expected_over_aggressive_score_probability_loss(
        scores,
        over_aggressive_actions,
        mask,
        sample_weights,
    )
    safe_utility_rank_loss = _safe_utility_rank_loss(
        scores,
        rewards,
        over_aggressive_actions,
        mask,
        sample_weights,
        margin=float(profile.safe_utility_margin),
    )
    loss = (
        float(profile.best_immediate_ce_loss_weight) * best_immediate_ce_loss
        + float(profile.pairwise_score_loss_weight) * pairwise_score_loss
        + float(profile.reward_loss_weight) * reward_loss
        + float(profile.rebuffer_loss_weight) * rebuffer_loss
        + float(profile.qoe_gap_loss_weight) * qoe_gap_loss
        + float(profile.smoothness_loss_weight) * smoothness_loss
        + float(profile.risk_loss_weight) * risk_loss
        + float(profile.over_aggressive_score_loss_weight) * over_aggressive_score_probability_loss
        + float(profile.safe_utility_rank_loss_weight) * safe_utility_rank_loss
    )
    return {
        "loss_tensor": loss,
        "loss": loss.detach(),
        "best_immediate_ce_loss": best_immediate_ce_loss.detach(),
        "pairwise_score_loss": pairwise_score_loss.detach(),
        "reward_loss": reward_loss.detach(),
        "rebuffer_loss": rebuffer_loss.detach(),
        "qoe_gap_loss": qoe_gap_loss.detach(),
        "smoothness_loss": smoothness_loss.detach(),
        "risk_loss": risk_loss.detach(),
        "over_aggressive_score_probability_loss": over_aggressive_score_probability_loss.detach(),
        "safe_utility_rank_loss": safe_utility_rank_loss.detach(),
    }


def _masked_weighted_cross_entropy(
    logits: torch.Tensor,
    labels: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    log_probs = F.log_softmax(logits.masked_fill(~active_mask, -1.0e9), dim=1)
    losses = -torch.gather(log_probs, 1, labels.view(-1, 1)).squeeze(1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (losses * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _pairwise_score_loss(
    scores: torch.Tensor,
    preferred: torch.Tensor,
    rejected: torch.Tensor,
    pair_weights: torch.Tensor,
    reward_gaps: torch.Tensor,
    pair_mask: torch.Tensor,
    *,
    margin_scale: float,
) -> torch.Tensor:
    pref_scores = torch.gather(scores, 1, preferred)
    rej_scores = torch.gather(scores, 1, rejected)
    margin = torch.clamp(reward_gaps.to(device=scores.device, dtype=scores.dtype), min=0.0, max=10.0) * float(margin_scale)
    raw = F.relu(margin - (pref_scores - rej_scores))
    weights = pair_weights.to(device=scores.device, dtype=scores.dtype)
    mask = pair_mask.to(device=scores.device, dtype=scores.dtype)
    return (raw * weights * mask).sum() / torch.clamp((weights * mask).sum(), min=1.0)


def _masked_weighted_smooth_l1(
    predictions: torch.Tensor,
    targets: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=predictions.device)
    targets = targets.to(device=predictions.device, dtype=predictions.dtype)
    raw = F.smooth_l1_loss(predictions, targets, reduction="none")
    valid_counts = torch.clamp(active_mask.sum(dim=1).to(dtype=predictions.dtype), min=1.0)
    per_sample_loss = (raw * active_mask.to(dtype=predictions.dtype)).sum(dim=1) / valid_counts
    weights = sample_weights.to(device=predictions.device, dtype=predictions.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _masked_weighted_binary_cross_entropy(
    logits: torch.Tensor,
    targets: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
    *,
    positive_weight: float,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    targets = targets.to(device=logits.device, dtype=logits.dtype)
    raw = F.binary_cross_entropy_with_logits(logits, targets, reduction="none")
    action_weights = torch.where(targets >= 0.5, torch.full_like(targets, float(positive_weight)), torch.ones_like(targets))
    valid_counts = torch.clamp(active_mask.sum(dim=1).to(dtype=logits.dtype), min=1.0)
    per_sample_loss = (raw * action_weights * active_mask.to(dtype=logits.dtype)).sum(dim=1) / valid_counts
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _expected_over_aggressive_score_probability_loss(
    scores: torch.Tensor,
    over_aggressive_actions: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=scores.device)
    over_mask = over_aggressive_actions.to(dtype=torch.bool, device=scores.device) & active_mask
    probabilities = F.softmax(scores.masked_fill(~active_mask, -1.0e9), dim=1)
    per_sample_loss = (probabilities * over_mask.to(dtype=scores.dtype)).sum(dim=1)
    weights = sample_weights.to(device=scores.device, dtype=scores.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _safe_utility_rank_loss(
    scores: torch.Tensor,
    rewards: torch.Tensor,
    over_aggressive_actions: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
    *,
    margin: float,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=scores.device)
    over_mask = over_aggressive_actions.to(dtype=torch.bool, device=scores.device) & active_mask
    safe_mask = active_mask & ~over_mask
    has_safe = safe_mask.any(dim=1, keepdim=True)
    effective_safe_mask = torch.where(has_safe, safe_mask, active_mask)
    rewards = rewards.to(device=scores.device, dtype=scores.dtype)
    safe_rewards = rewards.masked_fill(~effective_safe_mask, -1.0e9)
    best_safe = safe_rewards.argmax(dim=1)
    masked_scores = scores.masked_fill(~active_mask, -1.0e9)
    best_safe_scores = torch.gather(masked_scores, 1, best_safe.unsqueeze(1)).squeeze(1)
    action_indices = torch.arange(scores.shape[1], device=scores.device).unsqueeze(0)
    competing_safe_mask = effective_safe_mask & (action_indices != best_safe.unsqueeze(1))
    has_competing_safe = competing_safe_mask.any(dim=1)
    competing_scores = masked_scores.masked_fill(~competing_safe_mask, -1.0e9)
    best_competing_scores = competing_scores.max(dim=1).values
    per_sample_loss = F.relu(float(margin) + best_competing_scores - best_safe_scores)
    per_sample_loss = torch.where(has_competing_safe, per_sample_loss, torch.zeros_like(per_sample_loss))
    weights = sample_weights.to(device=scores.device, dtype=scores.dtype) * has_competing_safe.to(dtype=scores.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _prediction_metrics(outputs: Mapping[str, torch.Tensor], batch: Sequence[torch.Tensor]) -> Mapping[str, float]:
    mask = batch[3].to(dtype=torch.bool)
    reward_pred = outputs["predicted_reward_n_by_action"]
    rebuffer_pred = outputs["predicted_rebuffer_s_by_action"]
    qoe_gap_pred = outputs["predicted_qoe_gap_by_action"]
    smoothness_pred = outputs["predicted_smoothness_mbps_by_action"]
    risk_probs = torch.sigmoid(outputs["predicted_target_risk_logits_by_action"])
    reward_target = batch[8].to(device=reward_pred.device, dtype=reward_pred.dtype)
    rebuffer_target = batch[7].to(device=reward_pred.device, dtype=reward_pred.dtype)
    qoe_gap_target = batch[6].to(device=reward_pred.device, dtype=reward_pred.dtype)
    smoothness_target = batch[10].to(device=reward_pred.device, dtype=reward_pred.dtype)
    risk_target = batch[11].to(device=reward_pred.device, dtype=reward_pred.dtype)
    active = mask.to(device=reward_pred.device)
    valid_count = torch.clamp(active.sum().to(dtype=reward_pred.dtype), min=1.0)
    risk_pred = risk_probs >= 0.5
    risk_true = risk_target >= 0.5
    positives = (risk_true & active).sum().detach().cpu().item()
    false_negatives = ((~risk_pred) & risk_true & active).sum().detach().cpu().item()
    valid_count_value = float(valid_count.detach().cpu().item())
    return {
        "reward_mae": float((torch.abs(reward_pred - reward_target) * active).sum().detach().cpu().item() / valid_count_value),
        "rebuffer_mae_s": float((torch.abs(rebuffer_pred - rebuffer_target) * active).sum().detach().cpu().item() / valid_count_value),
        "qoe_gap_mae": float((torch.abs(qoe_gap_pred - qoe_gap_target) * active).sum().detach().cpu().item() / valid_count_value),
        "smoothness_mae_mbps": float(
            (torch.abs(smoothness_pred - smoothness_target) * active).sum().detach().cpu().item() / valid_count_value
        ),
        "risk_brier": float((((risk_probs - risk_target) ** 2) * active).sum().detach().cpu().item() / valid_count_value),
        "risk_accuracy": float(((risk_pred == risk_true) & active).sum().detach().cpu().item() / valid_count_value),
        "risk_false_negative_rate": float(false_negatives / positives) if positives else 0.0,
    }


@dataclass
class _LossTotals:
    weight: int = 0
    losses: dict[str, float] | None = None

    def __post_init__(self) -> None:
        self.losses = defaultdict(float)

    def add(self, losses: Mapping[str, object], batch_size: int) -> None:
        self.weight += int(batch_size)
        for name in _LOSS_METRIC_NAMES:
            value = losses[name]
            numeric = float(value.detach().cpu().item()) if hasattr(value, "detach") else float(value)
            self.losses[name] += numeric * float(batch_size)

    def to_json(self) -> dict[str, float]:
        denominator = max(float(self.weight), 1.0)
        payload = {name: round(value / denominator, 9) for name, value in sorted(self.losses.items())}
        payload["sample_count"] = int(self.weight)
        return payload


@dataclass
class _PredictionMetricTotals:
    weight: int = 0
    metrics: dict[str, float] | None = None

    def __post_init__(self) -> None:
        self.metrics = defaultdict(float)

    def add(self, metrics: Mapping[str, float], batch_size: int) -> None:
        self.weight += int(batch_size)
        for name, value in metrics.items():
            self.metrics[name] += float(value) * float(batch_size)

    def to_json(self) -> dict[str, float]:
        denominator = max(float(self.weight), 1.0)
        return {name: round(value / denominator, 6) for name, value in sorted(self.metrics.items())}


@dataclass
class _ScorerMetricTotals:
    policy: _PolicyMetricTotals | None = None
    predictions: _PredictionMetricTotals | None = None
    losses: _LossTotals | None = None

    def __post_init__(self) -> None:
        self.policy = _PolicyMetricTotals()
        self.predictions = _PredictionMetricTotals()
        self.losses = _LossTotals()

    def add(
        self,
        observations: Sequence[Mapping[str, object]],
        prediction_metrics: Mapping[str, float],
        losses: Mapping[str, object],
        batch_size: int,
    ) -> None:
        self.policy.add_observations(observations, {}, batch_size)
        self.predictions.add(prediction_metrics, batch_size)
        if losses:
            self.losses.add(losses, batch_size)

    def to_json(self, *, include_losses: bool = True) -> dict[str, object]:
        payload = self.policy.to_json(include_losses=False)
        payload.update(self.predictions.to_json())
        if include_losses:
            payload.update(self.losses.to_json())
        return payload


def _selection_score(metrics: Mapping[str, object], profile: SpcV2RewardRiskTrainingProfile) -> float:
    score = (
        float(metrics.get("selected_utility_regret_vs_best_immediate_mean", 0.0))
        + float(profile.selection_rebuffer_weight)
        * float(metrics.get("selected_rebuffer_regret_vs_best_immediate_mean", 0.0))
        + float(profile.selection_over_aggressive_weight) * float(metrics.get("over_aggressive_rate_vs_oracle", 0.0))
        + float(profile.selection_invalid_weight) * float(metrics.get("invalid_action_rate", 0.0))
        + float(profile.selection_prediction_loss_weight)
        * (
            float(metrics.get("reward_mae", 0.0))
            + float(metrics.get("rebuffer_mae_s", 0.0))
            + float(metrics.get("qoe_gap_mae", 0.0))
            + float(metrics.get("risk_brier", 0.0))
        )
    )
    focus = metrics.get("focus_2_5_mbps")
    if isinstance(focus, Mapping) and focus.get("bucket_present"):
        score += float(profile.selection_focus_weight) * (
            float(focus.get("selected_utility_regret_vs_best_immediate_mean", 0.0))
            + float(profile.selection_rebuffer_weight)
            * float(focus.get("selected_rebuffer_regret_vs_best_immediate_mean", 0.0))
            + float(profile.selection_over_aggressive_weight) * float(focus.get("over_aggressive_rate_vs_oracle", 0.0))
            + float(profile.selection_invalid_weight) * float(focus.get("invalid_action_rate", 0.0))
        )
    return float(score)


def _evaluate_reference_policy_if_available(
    checkpoint_path: object | None,
    *,
    validation_examples: Sequence[SpbcV2DpoExample],
    batch_size: int,
    device: torch.device,
    scorer_validation_metrics: Mapping[str, object],
    progress_callback: Callable[[Mapping[str, object]], None] | None,
) -> Mapping[str, object]:
    if checkpoint_path is None:
        return {"available": False, "reason": "no_reference_policy_checkpoint_requested"}
    path = Path(checkpoint_path).expanduser()
    if not path.is_file():
        return {"available": False, "reason": "reference_policy_checkpoint_missing", "path": str(path)}
    try:
        _emit_progress(progress_callback, "reference_evaluation_started", "Comparando scorer contra politica offline de referencia")
        payload = _load_torch_mapping(path)
        model, normalization = _reference_model_and_normalization(payload, path)
        model = model.to(device)
        tensors = examples_to_tensors(validation_examples, normalization)
        loader = DataLoader(TensorDataset(*tensors), batch_size=batch_size, shuffle=False)
        metrics = _evaluate_policy_like_model(model, loader, device=device, examples=validation_examples)
        return {
            "available": True,
            "path": str(path),
            "checkpoint_sha256": _sha256_file(path),
            "model_key": str(payload.get("model_key")),
            "validation_metrics": metrics,
            "validation_delta_vs_scorer": _metric_delta(scorer_validation_metrics, metrics),
        }
    except Exception as exc:  # noqa: BLE001 - comparison is optional and audited in the report.
        return {
            "available": False,
            "reason": "reference_policy_comparison_failed",
            "path": str(path),
            "error_type": type(exc).__name__,
            "message": str(exc),
        }


def _reference_model_and_normalization(
    payload: Mapping[str, object],
    path: Path,
) -> tuple[nn.Module, SpcV2RewardRiskNormalizationStats]:
    model_key = str(payload.get("model_key"))
    schema_id = payload.get("schema_id")
    config = _require_mapping(payload.get("model_config"), "reference model_config")
    state_dict = payload.get("model_state_dict")
    if not isinstance(state_dict, Mapping):
        raise SpcV2RewardRiskTrainingError("reference checkpoint missing model_state_dict")
    if schema_id == SPBC_CHECKPOINT_SCHEMA_ID and model_key == "spbc_abr_v1":
        model: nn.Module = SpbcAbrV1Policy(
            history_hidden_size=int(config["history_hidden_size"]),
            state_hidden_size=int(config["state_hidden_size"]),
            candidate_hidden_size=int(config["candidate_hidden_size"]),
            shared_hidden_size=int(config["shared_hidden_size"]),
            dropout=float(config["dropout"]),
        )
    elif schema_id == SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID and model_key == SPBC_V2_DPO_MODEL_KEY:
        model = SpbcAbrV2DpoPolicy(
            history_hidden_size=int(config["history_hidden_size"]),
            state_hidden_size=int(config["state_hidden_size"]),
            candidate_hidden_size=int(config["candidate_hidden_size"]),
            shared_hidden_size=int(config["shared_hidden_size"]),
            dropout=float(config["dropout"]),
            decision_reward_fusion_weight=float(config.get("decision_reward_fusion_weight", 0.12)),
            decision_rebuffer_fusion_weight=float(config.get("decision_rebuffer_fusion_weight", 0.30)),
            decision_risk_fusion_weight=float(config.get("decision_risk_fusion_weight", 0.18)),
            rebuffer_prediction_cap_s=float(config.get("rebuffer_prediction_cap_s", REBUFFER_PREDICTION_CAP_S)),
        )
    else:
        raise SpcV2RewardRiskTrainingError("unsupported reference policy checkpoint: {0}".format(path))
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    normalization = _normalization_from_payload(payload, path)
    return model, normalization


def _evaluate_policy_like_model(
    model: nn.Module,
    loader: DataLoader,
    *,
    device: torch.device,
    examples: Sequence[SpbcV2DpoExample],
) -> Mapping[str, object]:
    model.eval()
    totals = _PolicyMetricTotals()
    by_bucket: dict[str, _PolicyMetricTotals] = defaultdict(_PolicyMetricTotals)
    start_index = 0
    with torch.no_grad():
        for batch in loader:
            moved = _move_batch(batch, device)
            outputs = model(moved[0], moved[1], moved[2], moved[3])
            observations = _policy_observations(outputs, moved)
            batch_size = int(moved[0].shape[0])
            totals.add_observations(observations, {}, batch_size)
            for row_offset, observation in enumerate(observations):
                example = examples[start_index + row_offset]
                by_bucket[example.throughput_bucket].add_observations((observation,), {}, 1)
            start_index += batch_size
    by_bucket_payload = {bucket: metrics.to_json(include_losses=False) for bucket, metrics in sorted(by_bucket.items())}
    focus_metrics = by_bucket_payload.get(FOCUS_THROUGHPUT_BUCKET)
    if focus_metrics is None:
        focus_metrics = {"sample_count": 0, "bucket_present": False}
    else:
        focus_metrics = {**focus_metrics, "bucket_present": True}
    return {
        **totals.to_json(include_losses=False),
        "by_throughput_bucket": by_bucket_payload,
        "focus_2_5_mbps": focus_metrics,
    }


def _metric_delta(
    scorer_metrics: Mapping[str, object],
    reference_metrics: Mapping[str, object],
) -> Mapping[str, float]:
    keys = (
        "top1_accuracy",
        "top2_accuracy",
        "best_immediate_accuracy",
        "predicted_reward_n_mean",
        "predicted_rebuffer_s_mean",
        "selected_utility_regret_vs_best_immediate_mean",
        "selected_rebuffer_regret_vs_best_immediate_mean",
        "over_aggressive_rate_vs_oracle",
        "under_aggressive_rate_vs_oracle",
        "predicted_target_risk_rate",
    )
    return {
        key: round(float(scorer_metrics.get(key, 0.0)) - float(reference_metrics.get(key, 0.0)), 9)
        for key in keys
    }


def _normalization_from_payload(payload: Mapping[str, object], checkpoint_path: Path) -> SpcV2RewardRiskNormalizationStats:
    normalization = _require_mapping(payload.get("normalization"), "reference normalization")
    return SpcV2RewardRiskNormalizationStats(
        schema_id="phase45_v2_spc_reward_risk_normalization_v1",
        fitted_on_data_role=TRAINING_ROLE,
        source="reference_policy_checkpoint_train_only",
        source_checkpoint=str(checkpoint_path),
        sequence_mean=_tuple_of_floats(normalization.get("sequence_mean"), len(SEQUENCE_FEATURES), "sequence_mean"),
        sequence_std=_tuple_of_floats(normalization.get("sequence_std"), len(SEQUENCE_FEATURES), "sequence_std"),
        scalar_mean=_tuple_of_floats(normalization.get("scalar_mean"), len(SCALAR_FEATURES), "scalar_mean"),
        scalar_std=_tuple_of_floats(normalization.get("scalar_std"), len(SCALAR_FEATURES), "scalar_std"),
        candidate_mean=_tuple_of_floats(normalization.get("candidate_mean"), len(CANDIDATE_FEATURES), "candidate_mean"),
        candidate_std=_tuple_of_floats(normalization.get("candidate_std"), len(CANDIDATE_FEATURES), "candidate_std"),
        sample_count=int(normalization.get("sample_count", 0) or 0),
        candidate_row_count=int(normalization.get("candidate_row_count", 0) or 0),
    )


def _move_batch(batch: Sequence[torch.Tensor], device: torch.device) -> tuple[torch.Tensor, ...]:
    return tuple(tensor.to(device) for tensor in batch)


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


def _progress_batch_interval(total_batches: int) -> int:
    return max(1, total_batches // 20)


def _resolve_limit(value: int | None | str, profile_value: int | None) -> int | None:
    if value == "profile":
        return profile_value
    if value is None:
        return None
    return int(value)


def _validate_training_args(
    epochs: int,
    batch_size: int,
    learning_rate: float,
    max_training_samples: int | None,
    max_validation_samples: int | None,
) -> None:
    if epochs <= 0 or batch_size <= 0:
        raise SpcV2RewardRiskTrainingError("epochs and batch_size must be positive")
    if not math.isfinite(float(learning_rate)) or float(learning_rate) <= 0.0:
        raise SpcV2RewardRiskTrainingError("learning_rate must be finite and positive")
    for name, value in (("max_training_samples", max_training_samples), ("max_validation_samples", max_validation_samples)):
        if value is not None and int(value) <= 0:
            raise SpcV2RewardRiskTrainingError("{0} must be positive when provided".format(name))


def _column_means(rows: Sequence[Sequence[float]]) -> tuple[float, ...]:
    width = _matrix_width(rows)
    return tuple(sum(row[index] for row in rows) / float(len(rows)) for index in range(width))


def _column_stds(rows: Sequence[Sequence[float]]) -> tuple[float, ...]:
    means = _column_means(rows)
    variances = []
    for index, mean in enumerate(means):
        variance = sum((row[index] - mean) ** 2 for row in rows) / float(len(rows))
        std = math.sqrt(max(variance, 0.0))
        variances.append(std if std > 1.0e-12 else 1.0)
    return tuple(variances)


def _matrix_width(rows: Sequence[Sequence[float]]) -> int:
    if not rows:
        raise SpcV2RewardRiskTrainingError("normalization rows must not be empty")
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise SpcV2RewardRiskTrainingError("normalization row width changed")
    return width


def _tuple_of_floats(value: object, expected_len: int, name: str) -> tuple[float, ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise SpcV2RewardRiskTrainingError("{0} must be a sequence".format(name))
    parsed = tuple(float(item) for item in value)
    if len(parsed) != int(expected_len) or not all(math.isfinite(item) for item in parsed):
        raise SpcV2RewardRiskTrainingError("{0} has invalid width or non-finite values".format(name))
    return parsed


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SpcV2RewardRiskTrainingError("{0} must be an object".format(name))
    return value


def _load_torch_mapping(path: Path) -> Mapping[str, object]:
    try:
        payload = torch.load(path, map_location="cpu", weights_only=False)
    except TypeError:
        payload = torch.load(path, map_location="cpu")
    if not isinstance(payload, Mapping):
        raise SpcV2RewardRiskTrainingError("checkpoint must contain a mapping: {0}".format(path))
    return payload


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
