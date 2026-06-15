from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from core.phase6.analysis import analyze_phase6_run, sign_test_exact
from core.phase6.config import DEFAULT_PHASE6_CONFIG
from core.phase6.selection import select_trace_windows
from core.phase6.verification import verify_phase6_package
from core.trace_replay.controlled_downloader import (
    TraceControlledDownloader,
    clip_loaded_trace_window,
    compact_loaded_trace_timeline,
)
from core.trace_replay.loader import load_normalized_trace_csv
from scripts.phase6_gui import build_phase6_command, parse_phase6_progress_line
from scripts.run_phase6_validacion_comparativa import build_client_config, build_phase6_protocol_and_plan, run_session


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
        self.assertTrue(all(window["window_duration_s"] == 300.0 for window in windows))
        self.assertEqual(len({window["trace_id"] for window in windows}), len(windows))

    def test_filters_impossible_real_windows_but_keeps_synthetic_diagnostic(self):
        manifest = {"traces": []}
        for index in range(8):
            manifest["traces"].append(_trace(index, split="eval", synthetic=False, mean_kbps=800.0))
        for index in range(4):
            manifest["traces"].append(_trace(20 + index, split="eval", synthetic=False, mean_kbps=50.0, max_kbps=90.0))
        for index in range(2):
            manifest["traces"].append(_trace(100 + index, split="eval", synthetic=True, mean_kbps=100.0, max_kbps=100.0))

        windows = select_trace_windows(manifest, "rapido", dict(DEFAULT_PHASE6_CONFIG))

        self.assertEqual(8, sum(1 for window in windows if not window["synthetic"]))
        self.assertEqual(2, sum(1 for window in windows if window["synthetic"]))
        self.assertTrue(all(float(window["throughput_mean_kbps"]) >= 450.0 for window in windows if not window["synthetic"]))


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

    def test_compacts_sparse_trace_before_clipping(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace_path = Path(tmp) / "trace.csv"
            trace_path.write_text(
                "\n".join(
                    [
                        "timestamp_s,duration_s,throughput_kbps",
                        "0,10,1000",
                        "7355,10,900",
                        "14483,10,800",
                    ]
                ),
                encoding="utf-8",
            )
            loaded = load_normalized_trace_csv(trace_path)
            compacted = compact_loaded_trace_timeline(loaded)
            clipped = clip_loaded_trace_window(compacted, window_start_s=15.0, window_duration_s=10.0)

        self.assertEqual(2, len(clipped.samples))
        self.assertAlmostEqual(0.0, clipped.samples[0].timestamp_s)
        self.assertAlmostEqual(5.0, clipped.samples[0].duration_s)
        self.assertAlmostEqual(5.0, clipped.samples[1].timestamp_s)
        self.assertAlmostEqual(5.0, clipped.samples[1].duration_s)

    def test_downloader_uses_compact_timeline_for_sparse_trace(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace_path = Path(tmp) / "trace.csv"
            trace_path.write_text(
                "\n".join(
                    [
                        "timestamp_s,duration_s,throughput_kbps",
                        "0,10,1000",
                        "7355,10,1000",
                    ]
                ),
                encoding="utf-8",
            )
            downloader = TraceControlledDownloader(
                FakeBaseDownloader(payload_size=1000),
                trace_csv_path=trace_path,
                window_start_s=15.0,
                window_duration_s=4.0,
                sleep=False,
            )
            data, info = downloader.download("http://example.invalid/seg.m4s")

        self.assertEqual(1000, len(data))
        self.assertTrue(info["trace_replay_compact_timestamps"])


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

    def test_analysis_writes_academic_metric_columns(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_metrics"
            session = _session(root, alias="base_robust_mpc", synthetic=False)
            _write_run(session, bitrate_Bps=100000.0, bitrates_Bps=[100000.0, 200000.0, 100000.0])
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "diagnostico",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                        "preset_runtime": {"max_media_segments": 6, "network_window_duration_s": 90.0},
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": [session]}), encoding="utf-8")

            package = analyze_phase6_run(root, generate_plots=False)
            summary_rows = _read_csv(root / "02_resultados" / "session_summary.csv")
            raw_rows = _read_csv(root / "02_resultados" / "raw_chunks.csv")

        self.assertGreater(_as_float(summary_rows[0]["positive_smoothness_mbps"]), 0.0)
        self.assertGreater(_as_float(summary_rows[0]["negative_smoothness_mbps"]), 0.0)
        self.assertGreater(_as_float(summary_rows[0]["avg_download_time_s"]), 0.0)
        self.assertGreater(_as_float(summary_rows[0]["avg_measured_throughput_kbps"]), 0.0)
        self.assertIn("chunk_size_bytes", raw_rows[0])
        self.assertIn("download_time_s", raw_rows[0])
        self.assertIn("buffer_after_s", raw_rows[0])
        self.assertEqual("diagnostico", package["protocol"]["preset"])

    def test_sign_test_exact_handles_clear_direction(self):
        self.assertLess(sign_test_exact([1.0] * 8), 0.01)

    def test_analysis_resolves_copied_package_run_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "copied_phase6_package"
            actual_session = _session(root, alias="base_robust_mpc", synthetic=False)
            planned_session = dict(actual_session)
            planned_session["run_output_root"] = "/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/pkg/01_ejecucion/runs/{0}".format(
                planned_session["session_id"]
            )
            _write_run(actual_session, bitrate_Bps=100000.0)
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "rapido",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": [planned_session]}), encoding="utf-8")

            package = analyze_phase6_run(root, generate_plots=False)

        self.assertEqual(1, package["session_counts"]["evaluable"])
        self.assertEqual(1, package["session_counts"]["completed"])

    def test_failed_partial_sessions_do_not_feed_aggregates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_failed_partial"
            session = _session(root, alias="base_robust_mpc", synthetic=False)
            _write_run(session, bitrate_Bps=100000.0)
            run_dir = next(Path(session["run_output_root"]).iterdir())
            (run_dir / "run_manifest.json").write_text(json.dumps({"status": "failed"}), encoding="utf-8")
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "rapido",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": [session]}), encoding="utf-8")

            package = analyze_phase6_run(root, generate_plots=False)

        self.assertEqual(0, package["session_counts"]["evaluable"])
        self.assertEqual([], package["aggregates"])

    def test_plot_manifest_is_generated_with_minimal_dataset(self):
        try:
            import matplotlib  # noqa: F401
        except Exception as exc:
            self.skipTest("matplotlib unavailable: {0}".format(exc))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_plots"
            sessions = []
            for alias, bitrate_Bps in (("base_robust_mpc", 100000.0), ("base_bba", 200000.0)):
                session = _session(root, alias=alias, synthetic=False)
                sessions.append(session)
                _write_run(session, bitrate_Bps=bitrate_Bps)
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "diagnostico",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                        "preset_runtime": {"max_media_segments": 6, "network_window_duration_s": 90.0},
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": sessions}), encoding="utf-8")

            analyze_phase6_run(root, generate_plots=True)
            manifest = json.loads((root / "03_graficas" / "plot_manifest.json").read_text(encoding="utf-8"))

        self.assertTrue(any(row["status"] == "generated" for row in manifest["plots"]))

    def test_package_verifier_passes_correct_package_and_fails_failed_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_verify_ok"
            session = _session(root, alias="base_robust_mpc", synthetic=False)
            synthetic_session = _session(root, alias="base_robust_mpc", synthetic=True)
            _write_run(session, bitrate_Bps=100000.0)
            _write_run(synthetic_session, bitrate_Bps=100000.0)
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "diagnostico",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": [session, synthetic_session]}), encoding="utf-8")
            analyze_phase6_run(root, generate_plots=False)

            ok = verify_phase6_package(root, require_plots=False)

            failed_root = Path(tmp) / "phase6_verify_failed"
            failed_session = _session(failed_root, alias="base_robust_mpc", synthetic=False)
            _write_run(failed_session, bitrate_Bps=100000.0, status="failed")
            failed_protocol = failed_root / "00_protocolo"
            failed_protocol.mkdir(parents=True)
            (failed_protocol / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "diagnostico",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                    }
                ),
                encoding="utf-8",
            )
            (failed_protocol / "session_plan.json").write_text(json.dumps({"sessions": [failed_session]}), encoding="utf-8")
            analyze_phase6_run(failed_root, generate_plots=False)

            bad = verify_phase6_package(failed_root, require_plots=False)

        self.assertTrue(ok["all_checks_passed"])
        self.assertFalse(bad["all_checks_passed"])

    def test_own_controller_neural_audit_is_preserved_and_gated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_neural_audit"
            session = _session(root, alias="propio_th", synthetic=False)
            _write_run(session, bitrate_Bps=100000.0, neural_success=True)
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "diagnostico",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": [session]}), encoding="utf-8")

            package = analyze_phase6_run(root, generate_plots=False)
            summary = _read_csv(root / "02_resultados" / "session_summary.csv")[0]
            chunks = _read_csv(root / "02_resultados" / "raw_chunks.csv")
            markdown = (root / "02_resultados" / "resultados_para_validar.md").read_text(encoding="utf-8")

        self.assertEqual("3", summary["neural_success_row_count"])
        self.assertEqual("3", summary["neural_inference_row_count"])
        self.assertEqual("0", summary["neural_audit_missing_row_count"])
        self.assertGreater(_as_float(summary["neural_inference_ms_mean"]), 0.0)
        self.assertEqual("success_neural", chunks[0]["neural_fallback_reason"])
        self.assertEqual(1.0, _as_float(chunks[0]["neural_bundle_loaded"]))
        self.assertTrue(package["gates"]["gate_items"]["propios_with_verified_neural_inference"])
        self.assertIn("Auditoria de inferencia propia", markdown)
        self.assertIn("auditadas 3/3", markdown)

    def test_own_controller_without_neural_audit_fails_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "phase6_neural_audit_missing"
            session = _session(root, alias="propio_th", synthetic=False)
            _write_run(session, bitrate_Bps=100000.0, neural_success=False)
            protocol_dir = root / "00_protocolo"
            protocol_dir.mkdir(parents=True)
            (protocol_dir / "protocolo_validacion.json").write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_validacion_comparativa_v1",
                        "preset": "diagnostico",
                        "benchmark_capable": False,
                        "ranking_capable": False,
                        "qoe_formula_version": "qoe_linear_v1",
                    }
                ),
                encoding="utf-8",
            )
            (protocol_dir / "session_plan.json").write_text(json.dumps({"sessions": [session]}), encoding="utf-8")

            package = analyze_phase6_run(root, generate_plots=False)

        self.assertFalse(package["gates"]["gate_items"]["propios_with_verified_neural_inference"])
        self.assertIn(session["session_id"], package["gates"]["violations"]["neural_audit_violations"])


