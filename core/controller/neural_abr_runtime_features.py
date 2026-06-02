"""Online NeuralABR-Lite feature construction from controller feedback."""

from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Real
from typing import Mapping, Sequence

from core.neural_abr.constants import CANDIDATE_FEATURES, CONTEXT_SCALAR_FEATURES, FORBIDDEN_MODEL_INPUT_KEYS, K_CONTEXT


class RuntimeFeatureError(ValueError):
    def __init__(self, reason: str, message: str | None = None, missing_features: Sequence[str] | None = None):
        self.reason = reason
        self.missing_features = tuple(missing_features or ())
        super().__init__(message or reason)


@dataclass(frozen=True)
class RuntimeSample:
    context: Mapping[str, object]
    candidates: tuple[Mapping[str, object], ...]
    action_mask: tuple[bool, ...]
    rates_Bps: tuple[float, ...]
    throughput_history_Bps: tuple[float, ...]
    download_time_history_s: tuple[float, ...]
    missing_features: tuple[str, ...] = ()


def build_runtime_sample(
    feedback: Mapping[str, object],
    throughput_history_Bps: Sequence[object] = (),
    download_time_history_s: Sequence[object] = (),
    previous_levels: Sequence[object] | None = None,
    *,
    include_feedback_sample: bool = True,
) -> RuntimeSample:
    _reject_forbidden_feedback(feedback)
    rates = _rates_from_feedback(feedback)
    action_mask = build_action_mask_from_feedback(feedback)
    if len(action_mask) != len(rates):
        raise RuntimeFeatureError("action_mask_invalid", "action_mask length does not match rates")

    throughput_history = _finite_history(throughput_history_Bps, "throughput_history_Bps", positive_only=True)
    download_history = _finite_history(download_time_history_s, "download_time_history_s", positive_only=True)
    if include_feedback_sample:
        sample = feedback_throughput_sample_Bps(feedback)
        if sample is not None:
            throughput_history = throughput_history + (sample[0],)
            download_history = download_history + (sample[1],)

    context = _build_context(
        feedback=feedback,
        rates_Bps=rates,
        throughput_history_Bps=throughput_history,
        download_time_history_s=download_history,
        previous_levels=previous_levels or (),
    )
    candidates = _build_candidates(feedback, rates)

    _validate_context_features(context)
    for candidate in candidates:
        _validate_candidate_features(candidate)

    return RuntimeSample(
        context=context,
        candidates=candidates,
        action_mask=action_mask,
        rates_Bps=rates,
        throughput_history_Bps=throughput_history,
        download_time_history_s=download_history,
    )


def build_action_mask_from_feedback(feedback: Mapping[str, object]) -> tuple[bool, ...]:
    rates = _rates_from_feedback(feedback, allow_invalid=True)
    if not rates:
        raise RuntimeFeatureError("all_actions_invalid", "rates ladder is empty")

    max_level = _int_value(feedback.get("max_level"), len(rates) - 1)
    max_level = max(-1, min(max_level, len(rates) - 1))

    mask = []
    for index, rate in enumerate(rates):
        valid = (
            index <= max_level
            and isinstance(rate, Real)
            and not isinstance(rate, bool)
            and math.isfinite(float(rate))
            and float(rate) > 0.0
        )
        mask.append(bool(valid))

    if not any(mask):
        raise RuntimeFeatureError("all_actions_invalid", "action mask has no valid action")
    return tuple(mask)


def feedback_throughput_sample_Bps(feedback: Mapping[str, object]) -> tuple[float, float] | None:
    size = _optional_finite_float(feedback.get("last_fragment_size"))
    duration = _optional_finite_float(feedback.get("last_download_time"))
    if size is None or duration is None:
        return None
    if size <= 0.0 or duration <= 0.0:
        return None
    return float(size) / float(duration), float(duration)


