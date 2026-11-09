# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_7_interpretacion_cierre.docx: apartado 6.7 (interpretacion y
limitaciones) y el cierre del capitulo 6 (parrafos sin epigrafe, como en el capitulo 5).

No introduce cifras nuevas: cada numero sale de contrastes_prerregistrados.json, agregados_por_controlador.json,
sesiones.csv o el protocolo del paquete, y ya se ha dado en 6.1 a 6.6 (el script lo comprueba contra los .docx
anteriores).

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_7.py
"""
from __future__ import annotations

import csv
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
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
SALIDA = BORRADORES / "cap6_7_interpretacion_cierre.docx"


def coma(x, dec=3, signo=False):
    return ("{0:+.%df}" % dec if signo else "{0:.%df}" % dec).format(x).replace(".", ",").replace("-", "−")


def ic(v, dec=3):
    return "[{0}; {1}]".format(coma(v[0], dec, True), coma(v[1], dec, True))


def texto_docx(ruta):
    d = Document(str(ruta))
    return "\n".join([p.text for p in d.paragraphs] + [c.text for t in d.tables for r in t.rows for c in r.cells])


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    contr = json.load(open(PAQUETE / "02_resultados" / "contrastes_prerregistrados.json", encoding="utf-8"))
    P = contr["principales"]
    E = contr["estratos"]
    inter = contr["contenido_nuevo_frente_a_visto"]
    agg = {a["alias_controlador"]: a for a in json.load(open(PAQUETE / "02_resultados" / "agregados_por_controlador.json", encoding="utf-8"))}
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    with open(PAQUETE / "02_resultados" / "sesiones.csv", encoding="utf-8", newline="") as f:
        sesiones = list(csv.DictReader(f))
    reales = [s for s in sesiones if s["sintetica"] == "0"]
    assert len(reales) == 1184 and protocolo["num_sesiones"] == 1208
    ventanas = {s["id_ventana_traza"] for s in reales}
    por_dataset = {}
    for s in reales:
        por_dataset.setdefault(s["id_dataset"], set()).add(s["id_ventana_traza"])
    assert len(ventanas) == 74 and len(por_dataset["oboe"]) == 56 and len(por_dataset["fcc_measuring_broadband_america"]) == 18
    propio, mpc = agg["controlador_propio"], agg["mpc_robusto"]
    cociente_paradas = mpc["num_stalls_media"] / propio["num_stalls_media"]
    assert 3.9 < cociente_paradas <= 4.05
    orden_qoe = sorted(agg, key=lambda a: -agg[a]["qoe_lineal_media"])
    assert orden_qoe.index("controlador_propio") == 3
    # Cada cifra que se repite aqui ya esta en 6.1-6.6.
    anteriores = "\n".join(texto_docx(BORRADORES / n) for n in (
        "cap6_1_diseno_experimento.docx", "cap6_2_metricas_hipotesis.docx", "cap6_3_integridad_verificacion.docx",
        "cap6_4_resultados_hipotesis.docx", "cap6_5_descriptivos.docx", "cap6_6_exploratorio.docx"))
    for frag in ("−0,001", "[−0,018; +0,017]", "0,041", "0,162", "35 032", "1208", "41,3 h", "0,28 y 0,31", "−0,045", "p = 0,34",
                 "2,547", "2,583", "0,625", "±0,02", "+0,149", "−0,791", "−0,439", "−0,122", "2,1 %"):
        assert frag in anteriores, frag

    b = Borrador(PLANTILLA)
    b.h2("6.7. Interpretación y limitaciones")
    b.parrafo(
        "Los apartados anteriores han dado las cifras; este dice qué significan y hasta dónde llegan. Primero "
        "se enuncia lo que el experimento permite afirmar y lo que no, después las limitaciones que acotan "
        "cada afirmación y, por último, la fidelidad de la ejecución al protocolo fijado antes de empezar."
    )

    b.h3("6.7.1. Qué se puede afirmar y qué no")
    b.parrafo(
        "Se pueden afirmar tres cosas, todas sobre el dominio del experimento: 74 ventanas reales de red "
        "emulada, de Oboe y de la FCC, con dos contenidos por ventana, uno visto en el entrenamiento y uno "
        "nuevo, y sesiones de 30 segmentos de 4 s. La primera es que el controlador propio da una calidad de "
        "experiencia lineal equivalente a la del MPC robusto canónico: la diferencia media es de {0} puntos y "
        "su intervalo al 90 %, {1}, cabe en el margen prerregistrado de ±0,15 y cabría en uno de ±0,02. La "
        "segunda es que lo hace con menos paradas y menos rebuffering: {2} paradas por sesión frente a {3}, unas "
        "cuatro veces menos, con la hipótesis P2 aceptada tras la corrección de Holm. La tercera es que las dos "
        "piezas que distinguen al controlador aportan cada una algo medible con el mismo planificador: la red "
        "de cuantiles, frente a estimadores sin red, evita paradas (P3) o gana calidad (P4) según con qué se la "
        "compare, y la agregación de riesgo, frente a la mediana sola, evita la mayor parte de las paradas (P5). "
        "Las tres afirmaciones salen de hipótesis fijadas antes de ejecutar, con la unidad de inferencia, el "
        "margen y el método declarados, y de una ejecución cuyas {4} decisiones se han repetido idénticas fuera "
        "de línea.".format(coma(P["P1"]["media_diferencia"], 3, True), ic(P["P1"]["ic90"]), coma(propio["num_stalls_media"], 3),
                            coma(mpc["num_stalls_media"], 3), "35 032")
    )
    b.parrafo(
        "Y hay cosas que no se afirman, porque el experimento no las sostiene. No se afirma que el controlador "
        "propio tenga la mejor calidad de experiencia: es el cuarto de ocho en QoE lineal media, por detrás de "
        "dos de sus propias variantes, y no se planteó así. No se afirma que mejore la QoE del MPC robusto: la "
        "hipótesis era de equivalencia y la equivalencia es lo que se obtuvo. No se afirma que el resultado "
        "generalice a redes reales con una pila TCP y tráfico competidor, a otros contenidos distintos de los "
        "tres usados, a otras duraciones de segmento o de sesión, ni a métricas perceptuales de calidad. Y sobre "
        "el contenido nuevo no se afirma nada más allá de lo exploratorio del apartado 6.6: la equivalencia se "
        "mantiene y la ventaja en paradas se estrecha, por causas que este experimento no separa."
    )

    b.h3("6.7.2. Limitaciones")
    b.parrafo(
        "Las limitaciones que siguen acotan las afirmaciones anteriores. Las cuatro primeras estaban declaradas "
        "en el protocolo antes de ejecutar; las demás se han identificado al analizar y al redactar, y se "
        "declaran con el mismo peso."
    )
    b.lista([
        ("Emulación de red", "la red se reproduce con trazas de throughput sobre una descarga real, sin pila TCP, "
         "sin latencia variable de la petición ni tráfico competidor (apartado 4.7). El throughput que ve el "
         "cliente es el de la traza, no el que negociaría una conexión real; los efectos de control de "
         "congestión y de compartición del enlace quedan fuera."),
        ("Origen de las ventanas", "las {0} ventanas proceden de dos conjuntos de datos, {1} de Oboe y {2} de la FCC, "
         "porque son los que tienen ventanas de 160 s dentro del filtro de relevancia en la partición de "
         "evaluación. Las redes móviles 4G y 5G del catálogo quedan casi siempre por encima de 6 Mbit/s y no "
         "entran; el resultado habla de redes de capacidad baja y media.".format(len(ventanas), len(por_dataset["oboe"]),
                                                                                  len(por_dataset["fcc_measuring_broadband_america"]))),
        ("Un solo contenido nuevo", "Tears of Steel es el único vídeo no visto, con un perfil de tamaños muy "
         "variable; la interacción observada con el contenido no puede separarse de las particularidades de "
         "ese vídeo."),
        ("Calidad medida por el bitrate", "la QoE lineal usa el bitrate nominal del nivel como medida de "
         "calidad, como la literatura con la que se compara, no una métrica perceptual como VMAF [netflixVmaf]. "
         "Dos segmentos del mismo nivel pueden tener calidades visuales distintas, y eso la métrica no lo ve."),
        ("Decisiones de diseño tomadas en validación", "el valor de α, la arquitectura del predictor y el "
         "ensanchado epistémico se eligieron con la partición de validación del catálogo (apartados 5.6 y 5.7). "
         "La partición de evaluación no se tocó hasta el experimento, pero el controlador que se evalúa es el "
         "resultado de esas elecciones."),
        ("Una sola referencia canónica", "la equivalencia se prueba contra el MPC robusto en su forma de "
         "referencia, con sus parámetros por defecto y los tamaños reales. Un MPC robusto ajustado a estas "
         "redes, o un controlador más reciente de la literatura, podría mover el punto de comparación."),
        ("Una repetición por escenario y sesiones cortas", "cada escenario se ejecutó una vez; el determinismo "
         "de las decisiones y la fidelidad de la física (apartado 6.3) lo justifican, pero el ruido temporal de "
         "la máquina virtual entra en los datos una sola vez. Las sesiones duran 30 segmentos, unos dos "
         "minutos de vídeo: el comportamiento en sesiones largas, con más cambios de régimen, no se ha medido."),
        ("Métricas secundarias", "la QoE logarítmica toma como referencia el bitrate más bajo de cada sesión, "
         "lo que la hace poco comparable entre sesiones, y el retardo de arranque no se midió porque es "
         "idéntico por construcción (apartado 6.2); ninguna de las dos interviene en las hipótesis."),
    ])
    b.parrafo(
        "Ninguna de estas limitaciones afecta a la validez interna del experimento, que el apartado 6.3 "
        "comprueba; todas afectan a su alcance. El trabajo futuro del apartado 7.4 parte de ellas."
    )

    b.h3("6.7.3. Fidelidad al protocolo")
    b.parrafo(
        "El protocolo preveía documentar cualquier desviación con su motivo. No hubo ninguna: las {0} sesiones "
        "se ejecutaron una sola vez, sin repeticiones ni descartes; el código, el modelo, la configuración y los "
        "parámetros fueron los congelados antes de lanzar, con sus huellas comprobadas; las hipótesis, el "
        "margen, las pruebas y la corrección fueron los copiados al protocolo al planificar; y el análisis "
        "publicado es el prerregistrado, reproducido en una segunda máquina. Las reglas de validez para "
        "sesiones no completadas no llegaron a aplicarse. El análisis secundario se ha presentado como "
        "exploratorio, tal como lo fijaba el protocolo, y las ventanas sintéticas aparte.".format(protocolo["num_sesiones"])
    )

    # Cierre del capitulo, sin epigrafe (biblia 6.3; como en el capitulo 5).
    b.parrafo(
        "Este capítulo ha evaluado el sistema con un único experimento cuyo diseño se fijó y se congeló antes "
        "de ejecutar: 74 ventanas reales de red, dos vídeos por ventana y ocho controladores, 1208 sesiones en "
        "41,3 h de máquina virtual, con cinco hipótesis prerregistradas, su unidad de inferencia y su método "
        "estadístico escritos en el código y copiados al protocolo (apartados 6.1 y 6.2). La integridad de la "
        "ejecución se ha comprobado en cuatro niveles, hasta repetir idénticas las {0} decisiones con el código "
        "congelado y reproducir la física de cada sesión (apartado 6.3).".format("35 032")
    )
    b.parrafo(
        "Las cinco hipótesis se aceptan tras la corrección de Holm: el controlador propio iguala en QoE lineal "
        "al MPC robusto canónico, dentro de un margen mucho más estrecho que el prerregistrado, y para unas "
        "cuatro veces menos; la red de cuantiles y la agregación de riesgo aportan cada una algo medible "
        "(apartado 6.4). El cuadro completo muestra que no es el controlador con más QoE media, sino el que "
        "menos para de entre los que la tienen alta, con la mejor cola inferior (apartado 6.5); el análisis "
        "exploratorio sitúa la holgura en las redes fijas y el precio de la prudencia en las variables y en el "
        "contenido nuevo (apartado 6.6). Las limitaciones, de alcance y no de validez, quedan declaradas "
        "(apartado 6.7). El capítulo 7 recapitula estos resultados frente a los objetivos del trabajo, recoge "
        "los resultados negativos de las líneas descartadas y propone el trabajo futuro que las limitaciones "
        "sugieren."
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("cociente paradas", round(cociente_paradas, 2), "orden QoE", orden_qoe)


if __name__ == "__main__":
    main()
