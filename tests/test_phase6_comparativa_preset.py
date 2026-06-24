from __future__ import annotations

import unittest

from core.phase6.catalog import PRESET_NAMES, preset_spec


class Phase6ComparativaPresetTest(unittest.TestCase):
    def test_comparativa_preset_is_registered_and_rankable(self):
        self.assertIn("comparativa", PRESET_NAMES)
        spec = preset_spec("comparativa")
        self.assertTrue(spec["benchmark_capable"])
        self.assertTrue(spec["ranking_capable"])
        self.assertEqual(spec["real_windows"], 12)
        self.assertEqual(spec["synthetic_windows"], 3)
        self.assertEqual(spec["max_media_segments"], 30)
        self.assertEqual(spec["media_profile_ids"], ["paseo_10min_30fps_4s"])

    def test_tfg_final_preset_multivideo_and_rankable(self):
        self.assertIn("tfg_final", PRESET_NAMES)
        spec = preset_spec("tfg_final")
        self.assertTrue(spec["benchmark_capable"] and spec["ranking_capable"])
        self.assertEqual(len(spec["media_profile_ids"]), 4)  # paseo+blender x 30/60fps
        self.assertIn("blender_10min_60fps_4s", spec["media_profile_ids"])

    def test_comparativa_authorizes_ranking_gate(self):
        from core.phase6.analysis import evaluate_gates

        # Protocolo comparativa con todo correcto -> benchmark/ranking autorizado.
        protocol = {"preset": "comparativa", "benchmark_capable": True}
        sessions = [
            {"session_id": "s1", "synthetic": False, "source_split": "eval", "segment_duration_s": 4.0},
            {"session_id": "s2", "synthetic": True, "source_split": "eval", "segment_duration_s": 4.0},
        ]
        summaries = [
            {
                "session_id": "s1", "synthetic": False, "run_status": "completed", "evaluable": 1,
                "controller_alias": "base_robust_mpc", "segment_count": 6, "legacy_artifacts_present": 0,
            },
            {
                "session_id": "s2", "synthetic": True, "run_status": "completed", "evaluable": 1,
                "controller_alias": "base_robust_mpc", "segment_count": 6, "legacy_artifacts_present": 0,
            },
        ]
        gates = evaluate_gates(protocol, sessions, summaries)
        self.assertTrue(gates["all_gates_passed"])
        self.assertTrue(gates["benchmark_authorized"])
        self.assertTrue(gates["ranking_authorized"])


if __name__ == "__main__":
    unittest.main()
