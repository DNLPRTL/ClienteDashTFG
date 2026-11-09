# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap5_8_resumen_capitulo5.docx: el cierre del capitulo 5.

Forma: tres parrafos corridos sin epigrafe propio (biblia 6.3: cada capitulo cierra con un resumen
que enlaza con el siguiente; en el corpus del tutor el cierre va sin titulo). Se pega al final del
5.7, despues de su ultimo parrafo. No introduce cifras nuevas: cada numero que menciona ya aparece
en 5.1 a 5.7, y el script lo comprueba contra el texto de los borradores .docx entregados y de los
apartados de Daniel (5.1 y 5.2, en docs/memoria/borradores/*.md).

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap5_resumen.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES_DOCX = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
BORRADORES_MD = RAIZ_REPO / "docs" / "memoria" / "borradores"
SALIDA = BORRADORES_DOCX / "cap5_8_resumen_capitulo5.docx"

PARRAFOS = [
    # 5.1 a 5.4: lenguaje, cliente, analizador, ejecutor.
    "Este capítulo ha descrito cómo se materializa el diseño del capítulo 4. Todo el sistema está "
    "escrito en Python, compatible desde la versión 3.8 de la máquina virtual cliente, con tres "
    "dependencias externas declaradas y PyTorch instalado aparte para el modelo del controlador propio "
    "(apartado 5.1). El cliente monta cada sesión a partir de un fichero de configuración, reproduce "
    "en dos hilos con el motor simulado, descarga con un descargador que la emulación de red envuelve "
    "sin que el reproductor lo note y registra la telemetría de cada segmento (apartado 5.2). El "
    "analizador del manifiesto resuelve los cinco MPD del experimento con plantillas de URL e índices "
    "sidx y entrega al reproductor la escalera y la lista de segmentos (apartado 5.3). El ejecutor de "
    "experimentos convierte un preset y una configuración en un protocolo y un plan de sesiones "
    "deterministas, los ejecuta en serie y deja un paquete de evidencia que el análisis lee después "
    "(apartado 5.4).",
    # 5.5 a 5.7: controladores y entrenamiento.
    "Sobre la interfaz común corren los cuatro comparadores clásicos, con el MPC robusto en su forma "
    "canónica de horizonte cinco, QoE lineal y tamaños reales de los segmentos, y el planificador que "
    "comparte con el controlador propio (apartado 5.5). El controlador propio conserva ese planificador "
    "y cambia la predicción: un conjunto de cinco redes recurrentes predice cuatro cuantiles del "
    "throughput para cada uno de los cinco segmentos siguientes, ensanchados según el desacuerdo entre "
    "las redes, y el planificador promedia los tres escenarios no optimistas con α = 0,75; si el modelo "
    "falla, decide el MPC robusto como respaldo, y tres variantes de ablación aíslan la red y la "
    "agregación de riesgo (apartado 5.6). El modelo se entrena fuera del cliente, en un simulador que "
    "comparte con él la física de la red y los tamaños reales, con ventanas de las particiones de "
    "entrenamiento y validación del catálogo y una comprobación de calibración antes de exportar el "
    "paquete (apartado 5.7).",
    # Enlace con el capitulo 6.
    "Con esto queda cerrada la implementación y puede medirse. El capítulo 6 presenta el experimento "
    "final: 74 ventanas reales de la partición de evaluación, cada una con un vídeo visto en el "
    "entrenamiento y con un contenido nuevo, ejecutadas con los ocho controladores en 1208 sesiones en "
    "la máquina virtual cliente, con un protocolo fijado antes de ejecutar. Se contrastan cinco "
    "hipótesis prerregistradas sobre la QoE lineal y las paradas del controlador propio frente al MPC "
    "robusto y frente a sus variantes de ablación, se comprueba la integridad de la ejecución y se "
    "informa de todos los resultados, favorables o no.",
]

# Cifras y hechos del resumen que deben existir ya en el capitulo (apartado donde se dicen).
COMPROBACIONES = {
    "3.8": ("5.1", "md"),
    "tres paquetes externos": ("5.1", "md"),
    "dos hilos": ("5.2", "md"),
    "cinco manifiestos": ("5.3", "docx"),
    "sidx": ("5.3", "docx"),
    "1208": ("5.4", "docx"),
    "74": ("5.4", "docx"),
    "horizonte": ("5.5", "docx"),
    "α = 0,75": ("5.6", "docx"),
    "cuatro cuantiles": ("5.6", "docx"),
    "respaldo": ("5.6", "docx"),
    "ablación": ("5.6", "docx"),
    "calibración": ("5.7", "docx"),
    "simulador": ("5.7", "docx"),
}
FICHEROS = {
    "5.1": BORRADORES_MD / "cap5_1_lenguaje_librerias.md",
    "5.2": BORRADORES_MD / "cap5_2_cliente_replay.md",
    "5.3": BORRADORES_DOCX / "cap5_3_analizador_mpd.docx",
    "5.4": BORRADORES_DOCX / "cap5_4_ejecutor_configuracion.docx",
    "5.5": BORRADORES_DOCX / "cap5_5_controladores_clasicos.docx",
    "5.6": BORRADORES_DOCX / "cap5_6_controlador_propio.docx",
    "5.7": BORRADORES_DOCX / "cap5_7_entorno_entrenamiento.docx",
}


def texto_de(ruta: Path) -> str:
    if ruta.suffix == ".docx":
        d = Document(str(ruta))
        partes = [p.text for p in d.paragraphs]
        partes += [c.text for t in d.tables for r in t.rows for c in r.cells]
        return "\n".join(partes)
    return ruta.read_text(encoding="utf-8")


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    textos = {k: texto_de(v) for k, v in FICHEROS.items()}
    faltan = [(frag, ap) for frag, (ap, _) in COMPROBACIONES.items() if frag not in textos[ap]]
    assert not faltan, "cifras del resumen que no aparecen en el capitulo: {0}".format(faltan)
    # Tres variantes de ablacion, cinco redes, cinco horizontes: dichos en el 5.6.
    for frag in ("tres variantes", "5 GRU", "cinco segmentos"):
        assert frag in textos["5.6"] or frag in textos["5.7"], frag
    # Ocho controladores y dos videos por ventana: dichos en el 5.4.
    for frag in ("8", "uno visto"):
        assert frag in textos["5.4"], frag

    b = Borrador(PLANTILLA)
    for p in PARRAFOS:
        b.parrafo(p)
    b.guardar(SALIDA)
    palabras = sum(len(re.findall(r"\w+", p)) for p in PARRAFOS)
    print("palabras del cuerpo:", palabras)
    print("salida:", SALIDA)


if __name__ == "__main__":
    main()
