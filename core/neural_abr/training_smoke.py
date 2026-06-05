from __future__ import annotations

import random
from pathlib import Path
from typing import Mapping, Sequence

import torch

from core.neural_abr.artifacts import ensure_existing_dir, read_jsonl, write_json
from core.neural_abr.constants import (
    DATA_FILENAMES,
    PHASE4_TRAINING_SMOKE_SCHEMA_ID,
    TRAINING_ROLE,
    TRAINING_SMOKE_REPORT_FILENAME,
    VALIDATION_ROLE,
)
from core.neural_abr.model import NeuralAbrLiteCandidateScorer, masked_cross_entropy, predict_actions
from core.neural_abr.normalization import FeatureNormalizer
from core.neural_abr.sample_schema import validate_sample


class TrainingSmokeError(ValueError):
    """Raised when the diagnostic training smoke cannot run."""


def run_phase4_training_smoke(
    training_data_dir: object,
    output_dir: object,
    epochs: int = 1,
    batch_size: int = 8,
    max_samples: int = 128,
    seed: int = 123,
    device: str = "cpu",
) -> Mapping[str, object]:
    if device != "cpu":
        raise TrainingSmokeError("Phase 4 diagnostic training smoke is CPU-only")
    if epochs <= 0 or batch_size <= 0 or max_samples <= 0:
        raise TrainingSmokeError("epochs, batch_size and max_samples must be positive")
    data_path = ensure_existing_dir(training_data_dir, purpose="phase4 training data")
    output_path = Path(output_dir).expanduser().resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    _set_determinism(seed)

    training_samples = tuple(read_jsonl(data_path / DATA_FILENAMES[TRAINING_ROLE], limit=max_samples))
    validation_samples = tuple(read_jsonl(data_path / DATA_FILENAMES[VALIDATION_ROLE], limit=max_samples))
    for sample in training_samples:
        validate_sample(sample, expected_role=TRAINING_ROLE)
    for sample in validation_samples:
        validate_sample(sample, expected_role=VALIDATION_ROLE)
    if not training_samples or not validation_samples:
        raise TrainingSmokeError("training smoke requires training and validation samples")

    normalizer = FeatureNormalizer.fit_training_only(training_samples)
    model = NeuralAbrLiteCandidateScorer()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    rng = random.Random(seed)
    losses = []
    for _epoch in range(int(epochs)):
        order = list(range(len(training_samples)))
        rng.shuffle(order)
        for start in range(0, len(order), int(batch_size)):
            batch = [training_samples[index] for index in order[start : start + int(batch_size)]]
            tensors = _batch_to_tensors(batch, normalizer)
            optimizer.zero_grad()
            scores = model(tensors["context"], tensors["candidates"], tensors["mask"])
            loss = masked_cross_entropy(scores, tensors["labels"], tensors["mask"])
            loss.backward()
            optimizer.step()
            losses.append(float(loss.detach().cpu().item()))

    training_metrics = _evaluate(model, normalizer, training_samples, batch_size)
    validation_metrics = _evaluate(model, normalizer, validation_samples, batch_size)
    report = {
        "schema_id": PHASE4_TRAINING_SMOKE_SCHEMA_ID,
        "human_readable_name": "Prueba rapida de entrenamiento diagnostica de NeuralABR-Lite",
        "status": "PASS",
        "device": "cpu",
        "epochs": int(epochs),
        "batch_size": int(batch_size),
        "max_samples_per_role": int(max_samples),
        "loss_last": losses[-1] if losses else None,
        "loss_mean": sum(losses) / len(losses) if losses else None,
        "training_metrics": training_metrics,
        "validation_metrics": validation_metrics,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": False,
        "formal_ia_training_performed": False,
        "diagnostic_training_smoke_performed": True,
        "candidate_model_created": False,
        "checkpoint_written": False,
    }
    write_json(output_path / TRAINING_SMOKE_REPORT_FILENAME, report)
    return report


def _evaluate(
    model: NeuralAbrLiteCandidateScorer,
    normalizer: FeatureNormalizer,
    samples: Sequence[Mapping[str, object]],
    batch_size: int,
) -> Mapping[str, object]:
    model.eval()
    valid_count = 0
    agreement_count = 0
    prediction_counts: dict[str, int] = {}
    with torch.no_grad():
        for start in range(0, len(samples), int(batch_size)):
            batch = samples[start : start + int(batch_size)]
            tensors = _batch_to_tensors(batch, normalizer)
            scores = model(tensors["context"], tensors["candidates"], tensors["mask"])
            predictions = predict_actions(scores)
            for row_index, action in enumerate(predictions.tolist()):
                if bool(tensors["mask"][row_index, action]):
                    valid_count += 1
                if int(action) == int(tensors["labels"][row_index].item()):
                    agreement_count += 1
                prediction_counts[str(int(action))] = prediction_counts.get(str(int(action)), 0) + 1
    model.train()
    return {
        "sample_count": len(samples),
        "valid_action_rate": valid_count / float(len(samples)),
        "teacher_agreement": agreement_count / float(len(samples)),
        "prediction_distribution": dict(sorted(prediction_counts.items())),
    }


def _batch_to_tensors(samples: Sequence[Mapping[str, object]], normalizer: FeatureNormalizer) -> Mapping[str, torch.Tensor]:
    max_candidates = max(len(sample["candidate_features"]) for sample in samples)  # type: ignore[arg-type]
    context_rows = []
    candidate_rows = []
    mask_rows = []
    labels = []
    for sample in samples:
        context_vector, candidate_vectors = normalizer.normalize_sample(sample)
        context_rows.append(context_vector)
        candidate_width = len(candidate_vectors[0])
        padded_candidates = [list(vector) for vector in candidate_vectors]
        padded_mask = [bool(value) for value in sample["action_mask"]]  # type: ignore[index]
        while len(padded_candidates) < max_candidates:
            padded_candidates.append([0.0 for _ in range(candidate_width)])
            padded_mask.append(False)
        candidate_rows.append(padded_candidates)
        mask_rows.append(padded_mask)
        labels.append(int(sample["label"]["teacher_action"]))  # type: ignore[index]
    return {
        "context": torch.tensor(context_rows, dtype=torch.float32),
        "candidates": torch.tensor(candidate_rows, dtype=torch.float32),
        "mask": torch.tensor(mask_rows, dtype=torch.bool),
        "labels": torch.tensor(labels, dtype=torch.long),
    }


def _set_determinism(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    torch.use_deterministic_algorithms(True)

