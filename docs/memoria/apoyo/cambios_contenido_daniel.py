# -*- coding: utf-8 -*-
"""Cambios de contenido sobre el capitulo 4 y los apartados 5.1-5.2 de Daniel (revisiones del 09/11, C1-C32, D1-D8,
E1-E9), mas las erratas y las citas propuestas el 10/11. Los aplica convertir_word_daniel.py sobre su texto y TODO lo
nuevo sale en rojo subrayado para que Daniel lo reescriba con sus palabras.

Cada sustitucion: documento, identificador, texto original EXACTO (tal como queda tras los ajustes tipograficos, sin
marcas de cursiva) y texto nuevo. En el texto nuevo, lo que va entre ⟦ y ⟧ se pinta en rojo; //x// es cursiva.
`exacto` obliga a que el texto original sea la celda entera (para celdas cortas como «0,5 s»).
"""

SUSTITUCIONES = [
    # ------------------------------------------------------------------ Capitulo 4
    ("cap4", "errata 4.1 (al / Adaptive)",
     "enfocada a él streaming adaptativo en MPEG-DASH",
     "enfocada ⟦al⟧ streaming adaptativo en MPEG-DASH"),
    ("cap4", "errata 4.1 (Adaptive)", "Adaptative Bitrate", "⟦Adaptive⟧ Bitrate"),
    ("cap4", "errata 4.1 (apartado sin cerrar)",
     "basado en GStreamer (apartado", "basado en GStreamer (apartado ⟦4.4)⟧"),
    ("cap4", "C1+C2",
     "Ya fuera del bucle de sesión restan dos componentes. Uno de ellos es el paquete donde se evalúa "
     "(core/evaluacion/), calcula la métrica de calidad de experiencia, también conocida como QoE o Quality of "
     "Experience y analiza los resultados obtenidos;",
     "Ya fuera del bucle de sesión restan ⟦tres⟧ componentes. Uno de ellos es el paquete donde se evalúa "
     "(//core/evaluacion///), calcula la métrica de calidad de experiencia, también conocida como QoE o Quality of "
     "Experience⟦, aplica los contrastes estadísticos fijados antes de ejecutar (apartado 4.8)⟧ y analiza los "
     "resultados obtenidos;"),
    ("cap4", "C3 + errata (al, halla) + C1 pruebas",
     "En cuanto a el paquete de entrenamiento (entrenamiento/), se haya separado del núcleo, en él se incluye el "
     "proceso por el cual el modelo del controlador propio es fabricado; durante las sesiones no se ejecuta y su "
     "salida es un paquete que el controlador carga a la hora de comenzar su operación.",
     "En cuanto ⟦al⟧ paquete de entrenamiento (//entrenamiento///), se ⟦halla⟧ separado del núcleo, en él se "
     "incluye el proceso por el cual el modelo del controlador propio es fabricado; durante las sesiones no se "
     "ejecuta y su salida es un paquete que el controlador carga ⟦al crearse, antes de que arranque la sesión⟧. "
     "⟦El tercero es la carpeta //pruebas///: dieciocho pruebas automáticas (unittest) del reproductor, del MPC "
     "canónico, de las variantes del propio, de los contrastes y de la carga del modelo; se ejecutan antes de cada "
     "evaluación y no intervienen en la sesión.⟧"),
    ("cap4", "C5 Tabla 4.1 (evaluacion)",
     "QoE y análisis de los resultados (fuera del núcleo o sesión)",
     "⟦QoE, contrastes prerregistrados y análisis⟧ (fuera del núcleo o sesión)"),
    ("cap4", "C4",
     "construye una lista con los segmentos por nivel de calidad disponibles para ese contenido y toma la primera "
     "de las decisiones. Desde ese punto se repite el mismo bucle para cada segmento:",
     "construye una lista con los segmentos por nivel de calidad disponibles para ese contenido y ⟦fija el nivel "
     "inicial: en la evaluación es el más bajo de la escalera para todos los controladores (el reproductor puede "
     "pedir esa primera decisión al controlador, pero la opción no se usa). El primer segmento se descarga sin "
     "consultar al controlador (calentamiento) y desde el segundo se repite el mismo bucle⟧ para cada segmento:"),
    ("cap4", "cita 4.1 (dash.js, Shaka) + errata (halla)",
     "desarrollar un cliente propio en vez de emplear uno existente:",
     "desarrollar un cliente propio en vez de emplear uno existente ⟦[dashjsRefClient], [shakaPlayer]⟧:"),
    ("cap4", "errata 4.1 (halla)",
     "Esta frontera, que se haya definida específicamente", "Esta frontera, que se ⟦halla⟧ definida específicamente"),
    ("cap4", "C7",
     "(en las variantes del contenido a 60 frames por segundo de 60000 con mismo resultado)",
     "(⟦Paseo a 60 fps usa timescale 60000 y duration 240000, también 4,000 s; Blender a 60 fps conserva 15360 y "
     "61440⟧)"),
    ("cap4", "cita 4.2 (ISO BMFF)",
     "el rango de bytes al que corresponde su índice (sidx).",
     "el rango de bytes al que corresponde su índice (sidx) ⟦[iso14496_12_2015]⟧."),
    ("cap4", "C6",
     "(tanto en el principal contenido como en el del experimento, PT0H10M0.100S: diez minutos más una décima de "
     "segundo)",
     "(⟦en el contenido principal, Paseo a 30 fps, PT0H10M0.100S: diez minutos más una décima de segundo; cada "
     "vídeo del experimento lleva la suya: PT0H10M34.600S en Blender a 30 fps y PT0H10M0.000S en Tears of Steel⟧)"),
    ("cap4", "cita 4.3 (RFC 9111, caché)",
     "evitando de ese modo una caché intermedia que pueda contaminar los tiempos de descarga",
     "evitando de ese modo una caché intermedia ⟦[rfc9111]⟧ que pueda contaminar los tiempos de descarga"),
    ("cap4", "C9+C10",
     "el reproductor espera hasta 10 segundos con un retroceso exponencial de 0,5 segundos que se duplican hasta "
     "alcanzar ese límite, una vez agotados seis intentos, ordena una degradación al nivel de calidad más bajo en "
     "la petición y lo vuelve a intentar; solo en el caso de que el fallo continue aun con el nivel más bajo, el "
     "segmento es abandonado y se salta al siguiente.",
     "el reproductor espera ⟦con una pausa que se duplica en cada intento, de 1 s a un tope de 10 s (1, 2, 4, 8, "
     "10)⟧, una vez agotados seis intentos, ⟦baja un nivel y repite el ciclo de seis intentos; solo cuando el fallo "
     "persiste ya en el nivel más bajo⟧, el segmento es abandonado y se salta al siguiente."),
    ("cap4", "C8",
     "espera dando pasos de 0,5 segundos hasta que el umbral baje",
     "espera dando pasos ⟦cortos (0,5 s por defecto; 0,01 s en la evaluación, para no retrasar la siguiente "
     "descarga)⟧ hasta que el umbral baje"),
    ("cap4", "C11",
     "recopila sus valores por defecto, que son exactamente los que se usan en la evaluación del capítulo 6.",
     "recopila sus valores por defecto ⟦y, cuando difieren, los fijados en la evaluación del capítulo 6⟧."),
    ("cap4", "C11 Tabla 4.3 cabecera", "Valor por defecto usado en el capítulo 6",
     "⟦Valor por defecto (en la evaluación, si difiere)⟧", "exacto"),
    ("cap4", "C11 Tabla 4.3 paso", "0,5 s", "0,5 s ⟦(0,01 s en la evaluación)⟧", "exacto"),
    ("cap4", "C10 Tabla 4.3 espera", "0,5 s hasta 10 s", "⟦1 s hasta 10 s, duplicándose⟧", "exacto"),
    ("cap4", "C12",
     "(este valor es de 1 segundo por defecto)",
     "(⟦1 s por defecto; 0,1 s en la evaluación, para que el arranque y la salida de cada parada dependan de la red "
     "y no del umbral⟧)"),
    ("cap4", "C13 + citas BBA/BOLA/MPC/Pensieve",
     "El registro cuenta con seis controladores: uno basado en la tasa de bits, dos basados en el buffer (BOLA y "
     "BBA), dos basados en control con carácter predictivo (MPC y su versión robusta) y el controlador propio "
     "propuesto en este trabajo.",
     "El registro cuenta con ⟦nueve entradas: uno basado en la tasa de bits, dos basados en el buffer (BBA "
     "[huang2014bba] y BOLA [spiteri2020bola]), el MPC y su versión robusta en la forma canónica de Yin et al. "
     "[yin2015mpc] y del código de Pensieve [mao2017pensieve] (horizonte de cinco segmentos, QoE lineal, tamaños "
     "reales, error frente a la media armónica), el controlador propio propuesto en este trabajo y tres variantes "
     "de ablación que comparten su planificador y cambian solo la predicción (solo la mediana de la red; cuantiles "
     "fijos sin red; cuantiles de las últimas descargas sin red). En la evaluación corren ocho: todos salvo el MPC "
     "no robusto.⟧"),
    ("cap4", "C14+C15+C16",
     "una máscara que describe las acciones válidas y comprueba que la acción escogida pertenece a una "
     "representación real y permitida (ofreciendo la acción menor válida como alternativa de seguridad); un "
     "controlador clásico a modo de respaldo, el cual recibe el peso de la decisión si el modelo falla o supera un "
     "límite de tiempo en su ejecución; y la comprobación del estado de integridad en la carga del paquete del "
     "modelo predictivo.",
     "una máscara que describe las acciones válidas y comprueba que la acción escogida pertenece a una "
     "representación real y permitida (⟦si la acción no pasa la máscara, decide el respaldo; la acción válida más "
     "baja queda como último recurso si el respaldo también falla⟧); ⟦el MPC robusto canónico como respaldo, creado "
     "junto al propio para el mismo vídeo y alimentado con toda la realimentación de la sesión, de modo que su "
     "historial está completo si tiene que decidir; entra si el modelo falla, si la acción no es válida o si la "
     "inferencia supera 50 ms⟧; y ⟦la carga del paquete del modelo predictivo con comprobación de integridad al "
     "crear el controlador, antes de la sesión; si falla, se reintenta en cada decisión y mientras decide el "
     "respaldo⟧."),
    ("cap4", "errata pie Figura 4.5 (dividido)",
     "un contrato de realimentación (divido en cuatro bloques)",
     "un contrato de realimentación (⟦dividido⟧ en cuatro bloques)"),
    ("cap4", "C17",
     "A modo de respaldo para que la medida entre todos los controladores sea equitativa, las paradas producidas "
     "por el último segmento no valen en la evaluación, lo cual es razonable dado que el consumo último del buffer "
     "no es motivo de comparación.",
     "⟦Cada parada se apunta al segmento que el cliente está esperando descargar, que es el que falta en el "
     "buffer. Las paradas que empiezan cuando ya no queda nada por descargar son el vaciado final y se ignoran: la "
     "sesión las distingue por estado, no por posición, y la fila del último segmento se conserva como las "
     "demás.⟧"),
    ("cap4", "errata 4.6 (punto)", "Clasificaciones de fase En cada fila", "Clasificaciones de fase⟦.⟧ En cada fila"),
    ("cap4", "C18",
     "la etapa donde se produce un régimen estable y finalmente el vaciado del contenido.",
     "la etapa donde se produce un régimen estable⟦; el vaciado final no genera filas y se trata como un estado de "
     "la sesión⟧."),
    ("cap4", "errata pie Tabla 4.6 (cinco)",
     "Tabla 4.6: Los cuatro bloques de columnas", "Tabla 4.6: Los ⟦cinco⟧ bloques de columnas"),
    ("cap4", "cita 4.7 (Oboe)",
     "redes de 4G y 5G [raca2018beyondThroughput4g], [narayanan2020lumos5g], son un ejemplo",
     "redes de 4G y 5G [raca2018beyondThroughput4g], [narayanan2020lumos5g] ⟦y sesiones de vídeo reales de Oboe "
     "[akhtar2018oboe]⟧, son un ejemplo"),
    ("cap4", "C19", "(fase de entrenamiento, test y evaluación)", "(⟦entrenamiento, validación y evaluación⟧)"),
    ("cap4", "C20",
     "(en el caso de la evaluación, 300 segundos)",
     "(⟦en la evaluación, 160 s, con una vuelta de seguridad: si la sesión consume la ventana, la traza vuelve a "
     "su inicio una sola vez; una sesión de 30 segmentos consume como mucho unos 145 s⟧)"),
    ("cap4", "C21",
     "si se agotase la ventana en medio de una descarga, la sesión falla y se marca",
     "⟦si la ventana se agota, la traza se repite desde su inicio una sola vez y, si aun así se agota, la sesión "
     "falla y queda marcada⟧"),
    ("cap4", "errata 4.7 (espacio)", "(VBR o Variable Bit Rate )", "(VBR o Variable Bit Rate)"),
    ("cap4", "C22",
     "aparecen unas desviaciones en el tamaño del contenido entre segmentos de la misma representación de hasta "
     "el 16 por ciento, por otro lado, la media total por representación si se aproxima razonablemente al valor "
     "nominal.",
     "⟦en los vídeos vistos, el coeficiente de variación dentro de una representación está entre 0,05 y 0,19 en "
     "los 30 segmentos de una sesión (hasta 0,16 sobre el vídeo completo); en Tears of Steel sube a 0,28–0,31. La "
     "media por representación queda cerca del nominal en los vistos (de un 6 % por debajo a un 3 % por encima) y "
     "entre un 8 y un 12 % por debajo en Tears of Steel, cuyos dos primeros segmentos son casi negros.⟧"),
    ("cap4", "C23",
     "Este contenido es consumido por dos entidades: primero por el entrenamiento del controlador propuesto, su "
     "simulador de sesiones de descarga emplea los segmentos con sus pesos de verdad, y segundo el planificador de "
     "la ejecución, que realiza la aproximación del tiempo de descarga del próximo segmento usando también el "
     "tamaño real.",
     "Este contenido es consumido por ⟦tres⟧ entidades: primero por el entrenamiento del controlador propuesto, "
     "su simulador de sesiones de descarga emplea los segmentos con sus pesos de verdad, ⟦después⟧ el planificador "
     "de la ejecución, que realiza la aproximación del tiempo de descarga del próximo segmento usando también el "
     "tamaño real⟦, y por último el MPC robusto canónico, que decide con el mismo planificador y los mismos "
     "tamaños reales con un único escenario⟧."),
    ("cap4", "C24",
     "Hablando de los algoritmos clásicos, ellos no emplean este dato, dado que su literatura oficial no lo toma "
     "en cuenta; cabe destacar que el JSON que describe los tamaños reales no tiene efecto en la sesión: solo sirve "
     "para aquel que sepa usarlo.",
     "⟦El basado en tasa, BBA y BOLA no lo usan (BOLA usa el nominal, como su artículo). El MPC robusto sí, porque "
     "su forma de referencia (código de Pensieve) planifica con tamaños reales. El descriptor no altera la sesión: "
     "solo lo lee quien lo necesita.⟧"),
    ("cap4", "C25",
     "tanto BOLA como MPC usan el dato nominal. Modificarlos podría dejar a la comparativa sin un respaldo "
     "bibliográfico, dado que ya se convertirían en versiones alternativas o implementaciones propias. Para los "
     "clásicos, el resultado de esta diferencia esta mas que contenido, dado que la media de tamaño del contenido "
     "real coincide con la media nominal, con una desviación muy pequeña (0,4 por ciento), por consiguiente, no "
     "existe un sesgo, tan solo se ignora la variabilidad entre el tamaño de los segmentos.",
     "⟦BOLA usa el nominal; el MPC robusto usa los tamaños reales como el código de Pensieve, de modo que frente al "
     "propio solo cambia la predicción⟧. Modificarlos podría dejar a la comparativa sin un respaldo bibliográfico, "
     "dado que ya se convertirían en versiones alternativas o implementaciones propias. ⟦Para BOLA el efecto está "
     "acotado: en los vídeos vistos la media real se desvía del nominal entre −6 % y +3 %; en Tears of Steel el "
     "nominal sobreestima el tamaño medio entre un 8 y un 12 %, un sesgo hacia la prudencia.⟧"),
    ("cap4", "C26 + cita Pensieve (filtro)",
     "se escogen de manera balanceada respecto a su origen y tienen asociada una seed o semilla fija que da lugar "
     "a repetirlo si fuera necesario.",
     "⟦se usan todas las ventanas de 160 s de la partición de evaluación que superan un filtro de relevancia "
     "tomado de Pensieve [mao2017pensieve] (media < 6 Mbit/s y mínimo > 0,2 Mbit/s sobre la propia ventana), "
     "excluidos los 42 grupos de captura usados en el desarrollo, de modo que ninguna ventana se había ejecutado "
     "antes; el inicio de cada ventana se sortea con semilla fija, lo que permite repetirlo si fuera necesario.⟧"),
    ("cap4", "C27",
     "la metodología se basa en emparejar, eso quiere decir que todos los controladores se ejecutan para cada "
     "combinación entre vídeo y ventana de red, así las comparaciones",
     "la metodología se basa en emparejar: ⟦cada ventana real se empareja con dos vídeos, uno visto (en rotación "
     "entre los cuatro) y el contenido nuevo (Tears of Steel), y cada escenario se ejecuta con los ocho "
     "controladores en orden sorteado con semilla, para que la posición en la serie no favorezca a ninguno⟧, así "
     "las comparaciones"),
    ("cap4", "C28",
     "Cada experimento genera consigo el archivo de configuración que se usó, haciendo posible su auditoría.",
     "Cada experimento genera consigo el archivo de configuración que se usó⟦ y copia en el protocolo, antes de la "
     "primera sesión, las hipótesis que se contrastarán (referencia, rivales, métricas, margen y método), de modo "
     "que el análisis no se elige a la vista de los resultados⟧, haciendo posible su auditoría."),
    ("cap4", "cita 4.8 (Pensieve, QoE)",
     "que puede ser encontrada en la literatura [yin2015mpc]:",
     "que puede ser encontrada en la literatura [yin2015mpc]⟦, [mao2017pensieve]⟧:"),
    ("cap4", "C29",
     "En el momento de realizar los experimentos, esta medida de seguridad fue de gran ayuda dado que algunas "
     "ejecuciones que parecían completas fueron descartadas al fallar en una de las pruebas, permitiendo así "
     "detectar el problema y repetir el experimento habiéndolo solucionado.",
     "⟦Esta separación entre validez y comparación evita que una ejecución incompleta o contaminada entre en la "
     "comparativa.⟧"),
    ("cap4", "C30 Tabla 4.7 (respaldo)",
     "El controlador con modelo fue siempre quien tomó las decisiones",
     "⟦El propio y sus tres variantes decidieron siempre por sí mismos, sin respaldo⟧", "exacto"),
    ("cap4", "C30 Tabla 4.7 (inferencia)",
     "Cada decisión quedo registrada para ser auditada",
     "⟦Cada decisión del propio y de sus variantes lleva su auditoría; el tiempo de inferencia de la red se exige "
     "solo a las dos variantes que la usan⟧", "exacto"),
    ("cap4", "C31 + errata (punto)",
     "La verificación del paquete de evidencia Después del análisis se comprueba por medio de una verificación "
     "automática que todo el paquete",
     "La verificación del paquete de evidencia⟦.⟧ Después del análisis se comprueba por medio de una verificación "
     "automática ⟦de quince comprobaciones (estructura, ficheros, plan frente a sesiones, sin fallidas, sintéticas "
     "aparte, gráficas)⟧ que todo el paquete"),
    ("cap4", "C32",
     "En relación con el análisis estadístico, las sesiones de un controlador solo se comparan con las sesiones de "
     "otro que ha experimentado las mismas sesiones, la comparación se realiza usando deltas pareados por "
     "escenario, básicamente es la diferencia entre dos controladores, luego se aplica intervalos de confianza "
     "para la estimación de la mejora y de su incertidumbre, además inferencia no paramétrica, dado que en el "
     "streaming las métricas pueden ser muy irregulares, no se asume una distribución normal en específico, los "
     "resultados no solo se analizan por medias, si no que en su lugar se emplean distribuciones y colas para no "
     "ocultar comportamientos muy extremos, fijándonos en las buenas prácticas que aparecen en la literatura "
     "respecto a la evaluación del QoE [peroni2024qoePitfalls]. El como se aplican y los resultados finales son "
     "presentados en el capítulo 6.",
     "⟦El análisis se fijó antes de ejecutar. Las comparaciones son pareadas por escenario (ventana y vídeo). Como "
     "los dos escenarios de una ventana comparten red, la unidad de inferencia es la ventana: prueba del signo "
     "sobre la diferencia media por ventana e intervalos por bootstrap de ventanas. La hipótesis principal frente "
     "al MPC robusto es de equivalencia en QoE (TOST con margen fijado de antemano), acompañada de hipótesis de "
     "superioridad en paradas frente al MPC robusto y frente a las variantes de ablación, con corrección de Holm. "
     "No se asume normalidad; se presentan intervalos y distribuciones, no solo medias, siguiendo las buenas "
     "prácticas de la literatura sobre evaluación de QoE [peroni2024qoePitfalls]. El detalle y los resultados se "
     "presentan en el capítulo 6.⟧"),
    # ------------------------------------------------------------------ 5.1 y 5.2
    ("cap5", "errata 5.1 (halla)", "se haya redactado en Python", "se ⟦halla⟧ redactado en Python"),
    ("cap5", "D1",
     "Los intérpretes usados van de la versión 3.8 (en la máquina virtual cliente) a la 3.12 (Máquina anfitrión "
     "Windows y WSL).",
     "⟦Los intérpretes usados son Python 3.8.10 en la máquina virtual cliente, que es la que ejecutó el "
     "experimento; 3.12.3 en WSL para el entrenamiento; y 3.11 en la máquina Windows de desarrollo.⟧"),
    ("cap5", "D2",
     "Para instalar el cliente solo se requieren dos paquetes externos, requests, para el protocolo de descargas "
     "HTTP, y matplotlib, cuya función es crear las gráficas fruto del análisis. Cualquier otra cosa que necesite "
     "el sistema de manera obligatoria viene de la biblioteca estándar.",
     "⟦El fichero de requisitos lista tres paquetes: requests, para el protocolo de descargas HTTP; NumPy, para el "
     "planificador que comparten el propio, sus variantes y el MPC robusto; y matplotlib, cuya función es crear "
     "las gráficas fruto del análisis. PyTorch se instala aparte, en la máquina virtual en su variante de CPU. En "
     "la práctica, el registro de controladores importa el controlador propio al arrancar, así que NumPy y PyTorch "
     "tienen que estar instalados para ejecutar cualquier sesión, también con un controlador clásico; matplotlib "
     "solo se importa al generar gráficas y PyYAML es opcional. El resto viene de la biblioteca estándar.⟧"),
    ("cap5", "D3 (frase)",
     "Esta dependencia es la única que es externa y a la vez obligatoria para la ejecución del programa, requests "
     "[requestsDoc].",
     "⟦Esta es la dependencia externa para la descarga, requests [requestsDoc].⟧"),
    ("cap5", "D3 (versión)",
     "La versión empleada de esta biblioteca es la 2.22.",
     "La versión ⟦que ejecutó el experimento final es la 2.32.4⟧."),
    ("cap5", "D8",
     "por lo tanto, la dependencia acaba siendo opcional.",
     "por lo tanto, la dependencia acaba siendo opcional⟦; en la evaluación el ejecutor escribe la configuración de "
     "cada sesión en JSON, así que PyYAML no interviene en el experimento⟧."),
    ("cap5", "errata 5.1 (espacio)", "( por medio de la CPU", "(por medio de la CPU"),
    ("cap5", "D6",
     "el coste de decidir en la inferencia también se registra en la telemetría por medio del respaldo explicado "
     "en el 4.5.",
     "⟦el tiempo de inferencia y el tiempo total de decisión se registran en la telemetría de cada segmento; si la "
     "inferencia supera 50 ms, decide el respaldo explicado en el 4.5.⟧"),
    ("cap5", "D5",
     "El cómo está conformada la red no se encuentra dentro del paquete del modelo, este solo incluye los números "
     "que el modelo aprendió en su momento y es el código del cliente quien ya sabe cómo es el modelo y como está "
     "diseñada la red, se encarga de instanciar el modelo y cargar los parámetros.",
     "⟦El paquete no contiene código: lleva los pesos, un JSON con los hiperparámetros de la arquitectura (capas y "
     "tamaño oculto de la GRU, capas del MLP, cuantiles, horizonte, tamaño del ensemble), la normalización de "
     "entradas, la configuración del planificador y un manifiesto con la huella SHA-256 de cada fichero. El código "
     "del cliente define la red, la instancia con esos hiperparámetros y carga los pesos.⟧"),
    ("cap5", "D7 (bloques)", "El proyecto tiene cuatro bloques como tal.", "El proyecto tiene ⟦cinco⟧ bloques como tal."),
    ("cap5", "D7 (config, pruebas)",
     "en config/ se guardan las plantillas de configuración y en perfiles_video/ se guardan los descriptores de "
     "los tamaños que se explicaron en el 4.7.",
     "en //config/// se guardan las plantillas de configuración ⟦y la configuración de la evaluación⟧, en "
     "//perfiles_video/// se guardan los descriptores de los tamaños que se explicaron en el 4.7 ⟦y en "
     "//pruebas/// las 18 pruebas automáticas (unittest), que se lanzan antes de cada evaluación⟧."),
    ("cap5", "D1 Tabla 5.1 Python", "3.8.10 (MV cliente) / 3.12 (Windows Anfitrión y WSL)",
     "⟦3.8.10 (MV cliente) / 3.12.3 (WSL) / 3.11.9 (Windows)⟧", "exacto"),
    ("cap5", "D3 Tabla 5.1 requests tipo", "Núcleo (única dependencia obligatoria)", "⟦Núcleo⟧", "exacto"),
    ("cap5", "D3 Tabla 5.1 requests versión", "2.22", "⟦2.32.4⟧", "exacto"),
    ("cap5", "D4 Tabla 5.1 PyTorch", "Núcleo (solo se usa con el modelo propio)",
     "Núcleo ⟦(lo usa el modelo propio; hace falta para arrancar el cliente)⟧", "exacto"),
    ("cap5", "D4 Tabla 5.1 matplotlib", "3.8", "⟦3.7.5⟧", "exacto"),
    ("cap5", "E1",
     "y la política de actuación para cuando se acabe la ventana.",
     "y ⟦la política de fin de ventana con su número máximo de vueltas (en la evaluación, bucle con una sola "
     "vuelta)⟧."),
    ("cap5", "E3",
     "en la evaluación del capítulo 6 se emplea ese recorte para que todas las sesiones tengan una duración "
     "uniforme.",
     "en la evaluación del capítulo 6 se emplea ese recorte para que todas las sesiones tengan una duración "
     "uniforme⟦: 30 segmentos de 4 s, es decir, 29 decisiones tras el de calentamiento⟧."),
    ("cap5", "E2", "este se queda esperando en pasos fijos,",
     "este se queda esperando en pasos fijos ⟦(0,5 s por defecto; 0,01 s en la evaluación)⟧,"),
    ("cap5", "E4",
     "se apunta la parada al segmento que se estaba reproduciendo cuando se agotaron los datos, la cola es "
     "necesaria y nos permite mantener la correspondencia dado que un segmento ya descargado puede no haber sido "
     "reproducido.",
     "⟦la parada se apunta al segmento que el bucle está descargando en ese momento, el que falta para reanudar; "
     "la cola de índices sigue sirviendo para saber qué fila cerrar cuando el motor consume un segmento. Las "
     "paradas que empiezan cuando ya no queda nada por descargar son el vaciado final y se ignoran por estado.⟧"),
    ("cap5", "E5",
     "se escriben las últimas filas de telemetría pendientes, se cierran los ficheros de esta y el motor se "
     "detiene.",
     "se escriben las últimas filas de telemetría pendientes⟦, incluida la fila del último segmento, que se "
     "conserva como las demás,⟧ se cierran los ficheros de esta y el motor se detiene."),
    ("cap5", "E6",
     "el tamaño de los segmentos ocupa el rango desde las decenas de kilobytes a un par de megabytes",
     "el tamaño de los segmentos ⟦va desde unos 9 kB (los dos segmentos casi negros con que empieza Tears of "
     "Steel) y unos 80 kB en el nivel más bajo del resto de vídeos hasta unos 2,6 MB en el nivel más alto⟧"),
    ("cap5", "E7 Tabla 5.2", "Traza no está vacía y tiene caudal positivo", "⟦Traza no vacía⟧", "exacto"),
    ("cap5", "E8",
     "se modifica el origen temporal (el instante) de estas para que formen una secuencia partiendo del 0.",
     "⟦se compacta la línea temporal: cada muestra empieza donde acaba la anterior, desde 0, y desaparecen huecos "
     "y solapes.⟧"),
    ("cap5", "E9",
     "si la ventana se agota antes de que la entrega haya sido completada, la sesión es marcada como fallida.",
     "⟦si la ventana se agota, la traza vuelve a su inicio una sola vez (bucle con una vuelta); si también se "
     "agota esa vuelta, la sesión falla y queda marcada. Una sesión consume como mucho unos 145 s de los 160 s, "
     "así que el bucle es una salvaguarda.⟧"),
]

