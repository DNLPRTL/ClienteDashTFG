#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/DashClientModular4"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

DATASET_DIR="${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1"
SPBC_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt"
OUTPUT_ROOT="${HOME}/TFG/modelos/phase45_v1/spbc_spc_v2_hybrid_offline"

for SEED in 450841 450842 450843; do
  SPC_RUN="pilot_dagger2_reward_risk_anchor_ref_seed_${SEED}_v1"
  SPC_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/${SPC_RUN}/modelo_spc_abr_v2_reward_risk.pt"
  LOG="/tmp/phase45_v2_spbc_spc_hybrid_${SPC_RUN}_$(date +%Y%m%d_%H%M%S).log"

  python3 scripts/validate_phase45_v2_spbc_spc_hybrid_offline.py \
    --profile pilot \
    --dataset-dir "${DATASET_DIR}" \
    --spbc-checkpoint "${SPBC_CHECKPOINT}" \
    --spc-checkpoint "${SPC_CHECKPOINT}" \
    --output-dir "${OUTPUT_ROOT}/${SPC_RUN}" \
    --overwrite \
    --device auto \
    --risk-threshold 0.50 \
    --rebuffer-threshold-s 0.10 \
    --rerank-top-k 2 \
    2>&1 | tee "${LOG}"
  echo "Salida ${SPC_RUN}: ${LOG}"
done

python3 scripts/summarize_phase45_v2_spbc_spc_hybrid_offline.py
