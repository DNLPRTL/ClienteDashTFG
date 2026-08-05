"""Bundle de runtime para MPC Prudente v1: predictor MLP + config del planner
(risk_alpha, media_profile_id, pesos), con hashes sha256 verificados al cargar.
"""

from __future__ import annotations

import math
import shutil
import time
from pathlib import Path
from typing import Mapping

import torch

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, write_json
from core.neural_abr.bundle import bundle_file_record, sha256_file
from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME,
    THROUGHPUT_QUANTILE_MODEL_FILENAME,
    THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME,
)
from core.phase45_v3.throughput_quantile_dataset import harmonic_mean_bps
from core.phase45_v3.throughput_quantile_model import (
    PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
    ThroughputQuantilePredictor,
)

SCHEMA_ID_BUNDLE = "mpc_prudente_runtime_bundle_v1"

FICHERO_MODELO_BUNDLE = "modelo_throughput_quantile.pt"
FICHERO_CONFIG_MODELO_BUNDLE = "model_config.json"
FICHERO_NORMALIZACION_BUNDLE = "normalization.json"
FICHERO_CONFIG_PLANNER_BUNDLE = "planner_config.json"
FICHERO_MANIFIESTO_BUNDLE = "manifest.json"

FICHEROS_BUNDLE_REQUERIDOS = (
    FICHERO_MANIFIESTO_BUNDLE,
    FICHERO_MODELO_BUNDLE,
    FICHERO_CONFIG_MODELO_BUNDLE,
    FICHERO_NORMALIZACION_BUNDLE,
    FICHERO_CONFIG_PLANNER_BUNDLE,
)
FICHEROS_BUNDLE_CON_HASH = tuple(f for f in FICHEROS_BUNDLE_REQUERIDOS if f != FICHERO_MANIFIESTO_BUNDLE)

RISK_ALPHA_POR_DEFECTO = 0.75
PESO_REBUFFER_POR_DEFECTO = 4.3
PESO_SUAVIDAD_POR_DEFECTO = 1.0


class ErrorBundleMpcPrudente(ValueError):
    """Error al validar o cargar el bundle runtime."""


def verificar_ficheros_del_manifiesto(
    bundle_path: Path,
    files: Mapping,
    hashed_files,
    *,
    verify_hashes: bool,
) -> None:
    """Comprueba tamaño y sha256 de cada archivo del bundle contra su manifiesto."""
    mismatches = []
    for filename in hashed_files:
        record = files.get(filename)
        if not isinstance(record, Mapping):
            raise ErrorBundleMpcPrudente("el manifiesto no tiene registro del fichero {0}".format(filename))
        actual = bundle_file_record(bundle_path / filename, filename)
        if int(record.get("size_bytes", 0) or 0) != actual["size_bytes"]:
            mismatches.append("{0}: size mismatch".format(filename))
        if verify_hashes and str(record.get("sha256", "")) != actual["sha256"]:
            mismatches.append("{0}: sha256 mismatch".format(filename))
    if mismatches:
        raise ErrorBundleMpcPrudente("; ".join(mismatches))


def filas_log_ratio_a_bps(matrix, base_tp_bps: float, horizon: int, quantile_count: int):
    """Convierte la salida del modelo (log-ratio sobre la media armónica) a bps.

    Recorta el ratio a [0.15, 4.0] para que una predicción disparatada no pueda
    arrastrar al planner, y ordena cada fila por seguridad (monotonía).
    """
    base = float(base_tp_bps)
    rows = []
    for h in range(int(horizon)):
        row = []
        for q in range(int(quantile_count)):
            value = float(matrix[h, q])
            if not math.isfinite(value):
                raise ErrorBundleMpcPrudente("prediccion de throughput no finita")
            clipped = max(min(value, math.log(4.0)), math.log(0.15))
            predicted = base * math.exp(clipped)
            row.append(min(max(predicted, 0.15 * base), 4.0 * base))
        rows.append(tuple(sorted(row)))
    return tuple(rows)


def exportar_bundle_mpc_prudente(
    training_output_dir: object,
    bundle_dir: object,
    *,
    media_profile_id: str,
    risk_alpha: float = RISK_ALPHA_POR_DEFECTO,
    rebuffer_weight: float = PESO_REBUFFER_POR_DEFECTO,
    switch_weight: float = PESO_SUAVIDAD_POR_DEFECTO,
    overwrite: bool = False,
) -> Mapping[str, object]:
    train_dir = ensure_existing_dir(training_output_dir, purpose="salida de entrenamiento mpc_prudente")
    bundle_path = prepare_output_dir(bundle_dir, overwrite=overwrite, purpose="bundle runtime mpc_prudente")

    shutil.copy(train_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME, bundle_path / FICHERO_MODELO_BUNDLE)
    model_config = dict(read_json(train_dir / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME))
    normalization = dict(read_json(train_dir / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME))
    write_json(bundle_path / FICHERO_CONFIG_MODELO_BUNDLE, model_config)
    write_json(bundle_path / FICHERO_NORMALIZACION_BUNDLE, normalization)

    if not 0.0 < float(risk_alpha) <= 1.0:
        raise ErrorBundleMpcPrudente("risk_alpha debe estar en (0, 1]")
    planner_config = {
        "schema_id": "mpc_prudente_planner_config_v1",
        "risk_alpha": float(risk_alpha),
        "media_profile_id": str(media_profile_id),
        "rebuffer_weight": float(rebuffer_weight),
        "switch_weight": float(switch_weight),
        "quantiles": [float(q) for q in model_config["quantiles"]],
        "horizon_segments": int(model_config["horizon_segments"]),
        "segment_size_source": "real_vbr_from_server",
        "planner": "cvar_lower_tail",
    }
    write_json(bundle_path / FICHERO_CONFIG_PLANNER_BUNDLE, planner_config)

    files = {f: bundle_file_record(bundle_path / f, f) for f in FICHEROS_BUNDLE_CON_HASH}
    manifest = {
        "schema_id": SCHEMA_ID_BUNDLE,
        "human_readable_name": "Bundle runtime MPC Neuronal Prudente",
        "media_profile_id": str(media_profile_id),
        "risk_alpha": float(risk_alpha),
        "required_files": list(FICHEROS_BUNDLE_REQUERIDOS),
        "hash_policy": "sha256 de todos los archivos salvo el manifiesto",
        "files": files,
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
    }
    write_json(bundle_path / FICHERO_MANIFIESTO_BUNDLE, manifest)
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": manifest}


