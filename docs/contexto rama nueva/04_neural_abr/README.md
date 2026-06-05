# Phase 4 Rebuild - NeuralABR offline

Status: phase4a_training_corpus_sampler_in_progress.

Phase 4 debera reconstruirse sobre:

- `phase3_trace_manifest_curated.json`
- el contrato QoE/reward de `03_qoe_reward`
- un sampler balanceado nuevo

No reutilizar dry-runs legacy ni datasets de entrenamiento antiguos.

## Phase 4A

Primer bloque activo:

```text
phase4a_corpus_y_sampler_de_entrenamiento.md
```

Este bloque prepara un plan auditable de ventanas de traza para entrenamiento
offline. No entrena IA, no genera labels de teacher y no produce resultados de
benchmark.
