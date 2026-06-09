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
    DATA_FILENAMES,
    MEDIA_PROFILE_ID,
    REWARD_VERSION,
    SPBC_CHECKPOINT_SCHEMA_ID,
    SPBC_MODEL_CONFIG_FILENAME,
    SPBC_MODEL_CONFIG_SCHEMA_ID,
    SPBC_MODEL_FILENAME,
    SPBC_NORMALIZATION_FILENAME,
    SPBC_TARGET_ID,
    SPBC_TRAINING_REPORT_FILENAME,
    SPBC_TRAINING_REPORT_SCHEMA_ID,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.phase45_v1.validation import validate_phase45_v1_dataset_dir


class SpbcTrainingError(ValueError):
    """Raised when spbc_abr_v1 offline training cannot proceed safely."""


SEQUENCE_FEATURES = ("throughput_history_bps", "download_time_history_s")
SCALAR_FEATURES = (
    "buffer_s",
    "last_representation_index",
    "last_bitrate_bps",
    "recent_rebuffer_s",
    "recent_switch_abs",
    "chunks_remaining_norm",
    "has_chunks_remaining",
)
CANDIDATE_FEATURES = (
    "candidate_representation_index",
    "candidate_ladder_position_norm",
    "candidate_bitrate_bps",
    "candidate_bitrate_norm_ladder",
    "candidate_delta_from_last_bitrate_norm",
    "candidate_chunk_size_bytes",
    "candidate_chunk_size_available",
)


@dataclass(frozen=True)
class SpbcTrainingProfile:
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
    label_smoothing: float = 0.03
    class_weight_power: float = 0.5
    class_weight_min: float = 0.35
    class_weight_max: float = 3.0
    seed: int = 450501

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
            "class_weight_power": self.class_weight_power,
            "class_weight_min": self.class_weight_min,
            "class_weight_max": self.class_weight_max,
            "seed": self.seed,
        }


SPBC_TRAINING_PROFILES: dict[str, SpbcTrainingProfile] = {
    "smoke": SpbcTrainingProfile(
        name="smoke",
        epochs=1,
        batch_size=32,
        learning_rate=1.0e-3,
        max_training_samples=512,
        max_validation_samples=256,
        history_hidden_size=32,
        state_hidden_size=32,
        candidate_hidden_size=24,
        shared_hidden_size=64,
        dropout=0.0,
        label_smoothing=0.02,
        seed=450511,
    ),
    "pilot": SpbcTrainingProfile(
        name="pilot",
        epochs=10,
        batch_size=512,
        learning_rate=7.0e-4,
        max_training_samples=30000,
        max_validation_samples=8000,
        history_hidden_size=64,
        state_hidden_size=64,
        candidate_hidden_size=32,
        shared_hidden_size=128,
        dropout=0.05,
        label_smoothing=0.03,
        seed=450521,
    ),
    "full_v1": SpbcTrainingProfile(
        name="full_v1",
        epochs=35,
        batch_size=1024,
        learning_rate=5.0e-4,
        max_training_samples=None,
        max_validation_samples=None,
        history_hidden_size=128,
        state_hidden_size=96,
        candidate_hidden_size=48,
        shared_hidden_size=192,
        dropout=0.10,
        label_smoothing=0.03,
        seed=450531,
    ),
}


@dataclass(frozen=True)
class SpbcExample:
    sequence: tuple[tuple[float, float], ...]
    scalars: tuple[float, ...]
    candidates: tuple[tuple[float, ...], ...]
    action_mask: tuple[bool, ...]
    oracle_action: int
    oracle_reward_n: float
    risk_targets: tuple[float, ...]
    data_role: str
    throughput_bucket: str
    synthetic: bool


@dataclass(frozen=True)
class SpbcNormalizationStats:
    schema_id: str
    fitted_on_data_role: str
    sequence_mean: tuple[float, float]
    sequence_std: tuple[float, float]
    scalar_mean: tuple[float, ...]
    scalar_std: tuple[float, ...]
    candidate_mean: tuple[float, ...]
    candidate_std: tuple[float, ...]
    sample_count: int
    candidate_row_count: int

    def to_json(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "fitted_on_data_role": self.fitted_on_data_role,
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
        }


