"""Calidad y calibracion del predictor sobre el dataset de validacion (fase de blindaje, D3).

Para cada horizonte h y cuantil tau, en el espacio de salida de la red (log del throughput futuro
entre la media armonica de las ultimas descargas):
- cobertura empirica P(y <= q) y perdida pinball;
- red tal como decide (ensemble con ensanchado de la cola), red sin ensanchado, cuantiles fijos
  (los del dataset de entrenamiento) y cuantiles de las ultimas descargas;
- R1(tau) de Koenker y Machado (1999): 1 - pinball(red) / pinball(cuantiles fijos);
- recalibracion conformal: desplazamiento s(h, tau) = cuantil tau de (y - q) en la mitad A de la
  validacion (por grupo de captura), y su efecto en la cobertura de la mitad B.

Uso: python calibracion_predictor.py --salida informe.json [--recalibracion desplazamientos.json]
Solo muestras con historial no vacio, como decide el controlador. No va a la memoria tal cual.
"""
from __future__ import annotations

import argparse
import json
import math

import numpy as np
import torch

import simulador as sim  # noqa: F401  (anade el codigo entregado al path)
import ventanas as ven
from core.modelo_propio.bundle import RATIO_LOG_MAX, RATIO_LOG_MIN, BundleModelo
from core.modelo_propio.estado_sesion import media_armonica_bps
from core.modelo_propio.modelo import combinar_cuantiles_ensemble

RUTA_VALIDACION = r"C:\Users\danie\Documents\TFG Material\06_dataset_entrenamiento\dataset_entrenamiento\datos_validacion.jsonl"
RUTA_FIJOS = r"C:\Users\danie\Documents\TFG Material\03_modelos\cuantiles_fijos\cuantiles_fijos.json"
NOMBRES_DATASET = (
    "buffer_s",
    "indice_ultima_representacion",
    "ultimo_bitrate_bps",
    "rebuffering_reciente_s",
    "cambio_reciente_abs",
    "segmentos_restantes_norm",
    "hay_segmentos_restantes",
)


def leer_validacion(ruta: str):
    secuencias, escalares, objetivos, grupos, historiales = [], [], [], [], []
    with open(ruta, encoding="utf-8") as fichero:
        for linea in fichero:
            m = json.loads(linea)
            ctx = m["entradas_modelo"]["contexto"]
            tp = [float(v) for v in ctx["historial_throughput_bps"]]
            if not any(v > 0 for v in tp):
                continue
            dt = [float(v) for v in ctx["historial_tiempo_descarga_s"]]
            secuencias.append([[math.log1p(max(a, 0.0)), b] for a, b in zip(tp, dt)])
            escalares.append([float(ctx[n]) for n in NOMBRES_DATASET])
            objetivos.append([float(v) for v in m["objetivos_cuantiles_throughput"]["log_ratio_objetivo_por_horizonte"]])
            grupos.append(m["metadatos"]["grupo_fuga"])
            historiales.append([v for v in tp if v > 0])
    return np.array(secuencias), np.array(escalares), np.array(objetivos), grupos, historiales


def predecir_lote(bundle: BundleModelo, secuencias, escalares, ensanchado: float):
    sec = (secuencias - np.array(bundle._media_secuencia)) / np.maximum(np.array(bundle._desviacion_secuencia), 1e-9)
    esc = (escalares - np.array(bundle._media_escalares)) / np.maximum(np.array(bundle._desviacion_escalares), 1e-9)
    salidas = []
    with torch.no_grad():
        for inicio in range(0, len(sec), 8192):
            s = torch.tensor(sec[inicio:inicio + 8192], dtype=torch.float32)
            e = torch.tensor(esc[inicio:inicio + 8192], dtype=torch.float32)
            pred = torch.stack([m(s, e) for m in bundle.miembros], dim=0)
            salidas.append(combinar_cuantiles_ensemble(pred, bundle.cuantiles, ensanchado_cola=ensanchado).numpy())
    return np.clip(np.concatenate(salidas, axis=0), RATIO_LOG_MIN, RATIO_LOG_MAX)


def recientes(historiales, cuantiles, horizonte):
    filas = []
    for h in historiales:
        base = media_armonica_bps(h)
        q = np.log(np.maximum(np.quantile(h, cuantiles), 1.0) / base)
        filas.append(np.tile(np.sort(q), (horizonte, 1)))
    return np.clip(np.array(filas), RATIO_LOG_MIN, RATIO_LOG_MAX)


