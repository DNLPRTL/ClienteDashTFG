# -*- coding: utf-8 -*-
"""Pasa los Word de Daniel (capitulo 4 y apartados 5.1-5.2) al formato de la biblia SIN tocar su redaccion.

Lee los dos .docx de `G:\\...\\backup memo\\` en solo lectura y escribe:
  docs/memoria/borradores_docx/cap4_diseno_daniel.docx
  docs/memoria/borradores_docx/cap5_1_2_daniel.docx

Solo cambia el formato, nunca las palabras:
  - los titulos escritos como texto («Capitulo 4. Diseño», «4.1. ...», «Capitulo 4.2. ...») pasan a los estilos de
    capitulo y de nivel 2 (el «Capitulo» sobrante de los niveles 2 se quita: es numeracion, no prosa);
  - los marcadores de maquetacion «[FIGURA ...]», «[TABLA ...]», «Fichero: `figuras/...`» y el prefijo «Pie: » de
    los pies desaparecen; los pies partidos en varias lineas se unen en un parrafo con el estilo de pie;
  - las imagenes incrustadas se recolocan con su pie (estilo Figura + Pie de figura); la Figura 5.1, que en el Word
    es solo una referencia a fichero, se toma de docs/memoria/figuras/;
  - los restos de markdown pasan a formato real: `x` y ‘’x’’ a cursiva, **x** a negrita, las tablas escritas con
    barras a tablas de Word; las tablas de Word se reconstruyen con el estilo de la plantilla;
  - los parrafos vacios y los espacios o tabuladores de los extremos se eliminan; las listas conservan su tipo
    (numerada o con vinetas).
Al final comprueba que la secuencia de palabras del resultado es identica a la del original (salvo los marcadores
quitados) y pasa el comprobador de la biblia, cuyos avisos se imprimen para que Daniel los corrija el mismo.

Ejecutar desde la raiz del repo:  python docs/memoria/apoyo/convertir_word_daniel.py
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
FIGURAS = RAIZ_REPO / "docs" / "memoria" / "figuras"
WORD_DANIEL = Path(r"G:\Otros ordenadores\Mi portátil\backup memo")
DOCUMENTOS = [
    (WORD_DANIEL / "Borrador Capitulo 4 Diseño.docx", BORRADORES / "cap4_diseno_daniel.docx"),
    (WORD_DANIEL / "hasta 5_2.docx", BORRADORES / "cap5_1_2_daniel.docx"),
]

RE_CAPITULO = re.compile(r"^Capítulo (\d+)\. (.+)$")
RE_H2 = re.compile(r"^(?:Capítulo )?(\d+\.\d+)\. (.+)$")
RE_PLACEHOLDER = re.compile(r"^\**\[(TABLA|FIGURA) (\d+\.\d+)")
RE_FICHERO = re.compile(r"^(Fichero: )?`figuras/([\w.]+)`\]\**$")
RE_PIE = re.compile(r"^\*?(Pie: )?((Figura|Tabla) \d+\.\d+: .*?)\*?$", re.S)
RE_SEPARADOR_MD = re.compile(r"^\|[-| ]+\|$")


def palabras(texto):
    return re.findall(r"\w+", texto)


# Ajustes tipograficos de la biblia autorizados por Daniel el 10/11 (caracteres y formato, nunca la gramatica ni la
# eleccion de palabras). Cada aplicacion se registra en CAMBIOS con su contexto para que pueda revisarlos uno a uno.
AJUSTES = [
    ("mayúscula en Figura/Tabla", re.compile(r"\b(figura|tabla)(s?) (?=\d+\.\d+)"),
     lambda m: m.group(1).capitalize() + m.group(2) + " "),
    ("espacio sobrante antes de signo", re.compile(r" +([,;:.])(?=\s|$)"), r"\1"),
    ("espacio tras dos puntos", re.compile(r"(?<=[\w)]):(?=[A-Za-zÁ-ÿ])"), ": "),
    ("doble espacio", re.compile(r"(?<=\S)  +(?=\S)"), " "),
    ("«vídeo» con tilde (como en el resto del texto)", re.compile(r"\bvideo(s?)\b"), r"vídeo\1"),
    ("sigla DASH", re.compile(r"\bDash\b"), "DASH"),
    ("errata «amuestra»", re.compile(r"\bamuestra\b"), "a muestra"),
    ("tilde «cálculo»", re.compile(r"\bcalculo estimado\b"), "cálculo estimado"),
    ("tilde «está»", re.compile(r"\besta diseñada\b"), "está diseñada"),
]
CAMBIOS = []


def ajustar(texto):
    t = texto
    for nombre, patron, repl in AJUSTES:
        for m in patron.finditer(t):
            CAMBIOS.append((nombre, t[max(0, m.start() - 25):m.end() + 25].replace("\n", " ")))
        t = patron.sub(repl, t)
    return t


def marcar(texto):
    """Restos de markdown a la marca de Borrador: `x` y ‘’x’’ a //x// (cursiva); **x** ya lo entiende."""
    t = re.sub(r"`([^`]*)`", r"//\1//", texto)
    t = re.sub(r"‘’(.*?)’’", r"//\1//", t)
    # Citas escritas con la sintaxis de LaTeX pasan a la de los borradores: \cite{a,b} -> [a], [b]
    t = re.sub(r"\\cite\{([^}]*)\}", lambda m: ", ".join("[{0}]".format(k.strip()) for k in m.group(1).split(",")), t)
    return t


