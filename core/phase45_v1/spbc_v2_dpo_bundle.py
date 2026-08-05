from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping

import torch

from core.neural_abr.artifacts import ensure_outside_repo, prepare_output_dir, read_json, write_json
from core.neural_abr.constants import DEFAULT_CONTEXT_HISTORY_LENGTH, DEFAULT_REPRESENTATION_KBPS, REWARD_VERSION
from core.phase45_v1.spbc_training import CANDIDATE_FEATURES, SCALAR_FEATURES, SEQUENCE_FEATURES
from core.phase45_v1.spbc_v2_dpo_training import (
    SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
    SPBC_V2_DPO_MODEL_KEY,
    SPBC_V2_DPO_TRAINING_REPORT_FILENAME,
)


SPBC_V2_DPO_CONTROLLER_KEY = "spbc_abr_v2_dpo_anchor_safe_rank"
SPBC_V2_DPO_CONTROLLER_ALIAS = "propio_spbc_v2_anchor"
SPBC_V2_DPO_CONTROLLER_DISPLAY_NAME = "Propio SPBC v2 Anchor"

SPBC_V2_DPO_BUNDLE_SCHEMA_ID = "phase45_v2_spbc_dpo_inference_bundle_v1"
SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME = "manifiesto_bundle_inferencia_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_MODEL_FILENAME = "modelo_para_inferencia_spbc_abr_v2_dpo.pt"
SPBC_V2_DPO_BUNDLE_MODEL_CONFIG_FILENAME = "configuracion_modelo_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME = "normalizacion_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME = "esquema_features_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_LADDER_SCHEMA_FILENAME = "esquema_ladder_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME = "tarjeta_modelo_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME = "contrato_inferencia_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_FALLBACK_POLICY_FILENAME = "politica_respaldo_spbc_abr_v2_dpo.json"
SPBC_V2_DPO_BUNDLE_EXPORT_REPORT_FILENAME = "reporte_export_bundle_spbc_abr_v2_dpo.json"

SPBC_V2_DPO_BUNDLE_REQUIRED_FILES = (
    SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_CONFIG_FILENAME,
    SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME,
    SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME,
    SPBC_V2_DPO_BUNDLE_LADDER_SCHEMA_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME,
    SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME,
    SPBC_V2_DPO_BUNDLE_FALLBACK_POLICY_FILENAME,
)
SPBC_V2_DPO_BUNDLE_HASHED_FILES = tuple(
    filename
    for filename in SPBC_V2_DPO_BUNDLE_REQUIRED_FILES
    if filename != SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME
)


class SpbcV2DpoBundleError(ValueError):
    """Raised when a Phase 4-5 v1 SPBC v2 inference bundle is invalid."""


