from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest

from core.trace_replay.controller_adapter import (
    ControllerAdapterError,
    ControllerDecision,
    ExistingControllerAdapter,
)
from core.trace_replay.dry_run import (
    ROW_EVAL_GATE,
    TraceDryRunConfig,
    build_representations_from_kbps,
    estimate_segment_size_bytes,
    run_trace_dry_run,
    write_trace_dry_run_artifacts,
)
from core.trace_replay.loader import load_normalized_trace_rows


class DeterministicAdapter:
    def __init__(self, representation_index=0):
        self._representation_index = representation_index
        self.feedback_seen = []
        self.reset_count = 0

    @property
    def name(self):
        return "deterministic_test"

    def reset(self):
        self.reset_count += 1

    def decide(self, feedback):
        self.feedback_seen.append(dict(feedback))
        return ControllerDecision(
            representation_index=self._representation_index,
            reason="test_fixed_index",
            raw_controller_output={"representation_index": self._representation_index},
        )


class MappingOutputController:
    def __init__(self, raw_output):
        self.raw_output = raw_output
        self.feedback = None

    def setPlayerFeedback(self, feedback):
        self.feedback = feedback

    def calcControlAction(self):
        return self.raw_output


class TraceDryRunTest(unittest.TestCase):
    def test_build_representations_from_kbps_builds_ordered_ladder_with_indices(self):
        representations = build_representations_from_kbps([1200, 300, 750])

        self.assertEqual([0, 1, 2], [representation.index for representation in representations])
        self.assertEqual([300.0, 750.0, 1200.0], [representation.bitrate_kbps for representation in representations])
        self.assertEqual(["300kbps", "750kbps", "1200kbps"], [representation.label for representation in representations])

    def test_estimate_segment_size_bytes_is_coherent(self):
        self.assertEqual(250000, estimate_segment_size_bytes(1000, 2.0))
        self.assertEqual(75000, estimate_segment_size_bytes(300, 2.0))

    def test_run_trace_dry_run_works_with_constant_trace_and_deterministic_adapter(self):
        result = run_trace_dry_run(
            self.constant_trace(throughput_kbps=1000.0),
            DeterministicAdapter(representation_index=1),
            self.config(segment_count=3, initial_buffer_s=1.0),
        )

        self.assertEqual("synthetic-trace", result.trace_id)
        self.assertEqual("deterministic_test", result.controller_name)
        self.assertEqual("3.4C", result.phase)
        self.assertFalse(result.outputs_are_benchmark_results)
        self.assertFalse(result.final_qoe_reward_defined)
        self.assertTrue(result.no_final_ranking)
        self.assertEqual(3, result.segment_count)
        self.assertEqual(3, len(result.records))
        self.assertTrue(all(record.representation_index == 1 for record in result.records))

    def test_dry_run_records_one_row_per_segment(self):
        result = run_trace_dry_run(
            self.constant_trace(),
            DeterministicAdapter(),
            self.config(segment_count=4, initial_buffer_s=1.0),
        )

        self.assertEqual([0, 1, 2, 3], [record.segment_index for record in result.records])

    def test_buffer_model_increases_after_downloaded_segment_and_decreases_by_download_time(self):
        result = run_trace_dry_run(
            self.constant_trace(throughput_kbps=1000.0),
            DeterministicAdapter(representation_index=0),
            self.config(segment_count=1, initial_buffer_s=1.0),
        )

        record = result.records[0]
        self.assertAlmostEqual(1.0, record.buffer_before_s)
        self.assertAlmostEqual(0.6, record.download_duration_s)
        self.assertAlmostEqual(2.4, record.buffer_after_s)
        self.assertAlmostEqual(0.0, record.rebuffer_s)

    def test_rebuffer_is_positive_when_download_duration_exceeds_available_buffer(self):
        result = run_trace_dry_run(
            self.constant_trace(throughput_kbps=100.0, duration_s=20.0),
            DeterministicAdapter(representation_index=0),
            self.config(segment_count=1, initial_buffer_s=1.0),
        )

        record = result.records[0]
        self.assertAlmostEqual(6.0, record.download_duration_s)
        self.assertAlmostEqual(5.0, record.rebuffer_s)
        self.assertAlmostEqual(2.0, record.buffer_after_s)

    def test_output_artifacts_are_written_to_tempfile_output_directory(self):
        result = run_trace_dry_run(
            self.constant_trace(),
            DeterministicAdapter(),
            self.config(segment_count=2, initial_buffer_s=1.0),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            artifacts = write_trace_dry_run_artifacts(result, temp_dir)
            for path in artifacts.values():
                self.assertTrue(os.path.isfile(path))

            with open(artifacts["manifest"], "r", encoding="utf-8") as handle:
                manifest = json.load(handle)
            with open(artifacts["summary"], "r", encoding="utf-8") as handle:
                summary = json.load(handle)
            with open(artifacts["segments"], "r", newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))

        self.assertFalse(manifest["outputs_are_benchmark_results"])
        self.assertFalse(summary["outputs_are_benchmark_results"])
        self.assertFalse(manifest["final_qoe_reward_defined"])
        self.assertFalse(summary["final_qoe_reward_defined"])
        self.assertEqual(ROW_EVAL_GATE, manifest["row_eval_gate"])
        self.assertEqual(ROW_EVAL_GATE, summary["row_eval_gate"])
        self.assertEqual(ROW_EVAL_GATE, rows[0]["row_eval_gate"])
        self.assertEqual("false", rows[0]["outputs_are_benchmark_results"])
        self.assertEqual("false", rows[0]["final_qoe_reward_defined"])

    def test_controller_adapter_clamps_invalid_index_decisions_consistently(self):
        adapter = ExistingControllerAdapter(
            "test_mapping",
            controller=MappingOutputController({"representation_index": 99}),
        )

        decision = adapter.decide(self.complete_controller_feedback())

        self.assertEqual(2, decision.representation_index)
        self.assertIn("clamped", decision.reason)

    def test_controller_adapter_can_reject_invalid_index_decisions(self):
        adapter = ExistingControllerAdapter(
            "test_mapping",
            controller=MappingOutputController({"representation_index": -1}),
            invalid_decision_policy="reject",
        )

        with self.assertRaisesRegex(ControllerAdapterError, "outside ladder"):
            adapter.decide(self.complete_controller_feedback())

    def test_adapter_feedback_does_not_include_full_trace_or_future_samples(self):
        adapter = DeterministicAdapter()
        run_trace_dry_run(
            self.constant_trace(),
            adapter,
            self.config(segment_count=2, initial_buffer_s=1.0),
        )

        forbidden = {
            "trace",
            "loaded_trace",
            "full_trace",
            "trace_samples",
            "samples",
            "future_samples",
            "future_throughput",
            "raw_trace_metadata",
            "trace_metadata",
            "metadata",
            "ood_label",
        }
        self.assertEqual(2, len(adapter.feedback_seen))
        for feedback in adapter.feedback_seen:
            self.assertFalse(forbidden.intersection(feedback))
            self.assertIn("bwe", feedback)
            self.assertIn("queued_time", feedback)
            self.assertIn("rates", feedback)
            self.assertNotIn("throughput_kbps", feedback)

    def test_cli_works_with_synthetic_trace_and_supported_controller(self):
        repo_root = os.path.dirname(os.path.dirname(__file__))
        script_path = os.path.join(repo_root, "scripts", "run_trace_dry_run.py")
        with tempfile.TemporaryDirectory() as temp_dir:
            trace_path = os.path.join(temp_dir, "cli_synthetic.csv")
            output_dir = os.path.join(temp_dir, "dry_run_output")
            self.write_trace_csv(trace_path)

            completed = subprocess.run(
                [
                    sys.executable,
                    script_path,
                    "--trace-csv",
                    trace_path,
                    "--controller",
                    "min_rate",
                    "--output-dir",
                    output_dir,
                    "--segment-count",
                    "2",
                    "--segment-duration-s",
                    "2.0",
                    "--representation-kbps",
                    "300,750,1200",
                    "--end-policy",
                    "loop",
                    "--max-loops",
                    "3",
                    "--overwrite",
                ],
                cwd=repo_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            self.assertEqual("", completed.stderr)
            self.assertEqual(0, completed.returncode)
            self.assertIn("trace_id: cli_synthetic", completed.stdout)
            self.assertTrue(os.path.isfile(os.path.join(output_dir, "trace_dry_run_manifest.json")))
            self.assertTrue(os.path.isfile(os.path.join(output_dir, "trace_dry_run_segments.csv")))
            self.assertTrue(os.path.isfile(os.path.join(output_dir, "trace_dry_run_summary.json")))

    def test_existing_controller_adapter_imports_current_contract_and_registry(self):
        adapter = ExistingControllerAdapter("min_rate")
        decision = adapter.decide(self.complete_controller_feedback())

        self.assertEqual("min_rate", adapter.name)
        self.assertEqual(0, decision.representation_index)

    def test_no_persistent_fixtures_datasets_logs_zips_pdfs_or_media_are_added(self):
        forbidden_extensions = {".csv", ".log", ".zip", ".pdf", ".mp4", ".m4s", ".mpd"}
        tests_dir = os.path.dirname(__file__)
        found = []
        for root, _dirs, files in os.walk(tests_dir):
            for filename in files:
                if os.path.splitext(filename)[1].lower() in forbidden_extensions:
                    found.append(os.path.join(root, filename))
        self.assertEqual([], found)

    def config(self, segment_count=1, initial_buffer_s=0.0):
        return TraceDryRunConfig(
            segment_duration_s=2.0,
            segment_count=segment_count,
            representations=build_representations_from_kbps([300, 750, 1200]),
            initial_buffer_s=initial_buffer_s,
            end_policy="loop",
            max_loops=3,
        )

    def constant_trace(self, throughput_kbps=1000.0, duration_s=20.0):
        return load_normalized_trace_rows(
            [
                {
                    "timestamp_s": "0",
                    "duration_s": str(duration_s),
                    "throughput_kbps": str(throughput_kbps),
                    "mobility_label": "synthetic-stationary",
                }
            ],
            trace_id="synthetic-trace",
            source="synthetic-memory",
        )

    def complete_controller_feedback(self):
        rates = [37500.0, 93750.0, 150000.0]
        return {
            "queued_bytes": 0,
            "queued_time": 0.0,
            "cur_bitrate": rates[0],
            "bwe": 0.0,
            "level": 0,
            "max_level": 2,
            "cur_rate": rates[0],
            "max_rate": rates[-1],
            "min_rate": rates[0],
            "max_bitrate": rates[-1],
            "min_bitrate": rates[0],
            "last_fragment_size": 0,
            "last_download_time": 0.0,
            "downloaded_bytes": 0,
            "fragment_duration": 2.0,
            "rates": rates,
            "segment_index": 0,
            "start_segment_request": 0.0,
            "stop_segment_request": 0.0,
        }

    def write_trace_csv(self, path):
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["timestamp_s", "duration_s", "throughput_kbps"])
            writer.writeheader()
            writer.writerow({"timestamp_s": "0", "duration_s": "20", "throughput_kbps": "1000"})


if __name__ == "__main__":
    unittest.main()
