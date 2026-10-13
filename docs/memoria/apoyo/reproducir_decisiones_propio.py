"""Reproduce fuera de linea las decisiones del controlador propio del paquete canonico.

Para cada sesion del controlador propio: reinyecta, fila a fila, la realimentacion
registrada en la telemetria en un ControladorPropio nuevo (mismo bundle, mismo
descriptor de video), compara la accion con la registrada y evalua criterios
alternativos sobre el mismo estado (escenario central, peor caso, media de los 4,
tamanos nominales, sin ensanchado epistemico, progreso medido como en el
entrenamiento). Escribe un JSONL por decision y un resumen.
"""
from __future__ import annotations

import ast
import csv
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

CODE = Path(r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG")
BUNDLE = Path(r"C:\Users\danie\Documents\TFG Material\03_modelos\modelo_propio\bundle")
PKG = Path(r"C:\Users\danie\Documents\TFG Material\04_evidencia_final\20260810_133520_tfg_final")
OUT = Path(r"C:\Users\danie\Documents\TFG\apoyo_memoria")
OUT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(CODE))

import torch  # noqa: E402

from core.controladores.contrato import CLAVES_REALIMENTACION  # noqa: E402
from core.controladores.controlador_propio import ControladorPropio  # noqa: E402
from core.controladores.entradas_contexto import construir_entradas_contexto  # noqa: E402
from core.modelo_propio import bundle as bundle_mod  # noqa: E402
from core.modelo_propio.bundle import filas_log_ratio_a_bps  # noqa: E402
from core.modelo_propio.estado_sesion import media_armonica_bps  # noqa: E402
from core.modelo_propio.modelo import NOMBRES_FEATURES_ESCALARES, combinar_cuantiles_ensemble  # noqa: E402

CAPTURA: dict = {}
_predecir_original = bundle_mod.BundleModelo.predecir


def _predecir_capturando(self, estado, escalera):
    resultado = _predecir_original(self, estado, escalera)
    CAPTURA.update(estado=estado, escalera=escalera, pred=resultado, bundle=self)
    return resultado


bundle_mod.BundleModelo.predecir = _predecir_capturando

SECUENCIAS = np.array(list(itertools.product(range(6), repeat=5)), dtype=np.int64)
DURACION_S = 4.0
BUFFER_MAX_S = 60.0
PESO_REB = 4.3
PESO_CAMBIOS = 1.0


def parsear(valor: str):
    texto = (valor or "").strip()
    if texto == "":
        return None
    if texto.startswith("["):
        return ast.literal_eval(texto)
    try:
        return int(texto)
    except ValueError:
        pass
    try:
        return float(texto)
    except ValueError:
        return texto


class EscaleraProgresoSesion:
    """Vista de la escalera con num_segmentos de la sesion (31), como en el entrenamiento."""

    def __init__(self, base, num_segmentos):
        self._base = base
        self.num_segmentos = num_segmentos

    def bitrate_bps(self, indice):
        return self._base.bitrate_bps(indice)


def miembros_log_ratio(bundle, estado, escalera):
    contexto = construir_entradas_contexto(estado, escalera)
    historial_tp = [float(v) for v in (contexto.get("historial_throughput_bps") or [])]
    historial_dt = [float(v) for v in (contexto.get("historial_tiempo_descarga_s") or [])]
    longitud = min(len(historial_tp), len(historial_dt))
    if longitud <= 0:
        secuencia = [[0.0, 0.0]]
    else:
        secuencia = [[math.log1p(max(historial_tp[i], 0.0)), historial_dt[i]] for i in range(longitud)]
    secuencia_norm = [
        [
            (paso[f] - bundle._media_secuencia[f]) / max(bundle._desviacion_secuencia[f], 1.0e-9)
            for f in range(2)
        ]
        for paso in secuencia
    ]
    escalares = [float(contexto.get(nombre, 0.0) or 0.0) for nombre in NOMBRES_FEATURES_ESCALARES]
    escalares_norm = [
        (escalares[j] - bundle._media_escalares[j]) / max(bundle._desviacion_escalares[j], 1.0e-9)
        for j in range(len(escalares))
    ]
    t_seq = torch.tensor([secuencia_norm], dtype=torch.float32)
    t_esc = torch.tensor([escalares_norm], dtype=torch.float32)
    with torch.no_grad():
        return torch.stack([m(t_seq, t_esc) for m in bundle.miembros], dim=0)


def a_bps(combinadas, estado, bundle):
    tp_base = media_armonica_bps(estado.historial_throughput_bps)
    return np.array(
        filas_log_ratio_a_bps(combinadas, tp_base, bundle.horizonte_segmentos, len(bundle.cuantiles)),
        dtype=float,
    )


