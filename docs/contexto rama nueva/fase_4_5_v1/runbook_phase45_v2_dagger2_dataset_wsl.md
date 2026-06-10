# Runbook Phase 4-5 v2 - Dataset DAgger-2 para 7B

## Objetivo

Generar un dataset externo nuevo con estados on-policy de la politica
`spbc_abr_v2_dpo/full_v1_utility_risk_v1` y reetiquetado oracle. No entrena, no
integra controllers, no ejecuta Phase 6 y no produce benchmark.

## Rutas

Dataset externo:

```bash
~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
```

Checkpoint v1 requerido para `spbc_v1_on_policy`:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v1/full_v1/modelo_spbc_abr_v1.pt
```

Checkpoint v2 requerido para `spbc_v2_dpo_on_policy`:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v1_utility_risk_v1/modelo_spbc_abr_v2_dpo.pt
```

## Smoke DAgger-2

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

LOG=/tmp/phase45_v2_dagger2_smoke_$(date +%Y%m%d_%H%M%S).log
{
  python3 scripts/build_phase45_v2_dagger2_dataset.py \
    --profile smoke \
    --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1_smoke \
    --overwrite \
    --device auto
} 2>&1 | tee "$LOG"
cat "$LOG" | clip.exe
echo "Salida copiada al portapapeles: $LOG"
```

## Pilot DAgger-2

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

LOG=/tmp/phase45_v2_dagger2_pilot_$(date +%Y%m%d_%H%M%S).log
{
  python3 scripts/build_phase45_v2_dagger2_dataset.py \
    --profile pilot \
    --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1_pilot \
    --overwrite \
    --device auto
} 2>&1 | tee "$LOG"
cat "$LOG" | clip.exe
echo "Salida copiada al portapapeles: $LOG"
```

## Full DAgger-2

No lanzarlo hasta que el smoke o pilot confirme las tres fuentes:

```text
oracle_rollout
spbc_v1_on_policy
spbc_v2_dpo_on_policy
```

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

LOG=/tmp/phase45_v2_dagger2_full_$(date +%Y%m%d_%H%M%S).log
{
  python3 scripts/build_phase45_v2_dagger2_dataset.py \
    --profile full_v1 \
    --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1 \
    --overwrite \
    --device auto
} 2>&1 | tee "$LOG"
cat "$LOG" | clip.exe
echo "Salida copiada al portapapeles: $LOG"
```

`full_v1` falla si falta `spbc_abr_v1/full_v1` salvo
`--allow-oracle-only-full`. El script DAgger-2 tambien falla si falta el
checkpoint `spbc_abr_v2_dpo/full_v1_utility_risk_v1` salvo
`--allow-no-v2-policy-rollout`, que es solo diagnostico y no debe usarse para
cerrar 7B.

## Validar Dataset

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

LOG=/tmp/phase45_v2_dagger2_validate_$(date +%Y%m%d_%H%M%S).log
{
  python3 scripts/build_phase45_v2_dagger2_dataset.py \
    --validate-only \
    --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
} 2>&1 | tee "$LOG"
cat "$LOG" | clip.exe
echo "Salida copiada al portapapeles: $LOG"
```

## Entrenar 7B sobre DAgger-2

Primero pilot, no full. DAgger-2 debe refinar la politica que genero la tercera
fuente (`spbc_v2_dpo_on_policy`), no volver a entrenar en frio desde
`spbc_abr_v1`. Por tanto, el pilot recomendado arranca desde
`spbc_abr_v2_dpo/full_v1_utility_risk_v1` como checkpoint inicial congelado y
lo usa tambien como referencia DPO/auditoria.

Despues de los pilots `warm_v2_focus`, `warm_v2_guarded` y
`warm_v2_constrained`, el siguiente pilot no debe relajar el gate ni lanzar full.
El pilot constrained devolvio `best_epoch=0`: los epochs entrenados bajaban
regret, pero subian demasiado `over_aggressive`, especialmente en
`2_5_mbps`. Por tanto, el siguiente ataque convierte esa senal de rechazo en
loss interna: KL a la referencia congelada, penalizacion de probabilidad sobre
acciones `over_aggressive_rebuffer`, margen contra esas acciones y penalizacion
del exceso de probabilidad respecto al checkpoint inicial.

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

