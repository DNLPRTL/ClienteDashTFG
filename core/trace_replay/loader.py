from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from core.trace_replay.validation import TraceValidationError, validate_normalized_trace_csv, validate_normalized_trace_rows


class TraceLoadError(RuntimeError):
    """Raised when a normalized trace cannot be loaded."""


@dataclass(frozen=True)
class TraceSample:
    timestamp_s: float
    duration_s: float
    throughput_kbps: float


@dataclass(frozen=True)
class LoadedTrace:
    trace_id: str
    samples: tuple[TraceSample, ...]
    duration_s: float
    throughput_min_kbps: float
    throughput_mean_kbps: float
    throughput_max_kbps: float
    content_fingerprint_sha256: str


def _sample_from_row(row: Mapping[str, object], row_number: int) -> TraceSample:
    try:
        return TraceSample(
            timestamp_s=float(row["timestamp_s"]),
            duration_s=float(row["duration_s"]),
            throughput_kbps=float(row["throughput_kbps"]),
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise TraceLoadError("row {0}: cannot build TraceSample".format(row_number)) from exc


def load_normalized_trace_rows(rows: Iterable[Mapping[str, object]], trace_id: str = "<rows>") -> LoadedTrace:
    materialized = list(rows)
    try:
        stats = validate_normalized_trace_rows(materialized, source=trace_id)
    except TraceValidationError as exc:
        raise TraceLoadError(str(exc)) from exc

    samples = tuple(_sample_from_row(row, index) for index, row in enumerate(materialized, start=1))
    return LoadedTrace(
        trace_id=trace_id,
        samples=samples,
        duration_s=stats.duration_s,
        throughput_min_kbps=stats.throughput_min_kbps,
        throughput_mean_kbps=stats.throughput_mean_kbps,
        throughput_max_kbps=stats.throughput_max_kbps,
        content_fingerprint_sha256=stats.content_fingerprint_sha256,
    )


def load_normalized_trace_csv(path: str | Path, trace_id: str | None = None) -> LoadedTrace:
    csv_path = Path(path)
    try:
        stats = validate_normalized_trace_csv(csv_path)
        with csv_path.open("r", newline="", encoding="utf-8") as handle:
            rows: Sequence[Mapping[str, object]] = tuple(csv.DictReader(handle))
    except (OSError, TraceValidationError) as exc:
        raise TraceLoadError(str(exc)) from exc

    samples = tuple(_sample_from_row(row, index) for index, row in enumerate(rows, start=1))
    return LoadedTrace(
        trace_id=trace_id or csv_path.stem,
        samples=samples,
        duration_s=stats.duration_s,
        throughput_min_kbps=stats.throughput_min_kbps,
        throughput_mean_kbps=stats.throughput_mean_kbps,
        throughput_max_kbps=stats.throughput_max_kbps,
        content_fingerprint_sha256=stats.content_fingerprint_sha256,
    )
