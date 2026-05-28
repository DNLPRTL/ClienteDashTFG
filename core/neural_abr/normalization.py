"""Train-only normalization for NeuralABR-Lite features."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence, Tuple

from core.neural_abr.constants import (
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    NORMALIZATION_SCHEMA_VERSION,
    TRAIN_SPLIT,
)
from core.neural_abr.features import flatten_candidate_features, flatten_context_features


class NormalizationError(ValueError):
    """Raised when normalization scope or statistics are invalid."""


@dataclass(frozen=True)
class NormalizationStats:
    schema_version: str
    fitted_on_split: str
    feature_names: Tuple[str, ...]
    mean: Tuple[float, ...]
    std: Tuple[float, ...]
    sample_count: int
    candidate_row_count: int

    def to_json(self) -> Mapping[str, object]:
        return {
            "schema_version": self.schema_version,
            "fitted_on_split": self.fitted_on_split,
            "feature_names": list(self.feature_names),
            "mean": list(self.mean),
            "std": list(self.std),
            "sample_count": self.sample_count,
            "candidate_row_count": self.candidate_row_count,
        }

    @classmethod
    def from_json(cls, payload: Mapping[str, object]) -> "NormalizationStats":
        if payload.get("schema_version") != NORMALIZATION_SCHEMA_VERSION:
            raise NormalizationError("normalization stats schema_version is invalid")
        return cls(
            schema_version=str(payload["schema_version"]),
            fitted_on_split=str(payload["fitted_on_split"]),
            feature_names=tuple(str(value) for value in payload["feature_names"]),
            mean=tuple(float(value) for value in payload["mean"]),
            std=tuple(float(value) for value in payload["std"]),
            sample_count=int(payload["sample_count"]),
            candidate_row_count=int(payload["candidate_row_count"]),
        )


class FeatureNormalizer:
    def __init__(self, stats: NormalizationStats):
        if stats.fitted_on_split != TRAIN_SPLIT:
            raise NormalizationError("normalization stats must be fitted on train")
        if len(stats.feature_names) != len(stats.mean) or len(stats.mean) != len(stats.std):
            raise NormalizationError("normalization stats lengths do not match")
        self.stats = stats

    @classmethod
    def fit_train(cls, samples: Sequence[Mapping[str, object]]) -> "FeatureNormalizer":
        rows = []
        sample_count = 0
        for sample in samples:
            split = sample.get("split")
            if split != TRAIN_SPLIT:
                raise NormalizationError("normalization fit may only consume train samples")
            sample_count += 1
            context_vector = flatten_context_features(sample["context"])  # type: ignore[arg-type]
            for candidate in sample["candidates"]:  # type: ignore[index]
                candidate_vector = flatten_candidate_features(candidate)
                rows.append(context_vector + candidate_vector)
        if not rows:
            raise NormalizationError("normalization fit requires at least one candidate row")

        width = len(rows[0])
        sums = [0.0 for _ in range(width)]
        for row in rows:
            if len(row) != width:
                raise NormalizationError("feature vector width changed during fit")
            for index, value in enumerate(row):
                sums[index] += value
        means = [value / float(len(rows)) for value in sums]

        variances = [0.0 for _ in range(width)]
        for row in rows:
            for index, value in enumerate(row):
                delta = value - means[index]
                variances[index] += delta * delta
        stds = []
        for variance in variances:
            std = math.sqrt(variance / float(len(rows)))
            stds.append(std if std > 1e-12 else 1.0)

        feature_names = tuple(CONTEXT_VECTOR_NAMES) + tuple(CANDIDATE_VECTOR_NAMES)
        stats = NormalizationStats(
            schema_version=NORMALIZATION_SCHEMA_VERSION,
            fitted_on_split=TRAIN_SPLIT,
            feature_names=feature_names,
            mean=tuple(means),
            std=tuple(stds),
            sample_count=sample_count,
            candidate_row_count=len(rows),
        )
        return cls(stats)

    def normalize_pair(self, context: Mapping[str, object], candidate: Mapping[str, object]) -> Tuple[Tuple[float, ...], Tuple[float, ...]]:
        context_vector = flatten_context_features(context)
        candidate_vector = flatten_candidate_features(candidate)
        combined = context_vector + candidate_vector
        if len(combined) != len(self.stats.mean):
            raise NormalizationError("feature vector width does not match normalization stats")
        normalized = tuple(
            (value - self.stats.mean[index]) / self.stats.std[index]
            for index, value in enumerate(combined)
        )
        context_width = len(CONTEXT_VECTOR_NAMES)
        return normalized[:context_width], normalized[context_width:]

    def normalize_sample(self, sample: Mapping[str, object]) -> Tuple[Tuple[float, ...], Tuple[Tuple[float, ...], ...]]:
        normalized_context = None
        normalized_candidates = []
        for candidate in sample["candidates"]:  # type: ignore[index]
            context_vector, candidate_vector = self.normalize_pair(sample["context"], candidate)  # type: ignore[arg-type]
            if normalized_context is None:
                normalized_context = context_vector
            normalized_candidates.append(candidate_vector)
        if normalized_context is None:
            raise NormalizationError("sample has no candidates")
        return normalized_context, tuple(normalized_candidates)
