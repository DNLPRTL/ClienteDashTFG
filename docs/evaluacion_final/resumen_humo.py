"""Resume la prueba de humo: sesiones completadas y auditoria del controlador propio.

Uso: python3 resumen_humo.py <paquete>
"""
import csv
import glob
import os
import statistics
import sys


def main():
    paquete = sys.argv[1]
    sesiones = sorted(glob.glob(os.path.join(paquete, "01_ejecucion", "ejecuciones", "*")))
    completadas = 0
    for sesion in sesiones:
        for manifiesto in glob.glob(os.path.join(sesion, "ejecucion_*", "manifiesto_ejecucion.json")):
            with open(manifiesto, encoding="utf-8") as fichero:
                completadas += int('"estado": "completado"' in fichero.read())
    print("   sesiones completadas: {0} de {1}".format(completadas, len(sesiones)))
    correcto = len(sesiones) == 5 and completadas == 5

    for telemetria in glob.glob(os.path.join(paquete, "01_ejecucion", "ejecuciones", "*controlador_propio*", "ejecucion_*", "telemetria_segmentos.csv")):
        with open(telemetria, encoding="utf-8") as fichero:
            filas = [f for f in csv.DictReader(fichero) if (f.get("tasa_objetivo_politica") or "").strip()]
        respaldos = sum(1 for f in filas if f["feedback_respaldo_red_usado"] == "1")
        inferencia = [float(f["feedback_ms_inferencia_red"]) for f in filas if f["feedback_ms_inferencia_red"]]
        decision = [float(f["ms_decision_politica"]) for f in filas]
        print("   controlador propio: {0} decisiones, {1} respaldos; inferencia media {2:.2f} ms (max {3:.2f}); "
              "decision media {4:.1f} ms".format(len(filas), respaldos, statistics.mean(inferencia), max(inferencia),
                                                 statistics.mean(decision)))
        correcto = correcto and respaldos == 0 and len(filas) == 29
    return 0 if correcto else 1


if __name__ == "__main__":
    sys.exit(main())
