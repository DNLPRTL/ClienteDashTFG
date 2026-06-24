import json
import os
import unittest

from core.mpc_prudente.media_profile import (
    MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID,
    SEGMENT_SIZES_DIR,
    MediaProfileError,
    MediaProfileSegmentSizes,
    available_media_profiles,
)
from core.neural_abr.action_mask import build_action_mask
from core.neural_abr.content_ladder import ContentLadderError
from core.phase45_v3.abr_closed_loop_env import (
    initial_closed_loop_state,
    simulate_closed_loop_step,
)


def _synthetic_descriptor() -> dict:
    return {
        "schema_id": MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID,
        "media_profile_id": "synthetic_test",
        "mpd_url": "http://example/test.mpd",
        "segment_duration_s": 4.0,
        "segment_count": 3,
        "vbr_cv_max": 0.2,
        "representations": [
            # desordenadas a propósito: el loader debe ordenarlas ascendente
            {"bandwidth_bps": 1200000, "segment_bytes": [600000, 700000, 500000]},
            {"bandwidth_bps": 300000, "segment_bytes": [150000, 120000, 170000]},
        ],
    }


class MediaProfileLoaderTests(unittest.TestCase):
    def test_loads_and_sorts_representations_ascending(self):
        profile = MediaProfileSegmentSizes.from_mapping(_synthetic_descriptor())
        self.assertEqual(profile.representation_count, 2)
        self.assertEqual(profile.segment_count, 3)
        self.assertEqual(profile.bitrates_bps, (300000, 1200000))
        # index 0 = bitrate más bajo
        self.assertEqual(profile.segment_size_bytes(0, 0), 150000)
        self.assertEqual(profile.segment_size_bytes(1, 1), 700000)

    def test_rejects_wrong_schema(self):
        data = _synthetic_descriptor()
        data["schema_id"] = "otro"
        with self.assertRaises(MediaProfileError):
            MediaProfileSegmentSizes.from_mapping(data)

    def test_rejects_inconsistent_segment_counts(self):
        data = _synthetic_descriptor()
        data["representations"][0]["segment_bytes"] = [1, 2]  # 2 vs 3
        with self.assertRaises(MediaProfileError):
            MediaProfileSegmentSizes.from_mapping(data)

    def test_faithful_ladder_returns_real_sizes(self):
        profile = MediaProfileSegmentSizes.from_mapping(_synthetic_descriptor())
        ladder = profile.to_faithful_ladder(max_buffer_s=60.0)
        self.assertEqual(ladder.representation_count, 2)
        self.assertEqual(ladder.segment_count, 3)
        self.assertEqual(ladder.max_buffer_s, 60.0)
        self.assertEqual(ladder.bitrate_bps(1), 1200000)
        # tamaño real, no CBR (CBR de 300k a 4s = 150000 por casualidad aquí, pero
        # el del segmento 2 es 170000 != 150000):
        self.assertEqual(ladder.segment_size_bytes(0, 2), 170000)
        self.assertNotEqual(
            ladder.segment_size_bytes(0, 2),
            ladder.cbr_nominal_bytes(0),
        )
        with self.assertRaises(ContentLadderError):
            ladder.segment_size_bytes(0, 3)  # fuera de rango

    def test_faithful_ladder_window_length_limits_segments(self):
        profile = MediaProfileSegmentSizes.from_mapping(_synthetic_descriptor())
        ladder = profile.to_faithful_ladder(segment_count=2)
        self.assertEqual(ladder.segment_count, 2)
        self.assertEqual(ladder.segment_size_bytes(0, 1), 120000)
        with self.assertRaises(ContentLadderError):
            ladder.segment_size_bytes(0, 2)

    def test_faithful_ladder_cycles_when_window_longer_than_media(self):
        profile = MediaProfileSegmentSizes.from_mapping(_synthetic_descriptor())  # 3 segmentos reales
        ladder = profile.to_faithful_ladder(segment_count=5)
        # seg 3 y 4 ciclan al inicio del medio real
        self.assertEqual(ladder.segment_size_bytes(0, 3), ladder.segment_size_bytes(0, 0))
        self.assertEqual(ladder.segment_size_bytes(0, 4), ladder.segment_size_bytes(0, 1))

    def test_faithful_ladder_start_offset(self):
        profile = MediaProfileSegmentSizes.from_mapping(_synthetic_descriptor())
        ladder = profile.to_faithful_ladder(start_offset=1)
        self.assertEqual(ladder.segment_size_bytes(0, 0), 120000)  # real[0][1]

    def test_faithful_ladder_drives_closed_loop_engine_with_real_sizes(self):
        # Demuestra que el motor congelado usa los tamaños reales sin tocarlo.
        profile = MediaProfileSegmentSizes.from_mapping(_synthetic_descriptor())
        ladder = profile.to_faithful_ladder()
        state = initial_closed_loop_state(ladder, initial_buffer_s=10.0)
        mask = build_action_mask(ladder, state.segment_index)
        self.assertEqual(len(mask), 2)
        _, step = simulate_closed_loop_step(
            state, ladder, action=1, download_time_s=1.0
        )
        # action 1 (1.2 Mbps), segmento 0 -> 600000 bytes reales
        self.assertEqual(step.segment_size_bytes, 600000)


class RealDescriptorTests(unittest.TestCase):
    PROFILE_ID = "paseo_almunecar_10min_30fps_4s"

    def setUp(self):
        self.path = os.path.join(SEGMENT_SIZES_DIR, self.PROFILE_ID + ".json")
        if not os.path.isfile(self.path):
            self.skipTest("descriptor real no presente (aún no extraído)")

    def test_real_paseo_profile_structure(self):
        profile = MediaProfileSegmentSizes.load(self.path)
        self.assertEqual(profile.representation_count, 6)
        self.assertEqual(profile.segment_count, 151)
        self.assertEqual(profile.segment_duration_s, 4.0)
        self.assertEqual(profile.bitrates_bps[0], 300000)
        self.assertEqual(profile.bitrates_bps[-1], 4300000)

    def test_ladder_matches_raw_json(self):
        with open(self.path, "r", encoding="utf-8") as handle:
            raw = json.load(handle)
        raw_sorted = sorted(raw["representations"], key=lambda r: r["bandwidth_bps"])
        profile = MediaProfileSegmentSizes.load(self.path)
        ladder = profile.to_faithful_ladder()
        for rep_index in (0, 5):
            for seg_index in (0, 1, 150):
                self.assertEqual(
                    ladder.segment_size_bytes(rep_index, seg_index),
                    raw_sorted[rep_index]["segment_bytes"][seg_index],
                )

    def test_available_media_profiles_includes_real(self):
        ids = available_media_profiles()
        self.assertIn(self.PROFILE_ID, ids)

    def test_phase6_media_id_resolves_to_descriptor(self):
        from core.mpc_prudente.media_profile import resolve_media_descriptor_id

        self.assertEqual(resolve_media_descriptor_id("paseo_10min_30fps_4s"), "paseo_almunecar_10min_30fps_4s")
        self.assertEqual(resolve_media_descriptor_id("blender_10min_60fps_4s"), "blender_sunflower_10min_60fps_4s")
        # un id que ya es de descriptor se devuelve igual
        self.assertEqual(resolve_media_descriptor_id(self.PROFILE_ID), self.PROFILE_ID)
        # cargar por el id corto de Phase 6 funciona
        profile = MediaProfileSegmentSizes.load_by_id("paseo_10min_30fps_4s")
        self.assertEqual(profile.representation_count, 6)


if __name__ == "__main__":
    unittest.main()
