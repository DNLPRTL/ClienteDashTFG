from __future__ import annotations

from typing import Iterable, Sequence

from core.neural_abr.content_ladder import ContentLadder


class ActionMaskError(ValueError):
    """Raised when an action or action mask is invalid."""


def build_action_mask(ladder: ContentLadder, segment_index: int) -> tuple[bool, ...]:
    if segment_index < 0 or segment_index >= ladder.segment_count:
        return tuple(False for _ in range(ladder.representation_count))
    return tuple(True for _ in range(ladder.representation_count))


def validate_action_mask(action_mask: Iterable[object], representation_count: int) -> tuple[bool, ...]:
    try:
        mask = tuple(bool(value) for value in action_mask)
    except TypeError as exc:
        raise ActionMaskError("action_mask must be iterable") from exc
    if len(mask) != representation_count:
        raise ActionMaskError("action_mask length must match representation_count")
    if not any(mask):
        raise ActionMaskError("action_mask must contain at least one valid action")
    return mask


def assert_action_valid(representation_index: int, action_mask: Sequence[bool]) -> None:
    if isinstance(representation_index, bool) or not isinstance(representation_index, int):
        raise ActionMaskError("representation_index must be an integer")
    if representation_index < 0 or representation_index >= len(action_mask):
        raise ActionMaskError("representation_index is outside the action mask")
    if not bool(action_mask[representation_index]):
        raise ActionMaskError("representation_index is masked out")


def lowest_valid_action(action_mask: Sequence[bool]) -> int:
    for index, valid in enumerate(action_mask):
        if valid:
            return index
    raise ActionMaskError("action_mask must contain at least one valid action")

