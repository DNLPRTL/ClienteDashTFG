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
from typing import Callable, Iterable, Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, TensorDataset

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, write_json
from core.phase45_v1.constants import (
    DATA_FILENAMES,
    DATA_ROLES,
    MEDIA_PROFILE_ID,
    REWARD_VERSION,
    SPC_CHECKPOINT_SCHEMA_ID,
    SPC_MODEL_CONFIG_FILENAME,
    SPC_MODEL_CONFIG_SCHEMA_ID,
    SPC_MODEL_FILENAME,
    SPC_NORMALIZATION_FILENAME,
    SPC_TARGET_ID,
    SPC_TRAINING_REPORT_FILENAME,
    SPC_TRAINING_REPORT_SCHEMA_ID,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.phase45_v1.validation import validate_phase45_v1_dataset_dir


class SpcTrainingError(ValueError):
    """Raised when spc_abr_v1 offline training cannot proceed safely."""


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
QUANTILE_KEYS = ("p10", "p25", "p50")
QUANTILE_VALUES = (0.10, 0.25, 0.50)


@dataclass(frozen=True)
class SpcTrainingProfile:
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
    quantile_loss_weight: float = 1.0
    capacity_loss_weight: float = 0.5
    risk_loss_weight: float = 1.0
    seed: int = 450401

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
            "quantile_loss_weight": self.quantile_loss_weight,
            "capacity_loss_weight": self.capacity_loss_weight,
            "risk_loss_weight": self.risk_loss_weight,
            "seed": self.seed,
        }


SPC_TRAINING_PROFILES: dict[str, SpcTrainingProfile] = {
    "smoke": SpcTrainingProfile(
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
        seed=450411,
    ),
    "pilot": SpcTrainingProfile(
        name="pilot",
        epochs=8,
        batch_size=512,
        learning_rate=8.0e-4,
        max_training_samples=30000,
        max_validation_samples=8000,
        history_hidden_size=64,
        state_hidden_size=64,
        candidate_hidden_size=32,
        shared_hidden_size=128,
        dropout=0.05,
        seed=450421,
    ),
    "full_v1": SpcTrainingProfile(
        name="full_v1",
        epochs=30,
        batch_size=1024,
        learning_rate=5.0e-4,
        max_training_samples=None,
        max_validation_samples=None,
        history_hidden_size=128,
        state_hidden_size=96,
        candidate_hidden_size=48,
        shared_hidden_size=192,
        dropout=0.10,
        seed=450431,
    ),
}


@dataclass(frozen=True)
class SpcExample:
    sequence: tuple[tuple[float, float], ...]
    scalars: tuple[float, ...]
    candidates: tuple[tuple[float, ...], ...]
    action_mask: tuple[bool, ...]
    quantile_log_targets: tuple[float, float, float]
    capacity_log_target: float
    risk_targets: tuple[float, ...]
    data_role: str
    throughput_bucket: str
    synthetic: bool


@dataclass(frozen=True)
class SpcNormalizationStats:
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


