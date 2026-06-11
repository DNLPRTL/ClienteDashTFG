#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Mapping


def main() -> int:
    parser = argparse.ArgumentParser(description="Resume pilots SPBC residual safe-rank sin tratarlos como benchmark.")
    parser.add_argument(
        "--epochs",
        action="store_true",
        help="Incluye una linea diagnostica por epoch entrenado con gate, deltas y checks fallidos.",
    )
    args = parser.parse_args()

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
        fallback = int(report["best_epoch"]) == 0
        print(
            path.parent.name,
            "status=", report["status"],
            "best_epoch=", report["best_epoch"],
            "fallback_to_reference=", fallback,
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
        if args.epochs:
            _print_epoch_diagnostics(report)
    return 0


def _print_epoch_diagnostics(report: Mapping[str, object]) -> None:
    for epoch in report.get("epoch_reports", []):
        if not isinstance(epoch, Mapping):
            continue
        gate = epoch.get("validation_safety_gate", {})
        failed = _failed_checks(gate if isinstance(gate, Mapping) else {})
        print(
            "  epoch=",
            epoch.get("epoch"),
            "gate=",
            epoch.get("validation_safety_gate_passed"),
            "selection=",
            _value(epoch, "validation_selection_score"),
            "global_over=",
            _value(epoch, "validation_over_aggressive_rate_vs_oracle"),
            "focus_over=",
            _value(epoch, "validation_focus_2_5_mbps_over_aggressive_rate_vs_oracle"),
            "spbc2_over=",
            _value(epoch, "validation_spbc_v2_dpo_on_policy_over_aggressive_rate_vs_oracle"),
            "global_u=",
            _value(epoch, "validation_selected_utility_regret_vs_oracle_mean"),
            "focus_u=",
            _value(epoch, "validation_focus_2_5_mbps_selected_utility_regret_vs_oracle_mean"),
            "spbc2_u=",
            _value(epoch, "validation_spbc_v2_dpo_on_policy_selected_utility_regret_vs_oracle_mean"),
            "safe_improve=",
            _value(epoch, "validation_safe_improvement_rank_loss"),
            "copy_base=",
            _value(epoch, "validation_copy_baseline_loss"),
            "residual_l2=",
            _value(epoch, "validation_residual_logit_l2_loss"),
            "failed=",
            ",".join(failed) if failed else "none",
        )


def _failed_checks(gate: Mapping[str, object]) -> tuple[str, ...]:
    raw = gate.get("failed_checks", ())
    if not isinstance(raw, list):
        return ()
    return tuple(str(value) for value in raw)


def _value(payload: Mapping[str, object], key: str) -> object:
    value = payload.get(key)
    if value is None:
        return "NA"
    return value


if __name__ == "__main__":
    raise SystemExit(main())