def export_spbc_v2_dpo_inference_bundle(
    *,
    checkpoint_path: object,
    output_dir: object,
    training_report_path: object | None = None,
    overwrite: bool = False,
    expected_checkpoint_sha256: str | None = None,
) -> Mapping[str, object]:
    checkpoint_file = _ensure_existing_file_outside_repo(checkpoint_path, "spbc_abr_v2_dpo checkpoint")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="spbc_abr_v2_dpo inference bundle")
    source_sha256 = sha256_file(checkpoint_file)
    if expected_checkpoint_sha256 and str(expected_checkpoint_sha256).strip().lower() != source_sha256:
        raise SpbcV2DpoBundleError(
            "checkpoint sha256 mismatch: expected {0}, got {1}".format(expected_checkpoint_sha256, source_sha256)
        )

    checkpoint = _torch_load_checkpoint(checkpoint_file)
    _validate_training_checkpoint(checkpoint)
    training_report = _optional_training_report(training_report_path, checkpoint_file)
    model_config = dict(_mapping(checkpoint["model_config"]))
    normalization = dict(_mapping(checkpoint["normalization"]))
    _validate_normalization(normalization)

    inference_checkpoint = {
        "schema_id": SPBC_V2_DPO_BUNDLE_SCHEMA_ID,
        "model_key": SPBC_V2_DPO_MODEL_KEY,
        "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
        "model_state_dict": checkpoint["model_state_dict"],
        "model_config": model_config,
        "normalization": normalization,
        "source_checkpoint_sha256": source_sha256,
        "source_checkpoint_best_epoch": checkpoint.get("best_epoch"),
        "device": "cpu",
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
    }
    torch.save(inference_checkpoint, output_path / SPBC_V2_DPO_BUNDLE_MODEL_FILENAME)
    write_json(output_path / SPBC_V2_DPO_BUNDLE_MODEL_CONFIG_FILENAME, model_config)
    write_json(output_path / SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME, normalization)
    write_json(output_path / SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME, build_spbc_v2_dpo_feature_schema())
    write_json(output_path / SPBC_V2_DPO_BUNDLE_LADDER_SCHEMA_FILENAME, build_spbc_v2_dpo_ladder_schema())
    write_json(
        output_path / SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME,
        build_spbc_v2_dpo_model_card(checkpoint_file, source_sha256, checkpoint, training_report),
    )
    write_json(output_path / SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME, build_spbc_v2_dpo_inference_contract())
    write_json(output_path / SPBC_V2_DPO_BUNDLE_FALLBACK_POLICY_FILENAME, build_spbc_v2_dpo_fallback_policy())

    manifest = write_spbc_v2_dpo_bundle_manifest(
        output_path,
        {
            "created_at_utc": _utc_now(),
            "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
            "controller_alias": SPBC_V2_DPO_CONTROLLER_ALIAS,
            "controller_display_name": SPBC_V2_DPO_CONTROLLER_DISPLAY_NAME,
            "source_checkpoint": str(checkpoint_file),
            "source_checkpoint_sha256": source_sha256,
            "source_training_report": str(training_report_path or _default_training_report(checkpoint_file)),
            "source_best_epoch": checkpoint.get("best_epoch"),
            "source_safety_gate_enabled": bool(checkpoint.get("safety_gate_enabled")),
            "model_key": SPBC_V2_DPO_MODEL_KEY,
            "model_family": "Safe Preference Behavioral Cloning ABR v2 DPO",
            "training_method": "behavior_cloning_plus_dpo_safe_rank",
            "reward_version": REWARD_VERSION,
            "action_space": "representation_index",
            "offline_inference_only": True,
            "export_bundle_created": True,
            "qoe_improvement_claimed": False,
            "sota_claimed": False,
            "real_world_generalization_claimed": False,
            "benchmark_performed": False,
            "outputs_are_benchmark_results": False,
            "ranking_performed": False,
            "no_final_ranking": True,
        },
    )
    report = {
        "schema_id": "phase45_v2_spbc_dpo_export_bundle_report_v1",
        "human_readable_name": "Export del bundle de inferencia SPBC ABR v2 DPO",
        "status": "PASS",
        "decision": "SPBC_V2_DPO_BUNDLE_WRITTEN_VALIDATE_NEXT",
        "bundle_dir": str(output_path),
        "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
        "source_checkpoint": str(checkpoint_file),
        "source_checkpoint_sha256": source_sha256,
        "manifest": str(output_path / SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME),
        "required_files": list(SPBC_V2_DPO_BUNDLE_REQUIRED_FILES),
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "export_bundle_created": True,
        "phase6_formal_evaluation_performed": False,
    }
    write_json(output_path / SPBC_V2_DPO_BUNDLE_EXPORT_REPORT_FILENAME, report)
    # {**a, **b} en vez de "a | b" por compatibilidad con Python 3.8 (Ubuntu cliente).
    return {**report, "manifest_payload": manifest}


