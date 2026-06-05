# Phase 4 Rebuild - NeuralABR offline

Status: phase4g_closed_ready_for_phase5.

Phase 4 debera reconstruirse sobre:

- `phase3_trace_manifest_curated.json`
- el contrato QoE/reward de `03_qoe_reward`
- un sampler balanceado nuevo

No reutilizar dry-runs legacy ni datasets de entrenamiento antiguos.

## Phase 4A

Primer bloque activo:

```text
phase4a_plan_de_trazas_para_entrenamiento.md
```

Este bloque prepara un plan auditable de ventanas de traza para entrenamiento
offline. No entrena IA, no genera labels de teacher y no produce resultados de
benchmark.

Siguiente bloque activo:

```text
phase4bcd_datos_y_prueba_rapida_offline.md
```

Este bloque genera datos offline con labels `robust_mpc`, normalizacion
train-only y una prueba rapida diagnostica de entrenamiento en CPU. Los labels
`robust_mpc` se generan ejecutando el controller real de Phase 2 dentro del
replay offline. No genera modelo candidato.

Bloque activo:

```text
phase4e_entrenamiento_modelo_candidato.md
```

Este bloque entrena un checkpoint externo de NeuralABR-Lite y revisa si queda
listo para Phase 4F export. No integra controller y no produce benchmark.

Bloque activo:

```text
phase4f_export_bundle_inferencia.md
```

Este bloque exporta un bundle local de inferencia, valida hashes y ejecuta una
prueba offline de inferencia CPU. No integra controller y no produce benchmark.

Extension cerrada:

```text
phase4h_teacher_hibrido_sin_vmaf.md
```

Este bloque genera un segundo modelo offline con `teacher_hibrido`, seleccionando
por ventana el mejor comportamiento entre controllers clasicos bajo
`qoe_linear_v1`. No usa VMAF, no integra controller y no produce benchmark.

Cierre:

```text
phase4g_cierre_modelos_offline.md
```

Phase 4 queda cerrada con dos bundles offline:

- `NeuralABR-Lite robust_mpc`
- `NeuralABR-Lite teacher_hibrido`

Contexto para continuar en un hilo nuevo:

```text
phase5_contexto_nuevo_hilo_integracion_dos_modelos.md
```
