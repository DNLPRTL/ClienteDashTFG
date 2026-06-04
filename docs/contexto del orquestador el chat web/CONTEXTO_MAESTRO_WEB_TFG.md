# Contexto maestro normalizado — DashClientModular4

**Proyecto:** TFG DashClientModular4 — cliente DASH modular con evaluación ABR clásica e IA.
**Rol de este documento:** contexto operativo para chats futuros en el navegador, especialmente el chat que orquesta el desarrollo y prepara trabajo para Codex.
**Fuente:** normalización del documento acumulado `MENSAJE_CONTEXTUAL_DEFINITIVO.txt`.
**Estado consolidado del documento original:** Phase 1, Phase 2, Phase 3/3.5, Phase 4 y Phase 5 cerradas.
**Siguiente fase declarada en el documento original:** Phase 6 — evaluación formal.

> Este documento es un **contexto maestro**, no una orden de implementación. Sirve para que un chat futuro entienda qué se hizo, por qué se hizo, qué decisiones estaban congeladas y qué no debe tocarse sin una nueva decisión documentada.

---

## 0. Cómo usar este documento en chats futuros

En un chat nuevo del navegador, pegar este Markdown o adjuntarlo y decir:

```text
Estoy continuando el TFG DashClientModular4. Usa el documento de contexto maestro adjunto como histórico consolidado del proyecto.
No programes directamente. Primero verifica en qué fase estamos, qué decisiones están congeladas, qué se quiere reabrir si procede y qué debe hacer Codex.
```

Si el objetivo es pedir trabajo a Codex, el navegador debe:

1. Entender el estado del proyecto.
2. Separar decisión científica de implementación.
3. Crear un `.md` o prompt operativo claro para Codex.
4. Evitar que Codex improvise ciencia, metodología o métricas.
5. Exigir validaciones, tests, commit y push.
6. Sincronizar y validar en Ubuntu cuando corresponda.

---

## 1. Resumen ejecutivo

DashClientModular4 es un cliente DASH modular en Python preparado para comparar controllers ABR clásicos y un controller IA bajo condiciones reproducibles.

La evolución consolidada fue:

```text
Phase 1  -> cliente DASH modular, reproducible, ABR-neutral y con contratos claros
Phase 2  -> baselines ABR clásicos implementados y documentados
Phase 3  -> pipeline trace-driven para condiciones de red reproducibles
Phase 3.5 -> QoE/reward/gates congelados
Phase 4  -> modelo IA NeuralABR-Lite entrenado offline y exportado como bundle
Phase 5  -> controller IA neural_abr_lite integrado con safety, fallback y telemetría
Phase 6  -> evaluación formal pendiente / siguiente fase declarada
```

La idea central del proyecto es:

> No se evalúan controllers usando la red real entre VMs como benchmark principal. Se evalúan con un pipeline Python trace-driven, trazas reales normalizadas, media profiles congelados, QoE definida, gates de evaluación y protocolo formal.

---

## 2. Estado global por fases

| Fase | Estado | Resultado principal | Commit/HEAD clave |
|---|---:|---|---|
| Phase 1 | Cerrada | Cliente DASH modular endurecido, reproducible, ABR-neutral, con readiness gate | `00d4f8b` |
| Phase 2 | Cerrada | Baselines ABR clásicos implementados como controllers | `28f9741` |
| Phase 3 + 3.5 | Cerrada | Pipeline trace-driven + QoE/reward/gates | `7301cb8` |
| Phase 4 | Cerrada | Modelo IA NeuralABR-Lite Candidate Scorer entrenado offline y exportado | `3b8c6ad` |
| Phase 5 | Cerrada | Controller `neural_abr_lite` integrado con safety/fallback | `0c1018d` |
| Phase 6 | Pendiente según documento | Evaluación formal comparativa baselines + IA | No cerrada |

---

## 3. Roles de trabajo

### 3.1 Chat del navegador

El chat del navegador es el **orquestador** del proyecto.

Debe encargarse de:

- tomar decisiones metodológicas;
- leer y sintetizar papers;
- transformar PDFs/resultados en `.md` operativos;
- diseñar prompts para Codex;
- decidir fases, subfases y gates;
- auditar lo que Codex reporta;
- mantener coherencia científica;
- evitar conclusiones prematuras;
- preparar comandos Windows/Ubuntu;
- decidir cuándo avanzar de fase.

No debe actuar como un simple generador de código sin contexto.

### 3.2 Codex

Codex es el **desarrollador/ejecutor**.

Debe:

