#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping


SPC_REPORT_NAME = "reporte_entrenamiento_spc_abr_v2_reward_risk.json"
HYBRID_REPORT_NAME = "reporte_validacion_spbc_spc_v2_hybrid_offline.json"


def main() -> int:
    spc_root = Path.home() / "TFG/modelos/phase45_v1/spc_abr_v2_reward_risk"
    hybrid_root = Path.home() / "TFG/modelos/phase45_v1/spbc_spc_v2_hybrid_offline"
    training_reports = sorted(spc_root.glob(f"critic_copilot_dagger2_seed_*_v1/{SPC_REPORT_NAME}"))
    hybrid_reports = sorted(hybrid_root.glob(f"critic_copilot_dagger2_seed_*_v1_*_k2/{HYBRID_REPORT_NAME}"))

    if not training_reports:
        print(f"No critic copilot SPC training reports found under: {spc_root}")
        return 1

    print("SPC critic/coplilot training")
    for path in training_reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        validation = report.get("validation_metrics", {})
        reference = report.get("reference_policy_comparison", {})
        delta = reference.get("validation_delta_vs_scorer", {}) if isinstance(reference, Mapping) else {}
        print(
            path.parent.name,
            "status=", report.get("status"),
            "best_epoch=", report.get("best_epoch"),
            "reward_mae=", validation.get("reward_mae"),
            "rebuffer_mae=", validation.get("rebuffer_mae_s"),
            "qoe_gap_mae=", validation.get("qoe_gap_mae"),
            "risk_brier=", validation.get("risk_brier"),
            "risk_fn=", validation.get("risk_false_negative_rate"),
            "scorer_global_u=", validation.get("selected_utility_regret_vs_best_immediate_mean"),
            "scorer_global_rb=", validation.get("selected_rebuffer_regret_vs_best_immediate_mean"),
            "delta_vs_spbc_u=", _value(delta, "selected_utility_regret_vs_best_immediate_mean"),
            "delta_vs_spbc_rb=", _value(delta, "selected_rebuffer_regret_vs_best_immediate_mean"),
            "checkpoint=", report.get("artifacts", {}).get("checkpoint"),
            "sha256=", report.get("artifacts", {}).get("checkpoint_sha256"),
        )

    if not hybrid_reports:
        print(f"No critic copilot hybrid reports found under: {hybrid_root}")
        return 1

    print("SPBC driver + SPC critic offline validation")
    for path in hybrid_reports:
        report = json.loads(path.read_text(encoding="utf-8"))
        design = report.get("hybrid_policy_design", {})
        prediction = report.get("spc_prediction_metrics", {})
        gates = report.get("hybrid_gates", {})
        modes = report.get("mode_metrics", {})
        deltas = report.get("mode_deltas_vs_spbc_only", {})
        print(
            path.parent.name,
            "risk=", design.get("risk_threshold"),
            "rb=", design.get("rebuffer_threshold_s"),
            "risk_brier=", prediction.get("risk_brier"),
            "risk_fn=", prediction.get("risk_false_negative_rate"),
            "hybrid_any_gate=", report.get("hybrid_candidate_gate_passed"),
        )
        for mode in ("spbc_spc_veto_only", "spbc_spc_topk_rerank"):
            metrics = modes.get(mode, {})
            gate = gates.get(mode, {})
            delta = deltas.get(mode, {})
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


def _value(payload: object, key: str) -> object:
    if isinstance(payload, Mapping):
        return payload.get(key, "NA")
    return "NA"


if __name__ == "__main__":
    raise SystemExit(main())
