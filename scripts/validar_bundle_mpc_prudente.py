#!/usr/bin/env python3
"""Valida el bundle runtime de MPC Prudente (hashes + que el modelo carga)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

RAIZ_REPO = Path(__file__).resolve().parents[1]
if str(RAIZ_REPO) not in sys.path:
    sys.path.insert(0, str(RAIZ_REPO))

from core.mpc_prudente.bundle import BundleRuntimeMpcPrudente, validar_dir_bundle_mpc_prudente

TFG_ROOT = RAIZ_REPO.parent
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "mpc_prudente" / "runtime_bundle_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Valida el bundle runtime de MPC Prudente.")
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    args = parser.parse_args(argv)

    validation = validar_dir_bundle_mpc_prudente(args.bundle_dir)
    bundle = BundleRuntimeMpcPrudente(args.bundle_dir)  # carga el modelo (weights_only)
    print(json.dumps(validation, indent=2, sort_keys=True, default=str))
    print(
        "MPC_PRUDENTE_BUNDLE_VALIDATION status={st} risk_alpha={a} media={m} quantiles={q} horizon={h}".format(
            st=validation["status"],
            a=bundle.risk_alpha,
            m=bundle.media_profile_id,
            q=list(bundle.quantiles),
            h=bundle.horizon_segments,
        )
    )
    return 0 if validation["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
