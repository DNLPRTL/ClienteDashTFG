"""Bundle de runtime para MPC Prudente v2: ensemble temporal (GRU) + config.

En runtime carga los M miembros y predice con `combinar_cuantiles_ensemble` (media +
ensanchado de la cola inferior según la discrepancia entre miembros).
"""

from __future__ import annotations

import math
import shutil
import time
from pathlib import Path
from typing import Mapping

import torch

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, write_json
from core.neural_abr.bundle import bundle_file_record
from core.mpc_prudente.bundle import (
    FICHERO_MANIFIESTO_BUNDLE,
    FICHERO_CONFIG_PLANNER_BUNDLE,
    PESO_REBUFFER_POR_DEFECTO,
    RISK_ALPHA_POR_DEFECTO,
    PESO_SUAVIDAD_POR_DEFECTO,
    ErrorBundleMpcPrudente,
    filas_log_ratio_a_bps,
    verificar_ficheros_del_manifiesto,
)
from core.mpc_prudente.modelo_temporal import (
    CLAVE_MODELO_TEMPORAL,
    NOMBRES_FEATURES_ESCALARES,
    PredictorTemporalCuantiles,
    combinar_cuantiles_ensemble,
)
from core.mpc_prudente.entrenamiento_temporal import (
    FICHERO_CONFIG_TEMPORAL,
    FICHERO_MODELO_TEMPORAL,
    FICHERO_NORMALIZACION_TEMPORAL,
)
from core.phase45_v3.throughput_quantile_dataset import harmonic_mean_bps

SCHEMA_ID_BUNDLE_TEMPORAL = "mpc_prudente_temporal_runtime_bundle_v1"
DOWNSIDE_WIDEN_POR_DEFECTO = 1.0

FICHEROS_BUNDLE_TEMPORAL_REQUERIDOS = (
    FICHERO_MANIFIESTO_BUNDLE,
    FICHERO_MODELO_TEMPORAL,
    FICHERO_CONFIG_TEMPORAL,
    FICHERO_NORMALIZACION_TEMPORAL,
    FICHERO_CONFIG_PLANNER_BUNDLE,
)
FICHEROS_BUNDLE_TEMPORAL_CON_HASH = tuple(f for f in FICHEROS_BUNDLE_TEMPORAL_REQUERIDOS if f != FICHERO_MANIFIESTO_BUNDLE)


def exportar_bundle_temporal_mpc_prudente(
    training_output_dir: object,
    bundle_dir: object,
    *,
    media_profile_id: str,
    risk_alpha: float = RISK_ALPHA_POR_DEFECTO,
    rebuffer_weight: float = PESO_REBUFFER_POR_DEFECTO,
    switch_weight: float = PESO_SUAVIDAD_POR_DEFECTO,
    downside_widen: float | None = None,
    overwrite: bool = False,
) -> Mapping[str, object]:
    train_dir = ensure_existing_dir(training_output_dir, purpose="salida de entrenamiento temporal mpc_prudente")
    bundle_path = prepare_output_dir(bundle_dir, overwrite=overwrite, purpose="bundle runtime temporal mpc_prudente")

    shutil.copy(train_dir / FICHERO_MODELO_TEMPORAL, bundle_path / FICHERO_MODELO_TEMPORAL)
    model_config = dict(read_json(train_dir / FICHERO_CONFIG_TEMPORAL))
    normalization = dict(read_json(train_dir / FICHERO_NORMALIZACION_TEMPORAL))
    write_json(bundle_path / FICHERO_CONFIG_TEMPORAL, model_config)
    write_json(bundle_path / FICHERO_NORMALIZACION_TEMPORAL, normalization)

    if not 0.0 < float(risk_alpha) <= 1.0:
        raise ErrorBundleMpcPrudente("risk_alpha debe estar en (0, 1]")
    checkpoint = torch.load(bundle_path / FICHERO_MODELO_TEMPORAL, map_location="cpu", weights_only=True)
    widen = float(downside_widen) if downside_widen is not None else float(checkpoint.get("downside_widen", DOWNSIDE_WIDEN_POR_DEFECTO))
    planner_config = {
        "schema_id": "mpc_prudente_planner_config_v1",
        "risk_alpha": float(risk_alpha),
        "media_profile_id": str(media_profile_id),
        "rebuffer_weight": float(rebuffer_weight),
        "switch_weight": float(switch_weight),
        "downside_widen": widen,
        "quantiles": [float(q) for q in model_config["quantiles"]],
        "horizon_segments": int(model_config["horizon_segments"]),
        "segment_size_source": "real_vbr_from_server",
        "planner": "cvar_lower_tail_temporal_ensemble",
    }
    write_json(bundle_path / FICHERO_CONFIG_PLANNER_BUNDLE, planner_config)

    files = {f: bundle_file_record(bundle_path / f, f) for f in FICHEROS_BUNDLE_TEMPORAL_CON_HASH}
    manifest = {
        "schema_id": SCHEMA_ID_BUNDLE_TEMPORAL,
        "human_readable_name": "Bundle runtime MPC Prudente — predictor temporal ensemble",
        "media_profile_id": str(media_profile_id),
        "risk_alpha": float(risk_alpha),
        "downside_widen": widen,
        "ensemble_size": int(checkpoint.get("ensemble_size", 0)),
        "required_files": list(FICHEROS_BUNDLE_TEMPORAL_REQUERIDOS),
        "files": files,
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
    }
    write_json(bundle_path / FICHERO_MANIFIESTO_BUNDLE, manifest)
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": manifest}


