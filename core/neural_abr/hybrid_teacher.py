from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence

from core.controller.bba import BbaController
from core.controller.bola import BolaController
from core.controller.contract import quantize_rate_to_level
from core.controller.mpc import MpcController
from core.controller.rate_based import RateBasedController
from core.controller.robust_mpc import RobustMpcController
from core.evaluation.qoe import SegmentQoEInput, compute_linear_qoe
from core.neural_abr.action_mask import assert_action_valid, lowest_valid_action, validate_action_mask
from core.neural_abr.constants import HYBRID_SOURCE_TEACHERS, HYBRID_TEACHER, REWARD_VERSION
from core.neural_abr.content_ladder import ContentLadder
from core.neural_abr.features import build_candidate_features, build_context_features
from core.neural_abr.replay_environment import ReplayState, TraceReplayEnvironment


@dataclass(frozen=True)
class ClassicTeacherDecision:
    representation_index: int
    teacher_policy: str
    reward_version: str
    reason: str


@dataclass(frozen=True)
class HybridTeacherSampleDraft:
    segment_index: int
    context_features: Mapping[str, object]
    candidate_features: tuple[Mapping[str, object], ...]
    action_mask: tuple[bool, ...]
    teacher_action: int
    source_teacher: str
    source_teacher_reason: str
    segment_reward_n: float


@dataclass(frozen=True)
class ClassicTeacherTrajectory:
    source_teacher: str
    qoe_mean: float
    qoe_sum: float
    total_rebuffer_s: float
    quality_switch_count: int
    segment_count: int
    samples: tuple[HybridTeacherSampleDraft, ...]


@dataclass(frozen=True)
class HybridTeacherWindowSelection:
    winner: ClassicTeacherTrajectory
    trajectories: tuple[ClassicTeacherTrajectory, ...]
    failed_teachers: tuple[Mapping[str, object], ...]
    tie_break_order: tuple[str, ...]


class HybridTeacherError(ValueError):
    """Raised when the hybrid teacher cannot select a valid offline expert."""


class ClassicControllerTeacher:
    """Adapter from Phase 2 controller classes to Phase 4 offline teacher labels."""

    def __init__(self, name: str) -> None:
        if name not in HYBRID_SOURCE_TEACHERS:
            raise HybridTeacherError("unsupported source teacher: {0}".format(name))
        self.name = name
        self.controller = _build_controller(name)

    def select_action(
        self,
        state: ReplayState,
        ladder: ContentLadder,
        action_mask: Sequence[bool],
    ) -> ClassicTeacherDecision:
        mask = validate_action_mask(action_mask, ladder.representation_count)
        feedback = _feedback_from_state(state, ladder)
        self.controller.setPlayerFeedback(feedback)
        target_rate = self.controller.calcControlAction()
        if target_rate is None:
            target_rate = self.controller.getControlAction()
        action = _action_from_target_rate(target_rate, feedback["rates"], mask)
        assert_action_valid(action, mask)
        reason = str(getattr(self.controller, "last_metrics", {}).get("reason", "controller_decision"))
        return ClassicTeacherDecision(
            representation_index=action,
            teacher_policy=self.name,
            reward_version=REWARD_VERSION,
            reason=reason,
        )


def select_hybrid_teacher_for_window(
    loaded_trace,
    ladder: ContentLadder,
    source_teacher_names: Sequence[str] = HYBRID_SOURCE_TEACHERS,
) -> HybridTeacherWindowSelection:
    trajectories = []
    failed_teachers = []
    for teacher_name in source_teacher_names:
        try:
            trajectories.append(_simulate_teacher_trajectory(loaded_trace, ladder, teacher_name))
        except Exception as exc:  # noqa: BLE001 - failures are audited and other teachers can still win.
            failed_teachers.append(
                {
                    "source_teacher": str(teacher_name),
                    "reason": type(exc).__name__,
                    "message": str(exc),
                }
            )
    if not trajectories:
        raise HybridTeacherError("all source teachers failed for selected window")
    tie_break_order = ("robust_mpc", "mpc", "bola", "bba", "rate_based")
    winner = max(trajectories, key=lambda item: _trajectory_sort_key(item, tie_break_order))
    return HybridTeacherWindowSelection(
        winner=winner,
        trajectories=tuple(trajectories),
        failed_teachers=tuple(failed_teachers),
        tie_break_order=tie_break_order,
    )


