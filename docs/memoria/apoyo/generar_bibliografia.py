# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/bibliografia.docx: la lista de referencias impresa, SOLO con lo citado,
numerada por orden de primera aparicion en la memoria (biblia §4: IEEE/unsrt), y el mapa clave -> numero en
docs/memoria/apoyo/bibliografia_numeracion.json para convertir las citas [clave] en [n] al maquetar.

Orden de lectura = orden de la memoria: resumen, cap 1, cap 2, cap 3, cap 4 (Word de Daniel, solo lectura),
5.1-5.2 (Word de Daniel, solo lectura), 5.3-5.8, cap 6, cap 7, anexos. Las citas se buscan como [clave] o
[clave1], [clave2] en parrafos y tablas, en el orden real del documento.

Formato de cada entrada: el de unsrt (autores con iniciales, titulo, revista o congreso en cursiva, volumen(numero):
paginas, ano) con los conectores en castellano, DOI cuando existe y, para las webs, «[En linea]. Disponible en: URL.
[Ultimo acceso: mes de ano]» (biblia §4). Se comprueba por programa que ninguna URL lleva parametros de seguimiento y
que los meses de acceso estan en castellano.

Ejecutar desde la raiz del repo:  python docs/memoria/apoyo/generar_bibliografia.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt
from docx.table import Table
from docx.text.paragraph import Paragraph

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"
SALIDA = BORRADORES / "bibliografia.docx"
SALIDA_JSON = RAIZ_REPO / "docs" / "memoria" / "apoyo" / "bibliografia_numeracion.json"

WORD_DANIEL = Path(r"G:\Otros ordenadores\Mi portátil\backup memo")
ORDEN = [
    BORRADORES / "resumen_abstract.docx",
    BORRADORES / "cap1_introduccion.docx",
    BORRADORES / "cap2_1_2_has_dash.docx",
    BORRADORES / "cap2_3_4_problema_familias.docx",
    BORRADORES / "cap2_5_7_qoe_reproductores_lagunas.docx",
    BORRADORES / "cap3_planificacion_costes.docx",
    BORRADORES / "cap4_diseno_daniel.docx",  # conversion al formato de la biblia de los Word de Daniel
    BORRADORES / "cap5_1_2_daniel.docx",      # (apoyo/convertir_word_daniel.py), con sus citas como [clave]
    BORRADORES / "cap5_3_analizador_mpd.docx",
    BORRADORES / "cap5_4_ejecutor_configuracion.docx",
    BORRADORES / "cap5_5_controladores_clasicos.docx",
    BORRADORES / "cap5_6_controlador_propio.docx",
    BORRADORES / "cap5_7_entorno_entrenamiento.docx",
    BORRADORES / "cap5_8_resumen_capitulo5.docx",
    BORRADORES / "cap6_1_diseno_experimento.docx",
    BORRADORES / "cap6_2_metricas_hipotesis.docx",
    BORRADORES / "cap6_3_integridad_verificacion.docx",
    BORRADORES / "cap6_4_resultados_hipotesis.docx",
    BORRADORES / "cap6_5_descriptivos.docx",
    BORRADORES / "cap6_6_exploratorio.docx",
    BORRADORES / "cap6_7_interpretacion_cierre.docx",
    BORRADORES / "cap7_conclusiones.docx",
    BORRADORES / "anexos.docx",
]
MESES = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
         "noviembre", "diciembre")


# --- BibTeX ----------------------------------------------------------------------------------------------
def leer_bib(ruta):
    texto = ruta.read_text(encoding="utf-8")
    entradas = {}
    for bloque in re.split(r"\n(?=@)", texto):
        m = re.match(r"@(\w+)\{([^,]+),", bloque)
        if not m:
            continue
        tipo, clave = m.group(1).lower(), m.group(2).strip()
        campos = {}
        for cm in re.finditer(r"^\s*(\w+)\s*=\s*\{(.*)\},?\s*$", bloque, re.M):
            campos[cm.group(1).lower()] = cm.group(2).strip()
        campos["_tipo"] = tipo
        entradas[clave] = campos
    return entradas


