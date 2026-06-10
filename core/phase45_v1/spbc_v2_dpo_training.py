from __future__ import annotations

import hashlib
import json
import math
import random
import time
from collections import Counter, defaultdict
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
from core.phase45_v1.preference_dataset_v2 import (
    V2_DATA_FILENAMES,
    validate_phase45_v2_dataset_dir,
)
from core.phase45_v1.spbc_training import (
    CANDIDATE_FEATURES,
    SCALAR_FEATURES,
    SEQUENCE_FEATURES,
    SpbcAbrV1Policy,
    SpbcTrainingError,
)


SPBC_V2_DPO_MODEL_KEY = "spbc_abr_v2_dpo"
SPBC_V2_DPO_MODEL_CONFIG_SCHEMA_ID = "phase45_v2_spbc_dpo_model_config_v1"
SPBC_V2_DPO_TRAINING_REPORT_SCHEMA_ID = "phase45_v2_spbc_dpo_training_report_v1"
SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID = "phase45_v2_spbc_dpo_checkpoint_v1"

SPBC_V2_DPO_MODEL_FILENAME = "modelo_spbc_abr_v2_dpo.pt"
SPBC_V2_DPO_MODEL_CONFIG_FILENAME = "configuracion_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_NORMALIZATION_FILENAME = "normalizacion_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_spbc_abr_v2_dpo.json"

PAIR_SOURCE_WEIGHTS = {
    "oracle_vs_spbc_policy": 1.30,
    "oracle_vs_rollout_policy": 1.35,
    "best_reward_vs_worst_valid": 1.00,
    "safe_vs_rebuffer": 1.45,
    "best_reward_vs_over_aggressive": 1.55,
    "smoothness_tiebreak_when_reward_close": 1.15,
    "fallback_valid_distinction": 0.60,
}
MODEL_INPUT_KEYS = frozenset(("context", "candidates", "action_mask"))
CONTEXT_INPUT_KEYS = frozenset(SEQUENCE_FEATURES + SCALAR_FEATURES)
CANDIDATE_INPUT_KEYS = frozenset(CANDIDATE_FEATURES)
TARGET_RISK_QOE_GAP_THRESHOLD = 0.25
FOCUS_THROUGHPUT_BUCKET = "2_5_mbps"
SAFETY_ROLLOUT_SOURCE = "spbc_v2_dpo_on_policy"
REBUFFER_LOSS_SECONDS_CAP = 4.0
_LOSS_METRIC_NAMES = (
    "loss",
    "ce_loss",
    "dpo_loss",
    "ranking_loss",
    "utility_loss",
    "rebuffer_loss",
    "aux_reward_loss",
    "aux_rebuffer_loss",
    "aux_risk_loss",
    "reference_kl_loss",
    "over_aggressive_probability_loss",
    "over_aggressive_margin_loss",
    "over_aggressive_reference_excess_loss",
)


class SpbcV2DpoTrainingError(ValueError):
    """Raised when spbc_abr_v2_dpo offline training cannot proceed safely."""


@dataclass(frozen=True)
class SpbcV2DpoTrainingProfile:
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
    label_smoothing: float = 0.02
    ce_loss_weight: float = 0.45
    dpo_loss_weight: float = 0.85
    ranking_loss_weight: float = 0.35
    utility_loss_weight: float = 0.55
    rebuffer_loss_weight: float = 0.45
    dpo_beta: float = 0.20
    ranking_margin_scale: float = 0.15
    utility_temperature: float = 0.55
    rebuffer_loss_cap_s: float = REBUFFER_LOSS_SECONDS_CAP
    aux_reward_loss_weight: float = 0.08
    aux_rebuffer_loss_weight: float = 0.10
    aux_risk_loss_weight: float = 0.08
    reference_kl_loss_weight: float = 0.0
    over_aggressive_probability_loss_weight: float = 0.0
    over_aggressive_margin_loss_weight: float = 0.0
    over_aggressive_reference_excess_loss_weight: float = 0.0
    over_aggressive_margin: float = 0.25
    decision_reward_fusion_weight: float = 0.12
    decision_rebuffer_fusion_weight: float = 0.30
    decision_risk_fusion_weight: float = 0.18
    focus_bucket_sample_weight: float = 1.45
    severe_error_sample_weight: float = 1.25
    safe_vs_rebuffer_pair_weight: float = 1.25
    over_aggressive_rebuffer_action_weight: float = 1.75
    selection_focus_weight: float = 1.00
    selection_rebuffer_weight: float = 4.30
    selection_over_aggressive_weight: float = 0.20
    selection_invalid_weight: float = 10.00
    safety_gate_enabled: bool = False
    safety_global_over_aggressive_tolerance: float = 0.006
    safety_focus_over_aggressive_tolerance: float = 0.015
    safety_spbc_v2_over_aggressive_tolerance: float = 0.012
    safety_utility_regret_tolerance: float = 0.001
    safety_rebuffer_regret_tolerance: float = 0.001
    max_pair_weight: float = 6.0
    seed: int = 450701

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
            "label_smoothing": self.label_smoothing,
            "ce_loss_weight": self.ce_loss_weight,
            "dpo_loss_weight": self.dpo_loss_weight,
            "ranking_loss_weight": self.ranking_loss_weight,
            "utility_loss_weight": self.utility_loss_weight,
            "rebuffer_loss_weight": self.rebuffer_loss_weight,
            "dpo_beta": self.dpo_beta,
            "ranking_margin_scale": self.ranking_margin_scale,
            "utility_temperature": self.utility_temperature,
            "rebuffer_loss_cap_s": self.rebuffer_loss_cap_s,
            "aux_reward_loss_weight": self.aux_reward_loss_weight,
            "aux_rebuffer_loss_weight": self.aux_rebuffer_loss_weight,
            "aux_risk_loss_weight": self.aux_risk_loss_weight,
            "reference_kl_loss_weight": self.reference_kl_loss_weight,
            "over_aggressive_probability_loss_weight": self.over_aggressive_probability_loss_weight,
            "over_aggressive_margin_loss_weight": self.over_aggressive_margin_loss_weight,
            "over_aggressive_reference_excess_loss_weight": self.over_aggressive_reference_excess_loss_weight,
            "over_aggressive_margin": self.over_aggressive_margin,
            "decision_reward_fusion_weight": self.decision_reward_fusion_weight,
            "decision_rebuffer_fusion_weight": self.decision_rebuffer_fusion_weight,
            "decision_risk_fusion_weight": self.decision_risk_fusion_weight,
            "focus_bucket_sample_weight": self.focus_bucket_sample_weight,
            "severe_error_sample_weight": self.severe_error_sample_weight,
            "safe_vs_rebuffer_pair_weight": self.safe_vs_rebuffer_pair_weight,
            "over_aggressive_rebuffer_action_weight": self.over_aggressive_rebuffer_action_weight,
            "selection_focus_weight": self.selection_focus_weight,
            "selection_rebuffer_weight": self.selection_rebuffer_weight,
            "selection_over_aggressive_weight": self.selection_over_aggressive_weight,
            "selection_invalid_weight": self.selection_invalid_weight,
            "safety_gate_enabled": self.safety_gate_enabled,
            "safety_global_over_aggressive_tolerance": self.safety_global_over_aggressive_tolerance,
            "safety_focus_over_aggressive_tolerance": self.safety_focus_over_aggressive_tolerance,
            "safety_spbc_v2_over_aggressive_tolerance": self.safety_spbc_v2_over_aggressive_tolerance,
            "safety_utility_regret_tolerance": self.safety_utility_regret_tolerance,
            "safety_rebuffer_regret_tolerance": self.safety_rebuffer_regret_tolerance,
            "max_pair_weight": self.max_pair_weight,
            "seed": self.seed,
        }


SPBC_V2_DPO_TRAINING_PROFILES: dict[str, SpbcV2DpoTrainingProfile] = {
    "smoke": SpbcV2DpoTrainingProfile(
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
        seed=450711,
    ),
    "pilot": SpbcV2DpoTrainingProfile(
        name="pilot",
        epochs=10,
        batch_size=512,
        learning_rate=6.0e-4,
        max_training_samples=40000,
        max_validation_samples=10000,
        history_hidden_size=128,
        state_hidden_size=96,
        candidate_hidden_size=48,
        shared_hidden_size=192,
        dropout=0.08,
        seed=450721,
    ),
    "full_v1": SpbcV2DpoTrainingProfile(
        name="full_v1",
        epochs=32,
        batch_size=1024,
        learning_rate=4.0e-4,
        max_training_samples=None,
        max_validation_samples=None,
        history_hidden_size=128,
        state_hidden_size=96,
        candidate_hidden_size=48,
        shared_hidden_size=192,
        dropout=0.10,
        seed=450731,
    ),
}


@dataclass(frozen=True)
class PreferencePair:
    preferred_action: int
    rejected_action: int
    reward_gap: float
    qoe_gap: float
    source: str
    weight: float


@dataclass(frozen=True)
class SpbcV2DpoExample:
    sequence: tuple[tuple[float, float], ...]
    scalars: tuple[float, ...]
    candidates: tuple[tuple[float, ...], ...]
    action_mask: tuple[bool, ...]
    oracle_action: int
    best_immediate_action: int
    qoe_gap_by_action: tuple[float, ...]
    rebuffer_s_by_action: tuple[float, ...]
    reward_by_action: tuple[float, ...]
    bitrate_kbps_by_action: tuple[float, ...]
    smoothness_mbps_by_action: tuple[float, ...]
    target_risk_by_action: tuple[float, ...]
    rebuffer_penalty_by_action: tuple[float, ...]
    over_aggressive_action_by_action: tuple[bool, ...]
    pairs: tuple[PreferencePair, ...]
    sample_weight: float
    max_pair_weight: float
    data_role: str
    rollout_source: str
    throughput_bucket: str
    synthetic: bool


@dataclass(frozen=True)
class SpbcV2DpoNormalizationStats:
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


class SpbcAbrV2DpoPolicy(SpbcAbrV1Policy):
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
        decision_reward_fusion_weight: float = 0.12,
        decision_rebuffer_fusion_weight: float = 0.30,
        decision_risk_fusion_weight: float = 0.18,
        rebuffer_prediction_cap_s: float = REBUFFER_LOSS_SECONDS_CAP,
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
        self.decision_reward_fusion_weight = float(decision_reward_fusion_weight)
        self.decision_rebuffer_fusion_weight = float(decision_rebuffer_fusion_weight)
        self.decision_risk_fusion_weight = float(decision_risk_fusion_weight)
        self.rebuffer_prediction_cap_s = float(rebuffer_prediction_cap_s)
        aux_input_dim = self.shared_hidden_size + self.candidate_hidden_size
        self.reward_head = self._auxiliary_head(aux_input_dim)
        self.rebuffer_head = self._auxiliary_head(aux_input_dim)
        self.risk_head = self._auxiliary_head(aux_input_dim)
        self._zero_initialize_auxiliary_heads()

    def _auxiliary_head(self, input_dim: int) -> nn.Sequential:
        return nn.Sequential(
            nn.Linear(input_dim, self.shared_hidden_size),
            nn.ReLU(),
            nn.Dropout(self.dropout),
            nn.Linear(self.shared_hidden_size, 1),
        )

    def _zero_initialize_auxiliary_heads(self) -> None:
        for head in (self.reward_head, self.rebuffer_head, self.risk_head):
            final = head[-1]
            if isinstance(final, nn.Linear):
                nn.init.zeros_(final.weight)
                nn.init.zeros_(final.bias)

    def forward(
        self,
        sequence: torch.Tensor,
        scalars: torch.Tensor,
        candidates: torch.Tensor,
        action_mask: torch.Tensor,
    ) -> Mapping[str, torch.Tensor]:
        if sequence.ndim != 3 or sequence.shape[2] != self.sequence_dim:
            raise SpbcTrainingError("sequence must have shape [batch, history, sequence_dim]")
        if scalars.ndim != 2 or scalars.shape[1] != self.scalar_dim:
            raise SpbcTrainingError("scalars must have shape [batch, scalar_dim]")
        if candidates.ndim != 3 or candidates.shape[2] != self.candidate_dim:
            raise SpbcTrainingError("candidates must have shape [batch, candidates, candidate_dim]")
        if action_mask.shape != candidates.shape[:2]:
            raise SpbcTrainingError("action_mask shape must match candidate rows")

        _history_output, hidden = self.history_encoder(sequence)
        history_vector = hidden[-1]
        state_vector = self.state_encoder(scalars)
        shared = self.shared(torch.cat([history_vector, state_vector], dim=1))

        batch_size, candidate_count, _ = candidates.shape
        candidate_vectors = self.candidate_encoder(candidates)
        expanded_shared = shared.unsqueeze(1).expand(batch_size, candidate_count, self.shared_hidden_size)
        joint = torch.cat([expanded_shared, candidate_vectors], dim=2)

        base_logits = self.policy_head(joint).squeeze(2)
        predicted_reward = self.reward_head(joint).squeeze(2)
        predicted_rebuffer_norm = torch.sigmoid(self.rebuffer_head(joint).squeeze(2))
        predicted_rebuffer_s = predicted_rebuffer_norm * max(float(self.rebuffer_prediction_cap_s), 1.0e-6)
        predicted_risk_logits = self.risk_head(joint).squeeze(2)
        predicted_risk_probability = torch.sigmoid(predicted_risk_logits)

        mask = action_mask.to(dtype=torch.bool, device=base_logits.device)
        valid_counts = torch.clamp(mask.sum(dim=1, keepdim=True).to(dtype=base_logits.dtype), min=1.0)
        reward_sum = predicted_reward.masked_fill(~mask, 0.0).sum(dim=1, keepdim=True)
        centered_reward = predicted_reward - (reward_sum / valid_counts)
        fusion = (
            float(self.decision_reward_fusion_weight) * centered_reward
            - float(self.decision_rebuffer_fusion_weight) * predicted_rebuffer_norm
            - float(self.decision_risk_fusion_weight) * predicted_risk_probability
        )
        logits = base_logits + fusion
        masked_logits = logits.masked_fill(~mask, -1.0e9)
        return {
            "action_logits": masked_logits,
            "base_action_logits": base_logits.masked_fill(~mask, -1.0e9),
            "predicted_reward_n_by_action": predicted_reward.masked_fill(~mask, 0.0),
            "predicted_rebuffer_s_by_action": predicted_rebuffer_s.masked_fill(~mask, 0.0),
            "predicted_target_risk_logits_by_action": predicted_risk_logits.masked_fill(~mask, -1.0e9),
        }

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": SPBC_V2_DPO_MODEL_CONFIG_SCHEMA_ID,
            "model_key": SPBC_V2_DPO_MODEL_KEY,
            "model_family": "Safe Preference Behavioral Cloning ABR v2 DPO",
            "model_type": "gru_candidate_policy_with_auxiliary_utility_risk_heads",
            "sequence_features": list(SEQUENCE_FEATURES),
            "scalar_features": list(SCALAR_FEATURES),
            "candidate_features": list(CANDIDATE_FEATURES),
            "target": "phase45_v2 oracle_action + preference_pairs",
            "forward_input_contract": {
                "allowed_model_input_keys": sorted(MODEL_INPUT_KEYS),
                "allowed_context_keys": sorted(CONTEXT_INPUT_KEYS),
                "allowed_candidate_keys": sorted(CANDIDATE_INPUT_KEYS),
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
            "auxiliary_heads": {
                "predicted_reward_n_by_action": True,
                "predicted_rebuffer_s_by_action": True,
                "predicted_target_risk_logits_by_action": True,
                "targets_used_only_for_training": True,
            },
            "decision_fusion": {
                "enabled": True,
                "reward_weight": self.decision_reward_fusion_weight,
                "rebuffer_weight": self.decision_rebuffer_fusion_weight,
                "risk_weight": self.decision_risk_fusion_weight,
                "rebuffer_prediction_cap_s": self.rebuffer_prediction_cap_s,
            },
            "decision_reward_fusion_weight": self.decision_reward_fusion_weight,
            "decision_rebuffer_fusion_weight": self.decision_rebuffer_fusion_weight,
            "decision_risk_fusion_weight": self.decision_risk_fusion_weight,
            "rebuffer_prediction_cap_s": self.rebuffer_prediction_cap_s,
            "controller_registered": False,
            "bundle_exported": False,
        }


