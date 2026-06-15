from __future__ import annotations

import hashlib
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import ensure_outside_repo, prepare_output_dir, read_json, write_json
from core.neural_abr.constants import CONTEXT_VECTOR_NAMES
from core.phase45_v3.constants import MEDIA_PROFILE_ID, REWARD_VERSION, no_benchmark_policy
from core.phase45_v3.neural_mpc_controller import (
    DEFAULT_NEURAL_MPC_HORIZON,
    DEFAULT_NEURAL_MPC_QUANTILES,
    DEFAULT_REBUFFER_WEIGHT,
    DEFAULT_SWITCH_WEIGHT,
    NEURAL_MPC_BLEND_BUFFER_MAX_S,
    NEURAL_MPC_CONTROLLER_KEYS,
    NEURAL_MPC_CONTROLLER_KEY,
    NEURAL_MPC_Q10_BUFFER_MAX_S,
    NEURAL_MPC_Q25_BUFFER_MAX_S,
)
from core.phase45_v3.neural_mpc_evaluation import NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME
from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME,
    THROUGHPUT_QUANTILE_MODEL_FILENAME,
    THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME,
    THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME,
)
from core.phase45_v3.throughput_quantile_model import PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY


NEURAL_MPC_BUNDLE_SCHEMA_ID = "phase45_v3_neural_mpc_experimental_bundle_v1"
NEURAL_MPC_BUNDLE_REPORT_SCHEMA_ID = "phase45_v3_neural_mpc_experimental_bundle_export_report_v1"
NEURAL_MPC_BUNDLE_MANIFEST_FILENAME = "manifiesto_bundle_neural_mpc_phase45_v3.json"
NEURAL_MPC_BUNDLE_MODEL_FILENAME = THROUGHPUT_QUANTILE_MODEL_FILENAME
NEURAL_MPC_BUNDLE_MODEL_CONFIG_FILENAME = THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME
NEURAL_MPC_BUNDLE_NORMALIZATION_FILENAME = THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME
NEURAL_MPC_BUNDLE_MODEL_CARD_FILENAME = "tarjeta_modelo_neural_mpc_phase45_v3.json"
NEURAL_MPC_BUNDLE_INFERENCE_CONTRACT_FILENAME = "contrato_inferencia_neural_mpc_phase45_v3.json"
NEURAL_MPC_BUNDLE_FALLBACK_POLICY_FILENAME = "politica_respaldo_neural_mpc_phase45_v3.json"
NEURAL_MPC_BUNDLE_EXPORT_REPORT_FILENAME = "reporte_export_bundle_neural_mpc_phase45_v3.json"

NEURAL_MPC_BUNDLE_REQUIRED_FILES = (
    NEURAL_MPC_BUNDLE_MANIFEST_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_CONFIG_FILENAME,
    NEURAL_MPC_BUNDLE_NORMALIZATION_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_CARD_FILENAME,
    NEURAL_MPC_BUNDLE_INFERENCE_CONTRACT_FILENAME,
    NEURAL_MPC_BUNDLE_FALLBACK_POLICY_FILENAME,
    NEURAL_MPC_BUNDLE_EXPORT_REPORT_FILENAME,
)
NEURAL_MPC_BUNDLE_HASHED_FILES = tuple(
    filename
    for filename in NEURAL_MPC_BUNDLE_REQUIRED_FILES
    if filename != NEURAL_MPC_BUNDLE_MANIFEST_FILENAME
)


class Phase45V3NeuralMpcBundleError(ValueError):
    """Raised when a Phase45 v3 Neural-MPC experimental bundle is invalid."""


