"""Trace replay schema, loading and conversion helpers.

Phase 3 exposes normalized trace validation, loading, and raw-dataset
conversion infrastructure. It does not implement replay, client-runtime trace
integration, controller changes, or QoE scoring.
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
from core.trace_replay.converters import (
    ConversionBatchResult,
    ConvertedTrace,
    ConversionError,
    convert_dataset,
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
    "ConversionBatchResult",
    "ConvertedTrace",
    "ConversionError",
    "convert_dataset",
    "TraceValidationResult",
    "load_normalized_trace_csv",
    "load_normalized_trace_rows",
    "validate_normalized_trace_csv",
    "validate_normalized_trace_rows",
]