class SpbcAbrV1Policy(nn.Module):
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
    ) -> None:
        super().__init__()
        self.sequence_dim = int(sequence_dim)
        self.scalar_dim = int(scalar_dim)
        self.candidate_dim = int(candidate_dim)
        self.history_hidden_size = int(history_hidden_size)
        self.state_hidden_size = int(state_hidden_size)
        self.candidate_hidden_size = int(candidate_hidden_size)
        self.shared_hidden_size = int(shared_hidden_size)
        self.dropout = float(dropout)

        self.history_encoder = nn.GRU(
            input_size=self.sequence_dim,
            hidden_size=self.history_hidden_size,
            batch_first=True,
        )
        self.state_encoder = nn.Sequential(
            nn.Linear(self.scalar_dim, self.state_hidden_size),
            nn.ReLU(),
            nn.Dropout(self.dropout),
        )
        self.shared = nn.Sequential(
            nn.Linear(self.history_hidden_size + self.state_hidden_size, self.shared_hidden_size),
            nn.ReLU(),
            nn.Dropout(self.dropout),
            nn.Linear(self.shared_hidden_size, self.shared_hidden_size),
            nn.ReLU(),
        )
        self.candidate_encoder = nn.Sequential(
            nn.Linear(self.candidate_dim, self.candidate_hidden_size),
            nn.ReLU(),
            nn.Dropout(self.dropout),
        )
        self.policy_head = nn.Sequential(
            nn.Linear(self.shared_hidden_size + self.candidate_hidden_size, self.shared_hidden_size),
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
        logits = self.policy_head(torch.cat([expanded_shared, candidate_vectors], dim=2)).squeeze(2)
        mask = action_mask.to(dtype=torch.bool, device=logits.device)
        return {"action_logits": logits.masked_fill(~mask, -1.0e9)}

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": SPBC_MODEL_CONFIG_SCHEMA_ID,
            "model_key": "spbc_abr_v1",
            "model_family": "Safe Policy Behavioral Cloning ABR v1",
            "model_type": "gru_candidate_policy",
            "sequence_features": list(SEQUENCE_FEATURES),
            "scalar_features": list(SCALAR_FEATURES),
            "candidate_features": list(CANDIDATE_FEATURES),
            "target": "spbc_targets.oracle_action",
            "sequence_dim": self.sequence_dim,
            "scalar_dim": self.scalar_dim,
            "candidate_dim": self.candidate_dim,
            "history_hidden_size": self.history_hidden_size,
            "state_hidden_size": self.state_hidden_size,
            "candidate_hidden_size": self.candidate_hidden_size,
            "shared_hidden_size": self.shared_hidden_size,
            "dropout": self.dropout,
            "controller_registered": False,
            "bundle_exported": False,
        }


def profile_by_name(name: str) -> SpbcTrainingProfile:
    key = str(name).strip()
    if key not in SPBC_TRAINING_PROFILES:
        raise SpbcTrainingError("unknown spbc_abr_v1 training profile: {0}".format(name))
    return SPBC_TRAINING_PROFILES[key]


