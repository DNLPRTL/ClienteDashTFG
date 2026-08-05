#!/usr/bin/env python3
"""Exporta el bundle runtime del predictor TEMPORAL (ensemble) de MPC Prudente."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

RAIZ_REPO = Path(__file__).resolve().parents[1]
if str(RAIZ_REPO) not in sys.path:
    sys.path.insert(0, str(RAIZ_REPO))

from core.mpc_prudente.bundle import RISK_ALPHA_POR_DEFECTO
from core.mpc_prudente.dataset_fiel import ID_PERFIL_MEDIO_PILOTO
from core.mpc_prudente.bundle_temporal import (
    exportar_bundle_temporal_mpc_prudente,
    validar_dir_bundle_temporal_mpc_prudente,
)

TFG_ROOT = RAIZ_REPO.parent
DEFAULT_TRAINING_DIR = TFG_ROOT / "modelos" / "mpc_prudente" / "temporal_predictor" / "full_multimedia"
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "mpc_prudente" / "temporal_runtime_bundle_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Exporta el bundle runtime temporal de MPC Prudente.")
    parser.add_argument("--training-dir", type=Path, default=DEFAULT_TRAINING_DIR)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--media-profile-id", default=ID_PERFIL_MEDIO_PILOTO)
    parser.add_argument("--risk-alpha", type=float, default=RISK_ALPHA_POR_DEFECTO)
    parser.add_argument("--downside-widen", type=float, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    result = exportar_bundle_temporal_mpc_prudente(
        args.training_dir,
        args.bundle_dir,
        media_profile_id=args.media_profile_id,
        risk_alpha=float(args.risk_alpha),
        downside_widen=args.downside_widen,
        overwrite=args.overwrite,
    )
    validation = validar_dir_bundle_temporal_mpc_prudente(args.bundle_dir)
    status = "PASS" if result["status"] == "PASS" and validation["status"] == "PASS" else "FAIL"
    print(json.dumps({"export": result, "validation": validation}, indent=2, sort_keys=True, default=str))
    print(
        "MPC_PRUDENTE_TEMPORAL_BUNDLE status={st} bundle_dir={bd} media={md} risk_alpha={ra} ensemble={en}".format(
            st=status,
            bd=args.bundle_dir,
            md=args.media_profile_id,
            ra=args.risk_alpha,
            en=result["manifest"].get("ensemble_size"),
        )
    )
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
