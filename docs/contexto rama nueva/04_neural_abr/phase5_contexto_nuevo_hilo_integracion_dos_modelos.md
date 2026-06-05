# Phase 5 - Contexto para nuevo hilo

Copiar este texto al abrir un nuevo hilo de Codex para continuar con Phase 5.

```text
Estamos en el proyecto DashClientModular4.

Ruta Windows:
C:\Users\danie\Documents\TFG\DashClientModular4

Rama activa:
rebuild/phase3-from-phase2

GitHub:
origin/rebuild/phase3-from-phase2

IMPORTANTE: leer siempre al inicio:

docs/arquitectura y procedimientos estandar tfg dash/arquitectura_y_procedimientos_estandar_tfg_dash.md
docs/arquitectura y procedimientos estandar tfg dash/TFG_PLAN_GENERICO.md
AGENTS.md

Contexto principal:
docs/contexto rama nueva/

Contexto Phase 4 cerrado:
docs/contexto rama nueva/04_neural_abr/phase4g_cierre_modelos_offline.md
docs/contexto rama nueva/04_neural_abr/phase4f_export_bundle_inferencia.md
docs/contexto rama nueva/04_neural_abr/phase4h_teacher_hibrido_sin_vmaf.md

Estado:

Phase 1 cerrada.
Phase 2 cerrada con controllers reales: rate_based, bba, bola, mpc, robust_mpc.
Phase 3 Rebuild cerrada con manifest curado de trazas.
Phase 3.5 Rebuild cerrada con qoe_linear_v1.
Phase 4 Rebuild cerrada con dos modelos offline exportados como bundles.

Siguiente fase:
Phase 5 - integracion de dos modelos NeuralABR-Lite como controllers separados.

No hay benchmark, ranking, ganador ni claim de mejora QoE autorizado todavia.
Phase 5 debe integrar controllers y validar smokes/contratos, no comparar formalmente.

Reglas permanentes:

- No usar git add .
- No commitear datasets, JSONL, runs, logs, modelos, bundles, zips, PDFs ni videos.
- Windows desarrolla, testea, commitea y pushea.
- Ubuntu cliente valida con git pull.
- Ubuntu servidor solo sirve contenido DASH.
- No tocar runtime/player/media/controllers sin contrato y tests.
- No llamar benchmark a smokes.
- No usar dry-runs legacy como training data.
- No permitir que el modelo/controller vea trace_id, dataset_id, split, leakage_group, labels OOD ni throughput futuro como feature.

Commits recientes:

8e08d4e feat(neural-abr): train robust model from real controller
c2915c4 feat(neural-abr): add phase4 hybrid teacher model path
f5da074 feat(neural-abr): export phase4 inference bundle
b5ccc36 feat(neural-abr): add phase4 candidate training gate
4e6a419 feat(neural-abr): add phase4 offline training data pipeline

Phase 4A:

Plan de trazas externo en Ubuntu:
/home/daniel/TFG/manifests_trazas/phase4/phase4A_plan_de_trazas_para_entrenamiento

Plan de trazas externo en Windows:
C:\Users\danie\Documents\TFG\manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento

Phase 4 genero 3338 ventanas de entrenamiento y 792 de validacion.
Ventanas de 120s.
Segmentos primarios de 4s.
2s queda diagnostic-only.

Modelo 1:
NeuralABR-Lite robust_mpc

Teacher:
controller real core.controller.robust_mpc.RobustMpcController ejecutado en replay offline.

Bundle Ubuntu:
/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite

Bundle Windows:
C:\Users\danie\Documents\TFG\modelos\phase4\phase4F_bundle_para_inferencia_neural_abr_lite

Datos Ubuntu:
/home/daniel/TFG/datasets_normalizados/phase4/phase4B_datos_para_entrenamiento

Metricas Ubuntu:
training_samples=100050
validation_samples=23700
validation_teacher_agreement=0.9249367088607595
valid_action_rate=1.0
bundle_p95_latency_ms=0.12679817155003548
deterministic_rate=1.0
decision=PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G

Modelo 2:
NeuralABR-Lite teacher_hibrido

Teacher:
seleccion offline por ventana entre controllers reales:
rate_based, bba, bola, mpc, robust_mpc.

Bundle Ubuntu:
/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite

Bundle Windows:
C:\Users\danie\Documents\TFG\modelos\phase4\phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite

Datos Ubuntu:
/home/daniel/TFG/datasets_normalizados/phase4/phase4H_datos_teacher_hibrido_sin_vmaf

Metricas Ubuntu:
winner_counts:
  robust_mpc=2822
  mpc=744
  bba=267
  bola=167
  rate_based=125
validation_teacher_agreement=0.9326582278481013
valid_action_rate=1.0
bundle_p95_latency_ms=0.1200730912387371
deterministic_rate=1.0
decision=PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G

Objetivo Phase 5:

Integrar ambos bundles como controllers IA separados dentro del cliente.

Nombres propuestos de controllers:

neural_abr_lite_robust_mpc
neural_abr_lite_teacher_hibrido

Requisitos Phase 5:

- Crear contrato de integracion antes de tocar runtime.
- Cargar bundle desde ruta externa configurable.
- Validar schema, hashes y feature schema del bundle.
- Construir features runtime equivalentes a Phase 4: context_features, candidate_features, action_mask.
- No pasar metadata de traza al modelo.
- Aplicar action mask siempre.
- Fallback obligatorio si:
  - bundle ausente,
  - hash/schema invalido,
  - error de carga,
  - NaN/Inf,
  - accion invalida,
  - latencia fuera de limite,
  - feature contract incompatible.
- Fallback recomendado: robust_mpc o controller clasico seguro ya validado.
- Registrar telemetria diagnostica:
  - modelo usado,
  - bundle path,
  - selected_representation_index,
  - fallback_used,
  - fallback_reason,
  - inference_latency_ms,
  - valid_action,
  - no incluir scores completos si ensucia demasiado CSV salvo artifact diagnostico separado.
- Añadir tests unitarios y smokes.
- No ejecutar benchmark ni declarar mejoras.

Separacion:

Phase 5 integra controllers IA.
Phase 6 futura evaluara formalmente.

Validaciones base esperadas en Windows:

git status --short --branch
git diff --check
python -m unittest discover
python scripts/check_client_readiness.py --strict

Validacion en Ubuntu cliente:

cd ~/TFG/DashClientModular4
git pull --ff-only origin rebuild/phase3-from-phase2
python -m unittest discover
python scripts/check_client_readiness.py --strict

No hace falta ZIP al iniciar Phase 5 si los bundles ya existen en Ubuntu. Preparar ZIP de artifacts externos solo al cerrar fase o si hay que mover/sustituir directorios completos.
```
