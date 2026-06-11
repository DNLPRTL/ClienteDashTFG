from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import torch

from core.neural_abr.artifacts import read_json
from core.phase45_v1.spc_v2_reward_risk_training import (
    SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID,
    SPC_V2_REWARD_RISK_MODEL_KEY,
    SPC_V2_REWARD_RISK_MODEL_FILENAME,
    SpcAbrV2RewardRiskScorer,
    fit_spc_v2_reward_risk_normalization,
)
from core.phase45_v1.spbc_spc_v2_hybrid_validation import (
    SPBC_SPC_V2_HYBRID_VALIDATION_REPORT_FILENAME,
    hybrid_profile_by_name,
    validate_spbc_spc_v2_hybrid_offline,
)
from core.phase45_v1.spbc_v2_dpo_training import (
    SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
    SPBC_V2_DPO_MODEL_FILENAME,
    SPBC_V2_DPO_MODEL_KEY,
    SpbcAbrV2DpoPolicy,
    fit_spbc_v2_dpo_normalization,
    load_spbc_v2_dpo_examples,
)
from core.phase45_v1.preference_dataset_v2 import V2_TRAINING_DATA_FILENAME
from tests.test_phase45_v2_spbc_dpo_training import build_unit_v2_dataset


class Phase45V2SpbcSpcHybridValidationTest(unittest.TestCase):
    def test_hybrid_validation_reports_driver_copilot_modes_without_benchmark_flags(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=False)
            examples = load_spbc_v2_dpo_examples(dataset_dir / V2_TRAINING_DATA_FILENAME, "training", limit=48)
            spbc_checkpoint = root / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "stub" / SPBC_V2_DPO_MODEL_FILENAME
            spc_checkpoint = (
                root
                / "modelos"
                / "phase45_v1"
                / "spc_abr_v2_reward_risk"
                / "stub"
                / SPC_V2_REWARD_RISK_MODEL_FILENAME
            )
            _write_stub_spbc_v2_checkpoint(spbc_checkpoint, examples)
            _write_stub_spc_v2_checkpoint(spc_checkpoint, examples)
            output_dir = root / "modelos" / "phase45_v1" / "spbc_spc_v2_hybrid_offline" / "stub"

            report = validate_spbc_spc_v2_hybrid_offline(
                dataset_dir,
                spbc_checkpoint,
                spc_checkpoint,
                output_dir,
                profile=hybrid_profile_by_name("smoke"),
                overwrite=True,
                device="cpu",
                max_validation_samples=32,
                validate_dataset=False,
                progress_callback=None,
            )
            report_file = read_json(output_dir / SPBC_SPC_V2_HYBRID_VALIDATION_REPORT_FILENAME)

            self.assertEqual("PASS", report["status"])
            self.assertIn("spbc_only", report_file["mode_metrics"])
            self.assertIn("spc_only_reward", report_file["mode_metrics"])
            self.assertIn("spbc_spc_veto_only", report_file["mode_metrics"])
            self.assertIn("spbc_spc_topk_rerank", report_file["mode_metrics"])
            self.assertIn("spbc_spc_veto_only", report_file["hybrid_gates"])
            veto_metrics = report_file["mode_metrics"]["spbc_spc_veto_only"]
            self.assertIn("harmful_intervention_rate", veto_metrics)
            self.assertIn("intervention_reward_delta_mean", veto_metrics)
            self.assertIn("over_aggressive_fix_rate", veto_metrics)
            self.assertIn("intervention", report_file["hybrid_gates"]["spbc_spc_veto_only"])
            self.assertIn("risk_brier", report_file["spc_prediction_metrics"])
            self.assertFalse(report_file["benchmark_performed"])
            self.assertFalse(report_file["ranking_performed"])
            self.assertTrue(report_file["no_final_ranking"])
            self.assertFalse(report_file["ia_training_performed"])
            self.assertFalse(report_file["bundle_exported"])
            self.assertFalse(report_file["controller_registered"])


def _write_stub_spbc_v2_checkpoint(path: Path, examples) -> None:
    normalization = fit_spbc_v2_dpo_normalization(examples)
    model = SpbcAbrV2DpoPolicy(
        history_hidden_size=8,
        state_hidden_size=8,
        candidate_hidden_size=8,
        shared_hidden_size=16,
        dropout=0.0,
    )
    _save_checkpoint(
        path,
        {
            "schema_id": SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
            "model_key": SPBC_V2_DPO_MODEL_KEY,
            "model_state_dict": model.state_dict(),
            "model_config": dict(model.config()),
            "normalization": normalization.to_json(),
        },
    )


def _write_stub_spc_v2_checkpoint(path: Path, examples) -> None:
    normalization = fit_spc_v2_reward_risk_normalization(examples)
    model = SpcAbrV2RewardRiskScorer(
        history_hidden_size=8,
        state_hidden_size=8,
        candidate_hidden_size=8,
        shared_hidden_size=16,
        dropout=0.0,
        score_rebuffer_weight=0.0,
        score_risk_weight=0.0,
        score_smoothness_weight=0.0,
        score_qoe_gap_weight=0.0,
    )
    _save_checkpoint(
        path,
        {
            "schema_id": SPC_V2_REWARD_RISK_CHECKPOINT_SCHEMA_ID,
            "model_key": SPC_V2_REWARD_RISK_MODEL_KEY,
            "model_state_dict": model.state_dict(),
            "model_config": dict(model.config()),
            "normalization": normalization.to_json(),
        },
    )


def _save_checkpoint(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(payload, path)


if __name__ == "__main__":
    unittest.main()
