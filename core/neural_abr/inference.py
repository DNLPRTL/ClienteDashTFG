from __future__ import annotations

import math
import time
from pathlib import Path
from typing import Mapping, Sequence

import torch

from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.artifacts import ensure_existing_dir, read_json, read_jsonl, write_json
from core.neural_abr.bundle import validate_phase4_bundle_dir
from core.neural_abr.constants import (
    BUNDLE_INFERENCE_SMOKE_REPORT_FILENAME,
    BUNDLE_LATENCY_REPORT_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_MODEL_FILENAME,
    DATA_FILENAMES,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_INFERENCE_SMOKE_SCHEMA_ID,
    VALIDATION_ROLE,
)
from core.neural_abr.model import NeuralAbrLiteCandidateScorer
from core.neural_abr.normalization import FeatureNormalizer, NormalizationStats
from core.neural_abr.sample_schema import validate_sample


class InferenceError(ValueError):
    """Raised when Phase 4F offline inference is invalid or unsafe."""


class NeuralAbrLiteInferenceBundle:
    def __init__(self, bundle_dir: object) -> None:
        validation = validate_phase4_bundle_dir(bundle_dir)
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = validation["manifest"]
        self.model_card = read_json(self.bundle_dir / BUNDLE_MODEL_CARD_FILENAME)
        self.normalizer = FeatureNormalizer(NormalizationStats.from_json(read_json(self.bundle_dir / NORMALIZATION_STATS_FILENAME)))
        self.model = self._load_model()
        self.model.eval()

    def score_sample(self, sample: Mapping[str, object]) -> Mapping[str, object]:
        validate_sample(sample, expected_role=str(sample.get("data_role", VALIDATION_ROLE)))
        return self.score(
            context_features=_mapping(sample.get("context_features"), "context_features"),
            candidate_features=_candidate_sequence(sample.get("candidate_features")),
            action_mask=_sequence(sample.get("action_mask"), "action_mask"),
        )

    def score(
        self,
        context_features: Mapping[str, object],
        candidate_features: Sequence[Mapping[str, object]],
        action_mask: Sequence[object],
    ) -> Mapping[str, object]:
        if not candidate_features:
            raise InferenceError("candidate_features must not be empty")
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
        with torch.no_grad():
            scores = self.model(context_tensor, candidate_tensor, mask_tensor).detach().cpu()[0].tolist()
        latency_ms = (time.perf_counter() - started) * 1000.0
        parsed_scores = _finite_scores(scores)
        selected_position = _select_position(parsed_scores, mask)
        selected_representation_index = int(candidate_features[selected_position]["candidate_representation_index"])
        assert_action_valid(selected_representation_index, mask)
        return {
            "scores": parsed_scores,
            "selected_candidate_position": selected_position,
            "selected_representation_index": selected_representation_index,
            "latency_ms": latency_ms,
            "fallback_used": False,
        }

    def _load_model(self) -> NeuralAbrLiteCandidateScorer:
        checkpoint = _torch_load_cpu(self.bundle_dir / BUNDLE_MODEL_FILENAME)
        if not isinstance(checkpoint, Mapping):
            raise InferenceError("modelo_para_inferencia.pt must contain a mapping")
        config = checkpoint.get("model_config")
        if not isinstance(config, Mapping):
            config = self.model_card.get("model_config")
        if not isinstance(config, Mapping):
            raise InferenceError("bundle model config is missing")
        model = NeuralAbrLiteCandidateScorer(
            context_dim=int(config.get("context_dim", 0) or 0) or None,
            candidate_dim=int(config.get("candidate_dim", 0) or 0) or None,
            hidden_sizes=tuple(int(value) for value in config.get("hidden_sizes", (32, 16))),  # type: ignore[arg-type]
        )
        state_dict = checkpoint.get("model_state_dict")
        if not isinstance(state_dict, Mapping):
            raise InferenceError("modelo_para_inferencia.pt missing model_state_dict")
        model.load_state_dict(state_dict)
        return model


def load_phase4_inference_bundle(bundle_dir: object) -> NeuralAbrLiteInferenceBundle:
    torch.use_deterministic_algorithms(True)
    return NeuralAbrLiteInferenceBundle(bundle_dir)


