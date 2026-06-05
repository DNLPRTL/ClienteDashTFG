from __future__ import annotations

PHASE4_TRAINING_DATA_SCHEMA_ID = "phase4_datos_para_entrenamiento_v1"
PHASE4_FEATURE_SCHEMA_ID = "phase4_esquema_features_modelo_v1"
PHASE4_LABEL_SCHEMA_ID = "phase4_esquema_labels_teacher_v1"
PHASE4_NORMALIZATION_SCHEMA_ID = "phase4_estadisticas_normalizacion_v1"
PHASE4_LEAKAGE_AUDIT_SCHEMA_ID = "phase4_auditoria_no_contaminacion_v1"
PHASE4_TRAINING_SMOKE_SCHEMA_ID = "phase4_prueba_rapida_entrenamiento_v1"
PHASE4_MODEL_CONFIG_SCHEMA_ID = "phase4_neural_abr_lite_model_config_v1"
PHASE4_FORMAL_TRAINING_SCHEMA_ID = "phase4_entrenamiento_modelo_candidato_v1"
PHASE4_CANDIDATE_REVIEW_SCHEMA_ID = "phase4_revision_modelo_candidato_v1"

TRAINING_ROLE = "training"
VALIDATION_ROLE = "validation"
DATA_ROLES = (TRAINING_ROLE, VALIDATION_ROLE)

TRAINING_DATA_FILENAME = "datos_entrenamiento.jsonl"
VALIDATION_DATA_FILENAME = "datos_validacion.jsonl"
TRAINING_DATA_SUMMARY_FILENAME = "resumen_datos_entrenamiento.json"
FEATURE_SCHEMA_FILENAME = "esquema_features_modelo.json"
LABEL_SCHEMA_FILENAME = "esquema_labels_teacher.json"
LEAKAGE_AUDIT_FILENAME = "auditoria_no_contaminacion.json"
NORMALIZATION_STATS_FILENAME = "estadisticas_normalizacion_train_only.json"
TRAINING_SMOKE_REPORT_FILENAME = "reporte_prueba_rapida_entrenamiento.json"
CANDIDATE_MODEL_FILENAME = "modelo_candidato_neural_abr_lite.pt"
CANDIDATE_MODEL_CONFIG_FILENAME = "configuracion_modelo.json"
FORMAL_TRAINING_REPORT_FILENAME = "reporte_entrenamiento_modelo.json"
CANDIDATE_REVIEW_REPORT_FILENAME = "reporte_revision_modelo_candidato.json"

DATA_FILENAMES = {
    TRAINING_ROLE: TRAINING_DATA_FILENAME,
    VALIDATION_ROLE: VALIDATION_DATA_FILENAME,
}

REQUIRED_TRAINING_DATA_FILES = (
    TRAINING_DATA_SUMMARY_FILENAME,
    TRAINING_DATA_FILENAME,
    VALIDATION_DATA_FILENAME,
    FEATURE_SCHEMA_FILENAME,
    LABEL_SCHEMA_FILENAME,
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
)

PRIMARY_TEACHER = "robust_mpc"
REWARD_VERSION = "qoe_linear_v1"
DEFAULT_SEGMENT_DURATION_S = 4.0
DEFAULT_WINDOW_DURATION_S = 120.0
DEFAULT_MAX_BUFFER_S = 20.0
DEFAULT_CONTEXT_HISTORY_LENGTH = 5
DEFAULT_REPRESENTATION_KBPS = (300, 750, 1200, 1850, 2850, 4300)

CONTEXT_ARRAY_FEATURES = (
    "throughput_history_bps",
    "download_time_history_s",
)

CONTEXT_SCALAR_FEATURES = (
    "buffer_s",
    "last_representation_index",
    "last_bitrate_bps",
    "recent_rebuffer_s",
    "recent_switch_abs",
    "chunks_remaining_norm",
    "has_chunks_remaining",
)

CANDIDATE_FEATURES = (
    "candidate_representation_index",
    "candidate_ladder_position_norm",
    "candidate_bitrate_bps",
    "candidate_bitrate_norm_ladder",
    "candidate_delta_from_last_bitrate_norm",
    "candidate_chunk_size_bytes",
    "candidate_chunk_size_available",
)

CONTEXT_VECTOR_NAMES = tuple(
    "throughput_history_bps_{0}".format(index) for index in range(DEFAULT_CONTEXT_HISTORY_LENGTH)
) + tuple("download_time_history_s_{0}".format(index) for index in range(DEFAULT_CONTEXT_HISTORY_LENGTH)) + tuple(
    CONTEXT_SCALAR_FEATURES
)

CANDIDATE_VECTOR_NAMES = CANDIDATE_FEATURES

FORBIDDEN_MODEL_INPUT_FIELDS = frozenset(
    {
        "trace_id",
        "dataset_id",
        "source_id",
        "split",
        "source_split",
        "training_plan_role",
        "data_role",
        "group_id",
        "leakage_group",
        "semantics",
        "network_condition",
        "synthetic",
        "synthetic_scenario",
        "future_throughput",
        "future_throughput_bps",
        "future_throughput_kbps",
        "future_download_time",
        "future_download_time_s",
        "future_reward",
        "future_qoe",
        "final_qoe",
        "teacher_action",
        "teacher_reward",
        "teacher_reward_n",
        "teacher_policy",
        "reward_version",
        "benchmark_result",
        "benchmark_rank",
        "controller_name",
    }
)
