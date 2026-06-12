from __future__ import annotations

PHASE45_V3_PHASE = "fase_4_5_v3_closed_loop_qh_dataset"

DATASET_SCHEMA_ID = "phase45_v3_closed_loop_qh_dataset_v1"
SAMPLE_SCHEMA_ID = "phase45_v3_closed_loop_qh_sample_v1"
FEATURE_SCHEMA_ID = "phase45_v3_model_inputs_schema_v1"
TARGET_SCHEMA_ID = "phase45_v3_qh_targets_schema_v1"
LEAKAGE_AUDIT_SCHEMA_ID = "phase45_v3_no_contamination_audit_v1"
NORMALIZATION_SCHEMA_ID = "phase45_v3_normalization_stats_v1"
QH_AUDIT_SCHEMA_ID = "phase45_v3_qh_oracle_audit_v1"

TRAINING_ROLE = "training"
VALIDATION_ROLE = "validation"
DATA_ROLES = (TRAINING_ROLE, VALIDATION_ROLE)

TRAINING_DATA_FILENAME = "datos_entrenamiento_phase45_v3_qh.jsonl"
VALIDATION_DATA_FILENAME = "datos_validacion_phase45_v3_qh.jsonl"
SUMMARY_FILENAME = "resumen_dataset_phase45_v3_qh.json"
SAMPLING_PLAN_FILENAME = "plan_muestreo_phase45_v3_qh.json"
SAMPLING_AUDIT_FILENAME = "auditoria_muestreo_phase45_v3_qh.json"
FEATURE_SCHEMA_FILENAME = "esquema_model_inputs_phase45_v3.json"
TARGET_SCHEMA_FILENAME = "esquema_targets_phase45_v3_qh.json"
LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion_phase45_v3.json"
NORMALIZATION_STATS_FILENAME = "estadisticas_normalizacion_train_only_phase45_v3.json"
QH_AUDIT_FILENAME = "auditoria_qh_oracle_phase45_v3.json"

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
    QH_AUDIT_FILENAME,
)

QH_TARGET_ID = "phase45_v3_qh_targets_v1"
MEDIA_PROFILE_ID = "paseo_10min_30fps_4s"
REWARD_VERSION = "qoe_linear_v1"

ROLLOUT_QH_ORACLE = "qh_oracle"
ROLLOUT_QH_MINUS_ONE = "qh_minus_one"
ROLLOUT_QH_PLUS_ONE = "qh_plus_one"
ROLLOUT_STARTUP_CONSERVATIVE = "startup_conservative"
ROLLOUT_POLICIES = (
    ROLLOUT_QH_ORACLE,
    ROLLOUT_QH_MINUS_ONE,
    ROLLOUT_QH_PLUS_ONE,
    ROLLOUT_STARTUP_CONSERVATIVE,
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
