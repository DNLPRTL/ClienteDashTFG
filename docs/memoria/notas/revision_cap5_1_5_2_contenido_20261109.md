# Revisión de CONTENIDO de 5.1 y 5.2 (Word de Daniel) contra el sistema final — 09/11/2026

Documento revisado: `G:\Otros ordenadores\Mi portátil\backup memo\hasta 5_2.docx` (4083 palabras extraídas,
T5.1, T5.2, F5.1). Cotejado con el código de `TFG Material\01_codigo\ClienteDashTFG`, con `requirements.txt`,
con `00_info_entorno\*.txt`, con el `entorno.json` de las sesiones del paquete final y con
`docs/blindaje/03_CAMBIOS_CODIGO_BLINDAJE.md`. Solo contenido.

Formato: apartado · frase actual · frase propuesta · por qué (fuente). Las propuestas son borrador.

## 5.1 Lenguaje y bibliotecas

D1 · «Los intérpretes usados van de la versión 3.8 (en la máquina virtual cliente) a la 3.12 (Máquina
anfitrión Windows y WSL).»
→ «Los intérpretes usados son Python 3.8.10 en la máquina virtual cliente, que es la que ejecutó el
experimento, 3.12.3 en WSL para el entrenamiento y 3.11 en la máquina Windows de desarrollo.»
Tabla 5.1, fila Python: «3.8.10 (VM cliente) / 3.12.3 (WSL) / 3.11 (Windows)».
Por qué: `entorno.json` de las 1208 sesiones (3.8.10), `info_entorno_wsl.txt` (3.12.3), intérprete de la
máquina Windows (3.11.9).

D2 · «Para instalar el cliente solo se requieren dos paquetes externos, `requests`, para el protocolo de
descargas HTTP, y `matplotlib`, cuya función es crear las gráficas fruto del análisis. Cualquier otra cosa
que necesite el sistema de manera obligatoria viene de la biblioteca estándar.»
→ «El fichero de requisitos del cliente lista tres paquetes: `requests` para las descargas HTTP, NumPy para
el planificador que comparten el controlador propio, sus variantes y el MPC robusto, y `matplotlib` para las
gráficas del análisis. PyTorch se instala aparte (en la máquina virtual, la variante de CPU) para el modelo
del controlador propio. En la práctica, el registro de controladores importa el controlador propio al
arrancar, así que NumPy y PyTorch tienen que estar instalados para ejecutar cualquier sesión, también con un
controlador clásico; `matplotlib` solo se importa al generar gráficas y PyYAML es opcional. Lo demás viene
de la biblioteca estándar.»
Por qué: `requirements.txt` (requests, numpy, matplotlib); cadena de importación `main.py` →
`core/controladores/registro.py` → `controlador_propio.py` (numpy) → `core/modelo_propio/bundle.py`
(`import torch` al nivel del módulo); `core/evaluacion/analisis.py` importa matplotlib dentro de la función
de gráficas; el kit de la VM comprueba «Python tiene numpy y torch» antes de lanzar.

D3 · «Esta dependencia es la única que es externa y a la vez obligatoria para la ejecución del programa,
`requests` (...). La versión empleada de esta biblioteca es la 2.22.»
→ «`requests` es la dependencia externa del cliente para la descarga (...). La versión que ejecutó el
experimento final es la 2.32.4.»
Tabla 5.1, fila `requests`: «2.32.4» y «Núcleo» (sin «única dependencia obligatoria»).
Por qué: `entorno.json` de cada sesión registra `requests 2.32.4`. El 2.22.0 del `pip freeze` de
`info_entorno_cliente.txt` es el paquete del sistema de Ubuntu 20.04, no el que importó Python 3.8 en las
sesiones.

D4 · Tabla 5.1, otras filas:
`matplotlib` «3.8» → «3.7.5» (entorno.json; la 3.8 no existe para Python 3.8).
Fila nueva: «NumPy | Cálculo vectorial del planificador (controlador propio, sus variantes y MPC robusto) |
Núcleo | 1.24.4 | —» (entorno.json).
PyTorch: «2.4.1 (para la inferencia por CPU) / 2.9.1 (entrenamiento con GPU)» se mantiene (VM: 2.4.1+cu121
ejecutando en CPU, `info_entorno_cliente.txt`; WSL: 2.9.1+rocm7.2.1); «Núcleo (solo se usa con el modelo
propio)» → «Núcleo (lo usa el modelo propio; hace falta para arrancar el cliente)».
PyYAML 5.3.1, GStreamer 1.16.3 y PyGObject 3.36.0: correctos (`info_entorno_cliente.txt`).

