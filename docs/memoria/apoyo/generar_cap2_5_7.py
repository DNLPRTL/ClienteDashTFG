# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap2_5_7_qoe_reproductores_lagunas.docx: apartados 2.5 (calidad de
experiencia), 2.6 (reproductores DASH existentes), 2.7 (lagunas que motivan el enfoque) y el cierre del capitulo 2
(parrafos sin epigrafe).

Capitulo bibliografico: las citas son claves del .bib, con su pagina en las notas. Los pesos de la QoE que se
mencionan se leen de core/evaluacion/qoe.py del entregable.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap2_5_7.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

CODIGO = Path(r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG")
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap2_5_7_qoe_reproductores_lagunas.docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"
sys.path.insert(0, str(CODIGO))


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from core.evaluacion.qoe import PESO_REBUFFERING_LINEAL, PESO_REBUFFERING_LOG
    assert PESO_REBUFFERING_LINEAL == 4.3 and PESO_REBUFFERING_LOG == 2.66
    claves = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))
    b = Borrador(PLANTILLA)

    b.h2("2.5. Calidad de experiencia: modelos y métricas")
    b.parrafo(
        "Todo algoritmo de adaptación optimiza algo, y ese algo es una medida de la calidad de experiencia, QoE "
        "por sus siglas en inglés: lo que el usuario percibe de la sesión, no lo que mide la red. El survey de "
        "Seufert et al. ordena los factores que influyen en la QoE del streaming adaptativo en tres grupos: el "
        "retardo de arranque, las paradas de la reproducción por vaciado del buffer y la adaptación de la "
        "calidad, con su nivel medio y la frecuencia y la amplitud de los cambios [seufert2015hasQoeSurvey]. "
        "De los tres, las paradas son el factor más dañino: los estudios que el survey recoge muestran que los "
        "usuarios prefieren un retardo inicial a una parada en una proporción cercana al 90 %, y que retardos "
        "iniciales de hasta 16 s se toleran mientras que una parada de pocos segundos degrada la valoración de "
        "forma clara [seufert2015hasQoeSurvey]. Los cambios de calidad importan menos que las paradas, pero "
        "los cambios frecuentes y de gran amplitud se perciben peor que una calidad constante algo inferior, "
        "y de ahí que todas las métricas penalicen la falta de suavidad."
    )
    b.parrafo(
        "Medir la QoE con usuarios es caro y lento, así que la práctica habitual es un modelo objetivo que "
        "combina los factores anteriores en una cifra. Barman y Martini revisan esos modelos y sus problemas "
        "abiertos, entre ellos la dependencia del contenido y la dificultad de validarlos fuera de la base de "
        "datos con la que se ajustaron [barman2019qoeModeling]. Duanmu et al. proponen un índice continuo en el "
        "tiempo que integra la calidad de presentación y las paradas con sus interacciones, en lugar de usar el "
        "bitrate y estadísticos globales de las paradas, y señalan que el mismo bitrate produce calidades muy "
        "distintas según el contenido [duanmu2017qoeIndex]. Zuo et al. añaden otra dimensión: los usuarios "
        "difieren en sus preferencias, y un algoritmo diseñado para un usuario medio no es óptimo para "
        "ninguno en particular [zuo2022ruyiPreferenceQoe]. Taraghi et al. contrastan con estudios objetivos y "
        "subjetivos los algoritmos heurísticos de los reproductores reales, basados en el buffer, en el "
        "throughput y predictivos, y muestran que el orden entre ellos depende de la métrica y del escenario "
        "[taraghi2021understandingQoe]."
    )
    b.parrafo(
        "Frente a esa variedad, la literatura de algoritmos de adaptación converge en una familia de métricas "
        "sencillas que suman por segmento una utilidad de la calidad, una penalización por los segundos de "
        "parada y una penalización por el cambio de utilidad entre segmentos consecutivos. Yin et al. la "
        "formularon para el MPC [yin2015mpc] y Pensieve fijó tres variantes con sus pesos: la lineal, cuya "
        "utilidad es el bitrate en Mbit/s y cuyo peso del rebuffering es {0}; la logarítmica, con utilidad "
        "logarítmica del bitrate y peso {1}; y una variante para alta definición [mao2017pensieve]. Este "
        "trabajo adopta la QoE lineal de Pensieve como métrica principal, con sus pesos exactos, por tres "
        "razones: es la métrica con la que se han comparado los algoritmos de las familias del apartado 2.4 "
        "desde 2017, de modo que los resultados quedan en una escala conocida; sus componentes son "
        "interpretables, porque el peso dice cuántos Mbit/s de bitrate cuesta un segundo de parada; y es la "
        "que se puede calcular con exactitud desde la telemetría del cliente, sin un modelo perceptual que "
        "exigiría decodificar el vídeo. La elección tiene un coste, que el apartado 6.7 declara: el bitrate es "
        "un sustituto de la calidad visual, no la calidad visual. Peroni y Gorinsky alertan además de que los "
        "modelos de QoE proliferan sin consenso y de que el orden entre algoritmos puede cambiar con el modelo "
        "elegido, y recomiendan informar las componentes y las distribuciones y no solo las medias "
        "[peroni2024qoePitfalls]; la evaluación del capítulo 6 sigue esa recomendación.".format(
            coma(PESO_REBUFFERING_LINEAL, 1), coma(PESO_REBUFFERING_LOG, 2))
    )

    b.h2("2.6. Reproductores DASH existentes")
    b.parrafo(
        "Existen reproductores DASH maduros y de código abierto, y conviene decir por qué este trabajo "
        "construye el suyo en lugar de usarlos. El reproductor de referencia del DASH Industry Forum, dash.js, "
        "es una biblioteca JavaScript que se ejecuta en el navegador sobre las extensiones de fuente "
        "multimedia, implementa el estándar y los puntos de interoperabilidad y sirve de banco de pruebas a la "
        "propia comunidad [dashjsRefClient]; Spiteri et al. desarrollaron sobre él los algoritmos BOLA-E y "
        "DYNAMIC, que hoy forman parte del reproductor y se usan en producción, con un simulador propio para "
        "diseñarlos [spiteri2019dashjs]. Shaka Player, de Google, es otra biblioteca JavaScript que reproduce "
        "DASH y HLS en el navegador con un algoritmo de adaptación basado en el throughput [shakaPlayer]. GPAC, "
        "con su herramienta MP4Box, es el conjunto de utilidades de código abierto con el que se empaqueta "
        "contenido DASH y que incluye también un reproductor [gpacMp4boxWiki]; es la herramienta que genera el "
        "contenido de este trabajo (apartado 4.7)."
    )
    b.parrafo(
        "Ninguno de los tres sirve como banco experimental controlado para comparar algoritmos de adaptación. "
        "Los dos reproductores web viven dentro de un navegador, que impone su propia pila de red, su "
        "planificación de hilos y su decodificación, de modo que la temporalidad de una descarga depende de "
        "factores que el experimentador no controla ni registra; sus algoritmos de adaptación están "
        "entrelazados con el resto del reproductor, así que añadir un controlador externo, y más uno con un "
        "modelo neuronal en Python, exige modificar la biblioteca; y su telemetría no está pensada para "
        "reconstruir cada decisión con la realimentación exacta que la produjo. Lo que este trabajo necesita "
        "es lo contrario: un cliente en el que la red se pueda emular de forma determinista con trazas reales, "
        "la interfaz del controlador sea un contrato explícito e intercambiable, cada decisión quede registrada "
        "con todo lo que el controlador vio, y las 1208 sesiones del experimento se ejecuten sin intervención "
        "y con el mismo entorno. Esa es la justificación del cliente propio del capítulo 4, que renuncia a la "
        "generalidad de un reproductor de producción a cambio de control y reproducibilidad, y que se apoya en "
        "las mismas herramientas de empaquetado que los reproductores anteriores."
    )

    b.h2("2.7. Lagunas que motivan el enfoque")
    b.parrafo(
        "La revisión anterior deja tres lagunas que la literatura reciente señala de forma insistente y que "
        "este trabajo toma como punto de partida. La primera es la distancia entre el simulador y la realidad. "
        "Yan et al. mostraron en Puffer, con usuarios reales durante meses, que algoritmos con excelentes "
        "resultados en simuladores y emuladores no los mantenían en la red real, y atribuyeron parte de la "
        "diferencia a que los simuladores con trazas reproducen mal la dinámica real de la red [yan2020puffer]. "
        "Hoffman et al. fueron más lejos: incluso las pruebas en despliegues reales generalizan mal, porque "
        "cada plataforma cubre una región geográfica y un conjunto de usuarios estrechos y afectados por sesgo "
        "de supervivencia [hoffman2025intoTheWildABR]. Alomar et al. identificaron una causa concreta del "
        "problema: las trazas se recogen bajo una política de adaptación concreta y llevan impresa su huella, de "
        "modo que simular otra política sobre ellas introduce un sesgo, y propusieron CausalSim para corregirlo "
        "con un marco causal [alomar2023causalsim]; Bothra et al. abordaron la misma pregunta, qué pasaría con "
        "otro algoritmo a partir de las trazas de uno solo, sin ensayos aleatorizados [bothra2023veritas]."
    )
    b.parrafo(
        "La segunda laguna es la generalización y la fiabilidad de las políticas aprendidas. Las revisiones "
        "recientes de los métodos con aprendizaje coinciden en los problemas abiertos: generalizar fuera de las "
        "redes de entrenamiento, interpretar y acotar lo que la política hace, y desplegarla con garantías "
        "[amer2025learningReview]; las revisiones generales del streaming adaptativo sitúan además esos "
        "problemas en un contexto de redes y contenidos cada vez más variados [timmerer2025hasReview, "
        "alsader2025qoeDriven6g, peroni2025pipelineSurvey]. La tercera laguna es el tratamiento del riesgo: la "
        "mayor parte de los algoritmos, aprendidos o no, optimizan la calidad media, y una métrica media "
        "esconde las sesiones malas; los trabajos de la familia de la incertidumbre del apartado 2.4 "
        "[kan2021bayesmpc, xie2026safesabr] y las guías de evaluación [peroni2024qoePitfalls] reclaman decidir y "
        "evaluar con la distribución, no solo con la media."
    )
    b.parrafo(
        "Este trabajo responde a las tres lagunas con tres decisiones que estructuran los capítulos "
        "siguientes. Frente a la distancia simulador-realidad, fidelidad al medio: el contenido es real, con los "
        "tamaños reales de cada segmento, servido por un servidor web real y descargado por un cliente real; lo "
        "único emulado es la temporalidad de la red, reproducida con trazas reales, y el mismo entorno, con la "
        "misma física, se usa para entrenar el predictor y para evaluarlo, de modo que lo aprendido en el "
        "entrenamiento sea lo que se encuentra en la evaluación (apartados 4.7 y 5.7). Frente a la "
        "generalización y la fiabilidad, aprendizaje acotado: la red neuronal predice el throughput, que es "
        "una magnitud medible y calibrable, y no la decisión; la decisión la toma un planificador explícito "
        "con un respaldo clásico, cuyas acciones se pueden auditar una a una (apartado 5.6). Frente al riesgo, "
        "una decisión que cuenta con la incertidumbre y una evaluación que la mide: el planificador promedia "
        "los escenarios desfavorables de la predicción, y el experimento prerregistra hipótesis de "
        "equivalencia en calidad y de superioridad en paradas, e informa distribuciones y estratos, no solo "
        "medias (capítulo 6). La emulación con trazas conserva, con todo, una de las limitaciones señaladas: "
        "no reproduce la pila TCP ni el tráfico competidor, y las trazas llevan la huella de la política con que "
        "se recogieron; el apartado 6.7 lo declara."
    )

    # Cierre del capitulo, sin epigrafe (biblia 6.3).
    b.parrafo(
        "Este capítulo ha situado el trabajo en su contexto. El streaming adaptativo sobre HTTP trasladó el "
        "control de la sesión al cliente y MPEG-DASH normalizó el manifiesto y los segmentos dejando libre la "
        "decisión de adaptación, que es un problema de control con objetivos en conflicto e información "
        "incompleta sobre el futuro (apartados 2.1 a 2.3). Las familias de algoritmos se distinguen por la señal "
        "que observan y por cómo tratan la incertidumbre, desde las reglas sobre el throughput o el buffer hasta "
        "el control predictivo, las políticas aprendidas y los métodos que incorporan el riesgo, entre los que "
        "se sitúa este trabajo (apartado 2.4). La calidad de experiencia se mide con una métrica lineal de "
        "bitrate, paradas y suavidad, adoptada por ser la de la literatura con la que se compara y declarada "
        "como sustituto de la calidad visual (apartado 2.5)."
    )
    b.parrafo(
        "Los reproductores existentes no ofrecen el control ni la trazabilidad que exige una comparación "
        "rigurosa, lo que justifica el cliente propio (apartado 2.6), y la literatura reciente deja tres "
        "lagunas, la distancia entre simulador y realidad, la generalización de lo aprendido y el tratamiento "
        "del riesgo, a las que este trabajo responde con fidelidad al medio, aprendizaje acotado a la "
        "predicción y una decisión y una evaluación que cuentan con la incertidumbre (apartado 2.7). El "
        "capítulo 3 describe cómo se planificó y qué costó llevar esas decisiones a la práctica, antes de que "
        "los capítulos 4 y 5 presenten el diseño y la implementación."
    )

    b.guardar(SALIDA)
    texto = " ".join(p.text for p in b.doc.paragraphs)
    citas = set(c.strip() for grupo in re.findall(r"\[([A-Za-z][\w, ]*)\]", texto) for c in grupo.split(","))
    assert not (citas - claves), citas - claves
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("citas:", len(citas), sorted(citas))


if __name__ == "__main__":
    main()
