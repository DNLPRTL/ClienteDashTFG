# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_5_descriptivos.docx (apartado 6.5) y las Figuras 6.3 y 6.4.

Fuentes: sesiones.csv del paquete final (148 sesiones reales por controlador), agregados_por_controlador.json
(para cotejar la Tabla 6.8) y contrastes_prerregistrados.json (secundarias con IC95). La Tabla 6.9 descompone la
diferencia de QoE propio − rival en sus tres componentes a partir de las columnas por sesion. Las figuras se
dibujan con matplotlib desde sesiones.csv (no se pegan las PNG del paquete).

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_5.py
"""
from __future__ import annotations

import csv
import json
import statistics
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIGS = RAIZ_REPO / "docs" / "memoria" / "figuras"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap6_5_descriptivos.docx"

AZUL, GRIS, GRIS_CLARO, AMARILLO, ROJO, NEGRO = "#1971c2", "#495057", "#adb5bd", "#fff9db", "#c92a2a", "#212529"
ORDEN = ["propio_cuantiles_recientes", "propio_mediana", "mpc_robusto", "controlador_propio", "propio_cuantiles_fijos", "bba", "basado_en_tasa", "bola"]
NOMBRE = {
    "basado_en_tasa": "Basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "MPC robusto",
    "controlador_propio": "Controlador propio", "propio_mediana": "Propio, solo la mediana",
    "propio_cuantiles_recientes": "Propio, cuantiles recientes", "propio_cuantiles_fijos": "Propio, cuantiles fijos",
}
CORTO = {
    "basado_en_tasa": "basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "MPC robusto",
    "controlador_propio": "propio", "propio_mediana": "mediana sola",
    "propio_cuantiles_recientes": "cuantiles recientes", "propio_cuantiles_fijos": "cuantiles fijos",
}
ESTILO = {  # color, estilo de linea, grosor
    "controlador_propio": (AZUL, "-", 2.0), "mpc_robusto": (NEGRO, "-", 1.4),
    "propio_mediana": (AZUL, ":", 1.2), "propio_cuantiles_recientes": (AZUL, "--", 1.2), "propio_cuantiles_fijos": (AZUL, "-.", 1.2),
    "bba": (GRIS, "--", 1.2), "basado_en_tasa": (GRIS, ":", 1.2), "bola": (GRIS, "-.", 1.2),
}


def coma(x, dec=3, signo=False):
    return ("{0:+.%df}" % dec if signo else "{0:.%df}" % dec).format(x).replace(".", ",").replace("-", "−")


def ic(v, dec=3):
    return "[{0}; {1}]".format(coma(v[0], dec, True), coma(v[1], dec, True))


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def media(xs):
    return sum(xs) / len(xs)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    sesiones = leer_csv(PAQUETE / "02_resultados" / "sesiones.csv")
    reales = [s for s in sesiones if s["sintetica"] == "0"]
    agregados = {a["alias_controlador"]: a for a in json.load(open(PAQUETE / "02_resultados" / "agregados_por_controlador.json", encoding="utf-8"))}
    contrastes = json.load(open(PAQUETE / "02_resultados" / "contrastes_prerregistrados.json", encoding="utf-8"))
    sec = contrastes["secundarias"]
    por = {a: [s for s in reales if s["alias_controlador"] == a] for a in ORDEN}
    assert all(len(v) == 148 for v in por.values()) and set(agregados) == set(ORDEN)

    # ---- Tabla 6.8: agregados recalculados y cotejados ---------------------------------------
    def col(a, c):
        return [float(s[c]) for s in por[a]]

    agg = {}
    for a in ORDEN:
        agg[a] = {
            "qoe": media(col(a, "qoe_lineal_media")), "qoe_log": media(col(a, "qoe_log_media")),
            "bitrate": media(col(a, "bitrate_medio_kbps")), "rebuf": media(col(a, "rebuffering_total_s")),
            "paradas": media(col(a, "num_stalls")), "con_parada": sum(1 for x in col(a, "num_stalls") if x > 0) / 148,
            "cambios": media(col(a, "num_cambios_calidad")), "p05": agregados[a]["qoe_lineal_p05"],  # percentil del paquete
            "min": min(col(a, "qoe_lineal_media")), "rebuf_max": max(col(a, "rebuffering_total_s")),
            "gt5": sum(1 for x in col(a, "rebuffering_total_s") if x > 5),
        }
        ag = agregados[a]
        assert abs(agg[a]["qoe"] - ag["qoe_lineal_media"]) < 1e-9 and abs(agg[a]["qoe_log"] - ag["qoe_log_media"]) < 1e-9
        assert abs(agg[a]["bitrate"] - ag["bitrate_medio_kbps"]) < 1e-6 and abs(agg[a]["rebuf"] - ag["rebuffering_total_s_media"]) < 1e-9
        assert abs(agg[a]["paradas"] - ag["num_stalls_media"]) < 1e-9 and abs(agg[a]["con_parada"] - ag["proporcion_sesiones_con_stall"]) < 1e-9
        assert abs(agg[a]["min"] - ag["qoe_lineal_min"]) < 1e-9 and abs(agg[a]["rebuf_max"] - ag["rebuffering_total_s_max"]) < 1e-9
        assert ag["num_sesiones"] == 148
    orden_qoe = sorted(ORDEN, key=lambda a: -agg[a]["qoe"])
    assert orden_qoe == ORDEN, orden_qoe  # el orden de la tabla es el de QoE descendente
    assert orden_qoe[3] == "controlador_propio"  # el propio es el cuarto: NO tiene la QoE mas alta
    mejor_p05 = max(ORDEN, key=lambda a: agg[a]["p05"])
    assert mejor_p05 == "controlador_propio"

    # ---- Tabla 6.9: descomposicion de la diferencia de QoE por componentes -------------------
    # QoE por sesion = calidad_media_mbps − 4,3·rebuffering_total_s/29 − penalizacion_suavidad/29.
    for s in reales:
        q = float(s["calidad_media_mbps"]) - 4.3 * float(s["rebuffering_total_s"]) / 29 - float(s["penalizacion_suavidad"]) / 29
        assert abs(q - float(s["qoe_lineal_media"])) < 1e-9
    esc = {}
    for s in reales:
        esc.setdefault((s["id_ventana_traza"], s["id_perfil_video"]), {})[s["alias_controlador"]] = s
    assert len(esc) == 148

    def descomp(rival):
        d = {"qoe": [], "bitrate": [], "rebuf": [], "suav": []}
        for e in esc.values():
            p, r = e["controlador_propio"], e[rival]
            d["qoe"].append(float(p["qoe_lineal_media"]) - float(r["qoe_lineal_media"]))
            d["bitrate"].append(float(p["calidad_media_mbps"]) - float(r["calidad_media_mbps"]))
            d["rebuf"].append(-(4.3 * float(p["rebuffering_total_s"]) - 4.3 * float(r["rebuffering_total_s"])) / 29)
            d["suav"].append(-(float(p["penalizacion_suavidad"]) - float(r["penalizacion_suavidad"])) / 29)
        m = {k: media(v) for k, v in d.items()}
        assert abs(m["qoe"] - (m["bitrate"] + m["rebuf"] + m["suav"])) < 1e-9
        assert abs(m["qoe"] - sec[rival]["qoe_lineal_media"]["media_diferencia"]) < 1e-9
        return m

    rivales = ["mpc_robusto", "propio_cuantiles_recientes", "propio_mediana", "propio_cuantiles_fijos", "bba", "basado_en_tasa", "bola"]
    desc = {r: descomp(r) for r in rivales}

    # Ejemplo real: el escenario con mayor diferencia de QoE a favor del MPC robusto (regla fijada antes de mirar).
    peor = min(esc.values(), key=lambda e: float(e["controlador_propio"]["qoe_lineal_media"]) - float(e["mpc_robusto"]["qoe_lineal_media"]))
    pe, me = peor["controlador_propio"], peor["mpc_robusto"]
    ventanas_orden = []
    for s in reales:
        if s["id_ventana_traza"] not in ventanas_orden:
            ventanas_orden.append(s["id_ventana_traza"])
    num_ventana_peor = ventanas_orden.index(pe["id_ventana_traza"]) + 1
    d_peor = float(pe["qoe_lineal_media"]) - float(me["qoe_lineal_media"])
    comp_peor = (float(pe["calidad_media_mbps"]) - float(me["calidad_media_mbps"]),
                 -(4.3 * (float(pe["rebuffering_total_s"]) - float(me["rebuffering_total_s"]))) / 29,
                 -(float(pe["penalizacion_suavidad"]) - float(me["penalizacion_suavidad"])) / 29)
    assert abs(sum(comp_peor) - d_peor) < 1e-9

    # ---- Figura 6.3: CDF de la QoE lineal ------------------------------------------------------
    plt.rcParams.update({"font.family": "Arial", "font.size": 8, "axes.edgecolor": GRIS, "axes.labelcolor": GRIS,
                         "xtick.color": GRIS, "ytick.color": GRIS, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(6.3, 3.1), dpi=220)
    for a in ORDEN:
        v = sorted(col(a, "qoe_lineal_media"))
        y = [(i + 1) / len(v) for i in range(len(v))]
        c, ls, lw = ESTILO[a]
        ax.step(v, y, where="post", color=c, ls=ls, lw=lw, label=NOMBRE[a])
    ax.set_xlim(-1, 4.5)
    ax.set_ylim(0, 1)
    ax.set_xlabel("QoE lineal media de la sesión")
    ax.set_ylabel("fracción de sesiones (148 reales por controlador)")
    ax.axvline(0, color=GRIS_CLARO, lw=0.8)
    ax.text(-0.95, 0.9, "BOLA: {0} sesiones por debajo de −1 (mínimo {1})".format(sum(1 for x in col("bola", "qoe_lineal_media") if x < -1), coma(agg["bola"]["min"], 1)), fontsize=6.5, color=GRIS)
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    ax.legend(loc="lower right", frameon=False, fontsize=6.8)
    fig.tight_layout()
    fig.savefig(FIGS / "fig_6_3_cdf_qoe.svg")
    fig.savefig(FIGS / "fig_6_3_cdf_qoe.png")
    plt.close(fig)

    # ---- Figura 6.4: paradas frente a bitrate medio -----------------------------------------------
    fig, ax = plt.subplots(figsize=(6.3, 3.1), dpi=220)
    for a in ORDEN:
        x, y = agg[a]["paradas"], agg[a]["bitrate"]
        c = AZUL if a == "controlador_propio" else (NEGRO if a == "mpc_robusto" else GRIS)
        ax.scatter([x], [y], s=34 if a == "controlador_propio" else 22, color=c, zorder=3)
        dx, dy, ha = 0.02, 0, "left"
        if a == "propio_cuantiles_fijos":
            dy = -70
        if a == "controlador_propio":
            dx, dy, ha = -0.015, -130, "left"
        if a == "mpc_robusto":
            dy = 70
        ax.annotate(NOMBRE[a] + "  ({0})".format(coma(agg[a]["qoe"], 2)), (x, y), xytext=(x + dx, y + dy), fontsize=6.8, color=c, ha=ha, va="center")
    ax.set_xlabel("paradas por sesión (media)")
    ax.set_ylabel("bitrate medio (kbit/s)")
    ax.set_xlim(-0.03, 1.5)
    ax.set_ylim(1700, 3100)
    ax.text(0.6, 1760, "entre paréntesis, la QoE lineal media", fontsize=6.5, color=GRIS)
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    fig.tight_layout()
    fig.savefig(FIGS / "fig_6_4_paradas_bitrate.svg")
    fig.savefig(FIGS / "fig_6_4_paradas_bitrate.png")
    plt.close(fig)

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.h2("6.5. Resultados descriptivos por controlador")
    b.parrafo(
        "Las hipótesis del apartado 6.4 comparan al controlador propio con cuatro rivales en dos métricas. "
        "Este apartado sitúa esas comparaciones en el cuadro completo: los ocho controladores, todas las "
        "métricas y la distribución de los resultados, no solo su media. La Tabla 6.8 recoge los agregados de "
        "las 148 sesiones reales de cada controlador, ordenados por QoE lineal; la Tabla 6.9 descompone la "
        "diferencia de QoE entre el propio y cada rival en sus tres componentes; la Figura 6.3 muestra la "
        "distribución completa de la QoE y la Figura 6.4 el compromiso entre bitrate y paradas. Todo lo que "
        "sigue es descriptivo: las únicas decisiones son las del apartado anterior."
    )
    filas = []
    for a in ORDEN:
        g = agg[a]
        filas.append((NOMBRE[a], coma(g["qoe"], 3), coma(g["qoe_log"], 3), coma(g["bitrate"], 0), coma(g["rebuf"], 2),
                      coma(g["paradas"], 3), coma(100 * g["con_parada"], 1) + " %", coma(g["cambios"], 2)))
    b.tabla(
        ["Controlador", "QoE lineal", "QoE log", "Bitrate (kbit/s)", "Rebuf. (s)", "Paradas", "Con parada", "Cambios"],
        filas,
        "Tabla 6.8: Agregados de las 148 sesiones reales de cada controlador, ordenados por QoE lineal media: "
        "rebuffering en segundos por sesión, paradas por sesión, fracción de sesiones con alguna parada y cambios de "
        "nivel por sesión. Las medias se recalculan desde el fichero de sesiones del paquete y coinciden con sus agregados.",
        anchos_cm=[3.5, 1.7, 1.5, 1.8, 1.5, 1.8, 2.0, 1.9],
        alineaciones=["l", "c", "c", "c", "c", "c", "c", "c"],
    )
    b.parrafo(
        "La primera lectura de la Tabla 6.8 es la que no conviene maquillar: el controlador propio no tiene la "
        "QoE lineal media más alta. Es el cuarto, con {0}, por detrás de sus dos variantes más arriesgadas, la "
        "de cuantiles recientes ({1}) y la de la mediana sola ({2}), y empatado con el MPC robusto ({3}). La "
        "razón está en la propia métrica: una parada repartida entre 29 segmentos pesa poco, así que un "
        "controlador que apura el bitrate y para de vez en cuando puede sumar algo más de QoE media que uno "
        "que no para. Las dos variantes ganan {4} y {5} puntos de QoE a cambio de {6} y {7} veces más paradas. "
        "La segunda lectura es la que el diseño buscaba: de los cuatro controladores con QoE alta, el propio es "
        "el que menos para ({8} paradas por sesión, alguna parada en el {9} % de las sesiones) y el que menos "
        "rebuffering acumula ({10} s por sesión frente a {11} s del MPC robusto). Solo la variante de cuantiles "
        "fijos y el basado en tasa paran menos, y ambos lo pagan en QoE: {12} y {13} puntos menos que el "
        "propio.".format(
            coma(agg["controlador_propio"]["qoe"], 3), coma(agg["propio_cuantiles_recientes"]["qoe"], 3), coma(agg["propio_mediana"]["qoe"], 3),
            coma(agg["mpc_robusto"]["qoe"], 3), coma(agg["propio_cuantiles_recientes"]["qoe"] - agg["controlador_propio"]["qoe"], 3),
            coma(agg["propio_mediana"]["qoe"] - agg["controlador_propio"]["qoe"], 3),
            coma(agg["propio_cuantiles_recientes"]["paradas"] / agg["controlador_propio"]["paradas"], 0),
            coma(agg["propio_mediana"]["paradas"] / agg["controlador_propio"]["paradas"], 0),
            coma(agg["controlador_propio"]["paradas"], 3), coma(100 * agg["controlador_propio"]["con_parada"], 1),
            coma(agg["controlador_propio"]["rebuf"], 2), coma(agg["mpc_robusto"]["rebuf"], 2),
            coma(agg["controlador_propio"]["qoe"] - agg["propio_cuantiles_fijos"]["qoe"], 3), coma(agg["controlador_propio"]["qoe"] - agg["basado_en_tasa"]["qoe"], 3))
    )
    b.parrafo(
        "Los tres clásicos quedan por debajo en QoE. BBA, con {0}, cambia de nivel {1} veces por sesión, más "
        "del doble que cualquier otro, porque sigue la ocupación del buffer sin memoria de la red; el basado "
        "en tasa, con {2}, casi no para pero se queda en {3} kbit/s de media; y BOLA, con {4}, acumula {5} s de "
        "rebuffering por sesión y {6} paradas, concentradas en las ventanas de menor capacidad, donde su "
        "optimización sobre el buffer con tamaños nominales lo lleva a pedir niveles que la red no sostiene. La "
        "QoE logarítmica ordena igual a los ocho, con diferencias más comprimidas porque el logaritmo valora "
        "menos los niveles altos; como su referencia es el bitrate más bajo de cada sesión (apartado 6.2), no "
        "se extrae de ella ninguna conclusión más.".format(
            coma(agg["bba"]["qoe"], 3), coma(agg["bba"]["cambios"], 1), coma(agg["basado_en_tasa"]["qoe"], 3), coma(agg["basado_en_tasa"]["bitrate"], 0),
            coma(agg["bola"]["qoe"], 3), coma(agg["bola"]["rebuf"], 2), coma(agg["bola"]["paradas"], 2))
    )
    assert [a for a in sorted(ORDEN, key=lambda a: -agg[a]["qoe_log"])] == ORDEN
    b.figura(
        FIGS / "fig_6_3_cdf_qoe.png",
        "Figura 6.3: Distribución acumulada de la QoE lineal media por sesión de cada controlador (148 "
        "sesiones reales cada uno). En azul el controlador propio y sus tres variantes; en negro el MPC "
        "robusto; en gris los clásicos. El eje se corta en −1 para que se vea el centro de la distribución.",
        ancho_cm=16.0,
    )
    b.parrafo(
        "La Figura 6.3 muestra que las medias no lo cuentan todo. Las curvas del propio, el MPC robusto y las "
        "dos variantes arriesgadas van casi superpuestas en la mitad superior, donde la red sobra y todos "
        "eligen el nivel más alto, y se separan en la cola inferior: el percentil 5 de la QoE del propio es "
        "{0}, el más alto de los ocho, frente a {1} del MPC robusto y {2} de la mediana sola. Es decir, el "
        "propio no gana en las sesiones fáciles, donde cede algo de bitrate, y gana en las difíciles, donde "
        "evita la parada. BOLA tiene {3} sesiones con QoE negativa, con un mínimo de {4}, que es una sesión con "
        "{5} s de rebuffering; ningún otro controlador baja de {6}.".format(
            coma(agg["controlador_propio"]["p05"], 3), coma(agg["mpc_robusto"]["p05"], 3), coma(agg["propio_mediana"]["p05"], 3),
            sum(1 for x in col("bola", "qoe_lineal_media") if x < 0), coma(agg["bola"]["min"], 2), coma(agg["bola"]["rebuf_max"], 1),
            coma(min(agg[a]["min"] for a in ORDEN if a != "bola"), 2))
    )
    filas9 = [(NOMBRE[r], coma(desc[r]["qoe"], 3, True), coma(desc[r]["bitrate"], 3, True), coma(desc[r]["rebuf"], 3, True), coma(desc[r]["suav"], 3, True),
               ic(sec[r]["qoe_lineal_media"]["ic95"])) for r in rivales]
    b.tabla(
        ["Rival", "ΔQoE", "Bitrate", "Rebuffering", "Suavidad", "IC95 de ΔQoE"],
        filas9,
        "Tabla 6.9: Descomposición de la diferencia de QoE lineal (controlador propio menos rival, media de los "
        "148 escenarios) en sus tres componentes por segmento: bitrate en Mbit/s, penalización de rebuffering "
        "(4,3 veces los segundos, entre 29) y penalización de suavidad. Un valor positivo favorece al propio. "
        "El intervalo al 95 % es el bootstrap por ventanas del análisis.",
        anchos_cm=[4.0, 1.8, 1.8, 2.2, 1.8, 4.4],
        alineaciones=["l", "c", "c", "c", "c", "c"],
    )
    m = desc["mpc_robusto"]
    b.parrafo(
        "La Tabla 6.9 dice de dónde sale cada diferencia. Frente al MPC robusto, el propio cede {0} Mbit/s de "
        "bitrate por segmento ({1} kbit/s de media, un {2} %) y lo recupera casi entero con {3} de menor "
        "penalización de rebuffering y {4} de cambios más suaves: el resultado es la equivalencia de P1. "
        "Frente a las dos variantes arriesgadas el patrón es el mismo pero más marcado: cede {5} y {6} Mbit/s de "
        "bitrate y recupera la mayor parte en rebuffering y suavidad, con un saldo de {7} y {8} puntos de QoE "
        "cuyos intervalos incluyen o rozan el cero. Frente a la variante de cuantiles fijos ocurre lo contrario: "
        "gana {9} Mbit/s de bitrate con la misma penalización de rebuffering ({10}) y pierde algo de suavidad "
        "({11}), porque sube más a menudo. Frente a BBA, la ganancia es sobre todo de suavidad ({12}); frente al "
        "basado en tasa y a BOLA, de bitrate ({13} y {14} Mbit/s).".format(
            coma(abs(m["bitrate"]), 3), coma(abs(agg["controlador_propio"]["bitrate"] - agg["mpc_robusto"]["bitrate"]), 0),
            coma(100 * abs(agg["controlador_propio"]["bitrate"] - agg["mpc_robusto"]["bitrate"]) / agg["mpc_robusto"]["bitrate"], 1),
            coma(m["rebuf"], 3, True), coma(m["suav"], 3, True),
            coma(abs(desc["propio_cuantiles_recientes"]["bitrate"]), 3), coma(abs(desc["propio_mediana"]["bitrate"]), 3),
            coma(desc["propio_cuantiles_recientes"]["qoe"], 3, True), coma(desc["propio_mediana"]["qoe"], 3, True),
            coma(desc["propio_cuantiles_fijos"]["bitrate"], 3, True), coma(desc["propio_cuantiles_fijos"]["rebuf"], 3, True),
            coma(desc["propio_cuantiles_fijos"]["suav"], 3, True), coma(desc["bba"]["suav"], 3, True),
            coma(desc["basado_en_tasa"]["bitrate"], 3, True), coma(desc["bola"]["bitrate"], 3, True))
    )
    b.parrafo(
        "Leídas juntas, las tres variantes de ablación dicen qué aporta cada pieza del controlador. La red, "
        "frente a los cuantiles de las últimas descargas, cuesta {0} puntos de QoE (intervalo {1}) y evita {2} "
        "paradas por sesión (P3); frente a los cuantiles fijos, da {3} puntos de QoE (P4) con una diferencia de "
        "paradas de {4}, intervalo {5}, que no se distingue de cero: la red consigue casi la QoE de la opción "
        "arriesgada con la seguridad de la prudente. La agregación de riesgo, frente a la mediana sola, cuesta "
        "{6} puntos de QoE, intervalo {7}, tampoco distinguible de cero, y evita {8} paradas por sesión (P5). "
        "Frente a los clásicos, el propio supera en QoE a BBA en {9}, al basado en tasa en {10} y a BOLA en {11}, "
        "con intervalos que no tocan el cero; en paradas no se distingue del basado en tasa ni de BBA.".format(
            coma(abs(sec["propio_cuantiles_recientes"]["qoe_lineal_media"]["media_diferencia"]), 3), ic(sec["propio_cuantiles_recientes"]["qoe_lineal_media"]["ic95"]),
            coma(abs(sec["propio_cuantiles_recientes"]["num_stalls"]["media_diferencia"]), 3),
            coma(sec["propio_cuantiles_fijos"]["qoe_lineal_media"]["media_diferencia"], 3, True),
            coma(sec["propio_cuantiles_fijos"]["num_stalls"]["media_diferencia"], 3, True), ic(sec["propio_cuantiles_fijos"]["num_stalls"]["ic95"]),
            coma(abs(sec["propio_mediana"]["qoe_lineal_media"]["media_diferencia"]), 3), ic(sec["propio_mediana"]["qoe_lineal_media"]["ic95"]),
            coma(abs(sec["propio_mediana"]["num_stalls"]["media_diferencia"]), 3),
            coma(sec["bba"]["qoe_lineal_media"]["media_diferencia"], 3, True), coma(sec["basado_en_tasa"]["qoe_lineal_media"]["media_diferencia"], 3, True),
            coma(sec["bola"]["qoe_lineal_media"]["media_diferencia"], 3, True))
    )
    assert sec["propio_cuantiles_fijos"]["num_stalls"]["ic95"][0] < 0 < sec["propio_cuantiles_fijos"]["num_stalls"]["ic95"][1]
    assert sec["propio_mediana"]["qoe_lineal_media"]["ic95"][0] < 0 < sec["propio_mediana"]["qoe_lineal_media"]["ic95"][1]
    assert sec["bba"]["num_stalls"]["ic95"][0] < 0 < sec["bba"]["num_stalls"]["ic95"][1] and sec["basado_en_tasa"]["num_stalls"]["ic95"][0] <= 0 <= sec["basado_en_tasa"]["num_stalls"]["ic95"][1]
    assert all(sec[r]["qoe_lineal_media"]["ic95"][0] > 0 for r in ("bba", "basado_en_tasa", "bola"))
    b.figura(
        FIGS / "fig_6_4_paradas_bitrate.png",
        "Figura 6.4: Paradas por sesión frente a bitrate medio de los ocho controladores (medias de 148 "
        "sesiones reales), con la QoE lineal media entre paréntesis. Abajo a la izquierda, los controladores "
        "seguros; arriba a la derecha, los que apuran el bitrate.",
        ancho_cm=14.0,
    )
    b.parrafo(
        "La Figura 6.4 resume el compromiso en un solo plano: hacia arriba más bitrate, hacia la derecha más "
        "paradas. El MPC robusto, la mediana sola y los cuantiles recientes están más arriba que el propio y "
        "también más a la derecha; los cuantiles fijos y el basado en tasa, más a la izquierda y mucho más "
        "abajo. El propio ocupa la esquina que el diseño pretendía: casi el bitrate de los primeros con casi "
        "las paradas de los segundos. Un ejemplo concreto enseña el precio de esa posición. La regla, fijada "
        "antes de mirar, es tomar el escenario con la mayor diferencia de QoE a favor del MPC robusto: es la "
        "ventana {0}, una traza de {1}, con {2}. Allí el propio obtuvo {3} de QoE frente a {4} del MPC robusto, "
        "{5} puntos menos, sin que ninguno de los dos parara; la diferencia se reparte entre bitrate ({6} Mbit/s "
        "por segmento) y suavidad ({7}): el propio subió más tarde y a saltos más cortos. En esa red fue más "
        "prudente de lo necesario. El apartado 6.6 mira si ese comportamiento depende del origen de la red o del contenido.".format(
            num_ventana_peor, "Oboe" if pe["id_dataset"] == "oboe" else "la FCC",
            {"paseo_10min_30fps_4s": "Paseo de Almuñécar a 30 fps", "paseo_10min_60fps_4s": "Paseo de Almuñécar a 60 fps",
             "blender_10min_30fps_4s": "Blender Sunflower a 30 fps", "blender_10min_60fps_4s": "Blender Sunflower a 60 fps",
             "tears_10min_30fps_4s": "Tears of Steel"}[pe["id_perfil_video"]],
            coma(float(pe["qoe_lineal_media"]), 3), coma(float(me["qoe_lineal_media"]), 3), coma(abs(d_peor), 3),
            coma(comp_peor[0], 3, True), coma(comp_peor[2], 3, True))
    )
    assert int(pe["num_stalls"]) == 0 and int(me["num_stalls"]) == 0 and abs(comp_peor[1]) < 1e-12

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("agg", {a: {k: round(v, 3) for k, v in g.items()} for a, g in agg.items()})
    print("desc", {r: {k: round(v, 4) for k, v in d.items()} for r, d in desc.items()})
    print("peor", pe["id_sesion"], me["id_sesion"], round(d_peor, 4), [round(c, 4) for c in comp_peor], "ventana", num_ventana_peor)


if __name__ == "__main__":
    main()
