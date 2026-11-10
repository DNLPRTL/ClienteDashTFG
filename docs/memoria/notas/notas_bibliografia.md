# Notas de la bibliografía impresa (no van a la memoria) — 10/11/2026

Entregable: `docs/memoria/borradores_docx/bibliografia.docx` (78 entradas, comprobador sin avisos) y
`docs/memoria/apoyo/bibliografia_numeracion.json` (clave → número, primera aparición de cada clave, citas por
documento, claves no citadas, texto impreso de cada entrada). Generado por `docs/memoria/apoyo/generar_bibliografia.py`
(Python 3.11 basta; no importa el código entregado).

## Cómo se numera

- Orden de primera aparición en la memoria (biblia §4: IEEE, `unsrt`), leyendo los .docx en el orden de la memoria:
  resumen, cap 1, cap 2 (3 docx), cap 3, **cap 4 y 5.1–5.2 de Daniel (sus Word convertidos al formato por
  `apoyo/convertir_word_daniel.py`, ver `notas_conversion_word_daniel.md`)**, 5.3–5.8, cap 6 (7 docx), cap 7, anexos.
  Las citas se buscan como `[clave]`, `[clave1], [clave2]` o `\cite{clave}` / `\cite{a,b}` en párrafos y tablas en
  el orden real del cuerpo (párrafos y tablas intercalados).
- Daniel cita con la sintaxis de LaTeX (`\cite{iso23009_1_2022}`): la primera pasada, que solo buscaba corchetes,
  contó cero citas en sus Word; corregido el 10/11. Sus 30 claves (17 citas en el cap 4, 13 en el 5.1–5.2) están
  todas en el .bib. Si cambia sus citas, basta con volver a ejecutar el conversor y después este script.
- Solo se imprime lo citado: 78 de las 96 entradas. Las 18 no citadas no se imprimen (biblia: «entradas nunca
  citadas» es error del corpus del tutor): bentaleb2024ahaggar, huang2023deepbuffer, huang2026eastream,
  hussein2026mambra, kingma2015adam, li2024metaabr, luo2025sabr, mao2020abrl, patel2023plume, rfc9111,
  sentosa2025cellreplay, wang2026nmoeabr, wei2019traceBasedEmulation, yi2025airl, yi2025fortuna, yin2024ant,
  zhang2025beta, zhou2022adaptiveStreamingQualityAssessment. Son descartes del cap 2 (más la RFC 9111 de caché y
  Adam, ver pendientes).
- Citas por documento (ocurrencias de clave): cap 1 21, cap 2 65 (13 + 28 + 24), cap 4 19, 5.1–5.2 15, 5.3 6, 5.4 1,
  5.5 19, 5.6 8, 6.1 7, 6.2 6, 6.7 1, cap 7 5, anexos 24; resumen, cap 3, 5.7, 5.8, 6.3–6.6: 0.

## Citas añadidas el 10/11 para no dejar fuentes sin citar

- Anexo C, Tabla C.1: la fuente de cada conjunto de trazas en la columna «Conjunto» (FCC, GAViST5G, Gante,
  Lumos5G, Noruega, NYU-METS con su paper y su repositorio, Oboe, Puffer con su paper y su archivo de datos, Roma,
  UCC 4G y UCC 5G).
- Anexo B: requests, PyYAML, PyGObject, ffmpeg, GPAC y Docker donde se nombran (B.1, B.2, B.7).
- 6.1.4: VirtualBox, WSL y ROCm (`generar_cap6_1.py` regenerado; comprobador sin avisos).

## Formato de cada entrada (unsrt con conectores en castellano)

- Autores con iniciales y apellido, «y» antes del último; organizaciones tal cual (`{...}` del .bib).
- Artículo: `Autores. Título. //Revista//, volumen(número):páginas, año. DOI: …`
- Congreso: `Autores. Título. En //Congreso//, páginas a–b. Editorial, año. DOI: …` (URL si no hay DOI: USENIX, NeurIPS).
- Libro: `Autores. //Título//. Serie, n.º N. Editorial, Ciudad, año. ISBN …`
- Norma (techreport): `Organismo. Título. International Standard, N.ª edición. Organismo, Ciudad, año. [En línea]…`
- Web (misc): `Autor. Título. Texto de howpublished y de la nota sin la fecha de acceso. Año. [En línea]. Disponible
  en: URL. [Último acceso: mes de año].` (biblia §4); arXiv y RFC llevan su identificador.
- Las notas del .bib se imprimen solo si son de la propia referencia (webs) o apuntan al dataset asociado (empiezan
  por «Dataset»); las notas de trabajo (p. ej. la de Comyco sobre el PDF, la de digregorio sobre `weights_only`) no.
- LaTeX a texto: acentos (`{\'o}`, `{\ss}`, `{\c{C}}`, `{\u{g}}`, `{\aa}`…), `\&`, `\_`, `\texttt{}`, `---` → « – »,
  `--` → «–», `\url{}`; la virgulilla de las URL se conserva; si la URL es el propio DOI no se repite.
- Comprobaciones por programa: ninguna URL con parámetros de seguimiento; meses de acceso en castellano; año en todo
  lo que no sea web; ninguna cita fuera del .bib en ningún docx.
- Estilo de párrafo propio «Bibliografia» (sangría francesa 1 cm, 11 pt, alineado a la izquierda): el comprobador lo
  excluye de la regla de la coma decimal, porque los DOI llevan puntos.

## Pendiente de Daniel

- El 5.7 dice «AdamW»; el .bib solo tiene Adam (kingma2015adam). Citar Adam para AdamW sería impreciso; si quiere
  cita, hace falta la referencia nueva de Loshchilov y Hutter (2019), que requiere su permiso.
- Al maquetar: convertir `[clave]` en `[n]` con `bibliografia_numeracion.json` (o con BibTeX `unsrt` si la memoria
  final va en LaTeX: el .bib ya está preparado y el orden coincidirá si los capítulos se compilan en este orden).
- Para la pasada de coherencia: el 5.7 escribe «1 024 muestras» con espacio en un número de cuatro cifras; la biblia
  pone el separador a partir de cinco («1208», «35 032»).
