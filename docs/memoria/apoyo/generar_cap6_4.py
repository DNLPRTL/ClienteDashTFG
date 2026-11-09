# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_4_resultados_hipotesis.docx (apartado 6.4) y la Figura 6.2.

Fuentes: 02_resultados/contrastes_prerregistrados.json (los cinco contrastes, tal como los escribio el
analisis en la VM) y sesiones.csv del paquete final. La Tabla 6.7 se construye desde el JSON y se coteja con
apoyo/contrastes_reproducidos.json (analisis repetido en Windows, 6.3). La Figura 6.2 se dibuja con matplotlib
desde las diferencias por ventana recalculadas con contrastes.diferencias_por_ventana del entregable.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_4.py
"""
from __future__ import annotations

import csv
import json
import math
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
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIG_SVG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_6_2_diferencias_por_ventana.svg"
FIG_PNG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_6_2_diferencias_por_ventana.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap6_4_resultados_hipotesis.docx"
CACHE = Path(__file__).resolve().parent / "contrastes_reproducidos.json"
sys.path.insert(0, str(CODIGO))

AZUL, GRIS, GRIS_CLARO, AMARILLO, ROJO = "#1971c2", "#495057", "#adb5bd", "#fff9db", "#c92a2a"
NOMBRE_RIVAL = {
    "mpc_robusto": "MPC robusto", "propio_cuantiles_recientes": "propio, cuantiles recientes",
    "propio_cuantiles_fijos": "propio, cuantiles fijos", "propio_mediana": "propio, solo la mediana",
}
ENUNCIADO = {
    "P1": "QoE equivalente al MPC robusto (±0,15)", "P2": "menos paradas que el MPC robusto",
    "P3": "menos paradas que los cuantiles recientes", "P4": "más QoE que los cuantiles fijos",
    "P5": "menos paradas que la mediana sola",
}


def coma(x, dec=3, signo=False):
    s = ("{0:+.%df}" % dec if signo else "{0:.%df}" % dec).format(x).replace(".", ",").replace("-", "−")
    return s


def ic(v, dec=3):
    return "[{0}; {1}]".format(coma(v[0], dec, True), coma(v[1], dec, True))


def p_texto(p):
    if p < 1e-10:
        return "< 10⁻¹⁰"
    if p < 1e-4:
        e = int(math.floor(math.log10(p)))
        return "{0}·10{1}".format(coma(p / 10 ** e, 1), "⁻" + str(-e).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")))
    return coma(p, 4)


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from core.evaluacion import contrastes as C

    oficial = json.load(open(PAQUETE / "02_resultados" / "contrastes_prerregistrados.json", encoding="utf-8"))
    repetido = json.load(open(CACHE, encoding="utf-8"))
    P = oficial["principales"]
    assert list(P) == ["P1", "P2", "P3", "P4", "P5"]
    for k in P:
        for campo in ("media_diferencia", "p_valor", "p_holm", "ventanas_positivas", "ventanas_negativas", "ventanas_empate"):
            assert abs(float(P[k][campo]) - float(repetido["principales"][k][campo])) < 1e-9, (k, campo)
        assert P[k]["n_ventanas"] == 74 and P[k]["n_escenarios"] == 148 and P[k]["rechazada_nula"] is True
        assert P[k]["ventanas_positivas"] + P[k]["ventanas_negativas"] + P[k]["ventanas_empate"] == 74
    assert P["P1"]["equivalente_ic90"] is True and P["P1"]["margen"] == 0.15
    assert all(P[k]["p_holm"] <= 0.05 for k in P)
    # Holm recalculado a mano sobre los cinco p.
    holm = C.holm({k: P[k]["p_valor"] for k in P})
    assert all(abs(holm[k]["p_holm"] - P[k]["p_holm"]) < 1e-12 for k in P)

    sesiones = leer_csv(PAQUETE / "02_resultados" / "sesiones.csv")
    reales = [s for s in sesiones if s["sintetica"] == "0"]
    # Diferencias por ventana con la funcion del entregable (misma que uso el analisis).
    dif = {}
    for k in P:
        dif[k] = C.diferencias_por_ventana(reales, "controlador_propio", P[k]["rival"], P[k]["metrica"])
        assert len(dif[k]) == 74 and sum(len(v) for v in dif[k].values()) == 148
        medias = [sum(v) / len(v) for v in dif[k].values()]
        assert abs(sum(sum(v) for v in dif[k].values()) / 148 - P[k]["media_diferencia"]) < 1e-9
        pos = sum(1 for m in medias if m > 1e-12)
        neg = sum(1 for m in medias if m < -1e-12)
        assert pos == P[k]["ventanas_positivas"] and neg == P[k]["ventanas_negativas"]
    # P1: TOST a mano para conocer el orden de magnitud del p (el JSON guarda 0.0 por redondeo).
    m1 = [sum(v) / len(v) for v in dif["P1"].values()]
    de = statistics.stdev(m1)
    ee = de / math.sqrt(len(m1))
    centro = statistics.mean(m1)
    p_inf = 1 - C._normal((centro + 0.15) / ee)
    p_sup = C._normal((centro - 0.15) / ee)
    z_tost = min((centro + 0.15) / ee, (0.15 - centro) / ee)
    assert max(p_inf, p_sup) < 1e-10 and z_tost > 10
    # Margen mas estrecho en el que aun cabria el IC90 (redondeado al 0,01 superior).
    ic90 = P["P1"]["ic90"]
    margen_min = math.ceil(max(abs(ic90[0]), abs(ic90[1])) * 100) / 100
    # P2: p del signo a mano.
    n2 = P["P2"]["ventanas_positivas"] + P["P2"]["ventanas_negativas"]
    assert abs(C._cola_binomial(n2, P["P2"]["ventanas_positivas"]) - P["P2"]["p_valor"]) < 1e-12
    # Medias por controlador para interpretar (148 sesiones reales cada uno).
    def media(alias, metrica):
        v = [float(s[metrica]) for s in reales if s["alias_controlador"] == alias]
        assert len(v) == 148
        return sum(v) / len(v)

    paradas = {a: media(a, "num_stalls") for a in ("controlador_propio", "mpc_robusto", "propio_cuantiles_recientes", "propio_mediana", "propio_cuantiles_fijos")}
    qoe = {a: media(a, "qoe_lineal_media") for a in ("controlador_propio", "mpc_robusto", "propio_cuantiles_fijos")}
    sesiones_con_parada = {a: sum(1 for s in reales if s["alias_controlador"] == a and int(s["num_stalls"]) > 0) for a in paradas}
    # Ventanas de P2 en las que el MPC para y el propio no, y al reves.
    v2 = dif["P2"]
    # Ejemplo: la ventana 1 (la de la sesion 8), sus dos escenarios.
    ventana_ej = "real_001_e5ffa59001"
    ej = {}
    for s in reales:
        if s["id_ventana_traza"] == ventana_ej and s["alias_controlador"] in ("controlador_propio", "mpc_robusto"):
            ej.setdefault(s["id_perfil_video"], {})[s["alias_controlador"]] = (float(s["qoe_lineal_media"]), int(s["num_stalls"]))
    assert set(ej) == {"paseo_10min_30fps_4s", "tears_10min_30fps_4s"}
    d_ej_qoe = [ej[v]["controlador_propio"][0] - ej[v]["mpc_robusto"][0] for v in ("paseo_10min_30fps_4s", "tears_10min_30fps_4s")]
    assert abs(sum(d_ej_qoe) / 2 - sum(v2 and dif["P1"][ventana_ej]) / 2) < 1e-9

    # ---- Figura 6.2 --------------------------------------------------------------------------
    plt.rcParams.update({"font.family": "Arial", "font.size": 8, "axes.edgecolor": GRIS, "axes.labelcolor": GRIS,
                         "xtick.color": GRIS, "ytick.color": GRIS, "svg.fonttype": "none"})
    fig, (a, bx) = plt.subplots(1, 2, figsize=(6.3, 2.9), dpi=220)
    m1s = sorted(m1)
    a.axhspan(-0.15, 0.15, color=AMARILLO, zorder=0)
    a.axhline(0, color=GRIS_CLARO, lw=0.8, zorder=1)
    a.scatter(range(1, 75), m1s, s=9, color=GRIS, zorder=3, label="ventana (media de sus 2 vídeos)")
    a.axhspan(ic90[0], ic90[1], color=AZUL, alpha=0.25, zorder=2)
    a.axhline(P["P1"]["media_diferencia"], color=AZUL, lw=1.2, zorder=4)
    a.set_ylim(-0.6, 0.6)
    a.set_xlabel("ventanas ordenadas por la diferencia")
    a.set_ylabel("ΔQoE lineal (propio − MPC robusto)")
    a.set_title("(a) P1: equivalencia en QoE", fontsize=8.5, color="#212529")
    a.text(2, 0.165, "margen ±0,15", fontsize=7, color=GRIS, va="bottom")
    a.text(2, -0.50, "media {0}\nIC90 {1}".format(coma(P["P1"]["media_diferencia"], 3, True), ic(ic90, 3)), fontsize=7, color=AZUL, va="bottom")
    for s_ in ("top", "right"):
        a.spines[s_].set_visible(False)
        bx.spines[s_].set_visible(False)
    m2 = [sum(v) / len(v) for v in v2.values()]
    m2s = sorted(m2)
    bx.axhline(0, color=GRIS_CLARO, lw=0.8, zorder=1)
    colores = [ROJO if m > 1e-12 else (AZUL if m < -1e-12 else GRIS_CLARO) for m in m2s]
    bx.scatter(range(1, 75), m2s, s=9, color=colores, zorder=3)
    bx.axhspan(P["P2"]["ic95"][0], P["P2"]["ic95"][1], color=AZUL, alpha=0.25, zorder=2)
    bx.axhline(P["P2"]["media_diferencia"], color=AZUL, lw=1.2, zorder=4)
    bx.set_xlabel("ventanas ordenadas por la diferencia")
    bx.set_ylabel("Δ paradas por sesión (propio − MPC robusto)")
    bx.set_title("(b) P2: paradas", fontsize=8.5, color="#212529")
    ymin = min(m2s) - 0.3
    bx.set_ylim(ymin, 0.95)
    bx.text(2, 0.68, "{0} ventanas empatadas (gris)\n{1} a favor del propio (azul), {2} en contra (rojo)".format(
        P["P2"]["ventanas_empate"], P["P2"]["ventanas_negativas"], P["P2"]["ventanas_positivas"]), fontsize=6.5, color=GRIS, va="bottom")
    bx.text(2, P["P2"]["ic95"][0] - 0.05, "media {0}, IC95 {1}".format(coma(P["P2"]["media_diferencia"], 3, True), ic(P["P2"]["ic95"], 3)), fontsize=7, color=AZUL, va="top")
    fig.tight_layout(w_pad=2.0)
    fig.savefig(FIG_SVG)
    fig.savefig(FIG_PNG)
    plt.close(fig)

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.h2("6.4. Resultados de las hipótesis prerregistradas")
    b.parrafo(
        "Este apartado responde a las cinco hipótesis del apartado 6.2 con los datos de las 148 sesiones "
        "reales por controlador, agrupadas en sus 74 ventanas. La Tabla 6.7 recoge, para cada hipótesis, la "
        "diferencia media entre el controlador propio y su rival, los intervalos de confianza por bootstrap de "
        "ventanas, el recuento de ventanas a favor, en contra y empatadas, el valor p de la prueba y el p "
        "ajustado por Holm. Las cinco hipótesis se aceptan. A continuación se interpreta cada una con su "
        "magnitud, lo que significa y lo que no significa; la Figura 6.2 muestra las dos que comparan con el "
        "MPC robusto, ventana a ventana."
    )
    filas = []
    for k in P:
        h = P[k]
        filas.append((k, ENUNCIADO[k], coma(h["media_diferencia"], 3, True), ic(h["ic95"]), ic(h["ic90"]),
                      "{0}/{1}/{2}".format(h["ventanas_positivas"], h["ventanas_negativas"], h["ventanas_empate"]),
                      p_texto(h["p_valor"]), p_texto(h["p_holm"]), "sí"))
    b.tabla(
        ["Id", "Hipótesis", "Media", "IC95", "IC90", "+/−/=", "p", "p Holm", "Se acepta"],
        filas,
        "Tabla 6.7: Resultados de las cinco hipótesis prerregistradas sobre las 74 ventanas reales (148 "
        "escenarios). Diferencia = controlador propio menos rival, en puntos de QoE lineal (P1, P4) o en paradas "
        "por sesión (P2, P3, P5). Ventanas +/−/= según el signo de su diferencia media. Las p de las pruebas del "
        "signo son unilaterales; la de P1 es la del TOST.",
        anchos_cm=[0.9, 4.3, 1.5, 2.6, 2.6, 1.4, 1.3, 1.3, 1.1],
        alineaciones=["l", "l", "c", "c", "c", "c", "c", "c", "c"],
    )
    b.figura(
        FIG_PNG,
        "Figura 6.2: Diferencias por ventana entre el controlador propio y el MPC robusto, ordenadas de menor a "
        "mayor. (a) QoE lineal media de los dos vídeos de cada ventana, con el margen de equivalencia ±0,15 en "
        "amarillo y la media con su intervalo al 90 % en azul. (b) Paradas por sesión, con la media y su "
        "intervalo al 95 %; las ventanas empatadas a cero aparecen en gris.",
        ancho_cm=16.0,
    )
    b.parrafo(
        "P1, equivalencia en QoE con el MPC robusto. La diferencia media es de {0} puntos, con intervalo al "
        "90 % {1}: cabe holgadamente en el margen prerregistrado de ±0,15 y cabría incluso en uno de ±{2}, que "
        "equivale a unos {3} s de rebuffering en toda la sesión. El estadístico del TOST queda tan lejos de los "
        "límites que su p es menor de 10⁻¹⁰. Ventana a ventana, el propio gana en {4} y pierde en {5}, con {6} "
        "empates exactos, y la Figura 6.2(a) muestra que las diferencias se reparten a ambos lados de cero y "
        "que ninguna ventana se acerca al margen: la mayor diferencia a favor del MPC robusto es de {7} puntos y "
        "la mayor a favor del propio de {8}. En valores absolutos, la QoE media es {9} para el propio y {10} "
        "para el MPC robusto. Lo que P1 dice es que los dos controladores dan la misma calidad de experiencia "
        "lineal en estas redes y contenidos; lo que no dice es que el propio sea mejor en QoE, ni lo pretende.".format(
            coma(P["P1"]["media_diferencia"], 3, True), ic(ic90), coma(margen_min, 2), coma(margen_min * 29 / 4.3, 2),
            P["P1"]["ventanas_positivas"], P["P1"]["ventanas_negativas"], P["P1"]["ventanas_empate"],
            coma(abs(min(m1)), 3), coma(max(m1), 3), coma(qoe["controlador_propio"], 3), coma(qoe["mpc_robusto"], 3))
    )
    b.parrafo(
        "P2, menos paradas que el MPC robusto. La diferencia media es de {0} paradas por sesión, intervalo al "
        "95 % {1}: el propio para {2} veces por sesión frente a {3} del MPC robusto, cerca de cuatro veces "
        "menos, y tiene alguna parada en {4} de sus 148 sesiones frente a {5} del MPC robusto. La Figura 6.2(b) "
        "enseña la forma del resultado: en {6} de las 74 ventanas los dos controladores empatan, casi siempre "
        "porque ninguno para, y de las {7} ventanas en que difieren el propio para menos en {8} y más en {9}. "
        "La prueba del signo se decide solo con esas {7} ventanas, y aun así da p = {10}, ajustado {11}. Es el "
        "resultado de seguridad que el diseño buscaba, y es también el más frágil de los cinco en términos de "
        "recuento: depende de trece ventanas, las que tienen una red lo bastante difícil para hacer parar a un "
        "controlador prudente.".format(
            coma(P["P2"]["media_diferencia"], 3, True), ic(P["P2"]["ic95"]), coma(paradas["controlador_propio"], 3), coma(paradas["mpc_robusto"], 3),
            sesiones_con_parada["controlador_propio"], sesiones_con_parada["mpc_robusto"], P["P2"]["ventanas_empate"], n2,
            P["P2"]["ventanas_negativas"], P["P2"]["ventanas_positivas"], p_texto(P["P2"]["p_valor"]), p_texto(P["P2"]["p_holm"]))
    )
    b.parrafo(
        "P3, menos paradas que la variante de cuantiles recientes. Las dos usan el mismo planificador y la "
        "misma agregación de riesgo; la variante estima los cuantiles con las cinco últimas descargas, sin red. "
        "La diferencia es de {0} paradas por sesión, intervalo {1}: la variante para {2} veces por sesión y el "
        "propio {3}, unas {4} veces menos. El propio para menos en {5} ventanas y más en {6}, con {7} empates. "
        "Es la medida de lo que aporta la red frente a una distribución local sin modelo: con la misma "
        "prudencia en el planificador, predecir la red con lo aprendido evita la mayor parte de las paradas que "
        "provoca fiarse de las últimas cinco descargas.".format(
            coma(P["P3"]["media_diferencia"], 3, True), ic(P["P3"]["ic95"]), coma(paradas["propio_cuantiles_recientes"], 3),
            coma(paradas["controlador_propio"], 3), coma(paradas["propio_cuantiles_recientes"] / paradas["controlador_propio"], 0),
            P["P3"]["ventanas_negativas"], P["P3"]["ventanas_positivas"], P["P3"]["ventanas_empate"])
    )
    b.parrafo(
        "P4, más QoE que la variante de cuantiles fijos. Esta variante aplica a la media armónica unos cuantiles "
        "fijos del error, aprendidos en el entrenamiento, y es por construcción muy prudente. El propio la "
        "supera en {0} puntos de QoE, intervalo {1}, y gana en {2} de las 74 ventanas sin ninguna en contra "
        "({3} empates). La QoE media pasa de {4} a {5}. Es la otra cara de la aportación de la red: frente a una "
        "distribución fija, el modelo distingue cuándo la red permite subir y recupera calidad sin pagar en "
        "paradas (apartado 6.5).".format(
            coma(P["P4"]["media_diferencia"], 3, True), ic(P["P4"]["ic95"]), P["P4"]["ventanas_positivas"], P["P4"]["ventanas_empate"],
            coma(qoe["propio_cuantiles_fijos"], 3), coma(qoe["controlador_propio"], 3))
    )
    b.parrafo(
        "P5, menos paradas que la variante que usa solo la mediana. Esta variante recibe la misma predicción de "
        "la red, pero planifica con un solo escenario, el cuantil 0,50, en lugar de promediar los tres no "
        "optimistas. La diferencia es de {0} paradas por sesión, intervalo {1}: la mediana sola para {2} veces "
        "por sesión frente a {3} del propio, unas {4} veces más, y pierde en {5} ventanas frente a {6} en que gana, "
        "con {7} empates. Es el efecto de la agregación de riesgo aislado de todo lo demás: la misma red, el "
        "mismo planificador, y solo cambia cuántos escenarios se miran. Mirar únicamente el central lleva a "
        "elegir niveles que la red no sostiene cuando cae por debajo de su mediana.".format(
            coma(P["P5"]["media_diferencia"], 3, True), ic(P["P5"]["ic95"]), coma(paradas["propio_mediana"], 3), coma(paradas["controlador_propio"], 3),
            coma(paradas["propio_mediana"] / paradas["controlador_propio"], 0), P["P5"]["ventanas_negativas"], P["P5"]["ventanas_positivas"], P["P5"]["ventanas_empate"])
    )
    b.parrafo(
        "La corrección de Holm apenas cambia la lectura: los p ajustados de la Tabla 6.7 son todos menores de "
        "0,01, y el mayor es el de P2, {0}. Las cinco hipótesis se aceptan al nivel conjunto del 5 %. En la "
        "ventana 1, la de los ejemplos anteriores, la lectura por ventana se ve en pequeño: con Paseo a 30 fps "
        "el propio obtuvo una QoE de {1} y el MPC robusto {2}, y con Tears of Steel {3} y {4}; la diferencia "
        "media de la ventana es {5} puntos, dentro del margen, y ninguno de los dos paró en ninguno de los dos "
        "vídeos, así que esa ventana es uno de los {6} empates de P2. El apartado 6.5 sitúa estas diferencias en "
        "la tabla completa de los ocho controladores y descompone de dónde sale cada una.".format(
            p_texto(P["P2"]["p_holm"]), coma(ej["paseo_10min_30fps_4s"]["controlador_propio"][0], 3), coma(ej["paseo_10min_30fps_4s"]["mpc_robusto"][0], 3),
            coma(ej["tears_10min_30fps_4s"]["controlador_propio"][0], 3), coma(ej["tears_10min_30fps_4s"]["mpc_robusto"][0], 3),
            coma(sum(d_ej_qoe) / 2, 3, True), P["P2"]["ventanas_empate"])
    )
    assert all(ej[v][a][1] == 0 for v in ej for a in ej[v])

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("P1 tost z", round(z_tost, 1), "p", max(p_inf, p_sup), "margen min", margen_min, "ic90", ic90, "min/max ventana", round(min(m1), 3), round(max(m1), 3))
    print("paradas", {k: round(v, 3) for k, v in paradas.items()}, "qoe", {k: round(v, 3) for k, v in qoe.items()}, "con parada", sesiones_con_parada)
    print("ejemplo ventana 1", ej, "dif", d_ej_qoe)
    print("tabla", filas)


if __name__ == "__main__":
    main()
