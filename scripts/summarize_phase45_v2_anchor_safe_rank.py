#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path.home() / "TFG/modelos/phase45_v1/spbc_abr_v2_dpo"
    reports = sorted(
        root.glob("pilot_dagger2_warm_v3_anchor_safe_rank_seed_*_v1/reporte_entrenamiento_spbc_abr_v2_dpo.json")
    )
    if not reports:
        print("No anchor_safe_rank reports found.")
        return 1
    for path in reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        metrics = report["validation_metrics"]
        focus = metrics["focus_2_5_mbps"]
        source = metrics["by_rollout_source"].get("spbc_v2_dpo_on_policy", {})
        gate = report["selected_checkpoint_safety_gate"]
        print(
            path.parent.name,
            "best_epoch=", report["best_epoch"],
            "gate=", gate["passed"],
            "global_over=", metrics["over_aggressive_rate_vs_oracle"],
            "focus_over=", focus["over_aggressive_rate_vs_oracle"],
            "spbc2_over=", source.get("over_aggressive_rate_vs_oracle"),
            "global_u=", metrics["selected_utility_regret_vs_oracle_mean"],
            "focus_u=", focus["selected_utility_regret_vs_oracle_mean"],
            "spbc2_u=", source.get("selected_utility_regret_vs_oracle_mean"),
            "safe_rank=", metrics.get("safe_utility_rank_loss"),
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
