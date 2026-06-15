#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1}"
ARCHIVE_PATH="${PHASE45_V3_NEURAL_MPC_TRANSFER_ARCHIVE:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1.tar.gz}"

echo "== Phase45 v3 Neural-MPC bundle transfer package: WSL2 =="
echo "benchmark_performed=false ranking_performed=false controller_integrated=false"
echo "bundle_dir=${BUNDLE_DIR}"
echo "archive_path=${ARCHIVE_PATH}"

python3 scripts/validate_phase45_v3_neural_mpc_experimental_bundle.py \
  --bundle-dir "$BUNDLE_DIR" >/dev/null

mkdir -p "$(dirname "$ARCHIVE_PATH")"
tar -C "$(dirname "$BUNDLE_DIR")" -czf "$ARCHIVE_PATH" "$(basename "$BUNDLE_DIR")"

ARCHIVE_PATH="$ARCHIVE_PATH" BUNDLE_DIR="$BUNDLE_DIR" python3 - <<'PY'
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

archive = Path(os.environ["ARCHIVE_PATH"]).expanduser()
bundle_dir = Path(os.environ["BUNDLE_DIR"]).expanduser()

digest = hashlib.sha256()
with archive.open("rb") as handle:
    for chunk in iter(lambda: handle.read(1024 * 1024), b""):
        digest.update(chunk)

payload = {
    "schema_id": "phase45_v3_neural_mpc_bundle_transfer_package_v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "status": "PASS",
    "bundle_dir": str(bundle_dir),
    "archive_path": str(archive),
    "archive_sha256": digest.hexdigest(),
    "archive_size_bytes": archive.stat().st_size,
    "benchmark_performed": False,
    "ranking_performed": False,
    "no_final_ranking": True,
    "controller_integrated": False,
    "next_step": "copy archive to Ubuntu cliente and run scripts/unpack_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh",
}
print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
PY
