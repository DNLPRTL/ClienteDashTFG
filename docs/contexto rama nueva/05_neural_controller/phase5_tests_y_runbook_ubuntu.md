# Phase 5 - Tests y runbook Ubuntu

## Validacion Windows

Comandos base:

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Los tests nuevos crean bundles Phase 4 minimos en directorios temporales fuera
del repo. No consumen ni commitean modelos reales.

## Smoke Ubuntu sin bundle

Objetivo: comprobar fallo cerrado y fallback.

```bash
cd ~/TFG/DashClientModular4
git pull --ff-only origin rebuild/phase3-from-phase2
python -m unittest discover
python scripts/check_client_readiness.py --strict
```

Despues, ejecutar un run pequeno con:

```yaml
controller:
  name: "neural_abr_lite_robust_mpc"
  params:
    fallback_controller: "robust_mpc"
```

Resultado esperado:

```text
feedback_neural_fallback_used=1
feedback_neural_fallback_reason=missing_bundle_dir
evaluation_segments.csv sin feedback_neural_*
```

## Smoke Ubuntu con bundles reales

Rutas previstas:

```text
/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite
/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite
```

Ejecutar un smoke estructural por controller:

```yaml
controller:
  name: "neural_abr_lite_robust_mpc"
  params:
    bundle_dir: "/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite"
    fallback_controller: "robust_mpc"
    verify_hashes: true
    max_inference_latency_ms: 50.0
```

```yaml
controller:
  name: "neural_abr_lite_teacher_hibrido"
  params:
    bundle_dir: "/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite"
    fallback_controller: "robust_mpc"
    verify_hashes: true
    max_inference_latency_ms: 50.0
```

Resultado esperado:

```text
run_manifest.json status=completed
segment_telemetry.csv contiene feedback_neural_*
evaluation_segments.csv no contiene feedback_neural_*
dataset.csv ausente
dataset_training.csv ausente
feedback_neural_bundle_loaded=1
feedback_neural_diagnostic_only=1
```

Estos smokes no son benchmark.

## Resultado ejecutado

Ubuntu cliente ejecuto los dos smokes con bundles reales el 2026-06-05:

```text
smoke_neural_robust_mpc/run_20260605_143034
smoke_neural_teacher_hibrido/run_20260605_143136
```

Ambos quedaron `status=completed`, con bundle cargado, `success_neural`,
telemetria `feedback_neural_*` solo en `segment_telemetry.csv` y sin artefactos
legacy `dataset.csv` ni `dataset_training.csv`.

La red del smoke fue la red rapida del adaptador puente entre VM cliente y VM
servidor. Se acepta solo como smoke estructural de integracion. No autoriza
benchmark, ranking, comparacion QoE ni claim de mejora.
