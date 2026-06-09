from __future__ import annotations

PHASE45_V1_PHASE = "fase_4_5_v1_dataset_derivado"

DATASET_SCHEMA_ID = "phase45_v1_spc_spbc_dataset_v1"
SAMPLE_SCHEMA_ID = "phase45_v1_spc_spbc_sample_v1"
SAMPLING_PLAN_SCHEMA_ID = "phase45_v1_sampling_plan_v1"
SAMPLING_AUDIT_SCHEMA_ID = "phase45_v1_sampling_audit_v1"
FEATURE_SCHEMA_ID = "phase45_v1_model_inputs_schema_v1"
TARGET_SCHEMA_ID = "phase45_v1_targets_schema_v1"
LEAKAGE_AUDIT_SCHEMA_ID = "phase45_v1_no_contamination_audit_v1"
NORMALIZATION_SCHEMA_ID = "phase45_v1_normalization_stats_v1"
ORACLE_AUDIT_SCHEMA_ID = "phase45_v1_oracle_qoe_beam_audit_v1"

TRAINING_ROLE = "training"
VALIDATION_ROLE = "validation"
DATA_ROLES = (TRAINING_ROLE, VALIDATION_ROLE)

TRAINING_DATA_FILENAME = "datos_entrenamiento_spc_spbc.jsonl"
VALIDATION_DATA_FILENAME = "datos_validacion_spc_spbc.jsonl"
SUMMARY_FILENAME = "resumen_dataset_phase45_v1.json"
SAMPLING_PLAN_FILENAME = "plan_muestreo_phase45_v1.json"
SAMPLING_AUDIT_FILENAME = "auditoria_muestreo_phase45_v1.json"
FEATURE_SCHEMA_FILENAME = "esquema_model_inputs_phase45_v1.json"
TARGET_SCHEMA_FILENAME = "esquema_targets_phase45_v1.json"
LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion_phase45_v1.json"
NORMALIZATION_STATS_FILENAME = "estadisticas_normalizacion_train_only_phase45_v1.json"
ORACLE_AUDIT_FILENAME = "auditoria_oracle_qoe_beam_v1.json"

DATA_FILENAMES = {
    TRAINING_ROLE: TRAINING_DATA_FILENAME,
    VALIDATION_ROLE: VALIDATION_DATA_FILENAME,
}

REQUIRED_DATASET_FILES = (
    SUMMARY_FILENAME,
    TRAINING_DATA_FILENAME,
    VALIDATION_DATA_FILENAME,
    SAMPLING_PLAN_FILENAME,
    SAMPLING_AUDIT_FILENAME,
    FEATURE_SCHEMA_FILENAME,
    TARGET_SCHEMA_FILENAME,
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    ORACLE_AUDIT_FILENAME,
)

ORACLE_POLICY_ID = "oracle_qoe_beam_v1"
SPC_TARGET_ID = "spc_targets_v1"
SPBC_TARGET_ID = "spbc_targets_v1"
MEDIA_PROFILE_ID = "paseo_10min_30fps_4s"
REWARD_VERSION = "qoe_linear_v1"

CLASSIC_AUDIT_CONTROLLERS = ("rate_based", "bba", "bola", "mpc", "robust_mpc")

THROUGHPUT_BUCKETS = (
    "lte_1_mbps",
    "1_2_mbps",
    "2_5_mbps",
    "5_20_mbps",
    "gt_20_mbps",
)

FORBIDDEN_MODEL_INPUT_FIELDS = frozenset(
    {
        "trace_id",
        "dataset_id",
        "source_id",
        "split",
        "source_split",
        "group_id",
        "leakage_group",
        "semantics",
        "network_condition",
        "synthetic",
        "synthetic_scenario",
        "window_id",
        "window_start_s",
        "window_end_s",
        "training_plan_role",
        "data_role",
        "metadata",
        "future_throughput",
        "future_throughput_kbps",
        "future_download_time_s",
        "future_rebuffer_s",
        "oracle_action",
        "teacher_action",
        "teacher_policy",
        "controller_name",
        "benchmark_result",
        "benchmark_rank",
    }
)


def no_benchmark_policy() -> dict[str, object]:
    return {
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": False,
        "formal_ia_training_performed": False,
        "candidate_model_created": False,
        "qoe_claims_authorized": False,
    }