- implementar desde `.md`, specs, contratos y acceptance tests;
- no decidir ciencia;
- no leer PDFs brutos como fuente principal;
- no improvisar metodología;
- crear tests;
- ejecutar validaciones;
- hacer commit;
- hacer push a GitHub;
- reportar exactamente qué cambió, qué tests pasaron y qué queda pendiente.

Regla crítica:

> Codex no debe implementar desde ideas vagas. Primero se le da un documento operativo claro.

### 3.3 Windows físico

Windows es el entorno principal de desarrollo con Codex.

Uso previsto:

- Codex desarrolla.
- Se hacen commits.
- Se ejecutan tests.
- Se hace push a GitHub.
- Se preparan scripts, docs y validaciones.
- No es el entorno final de benchmark.

### 3.4 VM cliente Ubuntu

La VM cliente Ubuntu es el entorno de ejecución/validación final.

Uso previsto:

- sincronizar el repo;
- ejecutar scripts finales;
- alojar trazas normalizadas;
- alojar manifests finales;
- alojar bundle IA final;
- ejecutar evaluación formal;
- generar paquete de evidencia.

### 3.5 VM servidor Ubuntu

La VM servidor Ubuntu aporta contenido DASH, no la red del benchmark.

Uso previsto:

- alojar `/var/www/html/dash`;
- servir MPDs y segmentos por HTTP;
- aportar `media_profile`;
- permitir demo cliente-servidor;
- permitir pruebas end-to-end;
- no definir las condiciones de red de la evaluación formal.

Decisión central:

> El servidor aporta contenido y perfil multimedia. El pipeline Python aporta las condiciones de red reproducibles.

---

## 4. Reglas globales congeladas

Estas reglas atraviesan todo el proyecto:

1. No usar `git add .`.
2. No commitear datasets reales.
3. No commitear CSVs reales de runs.
4. No commitear logs, zips, PDFs, media, modelos, checkpoints ni TensorBoard.
5. No llamar benchmark a un smoke test.
6. No llamar training dataset a telemetría runtime.
7. No usar la red real VM cliente ↔ VM servidor como benchmark principal.
8. No mezclar train, validation, test y OOD.
9. No usar test/OOD para entrenar o ajustar.
10. No permitir que un controller vea `trace_id`, `dataset_id`, `split`, etiqueta OOD o throughput futuro.
11. No hacer ranking antes de Phase 6 formal.
12. No afirmar que IA gana a un baseline sin protocolo formal.
13. No cambiar `qoe_linear_v1` sin crear nueva versión documentada.
14. No cambiar `reward_n` sin nueva versión documentada.
15. No integrar cambios grandes sin tests y documentación.

---

## 5. Arquitectura conceptual final

```text
config YAML
  -> main.py
  -> core.client_config
  -> core.run_context
  -> parser MPD / representation ladder
  -> controller registry
  -> controller seleccionado
  -> runtime feedback
  -> downloader
  -> media engine fake o GStreamer
  -> player loop / buffer lógico / eventos
  -> run directory autosuficiente
  -> manifest + config + environment + log + CSVs
```

Artefactos canónicos de un run:

```text
run_manifest.json
config.resolved.json
environment.json
run.log
segment_telemetry.csv
evaluation_segments.csv
```

Artefactos legacy prohibidos en runs nuevos:

```text
dataset.csv
dataset_training.csv
```

---

## 6. Phase 1 — Cliente DASH endurecido

### 6.1 Objetivo

Phase 1 respondió a esta pregunta:

> ¿Existe un cliente DASH Python limpio, modular, reproducible y neutral para implementar baselines ABR e IA sin arrastrar errores, nombres legacy o metodología contaminada?

Respuesta final:

> Sí, tras Phase 1.

Phase 1 fue ingeniería del cliente, no papers, no IA y no benchmark.

### 6.2 Resultado

Phase 1 cerró con:

- cliente DASH modular endurecido;
- runner controlado por YAML;
- imports seguros;
- validación de entorno;
- layout reproducible de runs;
- fake engine estable;
- integración GStreamer endurecida;
- contrato de controller;
- contrato de benchmark neutrality;
- outputs canónicos;
- métricas catalogadas;
- readiness gate;
- documentación de arquitectura;
- tests de fragment flow y artefactos.

Commit final:

```text
00d4f8b Certify client readiness for Phase 1 closure
```

### 6.3 Qué no significó Phase 1

Phase 1 no significó:

- benchmark final;
- ranking;
- QoE final;
- reward final;
- baselines académicos;
- IA;
- GStreamer benchmark-grade;
- fake smoke como resultado experimental.

### 6.4 Subfases principales

