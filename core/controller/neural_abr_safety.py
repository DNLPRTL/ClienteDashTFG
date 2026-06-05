from __future__ import annotations

import math
from collections.abc import Sequence


class NeuralAbrSafetyError(ValueError):
    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = reason


def safe_action_to_rate(
    action: object,
    action_mask: Sequence[bool],
    rates_Bps: Sequence[float],
) -> tuple[int, float]:
    if isinstance(action, bool):
        raise NeuralAbrSafetyError("selected_masked_action", "action must be an integer")
    try:
        parsed_action = int(action)
    except (TypeError, ValueError) as exc:
        raise NeuralAbrSafetyError("selected_masked_action", "action must be an integer") from exc
    if parsed_action < 0 or parsed_action >= len(action_mask):
        raise NeuralAbrSafetyError("selected_masked_action", "action is outside the action mask")
    if not bool(action_mask[parsed_action]):
        raise NeuralAbrSafetyError("selected_masked_action", "action is masked")
    if parsed_action >= len(rates_Bps):
        raise NeuralAbrSafetyError("selected_masked_action", "action is outside the rate ladder")
    rate = float(rates_Bps[parsed_action])
    if not math.isfinite(rate) or rate <= 0.0:
        raise NeuralAbrSafetyError("safety_guard_rejected", "selected rate is not finite and positive")
    return parsed_action, rate


def lowest_valid_action(action_mask: Sequence[bool]) -> int | None:
    for index, valid in enumerate(action_mask):
        if valid:
            return index
    return None

