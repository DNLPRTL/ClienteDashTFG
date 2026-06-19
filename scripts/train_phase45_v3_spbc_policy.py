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

from core.phase45_v3.spbc_policy_training import (
    SPBC_POLICY_TRAINING_PROFILES,
    spbc_policy_training_profile_by_name,
    train_phase45_v3_spbc_policy,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v3" / "spbc_policy"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Entrena SPBC-v3 policy pura sobre dataset closed-loop SPBC/SPC.")
    parser.add_argument("--profile", choices=sorted(SPBC_POLICY_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-profile", default="full_v1")
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--device", default=None, help="cpu, cuda o vacio para autodetectar.")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--hidden-sizes", default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--max-training-samples", type=int, default=None)
    parser.add_argument("--max-validation-samples", type=int, default=None)
    args = parser.parse_args(argv)

    dataset_dir = args.dataset_dir or DEFAULT_DATASET_ROOT / "closedloop_spbc_spc_{0}_v1".format(args.dataset_profile)
    run_name = args.run_name or "spbc_policy_{0}_dataset_{1}_v1".format(args.profile, args.dataset_profile)
    output_dir = args.output_dir or DEFAULT_MODEL_ROOT / run_name
    report = train_phase45_v3_spbc_policy(
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
    profile = spbc_policy_training_profile_by_name(args.profile)
    overrides: dict[str, object] = {}
    for field in (
        "epochs",
        "batch_size",
        "learning_rate",
        "seed",
        "max_training_samples",
        "max_validation_samples",
    ):
        value = getattr(args, field)
        if value is not None:
            overrides[field] = value
    if args.hidden_sizes is not None:
        overrides["hidden_sizes"] = _parse_hidden_sizes(args.hidden_sizes)
    return replace(profile, **overrides)


def _parse_hidden_sizes(raw: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in str(raw).split(",") if part.strip())
    if not values or any(value <= 0 for value in values):
        raise argparse.ArgumentTypeError("--hidden-sizes debe contener enteros positivos separados por coma")
    return values


def _print_compact(report: dict[str, object]) -> None:
    metrics = report["final_validation"]  # type: ignore[index]
    gates = report["gates"]  # type: ignore[index]
    print(
        "phase45_v3_spbc_policy status={status} device={device} "
        "top1={top1_accuracy} mean_regret={mean_regret_q_h} p95_regret={p95_regret_q_h} "
        "expected_regret={expected_regret_mean} gt2={regret_gt_2_0_rate} gt5={regret_gt_5_0_rate} "
        "catastrophic={catastrophic_predicted_rate} "
        "high_capacity_action0={high_capacity_predicted_action0_rate} "
        "predicted_actions={predicted_action_distribution} failed={failed} "
        "model={model_path} sha256={sha}".format(
            status=report["status"],
            device=report["device"],
            top1_accuracy=metrics["top1_accuracy"],
            mean_regret_q_h=metrics["mean_regret_q_h"],
            p95_regret_q_h=metrics["p95_regret_q_h"],
            expected_regret_mean=metrics["expected_regret_mean"],
            regret_gt_2_0_rate=metrics.get("regret_gt_2_0_rate", "NA"),
            regret_gt_5_0_rate=metrics.get("regret_gt_5_0_rate", "NA"),
            catastrophic_predicted_rate=metrics["catastrophic_predicted_rate"],
            high_capacity_predicted_action0_rate=metrics["high_capacity_predicted_action0_rate"],
            predicted_action_distribution=metrics["predicted_action_distribution"],
            failed=gates["failed"],
            model_path=report["model_path"],
            sha=report["model_sha256"],
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
