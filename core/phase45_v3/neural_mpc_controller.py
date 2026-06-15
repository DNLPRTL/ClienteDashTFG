from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Mapping, Sequence

import torch

from core.neural_abr.constants import CONTEXT_VECTOR_NAMES
from core.neural_abr.features import build_context_features, flatten_context_features
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopState, runtime_feedback_from_state
from core.phase45_v3.throughput_quantile_dataset import harmonic_mean_bps
from core.phase45_v3.throughput_quantile_model import ThroughputQuantilePredictor
from core.controller.robust_mpc import RobustMpcController


NEURAL_MPC_CONTROLLER_KEY = "phase45_v3_neural_throughput_calibrated_mpc_v1"
DEFAULT_NEURAL_MPC_HORIZON = 5
DEFAULT_NEURAL_MPC_QUANTILES = (0.10, 0.25, 0.50, 0.75)
DEFAULT_REBUFFER_WEIGHT = 4.3
DEFAULT_SWITCH_WEIGHT = 1.0
NEURAL_MPC_Q10_BUFFER_MAX_S = 4.0
NEURAL_MPC_Q25_BUFFER_MAX_S = 12.0
NEURAL_MPC_BLEND_BUFFER_MAX_S = 20.0


class Phase45V3NeuralMpcError(ValueError):
    """Raised when Neural Throughput-Calibrated MPC cannot make a safe decision."""


@dataclass(frozen=True)
class NeuralMpcDecision:
    action: int
    bitrate_bps: float
    chosen_quantile: str
    throughput_plan_bps: tuple[float, ...]
    best_sequence: tuple[int, ...]
    best_score: float
    estimated_total_rebuffer_s: float
    fallback_used: bool = False
    fallback_reason: str = "success_neural_mpc"
    raw_prediction_bps_by_horizon_quantile: tuple[tuple[float, ...], ...] = ()

    def to_json(self) -> dict[str, object]:
        return {
            "controller_key": NEURAL_MPC_CONTROLLER_KEY,
            "action": int(self.action),
            "bitrate_bps": float(self.bitrate_bps),
            "chosen_quantile": self.chosen_quantile,
            "throughput_plan_bps": [float(value) for value in self.throughput_plan_bps],
            "best_sequence": [int(value) for value in self.best_sequence],
            "best_score": float(self.best_score),
            "estimated_total_rebuffer_s": float(self.estimated_total_rebuffer_s),
            "fallback_used": bool(self.fallback_used),
            "fallback_reason": self.fallback_reason,
            "raw_prediction_bps_by_horizon_quantile": [
                [float(value) for value in row] for row in self.raw_prediction_bps_by_horizon_quantile
            ],
        }


class NeuralThroughputCalibratedMpcController:
    """Offline candidate controller: neural throughput quantiles plus explicit MPC."""

    def __init__(
        self,
        predictor: Callable[[AbrClosedLoopState, object], Sequence[Sequence[float]]],
        *,
        quantiles: Sequence[float] = DEFAULT_NEURAL_MPC_QUANTILES,
        horizon_segments: int = DEFAULT_NEURAL_MPC_HORIZON,
    ) -> None:
        self.predictor = predictor
        self.quantiles = tuple(float(value) for value in quantiles)
        self.horizon_segments = int(horizon_segments)
        self.last_decision: NeuralMpcDecision | None = None
        self._fallback = RobustMpcController(horizon=self.horizon_segments)

    def select_action(self, state: AbrClosedLoopState, ladder, action_mask: Sequence[bool] | None = None) -> NeuralMpcDecision:
        try:
            prediction = tuple(tuple(float(value) for value in row) for row in self.predictor(state, ladder))
            decision = plan_neural_mpc_action(
                state=state,
                ladder=ladder,
                predicted_bps_by_horizon_quantile=prediction,
                quantiles=self.quantiles,
                horizon_segments=self.horizon_segments,
                action_mask=action_mask,
            )
        except Exception as exc:  # noqa: BLE001 - fallback must be explicit and audited.
            decision = self._fallback_decision(state, ladder, str(type(exc).__name__))
        self.last_decision = decision
        return decision

    def _fallback_decision(self, state: AbrClosedLoopState, ladder, reason: str) -> NeuralMpcDecision:
        feedback = runtime_feedback_from_state(state, ladder)
        feedback = dict(feedback)
        feedback["throughput_history_bps"] = [float(value) for value in state.throughput_history_bps]
        self._fallback.setPlayerFeedback(feedback)
        target_rate_Bps = float(self._fallback.calcControlAction())
        action = self._fallback.quantizeRate(target_rate_Bps)
        return NeuralMpcDecision(
            action=int(action),
            bitrate_bps=float(ladder.bitrate_bps(int(action))),
            chosen_quantile="fallback_robust_mpc",
            throughput_plan_bps=(),
            best_sequence=(int(action),),
            best_score=0.0,
            estimated_total_rebuffer_s=0.0,
            fallback_used=True,
            fallback_reason=reason,
        )


