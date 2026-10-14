"""Resume la prueba de humo: 8 sesiones completadas y auditoria de las variantes del propio.

Uso: python3 resumen_humo.py <paquete>
"""
import csv
import glob
import os
import statistics
import sys

CON_RED = ("controlador_propio", "propio_mediana")


def main():
    paquete = sys.argv[1]
    sesiones = sorted(glob.glob(os.path.join(paquete, "01_ejecucion", "ejecuciones", "*")))
    completadas = 0
    for sesion in sesiones:
        for manifiesto in glob.glob(os.path.join(sesion, "ejecucion_*", "manifiesto_ejecucion.json")):
            with open(manifiesto, encoding="utf-8") as fichero:
                completadas += int('"estado": "completado"' in fichero.read())
    print("   sesiones completadas: {0} de {1}".format(completadas, len(sesiones)))
    correcto = len(sesiones) == 8 and completadas == 8

    for sesion in sesiones:
        nombre = os.path.basename(sesion)
        for telemetria in glob.glob(os.path.join(sesion, "ejecucion_*", "telemetria_segmentos.csv")):
            with open(telemetria, encoding="utf-8") as fichero:
                filas = [f for f in csv.DictReader(fichero) if (f.get("tasa_objetivo_politica") or "").strip()]
            decision = [float(f["ms_decision_politica"]) for f in filas]
            texto = "   {0}: {1} decisiones, decision media {2:.1f} ms (max {3:.1f})".format(
                nombre[7:45], len(filas), statistics.mean(decision), max(decision))
            correcto = correcto and len(filas) == 29
            if "feedback_respaldo_red_usado" in (filas[0] if filas else {}):
                respaldos = sum(1 for f in filas if f["feedback_respaldo_red_usado"] == "1")
                texto += ", {0} respaldos".format(respaldos)
                correcto = correcto and respaldos == 0
                if any(clave in nombre for clave in CON_RED) and "cuantiles" not in nombre:
                    inferencia = [float(f["feedback_ms_inferencia_red"]) for f in filas if f["feedback_ms_inferencia_red"]]
                    texto += ", inferencia media {0:.2f} ms (max {1:.2f})".format(statistics.mean(inferencia), max(inferencia))
                    correcto = correcto and max(inferencia) < 50.0
            print(texto)
    return 0 if correcto else 1


if __name__ == "__main__":
    sys.exit(main())
