"""Trace replay schema, loading, conversion and dry-run helpers.

Phase 3 exposes normalized trace validation, loading, and raw-dataset
conversion infrastructure plus deterministic network-model and dry-run
boundaries. It does not implement client-runtime trace integration, controller
changes, benchmark ranking, or final QoE scoring.
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
from core.trace_replay.fake_replay_adapter import TraceDrivenFakeReplayAdapter
from core.trace_replay.network_model import (
    END_POLICY_FAIL,
    END_POLICY_LOOP,
    SegmentDownloadResult,
    TraceDrivenNetworkModel,
    TraceReplayError,
)
from core.trace_replay.controller_adapter import (
    ControllerAdapterError,
    ControllerDecision,
    ExistingControllerAdapter,
)
from core.trace_replay.dry_run import (
    Representation,
    SegmentDryRunRecord,
    TraceDryRunConfig,
    TraceDryRunError,
    TraceDryRunResult,
    build_representations_from_kbps,
    estimate_segment_size_bytes,
    run_trace_dry_run,
    write_trace_dry_run_artifacts,
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
    "END_POLICY_FAIL",
    "END_POLICY_LOOP",
    "SegmentDownloadResult",
    "TraceDrivenFakeReplayAdapter",
    "TraceDrivenNetworkModel",
    "TraceReplayError",
    "ControllerAdapterError",
    "ControllerDecision",
    "ExistingControllerAdapter",
    "Representation",
    "SegmentDryRunRecord",
    "TraceDryRunConfig",
    "TraceDryRunError",
    "TraceDryRunResult",
    "build_representations_from_kbps",
    "estimate_segment_size_bytes",
    "run_trace_dry_run",
    "write_trace_dry_run_artifacts",
    "TraceValidationResult",
    "load_normalized_trace_csv",
    "load_normalized_trace_rows",
    "validate_normalized_trace_csv",
    "validate_normalized_trace_rows",
]
