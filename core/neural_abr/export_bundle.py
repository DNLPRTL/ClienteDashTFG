from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping

import torch

from core.neural_abr.artifacts import ensure_existing_dir, read_json, write_json
from core.neural_abr.bundle import prepare_bundle_output_dir, sha256_file, write_phase4_bundle_manifest
from core.neural_abr.constants import (
    BUNDLE_FALLBACK_POLICY_FILENAME,
    BUNDLE_EXPORT_REPORT_FILENAME,
    BUNDLE_INFERENCE_CONTRACT_FILENAME,
    BUNDLE_LADDER_SCHEMA_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_MODEL_FILENAME,
    BUNDLE_VALIDATION_REPORT_FILENAME,
    CANDIDATE_MODEL_CONFIG_FILENAME,
    CANDIDATE_MODEL_FILENAME,
    CANDIDATE_REVIEW_REPORT_FILENAME,
    FEATURE_SCHEMA_FILENAME,
    FORMAL_TRAINING_REPORT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_FORMAL_TRAINING_SCHEMA_ID,
    PHASE4_INFERENCE_BUNDLE_SCHEMA_ID,
    PRIMARY_TEACHER,
    REWARD_VERSION,
    TRAINING_DATA_SUMMARY_FILENAME,
)
from core.neural_abr.features import build_feature_schema
from core.neural_abr.model_training import load_phase4_candidate_model


class BundleExportError(ValueError):
    """Raised when Phase 4F export cannot build a safe inference bundle."""


def export_phase4_inference_bundle(
    model_dir: object,
    data_dir: object,
    output_dir: object,
    overwrite: bool = False,
) -> Mapping[str, object]:
    model_path = ensure_existing_dir(model_dir, purpose="phase4 candidate model")
    data_path = ensure_existing_dir(data_dir, purpose="phase4 training data")
    output_path = prepare_bundle_output_dir(output_dir, overwrite=overwrite)

    training_report = read_json(model_path / FORMAL_TRAINING_REPORT_FILENAME)
    candidate_review = read_json(model_path / CANDIDATE_REVIEW_REPORT_FILENAME)
    model_config = read_json(model_path / CANDIDATE_MODEL_CONFIG_FILENAME)
    normalization_stats = read_json(model_path / NORMALIZATION_STATS_FILENAME)
    data_summary = read_json(data_path / TRAINING_DATA_SUMMARY_FILENAME)

    _validate_export_inputs(training_report, candidate_review, normalization_stats)
    _model, _normalizer, checkpoint = load_phase4_candidate_model(model_path)
    source_checkpoint = model_path / CANDIDATE_MODEL_FILENAME
    source_checkpoint_hash = sha256_file(source_checkpoint)

    inference_checkpoint = {
        "schema_id": PHASE4_INFERENCE_BUNDLE_SCHEMA_ID,
        "human_readable_name": "Pesos para inferencia offline de NeuralABR-Lite",
        "model_family": "NeuralABR-Lite Candidate Scorer",
        "model_state_dict": checkpoint["model_state_dict"],
        "model_config": dict(model_config),
        "source_candidate_checkpoint_sha256": source_checkpoint_hash,
        "normalization_stats_file": NORMALIZATION_STATS_FILENAME,
        "feature_schema_file": FEATURE_SCHEMA_FILENAME,
        "device": "cpu",
        "controller_registered": False,
        "controller_integrated": False,
    }
    torch.save(inference_checkpoint, output_path / BUNDLE_MODEL_FILENAME)
    write_json(output_path / CANDIDATE_MODEL_CONFIG_FILENAME, model_config)
    write_json(output_path / NORMALIZATION_STATS_FILENAME, normalization_stats)
    write_json(output_path / FEATURE_SCHEMA_FILENAME, build_feature_schema())
    write_json(output_path / BUNDLE_LADDER_SCHEMA_FILENAME, _build_ladder_schema(data_summary))
    write_json(output_path / BUNDLE_MODEL_CARD_FILENAME, _build_model_card(training_report, candidate_review, data_summary, model_config))
    write_json(output_path / BUNDLE_INFERENCE_CONTRACT_FILENAME, _build_inference_contract(model_config))
    write_json(output_path / BUNDLE_FALLBACK_POLICY_FILENAME, _build_fallback_policy())

    manifest = write_phase4_bundle_manifest(
        output_path,
        {
            "created_at_utc": _utc_now(),
            "source_model_dir": str(model_path),
            "source_data_dir": str(data_path),
            "source_training_report": str(model_path / FORMAL_TRAINING_REPORT_FILENAME),
            "source_candidate_review": str(model_path / CANDIDATE_REVIEW_REPORT_FILENAME),
            "source_candidate_checkpoint_sha256": source_checkpoint_hash,
            "source_decision": candidate_review.get("decision"),
            "candidate_ready_for_phase4f": candidate_review.get("candidate_ready_for_phase4f"),
            "model_family": "NeuralABR-Lite Candidate Scorer",
            "training_method": "behavior_cloning",
            "teacher": PRIMARY_TEACHER,
            "reward_version": REWARD_VERSION,
            "action_space": "representation_index",
            "segment_duration_s": data_summary.get("content_ladder", {}).get("segment_duration_s"),
            "offline_inference_only": True,
            "export_bundle_created": True,
            "qoe_improvement_claimed": False,
            "sota_claimed": False,
            "real_world_generalization_claimed": False,
        },
    )
    report = {
        "schema_id": "phase4_export_bundle_inferencia_report_v1",
        "human_readable_name": "Export del bundle de inferencia NeuralABR-Lite",
        "phase": "phase4f_export_bundle_inferencia",
        "status": "PASS",
        "decision": "PHASE4F_EXPORT_BUNDLE_WRITTEN_VALIDATE_NEXT",
        "bundle_dir": str(output_path),
        "source_model_dir": str(model_path),
        "source_data_dir": str(data_path),
        "manifest": str(output_path / "manifiesto_bundle_inferencia.json"),
        "required_files": manifest["required_files"],
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "controller_integrated": False,
        "controller_registered": False,
        "export_bundle_created": True,
        "validation_report_created": False,
        "next_report": BUNDLE_VALIDATION_REPORT_FILENAME,
    }
    write_json(output_path / BUNDLE_EXPORT_REPORT_FILENAME, report)
    return report