def train_spbc_abr_v1(
    dataset_dir: object,
    output_dir: object,
    *,
    profile: SpbcTrainingProfile,
    overwrite: bool = False,
    device: str = "auto",
    epochs: int | None = None,
    batch_size: int | None = None,
    learning_rate: float | None = None,
    max_training_samples: int | None | str = "profile",
    max_validation_samples: int | None | str = "profile",
    validate_dataset: bool = True,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
) -> Mapping[str, object]:
    _emit_progress(progress_callback, "preparing", "Preparando entrenamiento spbc_abr_v1")
    data_path = ensure_existing_dir(dataset_dir, purpose="phase45_v1 dataset")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="spbc_abr_v1 model")
    if validate_dataset:
        _emit_progress(progress_callback, "validating_dataset", "Validando dataset phase45_v1")
        dataset_validation = validate_phase45_v1_dataset_dir(data_path)
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
        "Cargando muestras JSONL",
        device_used=str(selected_device),
        training_limit=train_limit,
        validation_limit=val_limit,
    )
    training_examples = load_spbc_examples(data_path / DATA_FILENAMES[TRAINING_ROLE], TRAINING_ROLE, limit=train_limit)
    validation_examples = load_spbc_examples(data_path / DATA_FILENAMES[VALIDATION_ROLE], VALIDATION_ROLE, limit=val_limit)
    if not training_examples or not validation_examples:
        raise SpbcTrainingError("spbc_abr_v1 training requires training and validation examples")
    _emit_progress(
        progress_callback,
        "examples_loaded",
        "Muestras cargadas",
        training_samples=len(training_examples),
        validation_samples=len(validation_examples),
    )
    normalization = fit_spbc_normalization(training_examples)
    train_tensors = examples_to_tensors(training_examples, normalization)
    validation_tensors = examples_to_tensors(validation_examples, normalization)
    class_count = int(train_tensors[2].shape[1])
    class_weighting = compute_class_weighting(training_examples, class_count, profile)
    class_weights = torch.tensor(class_weighting["weights"], dtype=torch.float32, device=selected_device)

    model = SpbcAbrV1Policy(
        history_hidden_size=profile.history_hidden_size,
        state_hidden_size=profile.state_hidden_size,
        candidate_hidden_size=profile.candidate_hidden_size,
        shared_hidden_size=profile.shared_hidden_size,
        dropout=profile.dropout,
    ).to(selected_device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=active_learning_rate)
    generator = torch.Generator()
    generator.manual_seed(profile.seed)
    train_loader = DataLoader(
        TensorDataset(*train_tensors),
        batch_size=active_batch_size,
        shuffle=True,
        generator=generator,
    )
    train_eval_loader = DataLoader(
        TensorDataset(*train_tensors),
        batch_size=active_batch_size,
        shuffle=False,
    )
    validation_loader = DataLoader(
        TensorDataset(*validation_tensors),
        batch_size=active_batch_size,
        shuffle=False,
    )

    epoch_reports = []
    best_validation_loss = math.inf
    best_state_dict = None
    best_epoch = 0
    for epoch in range(1, active_epochs + 1):
        epoch_started = time.monotonic()
        _emit_progress(
            progress_callback,
            "epoch_started",
            "Iniciando epoca",
            epoch=epoch,
            epochs=active_epochs,
            train_batches=len(train_loader),
        )
        train_metrics = _run_epoch(
            model,
            train_loader,
            device=selected_device,
            optimizer=optimizer,
            class_weights=class_weights,
            profile=profile,
            progress_callback=progress_callback,
            epoch=epoch,
            epochs=active_epochs,
        )
        _emit_progress(
            progress_callback,
            "epoch_validation_started",
            "Validando epoca",
            epoch=epoch,
            epochs=active_epochs,
            validation_batches=len(validation_loader),
        )
        validation_metrics = evaluate_spbc_model(
            model,
            validation_loader,
            device=selected_device,
            class_weights=class_weights,
            profile=profile,
            examples=validation_examples,
        )
        epoch_report = {
            "epoch": epoch,
            "training_loss": train_metrics["loss"],
            "training_weighted_cross_entropy_loss": train_metrics["weighted_cross_entropy_loss"],
            "validation_loss": validation_metrics["loss"],
            "validation_top1_accuracy": validation_metrics["top1_accuracy"],
            "validation_balanced_accuracy": validation_metrics["balanced_accuracy"],
            "validation_macro_f1": validation_metrics["macro_f1"],
            "validation_predicted_action_risk_rate": validation_metrics["predicted_action_risk_rate"],
        }
        epoch_reports.append(epoch_report)
        is_best = float(validation_metrics["loss"]) < best_validation_loss
        if is_best:
            best_validation_loss = float(validation_metrics["loss"])
            best_epoch = epoch
            best_state_dict = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}
        _emit_progress(
            progress_callback,
            "epoch_finished",
            "Epoca completada",
            epoch=epoch,
            epochs=active_epochs,
            epoch_duration_s=time.monotonic() - epoch_started,
            training_loss=train_metrics["loss"],
            validation_loss=validation_metrics["loss"],
            validation_top1_accuracy=validation_metrics["top1_accuracy"],
            validation_balanced_accuracy=validation_metrics["balanced_accuracy"],
            validation_macro_f1=validation_metrics["macro_f1"],
            best_epoch=best_epoch,
            best_so_far=is_best,
        )

    if best_state_dict is not None:
        model.load_state_dict(best_state_dict)
    _emit_progress(progress_callback, "final_evaluation_started", "Calculando metricas finales")
    final_training_metrics = evaluate_spbc_model(
        model,
        train_eval_loader,
        device=selected_device,
        class_weights=class_weights,
        profile=profile,
        examples=training_examples,
    )
    final_validation_metrics = evaluate_spbc_model(
        model,
        validation_loader,
        device=selected_device,
        class_weights=class_weights,
        profile=profile,
        examples=validation_examples,
    )
    model_config = dict(model.config())
    normalization_payload = normalization.to_json()
    checkpoint_path = output_path / SPBC_MODEL_FILENAME
    config_path = output_path / SPBC_MODEL_CONFIG_FILENAME
    normalization_path = output_path / SPBC_NORMALIZATION_FILENAME
    report_path = output_path / SPBC_TRAINING_REPORT_FILENAME
    checkpoint = {
        "schema_id": SPBC_CHECKPOINT_SCHEMA_ID,
        "model_key": "spbc_abr_v1",
        "model_state_dict": model.state_dict(),
        "model_config": model_config,
        "normalization": normalization_payload,
        "class_weighting": class_weighting,
        "training_profile": profile.to_json(),
        "best_epoch": best_epoch,
        "device_used": str(selected_device),
        "controller_registered": False,
        "bundle_exported": False,
    }
    torch.save(checkpoint, checkpoint_path)
    write_json(config_path, model_config)
    write_json(normalization_path, normalization_payload)
    duration_s = time.monotonic() - started
    report = {
        "schema_id": SPBC_TRAINING_REPORT_SCHEMA_ID,
        "human_readable_name": "Entrenamiento offline de spbc_abr_v1",
        "phase": "fase_4_5_v1_bloque5_entrenamiento_spbc_abr_v1",
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
        "epoch_reports": epoch_reports,
        "class_weighting": class_weighting,
        "training_metrics": final_training_metrics,
        "validation_metrics": final_validation_metrics,
        "training_duration_s": duration_s,
        "model_config": model_config,
        "artifacts": {
            "checkpoint": str(checkpoint_path),
            "checkpoint_sha256": _sha256_file(checkpoint_path),
            "model_config": str(config_path),
            "normalization": str(normalization_path),
            "training_report": str(report_path),
        },
        "normalization_fitted_on": TRAINING_ROLE,
        "class_weights_fitted_on": TRAINING_ROLE,
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
        "spc_checkpoint_used": False,
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
        "Entrenamiento spbc_abr_v1 finalizado",
        training_duration_s=duration_s,
        output_dir=str(output_path),
        best_epoch=best_epoch,
    )
    return report


