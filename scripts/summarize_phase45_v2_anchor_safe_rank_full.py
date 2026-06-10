#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    path = (
        Path.home()
        / "TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/reporte_entrenamiento_spbc_abr_v2_dpo.json"
    )
    if not path.is_file():
        print(f"Report not found: {path}")
        return 1

    report = json.loads(path.read_text(encoding="utf-8"))
    metrics = report["validation_metrics"]
    focus = metrics["focus_2_5_mbps"]
    source = metrics["by_rollout_source"].get("spbc_v2_dpo_on_policy", {})
    gate = report["selected_checkpoint_safety_gate"]
    comparison = report["init_checkpoint_reference_comparison"]

    print("best_epoch=", report["best_epoch"])
    print("gate=", gate["passed"])
    print("global_over=", metrics["over_aggressive_rate_vs_oracle"])
    print("focus_over=", focus["over_aggressive_rate_vs_oracle"])
    print("spbc2_over=", source.get("over_aggressive_rate_vs_oracle"))
    print("global_u=", metrics["selected_utility_regret_vs_oracle_mean"])
    print("focus_u=", focus["selected_utility_regret_vs_oracle_mean"])
    print("spbc2_u=", source.get("selected_utility_regret_vs_oracle_mean"))
    print("safe_rank=", metrics.get("safe_utility_rank_loss"))
    print("comparison=", comparison["validation_delta_candidate_minus_reference"])
    print("focus_comparison=", comparison["validation_focus_2_5_mbps_delta_candidate_minus_reference"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
