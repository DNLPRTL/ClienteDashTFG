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
core/mpc_prudente/perfil_medio.py           # escalera con tamaños VBR reales
core/mpc_prudente/dataset_fiel.py           # dataset fiel (single y multi-vídeo)
core/mpc_prudente/entrenamiento.py          # entrenamiento MLP + calibración (v1)
core/mpc_prudente/modelo_temporal.py        # GRU + ensemble (v2)
core/mpc_prudente/entrenamiento_temporal.py # entrenamiento del ensemble (v2)
core/mpc_prudente/planificador.py           # planner CVaR con tamaños reales
core/mpc_prudente/bundle.py                 # bundle runtime v1 + helpers comunes
core/mpc_prudente/bundle_temporal.py        # bundle runtime v2 + dispatcher
core/mpc_prudente/diagnostico.py            # diagnóstico closed-loop offline
core/phase45_v3/                       # base reutilizada (dataset cuantiles, env closed-loop, MLP)
core/neural_abr/                       # base reutilizada (features, safety, bundles, ladder)
```

### Phase 6 (evaluación formal)
```text
core/fase6/catalogo.py      # presets (tfg_final) y perfiles de medio
core/fase6/seleccion.py     # selección determinista de ventanas eval
core/fase6/configuracion.py # carga de config
core/fase6/analisis.py      # métricas, estadística pareada, gates, plots
core/fase6/verificacion.py  # verificación automática del paquete
scripts/ejecutar_fase6.py   # runner (orquesta las 360 sesiones)
```

### Datos versionados y scripts
```text
media_profiles/segment_sizes/*.json    # 8 tablas VBR reales (COMMITEADAS)
scripts/extraer_tamanos_reales_segmentos.py
scripts/generar_dataset_multimedia_mpc_prudente_wsl.sh   # (re-entrenar) dataset
scripts/entrenar_temporal_mpc_prudente_wsl.sh    # (re-entrenar) ensemble
scripts/exportar_bundle_temporal_mpc_prudente_wsl.sh      # (re-entrenar) export bundle
scripts/comprobar_cliente.py
config/fase6.example.yaml             # plantilla de config
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

Las URLs concretas están en `core/fase6/catalogo.py` (MEDIA_PROFILES); en otro PC
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
nada (`analizar_paquete_fase6` sobre el paquete los recalcula desde la telemetría).

---

## Receta mínima de reproducción (otro PC, Linux)

1. `git clone` + checkout de la rama; `pip install -r requirements.txt`.
2. Copiar Bloque 2 (manifest + trazas eval + 2 bundles) respetando rutas o
   adaptando `config/phase6.local.json`.
3. Servir el contenido DASH (Bloque 3) y apuntar las URLs.
4. `python -m unittest discover` y `python scripts/comprobar_cliente.py --strict`.
5. `python3 scripts/ejecutar_fase6.py --config config/phase6.local.json --preset tfg_final`
   (~12.5 h estimadas; selección de ventanas y semillas deterministas → mismas
   trazas y mismos escenarios que el paquete original).

## Qué es redundante (NO mover)

- Líneas abandonadas: `core/phase45_v1` SPBC (solo evidencia negativa), Q_H scorer,
  bundles de NeuralABR-Lite y Neural-MPC v1/v2 viejos (salvo que se quiera
  reproducir la comparativa histórica).
- `docs/` completo (contexto de desarrollo), `analysis_output/`, `logs/`, `tmp/`,
  paquetes Phase 6 antiguos (diagnostico/rapido), datasets brutos originales
  (el manifest + normalizadas ya son el corpus curado).
