"""El MPC canonico del cliente decide como el codigo de referencia de Pensieve (test/mpc.py).

Se compara, sobre estados aleatorios con tamanos reales de un video del experimento, la primera
accion del planificador del cliente con un solo escenario frente a una copia literal del bucle de
Pensieve. Ademas se comprueba la prediccion robusta: media armonica de las 5 ultimas descargas
dividida por (1 + error porcentual maximo de esa media en las 5 ultimas), sin factor de arranque.
"""
from __future__ import annotations

import itertools
import os
import random
import sys
import unittest

CODIGO = os.environ.get("TFG_CODIGO", r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG")
sys.path.insert(0, CODIGO)

from core.controladores.robust_mpc import ControladorMpcRobusto  # noqa: E402
from core.feedback_reproductor import construir_realimentacion_controlador  # noqa: E402
from core.modelo_propio.estado_sesion import EstadoSesion, media_armonica_bps  # noqa: E402
from core.modelo_propio.perfil_video import PerfilTamanosSegmentos  # noqa: E402
from core.modelo_propio.planificador import planificar_accion  # noqa: E402

VIDEO = "blender_sunflower_10min_30fps_4s"
SEGMENTOS = 30


def recompensa_pensieve(combo, buffer_s, ultimo_nivel, siguiente, tamanos, bitrates_kbps, ancho_banda_bps):
    # Copia de test/mpc.py de Pensieve (bucle interior), con el tamano real de cada segmento.
    buffer = buffer_s
    rebuffer = 0.0
    suma = 0.0
    suavidad = 0.0
    ultimo = ultimo_nivel
    for posicion, nivel in enumerate(combo):
        descarga = tamanos[nivel][siguiente + posicion] * 8.0 / ancho_banda_bps
        if buffer < descarga:
            rebuffer += descarga - buffer
            buffer = 0.0
        else:
            buffer -= descarga
        buffer += 4.0
        suma += bitrates_kbps[nivel]
        suavidad += abs(bitrates_kbps[nivel] - bitrates_kbps[ultimo])
        ultimo = nivel
    return suma / 1000.0 - 4.3 * rebuffer - suavidad / 1000.0


def mejor_pensieve(buffer_s, ultimo_nivel, siguiente, tamanos, bitrates_kbps, ancho_banda_bps, total):
    futuros = min(5, total - siguiente)
    mejor, mejor_combo = -1e18, ()
    for combo in itertools.product(range(len(bitrates_kbps)), repeat=futuros):
        recompensa = recompensa_pensieve(combo, buffer_s, ultimo_nivel, siguiente, tamanos, bitrates_kbps, ancho_banda_bps)
        if recompensa > mejor:
            mejor, mejor_combo = recompensa, combo
    return mejor, mejor_combo


class TestMpcCanonico(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        perfil = PerfilTamanosSegmentos.cargar_por_id(VIDEO)
        cls.escalera = perfil.a_escalera_fiel(buffer_maximo_s=60.0, num_segmentos=SEGMENTOS)
        cls.bitrates_kbps = [b / 1000.0 for b in cls.escalera.bitrates_bps]
        cls.tamanos = [[cls.escalera.bytes_segmento(n, i) for i in range(SEGMENTOS)] for n in range(6)]

    def test_misma_accion_que_pensieve(self):
        # La secuencia que elige el planificador tiene la recompensa maxima de Pensieve. En los
        # empates exactos (misma recompensa en aritmetica exacta) el desempate depende del
        # redondeo, porque las sumas van en otro orden; fuera de ellos, la accion es la misma.
        rng = random.Random(2015)
        iguales = 0
        for _ in range(400):
            # Buffer <= 40 s: en 5 pasos no llega al tope de 60 s del planificador.
            buffer_s = rng.uniform(0.0, 40.0)
            ultimo = rng.randrange(6)
            siguiente = rng.randrange(1, SEGMENTOS)
            ancho_banda = rng.uniform(0.2e6, 8e6)
            estado = EstadoSesion(siguiente, buffer_s, ultimo, (ancho_banda,), (1.0,), 0.0, 0.0, 0.0, SEGMENTOS)
            decision = planificar_accion(
                estado=estado,
                escalera=self.escalera,
                prediccion_bps_por_horizonte_y_cuantil=[(ancho_banda,)] * 5,
                cuantiles=(0.5,),
                horizonte_segmentos=5,
                alfa_riesgo=1.0,
            )
            mejor, combo = mejor_pensieve(
                buffer_s, ultimo, siguiente, self.tamanos, self.bitrates_kbps, ancho_banda, SEGMENTOS
            )
            elegida = recompensa_pensieve(
                decision.mejor_secuencia, buffer_s, ultimo, siguiente, self.tamanos, self.bitrates_kbps, ancho_banda
            )
            self.assertAlmostEqual(elegida, mejor, places=9, msg=(buffer_s, ultimo, siguiente, ancho_banda))
            iguales += int(decision.accion == combo[0])
        self.assertGreaterEqual(iguales, 390)

    def _fb(self, indice, tamano, tiempo, nivel=0, buffer_s=8.0):
        tasas = [b / 8.0 for b in self.escalera.bitrates_bps]
        return construir_realimentacion_controlador(
            bytes_en_cola=0, tiempo_en_cola=buffer_s, tasas=tasas, duraciones_fragmentos=[4.0] * 6,
            nivel_actual=nivel, nivel_max=5, bytes_descargados=0, indice_segmento=indice,
            inicio_peticion_segmento=None, fin_peticion_segmento=None, ultimo_tamano=tamano,
            ultimo_tiempo=tiempo, duracion_fragmento=4.0, segmentos_totales=SEGMENTOS + 1,
        )

    def test_prediccion_robusta_con_error_respecto_a_la_media_armonica(self):
        mpc = ControladorMpcRobusto(id_perfil_video=VIDEO)
        muestras_bps = [2.0e6, 1.0e6, 3.0e6, 1.5e6, 2.5e6, 0.8e6, 2.2e6]
        esperado_errores = []
        prediccion_previa = None
        historial = []
        for indice, bps in enumerate(muestras_bps, start=1):
            mpc.fijarFeedbackReproductor(self._fb(indice, 500_000, 500_000 * 8.0 / bps))
            historial = (historial + [bps])[-5:]
            if prediccion_previa is not None:
                esperado_errores = (esperado_errores + [abs(prediccion_previa - bps) / bps])[-5:]
            prediccion_previa = media_armonica_bps(historial)
        self.assertEqual(len(mpc._errores_prediccion), 5)
        for real, esperado in zip(mpc._errores_prediccion, esperado_errores):
            self.assertAlmostEqual(real, esperado, places=9)
        prevista = mpc.prediccion_throughput_bps(historial)
        self.assertAlmostEqual(prevista, media_armonica_bps(historial) / (1.0 + max(esperado_errores)), places=3)

    def test_sin_errores_previos_la_prediccion_es_la_media_armonica(self):
        mpc = ControladorMpcRobusto(id_perfil_video=VIDEO)
        mpc.fijarFeedbackReproductor(self._fb(1, 400_000, 1.6))
        self.assertEqual(mpc._errores_prediccion, [])
        self.assertAlmostEqual(mpc.prediccion_throughput_bps((2.0e6,)), 2.0e6, places=6)

    def test_el_historial_incluye_el_calentamiento(self):
        # El reproductor no pide decision tras el primer segmento: su descarga tiene que contar.
        mpc = ControladorMpcRobusto(id_perfil_video=VIDEO)
        mpc.fijarFeedbackReproductor(self._fb(1, 150_000, 0.6))
        mpc.fijarFeedbackReproductor(self._fb(2, 150_000, 0.3))
        mpc.calcularAccionControl()
        self.assertEqual(len(mpc.ultimas_metricas["historial_throughput_bps"]), 2)

    def test_falta_el_descriptor(self):
        with self.assertRaises(Exception):
            ControladorMpcRobusto(id_perfil_video="video_que_no_existe")


if __name__ == "__main__":
    unittest.main()