def export_phase45_v3_neural_mpc_experimental_bundle(
    *,
    model_root: object,
    run_root: object,
    output_dir: object,
    canonical_seed: str = "451001",
    seeds: Sequence[str] = ("451001", "451002", "451003"),
    controller_key: str = NEURAL_MPC_CONTROLLER_KEY,
    candidate_key: str | None = None,
    overwrite: bool = False,
) -> Mapping[str, object]:
    clean_controller_key = _validate_controller_key(controller_key)
    clean_candidate_key = str(candidate_key or clean_controller_key)
    model_root_path = _ensure_existing_dir_outside_repo(model_root, "phase45_v3 neural mpc model root")
    run_root_path = _ensure_existing_dir_outside_repo(run_root, "phase45_v3 neural mpc run root")
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 neural mpc experimental bundle")

    readiness = collect_neural_mpc_candidate_readiness(
        model_root=model_root_path,
        run_root=run_root_path,
        canonical_seed=canonical_seed,
        seeds=seeds,
        candidate_key=clean_candidate_key,
    )
    if readiness["status"] != "READY":
        raise Phase45V3NeuralMpcBundleError("candidate readiness is not READY; do not export bundle")

    canonical = _canonical_seed_record(readiness)
    canonical_seed_value = str(canonical["seed"])
    canonical_model_dir = model_root_path / f"seed_{canonical_seed_value}"
    source_checkpoint = canonical_model_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME
    source_config = canonical_model_dir / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME
    source_normalization = canonical_model_dir / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME
    _require_file(source_checkpoint, "canonical checkpoint")
    _require_file(source_config, "canonical model config")
    _require_file(source_normalization, "canonical normalization")
    actual_checkpoint_sha256 = sha256_file(source_checkpoint)
    reported_checkpoint_sha256 = str(canonical["model_sha256"])
    if reported_checkpoint_sha256 != actual_checkpoint_sha256:
        raise Phase45V3NeuralMpcBundleError(
            "canonical checkpoint sha256 mismatch: expected {0}, got {1}".format(
                reported_checkpoint_sha256,
                actual_checkpoint_sha256,
            )
        )

    shutil.copy2(source_checkpoint, output_path / NEURAL_MPC_BUNDLE_MODEL_FILENAME)
    shutil.copy2(source_config, output_path / NEURAL_MPC_BUNDLE_MODEL_CONFIG_FILENAME)
    shutil.copy2(source_normalization, output_path / NEURAL_MPC_BUNDLE_NORMALIZATION_FILENAME)

    model_config = read_json(source_config)
    normalization = read_json(source_normalization)
    write_json(
        output_path / NEURAL_MPC_BUNDLE_MODEL_CARD_FILENAME,
        build_neural_mpc_model_card(
            source_checkpoint=source_checkpoint,
            source_checkpoint_sha256=actual_checkpoint_sha256,
            readiness=readiness,
            model_config=model_config,
            normalization=normalization,
            controller_key=clean_controller_key,
        ),
    )
    write_json(output_path / NEURAL_MPC_BUNDLE_INFERENCE_CONTRACT_FILENAME, build_neural_mpc_inference_contract())
    write_json(output_path / NEURAL_MPC_BUNDLE_FALLBACK_POLICY_FILENAME, build_neural_mpc_fallback_policy())

    report = {
        "schema_id": NEURAL_MPC_BUNDLE_REPORT_SCHEMA_ID,
        "status": "PASS",
        "decision": "EXPERIMENTAL_BUNDLE_READY_VALIDATE_IN_UBUNTU_CLIENTE",
        "bundle_dir": str(output_path),
        "manifest": str(output_path / NEURAL_MPC_BUNDLE_MANIFEST_FILENAME),
        "controller_key": clean_controller_key,
        "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
        "canonical_seed": canonical_seed_value,
        "canonical_checkpoint_path": str(source_checkpoint),
        "canonical_model_sha256": actual_checkpoint_sha256,
        "required_files": list(NEURAL_MPC_BUNDLE_REQUIRED_FILES),
        "bundle_created": True,
        "controller_integrated": False,
        "diagnostic_only": True,
        "phase6_formal_evaluation_performed": False,
        "qoe_claims_authorized": False,
        **no_benchmark_policy(),
    }
    write_json(output_path / NEURAL_MPC_BUNDLE_EXPORT_REPORT_FILENAME, report)

    manifest = write_neural_mpc_bundle_manifest(
        output_path,
        {
            "created_at_utc": _utc_now(),
            "phase": "fase_4_5_v3_neural_mpc_v1",
            "candidate_key": clean_candidate_key,
            "controller_key": clean_controller_key,
            "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
            "model_family": "Neural throughput quantile predictor plus explicit MPC",
            "training_method": "future_throughput_quantile_prediction",
            "decision_method": "explicit_mpc_with_qoe_linear_v1",
            "media_profile_id": MEDIA_PROFILE_ID,
            "qoe_formula_version": REWARD_VERSION,
            "canonical_seed": canonical_seed_value,
            "source_checkpoint": str(source_checkpoint),
            "source_checkpoint_sha256": actual_checkpoint_sha256,
            "source_model_root": str(model_root_path),
            "source_run_root": str(run_root_path),
            "readiness": readiness,
            "offline_experimental_bundle": True,
            "runtime_controller_integrated": False,
            "phase6_formal_evaluation_performed": False,
            "qoe_improvement_claimed": False,
            "real_world_generalization_claimed": False,
            **no_benchmark_policy(),
        },
    )

    validate_phase45_v3_neural_mpc_bundle_dir(output_path)
    return report | {"manifest_payload": manifest}


