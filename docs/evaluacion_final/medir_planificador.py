"""Mide en la maquina actual el tiempo de una decision del planificador (sin la red neuronal).

Se ejecuta desde la carpeta del codigo: cd ~/TFG/ClienteDashTFG && python3 medir_planificador.py
"""
import statistics
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, ".")

from core.modelo_propio.estado_sesion import EstadoSesion  # noqa: E402
from core.modelo_propio.perfil_video import PerfilTamanosSegmentos  # noqa: E402
from core.modelo_propio.planificador import planificar_accion  # noqa: E402

escalera = PerfilTamanosSegmentos.cargar_por_id("paseo_almunecar_10min_30fps_4s").a_escalera_fiel(num_segmentos=30)
estado = EstadoSesion(10, 16.6, 3, (2.0e6,) * 5, (2.4,) * 5, 0.0, 0.0, 0.0, 30)
prediccion = [(1.25e6, 1.64e6, 1.84e6, 2.08e6)] * 5
tiempos = []
for _ in range(30):
    inicio = time.perf_counter()
    planificar_accion(
        estado=estado, escalera=escalera, prediccion_bps_por_horizonte_y_cuantil=prediccion,
        mascara_acciones=(True,) * 6, alfa_riesgo=0.75,
    )
    tiempos.append(1000.0 * (time.perf_counter() - inicio))
media = statistics.mean(tiempos[1:])
print("   planificador: {0:.1f} ms de media por decision (maximo {1:.1f} ms)".format(media, max(tiempos[1:])))
sys.exit(0 if media < 50.0 else 1)
