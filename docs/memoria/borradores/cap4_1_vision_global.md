# Borrador 4.1 — Visión global del sistema y módulos

> BORRADOR para masticar y reescribir (12/08/2026). Impersonal, frases cortas.
> Los números de figura/tabla (4.1, 4.2…) son provisionales: en LaTeX los
> resuelven `\label`/`\ref`. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `TFG Material\01_codigo\ClienteDashTFG` (verificado 12/08).

---

## Capítulo 4. Diseño

*(Apertura del capítulo — obligatoria por las reglas de estilo)*

En el capítulo anterior se presentó la planificación del trabajo y la
descomposición del proyecto en paquetes de tareas. En este capítulo se describe
el diseño de la solución: la arquitectura global del sistema, sus módulos y las
decisiones estructurales que los conectan. La implementación concreta de cada
módulo se detalla en el capítulo 5.

### 4.1. Visión global del sistema

El sistema desarrollado es una plataforma experimental para streaming
adaptativo sobre MPEG-DASH \cite{iso23009_1_2022}. Consta de un cliente de
reproducción escrito en Python y de una infraestructura de apoyo para emular
condiciones de red, registrar telemetría y evaluar controladores de adaptación
de tasa binaria (ABR, *Adaptive Bitrate*). El diseño responde a cinco
requisitos fijados al inicio del proyecto:

1. Reproducir contenido DASH real servido por HTTP: interpretar el manifiesto
   (MPD), descargar segmentos de vídeo y gestionar un buffer de reproducción.
2. Admitir distintos controladores ABR de forma intercambiable, bajo una
   interfaz común, sin modificar el resto del cliente.
3. Someter cualquier controlador a condiciones de red reproducibles, mediante
   la reproducción de trazas de ancho de banda reales.
4. Registrar telemetría completa de cada sesión, con un formato estable que
   sirva de base a la evaluación.
5. Separar estrictamente la ejecución de sesiones de su evaluación posterior,
   de modo que las métricas de calidad no dependan del código que toma las
   decisiones.

El principio rector del diseño es la separación de responsabilidades. Cada
función del sistema (interpretar el MPD, descargar, reproducir, decidir la
calidad, registrar, evaluar) reside en un módulo independiente con una
interfaz reducida. Esta organización permite sustituir una pieza sin tocar las
demás. La consecuencia práctica más importante es que los seis controladores
implementados en este trabajo se ejecutan sobre exactamente el mismo cliente,
lo que garantiza una comparación en igualdad de condiciones.

La Figura 4.1 muestra la arquitectura de módulos. Se distinguen cuatro zonas:
la entrada y orquestación de una sesión, el núcleo de reproducción, los
módulos de apoyo que el núcleo utiliza, y los componentes que operan fuera de
la sesión (evaluación y entrenamiento).

**[FIGURA 4.1 — Arquitectura de módulos del cliente. Fichero:
`figuras/fig_4_1_arquitectura.svg`]**
*Pie: Figura 4.1: Arquitectura de módulos del sistema. Las flechas continuas
indican interacción durante una sesión de reproducción; las discontinuas,
procesos fuera de línea (evaluación de resultados y entrenamiento del modelo
del controlador propio).*

La zona de entrada la forman el punto de arranque (`main.py`) y dos módulos de
soporte: la configuración del cliente (`core/configuracion_cliente.py`), que
carga y valida un fichero YAML o JSON con todos los parámetros de la sesión, y
el contexto de ejecución (`core/contexto_ejecucion.py`), que crea un directorio
de salida por sesión y deja en él la configuración resuelta, un manifiesto de
ejecución y la información del entorno. Con ello, cada sesión queda
documentada y es repetible a partir de sus propios artefactos.

El núcleo es el reproductor (`reproductor.py`, clase `Reproductor`). Ejecuta
el bucle de sesión: recorre los segmentos del vídeo, coordina al resto de
módulos y registra una fila de telemetría por segmento. A su alrededor
trabajan cuatro grupos de módulos:

- **Análisis del manifiesto** (`core/analizador_mpd/`): interpreta el MPD y
  entrega al reproductor la lista de representaciones disponibles (la
  "escalera" de calidades) y los segmentos de cada una.
- **Descarga** (`core/descargador.py`): realiza las peticiones HTTP de
  segmentos, con reintentos ante errores. Cuando la sesión se ejecuta bajo
  red emulada, este descargador se envuelve con el descargador controlado por
  traza (`core/reproduccion_trazas/`), que limita el caudal efectivo según una
  traza de ancho de banda real; el diseño de esta emulación se detalla en el
  apartado 4.7.
- **Motor de reproducción** (`core/motores/`): consume el contenido encolado y
  hace avanzar el tiempo de reproducción, notificando eventos (segmento
  consumido, parada por falta de datos y su recuperación). Existen dos
  motores intercambiables: uno simulado y otro basado en GStreamer
  (apartado 4.4).
- **Control ABR** (`core/controladores/`): agrupa la interfaz común, el
  registro de controladores disponibles y las implementaciones concretas. El
  controlador propio se apoya además en el paquete `core/modelo_propio/`, que
  contiene su modelo de predicción y su planificador (capítulo 5).