def profile_by_name(name: str) -> SpbcV2DpoTrainingProfile:
    key = str(name).strip()
    if key not in SPBC_V2_DPO_TRAINING_PROFILES:
        raise SpbcV2DpoTrainingError("unknown spbc_abr_v2_dpo training profile: {0}".format(name))
    return SPBC_V2_DPO_TRAINING_PROFILES[key]


def train_spbc_abr_v2_dpo(
    dataset_dir: object,
    output_dir: object,
    *,
    profile: SpbcV2DpoTrainingProfile,
    overwrite: bool = False,
    device: str = "auto",
    init_checkpoint: object | None = None,
    allow_random_init_full: bool = False,
    epochs: int | None = None,
    batch_size: int | None = None,
    learning_rate: float | None = None,
    max_training_samples: int | None | str = "profile",
    max_validation_samples: int | None | str = "profile",
    validate_dataset: bool = True,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
) -> Mapping[str, object]:
    _emit_progress(progress_callback, "preparing", "Preparando entrenamiento spbc_abr_v2_dpo")
    data_path = ensure_existing_dir(dataset_dir, purpose="phase45_v2 preference dataset")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="spbc_abr_v2_dpo model")
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
    _validate_training_args(active_epochs, active_batch_size, active_learning_rate, train_limit, val_limit, profile)

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
    training_examples = load_spbc_v2_dpo_examples(
        data_path / V2_DATA_FILENAMES[TRAINING_ROLE],
        TRAINING_ROLE,
        limit=train_limit,
        max_pair_weight=profile.max_pair_weight,
        focus_bucket_sample_weight=profile.focus_bucket_sample_weight,
        severe_error_sample_weight=profile.severe_error_sample_weight,
        safe_vs_rebuffer_pair_weight=profile.safe_vs_rebuffer_pair_weight,
        over_aggressive_rebuffer_action_weight=profile.over_aggressive_rebuffer_action_weight,
        rebuffer_loss_cap_s=profile.rebuffer_loss_cap_s,
    )
    validation_examples = load_spbc_v2_dpo_examples(
        data_path / V2_DATA_FILENAMES[VALIDATION_ROLE],
        VALIDATION_ROLE,
        limit=val_limit,
        max_pair_weight=profile.max_pair_weight,
        focus_bucket_sample_weight=profile.focus_bucket_sample_weight,
        severe_error_sample_weight=profile.severe_error_sample_weight,
        safe_vs_rebuffer_pair_weight=profile.safe_vs_rebuffer_pair_weight,
        over_aggressive_rebuffer_action_weight=profile.over_aggressive_rebuffer_action_weight,
        rebuffer_loss_cap_s=profile.rebuffer_loss_cap_s,
    )
    if not training_examples or not validation_examples:
        raise SpbcV2DpoTrainingError("spbc_abr_v2_dpo training requires training and validation examples")
    _emit_progress(
        progress_callback,
        "examples_loaded",
        "Muestras v2 cargadas",
        training_samples=len(training_examples),
        validation_samples=len(validation_examples),
    )

    init_payload = _load_initial_checkpoint(init_checkpoint, profile, allow_random_init_full)
    if profile.safety_gate_enabled and init_payload is None:
        raise SpbcV2DpoTrainingError("safety_gate_enabled requires an init checkpoint reference")
    normalization = _normalization_from_init_checkpoint(init_payload)
    if normalization is None:
        normalization = fit_spbc_v2_dpo_normalization(training_examples)
    model = _build_model_from_profile_or_checkpoint(profile, init_payload).to(selected_device)
    state_load_report = {"loaded": False, "missing_keys": [], "unexpected_keys": []}
    if init_payload is not None:
        state_load_report = _load_initial_state_dict(model, init_payload)
    reference_model = _clone_reference_model(model, selected_device)
    train_tensors = examples_to_tensors(training_examples, normalization)
    validation_tensors = examples_to_tensors(validation_examples, normalization)
    optimizer = torch.optim.AdamW(model.parameters(), lr=active_learning_rate)
    generator = torch.Generator()
    generator.manual_seed(profile.seed)
    train_loader = DataLoader(TensorDataset(*train_tensors), batch_size=active_batch_size, shuffle=True, generator=generator)
    train_eval_loader = DataLoader(TensorDataset(*train_tensors), batch_size=active_batch_size, shuffle=False)
    validation_loader = DataLoader(TensorDataset(*validation_tensors), batch_size=active_batch_size, shuffle=False)

    reference_validation_metrics_for_selection = None
    initial_state_dict = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}
    if profile.safety_gate_enabled:
        _emit_progress(
            progress_callback,
            "reference_gate_evaluation_started",
            "Calculando referencia congelada para safety gate",
        )
        reference_validation_metrics_for_selection = evaluate_spbc_v2_dpo_model(
            reference_model,
            reference_model,
            validation_loader,
            device=selected_device,
            profile=profile,
            examples=validation_examples,
        )

    epoch_reports = []
    best_validation_loss = math.inf
    best_validation_selection_score = (
        _selection_score(reference_validation_metrics_for_selection, profile)
        if reference_validation_metrics_for_selection is not None
        else math.inf
    )
    best_state_dict = initial_state_dict if profile.safety_gate_enabled else None
    best_epoch = 0
    for epoch in range(1, active_epochs + 1):
        epoch_started = time.monotonic()
        _emit_progress(
            progress_callback,
            "epoch_started",
            "Iniciando epoca spbc_v2_dpo",
            epoch=epoch,
            epochs=active_epochs,
            train_batches=len(train_loader),
        )
        train_metrics = _run_epoch(
            model,
            reference_model,
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
            "Validando epoca spbc_v2_dpo",
            epoch=epoch,
            epochs=active_epochs,
            validation_batches=len(validation_loader),
        )
        validation_metrics = evaluate_spbc_v2_dpo_model(
            model,
            reference_model,
            validation_loader,
            device=selected_device,
            profile=profile,
            examples=validation_examples,
        )
        critical_metrics = _critical_metric_summary(validation_metrics)
        critical_delta = _critical_metric_delta(
            validation_metrics,
            reference_validation_metrics_for_selection,
        )
        safety_gate = _safety_gate_result(
            validation_metrics,
            reference_validation_metrics_for_selection,
            profile,
        )
        epoch_report = {
            "epoch": epoch,
            "training_loss": train_metrics["loss"],
            "training_ce_loss": train_metrics["ce_loss"],
            "training_dpo_loss": train_metrics["dpo_loss"],
            "training_ranking_loss": train_metrics["ranking_loss"],
            "training_utility_loss": train_metrics["utility_loss"],
            "training_rebuffer_loss": train_metrics["rebuffer_loss"],
            "training_aux_reward_loss": train_metrics["aux_reward_loss"],
            "training_aux_rebuffer_loss": train_metrics["aux_rebuffer_loss"],
            "training_aux_risk_loss": train_metrics["aux_risk_loss"],
            "training_reference_kl_loss": train_metrics["reference_kl_loss"],
            "training_over_aggressive_probability_loss": train_metrics["over_aggressive_probability_loss"],
            "training_over_aggressive_margin_loss": train_metrics["over_aggressive_margin_loss"],
            "training_over_aggressive_reference_excess_loss": train_metrics["over_aggressive_reference_excess_loss"],
            "validation_loss": validation_metrics["loss"],
            "validation_utility_loss": validation_metrics["utility_loss"],
            "validation_rebuffer_loss": validation_metrics["rebuffer_loss"],
            "validation_aux_reward_loss": validation_metrics["aux_reward_loss"],
            "validation_aux_rebuffer_loss": validation_metrics["aux_rebuffer_loss"],
            "validation_aux_risk_loss": validation_metrics["aux_risk_loss"],
            "validation_reference_kl_loss": validation_metrics["reference_kl_loss"],
            "validation_over_aggressive_probability_loss": validation_metrics["over_aggressive_probability_loss"],
            "validation_over_aggressive_margin_loss": validation_metrics["over_aggressive_margin_loss"],
            "validation_over_aggressive_reference_excess_loss": validation_metrics[
                "over_aggressive_reference_excess_loss"
            ],
            "validation_top1_accuracy": validation_metrics["top1_accuracy"],
            "validation_pair_preference_accuracy": validation_metrics["pair_preference_accuracy"],
            "validation_predicted_qoe_gap_mean": validation_metrics["predicted_qoe_gap_mean"],
            "validation_selected_utility_regret_vs_best_immediate_mean": validation_metrics[
                "selected_utility_regret_vs_best_immediate_mean"
            ],
            "validation_selected_rebuffer_regret_vs_best_immediate_mean": validation_metrics[
                "selected_rebuffer_regret_vs_best_immediate_mean"
            ],
            "validation_critical_metrics": critical_metrics,
            "validation_critical_delta_candidate_minus_reference": critical_delta,
            "validation_safety_gate": safety_gate,
            **_flatten_epoch_critical_metrics(critical_metrics),
        }
        selection_score = _selection_score(validation_metrics, profile)
        epoch_report["validation_selection_score"] = selection_score
        epoch_report["validation_safety_gate_passed"] = bool(safety_gate["passed"])
        epoch_reports.append(epoch_report)
        best_validation_loss = min(best_validation_loss, float(validation_metrics["loss"]))
        is_best = bool(safety_gate["passed"]) and float(selection_score) < best_validation_selection_score
        if is_best:
            best_validation_selection_score = float(selection_score)
            best_epoch = epoch
            best_state_dict = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}
        _emit_progress(
            progress_callback,
            "epoch_finished",
            "Epoca spbc_v2_dpo completada",
            epoch=epoch,
            epochs=active_epochs,
            epoch_duration_s=time.monotonic() - epoch_started,
            training_loss=train_metrics["loss"],
            validation_loss=validation_metrics["loss"],
            validation_top1_accuracy=validation_metrics["top1_accuracy"],
            validation_pair_preference_accuracy=validation_metrics["pair_preference_accuracy"],
            validation_predicted_qoe_gap_mean=validation_metrics["predicted_qoe_gap_mean"],
            validation_utility_regret=validation_metrics["selected_utility_regret_vs_best_immediate_mean"],
            validation_rebuffer_regret=validation_metrics["selected_rebuffer_regret_vs_best_immediate_mean"],
            validation_over_aggressive=validation_metrics["over_aggressive_rate_vs_oracle"],
            validation_under_aggressive=validation_metrics["under_aggressive_rate_vs_oracle"],
            validation_focus_over_aggressive=critical_metrics[FOCUS_THROUGHPUT_BUCKET]["over_aggressive_rate_vs_oracle"],
            validation_safety_gate_passed=safety_gate["passed"],
            validation_selection_score=selection_score,
            best_epoch=best_epoch,
            best_so_far=is_best,
        )

    if best_state_dict is not None:
        model.load_state_dict(best_state_dict)
    _emit_progress(progress_callback, "final_evaluation_started", "Calculando metricas finales spbc_v2_dpo")
    final_training_metrics = evaluate_spbc_v2_dpo_model(
        model,
        reference_model,
        train_eval_loader,
        device=selected_device,
        profile=profile,
        examples=training_examples,
    )
    final_validation_metrics = evaluate_spbc_v2_dpo_model(
        model,
        reference_model,
        validation_loader,
        device=selected_device,
        profile=profile,
        examples=validation_examples,
    )
    reference_training_metrics = None
    reference_validation_metrics = reference_validation_metrics_for_selection
    if init_payload is not None:
        _emit_progress(progress_callback, "reference_evaluation_started", "Comparando contra checkpoint inicial congelado")
        reference_training_metrics = evaluate_spbc_v2_dpo_model(
            reference_model,
            reference_model,
            train_eval_loader,
            device=selected_device,
            profile=profile,
            examples=training_examples,
        )
        if reference_validation_metrics is None:
            reference_validation_metrics = evaluate_spbc_v2_dpo_model(
                reference_model,
                reference_model,
                validation_loader,
                device=selected_device,
                profile=profile,
                examples=validation_examples,
            )

    model_config = dict(model.config())
    normalization_payload = normalization.to_json()
    checkpoint_path = output_path / SPBC_V2_DPO_MODEL_FILENAME
    config_path = output_path / SPBC_V2_DPO_MODEL_CONFIG_FILENAME
    normalization_path = output_path / SPBC_V2_DPO_NORMALIZATION_FILENAME
    report_path = output_path / SPBC_V2_DPO_TRAINING_REPORT_FILENAME
    checkpoint = {
        "schema_id": SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
        "model_key": SPBC_V2_DPO_MODEL_KEY,
        "model_state_dict": model.state_dict(),
        "model_config": model_config,
        "normalization": normalization_payload,
        "training_profile": profile.to_json(),
        "init_checkpoint": init_payload["path"] if init_payload is not None else None,
        "init_checkpoint_sha256": init_payload["sha256"] if init_payload is not None else None,
        "reference_policy_source": _reference_policy_source(init_payload),
        "best_epoch": best_epoch,
        "best_validation_selection_score": best_validation_selection_score,
        "best_validation_loss_seen": best_validation_loss,
        "safety_gate_enabled": bool(profile.safety_gate_enabled),
        "device_used": str(selected_device),
        "controller_registered": False,
        "bundle_exported": False,
    }
    torch.save(checkpoint, checkpoint_path)
    write_json(config_path, model_config)
    write_json(normalization_path, normalization_payload)
    duration_s = time.monotonic() - started
    report = {
        "schema_id": SPBC_V2_DPO_TRAINING_REPORT_SCHEMA_ID,
        "human_readable_name": "Entrenamiento offline de spbc_abr_v2_dpo",
        "phase": "fase_4_5_v1_bloque7b3_entrenamiento_spbc_abr_v2_dpo_utility_risk",
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
            "criterion": "validation_selection_score_with_safety_gate"
            if profile.safety_gate_enabled
            else "validation_selection_score",
            "lower_is_better": True,
            "uses_eval_split": False,
            "focus_throughput_bucket": FOCUS_THROUGHPUT_BUCKET,
            "safety_gate_enabled": bool(profile.safety_gate_enabled),
            "safety_gate_mode": "relative_to_initial_checkpoint" if profile.safety_gate_enabled else "disabled",
            "safety_gate_fallback_epoch": 0,
            "safety_gate_tolerances": _safety_gate_tolerances(profile),
        },
        "epoch_reports": epoch_reports,
        "training_metrics": final_training_metrics,
        "validation_metrics": final_validation_metrics,
        "safety_gate_reference_validation_critical_metrics": _critical_metric_summary(
            reference_validation_metrics_for_selection
        )
        if reference_validation_metrics_for_selection is not None
        else None,
        "selected_checkpoint_safety_gate": _safety_gate_result(
            final_validation_metrics,
            reference_validation_metrics_for_selection,
            profile,
        ),
        "init_checkpoint_reference_comparison": _build_checkpoint_reference_comparison(
            training_metrics=final_training_metrics,
            validation_metrics=final_validation_metrics,
            reference_training_metrics=reference_training_metrics,
            reference_validation_metrics=reference_validation_metrics,
            reference_label=_reference_policy_source(init_payload),
            unavailable_reason="init checkpoint not available",
        ),
        "spbc_v1_reference_comparison": _build_reference_comparison(
            training_metrics=final_training_metrics,
            validation_metrics=final_validation_metrics,
            reference_training_metrics=reference_training_metrics
            if init_payload is not None and init_payload.get("model_key") == "spbc_abr_v1"
            else None,
            reference_validation_metrics=reference_validation_metrics
            if init_payload is not None and init_payload.get("model_key") == "spbc_abr_v1"
            else None,
        ),
        "training_duration_s": duration_s,
        "model_config": model_config,
        "init_checkpoint": init_payload["path"] if init_payload is not None else None,
        "init_checkpoint_sha256": init_payload["sha256"] if init_payload is not None else None,
        "reference_policy_source": _reference_policy_source(init_payload),
        "state_load_report": state_load_report,
        "loss_design": {
            "cross_entropy_target": "oracle_action",
            "cross_entropy_role": "anchor_not_primary_objective",
            "dpo_pairs": "preference_pairs",
            "dpo_reference_policy": _reference_policy_source(init_payload),
            "dpo_formula": "-logsigmoid(beta * ((logp_theta(preferred)-logp_theta(rejected)) - (logp_ref(preferred)-logp_ref(rejected))))",
            "ranking_weighted_by": "normalized_capped_reward_gap/qoe_gap/source",
            "utility_loss": "cross_entropy_against_softmax_reward_distribution_over_valid_actions",
            "utility_temperature": profile.utility_temperature,
            "rebuffer_loss": "expected_normalized_rebuffer_penalty_under_policy_distribution",
            "rebuffer_loss_cap_s": profile.rebuffer_loss_cap_s,
            "auxiliary_reward_loss": "masked_smooth_l1_prediction_of_reward_n_by_action",
            "auxiliary_rebuffer_loss": "masked_smooth_l1_prediction_of_capped_rebuffer_by_action",
            "auxiliary_risk_loss": "masked_bce_prediction_of_target_risk_by_action",
            "reference_kl_loss": "weighted_KL(policy_distribution || frozen_reference_distribution)",
            "reference_kl_loss_weight": profile.reference_kl_loss_weight,
            "over_aggressive_probability_loss": "expected_policy_probability_on_actions_marked_over_aggressive_rebuffer",
            "over_aggressive_probability_loss_weight": profile.over_aggressive_probability_loss_weight,
            "over_aggressive_margin_loss": "softplus_margin_between_best_immediate_action_and_over_aggressive_actions",
            "over_aggressive_margin_loss_weight": profile.over_aggressive_margin_loss_weight,
            "over_aggressive_reference_excess_loss": "positive_policy_probability_excess_over_frozen_reference_on_over_aggressive_actions",
            "over_aggressive_reference_excess_loss_weight": profile.over_aggressive_reference_excess_loss_weight,
            "over_aggressive_margin": profile.over_aggressive_margin,
            "decision_fusion": "policy_logits_plus_predicted_utility_minus_predicted_rebuffer_and_risk",
            "decision_reward_fusion_weight": profile.decision_reward_fusion_weight,
            "decision_rebuffer_fusion_weight": profile.decision_rebuffer_fusion_weight,
            "decision_risk_fusion_weight": profile.decision_risk_fusion_weight,
            "checkpoint_selected_by": "validation_selection_score_with_reference_relative_safety_gate"
            if profile.safety_gate_enabled
            else "validation_selection_score_aligned_with_regret_rebuffer_focus_bucket",
            "selection_focus_weight": profile.selection_focus_weight,
            "selection_rebuffer_weight": profile.selection_rebuffer_weight,
            "selection_over_aggressive_weight": profile.selection_over_aggressive_weight,
            "selection_invalid_weight": profile.selection_invalid_weight,
            "safety_gate": _safety_gate_tolerances(profile),
            "pair_weights_normalized_and_capped": True,
            "sample_weights_include_focus_bucket_and_severe_errors": True,
            "focus_throughput_bucket": FOCUS_THROUGHPUT_BUCKET,
            "focus_bucket_sample_weight": profile.focus_bucket_sample_weight,
            "severe_error_sample_weight": profile.severe_error_sample_weight,
            "safe_vs_rebuffer_pair_weight": profile.safe_vs_rebuffer_pair_weight,
            "over_aggressive_rebuffer_action_weight": profile.over_aggressive_rebuffer_action_weight,
            "max_pair_weight": profile.max_pair_weight,
            "soft_utility_ranking_loss_enabled": float(profile.ranking_loss_weight) > 0.0,
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
        "normalization_source_checkpoint": normalization_payload["source_checkpoint"],
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
        "preference_fields_are_model_features": False,
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
        "Entrenamiento spbc_abr_v2_dpo finalizado",
        training_duration_s=duration_s,
        output_dir=str(output_path),
        best_epoch=best_epoch,
    )
    return report