def metricas(pred, y, cuantiles):
    # pred [N, H, Q], y [N, H] -> cobertura y pinball [H, Q]
    dif = y[:, :, None] - pred
    tau = np.array(cuantiles)[None, None, :]
    pinball = np.maximum(tau * dif, (tau - 1.0) * dif).mean(axis=0)
    cobertura = (dif <= 0).mean(axis=0)
    return cobertura, pinball


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--salida", required=True)
    p.add_argument("--recalibracion", default="")
    args = p.parse_args()

    bundle = BundleModelo(sim.DIR_BUNDLE_WINDOWS)
    cuantiles = list(bundle.cuantiles)
    H = bundle.horizonte_segmentos
    secuencias, escalares, y, grupos, historiales = leer_validacion(RUTA_VALIDACION)
    mitades = np.array([ven.mitad_validacion(g) for g in grupos])
    fijos = np.array(json.load(open(RUTA_FIJOS, encoding="utf-8"))["valores_log_ratio_por_horizonte_y_cuantil"])

    predictores = {
        "red": predecir_lote(bundle, secuencias, escalares, bundle.ensanchado_cola),
        "red_sin_ensanchado": predecir_lote(bundle, secuencias, escalares, 0.0),
        "cuantiles_fijos": np.clip(np.broadcast_to(fijos, (len(y), H, len(cuantiles))), RATIO_LOG_MIN, RATIO_LOG_MAX),
        "cuantiles_recientes": recientes(historiales, cuantiles, H),
    }
    informe = {"muestras": int(len(y)), "cuantiles": cuantiles, "por_predictor": {}}
    for nombre, pred in predictores.items():
        cob, pin = metricas(pred, y, cuantiles)
        informe["por_predictor"][nombre] = {"cobertura": cob.round(4).tolist(), "pinball": pin.round(5).tolist(),
                                            "pinball_medio": float(pin.mean())}
    pin_red = np.array(informe["por_predictor"]["red"]["pinball"])
    pin_fij = np.array(informe["por_predictor"]["cuantiles_fijos"]["pinball"])
    pin_rec = np.array(informe["por_predictor"]["cuantiles_recientes"]["pinball"])
    informe["R1_frente_a_fijos"] = (1.0 - pin_red / pin_fij).round(4).tolist()
    informe["R1_frente_a_recientes"] = (1.0 - pin_red / pin_rec).round(4).tolist()

    # Recalibracion conformal con la mitad A, evaluada en la mitad B.
    red = predictores["red"]
    a, b = mitades == "A", mitades == "B"
    desplazamientos = np.zeros((H, len(cuantiles)))
    for h in range(H):
        for k, tau in enumerate(cuantiles):
            desplazamientos[h, k] = float(np.quantile(y[a, h] - red[a, h, k], tau))
    recal = np.clip(red + desplazamientos[None], RATIO_LOG_MIN, RATIO_LOG_MAX)
    cob_b, pin_b = metricas(red[b], y[b], cuantiles)
    cob_br, pin_br = metricas(np.sort(recal[b], axis=2), y[b], cuantiles)
    informe["recalibracion"] = {
        "muestras_A": int(a.sum()), "muestras_B": int(b.sum()),
        "desplazamientos": desplazamientos.round(5).tolist(),
        "cobertura_B_antes": cob_b.round(4).tolist(), "cobertura_B_despues": cob_br.round(4).tolist(),
        "pinball_B_antes": float(pin_b.mean()), "pinball_B_despues": float(pin_br.mean()),
    }
    with open(args.salida, "w", encoding="utf-8") as fichero:
        json.dump(informe, fichero, indent=1)
    if args.recalibracion:
        with open(args.recalibracion, "w", encoding="utf-8") as fichero:
            json.dump({"id_esquema": "recalibracion_conformal_v1", "cuantiles": cuantiles, "horizonte_segmentos": H,
                       "desplazamientos_log_ratio_por_horizonte_y_cuantil": desplazamientos.tolist(),
                       "origen": "mitad A de la validacion por grupo de captura"}, fichero, indent=2)

    def fmt(m):
        return " | ".join(" ".join("%5.1f" % (100 * v) for v in fila) for fila in m)

    print("muestras", len(y), "(A %d, B %d)" % (a.sum(), b.sum()))
    for nombre, d in informe["por_predictor"].items():
        print("%-20s cobertura%% h1..h5 [q10 q25 q50 q75]: %s | pinball medio %.5f" % (nombre, fmt(d["cobertura"]), d["pinball_medio"]))
    print("R1 frente a fijos (por h, media en tau):", [round(float(np.mean(f)), 3) for f in informe["R1_frente_a_fijos"]])
    print("R1 frente a recientes (por h, media en tau):", [round(float(np.mean(f)), 3) for f in informe["R1_frente_a_recientes"]])
    r = informe["recalibracion"]
    print("recalibracion, cobertura en B antes:", fmt(r["cobertura_B_antes"]))
    print("recalibracion, cobertura en B despues:", fmt(r["cobertura_B_despues"]))
    print("pinball B antes %.5f despues %.5f" % (r["pinball_B_antes"], r["pinball_B_despues"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
