from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence

from core.neural_abr.constants import (
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    PHASE4_NORMALIZATION_SCHEMA_ID,
    TRAINING_ROLE,
)
from core.neural_abr.features import flatten_candidate_features, flatten_context_features


class NormalizationError(ValueError):
    """Raised when train-only normalization is invalid."""


@dataclass(frozen=True)
class NormalizationStats:
    schema_id: str
    fitted_on_data_role: str
    feature_names: tuple[str, ...]
    mean: tuple[float, ...]
    std: tuple[float, ...]
    sample_count: int
    candidate_row_count: int

    def to_json(self) -> Mapping[str, object]:
        return {
            "schema_id": self.schema_id,
            "human_readable_name": "Estadisticas de normalizacion ajustadas solo con datos de entrenamiento",
            "fitted_on_data_role": self.fitted_on_data_role,
            "feature_names": list(self.feature_names),
            "mean": list(self.mean),
            "std": list(self.std),
            "sample_count": self.sample_count,
            "candidate_row_count": self.candidate_row_count,
        }

    @classmethod
    def from_json(cls, payload: Mapping[str, object]) -> "NormalizationStats":
        if payload.get("schema_id") != PHASE4_NORMALIZATION_SCHEMA_ID:
            raise NormalizationError("normalization schema_id is invalid")
        return cls(
            schema_id=str(payload["schema_id"]),
            fitted_on_data_role=str(payload["fitted_on_data_role"]),
            feature_names=tuple(str(value) for value in payload["feature_names"]),
            mean=tuple(float(value) for value in payload["mean"]),
            std=tuple(float(value) for value in payload["std"]),
            sample_count=int(payload["sample_count"]),
            candidate_row_count=int(payload["candidate_row_count"]),
        )


class FeatureNormalizer:
    def __init__(self, stats: NormalizationStats) -> None:
        if stats.fitted_on_data_role != TRAINING_ROLE:
            raise NormalizationError("normalization stats must be fitted only on training data")
        if len(stats.feature_names) != len(stats.mean) or len(stats.mean) != len(stats.std):
            raise NormalizationError("normalization stats lengths do not match")
        self.stats = stats

    @classmethod
    def fit_training_only(cls, samples: Sequence[Mapping[str, object]]) -> "FeatureNormalizer":
        rows: list[tuple[float, ...]] = []
        for sample in samples:
            if sample.get("data_role") != TRAINING_ROLE:
                raise NormalizationError("normalization may only consume training samples")
            context_vector = flatten_context_features(sample["context_features"])  # type: ignore[arg-type]
            for candidate in sample["candidate_features"]:  # type: ignore[index]
                rows.append(context_vector + flatten_candidate_features(candidate))
        if not rows:
            raise NormalizationError("normalization requires at least one candidate row")
        width = len(rows[0])
        sums = [0.0 for _ in range(width)]
        for row in rows:
            if len(row) != width:
                raise NormalizationError("feature vector width changed")
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
        stats = NormalizationStats(
            schema_id=PHASE4_NORMALIZATION_SCHEMA_ID,
            fitted_on_data_role=TRAINING_ROLE,
            feature_names=tuple(CONTEXT_VECTOR_NAMES) + tuple(CANDIDATE_VECTOR_NAMES),
            mean=tuple(means),
            std=tuple(stds),
            sample_count=len(samples),
            candidate_row_count=len(rows),
        )
        return cls(stats)

    def normalize_pair(self, context: Mapping[str, object], candidate: Mapping[str, object]) -> tuple[tuple[float, ...], tuple[float, ...]]:
        combined = flatten_context_features(context) + flatten_candidate_features(candidate)
        if len(combined) != len(self.stats.mean):
            raise NormalizationError("feature vector width mismatch")
        normalized = tuple(
            (value - self.stats.mean[index]) / self.stats.std[index] for index, value in enumerate(combined)
        )
        context_width = len(CONTEXT_VECTOR_NAMES)
        return normalized[:context_width], normalized[context_width:]

    def normalize_sample(self, sample: Mapping[str, object]) -> tuple[tuple[float, ...], tuple[tuple[float, ...], ...]]:
        normalized_context = None
        normalized_candidates = []
        for candidate in sample["candidate_features"]:  # type: ignore[index]
            context_vector, candidate_vector = self.normalize_pair(sample["context_features"], candidate)  # type: ignore[arg-type]
            if normalized_context is None:
                normalized_context = context_vector
            normalized_candidates.append(candidate_vector)
        if normalized_context is None:
            raise NormalizationError("sample has no candidates")
        return normalized_context, tuple(normalized_candidates)

