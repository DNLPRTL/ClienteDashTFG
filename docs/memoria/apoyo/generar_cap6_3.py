# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_3_integridad_verificacion.docx (apartado 6.3).

Fuentes, todas en TFG Material: el paquete final (sesiones.csv, segmentos.csv, verificacion_paquete.json,
resumen_resultados.json, manifiestos y entorno.json de las 1208 ejecuciones) y la verificacion fuera de linea
de verificacion_windows_20261016 (auditoria_decisiones.json, validacion_simulador.json,
huellas_paquete.sha256). Ademas, el script REPITE aqui el analisis prerregistrado con el modulo
core/evaluacion/contrastes.py del entregable sobre sesiones.csv y lo compara numero a numero con
contrastes_prerregistrados.json (resultado en apoyo/contrastes_reproducidos.json), y recalcula el
SHA-256 de los 9699 ficheros del paquete contra la lista de huellas.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_3.py   (unos minutos)
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import statistics
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
VERIF_WIN = TFG_MATERIAL / "04_evidencia_final" / "verificacion_windows_20261016"
KIT_VM = RAIZ_REPO / "docs" / "blindaje" / "kit_vm"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap6_3_integridad_verificacion.docx"
CACHE_CONTRASTES = Path(__file__).resolve().parent / "contrastes_reproducidos.json"
sys.path.insert(0, str(CODIGO))

NOMBRE_CTRL = {
    "basado_en_tasa": "basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "MPC robusto",
    "controlador_propio": "controlador propio", "propio_mediana": "propio, solo la mediana",
    "propio_cuantiles_recientes": "propio, cuantiles recientes", "propio_cuantiles_fijos": "propio, cuantiles fijos",
}
COMPUERTAS = {
    "sesiones_reales_completadas": "todas las sesiones reales completadas y evaluables",
    "evaluacion_formal_solo_eval": "todas las ventanas reales de la partición de evaluación",
    "evaluacion_formal_solo_perfiles_4s": "todos los vídeos con segmentos de 4 s",
    "propios_sin_respaldo_en_evaluables": "ningún respaldo en las sesiones del propio y sus variantes",
    "propios_con_inferencia_verificada": "auditoría de inferencia completa en las variantes con red",
    "sin_artefactos_antiguos": "ningún artefacto de versiones anteriores del cliente",
    "sinteticas_informadas_aparte": "sintéticas separadas de las reales",
    "resumen_en_texto_disponible": "resumen legible del paquete presente",
}


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def miles(n):
    return "{0:,}".format(int(n)).replace(",", " ") if int(n) >= 10000 else str(int(n))


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def percentil(valores, q):
    v = sorted(valores)
    k = (len(v) - 1) * q
    i, j = int(k), min(int(k) + 1, len(v) - 1)
    return v[i] + (v[j] - v[i]) * (k - i)


