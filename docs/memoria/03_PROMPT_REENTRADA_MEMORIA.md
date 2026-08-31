# Prompt de reentrada al hilo de la memoria (v3 — 27/08/2026)

> Uso: copiar TODO lo que hay debajo de la raya y pegarlo tal cual como primer
> mensaje del NUEVO hilo de la memoria (hilo del capítulo 5). Versionado aquí
> para que cualquier hilo sepa qué contexto se le dio.
>
> v3 (27/08): capítulo 4 COMPLETO en borradores (8 apartados + F4.1–F4.6 +
> T4.1–T4.7), protocolo por apartado rodado, hilo VBR de 6 preguntas resuelto
> y apuntado. El hilo nuevo arranca directamente con el capítulo 5.
> v2 (10/08): paquete canónico 20260810_133520_tfg_final; regla cero TFG Material.

---

Retomamos la redacción de la MEMORIA de mi TFG (cliente DASH + controlador ABR
propio). Venimos de un hilo donde completamos TODO el capítulo 4 (Diseño) con
un protocolo que funcionó de lujo; tú eres el mismo arquitecto de la memoria y
mi guía milimétrica. Este hilo es para el CAPÍTULO 5 (Implementación).

REGLA CERO — FUENTE DE VERDAD (no la olvides nunca):
De cara a la memoria SOLO EXISTE `C:\Users\danie\Documents\TFG Material\`.
Es el material final de entrega: `01_codigo\ClienteDashTFG` (el código real que
se describe y defiende: podado, en castellano, 81 .py), `02_corpus_red`,
`03_modelos\modelo_propio\bundle`, `04_evidencia_final`, `05_contenido_dash`
(completo, 12,5 GB), `06_dataset_entrenamiento`, `00_info_entorno` y su
`LEEME.md` (actualizado 12/08). El repo donde trabajas
(DashClientModular4/GitHub) es el BRUTO: sirve para contexto, planes,
decisiones y bibliografía (docs/), pero su código está en nomenclatura vieja
inglesa y NO es lo que se entrega. Si el repo y TFG Material discrepan, manda
TFG Material. ANTES de redactar cada apartado, LEES el código real del
entregable que le corresponde (así se hizo todo el cap 4: nada se afirma sin
verificarlo en código o datos).

Ponte al día EN ESTE ORDEN (sin narrarme cada lectura; resumen final corto):

1. `CLAUDE.md` + tu memoria persistente — la clave es
   `memoria-redaccion-estado` (estado del hilo de redacción: números canónicos,
   qué está entregado, el hilo VBR de 6 preguntas con sus destinos por
   apartado, apuntes para 5.5/5.6/5.7/6.7/7.4). También
   `bibliografia-tfg-estado`, `ordenacion-material-tfg`,
   `revision-consciente-agosto`, `memoria-tooling-y-no-rastro-ia`.
2. `docs/memoria/00_PLAN_MAESTRO_MEMORIA.md` — la biblia (índice expandido).
   Su §9 tiene el checklist al día. OJO: nomenclatura vieja de junio → se
   traduce SIEMPRE con `docs/memoria/04_CORRESPONDENCIAS_NOMENCLATURA.md`.
   El reparto de la emulación ya está fijado en el plan: replay→5.2,
   normalización del corpus→6.3(+cap 3), muestreo de ventanas→5.7.
3. `docs/memoria/02_BIBLIOGRAFIA_DEFINITIVA.md` + `bibliografia.bib` (92
   claves): las ÚNICAS citas válidas; ni una referencia fuera del .bib.
   NORMA PDF-PRIMERO: toda afirmación con cita se verifica contra el PDF
   original de `C:\Users\danie\Documents\TFG\literatura\biblioteca_final\`
   (ficheros renombrados a su clave BibTeX; los .md convertidos del repo son
   solo índice de búsqueda).
4. Los 8 borradores del cap 4 en `docs/memoria/borradores/cap4_*.md` —
   LÉELOS: definen el estilo, la terminología ya fijada y las fronteras
   diseño↔implementación (cada uno delega detalles concretos al cap 5; esas
   promesas hay que cumplirlas ahora). Yo los mastico y reescribo en Word, y
   edito las figuras SVG con Boxy — los cambios que veas en borradores y
   figuras son míos: NUNCA los reviertas; si ves un typo mío, avísame sin
   tocarlo.
5. `docs/contexto rama original/01_baselines/<x>/notes_for_memory.md` +
   `paper_card.md` + `implementation_spec.md` de los 5 clásicos — material ya
   escrito que se reutiliza en el 5.5 (con Citation Plan).
6. `docs/defensa/componentes_experimento.md` (versiones exactas de todo) y
   `docs/defensa/apropiacion_codigo.md` + `preguntas_tribunal.md` si existen.
   `HANDOFF_mpc_prudente_estado_completo_20260624.md` solo como contexto
   técnico del controlador propio — ADVERTENCIA: sus números son de junio.
7. `docs/contexto rama nueva/fase_4_5_v1/decision_revision_final_tecnica_20260805.md`
   — cómo se redactan los resultados (citar CI, no solo medias). Y las
   decisiones `decision_mpc_prudente_*.md` como contexto del diseño del
   controlador propio (nomenclatura vieja).

EVIDENCIA CANÓNICA (no se re-verifica, se usa): TODOS los números de
resultados salen EXCLUSIVAMENTE del paquete
`TFG Material\04_evidencia_final\20260810_133520_tfg_final` (300 sesiones,
5 controladores, gates 8/8). Los números que veas en HANDOFF/plan
maestro/decisiones de junio NO van a la memoria. Los números clave ya están
resumidos en la memoria persistente (`memoria-redaccion-estado`) y en el §5
cap 6 del plan maestro (reescrito con el paquete canónico).

ESTADO ACTUAL (27/08): capítulo 4 COMPLETO — 8 borradores entregados y
masticados por mí (4.1 visión global, 4.2 analizador MPD, 4.3
descarga/buffer, 4.4 motores, 4.5 interfaz de controladores, 4.6 telemetría,
4.7 red y medio con el párrafo de justificación VBR verificado contra PDFs,
4.8 separación ejecución/evaluación + resumen del capítulo). Figuras
F4.1–F4.6 en `docs/memoria/figuras/` (SVG editables, estilo sobrio: grises +
azul #1971c2 decisión + amarillo #fff9db asíncrono/medio + rojo #c92a2a
alertas — MANTENER ese estilo). Tablas T4.1–T4.7 dentro de los borradores.

EL ENCARGO (mismo protocolo rodado, innegociable): trabajamos UN apartado por
turno. En cada turno me entregas el paquete completo:
(a) Alcance (qué cuenta y qué NO, para no pisar otros apartados).
(b) BORRADOR COMPLETO en español, impersonal, frases cortas, calidad
    académica alta (soy alumno del Grado de Teleco, ETSIIT UGR — nivel de TFG
    de grado, no paper), listo para masticar; la longitud que necesite. En la
    memoria no queda NINGÚN rastro de IA.
(c) FIGURAS que toquen: SVG editable hecho por ti con contenido técnico EXACTO
    del entregable, verificado renderizándolo (abrir en el navegador y
    corregir solapes ANTES de entregarlo), pie numerado y referencia en el
    texto. Nada de IA generativa de imágenes. Me las envías renderizadas.
(d) TABLAS con contenido real del entregable o del paquete canónico.
(e) CITAS: solo claves del .bib, las del plan; afirmaciones con cita
    verificadas contra el PDF original (pdfminer; el Read visual de PDF no
    funciona en este entorno).
(f) Checklist de cierre + actualizar el §9 del plan maestro + commit y push
    con rutas explícitas (nunca git add .) + notas "no van a la memoria" con
    los argumentos de defensa y citas textuales cuando las haya.
Cuando yo diga "listo, X terminado, vamos con Y", conservas mis versiones
masticadas tal cual y sigues.

PLAN DE SESIÓN DEL CAPÍTULO 5 (construido en el hilo anterior; síguelo):
- 5.1 Lenguaje, frameworks y librerías (por qué Python puro, requests,
  ElementTree, PyYAML, PyTorch solo para el propio, GStreamer opcional;
  versiones reales de componentes_experimento; cita digregorio2026mlLoading
  para la carga segura del modelo, weights_only).
- 5.2 Cliente y reproductor — INCLUYE la implementación del replay
  (`core/reproduccion_trazas/`): cargador+validación del CSV, modelo de red,
  descargador controlado. Fragmentos de código SOLO si explican una decisión.
- 5.3 Analizador del MPD (ElementTree, namespaces, duraciones ISO 8601,
  parseo binario del sidx — lo prometido en 4.2).
- 5.4 Runner y configuración (scripts/3_evaluacion/ejecutar_evaluacion.py,
  GUI tkinter, config JSON, generación de configs por sesión).
- 5.5 Baselines clásicos (basado_en_tasa/bba/bola/mpc/mpc_robusto):
  REUTILIZAR notes_for_memory + paper cards; mapping fórmula-paper→código;
  citas liu2011rateAdaptation, huang2014bba, spiteri2020bola, yin2015mpc
  (+spiteri2019dashjs contexto). Marco "familias reactiva vs informada del
  contenido" del hilo VBR.
- 5.6 Controlador propio — EL PLATO FUERTE (2 turnos si hace falta):
  predictor de cuantiles (ensemble de 5 GRU, incertidumbre epistémica que
  ensancha la cola inferior) + planificador CVaR (α=0,75 fijo, tamaños VBR
  reales, media de los escenarios pesimistas q10/q25/q50) + salvaguardas
  (respaldo mpc_robusto, latencia máx 50 ms, hashes) + ARQUITECTURA DE
  GENERALIZACIÓN (predictor agnóstico al contenido; tabla del vídeo activo
  como dato → vídeo nuevo sin reentrenar). Citas: kan2021bayesmpc,
  yan2020puffer, koenker1978quantiles, rockafellar2000cvar, cho2014gru,
  lakshminarayanan2017ensembles. Figuras nuevas F5.x: arquitectura
  predictor+planificador y bucle de decisión (F5/F6 del plan maestro).
  USAR las respuestas del hilo VBR (en memoria-redaccion-estado): reacción vs
  anticipación, tres papeles de la información, chuletas de defensa.
- 5.7 Entorno de entrenamiento fiel (entrenamiento/: simulador de sesiones,
  dataset de cuantiles, muestreo de ventanas SOLO de la partición de
  entrenamiento, rotación de los 8 vídeos, entrenamiento del ensemble en WSL
  con ROCm, exportación del bundle). Contar: los tamaños como FÍSICA del
  entorno (tres papeles), régimen de diseño declarado, y el resultado
  negativo del predecesor CBR como motivación (sin números de junio).
- Cierre: resumen del capítulo 5 + pasada de coherencia.

REGLAS DE ESTILO (plan maestro §2): impersonal; una idea por frase; capítulo
abre con contexto y cierra con resumen; siglas definidas la primera vez;
figuras/tablas numeradas, con pie, referenciadas, nada decorativo; títulos de
papers en inglés; terminología del entregable (04_CORRESPONDENCIAS §5:
"controlador propio", nunca mpc_prudente/v2/Phase 6); cero claims sin el
paquete canónico; ≤100 páginas en total (el cap 5 debe ser sustancioso pero
no un manual: fragmentos de código solo si justifican una decisión).

Reparto de herramientas: TÚ = arquitecto + capítulos técnicos + figuras +
tablas + coherencia. NotebookLM = solo cap 2 (más adelante) y estudio para la
defensa. Prism/LaTeX = solo maquetar texto ya masticado. Yo paso los
borradores a limpio en Word.

PRIMER TURNO DE ESTE HILO: ponte al día con las lecturas de arriba (di solo
"al día" + 3-4 líneas de confirmación del estado) y entrega DIRECTAMENTE el
paquete completo del **5.1** según el protocolo. Después seguimos apartado a
apartado como siempre.
