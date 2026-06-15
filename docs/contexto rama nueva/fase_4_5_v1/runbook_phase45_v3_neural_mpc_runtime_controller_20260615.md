# Runbook Phase45 v3 Neural-MPC Runtime Controller - 2026-06-15

## Proposito

Integrar `phase45_v3_neural_throughput_calibrated_mpc_v1` como controller
runtime guarded, usando el bundle experimental validado en Ubuntu cliente.

Este paso no ejecuta Phase 6 formal, no es benchmark y no autoriza ranking ni
afirmaciones de mejora QoE.

## Estado de entrada

Bundle validado en Ubuntu cliente:

```text
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
```

Resultado previo:

```text
status=PASS
hashes_valid=true
controller_integrated=false
benchmark_performed=false
ranking_performed=false
```

## Controller registrado

Clave:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

Nombre en GUI:

```text
Propio Neural-MPC v1
```

Parametros por defecto Phase 6:

```text
bundle_dir=/home/daniel/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
fallback_controller=robust_mpc
verify_hashes=true
max_inference_latency_ms=50.0
diagnostic_only=false
```

## Smoke obligatorio en Ubuntu cliente

Antes de abrir la ventana de experimentos:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/smoke_phase45_v3_neural_mpc_runtime_controller_ubuntu_cliente.sh
```

Salida esperada:

```text
status=PASS
decision=RUNTIME_CONTROLLER_LOADS_AND_SELECTS
neural_bundle_loaded=1
neural_bundle_hash_ok=1
neural_valid_action=1
neural_fallback_used=0
neural_fallback_reason=success_neural
```

Si falla, no abrir Phase 6. Pegar el JSON en el chat.

## Como lanzar la ventana de experimentos

En Ubuntu cliente:

```bash
cd ~/TFG/DashClientModular4
python3 scripts/phase6_gui.py
```

Para el primer experimento con este controller seleccionar:

```text
Preset: diagnostico
Motor: fake
Controllers:
  Rate Based
  BOLA
  Robust MPC
  Propio Neural-MPC v1
Reanudar: activado
Dry run: desactivado
Solo plan: desactivado
Sin analisis: desactivado
Limite: vacio
```

No seleccionar aun:

```text
equilibrado
extendido
Propio SPBC v2 Anchor
NeuralABR-Lite robust_mpc
NeuralABR-Lite teacher_hibrido
```

Motivo: el primer run debe aislar el nuevo controller frente a baselines
clasicos. Los presets `equilibrado` y `extendido` son candidatos a evaluacion
formal solo despues de validar el comportamiento diagnostico.

## Que carpeta adjuntar

Tras terminar la GUI, adjuntar la carpeta completa que aparezca bajo:

```text
~/TFG/runs_trazas/phase6/validacion_comparativa/
```

Normalmente tendra forma:

```text
YYYYMMDD_HHMMSS_diagnostico
```

Esa carpeta incluye protocolo, configs por sesion, logs, resultados y
verificacion. No se debe editar a mano.

## Lectura permitida

Si el diagnostico pasa, se puede avanzar a un preset mas amplio o a un contrato
formal de Phase 6.

Si no pasa, se revisan logs y telemetria. No se relajan gates ni se declaran
resultados comparativos.
