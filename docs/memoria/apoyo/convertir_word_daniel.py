# -*- coding: utf-8 -*-
"""Pasa los Word de Daniel (capitulo 4 y apartados 5.1-5.2) al formato de la biblia y, salvo que se pida lo
contrario, les aplica los cambios de contenido acordados MARCADOS EN ROJO SUBRAYADO.

Lee los dos .docx de `G:\\...\\backup memo\\` en solo lectura y escribe:
  docs/memoria/borradores_docx/cap4_diseno_daniel.docx
  docs/memoria/borradores_docx/cap5_1_2_daniel.docx

Capas, en este orden:
  1. Formato (nunca cambia palabras): titulos escritos como texto a estilos de capitulo y nivel 2; marcadores
     «[FIGURA ...]», «[TABLA ...]», «Fichero: `figuras/...`» y prefijo «Pie: » fuera; pies partidos unidos; imagenes
     incrustadas recolocadas con su pie (la Figura 5.1 se toma de docs/memoria/figuras/); `x` y ‘’x’’ a cursiva,
     **x** a negrita, tablas en markdown a tablas de Word; listas con su tipo y entradilla en negrita; vacios fuera;
     citas LaTeX \\cite{a,b} a [a], [b].
  2. Ajustes tipograficos autorizados por Daniel (caracteres, no gramatica): Figura/Tabla en mayuscula, espacios
     antes de signos, dobles espacios, punto final del pie, video/DASH, dos tildes, una errata. Se registran.
  3. Cambios de contenido (cambios_contenido_daniel.py: C1-C32, D1-D8, E1-E9, erratas y citas), cada uno aplicado
     exactamente una vez y pintado en rojo subrayado; filas nuevas en tablas, enteras en rojo. Con --texto-intacto
     se omite esta capa.
Al final comprueba que la secuencia de palabras del resultado es identica a la del texto tras esas capas (asi
ninguna otra cosa cambia) y pasa el comprobador de la biblia.

Ejecutar desde la raiz del repo:  python docs/memoria/apoyo/convertir_word_daniel.py [--texto-intacto]
"""
from __future__ import annotations

import argparse
import copy
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import RGBColor
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, _anadir_texto_marcado, crear_plantilla  # noqa: E402
from cambios_contenido_daniel import FILAS_NUEVAS, SUSTITUCIONES  # noqa: E402

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
FIGURAS = RAIZ_REPO / "docs" / "memoria" / "figuras"
WORD_DANIEL = Path(r"G:\Otros ordenadores\Mi portátil\backup memo")
DOCUMENTOS = [
    ("cap4", WORD_DANIEL / "Borrador Capitulo 4 Diseño.docx", BORRADORES / "cap4_diseno_daniel.docx"),
    ("cap5", WORD_DANIEL / "hasta 5_2.docx", BORRADORES / "cap5_1_2_daniel.docx"),
]
ROJO = RGBColor(0xC0, 0x00, 0x00)

RE_CAPITULO = re.compile(r"^Capítulo (\d+)\. (.+)$")
RE_H2 = re.compile(r"^(?:Capítulo )?(\d+\.\d+)\. (.+)$")
RE_PLACEHOLDER = re.compile(r"^\**\[(TABLA|FIGURA) (\d+\.\d+)")
RE_FICHERO = re.compile(r"^(Fichero: )?`figuras/([\w.]+)`\]\**$")
RE_PIE = re.compile(r"^\*?(Pie: )?((Figura|Tabla) \d+\.\d+: .*?)\*?$", re.S)
RE_SEPARADOR_MD = re.compile(r"^\|[-| ]+\|$")


def palabras(texto):
    return re.findall(r"\w+", texto)


def quitar_marcas(texto):
    return texto.replace("//", "").replace("**", "").replace("⟦", "").replace("⟧", "")


# --- Capa 2: ajustes tipograficos -----------------------------------------------------------------------------
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
    t = re.sub(r"\\cite\{([^}]*)\}", lambda m: ", ".join("[{0}]".format(k.strip()) for k in m.group(1).split(",")), t)
    return t