LOG=/tmp/phase45_v2_spbc_dpo_dagger2_warm_v2_safe_margin_$(date +%Y%m%d_%H%M%S).log
{
  python3 scripts/train_phase45_v2_spbc_dpo.py \
    --profile pilot \
    --dataset-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1 \
    --output-dir ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot_dagger2_warm_v2_safe_margin_v1 \
    --init-checkpoint ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v1_utility_risk_v1/modelo_spbc_abr_v2_dpo.pt \
    --overwrite \
    --device auto \
    --epochs 10 \
    --batch-size 1024 \
    --learning-rate 0.00010 \
    --max-training-samples 150000 \
    --max-validation-samples 40000 \
    --utility-loss-weight 0.62 \
    --rebuffer-loss-weight 0.90 \
    --focus-bucket-sample-weight 2.35 \
    --severe-error-sample-weight 1.90 \
    --safe-vs-rebuffer-pair-weight 2.10 \
    --over-aggressive-rebuffer-action-weight 5.00 \
    --reference-kl-loss-weight 0.22 \
    --over-aggressive-probability-loss-weight 2.80 \
    --over-aggressive-margin-loss-weight 1.40 \
    --over-aggressive-reference-excess-loss-weight 2.20 \
    --over-aggressive-margin 0.40 \
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
    --safety-rebuffer-regret-tolerance 0.0010
} 2>&1 | tee "$LOG"
cat "$LOG" | clip.exe
echo "Salida copiada al portapapeles: $LOG"
```

Full solo si este pilot selecciona un `best_epoch` mayor que 0, pasa
`selected_checkpoint_safety_gate.passed=true`, mejora frente al checkpoint
inicial `full_v1_utility_risk_v1` en `init_checkpoint_reference_comparison` y,
sobre todo, no rompe el fallo real: `2_5_mbps`, `spbc_v2_dpo_on_policy`,
utility regret, rebuffer regret, over-aggressive y under-aggressive. No aceptar
un run que solo mejore `top1` global.

El confirmatorio full-samples observado para `safe_margin_v1` paso el gate con
`best_epoch=2`, `selected_checkpoint_safety_gate.passed=true`,
`training=557460` y `validation=128970`. Frente al checkpoint inicial en la
misma validacion:

```text
global utility_regret delta=-0.011653
global rebuffer_regret delta=-0.004669
global over_aggressive delta=-0.000202
global under_aggressive delta=-0.010987

2_5_mbps utility_regret delta=-0.007613
2_5_mbps rebuffer_regret delta=-0.007870
2_5_mbps over_aggressive delta=+0.000580

