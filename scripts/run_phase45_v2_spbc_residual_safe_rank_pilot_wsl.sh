#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashTFG"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

for SEED in 450861 450862 450863; do
  LOG="/tmp/phase45_v2_spbc_dpo_residual_safe_rank_seed_${SEED}_$(date +%Y%m%d_%H%M%S).log"
  python3 scripts/train_phase45_v2_spbc_dpo.py \
    --profile pilot \
    --dataset-dir "${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1" \
    --output-dir "${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot_dagger2_residual_safe_rank_seed_${SEED}_v1" \
    --init-checkpoint "${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt" \
    --overwrite \
    --device auto \
    --epochs 6 \
    --batch-size 1024 \
    --learning-rate 0.00005 \
    --no-profile-sample-limits \
    --seed "${SEED}" \
    --utility-loss-weight 0.62 \
    --rebuffer-loss-weight 0.90 \
    --focus-bucket-sample-weight 2.35 \
    --severe-error-sample-weight 1.90 \
    --safe-vs-rebuffer-pair-weight 2.10 \
    --over-aggressive-rebuffer-action-weight 5.00 \
    --reference-kl-loss-weight 0.40 \
    --over-aggressive-probability-loss-weight 2.40 \
    --over-aggressive-margin-loss-weight 1.50 \
    --over-aggressive-reference-excess-loss-weight 2.40 \
    --over-aggressive-margin 0.40 \
    --safe-utility-rank-loss-weight 1.80 \
    --safe-utility-margin 0.25 \
    --safe-improvement-rank-loss-weight 1.20 \
    --safe-improvement-reward-margin 0.002 \
    --copy-baseline-loss-weight 0.35 \
    --copy-baseline-reward-margin 0.002 \
    --residual-logit-l2-loss-weight 0.02 \
    --decision-rebuffer-fusion-weight 0.52 \
    --decision-risk-fusion-weight 0.40 \
    --selection-focus-weight 2.20 \
    --selection-rebuffer-weight 9.20 \
    --selection-over-aggressive-weight 3.00 \
    --enable-safety-gate \
    --safety-global-over-aggressive-tolerance 0.002 \
    --safety-focus-over-aggressive-tolerance 0.004 \
    --safety-spbc-v2-over-aggressive-tolerance 0.002 \
    --safety-utility-regret-tolerance 0.0005 \
    --safety-rebuffer-regret-tolerance 0.0005 \
    2>&1 | tee "${LOG}"
  echo "Salida seed ${SEED}: ${LOG}"
done

python3 scripts/summarize_phase45_v2_spbc_residual_safe_rank_pilot.py
