#!/usr/bin/env bash
set -euo pipefail

cd "${HOME}/TFG/ClienteDashPrudente"
git pull
source "${HOME}/venvs/rocm721/bin/activate"

LOG="/tmp/phase45_v2_spbc_dpo_anchor_safe_rank_full_v1_$(date +%Y%m%d_%H%M%S).log"

python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile full_v1 \
  --dataset-dir "${HOME}/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1" \
  --output-dir "${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1" \
  --init-checkpoint "${HOME}/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v1_utility_risk_v1/modelo_spbc_abr_v2_dpo.pt" \
  --overwrite \
  --device auto \
  --learning-rate 0.000075 \
  --utility-loss-weight 0.62 \
  --rebuffer-loss-weight 0.90 \
  --focus-bucket-sample-weight 2.35 \
  --severe-error-sample-weight 1.90 \
  --safe-vs-rebuffer-pair-weight 2.10 \
  --over-aggressive-rebuffer-action-weight 5.00 \
  --reference-kl-loss-weight 0.30 \
  --over-aggressive-probability-loss-weight 2.40 \
  --over-aggressive-margin-loss-weight 1.50 \
  --over-aggressive-reference-excess-loss-weight 2.40 \
  --over-aggressive-margin 0.40 \
  --safe-utility-rank-loss-weight 1.80 \
  --safe-utility-margin 0.25 \
  --decision-rebuffer-fusion-weight 0.52 \
  --decision-risk-fusion-weight 0.40 \
  --selection-focus-weight 2.20 \
  --selection-rebuffer-weight 9.20 \
  --selection-over-aggressive-weight 3.00 \
  --enable-safety-gate \
  --safety-global-over-aggressive-tolerance 0.006 \
  --safety-focus-over-aggressive-tolerance 0.015 \
  --safety-spbc-v2-over-aggressive-tolerance 0.012 \
  --safety-utility-regret-tolerance 0.0015 \
  --safety-rebuffer-regret-tolerance 0.0010 \
  2>&1 | tee "${LOG}"

echo "Salida full_v1: ${LOG}"
python3 scripts/summarize_phase45_v2_anchor_safe_rank_full.py
