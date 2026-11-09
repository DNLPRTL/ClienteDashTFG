# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_6_exploratorio.docx (apartado 6.6).

Fuentes: contrastes_prerregistrados.json (estratos e interaccion de contenido, con sus IC bootstrap) y
sesiones.csv del paquete final (medias absolutas por estrato, sinteticas y ejemplo). Las medias de los estratos
se recalculan con contrastes.diferencias_por_ventana del entregable y deben coincidir con el JSON.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_6.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap6_6_exploratorio.docx"
sys.path.insert(0, str(CODIGO))

ESTRATOS = [("fcc", "FCC (acceso fijo)", lambda f: f["id_dataset"].startswith("fcc")),
            ("oboe", "Oboe", lambda f: f["id_dataset"].startswith("oboe")),
            ("videos_vistos", "Vídeos vistos", lambda f: "tears" not in f["id_perfil_video"]),
            ("video_nuevo", "Vídeo nuevo (Tears of Steel)", lambda f: "tears" in f["id_perfil_video"])]
RIVALES = [("mpc_robusto", "MPC robusto"), ("propio_cuantiles_recientes", "propio, cuantiles recientes")]
NOMBRE_SINT = {"synthetic_stable_low": "estable y baja", "synthetic_perfect_high": "perfecta y alta",
               "synthetic_periodic_oscillation": "oscilación periódica"}
CTRL = {"basado_en_tasa": "basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "MPC robusto",
        "controlador_propio": "propio", "propio_mediana": "mediana sola", "propio_cuantiles_recientes": "cuantiles recientes",
        "propio_cuantiles_fijos": "cuantiles fijos"}


def coma(x, dec=3, signo=False):
    return ("{0:+.%df}" % dec if signo else "{0:.%df}" % dec).format(x).replace(".", ",").replace("-", "−")


def ic(v, dec=3):
    return "[{0}; {1}]".format(coma(v[0], dec, True), coma(v[1], dec, True))


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def media(xs):
    return sum(xs) / len(xs)