class TorchThroughputQuantilePredictor:
    """Checkpoint-backed predictor used by offline evaluation scripts."""

    def __init__(self, checkpoint_path: object, *, device: str | None = None) -> None:
        path = Path(checkpoint_path).expanduser()
        checkpoint = torch.load(path, map_location="cpu", weights_only=False)
        model_config = checkpoint["model_config"]
        normalization = checkpoint["normalization"]
        self.quantiles = tuple(float(value) for value in model_config["quantiles"])
        self.horizon_segments = int(model_config["horizon_segments"])
        self.context_mean = tuple(float(value) for value in normalization["context_mean"])
        self.context_std = tuple(float(value) for value in normalization["context_std"])
        self.device = _resolve_device(device)
        self.model = ThroughputQuantilePredictor(
            input_dim=int(model_config["input_dim"]),
            horizon_segments=self.horizon_segments,
            quantiles=self.quantiles,
            hidden_sizes=tuple(int(value) for value in model_config["hidden_sizes"]),
        )
        self.model.load_state_dict(checkpoint["model_state_dict"])
        self.model.to(self.device)
        self.model.eval()
        self.checkpoint_path = str(path)
        self.model_sha256 = checkpoint.get("model_sha256")

    def __call__(self, state: AbrClosedLoopState, ladder) -> tuple[tuple[float, ...], ...]:
        context = flatten_context_features(build_context_features(state, ladder))
        normalized = _normalize_vector(context, self.context_mean, self.context_std)
        tensor = torch.tensor([normalized], dtype=torch.float32, device=self.device)
        with torch.no_grad():
            prediction_log_ratio = self.model(tensor).detach().cpu()[0]
        base_tp = harmonic_mean_bps(state.throughput_history_bps)
        rows = []
        for horizon_index in range(self.horizon_segments):
            row = []
            for quantile_index in range(len(self.quantiles)):
                log_ratio = float(prediction_log_ratio[horizon_index, quantile_index])
                predicted = float(base_tp) * math.exp(max(min(log_ratio, math.log(4.0)), math.log(0.15)))
                row.append(min(max(predicted, 0.15 * float(base_tp)), 4.0 * float(base_tp)))
            rows.append(_monotonicize_quantile_row(row))
        return tuple(rows)


def plan_neural_mpc_action(
    *,
    state: AbrClosedLoopState,
    ladder,
    predicted_bps_by_horizon_quantile: Sequence[Sequence[float]],
    quantiles: Sequence[float] = DEFAULT_NEURAL_MPC_QUANTILES,
    horizon_segments: int = DEFAULT_NEURAL_MPC_HORIZON,
    action_mask: Sequence[bool] | None = None,
) -> NeuralMpcDecision:
    prediction = _validate_prediction(predicted_bps_by_horizon_quantile, horizon_segments, len(tuple(quantiles)))
    throughput_plan, chosen_quantile = select_throughput_plan_for_buffer(
        prediction,
        quantiles=quantiles,
        buffer_s=float(state.buffer_s),
    )
    valid_actions = _valid_actions(action_mask, ladder.representation_count)
    if not valid_actions:
        raise Phase45V3NeuralMpcError("no valid actions for neural MPC")

    effective_horizon = min(int(horizon_segments), len(throughput_plan), max(ladder.segment_count - state.segment_index, 1))
    best_score = -math.inf
    best_sequence: tuple[int, ...] | None = None
    best_rebuffer = 0.0
    for sequence in itertools.product(valid_actions, repeat=effective_horizon):
        score, total_rebuffer = _score_sequence(
            sequence=sequence,
            state=state,
            ladder=ladder,
            throughput_plan_bps=throughput_plan[:effective_horizon],
        )
        if score > best_score:
            best_score = score
            best_sequence = tuple(int(value) for value in sequence)
            best_rebuffer = total_rebuffer

    if best_sequence is None:
        raise Phase45V3NeuralMpcError("MPC enumeration produced no sequence")
    action = int(best_sequence[0])
    return NeuralMpcDecision(
        action=action,
        bitrate_bps=float(ladder.bitrate_bps(action)),
        chosen_quantile=chosen_quantile,
        throughput_plan_bps=tuple(float(value) for value in throughput_plan[:effective_horizon]),
        best_sequence=best_sequence,
        best_score=float(best_score),
        estimated_total_rebuffer_s=float(best_rebuffer),
        raw_prediction_bps_by_horizon_quantile=prediction,
    )


