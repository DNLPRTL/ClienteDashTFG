"""Shared types for Phase 3 dataset converters."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from core.trace_replay.validation import TraceValidationResult


class ConversionError(Exception):
    """Raised when a trace dataset conversion cannot be completed safely."""


@dataclass(frozen=True)
class ConvertedTrace:
    trace_id: str
    dataset_id: str
    source_path: str
    output_csv_path: str
    manifest_path: str
    validation: TraceValidationResult
    sample_count: int
    duration_s: float
    min_throughput_kbps: Optional[float]
    mean_throughput_kbps: Optional[float]
    max_throughput_kbps: Optional[float]


@dataclass(frozen=True)
class ConversionBatchResult:
    dataset_id: str
    input_dir: str
    output_dir: str
    manifest_dir: str
    converted_traces: Tuple[ConvertedTrace, ...]
    skipped_inputs: Tuple[str, ...]
    errors: Tuple[str, ...]
