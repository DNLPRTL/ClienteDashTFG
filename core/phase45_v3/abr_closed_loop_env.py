from __future__ import annotations

import math
from dataclasses import dataclass, replace
from typing import Mapping, Sequence

from core.evaluation.qoe import DEFAULT_LINEAR_REBUFFER_WEIGHT, LINEAR_QOE_VERSION
from core.neural_abr.action_mask import assert_action_valid, build_action_mask
from core.neural_abr.constants import DEFAULT_CONTEXT_HISTORY_LENGTH, DEFAULT_REPRESENTATION_KBPS
from core.neural_abr.content_ladder import ContentLadder, default_training_ladder
from core.trace_replay.network_model import TraceDrivenNetworkModel


PHASE45_V3_DEFAULT_MAX_BUFFER_S = 60.0
PHASE45_V3_DEFAULT_SEGMENT_DURATION_S = 4.0


class AbrClosedLoopEnvError(ValueError):
    """Raised when the Phase 4-5 v3 closed-loop environment cannot step safely."""


@dataclass(frozen=True)
class AbrClosedLoopState:
    segment_index: int
    buffer_s: float
    last_representation_index: int
    throughput_history_bps: tuple[float, ...]
    download_time_history_s: tuple[float, ...]
    recent_rebuffer_s: float
    recent_switch_abs: float
    network_time_s: float
    total_segments: int


@dataclass(frozen=True)
class AbrClosedLoopStep:
    action: int
    segment_index: int
    bitrate_kbps: float
    segment_size_bytes: int
    download_time_s: float
    rebuffer_s: float
    buffer_s_before: float
    buffer_s_after: float
    measured_throughput_bps: float
    reward_n: float
    quality_mbps: float
    smoothness_mbps: float
    network_time_s_before: float
    network_time_s_after: float
    qoe_formula_version: str = LINEAR_QOE_VERSION


def default_phase45_v3_ladder(
    *,
    segment_duration_s: float = PHASE45_V3_DEFAULT_SEGMENT_DURATION_S,
    segment_count: int = 30,
    representation_kbps: Sequence[int] = DEFAULT_REPRESENTATION_KBPS,
    max_buffer_s: float = PHASE45_V3_DEFAULT_MAX_BUFFER_S,
) -> ContentLadder:
    return default_training_ladder(
        segment_duration_s=segment_duration_s,
        segment_count=segment_count,
        representation_kbps=representation_kbps,
        max_buffer_s=max_buffer_s,
    )


def initial_closed_loop_state(ladder: ContentLadder, initial_buffer_s: float = 0.0) -> AbrClosedLoopState:
    return AbrClosedLoopState(
        segment_index=0,
        buffer_s=max(0.0, float(initial_buffer_s)),
        last_representation_index=-1,
        throughput_history_bps=(),
        download_time_history_s=(),
        recent_rebuffer_s=0.0,
        recent_switch_abs=0.0,
        network_time_s=0.0,
        total_segments=int(ladder.segment_count),
    )


def simulate_closed_loop_step(
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    action: int,
    *,
    download_time_s: float,
    measured_throughput_bps: float | None = None,
    segment_size_bytes: int | None = None,
) -> tuple[AbrClosedLoopState, AbrClosedLoopStep]:
    if state.segment_index >= ladder.segment_count:
        raise AbrClosedLoopEnvError("closed-loop environment is already done")
    assert_action_valid(int(action), build_action_mask(ladder, state.segment_index))

    size_bytes = int(segment_size_bytes or ladder.segment_size_bytes(int(action), state.segment_index))
    if size_bytes <= 0:
        raise AbrClosedLoopEnvError("segment_size_bytes must be positive")
    download_time = _finite_positive(download_time_s, "download_time_s")
    measured_bps = (
        _finite_positive(measured_throughput_bps, "measured_throughput_bps")
        if measured_throughput_bps is not None
        else 8.0 * float(size_bytes) / download_time
    )

    rebuffer_s = max(download_time - float(state.buffer_s), 0.0)
    buffer_after = max(float(state.buffer_s) - download_time, 0.0) + float(ladder.segment_duration_s)
    buffer_after = min(buffer_after, float(ladder.max_buffer_s))
    recent_switch_abs = (
        abs(int(action) - int(state.last_representation_index))
        if int(state.last_representation_index) >= 0
        else 0.0
    )
    reward_n, quality_mbps, smoothness_mbps = linear_transition_reward(
        state=state,
        ladder=ladder,
        action=int(action),
        rebuffer_s=rebuffer_s,
    )
    next_state = replace(
        state,
        segment_index=int(state.segment_index) + 1,
        buffer_s=float(buffer_after),
        last_representation_index=int(action),
        throughput_history_bps=_append_history(state.throughput_history_bps, measured_bps),
        download_time_history_s=_append_history(state.download_time_history_s, download_time),
        recent_rebuffer_s=float(rebuffer_s),
        recent_switch_abs=float(recent_switch_abs),
        network_time_s=float(state.network_time_s) + download_time,
    )
    step = AbrClosedLoopStep(
        action=int(action),
        segment_index=int(state.segment_index),
        bitrate_kbps=float(ladder.bitrate_bps(int(action))) / 1000.0,
        segment_size_bytes=size_bytes,
        download_time_s=float(download_time),
        rebuffer_s=float(rebuffer_s),
        buffer_s_before=float(state.buffer_s),
        buffer_s_after=float(buffer_after),
        measured_throughput_bps=float(measured_bps),
        reward_n=float(reward_n),
        quality_mbps=float(quality_mbps),
        smoothness_mbps=float(smoothness_mbps),
        network_time_s_before=float(state.network_time_s),
        network_time_s_after=float(state.network_time_s) + download_time,
    )
    return next_state, step


