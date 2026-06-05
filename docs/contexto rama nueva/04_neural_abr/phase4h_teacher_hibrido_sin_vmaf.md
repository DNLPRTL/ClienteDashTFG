# Phase 4H - Teacher hibrido sin VMAF

## Objetivo

Construir un segundo modelo offline `NeuralABR-Lite Candidate Scorer` usando
imitation learning con un teacher hibrido. Este bloque no sustituye al modelo
principal entrenado con `robust_mpc`; lo complementa como segunda variante
offline para una comparacion futura autorizada.

## Idea

Para cada ventana de traza seleccionada en Phase 4A se simulan varios
controllers clasicos:

- `rate_based`
- `bba`
- `bola`
- `mpc`
- `robust_mpc`

Cada controller produce una trayectoria completa sobre la misma ventana. La
trayectoria ganadora se selecciona con `qoe_linear_v1_mean`. Las acciones de esa
trayectoria se usan como labels de entrenamiento con:

```text
teacher_policy=teacher_hibrido
hybrid_source_teacher=<controller ganador de la ventana>
```

## Limites metodologicos

- No se usa VMAF.
- No se modifica `qoe_linear_v1`.
- No se ejecuta benchmark.
- No se declara ranking, ganador ni mejora de QoE.
- La simulacion completa de ventana solo se usa para crear labels offline.
- El modelo no recibe `trace_id`, `dataset_id`, `split`, `leakage_group`,
  `hybrid_source_teacher`, QoE futuro ni throughput futuro como feature.
- El resultado es un segundo modelo offline exportable, no un controller
  integrado.

## Rutas externas

Datos:

```text
C:\Users\danie\Documents\TFG\datasets_normalizados\phase4\phase4H_datos_teacher_hibrido_sin_vmaf
/home/daniel/TFG/datasets_normalizados/phase4/phase4H_datos_teacher_hibrido_sin_vmaf
```

Modelo:

```text
C:\Users\danie\Documents\TFG\modelos\phase4\phase4H_modelo_teacher_hibrido_neural_abr_lite
/home/daniel/TFG/modelos/phase4/phase4H_modelo_teacher_hibrido_neural_abr_lite
```

Bundle:

```text
C:\Users\danie\Documents\TFG\modelos\phase4\phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite
/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite
```

Validacion:

```text
C:\Users\danie\Documents\TFG\runs_trazas\phase4\phase4H_validacion_bundle_teacher_hibrido
/home/daniel/TFG/runs_trazas/phase4/phase4H_validacion_bundle_teacher_hibrido
```

## Runbook Ubuntu cliente

Crear datos:

```bash
cd ~/TFG/DashClientModular4
python scripts/build_phase4_datos_teacher_hibrido.py --overwrite
python scripts/validate_phase4_datos_teacher_hibrido.py
```

Entrenar y revisar:

```bash
python scripts/entrenar_phase4_modelo_teacher_hibrido.py --overwrite --epochs 20 --batch-size 64
python scripts/revisar_phase4_modelo_teacher_hibrido.py
```

Exportar y validar bundle:

```bash
python scripts/exportar_phase4_bundle_teacher_hibrido.py --overwrite
python scripts/validar_phase4_bundle_teacher_hibrido.py
```

## Interpretacion

Este modelo aprende a aproximar la accion del experto clasico que mejor
resultado obtiene por ventana bajo `qoe_linear_v1`. Academicamente es una
variante de multi-teacher imitation learning / algorithm selection.

Si pasa los gates, Phase 4 queda con dos bundles offline:

- `robust_mpc`: imitacion de un teacher fijo fuerte.
- `teacher_hibrido`: imitacion de un experto compuesto por seleccion offline.

La comparacion formal entre ambos queda reservada para una fase de evaluacion
autorizada.