def collect_neural_mpc_candidate_readiness(
    *,
    model_root: object,
    run_root: object,
    canonical_seed: str = "451001",
    seeds: Sequence[str] = ("451001", "451002", "451003"),
    candidate_key: str = NEURAL_MPC_CONTROLLER_KEY,
) -> Mapping[str, object]:
    model_root_path = _ensure_existing_dir_outside_repo(model_root, "phase45_v3 neural mpc model root")
    run_root_path = _ensure_existing_dir_outside_repo(run_root, "phase45_v3 neural mpc run root")
    seed_records = []
    for seed in tuple(str(value).strip() for value in seeds if str(value).strip()):
        model_dir = model_root_path / f"seed_{seed}"
        run_dir = run_root_path / f"seed_{seed}"
        training_path = model_dir / THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME
        evaluation_path = run_dir / NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME
        checkpoint_path = model_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME
        training_report = read_json(training_path) if training_path.is_file() else {}
        evaluation_report = read_json(evaluation_path) if evaluation_path.is_file() else {}
        metrics = _mapping(evaluation_report.get("metrics")).get("neural_mpc", {})
        metrics = _mapping(metrics)
        seed_records.append(
            {
                "seed": seed,
                "training_report": str(training_path),
                "training_status": training_report.get("status"),
                "evaluation_report": str(evaluation_path),
                "evaluation_status": evaluation_report.get("status"),
                "failed_gates": _failed_gates(evaluation_report),
                "checkpoint_path": str(checkpoint_path),
                "checkpoint_exists": checkpoint_path.is_file(),
                "model_sha256": training_report.get("model_sha256") or _optional_sha256(checkpoint_path),
                "window_count": evaluation_report.get("window_count"),
                "session_count": evaluation_report.get("session_count"),
                "fallback_rate": metrics.get("fallback_rate"),
                "invalid_action_count": metrics.get("invalid_action_count"),
                "high_capacity_action0_rate": metrics.get("high_capacity_action0_rate"),
                "high_capacity_mean_bitrate_ratio_vs_robust_mpc": metrics.get(
                    "high_capacity_mean_bitrate_ratio_vs_robust_mpc"
                ),
                "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": metrics.get(
                    "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"
                ),
                "qoe_delta_vs_robust_mpc_mean": metrics.get("qoe_delta_vs_robust_mpc_mean"),
            }
        )
    canonical = next((row for row in seed_records if row["seed"] == str(canonical_seed)), None)
    all_passed = bool(seed_records) and all(
        row["training_status"] == "PASS"
        and row["evaluation_status"] == "PASS"
        and bool(row["checkpoint_exists"])
        and not row["failed_gates"]
        for row in seed_records
    )
    canonical_ready = (
        bool(canonical)
        and canonical.get("training_status") == "PASS"
        and canonical.get("evaluation_status") == "PASS"
        and bool(canonical.get("checkpoint_exists"))
        and not canonical.get("failed_gates")
    )
    return {
        "schema_id": "phase45_v3_neural_mpc_experimental_candidate_readiness_v1",
        "generated_at_utc": _utc_now(),
        "candidate_key": str(candidate_key),
        "candidate_stage": "experimental_bundle_input_readiness",
        "status": "READY" if all_passed and canonical_ready else "REVIEW",
        "model_root": str(model_root_path),
        "run_root": str(run_root_path),
        "canonical_seed": str(canonical_seed),
        "canonical_checkpoint_path": canonical.get("checkpoint_path") if canonical else None,
        "canonical_model_sha256": canonical.get("model_sha256") if canonical else None,
        "all_seed_reports_passed": bool(all_passed),
        "canonical_ready": bool(canonical_ready),
        "seed_count": len(seed_records),
        "seeds": seed_records,
        "bundle_created": False,
        "controller_integrated": False,
        "diagnostic_only": True,
        "qoe_claims_authorized": False,
        **no_benchmark_policy(),
    }


