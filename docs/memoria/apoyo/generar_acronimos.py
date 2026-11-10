# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/acronimos.docx: la lista de acronimos de los preliminares (biblia §3.9):
sigla en negrita, expansion inglesa en cursiva y traduccion entre parentesis; SOLO las siglas que se usan en los
borradores (se cuentan por programa sobre todos los .docx). Las siglas que aparecen en el texto y no estan en el
diccionario se imprimen como aviso, para decidir si son siglas o nombres propios.

Ejecutar desde la raiz del repo:  python docs/memoria/apoyo/generar_acronimos.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
SALIDA = BORRADORES / "acronimos.docx"

# sigla: (expansion inglesa o None si es castellana, traduccion o aclaracion)
ACRONIMOS = {
    "ABR": ("Adaptive Bitrate", "adaptación de la tasa binaria"),
    "AMD": ("Advanced Micro Devices", "fabricante de la GPU de entrenamiento"),
    "BBA": ("Buffer-Based Approach", "algoritmo de adaptación basado en el buffer"),
    "BMFF": ("Base Media File Format", "formato de fichero multimedia base de ISO"),
    "BOLA": ("Buffer Occupancy based Lyapunov Algorithm", "algoritmo de adaptación basado en la ocupación del buffer"),
    "CBR": ("Constant Bitrate", "tasa binaria constante"),
    "CMAF": ("Common Media Application Format", "formato común de aplicaciones multimedia"),
    "CPU": ("Central Processing Unit", "unidad central de proceso"),
    "CSV": ("Comma-Separated Values", "valores separados por comas"),
    "CVaR": ("Conditional Value at Risk", "valor en riesgo condicional"),
    "DASH": ("Dynamic Adaptive Streaming over HTTP", "streaming adaptativo dinámico sobre HTTP"),
    "FCC": ("Federal Communications Commission", "comisión federal de comunicaciones de Estados Unidos"),
    "GPU": ("Graphics Processing Unit", "unidad de procesamiento gráfico"),
    "GRU": ("Gated Recurrent Unit", "unidad recurrente con puertas"),
    "HAS": ("HTTP Adaptive Streaming", "streaming adaptativo sobre HTTP"),
    "HLS": ("HTTP Live Streaming", "protocolo de streaming de Apple"),
    "HSDPA": ("High-Speed Downlink Packet Access", "acceso de paquetes de alta velocidad en el enlace descendente (3G)"),
    "HTTP": ("Hypertext Transfer Protocol", "protocolo de transferencia de hipertexto"),
    "IC": (None, "intervalo de confianza"),
    "IEC": ("International Electrotechnical Commission", "comisión electrotécnica internacional"),
    "ISO": ("International Organization for Standardization", "organización internacional de normalización"),
    "JSON": ("JavaScript Object Notation", "notación de objetos de JavaScript"),
    "LTE": ("Long Term Evolution", "red móvil de cuarta generación"),
    "LTS": ("Long-Term Support", "versión con soporte extendido"),
    "MLP": ("Multilayer Perceptron", "perceptrón multicapa"),
    "MPC": ("Model Predictive Control", "control predictivo basado en modelo"),
    "MPD": ("Media Presentation Description", "descripción de la presentación multimedia; el manifiesto DASH"),
    "MPEG": ("Moving Picture Experts Group", "grupo de expertos en imágenes en movimiento"),
    "MV": (None, "máquina virtual"),
    "NB-IoT": ("Narrowband Internet of Things", "internet de las cosas de banda estrecha"),
    "NSA": ("Non-Standalone", "despliegue 5G no autónomo, apoyado en la red 4G"),
    "QoE": ("Quality of Experience", "calidad de experiencia"),
    "RFC": ("Request for Comments", "documento normativo del IETF"),
    "SHA": ("Secure Hash Algorithm", "algoritmo de resumen criptográfico; SHA-256"),
    "TCP": ("Transmission Control Protocol", "protocolo de control de transmisión"),
    "TFG": (None, "Trabajo Fin de Grado"),
    "TOST": ("Two One-Sided Tests", "dos pruebas unilaterales; prueba de equivalencia"),
    "UCC": ("University College Cork", "universidad de Cork, origen de dos conjuntos de trazas"),
    "URL": ("Uniform Resource Locator", "localizador uniforme de recursos"),
    "UTC": ("Coordinated Universal Time", "tiempo universal coordinado"),
    "VBR": ("Variable Bitrate", "tasa binaria variable"),
    "VMAF": ("Video Multi-Method Assessment Fusion", "métrica perceptual de calidad de vídeo de Netflix"),
    "WSL": ("Windows Subsystem for Linux", "subsistema de Windows para Linux"),
    "XML": ("Extensible Markup Language", "lenguaje de marcado extensible"),
    "YAML": ("YAML Ain't Markup Language", "formato de configuración legible"),
}
# Tokens con mayusculas que NO son siglas (nombres propios, unidades, identificadores) y no se listan.
NO_SIGLAS = {"PyTorch", "NumPy", "PyYAML", "ROCm", "GPAC", "FFmpeg", "GitHub", "YouTube", "GaVist", "AdamW", "BaseURL",
             "MERINA", "SODA", "SafeSABR", "DYNAMIC", "INFO", "DEBUG", "RX", "XT", "GiB", "MB", "GB", "kB", "NYU",
             "METS", "HM", "ID", "NB", "IoT", "BOLA-E", "NYU-METS"}


