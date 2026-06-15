#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DATASET_DIR="${PHASE45_V3_NEURAL_MPC_FULL_V2_DATASET_DIR:-$HOME/TFG/datasets_normalizados/phase45_v3/throughput_quantile_full_v1_neural_mpc_v2}"

DATASET_DIR="$DATASET_DIR" python3 - <<'PY'
import json
import os
from datetime import datetime, timezone
from pathlib import Path

DATASET_DIR = Path(os.environ["DATASET_DIR"]).expanduser()

THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_SAMPLING_AUDIT_FILENAME = "auditoria_muestreo_phase45_v3_throughput_quantile.json"
THROUGHPUT_QUANTILE_SUMMARY_FILENAME = "resumen_dataset_phase45_v3_throughput_quantile.json"


def read_optional_json(name):
    path = DATASET_DIR / name
    if not path.is_file():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


try:
    from core.phase45_v3.throughput_quantile_dataset import validate_phase45_v3_throughput_quantile_dataset_dir

    validation = dict(validate_phase45_v3_throughput_quantile_dataset_dir(DATASET_DIR))
except Exception as exc:  # noqa: BLE001 - this script must produce pasteable diagnostics.
    status = "ENVIRONMENT_ERROR" if type(exc).__name__ == "ModuleNotFoundError" else "NO_DATASET"
    payload = {
        "schema_id": "phase45_v3_neural_mpc_full_dataset_v2_summary_v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": status,
        "dataset_dir": str(DATASET_DIR),
        "error_type": type(exc).__name__,
        "error_message": str(exc),
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "qoe_claims_authorized": False,
        "next_step": "run bash scripts/generate_phase45_v3_neural_mpc_full_dataset_v2_wsl.sh",
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    raise SystemExit(0)

summary = read_optional_json(THROUGHPUT_QUANTILE_SUMMARY_FILENAME)
leakage = read_optional_json(THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME)
sampling_audit = read_optional_json(THROUGHPUT_QUANTILE_SAMPLING_AUDIT_FILENAME)

profile = summary.get("profile", {}) if isinstance(summary.get("profile"), dict) else {}
status = "PASS" if validation.get("status") == "PASS" and leakage.get("status") == "PASS" else "REVIEW"

payload = {
    "schema_id": "phase45_v3_neural_mpc_full_dataset_v2_summary_v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "status": status,
    "stage": "full_dataset_v2_ready_for_training" if status == "PASS" else "full_dataset_v2_review",
    "dataset_dir": str(DATASET_DIR),
    "dataset_profile": profile.get("name"),
    "profile": profile,
    "media_profile_id": summary.get("media_profile_id"),
    "horizon_segments": summary.get("horizon_segments"),
    "quantiles": summary.get("quantiles"),
    "generation_window_counts": summary.get("generation_window_counts"),
    "sample_counts": summary.get("sample_counts"),
    "validation": validation,
    "leakage_audit": {
        "status": leakage.get("status"),
        "metadata_fields_are_model_features": leakage.get("metadata_fields_are_model_features"),
        "future_throughput_as_feature": leakage.get("future_throughput_as_feature"),
        "eval_split_used": leakage.get("eval_split_used"),
    },
    "sampling_audit_status": sampling_audit.get("status"),
    "skipped_window_count": len(summary.get("skipped_windows", [])) if isinstance(summary.get("skipped_windows"), list) else None,
    "benchmark_performed": False,
    "ranking_performed": False,
    "no_final_ranking": True,
    "qoe_claims_authorized": False,
    "next_step_if_pass": "run bash scripts/run_phase45_v3_neural_mpc_full_training_v2_wsl.sh",
}

print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
PY
