from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping

from core.evaluation.qoe import LINEAR_QOE_VERSION
from core.neural_abr.action_mask import build_action_mask, lowest_valid_action
from core.neural_abr.content_ladder import ContentLadder
from core.phase45_v3.abr_closed_loop_env import (
    AbrClosedLoopState,
    AbrClosedLoopStep,
    simulate_closed_loop_step,
)
from core.trace_replay.network_model import TraceDrivenNetworkModel, TraceReplayError


PHASE45_V3_QH_ORACLE_ID = "phase45_v3_qh_oracle_v1"


class Phase45V3QhOracleError(ValueError):
    """Raised when the Phase 4-5 v3 Q_H oracle cannot produce labels."""


@dataclass(frozen=True)
class QhOracleConfig:
    horizon_segments: int = 5
    beam_width: int = 24

    def __post_init__(self) -> None:
        if isinstance(self.horizon_segments, bool) or not isinstance(self.horizon_segments, int) or self.horizon_segments <= 0:
            raise Phase45V3QhOracleError("horizon_segments must be a positive integer")
        if isinstance(self.beam_width, bool) or not isinstance(self.beam_width, int) or self.beam_width <= 0:
            raise Phase45V3QhOracleError("beam_width must be a positive integer")

    def to_json(self) -> dict[str, object]:
        return {"horizon_segments": self.horizon_segments, "beam_width": self.beam_width}


