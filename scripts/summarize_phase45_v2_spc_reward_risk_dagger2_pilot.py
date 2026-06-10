#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


REPORT_NAME = "reporte_entrenamiento_spc_abr_v2_reward_risk.json"


def main() -> int:
    root = Path.home() / "TFG/modelos/phase45_v1/spc_abr_v2_reward_risk"
    reports = sorted(root.glob(f"pilot_dagger2_reward_risk_anchor_ref_seed_*_v1/{REPORT_NAME}"))
    if not reports:
        print(f"No reports found under: {root}")
        return 1

    for path in reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        metrics = report["validation_metrics"]
        focus = metrics.get("focus_2_5_mbps", {})
        spbc2 = metrics.get("by_rollout_source", {}).get("spbc_v2_dpo_on_policy", {})
        reference = report.get("reference_policy_comparison", {})
        delta = reference.get("validation_delta_vs_scorer", {}) if reference.get("available") else {}
        artifacts = report.get("artifacts", {})

        print(
            path.parent.name,
            "best_epoch=", report.get("best_epoch"),
            "global_u_bi=", metrics.get("selected_utility_regret_vs_best_immediate_mean"),
            "global_rb_bi=", metrics.get("selected_rebuffer_regret_vs_best_immediate_mean"),
            "global_over=", metrics.get("over_aggressive_rate_vs_oracle"),
            "global_under=", metrics.get("under_aggressive_rate_vs_oracle"),
            "focus_u_bi=", focus.get("selected_utility_regret_vs_best_immediate_mean"),
            "focus_rb_bi=", focus.get("selected_rebuffer_regret_vs_best_immediate_mean"),
            "focus_over=", focus.get("over_aggressive_rate_vs_oracle"),
            "focus_under=", focus.get("under_aggressive_rate_vs_oracle"),
            "spbc2_u_bi=", spbc2.get("selected_utility_regret_vs_best_immediate_mean"),
            "spbc2_rb_bi=", spbc2.get("selected_rebuffer_regret_vs_best_immediate_mean"),
            "spbc2_over=", spbc2.get("over_aggressive_rate_vs_oracle"),
            "risk_brier=", metrics.get("risk_brier"),
            "risk_fn=", metrics.get("risk_false_negative_rate"),
        )
        print(
            "  reference_available=",
            reference.get("available"),
            "reference_sha256=",
            reference.get("checkpoint_sha256"),
        )
        print(
            "  delta_scorer_minus_reference=",
            {
                "utility_regret": delta.get("selected_utility_regret_vs_best_immediate_mean"),
                "rebuffer_regret": delta.get("selected_rebuffer_regret_vs_best_immediate_mean"),
                "over": delta.get("over_aggressive_rate_vs_oracle"),
                "under": delta.get("under_aggressive_rate_vs_oracle"),
                "risk_rate": delta.get("predicted_target_risk_rate"),
            },
        )
        print("  checkpoint=", artifacts.get("checkpoint"))
        print("  checkpoint_sha256=", artifacts.get("checkpoint_sha256"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
