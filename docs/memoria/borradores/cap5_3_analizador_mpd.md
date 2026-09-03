# Borrador 5.3 — Implementación del analizador del manifiesto

> BORRADOR para masticar y reescribir (03/09/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: entregable — `core/analizador_mpd/base.py` y
> `core/analizador_mpd/dash.py` leídos enteros (03/09) + MPD real de
> `05_contenido_dash` (Paseo 30 fps) + PDFs de ISO 23009-1 e ISO 14496-12
> (norma PDF-primero; pasajes en las notas).

---

### 5.3. Implementación del analizador del manifiesto

El apartado 4.2 fijó qué extrae el analizador del MPD y el contrato de salida
que entrega al reproductor. Este apartado describe cómo se implementa. El
analizador es un módulo compacto y sin estado compartido con el resto del
cliente; su única dependencia externa es la misma biblioteca HTTP que usa el
descargador.

**Lectura del XML y espacio de nombres.** El manifiesto se obtiene con una
petición HTTP (o de un fichero local, útil en pruebas) y se convierte en un
árbol con `ElementTree`. Todos los elementos del MPD pertenecen al espacio de
nombres del esquema del estándar, `urn:mpeg:dash:schema:mpd:2011`
\cite{iso23009_1_2022}, y `ElementTree` exige nombrarlo en cada búsqueda: el
analizador lo define como constante y lo antepone a cada etiqueta que busca.
El recorrido sigue la jerarquía del documento —atributos globales del MPD,
periodos, conjuntos de adaptación y representaciones— y todo atributo ausente
recibe un valor por defecto, de modo que un manifiesto incompleto degrada de
forma controlada en lugar de interrumpir el análisis.

**Duraciones.** Las duraciones del MPD llegan en el formato de duración de
ISO 8601; el contenido principal del experimento declara `PT0H10M0.100S`. El
analizador las convierte a segundos con una expresión regular que captura
horas, minutos y segundos fraccionarios. Cubre el subconjunto del formato que
emplean los manifiestos del proyecto; no pretende ser un intérprete general
del estándar de fechas.

**Resolución de direcciones.** La base de las URL es el elemento `BaseURL`
del manifiesto si existe; en su ausencia, el directorio de la URL del propio
MPD, derivado con la resolución estándar de referencias del apartado 4.2.
Las URL relativas de inicialización y de segmentos se resuelven contra esa
base. Una representación puede aportar además su propia base, el caso del
direccionamiento por fichero único.

**Plantillas (`SegmentTemplate`), el esquema del experimento.** La plantilla
puede declararse en la representación o en su conjunto de adaptación, y el
analizador la busca en ese orden. En los manifiestos del experimento está en
el conjunto de adaptación y las seis representaciones la heredan. La
expansión sustituye literalmente las variables `$RepresentationID$`,
`$Number$` y `$Bandwidth$`; los manifiestos propios usan las dos últimas. El
número de segmentos se calcula redondeando el producto de la duración del
periodo por la escala de tiempo, dividido por la duración declarada del
segmento, y las URL se generan desde el número inicial (`startNumber`). Con
los valores reales del contenido principal (periodo de 600,1 segundos;
61440/15360 = 4,000 segundos por segmento) el cálculo produce 150 segmentos
completos: el fragmento residual de una décima de segundo que existe en el
servidor queda fuera de la lista, y esa es la razón de la diferencia entre
los 151 ficheros publicados por representación y los 150 segmentos que el
cliente descarga y reproduce. Las duraciones por segmento se asignan con la
regla del apartado 4.2: la nominal para todos y el último ajustado al tiempo
restante del periodo, sin superar la nominal.

**Listas explícitas (`SegmentList`).** El caso más simple: se recorre la
lista de URL del manifiesto, con su segmento de inicialización, y la duración
por segmento sale del par escala-duración o, si falta, del reparto uniforme
de la duración del periodo entre los segmentos enumerados.

**Fichero único (`SegmentBase`) e índice `sidx`.** En este esquema el
manifiesto anuncia solo el rango de bytes del índice de segmentación. El
analizador descarga únicamente ese rango con una petición de rango HTTP y lo
interpreta a nivel binario. La caja `sidx` está definida en el formato
contenedor de los medios (ISO BMFF, *ISO Base Media File Format*)
\cite{iso14496_12_2015}: una secuencia de campos de tamaño fijo con los
enteros en orden de red. El analizador comprueba el tipo de caja, lee la
versión (que determina el ancho de dos campos temporales que no necesita),
la escala de tiempo y el contador de referencias, y extrae de cada
referencia el tamaño del subsegmento —los 31 bits bajos de su primer
entero— y su duración en unidades de la escala. Los campos restantes
(instante de presentación más temprano, desplazamiento inicial e información
de puntos de acceso) se omiten. Con esto construye lo que el reproductor
necesita: la lista de rangos de bytes consecutivos a partir del final del
índice y la duración de cada subsegmento. La Tabla 5.3 resume los campos
leídos y su uso. Si el índice no puede interpretarse, el analizador degrada
la representación a un único bloque con la duración del periodo completo y
lo anota; la sesión puede continuar.

**[TABLA 5.3 — Campos de la caja `sidx` que lee el analizador]**

| Campo | Tamaño | Uso en el cliente |
|---|---|---|
| Tipo de caja (`sidx`) | 4 bytes | Confirmar que el rango descargado es el índice |
| `version` | 1 byte | Ancho (32 o 64 bits) de los campos temporales que se omiten |
| `timescale` | 4 bytes | Convertir las duraciones del índice a segundos |
| `reference_count` | 2 bytes | Número de subsegmentos de la representación |
| `referenced_size` | 31 bits | Tamaño de cada subsegmento; de él salen los rangos de bytes de descarga |
| `subsegment_duration` | 4 bytes | Duración de cada subsegmento |

*Pie: Tabla 5.3: Campos del índice de segmentación (`sidx`) que interpreta el
analizador y uso que se les da.*

El resultado del análisis completo se entrega en estructuras de datos
elementales del lenguaje (diccionarios y listas), sin tipos propios del
módulo: el reproductor consume el contrato descrito en el apartado 4.2 sin
acoplarse a ningún detalle interno del analizador, que puede sustituirse por
otro que produzca la misma estructura.

*(El apartado 5.4 describe el lanzador de experimentos y la configuración.)*

---

### Notas para Daniel (no van a la memoria)

- **Citas (2), ambas verificadas contra PDF (03/09, pdfminer):**
  · `iso23009_1_2022`: el identificador `urn:mpeg:dash:schema:mpd:2011`
    figura en la Tabla 2 del estándar ("Schemes defined in this document").
    Es re-cita (ya citada en 4.2); aquí ancla el espacio de nombres.
  · `iso14496_12_2015`: la sintaxis de `SegmentIndexBox` (§8.16.3) coincide
    CAMPO A CAMPO con el parseo del código: `reference_ID(32)`,
    `timescale(32)`, `earliest_presentation_time`/`first_offset` (32+32 en
    version 0, 64+64 en version 1 → el código salta 8 o 16 bytes),
    `reserved(16)`, `reference_count(16)` y, por entrada,
    `reference_type(1)+referenced_size(31)` (la máscara `0x7FFFFFFF` del
    código), `subsegment_duration(32)` y los 32 bits de SAP que el código
    salta. Pasaje textual guardado en
    `scratchpad/sidx_iso.txt` de la sesión. Chuleta de defensa: "leo el
    índice tal cual lo define ISO 14496-12 §8.16.3, con struct en
    big-endian; puedo recitar el layout de memoria".
- **Verificado contra el MPD real (05_contenido_dash, Paseo 30 fps):**
  `SegmentTemplate` está EN EL AdaptationSet (las 6 Representation lo
  heredan) → la búsqueda en dos niveles del código es el caso real, no
  robustez teórica. Atributos reales: `timescale="15360"`,
  `duration="61440"`, `startNumber="1"`, media con `$Bandwidth$` y
  `$Number$`; `Period duration="PT0H10M0.100S"`; namespace en la raíz.
- **La matemática del 151/150** (por si el tribunal pregunta):
  `round(600,1 × 15360 / 61440) = round(150,025) = 150`. El servidor tiene
  151 `.m4s` (150 completos + residual de 0,1 s); el cliente lista 150. Es
  la explicación prometida en las notas del 4.2, ahora con el mecanismo.
- **Detalles del código que el texto NO cuenta** (decisión deliberada; que
  no te pillen sin saberlos):
  · Si la plantilla no declara `duration`, el código asume 30 segmentos
    como último recurso (los manifiestos con `SegmentTimeline` no se
    soportan; el contenido propio no los usa).
  · El parseo del `sidx` asume `first_offset = 0` (subsegmentos
    inmediatamente tras el índice): el caso de los empaquetados con un solo
    índice, que es el que produce MP4Box.
  · El formato con relleno `$Number%05d$` no se soporta (los MPD propios
    usan `$Number$` a secas).
  · La sustitución de variables es reemplazo literal de cadenas, no un
    intérprete de plantillas.
  · Las URL relativas se resuelven por concatenación con la base (la base
    sí se deriva con `urljoin`); suficiente para manifiestos sin rutas
    `../`, que son los del corpus del proyecto.
- **AVISO (resto muerto, no tocado):** `base.py` define dos atributos que
  nadie usa (`self.niveles`, `self.listas_segmentos`) — supervivientes de la
  poda. Si quieres, los quito (2 líneas) y queda la base limpia con solo
  `cargar()`; dímelo (goldens no se ven afectados: es código nunca leído).
- **Sin figura nueva:** F4.3 ya ilustra el flujo del analizador con el MPD
  real; una figura del layout binario del `sidx` sobredimensionaría el
  esquema secundario (el experimento usa plantillas). T5.3 carga el detalle.
- **Fronteras:** la construcción de la lista de reproducción con los rangos
  (init virtual, mínimo común) ya se contó en 5.2; el contrato de salida y
  la jerarquía del MPD, en 4.2; el contenido y su generación, en 6.3.
- Longitud: ~950 palabras. Si al masticar recortas, el candidato es el
  párrafo de `SegmentList` (el caso trivial); mantén entero el del `sidx`
  (es la promesa explícita del 4.2) y el del cálculo 150/151.
