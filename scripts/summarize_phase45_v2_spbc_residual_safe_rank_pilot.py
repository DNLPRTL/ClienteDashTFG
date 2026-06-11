#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping


def main() -> int:
    root = Path.home() / "TFG/modelos/phase45_v1/spbc_abr_v2_dpo"
    reports = sorted(
        root.glob("pilot_dagger2_residual_safe_rank_seed_*_v1/reporte_entrenamiento_spbc_abr_v2_dpo.json")
    )
    if not reports:
        print("No residual_safe_rank pilot reports found.")
        return 1

    for path in reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        metrics = report["validation_metrics"]
        focus = metrics["focus_2_5_mbps"]
        source = metrics["by_rollout_source"].get("spbc_v2_dpo_on_policy", {})
        gate = report["selected_checkpoint_safety_gate"]
        comparison = report.get("init_checkpoint_reference_comparison", {})
        delta = comparison.get("validation_delta_candidate_minus_reference", {})
        focus_delta = comparison.get("validation_focus_2_5_mbps_delta_candidate_minus_reference", {})
        artifacts = report.get("artifacts", {})
        print(
            path.parent.name,
            "status=", report["status"],
            "best_epoch=", report["best_epoch"],
            "gate=", gate["passed"],
            "global_over=", _value(metrics, "over_aggressive_rate_vs_oracle"),
            "focus_over=", _value(focus, "over_aggressive_rate_vs_oracle"),
            "spbc2_over=", _value(source, "over_aggressive_rate_vs_oracle"),
            "global_u=", _value(metrics, "selected_utility_regret_vs_oracle_mean"),
            "focus_u=", _value(focus, "selected_utility_regret_vs_oracle_mean"),
            "spbc2_u=", _value(source, "selected_utility_regret_vs_oracle_mean"),
            "delta_global_over=", _value(delta, "over_aggressive_rate_vs_oracle"),
            "delta_focus_over=", _value(focus_delta, "over_aggressive_rate_vs_oracle"),
            "safe_rank=", _value(metrics, "safe_utility_rank_loss"),
            "safe_improve=", _value(metrics, "safe_improvement_rank_loss"),
            "copy_base=", _value(metrics, "copy_baseline_loss"),
            "residual_l2=", _value(metrics, "residual_logit_l2_loss"),
            "checkpoint=", artifacts.get("checkpoint"),
            "sha256=", artifacts.get("checkpoint_sha256"),
        )
    return 0


def _value(payload: Mapping[str, object], key: str) -> object:
    value = payload.get(key)
    if value is None:
        return "NA"
    return value


if __name__ == "__main__":
    raise SystemExit(main())
