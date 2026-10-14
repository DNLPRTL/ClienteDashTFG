"""Repetibilidad del banco de pruebas: compara sesion a sesion las 60 sesiones sinteticas,
que se ejecutaron con las mismas condiciones en las dos evaluaciones (misma ventana,
mismo video, mismo controlador, mismo codigo y mismo modelo).

Uso: python repetibilidad_sinteticas.py <paquete_1> <paquete_2>
"""
from __future__ import annotations

import csv
import statistics
import sys
from pathlib import Path


def sesiones_sinteticas(paquete: Path):
    with (paquete / "02_resultados" / "sesiones.csv").open(encoding="utf-8", newline="") as fichero:
        filas = [fila for fila in csv.DictReader(fichero) if fila["sintetica"] == "1"]
    return {(f["alias_controlador"], f["id_perfil_video"], f["id_ventana_traza"]): f for f in filas}


def niveles(paquete: Path, id_sesion: str):
    rutas = sorted((paquete / "01_ejecucion" / "ejecuciones" / id_sesion).glob("ejecucion_*/telemetria_segmentos.csv"))
    with rutas[-1].open(encoding="utf-8", newline="") as fichero:
        return [fila["nivel_elegido_politica"] for fila in csv.DictReader(fichero)]


def main():
    p1, p2 = Path(sys.argv[1]), Path(sys.argv[2])
    s1, s2 = sesiones_sinteticas(p1), sesiones_sinteticas(p2)
    comunes = sorted(set(s1) & set(s2))
    print("Sesiones sinteticas comunes:", len(comunes))
    por_controlador = {}
    for clave in comunes:
        a, b = s1[clave], s2[clave]
        iguales = niveles(p1, a["id_sesion"]) == niveles(p2, b["id_sesion"])
        dq = float(b["qoe_lineal_media"]) - float(a["qoe_lineal_media"])
        por_controlador.setdefault(clave[0], []).append((iguales, dq))
    print("{:<20} {:>9} {:>14} {:>14}".format("controlador", "identicas", "|dQoE| medio", "|dQoE| max"))
    todas = []
    for alias, datos in sorted(por_controlador.items()):
        dif = [abs(dq) for _, dq in datos]
        todas.extend(dif)
        print("{:<20} {:>5}/{:<3} {:>14.4f} {:>14.4f}".format(
            alias, sum(1 for iguales, _ in datos if iguales), len(datos), statistics.mean(dif), max(dif)))
    print("Total: |dQoE| medio {:.4f}, maximo {:.4f}".format(statistics.mean(todas), max(todas)))


if __name__ == "__main__":
    main()
