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

## Ajustes tipográficos autorizados (10/11, segunda pasada)

Daniel aclaró que sí podía tocar caracteres y formato, no la gramática ni la elección de palabras. El script aplica
ahora, además del formato, estos ajustes de la biblia, cada uno registrado con su contexto (lista completa abajo):
mayúscula en «Figura n.m» y «Tabla n.m» en el texto; espacio sobrante antes de coma, punto y coma o dos puntos;
espacio tras dos puntos («(60 s):antes»); dobles espacios; punto final del pie de la Figura 4.2; «video» → «vídeo»
(él mismo escribe «vídeo» 15 veces); «Dash» → «DASH»; la errata «amuestra»; las tildes de «cálculo estimado» y «está
diseñada»; y las entradillas de las viñetas en negrita (9 ítems con la forma «Nombre: texto»). La comparación de
palabras se hace sobre el texto ya ajustado, así que sigue garantizando que no hay ningún otro cambio.

NO se han tocado, por ser redacción y no tipografía (los decide Daniel): «se haya definida» y «se haya separado»
(«halla»), «divido en» («dividido»), «haya redactado» («halla»), los tres tics «cabe destacar», «dicho de otro modo»
y «es importante destacar», y la Figura 4.5, que el texto no anuncia antes del pie (el comprobador lo avisa).

Lista de los 42 ajustes aplicados (regla :: contexto):

- «vídeo» con tilde (como en el resto del texto) :: scargar los segmentos de video que aloja el servidor y
- sigla DASH :: ucir realmente contenido Dash servido a través de HTTP
- mayúscula en Figura/Tabla :: En la figura 4.1 se presenta la arquit
- mayúscula en Figura/Tabla :: La tabla 4.1 es un resumen de los
- mayúscula en Figura/Tabla :: a sesión se resume en la figura 4.2. Una vez se ha cargad
- tilde «cálculo» :: a descarga más reciente, calculo estimado del ancho de banda) y se
- «vídeo» con tilde (como en el resto del texto) :: ite por cada segmento de video; los eventos que suceden
- espacio sobrante antes de signo :: te de cara al controlador : el reproductor es ignora
- «vídeo» con tilde (como en el resto del texto) ::  a la inicialización del video y los segmentos de este)
- «vídeo» con tilde (como en el resto del texto) :: gmentos que conforman el video, su duración y, si fuera
- mayúscula en Figura/Tabla :: en el experimento, en la tabla 4.2 se detalla que inform
- espacio sobrante antes de signo ::  para todos los segmentos , de manera que, de nuevo,
- «vídeo» con tilde (como en el resto del texto) :: s modelado por tiempo de video almacenado: lo que nos a
- espacio tras dos puntos :: Tope de ocupación (60 s):antes de que dé lugar la
- mayúscula en Figura/Tabla :: nto de configuración; la tabla 4.3 que se muestra a cont
- mayúscula en Figura/Tabla :: pítulo 6. En cuanto a la figura 4.4 esta resume el diseño
- mayúscula en Figura/Tabla :: rarse en cuatro bloques (tabla 4.5): el estado en el buf
- espacio sobrante antes de signo :: nos de tasa y no de nivel ; el otro beneficio es que
- espacio sobrante antes de signo :: lásico a modo de respaldo , el cual recibe el peso d
- mayúscula en Figura/Tabla :: ues de orden invariable (tabla 4.6): el identificador de
- espacio sobrante antes de signo :: ilidad de la red reciente , buffer en número de segm
- espacio sobrante antes de signo :: en el que los bits llegan , por otra parte, tenemos
- doble espacio :: banda del que se dispone)  se establecen las condici
- tilde «está» :: La emulación esta diseñada de tal manera que se apl
- espacio sobrante antes de signo ::  esta información del VBR , por lo tanto, solo forma
- «vídeo» con tilde (como en el resto del texto) :: ara funcionar bien en un video en concreto, dado que el
- espacio sobrante antes de signo ::  pequeña (0,4 por ciento) , por consiguiente, no exi
- mayúscula en Figura/Tabla :: La figura 4.6 resumen los dos aspec
- espacio sobrante antes de signo :: as únicas que se utilizan , se escogen de manera bal
- doble espacio :: os con los controladores.  La expresión concreta y l
- mayúscula en Figura/Tabla :: validez del experimento (tabla 4.7). En el caso de que t
- espacio sobrante antes de signo :: n el análisis estadístico , las sesiones de un contr
- punto final del pie :: …ra asíncrona en el fichero de telemetría → .
- doble espacio :: ema de Windows para Linux  (WSL) para poder hacer us
- mayúscula en Figura/Tabla :: ferentes entornos. En la tabla 5.1 se muestra un resumen
- espacio sobrante antes de signo ::  de datos (`dataclasses`) , especificando que tipo d
- espacio sobrante antes de signo :: 5.7, en su versión 2.9.1) , también es empleada una
- mayúscula en Figura/Tabla :: tulo 4 y resumidos en la tabla 4.1. Dentro de `entrenami
- espacio sobrante antes de signo :: pción de emulación de red , el descargador se ve cub
- espacio sobrante antes de signo ::  entregado al controlador , ya podría decidir el niv
- espacio sobrante antes de signo ::  fichero de manera remota , a través de una petición
- errata «amuestra» :: ventana de traza muestra amuestra, con la última usada sol

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