def palabras_sin_cite(texto):
    """Palabras del original, descontando el «cite» de las citas LaTeX (el marcado cambia, la clave se conserva)."""
    return palabras(re.sub(r"\\cite\{", "{", texto))


class Lector:
    """Recorre el cuerpo del Word en orden: parrafos (con su numeracion e imagenes) y tablas."""

    def __init__(self, ruta):
        self.doc = Document(str(ruta))
        self.items = []
        for hijo in self.doc.element.body.iterchildren():
            tag = hijo.tag.rsplit("}", 1)[-1]
            if tag == "p":
                p = Paragraph(hijo, self.doc)
                blip = hijo.find(".//" + qn("a:blip"))
                rid = blip.get(qn("r:embed")) if blip is not None else None
                numpr = hijo.find(".//" + qn("w:numPr"))
                fmt = None
                if numpr is not None:
                    fmt = self._formato_numeracion(numpr.find(qn("w:numId")).get(qn("w:val")))
                self.items.append({"tipo": "p", "texto": ajustar(p.text.strip()), "imagen": rid, "lista": fmt})
            elif tag == "tbl":
                tb = Table(hijo, self.doc)
                filas = [[ajustar(c.text.strip()) for c in fila.cells] for fila in tb.rows]
                self.items.append({"tipo": "tbl", "filas": filas})

    def _formato_numeracion(self, num_id):
        try:
            np_ = self.doc.part.numbering_part.element
        except Exception:
            return "bullet"
        for num in np_.findall(qn("w:num")):
            if num.get(qn("w:numId")) == num_id:
                aid = num.find(qn("w:abstractNumId")).get(qn("w:val"))
                for ab in np_.findall(qn("w:abstractNum")):
                    if ab.get(qn("w:abstractNumId")) == aid:
                        return ab.find(qn("w:lvl")).find(qn("w:numFmt")).get(qn("w:val"))
        return "bullet"

    def imagen(self, rid, destino):
        parte = self.doc.part.related_parts[rid]
        ext = parte.content_type.split("/")[-1].replace("jpeg", "jpg")
        ruta = Path(destino) / "{0}.{1}".format(rid, ext)
        ruta.write_bytes(parte.blob)
        return ruta


