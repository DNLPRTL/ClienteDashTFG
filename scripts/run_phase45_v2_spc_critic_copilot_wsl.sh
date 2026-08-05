#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashTFG"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

DATASET_DIR="${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1"
SPBC_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt"
SPC_ROOT="${HOME}/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk"
HYBRID_ROOT="${HOME}/TFG/modelos/phase45_v1/spbc_spc_v2_hybrid_offline"

for SEED in 450871 450872 450873; do
  RUN_NAME="critic_copilot_dagger2_seed_${SEED}_v1"
  SPC_OUTPUT="${SPC_ROOT}/${RUN_NAME}"
  SPC_CHECKPOINT="${SPC_OUTPUT}/modelo_spc_abr_v2_reward_risk.pt"
  TRAIN_LOG="/tmp/phase45_v2_spc_critic_copilot_train_seed_${SEED}_$(date +%Y%m%d_%H%M%S).log"

  python3 scripts/train_phase45_v2_spc_reward_risk.py \
    --profile critic_v1 \
    --dataset-dir "${DATASET_DIR}" \
    --output-dir "${SPC_OUTPUT}" \
    --reference-policy-checkpoint "${SPBC_CHECKPOINT}" \
    --overwrite \
    --device auto \
    --seed "${SEED}" \
    2>&1 | tee "${TRAIN_LOG}"
  echo "Entrenamiento ${RUN_NAME}: ${TRAIN_LOG}"

  for MODE in strict balanced risk_guard rebuffer_guard; do
    case "${MODE}" in
      strict)
        RISK="0.35"
        RB="0.03"
        ;;
      balanced)
        RISK="0.45"
        RB="0.05"
        ;;
      risk_guard)
        RISK="0.35"
        RB="0.10"
        ;;
      rebuffer_guard)
        RISK="0.50"
        RB="0.03"
        ;;
    esac

    HYBRID_RUN="${RUN_NAME}_${MODE}_k2"
    HYBRID_LOG="/tmp/phase45_v2_spc_critic_copilot_hybrid_${HYBRID_RUN}_$(date +%Y%m%d_%H%M%S).log"
    python3 scripts/validate_phase45_v2_spbc_spc_hybrid_offline.py \
      --profile pilot \
      --dataset-dir "${DATASET_DIR}" \
      --spbc-checkpoint "${SPBC_CHECKPOINT}" \
      --spc-checkpoint "${SPC_CHECKPOINT}" \
      --output-dir "${HYBRID_ROOT}/${HYBRID_RUN}" \
      --overwrite \
      --device auto \
      --skip-dataset-validation \
      --risk-threshold "${RISK}" \
      --rebuffer-threshold-s "${RB}" \
      --rerank-top-k 2 \
      --min-intervention-rate 0.001 \
      --min-useful-intervention-rate 0.10 \
      2>&1 | tee "${HYBRID_LOG}"
    echo "Evaluacion ${HYBRID_RUN}: ${HYBRID_LOG}"
  done
done

python3 scripts/summarize_phase45_v2_spc_critic_copilot.py
