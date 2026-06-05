from __future__ import annotations

import hashlib
import math
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import torch

from core.neural_abr.artifacts import (
    ensure_existing_dir,
    prepare_output_dir,
    read_json,
    read_jsonl,
    write_json,
)
from core.neural_abr.constants import (
    CANDIDATE_MODEL_CONFIG_FILENAME,
    CANDIDATE_MODEL_FILENAME,
    DATA_FILENAMES,
    FORMAL_TRAINING_REPORT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_FORMAL_TRAINING_SCHEMA_ID,
    PRIMARY_TEACHER,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.neural_abr.model import NeuralAbrLiteCandidateScorer, masked_cross_entropy
from core.neural_abr.normalization import FeatureNormalizer, NormalizationStats
from core.neural_abr.sample_schema import validate_sample
from core.neural_abr.training_data_validation import validate_phase4_training_data_dir
from core.neural_abr.training_runtime import batch_to_tensors, evaluate_candidate_scorer, set_training_determinism


class CandidateModelTrainingError(ValueError):
    """Raised when formal Phase 4E training cannot run safely."""


def train_phase4_candidate_model(
    training_data_dir: object,
    output_dir: object,
    overwrite: bool = False,
    epochs: int = 20,
    batch_size: int = 64,
    learning_rate: float = 1e-3,
    seed: int = 40403,
    device: str = "cpu",
    max_training_samples: int | None = None,
    max_validation_samples: int | None = None,
    hidden_sizes: Sequence[int] = (32, 16),
    label_teacher: str = PRIMARY_TEACHER,
    phase_name: str = "phase4e_entrenamiento_modelo_candidato_offline",
    human_readable_name: str = "Entrenamiento formal offline del modelo candidato NeuralABR-Lite",
    feature_source: str = "phase4B_datos_para_entrenamiento",
) -> Mapping[str, object]:
    if device != "cpu":
        raise CandidateModelTrainingError("Phase 4E formal training is CPU-only")
    if epochs <= 0 or batch_size <= 0:
        raise CandidateModelTrainingError("epochs and batch_size must be positive")
    if not math.isfinite(float(learning_rate)) or float(learning_rate) <= 0.0:
        raise CandidateModelTrainingError("learning_rate must be finite and positive")
    _validate_optional_sample_limit(max_training_samples, "max_training_samples")
    _validate_optional_sample_limit(max_validation_samples, "max_validation_samples")

    data_path = ensure_existing_dir(training_data_dir, purpose="phase4 training data")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase4 candidate model")
    data_validation = validate_phase4_training_data_dir(data_path, allowed_teacher_policies=(label_teacher,))
    set_training_determinism(seed)

    training_samples = tuple(read_jsonl(data_path / DATA_FILENAMES[TRAINING_ROLE], limit=max_training_samples))
    validation_samples = tuple(read_jsonl(data_path / DATA_FILENAMES[VALIDATION_ROLE], limit=max_validation_samples))
    for sample in training_samples:
        validate_sample(sample, expected_role=TRAINING_ROLE, allowed_teacher_policies=(label_teacher,))
    for sample in validation_samples:
        validate_sample(sample, expected_role=VALIDATION_ROLE, allowed_teacher_policies=(label_teacher,))
    if not training_samples or not validation_samples:
        raise CandidateModelTrainingError("formal training requires training and validation samples")

    normalizer = FeatureNormalizer(NormalizationStats.from_json(read_json(data_path / NORMALIZATION_STATS_FILENAME)))
    model = NeuralAbrLiteCandidateScorer(hidden_sizes=tuple(int(value) for value in hidden_sizes))
    optimizer = torch.optim.Adam(model.parameters(), lr=float(learning_rate))
    rng = random.Random(int(seed))
    started = time.monotonic()
    loss_values = []
    loss_mean_by_epoch = []

    for _epoch in range(int(epochs)):
        order = list(range(len(training_samples)))
        rng.shuffle(order)
        epoch_losses = []
        model.train()
        for start in range(0, len(order), int(batch_size)):
            batch = [training_samples[index] for index in order[start : start + int(batch_size)]]
            tensors = batch_to_tensors(batch, normalizer)
            optimizer.zero_grad()
            scores = model(tensors["context"], tensors["candidates"], tensors["mask"])
            loss = masked_cross_entropy(scores, tensors["labels"], tensors["mask"])
            loss.backward()
            optimizer.step()
            loss_value = float(loss.detach().cpu().item())
            loss_values.append(loss_value)
            epoch_losses.append(loss_value)
        loss_mean_by_epoch.append(sum(epoch_losses) / len(epoch_losses) if epoch_losses else None)

    training_metrics = evaluate_candidate_scorer(model, normalizer, training_samples, batch_size=batch_size)
    validation_metrics = evaluate_candidate_scorer(model, normalizer, validation_samples, batch_size=batch_size)
    model_config = dict(model.config())
    normalization_stats = dict(normalizer.stats.to_json())
    model_config_path = output_path / CANDIDATE_MODEL_CONFIG_FILENAME
    normalization_path = output_path / NORMALIZATION_STATS_FILENAME
    checkpoint_path = output_path / CANDIDATE_MODEL_FILENAME
    report_path = output_path / FORMAL_TRAINING_REPORT_FILENAME

    write_json(model_config_path, model_config)
    write_json(normalization_path, normalization_stats)
    checkpoint = {
        "schema_id": PHASE4_FORMAL_TRAINING_SCHEMA_ID,
        "human_readable_name": "Modelo candidato NeuralABR-Lite entrenado offline",
        "model_family": "NeuralABR-Lite Candidate Scorer",
        "model_state_dict": model.state_dict(),
        "model_config": model_config,
        "normalization_stats_file": NORMALIZATION_STATS_FILENAME,
        "feature_source": str(feature_source),
        "teacher_policy": str(label_teacher),
        "seed": int(seed),
        "device": "cpu",
    }
    torch.save(checkpoint, checkpoint_path)

    duration_s = time.monotonic() - started
    report = {
        "schema_id": PHASE4_FORMAL_TRAINING_SCHEMA_ID,
        "human_readable_name": human_readable_name,
        "phase": phase_name,
        "status": "PASS",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_training_data_dir": str(data_path),
        "source_data_validation": dict(data_validation),
        "output_dir": str(output_path),
        "device": "cpu",
        "seed": int(seed),
        "epochs": int(epochs),
        "batch_size": int(batch_size),
        "learning_rate": float(learning_rate),
        "hidden_sizes": [int(value) for value in hidden_sizes],
        "label_teacher": str(label_teacher),
        "max_training_samples": max_training_samples,
        "max_validation_samples": max_validation_samples,
        "sample_counts_used": {
            TRAINING_ROLE: len(training_samples),
            VALIDATION_ROLE: len(validation_samples),
        },
        "loss_last": loss_values[-1] if loss_values else None,
        "loss_mean": sum(loss_values) / len(loss_values) if loss_values else None,
        "loss_mean_by_epoch": loss_mean_by_epoch,
        "training_metrics": dict(training_metrics),
        "validation_metrics": dict(validation_metrics),
        "training_duration_s": duration_s,
        "files": {
            "checkpoint": CANDIDATE_MODEL_FILENAME,
            "model_config": CANDIDATE_MODEL_CONFIG_FILENAME,
            "normalization_stats": NORMALIZATION_STATS_FILENAME,
            "training_report": FORMAL_TRAINING_REPORT_FILENAME,
        },
        "artifacts": {
            "checkpoint": str(checkpoint_path),
            "checkpoint_sha256": _sha256_file(checkpoint_path),
            "model_config": str(model_config_path),
            "normalization_stats": str(normalization_path),
            "training_report": str(report_path),
        },
        "normalization_fitted_on": "training samples only",
        "metadata_fields_are_model_features": False,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": True,
        "formal_ia_training_performed": True,
        "diagnostic_training_smoke_performed": False,
        "candidate_model_created": True,
        "checkpoint_written": True,
        "export_bundle_created": False,
        "controller_registered": False,
        "controller_integrated": False,
        "qoe_improvement_claimed": False,
        "sota_claimed": False,
        "real_world_generalization_claimed": False,
    }
    write_json(report_path, report)
    return report


def load_phase4_candidate_model(model_dir: object) -> tuple[NeuralAbrLiteCandidateScorer, FeatureNormalizer, Mapping[str, object]]:
    model_path = ensure_existing_dir(model_dir, purpose="phase4 candidate model")
    checkpoint_path = model_path / CANDIDATE_MODEL_FILENAME
    if not checkpoint_path.is_file():
        raise CandidateModelTrainingError("candidate model checkpoint does not exist: {0}".format(checkpoint_path))
    checkpoint = _torch_load_cpu(checkpoint_path)
    if not isinstance(checkpoint, Mapping):
        raise CandidateModelTrainingError("candidate model checkpoint must be a mapping")
    config = checkpoint.get("model_config")
    if not isinstance(config, Mapping):
        config = read_json(model_path / CANDIDATE_MODEL_CONFIG_FILENAME)
    normalizer = FeatureNormalizer(NormalizationStats.from_json(read_json(model_path / NORMALIZATION_STATS_FILENAME)))
    model = NeuralAbrLiteCandidateScorer(
        context_dim=int(config.get("context_dim", 0) or 0) or None,
        candidate_dim=int(config.get("candidate_dim", 0) or 0) or None,
        hidden_sizes=tuple(int(value) for value in config.get("hidden_sizes", (32, 16))),  # type: ignore[arg-type]
    )
    state_dict = checkpoint.get("model_state_dict")
    if not isinstance(state_dict, Mapping):
        raise CandidateModelTrainingError("candidate model checkpoint has no model_state_dict")
    model.load_state_dict(state_dict)
    model.eval()
    return model, normalizer, checkpoint


def _validate_optional_sample_limit(value: int | None, name: str) -> None:
    if value is None:
        return
    if isinstance(value, bool) or int(value) <= 0:
        raise CandidateModelTrainingError("{0} must be positive when provided".format(name))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _torch_load_cpu(path: Path) -> object:
    try:
        return torch.load(path, map_location="cpu", weights_only=False)
    except TypeError:
        return torch.load(path, map_location="cpu")
