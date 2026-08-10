# Plan maestro de la memoria del TFG (la "biblia")

> Documento operativo único para escribir la memoria sin dudas. Define: título,
> resumen, reglas de estilo, reparto de herramientas, orden de redacción y —lo
> principal— **qué va exactamente en cada apartado**, con qué figura/tabla, de
> dónde sale el material en el repo, qué bibliografía lo apoya y qué es aportación
> propia frente a prestada. Convive con `00_INVENTARIO_BIBLIOGRAFIA.md` (qué fuente
> va en qué capítulo) y con `CLAUDE.md`/`AGENTS.md`/`HANDOFF_mpc_prudente_*`.

| Campo | Valor |
|---|---|
| Fecha | 2026-06-25 |
| Autor | Daniel Pretel |
| Centro | Universidad de Granada (UGR) — plantilla LaTeX oficial |
| Estado proyecto | Parte técnica TERMINADA. Esta fase = redacción de la memoria (Fase 7). |
| Estructura | Fijada por el profesor: Cap 1–7 + Bibliografía + Anexos (no se cambia el macro) |

---

## 0. Cómo usar este documento

1. Es el **índice expandido**. Cada apartado lleva: *Qué explicar*, *De dónde sale*,
   *Figuras/Tablas*, *Bibliografía*, *Aportación propia vs prestada*.
2. La columna "Bibliografía" usa **claves cortas** (p. ej. `Bentaleb19`, `Yin15`).
   La correspondencia clave → fichero está en `00_INVENTARIO_BIBLIOGRAFIA.md`.
3. Para escribir un apartado: lee este plan + las fuentes marcadas + el material del
   repo indicado. Borrador (Claude o NotebookLM) → tú lo masticas y reescribes.
4. Marca el estado de cada apartado al final (sección 9, checklist).

---

## 1. Título, resumen, keywords

**Título (opción A elegida; confirmar con tutor):**
> *Plataforma experimental modular para streaming adaptativo MPEG-DASH: cliente de
> reproducción y control ABR predictivo consciente del riesgo.*

**Subtítulo/línea alternativa para portada si piden algo más corto:**
> *Diseño, implementación y evaluación comparativa de controladores de bitrate
> adaptativo sobre un cliente DASH propio.*

**Resumen (ES):**
> Este trabajo desarrolla una plataforma experimental modular para streaming
> adaptativo MPEG-DASH. Se implementa un cliente de reproducción en Python que
> descarga y reproduce contenido segmentado, interpreta el MPD, registra telemetría
> y ejecuta distintos controladores de bitrate adaptativo (ABR) bajo una interfaz
> común, evaluándolos bajo condiciones de red reproducibles mediante trazas. Sobre
> esa base se implementan baselines clásicos de ABR fieles a la literatura y se
> diseña un controlador propio que combina un predictor temporal de throughput con
> estimación de incertidumbre y un planificador de control predictivo (MPC)
> consciente del riesgo. El proyecto incorpora un procedimiento reproducible de
> evaluación comparativa con métricas de calidad de experiencia (QoE), control de
> artefactos y separación estricta entre pruebas de humo y evaluación formal, junto
> con un análisis honesto de resultados y limitaciones.

**Abstract (EN):** (traducción fiel del anterior; redactar al cerrar el resumen ES).

**Palabras clave:** streaming adaptativo; MPEG-DASH; ABR; QoE; control predictivo
(MPC); predicción de throughput; incertidumbre; aprendizaje automático;
reproducibilidad.

**Keywords:** adaptive streaming; MPEG-DASH; ABR; QoE; model predictive control;
throughput prediction; uncertainty; machine learning; reproducibility.

---

## 2. Reglas de estilo (obligatorias)

Del profesor + anti-"olor a IA":

- Estilo **impersonal** ("se implementa", "se evalúa"), nunca primera persona.
- Frases **cortas**. Una idea por frase.
- Cada capítulo abre con 2–3 líneas: *qué se vio antes / qué se ve ahora*.
- Cada capítulo cierra con un **resumen** de lo visto.
- Toda figura: número + descripción debajo + **referenciada en el texto**. Sin
  figuras decorativas.
