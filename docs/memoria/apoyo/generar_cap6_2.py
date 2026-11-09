# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_2_metricas_hipotesis.docx (apartado 6.2).

Fuentes: core/evaluacion/qoe.py y contrastes.py del codigo entregado (constantes y funciones), el
protocolo y los ficheros 02_resultados/segmentos.csv y sesiones.csv del paquete final. El ejemplo
real recalcula la QoE de la sesion 8 del plan (la misma del 6.1) con la funcion del entregable a
partir de sus 29 segmentos y exige que coincida con sesiones.csv. Ningun resultado de los
contrastes se cita aqui: eso es el 6.4.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_2.py
"""
from __future__ import annotations

import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla, m_d, m_f, m_r, m_sub  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap6_2_metricas_hipotesis.docx"
sys.path.insert(0, str(CODIGO))

NOMBRE_RIVAL = {
    "mpc_robusto": "MPC robusto", "propio_cuantiles_recientes": "propio, cuantiles recientes",
    "propio_cuantiles_fijos": "propio, cuantiles fijos", "propio_mediana": "propio, solo la mediana",
}
NOMBRE_METRICA = {"qoe_lineal_media": "QoE lineal media", "num_stalls": "paradas por sesión"}


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def m_sum(sub, sup, cuerpo):
    return ('<m:nary><m:naryPr><m:chr m:val="∑"/></m:naryPr><m:sub>{0}</m:sub><m:sup>{1}</m:sup><m:e>{2}</m:e></m:nary>'
            .format(sub, sup, cuerpo))


def m_func(nombre, arg):
    return "<m:func><m:fName>{0}</m:fName><m:e>{1}</m:e></m:func>".format(m_r(nombre, cursiva=False), arg)


def m_bar(x):
    return '<m:acc><m:accPr><m:chr m:val="̄"/></m:accPr><m:e>{0}</m:e></m:acc>'.format(x)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from core.evaluacion import contrastes as C
    from core.evaluacion.qoe import (PESO_REBUFFERING_LINEAL, PESO_REBUFFERING_LOG, PESO_SUAVIDAD_POR_DEFECTO,
                                     EntradaQoESegmento, calcular_qoe_lineal, calcular_qoe_log)

    assert PESO_REBUFFERING_LINEAL == 4.3 and PESO_REBUFFERING_LOG == 2.66 and PESO_SUAVIDAD_POR_DEFECTO == 1.0
    assert C.MARGEN_EQUIVALENCIA_QOE == 0.15 and C.REMUESTREOS_BOOTSTRAP == 10000 and C.SEMILLA_BOOTSTRAP == 2026
    assert C.REFERENCIA == "controlador_propio" and len(C.HIPOTESIS_PRINCIPALES) == 5
    assert [h["id"] for h in C.HIPOTESIS_PRINCIPALES] == ["P1", "P2", "P3", "P4", "P5"]
    assert [h["tipo"] for h in C.HIPOTESIS_PRINCIPALES] == ["equivalencia", "menor", "menor", "mayor", "menor"]
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    hip = protocolo["hipotesis"]
    assert hip["version"] == C.VERSION_HIPOTESIS and hip["alfa"] == 0.05 and hip["margen_equivalencia_qoe"] == 0.15
    assert [h["id"] for h in hip["principales"]] == ["P1", "P2", "P3", "P4", "P5"]
    assert hip["metricas_secundarias"] == list(C.METRICAS_SECUNDARIAS)
    # La prueba del signo y Holm del entregable, comprobadas sobre casos de valor conocido.
    assert abs(C._cola_binomial(13, 1) - 14 / 2 ** 13) < 1e-12 and C._cola_binomial(0, 0) == 1.0
    assert abs(C._normal(0.0) - 0.5) < 1e-12 and abs(C._normal(1.6448536) - 0.95) < 1e-6
    h = C.holm({"a": 0.01, "b": 0.04, "c": 0.03})
    assert abs(h["a"]["p_holm"] - 0.03) < 1e-12 and abs(h["c"]["p_holm"] - 0.06) < 1e-12 and abs(h["b"]["p_holm"] - 0.06) < 1e-12
    assert h["a"]["rechazada_nula"] and not h["c"]["rechazada_nula"] and not h["b"]["rechazada_nula"]

    # ---- Sesiones y segmentos del paquete --------------------------------------------------
    sesiones = leer_csv(PAQUETE / "02_resultados" / "sesiones.csv")
    segmentos = leer_csv(PAQUETE / "02_resultados" / "segmentos.csv")
    reales = [s for s in sesiones if s["sintetica"].strip().lower() not in ("1", "true")]
    assert len(sesiones) == 1208 and len(reales) == 1184
    assert {int(s["num_segmentos"]) for s in sesiones} == {29}
    escenarios = {(s["id_ventana_traza"], s["id_perfil_video"]) for s in reales}
    ventanas = {s["id_ventana_traza"] for s in reales}
    assert len(escenarios) == 148 and len(ventanas) == 74
    por_sesion = Counter(f["id_sesion"] for f in segmentos)
    assert set(por_sesion.values()) == {29} and len(por_sesion) == 1208
    # Una parada = un segmento evaluable con rebuffering > 0: el total de filas con rebuffering
    # coincide con la suma de num_stalls.
    assert sum(1 for f in segmentos if float(f["rebuffering_s"]) > 0) == sum(int(s["num_stalls"]) for s in sesiones)
    margen = PESO_REBUFFERING_LINEAL / 29

    # ---- Ejemplo real: la sesion 8 del plan (misma regla que el 6.1) ----------------------------
    id_ej = next(s["id_sesion"] for s in sesiones if s["id_sesion"].startswith("s00008_"))
    assert "controlador_propio" in id_ej
    ses_ej = next(s for s in sesiones if s["id_sesion"] == id_ej)
    seg_ej = sorted((f for f in segmentos if f["id_sesion"] == id_ej), key=lambda f: int(f["indice_segmento"]))
    assert len(seg_ej) == 29 and int(seg_ej[0]["indice_segmento"]) == 2
    entradas = [EntradaQoESegmento(float(f["bitrate_kbps"]), float(f["rebuffering_s"])) for f in seg_ej]
    q = calcular_qoe_lineal(entradas)
    qlog = calcular_qoe_log(entradas, min_bitrate_kbps=min(e.bitrate_kbps for e in entradas))
    assert abs(q.qoe_media - float(ses_ej["qoe_lineal_media"])) < 1e-9
    assert abs(qlog.qoe_media - float(ses_ej["qoe_log_media"])) < 1e-9
    assert abs(q.bitrate_medio_kbps - float(ses_ej["bitrate_medio_kbps"])) < 1e-6
    assert q.num_stalls == int(ses_ej["num_stalls"]) == 0 and q.num_cambios_calidad == int(ses_ej["num_cambios_calidad"]) == 2
    niveles = [int(float(f["bitrate_kbps"])) for f in seg_ej]
    cambios = [(i + 1, niveles[i], niveles[i + 1]) for i in range(len(niveles) - 1) if niveles[i] != niveles[i + 1]]
    suav_total = sum(q.suavidad_por_segmento)
    assert abs(suav_total - float(ses_ej["penalizacion_suavidad"])) < 1e-9
    # Comprobacion con la ecuacion (6.1) escrita a mano.
    R = [n / 1000 for n in niveles]
    qoe_mano = sum(R[n] - 4.3 * entradas[n].rebuffering_s - (abs(R[n] - R[n - 1]) if n > 0 else 0.0) for n in range(29)) / 29
    assert abs(qoe_mano - q.qoe_media) < 1e-9
    r_min = min(niveles)
    # Numero de cuantiles de la QoE log: ln(4300/300).
    ln_max = math.log(max(niveles) / r_min)

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.h2("6.2. Métricas e hipótesis prerregistradas")
    b.parrafo(
        "Este apartado define qué se mide en cada sesión y qué se contrasta después. Las métricas se "
        "calculan con el módulo de evaluación del cliente (apartado 4.8) a partir de la telemetría de cada "
        "sesión, y las hipótesis, con su método estadístico, están escritas en el código y copiadas al "
        "protocolo del paquete antes de ejecutar la primera sesión. Primero se definen las métricas "
        "(6.2.1), después la unidad de análisis y las cinco hipótesis (6.2.2) y por último los "
        "procedimientos estadísticos con los que se deciden (6.2.3)."
    )

    b.h3("6.2.1. Métricas por sesión")
    b.parrafo(
        "De los 30 segmentos de una sesión se evalúan los 29 que siguen al de calentamiento, que es el "
        "primero y se descarga siempre en el nivel más bajo sin consultar al controlador (apartado 6.1). "
        "Cada segmento evaluable aporta tres magnitudes: el bitrate nominal del nivel elegido, el "
        "rebuffering que la reproducción sufrió esperándolo (apartado 4.6) y el cambio de nivel respecto "
        "al segmento anterior. La métrica principal es la calidad de experiencia lineal por sesión, la "
        "media por segmento de la recompensa que usan Yin et al. para el MPC [yin2015mpc] y que Pensieve "
        "fija con sus pesos [mao2017pensieve]:"
    )
    b.ecuacion(
        m_sub(m_r("QoE"), m_r("lin")) + m_r("=", cursiva=False)
        + m_f(m_r("1", cursiva=False), m_r("N"))
        + m_sum(m_r("n=1"), m_r("N"),
                m_d(m_sub(m_r("R"), m_r("n")) + m_r("−", cursiva=False) + m_r("μ") + m_r("·", cursiva=False) + m_sub(m_r("T"), m_r("n"))
                    + m_r("−", cursiva=False) + m_d(m_sub(m_r("R"), m_r("n")) + m_r("−", cursiva=False) + m_sub(m_r("R"), m_r("n−1")), abre="|", cierra="|"),
                    abre="[", cierra="]")),
        "6.1",
    )
    b.parrafo(
        "donde N = 29 es el número de segmentos evaluables, R~n~ el bitrate nominal del segmento n en "
        "Mbit/s, T~n~ el rebuffering en segundos que precedió a su reproducción y μ = {0} el peso del "
        "rebuffering; el término de suavidad vale cero en el primer segmento evaluable. Los tres sumandos "
        "están en las mismas unidades, Mbit/s por segmento, y el peso μ dice cuánto cuesta un segundo de "
        "parada: lo mismo que bajar el bitrate medio de la sesión en {0} Mbit/s durante un segmento, es decir, "
        "la escalera entera, del nivel más alto al más bajo. Son los pesos de la QoE lineal de Pensieve, "
        "con los que se entrena y se compara buena parte de la literatura posterior, y la misma escalera de "
        "300 a 4300 kbit/s; la comparación con otros trabajos queda así en una escala conocida.".format(coma(PESO_REBUFFERING_LINEAL, 1))
    )
    b.parrafo(
        "La segunda métrica principal, de seguridad, es el número de paradas por sesión: los segmentos "
        "evaluables con rebuffering mayor que cero. Se eligió el número y no la duración porque es la "
        "magnitud que no se diluye: una parada de medio segundo en 29 segmentos apenas mueve la QoE lineal "
        "({0} puntos), pero es una interrupción que el usuario percibe, y la duración ya entra en la QoE a "
        "través de μ. Las métricas secundarias, que solo se informan, son el rebuffering total en segundos, "
        "el bitrate medio, el número de cambios de nivel y la QoE logarítmica de Pensieve, con utilidad "
        "ln(R~n~ / R~mín~) y peso {1}, donde R~mín~ es el bitrate más bajo que alcanzó la propia sesión, de "
        "modo que su escala depende de cada sesión y solo sirve como contraste de la lineal. El retardo de "
        "arranque no interviene: en la evaluación todas las sesiones arrancan en el nivel más bajo, sin "
        "ventana de arranque y con la misma cola mínima, así que es idéntico por construcción. La Tabla 6.4 "
        "resume las métricas y su papel.".format(coma(PESO_REBUFFERING_LINEAL * 0.5 / 29, 3), coma(PESO_REBUFFERING_LOG, 2))
    )
    b.tabla(
        ["Métrica", "Definición por sesión", "Unidad", "Papel"],
        [
            ("QoE lineal", "ecuación (6.1): bitrate menos {0} veces el rebuffering menos el cambio de bitrate, media de 29 segmentos".format(coma(PESO_REBUFFERING_LINEAL, 1)), "Mbit/s", "principal (P1, P4)"),
            ("Paradas", "segmentos evaluables con rebuffering mayor que cero", "paradas", "principal de seguridad (P2, P3, P5)"),
            ("Rebuffering total", "suma del rebuffering de los 29 segmentos", "s", "secundaria"),
            ("Bitrate medio", "media del bitrate nominal de los 29 segmentos", "kbit/s", "secundaria"),
            ("Cambios de nivel", "transiciones entre segmentos consecutivos con nivel distinto", "cambios", "secundaria"),
            ("QoE logarítmica", "como (6.1) con utilidad ln(R~n~/R~mín~) y peso {0}".format(coma(PESO_REBUFFERING_LOG, 2)), "nats", "secundaria"),
        ],
        "Tabla 6.4: Métricas por sesión del experimento final. Las dos principales son las de las hipótesis; "
        "las secundarias se informan con intervalos pero sin decisión.",
        anchos_cm=[3.0, 7.4, 1.8, 3.8],
    )
    b.parrafo(
        "La sesión 8 del plan, la misma del apartado 6.1, sirve de ejemplo de cálculo. Sus 29 segmentos "
        "evaluables empezaron en {0} kbit/s, el controlador subió a {1} kbit/s en el segundo y a {2} kbit/s "
        "en el tercero, y se mantuvo ahí hasta el final; no hubo rebuffering. El bitrate medio es {3} Mbit/s, "
        "la penalización de suavidad suma {4} Mbit/s en toda la sesión ({5} y {6} en los dos cambios), que "
        "repartida entre 29 segmentos vale {7}, y la QoE lineal queda en {3} − 0 − {7} = {8}. El valor que "
        "guarda el resumen del paquete para esa sesión es {9}, calculado por el mismo módulo; el script que "
        "genera este apartado lo recalcula desde los segmentos y exige que coincida. La QoE logarítmica de "
        "la misma sesión es {10}, con R~mín~ = {0} kbit/s y ln({2}/{0}) = {11} como utilidad de los 27 "
        "segmentos en el nivel más alto.".format(
            niveles[0], cambios[0][2], cambios[1][2], coma(q.bitrate_medio_kbps / 1000, 3), coma(suav_total, 2),
            coma(q.suavidad_por_segmento[cambios[0][0]], 2), coma(q.suavidad_por_segmento[cambios[1][0]], 2),
            coma(suav_total / 29, 3), coma(q.qoe_media, 3), coma(float(ses_ej["qoe_lineal_media"]), 3),
            coma(qlog.qoe_media, 3), coma(ln_max, 3))
    )

    b.h3("6.2.2. Unidad de análisis, bloques e hipótesis")
    b.parrafo(
        "Las comparaciones son pareadas: cada controlador se compara con el propio en el mismo escenario, "
        "es decir, en la misma ventana de red y con el mismo vídeo, de modo que la diferencia de QoE o de "
        "paradas entre ambos no depende de que a uno le tocara una red peor. La unidad de análisis es el "
        "escenario, y hay 148 reales (74 ventanas por 2 vídeos). Pero los dos escenarios de una ventana "
        "comparten la red, así que sus diferencias no son independientes; por eso el bloque de inferencia "
        "es la ventana: las pruebas de decisión usan la diferencia media de los dos escenarios de cada "
        "ventana (74 valores) y los intervalos de confianza remuestrean ventanas enteras. La alternativa, "
        "tratar los 148 escenarios como independientes, habría dado intervalos más estrechos de lo que los "
        "datos permiten. Las sesiones sintéticas no entran en ningún contraste."
    )
    b.parrafo(
        "Las cinco hipótesis de la Tabla 6.5 se fijaron antes de ejecutar y responden a las dos preguntas "
        "del apartado 6.1. P1 y P2 comparan el controlador propio con el MPC robusto canónico, que es la "
        "referencia fuerte: P1 pide equivalencia en QoE lineal, no superioridad, porque el objetivo del "
        "diseño es igualar la calidad y ganar en seguridad, y P2 pide menos paradas. P3, P4 y P5 comparan el "
        "propio con sus tres variantes de ablación (apartado 5.6) y aíslan cada pieza: la red frente a los "
        "cuantiles de las últimas descargas (P3, en paradas), la red frente a cuantiles fijos (P4, en QoE, "
        "porque la variante fija ya es prudente y lo que puede aportar la red es calidad) y la agregación "
        "de riesgo frente a la mediana sola (P5, en paradas). Todas son unilaterales salvo P1, y su sentido "
        "está declarado en la tabla."
    )
    filas_h = []
    for h in C.HIPOTESIS_PRINCIPALES:
        prueba = {"equivalencia": "TOST, margen ±{0}".format(coma(C.MARGEN_EQUIVALENCIA_QOE, 2)),
                  "menor": "signo, unilateral (menos)", "mayor": "signo, unilateral (más)"}[h["tipo"]]
        filas_h.append((h["id"], h["texto"].replace("+-", "±").replace("sesion", "sesión").replace("ultimas", "últimas").replace("mas QoE", "más QoE"),
                        NOMBRE_RIVAL[h["rival"]], NOMBRE_METRICA[h["metrica"]], prueba))
    b.tabla(
        ["Id", "Hipótesis (propio frente al rival)", "Rival", "Métrica", "Prueba"],
        filas_h,
        "Tabla 6.5: Hipótesis prerregistradas del experimento final. La referencia es siempre el controlador "
        "propio; la decisión se toma con el p ajustado por Holm sobre las cinco.",
        anchos_cm=[1.0, 6.2, 3.4, 2.6, 2.8],
    )
    b.parrafo(
        "El margen de equivalencia de P1 es ±{0} puntos de QoE lineal. Sale de la propia métrica: una "
        "parada de un segundo en una sesión de 29 segmentos cuesta {1}/29 = {2} puntos, así que dos "
        "controladores cuya QoE media difiere en menos de {0} están más cerca de lo que los separaría un solo "
        "segundo de rebuffering en toda la sesión. Se fijó antes de ver ningún dato y se informa también si el "
        "intervalo observado cabe en márgenes más estrechos.".format(coma(C.MARGEN_EQUIVALENCIA_QOE, 2), coma(PESO_REBUFFERING_LINEAL, 1), coma(margen, 3))
    )

    b.h3("6.2.3. Procedimientos estadísticos")
    b.parrafo(
        "Las hipótesis de superioridad (P2 a P5) se deciden con la prueba exacta del signo sobre las 74 "
        "diferencias medias por ventana. Bajo la hipótesis nula, cada ventana tiene la misma probabilidad de "
        "favorecer a uno u otro controlador, de modo que el número de ventanas favorables al rival sigue una "
        "binomial de parámetro 1/2 sobre las ventanas no empatadas, y el valor p es la probabilidad de "
        "observar tan pocas o menos. Las ventanas con diferencia media exactamente cero no cuentan y se "
        "informa cuántas hay; en paradas son frecuentes, porque muchas ventanas terminan sin ninguna parada "
        "con los dos controladores. Se eligió el signo frente a una prueba t o de Wilcoxon porque no supone "
        "ninguna forma de la distribución y no la mueven los valores extremos, que en esta métrica existen "
        "(apartado 6.5); a cambio es menos potente, lo que juega en contra de aceptar las hipótesis."
    )
    b.parrafo(
        "Los intervalos de confianza de todas las diferencias se obtienen por bootstrap por bloques "
        "[efron1993bootstrap]: se remuestrean con reposición las 74 ventanas, con todos sus escenarios, "
        "{0} veces con la semilla {1}, se calcula en cada réplica la diferencia media y se toman los "
        "percentiles 2,5 y 97,5 (intervalo al 95 %) o 5 y 95 (intervalo al 90 %). Remuestrear ventanas y no "
        "escenarios respeta la dependencia entre los dos vídeos de una misma red.".format(
            "10 000", C.SEMILLA_BOOTSTRAP)
    )
    b.parrafo(
        "La equivalencia de P1 se decide con el procedimiento de las dos pruebas unilaterales, TOST "
        "[schuirmann1987tost]: se rechaza por separado que la diferencia sea menor que −δ y que sea mayor "
        "que +δ, y el valor p de la equivalencia es el mayor de los dos:"
    )
    dbar = m_bar(m_r("d"))
    ee = m_sub(m_r("s"), m_r("d")) + m_r("/", cursiva=False) + '<m:rad><m:radPr><m:degHide m:val="1"/></m:radPr><m:deg/><m:e>' + m_r("74", cursiva=False) + "</m:e></m:rad>"
    b.ecuacion(
        m_sub(m_r("p"), m_r("TOST")) + m_r("=", cursiva=False)
        + m_func("máx", m_d(
            m_r("1", cursiva=False) + m_r("−", cursiva=False) + m_r("Φ") + m_d(m_f(dbar + m_r("+", cursiva=False) + m_r("δ"), ee))
            + m_r(",  ", cursiva=False) + m_r("Φ") + m_d(m_f(dbar + m_r("−", cursiva=False) + m_r("δ"), ee)),
            abre="{", cierra="}")),
        "6.2",
    )
    b.parrafo(
        "donde d̄ es la media de las 74 diferencias por ventana (propio menos MPC robusto, en puntos de "
        "QoE), s~d~ su desviación típica, δ = {0} el margen y Φ la función de distribución normal estándar. "
        "Es la aproximación normal con 74 bloques; Schuirmann demuestra que el procedimiento equivale a "
        "exigir que el intervalo de confianza al 1 − 2α, aquí el 90 %, quede dentro de [−δ, +δ], y por eso "
        "el análisis informa también si el intervalo al 90 % por bootstrap cabe en el margen, que es una "
        "comprobación sin supuesto de normalidad.".format(coma(C.MARGEN_EQUIVALENCIA_QOE, 2))
    )
    b.parrafo(
        "Como se deciden cinco hipótesis a la vez, los cinco valores p se corrigen con el método de Holm "
        "[holm1979bonferroni], que controla la probabilidad de aceptar por azar alguna de las cinco en el "
        "5 % y es uniformemente más potente que Bonferroni. Ordenados los p de menor a mayor, p~(1)~ ≤ … ≤ "
        "p~(m)~ con m = 5, el p ajustado es:"
    )
    b.ecuacion(
        m_sub('<m:acc><m:accPr><m:chr m:val="̃"/></m:accPr><m:e>' + m_r("p") + "</m:e></m:acc>", m_d(m_r("i")))
        + m_r("=", cursiva=False)
        + '<m:func><m:fName><m:limLow><m:e>' + m_r("máx", cursiva=False) + "</m:e><m:lim>" + m_r("j") + m_r("≤", cursiva=False) + m_r("i") + "</m:lim></m:limLow></m:fName><m:e>"
        + m_func("mín", m_d(m_r("1", cursiva=False) + m_r(",  ", cursiva=False) + m_d(m_r("m") + m_r("−", cursiva=False) + m_r("j") + m_r("+", cursiva=False) + m_r("1", cursiva=False))
                           + m_r("·", cursiva=False) + m_sub(m_r("p"), m_d(m_r("j"))), abre="{", cierra="}"))
        + "</m:e></m:func>",
        "6.3",
    )
    b.parrafo(
        "y una hipótesis se acepta si su p ajustado es menor o igual que 0,05. El p más pequeño se "
        "multiplica por cinco, el siguiente por cuatro, y así hasta el mayor, que no se corrige; el máximo "
        "acumulado impide que un p ajustado sea menor que el de una hipótesis con p menor. Todo el "
        "procedimiento, hipótesis, margen, pruebas, bootstrap y corrección, está en un solo módulo del "
        "código entregado con una prueba automática de valor conocido, y el ejecutor lo copia al protocolo "
        "del paquete al planificar, de modo que el análisis publicado es el mismo que estaba escrito antes "
        "de la primera sesión."
    )
    b.parrafo(
        "El resto del análisis es descriptivo y se presenta como tal. Para cada rival y cada métrica se "
        "informa la diferencia media con su intervalo al 95 % y una prueba del signo bilateral; para el MPC "
        "robusto y la variante de cuantiles recientes se repite por estratos (Oboe y FCC; vídeos vistos y "
        "contenido nuevo) y se mide la interacción con el contenido: la diferencia propio menos MPC robusto "
        "con el vídeo nuevo menos esa misma diferencia con el vídeo visto, ventana a ventana. Ninguna de "
        "estas cifras decide nada; sirven para entender de dónde sale el resultado principal y para "
        "declarar lo que no generaliza. Las componentes de la QoE (bitrate, rebuffering y suavidad) se "
        "informan por separado y las distribuciones completas acompañan a las medias, porque el orden entre "
        "algoritmos puede cambiar con el modelo de calidad de experiencia que se elija [peroni2024qoePitfalls] "
        "y una media sola oculta las colas. Los límites del método son dos: la aproximación normal del TOST, "
        "mitigada con el intervalo bootstrap, y el que impone la propia métrica, que mide la calidad por el "
        "bitrate y no por una medida perceptual; ambos se retoman en el apartado 6.7."
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("ejemplo:", id_ej, "niveles", niveles[:4], "cambios", cambios, "qoe", round(q.qoe_media, 4), "qlog", round(qlog.qoe_media, 4),
          "suav", suav_total, "bitrate", round(q.bitrate_medio_kbps, 1), "ln", round(ln_max, 4), "margen", round(margen, 4))


if __name__ == "__main__":
    main()