def puntuar(pred_bps, tamanos_B, bitrates_bps, buffer0_s, nivel_previo):
    n = len(SECUENCIAS)
    q = pred_bps.shape[1]
    puntos = np.zeros((n, q))
    rebuf = np.zeros((n, q))
    for k in range(q):
        buf = np.full(n, float(buffer0_s))
        previo = np.full(n, float(bitrates_bps[nivel_previo]))
        for h in range(5):
            a = SECUENCIAS[:, h]
            tp = max(float(pred_bps[h, k]), 1.0)
            t = 8.0 * tamanos_B[a, h] / tp
            r = np.maximum(t - buf, 0.0)
            cambio = np.abs(bitrates_bps[a] - previo) / 1_000_000.0
            puntos[:, k] += bitrates_bps[a] / 1_000_000.0 - PESO_REB * r - PESO_CAMBIOS * cambio
            rebuf[:, k] += r
            buf = np.minimum(np.maximum(buf - t, 0.0) + DURACION_S, BUFFER_MAX_S)
            previo = bitrates_bps[a]
    return puntos, rebuf


def cvar(puntos, alfa=0.75):
    m = max(1, int(math.ceil(alfa * puntos.shape[1])))
    return np.sort(puntos, axis=1)[:, :m].sum(axis=1) / float(m)


