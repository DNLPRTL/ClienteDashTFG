# -*- coding: utf-8 -*-
"""Convierte un .docx a PDF con Microsoft Word (COM) para revisar el resultado.

Uso: python docs/memoria/apoyo/docx_a_pdf.py entrada.docx [salida.pdf]
"""
import sys
from pathlib import Path

import win32com.client


def main():
    entrada = Path(sys.argv[1]).resolve()
    salida = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else entrada.with_suffix(".pdf")
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(str(entrada), ReadOnly=True)
        try:
            doc.ExportAsFixedFormat(str(salida), 17)  # 17 = wdExportFormatPDF
            print("paginas:", doc.ComputeStatistics(2), "| palabras:", doc.ComputeStatistics(0))
        finally:
            doc.Close(False)
    finally:
        word.Quit()
    print("pdf:", salida)


if __name__ == "__main__":
    main()