def validate_spbc_v2_dpo_bundle_dir(bundle_dir: object, verify_hashes: bool = True) -> Mapping[str, object]:
    bundle_path = _ensure_existing_dir_outside_repo(bundle_dir, "spbc_abr_v2_dpo inference bundle")
    missing = [filename for filename in SPBC_V2_DPO_BUNDLE_REQUIRED_FILES if not (bundle_path / filename).is_file()]
    if missing:
        raise SpbcV2DpoBundleError("missing bundle file(s): {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME)
    if manifest.get("schema_id") != SPBC_V2_DPO_BUNDLE_SCHEMA_ID:
        raise SpbcV2DpoBundleError("bundle manifest schema_id is invalid")
    if manifest.get("model_key") != SPBC_V2_DPO_MODEL_KEY:
        raise SpbcV2DpoBundleError("bundle manifest model_key is invalid")
    if manifest.get("controller_key") != SPBC_V2_DPO_CONTROLLER_KEY:
        raise SpbcV2DpoBundleError("bundle manifest controller_key is invalid")
    for flag in ("benchmark_performed", "outputs_are_benchmark_results", "ranking_performed"):
        if manifest.get(flag) is not False:
            raise SpbcV2DpoBundleError("{0} must be false".format(flag))
    if manifest.get("no_final_ranking") is not True:
        raise SpbcV2DpoBundleError("no_final_ranking must be true")

    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise SpbcV2DpoBundleError("bundle manifest files must be a mapping")
    records = {}
    mismatches = []
    for filename in SPBC_V2_DPO_BUNDLE_HASHED_FILES:
        expected = files.get(filename)
        if not isinstance(expected, Mapping):
            raise SpbcV2DpoBundleError("bundle manifest missing file record for {0}".format(filename))
        actual = bundle_file_record(bundle_path / filename, filename)
        records[filename] = actual
        if int(expected.get("size_bytes", 0) or 0) != int(actual["size_bytes"]):
            mismatches.append("{0}: size mismatch".format(filename))
        if verify_hashes and str(expected.get("sha256", "")) != str(actual["sha256"]):
            mismatches.append("{0}: sha256 mismatch".format(filename))
    if mismatches:
        raise SpbcV2DpoBundleError("; ".join(mismatches))
    return {
        "status": "PASS",
        "bundle_dir": str(bundle_path),
        "manifest": dict(manifest),
        "required_files": list(SPBC_V2_DPO_BUNDLE_REQUIRED_FILES),
        "file_records": records,
        "hashes_valid": True,
    }


def write_spbc_v2_dpo_bundle_manifest(bundle_dir: object, metadata: Mapping[str, object]) -> Mapping[str, object]:
    bundle_path = _ensure_existing_dir_outside_repo(bundle_dir, "spbc_abr_v2_dpo inference bundle")
    files = {
        filename: bundle_file_record(bundle_path / filename, filename)
        for filename in SPBC_V2_DPO_BUNDLE_HASHED_FILES
    }
    manifest = dict(metadata)
    manifest.update(
        {
            "schema_id": SPBC_V2_DPO_BUNDLE_SCHEMA_ID,
            "human_readable_name": "Bundle local para inferencia de SPBC ABR v2 DPO",
            "required_files": list(SPBC_V2_DPO_BUNDLE_REQUIRED_FILES),
            "hash_policy": "sha256 de todos los archivos del bundle salvo el manifiesto",
            "files": files,
        }
    )
    write_json(bundle_path / SPBC_V2_DPO_BUNDLE_MANIFEST_FILENAME, manifest)
    return manifest


def build_spbc_v2_dpo_feature_schema() -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v2_spbc_dpo_runtime_feature_schema_v1",
        "model_key": SPBC_V2_DPO_MODEL_KEY,
        "context_history_length": DEFAULT_CONTEXT_HISTORY_LENGTH,
        "sequence_features": list(SEQUENCE_FEATURES),
        "scalar_features": list(SCALAR_FEATURES),
        "candidate_features": list(CANDIDATE_FEATURES),
        "runtime_feature_builder": "core.controller.neural_abr_runtime_features.NeuralAbrRuntimeFeatureBuilder",
        "forbidden_runtime_inputs": [
            "trace_id",
            "dataset_id",
            "source_id",
            "split",
            "group_id",
            "leakage_group",
            "future_throughput",
            "oracle_action",
            "reward_n",
            "qoe_gap",
            "rollout_source",
        ],
        "metadata_fields_used": False,
        "future_fields_used_as_inputs": False,
        "oracle_fields_used_as_inputs": False,
    }


def build_spbc_v2_dpo_ladder_schema() -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v2_spbc_dpo_ladder_schema_v1",
        "action_space": "representation_index",
        "representation_index_policy": "indices enteros contiguos desde cero",
        "representation_kbps": list(DEFAULT_REPRESENTATION_KBPS),
        "segment_duration_s": 4.0,
        "segment_size_source": "runtime MPD rate_Bps * fragment_duration_s",
        "runtime_ladder_source": "MPD feedback rates",
    }


