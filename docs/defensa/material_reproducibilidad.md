# Material exacto de la parte técnica (inventario de reproducibilidad)

Fecha: 2026-08-05. Pregunta que responde: **si quisiera repetir el experimento
final (Phase 6 `tfg_final`) en cualquier PC del mundo, ¿qué tendría que mover?**

Son 4 bloques. Todo lo que no está aquí es documentación, histórico o líneas
abandonadas: no hace falta para reproducir.

---

## Bloque 1 — El repositorio (código). Se mueve con `git clone`

Rama: `rebuild/phase3-from-phase2`. Dentro del repo, lo que realmente ejecuta el
experimento:

### Cliente DASH (congelado, común a todos los controllers)
```text
main.py                      # punto de entrada de una sesión
player.py                    # bucle de reproducción
core/parser/                 # parser del MPD
core/downloader.py           # descarga de segmentos
core/media_engine/           # motores de reproducción (fake para Phase 6)
core/runtime_feedback.py     # feedback que ve cualquier controller
core/client_config.py        # config de sesión
core/output_artifacts.py     # telemetría por segmento (segment_telemetry.csv)
core/trace_replay/           # replay de trazas de red (la "red" del experimento)
core/evaluation/             # QoE congelada (qoe_linear_v1)
```

### Controllers (los 6 comparados)
```text
core/controller/registry.py             # registro por nombre
core/controller/rate_based.py           # baseline Liu 2011
core/controller/bba.py                  # baseline Huang 2014 (BBA-0)
core/controller/bola.py                 # baseline Spiteri 2016 (BOLA-BASIC)
core/controller/mpc.py                  # baseline Yin 2015 (FastMPC)
core/controller/robust_mpc.py           # baseline Yin 2015 (RobustMPC)
core/controller/mpc_prudente_runtime.py # NUESTROS v1 y v2 (runtime)
```

### Línea propia MPC Prudente (entrenamiento + planner + bundles)
```text
core/mpc_prudente/media_profile.py     # ladder con tamaños VBR reales
core/mpc_prudente/dataset.py           # dataset fiel (single y multi-vídeo)
core/mpc_prudente/training.py          # entrenamiento MLP + calibración (v1)
core/mpc_prudente/temporal_model.py    # GRU + ensemble_quantiles (v2)
core/mpc_prudente/temporal_training.py # entrenamiento del ensemble (v2)
core/mpc_prudente/planner.py           # planner CVaR con tamaños reales
core/mpc_prudente/bundle.py            # bundle runtime v1 + helpers comunes
core/mpc_prudente/temporal_bundle.py   # bundle runtime v2 + dispatcher
core/mpc_prudente/evaluation.py        # diagnóstico closed-loop offline
core/phase45_v3/                       # base reutilizada (dataset cuantiles, env closed-loop, MLP)
core/neural_abr/                       # base reutilizada (features, safety, bundles, ladder)
```

### Phase 6 (evaluación formal)
```text
core/phase6/catalog.py       # presets (tfg_final) y perfiles de medio
core/phase6/selection.py     # selección determinista de ventanas eval
core/phase6/config.py        # carga de config
core/phase6/analysis.py      # métricas, estadística pareada, gates, plots
core/phase6/verification.py  # verificación automática del paquete
scripts/run_phase6_validacion_comparativa.py   # runner (orquesta las 360 sesiones)
```

### Datos versionados y scripts
```text
media_profiles/segment_sizes/*.json    # 8 tablas VBR reales (COMMITEADAS)
scripts/extraer_tamanos_reales_segmentos.py
scripts/run_mpc_prudente_multimedia_dataset_wsl.sh   # (re-entrenar) dataset
scripts/run_mpc_prudente_temporal_training_wsl.sh    # (re-entrenar) ensemble
scripts/run_mpc_prudente_temporal_bundle_wsl.sh      # (re-entrenar) export bundle
scripts/check_client_readiness.py
config/phase6.example.yaml             # plantilla de config
tests/                                 # 489 tests
```

