#!/usr/bin/env python3
"""Exporta el bundle runtime del predictor TEMPORAL (ensemble) de MPC Prudente."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.mpc_prudente.bundle import DEFAULT_RISK_ALPHA
from core.mpc_prudente.dataset import DEFAULT_PILOT_MEDIA_PROFILE_ID
from core.mpc_prudente.temporal_bundle import (
    export_mpc_prudente_temporal_bundle,
    validate_mpc_prudente_temporal_bundle_dir,
)

TFG_ROOT = REPO_ROOT.parent
DEFAULT_TRAINING_DIR = TFG_ROOT / "modelos" / "mpc_prudente" / "temporal_predictor" / "full_multimedia"
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "mpc_prudente" / "temporal_runtime_bundle_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Exporta el bundle runtime temporal de MPC Prudente.")
    parser.add_argument("--training-dir", type=Path, default=DEFAULT_TRAINING_DIR)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--media-profile-id", default=DEFAULT_PILOT_MEDIA_PROFILE_ID)
    parser.add_argument("--risk-alpha", type=float, default=DEFAULT_RISK_ALPHA)
    parser.add_argument("--downside-widen", type=float, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    result = export_mpc_prudente_temporal_bundle(
        args.training_dir,
        args.bundle_dir,
        media_profile_id=args.media_profile_id,
        risk_alpha=float(args.risk_alpha),
        downside_widen=args.downside_widen,
        overwrite=args.overwrite,
    )
    validation = validate_mpc_prudente_temporal_bundle_dir(args.bundle_dir)
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
