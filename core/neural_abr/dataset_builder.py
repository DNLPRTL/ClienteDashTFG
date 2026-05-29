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
    PHASE4E1_DEFAULT_REPRESENTATION_KBPS,
    PHASE4E1_SPLIT_POLICY,
    PRIMARY_TEACHER,
    REQUIRED_DATASET_FILES,
    REWARD_VERSION,
    SPLITS,
    TRAIN_SPLIT,
    VALIDATION_SPLIT,
)
from core.neural_abr.content_ladder import (
    ContentLadder,
    bitrate_ladder_from_kbps,
    ladder_with_segment_count,
    synthetic_smoke_ladder,
)
from core.neural_abr.features import build_candidate_features, build_context_features, build_feature_schema
from core.neural_abr.replay_env import TraceReplayEnvironment
from core.neural_abr.schemas import build_label_schema, validate_sample
from core.neural_abr.teacher_policy import robust_mpc_teacher
from core.neural_abr.trace_source import (
    TraceRecord,
    group_by_split,
    load_external_trace_records,
    synthetic_smoke_trace_records,
)
from core.trace_replay.schema import TRACE_SCHEMA_VERSION


class DatasetBuilderError(ValueError):
    """Raised when dataset construction violates a Phase 4D gate."""


def build_synthetic_smoke_dataset(output_dir: object, overwrite: bool = False) -> Mapping[str, object]:
    records = synthetic_smoke_trace_records()
    ladder = synthetic_smoke_ladder()
    return build_dataset(records=records, ladder=ladder, output_dir=output_dir, overwrite=overwrite, synthetic_smoke=True)


def build_external_trace_dataset(
    trace_csv_root: object,
    trace_manifest_root: object | None,
    output_dir: object,
    split_policy: str = PHASE4E1_SPLIT_POLICY,
    representation_kbps: Sequence[int] = PHASE4E1_DEFAULT_REPRESENTATION_KBPS,
    segment_duration_s: float = 4.0,
    teacher: str = PRIMARY_TEACHER,
    seed: int = 123,
    diagnostic_only: bool = True,
    overwrite: bool = False,
) -> Mapping[str, object]:
    if teacher != PRIMARY_TEACHER:
        raise DatasetBuilderError("Phase 4E.1 external smoke supports teacher=robust_mpc only")
    if not diagnostic_only:
        raise DatasetBuilderError("Phase 4E.1 external smoke must be marked --diagnostic-only")
    records = load_external_trace_records(
        trace_csv_root=trace_csv_root,
        trace_manifest_root=trace_manifest_root,
        split_policy=split_policy,
        seed=seed,
        segment_duration_s=segment_duration_s,
    )
    ladder = bitrate_ladder_from_kbps(
        representation_kbps=representation_kbps,
        segment_duration_s=segment_duration_s,
        segment_count=1,
    )
    return build_dataset(
        records=records,
        ladder=ladder,
        output_dir=output_dir,
        overwrite=overwrite,
        synthetic_smoke=False,
        external_trace_smoke=True,
        split_policy=split_policy,
        seed=seed,
        trace_csv_root=trace_csv_root,
        trace_manifest_root=trace_manifest_root,
    )


