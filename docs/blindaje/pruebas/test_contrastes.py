"""Contrastes prerregistrados con datos sinteticos de resultado conocido."""
from __future__ import annotations

import os
import random
import sys
import unittest

CODIGO = os.environ.get("TFG_CODIGO", r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG")
sys.path.insert(0, CODIGO)

from core.evaluacion.contrastes import contrastes_prerregistrados, holm  # noqa: E402


def banco(semilla=1, ventanas=74, efecto_paradas=-0.5, efecto_qoe=0.0):
    rng = random.Random(semilla)
    filas = []
    for v in range(ventanas):
        base = rng.uniform(1.0, 3.0)
        for video in ("visto_%d" % (v % 4), "tears_10min_30fps_4s"):
            for alias, dq, dp in (
                ("controlador_propio", 0.0, 0.0),
                ("mpc_robusto", -efecto_qoe, -efecto_paradas),
                ("propio_cuantiles_recientes", 0.0, 0.6),
                ("propio_cuantiles_fijos", -0.15, 0.0),
                ("propio_mediana", -0.05, 0.9),
            ):
                filas.append({
                    "alias_controlador": alias, "id_ventana_traza": "real_%03d" % v, "id_perfil_video": video,
                    "repeticion": 1, "sintetica": False, "evaluables": 1, "id_dataset": "oboe" if v % 3 else "fcc",
                    "qoe_lineal_media": base + dq + rng.gauss(0, 0.05),
                    "num_stalls": max(0.0, 0.3 + dp + rng.gauss(0, 0.1)),
                    "rebuffering_total_s": 0.0, "bitrate_medio_kbps": 2500.0, "num_cambios_calidad": 3, "qoe_log_media": 1.0,
                })
    return filas


class TestContrastes(unittest.TestCase):
    def test_hipotesis_con_efecto_conocido(self):
        r = contrastes_prerregistrados(banco())
        p = r["principales"]
        self.assertTrue(p["P1"]["equivalente_ic90"])            # QoE igual
        self.assertTrue(p["P1"]["rechazada_nula"])
        self.assertTrue(p["P2"]["rechazada_nula"])              # menos paradas que el MPC
        self.assertLess(p["P2"]["media_diferencia"], 0)
        self.assertTrue(p["P3"]["rechazada_nula"])
        self.assertTrue(p["P4"]["rechazada_nula"])              # mas QoE que los fijos
        self.assertTrue(p["P5"]["rechazada_nula"])
        self.assertEqual(p["P2"]["n_ventanas"], 74)
        self.assertEqual(p["P2"]["n_escenarios"], 148)

    def test_sin_efecto_no_se_afirma_nada(self):
        r = contrastes_prerregistrados(banco(semilla=3, efecto_paradas=0.0))
        self.assertFalse(r["principales"]["P2"]["rechazada_nula"])

    def test_equivalencia_falla_si_la_diferencia_es_grande(self):
        r = contrastes_prerregistrados(banco(semilla=5, efecto_qoe=0.3))
        self.assertFalse(r["principales"]["P1"]["equivalente_ic90"])

    def test_holm(self):
        ajuste = holm({"a": 0.01, "b": 0.04, "c": 0.03})
        self.assertAlmostEqual(ajuste["a"]["p_holm"], 0.03)
        self.assertAlmostEqual(ajuste["c"]["p_holm"], 0.06)
        self.assertAlmostEqual(ajuste["b"]["p_holm"], 0.06)
        self.assertTrue(ajuste["a"]["rechazada_nula"])
        self.assertFalse(ajuste["c"]["rechazada_nula"])

    def test_interaccion_contenido(self):
        r = contrastes_prerregistrados(banco())
        self.assertEqual(r["contenido_nuevo_frente_a_visto"]["n_ventanas"], 74)


if __name__ == "__main__":
    unittest.main()
