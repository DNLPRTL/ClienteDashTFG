from __future__ import annotations

import math
import time
from collections.abc import Mapping, Sequence
from numbers import Real
from pathlib import Path

import torch

from core.controller.neural_abr_loader import NeuralAbrRuntimeBundleError
from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.artifacts import read_json
from core.phase45_v1.spbc_training import CANDIDATE_FEATURES, SCALAR_FEATURES, SEQUENCE_FEATURES
from core.phase45_v1.spbc_v2_dpo_bundle import (
    SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME,
    SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_FILENAME,
    SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME,
    SPBC_V2_DPO_BUNDLE_SCHEMA_ID,
    validate_spbc_v2_dpo_bundle_dir,
)
from core.phase45_v1.spbc_v2_dpo_training import SPBC_V2_DPO_MODEL_KEY, SpbcAbrV2DpoPolicy


class SpbcV2DpoRuntimeBundle:
    def __init__(self, bundle_dir: object, verify_hashes: bool = True) -> None:
        validation = _validate_bundle(bundle_dir, verify_hashes=bool(verify_hashes))
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.feature_schema = _load_feature_schema(self.bundle_dir / SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME)
        self.inference_contract = read_json(self.bundle_dir / SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME)
        self.model_card = read_json(self.bundle_dir / SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME)
        self.normalization = _load_normalization(self.bundle_dir / SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME)
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
        sequence, scalars, candidates = _build_feature_rows(context_features, candidate_features, self.normalization)
        sequence_tensor = torch.tensor([sequence], dtype=torch.float32)
        scalar_tensor = torch.tensor([scalars], dtype=torch.float32)
        candidate_tensor = torch.tensor([candidates], dtype=torch.float32)
        mask_tensor = torch.tensor([mask], dtype=torch.bool)
        try:
            with torch.no_grad():
                outputs = self.model(sequence_tensor, scalar_tensor, candidate_tensor, mask_tensor)
        except Exception as exc:
            raise NeuralAbrRuntimeBundleError("inference_failed", "model forward failed") from exc
        latency_ms = (time.perf_counter() - started) * 1000.0
        logits = _tensor_row(outputs.get("action_logits"), "action_logits")
        parsed_logits = _finite_scores(logits)
        if len(parsed_logits) != len(mask):
            raise NeuralAbrRuntimeBundleError("inference_failed", "score count does not match action mask")
        selected_position = _select_position(parsed_logits, mask)
        selected_representation_index = int(candidate_features[selected_position]["candidate_representation_index"])
        try:
            assert_action_valid(selected_representation_index, mask)
        except ValueError as exc:
            raise NeuralAbrRuntimeBundleError("selected_masked_action", str(exc)) from exc
        return {
            "scores": parsed_logits,
            "selected_candidate_position": selected_position,
            "selected_representation_index": selected_representation_index,
            "latency_ms": latency_ms,
        }

    def _load_model(self) -> SpbcAbrV2DpoPolicy:
        checkpoint = _torch_load_weights_only(self.bundle_dir / SPBC_V2_DPO_BUNDLE_MODEL_FILENAME)
        if not isinstance(checkpoint, Mapping):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model checkpoint must contain a mapping")
        if checkpoint.get("schema_id") != SPBC_V2_DPO_BUNDLE_SCHEMA_ID:
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model checkpoint schema_id is invalid")
        if checkpoint.get("model_key") != SPBC_V2_DPO_MODEL_KEY:
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model checkpoint model_key is invalid")
        config = checkpoint.get("model_config")
        if not isinstance(config, Mapping):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "bundle model config is missing")
        model = SpbcAbrV2DpoPolicy(
            sequence_dim=int(config.get("sequence_dim", len(SEQUENCE_FEATURES)) or len(SEQUENCE_FEATURES)),
            scalar_dim=int(config.get("scalar_dim", len(SCALAR_FEATURES)) or len(SCALAR_FEATURES)),
            candidate_dim=int(config.get("candidate_dim", len(CANDIDATE_FEATURES)) or len(CANDIDATE_FEATURES)),
            history_hidden_size=int(config["history_hidden_size"]),
            state_hidden_size=int(config["state_hidden_size"]),
            candidate_hidden_size=int(config["candidate_hidden_size"]),
            shared_hidden_size=int(config["shared_hidden_size"]),
            dropout=float(config.get("dropout", 0.0) or 0.0),
            decision_reward_fusion_weight=float(config.get("decision_reward_fusion_weight", 0.12) or 0.12),
            decision_rebuffer_fusion_weight=float(config.get("decision_rebuffer_fusion_weight", 0.30) or 0.30),
            decision_risk_fusion_weight=float(config.get("decision_risk_fusion_weight", 0.18) or 0.18),
            rebuffer_prediction_cap_s=float(config.get("rebuffer_prediction_cap_s", 4.0) or 4.0),
        )
        state_dict = checkpoint.get("model_state_dict")
        if not isinstance(state_dict, Mapping):
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model checkpoint missing model_state_dict")
        try:
            model.load_state_dict(state_dict)
        except Exception as exc:
            raise NeuralAbrRuntimeBundleError("model_config_invalid", "model state_dict is incompatible") from exc
        return model


def load_spbc_v2_dpo_runtime_bundle(bundle_dir: object, verify_hashes: bool = True) -> SpbcV2DpoRuntimeBundle:
    torch.use_deterministic_algorithms(True)
    return SpbcV2DpoRuntimeBundle(bundle_dir, verify_hashes=verify_hashes)


