from __future__ import annotations

import csv
import hashlib
import math
from pathlib import Path
from typing import Iterable, Mapping

from core.trace_replay.schema import NormalizedTraceStats, REQUIRED_COLUMNS, has_required_columns


class TraceValidationError(ValueError):
    """Raised when a normalized trace does not satisfy schema_v1."""


def _as_float(value: object, column: str, row_number: int) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise TraceValidationError("row {0}: {1} is not numeric".format(row_number, column)) from exc
    if not math.isfinite(parsed):
        raise TraceValidationError("row {0}: {1} must be finite".format(row_number, column))
    return parsed


def validate_normalized_trace_rows(rows: Iterable[Mapping[str, object]], source: str = "<rows>") -> NormalizedTraceStats:
    previous_timestamp: float | None = None
    row_count = 0
    duration_total = 0.0
    throughput_total = 0.0
    throughput_min: float | None = None
    throughput_max: float | None = None
    fingerprint = hashlib.sha256()

    for row_count, row in enumerate(rows, start=1):
        missing = [column for column in REQUIRED_COLUMNS if column not in row]
        if missing:
            raise TraceValidationError("{0}: row {1}: missing columns {2}".format(source, row_count, ", ".join(missing)))

        timestamp_s = _as_float(row["timestamp_s"], "timestamp_s", row_count)
        duration_s = _as_float(row["duration_s"], "duration_s", row_count)
        throughput_kbps = _as_float(row["throughput_kbps"], "throughput_kbps", row_count)

        if timestamp_s < 0:
            raise TraceValidationError("{0}: row {1}: timestamp_s must be >= 0".format(source, row_count))
        if previous_timestamp is not None and timestamp_s < previous_timestamp:
            raise TraceValidationError("{0}: row {1}: timestamp_s must be nondecreasing".format(source, row_count))
        if duration_s <= 0:
            raise TraceValidationError("{0}: row {1}: duration_s must be > 0".format(source, row_count))
        if throughput_kbps < 0:
            raise TraceValidationError("{0}: row {1}: throughput_kbps must be >= 0".format(source, row_count))

        previous_timestamp = timestamp_s
        duration_total += duration_s
        throughput_total += throughput_kbps
        throughput_min = throughput_kbps if throughput_min is None else min(throughput_min, throughput_kbps)
        throughput_max = throughput_kbps if throughput_max is None else max(throughput_max, throughput_kbps)
        fingerprint.update("{0:.9f},{1:.9f},{2:.9f}\n".format(timestamp_s, duration_s, throughput_kbps).encode("ascii"))

    if row_count == 0:
        raise TraceValidationError("{0}: trace must not be empty".format(source))

    return NormalizedTraceStats(
        row_count=row_count,
        duration_s=duration_total,
        throughput_min_kbps=throughput_min if throughput_min is not None else 0.0,
        throughput_mean_kbps=throughput_total / row_count,
        throughput_max_kbps=throughput_max if throughput_max is not None else 0.0,
        content_fingerprint_sha256=fingerprint.hexdigest(),
    )


def validate_normalized_trace_csv(path: str | Path) -> NormalizedTraceStats:
    csv_path = Path(path)
    with csv_path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not has_required_columns(reader.fieldnames):
            raise TraceValidationError(
                "{0}: expected required columns {1}".format(csv_path, ", ".join(REQUIRED_COLUMNS))
            )
        return validate_normalized_trace_rows(reader, source=str(csv_path))
