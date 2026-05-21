"""Loader for already-normalized Phase 3 trace CSV data.

This module is intentionally small: it loads normalized_trace_schema_v1 rows
and CSV files after validation. It is not a converter, replay runner, client
integration point, or QoE/reward implementation.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, Mapping, Optional, Sequence, Tuple

from core.trace_replay.schema import REQUIRED_TRACE_COLUMNS, TRACE_SCHEMA_VERSION
from core.trace_replay.validation import (
    TraceValidationResult,
    validate_normalized_trace_csv,
    validate_normalized_trace_rows,
)


class TraceLoadError(ValueError):
    """Raised when a normalized trace cannot be structurally loaded."""


@dataclass(frozen=True)
class TraceSample:
    timestamp_s: float
    duration_s: float
    throughput_kbps: float
    metadata: Mapping[str, str]


@dataclass(frozen=True)
class LoadedTrace:
    trace_id: str
    source: str
    schema_version: str
    samples: Tuple[TraceSample, ...]
    validation: TraceValidationResult

    @property
    def sample_count(self) -> int:
        return self.validation.sample_count

    @property
    def duration_s(self) -> float:
        return self.validation.duration_s

    @property
    def min_throughput_kbps(self) -> Optional[float]:
        return self.validation.min_throughput_kbps

    @property
    def mean_throughput_kbps(self) -> Optional[float]:
        return self.validation.mean_throughput_kbps

    @property
    def max_throughput_kbps(self) -> Optional[float]:
        return self.validation.max_throughput_kbps

    @property
    def nominal_granularity_s(self) -> Optional[float]:
        return self.validation.nominal_granularity_s

    @property
    def has_zero_throughput(self) -> bool:
        return self.validation.has_zero_throughput

    def iter_samples(self) -> Iterator[TraceSample]:
        return iter(self.samples)


def load_normalized_trace_rows(
    rows: Iterable[Mapping[str, object]],
    trace_id: str = "<memory>",
    source: str = "<memory>",
    strict: bool = True,
) -> LoadedTrace:
    materialized_rows = tuple(rows)
    validation = validate_normalized_trace_rows(materialized_rows, source=source)
    if strict and not validation.is_valid:
        raise _validation_error(source, validation)

    samples = _build_samples(materialized_rows, source=source)
    return LoadedTrace(
        trace_id=trace_id,
        source=source,
        schema_version=TRACE_SCHEMA_VERSION,
        samples=samples,
        validation=validation,
    )


def load_normalized_trace_csv(
    path: object,
    trace_id: Optional[str] = None,
    source: Optional[str] = None,
    strict: bool = True,
) -> LoadedTrace:
    csv_path = Path(path)
    resolved_trace_id = trace_id if trace_id is not None else csv_path.stem
    resolved_source = source if source is not None else str(csv_path)

    try:
        validation = validate_normalized_trace_csv(csv_path)
        rows, fieldnames = _read_csv_rows(csv_path)
    except FileNotFoundError as exc:
        raise TraceLoadError("{0}: normalized trace CSV not found".format(resolved_source)) from exc

    missing_columns = tuple(column for column in REQUIRED_TRACE_COLUMNS if column not in fieldnames)
    if missing_columns:
        raise TraceLoadError(
            "{0}: cannot load trace; missing required columns: {1}".format(
                resolved_source,
                ", ".join(missing_columns),
            )
        )

    if strict and not validation.is_valid:
        raise _validation_error(resolved_source, validation)

    samples = _build_samples(rows, source=resolved_source)
    return LoadedTrace(
        trace_id=resolved_trace_id,
        source=resolved_source,
        schema_version=TRACE_SCHEMA_VERSION,
        samples=samples,
        validation=validation,
    )


def _read_csv_rows(path: Path) -> Tuple[Tuple[Mapping[str, object], ...], Tuple[str, ...]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = tuple(reader.fieldnames or ())
        rows = tuple(reader)
    return rows, fieldnames


def _build_samples(rows: Sequence[Mapping[str, object]], source: str) -> Tuple[TraceSample, ...]:
    samples = []
    for row_index, row in enumerate(rows, start=1):
        missing_columns = tuple(column for column in REQUIRED_TRACE_COLUMNS if column not in row)
        if missing_columns:
            raise TraceLoadError(
                "{0}: row {1}: cannot load trace; missing required columns: {2}".format(
                    source,
                    row_index,
                    ", ".join(missing_columns),
                )
            )

        timestamp_s = _load_finite_float(row["timestamp_s"], source, row_index, "timestamp_s")
        duration_s = _load_finite_float(row["duration_s"], source, row_index, "duration_s")
        throughput_kbps = _load_finite_float(row["throughput_kbps"], source, row_index, "throughput_kbps")
        metadata = _metadata_from_row(row)
        samples.append(
            TraceSample(
                timestamp_s=timestamp_s,
                duration_s=duration_s,
                throughput_kbps=throughput_kbps,
                metadata=metadata,
            )
        )
    return tuple(samples)


def _load_finite_float(raw_value: object, source: str, row_index: int, column: str) -> float:
    if raw_value is None:
        raise TraceLoadError("{0}: row {1}: {2} is missing".format(source, row_index, column))
    if isinstance(raw_value, bool):
        raise TraceLoadError("{0}: row {1}: {2} must be numeric and finite".format(source, row_index, column))
    if isinstance(raw_value, str) and raw_value.strip() == "":
        raise TraceLoadError("{0}: row {1}: {2} is empty".format(source, row_index, column))

    try:
        value = float(raw_value)
    except (TypeError, ValueError) as exc:
        raise TraceLoadError(
            "{0}: row {1}: {2} must be numeric and finite".format(source, row_index, column)
        ) from exc

    if not math.isfinite(value):
        raise TraceLoadError("{0}: row {1}: {2} must be numeric and finite".format(source, row_index, column))
    return value


def _metadata_from_row(row: Mapping[str, object]) -> Dict[str, str]:
    metadata = {}
    for key, value in row.items():
        if key is None:
            continue
        key_text = str(key)
        if key_text in REQUIRED_TRACE_COLUMNS:
            continue
        metadata[key_text] = "" if value is None else str(value)
    return metadata


def _validation_error(source: str, validation: TraceValidationResult) -> TraceLoadError:
    message = "; ".join(validation.errors) if validation.errors else "unknown validation error"
    return TraceLoadError("{0}: invalid normalized trace: {1}".format(source, message))