spbc_v2_dpo_on_policy utility_regret delta=-0.018673
spbc_v2_dpo_on_policy rebuffer_regret delta=-0.005901
spbc_v2_dpo_on_policy over_aggressive delta=-0.000279
spbc_v2_dpo_on_policy under_aggressive delta=-0.048802
```

Este resultado permitio tratar `safe_margin_v1` como candidato offline
prometedor, pero no autoriza todavia bundle, controller, ranking ni afirmacion
de mejora. Antes de escalar, confirmar estabilidad con varias seeds manteniendo
el mismo gate y la misma receta de loss.

## Confirmacion multi-seed de safe_margin_v1 full-samples

Ejecutar en WSL2. No usar estas salidas como benchmark. Solo confirman si el
candidato es estable ante la semilla de entrenamiento.

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

for SEED in 450741 450742 450743; do
  LOG=/tmp/phase45_v2_spbc_dpo_safe_margin_fullsamples_seed_${SEED}_$(date +%Y%m%d_%H%M%S).log
  {
    python3 scripts/train_phase45_v2_spbc_dpo.py \
      --profile pilot \
      --dataset-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1 \
      --output-dir ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot_dagger2_warm_v2_safe_margin_fullsamples_seed_${SEED}_v1 \
      --init-checkpoint ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v1_utility_risk_v1/modelo_spbc_abr_v2_dpo.pt \
      --overwrite \
      --device auto \
      --epochs 6 \
      --batch-size 1024 \
      --learning-rate 0.00010 \
      --no-profile-sample-limits \
      --seed "$SEED" \
      --utility-loss-weight 0.62 \
      --rebuffer-loss-weight 0.90 \
      --focus-bucket-sample-weight 2.35 \
      --severe-error-sample-weight 1.90 \
      --safe-vs-rebuffer-pair-weight 2.10 \
      --over-aggressive-rebuffer-action-weight 5.00 \
      --reference-kl-loss-weight 0.22 \
      --over-aggressive-probability-loss-weight 2.80 \
      --over-aggressive-margin-loss-weight 1.40 \
      --over-aggressive-reference-excess-loss-weight 2.20 \
      --over-aggressive-margin 0.40 \
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
      --safety-rebuffer-regret-tolerance 0.0010
  } 2>&1 | tee "$LOG"
  echo "Salida seed ${SEED}: $LOG"
done

python3 - <<'PY'
from pathlib import Path
import json

root = Path.home() / "TFG/modelos/phase45_v1/spbc_abr_v2_dpo"
for path in sorted(root.glob("pilot_dagger2_warm_v2_safe_margin_fullsamples_seed_*_v1/reporte_entrenamiento_spbc_abr_v2_dpo.json")):
    report = json.loads(path.read_text(encoding="utf-8"))
    metrics = report["validation_metrics"]
    focus = metrics["focus_2_5_mbps"]
    source = metrics["by_rollout_source"].get("spbc_v2_dpo_on_policy", {})
    gate = report["selected_checkpoint_safety_gate"]
    print(
        path.parent.name,
        "best_epoch=", report["best_epoch"],
        "gate=", gate["passed"],
        "global_over=", metrics["over_aggressive_rate_vs_oracle"],
        "focus_over=", focus["over_aggressive_rate_vs_oracle"],
        "spbc2_over=", source.get("over_aggressive_rate_vs_oracle"),
        "global_u=", metrics["selected_utility_regret_vs_oracle_mean"],
        "focus_u=", focus["selected_utility_regret_vs_oracle_mean"],
        "spbc2_u=", source.get("selected_utility_regret_vs_oracle_mean"),
    )
PY
```

Aceptar la familia solo si la mayoria de seeds mantiene `best_epoch > 0`,
`selected_checkpoint_safety_gate.passed=true`, mejora regret frente al checkpoint
inicial y no consume de forma fragil el margen de `2_5_mbps over_aggressive`.

Resultado observado: el multi-seed full-samples de `safe_margin_v1` no queda
aprobado. Las tres seeds resumidas terminaron con `best_epoch=0`; el
`gate=true` final correspondia al fallback del checkpoint inicial, no a un epoch
entrenado. El fallo dominante no fue `over_aggressive`, sino no sostener
utility regret en `2_5_mbps` y `spbc_v2_dpo_on_policy` frente al gate relativo.
No lanzar `--profile full_v1` con `safe_margin_v1` tras este resultado.

## Piloto v3 trainer-only: anchor_safe_rank

El siguiente intento mantiene el marco de mejora segura anclada al checkpoint
inicial, pero anade una perdida positiva dentro del conjunto seguro:
`safe_utility_rank_loss`. Esta perdida usa solo targets de entrenamiento ya
existentes (`reward_by_action`, `action_mask` y
`over_aggressive_action_by_action`), no cambia el contrato de inferencia y no
toca runtime ni controller final.

Ejecutar primero como confirmacion full-samples con profile `pilot` y
`--no-profile-sample-limits`. No llamar benchmark a esta salida y no declarar
mejora de QoE.

