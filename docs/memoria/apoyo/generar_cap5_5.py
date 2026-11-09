# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap5_5_controladores_clasicos.docx y la Figura 5.3.

Ejemplo real reproducible, con regla fijada antes de mirar el resultado: la primera sesion del MPC
robusto en el orden del plan del experimento final cuya ventana es de Oboe (trazas variables, donde la
correccion robusta tiene algo que corregir) y cuyo video es uno visto; dentro de ella, la primera
decision con historial de cinco descargas y ventana de cinco errores completos. Se reproducen las 29
decisiones de la sesion con el codigo del entregable a partir de la realimentacion registrada en
telemetria_segmentos.csv, como hace la auditoria de decisiones, y se comprueba que coinciden con las
registradas en la VM.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap5_5.py
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla, m_d, m_f, m_r, m_sub  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIG_SVG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_3_decision_mpc_robusto.svg"
FIG_PNG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_3_decision_mpc_robusto.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap5_5_controladores_clasicos.docx"
sys.path.insert(0, str(CODIGO))

ENTERO = re.compile(r"-?\d+")


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def _valor(texto, clave):
    if texto == "":
        return None
    if clave == "tasas":
        return json.loads(texto)
    return int(texto) if ENTERO.fullmatch(texto) else float(texto)


def reproducir_sesion_mpc():
    from core.controladores.robust_mpc import ControladorMpcRobusto
    from core.controladores.entradas_planificador import estado_desde_carga, segmentos_video_sesion
    from core.feedback_reproductor import CLAVES_REALIMENTACION, construir_realimentacion_controlador
    from core.modelo_propio.estado_sesion import media_armonica_bps
    from core.modelo_propio.planificador import planificar_accion

    plan = json.load(open(PAQUETE / "00_protocolo" / "plan_sesiones.json", encoding="utf-8"))["sesiones"]
    sesion = next(
        s for s in plan
        if s["alias_controlador"] == "mpc_robusto" and s["id_dataset"] == "oboe" and s["id_perfil_video"] != "tears_10min_30fps_4s"
    )
    dir_ejec = sorted(glob.glob(os.path.join(str(PAQUETE), "01_ejecucion", "ejecuciones", sesion["id_sesion"], "ejecucion_*")))[-1]
    filas = list(csv.DictReader(open(os.path.join(dir_ejec, "telemetria_segmentos.csv"), encoding="utf-8")))
    config = json.load(open(PAQUETE / "00_protocolo" / "configs_cliente" / (sesion["id_sesion"] + ".yaml"), encoding="utf-8"))
    parametros = dict(config["controlador"]["parametros"])
    mpc = ControladorMpcRobusto(**parametros)

    def fb_de(fila):
        return {clave: _valor(fila["feedback_" + clave], clave) for clave in CLAVES_REALIMENTACION}

    primera = fb_de(filas[0])
    mpc.fijarFeedbackReproductor(
        construir_realimentacion_controlador(
            bytes_en_cola=0, tiempo_en_cola=0, tasas=list(primera["tasas"]), duraciones_fragmentos=[4.0] * 6,
            nivel_actual=int(config["reproduccion"]["calidad_inicial"]), nivel_max=primera["nivel_max"],
            bytes_descargados=0, indice_segmento=0, inicio_peticion_segmento=None, fin_peticion_segmento=None,
            ultimo_tamano=0, ultimo_tiempo=0.0, duracion_fragmento=None, segmentos_totales=primera["segmentos_totales"],
        )
    )
    decisiones, iguales, ejemplo = 0, 0, None
    nivel_previo = int(config["reproduccion"]["calidad_inicial"])
    for fila in filas:
        fb = fb_de(fila)
        mpc.fijarFeedbackReproductor(fb)
        if fila["es_init"] == "1" or not (fila.get("tasa_objetivo_politica") or "").strip():
            continue
        tasa = mpc.calcularAccionControl()
        nivel = min(mpc.cuantizarTasa(tasa), int(fila["feedback_nivel_max"]))
        decisiones += 1
        coincide = nivel == int(fila["nivel_elegido_politica"]) and float(tasa) == float(fila["tasa_objetivo_politica"])
        iguales += int(coincide)
        m = dict(mpc.ultimas_metricas)
        if ejemplo is None and len(m["errores_prediccion"]) == 5 and len(m["historial_throughput_bps"]) == 5:
            errores = list(m["errores_prediccion"])
            historial = list(m["historial_throughput_bps"])
            hm = media_armonica_bps(historial)
            # Decision del MPC no robusto en el mismo estado (misma carga, prediccion = media armonica).
            carga = mpc.constructor_entradas.construir(fb)
            estado = estado_desde_carga(carga.entradas_contexto, carga.tasas_Bps, fb)
            escalera = mpc._asegurar_escalera(carga.tasas_Bps, segmentos_video_sesion(fb))
            basica = planificar_accion(
                estado=estado, escalera=escalera, prediccion_bps_por_horizonte_y_cuantil=[(hm,)] * mpc.horizonte,
                cuantiles=(0.5,), horizonte_segmentos=mpc.horizonte, mascara_acciones=carga.mascara_acciones,
                alfa_riesgo=1.0, peso_rebuffering=mpc.penalizacion_rebuffering, peso_cambios=mpc.penalizacion_cambios,
            )
            tamanos = [
                [escalera.bytes_segmento(n, estado.indice_segmento + paso) for paso in range(mpc.horizonte)]
                for n in range(escalera.num_representaciones)
            ]
            ejemplo = {
                "indice_segmento": int(fila["indice_segmento"]), "nivel_previo": nivel_previo, "nivel": nivel,
                "buffer_s": float(fb["tiempo_en_cola"]), "historial_bps": historial, "media_armonica_bps": hm,
                "errores": errores, "error_max": max(errores) if errores else 0.0,
                "prediccion_bps": float(m["throughput_previsto_bps"]), "secuencia": list(m["mejor_secuencia"]),
                "puntuacion": float(m["mejor_puntuacion"]), "secuencia_basica": list(basica.mejor_secuencia),
                "puntuacion_basica": float(basica.cvar_puntuacion), "bitrates_kbps": [b / 1000 for b in escalera.bitrates_bps],
                "tamanos_bytes": tamanos, "indice_video": estado.indice_segmento, "registrado": int(fila["nivel_elegido_politica"]),
            }
        nivel_previo = nivel
    assert decisiones == 29 and iguales == 29, (decisiones, iguales)
    assert ejemplo is not None and ejemplo["nivel"] == ejemplo["registrado"]
    return sesion, ejemplo


