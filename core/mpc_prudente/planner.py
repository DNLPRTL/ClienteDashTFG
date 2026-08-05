"""Planner MPC prudente: evalúa cada secuencia de acciones bajo todos los
cuantiles de throughput predichos y agrega con CVaR_alpha (media de los peores
escenarios), usando los tamaños reales (VBR) de los segmentos.

El nivel de riesgo `alpha` es configurable: existe una regla adaptativa por buffer
(`buffer_risk_alpha`, usada en los diagnósticos offline), pero en la evaluación
final de Phase 6 se fijó `alpha=0.75` (media de los 3 peores escenarios de 4).
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Callable, Sequence

from core.controller.robust_mpc import RobustMpcController
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopState, runtime_feedback_from_state

MPC_PRUDENTE_CONTROLLER_KEY = "mpc_prudente_v1"
DEFAULT_QUANTILES = (0.10, 0.25, 0.50, 0.75)
DEFAULT_HORIZON = 5
DEFAULT_REBUFFER_WEIGHT = 4.3
DEFAULT_SWITCH_WEIGHT = 1.0

# Niveles de riesgo CVaR por buffer (fracción de peores escenarios a promediar).
RISK_ALPHA_LOW_BUFFER = 0.25
RISK_ALPHA_MID_BUFFER = 0.50
RISK_ALPHA_HIGH_BUFFER = 0.75
RISK_ALPHA_SAFE_BUFFER = 1.00
RISK_BUFFER_LOW_S = 4.0
RISK_BUFFER_MID_S = 12.0
RISK_BUFFER_HIGH_S = 20.0


class MpcPrudentePlannerError(ValueError):
    """Raised when the prudent planner cannot make a safe decision."""


@dataclass(frozen=True)
class PrudentDecision:
    action: int
    bitrate_bps: float
    risk_alpha: float
    cvar_score: float
    best_sequence: tuple[int, ...]
    per_quantile_rebuffer_s: tuple[float, ...]
    fallback_used: bool = False
    fallback_reason: str = "success_mpc_prudente"

    def to_json(self) -> dict[str, object]:
        return {
            "controller_key": MPC_PRUDENTE_CONTROLLER_KEY,
            "action": int(self.action),
            "bitrate_bps": float(self.bitrate_bps),
            "risk_alpha": float(self.risk_alpha),
            "cvar_score": float(self.cvar_score),
            "best_sequence": [int(value) for value in self.best_sequence],
            "per_quantile_rebuffer_s": [float(value) for value in self.per_quantile_rebuffer_s],
            "fallback_used": bool(self.fallback_used),
            "fallback_reason": self.fallback_reason,
        }


def buffer_risk_alpha(buffer_s: float) -> float:
    """Nivel CVaR según el buffer: menos buffer → más pesimista (alpha menor)."""
    buffer = float(buffer_s)
    if buffer < RISK_BUFFER_LOW_S:
        return RISK_ALPHA_LOW_BUFFER
    if buffer < RISK_BUFFER_MID_S:
        return RISK_ALPHA_MID_BUFFER
    if buffer < RISK_BUFFER_HIGH_S:
        return RISK_ALPHA_HIGH_BUFFER
    return RISK_ALPHA_SAFE_BUFFER


def plan_prudent_action(
    *,
    state: AbrClosedLoopState,
    ladder,
    predicted_bps_by_horizon_quantile: Sequence[Sequence[float]],
    quantiles: Sequence[float] = DEFAULT_QUANTILES,
    horizon_segments: int = DEFAULT_HORIZON,
    action_mask: Sequence[bool] | None = None,
    risk_alpha: float | None = None,
    rebuffer_weight: float = DEFAULT_REBUFFER_WEIGHT,
    switch_weight: float = DEFAULT_SWITCH_WEIGHT,
) -> PrudentDecision:
    prediction = _validated_prediction(predicted_bps_by_horizon_quantile, horizon_segments, len(tuple(quantiles)))
    alpha = float(risk_alpha) if risk_alpha is not None else buffer_risk_alpha(state.buffer_s)
    valid_actions = _valid_actions(action_mask, ladder.representation_count)
    if not valid_actions:
        raise MpcPrudentePlannerError("no valid actions for prudent MPC")

    remaining = max(int(ladder.segment_count) - int(state.segment_index), 1)
    effective_horizon = min(int(horizon_segments), len(prediction), remaining)

    best_score = -math.inf
    best_sequence: tuple[int, ...] | None = None
    best_rebuffer: tuple[float, ...] = ()
    for sequence in itertools.product(valid_actions, repeat=effective_horizon):
        cvar, per_quantile_rebuffer = _score_sequence_cvar(
            sequence=sequence,
            state=state,
            ladder=ladder,
            prediction=prediction[:effective_horizon],
            alpha=alpha,
            rebuffer_weight=rebuffer_weight,
            switch_weight=switch_weight,
        )
        if cvar > best_score:
            best_score = cvar
            best_sequence = tuple(int(value) for value in sequence)
            best_rebuffer = per_quantile_rebuffer

    if best_sequence is None:
        raise MpcPrudentePlannerError("prudent MPC enumeration produced no sequence")
    action = int(best_sequence[0])
    return PrudentDecision(
        action=action,
        bitrate_bps=float(ladder.bitrate_bps(action)),
        risk_alpha=float(alpha),
        cvar_score=float(best_score),
        best_sequence=best_sequence,
        per_quantile_rebuffer_s=tuple(float(value) for value in best_rebuffer),
    )


def _score_sequence_cvar(
    *,
    sequence: Sequence[int],
    state: AbrClosedLoopState,
    ladder,
    prediction: Sequence[Sequence[float]],
    alpha: float,
    rebuffer_weight: float,
    switch_weight: float,
) -> tuple[float, tuple[float, ...]]:
    quantile_count = len(prediction[0])
    per_quantile_score = [0.0] * quantile_count
    per_quantile_rebuffer = [0.0] * quantile_count
    segment_duration_s = float(ladder.segment_duration_s)
    max_buffer_s = float(ladder.max_buffer_s)
    for k in range(quantile_count):
        buffer_s = float(state.buffer_s)
        previous_bitrate_bps = (
            float(ladder.bitrate_bps(int(state.last_representation_index)))
            if int(state.last_representation_index) >= 0
            else 0.0
        )
        for horizon_index, action in enumerate(sequence):
            bitrate_bps = float(ladder.bitrate_bps(int(action)))
            segment_index = int(state.segment_index) + int(horizon_index)
            # Peso REAL (VBR) del segmento, no CBR.
            segment_size_bits = 8.0 * float(ladder.segment_size_bytes(int(action), segment_index))
            throughput_bps = max(float(prediction[horizon_index][k]), 1.0)
            download_time_s = segment_size_bits / throughput_bps
            rebuffer_s = max(download_time_s - buffer_s, 0.0)
            smoothness_mbps = (
                abs(bitrate_bps - previous_bitrate_bps) / 1_000_000.0 if previous_bitrate_bps > 0.0 else 0.0
            )
            reward = bitrate_bps / 1_000_000.0 - float(rebuffer_weight) * rebuffer_s - float(switch_weight) * smoothness_mbps
            per_quantile_score[k] += reward
            per_quantile_rebuffer[k] += rebuffer_s
            buffer_s = min(max(buffer_s - download_time_s, 0.0) + segment_duration_s, max_buffer_s)
            previous_bitrate_bps = bitrate_bps
    return _cvar(per_quantile_score, alpha), tuple(per_quantile_rebuffer)


def _cvar(scores: Sequence[float], alpha: float) -> float:
    """CVaR_alpha: media de los peores ceil(alpha*K) escenarios (peor = menor QoE)."""
    ordered = sorted(float(value) for value in scores)  # ascendente: peores primero
    count = len(ordered)
    if count == 0:
        return 0.0
    worst_m = max(1, int(math.ceil(max(min(float(alpha), 1.0), 0.0) * count)))
    return sum(ordered[:worst_m]) / float(worst_m)


def _validated_prediction(
    prediction: Sequence[Sequence[float]], horizon_segments: int, quantile_count: int
) -> tuple[tuple[float, ...], ...]:
    rows = []
    for row in prediction:
        values = tuple(float(value) for value in row)
        if len(values) != int(quantile_count):
            raise MpcPrudentePlannerError("prediction quantile dimension mismatch")
        if any(not math.isfinite(value) or value <= 0.0 for value in values):
            raise MpcPrudentePlannerError("prediction contains invalid throughput")
        # Forzar monotonía (q ascendente) por robustez ante crossing residual.
        rows.append(tuple(sorted(values)))
    if len(rows) < int(horizon_segments):
        raise MpcPrudentePlannerError("prediction has fewer horizons than requested")
    return tuple(rows)


def _valid_actions(action_mask: Sequence[bool] | None, representation_count: int) -> tuple[int, ...]:
    if action_mask is None:
        return tuple(range(int(representation_count)))
    return tuple(index for index, allowed in enumerate(action_mask[: int(representation_count)]) if bool(allowed))


class PrudentMpcController:
    """Controller candidato: cuantiles neuronales + planner MPC prudente (CVaR)."""

    def __init__(
        self,
        predictor: Callable[[AbrClosedLoopState, object], Sequence[Sequence[float]]],
        *,
        quantiles: Sequence[float] = DEFAULT_QUANTILES,
        horizon_segments: int = DEFAULT_HORIZON,
        risk_alpha_fn: Callable[[float], float] = buffer_risk_alpha,
    ) -> None:
        self.predictor = predictor
        self.quantiles = tuple(float(value) for value in quantiles)
        self.horizon_segments = int(horizon_segments)
        self.risk_alpha_fn = risk_alpha_fn
        self.last_decision: PrudentDecision | None = None
        self._fallback = RobustMpcController(horizon=self.horizon_segments)

    def select_action(
        self, state: AbrClosedLoopState, ladder, action_mask: Sequence[bool] | None = None
    ) -> PrudentDecision:
        try:
            prediction = tuple(tuple(float(value) for value in row) for row in self.predictor(state, ladder))
            decision = plan_prudent_action(
                state=state,
                ladder=ladder,
                predicted_bps_by_horizon_quantile=prediction,
                quantiles=self.quantiles,
                horizon_segments=self.horizon_segments,
                action_mask=action_mask,
                risk_alpha=self.risk_alpha_fn(float(state.buffer_s)),
            )
        except Exception as exc:  # noqa: BLE001 - fallback explícito y auditado.
            decision = self._fallback_decision(state, ladder, str(type(exc).__name__))
        self.last_decision = decision
        return decision

    def _fallback_decision(self, state: AbrClosedLoopState, ladder, reason: str) -> PrudentDecision:
        feedback = dict(runtime_feedback_from_state(state, ladder))
        feedback["throughput_history_bps"] = [float(value) for value in state.throughput_history_bps]
        self._fallback.setPlayerFeedback(feedback)
        target_rate_Bps = float(self._fallback.calcControlAction())
        action = int(self._fallback.quantizeRate(target_rate_Bps))
        return PrudentDecision(
            action=action,
            bitrate_bps=float(ladder.bitrate_bps(action)),
            risk_alpha=0.0,
            cvar_score=0.0,
            best_sequence=(action,),
            per_quantile_rebuffer_s=(),
            fallback_used=True,
            fallback_reason=reason,
        )
