from __future__ import annotations

import csv
import io
import json
import logging
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import main
from core.output_artifacts import EVALUATION_SEGMENTS_FILENAME, SEGMENT_TELEMETRY_FILENAME
from tests.test_neural_abr_model_loading_runtime import write_runtime_bundle


class FakeSegmentDownloader:
    instances = []

    def __init__(self, max_retries=3, verbose=False):
        self.max_retries = max_retries
        self.verbose = verbose
        self.on_event = None
        self.downloaded_urls = []
        self.__class__.instances.append(self)

    def download(self, url, byte_range=None):
        text_url = str(url)
        if text_url.startswith(("http://", "https://")):
            raise AssertionError("External HTTP is not allowed in neural smoke tests")
        self.downloaded_urls.append(text_url)
        payload = "neural fake segment: {0}".format(text_url.rsplit("/", 1)[-1]).encode("ascii")
        return payload, {
            "url": text_url,
            "range": byte_range,
            "size": len(payload),
            "status": "ok",
            "elapsed_total": 0.001,
            "elapsed_payload": 0.001,
            "ttfb": 0.0,
            "attempt": 1,
            "saved": False,
            "save_path": None,
            "content_length_header": str(len(payload)),
            "content_range_header": None,
            "aborted": False,
            "bytes_downloaded": len(payload),
        }

    def get_file_size(self, url):
        raise AssertionError("SegmentList smoke test must not call get_file_size")


class NeuralAbrFakeSmokeTest(unittest.TestCase):
    def test_fake_engine_structural_smoke_with_temp_bundle(self):
        FakeSegmentDownloader.instances = []

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bundle_dir = write_runtime_bundle(tmp_path / "bundle")
            mpd_path = tmp_path / "tiny_neural.mpd"
            config_path = tmp_path / "client.neural.smoke.yaml"
            output_root = tmp_path / "runs"
            _write_mpd(mpd_path)
            _write_config(config_path, mpd_path, output_root, bundle_dir)

            try:
                with mock.patch.object(main, "SegmentDownloader", FakeSegmentDownloader):
                    with mock.patch(
                        "requests.sessions.Session.request",
                        side_effect=AssertionError("External HTTP is not allowed in neural smoke tests"),
                    ):
                        with mock.patch("sys.stdout", io.StringIO()):
                            with mock.patch("sys.stderr", io.StringIO()):
                                exit_code = main.main(["--config", str(config_path)])

                self.assertEqual(0, exit_code)
                run_dirs = sorted(path for path in output_root.iterdir() if path.is_dir() and path.name.startswith("run_"))
                self.assertEqual(1, len(run_dirs))
                run_dir = run_dirs[0]

                manifest_path = run_dir / "run_manifest.json"
                resolved_config_path = run_dir / "config.resolved.json"
                environment_path = run_dir / "environment.json"
                segment_telemetry_path = run_dir / SEGMENT_TELEMETRY_FILENAME
                evaluation_segments_path = run_dir / EVALUATION_SEGMENTS_FILENAME

                for expected in [
                    manifest_path,
                    resolved_config_path,
                    environment_path,
                    segment_telemetry_path,
                    evaluation_segments_path,
                ]:
                    self.assertTrue(expected.is_file(), expected)

                self.assertFalse((run_dir / "dataset.csv").exists())
                self.assertFalse((run_dir / "dataset_training.csv").exists())

                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual("completed", manifest["status"])
                self.assertEqual("neural_abr_lite", manifest["controller"]["name"])
                self.assertEqual("fake", manifest["media_engine"]["name"])

                with segment_telemetry_path.open(newline="", encoding="utf-8") as handle:
                    segment_rows = list(csv.reader(handle))
                with evaluation_segments_path.open(newline="", encoding="utf-8") as handle:
                    evaluation_rows = list(csv.reader(handle))

                segment_header = segment_rows[0]
                evaluation_header = evaluation_rows[0]
                self.assertIn("feedback_neural_raw_action", segment_header)
                self.assertIn("feedback_neural_safe_action", segment_header)
                self.assertIn("feedback_neural_fallback_used", segment_header)
                self.assertIn("feedback_neural_fallback_reason", segment_header)
                self.assertIn("feedback_neural_diagnostic_only", segment_header)
                self.assertFalse(any("neural_" in column for column in evaluation_header))

                forbidden_claim_columns = ("rank", "winner", "improvement", "p_value", "p-value")
                self.assertFalse(any(any(term in column.lower() for term in forbidden_claim_columns) for column in segment_header))
                self.assertFalse(any(any(term in column.lower() for term in forbidden_claim_columns) for column in evaluation_header))

                for row in segment_rows[1:]:
                    self.assertEqual(len(segment_header), len(row))
                    for column in [
                        "feedback_neural_raw_action",
                        "feedback_neural_safe_action",
                        "feedback_neural_fallback_used",
                        "feedback_neural_fallback_reason",
                        "feedback_neural_diagnostic_only",
                    ]:
                        value = row[segment_header.index(column)]
                        self.assertNotIn("\n", value)
                for row in evaluation_rows[1:]:
                    self.assertEqual(len(evaluation_header), len(row))

                self.assertEqual(1, len(FakeSegmentDownloader.instances))
                self.assertTrue(FakeSegmentDownloader.instances[0].downloaded_urls)
            finally:
                reset_logging()