def validate_phase45_v3_neural_mpc_bundle_dir(
    bundle_dir: object,
    *,
    verify_hashes: bool = True,
) -> Mapping[str, object]:
    bundle_path = _ensure_existing_dir_outside_repo(bundle_dir, "phase45_v3 neural mpc experimental bundle")
    missing = [filename for filename in NEURAL_MPC_BUNDLE_REQUIRED_FILES if not (bundle_path / filename).is_file()]
    if missing:
        raise Phase45V3NeuralMpcBundleError("missing bundle file(s): {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / NEURAL_MPC_BUNDLE_MANIFEST_FILENAME)
    if manifest.get("schema_id") != NEURAL_MPC_BUNDLE_SCHEMA_ID:
        raise Phase45V3NeuralMpcBundleError("bundle manifest schema_id is invalid")
    if manifest.get("controller_key") not in NEURAL_MPC_CONTROLLER_KEYS:
        raise Phase45V3NeuralMpcBundleError("bundle manifest controller_key is invalid")
    if manifest.get("model_key") != PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY:
        raise Phase45V3NeuralMpcBundleError("bundle manifest model_key is invalid")
    if manifest.get("runtime_controller_integrated") is not False:
        raise Phase45V3NeuralMpcBundleError("runtime_controller_integrated must be false")
    for flag in ("benchmark_performed", "outputs_are_benchmark_results", "ranking_performed"):
        if manifest.get(flag) is not False:
            raise Phase45V3NeuralMpcBundleError("{0} must be false".format(flag))
    if manifest.get("no_final_ranking") is not True:
        raise Phase45V3NeuralMpcBundleError("no_final_ranking must be true")

    files = _mapping(manifest.get("files"))
    records = {}
    mismatches = []
    for filename in NEURAL_MPC_BUNDLE_HASHED_FILES:
        expected = _mapping(files.get(filename))
        if not expected:
            raise Phase45V3NeuralMpcBundleError("bundle manifest missing file record for {0}".format(filename))
        actual = bundle_file_record(bundle_path / filename, filename)
        records[filename] = actual
        if int(expected.get("size_bytes", 0) or 0) != int(actual["size_bytes"]):
            mismatches.append("{0}: size mismatch".format(filename))
        if verify_hashes and str(expected.get("sha256", "")) != str(actual["sha256"]):
            mismatches.append("{0}: sha256 mismatch".format(filename))
    if mismatches:
        raise Phase45V3NeuralMpcBundleError("; ".join(mismatches))
    return {
        "status": "PASS",
        "bundle_dir": str(bundle_path),
        "manifest": dict(manifest),
        "required_files": list(NEURAL_MPC_BUNDLE_REQUIRED_FILES),
        "file_records": records,
        "hashes_valid": True,
    }


def write_neural_mpc_bundle_manifest(bundle_dir: object, metadata: Mapping[str, object]) -> Mapping[str, object]:
    bundle_path = _ensure_existing_dir_outside_repo(bundle_dir, "phase45_v3 neural mpc experimental bundle")
    files = {
        filename: bundle_file_record(bundle_path / filename, filename)
        for filename in NEURAL_MPC_BUNDLE_HASHED_FILES
        if (bundle_path / filename).is_file()
    }
    manifest = dict(metadata)
    manifest.update(
        {
            "schema_id": NEURAL_MPC_BUNDLE_SCHEMA_ID,
            "human_readable_name": "Bundle experimental Neural Throughput-Calibrated MPC Phase45 v3",
            "required_files": list(NEURAL_MPC_BUNDLE_REQUIRED_FILES),
            "hash_policy": "sha256 de todos los archivos del bundle salvo el manifiesto",
            "files": files,
        }
    )
    write_json(bundle_path / NEURAL_MPC_BUNDLE_MANIFEST_FILENAME, manifest)
    return manifest


def build_neural_mpc_model_card(
    *,
    source_checkpoint: object,
    source_checkpoint_sha256: str,
    readiness: Mapping[str, object],
    model_config: Mapping[str, object],
    normalization: Mapping[str, object],
    controller_key: str = NEURAL_MPC_CONTROLLER_KEY,
) -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v3_neural_mpc_model_card_v1",
        "human_readable_name": "Tarjeta del modelo Neural Throughput-Calibrated MPC Phase45 v3",
        "controller_key": _validate_controller_key(controller_key),
        "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
        "model_family": "MLP predictor de cuantiles de throughput futuro mas MPC explicito",
        "source_checkpoint": str(source_checkpoint),
        "source_checkpoint_sha256": str(source_checkpoint_sha256),
        "model_config": dict(model_config),
        "normalization_schema_id": normalization.get("schema_id"),
        "context_feature_names": list(normalization.get("context_feature_names", CONTEXT_VECTOR_NAMES)),
        "training_target": {
            "target": "future throughput log-ratio by horizon",
            "horizon_segments": int(model_config.get("horizon_segments", DEFAULT_NEURAL_MPC_HORIZON)),
            "quantiles": list(model_config.get("quantiles", DEFAULT_NEURAL_MPC_QUANTILES)),
            "future_used_only_as_offline_target": True,
        },
        "diagnostic_evidence": {
            "readiness_status": readiness.get("status"),
            "seed_count": readiness.get("seed_count"),
            "canonical_seed": readiness.get("canonical_seed"),
            "seeds": readiness.get("seeds"),
        },
        "boundaries": {
            "experimental_bundle_created": True,
            "controller_integrated": False,
            "phase6_formal_evaluation_performed": False,
            "benchmark_performed": False,
            "ranking_performed": False,
            "qoe_improvement_claimed": False,
            "real_world_generalization_claimed": False,
            "controller_receives_only_runtime_visible_features": True,
        },
    }


