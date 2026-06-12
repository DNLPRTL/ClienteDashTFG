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
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--hidden-sizes", default=None, help="Capas ocultas separadas por coma, por ejemplo 384,192,96.")
    parser.add_argument("--model-architecture", default=None)
    parser.add_argument("--history-gru-hidden-size", type=int, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--ce-loss-weight", type=float, default=None)
    parser.add_argument("--q-value-loss-weight", type=float, default=None)
    parser.add_argument("--pairwise-rank-loss-weight", type=float, default=None)
    parser.add_argument("--pairwise-margin-scale", type=float, default=None)
    parser.add_argument("--pairwise-q-gap-cap", type=float, default=None)
    parser.add_argument("--pairwise-use-denormalized-q-gap", action="store_true", default=None)
    parser.add_argument("--soft-q-kl-loss-weight", type=float, default=None)
    parser.add_argument("--q-softmax-temperature", type=float, default=None)
    parser.add_argument("--expected-regret-loss-weight", type=float, default=None)
    parser.add_argument("--tail-regret-loss-weight", type=float, default=None)
    parser.add_argument("--tail-regret-fraction", type=float, default=None)
    parser.add_argument("--advantage-huber-loss-weight", type=float, default=None)
    parser.add_argument("--advantage-scale", type=float, default=None)
    parser.add_argument("--top-vs-bad-margin-loss-weight", type=float, default=None)
    parser.add_argument("--top-vs-bad-regret-threshold", type=float, default=None)
    parser.add_argument("--top-vs-bad-margin-scale", type=float, default=None)
    parser.add_argument("--top-vs-bad-gap-cap", type=float, default=None)
    parser.add_argument("--structured-cost-hinge-loss-weight", type=float, default=None)
    parser.add_argument("--structured-cost-margin-scale", type=float, default=None)
    parser.add_argument("--structured-cost-gap-cap", type=float, default=None)
    parser.add_argument("--catastrophic-prob-loss-weight", type=float, default=None)
    parser.add_argument("--catastrophic-regret-threshold", type=float, default=None)
    parser.add_argument("--catastrophic-regret-cap", type=float, default=None)
    parser.add_argument("--catastrophic-regret-power", type=float, default=None)
    parser.add_argument("--slice-weight-throughput-2-5", type=float, default=None)
    parser.add_argument("--slice-weight-buffer-0-4", type=float, default=None)
    parser.add_argument("--slice-weight-buffer-4-16", type=float, default=None)
    parser.add_argument("--slice-weight-buffer-16-32", type=float, default=None)
    parser.add_argument("--slice-weight-rollout-qh-plus-one", type=float, default=None)
    parser.add_argument("--slice-weight-max-regret-5", type=float, default=None)
    parser.add_argument("--slice-weight-max-regret-20", type=float, default=None)
    parser.add_argument("--slice-weight-max", type=float, default=None)
    args = parser.parse_args(argv)

    dataset_profile = args.dataset_profile or args.profile
    dataset_dir = args.dataset_dir or DEFAULT_DATASET_ROOT / "qh_closed_loop_{0}".format(dataset_profile)
    run_name = args.run_name or "qh_scorer_{0}_dataset_{1}_v1".format(args.profile, dataset_profile)
    output_dir = args.output_dir or DEFAULT_MODEL_ROOT / run_name
    report = train_phase45_v3_qh_scorer(
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
    profile = training_profile_by_name(args.profile)
    overrides: dict[str, object] = {}
    direct_fields = (
        "epochs",
        "batch_size",
        "learning_rate",
        "seed",
        "model_architecture",
        "history_gru_hidden_size",
        "ce_loss_weight",
        "q_value_loss_weight",
        "pairwise_rank_loss_weight",
        "pairwise_margin_scale",
        "pairwise_q_gap_cap",
        "pairwise_use_denormalized_q_gap",
        "soft_q_kl_loss_weight",
        "q_softmax_temperature",
        "expected_regret_loss_weight",
        "tail_regret_loss_weight",
        "tail_regret_fraction",
        "advantage_huber_loss_weight",
        "advantage_scale",
        "top_vs_bad_margin_loss_weight",
        "top_vs_bad_regret_threshold",
        "top_vs_bad_margin_scale",
        "top_vs_bad_gap_cap",
        "structured_cost_hinge_loss_weight",
        "structured_cost_margin_scale",
        "structured_cost_gap_cap",
        "catastrophic_prob_loss_weight",
        "catastrophic_regret_threshold",
        "catastrophic_regret_cap",
        "catastrophic_regret_power",
        "slice_weight_throughput_2_5",
        "slice_weight_buffer_0_4",
        "slice_weight_buffer_4_16",
        "slice_weight_buffer_16_32",
        "slice_weight_rollout_qh_plus_one",
        "slice_weight_max_regret_5",
        "slice_weight_max_regret_20",
        "slice_weight_max",
    )
    for field in direct_fields:
        value = getattr(args, field)
        if value is not None:
            overrides[field] = value
    if args.hidden_sizes is not None:
        overrides["hidden_sizes"] = _parse_hidden_sizes(args.hidden_sizes)
    profile = replace(profile, **overrides)
    if (
        "pairwise_use_denormalized_q_gap" not in overrides
        and float(profile.pairwise_rank_loss_weight) > 0.0
        and (
            float(profile.soft_q_kl_loss_weight) > 0.0
            or float(profile.expected_regret_loss_weight) > 0.0
            or float(profile.tail_regret_loss_weight) > 0.0
            or float(profile.advantage_huber_loss_weight) > 0.0
            or float(profile.top_vs_bad_margin_loss_weight) > 0.0
        )
    ):
        profile = replace(profile, pairwise_use_denormalized_q_gap=True)
    return profile


def _parse_hidden_sizes(raw: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in str(raw).split(",") if part.strip())
    if not values or any(value <= 0 for value in values):
        raise argparse.ArgumentTypeError("--hidden-sizes debe contener enteros positivos separados por coma")
    return values


def _print_compact(report: dict[str, object]) -> None:
    metrics = report["final_validation"]  # type: ignore[index]
    gates = report["gates"]  # type: ignore[index]
    print(
        "phase45_v3_qh_scorer status={status} device={device} "
        "top1={top1_accuracy} mean_regret={mean_regret_q_h} p95_regret={p95_regret_q_h} "
        "gt2={regret_gt_2_0_rate} gt5={regret_gt_5_0_rate} gt20={regret_gt_20_0_rate} "
        "high_capacity_action0={high_capacity_predicted_action0_rate} "
        "predicted_actions={predicted_action_distribution} failed={failed} model={model_path} sha256={sha}".format(
            status=report["status"],
            device=report["device"],
            top1_accuracy=metrics["top1_accuracy"],
            mean_regret_q_h=metrics["mean_regret_q_h"],
            p95_regret_q_h=metrics["p95_regret_q_h"],
            regret_gt_2_0_rate=metrics.get("regret_gt_2_0_rate", "NA"),
            regret_gt_5_0_rate=metrics.get("regret_gt_5_0_rate", "NA"),
            regret_gt_20_0_rate=metrics.get("regret_gt_20_0_rate", "NA"),
            high_capacity_predicted_action0_rate=metrics["high_capacity_predicted_action0_rate"],
            predicted_action_distribution=metrics["predicted_action_distribution"],
            failed=gates["failed"],
            model_path=report["model_path"],
            sha=report["model_sha256"],
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