| Bloque | Resultado |
|---:|---|
| 1 | Importability hardening |
| 2 | Config-driven runner |
| 3 | Environment/dependencies |
| 4 | Reproducible run layout |
| 5 | Fake-engine smoke path |
| 6 | Telemetry schema contract |
| 7 | Controller API / ABR decision contract |
| 8 | Deterministic test controllers |
| 9 | Runtime/player responsibility split |
| 10 | Benchmark neutrality contract |
| 11 | Academic output hygiene / legacy cleanup |
| 12 | GStreamer integration hardening |
| 13 | Phase 1 acceptance / metric provenance |
| 14 | Client readiness certification |

### 6.5 Decisiones clave

- Config YAML como entrada principal.
- Directorio de run autosuficiente.
- Separación entre telemetría runtime y benchmark final.
- Eliminación de `dataset.csv` y `dataset_training.csv` como outputs canónicos.
- Controller contract antes de baselines.
- Fake engine como camino controlado.
- GStreamer como integración/demo, no benchmark.
- Terminal drain stall no es steady-state rebuffering.
- Consola/progress bar no es autoridad experimental.
- `scripts/check_client_readiness.py --strict` como gate obligatorio.

### 6.6 Validación

Windows:

```text
96 tests OK
py_compile OK
check_environment --profile dev OK
check_environment --profile gst no estricto OK con warnings esperados
check_client_readiness.py OK
check_client_readiness.py --strict OK
```

Ubuntu:

```text
96 tests OK
py_compile OK
check_environment --profile dev OK
check_environment --profile gst --strict OK
check_client_readiness.py --strict OK
fake run final correcto
artefactos canónicos presentes
legacy ausente
```

---

## 7. Phase 2 — Baselines ABR clásicos

### 7.1 Objetivo

Phase 2 respondió a esta pregunta:

> ¿Qué baselines ABR clásicos y modernos mínimos, defendibles y portables deben existir antes de construir o evaluar IA?

Respuesta final:

- controles técnicos: `min_rate`, `fixed_rate`, `max_rate`;
- baselines académicos: `rate_based`, `bba`, `bola`, `mpc`, `robust_mpc`;
- candidatos documentados pero no implementados: SODA, RBC, Pensieve, DYNAMIC, FAST SWITCHING.

Commit final:

```text
28f9741 docs(science): formally close Phase 2 baseline work
```

### 7.2 Metodología PDF -> MD -> Codex -> tests

Flujo cerrado:

```text
PDF / paper / standard
-> paper_card.md
-> source_evidence.md
-> implementation_spec.md
-> controller_api_mapping.md
-> acceptance_tests.md
-> notes_for_memory.md
-> Codex implementation prompt
-> código Python
-> unit tests
-> fake smoke
-> docs update
-> commit
-> Ubuntu validation
```

Regla:

> Un controller no se implementa porque “parece claro”. Se implementa cuando existe documentación suficiente para que Codex no tenga que improvisar.

### 7.3 Fuentes principales

DASH / estándar:

- Stockhammer 2011 — DASH standards and design principles.
- ISO/IEC 23009-1:2022 — MPEG-DASH Part 1.

Surveys:

- Bentaleb et al. 2019 — ABR survey.
- Timmerer et al. 2025 — HTTP Adaptive Streaming review.
- Peroni & Gorinsky 2025 — end-to-end video streaming pipeline.

Baselines:

- Liu et al. 2011 — rate-based.
- Huang et al. 2014 — BBA.
- Spiteri et al. 2020 — BOLA.
- Yin et al. 2015 — MPC.
- Mao et al. 2017 — Pensieve / RobustMPC comparison context.
- Spiteri et al. 2019 — DASH reference player / practical BOLA.
- Chen et al. 2024 — SODA como candidato moderno opcional.

Trabajos locales:

- Ameigeiras et al. 2012 — YouTube traffic.
- Ramos-Muñoz et al. 2014 — mobile YouTube traffic.

### 7.4 Controllers implementados

```text
min_rate
fixed_rate
max_rate
rate_based
bba
bola
mpc
robust_mpc
```

Archivos principales:

```text
core/controller/sanity_rate.py
core/controller/rate_based.py
core/controller/bba.py
core/controller/bola.py
core/controller/mpc.py
core/controller/robust_mpc.py
core/controller/registry.py
```

Tests principales:

```text
tests/test_sanity_rate_controllers.py
tests/test_rate_based_controller.py
tests/test_bba_controller.py
tests/test_bola_controller.py
tests/test_mpc_controller.py
tests/test_robust_mpc_controller.py
tests/test_baseline_registry_audit.py
```

### 7.5 Decisiones por controller

#### `rate_based`

- throughput-based;
- usa tamaño de segmento y tiempo de descarga;
- aplica safety factor;
- elige bitrate máximo seguro;
- bajada agresiva y subida conservadora;
- no usa RTT, packet loss, congestion window ni futuro.

