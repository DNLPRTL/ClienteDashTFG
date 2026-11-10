# Notas de la conversión de los Word de Daniel al formato de la biblia (no van a la memoria) — 10/11/2026

Petición de Daniel: pasar su capítulo 4 y sus apartados 5.1–5.2 al formato de la plantilla **sin cambiar ni una
palabra de su redacción** (para que ningún detector de IA toque su texto), sin aplicar las revisiones de contenido
C1–C32 y D/E de `revision_cap4_contenido_20261109.md` y `revision_cap5_1_5_2_contenido_20261109.md`, que él
aplicará a mano después.

Entregables (generados por `docs/memoria/apoyo/convertir_word_daniel.py`, que lee sus Word de
`G:\Otros ordenadores\Mi portátil\backup memo\` en solo lectura):

- `docs/memoria/borradores_docx/cap4_diseno_daniel.docx` (25 páginas, 10 272 palabras, 6 figuras, 7 tablas, 19
  elementos de lista, 17 citas).
- `docs/memoria/borradores_docx/cap5_1_2_daniel.docx` (9 páginas, 4034 palabras, 1 figura, 2 tablas, 13 citas).

## Garantía de texto intacto

El script compara, al final, la secuencia completa de palabras (`\w+`) del original con la del documento generado y
falla si difieren en una sola. Pasa en los dos documentos. Las únicas diferencias admitidas, todas de marcado y no de
redacción, son las que se quitan del original antes de comparar: los marcadores «[FIGURA …]», «[TABLA …]» y
«Fichero: `figuras/…`», el prefijo «Pie: » de los pies, la palabra «Capítulo» delante de los títulos de nivel 2
(«Capítulo 4.2. …» → «4.2. …», que es la numeración de la biblia) y la palabra «cite» de las citas LaTeX
(`\cite{clave}` → `[clave]`, la convención de los borradores).

## Formato aplicado (sin tocar palabras)

| Qué | Cap 4 | 5.1–5.2 |
|---|---|---|
| Títulos de texto → estilos Capítulo / nivel 2 | 9 | 3 |
| Marcadores de maquetación eliminados | 19 | 4 |
| Prefijo «Pie: » eliminado | 10 | 3 |
| Pies partidos en varios párrafos, unidos (Figuras 4.4 y 4.5) | 6 líneas | 0 |
| Imágenes incrustadas recolocadas con su pie (estilo Figura) | 6 | 1 (la Figura 5.1 no estaba incrustada: se toma `figuras/fig_5_1_emulacion_descarga.jpeg`) |
| Tablas de Word reconstruidas con el estilo de la plantilla | 7 | 0 |
| Tablas escritas en markdown (`\| a \| b \|`) → tablas de Word | 0 | 2 |
| Acentos graves y ‘’…’’ → cursiva (identificadores y ficheros) | 41 | 23 |
| `**x**` → negrita real (entradillas de párrafo) | 0 | 12 |
| `\cite{clave}` → `[clave]` | 17 | 13 |
| Listas: numerada (requisitos) y de viñetas, con el tipo original | 19 ítems | 0 |
| Párrafos vacíos y espacios o tabuladores de los extremos eliminados | 97 | 19 |

Las citas de Daniel estaban escritas con la sintaxis de LaTeX y por eso la primera pasada del generador de la
bibliografía (que buscaba corchetes) contó cero citas en sus Word. Ahora el generador lee los dos docx convertidos (en
su posición: cap 4 tras el cap 3; 5.1–5.2 antes del 5.3) y entiende también `\cite{}` por si vuelve a usarla. Las 30
claves que cita están todas en el .bib; se incorporan a la numeración (y varias entradas que estaban sin citar, como
pythonDocs, las RFC 9110 y 9112, mahimahi y digregorio2026mlLoading, ya se imprimen).

## Avisos del comprobador que son de Daniel (NO se han tocado)

- Pie de la Figura 4.2 sin punto final.
- Tres tics de la lista de la biblia en su prosa: «cabe destacar», «dicho de otro modo», «es importante destacar».
- Menciones «figura 4.1», «tabla 4.1» en minúscula (la biblia unifica a «Figura 4.1», «Tabla 4.1»); por eso el
  comprobador dice que las figuras y tablas «no se anuncian antes del pie».
- Pie de la Tabla 5.1: igual, la mención en el texto va en minúscula.
- Decimales con punto, si los hay, y demás reglas de estilo se verán en la pasada de coherencia.

## Decisiones

- Las imágenes del cap 4 se toman tal cual están incrustadas en su Word (PNG), no de los SVG del repo, para
  reproducir lo que él puso. Si prefiere los PNG de mayor calidad del repo, basta con cambiar el script (los nombres
  de fichero están en sus marcadores).
- Las cabeceras de las tablas quedan en negrita y sombreadas por el estilo de la plantilla (en su Word no lo
  estaban): es formato.
- El ancho de las columnas es uniforme (el estilo por defecto de `Borrador.tabla`); si alguna tabla queda mal
  repartida se ajusta a mano al maquetar.
- Nada de lo anterior toca sus ficheros: los Word de G: y los `.md`, `.svg` y `.jpeg` sin commitear del repo siguen
  intactos.
