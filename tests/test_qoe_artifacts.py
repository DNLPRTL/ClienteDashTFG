from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from core.evaluation.artifacts import (
    DRY_RUN_MANIFEST_FILENAME,
    DRY_RUN_SEGMENTS_FILENAME,
    DRY_RUN_SUMMARY_FILENAME,
    QOE_ARTIFACT_MANIFEST_FILENAME,
    QOE_RUN_SUMMARY_FILENAME,
    QOE_SEGMENT_REWARDS_FILENAME,
    QoEArtifactError,
    compute_qoe_artifacts_from_dry_run,
    compute_qoe_summary_from_segments_csv,
    load_segment_qoe_inputs_from_csv,
)


class QoEArtifactsTest(unittest.TestCase):
    def test_load_segment_qoe_inputs_from_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / DRY_RUN_SEGMENTS_FILENAME
            self._write_segments(path)

            segments = load_segment_qoe_inputs_from_csv(path)

        self.assertEqual(3, len(segments))
        self.assertEqual(1000.0, segments[0].bitrate_kbps)
        self.assertEqual(0.0, segments[0].rebuffer_s)

    def test_missing_required_column_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / DRY_RUN_SEGMENTS_FILENAME
            path.write_text("representation_bitrate_kbps\n1000\n", encoding="utf-8")

            with self.assertRaises(QoEArtifactError):
                load_segment_qoe_inputs_from_csv(path)

    def test_compute_qoe_summary_from_segments_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / DRY_RUN_SEGMENTS_FILENAME
            self._write_segments(path)

            summary = compute_qoe_summary_from_segments_csv(path, expected_segment_count=3)

        self.assertAlmostEqual(2.0, summary["qoe_sum"])
        self.assertAlmostEqual(2.0 / 3.0, summary["qoe_mean"])
        self.assertTrue(summary["session_completed"])

    def test_compute_qoe_artifacts_writes_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            dry_run = Path(tmp) / "dry_run"
            output = Path(tmp) / "qoe"
            self._write_dry_run(dry_run)

            result = compute_qoe_artifacts_from_dry_run(dry_run, output)

            summary = json.loads((output / QOE_RUN_SUMMARY_FILENAME).read_text(encoding="utf-8"))
            manifest = json.loads((output / QOE_ARTIFACT_MANIFEST_FILENAME).read_text(encoding="utf-8"))

        self.assertEqual("use_for_eval", result.session_eval_gate)
        self.assertEqual(3, result.segment_count)
        self.assertEqual(QOE_SEGMENT_REWARDS_FILENAME, Path(result.qoe_segment_rewards_path).name)
        self.assertAlmostEqual(2.0, summary["qoe_sum"])
        self.assertFalse(summary["outputs_are_benchmark_results"])
        self.assertFalse(summary["benchmark_performed"])
        self.assertFalse(summary["ranking_performed"])
        self.assertTrue(summary["no_final_ranking"])
        self.assertEqual("qoe_artifact_manifest_v1", manifest["schema_id"])

    def test_legacy_artifact_is_gated_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            dry_run = Path(tmp) / "dry_run"
            output = Path(tmp) / "qoe"
            self._write_dry_run(
                dry_run,
                manifest={
                    "legacy_dry_run": True,
                    "generated_before_phase_3_5a2": True,
                    "final_qoe_reward_defined": False,
                    "outputs_are_benchmark_results": False,
                    "row_eval_gate": "do_not_use_for_eval",
                    "gate_reasons": ["legacy_dry_run"],
                },
                row_gate="do_not_use_for_eval",
            )

            result = compute_qoe_artifacts_from_dry_run(dry_run, output)

        self.assertEqual("do_not_use_for_eval", result.session_eval_gate)
        self.assertIn("legacy_dry_run", result.gate_reasons)

    def test_incomplete_session_is_gated_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            dry_run = Path(tmp) / "dry_run"
            output = Path(tmp) / "qoe"
            self._write_dry_run(dry_run, summary={"expected_segment_count": 4, "session_completed": False})

            result = compute_qoe_artifacts_from_dry_run(dry_run, output)

        self.assertEqual("do_not_use_for_eval", result.session_eval_gate)
        self.assertIn("incomplete_session", result.gate_reasons)

    def test_source_claiming_benchmark_is_forced_out(self):
        with tempfile.TemporaryDirectory() as tmp:
            dry_run = Path(tmp) / "dry_run"
            output = Path(tmp) / "qoe"
            self._write_dry_run(
                dry_run,
                manifest={
                    "final_qoe_reward_defined": True,
                    "outputs_are_benchmark_results": True,
                    "no_final_ranking": False,
                },
            )

            result = compute_qoe_artifacts_from_dry_run(dry_run, output)
            summary = json.loads((output / QOE_RUN_SUMMARY_FILENAME).read_text(encoding="utf-8"))

        self.assertEqual("do_not_use_for_eval", result.session_eval_gate)
        self.assertIn("source_claims_benchmark_result", result.gate_reasons)
        self.assertFalse(summary["outputs_are_benchmark_results"])

    def _write_dry_run(
        self,
        path: Path,
        summary: dict[str, object] | None = None,
        manifest: dict[str, object] | None = None,
        row_gate: str = "use_for_eval",
    ) -> None:
        path.mkdir(parents=True, exist_ok=True)
        self._write_segments(path / DRY_RUN_SEGMENTS_FILENAME, row_gate=row_gate)
        (path / DRY_RUN_SUMMARY_FILENAME).write_text(
            json.dumps(summary or {"expected_segment_count": 3, "session_completed": True}),
            encoding="utf-8",
        )
        (path / DRY_RUN_MANIFEST_FILENAME).write_text(
            json.dumps(
                manifest
                or {
                    "final_qoe_reward_defined": True,
                    "outputs_are_benchmark_results": False,
                    "no_final_ranking": True,
                    "row_eval_gate": "use_for_eval",
                }
            ),
            encoding="utf-8",
        )

    def _write_segments(self, path: Path, row_gate: str = "use_for_eval") -> None:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["segment_index", "representation_bitrate_kbps", "rebuffer_s", "row_eval_gate"],
            )
            writer.writeheader()
            for index, bitrate in enumerate((1000, 2000, 1000)):
                writer.writerow(
                    {
                        "segment_index": index,
                        "representation_bitrate_kbps": bitrate,
                        "rebuffer_s": 0,
                        "row_eval_gate": row_gate,
                    }
                )


if __name__ == "__main__":
    unittest.main()
