# Notas de la pasada de coherencia (no van a la memoria) — 10/11/2026

Herramienta: `docs/memoria/apoyo/comprobar_coherencia.py` (Python 3.11 basta). Lee los 23 borradores .docx en el orden
de la memoria (los de Claude y los dos de Daniel convertidos) y comprueba numeración de objetos, remisiones, números y
unidades, siglas, citas y, por documento, el comprobador de la biblia. Termina con código 1 si hay algún hallazgo no
informativo. Se repite cada vez que cambie un borrador.

## Resultado del 10/11

- 18 figuras, 49 tablas, 6 listados y 18 ecuaciones: sin duplicados, sin huecos por capítulo, toda referencia
  «Figura/Tabla/Listado n.m» apunta a un objeto definido y todo objeto se referencia al menos una vez.
- Remisiones «apartado n.m», «capítulo n», «anexo X», «punto n.m», «sección n.m»: todas a títulos existentes (incluidas
  las del cap 4 y 5.1–5.2 de Daniel hacia el 5.3–5.7 y el cap 6).
- Separador de miles: corregido en los generadores del cap 3 (`eur`), 5.6 y 5.7 (`miles`), que separaban desde cuatro
  cifras («4 379», «1 024», «7 556,25 €»); ahora solo desde cinco, como la biblia y el resto de capítulos (regenerados;
  sin avisos). Los enteros largos que quedan sin separador son identificadores (sesión, hash) o números de norma,
  modelo o timescale, no cantidades.
- Unidades: la Tabla C.2 del anexo mostraba los nombres de carpeta de los vídeos («Paseo Almunecar 10min 30fps»); ahora
  nombres legibles («Paseo de Almuñécar, 10 min, 30 fps»). Ninguna unidad pegada al número en el resto. «kbps»/«Mbps»
  no aparecen (todo «kbit/s», «Mbit/s»).
- Siglas: 44 de las 45 del diccionario se usan y van en `borradores_docx/acronimos.docx` (`apoyo/generar_acronimos.py`:
  sigla en negrita, expansión inglesa en cursiva y traducción, solo las usadas, biblia §3.9). Fuera del diccionario
  solo quedan nombres propios y unidades (lista NO_SIGLAS). La expansión en el primer uso de cada capítulo no se ha
  forzado: la biblia la pide «si hace falta» y cuenta como error repetirla en cada uso; la lista de acrónimos cubre el
  resto.
- Citas: las 79 claves citadas están en el .bib; 17 entradas sin citar no se imprimen (`notas_bibliografia.md`).
  `apoyo/numerar_citas.py` escribe en `borradores_docx/numerado/` una copia de cada borrador con «[clave]» → «[n]»
  (199 citas convertidas, formato de los runs conservado, incluido el rojo); esa carpeta no se versiona.
- Comprobador de la biblia por documento: solo quedan 4 avisos, todos de redacción de Daniel en el cap 4 («cabe
  destacar», «dicho de otro modo», «es importante destacar», y la Figura 4.5 sin anunciar en el texto antes del pie).

## Terminología (informe, sin cambios)

- «bitrate» (47, sobre todo cap 6 y resumen) convive con «tasa binaria» (7, caps 1, 2 y 4): el primero es el término
  de la fórmula de QoE; se deja.
- «stall» (10) solo en el cap 4 y el 5.1–5.2 de Daniel, junto a «parada» (134) en toda la memoria; es su redacción.
- «MPC robusto» uniforme (113); «RobustMPC»/«Robust MPC» no aparecen en el texto.
- «Paseo de Almuñécar» con tilde en todos los sitios tras el ajuste del anexo.

## Pendiente de Daniel (de esta pasada)

- Reformular lo rojo del cap 4 y del 5.1–5.2, los tres tics y anunciar la Figura 4.5 antes de que aparezca; después,
  `python docs/memoria/apoyo/convertir_word_daniel.py` fallará si los textos originales de la tabla de cambios ya no
  existen: entonces se borran de `cambios_contenido_daniel.py` los ya incorporados (o se regenera con `--texto-intacto`).
- Textos de las Figuras 4.2, 4.5, 4.6 y 5.1 (SVG suyos; lista en `notas_conversion_word_daniel.md`).
- Al maquetar: usar los docx de `numerado/` (citas con número) o BibTeX `unsrt` si la memoria final va en LaTeX.
