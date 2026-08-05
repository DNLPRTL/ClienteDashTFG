# Apropiación del código — línea MPC Neuronal Prudente, módulo a módulo

Fecha: 2026-08-05. Objetivo: que Daniel pueda explicar CADA pieza ante el tribunal:
qué hace, por qué existe y qué decisión de diseño hay detrás.

## 0. La idea en una frase

Un controller ABR en dos piezas separadas: un **predictor neuronal** que estima
CUANTILES del throughput futuro (no un valor único: una distribución), y un
**planner MPC** que simula las próximas decisiones bajo cada cuantil usando los
**tamaños reales (VBR) de los segmentos** y elige la acción con mejor **CVaR**
(media de los peores escenarios). Aprendizaje supervisado + control clásico;
paradigma tipo Fugu/Puffer, no RL de caja negra.

Las dos causas raíz que ataca (aprendidas de los fracasos previos):
1. **Fidelidad al medio**: el Neural-MPC anterior asumía CBR (`bitrate × 4s / 8`),
   pero los vídeos reales son VBR: un segmento "de 4300 kbps" puede pesar bastante
   más que su nominal → subestimas el tiempo de descarga → stall.
2. **Consciencia del riesgo**: predecir solo la media del throughput hace al
   planner optimista justo cuando la red es inestable. Con cuantiles + CVaR, la
   cola inferior de la predicción penaliza las acciones agresivas cuando hay riesgo.

## 1. `core/mpc_prudente/perfil_medio.py` — el medio de verdad

- **Qué hace:** carga `media_profiles/segment_sizes/<id>.json` (tabla extraída del
  servidor: bytes reales de cada segmento por representación) y construye
  `EscaleraFiel`, que implementa la MISMA interfaz que el `ContentLadder`
  clásico pero `segment_size_bytes(rep, seg)` devuelve el peso real.
- **Por qué así:** duck-typing. El entorno closed-loop y el planner llaman
  `ladder.segment_size_bytes(...)`; al pasarles este ladder, toda la física de
  descarga pasa a ser real SIN tocar el código congelado de `phase45_v3`.
- **Detalles defendibles:** valida schema y tamaños positivos; ordena las
  representaciones por bandwidth; si la ventana pide más segmentos que el vídeo,
  cicla (`% real_segment_count`); `resolver_id_descriptor_medio` mapea los ids
  cortos de Phase 6 (`paseo_10min_30fps_4s`) a los descriptores del MPD real.

## 2. `core/mpc_prudente/dataset_fiel.py` — dataset fiel

- **Qué hace:** reutiliza el generador de datasets de cuantiles de `phase45_v3`
  (ya probado) inyectándole un `ladder_factory` fiel. Dos variantes: un solo medio
  y **multi-vídeo** (`construir_dataset_multimedia_mpc_prudente`): cada ventana de red
  rota entre los 8 perfiles de 4 s, elegido determinísticamente por hash del
  `window_id`.
- **Por qué:** los rollouts que generan los ejemplos avanzan el buffer con la
  física real → el estado que ve el modelo en entrenamiento se parece al de
  runtime. La rotación multi-vídeo evita sesgar la dinámica de buffer a un solo
  vídeo (mata la crítica "lo ajustaste al Paseo").
- **Clave conceptual:** el TARGET (throughput futuro) es propiedad de la RED, no
  del vídeo; el medio solo cambia el estado (buffer, tiempos de descarga). Por eso
  rotar vídeos enriquece sin contaminar.

## 3. `core/mpc_prudente/entrenamiento.py` — entrenamiento v1 (MLP) + calibración

- **Qué hace:** llama al entrenador base de `phase45_v3` (pinball loss sobre
  log-ratio de throughput) y añade la auditoría que faltaba: **calibración**
  (cobertura empírica de cada cuantil ≈ nivel nominal, tolerancia 0.08) y
  **monotonía** (tasa de crossing ≤ 2%). Gates en el reporte.
- **Por qué:** para un predictor puntual basta que la loss baje; para cuantiles
  no: si q10 dice "10% de las veces el throughput cae por debajo de X" y en
  validación cae el 30%, el planner confía en una cola falsa. Calibración = el
  contrato semántico de los cuantiles.
- **Pinball loss (saber explicar):** para cuantil q, error e = y − ŷ:
  pérdida = max(q·e, (q−1)·e). Minimizarla hace que ŷ converja al cuantil q real.

