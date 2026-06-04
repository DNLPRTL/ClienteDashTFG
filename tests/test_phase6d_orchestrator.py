from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_phase6_mpd_media_profile_extraction import PHASE6_MPD_FIXTURE


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_phase6d_media_profile_freeze.py"


class Phase6DOrchestratorTest(unittest.TestCase):
    def test_orchestrator_produces_external_profile_reports_and_summary(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            mpd = root / "paseo.mpd"
            external_root = root / "external"
            mpd.write_text(PHASE6_MPD_FIXTURE, encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    "-u",
                    str(SCRIPT),
                    "--external-root",
                    str(external_root),
                    "--mpd",
                    str(mpd),
                    "--size-policy",
                    "bitrate_estimate",
                    "--strict",
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(0, result.returncode, result.stderr)
            frozen_profile = external_root / "media_profiles" / "media_profile_phase6_v1.json"
            validation = external_root / "reports" / "phase6d_media_profile_validation.json"
            compatibility = external_root / "reports" / "phase6d_media_profile_compatibility.json"
            summary_path = external_root / "reports" / "phase6d_media_profile_freeze_summary.json"
            self.assertTrue(frozen_profile.is_file())
            self.assertTrue(validation.is_file())
            self.assertTrue(compatibility.is_file())
            self.assertTrue(summary_path.is_file())

            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            self.assertTrue(summary["valid"])
            self.assertFalse(summary["benchmark_authorized"])
            self.assertFalse(summary["ready_for_benchmark"])
            self.assertEqual("mpd_content_media_profile_source_not_benchmark_network", summary["server_role"])
            self.assertFalse((external_root / "results").exists())
            self.assertFalse((external_root / "plots").exists())
            self.assertFalse((external_root / "runs").exists())


if __name__ == "__main__":
    unittest.main()