def build_neural_mpc_inference_contract() -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v3_neural_mpc_inference_contract_v1",
        "controller_key": NEURAL_MPC_CONTROLLER_KEY,
        "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
        "input_contract": {
            "context": "features built from runtime-visible ABR state, throughput history, buffer and ladder feedback",
            "forbidden_inputs": [
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
        },
        "prediction_contract": {
            "output": "future throughput log-ratio quantiles",
            "shape": "horizon_segments x quantiles",
            "monotonic_quantile_postprocess_required": True,
            "horizon_segments": DEFAULT_NEURAL_MPC_HORIZON,
            "quantiles": list(DEFAULT_NEURAL_MPC_QUANTILES),
        },
        "planner_contract": {
            "method": "enumerative MPC over valid representation indices",
            "reward": "qoe_linear_v1 = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps",
            "rebuffer_weight": DEFAULT_REBUFFER_WEIGHT,
            "switch_weight": DEFAULT_SWITCH_WEIGHT,
            "buffer_quantile_policy": {
                "buffer_lt_4s": "q10",
                "buffer_4_to_12s": "q25",
                "buffer_12_to_20s": "blend_q25_q50",
                "buffer_gte_20s": "q50",
                "thresholds_s": [
                    NEURAL_MPC_Q10_BUFFER_MAX_S,
                    NEURAL_MPC_Q25_BUFFER_MAX_S,
                    NEURAL_MPC_BLEND_BUFFER_MAX_S,
                ],
            },
        },
        "output_contract": {
            "selected_representation_index": "valid integer action under runtime action_mask",
            "telemetry": "chosen_quantile, throughput_plan_bps, best_sequence, fallback_used, fallback_reason",
        },
        "hard_rules": [
            "no usar throughput futuro como input",
            "no usar metadatos de dataset o split como input",
            "no devolver acciones fuera del MPD",
            "aplicar fallback clasico si bundle, prediccion, MPC o accion fallan",
            "no declarar benchmark ni mejora QoE desde diagnosticos",
        ],
        "cpu_inference_supported": True,
        "deterministic_eval_required": True,
        **no_benchmark_policy(),
    }