@dataclass(frozen=True)
class QhActionValue:
    action: int
    feasible: bool
    q_h_reward_n: float
    first_step_reward_n: float
    total_rebuffer_s: float
    switch_count: int
    best_sequence: tuple[int, ...]
    horizon_segments_evaluated: int
    evaluated_sequence_count: int
    reason: str

    def to_json(self) -> dict[str, object]:
        return {
            "action": self.action,
            "feasible": self.feasible,
            "q_h_reward_n": _finite_json_number(self.q_h_reward_n),
            "first_step_reward_n": _finite_json_number(self.first_step_reward_n),
            "total_rebuffer_s": _finite_json_number(self.total_rebuffer_s),
            "switch_count": self.switch_count,
            "best_sequence": list(self.best_sequence),
            "horizon_segments_evaluated": self.horizon_segments_evaluated,
            "evaluated_sequence_count": self.evaluated_sequence_count,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class QhOracleDecision:
    action: int
    policy_id: str
    qoe_formula_version: str
    action_values: tuple[QhActionValue, ...]
    fallback_used: bool
    reason: str

    def to_json(self) -> dict[str, object]:
        return {
            "action": self.action,
            "policy_id": self.policy_id,
            "qoe_formula_version": self.qoe_formula_version,
            "action_values": [row.to_json() for row in self.action_values],
            "fallback_used": self.fallback_used,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class _BeamNode:
    reward_sum: float
    total_rebuffer_s: float
    switch_count: int
    actions: tuple[int, ...]
    state: AbrClosedLoopState
    evaluated_sequence_count: int


def evaluate_qh_actions(
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    network_model: TraceDrivenNetworkModel,
    config: QhOracleConfig | None = None,
) -> QhOracleDecision:
    cfg = config or QhOracleConfig()
    if state.segment_index >= ladder.segment_count:
        raise Phase45V3QhOracleError("cannot label a completed closed-loop state")

    values = []
    mask = build_action_mask(ladder, state.segment_index)
    for action, allowed in enumerate(mask):
        if not allowed:
            values.append(_infeasible_action(action, "masked_by_ladder"))
            continue
        values.append(_evaluate_forced_first_action(state, ladder, network_model, cfg, int(action)))

    feasible = [row for row in values if row.feasible]
    if not feasible:
        fallback_action = lowest_valid_action(mask)
        return QhOracleDecision(
            action=int(fallback_action),
            policy_id=PHASE45_V3_QH_ORACLE_ID,
            qoe_formula_version=LINEAR_QOE_VERSION,
            action_values=tuple(values),
            fallback_used=True,
            reason="qh_oracle_fallback_lowest_valid_action_no_feasible_download",
        )

    best = sorted(feasible, key=_action_value_sort_key, reverse=True)[0]
    return QhOracleDecision(
        action=int(best.action),
        policy_id=PHASE45_V3_QH_ORACLE_ID,
        qoe_formula_version=LINEAR_QOE_VERSION,
        action_values=tuple(values),
        fallback_used=False,
        reason="qh_oracle_beam_search_all_actions_closed_loop_v1",
    )


def qh_oracle_card(config: QhOracleConfig) -> Mapping[str, object]:
    return {
        "policy_id": PHASE45_V3_QH_ORACLE_ID,
        "qoe_formula_version": LINEAR_QOE_VERSION,
        "type": "offline_closed_loop_q_h_oracle",
        "uses_future_information": True,
        "future_information_is_target_only": True,
        "runtime_controller": False,
        "config": config.to_json(),
        "tie_break": "higher Q_H, lower rebuffer, fewer switches, lower first action",
    }


def _evaluate_forced_first_action(
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    network_model: TraceDrivenNetworkModel,
    cfg: QhOracleConfig,
    action: int,
) -> QhActionValue:
    try:
        next_state, first_step = _step_with_network(state, ladder, network_model, action)
    except TraceReplayError as exc:
        return _infeasible_action(action, "trace_replay_error:{0}".format(exc))

    remaining_depth = min(
        int(cfg.horizon_segments) - 1,
        int(ladder.segment_count) - int(next_state.segment_index),
    )
    if remaining_depth <= 0:
        return QhActionValue(
            action=int(action),
            feasible=True,
            q_h_reward_n=round(float(first_step.reward_n), 6),
            first_step_reward_n=round(float(first_step.reward_n), 6),
            total_rebuffer_s=round(float(first_step.rebuffer_s), 6),
            switch_count=1 if next_state.recent_switch_abs > 0.0 else 0,
            best_sequence=(int(action),),
            horizon_segments_evaluated=1,
            evaluated_sequence_count=1,
            reason="qh_oracle_forced_action_terminal_horizon",
        )

    best_tail = _best_tail_beam(next_state, ladder, network_model, cfg, remaining_depth)
    reward = float(first_step.reward_n) + float(best_tail.reward_sum)
    return QhActionValue(
        action=int(action),
        feasible=True,
        q_h_reward_n=round(reward, 6),
        first_step_reward_n=round(float(first_step.reward_n), 6),
        total_rebuffer_s=round(float(first_step.rebuffer_s) + float(best_tail.total_rebuffer_s), 6),
        switch_count=int((1 if next_state.recent_switch_abs > 0.0 else 0) + best_tail.switch_count),
        best_sequence=(int(action),) + best_tail.actions,
        horizon_segments_evaluated=1 + len(best_tail.actions),
        evaluated_sequence_count=1 + int(best_tail.evaluated_sequence_count),
        reason="qh_oracle_forced_action_beam_search",
    )


def _best_tail_beam(
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    network_model: TraceDrivenNetworkModel,
    cfg: QhOracleConfig,
    depth: int,
) -> _BeamNode:
    beams = (
        _BeamNode(
            reward_sum=0.0,
            total_rebuffer_s=0.0,
            switch_count=0,
            actions=(),
            state=state,
            evaluated_sequence_count=0,
        ),
    )
    evaluated_sequence_count = 0
    for _ in range(depth):
        expanded: list[_BeamNode] = []
        for node in beams:
            mask = build_action_mask(ladder, node.state.segment_index)
            for action, allowed in enumerate(mask):
                if not allowed:
                    continue
                try:
                    next_state, step = _step_with_network(node.state, ladder, network_model, int(action))
                except TraceReplayError:
                    continue
                evaluated_sequence_count += 1
                expanded.append(
                    _BeamNode(
                        reward_sum=float(node.reward_sum) + float(step.reward_n),
                        total_rebuffer_s=float(node.total_rebuffer_s) + float(step.rebuffer_s),
                        switch_count=int(node.switch_count) + (1 if next_state.recent_switch_abs > 0.0 else 0),
                        actions=node.actions + (int(action),),
                        state=next_state,
                        evaluated_sequence_count=evaluated_sequence_count,
                    )
                )
        if not expanded:
            return _BeamNode(
                reward_sum=0.0,
                total_rebuffer_s=0.0,
                switch_count=0,
                actions=(),
                state=state,
                evaluated_sequence_count=evaluated_sequence_count,
            )
        beams = tuple(sorted(expanded, key=_beam_sort_key, reverse=True)[: int(cfg.beam_width)])

    best = sorted(beams, key=_beam_sort_key, reverse=True)[0]
    return _BeamNode(
        reward_sum=float(best.reward_sum),
        total_rebuffer_s=float(best.total_rebuffer_s),
        switch_count=int(best.switch_count),
        actions=best.actions,
        state=best.state,
        evaluated_sequence_count=evaluated_sequence_count,
    )


def _step_with_network(
    state: AbrClosedLoopState,
    ladder: ContentLadder,
    network_model: TraceDrivenNetworkModel,
    action: int,
) -> tuple[AbrClosedLoopState, AbrClosedLoopStep]:
    size_bytes = ladder.segment_size_bytes(int(action), state.segment_index)
    download = network_model.download(segment_size_bytes=size_bytes, start_time_s=state.network_time_s)
    return simulate_closed_loop_step(
        state,
        ladder,
        int(action),
        download_time_s=float(download.duration_s),
        measured_throughput_bps=float(download.measured_throughput_kbps) * 1000.0,
        segment_size_bytes=size_bytes,
    )


def _action_value_sort_key(row: QhActionValue) -> tuple[float, float, int, int]:
    reward = row.q_h_reward_n if math.isfinite(float(row.q_h_reward_n)) else -math.inf
    return (float(reward), -float(row.total_rebuffer_s), -int(row.switch_count), -int(row.action))


def _beam_sort_key(node: _BeamNode) -> tuple[float, float, int, tuple[int, ...]]:
    reward = node.reward_sum if math.isfinite(float(node.reward_sum)) else -math.inf
    conservative_tail = tuple(-int(action) for action in node.actions)
    return (float(reward), -float(node.total_rebuffer_s), -int(node.switch_count), conservative_tail)


def _infeasible_action(action: int, reason: str) -> QhActionValue:
    return QhActionValue(
        action=int(action),
        feasible=False,
        q_h_reward_n=-math.inf,
        first_step_reward_n=-math.inf,
        total_rebuffer_s=math.inf,
        switch_count=0,
        best_sequence=(),
        horizon_segments_evaluated=0,
        evaluated_sequence_count=0,
        reason=reason,
    )


def _finite_json_number(value: object) -> float | None:
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None
