# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/resumen_abstract.docx: pagina de resumen (titulo, autor, palabras clave,
resumen en cuatro parrafos) y pagina de abstract (lo mismo en ingles), segun la biblia §3 (300-400 palabras,
6-8 palabras clave, siglas definidas tambien aqui).

Regla cero: ninguna cifra nueva. Cada numero del resumen ya esta en los .docx del capitulo 6 (se comprueba), y los
datos del experimento se leen del protocolo del material entregado. El titulo se lee del plan maestro (§1, opcion A).

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_resumen.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
PLAN = RAIZ_REPO / "docs" / "memoria" / "00_PLAN_MAESTRO_MEMORIA.md"
SALIDA = BORRADORES / "resumen_abstract.docx"

AUTOR = "Daniel Pretel"
TITULO_EN = ("A modular experimental platform for MPEG-DASH adaptive streaming: a playback client and a "
             "risk-aware predictive ABR controller")
PALABRAS_CLAVE = ["streaming adaptativo", "MPEG-DASH", "adaptación de tasa (ABR)", "calidad de experiencia (QoE)",
                  "control predictivo (MPC)", "predicción de cuantiles", "riesgo (CVaR)", "reproducibilidad"]
KEYWORDS = ["adaptive streaming", "MPEG-DASH", "adaptive bitrate (ABR)", "quality of experience (QoE)",
            "model predictive control (MPC)", "quantile prediction", "risk (CVaR)", "reproducibility"]
CIFRAS_REPETIDAS = ["−0,001", "±0,15", "0,041", "0,162", "1208", "74 ventanas", "35 032"]
PROHIBIDOS = ["SPBC", "Q_H", "mpc_prudente", "Phase", "Fase 6", "v1", "v2", "Neural", "tfg_final",
              "benchmark_autorizado", "ensemble temporal"]


def texto_docx(ruta):
    d = Document(str(ruta))
    return "\n".join(p.text for p in d.paragraphs)


def datos_verificados():
    plan = PLAN.read_text(encoding="utf-8")
    m = re.search(r"\*\*Título \(opción A elegida; confirmar con tutor\):\*\*\s*\n> \*(.+?)\*", plan, re.S)
    assert m, "titulo A no encontrado en el plan"
    titulo = " ".join(t for t in m.group(1).split() if t != ">").rstrip(".")
    assert ">" not in titulo and "*" not in titulo, titulo
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    hip = protocolo["hipotesis"]
    assert len(hip["principales"]) == 5 and hip["margen_equivalencia_qoe"] == 0.15 and "Holm" in hip["multiplicidad"]
    assert len(protocolo["controladores"]) == 8 and protocolo["num_sesiones"] == 1208
    assert len(protocolo["perfiles_video"]) == 5
    anteriores = "\n".join(texto_docx(BORRADORES / n) for n in (
        "cap6_1_diseno_experimento.docx", "cap6_3_integridad_verificacion.docx", "cap6_4_resultados_hipotesis.docx",
        "cap6_5_descriptivos.docx", "cap6_7_interpretacion_cierre.docx"))
    for frag in CIFRAS_REPETIDAS:
        assert frag in anteriores, frag
    assert 6 <= len(PALABRAS_CLAVE) <= 8 and len(PALABRAS_CLAVE) == len(KEYWORDS)
    return {"titulo": titulo, "n_hipotesis": len(hip["principales"]), "n_controladores": len(protocolo["controladores"])}


RESUMEN = [
    "El vídeo bajo demanda se distribuye sobre HTTP con el estándar MPEG-DASH (Dynamic Adaptive Streaming over "
    "HTTP), que ofrece el contenido en segmentos a varias calidades y deja al cliente la elección. Esa adaptación de tasa o ABR (Adaptive Bitrate) se decide con incertidumbre sobre el ancho "
    "de banda futuro y, con contenido de tasa variable, con segmentos cuyo tamaño real se aparta del nominal. Los "
    "métodos con aprendizaje suelen evaluarse en simuladores de fidelidad no comprobada.",

    "Este trabajo construye un cliente MPEG-DASH modular en Python que descarga de un servidor web "
    "real, gestiona el buffer, reproduce con un motor real o simulado y registra cada decisión. Sobre una interfaz "
    "común se implementan cuatro controladores clásicos según sus artículos y un controlador propio que combina un "
    "conjunto de redes recurrentes, que predice cuantiles del throughput futuro, con un "
    "planificador de control predictivo o MPC (Model Predictive Control) que usa los tamaños reales de los "
    "segmentos y una medida de riesgo, el valor en riesgo condicional o CVaR, sobre los peores escenarios. "
    "El modelo se entrena fuera de línea en un simulador fiel al contenido real, con trazas de red públicas sin "
    "fuga hacia las de evaluación.",

    "La evaluación es un experimento único con protocolo fijado antes de ejecutar: 74 ventanas de trazas reales, "
    "dos vídeos por ventana, uno de ellos nuevo, y ocho controladores, 1208 sesiones, con cinco hipótesis "
    "prerregistradas y corrección por comparaciones múltiples. Las cinco se aceptan: el controlador propio obtiene "
    "una calidad de experiencia o QoE (Quality of Experience) equivalente a la del MPC robusto canónico (diferencia "
    "media de −0,001 puntos, dentro del margen de ±0,15) con unas cuatro veces menos paradas (0,041 frente a 0,162 "
    "por sesión), y las variantes de ablación muestran que la red de cuantiles y la medida de riesgo aportan cada "
    "una. No tiene la QoE media más alta de los ocho.",

    "Las aportaciones son un banco de pruebas reproducible, un controlador que acota el aprendizaje a la predicción "
    "y decide con el riesgo, un método de evaluación prerregistrado cuyo paquete de evidencia permite repetir "
    "idénticas sus 35 032 decisiones, y el registro de las líneas descartadas. Los resultados se limitan a una red "
    "emulada por trazas, sin pila TCP ni tráfico competidor, a redes de capacidad baja y media, a un contenido "
    "nuevo y al bitrate como medida de calidad.",
]

