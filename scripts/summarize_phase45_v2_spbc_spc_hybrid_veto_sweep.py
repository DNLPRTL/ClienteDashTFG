#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping


REPORT_NAME = "reporte_validacion_spbc_spc_v2_hybrid_offline.json"


def main() -> int:
    root = Path.home() / "TFG/modelos/phase45_v1/spbc_spc_v2_hybrid_offline"
    reports = sorted(root.glob(f"veto_sweep_*/{REPORT_NAME}"))
    if not reports:
        print(f"No veto sweep reports found under: {root}")
        return 1

    rows = []
    for path in reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        design = report.get("hybrid_policy_design", {})
        prediction = report.get("spc_prediction_metrics", {})
        mode = report.get("mode_metrics", {}).get("spbc_spc_veto_only", {})
        delta = report.get("mode_deltas_vs_spbc_only", {}).get("spbc_spc_veto_only", {})
        gate = report.get("hybrid_gates", {}).get("spbc_spc_veto_only", {})
        rows.append(
            {
                "name": path.parent.name,
                "risk": design.get("risk_threshold"),
                "rb": design.get("rebuffer_threshold_s"),
                "gate": gate.get("passed"),
                "intervention": mode.get("intervention_rate"),
                "useful": mode.get("useful_intervention_rate"),
                "risk_brier": prediction.get("risk_brier"),
                "risk_fn": prediction.get("risk_false_negative_rate"),
                "global": _short_delta(delta.get("global", {})),
                "focus": _short_delta(delta.get("focus_2_5_mbps", {})),
                "spbc2": _short_delta(delta.get("spbc_v2_dpo_on_policy", {})),
            }
        )

    rows.sort(key=lambda row: (row["gate"] is not True, -(float(row["intervention"] or 0.0)), float(row["rb"] or 0.0)))
    for row in rows:
        print(
            row["name"],
            "risk=", row["risk"],
            "rb=", row["rb"],
            "gate=", row["gate"],
            "intervention=", row["intervention"],
            "useful=", row["useful"],
            "risk_brier=", row["risk_brier"],
            "risk_fn=", row["risk_fn"],
        )
        print("  global_delta=", row["global"], "focus_delta=", row["focus"], "spbc2_delta=", row["spbc2"])
    return 0


def _short_delta(delta: object) -> dict[str, float | None]:
    if not isinstance(delta, Mapping):
        return {}
    return {
        "u": delta.get("selected_utility_regret_vs_best_immediate_mean"),
        "rb": delta.get("selected_rebuffer_regret_vs_best_immediate_mean"),
        "over": delta.get("over_aggressive_rate_vs_oracle"),
        "under": delta.get("under_aggressive_rate_vs_oracle"),
    }


if __name__ == "__main__":
    raise SystemExit(main())