class SpcAbrV1Predictor(nn.Module):
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
        self.quantile_head = nn.Linear(self.shared_hidden_size, len(QUANTILE_KEYS))
        self.capacity_head = nn.Linear(self.shared_hidden_size, 1)
        self.candidate_encoder = nn.Sequential(
            nn.Linear(self.candidate_dim, self.candidate_hidden_size),
            nn.ReLU(),
            nn.Dropout(self.dropout),
        )
        self.risk_head = nn.Sequential(
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
            raise SpcTrainingError("sequence must have shape [batch, history, sequence_dim]")
        if scalars.ndim != 2 or scalars.shape[1] != self.scalar_dim:
            raise SpcTrainingError("scalars must have shape [batch, scalar_dim]")
        if candidates.ndim != 3 or candidates.shape[2] != self.candidate_dim:
            raise SpcTrainingError("candidates must have shape [batch, candidates, candidate_dim]")
        if action_mask.shape != candidates.shape[:2]:
            raise SpcTrainingError("action_mask shape must match candidate rows")

        _history_output, hidden = self.history_encoder(sequence)
        history_vector = hidden[-1]
        state_vector = self.state_encoder(scalars)
        shared = self.shared(torch.cat([history_vector, state_vector], dim=1))

        raw_quantiles = self.quantile_head(shared)
        q10 = raw_quantiles[:, 0]
        q25 = q10 + F.softplus(raw_quantiles[:, 1])
        q50 = q25 + F.softplus(raw_quantiles[:, 2])
        quantiles = torch.stack([q10, q25, q50], dim=1)
        capacity = self.capacity_head(shared).squeeze(1)

        batch_size, candidate_count, _ = candidates.shape
        candidate_vectors = self.candidate_encoder(candidates)
        expanded_shared = shared.unsqueeze(1).expand(batch_size, candidate_count, self.shared_hidden_size)
        risk_logits = self.risk_head(torch.cat([expanded_shared, candidate_vectors], dim=2)).squeeze(2)
        mask = action_mask.to(dtype=torch.bool, device=risk_logits.device)
        return {
            "quantile_log_kbps": quantiles,
            "capacity_log_kbps": capacity,
            "risk_logits": risk_logits.masked_fill(~mask, 0.0),
        }

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": SPC_MODEL_CONFIG_SCHEMA_ID,
            "model_key": "spc_abr_v1",
            "model_family": "Safe Predictive Control ABR v1",
            "model_type": "gru_capacity_risk_predictor",
            "sequence_features": list(SEQUENCE_FEATURES),
            "scalar_features": list(SCALAR_FEATURES),
            "candidate_features": list(CANDIDATE_FEATURES),
            "quantile_keys": list(QUANTILE_KEYS),
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


def profile_by_name(name: str) -> SpcTrainingProfile:
    key = str(name).strip()
    if key not in SPC_TRAINING_PROFILES:
        raise SpcTrainingError("unknown spc_abr_v1 training profile: {0}".format(name))
    return SPC_TRAINING_PROFILES[key]


def train_spc_abr_v1(
    dataset_dir: object,
    output_dir: object,
    *,
    profile: SpcTrainingProfile,
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
    _emit_progress(progress_callback, "preparing", "Preparando entrenamiento spc_abr_v1")
    data_path = ensure_existing_dir(dataset_dir, purpose="phase45_v1 dataset")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="spc_abr_v1 model")
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
    training_examples = load_spc_examples(data_path / DATA_FILENAMES[TRAINING_ROLE], TRAINING_ROLE, limit=train_limit)
    validation_examples = load_spc_examples(data_path / DATA_FILENAMES[VALIDATION_ROLE], VALIDATION_ROLE, limit=val_limit)
    if not training_examples or not validation_examples:
        raise SpcTrainingError("spc_abr_v1 training requires training and validation examples")
    _emit_progress(
        progress_callback,
        "examples_loaded",
        "Muestras cargadas",
        training_samples=len(training_examples),
        validation_samples=len(validation_examples),
    )
    normalization = fit_spc_normalization(training_examples)
    train_tensors = examples_to_tensors(training_examples, normalization)
    validation_tensors = examples_to_tensors(validation_examples, normalization)

    model = SpcAbrV1Predictor(
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
        validation_metrics = evaluate_spc_model(
            model,
            validation_loader,
            device=selected_device,
            profile=profile,
            examples=validation_examples,
        )
        epoch_report = {
            "epoch": epoch,
            "training_loss": train_metrics["loss"],
            "training_quantile_loss": train_metrics["quantile_loss"],
            "training_capacity_loss": train_metrics["capacity_loss"],
            "training_risk_loss": train_metrics["risk_loss"],
            "validation_loss": validation_metrics["loss"],
            "validation_p50_mae_kbps": validation_metrics["p50_mae_kbps"],
            "validation_capacity_mae_kbps": validation_metrics["capacity_mae_kbps"],
            "validation_risk_brier": validation_metrics["risk_brier"],
        }
        epoch_reports.append(epoch_report)
        is_best = float(validation_metrics["loss"]) < best_validation_loss
        if float(validation_metrics["loss"]) < best_validation_loss:
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
            validation_p50_mae_kbps=validation_metrics["p50_mae_kbps"],
            validation_capacity_mae_kbps=validation_metrics["capacity_mae_kbps"],
            validation_risk_brier=validation_metrics["risk_brier"],
            best_epoch=best_epoch,
            best_so_far=is_best,
        )

    if best_state_dict is not None:
        model.load_state_dict(best_state_dict)
    _emit_progress(progress_callback, "final_evaluation_started", "Calculando metricas finales")
    final_training_metrics = evaluate_spc_model(
        model,
        train_eval_loader,
        device=selected_device,
        profile=profile,
        examples=training_examples,
    )
    final_validation_metrics = evaluate_spc_model(
        model,
        validation_loader,
        device=selected_device,
        profile=profile,
        examples=validation_examples,
    )
    model_config = dict(model.config())
    normalization_payload = normalization.to_json()
    checkpoint_path = output_path / SPC_MODEL_FILENAME
    config_path = output_path / SPC_MODEL_CONFIG_FILENAME
    normalization_path = output_path / SPC_NORMALIZATION_FILENAME
    report_path = output_path / SPC_TRAINING_REPORT_FILENAME
    checkpoint = {
        "schema_id": SPC_CHECKPOINT_SCHEMA_ID,
        "model_key": "spc_abr_v1",
        "model_state_dict": model.state_dict(),
        "model_config": model_config,
        "normalization": normalization_payload,
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
        "schema_id": SPC_TRAINING_REPORT_SCHEMA_ID,
        "human_readable_name": "Entrenamiento offline de spc_abr_v1",
        "phase": "fase_4_5_v1_bloque4_entrenamiento_spc_abr_v1",
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
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
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
        "Entrenamiento spc_abr_v1 finalizado",
        training_duration_s=duration_s,
        output_dir=str(output_path),
        best_epoch=best_epoch,
    )
    return report


def load_spc_examples(path: object, data_role: str, limit: int | None = None) -> tuple[SpcExample, ...]:
    examples = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                raw = json.loads(text)
            except json.JSONDecodeError as exc:
                raise SpcTrainingError("{0}: invalid JSONL line {1}".format(path, line_number)) from exc
            examples.append(_example_from_sample(raw, data_role, line_number))
            if limit is not None and len(examples) >= int(limit):
                break
    return tuple(examples)


def fit_spc_normalization(examples: Sequence[SpcExample]) -> SpcNormalizationStats:
    if not examples:
        raise SpcTrainingError("normalization requires training examples")
    sequence_rows = [step for example in examples for step in example.sequence]
    scalar_rows = [example.scalars for example in examples]
    candidate_rows = [candidate for example in examples for candidate in example.candidates]
    return SpcNormalizationStats(
        schema_id="phase45_v1_spc_abr_normalization_v1",
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
    examples: Sequence[SpcExample],
    normalization: SpcNormalizationStats,
) -> tuple[torch.Tensor, ...]:
    if not examples:
        raise SpcTrainingError("examples_to_tensors requires examples")
    max_candidates = max(len(example.candidates) for example in examples)
    sequence_rows = []
    scalar_rows = []
    candidate_rows = []
    mask_rows = []
    quantile_targets = []
    capacity_targets = []
    risk_targets = []
    for example in examples:
        sequence_rows.append(_normalize_matrix(example.sequence, normalization.sequence_mean, normalization.sequence_std))
        scalar_rows.append(_normalize_vector(example.scalars, normalization.scalar_mean, normalization.scalar_std))
        candidates = [_normalize_vector(candidate, normalization.candidate_mean, normalization.candidate_std) for candidate in example.candidates]
        mask = [bool(value) for value in example.action_mask]
        risks = [float(value) for value in example.risk_targets]
        while len(candidates) < max_candidates:
            candidates.append([0.0 for _ in CANDIDATE_FEATURES])
            mask.append(False)
            risks.append(0.0)
        candidate_rows.append(candidates)
        mask_rows.append(mask)
        risk_targets.append(risks)
        quantile_targets.append(list(example.quantile_log_targets))
        capacity_targets.append(example.capacity_log_target)
    return (
        torch.tensor(sequence_rows, dtype=torch.float32),
        torch.tensor(scalar_rows, dtype=torch.float32),
        torch.tensor(candidate_rows, dtype=torch.float32),
        torch.tensor(mask_rows, dtype=torch.bool),
        torch.tensor(quantile_targets, dtype=torch.float32),
        torch.tensor(capacity_targets, dtype=torch.float32),
        torch.tensor(risk_targets, dtype=torch.float32),
    )


def evaluate_spc_model(
    model: SpcAbrV1Predictor,
    loader: DataLoader,
    *,
    device: torch.device,
    profile: SpcTrainingProfile,
    examples: Sequence[SpcExample],
) -> Mapping[str, object]:
    model.eval()
    totals = _MetricTotals()
    predictions_by_bucket: dict[str, _MetricTotals] = defaultdict(_MetricTotals)
    start_index = 0
    with torch.no_grad():
        for batch in loader:
            moved = _move_batch(batch, device)
            outputs = model(moved[0], moved[1], moved[2], moved[3])
            losses = _loss_components(outputs, moved, profile)
            batch_metrics = _batch_metrics(outputs, moved)
            batch_size = int(moved[0].shape[0])
            totals.add(batch_metrics, losses, batch_size)
            for row_offset in range(batch_size):
                example = examples[start_index + row_offset]
                single = _single_row_metrics(outputs, moved, row_offset)
                predictions_by_bucket[example.throughput_bucket].add(single, {}, 1)
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
        raise SpcTrainingError("CUDA/ROCm device requested but torch.cuda.is_available() is false")
    if key not in {"cpu", "cuda"}:
        raise SpcTrainingError("device must be cpu, cuda or auto")
    return torch.device(key)


def set_training_seed(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(seed))


def _run_epoch(
    model: SpcAbrV1Predictor,
    loader: DataLoader,
    *,
    device: torch.device,
    optimizer: torch.optim.Optimizer,
    profile: SpcTrainingProfile,
    progress_callback: Callable[[Mapping[str, object]], None] | None = None,
    epoch: int | None = None,
    epochs: int | None = None,
) -> Mapping[str, float]:
    model.train()
    totals = _MetricTotals()
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
        totals.add({}, losses, batch_size)
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
    return totals.to_json(metrics_only=False)


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


def _loss_components(
    outputs: Mapping[str, torch.Tensor],
    batch: Sequence[torch.Tensor],
    profile: SpcTrainingProfile,
) -> dict[str, torch.Tensor]:
    mask = batch[3].to(dtype=torch.bool)
    quantile_targets = batch[4]
    capacity_targets = batch[5]
    risk_targets = batch[6]
    quantile_loss = _pinball_loss(outputs["quantile_log_kbps"], quantile_targets)
    capacity_loss = F.smooth_l1_loss(outputs["capacity_log_kbps"], capacity_targets)
    risk_loss_raw = F.binary_cross_entropy_with_logits(outputs["risk_logits"], risk_targets, reduction="none")
    risk_loss = risk_loss_raw.masked_select(mask).mean()
    loss = (
        profile.quantile_loss_weight * quantile_loss
        + profile.capacity_loss_weight * capacity_loss
        + profile.risk_loss_weight * risk_loss
    )
    return {
        "loss_tensor": loss,
        "loss": loss.detach(),
        "quantile_loss": quantile_loss.detach(),
        "capacity_loss": capacity_loss.detach(),
        "risk_loss": risk_loss.detach(),
    }


def _pinball_loss(predictions: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    quantiles = torch.tensor(QUANTILE_VALUES, dtype=predictions.dtype, device=predictions.device).view(1, -1)
    errors = targets - predictions
    return torch.maximum(quantiles * errors, (quantiles - 1.0) * errors).mean()


def _batch_metrics(outputs: Mapping[str, torch.Tensor], batch: Sequence[torch.Tensor]) -> Mapping[str, float]:
    predictions = _decoded_predictions(outputs)
    targets = _decoded_targets(batch)
    risk_probs = torch.sigmoid(outputs["risk_logits"])
    mask = batch[3].to(dtype=torch.bool)
    risk_targets = batch[6]
    return _metric_values(predictions, targets, risk_probs, risk_targets, mask)


def _single_row_metrics(
    outputs: Mapping[str, torch.Tensor],
    batch: Sequence[torch.Tensor],
    row_index: int,
) -> Mapping[str, float]:
    sliced_outputs = {name: value[row_index : row_index + 1] for name, value in outputs.items()}
    sliced_batch = tuple(value[row_index : row_index + 1] for value in batch)
    return _batch_metrics(sliced_outputs, sliced_batch)


def _decoded_predictions(outputs: Mapping[str, torch.Tensor]) -> Mapping[str, torch.Tensor]:
    quantiles = torch.expm1(outputs["quantile_log_kbps"]).clamp(min=0.0)
    capacity = torch.expm1(outputs["capacity_log_kbps"]).clamp(min=0.0)
    return {
        "p10": quantiles[:, 0],
        "p25": quantiles[:, 1],
        "p50": quantiles[:, 2],
        "capacity": capacity,
    }


def _decoded_targets(batch: Sequence[torch.Tensor]) -> Mapping[str, torch.Tensor]:
    quantiles = torch.expm1(batch[4]).clamp(min=0.0)
    capacity = torch.expm1(batch[5]).clamp(min=0.0)
    return {
        "p10": quantiles[:, 0],
        "p25": quantiles[:, 1],
        "p50": quantiles[:, 2],
        "capacity": capacity,
    }


def _metric_values(
    predictions: Mapping[str, torch.Tensor],
    targets: Mapping[str, torch.Tensor],
    risk_probs: torch.Tensor,
    risk_targets: torch.Tensor,
    mask: torch.Tensor,
) -> Mapping[str, float]:
    risk_pred = risk_probs >= 0.5
    risk_true = risk_targets >= 0.5
    valid_probs = risk_probs.masked_select(mask)
    valid_targets = risk_targets.masked_select(mask)
    valid_pred = risk_pred.masked_select(mask)
    valid_true = risk_true.masked_select(mask)
    positives = valid_true.sum().item()
    false_negatives = ((~valid_pred) & valid_true).sum().item()
    return {
        "p10_mae_kbps": float(torch.mean(torch.abs(predictions["p10"] - targets["p10"])).detach().cpu().item()),
        "p25_mae_kbps": float(torch.mean(torch.abs(predictions["p25"] - targets["p25"])).detach().cpu().item()),
        "p50_mae_kbps": float(torch.mean(torch.abs(predictions["p50"] - targets["p50"])).detach().cpu().item()),
        "capacity_mae_kbps": float(
            torch.mean(torch.abs(predictions["capacity"] - targets["capacity"])).detach().cpu().item()
        ),
        "p10_label_coverage": float(torch.mean((targets["p10"] <= predictions["p10"]).to(torch.float32)).detach().cpu().item()),
        "p25_label_coverage": float(torch.mean((targets["p25"] <= predictions["p25"]).to(torch.float32)).detach().cpu().item()),
        "p50_label_coverage": float(torch.mean((targets["p50"] <= predictions["p50"]).to(torch.float32)).detach().cpu().item()),
        "risk_brier": float(torch.mean((valid_probs - valid_targets) ** 2).detach().cpu().item()),
        "risk_accuracy": float(torch.mean((valid_pred == valid_true).to(torch.float32)).detach().cpu().item()),
        "risk_false_negative_rate": float(false_negatives / positives) if positives else 0.0,
    }


@dataclass
class _MetricTotals:
    weight: int = 0
    losses: dict[str, float] | None = None
    metrics: dict[str, float] | None = None

    def __post_init__(self) -> None:
        self.losses = defaultdict(float)
        self.metrics = defaultdict(float)

    def add(self, metrics: Mapping[str, float], losses: Mapping[str, object], batch_size: int) -> None:
        self.weight += int(batch_size)
        for name in ("loss", "quantile_loss", "capacity_loss", "risk_loss"):
            if name in losses:
                value = losses[name]
                if hasattr(value, "detach"):
                    numeric = float(value.detach().cpu().item())  # type: ignore[union-attr]
                else:
                    numeric = float(value)
                self.losses[name] += numeric * float(batch_size)
        for name, value in metrics.items():
            self.metrics[name] += float(value) * float(batch_size)

    def to_json(self, *, include_losses: bool = True, metrics_only: bool = True) -> dict[str, float]:
        denominator = max(float(self.weight), 1.0)
        payload = {}
        if include_losses:
            payload.update({name: round(value / denominator, 9) for name, value in sorted(self.losses.items())})
        if metrics_only or self.metrics:
            payload.update({name: round(value / denominator, 6) for name, value in sorted(self.metrics.items())})
        payload["sample_count"] = int(self.weight)
        return payload


def _move_batch(batch: Sequence[torch.Tensor], device: torch.device) -> tuple[torch.Tensor, ...]:
    return tuple(tensor.to(device) for tensor in batch)


def _example_from_sample(sample: Mapping[str, object], expected_role: str, line_number: int) -> SpcExample:
    if sample.get("data_role") != expected_role:
        raise SpcTrainingError("line {0}: data_role mismatch".format(line_number))
    model_inputs = _require_mapping(sample.get("model_inputs"), "model_inputs")
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidates_raw = model_inputs.get("candidates")
    action_mask_raw = model_inputs.get("action_mask")
    if not isinstance(candidates_raw, list) or not isinstance(action_mask_raw, list):
        raise SpcTrainingError("line {0}: candidates/action_mask must be lists".format(line_number))
    spc_targets = _require_mapping(sample.get("spc_targets"), "spc_targets")
    if spc_targets.get("target_id") != SPC_TARGET_ID:
        raise SpcTrainingError("line {0}: unexpected spc target id".format(line_number))
    future = _require_mapping(spc_targets.get("future_throughput_kbps"), "future_throughput_kbps")
    per_candidate = spc_targets.get("per_candidate_download_risk")
    if not isinstance(per_candidate, list):
        raise SpcTrainingError("line {0}: per_candidate_download_risk must be a list".format(line_number))
    sequence = _sequence_from_context(context)
    scalars = tuple(_finite_number(context.get(name), name) for name in SCALAR_FEATURES)
    candidates = tuple(
        tuple(_finite_number(_require_mapping(candidate, "candidate").get(name), name) for name in CANDIDATE_FEATURES)
        for candidate in candidates_raw
    )
    action_mask = tuple(bool(value) for value in action_mask_raw)
    risk_targets = tuple(_risk_target_for_candidate(item, index) for index, item in enumerate(per_candidate))
    if len(candidates) != len(action_mask) or len(candidates) != len(risk_targets):
        raise SpcTrainingError("line {0}: candidates, mask and risk targets length mismatch".format(line_number))
    quantiles = tuple(_log_kbps(future[key]) for key in QUANTILE_KEYS)
    capacity = _log_kbps(spc_targets.get("conservative_capacity_kbps"))
    metadata = _require_mapping(sample.get("metadata"), "metadata")
    return SpcExample(
        sequence=sequence,
        scalars=scalars,
        candidates=candidates,
        action_mask=action_mask,
        quantile_log_targets=quantiles,  # type: ignore[arg-type]
        capacity_log_target=capacity,
        risk_targets=risk_targets,
        data_role=expected_role,
        throughput_bucket=str(metadata.get("throughput_bucket", "unknown")),
        synthetic=bool(metadata.get("synthetic") is True),
    )


def _sequence_from_context(context: Mapping[str, object]) -> tuple[tuple[float, float], ...]:
    throughput = _numeric_sequence(context.get("throughput_history_bps"), "throughput_history_bps")
    download = _numeric_sequence(context.get("download_time_history_s"), "download_time_history_s")
    if len(throughput) != len(download):
        raise SpcTrainingError("history feature lengths differ")
    return tuple((throughput[index], download[index]) for index in range(len(throughput)))


def _risk_target_for_candidate(item: object, index: int) -> float:
    mapping = _require_mapping(item, "risk candidate {0}".format(index))
    risk = _finite_number(mapping.get("rebuffer_risk"), "rebuffer_risk")
    return 1.0 if risk >= 0.5 else 0.0


def _numeric_sequence(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise SpcTrainingError("{0} must be a sequence".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SpcTrainingError("{0} must be an object".format(name))
    return value


def _finite_number(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise SpcTrainingError("{0} must be numeric".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise SpcTrainingError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(parsed):
        raise SpcTrainingError("{0} must be finite".format(name))
    return parsed


def _log_kbps(value: object) -> float:
    return float(math.log1p(max(_finite_number(value, "throughput target"), 0.0)))


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
        raise SpcTrainingError("normalization rows must not be empty")
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise SpcTrainingError("normalization row width changed")
    return width


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> list[float]:
    if len(values) != len(mean) or len(mean) != len(std):
        raise SpcTrainingError("normalization vector width mismatch")
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
        raise SpcTrainingError("epochs and batch_size must be positive")
    if not math.isfinite(float(learning_rate)) or float(learning_rate) <= 0.0:
        raise SpcTrainingError("learning_rate must be finite and positive")
    for name, value in (("max_training_samples", max_training_samples), ("max_validation_samples", max_validation_samples)):
        if value is not None and int(value) <= 0:
            raise SpcTrainingError("{0} must be positive when provided".format(name))


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
