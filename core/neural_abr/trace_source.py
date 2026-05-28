"""Trace loading helpers for Phase 4D.

The loader delegates normalized trace validation/loading to Phase 3 modules and
does not define a parallel raw trace schema.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence, Tuple

from core.neural_abr.constants import OOD_SPLIT, SPLITS, TRAIN_SPLIT, VALIDATION_SPLIT
from core.neural_abr.artifacts import read_json
from core.trace_replay.loader import LoadedTrace, load_normalized_trace_csv, load_normalized_trace_rows
from core.trace_replay.schema import TRACE_SCHEMA_VERSION


class TraceSourceError(ValueError):
    """Raised when trace source manifests violate Phase 4D rules."""


@dataclass(frozen=True)
class TraceRecord:
    trace: LoadedTrace
    split: str
    source_dataset: str
    diagnostic_only: bool = True


def load_trace_manifest(path: object) -> Tuple[TraceRecord, ...]:
    manifest_path = Path(path)
    payload = read_json(manifest_path)
    traces = payload.get("traces")
    if not isinstance(traces, Sequence) or isinstance(traces, (str, bytes)):
        raise TraceSourceError("trace manifest must contain a traces list")

    records = []
    seen_trace_ids = set()
    for entry in traces:
        if not isinstance(entry, Mapping):
            raise TraceSourceError("trace manifest entries must be mappings")
        split = str(entry.get("split", ""))
        if split not in SPLITS:
            raise TraceSourceError("invalid trace split: {0}".format(split))
        trace_id = str(entry.get("trace_id", "")).strip()
        if not trace_id:
            raise TraceSourceError("trace_id must be non-empty")
        if trace_id in seen_trace_ids:
            raise TraceSourceError("duplicate trace_id: {0}".format(trace_id))
        seen_trace_ids.add(trace_id)

        trace_path = Path(str(entry.get("path", "")))
        if not trace_path.is_absolute():
            trace_path = (manifest_path.parent / trace_path).resolve()
        trace = load_normalized_trace_csv(trace_path, trace_id=trace_id, strict=True)
        if trace.schema_version != TRACE_SCHEMA_VERSION:
            raise TraceSourceError("trace must use {0}".format(TRACE_SCHEMA_VERSION))
        source_dataset = str(entry.get("source_dataset", "external_normalized_trace")).strip()
        records.append(TraceRecord(trace=trace, split=split, source_dataset=source_dataset))
    return tuple(records)


def synthetic_smoke_trace_records() -> Tuple[TraceRecord, ...]:
    return (
        _synthetic_trace_record("synthetic_train_variable_a", TRAIN_SPLIT, (900, 1300, 2100, 2600, 1800, 3200)),
        _synthetic_trace_record("synthetic_train_variable_b", TRAIN_SPLIT, (1800, 2800, 4200, 2400, 1500, 3600)),
        _synthetic_trace_record("synthetic_validation_variable", VALIDATION_SPLIT, (1000, 1600, 2300, 1900, 2900, 1700)),
        _synthetic_trace_record("synthetic_ood_diagnostic_low_high", OOD_SPLIT, (450, 650, 5200, 4700, 800, 3800)),
    )


def group_by_split(records: Iterable[TraceRecord]) -> Mapping[str, Tuple[TraceRecord, ...]]:
    grouped = {split: [] for split in SPLITS}
    seen = set()
    for record in records:
        if record.split not in SPLITS:
            raise TraceSourceError("invalid split: {0}".format(record.split))
        if record.trace.trace_id in seen:
            raise TraceSourceError("trace_id appears in more than one split: {0}".format(record.trace.trace_id))
        seen.add(record.trace.trace_id)
        grouped[record.split].append(record)
    return {split: tuple(values) for split, values in grouped.items()}


def _synthetic_trace_record(trace_id: str, split: str, throughput_pattern_kbps: Sequence[int]) -> TraceRecord:
    rows = []
    timestamp_s = 0.0
    for sample_index in range(48):
        throughput_kbps = throughput_pattern_kbps[sample_index % len(throughput_pattern_kbps)]
        rows.append(
            {
                "timestamp_s": "{0:.3f}".format(timestamp_s),
                "duration_s": "1.000",
                "throughput_kbps": str(throughput_kbps),
                "source_dataset": "synthetic_smoke_diagnostic_only",
            }
        )
        timestamp_s += 1.0
    trace = load_normalized_trace_rows(rows, trace_id=trace_id, source="synthetic_smoke:{0}".format(trace_id))
    return TraceRecord(trace=trace, split=split, source_dataset="synthetic_smoke_diagnostic_only")
