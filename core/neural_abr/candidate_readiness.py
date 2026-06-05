from __future__ import annotations

import hashlib
import math
from pathlib import Path
from typing import Iterable, Mapping

from core.neural_abr.artifacts import ensure_existing_dir, ensure_outside_repo, read_json, write_json
from core.neural_abr.constants import (
    CANDIDATE_MODEL_FILENAME,
    CANDIDATE_REVIEW_REPORT_FILENAME,
    FORMAL_TRAINING_REPORT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_CANDIDATE_REVIEW_SCHEMA_ID,
    PHASE4_FORMAL_TRAINING_SCHEMA_ID,
    PHASE4_NORMALIZATION_SCHEMA_ID,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.neural_abr.model_training import load_phase4_candidate_model
from core.neural_abr.training_data_validation import validate_phase4_training_data_dir


class CandidateReadinessError(ValueError):
    """Raised when a Phase 4E candidate review cannot be completed."""


def assess_phase4_candidate_model(
    model_dir: object,
    data_dir: object | None = None,
    output_dir: object | None = None,
    min_training_samples: int = 1000,
    min_validation_samples: int = 250,
    min_training_teacher_agreement: float = 0.85,
    min_validation_teacher_agreement: float = 0.80,
) -> Mapping[str, object]:
    model_path = ensure_existing_dir(model_dir, purpose="phase4 candidate model")
    report_path = model_path / FORMAL_TRAINING_REPORT_FILENAME
    training_report = read_json(report_path)
    if training_report.get("schema_id") != PHASE4_FORMAL_TRAINING_SCHEMA_ID:
        raise CandidateReadinessError("training report schema_id is invalid")

    source_data_dir = data_dir if data_dir is not None else training_report.get("source_training_data_dir")
    if not source_data_dir:
        raise CandidateReadinessError("data_dir is required when training report has no source path")
    data_validation = validate_phase4_training_data_dir(source_data_dir)
    output_path = ensure_outside_repo(output_dir or model_path, purpose="phase4 candidate review output")
    if output_path.exists() and not output_path.is_dir():
        raise CandidateReadinessError("candidate review output exists and is not a directory: {0}".format(output_path))
    output_path.mkdir(parents=True, exist_ok=True)
    normalization = read_json(model_path / NORMALIZATION_STATS_FILENAME)

    load_error = None
    try:
        load_phase4_candidate_model(model_path)
    except Exception as exc:  # noqa: BLE001 - this becomes a gate detail.
        load_error = str(exc)

    checkpoint_path = model_path / CANDIDATE_MODEL_FILENAME
    checkpoint_hash = _sha256_file(checkpoint_path) if checkpoint_path.is_file() else None
    expected_hash = _mapping(training_report.get("artifacts")).get("checkpoint_sha256")
    training_metrics = _mapping(training_report.get("training_metrics"))
    validation_metrics = _mapping(training_report.get("validation_metrics"))
    sample_counts = _mapping(training_report.get("sample_counts_used"))

    gates = {
        "training_report_pass": _gate(training_report.get("status") == "PASS", training_report.get("status")),
        "checkpoint_exists": _gate(checkpoint_path.is_file(), str(checkpoint_path)),
        "checkpoint_hash_matches_report": _gate(
            bool(checkpoint_hash) and checkpoint_hash == expected_hash,
            {"computed": checkpoint_hash, "expected": expected_hash},
        ),
        "checkpoint_loads_on_cpu": _gate(load_error is None, load_error or "loaded"),
        "data_validation_pass": _gate(data_validation.get("status") == "PASS", data_validation.get("status")),
        "normalization_train_only": _gate(
            normalization.get("schema_id") == PHASE4_NORMALIZATION_SCHEMA_ID
            and normalization.get("fitted_on_data_role") == TRAINING_ROLE,
            {
                "schema_id": normalization.get("schema_id"),
                "fitted_on_data_role": normalization.get("fitted_on_data_role"),
            },
        ),
        "cpu_training": _gate(training_report.get("device") == "cpu", training_report.get("device")),
        "no_benchmark_or_ranking": _gate(
            training_report.get("benchmark_performed") is False
            and training_report.get("outputs_are_benchmark_results") is False
            and training_report.get("ranking_performed") is False
            and training_report.get("no_final_ranking") is True,
            {
                "benchmark_performed": training_report.get("benchmark_performed"),
                "outputs_are_benchmark_results": training_report.get("outputs_are_benchmark_results"),
                "ranking_performed": training_report.get("ranking_performed"),
                "no_final_ranking": training_report.get("no_final_ranking"),
            },
        ),
        "formal_training_was_declared": _gate(
            training_report.get("ia_training_performed") is True
            and training_report.get("formal_ia_training_performed") is True
            and training_report.get("candidate_model_created") is True,
            {
                "ia_training_performed": training_report.get("ia_training_performed"),
                "formal_ia_training_performed": training_report.get("formal_ia_training_performed"),
                "candidate_model_created": training_report.get("candidate_model_created"),
            },
        ),
        "no_controller_or_export_scope": _gate(
            training_report.get("controller_registered") is False
            and training_report.get("controller_integrated") is False
            and training_report.get("export_bundle_created") is False,
            {
                "controller_registered": training_report.get("controller_registered"),
                "controller_integrated": training_report.get("controller_integrated"),
                "export_bundle_created": training_report.get("export_bundle_created"),
            },
        ),
        "metrics_are_finite": _gate(_all_finite(training_report), "all numeric report values must be finite"),
        "training_valid_action_rate_is_1": _gate(
            _float_eq(training_metrics.get("valid_action_rate"), 1.0),
            training_metrics.get("valid_action_rate"),
        ),
        "validation_valid_action_rate_is_1": _gate(
            _float_eq(validation_metrics.get("valid_action_rate"), 1.0),
            validation_metrics.get("valid_action_rate"),
        ),
        "enough_training_samples": _gate(
            int(sample_counts.get(TRAINING_ROLE, 0) or 0) >= int(min_training_samples),
            {"actual": sample_counts.get(TRAINING_ROLE), "minimum": int(min_training_samples)},
        ),
        "enough_validation_samples": _gate(
            int(sample_counts.get(VALIDATION_ROLE, 0) or 0) >= int(min_validation_samples),
            {"actual": sample_counts.get(VALIDATION_ROLE), "minimum": int(min_validation_samples)},
        ),
        "training_teacher_agreement_high_enough": _gate(
            _float_at_least(training_metrics.get("teacher_agreement"), min_training_teacher_agreement),
            {"actual": training_metrics.get("teacher_agreement"), "minimum": float(min_training_teacher_agreement)},
        ),
        "validation_teacher_agreement_high_enough": _gate(
            _float_at_least(validation_metrics.get("teacher_agreement"), min_validation_teacher_agreement),
            {"actual": validation_metrics.get("teacher_agreement"), "minimum": float(min_validation_teacher_agreement)},
        ),
    }

    hard_gate_names = (
        "training_report_pass",
        "checkpoint_exists",
        "checkpoint_hash_matches_report",
        "checkpoint_loads_on_cpu",
        "data_validation_pass",
        "normalization_train_only",
        "cpu_training",
        "no_benchmark_or_ranking",
        "formal_training_was_declared",
        "no_controller_or_export_scope",
        "metrics_are_finite",
        "training_valid_action_rate_is_1",
        "validation_valid_action_rate_is_1",
    )
    candidate_gate_names = (
        "enough_training_samples",
        "enough_validation_samples",
        "training_teacher_agreement_high_enough",
        "validation_teacher_agreement_high_enough",
    )
    hard_failures = [name for name in hard_gate_names if gates[name]["status"] == "FAIL"]
    candidate_failures = [name for name in candidate_gate_names if gates[name]["status"] == "FAIL"]
    warnings = _prediction_warnings(training_metrics, validation_metrics)
    if hard_failures:
        status = "BLOCKED_NEEDS_FIX"
        decision = "PHASE4E_MODELO_CANDIDATO_BLOCKED_NEEDS_FIX"
        ready = False
    elif candidate_failures:
        status = "PASS_NOT_CANDIDATE"
        decision = "PHASE4E_ENTRENAMIENTO_PASS_NOT_CANDIDATE"
        ready = False
    else:
        status = "PASS"
        decision = "PHASE4E_MODELO_CANDIDATO_READY_FOR_PHASE4F"
        ready = True

    review = {
        "schema_id": PHASE4_CANDIDATE_REVIEW_SCHEMA_ID,
        "human_readable_name": "Revision del modelo candidato NeuralABR-Lite",
        "phase": "phase4e_entrenamiento_modelo_candidato_offline",
        "status": status,
        "decision": decision,
        "candidate_ready_for_phase4f": ready,
        "model_dir": str(model_path),
        "data_dir": str(Path(source_data_dir).expanduser().resolve()),
        "output_dir": str(output_path),
        "training_report": str(report_path),
        "hard_gate_names": list(hard_gate_names),
        "candidate_gate_names": list(candidate_gate_names),
        "gates": gates,
        "hard_failures": hard_failures,
        "candidate_readiness_failures": candidate_failures,
        "warnings": warnings,
        "training_metrics": dict(training_metrics),
        "validation_metrics": dict(validation_metrics),
        "sample_counts_used": dict(sample_counts),
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "controller_integrated": False,
        "export_bundle_created": False,
        "qoe_improvement_claimed": False,
        "real_world_generalization_claimed": False,
    }
    write_json(output_path / CANDIDATE_REVIEW_REPORT_FILENAME, review)
    return review


def _gate(passed: bool, details: object) -> Mapping[str, object]:
    return {
        "status": "PASS" if bool(passed) else "FAIL",
        "passed": bool(passed),
        "details": details,
    }


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _float_eq(value: object, expected: float) -> bool:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return False
    return math.isclose(parsed, float(expected), rel_tol=0.0, abs_tol=1e-12)


def _float_at_least(value: object, minimum: float) -> bool:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return False
    return math.isfinite(parsed) and parsed >= float(minimum)


def _all_finite(value: object) -> bool:
    if value is None or isinstance(value, bool):
        return True
    if isinstance(value, (int, float)):
        return math.isfinite(float(value))
    if isinstance(value, Mapping):
        return all(_all_finite(item) for item in value.values())
    if isinstance(value, (str, bytes)):
        return True
    if isinstance(value, Iterable):
        return all(_all_finite(item) for item in value)
    return True


def _prediction_warnings(
    training_metrics: Mapping[str, object],
    validation_metrics: Mapping[str, object],
) -> list[str]:
    warnings = []
    for role_name, metrics in (("training", training_metrics), ("validation", validation_metrics)):
        distribution = _mapping(metrics.get("prediction_distribution"))
        total = sum(int(value) for value in distribution.values())
        if total <= 0:
            continue
        _action, count = max(distribution.items(), key=lambda item: int(item[1]))
        share = int(count) / float(total)
        if share >= 0.95:
            warnings.append("{0} predictions are dominated by one action ({1:.1%})".format(role_name, share))
    return warnings


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
