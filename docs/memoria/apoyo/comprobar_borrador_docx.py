# -*- coding: utf-8 -*-
"""Lista de comprobaciones de la biblia (apartado 7.4) sobre un borrador .docx.

Uso: python docs/memoria/apoyo/comprobar_borrador_docx.py borrador.docx
Comprueba: titulos numerados en estilo de titulo, figuras y tablas anunciadas antes del pie,
formato de los pies, coma decimal, tics de IA prohibidos, markdown residual, claves de cita
presentes en bibliografia.bib y recuento de palabras del cuerpo.
"""
import re
import sys
from pathlib import Path

from docx import Document

RAIZ = Path(__file__).resolve().parents[3]
BIB = RAIZ / "docs" / "memoria" / "bibliografia.bib"
TICS = [
    "—", "cabe destacar", "conviene subrayar", "conviene precisar", "dicho de otro modo",
    "en definitiva", "es importante destacar", "en el vasto", "clave para", "muy robust", "más robust", "bastante robust",
]


def main(ruta):
    doc = Document(ruta)
    avisos = []
    parrafos = [(p.style.name, p.text) for p in doc.paragraphs]
    texto = "\n".join(t for _, t in parrafos)
    celdas = "\n".join(c.text for t in doc.tables for r in t.rows for c in r.cells)

    # 1. Titulos numerados y en estilo de titulo.
    for estilo, t in parrafos:
        if estilo.startswith("Heading") and estilo != "Heading 1" and not re.match(r"^([A-Z]|\d+)(\.\d+)*\. \S", t):  # Heading 1 = titulo del capitulo o anexo, sin numero; anexos: A.1.
            avisos.append("titulo sin numeracion 'N.M. Titulo': " + t)
        if estilo == "Normal" and re.match(r"^\d+\.\d+(\.\d+)?\. [A-ZÁÉÍÓÚ]", t) and len(t) < 90:
            avisos.append("posible titulo en estilo Normal: " + t)

    # 2. Pies y referencias.
    pies = [(e, t) for e, t in parrafos if e.startswith("Pie de")]
    for estilo, t in pies:
        m = re.match(r"^(Figura|Tabla|Listado) ((?:[A-Z]|\d+)\.\d+): .+\.$", t)
        if not m:
            avisos.append("pie con formato incorrecto: " + t[:60])
            continue
        tipo, num = m.group(1), m.group(2)
        pos_pie = texto.find(t)
        antes = texto[:pos_pie]
        if ("{0} {1}".format(tipo, num) not in antes):
            avisos.append("{0} {1} no se anuncia antes del pie".format(tipo, num))
        if tipo == "Figura" and estilo != "Pie de figura" or tipo == "Tabla" and estilo != "Pie de tabla":
            avisos.append("pie con estilo cambiado: " + t[:40])
    for ref in set(re.findall(r"\b(Figura|Tabla) ((?:[A-Z]|\d+)\.\d+)\b", texto)):
        if not any(t.startswith("{0} {1}:".format(*ref)) for _, t in pies):
            if ref[1].split(".")[0] == texto[:200].strip()[0:1]:
                avisos.append("referencia a {0} {1} sin pie en este borrador (puede ser de otro apartado)".format(*ref))
    if re.search(r"\bfigura \d|\btabla \d|\bFig\.", texto):
        avisos.append("mencion en minuscula o 'Fig.' (la biblia pide 'Figura 4.3', 'Tabla 4.1')")

    # 3. Numeros: coma decimal (el abstract en ingles, si lo hay, lleva punto decimal y se excluye; los listados
    #    de codigo tambien, porque reproducen ficheros y comandos tal cual).
    texto_es = "\n".join(t for e, t in parrafos if e not in ("Codigo", "Bibliografia"))  # DOI y URL llevan puntos
    texto_es = texto_es.split("\nAbstract\n")[0] if "\nKeywords:" in texto_es else texto_es
    for m in re.finditer(r"\b\d+\.\d+\b", texto_es + "\n" + celdas):
        trozo = m.group(0)
        if re.match(r"^\d\.\d+$", trozo) and int(trozo.split(".")[0]) <= 9 and len(trozo.split(".")[1]) <= 2:
            continue  # numero de apartado, ecuacion, tabla o figura
        if re.search(r"Ubuntu " + re.escape(trozo), texto_es + "\n" + celdas):
            continue  # version de Ubuntu (20.04), no es un decimal
        if re.search(r"\b\d+\.\d+\.\d+\.\d+\b", texto_es + "\n" + celdas) and re.search(
                r"(^|[^\d.])" + re.escape(trozo) + r"\.\d|\d\." + re.escape(trozo) + r"([^\d.]|$)", texto_es + "\n" + celdas):
            continue  # direccion IP (192.168.1.132), no es un decimal
        avisos.append("punto decimal: " + trozo)

    # 4. Tics y markdown.
    bajo = texto.lower()
    sin_mpc = bajo
    for tic in TICS:
        if tic.lower() in sin_mpc:
            avisos.append("tic prohibido: " + tic.strip())
    if re.search(r"(^|\n)#|\*\*|`|\|---", texto):
        avisos.append("markdown residual")

    # 5. Citas.
    claves_bib = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))
    citas = set(re.findall(r"\[([A-Za-z][\w]*\d{4}[\w]*|rfc\d+|iso\d+[_\d]*|python\w+|\w+Doc|dashIfIop)\]", texto))
    for c in sorted(citas):
        if c not in claves_bib:
            avisos.append("cita fuera del .bib: " + c)

    # 6. Recuento.
    cuerpo = " ".join(t for e, t in parrafos if e in ("Normal", "List Bullet"))
    palabras = len(re.findall(r"\w+", cuerpo))

    print("palabras del cuerpo:", palabras, "| parrafos:", len([1 for e, _ in parrafos if e == "Normal"]),
          "| tablas:", len(doc.tables), "| citas:", sorted(citas))
    if avisos:
        print("AVISOS:")
        for a in avisos:
            print(" -", a.encode("ascii", "replace").decode())
    else:
        print("sin avisos")


if __name__ == "__main__":
    main(sys.argv[1])
