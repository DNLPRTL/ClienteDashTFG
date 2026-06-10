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
