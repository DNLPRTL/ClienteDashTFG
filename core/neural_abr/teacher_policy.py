"""Offline teacher policies for NeuralABR-Lite behavior cloning labels."""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Sequence, Tuple

from core.neural_abr.action_mask import assert_action_valid, lowest_valid_action, validate_action_mask
from core.neural_abr.constants import (
    BOUNDED_ORACLE_TEACHER,
    DEFAULT_SEGMENT_DURATION_S,
    PRIMARY_TEACHER,
    REWARD_VERSION,
    SECONDARY_TEACHER,
)
from core.neural_abr.content_ladder import ContentLadder
from core.neural_abr.replay_env import ReplayState


@dataclass(frozen=True)
class TeacherDecision:
    representation_index: int
    teacher_policy: str
    reward_version: str
    reward_n: float
    reason: str


class TeacherPolicyError(ValueError):
    """Raised when an offline teacher cannot produce a valid label."""


@dataclass(frozen=True)
class MpcTeacherConfig:
    policy_name: str = PRIMARY_TEACHER
    horizon: int = 3
    rebuffer_penalty: float = 4.3
    switch_penalty: float = 1.0
    startup_action: int = 0
    robust_safety_factor: float = 0.85
    max_enumerated_sequences: int = 4096


class MpcTeacherPolicy:
    """Small enumerative MPC/RobustMPC labeler for offline samples."""

    def __init__(self, config: MpcTeacherConfig | None = None):
        self.config = config or MpcTeacherConfig()
        if self.config.policy_name not in (PRIMARY_TEACHER, SECONDARY_TEACHER):
            raise TeacherPolicyError("unsupported non-oracle teacher: {0}".format(self.config.policy_name))

    @property
    def name(self) -> str:
        return self.config.policy_name

    def select_action(
        self,
        state: ReplayState,
        ladder: ContentLadder,
        action_mask: Sequence[bool],
    ) -> TeacherDecision:
        mask = validate_action_mask(action_mask, ladder.representation_count)
        valid_actions = tuple(index for index, valid in enumerate(mask) if valid)
        if len(valid_actions) == 1:
            action = valid_actions[0]
            return TeacherDecision(action, self.name, REWARD_VERSION, 0.0, "single_valid_action")

        predicted_throughput_bps = _predict_throughput_bps(state.throughput_history_bps)
        if predicted_throughput_bps is None:
            action = min(max(self.config.startup_action, 0), ladder.representation_count - 1)
            if not mask[action]:
                action = lowest_valid_action(mask)
            return TeacherDecision(action, self.name, REWARD_VERSION, 0.0, "startup_no_history_fallback")

        if self.name == PRIMARY_TEACHER:
            predicted_throughput_bps = max(1.0, predicted_throughput_bps * self.config.robust_safety_factor)

        horizon = _effective_horizon(self.config.horizon, ladder, state)
        best_score = -math.inf
        best_sequence: Tuple[int, ...] | None = None
        sequence_count = 0
        for sequence in itertools.product(valid_actions, repeat=horizon):
            sequence_count += 1
            if sequence_count > self.config.max_enumerated_sequences:
                break
            score = _score_sequence(
                sequence=sequence,
                state=state,
                ladder=ladder,
                predicted_throughput_bps=predicted_throughput_bps,
                rebuffer_penalty=self.config.rebuffer_penalty,
                switch_penalty=self.config.switch_penalty,
            )
            if score > best_score:
                best_score = score
                best_sequence = tuple(sequence)

        if best_sequence is None:
            action = lowest_valid_action(mask)
            return TeacherDecision(action, self.name, REWARD_VERSION, 0.0, "no_sequence_fallback")

        action = int(best_sequence[0])
        assert_action_valid(action, mask)
        reward_n = best_score / float(max(len(best_sequence), 1))
        return TeacherDecision(action, self.name, REWARD_VERSION, float(reward_n), "enumerative_qoe_linear_v1")


def robust_mpc_teacher() -> MpcTeacherPolicy:
    return MpcTeacherPolicy(MpcTeacherConfig(policy_name=PRIMARY_TEACHER))


def mpc_teacher() -> MpcTeacherPolicy:
    return MpcTeacherPolicy(MpcTeacherConfig(policy_name=SECONDARY_TEACHER, robust_safety_factor=1.0))


def bounded_oracle_is_diagnostic_only() -> str:
    return BOUNDED_ORACLE_TEACHER


def _predict_throughput_bps(history_bps: Sequence[float]) -> float | None:
    positives = [float(value) for value in history_bps if float(value) > 0.0]
    if not positives:
        return None
    denominator = sum(1.0 / value for value in positives)
    if denominator <= 0.0:
        return None
    prediction = len(positives) / denominator
    if not math.isfinite(prediction) or prediction <= 0.0:
        return None
    return prediction


def _effective_horizon(configured_horizon: int, ladder: ContentLadder, state: ReplayState) -> int:
    remaining = max(ladder.segment_count - state.segment_index, 1)
    horizon = max(1, int(configured_horizon))
    return min(horizon, remaining)


def _score_sequence(
    sequence: Sequence[int],
    state: ReplayState,
    ladder: ContentLadder,
    predicted_throughput_bps: float,
    rebuffer_penalty: float,
    switch_penalty: float,
) -> float:
    buffer_s = float(state.buffer_s)
    previous_bitrate_bps = (
        float(ladder.bitrate_bps(state.last_representation_index))
        if state.last_representation_index >= 0
        else 0.0
    )
    score = 0.0
    for offset, representation_index in enumerate(sequence):
        segment_index = min(state.segment_index + offset, ladder.segment_count - 1)
        if offset == 0:
            size_bytes = ladder.segment_size_bytes(representation_index, segment_index)
        else:
            size_bytes = max(
                1,
                int(round(ladder.bitrate_bps(representation_index) * DEFAULT_SEGMENT_DURATION_S / 8.0)),
            )
        download_time_s = float(size_bytes) * 8.0 / predicted_throughput_bps
        rebuffer_s = max(download_time_s - buffer_s, 0.0)
        buffer_s = max(buffer_s - download_time_s, 0.0) + ladder.segment_duration_s
        buffer_s = min(buffer_s, ladder.max_buffer_s)

        bitrate_bps = float(ladder.bitrate_bps(representation_index))
        quality_mbps = bitrate_bps / 1_000_000.0
        if previous_bitrate_bps > 0.0:
            switch_mbps = abs(bitrate_bps - previous_bitrate_bps) / 1_000_000.0
        else:
            switch_mbps = 0.0
        score += quality_mbps
        score -= float(rebuffer_penalty) * rebuffer_s
        score -= float(switch_penalty) * switch_mbps
        previous_bitrate_bps = bitrate_bps
    return float(score)
