# Runbook Phase 4-5 v2 - Entrenamiento spbc_abr_v2_dpo

## Objetivo

Entrenar la politica base `spbc_abr_v2_dpo` sobre el dataset externo
`phase45v2_preference_onpolicy_dataset_v1`.

Este bloque no toca runtime, `player.py`, controllers, bundles ni Phase 6. Sus
salidas son checkpoints candidatos offline y auditorias de entrenamiento. No
autoriza benchmark, ranking, ganador ni afirmacion de mejora QoE.

## Entradas

Dataset v2 validado:

```bash
~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dataset_v1/
```

Referencia congelada por defecto:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v1/full_v1/modelo_spbc_abr_v1.pt
```

## Salidas externas

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/<profile>/
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

La salida esperada del entorno GPU actual es `True` y la GPU AMD expuesta por
ROCm.

## Validar dataset v2 existente

```bash
python3 scripts/build_phase45_v2_dataset.py \
  --validate-only \
  --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dataset_v1
```

Debe terminar con:

```json
{
  "status": "PASS"
}
```

## Smoke

```bash
python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile smoke \
  --overwrite \
  --device auto
```

Salida esperada:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/smoke/
```

## Pilot

```bash
python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile pilot \
  --overwrite \
  --device auto
```

Salida esperada:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot/
```

## Pilot utility-aware 7B.2 recomendado

Este run usa el objetivo ampliado tras los pilots iniciales: CE queda como
ancla, y la loss incorpora utilidad soft por `reward_n`, penalizacion esperada
de rebuffer y pesos para `2_5_mbps`/errores graves.

```bash
python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile pilot \
  --output-dir ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot_utility_v1 \
  --overwrite \
  --device auto
```

Si hace falta endurecer aun mas el rebuffer en `2_5_mbps`, usar una variante
explícita:

```bash
python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile pilot \
  --output-dir ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot_utility_focus_v1 \
  --overwrite \
  --device auto \
  --utility-loss-weight 0.65 \
  --rebuffer-loss-weight 0.65 \
  --focus-bucket-sample-weight 1.75 \
  --over-aggressive-rebuffer-action-weight 2.25
```

No pasar a `full_v1` si `focus_2_5_mbps` mejora `top1` pero empeora
`selected_utility_regret_vs_best_immediate_mean`,
`selected_rebuffer_regret_vs_best_immediate_mean`, over-aggressive o rebuffer.

## Full v1

```bash
python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile full_v1 \
  --overwrite \
  --device auto
```

`full_v1` falla si no existe la referencia `spbc_abr_v1/full_v1`, salvo flag
explicita:

```bash
python3 scripts/train_phase45_v2_spbc_dpo.py \
  --profile full_v1 \
  --overwrite \
  --device auto \
  --allow-random-init-full
```

No usar esa excepcion para resultados principales; solo sirve como diagnostico
si falta el checkpoint de referencia.

## Check rapido de reporte

```bash
python3 - <<'PY'
import json
from pathlib import Path

report = Path.home() / "TFG/modelos/phase45_v1/spbc_abr_v2_dpo/smoke/reporte_entrenamiento_spbc_abr_v2_dpo.json"
data = json.loads(report.read_text(encoding="utf-8"))
print(data["status"])
print(data["reference_policy_source"])
print(data["validation_metrics"]["focus_2_5_mbps"])
print(data["spbc_v1_reference_comparison"]["available"])
print(data["benchmark_performed"], data["ranking_performed"], data["no_final_ranking"])
print(data["bundle_exported"], data["controller_registered"])
PY
```

Valores esperados:

```text
PASS
spbc_abr_v1_full_v1_frozen_checkpoint
...
True
False False True
False False
```

## Contrato

- El forward del modelo consume solo `model_inputs.context`,
  `model_inputs.candidates` y `action_mask`.
- `preference_pairs`, `per_action_outcomes`, `qoe_gap`, `reward_n`,
  `rollout_source` y `metadata` son targets/auditoria, nunca inputs.
- DPO usa pares `preferred/rejected` con la formula:
  `-logsigmoid(beta * ((logp_theta(pref)-logp_theta(rej)) - (logp_ref(pref)-logp_ref(rej))))`.
- La referencia por defecto es `spbc_abr_v1/full_v1` congelada.
- La loss total combina CE contra `oracle_action`, DPO ponderado por gaps
  normalizados/capados, ranking/soft utility, distribucion soft por `reward_n`
  y penalizacion esperada de rebuffer.
- El reporte incluye metricas globales, por `throughput_bucket`, por
  `rollout_source`, foco `2_5_mbps`, selected utility regret y selected
  rebuffer regret contra oracle y mejor accion inmediata.
- Las banderas obligatorias se mantienen:
  `benchmark_performed=false`, `ranking_performed=false`,
  `no_final_ranking=true`, `bundle_exported=false`,
  `controller_registered=false`.