# --- Capa 3: cambios de contenido ------------------------------------------------------------------------------
class Cambiador:
    def __init__(self, doc_id, activo):
        self.doc_id = doc_id
        self.activo = activo
        self.reglas = [s for s in SUSTITUCIONES if s[0] == doc_id]
        self.aplicadas = {s[1]: 0 for s in self.reglas}
        self.filas = [f for f in FILAS_NUEVAS if f[0] == doc_id]
        self.filas_aplicadas = {f[1]: 0 for f in self.filas}

    @staticmethod
    def plano(tm):
        """Texto sin marcas //, ** y su mapa de indices plano -> marcado."""
        chars, mapa, i = [], [], 0
        while i < len(tm):
            if tm.startswith("//", i) or tm.startswith("**", i):
                i += 2
                continue
            chars.append(tm[i])
            mapa.append(i)
            i += 1
        return "".join(chars), mapa

    def __call__(self, tm, celda=False):
        if not self.activo:
            return tm
        for regla in self.reglas:
            _, ident, viejo, nuevo = regla[:4]
            exacto = len(regla) > 4 and regla[4] == "exacto"
            plano, mapa = self.plano(tm)
            if exacto:
                if not celda or plano != viejo:
                    continue
                tm = nuevo
                self.aplicadas[ident] += 1
                continue
            pos = plano.find(viejo)
            if pos < 0:
                continue
            assert plano.find(viejo, pos + 1) < 0, "texto original repetido para " + ident
            ini = mapa[pos]
            fin = mapa[pos + len(viejo) - 1] + 1
            tm = tm[:ini] + nuevo + tm[fin:]
            self.aplicadas[ident] += 1
        return tm

    def filas_tras(self, primera_celda_plana):
        return [f for f in self.filas if f[2] == primera_celda_plana] if self.activo else []

    def comprobar(self):
        for ident, n in self.aplicadas.items():
            assert n == 1, "cambio {0!r} aplicado {1} veces".format(ident, n)
        for ident, n in self.filas_aplicadas.items():
            assert n == 1, "fila nueva {0!r} insertada {1} veces".format(ident, n)


def colorear_rojo(doc):
    """Pinta en rojo subrayado el texto entre ⟦ y ⟧ (en parrafos y celdas) y quita las marcas."""
    def parrafos():
        for p in doc.paragraphs:
            yield p
        for t in doc.tables:
            for fila in t.rows:
                for celda in fila.cells:
                    for p in celda.paragraphs:
                        yield p

    def pintar(run):
        run.font.color.rgb = ROJO
        run.font.underline = True

    n = 0
    for p in parrafos():
        if "⟦" not in p.text and "⟧" not in p.text:
            continue
        en_rojo = False
        for run in list(p.runs):
            texto = run.text
            if "⟦" not in texto and "⟧" not in texto:
                if en_rojo:
                    pintar(run)
                continue
            piezas = re.split(r"(⟦|⟧)", texto)
            run.text = piezas[0]
            if en_rojo:
                pintar(run)
            anterior = run
            for pieza in piezas[1:]:
                if pieza == "⟦":
                    en_rojo = True
                    n += 1
                    continue
                if pieza == "⟧":
                    en_rojo = False
                    continue
                if not pieza:
                    continue
                nuevo_r = copy.deepcopy(anterior._r)
                anterior._r.addnext(nuevo_r)
                from docx.text.run import Run
                nuevo = Run(nuevo_r, p)
                nuevo.text = pieza
                nuevo.font.color.rgb = None
                nuevo.font.underline = None
                if en_rojo:
                    pintar(nuevo)
                anterior = nuevo
        assert not en_rojo, "marca de rojo sin cerrar en: " + p.text[:80]
    return n


# --- Lectura del Word ------------------------------------------------------------------------------------------
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