No pegar el comando largo manualmente en WSL. Usar el runner versionado:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_anchor_safe_rank_wsl.sh
```

Para repetir solo el resumen:

```bash
cd ~/TFG/DashClientModular4
python3 scripts/summarize_phase45_v2_anchor_safe_rank.py
```

Aceptar `anchor_safe_rank` solo si la mayoria de seeds tiene `best_epoch > 0`,
`selected_checkpoint_safety_gate.passed=true`, mejora regret frente al
checkpoint inicial y no consume de forma fragil el margen de `2_5_mbps` ni de
`spbc_v2_dpo_on_policy`. Si vuelve a caer a `best_epoch=0` en la mayoria, no
relajar el gate: pasar a diagnostico de dataset/labels o a residual/logit-delta
anclado.

Resultado observado del multi-seed `anchor_safe_rank`:

```text
seed_450741 best_epoch=6 gate=true global_over=0.009971 focus_over=0.026763 spbc2_over=0.005397 global_u=0.054827 focus_u=0.064302 spbc2_u=0.047667
seed_450742 best_epoch=6 gate=true global_over=0.009677 focus_over=0.026441 spbc2_over=0.005211 global_u=0.054297 focus_u=0.062302 spbc2_u=0.047701
seed_450743 best_epoch=6 gate=true global_over=0.010204 focus_over=0.026860 spbc2_over=0.005676 global_u=0.054066 focus_u=0.062735 spbc2_u=0.046887
```

Lectura: la receta pasa la condicion operativa de estabilidad full-samples con
profile `pilot`: 3/3 seeds tienen `best_epoch > 0`, `gate=true`, over controlado
y utility regret estable en `2_5_mbps` y `spbc_v2_dpo_on_policy`. Esto no es
benchmark, ranking ni claim de mejora QoE; solo autoriza el siguiente paso del
plan: ejecutar el entrenamiento normal con `--profile full_v1` usando la misma
familia de loss.

## Entrenamiento normal full_v1 anchor_safe_rank

Ejecutar solo despues de que el multi-seed anterior pase. No pegar el comando
largo manualmente en WSL; usar el runner versionado:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v2_anchor_safe_rank_full_wsl.sh
```

Para repetir solo el resumen:

```bash
cd ~/TFG/DashClientModular4
python3 scripts/summarize_phase45_v2_anchor_safe_rank_full.py
```

Aceptar el `full_v1` normal solo si `best_epoch > 0`,
`selected_checkpoint_safety_gate.passed=true` y los deltas frente al checkpoint
inicial mantienen no-regresion en global, `2_5_mbps` y
`spbc_v2_dpo_on_policy`. Si falla, no relajar gate ni congelar candidato.

Resultado observado del `full_v1 anchor_safe_rank`:

```text
best_epoch=8
gate=true
global_over=0.009878
focus_over=0.026312
spbc2_over=0.005187
global_u=0.053229
focus_u=0.062015
spbc2_u=0.044244
safe_rank=0.018196476
```

Deltas principales frente a `full_v1_utility_risk_v1`:

```text
global utility_regret delta=-0.015430
global rebuffer_regret delta=-0.003992
global over_aggressive delta=-0.005777
global predicted_rebuffer_s_mean delta=-0.004228
global predicted_bitrate_kbps_mean delta=-127.600217
global under_aggressive delta=+0.059409

2_5_mbps utility_regret delta=-0.026998
2_5_mbps rebuffer_regret delta=-0.007969
2_5_mbps over_aggressive delta=-0.018583
2_5_mbps predicted_rebuffer_s_mean delta=-0.008934
2_5_mbps predicted_bitrate_kbps_mean delta=-340.249597
2_5_mbps under_aggressive delta=+0.163059
```

Lectura: el run normal pasa el gate con un epoch entrenado y mejora la zona que
habia bloqueado `safe_margin_v1`, incluido `2_5_mbps`. La contrapartida es una
politica mas conservadora: baja `top1_accuracy`, `balanced_accuracy` y
`macro_f1`, baja el bitrate medio predicho y sube `under_aggressive`. Por tanto,
queda aceptado solo como candidato offline, no como controller final.

Artefacto candidato:

```text
checkpoint=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
checkpoint_sha256=43b4d012448e12885fac8cbfec914aab6450e0c1b146a4bb8534e8b90b61c227
training_report=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/reporte_entrenamiento_spbc_abr_v2_dpo.json
```

Para verificar de nuevo ruta y SHA del checkpoint despues de actualizar el repo:

```bash
cd ~/TFG/DashClientModular4
git pull
python3 scripts/summarize_phase45_v2_anchor_safe_rank_full.py
```

No exportar bundle, no registrar controller, no lanzar Phase 6 y no declarar
ranking, ganador, mejora QoE ni generalizacion con este resultado. El siguiente
paso de IA recomendado es preparar/evaluar offline el modelo complementario
`spc_abr_v2_reward_risk` con scripts versionados y gates analogos.
