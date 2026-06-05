from __future__ import annotations

import csv
import io
import logging
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import main
from core.output_artifacts import EVALUATION_SEGMENTS_FILENAME, SEGMENT_TELEMETRY_FILENAME
from tests.neural_abr_bundle_utils import build_minimal_phase4_bundle


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
        payload = "fake segment: {0}".format(text_url.rsplit("/", 1)[-1]).encode("ascii")
        return payload, {
            "url": text_url,
            "range": byte_range,
            "size": len(payload),
            "status": "ok",
            "elapsed_total": 0.001,
        }

    def get_file_size(self, url):
        raise AssertionError("SegmentList smoke test must not call get_file_size")


class NeuralAbrPlayerSmokeTest(unittest.TestCase):
    def test_fake_player_smoke_writes_neural_telemetry_only_to_segment_csv(self):
        cases = (
            ("neural_abr_lite_robust_mpc", "robust_mpc"),
            ("neural_abr_lite_teacher_hibrido", "teacher_hibrido"),
        )
        for controller_name, teacher in cases:
            with self.subTest(controller=controller_name):
                self._run_smoke(controller_name, teacher)

    def _run_smoke(self, controller_name: str, teacher: str) -> None:
        FakeSegmentDownloader.instances = []
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            bundle_dir = build_minimal_phase4_bundle(tmp_path, teacher=teacher)
            mpd_path = tmp_path / "tiny_neural.mpd"
            config_path = tmp_path / "client.neural.yaml"
            output_root = tmp_path / "runs"
            mpd_path.write_text(_tiny_mpd(), encoding="utf-8")
            config_path.write_text(
                "\n".join(
                    [
                        'mpd_url: "{0}"'.format(mpd_path.as_posix()),
                        "media_engine:",
                        '  name: "fake"',
                        "  min_queue_time: 0.09",
                        "controller:",
                        '  name: "{0}"'.format(controller_name),
                        "  params:",
                        '    bundle_dir: "{0}"'.format(bundle_dir.as_posix()),
                        '    fallback_controller: "robust_mpc"',
                        "    verify_hashes: true",
                        "    max_inference_latency_ms: 1000.0",
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
                segment_path = run_dir / SEGMENT_TELEMETRY_FILENAME
                eval_path = run_dir / EVALUATION_SEGMENTS_FILENAME
                self.assertTrue(segment_path.is_file())
                self.assertTrue(eval_path.is_file())
                self.assertFalse((run_dir / "dataset.csv").exists())
                self.assertFalse((run_dir / "dataset_training.csv").exists())

                with segment_path.open(newline="", encoding="utf-8") as handle:
                    segment_rows = list(csv.reader(handle))
                with eval_path.open(newline="", encoding="utf-8") as handle:
                    eval_rows = list(csv.reader(handle))

                segment_header = segment_rows[0]
                eval_header = eval_rows[0]
                self.assertIn("feedback_neural_model_label", segment_header)
                self.assertIn("feedback_neural_fallback_used", segment_header)
                self.assertIn("feedback_neural_fallback_reason", segment_header)
                self.assertNotIn("feedback_neural_model_label", eval_header)
                self.assertNotIn("feedback_neural_fallback_used", eval_header)

                reason_idx = segment_header.index("feedback_neural_fallback_reason")
                model_idx = segment_header.index("feedback_neural_model_label")
                reasons = {row[reason_idx] for row in segment_rows[1:]}
                models = {row[model_idx] for row in segment_rows[1:]}
                self.assertIn("success_neural", reasons)
                self.assertTrue(any(teacher in model for model in models))
            finally:
                _reset_logging()


def _tiny_mpd() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011"
     type="static"
     minBufferTime="PT0.001S"
     mediaPresentationDuration="PT0.10S"
     profiles="urn:mpeg:dash:profile:isoff-on-demand:2011">
  <Period id="0" duration="PT0.10S">
    <AdaptationSet contentType="video" mimeType="video/mp4">
      <Representation id="v0" bandwidth="300000" width="16" height="16" codecs="avc1.42E01E">
        <SegmentList timescale="1000" duration="50">
          <Initialization sourceURL="init_300.m4s" />
          <SegmentURL media="seg1_300.m4s" />
          <SegmentURL media="seg2_300.m4s" />
        </SegmentList>
      </Representation>
      <Representation id="v1" bandwidth="750000" width="16" height="16" codecs="avc1.42E01E">
        <SegmentList timescale="1000" duration="50">
          <Initialization sourceURL="init_750.m4s" />
          <SegmentURL media="seg1_750.m4s" />
          <SegmentURL media="seg2_750.m4s" />
        </SegmentList>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
"""


def _reset_logging():
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

