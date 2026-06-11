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
    _copy_baseline_loss,
    _loss_components,
    _ppo_clipped_policy_loss,
    _residual_logit_l2_loss,
    _safe_improvement_rank_loss,
    _safety_gate_result,
    _selection_score,
)
from tests.test_phase45_v2_preference_dataset import (
    build_manifest_with_trace_files,
    unit_profile,
    write_stub_spbc_checkpoint,
    write_stub_spbc_v2_dpo_checkpoint,
)


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
            self.assertEqual((len(examples), 6), tensors[19].shape)
            self.assertEqual(torch.bool, tensors[19].dtype)
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
        outputs = model(sequence, scalars, candidates, mask)

        self.assertEqual((2, 6), logits.shape)
        self.assertLess(float(logits[0, 2]), -1.0e8)
        self.assertLess(float(logits[1, 1]), -1.0e8)
        self.assertEqual((2, 6), outputs["base_action_logits"].shape)
        self.assertEqual((2, 6), outputs["predicted_reward_n_by_action"].shape)
        self.assertEqual((2, 6), outputs["predicted_rebuffer_s_by_action"].shape)
        self.assertEqual((2, 6), outputs["predicted_target_risk_logits_by_action"].shape)
        self.assertEqual("spbc_abr_v2_dpo", model.config()["model_key"])
        self.assertFalse(model.config()["forward_input_contract"]["preference_pairs_used_as_inputs"])
        self.assertTrue(model.config()["auxiliary_heads"]["targets_used_only_for_training"])

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
            self.assertTrue(report_file["init_checkpoint_reference_comparison"]["available"])
            self.assertEqual(
                "spbc_abr_v1_full_v1_frozen_checkpoint",
                report_file["init_checkpoint_reference_comparison"]["reference_label"],
            )
            self.assertTrue(report_file["spbc_v1_reference_comparison"]["available"])
            self.assertIn("focus_2_5_mbps", report_file["validation_metrics"])
            self.assertIn("by_rollout_source", report_file["validation_metrics"])
            self.assertIn("predicted_target_risk_rate", report_file["validation_metrics"])
            self.assertIn("utility_loss", report_file["validation_metrics"])
            self.assertIn("rebuffer_loss", report_file["validation_metrics"])
            self.assertIn("aux_reward_loss", report_file["validation_metrics"])
            self.assertIn("aux_rebuffer_loss", report_file["validation_metrics"])
            self.assertIn("aux_risk_loss", report_file["validation_metrics"])
            self.assertIn("reference_kl_loss", report_file["validation_metrics"])
            self.assertIn("over_aggressive_probability_loss", report_file["validation_metrics"])
            self.assertIn("over_aggressive_margin_loss", report_file["validation_metrics"])
            self.assertIn("over_aggressive_reference_excess_loss", report_file["validation_metrics"])
            self.assertIn("safe_utility_rank_loss", report_file["validation_metrics"])
            self.assertIn("safe_improvement_rank_loss", report_file["validation_metrics"])
            self.assertIn("copy_baseline_loss", report_file["validation_metrics"])
            self.assertIn("residual_logit_l2_loss", report_file["validation_metrics"])
            self.assertIn("ppo_clip_loss", report_file["validation_metrics"])
            self.assertIn("selected_utility_regret_vs_best_immediate_mean", report_file["validation_metrics"])
            self.assertIn("selected_rebuffer_regret_vs_best_immediate_mean", report_file["validation_metrics"])
            self.assertEqual("validation_selection_score", report_file["checkpoint_selection"]["criterion"])
            self.assertTrue(report_file["state_load_report"]["loaded"])
            self.assertTrue(report_file["state_load_report"]["auxiliary_heads_initialized_from_zero"])
            self.assertIn("decision_fusion", report_file["loss_design"])
            self.assertIn("over_aggressive_margin_loss", report_file["loss_design"])
            self.assertIn("safe_utility_rank_loss", report_file["loss_design"])
            self.assertIn("safe_improvement_rank_loss", report_file["loss_design"])
            self.assertIn("copy_baseline_loss", report_file["loss_design"])
            self.assertIn("residual_logit_l2_loss", report_file["loss_design"])
            self.assertIn("ppo_clip_loss", report_file["loss_design"])
            self.assertTrue(report_file["loss_design"]["sample_weights_include_focus_bucket_and_severe_errors"])

    def test_training_can_warm_start_from_v2_checkpoint_and_compare_initial_policy(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            spbc_checkpoint = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
            dataset_dir = build_unit_v2_dataset(root, with_spbc=True, checkpoint_path=spbc_checkpoint)
            v2_checkpoint = (
                root
                / "modelos"
                / "phase45_v1"
                / "spbc_abr_v2_dpo"
                / "full_v1_utility_risk_v1"
                / "modelo_spbc_abr_v2_dpo.pt"
            )
            write_stub_spbc_v2_dpo_checkpoint(v2_checkpoint)
            output_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "pilot_dagger2_warm"
            profile = replace(
                profile_by_name("smoke"),
                epochs=1,
                batch_size=32,
                max_training_samples=96,
                max_validation_samples=48,
                decision_rebuffer_fusion_weight=0.77,
            )

            report = train_spbc_abr_v2_dpo(
                dataset_dir,
                output_dir,
                profile=profile,
                overwrite=True,
                device="cpu",
                init_checkpoint=v2_checkpoint,
                validate_dataset=True,
                progress_callback=None,
            )
            report_file = read_json(output_dir / SPBC_V2_DPO_TRAINING_REPORT_FILENAME)

            self.assertEqual("PASS", report["status"])
            self.assertEqual("spbc_abr_v2_dpo_frozen_initial_checkpoint", report_file["reference_policy_source"])
            self.assertTrue(report_file["state_load_report"]["loaded"])
            self.assertFalse(report_file["state_load_report"]["auxiliary_heads_initialized_from_zero"])
            self.assertTrue(report_file["init_checkpoint_reference_comparison"]["available"])
            self.assertEqual(
                "spbc_abr_v2_dpo_frozen_initial_checkpoint",
                report_file["init_checkpoint_reference_comparison"]["reference_label"],
            )
            self.assertNotIn(
                "training_delta_candidate_minus_spbc_v1",
                report_file["init_checkpoint_reference_comparison"],
            )
            self.assertFalse(report_file["spbc_v1_reference_comparison"]["available"])
            self.assertEqual(
                0.77,
                report_file["model_config"]["decision_rebuffer_fusion_weight"],
            )

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
        outputs_risky = {
            "action_logits": logits_risky,
            "predicted_reward_n_by_action": torch.tensor([[2.0, -5.0]], dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.tensor([[0.0, 2.0]], dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.tensor([[-3.0, 3.0]], dtype=torch.float32),
        }
        outputs_safe = {
            "action_logits": logits_safe,
            "predicted_reward_n_by_action": torch.tensor([[2.0, -5.0]], dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.tensor([[0.0, 2.0]], dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.tensor([[-3.0, 3.0]], dtype=torch.float32),
        }
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
        self.assertLess(float(risky_losses["aux_reward_loss"]), 1.0e-6)
        self.assertLess(float(risky_losses["aux_rebuffer_loss"]), 1.0e-6)
        self.assertLess(float(risky_losses["aux_risk_loss"]), 0.05)

    def test_loss_components_penalize_over_aggressive_probability_and_margin(self):
        profile = replace(
            profile_by_name("smoke"),
            ce_loss_weight=0.0,
            dpo_loss_weight=0.0,
            ranking_loss_weight=0.0,
            utility_loss_weight=0.0,
            rebuffer_loss_weight=0.0,
            aux_reward_loss_weight=0.0,
            aux_rebuffer_loss_weight=0.0,
            aux_risk_loss_weight=0.0,
            reference_kl_loss_weight=1.0,
            over_aggressive_probability_loss_weight=1.0,
            over_aggressive_margin_loss_weight=1.0,
            over_aggressive_reference_excess_loss_weight=1.0,
            over_aggressive_margin=0.40,
        )
        outputs_risky = {
            "action_logits": torch.tensor([[0.0, 3.0]], dtype=torch.float32),
            "predicted_reward_n_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.zeros((1, 2), dtype=torch.float32),
        }
        outputs_safe = {
            "action_logits": torch.tensor([[3.0, 0.0]], dtype=torch.float32),
            "predicted_reward_n_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.zeros((1, 2), dtype=torch.float32),
        }
        ref_outputs = {"action_logits": torch.tensor([[3.0, 0.0]], dtype=torch.float32)}
        batch = (
            torch.zeros((1, 8, 2), dtype=torch.float32),
            torch.zeros((1, 7), dtype=torch.float32),
            torch.zeros((1, 2, 7), dtype=torch.float32),
            torch.tensor([[True, True]], dtype=torch.bool),
            torch.tensor([0], dtype=torch.long),
            torch.tensor([0], dtype=torch.long),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.tensor([1.0], dtype=torch.float32),
            torch.tensor([[0]], dtype=torch.long),
            torch.tensor([[1]], dtype=torch.long),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[True]], dtype=torch.bool),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.tensor([[False, True]], dtype=torch.bool),
        )

        risky_losses = _loss_components(outputs_risky, ref_outputs, batch, profile)
        safe_losses = _loss_components(outputs_safe, ref_outputs, batch, profile)

        self.assertGreater(
            float(risky_losses["over_aggressive_probability_loss"]),
            float(safe_losses["over_aggressive_probability_loss"]),
        )
        self.assertGreater(
            float(risky_losses["over_aggressive_margin_loss"]),
            float(safe_losses["over_aggressive_margin_loss"]),
        )
        self.assertGreater(
            float(risky_losses["over_aggressive_reference_excess_loss"]),
            float(safe_losses["over_aggressive_reference_excess_loss"]),
        )
        self.assertGreater(float(risky_losses["reference_kl_loss"]), float(safe_losses["reference_kl_loss"]))
        self.assertGreater(float(risky_losses["loss"]), float(safe_losses["loss"]))

    def test_safe_utility_rank_loss_targets_best_non_over_aggressive_action(self):
        profile = replace(
            profile_by_name("smoke"),
            ce_loss_weight=0.0,
            dpo_loss_weight=0.0,
            ranking_loss_weight=0.0,
            utility_loss_weight=0.0,
            rebuffer_loss_weight=0.0,
            aux_reward_loss_weight=0.0,
            aux_rebuffer_loss_weight=0.0,
            aux_risk_loss_weight=0.0,
            reference_kl_loss_weight=0.0,
            over_aggressive_probability_loss_weight=0.0,
            over_aggressive_margin_loss_weight=0.0,
            over_aggressive_reference_excess_loss_weight=0.0,
            safe_utility_rank_loss_weight=1.0,
            safe_utility_margin=0.50,
        )
        outputs_wrong_safe = {
            "action_logits": torch.tensor([[3.0, 0.0, 9.0]], dtype=torch.float32),
            "predicted_reward_n_by_action": torch.zeros((1, 3), dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.zeros((1, 3), dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.zeros((1, 3), dtype=torch.float32),
        }
        outputs_best_safe = {
            "action_logits": torch.tensor([[0.0, 3.0, 9.0]], dtype=torch.float32),
            "predicted_reward_n_by_action": torch.zeros((1, 3), dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.zeros((1, 3), dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.zeros((1, 3), dtype=torch.float32),
        }
        ref_outputs = {"action_logits": torch.zeros((1, 3), dtype=torch.float32)}
        batch = (
            torch.zeros((1, 8, 2), dtype=torch.float32),
            torch.zeros((1, 7), dtype=torch.float32),
            torch.zeros((1, 3, 7), dtype=torch.float32),
            torch.tensor([[True, True, True]], dtype=torch.bool),
            torch.tensor([2], dtype=torch.long),
            torch.tensor([2], dtype=torch.long),
            torch.zeros((1, 3), dtype=torch.float32),
            torch.zeros((1, 3), dtype=torch.float32),
            torch.tensor([[0.0, 2.0, 9.0]], dtype=torch.float32),
            torch.zeros((1, 3), dtype=torch.float32),
            torch.zeros((1, 3), dtype=torch.float32),
            torch.zeros((1, 3), dtype=torch.float32),
            torch.tensor([1.0], dtype=torch.float32),
            torch.tensor([[1]], dtype=torch.long),
            torch.tensor([[0]], dtype=torch.long),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[True]], dtype=torch.bool),
            torch.zeros((1, 3), dtype=torch.float32),
            torch.tensor([[False, False, True]], dtype=torch.bool),
        )

        wrong_losses = _loss_components(outputs_wrong_safe, ref_outputs, batch, profile)
        best_losses = _loss_components(outputs_best_safe, ref_outputs, batch, profile)

        self.assertGreater(float(wrong_losses["safe_utility_rank_loss"]), 0.0)
        self.assertLess(float(best_losses["safe_utility_rank_loss"]), 1.0e-6)
        self.assertGreater(float(wrong_losses["loss"]), float(best_losses["loss"]))

    def test_safe_improvement_rank_loss_only_promotes_clear_safe_gain_against_reference(self):
        ref_logits = torch.tensor([[4.0, 1.0, 0.0]], dtype=torch.float32)
        mask = torch.tensor([[True, True, True]], dtype=torch.bool)
        over_aggressive = torch.tensor([[False, False, True]], dtype=torch.bool)
        sample_weights = torch.tensor([1.0], dtype=torch.float32)
        rewards_with_gain = torch.tensor([[0.0, 0.30, -1.0]], dtype=torch.float32)
        rewards_without_gain = torch.tensor([[0.0, 0.02, -1.0]], dtype=torch.float32)

        bad_loss = _safe_improvement_rank_loss(
            torch.tensor([[3.0, 0.0, 0.0]], dtype=torch.float32),
            ref_logits,
            rewards_with_gain,
            over_aggressive,
            mask,
            sample_weights,
            reward_margin=0.05,
            margin=0.50,
        )
        good_loss = _safe_improvement_rank_loss(
            torch.tensor([[0.0, 3.0, 0.0]], dtype=torch.float32),
            ref_logits,
            rewards_with_gain,
            over_aggressive,
            mask,
            sample_weights,
            reward_margin=0.05,
            margin=0.50,
        )
        no_gain_loss = _safe_improvement_rank_loss(
            torch.tensor([[3.0, 0.0, 0.0]], dtype=torch.float32),
            ref_logits,
            rewards_without_gain,
            over_aggressive,
            mask,
            sample_weights,
            reward_margin=0.05,
            margin=0.50,
        )

        self.assertGreater(float(bad_loss), 0.0)
        self.assertLess(float(good_loss), 1.0e-6)
        self.assertLess(float(no_gain_loss), 1.0e-6)

    def test_copy_baseline_loss_only_applies_without_clear_safe_improvement(self):
        ref_logits = torch.tensor([[3.0, 0.0, -1.0]], dtype=torch.float32)
        drift_logits = torch.tensor([[0.0, 3.0, -1.0]], dtype=torch.float32)
        mask = torch.tensor([[True, True, True]], dtype=torch.bool)
        over_aggressive = torch.tensor([[False, False, True]], dtype=torch.bool)
        sample_weights = torch.tensor([1.0], dtype=torch.float32)
        rewards_without_gain = torch.tensor([[0.0, 0.01, -1.0]], dtype=torch.float32)
        rewards_with_gain = torch.tensor([[0.0, 0.50, -1.0]], dtype=torch.float32)

        drift_loss = _copy_baseline_loss(
            drift_logits,
            ref_logits,
            rewards_without_gain,
            over_aggressive,
            mask,
            sample_weights,
            reward_margin=0.05,
        )
        copied_loss = _copy_baseline_loss(
            ref_logits,
            ref_logits,
            rewards_without_gain,
            over_aggressive,
            mask,
            sample_weights,
            reward_margin=0.05,
        )
        clear_gain_loss = _copy_baseline_loss(
            drift_logits,
            ref_logits,
            rewards_with_gain,
            over_aggressive,
            mask,
            sample_weights,
            reward_margin=0.05,
        )

        self.assertGreater(float(drift_loss), float(copied_loss))
        self.assertLess(float(copied_loss), 1.0e-6)
        self.assertLess(float(clear_gain_loss), 1.0e-6)

    def test_residual_logit_l2_loss_tracks_valid_logit_drift(self):
        ref_logits = torch.tensor([[1.0, 2.0, 9.0]], dtype=torch.float32)
        same_logits = torch.tensor([[1.0, 2.0, -4.0]], dtype=torch.float32)
        drift_logits = torch.tensor([[3.0, 2.0, -4.0]], dtype=torch.float32)
        mask = torch.tensor([[True, True, False]], dtype=torch.bool)
        sample_weights = torch.tensor([1.0], dtype=torch.float32)

        same_loss = _residual_logit_l2_loss(same_logits, ref_logits, mask, sample_weights)
        drift_loss = _residual_logit_l2_loss(drift_logits, ref_logits, mask, sample_weights)

        self.assertLess(float(same_loss), 1.0e-6)
        self.assertGreater(float(drift_loss), 0.0)

    def test_ppo_clip_loss_rewards_safe_positive_advantage_and_penalizes_over_aggressive(self):
        ref_logits = torch.tensor([[2.0, 0.0, -1.0]], dtype=torch.float32)
        mask = torch.tensor([[True, True, True]], dtype=torch.bool)
        rewards = torch.tensor([[0.0, 1.0, 2.0]], dtype=torch.float32)
        rebuffer = torch.tensor([[0.0, 0.0, 2.0]], dtype=torch.float32)
        risks = torch.tensor([[0.0, 0.0, 1.0]], dtype=torch.float32)
        over_aggressive = torch.tensor([[False, False, True]], dtype=torch.bool)
        weights = torch.tensor([1.0], dtype=torch.float32)

        better_safe_loss = _ppo_clipped_policy_loss(
            torch.tensor([[0.0, 2.0, -1.0]], dtype=torch.float32),
            ref_logits,
            rewards,
            rebuffer,
            risks,
            over_aggressive,
            mask,
            weights,
            clip_epsilon=0.20,
            advantage_clip=2.0,
            over_aggressive_penalty=3.0,
            rebuffer_penalty=0.0,
            risk_penalty=0.0,
        )
        worse_safe_loss = _ppo_clipped_policy_loss(
            torch.tensor([[2.0, 0.0, -1.0]], dtype=torch.float32),
            ref_logits,
            rewards,
            rebuffer,
            risks,
            over_aggressive,
            mask,
            weights,
            clip_epsilon=0.20,
            advantage_clip=2.0,
            over_aggressive_penalty=3.0,
            rebuffer_penalty=0.0,
            risk_penalty=0.0,
        )
        over_aggressive_loss = _ppo_clipped_policy_loss(
            torch.tensor([[0.0, -1.0, 3.0]], dtype=torch.float32),
            ref_logits,
            rewards,
            rebuffer,
            risks,
            over_aggressive,
            mask,
            weights,
            clip_epsilon=0.20,
            advantage_clip=2.0,
            over_aggressive_penalty=3.0,
            rebuffer_penalty=0.0,
            risk_penalty=0.0,
        )

        self.assertLess(float(better_safe_loss), float(worse_safe_loss))
        self.assertGreater(float(over_aggressive_loss), float(worse_safe_loss))

    def test_selection_score_prioritizes_regret_rebuffer_and_focus_bucket(self):
        profile = profile_by_name("smoke")
        low_loss_bad_policy = {
            "selected_utility_regret_vs_best_immediate_mean": 0.20,
            "selected_rebuffer_regret_vs_best_immediate_mean": 0.05,
            "over_aggressive_rate_vs_oracle": 0.20,
            "invalid_action_rate": 0.0,
            "focus_2_5_mbps": {
                "bucket_present": True,
                "selected_utility_regret_vs_best_immediate_mean": 0.40,
                "selected_rebuffer_regret_vs_best_immediate_mean": 0.10,
                "over_aggressive_rate_vs_oracle": 0.30,
                "invalid_action_rate": 0.0,
            },
        }
        higher_loss_better_policy = {
            "selected_utility_regret_vs_best_immediate_mean": 0.05,
            "selected_rebuffer_regret_vs_best_immediate_mean": 0.01,
            "over_aggressive_rate_vs_oracle": 0.08,
            "invalid_action_rate": 0.0,
            "focus_2_5_mbps": {
                "bucket_present": True,
                "selected_utility_regret_vs_best_immediate_mean": 0.06,
                "selected_rebuffer_regret_vs_best_immediate_mean": 0.01,
                "over_aggressive_rate_vs_oracle": 0.10,
                "invalid_action_rate": 0.0,
            },
        }

        self.assertLess(
            _selection_score(higher_loss_better_policy, profile),
            _selection_score(low_loss_bad_policy, profile),
        )

    def test_safety_gate_rejects_lower_regret_checkpoint_when_over_aggressive_regresses(self):
        profile = replace(
            profile_by_name("smoke"),
            safety_gate_enabled=True,
            safety_global_over_aggressive_tolerance=0.005,
            safety_focus_over_aggressive_tolerance=0.010,
            safety_spbc_v2_over_aggressive_tolerance=0.010,
            safety_utility_regret_tolerance=0.001,
            safety_rebuffer_regret_tolerance=0.001,
        )
        reference = {
            "selected_utility_regret_vs_oracle_mean": 0.060,
            "selected_rebuffer_regret_vs_oracle_mean": 0.010,
            "over_aggressive_rate_vs_oracle": 0.020,
            "under_aggressive_rate_vs_oracle": 0.250,
            "focus_2_5_mbps": {
                "bucket_present": True,
                "selected_utility_regret_vs_oracle_mean": 0.050,
                "selected_rebuffer_regret_vs_oracle_mean": 0.015,
                "over_aggressive_rate_vs_oracle": 0.060,
                "under_aggressive_rate_vs_oracle": 0.300,
            },
            "by_rollout_source": {
                "spbc_v2_dpo_on_policy": {
                    "selected_utility_regret_vs_oracle_mean": 0.080,
                    "selected_rebuffer_regret_vs_oracle_mean": 0.020,
                    "over_aggressive_rate_vs_oracle": 0.020,
                    "under_aggressive_rate_vs_oracle": 0.400,
                }
            },
        }
        candidate = {
            "selected_utility_regret_vs_oracle_mean": 0.040,
            "selected_rebuffer_regret_vs_oracle_mean": 0.006,
            "over_aggressive_rate_vs_oracle": 0.030,
            "under_aggressive_rate_vs_oracle": 0.100,
            "focus_2_5_mbps": {
                "bucket_present": True,
                "selected_utility_regret_vs_oracle_mean": 0.030,
                "selected_rebuffer_regret_vs_oracle_mean": 0.009,
                "over_aggressive_rate_vs_oracle": 0.090,
                "under_aggressive_rate_vs_oracle": 0.120,
            },
            "by_rollout_source": {
                "spbc_v2_dpo_on_policy": {
                    "selected_utility_regret_vs_oracle_mean": 0.060,
                    "selected_rebuffer_regret_vs_oracle_mean": 0.015,
                    "over_aggressive_rate_vs_oracle": 0.040,
                    "under_aggressive_rate_vs_oracle": 0.200,
                }
            },
        }

        result = _safety_gate_result(candidate, reference, profile)

        self.assertTrue(result["enabled"])
        self.assertFalse(result["passed"])
        self.assertIn("focus_2_5_mbps_over_aggressive", result["failed_checks"])
        self.assertIn("spbc_v2_dpo_on_policy_over_aggressive", result["failed_checks"])

    def test_training_with_safety_gate_reports_epoch_critical_metrics(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            spbc_checkpoint = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
            dataset_dir = build_unit_v2_dataset(root, with_spbc=True, checkpoint_path=spbc_checkpoint)
            v2_checkpoint = (
                root
                / "modelos"
                / "phase45_v1"
                / "spbc_abr_v2_dpo"
                / "full_v1_utility_risk_v1"
                / "modelo_spbc_abr_v2_dpo.pt"
            )
            write_stub_spbc_v2_dpo_checkpoint(v2_checkpoint)
            output_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "pilot_safe_gate"
            profile = replace(
                profile_by_name("smoke"),
                epochs=1,
                batch_size=32,
                max_training_samples=96,
                max_validation_samples=48,
                safety_gate_enabled=True,
            )

            report = train_spbc_abr_v2_dpo(
                dataset_dir,
                output_dir,
                profile=profile,
                overwrite=True,
                device="cpu",
                init_checkpoint=v2_checkpoint,
                validate_dataset=True,
                progress_callback=None,
            )
            report_file = read_json(output_dir / SPBC_V2_DPO_TRAINING_REPORT_FILENAME)
            first_epoch = report_file["epoch_reports"][0]

            self.assertEqual("PASS", report["status"])
            self.assertEqual(
                "validation_selection_score_with_safety_gate",
                report_file["checkpoint_selection"]["criterion"],
            )
            self.assertTrue(report_file["checkpoint_selection"]["safety_gate_enabled"])
            self.assertIsNotNone(report_file["safety_gate_reference_validation_critical_metrics"])
            self.assertTrue(report_file["selected_checkpoint_safety_gate"]["enabled"])
            self.assertIn("validation_critical_metrics", first_epoch)
            self.assertIn("validation_safety_gate", first_epoch)
            self.assertIn("validation_safety_gate_passed", first_epoch)
            self.assertIn("validation_focus_2_5_mbps_over_aggressive_rate_vs_oracle", first_epoch)
            self.assertIn("validation_spbc_v2_dpo_on_policy_selected_utility_regret_vs_oracle_mean", first_epoch)


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
