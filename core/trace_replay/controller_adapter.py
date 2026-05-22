"""Controller adapter boundary for Phase 3.4C trace dry-runs.

The adapter calls existing Phase 2 controllers through the public
dict-feedback contract and registry. It deliberately exposes only normal
client/controller feedback, never complete traces or future samples.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Integral, Real
from typing import Mapping, Optional, Protocol, Sequence

from core.controller.contract import REQUIRED_FEEDBACK_KEYS, quantize_rate_to_level, validate_feedback_keys
from core.controller.registry import create_controller


INVALID_DECISION_CLAMP = "clamp"
INVALID_DECISION_REJECT = "reject"

FORBIDDEN_FEEDBACK_KEYS = frozenset(
    {
        "trace",
        "loaded_trace",
        "full_trace",
        "trace_samples",
        "samples",
        "future_samples",
        "future_trace_samples",
        "future_throughput",
        "future_throughput_kbps",
        "raw_trace_metadata",
        "trace_metadata",
        "metadata",
        "ood_label",
        "split",
        "domain_label",
        "leakage_group",
    }
)

ALLOWED_EXTRA_FEEDBACK_KEYS = frozenset(
    {
        "rates_unit",
        "max_buffer_time",
    }
)

ALLOWED_FEEDBACK_KEYS = frozenset(REQUIRED_FEEDBACK_KEYS) | ALLOWED_EXTRA_FEEDBACK_KEYS


class ControllerAdapterError(ValueError):
    """Raised when a controller cannot be adapted safely for dry-run use."""


@dataclass(frozen=True)
class ControllerDecision:
    representation_index: int
    reason: Optional[str] = None
    raw_controller_output: Optional[object] = None


class ControllerAdapter(Protocol):
    @property
    def name(self) -> str:
        """Controller name used in dry-run records."""

    def decide(self, feedback: Mapping[str, object]) -> ControllerDecision:
        """Return the next representation index from current feedback only."""

    def reset(self) -> None:
        """Reset adapter/controller state when supported."""


class ExistingControllerAdapter:
    """Wrap a registered project controller behind the dry-run decision API."""

    def __init__(
        self,
        controller_name: str,
        controller_params: Optional[Mapping[str, object]] = None,
        invalid_decision_policy: str = INVALID_DECISION_CLAMP,
        controller: Optional[object] = None,
    ):
        if invalid_decision_policy not in (INVALID_DECISION_CLAMP, INVALID_DECISION_REJECT):
            raise ControllerAdapterError("invalid_decision_policy must be 'clamp' or 'reject'")

        self._name = str(controller_name)
        self._controller_params = dict(controller_params or {})
        self._invalid_decision_policy = invalid_decision_policy
        self._injected_controller = controller
        self._controller = controller if controller is not None else self._create_controller()

    @property
    def name(self) -> str:
        return self._name

    def reset(self) -> None:
        if self._injected_controller is None:
            self._controller = self._create_controller()
            return

        reset = getattr(self._controller, "reset", None)
        if callable(reset):
            reset()

    def decide(self, feedback: Mapping[str, object]) -> ControllerDecision:
        safe_feedback = _sanitize_feedback(feedback)
        rates = _validate_rates_from_feedback(safe_feedback)

        set_feedback = getattr(self._controller, "setPlayerFeedback", None)
        calc_action = getattr(self._controller, "calcControlAction", None)
        if not callable(set_feedback) or not callable(calc_action):
            raise ControllerAdapterError(
                "controller '{0}' does not implement the public feedback/action contract".format(self.name)
            )

        try:
            set_feedback(dict(safe_feedback))
            raw_output = calc_action()
            if raw_output is None:
                get_action = getattr(self._controller, "getControlAction", None)
                if callable(get_action):
                    raw_output = get_action()
        except Exception as exc:
            raise ControllerAdapterError("controller '{0}' decision failed: {1}".format(self.name, exc)) from exc

        level, reason = self._normalize_controller_output(raw_output, rates)
        controller_reason = _controller_reason(self._controller)
        if controller_reason:
            reason = "{0}; {1}".format(reason, controller_reason)

        return ControllerDecision(
            representation_index=level,
            reason=reason,
            raw_controller_output=_safe_raw_controller_output(raw_output),
        )

    def _create_controller(self):
        try:
            return create_controller(self.name, params=self._controller_params)
        except ValueError as exc:
            raise ControllerAdapterError(str(exc)) from exc

    def _normalize_controller_output(self, raw_output: object, rates: Sequence[float]):
        if isinstance(raw_output, Mapping):
            for key in ("representation_index", "quality_index", "level"):
                if key in raw_output:
                    return self._normalize_index(raw_output.get(key), len(rates), "controller_index")
            for key in ("target_rate_Bps", "target_rate", "rate", "bitrate"):
                if key in raw_output:
                    return _quantize_rate(raw_output.get(key), rates), "controller_rate_quantized"
            raise ControllerAdapterError("controller mapping output does not contain a supported decision key")

        return _quantize_rate(raw_output, rates), "controller_rate_quantized"

    def _normalize_index(self, raw_index: object, representation_count: int, reason: str):
        if isinstance(raw_index, bool) or not isinstance(raw_index, Integral):
            raise ControllerAdapterError("controller representation index must be an integer")
        index = int(raw_index)
        if 0 <= index < representation_count:
            return index, reason

        if self._invalid_decision_policy == INVALID_DECISION_REJECT:
            raise ControllerAdapterError(
                "controller representation index {0} outside ladder [0, {1}]".format(
                    index,
                    representation_count - 1,
                )
            )

        clamped = max(0, min(index, representation_count - 1))
        return clamped, "{0}_clamped".format(reason)


def _sanitize_feedback(feedback: Mapping[str, object]) -> Mapping[str, object]:
    if not isinstance(feedback, Mapping):
        raise ControllerAdapterError("controller feedback must be a mapping")

    forbidden = sorted(key for key in feedback if key in FORBIDDEN_FEEDBACK_KEYS)
    if forbidden:
        raise ControllerAdapterError(
            "controller feedback contains forbidden future/non-client keys: {0}".format(", ".join(forbidden))
        )

    unknown = sorted(key for key in feedback if key not in ALLOWED_FEEDBACK_KEYS)
    if unknown:
        raise ControllerAdapterError(
            "controller feedback contains keys outside the controlled dry-run allowlist: {0}".format(
                ", ".join(unknown)
            )
        )

    try:
        validate_feedback_keys(feedback)
    except ValueError as exc:
        raise ControllerAdapterError(str(exc)) from exc

    return dict(feedback)


def _validate_rates_from_feedback(feedback: Mapping[str, object]):
    rates = feedback.get("rates")
    if not rates:
        raise ControllerAdapterError("controller feedback rates ladder must not be empty")
    normalized = []
    try:
        values = list(rates)
    except TypeError as exc:
        raise ControllerAdapterError("controller feedback rates ladder must be iterable") from exc
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise ControllerAdapterError("controller feedback rates ladder has a non-numeric value at index {0}".format(index))
        rate = float(value)
        if not math.isfinite(rate) or rate <= 0.0:
            raise ControllerAdapterError("controller feedback rates ladder has a non-positive value at index {0}".format(index))
        normalized.append(rate)
    return normalized


def _quantize_rate(raw_rate: object, rates: Sequence[float]) -> int:
    if isinstance(raw_rate, bool) or not isinstance(raw_rate, Real):
        raise ControllerAdapterError("controller target rate must be numeric")
    rate = float(raw_rate)
    if not math.isfinite(rate):
        raise ControllerAdapterError("controller target rate must be finite")
    try:
        return quantize_rate_to_level(rate, rates)
    except ValueError as exc:
        raise ControllerAdapterError(str(exc)) from exc


def _controller_reason(controller: object) -> Optional[str]:
    metrics = getattr(controller, "last_metrics", None)
    if not isinstance(metrics, Mapping):
        return None
    reason = metrics.get("reason")
    if reason is None:
        return None
    text = str(reason)
    if len(text) > 120:
        return text[:117] + "..."
    return text


def _safe_raw_controller_output(raw_output: object) -> object:
    if raw_output is None or isinstance(raw_output, (str, int, float, bool)):
        return raw_output

    if isinstance(raw_output, Mapping):
        safe = {}
        for index, key in enumerate(raw_output):
            if index >= 12:
                safe["..."] = "truncated"
                break
            safe[str(key)] = _safe_value(raw_output[key])
        return safe

    if isinstance(raw_output, (list, tuple)):
        return "{0}(len={1})".format(type(raw_output).__name__, len(raw_output))

    return type(raw_output).__name__


def _safe_value(value: object) -> object:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, (list, tuple)):
        return "{0}(len={1})".format(type(value).__name__, len(value))
    if isinstance(value, Mapping):
        return "mapping(len={0})".format(len(value))
    return type(value).__name__