#### `bba`

- buffer-based;
- estilo BBA-0;
- usa `reservoir_s` y `cushion_s`;
- buffer bajo -> calidad mínima;
- buffer alto -> calidad máxima;
- entre medias -> mapeo determinista.

#### `bola`

- buffer-based / utility;
- BOLA-basic;
- usa buffer, duración de segmento, utilidad y tamaño/bitrate;
- no implementa DYNAMIC ni FAST SWITCHING;
- no pretende ser dash.js production-grade.

#### `mpc`

- híbrido;
- usa predicción de throughput, buffer y horizonte pequeño;
- enumera secuencias;
- objetivo interno provisional:
  `quality_reward - rebuffer_penalty - switching_penalty`;
- no es FastMPC ni solver externo.

#### `robust_mpc`

- MPC con predicción conservadora;
- usa error porcentual reciente;
- reduce throughput predicho;
- fallback conservador si no hay historial;
- no es IA ni Pensieve.

### 7.6 Qué no significó Phase 2

Phase 2 no significó:

- ranking;
- benchmark;
- QoE final;
- trazas/replay final;
- IA;
- validación real-world;
- que un baseline sea mejor que otro.

Frase correcta:

> Phase 2 cerró la implementación y validación estructural de los baselines ABR. La comparación formal queda para fases posteriores con trazas, QoE y protocolo reproducible.

---

## 8. Phase 3 + Phase 3.5 — Trazas, replay, QoE y gates

### 8.1 Decisión central

La evaluación académica y reproducible no se hará usando directamente la red real entre VM cliente y VM servidor.

La evaluación principal se hará con:

```text
raw dataset fuera del repo
-> converter
-> normalized_trace_schema_v1 CSV
-> schema validator
-> TraceLoader
-> TraceDrivenNetworkModel
-> TraceDrivenFakeReplayAdapter
-> controlled dry-run harness
-> controller adapter
-> trace_dry_run artifacts
-> QoE post-processor
-> qoe_run_summary / qoe_segment_rewards / qoe_artifact_manifest
-> evaluación formal posterior
```

### 8.2 Por qué no usar la red real entre VMs como benchmark

La red real puede variar por:

- host físico;
- VirtualBox/VMware;
- adaptador puente;
- cachés;
- scheduler del sistema operativo;
- CPU;
- disco;
- servidor HTTP;
- red local.

Sirve para demo, pero no garantiza comparación científica justa.

### 8.3 Trazas previstas

Primer batch previsto:

```text
HSDPA Norway / Riiser MMSys 2013
Ghent 4G/LTE Bandwidth Logs
Lancaster ABR-Throughput-Traces
```

Más adelante / OOD:

```text
Raca 4G LTE
Raca 5G
Lumos5G
```

Ruta externa:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay
```

### 8.4 Media profile

Dos opciones:

#### Opción A — estimación por bitrate

```text
segment_size_bytes = representation_bitrate_kbps * 1000 / 8 * segment_duration_s
```

Ventaja: simple y determinista.
Limitación: no captura variación real de tamaño entre segmentos.

#### Opción B — media profile real

```text
VM servidor
-> MPD + fragmentos
-> extractor de media profile
-> media_profile.json fuera del repo
-> evaluación trace-driven usa tamaños reales por segmento
```

Decisión:

> El servidor aporta contenido y perfil multimedia. El pipeline Python aporta condiciones de red reproducibles.

### 8.5 Dry-run

Un dry-run simula sesión por segmentos:

1. El controller recibe estado permitido.
2. El controller elige representación.
3. Se calcula tamaño del segmento.
4. El modelo de red calcula duración de descarga bajo la traza.
5. Se actualiza tiempo.
6. Se actualiza buffer.
7. Se calcula rebuffering.
8. Se guarda telemetría.

Ejemplo:

```text
buffer_before_s = 4.0
bitrate = 1850 kbps
segment_size = 462500 bytes
download_duration_s = 1.4
buffer_after_s = 4.0 - 1.4 + 2.0 = 4.6
rebuffer_s = 0
```

### 8.6 QoE primaria congelada

Phase 3.5 congeló:

```text
qoe_formula_version = qoe_linear_v1
```

Por segmento:

```text
q_n = bitrate_kbps_n / 1000.0

smoothness_n =
  0.0 si n == 1
  abs(q_n - q_(n-1)) si n > 1

reward_n =
  q_n
  - 4.3 * rebuffer_s_n
  - smoothness_n