def build_spbc_v2_dpo_model_card(
    checkpoint_file: Path,
    source_sha256: str,
    checkpoint: Mapping[str, object],
    training_report: Mapping[str, object],
) -> Mapping[str, object]:
    validation_metrics = _mapping(training_report.get("validation_metrics"))
    return {
        "schema_id": "phase45_v2_spbc_dpo_model_card_v1",
        "human_readable_name": "Tarjeta del modelo SPBC ABR v2 DPO exportado",
        "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
        "model_key": SPBC_V2_DPO_MODEL_KEY,
        "model_family": "Safe Preference Behavioral Cloning ABR v2 DPO",
        "training_method": "behavior_cloning_plus_dpo_safe_rank",
        "reward_version": REWARD_VERSION,
        "device": "cpu",
        "source_checkpoint": str(checkpoint_file),
        "source_checkpoint_sha256": source_sha256,
        "best_epoch": checkpoint.get("best_epoch"),
        "safety_gate_enabled": bool(checkpoint.get("safety_gate_enabled")),
        "model_config": dict(_mapping(checkpoint.get("model_config"))),
        "validation_metrics_summary": {
            "over_aggressive_rate_vs_oracle": validation_metrics.get("over_aggressive_rate_vs_oracle"),
            "under_aggressive_rate_vs_oracle": validation_metrics.get("under_aggressive_rate_vs_oracle"),
            "selected_utility_regret_vs_oracle_mean": validation_metrics.get(
                "selected_utility_regret_vs_oracle_mean"
            ),
            "selected_rebuffer_regret_vs_oracle_mean": validation_metrics.get(
                "selected_rebuffer_regret_vs_oracle_mean"
            ),
        },
        "boundaries": {
            "phase6_formal_evaluation_performed": False,
            "benchmark_performed": False,
            "ranking_performed": False,
            "qoe_improvement_claimed": False,
            "real_world_generalization_claimed": False,
            "controller_receives_only_runtime_feedback": True,
        },
    }


def build_spbc_v2_dpo_inference_contract() -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v2_spbc_dpo_inference_contract_v1",
        "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
        "input_contract": {
            "sequence": "throughput/download-time history built from player feedback",
            "scalars": "buffer, last representation, recent switch and remaining-chunks signals",
            "candidates": "one row per MPD representation candidate",
            "action_mask": "boolean mask by representation_index",
        },
        "output_contract": {
            "action_logits": "finite score per candidate after model mask",
            "selected_representation_index": "valid action under action_mask",
        },
        "hard_rules": [
            "no usar trace_id, dataset_id, split, leakage_group ni metadata como feature",
            "no usar throughput futuro",
            "no usar labels offline, oracle_action, reward_n ni qoe_gap en runtime",
            "no devolver acciones fuera del MPD",
            "aplicar fallback clasico si el bundle, la inferencia o la accion fallan",
        ],
        "cpu_only": True,
        "deterministic_eval_required": True,
        "benchmark_performed": False,
        "ranking_performed": False,
    }


def build_spbc_v2_dpo_fallback_policy() -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v2_spbc_dpo_fallback_policy_v1",
        "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
        "fallback_controller_default": "robust_mpc",
        "fallback_required_when": [
            "bundle ausente o invalido",
            "schema incompatible",
            "fallo de carga del modelo",
            "logits NaN o infinito",
            "accion invalida o enmascarada",
            "latencia fuera de contrato",
        ],
        "safe_fallback_family": "controller clasico ya validado",
    }


def sha256_file(path: object) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bundle_file_record(path: object, filename: str) -> Mapping[str, object]:
    resolved = Path(path)
    if not resolved.is_file():
        raise SpbcV2DpoBundleError("missing bundle file: {0}".format(resolved))
    return {
        "filename": filename,
        "sha256": sha256_file(resolved),
        "size_bytes": resolved.stat().st_size,
    }