## 4. `core/mpc_prudente/modelo_temporal.py` — predictor v2 (GRU + ensemble)

- **Qué hace:** `PredictorTemporalCuantiles`: una GRU lee la secuencia
  (throughput, tiempo de descarga) por paso; su estado final se concatena con los
  escalares (buffer, último bitrate, rebuffer reciente...) y un MLP saca
  `[horizon × cuantiles]`. Los cuantiles son **monótonos por construcción**:
  salida = base + acumulado de incrementos softplus (no pueden cruzarse).
- **`combinar_cuantiles_ensemble`:** combina M miembros: media por cuantil + **ensancha la
  cola inferior** restando `downside_widen × std_entre_miembros(mediana)`,
  escalado más fuerte cuanto más bajo el cuantil; re-ordena por seguridad.
- **Por qué:** (a) el MLP aplana la secuencia y pierde la tendencia; la GRU la
  capta. (b) la softplus acumulada elimina el crossing de raíz (el MLP necesitaba
  vigilarlo a posteriori). (c) la discrepancia entre miembros con semillas
  distintas estima **incertidumbre epistémica**: en ventanas raras (outages tipo
  real_012) los miembros discrepan → la cola inferior baja → el planner se vuelve
  prudente exactamente donde el v1 se pasaba de optimista.

## 5. `core/mpc_prudente/entrenamiento_temporal.py` — entrenamiento v2

- **Qué hace:** entrena M=5 GRUs (semillas base_seed + 101·m), cada una con early
  selection por mejor pinball de validación; normalización ajustada SOLO con
  train; guarda los 5 state_dicts en un checkpoint; audita la calibración de la
  predicción COMBINADA (con el ensanchado aplicado).
- **Por qué los detalles:** semillas separadas → diversidad real del ensemble;
  normalización solo-train → sin fuga de validación; calibrar el combinado (no
  cada miembro) → es lo que verá el planner.

## 6. `core/mpc_prudente/planificador.py` — el planner CVaR

- **Qué hace:** `planificar_accion_prudente` enumera TODAS las secuencias de acciones de
  horizonte 5 (6^5 = 7776). Para cada secuencia simula la trayectoria del buffer
  bajo CADA cuantil predicho: tiempo de descarga = bytes reales del segmento /
  throughput del cuantil; recompensa por paso = **la misma fórmula QoE congelada**
  (bitrate_mbps − 4.3·rebuffer − |Δbitrate|). Suma por escenario → K puntuaciones
  → agrega con `CVaR_alpha` = media de los `ceil(α·K)` peores. Elige la secuencia
  con mejor CVaR y ejecuta su primera acción (receding horizon).
- **`risk_alpha`:** configurable. Existe `alpha_riesgo_por_buffer` (menos buffer → α
  menor → más pesimista), usada en los diagnósticos offline; en el experimento
  final Phase 6 se fijó **α = 0.75** → media de los 3 peores escenarios de 4
  (q10, q25, q50), descartando el optimista q75.
- **Defensas de robustez:** re-monotoniza los cuantiles de entrada (sort), valida
  finito/positivo, y `ControllerMpcPrudente` cae a RobustMPC ante CUALQUIER
  excepción, marcando `fallback_used` (auditable; en tfg_final: 0 fallbacks).
- **Por qué CVaR y no "elegir un cuantil":** la regla clásica buffer→cuantil es
  un caso particular y descarta información; CVaR usa toda la distribución y
  tiene interpretación estándar en control con riesgo.

## 7. `core/mpc_prudente/bundle.py` y `bundle_temporal.py` — empaquetado runtime

- **Qué hacen:** exportan/validan/cargan los bundles autocontenidos (modelo,
  config, normalización, config del planner, manifiesto con sha256 de todo).
  `cargar_bundle_runtime_prudente` despacha por `schema_id` → carga MLP o ensemble.
  Los dos `predict()` convierten la salida (log-ratio sobre la media armónica del
  throughput reciente) a bps con `filas_log_ratio_a_bps`: recorte del ratio a
  [0.15, 4.0] para que una predicción disparatada no arrastre al planner.
- **Por qué:** el bundle es el contrato entre WSL (entrena) y Ubuntu cliente
  (ejecuta): hashes verificados al cargar (`torch.load(weights_only=True)`, sin
  ejecución de código arbitrario), reproducible y auditable.