def load_spbc_examples(path: object, data_role: str, limit: int | None = None) -> tuple[SpbcExample, ...]:
    examples = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                raw = json.loads(text)
            except json.JSONDecodeError as exc:
                raise SpbcTrainingError("{0}: invalid JSONL line {1}".format(path, line_number)) from exc
            examples.append(_example_from_sample(raw, data_role, line_number))
            if limit is not None and len(examples) >= int(limit):
                break
    return tuple(examples)


def fit_spbc_normalization(examples: Sequence[SpbcExample]) -> SpbcNormalizationStats:
    if not examples:
        raise SpbcTrainingError("normalization requires training examples")
    sequence_rows = [step for example in examples for step in example.sequence]
    scalar_rows = [example.scalars for example in examples]
    candidate_rows = [candidate for example in examples for candidate in example.candidates]
    return SpbcNormalizationStats(
        schema_id="phase45_v1_spbc_abr_normalization_v1",
        fitted_on_data_role=TRAINING_ROLE,
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
    examples: Sequence[SpbcExample],
    normalization: SpbcNormalizationStats,
) -> tuple[torch.Tensor, ...]:
    if not examples:
        raise SpbcTrainingError("examples_to_tensors requires examples")
    max_candidates = max(len(example.candidates) for example in examples)
    sequence_rows = []
    scalar_rows = []
    candidate_rows = []
    mask_rows = []
    labels = []
    risk_targets = []
    for example in examples:
        if example.oracle_action >= len(example.candidates):
            raise SpbcTrainingError("oracle_action outside candidate range")
        if not example.action_mask[example.oracle_action]:
            raise SpbcTrainingError("oracle_action is masked as invalid")
        sequence_rows.append(_normalize_matrix(example.sequence, normalization.sequence_mean, normalization.sequence_std))
        scalar_rows.append(_normalize_vector(example.scalars, normalization.scalar_mean, normalization.scalar_std))
        candidates = [_normalize_vector(candidate, normalization.candidate_mean, normalization.candidate_std) for candidate in example.candidates]
        mask = [bool(value) for value in example.action_mask]
        risks = [float(value) for value in example.risk_targets]
        while len(candidates) < max_candidates:
            candidates.append([0.0 for _ in CANDIDATE_FEATURES])
            mask.append(False)
            risks.append(1.0)
        candidate_rows.append(candidates)
        mask_rows.append(mask)
        labels.append(int(example.oracle_action))
        risk_targets.append(risks)
    return (
        torch.tensor(sequence_rows, dtype=torch.float32),
        torch.tensor(scalar_rows, dtype=torch.float32),
        torch.tensor(candidate_rows, dtype=torch.float32),
        torch.tensor(mask_rows, dtype=torch.bool),
        torch.tensor(labels, dtype=torch.long),
        torch.tensor(risk_targets, dtype=torch.float32),
    )


