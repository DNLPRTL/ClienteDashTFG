"""Valida el simulador contra paquetes reales de la VM (fase de blindaje).

Dos modos por sesion:
- forzado: el simulador sigue los mismos niveles que eligio la VM. Valida la red, el buffer,
  las paradas y la QoE sin que influyan las decisiones.
- cerrado: decide el controlador real. Valida el conjunto, incluidas las decisiones.

Uso:
  python validar_simulador.py <paquete> [<paquete> ...] [--modo forzado|cerrado|ambos]
         [--controladores a,b] [--procesos N] [--regla cabeza|esperado] [--salida informe.json]

--regla esperado para los paquetes grabados con el reproductor corregido (C2, desde el 15/10).
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import statistics
import sys
from collections import defaultdict
from typing import Any, Dict, List, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import simulador as sim  # noqa: E402

from core.controladores.base import ControladorBase  # noqa: E402
from core.controladores.contrato import cuantizar_tasa_a_nivel  # noqa: E402
from core.evaluacion.qoe import EntradaQoESegmento, calcular_qoe_lineal  # noqa: E402

CLAVES_CONTROLADOR = (
    "basado_en_tasa",
    "bba",
    "bola",
    "mpc_robusto",
    "controlador_propio",
    "mpc",
    "propio_mediana",
    "propio_cuantiles_fijos",
    "propio_cuantiles_recientes",
)


class ControladorReplay(ControladorBase):
    """Devuelve, tras cada descarga, el nivel que la VM uso para el segmento siguiente."""

    nombre = "replay"

    def __init__(self, niveles_por_indice: Dict[int, int]) -> None:
        super().__init__()
        self.niveles = dict(niveles_por_indice)

    def calcularAccionControl(self):
        fb = self.feedback or {}
        tasas = list(fb.get("tasas") or [])
        siguiente = int(fb.get("indice_segmento", 0)) + 1
        nivel = self.niveles.get(siguiente, int(fb.get("nivel", 0)))
        self.fijarDuracionInactividad(0.0)
        tasa = float(tasas[max(0, min(nivel, len(tasas) - 1))])
        self.fijarAccionControl(tasa)
        return tasa

    def cuantizarTasa(self, tasa):
        return cuantizar_tasa_a_nivel(tasa, (self.feedback or {}).get("tasas"))


def leer_sesiones(raiz: str) -> List[Dict[str, Any]]:
    plan = json.load(open(os.path.join(raiz, "00_protocolo", "plan_sesiones.json"), encoding="utf-8"))["sesiones"]
    sesiones = []
    for sesion in plan:
        dirs = sorted(glob.glob(os.path.join(raiz, "01_ejecucion", "ejecuciones", sesion["id_sesion"], "ejecucion_*")))
        if not dirs:
            continue
        manifiesto = os.path.join(dirs[-1], "manifiesto_ejecucion.json")
        if not os.path.isfile(manifiesto) or json.load(open(manifiesto, encoding="utf-8")).get("estado") != "completado":
            continue
        ruta_cfg = os.path.join(raiz, "00_protocolo", "configs_cliente", sesion["id_sesion"] + ".yaml")
        config = json.load(open(ruta_cfg, encoding="utf-8"))
        filas = list(csv.DictReader(open(os.path.join(dirs[-1], "telemetria_segmentos.csv"), encoding="utf-8")))
        sesiones.append({"sesion": sesion, "config": config, "filas": filas})
    return sesiones


def qoe_vm(filas: List[Dict[str, str]]) -> Dict[str, float]:
    evaluables = [f for f in filas if f["es_init"] == "0" and f["usar_en_eval"] == "1"]
    entradas = [
        EntradaQoESegmento(
            bitrate_kbps=float(f["feedback_bitrate_actual"]) * 8.0 / 1000.0,
            rebuffering_s=float(f["duracion_stall"] or 0.0),
        )
        for f in evaluables
    ]
    q = calcular_qoe_lineal(entradas)
    return {
        "qoe_lineal_media": q.qoe_media,
        "rebuffering_total_s": q.rebuffering_total_s,
        "bitrate_medio_kbps": q.bitrate_medio_kbps,
        "num_stalls": q.num_stalls,
    }


def config_sim(item: Dict[str, Any]) -> sim.ConfigSesion:
    sesion, config = item["sesion"], item["config"]
    parametros = dict((config.get("controlador") or {}).get("parametros") or {})
    if "dir_bundle" in parametros:
        parametros["dir_bundle"] = sim.DIR_BUNDLE_WINDOWS
    if "ruta_cuantiles_fijos" in parametros:
        parametros["ruta_cuantiles_fijos"] = r"C:\Users\danie\Documents\TFG Material\03_modelos\cuantiles_fijos\cuantiles_fijos.json"
    red = config.get("reproduccion_red") or {}
    # Latencia de cada decision tal como la midio el reproductor (los paquetes de agosto y
    # octubre llevan el planificador antiguo, de 174-315 ms por decision).
    latencias = [
        float(f["ms_decision_politica"]) / 1000.0
        for f in item["filas"]
        if f["es_init"] == "0" and f.get("ms_decision_politica") not in (None, "", "0", "0.0")
    ]
    return sim.ConfigSesion(
        clave_controlador=sesion["clave_controlador"],
        parametros=parametros,
        id_perfil_video=sesion["id_perfil_video"],
        ruta_traza=sesion["ruta_traza_normalizada"],
        inicio_ventana_s=float(sesion["inicio_ventana_s"]),
        duracion_ventana_s=float(sesion["duracion_ventana_s"]),
        politica_fin=str(red.get("politica_fin", "fail")),
        max_bucles=int(red.get("max_bucles", 0) or 0),
        max_segmentos=int((config.get("reproduccion") or {}).get("max_segmentos_video", 30)),
        etiqueta=sesion["id_sesion"],
        latencias_registradas_s=latencias,
        # Paquetes con el reproductor corregido (C2): regla "esperado"; los anteriores, "cabeza".
        regla_paradas=item.get("regla", "cabeza"),
    )


def _comparar(item: Dict[str, Any], modo: str) -> Dict[str, Any]:
    cfg = config_sim(item)
    filas_vm = [f for f in item["filas"] if f["es_init"] == "0"]
    niveles_vm = {int(f["indice_segmento"]): int(f["feedback_nivel"]) for f in filas_vm}
    controlador = ControladorReplay(niveles_vm) if modo == "forzado" else None
    res = sim.simular_sesion(cfg, controlador=controlador)
    vm = qoe_vm(item["filas"])
    salida = {
        "id_sesion": cfg.etiqueta,
        "clave": cfg.clave_controlador,
        "id_ventana": item["sesion"]["id_ventana_traza"],
        "video": item["sesion"]["id_perfil_video"],
        "tramo": item["sesion"].get("tramo_dificultad", ""),
        "error": res.error,
        "qoe_vm": vm["qoe_lineal_media"],
        "rebuf_vm": vm["rebuffering_total_s"],
        "bitrate_vm": vm["bitrate_medio_kbps"],
    }
    if res.error:
        return salida
    niveles_sim = [f.nivel for f in res.filas]
    salida.update(
        {
            "qoe_sim": res.resumen["qoe_lineal_media"],
            "rebuf_sim": res.resumen["rebuffering_total_s"],
            "bitrate_sim": res.resumen["bitrate_medio_kbps"],
            "niveles_identicos": niveles_sim == [int(f["feedback_nivel"]) for f in filas_vm],
            "err_descarga_mediana_s": statistics.median(
                abs(a.tiempo_descarga_s - float(b["feedback_tiempo_ultima_descarga"]))
                for a, b in zip(res.filas, filas_vm)
            ),
            "err_buffer_mediana_s": statistics.median(
                abs(a.buffer_tras_encolar_s - float(b["feedback_tiempo_en_cola"])) for a, b in zip(res.filas, filas_vm)
            ),
        }
    )
    return salida


def _comparar_forzado(item):
    return _comparar(item, "forzado")


def _comparar_cerrado(item):
    return _comparar(item, "cerrado")


def resumen_modo(filas: List[Dict[str, Any]], modo: str) -> Dict[str, Any]:
    validas = [f for f in filas if not f.get("error")]
    errores = [f for f in filas if f.get("error")]
    dq = [abs(f["qoe_sim"] - f["qoe_vm"]) for f in validas]
    dr = [abs(f["rebuf_sim"] - f["rebuf_vm"]) for f in validas]
    out: Dict[str, Any] = {
        "modo": modo,
        "sesiones": len(filas),
        "errores": len(errores),
        "mediana_abs_dqoe": statistics.median(dq) if dq else None,
        "p90_abs_dqoe": sorted(dq)[int(0.9 * (len(dq) - 1))] if dq else None,
        "max_abs_dqoe": max(dq) if dq else None,
        "media_dqoe_sim_menos_vm": statistics.mean(f["qoe_sim"] - f["qoe_vm"] for f in validas) if validas else None,
        "mediana_abs_drebuf_s": statistics.median(dr) if dr else None,
        "niveles_identicos": sum(1 for f in validas if f["niveles_identicos"]),
        "mediana_err_descarga_s": statistics.median(f["err_descarga_mediana_s"] for f in validas) if validas else None,
        "mediana_err_buffer_s": statistics.median(f["err_buffer_mediana_s"] for f in validas) if validas else None,
    }
    por_clave = defaultdict(list)
    for f in validas:
        por_clave[f["clave"]].append(f)
    out["por_controlador"] = {
        clave: {
            "n": len(v),
            "mediana_abs_dqoe": statistics.median(abs(x["qoe_sim"] - x["qoe_vm"]) for x in v),
            "media_dqoe": statistics.mean(x["qoe_sim"] - x["qoe_vm"] for x in v),
            "niveles_identicos": sum(1 for x in v if x["niveles_identicos"]),
        }
        for clave, v in sorted(por_clave.items())
    }
    return out


def diferencias_pareadas(filas: List[Dict[str, Any]], a: str, b: str) -> Dict[str, Any]:
    por_escenario = defaultdict(dict)
    for f in filas:
        if not f.get("error"):
            por_escenario[(f["id_ventana"], f["video"])][f["clave"]] = f
    vm, si = [], []
    for valores in por_escenario.values():
        if a in valores and b in valores:
            vm.append(valores[a]["qoe_vm"] - valores[b]["qoe_vm"])
            si.append(valores[a]["qoe_sim"] - valores[b]["qoe_sim"])
    if len(vm) < 3:
        return {"n": len(vm)}
    return {
        "n": len(vm),
        "media_vm": statistics.mean(vm),
        "media_sim": statistics.mean(si),
        "correlacion": statistics.correlation(vm, si) if statistics.pstdev(vm) > 0 and statistics.pstdev(si) > 0 else None,
    }


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("paquetes", nargs="+")
    p.add_argument("--modo", choices=("forzado", "cerrado", "ambos"), default="ambos")
    p.add_argument("--controladores", default="")
    p.add_argument("--procesos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    p.add_argument("--regla", choices=("cabeza", "esperado"), default="cabeza")
    p.add_argument("--salida", default="")
    args = p.parse_args(argv)
    claves = set(filter(None, args.controladores.split(","))) or set(CLAVES_CONTROLADOR)

    items = []
    for raiz in args.paquetes:
        for item in leer_sesiones(raiz):
            if item["sesion"]["clave_controlador"] in claves and not item["sesion"].get("sintetica"):
                item["paquete"] = os.path.basename(raiz.rstrip("/\\"))
                item["regla"] = args.regla
                items.append(item)
    print("sesiones reales completadas:", len(items), flush=True)

    informe: Dict[str, Any] = {"paquetes": [os.path.basename(r.rstrip("/\\")) for r in args.paquetes]}
    modos = ("forzado", "cerrado") if args.modo == "ambos" else (args.modo,)
    from concurrent.futures import ProcessPoolExecutor

    for modo in modos:
        funcion = _comparar_forzado if modo == "forzado" else _comparar_cerrado
        with ProcessPoolExecutor(max_workers=args.procesos) as ej:
            filas = list(ej.map(funcion, items, chunksize=2))
        for item, fila in zip(items, filas):
            fila["paquete"] = item["paquete"]
        r = resumen_modo(filas, modo)
        if modo == "cerrado":
            for otro in ("mpc_robusto", "propio_mediana", "propio_cuantiles_fijos", "propio_cuantiles_recientes"):
                r["pareadas_propio_vs_" + otro] = diferencias_pareadas(filas, "controlador_propio", otro)
            r["pareadas_bola_vs_bba"] = diferencias_pareadas(filas, "bola", "bba")
        informe[modo] = r
        informe[modo + "_sesiones"] = filas
        print(json.dumps(r, indent=1, ensure_ascii=False, default=float), flush=True)
    if args.salida:
        with open(args.salida, "w", encoding="utf-8") as fichero:
            json.dump(informe, fichero, indent=1, ensure_ascii=False, default=float)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
