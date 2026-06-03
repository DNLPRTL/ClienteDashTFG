# AGENTS.md

Guia permanente de trabajo para `DashClientModular4`.

## Estado actual

Phase 5 esta cerrada. `neural_abr_lite` esta integrado como guarded neural scorer controller, pero no hay benchmark, ranking ni afirmacion de mejora de QoE.

La fase activa es:

```text
Phase 6A0 - Validation documentation scaffold and evidence consolidation
```

Phase 6A0 esta abierta como documentacion/protocolo intake solamente. No hay benchmark, ranking, graficas, resultados, ganador ni afirmacion de mejora de QoE.

La ruta activa de documentacion de validacion es:

```text
docs/science/06_validation/
```

## Reglas permanentes

1. Mantener el cliente limpio, modular y testeable.
2. No tocar runtime, `player.py`, controladores, `core/trace_replay` ni `core/evaluation` sin una especificacion explicita.
3. No ejecutar benchmark, generar graficas, crear rankings, declarar ganadores ni afirmar mejora de QoE en Phase 6A0.
4. No reentrenar NeuralABR-Lite ni cambiar `qoe_linear_v1` / `reward_n` en Phase 6A0.
5. No meter datasets, modelos, runs, logs, PDFs, CSVs, JSONL, zips, videos, segmentos DASH ni otros artifacts en Git.
6. Mantener workspaces externos bajo `C:\Users\danie\Documents\TFG\_datasets`, `_models`, `_runs`, `_scripts`, `_literature`, `_audits` y `_archive`.
7. No pedir a Codex implementar directamente desde PDFs brutos. Usar primero indices, source cards, specs y documentos canonicos.
8. Usar `docs/INDEX.md`, `docs/science/PHASE_INDEX.md` y `docs/science/CANONICAL_DOCUMENTS.md` como entrada antes de abrir cientos de Markdown historicos.
9. Usar staging explicito. No usar `git add .`.
10. Todo cambio importante debe tener commit propio.

## Separacion tecnica

Mantener separados:

- parser MPD
- descarga de segmentos
- buffer
- motor de reproduccion
- control ABR
- logging
- evaluacion
- documentacion cientifica
- workspaces locales externos

## Evidence guardrail

Phase 6 debe bloquear por checksum cualquier traza vista en Phase 4 si se usa para evaluar `neural_abr_lite` frente a baselines. Phase 4 teacher agreement/OOD queda como diagnostico, no como prueba fuerte de generalizacion.
