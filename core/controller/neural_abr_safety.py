"""Runtime safety guard and classical fallback for NeuralABR-Lite."""

from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Real
from typing import Mapping, Sequence

from core.controller.bba import BbaController
from core.controller.mpc import MpcController
from core.controller.rate_based import RateBasedController
from core.controller.robust_mpc import RobustMpcController
from core.controller.sanity_rate import MinRateController


DEFAULT_FALLBACK_ORDER = ("robust_mpc", "mpc", "rate_based", "bba", "min_rate")


@dataclass(frozen=True)
class SafetyDecision:
    action: int | None
    rate_Bps: float | None
    intervened: bool
    fallback_required: bool
    reason: str


@dataclass(frozen=True)
class FallbackDecision:
    action: int
    rate_Bps: float
    reason: str
    controller_name: str


def apply_safety_guard(
    raw_action: int,
    rates_Bps: Sequence[object],
    action_mask: Sequence[bool],
    feedback: Mapping[str, object],
    throughput_history_Bps: Sequence[object],
    *,
    safety_buffer_margin_s: float = 1.0,
    safety_throughput_factor: float = 0.85,
) -> SafetyDecision:
    rates = _valid_rates(rates_Bps)
    if raw_action < 0 or raw_action >= len(rates) or not bool(action_mask[raw_action]):
        return SafetyDecision(None, None, True, True, "selected_masked_action")

    buffer_s = _finite_float(feedback.get("queued_time"))
    fragment_duration_s = _finite_float(feedback.get("fragment_duration"))
    recent_throughput = _recent_throughput_Bps(throughput_history_Bps)
    if buffer_s is None or fragment_duration_s is None or fragment_duration_s <= 0.0 or recent_throughput is None:
        return SafetyDecision(None, None, True, True, "safety_guard_rejected")

    throughput_factor = _bounded_unit(safety_throughput_factor, 0.85)
    conservative_throughput_Bps = max(recent_throughput * throughput_factor, 1e-9)
    margin = max(float(safety_buffer_margin_s), 0.0)
    deadline_s = max(float(buffer_s) - margin, float(fragment_duration_s))

    raw_estimated_download_time_s = _estimated_download_time_s(raw_action, rates, conservative_throughput_Bps, fragment_duration_s)
    if raw_estimated_download_time_s is None:
        return SafetyDecision(None, None, True, True, "safety_guard_rejected")
    if raw_estimated_download_time_s <= float(deadline_s):
        return SafetyDecision(raw_action, float(rates[raw_action]), False, False, "success_neural")

    for action in range(raw_action - 1, -1, -1):
        estimated_download_time_s = _estimated_download_time_s(
            action,
            rates,
            conservative_throughput_Bps,
            fragment_duration_s,
        )
        if bool(action_mask[action]) and estimated_download_time_s is not None and estimated_download_time_s <= float(deadline_s):
            return SafetyDecision(action, float(rates[action]), True, False, "success_neural")

    lowest = lowest_valid_action(action_mask)
    lowest_estimated_download_time_s = _estimated_download_time_s(
        lowest,
        rates,
        conservative_throughput_Bps,
        fragment_duration_s,
    )
    if lowest_estimated_download_time_s is None:
        return SafetyDecision(None, None, True, True, "safety_guard_rejected")
    return SafetyDecision(
        lowest,
        float(rates[lowest]),
        True,
        False,
        "emergency_lowest_representation",
    )


def select_fallback_action(
    feedback: Mapping[str, object],
    rates_Bps: Sequence[object],
    action_mask: Sequence[bool],
    *,
    fallback_controller: str = "robust_mpc",
    fallback_params: Mapping[str, object] | None = None,
) -> FallbackDecision:
    rates = _valid_rates(rates_Bps)
    if not rates:
        return FallbackDecision(0, 0.0, "fallback_controller_failed", "none")

    preferred = str(fallback_controller or "robust_mpc").strip().lower()
    order = []
    for name in (preferred, *DEFAULT_FALLBACK_ORDER):
        if name in DEFAULT_FALLBACK_ORDER and name not in order:
            order.append(name)

    for name in order:
        try:
            controller = _create_fallback_controller(name, fallback_params if name == preferred else None)
            controller.setPlayerFeedback(dict(feedback))
            target_rate = controller.calcControlAction()
            action = quantize_to_valid_action(target_rate, rates, action_mask)
            return FallbackDecision(action, float(rates[action]), name, name)
        except Exception:
            continue

    lowest = lowest_valid_action(action_mask)
    return FallbackDecision(
        lowest,
        float(rates[lowest]),
        "fallback_controller_failed",
        "lowest_valid_representation",
    )


def quantize_to_valid_action(rate: object, rates_Bps: Sequence[object], action_mask: Sequence[bool]) -> int:
    rates = _valid_rates(rates_Bps)
    target = _finite_float(rate)
    if target is None:
        return lowest_valid_action(action_mask)

    chosen = None
    for index, rate_Bps in enumerate(rates):
        if not bool(action_mask[index]):
            continue
        if target >= float(rate_Bps):
            chosen = index
    if chosen is not None:
        return int(chosen)
    return lowest_valid_action(action_mask)


def lowest_valid_action(action_mask: Sequence[bool]) -> int:
    for index, valid in enumerate(action_mask):
        if bool(valid):
            return int(index)
    raise ValueError("action_mask must contain at least one valid action")


def _estimated_download_time_s(
    action: int,
    rates_Bps: Sequence[float],
    conservative_throughput_Bps: float,
    fragment_duration_s: float,
) -> float | None:
    candidate_size_bytes = float(rates_Bps[action]) * float(fragment_duration_s)
    estimated_download_time_s = candidate_size_bytes / conservative_throughput_Bps
    if not math.isfinite(estimated_download_time_s):
        return None
    return float(estimated_download_time_s)


def _create_fallback_controller(name: str, params: Mapping[str, object] | None):
    factories = {
        "robust_mpc": RobustMpcController,
        "mpc": MpcController,
        "rate_based": RateBasedController,
        "bba": BbaController,
        "min_rate": MinRateController,
    }
    factory = factories[name]
    return factory(**dict(params or {}))


def _valid_rates(rates_Bps: Sequence[object]) -> tuple[float, ...]:
    rates = []
    for index, value in enumerate(rates_Bps):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise ValueError("rate {0} must be numeric".format(index))
        rate = float(value)
        if not math.isfinite(rate) or rate <= 0.0:
            raise ValueError("rate {0} must be positive finite".format(index))
        rates.append(rate)
    return tuple(rates)


def _recent_throughput_Bps(values: Sequence[object]) -> float | None:
    parsed = []
    for value in values:
        sample = _finite_float(value)
        if sample is not None and sample > 0.0:
            parsed.append(sample)
    if not parsed:
        return None
    return min(parsed[-5:])


def _finite_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(parsed):
        return None
    return parsed


def _bounded_unit(value: object, default: float) -> float:
    parsed = _finite_float(value)
    if parsed is None or parsed <= 0.0 or parsed > 1.0:
        return float(default)
    return float(parsed)
