"""Safe local-only runtime loader for NeuralABR-Lite controller inference."""

from __future__ import annotations

import importlib
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.bundle import (
    BUNDLE_ACTION_SPACE,
    BUNDLE_MODEL_FAMILY,
    BUNDLE_TEACHER,
    BUNDLE_TRAINING_METHOD,
    InvalidBundleError,
    MissingBundleFileError,
    read_json_file,
    validate_bundle_dir,
)
from core.neural_abr.constants import (
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    FEATURE_SCHEMA_VERSION,
    MODEL_CONFIG_VERSION,
)


class NeuralAbrRuntimeLoadError(Exception):
    def __init__(self, reason: str, message: str | None = None):
        self.reason = reason
        super().__init__(message or reason)


class NeuralAbrRuntimeError(ValueError):
    def __init__(self, reason: str, message: str | None = None):
        self.reason = reason
        super().__init__(message or reason)


@dataclass(frozen=True)
class RuntimeScoringDecision:
    scores: tuple[float, ...]
    raw_action: int
    latency_ms: float


class NeuralAbrRuntimeEngine:
    def __init__(
        self,
        *,
        bundle_validation,
        model_card: Mapping[str, object],
        feature_schema: Mapping[str, object],
        normalization_stats: Mapping[str, object],
        ladder_schema: Mapping[str, object],
        inference_contract: Mapping[str, object],
        fallback_policy: Mapping[str, object],
        model,
        torch_module,
    ):
        self.bundle_validation = bundle_validation
        self.bundle_dir = bundle_validation.bundle_dir
        self.manifest = bundle_validation.manifest
        self.model_card = model_card
        self.feature_schema = feature_schema
        self.normalization_stats = normalization_stats
        self.ladder_schema = ladder_schema
        self.inference_contract = inference_contract
        self.fallback_policy = fallback_policy
        normalizer_cls, stats_cls = _normalization_classes()
        self.normalizer = normalizer_cls(stats_cls.from_json(normalization_stats))
        self.model = model
        self._torch = torch_module

    def score(
        self,
        context: Mapping[str, object],
        candidates: Sequence[Mapping[str, object]],
        action_mask: Sequence[object],
    ) -> RuntimeScoringDecision:
        if not candidates:
            raise NeuralAbrRuntimeError("action_mask_invalid", "inference requires at least one candidate")
        mask = validate_action_mask(action_mask, len(candidates))
        candidate_indices = _candidate_indices(candidates)

        context_vector = None
        candidate_vectors = []
        start = time.perf_counter()
        try:
            for candidate in candidates:
                normalized_context, normalized_candidate = self.normalizer.normalize_pair(context, candidate)
                if context_vector is None:
                    context_vector = normalized_context
                candidate_vectors.append(normalized_candidate)
            if context_vector is None:
                raise NeuralAbrRuntimeError("feature_build_failed", "inference requires a context vector")

            torch = self._torch
            context_tensor = torch.tensor([context_vector], dtype=torch.float32, device="cpu")
            candidate_tensor = torch.tensor([candidate_vectors], dtype=torch.float32, device="cpu")
            mask_tensor = torch.tensor([mask], dtype=torch.bool, device="cpu")
            with torch.no_grad():
                scores_tensor = self.model(context_tensor, candidate_tensor, mask_tensor).detach().cpu()[0]
        except NeuralAbrRuntimeError:
            raise
        except Exception as exc:  # noqa: BLE001 - controller converts to fail-closed fallback.
            raise NeuralAbrRuntimeError("inference_failed", "runtime inference failed") from exc
        latency_ms = (time.perf_counter() - start) * 1000.0

        scores = _finite_scores(scores_tensor.tolist())
        _validate_score_shape(scores, mask)
        selected_position = _select_candidate_position(scores, mask)
        raw_action = candidate_indices[selected_position]
        try:
            assert_action_valid(raw_action, mask)
        except Exception as exc:  # noqa: BLE001
            raise NeuralAbrRuntimeError("selected_masked_action", "selected action is invalid") from exc
        return RuntimeScoringDecision(scores=tuple(scores), raw_action=int(raw_action), latency_ms=float(latency_ms))


