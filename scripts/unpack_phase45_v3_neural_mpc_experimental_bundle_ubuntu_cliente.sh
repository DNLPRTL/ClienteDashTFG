#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

ARCHIVE_PATH="${1:-${PHASE45_V3_NEURAL_MPC_TRANSFER_ARCHIVE:-/tmp/neural_mpc_experimental_candidate_v1.tar.gz}}"
TARGET_ROOT="${PHASE45_V3_NEURAL_MPC_TARGET_ROOT:-$HOME/TFG/modelos/phase45_v3}"
BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_BUNDLE_DIR:-$TARGET_ROOT/neural_mpc_experimental_candidate_v1}"

echo "== Phase45 v3 Neural-MPC bundle unpack: Ubuntu cliente =="
echo "benchmark_performed=false ranking_performed=false controller_integrated=false"
echo "archive_path=${ARCHIVE_PATH}"
echo "target_root=${TARGET_ROOT}"
echo "bundle_dir=${BUNDLE_DIR}"

if [ ! -f "$ARCHIVE_PATH" ]; then
  echo "Archive not found: ${ARCHIVE_PATH}" >&2
  exit 2
fi

mkdir -p "$TARGET_ROOT"
tar -C "$TARGET_ROOT" -xzf "$ARCHIVE_PATH"

PHASE45_V3_NEURAL_MPC_BUNDLE_DIR="$BUNDLE_DIR" \
  bash scripts/validate_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh
