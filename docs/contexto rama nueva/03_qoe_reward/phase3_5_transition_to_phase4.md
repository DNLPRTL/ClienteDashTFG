# Transition to Phase 4

Status: ready_for_phase4_planning_after_phase3_5_validation.

Phase 4 no debe empezar entrenando directamente.

Primer bloque recomendado:

```text
Phase 4A - training corpus and sampler contract
```

Debe definir:

- lectura de `phase3_trace_manifest_curated.json`
- uso exclusivo de split `train` para entrenamiento
- no mezcla de `leakage_group`
- ventanas temporales reproducibles
- balance por `semantics`, dataset y dificultad de red
- separacion de train/test/eval
- exclusion de metadatos como features del modelo

Phase 3.5 aporta el reward candidato y los gates. Phase 4 debe decidir como construir muestras de entrenamiento sin dominancia de FCC ni contaminacion entre splits.
