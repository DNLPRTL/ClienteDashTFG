from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from numbers import Real
from typing import List

from core.neural_abr.action_mask import validate_action_mask
from core.neural_abr.constants import DEFAULT_CONTEXT_HISTORY_LENGTH, FORBIDDEN_MODEL_INPUT_FIELDS
from core.neural_abr.features import audit_feature_payload


class RuntimeFeatureError(ValueError):
    def __init__(self, reason: str, message: str, missing_features: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.reason = reason
        self.missing_features = tuple(str(value) for value in missing_features)


@dataclass(frozen=True)
class RuntimeFeaturePayload:
    context_features: Mapping[str, object]
    candidate_features: tuple[Mapping[str, object], ...]
    action_mask: tuple[bool, ...]
    rates_Bps: tuple[float, ...]
    valid_action_count: int


class NeuralAbrRuntimeFeatureBuilder:
    def __init__(self, history_length: int = DEFAULT_CONTEXT_HISTORY_LENGTH) -> None:
        self.history_length = int(history_length)
        self._throughput_history_bps: List[float] = []
        self._download_time_history_s: List[float] = []
        self._last_sample_key = None
        self._last_observed_level = None
        self._last_recent_switch_abs = 0.0

    def build(self, feedback: Mapping[str, object]) -> RuntimeFeaturePayload:
        self._reject_forbidden_feedback(feedback)
        rates_Bps = self._rates(feedback)
        max_level = self._max_level(feedback, len(rates_Bps))
        action_mask = tuple(index <= max_level for index in range(len(rates_Bps)))
        if not any(action_mask):
            raise RuntimeFeatureError("all_actions_invalid", "action_mask must contain at least one valid action")
        try:
            action_mask = validate_action_mask(action_mask, len(rates_Bps))
        except ValueError as exc:
            reason = "all_actions_invalid" if rates_Bps else "action_mask_invalid"
            raise RuntimeFeatureError(reason, str(exc)) from exc

        valid_action_count = sum(1 for valid in action_mask if valid)
        level = self._required_int(feedback, "level")
        current_level = _clamp(level, 0, len(rates_Bps) - 1)
        queued_time = self._required_finite(feedback, "queued_time")
        fragment_duration = self._required_finite(feedback, "fragment_duration")
        if fragment_duration <= 0.0:
            raise RuntimeFeatureError(
                "missing_required_feature",
                "fragment_duration must be positive",
                ("fragment_duration",),
            )

        self._append_download_sample(feedback)
        recent_switch_abs = self._recent_switch_abs(current_level, feedback)
        last_bitrate_bps = float(rates_Bps[current_level]) * 8.0
        chunks_remaining_norm, has_chunks_remaining = _chunks_remaining(feedback)

        context_features = {
            "throughput_history_bps": _left_pad(self._throughput_history_bps, self.history_length),
            "download_time_history_s": _left_pad(self._download_time_history_s, self.history_length),
            "buffer_s": float(max(queued_time, 0.0)),
            "last_representation_index": float(current_level),
            "last_bitrate_bps": float(last_bitrate_bps),
            "recent_rebuffer_s": 0.0,
            "recent_switch_abs": float(recent_switch_abs),
            "chunks_remaining_norm": float(chunks_remaining_norm),
            "has_chunks_remaining": float(has_chunks_remaining),
        }
        candidate_features = _candidate_features(rates_Bps, fragment_duration, last_bitrate_bps)
        audit = audit_feature_payload(context_features, candidate_features)
        if not audit["passed"]:
            raise RuntimeFeatureError("feature_build_failed", "; ".join(audit["errors"]))
        return RuntimeFeaturePayload(
            context_features=context_features,
            candidate_features=tuple(candidate_features),
            action_mask=action_mask,
            rates_Bps=tuple(rates_Bps),
            valid_action_count=valid_action_count,
        )

    def _reject_forbidden_feedback(self, feedback: Mapping[str, object]) -> None:
        offenders = sorted(str(key) for key in feedback.keys() if str(key) in FORBIDDEN_MODEL_INPUT_FIELDS)
        if offenders:
            raise RuntimeFeatureError(
                "feature_build_failed",
                "forbidden runtime feedback field(s): {0}".format(", ".join(offenders)),
            )

    def _rates(self, feedback: Mapping[str, object]) -> tuple[float, ...]:
        if "rates" not in feedback:
            raise RuntimeFeatureError("missing_required_feature", "rates is required", ("rates",))
        raw_rates = feedback.get("rates")
        if isinstance(raw_rates, (str, bytes)):
            raise RuntimeFeatureError("action_mask_invalid", "rates must be a numeric sequence")
        try:
            values = tuple(raw_rates)  # type: ignore[arg-type]
        except TypeError as exc:
            raise RuntimeFeatureError("action_mask_invalid", "rates must be iterable") from exc
        if not values:
            raise RuntimeFeatureError("all_actions_invalid", "rates must not be empty")
        rates = []
        for index, value in enumerate(values):
            parsed = _finite_number(value)
            if parsed is None or parsed <= 0.0:
                raise RuntimeFeatureError("action_mask_invalid", "invalid rate at index {0}".format(index))
            rates.append(float(parsed))
        return tuple(rates)

    def _max_level(self, feedback: Mapping[str, object], rate_count: int) -> int:
        value = feedback.get("max_level", rate_count - 1)
        parsed = _int_or_none(value)
        if parsed is None:
            raise RuntimeFeatureError("missing_required_feature", "max_level must be numeric", ("max_level",))
        return min(parsed, rate_count - 1)

    def _required_int(self, feedback: Mapping[str, object], key: str) -> int:
        if key not in feedback:
            raise RuntimeFeatureError("missing_required_feature", "{0} is required".format(key), (key,))
        parsed = _int_or_none(feedback.get(key))
        if parsed is None:
            raise RuntimeFeatureError("missing_required_feature", "{0} must be numeric".format(key), (key,))
        return parsed

    def _required_finite(self, feedback: Mapping[str, object], key: str) -> float:
        if key not in feedback:
            raise RuntimeFeatureError("missing_required_feature", "{0} is required".format(key), (key,))
        parsed = _finite_number(feedback.get(key))
        if parsed is None:
            raise RuntimeFeatureError("missing_required_feature", "{0} must be finite".format(key), (key,))
        return float(parsed)

    def _append_download_sample(self, feedback: Mapping[str, object]) -> None:
        size_B = _finite_number(feedback.get("last_fragment_size"))
        download_time_s = _finite_number(feedback.get("last_download_time"))
        if size_B is None or download_time_s is None or size_B <= 0.0 or download_time_s <= 0.0:
            return
        sample_key = (
            _int_or_none(feedback.get("segment_index")),
            float(size_B),
            float(download_time_s),
        )
        if sample_key == self._last_sample_key:
            return
        throughput_bps = 8.0 * float(size_B) / float(download_time_s)
        if not math.isfinite(throughput_bps) or throughput_bps <= 0.0:
            return
        self._throughput_history_bps.append(throughput_bps)
        self._download_time_history_s.append(float(download_time_s))
        self._throughput_history_bps = self._throughput_history_bps[-self.history_length :]
        self._download_time_history_s = self._download_time_history_s[-self.history_length :]
        self._last_sample_key = sample_key

    def _recent_switch_abs(self, current_level: int, feedback: Mapping[str, object]) -> float:
        segment_index = _int_or_none(feedback.get("segment_index"))
        sample_key = (segment_index, current_level)
        if sample_key == getattr(self, "_last_level_sample_key", None):
            return float(self._last_recent_switch_abs)

        if self._last_observed_level is None:
            recent = 0.0
        else:
            recent = float(abs(current_level - self._last_observed_level))
        self._last_observed_level = current_level
        self._last_recent_switch_abs = recent
        self._last_level_sample_key = sample_key
        return recent


def _candidate_features(
    rates_Bps: Sequence[float],
    fragment_duration_s: float,
    last_bitrate_bps: float,
) -> tuple[Mapping[str, object], ...]:
    rates_bps = tuple(float(rate) * 8.0 for rate in rates_Bps)
    min_bitrate = min(rates_bps)
    max_bitrate = max(rates_bps)
    bitrate_span = max(max_bitrate - min_bitrate, 1.0)
    position_denominator = max(len(rates_bps) - 1, 1)
    delta_denominator = max(max_bitrate, 1.0)
    candidates = []
    for index, bitrate_bps in enumerate(rates_bps):
        candidates.append(
            {
                "candidate_representation_index": float(index),
                "candidate_ladder_position_norm": float(index) / float(position_denominator),
                "candidate_bitrate_bps": float(bitrate_bps),
                "candidate_bitrate_norm_ladder": (float(bitrate_bps) - min_bitrate) / bitrate_span,
                "candidate_delta_from_last_bitrate_norm": (
                    0.0 if last_bitrate_bps <= 0.0 else (float(bitrate_bps) - float(last_bitrate_bps)) / delta_denominator
                ),
                "candidate_chunk_size_bytes": float(rates_Bps[index]) * float(fragment_duration_s),
                "candidate_chunk_size_available": 1.0,
            }
        )
    return tuple(candidates)


def _chunks_remaining(feedback: Mapping[str, object]) -> tuple[float, float]:
    total = _int_or_none(feedback.get("total_segments"))
    index = _int_or_none(feedback.get("segment_index"))
    if total is None or index is None or total <= 0:
        return 0.0, 0.0
    remaining = max(total - index - 1, 0)
    return float(remaining) / float(total), 1.0 if remaining > 0 else 0.0


def _left_pad(values: Sequence[float], expected: int) -> tuple[float, ...]:
    materialized = tuple(float(value) for value in values)
    if len(materialized) >= expected:
        return materialized[-expected:]
    return tuple(0.0 for _ in range(expected - len(materialized))) + materialized


def _finite_number(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, Real):
        return None
    parsed = float(value)
    if not math.isfinite(parsed):
        return None
    return parsed


def _int_or_none(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _clamp(value: int, lower: int, upper: int) -> int:
    return max(lower, min(int(value), upper))
