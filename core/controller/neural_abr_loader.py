from __future__ import annotations

import math
import time
from collections.abc import Mapping, Sequence
from pathlib import Path

import torch

from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.artifacts import read_json
from core.neural_abr.bundle import BundleError, validate_phase4_bundle_dir
from core.neural_abr.constants import (
    BUNDLE_INFERENCE_CONTRACT_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_MODEL_FILENAME,
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    FEATURE_SCHEMA_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_FEATURE_SCHEMA_ID,
)
from core.neural_abr.model import NeuralAbrLiteCandidateScorer
from core.neural_abr.normalization import FeatureNormalizer, NormalizationStats


class NeuralAbrRuntimeBundleError(ValueError):
    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = reason


class NeuralAbrRuntimeBundle:
    def __init__(self, bundle_dir: object, expected_teacher: str, verify_hashes: bool = True) -> None:
        validation = _validate_bundle(bundle_dir, verify_hashes=bool(verify_hashes))
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.expected_teacher = str(expected_teacher)
        self.teacher = str(self.manifest.get("teacher", ""))
        if self.teacher != self.expected_teacher:
            raise NeuralAbrRuntimeBundleError(
                "expected_teacher_mismatch",
                "expected teacher {0}, got {1}".format(self.expected_teacher, self.teacher),
            )
        self.feature_schema = _load_feature_schema(self.bundle_dir / FEATURE_SCHEMA_FILENAME)
        self.inference_contract = read_json(self.bundle_dir / BUNDLE_INFERENCE_CONTRACT_FILENAME)
        self.model_card = read_json(self.bundle_dir / BUNDLE_MODEL_CARD_FILENAME)
        self.normalizer = FeatureNormalizer(
            NormalizationStats.from_json(read_json(self.bundle_dir / NORMALIZATION_STATS_FILENAME))
        )
        self.model = self._load_model()
        self.model.eval()

    def score(
        self,
        context_features: Mapping[str, object],
        candidate_features: Sequence[Mapping[str, object]],
        action_mask: Sequence[object],
    ) -> Mapping[str, object]:
        if not candidate_features:
            raise NeuralAbrRuntimeBundleError("inference_failed", "candidate_features must not be empty")
        mask = validate_action_mask(action_mask, len(candidate_features))
        _assert_candidate_indices_are_positions(candidate_features)
        started = time.perf_counter()
        context_vector = None
        candidate_vectors = []
        for candidate in candidate_features:
            normalized_context, normalized_candidate = self.normalizer.normalize_pair(context_features, candidate)
            if context_vector is None:
                context_vector = normalized_context
            candidate_vectors.append(normalized_candidate)
        context_tensor = torch.tensor([context_vector], dtype=torch.float32)
        candidate_tensor = torch.tensor([candidate_vectors], dtype=torch.float32)
        mask_tensor = torch.tensor([mask], dtype=torch.bool)
        try:
            with torch.no_grad():
                raw = self.model(context_tensor, candidate_tensor, mask_tensor)
        except Exception as exc:
            raise NeuralAbrRuntimeBundleError("inference_failed", "model forward failed") from exc
        latency_ms = (time.perf_counter() - started) * 1000.0
        try:
            scores = raw.detach().cpu()[0].tolist()
        except Exception as exc:
            raise NeuralAbrRuntimeBundleError("inference_failed", "model output shape is invalid") from exc
        parsed_scores = _finite_scores(scores)
        if len(parsed_scores) != len(mask):
            raise NeuralAbrRuntimeBundleError("inference_failed", "score count does not match action mask")
        selected_position = _select_position(parsed_scores, mask)
        selected_representation_index = int(candidate_features[selected_position]["candidate_representation_index"])
        try:
            assert_action_valid(selected_representation_index, mask)
        except ValueError as exc:
            raise NeuralAbrRuntimeBundleError("selected_masked_action", str(exc)) from exc
        return {
            "scores": parsed_scores,
            "selected_candidate_position": selected_position,
            "selected_representation_index": selected_representation_index,
            "latency_ms": latency_ms,
        }

    def _load_model(self) -> NeuralAbrLiteCandidateScorer:
        checkpoint = _torch_load_weights_only(self.bundle_dir / BUNDLE_MODEL_FILENAME)
        if not isinstance(checkpoint, Mapping):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model checkpoint must contain a mapping")
        config = checkpoint.get("model_config")
        if not isinstance(config, Mapping):
            config = self.model_card.get("model_config")
        if not isinstance(config, Mapping):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "bundle model config is missing")
        context_dim = int(config.get("context_dim", 0) or 0)
        candidate_dim = int(config.get("candidate_dim", 0) or 0)
        if context_dim != len(CONTEXT_VECTOR_NAMES) or candidate_dim != len(CANDIDATE_VECTOR_NAMES):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model feature dimensions do not match Phase 4 schema")
        model = NeuralAbrLiteCandidateScorer(
            context_dim=context_dim,
            candidate_dim=candidate_dim,
            hidden_sizes=tuple(int(value) for value in config.get("hidden_sizes", (32, 16))),  # type: ignore[arg-type]
        )
        state_dict = checkpoint.get("model_state_dict")
        if not isinstance(state_dict, Mapping):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model checkpoint missing model_state_dict")
        try:
            model.load_state_dict(state_dict)
        except Exception as exc:
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model state_dict is incompatible") from exc
        return model


