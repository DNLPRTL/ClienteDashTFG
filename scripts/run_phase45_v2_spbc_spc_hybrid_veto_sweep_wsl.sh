#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashTFG"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

DATASET_DIR="${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1"
SPBC_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt"
SPC_RUN="pilot_dagger2_reward_risk_anchor_ref_seed_450842_v1"
SPC_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/${SPC_RUN}/modelo_spc_abr_v2_reward_risk.pt"
OUTPUT_ROOT="${HOME}/TFG/modelos/phase45_v1/spbc_spc_v2_hybrid_offline"

for RISK in 0.35 0.45 0.50; do
  for RB in 0.00 0.03 0.05 0.10; do
    RISK_TAG="${RISK/./}"
    RB_TAG="${RB/./}"
    RUN_NAME="veto_sweep_${SPC_RUN}_risk_${RISK_TAG}_rb_${RB_TAG}"
    LOG="/tmp/phase45_v2_spbc_spc_hybrid_${RUN_NAME}_$(date +%Y%m%d_%H%M%S).log"

    if python3 scripts/validate_phase45_v2_spbc_spc_hybrid_offline.py \
      --profile pilot \
      --dataset-dir "${DATASET_DIR}" \
      --spbc-checkpoint "${SPBC_CHECKPOINT}" \
      --spc-checkpoint "${SPC_CHECKPOINT}" \
      --output-dir "${OUTPUT_ROOT}/${RUN_NAME}" \
      --overwrite \
      --device auto \
      --skip-dataset-validation \
      --risk-threshold "${RISK}" \
      --rebuffer-threshold-s "${RB}" \
      --rerank-top-k 2 \
      >"${LOG}" 2>&1; then
      echo "Sweep ${RUN_NAME}: OK log=${LOG}"
    else
      echo "Sweep ${RUN_NAME}: ERROR log=${LOG}"
      tail -80 "${LOG}"
      exit 1
    fi
  done
done

python3 scripts/summarize_phase45_v2_spbc_spc_hybrid_veto_sweep.py
