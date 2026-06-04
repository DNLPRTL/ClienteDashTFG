"""Phase 3 trace replay primitives.

This package owns trace schema validation, normalized trace loading, raw dataset
inventory, dataset conversion, and split manifest construction. It deliberately
does not expose dataset metadata to controllers.
"""

from core.trace_replay.loader import LoadedTrace, TraceSample, load_normalized_trace_csv
from core.trace_replay.schema import NORMALIZED_TRACE_SCHEMA_ID, REQUIRED_COLUMNS

__all__ = [
    "LoadedTrace",
    "NORMALIZED_TRACE_SCHEMA_ID",
    "REQUIRED_COLUMNS",
    "TraceSample",
    "load_normalized_trace_csv",
]