def compute_class_weighting(
    examples: Sequence[SpbcExample],
    class_count: int,
    profile: SpbcTrainingProfile,
) -> Mapping[str, object]:
    counts = Counter(int(example.oracle_action) for example in examples)
    raw = []
    for index in range(class_count):
        count = int(counts.get(index, 0))
        raw.append(count ** (-float(profile.class_weight_power)) if count > 0 else 1.0)
    nonzero_indices = [index for index in range(class_count) if int(counts.get(index, 0)) > 0]
    mean_raw = sum(raw[index] for index in nonzero_indices) / float(len(nonzero_indices) or 1)
    normalized = [value / max(mean_raw, 1.0e-12) for value in raw]
    weights = [
        min(max(float(value), float(profile.class_weight_min)), float(profile.class_weight_max))
        for value in normalized
    ]
    return {
        "scheme": "inverse_sqrt_frequency_train_only",
        "class_weight_power": profile.class_weight_power,
        "class_weight_min": profile.class_weight_min,
        "class_weight_max": profile.class_weight_max,
        "class_counts": {str(index): int(counts.get(index, 0)) for index in range(class_count)},
        "weights": [round(float(value), 9) for value in weights],
        "fitted_on": TRAINING_ROLE,
        "metadata_used": False,
        "validation_used": False,
    }