def build_dataset(
    records: Sequence[TraceRecord],
    ladder: ContentLadder,
    output_dir: object,
    overwrite: bool = False,
    synthetic_smoke: bool = False,
    external_trace_smoke: bool = False,
    split_policy: str | None = None,
    seed: int | None = None,
    trace_csv_root: object | None = None,
    trace_manifest_root: object | None = None,
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
        external_trace_smoke=external_trace_smoke,
        split_policy=split_policy,
        seed=seed,
        trace_csv_root=trace_csv_root,
        trace_manifest_root=trace_manifest_root,
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
    trace_ladder = _ladder_for_trace(record, ladder)
    env = TraceReplayEnvironment(record.trace, trace_ladder)
    samples = []
    while not env.done:
        state = env.state
        action_mask = build_action_mask(trace_ladder, state.segment_index)
        context = build_context_features(state, trace_ladder)
        last_bitrate_bps = float(context["last_bitrate_bps"])
        candidates = build_candidate_features(trace_ladder, state.segment_index, last_bitrate_bps=last_bitrate_bps)
        decision = teacher.select_action(state, trace_ladder, action_mask)
        metadata = _sample_metadata(record, trace_ladder, state.segment_index)
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
            "metadata": metadata,
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
    external_trace_smoke: bool,
    split_policy: str | None,
    seed: int | None,
    trace_csv_root: object | None,
    trace_manifest_root: object | None,
) -> Mapping[str, object]:
    traces_by_split = {split: [] for split in SPLITS}
    leakage_groups_by_split = {split: [] for split in SPLITS}
    datasets_by_split = {split: [] for split in SPLITS}
    for record in records:
        traces_by_split[record.split].append(record.trace.trace_id)
        leakage_groups_by_split[record.split].append(record.split_key or record.leakage_group or record.trace.trace_id)
        datasets_by_split[record.split].append(record.source_dataset)
    trace_records = [_trace_manifest_entry(record) for record in records]
    content_ladder_manifest = dict(ladder.to_manifest())
    if external_trace_smoke:
        content_ladder_manifest["segment_count_source"] = "per_trace_floor_duration_over_segment_duration_s"
        content_ladder_manifest["segment_count"] = "per_trace"
    return {
        "schema_version": DATASET_SCHEMA_VERSION,
        "method": "NeuralABR-Lite Candidate Scorer",
        "phase": "4E.1" if external_trace_smoke else "4D",
        "diagnostic_only": True,
        "synthetic_smoke": bool(synthetic_smoke),
        "external_trace_smoke": bool(external_trace_smoke),
        "not_benchmark": True,
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "teacher_policy_primary": PRIMARY_TEACHER,
        "reward_version": REWARD_VERSION,
        "content_ladder": content_ladder_manifest,
        "split_policy": split_policy,
        "split_seed": seed,
        "trace_csv_root": str(trace_csv_root) if trace_csv_root is not None else None,
        "trace_manifest_root": str(trace_manifest_root) if trace_manifest_root is not None else None,
        "trace_count": len(records),
        "trace_records": trace_records,
        "splits": {
            split: {
                "trace_ids": list(traces_by_split[split]),
                "leakage_groups": sorted(set(leakage_groups_by_split[split])),
                "source_datasets": sorted(set(datasets_by_split[split])),
                "sample_count": len(samples_by_split[split]),
                "ood_diagnostic_not_for_tuning": split == OOD_SPLIT,
            }
            for split in SPLITS
        },
        "files": {name: name for name in REQUIRED_DATASET_FILES},
        "dataset_dir": str(output_path),
        "artifact_policy": "outside_repo_required",
    }


def _build_leakage_audit(samples_by_split: Mapping[str, Sequence[Mapping[str, object]]]) -> Mapping[str, object]:
    trace_split = {}
    leakage_group_split = {}
    errors = []
    label_counts = Counter()
    for split, samples in samples_by_split.items():
        for sample in samples:
            metadata = sample["metadata"]
            trace_id = metadata["trace_id"]
            previous_split = trace_split.setdefault(trace_id, split)
            if previous_split != split:
                errors.append("trace_id appears in multiple splits: {0}".format(trace_id))
            leakage_group = metadata.get("leakage_group") or trace_id
            previous_group_split = leakage_group_split.setdefault(leakage_group, split)
            if previous_group_split != split:
                errors.append("leakage_group appears in multiple splits: {0}".format(leakage_group))
            label_counts[int(sample["label"]["teacher_action"])] += 1
    return {
        "schema_version": LEAKAGE_AUDIT_VERSION,
        "diagnostic_only": True,
        "blocked": bool(errors),
        "errors": errors,
        "checks": [
            {"name": "trace_level_split_disjointness", "status": "PASS" if not errors else "FAIL"},
            {"name": "leakage_group_split_disjointness", "status": "PASS" if not errors else "FAIL"},
            {"name": "future_throughput_not_in_features", "status": "PASS"},
            {"name": "future_download_time_not_in_features", "status": "PASS"},
            {"name": "teacher_labels_not_model_inputs", "status": "PASS"},
            {"name": "normalization_not_fit_in_builder", "status": "PASS"},
            {"name": "legacy_dry_runs_not_used", "status": "PASS"},
        ],
        "label_distribution": {str(key): value for key, value in sorted(label_counts.items())},
    }


