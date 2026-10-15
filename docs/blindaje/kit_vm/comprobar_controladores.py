"""Crea los 8 controladores del experimento con cada uno de los 5 videos y les hace decidir una vez.

Detecta antes de lanzar nada un descriptor de video, un bundle o unos cuantiles fijos que falten, y
mide cuanto tarda en crearse cada controlador (ahi se carga el modelo) y su primera decision. Se ejecuta desde la carpeta del codigo:
  cd ~/TFG/ClienteDashTFG && python3 ~/TFG/kit_vm/comprobar_controladores.py
"""
import statistics
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, ".")

from core.controladores.registro import crear_controlador  # noqa: E402
from core.evaluacion.catalogo import PERFILES_VIDEO, especificacion_preset, parametros_controlador  # noqa: E402
from core.evaluacion.configuracion import cargar_config_evaluacion  # noqa: E402
from core.feedback_reproductor import construir_realimentacion_controlador  # noqa: E402
from core.modelo_propio.perfil_video import PerfilTamanosSegmentos  # noqa: E402


def realimentacion(indice, tasas, buffer_s):
    return construir_realimentacion_controlador(
        bytes_en_cola=0, tiempo_en_cola=buffer_s, tasas=tasas, duraciones_fragmentos=[4.0] * len(tasas),
        nivel_actual=0, nivel_max=len(tasas) - 1, bytes_descargados=0, indice_segmento=indice,
        inicio_peticion_segmento=None, fin_peticion_segmento=None, ultimo_tamano=150000,
        ultimo_tiempo=0.5, duracion_fragmento=4.0, segmentos_totales=31,
    )


def main():
    config = cargar_config_evaluacion(None)
    controladores = list(config["experimento"]["controladores"])
    videos = especificacion_preset("final_blindaje")["ids_perfiles_video"]
    latencias = {}
    primeras = {}
    creacion = {}
    for video in videos:
        perfil = PerfilTamanosSegmentos.cargar_por_id(video)
        tasas = [b / 8.0 for b in perfil.bitrates_bps]
        for clave in controladores:
            parametros = dict(parametros_controlador(config, clave))
            parametros["id_perfil_video"] = video
            inicio = time.perf_counter()
            controlador = crear_controlador(clave, parametros)
            creacion.setdefault(clave, []).append(1000.0 * (time.perf_counter() - inicio))
            controlador.fijarFeedbackReproductor(realimentacion(1, tasas, 4.0))
            controlador.fijarFeedbackReproductor(realimentacion(2, tasas, 7.5))
            inicio = time.perf_counter()
            controlador.calcularAccionControl()
            primeras.setdefault(clave, []).append(1000.0 * (time.perf_counter() - inicio))
            inicio = time.perf_counter()
            controlador.fijarFeedbackReproductor(realimentacion(3, tasas, 10.0))
            controlador.calcularAccionControl()
            latencias.setdefault(clave, []).append(1000.0 * (time.perf_counter() - inicio))
            if hasattr(controlador, "obtener_diagnosticos_red"):
                diag = controlador.obtener_diagnosticos_red()
                if int(diag.get("respaldo_red_usado", 0)):
                    print("   FALLO: {0} con {1} uso el respaldo ({2})".format(clave, video, diag.get("motivo_respaldo_red")))
                    return 1
        print("   {0}: los {1} controladores deciden".format(PERFILES_VIDEO[video]["nombre_visible"], len(controladores)))
    for clave, valores in latencias.items():
        print("   {0:28s} crear {1:6.1f} ms | primera decision {2:5.1f} ms | siguiente {3:5.1f} ms (maximos)".format(
            clave, max(creacion[clave]), max(primeras[clave]), max(valores)))
    peor = max(max(v) for v in list(latencias.values()) + list(primeras.values()))
    return 0 if peor < 50.0 else 1


if __name__ == "__main__":
    sys.exit(main())
