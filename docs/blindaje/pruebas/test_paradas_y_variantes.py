"""Correccion C2 del reproductor (a que fila va cada parada) y variantes del controlador propio."""
from __future__ import annotations

import os
import sys
import unittest

import numpy as np

CODIGO = os.environ.get("TFG_CODIGO", r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG")
BUNDLE = r"C:\Users\danie\Documents\TFG Material\03_modelos\modelo_propio\bundle"
FIJOS = r"C:\Users\danie\Documents\TFG Material\03_modelos\cuantiles_fijos\cuantiles_fijos.json"
sys.path.insert(0, CODIGO)

from core.controladores.registro import crear_controlador  # noqa: E402
from core.feedback_reproductor import construir_realimentacion_controlador  # noqa: E402
from core.modelo_propio.estado_sesion import EstadoSesion, media_armonica_bps  # noqa: E402
from core.modelo_propio.perfil_video import PerfilTamanosSegmentos  # noqa: E402
from reproductor import Reproductor  # noqa: E402


class _Nada:
    pass


class TestParadasC2(unittest.TestCase):
    def _reproductor(self):
        controlador = crear_controlador("bba")
        return Reproductor(_Nada(), _Nada(), "http://x/v.mpd", _Nada(), controlador)

    def test_la_parada_va_al_segmento_que_se_espera(self):
        r = self._reproductor()
        r._cola_reproduccion.extend([11])  # el 11 aun no se ha consumido entero
        r.indice_actual = 12  # se esta descargando el 12
        r._al_evento_motor("stall", {"id_stall": 1, "ts_evento": 10.0, "tiempo_actual": 0})
        r._al_evento_motor("stall_recuperado", {"id_stall": 1, "ts_evento": 13.5, "duracion_stall": 3.5, "tiempo_actual": 0})
        self.assertEqual(r._stalls_por_segmento, {12: {"marca": 1, "duracion": 3.5}})

    def test_el_vaciado_final_no_cuenta(self):
        r = self._reproductor()
        r.indice_actual = 31
        r._descargas_terminadas = True
        r._al_evento_motor("stall", {"id_stall": 2, "ts_evento": 100.0, "tiempo_actual": 0})
        self.assertEqual(r._stalls_por_segmento, {})
        self.assertEqual(r._stalls_abiertos, {})


class TestVariantesPropio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.escalera = PerfilTamanosSegmentos.cargar_por_id("paseo_almunecar_10min_30fps_4s").a_escalera_fiel(
            buffer_maximo_s=60.0, num_segmentos=30
        )
        cls.estado = EstadoSesion(5, 9.0, 3, (2.1e6, 1.8e6, 2.6e6, 2.2e6, 1.4e6), (0.5, 1.5, 2.0, 1.9, 2.1),
                                  0.0, 1.0, 0.0, 30)

    def _controlador(self, clave, **extra):
        parametros = {"dir_bundle": BUNDLE, "id_perfil_video": "paseo_10min_30fps_4s", "alfa_riesgo": 0.75}
        parametros.update(extra)
        return crear_controlador(clave, parametros)

    def test_mediana_es_la_columna_central_de_la_red(self):
        red = self._controlador("controlador_propio")
        med = self._controlador("propio_mediana")
        bundle = red._asegurar_bundle(red._diagnosticos_base())
        filas_red, _ = red._prediccion(bundle, self.estado, self.escalera)
        filas_med, cuantiles = med._prediccion(bundle, self.estado, self.escalera)
        self.assertEqual(cuantiles, (0.5,))
        self.assertEqual([f[0] for f in filas_med], [f[2] for f in filas_red])

    def test_cuantiles_recientes_son_los_de_las_ultimas_descargas(self):
        rec = self._controlador("propio_cuantiles_recientes")
        bundle = rec._asegurar_bundle(rec._diagnosticos_base())
        filas, cuantiles = rec._prediccion(bundle, self.estado, self.escalera)
        esperada = tuple(sorted(np.quantile(self.estado.historial_throughput_bps, cuantiles)))
        self.assertEqual(len(filas), bundle.horizonte_segmentos)
        for fila in filas:
            self.assertEqual(fila, esperada)

    def test_cuantiles_fijos_escalan_la_media_armonica(self):
        fij = self._controlador("propio_cuantiles_fijos", ruta_cuantiles_fijos=FIJOS)
        bundle = fij._asegurar_bundle(fij._diagnosticos_base())
        filas, _ = fij._prediccion(bundle, self.estado, self.escalera)
        base = media_armonica_bps(self.estado.historial_throughput_bps)
        self.assertAlmostEqual(filas[0][2], base, delta=1.0)  # mediana del error = 0
        self.assertLess(filas[4][0], filas[0][0])  # la cola baja se abre con el horizonte

    def test_variantes_sin_red_no_cuentan_inferencia(self):
        rec = self._controlador("propio_cuantiles_recientes")
        tasas = [b / 8.0 for b in self.escalera.bitrates_bps]
        for indice in (1, 2):
            rec.fijarFeedbackReproductor(construir_realimentacion_controlador(
                bytes_en_cola=0, tiempo_en_cola=4.0 * indice, tasas=tasas, duraciones_fragmentos=[4.0] * 6,
                nivel_actual=0, nivel_max=5, bytes_descargados=0, indice_segmento=indice,
                inicio_peticion_segmento=None, fin_peticion_segmento=None, ultimo_tamano=150_000,
                ultimo_tiempo=0.4, duracion_fragmento=4.0, segmentos_totales=31))
        rec.calcularAccionControl()
        self.assertEqual(rec.obtener_diagnosticos_red()["ms_inferencia_red"], "0.000000")
        self.assertEqual(rec.obtener_diagnosticos_red()["respaldo_red_usado"], 0)
        self.assertEqual(rec.nombre, "propio_cuantiles_recientes")


if __name__ == "__main__":
    unittest.main()
