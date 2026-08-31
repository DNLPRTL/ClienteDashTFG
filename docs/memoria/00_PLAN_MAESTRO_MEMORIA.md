# Plan maestro de la memoria del TFG (la "biblia")

> Documento operativo único para escribir la memoria sin dudas. Define: título,
> resumen, reglas de estilo, reparto de herramientas, orden de redacción y —lo
> principal— **qué va exactamente en cada apartado**, con qué figura/tabla, de
> dónde sale el material en el repo, qué bibliografía lo apoya y qué es aportación
> propia frente a prestada. Convive con `00_INVENTARIO_BIBLIOGRAFIA.md` (qué fuente
> va en qué capítulo) y con `CLAUDE.md`/`AGENTS.md`/`HANDOFF_mpc_prudente_*`.

| Campo | Valor |
|---|---|
| Fecha | 2026-06-25 (actualizado 2026-08-12) |
| Autor | Daniel Pretel |
| Centro | Universidad de Granada (UGR) — plantilla LaTeX oficial |
| Estado proyecto | Parte técnica TERMINADA. Esta fase = redacción de la memoria (Fase 7). |
| Estructura | Fijada por el profesor: Cap 1–7 + Bibliografía + Anexos (no se cambia el macro) |

> **ACTUALIZACIÓN 2026-08-12 (vigente):** (1) De cara a la memoria SOLO existe
> `C:\Users\danie\Documents\TFG Material\` (regla cero; el repo es bruto para
> contexto/planes/bibliografía). (2) La nomenclatura de este plan es la vieja de
> junio: se traduce SIEMPRE con `04_CORRESPONDENCIAS_NOMENCLATURA.md`. (3) Los
> números de resultados citados en este plan eran de junio: los CANÓNICOS son los
> del paquete `20260810_133520_tfg_final` (300 sesiones, **5 controladores**, sin
> v1) — el cap 6 de abajo ya está reescrito con ellos. (4) Citas: SOLO claves de
> `bibliografia.bib` (ver `02_BIBLIOGRAFIA_DEFINITIVA.md`); las claves [B] de este
> plan son etiquetas provisionales de junio, mapear a las del .bib. (5) Tutor:
> Juan José Ramos Muñoz (portada `\myProf`); plantilla en Prism con `unsrt`.

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
- **Norma de fuentes (12/08):** toda afirmación con cita se verifica contra el
  **PDF original** (`literatura\biblioteca_final\<carpeta>\<claveBib>.pdf`) antes
  de entrar en la memoria. Los `.md` convertidos del repo son solo índice de
  búsqueda, nunca fuente final.

---

## 3. Reparto de herramientas

| Herramienta | Rol | Qué le pides |
|---|---|---|
| **Claude** | Arquitecto + capítulos técnicos | Índice, mapa biblio, borradores cap 3/4/5/6/7, diagramas, tablas de resultados |
| **NotebookLM** | Experto en papers (cita fiel) | Cap 2 estado del arte y justificaciones biblio. Subes las fuentes del inventario por notebook temático |
| **Prism / LaTeX UGR** | Maqueta final | Pegar texto ya redactado → PDF con plantilla. No redactar de cero ahí |

**Notebooks de NotebookLM** (fuentes desde `literatura\biblioteca_final\`;
NotebookLM solo interviene en el cap 2 + estudio para la defensa):
1. `NB_estado_del_arte` (37): carpetas `01_surveys_qoe` + `02_trabajos_locales_ugr`
   + `04_abr_clasicos` + `05_abr_ia` + `06_riesgo_simtoreal` ENTERAS +
   `03/stockhammer2011dash.pdf` + de `09`: kan2022merina, huang2022a2br,
   yin2024ant, wang2026nmoeabr.
2. `NB_cliente_dash` (18 + webs): carpetas `03_dash_estandares_http` +
   `07_datasets_emulacion` ENTERAS + `04/spiteri2019dashjs.pdf`; las docs de
   herramientas de `08` se añaden como fuente "sitio web" (URL oficial), no como
   fichero (NotebookLM no admite .html locales).
3. `NB_ia_riesgo` (16): carpetas `05_abr_ia` + `06_riesgo_simtoreal` ENTERAS +
   `04/yin2015mpc.pdf` + `04/akhtar2018oboe.pdf` +
   `07/wei2019traceBasedEmulation.pdf` + `08/digregorio2026mlLoading.pdf`.

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
**Incluye la implementación de la reproducción de trazas** (`core/reproduccion_trazas/`:
cargador+validación del CSV, modelo de red, descargador controlado) — el diseño se
contó en 4.7; aquí el cómo.
- **[R]** `core/` reproductor, motores y reproduccion_trazas.
- NOTA de reparto (fijado 25/08): la NORMALIZACIÓN del corpus (12 datasets brutos →
  esquema común, catálogo, splits) NO va al cap 5 (su código no está en el
  entregable): se cuenta en 6.3 como preparación de datos + cap 3 como paquete de
  trabajo. El MUESTREO de ventanas para el dataset del modelo
  (`entrenamiento/corpus_trazas/`) va en 5.7.

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

**6.4 Controladores comparados.** Los **5 del experimento canónico**:
`basado_en_tasa`, `bba`, `bola`, `mpc_robusto`, `controlador_propio`. Nota de una
frase: el proyecto implementa también el MPC básico (`mpc`, FastMPC), pero la
comparativa evalúa su variante robusta por ser la referencia fuerte de la
literatura (Yin 2015). La antigua "ablación v1↔v2" NO va aquí: la variante MLP
del predictor quedó fuera del sistema final y se cuenta en 7.5 como iteración.

**6.5 Métricas.** QoE lineal (`reward_n = bitrate_mbps − 4.3·rebuffer_s −
smoothness_mbps`; columna `qoe_lineal_media`), rebuffer medio, stalls/sesión,
sesiones >5s/>10s, cola (P5, mínimo, peor 5%), latencia de decisión, auditoría de
inferencia (0 respaldos). QoE log secundaria; sintéticas reportadas aparte.
- **[F/T]** **Tabla: definición de métricas.**

**6.6 Resultados.** Paquete **`20260810_133520_tfg_final`** (300 sesiones = 240
reales + 60 sintéticas diagnósticas; 48 escenarios reales pareados × 5
controladores; 4 vídeos; gates 8/8; 0 respaldos; 1740/1740 inferencias auditadas;
inferencia neural media 1.26 ms; latencia de decisión media 174 ms).
Números canónicos (reales):
- QoE media: propio **2.0097** > basado_en_tasa 1.9701 > mpc_robusto 1.9471 >
  bba 1.7874 > bola 1.2439. Conclusión del paquete: "sin ganador
  estadísticamente concluyente" (empate en cabeza).
- Pareado vs mpc_robusto (n=48): propio Δ=+0.063, IC95 [−0.043,+0.209],
  sign_p=0.152 (empate); basado_en_tasa Δ=+0.023 pero **pierde 36/48 ventanas**
  (sign_p=7.2e-4); bba Δ=−0.160 (sign_p=3.3e-6); bola Δ=−0.703, IC excluye 0
  (sign_p=1.4e-8).
- Propio vs mpc_robusto por ventanas: **W8/L16/T24** — 24 empates exactos
  (ventanas fáciles, decisiones idénticas); la ventaja del propio es AGREGADA
  (evita catástrofes), NUNCA redactar "gana en la mayoría de escenarios".
- Claims positivos con significancia: propio > basado_en_tasa (W37/L11,
  sign_p=2.2e-4), > bba (W40/L8, IC [−0.331,−0.114] excluye 0, sign_p=3.3e-6),
  > bola (W42/L6, sign_p=1.0e-7).
- Rebuffering: propio 3.04 s vs robusto 3.85 s; stalls/sesión 0.33 vs 0.46;
  sesiones con stall 33% ambos; **sesiones >5 s: 12.5% vs 25%**; >10 s: 10.4% vs
  12.5%. rate_based el más conservador (1.49 s, 0.19 stalls) a costa de bitrate
  (2350 vs 2636 kbps del propio).
- Cola QoE: propio P5=−3.38/min=−3.90; robusto P5=−3.13/min=−3.22; peor delta del
  propio vs robusto −0.699 (ventana real_012, paseo 30fps). bba/bola colas peores
  (min −4.57/−4.89). Mediana: propio 2.89 (la más alta).
- **[F/T]** **T9: tabla principal** (QoE/bitrate/rebuffer/stalls/colas por
  controlador, de `agregados_por_controlador.json`). **T10: deltas pareados vs
  mpc_robusto** (Δ, IC95, sign test, W/L/T, de `estadistica.json` + cómputo
  propio verificado). **F8/F9: gráficas reales del paquete** (16 disponibles en
  `03_graficas/`: cdf_qoe_lineal, componentes_qoe, calidad_vs_rebuffering,
  qoe_robustez_peor_caso, stalls_por_controlador, cdf_rebuffering, cdf_bitrate,
  cdf_buffer, cdf_smoothness, cdf_qoe_log, qoe_por_dificultad_red,
  qoe_por_dataset, qoe_por_condicion_red, caso_temporal_bitrate_qoe,
  latencia_decision, sinteticas_diagnostico).
- **[R]** `TFG Material\04_evidencia_final\20260810_133520_tfg_final` (única
  fuente de números; junio y 06/08 solo como nota de consistencia si hace falta:
  propio 1º en media en las tres ejecuciones, robusto ~1.95 estable).

**6.7 Interpretación y limitaciones.** Lectura honesta: el controlador propio
obtiene la QoE media y mediana más altas y **empata estadísticamente** con
mpc_robusto (IC95 cruza 0, sign_p=0.152), **reduciendo el rebuffering** (menos
stalls/sesión y la mitad de sesiones >5 s); gana con significancia a los otros
tres baselines. La ventaja frente a mpc_robusto es agregada (evita catástrofes),
no por ventanas (W8/L16/T24). Limitaciones: 48 escenarios reales (n moderado),
2 ventanas comparten `leakage_group` (ghent bus), cola extrema residual del
propio (P5 −3.38, peor ventana real_012), los MPC clásicos optimizan
internamente un objetivo log distinto de la QoE lineal de evaluación (decisión
documentada que juega EN CONTRA del propio), y evaluación en emulación por
trazas (sim-to-real acotado por diseño, no eliminado).
- **[P]** **Propia.** Honestidad explícita (no "gano a todos"). Redactar los
  matices EXACTAMENTE como manda `decision_revision_final_tecnica_20260805.md`:
  citar el CI, no solo medias; empates exactos explican el n efectivo del sign
  test; nada de claims fuera de los autorizados.

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
**7.5 Resultados negativos como aportación.** Cuatro iteraciones descartadas,
contadas con descripciones funcionales (sin claves internas, ver 04_CORRESPONDENCIAS §5):
(1) políticas de clonación de comportamiento (colapso offline↔cliente);
(2) función de puntuación con horizonte (objetivo no aprendible desde el estado
observable); (3) "más datos no mejora" sin fidelidad al medio (el predecesor
entrenado con más datos empeoró); (4) **variante MLP del predictor, eliminada
del sistema final**: en la iteración de junio el ensemble temporal la superó de
forma consistente en QoE, cola y rebuffering → se cuenta CUALITATIVAMENTE como
decisión de diseño (regla: números de junio NO van a la memoria; si el tribunal
pide cifras, están en el histórico).
- **[R]** `why_not_*.md` de `docs/contexto rama original/04_neural_abr/`,
  `decision_*` y `plan_maestro_controller_ia_claude_*` (solo como contexto).
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
| F8 | QoE por controlador (CDF y/o media) | 6.6 | plots reales del paquete canónico `03_graficas/` |
| F9 | Robustez peor-caso / stalls | 6.6 | `qoe_robustez_peor_caso.png` + `stalls_por_controlador.png` del paquete canónico |
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
| T9 | Resultados principales (paquete canónico 20260810) | 6.6 |
| T10 | Deltas pareados vs mpc_robusto (Δ, IC95, sign test, W/L/T) | 6.6 |
| T11 | Hardware/software del entorno | 6.2 |

---

## 8. Material del repo ya reutilizable (no reinventar)

- **FUENTE DE VERDAD del sistema descrito:** `C:\Users\danie\Documents\TFG Material\`
  (código `01_codigo\ClienteDashTFG`, corpus `02_corpus_red\catalogo_trazas.json`,
  bundle `03_modelos`, **evidencia canónica `04_evidencia_final\20260810_133520_tfg_final`**,
  contenido `05_contenido_dash`, dataset `06_dataset_entrenamiento`, informes
  `00_info_entorno`). Traducción de nombres: `04_CORRESPONDENCIAS_NOMENCLATURA.md`.
- **Cómo redactar resultados:** `decision_revision_final_tecnica_20260805.md`
  (citar CI, no solo medias; matices win/loss; empates exactos).
- **Componentes/versiones del experimento:** `docs/defensa/componentes_experimento.md`
  (topología, versiones exactas, generación DASH; conteos de sesiones = canónico).
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
| Título / resumen / keywords | BORRADOR | título A elegido; confirmar con tutor |
| Cap 1 Introducción | TODO | |
| Cap 2 Estado del arte | TODO | NotebookLM (listas de fuentes fijadas 12/08) |
| Cap 3 Planificación/costes | TODO | sacar Gantt del git log |
| Cap 4 Diseño | BORRADORES COMPLETOS | 4.1–4.7 redactados por Daniel; 4.8 BORRADOR entregado 27/08 (cap4_8_separacion_evaluacion.md + T4.7 gates + resumen del capítulo). Al masticar 4.8: pasada de coherencia del capítulo entero. Siguiente capítulo: 5 |
| Cap 5 Implementación | EN CURSO | 5.1 BORRADOR entregado 31/08 (cap5_1_lenguaje_librerias.md + T5.1 componentes; digregorio verificado contra PDF). Siguiente: 5.2 cliente+replay. Para 5.5: reutilizar notes_for_memory baselines |
| Cap 6 Evaluación | TODO | números canónicos fijados en §5 (paquete 20260810) |
| Cap 7 Conclusiones | TODO | al final |
| Bibliografía (BibTeX) | HECHA (92 entradas) | `bibliografia.bib` cerrado 10/08; solo se imprime lo citado |
| Anexos | TODO | |
| Tabla de correspondencias | HECHA 12/08 | `04_CORRESPONDENCIAS_NOMENCLATURA.md` |