D5 · «El cómo está conformada la red no se encuentra dentro del paquete del modelo, este solo incluye los
números que el modelo aprendió en su momento y es el código del cliente quien ya sabe cómo es el modelo y
como está diseñada la red, se encarga de instanciar el modelo y cargar los parámetros.»
→ «El paquete del modelo no contiene código: lleva los pesos (`pesos_modelo.pt`), un JSON con los
hiperparámetros de la arquitectura (capas y tamaño oculto de la GRU, capas del MLP, cuantiles, horizonte y
tamaño del ensemble), la normalización de las entradas, la configuración del planificador y un manifiesto
con la huella SHA-256 de cada fichero. El código del cliente define la red, la instancia con esos
hiperparámetros y después carga los pesos.»
Por qué: `03_modelos\modelo_propio\bundle\` (5 ficheros; `configuracion_modelo.json` con `capas_gru`,
`tamano_oculto_gru`, `capas_ocultas_mlp`, `dropout`, `cuantiles`, `horizonte_segmentos`, `tamano_ensemble`).
`weights_only=True` y `map_location="cpu"`: confirmados en `bundle.py:156`.

D6 · «el coste de decidir en la inferencia también se registra en la telemetría por medio del respaldo
explicado en el 4.5»
→ «el tiempo de inferencia de la red y el tiempo total de decisión se registran en la telemetría de cada
segmento (apartado 4.6); si la inferencia supera 50 ms, decide el respaldo».
Por qué: `controlador_propio.py` (`ms_inferencia`, `LATENCIA_MAX_INFERENCIA_MS = 50`), columna
`ms_decision_politica`.

D7 · «Estructuración del código. El proyecto tiene cuatro bloques como tal. (...)»
→ añadir un bloque: «y en `pruebas/` las dieciocho pruebas automáticas (unittest) que se ejecutan con
`python -m unittest discover -s pruebas` antes de cada evaluación». Y en `config/`: «las plantillas de
configuración y la configuración de la evaluación (`evaluacion.local.json`)».
Por qué: C8; árbol del entregado (103 ficheros).

D8 · «Configuración en JSON o YAML.» Se mantiene. Añadir: «En la evaluación, el ejecutor escribe la
configuración de cada sesión en JSON, de modo que PyYAML no interviene en el experimento.»
Por qué: `ejecutar_evaluacion.py` escribe con `json.dumps`; `configuracion_cliente.py` detecta JSON por la
llave inicial e importa `yaml` solo si no lo es.

Resto del 5.1 se mantiene: evaluación pospuesta de anotaciones (`from __future__ import annotations` en 70
de los 86 `.py`), `ElementTree`, `urllib.parse`, `threading`, `csv`, `json`, `dataclasses`, `hashlib`,
`argparse`, `tkinter` (importado dentro de la GUI), comprobados en el código.

## 5.2 El cliente

E1 · «esa versión recibe la ruta del archivo de la traza, su ventana correspondiente (cuando empieza y cuánto
dura) y la política de actuación para cuando se acabe la ventana»
→ «(...) y la política de fin de ventana con su número máximo de vueltas (en la evaluación, bucle con una
sola vuelta)».
Por qué: C6; `config_resuelta.json` (`politica_fin = loop`, `max_bucles = 1`).

E2 (opcional) · «este se queda esperando en pasos fijos» → «en pasos fijos (0,5 s por defecto; 0,01 s en la
evaluación)». Coherente con el cambio C8 del capítulo 4.

E3 · «en la evaluación del capítulo 6 se emplea ese recorte para que todas las sesiones tengan una duración
uniforme»
→ «(...) uniforme: 30 segmentos de 4 s, es decir, 29 decisiones del controlador tras el de calentamiento».
Por qué: `max_segmentos_video = 30` en el preset y en `config_resuelta.json`.

E4 · «en el momento que el vídeo agota el buffer, se apunta la parada al segmento que se estaba
reproduciendo cuando se agotaron los datos, la cola es necesaria y nos permite mantener la correspondencia
dado que un segmento ya descargado puede no haber sido reproducido»
→ «cuando el buffer se agota, la parada se apunta al segmento que el bucle está descargando en ese momento,
que es el que falta para reanudar; la cola de índices sigue sirviendo para saber qué fila cerrar cada vez
que el motor consume un segmento, porque un segmento descargado puede tardar en reproducirse. Las paradas
que empiezan cuando ya no queda nada por descargar corresponden al vaciado final y se ignoran por estado.»
Por qué: C2 (`reproductor.py:216-231`, `_descargas_terminadas`).

E5 · «finalmente y en este orden: se escriben las últimas filas de telemetría pendientes, se cierran los
ficheros de esta y el motor se detiene»
→ añadir «incluida la fila del último segmento, que se conserva como las demás».
Por qué: C2 (ya no se anula la fila del último segmento).

E6 · «el tamaño de los segmentos ocupa el rango desde las decenas de kilobytes a un par de megabytes»
→ «el tamaño de los segmentos va desde unos 9 kB (los dos segmentos casi negros con que empieza Tears of
Steel) y unos 80 kB en el nivel más bajo del resto de vídeos hasta unos 2,6 MB en el nivel más alto».
Por qué: descriptores de los 5 vídeos del experimento, 30 primeros segmentos: mínimo 9227 B (Tears of
Steel, 300 kbit/s), 80 416 B (Blender 30 fps, 300 kbit/s); máximo 2 578 014 B (Blender 60 fps, 4300 kbit/s).

E7 · Tabla 5.2, fila «Traza no está vacía y tiene caudal positivo | Condiciones irreales de red»
→ «Traza no vacía | Ventana sin muestras» y nota en el texto: «que la traza tenga alguna muestra con caudal
positivo lo comprueba el modelo de red al construirse; si no la tiene, la primera descarga falla con un
error explícito».
Por qué: `validacion.py` comprueba columnas, numéricos finitos, tiempo ≥ 0 y no decreciente, duración > 0,
throughput ≥ 0 y traza no vacía; el caudal positivo está en `modelo_red.py` (`_tiene_throughput_positivo`).

E8 · «se modifica el origen temporal (el instante) de estas para que formen una secuencia partiendo del 0»
→ «se compacta la línea temporal: cada muestra empieza donde acaba la anterior, desde 0, de modo que
desaparecen los huecos y solapes entre muestras del fichero original».
Por qué: `compactar_tiempos_traza` en `descargador_controlado.py`.

E9 · «Como se definió en el punto 4.7, si la ventana se agota antes de que la entrega haya sido completada,
la sesión es marcada como fallida.»
→ «Si la ventana se agota antes de completar una entrega, la traza vuelve a su inicio una sola vez
(política de bucle con una vuelta); si también se agota esa vuelta, la sesión falla y queda marcada. En el
experimento final una sesión consume como mucho unos 145 s de los 160 s de ventana, así que el bucle es una
salvaguarda.»
Por qué: C6; `modelo_red.py` (`_gestionar_fin_traza`), `06_PROTOCOLO_FINAL.md`.

Figura 5.1: CAMBIAR UN TEXTO. «si se termina antes de finalizar una entrega, la sesión falla y se registra»
→ «al final de la ventana la traza vuelve a empezar (una sola vuelta); si aun así se agota, la sesión falla y
se registra». El resto del esquema (posición ligada al reloj, bytes reales, última muestra parcial) es
correcto. El SVG es el de Daniel (`docs/memoria/figuras/fig_5_1_emulacion_descarga.svg`, sin commitear).

Resto del 5.2 se mantiene: manifiesto con cuatro estados (creado, en marcha, completado, fallido), dos hilos,
reloj monotónico (`perf_counter`), índice cero para la inicialización con entrada nula si falta, mínimo
común de segmentos, descargador que devuelve el fallo como resultado, estimación inicial del ancho de banda
con la tasa del nivel actual, HEAD y rango de un byte para el tamaño remoto, campos de auditoría del
replay, el envoltorio no consulta al modelo si la red real falla.

## Avisos que no van a la memoria

1. **PyTorch es obligatorio para arrancar el cliente**, aunque el controlador sea clásico, por la cadena de
   importación del registro. Es una decisión de empaquetado discutible (bastaría importar `torch` dentro de
   la carga del bundle). El código está congelado y la memoria dice lo que hay. Respuesta para el tribunal:
   el registro central declara todos los controladores y el propio carga su biblioteca al importarse; la VM
   lo comprueba antes de lanzar; no afecta a las decisiones ni a los tiempos de los clásicos.
2. Versiones: fuente única para lo que ejecutó el experimento es `entorno.json` (Python 3.8.10, requests
   2.32.4, numpy 1.24.4, matplotlib 3.7.5, pandas 2.0.3, Linux 5.15). El `pip freeze` de
   `info_entorno_cliente.txt` es del Python 3.10 del sistema (requests 2.22.0, numpy 2.2.6) y no vale para
   la tabla. Torch 2.4.1+cu121 (build CUDA ejecutando en CPU) sale de la sección «CLIENTE: GSTREAMER Y
   TORCH» del mismo informe; 2.9.1+rocm7.2.1 del informe de WSL.
3. La máquina Windows tiene Python 3.11.9, no 3.12. Irrelevante para el experimento.
4. El borrador del repo `cap5_1_lenguaje_librerias.md` (cambios sin commitear de Daniel) ya lleva 2.32.4,
   3.7.5 y NumPy; el Word es anterior (3 de septiembre) y no.
