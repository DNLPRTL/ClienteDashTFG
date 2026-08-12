# Prompt de reentrada al hilo de la memoria (generado 10/08/2026)

> Uso: copiar TODO lo que hay debajo de la raya y pegarlo tal cual como primer
> mensaje al retomar el hilo/chat de la memoria. Versionado aquí para que
> cualquier hilo sepa qué contexto se le dio al de la memoria.

---

Retomo el TFG tras un mes parado para EMPEZAR A REDACTAR LA MEMORIA. Tú eres el
arquitecto de la memoria y mi guía milimétrica. Antes de proponer nada, ponte
al día EN ESTE ORDEN (todo son rutas del repo, léelas de verdad):

1. `CLAUDE.md` + tu memoria persistente (en especial `bibliografia-tfg-estado`,
   `ordenacion-material-tfg`, `revision-consciente-agosto`,
   `fase1-revision-final-hallazgos`, `memoria-tooling-y-no-rastro-ia`).
2. `docs/memoria/00_PLAN_MAESTRO_MEMORIA.md` — la biblia: índice expandido con
   [Q]/[R]/[F-T]/[B]/[P] de cada apartado. ES LA ESTRUCTURA, no se cambia.
3. `docs/memoria/02_BIBLIOGRAFIA_DEFINITIVA.md` + `docs/memoria/bibliografia.bib`
   — bibliografía CERRADA y VERIFICADA (10/08): lista ganadora anotada por
   capítulo, descartes, normativa ETSIIT aplicada. Las claves de ese `.bib` son
   las ÚNICAS citas válidas; ni una referencia fuera de él.
