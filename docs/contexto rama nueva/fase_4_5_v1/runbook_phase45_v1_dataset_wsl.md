# Runbook Phase 4-5 v1 - Dataset derivado SPC/SPBC en WSL2

## Objetivo

Generar el dataset derivado `phase45_v1` para los futuros candidatos
`spc_abr_v1` y `spbc_abr_v1`.

Este bloque no entrena modelos, no exporta bundles, no registra controllers y
no ejecuta Phase 6. Sus salidas no son benchmark, ranking ni evidencia de
mejora QoE.

## Artefactos

Entrada esperada en WSL2:

```bash
~/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
~/TFG/datasets_normalizados/phase3/final/
```

Salida externa:

```bash
~/TFG/datasets_normalizados/phase45_v1/phase45v1B_spc_spbc_dataset_v1/
```

El dataset contiene:

- `datos_entrenamiento_spc_spbc.jsonl`
- `datos_validacion_spc_spbc.jsonl`
- `resumen_dataset_phase45_v1.json`
- `plan_muestreo_phase45_v1.json`
- `auditoria_muestreo_phase45_v1.json`
- `auditoria_no_contaminacion_phase45_v1.json`
- `auditoria_oracle_qoe_beam_v1.json`
- `estadisticas_normalizacion_train_only_phase45_v1.json`
- schemas de inputs y targets

## Sincronizacion WSL2

Ejecutar desde Windows:

```bash
wsl -d Ubuntu-24.04
```

Dentro de WSL2:

```bash
mkdir -p ~/TFG/{datasets_normalizados,manifests_trazas,modelos,runs_trazas,auditorias_trazas}

rsync -a --info=progress2 /mnt/c/Users/danie/Documents/TFG/datasets_normalizados/ ~/TFG/datasets_normalizados/
rsync -a --info=progress2 /mnt/c/Users/danie/Documents/TFG/manifests_trazas/ ~/TFG/manifests_trazas/

cd ~/TFG/DashClientModular4
git status --short --branch
git pull

source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

La comprobacion de PyTorch debe devolver `True` y la GPU AMD expuesta por ROCm.

## Generacion recomendada

Primero generar un `pilot` para comprobar rutas y coste:

```bash
cd ~/TFG/DashClientModular4
source ~/venvs/rocm721/bin/activate

python3 scripts/build_phase45_v1_dataset.py \
  --profile pilot \
  --overwrite \
  --trace-path-rewrite /home/daniel/TFG=$HOME/TFG \
  --trace-path-rewrite /home/danie/TFG=$HOME/TFG
```

Si pasa, generar el dataset completo:

```bash
python3 scripts/build_phase45_v1_dataset.py \
  --profile full_v1 \
  --overwrite \
  --trace-path-rewrite /home/daniel/TFG=$HOME/TFG \
  --trace-path-rewrite /home/danie/TFG=$HOME/TFG
```

El script genera y valida el dataset en la misma ejecucion. La salida esperada
incluye:

```json
{
  "status": "PASS",
  "dataset_validation": {
    "status": "PASS"
  }
}
```

## Validacion de un dataset ya generado

```bash
python3 scripts/build_phase45_v1_dataset.py \
  --validate-only \
  --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v1B_spc_spbc_dataset_v1
```

## Notas de contrato

- `eval` queda excluido.
- Los splits se respetan por `leakage_group`.
- Las trazas sinteticas tienen cuota maxima del 15%.
- Las redes reales bajas y variables se priorizan en el muestreo.
- `future_throughput_kbps` y `oracle_action` son targets, nunca inputs.
- Los controllers clasicos reales se consultan solo para auditoria.
- `oracle_qoe_beam_v1` es profesor offline, no controller runtime.
