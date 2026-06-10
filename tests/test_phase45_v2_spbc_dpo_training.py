from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

import torch

from core.neural_abr.artifacts import read_json, read_jsonl, write_jsonl
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.preference_dataset_v2 import V2_TRAINING_DATA_FILENAME, build_phase45_v2_dataset
from core.phase45_v1.spbc_v2_dpo_training import (
    SPBC_V2_DPO_MODEL_FILENAME,
    SPBC_V2_DPO_TRAINING_REPORT_FILENAME,
    SpbcAbrV2DpoPolicy,
    SpbcV2DpoTrainingError,
    examples_to_tensors,
    fit_spbc_v2_dpo_normalization,
    load_spbc_v2_dpo_examples,
    profile_by_name,
    train_spbc_abr_v2_dpo,
    _loss_components,
)
from tests.test_phase45_v2_preference_dataset import build_manifest_with_trace_files, unit_profile, write_stub_spbc_checkpoint


class Phase45V2SpbcDpoTrainingTest(unittest.TestCase):
    def test_loads_examples_with_complete_target_surface_and_capped_pair_weights(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=True)
            examples = load_spbc_v2_dpo_examples(
                dataset_dir / V2_TRAINING_DATA_FILENAME,
                "training",
                limit=16,
                max_pair_weight=1.25,
            )
            normalization = fit_spbc_v2_dpo_normalization(examples)
            tensors = examples_to_tensors(examples, normalization)

            self.assertTrue(examples)
            self.assertEqual(len(examples[0].reward_by_action), len(examples[0].bitrate_kbps_by_action))
            self.assertEqual(len(examples[0].reward_by_action), len(examples[0].smoothness_mbps_by_action))
            self.assertLessEqual(max(pair.weight for example in examples for pair in example.pairs), 1.25)
            self.assertEqual((len(examples), 7), tensors[1].shape)
            self.assertEqual((len(examples), 6, 7), tensors[2].shape)
            self.assertEqual((len(examples), 6), tensors[9].shape)
            self.assertEqual((len(examples), 6), tensors[10].shape)
            self.assertEqual((len(examples), 6), tensors[11].shape)
            self.assertEqual((len(examples), 6), tensors[18].shape)
            self.assertGreaterEqual(max(example.sample_weight for example in examples), 1.0)

    def test_model_forward_masks_invalid_actions_and_only_accepts_feature_tensors(self):
        model = SpbcAbrV2DpoPolicy(
            history_hidden_size=8,
            state_hidden_size=8,
            candidate_hidden_size=8,
            shared_hidden_size=16,
            dropout=0.0,
        )
        sequence = torch.zeros((2, 8, 2), dtype=torch.float32)
        scalars = torch.zeros((2, 7), dtype=torch.float32)
        candidates = torch.zeros((2, 6, 7), dtype=torch.float32)
        mask = torch.tensor([[True, True, False, False, False, False], [True, False, True, False, False, False]])

        logits = model(sequence, scalars, candidates, mask)["action_logits"]

        self.assertEqual((2, 6), logits.shape)
        self.assertLess(float(logits[0, 2]), -1.0e8)
        self.assertLess(float(logits[1, 1]), -1.0e8)
        self.assertEqual("spbc_abr_v2_dpo", model.config()["model_key"])
        self.assertFalse(model.config()["forward_input_contract"]["preference_pairs_used_as_inputs"])

    def test_loader_rejects_forbidden_extra_model_input_fields(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=False)
            rows = list(read_jsonl(dataset_dir / V2_TRAINING_DATA_FILENAME))
            first = dict(rows[0])
            model_inputs = dict(first["model_inputs"])
            context = dict(model_inputs["context"])
            context["rollout_source"] = "leak"
            model_inputs["context"] = context
            first["model_inputs"] = model_inputs
            rows[0] = first
            write_jsonl(dataset_dir / V2_TRAINING_DATA_FILENAME, rows)

            with self.assertRaises(SpbcV2DpoTrainingError):
                load_spbc_v2_dpo_examples(dataset_dir / V2_TRAINING_DATA_FILENAME, "training", limit=1)

    def test_full_v1_requires_reference_checkpoint_unless_explicitly_overridden(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=False)
            profile = replace(profile_by_name("full_v1"), epochs=1)

            with self.assertRaises(SpbcV2DpoTrainingError):
                train_spbc_abr_v2_dpo(
                    dataset_dir,
                    root / "modelos" / "spbc_v2_missing_ref",
                    profile=profile,
                    overwrite=True,
                    device="cpu",
                    init_checkpoint=root / "missing" / "modelo_spbc_abr_v1.pt",
                    validate_dataset=True,
                    progress_callback=None,
                )

    def test_smoke_training_writes_checkpoint_report_and_reference_comparison(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            checkpoint = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
            dataset_dir = build_unit_v2_dataset(root, with_spbc=True, checkpoint_path=checkpoint)
            output_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "smoke"
            profile = replace(profile_by_name("smoke"), epochs=1, batch_size=32, max_training_samples=96, max_validation_samples=48)

            report = train_spbc_abr_v2_dpo(
                dataset_dir,
                output_dir,
                profile=profile,
                overwrite=True,
                device="cpu",
                init_checkpoint=checkpoint,
                validate_dataset=True,
                progress_callback=None,
            )
            report_file = read_json(output_dir / SPBC_V2_DPO_TRAINING_REPORT_FILENAME)

            self.assertEqual("PASS", report["status"])
            self.assertTrue((output_dir / SPBC_V2_DPO_MODEL_FILENAME).is_file())
            self.assertFalse(report_file["benchmark_performed"])
            self.assertFalse(report_file["ranking_performed"])
            self.assertFalse(report_file["bundle_exported"])
            self.assertFalse(report_file["controller_registered"])
            self.assertTrue(report_file["spbc_v1_reference_comparison"]["available"])
            self.assertIn("focus_2_5_mbps", report_file["validation_metrics"])
            self.assertIn("by_rollout_source", report_file["validation_metrics"])
            self.assertIn("predicted_target_risk_rate", report_file["validation_metrics"])
            self.assertIn("utility_loss", report_file["validation_metrics"])
            self.assertIn("rebuffer_loss", report_file["validation_metrics"])
            self.assertIn("selected_utility_regret_vs_best_immediate_mean", report_file["validation_metrics"])
            self.assertIn("selected_rebuffer_regret_vs_best_immediate_mean", report_file["validation_metrics"])
            self.assertTrue(report_file["loss_design"]["sample_weights_include_focus_bucket_and_severe_errors"])

    def test_loss_components_include_utility_and_rebuffer_penalty(self):
        profile = replace(
            profile_by_name("smoke"),
            ce_loss_weight=0.0,
            dpo_loss_weight=0.0,
            ranking_loss_weight=0.0,
            utility_loss_weight=1.0,
            rebuffer_loss_weight=1.0,
        )
        logits_risky = torch.tensor([[0.0, 3.0]], dtype=torch.float32)
        logits_safe = torch.tensor([[3.0, 0.0]], dtype=torch.float32)
        outputs_risky = {"action_logits": logits_risky}
        outputs_safe = {"action_logits": logits_safe}
        ref_outputs = {"action_logits": torch.zeros((1, 2), dtype=torch.float32)}
        batch = (
            torch.zeros((1, 8, 2), dtype=torch.float32),
            torch.zeros((1, 7), dtype=torch.float32),
            torch.zeros((1, 2, 7), dtype=torch.float32),
            torch.tensor([[True, True]], dtype=torch.bool),
            torch.tensor([0], dtype=torch.long),
            torch.tensor([0], dtype=torch.long),
            torch.tensor([[0.0, 2.0]], dtype=torch.float32),
            torch.tensor([[0.0, 2.0]], dtype=torch.float32),
            torch.tensor([[2.0, -5.0]], dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.tensor([[0.0, 1.0]], dtype=torch.float32),
            torch.tensor([1.0], dtype=torch.float32),
            torch.tensor([[0]], dtype=torch.long),
            torch.tensor([[1]], dtype=torch.long),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[True]], dtype=torch.bool),
            torch.tensor([[0.0, 1.0]], dtype=torch.float32),
        )

        risky_losses = _loss_components(outputs_risky, ref_outputs, batch, profile)
        safe_losses = _loss_components(outputs_safe, ref_outputs, batch, profile)

        self.assertGreater(float(risky_losses["rebuffer_loss"]), float(safe_losses["rebuffer_loss"]))
        self.assertGreater(float(risky_losses["utility_loss"]), float(safe_losses["utility_loss"]))


def build_unit_v2_dataset(
    root: Path,
    *,
    with_spbc: bool,
    checkpoint_path: Path | None = None,
) -> Path:
    manifest = build_manifest_with_trace_files(root)
    output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2"
    checkpoint = checkpoint_path
    if with_spbc:
        checkpoint = checkpoint or root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
        write_stub_spbc_checkpoint(checkpoint)
    build_phase45_v2_dataset(
        manifest,
        output_dir=output_dir,
        profile=unit_profile("unit_v2_spbc_dpo"),
        overwrite=True,
        trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
        spbc_checkpoint=checkpoint if with_spbc else None,
        device="cpu",
    )
    return output_dir


if __name__ == "__main__":
    unittest.main()
