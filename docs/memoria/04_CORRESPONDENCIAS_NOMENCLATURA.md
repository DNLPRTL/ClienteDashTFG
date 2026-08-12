# Correspondencias de nomenclatura — plan viejo (repo) → entregable (TFG Material)

> Tabla de traducción OBLIGATORIA para redactar la memoria. El plan maestro (00) y
> los docs del repo usan la nomenclatura vieja inglesa (junio); la memoria describe
> EXCLUSIVAMENTE el código del entregable
> `C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG` (castellanizado,
> podado, 5 controladores). Si el repo y TFG Material discrepan, manda TFG Material.
> Verificado contra el árbol real del entregable y el paquete canónico (12/08/2026).

| Campo | Valor |
|---|---|
| Fecha | 2026-08-12 |
| Código canónico | `TFG Material\01_codigo\ClienteDashTFG` (81 .py, sin tests/docs) |
| Evidencia canónica | `TFG Material\04_evidencia_final\20260810_133520_tfg_final` (300 sesiones, 5 controladores, gates 8/8) |

## 1. Controladores (registro real: 6 claves, 5 en el experimento)

| Viejo (repo/docs) | Clave entregable | Clase | Fichero | Nombre en gráficas/memoria |
|---|---|---|---|---|
| `rate_based` | `basado_en_tasa` | `ControladorBasadoEnTasa` | `core/controladores/basado_en_tasa.py` | Rate Based |
| `bba` | `bba` | `ControladorBba` | `core/controladores/bba.py` | BBA |
| `bola` | `bola` | `ControladorBola` | `core/controladores/bola.py` | BOLA |
| `mpc` (FastMPC) | `mpc` | `ControladorMpc` | `core/controladores/mpc.py` | MPC (implementado; NO corre en el experimento final — se evalúa su variante robusta) |
| `robust_mpc` | `mpc_robusto` | `ControladorMpcRobusto` | `core/controladores/robust_mpc.py` | Robust MPC |
| `mpc_prudente_v2` / "temporal" / "MPC Neuronal Prudente" | `controlador_propio` | `ControladorPropio` | `core/controladores/controlador_propio.py` | **Controlador propio** |
| `mpc_prudente_v1` (MLP) | — ELIMINADO del entregable | — | — | Solo cap 7.5 como iteración de diseño descartada ("variante MLP previa del predictor") |

## 2. Módulos y carpetas

| Viejo | Entregable | Nota |
|---|---|---|
| `player.py` (clase `Player`) | `reproductor.py` (clase `Reproductor`) | raíz del proyecto |
| `core/parser/` | `core/analizador_mpd/` (`ParserBase`, `ParserDash`) | |
| `core/engine/` fake | `core/motores/simulado.py` (`MotorSimulado`, base `MotorVideoBase`) | motor de la evaluación formal |
| `core/engine/` gstreamer | `core/motores/gstreamer.py` (`MotorGStreamer`) | reproducción real, smokes |
| `core/trace_replay/` | `core/reproduccion_trazas/` (`ModeloRedPorTraza`, `DescargadorControladoPorTraza`, `TrazaCargada`) | emulación de red |
| `core/controller/` | `core/controladores/` (contrato, registro, máscara, `ConstructorEntradas`, `DiagnosticosRed`, `seguridad_red`) | |
| `core/mpc_prudente/` | `core/modelo_propio/` (`modelo.py`, `bundle.py`→`BundleModelo`, `planificador.py`, `perfil_video.py`, `escalera_contenido.py`→`EscaleraContenido`, `estado_sesion.py`→`EstadoSesion`, `artefactos.py`, `integridad.py`) | |
| `core/phase6/` (o `core/fase6/`) | `core/evaluacion/` (`analisis.py`, `catalogo.py`, `configuracion.py`, `qoe.py`, `seleccion.py`, `verificacion.py`) | |
| `core/qoe.py` | `core/evaluacion/qoe.py` (`PesosQoE`, `ResultadoQoE`, `calcular_qoe_lineal`) | |
| `core/phase45_v1/` + `core/phase45_v3/` + `core/neural_abr/` | `entrenamiento/` (top-level, NO en core): `corpus_trazas/`, `simulador_sesiones.py` (`EntornoSesion`), `dataset_cuantiles.py`, `dataset_fiel.py`, `entrenamiento_modelo.py`, `exportar_bundles.py`, `politicas_rollout.py` | regla: "si no se ejecuta al lanzar, no vive en core" |
| `media_profiles/segment_sizes/` | `perfiles_video/tamanos_segmentos/` | tablas VBR (raíz del proyecto) |
| `config/phase6.local.json` | `config/evaluacion.local.json` (ejemplo: `evaluacion.local.example.json`) | |

## 3. Scripts

| Viejo | Entregable |
|---|---|
| `scripts/run_phase6_validacion_comparativa.py` / `ejecutar_fase6.py` | `scripts/3_evaluacion/ejecutar_evaluacion.py` |
| `scripts/gui_fase6.py` | `scripts/3_evaluacion/gui_evaluacion.py` (`InterfazEvaluacion`) |
| `scripts/analizar_resultados_fase6.py` | `scripts/3_evaluacion/analizar_resultados.py` |
| — | `scripts/3_evaluacion/verificar_paquete.py` |
| `scripts/generar_dataset_mpc_prudente.py` + wrappers | `scripts/2_entrenamiento/generar_dataset.py` + `wsl_generar_dataset.sh` |
| `scripts/entrenar_*_mpc_prudente*` | `scripts/2_entrenamiento/entrenar_modelo.py` + `wsl_entrenar_modelo.sh` |
| `scripts/export/empaquetar bundle temporal` | `scripts/2_entrenamiento/exportar_bundle.py` + `wsl_exportar_bundle.sh` |
| `scripts/extraer_tamanos_reales_segmentos.py` | `scripts/1_contenido/extraer_tamanos_reales_segmentos.py` |
| `scripts/servidor/*.sh` | `scripts/1_contenido/herramienta_video.sh` + `generar_dash_lote.sh` |
| `scripts/comprobar_cliente.py` (readiness) | — NO existe en el entregable (vive solo en el repo; la memoria no lo cita) |
| `tests/` (489 tests) | — NO existen en el entregable (validación descrita como parte del proceso, no del producto entregado) |

