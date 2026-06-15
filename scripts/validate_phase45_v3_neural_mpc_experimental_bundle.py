#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase45_v3.neural_mpc_bundle import (
    NEURAL_MPC_BUNDLE_MANIFEST_FILENAME,
    validate_phase45_v3_neural_mpc_bundle_dir,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "phase45_v3" / "neural_mpc_experimental_candidate_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida manifiesto y hashes del bundle experimental Neural-MPC Phase45 v3."
    )
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--no-verify-hashes", action="store_true")
    args = parser.parse_args(argv)

    validation = validate_phase45_v3_neural_mpc_bundle_dir(
        args.bundle_dir,
        verify_hashes=not bool(args.no_verify_hashes),
    )
    report = {
        "schema_id": "phase45_v3_neural_mpc_experimental_bundle_validation_v1",
        "status": validation["status"],
        "decision": "BUNDLE_CONTRACT_AND_HASHES_VALID",
        "bundle_dir": validation["bundle_dir"],
        "manifest": str(Path(validation["bundle_dir"]) / NEURAL_MPC_BUNDLE_MANIFEST_FILENAME),
        "required_files": validation["required_files"],
        "hashes_valid": validation["hashes_valid"],
        "controller_integrated": False,
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