- Toda tabla: número + descripción + referenciada. Las tablas **resumen**, no vuelcan.
- Siglas: definir en la primera aparición (ABR, DASH, MPD, QoE, MPC, RL…).
- Cada métrica con **interpretación**, no solo el número.
- **Prohibido olor a IA:** nada de "En el vasto mundo de…", "Es importante destacar",
  "En resumen, podemos afirmar", emojis, ni adjetivos grandilocuentes. Sin afirmar
  mejoras no respaldadas por resultados.
- Terminología **consistente** entre capítulos (mismos nombres que en el código:
  `rate_based`, `bba`, `bola`, `mpc`, `robust_mpc`, controlador prudente v1/v2…).
- Separar nítido **diseño (cap 4) / implementación (cap 5) / evaluación (cap 6)**.
- **Nada de rastro de uso de IA para redactar.** El controlador IA del proyecto SÍ
  se describe (es la aportación); lo que no aparece es que la redacción se apoyó en IA.

---

## 3. Reparto de herramientas

| Herramienta | Rol | Qué le pides |
|---|---|---|
| **Claude** | Arquitecto + capítulos técnicos | Índice, mapa biblio, borradores cap 3/4/5/6/7, diagramas, tablas de resultados |
| **NotebookLM** | Experto en papers (cita fiel) | Cap 2 estado del arte y justificaciones biblio. Subes las fuentes del inventario por notebook temático |
| **Prism / LaTeX UGR** | Maqueta final | Pegar texto ya redactado → PDF con plantilla. No redactar de cero ahí |

**Notebooks de NotebookLM sugeridos** (≤50 fuentes c/u, según inventario):
1. `NB_estado_del_arte` — surveys + DASH/estándares + familias ABR + QoE.
2. `NB_cliente_dash` — estándares DASH/MPD, RFCs HTTP, docs de herramientas (cap 4/5).
3. `NB_ia_riesgo` — Pensieve, Puffer, BayesMPC, CausalSim, SafeSABR, SODA, Oboe,
   sim-to-real (cap 5 controlador propio + cap 2 familia IA).

**Prompt base para NotebookLM** (adaptar por capítulo): *"Usando exclusivamente los
PDF subidos, redacta en español, estilo impersonal y frases cortas, un borrador del
apartado X sobre [tema]. Organiza con subsecciones [ejes]. Define las siglas en su
primera aparición. Incluye citas a las fuentes y no inventes referencias que no estén
en los PDF. Termina conectando con [siguiente idea]."*

---

## 4. Orden de redacción recomendado

```
1º  Cap 4 Diseño  +  Cap 5 Implementación   (salen del repo, base sólida)
2º  Cap 6 Evaluación                          (resultados tfg_final ya existen)
3º  Cap 2 Estado del arte                      (NotebookLM + 62 papers)
4º  Cap 3 Planificación y costes               (del git log + fases reales)
5º  Cap 1 Introducción  +  Cap 7 Conclusiones  (cierran el relato al final)
6º  Bibliografía  +  Anexos                    (se llenan en paralelo)
```

---

## 5. Índice expandido — qué va EXACTAMENTE en cada apartado

Leyenda de cada apartado: **[Q]** qué explicar · **[R]** de dónde sale en el repo ·
**[F/T]** figuras/tablas · **[B]** bibliografía (claves del inventario) ·
**[P]** aportación propia vs prestada.

### Capítulo 1 — Introducción

**1.1 Motivación.**
- **[Q]** El vídeo domina el tráfico de Internet; el consumo es bajo demanda y por
  HTTP; la calidad percibida importa para el negocio y el usuario.
- **[B]** `Bentaleb19`, `TimmererReview`, `Alsader25`, `PeroniGorinsky25` (cifras de
  tráfico y contexto). Citar dato de tráfico de vídeo de un survey reciente, no de blog.
- **[P]** Prestada (contexto). Propia: el encuadre del problema concreto.

**1.2 Problema técnico.**
- **[Q]** La red varía en el tiempo; el cliente debe elegir bitrate segmento a
  segmento; trade-off calidad ↔ rebuffer ↔ estabilidad; por qué es difícil (futuro
  de red desconocido, medio VBR).
