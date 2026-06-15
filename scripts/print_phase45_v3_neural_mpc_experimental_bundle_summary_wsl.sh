#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1}"

BUNDLE_DIR="$BUNDLE_DIR" python3 - <<'PY'
import json
import os
from datetime import datetime, timezone
from pathlib import Path

BUNDLE_DIR = Path(os.environ["BUNDLE_DIR"]).expanduser()
MANIFEST = "manifiesto_bundle_neural_mpc_phase45_v3.json"
REPORT = "reporte_export_bundle_neural_mpc_phase45_v3.json"


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


manifest_path = BUNDLE_DIR / MANIFEST
report_path = BUNDLE_DIR / REPORT

if not manifest_path.is_file() or not report_path.is_file():
    print(
        json.dumps(
            {
                "schema_id": "phase45_v3_neural_mpc_experimental_bundle_summary_v1",
                "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "status": "NO_BUNDLE",
                "bundle_dir": str(BUNDLE_DIR),
                "missing": [
                    str(path)
                    for path in (manifest_path, report_path)
                    if not path.is_file()
                ],
                "next_step": "run bash scripts/export_phase45_v3_neural_mpc_experimental_bundle_wsl.sh",
            },
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    raise SystemExit(0)

manifest = read_json(manifest_path)
report = read_json(report_path)
readiness = manifest.get("readiness", {})
files = manifest.get("files", {})

payload = {
    "schema_id": "phase45_v3_neural_mpc_experimental_bundle_summary_v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "status": report.get("status"),
    "decision": report.get("decision"),
    "bundle_dir": str(BUNDLE_DIR),
    "candidate_key": manifest.get("candidate_key"),
    "controller_key": manifest.get("controller_key"),
    "model_key": manifest.get("model_key"),
    "canonical_seed": manifest.get("canonical_seed"),
    "canonical_model_sha256": manifest.get("source_checkpoint_sha256"),
    "bundle_created": report.get("bundle_created"),
    "controller_integrated": report.get("controller_integrated"),
    "diagnostic_only": report.get("diagnostic_only"),
    "phase6_formal_evaluation_performed": report.get("phase6_formal_evaluation_performed"),
    "benchmark_performed": report.get("benchmark_performed"),
    "ranking_performed": report.get("ranking_performed"),
    "no_final_ranking": report.get("no_final_ranking"),
    "qoe_claims_authorized": report.get("qoe_claims_authorized"),
    "seed_count": readiness.get("seed_count"),
    "all_seed_reports_passed": readiness.get("all_seed_reports_passed"),
    "canonical_ready": readiness.get("canonical_ready"),
    "required_files": manifest.get("required_files"),
    "file_hashes": {
        name: {
            "sha256": row.get("sha256"),
            "size_bytes": row.get("size_bytes"),
        }
        for name, row in sorted(files.items())
    },
    "next_step_if_accepted": "validate this external bundle in Ubuntu cliente; do not claim benchmark yet",
}

print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
PY
