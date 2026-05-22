"""Small fake replay adapter boundary for trace-driven downloads."""

from __future__ import annotations

import math

from core.trace_replay.network_model import SegmentDownloadResult, TraceDrivenNetworkModel, TraceReplayError


class TraceDrivenFakeReplayAdapter:
    """Own a replay clock around a TraceDrivenNetworkModel.

    This adapter is intentionally not connected to core.media_engine.fake,
    player code, or runtime execution in Phase 3.4B.
    """

    def __init__(self, network_model: TraceDrivenNetworkModel, initial_time_s: float = 0.0):
        self.network_model = network_model
        self.current_time_s = _validate_current_time_s(initial_time_s)

    def download_segment(self, segment_size_bytes: int) -> SegmentDownloadResult:
        result = self.network_model.download(
            segment_size_bytes=segment_size_bytes,
            start_time_s=self.current_time_s,
        )
        self.current_time_s = result.end_time_s
        return result

    def reset(self, current_time_s: float = 0.0) -> None:
        self.current_time_s = _validate_current_time_s(current_time_s)


def _validate_current_time_s(current_time_s: float) -> float:
    if isinstance(current_time_s, bool):
        raise TraceReplayError("current_time_s must be finite and non-negative")
    try:
        value = float(current_time_s)
    except (TypeError, ValueError) as exc:
        raise TraceReplayError("current_time_s must be finite and non-negative") from exc
    if not math.isfinite(value) or value < 0:
        raise TraceReplayError("current_time_s must be finite and non-negative")
    return value
