"""Entrenamiento del predictor temporal (GRU) en ensemble.

Entrena M modelos con semillas distintas sobre el dataset fiel, los guarda juntos
y audita la calibración (cobertura empírica) de la predicción combinada.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import torch
from torch.utils.data import DataLoader, TensorDataset

from core.mpc_prudente.temporal_model import (
    MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
    SCALAR_FEATURE_NAMES,
    TemporalQuantilePredictor,
    ensemble_quantiles,
)
from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_jsonl, write_json
from core.phase45_v3.constants import TRAINING_ROLE, VALIDATION_ROLE
from core.phase45_v3.throughput_quantile_dataset import (
    THROUGHPUT_QUANTILE_TARGET_ID,
    THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME,
    THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME,
    validate_phase45_v3_throughput_quantile_dataset_dir,
)
from core.phase45_v3.throughput_quantile_model import pinball_quantile_loss, temporal_smoothness_penalty

TEMPORAL_MODEL_FILENAME = "modelo_temporal_ensemble.pt"
TEMPORAL_MODEL_CONFIG_FILENAME = "configuracion_temporal.json"
TEMPORAL_NORMALIZATION_FILENAME = "normalizacion_temporal.json"
TEMPORAL_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_temporal.json"

DEFAULT_COVERAGE_TOLERANCE = 0.08
DEFAULT_DOWNSIDE_WIDEN = 1.0


class TemporalTrainingError(ValueError):
    pass


@dataclass(frozen=True)
class TemporalTrainingProfile:
    name: str
    ensemble_size: int
    epochs: int
    batch_size: int
    learning_rate: float
    gru_hidden: int
    mlp_hidden: tuple[int, ...]
    quantiles: tuple[float, ...]
    horizon_segments: int
    base_seed: int
    smoothness_weight: float = 0.05
    dropout: float = 0.1

    def to_json(self) -> dict[str, object]:
        return {
            "name": self.name, "ensemble_size": self.ensemble_size, "epochs": self.epochs,
            "batch_size": self.batch_size, "learning_rate": self.learning_rate, "gru_hidden": self.gru_hidden,
            "mlp_hidden": list(self.mlp_hidden), "quantiles": list(self.quantiles),
            "horizon_segments": self.horizon_segments, "base_seed": self.base_seed,
            "smoothness_weight": self.smoothness_weight, "dropout": self.dropout,
        }


TEMPORAL_TRAINING_PROFILES: dict[str, TemporalTrainingProfile] = {
    "smoke": TemporalTrainingProfile(
        name="smoke", ensemble_size=2, epochs=2, batch_size=128, learning_rate=1.0e-3,
        gru_hidden=24, mlp_hidden=(24,), quantiles=(0.10, 0.25, 0.50, 0.75), horizon_segments=5, base_seed=460000,
    ),
    "full": TemporalTrainingProfile(
        name="full", ensemble_size=5, epochs=80, batch_size=1024, learning_rate=3.0e-4,
        gru_hidden=96, mlp_hidden=(96, 64), quantiles=(0.10, 0.25, 0.50, 0.75), horizon_segments=5, base_seed=461000,
    ),
}


def temporal_training_profile_by_name(name: str) -> TemporalTrainingProfile:
    key = str(name).strip()
    if key not in TEMPORAL_TRAINING_PROFILES:
        raise TemporalTrainingError("unknown temporal training profile: {0}".format(name))
    return TEMPORAL_TRAINING_PROFILES[key]


def _sample_arrays(sample: Mapping[str, object], horizon: int) -> tuple[list[list[float]], list[float], list[float]]:
    ctx = sample["model_inputs"]["context"]  # type: ignore[index]
    targets = sample["throughput_quantile_targets"]  # type: ignore[index]
    if targets.get("target_id") != THROUGHPUT_QUANTILE_TARGET_ID:
        raise TemporalTrainingError("unexpected target_id")
    tp = [float(v) for v in ctx["throughput_history_bps"]]
    dt = [float(v) for v in ctx["download_time_history_s"]]
    if len(tp) != len(dt):
        raise TemporalTrainingError("history length mismatch")
    seq = [[math.log1p(max(tp[i], 0.0)), float(dt[i])] for i in range(len(tp))]
    scalar = [float(ctx.get(name, 0.0) or 0.0) for name in SCALAR_FEATURE_NAMES]
    target = [float(v) for v in targets["target_log_ratio_by_horizon"]]
    if len(target) != int(horizon):
        raise TemporalTrainingError("target horizon mismatch")
    return seq, scalar, target


def _load_examples(path: Path, role: str, horizon: int) -> tuple[list, list, list]:
    seqs, scalars, targets = [], [], []
    for row in read_jsonl(path):
        if row.get("data_role") != role:
            raise TemporalTrainingError("data_role mismatch")
        s, sc, t = _sample_arrays(row, horizon)
        seqs.append(s)
        scalars.append(sc)
        targets.append(t)
    if not seqs:
        raise TemporalTrainingError("no examples in {0}".format(path))
    return seqs, scalars, targets


def _fit_normalization(seqs: Sequence, scalars: Sequence) -> dict:
    seq_flat = [step for seq in seqs for step in seq]  # [N*L, 2]
    seq_mean = [0.0, 0.0]; seq_std = [1.0, 1.0]
    for f in range(2):
        col = [row[f] for row in seq_flat]
        m = sum(col) / len(col)
        v = sum((x - m) ** 2 for x in col) / len(col)
        seq_mean[f] = m; seq_std[f] = math.sqrt(v) if v > 1e-12 else 1.0
    width = len(scalars[0])
    sc_mean = [0.0] * width; sc_std = [1.0] * width
    for f in range(width):
        col = [row[f] for row in scalars]
        m = sum(col) / len(col)
        v = sum((x - m) ** 2 for x in col) / len(col)
        sc_mean[f] = m; sc_std[f] = math.sqrt(v) if v > 1e-12 else 1.0
    return {"seq_mean": seq_mean, "seq_std": seq_std, "scalar_mean": sc_mean, "scalar_std": sc_std}


def _tensors(seqs, scalars, targets, norm) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    sm, ss = norm["seq_mean"], norm["seq_std"]
    cm, cs = norm["scalar_mean"], norm["scalar_std"]
    seq_t = torch.tensor(
        [[[(step[f] - sm[f]) / ss[f] for f in range(2)] for step in seq] for seq in seqs], dtype=torch.float32
    )
    sc_t = torch.tensor(
        [[(row[f] - cm[f]) / cs[f] for f in range(len(row))] for row in scalars], dtype=torch.float32
    )
    tg_t = torch.tensor(targets, dtype=torch.float32)
    return seq_t, sc_t, tg_t


def _seed(value: int) -> None:
    random.seed(int(value)); torch.manual_seed(int(value))
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(int(value))


def _device(device: str | None) -> torch.device:
    if device and str(device).strip().lower() not in {"auto", "default"}:
        return torch.device(device)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def train_mpc_prudente_temporal_ensemble(
    dataset_dir: object,
    output_dir: object,
    profile: TemporalTrainingProfile,
    *,
    overwrite: bool = False,
    device: str | None = None,
    coverage_tolerance: float = DEFAULT_COVERAGE_TOLERANCE,
    downside_widen: float = DEFAULT_DOWNSIDE_WIDEN,
) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(dataset_dir, purpose="mpc_prudente faithful dataset")
    validation = validate_phase45_v3_throughput_quantile_dataset_dir(data_dir)
    if validation["status"] != "PASS":
        raise TemporalTrainingError("dataset validation failed: {0}".format(validation["errors"]))
    out = prepare_output_dir(output_dir, overwrite=overwrite, purpose="mpc_prudente temporal training")
    dev = _device(device)
    horizon = int(profile.horizon_segments)

    tr_seq, tr_sc, tr_tg = _load_examples(data_dir / THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME, TRAINING_ROLE, horizon)
    va_seq, va_sc, va_tg = _load_examples(data_dir / THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME, VALIDATION_ROLE, horizon)
    norm = _fit_normalization(tr_seq, tr_sc)
    tr_t = _tensors(tr_seq, tr_sc, tr_tg, norm)
    va_t = tuple(t.to(dev) for t in _tensors(va_seq, va_sc, va_tg, norm))

    member_states = []
    member_reports = []
    for member in range(profile.ensemble_size):
        seed = int(profile.base_seed) + member * 101
        _seed(seed)
        model = TemporalQuantilePredictor(
            seq_features=2, scalar_dim=len(SCALAR_FEATURE_NAMES), horizon_segments=horizon,
            quantiles=profile.quantiles, gru_hidden=profile.gru_hidden, mlp_hidden=profile.mlp_hidden,
            dropout=profile.dropout,
        ).to(dev)
        optimizer = torch.optim.AdamW(model.parameters(), lr=float(profile.learning_rate), weight_decay=1.0e-5)
        loader = DataLoader(
            TensorDataset(*tr_t), batch_size=int(profile.batch_size), shuffle=True,
            generator=torch.Generator().manual_seed(seed),
        )
        best_val = math.inf; best_state = None; best_epoch = 0
        for epoch in range(1, int(profile.epochs) + 1):
            model.train()
            for seq_b, sc_b, tg_b in loader:
                seq_b, sc_b, tg_b = seq_b.to(dev), sc_b.to(dev), tg_b.to(dev)
                pred = model(seq_b, sc_b)
                loss = pinball_quantile_loss(pred, tg_b, profile.quantiles) + \
                    float(profile.smoothness_weight) * temporal_smoothness_penalty(pred)
                optimizer.zero_grad(set_to_none=True)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
                optimizer.step()
            model.eval()
            with torch.no_grad():
                val_pred = model(va_t[0], va_t[1])
                val_pinball = float(pinball_quantile_loss(val_pred, va_t[2], profile.quantiles).cpu())
            if val_pinball < best_val:
                best_val = val_pinball; best_epoch = epoch
                best_state = {k: v.detach().cpu() for k, v in model.state_dict().items()}
        if best_state is not None:
            model.load_state_dict(best_state)
        member_states.append({k: v.detach().cpu() for k, v in model.state_dict().items()})
        member_reports.append({"member": member, "seed": seed, "best_epoch": best_epoch, "val_pinball": round(best_val, 6)})

    calibration = _ensemble_calibration(member_states, profile, norm, va_t, dev, downside_widen)
    gates = _gates(calibration, member_reports, coverage_tolerance)

    checkpoint = {
        "model_key": MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
        "ensemble_size": profile.ensemble_size,
        "downside_widen": float(downside_widen),
        "model_config": _model_config(profile),
        "normalization": norm,
        "member_state_dicts": member_states,
    }
    torch.save(checkpoint, out / TEMPORAL_MODEL_FILENAME)
    write_json(out / TEMPORAL_MODEL_CONFIG_FILENAME, _model_config(profile))
    write_json(out / TEMPORAL_NORMALIZATION_FILENAME, norm)
    report = {
        "schema_id": "mpc_prudente_temporal_training_report_v1",
        "status": "PASS" if not gates["failed"] else "REVIEW",
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "device": str(dev), "dataset_dir": str(data_dir), "output_dir": str(out),
        "profile": profile.to_json(), "members": member_reports,
        "train_sample_count": len(tr_seq), "validation_sample_count": len(va_seq),
        "calibration": calibration, "gates": gates,
        "benchmark_performed": False, "ranking_performed": False, "qoe_claims_authorized": False,
    }
    write_json(out / TEMPORAL_TRAINING_REPORT_FILENAME, report)
    return report


def _model_config(profile: TemporalTrainingProfile) -> dict:
    return {
        "model_key": MPC_PRUDENTE_TEMPORAL_MODEL_KEY, "seq_features": 2,
        "scalar_dim": len(SCALAR_FEATURE_NAMES), "scalar_feature_names": list(SCALAR_FEATURE_NAMES),
        "horizon_segments": profile.horizon_segments, "quantiles": list(profile.quantiles),
        "gru_hidden": profile.gru_hidden, "gru_layers": 1, "mlp_hidden": list(profile.mlp_hidden),
        "dropout": profile.dropout, "ensemble_size": profile.ensemble_size,
    }


def _ensemble_calibration(member_states, profile, norm, va_t, dev, downside_widen) -> dict:
    models = []
    for state in member_states:
        m = TemporalQuantilePredictor(
            seq_features=2, scalar_dim=len(SCALAR_FEATURE_NAMES), horizon_segments=profile.horizon_segments,
            quantiles=profile.quantiles, gru_hidden=profile.gru_hidden, mlp_hidden=profile.mlp_hidden,
            dropout=profile.dropout,
        ).to(dev)
        m.load_state_dict(state); m.eval(); models.append(m)
    with torch.no_grad():
        preds = torch.stack([m(va_t[0], va_t[1]) for m in models], dim=0)  # [M,B,H,Q]
        combined = ensemble_quantiles(preds, profile.quantiles, downside_widen=float(downside_widen))  # [B,H,Q]
        target = va_t[2].unsqueeze(2)  # [B,H,1]
        below = (target <= combined).float()
        coverage = below.mean(dim=(0, 1)).tolist()
        epistemic = preds[:, :, :, min(range(len(profile.quantiles)), key=lambda i: abs(profile.quantiles[i] - 0.5))].std(dim=0).mean().item()
    cov_err = [abs(float(coverage[k]) - float(profile.quantiles[k])) for k in range(len(profile.quantiles))]
    return {
        "empirical_coverage_by_quantile": [round(float(c), 6) for c in coverage],
        "coverage_abs_error_by_quantile": [round(e, 6) for e in cov_err],
        "max_coverage_abs_error": round(max(cov_err), 6) if cov_err else 0.0,
        "mean_epistemic_disagreement": round(float(epistemic), 6),
    }


def _gates(calibration, member_reports, coverage_tolerance) -> dict:
    learned = all(float(m["val_pinball"]) < 10.0 and math.isfinite(float(m["val_pinball"])) for m in member_reports)
    gates = {
        "coverage_calibrated": {
            "passed": float(calibration["max_coverage_abs_error"]) <= float(coverage_tolerance),
            "observed": calibration["max_coverage_abs_error"], "threshold": coverage_tolerance,
        },
        "all_members_finite_loss": {
            "passed": bool(learned),
            "observed": [m["val_pinball"] for m in member_reports],
            "threshold": "finita y < 10.0",
        },
    }
    failed = [n for n, g in gates.items() if not g["passed"]]
    return {"failed": failed, "gates": gates}
