#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase45_v3.closedloop_spbc_spc_dataset import summarize_phase45_v3_closedloop_spbc_spc_dataset


TFG_ROOT = REPO_ROOT.parent
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resume un dataset Phase45 v3 closed-loop SPBC/SPC.")
    parser.add_argument("--profile", default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--json", action="store_true", help="Imprime el resumen como JSON.")
    args = parser.parse_args(argv)

    dataset_dir = args.dataset_dir or DEFAULT_OUTPUT_ROOT / "closedloop_spbc_spc_{0}_v1".format(args.profile)
    summary = summarize_phase45_v3_closedloop_spbc_spc_dataset(dataset_dir)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        _print_compact(summary)
    return 0 if summary["status"] == "PASS" else 1


def _print_compact(summary: Mapping[str, object]) -> None:
    print(
        "phase45_v3_closedloop_spbc_spc_dataset status={status} profile={profile} "
        "samples={sample_counts} windows={generation_window_counts} max_buffer_s={max_buffer_s} "
        "targets={target_status} leakage={leakage_status} fallback_count={fallback_count} "
        "target_action0_rate={target_action0_rate} "
        "high_capacity_safe_state_count={high_capacity_safe_state_count} "
        "high_capacity_safe_target_action0_rate={high_capacity_safe_target_action0_rate} "
        "safe_action_presence_rate={safe_action_presence_rate} "
        "catastrophic_action_fraction={catastrophic_action_fraction} "
        "policy_targets={policy_target_distribution} rollouts={rollout_policy_distribution} "
        "mean_best_q_h_reward_n={mean_best_q_h_reward_n}".format(**summary)
    )


if __name__ == "__main__":
    raise SystemExit(main())
