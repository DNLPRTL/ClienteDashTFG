from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.extract_phase6_media_profile_from_mpd import extract_media_profile
from scripts.validate_phase6_media_profile import validate_media_profile
from tests.test_phase6_mpd_media_profile_extraction import PHASE6_MPD_FIXTURE


class Phase6MediaProfileValidationTest(unittest.TestCase):
    def test_validates_clean_extracted_profile(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile_path = _write_profile(Path(temp_dir))

            report = validate_media_profile(profile_path, strict=True)

            self.assertTrue(report["valid"])
            self.assertFalse(report["benchmark_authorized"])
            self.assertFalse(report["ready_for_benchmark"])
            self.assertIn("all_segment_sizes_are_estimated", report["warnings"])
            self.assertIn("media_duration_is_short", "\n".join(report["warnings"]))

    def test_rejects_non_increasing_ladder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile_path = _write_profile(Path(temp_dir))
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            profile["representations"][1]["bitrate_kbps"] = profile["representations"][0]["bitrate_kbps"]
            profile_path.write_text(json.dumps(profile), encoding="utf-8")

            report = validate_media_profile(profile_path)

            self.assertFalse(report["valid"])
            self.assertIn("bitrate_kbps must be strictly increasing in representation order", report["errors"])

    def test_rejects_benchmark_authorized_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile_path = _write_profile(Path(temp_dir))
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            profile["benchmark_authorized"] = True
            profile_path.write_text(json.dumps(profile), encoding="utf-8")

            report = validate_media_profile(profile_path)

            self.assertFalse(report["valid"])
            self.assertIn("benchmark_authorized must be false", report["errors"])

    def test_rejects_ready_for_benchmark_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile_path = _write_profile(Path(temp_dir))
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            profile["ready_for_benchmark"] = True
            profile_path.write_text(json.dumps(profile), encoding="utf-8")

            report = validate_media_profile(profile_path)

            self.assertFalse(report["valid"])
            self.assertIn("ready_for_benchmark must be false", report["errors"])


def _write_profile(root: Path) -> Path:
    mpd = root / "paseo.mpd"
    output = root / "profile.json"
    mpd.write_text(PHASE6_MPD_FIXTURE, encoding="utf-8")
    extract_media_profile(mpd=str(mpd), output=output)
    return output


if __name__ == "__main__":
    unittest.main()
