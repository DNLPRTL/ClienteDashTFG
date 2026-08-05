#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashTFG"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

RUN_NAME="${RUN_NAME:-qh_scorer_pilot_rank_dataset_pilot_seed450923_v1}"
LOG="/tmp/phase45_v3_qh_scorer_pilot_rank_$(date +%Y%m%d_%H%M%S).log"

set +e
python3 scripts/train_phase45_v3_qh_scorer.py \
  --profile pilot_rank \
  --dataset-profile pilot \
  --run-name "${RUN_NAME}" \
  --device cuda \
  --overwrite \
  2>&1 | tee "${LOG}"
TRAIN_STATUS=${PIPESTATUS[0]}
set -e

echo "Salida ${RUN_NAME}: ${LOG}"
exit "${TRAIN_STATUS}"
