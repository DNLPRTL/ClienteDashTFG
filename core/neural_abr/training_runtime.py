from __future__ import annotations

import random
from collections import Counter
from typing import Mapping, Sequence

import torch

from core.neural_abr.model import NeuralAbrLiteCandidateScorer, predict_actions
from core.neural_abr.normalization import FeatureNormalizer


class TrainingRuntimeError(ValueError):
    """Raised when shared training runtime helpers receive invalid input."""


def set_training_determinism(seed: int) -> None:
    random.seed(int(seed))
    torch.manual_seed(int(seed))
    torch.use_deterministic_algorithms(True)


def batch_to_tensors(samples: Sequence[Mapping[str, object]], normalizer: FeatureNormalizer) -> Mapping[str, torch.Tensor]:
    if not samples:
        raise TrainingRuntimeError("batch_to_tensors requires at least one sample")
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


def evaluate_candidate_scorer(
    model: NeuralAbrLiteCandidateScorer,
    normalizer: FeatureNormalizer,
    samples: Sequence[Mapping[str, object]],
    batch_size: int,
) -> Mapping[str, object]:
    if not samples:
        return {
            "sample_count": 0,
            "valid_action_rate": 0.0,
            "teacher_agreement": 0.0,
            "prediction_distribution": {},
            "teacher_distribution": {},
            "invalid_prediction_count": 0,
        }
    model.eval()
    valid_count = 0
    agreement_count = 0
    invalid_prediction_count = 0
    prediction_counts: Counter[str] = Counter()
    teacher_counts: Counter[str] = Counter()
    with torch.no_grad():
        for start in range(0, len(samples), int(batch_size)):
            batch = samples[start : start + int(batch_size)]
            tensors = batch_to_tensors(batch, normalizer)
            scores = model(tensors["context"], tensors["candidates"], tensors["mask"])
            predictions = predict_actions(scores)
            for row_index, action in enumerate(predictions.tolist()):
                action_as_int = int(action)
                teacher_action = int(tensors["labels"][row_index].item())
                if bool(tensors["mask"][row_index, action_as_int]):
                    valid_count += 1
                else:
                    invalid_prediction_count += 1
                if action_as_int == teacher_action:
                    agreement_count += 1
                prediction_counts[str(action_as_int)] += 1
                teacher_counts[str(teacher_action)] += 1
    model.train()
    return {
        "sample_count": len(samples),
        "valid_action_rate": valid_count / float(len(samples)),
        "teacher_agreement": agreement_count / float(len(samples)),
        "prediction_distribution": dict(sorted(prediction_counts.items())),
        "teacher_distribution": dict(sorted(teacher_counts.items())),
        "invalid_prediction_count": invalid_prediction_count,
    }
