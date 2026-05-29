"""Constants for the Phase 4D offline NeuralABR-Lite pipeline."""

from __future__ import annotations

DATASET_SCHEMA_VERSION = "neural_abr_lite_dataset_v1"
FEATURE_SCHEMA_VERSION = "neural_abr_lite_feature_schema_v1"
LABEL_SCHEMA_VERSION = "neural_abr_lite_label_schema_v1"
LEAKAGE_AUDIT_VERSION = "neural_abr_lite_leakage_audit_v1"
MODEL_CONFIG_VERSION = "neural_abr_lite_model_config_v1"
NORMALIZATION_SCHEMA_VERSION = "neural_abr_lite_normalization_v1"
TRAINING_REPORT_VERSION = "neural_abr_lite_training_report_v1"
OFFLINE_VALIDATION_REPORT_VERSION = "neural_abr_lite_offline_validation_report_v1"

K_CONTEXT = 5

TRAIN_SPLIT = "train"
VALIDATION_SPLIT = "validation"
OOD_SPLIT = "ood_diagnostic"
SPLITS = (TRAIN_SPLIT, VALIDATION_SPLIT, OOD_SPLIT)
PHASE4E1_SPLIT_POLICY = "phase4e1_trace_level_regime_v1"

REWARD_VERSION = "qoe_linear_v1"
PRIMARY_TEACHER = "robust_mpc"
SECONDARY_TEACHER = "mpc"
BOUNDED_ORACLE_TEACHER = "bounded_oracle_diagnostic_only"

DEFAULT_SEGMENT_DURATION_S = 4.0
DEFAULT_MAX_BUFFER_S = 20.0
PHASE4E1_DEFAULT_REPRESENTATION_KBPS = (300, 750, 1200, 1850, 2850)

EXTERNAL_TRACE_METADATA_FIELDS = (
    "trace_id",
    "dataset_id",
    "leakage_group",
    "mean_throughput_kbps",
    "min_throughput_kbps",
    "max_throughput_kbps",
    "sample_count",
    "mobility_tags",
    "network_tags",
    "scenario_tags",
    "source_url_or_reference",
    "converter_name",
    "converter_version_or_commit",
    "checksum_sha256",
    "source_dataset",
    "source_file",
    "mobility_label",
    "network_type",
    "scenario_label",
    "notes",
)

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
    "throughput_history_bps_{0}".format(index) for index in range(K_CONTEXT)
) + tuple("download_time_history_s_{0}".format(index) for index in range(K_CONTEXT)) + CONTEXT_SCALAR_FEATURES

CANDIDATE_VECTOR_NAMES = CANDIDATE_FEATURES

FORBIDDEN_MODEL_INPUT_KEYS = frozenset(
    {
        "future_throughput",
        "future_throughput_bps",
        "future_download_time",
        "future_download_time_s",
        "future_rebuffer",
        "future_rebuffer_s",
        "future_reward",
        "future_qoe",
        "teacher_action",
        "teacher_reward",
        "teacher_reward_n",
        "teacher_score",
        "split",
        "trace_id",
        "source_dataset",
        "regime_label",
        "benchmark_result",
        "benchmark_rank",
        "controller_name",
    }
)

DATASET_FILENAMES = {
    TRAIN_SPLIT: "train.jsonl",
    VALIDATION_SPLIT: "validation.jsonl",
    OOD_SPLIT: "ood_diagnostic.jsonl",
}

REQUIRED_DATASET_FILES = (
    "dataset_manifest.json",
    DATASET_FILENAMES[TRAIN_SPLIT],
    DATASET_FILENAMES[VALIDATION_SPLIT],
    DATASET_FILENAMES[OOD_SPLIT],
    "feature_schema.json",
    "label_schema.json",
    "leakage_audit.json",
)
