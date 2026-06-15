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

from core.phase45_v3.neural_mpc_bundle import export_phase45_v3_neural_mpc_experimental_bundle


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v3" / "throughput_quantile_predictor" / "expanded_diag_v1"
DEFAULT_RUN_ROOT = TFG_ROOT / "runs_phase45_v3" / "neural_mpc_expanded_diag_v1"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "modelos" / "phase45_v3" / "neural_mpc_experimental_candidate_v1"
DEFAULT_SEEDS = "451001,451002,451003"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Exporta el candidato Neural-MPC Phase45 v3 a un bundle experimental externo."
    )
    parser.add_argument("--model-root", type=Path, default=DEFAULT_MODEL_ROOT)
    parser.add_argument("--run-root", type=Path, default=DEFAULT_RUN_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--canonical-seed", default="451001")
    parser.add_argument("--seeds", default=DEFAULT_SEEDS)
    parser.add_argument("--controller-key", default="phase45_v3_neural_throughput_calibrated_mpc_v1")
    parser.add_argument("--candidate-key", default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    report = export_phase45_v3_neural_mpc_experimental_bundle(
        model_root=args.model_root,
        run_root=args.run_root,
        output_dir=args.output_dir,
        canonical_seed=str(args.canonical_seed),
        seeds=_parse_seeds(args.seeds),
        controller_key=str(args.controller_key),
        candidate_key=args.candidate_key,
        overwrite=bool(args.overwrite),
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def _parse_seeds(raw: str) -> tuple[str, ...]:
    seeds = tuple(value.strip() for value in str(raw).replace(" ", ",").split(",") if value.strip())
    if not seeds:
        raise ValueError("--seeds must contain at least one seed")
    return seeds


if __name__ == "__main__":
    raise SystemExit(main())
