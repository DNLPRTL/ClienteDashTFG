"""Deterministic offline replay environment for segment decisions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from core.neural_abr.action_mask import assert_action_valid, build_action_mask
from core.neural_abr.constants import K_CONTEXT
from core.neural_abr.content_ladder import ContentLadder
from core.trace_replay.loader import LoadedTrace
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel


@dataclass(frozen=True)
class ReplayState:
    segment_index: int
    buffer_s: float
    last_representation_index: int
    previous_representation_index: int
    throughput_history_bps: Tuple[float, ...]
    download_time_history_s: Tuple[float, ...]
    recent_rebuffer_s: float
    recent_switch_abs: float
    playback_time_s: float


@dataclass(frozen=True)
class ReplayStepResult:
    action: int
    segment_index: int
    segment_size_bytes: int
    download_time_s: float
    rebuffer_s: float
    buffer_s_before: float
    buffer_s_after: float
    measured_throughput_bps: float
    playback_time_s_before: float
    playback_time_s_after: float


class ReplayEnvironmentError(ValueError):
    """Raised when deterministic replay cannot proceed safely."""


class TraceReplayEnvironment:
    """Offline segment replay using the Phase 3 trace network model."""

    def __init__(
        self,
        loaded_trace: LoadedTrace,
        ladder: ContentLadder,
        initial_buffer_s: float = 0.0,
        end_policy: str = END_POLICY_LOOP,
        max_loops: int = 100,
    ):
        self.loaded_trace = loaded_trace
        self.ladder = ladder
        self.network_model = TraceDrivenNetworkModel(loaded_trace, end_policy=end_policy, max_loops=max_loops)
        self._state = ReplayState(
            segment_index=0,
            buffer_s=max(0.0, float(initial_buffer_s)),
            last_representation_index=-1,
            previous_representation_index=-1,
            throughput_history_bps=(),
            download_time_history_s=(),
            recent_rebuffer_s=0.0,
            recent_switch_abs=0.0,
            playback_time_s=0.0,
        )

    @property
    def state(self) -> ReplayState:
        return self._state

    @property
    def done(self) -> bool:
        return self._state.segment_index >= self.ladder.segment_count

    def action_mask(self) -> Tuple[bool, ...]:
        return build_action_mask(self.ladder, self._state.segment_index)

    def step(self, representation_index: int) -> ReplayStepResult:
        if self.done:
            raise ReplayEnvironmentError("replay environment is already done")

        action_mask = self.action_mask()
        assert_action_valid(representation_index, action_mask)

        state = self._state
        segment_size_bytes = self.ladder.segment_size_bytes(representation_index, state.segment_index)
        download = self.network_model.download(
            segment_size_bytes=segment_size_bytes,
            start_time_s=state.playback_time_s,
        )
        download_time_s = float(download.duration_s)
        rebuffer_s = max(download_time_s - state.buffer_s, 0.0)
        buffer_after = max(state.buffer_s - download_time_s, 0.0) + self.ladder.segment_duration_s
        buffer_after = min(buffer_after, self.ladder.max_buffer_s)
        measured_throughput_bps = float(download.measured_throughput_kbps) * 1000.0

        if state.last_representation_index >= 0:
            recent_switch_abs = abs(representation_index - state.last_representation_index)
        else:
            recent_switch_abs = 0.0

        throughput_history = _append_context_value(state.throughput_history_bps, measured_throughput_bps)
        download_history = _append_context_value(state.download_time_history_s, download_time_s)
        next_state = ReplayState(
            segment_index=state.segment_index + 1,
            buffer_s=buffer_after,
            last_representation_index=representation_index,
            previous_representation_index=state.last_representation_index,
            throughput_history_bps=throughput_history,
            download_time_history_s=download_history,
            recent_rebuffer_s=rebuffer_s,
            recent_switch_abs=float(recent_switch_abs),
            playback_time_s=float(download.end_time_s),
        )
        self._state = next_state

        return ReplayStepResult(
            action=representation_index,
            segment_index=state.segment_index,
            segment_size_bytes=segment_size_bytes,
            download_time_s=download_time_s,
            rebuffer_s=rebuffer_s,
            buffer_s_before=state.buffer_s,
            buffer_s_after=buffer_after,
            measured_throughput_bps=measured_throughput_bps,
            playback_time_s_before=state.playback_time_s,
            playback_time_s_after=float(download.end_time_s),
        )


def _append_context_value(values: Tuple[float, ...], value: float) -> Tuple[float, ...]:
    combined = tuple(values) + (float(value),)
    return combined[-K_CONTEXT:]
