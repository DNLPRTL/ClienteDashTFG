"""Ventanas relevantes para las pruebas previas (fase de blindaje).

Mismo criterio que se propone para el experimento final, pero sobre la particion de
validacion (`test` en el catalogo):
- trazas reales de la particion, de al menos `duracion_s`, y su ventana con el inicio de
  core/evaluacion/seleccion.py (misma semilla);
- filtro de Pensieve (Mao et al., 2017, sec. 5.1) calculado sobre la propia ventana: throughput
  medio < 6 Mbit/s y minimo > 0,2 Mbit/s, para evitar ventanas donde elegir siempre el maximo es
  lo optimo o donde la red no sostiene ningun nivel;
- sin los grupos de captura excluidos (los ya usados en desarrollo) cuando se pide.
"""
from __future__ import annotations

import csv
import json
from typing import Any, Dict, Iterable, List, Mapping

import simulador as sim  # noqa: F401  (anade el codigo entregado al path)
from core.evaluacion.seleccion import _inicio_ventana_para_traza, es_traza_sintetica, tramo_dificultad

RUTA_CATALOGO = r"C:\Users\danie\Documents\TFG Material\02_corpus_red\catalogo_trazas.json"
MEDIA_MAX_KBPS = 6000.0
MINIMO_MIN_KBPS = 200.0


def mitad_validacion(grupo_fuga: str) -> str:
    # Particion fija de las ventanas de validacion en dos mitades por grupo de captura: en la A
    # se elige un ajuste, en la B se confirma (criterio D7 del plan).
    import zlib

    return "A" if zlib.crc32(str(grupo_fuga).encode("utf-8")) % 2 == 0 else "B"


def cargar_catalogo(ruta: str = RUTA_CATALOGO) -> Mapping[str, Any]:
    with open(ruta, encoding="utf-8") as fichero:
        return json.load(fichero)


def estadisticas_ventana(ruta_traza: str, inicio_s: float, duracion_s: float) -> Dict[str, float]:
    traza = sim.traza_ventana(ruta_traza, float(inicio_s), float(duracion_s))
    total = sum(m.duracion_s for m in traza.muestras)
    media = sum(m.throughput_kbps * m.duracion_s for m in traza.muestras) / total if total > 0 else 0.0
    return {
        "media_kbps": media,
        "min_kbps": min(m.throughput_kbps for m in traza.muestras),
        "max_kbps": max(m.throughput_kbps for m in traza.muestras),
        "duracion_cubierta_s": total,
    }


def ventanas_relevantes(
    catalogo: Mapping[str, Any],
    *,
    particion: str = "test",
    duracion_s: float = 160.0,
    semilla: int = 606,
    grupos_excluidos: Iterable[str] = (),
) -> List[Dict[str, Any]]:
    excluidos = set(grupos_excluidos)
    salida = []
    for traza in catalogo["trazas"]:
        if traza.get("particion") != particion or es_traza_sintetica(traza):
            continue
        if traza.get("usable_en_eval", True) is False or float(traza.get("duracion_s", 0) or 0) < duracion_s:
            continue
        if str(traza.get("grupo_fuga", "")) in excluidos:
            continue
        inicio = _inicio_ventana_para_traza(traza, semilla=semilla, duracion_ventana_s=duracion_s, decision_interval_s=4.0)
        est = estadisticas_ventana(traza["ruta_traza_normalizada"], inicio, duracion_s)
        if not (est["media_kbps"] < MEDIA_MAX_KBPS and est["min_kbps"] > MINIMO_MIN_KBPS):
            continue
        salida.append(
            {
                "id_traza": traza["id_traza"],
                "id_dataset": traza["id_dataset"],
                "grupo_fuga": traza["grupo_fuga"],
                "ruta_traza_normalizada": traza["ruta_traza_normalizada"],
                "inicio_ventana_s": float(inicio),
                "duracion_ventana_s": float(duracion_s),
                "tramo_dificultad_traza": tramo_dificultad(traza),
                **{k: round(v, 3) for k, v in est.items()},
            }
        )
    salida.sort(key=lambda v: v["id_traza"])
    return salida


def escribir_csv(ventanas: List[Dict[str, Any]], ruta: str) -> None:
    with open(ruta, "w", newline="", encoding="utf-8") as fichero:
        escritor = csv.DictWriter(fichero, fieldnames=list(ventanas[0].keys()))
        escritor.writeheader()
        escritor.writerows(ventanas)


if __name__ == "__main__":
    import sys
    from collections import Counter

    cat = cargar_catalogo()
    for particion in ("test", "eval"):
        v = ventanas_relevantes(cat, particion=particion)
        print(particion, len(v), dict(Counter(x["id_dataset"].split("_")[0] for x in v)),
              "| media < 450 kbps:", sum(1 for x in v if x["media_kbps"] < 450))
    if len(sys.argv) > 1:
        escribir_csv(ventanas_relevantes(cat, particion="test"), sys.argv[1])
