#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

RUN_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1}"
MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1}"

RUN_ROOT="$RUN_ROOT" MODEL_ROOT="$MODEL_ROOT" python3 - <<'PY'
import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path

RUN_ROOT = Path(os.environ["RUN_ROOT"]).expanduser()
MODEL_ROOT = Path(os.environ["MODEL_ROOT"]).expanduser()
REPORT_NAME = "reporte_phase45_v3_neural_mpc_closedloop.json"
TRAINING_REPORT_NAME = "reporte_entrenamiento_phase45_v3_throughput_quantile.json"


def finite_float(value, default=0.0):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def gate_failed(report):
    gates = report.get("gates", {})
    failed = gates.get("failed", [])
    return list(failed) if isinstance(failed, list) else []


def training_summary(seed):
    path = MODEL_ROOT / f"seed_{seed}" / TRAINING_REPORT_NAME
    if not path.is_file():
        return {"training_report_found": False}
    report = read_json(path)
    validation = report.get("final_validation", {})
    return {
        "training_report_found": True,
        "training_status": report.get("status"),
        "model_sha256": report.get("model_sha256"),
        "pinball_loss": validation.get("pinball_loss"),
        "median_abs_log_ratio_error_p95": validation.get("median_abs_log_ratio_error_p95"),
    }


seed_rows = []
for report_path in sorted(RUN_ROOT.glob(f"seed_*/{REPORT_NAME}")):
    seed = report_path.parent.name.replace("seed_", "")
    report = read_json(report_path)
    metrics = report.get("metrics", {})
    neural = metrics.get("neural_mpc", {})
    controllers = metrics.get("controllers", {})
    neural_controller = controllers.get("neural_mpc", {})
    robust_controller = controllers.get("robust_mpc", {})
    row = {
        "seed": seed,
        "status": report.get("status"),
        "failed_gates": gate_failed(report),
        "window_count": report.get("window_count"),
        "session_count": report.get("session_count"),
        "generated_at_utc": report.get("generated_at_utc"),
        "output_dir": report.get("output_dir"),
        "neural_mpc": {
            "qoe_delta_vs_robust_mpc_mean": neural.get("qoe_delta_vs_robust_mpc_mean"),
            "rebuffer_delta_vs_robust_mpc_mean": neural.get("rebuffer_delta_vs_robust_mpc_mean"),
            "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": neural.get(
                "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"
            ),
            "bucket_2_5_mbps_qoe_delta_vs_robust_mpc_mean": neural.get(
                "bucket_2_5_mbps_qoe_delta_vs_robust_mpc_mean"
            ),
            "high_capacity_action0_rate": neural.get("high_capacity_action0_rate"),
            "high_capacity_mean_bitrate_ratio_vs_robust_mpc": neural.get(
                "high_capacity_mean_bitrate_ratio_vs_robust_mpc"
            ),
            "fallback_rate": neural.get("fallback_rate"),
            "invalid_action_count": neural.get("invalid_action_count"),
        },
        "controllers_compact": {
            "neural_mpc": {
                "qoe_linear_mean": neural_controller.get("qoe_linear_mean"),
                "total_rebuffer_s": neural_controller.get("total_rebuffer_s"),
                "mean_bitrate_kbps": neural_controller.get("mean_bitrate_kbps"),
                "action0_rate": neural_controller.get("action0_rate"),
            },
            "robust_mpc": {
                "qoe_linear_mean": robust_controller.get("qoe_linear_mean"),
                "total_rebuffer_s": robust_controller.get("total_rebuffer_s"),
                "mean_bitrate_kbps": robust_controller.get("mean_bitrate_kbps"),
                "action0_rate": robust_controller.get("action0_rate"),
            },
        },
        "training": training_summary(seed),
    }
    seed_rows.append(row)


def values(path):
    result = []
    for row in seed_rows:
        current = row
        for key in path:
            if not isinstance(current, dict):
                current = None
                break
            current = current.get(key)
        result.append(finite_float(current))
    return result


def mean(items):
    return sum(items) / len(items) if items else 0.0


status_counts = {}
failed_gate_counts = {}
for row in seed_rows:
    status = str(row.get("status"))
    status_counts[status] = status_counts.get(status, 0) + 1
    for gate in row.get("failed_gates", []):
        failed_gate_counts[str(gate)] = failed_gate_counts.get(str(gate), 0) + 1

rebuffer_2_5 = values(("neural_mpc", "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"))
qoe_delta = values(("neural_mpc", "qoe_delta_vs_robust_mpc_mean"))
fallback_rates = values(("neural_mpc", "fallback_rate"))
invalid_counts = values(("neural_mpc", "invalid_action_count"))
high_capacity_action0 = values(("neural_mpc", "high_capacity_action0_rate"))
high_capacity_ratio = values(("neural_mpc", "high_capacity_mean_bitrate_ratio_vs_robust_mpc"))

summary = {
    "schema_id": "phase45_v3_neural_mpc_expanded_diagnostic_summary_v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "diagnostic_only": True,
    "benchmark_performed": False,
    "ranking_performed": False,
    "no_final_ranking": True,
    "qoe_claims_authorized": False,
    "run_root": str(RUN_ROOT),
    "model_root": str(MODEL_ROOT),
    "report_count": len(seed_rows),
    "all_reports_passed": bool(seed_rows) and all(row.get("status") == "PASS" for row in seed_rows),
    "status_counts": status_counts,
    "failed_gate_counts": failed_gate_counts,
    "aggregate": {
        "bucket_2_5_mbps_rebuffer_delta_max": max(rebuffer_2_5) if rebuffer_2_5 else None,
        "bucket_2_5_mbps_rebuffer_delta_mean": mean(rebuffer_2_5),
        "qoe_delta_vs_robust_mpc_mean_across_seeds": mean(qoe_delta),
        "qoe_delta_vs_robust_mpc_min": min(qoe_delta) if qoe_delta else None,
        "fallback_rate_max": max(fallback_rates) if fallback_rates else None,
        "invalid_action_count_max": max(invalid_counts) if invalid_counts else None,
        "high_capacity_action0_rate_max": max(high_capacity_action0) if high_capacity_action0 else None,
        "high_capacity_mean_bitrate_ratio_min": min(high_capacity_ratio) if high_capacity_ratio else None,
    },
    "seeds": seed_rows,
}

if not seed_rows:
    summary["status"] = "NO_REPORTS"
    summary["hint"] = "Run bash scripts/run_phase45_v3_neural_mpc_expanded_diagnostic_wsl.sh first."
else:
    summary["status"] = "PASS" if summary["all_reports_passed"] else "REVIEW"

print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))
PY