def figura(ej):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    gris, gris_osc, azul, amarillo, rojo = "#adb5bd", "#495057", "#1971c2", "#f5d76e", "#c92a2a"
    plt.rcParams.update({"font.family": "Arial", "font.size": 9})
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.4, 2.9), gridspec_kw={"width_ratios": [1.0, 1.25]})

    # (a) historial, media armonica y prediccion robusta
    h = [v / 1e6 for v in ej["historial_bps"]]
    x = list(range(1, len(h) + 1))
    a.bar(x, h, color=gris, width=0.6, label="throughput de las últimas descargas")
    hm = ej["media_armonica_bps"] / 1e6
    pr = ej["prediccion_bps"] / 1e6
    a.axhline(hm, color=gris_osc, lw=1.2, label="media armónica: {0} Mbit/s".format(coma(hm)))
    a.axhline(pr, color=azul, lw=1.6, ls="--", label="predicción robusta: {0} Mbit/s".format(coma(pr)))
    a.set_xlabel("descarga (de la más antigua a la más reciente)")
    a.set_ylabel("Mbit/s")
    a.set_xticks(x)
    a.set_title("(a) Predicción", loc="left", fontsize=9, fontweight="bold")
    a.legend(fontsize=7, loc="upper left", frameon=False)
    a.set_ylim(0, max(h) * 1.45)
    for s in ("top", "right"):
        a.spines[s].set_visible(False)

    # (b) secuencias elegidas en el horizonte
    pasos = list(range(1, len(ej["secuencia"]) + 1))
    kb = ej["bitrates_kbps"]
    seq_r = [kb[n] / 1000 for n in ej["secuencia"]]
    seq_b = [kb[n] / 1000 for n in ej["secuencia_basica"]]
    b.step([0] + pasos, [kb[ej["nivel_previo"]] / 1000] + seq_b, where="post", color=gris_osc, lw=1.2,
           label="MPC con la media armónica: {0}".format(" ".join(str(n) for n in ej["secuencia_basica"])))
    b.step([0] + pasos, [kb[ej["nivel_previo"]] / 1000] + seq_r, where="post", color=azul, lw=2.0,
           label="MPC robusto (aplicado): {0}".format(" ".join(str(n) for n in ej["secuencia"])))
    for nivel, kbps in enumerate(kb):
        b.axhline(kbps / 1000, color="#e9ecef", lw=0.8, zorder=0)
        b.text(5.15, kbps / 1000, "nivel {0}".format(nivel), fontsize=6.5, color=gris_osc, va="center")
    b.set_xlim(0, 5.9)
    b.set_xticks(pasos)
    b.set_xlabel("segmento del horizonte (1 = el que se decide)")
    b.set_ylabel("Mbit/s nominales")
    b.set_title("(b) Secuencias elegidas, buffer {0} s".format(coma(ej["buffer_s"], 1)), loc="left", fontsize=9, fontweight="bold")
    b.legend(fontsize=7, loc="upper left", frameon=False)
    for s in ("top", "right"):
        b.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(FIG_SVG)
    fig.savefig(FIG_PNG, dpi=220)
    plt.close(fig)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    sesion, ej = reproducir_sesion_mpc()
    figura(ej)

    h_mbps = [coma(v / 1e6) for v in ej["historial_bps"]]
    err_pct = [coma(100 * e, 0) for e in ej["errores"]]
    hm = ej["media_armonica_bps"] / 1e6
    pr = ej["prediccion_bps"] / 1e6
    kb = ej["bitrates_kbps"]

    b = Borrador(PLANTILLA)
    b.h2("5.5. Implementación de los controladores clásicos")
    b.parrafo(
        "Los controladores clásicos son los comparadores del capítulo 6. Sobre la interfaz común del apartado "
        "4.5 se implementan cuatro algoritmos de la literatura: el basado en tasa, BBA, BOLA y el MPC robusto, "
        "que es la referencia fuerte de la comparativa. El MPC básico existe también en el registro como paso "
        "intermedio hacia su variante robusta, pero no corre en la evaluación. Este apartado describe la "
        "estructura común, la regla de decisión de cada uno con sus parámetros, el planificador que el MPC "
        "robusto comparte con el controlador propio y una decisión real del MPC robusto reproducida con el "
        "código entregado."
    )

    b.h3("5.5.1. Principios comunes")
    b.parrafo(
        "Dos principios guían la implementación. El primero es la fidelidad a la referencia publicada: cada "
        "controlador reproduce la regla de decisión del artículo o del código de referencia, con sus parámetros, "
        "y toda simplificación se declara. El segundo es la neutralidad respecto al cliente: cada controlador "
        "lee del contrato de realimentación solo las señales que su algoritmo contempla, de modo que las "
        "diferencias de comportamiento vienen del algoritmo y no de un acceso privilegiado a la información. "
        "Así ordenados por la información que usan, el basado en tasa decide con la medida de la última "
        "descarga, BBA solo con la ocupación del buffer, BOLA con la ocupación y la escalera, y el MPC robusto "
        "con la ocupación, un historial de cinco descargas, la memoria de sus propios errores de predicción y "
        "los tamaños reales de los segmentos del vídeo."
    )
    b.parrafo(
        "Los cuatro comparten una plantilla. En cada decisión validan la escalera recibida (valores positivos, "
        "recortada al nivel máximo permitido), acotan todo índice al rango válido y devuelven la tasa objetivo "
        "en bytes por segundo, que el reproductor cuantiza al escalón común. Los casos degenerados tienen "
        "respuesta explícita: sin escalera, tasa cero; con una sola representación, esa; con una señal ausente "
        "o inválida, el nivel de arranque o el mínimo. Un parámetro de configuración inválido se sustituye por "
        "el valor por defecto del módulo. Ninguno usa aleatoriedad: ante la misma realimentación y el mismo "
        "estado interno, la decisión es la misma, lo que permite auditar cada decisión fuera de línea "
        "(apartado 6.1). En la evaluación final los cuatro corrieron con sus parámetros por defecto; la "
        "configuración de cada sesión solo les pasa el identificador del vídeo, que únicamente el MPC robusto "
        "utiliza. La Tabla 5.7 resume regla, parámetros e información de cada uno."
    )
    b.tabla(
        ["Controlador", "Referencia", "Regla de decisión", "Parámetros", "Información que usa"],
        [
            ("Basado en tasa", "[liu2011rateAdaptation]",
             "Escalón más alto bajo 0,85 × throughput suavizado; sube un nivel por decisión; baja sin límite",
             "suavizado α = 0,5; factor 0,85; buffer crítico 2 s", "última descarga (tamaño/tiempo); buffer solo como guarda"),
            ("BBA (BBA-0)", "[huang2014bba]",
             "Mapa por tramos de la ocupación: mínima bajo la reserva, lineal en el colchón, máxima por encima",
             "reserva 5 s; colchón 10 s", "solo la ocupación del buffer"),
            ("BOLA (básico)", "[spiteri2020bola]",
             "Máximo de (V(υ~m~ + γp) − Q)/S~m~ con υ~m~ = ln(S~m~/S~1~); mínima si ninguna puntuación es positiva",
             "V = 5; γ = 0,2; mínima si buffer ≤ p", "ocupación, duración del segmento y escalera (tamaños nominales)"),
            ("MPC robusto (canónico)", "[yin2015mpc], [mao2017pensieve]",
             "Primera acción de la mejor secuencia de 5 segmentos con QoE lineal; predicción = media armónica de "
             "5 descargas dividida por (1 + error máximo)",
             "horizonte 5; ventana 5; pesos 4,3 y 1; ventana de error 5",
             "ocupación, historial de 5 descargas, errores propios y tamaños reales de los segmentos"),
        ],
        "Tabla 5.7: Controladores clásicos implementados: referencia, regla de decisión, parámetros empleados en "
        "la evaluación final (valores por defecto del código) e información del contrato que utiliza cada uno.",
        anchos_cm=[2.4, 2.4, 5.0, 3.0, 3.2],
    )

    b.h3("5.5.2. Basado en tasa, BBA y BOLA")
    b.parrafo(
        "El controlador basado en tasa reproduce la adaptación dirigida por el receptor de Liu et al. "
        "[liu2011rateAdaptation]: medir el throughput de cada descarga en la capa de aplicación, suavizarlo y "
        "elegir la representación más alta que quepa bajo una estimación conservadora, sin información de la "
        "capa de transporte. El artículo compara el tiempo de descarga del segmento con su duración; la "
        "implementación usa la misma información como cociente tamaño entre tiempo, que es la medida cruda del "
        "contrato, con un suavizado exponencial de α = 0,5 y un factor de seguridad de 0,85. Las dos asimetrías "
        "del artículo se conservan: la subida se limita a un nivel por decisión y, si la medida instantánea con "
        "su factor ya no sostiene el nivel actual, se decide con la menor entre la suavizada y la instantánea, "
        "lo que permite bajar varios niveles de golpe. El buffer interviene solo como guarda: por debajo de 2 s "
        "se fuerza al menos un nivel menos que el actual."
    )
    b.parrafo(
        "BBA implementa el mapa de tasa de Huang et al. [huang2014bba] en su forma más simple, la que los "
        "autores llaman BBA-0. Por debajo de la reserva (5 s) se pide la representación mínima; por encima de "
        "la reserva más el colchón (15 s), la máxima; y en el colchón el nivel crece linealmente con la "
        "ocupación, redondeado hacia abajo al índice de la escalera. Reserva y colchón son los valores con que "
        "Yin et al. reproducen BBA como comparador [yin2015mpc]. El controlador ignora toda medida de "
        "throughput. El estimador de capacidad que el artículo propone para el arranque se omite, porque el "
        "transitorio de arranque queda fuera de la evaluación (apartado 4.6)."
    )
    b.parrafo(
        "BOLA implementa la versión básica de Spiteri et al. [spiteri2020bola], la que los autores derivan "
        "directamente de su problema de optimización y llaman BOLA-BASIC. En cada decisión se elige la "
        "representación m que maximiza:"
    )
    b.ecuacion(
        m_f(m_r("V") + m_d(m_sub(m_r("υ"), m_r("m")) + m_r("+", cursiva=False) + m_r("γ") + m_r("p"))
            + m_r("−", cursiva=False) + m_r("Q"), m_sub(m_r("S"), m_r("m")))
        + m_r(",   ", cursiva=False) + m_sub(m_r("υ"), m_r("m")) + m_r("=", cursiva=False)
        + m_r("ln", cursiva=False) + m_d(m_f(m_sub(m_r("S"), m_r("m")), m_sub(m_r("S"), m_r("1")))),
        "5.4",
    )
    b.parrafo(
        "donde Q es la ocupación del buffer en segmentos, p la duración del segmento en segundos, S~m~ el "
        "tamaño nominal de la representación m (tasa por duración), υ~m~ su utilidad logarítmica respecto a la "
        "mínima y V y γ los parámetros de control. Los tamaños se normalizan al menor, lo que no altera la "
        "representación ganadora. Dos decisiones propias se declaran. El artículo contempla no descargar cuando "
        "ninguna puntuación es positiva; el contrato del apartado 4.5 no expresa esa opción, así que se elige la "
        "mínima, y en la práctica el tope del buffer del apartado 4.3 detiene antes las descargas. Y los "
        "parámetros se fijan por configuración (V = 5, γ = 0,2) en lugar de derivarse de un objetivo de "
        "ocupación como propone el artículo, de modo que BOLA se evalúa con una parametrización razonable pero "
        "no calibrada. No se incorporan las mejoras que los mismos autores añadieron al reproductor de "
        "referencia dash.js (segmentos virtuales, conmutación dinámica a una regla de throughput con buffer "
        "bajo y sustitución de segmentos) [spiteri2019dashjs], que responden a necesidades de producción."
    )

    b.h3("5.5.3. El MPC robusto canónico y el planificador compartido")
    b.parrafo(
        "El MPC robusto se implementa en la forma canónica de Yin et al. [yin2015mpc] tal como la fija el código "
        "de referencia publicado con Pensieve, que es la versión que la literatura posterior usa como comparador "
        "[mao2017pensieve]: horizonte de cinco segmentos, calidad lineal en Mbit/s, penalizaciones de 4,3 por "
        "segundo de rebuffering y 1 por Mbit/s de cambio, tamaños reales de los segmentos del vídeo y predicción "
        "por media armónica de las cinco últimas descargas. Se descartó la alternativa de un MPC con horizonte "
        "corto, utilidad logarítmica y tamaños nominales: no se corresponde con ninguna referencia publicada y "
        "habría dejado al comparador en desventaja frente al controlador propio, que sí planifica con tamaños "
        "reales."
    )
    b.parrafo(
        "El MPC robusto decide con el mismo planificador que el controlador propio (apartado 5.6), alimentado "
        "con un único escenario de throughput. El planificador enumera las 6⁵ = 7776 secuencias de niveles del "
        "horizonte, simula para cada una la evolución del buffer con los tamaños reales de los segmentos que "
        "vienen y la puntúa con la QoE lineal acumulada:"
    )
    b.ecuacion(
        m_r("J") + m_d(m_r("a")) + m_r("=", cursiva=False)
        + '<m:nary><m:naryPr><m:chr m:val="∑"/></m:naryPr><m:sub>' + m_r("j") + m_r("=", cursiva=False) + m_r("1", cursiva=False)
        + "</m:sub><m:sup>" + m_r("5", cursiva=False) + "</m:sup><m:e>"
        + m_d(m_f(m_sub(m_r("R"), m_sub(m_r("a"), m_r("j"))), m_r("10⁶", cursiva=False))
              + m_r("−", cursiva=False) + m_r("4,3", cursiva=False) + m_r("·", cursiva=False)
              + m_sub(m_r("ρ"), m_r("j")) + m_r("−", cursiva=False)
              + m_f(m_d(m_sub(m_r("R"), m_sub(m_r("a"), m_r("j"))) + m_r("−", cursiva=False)
                        + m_sub(m_r("R"), m_sub(m_r("a"), m_r("j−1"))), abre="|", cierra="|"), m_r("10⁶", cursiva=False)))
        + "</m:e></m:nary>",
        "5.5",
    )
    b.parrafo(
        "donde a es la secuencia de niveles, R~a~ el bitrate nominal en bit/s del nivel elegido en cada paso, "
        "ρ~j~ el rebuffering previsto en el paso j en segundos (el tiempo de descarga del segmento real a la "
        "predicción menos el buffer disponible, si es positivo) y a~0~ el nivel del segmento anterior. Se aplica "
        "la primera acción de la secuencia de mayor puntuación y el proceso se repite en el segmento siguiente. "
        "La predicción robusta sigue la formulación del artículo: la media armónica de las cinco últimas "
        "descargas se divide por uno más el mayor error porcentual que esa media cometió en las cinco "
        "descargas anteriores:"
    )
    b.ecuacion(
        m_sub(m_r("Ĉ"), m_r("k")) + m_r("=", cursiva=False)
        + m_f(m_r("HM", cursiva=False) + m_d(m_sub(m_r("C"), m_r("k−5")) + m_r(", …, ", cursiva=False) + m_sub(m_r("C"), m_r("k−1"))),
              m_r("1", cursiva=False) + m_r("+", cursiva=False) + m_r("err", cursiva=False))
        + m_r(",   ", cursiva=False) + m_r("err", cursiva=False) + m_r("=", cursiva=False)
        + '<m:func><m:fName>' + m_r("max", cursiva=False) + "</m:fName><m:e>"
        + m_f(m_d(m_sub(m_r("Ĉ"), m_r("i")) + m_r("−", cursiva=False) + m_sub(m_r("C"), m_r("i")), abre="|", cierra="|"),
              m_sub(m_r("C"), m_r("i")))
        + "</m:e></m:func>",
        "5.6",
    )
    b.parrafo(
        "donde C~i~ es el throughput medido en la descarga i, Ĉ~i~ la media armónica que se predijo para ella y "
        "el máximo recorre las cinco descargas anteriores a k. El error se mide contra la media armónica, no "
        "contra la predicción ya rebajada; sin errores previos la predicción es la media armónica, sin factor de "
        "arranque; y la descarga de calentamiento también entra en el historial. Yin et al. demuestran que este "
        "control robusto equivale al MPC ordinario alimentado con la cota inferior del throughput "
        "[yin2015mpc], y así se implementa. La Tabla 5.8 recoge cada elemento con su fuente, su valor en el "
        "código y la prueba automática que lo fija."
    )
    b.tabla(
        ["Elemento", "Referencia", "En el código", "Prueba"],
        [
            ("Horizonte", "5 segmentos [yin2015mpc], [mao2017pensieve]", "5; se acorta al final del vídeo", "misma acción que el bucle de referencia"),
            ("Calidad", "lineal, q(R) = R [mao2017pensieve]", "R en Mbit/s", "misma acción que el bucle de referencia"),
            ("Penalizaciones", "4,3 por s de rebuffering; 1 por Mbit/s de cambio [mao2017pensieve]", "4,3 y 1,0", "misma acción que el bucle de referencia"),
            ("Tamaños", "tamaño real de cada segmento (código de referencia)", "descriptor del vídeo de la sesión", "misma acción que el bucle de referencia"),
            ("Predicción", "media armónica de 5 descargas [yin2015mpc]", "5, con la de calentamiento", "el historial incluye el calentamiento"),
            ("Robustez", "Ĉ/(1 + err), err máximo de 5 [yin2015mpc]", "ecuación (5.6)", "error frente a la media armónica"),
            ("Arranque", "sin factor (código de referencia)", "sin errores previos, Ĉ = HM", "sin errores la predicción es la media armónica"),
            ("Descriptor", "—", "se lee al crear el controlador", "falla si falta el descriptor"),
        ],
        "Tabla 5.8: Mapa del MPC robusto canónico: cada elemento de la regla con su referencia, su valor en el "
        "código del entregable y la prueba automática de la carpeta de pruebas que lo comprueba.",
        anchos_cm=[2.6, 5.4, 4.0, 4.0],
    )
    b.parrafo(
        "La prueba principal compara, en 400 estados aleatorios con los tamaños reales de un vídeo del "
        "experimento, la secuencia que elige el planificador con una copia literal del bucle de referencia: la "
        "secuencia elegida tiene siempre la recompensa máxima de ese bucle y la acción coincide en al menos 390 "
        "casos; el resto son empates exactos de recompensa que se resuelven por el orden de las sumas en coma "
        "flotante. El MPC robusto es además el respaldo del controlador propio (apartado 5.6): se crea junto a él "
        "para el mismo vídeo y recibe toda la realimentación de la sesión."
    )

    b.h3("5.5.4. Una decisión real del MPC robusto")
    b.parrafo(
        "Para fijar ideas se reproduce una decisión del experimento final con el código entregado. La regla de "
        "selección se fijó antes de mirar el resultado: la primera sesión del MPC robusto en el orden del plan "
        "cuya ventana de red procede de Oboe, donde el throughput varía y la corrección robusta tiene algo que "
        "corregir, con un vídeo visto: es la sesión {0} del plan, en la ventana real {1} de Oboe con el vídeo {2}. "
        "Dentro de ella se toma la primera decisión con historial de cinco descargas y cinco errores de predicción "
        "ya medidos. Las 29 decisiones de la sesión, reproducidas a partir de la realimentación registrada, "
        "coinciden con las que tomó la máquina virtual. La Figura 5.3 muestra esa decisión, en el segmento {3}, "
        "con el buffer en {4} s y el nivel anterior {5}.".format(
            int(sesion["id_sesion"][1:6]), sesion["id_ventana_traza"].split("_")[1], sesion["nombre_visible_video"],
            ej["indice_segmento"], coma(ej["buffer_s"], 1), ej["nivel_previo"]
        )
    )
    b.figura(
        FIG_PNG,
        "Figura 5.3: Decisión real del MPC robusto en el segmento {0} de la sesión //{1}//. (a) Throughput de las "
        "cinco últimas descargas, media armónica y predicción robusta. (b) Secuencia de niveles de mayor "
        "puntuación en el horizonte de cinco segmentos con la predicción robusta (aplicada) y con la media "
        "armónica sin rebajar.".format(ej["indice_segmento"], sesion["id_sesion"]),
        ancho_cm=16.0,
    )
    b.parrafo(
        "Las cinco últimas descargas midieron {0} Mbit/s; su media armónica es {1} Mbit/s. Los errores "
        "porcentuales de esa media en las cinco descargas anteriores fueron del {2} %, con máximo del {3} %, "
        "así que la predicción robusta queda en {4} Mbit/s. Con ella, la mejor secuencia es {5} (puntuación "
        "{6}) y se aplica el nivel {7}, de {8} kbit/s. Con la media armónica sin rebajar, el mismo planificador "
        "habría elegido la secuencia {9}{10}".format(
            ", ".join(h_mbps), coma(hm), ", ".join(err_pct), coma(100 * ej["error_max"], 0), coma(pr),
            " ".join(str(n) for n in ej["secuencia"]), coma(ej["puntuacion"]), ej["nivel"], int(kb[ej["nivel"]]),
            " ".join(str(n) for n in ej["secuencia_basica"]),
            (": la corrección robusta es lo que separa las dos decisiones en este estado."
             if ej["secuencia_basica"] != ej["secuencia"]
             else ", la misma: en este estado la corrección robusta no cambia la decisión, aunque sí la puntuación prevista."),
        )
    )
    b.parrafo(
        "Los límites de los comparadores son los declarados en cada párrafo: el basado en tasa mide con el "
        "cociente del contrato y no con el tiempo de descarga del artículo, BBA no lleva estimador de arranque, "
        "BOLA no está calibrado ni contempla la no descarga, y los tres deciden con tamaños nominales, como sus "
        "formulaciones. El MPC robusto es el único clásico que usa los tamaños reales, igual que el controlador "
        "propio, de modo que la comparación del capítulo 6 entre ambos aísla la predicción: todo lo demás es "
        "idéntico. El apartado 5.6 describe el controlador propio."
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("ejemplo:", json.dumps({k: v for k, v in ej.items() if k not in ("tamanos_bytes",)}, ensure_ascii=True))


if __name__ == "__main__":
    main()