def validar_dir_bundle_mpc_prudente(bundle_dir: object, *, verify_hashes: bool = True) -> Mapping[str, object]:
    bundle_path = ensure_existing_dir(bundle_dir, purpose="bundle runtime mpc_prudente")
    missing = [f for f in FICHEROS_BUNDLE_REQUERIDOS if not (bundle_path / f).is_file()]
    if missing:
        raise ErrorBundleMpcPrudente("faltan ficheros del bundle: {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / FICHERO_MANIFIESTO_BUNDLE)
    if manifest.get("schema_id") != SCHEMA_ID_BUNDLE:
        raise ErrorBundleMpcPrudente("schema_id del manifiesto del bundle invalido")
    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise ErrorBundleMpcPrudente("el campo files del manifiesto del bundle debe ser un mapping")
    verificar_ficheros_del_manifiesto(bundle_path, files, FICHEROS_BUNDLE_CON_HASH, verify_hashes=verify_hashes)
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": dict(manifest)}


class BundleRuntimeMpcPrudente:
    """Predictor + config del planner cargados para runtime (weights_only)."""

    def __init__(self, bundle_dir: object, *, verify_hashes: bool = True) -> None:
        validation = validar_dir_bundle_mpc_prudente(bundle_dir, verify_hashes=verify_hashes)
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.model_config = dict(read_json(self.bundle_dir / FICHERO_CONFIG_MODELO_BUNDLE))
        self.normalization = dict(read_json(self.bundle_dir / FICHERO_NORMALIZACION_BUNDLE))
        self.planner_config = dict(read_json(self.bundle_dir / FICHERO_CONFIG_PLANNER_BUNDLE))
        self.quantiles = tuple(float(q) for q in self.model_config["quantiles"])
        self.horizon_segments = int(self.model_config["horizon_segments"])
        self.risk_alpha = float(self.planner_config.get("risk_alpha", RISK_ALPHA_POR_DEFECTO))
        self.media_profile_id = str(self.planner_config.get("media_profile_id", ""))
        self.rebuffer_weight = float(self.planner_config.get("rebuffer_weight", PESO_REBUFFER_POR_DEFECTO))
        self.switch_weight = float(self.planner_config.get("switch_weight", PESO_SUAVIDAD_POR_DEFECTO))
        self.context_mean = tuple(float(v) for v in self.normalization["context_mean"])
        self.context_std = tuple(float(v) for v in self.normalization["context_std"])
        self.model = self._cargar_modelo()
        self.model.eval()
        self.last_latency_ms = 0.0

    def _cargar_modelo(self) -> ThroughputQuantilePredictor:
        try:
            checkpoint = torch.load(self.bundle_dir / FICHERO_MODELO_BUNDLE, map_location="cpu", weights_only=True)
        except Exception as exc:  # noqa: BLE001
            raise ErrorBundleMpcPrudente("torch.load (weights_only) fallo: {0}".format(exc)) from exc
        if not isinstance(checkpoint, Mapping) or checkpoint.get("model_key") != PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY:
            raise ErrorBundleMpcPrudente("model_key del checkpoint invalido")
        model = ThroughputQuantilePredictor(
            input_dim=int(self.model_config["input_dim"]),
            horizon_segments=self.horizon_segments,
            quantiles=self.quantiles,
            hidden_sizes=tuple(int(v) for v in self.model_config["hidden_sizes"]),
        )
        model.load_state_dict(checkpoint["model_state_dict"])
        return model

    def predecir(self, state, ladder) -> tuple[tuple[float, ...], ...]:
        from core.neural_abr.features import build_context_features, flatten_context_features

        context = flatten_context_features(build_context_features(state, ladder))
        if len(context) != len(self.context_mean):
            raise ErrorBundleMpcPrudente("la anchura del contexto no coincide con la normalizacion")
        normalized = [
            (float(v) - float(self.context_mean[i])) / max(float(self.context_std[i]), 1.0e-9)
            for i, v in enumerate(context)
        ]
        started = time.perf_counter()
        with torch.no_grad():
            log_ratio = self.model(torch.tensor([normalized], dtype=torch.float32)).detach().cpu()[0]
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        base_tp = harmonic_mean_bps(state.throughput_history_bps)
        return filas_log_ratio_a_bps(log_ratio, base_tp, self.horizon_segments, len(self.quantiles))