def build_neural_mpc_fallback_policy() -> Mapping[str, object]:
    return {
        "schema_id": "phase45_v3_neural_mpc_fallback_policy_v1",
        "controller_key": NEURAL_MPC_CONTROLLER_KEY,
        "fallback_controller_default": "robust_mpc",
        "fallback_required_when": [
            "bundle ausente o invalido",
            "schema incompatible",
            "fallo de carga del checkpoint",
            "prediccion con NaN, infinito o throughput <= 0",
            "cuantiles no monotonicos despues del postproceso",
            "MPC sin acciones validas",
            "accion fuera de mascara/runtime MPD",
            "latencia fuera del contrato futuro de integracion",
        ],
        "fallback_must_be_telemetry_visible": True,
        "safe_fallback_family": "controller clasico ya validado",
        **no_benchmark_policy(),
    }


def sha256_file(path: object) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bundle_file_record(path: object, filename: str) -> Mapping[str, object]:
    resolved = Path(path)
    _require_file(resolved, "bundle file")
    return {
        "filename": filename,
        "sha256": sha256_file(resolved),
        "size_bytes": resolved.stat().st_size,
    }


def _canonical_seed_record(readiness: Mapping[str, object]) -> Mapping[str, object]:
    canonical_seed = str(readiness.get("canonical_seed"))
    for row in readiness.get("seeds", []):  # type: ignore[union-attr]
        if isinstance(row, Mapping) and str(row.get("seed")) == canonical_seed:
            return row
    raise Phase45V3NeuralMpcBundleError("canonical seed record is missing")


def _failed_gates(report: Mapping[str, object]) -> list[str]:
    gates = _mapping(report.get("gates"))
    failed = gates.get("failed", [])
    return [str(value) for value in failed] if isinstance(failed, list) else []


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _validate_controller_key(value: object) -> str:
    key = str(value).strip()
    if key not in NEURAL_MPC_CONTROLLER_KEYS:
        raise Phase45V3NeuralMpcBundleError("invalid Neural-MPC controller_key: {0}".format(value))
    return key


def _optional_sha256(path: Path) -> str | None:
    return sha256_file(path) if path.is_file() else None


def _require_file(path: Path, purpose: str) -> None:
    if not path.is_file():
        raise Phase45V3NeuralMpcBundleError("{0} does not exist: {1}".format(purpose, path))


def _ensure_existing_dir_outside_repo(path: object, purpose: str) -> Path:
    resolved = ensure_outside_repo(path, purpose=purpose)
    if not resolved.is_dir():
        raise Phase45V3NeuralMpcBundleError("{0} does not exist: {1}".format(purpose, resolved))
    return resolved


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
