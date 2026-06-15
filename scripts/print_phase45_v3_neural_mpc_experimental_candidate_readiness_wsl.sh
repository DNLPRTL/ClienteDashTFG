#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

RUN_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_RUN_ROOT:-$HOME/TFG/runs_phase45_v3/neural_mpc_expanded_diag_v1}"
MODEL_ROOT="${PHASE45_V3_NEURAL_MPC_EXPANDED_MODEL_ROOT:-$HOME/TFG/modelos/phase45_v3/throughput_quantile_predictor/expanded_diag_v1}"
CANONICAL_SEED="${PHASE45_V3_NEURAL_MPC_CANONICAL_SEED:-451001}"

RUN_ROOT="$RUN_ROOT" MODEL_ROOT="$MODEL_ROOT" CANONICAL_SEED="$CANONICAL_SEED" python3 - <<'PY'
import json
import os
from datetime import datetime, timezone
from pathlib import Path

RUN_ROOT = Path(os.environ["RUN_ROOT"]).expanduser()
MODEL_ROOT = Path(os.environ["MODEL_ROOT"]).expanduser()
CANONICAL_SEED = str(os.environ["CANONICAL_SEED"])

EVAL_REPORT = "reporte_phase45_v3_neural_mpc_closedloop.json"
TRAINING_REPORT = "reporte_entrenamiento_phase45_v3_throughput_quantile.json"
CHECKPOINT = "modelo_phase45_v3_throughput_quantile.pt"


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def failed_gates(report):
    gates = report.get("gates", {})
    failed = gates.get("failed", [])
    return list(failed) if isinstance(failed, list) else []


seeds = []
for report_path in sorted(RUN_ROOT.glob(f"seed_*/{EVAL_REPORT}")):
    seed = report_path.parent.name.replace("seed_", "")
    eval_report = read_json(report_path)
    training_path = MODEL_ROOT / f"seed_{seed}" / TRAINING_REPORT
    checkpoint_path = MODEL_ROOT / f"seed_{seed}" / CHECKPOINT
    training_report = read_json(training_path) if training_path.is_file() else {}
    metrics = eval_report.get("metrics", {}).get("neural_mpc", {})
    seeds.append(
        {
            "seed": seed,
            "evaluation_status": eval_report.get("status"),
            "failed_gates": failed_gates(eval_report),
            "window_count": eval_report.get("window_count"),
            "session_count": eval_report.get("session_count"),
            "checkpoint_path": str(checkpoint_path),
            "checkpoint_exists": checkpoint_path.is_file(),
            "model_sha256": training_report.get("model_sha256"),
            "training_status": training_report.get("status"),
            "fallback_rate": metrics.get("fallback_rate"),
            "invalid_action_count": metrics.get("invalid_action_count"),
            "high_capacity_action0_rate": metrics.get("high_capacity_action0_rate"),
            "high_capacity_mean_bitrate_ratio_vs_robust_mpc": metrics.get(
                "high_capacity_mean_bitrate_ratio_vs_robust_mpc"
            ),
            "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": metrics.get(
                "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"
            ),
            "qoe_delta_vs_robust_mpc_mean": metrics.get("qoe_delta_vs_robust_mpc_mean"),
        }
    )

canonical = next((row for row in seeds if row["seed"] == CANONICAL_SEED), None)
all_passed = bool(seeds) and all(
    row["evaluation_status"] == "PASS"
    and row["training_status"] == "PASS"
    and row["checkpoint_exists"]
    and not row["failed_gates"]
    for row in seeds
)
canonical_ready = bool(canonical) and canonical["evaluation_status"] == "PASS" and canonical["checkpoint_exists"]

payload = {
    "schema_id": "phase45_v3_neural_mpc_experimental_candidate_readiness_v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "candidate_key": "phase45_v3_neural_throughput_calibrated_mpc_v1",
    "candidate_stage": "experimental_candidate_readiness",
    "status": "READY" if all_passed and canonical_ready else "REVIEW",
    "diagnostic_only": True,
    "benchmark_performed": False,
    "ranking_performed": False,
    "no_final_ranking": True,
    "qoe_claims_authorized": False,
    "controller_integrated": False,
    "bundle_created": False,
    "run_root": str(RUN_ROOT),
    "model_root": str(MODEL_ROOT),
    "canonical_seed": CANONICAL_SEED,
    "canonical_checkpoint_path": canonical["checkpoint_path"] if canonical else None,
    "canonical_model_sha256": canonical["model_sha256"] if canonical else None,
    "all_seed_reports_passed": all_passed,
    "canonical_ready": canonical_ready,
    "seed_count": len(seeds),
    "seeds": seeds,
    "next_step_if_ready": "define external experimental bundle contract; do not integrate runtime yet",
}

print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
PY
