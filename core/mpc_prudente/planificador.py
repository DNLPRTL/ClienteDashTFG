"""Planner MPC prudente: evalúa cada secuencia de acciones bajo todos los
cuantiles de throughput predichos y agrega con CVaR_alpha (media de los peores
escenarios), usando los tamaños reales (VBR) de los segmentos.

El nivel de riesgo `alpha` es configurable: existe una regla adaptativa por buffer
(`alpha_riesgo_por_buffer`, usada en los diagnósticos offline), pero en la evaluación
final de Phase 6 se fijó `alpha=0.75` (media de los 3 peores escenarios de 4).
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Callable, Sequence

from core.controller.robust_mpc import RobustMpcController
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopState, runtime_feedback_from_state

CLAVE_CONTROLLER_MPC_PRUDENTE = "mpc_prudente_v1"
CUANTILES_POR_DEFECTO = (0.10, 0.25, 0.50, 0.75)
HORIZONTE_POR_DEFECTO = 5
PESO_REBUFFER_POR_DEFECTO = 4.3
PESO_SUAVIDAD_POR_DEFECTO = 1.0

# Niveles de riesgo CVaR por buffer (fracción de peores escenarios a promediar).
ALPHA_BUFFER_BAJO = 0.25
ALPHA_BUFFER_MEDIO = 0.50
ALPHA_BUFFER_ALTO = 0.75
ALPHA_BUFFER_SEGURO = 1.00
UMBRAL_BUFFER_BAJO_S = 4.0
UMBRAL_BUFFER_MEDIO_S = 12.0
UMBRAL_BUFFER_ALTO_S = 20.0


class ErrorPlanificadorPrudente(ValueError):
    """Error cuando el planificador no puede tomar una decision segura."""


@dataclass(frozen=True)
class DecisionPrudente:
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
            "controller_key": CLAVE_CONTROLLER_MPC_PRUDENTE,
            "action": int(self.action),
            "bitrate_bps": float(self.bitrate_bps),
            "risk_alpha": float(self.risk_alpha),
            "cvar_score": float(self.cvar_score),
            "best_sequence": [int(value) for value in self.best_sequence],
            "per_quantile_rebuffer_s": [float(value) for value in self.per_quantile_rebuffer_s],
            "fallback_used": bool(self.fallback_used),
            "fallback_reason": self.fallback_reason,
        }


def alpha_riesgo_por_buffer(buffer_s: float) -> float:
    """Nivel CVaR según el buffer: menos buffer → más pesimista (alpha menor)."""
    buffer = float(buffer_s)
    if buffer < UMBRAL_BUFFER_BAJO_S:
        return ALPHA_BUFFER_BAJO
    if buffer < UMBRAL_BUFFER_MEDIO_S:
        return ALPHA_BUFFER_MEDIO
    if buffer < UMBRAL_BUFFER_ALTO_S:
        return ALPHA_BUFFER_ALTO
    return ALPHA_BUFFER_SEGURO


def planificar_accion_prudente(
    *,
    state: AbrClosedLoopState,
    ladder,
    prediccion_bps_por_horizonte_y_cuantil: Sequence[Sequence[float]],
    quantiles: Sequence[float] = CUANTILES_POR_DEFECTO,
    horizon_segments: int = HORIZONTE_POR_DEFECTO,
    action_mask: Sequence[bool] | None = None,
    risk_alpha: float | None = None,
    rebuffer_weight: float = PESO_REBUFFER_POR_DEFECTO,
    switch_weight: float = PESO_SUAVIDAD_POR_DEFECTO,
) -> DecisionPrudente:
    prediction = _validar_prediccion(prediccion_bps_por_horizonte_y_cuantil, horizon_segments, len(tuple(quantiles)))
    alpha = float(risk_alpha) if risk_alpha is not None else alpha_riesgo_por_buffer(state.buffer_s)
    valid_actions = _acciones_validas(action_mask, ladder.representation_count)
    if not valid_actions:
        raise ErrorPlanificadorPrudente("no hay acciones validas para el MPC prudente")

    remaining = max(int(ladder.segment_count) - int(state.segment_index), 1)
    effective_horizon = min(int(horizon_segments), len(prediction), remaining)

    best_score = -math.inf
    best_sequence: tuple[int, ...] | None = None
    best_rebuffer: tuple[float, ...] = ()
    for sequence in itertools.product(valid_actions, repeat=effective_horizon):
        cvar, per_quantile_rebuffer = _puntuar_secuencia_cvar(
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
        raise ErrorPlanificadorPrudente("la enumeracion del MPC prudente no produjo secuencia")
    action = int(best_sequence[0])
    return DecisionPrudente(
        action=action,
        bitrate_bps=float(ladder.bitrate_bps(action)),
        risk_alpha=float(alpha),
        cvar_score=float(best_score),
        best_sequence=best_sequence,
        per_quantile_rebuffer_s=tuple(float(value) for value in best_rebuffer),
    )


def _puntuar_secuencia_cvar(
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


def _validar_prediccion(
    prediction: Sequence[Sequence[float]], horizon_segments: int, quantile_count: int
) -> tuple[tuple[float, ...], ...]:
    rows = []
    for row in prediction:
        values = tuple(float(value) for value in row)
        if len(values) != int(quantile_count):
            raise ErrorPlanificadorPrudente("dimension de cuantiles de la prediccion incorrecta")
        if any(not math.isfinite(value) or value <= 0.0 for value in values):
            raise ErrorPlanificadorPrudente("la prediccion contiene throughput invalido")
        # Forzar monotonía (q ascendente) por robustez ante crossing residual.
        rows.append(tuple(sorted(values)))
    if len(rows) < int(horizon_segments):
        raise ErrorPlanificadorPrudente("la prediccion tiene menos horizontes de los pedidos")
    return tuple(rows)


def _acciones_validas(action_mask: Sequence[bool] | None, representation_count: int) -> tuple[int, ...]:
    if action_mask is None:
        return tuple(range(int(representation_count)))
    return tuple(index for index, allowed in enumerate(action_mask[: int(representation_count)]) if bool(allowed))


class ControllerMpcPrudente:
    """Controller candidato: cuantiles neuronales + planner MPC prudente (CVaR)."""

    def __init__(
        self,
        predictor: Callable[[AbrClosedLoopState, object], Sequence[Sequence[float]]],
        *,
        quantiles: Sequence[float] = CUANTILES_POR_DEFECTO,
        horizon_segments: int = HORIZONTE_POR_DEFECTO,
        funcion_alpha_riesgo: Callable[[float], float] = alpha_riesgo_por_buffer,
    ) -> None:
        self.predictor = predictor
        self.quantiles = tuple(float(value) for value in quantiles)
        self.horizon_segments = int(horizon_segments)
        self.funcion_alpha_riesgo = funcion_alpha_riesgo
        self.last_decision: DecisionPrudente | None = None
        self._fallback = RobustMpcController(horizon=self.horizon_segments)

    def select_action(
        self, state: AbrClosedLoopState, ladder, action_mask: Sequence[bool] | None = None
    ) -> DecisionPrudente:
        try:
            prediction = tuple(tuple(float(value) for value in row) for row in self.predictor(state, ladder))
            decision = planificar_accion_prudente(
                state=state,
                ladder=ladder,
                prediccion_bps_por_horizonte_y_cuantil=prediction,
                quantiles=self.quantiles,
                horizon_segments=self.horizon_segments,
                action_mask=action_mask,
                risk_alpha=self.funcion_alpha_riesgo(float(state.buffer_s)),
            )
        except Exception as exc:  # noqa: BLE001 - fallback explícito y auditado.
            decision = self._decidir_por_fallback(state, ladder, str(type(exc).__name__))
        self.last_decision = decision
        return decision

    def _decidir_por_fallback(self, state: AbrClosedLoopState, ladder, reason: str) -> DecisionPrudente:
        feedback = dict(runtime_feedback_from_state(state, ladder))
        feedback["throughput_history_bps"] = [float(value) for value in state.throughput_history_bps]
        self._fallback.setPlayerFeedback(feedback)
        target_rate_Bps = float(self._fallback.calcControlAction())
        action = int(self._fallback.quantizeRate(target_rate_Bps))
        return DecisionPrudente(
            action=action,
            bitrate_bps=float(ladder.bitrate_bps(action)),
            risk_alpha=0.0,
            cvar_score=0.0,
            best_sequence=(action,),
            per_quantile_rebuffer_s=(),
            fallback_used=True,
            fallback_reason=reason,
        )