def load_spbc_v2_dpo_examples(
    path: object,
    data_role: str,
    *,
    limit: int | None = None,
    max_pair_weight: float = 6.0,
    focus_bucket_sample_weight: float = 1.45,
    severe_error_sample_weight: float = 1.25,
    safe_vs_rebuffer_pair_weight: float = 1.25,
    over_aggressive_rebuffer_action_weight: float = 1.75,
    rebuffer_loss_cap_s: float = REBUFFER_LOSS_SECONDS_CAP,
) -> tuple[SpbcV2DpoExample, ...]:
    examples = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                raw = json.loads(text)
            except json.JSONDecodeError as exc:
                raise SpbcV2DpoTrainingError("{0}: invalid JSONL line {1}".format(path, line_number)) from exc
            examples.append(
                _example_from_sample(
                    raw,
                    data_role,
                    line_number,
                    max_pair_weight=max_pair_weight,
                    focus_bucket_sample_weight=focus_bucket_sample_weight,
                    severe_error_sample_weight=severe_error_sample_weight,
                    safe_vs_rebuffer_pair_weight=safe_vs_rebuffer_pair_weight,
                    over_aggressive_rebuffer_action_weight=over_aggressive_rebuffer_action_weight,
                    rebuffer_loss_cap_s=rebuffer_loss_cap_s,
                )
            )
            if limit is not None and len(examples) >= int(limit):
                break
    return tuple(examples)


