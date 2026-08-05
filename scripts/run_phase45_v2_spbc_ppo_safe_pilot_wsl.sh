#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashPrudente"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

DATASET_DIR="${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1"
INIT_CHECKPOINT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt"
OUTPUT_ROOT="${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo"
SEEDS="${PHASE45_SPBC_PPO_SEEDS:-450881 450882 450883}"
EPOCHS="${PHASE45_SPBC_PPO_EPOCHS:-4}"

for SEED in ${SEEDS}; do
  RUN_NAME="pilot_dagger2_ppo_safe_seed_${SEED}_v1"
  LOG="/tmp/phase45_v2_spbc_dpo_ppo_safe_seed_${SEED}_$(date +%Y%m%d_%H%M%S).log"
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
    --learning-rate 0.00003 \
    --no-profile-sample-limits \
    --seed "${SEED}" \
    --ce-loss-weight 0.03 \
    --dpo-loss-weight 0.05 \
    --ranking-loss-weight 0.05 \
    --utility-loss-weight 0.20 \
    --rebuffer-loss-weight 0.50 \
    --aux-reward-loss-weight 0.05 \
    --aux-rebuffer-loss-weight 0.08 \
    --aux-risk-loss-weight 0.08 \
    --reference-kl-loss-weight 0.90 \
    --over-aggressive-probability-loss-weight 2.80 \
    --over-aggressive-margin-loss-weight 1.80 \
    --over-aggressive-reference-excess-loss-weight 2.80 \
    --over-aggressive-margin 0.40 \
    --safe-utility-rank-loss-weight 0.60 \
    --safe-utility-margin 0.25 \
    --ppo-clip-loss-weight 1.00 \
    --ppo-clip-epsilon 0.06 \
    --ppo-advantage-clip 1.50 \
    --ppo-over-aggressive-advantage-penalty 2.50 \
    --ppo-rebuffer-advantage-penalty 0.35 \
    --ppo-risk-advantage-penalty 0.25 \
    --decision-rebuffer-fusion-weight 0.52 \
    --decision-risk-fusion-weight 0.40 \
    --selection-focus-weight 2.20 \
    --selection-rebuffer-weight 9.20 \
    --selection-over-aggressive-weight 3.00 \
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
    --require-trained-pass
done

python3 scripts/summarize_phase45_v2_spbc_ppo_safe_pilot.py --epochs
