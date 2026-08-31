# Borrador 5.1 — Lenguaje de programación y bibliotecas

> BORRADOR para masticar y reescribir (31/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: entregable `TFG Material\01_codigo\ClienteDashTFG` (censo de
> imports de los 80 .py, `requirements.txt`, `main.py`, `configuracion_cliente.py`,
> `core/modelo_propio/bundle.py`, `core/evaluacion/analisis.py`) +
> `docs/defensa/componentes_experimento.md` + `00_info_entorno/` (versiones).

---

## Capítulo 5. Implementación

*(Apertura del capítulo — obligatoria por las reglas de estilo)*

En el capítulo anterior se definió el diseño de la plataforma: sus módulos, las
fronteras entre ellos y las decisiones que las justifican. En este capítulo se
describe cómo se materializa ese diseño en código. Se presentan el lenguaje y
las bibliotecas empleadas (5.1), la implementación del cliente y de la
reproducción de trazas (5.2), el analizador del manifiesto (5.3), el lanzador
de experimentos y su configuración (5.4), los controladores clásicos (5.5), el
controlador propio (5.6) y el entorno de entrenamiento de su modelo (5.7). El
texto no reproduce código: describe las decisiones de implementación y recurre
a un fragmento solo cuando este explica algo que la prosa no puede justificar
por sí sola.

### 5.1. Lenguaje de programación y bibliotecas

Todo el software del proyecto está escrito en Python \cite{pythonDocs}. La
elección responde a tres razones. La primera es la portabilidad: el mismo
código se ejecuta sin modificaciones en los tres entornos que lo necesitan
(desarrollo en Windows, validación en una máquina virtual Linux y
entrenamiento del modelo en un segundo entorno Linux con GPU), sin pasos de
compilación ni empaquetado por plataforma; la topología completa de máquinas
se describe en el capítulo 6. La segunda es la amplitud de la biblioteca
estándar, que cubre la mayor parte de las necesidades del cliente (análisis de
XML, manejo de URL, concurrencia, formatos de datos, interfaz gráfica) sin
añadir dependencias externas. La tercera es el ecosistema de aprendizaje
automático: el modelo del controlador propio se entrena y se ejecuta con
PyTorch, y mantener un único lenguaje en todo el sistema evita duplicar
estructuras de datos y contratos entre un cliente y un entorno de
entrenamiento escritos en tecnologías distintas.

El rendimiento del lenguaje no es una limitación en este sistema, y no por
casualidad sino por diseño. El motor simulado hace avanzar el tiempo de
reproducción sin decodificar vídeo (apartado 4.4), y el motor real delega la
decodificación en GStreamer, una biblioteca nativa. El papel del código Python
durante una sesión se reduce a coordinar descargas, buffer y decisiones, una
carga dominada por las esperas de red y no por el cálculo.

Los intérpretes empleados van de la versión 3.8 (el Python del sistema de la
máquina de validación) a la 3.12 (desarrollo y entrenamiento). El código se
mantiene compatible con la versión más antigua. Para no renunciar por ello a
las anotaciones de tipos modernas, los módulos activan la evaluación pospuesta
de anotaciones que ofrece el propio lenguaje, de modo que la sintaxis reciente
de tipos convive con el intérprete antiguo.

**Política de dependencias mínimas.** La instalación del cliente declara solo
dos paquetes externos: `requests`, para las descargas HTTP, y `matplotlib`,
para las gráficas del análisis. Todo lo demás que el sistema necesita de forma
incondicional proviene de la biblioteca estándar. Las capacidades que amplían
el sistema (el motor de reproducción real, la configuración en formato YAML,
las propias gráficas) se apoyan en dependencias opcionales cuya ausencia
degrada una función concreta en lugar de impedir la ejecución. Esta política
tiene una motivación experimental además de práctica: cuantas menos piezas
externas, más sencillo resulta replicar el banco de pruebas en otra máquina y
menos superficie hay para diferencias de comportamiento entre entornos. La
Tabla 5.1 resume los componentes, su papel y las versiones empleadas.

**La biblioteca estándar.** Las piezas del cliente descritas en el capítulo 4
se implementan casi por completo con módulos estándar. El analizador del
manifiesto usa `xml.etree.ElementTree` para recorrer el árbol XML del MPD
\cite{pythonElementTree} y `urllib.parse` para resolver las URL relativas
contra la base del manifiesto \cite{pythonUrllibParse}. El motor simulado
sostiene su consumo a velocidad real sobre un hilo de la biblioteca de
concurrencia (`threading`). La telemetría y los artefactos de sesión se
escriben con los módulos de CSV y JSON, sin formatos binarios ni bases de
datos. Los contratos de datos internos (configuración, resultados de descarga,
estado de sesión) se definen como clases de datos (`dataclasses`) con tipos
explícitos. La verificación de integridad del paquete del modelo calcula
resúmenes SHA-256 con `hashlib`. Por último, las herramientas de línea de
órdenes definen sus argumentos con `argparse` y la interfaz gráfica del
lanzador de experimentos (apartado 5.4) se construye con `tkinter`, también
estándar. Ninguna de estas piezas añade requisitos de instalación.

**La descarga HTTP con `requests`.** La única dependencia externa obligatoria
del cliente es la biblioteca `requests` \cite{requestsDoc}. La alternativa
estándar (`urllib.request`) obligaría a construir a mano lo que el descargador
del apartado 4.3 exige: una conexión persistente reutilizada entre segmentos,
cabeceras controladas por petición, tiempos límite y peticiones de rango de
bytes. `requests` ofrece ese conjunto con un objeto de sesión maduro y de
comportamiento bien documentado, y su uso está muy asentado, lo que facilita
auditar que el cliente mide lo que dice medir. En la máquina de validación se
empleó la versión 2.22.

**Configuración en JSON o YAML.** Los ficheros de configuración del cliente y
de la evaluación admiten dos formatos de texto: JSON (*JavaScript Object
Notation*) y YAML (*YAML Ain't Markup Language*). El primero se procesa con la
biblioteca estándar. El segundo requiere el paquete `PyYAML` \cite{pyyamlDoc},
que se importa solo si el fichero lo necesita; para el caso de un entorno sin
el paquete, el cargador del cliente incorpora además un lector simplificado
propio que cubre el subconjunto de YAML empleado en el proyecto. La evaluación
formal del capítulo 6 se ejecutó con configuración JSON, de modo que esta
dependencia es estrictamente opcional.

**PyTorch, confinado al modelo propio.** PyTorch \cite{pytorchDocs} es la
única biblioteca de aprendizaje automático del sistema y desempeña dos
papeles: entrenar el modelo del controlador propio (en el entorno con GPU del
apartado 5.7, versión 2.9.1) y ejecutar su inferencia dentro del cliente
(sobre CPU en la máquina de validación, versión 2.4.1). Su uso está confinado
a los módulos del modelo propio y del entrenamiento; ningún otro componente
del cliente la utiliza. Que la inferencia se ejecute en CPU es un dato
relevante para la validez del experimento: el controlador propio decide en la
misma máquina virtual, sin aceleración, en la que compiten los controladores
clásicos, y su coste de decisión queda registrado en la telemetría y acotado
por las salvaguardas del apartado 4.5.

**Carga segura del modelo.** Los ficheros de pesos de PyTorch se serializan
con el módulo `pickle` de Python, un formato que puede ejecutar código
arbitrario durante la carga si no se restringe; el análisis de seguridad de
los mecanismos de carga de modelos de aprendizaje automático documenta este
riesgo y las opciones seguras de cada entorno \cite{digregorio2026mlLoading}.
El cliente adopta la variante restringida de PyTorch: los pesos se cargan con
la opción `weights_only`, que limita la deserialización a tensores y tipos
primitivos e impide importaciones dinámicas durante la carga. La arquitectura
de la red no viaja en el paquete del modelo: la define el propio código del
cliente, que instancia el modelo y le carga los parámetros. Como capa
adicional, cada fichero del paquete se comprueba contra su resumen SHA-256
antes de usarlo. El contenido del paquete del modelo se detalla en el
apartado 5.6.

**GStreamer y PyGObject, opcionales.** El motor de reproducción real depende
de GStreamer y de su enlace con Python, PyGObject (versiones 1.16.3 y 3.36 en
la máquina de validación). El arranque del cliente detecta su ausencia y la
comunica; sin ellos, el sistema queda limitado al motor simulado, que es
precisamente el empleado en toda la evaluación formal. La dependencia es, por
tanto, opcional en sentido estricto: ninguna medición del capítulo 6 la
necesita.

**Organización del código.** El proyecto se organiza en cuatro bloques. En la
raíz viven el punto de arranque (`main.py`) y el reproductor (`reproductor.py`).
El paquete `core/` contiene los módulos de ejecución presentados en el
capítulo 4 (Tabla 4.1). El paquete `entrenamiento/` agrupa la fabricación del
modelo del controlador propio y está separado del núcleo con una regla
estricta: ningún módulo del cliente lo importa, de modo que el código que se
ejecuta en una sesión no depende del código que fabrica el modelo. Por último,
`scripts/` reúne las herramientas de cada etapa del flujo experimental
(preparación del contenido, entrenamiento y evaluación), junto a los
directorios de apoyo `config/` (plantillas de configuración) y
`perfiles_video/` (los descriptores de tamaños del apartado 4.7). Las
herramientas externas con las que se generó y se sirve el contenido
(codificación, empaquetado DASH y servidor web) no forman parte del software
del cliente y se describen con el contenido y el entorno en el capítulo 6.

**[TABLA 5.1 — Componentes de software del sistema]**

| Componente | Papel en el sistema | Carácter | Versión empleada | Referencia |
|---|---|---|---|---|
| Python | Lenguaje de todo el sistema | Núcleo | 3.8.10 (validación) / 3.12 (desarrollo y entrenamiento) | \cite{pythonDocs} |
| Biblioteca estándar (`ElementTree`, `urllib.parse`, `threading`, `csv`, `json`, `dataclasses`, `hashlib`, `argparse`, `tkinter`) | Análisis del MPD, URL, concurrencia, telemetría, contratos, integridad, herramientas | Núcleo | La de cada intérprete | \cite{pythonElementTree, pythonUrllibParse} |
| `requests` | Descarga HTTP de manifiestos y segmentos | Núcleo (única obligatoria) | 2.22 | \cite{requestsDoc} |
| PyTorch | Modelo del controlador propio: entrenamiento e inferencia | Núcleo (uso confinado al modelo propio) | 2.4.1 (inferencia CPU) / 2.9.1 (entrenamiento GPU) | \cite{pytorchDocs} |
| `PyYAML` | Configuración en formato YAML | Opcional (con lector propio de respaldo) | 5.3.1 | \cite{pyyamlDoc} |
| `matplotlib` | Gráficas del análisis de resultados | Opcional (solo gráficas) | 3.8 o superior (requisito declarado) | — |
| GStreamer + PyGObject | Motor de reproducción real | Opcional (verificación funcional) | 1.16.3 / 3.36 | \cite{gstreamerDocs, pygobjectDoc} |

*Pie: Tabla 5.1: Componentes de software del sistema, su papel, su carácter y
las versiones empleadas en el experimento.*

*(El apartado 5.2 desciende a la implementación del cliente y de la
reproducción de trazas.)*

---

### Notas para Daniel (no van a la memoria)

- **Citas usadas (7 claves):** `pythonDocs`, `pythonElementTree`,
  `pythonUrllibParse`, `requestsDoc`, `pyyamlDoc`, `pytorchDocs`,
  `digregorio2026mlLoading`; en la tabla, además, `gstreamerDocs` y
  `pygobjectDoc` (ya citadas en 4.4 — repetirlas en la tabla es correcto).
  `matplotlib` NO tiene entrada en el `.bib` → va sin cita (regla: ni una
  referencia fuera del `.bib`). `rocmDocs` se reserva para 5.7/6.2.
- **Verificación PDF-primero de `digregorio2026mlLoading`** (hecha 31/08 con
  pdfminer sobre `biblioteca_final\08_herramientas_seguridad\`). Citas
  textuales por si el tribunal aprieta:
  · "when weights_only=True, PyTorch uses pickle with a restricted unpickler
    that limits deserialization to torch.Tensor objects and primitive types,
    and prevents dynamic imports during loading" — respalda la frase del
    borrador casi literal.
  · "When weights_only=False ... no security restrictions are enforced to
    prevent arbitrary code execution, as raw pickle is known to be insecure".
  · Matiz del paper: los formatos weights-only "merely shift the trust
    problem: model architecture code must be provided separately". En tu caso
    ese matiz JUEGA A FAVOR: la arquitectura la define TU código
    (`core/modelo_propio/modelo.py`), no el bundle → el problema de confianza
    desplazado queda resuelto dentro del propio cliente. Chuleta de defensa:
    "el bundle solo transporta tensores y JSON; el código que los interpreta
    es mío y está versionado; y cada fichero se verifica por SHA-256".
- **Todo verificado contra el entregable (31/08):**
  `weights_only=True` en `core/modelo_propio/bundle.py` (con `map_location="cpu"`)
  y en `entrenamiento/exportar_bundles.py`; lector YAML propio de respaldo en
  `core/configuracion_cliente.py` (`_parsear_yaml_simple`, se usa si
  `ModuleNotFoundError`); matplotlib diferido y protegido en
  `core/evaluacion/analisis.py` (backend `Agg`; si falla escribe
  `graficas_no_generadas.txt` y el análisis numérico sigue); GStreamer con
  import protegido en `main.py` (mensaje claro + motor simulado); `requests`
  solo en `core/descargador.py` y `core/analizador_mpd/dash.py`;
  `from __future__ import annotations` en 64 de los 80 .py (por el 3.8 de la
  VM); el entregable NO importa numpy ni pandas en ningún fichero (la
  estadística del análisis es Python puro) — por eso no aparecen en 5.1
  aunque estén instalados en la VM.
- **MATIZ IMPORTANTE que evité afirmar:** "los controladores clásicos
  funcionan sin PyTorch instalado" sería FALSO: el registro de controladores
  importa el controlador propio en cadena (registro → controlador_propio →
  modelo_propio.bundle → `import torch` a nivel de módulo), así que arrancar
  cualquier sesión requiere torch presente. El borrador dice "uso confinado
  al modelo propio" (verdadero) y en la tabla "Núcleo (uso confinado)". Si el
  tribunal pregunta: "la dependencia se carga al arrancar porque el registro
  declara los seis controladores; quien la usa es solo el modelo propio".
- **AVISOS (restos detectados hoy; no he tocado nada):**
  1. `requirements.txt` del ENTREGABLE conserva comentarios con nomenclatura
     vieja: "Dependencias del cliente y de Phase 6." y "PyTorch (controllers
     IA)". Propuesta si quieres que lo deje fino (2 líneas): "Dependencias del
     cliente y de la evaluación." / "GStreamer/PyGObject (motor real) y
     PyTorch (controlador propio) se instalan aparte." Dímelo y lo cambio yo,
     o cámbialo tú.
  2. `LEEME.md` de TFG Material dice "81 .py" pero el conteo real es **80**
     (quedó desactualizado cuando se eliminó `estado_replay.py` en la
     revisión). El borrador no cita el número; si quieres corrijo el LEEME.
  3. Coherencia menor: `requirements.txt` pide `requests>=2.31,<2.33` pero la
     VM de validación ejecutó la 2.22 del sistema (así lo registra
     `00_info_entorno` y así lo dice la memoria). No es contradictorio (el
     rango es para instalaciones nuevas), pero si el tribunal replica con
     `pip install -r requirements.txt` obtendrá 2.31+. Opciones: relajar a
     `>=2.22` o dejarlo. Decisión tuya.
- **Fronteras respetadas (qué NO cuenta 5.1):** el detalle del descargador y
  del replay (→5.2), el parseo del sidx (→5.3), runner/GUI (→5.4), algoritmos
  (→5.5/5.6), ROCm/WSL y el pipeline de entrenamiento (→5.7), topología de
  máquinas, hardware y herramientas del servidor ffmpeg/MP4Box/Apache/Docker
  (→6.2/6.3), números de resultados (→6.6).
- **Siglas:** JSON y YAML se definen aquí en su primera aparición formal. Si
  al montar el documento ya aparecieran definidas antes (cap 4.1 menciona
  "YAML o JSON" sin definir), deja la definición solo en la primera aparición
  global.
- **Sin figura:** un diagrama de librerías sería decorativo (regla del plan);
  la Tabla 5.1 carga el contenido. Las figuras nuevas del capítulo llegan en
  5.6 (F5/F6).
- Longitud: ~1080 palabras. Al masticar puedes recortar el párrafo de
  anotaciones pospuestas (el más prescindible) si te sobra detalle.
