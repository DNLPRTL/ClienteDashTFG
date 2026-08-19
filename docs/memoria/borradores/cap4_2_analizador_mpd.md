# Borrador 4.2 — Diseño del analizador del MPD

> BORRADOR para masticar y reescribir (12/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/analizador_mpd/` del entregable (leído entero 12/08) +
> `docs/defensa/componentes_experimento.md` (MPD real verificado en el servidor).

---

### 4.2. Analizador del manifiesto (MPD)

El punto de partida de toda sesión es el manifiesto MPD (*Media Presentation
Description*), el documento XML que describe el contenido disponible
\cite{iso23009_1_2022}. El cliente necesita extraer de él tres cosas: la
escalera de calidades (qué representaciones existen y a qué tasa binaria), la
forma de localizar cada segmento (las URL del segmento de inicialización y de
los segmentos de vídeo), y la información temporal (duración de cada segmento
y del contenido completo). El analizador de MPD es el módulo que resuelve esta
tarea y aísla al resto del cliente de los detalles del XML.

El diseño sigue la estructura jerárquica del estándar: un MPD contiene uno o
varios periodos (`Period`); cada periodo agrupa conjuntos de adaptación
(`AdaptationSet`), uno por tipo de contenido; y cada conjunto contiene las
representaciones (`Representation`), que son las versiones alternativas del
mismo contenido a distintas tasas binarias \cite{stockhammer2011dash}. De cada
representación, el analizador extrae los atributos que el cliente necesita
(identificador, tasa binaria nominal, resolución, códec y tasa de imágenes) y
construye la lista completa de segmentos.

La parte menos trivial del diseño es el direccionamiento de los segmentos,
porque el estándar admite varios esquemas. El analizador soporta los tres
habituales en manifiestos estáticos:

- **Lista explícita (`SegmentList`):** el MPD enumera la URL de cada segmento
  y la del segmento de inicialización. El analizador se limita a recorrer la
  lista.
- **Plantilla (`SegmentTemplate`):** el MPD define una plantilla de URL con
  variables (`$RepresentationID$`, `$Number$`, `$Bandwidth$`) y los parámetros
  temporales (`timescale`, `duration`, `startNumber`). El analizador calcula
  el número de segmentos a partir de la duración del periodo y expande la
  plantilla para generar todas las URL. Es el esquema del contenido usado en
  este trabajo: los manifiestos generados para el experimento emplean una
  plantilla con `$Bandwidth$` y `$Number$`; en el contenido a 30 fps,
  `timescale` 15360 y `duration` 61440, es decir, segmentos de 4,000 segundos
  exactos (las variantes a 60 fps usan una escala de 60000 con idéntico
  resultado).
- **Fichero único con índice (`SegmentBase`):** toda la representación está en
  un solo fichero y el MPD indica el rango de bytes de su índice (`sidx`). El
  analizador descarga solo ese rango, interpreta el índice y deriva el rango
  de bytes y la duración de cada subsegmento. Este esquema permite reproducir
  también contenido no segmentado en ficheros separados.

Dos aspectos complementarios cierran el diseño. Primero, la resolución de
direcciones: las URL del MPD pueden ser relativas, de modo que el analizador
las convierte en absolutas a partir del elemento `BaseURL` o, en su ausencia,
de la URL del propio manifiesto, según las reglas generales de resolución de
referencias \cite{rfc3986}. Segundo, la información temporal: las duraciones
globales del MPD se expresan en formato de duración ISO 8601 (en el contenido
principal del experimento, `PT0H10M0.100S`: diez minutos y una décima de
segundo) y el analizador las convierte a segundos; cuando el esquema de
direccionamiento no da la duración exacta de cada segmento, se reparte la
duración del periodo de forma uniforme, ajustando el último segmento al
tiempo restante.

El resultado del análisis es una estructura de datos neutra: una lista de
periodos, cada uno con sus conjuntos de adaptación y, dentro, las
representaciones con sus atributos, la URL de inicialización, la lista de URL
de segmentos, sus duraciones y, si procede, los rangos de bytes. El
reproductor consume esta estructura, ordena las representaciones por tasa
binaria creciente para formar la escalera de niveles y no vuelve a tocar el
XML en toda la sesión. Esta frontera mantiene el análisis del manifiesto como
una pieza sustituible: la interfaz del analizador se reduce a dos operaciones
(cargar un MPD y devolver los periodos), definida en una clase base de la que
hereda la implementación DASH concreta.

La Figura 4.3 resume el proceso con el manifiesto real del experimento, y la
Tabla 4.2 detalla qué información del MPD se extrae y para qué la usa el
cliente.

**[FIGURA 4.3 — Del MPD a las estructuras del cliente. Fichero:
`figuras/fig_4_3_analizador_mpd.svg`]**
*Pie: Figura 4.3: Análisis del manifiesto: de la jerarquía XML del MPD (con
los valores reales del contenido del experimento) a las estructuras que
consume el reproductor.*

**[TABLA 4.2 — Información del MPD utilizada por el cliente]**

| Elemento / atributo del MPD | Información | Uso en el cliente |
|---|---|---|
| `MPD@type`, `@profiles` | Manifiesto estático, perfil de interoperabilidad | Sesión de vídeo bajo demanda |
| `MPD@mediaPresentationDuration` | Duración total del contenido | Número de segmentos y fin de la sesión |
| `Representation@bandwidth` | Tasa binaria nominal | Escalera de niveles; entrada de la decisión ABR |
| `@width`, `@height`, `@codecs`, `@frameRate` | Características de cada representación | Registro y telemetría |
| `SegmentTemplate@media` + `$Number$`, `$Bandwidth$` | Plantilla de URL de segmentos | Generación de las URL de descarga |
| `SegmentTemplate@initialization` | URL del segmento de inicialización | Arranque del descodificador |
| `SegmentTemplate@timescale`, `@duration`, `@startNumber` | Duración de segmento y numeración | Planificación temporal y gestión del buffer |
| `SegmentList` / `SegmentURL@media` | Lista explícita de segmentos | Alternativa de direccionamiento |
| `SegmentBase@indexRange` + caja `sidx` | Índice de subsegmentos | Rangos de bytes y duraciones por subsegmento |
| `BaseURL` | Base de resolución de direcciones | Conversión de URL relativas en absolutas |

*Pie: Tabla 4.2: Información extraída del MPD y uso que el cliente hace de
cada elemento.*

*(El apartado 4.3 continúa con el diseño de la descarga y la gestión del
buffer.)*

---

### Notas para Daniel (no van a la memoria)

- Citas usadas: `\cite{iso23009_1_2022}` (el MPD y su jerarquía),
  `\cite{stockhammer2011dash}` (principios de diseño DASH),
  `\cite{rfc3986}` (resolución de URL relativas). Las tres están en el
  plan y en la lista ganadora.
- COMPLETADO tras el scp (12/08): todos los valores del apartado están ahora
  verificados contra los MPD reales de `05_contenido_dash`. Paseo 30fps:
  `mediaPresentationDuration="PT0H10M0.100S"`, timescale 15360 / duration
  61440; **el 60fps usa timescale 60000** (mismo 4,000 s); Blender 10min dura
  en realidad `PT0H10M34.600S` (~10,6 min → 159 segmentos). En disco, Paseo
  30fps tiene **151 segmentos** por representación: 150 de 4,000 s + 1
  residual de 0,1 s (el cliente reproduce las 150 medias completas; en la
  evaluación además se corta a 30 segmentos por sesión). Si el tribunal
  pregunta por el "151": esa es la explicación.
- El soporte de `SegmentList`/`SegmentBase` existe de verdad en el código (no
  es adorno): da robustez al cliente ante manifiestos de otras herramientas.
  En la defensa: "el contenido del experimento usa SegmentTemplate; los otros
  dos esquemas se soportan para no atar el cliente a un empaquetador".
- El parseo binario de la caja `sidx` es implementación → va en el cap 5
  (aquí solo se menciona "interpreta el índice").
- Frontera con 2.2: allí se explicará DASH didácticamente (qué es un MPD, por
  qué segmentar); aquí se da por introducido y se va al diseño. Cuando exista
  el cap 2, revisa que no haya duplicado.
- Longitud: ~800 palabras. La tabla puede migrar a dos columnas si en LaTeX
  queda ancha (elemento → uso, fundiendo la columna central).
