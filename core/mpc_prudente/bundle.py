"""Bundle de runtime para MPC Prudente: predictor + config del planner.

El predictor es el mismo `ThroughputQuantilePredictor` entrenado; el bundle añade
la configuración del planner prudente (`risk_alpha`, `media_profile_id`, pesos) y
los hashes sha256 para verificación en runtime. El controller runtime lo carga,
reconstruye la `MediaFaithfulLadder` del medio (tamaños reales VBR) y planifica con
`plan_prudent_action`.
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

MPC_PRUDENTE_BUNDLE_SCHEMA_ID = "mpc_prudente_runtime_bundle_v1"

BUNDLE_MODEL_FILENAME = "modelo_throughput_quantile.pt"
BUNDLE_MODEL_CONFIG_FILENAME = "model_config.json"
BUNDLE_NORMALIZATION_FILENAME = "normalization.json"
BUNDLE_PLANNER_CONFIG_FILENAME = "planner_config.json"
BUNDLE_MANIFEST_FILENAME = "manifest.json"

REQUIRED_BUNDLE_FILES = (
    BUNDLE_MANIFEST_FILENAME,
    BUNDLE_MODEL_FILENAME,
    BUNDLE_MODEL_CONFIG_FILENAME,
    BUNDLE_NORMALIZATION_FILENAME,
    BUNDLE_PLANNER_CONFIG_FILENAME,
)
HASHED_BUNDLE_FILES = tuple(f for f in REQUIRED_BUNDLE_FILES if f != BUNDLE_MANIFEST_FILENAME)

DEFAULT_RISK_ALPHA = 0.75
DEFAULT_REBUFFER_WEIGHT = 4.3
DEFAULT_SWITCH_WEIGHT = 1.0


class MpcPrudenteBundleError(ValueError):
    """Raised when the prudent runtime bundle is invalid."""


def export_mpc_prudente_bundle(
    training_output_dir: object,
    bundle_dir: object,
    *,
    media_profile_id: str,
    risk_alpha: float = DEFAULT_RISK_ALPHA,
    rebuffer_weight: float = DEFAULT_REBUFFER_WEIGHT,
    switch_weight: float = DEFAULT_SWITCH_WEIGHT,
    overwrite: bool = False,
) -> Mapping[str, object]:
    train_dir = ensure_existing_dir(training_output_dir, purpose="mpc_prudente training output")
    bundle_path = prepare_output_dir(bundle_dir, overwrite=overwrite, purpose="mpc_prudente runtime bundle")

    shutil.copy(train_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME, bundle_path / BUNDLE_MODEL_FILENAME)
    model_config = dict(read_json(train_dir / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME))
    normalization = dict(read_json(train_dir / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME))
    write_json(bundle_path / BUNDLE_MODEL_CONFIG_FILENAME, model_config)
    write_json(bundle_path / BUNDLE_NORMALIZATION_FILENAME, normalization)

    if not 0.0 < float(risk_alpha) <= 1.0:
        raise MpcPrudenteBundleError("risk_alpha must be in (0, 1]")
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
    write_json(bundle_path / BUNDLE_PLANNER_CONFIG_FILENAME, planner_config)

    files = {f: bundle_file_record(bundle_path / f, f) for f in HASHED_BUNDLE_FILES}
    manifest = {
        "schema_id": MPC_PRUDENTE_BUNDLE_SCHEMA_ID,
        "human_readable_name": "Bundle runtime MPC Neuronal Prudente",
        "media_profile_id": str(media_profile_id),
        "risk_alpha": float(risk_alpha),
        "required_files": list(REQUIRED_BUNDLE_FILES),
        "hash_policy": "sha256 de todos los archivos salvo el manifiesto",
        "files": files,
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
    }
    write_json(bundle_path / BUNDLE_MANIFEST_FILENAME, manifest)
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": manifest}


def validate_mpc_prudente_bundle_dir(bundle_dir: object, *, verify_hashes: bool = True) -> Mapping[str, object]:
    bundle_path = ensure_existing_dir(bundle_dir, purpose="mpc_prudente runtime bundle")
    missing = [f for f in REQUIRED_BUNDLE_FILES if not (bundle_path / f).is_file()]
    if missing:
        raise MpcPrudenteBundleError("missing bundle file(s): {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / BUNDLE_MANIFEST_FILENAME)
    if manifest.get("schema_id") != MPC_PRUDENTE_BUNDLE_SCHEMA_ID:
        raise MpcPrudenteBundleError("bundle manifest schema_id is invalid")
    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise MpcPrudenteBundleError("bundle manifest files must be a mapping")
    mismatches = []
    for filename in HASHED_BUNDLE_FILES:
        record = files.get(filename)
        if not isinstance(record, Mapping):
            raise MpcPrudenteBundleError("manifest missing file record for {0}".format(filename))
        actual = bundle_file_record(bundle_path / filename, filename)
        if int(record.get("size_bytes", 0) or 0) != actual["size_bytes"]:
            mismatches.append("{0}: size mismatch".format(filename))
        if verify_hashes and str(record.get("sha256", "")) != actual["sha256"]:
            mismatches.append("{0}: sha256 mismatch".format(filename))
    if mismatches:
        raise MpcPrudenteBundleError("; ".join(mismatches))
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": dict(manifest)}


class MpcPrudenteRuntimeBundle:
    """Predictor + config del planner cargados para runtime (weights_only)."""

    def __init__(self, bundle_dir: object, *, verify_hashes: bool = True) -> None:
        validation = validate_mpc_prudente_bundle_dir(bundle_dir, verify_hashes=verify_hashes)
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.model_config = dict(read_json(self.bundle_dir / BUNDLE_MODEL_CONFIG_FILENAME))
        self.normalization = dict(read_json(self.bundle_dir / BUNDLE_NORMALIZATION_FILENAME))
        self.planner_config = dict(read_json(self.bundle_dir / BUNDLE_PLANNER_CONFIG_FILENAME))
        self.quantiles = tuple(float(q) for q in self.model_config["quantiles"])
        self.horizon_segments = int(self.model_config["horizon_segments"])
        self.risk_alpha = float(self.planner_config.get("risk_alpha", DEFAULT_RISK_ALPHA))
        self.media_profile_id = str(self.planner_config.get("media_profile_id", ""))
        self.rebuffer_weight = float(self.planner_config.get("rebuffer_weight", DEFAULT_REBUFFER_WEIGHT))
        self.switch_weight = float(self.planner_config.get("switch_weight", DEFAULT_SWITCH_WEIGHT))
        self.context_mean = tuple(float(v) for v in self.normalization["context_mean"])
        self.context_std = tuple(float(v) for v in self.normalization["context_std"])
        self.model = self._load_model()
        self.model.eval()
        self.last_latency_ms = 0.0

    def _load_model(self) -> ThroughputQuantilePredictor:
        try:
            checkpoint = torch.load(self.bundle_dir / BUNDLE_MODEL_FILENAME, map_location="cpu", weights_only=True)
        except Exception as exc:  # noqa: BLE001
            raise MpcPrudenteBundleError("torch.load (weights_only) failed: {0}".format(exc)) from exc
        if not isinstance(checkpoint, Mapping) or checkpoint.get("model_key") != PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY:
            raise MpcPrudenteBundleError("checkpoint model_key invalid")
        model = ThroughputQuantilePredictor(
            input_dim=int(self.model_config["input_dim"]),
            horizon_segments=self.horizon_segments,
            quantiles=self.quantiles,
            hidden_sizes=tuple(int(v) for v in self.model_config["hidden_sizes"]),
        )
        model.load_state_dict(checkpoint["model_state_dict"])
        return model

    def predict(self, state, ladder) -> tuple[tuple[float, ...], ...]:
        from core.neural_abr.features import build_context_features, flatten_context_features

        context = flatten_context_features(build_context_features(state, ladder))
        if len(context) != len(self.context_mean):
            raise MpcPrudenteBundleError("context normalization width mismatch")
        normalized = [
            (float(v) - float(self.context_mean[i])) / max(float(self.context_std[i]), 1.0e-9)
            for i, v in enumerate(context)
        ]
        started = time.perf_counter()
        with torch.no_grad():
            log_ratio = self.model(torch.tensor([normalized], dtype=torch.float32)).detach().cpu()[0]
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        base_tp = harmonic_mean_bps(state.throughput_history_bps)
        rows = []
        for h in range(self.horizon_segments):
            row = []
            for q in range(len(self.quantiles)):
                value = float(log_ratio[h, q])
                if not math.isfinite(value):
                    raise MpcPrudenteBundleError("non-finite throughput prediction")
                clipped = max(min(value, math.log(4.0)), math.log(0.15))
                predicted = float(base_tp) * math.exp(clipped)
                row.append(min(max(predicted, 0.15 * float(base_tp)), 4.0 * float(base_tp)))
            rows.append(tuple(sorted(row)))
        return tuple(rows)