def load_runtime_engine(bundle_dir: object, verify_hashes: bool = True) -> NeuralAbrRuntimeEngine:
    resolved = _resolve_local_bundle_dir(bundle_dir)
    try:
        bundle_validation = validate_bundle_dir(resolved, verify_hashes=verify_hashes)
    except MissingBundleFileError as exc:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", str(exc)) from exc
    except InvalidBundleError as exc:
        reason = "bundle_hash_invalid" if "sha256" in str(exc).lower() or "hash" in str(exc).lower() else "bundle_schema_invalid"
        raise NeuralAbrRuntimeLoadError(reason, str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("bundle_load_failed", str(exc)) from exc

    try:
        manifest = bundle_validation.manifest
        _validate_manifest_runtime_metadata(manifest)
        model_card = read_json_file(resolved / "model_card.json")
        feature_schema = read_json_file(resolved / "feature_schema.json")
        normalization_stats = read_json_file(resolved / "normalization_stats.json")
        ladder_schema = read_json_file(resolved / "ladder_schema.json")
        inference_contract = read_json_file(resolved / "inference_contract.json")
        fallback_policy = read_json_file(resolved / "fallback_policy.json")
        _validate_model_card(model_card)
        _validate_feature_schema(feature_schema)
        _validate_auxiliary_schemas(ladder_schema, inference_contract, fallback_policy)
        model, torch_module = _load_model_cpu_safe(resolved / "model_state.pt", model_card)
    except NeuralAbrRuntimeLoadError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", str(exc)) from exc

    return NeuralAbrRuntimeEngine(
        bundle_validation=bundle_validation,
        model_card=model_card,
        feature_schema=feature_schema,
        normalization_stats=normalization_stats,
        ladder_schema=ladder_schema,
        inference_contract=inference_contract,
        fallback_policy=fallback_policy,
        model=model,
        torch_module=torch_module,
    )


def _resolve_local_bundle_dir(bundle_dir: object) -> Path:
    if bundle_dir is None or str(bundle_dir).strip() == "":
        raise NeuralAbrRuntimeLoadError("missing_bundle_dir", "bundle_dir is not configured")
    text = str(bundle_dir).strip()
    if "://" in text:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "bundle_dir must be a local filesystem path")
    resolved = Path(text).expanduser().resolve()
    if not resolved.is_dir():
        raise NeuralAbrRuntimeLoadError("missing_bundle_dir", "bundle_dir does not exist: {0}".format(resolved))
    return resolved


def _load_model_cpu_safe(model_state_path: Path, model_card: Mapping[str, object]):
    try:
        torch = importlib.import_module("torch")
    except ModuleNotFoundError as exc:
        raise NeuralAbrRuntimeLoadError("torch_unavailable", "PyTorch is unavailable") from exc
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("torch_unavailable", "PyTorch import failed") from exc

    try:
        model_module = importlib.import_module("core.neural_abr.model")
        model_cls = getattr(model_module, "NeuralAbrLiteCandidateScorer")
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("torch_unavailable", "model import failed after PyTorch import") from exc

    try:
        checkpoint = torch.load(model_state_path, map_location="cpu", weights_only=True)
    except TypeError as exc:
        raise NeuralAbrRuntimeLoadError("safe_torch_load_unavailable", "torch.load weights_only=True is unavailable") from exc
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("bundle_load_failed", "safe model_state.pt load failed") from exc

    if not isinstance(checkpoint, Mapping):
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_state.pt must contain a mapping")
    model_config = _model_config(checkpoint, model_card)
    _validate_model_config(model_config)

    try:
        model = model_cls(
            context_dim=int(model_config.get("context_dim")),
            candidate_dim=int(model_config.get("candidate_dim")),
            hidden_sizes=tuple(model_config.get("hidden_sizes", (32, 16))),
        )
        state_dict = checkpoint.get("model_state_dict") if "model_state_dict" in checkpoint else checkpoint
        if not isinstance(state_dict, Mapping):
            raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_state.pt missing state_dict mapping")
        model.load_state_dict(state_dict)
        model.to("cpu")
        model.eval()
        try:
            torch.use_deterministic_algorithms(True)
        except Exception:
            pass
    except NeuralAbrRuntimeLoadError:
        raise
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("bundle_load_failed", "state_dict load failed") from exc
    return model, torch


def _normalization_classes():
    try:
        normalization_module = importlib.import_module("core.neural_abr.normalization")
        return (
            getattr(normalization_module, "FeatureNormalizer"),
            getattr(normalization_module, "NormalizationStats"),
        )
    except Exception as exc:  # noqa: BLE001
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "normalization import failed") from exc


def _validate_manifest_runtime_metadata(manifest: Mapping[str, object]) -> None:
    expected = {
        "model_family": BUNDLE_MODEL_FAMILY,
        "training_method": BUNDLE_TRAINING_METHOD,
        "teacher": BUNDLE_TEACHER,
        "action_space": BUNDLE_ACTION_SPACE,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "manifest {0} is invalid".format(key))


def _validate_model_card(model_card: Mapping[str, object]) -> None:
    expected = {
        "model_family": BUNDLE_MODEL_FAMILY,
        "training_method": BUNDLE_TRAINING_METHOD,
        "teacher": BUNDLE_TEACHER,
        "action_space": BUNDLE_ACTION_SPACE,
    }
    for key, value in expected.items():
        if model_card.get(key) != value:
            raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_card {0} is invalid".format(key))
    _validate_model_config(_model_config({}, model_card))


