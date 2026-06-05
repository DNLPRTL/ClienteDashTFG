# Phase 3 Rebuild - Traces y replay

Status: closed_on_windows_pending_ubuntu_validation.

Phase 3 Rebuild define el corpus externo de trazas normalizadas y su manifest curado.

Artifacts externos principales:

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase3\final
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
C:\Users\danie\Documents\TFG\auditorias_trazas\phase3\final
C:\Users\danie\Documents\TFG\runs_trazas\phase3\final
```

El manifest curado es la entrada recomendada para preparar Phase 4, pero no es por si mismo un training dataset ni un benchmark.

Addendum sintetico:

```text
synthetic_controlled_network
semantics=synthetic_available_bandwidth
1024 traces
8 scenarios
300s per trace
1s granularity
split counts: train=720, test=152, eval=152
```

Las trazas sinteticas estan marcadas como sinteticas y pueden aparecer en `train`, `test` y `eval`, pero los resultados futuros sobre ellas deben reportarse separados de los resultados sobre trazas reales.

Guardrails:

- schema normalizado: `timestamp_s,duration_s,throughput_kbps`
- splits por `leakage_group`
- semanticas explicitas por dataset
- trazas demasiado cortas o todo cero excluidas del manifest curado
- trazas malas/intermitentes utiles conservadas con flags
- trazas sinteticas diferenciadas por `synthetic_scenario`
