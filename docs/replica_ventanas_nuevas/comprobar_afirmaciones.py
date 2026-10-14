"""Comprueba las afirmaciones de AFIRMACIONES_A_COMPROBAR.md en un paquete de evaluacion.

Recalcula los agregados y la estadistica pareada a partir de 02_resultados/sesiones.csv
con las MISMAS funciones del analisis de entrega (core/evaluacion/analisis.py) y
comprueba antes que el recalculo coincide con lo que el paquete escribio. Opcionalmente
excluye un escenario (ventana|perfil) para el analisis de sensibilidad.

Uso: python comprobar_afirmaciones.py <paquete> [--excluir VENTANA|PERFIL] [--json salida.json]
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

CODIGO = Path(r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG")
sys.dont_write_bytecode = True
sys.path.insert(0, str(CODIGO))

from core.evaluacion.analisis import _bool, _int, agregar_resumenes, estadistica_pareada  # noqa: E402

PROPIO = "controlador_propio"
ROBUSTO = "mpc_robusto"


def convertir(valor: str):
    texto = (valor or "").strip()
    if texto in ("True", "False"):
        return texto == "True"
    try:
        numero = float(texto)
    except ValueError:
        return texto
    return int(numero) if numero.is_integer() and "." not in texto and "e" not in texto.lower() else numero


def leer_sesiones(paquete: Path):
    with (paquete / "02_resultados" / "sesiones.csv").open(encoding="utf-8", newline="") as fichero:
        return [{clave: convertir(valor) for clave, valor in fila.items()} for fila in csv.DictReader(fichero)]


def escenario(fila):
    return (fila["id_ventana_traza"], fila["id_perfil_video"], fila["repeticion"])


def victorias(resumenes, rival):
    """W/L/T del propio frente a rival por escenario real, con el criterio del test de signos."""
    por_escenario = {}
    for fila in resumenes:
        if not _int(fila.get("evaluables")) or _bool(fila.get("sintetica")):
            continue
        por_escenario.setdefault(escenario(fila), {})[fila["alias_controlador"]] = float(fila["qoe_lineal_media"])
    gana = pierde = empata = 0
    for valores in por_escenario.values():
        if PROPIO in valores and rival in valores:
            delta = valores[PROPIO] - valores[rival]
            gana += delta > 0
            pierde += delta < 0
            empata += delta == 0
    return gana, pierde, empata


def delta_pareado(estadistica, rival):
    """Delta propio - rival (media, IC95, p) desde la estadistica pareada del analisis."""
    for fila in estadistica["deltas_entre_controladores"]:
        if {fila["alias_izq"], fila["alias_der"]} == {PROPIO, rival}:
            signo = 1.0 if fila["alias_izq"] == PROPIO else -1.0
            limites = sorted([signo * fila["delta_izq_menos_der_ic95_inf"], signo * fila["delta_izq_menos_der_ic95_sup"]])
            return {
                "media": signo * fila["delta_izq_menos_der_media"],
                "ic95": limites,
                "p_signo": fila["p_valor_test_signo"],
                "n": fila["num_emparejadas"],
            }
    raise KeyError(rival)


def comprobar(resumenes):
    agregados = {fila["alias_controlador"]: fila for fila in agregar_resumenes(resumenes)}
    estadistica = estadistica_pareada(resumenes)
    rivales = [alias for alias in agregados if alias != PROPIO]
    deltas = {rival: delta_pareado(estadistica, rival) for rival in rivales}
    wlt = {rival: victorias(resumenes, rival) for rival in rivales}
    propio, robusto = agregados[PROPIO], agregados[ROBUSTO]
    mejor_media = max(agregados.values(), key=lambda fila: fila["qoe_lineal_media"])["alias_controlador"]

    def significativa_a_favor(rival):
        return deltas[rival]["p_signo"] < 0.05 and wlt[rival][0] > wlt[rival][1]

    d_rob = deltas[ROBUSTO]
    afirmaciones = {
        "1_qoe_media_mas_alta": mejor_media == PROPIO,
        "2_empate_con_robusto": d_rob["ic95"][0] <= 0.0 <= d_rob["ic95"][1] and d_rob["p_signo"] >= 0.05,
        "3_mejor_que_bba_y_bola": significativa_a_favor("bba") and significativa_a_favor("bola"),
        "4_mejor_que_basado_en_tasa_signo": significativa_a_favor("basado_en_tasa"),
        "5_menos_paradas_y_sesiones_gt5s_que_robusto": (
            propio["num_stalls_media"] < robusto["num_stalls_media"]
            and propio["proporcion_sesiones_rebuffering_gt5s"] < robusto["proporcion_sesiones_rebuffering_gt5s"]
        ),
        "6_sin_respaldo_y_auditado": propio["num_filas_respaldo"] == 0 and propio["num_filas_sin_auditoria_red"] == 0,
    }
    return agregados, estadistica, deltas, wlt, afirmaciones


def validar_recalculo(paquete: Path, agregados, estadistica):
    escritos = json.loads((paquete / "02_resultados" / "agregados_por_controlador.json").read_text(encoding="utf-8"))
    estad_escrita = json.loads((paquete / "02_resultados" / "estadistica.json").read_text(encoding="utf-8"))
    iguales = all(
        math.isclose(fila["qoe_lineal_media"], agregados[fila["alias_controlador"]]["qoe_lineal_media"], rel_tol=1e-12)
        and math.isclose(fila["qoe_lineal_ic95_inf"], agregados[fila["alias_controlador"]]["qoe_lineal_ic95_inf"], rel_tol=1e-12)
        and math.isclose(fila["num_stalls_media"], agregados[fila["alias_controlador"]]["num_stalls_media"], rel_tol=1e-12)
        for fila in escritos
    )
    clave = lambda fila: (fila["alias_izq"], fila["alias_der"])  # noqa: E731
    recalc = {clave(fila): fila for fila in estadistica["deltas_entre_controladores"]}
    iguales = iguales and all(
        math.isclose(fila["delta_izq_menos_der_media"], recalc[clave(fila)]["delta_izq_menos_der_media"], rel_tol=1e-12, abs_tol=1e-15)
        and math.isclose(fila["delta_izq_menos_der_ic95_inf"], recalc[clave(fila)]["delta_izq_menos_der_ic95_inf"], rel_tol=1e-12, abs_tol=1e-15)
        and fila["p_valor_test_signo"] == recalc[clave(fila)]["p_valor_test_signo"]
        for fila in estad_escrita["deltas_entre_controladores"]
    )
    return iguales


def informe(nombre, agregados, deltas, wlt, afirmaciones):
    print("=== " + nombre)
    print("  {:<16} {:>8} {:>8} {:>9} {:>8} {:>8} {:>9}".format(
        "controlador", "QoE", "bitrate", "rebuf_s", "stalls", ">5s", "respaldo"))
    for alias, fila in sorted(agregados.items(), key=lambda par: -par[1]["qoe_lineal_media"]):
        print("  {:<16} {:>8.4f} {:>8.0f} {:>9.2f} {:>8.2f} {:>7.1f}% {:>9d}".format(
            alias, fila["qoe_lineal_media"], fila["bitrate_medio_kbps"], fila["rebuffering_total_s_media"],
            fila["num_stalls_media"], 100 * fila["proporcion_sesiones_rebuffering_gt5s"], fila["num_filas_respaldo"]))
    print("  propio - rival: delta medio [IC95], p signo, W/L/T")
    for rival, d in deltas.items():
        print("    {:<16} {:+.3f} [{:+.3f}, {:+.3f}]  p={:.2g}  W{}/L{}/T{}  (n={})".format(
            rival, d["media"], d["ic95"][0], d["ic95"][1], d["p_signo"], *wlt[rival], d["n"]))
    propio = agregados[PROPIO]
    print("  latencia decision media {:.1f} ms (p95 {:.1f}); inferencia media {:.2f} ms; sin auditoria {}".format(
        propio["latencia_decision_ms_media"], propio["latencia_decision_ms_p95"], propio["ms_inferencia_red_media"],
        propio["num_filas_sin_auditoria_red"]))
    for clave, valor in afirmaciones.items():
        print("  [{}] {}".format("SE CUMPLE" if valor else "NO SE CUMPLE", clave))


def main():
    argumentos = argparse.ArgumentParser()
    argumentos.add_argument("paquete", type=Path)
    argumentos.add_argument("--excluir", default=None, help="VENTANA|PERFIL de un escenario real a excluir")
    argumentos.add_argument("--json", type=Path, default=None)
    opciones = argumentos.parse_args()

    resumenes = leer_sesiones(opciones.paquete)
    agregados, estadistica, deltas, wlt, afirmaciones = comprobar(resumenes)
    print("Recalculo identico al escrito por el paquete:", validar_recalculo(opciones.paquete, agregados, estadistica))
    informe(opciones.paquete.name + " (completo)", agregados, deltas, wlt, afirmaciones)
    resultado = {"completo": {"afirmaciones": afirmaciones, "deltas": deltas, "wlt": wlt}}

    if opciones.excluir:
        ventana, perfil = opciones.excluir.split("|")
        filtrados = [
            fila for fila in resumenes
            if not (fila["id_ventana_traza"] == ventana and fila["id_perfil_video"] == perfil)
        ]
        print("\nExcluidas {} sesiones del escenario {}".format(len(resumenes) - len(filtrados), opciones.excluir))
        agregados_f, _, deltas_f, wlt_f, afirmaciones_f = comprobar(filtrados)
        informe(opciones.paquete.name + " (sin el escenario afectado)", agregados_f, deltas_f, wlt_f, afirmaciones_f)
        resultado["sin_escenario"] = {"afirmaciones": afirmaciones_f, "deltas": deltas_f, "wlt": wlt_f}

    if opciones.json:
        opciones.json.write_text(json.dumps(resultado, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
