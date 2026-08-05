# Castellanización del código entregable (línea propia + Phase 6)

| Campo | Valor |
|---|---|
| Fecha | 2026-08-05 |
| Alcance | `core/mpc_prudente/`, `core/controller/mpc_prudente_runtime.py`, `core/phase6/`, scripts y tests de la línea |
| Regla | Todo lo que se muestra, en castellano (sin tildes ni enie en IDENTIFICADORES). Cero cambio funcional. |
| Prueba de compatibilidad | Re-análisis del paquete `tfg_final` con código viejo vs nuevo EN LA MISMA MÁQUINA → salidas byte a byte IDÉNTICAS (aggregates, statistics, raw_chunks, session_summary, markdown). Gates OK, ranking autorizado. |
| Validación | 489 tests OK · readiness strict 104 OK/0 FAIL · compileall OK |

## 1. La frontera: qué se tradujo y qué NO (y por qué)

**SÍ (todo lo visible del código):** nombres de módulos .py de la línea propia y
de Phase 6, clases, funciones, constantes, variables, parámetros propios,
mensajes de error, comentarios y docstrings.

**NO (contrato de datos — cambiarlo rompería lo que quieres conservar):**
1. **Claves de JSON/CSV generados** (`qoe_linear_mean`, `session_id`,
   `controller_key`, `best_epoch`...): son el schema del paquete de evidencia ya
   generado; si cambian, el análisis nuevo no podría leer/reproducir el paquete
   congelado.
2. **Nombres de ficheros generados** (`session_summary.csv`, `raw_chunks.csv`,
   `statistics.json`, `manifest.json`, `model_config.json`,
   `modelo_temporal_ensemble.pt`...): los bundles YA exportados en Ubuntu/WSL
   contienen esos nombres con hash sha256; el resume/verificación del paquete
   también depende de ellos. (Muchos ya estaban en castellano:
   `resultados_para_validar.md`, `verificacion_paquete.json`, `reporte_*.json`.)
3. **Claves de config** (`bundle_dir`, `risk_alpha`, `media_profile_id`,
   `paths`, `experiment`...): tu `config/phase6.local.json` de Ubuntu y los 360
   client_configs del paquete usan esas claves.
4. **Claves de registry** `mpc_prudente_v1` / `mpc_prudente_v2` y `schema_id`s.
5. **Interfaz congelada**: métodos que replican `ContentLadder`/`BaseController`
   (`segment_size_bytes`, `bitrate_bps`, `calcControlAction`...), atributos de
   `NeuralAbrDiagnostics`, kwargs de APIs congeladas de `phase45_v3`/`neural_abr`,
   y los atributos `gru`/`head` del modelo (sus nombres forman las claves del
   `state_dict` guardado en los checkpoints ya entrenados).
6. **Convención declarada**: las variables que transportan un campo del contrato
   conservan el nombre del campo (`risk_alpha`, `downside_widen`, `buffer_s`...).
   Préstamos técnicos asentados en los propios docs del TFG se mantienen:
   *bundle, runtime, gates, fallback, ladder (en la interfaz), Phase 6*.
7. **Nombres de scripts** (`scripts/*.py|.sh`) y flags CLI (`--preset`,
   `--config`): tus comandos de siempre funcionan tal cual.
8. **Módulos congelados** de fases cerradas (`core/phase45_v3`, `core/neural_abr`,
   player, controllers clásicos, evaluación): no se tocan por contrato.

## 2. Mapa de módulos (git mv)

| Antes | Ahora |
|---|---|
| core/mpc_prudente/media_profile.py | core/mpc_prudente/perfil_medio.py |
| core/mpc_prudente/dataset.py | core/mpc_prudente/dataset_fiel.py |
| core/mpc_prudente/training.py | core/mpc_prudente/entrenamiento.py |
| core/mpc_prudente/temporal_model.py | core/mpc_prudente/modelo_temporal.py |
| core/mpc_prudente/temporal_training.py | core/mpc_prudente/entrenamiento_temporal.py |
| core/mpc_prudente/planner.py | core/mpc_prudente/planificador.py |
| core/mpc_prudente/temporal_bundle.py | core/mpc_prudente/bundle_temporal.py |
| core/mpc_prudente/evaluation.py | core/mpc_prudente/diagnostico.py |
| core/phase6/analysis.py | core/phase6/analisis.py |
| core/phase6/catalog.py | core/phase6/catalogo.py |
| core/phase6/selection.py | core/phase6/seleccion.py |
| core/phase6/config.py | core/phase6/configuracion.py |
| core/phase6/verification.py | core/phase6/verificacion.py |