4. `docs/memoria/01_INVENTARIO_BIBLIOGRAFIA.md` — mapa fichero→fuente de los
   ~100 PDFs de `C:\Users\danie\Documents\TFG\literatura\`.
5. `docs/contexto rama nueva/fase_4_5_v1/HANDOFF_mpc_prudente_estado_completo_20260624.md`
   y `docs/defensa/componentes_experimento.md` — estado técnico final y
   componentes reales (máquinas, versiones, generación DASH).
6. `docs/contexto rama nueva/fase_4_5_v1/decision_revision_final_tecnica_20260805.md`
   — CÓMO se redactan los resultados (matices win/loss; "citar el CI, no solo
   las medias").
7. Material reutilizable ya escrito: `docs/contexto rama original/01_baselines/<x>/notes_for_memory.md`
   (los 5 clásicos, con Citation Plan), `docs/contexto rama original/07_memory/`
   (política de citación, registro de figuras/tablas F1-F30/T1-T49) y los
   `why_not_*.md` de `04_neural_abr` (resultados negativos del cap 7.5).

QUÉ HA PASADO en este mes (para que no trabajes con estado viejo):

- **Revisión técnica final + naturalización**: el código se castellanizó y
  renombró ENTERO en la copia de defensa (`C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG`):
  el controlador IA ahora se llama `controlador_propio` (el v1 MLP se eliminó de
  esa copia; clásicos: `basado_en_tasa`, `bba`, `bola`, `mpc_robusto`), y hay
  renombres tipo `player.py`→`reproductor.py`. El repo de GitHub conserva la
  versión completa anterior en inglés. El plan maestro (00) todavía habla en
  nomenclatura vieja (`rate_based`, `mpc_prudente v1/v2`, 6 controllers).
- **OJO EVIDENCIA**: el paquete final histórico es `20260624_182747_tfg_final`
  (360 sesiones, 6 controllers incluyendo v1) y existe un relanzamiento con 5
  controladores: `C:\Users\danie\Documents\TFG\20260806_212937_tfg_final` (la
  memoria `revision-consciente-agosto` dice que un gate cayó por desfase y se
  relanzó). Hay que VERIFICAR cuál es el paquete vigente ANTES de escribir el
  cap 6.
- **Bibliografía y normativa CERRADAS** (hilo de bibliografía, 10/08): normativa
  ETSIIT leída de los PDF oficiales (no impone estilo de citas; su rúbrica
  puntúa "fuentes adecuadas/fiables/variadas/suficientes" y el "uso adecuado de
  bibliografía" puede suspender si es muy deficiente); memoria ≤100 páginas,
  castellano, títulos de papers en inglés.

DATOS FIJOS NUEVOS:

- **Tutor: Juan José Ramos Muñoz** — además primer autor de
  `ramosMunoz2014mobileYoutube` y coautor de `ameigeiras2012youtubeTraffic`,
  los "trabajos locales" del cap 1-2 (hay un párrafo en español ya redactado en
  `docs/contexto rama original/0_field_map/local_streaming_source_evidence.md`,
  líneas 103-105). Va en la portada (`\myProf`).
- **Plantilla LaTeX**: la oficial del grado, ya montada en Prism con logos y mi
  nombre (copia local: `C:\Users\danie\Documents\TFG\Plantilla_TFG_latex`).
  El ZIP oficial NO trae `miunsrturl.bst` → al activar la bibliografía:
  `\bibliographystyle{unsrt}` y copiar `docs/memoria/bibliografia.bib` como
  `bibliografia/bibliografia.bib` del proyecto Prism.
- **NotebookLM está VACÍO** todavía.

EL ENCARGO (modo de trabajo, innegociable):

Guíame PASO A PASO, MILÍMETRO A MILÍMETRO, en la construcción de la memoria:
cada apartado, cada figura, cada tabla, cada cita, cada título y cada número.
Empezamos por el **Cap 4** y seguimos el orden del plan maestro §4
(4→5→6→2→3→1→7; bibliografía y anexos en paralelo). En cada turno trabajamos
UN apartado (p. ej. 4.1) y me entregas el paquete completo:

(a) **Alcance**: qué cuenta ese apartado y qué NO (para no pisar otros).
(b) **BORRADOR COMPLETO** del texto en español, estilo impersonal, frases
    cortas, calidad académica alta, listo para que yo lo mastique y lo
    reescriba con mis palabras (regla del tutor: si no lo mastico, no lo
    defiendo; en la memoria no queda NINGÚN rastro de IA). Sin recortarte:
    la longitud que el apartado necesite.
(c) **FIGURAS**: las generas TÚ como fichero editable (SVG, o TikZ si encaja
    mejor en LaTeX) con el contenido técnico EXACTO sacado del repo, más pie
    de figura numerado y el punto del texto donde se referencia. NADA de IA
    generativa de imágenes para diagramas técnicos (texto corrupto, no
    editable, no reproducible, y huele a IA). Las gráficas de resultados salen
    de los plots reales de Phase 6; el Gantt, del `git log`.
(d) **TABLAS** con contenido real extraído del repo (nada inventado).
(e) **CITAS**: exactamente las de `bibliografia.bib` con su clave
    (`\cite{...}`), solo las que tocan en ese apartado (columna [B] del plan
    maestro + secciones 2.x de 02_BIBLIOGRAFIA_DEFINITIVA). Ni una referencia
    que no esté en el `.bib`.
(f) **Checklist de cierre** del apartado + actualización del checklist §9 del
    plan maestro (00) para que el progreso quede versionado.

PRIMER TURNO (antes de redactar nada, en este orden):

1. Verifica el paquete de evidencia vigente (20260624 con 6 vs 20260806 con 5)
   y dime el impacto exacto en el cap 6 (si el vigente es el de 5, la ablación
   v1↔v2 pasa a resultados negativos del cap 7.5/anexo — propón el ajuste del
   plan maestro).
2. Fija la DECISIÓN DE TERMINOLOGÍA de toda la memoria (nomenclatura
   castellana nueva vs nombres del plan viejo) con una tabla de
   correspondencias, y aplícala de forma consistente en todo lo que redactes.
3. Dame la LISTA EXACTA de PDFs que subo a cada notebook de NotebookLM
   (NB_estado_del_arte / NB_cliente_dash / NB_ia_riesgo), con la ruta de cada
   fichero dentro de `C:\Users\danie\Documents\TFG\literatura\` — una sola
   copia por paper (duplicados cazados en 01 §K y 02 §4) y solo fuentes de la
   lista ganadora (02 §2). Recuérdame el prompt base de NotebookLM del plan
   maestro §3 adaptado al cap 2.
4. Dame el plan de sesión del Cap 4: secuencia de apartados, qué figura/tabla
   cae en cada uno (F1-F4, T5-T7 del plan maestro) y qué material del repo usas
   de fuente en cada caso.

REGLAS DE ESTILO (plan maestro §2, repásalas y aplícalas SIEMPRE): impersonal;
una idea por frase; cada capítulo abre con 2-3 líneas de contexto y cierra con
resumen; siglas definidas en la primera aparición; toda figura/tabla numerada,
con pie y referenciada; títulos de papers en inglés; cero claims de mejora sin
gates (el resultado es: mejor QoE media, empate estadístico con Robust MPC,
menos rebuffering); cero muletillas de IA; terminología consistente con el
código; ≤100 páginas.

Reparto de herramientas (no lo mezcles): TÚ = arquitecto + todos los capítulos
técnicos + figuras + tablas + coherencia global. NotebookLM = solo cap 2 /
justificaciones con cita fiel a los PDFs subidos. Prism = solo maquetar texto
ya masticado (no se redacta allí de cero).
