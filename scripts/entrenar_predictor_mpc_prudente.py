#!/usr/bin/env python3
"""Entrena el predictor de cuantiles de throughput para MPC Prudente.

Reutiliza el entrenador de Neural-MPC y añade gates de calibración (cobertura
empírica por cuantil + monotonía). No es benchmark ni ranking.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.mpc_prudente.dataset import DEFAULT_PILOT_MEDIA_PROFILE_ID
from core.mpc_prudente.training import (
    DEFAULT_COVERAGE_TOLERANCE,
    DEFAULT_MAX_CROSSING_RATE,
    train_mpc_prudente_predictor,
)
from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_TRAINING_PROFILES,
    throughput_quantile_training_profile_by_name,
)

TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_ROOT = TFG_ROOT / "datasets_normalizados" / "mpc_prudente"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "mpc_prudente" / "throughput_quantile_predictor"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Entrena el predictor de cuantiles de MPC Prudente.")
    parser.add_argument("--profile", choices=sorted(THROUGHPUT_QUANTILE_TRAINING_PROFILES), default="pilot")
    parser.add_argument("--dataset-profile", default=None)
    parser.add_argument("--media-profile-id", default=DEFAULT_PILOT_MEDIA_PROFILE_ID)
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--hidden-sizes", default=None)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--coverage-tolerance", type=float, default=DEFAULT_COVERAGE_TOLERANCE)
    parser.add_argument("--max-crossing-rate", type=float, default=DEFAULT_MAX_CROSSING_RATE)
    args = parser.parse_args(argv)

    training_profile = _profile_with_overrides(args)
    dataset_profile = args.dataset_profile or args.profile
    dataset_dir = args.dataset_dir or DEFAULT_DATASET_ROOT / "throughput_quantile_{0}_{1}".format(
        dataset_profile, args.media_profile_id
    )
    run_name = args.run_name or "{0}_{1}_seed{2}".format(
        training_profile.name, args.media_profile_id, args.seed or training_profile.seed
    )
    output_dir = args.output_dir or DEFAULT_MODEL_ROOT / run_name

    report = train_mpc_prudente_predictor(
        dataset_dir,
        output_dir,
        training_profile,
        overwrite=args.overwrite,
        device=args.device,
        coverage_tolerance=float(args.coverage_tolerance),
        max_crossing_rate=float(args.max_crossing_rate),
    )

    print(json.dumps(report, indent=2, sort_keys=True))
    calibration = report["calibration"]
    print(
        "MPC_PRUDENTE_TRAINING status={st} device={dev} pinball={pb} "
        "coverage={cov} max_cov_err={mce} crossing_rate={cr} best_epoch={be} model={mp}".format(
            st=report["status"],
            dev=report["device"],
            pb=report["final_validation"]["pinball_loss"],
            cov=calibration["empirical_coverage_by_quantile"],
            mce=calibration["max_coverage_abs_error"],
            cr=calibration["quantile_crossing_rate"],
            be=report["best_epoch"],
            mp=report["model_path"],
        )
    )
    return 0 if report["status"] == "PASS" else 1


def _profile_with_overrides(args: argparse.Namespace):
    profile = throughput_quantile_training_profile_by_name(args.profile)
    overrides: dict[str, object] = {}
    for field in ("epochs", "batch_size", "learning_rate", "seed"):
        value = getattr(args, field)
        if value is not None:
            overrides[field] = value
    if args.hidden_sizes is not None:
        overrides["hidden_sizes"] = tuple(int(p.strip()) for p in str(args.hidden_sizes).split(",") if p.strip())
    if args.horizon is not None:
        overrides["horizon_segments"] = int(args.horizon)
    return replace(profile, **overrides)


if __name__ == "__main__":
    raise SystemExit(main())
