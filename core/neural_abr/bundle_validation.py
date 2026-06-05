from __future__ import annotations

from pathlib import Path
from typing import Mapping

from core.neural_abr.artifacts import write_json
from core.neural_abr.bundle import BundleError, validate_phase4_bundle_dir
from core.neural_abr.constants import (
    BUNDLE_VALIDATION_REPORT_FILENAME,
    PHASE4_BUNDLE_VALIDATION_SCHEMA_ID,
)
from core.neural_abr.inference import InferenceError, run_phase4_inference_smoke


class BundleValidationError(ValueError):
    """Raised when Phase 4F validation cannot complete."""


def validate_phase4_inference_bundle(
    bundle_dir: object,
    data_dir: object,
    output_dir: object,
    max_samples: int = 512,
    latency_p95_limit_ms: float = 10.0,
) -> Mapping[str, object]:
    output_path = Path(output_dir).expanduser().resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    gates: dict[str, Mapping[str, object]] = {}
    bundle_report: Mapping[str, object] | None = None
    smoke_report: Mapping[str, object] | None = None

    try:
        bundle_report = validate_phase4_bundle_dir(bundle_dir)
        gates["bundle_files_and_hashes"] = _gate(True, "required files present and sha256 hashes valid")
    except BundleError as exc:
        gates["bundle_files_and_hashes"] = _gate(False, str(exc))

    if bundle_report is not None:
        try:
            smoke_report = run_phase4_inference_smoke(bundle_dir, data_dir, output_dir=output_path, max_samples=max_samples)
            gates["model_loads_and_scores_cpu"] = _gate(True, "bundle loads and scores validation samples on CPU")
            gates["valid_action_rate_is_1"] = _gate(smoke_report.get("valid_action_rate") == 1.0, smoke_report.get("valid_action_rate"))
            gates["deterministic_rate_is_1"] = _gate(smoke_report.get("deterministic_rate") == 1.0, smoke_report.get("deterministic_rate"))
            gates["no_nan_inf_scores"] = _gate(smoke_report.get("no_nan_inf_scores") is True, smoke_report.get("no_nan_inf_scores"))
            p95_ms = _p95(smoke_report)
            gates["p95_latency_under_limit"] = _gate(
                p95_ms is not None and p95_ms <= float(latency_p95_limit_ms),
                {"p95_ms": p95_ms, "limit_ms": float(latency_p95_limit_ms)},
            )
        except (BundleError, InferenceError) as exc:
            gates["model_loads_and_scores_cpu"] = _gate(False, str(exc))
            gates["valid_action_rate_is_1"] = _gate(False, str(exc))
            gates["deterministic_rate_is_1"] = _gate(False, str(exc))
            gates["no_nan_inf_scores"] = _gate(False, str(exc))
            gates["p95_latency_under_limit"] = _gate(False, str(exc))
    else:
        for name in (
            "model_loads_and_scores_cpu",
            "valid_action_rate_is_1",
            "deterministic_rate_is_1",
            "no_nan_inf_scores",
            "p95_latency_under_limit",
        ):
            gates[name] = _gate(False, "bundle files/hash validation failed first")

    hard_gate_names = (
        "bundle_files_and_hashes",
        "model_loads_and_scores_cpu",
        "valid_action_rate_is_1",
        "deterministic_rate_is_1",
        "no_nan_inf_scores",
    )
    readiness_gate_names = ("p95_latency_under_limit",)
    hard_failures = [name for name in hard_gate_names if gates[name]["status"] != "PASS"]
    readiness_warnings = [name for name in readiness_gate_names if gates[name]["status"] != "PASS"]
    if hard_failures:
        status = "BLOCKED_NEEDS_FIX"
        decision = "PHASE4F_EXPORT_BUNDLE_BLOCKED_NEEDS_FIX"
        ready = False
    elif readiness_warnings:
        status = "PASS_WITH_WARNINGS"
        decision = "PHASE4F_EXPORT_BUNDLE_PASS_WITH_LATENCY_WARNING"
        ready = False
    else:
        status = "PASS"
        decision = "PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G"
        ready = True

    report = {
        "schema_id": PHASE4_BUNDLE_VALIDATION_SCHEMA_ID,
        "human_readable_name": "Validacion del bundle de inferencia NeuralABR-Lite",
        "phase": "phase4f_export_bundle_inferencia",
        "status": status,
        "decision": decision,
        "ready_for_phase4g": ready,
        "bundle_dir": str(Path(bundle_dir).expanduser().resolve()),
        "data_dir": str(Path(data_dir).expanduser().resolve()),
        "output_dir": str(output_path),
        "max_samples": int(max_samples),
        "gates": gates,
        "hard_gate_names": list(hard_gate_names),
        "readiness_gate_names": list(readiness_gate_names),
        "hard_failures": hard_failures,
        "readiness_warnings": readiness_warnings,
        "bundle_report": bundle_report or {},
        "inference_smoke_report": smoke_report or {},
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "controller_integrated": False,
        "controller_registered": False,
        "qoe_improvement_claimed": False,
        "real_world_generalization_claimed": False,
    }
    write_json(output_path / BUNDLE_VALIDATION_REPORT_FILENAME, report)
    return report


def _gate(passed: bool, details: object) -> Mapping[str, object]:
    return {
        "status": "PASS" if bool(passed) else "FAIL",
        "passed": bool(passed),
        "details": details,
    }


def _p95(smoke_report: Mapping[str, object]) -> float | None:
    latency = smoke_report.get("latency_summary")
    if not isinstance(latency, Mapping):
        return None
    value = latency.get("p95_ms")
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