class Phase6RunnerAndGuiTest(unittest.TestCase):
    def test_builds_protocol_and_client_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            manifest_path = tmp_path / "manifest.json"
            trace_path = tmp_path / "trace.csv"
            trace_path.write_text("timestamp_s,duration_s,throughput_kbps\n0,400,1000\n", encoding="utf-8")
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
        self.assertEqual(300.0, client_config["network_replay"]["window_duration_s"])
        self.assertTrue(client_config["network_replay"]["compact_timestamps"])
        self.assertEqual(30, client_config["playback"]["max_media_segments"])

    def test_diagnostico_preset_builds_short_full_pipeline_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            manifest_path = tmp_path / "manifest.json"
            trace_path = tmp_path / "trace.csv"
            trace_path.write_text("timestamp_s,duration_s,throughput_kbps\n0,120,1000\n", encoding="utf-8")
            traces = [_trace(index, split="eval", synthetic=False, path=trace_path.as_posix()) for index in range(2)]
            traces += [_trace(100, split="eval", synthetic=True, path=trace_path.as_posix())]
            manifest_path.write_text(json.dumps({"traces": traces}), encoding="utf-8")
            config = dict(DEFAULT_PHASE6_CONFIG)
            config["paths"] = dict(config["paths"])
            config["paths"]["manifest_path"] = manifest_path.as_posix()
            config["paths"]["output_root"] = (tmp_path / "out").as_posix()

            protocol, sessions = build_phase6_protocol_and_plan(config, "diagnostico", tmp_path / "package")
            client_config = build_client_config(config, sessions[0])

        self.assertEqual(27, len(sessions))
        self.assertFalse(protocol["benchmark_capable"])
        self.assertFalse(protocol["ranking_capable"])
        self.assertEqual(6, protocol["preset_runtime"]["max_media_segments"])
        self.assertEqual(90.0, protocol["preset_runtime"]["network_window_duration_s"])
        self.assertEqual(810.0, protocol["preset_runtime"]["estimated_total_duration_s"])
        self.assertEqual(6, client_config["playback"]["max_media_segments"])
        self.assertEqual(90.0, client_config["network_replay"]["window_duration_s"])

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

    def test_gui_progress_line_parser(self):
        parsed = parse_phase6_progress_line(
            "PHASE6_PROGRESS processed=7 total=70 percent=10.0 executed=7 failed=1 skipped=0 elapsed_s=120.5 last_session_s=20.0 avg_session_s=17.2 eta_s=1083.6 session=s00007\n"
        )

        self.assertEqual(7, parsed["processed"])
        self.assertEqual(70, parsed["total"])
        self.assertAlmostEqual(10.0, parsed["percent"])
        self.assertEqual(1, parsed["failed"])
        self.assertAlmostEqual(1083.6, parsed["eta_s"])

    def test_runner_tolerates_non_utf8_child_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            command_log_path = tmp_path / "session.log"
            session = {
                "session_id": "s00001_base_rate_based",
                "client_config_path": (tmp_path / "client.json").as_posix(),
                "run_output_root": (tmp_path / "runs" / "s00001").as_posix(),
                "command_log_path": command_log_path.as_posix(),
                "mpd_url": "http://example.invalid/video.mpd",
                "engine": "fake",
                "controller_key": "rate_based",
                "normalized_trace_path": (tmp_path / "trace.csv").as_posix(),
                "window_start_s": 0.0,
                "window_duration_s": 90.0,
            }
            config = dict(DEFAULT_PHASE6_CONFIG)
            config["execution"] = dict(config["execution"])
            config["execution"]["resume"] = False
            config["paths"] = dict(config["paths"])
            config["paths"]["python"] = "python"
            config["paths"]["repo_root"] = tmp_path.as_posix()

            completed = mock.Mock(returncode=0, stdout=b"linea valida\nbyte raro: \x98\n")
            with mock.patch("scripts.run_phase6_validacion_comparativa.subprocess.run", return_value=completed):
                result = run_session(config, session)

            log_text = command_log_path.read_text(encoding="utf-8")

        self.assertEqual({"executed": 1, "failed": 0, "skipped": 0}, result)
        self.assertIn("output_decoding=utf-8 errors=replace", log_text)
        self.assertIn("byte raro: �", log_text)


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


