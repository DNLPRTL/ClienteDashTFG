from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Optional, Sequence, Tuple


LINEAR_QOE_VERSION = "qoe_linear_v1"
LOG_QOE_VERSION = "qoe_log_v1"


@dataclass(frozen=True)
class SegmentQoEInput:
    bitrate_kbps: float
    rebuffer_s: float = 0.0


@dataclass(frozen=True)
class QoEWeights:
    rebuffer_weight: float = 4.3
    smoothness_weight: float = 1.0
    startup_penalty_weight: float = 0.0


@dataclass(frozen=True)
class QoEResult:
    formula_version: str
    segment_count: int
    qoe_sum: float
    qoe_mean: float
    quality_utility_sum: float
    avg_quality_mbps: float
    rebuffer_penalty: float
    smoothness_penalty: float
    avg_bitrate_kbps: float
    total_rebuffer_s: float
    stall_event_count: int
    total_switch_magnitude_kbps: float
    avg_switch_magnitude_kbps: float
    quality_switch_count: int
    up_switch_count: int
    down_switch_count: int
    segment_rewards: Tuple[float, ...]


def compute_linear_qoe(segments: Iterable[SegmentQoEInput], weights: Optional[QoEWeights] = None) -> QoEResult:
    """Compute the documented qoe_linear_v1 formula for a complete segment sequence."""
    qoe_weights = weights if weights is not None else QoEWeights()
    prepared_segments = _validate_segments(segments)
    qoe_weights = _validate_weights(qoe_weights)

    utilities = tuple(segment.bitrate_kbps / 1000.0 for segment in prepared_segments)
    return _compute_qoe(
        formula_version=LINEAR_QOE_VERSION,
        segments=prepared_segments,
        utilities=utilities,
        weights=qoe_weights,
    )


def compute_log_qoe(
    segments: Iterable[SegmentQoEInput],
    min_bitrate_kbps: float,
    weights: Optional[QoEWeights] = None,
) -> QoEResult:
    """Compute the documented qoe_log_v1 sensitivity formula."""
    min_bitrate_kbps = _validate_finite_positive(min_bitrate_kbps, "min_bitrate_kbps")
    qoe_weights = weights if weights is not None else QoEWeights(rebuffer_weight=2.66)
    prepared_segments = _validate_segments(segments)
    qoe_weights = _validate_weights(qoe_weights)

    utilities = tuple(
        math.log(segment.bitrate_kbps / float(min_bitrate_kbps))
        for segment in prepared_segments
    )
    return _compute_qoe(
        formula_version=LOG_QOE_VERSION,
        segments=prepared_segments,
        utilities=utilities,
        weights=qoe_weights,
    )


def _compute_qoe(
    formula_version: str,
    segments: Sequence[SegmentQoEInput],
    utilities: Sequence[float],
    weights: QoEWeights,
) -> QoEResult:
    segment_count = len(segments)
    segment_rewards = []
    smoothness_values = []

    for index, segment in enumerate(segments):
        if index == 0:
            smoothness = 0.0
        else:
            smoothness = abs(utilities[index] - utilities[index - 1])
        smoothness_values.append(smoothness)
        segment_rewards.append(
            utilities[index]
            - weights.rebuffer_weight * segment.rebuffer_s
            - weights.smoothness_weight * smoothness
        )

    quality_utility_sum = sum(utilities)
    total_rebuffer_s = sum(segment.rebuffer_s for segment in segments)
    rebuffer_penalty = weights.rebuffer_weight * total_rebuffer_s
    smoothness_penalty = weights.smoothness_weight * sum(smoothness_values)
    qoe_sum = sum(segment_rewards)
    total_bitrate_kbps = sum(segment.bitrate_kbps for segment in segments)
    avg_bitrate_kbps = total_bitrate_kbps / segment_count
    avg_quality_mbps = quality_utility_sum / segment_count

    (
        total_switch_magnitude_kbps,
        quality_switch_count,
        up_switch_count,
        down_switch_count,
    ) = _switch_metrics(segments)
    avg_switch_magnitude_kbps = (
        total_switch_magnitude_kbps / quality_switch_count
        if quality_switch_count > 0
        else 0.0
    )

    return QoEResult(
        formula_version=formula_version,
        segment_count=segment_count,
        qoe_sum=qoe_sum,
        qoe_mean=qoe_sum / segment_count,
        quality_utility_sum=quality_utility_sum,
        avg_quality_mbps=avg_quality_mbps,
        rebuffer_penalty=rebuffer_penalty,
        smoothness_penalty=smoothness_penalty,
        avg_bitrate_kbps=avg_bitrate_kbps,
        total_rebuffer_s=total_rebuffer_s,
        stall_event_count=sum(1 for segment in segments if segment.rebuffer_s > 0.0),
        total_switch_magnitude_kbps=total_switch_magnitude_kbps,
        avg_switch_magnitude_kbps=avg_switch_magnitude_kbps,
        quality_switch_count=quality_switch_count,
        up_switch_count=up_switch_count,
        down_switch_count=down_switch_count,
        segment_rewards=tuple(segment_rewards),
    )


