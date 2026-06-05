# Phase 4 Rebuild - NeuralABR offline

Status: phase4f_export_bundle_inferencia_in_progress.

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
train-only y una prueba rapida diagnostica de entrenamiento en CPU. No genera
modelo candidato.

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
