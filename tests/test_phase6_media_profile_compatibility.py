from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_phase6_media_profile_compatibility import check_media_profile_compatibility
from scripts.extract_phase6_media_profile_from_mpd import extract_media_profile
from tests.test_phase6_mpd_media_profile_extraction import PHASE6_MPD_FIXTURE


class Phase6MediaProfileCompatibilityTest(unittest.TestCase):
    def test_warns_when_no_neural_bundle_is_provided(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            profile_path = _write_profile(Path(temp_dir))

            report = check_media_profile_compatibility(media_profile=profile_path)

            self.assertTrue(report["valid"])
            self.assertIn("bundle_not_checked", report["warnings"])
            self.assertEqual("unknown", report["neural_abr_lite"]["compatible"])
            self.assertTrue(report["compatible_primary_profile_available"])

    def test_detects_compatible_candidate_count_from_ladder_schema(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            profile_path = _write_profile(root)
            bundle = _write_bundle(root, 6)

            report = check_media_profile_compatibility(media_profile=profile_path, neural_bundle_root=bundle, strict=True)

            self.assertTrue(report["valid"])
            self.assertTrue(report["neural_abr_lite"]["compatible"])
            self.assertTrue(report["full_ladder_compatible"])
            self.assertEqual("use_full_ladder", report["primary_recommendation"]["action"])

    def test_detects_incompatible_full_ladder_and_recommends_subset(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            profile_path = _write_profile(root)
            bundle = _write_bundle(root, 5)

            report = check_media_profile_compatibility(media_profile=profile_path, neural_bundle_root=bundle, strict=True)

            self.assertTrue(report["valid"])
            self.assertFalse(report["full_ladder_compatible"])
            self.assertFalse(report["neural_abr_lite"]["compatible"])
            self.assertEqual("freeze_subset_primary", report["primary_recommendation"]["action"])
            self.assertEqual([300, 750, 1200, 1850, 2850], report["primary_recommendation"]["selected_bitrate_kbps"])
            self.assertEqual([], report["hard_failures"])


def _write_profile(root: Path) -> Path:
    mpd = root / "paseo.mpd"
    output = root / "profile.json"
    mpd.write_text(PHASE6_MPD_FIXTURE, encoding="utf-8")
    extract_media_profile(mpd=str(mpd), output=output)
    return output


def _write_bundle(root: Path, candidate_count: int) -> Path:
    bundle = root / "bundle"
    bundle.mkdir()
    (bundle / "ladder_schema.json").write_text(
        json.dumps(
            {
                "schema_version": "synthetic_ladder_schema_v1",
                "num_actions": candidate_count,
            }
        ),
        encoding="utf-8",
    )
    return bundle


if __name__ == "__main__":
    unittest.main()
