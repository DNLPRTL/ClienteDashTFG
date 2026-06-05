from __future__ import annotations

import tempfile
import unittest
from unittest import mock

from core.neural_abr.artifacts import write_json
from core.neural_abr.bundle import write_phase4_bundle_manifest
from core.neural_abr.constants import BUNDLE_MODEL_CARD_FILENAME, FEATURE_SCHEMA_FILENAME
from core.controller import neural_abr_loader
from core.controller.neural_abr_loader import NeuralAbrRuntimeBundleError, load_neural_abr_runtime_bundle
from tests.neural_abr_bundle_utils import build_minimal_phase4_bundle, minimal_feedback
from core.controller.neural_abr_runtime_features import NeuralAbrRuntimeFeatureBuilder


class NeuralAbrLoaderTest(unittest.TestCase):
    def test_loads_valid_bundle_and_scores_payload(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="robust_mpc")
            bundle = load_neural_abr_runtime_bundle(bundle_dir, expected_teacher="robust_mpc")
            payload = NeuralAbrRuntimeFeatureBuilder().build(minimal_feedback())
            result = bundle.score(payload.context_features, payload.candidate_features, payload.action_mask)

            self.assertIn(result["selected_representation_index"], (0, 1))
            self.assertGreaterEqual(result["latency_ms"], 0.0)

    def test_rejects_expected_teacher_mismatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="robust_mpc")

            with self.assertRaises(NeuralAbrRuntimeBundleError) as ctx:
                load_neural_abr_runtime_bundle(bundle_dir, expected_teacher="teacher_hibrido")

            self.assertEqual("expected_teacher_mismatch", ctx.exception.reason)

    def test_detects_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="robust_mpc")
            write_json(bundle_dir / BUNDLE_MODEL_CARD_FILENAME, {"tampered": True})

            with self.assertRaises(NeuralAbrRuntimeBundleError) as ctx:
                load_neural_abr_runtime_bundle(bundle_dir, expected_teacher="robust_mpc")

            self.assertEqual("bundle_hash_invalid", ctx.exception.reason)

    def test_detects_feature_schema_mismatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="robust_mpc")
            write_json(
                bundle_dir / FEATURE_SCHEMA_FILENAME,
                {
                    "schema_id": "wrong",
                    "context_vector_names": [],
                    "candidate_vector_names": [],
                },
            )
            write_phase4_bundle_manifest(
                bundle_dir,
                {
                    "teacher": "robust_mpc",
                    "model_family": "NeuralABR-Lite Candidate Scorer",
                    "training_method": "behavior_cloning",
                    "action_space": "representation_index",
                    "reward_version": "qoe_linear_v1",
                },
            )

            with self.assertRaises(NeuralAbrRuntimeBundleError) as ctx:
                load_neural_abr_runtime_bundle(bundle_dir, expected_teacher="robust_mpc")

            self.assertEqual("feature_schema_invalid", ctx.exception.reason)

    def test_torch_load_uses_weights_only_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="robust_mpc")
            original_load = neural_abr_loader.torch.load
            observed = {}

            def fake_load(*args, **kwargs):
                observed["weights_only"] = kwargs.get("weights_only")
                return original_load(*args, **kwargs)

            with mock.patch.object(neural_abr_loader.torch, "load", side_effect=fake_load):
                load_neural_abr_runtime_bundle(bundle_dir, expected_teacher="robust_mpc")

            self.assertIs(True, observed["weights_only"])


if __name__ == "__main__":
    unittest.main()
