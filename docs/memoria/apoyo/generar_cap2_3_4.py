# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap2_3_4_problema_familias.docx: apartados 2.3 (el problema de la
adaptacion de tasa) y 2.4 (familias de algoritmos, con la Tabla 2.1).

Capitulo bibliografico: las citas son claves del .bib y cada afirmacion atribuida lleva su pagina en las notas
(notas_cap2_3_4_problema_familias.md). El script comprueba que todas las claves existen en el .bib.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap2_3_4.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap2_3_4_problema_familias.docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    claves = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))
    b = Borrador(PLANTILLA)

    b.h2("2.3. El problema de la adaptación de tasa")
    b.parrafo(
        "Con el contenido troceado y el control en el cliente, la pregunta que queda es cuál de las "
        "representaciones pedir para cada segmento. Es el problema de la adaptación de tasa, ABR por sus siglas "
        "en inglés (Adaptive Bitrate). Yin et al. lo formularon como un problema de control con cuatro "
        "objetivos en conflicto: maximizar la calidad, que crece con la tasa del nivel elegido; evitar las "
        "paradas de la reproducción, que ocurren cuando el buffer se vacía; limitar el retardo de arranque; y "
        "mantener la reproducción suave, sin cambios de nivel frecuentes o bruscos [yin2015mpc]. Elegir "
        "siempre el nivel más bajo evita las paradas pero desperdicia la red; elegir el más alto aprovecha la "
        "red pero vacía el buffer en cuanto esta cae; y seguir la red paso a paso produce un vídeo que cambia "
        "de calidad a cada segmento. La calidad de experiencia del apartado 2.5 pondera esos objetivos en una "
        "sola cifra, y el algoritmo de adaptación intenta maximizarla."
    )
    b.parrafo(
        "Lo que hace difícil el problema es la información disponible. En el momento de decidir, el cliente "
        "conoce el pasado y el presente: cuánto tardaron las últimas descargas y, por tanto, qué throughput "
        "obtuvo, cuántos segundos de vídeo tiene en el buffer, qué nivel acaba de reproducir y, si lee el "
        "manifiesto o un índice, cuántos bytes tiene cada segmento candidato. Lo que no conoce es el futuro: "
        "el throughput durante la próxima descarga, que es justo lo que determina si el segmento llegará antes "
        "de que el buffer se agote. Toda decisión es, por tanto, una apuesta sobre la red de los próximos "
        "segundos hecha con medidas de los segundos anteriores, y el buffer es el margen que absorbe los "
        "errores de esa apuesta. Las familias del apartado siguiente se distinguen por cómo hacen la apuesta: "
        "qué señal observan, si predicen o no el throughput, cuántos segmentos miran hacia delante y cómo "
        "tratan la incertidumbre de la predicción."
    )
    b.parrafo(
        "Dos rasgos del problema importan especialmente a este trabajo. El primero es el horizonte: la decisión "
        "sobre un segmento condiciona el buffer con el que se decidirá el siguiente, así que un algoritmo que "
        "solo mira el segmento actual puede meterse en un callejón del que luego no sale sin parar; mirar "
        "varios segmentos hacia delante, como hace el control predictivo, requiere predecir el throughput en "
        "ese horizonte y asumir el error de la predicción [yin2015mpc]. El segundo es el tamaño real de los "
        "segmentos: con codificación de tasa variable, el tiempo de descarga de un segmento depende de sus "
        "bytes y no de la tasa nominal de su nivel, de modo que un algoritmo que planifica con la tasa nominal "
        "se equivoca de forma sistemática en las escenas complejas (apartado 2.2). La forma de incorporar la "
        "incertidumbre del futuro y la física real del contenido en la decisión es, en síntesis, la aportación "
        "del controlador del capítulo 5."
    )

    b.h2("2.4. Familias de algoritmos de adaptación")
    b.parrafo(
        "La literatura sobre algoritmos de adaptación es extensa. El survey de Bentaleb et al. la organiza por "
        "dónde se toma la decisión, en el cliente, en el servidor o en la red, y distingue cinco clases de "
        "algoritmos de cliente: los basados en el ancho de banda disponible, los basados en el buffer, los "
        "mixtos, las soluciones propietarias y los basados en procesos de decisión de Markov [bentaleb2019survey]. "
        "Este apartado sigue esa organización, por la señal que gobierna la decisión, para los algoritmos de cliente, que "
        "son los que se comparan en el capítulo 6, y la extiende con las familias posteriores al survey: el "
        "aprendizaje por refuerzo, los métodos que buscan generalizar fuera de las redes de entrenamiento y los "
        "que incorporan la incertidumbre o el riesgo en la decisión. De cada familia se da la idea, la señal que "
        "usa, lo que aporta y lo que limita, con un representante; la Tabla 2.1 resume la comparación. Los "
        "cuatro algoritmos que el capítulo 5 implementa como comparadores son el representante de su familia."
    )

    b.h3("2.4.1. Basados en el throughput")
    b.parrafo(
        "La familia más antigua estima el throughput disponible a partir de las últimas descargas y elige el "
        "nivel más alto cuya tasa quepa en esa estimación, con algún margen de seguridad. Liu et al. comparan el "
        "tiempo que tardó en descargarse el último segmento con la duración de vídeo que contiene: si la "
        "descarga fue claramente más rápida que la reproducción hay capacidad sobrante y se sube un nivel; si "
        "fue más lenta se baja de forma agresiva, varios niveles de golpe si hace falta, para proteger el "
        "buffer [liu2011rateAdaptation]. La idea es simple y reacciona rápido, pero la estimación es ruidosa, "
        "porque una sola descarga dice poco de la red, y el algoritmo tiende a oscilar cuando el throughput "
        "fluctúa alrededor de la frontera entre dos niveles; además ignora el buffer, así que no distingue una "
        "caída de la red con el buffer lleno de otra con el buffer vacío. Es el comparador basado en tasa del "
        "capítulo 5."
    )

    b.h3("2.4.2. Basados en el buffer")
    b.parrafo(
        "La segunda familia invierte el punto de vista: en lugar de predecir la red, observa el buffer, que "
        "integra el pasado de la red y del propio algoritmo. Huang et al. propusieron BBA con un argumento "
        "directo: el objetivo es no vaciar el buffer y no llenarlo en exceso, así que basta con una función que "
        "asigne a cada ocupación del buffer un nivel, con una zona baja de reserva en la que se pide siempre el "
        "nivel mínimo, una zona intermedia en la que el nivel crece con la ocupación y una zona alta en la que "
        "se pide el máximo [huang2014bba]. Spiteri et al. dieron a la misma idea un fundamento formal con BOLA, "
        "que plantea la adaptación como la maximización de una utilidad, la calidad menos una penalización por "
        "rebuffering, y la resuelve con optimización de Lyapunov; el resultado es también una regla de decisión "
        "en función del buffer, con una garantía de que la utilidad obtenida queda a una distancia acotada de "
        "la óptima [spiteri2020bola]. Los algoritmos basados en el buffer son estables y no dependen de una "
        "predicción, pero reaccionan tarde: el buffer se entera de una caída de la red cuando ya se ha vaciado "
        "en parte, y en el arranque, con el buffer vacío, no tienen información. BBA y BOLA son los otros dos "
        "comparadores clásicos del capítulo 5."
    )

    b.h3("2.4.3. Control predictivo")
    b.parrafo(
        "Yin et al. unificaron las dos señales en un marco de control predictivo basado en modelo, MPC por sus "
        "siglas en inglés: el algoritmo predice el throughput de los próximos segmentos, simula con un modelo "
        "del buffer qué pasaría con cada secuencia posible de niveles en ese horizonte y elige la primera "
        "decisión de la secuencia que maximiza la calidad de experiencia; en el segmento siguiente repite el "
        "cálculo con la información nueva [yin2015mpc]. El marco es general y optimiza directamente el "
        "objetivo, pero depende de la predicción, y los propios autores mostraron que los errores de predicción "
        "degradan el resultado. Su variante robusta rebaja la predicción con el mayor error relativo cometido "
        "en las últimas descargas, de modo que el planificador cuenta con un throughput pesimista cuando la red "
        "ha sido imprevisible; es la forma de referencia que la literatura posterior usa como comparador fuerte "
        "y la que el capítulo 5 implementa como MPC robusto. Sus límites son los de una predicción puntual: "
        "un único valor no dice cuánto puede variar la red, y el rebaje por el error máximo es el mismo con una "
        "red estable que con una que acaba de caer."
    )

    b.h3("2.4.4. Ajuste automático de parámetros")
    b.parrafo(
        "Los algoritmos anteriores tienen parámetros, como el margen de seguridad, los umbrales del buffer o "
        "el peso de la penalización, que se fijan a mano y funcionan mejor en unas redes que en otras. Akhtar "
        "et al. observaron que el mejor valor de esos parámetros depende del estado de la red, caracterizado "
        "por la media y la desviación típica del throughput, y propusieron Oboe: calcular fuera de línea la "
        "mejor configuración para cada estado de red y, en tiempo de ejecución, detectar el estado y cambiar "
        "los parámetros del algoritmo subyacente [akhtar2018oboe]. Oboe mejora a BOLA y a MPC sin cambiar su "
        "lógica, lo que muestra cuánto pesa el ajuste en la comparación entre algoritmos; a cambio, exige un "
        "banco de redes representativo para la fase de ajuste y hereda las limitaciones del algoritmo al que "
        "ajusta. Las trazas que publicaron son uno de los dos orígenes de las ventanas del experimento de este "
        "trabajo (apartado 6.1)."
    )

    b.h3("2.4.5. Aprendizaje por refuerzo")
    b.parrafo(
        "Mao et al. propusieron con Pensieve sustituir las reglas por una red neuronal que aprende la política "
        "de adaptación por refuerzo: la red recibe las últimas medidas de throughput y de tiempo de descarga, "
        "el buffer, los tamaños de los segmentos candidatos y los segmentos restantes, y se entrena con el "
        "algoritmo actor-crítico A3C en un simulador que reproduce trazas de red, con la calidad de experiencia "
        "como recompensa [mao2017pensieve]. Pensieve superó a los algoritmos anteriores en su evaluación y "
        "generalizó razonablemente a redes no vistas, y fijó además la escalera, los pesos de la calidad de "
        "experiencia y el filtro de trazas que buena parte de la literatura posterior, y este trabajo, "
        "reutilizan. Sus límites abrieron las líneas siguientes: la política aprendida es opaca y difícil de "
        "acotar, el entrenamiento por refuerzo es costoso y sensible, y lo aprendido en el simulador no "
        "siempre se traslada a la red real. Huang et al. redujeron el coste de entrenamiento con Comyco, que "
        "en lugar de explorar imita las trayectorias de un experto que conoce el futuro de la red, con una "
        "recompensa consciente de la calidad visual [huang2020comyco]. Patel et al. llevaron el refuerzo a "
        "producción con Gelato, entrenado con un simulador de alta fidelidad y desplegado durante meses en la "
        "plataforma Puffer, con más de 280 000 usuarios [patel2024gelato]."
    )

    b.h3("2.4.6. Generalización fuera del entrenamiento")
    b.parrafo(
        "Que una política aprendida funcione en redes distintas de las del entrenamiento es el problema "
        "central de la familia anterior, y varios trabajos lo atacan de frente. Kan et al. aplicaron "
        "aprendizaje por refuerzo meta con MERINA, que aprende una política capaz de adaptarse con pocas "
        "muestras a una red nueva [kan2022merina]; Huang et al. siguieron la misma vía con A2BR, que aprende "
        "fuera de línea una política inicial sobre redes variadas y la ajusta en línea a la red y a las "
        "preferencias de cada usuario, con mejor comportamiento en entornos no vistos [huang2022a2br]. Son respuestas al mismo diagnóstico: la distribución de "
        "redes del entrenamiento no cubre la del despliegue. Este trabajo comparte el diagnóstico y toma otro "
        "camino: no aprende la política, sino solo la predicción del throughput, y deja la decisión a un "
        "planificador explícito que se puede acotar y auditar."
    )

    b.h3("2.4.7. Incertidumbre y riesgo en la decisión")
    b.parrafo(
        "La última familia es la más cercana a este trabajo. Parte de que la predicción del throughput es "
        "incierta y de que esa incertidumbre debe entrar en la decisión, no solo su valor esperado. Yan et al. "
        "mostraron con Puffer, una plataforma de televisión en directo con usuarios reales, que los algoritmos "
        "que destacaban en simuladores no lo hacían en la red real, y propusieron Fugu: un predictor "
        "supervisado del tiempo de transmisión de cada segmento, entrenado en el propio despliegue, que "
        "produce una distribución de probabilidad y alimenta un planificador MPC [yan2020puffer]. Es el "
        "paradigma de predictor probabilístico más control explícito que este trabajo adopta. Kan et al. "
        "fueron un paso más allá con una red neuronal bayesiana que separa la incertidumbre de los datos de "
        "la del modelo y entrega al MPC una región de confianza del throughput, con la que el planificador "
        "decide por el peor caso dentro de la región [kan2021bayesmpc]. Chen et al. tomaron otro camino con "
        "SODA, un controlador sin redes neuronales que formula la adaptación como optimización convexa en "
        "línea suavizada y garantiza una calidad consistente en el tiempo, como contrapunto a los métodos "
        "aprendidos [chen2024soda]. Y, en el extremo más reciente, SafeSABR plantea la adaptación en redes "
        "satelitales como un compromiso explícito entre la calidad media y el riesgo de eventos graves, con la "
        "calibración del riesgo como objetivo [xie2026safesabr]. El controlador de este trabajo se sitúa en "
        "esta familia: predice cuantiles del throughput con un conjunto de redes recurrentes, ensancha la "
        "predicción con el desacuerdo entre ellas y planifica promediando los escenarios desfavorables, con el "
        "valor en riesgo condicional como criterio (apartado 5.6). Frente a la región de confianza y al peor "
        "caso, la agregación de riesgo permite graduar la prudencia; frente a la mediana sola, la paga en "
        "paradas evitadas, como mide el capítulo 6."
    )

    b.tabla(
        ["Familia", "Idea", "Señal que usa", "Aporta", "Limita", "Ejemplo"],
        [
            ("Basados en el throughput", "elegir el nivel que cabe en el throughput estimado", "últimas descargas",
             "simple, reacciona rápido", "estimación ruidosa, oscila, ignora el buffer", "basado en tasa [liu2011rateAdaptation]"),
            ("Basados en el buffer", "nivel en función de la ocupación del buffer", "buffer",
             "estable, sin predicción, con garantías (BOLA)", "reacciona tarde, sin información en el arranque", "BBA [huang2014bba], BOLA [spiteri2020bola]"),
            ("Control predictivo", "predecir y optimizar la QoE en un horizonte con un modelo del buffer", "throughput y buffer",
             "optimiza el objetivo, general", "depende de una predicción puntual", "MPC y MPC robusto [yin2015mpc]"),
            ("Ajuste automático", "parámetros del algoritmo según el estado de la red", "media y variación del throughput",
             "mejora sin cambiar la lógica", "banco de ajuste; hereda los límites", "Oboe [akhtar2018oboe]"),
            ("Aprendizaje por refuerzo", "política aprendida de la QoE como recompensa", "throughput, buffer, tamaños",
             "sin reglas a mano, buen resultado medio", "opaca, entrenamiento costoso, salto simulador-realidad", "Pensieve [mao2017pensieve], Comyco [huang2020comyco]"),
            ("Generalización", "aprender a adaptarse a redes no vistas (aprendizaje meta)", "las del refuerzo",
             "menos degradación fuera del entrenamiento", "misma opacidad; coste", "MERINA [kan2022merina], A2BR [huang2022a2br]"),
            ("Incertidumbre y riesgo", "predicción probabilística y decisión que cuenta con ella", "distribución del throughput y buffer",
             "prudencia graduable, auditable", "más conservador en redes estables", "Fugu [yan2020puffer], MPC bayesiano [kan2021bayesmpc], este trabajo"),
        ],
        "Tabla 2.1: Familias de algoritmos de adaptación de tasa en el cliente: idea, señal que gobierna la "
        "decisión, lo que aportan, lo que las limita y un representante. Las cuatro primeras filas incluyen los "
        "comparadores del capítulo 5; la última, el controlador propio.",
        anchos_cm=[2.9, 3.1, 2.4, 2.6, 2.6, 2.4],
    )
    b.parrafo(
        "La Tabla 2.1 deja ver el hilo del capítulo. Las familias clásicas se distinguen por la señal: el "
        "throughput reacciona rápido y mal, el buffer reacciona bien y tarde, y el control predictivo combina "
        "ambas a costa de depender de una predicción. Las familias aprendidas sustituyen las reglas por una "
        "política entrenada y ganan en resultado medio lo que pierden en transparencia y en garantía fuera del "
        "entrenamiento. La familia de la incertidumbre vuelve al control explícito y pone el aprendizaje donde "
        "es más útil y menos peligroso, en la predicción, cuya calidad se puede medir y calibrar. Es la "
        "posición de este trabajo, y los apartados 2.5 y 2.7 añaden las dos piezas que faltan para justificarla: "
        "qué se entiende por calidad de experiencia y por qué los resultados de simulador no bastan."
    )

    b.guardar(SALIDA)
    texto = " ".join(p.text for p in b.doc.paragraphs) + " " + " ".join(c.text for t in b.doc.tables for r in t.rows for c in r.cells)
    citas = set(re.findall(r"\[([A-Za-z][\w]*)\]", texto))
    assert not (citas - claves), citas - claves
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("citas:", len(citas), sorted(citas))


if __name__ == "__main__":
    main()
