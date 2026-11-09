# -*- coding: utf-8 -*-
"""Plantilla y utilidades para generar los borradores .docx de la memoria.

Sigue la biblia de formato (docs/memoria/05_BIBLIA_FORMATO_TFG_UGR.md, apartado 2):
A4, margenes de 2,5 cm, cuerpo Arial 12 justificado con sangria de primera linea,
interlineado 1,15; "Capitulo N" en Arial 24 regular y titulo en Arial negrita 26;
nivel 2 "N.M. Titulo" en Arial negrita 18; nivel 3 en Arial negrita 12; pies de
figura y tabla centrados en Arial 9 ("Figura 5.2: Texto."); tablas nativas con
cabecera en negrita a 10 pt; codigo en Consolas 10 con pie "Listado N.M: Texto.";
ecuaciones del editor de Word centradas y numeradas "(N.M)" a la derecha; numero
de pagina centrado al pie.

Uso:
    from memoria_docx import crear_plantilla, Borrador
    crear_plantilla("docs/memoria/plantilla/plantilla_memoria_ugr.docx")
    b = Borrador("docs/memoria/plantilla/plantilla_memoria_ugr.docx")
    b.h2("5.3. Titulo")
    b.parrafo("Texto con //cursiva// y cita [clave_bib].")
    b.guardar("docs/memoria/borradores_docx/cap5_3_x.docx")

Marcas de texto: //texto// pasa a cursiva; **texto** a negrita (solo entradillas); V~r~ pone r como subindice.
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Cm, Pt, RGBColor

FUENTE = "Arial"
FUENTE_CODIGO = "Consolas"
NEGRO = RGBColor(0, 0, 0)
ANCHO_TEXTO_CM = 21.0 - 2 * 2.5  # 16 cm


def _fijar_fuente(estilo, nombre, tamano_pt, negrita=None, cursiva=None, color=NEGRO):
    fuente = estilo.font
    fuente.name = nombre
    fuente.size = Pt(tamano_pt)
    if negrita is not None:
        fuente.bold = negrita
    if cursiva is not None:
        fuente.italic = cursiva
    if color is not None:
        fuente.color.rgb = color
    rpr = estilo.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for atributo in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(atributo), nombre)
    for atributo in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rfonts.get(qn(atributo)) is not None:
            del rfonts.attrib[qn(atributo)]


def _fijar_parrafo(estilo, alineacion=None, antes=None, despues=None, interlineado=None,
                   sangria_primera=None, sangria_izq=None, mantener_siguiente=None,
                   salto_pagina_antes=None):
    pf = estilo.paragraph_format
    if alineacion is not None:
        pf.alignment = alineacion
    if antes is not None:
        pf.space_before = Pt(antes)
    if despues is not None:
        pf.space_after = Pt(despues)
    if interlineado is not None:
        pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
        pf.line_spacing = interlineado
    if sangria_primera is not None:
        pf.first_line_indent = Cm(sangria_primera)
    if sangria_izq is not None:
        pf.left_indent = Cm(sangria_izq)
    if mantener_siguiente is not None:
        pf.keep_with_next = mantener_siguiente
    if salto_pagina_antes is not None:
        pf.page_break_before = salto_pagina_antes


def _estilo(doc, nombre, tipo=WD_STYLE_TYPE.PARAGRAPH, base=None):
    estilos = doc.styles
    try:
        estilo = estilos[nombre]
    except KeyError:
        estilo = estilos.add_style(nombre, tipo)
    if base is not None:
        estilo.base_style = estilos[base]
    estilo.quick_style = True
    return estilo


def _pie_con_numero_de_pagina(seccion):
    pie = seccion.footer
    parrafo = pie.paragraphs[0] if pie.paragraphs else pie.add_paragraph()
    parrafo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    parrafo.paragraph_format.first_line_indent = Cm(0)
    run = parrafo.add_run()
    for tipo, texto in (("begin", None), (None, "PAGE"), ("end", None)):
        if tipo:
            fld = OxmlElement("w:fldChar")
            fld.set(qn("w:fldCharType"), tipo)
            run._r.append(fld)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = texto
            run._r.append(instr)
    run.font.name = FUENTE
    run.font.size = Pt(10)


def crear_plantilla(ruta_salida):
    """Crea la plantilla .docx con los estilos de la biblia."""
    doc = Document()

    # Pagina A4 y margenes de 2,5 cm.
    for seccion in doc.sections:
        seccion.orientation = WD_ORIENT.PORTRAIT
        seccion.page_width = Cm(21.0)
        seccion.page_height = Cm(29.7)
        seccion.left_margin = seccion.right_margin = Cm(2.5)
        seccion.top_margin = seccion.bottom_margin = Cm(2.5)
        seccion.footer_distance = Cm(1.25)
        _pie_con_numero_de_pagina(seccion)

    # Cuerpo.
    normal = doc.styles["Normal"]
    _fijar_fuente(normal, FUENTE, 12)
    _fijar_parrafo(normal, WD_ALIGN_PARAGRAPH.JUSTIFY, antes=0, despues=6, interlineado=1.15,
                   sangria_primera=0.75)

    # "Capitulo N" (linea propia, Arial 24 regular) y titulo del capitulo (Heading 1, 26 negrita).
    cap_num = _estilo(doc, "Capitulo numero", base="Normal")
    _fijar_fuente(cap_num, FUENTE, 24, negrita=False)
    _fijar_parrafo(cap_num, WD_ALIGN_PARAGRAPH.LEFT, antes=72, despues=6, interlineado=1.0,
                   sangria_primera=0, mantener_siguiente=True, salto_pagina_antes=True)

    h1 = doc.styles["Heading 1"]
    _fijar_fuente(h1, FUENTE, 26, negrita=True)
    _fijar_parrafo(h1, WD_ALIGN_PARAGRAPH.LEFT, antes=0, despues=36, interlineado=1.0,
                   sangria_primera=0, mantener_siguiente=True, salto_pagina_antes=False)

    h2 = doc.styles["Heading 2"]
    _fijar_fuente(h2, FUENTE, 18, negrita=True)
    _fijar_parrafo(h2, WD_ALIGN_PARAGRAPH.LEFT, antes=24, despues=12, interlineado=1.0,
                   sangria_primera=0, mantener_siguiente=True)

    h3 = doc.styles["Heading 3"]
    _fijar_fuente(h3, FUENTE, 12, negrita=True)
    _fijar_parrafo(h3, WD_ALIGN_PARAGRAPH.LEFT, antes=18, despues=6, interlineado=1.0,
                   sangria_primera=0, mantener_siguiente=True)

    # Pies de figura y tabla (Arial 9, centrados).
    pie = doc.styles["Caption"]
    _fijar_fuente(pie, FUENTE, 9, negrita=False, cursiva=False)
    _fijar_parrafo(pie, WD_ALIGN_PARAGRAPH.CENTER, antes=6, despues=12, interlineado=1.0,
                   sangria_primera=0)
    pie_fig = _estilo(doc, "Pie de figura", base="Caption")
    pie_tab = _estilo(doc, "Pie de tabla", base="Caption")
    _fijar_parrafo(pie_tab, antes=6, despues=12)

    # Parrafo que contiene una figura (centrado, sin sangria).
    fig = _estilo(doc, "Figura", base="Normal")
    _fijar_parrafo(fig, WD_ALIGN_PARAGRAPH.CENTER, antes=12, despues=0, sangria_primera=0,
                   mantener_siguiente=True)

    # Texto de tabla (10 pt) y cabecera (negrita).
    tab_txt = _estilo(doc, "Tabla texto", base="Normal")
    _fijar_fuente(tab_txt, FUENTE, 10)
    _fijar_parrafo(tab_txt, WD_ALIGN_PARAGRAPH.LEFT, antes=2, despues=2, interlineado=1.0,
                   sangria_primera=0)
    tab_cab = _estilo(doc, "Tabla cabecera", base="Tabla texto")
    _fijar_fuente(tab_cab, FUENTE, 10, negrita=True)

    # Codigo (Consolas 10) y su pie.
    cod = _estilo(doc, "Codigo", base="Normal")
    _fijar_fuente(cod, FUENTE_CODIGO, 10)
    _fijar_parrafo(cod, WD_ALIGN_PARAGRAPH.LEFT, antes=0, despues=0, interlineado=1.0,
                   sangria_primera=0, sangria_izq=0.75, mantener_siguiente=True)
    _estilo(doc, "Pie de listado", base="Caption")

    # Ecuacion: centrada con el numero a la derecha (tabulador).
    ecu = _estilo(doc, "Ecuacion", base="Normal")
    _fijar_parrafo(ecu, WD_ALIGN_PARAGRAPH.LEFT, antes=6, despues=6, interlineado=1.0,
                   sangria_primera=0)
    ecu.paragraph_format.tab_stops.add_tab_stop(Cm(ANCHO_TEXTO_CM / 2), WD_TAB_ALIGNMENT.CENTER)
    ecu.paragraph_format.tab_stops.add_tab_stop(Cm(ANCHO_TEXTO_CM), WD_TAB_ALIGNMENT.RIGHT)

    # Lista con entradilla en negrita.
    lista = doc.styles["List Bullet"]
    _fijar_fuente(lista, FUENTE, 12)
    _fijar_parrafo(lista, WD_ALIGN_PARAGRAPH.JUSTIFY, antes=0, despues=6, interlineado=1.15,
                   sangria_primera=0)

    # Caracter: cursiva para anglicismos, identificadores y ficheros.
    cur = _estilo(doc, "Identificador", tipo=WD_STYLE_TYPE.CHARACTER)
    cur.font.italic = True

    # Quitar el parrafo vacio inicial y guardar.
    cuerpo = doc.element.body
    for p in list(cuerpo.findall(qn("w:p"))):
        cuerpo.remove(p)
    Path(ruta_salida).parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(ruta_salida))
    return ruta_salida


_MARCAS = re.compile(r"(\*\*.+?\*\*|//.+?//|~[^~\s]+~)")


def _anadir_texto_marcado(parrafo, texto, tamano=None):
    for trozo in _MARCAS.split(texto):
        if not trozo:
            continue
        if trozo.startswith("**") and trozo.endswith("**"):
            run = parrafo.add_run(trozo[2:-2])
            run.bold = True
        elif trozo.startswith("//") and trozo.endswith("//"):
            run = parrafo.add_run(trozo[2:-2])
            run.italic = True
        elif trozo.startswith("~") and trozo.endswith("~"):
            run = parrafo.add_run(trozo[1:-1])
            run.font.subscript = True
        else:
            run = parrafo.add_run(trozo)
        if tamano is not None:
            run.font.size = Pt(tamano)


class Borrador:
    def __init__(self, ruta_plantilla):
        self.doc = Document(str(ruta_plantilla))
        self.palabras_cuerpo = 0

    # Titulos -------------------------------------------------------------
    def capitulo(self, numero, titulo):
        self.doc.add_paragraph("Capítulo {0}".format(numero), style="Capitulo numero")
        self.doc.add_paragraph(titulo, style="Heading 1")

    def h2(self, texto):
        self.doc.add_paragraph(texto, style="Heading 2")

    def h3(self, texto):
        self.doc.add_paragraph(texto, style="Heading 3")

    # Cuerpo --------------------------------------------------------------
    def parrafo(self, texto, estilo="Normal"):
        p = self.doc.add_paragraph(style=estilo)
        _anadir_texto_marcado(p, texto)
        self.palabras_cuerpo += len(re.findall(r"\w+", texto))
        return p

    def lista(self, items):
        """items: lista de (entradilla, texto). Entradilla en negrita con dos puntos."""
        for entradilla, texto in items:
            p = self.doc.add_paragraph(style="List Bullet")
            run = p.add_run(entradilla.rstrip(":") + ":")
            run.bold = True
            _anadir_texto_marcado(p, " " + texto)
            self.palabras_cuerpo += len(re.findall(r"\w+", entradilla + " " + texto))

    # Objetos -------------------------------------------------------------
    def figura(self, ruta_imagen, pie, ancho_cm=15.0):
        p = self.doc.add_paragraph(style="Figura")
        p.add_run().add_picture(str(ruta_imagen), width=Cm(ancho_cm))
        pf = self.doc.add_paragraph(style="Pie de figura")
        _anadir_texto_marcado(pf, pie)

    def tabla(self, cabecera, filas, pie, anchos_cm=None, alineaciones=None):
        tabla = self.doc.add_table(rows=1, cols=len(cabecera))
        tabla.style = self.doc.styles["Table Grid"]
        tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
        if anchos_cm is None:
            anchos_cm = [ANCHO_TEXTO_CM / len(cabecera)] * len(cabecera)
        for i, texto in enumerate(cabecera):
            celda = tabla.rows[0].cells[i]
            celda.width = Cm(anchos_cm[i])
            celda.paragraphs[0].style = self.doc.styles["Tabla cabecera"]
            _anadir_texto_marcado(celda.paragraphs[0], texto)
            self._sombrear(celda, "E7E6E6")
        for fila in filas:
            celdas = tabla.add_row().cells
            for i, texto in enumerate(fila):
                celdas[i].width = Cm(anchos_cm[i])
                p = celdas[i].paragraphs[0]
                p.style = self.doc.styles["Tabla texto"]
                if alineaciones and alineaciones[i] == "c":
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                elif alineaciones and alineaciones[i] == "r":
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                _anadir_texto_marcado(p, str(texto))
        # Repetir la cabecera si la tabla salta de pagina y no dejar la cabecera sola al pie.
        for fila in tabla.rows[:-1]:
            for celda in fila.cells:
                for p in celda.paragraphs:
                    p.paragraph_format.keep_with_next = True
            trpr_fila = fila._tr.get_or_add_trPr()
            cant = OxmlElement("w:cantSplit")
            cant.set(qn("w:val"), "true")
            trpr_fila.append(cant)
        trpr = tabla.rows[0]._tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader")
        th.set(qn("w:val"), "true")
        trpr.append(th)
        pt = self.doc.add_paragraph(style="Pie de tabla")
        _anadir_texto_marcado(pt, pie)
        return tabla

    @staticmethod
    def _sombrear(celda, color_hex):
        tcpr = celda._tc.get_or_add_tcPr()
        shd = parse_xml('<w:shd {0} w:val="clear" w:color="auto" w:fill="{1}"/>'.format(nsdecls("w"), color_hex))
        tcpr.append(shd)

    def codigo(self, lineas, pie):
        for linea in lineas:
            p = self.doc.add_paragraph(style="Codigo")
            p.add_run(linea)
        pl = self.doc.add_paragraph(style="Pie de listado")
        _anadir_texto_marcado(pl, pie)

    def ecuacion(self, omml_xml, numero):
        """omml_xml: contenido de <m:oMath>...</m:oMath> (sin el envoltorio oMathPara)."""
        p = self.doc.add_paragraph(style="Ecuacion")
        p.add_run("\t")
        omath = parse_xml(
            '<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
            'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">{0}</m:oMath>'.format(omml_xml)
        )
        p._p.append(omath)
        p.add_run("\t({0})".format(numero))
        return p

    def guardar(self, ruta):
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        self.doc.save(str(ruta))
        return ruta


# Ayudas OMML ----------------------------------------------------------------
def m_r(texto, cursiva=True):
    estilo = "" if cursiva else '<m:rPr><m:sty m:val="p"/></m:rPr>'
    return "<m:r>{0}<m:t xml:space=\"preserve\">{1}</m:t></m:r>".format(estilo, texto)


def m_f(num, den):
    return "<m:f><m:num>{0}</m:num><m:den>{1}</m:den></m:f>".format(num, den)


def m_sub(base, sub):
    return "<m:sSub><m:e>{0}</m:e><m:sub>{1}</m:sub></m:sSub>".format(base, sub)


def m_func(nombre, arg):
    return ("<m:func><m:fName>{0}</m:fName><m:e>{1}</m:e></m:func>"
            .format(m_r(nombre, cursiva=False), arg))


def m_d(contenido, abre="(", cierra=")"):
    return ('<m:d><m:dPr><m:begChr m:val="{0}"/><m:endChr m:val="{1}"/></m:dPr><m:e>{2}</m:e></m:d>'
            .format(abre, cierra, contenido))