def texto_docx(ruta, con_codigo=False):
    d = Document(str(ruta))
    partes = []
    for hijo in d.element.body.iterchildren():
        tag = hijo.tag.rsplit("}", 1)[-1]
        if tag == "p":
            p = Paragraph(hijo, d)
            if con_codigo or p.style.name not in ("Codigo", "Bibliografia"):
                partes.append(p.text)
        elif tag == "tbl":
            for fila in Table(hijo, d).rows:
                for celda in fila.cells:
                    partes.append(celda.text)
    return "\n".join(partes)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    docs = sorted(p for p in BORRADORES.glob("*.docx") if p.name not in ("acronimos.docx", "bibliografia.docx", "resumen_abstract.docx"))
    texto = "\n".join(texto_docx(p) for p in docs)
    usadas = Counter()
    for m in re.finditer(r"(?<![\w/.\-])([A-Z][A-Za-z\-]{1,7})(?![\w/])", texto):
        s = m.group(1)
        if sum(ch.isupper() for ch in s) >= 2 and not re.match(r"^[A-Z][a-z]+$", s):
            usadas[s] += 1
    usadas["NB-IoT"] += len(re.findall(r"\bNB-IoT\b", texto))
    usadas["IC"] += len(re.findall(r"\bIC\d{2}\b|\bIC\b", texto))  # «IC95», «IC90» en las tablas del cap 6
    presentes = [s for s in ACRONIMOS if usadas.get(s, 0) > 0]
    ausentes = [s for s in ACRONIMOS if usadas.get(s, 0) == 0]
    desconocidas = sorted(s for s in usadas if s not in ACRONIMOS and s not in NO_SIGLAS)

    b = Borrador(PLANTILLA)
    b.doc.add_paragraph("Acrónimos", style="Heading 1")
    for sigla in sorted(presentes, key=lambda s: s.lower()):
        ingles, trad = ACRONIMOS[sigla]
        if ingles:
            b.parrafo("**{0}**: //{1}// ({2}).".format(sigla, ingles, trad))
        else:
            b.parrafo("**{0}**: {1}.".format(sigla, trad))
    b.guardar(SALIDA)
    print("Guardado:", SALIDA, "|", len(presentes), "siglas usadas de", len(ACRONIMOS), "en el diccionario")
    print("usos:", {s: usadas[s] for s in sorted(presentes, key=lambda s: -usadas[s])})
    if ausentes:
        print("en el diccionario pero no usadas (no se imprimen):", ausentes)
    if desconocidas:
        print("AVISO, con mayúsculas y fuera del diccionario (¿sigla o nombre?):", desconocidas)


if __name__ == "__main__":
    main()
