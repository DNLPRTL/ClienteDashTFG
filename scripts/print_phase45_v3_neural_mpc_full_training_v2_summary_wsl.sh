#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_FULL_V2_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/full_v1_neural_mpc_v2}"
RUN_ROOT="${PHASE45_V3_NEURAL_MPC_FULL_V2_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_full_v1_v2}"
REBUFFER_SPIKE_DELTA_WARN_S="${PHASE45_V3_NEURAL_MPC_FULL_V2_REBUFFER_SPIKE_DELTA_WARN_S:-4.0}"
QOE_DROP_WARN="${PHASE45_V3_NEURAL_MPC_FULL_V2_QOE_DROP_WARN:--1.0}"

MODEL_ROOT="$MODEL_ROOT" RUN_ROOT="$RUN_ROOT" REBUFFER_SPIKE_DELTA_WARN_S="$REBUFFER_SPIKE_DELTA_WARN_S" QOE_DROP_WARN="$QOE_DROP_WARN" python3 - <<'PY'
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path

MODEL_ROOT = Path(os.environ["MODEL_ROOT"]).expanduser()
RUN_ROOT = Path(os.environ["RUN_ROOT"]).expanduser()
REBUFFER_SPIKE_DELTA_WARN_S = float(os.environ["REBUFFER_SPIKE_DELTA_WARN_S"])
QOE_DROP_WARN = float(os.environ["QOE_DROP_WARN"])

EVAL_REPORT = "reporte_phase45_v3_neural_mpc_closedloop.json"
TRAINING_REPORT = "reporte_entrenamiento_phase45_v3_throughput_quantile.json"
CHECKPOINT = "modelo_phase45_v3_throughput_quantile.pt"


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def finite_float(value, default=0.0):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def failed_gates(report):
    gates = report.get("gates", {})
    failed = gates.get("failed", [])
    return list(failed) if isinstance(failed, list) else []


def paired_deltas(report):
    paired = report.get("metrics", {}).get("paired_vs_robust_mpc", {})
    rows = paired.get("paired_deltas", [])
    return rows if isinstance(rows, list) else []


def worst_by(rows, key, reverse=False):
    clean = [row for row in rows if isinstance(row, dict) and row.get(key) is not None]
    if not clean:
        return None
    return sorted(clean, key=lambda row: finite_float(row.get(key)), reverse=reverse)[0]


