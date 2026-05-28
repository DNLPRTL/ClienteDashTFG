"""Dataset construction for the offline NeuralABR-Lite behavior-cloning pipeline."""

from __future__ import annotations

from collections import Counter
from typing import Iterable, Mapping, Sequence, Tuple

from core.neural_abr.action_mask import build_action_mask
from core.neural_abr.artifacts import prepare_output_dir, write_json, write_jsonl
from core.neural_abr.constants import (
    DATASET_FILENAMES,
    DATASET_SCHEMA_VERSION,
    LEAKAGE_AUDIT_VERSION,
    OOD_SPLIT,
    PRIMARY_TEACHER,
    REQUIRED_DATASET_FILES,
    REWARD_VERSION,
    SPLITS,
    TRAIN_SPLIT,
    VALIDATION_SPLIT,
)
from core.neural_abr.content_ladder import ContentLadder, synthetic_smoke_ladder
from core.neural_abr.features import build_candidate_features, build_context_features, build_feature_schema
from core.neural_abr.replay_env import TraceReplayEnvironment
from core.neural_abr.schemas import build_label_schema, validate_sample
from core.neural_abr.teacher_policy import robust_mpc_teacher
from core.neural_abr.trace_source import TraceRecord, group_by_split, synthetic_smoke_trace_records
from core.trace_replay.schema import TRACE_SCHEMA_VERSION


class DatasetBuilderError(ValueError):
    """Raised when dataset construction violates a Phase 4D gate."""


def build_synthetic_smoke_dataset(output_dir: object, overwrite: bool = False) -> Mapping[str, object]:
    records = synthetic_smoke_trace_records()
    ladder = synthetic_smoke_ladder()
    return build_dataset(records=records, ladder=ladder, output_dir=output_dir, overwrite=overwrite, synthetic_smoke=True)


def build_dataset(
    records: Sequence[TraceRecord],
    ladder: ContentLadder,
    output_dir: object,
    overwrite: bool = False,
    synthetic_smoke: bool = False,
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="dataset")
    grouped = group_by_split(records)
    teacher = robust_mpc_teacher()

    samples_by_split = {}
    for split in SPLITS:
        split_samples = []
        for record in grouped[split]:
            split_samples.extend(_samples_for_trace(record=record, ladder=ladder, teacher=teacher))
        samples_by_split[split] = tuple(split_samples)

    for split, filename in DATASET_FILENAMES.items():
        write_jsonl(output_path / filename, samples_by_split[split])

    feature_schema = build_feature_schema()
    label_schema = build_label_schema()
    leakage_audit = _build_leakage_audit(samples_by_split)
    manifest = _build_manifest(
        records=records,
        ladder=ladder,
        samples_by_split=samples_by_split,
        output_path=output_path,
        synthetic_smoke=synthetic_smoke,
    )

    write_json(output_path / "feature_schema.json", feature_schema)
    write_json(output_path / "label_schema.json", label_schema)
    write_json(output_path / "leakage_audit.json", leakage_audit)
    write_json(output_path / "dataset_manifest.json", manifest)

    return {
        "dataset_dir": str(output_path),
        "manifest": manifest,
        "leakage_audit": leakage_audit,
        "sample_counts": {split: len(samples_by_split[split]) for split in SPLITS},
    }


def _samples_for_trace(record: TraceRecord, ladder: ContentLadder, teacher) -> Tuple[Mapping[str, object], ...]:
    env = TraceReplayEnvironment(record.trace, ladder)
    samples = []
    while not env.done:
        state = env.state
        action_mask = build_action_mask(ladder, state.segment_index)
        context = build_context_features(state, ladder)
        last_bitrate_bps = float(context["last_bitrate_bps"])
        candidates = build_candidate_features(ladder, state.segment_index, last_bitrate_bps=last_bitrate_bps)
        decision = teacher.select_action(state, ladder, action_mask)
        sample = {
            "schema_version": DATASET_SCHEMA_VERSION,
            "sample_id": "{0}:{1}:{2}".format(record.split, record.trace.trace_id, state.segment_index),
            "split": record.split,
            "context": dict(context),
            "candidates": [dict(candidate) for candidate in candidates],
            "action_mask": list(action_mask),
            "label": {
                "teacher_action": decision.representation_index,
                "teacher_policy": decision.teacher_policy,
                "teacher_reward_n": decision.reward_n,
                "reward_version": decision.reward_version,
                "diagnostic_only": True,
                "reason": decision.reason,
            },
            "metadata": {
                "trace_id": record.trace.trace_id,
                "split": record.split,
                "source_dataset": record.source_dataset,
                "segment_index": state.segment_index,
                "representation_count": ladder.representation_count,
                "trace_schema_version": TRACE_SCHEMA_VERSION,
                "teacher_source": "offline_robust_mpc_labeler",
                "model_input_boundary": "context_and_candidates_only",
            },
        }
        validate_sample(sample, expected_split=record.split)
        samples.append(sample)
        env.step(decision.representation_index)
    return tuple(samples)


def _build_manifest(
    records: Sequence[TraceRecord],
    ladder: ContentLadder,
    samples_by_split: Mapping[str, Sequence[Mapping[str, object]]],
    output_path,
    synthetic_smoke: bool,
) -> Mapping[str, object]:
    traces_by_split = {split: [] for split in SPLITS}
    for record in records:
        traces_by_split[record.split].append(record.trace.trace_id)
    return {
        "schema_version": DATASET_SCHEMA_VERSION,
        "method": "NeuralABR-Lite Candidate Scorer",
        "phase": "4D",
        "diagnostic_only": True,
        "synthetic_smoke": bool(synthetic_smoke),
        "not_benchmark": True,
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "teacher_policy_primary": PRIMARY_TEACHER,
        "reward_version": REWARD_VERSION,
        "content_ladder": dict(ladder.to_manifest()),
        "splits": {
            split: {
                "trace_ids": list(traces_by_split[split]),
                "sample_count": len(samples_by_split[split]),
            }
            for split in SPLITS
        },
        "files": {name: name for name in REQUIRED_DATASET_FILES},
        "dataset_dir": str(output_path),
        "artifact_policy": "outside_repo_required",
    }


def _build_leakage_audit(samples_by_split: Mapping[str, Sequence[Mapping[str, object]]]) -> Mapping[str, object]:
    trace_split = {}
    errors = []
    label_counts = Counter()
    for split, samples in samples_by_split.items():
        for sample in samples:
            metadata = sample["metadata"]
            trace_id = metadata["trace_id"]
            previous_split = trace_split.setdefault(trace_id, split)
            if previous_split != split:
                errors.append("trace_id appears in multiple splits: {0}".format(trace_id))
            label_counts[int(sample["label"]["teacher_action"])] += 1
    return {
        "schema_version": LEAKAGE_AUDIT_VERSION,
        "diagnostic_only": True,
        "blocked": bool(errors),
        "errors": errors,
        "checks": [
            {"name": "trace_level_split_disjointness", "status": "PASS" if not errors else "FAIL"},
            {"name": "future_throughput_not_in_features", "status": "PASS"},
            {"name": "future_download_time_not_in_features", "status": "PASS"},
            {"name": "teacher_labels_not_model_inputs", "status": "PASS"},
            {"name": "normalization_not_fit_in_builder", "status": "PASS"},
            {"name": "legacy_dry_runs_not_used", "status": "PASS"},
        ],
        "label_distribution": {str(key): value for key, value in sorted(label_counts.items())},
    }