# Filas nuevas en tablas: (documento, identificador, primera celda de la fila tras la que se inserta, celdas).
FILAS_NUEVAS = [
    ("cap4", "C5 Tabla 4.1 pruebas/", "entrenamiento/",
     ["//pruebas///", "Pruebas automáticas del código entregado (18, unittest; fuera de la sesión)"]),
    ("cap4", "C11 Tabla 4.3 cola mínima", "Ventana de arranque (preroll)",
     ["Cola mínima del motor para arrancar o reanudar", "1 s (0,1 s en la evaluación)",
      "Segundos de vídeo en cola que exige el motor para empezar y para salir de cada parada (apartado 4.4)"]),
    ("cap5", "D4 Tabla 5.1 NumPy", "requests",
     ["NumPy", "Cálculo vectorial del planificador (propio, variantes y MPC robusto)", "Núcleo", "1.24.4", "—"]),
]

# Cambios en las figuras de Daniel (SVG suyos, NO se tocan aqui): solo se listan en las notas.
FIGURAS_PENDIENTES = {
    "Figura 4.2": "caja 5 → «Nivel inicial fijado por configuración (el más bajo en la evaluación); el primer segmento no "
                  "cambia (calentamiento)»",
    "Figura 4.5": "caja «Registro»: añadir las tres variantes; caja «Respaldo a controlador clásico» → «Respaldo al MPC "
                  "robusto»",
    "Figura 4.6": "«Ventana 300 s» → «Ventana 160 s con una vuelta de seguridad»; «entrenamiento / prueba / evaluación» → "
                  "«entrenamiento / validación / evaluación»; «si falla algo la sesión se detiene» → «la traza se repite "
                  "como mucho una vez; si aun así se agota, la sesión se detiene»; «8 vídeos en el servidor» → «9 vídeos "
                  "(5 en el experimento, uno nuevo)»; «variación típica 10 %, hasta 16 %» → «CV de 0,05 a 0,19 en los "
                  "vistos y de 0,28 a 0,31 en el contenido nuevo»",
    "Figura 5.1": "«si se termina antes de finalizar una entrega, la sesión falla y se registra» → «al final de la ventana "
                  "la traza vuelve a empezar (una sola vuelta); si aun así se agota, la sesión falla y se registra»",
}