---

## Bloque 2 — Artefactos externos (fuera de git). Se mueven a mano

| Qué | Ruta canónica (máquina de referencia) | Tamaño aprox | ¿Imprescindible? |
|---|---|---|---|
| Manifest curado de trazas | `~/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json` | MB | SÍ |
| Trazas normalizadas (CSV) | `~/TFG/datasets_normalizados/phase3/final/schema_v1/<dataset>/...` | GB | SÍ (al menos las del split eval) |
| Bundle modelo v1 (MLP) | `~/TFG/modelos/mpc_prudente/runtime_bundle_v1/` | MB | SÍ |
| Bundle modelo v2 (ensemble) | `~/TFG/modelos/mpc_prudente/temporal_runtime_bundle_v1/` | MB | SÍ |
| Config local | `config/phase6.local.json` (en el repo del cliente, no versionada) | KB | SÍ (adaptar rutas) |
| Dataset de entrenamiento | `~/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_multimedia/` | GB | Solo para RE-ENTRENAR |

Los bundles son autocontenidos: modelo + normalización + config del planner +
manifiesto con sha256. El cliente verifica los hashes al cargar.

## Bloque 3 — Contenido DASH (servidor)

Un servidor HTTP (en el TFG: VM Ubuntu, `/var/www/html/dash`) sirviendo los 4
vídeos del experimento, cada uno con su MPD, inits y segmentos de 4 s:

```text
Paseo_Almunecar_10min_30fps/4sec/  +  Paseo_Almunecar_10min_60fps/4sec/
Blender_Sunflower_10min_30fps/4sec/  +  Blender_Sunflower_10min_60fps/4sec/
```

Las URLs concretas están en `core/phase6/catalog.py` (MEDIA_PROFILES); en otro PC
basta cambiar la IP en la config local. Los 6 niveles son
300/750/1200/1850/2850/4300 kbps, codificación VBR (por eso existen las tablas del
Bloque 1).

## Bloque 4 — La evidencia generada (no hace falta para re-ejecutar, sí para auditar)

```text
~/TFG/runs_trazas/phase6/validacion_comparativa/20260624_182747_tfg_final/
  00_protocolo/   # protocolo, plan de sesiones, configs de cliente exactas
  01_ejecucion/   # 360 runs con telemetría cruda por segmento + logs
  02_resultados/  # CSVs, estadística, gates, verificación
  03_graficas/    # 16 plots
  04_informe/     # informes markdown
```

Este paquete permite re-derivar TODOS los números de la memoria sin re-ejecutar
nada (`analyze_phase6_run` sobre el paquete los recalcula desde la telemetría).

---

## Receta mínima de reproducción (otro PC, Linux)

1. `git clone` + checkout de la rama; `pip install -r requirements.txt`.
2. Copiar Bloque 2 (manifest + trazas eval + 2 bundles) respetando rutas o
   adaptando `config/phase6.local.json`.
3. Servir el contenido DASH (Bloque 3) y apuntar las URLs.
4. `python -m unittest discover` y `python scripts/check_client_readiness.py --strict`.
5. `python3 scripts/run_phase6_validacion_comparativa.py --config config/phase6.local.json --preset tfg_final`
   (~12.5 h estimadas; selección de ventanas y semillas deterministas → mismas
   trazas y mismos escenarios que el paquete original).

## Qué es redundante (NO mover)

- Líneas abandonadas: `core/phase45_v1` SPBC (solo evidencia negativa), Q_H scorer,
  bundles de NeuralABR-Lite y Neural-MPC v1/v2 viejos (salvo que se quiera
  reproducir la comparativa histórica).
- `docs/` completo (contexto de desarrollo), `analysis_output/`, `logs/`, `tmp/`,
  paquetes Phase 6 antiguos (diagnostico/rapido), datasets brutos originales
  (el manifest + normalizadas ya son el corpus curado).