## 4. Datos y artefactos

| Viejo | Entregable / canónico |
|---|---|
| `phase3_trace_manifest_curated.json` | `catalogo_trazas.json` (raíz de `02_corpus_red`; 6768 trazas, 12 datasets, splits por `leakage_group`) |
| `datasets_normalizados/phase3/final/schema_v1/<ds>/` | `datasets_normalizados/<ds>/` (aplanado) |
| `~/TFG/modelos/mpc_prudente/temporal_runtime_bundle_v1` | `modelos/modelo_propio/bundle` (id `bundle_modelo_propio_v1`; en `03_modelos`) |
| bundle v1 MLP (`runtime_bundle_v1`) | eliminado → `legacy/` (no se describe) |
| `throughput_quantile_full_v1_multimedia` | `datasets_normalizados/modelo_propio/dataset_entrenamiento` (`datos_entrenamiento.jsonl`, `datos_validacion.jsonl`, `resumen_dataset.json`; en `06_dataset_entrenamiento`) |
| salida `~/TFG/runs_trazas/phase6/validacion_comparativa/` | `~/TFG/validacion_comparativa/` |
| paquete `20260624_182747_tfg_final` (360 sesiones, 6 ctrl) | **`20260810_133520_tfg_final` (300 sesiones, 5 ctrl)** — ÚNICA fuente de números |
| ficheros del paquete: `session_summary.csv` / `raw_chunks.csv` / `aggregates_by_controller.json` / `statistics.json` / `plot_manifest.json` / `resultados_para_validar.md` | `sesiones.csv` / `segmentos.csv` / `agregados_por_controlador.json` / `estadistica.json` / `graficas.json` / `resumen_resultados.md` |
| telemetría `segment_telemetry.csv` | `telemetria_segmentos.csv` (por ejecución: `manifiesto_ejecucion.json`, `config_resuelta.json`, `entorno.json`, `ejecucion.log`) |
| columnas `timestamp_s,duration_s,throughput_kbps` | `tiempo_s,duracion_s,throughput_kbps` |
| métrica `qoe_linear_mean` | columna `qoe_lineal_media` (concepto en la memoria: "QoE lineal media"; fórmula congelada intacta) |

## 5. Términos en la PROSA de la memoria (qué decir y qué NO decir)

| Concepto | Término en la memoria | PROHIBIDO en la memoria |
|---|---|---|
| El controlador IA | "el controlador propio" (y en su presentación: "controlador propio basado en predicción de throughput con incertidumbre y planificación MPC consciente del riesgo") | "MPC Neuronal Prudente", "mpc_prudente", "v1"/"v2", "temporal ensemble" como marca |
| El predictor | "el modelo de predicción" / "predictor de cuantiles de throughput" (ensemble de 5 redes recurrentes GRU) | "modelo v2", "predictor temporal v2" |
| El planificador | "el planificador MPC del controlador propio" (coste CVaR, α=0.75 fijo) | "planner prudente" como nombre propio |
| La evaluación formal | "la evaluación comparativa (formal)" / "el protocolo de evaluación" | "Phase 6", "fase 6", "tfg_final" como nombre (el id del paquete puede citarse en el anexo de reproducibilidad) |
| Fases del proyecto (cap 3) | nombres descriptivos en español ("desarrollo del cliente", "corpus de trazas", "entrenamiento del modelo"...) | "Phase 1..7", "phase45_v1/v3", "rebuild" |
| Líneas IA abandonadas (cap 7.5) | descripciones funcionales: "políticas de clonación de comportamiento" (SPBC), "función de puntuación con horizonte" (Q_H), "variante MLP del predictor" | los nombres clave internos, salvo necesidad |
| Smokes/validaciones | "pruebas de humo" / "verificación funcional" | "smoke" a secas (anglicismo evitable) |
| Préstamos técnicos aceptados | throughput, bitrate, buffer, QoE, bundle, dataset, stall/rebuffering, ranking, benchmark, gates, preset | — |

**IDs internos conservados como DATOS** (pueden aparecer si el tribunal abre artefactos;
respuesta preparada: "identificadores internos de formato heredados del desarrollo"):
`schema_id`/`model_key` del bundle precintado (`mpc_prudente_temporal_*`), formato de
`id_ventana` (`..._phase45v1_start_...`), semillas (`phase45_*`), claves torch
(`member_state_dicts`, `gru.*`/`head.*`).

## 6. Números de entorno que cambian respecto a docs viejos

| Doc viejo dice | La memoria dice (canónico 10/08) |
|---|---|
| 360 sesiones, 6 controllers, 288 reales | **300 sesiones, 5 controladores, 240 reales + 60 sintéticas (diagnóstico aparte)** |
| 489 tests / readiness 104 checks | no se citan (el entregable no lleva tests; el proceso de validación se describe en cap 3/anexos si hace falta) |
| QoE propio 2.013 / robust 1.947 (junio) | QoE propio **2.0097** / rate **1.9701** / robusto **1.9471** / bba **1.7874** / bola **1.2439** |
| `componentes_experimento.md` "6 controllers, 360 sesiones" | mismo doc vale para versiones/máquinas, pero conteos = paquete canónico |
