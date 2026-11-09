# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap2_1_2_has_dash.docx: apertura del capitulo 2 y apartados 2.1
(streaming adaptativo sobre HTTP, con los antecedentes locales) y 2.2 (MPEG-DASH, MPD y segmentacion).

Capitulo bibliografico: no hay recuentos del paquete. Las citas son claves del .bib y cada afirmacion
atribuida tiene su pagina en las notas (notas_cap2_1_2_has_dash.md). Los unicos datos del proyecto que se
mencionan (escalera de 6 niveles, segmentos de 4 s) se leen del MPD entregado para no escribirlos a mano.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap2_1_2.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
MPD = TFG_MATERIAL / "05_contenido_dash" / "Paseo_Almunecar_10min_30fps" / "4sec" / "Paseo_Almunecar_10min_30fps_simple_4s.mpd"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap2_1_2_has_dash.docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    mpd = MPD.read_text(encoding="utf-8")
    anchos = sorted(int(b) // 1000 for b in re.findall(r'bandwidth="(\d+)"', mpd))
    assert anchos == [300, 750, 1200, 1850, 2850, 4300]
    ts, dur = int(re.search(r'timescale="(\d+)"', mpd).group(1)), int(re.search(r' duration="(\d+)"', mpd).group(1))
    assert dur / ts == 4.0 and 'profiles="urn:mpeg:dash:profile:isoff-live:2011"' in mpd and "$Number$" in mpd
    claves = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))

    b = Borrador(PLANTILLA)
    b.capitulo(2, "Estado del arte")
    b.parrafo(
        "El capítulo 1 ha planteado el problema: decidir, segmento a segmento, qué calidad de vídeo pedir "
        "cuando la red cambia y el futuro no se conoce. Este capítulo revisa el contexto técnico y científico "
        "en el que se sitúa esa decisión. Los apartados 2.1 y 2.2 presentan el streaming adaptativo sobre HTTP "
        "y el estándar MPEG-DASH que lo normaliza, con la terminología que usa el resto de la memoria. El 2.3 "
        "formula el problema de la adaptación de tasa y el 2.4 recorre las familias de algoritmos que lo "
        "abordan, de los heurísticos clásicos al aprendizaje por refuerzo, con una tabla comparativa. El 2.5 "
        "trata la calidad de experiencia y sus modelos, el 2.6 los reproductores existentes y el 2.7 reúne las "
        "lagunas que la literatura reciente señala y que motivan el enfoque de este trabajo."
    )

    b.h2("2.1. Streaming adaptativo sobre HTTP")
    b.parrafo(
        "El vídeo es, desde hace más de una década, la mayor parte del tráfico de Internet. El survey de "
        "Seufert et al. recogía ya en 2015 que el vídeo suponía más de la mitad del tráfico de consumo "
        "[seufert2015hasQoeSurvey], y la revisión reciente de Timmerer et al. sitúa esa fracción en más de la "
        "mitad del tráfico global [timmerer2025hasReview]. La forma dominante de distribuir ese vídeo bajo "
        "demanda es el streaming adaptativo sobre HTTP, conocido por sus siglas en inglés HAS (HTTP Adaptive "
        "Streaming): el contenido se codifica en varias versiones de distinta calidad y tasa binaria, cada "
        "versión se trocea en segmentos de unos pocos segundos y el cliente los descarga uno a uno con "
        "peticiones HTTP ordinarias, eligiendo en cada segmento la versión que mejor se ajusta a la red que "
        "observa. La inteligencia está en el cliente; el servidor es un servidor web."
    )
    b.parrafo(
        "Stockhammer resumió en 2011 los principios de diseño que llevaron a esa arquitectura "
        "[stockhammer2011dash]. La alternativa anterior, la descarga progresiva de un único fichero, "
        "aprovechaba ya la infraestructura web pero no podía cambiar de calidad durante la reproducción ni "
        "evitar descargar vídeo que el usuario no llegaría a ver; los protocolos de streaming con estado, por "
        "su parte, exigían servidores especializados y tropezaban con cortafuegos y traducción de direcciones. "
        "HTTP resolvía ambas cosas: es un protocolo sin estado, atraviesa los cortafuegos y la traducción de "
        "direcciones, y permite servir el contenido desde servidores y cachés web estándar y, por tanto, desde "
        "las redes de distribución de contenidos ya desplegadas, de modo que escalar a muchos clientes no exige "
        "más que añadir cachés. A cambio, el control de la sesión pasa entero al cliente, que decide cuándo pedir "
        "cada segmento y a qué tasa, mientras el servidor se limita a responder peticiones. Esa decisión del "
        "cliente es el problema de adaptación de tasa del apartado 2.3."
    )
    b.parrafo(
        "La tecnología llegó al mercado con tres soluciones propietarias e incompatibles entre sí: Smooth "
        "Streaming de Microsoft en 2008, HTTP Live Streaming de Apple en 2009 y HTTP Dynamic Streaming de "
        "Adobe en 2010, que compartían el mismo principio de funcionamiento con distintos formatos de fichero "
        "y de índice [seufert2015hasQoeSurvey]. La normalización empezó en el 3GPP en 2009 y culminó en MPEG "
        "con el estándar DASH, publicado en 2012 y descrito en el apartado 2.2. Desde entonces la evolución se "
        "ha concentrado en el contenido y en la entrega más que en el principio: el formato común CMAF "
        "armoniza los segmentos de HLS y DASH sobre el formato ISO de fichero multimedia y habilita el "
        "streaming en directo de baja latencia, la codificación por título ajusta la escalera de calidades a "
        "cada contenido, y los reproductores web implementan la adaptación en JavaScript sobre las extensiones "
        "de fuente multimedia de los navegadores [timmerer2025hasReview]. Peroni y Gorinsky describen el "
        "conjunto como una cadena de mejor esfuerzo, de la compresión y la transcodificación a la entrega por "
        "redes de distribución y a la calidad que percibe el usuario, en la que la adaptación de tasa es un "
        "eslabón entre otros [peroni2025pipelineSurvey]."
    )
    b.parrafo(
        "En el entorno de la Universidad de Granada, el grupo del tutor de este trabajo estudió el tráfico de "
        "vídeo en la época anterior a la generalización del streaming adaptativo. Ameigeiras et al. "
        "caracterizaron y modelaron el tráfico de YouTube, entonces servido por descarga progresiva: el "
        "servidor enviaba una ráfaga inicial de unos 40 s de vídeo y después limitaba la tasa de envío a un "
        "múltiplo de la tasa de codificación, de modo que una reducción del ancho de banda disponible se "
        "traducía en interrupciones de la reproducción [ameigeiras2012youtubeTraffic]. Ramos-Muñoz et al. "
        "extendieron el estudio a terminales móviles y encontraron que el comportamiento dependía del "
        "terminal: los dispositivos Android de gama alta aplicaban una política de doble umbral que "
        "interrumpía y reanudaba la descarga según la ocupación del buffer, mientras que en iOS la descarga no "
        "se interrumpía [ramosMunoz2014mobileYoutube]. Esos trabajos muestran el problema que el streaming "
        "adaptativo vino a resolver, la dependencia de la experiencia respecto de un ancho de banda que varía y "
        "de políticas de buffer fijas en el cliente, y son el antecedente local del interés de este trabajo por "
        "los mecanismos de adaptación en el cliente."
    )

    b.h2("2.2. MPEG-DASH: manifiesto, segmentos y perfiles")
    b.parrafo(
        "MPEG-DASH, Dynamic Adaptive Streaming over HTTP, es el estándar ISO/IEC 23009-1 que normaliza el "
        "streaming adaptativo [iso23009_1_2022]. El estándar define dos cosas y deja fuera una tercera: define "
        "el formato del manifiesto, llamado descripción de la presentación multimedia o MPD (Media "
        "Presentation Description), y el formato de los segmentos; no define cómo debe decidir el cliente qué "
        "segmento pedir. Esa separación es la que permite que existan reproductores y algoritmos de "
        "adaptación distintos sobre el mismo contenido, y es la que hace posible este trabajo: el cliente del "
        "capítulo 4 implementa la parte normalizada y deja la decisión a un controlador intercambiable."
    )
    b.parrafo(
        "El MPD es un documento XML con un modelo de datos jerárquico. En el eje temporal, la presentación "
        "se divide en periodos; dentro de un periodo, el contenido se organiza en conjuntos de adaptación, "
        "uno por componente, como el vídeo principal o el audio principal; cada conjunto de adaptación agrupa "
        "representaciones, que son versiones codificadas del mismo contenido perceptualmente equivalentes, "
        "entre las que el cliente puede cambiar en cualquier frontera de segmento sin que la reproducción se "
        "interrumpa; y cada representación se compone de un segmento de inicialización, con los parámetros "
        "del decodificador, y una secuencia de segmentos multimedia [iso23009_1_2022]. Las representaciones de "
        "un conjunto de adaptación de vídeo forman la escalera de calidades: en el contenido principal de este "
        "trabajo son {0} representaciones, de {1} a {2} kbit/s, con segmentos de {3} s. El manifiesto dice al "
        "cliente cómo construir la dirección de cada segmento, bien con una lista explícita, bien con una "
        "plantilla en la que el número del segmento y la tasa de la representación se sustituyen en una URL, "
        "que es el esquema que usa el contenido de este trabajo (apartado 5.3). Timmerer y Griwodz describen la "
        "cadena completa que lleva de un vídeo fuente a una presentación DASH: codificación en varias "
        "representaciones, segmentación, generación del manifiesto, publicación en un servidor web y consumo "
        "por un cliente que lee el manifiesto y pide segmentos [timmerer2012dashCreationConsumption].".format(
            len(anchos), anchos[0], anchos[-1], int(dur / ts))
    )
    b.parrafo(
        "El estándar admite varios formatos de segmento y declara perfiles que restringen las opciones para "
        "garantizar la interoperabilidad. El contenido de este trabajo usa el perfil en directo sobre el "
        "formato ISO de fichero multimedia, en el que cada segmento es un fragmento MP4 autocontenido y las "
        "direcciones se construyen por plantilla; aunque el nombre alude al directo, es el perfil habitual "
        "también para el vídeo bajo demanda empaquetado por herramientas de código abierto. Sobre el estándar, "
        "el DASH Industry Forum publica unas guías de implementación, los puntos de interoperabilidad, que fijan "
        "el subconjunto que los reproductores comerciales deben soportar [dashIfIop]."
    )
    b.parrafo(
        "Dos decisiones del empaquetado condicionan después a cualquier algoritmo de adaptación. La primera "
        "es la duración del segmento. Segmentos cortos permiten reaccionar antes a los cambios de la red y "
        "reducen el retardo en directo, pero multiplican las peticiones y los ficheros y empeoran la eficiencia "
        "de la codificación; segmentos largos hacen lo contrario, y en redes móviles con fluctuaciones rápidas "
        "pueden no bastar para adaptarse a tiempo y producir más paradas, aunque un buffer mayor lo compense en "
        "parte [seufert2015hasQoeSurvey]. Los valores habituales en la literatura y en la práctica van de 2 a "
        "10 s; este trabajo usa 4 s, la duración de los conjuntos de referencia con los que se compara "
        "(apartado 4.7). La segunda decisión es la tasa de cada representación. La tasa que anuncia el "
        "manifiesto es nominal: un codificador con tasa variable produce segmentos cuyo tamaño en bytes se "
        "aparta de ella según la complejidad de la escena, de modo que dos segmentos del mismo nivel pueden "
        "tardar en descargarse tiempos muy distintos con la misma red. Los algoritmos que razonan solo con la "
        "tasa nominal ignoran esa variación; los que leen el tamaño real de cada segmento, bien del manifiesto, "
        "bien de un índice, pueden planificar con los bytes que de verdad se van a pedir. La diferencia es "
        "central en este trabajo y se retoma en los apartados 2.4 y 4.7."
    )

    b.guardar(SALIDA)
    texto = " ".join(p.text for p in b.doc.paragraphs)
    citas = set(re.findall(r"\[([A-Za-z][\w]*)\]", texto))
    faltan = citas - claves
    assert not faltan, faltan
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("citas:", sorted(citas))


if __name__ == "__main__":
    main()
