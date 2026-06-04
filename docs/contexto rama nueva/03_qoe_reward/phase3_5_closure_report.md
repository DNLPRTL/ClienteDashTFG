# Phase 3.5 Rebuild closure report

Status: closed_phase3_5_rebuild_on_windows.

Phase 3.5 Rebuild queda cerrada en Windows despues de pasar las validaciones y subir la rama a GitHub.

Se cierra:

```text
qoe_linear_v1
qoe_linear_mean
reward_n candidate
qoe_log_v1 sensitivity
evaluation gates
no-ranking boundary
synthetic smoke scenarios
```

No se cierra:

```text
benchmark formal
ranking de controllers
entrenamiento IA
sampler de Phase 4
claim de mejora QoE
VMAF
startup penalty
```

Comandos de cierre ejecutados en Windows:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts\check_client_readiness.py --strict
python scripts\run_qoe_smoke_scenarios.py --output-root "C:\Users\danie\Documents\TFG\runs_trazas\phase3_5\smoke" --clean
```

Resultado:

```text
unittest discover: PASS, 299 tests
client readiness strict: PASS
QoE smoke scenarios: PASS, 4 scenarios
outputs_are_benchmark_results=false
ranking_performed=false
benchmark_performed=false
ia_training_performed=false
```
