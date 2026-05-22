from __future__ import annotations

import csv
import json
import os
import tempfile
import unittest
import zipfile

from core.trace_replay.converters import (
    ConversionError,
    convert_dataset,
    convert_ghent_4g,
    convert_hsdpa_norway,
    convert_lancaster_abr,
)
from core.trace_replay.validation import validate_normalized_trace_csv


MOBILE_INTERVAL_LOG = """\
1453205523380 837 51.0506973750722 3.71183730126282 713740 837
1453205524381 1838 51.0507043157784 3.71192786488257 2504584 1001
1453205525380 2837 51.0507088101884 3.71203513605697 2724960 999
"""


class TraceConvertersTest(unittest.TestCase):
    def test_synthetic_hsdpa_like_raw_file_converts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            route_dir = os.path.join(raw_dir, "routes", "car.oslo-grimstad")
            os.makedirs(route_dir)
            self.write_text(os.path.join(route_dir, "report.2011-04-21_1135CEST.log"), MOBILE_INTERVAL_LOG)

            result = convert_hsdpa_norway(raw_dir, output_dir, manifest_dir)

            self.assertEqual(1, len(result.converted_traces))
            trace = result.converted_traces[0]
            self.assert_valid_converted_trace(trace)
            rows = self.read_csv(trace.output_csv_path)
            self.assertEqual("hsdpa_norway_mmsys2013", rows[0]["source_dataset"])
            self.assertEqual("HSDPA", rows[0]["network_type"])
            self.assertEqual("car", rows[0]["mobility_label"])

    def test_synthetic_ghent_like_raw_file_converts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "report_tram_0007.log"), MOBILE_INTERVAL_LOG)

            result = convert_ghent_4g(raw_dir, output_dir, manifest_dir)

            self.assertEqual(1, len(result.converted_traces))
            trace = result.converted_traces[0]
            self.assert_valid_converted_trace(trace)
            rows = self.read_csv(trace.output_csv_path)
            self.assertEqual("ghent_4g_lte_bandwidth_logs", rows[0]["source_dataset"])
            self.assertEqual("LTE", rows[0]["network_type"])
            self.assertEqual("tram", rows[0]["mobility_label"])

    def test_synthetic_lancaster_one_value_per_line_trace_converts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "431.txt"), "2603\n2780\n0\n")

            result = convert_lancaster_abr(raw_dir, output_dir, manifest_dir)

            self.assertEqual(1, len(result.converted_traces))
            trace = result.converted_traces[0]
            self.assert_valid_converted_trace(trace)
            rows = self.read_csv(trace.output_csv_path)
            self.assertEqual("0", rows[0]["timestamp_s"])
            self.assertEqual("1", rows[0]["duration_s"])
            self.assertEqual("2603", rows[0]["throughput_kbps"])

    def test_synthetic_lancaster_two_column_trace_converts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "1083.txt"), "0.0 2250\n9.5 2258\n19.5 2324\n")

            result = convert_lancaster_abr(raw_dir, output_dir, manifest_dir)

            self.assertEqual(1, len(result.converted_traces))
            trace = result.converted_traces[0]
            self.assert_valid_converted_trace(trace)
            rows = self.read_csv(trace.output_csv_path)
            self.assertEqual("0", rows[0]["timestamp_s"])
            self.assertEqual("9.5", rows[0]["duration_s"])
            self.assertEqual("2250", rows[0]["throughput_kbps"])
            self.assertEqual("10", rows[1]["duration_s"])

    def test_manifests_are_written_outside_output_dir_with_required_fields(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "431.txt"), "2603\n2780\n")

            result = convert_lancaster_abr(raw_dir, output_dir, manifest_dir)
            trace = result.converted_traces[0]
            manifest = self.read_json(trace.manifest_path)

            self.assertFalse(os.path.normcase(trace.manifest_path).startswith(os.path.normcase(output_dir)))
            for field in self.required_manifest_fields():
                self.assertIn(field, manifest)
            self.assertEqual("conversion_only_no_final_split", manifest["split_candidate"])
            self.assertEqual("kbps", manifest["throughput_unit"])

    def test_max_traces_limits_outputs_deterministically(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "b.txt"), "2000\n")
            self.write_text(os.path.join(raw_dir, "a.txt"), "1000\n")
            self.write_text(os.path.join(raw_dir, "c.txt"), "3000\n")

            first = convert_lancaster_abr(raw_dir, output_dir, manifest_dir, max_traces=2)
            first_ids = [trace.trace_id for trace in first.converted_traces]
            second_output = os.path.join(temp_dir, "normalized_second")
            second_manifest = os.path.join(temp_dir, "manifests_second")
            second = convert_lancaster_abr(raw_dir, second_output, second_manifest, max_traces=2)
            second_ids = [trace.trace_id for trace in second.converted_traces]

            self.assertEqual(2, len(first.converted_traces))
            self.assertEqual(first_ids, second_ids)
            self.assertIn("_a_", first_ids[0])
            self.assertIn("_b_", first_ids[1])

    def test_overwrite_false_protects_existing_outputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "431.txt"), "2603\n2780\n")
            convert_lancaster_abr(raw_dir, output_dir, manifest_dir)

            with self.assertRaisesRegex(ConversionError, "overwrite=False"):
                convert_lancaster_abr(raw_dir, output_dir, manifest_dir, overwrite=False)

    def test_overwrite_true_can_replace_existing_outputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            raw_path = os.path.join(raw_dir, "431.txt")
            self.write_text(raw_path, "2603\n2780\n")
            first = convert_lancaster_abr(raw_dir, output_dir, manifest_dir)
            self.write_text(first.converted_traces[0].output_csv_path, "corrupt\n")
            self.write_text(raw_path, "1000\n2000\n3000\n")

            second = convert_lancaster_abr(raw_dir, output_dir, manifest_dir, overwrite=True)

            trace = second.converted_traces[0]
            validation = validate_normalized_trace_csv(trace.output_csv_path)
            self.assertTrue(validation.is_valid)
            self.assertEqual(3, validation.sample_count)

    def test_dispatcher_rejects_unknown_dataset_id(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            with self.assertRaisesRegex(ConversionError, "unknown dataset_id"):
                convert_dataset("unknown", raw_dir, output_dir, manifest_dir)

    def test_dispatcher_accepts_required_dataset_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "431.txt"), "2603\n2780\n")

            result = convert_dataset("lancaster_abr_throughput_traces", raw_dir, output_dir, manifest_dir)

            self.assertEqual("lancaster_abr_throughput_traces", result.dataset_id)
            self.assertEqual(1, len(result.converted_traces))

    def test_zip_input_with_tiny_text_trace_is_handled(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            zip_path = os.path.join(raw_dir, "ABR-Throughput-Traces.zip")
            with zipfile.ZipFile(zip_path, "w") as archive:
                archive.writestr("nested/001.txt", "1000\n1500\n")

            result = convert_lancaster_abr(raw_dir, output_dir, manifest_dir)

            self.assertEqual(1, len(result.converted_traces))
            self.assertIn("::nested/001.txt", result.converted_traces[0].source_path)
            self.assert_valid_converted_trace(result.converted_traces[0])

    def test_no_real_dataset_paths_are_referenced(self):
        forbidden = os.path.normcase(
            os.path.join(
                "C:\\",
                "Users",
                "danie",
                "Documents",
                "TFG",
                "_datasets",
                "phase3_traces_replay",
                "_raw_candidates",
            )
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            raw_dir, output_dir, manifest_dir = self.make_dirs(temp_dir)
            self.write_text(os.path.join(raw_dir, "431.txt"), "2603\n2780\n")
            result = convert_lancaster_abr(raw_dir, output_dir, manifest_dir)

            for trace in result.converted_traces:
                self.assertNotIn(forbidden, os.path.normcase(trace.source_path))
                self.assertNotIn(forbidden, os.path.normcase(trace.output_csv_path))
                self.assertNotIn(forbidden, os.path.normcase(trace.manifest_path))

    def test_no_persistent_csv_fixtures_are_stored_in_tests_directory(self):
        tests_dir = os.path.dirname(__file__)
        csv_files = []
        for root, _dirs, files in os.walk(tests_dir):
            for filename in files:
                if filename.endswith(".csv"):
                    csv_files.append(os.path.join(root, filename))

        self.assertEqual([], csv_files)

    def make_dirs(self, temp_dir):
        raw_dir = os.path.join(temp_dir, "raw")
        output_dir = os.path.join(temp_dir, "normalized")
        manifest_dir = os.path.join(temp_dir, "manifests")
        os.makedirs(raw_dir)
        os.makedirs(output_dir)
        os.makedirs(manifest_dir)
        return raw_dir, output_dir, manifest_dir

    def write_text(self, path, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)

    def read_csv(self, path):
        with open(path, newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    def read_json(self, path):
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)

    def assert_valid_converted_trace(self, trace):
        self.assertTrue(os.path.exists(trace.output_csv_path))
        self.assertTrue(os.path.exists(trace.manifest_path))
        validation = validate_normalized_trace_csv(trace.output_csv_path)
        self.assertTrue(validation.is_valid, validation.errors)
        self.assertEqual(validation, trace.validation)

    def required_manifest_fields(self):
        return (
            "schema_version",
            "trace_id",
            "dataset_id",
            "source_path",
            "output_csv_path",
            "converter_name",
            "converter_version_or_commit",
            "checksum_sha256",
            "sample_count",
            "duration_s",
            "nominal_granularity_s",
            "throughput_unit",
            "min_throughput_kbps",
            "mean_throughput_kbps",
            "max_throughput_kbps",
            "scenario_tags",
            "mobility_tags",
            "network_tags",
            "split_candidate",
            "leakage_group",
            "notes",
        )


if __name__ == "__main__":
    unittest.main()
