from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from core.phase45_v3.policy_collapse_audit import audit_phase6_policy_collapse


class Phase45V3AntiCollapseGateTest(unittest.TestCase):
    def test_audit_fails_spbc_like_high_capacity_action0_collapse(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_phase6_package(root, collapsed=True)

            report = audit_phase6_policy_collapse(root)

        self.assertEqual("FAIL", report["status"])
        self.assertIn("high_capacity_safe_action0_rate", report["gate_failures"])
        self.assertGreater(report["metrics"]["high_capacity_safe_action0_rate"], 0.05)

    def test_audit_passes_non_collapsed_high_capacity_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_phase6_package(root, collapsed=False)

            report = audit_phase6_policy_collapse(root)

        self.assertEqual("PASS", report["status"])
        self.assertFalse(report["collapse_detected"])


def _write_phase6_package(root: Path, *, collapsed: bool) -> None:
    results = root / "02_resultados"
    results.mkdir(parents=True)
    raw_fields = [
        "bitrate_kbps",
        "buffer_s",
        "chunk_index",
        "controller_alias",
        "fallback_used",
        "measured_throughput_kbps",
        "media_profile_id",
        "neural_fallback_reason",
        "neural_safe_action",
        "qoe_linear_reward",
        "rebuffer_s",
        "repetition",
        "segment_index",
        "session_id",
        "synthetic",
        "trace_window_id",
    ]
    raw_rows = []
    for alias, session_id in (
        ("base_robust_mpc", "s001_base"),
        ("propio_spbc_v2_anchor", "s002_spbc"),
    ):
        for chunk in range(1, 10):
            if alias == "base_robust_mpc":
                bitrate, action = 4300.0, ""
            elif collapsed:
                bitrate, action = 300.0, "0"
            else:
                bitrate, action = 4300.0, "5"
            raw_rows.append(
                {
                    "bitrate_kbps": bitrate,
                    "buffer_s": 20.0 + chunk,
                    "chunk_index": chunk,
                    "controller_alias": alias,
                    "fallback_used": 0,
                    "measured_throughput_kbps": 10000.0,
                    "media_profile_id": "paseo_10min_30fps_4s",
                    "neural_fallback_reason": "success_neural" if alias.startswith("propio") else "",
                    "neural_safe_action": action,
                    "qoe_linear_reward": 4.3 if bitrate == 4300.0 else 0.3,
                    "rebuffer_s": 0.0,
                    "repetition": 1,
                    "segment_index": chunk + 1,
                    "session_id": session_id,
                    "synthetic": 0,
                    "trace_window_id": "real_high",
                }
            )
    _write_csv(results / "raw_chunks.csv", raw_fields, raw_rows)

    summary_fields = [
        "avg_bitrate_kbps",
        "controller_alias",
        "media_profile_id",
        "qoe_linear_mean",
        "repetition",
        "synthetic",
        "total_rebuffer_s",
        "trace_window_id",
    ]
    target_qoe = 0.3 if collapsed else 4.3
    target_bitrate = 300.0 if collapsed else 4300.0
    _write_csv(
        results / "session_summary.csv",
        summary_fields,
        [
            {
                "avg_bitrate_kbps": 4300.0,
                "controller_alias": "base_robust_mpc",
                "media_profile_id": "paseo_10min_30fps_4s",
                "qoe_linear_mean": 4.3,
                "repetition": 1,
                "synthetic": 0,
                "total_rebuffer_s": 0.0,
                "trace_window_id": "real_high",
            },
            {
                "avg_bitrate_kbps": target_bitrate,
                "controller_alias": "propio_spbc_v2_anchor",
                "media_profile_id": "paseo_10min_30fps_4s",
                "qoe_linear_mean": target_qoe,
                "repetition": 1,
                "synthetic": 0,
                "total_rebuffer_s": 0.0,
                "trace_window_id": "real_high",
            },
        ],
    )


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
