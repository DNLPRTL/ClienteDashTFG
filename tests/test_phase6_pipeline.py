from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from core.phase6.analysis import analyze_phase6_run, sign_test_exact
from core.phase6.config import DEFAULT_PHASE6_CONFIG
from core.phase6.selection import select_trace_windows
from core.trace_replay.controlled_downloader import TraceControlledDownloader, clip_loaded_trace_window
from core.trace_replay.loader import load_normalized_trace_csv
from scripts.phase6_gui import build_phase6_command
from scripts.run_phase6_validacion_comparativa import build_client_config, build_phase6_protocol_and_plan


class Phase6SelectionTest(unittest.TestCase):
    def test_selects_eval_windows_without_train_test_leakage(self):
        manifest = {"traces": []}
        for index in range(10):
            manifest["traces"].append(_trace(index, split="eval", synthetic=False))
        for index in range(2):
            manifest["traces"].append(_trace(100 + index, split="eval", synthetic=True))
        manifest["traces"].append(_trace(999, split="train", synthetic=False))

        config = dict(DEFAULT_PHASE6_CONFIG)
        windows = select_trace_windows(manifest, "rapido", config)

        self.assertEqual(10, len(windows))
        self.assertEqual(8, sum(1 for window in windows if not window["synthetic"]))
        self.assertEqual(2, sum(1 for window in windows if window["synthetic"]))
        self.assertTrue(all(window["source_split"] == "eval" for window in windows))
        self.assertTrue(all(window["window_duration_s"] == 120.0 for window in windows))
        self.assertEqual(len({window["trace_id"] for window in windows}), len(windows))


