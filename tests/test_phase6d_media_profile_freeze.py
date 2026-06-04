from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.check_phase6_media_profile_compatibility import check_media_profile_compatibility
from scripts.extract_phase6_media_profile_from_mpd import extract_media_profile
from scripts.freeze_phase6_media_profile import freeze_media_profile
from scripts.validate_phase6_media_profile import validate_media_profile
from tests.test_phase6_mpd_media_profile_extraction import PHASE6_MPD_FIXTURE


class Phase6DMediaProfileFreezeTest(unittest.TestCase):
    def test_freeze_preserves_benchmark_flags_false(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            profile, validation, compatibility = _write_reports(root)
            output = root / "frozen.json"

            report = freeze_media_profile(
                extracted_profile=profile,
                validation_report=validation,
                compatibility_report=compatibility,
                output=output,
                strict=True,
            )

            self.assertEqual("full_mpd_ladder", report["primary_profile_mode"])
            frozen = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(frozen["benchmark_authorized"])
            self.assertFalse(frozen["ready_for_benchmark"])
            self.assertFalse(frozen["freeze_metadata"]["benchmark_authorized"])
            self.assertFalse(frozen["freeze_metadata"]["ready_for_benchmark"])
            self.assertIn("frozen_profile_sha256", frozen)

    def test_freeze_uses_compatible_subset_when_neural_bundle_supports_five(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            profile, validation, compatibility = _write_reports(root, neural_count=5)
            output = root / "frozen_subset.json"

            freeze_media_profile(
                extracted_profile=profile,
                validation_report=validation,
                compatibility_report=compatibility,
                output=output,
                strict=True,
            )

            frozen = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("mpd_derived_compatible_subset", frozen["primary_profile_mode"])
            self.assertEqual([300, 750, 1200, 1850, 2850], [item["bitrate_kbps"] for item in frozen["representations"]])
            self.assertEqual(list(range(5)), [item["representation_index"] for item in frozen["representations"]])
            self.assertEqual("diagnostic_full_mpd_ladder", frozen["diagnostic_profiles"][0]["profile_role"])
            self.assertEqual(6, len(frozen["diagnostic_profiles"][0]["profile"]["representations"]))
            self.assertFalse(frozen["benchmark_authorized"])
            self.assertFalse(frozen["ready_for_benchmark"])


def _write_reports(root: Path, neural_count: int = 6):
    mpd = root / "paseo.mpd"
    profile = root / "profile.json"
    validation = root / "validation.json"
    compatibility = root / "compatibility.json"
    bundle = root / "bundle"
    bundle.mkdir()
    (bundle / "ladder_schema.json").write_text(json.dumps({"num_actions": neural_count}), encoding="utf-8")
    mpd.write_text(PHASE6_MPD_FIXTURE, encoding="utf-8")
    extract_media_profile(mpd=str(mpd), output=profile)
    validation.write_text(json.dumps(validate_media_profile(profile)), encoding="utf-8")
    compatibility.write_text(
        json.dumps(check_media_profile_compatibility(media_profile=profile, neural_bundle_root=bundle, strict=True)),
        encoding="utf-8",
    )
    return profile, validation, compatibility


if __name__ == "__main__":
    unittest.main()