def comparar(a, b, ruta="", tol=1e-9):
    """Compara dos estructuras JSON numero a numero; devuelve la lista de diferencias."""
    dif = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in set(a) | set(b):
            if k in ("texto",):
                continue
            if k not in a or k not in b:
                dif.append(ruta + "/" + str(k) + ": falta")
            else:
                dif += comparar(a[k], b[k], ruta + "/" + str(k), tol)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            dif.append(ruta + ": longitud")
        for i, (x, y) in enumerate(zip(a, b)):
            dif += comparar(x, y, ruta + "[{0}]".format(i), tol)
    elif isinstance(a, bool) or isinstance(b, bool):
        if a != b:
            dif.append(ruta + ": {0} != {1}".format(a, b))
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if abs(float(a) - float(b)) > tol:
            dif.append(ruta + ": {0} != {1}".format(a, b))
    elif a != b:
        dif.append(ruta + ": {0!r} != {1!r}".format(a, b))
    return dif


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from core.evaluacion.contrastes import contrastes_prerregistrados

    # ---- Ejecucion -------------------------------------------------------------------------
    sesiones = leer_csv(PAQUETE / "02_resultados" / "sesiones.csv")
    segmentos = leer_csv(PAQUETE / "02_resultados" / "segmentos.csv")
    plan = leer_csv(PAQUETE / "00_protocolo" / "plan_sesiones.csv")
    assert len(sesiones) == len(plan) == 1208 and len(segmentos) == 35032
    assert {s["estado_ejecucion"] for s in sesiones} == {"completado"}
    assert {s["evaluables"] for s in sesiones} == {"1"} and {s["artefactos_requeridos_presentes"] for s in sesiones} == {"1"}
    assert {s["artefactos_antiguos_presentes"] for s in sesiones} == {"0"} and {s["motivo_fallo"] for s in sesiones} == {""}
    inicios, entornos = {}, set()
    for s in plan:
        carpetas = sorted((PAQUETE / "01_ejecucion" / "ejecuciones" / s["id_sesion"]).glob("ejecucion_*"))
        assert len(carpetas) == 1  # una sola ejecucion por sesion: sin reanudaciones
        m = json.load(open(carpetas[0] / "manifiesto_ejecucion.json", encoding="utf-8"))
        assert m["estado"] == "completado"
        inicios[s["id_sesion"]] = datetime.fromisoformat(m["creado_utc"].replace("Z", "+00:00"))
        e = json.load(open(carpetas[0] / "entorno.json", encoding="utf-8"))
        entornos.add(json.dumps({k: e[k] for k in ("python", "plataforma", "versiones_paquetes", "analisis_opcional")}, sort_keys=True))
    assert len(entornos) == 1
    entorno = json.loads(next(iter(entornos)))
    ordenados = sorted(inicios.values())
    huecos = [(b - a).total_seconds() for a, b in zip(ordenados, ordenados[1:])]
    dur_media = statistics.mean(huecos)
    horas = (ordenados[-1].timestamp() + dur_media - ordenados[0].timestamp()) / 3600
    assert max(huecos) < 300 and 41.0 < horas < 41.6
    # Ventanas: las 77 del protocolo son las esperadas por el kit.
    ventanas = leer_csv(PAQUETE / "00_protocolo" / "ventanas_trazas.csv")
    esperadas = [l.strip() for l in (KIT_VM / "ventanas_esperadas_final.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert [v["id_ventana_traza"] for v in ventanas] == esperadas and len(esperadas) == 77

    # Respaldos e inferencia (propio y variantes).
    propios = [s for s in sesiones if s["alias_controlador"].startswith(("controlador_propio", "propio_"))]
    dec_propios = sum(int(s["num_segmentos"]) for s in propios)
    respaldos = sum(int(s["num_filas_respaldo"]) for s in propios)
    auditoria_ok = sum(int(s["num_filas_auditoria_red_ok"]) for s in propios)
    inferencias = sum(int(s["num_filas_inferencia_red"]) for s in propios)
    assert len(propios) == 604 and dec_propios == 17516 and respaldos == 0 and auditoria_ok == 17516 and inferencias == 2 * 4379
    assert sum(int(f["respaldo_usado"]) for f in segmentos) == 0

    # Latencias.
    lat = [float(f["latencia_decision_ms"]) for f in segmentos]
    p99 = percentil(lat, 0.99)
    lentas = [f for f in segmentos if float(f["latencia_decision_ms"]) > 20]
    primer_indice = min(int(f["indice_segmento"]) for f in segmentos)
    assert all(int(f["indice_segmento"]) == primer_indice for f in lentas) and len(lentas) == 4
    por_ctrl = {}
    for f in segmentos:
        por_ctrl.setdefault(f["alias_controlador"], []).append(float(f["latencia_decision_ms"]))
    p99_ctrl = {c: percentil(v, 0.99) for c, v in por_ctrl.items()}
    p50_propio = statistics.median(por_ctrl["controlador_propio"])
    primeras_propio = [float(f["latencia_decision_ms"]) for f in segmentos
                       if f["alias_controlador"] == "controlador_propio" and int(f["indice_segmento"]) == primer_indice]
    inf = [float(f["ms_inferencia_red"]) for f in segmentos if float(f["ms_inferencia_red"]) > 0]
    assert len(inf) == 2 * 4379 and max(inf) < 50
    limite_inferencia = json.load(open(CODIGO / "config" / "evaluacion.local.json", encoding="utf-8"))["parametros_controladores"]["controlador_propio"]["latencia_max_inferencia_ms"]

    # ---- Compuertas y verificacion del paquete -----------------------------------------------
    resumen = json.load(open(PAQUETE / "02_resultados" / "resumen_resultados.json", encoding="utf-8"))
    gates = resumen["gates"]
    assert gates["gates_superados"] is True and set(gates["detalle_gates"]) == set(COMPUERTAS) and all(gates["detalle_gates"].values())
    assert all(not v for v in gates["violaciones"].values())
    verif = json.load(open(PAQUETE / "02_resultados" / "verificacion_paquete.json", encoding="utf-8"))
    comprobaciones = verif["comprobaciones"]
    assert len(comprobaciones) == 15 and all(c["superado"] for c in comprobaciones) and verif["preset"] == "final_blindaje"
    sinteticas = sum(1 for s in sesiones if s["sintetica"] == "1")
    assert sinteticas == 24

    # Huellas: la lista y los 9699 ficheros.
    lineas = [l.split("  ", 1) for l in (VERIF_WIN / "huellas_paquete.sha256").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(lineas) == 9699
    huella_lista = hashlib.sha256((VERIF_WIN / "huellas_paquete.sha256").read_bytes()).hexdigest()
    assert huella_lista.startswith("e5dc724b") and huella_lista.endswith("3126")
    malos = [ruta for h, ruta in lineas if hashlib.sha256((PAQUETE / ruta.strip().lstrip("./")).read_bytes()).hexdigest() != h]
    assert not malos, malos[:5]

    # ---- Auditoria de decisiones y validacion de la fisica -------------------------------------
    audit = json.load(open(VERIF_WIN / "auditoria_decisiones.json", encoding="utf-8"))
    total_dec = sum(s["decisiones"] for s in audit["sesiones"])
    distintas = sum(len(s["distintas"]) for s in audit["sesiones"])
    resp_audit = sum(s["respaldos_en_auditoria"] for s in audit["sesiones"])
    assert total_dec == 35032 and distintas == 0 and resp_audit == 0 and len(audit["sesiones"]) == 1208
    assert all(v["decisiones"] == 4379 and v["distintas"] == 0 for v in audit["por_controlador"].values())
    val = json.load(open(VERIF_WIN / "validacion_simulador.json", encoding="utf-8"))
    forz = val["forzado"]
    fs = val["forzado_sesiones"]
    assert forz["sesiones"] == len(fs) == 1184 and forz["errores"] == 0 and forz["niveles_identicos"] == 1184
    dq = [abs(x["qoe_sim"] - x["qoe_vm"]) for x in fs]
    grandes = [x for x in fs if abs(x["qoe_sim"] - x["qoe_vm"]) > 0.05]
    assert statistics.median(dq) == 0.0 and len(grandes) == 22
    assert all(x["rebuf_vm"] > x["rebuf_sim"] for x in grandes)
    cerr = val["cerrado"]
    assert cerr["sesiones"] == 1184 and cerr["errores"] == 0
    par = cerr["pareadas_propio_vs_mpc_robusto"]
    assert par["n"] == 148 and abs(par["media_vm"] - par["media_sim"]) < 0.005

    # ---- Analisis prerregistrado repetido en Windows ------------------------------------------
    oficial = json.load(open(PAQUETE / "02_resultados" / "contrastes_prerregistrados.json", encoding="utf-8"))
    if CACHE_CONTRASTES.exists():
        repetido = json.load(open(CACHE_CONTRASTES, encoding="utf-8"))
    else:
        repetido = contrastes_prerregistrados(sesiones, oficial["hipotesis"])
        json.dump(repetido, open(CACHE_CONTRASTES, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    diferencias = comparar(oficial, repetido)
    assert not diferencias, diferencias[:10]

    # ---- Ejemplo: la sesion 8 -------------------------------------------------------------
    id_ej = next(s["id_sesion"] for s in sesiones if s["id_sesion"].startswith("s00008_"))
    aud_ej = next(s for s in audit["sesiones"] if s["id_sesion"] == id_ej)
    forz_ej = next(x for x in fs if x["id_sesion"] == id_ej)
    seg_ej = [f for f in segmentos if f["id_sesion"] == id_ej]
    lat_ej = [float(f["latencia_decision_ms"]) for f in seg_ej]
    inf_ej = [float(f["ms_inferencia_red"]) for f in seg_ej]
    assert aud_ej["decisiones"] == 29 and not aud_ej["distintas"] and forz_ej["niveles_identicos"]
    assert abs(forz_ej["qoe_sim"] - forz_ej["qoe_vm"]) < 1e-12

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.h2("6.3. Integridad de la ejecución y verificación")
    b.parrafo(
        "Antes de leer ningún resultado hay que comprobar que el experimento se ejecutó como se diseñó y que "
        "el paquete de evidencia es el que produjo la máquina virtual. Este apartado lo hace en cuatro "
        "niveles, del más externo al más interno: la ejecución (todas las sesiones, un solo entorno, sin "
        "huecos ni reanudaciones), las compuertas y la verificación automática del paquete, la repetición "
        "de cada una de las {0} decisiones con el código congelado y la reproducción de la física de cada "
        "sesión con un simulador. Cierra con la repetición del análisis prerregistrado en otra máquina. La "
        "Tabla 6.6 resume las comprobaciones y su resultado; ninguna falló, y las que no se cumplieron por "
        "completo se dicen con su cifra.".format(miles(total_dec))
    )

    b.h3("6.3.1. Ejecución completa y uniforme")
    b.parrafo(
        "Las {0} sesiones del plan se completaron, cada una en una sola ejecución: no hubo sesiones "
        "fallidas, ni repetidas, ni reanudaciones, de modo que las dos reglas de validez del apartado 6.1 no "
        "llegaron a aplicarse. Las {1} ventanas del protocolo coinciden, una por una y en el mismo orden, con "
        "la lista que se congeló antes de lanzar. El entorno registrado por cada sesión es el mismo en las "
        "{0}: Python {2} sobre {3}, requests {4}, NumPy {5}. La serie arrancó el {6} a las {7} UTC y la "
        "última sesión terminó el {8} hacia las {9} UTC, {10} h en total; el mayor hueco entre el inicio de "
        "una sesión y el de la siguiente fue de {11} s, es decir, no hubo pausas ni cortes.".format(
            miles(len(sesiones)), len(esperadas), entorno["python"]["version"], entorno["plataforma"]["sistema"] + " " + entorno["plataforma"]["version_so"].split("-generic")[0],
            entorno["versiones_paquetes"]["requests"], entorno["analisis_opcional"]["numpy"]["version"],
            ordenados[0].strftime("%d/%m/%Y"), ordenados[0].strftime("%H:%M"), ordenados[-1].strftime("%d/%m/%Y"),
            datetime.utcfromtimestamp(ordenados[-1].timestamp() + dur_media).strftime("%H:%M"), coma(horas, 1), coma(max(huecos), 0))
    )
    b.parrafo(
        "El controlador propio y sus tres variantes decidieron siempre por sí mismos: en sus {0} sesiones y "
        "{1} decisiones no se activó ni una vez el respaldo, y las {1} filas de auditoría de la red (acción "
        "bruta, acción segura, máscara y motivo) son válidas. Las dos variantes que usan la red registraron "
        "una inferencia por decisión, {2} en total, con un máximo de {3} ms frente al límite de {4} ms que "
        "habría dado paso al respaldo. La latencia de decisión, medida en el cliente desde que se entrega la "
        "realimentación hasta que se devuelve el nivel, tiene un percentil 99 de {5} ms sobre las {6} "
        "decisiones; por controlador, el percentil 99 va de {7} ms en los clásicos a {8} ms en el propio, cuya "
        "mediana es {9} ms. Solo {10} decisiones superan los 20 ms, todas primeras decisiones de una sesión "
        "(la primera llamada al modelo y al planificador tras crear el controlador), con un máximo de {11} ms; "
        "la primera decisión del propio tiene una mediana de {12} ms. Ninguna de estas latencias afecta a la "
        "QoE: la decisión se toma mientras el segmento anterior se reproduce.".format(
            len(propios), miles(dec_propios), miles(inferencias), coma(max(inf), 1), coma(limite_inferencia, 0),
            coma(p99, 1), miles(len(lat)), coma(min(p99_ctrl.values()), 2), coma(p99_ctrl["controlador_propio"], 1),
            coma(p50_propio, 1), len(lentas), coma(max(lat), 1), coma(statistics.median(primeras_propio), 1))
    )

    b.h3("6.3.2. Compuertas y verificación del paquete")
    b.parrafo(
        "El análisis aplica antes de comparar nada las ocho compuertas del apartado 4.8, que separan la "
        "validez de la ejecución de la comparación entre controladores: {0}. Las ocho se superan sin "
        "ninguna violación. Después, la verificación automática del paquete repasa {1} comprobaciones de "
        "estructura y coherencia: carpetas y ficheros de resultados presentes, plan con {2} sesiones y "
        "resumen con las mismas {2}, ninguna fallida ni ausente, ninguna fila de segmentos fuera de sesiones "
        "completadas, las {3} sesiones sintéticas informadas aparte y las gráficas generadas sin error. Las "
        "{1} se superan. Por último, al copiar el paquete a la máquina de desarrollo se calculó la huella "
        "SHA-256 de sus {4} ficheros; la lista de huellas tiene su propia huella ({5}…), y el script que "
        "genera este apartado vuelve a calcular las {4} huellas y comprueba que ningún fichero ha cambiado "
        "desde entonces.".format(
            "; ".join(COMPUERTAS[k] for k in gates["detalle_gates"]), len(comprobaciones), miles(len(sesiones)), sinteticas,
            len(lineas), huella_lista[:8])
    )

    b.h3("6.3.3. Decisiones repetidas y física reproducida")
    b.parrafo(
        "La comprobación más fuerte es repetir las decisiones. Cada fila de la telemetría guarda, con todos "
        "sus decimales, el diccionario de realimentación que recibió el controlador (apartado 4.6). Un "
        "programa de auditoría crea en la máquina de desarrollo, con el código congelado y los parámetros de "
        "cada sesión, un controlador nuevo, le entrega esa realimentación en el mismo orden y compara cada "
        "decisión, tasa objetivo y nivel, con la que registró la máquina virtual. Las {0} decisiones de las "
        "{1} sesiones, {2} por controlador, se repitieron idénticas, sin ningún respaldo. Esto demuestra dos "
        "cosas: que las decisiones del experimento son las del código entregado, con el modelo entregado, y "
        "que son deterministas dada la realimentación, lo que respalda la única repetición por escenario del "
        "diseño. La alternativa, ejecutar el experimento entero una segunda vez en la máquina virtual, habría "
        "costado otras {3} h y solo habría comprobado lo mismo con más ruido de temporización.".format(
            miles(total_dec), len(audit["sesiones"]), audit["por_controlador"]["bba"]["decisiones"], coma(horas, 0))
    )
    b.parrafo(
        "La auditoría no comprueba la temporalidad: cuánto tardó cada descarga ni cuándo se paró la "
        "reproducción. Para eso se usó un simulador en tiempo virtual construido con las clases del propio "
        "cliente (el reproductor con el motor simulado y la emulación por traza, sin esperas reales), al que "
        "se forzaron los mismos niveles que eligió la máquina virtual en cada sesión. Si la red, el buffer y "
        "las paradas se reproducen, la QoE debe coincidir. En las {0} sesiones reales la secuencia de niveles "
        "se reprodujo entera y la diferencia absoluta de QoE entre simulador y máquina virtual tiene mediana "
        "{1}, percentil 90 de {2} y máximo de {3}, con un sesgo medio de {4} a favor del simulador. Las {5} "
        "sesiones ({6} %) en las que la diferencia pasa de 0,05 tienen todas más rebuffering en la máquina "
        "virtual que en el simulador: son desfases de temporización del sistema operativo durante la espera, "
        "que el simulador no modela y que juegan por igual para todos los controladores, porque el orden "
        "dentro de cada escenario estaba sorteado. Cuando el simulador decide por sí mismo, en lugar de "
        "copiar los niveles, la diferencia media pareada entre el controlador propio y el MPC robusto en los "
        "{7} escenarios difiere de la de la máquina virtual en menos de {9} puntos de QoE, con una "
        "correlación de {8} entre escenarios: el resultado principal no depende del ruido temporal de la "
        "máquina virtual.".format(
            miles(forz["sesiones"]), coma(forz["mediana_abs_dqoe"], 3), coma(forz["p90_abs_dqoe"], 3), coma(forz["max_abs_dqoe"], 2),
            ("+" if forz["media_dqoe_sim_menos_vm"] > 0 else "−") + coma(abs(forz["media_dqoe_sim_menos_vm"]), 3), len(grandes),
            coma(100 * len(grandes) / len(fs), 1), par["n"], coma(par["correlacion"], 2), coma(0.001 * (int(abs(par["media_vm"] - par["media_sim"]) * 1000) + 1), 3))
    )
    b.parrafo(
        "El análisis prerregistrado también se repitió fuera de la máquina virtual: el mismo módulo de "
        "contrastes del código entregado, ejecutado en la máquina de desarrollo sobre el fichero de sesiones "
        "del paquete, reproduce las cinco hipótesis, las secundarias, los estratos y la interacción con "
        "diferencias menores de 10⁻⁹, incluidos los intervalos bootstrap gracias a la semilla fija. El script "
        "de este apartado repite esa comparación cada vez que se genera."
    )
    b.tabla(
        ["Comprobación", "Resultado", "Fuente"],
        [
            ("Sesiones completadas, una ejecución cada una", "{0} de {0}; 0 fallidas, 0 reanudaciones".format(miles(len(sesiones))), "manifiestos de ejecución"),
            ("Ventanas iguales a las congeladas", "{0} de {0}, en el mismo orden".format(len(esperadas)), "protocolo y lista del kit"),
            ("Entorno idéntico en todas las sesiones", "1 configuración (Python {0})".format(entorno["python"]["version"]), "fichero de entorno de cada sesión"),
            ("Duración y continuidad", "{0} h; hueco máximo {1} s".format(coma(horas, 1), coma(max(huecos), 0)), "manifiestos"),
            ("Respaldos en el propio y variantes", "0 en {0} decisiones".format(miles(dec_propios)), "segmentos y auditoría de red"),
            ("Inferencia de la red", "{0} inferencias, máximo {1} ms (límite {2} ms)".format(miles(inferencias), coma(max(inf), 1), coma(limite_inferencia, 0)), "segmentos"),
            ("Latencia de decisión", "p99 {0} ms; {1} decisiones > 20 ms (primeras), máximo {2} ms".format(coma(p99, 1), len(lentas), coma(max(lat), 1)), "segmentos"),
            ("Compuertas del análisis", "8 de 8, sin violaciones", "resumen del paquete"),
            ("Verificación del paquete", "{0} de {0} comprobaciones".format(len(comprobaciones)), "verificación automática"),
            ("Huellas del paquete", "{0} ficheros sin cambios; lista {1}…".format(len(lineas), huella_lista[:8]), "lista SHA-256 recalculada"),
            ("Decisiones repetidas con el código congelado", "{0} de {0} idénticas; 0 respaldos".format(miles(total_dec)), "auditoría fuera de línea"),
            ("Física reproducida (niveles forzados)", "{0} sesiones; mediana |ΔQoE| {1}, p90 {2}; {3} sesiones > 0,05".format(
                miles(forz["sesiones"]), coma(forz["mediana_abs_dqoe"], 3), coma(forz["p90_abs_dqoe"], 3), len(grandes)), "validación del simulador"),
            ("Análisis repetido en otra máquina", "contrastes idénticos (diferencias < 10⁻⁹)", "módulo de contrastes sobre sesiones.csv"),
        ],
        "Tabla 6.6: Comprobaciones de integridad del experimento final y resultado de cada una. Todas las "
        "cifras se recalculan desde el paquete y la verificación fuera de línea al generar este apartado.",
        anchos_cm=[5.2, 6.6, 4.2],
    )
    b.parrafo(
        "La sesión 8 del plan, la de los apartados anteriores, pasa por los cuatro niveles. Sus 29 decisiones "
        "se repitieron idénticas en la auditoría, sin respaldo; sus 29 inferencias tardaron {0} ms de media y "
        "sus decisiones {1} ms de mediana, con la primera en {2} ms; y el simulador con sus niveles forzados "
        "reproduce exactamente su QoE de {3}, con un error mediano de {4} s en el buffer a lo largo de la "
        "sesión. Los límites de esta verificación son dos. La auditoría demuestra que las decisiones son las "
        "del código dada la realimentación, pero la realimentación misma, los tiempos de descarga, viene de "
        "una emulación de red sin pila TCP ni tráfico competidor (apartado 4.7). Y el simulador que reproduce "
        "la física comparte el modelo de red y la dinámica del buffer con el cliente, así que valida la "
        "coherencia interna del sistema y la ausencia de efectos de la máquina virtual, no la fidelidad de la "
        "emulación frente a una red real; esa limitación se retoma en el apartado 6.7. Con la ejecución "
        "verificada, el apartado 6.4 presenta el resultado de las cinco hipótesis.".format(
            coma(statistics.mean(inf_ej), 1), coma(statistics.median(lat_ej), 1), coma(lat_ej[0], 1),
            coma(forz_ej["qoe_vm"], 3), coma(forz_ej["err_buffer_mediana_s"], 3))
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("latencias: p99", round(p99, 2), "max", round(max(lat), 2), "lentas", len(lentas), "p99 ctrl", {k: round(v, 2) for k, v in p99_ctrl.items()},
          "p50 propio", round(p50_propio, 2), "primera propio", round(statistics.median(primeras_propio), 2), "inf max", round(max(inf), 2))
    print("horas", round(horas, 2), "hueco max", round(max(huecos), 1), "| sim: p90", round(forz["p90_abs_dqoe"], 4), "max", round(forz["max_abs_dqoe"], 3), "grandes", len(grandes),
          "| cerrado pareadas", par)
    print("ejemplo", id_ej, "inf media", round(statistics.mean(inf_ej), 2), "lat mediana", round(statistics.median(lat_ej), 2), "primera", round(lat_ej[0], 2), "err buffer", round(forz_ej["err_buffer_mediana_s"], 3))


if __name__ == "__main__":
    main()
