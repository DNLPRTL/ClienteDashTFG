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

from core.neural_abr.artifacts import read_json
from core.phase45_v3.constants import LEAKAGE_AUDIT_FILENAME, QH_AUDIT_FILENAME, SUMMARY_FILENAME
from core.phase45_v3.validation import validate_phase45_v3_dataset_dir


TFG_ROOT = REPO_ROOT.parent
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resume un dataset Phase 4-5 v3 Q_H closed-loop.")
    parser.add_argument("--profile", default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=None)
    parser.add_argument("--json", action="store_true", help="Imprime el resumen como JSON.")
    args = parser.parse_args(argv)

    dataset_dir = args.dataset_dir or DEFAULT_OUTPUT_ROOT / "qh_closed_loop_{0}".format(args.profile)
    summary = summarize_phase45_v3_qh_dataset(dataset_dir)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        _print_compact(summary)
    return 0 if summary["status"] == "PASS" else 1


def summarize_phase45_v3_qh_dataset(dataset_dir: object) -> Mapping[str, object]:
    root = Path(dataset_dir).expanduser()
    validation = validate_phase45_v3_dataset_dir(root)
    dataset_summary = read_json(root / SUMMARY_FILENAME)
    qh_audit = read_json(root / QH_AUDIT_FILENAME)
    leakage_audit = read_json(root / LEAKAGE_AUDIT_FILENAME)
    content_ladder = dataset_summary.get("content_ladder", {})
    profile = dataset_summary.get("profile", {})
    payload = {
        "status": "PASS"
        if validation["status"] == "PASS" and qh_audit.get("status") == "PASS" and leakage_audit.get("status") == "PASS"
        else "FAIL",
        "dataset_dir": str(root),
        "profile": profile.get("name") if isinstance(profile, Mapping) else "",
        "rollouts_per_window": profile.get("rollouts_per_window") if isinstance(profile, Mapping) else None,
        "sample_counts": dataset_summary.get("sample_counts", {}),
        "max_buffer_s": content_ladder.get("max_buffer_s") if isinstance(content_ladder, Mapping) else None,
        "validation_status": validation["status"],
        "leakage_status": leakage_audit.get("status"),
        "qh_status": qh_audit.get("status"),
        "skipped_window_count": len(dataset_summary.get("skipped_windows", [])),
        "fallback_count": qh_audit.get("fallback_count"),
        "target_action0_rate": qh_audit.get("target_action0_rate"),
        "high_capacity_safe_state_count": qh_audit.get("high_capacity_safe_state_count"),
        "high_capacity_safe_target_action0_rate": qh_audit.get("high_capacity_safe_target_action0_rate"),
        "target_action_distribution": qh_audit.get("target_action_distribution", {}),
        "rollout_policy_distribution": qh_audit.get("rollout_policy_distribution", {}),
        "q_h_reward_mean": qh_audit.get("q_h_reward_mean"),
    }
    return payload


def _print_compact(summary: Mapping[str, object]) -> None:
    print(
        "phase45_v3_qh_dataset status={status} profile={profile} "
        "samples={sample_counts} max_buffer_s={max_buffer_s} "
        "qh={qh_status} leakage={leakage_status} fallback_count={fallback_count} "
        "target_action0_rate={target_action0_rate} "
        "high_capacity_safe_state_count={high_capacity_safe_state_count} "
        "high_capacity_safe_target_action0_rate={high_capacity_safe_target_action0_rate} "
        "target_actions={target_action_distribution} rollouts={rollout_policy_distribution} "
        "q_h_reward_mean={q_h_reward_mean}".format(**summary)
    )


if __name__ == "__main__":
    raise SystemExit(main())
