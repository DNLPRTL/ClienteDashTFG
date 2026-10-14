"""Comprueba que el planificador vectorizado decide exactamente igual que el original.

Para cada decision registrada en las ejecuciones anteriores (estado, prediccion de cuantiles y
video), ejecuta el planificador original (copia archivada del codigo) y el nuevo (codigo de
entrega) con las mismas entradas y compara accion, puntuacion CVaR, secuencia elegida y
rebuffering por escenario. Mide tambien el tiempo de ambos.

Uso: python verificar_planificador.py <codigo_nuevo> <codigo_archivado> <decisiones.jsonl> [...]
"""
from __future__ import annotations

import functools
import importlib.util
import json
import operator
import sys
import time
from pathlib import Path


def main() -> int:
    nuevo, archivado = Path(sys.argv[1]), Path(sys.argv[2])
    ficheros = [Path(p) for p in sys.argv[3:]]
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(nuevo))
    from core.modelo_propio.estado_sesion import EstadoSesion
    from core.modelo_propio.perfil_video import PerfilTamanosSegmentos
    from core.modelo_propio.planificador import planificar_accion as planificar_nuevo

    especificacion = importlib.util.spec_from_file_location(
        "planificador_original", archivado / "core" / "modelo_propio" / "planificador.py"
    )
    original = importlib.util.module_from_spec(especificacion)
    sys.modules["planificador_original"] = original
    especificacion.loader.exec_module(original)
    # Desde Python 3.12, sum() de flotantes usa una suma compensada; la VM de validacion
    # ejecuta Python 3.8, cuya suma es secuencial. Se emula aqui para comparar con lo que
    # haria el original en la VM.
    original.sum = lambda valores: functools.reduce(operator.add, valores, 0)

    escaleras = {}
    total = iguales = 0
    t_original = t_nuevo = 0.0
    diferencias = []
    for fichero in ficheros:
        for linea in fichero.open(encoding="utf-8"):
            r = json.loads(linea)
            perfil = r["perfil"]
            if perfil not in escaleras:
                escaleras[perfil] = PerfilTamanosSegmentos.cargar_por_id(perfil).a_escalera_fiel(buffer_maximo_s=60.0)
            escalera = escaleras[perfil]
            estado = EstadoSesion(
                indice_segmento=int(r["k"]),
                buffer_s=float(r["buffer_s"]),
                indice_ultima_representacion=int(r["nivel_previo"]),
                historial_throughput_bps=tuple(r["historial_tp_bps"]),
                historial_tiempo_descarga_s=(),
                rebuffering_reciente_s=0.0,
                cambio_reciente_abs=0.0,
                tiempo_red_s=0.0,
                segmentos_totales=31,
            )
            argumentos = dict(
                estado=estado,
                escalera=escalera,
                prediccion_bps_por_horizonte_y_cuantil=r["pred_bps"],
                cuantiles=(0.10, 0.25, 0.50, 0.75),
                horizonte_segmentos=5,
                mascara_acciones=(True,) * 6,
                alfa_riesgo=0.75,
                peso_rebuffering=4.3,
                peso_cambios=1.0,
            )
            t0 = time.perf_counter()
            a = original.planificar_accion(**argumentos)
            t1 = time.perf_counter()
            b = planificar_nuevo(**argumentos)
            t2 = time.perf_counter()
            t_original += t1 - t0
            t_nuevo += t2 - t1
            total += 1
            mismo = (
                a.accion == b.accion
                and a.cvar_puntuacion == b.cvar_puntuacion
                and a.mejor_secuencia == b.mejor_secuencia
                and a.rebuffer_por_cuantil_s == b.rebuffer_por_cuantil_s
                and a.accion == int(r["accion_log"])
            )
            iguales += int(mismo)
            if not mismo and len(diferencias) < 5:
                diferencias.append((r["sesion"], r["k"], a.accion, b.accion, a.cvar_puntuacion, b.cvar_puntuacion))
    print("decisiones comparadas: {0}; identicas en accion, CVaR, secuencia y rebuffering: {1}".format(total, iguales))
    print("tiempo medio por decision: original {0:.1f} ms, vectorizado {1:.2f} ms".format(
        1000.0 * t_original / total, 1000.0 * t_nuevo / total))
    for d in diferencias:
        print("   DIFERENCIA:", d)
    return 0 if iguales == total else 1


if __name__ == "__main__":
    sys.exit(main())
