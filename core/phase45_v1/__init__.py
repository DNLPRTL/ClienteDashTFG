"""Phase 4-5 v1 offline dataset tooling for new ABR AI candidates."""

from __future__ import annotations

from core.phase45_v1.dataset import build_phase45_v1_dataset
from core.phase45_v1.offline_validation import apply_spc_guard, validate_spbc_spc_offline
from core.phase45_v1.preference_dataset_v2 import build_phase45_v2_dataset, validate_phase45_v2_dataset_dir
from core.phase45_v1.profiles import DatasetProfile, profile_by_name
from core.phase45_v1.spbc_training import SpbcAbrV1Policy, train_spbc_abr_v1
from core.phase45_v1.spbc_v2_dpo_training import SpbcAbrV2DpoPolicy, train_spbc_abr_v2_dpo
from core.phase45_v1.spc_training import SpcAbrV1Predictor, train_spc_abr_v1
from core.phase45_v1.spc_v2_reward_risk_training import SpcAbrV2RewardRiskScorer, train_spc_abr_v2_reward_risk
from core.phase45_v1.validation import validate_phase45_v1_dataset_dir

__all__ = [
    "DatasetProfile",
    "SpbcAbrV1Policy",
    "SpbcAbrV2DpoPolicy",
    "SpcAbrV1Predictor",
    "SpcAbrV2RewardRiskScorer",
    "apply_spc_guard",
    "build_phase45_v1_dataset",
    "build_phase45_v2_dataset",
    "profile_by_name",
    "train_spbc_abr_v1",
    "train_spbc_abr_v2_dpo",
    "train_spc_abr_v1",
    "train_spc_abr_v2_reward_risk",
    "validate_spbc_spc_offline",
    "validate_phase45_v1_dataset_dir",
    "validate_phase45_v2_dataset_dir",
]
