"""Bundle de runtime para el predictor TEMPORAL (ensemble GRU) de MPC Prudente.

Empaqueta el ensemble entrenado (`modelo_temporal_ensemble.pt` con los M state
dicts) + config + normalización + config del planner (risk_alpha, media_profile_id,
downside_widen). En runtime carga los M miembros y predice con `ensemble_quantiles`
(media + ensanchado de la cola inferior según la incertidumbre epistémica).
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
    BUNDLE_MANIFEST_FILENAME,
    BUNDLE_PLANNER_CONFIG_FILENAME,
    DEFAULT_REBUFFER_WEIGHT,
    DEFAULT_RISK_ALPHA,
    DEFAULT_SWITCH_WEIGHT,
    MpcPrudenteBundleError,
)
from core.mpc_prudente.temporal_model import (
    MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
    SCALAR_FEATURE_NAMES,
    TemporalQuantilePredictor,
    ensemble_quantiles,
)
from core.mpc_prudente.temporal_training import (
    TEMPORAL_MODEL_CONFIG_FILENAME,
    TEMPORAL_MODEL_FILENAME,
    TEMPORAL_NORMALIZATION_FILENAME,
)
from core.phase45_v3.throughput_quantile_dataset import harmonic_mean_bps

MPC_PRUDENTE_TEMPORAL_BUNDLE_SCHEMA_ID = "mpc_prudente_temporal_runtime_bundle_v1"
DEFAULT_DOWNSIDE_WIDEN = 1.0

REQUIRED_TEMPORAL_BUNDLE_FILES = (
    BUNDLE_MANIFEST_FILENAME,
    TEMPORAL_MODEL_FILENAME,
    TEMPORAL_MODEL_CONFIG_FILENAME,
    TEMPORAL_NORMALIZATION_FILENAME,
    BUNDLE_PLANNER_CONFIG_FILENAME,
)
HASHED_TEMPORAL_BUNDLE_FILES = tuple(f for f in REQUIRED_TEMPORAL_BUNDLE_FILES if f != BUNDLE_MANIFEST_FILENAME)


def export_mpc_prudente_temporal_bundle(
    training_output_dir: object,
    bundle_dir: object,
    *,
    media_profile_id: str,
    risk_alpha: float = DEFAULT_RISK_ALPHA,
    rebuffer_weight: float = DEFAULT_REBUFFER_WEIGHT,
    switch_weight: float = DEFAULT_SWITCH_WEIGHT,
    downside_widen: float | None = None,
    overwrite: bool = False,
) -> Mapping[str, object]:
    train_dir = ensure_existing_dir(training_output_dir, purpose="mpc_prudente temporal training output")
    bundle_path = prepare_output_dir(bundle_dir, overwrite=overwrite, purpose="mpc_prudente temporal runtime bundle")

    shutil.copy(train_dir / TEMPORAL_MODEL_FILENAME, bundle_path / TEMPORAL_MODEL_FILENAME)
    model_config = dict(read_json(train_dir / TEMPORAL_MODEL_CONFIG_FILENAME))
    normalization = dict(read_json(train_dir / TEMPORAL_NORMALIZATION_FILENAME))
    write_json(bundle_path / TEMPORAL_MODEL_CONFIG_FILENAME, model_config)
    write_json(bundle_path / TEMPORAL_NORMALIZATION_FILENAME, normalization)

    if not 0.0 < float(risk_alpha) <= 1.0:
        raise MpcPrudenteBundleError("risk_alpha must be in (0, 1]")
    checkpoint = torch.load(bundle_path / TEMPORAL_MODEL_FILENAME, map_location="cpu", weights_only=True)
    widen = float(downside_widen) if downside_widen is not None else float(checkpoint.get("downside_widen", DEFAULT_DOWNSIDE_WIDEN))
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
    write_json(bundle_path / BUNDLE_PLANNER_CONFIG_FILENAME, planner_config)

    files = {f: bundle_file_record(bundle_path / f, f) for f in HASHED_TEMPORAL_BUNDLE_FILES}
    manifest = {
        "schema_id": MPC_PRUDENTE_TEMPORAL_BUNDLE_SCHEMA_ID,
        "human_readable_name": "Bundle runtime MPC Prudente — predictor temporal ensemble",
        "media_profile_id": str(media_profile_id),
        "risk_alpha": float(risk_alpha),
        "downside_widen": widen,
        "ensemble_size": int(checkpoint.get("ensemble_size", 0)),
        "required_files": list(REQUIRED_TEMPORAL_BUNDLE_FILES),
        "files": files,
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
    }
    write_json(bundle_path / BUNDLE_MANIFEST_FILENAME, manifest)
    return {"status": "PASS", "bundle_dir": str(bundle_path), "manifest": manifest}


def validate_mpc_prudente_temporal_bundle_dir(bundle_dir: object, *, verify_hashes: bool = True) -> Mapping[str, object]:
    bundle_path = ensure_existing_dir(bundle_dir, purpose="mpc_prudente temporal runtime bundle")
    missing = [f for f in REQUIRED_TEMPORAL_BUNDLE_FILES if not (bundle_path / f).is_file()]
    if missing:
        raise MpcPrudenteBundleError("missing temporal bundle file(s): {0}".format(", ".join(missing)))
    manifest = read_json(bundle_path / BUNDLE_MANIFEST_FILENAME)
    if manifest.get("schema_id") != MPC_PRUDENTE_TEMPORAL_BUNDLE_SCHEMA_ID:
        raise MpcPrudenteBundleError("temporal bundle manifest schema_id is invalid")
    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise MpcPrudenteBundleError("temporal bundle manifest files must be a mapping")
    mismatches = []
    for filename in HASHED_TEMPORAL_BUNDLE_FILES:
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


def load_prudent_runtime_bundle(bundle_dir: object, *, verify_hashes: bool = True):
    """Carga el bundle correcto (MLP o temporal) según el schema_id del manifiesto."""
    from core.mpc_prudente.bundle import MpcPrudenteRuntimeBundle

    bundle_path = ensure_existing_dir(bundle_dir, purpose="mpc_prudente runtime bundle")
    manifest_path = bundle_path / BUNDLE_MANIFEST_FILENAME
    schema = ""
    if manifest_path.is_file():
        schema = str(read_json(manifest_path).get("schema_id", ""))
    if schema == MPC_PRUDENTE_TEMPORAL_BUNDLE_SCHEMA_ID:
        return MpcPrudenteTemporalRuntimeBundle(bundle_dir, verify_hashes=verify_hashes)
    return MpcPrudenteRuntimeBundle(bundle_dir, verify_hashes=verify_hashes)


class MpcPrudenteTemporalRuntimeBundle:
    """Carga el ensemble temporal y predice cuantiles de throughput (bps)."""

    def __init__(self, bundle_dir: object, *, verify_hashes: bool = True) -> None:
        validation = validate_mpc_prudente_temporal_bundle_dir(bundle_dir, verify_hashes=verify_hashes)
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.model_config = dict(read_json(self.bundle_dir / TEMPORAL_MODEL_CONFIG_FILENAME))
        self.normalization = dict(read_json(self.bundle_dir / TEMPORAL_NORMALIZATION_FILENAME))
        self.planner_config = dict(read_json(self.bundle_dir / BUNDLE_PLANNER_CONFIG_FILENAME))
        self.quantiles = tuple(float(q) for q in self.model_config["quantiles"])
        self.horizon_segments = int(self.model_config["horizon_segments"])
        self.risk_alpha = float(self.planner_config.get("risk_alpha", DEFAULT_RISK_ALPHA))
        self.media_profile_id = str(self.planner_config.get("media_profile_id", ""))
        self.rebuffer_weight = float(self.planner_config.get("rebuffer_weight", DEFAULT_REBUFFER_WEIGHT))
        self.switch_weight = float(self.planner_config.get("switch_weight", DEFAULT_SWITCH_WEIGHT))
        self.downside_widen = float(self.planner_config.get("downside_widen", DEFAULT_DOWNSIDE_WIDEN))
        self._seq_mean = [float(v) for v in self.normalization["seq_mean"]]
        self._seq_std = [float(v) for v in self.normalization["seq_std"]]
        self._scalar_mean = [float(v) for v in self.normalization["scalar_mean"]]
        self._scalar_std = [float(v) for v in self.normalization["scalar_std"]]
        self.members = self._load_members()
        self.last_latency_ms = 0.0

    def _load_members(self):
        try:
            checkpoint = torch.load(self.bundle_dir / TEMPORAL_MODEL_FILENAME, map_location="cpu", weights_only=True)
        except Exception as exc:  # noqa: BLE001
            raise MpcPrudenteBundleError("torch.load (weights_only) failed: {0}".format(exc)) from exc
        if checkpoint.get("model_key") != MPC_PRUDENTE_TEMPORAL_MODEL_KEY:
            raise MpcPrudenteBundleError("temporal checkpoint model_key invalid")
        states = checkpoint.get("member_state_dicts")
        if not isinstance(states, (list, tuple)) or not states:
            raise MpcPrudenteBundleError("temporal checkpoint has no member_state_dicts")
        members = []
        for state in states:
            model = TemporalQuantilePredictor(
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

    def predict(self, state, ladder) -> tuple[tuple[float, ...], ...]:
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
        scalar = [float(ctx.get(name, 0.0) or 0.0) for name in SCALAR_FEATURE_NAMES]
        scalar_norm = [
            (scalar[j] - self._scalar_mean[j]) / max(self._scalar_std[j], 1.0e-9) for j in range(len(scalar))
        ]
        seq_t = torch.tensor([seq_norm], dtype=torch.float32)
        scalar_t = torch.tensor([scalar_norm], dtype=torch.float32)
        started = time.perf_counter()
        with torch.no_grad():
            preds = torch.stack([m(seq_t, scalar_t) for m in self.members], dim=0)  # [M,1,H,Q]
            combined = ensemble_quantiles(preds, self.quantiles, downside_widen=self.downside_widen)[0]  # [H,Q]
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        base_tp = harmonic_mean_bps(state.throughput_history_bps)
        rows = []
        for h in range(self.horizon_segments):
            row = []
            for q in range(len(self.quantiles)):
                log_ratio = float(combined[h, q])
                if not math.isfinite(log_ratio):
                    raise MpcPrudenteBundleError("non-finite temporal prediction")
                clipped = max(min(log_ratio, math.log(4.0)), math.log(0.15))
                predicted = float(base_tp) * math.exp(clipped)
                row.append(min(max(predicted, 0.15 * float(base_tp)), 4.0 * float(base_tp)))
            rows.append(tuple(sorted(row)))
        return tuple(rows)