def build_hybrid_label_for_draft(
    draft: HybridTeacherSampleDraft,
    selection: HybridTeacherWindowSelection,
) -> Mapping[str, object]:
    return {
        "teacher_action": int(draft.teacher_action),
        "teacher_policy": HYBRID_TEACHER,
        "teacher_reward_n": float(draft.segment_reward_n),
        "reward_version": REWARD_VERSION,
        "diagnostic_only": True,
        "hybrid_source_teacher": draft.source_teacher,
        "teacher_selection_scope": "full_window_qoe_linear_v1",
        "teacher_window_qoe_mean": float(selection.winner.qoe_mean),
        "teacher_window_qoe_sum": float(selection.winner.qoe_sum),
        "reason": "window_winner:{0}; action_reason:{1}".format(draft.source_teacher, draft.source_teacher_reason),
    }


def qoe_linear_reward_for_replay_step(
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
    return float(quality_mbps - 4.3 * float(rebuffer_s) - smoothness_mbps)


def hybrid_selection_audit(selection: HybridTeacherWindowSelection) -> Mapping[str, object]:
    return {
        "winner": selection.winner.source_teacher,
        "winner_qoe_mean": selection.winner.qoe_mean,
        "tie_break_order": list(selection.tie_break_order),
        "failed_teachers": list(selection.failed_teachers),
        "source_teacher_results": [
            {
                "source_teacher": trajectory.source_teacher,
                "qoe_mean": trajectory.qoe_mean,
                "qoe_sum": trajectory.qoe_sum,
                "total_rebuffer_s": trajectory.total_rebuffer_s,
                "quality_switch_count": trajectory.quality_switch_count,
                "segment_count": trajectory.segment_count,
            }
            for trajectory in selection.trajectories
        ],
    }


def _simulate_teacher_trajectory(loaded_trace, ladder: ContentLadder, teacher_name: str) -> ClassicTeacherTrajectory:
    env = TraceReplayEnvironment(loaded_trace, ladder)
    teacher = ClassicControllerTeacher(teacher_name)
    drafts = []
    qoe_inputs = []
    while not env.done:
        state = env.state
        action_mask = env.action_mask()
        context = build_context_features(state, ladder)
        candidates = build_candidate_features(ladder, state.segment_index, float(context["last_bitrate_bps"]))
        decision = teacher.select_action(state, ladder, action_mask)
        step = env.step(decision.representation_index)
        bitrate_kbps = ladder.bitrate_bps(decision.representation_index) / 1000.0
        reward_n = qoe_linear_reward_for_replay_step(state, ladder, decision.representation_index, step.rebuffer_s)
        qoe_inputs.append(SegmentQoEInput(bitrate_kbps=bitrate_kbps, rebuffer_s=float(step.rebuffer_s)))
        drafts.append(
            HybridTeacherSampleDraft(
                segment_index=state.segment_index,
                context_features=dict(context),
                candidate_features=tuple(dict(candidate) for candidate in candidates),
                action_mask=tuple(bool(value) for value in action_mask),
                teacher_action=int(decision.representation_index),
                source_teacher=teacher_name,
                source_teacher_reason=decision.reason,
                segment_reward_n=reward_n,
            )
        )
    qoe = compute_linear_qoe(qoe_inputs)
    return ClassicTeacherTrajectory(
        source_teacher=teacher_name,
        qoe_mean=float(qoe.qoe_mean),
        qoe_sum=float(qoe.qoe_sum),
        total_rebuffer_s=float(qoe.total_rebuffer_s),
        quality_switch_count=int(qoe.quality_switch_count),
        segment_count=int(qoe.segment_count),
        samples=tuple(drafts),
    )


def _build_controller(name: str):
    if name == "rate_based":
        return RateBasedController()
    if name == "bba":
        return BbaController()
    if name == "bola":
        return BolaController()
    if name == "mpc":
        return MpcController(quality_reward_mode="log_rate_ratio")
    if name == "robust_mpc":
        return RobustMpcController(quality_reward_mode="log_rate_ratio")
    raise HybridTeacherError("unsupported source teacher: {0}".format(name))


def _feedback_from_state(state: ReplayState, ladder: ContentLadder) -> Mapping[str, object]:
    rates_Bps = [bitrate / 8.0 for bitrate in ladder.bitrates_bps]
    current_level = state.last_representation_index if state.last_representation_index >= 0 else 0
    current_level = max(0, min(current_level, len(rates_Bps) - 1))
    current_rate_Bps = rates_Bps[current_level]
    last_download_time_s = float(state.download_time_history_s[-1]) if state.download_time_history_s else 0.0
    last_throughput_bps = float(state.throughput_history_bps[-1]) if state.throughput_history_bps else 0.0
    last_throughput_Bps = last_throughput_bps / 8.0 if last_throughput_bps > 0.0 else 0.0
    last_fragment_size = last_throughput_Bps * last_download_time_s
    segment_sizes = [
        float(ladder.segment_size_bytes(index, state.segment_index))
        for index in range(ladder.representation_count)
    ]
    return {
        "queued_bytes": 0.0,
        "queued_time": float(state.buffer_s),
        "cur_bitrate": current_rate_Bps,
        "bwe": last_throughput_Bps,
        "level": current_level,
        "max_level": ladder.representation_count - 1,
        "cur_rate": current_rate_Bps,
        "max_rate": max(rates_Bps),
        "min_rate": min(rates_Bps),
        "max_bitrate": max(rates_Bps),
        "min_bitrate": min(rates_Bps),
        "last_fragment_size": last_fragment_size,
        "last_download_time": last_download_time_s,
        "downloaded_bytes": 0.0,
        "fragment_duration": float(ladder.segment_duration_s),
        "rates": rates_Bps,
        "rates_unit": "bytes_per_second",
        "segment_index": int(state.segment_index),
        "remaining_segments": max(ladder.segment_count - state.segment_index, 1),
        "start_segment_request": 0.0,
        "stop_segment_request": 0.0,
        "measured_throughput_Bps": last_throughput_Bps,
        "measured_throughput_bps": last_throughput_bps,
        "throughput_history_Bps": [float(value) / 8.0 for value in state.throughput_history_bps],
        "throughput_history_bps": [float(value) for value in state.throughput_history_bps],
        "segment_sizes_B": segment_sizes,
        "segment_sizes_unit": "bytes",
    }


def _action_from_target_rate(target_rate: object, rates_Bps: object, mask: Sequence[bool]) -> int:
    try:
        action = quantize_rate_to_level(target_rate, rates_Bps)  # type: ignore[arg-type]
    except ValueError:
        action = lowest_valid_action(mask)
    if action < 0 or action >= len(mask) or not mask[action]:
        return lowest_valid_action(mask)
    return int(action)


def _trajectory_sort_key(trajectory: ClassicTeacherTrajectory, tie_break_order: Sequence[str]) -> tuple[float, float, int, int]:
    try:
        tie_break_score = -int(tie_break_order.index(trajectory.source_teacher))
    except ValueError:
        tie_break_score = -len(tie_break_order)
    qoe = trajectory.qoe_mean if math.isfinite(trajectory.qoe_mean) else -math.inf
    return (qoe, -float(trajectory.total_rebuffer_s), -int(trajectory.quality_switch_count), tie_break_score)