```

Por sesión:

```text
qoe_linear_sum = sum(reward_n)
qoe_linear_mean = qoe_linear_sum / N
```

Métrica primaria futura:

```text
qoe_linear_mean
```

### 8.7 Métrica secundaria

`qoe_log_v1` queda como sensibilidad, no como métrica primaria.

```text
q_log_n = log(bitrate_kbps_n / min_bitrate_kbps)
reward_log_n = q_log_n - 2.66 * rebuffer_s_n - smoothness_log_n
```

### 8.8 Startup y VMAF

Startup:

- `startup_delay_s` es report-only;
- no entra en `qoe_linear_v1`;
- `startup_penalty_weight = 0.0`.

VMAF:

- deferred/artifact-dependent;
- no entra en Phase 3.5;
- no inventar QoE perceptual desde bitrate-only telemetry.

### 8.9 Gates de evaluación

Gates:

```text
use_for_eval
diagnostic_only
do_not_use_for_eval
```

Niveles:

```text
row_eval_gate
session_eval_gate
```

Regla:

> `session_eval_gate` domina si la sesión completa no es comparable.

Motivos típicos:

```text
missing_required_column
qoe_formula_not_defined
legacy_dry_run
incomplete_session
trace_split_not_allowed
controller_not_in_scope
runtime_error
non_deterministic_run
generated_before_phase_3_5a
startup_not_measured_homogeneously
vmaf_artifacts_missing
```

### 8.10 No-benchmark y no-ranking

Hasta Phase 6 formal:

```text
dry-run != benchmark
smoke run != benchmark
qoe_run_summary != benchmark aggregate
scenario order != ranking
run-level summary != ranking final
```

No escribir:

- “mejor controller”;
- “ganador”;
- “benchmark final”;
- “IA supera a X”;

si solo hay smokes o dry-runs aislados.

### 8.11 Estado final Phase 3.5

HEAD:

```text
7301cb8 docs(science): close Phase 3.5 QoE reward methodology
```

Validación final aproximada:

```text
361 tests OK
readiness strict PASS, 78 OK / 0 WARN / 0 FAIL
no IA
no training
no ranking
no benchmark
```

---

## 9. Phase 4 — Modelo IA NeuralABR-Lite offline

### 9.1 Veredicto

Phase 4 construyó, entrenó, validó offline, exportó y aceptó para integración un modelo IA propio:

```text
NeuralABR-Lite Candidate Scorer
```

Decisión:

```text
ACCEPTED_FOR_PHASE5_INTEGRATION
```

HEAD final:

```text
3b8c6ad docs(neural-abr): close Phase 4 and open Phase 5A0 gate
```

### 9.2 Qué significa Phase 4 cerrada

Significa:

- existe un modelo IA offline propio;
- método elegido por evidencia científica;
- CPU-first;
- entrenado por behavior cloning / imitation learning;
- teacher principal = `robust_mpc`;
- acción = `representation_index`;
- salida = score por representación candidata;
- action mask y contratos de features;
- trazas externas normalizadas;
- no dry-runs legacy;
- bundle inferible fuera del repo;
- validación CPU, determinismo y acciones válidas.

No significa:

- controller IA integrado;
- benchmark;
- ranking;
- mejora frente a baselines;
- SOTA;
- real-world validation.

### 9.3 Método seleccionado

```text
NeuralABR-Lite Candidate Scorer
```

Familia:

```text
small CPU-first neural ABR
behavior cloning / imitation learning
```

Teacher:

```text
robust_mpc primario
mpc secundario/comparator
bounded oracle solo diagnóstico
```

Acción:

```text
representation_index dentro de la ladder MPD
```

Salida:

```text
score por representación candidata válida
action = argmax(score_r over valid candidates)
```

Motivos de elección:

- entrenable en CPU;
- reproducible;
- explicable;
- evita RL pesado;
- compatible con `qoe_linear_v1`;
- permite action mask y fallback;
- defendible como TFG.

Por qué no PPO-first:

- coste alto;
- alta varianza;
- difícil reproducibilidad;
- riesgo de reward hacking;
- no justificado frente a imitation learning.

### 9.4 Features

`K_CONTEXT = 5`

Context features:

```text
throughput_history_bps[5]
download_time_history_s[5]
buffer_s
last_representation_index
last_bitrate_bps
recent_rebuffer_s
recent_switch_abs
chunks_remaining_norm
has_chunks_remaining
```

Candidate features:

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

Prohibido como feature:

```text
future throughput
future reward
QoE final
teacher action
trace_id
dataset_id
split
OOD label
ruta de archivo
métricas futuras
resultado benchmark
```

### 9.5 Corpus y resultados offline

Candidato Phase 4E.2:

```text
210 trazas externas normalizadas
85 Ghent 4G/LTE
5 HSDPA Norway
120 Lancaster
10 regime buckets
```

Dataset:

```text
train: 12.326 muestras
validation: 3.133 muestras
OOD diagnostic: 2.832 muestras
```

Resultados:

```text
validation valid_action_rate = 1.0
OOD valid_action_rate = 1.0
validation teacher_agreement ≈ 0.9614
OOD teacher_agreement ≈ 0.9583
correctness_failures = []
candidate_failures = []
```

Decisión:

```text
PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F
```

Limitaciones:

- HSDPA Norway infrarrepresentado;
- OOD diagnóstico, no ranking;
- teacher agreement no equivale a ganar QoE;
- no comparación formal contra baselines todavía.

### 9.6 Bundle Phase 4F

Bundle esperado:

```text
bundle_manifest.json
model_card.json
feature_schema.json
normalization_stats.json
ladder_schema.json
inference_contract.json
fallback_policy.json
model_state.pt
```

Ruta local original:

```text
C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite\phase4F\bundle_20260529_080755
```

Validación:

```text
PHASE4F_EXPORT_BUNDLE_READY_FOR_PHASE4G
sample_valid_action_rate = 1.0
deterministic_rate = 1.0
no NaN/Inf
p95 latency local ≈ 0.107–0.115 ms
```

La latencia es solo safety/local CPU check, no claim de producción.

---

## 10. Phase 5 — Integración del controller IA

### 10.1 Veredicto

Phase 5 integró el modelo NeuralABR-Lite como controller real:

```text
neural_abr_lite
```

Decisión:

```text
ACCEPTED_AS_INTEGRATED_GUARDED_CONTROLLER
```

HEAD final:

```text
0c1018d docs(neural-abr): record final Phase 5G smoke acceptance
```

ZIP limpio reportado:

```text
DashClientModular4_Phase5_closed_0c1018d.zip
```

### 10.2 Qué significa Phase 5 cerrada

Significa:

- existe controller IA real en el cliente;
- se registra como `neural_abr_lite`;
- usa API común de controllers;
- carga bundle local-only fuera del repo;
- ejecuta inferencia CPU;
- aplica action mask;
- aplica safety guard;
- usa fallback clásico si algo falla;
- nunca debe elegir representación fuera de ladder;
- devuelve rate existente en bytes/s;
- genera telemetría neural diagnóstica;
- no contamina `evaluation_segments.csv` con campos neural;
- pasa tests y readiness;
- pasó smoke estructural con bundle real;
- fue endurecido ante fallos.

No significa:

- que `neural_abr_lite` gane a baselines;
- ranking;
- benchmark final;
- mejora QoE;
- validación real-world;
- SOTA.

### 10.3 Cadena Phase 5

```text
Phase 5A0 -> literature delta and triage
Phase 5A1 -> source cards + integration evidence matrix
Phase 5A2 -> integration method decision
Phase 5B  -> integration contracts
Phase 5C  -> implementation specs
Phase 5D  -> implementation
Phase 5E  -> structural integration smoke
Phase 5F  -> fallback/error/telemetry hardening
Phase 5G  -> closure
```

### 10.4 Diseño final

Tipo:

```text
guarded neural scorer controller
```

Flujo:

```text
runtime feedback
-> online feature builder
-> bundle/schema validation
-> train-only normalization stats
-> action mask from current ladder
-> CPU inference
-> scores per representation
-> raw action
-> safety guard
-> fallback if needed
-> diagnostic telemetry
```

Carga segura:

```text
torch.load(..., map_location="cpu", weights_only=True)
```

Prohibido:

```text
weights_only=False en runtime
torch.hub
URLs
descarga automática
modelo dentro del repo
```

Fallback:

```text
fail closed
fallback clásico
emergency lowest representation si todo falla
fallback_reason estable
```

Telemetría:

```text
feedback_neural_* en segment_telemetry.csv
diagnostic-only
no benchmark
no neural fields en evaluation_segments.csv
```

### 10.5 Archivos principales creados

```text
core/controller/neural_abr_diagnostics.py
core/controller/neural_abr_lite.py
core/controller/neural_abr_loader.py
core/controller/neural_abr_runtime_features.py
core/controller/neural_abr_safety.py
```

Archivos modificados:

```text
core/controller/registry.py
player.py
config/client.example.yaml
docs/architecture/telemetry_column_provenance.md
```

Tests añadidos:

```text
tests/test_neural_abr_controller.py
tests/test_neural_abr_fake_smoke.py
tests/test_neural_abr_model_loading_runtime.py
tests/test_neural_abr_player_telemetry_hook.py
tests/test_neural_abr_registry.py
tests/test_neural_abr_runtime_features.py
tests/test_neural_abr_safety_fallback.py
tests/test_neural_abr_fault_injection.py
tests/test_neural_abr_hardening.py
tests/test_neural_abr_telemetry_hardening.py
```

### 10.6 Validación final esperada

Windows:

```text
HEAD -> 0c1018d
python -m unittest discover -> OK, 471 tests
python scripts/check_client_readiness.py --strict -> PASS, 78 OK / 0 WARN / 0 FAIL
```

Ubuntu:

```text
HEAD -> 0c1018d
python3 -m unittest discover -> OK, 471 tests
python3 scripts/check_client_readiness.py --strict -> PASS, 78 OK / 0 WARN / 0 FAIL
dev/gst environment checks -> PASS si se ejecutan
```

Smoke final:

```text
controller: neural_abr_lite
bundle: Phase 4F local-only bundle fuera del repo
media_engine: fake
run_manifest.json: OK
config.resolved.json: OK
environment.json: OK
run.log: OK
segment_telemetry.csv: OK
evaluation_segments.csv: OK
dataset.csv / dataset_training.csv: ausentes
feedback_neural_* presente en segment_telemetry.csv
evaluation_segments.csv sin campos neural
bundle_loaded = 1
fallback_used = 0
fallback_reason = success_neural
diagnostic_only = 1
```

---

## 11. Phase 6 — Evaluación formal pendiente

Phase 6 puede abrirse porque existen:

- cliente estable;
- baselines clásicos;
- pipeline trace-driven;
- QoE/reward/gates;
- modelo IA;
- controller IA integrado;
- smoke estructural;
- hardening de fallback/telemetry.

### 11.1 Objetivo

Comparar formalmente:

```text
controllers x traces x media_profile x seeds/config
```

Controllers mínimos:

```text
min_rate
fixed_rate
max_rate
rate_based
bba
bola
mpc
robust_mpc
neural_abr_lite
```

### 11.2 Reglas heredadas

- no usar red VM como benchmark principal;
- no usar smokes como benchmark;
- no mezclar train/validation/test/OOD;
- no usar trazas de entrenamiento IA para ventaja injusta;
- no dejar que controller vea `trace_id`, `dataset_id`, `split` u OOD label;
- no commitear datasets/artifacts;
- `qoe_linear_mean` es métrica primaria;
- `qoe_log_v1` sensibilidad;
- startup report-only;
- VMAF deferred.

### 11.3 Salidas esperadas de evaluación formal

Como mínimo:

- tabla por controller;
- tabla por dataset;
- tabla por split;
- media QoE;
- mediana QoE;
- desviación;
- percentiles;
- rebuffer medio;
- bitrate medio;
- switching medio;
- stall event count;
- fallos;
- número de sesiones `use_for_eval`;
- número de sesiones `diagnostic_only`;
- número de sesiones `do_not_use_for_eval`.

---

## 12. Política de repositorio y artefactos

El repo contiene:

```text
código
tests sintéticos
documentación
scripts
controllers
cliente
contratos de evaluación
specs
```

El repo no contiene:

```text
datasets reales
CSVs normalizados reales
manifests reales
outputs de runs
logs
zips
PDFs
media
modelos entrenados
checkpoints
TensorBoard logs
```

Rutas externas importantes mencionadas:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay
C:\Users\danie\Documents\TFG\_datasets\phase4_AI
C:\Users\danie\Documents\TFG\_runs\phase4_AI
C:\Users\danie\Documents\TFG\_models\phase4_AI\neural_abr_lite
```