ACENTOS = {"'": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú"},
           '"': {"a": "ä", "e": "ë", "i": "ï", "o": "ö", "u": "ü", "O": "Ö", "U": "Ü"},
           "~": {"n": "ñ", "N": "Ñ"}, "`": {"a": "à", "e": "è"}, "^": {"a": "â", "e": "ê"}, "c": {"c": "ç", "C": "Ç"}, "u": {"g": "ğ", "G": "Ğ"},
           "v": {"c": "č", "s": "š", "z": "ž", "C": "Č", "S": "Š", "Z": "Ž", "r": "ř"}}
LETRAS = {"\\ss": "ß", "\\o": "ø", "\\O": "Ø", "\\ae": "æ", "\\i": "ı", "\\l": "ł", "\\L": "Ł", "\\aa": "å"}


def limpiar(texto):
    """Pasa el LaTeX del .bib a texto plano."""
    t = texto
    t = re.sub(r"\\url\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\(texttt|textit|textbf|emph|textrm)\{([^}]*)\}", r"\2", t)
    for marca, mapa in ACENTOS.items():
        for letra, res in mapa.items():
            t = t.replace("{\\" + marca + letra + "}", res).replace("\\" + marca + "{" + letra + "}", res)
            t = t.replace("\\" + marca + letra, res)
    for cmd, res in LETRAS.items():
        t = t.replace("{" + cmd + "}", res).replace(cmd + " ", res).replace(cmd, res)
    t = t.replace("\\&", "&").replace("\\_", "_").replace("\\,", " ").replace("\\%", "%")
    t = re.sub(r"(?<![/\w])~", " ", t)  # espacio duro de BibTeX; la virgulilla de una URL se conserva
    t = t.replace("---", " – ").replace("--", "–")
    t = t.replace("{", "").replace("}", "")
    t = re.sub(r"\s+", " ", t).strip()
    assert "\\" not in t, t
    return t


def autores(campo):
    partes = [p.strip() for p in re.split(r"\s+and\s+", campo)]
    nombres = []
    for p in partes:
        if p.startswith("{") and p.endswith("}"):
            nombres.append(limpiar(p))
            continue
        if "," in p:
            apellido, nombre = [x.strip() for x in p.split(",", 1)]
        else:
            trozos = p.split()
            apellido, nombre = trozos[-1], " ".join(trozos[:-1])
        iniciales = " ".join(
            "-".join(s[0] + "." for s in token.split("-") if s) for token in limpiar(nombre).split() if token)
        nombres.append((iniciales + " " + limpiar(apellido)).strip())
    if len(nombres) == 1:
        return nombres[0]
    return ", ".join(nombres[:-1]) + " y " + nombres[-1]


def acceso(nota):
    if not nota:
        return None, nota
    m = re.search(r"Accedido:\s*([a-záéíóú]+) de (\d{4})\.?", nota)
    if not m:
        return None, nota
    mes = m.group(1).lower()
    assert mes in MESES, nota
    resto = (nota[:m.start()] + nota[m.end():]).strip().rstrip(".").strip()
    return "{0} de {1}".format(mes, m.group(2)), resto


def url_de(e):
    hp = e.get("howpublished", "")
    m = re.search(r"\\url\{([^}]*)\}", hp)
    if m:
        return m.group(1), limpiar(re.sub(r",?\s*\\url\{[^}]*\}", "", hp)).strip().rstrip(",")
    return None, limpiar(hp) if hp else ""


