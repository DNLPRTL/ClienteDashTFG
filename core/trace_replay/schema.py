from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


NORMALIZED_TRACE_SCHEMA_ID = "normalized_trace_schema_v1"
REQUIRED_COLUMNS = ("timestamp_s", "duration_s", "throughput_kbps")


@dataclass(frozen=True)
class NormalizedTraceStats:
    row_count: int
    duration_s: float
    throughput_min_kbps: float
    throughput_mean_kbps: float
    throughput_max_kbps: float
    content_fingerprint_sha256: str


def has_required_columns(fieldnames: Sequence[str] | None) -> bool:
    if fieldnames is None:
        return False
    available = set(fieldnames)
    return all(column in available for column in REQUIRED_COLUMNS)


def row_projection(row: Mapping[str, object]) -> tuple[object, object, object]:
    return tuple(row[column] for column in REQUIRED_COLUMNS)
