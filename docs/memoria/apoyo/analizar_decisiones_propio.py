"""Resume las decisiones reproducidas del controlador propio (apartado 5.6.4).

Entrada: decisiones_propio.jsonl, generado por reproducir_decisiones_propio.py en
C:/Users/danie/Documents/TFG/apoyo_memoria/.
Salida: resumen_decisiones_propio.json (junto a este script; es la fuente de los
numeros de la Tabla 5.7 y del ejemplo de la Figura 5.3) y ejemplo_decision.json
en la carpeta de apoyo (lo lee generar_fig_5_3.py).

Regla del ejemplo, fijada antes de mirar el desenlace: primera decision, en el
orden del experimento, de una sesion con traza REAL, buffer entre 8 y 30 s, en la
que el criterio CVaR y el escenario central eligen primeras acciones distintas,
ambas dentro de la mitad alta de la escalera (nivel >= 3, es decir >= 1850 kbit/s).
"""
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

DATOS = Path(r"C:\Users\danie\Documents\TFG\apoyo_memoria")
AQUI = Path(__file__).resolve().parent

filas = [json.loads(linea) for linea in (DATOS / "decisiones_propio.jsonl").open(encoding="utf-8")]
VARIANTES = ("central", "peor", "media4", "nominal", "sin_ensanchado", "progreso_sesion")


def resumir(rs):
    d = len(rs)
    salida = {
        "decisiones": d,
        "reproduccion_exacta": sum(r["accion_repro"] == r["accion_log"] for r in rs),
        "puntuaciones_ordenadas_por_cuantil": sum(r["monotono"] for r in rs),
        "variantes": {},
    }
    for alt in VARIANTES:
        difiere = [r for r in rs if r["primera"][alt] != r["primera"]["cvar"]]
        salida["variantes"][alt] = {
            "decisiones_con_otra_accion": len(difiere),
            "porcentaje": round(100.0 * len(difiere) / d, 2) if d else 0.0,
            "cvar_mas_bajo": sum(r["primera"]["cvar"] < r["primera"][alt] for r in difiere),
            "cvar_mas_alto": sum(r["primera"]["cvar"] > r["primera"][alt] for r in difiere),
        }
    sig = np.array([np.mean(r["sigma_log"]) for r in rs])
    salida["sigma_epistemica"] = {
        "mediana": float(np.median(sig)),
        "p90": float(np.percentile(sig, 90)),
        "maximo": float(sig.max()),
        "factor_q10_mediana": math.exp(-0.8 * float(np.median(sig))),
        "factor_q10_p90": math.exp(-0.8 * float(np.percentile(sig, 90))),
        "factor_q10_maximo": math.exp(-0.8 * float(sig.max())),
    }
    ratios = [r["tam_real_sig_B"][r["primera"]["cvar"]] / r["tam_nom_sig_B"][r["primera"]["cvar"]] for r in rs]
    salida["tamano_real_sobre_nominal_siguiente"] = {
        "minimo": float(min(ratios)),
        "mediana": float(np.median(ratios)),
        "maximo": float(max(ratios)),
    }
    salida["niveles_elegidos"] = dict(sorted(Counter(r["primera"]["cvar"] for r in rs).items()))
    return salida


reales = [r for r in filas if r["real"]]
sinteticas = [r for r in filas if not r["real"]]
candidatas = [
    r for r in reales
    if 8.0 <= r["buffer_s"] <= 30.0
    and r["primera"]["cvar"] != r["primera"]["central"]
    and min(r["primera"]["cvar"], r["primera"]["central"]) >= 3
]
ejemplo = candidatas[0]
(DATOS / "ejemplo_decision.json").write_text(json.dumps(ejemplo, indent=2), encoding="utf-8")

resumen = {
    "fuente": "telemetria del paquete 20260810_133520_tfg_final reproducida con el bundle de 03_modelos",
    "reales": resumir(reales),
    "sinteticas": resumir(sinteticas),
    "ejemplo": {
        "regla": "primera decision real, buffer 8-30 s, CVaR y central distintos, ambos nivel >= 3",
        "candidatas_que_cumplen_la_regla": len(candidatas),
        "sesion": ejemplo["sesion"],
        "k": ejemplo["k"],
        "buffer_s": ejemplo["buffer_s"],
        "nivel_previo": ejemplo["nivel_previo"],
        "historial_tp_mbps": [v / 1e6 for v in ejemplo["historial_tp_bps"]],
        "base_mbps": ejemplo["base_bps"] / 1e6,
        "pred_mbps_h1": [v / 1e6 for v in ejemplo["pred_bps"][0]],
        "pred_sin_ensanchado_mbps_h1": [v / 1e6 for v in ejemplo["pred_sin_ensanchado_bps"][0]],
        "secuencia_cvar": ejemplo["sec_cvar"],
        "secuencia_central": ejemplo["sec_central"],
        "puntos_secuencia_cvar": ejemplo["puntos_cvar_sec"],
        "puntos_secuencia_central": ejemplo["puntos_central_sec"],
        "rebuffer_secuencia_central_s": ejemplo["rebuf_central_sec"],
        "cvar_secuencia_cvar": ejemplo["cvar_de_cvar"],
        "cvar_secuencia_central": ejemplo["cvar_de_central"],
        "tam_real_sobre_nominal_siguiente": [a / b for a, b in zip(ejemplo["tam_real_sig_B"], ejemplo["tam_nom_sig_B"])],
        "primera_accion_por_criterio": ejemplo["primera"],
        "throughput_medido_despues_mbps": ejemplo["tp_siguiente_bps"] / 1e6,
    },
}
(AQUI / "resumen_decisiones_propio.json").write_text(json.dumps(resumen, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({"reales": resumen["reales"]["variantes"], "ejemplo": resumen["ejemplo"]["sesion"], "k": resumen["ejemplo"]["k"]}, indent=1))
