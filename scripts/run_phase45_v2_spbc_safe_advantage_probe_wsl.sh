#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashPrudente"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

DATASET_DIR="${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1"
INIT_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt"
OUTPUT_ROOT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo"
SEEDS="${PHASE45_SPBC_SAFE_ADVANTAGE_SEEDS:-450891}"
EPOCHS="${PHASE45_SPBC_SAFE_ADVANTAGE_EPOCHS:-3}"

for SEED in ${SEEDS}; do
  RUN_NAME="pilot_dagger2_safe_advantage_probe_seed_${SEED}_v1"
  LOG="/tmp/phase45_v2_spbc_dpo_safe_advantage_seed_${SEED}_$(date +%Y%m%d_%H%M%S).log"
  echo "Lanzando ${RUN_NAME}; log=${LOG}"
  python3 scripts/train_phase45_v2_spbc_dpo.py \
    --profile pilot \
    --dataset-dir "${DATASET_DIR}" \
    --output-dir "${OUTPUT_ROOT}/${RUN_NAME}" \
    --init-checkpoint "${INIT_CHECKPOINT}" \
    --overwrite \
    --device auto \
    --epochs "${EPOCHS}" \
    --batch-size 1024 \
    --learning-rate 0.000025 \
    --no-profile-sample-limits \
    --seed "${SEED}" \
    --ce-loss-weight 0.02 \
    --dpo-loss-weight 0.03 \
    --ranking-loss-weight 0.03 \
    --utility-loss-weight 0.08 \
    --rebuffer-loss-weight 0.32 \
    --aux-reward-loss-weight 0.05 \
    --aux-rebuffer-loss-weight 0.08 \
    --aux-risk-loss-weight 0.08 \
    --reference-kl-loss-weight 0.80 \
    --over-aggressive-probability-loss-weight 3.20 \
    --over-aggressive-margin-loss-weight 2.10 \
    --over-aggressive-reference-excess-loss-weight 3.20 \
    --over-aggressive-margin 0.40 \
    --safe-utility-rank-loss-weight 0.20 \
    --safe-utility-margin 0.25 \
    --safe-improvement-rank-loss-weight 0.70 \
    --safe-improvement-reward-margin 0.005 \
    --copy-baseline-loss-weight 0.50 \
    --copy-baseline-reward-margin 0.005 \
    --residual-logit-l2-loss-weight 0.015 \
    --safe-advantage-policy-loss-weight 1.20 \
    --safe-advantage-reward-margin 0.005 \
    --safe-advantage-temperature 0.30 \
    --safe-advantage-rebuffer-penalty 0.45 \
    --safe-advantage-risk-penalty 0.35 \
    --decision-rebuffer-fusion-weight 0.52 \
    --decision-risk-fusion-weight 0.40 \
    --focus-bucket-sample-weight 3.20 \
    --severe-error-sample-weight 1.60 \
    --safe-vs-rebuffer-pair-weight 2.00 \
    --over-aggressive-rebuffer-action-weight 5.50 \
    --selection-focus-weight 2.50 \
    --selection-rebuffer-weight 9.20 \
    --selection-over-aggressive-weight 3.50 \
    --enable-safety-gate \
    --safety-global-over-aggressive-tolerance 0.001 \
    --safety-focus-over-aggressive-tolerance 0.002 \
    --safety-spbc-v2-over-aggressive-tolerance 0.001 \
    --safety-utility-regret-tolerance 0.0005 \
    --safety-rebuffer-regret-tolerance 0.0005 \
    2>&1 | tee "${LOG}"
  echo "Salida ${RUN_NAME}: ${LOG}"
  python3 scripts/summarize_phase45_v2_spbc_ppo_safe_pilot.py \
    --run-name "${RUN_NAME}" \
    --epochs \
    --require-trained-pass
done
