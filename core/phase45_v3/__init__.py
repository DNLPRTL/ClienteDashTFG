"""Phase 4-5 v3 closed-loop ABR utilities."""

__all__ = [
    "AbrClosedLoopEnv",
    "Phase45V3DatasetProfile",
    "QhOracleConfig",
    "build_phase45_v3_closedloop_spbc_spc_dataset",
    "build_phase45_v3_qh_dataset",
    "default_phase45_v3_ladder",
    "evaluate_qh_actions",
    "profile_by_name",
    "validate_phase45_v3_closedloop_spbc_spc_dataset_dir",
    "validate_phase45_v3_dataset_dir",
]


def __getattr__(name: str):
    if name in ("AbrClosedLoopEnv", "default_phase45_v3_ladder"):
        from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopEnv, default_phase45_v3_ladder

        return {"AbrClosedLoopEnv": AbrClosedLoopEnv, "default_phase45_v3_ladder": default_phase45_v3_ladder}[name]
    if name == "build_phase45_v3_qh_dataset":
        from core.phase45_v3.dataset import build_phase45_v3_qh_dataset

        return build_phase45_v3_qh_dataset
    if name == "build_phase45_v3_closedloop_spbc_spc_dataset":
        from core.phase45_v3.closedloop_spbc_spc_dataset import build_phase45_v3_closedloop_spbc_spc_dataset

        return build_phase45_v3_closedloop_spbc_spc_dataset
    if name in ("Phase45V3DatasetProfile", "profile_by_name"):
        from core.phase45_v3.profiles import Phase45V3DatasetProfile, profile_by_name

        return {"Phase45V3DatasetProfile": Phase45V3DatasetProfile, "profile_by_name": profile_by_name}[name]
    if name in ("QhOracleConfig", "evaluate_qh_actions"):
        from core.phase45_v3.qh_oracle import QhOracleConfig, evaluate_qh_actions

        return {"QhOracleConfig": QhOracleConfig, "evaluate_qh_actions": evaluate_qh_actions}[name]
    if name == "validate_phase45_v3_dataset_dir":
        from core.phase45_v3.validation import validate_phase45_v3_dataset_dir

        return validate_phase45_v3_dataset_dir
    if name == "validate_phase45_v3_closedloop_spbc_spc_dataset_dir":
        from core.phase45_v3.closedloop_spbc_spc_dataset import validate_phase45_v3_closedloop_spbc_spc_dataset_dir

        return validate_phase45_v3_closedloop_spbc_spc_dataset_dir
    raise AttributeError(name)
