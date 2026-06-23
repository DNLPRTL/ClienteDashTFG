from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from core.mpc_prudente.dataset import build_mpc_prudente_dataset
from core.mpc_prudente.media_profile import MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID
from core.neural_abr.artifacts import read_json
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.throughput_quantile_dataset import (
    THROUGHPUT_QUANTILE_SUMMARY_FILENAME,
    validate_phase45_v3_throughput_quantile_dataset_dir,
)
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


def _write_synthetic_media_profile(base_dir: Path, media_profile_id: str) -> None:
    base_dir.mkdir(parents=True, exist_ok=True)
    bitrates = (300000, 750000, 1200000, 1850000, 2850000, 4300000)
    representations = []
    for bandwidth in bitrates:
        nominal = bandwidth * 4.0 / 8.0
        # tamaños "VBR" sintéticos alrededor del nominal (variando por segmento)
        sizes = [int(nominal * factor) for factor in (0.9, 1.1, 0.8, 1.2, 1.0, 0.95, 1.05, 0.85)]
        representations.append({"bandwidth_bps": bandwidth, "segment_bytes": sizes})
    descriptor = {
        "schema_id": MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID,
        "media_profile_id": media_profile_id,
        "mpd_url": "http://example/test.mpd",
        "segment_duration_s": 4.0,
        "segment_count": 8,
        "vbr_cv_max": 0.15,
        "representations": representations,
    }
    with open(base_dir / (media_profile_id + ".json"), "w", encoding="utf-8") as handle:
        json.dump(descriptor, handle)


class MpcPrudenteDatasetTest(unittest.TestCase):
    def test_builds_media_faithful_dataset(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            media_dir = root / "media_profiles" / "segment_sizes"
            _write_synthetic_media_profile(media_dir, "synthetic_test")
            output_dir = root / "datasets_normalizados" / "mpc_prudente" / "unit"
            profile = Phase45V3DatasetProfile(
                name="unit",
                train_window_count=2,
                validation_window_count=1,
                qh_horizon_segments=3,
                qh_beam_width=4,
                max_windows_per_trace=1,
                synthetic_max_fraction=0.50,
                dataset_max_fraction=1.0,
                semantics_max_fraction=1.0,
                seed="unit-mpc-prudente",
                rollouts_per_window=2,
            )

            result = build_mpc_prudente_dataset(
                manifest,
                output_dir=output_dir,
                profile=profile,
                media_profile_id="synthetic_test",
                media_profile_base_dir=str(media_dir),
                overwrite=True,
                horizon_segments=3,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )

            validation = validate_phase45_v3_throughput_quantile_dataset_dir(output_dir)
            summary = read_json(output_dir / THROUGHPUT_QUANTILE_SUMMARY_FILENAME)

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            # La marca de fidelidad: tamaños reales, no CBR.
            self.assertEqual("real_vbr_from_server", summary["segment_size_source"])
            self.assertEqual("synthetic_test", summary["media_profile_id"])
            self.assertEqual([300, 750, 1200, 1850, 2850, 4300], summary["representation_kbps"])

    def test_builds_multimedia_dataset(self):
        from core.mpc_prudente.dataset import build_mpc_prudente_multimedia_dataset

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            media_dir = root / "media_profiles" / "segment_sizes"
            _write_synthetic_media_profile(media_dir, "synthetic_a")
            _write_synthetic_media_profile(media_dir, "synthetic_b")
            output_dir = root / "datasets" / "multimedia_unit"
            profile = Phase45V3DatasetProfile(
                name="unit", train_window_count=2, validation_window_count=1, qh_horizon_segments=3,
                qh_beam_width=4, max_windows_per_trace=1, synthetic_max_fraction=0.5,
                dataset_max_fraction=1.0, semantics_max_fraction=1.0, seed="unit-mm", rollouts_per_window=2,
            )
            result = build_mpc_prudente_multimedia_dataset(
                manifest, output_dir=output_dir, profile=profile,
                media_profile_ids=("synthetic_a", "synthetic_b"), media_profile_base_dir=str(media_dir),
                overwrite=True, horizon_segments=3,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            self.assertEqual("PASS", result["status"])
            self.assertEqual(["synthetic_a", "synthetic_b"], result["media_profile_ids"])


if __name__ == "__main__":
    unittest.main()
