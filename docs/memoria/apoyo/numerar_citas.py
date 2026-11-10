# -*- coding: utf-8 -*-
"""Escribe en docs/memoria/borradores_docx/numerado/ una copia de cada borrador con las citas [clave] convertidas a
[n] segun apoyo/bibliografia_numeracion.json (generado por generar_bibliografia.py). Conserva el formato de los
runs (negritas, cursivas, rojo de los cambios de Daniel). Grupos «[a], [b]» pasan a «[n], [m]».

Ejecutar desde la raiz del repo, DESPUES de generar_bibliografia.py:  python docs/memoria/apoyo/numerar_citas.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from docx import Document

RAIZ_REPO = Path(__file__).resolve().parents[3]
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
SALIDA = BORRADORES / "numerado"
NUMERACION = RAIZ_REPO / "docs" / "memoria" / "apoyo" / "bibliografia_numeracion.json"


def parrafos(doc):
    for p in doc.paragraphs:
        yield p
    for t in doc.tables:
        for fila in t.rows:
            for celda in fila.cells:
                for p in celda.paragraphs:
                    yield p


def main():
    numero = json.load(open(NUMERACION, encoding="utf-8"))["numero_por_clave"]
    patron = re.compile(r"\[(" + "|".join(re.escape(k) for k in sorted(numero, key=len, reverse=True)) + r")\]")
    SALIDA.mkdir(exist_ok=True)
    total = 0
    for ruta in sorted(BORRADORES.glob("*.docx")):
        if ruta.name == "bibliografia.docx":
            continue
        doc = Document(str(ruta))
        n_doc = 0
        partidas = []
        for p in parrafos(doc):
            if "[" not in p.text:
                continue
            for run in p.runs:
                if "[" in run.text:
                    nuevo, k = patron.subn(lambda m: "[{0}]".format(numero[m.group(1)]), run.text)
                    if k:
                        run.text = nuevo
                        n_doc += k
            # citas partidas entre runs (no deberia ocurrir: se avisan y se dejan)
            for m in patron.finditer(p.text):
                partidas.append((ruta.name, m.group(0)))
        doc.save(str(SALIDA / ruta.name))
        total += n_doc
        print("{0:40s} {1:3d} citas numeradas".format(ruta.name, n_doc) + ("  AVISO sin convertir: " + str(partidas) if partidas else ""))
    print("total:", total, "| salida:", SALIDA)


if __name__ == "__main__":
    main()
