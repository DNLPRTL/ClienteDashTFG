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

Primero pilot, no full:

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate

LOG=/tmp/phase45_v2_spbc_dpo_dagger2_pilot_$(date +%Y%m%d_%H%M%S).log
{
  python3 scripts/train_phase45_v2_spbc_dpo.py \
    --profile pilot \
    --dataset-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1_pilot \
    --output-dir ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/pilot_dagger2_utility_risk_v1 \
    --overwrite \
    --device auto
} 2>&1 | tee "$LOG"
cat "$LOG" | clip.exe
echo "Salida copiada al portapapeles: $LOG"
```

Full solo si el pilot mejora el fallo real: `2_5_mbps`,
`spbc_v2_dpo_on_policy`, utility regret y rebuffer regret.