def _validate_export_inputs(
    training_report: Mapping[str, object],
    candidate_review: Mapping[str, object],
    normalization_stats: Mapping[str, object],
) -> None:
    if training_report.get("schema_id") != PHASE4_FORMAL_TRAINING_SCHEMA_ID:
        raise BundleExportError("source training report schema_id is invalid")
    if training_report.get("status") != "PASS":
        raise BundleExportError("source training report must be PASS")
    if candidate_review.get("status") != "PASS" or candidate_review.get("candidate_ready_for_phase4f") is not True:
        raise BundleExportError("candidate review must be PASS and ready for Phase 4F")
    if candidate_review.get("hard_failures"):
        raise BundleExportError("candidate review has hard failures")
    if normalization_stats.get("fitted_on_data_role") != "training":
        raise BundleExportError("normalization must be fitted on training only")


def _build_ladder_schema(data_summary: Mapping[str, object]) -> Mapping[str, object]:
    content_ladder = data_summary.get("content_ladder")
    if not isinstance(content_ladder, Mapping):
        raise BundleExportError("training data summary missing content_ladder")
    return {
        "schema_id": "phase4_esquema_ladder_contenido_v1",
        "human_readable_name": "Escalera de representaciones usada por NeuralABR-Lite",
        "action_space": "representation_index",
        "representation_index_policy": "indices enteros contiguos desde cero",
        "content_ladder": dict(content_ladder),
    }


def _build_model_card(
    training_report: Mapping[str, object],
    candidate_review: Mapping[str, object],
    data_summary: Mapping[str, object],
    model_config: Mapping[str, object],
) -> Mapping[str, object]:
    return {
        "schema_id": "phase4_tarjeta_modelo_neural_abr_lite_v1",
        "human_readable_name": "Tarjeta del modelo NeuralABR-Lite exportado",
        "model_family": "NeuralABR-Lite Candidate Scorer",
        "training_method": "behavior_cloning",
        "teacher": PRIMARY_TEACHER,
        "reward_version": REWARD_VERSION,
        "device": "cpu",
        "model_config": dict(model_config),
        "sample_counts_used": dict(training_report.get("sample_counts_used", {})),
        "training_metrics": dict(training_report.get("training_metrics", {})),
        "validation_metrics": dict(training_report.get("validation_metrics", {})),
        "candidate_review_decision": candidate_review.get("decision"),
        "content_ladder": dict(data_summary.get("content_ladder", {})),
        "boundaries": {
            "offline_inference_only": True,
            "controller_integrated": False,
            "controller_registered": False,
            "benchmark_performed": False,
            "ranking_performed": False,
            "qoe_improvement_claimed": False,
            "real_world_generalization_claimed": False,
        },
    }


def _build_inference_contract(model_config: Mapping[str, object]) -> Mapping[str, object]:
    return {
        "schema_id": "phase4_contrato_inferencia_neural_abr_lite_v1",
        "human_readable_name": "Contrato de inferencia CPU para NeuralABR-Lite",
        "model_config": dict(model_config),
        "input_contract": {
            "context_features": "features de estado recientes, sin metadata de traza",
            "candidate_features": "features por representacion candidata del MPD",
            "action_mask": "mascara booleana por representation_index",
        },
        "output_contract": {
            "scores": "score finito por representacion candidata",
            "selected_representation_index": "accion valida bajo action_mask",
        },
        "hard_rules": [
            "no usar trace_id, dataset_id, split, leakage_group ni metadata como feature",
            "no usar throughput futuro",
            "no devolver acciones fuera del MPD",
            "no integrar controller en Phase 4F",
        ],
        "cpu_only": True,
        "deterministic_eval_required": True,
    }


def _build_fallback_policy() -> Mapping[str, object]:
    return {
        "schema_id": "phase4_politica_respaldo_neural_abr_lite_v1",
        "human_readable_name": "Politica de respaldo para una integracion futura",
        "phase4f_executes_fallback": False,
        "future_integration_only": True,
        "fallback_required_when": [
            "bundle ausente o invalido",
            "schema incompatible",
            "fallo de carga del modelo",
            "score NaN o infinito",
            "accion invalida o enmascarada",
            "latencia fuera de contrato futuro",
        ],
        "safe_fallback_family": "controller clasico ya validado",
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
