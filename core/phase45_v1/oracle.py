from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence

from core.evaluation.qoe import DEFAULT_LINEAR_REBUFFER_WEIGHT, LINEAR_QOE_VERSION
from core.neural_abr.action_mask import assert_action_valid, build_action_mask, lowest_valid_action
from core.neural_abr.constants import DEFAULT_CONTEXT_HISTORY_LENGTH
from core.neural_abr.content_ladder import ContentLadder
from core.neural_abr.replay_environment import ReplayState, ReplayStepResult
from core.phase45_v1.constants import ORACLE_POLICY_ID
from core.trace_replay.network_model import TraceDrivenNetworkModel, TraceReplayError


class Phase45OracleError(ValueError):
    """Raised when oracle_qoe_beam_v1 cannot produce a safe label."""


@dataclass(frozen=True)
class OracleConfig:
    horizon_segments: int
    beam_width: int

    def __post_init__(self) -> None:
        if isinstance(self.horizon_segments, bool) or not isinstance(self.horizon_segments, int) or self.horizon_segments <= 0:
            raise Phase45OracleError("horizon_segments must be a positive integer")
        if isinstance(self.beam_width, bool) or not isinstance(self.beam_width, int) or self.beam_width <= 0:
            raise Phase45OracleError("beam_width must be a positive integer")

    def to_json(self) -> dict[str, object]:
        return {"horizon_segments": self.horizon_segments, "beam_width": self.beam_width}