def evaluate_spbc_model(
    model: SpbcAbrV1Policy,
    loader: DataLoader,
    *,
    device: torch.device,
    class_weights: torch.Tensor,
    profile: SpbcTrainingProfile,
    examples: Sequence[SpbcExample],
) -> Mapping[str, object]:
    model.eval()
    totals = _PolicyMetricTotals()
    predictions_by_bucket: dict[str, _PolicyMetricTotals] = defaultdict(_PolicyMetricTotals)
    start_index = 0
    with torch.no_grad():
        for batch in loader:
            moved = _move_batch(batch, device)
            outputs = model(moved[0], moved[1], moved[2], moved[3])
            losses = _loss_components(outputs, moved, class_weights, profile)
            batch_size = int(moved[0].shape[0])
            observations = _policy_observations(outputs, moved)
            totals.add_observations(observations, losses, batch_size)
            for row_offset, observation in enumerate(observations):
                example = examples[start_index + row_offset]
                predictions_by_bucket[example.throughput_bucket].add_observations((observation,), {}, 1)
            start_index += batch_size
    model.train()
    return {
        **totals.to_json(),
        "by_throughput_bucket": {
            bucket: metrics.to_json(include_losses=False)
            for bucket, metrics in sorted(predictions_by_bucket.items())
        },
    }


def resolve_torch_device(requested: str) -> torch.device:
    key = str(requested).strip().lower()
    if key == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if key == "cuda" and not torch.cuda.is_available():
        raise SpbcTrainingError("CUDA/ROCm device requested but torch.cuda.is_available() is false")
    if key not in {"cpu", "cuda"}:
        raise SpbcTrainingError("device must be cpu, cuda or auto")
    return torch.device(key)


def set_training_seed(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed))


def _run_epoch(
    model: SpbcAbrV1Policy,
    loader: DataLoader,
    *,
    device: torch.device,
    optimizer: torch.optim.Optimizer,
    class_weights: torch.Tensor,
    profile: SpbcTrainingProfile,
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
        losses = _loss_components(outputs, moved, class_weights, profile)
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
                "Entrenando batches",
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
    class_weights: torch.Tensor,
    profile: SpbcTrainingProfile,
) -> dict[str, torch.Tensor]:
    logits = outputs["action_logits"]
    mask = batch[3].to(dtype=torch.bool)
    labels = batch[4]
    loss = _masked_weighted_cross_entropy(
        logits,
        labels,
        mask,
        class_weights,
        label_smoothing=float(profile.label_smoothing),
    )
    return {
        "loss_tensor": loss,
        "loss": loss.detach(),
        "weighted_cross_entropy_loss": loss.detach(),
    }