def _validate_bundle(bundle_dir: object, verify_hashes: bool) -> Mapping[str, object]:
    if bundle_dir is None or not str(bundle_dir).strip():
        raise NeuralAbrRuntimeBundleError("missing_bundle_dir", "bundle_dir is required")
    try:
        return validate_spbc_v2_dpo_bundle_dir(bundle_dir, verify_hashes=verify_hashes)
    except Exception as exc:
        text = str(exc).lower()
        if "sha256 mismatch" in text or "size mismatch" in text:
            raise NeuralAbrRuntimeBundleError("bundle_hash_invalid", str(exc)) from exc
        if "does not exist" in text or "missing" in text or "must be outside" in text:
            raise NeuralAbrRuntimeBundleError("missing_bundle_dir", str(exc)) from exc
        raise NeuralAbrRuntimeBundleError("bundle_schema_invalid", str(exc)) from exc


def _load_feature_schema(path: Path) -> Mapping[str, object]:
    try:
        schema = read_json(path)
    except Exception as exc:
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "feature schema is not readable") from exc
    if schema.get("schema_id") != "phase45_v2_spbc_dpo_runtime_feature_schema_v1":
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "feature schema_id is invalid")
    if tuple(schema.get("sequence_features", ())) != tuple(SEQUENCE_FEATURES):
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "sequence feature names do not match")
    if tuple(schema.get("scalar_features", ())) != tuple(SCALAR_FEATURES):
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "scalar feature names do not match")
    if tuple(schema.get("candidate_features", ())) != tuple(CANDIDATE_FEATURES):
        raise NeuralAbrRuntimeBundleError("feature_schema_invalid", "candidate feature names do not match")
    return schema


def _load_normalization(path: Path) -> Mapping[str, tuple[float, ...]]:
    try:
        raw = read_json(path)
    except Exception as exc:
        raise NeuralAbrRuntimeBundleError("model_config_invalid", "normalization is not readable") from exc
    if raw.get("schema_id") != "phase45_v2_spbc_dpo_normalization_v1":
        raise NeuralAbrRuntimeBundleError("model_config_invalid", "normalization schema_id is invalid")
    return {
        "sequence_mean": _numeric_tuple(raw.get("sequence_mean"), len(SEQUENCE_FEATURES), "sequence_mean"),
        "sequence_std": _numeric_tuple(raw.get("sequence_std"), len(SEQUENCE_FEATURES), "sequence_std"),
        "scalar_mean": _numeric_tuple(raw.get("scalar_mean"), len(SCALAR_FEATURES), "scalar_mean"),
        "scalar_std": _numeric_tuple(raw.get("scalar_std"), len(SCALAR_FEATURES), "scalar_std"),
        "candidate_mean": _numeric_tuple(raw.get("candidate_mean"), len(CANDIDATE_FEATURES), "candidate_mean"),
        "candidate_std": _numeric_tuple(raw.get("candidate_std"), len(CANDIDATE_FEATURES), "candidate_std"),
    }


def _build_feature_rows(
    context_features: Mapping[str, object],
    candidate_features: Sequence[Mapping[str, object]],
    normalization: Mapping[str, tuple[float, ...]],
) -> tuple[list[list[float]], list[float], list[list[float]]]:
    throughput = _numeric_sequence(context_features.get("throughput_history_bps"), "throughput_history_bps")
    download_time = _numeric_sequence(context_features.get("download_time_history_s"), "download_time_history_s")
    if len(throughput) != len(download_time):
        raise NeuralAbrRuntimeBundleError("inference_failed", "history feature lengths differ")
    sequence = [[throughput[index], download_time[index]] for index in range(len(throughput))]
    scalars = [_required_finite(context_features, name) for name in SCALAR_FEATURES]
    candidates = [
        [_required_finite(candidate, name) for name in CANDIDATE_FEATURES]
        for candidate in candidate_features
    ]
    return (
        _normalize_matrix(sequence, normalization["sequence_mean"], normalization["sequence_std"]),
        _normalize_vector(scalars, normalization["scalar_mean"], normalization["scalar_std"]),
        [_normalize_vector(candidate, normalization["candidate_mean"], normalization["candidate_std"]) for candidate in candidates],
    )


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> list[float]:
    if len(values) != len(mean) or len(mean) != len(std):
        raise NeuralAbrRuntimeBundleError("inference_failed", "normalization vector width mismatch")
    return [(float(value) - float(mean[index])) / max(float(std[index]), 1.0e-12) for index, value in enumerate(values)]


def _normalize_matrix(values: Sequence[Sequence[float]], mean: Sequence[float], std: Sequence[float]) -> list[list[float]]:
    return [_normalize_vector(row, mean, std) for row in values]


def _tensor_row(value: object, name: str) -> Sequence[object]:
    if not isinstance(value, torch.Tensor):
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} output missing".format(name))
    try:
        row = value.detach().cpu()[0].tolist()
    except Exception as exc:
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} output shape is invalid".format(name)) from exc
    if not isinstance(row, list):
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} output row is invalid".format(name))
    return row


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


def _numeric_sequence(value: object, name: str) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} must be a sequence".format(name))
    return tuple(_finite_number(item, "{0}[{1}]".format(name, index)) for index, item in enumerate(value))


def _numeric_tuple(value: object, expected: int, name: str) -> tuple[float, ...]:
    values = _numeric_sequence(value, name)
    if len(values) != int(expected):
        raise NeuralAbrRuntimeBundleError("model_config_invalid", "{0} width mismatch".format(name))
    return values


def _required_finite(mapping: Mapping[str, object], name: str) -> float:
    if name not in mapping:
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} is missing".format(name))
    return _finite_number(mapping.get(name), name)


def _finite_number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} must be finite".format(name))
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NeuralAbrRuntimeBundleError("inference_failed", "{0} must be finite".format(name))
    return parsed
