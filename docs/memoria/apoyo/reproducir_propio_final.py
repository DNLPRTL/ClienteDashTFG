# -*- coding: utf-8 -*-
"""Reproduce fuera de linea las decisiones del controlador propio del experimento final.

Para cada sesion de `controlador_propio` del paquete final reinyecta la realimentacion registrada
en telemetria_segmentos.csv en un ControladorPropio nuevo (bundle de 03_modelos, descriptor del
video de la sesion), comprueba que la accion coincide con la registrada y, sobre el MISMO estado,
calcula que habria elegido el planificador con una pieza cambiada: solo la mediana, solo el
cuantil 0,10, media de los cuatro escenarios (alfa = 1), tamanos nominales y sin ensanchado
epistemico. Guarda tambien la dispersion del ensemble, la propiedad de orden de las puntuaciones
por escenario y los detalles de la decision que ilustra la Figura 5.5.

Regla del ejemplo (fijada antes de mirar): la sesion del propio con la misma ventana y el mismo
video que el ejemplo del 5.5 (ventana real_004 de Oboe, Blender 60 fps) y el mismo segmento (6).

Uso (unos minutos en CPU):  py -3.12 docs/memoria/apoyo/reproducir_propio_final.py
Salida: docs/memoria/apoyo/resumen_propio_final.json (resumen) y
        C:\\Users\\danie\\Documents\\TFG\\apoyo_memoria\\final\\decisiones_propio.jsonl (por decision)
"""
from __future__ import annotations

import csv
import glob
import json
import math
import os
import re
import statistics
import sys
import time
from pathlib import Path

import numpy as np

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
BUNDLE = TFG_MATERIAL / "03_modelos" / "modelo_propio" / "bundle"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
SALIDA_RESUMEN = Path(__file__).resolve().parent / "resumen_propio_final.json"
SALIDA_JSONL = Path(r"C:\Users\danie\Documents\TFG\apoyo_memoria\final\decisiones_propio.jsonl")
EJEMPLO_VENTANA = "real_004_33c3424595"
EJEMPLO_VIDEO = "blender_10min_60fps_4s"
EJEMPLO_SEGMENTO = 6

sys.dont_write_bytecode = True
sys.path.insert(0, str(CODIGO))

import torch  # noqa: E402

from core.controladores.contrato import CLAVES_REALIMENTACION  # noqa: E402
from core.controladores.controlador_propio import ControladorPropio  # noqa: E402
from core.feedback_reproductor import construir_realimentacion_controlador  # noqa: E402
from core.modelo_propio import bundle as bundle_mod  # noqa: E402
from core.modelo_propio import modelo as modelo_mod  # noqa: E402
from core.modelo_propio import planificador as plan_mod  # noqa: E402
from core.modelo_propio.bundle import filas_log_ratio_a_bps  # noqa: E402
from core.modelo_propio.escalera_contenido import escalera_entrenamiento_por_defecto  # noqa: E402
from core.modelo_propio.estado_sesion import media_armonica_bps  # noqa: E402

ENTERO = re.compile(r"-?\d+")
CAPTURA: dict = {}

_predecir_original = bundle_mod.BundleModelo.predecir
_combinar_original = modelo_mod.combinar_cuantiles_ensemble


def _combinar_capturando(predicciones, cuantiles, *, ensanchado_cola=1.0):
    CAPTURA["predicciones_miembros"] = predicciones.detach().clone()
    CAPTURA["ensanchado_cola"] = float(ensanchado_cola)
    return _combinar_original(predicciones, cuantiles, ensanchado_cola=ensanchado_cola)


def _predecir_capturando(self, estado, escalera):
    resultado = _predecir_original(self, estado, escalera)
    CAPTURA.update(estado=estado, escalera=escalera, pred=resultado, bundle=self)
    return resultado


bundle_mod.combinar_cuantiles_ensemble = _combinar_capturando
bundle_mod.BundleModelo.predecir = _predecir_capturando


def _valor(texto, clave):
    if texto == "":
        return None
    if clave == "tasas":
        return json.loads(texto)
    return int(texto) if ENTERO.fullmatch(texto) else float(texto)


