from __future__ import annotations

import math
from typing import Iterable, Mapping, Sequence

from core.neural_abr.constants import (
    CANDIDATE_FEATURES,
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_SCALAR_FEATURES,
    CONTEXT_VECTOR_NAMES,
    DEFAULT_CONTEXT_HISTORY_LENGTH,
    FORBIDDEN_MODEL_INPUT_FIELDS,
    PHASE4_FEATURE_SCHEMA_ID,
)
from core.neural_abr.content_ladder import ContentLadder
from core.neural_abr.replay_environment import ReplayState


class FeatureError(ValueError):
    """Raised when feature construction violates the no-contamination contract."""


def build_context_features(state: ReplayState, ladder: ContentLadder) -> Mapping[str, object]:
    last_bitrate_bps = 0.0
    if state.last_representation_index >= 0:
        last_bitrate_bps = float(ladder.bitrate_bps(state.last_representation_index))
    chunks_remaining = max(ladder.segment_count - state.segment_index, 0)
    chunks_remaining_norm = float(chunks_remaining) / float(max(ladder.segment_count, 1))
    return {
        "throughput_history_bps": _left_pad(state.throughput_history_bps, DEFAULT_CONTEXT_HISTORY_LENGTH),
        "download_time_history_s": _left_pad(state.download_time_history_s, DEFAULT_CONTEXT_HISTORY_LENGTH),
        "buffer_s": float(state.buffer_s),
        "last_representation_index": float(state.last_representation_index),
        "last_bitrate_bps": float(last_bitrate_bps),
        "recent_rebuffer_s": float(state.recent_rebuffer_s),
        "recent_switch_abs": float(state.recent_switch_abs),
        "chunks_remaining_norm": float(chunks_remaining_norm),
        "has_chunks_remaining": 1.0 if chunks_remaining > 0 else 0.0,
    }


def build_candidate_features(
    ladder: ContentLadder,
    segment_index: int,
    last_bitrate_bps: float,
) -> tuple[Mapping[str, object], ...]:
    min_bitrate = float(ladder.min_bitrate_bps)
    max_bitrate = float(ladder.max_bitrate_bps)
    bitrate_span = max(max_bitrate - min_bitrate, 1.0)
    position_denominator = max(ladder.representation_count - 1, 1)
    delta_denominator = max(max_bitrate, 1.0)
    candidates = []
    for representation_index, bitrate_bps in enumerate(ladder.bitrates_bps):
        candidates.append(
            {
                "candidate_representation_index": float(representation_index),
                "candidate_ladder_position_norm": float(representation_index) / float(position_denominator),
                "candidate_bitrate_bps": float(bitrate_bps),
                "candidate_bitrate_norm_ladder": (float(bitrate_bps) - min_bitrate) / bitrate_span,
                "candidate_delta_from_last_bitrate_norm": (
                    0.0 if last_bitrate_bps <= 0.0 else (float(bitrate_bps) - float(last_bitrate_bps)) / delta_denominator
                ),
                "candidate_chunk_size_bytes": float(ladder.segment_size_bytes(representation_index, segment_index)),
                "candidate_chunk_size_available": 1.0,
            }
        )
    return tuple(candidates)


def flatten_context_features(context: Mapping[str, object]) -> tuple[float, ...]:
    reject_forbidden_model_inputs(context)
    throughput = _numeric_sequence(context.get("throughput_history_bps"), "throughput_history_bps")
    download_times = _numeric_sequence(context.get("download_time_history_s"), "download_time_history_s")
    scalars = tuple(_finite_number(context.get(name), name) for name in CONTEXT_SCALAR_FEATURES)
    return throughput + download_times + scalars


def flatten_candidate_features(candidate: Mapping[str, object]) -> tuple[float, ...]:
    reject_forbidden_model_inputs(candidate)
    return tuple(_finite_number(candidate.get(name), name) for name in CANDIDATE_FEATURES)


def build_feature_schema() -> Mapping[str, object]:
    return {
        "schema_id": PHASE4_FEATURE_SCHEMA_ID,
        "human_readable_name": "Features visibles por el modelo NeuralABR-Lite",
        "context_history_length": DEFAULT_CONTEXT_HISTORY_LENGTH,
        "context_vector_names": list(CONTEXT_VECTOR_NAMES),
        "candidate_vector_names": list(CANDIDATE_VECTOR_NAMES),
        "forbidden_model_input_fields": sorted(FORBIDDEN_MODEL_INPUT_FIELDS),
    }


def audit_feature_payload(context: Mapping[str, object], candidates: Iterable[Mapping[str, object]]) -> Mapping[str, object]:
    errors = []
    try:
        flatten_context_features(context)
    except FeatureError as exc:
        errors.append(str(exc))
    for index, candidate in enumerate(candidates):
        try:
            flatten_candidate_features(candidate)
        except FeatureError as exc:
            errors.append("candidate {0}: {1}".format(index, exc))
    return {"passed": not errors, "errors": errors}


def reject_forbidden_model_inputs(mapping: Mapping[str, object]) -> None:
    offenders = sorted(str(key) for key in mapping.keys() if str(key) in FORBIDDEN_MODEL_INPUT_FIELDS)
    if offenders:
        raise FeatureError("forbidden model input field(s): {0}".format(", ".join(offenders)))


def _left_pad(values: Sequence[float], expected: int) -> tuple[float, ...]:
    materialized = tuple(float(value) for value in values)
    if len(materialized) >= expected:
        return materialized[-expected:]
    return tuple(0.0 for _ in range(expected - len(materialized))) + materialized


def _numeric_sequence(raw_values: object, name: str) -> tuple[float, ...]:
    try:
        values = tuple(raw_values)  # type: ignore[arg-type]
    except TypeError as exc:
        raise FeatureError("{0} must be a sequence".format(name)) from exc
    if len(values) != DEFAULT_CONTEXT_HISTORY_LENGTH:
        raise FeatureError("{0} must have length {1}".format(name, DEFAULT_CONTEXT_HISTORY_LENGTH))
    return tuple(_finite_number(value, "{0}[{1}]".format(name, index)) for index, value in enumerate(values))


def _finite_number(raw_value: object, name: str) -> float:
    if isinstance(raw_value, bool):
        raise FeatureError("{0} must be numeric and finite".format(name))
    try:
        value = float(raw_value)
    except (TypeError, ValueError) as exc:
        raise FeatureError("{0} must be numeric and finite".format(name)) from exc
    if not math.isfinite(value):
        raise FeatureError("{0} must be numeric and finite".format(name))
    return value

