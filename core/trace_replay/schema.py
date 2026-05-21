"""Schema constants for Phase 3 normalized trace validation."""

from __future__ import annotations

TRACE_SCHEMA_VERSION = "normalized_trace_schema_v1"

REQUIRED_TRACE_COLUMNS = (
    "timestamp_s",
    "duration_s",
    "throughput_kbps",
)

OPTIONAL_TRACE_COLUMNS = (
    "rtt_ms",
    "jitter_ms",
    "loss_rate",
    "source_timestamp",
    "latitude",
    "longitude",
    "mobility_label",
    "network_type",
    "operator_or_carrier",
    "scenario_label",
    "source_dataset",
    "source_file",
    "notes",
)

