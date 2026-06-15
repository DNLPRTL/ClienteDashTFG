from __future__ import annotations

import hashlib
import math
import random
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import torch
from torch.utils.data import DataLoader, TensorDataset

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_jsonl, write_json
from core.neural_abr.constants import CONTEXT_VECTOR_NAMES
from core.neural_abr.features import flatten_context_features
from core.phase45_v3.constants import MEDIA_PROFILE_ID, REWARD_VERSION, TRAINING_ROLE, VALIDATION_ROLE
from core.phase45_v3.throughput_quantile_dataset import (
    THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME,
    THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME,
    THROUGHPUT_QUANTILE_TARGET_ID,
    validate_phase45_v3_throughput_quantile_dataset_dir,
)
from core.phase45_v3.throughput_quantile_model import (
    PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
    ThroughputQuantilePredictor,
    quantile_crossing_penalty,
    throughput_quantile_loss,
)


THROUGHPUT_QUANTILE_CHECKPOINT_SCHEMA_ID = "phase45_v3_throughput_quantile_checkpoint_v1"
THROUGHPUT_QUANTILE_TRAINING_REPORT_SCHEMA_ID = "phase45_v3_throughput_quantile_training_report_v1"
THROUGHPUT_QUANTILE_NORMALIZATION_SCHEMA_ID = "phase45_v3_throughput_quantile_normalization_v1"

THROUGHPUT_QUANTILE_MODEL_FILENAME = "modelo_phase45_v3_throughput_quantile.pt"
THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME = "configuracion_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME = "normalizacion_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_phase45_v3_throughput_quantile.json"


class Phase45V3NeuralMpcTrainingError(ValueError):
    """Raised when throughput-quantile predictor training cannot proceed."""


@dataclass(frozen=True)
class ThroughputQuantileTrainingProfile:
    name: str
    epochs: int
    batch_size: int
    learning_rate: float
    hidden_sizes: tuple[int, ...]
    quantiles: tuple[float, ...]
    horizon_segments: int
    pinball_loss_weight: float = 1.0
    quantile_crossing_loss_weight: float = 0.10
    temporal_smoothness_loss_weight: float = 0.05
    max_training_samples: int | None = None
    max_validation_samples: int | None = None
    seed: int = 451001

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "learning_rate": self.learning_rate,
            "hidden_sizes": list(self.hidden_sizes),
            "quantiles": list(self.quantiles),
            "horizon_segments": self.horizon_segments,
            "pinball_loss_weight": self.pinball_loss_weight,
            "quantile_crossing_loss_weight": self.quantile_crossing_loss_weight,
            "temporal_smoothness_loss_weight": self.temporal_smoothness_loss_weight,
            "max_training_samples": self.max_training_samples,
            "max_validation_samples": self.max_validation_samples,
            "seed": self.seed,
        }


THROUGHPUT_QUANTILE_TRAINING_PROFILES: dict[str, ThroughputQuantileTrainingProfile] = {
    "smoke": ThroughputQuantileTrainingProfile(
        name="smoke",
        epochs=1,
        batch_size=64,
        learning_rate=1.0e-3,
        hidden_sizes=(64, 32),
        quantiles=(0.10, 0.25, 0.50, 0.75),
        horizon_segments=5,
        max_training_samples=512,
        max_validation_samples=256,
        seed=451011,
    ),
    "pilot": ThroughputQuantileTrainingProfile(
        name="pilot",
        epochs=40,
        batch_size=1024,
        learning_rate=3.0e-4,
        hidden_sizes=(256, 128, 64),
        quantiles=(0.10, 0.25, 0.50, 0.75),
        horizon_segments=5,
        seed=451001,
    ),
    "full_v1": ThroughputQuantileTrainingProfile(
        name="full_v1",
        epochs=60,
        batch_size=2048,
        learning_rate=3.0e-4,
        hidden_sizes=(256, 128, 64),
        quantiles=(0.10, 0.25, 0.50, 0.75),
        horizon_segments=5,
        seed=452001,
    ),
}


