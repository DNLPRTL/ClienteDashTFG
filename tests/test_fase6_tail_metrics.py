from __future__ import annotations

import unittest

from core.fase6.analisis import agregar_resumenes, estadistica_pareada

_NUMERIC_DEFAULTS = {
    "qoe_log_mean": 0.0,
    "avg_bitrate_kbps": 2000.0,
    "avg_quality_mbps": 2.0,
    "total_rebuffer_s": 0.0,
    "smoothness_penalty": 0.0,
    "positive_smoothness_mbps": 0.0,
    "negative_smoothness_mbps": 0.0,
    "switching_rate": 0.0,
    "avg_buffer_s": 10.0,
    "low_buffer_ratio": 0.0,
    "avg_download_time_s": 1.0,
    "avg_measured_throughput_kbps": 3000.0,
    "avg_chunk_size_bytes": 100000.0,
    "decision_latency_ms_mean": 1.0,
    "decision_latency_ms_p95": 2.0,
    "fallback_row_count": 0,
    "neural_audit_missing_row_count": 0,
    "neural_inference_ms_mean": 0.0,
    "neural_inference_ms_p95": 0.0,
}


def _summary(alias, window, qoe, rebuffer_ratio=0.0, stall_events=0, total_rebuffer_s=0.0):
    row = {
        "evaluable": 1,
        "synthetic": False,
        "controller_alias": alias,
        "controller_display_name": alias,
        "media_profile_id": "paseo_10min_30fps_4s",
        "trace_window_id": window,
        "repetition": 1,
        "qoe_linear_mean": float(qoe),
        "rebuffer_ratio": float(rebuffer_ratio),
        "stall_event_count": int(stall_events),
    }
    row.update(_NUMERIC_DEFAULTS)
    row["total_rebuffer_s"] = float(total_rebuffer_s)
    return row


def _summaries():
    windows = ["tw0", "tw1", "tw2", "tw3", "tw4"]
    robust_qoe = [1.0, 2.0, 3.0, 4.0, 5.0]
    prudent_qoe = [1.5, 2.0, 3.0, 3.5, 4.0]
    robust_rebuf = [0.0, 0.0, 6.0, 12.0, 20.0]
    rows = []
    for i, w in enumerate(windows):
        rows.append(
            _summary(
                "base_robust_mpc", w, robust_qoe[i],
                rebuffer_ratio=0.01 * i, stall_events=1 if i < 2 else 0, total_rebuffer_s=robust_rebuf[i],
            )
        )
        rows.append(_summary("propio_mpc_prudente", w, prudent_qoe[i], rebuffer_ratio=0.005 * i, stall_events=0))
    return rows


class Phase6TailMetricsTest(unittest.TestCase):
    def test_aggregate_has_tail_and_stability_fields(self):
        aggregates = {row["controller_alias"]: row for row in agregar_resumenes(_summaries())}
        robust = aggregates["base_robust_mpc"]
        self.assertAlmostEqual(robust["qoe_linear_min"], 1.0)
        self.assertAlmostEqual(robust["qoe_linear_median"], 3.0)
        # P5 cae entre el mínimo y la mediana (cola inferior)
        self.assertLessEqual(robust["qoe_linear_min"], robust["qoe_linear_p05"])
        self.assertLessEqual(robust["qoe_linear_p05"], robust["qoe_linear_median"])
        self.assertGreater(robust["qoe_linear_std"], 0.0)
        self.assertIn("rebuffer_ratio_p95", robust)
        # robust tiene stalls en 2 de 5 sesiones
        self.assertAlmostEqual(robust["stall_session_rate"], 0.4)
        # el prudente no tiene stalls
        self.assertAlmostEqual(aggregates["propio_mpc_prudente"]["stall_session_rate"], 0.0)
        # sesiones catastroficas (robust: rebuffer [0,0,6,12,20])
        self.assertAlmostEqual(robust["total_rebuffer_s_max"], 20.0)
        self.assertAlmostEqual(robust["session_gt_5s_rebuffer_rate"], 0.6)
        self.assertAlmostEqual(robust["session_gt_10s_rebuffer_rate"], 0.4)
        self.assertAlmostEqual(robust["worst_5pct_rebuffer_mean_s"], 20.0)

    def test_paired_has_worst_case_delta(self):
        stats = estadistica_pareada(_summaries())
        deltas = {row["controller_alias"]: row for row in stats["deltas_vs_baseline"]}
        prudent = deltas["propio_mpc_prudente"]
        self.assertIn("delta_qoe_linear_p05", prudent)
        self.assertIn("delta_qoe_linear_worst", prudent)
        # peor delta emparejado: tw4 -> 4.0 - 5.0 = -1.0
        self.assertAlmostEqual(prudent["delta_qoe_linear_worst"], -1.0)


if __name__ == "__main__":
    unittest.main()
