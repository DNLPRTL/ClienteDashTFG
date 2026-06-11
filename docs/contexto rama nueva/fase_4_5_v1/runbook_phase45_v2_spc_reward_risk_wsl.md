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

Resultado observado: el pilot `anchor_ref` v1 no se escala. Las tres seeds
mejoraron ligeramente rebuffer regret frente al SPBC congelado, pero empeoraron
utility regret y over-aggressive. El foco `2_5_mbps` mantuvo
`over_aggressive=0.031790..0.041975`, demasiado alto para cerrar candidato.

## Pilot DAgger-2 safe-rank v2

El siguiente intento aplica lo aprendido del SPBC `anchor_safe_rank`: ademas de
predecir reward/rebuffer/riesgo, fuerza que el score ordene mejor dentro del
conjunto seguro y penaliza masa de score sobre acciones `over_aggressive`.

Ejecutar con runner versionado:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spc_reward_risk_dagger2_safe_rank_pilot_wsl.sh
```

Para repetir solo el resumen:

```bash
cd ~/TFG/DashClientModular4
python3 scripts/summarize_phase45_v2_spc_reward_risk_dagger2_pilot.py
```

Aceptar solo si la mayoria de seeds mejora o al menos no empeora frente al SPBC
congelado en utility regret y over-aggressive, conserva la mejora de rebuffer y
no rompe `2_5_mbps`, `spbc_v2_dpo_on_policy`, `risk_brier` ni
`risk_false_negative_rate`. Si la v2 vuelve a comprar rebuffer con mas utility
regret u over-aggressive, no lanzar full.

Resultado observado: el pilot `safe-rank` v2 no se escala. Dos seeds
seleccionaron `best_epoch=1`, `risk_brier` subio a `0.152982` y `0.147532`, y
las tres seeds empeoraron utility regret, rebuffer regret y over-aggressive
frente al SPBC congelado. La causa probable es que las nuevas perdidas empujan
un score compuesto y deforman las cabezas predictivas.

## Reinicio SPC 2026-06-11 - critico, no segundo conductor

Tras revisar los informes externos y los pilots v1/v2, el siguiente paso no es
otro entrenamiento largo para demostrar que `SPC solo` gana al SPBC. La
hipotesis activa es:

```text
SPBC = conductor / policy decisora
SPC  = copiloto / critico predictivo por accion
```

Por tanto, el siguiente bloque operativo debe implementar primero una evaluacion
offline hibrida. Debe comparar:

```text
SPBC only
SPC only reward-only
SPBC + SPC veto-only conservador
SPBC top-k + SPC rerank con restricciones
```

`SPC only reward-only` queda como diagnostico, no como criterio principal de
aceptacion. El criterio fuerte es que `SPBC + SPC` ayude al conductor sin romper
global, `2_5_mbps` ni `spbc_v2_dpo_on_policy`.

### Runner hibrido offline

No ejecutar todavia un runner de entrenamiento `reward-only`: primero se evalua
si las seeds v1 del SPC sirven como copiloto del SPBC congelado.

Ejecutar en WSL2:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spbc_spc_hybrid_offline_wsl.sh
```

El runner versionado es:

```text
scripts/run_phase45_v2_spbc_spc_hybrid_offline_wsl.sh
```

Ese runner debe usar:

```text
SPBC congelado:
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt

SPC candidates iniciales:
pilot_dagger2_reward_risk_anchor_ref_seed_450841_v1
pilot_dagger2_reward_risk_anchor_ref_seed_450842_v1
pilot_dagger2_reward_risk_anchor_ref_seed_450843_v1
```

Usar primero las seeds v1 como criticos es intencionado: no fueron buenas como
policy autonoma, pero dos seeds conservaron calibracion de riesgo sana. Si el
evaluador hibrido muestra que el copiloto puede intervenir poco y bien, entonces
tiene sentido entrenar despues un `SPC reward-only calibrated` nuevo.

### Gates del hibrido

La aceptacion interna exige mirar global, `2_5_mbps` y
`spbc_v2_dpo_on_policy`:

- no empeorar `over_aggressive` frente a `SPBC only`
- no empeorar `selected_rebuffer_regret_vs_best_immediate_mean`
- aceptar solo degradacion minima y explicita de utility regret si reduce
  seguridad/rebuffer de forma estable
- mantener `risk_brier` y `risk_false_negative_rate` en banda sana
- reportar `intervention_rate` y `useful_intervention_rate`

Si el hibrido no aporta con las seeds v1, el siguiente entrenamiento
`reward-only calibrated` debe redisenarse como predictor/calibrador: ranking por
`predicted_reward_n_by_action`, rebuffer/riesgo como restricciones y sin
perdidas fuertes sobre score compuesto.

### Barrido de veto-only

Tras el primer hibrido, si `veto_only` es el unico modo con senal sana pero
interviene muy poco, ejecutar un barrido barato de umbrales sobre la seed con
mejor gate/calibracion:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spbc_spc_hybrid_veto_sweep_wsl.sh
```

Este runner no entrena. Evalua `pilot_dagger2_reward_risk_anchor_ref_seed_450842_v1`
con varias combinaciones de `risk_threshold` y `rebuffer_threshold_s`. Aceptar
solo si aumenta `intervention_rate` sin romper global, `2_5_mbps` ni
`spbc_v2_dpo_on_policy`. Si no aparece un veto no trivial y estable, la decision
correcta es mantener SPBC solo como candidato principal y redisenar el SPC como
predictor calibrado antes de gastar un full.

### SPC critic/copilot calibrado

Tras rechazar `SPBC residual safe-rank v1`, el siguiente intento SPC no debe
ser otro `SPC solo` ni safe-rank como policy. El runner nuevo entrena
`critic_v1`, pensado como critico predictivo, y evalua inmediatamente el rol
copiloto frente al SPBC congelado:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_spc_critic_copilot_wsl.sh
```

Resumen:

```bash
python3 scripts/summarize_phase45_v2_spc_critic_copilot.py
```

Aceptar solo si el hibrido interviene de forma no trivial, mantiene riesgo en
banda, no empeora over-aggressive/rebuffer frente a `SPBC only` y no compra
esas mejoras con una perdida grande de utility. Este runner no exporta bundle,
no registra controller y no ejecuta Phase 6.

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
