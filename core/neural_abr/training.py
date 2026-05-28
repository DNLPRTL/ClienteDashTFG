"""CPU-first training smoke for NeuralABR-Lite behavior cloning."""

from __future__ import annotations

import random
from pathlib import Path
from typing import Mapping, Sequence, Tuple

import torch

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_jsonl, write_json
from core.neural_abr.constants import DATASET_FILENAMES, TRAIN_SPLIT, TRAINING_REPORT_VERSION, VALIDATION_SPLIT
from core.neural_abr.model import NeuralAbrLiteCandidateScorer, masked_cross_entropy, predict_actions
from core.neural_abr.normalization import FeatureNormalizer
from core.neural_abr.schemas import validate_sample


class TrainingError(ValueError):
    """Raised when the training smoke cannot be run safely."""


def train_model(
    dataset_dir: object,
    output_dir: object,
    epochs: int = 1,
    batch_size: int = 8,
    seed: int = 123,
    device: str = "cpu",
    smoke: bool = False,
) -> Mapping[str, object]:
    if device != "cpu":
        raise TrainingError("Phase 4D training is CPU-first; use --device cpu")
    if epochs <= 0:
        raise TrainingError("epochs must be positive")
    if batch_size <= 0:
        raise TrainingError("batch_size must be positive")

    dataset_path = ensure_existing_dir(dataset_dir, purpose="dataset")
    output_path = prepare_output_dir(output_dir, overwrite=True, purpose="training run")
    _set_determinism(seed)

    train_samples = tuple(read_jsonl(dataset_path / DATASET_FILENAMES[TRAIN_SPLIT]))
    validation_samples = tuple(read_jsonl(dataset_path / DATASET_FILENAMES[VALIDATION_SPLIT]))
    for sample in train_samples:
        validate_sample(sample, expected_split=TRAIN_SPLIT)
    for sample in validation_samples:
        validate_sample(sample, expected_split=VALIDATION_SPLIT)

    normalizer = FeatureNormalizer.fit_train(train_samples)
    write_json(output_path / "normalization_stats.json", normalizer.stats.to_json())

    model = NeuralAbrLiteCandidateScorer()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    rng = random.Random(seed)
    losses = []
    for _epoch in range(int(epochs)):
        order = list(range(len(train_samples)))
        rng.shuffle(order)
        for start in range(0, len(order), int(batch_size)):
            batch = [train_samples[index] for index in order[start : start + int(batch_size)]]
            tensors = _batch_to_tensors(batch, normalizer)
            optimizer.zero_grad()
            scores = model(tensors["context"], tensors["candidates"], tensors["mask"])
            loss = masked_cross_entropy(scores, tensors["labels"], tensors["mask"])
            loss.backward()
            optimizer.step()
            losses.append(float(loss.detach().cpu().item()))

    train_metrics = evaluate_samples(model, normalizer, train_samples, batch_size=batch_size)
    validation_metrics = evaluate_samples(model, normalizer, validation_samples, batch_size=batch_size)

    checkpoint_path = output_path / "checkpoint.pt"
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "model_config": dict(model.config()),
            "normalization_stats_file": "normalization_stats.json",
            "seed": seed,
        },
        checkpoint_path,
    )
    write_json(output_path / "model_config.json", model.config())
    report = {
        "schema_version": TRAINING_REPORT_VERSION,
        "diagnostic_only": True,
        "not_benchmark": True,
        "smoke": bool(smoke),
        "device": "cpu",
        "seed": int(seed),
        "epochs": int(epochs),
        "batch_size": int(batch_size),
        "loss_last": losses[-1] if losses else None,
        "loss_mean": (sum(losses) / len(losses)) if losses else None,
        "train_metrics": train_metrics,
        "validation_metrics": validation_metrics,
        "artifacts": {
            "checkpoint": str(checkpoint_path),
            "normalization_stats": str(output_path / "normalization_stats.json"),
            "model_config": str(output_path / "model_config.json"),
        },
        "controller_registered": False,
    }
    write_json(output_path / "training_report.json", report)
    return report


def evaluate_samples(
    model: NeuralAbrLiteCandidateScorer,
    normalizer: FeatureNormalizer,
    samples: Sequence[Mapping[str, object]],
    batch_size: int = 32,
) -> Mapping[str, object]:
    if not samples:
        return {"sample_count": 0, "valid_action_rate": 0.0, "teacher_agreement": 0.0, "prediction_distribution": {}}
    model.eval()
    valid_count = 0
    agreement_count = 0
    prediction_counts = {}
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


def load_trained_model(run_dir: object) -> Tuple[NeuralAbrLiteCandidateScorer, FeatureNormalizer]:
    run_path = ensure_existing_dir(run_dir, purpose="training run")
    checkpoint_path = run_path / "checkpoint.pt"
    stats = FeatureNormalizer.fit_train  # keep linter honest about import ordering
    del stats
    from core.neural_abr.artifacts import read_json
    from core.neural_abr.normalization import NormalizationStats

    normalizer = FeatureNormalizer(NormalizationStats.from_json(read_json(run_path / "normalization_stats.json")))
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    config = checkpoint.get("model_config", {})
    model = NeuralAbrLiteCandidateScorer(
        context_dim=int(config.get("context_dim", 0) or 0) or None,
        candidate_dim=int(config.get("candidate_dim", 0) or 0) or None,
        hidden_sizes=tuple(config.get("hidden_sizes", (32, 16))),
    )
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    return model, normalizer


def _batch_to_tensors(samples: Sequence[Mapping[str, object]], normalizer: FeatureNormalizer) -> Mapping[str, torch.Tensor]:
    max_candidates = max(len(sample["candidates"]) for sample in samples)  # type: ignore[arg-type]
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
    random.seed(seed)
    torch.manual_seed(int(seed))
    torch.use_deterministic_algorithms(True)
