"""Content ladder and segment-size helpers for offline NeuralABR-Lite."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Optional, Sequence, Tuple

from core.neural_abr.constants import DEFAULT_MAX_BUFFER_S, DEFAULT_SEGMENT_DURATION_S


class ContentLadderError(ValueError):
    """Raised when a content ladder violates the representation contract."""


@dataclass(frozen=True)
class Representation:
    representation_index: int
    bitrate_bps: int


@dataclass(frozen=True)
class ContentLadder:
    representations: Tuple[Representation, ...]
    segment_duration_s: float = DEFAULT_SEGMENT_DURATION_S
    segment_count: int = 1
    max_buffer_s: float = DEFAULT_MAX_BUFFER_S
    segment_size_table: Optional[Tuple[Tuple[int, ...], ...]] = None

    def __post_init__(self) -> None:
        _validate_ladder(self)

    @property
    def representation_count(self) -> int:
        return len(self.representations)

    @property
    def bitrates_bps(self) -> Tuple[int, ...]:
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

        if self.segment_size_table is not None:
            return self.segment_size_table[segment_index][representation_index]

        return max(1, int(round(self.bitrate_bps(representation_index) * self.segment_duration_s / 8.0)))

    def segment_sizes_bytes(self, segment_index: int) -> Tuple[int, ...]:
        return tuple(self.segment_size_bytes(index, segment_index) for index in range(self.representation_count))

    def to_manifest(self) -> Mapping[str, object]:
        return {
            "representation_count": self.representation_count,
            "bitrates_bps": list(self.bitrates_bps),
            "segment_duration_s": self.segment_duration_s,
            "segment_count": self.segment_count,
            "max_buffer_s": self.max_buffer_s,
            "segment_size_source": "explicit_table" if self.segment_size_table is not None else "bitrate_duration",
        }


def synthetic_smoke_ladder(segment_count: int = 12) -> ContentLadder:
    bitrates_bps = (300_000, 750_000, 1_200_000, 1_850_000)
    table = []
    for segment_index in range(segment_count):
        multiplier = 0.94 + 0.02 * (segment_index % 4)
        row = []
        for bitrate_bps in bitrates_bps:
            row.append(max(1, int(round(bitrate_bps * DEFAULT_SEGMENT_DURATION_S * multiplier / 8.0))))
        table.append(tuple(row))
    return ContentLadder(
        representations=tuple(
            Representation(representation_index=index, bitrate_bps=bitrate_bps)
            for index, bitrate_bps in enumerate(bitrates_bps)
        ),
        segment_duration_s=DEFAULT_SEGMENT_DURATION_S,
        segment_count=segment_count,
        max_buffer_s=DEFAULT_MAX_BUFFER_S,
        segment_size_table=tuple(table),
    )


def _validate_ladder(ladder: ContentLadder) -> None:
    if not ladder.representations:
        raise ContentLadderError("content ladder must not be empty")
    if isinstance(ladder.segment_count, bool) or not isinstance(ladder.segment_count, int) or ladder.segment_count <= 0:
        raise ContentLadderError("segment_count must be a positive integer")
    for name, value in (("segment_duration_s", ladder.segment_duration_s), ("max_buffer_s", ladder.max_buffer_s)):
        if isinstance(value, bool):
            raise ContentLadderError("{0} must be finite and positive".format(name))
        try:
            numeric = float(value)
        except (TypeError, ValueError) as exc:
            raise ContentLadderError("{0} must be finite and positive".format(name)) from exc
        if not math.isfinite(numeric) or numeric <= 0.0:
            raise ContentLadderError("{0} must be finite and positive".format(name))

    expected_indices = tuple(range(len(ladder.representations)))
    actual_indices = tuple(representation.representation_index for representation in ladder.representations)
    if actual_indices != expected_indices:
        raise ContentLadderError("representation indices must be contiguous and zero-based")

    previous_bitrate = 0
    for representation in ladder.representations:
        if isinstance(representation.bitrate_bps, bool) or not isinstance(representation.bitrate_bps, int):
            raise ContentLadderError("bitrate_bps must be an integer")
        if representation.bitrate_bps <= 0:
            raise ContentLadderError("bitrate_bps must be positive")
        if representation.bitrate_bps <= previous_bitrate:
            raise ContentLadderError("representations must be sorted by increasing bitrate")
        previous_bitrate = representation.bitrate_bps

    if ladder.segment_size_table is None:
        return
    if len(ladder.segment_size_table) != ladder.segment_count:
        raise ContentLadderError("segment_size_table must contain one row per segment")
    for segment_index, row in enumerate(ladder.segment_size_table):
        if len(row) != len(ladder.representations):
            raise ContentLadderError("segment_size_table row {0} has wrong length".format(segment_index))
        for size_bytes in row:
            if isinstance(size_bytes, bool) or not isinstance(size_bytes, int) or size_bytes <= 0:
                raise ContentLadderError("segment sizes must be positive integers")
