#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PHASE45_V3_NEURAL_MPC_BUNDLE_DIR="${PHASE45_V3_NEURAL_MPC_V2_BUNDLE_DIR:-$HOME/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v2}" \
PHASE45_V3_NEURAL_MPC_CONTROLLER_KEY="phase45_v3_neural_throughput_calibrated_mpc_v2" \
  bash scripts/smoke_phase45_v3_neural_mpc_runtime_controller_ubuntu_cliente.sh