def validar_dir_bundle_temporal_mpc_prudente(bundle_dir: object, *, verify_hashes: bool = True) -> Mapping[str, object]:
    bundle_path = ensure_existing_dir(bundle_dir, purpose="bundle runtime temporal mpc_prudente")
    missing = [f for f in FICHEROS_BUNDLE_TEMPORAL_REQUERIDOS if not (bundle_path / f).is_file()]
    if missing:
        raise ErrorBundleMpcPrudente("faltan ficheros del bundle temporal: {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / FICHERO_MANIFIESTO_BUNDLE)
    if manifest.get("schema_id") != SCHEMA_ID_BUNDLE_TEMPORAL:
        raise ErrorBundleMpcPrudente("schema_id del manifiesto del bundle temporal invalido")
    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise ErrorBundleMpcPrudente("el campo files del manifiesto del bundle temporal debe ser un mapping")
    verificar_ficheros_del_manifiesto(bundle_path, files, FICHEROS_BUNDLE_TEMPORAL_CON_HASH, verify_hashes=verify_hashes)
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": dict(manifest)}


def cargar_bundle_runtime_prudente(bundle_dir: object, *, verify_hashes: bool = True):
    """Carga el bundle correcto (MLP o temporal) según el schema_id del manifiesto."""
    from core.mpc_prudente.bundle import BundleRuntimeMpcPrudente

    bundle_path = ensure_existing_dir(bundle_dir, purpose="bundle runtime mpc_prudente")
    manifest_path = bundle_path / FICHERO_MANIFIESTO_BUNDLE
    schema = ""
    if manifest_path.is_file():
        schema = str(read_json(manifest_path).get("schema_id", ""))
    if schema == SCHEMA_ID_BUNDLE_TEMPORAL:
        return BundleRuntimeTemporalMpcPrudente(bundle_dir, verify_hashes=verify_hashes)
    return BundleRuntimeMpcPrudente(bundle_dir, verify_hashes=verify_hashes)


class BundleRuntimeTemporalMpcPrudente:
    """Carga el ensemble temporal y predice cuantiles de throughput (bps)."""

    def __init__(self, bundle_dir: object, *, verify_hashes: bool = True) -> None:
        validation = validar_dir_bundle_temporal_mpc_prudente(bundle_dir, verify_hashes=verify_hashes)
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.model_config = dict(read_json(self.bundle_dir / FICHERO_CONFIG_TEMPORAL))
        self.normalization = dict(read_json(self.bundle_dir / FICHERO_NORMALIZACION_TEMPORAL))
        self.planner_config = dict(read_json(self.bundle_dir / FICHERO_CONFIG_PLANNER_BUNDLE))
        self.quantiles = tuple(float(q) for q in self.model_config["quantiles"])
        self.horizon_segments = int(self.model_config["horizon_segments"])
        self.risk_alpha = float(self.planner_config.get("risk_alpha", RISK_ALPHA_POR_DEFECTO))
        self.media_profile_id = str(self.planner_config.get("media_profile_id", ""))
        self.rebuffer_weight = float(self.planner_config.get("rebuffer_weight", PESO_REBUFFER_POR_DEFECTO))
        self.switch_weight = float(self.planner_config.get("switch_weight", PESO_SUAVIDAD_POR_DEFECTO))
        self.downside_widen = float(self.planner_config.get("downside_widen", DOWNSIDE_WIDEN_POR_DEFECTO))
        self._seq_mean = [float(v) for v in self.normalization["seq_mean"]]
        self._seq_std = [float(v) for v in self.normalization["seq_std"]]
        self._scalar_mean = [float(v) for v in self.normalization["scalar_mean"]]
        self._scalar_std = [float(v) for v in self.normalization["scalar_std"]]
        self.members = self._cargar_miembros()
        self.last_latency_ms = 0.0

    def _cargar_miembros(self):
        try:
            checkpoint = torch.load(self.bundle_dir / FICHERO_MODELO_TEMPORAL, map_location="cpu", weights_only=True)
        except Exception as exc:  # noqa: BLE001
            raise ErrorBundleMpcPrudente("torch.load (weights_only) fallo: {0}".format(exc)) from exc
        if checkpoint.get("model_key") != CLAVE_MODELO_TEMPORAL:
            raise ErrorBundleMpcPrudente("model_key del checkpoint temporal invalido")
        states = checkpoint.get("member_state_dicts")
        if not isinstance(states, (list, tuple)) or not states:
            raise ErrorBundleMpcPrudente("el checkpoint temporal no tiene member_state_dicts")
        members = []
        for state in states:
            model = PredictorTemporalCuantiles(
                seq_features=int(self.model_config["seq_features"]),
                scalar_dim=int(self.model_config["scalar_dim"]),
                horizon_segments=self.horizon_segments,
                quantiles=self.quantiles,
                gru_hidden=int(self.model_config["gru_hidden"]),
                gru_layers=int(self.model_config.get("gru_layers", 1)),
                mlp_hidden=tuple(int(h) for h in self.model_config["mlp_hidden"]),
                dropout=float(self.model_config.get("dropout", 0.0)),
            )
            model.load_state_dict(state)
            model.eval()
            members.append(model)
        return members

    def predecir(self, state, ladder) -> tuple[tuple[float, ...], ...]:
        from core.neural_abr.features import build_context_features

        ctx = build_context_features(state, ladder)
        tp_hist = [float(v) for v in (ctx.get("throughput_history_bps") or [])]
        dt_hist = [float(v) for v in (ctx.get("download_time_history_s") or [])]
        length = min(len(tp_hist), len(dt_hist))
        if length <= 0:
            seq = [[0.0, 0.0]]
        else:
            seq = [[math.log1p(max(tp_hist[i], 0.0)), dt_hist[i]] for i in range(length)]
        seq_norm = [[(step[f] - self._seq_mean[f]) / max(self._seq_std[f], 1.0e-9) for f in range(2)] for step in seq]
        scalar = [float(ctx.get(name, 0.0) or 0.0) for name in NOMBRES_FEATURES_ESCALARES]
        scalar_norm = [
            (scalar[j] - self._scalar_mean[j]) / max(self._scalar_std[j], 1.0e-9) for j in range(len(scalar))
        ]
        seq_t = torch.tensor([seq_norm], dtype=torch.float32)
        scalar_t = torch.tensor([scalar_norm], dtype=torch.float32)
        started = time.perf_counter()
        with torch.no_grad():
            preds = torch.stack([m(seq_t, scalar_t) for m in self.members], dim=0)  # [M,1,H,Q]
            combined = combinar_cuantiles_ensemble(preds, self.quantiles, downside_widen=self.downside_widen)[0]  # [H,Q]
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        base_tp = harmonic_mean_bps(state.throughput_history_bps)
        return filas_log_ratio_a_bps(combined, base_tp, self.horizon_segments, len(self.quantiles))
