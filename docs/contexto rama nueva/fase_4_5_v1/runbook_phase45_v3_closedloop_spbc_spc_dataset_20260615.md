# Runbook Phase45 v3 closed-loop SPBC/SPC dataset - 2026-06-15

## Objetivo

Preparar la linea paralela:

```text
phase45_v3_closedloop_spbc_spc_v1
```

sin tocar la linea viva:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

Este runbook solo genera y valida dataset. No entrena, no crea bundle, no
registra controller, no ejecuta Phase 6, no hace benchmark y no autoriza claims
de QoE.

## Filosofia del dataset

El dataset no reutiliza el SPBC v1/v2 fallido como evidencia primaria. Se genera
de nuevo desde:

- manifest curado Phase 3;
- entorno cerrado Phase45 v3;
- media profile `paseo_10min_30fps_4s`;
- fragmentos de 4 s;
- 30 segmentos por ventana;
- `max_buffer_s=60.0`;
- ladder `[300, 750, 1200, 1850, 2850, 4300]` kbps;
- reward `qoe_linear_v1`;
- splits train/test sin leakage.

El oracle Q_H cerrado actua como fabrica de etiquetas. Los futuros solo aparecen
como targets, nunca como inputs.

## Salidas

Pilot:

```text
~/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_pilot_v1
```

Full:

```text
~/TFG/datasets_normalizados/phase45_v3/closedloop_spbc_spc_full_v1
```

Ficheros principales:

```text
datos_entrenamiento_phase45_v3_closedloop_spbc_spc.jsonl
datos_validacion_phase45_v3_closedloop_spbc_spc.jsonl
resumen_dataset_phase45_v3_closedloop_spbc_spc.json
auditoria_no_contaminacion_phase45_v3_closedloop_spbc_spc.json
auditoria_targets_phase45_v3_closedloop_spbc_spc.json
esquema_model_inputs_phase45_v3_closedloop_spbc_spc.json
esquema_targets_phase45_v3_closedloop_spbc_spc.json
```

## Plan de ejecucion

- HECHO: documentar decision de linea paralela SPBC/SPC cerrada.
- HECHO: implementar generador con schema propio policy+critic.
- HECHO: implementar auditoria de leakage y targets.
- HECHO: implementar resumen pegable.
- HECHO: implementar tests unitarios de schema/paridad/leakage.
- SIGUIENTE: generar dataset pilot en WSL y pegar la salida.
- PENDIENTE: solo si pilot PASS, generar dataset full.
- PENDIENTE: disenar entrenamiento pilot SPBC/SPC.
- PENDIENTE: entrenar una seed pilot.
- PENDIENTE: analizar errores antes de multi-seed.
- PENDIENTE: bundle/controller solo si los gates offline lo justifican.

## Comando WSL pilot

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/generate_phase45_v3_closedloop_spbc_spc_pilot_dataset_wsl.sh
```

Pegar la salida completa del bloque `pasteable pilot dataset summary`.

## Comando WSL full

Usar solo cuando el pilot haya salido `PASS` y se haya revisado la distribucion
de targets:

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/generate_phase45_v3_closedloop_spbc_spc_full_dataset_wsl.sh
```

Pegar la salida completa del bloque `pasteable full dataset summary`.

## Interpretacion minima

La salida debe tener:

```text
status=PASS
targets=PASS
leakage=PASS
max_buffer_s=60.0
fallback_count=0
high_capacity_safe_target_action0_rate <= 0.05
safe_action_presence_rate=1.0
```

Si no cumple esto, no se entrena. Se revisa el dataset antes de gastar GPU.

## Nota de seguridad cientifica

Este dataset no es benchmark. Aunque el target oracle tenga reward/Q_H, la salida
solo valida que el material de entrenamiento es coherente con el entorno cerrado.
La comparativa formal sigue perteneciendo a Phase 6 autorizada.
