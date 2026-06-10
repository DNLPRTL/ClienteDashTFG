# Runbook Phase 4-5 v2 - Entrenamiento spc_abr_v2_reward_risk

## Objetivo

Entrenar el scorer `spc_abr_v2_reward_risk` sobre el dataset externo mas
avanzado `phase45v2_preference_onpolicy_dagger2_dataset_v1`.

Este bloque no toca runtime, `player.py`, controllers, bundles ni Phase 6. No
autoriza benchmark, ranking, ganador ni afirmacion de mejora QoE.

## Entradas

Dataset DAgger-2 validado:

```bash
~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1/
```

Politica opcional para comparacion offline:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
```

SHA congelado de la politica de referencia:

```text
43b4d012448e12885fac8cbfec914aab6450e0c1b146a4bb8534e8b90b61c227
```

## Salidas externas

```bash
~/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/<profile>/
```

No commitear checkpoints, reportes, logs ni carpetas de modelos generadas.

## Sincronizacion WSL2

Daniel ejecuta esto en WSL2:

```bash
cd ~/TFG/DashClientModular4
git status --short --branch
git pull

source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

## Pilot DAgger-2 multi-seed actual

No pegar comandos largos manualmente en WSL. Usar el runner versionado:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spc_reward_risk_dagger2_pilot_wsl.sh
```

Para repetir solo el resumen:

```bash
cd ~/TFG/DashClientModular4
python3 scripts/summarize_phase45_v2_spc_reward_risk_dagger2_pilot.py
```

Este pilot usa:

```text
profile=pilot
seeds=450841,450842,450843
dataset=phase45v2_preference_onpolicy_dagger2_dataset_v1
reference_policy=spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1
sample_limits=profile
```

Aceptar solo si la mayoria de seeds mantiene senal coherente en global,
`2_5_mbps` y `spbc_v2_dpo_on_policy`, sin disparar rebuffer,
over-aggressive, under-aggressive ni `risk_false_negative_rate`. Esta salida no
es benchmark ni ranking.

## Comandos historicos/manuales

Las secciones siguientes quedan como referencia tecnica. Para ejecucion normal,
preferir los runners versionados anteriores.

## Smoke

```bash
python3 scripts/train_phase45_v2_spc_reward_risk.py \
  --profile smoke \
  --overwrite \
  --device auto
```

## Pilot recomendado

```bash
python3 scripts/train_phase45_v2_spc_reward_risk.py \
  --profile pilot \
  --output-dir ~/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/pilot_reward_risk_v1 \
  --overwrite \
  --device auto
```

## Pilot mas conservador en riesgo

Usar si el pilot sube reward pero deja demasiado rebuffer u over-aggressive,
especialmente en `2_5_mbps`.

```bash
python3 scripts/train_phase45_v2_spc_reward_risk.py \
  --profile pilot \
  --output-dir ~/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/pilot_reward_risk_conservative_v1 \
  --overwrite \
  --device auto \
  --risk-positive-weight 2.75 \
  --rebuffer-loss-weight 1.05 \
  --risk-loss-weight 1.05 \
  --score-risk-weight 0.85 \
  --score-qoe-gap-weight 0.45 \
  --focus-bucket-sample-weight 1.85 \
  --over-aggressive-rebuffer-action-weight 2.50 \
  --selection-focus-weight 1.50
```

## Full v1

No lanzarlo hasta que el pilot tenga sentido frente a `spbc_abr_v2_dpo`.

```bash
python3 scripts/train_phase45_v2_spc_reward_risk.py \
  --profile full_v1 \
  --output-dir ~/TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/full_v1_reward_risk_v1 \
  --overwrite \
  --device auto
```

## Check rapido de reporte

```bash
python3 - <<'PY'
import json
from pathlib import Path

report = Path.home() / "TFG/modelos/phase45_v1/spc_abr_v2_reward_risk/pilot_reward_risk_v1/reporte_entrenamiento_spc_abr_v2_reward_risk.json"
data = json.loads(report.read_text(encoding="utf-8"))
print(data["status"])
print(data["validation_metrics"]["selected_utility_regret_vs_best_immediate_mean"])
print(data["validation_metrics"]["selected_rebuffer_regret_vs_best_immediate_mean"])
print(data["validation_metrics"]["focus_2_5_mbps"])
print(data["reference_policy_comparison"]["available"])
print(data["benchmark_performed"], data["ranking_performed"], data["no_final_ranking"])
print(data["bundle_exported"], data["controller_registered"])
PY
```

Valores esperados de flags:

```text
False False True
False False
```

## Criterio critico

No pasar a 7D con una sola media global bonita. Revisar:

- global
- `focus_2_5_mbps`
- `by_throughput_bucket`
- `by_rollout_source`
- `by_synthetic_source`
- utility regret
- rebuffer regret
- over/under-aggressive
- risk brier y risk false negative rate
