#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

ARCHIVE_PATH="${1:-${PHASE45_V3_NEURAL_MPC_V2_TRANSFER_ARCHIVE:-/tmp/neural_mpc_experimental_candidate_v2.tar.gz}}"

PHASE45_V3_NEURAL_MPC_TRANSFER_ARCHIVE="$ARCHIVE_PATH" \
PHASE45_V3_NEURAL_MPC_BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_V2_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v2}" \
  bash scripts/unpack_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh "$ARCHIVE_PATH"
