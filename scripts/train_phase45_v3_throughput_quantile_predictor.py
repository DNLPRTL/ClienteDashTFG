#!/usr/bin/env python3
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

from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_TRAINING_PROFILES,
    train_phase45_v3_throughput_quantile_predictor,
    throughput_quantile_training_profile_by_name,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v3" / "throughput_quantile_predictor"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Entrena el predictor Phase45 v3 de cuantiles de throughput.")
    parser.add_argument("--profile", choices=sorted(THROUGHPUT_QUANTILE_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-profile", default=None)
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--hidden-sizes", default=None)
    parser.add_argument("--quantiles", default=None)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--pinball-loss-weight", type=float, default=None)
    parser.add_argument("--quantile-crossing-loss-weight", type=float, default=None)
    parser.add_argument("--temporal-smoothness-loss-weight", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args(argv)

    dataset_profile = args.dataset_profile or args.profile
    dataset_dir = args.dataset_dir or DEFAULT_DATASET_ROOT / "throughput_quantile_{0}_v1".format(dataset_profile)
    run_name = args.run_name or "pilot_v1_seed{0}".format(args.seed or throughput_quantile_training_profile_by_name(args.profile).seed)
    output_dir = args.output_dir or DEFAULT_MODEL_ROOT / run_name
    report = train_phase45_v3_throughput_quantile_predictor(
        dataset_dir,
        output_dir,
        _profile_with_overrides(args),
        overwrite=args.overwrite,
        device=args.device,
    )
    _print_compact(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


def _profile_with_overrides(args: argparse.Namespace):
    profile = throughput_quantile_training_profile_by_name(args.profile)
    overrides: dict[str, object] = {}
    for field in (
        "epochs",
        "batch_size",
        "learning_rate",
        "pinball_loss_weight",
        "quantile_crossing_loss_weight",
        "temporal_smoothness_loss_weight",
        "seed",
    ):
        value = getattr(args, field)
        if value is not None:
            overrides[field] = value
    if args.hidden_sizes is not None:
        overrides["hidden_sizes"] = _parse_ints(args.hidden_sizes, "--hidden-sizes")
    if args.quantiles is not None:
        overrides["quantiles"] = _parse_floats(args.quantiles, "--quantiles")
    if args.horizon is not None:
        overrides["horizon_segments"] = int(args.horizon)
    return replace(profile, **overrides)


def _parse_ints(raw: str, option_name: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in str(raw).split(",") if part.strip())
    if not values or any(value <= 0 for value in values):
        raise argparse.ArgumentTypeError("{0} must contain positive integers".format(option_name))
    return values


def _parse_floats(raw: str, option_name: str) -> tuple[float, ...]:
    values = tuple(float(part.strip()) for part in str(raw).split(",") if part.strip())
    if not values:
        raise argparse.ArgumentTypeError("{0} must not be empty".format(option_name))
    return values


def _print_compact(report: dict[str, object]) -> None:
    metrics = report["final_validation"]  # type: ignore[index]
    print(
        "phase45_v3_throughput_quantile status={status} device={device} "
        "pinball={pinball} p95_abs_log_ratio={p95} model={model_path} sha256={sha}".format(
            status=report["status"],
            device=report["device"],
            pinball=metrics["pinball_loss"],
            p95=metrics["median_abs_log_ratio_error_p95"],
            model_path=report["model_path"],
            sha=report["model_sha256"],
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