def _masked_weighted_cross_entropy(
    logits: torch.Tensor,
    labels: torch.Tensor,
    mask: torch.Tensor,
    class_weights: torch.Tensor,
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
    sample_weights = class_weights.to(device=logits.device, dtype=logits.dtype)[labels]
    return (per_sample_loss * sample_weights).mean()


def _policy_observations(
    outputs: Mapping[str, torch.Tensor],
    batch: Sequence[torch.Tensor],
) -> tuple[Mapping[str, object], ...]:
    logits = outputs["action_logits"]
    labels = batch[4]
    risk_targets = batch[5]
    mask = batch[3].to(dtype=torch.bool)
    predictions = torch.argmax(logits, dim=1)
    k = min(2, int(logits.shape[1]))
    topk = torch.topk(logits, k=k, dim=1).indices
    observations = []
    labels_cpu = labels.detach().cpu().tolist()
    predictions_cpu = predictions.detach().cpu().tolist()
    topk_cpu = topk.detach().cpu().tolist()
    mask_cpu = mask.detach().cpu().tolist()
    risks_cpu = risk_targets.detach().cpu().tolist()
    for index, label in enumerate(labels_cpu):
        prediction = int(predictions_cpu[index])
        oracle_action = int(label)
        valid_prediction = bool(mask_cpu[index][prediction]) if prediction < len(mask_cpu[index]) else False
        observations.append(
            {
                "oracle_action": oracle_action,
                "predicted_action": prediction,
                "top2_hit": oracle_action in [int(value) for value in topk_cpu[index]],
                "valid_prediction": valid_prediction,
                "predicted_action_risk": float(risks_cpu[index][prediction]) if valid_prediction else 1.0,
                "oracle_action_risk": float(risks_cpu[index][oracle_action]),
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
        for name in ("loss", "weighted_cross_entropy_loss"):
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
    invalid_count: int = 0
    over_count: int = 0
    under_count: int = 0
    action_delta_sum: float = 0.0
    predicted_action_risk_sum: float = 0.0
    oracle_action_risk_sum: float = 0.0

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
        for name in ("loss", "weighted_cross_entropy_loss"):
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
            delta = predicted_action - oracle_action
            self.action_delta_sum += float(delta)
            if delta > 0:
                self.over_count += 1
            elif delta < 0:
                self.under_count += 1
            self.predicted_action_risk_sum += float(observation["predicted_action_risk"])
            self.oracle_action_risk_sum += float(observation["oracle_action_risk"])

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
                "balanced_accuracy": round(sum(recalls) / float(len(recalls) or 1), 6),
                "macro_f1": round(sum(f1_values) / float(len(f1_values) or 1), 6),
                "mean_action_delta": round(self.action_delta_sum / denominator, 6),
                "over_aggressive_rate": round(float(self.over_count) / denominator, 6),
                "under_aggressive_rate": round(float(self.under_count) / denominator, 6),
                "invalid_action_rate": round(float(self.invalid_count) / denominator, 6),
                "predicted_action_risk_rate": round(self.predicted_action_risk_sum / denominator, 6),
                "oracle_action_risk_rate": round(self.oracle_action_risk_sum / denominator, 6),
                "oracle_action_distribution": {key: int(self.target_counts.get(key, 0)) for key in target_class_keys},
                "predicted_action_distribution": {key: int(self.predicted_counts.get(key, 0)) for key in class_keys},
                "sample_count": int(self.weight),
            }
        )
        return payload


def _emit_progress(
    callback: Callable[[Mapping[str, object]], None] | None,
    event: str,
    message: str,
    **fields: object,
) -> None:
    if callback is None:
        return
    payload = {"event": event, "message": message, **fields}
    callback(payload)


def _progress_batch_interval(total_batches: int) -> int:
    if total_batches <= 10:
        return 1
    return max(1, total_batches // 20)


def _move_batch(batch: Sequence[torch.Tensor], device: torch.device) -> tuple[torch.Tensor, ...]:
    return tuple(tensor.to(device) for tensor in batch)


def _example_from_sample(sample: Mapping[str, object], expected_role: str, line_number: int) -> SpbcExample:
    if sample.get("data_role") != expected_role:
        raise SpbcTrainingError("line {0}: data_role mismatch".format(line_number))
    model_inputs = _require_mapping(sample.get("model_inputs"), "model_inputs")
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidates_raw = model_inputs.get("candidates")
    action_mask_raw = model_inputs.get("action_mask")
    if not isinstance(candidates_raw, list) or not isinstance(action_mask_raw, list):
        raise SpbcTrainingError("line {0}: candidates/action_mask must be lists".format(line_number))
    spbc_targets = _require_mapping(sample.get("spbc_targets"), "spbc_targets")
    if spbc_targets.get("target_id") != SPBC_TARGET_ID:
        raise SpbcTrainingError("line {0}: unexpected spbc target id".format(line_number))
    oracle_action = spbc_targets.get("oracle_action")
    if isinstance(oracle_action, bool) or not isinstance(oracle_action, int):
        raise SpbcTrainingError("line {0}: oracle_action must be an integer".format(line_number))
    spc_targets = _require_mapping(sample.get("spc_targets"), "spc_targets")
    per_candidate = spc_targets.get("per_candidate_download_risk")
    if not isinstance(per_candidate, list):
        raise SpbcTrainingError("line {0}: per_candidate_download_risk must be a list".format(line_number))
    sequence = _sequence_from_context(context)
    scalars = tuple(_finite_number(context.get(name), name) for name in SCALAR_FEATURES)
    candidates = tuple(
        tuple(_finite_number(_require_mapping(candidate, "candidate").get(name), name) for name in CANDIDATE_FEATURES)
        for candidate in candidates_raw
    )
    action_mask = tuple(bool(value) for value in action_mask_raw)
    risk_targets = tuple(_risk_target_for_candidate(item, index) for index, item in enumerate(per_candidate))
    if len(candidates) != len(action_mask) or len(candidates) != len(risk_targets):
        raise SpbcTrainingError("line {0}: candidates, mask and risk targets length mismatch".format(line_number))
    if int(oracle_action) < 0 or int(oracle_action) >= len(candidates):
        raise SpbcTrainingError("line {0}: oracle_action outside candidate range".format(line_number))
    if not action_mask[int(oracle_action)]:
        raise SpbcTrainingError("line {0}: oracle_action is masked as invalid".format(line_number))
    metadata = _require_mapping(sample.get("metadata"), "metadata")
    return SpbcExample(
        sequence=sequence,
        scalars=scalars,
        candidates=candidates,
        action_mask=action_mask,
        oracle_action=int(oracle_action),
        oracle_reward_n=_finite_number(spbc_targets.get("oracle_horizon_reward_n"), "oracle_horizon_reward_n"),
        risk_targets=risk_targets,
        data_role=expected_role,
        throughput_bucket=str(metadata.get("throughput_bucket", "unknown")),
        synthetic=bool(metadata.get("synthetic") is True),
    )


def _sequence_from_context(context: Mapping[str, object]) -> tuple[tuple[float, float], ...]:
    throughput = _numeric_sequence(context.get("throughput_history_bps"), "throughput_history_bps")
    download = _numeric_sequence(context.get("download_time_history_s"), "download_time_history_s")
    if len(throughput) != len(download):
        raise SpbcTrainingError("history feature lengths differ")
    return tuple((throughput[index], download[index]) for index in range(len(throughput)))


def _risk_target_for_candidate(item: object, index: int) -> float:
    mapping = _require_mapping(item, "risk candidate {0}".format(index))
    risk = _finite_number(mapping.get("rebuffer_risk"), "rebuffer_risk")
    return 1.0 if risk >= 0.5 else 0.0


def _numeric_sequence(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise SpbcTrainingError("{0} must be a sequence".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SpbcTrainingError("{0} must be an object".format(name))
    return value


def _finite_number(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise SpbcTrainingError("{0} must be numeric".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise SpbcTrainingError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(parsed):
        raise SpbcTrainingError("{0} must be finite".format(name))
    return parsed


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
        raise SpbcTrainingError("normalization rows must not be empty")
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise SpbcTrainingError("normalization row width changed")
    return width


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> list[float]:
    if len(values) != len(mean) or len(mean) != len(std):
        raise SpbcTrainingError("normalization vector width mismatch")
    return [(float(value) - float(mean[index])) / float(std[index]) for index, value in enumerate(values)]


def _normalize_matrix(
    values: Sequence[Sequence[float]],
    mean: Sequence[float],
    std: Sequence[float],
) -> list[list[float]]:
    return [_normalize_vector(row, mean, std) for row in values]


def _validate_training_args(
    epochs: int,
    batch_size: int,
    learning_rate: float,
    max_training_samples: int | None,
    max_validation_samples: int | None,
) -> None:
    if epochs <= 0 or batch_size <= 0:
        raise SpbcTrainingError("epochs and batch_size must be positive")
    if not math.isfinite(float(learning_rate)) or float(learning_rate) <= 0.0:
        raise SpbcTrainingError("learning_rate must be finite and positive")
    for name, value in (("max_training_samples", max_training_samples), ("max_validation_samples", max_validation_samples)):
        if value is not None and int(value) <= 0:
            raise SpbcTrainingError("{0} must be positive when provided".format(name))


def _resolve_limit(value: int | None | str, profile_value: int | None) -> int | None:
    if value == "profile":
        return profile_value
    if value is None:
        return None
    return int(value)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
