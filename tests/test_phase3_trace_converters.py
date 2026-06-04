from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from core.trace_replay.converters.fcc_mba import FccMbaConverter
from core.trace_replay.converters.gavist5g import Gavist5GConverter
from core.trace_replay.converters.interval_logs import Ghent4GLteConverter, NorwayHsdpaConverter
from core.trace_replay.converters.lumos5g import Lumos5GConverter
from core.trace_replay.converters.nyu_mets import NyuMetsConverter
from core.trace_replay.converters.oboe import OboeConverter
from core.trace_replay.converters.puffer import PufferConverter
from core.trace_replay.converters.roma import RomaActiveThroughputConverter
from core.trace_replay.converters.ucc import Ucc4GBeyondThroughputConverter, Ucc5GBeyondThroughputConverter


def read_normalized(path: str | Path) -> list[dict[str, float]]:
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        return [{key: float(value) for key, value in row.items()} for row in csv.DictReader(handle)]


class Phase3TraceConvertersTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "dataset en bruto"
        self.normalized = Path(self.tmp.name) / "datasets_normalizados"
        self.manifests = Path(self.tmp.name) / "manifests_trazas"

    def tearDown(self):
        self.tmp.cleanup()

    def convert_one(self, converter_cls):
        results = converter_cls(self.root).convert(self.normalized, self.manifests, max_traces=1)
        self.assertEqual(1, len(results), converter_cls.__name__)
        rows = read_normalized(results[0].normalized_trace_path)
        metadata_path = Path(results[0].metadata_path)
        self.assertTrue(metadata_path.is_file())
        return results[0], rows

    def test_norway_interval_log_uses_bytes_over_elapsed_ms(self):
        path = self.root / "Norway HSDPA (UMass trace archive)" / "bus" / "trace.log"
        path.parent.mkdir(parents=True)
        path.write_text("0 1000 0 0 1000000 1000\n0 2000 0 0 500000 1000\n", encoding="utf-8")

        result, rows = self.convert_one(NorwayHsdpaConverter)

        self.assertEqual("available_bandwidth", result.semantics)
        self.assertAlmostEqual(8000.0, rows[0]["throughput_kbps"])
        self.assertAlmostEqual(1.0, rows[0]["duration_s"])

    def test_ghent_interval_log_uses_same_formula(self):
        path = self.root / "BelgiumGhent 4G UGentIDLab LTE traces" / "trace_car_01.log"
        path.parent.mkdir(parents=True)
        path.write_text("0 1000 0 0 250000 500\n", encoding="utf-8")

        _, rows = self.convert_one(Ghent4GLteConverter)

        self.assertAlmostEqual(4000.0, rows[0]["throughput_kbps"])
        self.assertAlmostEqual(0.5, rows[0]["duration_s"])

    def test_ucc_4g_and_5g_use_dl_bitrate_as_kbps(self):
        path4 = self.root / "beyond_throughput_4g_lte" / "drive" / "trace.csv"
        path4.parent.mkdir(parents=True)
        path4.write_text("DL_bitrate\n1234\n", encoding="utf-8")
        _, rows4 = self.convert_one(Ucc4GBeyondThroughputConverter)
        self.assertAlmostEqual(1234.0, rows4[0]["throughput_kbps"])

        path5 = self.root / "bundle" / "UCC 5G Beyond Throughput, The Next Generation" / "5G-production-dataset" / "trace.csv"
        path5.parent.mkdir(parents=True)
        path5.write_text("DL_bitrate\n5678\n", encoding="utf-8")
        _, rows5 = self.convert_one(Ucc5GBeyondThroughputConverter)
        self.assertAlmostEqual(5678.0, rows5[0]["throughput_kbps"])

    def test_oboe_uses_ms_timestamps_and_second_column_kbps(self):
        path = self.root / "oboe" / "traces" / "trace.txt"
        path.parent.mkdir(parents=True)
        path.write_text("0 1000\n1000 2000\n", encoding="utf-8")

        _, rows = self.convert_one(OboeConverter)

        self.assertAlmostEqual(0.0, rows[0]["timestamp_s"])
        self.assertAlmostEqual(1.0, rows[0]["duration_s"])
        self.assertAlmostEqual(1000.0, rows[0]["throughput_kbps"])

    def test_nyu_mets_uses_mbps_to_kbps_one_second_samples(self):
        path = self.root / "bundle" / "NYU-METS" / "trace.csv"
        path.parent.mkdir(parents=True)
        path.write_text("1.5\n2.0\n", encoding="utf-8")

        _, rows = self.convert_one(NyuMetsConverter)

        self.assertAlmostEqual(1500.0, rows[0]["throughput_kbps"])
        self.assertAlmostEqual(1.0, rows[0]["duration_s"])

    def test_lumos5g_splits_by_run_num_and_uses_mbps_to_kbps(self):
        path = self.root / "bundle" / "Lumos5G-v1.0" / "Lumos5G-v1.0.csv"
        path.parent.mkdir(parents=True)
        path.write_text("run_num,Throughput\n1,3.5\n1,4.0\n2,9.0\n", encoding="utf-8")

        result, rows = self.convert_one(Lumos5GConverter)

        self.assertEqual("run_1", result.group_id)
        self.assertAlmostEqual(3500.0, rows[0]["throughput_kbps"])

    def test_fcc_groups_httpgetmt_by_unit_id(self):
        path = self.root / "FCC Measuring Broadband America" / "2020" / "curr_httpgetmt.csv"
        path.parent.mkdir(parents=True)
        path.write_text(
            "unit_id,dtime,bytes_sec,fetch_time\n"
            "u1,2020-01-01 00:00:00,1000000,1000000\n",
            encoding="utf-8",
        )

        result, rows = self.convert_one(FccMbaConverter)

        self.assertEqual("active_fixed_broadband_download_test", result.semantics)
        self.assertAlmostEqual(8000.0, rows[0]["throughput_kbps"])
        self.assertAlmostEqual(1.0, rows[0]["duration_s"])

    def test_roma_uses_current_network_dl_and_cuts_by_group(self):
        path = (
            self.root
            / "Large Scale Dataset of 4G NB-IoT and 5G Non-Standalone Network Measurements"
            / "Throughput Tests - Speedtest - Active Measurements.csv"
        )
        path.parent.mkdir(parents=True)
        path.write_text(
            "Date,Time,Campaign,Operator,Scenario,Current Netw. DL\n"
            "01.01.2020,00:00:00.000,A,Op,Urban,1111\n"
            "01.01.2020,00:00:01.000,A,Op,Urban,2222\n",
            encoding="utf-8",
        )

        result, rows = self.convert_one(RomaActiveThroughputConverter)

        self.assertEqual("active_mobile_speedtest", result.semantics)
        self.assertAlmostEqual(1111.0, rows[0]["throughput_kbps"])
        self.assertIn("A:Op:Urban", result.group_id)

    def test_gavist_aggregates_packet_lengths_per_second(self):
        path = self.root / "GAViST5G (Gaming and Video Streaming Traffic for 5G)" / "game" / "packets.csv"
        path.parent.mkdir(parents=True)
        path.write_text(
            "Time,Length\n"
            "2020-01-01 00:00:00,1000\n"
            "2020-01-01 00:00:00,500\n"
            "2020-01-01 00:00:01,1000\n",
            encoding="utf-8",
        )

        result, rows = self.convert_one(Gavist5GConverter)

        self.assertEqual("observed_application_traffic", result.semantics)
        self.assertAlmostEqual(12.0, rows[0]["throughput_kbps"])

    def test_puffer_joins_video_sent_and_acked_by_session_and_video_ts(self):
        root = self.root / "Puffer"
        root.mkdir(parents=True)
        (root / "video_acked_2020.csv").write_text("session_id,video_ts\ns1,v1\ns1,v2\n", encoding="utf-8")
        (root / "video_sent_2020.csv").write_text(
            "session_id,video_ts,delivery_rate,time (ns GMT)\n"
            "s1,v1,1000000,1000000000\n"
            "s1,v2,2000000,2000000000\n"
            "s2,v3,9000000,3000000000\n",
            encoding="utf-8",
        )

        results = PufferConverter(self.root, max_sessions=1, min_samples_per_session=1).convert(
            self.normalized,
            self.manifests,
            max_traces=1,
        )
        self.assertEqual(1, len(results))
        result = results[0]
        rows = read_normalized(result.normalized_trace_path)

        self.assertEqual("real_streaming_delivery_rate", result.semantics)
        self.assertGreaterEqual(len(rows), 1)
        self.assertAlmostEqual(8000.0, rows[0]["throughput_kbps"])

    def test_puffer_bounded_sampling_respects_session_limit_and_min_samples(self):
        root = self.root / "Puffer"
        root.mkdir(parents=True)
        ack_lines = ["session_id,video_ts"]
        sent_lines = ["session_id,video_ts,delivery_rate,time (ns GMT)"]
        for session_index in range(3):
            session_id = "s{0}".format(session_index)
            for sample_index in range(3):
                video_ts = "v{0}_{1}".format(session_index, sample_index)
                ack_lines.append("{0},{1}".format(session_id, video_ts))
                sent_lines.append("{0},{1},1000000,{2}".format(session_id, video_ts, 1_000_000_000 + sample_index * 1_000_000_000))
        (root / "video_acked_2020.csv").write_text("\n".join(ack_lines) + "\n", encoding="utf-8")
        (root / "video_sent_2020.csv").write_text("\n".join(sent_lines) + "\n", encoding="utf-8")

        results = PufferConverter(self.root, max_sessions=2, min_samples_per_session=3).convert(
            self.normalized,
            self.manifests,
        )

        self.assertEqual(2, len(results))
        for result in results:
            self.assertEqual(3, result.row_count)
            self.assertEqual("phase3_puffer_video_sent_acked_bounded_v1", result.converter_id)


if __name__ == "__main__":
    unittest.main()
