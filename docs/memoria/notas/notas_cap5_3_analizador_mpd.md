# Notas del 5.3 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap5_3_analizador_mpd.docx` (1201 palabras de cuerpo, 4
subapartados, 2 tablas, 1 ecuación, 5 citas, sin figura nueva). Generado por
`docs/memoria/apoyo/generar_cap5_3.py` con la plantilla `docs/memoria/plantilla/plantilla_memoria_ugr.docx`
(creada por `apoyo/memoria_docx.py` según la biblia §2). Comprobado con
`apoyo/comprobar_borrador_docx.py` (sin avisos) y renderizado con Word a PDF (4 páginas, sin solapes).

## Fuente de cada número

| Dato | Fuente |
|---|---|
| «unas trescientas líneas» | `core/analizador_mpd/dash.py` = 300 líneas; `base.py` = 8 |
| Tabla 5.3 entera (duración, timescale/duration, N, último segmento) | ejecución real de `ParserDash` sobre los 5 MPD de `05_contenido_dash` (el script la recalcula cada vez) |
| «segmentos en el servidor» (151, 150, 159, 159, 150) | `num_segmentos` de `perfiles_video/tamanos_segmentos/*.json` (sondeo HTTP del servidor) |
| 61440/15360 = 4,000 s | MPD a 30 fps; Paseo 60 fps usa 240000/60000 (también 4,000 s) |
| «startNumber 1 en todos» y «SegmentTemplate en el AdaptationSet» | comprobado en los 5 MPD |
| Tabla 5.4 (campos del sidx) | ISO 14496-12:2015 §8.16.3.2 (p. 121 del PDF) frente a `_parsear_sidx` del código: coinciden campo a campo |

## Citas verificadas contra el PDF o el documento original

- `iso23009_1_2022`: espacio de nombres `urn:mpeg:dash:schema:mpd:2011` en la tabla de identificadores
  de esquema (p. 27) y en el XSD (p. 31); identificadores `$Number$`, `$Bandwidth$`,
  `$RepresentationID$` (p. 91); `@startNumber` (p. 85); URL del segmento k con `$Number$` (p. 93,
  5.3.9.5.3); `@indexRange` (p. 83); `mediaPresentationDuration` de tipo `xs:duration` (p. 41).
- `iso14496_12_2015`: `SegmentIndexBox` §8.16.3.2 (p. 121): `reference_ID`, `timescale`,
  `earliest_presentation_time`/`first_offset` (32 o 64 bits según `version`), `reserved`,
  `reference_count`, y por entrada `reference_type(1)+referenced_size(31)`, `subsegment_duration(32)`
  y los 32 bits de SAP que el código salta.
- `rfc3986`: §5 «Reference Resolution» (5.1 base URI, 5.2 relative resolution).
- `pythonElementTree`, `pythonUrllibParse`: documentación oficial guardada en `biblioteca_final/03_...`.

## Preguntas probables del tribunal

1. **¿Por qué 150 segmentos si el servidor tiene 151?** `round(600,1·15360/61440) = round(150,025) = 150`.
   El fichero 151 dura 0,1 s. La sesión usa 30 segmentos, así que no afecta. Si hiciera falta el
   último, bastaría truncar hacia arriba en lugar de redondear; se dejó el redondeo porque un
   segmento de 0,1 s no aporta nada a la medida y GPAC lo genera por el residuo del vídeo original.
2. **¿Por qué no se usa una biblioteca externa de análisis de MPD?** Control de lo que se lee, cero
   dependencias y soporte acotado a los esquemas del contenido propio (plantillas con `$Number$` y
   `$Bandwidth$`). Si el tribunal pregunta por `SegmentTimeline`: no se soporta y se declara.
3. **¿El analizador toca la red?** Solo para bajar el MPD y, en el esquema `SegmentBase`, el rango del
   índice. En el experimento (plantillas) no descarga nada más que el MPD.
4. **¿Qué pasa con un MPD con audio?** El reproductor filtra los conjuntos de adaptación de vídeo
   (`type == video` o `mimeType video/*`); el contenido del proyecto se empaquetó sin audio.
5. **¿La expresión regular de duraciones es completa?** No: cubre `PT[H][M]S` con segundos
   fraccionarios, que es lo que escribe GPAC. Un `P1D` no lo leería. Declarado en el texto.

## Detalles que el texto no cuenta (para no quedar sin respuesta)

- La sustitución de variables de la plantilla es un reemplazo literal de cadenas; `$Number%05d$` no
  está soportado (los MPD propios usan `$Number$` a secas).
- Si falta `duration` en la plantilla, se asumen 30 segmentos (último recurso).
- `first_offset` del `sidx` se supone 0 (subsegmentos justo tras el índice), como empaqueta MP4Box.
- `url_absoluta` concatena base y ruta sin normalizar `../`; la base del MPD sí sale de `urljoin`.
- `base.py` conserva dos atributos sin uso (`niveles`, `listas_segmentos`): resto de la poda. Código
  congelado, no se toca.
- La lectura del MPD usa `requests.get` sin tiempo límite ni cabeceras especiales (solo se hace una
  vez por sesión).

## Addendum a la revisión del capítulo 4 (ojo, Daniel)

- **Figura 4.3**: el recuadro «6 niveles × (1 segmento de inicio + 151 segmentos de 4 s)» describe
  los ficheros del servidor, no lo que lista el analizador (150). No es falso, pero el 5.3 explica
  la diferencia; si quieres coherencia total, «151 ficheros de segmento en el servidor (el cliente
  lista 150)». Decisión tuya.
- En el 4.2 del Word dices «segmentos de 4,000 segundos precisos»: correcto, y el último de Blender
  dura 2,6 s (lo cuenta el 5.3).

## Qué se puede recortar

El párrafo de `SegmentList` (caso trivial) y la mitad del de límites. Mantener entero el cálculo
150/151 (promesa del 4.2) y el `sidx` (único sitio donde se explica).

## Pendiente que nace aquí

- Alinear la nota de `requestsDoc` en `bibliografia.bib` («Versión 2.22 en el cliente» → 2.32.4):
  hecho en este commit.
- Para los siguientes apartados con figura: hace falta un conversor SVG → PNG (no hay Inkscape ni
  rsvg en la máquina). Opción prevista: insertar el SVG en Word por COM y exportar, o instalar
  `cairosvg`. Se decide en el 5.4.
