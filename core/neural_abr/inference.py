"""CPU-only offline inference for Phase 4F NeuralABR-Lite bundles."""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

import torch

from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.artifacts import ensure_existing_dir, read_jsonl
from core.neural_abr.bundle import read_json_file, validate_bundle_dir
from core.neural_abr.constants import DATASET_FILENAMES, VALIDATION_SPLIT
from core.neural_abr.model import NeuralAbrLiteCandidateScorer
from core.neural_abr.normalization import FeatureNormalizer, NormalizationStats


class InferenceError(ValueError):
    """Raised when offline NeuralABR-Lite inference is unsafe or invalid."""


@dataclass(frozen=True)
class InferenceDecision:
    scores: tuple[float, ...]
    selected_representation_index: int
    selected_candidate_position: int
    latency_ms: float
    fallback_used: bool = False
    invalid_input_reason: str | None = None

    def to_json(self) -> Mapping[str, object]:
        return {
            "scores": list(self.scores),
            "selected_representation_index": self.selected_representation_index,
            "selected_candidate_position": self.selected_candidate_position,
            "latency_ms": self.latency_ms,
            "fallback_used": self.fallback_used,
            "invalid_input_reason": self.invalid_input_reason,
        }


class NeuralAbrLiteInferenceEngine:
    def __init__(self, bundle_dir: object):
        self.bundle_validation = validate_bundle_dir(bundle_dir)
        self.bundle_dir = self.bundle_validation.bundle_dir
        self.manifest = self.bundle_validation.manifest
        self.model_card = read_json_file(self.bundle_dir / "model_card.json")
        self.normalizer = FeatureNormalizer(
            NormalizationStats.from_json(read_json_file(self.bundle_dir / "normalization_stats.json"))
        )
        self.model = self._load_model_cpu()
        self.model.eval()

    def score_sample(self, sample: Mapping[str, object]) -> InferenceDecision:
        try:
            context = sample["context"]
            candidates = sample["candidates"]
            action_mask = sample["action_mask"]
        except KeyError as exc:
            raise InferenceError("sample missing inference field: {0}".format(exc.args[0])) from exc
        if not isinstance(context, Mapping):
            raise InferenceError("sample context must be a mapping")
        if not isinstance(candidates, Sequence) or isinstance(candidates, (str, bytes)) or not candidates:
            raise InferenceError("sample candidates must be a non-empty sequence")
        candidate_mappings = []
        for candidate in candidates:
            if not isinstance(candidate, Mapping):
                raise InferenceError("sample candidate must be a mapping")
            candidate_mappings.append(candidate)
        return self.score(context=context, candidates=tuple(candidate_mappings), action_mask=action_mask)

    def score(
        self,
        context: Mapping[str, object],
        candidates: Sequence[Mapping[str, object]],
        action_mask: Sequence[object],
    ) -> InferenceDecision:
        if not candidates:
            raise InferenceError("inference requires at least one candidate")
        mask = validate_action_mask(action_mask, len(candidates))
        candidate_indices = _candidate_indices(candidates)

        start = time.perf_counter()
        context_vector = None
        candidate_vectors = []
        for candidate in candidates:
            normalized_context, normalized_candidate = self.normalizer.normalize_pair(context, candidate)
            if context_vector is None:
                context_vector = normalized_context
            candidate_vectors.append(normalized_candidate)
        if context_vector is None:
            raise InferenceError("inference requires at least one candidate")

        context_tensor = torch.tensor([context_vector], dtype=torch.float32, device="cpu")
        candidate_tensor = torch.tensor([candidate_vectors], dtype=torch.float32, device="cpu")
        mask_tensor = torch.tensor([mask], dtype=torch.bool, device="cpu")
        with torch.no_grad():
            scores_tensor = self.model(context_tensor, candidate_tensor, mask_tensor).detach().cpu()[0]
        latency_ms = (time.perf_counter() - start) * 1000.0

        scores = _finite_scores(scores_tensor.tolist())
        selected_position = select_candidate_position(scores, mask)
        selected_representation_index = candidate_indices[selected_position]
        assert_action_valid(selected_representation_index, mask)
        return InferenceDecision(
            scores=tuple(scores),
            selected_representation_index=selected_representation_index,
            selected_candidate_position=selected_position,
            latency_ms=float(latency_ms),
        )

    def _load_model_cpu(self) -> NeuralAbrLiteCandidateScorer:
        model_state_path = self.bundle_dir / "model_state.pt"
        try:
            checkpoint = _torch_load_cpu(model_state_path)
        except Exception as exc:  # noqa: BLE001 - include bundle path in public error.
            raise InferenceError("failed to load model_state.pt on CPU") from exc
        if not isinstance(checkpoint, Mapping):
            raise InferenceError("model_state.pt must contain a mapping")

        model_config = _model_config(checkpoint, self.model_card)
        model = NeuralAbrLiteCandidateScorer(
            context_dim=int(model_config.get("context_dim", 0) or 0) or None,
            candidate_dim=int(model_config.get("candidate_dim", 0) or 0) or None,
            hidden_sizes=tuple(model_config.get("hidden_sizes", (32, 16))),
        )
        raw_state = checkpoint.get("model_state_dict") if "model_state_dict" in checkpoint else checkpoint
        if not isinstance(raw_state, Mapping):
            raise InferenceError("model_state.pt missing model_state_dict")
        model.load_state_dict(raw_state)
        return model


