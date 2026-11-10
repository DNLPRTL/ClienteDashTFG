# -*- coding: utf-8 -*-
"""Pasada de coherencia sobre TODOS los borradores .docx de la memoria (los de Claude y los de Daniel convertidos).

Comprueba, leyendo los documentos en el orden de la memoria:
  1. Numeracion de figuras, tablas, listados y ecuaciones: sin duplicados, sin huecos por capitulo, toda referencia
     «Figura n.m» / «Tabla n.m» / «Listado X.n» / «ecuacion n.m» apunta a un objeto definido, y todo objeto definido se
     referencia en algun sitio.
  2. Remisiones «apartado n.m», «capitulo n», «anexo X», «punto n.m», «seccion n.m»: el destino existe como titulo.
  3. Numeros: separador de miles solo a partir de cinco cifras («1208», «35 032»); unidades separadas del numero;
     «kbps»/«Mbps» en lugar de «kbit/s»/«Mbit/s».
  4. Siglas: inventario de las usadas frente al diccionario de generar_acronimos.py (avisa de las que faltan).
  5. Citas: todas las claves estan en bibliografia.bib; entradas del .bib citadas en ningun sitio (solo informa).
  6. Comprobador de la biblia (comprobar_borrador_docx.py) sobre cada documento, agregando sus avisos.
Imprime los hallazgos agrupados y termina con codigo 1 si hay alguno que no sea informativo.

Ejecutar desde la raiz del repo:  python docs/memoria/apoyo/comprobar_coherencia.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generar_acronimos import ACRONIMOS, NO_SIGLAS  # noqa: E402

BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"
ORDEN = ["resumen_abstract", "cap1_introduccion", "cap2_1_2_has_dash", "cap2_3_4_problema_familias",
         "cap2_5_7_qoe_reproductores_lagunas", "cap3_planificacion_costes", "cap4_diseno_daniel", "cap5_1_2_daniel",
         "cap5_3_analizador_mpd", "cap5_4_ejecutor_configuracion", "cap5_5_controladores_clasicos",
         "cap5_6_controlador_propio", "cap5_7_entorno_entrenamiento", "cap5_8_resumen_capitulo5",
         "cap6_1_diseno_experimento", "cap6_2_metricas_hipotesis", "cap6_3_integridad_verificacion",
         "cap6_4_resultados_hipotesis", "cap6_5_descriptivos", "cap6_6_exploratorio", "cap6_7_interpretacion_cierre",
         "cap7_conclusiones", "anexos"]
# Enteros largos que no son cantidades (normas, timescales, modelos de CPU, identificadores) y no llevan separador.
NO_CANTIDADES = {"23009", "14496", "15360", "61440", "60000", "240000", "14600", "3986", "9110", "9111", "9112", "8601"}


def leer(nombre):
    d = Document(str(BORRADORES / (nombre + ".docx")))
    cuerpo, titulos, pies, ecuaciones = [], [], [], []
    for hijo in d.element.body.iterchildren():
        tag = hijo.tag.rsplit("}", 1)[-1]
        if tag == "p":
            p = Paragraph(hijo, d)
            est = p.style.name
            if est.startswith("Heading") or est == "Capitulo numero":
                titulos.append(p.text)
            elif est.startswith("Pie de"):
                pies.append(p.text)
            elif est == "Ecuacion":
                ecuaciones.append(p.text)
            if est not in ("Codigo", "Bibliografia"):
                cuerpo.append(p.text)
        elif tag == "tbl":
            for fila in Table(hijo, d).rows:
                for celda in fila.cells:
                    cuerpo.append(celda.text)
    return "\n".join(cuerpo), titulos, pies, ecuaciones


def clave_num(v):
    a, b = v.split(".")
    return (0, int(a), int(b)) if a.isdigit() else (1, a, int(b))


def main():
    hallazgos = defaultdict(list)
    info = defaultdict(list)
    textos, titulos_todos = {}, set()
    definidos, referidos = defaultdict(list), defaultdict(list)
    ecs_def, ecs_ref = [], []

    for n in ORDEN:
        cuerpo, titulos, pies, ecuaciones = leer(n)
        textos[n] = cuerpo
        for t in titulos:
            m = re.match(r"^((?:[A-C]|\d+)(?:\.\d+)*)\. ", t)
            if m:
                titulos_todos.add(m.group(1))
            m = re.match(r"^(?:Capítulo|Anexo) (\w+)$", t)
            if m:
                titulos_todos.add(m.group(1))
        for p in pies:
            m = re.match(r"^(Figura|Tabla|Listado) ([A-Z0-9]+\.\d+):", p)
            if m:
                definidos[m.group(1)].append((m.group(2), n))
            else:
                hallazgos["pies con formato distinto"].append((n, p[:60]))
        for m in re.finditer(r"\b(Figura|Tabla|Listado)s? ([A-Z0-9]+\.\d+)", cuerpo):
            referidos[m.group(1)].append((m.group(2), n))
        for e in ecuaciones:
            m = re.search(r"\((\d+\.\d+)\)\s*$", e)
            if m:
                ecs_def.append(m.group(1))
        ecs_ref += re.findall(r"(?:ecuaci[oó]n|expresi[oó]n) \((\d+\.\d+)\)|ecuaci[oó]n (\d+\.\d+)", cuerpo)

    # 1. Numeracion de objetos
    for tipo in ("Figura", "Tabla", "Listado"):
        conteo = Counter(v for v, _ in definidos[tipo])
        for v, k in conteo.items():
            if k > 1:
                hallazgos["objetos duplicados"].append((tipo, v, [d for x, d in definidos[tipo] if x == v]))
        defs = set(conteo)
        refs = set(v for v, _ in referidos[tipo])
        for v in sorted(refs - defs, key=clave_num):
            hallazgos["referencias a objetos no definidos"].append((tipo, v, sorted({d for x, d in referidos[tipo] if x == v})))
        for v in sorted(defs - refs, key=clave_num):
            hallazgos["objetos definidos y nunca referidos"].append((tipo, v))
        por_cap = defaultdict(list)
        for v in defs:
            c, k = v.split(".")
            por_cap[c].append(int(k))
        for c, ks in por_cap.items():
            huecos = [k for k in range(1, max(ks) + 1) if k not in ks]
            if huecos:
                hallazgos["huecos en la numeracion"].append((tipo, c, huecos))
    ecs_ref_set = set(a or b for a, b in ecs_ref)
    for v in sorted(ecs_ref_set - set(ecs_def), key=clave_num):
        hallazgos["referencias a ecuaciones no definidas"].append(v)
    conteo_ec = Counter(ecs_def)
    for v, k in conteo_ec.items():
        if k > 1:
            hallazgos["ecuaciones duplicadas"].append(v)

    # 2. Remisiones
    for c in "1234567":
        titulos_todos.add(c)
    for n, t in textos.items():
        for m in re.finditer(r"\b(?:[Aa]partados?|[Ss]ecci[oó]n|[Pp]unto|[Cc]ap[ií]tulos?|[Aa]nexos?) ((?:[A-C]|\d+)(?:\.\d+)*)", t):
            ref = m.group(1).rstrip(".")
            if ref not in titulos_todos:
                hallazgos["remisiones a apartados inexistentes"].append((n, m.group(0)))

    # 3. Numeros y unidades
    for n, t in textos.items():
        for m in re.finditer(r"(?<![\d,.])\d \d{3}(?![\d])", t):
            hallazgos["separador de miles en cuatro cifras"].append((n, m.group(0)))
        for m in re.finditer(r"(?<![\d,.:/])\d{5,}(?![\d,.])", t):
            if m.group(0) not in NO_CANTIDADES and not m.group(0).startswith("0"):
                info["enteros de cinco o mas cifras sin separador (identificadores o hashes: normal)"].append((n, m.group(0)))
        for m in re.finditer(r"\d(?:ms|kB|MB|GB|Mbit/s|kbit/s|fps|kbps|Mbps|Hz)\b", t):
            hallazgos["unidad pegada al numero"].append((n, t[max(0, m.start() - 10):m.end()]))
        for m in re.finditer(r"\b[kM]bps\b", t):
            hallazgos["kbps/Mbps en lugar de kbit/s, Mbit/s"].append((n, t[max(0, m.start() - 15):m.end()]))
        for m in re.finditer(r"(?<=[a-z,;(] )(?:Capítulo|Apartado|Sección) \d", t):
            hallazgos["Capítulo/Apartado con mayúscula en medio de frase"].append((n, t[max(0, m.start() - 20):m.end() + 5]))

    # 4. Siglas
    todo = "\n".join(textos.values())
    usadas = Counter()
    for m in re.finditer(r"(?<![\w/.\-])([A-Z][A-Za-z\-]{1,7})(?![\w/])", todo):
        s = m.group(1)
        if sum(ch.isupper() for ch in s) >= 2 and not re.match(r"^[A-Z][a-z]+$", s):
            usadas[s] += 1
    for s in sorted(usadas):
        if s not in ACRONIMOS and s not in NO_SIGLAS:
            hallazgos["siglas fuera del diccionario de acronimos"].append((s, usadas[s]))

    # 5. Citas
    claves_bib = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))
    citadas = set()
    for n, t in textos.items():
        for m in re.finditer(r"\[([A-Za-z][\w]*)\]", t):
            k = m.group(1)
            if k in claves_bib:
                citadas.add(k)
            elif re.match(r"^[A-Za-z]\w*\d{4}\w*$|Docs?$|Doc$", k):
                hallazgos["citas fuera del .bib"].append((n, k))
    info["entradas del .bib no citadas (no se imprimen)"] = sorted(claves_bib - citadas)

    # 6. Comprobador de la biblia por documento
    for n in ORDEN + ["bibliografia", "acronimos"]:
        ruta = BORRADORES / (n + ".docx")
        if not ruta.exists():
            continue
        res = subprocess.run([sys.executable, "-I", "-X", "utf8", str(Path(__file__).with_name("comprobar_borrador_docx.py")), str(ruta)],
                             capture_output=True, text=True, encoding="utf-8")
        for linea in res.stdout.splitlines():
            if linea.startswith(" - "):
                aviso = linea[3:]
                if "puede ser de otro apartado" in aviso:
                    continue  # referencia cruzada entre borradores del mismo capitulo: la resuelve el punto 1
                hallazgos["avisos del comprobador de la biblia"].append((n, aviso))

    # Informe
    print("documentos leídos:", len(textos), "| figuras:", len(set(v for v, _ in definidos["Figura"])),
          "| tablas:", len(set(v for v, _ in definidos["Tabla"])), "| listados:", len(set(v for v, _ in definidos["Listado"])),
          "| ecuaciones:", len(set(ecs_def)), "| claves citadas:", len(citadas))
    for k, v in info.items():
        print("INFO", k, ":", v if len(v) <= 12 else v[:12] + ["…{0} más".format(len(v) - 12)])
    if not hallazgos:
        print("sin hallazgos")
        return 0
    for k, v in hallazgos.items():
        print("HALLAZGO", k, "({0})".format(len(v)))
        for x in v[:25]:
            print("   -", x)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