- **[B]** `Yin15`, `Seufert15`, `Bentaleb19`.
- **[P]** Propia: formulación del problema tal como lo aborda el proyecto.

**1.3 Por qué un cliente DASH propio (no caja negra).**
- **[Q]** Justificación de construir un entorno experimental válido y no contaminante,
  con telemetría controlada y trazas reproducibles, frente a usar un reproductor
  comercial cerrado. (Este es el punto que te preocupaba: aquí va.)
- **[R]** `core/` (cliente), `core/phase6/` (evaluación), contratos de telemetría.
- **[B]** `Puffer20`/`Hoffman25`/`CausalSim23` (la validez del entorno y el sesgo de
  simulación justifican por qué un entorno fiel importa).
- **[P]** **Propia (fuerte).** Es tu decisión de ingeniería.

**1.4 Objetivos.** Lista numerada, medibles. Propuesta:
1. Implementar un cliente/reproductor DASH modular en Python (MPD, descarga, buffer,
   reproducción, telemetría).
2. Definir una API común de controladores ABR e integrar baselines clásicos fieles a
   la literatura.
3. Diseñar e integrar un controlador propio con predicción de throughput,
   incertidumbre y planificación MPC consciente del riesgo.
4. Construir un procedimiento de evaluación reproducible con métricas QoE y trazas
   de red controladas.
5. Comparar controladores de forma honesta (mismas condiciones, sin claims sin gates).
- **[P]** Propia. **Las conclusiones (cap 7) responden una a una a estos objetivos.**

**1.5 Estructura del documento.** Una frase por capítulo.

> Resumen del capítulo.

### Capítulo 2 — Precedentes, antecedentes y estado del arte

> Apertura: en el cap 1 se planteó el problema; aquí se revisa el contexto técnico y
> científico.

**2.1 Streaming adaptativo HTTP (HAS).** Concepto, evolución, por qué HTTP/CDN.
- **[B]** `Seufert15`, `Bentaleb19`, `TimmererReview`, `Stockhammer11`.

**2.2 MPEG-DASH, MPD y segmentación.** Estándar, MPD (Period/AdaptationSet/
Representation/Segment), inicialización, perfiles, segmentación temporal, VBR vs CBR.
- **[B]** `ISO23009`, `Stockhammer11`, `Timmerer12`, `DASH_IF_IOP`. RFCs HTTP como apoyo.
- **[P]** Propia: explicación didáctica para lector no-DASH (el profesor lo pide).

**2.3 El problema ABR.** Variables observables (buffer, throughput pasado, tamaños),
decisión, objetivo QoE; horizonte; incertidumbre del futuro.
- **[B]** `Yin15`, `Bentaleb19`.

**2.4 Familias de algoritmos ABR (núcleo del capítulo).** Comparar qué aporta y qué
limita cada familia:
- *Rate-based* (throughput): `Liu11`.
- *Buffer-based*: `Huang14` (BBA), `Spiteri20`/`Spiteri19` (BOLA).
- *Control / MPC*: `Yin15` (MPC y RobustMPC).
- *Híbridos / auto-tuning*: `Oboe`.
- *Aprendizaje por refuerzo (RL)*: `Pensieve17`, `Comyco`, `Real-worldRL`,
  `Gelato`, `Plume`.
- *Generalización / meta / offline RL*: `MERINA`, `Fortuna`, `MetaABR`, `A2BR`,
  `BentalebMetaRL`, `ANT`, `BETA`, `NMoEABR`.
- *Riesgo / incertidumbre / consistencia*: `BayesMPC`, `SafeSABR`, `SODA`.
- **[F/T]** **Tabla comparativa de familias** (familia · idea · señal que usa · pros ·
  contras · ejemplo). Es la tabla estrella del capítulo.
- **[P]** Propia: la síntesis crítica y la tabla. Prestada: cada método.