def formatear(e):
    """Devuelve el texto de la entrada con //cursiva// para revistas, congresos y titulos de libros/webs."""
    tipo = e["_tipo"]
    aut = autores(e["author"])
    tit = limpiar(e["title"])
    doi = e.get("doi")
    url = e.get("url")
    if doi and url and url.lower().startswith("https://doi.org/"):
        url = None  # la URL es el propio DOI
    partes = [aut if aut.endswith(".") else aut + ".", tit if tit.endswith((".", "?")) else tit + "."]
    if tipo == "article":
        rev = "//" + limpiar(e["journal"]) + "//"
        vol = e.get("volume", "")
        num = e.get("number")
        pag = limpiar(e["pages"]) if e.get("pages") else ""
        cuerpo = rev
        if vol:
            cuerpo += ", " + vol + ("({0})".format(num) if num else "") + (":" + pag if pag else "")
        elif pag:
            cuerpo += ", páginas " + pag
        cuerpo += ", " + e["year"] + "."
        partes.append(cuerpo)
    elif tipo == "inproceedings":
        cuerpo = "En //" + limpiar(e["booktitle"]) + "//"
        if e.get("pages"):
            cuerpo += ", páginas " + limpiar(e["pages"])
        cuerpo += ". "
        if e.get("publisher"):
            cuerpo += limpiar(e["publisher"]) + ", "
        cuerpo += e["year"] + "."
        partes.append(cuerpo)
    elif tipo == "book":
        partes[1] = "//" + tit + "//."
        cuerpo = ""
        if e.get("series"):
            cuerpo += limpiar(e["series"]) + (", n.º " + e["number"] if e.get("number") else "") + ". "
        cuerpo += limpiar(e["publisher"]) + (", " + limpiar(e["address"]) if e.get("address") else "") + ", " + e["year"] + "."
        if e.get("isbn"):
            cuerpo += " ISBN " + e["isbn"] + "."
        partes.append(cuerpo)
    elif tipo == "techreport":
        cuerpo = limpiar(e.get("type", "Informe técnico"))
        if e.get("edition"):
            cuerpo += ", {0}.ª edición".format(e["edition"])
        cuerpo += ". " + limpiar(e["institution"]) + (", " + limpiar(e["address"]) if e.get("address") else "")
        cuerpo += ", " + e["year"] + "."
        partes.append(cuerpo)
    elif tipo == "misc":
        url_hp, texto_hp = url_de(e)
        url = url or url_hp
        fecha, resto_nota = acceso(limpiar(e.get("note", "")) if e.get("note") else "")
        cuerpo = ""
        if texto_hp:
            cuerpo += texto_hp + ("" if texto_hp.endswith(".") else ".") + " "
        if resto_nota:
            cuerpo += resto_nota + ". "
        if e.get("year") and e["year"] not in resto_nota:
            cuerpo += e["year"] + ". "
        if doi:
            cuerpo += "DOI: " + doi + ". "
        if url:
            cuerpo += "[En línea]. Disponible en: " + url + "."
            if fecha:
                cuerpo += " [Último acceso: " + fecha + "]."
        partes.append(cuerpo.strip())
        return " ".join(partes)
    else:
        raise ValueError(tipo)
    # Notas que apuntan al dataset asociado se imprimen; las notas de trabajo, no.
    nota = limpiar(e.get("note", "")) if e.get("note") else ""
    if nota and nota.startswith("Dataset"):
        partes.append(nota.rstrip(".") + ".")
    if doi:
        partes.append("DOI: " + doi + ".")
    elif url:
        partes.append("[En línea]. Disponible en: " + url + ".")
    return " ".join(partes)


# --- Citas en orden -------------------------------------------------------------------------------------
def texto_en_orden(ruta):
    """Texto del documento en el orden real del cuerpo (parrafos y tablas intercalados)."""
    doc = Document(str(ruta))
    trozos = []
    for hijo in doc.element.body.iterchildren():
        tag = hijo.tag.rsplit("}", 1)[-1]
        if tag == "p":
            trozos.append(Paragraph(hijo, doc).text)
        elif tag == "tbl":
            for fila in Table(hijo, doc).rows:
                for celda in fila.cells:
                    trozos.append(celda.text)
    return "\n".join(trozos)


