from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence

from core.neural_abr.constants import (
    DEFAULT_MAX_BUFFER_S,
    DEFAULT_REPRESENTATION_KBPS,
    DEFAULT_SEGMENT_DURATION_S,
)


class ContentLadderError(ValueError):
    """Raised when the offline content ladder is invalid."""


@dataclass(frozen=True)
class Representation:
    representation_index: int
    bitrate_bps: int


@dataclass(frozen=True)
class ContentLadder:
    representations: tuple[Representation, ...]
    segment_duration_s: float = DEFAULT_SEGMENT_DURATION_S
    segment_count: int = 1
    max_buffer_s: float = DEFAULT_MAX_BUFFER_S

    def __post_init__(self) -> None:
        _validate_ladder(self)

    @property
    def representation_count(self) -> int:
        return len(self.representations)

    @property
    def bitrates_bps(self) -> tuple[int, ...]:
        return tuple(representation.bitrate_bps for representation in self.representations)

    @property
    def min_bitrate_bps(self) -> int:
        return min(self.bitrates_bps)

    @property
    def max_bitrate_bps(self) -> int:
        return max(self.bitrates_bps)

    def bitrate_bps(self, representation_index: int) -> int:
        self.validate_representation_index(representation_index)
        return self.representations[representation_index].bitrate_bps

    def validate_representation_index(self, representation_index: int) -> None:
        if isinstance(representation_index, bool) or not isinstance(representation_index, int):
            raise ContentLadderError("representation_index must be an integer")
        if representation_index < 0 or representation_index >= self.representation_count:
            raise ContentLadderError("representation_index is outside the ladder")

    def segment_size_bytes(self, representation_index: int, segment_index: int) -> int:
        self.validate_representation_index(representation_index)
        if isinstance(segment_index, bool) or not isinstance(segment_index, int):
            raise ContentLadderError("segment_index must be an integer")
        if segment_index < 0 or segment_index >= self.segment_count:
            raise ContentLadderError("segment_index is outside the content duration")
        return max(1, int(round(self.bitrate_bps(representation_index) * self.segment_duration_s / 8.0)))

    def to_manifest(self) -> Mapping[str, object]:
        return {
            "representation_count": self.representation_count,
            "bitrates_bps": list(self.bitrates_bps),
            "segment_duration_s": self.segment_duration_s,
            "segment_count": self.segment_count,
            "max_buffer_s": self.max_buffer_s,
            "segment_size_source": "bitrate_times_duration_bytes",
        }


def default_training_ladder(
    segment_duration_s: float = DEFAULT_SEGMENT_DURATION_S,
    segment_count: int = 30,
    representation_kbps: Sequence[int] = DEFAULT_REPRESENTATION_KBPS,
    max_buffer_s: float = DEFAULT_MAX_BUFFER_S,
) -> ContentLadder:
    representations = tuple(
        Representation(representation_index=index, bitrate_bps=int(kbps) * 1000)
        for index, kbps in enumerate(representation_kbps)
    )
    return ContentLadder(
        representations=representations,
        segment_duration_s=float(segment_duration_s),
        segment_count=int(segment_count),
        max_buffer_s=float(max_buffer_s),
    )


def _validate_ladder(ladder: ContentLadder) -> None:
    if not ladder.representations:
        raise ContentLadderError("content ladder must not be empty")
    if isinstance(ladder.segment_count, bool) or not isinstance(ladder.segment_count, int) or ladder.segment_count <= 0:
        raise ContentLadderError("segment_count must be a positive integer")
    for name, value in (("segment_duration_s", ladder.segment_duration_s), ("max_buffer_s", ladder.max_buffer_s)):
        if isinstance(value, bool):
            raise ContentLadderError("{0} must be finite and positive".format(name))
        numeric = float(value)
        if not math.isfinite(numeric) or numeric <= 0.0:
            raise ContentLadderError("{0} must be finite and positive".format(name))
    expected_indices = tuple(range(len(ladder.representations)))
    actual_indices = tuple(representation.representation_index for representation in ladder.representations)
    if actual_indices != expected_indices:
        raise ContentLadderError("representation indices must be contiguous and zero-based")
    previous_bitrate = 0
    for representation in ladder.representations:
        if representation.bitrate_bps <= previous_bitrate:
            raise ContentLadderError("representations must be sorted by increasing bitrate")
        previous_bitrate = representation.bitrate_bps

