from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.extract_phase6_media_profile_from_mpd import extract_media_profile


class Phase6MpdMediaProfileExtractionTest(unittest.TestCase):
    def test_extracts_provided_mpd_structure(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            mpd = _write_mpd(root)
            output = root / "media_profile.json"

            profile = extract_media_profile(mpd=str(mpd), output=output)

            self.assertTrue(output.is_file())
            self.assertEqual("phase6_media_profile_extracted_v1", profile["schema_version"])
            self.assertEqual(60.0, profile["mpd_duration_s"])
            self.assertEqual(4.0, profile["segment_duration_s"])
            self.assertEqual(15, profile["segment_count"])
            self.assertEqual(6, len(profile["representations"]))
            self.assertEqual([300, 750, 1200, 1850, 2850, 4300], _bitrates(profile))
            self.assertEqual(["6", "5", "4", "3", "2", "1"], _mpd_ids(profile))
            self.assertEqual(list(range(6)), [item["representation_index"] for item in profile["representations"]])

    def test_computes_bitrate_estimated_segment_sizes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            mpd = _write_mpd(root)
            output = root / "media_profile.json"

            profile = extract_media_profile(mpd=str(mpd), output=output, size_policy="bitrate_estimate")

            first_segment = profile["segments"][0]
            self.assertEqual(150000, first_segment["size_bytes_by_representation"]["0"])
            self.assertEqual(2150000, first_segment["size_bytes_by_representation"]["5"])
            self.assertEqual("bitrate_estimate", first_segment["size_source_by_representation"]["0"])

    def test_uses_file_size_when_synthetic_segments_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            mpd = _write_mpd(root)
            content_root = root / "content"
            _write_synthetic_segments(content_root)
            output = root / "media_profile.json"

            profile = extract_media_profile(
                mpd=str(mpd),
                output=output,
                content_root=content_root,
                prefer_real_segment_sizes=True,
            )

            first_segment = profile["segments"][0]
            self.assertEqual(3001, first_segment["size_bytes_by_representation"]["0"])
            self.assertEqual(43001, first_segment["size_bytes_by_representation"]["5"])
            self.assertEqual("file_size", first_segment["size_source_by_representation"]["0"])
            self.assertEqual({"file_size": 90}, profile["size_source_counts"])


def _write_mpd(root: Path) -> Path:
    path = root / "paseo.mpd"
    path.write_text(PHASE6_MPD_FIXTURE, encoding="utf-8")
    return path


def _write_synthetic_segments(content_root: Path) -> None:
    bandwidths = [4300000, 2850000, 1850000, 1200000, 750000, 300000]
    for bandwidth in bandwidths:
        directory = content_root / "chunk_{0}bps".format(bandwidth)
        directory.mkdir(parents=True, exist_ok=True)
        size_prefix = int(bandwidth / 100000)
        for number in range(1, 16):
            segment = directory / "Paseo_Almunecar_1min_30fps_4s{0}.m4s".format(number)
            segment.write_bytes(b"x" * (size_prefix * 1000 + number))


def _bitrates(profile):
    return [item["bitrate_kbps"] for item in profile["representations"]]


def _mpd_ids(profile):
    return [item["mpd_representation_id"] for item in profile["representations"]]


PHASE6_MPD_FIXTURE = """<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011"
     type="static"
     mediaPresentationDuration="PT0H1M0.000S"
     minBufferTime="PT1.5S">
  <Period id="1" start="PT0S">
    <AdaptationSet id="1" mimeType="video/mp4" contentType="video" frameRate="30" codecs="avc1.640028">
      <SegmentTemplate
        timescale="15360"
        duration="61440"
        startNumber="1"
        media="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s$Number$.m4s"
        initialization="chunk_$Bandwidth$bps/Paseo_Almunecar_1min_30fps_4s.mp4" />
      <Representation id="1" bandwidth="4300000" width="1920" height="1080" />
      <Representation id="2" bandwidth="2850000" width="1280" height="720" />
      <Representation id="3" bandwidth="1850000" width="854" height="480" />
      <Representation id="4" bandwidth="1200000" width="640" height="360" />
      <Representation id="5" bandwidth="750000" width="426" height="240" />
      <Representation id="6" bandwidth="300000" width="256" height="144" />
    </AdaptationSet>
  </Period>
</MPD>
"""


if __name__ == "__main__":
    unittest.main()
