#!/usr/bin/env python3
"""Entrena el predictor TEMPORAL (GRU) en ensemble para MPC Prudente."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Sequence

RAIZ_REPO = Path(__file__).resolve().parents[1]
if str(RAIZ_REPO) not in sys.path:
    sys.path.insert(0, str(RAIZ_REPO))

from core.mpc_prudente.dataset_fiel import ID_PERFIL_MEDIO_PILOTO
from core.mpc_prudente.entrenamiento_temporal import (
    DOWNSIDE_WIDEN_POR_DEFECTO,
    PERFILES_ENTRENAMIENTO_TEMPORAL,
    perfil_entrenamiento_temporal_por_nombre,
    entrenar_ensemble_temporal_mpc_prudente,
)

TFG_ROOT = RAIZ_REPO.parent
DEFAULT_DATASET_ROOT = TFG_ROOT / "datasets_normalizados" / "mpc_prudente"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "mpc_prudente" / "temporal_predictor"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Entrena el predictor temporal (GRU) ensemble de MPC Prudente.")
    parser.add_argument("--profile", choices=sorted(PERFILES_ENTRENAMIENTO_TEMPORAL), default="full")
    parser.add_argument("--dataset-profile", default="full_v1")
    parser.add_argument("--media-profile-id", default=ID_PERFIL_MEDIO_PILOTO)
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--ensemble-size", type=int, default=None)
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--downside-widen", type=float, default=DOWNSIDE_WIDEN_POR_DEFECTO)
    parser.add_argument("--coverage-tolerance", type=float, default=0.08)
    args = parser.parse_args(argv)

    profile = perfil_entrenamiento_temporal_por_nombre(args.profile)
    overrides = {}
    if args.ensemble_size is not None:
        overrides["ensemble_size"] = int(args.ensemble_size)
    if args.epochs is not None:
        overrides["epochs"] = int(args.epochs)
    if overrides:
        profile = replace(profile, **overrides)

    dataset_dir = args.dataset_dir or DEFAULT_DATASET_ROOT / "throughput_quantile_{0}_{1}".format(
        args.dataset_profile, args.media_profile_id
    )
    output_dir = args.output_dir or DEFAULT_MODEL_ROOT / "{0}_{1}".format(args.profile, args.media_profile_id)

    report = entrenar_ensemble_temporal_mpc_prudente(
        dataset_dir, output_dir, profile,
        overwrite=args.overwrite, device=args.device,
        coverage_tolerance=float(args.coverage_tolerance), downside_widen=float(args.downside_widen),
    )
    print(json.dumps(report, indent=2, sort_keys=True, default=str))
    cal = report["calibration"]
    print(
        "MPC_PRUDENTE_TEMPORAL status={st} device={dev} ensemble={n} coverage={cov} "
        "max_cov_err={mce} epistemic={ep} model={out}".format(
            st=report["status"], dev=report["device"], n=report["profile"]["ensemble_size"],
            cov=cal["empirical_coverage_by_quantile"], mce=cal["max_coverage_abs_error"],
            ep=cal["mean_epistemic_disagreement"], out=report["output_dir"],
        )
    )
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