def _switch_metrics(segments: Sequence[SegmentQoEInput]) -> Tuple[float, int, int, int]:
    total_switch_magnitude_kbps = 0.0
    quality_switch_count = 0
    up_switch_count = 0
    down_switch_count = 0

    for index in range(1, len(segments)):
        previous_bitrate = segments[index - 1].bitrate_kbps
        current_bitrate = segments[index].bitrate_kbps
        delta = current_bitrate - previous_bitrate
        if delta == 0.0:
            continue
        total_switch_magnitude_kbps += abs(delta)
        quality_switch_count += 1
        if delta > 0.0:
            up_switch_count += 1
        else:
            down_switch_count += 1

    return (
        total_switch_magnitude_kbps,
        quality_switch_count,
        up_switch_count,
        down_switch_count,
    )


def _validate_segments(segments: Iterable[SegmentQoEInput]) -> Tuple[SegmentQoEInput, ...]:
    input_segments = tuple(segments)
    if not input_segments:
        raise ValueError("segments must not be empty")

    prepared_segments = []
    for index, segment in enumerate(input_segments):
        bitrate_kbps = _validate_finite_positive(segment.bitrate_kbps, "bitrate_kbps", index=index)
        rebuffer_s = _validate_finite_non_negative(segment.rebuffer_s, "rebuffer_s", index=index)
        prepared_segments.append(SegmentQoEInput(bitrate_kbps=bitrate_kbps, rebuffer_s=rebuffer_s))

    return tuple(prepared_segments)


def _validate_weights(weights: QoEWeights) -> QoEWeights:
    return QoEWeights(
        rebuffer_weight=_validate_finite_non_negative(weights.rebuffer_weight, "rebuffer_weight"),
        smoothness_weight=_validate_finite_non_negative(weights.smoothness_weight, "smoothness_weight"),
        startup_penalty_weight=_validate_finite_non_negative(
            weights.startup_penalty_weight,
            "startup_penalty_weight",
        ),
    )


def _validate_finite_positive(value: float, name: str, index: Optional[int] = None) -> float:
    value = _validate_finite(value, name, index=index)
    if value <= 0.0:
        raise ValueError(_format_error_name(name, index) + " must be > 0")
    return value


def _validate_finite_non_negative(value: float, name: str, index: Optional[int] = None) -> float:
    value = _validate_finite(value, name, index=index)
    if value < 0.0:
        raise ValueError(_format_error_name(name, index) + " must be >= 0")
    return value


def _validate_finite(value: float, name: str, index: Optional[int] = None) -> float:
    try:
        numeric_value = float(value)
    except (TypeError, ValueError):
        raise ValueError(_format_error_name(name, index) + " must be numeric")
    if not math.isfinite(numeric_value):
        raise ValueError(_format_error_name(name, index) + " must be finite")
    return numeric_value


def _format_error_name(name: str, index: Optional[int]) -> str:
    if index is None:
        return name
    return "%s at segment %d" % (name, index)
