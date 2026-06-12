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

from core.phase45_v3.qh_scorer_training import (
    QH_SCORER_TRAINING_PROFILES,
    train_phase45_v3_qh_scorer,
    training_profile_by_name,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v3" / "qh_scorer"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Entrena el scorer Phase 4-5 v3 Q_H.")
    parser.add_argument("--profile", choices=sorted(QH_SCORER_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-profile", default=None)
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--device", default=None, help="cpu, cuda o vacio para autodetectar.")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    dataset_profile = args.dataset_profile or args.profile
    dataset_dir = args.dataset_dir or DEFAULT_DATASET_ROOT / "qh_closed_loop_{0}".format(dataset_profile)
    run_name = args.run_name or "qh_scorer_{0}_dataset_{1}_v1".format(args.profile, dataset_profile)
    output_dir = args.output_dir or DEFAULT_MODEL_ROOT / run_name
    report = train_phase45_v3_qh_scorer(
        dataset_dir,
        output_dir,
        training_profile_by_name(args.profile),
        overwrite=args.overwrite,
        device=args.device,
    )
    _print_compact(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


def _print_compact(report: dict[str, object]) -> None:
    metrics = report["final_validation"]  # type: ignore[index]
    gates = report["gates"]  # type: ignore[index]
    print(
        "phase45_v3_qh_scorer status={status} device={device} "
        "top1={top1_accuracy} mean_regret={mean_regret_q_h} p95_regret={p95_regret_q_h} "
        "high_capacity_action0={high_capacity_predicted_action0_rate} "
        "predicted_actions={predicted_action_distribution} failed={failed} model={model_path} sha256={sha}".format(
            status=report["status"],
            device=report["device"],
            top1_accuracy=metrics["top1_accuracy"],
            mean_regret_q_h=metrics["mean_regret_q_h"],
            p95_regret_q_h=metrics["p95_regret_q_h"],
            high_capacity_predicted_action0_rate=metrics["high_capacity_predicted_action0_rate"],
            predicted_action_distribution=metrics["predicted_action_distribution"],
            failed=gates["failed"],
            model_path=report["model_path"],
            sha=report["model_sha256"],
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