`bundle.py` conserva su nombre (préstamo usado en toda la documentación) y
`mpc_prudente_runtime.py` también (ídem "runtime"). `core/phase6/` se queda
porque "Phase 6" es nombre propio de fase en todo el proyecto.

## 3. Renombres principales de API (el resto, en el diff del commit)

| Antes | Ahora |
|---|---|
| MediaFaithfulLadder / MediaProfileSegmentSizes | EscaleraFiel / PerfilTamanosSegmentos |
| build_mpc_prudente_(multimedia_)dataset | construir_dataset_(multimedia_)mpc_prudente |
| train_mpc_prudente_predictor | entrenar_predictor_mpc_prudente |
| TemporalQuantilePredictor / ensemble_quantiles | PredictorTemporalCuantiles / combinar_cuantiles_ensemble |
| train_mpc_prudente_temporal_ensemble | entrenar_ensemble_temporal_mpc_prudente |
| plan_prudent_action / PrudentDecision / buffer_risk_alpha | planificar_accion_prudente / DecisionPrudente / alpha_riesgo_por_buffer |
| PrudentMpcController (offline) | ControllerMpcPrudente |
| export/validate bundle (+temporal) | exportar_bundle_/validar_dir_bundle_ (+_temporal_) mpc_prudente |
| MpcPrudenteRuntimeBundle / load_prudent_runtime_bundle | BundleRuntimeMpcPrudente / cargar_bundle_runtime_prudente |
| MpcPrudente(Temporal)RuntimeController | ControllerRuntimeMpcPrudente(Temporal) |
| analyze_phase6_run / verify_phase6_package | analizar_paquete_phase6 / verificar_paquete_phase6 |
| aggregate_summaries / paired_statistics / evaluate_gates | agregar_resumenes / estadistica_pareada / evaluar_gates |
| select_trace_windows / load_trace_manifest | seleccionar_ventanas_trazas / cargar_manifest_trazas |
| load_phase6_config / preset_spec / discover_comparable_controllers | cargar_config_phase6 / especificacion_preset / descubrir_controllers_comparables |
| bootstrap_ci / sign_test_exact | intervalo_confianza_bootstrap / test_de_signos_exacto |

Mensajes de error y docstrings de excepciones también en castellano.

## 4. Cómo se garantizó "cero cambio funcional"

1. Renombrado programático con máscara de string-literals: ningún literal de una
   línea (donde viven todas las claves de datos) pudo ser modificado.
2. Suite completa tras cada paso: 489/489 OK, readiness strict PASS.
3. Prueba de oro: copia del paquete `20260624_182747_tfg_final` re-analizada con
   el código ANTERIOR (clon del commit previo) y con el NUEVO en el mismo
   Windows: los 6 artefactos de `02_resultados` salieron byte a byte idénticos
   (la única diferencia fue la ruta absoluta de cada copia). Nota: contra los
   resultados originales generados en Ubuntu hay diferencias de ~1e-14 por coma
   flotante entre plataformas — ya existían antes de este cambio y no afectan a
   ninguna cifra reportada (4 decimales).

## 5. Impacto en tus comandos

NINGUNO. `bash scripts/run_mpc_prudente_*.sh`, `python3 scripts/run_phase6_...py
--config ... --preset tfg_final`, la GUI, `python -m unittest discover` y
`check_client_readiness.py --strict` funcionan exactamente igual. Los bundles ya
exportados cargan sin re-exportar (se verificó que nombres de ficheros del
bundle, claves de checkpoint y state_dict no cambian).
