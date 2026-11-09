# -*- coding: utf-8 -*-
"""Calibracion del predictor entregado sobre el conjunto de validacion del dataset entregado.

Carga el bundle de 03_modelos y datos_validacion.jsonl de 06_dataset_entrenamiento, y calcula:
cobertura empirica por cuantil (fraccion de etiquetas por debajo de cada cuantil predicho), por
horizonte y global, con y sin ensanchado epistemico; perdida pinball media; desacuerdo medio del
ensemble; y el numero de muestras. Es la misma comprobacion que hace el entrenador al final
(entrenamiento_modelo._calibracion_ensemble), reproducida sobre el material entregado.

Uso:  py -3.12 docs/memoria/apoyo/calibracion_validacion.py
Salida: docs/memoria/apoyo/calibracion_validacion.json
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
BUNDLE = TFG_MATERIAL / "03_modelos" / "modelo_propio" / "bundle"
DATASET = TFG_MATERIAL / "06_dataset_entrenamiento" / "dataset_entrenamiento"
SALIDA = Path(__file__).resolve().parent / "calibracion_validacion.json"
sys.dont_write_bytecode = True
sys.path.insert(0, str(CODIGO))

import torch  # noqa: E402

from core.modelo_propio.bundle import cargar_bundle  # noqa: E402
from core.modelo_propio.modelo import NOMBRES_FEATURES_ESCALARES, combinar_cuantiles_ensemble  # noqa: E402
from entrenamiento.entrenamiento_modelo import perdida_pinball  # noqa: E402


def main():
    inicio = time.perf_counter()
    bundle = cargar_bundle(BUNDLE)
    cuantiles = bundle.cuantiles
    H = bundle.horizonte_segmentos
    secuencias, escalares, objetivos = [], [], []
    por_politica = {}
    with (DATASET / "datos_validacion.jsonl").open(encoding="utf-8") as f:
        for linea in f:
            m = json.loads(linea)
            c = m["entradas_modelo"]["contexto"]
            tp = [float(v) for v in c["historial_throughput_bps"]]
            dt = [float(v) for v in c["historial_tiempo_descarga_s"]]
            secuencias.append([[math.log1p(max(tp[i], 0.0)), dt[i]] for i in range(len(tp))])
            escalares.append([float(c.get(n, 0.0) or 0.0) for n in NOMBRES_FEATURES_ESCALARES])
            objetivos.append([float(v) for v in m["objetivos_cuantiles_throughput"]["log_ratio_objetivo_por_horizonte"]])
            pol = m["metadatos"]["politica_rollout"]
            por_politica[pol] = por_politica.get(pol, 0) + 1
    n = len(objetivos)
    ms, ds = bundle._media_secuencia, bundle._desviacion_secuencia
    me, de = bundle._media_escalares, bundle._desviacion_escalares
    X = torch.tensor([[[(p[f] - ms[f]) / max(ds[f], 1e-9) for f in range(2)] for p in s] for s in secuencias], dtype=torch.float32)
    E = torch.tensor([[(e[j] - me[j]) / max(de[j], 1e-9) for j in range(len(e))] for e in escalares], dtype=torch.float32)
    Y = torch.tensor(objetivos, dtype=torch.float32)
    with torch.no_grad():
        preds = []
        for i in range(0, n, 8192):
            preds.append(torch.stack([mod(X[i:i + 8192], E[i:i + 8192]) for mod in bundle.miembros], dim=0))
        P = torch.cat(preds, dim=1)  # [M, N, H, Q]
        comb = combinar_cuantiles_ensemble(P, cuantiles, ensanchado_cola=bundle.ensanchado_cola)
        comb_sin = combinar_cuantiles_ensemble(P, cuantiles, ensanchado_cola=0.0)
        idx_med = min(range(len(cuantiles)), key=lambda i: abs(cuantiles[i] - 0.5))
        sigma = P[:, :, :, idx_med].std(dim=0, unbiased=False)

        def cobertura(c):
            bajo = (Y.unsqueeze(2) <= c).float()
            return {
                "global": [round(float(v), 4) for v in bajo.mean(dim=(0, 1))],
                "por_horizonte": [[round(float(v), 4) for v in bajo[:, h, :].mean(dim=0)] for h in range(H)],
            }

        res = {
            "generado": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "num_muestras_validacion": n,
            "por_politica_rollout": por_politica,
            "cuantiles": list(cuantiles), "horizonte": H, "ensanchado_cola": bundle.ensanchado_cola,
            "cobertura_con_ensanchado": cobertura(comb),
            "cobertura_sin_ensanchado": cobertura(comb_sin),
            "pinball_media": round(float(perdida_pinball(comb, Y, cuantiles)), 5),
            "pinball_media_sin_ensanchado": round(float(perdida_pinball(comb_sin, Y, cuantiles)), 5),
            "pinball_por_miembro": [round(float(perdida_pinball(P[m], Y, cuantiles)), 5) for m in range(P.shape[0])],
            "desacuerdo_epistemico_medio": round(float(sigma.mean()), 5),
            "desacuerdo_epistemico_p90": round(float(sigma.flatten().quantile(0.9)), 5),
            "error_abs_max_cobertura": round(max(abs(float(c) - q) for c, q in zip(cobertura(comb)["global"], cuantiles)), 4),
            "duracion_s": round(time.perf_counter() - inicio, 1),
        }
    SALIDA.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