def veces(n):
    return {0: "ninguna vez", 1: "una vez", 2: "dos veces", 3: "tres veces"}.get(n, "{0} veces".format(n))


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from core.evaluacion import contrastes as C

    contr = json.load(open(PAQUETE / "02_resultados" / "contrastes_prerregistrados.json", encoding="utf-8"))
    E = contr["estratos"]
    inter = contr["contenido_nuevo_frente_a_visto"]
    sesiones = leer_csv(PAQUETE / "02_resultados" / "sesiones.csv")
    reales = [s for s in sesiones if s["sintetica"] == "0"]
    sint = [s for s in sesiones if s["sintetica"] == "1"]
    ventanas = leer_csv(PAQUETE / "00_protocolo" / "ventanas_trazas.csv")
    assert len(sint) == 24 and len(reales) == 1184

    # ---- Estratos: recalculo y cotejo ----------------------------------------------------------
    nv = {}
    for clave, _, filtro in ESTRATOS:
        for rival, _ in RIVALES:
            for metrica in ("qoe_lineal_media", "num_stalls"):
                d = C.diferencias_por_ventana(reales, "controlador_propio", rival, metrica, filtro)
                j = E[clave][rival][metrica]
                assert len(d) == j["n_ventanas"] and sum(len(v) for v in d.values()) == j["n_escenarios"]
                assert abs(sum(sum(v) for v in d.values()) / j["n_escenarios"] - j["media_diferencia"]) < 1e-9
            nv[clave] = E[clave][rival]["qoe_lineal_media"]["n_ventanas"]
    assert nv == {"fcc": 18, "oboe": 56, "videos_vistos": 74, "video_nuevo": 74}

    def abs_media(alias, metrica, filtro):
        v = [float(s[metrica]) for s in reales if s["alias_controlador"] == alias and filtro(s)]
        return media(v), len(v)

    absol = {clave: {a: abs_media(a, "qoe_lineal_media", f)[0] for a in ("controlador_propio", "mpc_robusto", "propio_cuantiles_recientes")}
             for clave, _, f in ESTRATOS}
    absp = {clave: {a: abs_media(a, "num_stalls", f)[0] for a in ("controlador_propio", "mpc_robusto", "propio_cuantiles_recientes")}
            for clave, _, f in ESTRATOS}
    assert abs_media("controlador_propio", "qoe_lineal_media", ESTRATOS[0][2])[1] == 36
    # Medias de los ocho con el video nuevo frente al visto.
    todos = sorted({s["alias_controlador"] for s in reales})
    sube_todos = all(abs_media(a, "qoe_lineal_media", ESTRATOS[3][2])[0] > abs_media(a, "qoe_lineal_media", ESTRATOS[2][2])[0] for a in todos)
    assert sube_todos

    # ---- Interaccion de contenido ------------------------------------------------------------
    nuevo = C.diferencias_por_ventana(reales, "controlador_propio", "mpc_robusto", "qoe_lineal_media", ESTRATOS[3][2])
    visto = C.diferencias_por_ventana(reales, "controlador_propio", "mpc_robusto", "qoe_lineal_media", ESTRATOS[2][2])
    inter_v = {v: nuevo[v][0] - visto[v][0] for v in nuevo}
    assert len(inter_v) == 74 and abs(media(list(inter_v.values())) - inter["media_diferencia"]) < 1e-9
    assert inter["ventanas_negativas"] == 40 and inter["ventanas_positivas"] == 31 and inter["ventanas_empate"] == 3
    assert inter["ic95"][1] < 0 < 0.05 and inter["p_valor_bilateral"] > 0.05
    # Ejemplo: la ventana con la interaccion mas negativa (regla fijada antes de mirar).
    v_ej = min(inter_v, key=inter_v.get)
    orden_v = [v["id_ventana_traza"] for v in ventanas]
    num_ej = orden_v.index(v_ej) + 1
    fila_v = next(v for v in ventanas if v["id_ventana_traza"] == v_ej)
    ses_ej = {(s["id_perfil_video"], s["alias_controlador"]): s for s in reales if s["id_ventana_traza"] == v_ej and s["alias_controlador"] in ("controlador_propio", "mpc_robusto")}
    vid_visto = next(k[0] for k in ses_ej if "tears" not in k[0])
    NOMBRE_VIDEO = {"paseo_10min_30fps_4s": "Paseo de Almuñécar a 30 fps", "paseo_10min_60fps_4s": "Paseo de Almuñécar a 60 fps",
                    "blender_10min_30fps_4s": "Blender Sunflower a 30 fps", "blender_10min_60fps_4s": "Blender Sunflower a 60 fps"}

    def q(video, alias):
        return float(ses_ej[(video, alias)]["qoe_lineal_media"])

    def st(video, alias):
        return int(ses_ej[(video, alias)]["num_stalls"])

    def br(video, alias):
        return float(ses_ej[(video, alias)]["bitrate_medio_kbps"])

    # ---- Sinteticas ---------------------------------------------------------------------------
    sint_v = {}
    for s in sint:
        sint_v.setdefault(s["id_ventana_traza"], {})[s["alias_controlador"]] = s
    assert len(sint_v) == 3 and all(len(v) == 8 for v in sint_v.values())
    esc_sint = {v["id_ventana_traza"]: v["escenario_sintetico"] for v in ventanas if v["sintetica"] == "True"}
    assert set(esc_sint.values()) == set(NOMBRE_SINT)
    media_sint = {a: media([float(s["qoe_lineal_media"]) for s in sint if s["alias_controlador"] == a]) for a in todos}
    paradas_sint = {a: sum(int(s["num_stalls"]) for s in sint if s["alias_controlador"] == a) for a in todos}
    orden_sint = sorted(sint_v, key=lambda k: list(NOMBRE_SINT).index(esc_sint[k]))

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.h2("6.6. Análisis secundario exploratorio")
    b.parrafo(
        "Las hipótesis del apartado 6.4 se contrastaron sobre las 74 ventanas en conjunto. Este apartado las "
        "desagrega para entender de dónde sale el resultado y dónde deja de sostenerse: por origen de la red "
        "(las {0} ventanas de la FCC y las {1} de Oboe), por contenido (el vídeo visto frente a Tears of Steel), "
        "con la interacción entre contenido y controlador, y con las tres ventanas sintéticas de diagnóstico. "
        "El protocolo fijó estos análisis como descriptivos: no se corrigen por multiplicidad, los estratos son "
        "más pequeños que la muestra completa y ninguna cifra de este apartado decide nada. Se presentan con "
        "sus intervalos al 95 % por bootstrap de ventanas y se leen como indicios para el apartado 6.7 y para el "
        "trabajo futuro.".format(nv["fcc"], nv["oboe"])
    )

    b.h3("6.6.1. Estratos por origen de la red y por contenido")
    b.parrafo(
        "La Tabla 6.10 repite, dentro de cada estrato, las dos comparaciones centrales del experimento: el propio "
        "frente al MPC robusto y frente a la variante de cuantiles recientes, en QoE lineal y en paradas, con la "
        "media de los escenarios del estrato y su intervalo al 95 % por bootstrap de las ventanas del estrato."
    )
    filas = []
    for clave, nombre, _ in ESTRATOS:
        for rival, nombre_r in RIVALES:
            jq, js = E[clave][rival]["qoe_lineal_media"], E[clave][rival]["num_stalls"]
            filas.append((nombre, str(nv[clave]), nombre_r, "{0} {1}".format(coma(jq["media_diferencia"], 3, True), ic(jq["ic95"])),
                          "{0} {1}".format(coma(js["media_diferencia"], 3, True), ic(js["ic95"]))))
    b.tabla(
        ["Estrato", "Ventanas", "Rival", "ΔQoE lineal (IC95)", "Δparadas por sesión (IC95)"],
        filas,
        "Tabla 6.10: Diferencias entre el controlador propio y dos rivales por estrato: origen de la red y "
        "contenido. Media de los escenarios del estrato e intervalo al 95 % por bootstrap de sus ventanas. "
        "Exploratorio, sin corrección por multiplicidad.",
        anchos_cm=[3.3, 1.9, 3.4, 3.7, 3.7],
        alineaciones=["l", "c", "l", "c", "c"],
    )
    fq, oq = E["fcc"]["mpc_robusto"]["qoe_lineal_media"], E["oboe"]["mpc_robusto"]["qoe_lineal_media"]
    fs, os_ = E["fcc"]["mpc_robusto"]["num_stalls"], E["oboe"]["mpc_robusto"]["num_stalls"]
    b.parrafo(
        "Por origen de la red, la equivalencia global con el MPC robusto se descompone en dos comportamientos "
        "distintos. En las {0} ventanas de la FCC, trazas de acceso fijo con medias altas y poca variación, el "
        "propio obtiene {1} puntos más de QoE, intervalo {2}, y {3} paradas menos por sesión, intervalo {4}: "
        "gana en las dos métricas a la vez, con una QoE media de {5} frente a {6}. En las {7} ventanas de Oboe, "
        "trazas de sesiones de vídeo reales con más variación, cede {8} puntos, intervalo {9}, y para {10} veces "
        "menos por sesión, intervalo {11}: es el compromiso del apartado 6.5, algo menos de bitrate a cambio de "
        "seguridad. Frente a la variante de cuantiles recientes el patrón es el mismo: igualdad en QoE y muchas "
        "menos paradas en la FCC, {12} puntos menos de QoE y {13} paradas menos en Oboe. Con {0} ventanas, el "
        "estrato de la FCC es pequeño y sus intervalos anchos; la lectura prudente es que el propio no pierde "
        "nada en redes fijas estables y que su prudencia tiene un precio pequeño en redes variables.".format(
            nv["fcc"], coma(fq["media_diferencia"], 3), ic(fq["ic95"]), coma(abs(fs["media_diferencia"]), 3), ic(fs["ic95"]),
            coma(absol["fcc"]["controlador_propio"], 3), coma(absol["fcc"]["mpc_robusto"], 3), nv["oboe"],
            coma(abs(oq["media_diferencia"]), 3), ic(oq["ic95"]), coma(abs(os_["media_diferencia"]), 3), ic(os_["ic95"]),
            coma(abs(E["oboe"]["propio_cuantiles_recientes"]["qoe_lineal_media"]["media_diferencia"]), 3),
            coma(abs(E["oboe"]["propio_cuantiles_recientes"]["num_stalls"]["media_diferencia"]), 3))
    )
    vq, nq = E["videos_vistos"]["mpc_robusto"]["qoe_lineal_media"], E["video_nuevo"]["mpc_robusto"]["qoe_lineal_media"]
    vs, ns = E["videos_vistos"]["mpc_robusto"]["num_stalls"], E["video_nuevo"]["mpc_robusto"]["num_stalls"]
    b.parrafo(
        "Por contenido, con los vídeos vistos en el entrenamiento el propio obtiene {0} puntos más de QoE que "
        "el MPC robusto, intervalo {1}, y {2} paradas menos por sesión, intervalo {3}. Con Tears of Steel, el "
        "contenido nuevo, la QoE queda {4} puntos por debajo, intervalo {5}, y la ventaja en paradas se reduce "
        "a {6}, intervalo {7}, que roza el cero. El contenido nuevo no hace fallar al controlador: sigue sin "
        "parar ({8} paradas por sesión, las mismas que con los vistos) y su QoE media es más alta que con los "
        "vídeos vistos ({9} frente a {10}), igual que la de los otros siete controladores, porque los segmentos "
        "reales de Tears of Steel son más pequeños que su tamaño nominal (apartado 6.1). Lo que cambia es la "
        "comparación: el MPC robusto mejora más que el propio con ese contenido.".format(
            coma(vq["media_diferencia"], 3), ic(vq["ic95"]), coma(abs(vs["media_diferencia"]), 3), ic(vs["ic95"]),
            coma(abs(nq["media_diferencia"]), 3), ic(nq["ic95"]), coma(abs(ns["media_diferencia"]), 3), ic(ns["ic95"]),
            coma(absp["video_nuevo"]["controlador_propio"], 3), coma(absol["video_nuevo"]["controlador_propio"], 3),
            coma(absol["videos_vistos"]["controlador_propio"], 3))
    )
    assert abs(absp["video_nuevo"]["controlador_propio"] - absp["videos_vistos"]["controlador_propio"]) < 1e-9

    b.h3("6.6.2. Interacción entre contenido y controlador")
    b.parrafo(
        "La medida directa de ese cambio es la interacción de contenido, calculada ventana a ventana: la "
        "diferencia propio menos MPC robusto con Tears of Steel menos esa misma diferencia con el vídeo visto. "
        "Su media es {0} puntos de QoE, intervalo {1}, y la prueba del signo bilateral da p = {2}, con {3} "
        "ventanas negativas, {4} positivas y {5} empates. Las dos lecturas no coinciden del todo: el intervalo "
        "excluye el cero, pero el recuento de ventanas no está lejos del empate. Es decir, en la mayoría de las "
        "ventanas la interacción es pequeña y de signo variable, y la media la mueven unas pocas ventanas en las "
        "que la diferencia entre los dos controladores cambia mucho de un vídeo al otro, a menudo por una sola "
        "parada. Es un resultado exploratorio y se informa tal "
        "cual: con el contenido nuevo la equivalencia en QoE se mantiene dentro del margen, pero la ventaja en "
        "paradas se estrecha.".format(
            coma(inter["media_diferencia"], 3, True), ic(inter["ic95"]), coma(inter["p_valor_bilateral"], 2),
            inter["ventanas_negativas"], inter["ventanas_positivas"], inter["ventanas_empate"])
    )
    b.parrafo(
        "Hay dos hipótesis de trabajo, no comprobadas en este experimento, sobre el porqué. La primera es la "
        "variabilidad del tamaño de los segmentos: en Tears of Steel el coeficiente de variación dentro de un "
        "nivel está entre 0,28 y 0,31, frente a un máximo de 0,19 en los vídeos vistos (apartado 6.1), y el "
        "planificador del propio y del MPC robusto usan ambos los tamaños reales, pero el predictor del propio "
        "aprendió a interpretar el throughput medido con descargas de tamaño poco variable. La segunda es el "
        "arranque: los dos primeros segmentos de Tears of Steel son casi negros, entre un 2 y un 6 % del "
        "tamaño nominal, y las primeras medidas de throughput de la sesión, calculadas sobre descargas "
        "diminutas, son poco fiables; el MPC robusto las rebaja por su error máximo y el propio las pasa por "
        "la red, que nunca vio descargas así. Comprobar cualquiera de las dos exigiría un experimento con más "
        "contenidos, y queda como trabajo futuro (apartado 7.4). La ventana {6}, una traza de {7}, es la de "
        "interacción más negativa y enseña lo que hay detrás de la media: con {8} el propio obtuvo {9} de "
        "QoE y el MPC robusto {10}, y con Tears of Steel {11} y {12}; la interacción es {13}. Con el vídeo visto "
        "el propio paró {16} y el MPC robusto {17}; con Tears of Steel, {18} y {19}, y el bitrate medio fue de "
        "{14} frente a {15} kbit/s.".format(
            0, 0, 0, 0, 0, 0, num_ej, "Oboe" if fila_v["id_dataset"] == "oboe" else "la FCC", NOMBRE_VIDEO[vid_visto],
            coma(q(vid_visto, "controlador_propio"), 3), coma(q(vid_visto, "mpc_robusto"), 3),
            coma(q("tears_10min_30fps_4s", "controlador_propio"), 3), coma(q("tears_10min_30fps_4s", "mpc_robusto"), 3),
            coma(inter_v[v_ej], 3, True), coma(br("tears_10min_30fps_4s", "controlador_propio"), 0), coma(br("tears_10min_30fps_4s", "mpc_robusto"), 0),
            veces(st(vid_visto, "controlador_propio")), veces(st(vid_visto, "mpc_robusto")), veces(st("tears_10min_30fps_4s", "controlador_propio")), veces(st("tears_10min_30fps_4s", "mpc_robusto")))
    )

    b.h3("6.6.3. Ventanas sintéticas de diagnóstico")
    b.parrafo(
        "Las tres ventanas sintéticas no entran en ningún contraste; sirven para comprobar que los "
        "controladores se comportan como se espera en redes de forma conocida. Con la red estable y baja, el "
        "propio, sus variantes y el MPC robusto quedan en {0} a {1} puntos de QoE, los clásicos por debajo. Con "
        "la red perfecta y alta, todos los que planifican alcanzan el techo de la escalera y obtienen la misma "
        "QoE, {2}, mientras que los clásicos se quedan en {3} a {4}: la red sobra y solo cuenta la rapidez en "
        "subir. Con la oscilación periódica, la ventana que más separa a los controladores, el propio obtiene "
        "{5} y el MPC robusto {6}, mientras que las variantes de ablación y BBA suben a {7} a {8}: las variantes "
        "siguen la oscilación y el propio la amortigua, con el coste en QoE que eso tiene cuando la oscilación "
        "no llega a vaciar el buffer. En las tres ventanas juntas, el propio promedia {9} puntos con {10} "
        "paradas y el MPC robusto {11} con {12} parada; con tres ventanas no se concluye nada, pero ninguna "
        "contradice lo observado en las reales.".format(
            coma(min(float(sint_v[orden_sint[0]][a]["qoe_lineal_media"]) for a in ("controlador_propio", "mpc_robusto", "propio_mediana", "propio_cuantiles_recientes", "propio_cuantiles_fijos")), 2),
            coma(max(float(sint_v[orden_sint[0]][a]["qoe_lineal_media"]) for a in ("controlador_propio", "mpc_robusto", "propio_mediana", "propio_cuantiles_recientes", "propio_cuantiles_fijos")), 2),
            coma(float(sint_v[orden_sint[1]]["controlador_propio"]["qoe_lineal_media"]), 2),
            coma(min(float(sint_v[orden_sint[1]][a]["qoe_lineal_media"]) for a in ("bba", "basado_en_tasa", "bola")), 2),
            coma(max(float(sint_v[orden_sint[1]][a]["qoe_lineal_media"]) for a in ("bba", "basado_en_tasa", "bola")), 2),
            coma(float(sint_v[orden_sint[2]]["controlador_propio"]["qoe_lineal_media"]), 2), coma(float(sint_v[orden_sint[2]]["mpc_robusto"]["qoe_lineal_media"]), 2),
            coma(min(float(sint_v[orden_sint[2]][a]["qoe_lineal_media"]) for a in ("bba", "propio_mediana", "propio_cuantiles_recientes", "propio_cuantiles_fijos")), 2),
            coma(max(float(sint_v[orden_sint[2]][a]["qoe_lineal_media"]) for a in ("bba", "propio_mediana", "propio_cuantiles_recientes", "propio_cuantiles_fijos")), 2),
            coma(media_sint["controlador_propio"], 3), paradas_sint["controlador_propio"], coma(media_sint["mpc_robusto"], 3), paradas_sint["mpc_robusto"])
    )
    assert paradas_sint["controlador_propio"] == 0 and paradas_sint["mpc_robusto"] == 1
    assert len({round(float(sint_v[orden_sint[1]][a]["qoe_lineal_media"]), 6) for a in ("controlador_propio", "mpc_robusto", "propio_mediana", "propio_cuantiles_recientes", "propio_cuantiles_fijos")}) == 1
    b.parrafo(
        "En resumen, el análisis secundario no cambia la respuesta de las hipótesis pero sí la matiza: la "
        "equivalencia en QoE y la ventaja en paradas se sostienen en los dos orígenes de red, con más holgura "
        "en las redes fijas que en las variables; con el contenido nuevo la equivalencia se mantiene y la "
        "ventaja en paradas se estrecha, por motivos que este experimento no puede separar. El apartado 6.7 "
        "reúne lo que se puede afirmar con todo lo anterior y lo que queda fuera."
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("ejemplo", v_ej, num_ej, fila_v["id_dataset"], vid_visto, round(inter_v[v_ej], 4), {k: (round(float(v["qoe_lineal_media"]), 3), v["num_stalls"], round(float(v["bitrate_medio_kbps"]))) for k, v in ses_ej.items()})
    print("sinteticas", orden_sint, {a: round(v, 3) for a, v in media_sint.items()}, paradas_sint)
    print("absol", {k: {a: round(x, 3) for a, x in v.items()} for k, v in absol.items()})


if __name__ == "__main__":
    main()
