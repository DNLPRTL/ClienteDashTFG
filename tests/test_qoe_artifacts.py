from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest

from core.evaluation.artifacts import (
    QOE_ARTIFACT_MANIFEST_FILENAME,
    QOE_RUN_SUMMARY_FILENAME,
    QOE_SEGMENT_REWARDS_FILENAME,
    QoEArtifactError,
    compute_qoe_artifacts_from_dry_run,
    load_segment_qoe_inputs_from_csv,
)


class QoEArtifactsTest(unittest.TestCase):
    def test_load_segment_qoe_inputs_sorts_by_segment_index(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            segments_path = os.path.join(temp_dir, "trace_dry_run_segments.csv")
            self.write_segments_csv(
                segments_path,
                rows=[
                    self.segment_row(2, 1000),
                    self.segment_row(0, 1000),
                    self.segment_row(1, 2000),
                ],
            )

            inputs = load_segment_qoe_inputs_from_csv(segments_path)

        self.assertEqual(3, len(inputs))
        self.assertEqual([1000.0, 2000.0, 1000.0], [item.bitrate_kbps for item in inputs])

    def test_compute_qoe_artifacts_from_eval_source_rows(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            dry_run_dir = os.path.join(temp_dir, "dry")
            output_dir = os.path.join(temp_dir, "qoe")
            self.write_dry_run_dir(
                dry_run_dir,
                rows=[
                    self.segment_row(0, 1000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                    self.segment_row(1, 2000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                    self.segment_row(2, 1000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                ],
                segment_count=3,
            )

            result = compute_qoe_artifacts_from_dry_run(dry_run_dir, output_dir)

            summary = self.read_json(os.path.join(output_dir, QOE_RUN_SUMMARY_FILENAME))
            self.assertTrue(os.path.isfile(result.qoe_run_summary_path))
            self.assertTrue(os.path.isfile(os.path.join(output_dir, QOE_SEGMENT_REWARDS_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(output_dir, QOE_ARTIFACT_MANIFEST_FILENAME)))

        self.assertAlmostEqual(2.0, summary["qoe_linear_sum"])
        self.assertAlmostEqual(2.0 / 3.0, summary["qoe_linear_mean"])
        self.assertEqual("use_for_eval", summary["session_eval_gate"])
        self.assertFalse(summary["outputs_are_benchmark_results"])
        self.assertTrue(summary["no_final_ranking"])

    def test_compute_qoe_artifacts_from_legacy_non_eval_rows(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            dry_run_dir = os.path.join(temp_dir, "dry")
            output_dir = os.path.join(temp_dir, "qoe")
            self.write_dry_run_dir(
                dry_run_dir,
                rows=[
                    self.segment_row(0, 1000, row_eval_gate="do_not_use_for_eval"),
                    self.segment_row(1, 2000, row_eval_gate="do_not_use_for_eval"),
                    self.segment_row(2, 1000, row_eval_gate="do_not_use_for_eval"),
                ],
                segment_count=3,
            )

            compute_qoe_artifacts_from_dry_run(dry_run_dir, output_dir)
            summary = self.read_json(os.path.join(output_dir, QOE_RUN_SUMMARY_FILENAME))

        self.assertAlmostEqual(2.0, summary["qoe_linear_sum"])
        self.assertEqual("do_not_use_for_eval", summary["session_eval_gate"])
        self.assertIn("legacy_dry_run", summary["gate_reasons"])
        self.assertIn("generated_before_phase_3_5a2", summary["gate_reasons"])
        self.assertFalse(summary["outputs_are_benchmark_results"])
        self.assertTrue(summary["no_final_ranking"])

    def test_incomplete_expected_segment_count_gates_session(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            dry_run_dir = os.path.join(temp_dir, "dry")
            output_dir = os.path.join(temp_dir, "qoe")
            self.write_dry_run_dir(
                dry_run_dir,
                rows=[
                    self.segment_row(0, 1000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                    self.segment_row(1, 2000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                ],
                segment_count=2,
            )

            compute_qoe_artifacts_from_dry_run(dry_run_dir, output_dir, expected_segment_count=3)
            summary = self.read_json(os.path.join(output_dir, QOE_RUN_SUMMARY_FILENAME))

        self.assertFalse(summary["session_completed"])
        self.assertEqual("do_not_use_for_eval", summary["session_eval_gate"])
        self.assertIn("incomplete_session", summary["gate_reasons"])

    def test_missing_required_column_raises_qoe_artifact_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            segments_path = os.path.join(temp_dir, "trace_dry_run_segments.csv")
            fieldnames = [name for name in self.segment_fieldnames() if name != "rebuffer_s"]
            self.write_segments_csv(
                segments_path,
                rows=[self.segment_row(0, 1000)],
                fieldnames=fieldnames,
            )

            with self.assertRaisesRegex(QoEArtifactError, "missing_required_column"):
                load_segment_qoe_inputs_from_csv(segments_path)

    def test_multiple_controller_names_raise_qoe_artifact_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            segments_path = os.path.join(temp_dir, "trace_dry_run_segments.csv")
            self.write_segments_csv(
                segments_path,
                rows=[
                    self.segment_row(0, 1000, controller_name="controller-a"),
                    self.segment_row(1, 2000, controller_name="controller-b"),
                ],
            )

            with self.assertRaises(QoEArtifactError):
                load_segment_qoe_inputs_from_csv(segments_path)

    def test_multiple_trace_ids_raise_qoe_artifact_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            segments_path = os.path.join(temp_dir, "trace_dry_run_segments.csv")
            self.write_segments_csv(
                segments_path,
                rows=[
                    self.segment_row(0, 1000, trace_id="trace-a"),
                    self.segment_row(1, 2000, trace_id="trace-b"),
                ],
            )

            with self.assertRaises(QoEArtifactError):
                load_segment_qoe_inputs_from_csv(segments_path)

    def test_log_qoe_is_computed_only_with_explicit_min_bitrate(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            dry_run_dir = os.path.join(temp_dir, "dry")
            no_log_output = os.path.join(temp_dir, "qoe-no-log")
            log_output = os.path.join(temp_dir, "qoe-log")
            self.write_dry_run_dir(
                dry_run_dir,
                rows=[
                    self.segment_row(0, 1000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                    self.segment_row(1, 2000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                ],
                segment_count=2,
            )

            compute_qoe_artifacts_from_dry_run(dry_run_dir, no_log_output)
            no_log_summary = self.read_json(os.path.join(no_log_output, QOE_RUN_SUMMARY_FILENAME))
            compute_qoe_artifacts_from_dry_run(dry_run_dir, log_output, min_bitrate_kbps=1000.0)
            log_summary = self.read_json(os.path.join(log_output, QOE_RUN_SUMMARY_FILENAME))

        self.assertFalse(no_log_summary["log_qoe_computed"])
        self.assertTrue(log_summary["log_qoe_computed"])
        self.assertAlmostEqual(0.0, log_summary["qoe_log_sum"])
        self.assertAlmostEqual(0.0, log_summary["qoe_log_mean"])
        self.assertAlmostEqual(1000.0, log_summary["qoe_log_min_bitrate_kbps"])

    def test_cli_computes_qoe_artifacts_from_tempfile_dry_run(self):
        repo_root = os.path.dirname(os.path.dirname(__file__))
        script_path = os.path.join(repo_root, "scripts", "compute_qoe_from_dry_run.py")
        with tempfile.TemporaryDirectory() as temp_dir:
            dry_run_dir = os.path.join(temp_dir, "dry")
            output_dir = os.path.join(temp_dir, "qoe")
            self.write_dry_run_dir(
                dry_run_dir,
                rows=[
                    self.segment_row(0, 1000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                    self.segment_row(1, 2000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                    self.segment_row(2, 1000, row_eval_gate="use_for_eval", final_qoe_reward_defined=True),
                ],
                segment_count=3,
            )

            completed = subprocess.run(
                [
                    sys.executable,
                    script_path,
                    "--dry-run-dir",
                    dry_run_dir,
                    "--output-dir",
                    output_dir,
                ],
                cwd=repo_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            self.assertEqual("", completed.stderr)
            self.assertEqual(0, completed.returncode)
            self.assertIn("qoe_linear_mean:", completed.stdout)
            self.assertTrue(os.path.isfile(os.path.join(output_dir, QOE_RUN_SUMMARY_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(output_dir, QOE_SEGMENT_REWARDS_FILENAME)))
            self.assertTrue(os.path.isfile(os.path.join(output_dir, QOE_ARTIFACT_MANIFEST_FILENAME)))

    def test_no_persistent_fixtures_datasets_logs_zips_pdfs_or_media_are_added(self):
        forbidden_extensions = {".csv", ".log", ".zip", ".pdf", ".mp4", ".m4s", ".mpd"}
        tests_dir = os.path.dirname(__file__)
        found = []
        for root, _dirs, files in os.walk(tests_dir):
            for filename in files:
                if os.path.splitext(filename)[1].lower() in forbidden_extensions:
                    found.append(os.path.join(root, filename))
        self.assertEqual([], found)

    def write_dry_run_dir(self, directory, rows, segment_count):
        os.makedirs(directory, exist_ok=True)
        self.write_segments_csv(os.path.join(directory, "trace_dry_run_segments.csv"), rows)
        summary = {
            "artifact_type": "trace_dry_run_summary",
            "segment_count": segment_count,
            "outputs_are_benchmark_results": False,
            "final_qoe_reward_defined": False,
            "no_final_ranking": True,
        }
        manifest = {
            "artifact_type": "trace_dry_run_manifest",
            "outputs_are_benchmark_results": False,
            "final_qoe_reward_defined": False,
            "no_final_ranking": True,
        }
        self.write_json(os.path.join(directory, "trace_dry_run_summary.json"), summary)
        self.write_json(os.path.join(directory, "trace_dry_run_manifest.json"), manifest)

    def write_segments_csv(self, path, rows, fieldnames=None):
        fieldnames = fieldnames or self.segment_fieldnames()
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow({field: row.get(field, "") for field in fieldnames})

    def write_json(self, path, payload):
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle)

    def read_json(self, path):
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def segment_fieldnames(self):
        return [
            "segment_index",
            "representation_bitrate_kbps",
            "rebuffer_s",
            "controller_name",
            "trace_id",
            "row_eval_gate",
            "outputs_are_benchmark_results",
            "final_qoe_reward_defined",
            "no_final_ranking",
            "phase",
            "phase_label",
            "schema_version",
            "segment_duration_s",
            "buffer_before_s",
            "buffer_after_s",
            "download_duration_s",
            "measured_throughput_kbps",
        ]

    def segment_row(
        self,
        segment_index,
        bitrate_kbps,
        rebuffer_s=0.0,
        controller_name="test_controller",
        trace_id="test_trace",
        row_eval_gate="use_for_eval",
        outputs_are_benchmark_results=False,
        final_qoe_reward_defined=False,
        no_final_ranking=True,
    ):
        return {
            "segment_index": str(segment_index),
            "representation_bitrate_kbps": str(bitrate_kbps),
            "rebuffer_s": str(rebuffer_s),
            "controller_name": controller_name,
            "trace_id": trace_id,
            "row_eval_gate": row_eval_gate,
            "outputs_are_benchmark_results": str(outputs_are_benchmark_results).lower(),
            "final_qoe_reward_defined": str(final_qoe_reward_defined).lower(),
            "no_final_ranking": str(no_final_ranking).lower(),
            "phase": "phase3_4c_dry_run",
            "phase_label": "3.4C",
            "schema_version": "synthetic",
            "segment_duration_s": "2.0",
            "buffer_before_s": "0.0",
            "buffer_after_s": "2.0",
            "download_duration_s": "0.1",
            "measured_throughput_kbps": "1000.0",
        }


if __name__ == "__main__":
    unittest.main()