def convertir(origen, salida, tmp):
    lector = Lector(origen)
    items = lector.items
    b = Borrador(PLANTILLA)
    stats = {"placeholders": 0, "pies_unidos": 0, "prefijo_pie": 0, "cursivas": 0, "negritas": 0, "titulos": 0,
             "tablas_md": 0, "tablas_word": 0, "figuras": 0, "vacios": 0, "listas": 0, "citas": 0, "entradillas": 0}
    palabras_orig = []  # palabras del original que deben aparecer en la salida
    consumidos = set()

    def texto_pie(i):
        """Pie en el item i (y sus continuaciones en minuscula); devuelve (texto, indices)."""
        m = RE_PIE.match(items[i]["texto"])
        texto = m.group(2).strip()
        if m.group(1):
            stats["prefijo_pie"] += 1
        indices = [i]
        j = i + 1
        while (not texto.endswith((".", "*")) and j < len(items) and items[j]["tipo"] == "p"
               and items[j]["texto"] and items[j]["texto"][0].islower()):
            texto += " " + items[j]["texto"]
            indices.append(j)
            stats["pies_unidos"] += 1
            j += 1
        texto = texto.rstrip("*").strip()
        if not texto.endswith("."):
            CAMBIOS.append(("punto final del pie", "…" + texto[-40:] + " → ."))
            texto += "."
        return texto, indices

    def buscar_pie(desde, clase, max_saltos=4):
        for j in range(desde, min(desde + max_saltos, len(items))):
            it = items[j]
            if it["tipo"] == "p" and it["texto"] and RE_PIE.match(it["texto"]) and RE_PIE.match(it["texto"]).group(3) == clase:
                return j
        return None

    def registrar(texto):
        palabras_orig.extend(palabras_sin_cite(texto))
        stats["citas"] += len(re.findall(r"\\cite\{", texto))

    def emitir_pie(texto, clase):
        # El pie se escribe tal cual (sin el «Pie: » ni los asteriscos de markdown).
        p = b.doc.add_paragraph(style="Pie de figura" if clase == "Figura" else "Pie de tabla")
        from memoria_docx import _anadir_texto_marcado
        _anadir_texto_marcado(p, marcar(texto))

    i = 0
    while i < len(items):
        if i in consumidos:
            i += 1
            continue
        it = items[i]
        if it["tipo"] == "tbl":
            filas = it["filas"]
            j = buscar_pie(i + 1, "Tabla")
            pie, idx = texto_pie(j) if j is not None else ("", [])
            consumidos.update(idx)
            registrar(" ".join(c for f in filas for c in f) + " " + pie)
            b.tabla([marcar(c) for c in filas[0]], [[marcar(c) for c in f] for f in filas[1:]], marcar(pie))
            stats["tablas_word"] += 1
            i += 1
            continue
        t = it["texto"]
        if not t:
            stats["vacios"] += 1
            i += 1
            continue
        m_ph = RE_PLACEHOLDER.match(t)
        if RE_FICHERO.match(t):
            stats["placeholders"] += 1  # linea de fichero suelta de un marcador ya tratado
            i += 1
            continue
        if m_ph and m_ph.group(1) == "FIGURA":
            # Marcador «[FIGURA n.m ...]» en una o dos lineas (la segunda, «Fichero: `figuras/x.svg`]»), despues
            # opcionalmente la imagen incrustada y, por ultimo, el pie.
            stats["placeholders"] += 1
            k = i + 1
            m_f = re.search(r"`figuras/([\w.]+)`", t)
            nombre = m_f.group(1) if m_f else None
            if k < len(items) and items[k]["tipo"] == "p" and RE_FICHERO.match(items[k]["texto"]):
                nombre = RE_FICHERO.match(items[k]["texto"]).group(2)
                consumidos.add(k)
                stats["placeholders"] += 1
                k += 1
            while k < len(items) and items[k]["tipo"] == "p" and not items[k]["texto"] and not items[k]["imagen"]:
                consumidos.add(k)
                stats["vacios"] += 1
                k += 1
            figura = None
            if k < len(items) and items[k]["tipo"] == "p" and items[k]["imagen"]:
                figura = lector.imagen(items[k]["imagen"], tmp)
                consumidos.add(k)
                k += 1
            else:
                base = nombre.rsplit(".", 1)[0] if nombre else None
                for ext in ("jpeg", "png", "jpg"):
                    if base and (FIGURAS / "{0}.{1}".format(base, ext)).exists():
                        figura = FIGURAS / "{0}.{1}".format(base, ext)
                        break
            assert figura is not None, t
            j = buscar_pie(k, "Figura")
            assert j is not None, t
            pie, idx = texto_pie(j)
            consumidos.update(idx)
            registrar(pie)
            b.figura(figura, marcar(pie), ancho_cm=15.0)
            stats["figuras"] += 1
            i += 1
            continue
        if m_ph:
            stats["placeholders"] += 1
            k = i + 1
            while k < len(items) and items[k]["tipo"] == "p" and not items[k]["texto"]:
                consumidos.add(k)
                stats["vacios"] += 1
                k += 1
            if k < len(items) and items[k]["tipo"] == "p" and items[k]["texto"].startswith("|"):
                # Tabla escrita en markdown: filas «| a | b |» hasta la primera linea que no empiece por «|».
                filas = []
                while k < len(items) and items[k]["tipo"] == "p" and (items[k]["texto"].startswith("|") or not items[k]["texto"]):
                    if items[k]["texto"].startswith("|") and not RE_SEPARADOR_MD.match(items[k]["texto"]):
                        filas.append([c.strip() for c in items[k]["texto"].strip("|").split("|")])
                    consumidos.add(k)
                    k += 1
                j = buscar_pie(k, "Tabla")
                pie, idx = texto_pie(j) if j is not None else ("", [])
                consumidos.update(idx)
                registrar(" ".join(c for f in filas for c in f) + " " + pie)
                b.tabla([marcar(c) for c in filas[0]], [[marcar(c) for c in f] for f in filas[1:]], marcar(pie))
                stats["tablas_md"] += 1
            i += 1
            continue
        if it["imagen"]:
            # imagen sin marcador delante
            figura = lector.imagen(it["imagen"], tmp)
            j = buscar_pie(i + 1, "Figura")
            pie, idx = texto_pie(j) if j is not None else ("", [])
            consumidos.update(idx)
            registrar(pie)
            b.figura(figura, marcar(pie), ancho_cm=15.0)
            stats["figuras"] += 1
            i += 1
            continue
        m = RE_CAPITULO.match(t)
        if m and "." not in m.group(2)[:-1]:
            registrar(t)
            b.capitulo(int(m.group(1)), m.group(2).strip())
            stats["titulos"] += 1
            i += 1
            continue
        m = RE_H2.match(t)
        if m and len(t) < 120:
            registrar(m.group(1) + ". " + m.group(2))  # sin el «Capítulo » sobrante
            b.h2(m.group(1) + ". " + m.group(2).strip())
            stats["titulos"] += 1
            i += 1
            continue
        if RE_PIE.match(t):
            # pie suelto (no consumido por una figura o tabla)
            pie, idx = texto_pie(i)
            consumidos.update(idx)
            registrar(pie)
            emitir_pie(pie, RE_PIE.match(t).group(3))
            i += 1
            continue
        registrar(t)
        stats["cursivas"] += t.count("`") // 2 + t.count("‘’")
        stats["negritas"] += t.count("**") // 2
        if it["lista"]:
            estilo = "List Number" if it["lista"] == "decimal" else "List Bullet"
            tm = marcar(t)
            # Vinetas con entradilla («Nombre (ruta): texto»): la entradilla en negrita, como pide la biblia.
            pos = -1
            if estilo == "List Bullet":
                dentro = False
                k = 0
                while k < len(tm) - 1 and k < 80:
                    if tm[k:k + 2] == "//":
                        dentro = not dentro
                        k += 2  # la marca ocupa dos caracteres (y «///» cierra una cursiva seguida de «/»)
                        continue
                    if tm[k] == ":" and not dentro:
                        pos = k
                        break
                    k += 1
            if pos > 0:
                from memoria_docx import _anadir_texto_marcado
                p = b.doc.add_paragraph(style=estilo)
                n0 = len(p.runs)
                _anadir_texto_marcado(p, tm[:pos] + ":")
                for r in p.runs[n0:]:
                    r.bold = True
                _anadir_texto_marcado(p, tm[pos + 1:])
                b.palabras_cuerpo += len(palabras(t))
                stats["entradillas"] += 1
            else:
                b.parrafo(tm, estilo=estilo)
            stats["listas"] += 1
        else:
            b.parrafo(marcar(t))
        i += 1

    b.guardar(salida)

    # Comprobacion: las palabras de la salida son exactamente las del original (en el mismo orden).
    d = Document(str(salida))
    palabras_salida = []
    for hijo in d.element.body.iterchildren():
        tag = hijo.tag.rsplit("}", 1)[-1]
        if tag == "p":
            palabras_salida.extend(palabras(Paragraph(hijo, d).text))
        elif tag == "tbl":
            for fila in Table(hijo, d).rows:
                for celda in fila.cells:
                    palabras_salida.extend(palabras(celda.text))
    if palabras_salida != palabras_orig:
        for k, (a, bb) in enumerate(zip(palabras_orig, palabras_salida)):
            if a != bb:
                raise AssertionError("difiere en la palabra {0}: original {1!r} salida {2!r}".format(k, palabras_orig[k - 3:k + 5], palabras_salida[k - 3:k + 5]))
        raise AssertionError("longitud distinta: {0} frente a {1}".format(len(palabras_orig), len(palabras_salida)))
    return stats, len(palabras_salida)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    tmp = tempfile.mkdtemp(prefix="word_daniel_")
    for origen, salida in DOCUMENTOS:
        assert origen.exists(), origen
        CAMBIOS.clear()
        stats, n = convertir(origen, salida, tmp)
        print("Guardado:", salida, "| palabras:", n, "| identicas al original (tras los ajustes): si")
        print("  formato aplicado:", stats)
        print("  ajustes tipograficos aplicados:", len(CAMBIOS))
        for nombre, contexto in CAMBIOS:
            print("    -", nombre, "::", contexto)
        res = subprocess.run([sys.executable, "-I", "-X", "utf8", str(Path(__file__).with_name("comprobar_borrador_docx.py")), str(salida)],
                             capture_output=True, text=True, encoding="utf-8")
        print(res.stdout.strip())


if __name__ == "__main__":
    main()
