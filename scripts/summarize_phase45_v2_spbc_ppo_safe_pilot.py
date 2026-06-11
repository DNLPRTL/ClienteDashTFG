#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Mapping, Sequence


REPORT_FILENAME = "reporte_entrenamiento_spbc_abr_v2_dpo.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resume pilots PPO-safe de SPBC sin tratarlos como benchmark.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.home() / "TFG/modelos/phase45_v1/spbc_abr_v2_dpo",
        help="Raiz externa de modelos spbc_abr_v2_dpo.",
    )
    parser.add_argument(
        "--run-name",
        action="append",
        default=[],
        help="Nombre concreto de run a resumir; se puede repetir.",
    )
    parser.add_argument(
        "--epochs",
        action="store_true",
        help="Incluye una linea diagnostica por epoch entrenado con gate, deltas y checks fallidos.",
    )
    parser.add_argument(
        "--require-trained-pass",
        action="store_true",
        help="Devuelve codigo no cero si algun run no tiene epoch entrenado seleccionado y gate true.",
    )
    args = parser.parse_args(argv)

    reports = _report_paths(args.root, args.run_name)
    if not reports:
        print("No PPO-safe SPBC pilot reports found.")
        return 1

    all_trained_pass = True
    for path in reports:
        if not path.is_file():
            print(path.parent.name, "status=", "MISSING_REPORT", "report=", path)
            all_trained_pass = False
            continue
        report = json.loads(path.read_text(encoding="utf-8"))
        trained_pass = _print_report(path, report, include_epochs=bool(args.epochs))
        all_trained_pass = all_trained_pass and trained_pass

    if args.require_trained_pass and not all_trained_pass:
        return 2
    return 0


def _report_paths(root: Path, run_names: Sequence[str]) -> list[Path]:
    if run_names:
        return [root / name / REPORT_FILENAME for name in run_names]
    return sorted(root.glob("pilot_dagger2_ppo_safe_seed_*_v1/" + REPORT_FILENAME))


def _print_report(path: Path, report: Mapping[str, object], *, include_epochs: bool) -> bool:
    metrics = _mapping(report.get("validation_metrics"))
    focus = _mapping(metrics.get("focus_2_5_mbps"))
    source = _mapping(_mapping(metrics.get("by_rollout_source")).get("spbc_v2_dpo_on_policy"))
    gate = _mapping(report.get("selected_checkpoint_safety_gate"))
    comparison = _mapping(report.get("init_checkpoint_reference_comparison"))
    delta = _mapping(comparison.get("validation_delta_candidate_minus_reference"))
    focus_delta = _mapping(comparison.get("validation_focus_2_5_mbps_delta_candidate_minus_reference"))
    source_delta = _mapping(comparison.get("validation_spbc_v2_dpo_on_policy_delta_candidate_minus_reference"))
    artifacts = _mapping(report.get("artifacts"))
    best_epoch = int(report.get("best_epoch", 0))
    status = str(report.get("status", "UNKNOWN"))
    gate_passed = gate.get("passed") is True
    fallback = best_epoch == 0
    trained_pass = status == "PASS" and gate_passed and not fallback

    print(
        path.parent.name,
        "decision=",
        "TRAINED_PASS" if trained_pass else "REVIEW",
        "status=",
        status,
        "best_epoch=",
        best_epoch,
        "fallback_to_reference=",
        fallback,
        "gate=",
        gate_passed,
        "failed=",
        _failed_checks_text(gate),
        "global_over=",
        _value(metrics, "over_aggressive_rate_vs_oracle"),
        "focus_over=",
        _value(focus, "over_aggressive_rate_vs_oracle"),
        "spbc2_over=",
        _value(source, "over_aggressive_rate_vs_oracle"),
        "global_under=",
        _value(metrics, "under_aggressive_rate_vs_oracle"),
        "focus_under=",
        _value(focus, "under_aggressive_rate_vs_oracle"),
        "spbc2_under=",
        _value(source, "under_aggressive_rate_vs_oracle"),
        "global_u=",
        _value(metrics, "selected_utility_regret_vs_oracle_mean"),
        "focus_u=",
        _value(focus, "selected_utility_regret_vs_oracle_mean"),
        "spbc2_u=",
        _value(source, "selected_utility_regret_vs_oracle_mean"),
        "global_rb=",
        _value(metrics, "selected_rebuffer_regret_vs_oracle_mean"),
        "focus_rb=",
        _value(focus, "selected_rebuffer_regret_vs_oracle_mean"),
        "spbc2_rb=",
        _value(source, "selected_rebuffer_regret_vs_oracle_mean"),
        "global_bitrate=",
        _value(metrics, "predicted_bitrate_kbps_mean"),
        "focus_bitrate=",
        _value(focus, "predicted_bitrate_kbps_mean"),
        "delta_global_over=",
        _value(delta, "over_aggressive_rate_vs_oracle"),
        "delta_focus_over=",
        _value(focus_delta, "over_aggressive_rate_vs_oracle"),
        "delta_spbc2_over=",
        _value(source_delta, "over_aggressive_rate_vs_oracle"),
        "delta_global_u=",
        _value(delta, "selected_utility_regret_vs_oracle_mean"),
        "delta_focus_u=",
        _value(focus_delta, "selected_utility_regret_vs_oracle_mean"),
        "delta_spbc2_u=",
        _value(source_delta, "selected_utility_regret_vs_oracle_mean"),
        "ppo=",
        _value(metrics, "ppo_clip_loss"),
        "kl=",
        _value(metrics, "reference_kl_loss"),
        "safe_rank=",
        _value(metrics, "safe_utility_rank_loss"),
        "safe_improve=",
        _value(metrics, "safe_improvement_rank_loss"),
        "copy_base=",
        _value(metrics, "copy_baseline_loss"),
        "checkpoint=",
        artifacts.get("checkpoint", "NA"),
        "sha256=",
        artifacts.get("checkpoint_sha256", "NA"),
    )
    if include_epochs:
        _print_epoch_diagnostics(report)
    return trained_pass


def _print_epoch_diagnostics(report: Mapping[str, object]) -> None:
    for epoch in report.get("epoch_reports", []):
        if not isinstance(epoch, Mapping):
            continue
        gate = _mapping(epoch.get("validation_safety_gate"))
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
            "ppo=",
            _value(epoch, "validation_ppo_clip_loss"),
            "kl=",
            _value(epoch, "validation_reference_kl_loss"),
            "safe_rank=",
            _value(epoch, "validation_safe_utility_rank_loss"),
            "failed=",
            _failed_checks_text(gate),
        )


def _failed_checks_text(gate: Mapping[str, object]) -> str:
    raw = gate.get("failed_checks", ())
    if not isinstance(raw, list):
        return "NA"
    return ",".join(str(value) for value in raw) if raw else "none"


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _value(payload: Mapping[str, object], key: str) -> object:
    value = payload.get(key)
    if value is None:
        return "NA"
    return value


if __name__ == "__main__":
    raise SystemExit(main())
