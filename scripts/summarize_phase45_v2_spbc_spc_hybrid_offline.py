#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping


REPORT_NAME = "reporte_validacion_spbc_spc_v2_hybrid_offline.json"


def main() -> int:
    root = Path.home() / "TFG/modelos/phase45_v1/spbc_spc_v2_hybrid_offline"
    reports = sorted(root.glob(f"*/{REPORT_NAME}"))
    if not reports:
        print(f"No hybrid reports found under: {root}")
        return 1

    for path in reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        prediction = report.get("spc_prediction_metrics", {})
        modes = report.get("mode_metrics", {})
        deltas = report.get("mode_deltas_vs_spbc_only", {})
        gates = report.get("hybrid_gates", {})
        print(
            path.parent.name,
            "samples=", report.get("sample_counts_used", {}).get("validation"),
            "risk_brier=", prediction.get("risk_brier"),
            "risk_fn=", prediction.get("risk_false_negative_rate"),
            "hybrid_gate=", report.get("hybrid_candidate_gate_passed"),
        )
        spbc = modes.get("spbc_only", {})
        print(
            "  spbc_only",
            "global_u=", spbc.get("selected_utility_regret_vs_best_immediate_mean"),
            "global_rb=", spbc.get("selected_rebuffer_regret_vs_best_immediate_mean"),
            "global_over=", spbc.get("over_aggressive_rate_vs_oracle"),
            "focus_over=", _focus(spbc).get("over_aggressive_rate_vs_oracle"),
            "spbc2_over=", _spbc2(spbc).get("over_aggressive_rate_vs_oracle"),
        )
        for mode in ("spc_only_reward", "spbc_spc_veto_only", "spbc_spc_topk_rerank"):
            metrics = modes.get(mode, {})
            delta = deltas.get(mode, {})
            gate = gates.get(mode, {})
            print(
                " ",
                mode,
                "gate=", gate.get("passed"),
                "intervention=", metrics.get("intervention_rate"),
                "useful=", metrics.get("useful_intervention_rate"),
                "harmful=", metrics.get("harmful_intervention_rate"),
                "d_reward=", metrics.get("intervention_reward_delta_mean"),
                "d_rebuffer=", metrics.get("intervention_rebuffer_delta_mean"),
                "fix_over=", metrics.get("over_aggressive_fix_rate"),
                "regress_over=", metrics.get("over_aggressive_regression_rate"),
                "global_delta=", _short_delta(delta.get("global", {})),
                "focus_delta=", _short_delta(delta.get("focus_2_5_mbps", {})),
                "spbc2_delta=", _short_delta(delta.get("spbc_v2_dpo_on_policy", {})),
            )
        print("  report=", path)
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


def _focus(metrics: object) -> Mapping[str, object]:
    if isinstance(metrics, Mapping):
        focus = metrics.get("focus_2_5_mbps", {})
        if isinstance(focus, Mapping):
            return focus
    return {}


def _spbc2(metrics: object) -> Mapping[str, object]:
    if isinstance(metrics, Mapping):
        by_source = metrics.get("by_rollout_source", {})
        if isinstance(by_source, Mapping):
            source = by_source.get("spbc_v2_dpo_on_policy", {})
            if isinstance(source, Mapping):
                return source
    return {}


if __name__ == "__main__":
    raise SystemExit(main())