def _validate_training_checkpoint(checkpoint: Mapping[str, object]) -> None:
    if checkpoint.get("schema_id") != SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID:
        raise SpbcV2DpoBundleError("checkpoint schema_id is invalid")
    if checkpoint.get("model_key") != SPBC_V2_DPO_MODEL_KEY:
        raise SpbcV2DpoBundleError("checkpoint model_key is invalid")
    if not isinstance(checkpoint.get("model_state_dict"), Mapping):
        raise SpbcV2DpoBundleError("checkpoint missing model_state_dict")
    if not isinstance(checkpoint.get("model_config"), Mapping):
        raise SpbcV2DpoBundleError("checkpoint missing model_config")
    if not isinstance(checkpoint.get("normalization"), Mapping):
        raise SpbcV2DpoBundleError("checkpoint missing normalization")


def _validate_normalization(normalization: Mapping[str, object]) -> None:
    if normalization.get("schema_id") != "phase45_v2_spbc_dpo_normalization_v1":
        raise SpbcV2DpoBundleError("normalization schema_id is invalid")
    if normalization.get("fitted_on_data_role") != "training":
        raise SpbcV2DpoBundleError("normalization must be fitted on training")
    if tuple(normalization.get("sequence_features", SEQUENCE_FEATURES)) != tuple(SEQUENCE_FEATURES):
        raise SpbcV2DpoBundleError("normalization sequence_features mismatch")
    if tuple(normalization.get("scalar_features", SCALAR_FEATURES)) != tuple(SCALAR_FEATURES):
        raise SpbcV2DpoBundleError("normalization scalar_features mismatch")
    if tuple(normalization.get("candidate_features", CANDIDATE_FEATURES)) != tuple(CANDIDATE_FEATURES):
        raise SpbcV2DpoBundleError("normalization candidate_features mismatch")
    _require_width(normalization.get("sequence_mean"), len(SEQUENCE_FEATURES), "sequence_mean")
    _require_width(normalization.get("sequence_std"), len(SEQUENCE_FEATURES), "sequence_std")
    _require_width(normalization.get("scalar_mean"), len(SCALAR_FEATURES), "scalar_mean")
    _require_width(normalization.get("scalar_std"), len(SCALAR_FEATURES), "scalar_std")
    _require_width(normalization.get("candidate_mean"), len(CANDIDATE_FEATURES), "candidate_mean")
    _require_width(normalization.get("candidate_std"), len(CANDIDATE_FEATURES), "candidate_std")


def _require_width(value: object, expected: int, name: str) -> None:
    if not isinstance(value, (list, tuple)) or len(value) != int(expected):
        raise SpbcV2DpoBundleError("{0} width mismatch".format(name))


def _torch_load_checkpoint(path: Path) -> Mapping[str, object]:
    try:
        checkpoint = torch.load(path, map_location="cpu", weights_only=True)
    except TypeError as exc:
        raise SpbcV2DpoBundleError("safe torch.load weights_only is unavailable") from exc
    except Exception as exc:
        raise SpbcV2DpoBundleError("torch.load failed: {0}".format(path)) from exc
    if not isinstance(checkpoint, Mapping):
        raise SpbcV2DpoBundleError("checkpoint must contain a mapping")
    return checkpoint


def _optional_training_report(path: object | None, checkpoint_file: Path) -> Mapping[str, object]:
    report_path = Path(path).expanduser() if path is not None else _default_training_report(checkpoint_file)
    if not report_path.is_file():
        return {}
    report = read_json(report_path)
    return dict(report)


def _default_training_report(checkpoint_file: Path) -> Path:
    return checkpoint_file.parent / SPBC_V2_DPO_TRAINING_REPORT_FILENAME


def _ensure_existing_file_outside_repo(path: object, purpose: str) -> Path:
    resolved = ensure_outside_repo(path, purpose=purpose)
    if not resolved.is_file():
        raise SpbcV2DpoBundleError("{0} does not exist: {1}".format(purpose, resolved))
    return resolved


def _ensure_existing_dir_outside_repo(path: object, purpose: str) -> Path:
    resolved = ensure_outside_repo(path, purpose=purpose)
    if not resolved.is_dir():
        raise SpbcV2DpoBundleError("{0} does not exist: {1}".format(purpose, resolved))
    return resolved


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
