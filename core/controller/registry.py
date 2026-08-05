from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Mapping, Optional

from .bola import BolaController
from .bba import BbaController
from .fixed_quality import FixedQualityController
from .max_quality_controller import MaxQualityController
from .mpc import MpcController
from .mpc_prudente_runtime import ControllerRuntimeMpcPrudente, ControllerRuntimeMpcPrudenteTemporal
from .neural_abr_lite import NeuralAbrLiteRobustMpcController, NeuralAbrLiteTeacherHibridoController
from .phase45_v3_neural_mpc import Phase45V3NeuralMpcController, Phase45V3NeuralMpcV2Controller
from .rate_based import RateBasedController
from .robust_mpc import RobustMpcController
from .sanity_rate import FixedRateController, MaxRateController, MinRateController
from .scripted_quality import ScriptedQualityController
from .spbc_abr_v2_dpo import SpbcAbrV2DpoAnchorSafeRankController


@dataclass(frozen=True)
class ControllerSpec:
    key: str
    label: str
    factory: Callable[..., object]


CONTROLLER_REGISTRY = {
    "min_rate": ControllerSpec(
        key="min_rate",
        label="Min rate (sanity/control)",
        factory=MinRateController,
    ),
    "fixed_rate": ControllerSpec(
        key="fixed_rate",
        label="Fixed rate or level (sanity/control)",
        factory=FixedRateController,
    ),
    "max_rate": ControllerSpec(
        key="max_rate",
        label="Max rate (sanity/control)",
        factory=MaxRateController,
    ),
    "rate_based": ControllerSpec(
        key="rate_based",
        label="Rate-based throughput baseline",
        factory=RateBasedController,
    ),
    "bba": ControllerSpec(
        key="bba",
        label="BBA buffer-based baseline",
        factory=BbaController,
    ),
    "bola": ControllerSpec(
        key="bola",
        label="BOLA-basic utility/buffer baseline",
        factory=BolaController,
    ),
    "mpc": ControllerSpec(
        key="mpc",
        label="MPC hybrid planning baseline",
        factory=MpcController,
    ),
    "robust_mpc": ControllerSpec(
        key="robust_mpc",
        label="RobustMPC conservative planning baseline",
        factory=RobustMpcController,
    ),
    "neural_abr_lite_robust_mpc": ControllerSpec(
        key="neural_abr_lite_robust_mpc",
        label="NeuralABR-Lite guarded controller (robust_mpc teacher)",
        factory=NeuralAbrLiteRobustMpcController,
    ),
    "neural_abr_lite_teacher_hibrido": ControllerSpec(
        key="neural_abr_lite_teacher_hibrido",
        label="NeuralABR-Lite guarded controller (teacher_hibrido)",
        factory=NeuralAbrLiteTeacherHibridoController,
    ),
    "spbc_abr_v2_dpo_anchor_safe_rank": ControllerSpec(
        key="spbc_abr_v2_dpo_anchor_safe_rank",
        label="SPBC ABR v2 DPO guarded controller (anchor safe-rank)",
        factory=SpbcAbrV2DpoAnchorSafeRankController,
    ),
    "phase45_v3_neural_throughput_calibrated_mpc_v1": ControllerSpec(
        key="phase45_v3_neural_throughput_calibrated_mpc_v1",
        label="Phase45 v3 Neural Throughput-Calibrated MPC",
        factory=Phase45V3NeuralMpcController,
    ),
    "phase45_v3_neural_throughput_calibrated_mpc_v2": ControllerSpec(
        key="phase45_v3_neural_throughput_calibrated_mpc_v2",
        label="Phase45 v3 Neural Throughput-Calibrated MPC v2",
        factory=Phase45V3NeuralMpcV2Controller,
    ),
    "mpc_prudente_v1": ControllerSpec(
        key="mpc_prudente_v1",
        label="MPC Neuronal Prudente (media-faithful, risk-aware)",
        factory=ControllerRuntimeMpcPrudente,
    ),
    "mpc_prudente_v2": ControllerSpec(
        key="mpc_prudente_v2",
        label="MPC Neuronal Prudente v2 (temporal ensemble)",
        factory=ControllerRuntimeMpcPrudenteTemporal,
    ),
    "fixed_quality": ControllerSpec(
        key="fixed_quality",
        label="Fixed quality (test/debug)",
        factory=FixedQualityController,
    ),
    "scripted_quality": ControllerSpec(
        key="scripted_quality",
        label="Scripted quality (test/debug)",
        factory=ScriptedQualityController,
    ),
    "max_quality": ControllerSpec(
        key="max_quality",
        label="Max quality (legacy/debug/stress)",
        factory=MaxQualityController,
    ),
}


def available_controllers():
    return list(CONTROLLER_REGISTRY.values())


def create_controller(key, params: Optional[Mapping[str, object]] = None):
    try:
        return CONTROLLER_REGISTRY[key].factory(**dict(params or {}))
    except KeyError as exc:
        available = ", ".join(sorted(CONTROLLER_REGISTRY))
        raise ValueError(f"Unknown controller '{key}'. Available: {available}") from exc