Dos módulos transversales cierran la sesión: la construcción de la
realimentación (`core/feedback_reproductor.py`), que resume el estado
observable del cliente en un diccionario con claves fijas que recibe el
controlador, y el esquema de telemetría (`core/esquema_telemetria.py`), que
define las cabeceras de los ficheros CSV de salida (apartado 4.6).

Fuera del bucle de sesión quedan dos componentes. El paquete de evaluación
(`core/evaluacion/`) genera los planes de experimento, calcula la métrica de
calidad de experiencia (QoE, *Quality of Experience*) y analiza los
resultados; por diseño solo consume los ficheros de telemetría, nunca el
estado interno del cliente (apartado 4.8). El paquete de entrenamiento
(`entrenamiento/`), separado del núcleo, contiene el proceso de fabricación
del modelo del controlador propio; no se ejecuta durante las sesiones y su
salida es un paquete de modelo autocontenido que el controlador carga al
arrancar.

La Tabla 4.1 resume los módulos y su responsabilidad.

**[TABLA 4.1 — Módulos del sistema]**

| Módulo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada; monta la sesión a partir de la configuración |
| `core/configuracion_cliente.py` | Carga y validación de la configuración (YAML/JSON) |
| `core/contexto_ejecucion.py` | Directorio por sesión; config resuelta, manifiesto y entorno |
| `reproductor.py` | Bucle de sesión; coordinación y telemetría |
| `core/analizador_mpd/` | Interpretación del MPD (representaciones y segmentos) |
| `core/descargador.py` | Descarga HTTP de segmentos con reintentos |
| `core/reproduccion_trazas/` | Emulación de red por reproducción de trazas |
| `core/motores/` | Consumo del buffer y avance de la reproducción (simulado / GStreamer) |
| `core/controladores/` | Interfaz común, registro e implementaciones ABR |
| `core/modelo_propio/` | Modelo de predicción y planificador del controlador propio |
| `core/feedback_reproductor.py` | Construcción de la realimentación para el controlador |
| `core/esquema_telemetria.py`, `core/artefactos_salida.py` | Esquema y ficheros de salida |
| `core/evaluacion/` | Planes de experimento, QoE y análisis (fuera de sesión) |
| `entrenamiento/` | Fabricación del modelo propio (fuera de sesión) |

*Pie: Tabla 4.1: Módulos del sistema y responsabilidad de cada uno.*

El funcionamiento de una sesión se resume en la Figura 4.2. Tras cargar la
configuración y crear el contexto de ejecución, el cliente descarga y analiza
el MPD, construye la lista de segmentos por nivel de calidad y toma la
decisión inicial. A partir de ahí se repite el mismo ciclo para cada segmento:
si el buffer supera su máximo, el cliente espera; después descarga el segmento
del nivel vigente, lo entrega al motor de reproducción, construye la
realimentación con lo observado (estado del buffer, tamaño y tiempo de la
última descarga, estimación de ancho de banda) y se la pasa al controlador,
que decide el nivel del siguiente segmento. Cada iteración produce una fila de
telemetría. Al agotar los segmentos, el cliente señala el fin de flujo, drena
el buffer restante, detiene el motor y cierra los ficheros de salida.

**[FIGURA 4.2 — Flujo de una sesión de reproducción. Fichero:
`figuras/fig_4_2_flujo_sesion.svg`]**
*Pie: Figura 4.2: Flujo de una sesión de reproducción. El ciclo central se
repite por cada segmento del vídeo; los eventos del motor (parada y
recuperación) se anotan de forma asíncrona en la telemetría.*

Dos decisiones de esta visión global merecen justificación. La primera es
programar un cliente propio en lugar de instrumentar un reproductor existente:
el objetivo del trabajo exige control total sobre el bucle de decisión, la
telemetría y las condiciones de red, algo difícil de garantizar sobre una base
de código externa y cambiante; el capítulo 2 desarrolla esta comparación. La
segunda es la neutralidad del cliente respecto al controlador: el reproductor
no conoce qué algoritmo tiene delante; solo le entrega la realimentación
acordada y recibe una tasa objetivo. Esta frontera, definida formalmente en el
apartado 4.5, es la que permite que la comparativa del capítulo 6 atribuya las
diferencias de comportamiento únicamente al algoritmo de adaptación.

*(El apartado 4.2 continúa con el diseño del analizador de MPD.)*

---

### Notas para Daniel (no van a la memoria)

- Citas usadas: SOLO `\cite{iso23009_1_2022}` (primera mención de MPEG-DASH en
  el capítulo). El resto del 4.1 es aportación propia, sin bibliografía.
- "seis controladores": los 5 de la comparativa + el MPC básico implementado.
  Si prefieres no mencionar el sexto aquí, cambia a "los controladores".
- La frase final del primer párrafo de la visión ("comparación en igualdad de
  condiciones") conecta deliberadamente con el cap 6 (rúbrica: hilo narrativo).
- Términos definidos aquí por primera vez en el cap 4: ABR y QoE (ya definidos
  antes en caps 1-2 cuando existan; mantener la definición en la PRIMERA
  aparición global del documento y quitar la de aquí si queda duplicada).
- Longitud borrador: ~950 palabras. Al masticar, recorta libremente las
  enumeraciones; las figuras y la tabla ya cargan parte del contenido.
