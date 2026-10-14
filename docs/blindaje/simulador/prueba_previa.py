"""Ejecuta en el simulador un banco de sesiones (ventanas x videos x controladores).

Sirve para la prueba previa sobre la particion de validacion (semaforo 1) y para la regresion
del codigo (mismas trayectorias antes y despues de un cambio). Escribe un JSON con una fila por
sesion: resumen de QoE y secuencia de niveles.

Uso:
  python prueba_previa.py --salida banco.json [--particion test] [--videos a,b] \
      [--controladores a,b] [--regla cabeza|esperado] [--parametros extra.json] [--procesos N]
"""
from __future__ import annotations

import argparse
import json
import os
import time
from typing import Any, Dict, List

import simulador as sim
import ventanas as ven

VIDEOS_VISTOS = ("paseo_10min_30fps_4s", "blender_10min_30fps_4s", "paseo_10min_60fps_4s", "blender_10min_60fps_4s")
CONTROLADORES_BASE = ("basado_en_tasa", "bba", "bola", "mpc_robusto", "controlador_propio")
PARAMETROS_PROPIO = {
    "dir_bundle": sim.DIR_BUNDLE_WINDOWS,
    "alfa_riesgo": 0.75,
    "solo_diagnostico": False,
    "controlador_respaldo": "mpc_robusto",
    "latencia_max_inferencia_ms": 50.0,
    "verificar_hashes": True,
}


def parametros_para(clave: str, id_video: str, extra: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    parametros: Dict[str, Any] = {}
    clave_registro = extra.get(clave, {}).get("_clave_registro", clave)
    if clave_registro.startswith(("controlador_propio", "propio")):
        parametros.update(PARAMETROS_PROPIO)
    parametros.update(extra.get(clave, {}))
    parametros["id_perfil_video"] = id_video
    return parametros


def construir_configs(
    ventanas: List[Dict[str, Any]],
    videos: List[str],
    controladores: List[str],
    *,
    regla: str,
    extra: Dict[str, Dict[str, Any]],
    politica_fin: str = "loop",
    max_bucles: int = 1,
) -> List[sim.ConfigSesion]:
    configs = []
    for ventana in ventanas:
        for video in videos:
            for clave in controladores:
                clave_registro = extra.get(clave, {}).get("_clave_registro", clave)
                parametros = {k: v for k, v in parametros_para(clave, video, extra).items() if not k.startswith("_")}
                configs.append(
                    sim.ConfigSesion(
                        clave_controlador=clave_registro,
                        parametros=parametros,
                        id_perfil_video=video,
                        ruta_traza=ventana["ruta_traza_normalizada"],
                        inicio_ventana_s=ventana["inicio_ventana_s"],
                        duracion_ventana_s=ventana["duracion_ventana_s"],
                        politica_fin=politica_fin,
                        max_bucles=max_bucles,
                        regla_paradas=regla,
                        etiqueta="{0}|{1}|{2}".format(ventana["id_traza"], video, clave),
                        extra={"alias": clave, "id_traza": ventana["id_traza"], "id_dataset": ventana["id_dataset"],
                               "grupo_fuga": ventana["grupo_fuga"], "video": video,
                               "mitad": ven.mitad_validacion(ventana["grupo_fuga"]),
                               "media_kbps": ventana["media_kbps"], "min_kbps": ventana["min_kbps"]},
                    )
                )
    return configs


def a_fila(res: sim.ResultadoSesion) -> Dict[str, Any]:
    fila = dict(res.extra)
    fila.update(res.resumen)
    fila["niveles"] = [f.nivel for f in res.filas]
    fila["rebuffering_por_fila"] = [round(f.rebuffering_s, 4) for f in res.filas]
    fila["error"] = res.error
    fila["excede_ventana"] = res.excede_ventana
    fila["t_ultima_descarga_s"] = round(res.t_ultima_descarga_s, 3)
    return fila


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--salida", required=True)
    p.add_argument("--particion", default="test")
    p.add_argument("--videos", default=",".join(VIDEOS_VISTOS))
    p.add_argument("--controladores", default=",".join(CONTROLADORES_BASE))
    p.add_argument("--regla", choices=("cabeza", "esperado"), default="esperado")
    p.add_argument("--parametros", default="", help="JSON {alias: {parametros..., _clave_registro: clave}}")
    p.add_argument("--max-ventanas", type=int, default=0)
    p.add_argument("--procesos", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    args = p.parse_args()

    extra = json.load(open(args.parametros, encoding="utf-8")) if args.parametros else {}
    ventanas = ven.ventanas_relevantes(ven.cargar_catalogo(), particion=args.particion)
    if args.max_ventanas:
        ventanas = ventanas[: args.max_ventanas]
    configs = construir_configs(
        ventanas, args.videos.split(","), args.controladores.split(","), regla=args.regla, extra=extra
    )
    inicio = time.perf_counter()
    resultados = sim.simular_lote(configs, procesos=args.procesos)
    filas = [a_fila(r) for r in resultados]
    with open(args.salida, "w", encoding="utf-8") as fichero:
        json.dump({"particion": args.particion, "regla": args.regla, "ventanas": len(ventanas), "sesiones": filas},
                  fichero, ensure_ascii=False)
    errores = sum(1 for f in filas if f["error"])
    print("sesiones {0} en {1:.0f} s, errores {2}, exceden la ventana {3}".format(
        len(filas), time.perf_counter() - inicio, errores, sum(1 for f in filas if f["excede_ventana"])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