seed_rows = []
for training_path in sorted(MODEL_ROOT.glob(f"seed_*/{TRAINING_REPORT}")):
    seed = training_path.parent.name.replace("seed_", "")
    model_dir = training_path.parent
    run_dir = RUN_ROOT / f"seed_{seed}"
    eval_path = run_dir / EVAL_REPORT
    checkpoint_path = model_dir / CHECKPOINT
    training = read_json(training_path)
    eval_report = read_json(eval_path) if eval_path.is_file() else {}
    metrics = eval_report.get("metrics", {}).get("neural_mpc", {})
    controllers = eval_report.get("metrics", {}).get("controllers", {})
    neural_controller = controllers.get("neural_mpc", {})
    robust_controller = controllers.get("robust_mpc", {})
    paired = paired_deltas(eval_report)
    worst_qoe = worst_by(paired, "qoe_delta")
    worst_rebuffer = worst_by(paired, "rebuffer_delta_s", reverse=True)
    max_rebuffer_delta = finite_float((worst_rebuffer or {}).get("rebuffer_delta_s"))
    min_qoe_delta = finite_float((worst_qoe or {}).get("qoe_delta"))
    warnings = []
    if max_rebuffer_delta > REBUFFER_SPIKE_DELTA_WARN_S:
        warnings.append("paired_rebuffer_spike_vs_robust_mpc")
    if min_qoe_delta < QOE_DROP_WARN:
        warnings.append("paired_qoe_drop_vs_robust_mpc")
    seed_rows.append(
        {
            "seed": seed,
            "training_status": training.get("status"),
            "evaluation_status": eval_report.get("status"),
            "failed_gates": failed_gates(eval_report),
            "checkpoint_path": str(checkpoint_path),
            "checkpoint_exists": checkpoint_path.is_file(),
            "model_sha256": training.get("model_sha256"),
            "training_profile": training.get("profile", {}).get("name") if isinstance(training.get("profile"), dict) else None,
            "final_validation": training.get("final_validation"),
            "window_count": eval_report.get("window_count"),
            "session_count": eval_report.get("session_count"),
            "neural_mpc": {
                "qoe_delta_vs_robust_mpc_mean": metrics.get("qoe_delta_vs_robust_mpc_mean"),
                "rebuffer_delta_vs_robust_mpc_mean": metrics.get("rebuffer_delta_vs_robust_mpc_mean"),
                "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": metrics.get(
                    "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"
                ),
                "fallback_rate": metrics.get("fallback_rate"),
                "invalid_action_count": metrics.get("invalid_action_count"),
                "high_capacity_action0_rate": metrics.get("high_capacity_action0_rate"),
                "high_capacity_mean_bitrate_ratio_vs_robust_mpc": metrics.get(
                    "high_capacity_mean_bitrate_ratio_vs_robust_mpc"
                ),
            },
            "controllers_compact": {
                "neural_mpc": {
                    "qoe_linear_mean": neural_controller.get("qoe_linear_mean"),
                    "total_rebuffer_s": neural_controller.get("total_rebuffer_s"),
                    "mean_bitrate_kbps": neural_controller.get("mean_bitrate_kbps"),
                },
                "robust_mpc": {
                    "qoe_linear_mean": robust_controller.get("qoe_linear_mean"),
                    "total_rebuffer_s": robust_controller.get("total_rebuffer_s"),
                    "mean_bitrate_kbps": robust_controller.get("mean_bitrate_kbps"),
                },
            },
            "paired_risk_audit": {
                "paired_count": len(paired),
                "worst_qoe_delta": worst_qoe,
                "worst_rebuffer_delta": worst_rebuffer,
                "max_rebuffer_delta_s": max_rebuffer_delta,
                "min_qoe_delta": min_qoe_delta,
                "warnings": warnings,
            },
        }
    )

all_passed = bool(seed_rows) and all(
    row["training_status"] == "PASS"
    and row["evaluation_status"] == "PASS"
    and row["checkpoint_exists"]
    and not row["failed_gates"]
    for row in seed_rows
)
warnings = sorted({warning for row in seed_rows for warning in row["paired_risk_audit"]["warnings"]})
status = "NO_REPORTS"
decision = "RUN_FULL_TRAINING_V2"
if seed_rows:
    status = "PASS" if all_passed and not warnings else "REVIEW"
    decision = "READY_TO_EXPORT_BUNDLE_V2" if status == "PASS" else "REVIEW_BEFORE_BUNDLE_V2"

payload = {
    "schema_id": "phase45_v3_neural_mpc_full_training_v2_summary_v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "status": status,
    "decision": decision,
    "diagnostic_only": True,
    "benchmark_performed": False,
    "ranking_performed": False,
    "no_final_ranking": True,
    "qoe_claims_authorized": False,
    "model_root": str(MODEL_ROOT),
    "run_root": str(RUN_ROOT),
    "seed_count": len(seed_rows),
    "all_seed_reports_passed": all_passed,
    "custom_review_rules": {
        "rebuffer_spike_delta_warn_s": REBUFFER_SPIKE_DELTA_WARN_S,
        "qoe_drop_warn": QOE_DROP_WARN,
        "warnings": warnings,
    },
    "seeds": seed_rows,
    "next_step_if_pass": "export bundle v2, validate in Ubuntu cliente, then run Phase 6 diagnostico/rapido against v1 and v2",
}

print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
PY