def fit_spbc_v2_dpo_normalization(examples: Sequence[SpbcV2DpoExample]) -> SpbcV2DpoNormalizationStats:
    if not examples:
        raise SpbcV2DpoTrainingError("normalization requires training examples")
    sequence_rows = [step for example in examples for step in example.sequence]
    scalar_rows = [example.scalars for example in examples]
    candidate_rows = [candidate for example in examples for candidate in example.candidates]
    return SpbcV2DpoNormalizationStats(
        schema_id="phase45_v2_spbc_dpo_normalization_v1",
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


def examples_to_tensors(
    examples: Sequence[SpbcV2DpoExample],
    normalization: SpbcV2DpoNormalizationStats,
) -> tuple[torch.Tensor, ...]:
    if not examples:
        raise SpbcV2DpoTrainingError("examples_to_tensors requires examples")
    max_candidates = max(len(example.candidates) for example in examples)
    max_pairs = max(len(example.pairs) for example in examples)
    sequence_rows = []
    scalar_rows = []
    candidate_rows = []
    mask_rows = []
    labels = []
    best_labels = []
    qoe_gap_rows = []
    rebuffer_rows = []
    reward_rows = []
    bitrate_rows = []
    smoothness_rows = []
    target_risk_rows = []
    sample_weights = []
    pair_preferred_rows = []
    pair_rejected_rows = []
    pair_weight_rows = []
    pair_reward_gap_rows = []
    pair_mask_rows = []
    rebuffer_penalty_rows = []
    over_aggressive_action_rows = []
    for example in examples:
        if example.oracle_action >= len(example.candidates):
            raise SpbcV2DpoTrainingError("oracle_action outside candidate range")
        if not example.action_mask[example.oracle_action]:
            raise SpbcV2DpoTrainingError("oracle_action is masked as invalid")
        sequence_rows.append(_normalize_matrix(example.sequence, normalization.sequence_mean, normalization.sequence_std))
        scalar_rows.append(_normalize_vector(example.scalars, normalization.scalar_mean, normalization.scalar_std))
        candidates = [_normalize_vector(candidate, normalization.candidate_mean, normalization.candidate_std) for candidate in example.candidates]
        mask = [bool(value) for value in example.action_mask]
        qoe_gaps = [float(value) for value in example.qoe_gap_by_action]
        rebuffer = [float(value) for value in example.rebuffer_s_by_action]
        rewards = [float(value) for value in example.reward_by_action]
        bitrates = [float(value) for value in example.bitrate_kbps_by_action]
        smoothness = [float(value) for value in example.smoothness_mbps_by_action]
        target_risks = [float(value) for value in example.target_risk_by_action]
        rebuffer_penalties = [float(value) for value in example.rebuffer_penalty_by_action]
        over_aggressive_actions = [bool(value) for value in example.over_aggressive_action_by_action]
        while len(candidates) < max_candidates:
            candidates.append([0.0 for _ in CANDIDATE_FEATURES])
            mask.append(False)
            qoe_gaps.append(0.0)
            rebuffer.append(0.0)
            rewards.append(0.0)
            bitrates.append(0.0)
            smoothness.append(0.0)
            target_risks.append(1.0)
            rebuffer_penalties.append(1.0)
            over_aggressive_actions.append(False)
        pair_preferred = [pair.preferred_action for pair in example.pairs]
        pair_rejected = [pair.rejected_action for pair in example.pairs]
        pair_weight = [min(pair.weight * float(example.sample_weight), float(example.max_pair_weight)) for pair in example.pairs]
        pair_reward_gap = [max(pair.reward_gap, 0.0) for pair in example.pairs]
        pair_mask = [True for _pair in example.pairs]
        while len(pair_preferred) < max_pairs:
            pair_preferred.append(0)
            pair_rejected.append(0)
            pair_weight.append(0.0)
            pair_reward_gap.append(0.0)
            pair_mask.append(False)
        candidate_rows.append(candidates)
        mask_rows.append(mask)
        labels.append(int(example.oracle_action))
        best_labels.append(int(example.best_immediate_action))
        qoe_gap_rows.append(qoe_gaps)
        rebuffer_rows.append(rebuffer)
        reward_rows.append(rewards)
        bitrate_rows.append(bitrates)
        smoothness_rows.append(smoothness)
        target_risk_rows.append(target_risks)
        sample_weights.append(float(example.sample_weight))
        pair_preferred_rows.append(pair_preferred)
        pair_rejected_rows.append(pair_rejected)
        pair_weight_rows.append(pair_weight)
        pair_reward_gap_rows.append(pair_reward_gap)
        pair_mask_rows.append(pair_mask)
        rebuffer_penalty_rows.append(rebuffer_penalties)
        over_aggressive_action_rows.append(over_aggressive_actions)
    return (
        torch.tensor(sequence_rows, dtype=torch.float32),
        torch.tensor(scalar_rows, dtype=torch.float32),
        torch.tensor(candidate_rows, dtype=torch.float32),
        torch.tensor(mask_rows, dtype=torch.bool),
        torch.tensor(labels, dtype=torch.long),
        torch.tensor(best_labels, dtype=torch.long),
        torch.tensor(qoe_gap_rows, dtype=torch.float32),
        torch.tensor(rebuffer_rows, dtype=torch.float32),
        torch.tensor(reward_rows, dtype=torch.float32),
        torch.tensor(bitrate_rows, dtype=torch.float32),
        torch.tensor(smoothness_rows, dtype=torch.float32),
        torch.tensor(target_risk_rows, dtype=torch.float32),
        torch.tensor(sample_weights, dtype=torch.float32),
        torch.tensor(pair_preferred_rows, dtype=torch.long),
        torch.tensor(pair_rejected_rows, dtype=torch.long),
        torch.tensor(pair_weight_rows, dtype=torch.float32),
        torch.tensor(pair_reward_gap_rows, dtype=torch.float32),
        torch.tensor(pair_mask_rows, dtype=torch.bool),
        torch.tensor(rebuffer_penalty_rows, dtype=torch.float32),
        torch.tensor(over_aggressive_action_rows, dtype=torch.bool),
    )


def evaluate_spbc_v2_dpo_model(
    model: SpbcAbrV2DpoPolicy,
    reference_model: SpbcAbrV2DpoPolicy,
    loader: DataLoader,
    *,
    device: torch.device,
    profile: SpbcV2DpoTrainingProfile,
    examples: Sequence[SpbcV2DpoExample],
) -> Mapping[str, object]:
    model.eval()
    reference_model.eval()
    totals = _PolicyMetricTotals()
    by_bucket: dict[str, _PolicyMetricTotals] = defaultdict(_PolicyMetricTotals)
    by_rollout: dict[str, _PolicyMetricTotals] = defaultdict(_PolicyMetricTotals)
    start_index = 0
    with torch.no_grad():
        for batch in loader:
            moved = _move_batch(batch, device)
            outputs = model(moved[0], moved[1], moved[2], moved[3])
            ref_outputs = reference_model(moved[0], moved[1], moved[2], moved[3])
            losses = _loss_components(outputs, ref_outputs, moved, profile)
            observations = _policy_observations(outputs, moved)
            batch_size = int(moved[0].shape[0])
            totals.add_observations(observations, losses, batch_size)
            for row_offset, observation in enumerate(observations):
                example = examples[start_index + row_offset]
                by_bucket[example.throughput_bucket].add_observations((observation,), {}, 1)
                by_rollout[example.rollout_source].add_observations((observation,), {}, 1)
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
    }


def resolve_torch_device(requested: str) -> torch.device:
    key = str(requested).strip().lower()
    if key == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if key == "cuda" and not torch.cuda.is_available():
        raise SpbcV2DpoTrainingError("CUDA/ROCm device requested but torch.cuda.is_available() is false")
    if key not in {"cpu", "cuda"}:
        raise SpbcV2DpoTrainingError("device must be cpu, cuda or auto")
    return torch.device(key)


def set_training_seed(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed))


def _run_epoch(
    model: SpbcAbrV2DpoPolicy,
    reference_model: SpbcAbrV2DpoPolicy,
    loader: DataLoader,
    *,
    device: torch.device,
    optimizer: torch.optim.Optimizer,
    profile: SpbcV2DpoTrainingProfile,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
    epoch: int | None = None,
    epochs: int | None = None,
) -> Mapping[str, float]:
    model.train()
    reference_model.eval()
    totals = _LossTotals()
    total_batches = len(loader)
    progress_every = _progress_batch_interval(total_batches)
    epoch_started = time.monotonic()
    for batch_index, batch in enumerate(loader, start=1):
        moved = _move_batch(batch, device)
        optimizer.zero_grad()
        outputs = model(moved[0], moved[1], moved[2], moved[3])
        with torch.no_grad():
            ref_outputs = reference_model(moved[0], moved[1], moved[2], moved[3])
        losses = _loss_components(outputs, ref_outputs, moved, profile)
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
                "Entrenando batches spbc_v2_dpo",
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
    ref_outputs: Mapping[str, torch.Tensor],
    batch: Sequence[torch.Tensor],
    profile: SpbcV2DpoTrainingProfile,
) -> dict[str, torch.Tensor]:
    logits = outputs["action_logits"]
    ref_logits = ref_outputs["action_logits"].detach()
    mask = batch[3].to(dtype=torch.bool)
    labels = batch[4]
    rewards = batch[8]
    rebuffer_s = batch[7]
    target_risks = batch[11]
    rebuffer_penalties = batch[18]
    over_aggressive_actions = batch[19] if len(batch) > 19 else torch.zeros_like(rebuffer_penalties, dtype=torch.bool)
    sample_weights = batch[12]
    pair_preferred = batch[13]
    pair_rejected = batch[14]
    pair_weights = batch[15]
    pair_reward_gaps = batch[16]
    pair_mask = batch[17].to(dtype=torch.bool)
    ce_loss = _masked_weighted_cross_entropy(
        logits,
        labels,
        mask,
        sample_weights,
        label_smoothing=float(profile.label_smoothing),
    )
    dpo_loss = _dpo_loss(
        logits,
        ref_logits,
        pair_preferred,
        pair_rejected,
        pair_weights,
        pair_mask,
        beta=float(profile.dpo_beta),
    )
    ranking_loss = _ranking_loss(
        logits,
        pair_preferred,
        pair_rejected,
        pair_weights,
        pair_reward_gaps,
        pair_mask,
        margin_scale=float(profile.ranking_margin_scale),
    )
    utility_loss = _utility_distribution_loss(
        logits,
        rewards,
        mask,
        sample_weights,
        temperature=float(profile.utility_temperature),
    )
    rebuffer_loss = _expected_rebuffer_penalty_loss(
        logits,
        rebuffer_penalties,
        mask,
        sample_weights,
    )
    aux_reward_loss = _masked_weighted_smooth_l1(
        outputs["predicted_reward_n_by_action"],
        rewards,
        mask,
        sample_weights,
    )
    aux_rebuffer_loss = _masked_weighted_smooth_l1(
        outputs["predicted_rebuffer_s_by_action"] / max(float(profile.rebuffer_loss_cap_s), 1.0e-6),
        torch.clamp(rebuffer_s, min=0.0, max=float(profile.rebuffer_loss_cap_s)) / max(float(profile.rebuffer_loss_cap_s), 1.0e-6),
        mask,
        sample_weights,
    )
    aux_risk_loss = _masked_weighted_binary_cross_entropy(
        outputs["predicted_target_risk_logits_by_action"],
        target_risks,
        mask,
        sample_weights,
    )
    reference_kl_loss = _masked_weighted_kl_to_reference_loss(
        logits,
        ref_logits,
        mask,
        sample_weights,
    )
    over_aggressive_probability_loss = _expected_over_aggressive_probability_loss(
        logits,
        over_aggressive_actions,
        mask,
        sample_weights,
    )
    over_aggressive_margin_loss = _over_aggressive_margin_loss(
        logits,
        batch[5],
        over_aggressive_actions,
        mask,
        sample_weights,
        margin=float(profile.over_aggressive_margin),
    )
    over_aggressive_reference_excess_loss = _over_aggressive_reference_excess_loss(
        logits,
        ref_logits,
        over_aggressive_actions,
        mask,
        sample_weights,
    )
    loss = (
        float(profile.ce_loss_weight) * ce_loss
        + float(profile.dpo_loss_weight) * dpo_loss
        + float(profile.ranking_loss_weight) * ranking_loss
        + float(profile.utility_loss_weight) * utility_loss
        + float(profile.rebuffer_loss_weight) * rebuffer_loss
        + float(profile.aux_reward_loss_weight) * aux_reward_loss
        + float(profile.aux_rebuffer_loss_weight) * aux_rebuffer_loss
        + float(profile.aux_risk_loss_weight) * aux_risk_loss
        + float(profile.reference_kl_loss_weight) * reference_kl_loss
        + float(profile.over_aggressive_probability_loss_weight) * over_aggressive_probability_loss
        + float(profile.over_aggressive_margin_loss_weight) * over_aggressive_margin_loss
        + float(profile.over_aggressive_reference_excess_loss_weight) * over_aggressive_reference_excess_loss
    )
    return {
        "loss_tensor": loss,
        "loss": loss.detach(),
        "ce_loss": ce_loss.detach(),
        "dpo_loss": dpo_loss.detach(),
        "ranking_loss": ranking_loss.detach(),
        "utility_loss": utility_loss.detach(),
        "rebuffer_loss": rebuffer_loss.detach(),
        "aux_reward_loss": aux_reward_loss.detach(),
        "aux_rebuffer_loss": aux_rebuffer_loss.detach(),
        "aux_risk_loss": aux_risk_loss.detach(),
        "reference_kl_loss": reference_kl_loss.detach(),
        "over_aggressive_probability_loss": over_aggressive_probability_loss.detach(),
        "over_aggressive_margin_loss": over_aggressive_margin_loss.detach(),
        "over_aggressive_reference_excess_loss": over_aggressive_reference_excess_loss.detach(),
    }


