# Contexto de Inicio para Phase 6

Status: handoff_ready.

Este documento recoge el estado minimo para abrir Phase 6 en un hilo nuevo.

## Estado cerrado

- Phase 1 cerrada: cliente modular, artifacts canonicos, readiness y neutralidad
  de benchmark.
- Phase 2 cerrada: controllers clasicos `rate_based`, `bba`, `bola`, `mpc` y
  `robust_mpc` implementados desde specs locales.
- Phase 3 Rebuild cerrada: trazas normalizadas, manifests y politica de splits.
- Phase 3.5 cerrada: QoE `qoe_linear_v1`, gates y no-ranking.
- Phase 4 cerrada: dos bundles offline NeuralABR-Lite.
- Phase 5 cerrada: dos controllers IA integrados:
  `neural_abr_lite_robust_mpc` y `neural_abr_lite_teacher_hibrido`.
- Fase de Verificacion cerrada en Ubuntu: cliente y controllers clasicos
  verificados con informe externo aceptado.

## Evidencia de verificacion

Ubuntu cliente reporto:

```text
python scripts/check_client_readiness.py --strict
-> 88 OK / 0 WARN / 0 FAIL

curl -I http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd
-> HTTP/1.1 200 OK

python scripts/verificar_cliente_y_controllers_clasicos.py --mpd-url http://192.168.1.132/dash/Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd
-> Status: accepted
```

Informe externo:

```text
/home/daniel/TFG/runs_trazas/fase_verificacion_cliente_y_controllers_clasicos/informe_verificacion_cliente_y_controllers_clasicos.md
```

El informe confirma:

- cinco controllers clasicos aceptados;
- runs contra servidor con artifacts canonicos;
- ausencia de `dataset.csv` y `dataset_training.csv`;
- `evaluation_segments.csv` limpio;
- ausencia de columnas IA en runs clasicos;
- no benchmark, no ranking, no ganador y no mejora QoE.

## Controllers disponibles para Phase 6

Clasicos:

```text
rate_based
bba
bola
mpc
robust_mpc
```

IA:

```text
neural_abr_lite_robust_mpc
neural_abr_lite_teacher_hibrido
```

No usar sanity/debug controllers como baselines academicos salvo control
tecnico explicitamente etiquetado.

## Guardrails para Phase 6

- No convertir smokes de Phase 5 ni de la Fase de Verificacion en benchmark.
- No mezclar red rapida de adaptador puente con evaluacion formal.
- No declarar ganador hasta que Phase 6 congele protocolo, trazas, media
  profile, QoE, seeds, gates y estadistica.
- Mantener separados artifacts runtime, trazas, modelos, bundles y resultados.
- Mantener fuera de Git runs, CSVs generados, modelos, bundles, zips y paquetes
  de evidencia.

## Proxima tarea

Phase 6 debe empezar definiendo el contrato de evaluacion formal:

- que controllers entran;
- que MPDs/media profiles se usan;
- que trazas/splits se usan;
- como se aplica el replay o control de red;
- que rows son evaluables;
- como se calcula `qoe_linear_v1`;
- como se agregan resultados;
- que condiciones autorizan ranking final.
