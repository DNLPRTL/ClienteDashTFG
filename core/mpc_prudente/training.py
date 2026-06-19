"""Entrenamiento del predictor de cuantiles para MPC Prudente.

Reutiliza el entrenador probado de Neural-MPC (`train_phase45_v3_throughput_quantile_predictor`)
SIN tocarlo, y le añade lo que faltaba para esta era: **gates de calibración reales**.

El entrenador base solo comprobaba que la loss fuese finita (que no explotara a NaN).
Para un predictor de cuantiles eso no basta: lo que importa es que esté
**bien calibrado** (la cobertura empírica de cada cuantil ≈ su nivel nominal) y que
los cuantiles sean **monótonos** (sin crossing), porque el planner prudente confiará
en la cola de la distribución para decidir con seguridad.

Por eso, tras entrenar, se hace una auditoría de calibración sobre validación.
"""

from __future__ import annotations

import math
from datetime import datetime, timezone
from typing import Mapping, Sequence

import torch

from core.neural_abr.artifacts import ensure_existing_dir, write_json
from core.phase45_v3.constants import VALIDATION_ROLE
from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_MODEL_FILENAME,
    ThroughputQuantileNormalization,
    ThroughputQuantileTrainingProfile,
    load_throughput_quantile_examples,
    throughput_quantile_examples_to_tensors,
    train_phase45_v3_throughput_quantile_predictor,
)
from core.phase45_v3.throughput_quantile_dataset import THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME
from core.phase45_v3.throughput_quantile_model import ThroughputQuantilePredictor

MPC_PRUDENTE_TRAINING_REPORT_SCHEMA_ID = "mpc_prudente_throughput_quantile_training_report_v1"
MPC_PRUDENTE_CALIBRATION_REPORT_FILENAME = "reporte_calibracion_mpc_prudente.json"
MPC_PRUDENTE_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_mpc_prudente.json"

# Tolerancia de calibración: |cobertura_empírica - cuantil_nominal| <= tol.
DEFAULT_COVERAGE_TOLERANCE = 0.08
# Fracción máxima de filas con cuantiles cruzados (no monótonos).
DEFAULT_MAX_CROSSING_RATE = 0.02


class MpcPrudenteTrainingError(ValueError):
    """Raised when the prudent predictor training/calibration cannot proceed."""


def train_mpc_prudente_predictor(
    dataset_dir: object,
    output_dir: object,
    profile: ThroughputQuantileTrainingProfile,
    *,
    overwrite: bool = False,
    device: str | None = None,
    coverage_tolerance: float = DEFAULT_COVERAGE_TOLERANCE,
    max_crossing_rate: float = DEFAULT_MAX_CROSSING_RATE,
) -> Mapping[str, object]:
    base_report = train_phase45_v3_throughput_quantile_predictor(
        dataset_dir, output_dir, profile, overwrite=overwrite, device=device
    )

    data_dir = ensure_existing_dir(dataset_dir, purpose="mpc_prudente dataset")
    output_path = ensure_existing_dir(output_dir, purpose="mpc_prudente training output")

    model, normalization = _load_trained_model(output_path)
    validation_examples = load_throughput_quantile_examples(
        data_dir / THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME, VALIDATION_ROLE, None, profile
    )
    context_t, target_t = throughput_quantile_examples_to_tensors(validation_examples, normalization)
    with torch.no_grad():
        prediction = model(context_t)  # [N, horizon, quantiles]

    calibration = _calibration_metrics(prediction, target_t, profile.quantiles)
    gates = _calibration_gates(
        base_report=base_report,
        calibration=calibration,
        coverage_tolerance=float(coverage_tolerance),
        max_crossing_rate=float(max_crossing_rate),
    )

    calibration_report = {
        "schema_id": "mpc_prudente_calibration_report_v1",
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "validation_sample_count": int(context_t.shape[0]),
        "quantiles": [float(q) for q in profile.quantiles],
        "coverage_tolerance": float(coverage_tolerance),
        "max_crossing_rate": float(max_crossing_rate),
        **calibration,
        "gates": gates,
    }
    write_json(output_path / MPC_PRUDENTE_CALIBRATION_REPORT_FILENAME, calibration_report)

    status = "PASS" if base_report["status"] == "PASS" and not gates["failed"] else "REVIEW"
    report = {
        "schema_id": MPC_PRUDENTE_TRAINING_REPORT_SCHEMA_ID,
        "status": status,
        "base_training_status": base_report["status"],
        "device": base_report["device"],
        "dataset_dir": str(data_dir),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "train_sample_count": base_report["train_sample_count"],
        "validation_sample_count": base_report["validation_sample_count"],
        "best_epoch": _best_epoch(base_report),
        "final_validation": base_report["final_validation"],
        "calibration": calibration_report,
        "model_path": base_report["model_path"],
        "model_sha256": base_report["model_sha256"],
        "elapsed_s": base_report["elapsed_s"],
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
        "controller_integrated": False,
    }
    write_json(output_path / MPC_PRUDENTE_TRAINING_REPORT_FILENAME, report)
    return report