def _masked_weighted_cross_entropy(
    logits: torch.Tensor,
    labels: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
    *,
    label_smoothing: float,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    active_logits = logits.masked_fill(~active_mask, -1.0e9)
    log_probs = F.log_softmax(active_logits, dim=1)
    valid_counts = active_mask.sum(dim=1).to(dtype=logits.dtype)
    smoothing = max(min(float(label_smoothing), 0.50), 0.0)
    non_target_counts = torch.clamp(valid_counts - 1.0, min=1.0)
    smooth_each = torch.where(valid_counts > 1.0, torch.full_like(valid_counts, smoothing) / non_target_counts, torch.zeros_like(valid_counts))
    target_confidence = torch.where(valid_counts > 1.0, torch.full_like(valid_counts, 1.0 - smoothing), torch.ones_like(valid_counts))
    target_distribution = active_mask.to(dtype=logits.dtype) * smooth_each.unsqueeze(1)
    target_distribution.scatter_(1, labels.view(-1, 1), target_confidence.view(-1, 1))
    per_sample_loss = -(target_distribution * log_probs).sum(dim=1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _dpo_loss(
    logits: torch.Tensor,
    ref_logits: torch.Tensor,
    preferred: torch.Tensor,
    rejected: torch.Tensor,
    pair_weights: torch.Tensor,
    pair_mask: torch.Tensor,
    *,
    beta: float,
) -> torch.Tensor:
    log_probs = F.log_softmax(logits, dim=1)
    ref_log_probs = F.log_softmax(ref_logits, dim=1)
    pref_lp = torch.gather(log_probs, 1, preferred)
    rej_lp = torch.gather(log_probs, 1, rejected)
    ref_pref_lp = torch.gather(ref_log_probs, 1, preferred)
    ref_rej_lp = torch.gather(ref_log_probs, 1, rejected)
    margin = (pref_lp - rej_lp) - (ref_pref_lp - ref_rej_lp)
    raw = -F.logsigmoid(float(beta) * margin)
    weights = pair_weights.to(device=logits.device, dtype=logits.dtype)
    mask = pair_mask.to(device=logits.device, dtype=logits.dtype)
    return (raw * weights * mask).sum() / torch.clamp((weights * mask).sum(), min=1.0)


def _ranking_loss(
    logits: torch.Tensor,
    preferred: torch.Tensor,
    rejected: torch.Tensor,
    pair_weights: torch.Tensor,
    reward_gaps: torch.Tensor,
    pair_mask: torch.Tensor,
    *,
    margin_scale: float,
) -> torch.Tensor:
    pref_logits = torch.gather(logits, 1, preferred)
    rej_logits = torch.gather(logits, 1, rejected)
    required_margin = torch.clamp(reward_gaps.to(dtype=logits.dtype, device=logits.device), min=0.0, max=10.0) * float(margin_scale)
    raw = F.relu(required_margin - (pref_logits - rej_logits))
    weights = pair_weights.to(device=logits.device, dtype=logits.dtype)
    mask = pair_mask.to(device=logits.device, dtype=logits.dtype)
    return (raw * weights * mask).sum() / torch.clamp((weights * mask).sum(), min=1.0)


def _utility_distribution_loss(
    logits: torch.Tensor,
    rewards: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
    *,
    temperature: float,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    active_logits = logits.masked_fill(~active_mask, -1.0e9)
    log_probs = F.log_softmax(active_logits, dim=1)
    rewards = rewards.to(device=logits.device, dtype=logits.dtype)
    masked_rewards = rewards.masked_fill(~active_mask, -1.0e9)
    centered_rewards = masked_rewards - masked_rewards.max(dim=1, keepdim=True).values
    target_distribution = F.softmax(centered_rewards / max(float(temperature), 1.0e-6), dim=1)
    per_sample_loss = -(target_distribution * log_probs).sum(dim=1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _expected_rebuffer_penalty_loss(
    logits: torch.Tensor,
    rebuffer_penalties: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    active_logits = logits.masked_fill(~active_mask, -1.0e9)
    probabilities = F.softmax(active_logits, dim=1)
    penalties = rebuffer_penalties.to(device=logits.device, dtype=logits.dtype).masked_fill(~active_mask, 0.0)
    per_sample_loss = (probabilities * penalties).sum(dim=1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


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
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    targets = targets.to(device=logits.device, dtype=logits.dtype)
    raw = F.binary_cross_entropy_with_logits(logits, targets, reduction="none")
    valid_counts = torch.clamp(active_mask.sum(dim=1).to(dtype=logits.dtype), min=1.0)
    per_sample_loss = (raw * active_mask.to(dtype=logits.dtype)).sum(dim=1) / valid_counts
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _masked_weighted_kl_to_reference_loss(
    logits: torch.Tensor,
    ref_logits: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    masked_logits = logits.masked_fill(~active_mask, -1.0e9)
    masked_ref_logits = ref_logits.to(device=logits.device, dtype=logits.dtype).masked_fill(~active_mask, -1.0e9)
    log_probs = F.log_softmax(masked_logits, dim=1)
    ref_log_probs = F.log_softmax(masked_ref_logits, dim=1)
    probabilities = F.softmax(masked_logits, dim=1)
    per_sample_loss = (probabilities * (log_probs - ref_log_probs) * active_mask.to(dtype=logits.dtype)).sum(dim=1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _expected_over_aggressive_probability_loss(
    logits: torch.Tensor,
    over_aggressive_actions: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    over_mask = over_aggressive_actions.to(dtype=torch.bool, device=logits.device) & active_mask
    masked_logits = logits.masked_fill(~active_mask, -1.0e9)
    probabilities = F.softmax(masked_logits, dim=1)
    per_sample_loss = (probabilities * over_mask.to(dtype=logits.dtype)).sum(dim=1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _over_aggressive_margin_loss(
    logits: torch.Tensor,
    safe_labels: torch.Tensor,
    over_aggressive_actions: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
    *,
    margin: float,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    safe = safe_labels.to(device=logits.device, dtype=torch.long)
    masked_logits = logits.masked_fill(~active_mask, -1.0e9)
    safe_logits = torch.gather(masked_logits, 1, safe.unsqueeze(1))
    action_indices = torch.arange(logits.shape[1], device=logits.device).unsqueeze(0)
    over_mask = over_aggressive_actions.to(dtype=torch.bool, device=logits.device) & active_mask
    over_mask = over_mask & (action_indices != safe.unsqueeze(1))
    raw = F.softplus(float(margin) + masked_logits - safe_logits)
    over_counts = torch.clamp(over_mask.sum(dim=1).to(dtype=logits.dtype), min=1.0)
    per_sample_loss = (raw * over_mask.to(dtype=logits.dtype)).sum(dim=1) / over_counts
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _over_aggressive_reference_excess_loss(
    logits: torch.Tensor,
    ref_logits: torch.Tensor,
    over_aggressive_actions: torch.Tensor,
    mask: torch.Tensor,
    sample_weights: torch.Tensor,
) -> torch.Tensor:
    active_mask = mask.to(dtype=torch.bool, device=logits.device)
    over_mask = over_aggressive_actions.to(dtype=torch.bool, device=logits.device) & active_mask
    masked_logits = logits.masked_fill(~active_mask, -1.0e9)
    masked_ref_logits = ref_logits.to(device=logits.device, dtype=logits.dtype).masked_fill(~active_mask, -1.0e9)
    probabilities = F.softmax(masked_logits, dim=1)
    ref_probabilities = F.softmax(masked_ref_logits, dim=1)
    excess = F.relu(probabilities - ref_probabilities)
    per_sample_loss = (excess * over_mask.to(dtype=logits.dtype)).sum(dim=1)
    weights = sample_weights.to(device=logits.device, dtype=logits.dtype)
    return (per_sample_loss * weights).sum() / torch.clamp(weights.sum(), min=1.0)


def _policy_observations(
    outputs: Mapping[str, torch.Tensor],
    batch: Sequence[torch.Tensor],
) -> tuple[Mapping[str, object], ...]:
    logits = outputs["action_logits"]
    labels = batch[4]
    best_labels = batch[5]
    qoe_gaps = batch[6]
    rebuffer = batch[7]
    rewards = batch[8]
    bitrate = batch[9]
    smoothness = batch[10]
    target_risk = batch[11]
    mask = batch[3].to(dtype=torch.bool)
    pair_preferred = batch[13]
    pair_rejected = batch[14]
    pair_mask = batch[17].to(dtype=torch.bool)
    predictions = torch.argmax(logits, dim=1)
    k = min(2, int(logits.shape[1]))
    topk = torch.topk(logits, k=k, dim=1).indices
    observations = []
    labels_cpu = labels.detach().cpu().tolist()
    best_cpu = best_labels.detach().cpu().tolist()
    predictions_cpu = predictions.detach().cpu().tolist()
    topk_cpu = topk.detach().cpu().tolist()
    qoe_cpu = qoe_gaps.detach().cpu().tolist()
    rebuffer_cpu = rebuffer.detach().cpu().tolist()
    rewards_cpu = rewards.detach().cpu().tolist()
    bitrate_cpu = bitrate.detach().cpu().tolist()
    smoothness_cpu = smoothness.detach().cpu().tolist()
    risk_cpu = target_risk.detach().cpu().tolist()
    mask_cpu = mask.detach().cpu().tolist()
    logits_cpu = logits.detach().cpu()
    preferred_cpu = pair_preferred.detach().cpu().tolist()
    rejected_cpu = pair_rejected.detach().cpu().tolist()
    pair_mask_cpu = pair_mask.detach().cpu().tolist()
    for index, label in enumerate(labels_cpu):
        prediction = int(predictions_cpu[index])
        oracle_action = int(label)
        best_immediate_action = int(best_cpu[index])
        valid_prediction = bool(mask_cpu[index][prediction]) if prediction < len(mask_cpu[index]) else False
        pair_total = 0
        pair_correct = 0
        for pair_index, active in enumerate(pair_mask_cpu[index]):
            if not active:
                continue
            pair_total += 1
            pref = int(preferred_cpu[index][pair_index])
            rej = int(rejected_cpu[index][pair_index])
            if float(logits_cpu[index, pref]) >= float(logits_cpu[index, rej]):
                pair_correct += 1
        observations.append(
            {
                "oracle_action": oracle_action,
                "best_immediate_action": best_immediate_action,
                "predicted_action": prediction,
                "top2_hit": oracle_action in [int(value) for value in topk_cpu[index]],
                "valid_prediction": valid_prediction,
                "predicted_qoe_gap": float(qoe_cpu[index][prediction]),
                "predicted_rebuffer_s": float(rebuffer_cpu[index][prediction]),
                "predicted_reward_n": float(rewards_cpu[index][prediction]),
                "predicted_bitrate_kbps": float(bitrate_cpu[index][prediction]),
                "predicted_smoothness_mbps": float(smoothness_cpu[index][prediction]),
                "predicted_target_risk": float(risk_cpu[index][prediction]),
                "oracle_reward_n": float(rewards_cpu[index][oracle_action]),
                "oracle_rebuffer_s": float(rebuffer_cpu[index][oracle_action]),
                "oracle_bitrate_kbps": float(bitrate_cpu[index][oracle_action]),
                "oracle_smoothness_mbps": float(smoothness_cpu[index][oracle_action]),
                "oracle_target_risk": float(risk_cpu[index][oracle_action]),
                "best_immediate_reward_n": float(rewards_cpu[index][best_immediate_action]),
                "best_immediate_rebuffer_s": float(rebuffer_cpu[index][best_immediate_action]),
                "pair_total": pair_total,
                "pair_correct": pair_correct,
            }
        )
    return tuple(observations)


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
class _PolicyMetricTotals:
    weight: int = 0
    losses: dict[str, float] | None = None
    target_counts: Counter[str] | None = None
    predicted_counts: Counter[str] | None = None
    true_positive: Counter[str] | None = None
    false_positive: Counter[str] | None = None
    false_negative: Counter[str] | None = None
    top1_count: int = 0
    top2_count: int = 0
    best_immediate_count: int = 0
    over_count: int = 0
    under_count: int = 0
    invalid_count: int = 0
    action_delta_sum: float = 0.0
    qoe_gap_sum: float = 0.0
    rebuffer_sum: float = 0.0
    rebuffer_positive_count: int = 0
    reward_sum: float = 0.0
    oracle_reward_sum: float = 0.0
    bitrate_sum: float = 0.0
    oracle_bitrate_sum: float = 0.0
    smoothness_sum: float = 0.0
    oracle_smoothness_sum: float = 0.0
    target_risk_count: int = 0
    oracle_target_risk_count: int = 0
    utility_regret_vs_oracle_sum: float = 0.0
    utility_regret_vs_best_sum: float = 0.0
    rebuffer_regret_vs_oracle_sum: float = 0.0
    rebuffer_regret_vs_best_sum: float = 0.0
    pair_total: int = 0
    pair_correct: int = 0

    def __post_init__(self) -> None:
        self.losses = defaultdict(float)
        self.target_counts = Counter()
        self.predicted_counts = Counter()
        self.true_positive = Counter()
        self.false_positive = Counter()
        self.false_negative = Counter()

    def add_observations(
        self,
        observations: Sequence[Mapping[str, object]],
        losses: Mapping[str, object],
        batch_size: int,
    ) -> None:
        self.weight += int(batch_size)
        for name in _LOSS_METRIC_NAMES:
            if name in losses:
                value = losses[name]
                numeric = float(value.detach().cpu().item()) if hasattr(value, "detach") else float(value)
                self.losses[name] += numeric * float(batch_size)
        for observation in observations:
            oracle_action = int(observation["oracle_action"])
            predicted_action = int(observation["predicted_action"])
            oracle_key = str(oracle_action)
            predicted_key = str(predicted_action)
            self.target_counts[oracle_key] += 1
            self.predicted_counts[predicted_key] += 1
            if predicted_action == oracle_action:
                self.top1_count += 1
                self.true_positive[oracle_key] += 1
            else:
                self.false_positive[predicted_key] += 1
                self.false_negative[oracle_key] += 1
            if bool(observation["top2_hit"]):
                self.top2_count += 1
            if not bool(observation["valid_prediction"]):
                self.invalid_count += 1
            if predicted_action == int(observation["best_immediate_action"]):
                self.best_immediate_count += 1
            delta = predicted_action - oracle_action
            self.action_delta_sum += float(delta)
            if delta > 0:
                self.over_count += 1
            elif delta < 0:
                self.under_count += 1
            self.qoe_gap_sum += float(observation["predicted_qoe_gap"])
            predicted_rebuffer = float(observation["predicted_rebuffer_s"])
            self.rebuffer_sum += predicted_rebuffer
            if predicted_rebuffer > 0.0:
                self.rebuffer_positive_count += 1
            self.reward_sum += float(observation["predicted_reward_n"])
            self.oracle_reward_sum += float(observation["oracle_reward_n"])
            self.utility_regret_vs_oracle_sum += max(
                float(observation["oracle_reward_n"]) - float(observation["predicted_reward_n"]),
                0.0,
            )
            self.utility_regret_vs_best_sum += max(
                float(observation["best_immediate_reward_n"]) - float(observation["predicted_reward_n"]),
                0.0,
            )
            self.rebuffer_regret_vs_oracle_sum += max(
                predicted_rebuffer - float(observation["oracle_rebuffer_s"]),
                0.0,
            )
            self.rebuffer_regret_vs_best_sum += max(
                predicted_rebuffer - float(observation["best_immediate_rebuffer_s"]),
                0.0,
            )
            self.bitrate_sum += float(observation["predicted_bitrate_kbps"])
            self.oracle_bitrate_sum += float(observation["oracle_bitrate_kbps"])
            self.smoothness_sum += float(observation["predicted_smoothness_mbps"])
            self.oracle_smoothness_sum += float(observation["oracle_smoothness_mbps"])
            if float(observation["predicted_target_risk"]) >= 0.5:
                self.target_risk_count += 1
            if float(observation["oracle_target_risk"]) >= 0.5:
                self.oracle_target_risk_count += 1
            self.pair_total += int(observation["pair_total"])
            self.pair_correct += int(observation["pair_correct"])

    def to_json(self, *, include_losses: bool = True) -> dict[str, object]:
        denominator = max(float(self.weight), 1.0)
        class_keys = sorted(set(self.target_counts) | set(self.predicted_counts), key=lambda value: int(value))
        target_class_keys = sorted(self.target_counts, key=lambda value: int(value))
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
        payload: dict[str, object] = {}
        if include_losses:
            payload.update({name: round(value / denominator, 9) for name, value in sorted(self.losses.items())})
        payload.update(
            {
                "top1_accuracy": round(float(self.top1_count) / denominator, 6),
                "top2_accuracy": round(float(self.top2_count) / denominator, 6),
                "best_immediate_accuracy": round(float(self.best_immediate_count) / denominator, 6),
                "balanced_accuracy": round(sum(recalls) / float(len(recalls) or 1), 6),
                "macro_f1": round(sum(f1_values) / float(len(f1_values) or 1), 6),
                "mean_action_delta_vs_oracle": round(self.action_delta_sum / denominator, 6),
                "over_aggressive_rate_vs_oracle": round(float(self.over_count) / denominator, 6),
                "under_aggressive_rate_vs_oracle": round(float(self.under_count) / denominator, 6),
                "invalid_action_rate": round(float(self.invalid_count) / denominator, 6),
                "predicted_qoe_gap_mean": round(self.qoe_gap_sum / denominator, 6),
                "predicted_rebuffer_s_mean": round(self.rebuffer_sum / denominator, 6),
                "predicted_rebuffer_rate": round(float(self.rebuffer_positive_count) / denominator, 6),
                "predicted_reward_n_mean": round(self.reward_sum / denominator, 6),
                "oracle_reward_n_mean": round(self.oracle_reward_sum / denominator, 6),
                "selected_utility_regret_vs_oracle_mean": round(self.utility_regret_vs_oracle_sum / denominator, 6),
                "selected_utility_regret_vs_best_immediate_mean": round(self.utility_regret_vs_best_sum / denominator, 6),
                "selected_rebuffer_regret_vs_oracle_mean": round(self.rebuffer_regret_vs_oracle_sum / denominator, 6),
                "selected_rebuffer_regret_vs_best_immediate_mean": round(self.rebuffer_regret_vs_best_sum / denominator, 6),
                "predicted_bitrate_kbps_mean": round(self.bitrate_sum / denominator, 6),
                "oracle_bitrate_kbps_mean": round(self.oracle_bitrate_sum / denominator, 6),
                "predicted_smoothness_mbps_mean": round(self.smoothness_sum / denominator, 6),
                "oracle_smoothness_mbps_mean": round(self.oracle_smoothness_sum / denominator, 6),
                "predicted_target_risk_rate": round(float(self.target_risk_count) / denominator, 6),
                "oracle_target_risk_rate": round(float(self.oracle_target_risk_count) / denominator, 6),
                "pair_preference_accuracy": round(float(self.pair_correct) / max(float(self.pair_total), 1.0), 6),
                "pair_count": int(self.pair_total),
                "oracle_action_distribution": {key: int(self.target_counts.get(key, 0)) for key in target_class_keys},
                "predicted_action_distribution": {key: int(self.predicted_counts.get(key, 0)) for key in class_keys},
                "sample_count": int(self.weight),
            }
        )
        return payload


def _example_from_sample(
    sample: Mapping[str, object],
    expected_role: str,
    line_number: int,
    *,
    max_pair_weight: float,
    focus_bucket_sample_weight: float,
    severe_error_sample_weight: float,
    safe_vs_rebuffer_pair_weight: float,
    over_aggressive_rebuffer_action_weight: float,
    rebuffer_loss_cap_s: float,
) -> SpbcV2DpoExample:
    if sample.get("data_role") != expected_role:
        raise SpbcV2DpoTrainingError("line {0}: data_role mismatch".format(line_number))
    model_inputs = _require_mapping(sample.get("model_inputs"), "model_inputs")
    _reject_unexpected_keys(model_inputs, MODEL_INPUT_KEYS, "model_inputs", line_number)
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    _reject_unexpected_keys(context, CONTEXT_INPUT_KEYS, "model_inputs.context", line_number)
    candidates_raw = model_inputs.get("candidates")
    action_mask_raw = model_inputs.get("action_mask")
    if not isinstance(candidates_raw, list) or not isinstance(action_mask_raw, list):
        raise SpbcV2DpoTrainingError("line {0}: candidates/action_mask must be lists".format(line_number))
    sequence = _sequence_from_context(context)
    scalars = tuple(_finite_number(context.get(name), name) for name in SCALAR_FEATURES)
    candidate_rows = []
    for candidate_index, candidate in enumerate(candidates_raw):
        candidate_mapping = _require_mapping(candidate, "candidate")
        _reject_unexpected_keys(candidate_mapping, CANDIDATE_INPUT_KEYS, "candidate[{0}]".format(candidate_index), line_number)
        candidate_rows.append(tuple(_finite_number(candidate_mapping.get(name), name) for name in CANDIDATE_FEATURES))
    candidates = tuple(candidate_rows)
    action_mask = tuple(bool(value) for value in action_mask_raw)
    oracle_action = _integer(sample.get("oracle_action"), "oracle_action")
    best_immediate_action = _integer(sample.get("best_immediate_action"), "best_immediate_action")
    outcomes_raw = sample.get("per_action_outcomes")
    if not isinstance(outcomes_raw, list) or len(outcomes_raw) != len(candidates):
        raise SpbcV2DpoTrainingError("line {0}: per_action_outcomes length mismatch".format(line_number))
    qoe_gaps = []
    rebuffer = []
    rewards = []
    bitrates = []
    smoothness = []
    target_risks = []
    rebuffer_penalties = []
    over_aggressive_actions = []
    has_severe_rebuffer_error = False
    for index, raw_outcome in enumerate(outcomes_raw):
        outcome = _require_mapping(raw_outcome, "per_action_outcomes[{0}]".format(index))
        bitrate_kbps = max(_finite_number(outcome.get("bitrate_kbps"), "bitrate_kbps"), 0.0)
        smoothness_mbps = max(_finite_number(outcome.get("smoothness_mbps"), "smoothness_mbps"), 0.0)
        bitrates.append(bitrate_kbps)
        smoothness.append(smoothness_mbps)
        over_aggressive_rebuffer = outcome.get("over_aggressive_rebuffer") is True
        over_aggressive_actions.append(over_aggressive_rebuffer)
        if outcome.get("valid_action") is True:
            qoe_gap = max(_finite_number(outcome.get("qoe_gap"), "qoe_gap"), 0.0)
            rebuffer_s = max(_finite_number(outcome.get("estimated_rebuffer_s"), "estimated_rebuffer_s"), 0.0)
            qoe_gaps.append(qoe_gap)
            rebuffer.append(rebuffer_s)
            rewards.append(_finite_number(outcome.get("reward_n"), "reward_n"))
            penalty = min(rebuffer_s, float(rebuffer_loss_cap_s)) / max(float(rebuffer_loss_cap_s), 1.0e-6)
            if over_aggressive_rebuffer:
                penalty *= max(float(over_aggressive_rebuffer_action_weight), 1.0)
                has_severe_rebuffer_error = True
            rebuffer_penalties.append(min(max(penalty, 0.0), max(float(max_pair_weight), 1.0)))
            target_risks.append(
                1.0
                if (
                    rebuffer_s > 0.0
                    or qoe_gap > TARGET_RISK_QOE_GAP_THRESHOLD
                    or over_aggressive_rebuffer
                    or outcome.get("under_aggressive_qoe_loss") is True
                )
                else 0.0
            )
        else:
            qoe_gaps.append(0.0)
            rebuffer.append(0.0)
            rewards.append(0.0)
            target_risks.append(1.0)
            rebuffer_penalties.append(1.0)
    pairs_raw = sample.get("preference_pairs")
    if not isinstance(pairs_raw, list) or not pairs_raw:
        raise SpbcV2DpoTrainingError("line {0}: preference_pairs must be non-empty".format(line_number))
    pairs = _normalized_preference_pairs(
        tuple(
            _preference_pair(
                pair,
                max_pair_weight=max_pair_weight,
                safe_vs_rebuffer_pair_weight=safe_vs_rebuffer_pair_weight,
            )
            for pair in pairs_raw
        ),
        max_pair_weight=max_pair_weight,
    )
    if (
        len(candidates) != len(action_mask)
        or len(candidates) != len(qoe_gaps)
        or len(candidates) != len(bitrates)
        or len(candidates) != len(smoothness)
        or len(candidates) != len(target_risks)
        or len(candidates) != len(rebuffer_penalties)
        or len(candidates) != len(over_aggressive_actions)
    ):
        raise SpbcV2DpoTrainingError("line {0}: candidates/mask/targets length mismatch".format(line_number))
    if int(oracle_action) < 0 or int(oracle_action) >= len(candidates) or not action_mask[int(oracle_action)]:
        raise SpbcV2DpoTrainingError("line {0}: oracle_action invalid".format(line_number))
    if int(best_immediate_action) < 0 or int(best_immediate_action) >= len(candidates) or not action_mask[int(best_immediate_action)]:
        raise SpbcV2DpoTrainingError("line {0}: best_immediate_action invalid".format(line_number))
    metadata = _require_mapping(sample.get("metadata"), "metadata")
    throughput_bucket = str(metadata.get("throughput_bucket", "unknown"))
    bucket_weight = float(focus_bucket_sample_weight) if throughput_bucket == FOCUS_THROUGHPUT_BUCKET else 1.0
    severe_weight = float(severe_error_sample_weight) if has_severe_rebuffer_error else 1.0
    sample_weight = min(max((1.0 + max(pair.qoe_gap for pair in pairs)) * bucket_weight * severe_weight, 1.0), float(max_pair_weight))
    return SpbcV2DpoExample(
        sequence=sequence,
        scalars=scalars,
        candidates=candidates,
        action_mask=action_mask,
        oracle_action=int(oracle_action),
        best_immediate_action=int(best_immediate_action),
        qoe_gap_by_action=tuple(qoe_gaps),
        rebuffer_s_by_action=tuple(rebuffer),
        reward_by_action=tuple(rewards),
        bitrate_kbps_by_action=tuple(bitrates),
        smoothness_mbps_by_action=tuple(smoothness),
        target_risk_by_action=tuple(target_risks),
        rebuffer_penalty_by_action=tuple(rebuffer_penalties),
        over_aggressive_action_by_action=tuple(over_aggressive_actions),
        pairs=pairs,
        sample_weight=sample_weight,
        max_pair_weight=float(max_pair_weight),
        data_role=expected_role,
        rollout_source=str(sample.get("rollout_source", "unknown")),
        throughput_bucket=throughput_bucket,
        synthetic=bool(metadata.get("synthetic") is True),
    )


def _preference_pair(
    raw: object,
    *,
    max_pair_weight: float,
    safe_vs_rebuffer_pair_weight: float = 1.25,
) -> PreferencePair:
    pair = _require_mapping(raw, "preference_pair")
    source = str(pair.get("preference_source", "unknown"))
    reward_gap = max(_finite_number(pair.get("reward_gap"), "reward_gap"), 0.0)
    qoe_gap = max(_finite_number(pair.get("qoe_gap"), "qoe_gap"), 0.0)
    source_weight = float(PAIR_SOURCE_WEIGHTS.get(source, 1.0))
    if source == "safe_vs_rebuffer":
        source_weight *= float(safe_vs_rebuffer_pair_weight)
    gap_weight = 1.0 + min(max(qoe_gap, reward_gap), float(max_pair_weight))
    weight = min(max(source_weight * gap_weight, 0.05), float(max_pair_weight))
    return PreferencePair(
        preferred_action=_integer(pair.get("preferred_action"), "preferred_action"),
        rejected_action=_integer(pair.get("rejected_action"), "rejected_action"),
        reward_gap=reward_gap,
        qoe_gap=qoe_gap,
        source=source,
        weight=weight,
    )


def _normalized_preference_pairs(
    pairs: Sequence[PreferencePair],
    *,
    max_pair_weight: float,
) -> tuple[PreferencePair, ...]:
    if not pairs:
        raise SpbcV2DpoTrainingError("preference pairs must not be empty")
    mean_weight = sum(float(pair.weight) for pair in pairs) / float(len(pairs))
    scale = 1.0 / max(mean_weight, 1.0e-12)
    normalized = []
    for pair in pairs:
        weight = min(max(float(pair.weight) * scale, 0.05), float(max_pair_weight))
        normalized.append(
            PreferencePair(
                preferred_action=pair.preferred_action,
                rejected_action=pair.rejected_action,
                reward_gap=pair.reward_gap,
                qoe_gap=pair.qoe_gap,
                source=pair.source,
                weight=weight,
            )
        )
    return tuple(normalized)


def _load_initial_checkpoint(
    path: object | None,
    profile: SpbcV2DpoTrainingProfile,
    allow_random_init_full: bool,
) -> Mapping[str, object] | None:
    if path is None:
        if profile.name == "full_v1" and not allow_random_init_full:
            raise SpbcV2DpoTrainingError("full_v1 requires --init-checkpoint or --allow-random-init-full")
        return None
    checkpoint_path = Path(path).expanduser()
    if not checkpoint_path.is_file():
        if profile.name == "full_v1" and not allow_random_init_full:
            raise SpbcV2DpoTrainingError("full_v1 requires an existing init checkpoint: {0}".format(checkpoint_path))
        return None
    try:
        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    except TypeError:
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
    if not isinstance(checkpoint, Mapping):
        raise SpbcV2DpoTrainingError("init checkpoint must contain a mapping: {0}".format(checkpoint_path))
    if checkpoint.get("schema_id") not in {SPBC_CHECKPOINT_SCHEMA_ID, SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID}:
        raise SpbcV2DpoTrainingError("unsupported init checkpoint schema_id: {0}".format(checkpoint_path))
    if checkpoint.get("model_key") not in {"spbc_abr_v1", SPBC_V2_DPO_MODEL_KEY}:
        raise SpbcV2DpoTrainingError("unsupported init checkpoint model_key: {0}".format(checkpoint_path))
    config = _require_mapping(checkpoint.get("model_config"), "init model_config")
    state_dict = checkpoint.get("model_state_dict")
    if not isinstance(state_dict, Mapping):
        raise SpbcV2DpoTrainingError("init checkpoint missing model_state_dict")
    normalization = _require_mapping(checkpoint.get("normalization"), "init normalization")
    return {
        "path": str(checkpoint_path),
        "sha256": _sha256_file(checkpoint_path),
        "config": config,
        "state_dict": state_dict,
        "normalization": normalization,
        "schema_id": checkpoint.get("schema_id"),
        "model_key": checkpoint.get("model_key"),
    }


def _normalization_from_init_checkpoint(
    init_payload: Mapping[str, object] | None,
) -> SpbcV2DpoNormalizationStats | None:
    if init_payload is None:
        return None
    normalization = _require_mapping(init_payload.get("normalization"), "init normalization")
    return SpbcV2DpoNormalizationStats(
        schema_id="phase45_v2_spbc_dpo_normalization_v1",
        fitted_on_data_role=TRAINING_ROLE,
        source="reference_checkpoint_train_only",
        source_checkpoint=str(init_payload.get("path")),
        sequence_mean=_tuple_of_floats(normalization.get("sequence_mean"), len(SEQUENCE_FEATURES), "sequence_mean"),
        sequence_std=_tuple_of_floats(normalization.get("sequence_std"), len(SEQUENCE_FEATURES), "sequence_std"),
        scalar_mean=_tuple_of_floats(normalization.get("scalar_mean"), len(SCALAR_FEATURES), "scalar_mean"),
        scalar_std=_tuple_of_floats(normalization.get("scalar_std"), len(SCALAR_FEATURES), "scalar_std"),
        candidate_mean=_tuple_of_floats(normalization.get("candidate_mean"), len(CANDIDATE_FEATURES), "candidate_mean"),
        candidate_std=_tuple_of_floats(normalization.get("candidate_std"), len(CANDIDATE_FEATURES), "candidate_std"),
        sample_count=int(normalization.get("sample_count", 0) or 0),
        candidate_row_count=int(normalization.get("candidate_row_count", 0) or 0),
    )


def _load_initial_state_dict(
    model: SpbcAbrV2DpoPolicy,
    init_payload: Mapping[str, object],
) -> Mapping[str, object]:
    result = model.load_state_dict(init_payload["state_dict"], strict=False)
    missing_keys = list(result.missing_keys)
    unexpected_keys = list(result.unexpected_keys)
    allowed_missing_prefixes = ("reward_head.", "rebuffer_head.", "risk_head.")
    disallowed_missing = [
        key
        for key in missing_keys
        if not any(str(key).startswith(prefix) for prefix in allowed_missing_prefixes)
    ]
    if disallowed_missing or unexpected_keys:
        raise SpbcV2DpoTrainingError(
            "init checkpoint incompatible with spbc_abr_v2_dpo: missing={0} unexpected={1}".format(
                disallowed_missing,
                unexpected_keys,
            )
        )
    return {
        "loaded": True,
        "missing_keys": missing_keys,
        "unexpected_keys": unexpected_keys,
        "auxiliary_heads_initialized_from_zero": bool(missing_keys),
    }


def _build_model_from_profile_or_checkpoint(
    profile: SpbcV2DpoTrainingProfile,
    init_payload: Mapping[str, object] | None,
) -> SpbcAbrV2DpoPolicy:
    if init_payload is not None:
        config = _require_mapping(init_payload["config"], "init model_config")
        return SpbcAbrV2DpoPolicy(
            history_hidden_size=int(config["history_hidden_size"]),
            state_hidden_size=int(config["state_hidden_size"]),
            candidate_hidden_size=int(config["candidate_hidden_size"]),
            shared_hidden_size=int(config["shared_hidden_size"]),
            dropout=float(config["dropout"]),
            decision_reward_fusion_weight=profile.decision_reward_fusion_weight,
            decision_rebuffer_fusion_weight=profile.decision_rebuffer_fusion_weight,
            decision_risk_fusion_weight=profile.decision_risk_fusion_weight,
            rebuffer_prediction_cap_s=profile.rebuffer_loss_cap_s,
        )
    return SpbcAbrV2DpoPolicy(
        history_hidden_size=profile.history_hidden_size,
        state_hidden_size=profile.state_hidden_size,
        candidate_hidden_size=profile.candidate_hidden_size,
        shared_hidden_size=profile.shared_hidden_size,
        dropout=profile.dropout,
        decision_reward_fusion_weight=profile.decision_reward_fusion_weight,
        decision_rebuffer_fusion_weight=profile.decision_rebuffer_fusion_weight,
        decision_risk_fusion_weight=profile.decision_risk_fusion_weight,
        rebuffer_prediction_cap_s=profile.rebuffer_loss_cap_s,
    )


def _clone_reference_model(model: SpbcAbrV2DpoPolicy, device: torch.device) -> SpbcAbrV2DpoPolicy:
    reference = SpbcAbrV2DpoPolicy(
        history_hidden_size=model.history_hidden_size,
        state_hidden_size=model.state_hidden_size,
        candidate_hidden_size=model.candidate_hidden_size,
        shared_hidden_size=model.shared_hidden_size,
        dropout=model.dropout,
        decision_reward_fusion_weight=model.decision_reward_fusion_weight,
        decision_rebuffer_fusion_weight=model.decision_rebuffer_fusion_weight,
        decision_risk_fusion_weight=model.decision_risk_fusion_weight,
        rebuffer_prediction_cap_s=model.rebuffer_prediction_cap_s,
    )
    reference.load_state_dict({key: value.detach().cpu().clone() for key, value in model.state_dict().items()})
    reference.to(device)
    reference.eval()
    for parameter in reference.parameters():
        parameter.requires_grad_(False)
    return reference


def _reference_policy_source(init_payload: Mapping[str, object] | None) -> str:
    if init_payload is None:
        return "random_initial_policy_smoke_or_pilot_only"
    if init_payload.get("model_key") == "spbc_abr_v1":
        return "spbc_abr_v1_full_v1_frozen_checkpoint"
    if init_payload.get("model_key") == SPBC_V2_DPO_MODEL_KEY:
        return "spbc_abr_v2_dpo_frozen_initial_checkpoint"
    return "unsupported_frozen_initial_checkpoint"


_CRITICAL_METRIC_KEYS = (
    "top1_accuracy",
    "balanced_accuracy",
    "selected_utility_regret_vs_oracle_mean",
    "selected_rebuffer_regret_vs_oracle_mean",
    "over_aggressive_rate_vs_oracle",
    "under_aggressive_rate_vs_oracle",
    "predicted_bitrate_kbps_mean",
    "predicted_rebuffer_rate",
)


def _critical_metric_summary(metrics: Mapping[str, object]) -> Mapping[str, object]:
    focus_metrics = _nested_mapping(metrics, "focus_2_5_mbps")
    source_metrics = _nested_mapping(_nested_mapping(metrics, "by_rollout_source"), SAFETY_ROLLOUT_SOURCE)
    return {
        "global": _critical_scope_summary(metrics, present=True),
        FOCUS_THROUGHPUT_BUCKET: _critical_scope_summary(
            focus_metrics,
            present=bool(focus_metrics.get("bucket_present", bool(focus_metrics))),
        ),
        SAFETY_ROLLOUT_SOURCE: _critical_scope_summary(source_metrics, present=bool(source_metrics)),
    }


def _critical_scope_summary(metrics: Mapping[str, object], *, present: bool) -> Mapping[str, object]:
    payload: dict[str, object] = {
        "present": bool(present),
        "sample_count": int(_metric_float(metrics, "sample_count")),
    }
    for key in _CRITICAL_METRIC_KEYS:
        payload[key] = _metric_float(metrics, key)
    return payload


def _critical_metric_delta(
    metrics: Mapping[str, object],
    reference_metrics: Mapping[str, object] | None,
) -> Mapping[str, object]:
    if reference_metrics is None:
        return {
            "available": False,
            "reason": "reference_validation_metrics_not_available",
        }
    candidate = _critical_metric_summary(metrics)
    reference = _critical_metric_summary(reference_metrics)
    deltas: dict[str, object] = {"available": True}
    for scope in ("global", FOCUS_THROUGHPUT_BUCKET, SAFETY_ROLLOUT_SOURCE):
        candidate_scope = _nested_mapping(candidate, scope)
        reference_scope = _nested_mapping(reference, scope)
        deltas[scope] = {
            key: round(_metric_float(candidate_scope, key) - _metric_float(reference_scope, key), 6)
            for key in _CRITICAL_METRIC_KEYS
        }
    return deltas


def _flatten_epoch_critical_metrics(summary: Mapping[str, object]) -> Mapping[str, object]:
    global_metrics = _nested_mapping(summary, "global")
    focus_metrics = _nested_mapping(summary, FOCUS_THROUGHPUT_BUCKET)
    source_metrics = _nested_mapping(summary, SAFETY_ROLLOUT_SOURCE)
    return {
        "validation_over_aggressive_rate_vs_oracle": global_metrics["over_aggressive_rate_vs_oracle"],
        "validation_under_aggressive_rate_vs_oracle": global_metrics["under_aggressive_rate_vs_oracle"],
        "validation_selected_utility_regret_vs_oracle_mean": global_metrics[
            "selected_utility_regret_vs_oracle_mean"
        ],
        "validation_selected_rebuffer_regret_vs_oracle_mean": global_metrics[
            "selected_rebuffer_regret_vs_oracle_mean"
        ],
        "validation_focus_2_5_mbps_over_aggressive_rate_vs_oracle": focus_metrics[
            "over_aggressive_rate_vs_oracle"
        ],
        "validation_focus_2_5_mbps_under_aggressive_rate_vs_oracle": focus_metrics[
            "under_aggressive_rate_vs_oracle"
        ],
        "validation_focus_2_5_mbps_selected_utility_regret_vs_oracle_mean": focus_metrics[
            "selected_utility_regret_vs_oracle_mean"
        ],
        "validation_focus_2_5_mbps_selected_rebuffer_regret_vs_oracle_mean": focus_metrics[
            "selected_rebuffer_regret_vs_oracle_mean"
        ],
        "validation_spbc_v2_dpo_on_policy_over_aggressive_rate_vs_oracle": source_metrics[
            "over_aggressive_rate_vs_oracle"
        ],
        "validation_spbc_v2_dpo_on_policy_under_aggressive_rate_vs_oracle": source_metrics[
            "under_aggressive_rate_vs_oracle"
        ],
        "validation_spbc_v2_dpo_on_policy_selected_utility_regret_vs_oracle_mean": source_metrics[
            "selected_utility_regret_vs_oracle_mean"
        ],
        "validation_spbc_v2_dpo_on_policy_selected_rebuffer_regret_vs_oracle_mean": source_metrics[
            "selected_rebuffer_regret_vs_oracle_mean"
        ],
    }


def _safety_gate_result(
    metrics: Mapping[str, object],
    reference_metrics: Mapping[str, object] | None,
    profile: SpbcV2DpoTrainingProfile,
) -> Mapping[str, object]:
    if not profile.safety_gate_enabled:
        return {
            "enabled": False,
            "passed": True,
            "mode": "disabled",
            "checks": [],
            "failed_checks": [],
        }
    if reference_metrics is None:
        return {
            "enabled": True,
            "passed": False,
            "mode": "relative_to_initial_checkpoint",
            "reason": "reference_validation_metrics_not_available",
            "checks": [],
            "failed_checks": ["reference_validation_metrics_not_available"],
        }
    candidate = _critical_metric_summary(metrics)
    reference = _critical_metric_summary(reference_metrics)
    checks = []
    checks.extend(
        (
            _upper_bound_gate_check(
                "global_over_aggressive",
                _nested_mapping(candidate, "global"),
                _nested_mapping(reference, "global"),
                "over_aggressive_rate_vs_oracle",
                profile.safety_global_over_aggressive_tolerance,
            ),
            _upper_bound_gate_check(
                "focus_2_5_mbps_over_aggressive",
                _nested_mapping(candidate, FOCUS_THROUGHPUT_BUCKET),
                _nested_mapping(reference, FOCUS_THROUGHPUT_BUCKET),
                "over_aggressive_rate_vs_oracle",
                profile.safety_focus_over_aggressive_tolerance,
            ),
            _upper_bound_gate_check(
                "spbc_v2_dpo_on_policy_over_aggressive",
                _nested_mapping(candidate, SAFETY_ROLLOUT_SOURCE),
                _nested_mapping(reference, SAFETY_ROLLOUT_SOURCE),
                "over_aggressive_rate_vs_oracle",
                profile.safety_spbc_v2_over_aggressive_tolerance,
                required=False,
            ),
        )
    )
    for scope in ("global", FOCUS_THROUGHPUT_BUCKET, SAFETY_ROLLOUT_SOURCE):
        required_scope = scope != SAFETY_ROLLOUT_SOURCE
        checks.append(
            _upper_bound_gate_check(
                "{0}_utility_regret_non_regression".format(scope),
                _nested_mapping(candidate, scope),
                _nested_mapping(reference, scope),
                "selected_utility_regret_vs_oracle_mean",
                profile.safety_utility_regret_tolerance,
                required=required_scope,
            )
        )
        checks.append(
            _upper_bound_gate_check(
                "{0}_rebuffer_regret_non_regression".format(scope),
                _nested_mapping(candidate, scope),
                _nested_mapping(reference, scope),
                "selected_rebuffer_regret_vs_oracle_mean",
                profile.safety_rebuffer_regret_tolerance,
                required=required_scope,
            )
        )
    failed = [str(check["id"]) for check in checks if check["passed"] is not True]
    return {
        "enabled": True,
        "passed": not failed,
        "mode": "relative_to_initial_checkpoint",
        "reference_scopes": reference,
        "candidate_scopes": candidate,
        "checks": checks,
        "failed_checks": failed,
    }


def _safety_gate_tolerances(profile: SpbcV2DpoTrainingProfile) -> Mapping[str, object]:
    return {
        "enabled": bool(profile.safety_gate_enabled),
        "global_over_aggressive_tolerance": profile.safety_global_over_aggressive_tolerance,
        "focus_2_5_mbps_over_aggressive_tolerance": profile.safety_focus_over_aggressive_tolerance,
        "spbc_v2_dpo_on_policy_over_aggressive_tolerance": profile.safety_spbc_v2_over_aggressive_tolerance,
        "utility_regret_tolerance": profile.safety_utility_regret_tolerance,
        "rebuffer_regret_tolerance": profile.safety_rebuffer_regret_tolerance,
        "fallback_epoch_when_no_trained_epoch_passes": 0,
    }


def _upper_bound_gate_check(
    check_id: str,
    candidate_scope: Mapping[str, object],
    reference_scope: Mapping[str, object],
    metric_name: str,
    tolerance: float,
    *,
    required: bool = True,
) -> Mapping[str, object]:
    candidate_present = bool(candidate_scope.get("present", True))
    reference_present = bool(reference_scope.get("present", True))
    candidate_value = _metric_float(candidate_scope, metric_name)
    reference_value = _metric_float(reference_scope, metric_name)
    max_allowed = reference_value + max(float(tolerance), 0.0)
    if not candidate_present or not reference_present:
        return {
            "id": check_id,
            "metric": metric_name,
            "candidate": round(candidate_value, 6),
            "reference": round(reference_value, 6),
            "tolerance": round(max(float(tolerance), 0.0), 6),
            "max_allowed": round(max_allowed, 6),
            "delta_candidate_minus_reference": round(candidate_value - reference_value, 6),
            "passed": not required,
            "skipped": not required,
            "reason": "scope_not_present",
        }
    passed = candidate_present and reference_present and candidate_value <= max_allowed + 1.0e-12
    return {
        "id": check_id,
        "metric": metric_name,
        "candidate": round(candidate_value, 6),
        "reference": round(reference_value, 6),
        "tolerance": round(max(float(tolerance), 0.0), 6),
        "max_allowed": round(max_allowed, 6),
        "delta_candidate_minus_reference": round(candidate_value - reference_value, 6),
        "passed": bool(passed),
    }


def _selection_score(metrics: Mapping[str, object], profile: SpbcV2DpoTrainingProfile) -> float:
    global_score = _selection_component(metrics, profile)
    focus_raw = metrics.get("focus_2_5_mbps", {})
    focus_score = 0.0
    if isinstance(focus_raw, Mapping) and focus_raw.get("bucket_present") is True:
        focus_score = _selection_component(focus_raw, profile)
    return round(float(global_score + float(profile.selection_focus_weight) * focus_score), 9)


def _selection_component(metrics: Mapping[str, object], profile: SpbcV2DpoTrainingProfile) -> float:
    utility_regret = _metric_float(metrics, "selected_utility_regret_vs_best_immediate_mean")
    rebuffer_regret = _metric_float(metrics, "selected_rebuffer_regret_vs_best_immediate_mean")
    over_aggressive = _metric_float(metrics, "over_aggressive_rate_vs_oracle")
    invalid = _metric_float(metrics, "invalid_action_rate")
    return (
        utility_regret
        + float(profile.selection_rebuffer_weight) * rebuffer_regret
        + float(profile.selection_over_aggressive_weight) * over_aggressive
        + float(profile.selection_invalid_weight) * invalid
    )


def _metric_float(metrics: Mapping[str, object], key: str) -> float:
    value = metrics.get(key, 0.0)
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        numeric = 0.0
    if not math.isfinite(numeric):
        return 0.0
    return numeric


def _build_reference_comparison(
    *,
    training_metrics: Mapping[str, object],
    validation_metrics: Mapping[str, object],
    reference_training_metrics: Mapping[str, object] | None,
    reference_validation_metrics: Mapping[str, object] | None,
) -> Mapping[str, object]:
    comparison = dict(
        _build_checkpoint_reference_comparison(
            training_metrics=training_metrics,
            validation_metrics=validation_metrics,
            reference_training_metrics=reference_training_metrics,
            reference_validation_metrics=reference_validation_metrics,
            reference_label="spbc_abr_v1_full_v1_frozen_checkpoint",
            unavailable_reason="spbc_abr_v1 checkpoint not available",
        )
    )
    if comparison.get("available"):
        metrics = comparison["metrics_compared"]
        comparison.update(
            {
                "training_delta_candidate_minus_spbc_v1": _metric_deltas(
                    training_metrics, reference_training_metrics or {}, metrics
                ),
                "validation_delta_candidate_minus_spbc_v1": _metric_deltas(
                    validation_metrics, reference_validation_metrics or {}, metrics
                ),
                "validation_focus_2_5_mbps_delta_candidate_minus_spbc_v1": _metric_deltas(
                    _nested_mapping(validation_metrics, "focus_2_5_mbps"),
                    _nested_mapping(reference_validation_metrics or {}, "focus_2_5_mbps"),
                    metrics,
                ),
                "spbc_v1_training_metrics": reference_training_metrics,
                "spbc_v1_validation_metrics": reference_validation_metrics,
            }
        )
    return comparison


def _build_checkpoint_reference_comparison(
    *,
    training_metrics: Mapping[str, object],
    validation_metrics: Mapping[str, object],
    reference_training_metrics: Mapping[str, object] | None,
    reference_validation_metrics: Mapping[str, object] | None,
    reference_label: str,
    unavailable_reason: str,
) -> Mapping[str, object]:
    if reference_training_metrics is None or reference_validation_metrics is None:
        return {
            "available": False,
            "reason": unavailable_reason,
            "reference_label": reference_label,
            "comparison_type": "offline_training_audit_not_benchmark",
            "benchmark_performed": False,
            "ranking_performed": False,
        }
    metrics = (
        "top1_accuracy",
        "top2_accuracy",
        "balanced_accuracy",
        "macro_f1",
        "predicted_reward_n_mean",
        "selected_utility_regret_vs_oracle_mean",
        "selected_utility_regret_vs_best_immediate_mean",
        "selected_rebuffer_regret_vs_oracle_mean",
        "selected_rebuffer_regret_vs_best_immediate_mean",
        "predicted_rebuffer_s_mean",
        "predicted_rebuffer_rate",
        "predicted_target_risk_rate",
        "predicted_bitrate_kbps_mean",
        "predicted_smoothness_mbps_mean",
        "over_aggressive_rate_vs_oracle",
        "under_aggressive_rate_vs_oracle",
        "invalid_action_rate",
    )
    return {
        "available": True,
        "reference_label": reference_label,
        "comparison_type": "offline_training_audit_not_benchmark",
        "benchmark_performed": False,
        "ranking_performed": False,
        "metrics_compared": list(metrics),
        "training_delta_candidate_minus_reference": _metric_deltas(training_metrics, reference_training_metrics, metrics),
        "validation_delta_candidate_minus_reference": _metric_deltas(validation_metrics, reference_validation_metrics, metrics),
        "validation_focus_2_5_mbps_delta_candidate_minus_reference": _metric_deltas(
            _nested_mapping(validation_metrics, "focus_2_5_mbps"),
            _nested_mapping(reference_validation_metrics, "focus_2_5_mbps"),
            metrics,
        ),
        "reference_training_metrics": reference_training_metrics,
        "reference_validation_metrics": reference_validation_metrics,
    }


def _metric_deltas(
    candidate: Mapping[str, object],
    reference: Mapping[str, object],
    metric_names: Sequence[str],
) -> Mapping[str, float]:
    deltas: dict[str, float] = {}
    for name in metric_names:
        if name not in candidate or name not in reference:
            continue
        try:
            deltas[name] = round(float(candidate[name]) - float(reference[name]), 6)
        except (TypeError, ValueError):
            continue
    return deltas


def _nested_mapping(mapping: Mapping[str, object], key: str) -> Mapping[str, object]:
    value = mapping.get(key)
    return value if isinstance(value, Mapping) else {}


def _sequence_from_context(context: Mapping[str, object]) -> tuple[tuple[float, float], ...]:
    throughput = _numeric_sequence(context.get("throughput_history_bps"), "throughput_history_bps")
    download = _numeric_sequence(context.get("download_time_history_s"), "download_time_history_s")
    if len(throughput) != len(download):
        raise SpbcV2DpoTrainingError("history feature lengths differ")
    return tuple((throughput[index], download[index]) for index in range(len(throughput)))


def _numeric_sequence(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise SpbcV2DpoTrainingError("{0} must be a sequence".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> list[float]:
    if len(values) != len(mean) or len(mean) != len(std):
        raise SpbcV2DpoTrainingError("normalization vector width mismatch")
    return [(float(value) - float(mean[index])) / max(float(std[index]), 1.0e-12) for index, value in enumerate(values)]


def _normalize_matrix(
    values: Sequence[Sequence[float]],
    mean: Sequence[float],
    std: Sequence[float],
) -> list[list[float]]:
    return [_normalize_vector(row, mean, std) for row in values]


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
        raise SpbcV2DpoTrainingError("normalization rows must not be empty")
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise SpbcV2DpoTrainingError("normalization row width changed")
    return width


def _validate_training_args(
    epochs: int,
    batch_size: int,
    learning_rate: float,
    max_training_samples: int | None,
    max_validation_samples: int | None,
    profile: SpbcV2DpoTrainingProfile,
) -> None:
    if epochs <= 0 or batch_size <= 0:
        raise SpbcV2DpoTrainingError("epochs and batch_size must be positive")
    if not math.isfinite(float(learning_rate)) or float(learning_rate) <= 0.0:
        raise SpbcV2DpoTrainingError("learning_rate must be finite and positive")
    for name, value in (("max_training_samples", max_training_samples), ("max_validation_samples", max_validation_samples)):
        if value is not None and int(value) <= 0:
            raise SpbcV2DpoTrainingError("{0} must be positive when provided".format(name))
    for name in (
        "ce_loss_weight",
        "dpo_loss_weight",
        "ranking_loss_weight",
        "utility_loss_weight",
        "rebuffer_loss_weight",
        "dpo_beta",
        "ranking_margin_scale",
        "utility_temperature",
        "rebuffer_loss_cap_s",
        "aux_reward_loss_weight",
        "aux_rebuffer_loss_weight",
        "aux_risk_loss_weight",
        "reference_kl_loss_weight",
        "over_aggressive_probability_loss_weight",
        "over_aggressive_margin_loss_weight",
        "over_aggressive_reference_excess_loss_weight",
        "over_aggressive_margin",
        "decision_reward_fusion_weight",
        "decision_rebuffer_fusion_weight",
        "decision_risk_fusion_weight",
        "focus_bucket_sample_weight",
        "severe_error_sample_weight",
        "safe_vs_rebuffer_pair_weight",
        "over_aggressive_rebuffer_action_weight",
        "selection_focus_weight",
        "selection_rebuffer_weight",
        "selection_over_aggressive_weight",
        "selection_invalid_weight",
        "safety_global_over_aggressive_tolerance",
        "safety_focus_over_aggressive_tolerance",
        "safety_spbc_v2_over_aggressive_tolerance",
        "safety_utility_regret_tolerance",
        "safety_rebuffer_regret_tolerance",
        "max_pair_weight",
    ):
        value = float(getattr(profile, name))
        if not math.isfinite(value) or value < 0.0:
            raise SpbcV2DpoTrainingError("{0} must be finite and non-negative".format(name))
    if float(profile.utility_temperature) <= 0.0 or float(profile.rebuffer_loss_cap_s) <= 0.0:
        raise SpbcV2DpoTrainingError("utility_temperature and rebuffer_loss_cap_s must be positive")


def _resolve_limit(value: int | None | str, profile_value: int | None) -> int | None:
    if value == "profile":
        return profile_value
    if value is None:
        return None
    return int(value)


def _move_batch(batch: Sequence[torch.Tensor], device: torch.device) -> tuple[torch.Tensor, ...]:
    return tuple(tensor.to(device) for tensor in batch)


def _progress_batch_interval(total_batches: int) -> int:
    if total_batches <= 10:
        return 1
    return max(1, total_batches // 20)


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SpbcV2DpoTrainingError("{0} must be an object".format(name))
    return value


def _reject_unexpected_keys(
    mapping: Mapping[str, object],
    allowed_keys: set[str] | frozenset[str],
    name: str,
    line_number: int,
) -> None:
    unexpected = sorted(str(key) for key in mapping.keys() if str(key) not in allowed_keys)
    if unexpected:
        raise SpbcV2DpoTrainingError(
            "line {0}: {1} has non-input field(s): {2}".format(line_number, name, ", ".join(unexpected))
        )


def _integer(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise SpbcV2DpoTrainingError("{0} must be an integer".format(name))
    return int(value)


def _finite_number(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise SpbcV2DpoTrainingError("{0} must be numeric".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise SpbcV2DpoTrainingError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(parsed):
        raise SpbcV2DpoTrainingError("{0} must be finite".format(name))
    return parsed


def _tuple_of_floats(value: object, expected_len: int, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise SpbcV2DpoTrainingError("{0} must be a sequence".format(name))
    if len(value) != int(expected_len):
        raise SpbcV2DpoTrainingError("{0} length mismatch".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
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