---

## 13. Validaciones estándar

### 13.1 Windows

```powershell
git status --short --branch
git diff --check
python -m unittest discover
python scripts\check_client_readiness.py --strict
```

Compilación opcional de módulos:

```powershell
Get-ChildItem core\controller -Filter *.py | ForEach-Object { python -m py_compile $_.FullName }
```

### 13.2 Ubuntu

```bash
git pull --ff-only
git status --short --branch
python3 -m unittest discover
python3 scripts/check_client_readiness.py --strict
```

Checks de entorno:

```bash
python3 scripts/check_environment.py --profile dev
python3 scripts/check_environment.py --profile gst --strict
```

---

## 14. Cómo debe trabajar un chat futuro

Antes de responder, el chat debe identificar:

1. Qué fase está cerrada.
2. Qué fase se quiere abrir o reabrir.
3. Qué decisiones son históricas y cuáles siguen siendo válidas.
4. Si se está pidiendo ciencia, implementación, auditoría o comandos.
5. Si hace falta preparar prompt para Codex.
6. Qué no debe tocarse.
7. Qué validaciones hay que exigir.

### 14.1 Si se pide implementar

No dar código grande directamente salvo que el usuario lo pida expresamente. Lo normal es preparar:

```text
documento .md para Codex
objetivo
contexto
archivos permitidos
archivos prohibidos
pasos
tests esperados
validación Windows
commit
push
validación Ubuntu
reporte esperado
```