**2.5 QoE: modelos y métricas.** Qué es QoE; modelos lineales vs logarítmicos;
componentes (bitrate, rebuffer, smoothness, startup); por qué se eligió QoE lineal.
- **[B]** `Seufert15`, `QoEModeling19`, `DuanmuQoE`, `PeroniQoE24`, `UnderstandingQoE`,
  `Zuo22`.
- **[P]** Propia: justificación de la métrica congelada del proyecto (enlaza con cap 6).

**2.6 Reproductores DASH existentes.** dash.js, Shaka, GPAC; qué hacen y por qué no
sirven como banco experimental controlado.
- **[B]** docs `dashjs`, `Shaka`, `GPAC` (carpeta cliente).
- **[P]** Propia: la comparación y la justificación del cliente propio.

**2.7 Surveys y síntesis crítica.** Lagunas y desacuerdos que justifican el enfoque
(fidelidad al medio + riesgo): sesgo de simulación, generalización, despliegue real.
- **[B]** `Puffer20`, `Hoffman25`, `CausalSim23`, `Veritas23`, `Alsader25`,
  `PeroniGorinsky25`.
- **[P]** Propia: el hilo argumental que lleva a tu controlador.

> Resumen del capítulo.

### Capítulo 3 — Planificación y estimación de costes

> Apertura: con el contexto fijado, se describe cómo se organizó el trabajo.

**3.1 Metodología por fases.** Fases reales del proyecto (Phase 1–7) y el contrato
operativo (desarrollo Windows / entrenamiento WSL / validación Ubuntu cliente).
- **[R]** `git log`, `AGENTS.md`, `CLAUDE.md`, docs de fases.

**3.2 Paquetes de trabajo y tareas.** Descomponer en WP: cliente, parser MPD,
baselines, dataset/red, controlador IA, evaluación Phase 6, memoria. Cada bloque →
tareas y subtareas (el profesor quiere granularidad).
- **[F/T]** Tabla WP → tareas → entregable.

**3.3 Diagrama de Gantt y desviaciones.** Cronograma planificado vs real. Marcar
hitos (cierre cliente, cierre baselines, líneas IA abandonadas, resultado final).
- **[F/T]** **Figura: Gantt.** (Extraer fechas del `git log`; te genero datos.)
- **[P]** Propia. Incluir las **adaptaciones** (líneas SPBC/Q_H abandonadas) como
  replanificación honesta.

**3.4 Estimación de horas.** Por WP. Tabla horas × tipo de tarea (biblio, desarrollo,
validación, redacción).

**3.5 Costes.** Humano (horas × €/h de ingeniero junior), hardware (PC, GPU AMD RX
7800 XT, VMs Ubuntu, servidor), software (todo open-source/gratuito → coste 0,
destacarlo). Coste por fases o mensual.
- **[F/T]** Tabla de costes desglosada.
- **[P]** Propia.

> Resumen del capítulo.

### Capítulo 4 — Diseño

> Apertura: qué se va a construir, a nivel arquitectura, antes de programarlo.

**4.1 Visión global y módulos.** Esquema de bloques y flujo extremo a extremo
(MPD → descarga → buffer → reproducción → decisión ABR → telemetría → evaluación).
- **[F/T]** **Figura: arquitectura de módulos.** **Figura: flujo de una sesión.**
- **[R]** `core/` (estructura de paquetes).
- **[P]** **Propia (núcleo del TFG como proyecto software).**

**4.2 Parser MPD.** Qué extrae (representations, bitrates, segmentos, plantillas URL,
init), separación parser ↔ resto.
- **[B]** `ISO23009`, doc `ElementTree`.

**4.3 Motor de descarga y buffer.** Modelo de descarga, ocupación de buffer, límites
(buffer máx. 60 s), relación con trace replay.
- **[B]** RFCs HTTP (`RFC9110/9112`), doc `Requests`.

**4.4 Motor de reproducción.** Consumo de buffer, rebuffering, eventos, telemetría de
reproducción.

**4.5 API común de controladores.** El contrato (qué ve y qué no ve un controlador:
nunca `trace_id`/`split`/futuro). Entradas/salidas, máscara de acciones, fallback.
- **[F/T]** **Figura/Tabla: interfaz del controlador** (firma + estado observable).
- **[R]** registro de controladores, `core/controller/`.
- **[P]** **Propia (clave para "acepta distintos controllers").**