def citas_en_orden(claves_bib):
    orden = []
    por_doc = {}
    leidos = []
    for ruta in ORDEN:
        if not ruta.exists():
            print("AVISO: no existe", ruta)
            continue
        leidos.append(ruta.name)
        t = texto_en_orden(ruta)
        encontradas = []
        # Citas como [clave] o [clave1], [clave2] (borradores) y como \cite{clave} o \cite{a,b} (Word de Daniel).
        for m in re.finditer(r"\[([^\[\]]+)\]|\\cite\{([^}]*)\}", t):
            for k in re.split(r"[,;]\s*", m.group(1) or m.group(2)):
                k = k.strip()
                if k in claves_bib:
                    encontradas.append(k)
                    if k not in orden:
                        orden.append(k)
                elif re.match(r"^[A-Za-z]\w*\d{4}\w*$", k):
                    raise AssertionError("cita fuera del .bib en {0}: {1}".format(ruta.name, k))
        por_doc[ruta.name] = encontradas
    return orden, por_doc, leidos


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    entradas = leer_bib(BIB)
    assert len(entradas) == 96, len(entradas)
    orden, por_doc, leidos = citas_en_orden(set(entradas))
    numero = {k: i + 1 for i, k in enumerate(orden)}

    # Comprobaciones de la biblia sobre las entradas que se imprimen.
    for k in orden:
        e = entradas[k]
        for campo in ("url", "howpublished"):
            if e.get(campo):
                u = e[campo]
                assert "utm_" not in u and "?ref" not in u and "&" not in u.replace("\\&", ""), (k, u)
        if e.get("note") and "Accedido" in e["note"]:
            m = re.search(r"Accedido:\s*(\w+)", e["note"])
            assert m and m.group(1).lower() in MESES, (k, e["note"])
        assert e.get("author") and e.get("title"), k
        if e["_tipo"] != "misc" or e.get("year"):
            assert e.get("year"), k

    b = Borrador(PLANTILLA)
    doc = b.doc
    # Estilo propio: cuerpo con sangria francesa, sin sangria de primera linea, para que el comprobador lo
    # distinga del texto normal (los DOI llevan puntos).
    est = doc.styles.add_style("Bibliografia", WD_STYLE_TYPE.PARAGRAPH)
    est.base_style = doc.styles["Normal"]
    est.paragraph_format.left_indent = Cm(1.0)
    est.paragraph_format.first_line_indent = Cm(-1.0)
    est.paragraph_format.space_after = Pt(6)
    est.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT  # las URL largas dejan huecos si se justifica
    est.font.size = Pt(11)
    doc.add_paragraph("Bibliografía", style="Heading 1")
    textos = {}
    for k in orden:
        texto = formatear(entradas[k])
        textos[k] = texto
        b.parrafo("[{0}] ".format(numero[k]) + texto, estilo="Bibliografia")
    b.guardar(SALIDA)

    no_citadas = sorted(set(entradas) - set(orden))
    SALIDA_JSON.write_text(json.dumps({
        "generado_desde": leidos,
        "numero_por_clave": numero,
        "primera_aparicion": {k: next(n for n, cs in por_doc.items() if k in cs) for k in orden},
        "citas_por_documento": {n: len(cs) for n, cs in por_doc.items()},
        "no_citadas_no_impresas": no_citadas,
        "texto_impreso": textos,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Guardado:", SALIDA)
    print("entradas impresas:", len(orden), "| no citadas (no se imprimen):", len(no_citadas))
    print("citas por documento:", {n: len(cs) for n, cs in por_doc.items()})
    for k in orden:
        print("[{0}] {1}".format(numero[k], textos[k]).encode("ascii", "replace").decode())


if __name__ == "__main__":
    main()