@dataclass(frozen=True)
class OracleDecision:
    action: int
    policy_id: str
    qoe_formula_version: str
    horizon_reward_n: float
    first_step_reward_n: float
    best_sequence: tuple[int, ...]
    horizon_segments_evaluated: int
    beam_width: int
    evaluated_sequence_count: int
    fallback_used: bool
    reason: str

    def to_json(self) -> dict[str, object]:
        return {
            "action": self.action,
            "policy_id": self.policy_id,
            "qoe_formula_version": self.qoe_formula_version,
            "horizon_reward_n": self.horizon_reward_n,
            "first_step_reward_n": self.first_step_reward_n,
            "best_sequence": list(self.best_sequence),
            "horizon_segments_evaluated": self.horizon_segments_evaluated,
            "beam_width": self.beam_width,
            "evaluated_sequence_count": self.evaluated_sequence_count,
            "fallback_used": self.fallback_used,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class _BeamNode:
    reward_sum: float
    total_rebuffer_s: float
    switch_count: int
    actions: tuple[int, ...]
    state: ReplayState
    first_step_reward_n: float


def select_oracle_action(
    state: ReplayState,
    ladder: ContentLadder,
    network_model: TraceDrivenNetworkModel,
    config: OracleConfig,
) -> OracleDecision:
    if state.segment_index >= ladder.segment_count:
        raise Phase45OracleError("cannot label a completed replay state")

    max_depth = min(config.horizon_segments, ladder.segment_count - state.segment_index)
    initial = _BeamNode(
        reward_sum=0.0,
        total_rebuffer_s=0.0,
        switch_count=0,
        actions=(),
        state=state,
        first_step_reward_n=0.0,
    )
    beams = (initial,)
    evaluated_sequence_count = 0
    for depth in range(max_depth):
        expanded: list[_BeamNode] = []
        for node in beams:
            mask = build_action_mask(ladder, node.state.segment_index)
            for action, allowed in enumerate(mask):
                if not allowed:
                    continue
                try:
                    next_state, step = simulate_step_from_state(node.state, ladder, network_model, action)
                except TraceReplayError:
                    continue
                reward_n = linear_reward_for_state(node.state, ladder, action, step.rebuffer_s)
                first_reward = reward_n if depth == 0 else node.first_step_reward_n
                expanded.append(
                    _BeamNode(
                        reward_sum=node.reward_sum + reward_n,
                        total_rebuffer_s=node.total_rebuffer_s + float(step.rebuffer_s),
                        switch_count=node.switch_count + (1 if next_state.recent_switch_abs > 0.0 else 0),
                        actions=node.actions + (int(action),),
                        state=next_state,
                        first_step_reward_n=first_reward,
                    )
                )
                evaluated_sequence_count += 1
        if not expanded:
            return _fallback_decision(state, ladder, config, evaluated_sequence_count)
        beams = tuple(sorted(expanded, key=_beam_sort_key, reverse=True)[: config.beam_width])

    best = sorted(beams, key=_beam_sort_key, reverse=True)[0]
    if not best.actions:
        return _fallback_decision(state, ladder, config, evaluated_sequence_count)
    return OracleDecision(
        action=int(best.actions[0]),
        policy_id=ORACLE_POLICY_ID,
        qoe_formula_version=LINEAR_QOE_VERSION,
        horizon_reward_n=round(float(best.reward_sum), 6),
        first_step_reward_n=round(float(best.first_step_reward_n), 6),
        best_sequence=best.actions,
        horizon_segments_evaluated=max_depth,
        beam_width=config.beam_width,
        evaluated_sequence_count=evaluated_sequence_count,
        fallback_used=False,
        reason="beam_search_qoe_linear_v1_conservative_tiebreak",
    )


def simulate_step_from_state(
    state: ReplayState,
    ladder: ContentLadder,
    network_model: TraceDrivenNetworkModel,
    representation_index: int,
) -> tuple[ReplayState, ReplayStepResult]:
    if state.segment_index >= ladder.segment_count:
        raise Phase45OracleError("cannot step a completed replay state")
    mask = build_action_mask(ladder, state.segment_index)
    assert_action_valid(representation_index, mask)
    segment_size_bytes = ladder.segment_size_bytes(representation_index, state.segment_index)
    download = network_model.download(segment_size_bytes=segment_size_bytes, start_time_s=state.playback_time_s)
    download_time_s = float(download.duration_s)
    rebuffer_s = max(download_time_s - state.buffer_s, 0.0)
    buffer_after = max(state.buffer_s - download_time_s, 0.0) + ladder.segment_duration_s
    buffer_after = min(buffer_after, ladder.max_buffer_s)
    measured_throughput_bps = float(download.measured_throughput_kbps) * 1000.0
    recent_switch_abs = (
        abs(int(representation_index) - state.last_representation_index)
        if state.last_representation_index >= 0
        else 0.0
    )
    next_state = ReplayState(
        segment_index=state.segment_index + 1,
        buffer_s=float(buffer_after),
        last_representation_index=int(representation_index),
        throughput_history_bps=_append_context_value(state.throughput_history_bps, measured_throughput_bps),
        download_time_history_s=_append_context_value(state.download_time_history_s, download_time_s),
        recent_rebuffer_s=float(rebuffer_s),
        recent_switch_abs=float(recent_switch_abs),
        playback_time_s=float(download.end_time_s),
    )
    step = ReplayStepResult(
        action=int(representation_index),
        segment_index=state.segment_index,
        segment_size_bytes=segment_size_bytes,
        download_time_s=float(download_time_s),
        rebuffer_s=float(rebuffer_s),
        buffer_s_before=float(state.buffer_s),
        buffer_s_after=float(buffer_after),
        measured_throughput_bps=float(measured_throughput_bps),
        playback_time_s_before=float(state.playback_time_s),
        playback_time_s_after=float(download.end_time_s),
    )
    return next_state, step


def linear_reward_for_state(
    state: ReplayState,
    ladder: ContentLadder,
    representation_index: int,
    rebuffer_s: float,
) -> float:
    bitrate_bps = float(ladder.bitrate_bps(int(representation_index)))
    previous_bitrate_bps = (
        float(ladder.bitrate_bps(state.last_representation_index))
        if state.last_representation_index >= 0
        else 0.0
    )
    quality_mbps = bitrate_bps / 1_000_000.0
    smoothness_mbps = (
        abs(bitrate_bps - previous_bitrate_bps) / 1_000_000.0
        if previous_bitrate_bps > 0.0
        else 0.0
    )
    return float(quality_mbps - DEFAULT_LINEAR_REBUFFER_WEIGHT * float(rebuffer_s) - smoothness_mbps)


def oracle_policy_card(config: OracleConfig) -> Mapping[str, object]:
    return {
        "policy_id": ORACLE_POLICY_ID,
        "qoe_formula_version": LINEAR_QOE_VERSION,
        "type": "offline_beam_search_oracle",
        "uses_future_information": True,
        "future_information_is_target_only": True,
        "runtime_controller": False,
        "config": config.to_json(),
        "tie_break": "higher reward, lower rebuffer, fewer switches, lower first action",
    }


def _beam_sort_key(node: _BeamNode) -> tuple[float, float, int, int]:
    first_action = node.actions[0] if node.actions else 0
    reward = node.reward_sum if math.isfinite(node.reward_sum) else -math.inf
    return (reward, -float(node.total_rebuffer_s), -int(node.switch_count), -int(first_action))


def _fallback_decision(
    state: ReplayState,
    ladder: ContentLadder,
    config: OracleConfig,
    evaluated_sequence_count: int,
) -> OracleDecision:
    action = lowest_valid_action(build_action_mask(ladder, state.segment_index))
    return OracleDecision(
        action=int(action),
        policy_id=ORACLE_POLICY_ID,
        qoe_formula_version=LINEAR_QOE_VERSION,
        horizon_reward_n=0.0,
        first_step_reward_n=0.0,
        best_sequence=(int(action),),
        horizon_segments_evaluated=0,
        beam_width=config.beam_width,
        evaluated_sequence_count=evaluated_sequence_count,
        fallback_used=True,
        reason="oracle_fallback_lowest_valid_action",
    )


def _append_context_value(values: Sequence[float], value: float) -> tuple[float, ...]:
    combined = tuple(float(item) for item in values) + (float(value),)
    return combined[-DEFAULT_CONTEXT_HISTORY_LENGTH:]
