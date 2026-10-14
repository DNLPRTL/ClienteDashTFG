"""Resumen rapido de un banco del simulador: medias por controlador y diferencias pareadas."""
from __future__ import annotations

import json
import random
import statistics as st
import sys
from collections import defaultdict


def cargar(ruta):
    return json.load(open(ruta, encoding="utf-8"))["sesiones"]


def por_escenario(filas):
    esc = defaultdict(dict)
    for f in filas:
        if not f.get("error"):
            esc[(f["id_traza"], f["video"])][f["alias"]] = f
    return esc


def bootstrap_cluster(difs_por_ventana, n=4000, semilla=1):
    # IC95 de la media de las diferencias, remuestreando ventanas (cada una con sus videos).
    rng = random.Random(semilla)
    claves = list(difs_por_ventana)
    medias = []
    for _ in range(n):
        muestra = [difs_por_ventana[rng.choice(claves)] for _ in claves]
        valores = [x for grupo in muestra for x in grupo]
        medias.append(sum(valores) / len(valores))
    medias.sort()
    return medias[int(0.025 * n)], medias[int(0.975 * n)], medias[int(0.05 * n)], medias[int(0.95 * n)]


def comparar(filas, a, b, metrica="qoe_lineal_media"):
    esc = por_escenario(filas)
    difs, por_ventana = [], defaultdict(list)
    for (traza, _video), v in esc.items():
        if a in v and b in v:
            d = v[a][metrica] - v[b][metrica]
            difs.append(d)
            por_ventana[traza].append(d)
    if not difs:
        return None
    lo, hi, lo90, hi90 = bootstrap_cluster(por_ventana)
    medias_ventana = [sum(x) / len(x) for x in por_ventana.values()]
    return {
        "n": len(difs), "ventanas": len(por_ventana), "media": st.mean(difs), "sd": st.stdev(difs),
        "sd_ventana": st.stdev(medias_ventana), "empates": sum(1 for d in difs if abs(d) < 1e-9),
        "gana": sum(1 for d in difs if d > 1e-9), "pierde": sum(1 for d in difs if d < -1e-9),
        "ic95": (lo, hi), "ic90": (lo90, hi90),
    }


def main():
    filas = cargar(sys.argv[1])
    ref = sys.argv[2] if len(sys.argv) > 2 else "controlador_propio"
    por_ctrl = defaultdict(list)
    for f in filas:
        if not f.get("error"):
            por_ctrl[f["alias"]].append(f)
    print("%-28s %5s %8s %8s %9s %8s %7s" % ("controlador", "n", "QoE", "bitrate", "rebuf_s", "paradas", ">5s%"))
    for c, v in sorted(por_ctrl.items(), key=lambda kv: -st.mean(x["qoe_lineal_media"] for x in kv[1])):
        print("%-28s %5d %8.3f %8.0f %9.2f %8.2f %7.1f" % (
            c, len(v), st.mean(x["qoe_lineal_media"] for x in v), st.mean(x["bitrate_medio_kbps"] for x in v),
            st.mean(x["rebuffering_total_s"] for x in v), st.mean(x["num_stalls"] for x in v),
            100 * sum(1 for x in v if x["rebuffering_total_s"] > 5) / len(v)))
    print("\nPareadas %s - otro (escenario = ventana x video; IC por bootstrap de ventanas)" % ref)
    for c in sorted(por_ctrl):
        if c == ref:
            continue
        r = comparar(filas, ref, c)
        if r:
            print("  vs %-24s n=%4d D=%+.3f IC95[%+.3f,%+.3f] IC90[%+.3f,%+.3f] sd=%.3f sd_v=%.3f G/P/E=%d/%d/%d" % (
                c, r["n"], r["media"], r["ic95"][0], r["ic95"][1], r["ic90"][0], r["ic90"][1], r["sd"], r["sd_ventana"],
                r["gana"], r["pierde"], r["empates"]))
        r2 = comparar(filas, ref, c, "rebuffering_total_s")
        if r2:
            print("     rebuffering D=%+.2f s IC95[%+.2f,%+.2f]" % (r2["media"], r2["ic95"][0], r2["ic95"][1]))


if __name__ == "__main__":
    main()
