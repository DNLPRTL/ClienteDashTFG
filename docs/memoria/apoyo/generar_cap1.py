# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap1_introduccion.docx: capitulo 1 completo (apertura, 1.1 motivacion,
1.2 problema, 1.3 enfoque, 1.4 objetivos numerados, 1.5 alcance, 1.6 estructura de la memoria).

Capitulo sin resultados (biblia §4). Los unicos datos del sistema que menciona se leen del material entregado
para no escribirlos a mano: escalera y duracion de segmento del MPD, numero de controladores y de hipotesis del
protocolo del experimento final, y la ausencia de pista de audio en el codigo (se comprueba por programa).
Las citas son claves del .bib y cada afirmacion atribuida tiene su pagina en notas_cap1_introduccion.md.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap1.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
MPD = TFG_MATERIAL / "05_contenido_dash" / "Paseo_Almunecar_10min_30fps" / "4sec" / "Paseo_Almunecar_10min_30fps_simple_4s.mpd"
PROTOCOLO = (TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje" / "00_protocolo"
             / "protocolo_validacion.json")
TAMANOS = CODIGO / "perfiles_video" / "tamanos_segmentos" / "paseo_almunecar_10min_30fps_4s.json"
CATALOGO = TFG_MATERIAL / "02_corpus_red" / "catalogo_trazas.json"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap1_introduccion.docx"
FIGURA_PNG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_1_1_enfoque_trabajo.png"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"


