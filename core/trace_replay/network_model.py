"""Deterministic trace-driven network model for Phase 3.4B.

This module turns an already-loaded normalized trace into simulated segment
download durations. It is not connected to the DashClientModular4 runtime, does
not call controllers, and does not expose complete traces as a controller API.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional, Tuple

from core.trace_replay.loader import LoadedTrace, TraceSample


END_POLICY_FAIL = "fail"
END_POLICY_LOOP = "loop"


class TraceReplayError(Exception):
    """Raised when a trace-driven download cannot be simulated safely."""


@dataclass(frozen=True)
class SegmentDownloadResult:
    trace_id: str
    requested_bytes: int
    delivered_bytes: int
    start_time_s: float
    end_time_s: float
    duration_s: float
    measured_throughput_kbps: float
    trace_time_start_s: float
    trace_time_end_s: float
    samples_touched: int
    end_policy: str


class TraceDrivenNetworkModel:
    """Simulate segment downloads against normalized trace samples."""

    def __init__(self, loaded_trace: LoadedTrace, end_policy: str = END_POLICY_FAIL, max_loops: int = 1):
        if end_policy not in (END_POLICY_FAIL, END_POLICY_LOOP):
            raise TraceReplayError("unsupported end_policy: {0}".format(end_policy))
        if isinstance(max_loops, bool) or not isinstance(max_loops, int) or max_loops < 0:
            raise TraceReplayError("max_loops must be a non-negative integer")

        self.loaded_trace = loaded_trace
        self.end_policy = end_policy
        self.max_loops = max_loops
        if not loaded_trace.validation.is_valid:
            raise TraceReplayError("loaded trace must be valid before replay")
        self._samples = tuple(loaded_trace.samples)
        if not self._samples:
            raise TraceReplayError("loaded trace has no samples")

        self._trace_start_s = 0.0
        self._trace_end_s = max(sample.timestamp_s + sample.duration_s for sample in self._samples)
        if not math.isfinite(self._trace_end_s) or self._trace_end_s <= self._trace_start_s:
            raise TraceReplayError("loaded trace has no positive time span")
        self._trace_span_s = self._trace_end_s - self._trace_start_s
        self._has_positive_throughput = any(sample.throughput_kbps > 0 for sample in self._samples)

    def download(self, segment_size_bytes: int, start_time_s: float = 0.0) -> SegmentDownloadResult:
        requested_bytes = _validate_segment_size_bytes(segment_size_bytes)
        wall_start_s = _validate_start_time_s(start_time_s)
        if not self._has_positive_throughput:
            raise TraceReplayError("trace cannot deliver positive downloads: all samples have zero throughput")

        wall_now_s = wall_start_s
        trace_now_s = self._trace_time_for_start(wall_start_s)
        trace_time_start_s = trace_now_s
        remaining_bytes = float(requested_bytes)
        samples_touched = 0
        loops_used = 0

        while True:
            next_window = self._next_sample_window(trace_now_s)
            if next_window is None:
                trace_now_s, wall_now_s, loops_used = self._handle_trace_end(
                    trace_now_s=trace_now_s,
                    wall_now_s=wall_now_s,
                    loops_used=loops_used,
                    requested_bytes=requested_bytes,
                )
                continue

            sample, usable_start_s, usable_end_s = next_window
            if trace_now_s < usable_start_s:
                gap_duration_s = usable_start_s - trace_now_s
                wall_now_s += gap_duration_s
                trace_now_s = usable_start_s

            usable_duration_s = usable_end_s - trace_now_s
            if usable_duration_s <= 0:
                trace_now_s = usable_end_s
                continue

            samples_touched += 1
            bytes_per_second = _throughput_kbps_to_bytes_per_second(sample.throughput_kbps)
            if bytes_per_second <= 0:
                wall_now_s += usable_duration_s
                trace_now_s = usable_end_s
                continue

            deliverable_bytes = bytes_per_second * usable_duration_s
            if deliverable_bytes >= remaining_bytes:
                time_needed_s = remaining_bytes / bytes_per_second
                end_time_s = wall_now_s + time_needed_s
                trace_time_end_s = trace_now_s + time_needed_s
                duration_s = end_time_s - wall_start_s
                return SegmentDownloadResult(
                    trace_id=self.loaded_trace.trace_id,
                    requested_bytes=requested_bytes,
                    delivered_bytes=requested_bytes,
                    start_time_s=wall_start_s,
                    end_time_s=end_time_s,
                    duration_s=duration_s,
                    measured_throughput_kbps=_measured_kbps(requested_bytes, duration_s),
                    trace_time_start_s=trace_time_start_s,
                    trace_time_end_s=trace_time_end_s,
                    samples_touched=samples_touched,
                    end_policy=self.end_policy,
                )

            remaining_bytes -= deliverable_bytes
            wall_now_s += usable_duration_s
            trace_now_s = usable_end_s

    def estimate_download_duration(self, segment_size_bytes: int, start_time_s: float = 0.0) -> SegmentDownloadResult:
        return self.download(segment_size_bytes=segment_size_bytes, start_time_s=start_time_s)

    def _trace_time_for_start(self, start_time_s: float) -> float:
        if self.end_policy == END_POLICY_LOOP:
            return self._trace_start_s + ((start_time_s - self._trace_start_s) % self._trace_span_s)
        return start_time_s

    def _next_sample_window(self, trace_time_s: float) -> Optional[Tuple[TraceSample, float, float]]:
        for sample in self._samples:
            sample_start_s = sample.timestamp_s
            sample_end_s = sample.timestamp_s + sample.duration_s
            if sample_end_s <= trace_time_s:
                continue
            if sample_start_s >= trace_time_s:
                return sample, sample_start_s, sample_end_s
            return sample, trace_time_s, sample_end_s
        return None

    def _handle_trace_end(
        self,
        trace_now_s: float,
        wall_now_s: float,
        loops_used: int,
        requested_bytes: int,
    ) -> Tuple[float, float, int]:
        if self.end_policy == END_POLICY_FAIL:
            raise TraceReplayError(
                "trace exhausted before delivering {0} bytes with end_policy=fail".format(requested_bytes)
            )
        if loops_used >= self.max_loops:
            raise TraceReplayError(
                "trace exhausted before delivering {0} bytes after {1} loop(s)".format(
                    requested_bytes,
                    loops_used,
                )
            )

        if trace_now_s < self._trace_end_s:
            wall_now_s += self._trace_end_s - trace_now_s
        return self._trace_start_s, wall_now_s, loops_used + 1


def _validate_segment_size_bytes(segment_size_bytes: int) -> int:
    if isinstance(segment_size_bytes, bool) or not isinstance(segment_size_bytes, int) or segment_size_bytes <= 0:
        raise TraceReplayError("segment_size_bytes must be a positive integer")
    return segment_size_bytes


def _validate_start_time_s(start_time_s: float) -> float:
    if isinstance(start_time_s, bool):
        raise TraceReplayError("start_time_s must be finite and non-negative")
    try:
        value = float(start_time_s)
    except (TypeError, ValueError) as exc:
        raise TraceReplayError("start_time_s must be finite and non-negative") from exc
    if not math.isfinite(value) or value < 0:
        raise TraceReplayError("start_time_s must be finite and non-negative")
    return value


def _throughput_kbps_to_bytes_per_second(throughput_kbps: float) -> float:
    return (throughput_kbps * 1000.0) / 8.0


def _measured_kbps(delivered_bytes: int, duration_s: float) -> float:
    if duration_s <= 0:
        raise TraceReplayError("download duration must be positive")
    return (delivered_bytes * 8.0) / (duration_s * 1000.0)
