#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PHASE45_V3_NEURAL_MPC_BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_V2_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v2}" \
  bash scripts/print_phase45_v3_neural_mpc_experimental_bundle_summary_wsl.sh