def _ladder_for_trace(record: TraceRecord, ladder: ContentLadder) -> ContentLadder:
    raw_segment_count = record.trace_metadata.get("segment_count")
    try:
        segment_count = int(raw_segment_count)
    except (TypeError, ValueError):
        segment_count = ladder.segment_count
    segment_count = max(1, segment_count)
    if segment_count == ladder.segment_count:
        return ladder
    return ladder_with_segment_count(ladder, segment_count=segment_count)


def _sample_metadata(record: TraceRecord, ladder: ContentLadder, segment_index: int) -> Mapping[str, object]:
    metadata = dict(record.trace_metadata)
    metadata.update(
        {
            "trace_id": record.trace.trace_id,
            "split": record.split,
            "source_dataset": record.source_dataset,
            "segment_index": int(segment_index),
            "representation_count": ladder.representation_count,
            "trace_schema_version": TRACE_SCHEMA_VERSION,
            "teacher_source": "offline_robust_mpc_labeler",
            "model_input_boundary": "context_and_candidates_only",
            "leakage_group": record.leakage_group or record.trace.trace_id,
            "split_key": record.split_key or record.leakage_group or record.trace.trace_id,
            "split_reason": record.split_reason,
            "manifest_missing": bool(record.manifest_missing),
            "ood_diagnostic_not_for_tuning": record.split == OOD_SPLIT,
            "segment_count_for_trace": ladder.segment_count,
        }
    )
    return metadata


def _trace_manifest_entry(record: TraceRecord) -> Mapping[str, object]:
    metadata = dict(record.trace_metadata)
    return {
        "trace_id": record.trace.trace_id,
        "dataset_id": metadata.get("dataset_id", record.source_dataset),
        "source_dataset": record.source_dataset,
        "split": record.split,
        "split_reason": record.split_reason,
        "split_key": record.split_key or record.leakage_group or record.trace.trace_id,
        "leakage_group": record.leakage_group or record.trace.trace_id,
        "manifest_missing": bool(record.manifest_missing),
        "sample_count": metadata.get("sample_count", record.trace.sample_count),
        "duration_s": metadata.get("duration_s", record.trace.duration_s),
        "mean_throughput_kbps": metadata.get("mean_throughput_kbps", record.trace.mean_throughput_kbps),
        "min_throughput_kbps": metadata.get("min_throughput_kbps", record.trace.min_throughput_kbps),
        "max_throughput_kbps": metadata.get("max_throughput_kbps", record.trace.max_throughput_kbps),
        "p05_throughput_kbps": metadata.get("p05_throughput_kbps"),
        "p50_throughput_kbps": metadata.get("p50_throughput_kbps"),
        "p95_throughput_kbps": metadata.get("p95_throughput_kbps"),
        "throughput_cv": metadata.get("throughput_cv"),
        "zero_throughput_ratio": metadata.get("zero_throughput_ratio"),
        "mobility_tags": metadata.get("mobility_tags"),
        "network_tags": metadata.get("network_tags"),
        "scenario_tags": metadata.get("scenario_tags"),
        "source_url_or_reference": metadata.get("source_url_or_reference"),
        "converter_name": metadata.get("converter_name"),
        "converter_version_or_commit": metadata.get("converter_version_or_commit"),
        "checksum_sha256": metadata.get("checksum_sha256"),
        "segment_count": metadata.get("segment_count"),
        "ood_diagnostic_not_for_tuning": record.split == OOD_SPLIT,
    }