def run_phase4_inference_smoke(
    bundle_dir: object,
    data_dir: object,
    output_dir: object | None = None,
    max_samples: int = 512,
) -> Mapping[str, object]:
    if max_samples <= 0:
        raise InferenceError("max_samples must be positive")
    data_path = ensure_existing_dir(data_dir, purpose="phase4 training data")
    engine = load_phase4_inference_bundle(bundle_dir)
    samples = tuple(read_jsonl(data_path / DATA_FILENAMES[VALIDATION_ROLE], limit=max_samples))
    if not samples:
        raise InferenceError("validation samples are required for inference smoke")
    decisions = []
    valid_count = 0
    deterministic_count = 0
    teacher_agreement_count = 0
    for sample in samples:
        first = engine.score_sample(sample)
        second = engine.score_sample(sample)
        selected = int(first["selected_representation_index"])
        deterministic = first["scores"] == second["scores"] and selected == int(second["selected_representation_index"])
        mask = tuple(bool(value) for value in sample["action_mask"])  # type: ignore[index]
        if selected < len(mask) and mask[selected]:
            valid_count += 1
        if deterministic:
            deterministic_count += 1
        teacher_action = int(sample["label"]["teacher_action"])  # type: ignore[index]
        if selected == teacher_action:
            teacher_agreement_count += 1
        decisions.append(
            {
                "sample_id": sample.get("sample_id"),
                "selected_representation_index": selected,
                "teacher_action": teacher_action,
                "deterministic": deterministic,
                "latency_ms": first["latency_ms"],
                "scores": first["scores"],
            }
        )
    latencies = [float(decision["latency_ms"]) for decision in decisions]
    smoke_report = {
        "schema_id": PHASE4_INFERENCE_SMOKE_SCHEMA_ID,
        "human_readable_name": "Prueba offline de inferencia del bundle NeuralABR-Lite",
        "phase": "phase4f_export_bundle_inferencia",
        "status": "PASS",
        "bundle_dir": str(Path(bundle_dir).expanduser().resolve()),
        "data_dir": str(data_path),
        "sample_count": len(samples),
        "valid_action_rate": valid_count / float(len(samples)),
        "deterministic_rate": deterministic_count / float(len(samples)),
        "teacher_agreement_report_only": teacher_agreement_count / float(len(samples)),
        "no_nan_inf_scores": all(_scores_are_finite(decision["scores"]) for decision in decisions),
        "latency_summary": _latency_summary(latencies),
        "decisions_preview": decisions[: min(10, len(decisions))],
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "controller_integrated": False,
        "controller_registered": False,
        "qoe_improvement_claimed": False,
    }
    if output_dir is not None:
        output_path = Path(output_dir).expanduser().resolve()
        output_path.mkdir(parents=True, exist_ok=True)
        write_json(output_path / BUNDLE_INFERENCE_SMOKE_REPORT_FILENAME, smoke_report)
        write_json(
            output_path / BUNDLE_LATENCY_REPORT_FILENAME,
            {
                "schema_id": "phase4_reporte_latencia_inferencia_v1",
                "phase": "phase4f_export_bundle_inferencia",
                "latency_summary": smoke_report["latency_summary"],
                "latency_is_benchmark": False,
                "production_latency_claim": False,
            },
        )
    return smoke_report


def _torch_load_cpu(path: Path) -> object:
    try:
        return torch.load(path, map_location="cpu", weights_only=False)
    except TypeError:
        return torch.load(path, map_location="cpu")


def _mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise InferenceError("{0} must be a mapping".format(name))
    return value


def _sequence(value: object, name: str) -> Sequence[object]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise InferenceError("{0} must be a sequence".format(name))
    return value


def _candidate_sequence(value: object) -> tuple[Mapping[str, object], ...]:
    sequence = _sequence(value, "candidate_features")
    candidates = []
    for candidate in sequence:
        if not isinstance(candidate, Mapping):
            raise InferenceError("candidate_features entries must be mappings")
        candidates.append(candidate)
    return tuple(candidates)


def _assert_candidate_indices_are_positions(candidates: Sequence[Mapping[str, object]]) -> None:
    for position, candidate in enumerate(candidates):
        raw_value = candidate.get("candidate_representation_index")
        if isinstance(raw_value, bool):
            raise InferenceError("candidate_representation_index must be numeric")
        try:
            parsed = int(float(raw_value))
        except (TypeError, ValueError) as exc:
            raise InferenceError("candidate_representation_index must be numeric") from exc
        if parsed != position:
            raise InferenceError("candidate_representation_index must match candidate position")


def _finite_scores(scores: Sequence[object]) -> list[float]:
    parsed = []
    for index, score in enumerate(scores):
        if isinstance(score, bool):
            raise InferenceError("score {0} must be finite".format(index))
        try:
            value = float(score)
        except (TypeError, ValueError) as exc:
            raise InferenceError("score {0} must be finite".format(index)) from exc
        if not math.isfinite(value):
            raise InferenceError("score {0} must be finite".format(index))
        parsed.append(value)
    return parsed


def _select_position(scores: Sequence[float], mask: Sequence[bool]) -> int:
    masked_scores = [score if mask[index] else -1.0e9 for index, score in enumerate(scores)]
    selected = max(range(len(masked_scores)), key=lambda index: masked_scores[index])
    if not mask[selected]:
        raise InferenceError("selected action is masked")
    return int(selected)


def _scores_are_finite(scores: object) -> bool:
    if not isinstance(scores, Sequence) or isinstance(scores, (str, bytes)):
        return False
    try:
        _finite_scores(scores)
    except InferenceError:
        return False
    return True


def _latency_summary(latencies_ms: Sequence[float]) -> Mapping[str, object]:
    ordered = sorted(float(value) for value in latencies_ms)
    if not ordered:
        return {"sample_count": 0, "min_ms": None, "p50_ms": None, "p95_ms": None, "max_ms": None, "mean_ms": None}
    return {
        "sample_count": len(ordered),
        "min_ms": ordered[0],
        "p50_ms": _percentile(ordered, 0.50),
        "p95_ms": _percentile(ordered, 0.95),
        "max_ms": ordered[-1],
        "mean_ms": sum(ordered) / float(len(ordered)),
    }


def _percentile(ordered_values: Sequence[float], percentile: float) -> float:
    index = int(math.ceil(float(percentile) * len(ordered_values))) - 1
    index = min(max(index, 0), len(ordered_values) - 1)
    return float(ordered_values[index])