def select_throughput_plan_for_buffer(
    predicted_bps_by_horizon_quantile: Sequence[Sequence[float]],
    *,
    quantiles: Sequence[float],
    buffer_s: float,
) -> tuple[tuple[float, ...], str]:
    prediction = tuple(tuple(float(value) for value in row) for row in predicted_bps_by_horizon_quantile)
    q10 = _nearest_quantile_index(quantiles, 0.10)
    q25 = _nearest_quantile_index(quantiles, 0.25)
    q50 = _nearest_quantile_index(quantiles, 0.50)
    if float(buffer_s) < NEURAL_MPC_Q10_BUFFER_MAX_S:
        return tuple(row[q10] for row in prediction), "q10"
    if float(buffer_s) < NEURAL_MPC_Q25_BUFFER_MAX_S:
        return tuple(row[q25] for row in prediction), "q25"
    if float(buffer_s) < NEURAL_MPC_BLEND_BUFFER_MAX_S:
        blend_width_s = NEURAL_MPC_BLEND_BUFFER_MAX_S - NEURAL_MPC_Q25_BUFFER_MAX_S
        alpha = min(max((NEURAL_MPC_BLEND_BUFFER_MAX_S - float(buffer_s)) / blend_width_s, 0.0), 1.0)
        return tuple(alpha * row[q25] + (1.0 - alpha) * row[q50] for row in prediction), "blend_q25_q50"
    return tuple(row[q50] for row in prediction), "q50"


def _score_sequence(
    *,
    sequence: Sequence[int],
    state: AbrClosedLoopState,
    ladder,
    throughput_plan_bps: Sequence[float],
) -> tuple[float, float]:
    buffer_s = float(state.buffer_s)
    previous_bitrate_bps = (
        float(ladder.bitrate_bps(int(state.last_representation_index)))
        if int(state.last_representation_index) >= 0
        else 0.0
    )
    score = 0.0
    total_rebuffer = 0.0
    for horizon_index, action in enumerate(sequence):
        bitrate_bps = float(ladder.bitrate_bps(int(action)))
        segment_size_bits = bitrate_bps * float(ladder.segment_duration_s)
        throughput_bps = max(float(throughput_plan_bps[horizon_index]), 1.0)
        download_time_s = segment_size_bits / throughput_bps
        rebuffer_s = max(download_time_s - buffer_s, 0.0)
        smoothness_mbps = abs(bitrate_bps - previous_bitrate_bps) / 1_000_000.0 if previous_bitrate_bps > 0.0 else 0.0
        reward = bitrate_bps / 1_000_000.0 - DEFAULT_REBUFFER_WEIGHT * rebuffer_s - DEFAULT_SWITCH_WEIGHT * smoothness_mbps
        score += reward
        total_rebuffer += rebuffer_s
        buffer_s = min(max(buffer_s - download_time_s, 0.0) + float(ladder.segment_duration_s), float(ladder.max_buffer_s))
        previous_bitrate_bps = bitrate_bps
    return float(score), float(total_rebuffer)


def _validate_prediction(
    prediction: Sequence[Sequence[float]],
    horizon_segments: int,
    quantile_count: int,
) -> tuple[tuple[float, ...], ...]:
    rows = tuple(tuple(float(value) for value in row) for row in prediction)
    if len(rows) < int(horizon_segments):
        raise Phase45V3NeuralMpcError("prediction has fewer horizons than requested")
    for row in rows[: int(horizon_segments)]:
        if len(row) != int(quantile_count):
            raise Phase45V3NeuralMpcError("prediction quantile dimension mismatch")
        if any(not math.isfinite(value) or value <= 0.0 for value in row):
            raise Phase45V3NeuralMpcError("prediction contains invalid throughput")
        for left, right in zip(row, row[1:]):
            if left > right:
                raise Phase45V3NeuralMpcError("prediction quantiles cross")
    return rows


def _valid_actions(action_mask: Sequence[bool] | None, representation_count: int) -> tuple[int, ...]:
    if action_mask is None:
        return tuple(range(int(representation_count)))
    return tuple(index for index, allowed in enumerate(action_mask[: int(representation_count)]) if bool(allowed))


def _nearest_quantile_index(quantiles: Sequence[float], target: float) -> int:
    values = tuple(float(value) for value in quantiles)
    if not values:
        raise Phase45V3NeuralMpcError("quantiles must not be empty")
    return min(range(len(values)), key=lambda index: abs(values[index] - float(target)))


def _monotonicize_quantile_row(row: Sequence[float]) -> tuple[float, ...]:
    return tuple(sorted(float(value) for value in row))


def _normalize_vector(values: Sequence[float], mean: Sequence[float], std: Sequence[float]) -> tuple[float, ...]:
    if len(values) != len(mean) or len(values) != len(std):
        raise Phase45V3NeuralMpcError("normalization dimension mismatch")
    return tuple((float(value) - float(mean[index])) / max(float(std[index]), 1.0e-9) for index, value in enumerate(values))


def _resolve_device(device: str | None) -> torch.device:
    if device and str(device).strip().lower() not in {"auto", "default"}:
        return torch.device(device)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")
