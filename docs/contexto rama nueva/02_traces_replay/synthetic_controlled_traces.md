# Synthetic controlled traces addendum

Status: phase3_addendum_synthetic_controlled_traces.

Este addendum incorpora trazas sinteticas controladas al corpus Phase 3 Rebuild. La motivacion viene de trabajos de ABR que usan trazas sinteticas de red con granularidad de 1 segundo para cubrir escenarios que no siempre aparecen con suficiente densidad en datasets reales.

## Decision

Se genera un bloque sintetico versionado:

```text
dataset_id=synthetic_controlled_network
generator_id=phase3_synthetic_controlled_network_v1
semantics=synthetic_available_bandwidth
trace_count=1024
count_per_scenario=128
duration_s=300
sample_duration_s=1
```

Resultado generado en Windows:

```text
synthetic_trace_count=1024
synthetic_split_counts: train=720, test=152, eval=152
synthetic_duration_total_s=307200
curated_manifest_trace_count=6768
curated_manifest_split_counts: train=4725, test=1018, eval=1025
```

Las trazas sinteticas usan el mismo schema normalizado:

```csv
timestamp_s,duration_s,throughput_kbps
```

## Escenarios

```text
synthetic_perfect_high
synthetic_stable_low
synthetic_sudden_drop
synthetic_sudden_recovery
synthetic_mobile_variable
synthetic_periodic_oscillation
synthetic_stall_trap
synthetic_high_jitter
```

`synthetic_mobile_variable` usa un modelo Markoviano de estados de throughput medio. El resto son patrones controlados para stress de ABR: caidas, recuperaciones, oscilacion, jitter, red lenta y caso trampa justo bajo la representation de 4300 kbps.

## Manifest y splits

Las sinteticas entran en `train`, `test` y `eval`, por decision explicita del proyecto, pero quedan marcadas con:

```text
synthetic=true
synthetic_scenario=<scenario>
generator_seed=phase3_synthetic_controlled_v1
intended_use=controlled_train_test_eval
```

Los splits se hacen por `leakage_group`, nunca por filas. Cada traza sintetica tiene su propio `leakage_group`.

## Guardrail de evaluacion

Los resultados sobre `synthetic_available_bandwidth` deben reportarse separados de las trazas reales. Sirven para robustez controlada, entrenamiento balanceado y scenarios de stress, no para afirmar generalizacion real-world.

Phase 4 debera limitar su cuota dentro del sampler para que no dominen el aprendizaje.

## Artifacts externos

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase3\final\schema_v1\synthetic_controlled_network
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\traces\synthetic_controlled_network
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\synthetic_sources\synthetic_controlled_network
C:\Users\danie\Documents\TFG\auditorias_trazas\phase3\final\phase3_synthetic_trace_generation_report.json
C:\Users\danie\Documents\TFG\ubuntu_phase3_ready_for_TFGv1.zip
```

Antes de actualizar el manifest con sinteticas se preservan snapshots real-only:

```text
phase3_trace_manifest_final_real_only_snapshot.json
phase3_trace_manifest_curated_real_only_snapshot.json
```
