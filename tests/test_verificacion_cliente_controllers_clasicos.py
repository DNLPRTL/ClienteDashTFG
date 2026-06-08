from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from core.dataset_schema import build_evaluation_segments_header
from core.output_artifacts import (
    ENVIRONMENT_FILENAME,
    EVALUATION_SEGMENTS_FILENAME,
    RESOLVED_CONFIG_FILENAME,
    RUN_LOG_FILENAME,
    RUN_MANIFEST_FILENAME,
    SEGMENT_TELEMETRY_FILENAME,
)
from scripts import verificar_cliente_y_controllers_clasicos as verifier


class VerificacionTheoryProbeTest(unittest.TestCase):
    def test_theory_probes_cover_all_classic_controllers(self):
        for controller in verifier.CLASSIC_CONTROLLERS:
            with self.subTest(controller=controller):
                result = verifier.run_theory_probe(controller)

                self.assertEqual([], result.errors)
                self.assertEqual("accepted", result.status)
                self.assertEqual(controller, result.controller)
                self.assertIn("chosen_level", result.data)
                self.assertIn("target_rate_Bps", result.data)
                self.assertIn("metrics", result.data)

    def test_controller_list_rejects_non_classic_controllers(self):
        with self.assertRaises(SystemExit):
            verifier.normalize_controller_list(["rate_based", "neural_abr_lite_robust_mpc"])


class VerificacionRunAuditTest(unittest.TestCase):
    def test_audit_accepts_clean_classic_run_artifacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir) / "run_20260608_120000"
            build_fake_run(run_dir, controller="bba")

            result = verifier.audit_run_directory(run_dir, expected_controller="bba")

            self.assertEqual([], result.errors)
            self.assertEqual("accepted", result.status)
            self.assertTrue(result.data["required_artifacts_present"])
            self.assertTrue(result.data["legacy_artifacts_absent"])
            self.assertTrue(result.data["evaluation_segments_clean"])
            self.assertEqual([], result.data["neural_columns_present"])
            self.assertEqual(1, result.data["decision_summary"]["checked_policy_decisions"])

    def test_audit_rejects_legacy_and_neural_artifacts_in_classic_run(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir) / "run_20260608_120000"
            build_fake_run(
                run_dir,
                controller="rate_based",
                segment_extra_header=["feedback_neural_model_label"],
            )
            (run_dir / "dataset.csv").write_text("legacy\n", encoding="utf-8")

            result = verifier.audit_run_directory(run_dir, expected_controller="rate_based")

            self.assertEqual("failed", result.status)
            self.assertTrue(any("artifact legacy" in error for error in result.errors))
            self.assertTrue(any("columnas IA" in error for error in result.errors))

    def test_report_uses_public_phase_name(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_root = Path(temp_dir)
            summary = verifier.build_summary(
                started_at="2026-06-08T12:00:00+0200",
                mpd_url="http://example.invalid/video.mpd",
                output_root=output_root,
                controllers=["bba"],
                theory_results=[verifier.run_theory_probe("bba")],
                smoke_results=[],
                gstreamer_result=None,
            )

            report = verifier.render_report(summary)

            self.assertIn("Fase de Verificacion", report)
            self.assertNotIn("5" + "_5", report)
            self.assertNotIn("Phase " + "5.5", report)


def build_fake_run(run_dir: Path, controller: str, segment_extra_header=None) -> None:
    segment_extra_header = list(segment_extra_header or [])
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / RUN_MANIFEST_FILENAME).write_text(
        json.dumps(
            {
                "status": "completed",
                "controller": {"name": controller, "params": {}},
                "benchmark_neutrality": {
                    "outputs_are_benchmark_results": False,
                    "final_qoe_reward_defined": False,
                    "final_training_dataset_defined": False,
                },
            }
        ),
        encoding="utf-8",
    )
    (run_dir / RESOLVED_CONFIG_FILENAME).write_text("{}", encoding="utf-8")
    (run_dir / ENVIRONMENT_FILENAME).write_text("{}", encoding="utf-8")
    (run_dir / RUN_LOG_FILENAME).write_text("ok\n", encoding="utf-8")

    segment_header = [
        "segment_index",
        "feedback_queued_time",
        "feedback_bwe",
        "feedback_rates",
        "policy_chosen_level",
        "policy_target_rate",
        "policy_decision_ms",
        "eval_phase",
        "use_for_eval",
    ] + segment_extra_header
    segment_row = {
        "segment_index": "1",
        "feedback_queued_time": "8.0",
        "feedback_bwe": "1000.0",
        "feedback_rates": "[100.0, 200.0, 400.0]",
        "policy_chosen_level": "1",
        "policy_target_rate": "200.0",
        "policy_decision_ms": "0.2",
        "eval_phase": "startup",
        "use_for_eval": "0",
    }
    for header in segment_extra_header:
        segment_row[header] = ""
    with (run_dir / SEGMENT_TELEMETRY_FILENAME).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=segment_header)
        writer.writeheader()
        writer.writerow(segment_row)

    eval_header = build_evaluation_segments_header()
    eval_row = {
        "segment_index": "1",
        "is_init": "0",
        "eval_phase": "startup",
        "use_for_eval": "0",
        "last_fragment_size": "1000",
        "last_download_time": "1.0",
        "fragment_duration": "4.0",
    }
    with (run_dir / EVALUATION_SEGMENTS_FILENAME).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=eval_header)
        writer.writeheader()
        writer.writerow(eval_row)


if __name__ == "__main__":
    unittest.main()