def _load_trained_model(output_path) -> tuple[ThroughputQuantilePredictor, ThroughputQuantileNormalization]:
    checkpoint_path = output_path / THROUGHPUT_QUANTILE_MODEL_FILENAME
    # Checkpoint propio recién escrito: weights_only=False para leer config+normalización.
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    config = checkpoint["model_config"]
    model = ThroughputQuantilePredictor(
        input_dim=int(config["input_dim"]),
        horizon_segments=int(config["horizon_segments"]),
        quantiles=tuple(float(q) for q in config["quantiles"]),
        hidden_sizes=tuple(int(h) for h in config["hidden_sizes"]),
    )
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    norm = checkpoint["normalization"]
    normalization = ThroughputQuantileNormalization(
        schema_id=str(norm["schema_id"]),
        context_mean=tuple(float(v) for v in norm["context_mean"]),
        context_std=tuple(float(v) for v in norm["context_std"]),
    )
    return model, normalization


def _calibration_metrics(
    prediction: torch.Tensor, target: torch.Tensor, quantiles: Sequence[float]
) -> Mapping[str, object]:
    # prediction [N, H, Q]; target [N, H].
    target_exp = target.unsqueeze(2)  # [N, H, 1]
    below = (target_exp <= prediction).float()  # [N, H, Q]
    empirical_coverage = below.mean(dim=(0, 1)).tolist()  # por cuantil
    coverage_error = [
        abs(float(empirical_coverage[k]) - float(quantiles[k])) for k in range(len(quantiles))
    ]
    # Monotonía: filas (n,h) con algún par adyacente cruzado.
    diffs = prediction[:, :, 1:] - prediction[:, :, :-1]  # >=0 si monótono creciente
    crossed_rows = (diffs < 0).any(dim=2).float()  # [N, H]
    crossing_rate = float(crossed_rows.mean().item()) if crossed_rows.numel() else 0.0
    crossing_magnitude = float(torch.relu(-diffs).mean().item()) if diffs.numel() else 0.0
    return {
        "empirical_coverage_by_quantile": [round(float(v), 6) for v in empirical_coverage],
        "coverage_abs_error_by_quantile": [round(float(v), 6) for v in coverage_error],
        "max_coverage_abs_error": round(max(coverage_error), 6) if coverage_error else 0.0,
        "quantile_crossing_rate": round(crossing_rate, 6),
        "quantile_crossing_magnitude": round(crossing_magnitude, 6),
    }


def _calibration_gates(
    *,
    base_report: Mapping[str, object],
    calibration: Mapping[str, object],
    coverage_tolerance: float,
    max_crossing_rate: float,
) -> Mapping[str, object]:
    final_pinball = float(base_report["final_validation"]["pinball_loss"])  # type: ignore[index]
    learned = _learned_signal(base_report)
    gates = {
        "coverage_calibrated": {
            "passed": float(calibration["max_coverage_abs_error"]) <= coverage_tolerance,
            "observed": calibration["max_coverage_abs_error"],
            "threshold": coverage_tolerance,
        },
        "quantiles_monotone": {
            "passed": float(calibration["quantile_crossing_rate"]) <= max_crossing_rate,
            "observed": calibration["quantile_crossing_rate"],
            "threshold": max_crossing_rate,
        },
        "finite_validation_pinball": {
            "passed": math.isfinite(final_pinball),
            "observed": final_pinball,
            "threshold": "finite",
        },
        "learned_signal_over_epoch1": {
            "passed": bool(learned["passed"]),
            "observed": learned["observed"],
            "threshold": "final_pinball < epoch1_pinball",
        },
    }
    failed = [name for name, gate in gates.items() if not gate["passed"]]
    return {"failed": failed, "gates": gates}


def _epoch_validation_pinball(epoch_record: Mapping[str, object]) -> float:
    return float(epoch_record["validation"]["pinball_loss"])  # type: ignore[index]


def _best_epoch(base_report: Mapping[str, object]) -> int:
    epochs = list(base_report.get("epochs", []))  # type: ignore[arg-type]
    if not epochs:
        return 0
    best = min(epochs, key=_epoch_validation_pinball)
    return int(best["epoch"])


def _learned_signal(base_report: Mapping[str, object]) -> Mapping[str, object]:
    epochs = list(base_report.get("epochs", []))  # type: ignore[arg-type]
    final_pinball = float(base_report["final_validation"]["pinball_loss"])  # type: ignore[index]
    if not epochs:
        return {"passed": False, "observed": {"final_pinball": final_pinball}}
    epoch1_pinball = _epoch_validation_pinball(epochs[0])
    passed = math.isfinite(final_pinball) and final_pinball < epoch1_pinball
    return {
        "passed": bool(passed),
        "observed": {"epoch1_pinball": round(epoch1_pinball, 6), "final_pinball": round(final_pinball, 6)},
    }