**4.6 Telemetría y logging.** Qué se registra por segmento/sesión, contratos de
métricas, separación logging ↔ evaluación.

**4.7 Red (trace replay) vs medio (media profile VBR).** **Distinción crítica**: la
red se emula con trazas externas curadas; el medio es el MPD real (6 niveles, 151
segmentos 4 s, VBR). No confundir.
- **[R]** manifest curado phase3, `media_profiles/segment_sizes/*.json`.
- **[B]** `Riiser13`, `Raca18`, `Raca20`, `Lumos5G20`, `Mahimahi15`, `CellReplay`,
  `Wei19` (procedencia y semántica de trazas/emulación).
- **[P]** **Propia (fidelidad al medio = aportación metodológica).**

**4.8 Separación cliente / controllers / métricas / benchmark.** Por qué smokes ≠
benchmark; gates (`use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`).
- **[P]** Propia.

> Resumen del capítulo.

### Capítulo 5 — Implementación

> Apertura: cómo se materializa en código el diseño del cap 4.

**5.1 Lenguaje, frameworks y librerías.** Python (por qué), ElementTree, Requests,
PyYAML, PyTorch (controlador IA), ONNX (si aplica). Justificar cada elección.
- **[B]** docs `ElementTree`, `Requests`, `PyYAML`, `PyTorch`, `ONNX`,
  `MLModelSecurity` (seguridad al cargar modelos).

**5.2 Cliente y player.** Implementación de descarga/buffer/reproducción; decisiones
relevantes (no transcribir código; solo fragmentos que expliquen una decisión).
- **[R]** `core/` player y motor.

**5.3 Parser MPD.** Detalles de implementación, casos del MPD real (Paseo/Blender).

**5.4 Runner y configuración.** Cómo se lanza una sesión/evaluación, config por JSON,
inyección del media por sesión (multi-vídeo).
- **[R]** `scripts/run_phase6_*`, `config/phase6.local.json`, `core/phase6/`.

**5.5 Baselines clásicos.** Implementación fiel de `rate_based`, `bba`, `bola`, `mpc`,
`robust_mpc`; mapping fórmula-paper → código.
- **[R]** `docs/contexto rama original/01_baselines/<x>/{paper_card,source_evidence,
  notes_for_memory,implementation_spec}.md` — **YA ESCRITO, reutilizar tal cual.**
- **[B]** `Liu11`, `Huang14`, `Spiteri20`, `Yin15` (RobustMPC).
- **[P]** Propia: la implementación y la verificación de fidelidad. Prestada: algoritmos.

**5.6 Controlador propio (IA) — el plato fuerte.** Predictor de cuantiles de
throughput (MLP v1; ensemble temporal GRU v2 con incertidumbre epistémica) + planner
MPC prudente (coste CVaR) con tamaños VBR reales. Paradigma predictor+control.
- **[R]** `core/mpc_prudente/*` (media_profile, dataset, training, temporal_model,
  temporal_training, planner, bundle, temporal_bundle, evaluation),
  `core/controller/mpc_prudente_runtime.py`. Mapa en `HANDOFF_mpc_prudente_*`.
- **[B]** `BayesMPC`, `Puffer20`, `Pensieve17`, `SafeSABR`, `SODA`, `Oboe`,
  `CausalSim23`, `Hoffman25`.
- **[F/T]** **Figura: arquitectura predictor+planner.** **Figura: bucle de decisión.**
- **[P]** **Propia (máxima).** Idea, diseño, integración.

**5.7 Entorno de entrenamiento fiel al medio (VBR).** Por qué el viejo enfoque CBR
fallaba; cómo el dataset y el planner usan tamaños reales por segmento.
- **[R]** `core/mpc_prudente/media_profile.py`, `dataset.py`; decisiones
  `decision_mpc_prudente_*`.
- **[P]** Propia.

> Resumen del capítulo.

### Capítulo 6 — Evaluación

> Apertura: con el sistema implementado, se evalúa de forma reproducible y honesta.