def _build_context(
    feedback: Mapping[str, object],
    rates_Bps: Sequence[float],
    throughput_history_Bps: Sequence[float],
    download_time_history_s: Sequence[float],
    previous_levels: Sequence[object],
) -> Mapping[str, object]:
    missing = [key for key in ("queued_time", "level", "fragment_duration") if key not in feedback]
    if missing:
        raise RuntimeFeatureError("missing_required_feature", "feedback missing required feature", missing)

    buffer_s = _required_finite_float(feedback.get("queued_time"), "queued_time")
    fragment_duration_s = _required_finite_float(feedback.get("fragment_duration"), "fragment_duration")
    last_index = _clamp_index(_int_value(feedback.get("level"), 0), rates_Bps)
    last_bitrate_bps = float(rates_Bps[last_index]) * 8.0
    segment_index = _int_value(feedback.get("segment_index"), 0)
    chunks_remaining_norm, has_chunks_remaining = _chunks_remaining(feedback, segment_index)

    return {
        "throughput_history_bps": _left_pad([value * 8.0 for value in throughput_history_Bps], K_CONTEXT),
        "download_time_history_s": _left_pad(download_time_history_s, K_CONTEXT),
        "buffer_s": float(buffer_s),
        "last_representation_index": float(last_index),
        "last_bitrate_bps": float(last_bitrate_bps),
        "recent_rebuffer_s": 0.0,
        "recent_switch_abs": float(_recent_switch_abs(previous_levels)),
        "chunks_remaining_norm": float(chunks_remaining_norm),
        "has_chunks_remaining": float(has_chunks_remaining),
        "segment_index": float(segment_index),
        "fragment_duration_s": float(fragment_duration_s),
    }


def _build_candidates(feedback: Mapping[str, object], rates_Bps: Sequence[float]) -> tuple[Mapping[str, object], ...]:
    fragment_duration_s = _required_finite_float(feedback.get("fragment_duration"), "fragment_duration")
    bitrates_bps = [float(rate) * 8.0 for rate in rates_Bps]
    min_bitrate_bps = min(bitrates_bps)
    max_bitrate_bps = max(bitrates_bps)
    bitrate_span = max(max_bitrate_bps - min_bitrate_bps, 1.0)
    position_denominator = max(len(rates_Bps) - 1, 1)
    last_index = _clamp_index(_int_value(feedback.get("level"), 0), rates_Bps)
    last_bitrate_bps = float(rates_Bps[last_index]) * 8.0
    explicit_sizes = _explicit_candidate_sizes(feedback, len(rates_Bps))

    candidates = []
    for index, rate_Bps in enumerate(rates_Bps):
        candidate_bitrate_bps = float(rate_Bps) * 8.0
        if explicit_sizes is not None:
            candidate_size = explicit_sizes[index]
            size_available = 1.0
        else:
            candidate_size = float(rate_Bps) * max(float(fragment_duration_s), 0.0)
            size_available = 0.0
        candidates.append(
            {
                "candidate_representation_index": float(index),
                "candidate_ladder_position_norm": float(index) / float(position_denominator),
                "candidate_bitrate_bps": float(candidate_bitrate_bps),
                "candidate_bitrate_norm_ladder": (candidate_bitrate_bps - min_bitrate_bps) / bitrate_span,
                "candidate_delta_from_last_bitrate_norm": (
                    (candidate_bitrate_bps - last_bitrate_bps) / max(max_bitrate_bps, 1.0)
                ),
                "candidate_chunk_size_bytes": float(candidate_size),
                "candidate_chunk_size_available": float(size_available),
            }
        )
    return tuple(candidates)


def _rates_from_feedback(feedback: Mapping[str, object], allow_invalid: bool = False) -> tuple[float, ...] | tuple[object, ...]:
    raw_rates = feedback.get("rates")
    if raw_rates is None:
        raise RuntimeFeatureError("missing_required_feature", "feedback missing rates", ("rates",))
    try:
        values = tuple(raw_rates)  # type: ignore[arg-type]
    except TypeError as exc:
        raise RuntimeFeatureError("action_mask_invalid", "rates must be iterable") from exc
    if not values:
        raise RuntimeFeatureError("all_actions_invalid", "rates ladder is empty")
    if allow_invalid:
        return values

    rates = []
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise RuntimeFeatureError("action_mask_invalid", "rate {0} is not numeric".format(index))
        rate = float(value)
        if not math.isfinite(rate) or rate <= 0.0:
            raise RuntimeFeatureError("action_mask_invalid", "rate {0} is not positive finite".format(index))
        rates.append(rate)
    return tuple(rates)


