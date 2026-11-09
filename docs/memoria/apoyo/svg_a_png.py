# -*- coding: utf-8 -*-
"""Convierte un SVG a PNG con Microsoft Word (COM) y PyMuPDF.

Word importa el SVG con sus fuentes (Arial) y lo exporta a PDF en una pagina del tamano exacto
de la figura; PyMuPDF rasteriza esa pagina. Asi el PNG es fiel a lo que vera Word.

Uso: python docs/memoria/apoyo/svg_a_png.py figura.svg [salida.png] [dpi]
"""
import re
import sys
import tempfile
from pathlib import Path

import pymupdf
import win32com.client


def tamano_svg(ruta):
    texto = Path(ruta).read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([\d.\s-]+)"', texto)
    if vb:
        _, _, w, h = [float(x) for x in vb.group(1).split()]
        return w, h
    w = float(re.search(r'width="([\d.]+)', texto).group(1))
    h = float(re.search(r'height="([\d.]+)', texto).group(1))
    return w, h


def main():
    entrada = Path(sys.argv[1]).resolve()
    salida = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else entrada.with_suffix(".png")
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 220
    ancho_px, alto_px = tamano_svg(entrada)
    # 1 px del SVG = 0,75 pt (96 ppp).
    ancho_pt, alto_pt = ancho_px * 0.75, alto_px * 0.75

    pdf = Path(tempfile.gettempdir()) / (entrada.stem + "_svg.pdf")
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Add()
        ps = doc.PageSetup
        ps.TopMargin = ps.BottomMargin = ps.LeftMargin = ps.RightMargin = 0
        ps.HeaderDistance = ps.FooterDistance = 0
        ps.PageWidth = ancho_pt
        ps.PageHeight = alto_pt
        forma = doc.InlineShapes.AddPicture(str(entrada), False, True)
        forma.LockAspectRatio = True
        forma.Width = ancho_pt
        doc.Paragraphs(1).SpaceBefore = 0
        doc.Paragraphs(1).SpaceAfter = 0
        doc.Paragraphs(1).LineSpacingRule = 0  # wdLineSpaceSingle
        doc.ExportAsFixedFormat(str(pdf), 17)
        doc.Close(False)
    finally:
        word.Quit()

    pagina = pymupdf.open(str(pdf))[0]
    pix = pagina.get_pixmap(dpi=dpi, alpha=False)
    pix.save(str(salida))
    print("png:", salida, pix.width, "x", pix.height)


if __name__ == "__main__":
    main()
