# Maquetación medida de los TFG de referencia (08/11/2026)

Medidas sacadas de los propios ficheros PDF con un script sin dependencias
(`/BaseFont`, `/MediaBox` y los operadores de texto `Tf`, `Tm`, `Tj`/`TJ` de
los flujos comprimidos). El tamaño de letra está ponderado por caracteres
pintados, así que el valor dominante es el del cuerpo de texto. Los metadatos
`/Producer` y `/Creator` salen del propio PDF cuando no están comprimidos.

| TFG | Año | Herramienta | Papel | Cuerpo (% caracteres) | Otros tamaños | Familia tipográfica |
|---|---|---|---|---|---|---|
| Tutor: Cañizares Cancho | 2025 | Microsoft Word 2019 | A4 | 12 pt (94,5 %) | 9 pt pies y tablas (3 %), 18 pt títulos | Arial (regular, negrita, cursiva); Courier New para código; Cambria Math |
| Tutor: Marín Munuera | 2024 | LaTeX, plantilla de la ETSIIT | A4 | 11 pt (79,5 %) | 10 y 8 pt en los apéndices de código (14 %), 14,5 pt, 25 pt | Computer Modern (CMR, CMBX, CMTI, CMTT para código); SFRM en la portada |
| Tutor: González Callejas | 2017 | pdflatex, plantilla de la ETSIIT | A4 | 11 pt (95 %) | 9 pt (3 %), 12, 14,5, 25 pt | Computer Modern; Minion Pro en la portada |
| Sánchez Martínez | reciente | LaTeX (PDF pasado por iLovePDF) | A4 | 11 pt (92 %) | 10 pt (5 %), 8 pt | Computer Modern |
| Romero Espigares | reciente | LaTeX | A4 | 10 pt (60 %) y 9 pt (27 %) | 5–7,5 pt en figuras | Latin Modern; Times New Roman y Verdana dentro de figuras |
| TFG_FS | reciente | pdflatex, plantilla de la ETSIIT | A4 | 11 pt (97 %) | 17,5 pt, 14,5 pt, 25 pt | Latin Modern; Tahoma, Arial y Trebuchet dentro de figuras |
| Hernández Manrique | reciente | LaTeX (páginas sueltas añadidas) | A4 | 11 pt (97 %) | 12, 14,5, 25 pt | Computer Modern; Liberation en las páginas añadidas |

Lectura:

- **Seis de los siete** están hechos con LaTeX y la plantilla de la ETSIIT
  (clase a 11 pt, Computer Modern o Latin Modern, A4). La plantilla fija los
  títulos de capítulo a unos 25 pt y los de sección a unos 14,5 pt.
- El **único en Word** es el del tutor de 2025: Arial 12 pt, pies a 9 pt,
  títulos a 18 pt. Primer carácter de línea a 25 mm del borde izquierdo
  (margen de 2,5 cm), texto hasta 23 mm del borde inferior.
- El de Romero usa 10 pt porque el cuerpo lleva mucho texto pequeño en tablas
  y listados; no es el patrón.

Posiciones en los PDF de LaTeX: no se pudieron medir (usan `Td`, no `Tm`),
así que los márgenes de la plantilla se toman de la propia clase (la plantilla
de la ETSIIT, en `docs/memoria/apoyo/` cuando Daniel la pase) y no de aquí.

Borrador de Daniel (`Borrador Capitulo 4 Diseño.docx`, Word): A4; márgenes
superior e inferior 2,5 cm, izquierdo y derecho 3 cm; letra del tema (minor)
a 12 pt; interlineado 1,16 con 8 pt tras párrafo; títulos con el estilo por
defecto de Word (color azul 0F4761, 20/16/14 pt). Pies con dos puntos:
«Figura 4.2: …», «Tabla 4.1: …». Esto se alinea con la biblia en
`docs/memoria/05_BIBLIA_FORMATO_TFG_UGR.md`.
