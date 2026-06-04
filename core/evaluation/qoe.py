from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Sequence


LINEAR_QOE_VERSION = "qoe_linear_v1"
LOG_QOE_VERSION = "qoe_log_v1"
DEFAULT_LINEAR_REBUFFER_WEIGHT = 4.3
DEFAULT_LOG_REBUFFER_WEIGHT = 2.66
DEFAULT_SMOOTHNESS_WEIGHT = 1.0


@dataclass(frozen=True)
class SegmentQoEInput:
    bitrate_kbps: float
    rebuffer_s: float = 0.0


@dataclass(frozen=True)
class QoEWeights:
    rebuffer_weight: float = DEFAULT_LINEAR_REBUFFER_WEIGHT
    smoothness_weight: float = DEFAULT_SMOOTHNESS_WEIGHT
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
    quality_switch_count: int
    up_switch_count: int
    down_switch_count: int
    total_switch_magnitude_kbps: float
    avg_switch_magnitude_kbps: float
    segment_rewards: tuple[float, ...]
    segment_quality_utilities: tuple[float, ...]
    segment_smoothness: tuple[float, ...]


def compute_linear_qoe(
    segments: Iterable[SegmentQoEInput],
    weights: QoEWeights | None = None,
) -> QoEResult:
    segment_list = _validated_segments(segments)
    active_weights = _validated_weights(weights or QoEWeights())
    quality_utilities = tuple(segment.bitrate_kbps / 1000.0 for segment in segment_list)
    smoothness = _adjacent_deltas(quality_utilities)
    rewards = tuple(
        quality
        - active_weights.rebuffer_weight * segment.rebuffer_s
        - active_weights.smoothness_weight * smooth
        for segment, quality, smooth in zip(segment_list, quality_utilities, smoothness)
    )
    return _build_result(
        formula_version=LINEAR_QOE_VERSION,
        segments=segment_list,
        quality_utilities=quality_utilities,
        smoothness=smoothness,
        rewards=rewards,
        weights=active_weights,
    )


def compute_log_qoe(
    segments: Iterable[SegmentQoEInput],
    min_bitrate_kbps: float,
    weights: QoEWeights | None = None,
) -> QoEResult:
    segment_list = _validated_segments(segments)
    _require_finite_positive("min_bitrate_kbps", min_bitrate_kbps)
    active_weights = _validated_weights(
        weights
        or QoEWeights(
            rebuffer_weight=DEFAULT_LOG_REBUFFER_WEIGHT,
            smoothness_weight=DEFAULT_SMOOTHNESS_WEIGHT,
            startup_penalty_weight=0.0,
        )
    )
    quality_utilities = tuple(
        math.log(segment.bitrate_kbps / float(min_bitrate_kbps))
        for segment in segment_list
    )
    smoothness = _adjacent_deltas(quality_utilities)
    rewards = tuple(
        quality
        - active_weights.rebuffer_weight * segment.rebuffer_s
        - active_weights.smoothness_weight * smooth
        for segment, quality, smooth in zip(segment_list, quality_utilities, smoothness)
    )
    return _build_result(
        formula_version=LOG_QOE_VERSION,
        segments=segment_list,
        quality_utilities=quality_utilities,
        smoothness=smoothness,
        rewards=rewards,
        weights=active_weights,
    )


def _validated_segments(segments: Iterable[SegmentQoEInput]) -> tuple[SegmentQoEInput, ...]:
    segment_list = tuple(segments)
    if not segment_list:
        raise ValueError("segments must not be empty")
    validated = []
    for index, segment in enumerate(segment_list):
        if not isinstance(segment, SegmentQoEInput):
            raise ValueError("segment {0} must be SegmentQoEInput".format(index))
        _require_finite_positive("segment {0} bitrate_kbps".format(index), segment.bitrate_kbps)
        _require_finite_non_negative("segment {0} rebuffer_s".format(index), segment.rebuffer_s)
        validated.append(
            SegmentQoEInput(
                bitrate_kbps=float(segment.bitrate_kbps),
                rebuffer_s=float(segment.rebuffer_s),
            )
        )
    return tuple(validated)


def _validated_weights(weights: QoEWeights) -> QoEWeights:
    if not isinstance(weights, QoEWeights):
        raise ValueError("weights must be QoEWeights")
    _require_finite_non_negative("rebuffer_weight", weights.rebuffer_weight)
    _require_finite_non_negative("smoothness_weight", weights.smoothness_weight)
    _require_finite_non_negative("startup_penalty_weight", weights.startup_penalty_weight)
    return QoEWeights(
        rebuffer_weight=float(weights.rebuffer_weight),
        smoothness_weight=float(weights.smoothness_weight),
        startup_penalty_weight=float(weights.startup_penalty_weight),
    )


def _require_finite_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if float(value) <= 0.0:
        raise ValueError("{0} must be > 0".format(name))


def _require_finite_non_negative(name: str, value: float) -> None:
    _require_finite(name, value)
    if float(value) < 0.0:
        raise ValueError("{0} must be >= 0".format(name))


def _require_finite(name: str, value: float) -> None:
    try:
        numeric = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(numeric):
        raise ValueError("{0} must be finite".format(name))


def _adjacent_deltas(values: Sequence[float]) -> tuple[float, ...]:
    deltas = [0.0]
    for previous, current in zip(values, values[1:]):
        deltas.append(abs(current - previous))
    return tuple(deltas)


def _build_result(
    formula_version: str,
    segments: Sequence[SegmentQoEInput],
    quality_utilities: Sequence[float],
    smoothness: Sequence[float],
    rewards: Sequence[float],
    weights: QoEWeights,
) -> QoEResult:
    segment_count = len(segments)
    qoe_sum = sum(rewards)
    total_rebuffer_s = sum(segment.rebuffer_s for segment in segments)
    bitrates = tuple(segment.bitrate_kbps for segment in segments)
    switch_magnitudes = tuple(abs(current - previous) for previous, current in zip(bitrates, bitrates[1:]))
    actual_switches = tuple(magnitude for magnitude in switch_magnitudes if magnitude > 0.0)
    up_switch_count = sum(1 for previous, current in zip(bitrates, bitrates[1:]) if current > previous)
    down_switch_count = sum(1 for previous, current in zip(bitrates, bitrates[1:]) if current < previous)
    total_switch_magnitude = sum(actual_switches)
    quality_switch_count = len(actual_switches)
    return QoEResult(
        formula_version=formula_version,
        segment_count=segment_count,
        qoe_sum=qoe_sum,
        qoe_mean=qoe_sum / float(segment_count),
        quality_utility_sum=sum(quality_utilities),
        avg_quality_mbps=sum(quality_utilities) / float(segment_count),
        rebuffer_penalty=weights.rebuffer_weight * total_rebuffer_s,
        smoothness_penalty=weights.smoothness_weight * sum(smoothness),
        avg_bitrate_kbps=sum(bitrates) / float(segment_count),
        total_rebuffer_s=total_rebuffer_s,
        stall_event_count=sum(1 for segment in segments if segment.rebuffer_s > 0.0),
        quality_switch_count=quality_switch_count,
        up_switch_count=up_switch_count,
        down_switch_count=down_switch_count,
        total_switch_magnitude_kbps=total_switch_magnitude,
        avg_switch_magnitude_kbps=(
            total_switch_magnitude / float(quality_switch_count)
            if quality_switch_count
            else 0.0
        ),
        segment_rewards=tuple(rewards),
        segment_quality_utilities=tuple(quality_utilities),
        segment_smoothness=tuple(smoothness),
    )
