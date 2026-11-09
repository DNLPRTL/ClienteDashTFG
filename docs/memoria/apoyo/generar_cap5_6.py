# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap5_6_controlador_propio.docx y la Figura 5.5.

Lee resumen_propio_final.json, producido por reproducir_propio_final.py sobre el paquete del
experimento final (4379 decisiones del controlador propio reproducidas con el codigo del
entregable y variantes sobre el mismo estado). Lee ademas latencias de decision de la telemetria.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap5_6.py
"""
from __future__ import annotations

import csv
import glob
import json
import os
import statistics
import sys
from pathlib import Path

import numpy as np

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla, m_d, m_f, m_r, m_sub  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
RESUMEN = Path(__file__).resolve().parent / "resumen_propio_final.json"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIG_ARQ = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_4_arquitectura_controlador_propio.png"
FIG_DEC_SVG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_5_decision_propio.svg"
FIG_DEC_PNG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_5_decision_propio.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap5_6_controlador_propio.docx"


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def miles(n):
    return "{0:,}".format(int(n)).replace(",", " ")


def m_sup(base, sup):
    return "<m:sSup><m:e>{0}</m:e><m:sup>{1}</m:sup></m:sSup>".format(base, sup)


def m_subsup(base, sub, sup):
    return "<m:sSubSup><m:e>{0}</m:e><m:sub>{1}</m:sub><m:sup>{2}</m:sup></m:sSubSup>".format(base, sub, sup)


def m_sum(sub, sup, cuerpo):
    return ('<m:nary><m:naryPr><m:chr m:val="∑"/></m:naryPr><m:sub>{0}</m:sub><m:sup>{1}</m:sup><m:e>{2}</m:e></m:nary>'
            .format(sub, sup, cuerpo))


def m_func(nombre, arg):
    return "<m:func><m:fName>{0}</m:fName><m:e>{1}</m:e></m:func>".format(m_r(nombre, cursiva=False), arg)


def latencias_decision():
    valores = []
    for ruta in glob.glob(os.path.join(str(PAQUETE), "01_ejecucion", "ejecuciones", "*_controlador_propio_*", "ejecucion_*", "telemetria_segmentos.csv")):
        for fila in csv.DictReader(open(ruta, encoding="utf-8")):
            if fila["es_init"] == "0" and (fila.get("ms_decision_politica") or "").strip():
                v = float(fila["ms_decision_politica"])
                if v > 0:
                    valores.append(v)
    return {"n": len(valores), "mediana": statistics.median(valores), "p99": float(np.percentile(valores, 99)), "max": max(valores)}


def figura(ej):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    gris, gris_osc, azul, rojo = "#adb5bd", "#495057", "#1971c2", "#c92a2a"
    plt.rcParams.update({"font.family": "Arial", "font.size": 9})
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.4, 3.0), gridspec_kw={"width_ratios": [1.15, 1.0]})
    pred = np.array(ej["pred_bps"]) / 1e6
    h = np.arange(1, pred.shape[0] + 1)
    etiquetas = ["cuantil 0,10", "cuantil 0,25", "mediana", "cuantil 0,75"]
    estilos = [("--", azul), ("-", azul), ("-", gris_osc), (":", gris_osc)]
    for k in range(pred.shape[1]):
        a.plot(h, pred[:, k], estilos[k][0], color=estilos[k][1], lw=1.6 if k < 2 else 1.2, marker="o", ms=3, label=etiquetas[k])
    a.axhline(ej["media_armonica_bps"] / 1e6, color=gris, lw=1.0, label="media armónica (base): {0} Mbit/s".format(coma(ej["media_armonica_bps"] / 1e6)))
    if ej.get("throughput_siguiente_bps"):
        a.plot([1], [ej["throughput_siguiente_bps"] / 1e6], marker="x", color=rojo, ms=8, mew=2, ls="none",
               label="medido después: {0} Mbit/s".format(coma(ej["throughput_siguiente_bps"] / 1e6)))
    for kbps in ej["bitrates_kbps"]:
        a.axhline(kbps / 1000, color="#e9ecef", lw=0.8, zorder=0)
    a.set_xticks(h)
    a.set_xlabel("segmento del horizonte")
    a.set_ylabel("Mbit/s")
    a.set_title("(a) Escenarios predichos, buffer {0} s".format(coma(ej["buffer_s"], 1)), loc="left", fontsize=9, fontweight="bold")
    a.legend(fontsize=6.5, loc="upper left", frameon=False, ncol=2)
    a.set_ylim(0, max(pred.max(), ej["media_armonica_bps"] / 1e6) * 1.6)
    for s in ("top", "right"):
        a.spines[s].set_visible(False)

    esc = ["0,10", "0,25", "0,50", "0,75"]
    x = np.arange(4)
    pc = ej["mejor_cvar"]["puntuaciones"]
    pm = ej["mejor_mediana"]["puntuaciones"]
    b.bar(x - 0.18, pm, width=0.34, color=gris, label="mejor por la mediana: {0} (CVaR {1})".format(" ".join(map(str, ej["mejor_mediana"]["secuencia"])), coma(ej["mejor_mediana"]["cvar"])))
    b.bar(x + 0.18, pc, width=0.34, color=azul, label="mejor por CVaR (aplicada): {0} (CVaR {1})".format(" ".join(map(str, ej["mejor_cvar"]["secuencia"])), coma(ej["mejor_cvar"]["cvar"])))
    b.axhline(0, color=gris_osc, lw=0.8)
    b.set_xticks(x)
    b.set_xticklabels(["escenario\n" + e for e in esc])
    b.set_ylabel("puntuación de la secuencia")
    b.set_title("(b) Puntuación por escenario", loc="left", fontsize=9, fontweight="bold")
    b.legend(fontsize=6.5, loc="lower right", frameon=False)
    for s in ("top", "right"):
        b.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(FIG_DEC_SVG)
    fig.savefig(FIG_DEC_PNG, dpi=220)
    plt.close(fig)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    R = json.load(open(RESUMEN, encoding="utf-8"))
    T = R["totales"]
    C = R["cambios_sobre_mismo_estado_reales"]
    E = R["ensanchado"]
    I = R["inferencia_ms"]
    ej = R["ejemplo"]
    assert T["decisiones"] == T["iguales"] and T["respaldos"] == 0
    assert R["orden_puntuaciones"]["decisiones"] == R["orden_puntuaciones"]["no_decrecientes"]
    assert ej and ej["nivel"] == ej["registrado"]
    lat = latencias_decision()
    figura(ej)
    nr = T["decisiones_reales"]
    pct = lambda n: coma(100.0 * n / nr, 1)  # noqa: E731

    b = Borrador(PLANTILLA)
    b.h2("5.6. El controlador propio")
    b.parrafo(
        "El MPC robusto del apartado 5.5 planifica con un único valor pesimista del throughput, obtenido al "
        "rebajar la media armónica por el mayor error reciente. Ese valor no dice cuánto puede variar la red ni "
        "si la predicción es fiable en la situación concreta: un mismo rebaje se aplica a una red estable y a "
        "una red que acaba de caer. El controlador propio conserva la estructura de control predictivo y el "
        "planificador del MPC robusto, con los tamaños reales de los segmentos, y cambia la predicción: en "
        "lugar de un valor, predice una distribución del throughput de los cinco segmentos siguientes, "
        "acompañada de una medida de la confianza del propio modelo, y decide promediando los escenarios "
        "desfavorables de esa distribución. La Tabla 5.9 resume qué comparten los dos controladores y en qué "
        "difieren."
    )
    b.tabla(
        ["Aspecto", "MPC robusto (5.5)", "Controlador propio"],
        [
            ("Predicción del throughput", "un valor: media armónica dividida por (1 + error máximo reciente)",
             "cuatro cuantiles por segmento futuro, aprendidos de trazas reales y ensanchados según la desconfianza del modelo"),
            ("Escenarios que se ponderan", "uno", "los ⌈α·K⌉ peores de K = 4: con α = 0,75, los tres no optimistas, promediados"),
            ("Planificador", "el mismo: 7776 secuencias de 5 niveles, QoE lineal, tamaños reales, buffer simulado hasta 60 s", "el mismo"),
            ("Respaldo", "no necesita", "el MPC robusto, con la misma realimentación"),
        ],
        "Tabla 5.9: Qué comparten y en qué difieren el MPC robusto y el controlador propio. La comparación "
        "entre ambos en el capítulo 6 aísla la predicción y la agregación de riesgo.",
        anchos_cm=[3.4, 5.6, 7.0],
    )
    b.parrafo(
        "La combinación de un predictor aprendido con un controlador clásico tiene precedentes. En Fugu, "
        "desplegado en la plataforma Puffer, un predictor neuronal probabilístico entrenado con datos del "
        "propio despliegue informa a un MPC [yan2020puffer]. En el MPC bayesiano, una red neuronal bayesiana "
        "estima la incertidumbre aleatoria y epistémica de la predicción y el planificador maximiza el peor "
        "caso dentro de la región de confianza resultante [kan2021bayesmpc]. La separación entre predicción y "
        "decisión responde además a la experiencia de este trabajo: las primeras iteraciones, con políticas "
        "aprendidas que elegían directamente la calidad, no superaron a los controladores clásicos "
        "(apartado 7.5). Al separar las dos tareas, la red aprende solo lo que puede aprenderse y medirse con "
        "datos, cómo evolucionará la red, y la decisión la toma un optimizador determinista que puede "
        "inspeccionarse paso a paso. La Figura 5.4 muestra la arquitectura: la información de red, observada "
        "en el pasado, llega al planificador a través del predictor; la información del contenido, conocida "
        "de antemano, llega directamente desde la tabla de tamaños del vídeo. Los subapartados siguientes "
        "recorren cada pieza."
    )
    b.figura(
        FIG_ARQ,
        "Figura 5.4: Arquitectura del controlador propio. La información de red llega al planificador a "
        "través del predictor de cuantiles y la del contenido, desde la tabla de tamaños del vídeo activo. Las "
        "salvaguardas validan cada decisión o la delegan en el MPC robusto.",
        ancho_cm=16.0,
    )

    b.h3("5.6.1. Entradas del predictor")
    b.parrafo(
        "El predictor recibe dos grupos de entradas, construidos en cada decisión a partir del contrato de "
        "realimentación del apartado 4.5 (Tabla 5.10). El primero es una secuencia con las cinco últimas "
        "descargas de segmentos de vídeo, incluida la de calentamiento: de cada una se toma el throughput "
        "medido, en escala logarítmica, y el tiempo de descarga. El segundo son siete escalares que describen "
        "el estado de la sesión. El rebuffering reciente se calcula como en el simulador de entrenamiento, "
        "como el exceso del tiempo de la última descarga sobre el buffer previo, y los indicadores de progreso "
        "se refieren a los 30 segmentos de la sesión. Todas las entradas se normalizan con la media y la "
        "desviación típica calculadas solo sobre la partición de entrenamiento, que viajan en el paquete del "
        "modelo."
    )
    b.tabla(
        ["Grupo", "Señal", "Qué mide"],
        [
            ("Secuencia (5 descargas)", "throughput medido", "ln(1 + bit/s) de cada una de las cinco últimas descargas"),
            ("", "tiempo de descarga", "segundos que tardó cada una"),
            ("Escalares", "buffer", "segundos de vídeo en el buffer"),
            ("", "nivel actual", "índice y tasa nominal del nivel del último segmento"),
            ("", "cambio reciente", "magnitud del último cambio de nivel"),
            ("", "rebuffering reciente", "exceso del tiempo de la última descarga sobre el buffer previo"),
            ("", "progreso", "fracción de segmentos que quedan y si queda alguno"),
        ],
        "Tabla 5.10: Entradas del predictor de cuantiles: dos secuencias de cinco valores y siete escalares, "
        "normalizados con las estadísticas de la partición de entrenamiento.",
        anchos_cm=[3.6, 3.6, 8.8],
    )
    b.parrafo(
        "Lo que el predictor no recibe es tan importante como lo que recibe. No ve el tamaño de ningún "
        "segmento ni ningún rasgo de la escena: la única información del contenido a su alcance es la tasa "
        "nominal del nivel en curso. Tampoco ve la identidad de la traza, su partición, su dificultad ni el "
        "throughput futuro. Esta exclusión no depende de la disciplina de quien programa: el constructor de "
        "entradas rechaza cualquier realimentación que contenga alguna de las 29 claves prohibidas y comprueba "
        "que cada entrada sea numérica, finita y de la longitud esperada. Si algo falla, el controlador no "
        "improvisa una entrada: delega la decisión y registra el motivo (apartado 5.6.4)."
    )

    b.h3("5.6.2. Predictor de cuantiles del throughput")
    b.parrafo(
        "Un único valor previsto oculta lo que más interesa al decidir: cuánto puede empeorar la red. Por eso "
        "el predictor estima cuantiles. El cuantil τ del throughput es el valor que la red supera con "
        "probabilidad 1 − τ; el cuantil 0,10 es el throughput que se supera nueve de cada diez veces. El "
        "predictor estima cuatro cuantiles, τ ∈ {0,10; 0,25; 0,50; 0,75}, para cada uno de los cinco segmentos "
        "siguientes, sin suponer ninguna forma para la distribución. No predice el throughput en valor "
        "absoluto, sino su logaritmo relativo a la media armónica de las descargas del historial, el mismo "
        "estimador que usa el MPC robusto. La etiqueta de entrenamiento para el horizonte h es:"
    )
    b.ecuacion(
        m_sub(m_r("y"), m_r("k,h")) + m_r("=", cursiva=False)
        + m_func("ln", m_f(m_sub(m_r("C"), m_r("k+h")), m_sub(m_r("C̄"), m_r("k"))))
        + m_r(",   ", cursiva=False) + m_r("h") + m_r("=", cursiva=False) + m_r("1, …, 5", cursiva=False),
        "5.7",
    )
    b.parrafo(
        "donde C~k+h~ es el throughput medido en la descarga h-ésima posterior a la decisión k y C̄~k~ la media "
        "armónica del historial en ese momento. Al trabajar en escala relativa, un mismo modelo sirve para "
        "redes de cientos de kbit/s y de decenas de Mbit/s. En ejecución, cada cuantil predicho se reconvierte "
        "a bit/s multiplicando la base por su exponencial, acotado entre 0,15 y 4 veces la base para que una "
        "predicción anómala no arrastre al planificador."
    )
    b.parrafo(
        "La secuencia de descargas la procesa una red recurrente con unidades GRU (//Gated Recurrent Unit//) "
        "de 96 dimensiones [cho2014gru]. Una GRU recorre la secuencia paso a paso y mantiene un vector de "
        "estado que resume lo observado; unas puertas aprendidas deciden en cada paso qué parte del estado "
        "conservar y cuánto actualizarlo con la nueva muestra, como un filtro recursivo no lineal cuyos "
        "coeficientes se aprenden de los datos. El estado final se concatena con los siete escalares y una red "
        "densa de dos capas (96 y 64 neuronas, con desactivación aleatoria del 10 % durante el entrenamiento) "
        "produce veinte valores: cuatro cuantiles por cinco horizontes. Para cada horizonte la red emite el "
        "cuantil más bajo y, para los demás, incrementos forzados a ser positivos:"
    )
    b.ecuacion(
        m_sup(m_r("ŷ"), m_d(m_sub(m_r("τ"), m_r("1")))) + m_r("=", cursiva=False) + m_sub(m_r("z"), m_r("1"))
        + m_r(",   ", cursiva=False)
        + m_sup(m_r("ŷ"), m_d(m_sub(m_r("τ"), m_r("j")))) + m_r("=", cursiva=False)
        + m_sup(m_r("ŷ"), m_d(m_sub(m_r("τ"), m_r("j−1")))) + m_r("+", cursiva=False)
        + m_func("ln", m_d(m_r("1", cursiva=False) + m_r("+", cursiva=False) + m_sup(m_r("e"), m_sub(m_r("z"), m_r("j")))))
        + m_r(",   ", cursiva=False) + m_r("j") + m_r("=", cursiva=False) + m_r("2, 3, 4", cursiva=False),
        "5.8",
    )
    b.parrafo(
        "donde z~j~ son las salidas de la red y ln(1 + e^z), la función //softplus//, siempre es positiva. Así "
        "los cuantiles nunca se cruzan. El criterio de entrenamiento es la pérdida de cuantiles o pérdida "
        "//pinball// de la regresión cuantílica [koenker1978quantiles]:"
    )
    b.ecuacion(
        m_sub(m_r("ρ"), m_r("τ")) + m_d(m_r("u")) + m_r("=", cursiva=False)
        + m_func("max", m_d(m_r("τ") + m_r("u") + m_r(", ", cursiva=False) + m_d(m_r("τ") + m_r("−", cursiva=False) + m_r("1", cursiva=False)) + m_r("u")))
        + m_r(",   ", cursiva=False) + m_r("u") + m_r("=", cursiva=False) + m_r("y") + m_r("−", cursiva=False)
        + m_sup(m_r("ŷ"), m_d(m_r("τ"))),
        "5.9",
    )
    b.parrafo(
        "La asimetría de esta pérdida hace que su mínimo se alcance en el cuantil τ. Para τ = 0,10, una "
        "predicción por encima del valor real cuesta 0,9 por unidad de error y una por debajo, 0,1: "
        "sobrestimar es nueve veces más caro, y el cuantil aprendido se sitúa donde solo una de cada diez "
        "observaciones queda por debajo. El entrenamiento completo se describe en el apartado 5.7."
    )
    b.parrafo(
        "La incertidumbre tiene dos orígenes que el diseño trata por separado, siguiendo la distinción de la "
        "literatura [kan2021bayesmpc]. La variabilidad de la red, o incertidumbre aleatoria, la capturan los "
        "cuantiles. La desconfianza del modelo en sí mismo, o incertidumbre epistémica, crece en situaciones "
        "poco representadas en el entrenamiento y un único modelo no la percibe. Para estimarla se entrenan "
        "cinco redes idénticas con inicializaciones distintas, la técnica de los conjuntos profundos "
        "[lakshminarayanan2017ensembles]: donde los datos abundan las cinco coinciden; donde escasean, "
        "discrepan. La combinación es deliberadamente asimétrica. Para cada horizonte y cuantil se promedian "
        "las cinco predicciones y después los cuantiles inferiores se desplazan hacia abajo en proporción al "
        "desacuerdo:"
    )
    b.ecuacion(
        m_sup(m_r("ỹ"), m_d(m_r("τ"))) + m_r("=", cursiva=False) + m_sup(m_r("ȳ"), m_d(m_r("τ")))
        + m_r("−", cursiva=False) + m_r("c") + m_r("·", cursiva=False)
        + m_f(m_r("0,5", cursiva=False) + m_r("−", cursiva=False) + m_r("τ"), m_r("0,5", cursiva=False))
        + m_r("·", cursiva=False) + m_r("σ") + m_r("   para ", cursiva=False) + m_r("τ") + m_r("<", cursiva=False) + m_r("0,5", cursiva=False),
        "5.10",
    )
    b.parrafo(
        "donde ȳ es la media de los cinco miembros, σ la desviación típica de sus cinco medianas y c = 1 el "
        "factor de ensanchado. El cuantil 0,10 baja 0,8σ y el 0,25, 0,5σ, en escala logarítmica; los "
        "superiores no se tocan. La razón es que solo la cola inferior provoca paradas: cuando el modelo no "
        "sabe, los escenarios pesimistas se vuelven más pesimistas y los optimistas no se inflan. En las "
        "{0} decisiones reales del experimento final el desacuerdo fue pequeño en la mayoría de los casos: en "
        "la decisión mediana el ensanchado rebajó el cuantil 0,10 del primer horizonte un {1} %, en el 10 % de "
        "decisiones con más desacuerdo lo rebajó más de un {2} % y en el caso extremo un {3} %. El modelo es "
        "pequeño a propósito: {4} parámetros por miembro, {5} en el conjunto y menos de un megabyte de pesos. "
        "La inferencia de los cinco miembros, en un solo hilo de CPU, duró {6} ms de mediana en el experimento "
        "final, con un máximo de {7} ms frente al límite de 50 ms que vigilan las salvaguardas.".format(
            miles(nr), coma(E["descenso_q10_mediana_pct"], 1), coma(E["descenso_q10_p90_pct"], 1),
            coma(E["descenso_q10_max_pct"], 0), miles(R["parametros_por_miembro"]), miles(R["parametros_total"]),
            coma(I["mediana"], 1), coma(I["max"], 1),
        )
    )

    b.h3("5.6.3. Planificador con agregación de riesgo")
    b.parrafo(
        "El planificador recibe del predictor una matriz de cinco horizontes por cuatro cuantiles, ya en bit/s. "
        "Cada columna se interpreta como un escenario de red para los cinco segmentos siguientes: pesimista "
        "(τ = 0,10), desfavorable (0,25), central (0,50) y optimista (0,75); cada escenario mantiene el mismo "
        "cuantil en los cinco segmentos, es decir, supone que un periodo malo de la red se prolonga durante el "
        "horizonte. Para cada secuencia de acciones y cada escenario simula el buffer con la misma dinámica del "
        "cliente y con el tamaño real de cada segmento, y puntúa la secuencia con la QoE lineal acumulada de la "
        "ecuación (5.5). Con seis niveles y cinco segmentos hay 6⁵ = 7776 secuencias, evaluadas a la vez con "
        "operaciones vectoriales, cada una en los cuatro escenarios."
    )
    b.parrafo(
        "Un MPC ordinario elegiría la secuencia con mejor puntuación en el escenario central y el MPC robusto, "
        "la mejor en un único escenario pesimista. El planificador propio usa un criterio intermedio con "
        "fundamento formal, el valor en riesgo condicional (CVaR, //Conditional Value at Risk//) "
        "[rockafellar2000cvar], que promedia las puntuaciones de la fracción peor de los escenarios. Con K "
        "escenarios del mismo peso y con la convención en la que α es la fracción de escenarios peores que se "
        "promedia:"
    )
    b.ecuacion(
        m_sub(m_r("CVaR", cursiva=False), m_r("α")) + m_d(m_r("a")) + m_r("=", cursiva=False)
        + m_f(m_r("1", cursiva=False), m_r("m"))
        + m_sum(m_r("j") + m_r("=", cursiva=False) + m_r("1", cursiva=False), m_r("m"), m_sub(m_r("J"), m_d(m_r("j"))) + m_d(m_r("a")))
        + m_r(",   ", cursiva=False) + m_r("m") + m_r("=", cursiva=False)
        + m_d(m_r("α") + m_r("K"), abre="⌈", cierra="⌉"),
        "5.11",
    )
    b.parrafo(
        "donde J~(1)~ ≤ … ≤ J~(K)~ son las puntuaciones de la secuencia a ordenadas de peor a mejor. Con α = 1 "
        "el criterio es la media de todos los escenarios y, al reducir α, se acerca al peor caso. El "
        "controlador usa α = 0,75, de modo que con K = 4 promedia m = 3 escenarios. Como m es un entero, α "
        "solo cambia la decisión en saltos de 0,25: 0,70 y 0,75 deciden igual. Los cuantiles no reparten la "
        "probabilidad por igual, y los tres puntos promediados se concentran en la parte baja del intervalo "
        "que representan; el criterio debe leerse como una aproximación discreta y prudente del CVaR de la "
        "distribución predicha, no como el CVaR exacto. El planificador elige la secuencia de mayor CVaR, "
        "aplica su primera acción y vuelve a planificar en el segmento siguiente, igual que el MPC "
        "[yin2015mpc]."
    )
    b.parrafo(
        "La expresión (5.11) admite una lectura más sencilla. En la puntuación (5.5), la calidad y los cambios "
        "de nivel de una secuencia no dependen del escenario: solo el rebuffering depende de la red. Como los "
        "cuantiles están ordenados y una red más rápida nunca produce más rebuffering, las puntuaciones quedan "
        "ordenadas igual que los escenarios y los tres peores son siempre los de τ = 0,10, 0,25 y 0,50, "
        "propiedad comprobada en las {0} decisiones reales del experimento final. Por tanto:".format(miles(nr))
    )
    b.ecuacion(
        m_sub(m_r("CVaR", cursiva=False), m_r("0,75")) + m_d(m_r("a")) + m_r("=", cursiva=False)
        + m_sum(m_r("j"), "", m_f(m_sub(m_r("R"), m_sub(m_r("a"), m_r("j"))), m_r("10⁶", cursiva=False)))
        + m_r("−", cursiva=False)
        + m_sum(m_r("j"), "", m_f(m_d(m_sub(m_r("R"), m_sub(m_r("a"), m_r("j"))) + m_r("−", cursiva=False) + m_sub(m_r("R"), m_sub(m_r("a"), m_r("j−1"))), abre="|", cierra="|"), m_r("10⁶", cursiva=False)))
        + m_r("−", cursiva=False) + m_r("4,3", cursiva=False) + m_r("·", cursiva=False)
        + m_f(m_r("1", cursiva=False), m_r("3", cursiva=False))
        + m_sum(m_r("τ") + m_r("∈", cursiva=False) + m_r("{0,10; 0,25; 0,50}", cursiva=False), "",
                m_sum(m_r("j"), "", m_subsup(m_r("ρ"), m_r("j"), m_d(m_r("τ"))))),
        "5.12",
    )
    b.parrafo(
        "El planificador es, así, un MPC cuya penalización por rebuffering es la media del rebuffering simulado "
        "en los tres escenarios no optimistas, con el tamaño real de cada segmento. El escenario optimista no "
        "interviene: ninguna secuencia se premia por lo bien que saldría si la red fuera generosa. Es el mismo "
        "principio por el que un radioenlace se dimensiona con un margen de desvanecimiento: no para el canal "
        "medio, sino para que el servicio se mantenga en la fracción desfavorable de las condiciones. Con esta "
        "lectura se cierra el diseño del predictor: como el desacuerdo del conjunto solo ensancha la cola "
        "inferior, las situaciones que el modelo conoce peor se traducen en decisiones más prudentes."
    )
    b.parrafo(
        "El valor de α se fijó durante el desarrollo, con una versión anterior del predictor, mediante un "
        "barrido sobre ventanas de la partición de validación: 0,75 ofreció el mejor peor caso con el menor "
        "coste en calidad media. Se descartaron dos alternativas. La primera versión del planificador hacía "
        "depender α de la ocupación del buffer, con más prudencia cuanto menos buffer; el valor fijo igualó o "
        "mejoró a esa regla, que el código conserva sin activar. También se probó un criterio basado en una "
        "cota inferior de confianza, que empeoró el peor caso. El apartado 5.6.6 muestra con las decisiones del "
        "propio experimento por qué el valor exacto de α importa poco. El coste de planificar es pequeño: la "
        "decisión completa del controlador propio, inferencia y planificación, duró {0} ms de mediana en el "
        "experimento final, con un percentil 99 de {1} ms y un máximo de {2} ms.".format(
            coma(lat["mediana"], 1), coma(lat["p99"], 1), coma(lat["max"], 1)
        )
    )

    b.h3("5.6.4. Salvaguardas y paquete del modelo")
    b.parrafo(
        "El apartado 4.5 fijó el principio: un controlador con modelo nunca puede invalidar una sesión. La "
        "implementación lo cumple con rutas de respaldo en tres puntos. Al crear el controlador, antes de que "
        "arranque la sesión, se carga el paquete del modelo; si no supera la verificación (un fichero ausente, "
        "un esquema desconocido, un tamaño o un resumen SHA-256 que no coincide con el manifiesto), la carga se "
        "reintenta en cada decisión y mientras tanto decide el respaldo. Antes de predecir, si la "
        "realimentación no permite construir las entradas (una clave obligatoria ausente o no numérica, una "
        "máscara sin acciones válidas, un campo prohibido) o si la escalera del vídeo no coincide con la del "
        "manifiesto, el controlador delega. Después de planificar, comprueba que la inferencia no superó los "
        "50 ms, que la acción pertenece a la máscara y que la tasa es finita y positiva; cualquier excepción "
        "imprevista se trata como fallo de inferencia. El respaldo es el MPC robusto del apartado 5.5, creado "
        "junto al controlador para el mismo vídeo y alimentado con toda la realimentación de la sesión; su "
        "decisión se comprueba también contra la máscara y, si fallase, se devuelve la menor tasa válida. El "
        "reproductor recibe siempre una tasa."
    )
    b.parrafo(
        "Cada decisión deja en la telemetría 25 campos de diagnóstico: si el paquete se cargó y se verificó, si "
        "las entradas eran válidas, la acción bruta del planificador y la acción final, la latencia de "
        "inferencia y, en su caso, el uso del respaldo y su motivo, tomado de un vocabulario cerrado de 20 "
        "valores. Con ellos la evaluación audita el controlador decisión a decisión: en el experimento final, "
        "las {0} decisiones del controlador propio quedaron auditadas y ninguna recurrió al respaldo. El "
        "paquete del modelo reúne en cinco ficheros todo lo que el controlador necesita del entrenamiento: los "
        "pesos de los cinco miembros, la configuración del modelo, la normalización, la configuración del "
        "planificador (α, pesos del objetivo, horizonte y factor de ensanchado) y un manifiesto con el tamaño y "
        "el resumen SHA-256 de cada uno de los otros cuatro (apartado 5.1). Cualquier alteración posterior lo "
        "haría inservible en lugar de silenciosamente distinto.".format(miles(T["decisiones"]))
    )

    b.h3("5.6.5. Variantes de ablación como diseño del experimento")
    b.parrafo(
        "Para medir qué aporta cada pieza, el experimento del capítulo 6 incluye tres variantes del controlador "
        "propio que comparten el planificador, los tamaños reales, α y el respaldo, y cambian solo la "
        "predicción (Tabla 5.11). La variante de la mediana usa únicamente el cuantil central de la red, de modo "
        "que el planificador decide con un solo escenario y no hay agregación de riesgo: aísla el aporte del "
        "CVaR. Las otras dos sustituyen la red por estimadores sin aprendizaje. Los cuantiles fijos son los "
        "cuantiles empíricos del logaritmo del cociente entre el throughput futuro y la media armónica, "
        "calculados una vez sobre las {0} muestras con historial del dataset de entrenamiento, por horizonte y "
        "cuantil; en cada decisión se aplican a la media armónica actual. Los cuantiles recientes son los "
        "cuantiles empíricos de las cinco últimas descargas, iguales en los cinco horizontes. Estas dos aíslan "
        "el aporte de la red frente a una distribución fija y frente a una distribución local sin modelo.".format(
            miles(474150)
        )
    )
    b.tabla(
        ["Variante", "Predicción que recibe el planificador", "Qué aísla", "Hipótesis del capítulo 6"],
        [
            ("Controlador propio", "cuatro cuantiles de la red, ensanchados", "referencia", "P1 y P2 frente al MPC robusto"),
            ("Solo la mediana", "el cuantil 0,50 de la red, un escenario", "la agregación de riesgo (CVaR)", "P5"),
            ("Cuantiles fijos", "cuantiles del error de la media armónica en el entrenamiento, aplicados a la media armónica actual", "la red frente a una distribución fija", "P4"),
            ("Cuantiles recientes", "cuantiles empíricos de las cinco últimas descargas", "la red frente a una distribución local sin modelo", "P3"),
        ],
        "Tabla 5.11: El controlador propio y sus tres variantes de ablación. Las cuatro comparten el "
        "planificador, los tamaños reales, α = 0,75 y el respaldo; cambia solo la predicción.",
        anchos_cm=[3.0, 5.6, 4.0, 3.4],
    )
    b.parrafo(
        "Las variantes son el mismo controlador con un modo de predicción distinto, registradas con sus "
        "propias claves, y las dos sin red no ejecutan inferencia, lo que la auditoría tiene en cuenta. Las "
        "pruebas automáticas comprueban que la mediana es la columna central de la red, que los cuantiles "
        "recientes son los de las últimas descargas, que los cuantiles fijos escalan la media armónica y que "
        "las variantes sin red no cuentan inferencia."
    )

    b.h3("5.6.6. Una decisión real y el peso de cada pieza")
    mc, mm = ej["mejor_cvar"], ej["mejor_mediana"]
    pred = np.array(ej["pred_bps"]) / 1e6
    b.parrafo(
        "Las decisiones del controlador propio en el experimento final pueden reproducirse fuera de línea: "
        "basta con reinyectar, en orden, la realimentación registrada en la telemetría de cada sesión en un "
        "controlador nuevo con el mismo paquete del modelo y la misma tabla de tamaños. Las {0} decisiones de "
        "las {1} sesiones del controlador propio, reproducidas en otra máquina y con otra versión de PyTorch, "
        "devuelven exactamente las acciones registradas. Esa reproducibilidad permite examinar cualquier "
        "decisión y medir qué aporta cada pieza. La Figura 5.5 reconstruye la decisión del segmento {2} de la "
        "sesión del controlador propio en la misma ventana de Oboe y con el mismo vídeo que la Figura 5.3, "
        "elegida con esa regla para comparar los dos controladores en estados comparables aunque no idénticos. "
        "El buffer está en {3} s y el nivel anterior es {4}; las cinco últimas descargas midieron {5} Mbit/s y su "
        "media armónica, la base, es {6} Mbit/s.".format(
            miles(T["decisiones"]), T["sesiones"], ej["segmento"], coma(ej["buffer_s"], 1), ej["nivel_previo"],
            ", ".join(coma(v / 1e6) for v in ej["historial_bps"]), coma(ej["media_armonica_bps"] / 1e6),
        )
    )
    b.figura(
        FIG_DEC_PNG,
        "Figura 5.5: Decisión real del controlador propio en el segmento {0} de la sesión {1}. (a) Cuantiles "
        "predichos del throughput para los cinco segmentos siguientes, media armónica de base, niveles de la "
        "escalera y throughput medido en la descarga siguiente. (b) Puntuación en cada escenario de la mejor "
        "secuencia según la mediana y de la mejor según el CVaR, que es la aplicada.".format(ej["segmento"], int(ej["sesion"][1:6])),
        ancho_cm=16.0,
    )
    kb = ej["bitrates_kbps"]
    b.parrafo(
        "Para el segmento siguiente el predictor da un cuantil 0,10 de {0} Mbit/s, un 0,25 de {1}, una mediana "
        "de {2} y un 0,75 de {3} Mbit/s. La mejor secuencia según la mediana es {4}, con puntuación {5} en el "
        "escenario central pero {6} y {7} en los escenarios 0,25 y 0,10; su CVaR es {8}. La mejor secuencia "
        "según el CVaR es {9}, con puntuaciones {10} en los cuatro escenarios y CVaR {11}. El controlador aplica "
        "el nivel {12}, de {13} kbit/s. La descarga siguiente midió {14} Mbit/s.".format(
            coma(pred[0, 0]), coma(pred[0, 1]), coma(pred[0, 2]), coma(pred[0, 3]),
            " ".join(map(str, mm["secuencia"])), coma(mm["puntuaciones"][2]), coma(mm["puntuaciones"][1]), coma(mm["puntuaciones"][0]), coma(mm["cvar"]),
            " ".join(map(str, mc["secuencia"])), ", ".join(coma(v) for v in mc["puntuaciones"]), coma(mc["cvar"]),
            ej["nivel"], int(kb[ej["nivel"]]),
            coma(ej["throughput_siguiente_bps"] / 1e6) if ej.get("throughput_siguiente_bps") else "—",
        )
    )
    b.parrafo(
        "La misma reproducción permite medir qué parte del controlador determina las decisiones. Para cada "
        "una de las {0} decisiones de las sesiones con trazas reales se recalculó, sobre exactamente el mismo "
        "estado, la acción que habría elegido el planificador con una pieza cambiada (Tabla 5.12). La pieza que "
        "más pesa es el criterio de riesgo: planificar solo con la mediana habría cambiado el {1} % de las "
        "decisiones, casi siempre hacia un nivel más alto. El valor exacto de α importa poco: sustituir el CVaR "
        "por el peor escenario cambia el {2} % y por la media de los cuatro, el {3} %; en la ecuación (5.12) se "
        "ve por qué, el rebuffering de una secuencia arriesgada aparece de golpe en los escenarios pesimistas y "
        "cualquier criterio que los tenga en cuenta la descarta. El tamaño real de los segmentos cambia el "
        "{4} % de las decisiones, en los dos sentidos, y el ensanchado epistémico el {5} %, sobre todo hacia la "
        "prudencia. Estos porcentajes miden el cambio en la decisión inmediata; su efecto sobre la calidad de "
        "experiencia en sesiones completas es lo que miden las variantes del capítulo 6.".format(
            miles(nr), pct(C["mediana"]["n"]), pct(C["peor"]["n"]), pct(C["media4"]["n"]), pct(C["nominal"]["n"]), pct(C["sin_ensanchado"]["n"])
        )
    )
    b.tabla(
        ["Variante sobre el mismo estado", "Decisiones con otra acción (de {0})".format(miles(nr)), "Sentido del cambio"],
        [
            ("Solo el escenario central (mediana)", "{0} ({1} %)".format(C["mediana"]["n"], pct(C["mediana"]["n"])),
             "el CVaR elige más bajo en {0}".format(C["mediana"]["mas_bajo"])),
            ("Solo el escenario pesimista (cuantil 0,10)", "{0} ({1} %)".format(C["peor"]["n"], pct(C["peor"]["n"])),
             "el peor caso elige más bajo en {0}".format(C["peor"]["mas_alto"])),
            ("Media de los cuatro escenarios (α = 1)", "{0} ({1} %)".format(C["media4"]["n"], pct(C["media4"]["n"])),
             "el CVaR elige más bajo en {0}".format(C["media4"]["mas_bajo"])),
            ("Tamaños nominales en lugar de reales", "{0} ({1} %)".format(C["nominal"]["n"], pct(C["nominal"]["n"])),
             "más bajo con tamaños reales en {0}, más alto en {1}".format(C["nominal"]["mas_bajo"], C["nominal"]["mas_alto"])),
            ("Sin ensanchado epistémico", "{0} ({1} %)".format(C["sin_ensanchado"]["n"], pct(C["sin_ensanchado"]["n"])),
             "con ensanchado se elige más bajo en {0}".format(C["sin_ensanchado"]["mas_bajo"])),
        ],
        "Tabla 5.12: Decisiones de las sesiones reales del experimento final en las que la variante indicada, "
        "sobre el mismo estado, habría elegido otra acción que el controlador propio.",
        anchos_cm=[5.6, 4.4, 6.0],
    )
    b.parrafo(
        "Los límites del controlador son los de su diseño. El predictor aprende con segmentos de 4 s, la "
        "escalera de 300 a 4300 kbit/s y los vídeos del entrenamiento; un contenido con otra escalera u otra "
        "duración de segmento queda fuera del régimen para el que se diseñó, y el comportamiento con el "
        "contenido nuevo del experimento es una propiedad medida en el capítulo 6, no supuesta. El CVaR sobre "
        "cuatro cuantiles es una aproximación discreta y α solo actúa en saltos de 0,25. Y el controlador es "
        "tan bueno como su planificador y su tabla de tamaños: un descriptor equivocado haría planificar con "
        "bytes que no son los del vídeo, por lo que la escalera se coteja con el manifiesto antes de decidir. El "
        "apartado 5.7 describe el entorno con el que se entrena y empaqueta el modelo."
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("latencia decision:", lat)


if __name__ == "__main__":
    main()