### 14.2 Si se pide auditar

Auditar con este orden:

1. estado de Git;
2. commits;
3. archivos creados/modificados;
4. tests;
5. readiness;
6. artefactos prohibidos;
7. coherencia metodológica;
8. si se puede avanzar o no.

### 14.3 Si se pide reabrir una fase

No asumir que el histórico debe mantenerse intacto a toda costa. Si Daniel decide reabrir por errores reales, tratar el documento como histórico y crear una nueva sección:

```text
Replanificación / revisión metodológica
Fecha
Motivo
Qué se invalida
Qué se conserva
Qué se rehace
Plan de corrección
Gates nuevos
```

---

## 15. Lista de “NO HACER”

Un chat futuro no debe:

- reabrir Phase 1 sin bug real;
- decir que Phase 1 implementó baselines;
- decir que Phase 2 demostró rendimiento final;
- convertir la red entre VMs en benchmark principal;
- usar Mahimahi/tc como benchmark equivalente al pipeline Python;
- usar dry-runs legacy como resultados finales;
- usar smoke scenarios como benchmark;
- entrenar IA antes de cerrar data/splits/gates;
- usar test/OOD para entrenar;
- permitir leakage por `trace_id`, `dataset_id`, `split` o futuro;
- cambiar `qoe_linear_v1` sin versión nueva;
- reentrenar IA sin nueva justificación;
- registrar o modificar controllers sin docs/tests;
- tocar player/runtime/media sin contrato;
- decir que IA gana antes de Phase 6;
- decir SOTA;
- decir real-world validation;
- meter `.pt`, `.pth`, `.onnx`, logs, CSVs, datasets, zips, PDFs o media en Git;
- usar `git add .`;
- pedir a Codex implementar desde PDFs brutos.