def load_neural_abr_runtime_bundle(
    bundle_dir: object,
    expected_teacher: str,
    verify_hashes: bool = True,
) -> NeuralAbrRuntimeBundle:
    torch.use_deterministic_algorithms(True)
    return NeuralAbrRuntimeBundle(bundle_dir, expected_teacher=expected_teacher, verify_hashes=verify_hashes)


def _validate_bundle(bundle_dir: object, verify_hashes: bool) -> Mapping[str, object]:
    if bundle_dir is None or not str(bundle_dir).strip():
        raise NeuralAbrRuntimeBundleError("missing_bundle_dir", "bundle_dir is required")
    try:
        return validate_phase4_bundle_dir(bundle_dir, verify_hashes=verify_hashes)
    except BundleError as exc:
        text = str(exc).lower()
        if "sha256 mismatch" in text or "size mismatch" in text:
            raise NeuralAbrRuntimeBundleError("bundle_hash_invalid", str(exc)) from exc
        raise NeuralAbrRuntimeBundleError("bundle_schema_invalid", str(exc)) from exc
    except Exception as exc:
        raise NeuralAbrRuntimeBundleError("missing_bundle_dir", str(exc)) from exc


def _load_feature_schema(path: Path) -> Mapping[str, object]:
    try:
        schema = read_json(path)
    except Exception as exc:
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "feature schema is not readable") from exc
    if schema.get("schema_id") != PHASE4_FEATURE_SCHEMA_ID:
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "feature schema_id is invalid")
    if tuple(schema.get("context_vector_names", ())) != tuple(CONTEXT_VECTOR_NAMES):
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "context feature names do not match")
    if tuple(schema.get("candidate_vector_names", ())) != tuple(CANDIDATE_VECTOR_NAMES):
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "candidate feature names do not match")
    return schema


def _torch_load_weights_only(path: Path) -> object:
    try:
        return torch.load(path, map_location="cpu", weights_only=True)
    except TypeError as exc:
        raise NeuralAbrRuntimeBundleError("safe_torch_load_unavailable", "torch.load weights_only is unavailable") from exc
    except Exception as exc:
        raise NeuralAbrRuntimeBundleError("bundle_load_failed", "torch.load failed") from exc


def _assert_candidate_indices_are_positions(candidates: Sequence[Mapping[str, object]]) -> None:
    for position, candidate in enumerate(candidates):
        raw_value = candidate.get("candidate_representation_index")
        if isinstance(raw_value, bool):
            raise NeuralAbrRuntimeBundleError("inference_failed", "candidate_representation_index must be numeric")
        try:
            parsed = int(float(raw_value))
        except (TypeError, ValueError) as exc:
            raise NeuralAbrRuntimeBundleError("inference_failed", "candidate_representation_index must be numeric") from exc
        if parsed != position:
            raise NeuralAbrRuntimeBundleError(
                "inference_failed",
                "candidate_representation_index must match candidate position",
            )


def _finite_scores(scores: Sequence[object]) -> list[float]:
    parsed = []
    for index, score in enumerate(scores):
        if isinstance(score, bool):
            raise NeuralAbrRuntimeBundleError("nan_inf_scores", "score {0} must be finite".format(index))
        try:
            value = float(score)
        except (TypeError, ValueError) as exc:
            raise NeuralAbrRuntimeBundleError("nan_inf_scores", "score {0} must be finite".format(index)) from exc
        if not math.isfinite(value):
            raise NeuralAbrRuntimeBundleError("nan_inf_scores", "score {0} must be finite".format(index))
        parsed.append(value)
    return parsed


def _select_position(scores: Sequence[float], mask: Sequence[bool]) -> int:
    masked_scores = [score if mask[index] else -1.0e9 for index, score in enumerate(scores)]
    selected = max(range(len(masked_scores)), key=lambda index: masked_scores[index])
    if not mask[selected]:
        raise NeuralAbrRuntimeBundleError("selected_masked_action", "selected action is masked")
    return int(selected)