def _write_mpd(path: Path) -> None:
    path.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011"
     type="static"
     minBufferTime="PT0.001S"
     mediaPresentationDuration="PT0.03S"
     profiles="urn:mpeg:dash:profile:isoff-on-demand:2011">
  <Period id="0" duration="PT0.03S">
    <AdaptationSet contentType="video" mimeType="video/mp4">
      <Representation id="v0" bandwidth="8000" width="16" height="16" codecs="avc1.42E01E">
        <SegmentList timescale="1000" duration="10">
          <Initialization sourceURL="init0.m4s" />
          <SegmentURL media="v0_seg1.m4s" />
          <SegmentURL media="v0_seg2.m4s" />
        </SegmentList>
      </Representation>
      <Representation id="v1" bandwidth="16000" width="16" height="16" codecs="avc1.42E01E">
        <SegmentList timescale="1000" duration="10">
          <Initialization sourceURL="init1.m4s" />
          <SegmentURL media="v1_seg1.m4s" />
          <SegmentURL media="v1_seg2.m4s" />
        </SegmentList>
      </Representation>
      <Representation id="v2" bandwidth="24000" width="16" height="16" codecs="avc1.42E01E">
        <SegmentList timescale="1000" duration="10">
          <Initialization sourceURL="init2.m4s" />
          <SegmentURL media="v2_seg1.m4s" />
          <SegmentURL media="v2_seg2.m4s" />
        </SegmentList>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
""",
        encoding="utf-8",
    )


def _write_config(config_path: Path, mpd_path: Path, output_root: Path, bundle_dir: Path) -> None:
    config_path.write_text(
        "\n".join(
            [
                'mpd_url: "{0}"'.format(mpd_path.as_posix()),
                "media_engine:",
                '  name: "fake"',
                "  min_queue_time: 0.001",
                "controller:",
                '  name: "neural_abr_lite"',
                "  params:",
                '    bundle_dir: "{0}"'.format(bundle_dir.as_posix()),
                "    enabled: true",
                '    fallback_controller: "robust_mpc"',
                "    diagnostic_telemetry: true",
                "    fail_closed: true",
                "    idle_duration: 0.0",
                "playback:",
                "  initial_quality: 0",
                "  initial_controller_decision: false",
                "  headless: true",
                "  max_buffer_seconds: 60.0",
                "  drain_buffer_sleep_seconds: 0.01",
                "  preroll_seconds: 0.0",
                "downloader:",
                "  max_retries: 1",
                "  verbose: false",
                "output:",
                '  root_dir: "{0}"'.format(output_root.as_posix()),
                '  segment_telemetry_filename: "{0}"'.format(SEGMENT_TELEMETRY_FILENAME),
                '  evaluation_segments_filename: "{0}"'.format(EVALUATION_SEGMENTS_FILENAME),
                "logging:",
                "  enabled: true",
                '  level: "WARNING"',
                "analysis:",
                "  enabled: false",
            ]
        ),
        encoding="utf-8",
    )


def reset_logging():
    logging.shutdown()
    root = logging.getLogger()
    for handler in list(root.handlers):
        root.removeHandler(handler)
        try:
            handler.close()
        except Exception:
            pass
    logging.disable(logging.NOTSET)


if __name__ == "__main__":
    unittest.main()