def _trace(index, *, split, synthetic, path=None, mean_kbps=None, max_kbps=None):
    return {
        "trace_id": "trace_{0}".format(index),
        "dataset_id": "synthetic_controlled_network" if synthetic else "dataset_{0}".format(index % 3),
        "duration_s": 400.0,
        "split": split,
        "usable_for_eval": True,
        "semantics": "synthetic_available_bandwidth" if synthetic else "available_bandwidth",
        "network_condition": "usable_network_trace",
        "normalized_trace_path": path or "/tmp/trace_{0}.csv".format(index),
        "leakage_group": "group_{0}".format(index),
        "throughput_mean_kbps": float(mean_kbps if mean_kbps is not None else 1000.0 + index),
        "throughput_min_kbps": 500.0,
        "throughput_max_kbps": float(max_kbps if max_kbps is not None else 2000.0),
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


def _write_run(session, *, bitrate_Bps, bitrates_Bps=None, status="completed", neural_success=False):
    run_root = Path(session["run_output_root"])
    run_dir = run_root / "run_20260101_000000"
    run_dir.mkdir(parents=True)
    (run_dir / "run_manifest.json").write_text(json.dumps({"status": status}), encoding="utf-8")
    (run_dir / "evaluation_segments.csv").write_text("segment_index,is_init,eval_phase,use_for_eval,last_fragment_size,last_download_time,fragment_duration\n", encoding="utf-8")
    with (run_dir / "segment_telemetry.csv").open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "segment_index",
            "is_init",
            "use_for_eval",
            "feedback_cur_bitrate",
            "feedback_cur_rate",
            "feedback_last_fragment_size",
            "feedback_last_download_time",
            "feedback_fragment_duration",
            "feedback_queued_time",
            "stall_duration",
            "policy_decision_ms",
            "feedback_neural_fallback_used",
            "feedback_neural_diagnostic_only",
            "feedback_neural_enabled",
            "feedback_neural_model_label",
            "feedback_neural_bundle_loaded",
            "feedback_neural_bundle_hash_ok",
            "feedback_neural_feature_vector_ok",
            "feedback_neural_inference_ms",
            "feedback_neural_fallback_reason",
            "feedback_neural_raw_action",
            "feedback_neural_safe_action",
            "feedback_neural_valid_action",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"segment_index": 0, "is_init": 1, "use_for_eval": 0})
        writer.writerow({"segment_index": 1, "is_init": 0, "use_for_eval": 0, "feedback_cur_bitrate": bitrate_Bps})
        values = list(bitrates_Bps or [bitrate_Bps, bitrate_Bps, bitrate_Bps])
        for segment_index, selected_bitrate in zip((2, 3, 4), values):
            writer.writerow(
                {
                    "segment_index": segment_index,
                    "is_init": 0,
                    "use_for_eval": 1,
                    "feedback_cur_bitrate": selected_bitrate,
                    "feedback_cur_rate": selected_bitrate,
                    "feedback_last_fragment_size": 500000,
                    "feedback_last_download_time": 4.0,
                    "feedback_fragment_duration": 4.0,
                    "feedback_queued_time": 8.0,
                    "stall_duration": 0.0,
                    "policy_decision_ms": 1.0,
                    "feedback_neural_fallback_used": 0,
                    "feedback_neural_diagnostic_only": 0,
                    "feedback_neural_enabled": 1 if neural_success else 0,
                    "feedback_neural_model_label": "NeuralABR-Lite teacher_hibrido" if neural_success else "",
                    "feedback_neural_bundle_loaded": 1 if neural_success else 0,
                    "feedback_neural_bundle_hash_ok": 1 if neural_success else 0,
                    "feedback_neural_feature_vector_ok": 1 if neural_success else 0,
                    "feedback_neural_inference_ms": 0.5 if neural_success else "",
                    "feedback_neural_fallback_reason": "success_neural" if neural_success else "",
                    "feedback_neural_raw_action": 1 if neural_success else "",
                    "feedback_neural_safe_action": 1 if neural_success else "",
                    "feedback_neural_valid_action": 1 if neural_success else 0,
                }
            )


def _read_csv(path: Path):
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


if __name__ == "__main__":
    unittest.main()
