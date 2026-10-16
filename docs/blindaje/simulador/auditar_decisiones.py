"""Auditoria fuera de linea de las decisiones de un paquete de la VM (fase de blindaje).

Para cada sesion crea el controlador con el codigo entregado y los parametros de la sesion, le da la
misma realimentacion que registro el reproductor, en el mismo orden, y comprueba que cada decision
coincide con la registrada (tasa objetivo y nivel).

La realimentacion sale de telemetria_segmentos.csv: las columnas feedback_* son exactamente el
diccionario que recibio el controlador (construir_realimentacion_controlador), escrito con todos
los decimales. Antes de la primera fila, el reproductor da una realimentacion de cabecera sin
descarga (reproductor.py, obtener_realimentacion(0, 0, 0.0)), que aqui se reconstruye igual.

Uso: python auditar_decisiones.py <paquete> [--procesos N] [--salida informe.json]
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from typing import Any, Dict, List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import simulador as sim  # noqa: E402,F401  (anade el codigo entregado al path)

from core.controladores.registro import crear_controlador  # noqa: E402
from core.feedback_reproductor import CLAVES_REALIMENTACION, construir_realimentacion_controlador  # noqa: E402

RUTA_CUANTILES_FIJOS_WINDOWS = r"C:\Users\danie\Documents\TFG Material\03_modelos\cuantiles_fijos\cuantiles_fijos.json"
ENTERO = re.compile(r"-?\d+")


def _valor(texto: str, clave: str) -> Any:
    if texto == "":
        return None
    if clave == "tasas":
        return json.loads(texto)
    return int(texto) if ENTERO.fullmatch(texto) else float(texto)


def realimentacion_de_fila(fila: Dict[str, str]) -> Dict[str, Any]:
    return {clave: _valor(fila["feedback_" + clave], clave) for clave in CLAVES_REALIMENTACION}


def realimentacion_cabecera(primera: Dict[str, Any], nivel_inicial: int) -> Dict[str, Any]:
    tasas = list(primera["tasas"])
    return construir_realimentacion_controlador(
        bytes_en_cola=0,
        tiempo_en_cola=0,
        tasas=tasas,
        duraciones_fragmentos=[4.0] * len(tasas),
        nivel_actual=nivel_inicial,
        nivel_max=primera["nivel_max"],
        bytes_descargados=0,
        indice_segmento=0,
        inicio_peticion_segmento=None,
        fin_peticion_segmento=None,
        ultimo_tamano=0,
        ultimo_tiempo=0.0,
        duracion_fragmento=None,
        segmentos_totales=primera["segmentos_totales"],
    )


def auditar_sesion(item: Dict[str, Any]) -> Dict[str, Any]:
    config = item["config"]
    clave = config["controlador"]["nombre"]
    parametros = dict(config["controlador"].get("parametros") or {})
    if "dir_bundle" in parametros:
        parametros["dir_bundle"] = sim.DIR_BUNDLE_WINDOWS
    if "ruta_cuantiles_fijos" in parametros:
        parametros["ruta_cuantiles_fijos"] = RUTA_CUANTILES_FIJOS_WINDOWS
    controlador = crear_controlador(clave, parametros)
    filas = item["filas"]
    nivel_inicial = int((config.get("reproduccion") or {}).get("calidad_inicial", 0))
    controlador.fijarFeedbackReproductor(realimentacion_cabecera(realimentacion_de_fila(filas[0]), nivel_inicial))
    decisiones, distintas, respaldos = 0, [], 0
    for fila in filas:
        controlador.fijarFeedbackReproductor(realimentacion_de_fila(fila))
        if fila["es_init"] == "1" or not (fila.get("tasa_objetivo_politica") or "").strip():
            continue
        tasa = controlador.calcularAccionControl()
        nivel = min(controlador.cuantizarTasa(tasa), int(fila["feedback_nivel_max"]))
        decisiones += 1
        if hasattr(controlador, "obtener_diagnosticos_red"):
            respaldos += int(controlador.obtener_diagnosticos_red().get("respaldo_red_usado", 0) or 0)
        if nivel != int(fila["nivel_elegido_politica"]) or float(tasa) != float(fila["tasa_objetivo_politica"]):
            distintas.append((int(fila["indice_segmento"]), int(fila["nivel_elegido_politica"]), nivel))
    return {"id_sesion": item["id_sesion"], "clave": clave, "decisiones": decisiones, "distintas": distintas,
            "respaldos_en_auditoria": respaldos}


def leer(raiz: str) -> List[Dict[str, Any]]:
    plan = json.load(open(os.path.join(raiz, "00_protocolo", "plan_sesiones.json"), encoding="utf-8"))["sesiones"]
    items = []
    for sesion in plan:
        dirs = sorted(glob.glob(os.path.join(raiz, "01_ejecucion", "ejecuciones", sesion["id_sesion"], "ejecucion_*")))
        config = json.load(open(os.path.join(raiz, "00_protocolo", "configs_cliente", sesion["id_sesion"] + ".yaml"), encoding="utf-8"))
        with open(os.path.join(dirs[-1], "telemetria_segmentos.csv"), encoding="utf-8") as fichero:
            filas = list(csv.DictReader(fichero))
        items.append({"id_sesion": sesion["id_sesion"], "config": config, "filas": filas})
    return items


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("paquete")
    p.add_argument("--procesos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    p.add_argument("--salida", default="")
    args = p.parse_args()
    items = leer(args.paquete)
    with ProcessPoolExecutor(max_workers=args.procesos) as ejecutor:
        resultados = list(ejecutor.map(auditar_sesion, items, chunksize=4))
    por_clave: Dict[str, Counter] = defaultdict(Counter)
    for r in resultados:
        por_clave[r["clave"]]["sesiones"] += 1
        por_clave[r["clave"]]["decisiones"] += r["decisiones"]
        por_clave[r["clave"]]["distintas"] += len(r["distintas"])
        por_clave[r["clave"]]["respaldos"] += r["respaldos_en_auditoria"]
    total = sum(c["decisiones"] for c in por_clave.values())
    distintas = sum(c["distintas"] for c in por_clave.values())
    for clave, c in sorted(por_clave.items()):
        print("{0:28s} sesiones {1:4d} | decisiones {2:5d} | distintas {3:3d} | respaldos {4}".format(
            clave, c["sesiones"], c["decisiones"], c["distintas"], c["respaldos"]))
    print("TOTAL: {0} decisiones, {1} distintas".format(total, distintas))
    for r in resultados:
        if r["distintas"]:
            print("  ", r["id_sesion"], r["distintas"][:5])
    if args.salida:
        with open(args.salida, "w", encoding="utf-8") as fichero:
            json.dump({"por_controlador": por_clave, "sesiones": resultados}, fichero, indent=1)
    return 0 if distintas == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
