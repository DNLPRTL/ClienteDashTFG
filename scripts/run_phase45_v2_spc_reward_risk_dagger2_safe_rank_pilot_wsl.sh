#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashPrudente"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

for SEED in 450851 450852 450853; do
  LOG="/tmp/phase45_v2_spc_reward_risk_dagger2_safe_rank_seed_${SEED}_$(date +%Y%m%d_%H%M%S).log"
  python3 scripts/train_phase45_v2_spc_reward_risk.py \
    --profile pilot \
    --dataset-dir "${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1" \
    --output-dir "${HOME}/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/pilot_dagger2_reward_risk_safe_rank_seed_${SEED}_v2" \
    --reference-policy-checkpoint "${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt" \
    --overwrite \
    --device auto \
    --epochs 12 \
    --batch-size 1024 \
    --learning-rate 0.00040 \
    --seed "${SEED}" \
    --best-immediate-ce-loss-weight 0.22 \
    --pairwise-score-loss-weight 0.44 \
    --reward-loss-weight 1.10 \
    --rebuffer-loss-weight 0.95 \
    --qoe-gap-loss-weight 0.70 \
    --smoothness-loss-weight 0.22 \
    --risk-loss-weight 1.00 \
    --score-rebuffer-weight 4.30 \
    --score-risk-weight 0.58 \
    --score-smoothness-weight 0.20 \
    --score-qoe-gap-weight 0.32 \
    --pairwise-margin-scale 0.20 \
    --risk-positive-weight 2.40 \
    --focus-bucket-sample-weight 2.10 \
    --severe-error-sample-weight 1.75 \
    --safe-vs-rebuffer-pair-weight 2.20 \
    --over-aggressive-rebuffer-action-weight 3.50 \
    --over-aggressive-score-loss-weight 1.60 \
    --safe-utility-rank-loss-weight 1.30 \
    --safe-utility-margin 0.22 \
    --max-pair-weight 6.00 \
    --selection-focus-weight 2.00 \
    --selection-rebuffer-weight 4.80 \
    --selection-over-aggressive-weight 2.00 \
    --selection-invalid-weight 10.00 \
    --selection-prediction-loss-weight 0.04 \
    2>&1 | tee "${LOG}"
  echo "Salida seed ${SEED}: ${LOG}"
done

python3 scripts/summarize_phase45_v2_spc_reward_risk_dagger2_pilot.py
