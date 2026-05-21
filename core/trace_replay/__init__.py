"""Trace replay schema helpers.

Phase 3.3A exposes validation helpers only. It does not implement replay,
dataset conversion, trace loading for client runs, or QoE scoring.
"""

from __future__ import annotations

from core.trace_replay.schema import (
    OPTIONAL_TRACE_COLUMNS,
    REQUIRED_TRACE_COLUMNS,
    TRACE_SCHEMA_VERSION,
)
from core.trace_replay.loader import (
    LoadedTrace,
    TraceLoadError,
    TraceSample,
    load_normalized_trace_csv,
    load_normalized_trace_rows,
)
from core.trace_replay.validation import (
    TraceValidationResult,
    validate_normalized_trace_csv,
    validate_normalized_trace_rows,
)

__all__ = [
    "OPTIONAL_TRACE_COLUMNS",
    "REQUIRED_TRACE_COLUMNS",
    "TRACE_SCHEMA_VERSION",
    "LoadedTrace",
    "TraceLoadError",
    "TraceSample",
    "TraceValidationResult",
    "load_normalized_trace_csv",
    "load_normalized_trace_rows",
    "validate_normalized_trace_csv",
    "validate_normalized_trace_rows",
]
