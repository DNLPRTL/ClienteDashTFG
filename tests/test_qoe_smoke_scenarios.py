from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from core.evaluation.artifacts import (
    QOE_ARTIFACT_MANIFEST_FILENAME,
    QOE_RUN_SUMMARY_FILENAME,
    QOE_SEGMENT_REWARDS_FILENAME,
)
from scripts.run_qoe_smoke_scenarios import (
    SMOKE_REPORT_FILENAME,
    run_qoe_smoke_scenarios,
)


class QoESmokeScenariosTest(unittest.TestCase):

    def test_run_qoe_smoke_scenarios_generates_report_and_checks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_root = os.path.join(temp_dir, "phase3_5d_smoke")

            report = run_qoe_smoke_scenarios(output_root)
            report_path = os.path.join(output_root, SMOKE_REPORT_FILENAME)

            self.assertTrue(os.path.isfile(report_path))
            self.assertTrue(report["all_checks_passed"])
            self.assertFalse(report["outputs_are_benchmark_results"])
            self.assertTrue(report["no_final_ranking"])
            self.assertFalse(report["ranking_performed"])
            self.assertFalse(report["benchmark_performed"])
            self.assertEqual(4, report["scenario_count"])

    def test_expected_scenario_outcomes_are_recorded_without_ranking(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report = run_qoe_smoke_scenarios(os.path.join(temp_dir, "smoke"))

            scenarios = {
                scenario["scenario_name"]: scenario
                for scenario in report["scenarios"]
            }

            complete = scenarios["complete_use_for_eval"]
            self.assertAlmostEqual(2.0, complete["qoe_linear_sum"])
            self.assertAlmostEqual(2.0 / 3.0, complete["qoe_linear_mean"])
            self.assertEqual("use_for_eval", complete["session_eval_gate"])

            legacy = scenarios["legacy_do_not_use_for_eval"]
            self.assertEqual("do_not_use_for_eval", legacy["session_eval_gate"])

            incomplete = scenarios["incomplete_session"]
            self.assertIn("incomplete_session", incomplete["gate_reasons"])

            source_claims_benchmark = scenarios["source_claims_benchmark"]
            self.assertFalse(source_claims_benchmark["outputs_are_benchmark_results"])
            self.assertTrue(source_claims_benchmark["no_final_ranking"])

    def test_each_scenario_has_qoe_artifacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report = run_qoe_smoke_scenarios(os.path.join(temp_dir, "smoke"))

            for scenario in report["scenarios"]:
                qoe_output_dir = scenario["qoe_output_dir"]
                self.assertTrue(os.path.isfile(os.path.join(qoe_output_dir, QOE_RUN_SUMMARY_FILENAME)))
                self.assertTrue(os.path.isfile(os.path.join(qoe_output_dir, QOE_SEGMENT_REWARDS_FILENAME)))
                self.assertTrue(os.path.isfile(os.path.join(qoe_output_dir, QOE_ARTIFACT_MANIFEST_FILENAME)))

    def test_cli_generates_report_in_tempfile_output_root(self):
        repo_root = os.path.dirname(os.path.dirname(__file__))
        script_path = os.path.join(repo_root, "scripts", "run_qoe_smoke_scenarios.py")
        with tempfile.TemporaryDirectory() as temp_dir:
            output_root = os.path.join(temp_dir, "smoke-cli")

            completed = subprocess.run(
                [
                    sys.executable,
                    script_path,
                    "--output-root",
                    output_root,
                    "--overwrite",
                ],
                cwd=repo_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            self.assertEqual("", completed.stderr)
            self.assertEqual(0, completed.returncode)
            self.assertIn("all_checks_passed=true", completed.stdout)
            self.assertTrue(os.path.isfile(os.path.join(output_root, SMOKE_REPORT_FILENAME)))
            report = self.read_json(os.path.join(output_root, SMOKE_REPORT_FILENAME))
            self.assertTrue(report["all_checks_passed"])

    def test_cli_rejects_output_root_inside_repository(self):
        repo_root = os.path.dirname(os.path.dirname(__file__))
        script_path = os.path.join(repo_root, "scripts", "run_qoe_smoke_scenarios.py")
        inside_repo_output = os.path.join(repo_root, "tmp_phase35d_inside_repo_reject")
        if os.path.isdir(inside_repo_output):
            shutil.rmtree(inside_repo_output)

        completed = subprocess.run(
            [
                sys.executable,
                script_path,
                "--output-root",
                inside_repo_output,
                "--overwrite",
            ],
            cwd=repo_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        self.assertNotEqual(0, completed.returncode)
        self.assertIn("outside the repository", completed.stderr)
        self.assertFalse(os.path.exists(inside_repo_output))

    def test_no_persistent_fixtures_datasets_logs_zips_pdfs_or_media_are_added(self):
        forbidden_extensions = {".csv", ".log", ".zip", ".pdf", ".mp4", ".m4s", ".mpd"}
        tests_dir = os.path.dirname(__file__)
        found = []
        for root, _dirs, files in os.walk(tests_dir):
            for filename in files:
                if os.path.splitext(filename)[1].lower() in forbidden_extensions:
                    found.append(os.path.join(root, filename))
        self.assertEqual([], found)

    def read_json(self, path):
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)


if __name__ == "__main__":
    unittest.main()
