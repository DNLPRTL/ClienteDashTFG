#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashTFG"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

python3 - <<'PY'
import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "NO_CUDA")
if not torch.cuda.is_available():
    raise SystemExit("ROCm/GPU no disponible: no se lanza entrenamiento pilot_adv_regret_hardneg_v1 en CPU.")
PY

RUN_NAME="${RUN_NAME:-qh_scorer_pilot_adv_regret_hardneg_dataset_pilot_seed450926_v1}"
LOG="/tmp/phase45_v3_qh_scorer_pilot_adv_regret_hardneg_seed450926_$(date +%Y%m%d_%H%M%S).log"

set +e
python3 scripts/train_phase45_v3_qh_scorer.py \
  --profile pilot_adv_regret_hardneg_v1 \
  --dataset-profile pilot \
  --run-name "${RUN_NAME}" \
  --device cuda \
  --overwrite \
  2>&1 | tee "${LOG}"
TRAIN_STATUS=${PIPESTATUS[0]}
set -e

echo "Salida ${RUN_NAME}: ${LOG}"
exit "${TRAIN_STATUS}"