**6.1 Qué y cómo se evalúa (protocolo Phase 6).** Comparativa formal, gates, splits
por `leakage_group` (eval reservado), deltas pareados, CI95, sign-test.
- **[R]** `core/phase6/analysis.py`, `catalog.py` (preset `tfg_final`).
- **[P]** **Propia (rigor metodológico = aportación principal).**

**6.2 Entorno experimental.** Las 4 máquinas (Windows dev, WSL2 ROCm entrenamiento,
Ubuntu cliente validación, Ubuntu servidor HTTP). Hardware (CPU, GPU AMD RX 7800 XT,
ROCm 7.2.1, torch 2.9.1) y software.
- **[F/T]** **Figura: topología de entornos.** **Tabla: hardware/software.**

**6.3 Vídeos y trazas.** Lista de vídeos (Paseo_Almuñécar 10min 30fps 4s + Blender,
30/60fps; 4 vídeos en `tfg_final`); perfil VBR (6 niveles 300–4300 kbps, 151 seg).
Corpus de trazas curado (6768 trazas; FCC/Norway/Oboe/Lumos5G/Puffer + sintéticas;
eval ≈1025).
- **[F/T]** **Tabla: niveles de calidad.** **Tabla: vídeos.** **Tabla: corpus trazas.**
- **[B]** `Riiser13`, `Raca18`, `Raca20`, `Lumos5G20`, `Puffer20`.

**6.4 Controladores comparados.** Los 6: `rate_based`, `bba`, `bola`, `mpc`/
`robust_mpc`, prudente v1, prudente v2.

**6.5 Métricas.** QoE lineal (`reward_n = bitrate_mbps − 4.3·rebuffer_s −
smoothness_mbps`), rebuffer medio, stalls/sesión, sesiones >5s/>10s, cola (P5,
peor-caso), inferencia ms, fallback. QoE log como secundaria; startup report-only.
- **[F/T]** **Tabla: definición de métricas.**

**6.6 Resultados.** Paquete `20260624_182747_tfg_final` (360 sesiones, 6 controllers,
4 vídeos, gates OK, 0 fallback). Tabla principal de QoE/rebuffer/stalls + estadística
pareada vs `robust_mpc`. Ablación v1 vs v2.
- **[F/T]** **Tabla principal de resultados.** **Figura: QoE por controlador.**
  **Figura: robustez peor-caso / stalls** (plots `qoe_robustez_peor_caso`,
  `stalls_por_controller`). **Tabla: ablación v1↔v2.**
- **[R]** `~/TFG/runs_trazas/phase6/20260624_182747_tfg_final` (artefacto externo).

**6.7 Interpretación y limitaciones.** Lectura honesta: v2 = QoE media más alta,
**empate estadístico** con `robust_mpc` (sign_p=0.54), pero **menos rebuffering**;
v2 > v1 (valida ensemble temporal). Limitaciones: muestra, cola extrema en Blender
60fps, objetivo interno de MPC vs métrica de eval, simulación.
- **[P]** **Propia.** Honestidad explícita (no "gano a todos").

> Resumen del capítulo.

### Capítulo 7 — Conclusiones y trabajo futuro

> Apertura: se recapitula frente a los objetivos del cap 1. Sin resultados nuevos.

**7.1 Hitos vs objetivos.** Responder objetivo a objetivo (1.4): cliente DASH modular,
parser MPD, API de controllers, baselines fieles, controlador IA, evaluación
reproducible.
**7.2 Resultados principales.** Resumen del cap 6 (sin números nuevos).
**7.3 Limitaciones honestas.** Muestra, fidelidad simulación, alcance de vídeos/red.
**7.4 Trabajo futuro.** Conectado a limitaciones: afinar cola extrema, alinear objetivo
de planner con QoE de eval, más vídeos/redes, validación en despliegue real.
**7.5 Resultados negativos como aportación.** SPBC/SPC (colapso offline↔cliente),
Q_H scorer (target no aprendible), "más datos no mejora" (Neural-MPC v1 vs v2).
- **[R]** `decision_*` y `plan_maestro_controller_ia_claude_*`.
- **[P]** **Propia.** Madurez científica.

