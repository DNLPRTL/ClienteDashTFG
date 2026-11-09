# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap3_planificacion_costes.docx (capitulo 3 entero) y la Figura 3.1 (Gantt).

TODOS los datos salen de docs/memoria/apoyo/planificacion_cap3.json (fases, fechas, horas, hitos, supuestos,
hardware, software): es el fichero que edita Daniel. Este script solo lee, calcula (duraciones, totales,
amortizacion) y escribe. Las anclas del historial git se comprueban contra el repositorio.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap3.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker  # noqa: E402

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla, m_d, m_f, m_r  # noqa: E402

DATOS = Path(__file__).resolve().parent / "planificacion_cap3.json"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIG_SVG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_3_1_gantt.svg"
FIG_PNG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_3_1_gantt.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap3_planificacion_costes.docx"
AZUL, GRIS, GRIS_CLARO, AMARILLO, ROJO, NEGRO = "#1971c2", "#495057", "#adb5bd", "#fff9db", "#c92a2a", "#212529"
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
TIPOS = {"estudio": "estudio", "desarrollo": "desarrollo", "validacion": "validación", "redaccion": "redacción"}


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def eur(x):
    s = "{0:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", " ")
    return s + " €"


def fecha(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def fecha_texto(d):
    return "{0} de {1} de {2}".format(d.day, MESES[d.month - 1], d.year)


def mes_texto(d):
    return "{0} de {1}".format(MESES[d.month - 1], d.year)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    cfg = json.load(open(DATOS, encoding="utf-8"))
    fases = cfg["fases"]
    sup = cfg["supuestos"]
    for f in fases:
        f["ini"], f["finf"] = fecha(f["inicio"]), fecha(f["fin"])
        assert f["ini"] < f["finf"], f["id"]
    inicio = min(f["ini"] for f in fases)
    fin = max(f["finf"] for f in fases)
    assert inicio == fecha(cfg["proyecto"]["inicio"]) and fin == fecha(cfg["proyecto"]["fin"])
    horas_total = sum(f["horas"] for f in fases)
    horas_tipo = {}
    for f in fases:
        horas_tipo[f["tipo"]] = horas_tipo.get(f["tipo"], 0) + f["horas"]
    # Anclas del historial git.
    primer = subprocess.check_output(["git", "log", "--reverse", "--date=short", "--format=%ad"], cwd=RAIZ_REPO, text=True).splitlines()[0]
    assert primer == "2026-05-06" and any(h["fecha"] == primer for h in cfg["hitos"])
    n_commits = int(subprocess.check_output(["git", "rev-list", "--count", "HEAD"], cwd=RAIZ_REPO, text=True).strip())
    meses_proyecto = sup["meses_proyecto"]
    assert abs(((fin.year - inicio.year) * 12 + fin.month - inicio.month + 1) - meses_proyecto) <= 1

    # ---- Costes -------------------------------------------------------------------------------
    coste_alumno = horas_total * sup["tarifa_alumno_eur_h"]
    coste_tutor = sup["horas_tutor"] * sup["tarifa_tutor_eur_h"]
    vida_meses = sup["vida_util_hardware_anios"] * 12
    hw = []
    for h in cfg["hardware"]:
        amort = h["precio_eur"] * h["uso_meses"] / vida_meses
        hw.append((h["concepto"], h["precio_eur"], h["uso_meses"], amort))
    coste_hw = sum(x[3] for x in hw)
    coste_sw = sum(s["coste_eur"] for s in cfg["software"])
    total = coste_alumno + coste_tutor + coste_hw + coste_sw

    # ---- Figura 3.1: Gantt -----------------------------------------------------------------
    plt.rcParams.update({"font.family": "Arial", "font.size": 8, "axes.edgecolor": GRIS, "axes.labelcolor": GRIS,
                         "xtick.color": GRIS, "ytick.color": GRIS, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(6.3, 2.9), dpi=220)
    colores = {"estudio": GRIS_CLARO, "desarrollo": GRIS, "validacion": AZUL, "redaccion": AMARILLO}
    for i, f in enumerate(fases):
        y = len(fases) - 1 - i
        ax.barh(y, (f["finf"] - f["ini"]).days, left=mdates.date2num(f["ini"]), height=0.55, color=colores[f["tipo"]],
                edgecolor=GRIS if f["tipo"] == "redaccion" else "none", linewidth=0.6)
        ax.text(mdates.date2num(f["finf"]) + 2, y, "{0} h".format(f["horas"]), va="center", fontsize=7, color=GRIS)
    ax.set_yticks(range(len(fases)))
    ax.set_yticklabels(["{0}. {1}".format(f["id"], f["nombre"]) for f in reversed(fases)], fontsize=7)
    for h in cfg["hitos"]:
        x = mdates.date2num(fecha(h["fecha"]))
        ax.axvline(x, color=ROJO if "final" in h["texto"] else GRIS_CLARO, lw=0.8, ls=":" if "final" not in h["texto"] else "-", zorder=0)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ABREV = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: ABREV[mdates.num2date(x).month - 1]))
    ax.set_xlim(mdates.date2num(date(inicio.year, inicio.month, 1)), mdates.date2num(date(fin.year, fin.month, 28)) + 12)
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
    ax.set_xlabel("2026")
    leyenda = [plt.Rectangle((0, 0), 1, 1, color=colores[t]) for t in ("estudio", "desarrollo", "validacion", "redaccion")]
    ax.legend(leyenda, [TIPOS[t] for t in ("estudio", "desarrollo", "validacion", "redaccion")], loc="lower left", frameon=False, fontsize=6.5, ncol=4,
              bbox_to_anchor=(0.0, -0.32))
    fig.tight_layout()
    fig.savefig(FIG_SVG)
    fig.savefig(FIG_PNG)
    plt.close(fig)

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.capitulo(3, "Planificación y costes")
    b.parrafo(
        "Con el contexto del capítulo 2 fijado, este capítulo describe cómo se organizó el trabajo y qué "
        "costó. El apartado 3.1 presenta la metodología y las fases en que se dividió el proyecto; el 3.2 "
        "recoge el cronograma, con sus hitos y las desviaciones respecto a lo previsto; el 3.3 estima las horas "
        "dedicadas a cada fase, y el 3.4 traduce las horas y los recursos empleados a un coste, con las hipótesis "
        "de cálculo declaradas. Todo lo que sigue describe un trabajo ya realizado, entre {0} y {1}.".format(
            mes_texto(inicio), mes_texto(fin))
    )

    b.h2("3.1. Metodología y fases")
    b.parrafo(
        "El trabajo se organizó en {0} fases, con un método común: cada pieza se diseñaba, se implementaba con "
        "sus pruebas, se validaba en el entorno real y se documentaba antes de pasar a la siguiente, y las "
        "decisiones de diseño se registraban por escrito con la alternativa descartada y el motivo. El código se "
        "versionó con Git desde el primer día ({1} confirmaciones hasta el cierre de la redacción), de modo que "
        "el cronograma del apartado 3.2 se apoya en fechas registradas y no en el recuerdo. El desarrollo se "
        "hizo en el equipo con Windows, el entrenamiento del modelo en el subsistema Linux con GPU y la "
        "validación y el experimento final en las máquinas virtuales Linux (apartado 6.1), con una regla fija: "
        "si el comportamiento difería entre entornos, mandaba el de la máquina virtual cliente, que es la que "
        "produce la evidencia. Las fases fueron las siguientes.".format(len(fases), n_commits)
    )
    b.lista([(f["nombre"], f["descripcion"] + " ({0} a {1}).".format(fecha_texto(f["ini"]), fecha_texto(f["finf"]))) for f in fases])
    b.parrafo(
        "Las fases no fueron estrictamente secuenciales: la infraestructura experimental y los controladores "
        "clásicos se construyeron en paralelo sobre el cliente ya terminado, el controlador propio empezó antes "
        "de cerrar la infraestructura, y la redacción de la memoria arrancó con la primera evaluación completa y "
        "se solapó con la evaluación final. La Tabla 3.1 desglosa cada fase en sus tareas y su entregable."
    )
    b.tabla(
        ["Fase", "Tareas", "Entregable"],
        [("{0}. {1}".format(f["id"], f["nombre"]), "; ".join(f["tareas"]), f["entregable"]) for f in fases],
        "Tabla 3.1: Fases del proyecto con sus tareas y el entregable que cerró cada una.",
        anchos_cm=[4.0, 7.4, 4.6],
    )

    b.h2("3.2. Cronograma e hitos")
    b.parrafo(
        "La Figura 3.1 muestra el cronograma real del proyecto, con las fases en barras, las horas dedicadas al "
        "final de cada barra y los hitos en líneas verticales. Las fechas de inicio y fin de cada fase se han "
        "redondeado a la semana a partir del historial de versiones y de los documentos de decisión del "
        "proyecto; la primera fase, de estudio, es anterior al primer registro del código ({0}) y se fecha por "
        "las notas de lectura.".format(fecha_texto(fecha(primer)))
    )
    b.figura(
        FIG_PNG,
        "Figura 3.1: Diagrama de Gantt del proyecto. Barras por fase, coloreadas por tipo de trabajo, con las "
        "horas de cada una; las líneas verticales marcan los hitos, en rojo el experimento final.",
        ancho_cm=16.0,
    )
    hitos_txt = "; ".join("{0} ({1})".format(h["texto"], fecha_texto(fecha(h["fecha"]))) for h in cfg["hitos"])
    b.parrafo("Los hitos marcados son: {0}.".format(hitos_txt))
    b.parrafo(
        "Hubo dos desviaciones respecto a la planificación inicial, y conviene decirlas porque explican la "
        "forma del cronograma. La primera está dentro de la fase del controlador propio: se probaron y se "
        "descartaron tres líneas antes de llegar al diseño final, una política aprendida por clonación de "
        "comportamiento, una función de puntuación con horizonte y un predictor sin memoria temporal, y cada "
        "descarte se documentó como resultado negativo (apartado 7.5). Esa fase duró casi el doble de lo "
        "previsto y desplazó la evaluación al final del verano. La segunda es la fase de blindaje de octubre: "
        "la primera evaluación completa, de agosto, destapó deficiencias en los comparadores y en el diseño "
        "estadístico, así que se detuvo el experimento que estaba en marcha, se revisó el código entregado, se "
        "fijó un protocolo con hipótesis prerregistradas y se ejecutó una única vez el experimento final que "
        "presenta el capítulo 6. Las evaluaciones anteriores quedaron como desarrollo y no forman parte de los "
        "resultados."
    )

    b.h2("3.3. Estimación de horas")
    b.parrafo(
        "La Tabla 3.2 recoge las horas dedicadas por el alumno a cada fase, estimadas a partir del historial de "
        "versiones y de los registros de trabajo, redondeadas a la decena. El total es de {0} h, que corresponde "
        "a los 12 créditos del Trabajo Fin de Grado a razón de 25 h por crédito. Por tipo de trabajo, el "
        "desarrollo concentra {1} h, la validación y la evaluación {2} h, la redacción {3} h y el estudio previo "
        "{4} h. No se contabilizan como horas del alumno las {5} h de ejecución desatendida del experimento "
        "final en la máquina virtual ni las horas de entrenamiento del modelo en la GPU.".format(
            horas_total, horas_tipo.get("desarrollo", 0), horas_tipo.get("validacion", 0), horas_tipo.get("redaccion", 0),
            horas_tipo.get("estudio", 0), "41,3")
    )
    filas = [("{0}. {1}".format(f["id"], f["nombre"]), TIPOS[f["tipo"]], str(f["horas"])) for f in fases] + [("Total", "", str(horas_total))]
    b.tabla(["Fase", "Tipo de trabajo", "Horas"], filas,
            "Tabla 3.2: Horas dedicadas por fase y tipo de trabajo.", anchos_cm=[8.0, 4.0, 4.0], alineaciones=["l", "l", "c"])

    b.h2("3.4. Estimación de costes")
    b.parrafo(
        "El coste del proyecto se estima como si se hubiera realizado en un entorno profesional, con tres "
        "partidas: recursos humanos, hardware y software. Las hipótesis son las habituales en los trabajos de "
        "la escuela: una tarifa de {0} €/h para el alumno, como ingeniero junior, y de {1} €/h para el tutor, con "
        "{2} h de dirección y revisión; y una vida útil de {3} años para el hardware, del que se imputa solo la "
        "parte proporcional a los {4} meses del proyecto:".format(
            sup["tarifa_alumno_eur_h"], sup["tarifa_tutor_eur_h"], sup["horas_tutor"], sup["vida_util_hardware_anios"], meses_proyecto)
    )
    b.ecuacion(
        m_r("C") + m_r("=", cursiva=False) + m_r("P") + m_r("·", cursiva=False) + m_f(m_r("m"), m_r("12", cursiva=False) + m_r("·", cursiva=False) + m_r("v")),
        "3.1",
    )
    b.parrafo(
        "donde C es el coste imputado en euros, P el precio de adquisición, m los meses de uso en el proyecto y v "
        "la vida útil en años. El hardware se reduce a un equipo, porque las dos máquinas virtuales y el "
        "subsistema Linux con GPU se ejecutan en el mismo equipo físico; no se alquiló ningún servicio en la nube. "
        "La Tabla 3.3 recoge el hardware y su amortización."
    )
    b.tabla(
        ["Concepto", "Precio (€)", "Uso (meses)", "Coste imputado (€)"],
        [(c, coma(p, 0), str(m), coma(a, 2)) for c, p, m, a in hw] + [("Total hardware", "", "", coma(coste_hw, 2))],
        "Tabla 3.3: Hardware empleado y coste imputado al proyecto con la ecuación (3.1), vida útil de {0} años.".format(sup["vida_util_hardware_anios"]),
        anchos_cm=[8.4, 2.2, 2.4, 3.0], alineaciones=["l", "c", "c", "c"],
    )
    b.parrafo(
        "Todo el software empleado es libre o está incluido en licencias de la universidad, de modo que su "
        "coste es nulo: {0}. Es una característica del trabajo y no una casualidad: la elección de Python, de "
        "herramientas de empaquetado de código abierto y de un servidor web estándar responde a los principios "
        "del apartado 2.1 y permite que el experimento se reproduzca sin coste de licencias. La Tabla 3.4 reúne "
        "las tres partidas.".format("; ".join(s["concepto"] for s in cfg["software"]))
    )
    b.tabla(
        ["Partida", "Detalle", "Coste (€)"],
        [
            ("Recursos humanos: alumno", "{0} h × {1} €/h".format(horas_total, sup["tarifa_alumno_eur_h"]), coma(coste_alumno, 2)),
            ("Recursos humanos: tutor", "{0} h × {1} €/h".format(sup["horas_tutor"], sup["tarifa_tutor_eur_h"]), coma(coste_tutor, 2)),
            ("Hardware", "amortización de {0} meses (Tabla 3.3)".format(meses_proyecto), coma(coste_hw, 2)),
            ("Software", "libre o incluido", coma(coste_sw, 2)),
            ("Total", "", coma(total, 2)),
        ],
        "Tabla 3.4: Coste total estimado del proyecto.",
        anchos_cm=[5.0, 7.4, 3.6], alineaciones=["l", "l", "c"],
    )
    b.parrafo(
        "El coste total estimado es de {0}, del que el {1} % corresponde a recursos humanos. Es el perfil típico "
        "de un trabajo de software con infraestructura propia: el coste está en las horas, no en los medios.".format(
            eur(total), coma(100 * (coste_alumno + coste_tutor) / total, 0))
    )
    # Cierre del capitulo, sin epigrafe.
    b.parrafo(
        "Este capítulo ha descrito la organización del trabajo en {0} fases, del estudio previo a la redacción, "
        "con un cronograma apoyado en el historial de versiones, dos desviaciones declaradas, las iteraciones "
        "descartadas del controlador y la fase de blindaje que precedió al experimento final, y una estimación de "
        "{1} h de trabajo y {2} de coste, concentrado en las horas. El capítulo 4 presenta el diseño del cliente y "
        "de su banco experimental, primer resultado de esas fases.".format(len(fases), horas_total, eur(total))
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("horas", horas_total, horas_tipo, "| costes alumno", coste_alumno, "tutor", coste_tutor, "hw", round(coste_hw, 2), "total", round(total, 2))


if __name__ == "__main__":
    main()
