# Runbook Phase 4-5 v1 - Entrenamiento `spc_abr_v1`

## Objetivo

Entrenar offline el primer candidato nuevo de Fase 4-5 v1:

```text
spc_abr_v1 = Safe Predictive Control ABR v1
```

Este bloque entrena un predictor neural de capacidad futura y riesgo de
rebuffer por representation. No exporta bundle, no registra controller, no
ejecuta Phase 6 y no autoriza ranking ni mejora QoE.

## Entradas

Dataset derivado validado:

```bash
~/TFG/datasets_normalizados/phase45_v1/phase45v1B_spc_spbc_dataset_v1/
```

Perfil multimedia usado por contrato offline:

```text
media_profile_id=paseo_10min_30fps_4s
segment_duration_s=4
segment_count=30
representation_kbps=300,750,1200,1850,2850,4300
```

El entrenamiento no descarga MPDs ni segmentos. Aprende desde replay offline
con trazas. Cuando exista controller runtime, recibira la ladder real del MPD
igual que los controllers clasicos.

## Salidas

Checkpoint externo:

```bash
~/TFG/modelos/phase45_v1/spc_abr_v1/<profile>/
```

Ficheros principales:

- `modelo_spc_abr_v1.pt`
- `configuracion_spc_abr_v1.json`
- `normalizacion_spc_abr_v1.json`
- `reporte_entrenamiento_spc_abr_v1.json`

No commitear esta carpeta.

## Comandos

Sincronizar repo y activar entorno:

```bash
cd ~/TFG/DashClientModular4
git status --short --branch
git pull
source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

Validar que el dataset completo sigue correcto:

```bash
python3 scripts/build_phase45_v1_dataset.py \
  --validate-only \
  --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v1B_spc_spbc_dataset_v1
```

Smoke rapido:

```bash
python3 scripts/train_phase45_v1_spc_abr.py --profile smoke --overwrite
```

Pilot:

```bash
python3 scripts/train_phase45_v1_spc_abr.py --profile pilot --overwrite
```

Entrenamiento completo:

```bash
python3 scripts/train_phase45_v1_spc_abr.py --profile full_v1 --overwrite --device auto
```

## Salida esperada

Cada entrenamiento debe terminar con:

```json
{
  "status": "PASS",
  "benchmark_performed": false,
  "controller_registered": false,
  "bundle_exported": false,
  "ia_training_performed": true
}
```

Metricas a revisar en `validation_metrics`:

- `p50_mae_kbps`
- `capacity_mae_kbps`
- `risk_brier`
- `risk_accuracy`
- `risk_false_negative_rate`
- `by_throughput_bucket`

Estas metricas son diagnostico offline de entrenamiento, no benchmark formal.