---

## 16. Lista de “SÍ HACER”

Un chat futuro sí puede:

- usar Phase 1 como base técnica cerrada;
- usar Phase 2 como base de baselines;
- usar Phase 3/3.5 como autoridad de trace-driven/QoE/gates;
- usar Phase 4 como histórico del modelo offline;
- usar Phase 5 como histórico de integración del controller IA;
- preparar Phase 6 formal con protocolo sólido;
- auditar rutas, manifests, splits y media profiles;
- crear prompts Codex desde documentos operativos;
- actualizar docs si se toma una nueva decisión documentada;
- exigir tests y readiness;
- mantener separación Windows/Ubuntu/servidor;
- tratar todo artifact generado como externo salvo que sea código/doc/test.

---

## 17. Prompt corto para abrir un chat nuevo

```text
Estoy continuando el TFG DashClientModular4. Usa el contexto maestro adjunto como histórico normalizado.

Estado consolidado del documento:
- Phase 1 cerrada: cliente DASH modular, reproducible y ABR-neutral.
- Phase 2 cerrada: baselines min/fixed/max, rate_based, bba, bola, mpc, robust_mpc.
- Phase 3/3.5 cerradas: pipeline Python trace-driven, qoe_linear_v1, reward_n, gates.
- Phase 4 cerrada: NeuralABR-Lite Candidate Scorer entrenado offline y exportado como bundle.
- Phase 5 cerrada: controller neural_abr_lite integrado con action mask, safety guard, fallback y telemetría diagnóstica.
- Phase 6 es la evaluación formal pendiente según el documento.

Reglas:
- No usar red real entre VMs como benchmark principal.
- No benchmark ni ranking con smokes.
- No mezclar train/validation/test/OOD.
- No usar información futura ni trace_id/dataset_id/split como feature.
- No commitear datasets, CSVs reales, logs, PDFs, media, modelos ni zips.
- No usar git add .
- Codex implementa solo desde specs y .md operativos.

Primero verifica qué fase queremos abrir o reabrir, qué se conserva del histórico y qué plan exacto conviene seguir.
```

---

## 18. Resumen final en una frase

DashClientModular4 llegó a Phase 5 con un cliente DASH modular y reproducible, baselines ABR clásicos, pipeline trace-driven, QoE/gates congelados, un modelo NeuralABR-Lite entrenado offline y un controller `neural_abr_lite` integrado con safety/fallback; la comparación formal contra baselines queda reservada para Phase 6 bajo protocolo reproducible, sin usar smokes ni red real entre VMs como benchmark principal.