def _explicit_candidate_sizes(feedback: Mapping[str, object], count: int) -> tuple[float, ...] | None:
    for key in ("candidate_chunk_sizes_bytes", "candidate_chunk_size_bytes_by_level", "segment_size_bytes_by_level"):
        if key not in feedback:
            continue
        try:
            values = tuple(feedback.get(key) or [])
        except TypeError:
            return None
        if len(values) != count:
            return None
        sizes = []
        for value in values:
            parsed = _optional_finite_float(value)
            if parsed is None or parsed < 0.0:
                return None
            sizes.append(parsed)
        return tuple(sizes)
    return None


def _chunks_remaining(feedback: Mapping[str, object], segment_index: int) -> tuple[float, float]:
    for key in ("total_segments", "segment_count", "media_segment_count"):
        if key not in feedback:
            continue
        total = _optional_finite_float(feedback.get(key))
        if total is not None and total > 0.0:
            remaining = max(float(total) - float(segment_index), 0.0)
            return remaining / float(total), 1.0
    return 0.0, 0.0


def _recent_switch_abs(previous_levels: Sequence[object]) -> float:
    parsed = []
    for value in previous_levels:
        parsed.append(_int_value(value, 0))
    if len(parsed) < 2:
        return 0.0
    return float(abs(parsed[-1] - parsed[-2]))


def _left_pad(values: Sequence[object], expected: int) -> tuple[float, ...]:
    parsed = tuple(float(value) for value in values)
    if len(parsed) >= expected:
        return parsed[-expected:]
    return tuple(0.0 for _ in range(expected - len(parsed))) + parsed


def _finite_history(values: Sequence[object], name: str, *, positive_only: bool) -> tuple[float, ...]:
    parsed = []
    for index, value in enumerate(values):
        number = _optional_finite_float(value)
        if number is None:
            raise RuntimeFeatureError("feature_build_failed", "{0}[{1}] must be finite".format(name, index))
        if positive_only and number <= 0.0:
            continue
        parsed.append(float(number))
    return tuple(parsed)


def _required_finite_float(value: object, name: str) -> float:
    parsed = _optional_finite_float(value)
    if parsed is None:
        raise RuntimeFeatureError("missing_required_feature", "{0} must be finite".format(name), (name,))
    return parsed


def _optional_finite_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(parsed):
        return None
    return parsed


def _int_value(value: object, default: int) -> int:
    if isinstance(value, bool):
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _clamp_index(value: int, rates_Bps: Sequence[float]) -> int:
    return max(0, min(int(value), len(rates_Bps) - 1))


def _reject_forbidden_feedback(feedback: Mapping[str, object]) -> None:
    offenders = sorted(str(key) for key in feedback.keys() if str(key) in FORBIDDEN_MODEL_INPUT_KEYS)
    if offenders:
        raise RuntimeFeatureError(
            "feature_build_failed",
            "forbidden runtime model input key(s): {0}".format(", ".join(offenders)),
        )


def _validate_context_features(context: Mapping[str, object]) -> None:
    _reject_forbidden_feedback(context)
    throughput = context.get("throughput_history_bps")
    download_times = context.get("download_time_history_s")
    _validate_numeric_sequence(throughput, "throughput_history_bps", K_CONTEXT)
    _validate_numeric_sequence(download_times, "download_time_history_s", K_CONTEXT)
    for name in CONTEXT_SCALAR_FEATURES:
        _required_finite_float(context.get(name), name)


def _validate_candidate_features(candidate: Mapping[str, object]) -> None:
    _reject_forbidden_feedback(candidate)
    for name in CANDIDATE_FEATURES:
        _required_finite_float(candidate.get(name), name)


def _validate_numeric_sequence(raw_values: object, name: str, expected_length: int) -> None:
    try:
        values = tuple(raw_values)  # type: ignore[arg-type]
    except TypeError as exc:
        raise RuntimeFeatureError("feature_build_failed", "{0} must be a sequence".format(name)) from exc
    if len(values) != expected_length:
        raise RuntimeFeatureError("feature_build_failed", "{0} must have length {1}".format(name, expected_length))
    for index, value in enumerate(values):
        _required_finite_float(value, "{0}[{1}]".format(name, index))