ABSTRACT = [
    "Video on demand is delivered over HTTP with the MPEG-DASH standard (Dynamic Adaptive Streaming over "
    "HTTP), which offers the content in segments at several quality levels and leaves the choice to the client. "
    "That adaptive bitrate (ABR) decision is made under uncertainty about "
    "the future bandwidth and, with variable-bitrate content, with segments whose actual size departs from the "
    "nominal one. Learning-based methods are usually evaluated in simulators of unverified fidelity.",

    "This work builds a modular MPEG-DASH client in Python that downloads from a real web server, "
    "manages the buffer, plays back with a real or a simulated engine and records every decision. On a common "
    "interface, four classical controllers are implemented according to their papers, together with an own "
    "controller that combines an ensemble of recurrent networks, which predicts quantiles of the future throughput, "
    "with a model predictive control (MPC) planner that uses the actual segment sizes and a risk "
    "measure, the conditional value at risk (CVaR), over the worst scenarios. The model is trained offline "
    "in a simulator faithful to the real content, with public network traces that do not leak into the evaluation "
    "ones.",

    "The evaluation is a single experiment with a protocol fixed before running it: 74 real trace windows, two "
    "videos per window, one of them new, and eight controllers, 1208 sessions, with five preregistered hypotheses "
    "and correction for multiple comparisons. All five are accepted: the own controller achieves a quality of "
    "experience (QoE) equivalent to that of the canonical robust MPC (mean difference of −0.001 points, within the "
    "±0.15 margin) with about four times fewer stalls (0.041 versus 0.162 per session), and the ablation variants "
    "show that the quantile network and the risk measure each contribute. It does not have the highest mean QoE "
    "of the eight.",

    "The contributions are a reproducible test bench, a controller that restricts learning to prediction and "
    "decides with the risk, a preregistered evaluation method whose evidence package allows its 35,032 decisions "
    "to be replayed identically, and the record of the discarded lines. The results are limited to a "
    "trace-emulated network, without a TCP stack or competing traffic, to networks of low and medium capacity, to "
    "a single new content and to bitrate as the quality measure.",
]


def titulo_pagina(b, texto):
    """Titulo de la pagina de resumen: negrita a 16 pt, sin numero de capitulo (como en el corpus del tutor)."""
    p = b.doc.add_paragraph(style="Normal")
    r = p.add_run(texto)
    r.bold = True
    r.font.size = Pt(16)
    p.paragraph_format.space_after = Pt(12)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    d = datos_verificados()
    b = Borrador(PLANTILLA)
    # Pagina de resumen -----------------------------------------------------------------------------------
    titulo_pagina(b, d["titulo"])
    b.parrafo(AUTOR)
    b.parrafo("**Palabras clave:** " + ", ".join(PALABRAS_CLAVE))
    b.parrafo("**Resumen**")
    for p in RESUMEN:
        b.parrafo(p)
    # Pagina de abstract (salto de pagina en el titulo, sin pagina en blanco) ------------------------------
    titulo_pagina(b, TITULO_EN).paragraph_format.page_break_before = True
    b.parrafo(AUTOR)
    b.parrafo("**Keywords:** " + ", ".join(KEYWORDS))
    b.parrafo("**Abstract**")
    for p in ABSTRACT:
        b.parrafo(p)

    # Comprobaciones --------------------------------------------------------------------------------------
    # Palabras = tokens separados por espacio (MPEG-DASH, −0,001 o 35 032 cuentan como una o dos, como al leer).
    n_es = len(" ".join(RESUMEN).split())
    n_en = len(" ".join(ABSTRACT).split())
    assert 300 <= n_es <= 400, n_es
    assert 300 <= n_en <= 420, n_en
    texto_es = " ".join(RESUMEN)
    for sigla, expansion in (("DASH", "Dynamic Adaptive Streaming over HTTP"), ("ABR", "Adaptive Bitrate"),
                             ("MPC", "Model Predictive Control"), ("CVaR", "valor en riesgo condicional"),
                             ("QoE", "Quality of Experience")):
        assert sigla in texto_es and expansion in texto_es, sigla
    texto = texto_es + " " + " ".join(ABSTRACT)
    for nombre in PROHIBIDOS:
        assert not re.search(r"\b" + re.escape(nombre) + r"\b", texto), nombre
    permitidas = " ".join(CIFRAS_REPETIDAS)
    for dec in set(re.findall(r"[−+]?\d+,\d+", texto_es)):
        assert dec in permitidas, dec
    for dec in set(re.findall(r"[−+]?\d+\.\d+", " ".join(ABSTRACT))):
        assert dec.replace(".", ",") in permitidas, dec
    for ent in set(re.findall(r"\b\d{4,}\b|\b\d{2}[ ,]\d{3}\b", texto)):
        assert ent in ("1208", "35 032", "35,032"), ent
    assert d["n_hipotesis"] == 5 and d["n_controladores"] == 8
    b.guardar(SALIDA)
    print("Guardado:", SALIDA)
    print("Palabras resumen:", n_es, "| abstract:", n_en, "| palabras clave:", len(PALABRAS_CLAVE))


if __name__ == "__main__":
    main()