# --- Conversion ------------------------------------------------------------------------------------------------
def convertir(doc_id, origen, salida, tmp, con_cambios):
    lector = Lector(origen)
    items = lector.items
    b = Borrador(PLANTILLA)
    cambiar = Cambiador(doc_id, con_cambios)
    stats = {"placeholders": 0, "pies_unidos": 0, "prefijo_pie": 0, "cursivas": 0, "negritas": 0, "titulos": 0,
             "tablas_md": 0, "tablas_word": 0, "figuras": 0, "vacios": 0, "listas": 0, "citas": 0, "entradillas": 0,
             "filas_nuevas": 0}
    palabras_esperadas = []
    consumidos = set()

    def registrar(tm):
        palabras_esperadas.extend(palabras(quitar_marcas(tm)))

    def texto_pie(i):
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
        return cambiar(marcar(texto)), indices

    def buscar_pie(desde, clase, max_saltos=4):
        for j in range(desde, min(desde + max_saltos, len(items))):
            it = items[j]
            if it["tipo"] == "p" and it["texto"] and RE_PIE.match(it["texto"]) and RE_PIE.match(it["texto"]).group(3) == clase:
                return j
        return None

    def emitir_tabla(filas_crudas, pie):
        filas = [[cambiar(marcar(c), celda=True) for c in f] for f in filas_crudas]
        completas = []
        for f in filas:
            completas.append(f)
            for nueva in cambiar.filas_tras(Cambiador.plano(f[0])[0]):
                completas.append(["⟦" + c + "⟧" for c in nueva[3]])
                cambiar.filas_aplicadas[nueva[1]] += 1
                stats["filas_nuevas"] += 1
        registrar(" ".join(c for f in completas for c in f) + " " + pie)
        b.tabla(completas[0], completas[1:], pie)

    def emitir_pie(texto, clase):
        p = b.doc.add_paragraph(style="Pie de figura" if clase == "Figura" else "Pie de tabla")
        _anadir_texto_marcado(p, texto)

    i = 0
    while i < len(items):
        if i in consumidos:
            i += 1
            continue
        it = items[i]
        if it["tipo"] == "tbl":
            j = buscar_pie(i + 1, "Tabla")
            pie, idx = texto_pie(j) if j is not None else ("", [])
            consumidos.update(idx)
            emitir_tabla(it["filas"], pie)
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
            stats["placeholders"] += 1
            i += 1
            continue
        if m_ph and m_ph.group(1) == "FIGURA":
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
            b.figura(figura, pie, ancho_cm=15.0)
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
                filas = []
                while k < len(items) and items[k]["tipo"] == "p" and (items[k]["texto"].startswith("|") or not items[k]["texto"]):
                    if items[k]["texto"].startswith("|") and not RE_SEPARADOR_MD.match(items[k]["texto"]):
                        filas.append([c.strip() for c in items[k]["texto"].strip("|").split("|")])
                    consumidos.add(k)
                    k += 1
                j = buscar_pie(k, "Tabla")
                pie, idx = texto_pie(j) if j is not None else ("", [])
                consumidos.update(idx)
                emitir_tabla(filas, pie)
                stats["tablas_md"] += 1
            i += 1
            continue
        if it["imagen"]:
            figura = lector.imagen(it["imagen"], tmp)
            j = buscar_pie(i + 1, "Figura")
            pie, idx = texto_pie(j) if j is not None else ("", [])
            consumidos.update(idx)
            registrar(pie)
            b.figura(figura, pie, ancho_cm=15.0)
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
            registrar(m.group(1) + ". " + m.group(2))
            b.h2(m.group(1) + ". " + m.group(2).strip())
            stats["titulos"] += 1
            i += 1
            continue
        if RE_PIE.match(t):
            pie, idx = texto_pie(i)
            consumidos.update(idx)
            registrar(pie)
            emitir_pie(pie, RE_PIE.match(t).group(3))
            i += 1
            continue
        stats["cursivas"] += t.count("`") // 2 + t.count("‘’")
        stats["negritas"] += t.count("**") // 2
        stats["citas"] += len(re.findall(r"\\cite\{", t))
        tm = cambiar(marcar(t))
        registrar(tm)
        if it["lista"]:
            estilo = "List Number" if it["lista"] == "decimal" else "List Bullet"
            pos = -1
            if estilo == "List Bullet":
                dentro = False
                k = 0
                while k < len(tm) - 1 and k < 80:
                    if tm[k:k + 2] == "//":
                        dentro = not dentro
                        k += 2
                        continue
                    if tm[k] == ":" and not dentro:
                        pos = k
                        break
                    k += 1
            if pos > 0:
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
            b.parrafo(tm)
        i += 1

    cambiar.comprobar()
    n_rojo = colorear_rojo(b.doc)
    b.guardar(salida)

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
    if palabras_salida != palabras_esperadas:
        for k, (a, bb) in enumerate(zip(palabras_esperadas, palabras_salida)):
            if a != bb:
                raise AssertionError("difiere en la palabra {0}: esperado {1!r} salida {2!r}".format(
                    k, palabras_esperadas[k - 3:k + 5], palabras_salida[k - 3:k + 5]))
        raise AssertionError("longitud distinta: {0} frente a {1}".format(len(palabras_esperadas), len(palabras_salida)))
    stats["tramos_en_rojo"] = n_rojo
    stats["cambios_contenido"] = sum(cambiar.aplicadas.values())
    return stats, len(palabras_salida)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--texto-intacto", action="store_true", help="solo formato y ajustes, sin los cambios de contenido")
    args = ap.parse_args()
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    tmp = tempfile.mkdtemp(prefix="word_daniel_")
    for doc_id, origen, salida in DOCUMENTOS:
        assert origen.exists(), origen
        CAMBIOS.clear()
        stats, n = convertir(doc_id, origen, salida, tmp, not args.texto_intacto)
        print("Guardado:", salida, "| palabras:", n, "| identicas al texto tras las capas: si")
        print("  formato y cambios:", stats)
        print("  ajustes tipograficos aplicados:", len(CAMBIOS))
        for nombre, contexto in CAMBIOS:
            print("    -", nombre, "::", contexto)
        res = subprocess.run([sys.executable, "-I", "-X", "utf8", str(Path(__file__).with_name("comprobar_borrador_docx.py")), str(salida)],
                             capture_output=True, text=True, encoding="utf-8")
        print(res.stdout.strip())


if __name__ == "__main__":
    main()
