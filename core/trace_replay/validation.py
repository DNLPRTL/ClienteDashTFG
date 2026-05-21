"""Validation for normalized Phase 3 trace rows and CSV files."""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Optional, Sequence, Tuple

from core.trace_replay.schema import REQUIRED_TRACE_COLUMNS


@dataclass(frozen=True)
class TraceValidationResult:
    is_valid: bool
    sample_count: int
    duration_s: float
    min_throughput_kbps: Optional[float]
    mean_throughput_kbps: Optional[float]
    max_throughput_kbps: Optional[float]
    nominal_granularity_s: Optional[float]
    has_zero_throughput: bool
    errors: Tuple[str, ...]
    warnings: Tuple[str, ...]


def validate_normalized_trace_csv(path: object) -> TraceValidationResult:
    """Validate a CSV file that should follow normalized_trace_schema_v1.

    Missing files intentionally raise FileNotFoundError. Malformed contents
    return a TraceValidationResult with is_valid=False and human-readable
    errors.
    """

    csv_path = Path(path)
    with csv_path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = tuple(reader.fieldnames or ())
        rows = list(reader)

    missing_columns = tuple(column for column in REQUIRED_TRACE_COLUMNS if column not in fieldnames)
    return _validate_rows(rows, source=str(csv_path), missing_columns=missing_columns)


def validate_normalized_trace_rows(
    rows: Iterable[Mapping[str, object]],
    source: str = "<memory>",
) -> TraceValidationResult:
    """Validate in-memory rows that should follow normalized_trace_schema_v1."""

    return _validate_rows(tuple(rows), source=source, missing_columns=())


def _validate_rows(
    rows: Sequence[Mapping[str, object]],
    source: str,
    missing_columns: Sequence[str],
) -> TraceValidationResult:
    errors = []
    warnings = []
    durations = []
    throughputs = []
    previous_timestamp = None

    if missing_columns:
        errors.append(
            "{0}: missing required columns: {1}".format(
                source,
                ", ".join(missing_columns),
            )
        )

    if not rows:
        errors.append("{0}: trace has no samples".format(source))

    for row_index, row in enumerate(rows, start=1):
        parsed = {}
        row_has_error = False

        for column in REQUIRED_TRACE_COLUMNS:
            if column in missing_columns:
                row_has_error = True
                continue
            if column not in row:
                errors.append("{0}: row {1}: missing required column {2}".format(source, row_index, column))
                row_has_error = True
                continue

            value, error = _parse_finite_number(row[column], column)
            if error:
                errors.append("{0}: row {1}: {2}".format(source, row_index, error))
                row_has_error = True
            else:
                parsed[column] = value

        timestamp = parsed.get("timestamp_s")
        duration = parsed.get("duration_s")
        throughput = parsed.get("throughput_kbps")

        if timestamp is not None:
            if timestamp < 0:
                errors.append("{0}: row {1}: timestamp_s must be greater than or equal to 0".format(source, row_index))
                row_has_error = True
            if previous_timestamp is not None and timestamp < previous_timestamp:
                errors.append("{0}: row {1}: timestamp_s must be monotonically non-decreasing".format(source, row_index))
                row_has_error = True
            previous_timestamp = timestamp

        if duration is not None:
            if duration <= 0:
                errors.append("{0}: row {1}: duration_s must be strictly greater than 0".format(source, row_index))
                row_has_error = True

        if throughput is not None:
            if throughput < 0:
                errors.append(
                    "{0}: row {1}: throughput_kbps must be greater than or equal to 0".format(source, row_index)
                )
                row_has_error = True

        if not row_has_error and duration is not None and throughput is not None:
            durations.append(duration)
            throughputs.append(throughput)

    return TraceValidationResult(
        is_valid=not errors,
        sample_count=len(rows),
        duration_s=sum(durations),
        min_throughput_kbps=min(throughputs) if throughputs else None,
        mean_throughput_kbps=(sum(throughputs) / len(throughputs)) if throughputs else None,
        max_throughput_kbps=max(throughputs) if throughputs else None,
        nominal_granularity_s=_nominal_granularity(durations),
        has_zero_throughput=any(value == 0 for value in throughputs),
        errors=tuple(errors),
        warnings=tuple(warnings),
    )


def _parse_finite_number(raw_value: object, column: str) -> Tuple[Optional[float], Optional[str]]:
    if raw_value is None:
        return None, "{0} is missing".format(column)
    if isinstance(raw_value, bool):
        return None, "{0} must be numeric and finite".format(column)
    if isinstance(raw_value, str) and raw_value.strip() == "":
        return None, "{0} is empty".format(column)

    try:
        value = float(raw_value)
    except (TypeError, ValueError):
        return None, "{0} must be numeric and finite".format(column)

    if not math.isfinite(value):
        return None, "{0} must be numeric and finite".format(column)

    return value, None


def _nominal_granularity(durations: Sequence[float]) -> Optional[float]:
    if not durations:
        return None

    first = durations[0]
    for value in durations[1:]:
        if not math.isclose(value, first, rel_tol=0.0, abs_tol=1e-12):
            return None
    return first

