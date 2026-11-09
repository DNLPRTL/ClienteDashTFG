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
| Estado proyecto | FASE DE BLINDAJE (desde el 14/10/2026 por la noche): redacción pausada hasta cerrar la parte técnica |
| Estructura | Fijada por el profesor: Cap 1–7 + Bibliografía + Anexos (no se cambia el macro) |

> **ACTUALIZACIÓN 2026-10-14, noche (VIGENTE; manda sobre todo lo de abajo):**
> 1. Daniel detuvo el experimento final del 14/10. Se abre la fase de blindaje
>    (`docs/blindaje/00_HANDOFF_FASE_BLINDAJE.md`): mejoras, prueba previa sobre
>    validación y UN experimento final nuevo, con protocolo propio. Los §6.1–6.7
>    de abajo (ventanas, controladores, tamaño, limitaciones) se rehacen con
>    ese diseño.
> 2. La memoria presenta SOLO ese experimento. Las ejecuciones de junio, agosto,
>    la réplica y la del 14/10 son desarrollo; ninguna de sus cifras se cita.
> 3. Borradores: el capítulo 4 y el 5.1–5.3 los tiene Daniel en Word y su
>    versión manda. Al cerrar lo técnico, los pasa y Claude indica qué cambia.
>    Desde el 5.4, Claude rehace los borradores enteros. Mientras dura el
>    blindaje no se redacta.
>
> **ACTUALIZACIÓN 2026-08-12:** (1) De cara a la memoria SOLO existe
> `C:\Users\danie\Documents\TFG Material\` (regla cero; el repo es bruto para
> contexto/planes/bibliografía). (2) La nomenclatura de este plan es la vieja de
> junio: se traduce SIEMPRE con `04_CORRESPONDENCIAS_NOMENCLATURA.md`. (3) Los
> números de resultados citados en este plan son de ejecuciones de DESARROLLO
> (junio, agosto, réplica): ninguno es canónico; los únicos válidos serán los
> del experimento final del blindaje. (4) Citas: SOLO claves de
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
- **Estándar de redacción v2 (13/10, desde el 5.6):** estructura problema →
  idea → mecanismo → ecuación → ejemplo real → límites; ecuaciones numeradas
  para los mecanismos centrales; ejemplos con datos reales del paquete canónico
  reproducidos por script (`docs/memoria/apoyo/`) y elegidos con regla fijada
  de antemano; cada decisión con la alternativa descartada y su motivo; sin
  rayas para incisos ni muletillas; recuentos verificados por programa;
  figuras de datos generadas por script y comprobadas sin solapes.

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

> **ENTREGADO 09/11** como `borradores_docx/cap1_introduccion.docx` (`apoyo/generar_cap1.py`; notas en
> `notas/notas_cap1_introduccion.md`). Estructura final (difiere de la propuesta inicial: el 1.3 pasa a ser
> «Enfoque del trabajo» con las cuatro decisiones de partida y se añade el 1.5 «Alcance» que pide la biblia §4):

**Apertura.** Un párrafo: qué construye el trabajo y mapa 1.1–1.6.
**1.1 Motivación y contexto.** Vídeo = mayoría del tráfico (Seufert 2015 p. 1, Timmerer 2025 p. 2); HAS y DASH
(ISO 23009-1, Stockhammer); la QoE la deciden las paradas y los cambios (Seufert); el estándar no fija el
controlador; campo activo (Bentaleb, Amer, Peroni 2025, Timmerer, Alsader); antecedentes locales del grupo del
tutor (Ameigeiras 2012, Ramos-Muñoz 2014) → «este trabajo continúa esa línea en el controlador del cliente».
**1.2 Problema.** Decisión secuencial bajo incertidumbre con objetivos en conflicto (Yin 2015); dos rasgos:
error de predicción asimétrico (MPC robusto, BayesMPC) y medio VBR (tasa nominal ≠ bytes reales); problema de
evaluación: simulación frente a realidad (Puffer, Hoffman 2025), sesgo de las trazas (CausalSim), el orden
depende del modelo de QoE (Peroni 2024). «Decidir mejor y evaluar de forma defendible».
**1.3 Enfoque del trabajo.** Cuatro decisiones con sus razones + **Figura 1.1** (`fig_1_1_enfoque_trabajo.svg`):
(1) entorno completo propio, cliente ABR-neutral (remite a 2.6); (2) fidelidad al medio (contenido real VBR, 6
calidades 300–4300, 4 s, servidor real; red emulada por trazas sin fuga; entrenamiento con tamaños reales);
(3) aprendizaje acotado a la predicción: cuantiles + MPC con medida de riesgo; 4 clásicos + 3 variantes (leídos
del protocolo); (4) evaluación como ensayo prerregistrado, ejecución única, paquete verificable.
**1.4 Objetivos.** Objetivo general + **Objetivos 1–5** en lista con entradilla «Objetivo n» (cliente; interfaz y
clásicos fieles; controlador propio + entorno de entrenamiento; banco de evaluación reproducible con protocolo
prerregistrado; evaluación y declaración de lo que se puede afirmar). Párrafo final: correspondencia con los
capítulos. **El 7.1 responde a estos cinco, por número.**
**1.5 Alcance.** VoD (no directo ni baja latencia); una pista de vídeo sin audio ni subtítulos (comprobado en el
código: 0 menciones a «audio»); una sesión, un servidor local, sin CDN ni clientes competidores; red emulada
(limitación declarada → 6.7); QoE lineal por bitrate, sin métricas perceptuales ni usuarios; clásicos con
parámetros publicados, sin ajuste.
**1.6 Estructura de la memoria.** Lista con entradilla «Capítulo n» (2–7) y «Anexos», una frase cada uno. Sin
cierre: el capítulo termina en la estructura (corpus del tutor).

Ampliado 09/11 a petición de Daniel (de 7 a 8 páginas) con cinco párrafos verificables: buffer y experiencia (1.1), variabilidad real de tamaños del contenido principal (1.2: cociente máx/mín > 14 en la calidad más alta, leído del descriptor entregado), aportaciones (1.3), material entregado con los 12 conjuntos de trazas (1.5) y convenciones (1.6).

Sin resultados ni cifras del experimento (el script lo comprueba: ninguna cifra decimal, ni 1208, ni 41,3).

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

> REESCRITO 09/11/2026 con el experimento final de la fase de blindaje (único que va a la
> memoria). Fuentes: `docs/blindaje/06_PROTOCOLO_FINAL.md` (diseño fijado antes de ejecutar),
> `docs/blindaje/07_RESULTADO_FINAL.md` (resultados y matices) y el paquete
> `TFG Material\04_evidencia_final\20261015_031741_final_blindaje` (02_resultados, 03_graficas,
> 01_sesiones) más `verificacion_windows_20261016` (auditoría de decisiones, física, huellas).
> Patrón de la biblia §4: preguntas numeradas, cada una con su tabla, la cifra, la interpretación
> y la limitación en el mismo bloque; sin «gana a todos». Lo que ya cuenta Daniel en el cap 4
> (4.7 corpus de trazas, particiones, vídeos y VBR; 4.8 compuertas y planteamiento estadístico) y
> el 5.4 (preset, embudo de ventanas 873→831→707→74, plan de sesiones) NO se repite: se remite y
> se añade solo lo específico del experimento. Numeración: empieza en Figura 6.1, Tabla 6.1 y
> ecuación (6.1). Nunca se cita el indicador `benchmark_autorizado` del paquete (falso por una
> lista de presets antigua): se habla de compuertas superadas y contrastes prerregistrados.

> Apertura (párrafo sin epígrafe): qué venía antes (sistema implementado, cap 5) y qué contiene
> el capítulo: un único experimento final con protocolo fijado antes de ejecutar; 6.1 diseño,
> 6.2 métricas e hipótesis, 6.3 integridad, 6.4 hipótesis, 6.5 descriptivos, 6.6 exploratorio,
> 6.7 interpretación y limitaciones.

**6.1 Diseño del experimento final.** Pregunta (¿iguala el propio al MPC robusto canónico en
QoE y lo mejora en paradas? ¿qué aporta la red frente a estimadores sin red con el mismo
planificador?). Lo que se congela antes de ejecutar: código entregado (103 ficheros), configuración,
modelo (bundle de 5 ficheros), cuantiles fijos, catálogo, descriptor de Tears of Steel, 77 ventanas
esperadas e hipótesis copiadas al protocolo; comprobación en la VM antes de lanzar (huellas,
pruebas automáticas, plan en seco). Red: 74 ventanas reales de 160 s de la partición de evaluación
(Oboe 56, FCC 18), filtro de relevancia de Pensieve sobre la ventana (media < 6 Mbit/s, mínimo
> 0,2 Mbit/s), 42 grupos de captura del desarrollo excluidos (UNA frase metodológica: ninguna
ventana se había ejecutado antes), inicio determinista con semilla 606, bucle de seguridad de una
vuelta; 3 ventanas sintéticas solo de diagnóstico. Contenido: en cada ventana real un vídeo visto
en rotación (Paseo 30/60 fps, Blender 30/60 fps) y Tears of Steel como contenido nuevo (Blender
Foundation, CC-BY 3.0; 1920×800 a 24 fps remuestreado a 30 fps, 600 s, 6 niveles, VBR con CV
0,28–0,31). Controladores: los 8 con su papel (3 clásicos, MPC robusto canónico, propio, 3
variantes de ablación) y la hipótesis en la que intervienen; un solo juego de parámetros por
controlador. Ejecución: VM cliente (192.168.1.160) contra VM servidor (192.168.1.132), en serie,
orden de los controladores sorteado en cada escenario, 30 segmentos y 29 evaluables, nivel inicial
0 sin decisión inicial, buffer 60 s, 1208 sesiones = (74 × 2 + 3) × 8, 41,3 h. Entorno de las
máquinas (el 5.1 de Daniel remite «la topología completa de máquinas» al cap 6): VM cliente y VM
servidor (Ubuntu 20.04, Python 3.8.10, requests 2.32.4, numpy 1.24.4, torch 2.4.1 en CPU),
WSL2 con ROCm para el entrenamiento, Windows para el desarrollo. Ejemplo real: una sesión del plan
con identificadores legibles (regla fijada antes de mirar: la primera sesión del plan en la que
corre el controlador propio), descrita por su número de sesión, ventana, vídeo, posición en el
sorteo y artefactos.
- **[F/T]** **Figura 6.1** diseño del experimento (ventanas × vídeos × controladores → 1208
  sesiones, con lo que se congela), SVG propio. **Tabla 6.1** los 8 controladores: papel e
  hipótesis. **Tabla 6.2** lo que se congela antes de ejecutar (pieza, contenido, huella o
  comprobación; los parámetros del preset ya están en la Tabla 5.5 y se remite a ella).
  **Tabla 6.3** las cuatro máquinas (rol, sistema, CPU y memoria, Python y paquetes que
  ejecutaron el experimento, desde `00_info_entorno` y `entorno.json`).
- **[R]** `core/evaluacion/catalogo.py` (preset `final_blindaje`), `config/evaluacion.local.json`,
  `00_protocolo/protocolo_validacion.json`, `plan_sesiones.csv`, `ventanas_trazas.csv`,
  `docs/blindaje/kit_vm/blindaje_vm.sh`.
- **[B]** `mao2017pensieve` (filtro), `yin2015mpc` (MPC robusto), ficha de Tears of Steel
  (pendiente de permiso).
- **[P]** Propia (diseño prerregistrado).

**6.2 Métricas e hipótesis prerregistradas.** Métrica principal: QoE lineal por sesión sobre los
29 segmentos evaluables, ecuación (6.1): media de bitrate (Mbit/s) − 4,3 · rebuffering (s) −
|Δ bitrate| (Mbit/s), pesos de Pensieve; co-principal de seguridad: paradas por sesión;
secundarias: rebuffering total, bitrate medio, cambios de calidad, QoE logarítmica; retardo de
arranque solo informativo. Hipótesis P1–P5 con referencia el propio: P1 equivalencia de QoE con el
MPC robusto (TOST, margen ±0,15 = 1 s de rebuffering en 29 segmentos, 4,3/29), P2 menos paradas
que el MPC robusto, P3 menos paradas que los cuantiles recientes, P4 más QoE que los cuantiles
fijos, P5 menos paradas que la mediana sola. Unidad: escenario (ventana × vídeo); bloque: ventana
(sus dos escenarios comparten red). Prueba del signo exacta unilateral sobre la diferencia media
por ventana (empates excluidos e informados); IC por bootstrap por bloques de ventanas (10 000
remuestreos, semilla 2026); TOST con p = máximo de los dos unilaterales (aproximación normal sobre
las medias por ventana) e IC90 dentro del margen; Holm sobre P1–P5 con α = 0,05. Todo escrito en
`core/evaluacion/contrastes.py` y copiado al protocolo antes de ejecutar.
- **[F/T]** **Tabla 6.4** métricas por sesión; **Tabla 6.5** las cinco hipótesis (id, enunciado, rival, métrica, prueba).
  Ecuaciones (6.1) QoE lineal, (6.2) TOST (los dos unilaterales), (6.3) Holm. HECHO 09/11; las tablas de 6.3–6.6 pasan a T6.6–T6.10.
- **[B]** `mao2017pensieve` (QoE), Schuirmann 1987 (TOST), Holm 1979, Efron y Tibshirani 1993
  (bootstrap), `peroni2024qoePitfalls` (distribuciones, no solo medias). Las tres estadísticas
  NO están en el .bib: pedir permiso antes de descargar.
- **[P]** Propia: prerregistro, elección de unidad y bloque, margen justificado.

**6.3 Integridad de la ejecución y verificación.** 1208/1208 sesiones completadas, 0 fallidas,
una sola ejecución por sesión, del 15/10 al 16/10/2026, 41,3 h sin huecos; 8 compuertas superadas
y 15 comprobaciones del paquete; 0 respaldos en las 604 sesiones del propio y sus variantes
(17 516 decisiones); latencia de decisión p99 4,4 ms, inferencia ≤ 5,6 ms; mismo entorno en las
1208 sesiones; auditoría de decisiones: 35 032/35 032 idénticas al repetirlas con el código
congelado desde la realimentación registrada (contraprueba: α = 0,5 cambia 96, MPC no robusto
876); fidelidad del simulador en modo forzado (mediana |ΔQoE| = 0, p90 0,006); análisis
reproducido en Windows (contrastes idénticos); huellas de los 9699 ficheros. Las 77 ventanas
coinciden con las esperadas.
- **[F/T]** **Tabla 6.6** comprobaciones de integridad (qué, resultado).
- **[R]** `verificacion_paquete.{md,json}`, `verificacion_windows_20261016/*.json`,
  `resumen_resultados.json` (auditoría de inferencia).
- **[P]** Propia (rigor).

**6.4 Resultados de las hipótesis prerregistradas.** Tabla principal P1–P5 con media de la
diferencia, IC95, IC90, ventanas +/−/=, p y p de Holm, y la decisión. Las cinco se aceptan: P1
−0,001 con IC90 [−0,018; +0,017] dentro de ±0,15 (cabría en ±0,02); P2 −0,122 paradas por sesión
(61 ventanas empatadas, 12 de 13 a favor del propio); P3 −0,439; P4 +0,149; P5 −0,791. Cada
cifra con su interpretación y lo que NO dice (P1 no es superioridad en QoE).
- **[F/T]** **Tabla 6.7** P1–P5 recalculada por el script desde `contrastes_prerregistrados.json`
  (debe coincidir). **Figura 6.2** diferencias por ventana (propio − MPC robusto en QoE y en
  paradas) con el margen de equivalencia y los IC, matplotlib desde `sesiones.csv`.
- **[P]** Propia.

**6.5 Resultados descriptivos por controlador.** Tabla de agregados de las 148 sesiones reales por
controlador (QoE lineal, QoE log, bitrate, rebuffering, paradas por sesión, sesiones con parada,
cambios), ordenada por QoE lineal. Lectura honesta: el propio NO tiene la QoE media más alta (las
dos variantes más arriesgadas lo superan en 0,02–0,04); iguala al MPC canónico con 4 veces menos
paradas (0,041 frente a 0,162; 4,1 % frente a 14,9 % de sesiones con parada). Descomposición de la
diferencia de QoE por componentes (bitrate, rebuffering, suavidad) frente a cada rival: frente al
MPC cede 59 kbit/s y lo recupera en rebuffering y suavidad. Lo que aporta cada pieza: red frente a
cuantiles recientes (−0,036 QoE, 12 veces menos paradas), frente a cuantiles fijos (+0,149 QoE,
misma seguridad), CVaR frente a mediana (−0,024 QoE no significativo, 20 veces menos paradas).
Frente a los clásicos: BBA +0,315, basado en tasa +0,796, BOLA +1,353 (BOLA sufre en baja
capacidad, 4,05 s de rebuffering por sesión).
- **[F/T]** **Tabla 6.8** agregados por controlador (de `agregados_por_controlador.json`,
  recalculados desde `sesiones.csv`). **Tabla 6.9** descomposición de ΔQoE por componentes.
  **Figura 6.3** CDF de la QoE lineal por controlador y **Figura 6.4** paradas o rebuffering
  frente a bitrate medio (dispersión), ambas REHECHAS con estilo sobrio desde `sesiones.csv`;
  las PNG del paquete (`03_graficas`) no se pegan tal cual (decidir por figura y decirlo).
- **[P]** Propia.

**6.6 Análisis secundario exploratorio.** Marcado como exploratorio, sin claims: estratos Oboe
(56) y FCC (18); vídeos vistos frente a Tears of Steel (propio − MPC: +0,021 frente a −0,023 en
QoE; −0,176 frente a −0,068 en paradas); interacción de contenido −0,045 [−0,077; −0,014] con
signo p = 0,34 (40/31/3): con el contenido nuevo la ventaja en paradas se reduce y la QoE queda
algo por debajo; hipótesis de trabajo NO comprobadas (VBR mucho mayor, dos primeros segmentos
casi negros). Las 3 sintéticas aparte (propio 2,448 y 0 paradas; MPC 2,416 y 0,33; n = 3, nada
se concluye).
- **[F/T]** **Tabla 6.10** estratos (ventanas, ΔQoE con IC95, Δparadas con IC95).
- **[P]** Propia (honestidad).

**6.7 Interpretación y limitaciones.** Qué se puede afirmar (equivalencia en QoE con el MPC
canónico en 74 ventanas emuladas con dos contenidos, menos paradas, aportación de la red y del
CVaR, todo prerregistrado y corregido por Holm) y qué no (mejor QoE; mejorar al MPC en QoE;
generalizar a redes con TCP y tráfico competidor, a otros contenidos o a métricas perceptuales).
Limitaciones declaradas: emulación sin TCP ni tráfico competidor; ventanas concentradas en Oboe y
FCC; un solo contenido nuevo; bitrate como proxy sin VMAF; α y el modelo elegidos con la partición
de validación; equivalencia probada contra UNA referencia canónica con sus parámetros por defecto;
una repetición por escenario (determinista). Desviaciones del protocolo: ninguna (07_RESULTADO §7).
- **[P]** Propia.

> Cierre del capítulo: dos o tres párrafos sin epígrafe (como en el cap 5) que recapitulan y
> enlazan con el 7.

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
| F1.1 | Enfoque del trabajo: real/emulado, interfaz común con clásicos + propio + variantes, entrenamiento fuera de línea, protocolo → experimento único → paquete (HECHA 09/11) | 1.3 | `fig_1_1_enfoque_trabajo.svg` (propia) |
| F1 | Arquitectura de módulos del cliente | 4.1 | diagrama propio |
| F2 | Flujo de una sesión (secuencia) | 4.1 | diagrama propio |
| F3 | Interfaz del controlador ABR | 4.5 | diagrama propio |
| F4 | Red (trazas) vs medio (VBR) | 4.7 | diagrama propio |
| F5.2 | Flujo del ejecutor de experimentos (HECHA 09/11) | 5.4 | `fig_5_2_ejecutor_evaluacion.svg` |
| F5.3 | Decisión real del MPC robusto (HECHA 09/11, script) | 5.5 | `fig_5_3_decision_mpc_robusto.svg` |
| F5.4 | Arquitectura del controlador propio (HECHA) | 5.6 | `fig_5_4_arquitectura_controlador_propio.svg` |
| F5.5 | Decisión real del controlador propio (HECHA 09/11, script) | 5.6 | `fig_5_5_decision_propio.svg` |
| F5.6 | Entorno de entrenamiento fiel al medio (HECHA 09/11) | 5.7 | `fig_5_6_entorno_entrenamiento.svg` |
| F6 | Bucle de decisión del controlador | 5.6 | diagrama propio |
| F6.1 | Diseño del experimento final (ventanas × vídeos × controladores → 1208 sesiones; lo que se congela) | 6.1 | `fig_6_1_diseno_experimento.svg` (propia) |
| F6.2 | Diferencias por ventana propio − MPC robusto (QoE y paradas) con margen e IC (HECHA 09/11) | 6.4 | `fig_6_2_diferencias_por_ventana.svg` (matplotlib desde `sesiones.csv` y `contrastes_prerregistrados.json`) |
| F6.3 | CDF de la QoE lineal por controlador (rehecha, estilo sobrio) (HECHA 09/11) | 6.5 | `fig_6_3_cdf_qoe.svg` (matplotlib desde `sesiones.csv`) |
| F6.4 | Paradas frente a bitrate medio por controlador (rehecha) (HECHA 09/11) | 6.5 | `fig_6_4_paradas_bitrate.svg` (matplotlib desde `sesiones.csv`) |
| F7 | Topología de los 4 entornos: DESCARTADA (va como Tabla 6.3) | — | — |
| F3.1 | Diagrama de Gantt (HECHA 09/11, desde `planificacion_cap3.json`) | 3.2 | `fig_3_1_gantt.svg` |

(Las figuras propias las puedo generar en SVG/diagrama cuando lleguemos a cada cap.)

## 7. Mapa global de tablas

| # | Tabla | Capítulo |
|---|---|---|
| T2.1 | Comparativa de familias ABR (HECHA 09/11) | 2.4 |
| T3.1 | Fases → tareas → entregable (HECHA 09/11) | 3.1 |
| T3.2 | Horas por fase (HECHA 09/11) | 3.3 |
| T3.3 / T3.4 | Hardware amortizado / coste total (HECHAS 09/11) | 3.4 |
| T6.1 | Los 8 controladores: papel e hipótesis en la que intervienen | 6.1 |
| T6.2 | Lo que se congela antes de ejecutar (pieza, contenido, huella o comprobación) | 6.1 |
| T6.3 | Las cuatro máquinas del proyecto (rol, sistema, hardware, Python y paquetes) | 6.1 |
| T6.4 | Métricas por sesión (definición, unidad, papel) (HECHA 09/11) | 6.2 |
| T6.5 | Hipótesis prerregistradas P1–P5 (enunciado, rival, métrica, prueba) (HECHA 09/11) | 6.2 |
| T6.6 | Comprobaciones de integridad de la ejecución y del paquete (HECHA 09/11) | 6.3 |
| T6.7 | Resultados P1–P5: media, IC95, IC90, ventanas +/−/=, p, p Holm, decisión (HECHA 09/11) | 6.4 |
| T6.8 | Agregados por controlador (148 sesiones reales) (HECHA 09/11) | 6.5 |
| T6.9 | Descomposición de ΔQoE por componentes frente a cada rival (HECHA 09/11) | 6.5 |
| T6.10 | Estratos exploratorios (Oboe/FCC, visto/nuevo) (HECHA 09/11) | 6.6 |
| T7 | Corpus de trazas (los 12 conjuntos) | Anexo D (el cap 4.7 ya lo resume) |

---

## 8. Material del repo ya reutilizable (no reinventar)

- **FUENTE DE VERDAD del sistema descrito:** `C:\Users\danie\Documents\TFG Material\`
  (código `01_codigo\ClienteDashTFG`, corpus `02_corpus_red\catalogo_trazas.json`,
  bundle `03_modelos`, **evidencia canónica `04_evidencia_final\` (solo el paquete del experimento final)**,
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
| Cap 1 Introducción | **ENTREGADO 09/11** (`borradores_docx/cap1_introduccion.docx`, ≈3400 palabras, 8 páginas; apertura, 1.1 motivación, 1.2 problema, 1.3 enfoque con F1.1 `fig_1_1_enfoque_trabajo.svg/png`, 1.4 Objetivos 1–5 numerados, 1.5 alcance, 1.6 estructura; 17 citas ya verificadas en los caps 2 y 5; `apoyo/generar_cap1.py` lee escalera, controladores y variantes del material entregado y comprueba que no hay cifras de resultados; notas en `notas/notas_cap1_introduccion.md`) | Siguiente: capítulo 7 (responde a los Objetivos 1–5 por número) |
| Cap 2 Estado del arte | **APERTURA + 2.1 + 2.2 ENTREGADOS 09/11** (`borradores_docx/cap2_1_2_has_dash.docx`, ≈1520 palabras, 9 citas verificadas con página; `apoyo/generar_cap2_1_2.py`; notas en `notas/notas_cap2_1_2_has_dash.md`). **2.3 + 2.4 ENTREGADOS 09/11** (`borradores_docx/cap2_3_4_problema_familias.docx`, ≈2190 palabras, Tabla 2.1 de familias, 15 citas con página; `apoyo/generar_cap2_3_4.py`; notas en `notas/notas_cap2_3_4_problema_familias.md`). **2.5 + 2.6 + 2.7 + CIERRE ENTREGADOS 09/11** (`borradores_docx/cap2_5_7_qoe_reproductores_lagunas.docx`, ≈1790 palabras, 22 citas; `apoyo/generar_cap2_5_7.py`; notas en `notas/notas_cap2_5_7_qoe_reproductores_lagunas.md`). **CAPÍTULO 2 COMPLETO** (2.1–2.7 + cierre; T2.1; sin figuras). Siguiente: capítulo 3 | Fuentes: 02_BIBLIOGRAFIA §2.1–2.3; .md convertidos en `docs/todos los estudios pdf convertidos a md/` para buscar, PDF de `biblioteca_final` para la página |
| Cap 3 Planificación/costes | **ENTREGADO 09/11** (`borradores_docx/cap3_planificacion_costes.docx`, ≈1390 palabras; F3.1 Gantt `fig_3_1_gantt.svg/png`; T3.1 fases→tareas→entregable, T3.2 horas, T3.3 hardware, T3.4 total; ec. 3.1 amortización). **DATOS EDITABLES en `apoyo/planificacion_cap3.json`** (fases, fechas, horas, tarifas, hardware); regenerar con `apoyo/generar_cap3.py`. Notas en `notas/notas_cap3_planificacion_costes.md` | Supuestos a revisar por Daniel: fechas de F1, horas (300 = 12 ECTS × 25 h), tarifas 20/50 €/h, precios del hardware |
| Cap 4 Diseño | REDACTADO POR DANIEL EN WORD; REVISADO 09/11 (`notas/revision_cap4_contenido_20261109.md`: C1–C32, F4.2/F4.5/F4.6 textos) | Su Word manda; no tocar los borradores del repo. Al cerrar el blindaje, Daniel pasa el Word y Claude indica cambios de texto y figuras (lista orientativa en §8 del traspaso de `docs/blindaje/`). Historial: 4.1–4.7 redactados por Daniel; 4.8 BORRADOR entregado 27/08 (cap4_8_separacion_evaluacion.md + T4.7 gates + resumen del capítulo). Al masticar 4.8: pasada de coherencia del capítulo entero. 14/10 (cc38089): borradores devueltos al estado del remake del 5.6; solo se añaden "validación" (4.7 y T4.7) y el paso de espera de 0,01 s en la evaluación (4.3/T4.3). La frase del empate del 4.7 se revisa con el experimento final |
| Cap 5 Implementación | 5.1–5.2 EN WORD DE DANIEL (revisados 09/11: `notas/revision_cap5_1_5_2_contenido_20261109.md`); **5.3 ENTREGADO 09/11** (`borradores_docx/cap5_3_analizador_mpd.docx`, 1201 palabras, T5.3 y T5.4, ec. 5.1, 5 citas verificadas en PDF; notas en `notas/notas_cap5_3_analizador_mpd.md`); **5.4 ENTREGADO 09/11** (`borradores_docx/cap5_4_ejecutor_configuracion.docx`, 1634 palabras, F5.2 `fig_5_2_ejecutor_evaluacion.svg/png`, T5.5 y T5.6, ec. 5.2 y 5.3; selección de ventanas reproducida con el código del entregable: 77/77 iguales al paquete; notas en `notas/notas_cap5_4_ejecutor_configuracion.md`); **5.5 ENTREGADO 09/11** (`borradores_docx/cap5_5_controladores_clasicos.docx`, 1747 palabras, F5.3 `fig_5_3_decision_mpc_robusto.svg/png` generada por script desde el paquete, T5.7 y T5.8, ec. 5.4–5.6, 6 citas verificadas; 29/29 decisiones de una sesión del MPC robusto reproducidas; notas en `notas/notas_cap5_5_controladores_clasicos.md`); **5.6 ENTREGADO 09/11** (`borradores_docx/cap5_6_controlador_propio.docx`, ≈3250 palabras, F5.4 arquitectura y F5.5 decisión real por script, T5.9–T5.12, ec. 5.7–5.12, 7 citas; 4379/4379 decisiones del propio reproducidas desde el paquete final con `apoyo/reproducir_propio_final.py`; notas en `notas/notas_cap5_6_controlador_propio.md`); **5.7 ENTREGADO 09/11** (`borradores_docx/cap5_7_entorno_entrenamiento.docx`, ≈1735 palabras, F5.6, T5.13–T5.15, ec. 5.13–5.14; calibración del modelo entregado recalculada con `apoyo/calibracion_validacion.py` sobre las 111 630 muestras de validación; notas en `notas/notas_cap5_7_entorno_entrenamiento.md`). **RESUMEN DEL CAPÍTULO ENTREGADO 09/11** (`borradores_docx/cap5_8_resumen_capitulo5.docx`, 425 palabras, 3 párrafos sin epígrafe, cierre del 5.7 según biblia §6.3; `apoyo/generar_cap5_resumen.py` verifica que cada cifra ya está en 5.1–5.7; el 5.7 se regeneró sin sus dos frases de cierre, 1702 palabras; notas en `notas/notas_cap5_resumen.md`). CAPÍTULO 5 COMPLETO (5.1–5.2 de Daniel + 5.3–5.7 y cierre de Claude) | 5.1–5.3: igual que el cap 4 (Word de Daniel; Claude indica cambios al cerrar lo técnico). 5.4–5.7: Claude rehace los borradores ENTEROS con el experimento final del blindaje; los actuales del repo son base. Historial: 5.1–5.5 masticados por Daniel. 5.6 VERSIÓN 2 entregada 13/10 (cap5_6_controlador_propio.md rehecho: 6 subapartados, 8 ecuaciones, decisión real reproducida, T5.6 comparativa MPC/robusto/propio, T5.7 efecto de cada componente, ficha al Anexo A; F5.2 rehecha + F5.3 nueva `fig_5_3_decision_real.svg` generada por script; reproducción 1740/1740 en `docs/memoria/apoyo/`). 14/10 (cc38089): borradores devueltos al estado del remake del 5.6; correcciones válidas: 5.1 (requests 2.32.4, matplotlib 3.7.5, NumPy como dependencia del planificador), 5.4 (configuración final con grupos de captura excluidos y la frase metodológica de las ventanas) y 5.5 (referencia "fijada antes de evaluar, por diseño"). El 5.6 se actualiza en UNA pasada con el paquete final (lista en sus notas). cap5_1 queda SIN commitear porque lleva cambios de Daniel pendientes. Siguiente: 5.7 entorno de entrenamiento fiel. PENDIENTE EN CAP 4: corregir T4.3 "paso de espera 0,5 s" → "0,5 s (0,01 s en la evaluación)" |
| Cap 6 Evaluación | ESQUEMA REESCRITO 09/11 con el experimento final (§5, Capítulo 6: 6.1–6.7 y cierre; mapas de figuras F6.1–F6.4 y tablas T6.1–T6.9). **6.1 ENTREGADO 09/11** (`borradores_docx/cap6_1_diseno_experimento.docx`: apertura del capítulo + 6.1.1–6.1.4, ≈1890 palabras, F6.1 `fig_6_1_diseno_experimento.svg/png`, T6.1 controladores e hipótesis, T6.2 lo que se congela, T6.3 máquinas; ejemplo = sesión 8 del plan; `apoyo/generar_cap6_1.py` recalcula todo desde el paquete, el kit y el código y verifica las huellas; notas en `notas/notas_cap6_1_diseno_experimento.md`). **6.2 ENTREGADO 09/11** (`borradores_docx/cap6_2_metricas_hipotesis.docx`, ≈1810 palabras, T6.4 métricas, T6.5 hipótesis, ec. 6.1 QoE, 6.2 TOST, 6.3 Holm; ejemplo = QoE de la sesión 8 recalculada desde sus segmentos con el módulo del entregable; 6 citas verificadas; `apoyo/generar_cap6_2.py`; notas en `notas/notas_cap6_2_metricas_hipotesis.md`). **6.3 ENTREGADO 09/11** (`borradores_docx/cap6_3_integridad_verificacion.docx`, ≈1340 palabras, T6.6; `apoyo/generar_cap6_3.py` recalcula las 9699 huellas del paquete y repite el análisis prerregistrado con el módulo del entregable (0 diferencias > 1e-9, caché en `apoyo/contrastes_reproducidos.json`); notas en `notas/notas_cap6_3_integridad_verificacion.md`). **6.4 ENTREGADO 09/11** (`borradores_docx/cap6_4_resultados_hipotesis.docx`, ≈970 palabras, T6.7 desde `contrastes_prerregistrados.json` cotejada con el análisis repetido, F6.2 `fig_6_2_diferencias_por_ventana.svg/png` por matplotlib desde `sesiones.csv`; `apoyo/generar_cap6_4.py`; notas en `notas/notas_cap6_4_resultados_hipotesis.md`). **6.5 ENTREGADO 09/11** (`borradores_docx/cap6_5_descriptivos.docx`, ≈1140 palabras, T6.8 agregados recalculados = `agregados_por_controlador.json`, T6.9 descomposición de ΔQoE, F6.3 CDF y F6.4 paradas-bitrate rehechas con matplotlib; `apoyo/generar_cap6_5.py`; `memoria_docx.tabla` ahora con anchos fijos; notas en `notas/notas_cap6_5_descriptivos.md`). **6.6 ENTREGADO 09/11** (`borradores_docx/cap6_6_exploratorio.docx`, ≈1260 palabras, T6.10 estratos recalculados con las funciones del entregable; interacción 40/31/3; sintéticas aparte; `apoyo/generar_cap6_6.py`; notas en `notas/notas_cap6_6_exploratorio.md`). **6.7 + CIERRE ENTREGADOS 09/11** (`borradores_docx/cap6_7_interpretacion_cierre.docx`, ≈1280 palabras: qué se afirma y qué no, 8 limitaciones, fidelidad al protocolo, cierre sin epígrafe; `apoyo/generar_cap6_7.py` comprueba que no introduce cifras nuevas; notas en `notas/notas_cap6_7_interpretacion_cierre.md`). **CAPÍTULO 6 COMPLETO** (6.1–6.7 + cierre; F6.1–F6.4; T6.1–T6.10; ec. 6.1–6.3). Siguiente: capítulos 2, 3, 1 y 7 | 14/10 noche: el experimento con el kit de `docs/evaluacion_final/` se detuvo (desarrollo, no se analiza). El diseño nuevo (controladores, ventanas, vídeos, estadística) sale de la fase de blindaje (`docs/blindaje/`). Historial: EXPERIMENTO FINAL ÚNICO con la versión final del controlador (planificador vectorizado, inferencia de un hilo, calentamiento, entradas como en el entrenamiento) y 12 ventanas nunca ejecutadas; protocolo y kit en `docs/evaluacion_final/`. Las ejecuciones de agosto y de la réplica son desarrollo (archivadas en `TFG\legacy\evidencia_desarrollo\`) y no van a la memoria |
| Cap 7 Conclusiones | TODO | al final |
| Bibliografía (BibTeX) | HECHA (96 entradas) | `bibliografia.bib` cerrado 10/08; 4 altas 09/11 para el cap 6 (TOST, Holm, bootstrap, Tears of Steel); solo se imprime lo citado |
| Anexos | TODO | |
| Tabla de correspondencias | HECHA 12/08 | `04_CORRESPONDENCIAS_NOMENCLATURA.md` |
| Plantilla .docx y tooling | HECHA 09/11 | `plantilla/plantilla_memoria_ugr.docx` (biblia §2) generada por `apoyo/memoria_docx.py`; `apoyo/comprobar_borrador_docx.py` (lista §7.4 de la biblia) y `apoyo/docx_a_pdf.py` (render con Word) |
