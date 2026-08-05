#!/usr/bin/env python3
"""Exporta el bundle runtime de MPC Prudente desde el modelo entrenado.

Bundle = predictor entrenado + config del planner (risk_alpha, media_profile_id) +
hashes. No es benchmark ni ranking.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

RAIZ_REPO = Path(__file__).resolve().parents[1]
if str(RAIZ_REPO) not in sys.path:
    sys.path.insert(0, str(RAIZ_REPO))

from core.mpc_prudente.bundle import (
    RISK_ALPHA_POR_DEFECTO,
    exportar_bundle_mpc_prudente,
    validar_dir_bundle_mpc_prudente,
)

TFG_ROOT = RAIZ_REPO.parent
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "mpc_prudente" / "throughput_quantile_predictor"
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "mpc_prudente" / "runtime_bundle_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Exporta el bundle runtime de MPC Prudente.")
    parser.add_argument("--media-profile-id", default="paseo_almunecar_10min_30fps_4s")
    parser.add_argument("--train-profile", default="pilot")
    parser.add_argument("--seed", type=int, default=451001)
    parser.add_argument("--training-dir", type=Path, default=None)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--risk-alpha", type=float, default=RISK_ALPHA_POR_DEFECTO)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    training_dir = args.training_dir or (
        DEFAULT_MODEL_ROOT / "{0}_{1}_seed{2}".format(args.train_profile, args.media_profile_id, args.seed)
    )
    result = exportar_bundle_mpc_prudente(
        training_dir,
        args.bundle_dir,
        media_profile_id=args.media_profile_id,
        risk_alpha=float(args.risk_alpha),
        overwrite=args.overwrite,
    )
    validation = validar_dir_bundle_mpc_prudente(args.bundle_dir)
    print(json.dumps({"export": result, "validation": validation}, indent=2, sort_keys=True, default=str))
    print(
        "MPC_PRUDENTE_BUNDLE status={st} risk_alpha={a} media={m} bundle_dir={d}".format(
            st="PASS" if validation["status"] == "PASS" else "FAIL",
            a=args.risk_alpha,
            m=args.media_profile_id,
            d=args.bundle_dir,
        )
    )
    return 0 if validation["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
