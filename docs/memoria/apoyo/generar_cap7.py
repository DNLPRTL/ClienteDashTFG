# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap7_conclusiones.docx: capitulo 7 completo (Conclusiones y trabajo futuro).

Regla cero: el capitulo no introduce ninguna cifra nueva. Cada numero que repite ya esta en los .docx de los
capitulos 5 y 6 (el script lo comprueba) y los datos del sistema se leen del material entregado (bundle del modelo,
protocolo del experimento). El 7.1 responde a los Objetivos 1-5 del capitulo 1 por numero (se comprueba que existen).
Las lineas descartadas del 7.5 se describen de forma cualitativa, sin cifras de desarrollo.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap7.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from docx import Document

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
BUNDLE = TFG_MATERIAL / "03_modelos" / "modelo_propio" / "bundle"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"
SALIDA = BORRADORES / "cap7_conclusiones.docx"

# Cifras que el capitulo repite; cada una debe estar ya en el texto de los capitulos 5 o 6.
CIFRAS_REPETIDAS = ["−0,001", "[−0,018; +0,017]", "±0,15", "±0,02", "0,041", "0,162", "0,439", "0,149", "0,791",
                    "1208", "35 032", "0,625", "74 ventanas", "0,25"]
# Nombres internos que no pueden aparecer en la memoria (04_CORRESPONDENCIAS §5).
PROHIBIDOS = ["SPBC", "Q_H", "mpc_prudente", "Phase", "Fase 6", "v1", "v2", "Neural", "tfg_final",
              "benchmark_autorizado", "ensemble temporal", "Codex"]


def texto_docx(ruta):
    d = Document(str(ruta))
    return "\n".join([p.text for p in d.paragraphs] + [c.text for t in d.tables for r in t.rows for c in r.cells])


