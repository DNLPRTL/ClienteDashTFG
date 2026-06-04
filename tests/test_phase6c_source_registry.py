from __future__ import annotations

import unittest

from scripts.phase6c_source_registry import DEFAULT_REGISTRY_PATH, load_source_registry, selected_sources, sources_by_id


class Phase6CSourceRegistryTest(unittest.TestCase):
    def test_source_registry_loads(self):
        registry = load_source_registry(DEFAULT_REGISTRY_PATH)
        self.assertEqual("phase6c_public_source_registry_v1", registry["schema_version"])
        self.assertGreaterEqual(len(registry["sources"]), 6)

    def test_raca_4g_has_md5(self):
        source = sources_by_id(load_source_registry(DEFAULT_REGISTRY_PATH))["raca_4g_lte"]
        self.assertEqual("27da16b90a94ded3511bad9682f2e166", source["expected_hashes"]["md5"])

    def test_lancaster_is_excluded(self):
        source = sources_by_id(load_source_registry(DEFAULT_REGISTRY_PATH))["lancaster_abr_throughput_traces"]
        self.assertFalse(source["download_by_default"])
        self.assertEqual("do_not_use_for_eval", source["eval_gate"])
        with self.assertRaises(Exception):
            selected_sources(load_source_registry(DEFAULT_REGISTRY_PATH), "lancaster_abr_throughput_traces")

    def test_ghent_default_does_not_combine_logs_all_and_per_mobility(self):
        source = sources_by_id(load_source_registry(DEFAULT_REGISTRY_PATH))["ghent_4g_lte"]
        self.assertEqual(["https://users.ugent.be/~jvdrhoof/dataset-4g/logs/logs_all.zip"], source["urls"])
        self.assertTrue(source["ghent_policy"]["do_not_combine_with_per_mobility_archives"])


if __name__ == "__main__":
    unittest.main()
