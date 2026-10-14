"""Prueba de humo: sesiones reales del cliente en Windows contra el servidor DASH (tiempo real).

Construye la config de cliente igual que scripts/3_evaluacion/ejecutar_evaluacion.py para una
ventana de validacion, ejecuta main.py y compara la sesion real con la del simulador (regla de
paradas corregida, C2). No es la VM: solo comprueba que el codigo nuevo funciona de punta a punta.

Uso: python sesion_real_windows.py <id_traza> <video> <controlador> [<controlador> ...]
"""
from __future__ import annotations

import csv
import glob
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

import simulador as sim
import ventanas as ven
from core.evaluacion.catalogo import PERFILES_VIDEO
from core.evaluacion.qoe import EntradaQoESegmento, calcular_qoe_lineal
from prueba_previa import parametros_para

PARAMETROS_EXTRA = {
    "propio_cuantiles_fijos": {
        "ruta_cuantiles_fijos": r"C:\Users\danie\Documents\TFG Material\03_modelos\cuantiles_fijos\cuantiles_fijos.json"
    }
}


def config_cliente(ventana, video, clave, dir_salida):
    return {
        "mpd_url": PERFILES_VIDEO[video]["mpd_url"],
        "motor_video": {"nombre": "simulado", "tiempo_min_cola": 0.1, "decodificar_video": False, "nombre_sink": None},
        "controlador": {"nombre": clave, "parametros": parametros_para(clave, video, PARAMETROS_EXTRA)},
        "reproduccion": {"calidad_inicial": 0, "decision_inicial_controlador": False, "headless": True,
                         "buffer_maximo_s": 60.0, "espera_vaciado_buffer_s": 0.01, "preroll_s": 0.0,
                         "max_segmentos_video": 30},
        "descargador": {"max_reintentos": 3, "detallado": False},
        "reproduccion_red": {"activada": True, "ruta_csv_traza": sim.ruta_traza_local(ventana["ruta_traza_normalizada"]),
                             "inicio_ventana_s": ventana["inicio_ventana_s"], "duracion_ventana_s": ventana["duracion_ventana_s"],
                             "politica_fin": "loop", "max_bucles": 1, "tiempos_compactos": True, "con_esperas": True},
        "salida": {"dir_raiz": dir_salida, "fichero_telemetria_segmentos": "telemetria_segmentos.csv",
                   "fichero_segmentos_evaluacion": "segmentos_evaluacion.csv"},
        "registro": {"activada": True, "nivel": "INFO"},
        "analisis": {"activada": False},
    }


def ejecutar(ventana, video, clave, raiz):
    dir_salida = os.path.join(raiz, clave)
    os.makedirs(dir_salida, exist_ok=True)
    ruta_cfg = os.path.join(raiz, clave + ".json")
    with open(ruta_cfg, "w", encoding="utf-8") as fichero:
        json.dump(config_cliente(ventana, video, clave, dir_salida), fichero, indent=1)
    entorno = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    proceso = subprocess.run([sys.executable, os.path.join(sim.RAIZ_CODIGO, "main.py"), "--config", ruta_cfg],
                             cwd=sim.RAIZ_CODIGO, env=entorno, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    telemetria = glob.glob(os.path.join(dir_salida, "**", "telemetria_segmentos.csv"), recursive=True)
    if proceso.returncode != 0 or not telemetria:
        return clave, None, proceso.stdout.decode("utf-8", "replace")[-2000:]
    filas = list(csv.DictReader(open(telemetria[0], encoding="utf-8")))
    return clave, filas, ""


def main():
    id_traza, video, *claves = sys.argv[1:]
    ventana = next(v for v in ven.ventanas_relevantes(ven.cargar_catalogo(), particion="test") if v["id_traza"] == id_traza)
    raiz = tempfile.mkdtemp(prefix="humo_windows_", dir=os.environ.get("TMP"))
    with ThreadPoolExecutor(max_workers=len(claves)) as ej:
        resultados = list(ej.map(lambda c: ejecutar(ventana, video, c, raiz), claves))
    for clave, filas, error in resultados:
        if filas is None:
            print(clave, "FALLO\n", error)
            continue
        evaluables = [f for f in filas if f["es_init"] == "0" and f["usar_en_eval"] == "1"]
        q = calcular_qoe_lineal([EntradaQoESegmento(float(f["feedback_bitrate_actual"]) * 8 / 1000, float(f["duracion_stall"] or 0)) for f in evaluables])
        respaldos = sum(int(f.get("feedback_respaldo_red_usado") or 0) for f in evaluables)
        niveles_real = [int(f["feedback_nivel"]) for f in filas if f["es_init"] == "0"]
        cfg = sim.ConfigSesion(clave_controlador=clave, parametros=parametros_para(clave, video, PARAMETROS_EXTRA),
                               id_perfil_video=video, ruta_traza=ventana["ruta_traza_normalizada"],
                               inicio_ventana_s=ventana["inicio_ventana_s"], duracion_ventana_s=ventana["duracion_ventana_s"],
                               politica_fin="loop", max_bucles=1, regla_paradas="esperado", etiqueta="humo")
        r = sim.simular_sesion(cfg)
        print("%-28s real: QoE %.3f rebuf %.2f s paradas %d respaldos %d | simulador: QoE %.3f rebuf %.2f s | niveles iguales: %s" % (
            clave, q.qoe_media, q.rebuffering_total_s, q.num_stalls, respaldos, r.resumen["qoe_lineal_media"],
            r.resumen["rebuffering_total_s"], niveles_real == [f.nivel for f in r.filas]))
        print("   paradas por fila (real):", {int(f["indice_segmento"]): round(float(f["duracion_stall"]), 2) for f in filas if float(f["duracion_stall"] or 0) > 0})
    print("salida en", raiz)


if __name__ == "__main__":
    main()