def main(max_sesiones=None):
    dir_ejec = PKG / "01_ejecucion" / "ejecuciones"
    sesiones = sorted(p.name for p in dir_ejec.iterdir() if "controlador_propio" in p.name)
    if max_sesiones:
        sesiones = sesiones[: int(max_sesiones)]
    salida = (OUT / "decisiones_propio.jsonl").open("w", encoding="utf-8")
    bundles_vistos, perfiles_vistos = set(), set()
    t0 = time.perf_counter()
    total = coincide_accion = coincide_nivel = 0
    for n_ses, sid in enumerate(sesiones, start=1):
        cfg = json.loads((PKG / "00_protocolo" / "configs_cliente" / f"{sid}.yaml").read_text(encoding="utf-8"))
        params = dict(cfg["controlador"]["parametros"])
        bundles_vistos.add(params.get("dir_bundle"))
        perfiles_vistos.add(params.get("id_perfil_video"))
        params["dir_bundle"] = str(BUNDLE)
        ctrl = ControladorPropio(**params)
        dir_run = next((dir_ejec / sid).iterdir())
        with (dir_run / "telemetria_segmentos.csv").open(encoding="utf-8", newline="") as fh:
            filas = list(csv.DictReader(fh))
        decisiones = [f for f in filas if (f.get("tasa_objetivo_politica") or "").strip() != ""]
        for i, fila in enumerate(decisiones):
            fb = {c: parsear(fila["feedback_" + c]) for c in CLAVES_REALIMENTACION}
            ctrl.fijarFeedbackReproductor(fb)
            CAPTURA.clear()
            tasa = ctrl.calcularAccionControl()
            nivel = min(ctrl.cuantizarTasa(tasa), int(fb["nivel_max"]))
            dec = ctrl.ultima_decision
            accion_log = parsear(fila["feedback_accion_bruta_red"])
            nivel_log = parsear(fila["nivel_elegido_politica"])
            total += 1
            coincide_accion += int(dec is not None and int(dec.accion) == int(accion_log))
            coincide_nivel += int(int(nivel) == int(nivel_log))

            estado, escalera, bundle = CAPTURA["estado"], CAPTURA["escalera"], CAPTURA["bundle"]
            pred = np.array(CAPTURA["pred"], dtype=float)
            k = int(estado.indice_segmento)
            bitrates = np.array(escalera.bitrates_bps, dtype=float)
            tam_real = np.array([[escalera.bytes_segmento(a, k + h) for h in range(5)] for a in range(6)], dtype=float)
            tam_nom = np.array([[max(1, int(round(bitrates[a] * DURACION_S / 8.0))) for h in range(5)] for a in range(6)], dtype=float)
            previo = int(estado.indice_ultima_representacion)

            puntos, rebuf = puntuar(pred, tam_real, bitrates, estado.buffer_s, previo)
            monotono = bool(np.all(np.diff(puntos, axis=1) >= -1e-9))
            idx_cvar = int(np.argmax(cvar(puntos)))
            idx_central = int(np.argmax(puntos[:, 2]))
            idx_peor = int(np.argmax(puntos[:, 0]))
            idx_media4 = int(np.argmax(puntos.mean(axis=1)))
            p_nom, _ = puntuar(pred, tam_nom, bitrates, estado.buffer_s, previo)
            idx_nominal = int(np.argmax(cvar(p_nom)))

            miembros = miembros_log_ratio(bundle, estado, escalera)
            sin_ens = a_bps(combinar_cuantiles_ensemble(miembros, bundle.cuantiles, ensanchado_cola=0.0)[0], estado, bundle)
            idx_sin_ens = int(np.argmax(cvar(puntuar(sin_ens, tam_real, bitrates, estado.buffer_s, previo)[0])))
            sigma = miembros[:, 0, :, 2].std(dim=0, unbiased=False).numpy().tolist()
            vista = EscaleraProgresoSesion(escalera, int(fb["segmentos_totales"]))
            m_ses = miembros_log_ratio(bundle, estado, vista)
            pred_ses = a_bps(combinar_cuantiles_ensemble(m_ses, bundle.cuantiles, ensanchado_cola=bundle.ensanchado_cola)[0], estado, bundle)
            idx_ses = int(np.argmax(cvar(puntuar(pred_ses, tam_real, bitrates, estado.buffer_s, previo)[0])))

            siguiente = decisiones[i + 1] if i + 1 < len(decisiones) else None
            tp_siguiente_bps = None
            if siguiente is not None:
                tam_s = parsear(siguiente["feedback_tamano_ultimo_fragmento"])
                t_s = parsear(siguiente["feedback_tiempo_ultima_descarga"])
                if tam_s and t_s:
                    tp_siguiente_bps = 8.0 * float(tam_s) / float(t_s)

            registro = {
                "sesion": sid,
                "real": "_real_" in sid,
                "perfil": params.get("id_perfil_video"),
                "k": k,
                "buffer_s": float(estado.buffer_s),
                "nivel_previo": previo,
                "historial_tp_bps": list(estado.historial_throughput_bps),
                "base_bps": float(media_armonica_bps(estado.historial_throughput_bps)),
                "pred_bps": pred.tolist(),
                "pred_sin_ensanchado_bps": sin_ens.tolist(),
                "sigma_log": sigma,
                "accion_log": int(accion_log),
                "nivel_log": int(nivel_log),
                "accion_repro": int(dec.accion) if dec is not None else None,
                "cvar_repro": float(dec.cvar_puntuacion) if dec is not None else None,
                "monotono": monotono,
                "sec_cvar": SECUENCIAS[idx_cvar].tolist(),
                "sec_central": SECUENCIAS[idx_central].tolist(),
                "sec_peor": SECUENCIAS[idx_peor].tolist(),
                "primera": {
                    "cvar": int(SECUENCIAS[idx_cvar, 0]),
                    "central": int(SECUENCIAS[idx_central, 0]),
                    "peor": int(SECUENCIAS[idx_peor, 0]),
                    "media4": int(SECUENCIAS[idx_media4, 0]),
                    "nominal": int(SECUENCIAS[idx_nominal, 0]),
                    "sin_ensanchado": int(SECUENCIAS[idx_sin_ens, 0]),
                    "progreso_sesion": int(SECUENCIAS[idx_ses, 0]),
                },
                "puntos_cvar_sec": puntos[idx_cvar].tolist(),
                "puntos_central_sec": puntos[idx_central].tolist(),
                "rebuf_cvar_sec": rebuf[idx_cvar].tolist(),
                "rebuf_central_sec": rebuf[idx_central].tolist(),
                "cvar_de_cvar": float(cvar(puntos)[idx_cvar]),
                "cvar_de_central": float(cvar(puntos)[idx_central]),
                "tam_real_sig_B": tam_real[:, 0].tolist(),
                "tam_nom_sig_B": tam_nom[:, 0].tolist(),
                "tp_siguiente_bps": tp_siguiente_bps,
            }
            salida.write(json.dumps(registro) + "\n")
        print(f"[{n_ses}/{len(sesiones)}] {sid} decisiones={len(decisiones)} t={time.perf_counter() - t0:.0f}s", flush=True)
    salida.close()
    resumen = {
        "decisiones": total,
        "coincide_accion_planificador": coincide_accion,
        "coincide_nivel_final": coincide_nivel,
        "bundles_en_configs": sorted(str(b) for b in bundles_vistos),
        "perfiles_en_configs": sorted(str(p) for p in perfiles_vistos),
        "torch": torch.__version__,
    }
    (OUT / "resumen_reproduccion.json").write_text(json.dumps(resumen, indent=2), encoding="utf-8")
    print(json.dumps(resumen, indent=2))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