@dataclass(frozen=True)
class ThroughputQuantileNormalization:
    schema_id: str
    context_mean: tuple[float, ...]
    context_std: tuple[float, ...]
    fitted_on_data_role: str = TRAINING_ROLE

    def to_json(self) -> dict[str, object]:
        return {
            "schema_id": self.schema_id,
            "fitted_on_data_role": self.fitted_on_data_role,
            "context_feature_names": list(CONTEXT_VECTOR_NAMES),
            "context_mean": list(self.context_mean),
            "context_std": list(self.context_std),
        }


def throughput_quantile_training_profile_by_name(name: str) -> ThroughputQuantileTrainingProfile:
    key = str(name).strip()
    if key not in THROUGHPUT_QUANTILE_TRAINING_PROFILES:
        raise Phase45V3NeuralMpcTrainingError("unknown throughput quantile training profile: {0}".format(name))
    return THROUGHPUT_QUANTILE_TRAINING_PROFILES[key]


def train_phase45_v3_throughput_quantile_predictor(
    dataset_dir: object,
    output_dir: object,
    profile: ThroughputQuantileTrainingProfile,
    *,
    overwrite: bool = False,
    device: str | None = None,
) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(dataset_dir, purpose="phase45_v3 throughput quantile dataset")
    validation = validate_phase45_v3_throughput_quantile_dataset_dir(data_dir)
    if validation["status"] != "PASS":
        raise Phase45V3NeuralMpcTrainingError("dataset validation failed: {0}".format(validation["errors"]))
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 throughput quantile training")
    _seed_everything(profile.seed)
    active_device = _resolve_device(device)

    train_examples = load_throughput_quantile_examples(
        data_dir / THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME,
        TRAINING_ROLE,
        profile.max_training_samples,
        profile,
    )
    validation_examples = load_throughput_quantile_examples(
        data_dir / THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME,
        VALIDATION_ROLE,
        profile.max_validation_samples,
        profile,
    )
    normalization = fit_throughput_quantile_normalization(train_examples)
    train_tensors = throughput_quantile_examples_to_tensors(train_examples, normalization)
    validation_tensors = throughput_quantile_examples_to_tensors(validation_examples, normalization)

    model = ThroughputQuantilePredictor(
        input_dim=len(CONTEXT_VECTOR_NAMES),
        horizon_segments=int(profile.horizon_segments),
        quantiles=profile.quantiles,
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
    best_validation = math.inf
    started = time.time()
    for epoch in range(1, int(profile.epochs) + 1):
        model.train()
        train_losses = []
        train_parts: dict[str, float] = {}
        for batch in train_loader:
            context, target = tuple(tensor.to(active_device) for tensor in batch)
            prediction = model(context)
            loss, parts = throughput_quantile_loss(
                prediction,
                target,
                profile.quantiles,
                pinball_loss_weight=profile.pinball_loss_weight,
                quantile_crossing_loss_weight=profile.quantile_crossing_loss_weight,
                temporal_smoothness_loss_weight=profile.temporal_smoothness_loss_weight,
            )
            optimizer.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            optimizer.step()
            train_losses.append(float(loss.detach().cpu()))
            for name, value in parts.items():
                train_parts[name] = train_parts.get(name, 0.0) + float(value)
        validation_metrics = evaluate_throughput_quantile_predictor(
            model,
            validation_tensors,
            profile,
            active_device,
        )
        epoch_record = {
            "epoch": epoch,
            "train_loss_mean": round(sum(train_losses) / float(len(train_losses)), 6) if train_losses else 0.0,
            "train_loss_components": {
                name: round(value / float(max(len(train_losses), 1)), 6) for name, value in sorted(train_parts.items())
            },
            "validation": validation_metrics,
        }
        epochs.append(epoch_record)
        if float(validation_metrics["pinball_loss"]) < best_validation:
            best_validation = float(validation_metrics["pinball_loss"])
            best_state = {key: value.detach().cpu() for key, value in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    final_validation = evaluate_throughput_quantile_predictor(model, validation_tensors, profile, active_device)
    gates = _evaluate_training_gates(final_validation)
    checkpoint = {
        "schema_id": THROUGHPUT_QUANTILE_CHECKPOINT_SCHEMA_ID,
        "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "model_config": model.config(),
        "normalization": normalization.to_json(),
        "model_state_dict": model.state_dict(),
        "profile": profile.to_json(),
        "dataset_dir": str(data_dir),
    }
    model_path = output_path / THROUGHPUT_QUANTILE_MODEL_FILENAME
    torch.save(checkpoint, model_path)
    report = {
        "schema_id": THROUGHPUT_QUANTILE_TRAINING_REPORT_SCHEMA_ID,
        "status": "PASS" if not gates["failed"] else "REVIEW",
        "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
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
    write_json(output_path / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME, dict(model.config()))
    write_json(output_path / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME, normalization.to_json())
    write_json(output_path / THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME, report)
    return report


def load_throughput_quantile_examples(
    path: object,
    role: str,
    limit: int | None,
    profile: ThroughputQuantileTrainingProfile,
) -> tuple[Mapping[str, object], ...]:
    rows = list(read_jsonl(path))
    output = []
    for row in rows:
        if row.get("data_role") != role:
            raise Phase45V3NeuralMpcTrainingError("{0}: data_role mismatch".format(row.get("sample_id")))
        _sample_to_arrays(row, profile)
        output.append(row)
        if limit is not None and len(output) >= int(limit):
            break
    if not output:
        raise Phase45V3NeuralMpcTrainingError("no throughput quantile examples loaded from {0}".format(path))
    return tuple(output)


def fit_throughput_quantile_normalization(
    examples: Sequence[Mapping[str, object]],
) -> ThroughputQuantileNormalization:
    contexts = []
    for example in examples:
        context, _target = _sample_to_arrays(example, None)
        contexts.append(context)
    mean, std = _mean_std_rows(contexts)
    return ThroughputQuantileNormalization(
        schema_id=THROUGHPUT_QUANTILE_NORMALIZATION_SCHEMA_ID,
        context_mean=mean,
        context_std=std,
    )


def throughput_quantile_examples_to_tensors(
    examples: Sequence[Mapping[str, object]],
    normalization: ThroughputQuantileNormalization,
) -> tuple[torch.Tensor, torch.Tensor]:
    contexts = []
    targets = []
    for example in examples:
        context, target = _sample_to_arrays(example, None)
        contexts.append(_normalize_vector(context, normalization.context_mean, normalization.context_std))
        targets.append(target)
    return (
        torch.tensor(contexts, dtype=torch.float32),
        torch.tensor(targets, dtype=torch.float32),
    )


def evaluate_throughput_quantile_predictor(
    model: ThroughputQuantilePredictor,
    tensors: tuple[torch.Tensor, torch.Tensor],
    profile: ThroughputQuantileTrainingProfile,
    device: torch.device,
) -> Mapping[str, object]:
    model.eval()
    context, target = tuple(tensor.to(device) for tensor in tensors)
    with torch.no_grad():
        prediction = model(context)
        loss, parts = throughput_quantile_loss(
            prediction,
            target,
            profile.quantiles,
            pinball_loss_weight=profile.pinball_loss_weight,
            quantile_crossing_loss_weight=profile.quantile_crossing_loss_weight,
            temporal_smoothness_loss_weight=profile.temporal_smoothness_loss_weight,
        )
        median_index = _nearest_quantile_index(profile.quantiles, 0.50)
        median_error = torch.abs(prediction[:, :, median_index] - target)
        crossing = quantile_crossing_penalty(prediction)
    return {
        "loss": round(float(loss.detach().cpu()), 6),
        "pinball_loss": round(float(parts["pinball_loss"]), 6),
        "quantile_crossing_loss": round(float(crossing.detach().cpu()), 6),
        "median_abs_log_ratio_error_mean": round(float(median_error.mean().detach().cpu()), 6),
        "median_abs_log_ratio_error_p95": round(_tensor_quantile(median_error, 0.95), 6),
        "sample_count": int(context.shape[0]),
        "horizon_segments": int(profile.horizon_segments),
        "quantiles": list(profile.quantiles),
    }


def _sample_to_arrays(
    sample: Mapping[str, object],
    profile: ThroughputQuantileTrainingProfile | None,
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    model_inputs = sample.get("model_inputs")
    targets = sample.get("throughput_quantile_targets")
    if not isinstance(model_inputs, Mapping) or not isinstance(targets, Mapping):
        raise Phase45V3NeuralMpcTrainingError("invalid throughput quantile sample shape")
    if targets.get("target_id") != THROUGHPUT_QUANTILE_TARGET_ID:
        raise Phase45V3NeuralMpcTrainingError("unexpected throughput quantile target id")
    context = flatten_context_features(model_inputs.get("context"))  # type: ignore[arg-type]
    target_log_ratio = tuple(float(value) for value in targets.get("target_log_ratio_by_horizon", ()))
    if not target_log_ratio or any(not math.isfinite(value) for value in target_log_ratio):
        raise Phase45V3NeuralMpcTrainingError("target_log_ratio_by_horizon must be finite")
    if profile is not None:
        if len(target_log_ratio) != int(profile.horizon_segments):
            raise Phase45V3NeuralMpcTrainingError("sample horizon does not match training profile")
        sample_quantiles = tuple(float(value) for value in targets.get("quantiles", ()))
        if sample_quantiles != tuple(float(value) for value in profile.quantiles):
            raise Phase45V3NeuralMpcTrainingError("sample quantiles do not match training profile")
    return context, target_log_ratio


def _evaluate_training_gates(metrics: Mapping[str, object]) -> Mapping[str, object]:
    gates = {
        "finite_validation_loss": {
            "passed": math.isfinite(float(metrics["loss"])),
            "observed": metrics["loss"],
            "threshold": "finite",
        },
        "finite_median_abs_log_ratio_error": {
            "passed": math.isfinite(float(metrics["median_abs_log_ratio_error_mean"])),
            "observed": metrics["median_abs_log_ratio_error_mean"],
            "threshold": "finite",
        },
    }
    failed = [name for name, gate in gates.items() if not gate["passed"]]
    return {"failed": failed, "gates": gates}


def _nearest_quantile_index(quantiles: Sequence[float], target: float) -> int:
    values = tuple(float(value) for value in quantiles)
    return min(range(len(values)), key=lambda index: abs(values[index] - float(target)))


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
        raise Phase45V3NeuralMpcTrainingError("normalization rows must not be empty")
    width = len(rows[0])
    columns = [[float(row[index]) for row in rows] for index in range(width)]
    means = []
    stds = []
    for column in columns:
        mean = sum(column) / float(len(column))
        variance = sum((value - mean) ** 2 for value in column) / float(len(column))
        std = math.sqrt(max(variance, 0.0))
        means.append(float(mean))
        stds.append(float(std if std > 1.0e-9 else 1.0))
    return tuple(means), tuple(stds)


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> tuple[float, ...]:
    return tuple((float(value) - float(mean[index])) / max(float(std[index]), 1.0e-9) for index, value in enumerate(values))


def _tensor_quantile(values: torch.Tensor, q: float) -> float:
    if values.numel() == 0:
        return 0.0
    ordered = torch.sort(values.detach().flatten().to("cpu", dtype=torch.float32)).values
    index = min(max(int(round(float(q) * (int(ordered.numel()) - 1))), 0), int(ordered.numel()) - 1)
    return float(ordered[index])


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