def _validate_feature_schema(feature_schema: Mapping[str, object]) -> None:
    if feature_schema.get("schema_version") != FEATURE_SCHEMA_VERSION:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "feature_schema schema_version is invalid")
    if tuple(feature_schema.get("context_vector_names", ())) != tuple(CONTEXT_VECTOR_NAMES):
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "feature_schema context vector names mismatch")
    if tuple(feature_schema.get("candidate_vector_names", ())) != tuple(CANDIDATE_VECTOR_NAMES):
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "feature_schema candidate vector names mismatch")


def _validate_auxiliary_schemas(
    ladder_schema: Mapping[str, object],
    inference_contract: Mapping[str, object],
    fallback_policy: Mapping[str, object],
) -> None:
    if ladder_schema.get("schema_version") != "neural_abr_lite_ladder_schema_v1":
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "ladder_schema schema_version is invalid")
    if ladder_schema.get("action_space") != BUNDLE_ACTION_SPACE:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "ladder_schema action_space is invalid")
    if inference_contract.get("schema_version") != "neural_abr_lite_inference_contract_v1":
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "inference_contract schema_version is invalid")
    if inference_contract.get("cpu_first") is not True:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "inference_contract must be CPU-first")
    if fallback_policy.get("schema_version") != "neural_abr_lite_fallback_policy_v1":
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "fallback_policy schema_version is invalid")


def _validate_model_config(model_config: Mapping[str, object]) -> None:
    if model_config.get("schema_version") != MODEL_CONFIG_VERSION:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_config schema_version is invalid")
    if model_config.get("model_type") != "shared_mlp_candidate_scorer":
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_config model_type is invalid")
    if int(model_config.get("context_dim", 0)) != len(CONTEXT_VECTOR_NAMES):
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_config context_dim mismatch")
    if int(model_config.get("candidate_dim", 0)) != len(CANDIDATE_VECTOR_NAMES):
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_config candidate_dim mismatch")
    hidden_sizes = model_config.get("hidden_sizes")
    if not isinstance(hidden_sizes, Sequence) or isinstance(hidden_sizes, (str, bytes)) or not hidden_sizes:
        raise NeuralAbrRuntimeLoadError("bundle_schema_invalid", "model_config hidden_sizes is invalid")


def _model_config(checkpoint: Mapping[str, object], model_card: Mapping[str, object]) -> Mapping[str, object]:
    raw_config = checkpoint.get("model_config")
    if isinstance(raw_config, Mapping):
        return raw_config
    card_config = model_card.get("model_config")
    if isinstance(card_config, Mapping):
        return card_config
    return {}


def _candidate_indices(candidates: Sequence[Mapping[str, object]]) -> tuple[int, ...]:
    indices = []
    for expected, candidate in enumerate(candidates):
        raw_value = candidate.get("candidate_representation_index")
        if isinstance(raw_value, bool):
            raise NeuralAbrRuntimeError("feature_build_failed", "candidate_representation_index must be numeric")
        try:
            parsed = int(float(raw_value))
        except (TypeError, ValueError) as exc:
            raise NeuralAbrRuntimeError("feature_build_failed", "candidate_representation_index must be numeric") from exc
        if parsed != expected:
            raise NeuralAbrRuntimeError(
                "feature_build_failed",
                "candidate_representation_index must be contiguous and aligned with action_mask",
            )
        indices.append(parsed)
    return tuple(indices)


def _finite_scores(scores: Sequence[object]) -> list[float]:
    parsed_scores = []
    for index, raw_score in enumerate(scores):
        if isinstance(raw_score, bool):
            raise NeuralAbrRuntimeError("non_finite_scores", "score {0} must be finite".format(index))
        try:
            score = float(raw_score)
        except (TypeError, ValueError) as exc:
            raise NeuralAbrRuntimeError("non_finite_scores", "score {0} must be finite".format(index)) from exc
        if not math.isfinite(score):
            raise NeuralAbrRuntimeError("non_finite_scores", "score {0} must be finite".format(index))
        parsed_scores.append(score)
    return parsed_scores


def _validate_score_shape(scores: Sequence[float], action_mask: Sequence[bool]) -> None:
    if not scores or len(scores) != len(action_mask):
        raise NeuralAbrRuntimeError("inference_failed", "score length must match action mask")


def _select_candidate_position(scores: Sequence[float], action_mask: Sequence[bool]) -> int:
    masked_scores = [score if bool(action_mask[index]) else -1.0e9 for index, score in enumerate(scores)]
    best_position = max(range(len(masked_scores)), key=lambda index: masked_scores[index])
    if not bool(action_mask[best_position]):
        raise NeuralAbrRuntimeError("selected_masked_action", "inference selected a masked candidate")
    return int(best_position)