def datos_verificados():
    """Lee del material entregado lo poco que el capitulo afirma sobre el sistema."""
    mpd = MPD.read_text(encoding="utf-8")
    anchos = sorted(int(b) // 1000 for b in re.findall(r'bandwidth="(\d+)"', mpd))
    assert anchos == [300, 750, 1200, 1850, 2850, 4300], anchos
    ts = int(re.search(r'timescale="(\d+)"', mpd).group(1))
    dur = int(re.search(r' duration="(\d+)"', mpd).group(1))
    assert dur / ts == 4.0
    proto = json.loads(PROTOCOLO.read_text(encoding="utf-8"))
    controladores = [c["alias"] for c in proto["controladores"]]
    clasicos = [c for c in controladores if not c.startswith("propio") and c != "controlador_propio"]
    variantes = [c for c in controladores if c.startswith("propio_")]
    assert clasicos == ["basado_en_tasa", "bba", "bola", "mpc_robusto"], clasicos
    assert len(variantes) == 3 and "controlador_propio" in controladores
    hipotesis = proto["hipotesis"]["principales"]
    assert len(hipotesis) == 5 and proto["hipotesis"]["referencia"] == "controlador_propio"
    assert proto["motor"] == "simulado"
    # Sin pista de audio en el codigo entregado: ninguna fuente menciona "audio".
    con_audio = [p for p in CODIGO.rglob("*.py") if "audio" in p.read_text(encoding="utf-8", errors="ignore").lower()]
    assert not con_audio, con_audio
    # Variabilidad real de los tamaños en la calidad mas alta del contenido principal (descriptor entregado).
    tam = json.loads(TAMANOS.read_text(encoding="utf-8"))
    rep_max = max(tam["representations"], key=lambda r: r["bandwidth_bps"])
    assert rep_max["bandwidth_bps"] // 1000 == anchos[-1]
    bytes_seg = [x for x in rep_max["segment_bytes"] if x]
    nominal = rep_max["cbr_nominal_bytes"]
    cociente = max(bytes_seg) / min(bytes_seg)
    assert cociente >= 10 and max(bytes_seg) / nominal > 1.10 and min(bytes_seg) / nominal < 0.10, (
        cociente, max(bytes_seg) / nominal, min(bytes_seg) / nominal)
    # Corpus de red entregado: numero de conjuntos de trazas.
    cat = json.loads(CATALOGO.read_text(encoding="utf-8"))
    conjuntos = {t["id_dataset"] for t in cat["trazas"]}
    carpetas = {c.name for c in (TFG_MATERIAL / "02_corpus_red" / "datasets_normalizados").iterdir() if c.is_dir()}
    assert conjuntos == carpetas and len(conjuntos) == 12, (len(conjuntos), conjuntos ^ carpetas)
    # Bloques del material entregado que el 1.5 enumera.
    for bloque in ["00_info_entorno", "01_codigo", "02_corpus_red", "03_modelos", "04_evidencia_final",
                   "05_contenido_dash", "06_dataset_entrenamiento"]:
        assert (TFG_MATERIAL / bloque).is_dir(), bloque
    return {"niveles": len(anchos), "min_kbps": anchos[0], "max_kbps": anchos[-1], "seg_s": int(dur / ts),
            "n_clasicos": len(clasicos), "n_variantes": len(variantes), "n_hipotesis": len(hipotesis),
            "cociente_tamanos": int(cociente), "n_conjuntos": len(conjuntos)}


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    d = datos_verificados()
    claves = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))

    b = Borrador(PLANTILLA)
    b.capitulo(1, "Introducción")
    b.parrafo(
        "Este trabajo construye un cliente de streaming adaptativo MPEG-DASH y, sobre él, un controlador de "
        "adaptación de tasa propio que decide con la incertidumbre de la red a la vista, y compara ese "
        "controlador con los algoritmos clásicos de la literatura en un experimento diseñado y fijado antes de "
        "ejecutarlo. Este capítulo presenta el contexto que lo motiva (1.1), formula el problema técnico que "
        "aborda (1.2), expone el enfoque elegido y las razones de cada decisión de partida (1.3), enumera los "
        "objetivos que el capítulo 7 responderá uno a uno (1.4), delimita el alcance (1.5) y describe la "
        "estructura del resto de la memoria (1.6)."
    )

    # 1.1 ------------------------------------------------------------------------------------------------
    b.h2("1.1. Motivación y contexto")
    b.parrafo(
        "El vídeo es la mayor parte del tráfico de Internet desde hace más de una década. El survey de Seufert "
        "et al. lo situaba ya en 2015 por encima de la mitad del tráfico de consumo [seufert2015hasQoeSurvey], "
        "y la revisión de Timmerer et al. de 2025 mantiene esa fracción para el tráfico global "
        "[timmerer2025hasReview]. La mayor parte de ese vídeo se consume bajo demanda y se distribuye con "
        "streaming adaptativo sobre HTTP: el contenido se codifica en varias calidades, cada calidad se trocea "
        "en segmentos de unos pocos segundos y el cliente los descarga uno a uno con peticiones web ordinarias, "
        "eligiendo en cada segmento la calidad que mejor se ajusta a la red que observa. La arquitectura, "
        "normalizada por MPEG en el estándar DASH [iso23009_1_2022], se impuso porque reutiliza la "
        "infraestructura web existente, atraviesa cortafuegos y traductores de direcciones y escala añadiendo "
        "cachés, a cambio de trasladar al cliente toda la inteligencia de la sesión [stockhammer2011dash]."
    )
    b.parrafo(
        "Esa inteligencia es la que determina lo que el usuario percibe. Los estudios de calidad de experiencia "
        "coinciden en que las interrupciones de la reproducción son el factor que más la degrada, por delante "
        "de la calidad de imagen y del retardo inicial, y en que los cambios de calidad frecuentes o bruscos "
        "también penalizan [seufert2015hasQoeSurvey]. Para el proveedor, esa percepción se traduce en abandono "
        "de la sesión y del servicio; para el usuario, en una experiencia peor con la misma red y el mismo "
        "contenido. El algoritmo que elige la calidad de cada segmento, el controlador de adaptación de tasa o "
        "controlador ABR por sus siglas en inglés, es así una pieza pequeña con un efecto grande, y el estándar "
        "la deja deliberadamente sin especificar: DASH fija el formato del manifiesto y de los segmentos, pero "
        "no cómo debe decidir el cliente."
    )
    b.parrafo(
        "Conviene fijar desde ahora cómo se produce esa experiencia, porque todo el trabajo gira en torno a ello. "
        "El cliente no reproduce lo que descarga en el instante, sino que acumula por delante unos segundos de "
        "vídeo en un buffer: mientras la red va más deprisa que la reproducción, el buffer crece; cuando va más "
        "despacio, se consume. Si llega a vaciarse, la imagen se congela hasta que llega el siguiente segmento, "
        "y esa parada es lo que los usuarios peor toleran: los estudios recogidos por Seufert et al. muestran que "
        "la gran mayoría prefiere esperar unos segundos al principio antes que sufrir una interrupción a mitad "
        "de la reproducción [seufert2015hasQoeSurvey]. La adaptación de la calidad existe para evitar esas "
        "paradas sin renunciar a la imagen que la red permite, pero introduce su propio coste, el de los "
        "cambios de calidad visibles. El buffer es, por tanto, la variable que media entre la red y el usuario, "
        "y la decisión del controlador consiste en administrarlo."
    )
    b.parrafo(
        "El problema sigue abierto y activo. Las revisiones de la última década lo han recorrido desde los "
        "heurísticos basados en el ancho de banda o en el buffer hasta los métodos con aprendizaje automático "
        "[bentaleb2019survey, amer2025learningReview], y las de los dos últimos años lo sitúan en la cadena "
        "completa de distribución, del codificador a la pantalla [peroni2025pipelineSurvey, timmerer2025hasReview], "
        "y en las redes móviles de próxima generación, donde la variabilidad del canal hace más difícil decidir "
        "[alsader2025qoeDriven6g]. Dentro de la Universidad de Granada, el grupo del tutor de este trabajo "
        "estudió el comportamiento del tráfico de vídeo de YouTube en la época anterior a la adaptación en el "
        "cliente, tanto en redes fijas [ameigeiras2012youtubeTraffic] como en terminales móviles "
        "[ramosMunoz2014mobileYoutube], y documentó cómo las estrategias de descarga por ráfagas y umbrales de "
        "buffer fijos producían interrupciones cuando el ancho de banda caía. Este trabajo continúa esa línea en "
        "el punto donde el problema se decide hoy: el controlador del cliente."
    )

    # 1.2 ------------------------------------------------------------------------------------------------
    b.h2("1.2. Problema")
    b.parrafo(
        "El problema técnico es una decisión secuencial bajo incertidumbre. Antes de pedir cada segmento, el "
        "cliente conoce el estado de su buffer, la calidad del segmento anterior, los tiempos que han tardado "
        "las últimas descargas y la lista de calidades disponibles; no conoce el ancho de banda que tendrá "
        "durante la próxima descarga ni durante las siguientes. Con esa información debe elegir una calidad que "
        "satisfaga a la vez varios objetivos en conflicto: una tasa binaria alta, ninguna interrupción, pocos "
        "cambios de calidad y un arranque rápido [yin2015mpc]. Pedir más calidad de la que la red va a "
        "sostener vacía el buffer y para la reproducción; pedir menos desperdicia ancho de banda y ofrece peor "
        "imagen de la posible; cambiar a menudo molesta aunque la media sea buena. Cualquier controlador es una "
        "forma de resolver ese compromiso con la información disponible."
    )
    b.parrafo(
        "Dos rasgos del problema real lo hacen más difícil de lo que sugiere su enunciado. El primero es que el "
        "futuro de la red no se puede conocer, solo estimar, y el error de esa estimación no es simétrico: "
        "sobrestimar el ancho de banda cuesta una parada, subestimarlo cuesta algo de calidad. Un controlador "
        "que razone solo con la estimación puntual y la trate como cierta se expone a la cola mala de la "
        "distribución, que es precisamente la que produce las interrupciones; el MPC robusto de Yin et al. "
        "nació como respuesta a ese error de predicción [yin2015mpc], y trabajos posteriores han propuesto "
        "modelar explícitamente la incertidumbre y decidir con ella [kan2021bayesmpc]. El segundo rasgo es el "
        "medio. La tasa que anuncia el manifiesto para cada calidad es nominal: un codificador con tasa variable "
        "produce segmentos cuyo tamaño en bytes se aparta de ella según la complejidad de la escena, de modo que "
        "dos segmentos de la misma calidad pueden tardar en descargarse tiempos muy distintos con la misma red. "
        "Un controlador que planifique con la tasa nominal planifica con unos bytes que no son los que va a "
        "pedir."
    )
    b.parrafo(
        "El efecto no es marginal. En el contenido principal de este trabajo, un vídeo de diez minutos "
        "codificado con tasa variable, el segmento más pesado de la calidad más alta ocupa más de {0} veces los "
        "bytes del más ligero de esa misma calidad; el más pesado supera en más de un diez por ciento el tamaño "
        "que correspondería a la tasa nominal y el más ligero no llega a la décima parte. Con un ancho de banda "
        "constante, descargar uno u otro tarda, por tanto, tiempos que difieren en más de un orden de magnitud, "
        "y la diferencia entre vaciar el buffer o no está en saber cuál de los dos se va a pedir. El cliente "
        "puede saberlo, porque el tamaño de cada segmento se conoce al empaquetar el contenido; el apartado 1.3 "
        "explica cómo este trabajo pone esa información al alcance del controlador.".format(d["cociente_tamanos"])
    )
    b.parrafo(
        "A este problema de decisión se suma otro de evaluación, que la literatura reciente ha puesto en primer "
        "plano. La mayoría de los controladores publicados se desarrollan y se comparan en simuladores que "
        "reproducen trazas de ancho de banda, y la plataforma Puffer mostró que los algoritmos que destacan en "
        "esos simuladores no lo hacen necesariamente en una red real [yan2020puffer]; estudios posteriores han "
        "medido esa distancia entre simulación y realidad [hoffman2025intoTheWildABR] y han señalado que las "
        "propias trazas llevan impresa la política con la que se recogieron, lo que sesga cualquier "
        "comparación que las reutilice sin más [alomar2023causalsim]. Además, el orden de los controladores "
        "cambia según el modelo de calidad de experiencia con que se les mida [peroni2024qoePitfalls]. Comparar "
        "controladores de forma creíble exige, por tanto, un entorno cuyo nivel de fidelidad se conozca, unas "
        "métricas fijadas de antemano y una estadística que no se elija después de ver los datos. Este trabajo "
        "aborda las dos partes del problema: decidir mejor con la incertidumbre y el medio reales, y evaluar de "
        "una forma que se pueda defender."
    )

    # 1.3 ------------------------------------------------------------------------------------------------
    b.h2("1.3. Enfoque del trabajo")
    b.parrafo(
        "El trabajo responde a las dos partes del problema con cuatro decisiones de partida, que la Figura 1.1 "
        "sitúa en el conjunto: construir el entorno experimental completo, ser fiel al medio, acotar el "
        "aprendizaje a la predicción y evaluar con un protocolo fijado de antemano. Los apartados siguientes de "
        "este capítulo y los capítulos 4 a 6 las desarrollan; aquí se exponen con sus razones."
    )
    b.figura(FIGURA_PNG,
             "Figura 1.1: Enfoque del trabajo. Arriba, lo que es real (servidor, contenido y cliente) y lo que se "
             "emula (la red). En el centro, la interfaz común con los cuatro controladores clásicos, el "
             "controlador propio y sus tres variantes, y el entrenamiento fuera de línea del predictor. Abajo, la "
             "evaluación: protocolo fijado antes, experimento ejecutado una sola vez y paquete de evidencia del "
             "que salen los resultados del capítulo 6.")
    b.parrafo(
        "La primera decisión del trabajo es construir el entorno experimental completo en lugar de apoyarse en "
        "un reproductor existente. Los reproductores de referencia, como dash.js o Shaka Player, funcionan "
        "dentro de un navegador, entrelazan la adaptación con el resto de la lógica de reproducción y no "
        "ofrecen la telemetría por decisión ni el control del tiempo que exige una comparación reproducible "
        "(apartado 2.6). El cliente de este trabajo es un programa en Python que interpreta el manifiesto, "
        "descarga los segmentos de un servidor web real, mantiene el buffer, reproduce el contenido con un motor "
        "real o con uno simulado que respeta los mismos tiempos, y registra cada decisión con el estado que la "
        "produjo. Los controladores se conectan a una interfaz común y reciben exactamente la misma información: "
        "la escalera de calidades, el buffer y las medidas de las descargas ya hechas. Esa neutralidad del "
        "cliente respecto al controlador es una condición de diseño, no una consecuencia."
    )
    b.parrafo(
        "La segunda decisión es la fidelidad al medio. El contenido es vídeo real codificado con tasa variable "
        "en {0} calidades, de {1} a {2} kbit/s, troceado en segmentos de {3} s y servido por un servidor web "
        "real; el cliente pide y recibe los bytes de verdad, y el controlador dispone del tamaño real de cada "
        "segmento candidato, no de la tasa nominal. Lo que se emula es la red: el ancho de banda disponible se "
        "limita siguiendo trazas de redes reales, tomadas de conjuntos públicos y repartidas de modo que ninguna "
        "fuente de captura esté a la vez en los datos de entrenamiento y en los de evaluación. El mismo "
        "principio gobierna el entorno de entrenamiento del controlador propio, que simula sesiones completas "
        "con los tamaños reales de los segmentos para que lo aprendido fuera de línea siga valiendo dentro del "
        "cliente.".format(d["niveles"], d["min_kbps"], d["max_kbps"], d["seg_s"])
    )
    b.parrafo(
        "La tercera decisión es acotar el aprendizaje. El controlador propio no aprende la política de decisión "
        "de extremo a extremo, como hacen los métodos de aprendizaje por refuerzo [mao2017pensieve], sino solo "
        "la parte del problema que es genuinamente predictiva: un modelo neuronal estima varios cuantiles del "
        "ancho de banda de las próximas descargas a partir de las medidas recientes, y un planificador de "
        "control predictivo decide con ellos. El planificador recorre un horizonte de varios segmentos con los "
        "tamaños reales, evalúa cada plan en los escenarios de red que describen los cuantiles y elige el que "
        "optimiza una medida de riesgo que pondera más los escenarios desfavorables. La predicción se puede "
        "medir y calibrar por separado; la decisión queda explicable segmento a segmento, y la misma estructura "
        "permite construir variantes que quitan una pieza cada vez para medir lo que aporta. En el experimento "
        "final el controlador propio se compara con {0} controladores clásicos implementados según sus artículos "
        "y con {1} variantes de sí mismo: dos sustituyen el predictor neuronal por cuantiles calculados de las "
        "últimas descargas o por cuantiles fijos, y la tercera decide con la mediana de la predicción, sin la "
        "medida de riesgo.".format(d["n_clasicos"], d["n_variantes"])
    )
    b.parrafo(
        "La cuarta decisión es evaluar como en un ensayo prerregistrado. Antes de ejecutar el experimento se "
        "fijaron los controladores a comparar, las ventanas de red, los vídeos, las métricas, las hipótesis y "
        "las pruebas estadísticas con su corrección por comparaciones múltiples, y se congeló el código con sus "
        "huellas criptográficas. El experimento se ejecutó una sola vez, en una máquina virtual dedicada, y "
        "produjo un paquete de evidencia que cualquier lector puede verificar y con el que se rehacen las "
        "tablas y figuras de esta memoria. Las hipótesis se formularon para que un resultado negativo también "
        "fuera informativo, y la memoria da cuenta de lo que se cumplió y de lo que no."
    )
    b.parrafo(
        "De esas cuatro decisiones se derivan las aportaciones del trabajo. La primera es un instrumento: un "
        "cliente DASH y un banco de pruebas que permiten comparar cualquier controlador escrito contra la misma "
        "interfaz en condiciones idénticas de red y de contenido, con la telemetría necesaria para explicar cada "
        "decisión. La segunda es el controlador propio, con su predictor de cuantiles, su planificador con medida "
        "de riesgo y el entorno de entrenamiento fiel al medio que lo hace posible. La tercera es un método de "
        "evaluación, trasladado de los ensayos prerregistrados a la comparación de algoritmos de adaptación: "
        "hipótesis, métricas y pruebas fijadas antes, una sola ejecución y un paquete de evidencia que cualquiera "
        "puede verificar. La cuarta, menos habitual en un trabajo de este tipo, es el registro de las líneas que "
        "se intentaron y se descartaron durante el desarrollo, con las razones por las que no funcionaron, que el "
        "capítulo 7 recoge como resultados negativos."
    )

    # 1.4 ------------------------------------------------------------------------------------------------
    b.h2("1.4. Objetivos")
    b.parrafo(
        "El objetivo general del trabajo es diseñar, implementar y evaluar un controlador de adaptación de tasa "
        "que decida con la incertidumbre de la red y con las características reales del contenido, sobre un "
        "cliente DASH propio que permita compararlo de forma reproducible con los algoritmos de referencia. "
        "Ese objetivo se concreta en los cinco objetivos específicos siguientes, numerados para que el "
        "capítulo 7 pueda responder a cada uno."
    )
    b.lista([
        ("Objetivo 1",
         "Diseñar e implementar un cliente MPEG-DASH modular en Python que interprete el manifiesto, descargue "
         "los segmentos de un servidor real, gestione el buffer, reproduzca el contenido con un motor real y con "
         "uno simulado equivalente en tiempos, y registre una telemetría completa de cada sesión, sin favorecer "
         "a ningún controlador."),
        ("Objetivo 2",
         "Definir una interfaz común de controladores e implementar sobre ella, con fidelidad a sus artículos, "
         "los algoritmos clásicos de referencia: el basado en tasa, el basado en buffer, el basado en utilidad y "
         "el control predictivo robusto."),
        ("Objetivo 3",
         "Diseñar, entrenar e integrar un controlador propio que combine un predictor neuronal de cuantiles del "
         "ancho de banda con un planificador de control predictivo que use los tamaños reales de los segmentos "
         "y una medida de riesgo sobre los escenarios desfavorables, junto con un entorno de entrenamiento fiel "
         "al medio en que se va a usar."),
        ("Objetivo 4",
         "Construir un banco de evaluación reproducible: servidor y contenido DASH reales con tasa variable, "
         "emulación de red a partir de trazas reales con particiones sin fuga entre entrenamiento y evaluación, "
         "un protocolo con métricas, hipótesis y pruebas estadísticas fijadas antes de ejecutar, y un paquete de "
         "evidencia verificable."),
        ("Objetivo 5",
         "Evaluar el controlador propio frente a los algoritmos de referencia y frente a sus propias variantes "
         "en condiciones idénticas, contrastar las hipótesis prerregistradas y declarar con precisión qué se "
         "puede afirmar a partir de los resultados y qué no."),
    ])
    b.parrafo(
        "Los objetivos 1, 2 y 4 construyen el instrumento; el 3 construye la aportación, y el 5 la somete a "
        "prueba. Los tres primeros se corresponden con los capítulos 4 y 5, el cuarto con los capítulos 4, 5 y "
        "6, y el quinto con el capítulo 6."
    )

    # 1.5 ------------------------------------------------------------------------------------------------
    b.h2("1.5. Alcance")
    b.parrafo(
        "El trabajo se ciñe al vídeo bajo demanda: el contenido está codificado y segmentado de antemano y el "
        "manifiesto describe la sesión completa, de modo que quedan fuera el directo y la baja latencia, con sus "
        "problemas propios de generación de segmentos y de retardo extremo a extremo. El cliente reproduce una "
        "sola pista de vídeo, sin audio ni subtítulos, y gestiona una sola sesión a la vez; no se estudian la "
        "competencia entre varios clientes por el mismo enlace ni la interacción con redes de distribución de "
        "contenidos, que en el experimento se reducen a un servidor web en la red local. Las calidades "
        "disponibles son las {0} de la escalera descrita en el apartado 1.3, con segmentos de {1} s, que es el "
        "régimen habitual de los trabajos con los que se compara.".format(d["niveles"], d["seg_s"])
    )
    b.parrafo(
        "La red es emulada, no real. Las sesiones se ejecutan contra un servidor real con los bytes reales del "
        "contenido, pero el ancho de banda disponible lo impone una traza registrada en una red real, "
        "reproducida con la misma secuencia para todos los controladores. Eso hace la comparación repetible al "
        "precio de dejar fuera la reacción del transporte y del tráfico competidor a las decisiones del "
        "cliente, una limitación que se declara en el capítulo 6. La calidad de experiencia se mide con el "
        "modelo lineal más usado en la literatura, basado en la tasa binaria de cada segmento, las "
        "interrupciones y los cambios de calidad; no se usan métricas perceptuales que requieran decodificar el "
        "vídeo, ni se realizan estudios con usuarios. Por último, los controladores de referencia se implementan "
        "según sus artículos con sus parámetros publicados, sin ajustarlos al contenido ni a las trazas de este "
        "trabajo, de modo que la comparación mide la aportación de la predicción y del planificador, no la de "
        "una puesta a punto."
    )
    b.parrafo(
        "El trabajo entrega, además de esta memoria, el material necesario para auditarlo y repetirlo: el código "
        "del cliente, de los controladores, del modelo y de la evaluación, escrito en Python y documentado en "
        "castellano; el corpus de red, con el catálogo de trazas de {0} conjuntos públicos y sus particiones sin "
        "fuga; el modelo entrenado con las huellas de sus ficheros; el paquete de evidencia del experimento final, "
        "con la telemetría de cada sesión, los resultados y la verificación de su integridad; el contenido DASH tal "
        "como lo sirve el servidor; el conjunto de datos con que se entrenó el modelo, y los informes de hardware y "
        "software de cada máquina. Los anexos describen cómo se reproduce el experimento a partir de ese "
        "material.".format(d["n_conjuntos"])
    )

    # 1.6 ------------------------------------------------------------------------------------------------
    b.h2("1.6. Estructura de la memoria")
    b.parrafo("El resto de la memoria se organiza en seis capítulos, la bibliografía y los anexos.")
    b.lista([
        ("Capítulo 2",
         "revisa el estado del arte: el streaming adaptativo y el estándar MPEG-DASH, el problema de la "
         "adaptación de tasa, las familias de algoritmos que lo abordan con una tabla comparativa, los modelos de "
         "calidad de experiencia, los reproductores existentes y las lagunas que motivan este trabajo."),
        ("Capítulo 3",
         "describe la planificación del proyecto, con sus fases, cronograma, horas dedicadas y una estimación de "
         "costes con las hipótesis de cálculo declaradas."),
        ("Capítulo 4",
         "presenta el diseño del sistema: la vista global del cliente, el analizador del manifiesto, la descarga "
         "y el buffer, los motores de reproducción, la interfaz común de los controladores, la telemetría, las "
         "condiciones del experimento y la separación entre ejecución y evaluación."),
        ("Capítulo 5",
         "detalla la implementación: el lenguaje y las bibliotecas, el cliente, el analizador del manifiesto, el "
         "ejecutor de experimentos y su configuración, los controladores clásicos, el controlador propio y el "
         "entorno de entrenamiento."),
        ("Capítulo 6",
         "expone la evaluación: el diseño del experimento final, las métricas e hipótesis, la verificación de la "
         "integridad del paquete de evidencia, los resultados de las hipótesis prerregistradas, los descriptivos, "
         "el análisis exploratorio y la interpretación con sus limitaciones."),
        ("Capítulo 7",
         "recoge las conclusiones, objetivo a objetivo, los resultados negativos de las líneas descartadas durante "
         "el desarrollo y el trabajo futuro."),
        ("Anexos",
         "reúnen el material de apoyo: la reproducción del experimento a partir del paquete de evidencia, el "
         "manual de uso del cliente y la documentación complementaria a la que remite el texto."),
    ])
    b.parrafo(
        "Algunas convenciones se mantienen en toda la memoria. Los términos técnicos que la literatura y la "
        "práctica usan en inglés sin traducción asentada, como buffer, bitrate, throughput o QoE, se conservan y "
        "se explican la primera vez que aparecen; las siglas se expanden en su primer uso y se recogen en la lista "
        "de acrónimos del principio. Las figuras, tablas y ecuaciones se numeran por capítulo y se anuncian en el "
        "texto antes de aparecer. Las referencias bibliográficas se numeran por orden de aparición. Todas las "
        "cifras del capítulo 6 proceden del paquete de evidencia del experimento final y se recalculan a partir "
        "de él con los programas que acompañan a la memoria, de modo que cada tabla y cada figura se pueden "
        "regenerar desde los datos originales."
    )

    b.guardar(SALIDA)
    texto = " ".join(p.text for p in b.doc.paragraphs)
    citas = set()
    for grupo in re.findall(r"\[([A-Za-z][\w, ]*)\]", texto):
        citas.update(c.strip() for c in grupo.split(","))
    faltan = citas - claves
    assert not faltan, faltan
    # Sin resultados: ninguna cifra de QoE, p-valores ni recuentos del experimento.
    assert not re.search(r"\d,\d{2,3}\b", texto), "cifras con decimales en la introducción"
    assert "1208" not in texto and "41,3" not in texto
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("citas (%d):" % len(citas), sorted(citas))
    print("datos verificados:", d)


if __name__ == "__main__":
    main()