def load_neural_abr_bundle(bundle_dir: object) -> NeuralAbrLiteInferenceEngine:
    torch.use_deterministic_algorithms(True)
    return NeuralAbrLiteInferenceEngine(bundle_dir)


def select_candidate_position(scores: Sequence[object], action_mask: Sequence[object]) -> int:
    finite_scores = _finite_scores(scores)
    mask = validate_action_mask(action_mask, len(finite_scores))
    masked_scores = [
        score if mask[index] else -1.0e9
        for index, score in enumerate(finite_scores)
    ]
    best_position = max(range(len(masked_scores)), key=lambda index: masked_scores[index])
    if not mask[best_position]:
        raise InferenceError("inference selected a masked candidate")
    return int(best_position)


def load_validation_samples(dataset_dir: object, max_samples: int | None = None) -> Sequence[Mapping[str, object]]:
    dataset_path = ensure_existing_dir(dataset_dir, purpose="Phase 4E.2 dataset")
    rows = read_jsonl(dataset_path / DATASET_FILENAMES[VALIDATION_SPLIT])
    if max_samples is None:
        return rows
    return tuple(rows[: max(0, int(max_samples))])


def run_sample_inference(
    engine: NeuralAbrLiteInferenceEngine,
    samples: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    if not samples:
        raise InferenceError("sample inference requires at least one sample")
    decisions = []
    valid_count = 0
    deterministic_count = 0
    for sample in samples:
        first = engine.score_sample(sample)
        second = engine.score_sample(sample)
        deterministic = (
            first.selected_representation_index == second.selected_representation_index
            and first.scores == second.scores
        )
        deterministic_count += 1 if deterministic else 0
        mask = tuple(bool(value) for value in sample["action_mask"])  # type: ignore[index]
        if bool(mask[first.selected_representation_index]):
            valid_count += 1
        entry = dict(first.to_json())
        entry["sample_id"] = sample.get("sample_id")
        entry["deterministic"] = deterministic
        decisions.append(entry)

    latencies = [float(decision["latency_ms"]) for decision in decisions]
    no_nan_inf = all(_scores_are_finite(decision["scores"]) for decision in decisions)
    return {
        "schema_version": "neural_abr_lite_phase4f_sample_inference_report_v1",
        "phase": "phase4f",
        "sample_count": len(samples),
        "valid_action_rate": valid_count / float(len(samples)),
        "deterministic_rate": deterministic_count / float(len(samples)),
        "no_nan_inf_scores": no_nan_inf,
        "decisions": decisions,
        "latency_summary": summarize_latency_ms(latencies),
        "diagnostic_only": True,
        "not_benchmark": True,
        "client_integration": False,
        "controller_registered": False,
    }


def summarize_latency_ms(latencies_ms: Sequence[float]) -> Mapping[str, object]:
    if not latencies_ms:
        return {
            "sample_count": 0,
            "min_ms": None,
            "p50_ms": None,
            "p95_ms": None,
            "max_ms": None,
            "mean_ms": None,
        }
    ordered = sorted(float(value) for value in latencies_ms)
    for value in ordered:
        if not math.isfinite(value) or value < 0.0:
            raise InferenceError("latency values must be finite and non-negative")
    return {
        "sample_count": len(ordered),
        "min_ms": ordered[0],
        "p50_ms": _percentile(ordered, 0.50),
        "p95_ms": _percentile(ordered, 0.95),
        "max_ms": ordered[-1],
        "mean_ms": sum(ordered) / float(len(ordered)),
    }


def write_inference_reports(
    sample_report: Mapping[str, object],
    output_dir: object,
    docs_dir: object | None = None,
) -> Mapping[str, object]:
    from core.neural_abr.artifacts import ensure_outside_repo
    from core.neural_abr.bundle import write_json_file

    output_path = ensure_outside_repo(output_dir, purpose="Phase 4F inference output")
    output_path.mkdir(parents=True, exist_ok=True)
    latency_report = {
        "schema_version": "neural_abr_lite_phase4f_latency_report_v1",
        "phase": "phase4f",
        "latency_summary": sample_report.get("latency_summary"),
        "target_p95_ms": 10.0,
        "diagnostic_only": True,
        "not_benchmark": True,
        "production_latency_claim": False,
    }
    write_json_file(output_path / "sample_inference_report.json", sample_report)
    write_json_file(output_path / "inference_latency_report.json", latency_report)

    if docs_dir is not None:
        docs_path = Path(docs_dir)
        docs_path.mkdir(parents=True, exist_ok=True)
        (docs_path / "phase4f_inference_smoke_report.md").write_text(
            render_inference_smoke_markdown(sample_report),
            encoding="utf-8",
        )
        (docs_path / "phase4f_inference_latency_report.md").write_text(
            render_latency_markdown(latency_report),
            encoding="utf-8",
        )
    return latency_report


def render_inference_smoke_markdown(sample_report: Mapping[str, object]) -> str:
    latency = _mapping(sample_report.get("latency_summary"))
    return "\n".join(
        [
            "# Phase 4F Inference Smoke Report",
            "",
            "Phase 4F inference is offline-only. No client integration and no neural controller registration occurred.",
            "",
            "- Sample count: `{0}`".format(sample_report.get("sample_count")),
            "- Valid action rate: `{0}`".format(sample_report.get("valid_action_rate")),
            "- Deterministic rate: `{0}`".format(sample_report.get("deterministic_rate")),
            "- No NaN/Inf scores: `{0}`".format(sample_report.get("no_nan_inf_scores")),
            "- p95 latency ms: `{0}`".format(latency.get("p95_ms")),
            "",
            "This smoke is not a benchmark, ranking, SOTA claim, or real-world validation.",
            "",
        ]
    )


def render_latency_markdown(latency_report: Mapping[str, object]) -> str:
    summary = _mapping(latency_report.get("latency_summary"))
    return "\n".join(
        [
            "# Phase 4F Inference Latency Report",
            "",
            "Latency is measured only as an offline CPU safety feasibility gate. It is not a benchmark against ABR controllers.",
            "",
            "- Sample count: `{0}`".format(summary.get("sample_count")),
            "- p50 ms: `{0}`".format(summary.get("p50_ms")),
            "- p95 ms: `{0}`".format(summary.get("p95_ms")),
            "- Max ms: `{0}`".format(summary.get("max_ms")),
            "- Target p95 ms: `{0}`".format(latency_report.get("target_p95_ms")),
            "- Production latency claim: `{0}`".format(latency_report.get("production_latency_claim")),
            "",
            "No client integration, controller registration, benchmark/ranking, SOTA, or real-world claim is made.",
            "",
        ]
    )


def _candidate_indices(candidates: Sequence[Mapping[str, object]]) -> tuple[int, ...]:
    indices = []
    for expected, candidate in enumerate(candidates):
        raw_value = candidate.get("candidate_representation_index")
        if isinstance(raw_value, bool):
            raise InferenceError("candidate_representation_index must be numeric")
        try:
            parsed = int(float(raw_value))
        except (TypeError, ValueError) as exc:
            raise InferenceError("candidate_representation_index must be numeric") from exc
        if parsed != expected:
            raise InferenceError("candidate_representation_index must be contiguous and aligned with action_mask")
        indices.append(parsed)
    return tuple(indices)


def _finite_scores(scores: Sequence[object]) -> list[float]:
    parsed_scores = []
    for index, raw_score in enumerate(scores):
        if isinstance(raw_score, bool):
            raise InferenceError("score {0} must be finite".format(index))
        try:
            score = float(raw_score)
        except (TypeError, ValueError) as exc:
            raise InferenceError("score {0} must be finite".format(index)) from exc
        if not math.isfinite(score):
            raise InferenceError("score {0} must be finite".format(index))
        parsed_scores.append(score)
    return parsed_scores


def _scores_are_finite(scores: object) -> bool:
    if not isinstance(scores, Sequence) or isinstance(scores, (str, bytes)):
        return False
    try:
        _finite_scores(scores)
    except InferenceError:
        return False
    return True


def _model_config(checkpoint: Mapping[str, object], model_card: Mapping[str, object]) -> Mapping[str, object]:
    raw_config = checkpoint.get("model_config")
    if isinstance(raw_config, Mapping):
        return raw_config
    card_config = model_card.get("model_config")
    if isinstance(card_config, Mapping):
        return card_config
    return {}


def _torch_load_cpu(path: Path) -> object:
    try:
        return torch.load(path, map_location="cpu", weights_only=True)
    except TypeError:
        return torch.load(path, map_location="cpu")
    except Exception:
        return torch.load(path, map_location="cpu", weights_only=False)


def _percentile(ordered_values: Sequence[float], percentile: float) -> float:
    if len(ordered_values) == 1:
        return float(ordered_values[0])
    index = int(math.ceil(percentile * len(ordered_values))) - 1
    index = min(max(index, 0), len(ordered_values) - 1)
    return float(ordered_values[index])


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}
