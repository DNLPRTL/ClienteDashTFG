from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.run_qoe_smoke_scenarios import run_qoe_smoke_scenarios


class QoESmokeScenariosTest(unittest.TestCase):
    def test_smoke_scenarios_keep_no_benchmark_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = run_qoe_smoke_scenarios(Path(tmp) / "smoke", clean=False)
            report_path = Path(tmp) / "smoke" / "qoe_smoke_report.json"
            stored = json.loads(report_path.read_text(encoding="utf-8"))

        self.assertTrue(report["all_checks_passed"])
        self.assertTrue(stored["all_checks_passed"])
        self.assertEqual(4, report["scenario_count"])
        self.assertFalse(report["outputs_are_benchmark_results"])
        self.assertTrue(report["no_final_ranking"])
        self.assertFalse(report["ranking_performed"])
        self.assertFalse(report["benchmark_performed"])
        self.assertFalse(report["ia_training_performed"])

        scenarios = {item["scenario"]: item for item in report["scenarios"]}
        self.assertEqual("use_for_eval", scenarios["complete_use_for_eval"]["observed_gate"])
        self.assertAlmostEqual(2.0, scenarios["complete_use_for_eval"]["qoe_linear_sum"])
        self.assertEqual("do_not_use_for_eval", scenarios["legacy_do_not_use_for_eval"]["observed_gate"])
        self.assertIn("legacy_dry_run", scenarios["legacy_do_not_use_for_eval"]["observed_reasons"])
        self.assertIn("incomplete_session", scenarios["incomplete_session"]["observed_reasons"])
        self.assertIn("source_claims_benchmark_result", scenarios["source_claims_benchmark"]["observed_reasons"])


if __name__ == "__main__":
    unittest.main()