## 8. `core/controller/mpc_prudente_runtime.py` — integración en el cliente

- **Qué hace:** `ControllerRuntimeMpcPrudente` (v1) y su subclase temporal (v2).
  En cada decisión: construye las features runtime (mismo builder guarded que
  Neural-MPC) → carga perezosa del bundle y de la `EscaleraFiel` del
  `media_profile_id` de la sesión (comprueba que la escalera del perfil coincide
  con la del MPD del cliente) → predice cuantiles → `planificar_accion_prudente` →
  chequeo de seguridad (acción válida en la máscara) → tasa. Ante cualquier fallo
  (features, bundle, medio, timeout de inferencia, seguridad) cae a robust_mpc
  con el motivo grabado en la telemetría.
- **Por qué:** el controller NUNCA debe tumbar al cliente ni decidir con datos
  rotos; y toda decisión neural queda auditada fila a fila (en tfg_final:
  1740/1740 auditadas por controller, 0 fallback).

## 9. `core/mpc_prudente/diagnostico.py` — diagnóstico closed-loop offline

- **Qué hace:** compara el prudente vs robust_mpc/bola/neural_mpc viejo en el
  entorno closed-loop con ladder fiel sobre ventanas de VALIDACIÓN, con suelo de
  servibilidad y estratificación por buckets. Gates de no-regresión.
- **Por qué existe:** es la etapa 5 del embudo (antes de tocar el cliente real);
  eval queda intacto para Phase 6. No es benchmark.

## 10. Phase 6 (`core/fase6/` + runner) — la evaluación formal

- `catalogo.py`: presets; `tfg_final` = 12 ventanas reales + 3 sintéticas × 4
  vídeos × 6 controllers = 360 sesiones.
- `seleccion.py`: selección DETERMINISTA de ventanas del split eval (semilla 606,
  balanceo por dataset/semántica/condición/dificultad, suelo de throughput para
  formal); reproducible en cualquier PC.
- Runner: genera el protocolo y una config de cliente POR SESIÓN (por eso el
  paquete permite auditar exactamente qué corrió cada sesión), ejecuta `main.py`
  360 veces con timeout, reanudable; **inyecta el `media_profile_id` del vídeo de
  la sesión a los controllers mpc_prudente** (multi-vídeo sin sesgo).
- `analisis.py`: recalcula la QoE desde la telemetría cruda por segmento
  (verificado a mano: coincide), agrega solo sesiones reales, estadística pareada
  por escenario (bootstrap CI + sign test exacto), gates, ranking solo si gates
  OK, 16 plots.
- `verificacion.py`: checks automáticos del paquete (sesiones completas,
  artefactos, plots no vacíos, sin legacy).

## 11. Flujo end-to-end (para contarlo de memoria)

```text
extraer tamaños VBR del servidor  →  media_profiles/segment_sizes/*.json
manifest curado Phase 3 (trazas)  →  dataset multi-vídeo fiel (WSL, GPU)
                                  →  entrenar: v1 MLP / v2 ensemble GRU (5 semillas)
                                  →  gates de calibración y monotonía
                                  →  export bundle (hashes) → mover a Ubuntu cliente
Ubuntu cliente: Phase 6 tfg_final →  360 sesiones (protocolo determinista)
                                  →  análisis pareado + gates + verificación
                                  →  paquete de evidencia 20260624_182747_tfg_final
```

## 12. Resultado y claim exacto (no exagerar)

- v2: QoE media más alta de los 6 (2.013); **empate estadístico** con robust_mpc
  (ΔQoE +0.060, CI95 [−0.05, +0.21], sign p=0.54) **con menos rebuffering**
  (stalls/sesión 0.29 vs 0.44; sesiones >5 s: 12% vs 23%).
- v2 > v1: Δ pareado +0.079 con CI95 [+0.020, +0.168] (excluye 0) → el ensemble
  temporal aporta. (El sign test no llega a significativo: p=0.12.)
- v2 gana a rate_based en 38/48 ventanas (sign p=0.0001), aunque la diferencia
  de medias no es distinguible de 0.
- Matiz de honestidad: contra robust, v2 gana 10 / pierde 14 / empata 24 ventanas;
  su ventaja es AGREGADA (evita catástrofes), no "gana la mayoría de ventanas".
- Peor caso de v2: P5 = −3.70 (peor que rate_based −1.50), concentrado en
  Blender 60fps + la traza con outage real_012.