> Resumen del capítulo.

### Bibliografía
- Gestor: BibTeX (plantilla UGR). Una entrada por fuente del inventario **realmente
  citada**. No citar lo no usado.
- Distinguir aportación propia vs previa por las citas.

### Anexos
- A. Configuración completa (config Phase 6, registro de controladores).
- B. Comandos de validación y reproducción (scripts `run_*`, `check_client_readiness`).
- C. Detalle de entorno (versiones, hardware, ROCm).
- D. Tablas largas (corpus de trazas, tamaños VBR por segmento).
- E. Fragmentos de implementación extensos (si no caben en cap 5).

---

## 6. Mapa global de figuras (objetivo, no decorativas)

| # | Figura | Capítulo | Origen |
|---|---|---|---|
| F1 | Arquitectura de módulos del cliente | 4.1 | diagrama propio |
| F2 | Flujo de una sesión (secuencia) | 4.1 | diagrama propio |
| F3 | Interfaz del controlador ABR | 4.5 | diagrama propio |
| F4 | Red (trazas) vs medio (VBR) | 4.7 | diagrama propio |
| F5 | Arquitectura predictor + planner MPC prudente | 5.6 | diagrama propio |
| F6 | Bucle de decisión del controlador | 5.6 | diagrama propio |
| F7 | Topología de los 4 entornos | 6.2 | diagrama propio |
| F8 | QoE media por controlador | 6.6 | plot Phase 6 |
| F9 | Robustez peor-caso / stalls | 6.6 | plots Phase 6 |
| F10 | Diagrama de Gantt | 3.3 | git log |

(Las figuras propias las puedo generar en SVG/diagrama cuando lleguemos a cada cap.)

## 7. Mapa global de tablas

| # | Tabla | Capítulo |
|---|---|---|
| T1 | Comparativa de familias ABR | 2.4 |
| T2 | WP → tareas → entregables | 3.2 |
| T3 | Horas por WP | 3.4 |
| T4 | Costes (humano/hardware/software) | 3.5 |
| T5 | Niveles de calidad del vídeo (VBR) | 6.3 |
| T6 | Vídeos usados | 6.3 |
| T7 | Corpus de trazas | 6.3 / Anexo D |
| T8 | Definición de métricas | 6.5 |
| T9 | Resultados principales (tfg_final) | 6.6 |
| T10 | Ablación v1 ↔ v2 | 6.6 |
| T11 | Hardware/software del entorno | 6.2 |

---

## 8. Material del repo ya reutilizable (no reinventar)

- **Baselines:** `docs/contexto rama original/01_baselines/<x>/notes_for_memory.md`,
  `paper_card.md`, `source_evidence.md`, `implementation_spec.md` (5 controladores).
- **Resultado final + tesis honesta:** `HANDOFF_mpc_prudente_estado_completo_20260624.md`,
  `resultado_final_mpc_prudente_phase6_20260624.md`.
- **Decisiones de la línea IA:** `decision_mpc_prudente_*.md`, `plan_maestro_controller_ia_*`.
- **Causa raíz CBR→VBR:** `vbr-media-fidelity-gap` (memoria) + plan maestro §2.
- **Métricas/papers de evaluación:** `catalogo_metricas_evaluacion_abr_papers_20260619.md`.
- **62 papers en Markdown:** `docs/todos los estudios pdf convertidos a md/` (lectura barata).

---

## 9. Checklist de estado (actualizar al avanzar)

| Apartado | Estado | Nota |
|---|---|---|
| Título / resumen / keywords | BORRADOR | confirmar título con tutor |
| Cap 1 Introducción | TODO | |
| Cap 2 Estado del arte | TODO | NotebookLM |
| Cap 3 Planificación/costes | TODO | sacar Gantt del git log |
| Cap 4 Diseño | TODO | empezar por aquí |
| Cap 5 Implementación | TODO | reutilizar notes_for_memory baselines |
| Cap 6 Evaluación | TODO | datos tfg_final listos |
| Cap 7 Conclusiones | TODO | al final |
| Bibliografía (BibTeX) | TODO | solo lo citado |
| Anexos | TODO | |