def fb_de(fila):
    return {clave: _valor(fila["feedback_" + clave], clave) for clave in CLAVES_REALIMENTACION}


def planificar(estado, escalera, pred, cuantiles, alfa, bundle, mascara):
    return plan_mod.planificar_accion(
        estado=estado, escalera=escalera, prediccion_bps_por_horizonte_y_cuantil=pred, cuantiles=cuantiles,
        horizonte_segmentos=bundle.horizonte_segmentos, mascara_acciones=mascara, alfa_riesgo=alfa,
        peso_rebuffering=bundle.peso_rebuffering, peso_cambios=bundle.peso_cambios,
    )


def puntuaciones_por_escenario(estado, escalera, pred, bundle):
    restantes = max(int(escalera.num_segmentos) - int(estado.indice_segmento), 1)
    h = min(bundle.horizonte_segmentos, len(pred), restantes)
    secuencias = plan_mod._secuencias(tuple(range(escalera.num_representaciones)), h)
    puntuaciones, _ = plan_mod._puntuar_secuencias(
        secuencias=secuencias, estado=estado, escalera=escalera, prediccion=pred[:h],
        peso_rebuffering=bundle.peso_rebuffering, peso_cambios=bundle.peso_cambios,
    )
    return secuencias, puntuaciones


def main():
    plan = json.load(open(PAQUETE / "00_protocolo" / "plan_sesiones.json", encoding="utf-8"))["sesiones"]
    sesiones = [s for s in plan if s["alias_controlador"] == "controlador_propio"]
    SALIDA_JSONL.parent.mkdir(parents=True, exist_ok=True)
    inicio = time.perf_counter()
    totales = {"sesiones": 0, "decisiones": 0, "iguales": 0, "respaldos": 0, "reales": 0, "decisiones_reales": 0}
    cambios = {k: {"n": 0, "mas_bajo": 0, "mas_alto": 0} for k in ("mediana", "peor", "media4", "nominal", "sin_ensanchado")}
    orden_ok, orden_total = 0, 0
    descensos_q10 = []
    sigmas_h1 = []
    inferencias_ms = []
    ejemplo = None
    bundle_ref = None
    with SALIDA_JSONL.open("w", encoding="utf-8") as salida:
        for sesion in sesiones:
            dir_ejec = sorted(glob.glob(os.path.join(str(PAQUETE), "01_ejecucion", "ejecuciones", sesion["id_sesion"], "ejecucion_*")))[-1]
            filas = list(csv.DictReader(open(os.path.join(dir_ejec, "telemetria_segmentos.csv"), encoding="utf-8")))
            config = json.load(open(PAQUETE / "00_protocolo" / "configs_cliente" / (sesion["id_sesion"] + ".yaml"), encoding="utf-8"))
            parametros = dict(config["controlador"]["parametros"])
            parametros["dir_bundle"] = str(BUNDLE)
            ctrl = ControladorPropio(**parametros)
            bundle_ref = ctrl._bundle
            primera = fb_de(filas[0])
            ctrl.fijarFeedbackReproductor(
                construir_realimentacion_controlador(
                    bytes_en_cola=0, tiempo_en_cola=0, tasas=list(primera["tasas"]), duraciones_fragmentos=[4.0] * 6,
                    nivel_actual=int(config["reproduccion"]["calidad_inicial"]), nivel_max=primera["nivel_max"],
                    bytes_descargados=0, indice_segmento=0, inicio_peticion_segmento=None, fin_peticion_segmento=None,
                    ultimo_tamano=0, ultimo_tiempo=0.0, duracion_fragmento=None, segmentos_totales=primera["segmentos_totales"],
                )
            )
            real = not sesion["sintetica"]
            totales["sesiones"] += 1
            totales["reales"] += int(real)
            nivel_previo = int(config["reproduccion"]["calidad_inicial"])
            for fila in filas:
                fb = fb_de(fila)
                ctrl.fijarFeedbackReproductor(fb)
                if fila["es_init"] == "1" or not (fila.get("tasa_objetivo_politica") or "").strip():
                    continue
                CAPTURA.clear()
                tasa = ctrl.calcularAccionControl()
                nivel = min(ctrl.cuantizarTasa(tasa), int(fila["feedback_nivel_max"]))
                diag = ctrl.obtener_diagnosticos_red()
                totales["decisiones"] += 1
                totales["decisiones_reales"] += int(real)
                totales["respaldos"] += int(diag.get("respaldo_red_usado", 0) or 0)
                coincide = nivel == int(fila["nivel_elegido_politica"]) and float(tasa) == float(fila["tasa_objetivo_politica"])
                totales["iguales"] += int(coincide)
                inferencias_ms.append(float(fila["feedback_ms_inferencia_red"]))

                estado, escalera, pred, bundle = CAPTURA["estado"], CAPTURA["escalera"], CAPTURA["pred"], CAPTURA["bundle"]
                mascara = None
                cuantiles = bundle.cuantiles
                idx_med = min(range(len(cuantiles)), key=lambda i: abs(cuantiles[i] - 0.5))
                registro = {"sesion": sesion["id_sesion"], "real": real, "segmento": int(fila["indice_segmento"]),
                            "nivel": nivel, "nivel_previo": nivel_previo, "coincide": coincide,
                            "buffer_s": float(fb["tiempo_en_cola"]), "pred_bps": [list(f) for f in pred]}
                if real:
                    # Variantes sobre el mismo estado.
                    alternativas = {
                        "mediana": planificar(estado, escalera, [(f[idx_med],) for f in pred], (0.5,), 1.0, bundle, mascara).accion,
                        "peor": planificar(estado, escalera, [(f[0],) for f in pred], (0.1,), 1.0, bundle, mascara).accion,
                        "media4": planificar(estado, escalera, pred, cuantiles, 1.0, bundle, mascara).accion,
                    }
                    nominal = escalera_entrenamiento_por_defecto(num_segmentos=escalera.num_segmentos, buffer_maximo_s=escalera.buffer_maximo_s)
                    alternativas["nominal"] = planificar(estado, nominal, pred, cuantiles, bundle.alfa_riesgo, bundle, mascara).accion
                    miembros = CAPTURA["predicciones_miembros"]
                    sin_ens = _combinar_original(miembros, cuantiles, ensanchado_cola=0.0)[0]
                    base = media_armonica_bps(estado.historial_throughput_bps)
                    pred_sin = filas_log_ratio_a_bps(sin_ens, base, bundle.horizonte_segmentos, len(cuantiles))
                    alternativas["sin_ensanchado"] = planificar(estado, escalera, pred_sin, cuantiles, bundle.alfa_riesgo, bundle, mascara).accion
                    for clave, accion in alternativas.items():
                        if int(accion) != nivel:
                            cambios[clave]["n"] += 1
                            if nivel < int(accion):
                                cambios[clave]["mas_bajo"] += 1
                            else:
                                cambios[clave]["mas_alto"] += 1
                    registro["alternativas"] = {k: int(v) for k, v in alternativas.items()}
                    # Propiedad de orden: puntuaciones no decrecientes con el cuantil, en todas las secuencias.
                    _, punt = puntuaciones_por_escenario(estado, escalera, pred, bundle)
                    orden_total += 1
                    orden_ok += int(bool(np.all(np.diff(punt, axis=1) >= -1e-9)))
                    # Dispersion epistemica (desviacion de las medianas de los 5 miembros, horizonte 1) y descenso del q10.
                    sigma = float(miembros[:, 0, 0, idx_med].std(unbiased=False))
                    sigmas_h1.append(sigma)
                    descensos_q10.append(1.0 - math.exp(-0.8 * sigma))
                    registro["sigma_h1"] = sigma
                if (ejemplo is None and sesion["id_ventana_traza"] == EJEMPLO_VENTANA
                        and sesion["id_perfil_video"] == EJEMPLO_VIDEO and int(fila["indice_segmento"]) == EJEMPLO_SEGMENTO):
                    miembros = CAPTURA["predicciones_miembros"]
                    sin_ens = _combinar_original(miembros, cuantiles, ensanchado_cola=0.0)[0]
                    base = media_armonica_bps(estado.historial_throughput_bps)
                    secuencias, punt = puntuaciones_por_escenario(estado, escalera, pred, bundle)
                    cvar = plan_mod._cvar(punt, bundle.alfa_riesgo)
                    mejor = int(np.argmax(cvar))
                    mejor_med = int(np.argmax(punt[:, idx_med]))
                    ejemplo = {
                        "sesion": sesion["id_sesion"], "segmento": int(fila["indice_segmento"]), "nivel": nivel,
                        "nivel_previo": nivel_previo, "registrado": int(fila["nivel_elegido_politica"]),
                        "buffer_s": float(fb["tiempo_en_cola"]), "historial_bps": list(estado.historial_throughput_bps),
                        "media_armonica_bps": base, "pred_bps": [list(f) for f in pred],
                        "pred_sin_ensanchado_bps": [list(f) for f in filas_log_ratio_a_bps(sin_ens, base, bundle.horizonte_segmentos, len(cuantiles))],
                        "sigma_medianas": [float(miembros[:, 0, h, idx_med].std(unbiased=False)) for h in range(bundle.horizonte_segmentos)],
                        "cuantiles": list(cuantiles), "alfa": float(bundle.alfa_riesgo),
                        "mejor_cvar": {"secuencia": [int(v) for v in secuencias[mejor]], "puntuaciones": [float(v) for v in punt[mejor]], "cvar": float(cvar[mejor])},
                        "mejor_mediana": {"secuencia": [int(v) for v in secuencias[mejor_med]], "puntuaciones": [float(v) for v in punt[mejor_med]], "cvar": float(cvar[mejor_med])},
                        "bitrates_kbps": [b / 1000 for b in escalera.bitrates_bps],
                        "tamanos_bytes_siguientes": [[int(escalera.bytes_segmento(n, estado.indice_segmento + p)) for p in range(bundle.horizonte_segmentos)] for n in range(escalera.num_representaciones)],
                        "throughput_siguiente_bps": None,
                    }
                salida.write(json.dumps(registro) + "\n")
                nivel_previo = nivel
            # throughput medido en la descarga siguiente al ejemplo
            if ejemplo is not None and ejemplo["sesion"] == sesion["id_sesion"] and ejemplo["throughput_siguiente_bps"] is None:
                for fila in filas:
                    if fila["es_init"] == "0" and int(fila["indice_segmento"]) == EJEMPLO_SEGMENTO + 1:
                        ejemplo["throughput_siguiente_bps"] = 8.0 * float(fila["feedback_tamano_ultimo_fragmento"]) / float(fila["feedback_tiempo_ultima_descarga"])
            print("{0:3d}/{1} {2} decisiones {3} iguales {4}".format(totales["sesiones"], len(sesiones), sesion["id_sesion"][:40], totales["decisiones"], totales["iguales"]), flush=True)

    parametros_miembro = sum(p.numel() for p in bundle_ref.miembros[0].parameters())
    inf = sorted(inferencias_ms)
    resumen = {
        "generado": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "paquete": str(PAQUETE), "torch": torch.__version__,
        "totales": totales,
        "cambios_sobre_mismo_estado_reales": cambios,
        "orden_puntuaciones": {"decisiones": orden_total, "no_decrecientes": orden_ok},
        "ensanchado": {
            "sigma_h1_mediana": statistics.median(sigmas_h1), "sigma_h1_p90": float(np.percentile(sigmas_h1, 90)), "sigma_h1_max": max(sigmas_h1),
            "descenso_q10_mediana_pct": 100 * statistics.median(descensos_q10), "descenso_q10_p90_pct": 100 * float(np.percentile(descensos_q10, 90)),
            "descenso_q10_max_pct": 100 * max(descensos_q10),
        },
        "inferencia_ms": {"media": statistics.mean(inf), "mediana": statistics.median(inf), "p99": float(np.percentile(inf, 99)), "max": max(inf)},
        "parametros_por_miembro": int(parametros_miembro), "parametros_total": int(parametros_miembro * len(bundle_ref.miembros)),
        "miembros": len(bundle_ref.miembros),
        "ejemplo": ejemplo,
        "duracion_s": time.perf_counter() - inicio,
    }
    SALIDA_RESUMEN.write_text(json.dumps(resumen, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in resumen.items() if k != "ejemplo"}, indent=1, ensure_ascii=True))


if __name__ == "__main__":
    main()
