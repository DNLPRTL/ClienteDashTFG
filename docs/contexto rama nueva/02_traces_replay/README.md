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

Guardrails:

- schema normalizado: `timestamp_s,duration_s,throughput_kbps`
- splits por `leakage_group`
- semanticas explicitas por dataset
- trazas demasiado cortas o todo cero excluidas del manifest curado
- trazas malas/intermitentes utiles conservadas con flags