def linear_transition_reward(
    *,
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    action: int,
    rebuffer_s: float,
) -> tuple[float, float, float]:
    bitrate_bps = float(ladder.bitrate_bps(int(action)))
    previous_bitrate_bps = (
        float(ladder.bitrate_bps(int(state.last_representation_index)))
        if int(state.last_representation_index) >= 0
        else 0.0
    )
    quality_mbps = bitrate_bps / 1_000_000.0
    smoothness_mbps = (
        abs(bitrate_bps - previous_bitrate_bps) / 1_000_000.0
        if previous_bitrate_bps > 0.0
        else 0.0
    )
    reward = quality_mbps - DEFAULT_LINEAR_REBUFFER_WEIGHT * float(rebuffer_s) - smoothness_mbps
    return float(reward), float(quality_mbps), float(smoothness_mbps)


def runtime_feedback_from_state(
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    *,
    last_step: AbrClosedLoopStep | None = None,
) -> Mapping[str, object]:
    rates_Bps = tuple(float(bitrate_bps) / 8.0 for bitrate_bps in ladder.bitrates_bps)
    current_level = (
        int(state.last_representation_index)
        if int(state.last_representation_index) >= 0
        else 0
    )
    current_level = max(0, min(current_level, len(rates_Bps) - 1))
    last_fragment_size = float(last_step.segment_size_bytes) if last_step is not None else 0.0
    last_download_time = float(last_step.download_time_s) if last_step is not None else 0.0
    return {
        "rates": list(rates_Bps),
        "rates_unit": "bytes_per_second",
        "queued_time": float(state.buffer_s),
        "cur_bitrate": float(rates_Bps[current_level]),
        "bwe": float(state.throughput_history_bps[-1]) / 8.0 if state.throughput_history_bps else 0.0,
        "level": int(current_level),
        "max_level": len(rates_Bps) - 1,
        "cur_rate": float(rates_Bps[current_level]),
        "max_rate": max(rates_Bps),
        "min_rate": min(rates_Bps),
        "max_bitrate": max(rates_Bps),
        "min_bitrate": min(rates_Bps),
        "last_fragment_size": last_fragment_size,
        "last_download_time": last_download_time,
        "fragment_duration": float(ladder.segment_duration_s),
        "segment_index": int(state.segment_index),
        "total_segments": int(state.total_segments),
    }


class AbrClosedLoopEnv:
    """Closed-loop ABR environment aligned with the Phase 6 client contract."""

    def __init__(
        self,
        *,
        ladder: ContentLadder | None = None,
        network_model: TraceDrivenNetworkModel | None = None,
        initial_buffer_s: float = 0.0,
    ) -> None:
        self.ladder = ladder or default_phase45_v3_ladder()
        self.network_model = network_model
        self._state = initial_closed_loop_state(self.ladder, initial_buffer_s=initial_buffer_s)

    @property
    def state(self) -> AbrClosedLoopState:
        return self._state

    @property
    def done(self) -> bool:
        return self._state.segment_index >= self.ladder.segment_count

    def action_mask(self) -> tuple[bool, ...]:
        return build_action_mask(self.ladder, self._state.segment_index)

    def step(self, action: int) -> AbrClosedLoopStep:
        if self.network_model is None:
            raise AbrClosedLoopEnvError("network_model is required for step(); use step_with_download_time in tests")
        size_bytes = self.ladder.segment_size_bytes(int(action), self._state.segment_index)
        download = self.network_model.download(segment_size_bytes=size_bytes, start_time_s=self._state.network_time_s)
        self._state, step = simulate_closed_loop_step(
            self._state,
            self.ladder,
            int(action),
            download_time_s=float(download.duration_s),
            measured_throughput_bps=float(download.measured_throughput_kbps) * 1000.0,
            segment_size_bytes=size_bytes,
        )
        return step

    def step_with_download_time(self, action: int, download_time_s: float) -> AbrClosedLoopStep:
        self._state, step = simulate_closed_loop_step(
            self._state,
            self.ladder,
            int(action),
            download_time_s=float(download_time_s),
        )
        return step


def _append_history(values: Sequence[float], value: float) -> tuple[float, ...]:
    combined = tuple(float(item) for item in values) + (float(value),)
    return combined[-DEFAULT_CONTEXT_HISTORY_LENGTH:]


def _finite_positive(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise AbrClosedLoopEnvError("{0} must be finite and positive".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise AbrClosedLoopEnvError("{0} must be finite and positive".format(name)) from exc
    if not math.isfinite(parsed) or parsed <= 0.0:
        raise AbrClosedLoopEnvError("{0} must be finite and positive".format(name))
    return parsed