class TraceControlledDownloaderTest(unittest.TestCase):
    def test_wraps_download_time_with_trace_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace_path = Path(tmp) / "trace.csv"
            trace_path.write_text(
                "timestamp_s,duration_s,throughput_kbps\n0,10,800\n",
                encoding="utf-8",
            )
            downloader = TraceControlledDownloader(
                FakeBaseDownloader(payload_size=1000),
                trace_csv_path=trace_path,
                sleep=False,
            )

            data, info = downloader.download("http://example.invalid/seg.m4s")

        self.assertEqual(1000, len(data))
        self.assertTrue(info["trace_replay_enabled"])
        self.assertAlmostEqual(0.01, info["elapsed_total"], places=4)
        self.assertAlmostEqual(800.0, info["trace_replay_measured_throughput_kbps"], places=3)

    def test_clips_trace_window_and_rebases_time(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace_path = Path(tmp) / "trace.csv"
            trace_path.write_text(
                "\n".join(
                    [
                        "timestamp_s,duration_s,throughput_kbps",
                        "0,5,1000",
                        "5,5,2000",
                        "10,5,3000",
                    ]
                ),
                encoding="utf-8",
            )
            loaded = load_normalized_trace_csv(trace_path)
            clipped = clip_loaded_trace_window(loaded, window_start_s=4.0, window_duration_s=4.0)

        self.assertEqual(2, len(clipped.samples))
        self.assertAlmostEqual(0.0, clipped.samples[0].timestamp_s)
        self.assertAlmostEqual(1.0, clipped.samples[0].duration_s)
        self.assertAlmostEqual(1.0, clipped.samples[1].timestamp_s)
        self.assertAlmostEqual(3.0, clipped.samples[1].duration_s)


class Phase6AnalysisTest(unittest.TestCase):
    def test_analyzes_package_and_writes_validation_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_package"
            sessions = []
            for synthetic in (False, True):
                for alias, bitrate_Bps in (("base_robust_mpc", 100000.0), ("base_bba", 200000.0)):
                    session = _session(root, alias=alias, synthetic=synthetic)
                    sessions.append(session)
                    _write_run(session, bitrate_Bps=bitrate_Bps)
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "equilibrado",
                        "benchmark_capable": True,
                        "ranking_capable": True,
                        "qoe_formula_version": "qoe_linear_v1",
                        "controllers": [],
                        "media_profiles": [],
                        "trace_windows": [],
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": sessions}), encoding="utf-8")

            package = analyze_phase6_run(root, generate_plots=False)

            self.assertTrue((root / "02_resultados" / "resultados_para_validar.md").is_file())
            self.assertTrue((root / "02_resultados" / "session_summary.csv").is_file())
            self.assertTrue(package["gates"]["gate_items"]["synthetic_reported_separately"])
            self.assertEqual(4, package["session_counts"]["evaluable"])
            self.assertGreater(package["aggregates"][0]["qoe_linear_mean"], package["aggregates"][1]["qoe_linear_mean"])

    def test_sign_test_exact_handles_clear_direction(self):
        self.assertLess(sign_test_exact([1.0] * 8), 0.01)


class Phase6RunnerAndGuiTest(unittest.TestCase):
    def test_builds_protocol_and_client_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            manifest_path = tmp_path / "manifest.json"
            trace_path = tmp_path / "trace.csv"
            trace_path.write_text("timestamp_s,duration_s,throughput_kbps\n0,130,1000\n", encoding="utf-8")
            traces = [_trace(index, split="eval", synthetic=False, path=trace_path.as_posix()) for index in range(8)]
            traces += [_trace(100 + index, split="eval", synthetic=True, path=trace_path.as_posix()) for index in range(2)]
            manifest_path.write_text(json.dumps({"traces": traces}), encoding="utf-8")
            config = dict(DEFAULT_PHASE6_CONFIG)
            config["paths"] = dict(config["paths"])
            config["paths"]["manifest_path"] = manifest_path.as_posix()
            config["paths"]["output_root"] = (tmp_path / "out").as_posix()
            config["experiment"] = dict(config["experiment"])
            config["experiment"]["controllers"] = ["rate_based", "robust_mpc"]

            package_root = tmp_path / "package"
            protocol, sessions = build_phase6_protocol_and_plan(config, "rapido", package_root)
            client_config = build_client_config(config, sessions[0])

        self.assertFalse(protocol["benchmark_capable"])
        self.assertEqual(20, len(sessions))
        self.assertTrue(client_config["network_replay"]["enabled"])
        self.assertEqual(30, client_config["playback"]["max_media_segments"])

    def test_gui_command_builder_is_parameterized(self):
        command = build_phase6_command(
            config_path="config/phase6.local.yaml",
            preset="equilibrado",
            output_root="/tmp/phase6",
            dry_run=True,
            resume=False,
            max_sessions=3,
        )

        self.assertIn("--preset", command)
        self.assertIn("equilibrado", command)
        self.assertIn("--dry-run", command)
        self.assertIn("--no-resume", command)
        self.assertIn("3", command)


class FakeBaseDownloader:
    def __init__(self, payload_size: int):
        self.payload = b"x" * payload_size
        self.on_event = None

    def download(self, url, byte_range=None, timeout=10, callback=None, save_path=None, **kwargs):
        return self.payload, {
            "url": url,
            "range": byte_range,
            "size": len(self.payload),
            "status": 200,
            "elapsed_total": 0.0,
            "elapsed_payload": 0.0,
            "bytes_downloaded": len(self.payload),
        }

    def get_file_size(self, url, timeout=10):
        return len(self.payload)


def _trace(index, *, split, synthetic, path=None):
    return {
        "trace_id": "trace_{0}".format(index),
        "dataset_id": "synthetic_controlled_network" if synthetic else "dataset_{0}".format(index % 3),
        "duration_s": 180.0,
        "split": split,
        "usable_for_eval": True,
        "semantics": "synthetic_available_bandwidth" if synthetic else "available_bandwidth",
        "network_condition": "usable_network_trace",
        "normalized_trace_path": path or "/tmp/trace_{0}.csv".format(index),
        "leakage_group": "group_{0}".format(index),
        "throughput_mean_kbps": 1000.0 + index,
        "throughput_min_kbps": 500.0,
        "throughput_max_kbps": 2000.0,
        "synthetic": synthetic,
    }


def _session(root: Path, *, alias: str, synthetic: bool):
    session_id = "{0}_{1}".format(alias, "synthetic" if synthetic else "real")
    return {
        "session_id": session_id,
        "controller_alias": alias,
        "controller_display_name": alias,
        "media_profile_id": "paseo_10min_30fps_4s",
        "trace_window_id": "tw_synth" if synthetic else "tw_real",
        "dataset_id": "synthetic_controlled_network" if synthetic else "dataset",
        "semantics": "synthetic_available_bandwidth" if synthetic else "available_bandwidth",
        "network_condition": "usable_network_trace",
        "difficulty_bucket": "media_capacidad",
        "synthetic": synthetic,
        "source_split": "eval",
        "segment_duration_s": 4.0,
        "repetition": 1,
        "run_output_root": (root / "01_ejecucion" / "runs" / session_id).as_posix(),
    }


def _write_run(session, *, bitrate_Bps):
    run_root = Path(session["run_output_root"])
    run_dir = run_root / "run_20260101_000000"
    run_dir.mkdir(parents=True)
    (run_dir / "run_manifest.json").write_text(json.dumps({"status": "completed"}), encoding="utf-8")
    (run_dir / "evaluation_segments.csv").write_text("segment_index,is_init,eval_phase,use_for_eval,last_fragment_size,last_download_time,fragment_duration\n", encoding="utf-8")
    with (run_dir / "segment_telemetry.csv").open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "segment_index",
            "is_init",
            "use_for_eval",
            "feedback_cur_bitrate",
            "feedback_cur_rate",
            "feedback_fragment_duration",
            "feedback_queued_time",
            "stall_duration",
            "policy_decision_ms",
            "feedback_neural_fallback_used",
            "feedback_neural_diagnostic_only",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"segment_index": 0, "is_init": 1, "use_for_eval": 0})
        writer.writerow({"segment_index": 1, "is_init": 0, "use_for_eval": 0, "feedback_cur_bitrate": bitrate_Bps})
        for segment_index in (2, 3, 4):
            writer.writerow(
                {
                    "segment_index": segment_index,
                    "is_init": 0,
                    "use_for_eval": 1,
                    "feedback_cur_bitrate": bitrate_Bps,
                    "feedback_cur_rate": bitrate_Bps,
                    "feedback_fragment_duration": 4.0,
                    "feedback_queued_time": 8.0,
                    "stall_duration": 0.0,
                    "policy_decision_ms": 1.0,
                    "feedback_neural_fallback_used": 0,
                    "feedback_neural_diagnostic_only": 0,
                }
            )


if __name__ == "__main__":
    unittest.main()