def datos_verificados():
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    hip = protocolo["hipotesis"]
    assert len(hip["principales"]) == 5 and hip["referencia"] == "controlador_propio"
    assert hip["margen_equivalencia_qoe"] == 0.15 and "Holm" in hip["multiplicidad"]
    assert len(protocolo["controladores"]) == 8 and protocolo["num_sesiones"] == 1208
    modelo = json.load(open(BUNDLE / "configuracion_modelo.json", encoding="utf-8"))
    plan = json.load(open(BUNDLE / "configuracion_planificador.json", encoding="utf-8"))
    assert modelo["tamano_ensemble"] == 5 and len(modelo["cuantiles"]) == 4 and modelo["horizonte_segmentos"] == 5
    assert plan["alfa_riesgo"] == 0.75 and plan["cuantiles"] == modelo["cuantiles"]
    assert plan["origen_tamanos_segmentos"] == "vbr_real_del_servidor"
    # Con K = 4 escenarios, alfa solo cambia la decision en saltos de 1/K = 0,25.
    salto = 1.0 / len(plan["cuantiles"])
    assert salto == 0.25
    # El capitulo 1 numera los objetivos a los que responde el 7.1.
    cap1 = texto_docx(BORRADORES / "cap1_introduccion.docx")
    for n in range(1, 6):
        assert "Objetivo {0}:".format(n) in cap1, n
    assert "El objetivo general del trabajo es diseñar, implementar y evaluar" in cap1
    # Cada cifra repetida ya esta en los capitulos 5 o 6.
    anteriores = "\n".join(texto_docx(BORRADORES / n) for n in (
        "cap5_6_controlador_propio.docx", "cap5_7_entorno_entrenamiento.docx",
        "cap6_1_diseno_experimento.docx", "cap6_2_metricas_hipotesis.docx", "cap6_3_integridad_verificacion.docx",
        "cap6_4_resultados_hipotesis.docx", "cap6_5_descriptivos.docx", "cap6_6_exploratorio.docx",
        "cap6_7_interpretacion_cierre.docx"))
    for frag in CIFRAS_REPETIDAS:
        assert frag in anteriores, frag
    # Afirmaciones del 7.1 y 7.2 que deben estar ya dichas en el capitulo 6.
    for frase in ("cuarto de ocho", "el más alto de los ocho", "ninguna recurrió al respaldo", "sin ningún respaldo",
                  "segunda máquina", "No hubo ninguna"):
        assert frase in anteriores, frase
    return {"n_hipotesis": len(hip["principales"]), "n_controladores": len(protocolo["controladores"]),
            "n_miembros": modelo["tamano_ensemble"], "n_cuantiles": len(modelo["cuantiles"]),
            "horizonte": modelo["horizonte_segmentos"], "alfa": plan["alfa_riesgo"], "salto_alfa": salto}


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    d = datos_verificados()
    b = Borrador(PLANTILLA)
    b.capitulo(7, "Conclusiones y trabajo futuro")
    b.parrafo(
        "Este capítulo cierra la memoria. Se responde, uno a uno, a los cinco objetivos del apartado 1.4 (apartado "
        "7.1); se resumen los resultados del capítulo 6 sin cifras nuevas (apartado 7.2) y las limitaciones que los "
        "acotan (apartado 7.3); se propone el trabajo futuro que esas limitaciones sugieren (apartado 7.4) y, por "
        "último, se documentan como resultados negativos las líneas descartadas durante el desarrollo (apartado "
        "7.5)."
    )

    # 7.1 ------------------------------------------------------------------------------------------------
    b.h2("7.1. Cumplimiento de los objetivos")
    b.parrafo(
        "El objetivo general del trabajo era diseñar, implementar y evaluar un controlador de adaptación de tasa "
        "que decidiera con la incertidumbre de la red y con las características reales del contenido, sobre un "
        "cliente DASH propio que permitiera compararlo de forma reproducible con los algoritmos de referencia. "
        "Los cinco objetivos específicos en que se concretó se revisan a continuación con la numeración del "
        "apartado 1.4, indicando en cada caso qué se ha hecho, dónde se describe y con qué evidencia se comprueba."
    )
    b.lista([
        ("Objetivo 1",
         "Cumplido. El cliente de los capítulos 4 y 5 interpreta el manifiesto con plantillas de URL e índices de "
         "segmentos (apartado 5.3), descarga los segmentos de un servidor web real, gestiona el buffer, reproduce "
         "con un motor simulado que respeta los tiempos del real y registra la telemetría de cada segmento y de "
         "cada decisión (apartado 5.2). La neutralidad respecto al controlador está garantizada por construcción: "
         "la interfaz entrega a todos la misma información y el código impide el acceso a los campos que describen "
         "la traza o el futuro (apartado 5.6). El motor simulado reprodujo la física de las sesiones del "
         "experimento (apartado 6.3)."),
        ("Objetivo 2",
         "Cumplido. Sobre la interfaz común corren el controlador basado en tasa, el basado en buffer, el basado en "
         "utilidad y el control predictivo robusto, implementados a partir de sus artículos con sus parámetros "
         "publicados y sin ajuste a este contenido ni a estas trazas (apartado 5.5). El MPC robusto se implementó "
         "en su forma canónica, con horizonte de {0} segmentos, la misma QoE lineal y los tamaños reales de los "
         "segmentos, y comparte el planificador con el controlador propio, de modo que la comparación entre ambos "
         "aísla la predicción. Sus decisiones se reprodujeron fuera de línea a partir de la telemetría "
         "(apartados 5.5 y 6.3).".format(d["horizonte"])),
        ("Objetivo 3",
         "Cumplido. El controlador propio combina un conjunto de {0} redes recurrentes, que predicen {1} cuantiles "
         "del throughput para cada uno de los {2} segmentos siguientes, con un planificador de control predictivo "
         "que evalúa cada plan en los escenarios de cuantil con los tamaños reales de los segmentos y elige el que "
         "optimiza la media de los escenarios no optimistas (apartado 5.6). El modelo se entrena fuera del cliente, "
         "en un simulador que comparte con él la física de la red y los tamaños reales, con ventanas de las "
         "particiones de entrenamiento y validación del catálogo y una comprobación de calibración antes de "
         "exportarlo (apartado 5.7). En el experimento, el modelo decidió en todas las sesiones sin recurrir al "
         "respaldo (apartado 6.3).".format(
             {5: "cinco"}[d["n_miembros"]], {4: "cuatro"}[d["n_cuantiles"]], {5: "cinco"}[d["horizonte"]])),
        ("Objetivo 4",
         "Cumplido. El banco de evaluación lo forman el servidor y el contenido DASH reales con tasa variable, la "
         "emulación de red por trazas del catálogo con particiones por grupo de captura sin fuga entre "
         "entrenamiento, validación y evaluación, el ejecutor que convierte un protocolo en un plan determinista de "
         "sesiones (apartado 5.4) y el paquete de evidencia que deja cada ejecución. El protocolo del experimento "
         "final fijó antes de ejecutar los controladores, las ventanas, los vídeos, las métricas, las {0} hipótesis "
         "y sus pruebas con corrección por comparaciones múltiples, y el código quedó congelado con sus huellas "
         "(apartado 6.1). La integridad del paquete se comprobó en cuatro niveles, hasta repetir idénticas las "
         "35 032 decisiones y reproducir el análisis en una segunda máquina (apartado 6.3).".format(
             {5: "cinco"}[d["n_hipotesis"]])),
        ("Objetivo 5",
         "Cumplido. El controlador propio se evaluó en 1208 sesiones frente a los cuatro clásicos y a sus tres "
         "variantes, en condiciones idénticas de red y de contenido; las {0} hipótesis prerregistradas se "
         "contrastaron y se aceptaron tras la corrección de Holm (apartado 6.4); el cuadro completo, los estratos y "
         "la interacción con el contenido se presentaron con sus intervalos (apartados 6.5 y 6.6), y el apartado "
         "6.7 declara qué se afirma, qué no y con qué limitaciones. El resultado no es el más favorable al "
         "controlador propio, que no tiene la QoE media más alta, y se informa tal cual.".format(
             {5: "cinco"}[d["n_hipotesis"]])),
    ])
    b.parrafo(
        "Los cinco objetivos se han cumplido en los términos en que se formularon. El Objetivo 5 merece una "
        "precisión: cumplirlo significa haber evaluado y declarado con exactitud, no haber obtenido el mejor "
        "resultado posible; se habría dado por cumplido igualmente si alguna hipótesis se hubiera rechazado y el "
        "rechazo se hubiera informado con la misma precisión."
    )

    # 7.2 ------------------------------------------------------------------------------------------------
    b.h2("7.2. Resultados principales")
    b.parrafo(
        "El resultado central es una equivalencia con menos paradas. En 74 ventanas reales de red emulada, con dos "
        "contenidos por ventana, la diferencia media de QoE lineal entre el controlador propio y el MPC robusto "
        "canónico fue de −0,001 puntos, con un intervalo al 90 % de [−0,018; +0,017] que cabe en el margen "
        "prerregistrado de ±0,15 y cabría en uno de ±0,02 (hipótesis P1). Al mismo tiempo, el controlador propio "
        "paró unas cuatro veces menos: 0,041 paradas por sesión frente a 0,162 (P2). Es la misma calidad media con "
        "una fracción de las interrupciones, que es el compromiso que el diseño buscaba."
    )
    b.parrafo(
        "Las variantes de ablación dicen de dónde sale ese comportamiento, porque usan el mismo planificador y "
        "cambian solo la predicción. Frente a los cuantiles de las últimas descargas, la red evita 0,439 paradas "
        "por sesión a cambio de una pérdida pequeña de QoE (P3); frente a los cuantiles fijos, gana 0,149 puntos de "
        "QoE sin una diferencia apreciable en paradas (P4); y la agregación de riesgo, frente a decidir con la "
        "mediana sola, evita 0,791 paradas por sesión con un coste en QoE que no se distingue de cero (P5). La red "
        "aporta el condicionamiento al estado de la red y la medida de riesgo aporta la seguridad: cada pieza hace "
        "aquello para lo que se diseñó."
    )
    b.parrafo(
        "El cuadro completo matiza el resultado sin contradecirlo. El controlador propio es el cuarto de ocho en "
        "QoE lineal media, por detrás de sus dos variantes más arriesgadas y empatado con el MPC robusto, porque la "
        "QoE lineal castiga poco una parada repartida en una sesión; a cambio tiene la cola inferior más alta de los "
        "ocho, con un percentil 5 de 0,625, y es el que menos para de entre los que tienen QoE alta. A los tres "
        "clásicos restantes los supera con claridad en QoE. En el análisis exploratorio, la equivalencia y la "
        "ventaja en paradas se sostienen en los dos orígenes de red, con más holgura en las redes fijas que en las "
        "variables; con el contenido nuevo la equivalencia se mantiene y la ventaja en paradas se estrecha."
    )
    b.parrafo(
        "El último resultado es metodológico. Todas las cifras anteriores salen de una única ejecución de 1208 "
        "sesiones cuyo protocolo se fijó antes, cuyas decisiones se repitieron idénticas fuera de línea y cuyo "
        "análisis se reprodujo en una segunda máquina, sin desviaciones del protocolo. Lo que se afirma es lo que "
        "se planteó demostrar, con la unidad de inferencia, el margen y la corrección declarados antes de ver los "
        "datos; lo que no se afirma queda dicho con la misma claridad."
    )

    # 7.3 ------------------------------------------------------------------------------------------------
    b.h2("7.3. Limitaciones")
    b.parrafo(
        "El apartado 6.7 enumera ocho limitaciones, cuatro declaradas en el protocolo y cuatro identificadas al "
        "analizar. Aquí se agrupan en tres clases según lo que acotan. Ninguna afecta a la validez interna del "
        "experimento, comprobada en el apartado 6.3; todas afectan a su alcance."
    )
    b.parrafo(
        "La primera clase acota el dominio. La red es emulada: el ancho de banda lo impone una traza sobre una "
        "descarga real, sin pila TCP, sin latencia variable ni tráfico competidor, de modo que la reacción del "
        "transporte a las decisiones del cliente queda fuera. Las 74 ventanas proceden de dos conjuntos de datos de "
        "capacidad baja y media, porque las trazas de redes móviles del catálogo quedan por encima de la escalera "
        "de calidades y no superan el filtro de relevancia. Las sesiones duran treinta segmentos, unos dos minutos "
        "de vídeo, y hay un solo contenido no visto en el entrenamiento, con un perfil de tamaños muy variable que "
        "no permite separar el efecto del contenido nuevo del de ese vídeo en concreto."
    )
    b.parrafo(
        "La segunda clase acota la medida. La calidad se mide por el bitrate nominal del nivel, como en la "
        "literatura con la que se compara, y no con una métrica perceptual: dos segmentos del mismo nivel pueden "
        "verse distintos y la QoE no lo registra. La QoE logarítmica toma como referencia el bitrate más bajo de "
        "cada sesión y es poco comparable entre sesiones, y el retardo de arranque no se midió porque es idéntico "
        "por construcción; ninguna de las dos interviene en las hipótesis."
    )
    b.parrafo(
        "La tercera clase acota el diseño de la comparación. El valor de α, la arquitectura del predictor y el "
        "ensanchado de la cola se eligieron sobre la partición de validación, sin tocar la de evaluación, pero el "
        "controlador evaluado es el resultado de esas elecciones. La equivalencia se prueba contra una sola "
        "referencia canónica con sus parámetros publicados, y cada escenario se ejecutó una vez, de modo que el "
        "ruido temporal de la máquina virtual entra en los datos una sola vez. Otra referencia podría mover el punto "
        "de comparación."
    )

    # 7.4 ------------------------------------------------------------------------------------------------
    b.h2("7.4. Trabajo futuro")
    b.parrafo(
        "Las limitaciones anteriores marcan el trabajo futuro. Las propuestas van de la que reutiliza el banco tal "
        "cual a la que exigiría más desarrollo; todas admiten el mismo tipo de protocolo prerregistrado."
    )
    b.lista([
        ("Validación en una red real",
         "La primera extensión sería repetir la comparación con una pila TCP real y tráfico competidor, bien en una "
         "emulación de red a nivel de paquete, bien en un despliegue con usuarios como el de la plataforma Puffer "
         "[yan2020puffer]. El cliente ya separa el descargador de la emulación (apartado 5.2), por lo que el cambio "
         "afectaría a la capa de red y no al controlador. Es la única forma de saber si la ventaja en paradas "
         "sobrevive a la reacción del transporte."),
        ("Más contenidos y sesiones más largas",
         "Un conjunto de vídeos no vistos con perfiles de tamaño distintos permitiría separar las dos hipótesis de "
         "trabajo del apartado 6.6 sobre el contenido nuevo: la variabilidad de los tamaños y el arranque con "
         "segmentos diminutos. Sesiones de la duración de un vídeo completo, con varios cambios de régimen de red, "
         "medirían el comportamiento que las de dos minutos no recogen. Ambas cosas caben en el banco actual: basta "
         "con añadir descriptores de tamaños y ampliar la duración de las ventanas."),
        ("Redes de mayor capacidad",
         "Las trazas de redes móviles de cuarta y quinta generación del catálogo quedaron fuera porque superan el "
         "techo de la escalera. Una escalera con niveles de varias decenas de megabits por segundo permitiría "
         "evaluar el controlador en el régimen en que la variabilidad es mayor y la predicción más difícil."),
        ("Calidad perceptual en la métrica",
         "Sustituir el bitrate nominal por una medida perceptual por segmento, como VMAF [netflixVmaf], tanto en la "
         "QoE de evaluación como en el objetivo del planificador, alinearía lo que se optimiza con lo que el usuario "
         "percibe. Como el planificador ya consulta un descriptor por segmento para los tamaños, incorporar una "
         "puntuación de calidad por segmento sería una extensión del mismo mecanismo."),
        ("El riesgo como mando y como hipótesis",
         "El parámetro α fija cuántos escenarios de cuantil entran en la media; con {0} cuantiles solo cambia la "
         "decisión en saltos de 0,25. Predecir más cuantiles permitiría un mando de riesgo más fino y una curva de "
         "compromiso entre QoE media y paradas, como la que presentan Kan et al. [kan2021bayesmpc]; y la cola "
         "inferior de la QoE, que en este experimento solo se describe, podría entrar como hipótesis prerregistrada "
         "en una comparación futura.".format({4: "cuatro"}[d["n_cuantiles"]])),
        ("Calibración en línea",
         "El predictor se calibra una vez, sobre la partición de validación, y no se adapta durante la sesión. Una "
         "recalibración de los cuantiles con la cobertura observada en las descargas ya hechas, o un reentrenamiento "
         "periódico con los datos del propio despliegue, como hace Fugu [yan2020puffer], trasladarían al "
         "controlador en funcionamiento la fidelidad al medio que aquí se consiguió fuera de línea."),
        ("Rivales adicionales",
         "El banco admite cualquier controlador escrito contra la interfaz común. Añadir un MPC robusto ajustado a "
         "estas redes y controladores con aprendizaje de extremo a extremo [mao2017pensieve], con el mismo "
         "protocolo, situaría al controlador propio frente a un abanico más amplio y respondería a la limitación de "
         "la referencia única."),
    ])

    # 7.5 ------------------------------------------------------------------------------------------------
    b.h2("7.5. Resultados negativos")
    b.parrafo(
        "El controlador del capítulo 5 no fue el primer intento. Durante el desarrollo se exploraron y se "
        "descartaron tres líneas de aprendizaje y una variante del predictor. Se recogen aquí porque explican por "
        "qué el diseño final es el que es, y porque un resultado negativo documentado ahorra a quien continúe el "
        "trabajo recorrer el mismo camino. Se describen de forma cualitativa: sus cifras pertenecen a ejecuciones de "
        "desarrollo, con particiones y versiones del cliente distintas de las del experimento final, y no son "
        "comparables con las del capítulo 6."
    )
    b.parrafo(
        "La primera línea fue una política de decisión aprendida por clonación de comportamiento. Una red neuronal "
        "recibía el estado observable de la sesión y devolvía directamente el nivel a pedir; se entrenaba fuera de "
        "línea para imitar a un maestro que decidía con información del futuro, primero con una pérdida de "
        "clasificación y después con pares de preferencia y penalizaciones del rebuffering esperado. Las métricas "
        "fuera de línea eran razonables, pero al conectarla al cliente la política se degradaba: la dinámica del "
        "buffer con que se había entrenado no coincidía con la del cliente, y cada ajuste de la función de pérdida "
        "desplazaba el modo de fallo, de pedir de más en redes de capacidad media a pedir de menos, sin "
        "eliminarlo. La lección fue doble: una política de extremo a extremo vale lo que vale el simulador en que "
        "se entrena, y sus errores no se pueden diagnosticar por partes. De ahí la decisión de acotar el "
        "aprendizaje a la predicción."
    )
    b.parrafo(
        "La segunda línea fue una función de puntuación con horizonte: una red que, para cada nivel candidato, "
        "estimaba la QoE que se obtendría en los segmentos siguientes si se eligiera, entrenada con el "
        "arrepentimiento respecto a la mejor acción conocida a posteriori. La red acertaba la mejor acción la mayor "
        "parte de las veces, pero el arrepentimiento medio no bajaba del umbral fijado, y el error se concentraba "
        "en las redes de capacidad media con buffer bajo o medio; las "
        "reponderaciones sensibles al coste saturaban los pesos sin corregirlo. La explicación es que el objetivo "
        "no es aprendible desde el estado observable: la QoE futura de una acción depende del throughput futuro, "
        "que no está en las entradas, de modo que la red solo puede aprender su valor medio y falla en las colas. El "
        "diseño final separa lo predecible, el throughput con su incertidumbre, de lo decidible, el plan, que se "
        "calcula en lugar de aprenderse."
    )
    b.parrafo(
        "La tercera es que más datos no mejoran sin fidelidad al medio. El predecesor directo del controlador propio "
        "ya combinaba un predictor de cuantiles con un planificador, pero se había entrenado y planificaba con los "
        "tamaños nominales de los segmentos, los de la tasa constante, mientras que el cliente reproducía contenido "
        "con tasa variable. En las ventanas de capacidad media y variable el planificador subestimaba el tiempo de "
        "descarga y el cliente paraba. La primera respuesta fue escalar el conjunto de datos y el entrenamiento "
        "manteniendo todo lo demás, para aislar la causa; el modelo entrenado con más datos no corrigió el problema "
        "y en el cliente resultó más agresivo, con más rebuffering. La causa no era la cantidad de datos sino el "
        "medio: el simulador de entrenamiento no reproducía los bytes que el cliente iba a pedir. Esa constatación "
        "dio lugar al entorno fiel del apartado 5.7, al uso de los tamaños reales en el planificador y a la medida "
        "de riesgo sobre la cola inferior."
    )
    b.parrafo(
        "La cuarta es una variante del predictor que se eliminó del sistema final. La primera versión del predictor "
        "de cuantiles era un perceptrón multicapa sobre las medidas recientes aplanadas en un vector. Sobre la "
        "partición de validación empataba con el MPC robusto en QoE, pero en las ventanas más difíciles se mostraba "
        "optimista y la medida de riesgo no bastaba para evitar la parada. Se sustituyó por el conjunto de redes "
        "recurrentes del apartado 5.6, que leen la secuencia de medidas, producen cuantiles que no se cruzan por "
        "construcción y ensanchan la cola inferior cuando los miembros discrepan, es decir, cuando la situación se "
        "parece poco a lo visto en el entrenamiento. En validación fue más prudente en esas ventanas y se adoptó; "
        "la versión anterior no forma parte del material entregado."
    )
    b.parrafo(
        "Leídas juntas, las cuatro líneas descartadas apuntan en la misma dirección que las decisiones de partida "
        "del apartado 1.3: aprender solo lo que se puede predecir, ser fiel al medio en que se va a decidir y "
        "comprobar cada pieza por separado. El controlador propio es el resultado de ese recorrido, y el "
        "experimento final, con su protocolo fijado antes y su paquete verificable, es la forma de dar cuenta de él."
    )

    # Comprobaciones finales sobre el texto -----------------------------------------------------------------
    texto = "\n".join(p.text for p in b.doc.paragraphs)
    bib = BIB.read_text(encoding="utf-8")
    claves = set(re.findall(r"@\w+\{([^,]+),", bib))
    citas = set()
    for grupo in re.findall(r"\[([a-zA-Z][\w]*(?:,\s*[a-zA-Z][\w]*)*)\]", texto):
        citas.update(c.strip() for c in grupo.split(","))
    citas = {c for c in citas if not c.startswith("Objetivo")}
    faltan = citas - claves
    assert not faltan, faltan
    for nombre in PROHIBIDOS:
        assert not re.search(r"\b" + re.escape(nombre) + r"\b", texto), nombre
    # Ninguna cifra decimal nueva: todas las que aparecen estan en la lista de repetidas.
    permitidas = " ".join(CIFRAS_REPETIDAS)
    for dec in set(re.findall(r"[−+]?\d+,\d+", texto)):
        assert dec.lstrip("+") in permitidas or dec in permitidas, dec
    # Sin resultados de desarrollo: ningun numero con mas de 3 cifras salvo los repetidos.
    for ent in set(re.findall(r"\b\d{4,}\b|\b\d{2} \d{3}\b", texto)):
        assert ent in ("1208", "35 032"), ent
    b.guardar(SALIDA)
    print("Guardado:", SALIDA)
    print("Palabras de cuerpo:", b.palabras_cuerpo, "| citas:", sorted(citas))


if __name__ == "__main__":
    main()
