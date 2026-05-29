"""Trace loading helpers for Phase 4D/4E.1/4E.2.

The loader delegates normalized trace validation/loading to Phase 3 modules and
does not define a parallel raw trace schema.
"""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Iterable, Mapping, Sequence, Tuple

from core.neural_abr.constants import (
    EXTERNAL_TRACE_METADATA_FIELDS,
    OOD_SPLIT,
    PHASE4E1_SPLIT_POLICY,
    PHASE4E2_SPLIT_POLICY,
    SPLITS,
    TRAIN_SPLIT,
    VALIDATION_SPLIT,
)
from core.neural_abr.artifacts import read_json
from core.trace_replay.loader import LoadedTrace, load_normalized_trace_csv, load_normalized_trace_rows
from core.trace_replay.schema import TRACE_SCHEMA_VERSION

SUPPORTED_EXTERNAL_SPLIT_POLICIES = (
    PHASE4E1_SPLIT_POLICY,
    PHASE4E2_SPLIT_POLICY,
)


class TraceSourceError(ValueError):
    """Raised when trace source manifests violate Phase 4D/4E rules."""


@dataclass(frozen=True)
class TraceRecord:
    trace: LoadedTrace
    split: str
    source_dataset: str
    diagnostic_only: bool = True
    trace_metadata: Mapping[str, object] = field(default_factory=dict)
    split_reason: str = ""
    leakage_group: str = ""
    split_key: str = ""
    manifest_missing: bool = False


def load_trace_manifest(path: object) -> Tuple[TraceRecord, ...]:
    manifest_path = Path(path)
    payload = read_json(manifest_path)
    traces = payload.get("traces")
    if not isinstance(traces, Sequence) or isinstance(traces, (str, bytes)):
        raise TraceSourceError("trace manifest must contain a traces list")

    records = []
    seen_trace_ids = set()
    for entry in traces:
        if not isinstance(entry, Mapping):
            raise TraceSourceError("trace manifest entries must be mappings")
        split = str(entry.get("split", ""))
        if split not in SPLITS:
            raise TraceSourceError("invalid trace split: {0}".format(split))
        trace_id = str(entry.get("trace_id", "")).strip()
        if not trace_id:
            raise TraceSourceError("trace_id must be non-empty")
        if trace_id in seen_trace_ids:
            raise TraceSourceError("duplicate trace_id: {0}".format(trace_id))
        seen_trace_ids.add(trace_id)

        trace_path = Path(str(entry.get("path", "")))
        if not trace_path.is_absolute():
            trace_path = (manifest_path.parent / trace_path).resolve()
        trace = load_normalized_trace_csv(trace_path, trace_id=trace_id, strict=True)
        if trace.schema_version != TRACE_SCHEMA_VERSION:
            raise TraceSourceError("trace must use {0}".format(TRACE_SCHEMA_VERSION))
        source_dataset = str(entry.get("source_dataset", "external_normalized_trace")).strip()
        metadata = {
            "trace_id": trace.trace_id,
            "dataset_id": source_dataset,
            "leakage_group": trace.trace_id,
            "manifest_missing": True,
            "split_policy": "explicit_manifest",
            "split_reason": "explicit_split_from_manifest",
            "split_key": trace.trace_id,
            "segment_count": _segment_count_for_trace(trace, 4.0),
        }
        records.append(
            TraceRecord(
                trace=trace,
                split=split,
                source_dataset=source_dataset,
                trace_metadata=metadata,
                split_reason="explicit_split_from_manifest",
                leakage_group=trace.trace_id,
                split_key=trace.trace_id,
                manifest_missing=True,
            )
        )
    return tuple(records)


def load_external_trace_records(
    trace_csv_root: object,
    trace_manifest_root: object | None = None,
    split_policy: str = PHASE4E1_SPLIT_POLICY,
    seed: int = 123,
    segment_duration_s: float = 4.0,
) -> Tuple[TraceRecord, ...]:
    if split_policy not in SUPPORTED_EXTERNAL_SPLIT_POLICIES:
        raise TraceSourceError("unsupported split policy: {0}".format(split_policy))

    csv_root = Path(trace_csv_root).expanduser().resolve()
    if not csv_root.is_dir():
        raise TraceSourceError("trace-csv-root does not exist: {0}".format(csv_root))
    manifest_root = None
    if trace_manifest_root is not None:
        manifest_root = Path(trace_manifest_root).expanduser().resolve()
        if not manifest_root.is_dir():
            raise TraceSourceError("trace-manifest-root does not exist: {0}".format(manifest_root))

    csv_paths = tuple(sorted(path for path in csv_root.rglob("*.csv") if path.is_file()))
    if not csv_paths:
        raise TraceSourceError("trace-csv-root contains no CSV traces")

    manifest_index = _build_manifest_index(manifest_root) if manifest_root is not None else {}
    unsplit_records = []
    seen_trace_ids = set()
    for csv_path in csv_paths:
        manifest_path = _matching_manifest_path(csv_path, csv_root, manifest_root, manifest_index)
        manifest = read_json(manifest_path) if manifest_path is not None else {}
        if not isinstance(manifest, Mapping):
            raise TraceSourceError("trace manifest must be a JSON object: {0}".format(manifest_path))

        trace_id = _text(manifest.get("trace_id")) or csv_path.stem
        if trace_id in seen_trace_ids:
            raise TraceSourceError("duplicate trace_id: {0}".format(trace_id))
        seen_trace_ids.add(trace_id)

        trace = load_normalized_trace_csv(csv_path, trace_id=trace_id, strict=True)
        metadata = _external_trace_metadata(
            trace=trace,
            csv_path=csv_path,
            csv_root=csv_root,
            manifest=manifest,
            manifest_path=manifest_path,
            segment_duration_s=segment_duration_s,
            split_policy=split_policy,
        )
        source_dataset = _text(metadata.get("dataset_id")) or _text(metadata.get("source_dataset")) or csv_path.parent.name
        leakage_group = _text(metadata.get("leakage_group")) or trace_id
        split_key = leakage_group or trace_id
        unsplit_records.append(
            TraceRecord(
                trace=trace,
                split="",
                source_dataset=source_dataset,
                diagnostic_only=True,
                trace_metadata=metadata,
                leakage_group=leakage_group,
                split_key=split_key,
                manifest_missing=bool(metadata.get("manifest_missing")),
            )
        )

    if split_policy == PHASE4E2_SPLIT_POLICY:
        return _apply_phase4e2_regime_balanced_split(unsplit_records, seed=seed)

    return _apply_phase4e1_split(unsplit_records, seed=seed)


def synthetic_smoke_trace_records() -> Tuple[TraceRecord, ...]:
    return (
        _synthetic_trace_record("synthetic_train_variable_a", TRAIN_SPLIT, (900, 1300, 2100, 2600, 1800, 3200)),
        _synthetic_trace_record("synthetic_train_variable_b", TRAIN_SPLIT, (1800, 2800, 4200, 2400, 1500, 3600)),
        _synthetic_trace_record("synthetic_validation_variable", VALIDATION_SPLIT, (1000, 1600, 2300, 1900, 2900, 1700)),
        _synthetic_trace_record("synthetic_ood_diagnostic_low_high", OOD_SPLIT, (450, 650, 5200, 4700, 800, 3800)),
    )


def group_by_split(records: Iterable[TraceRecord]) -> Mapping[str, Tuple[TraceRecord, ...]]:
    grouped = {split: [] for split in SPLITS}
    seen = set()
    leakage_groups = {}
    for record in records:
        if record.split not in SPLITS:
            raise TraceSourceError("invalid split: {0}".format(record.split))
        if record.trace.trace_id in seen:
            raise TraceSourceError("trace_id appears in more than one split: {0}".format(record.trace.trace_id))
        seen.add(record.trace.trace_id)
        split_key = record.split_key or record.leakage_group or record.trace.trace_id
        previous_split = leakage_groups.setdefault(split_key, record.split)
        if previous_split != record.split:
            raise TraceSourceError("leakage group appears in more than one split: {0}".format(split_key))
        grouped[record.split].append(record)
    return {split: tuple(values) for split, values in grouped.items()}


def _synthetic_trace_record(trace_id: str, split: str, throughput_pattern_kbps: Sequence[int]) -> TraceRecord:
    rows = []
    timestamp_s = 0.0
    for sample_index in range(48):
        throughput_kbps = throughput_pattern_kbps[sample_index % len(throughput_pattern_kbps)]
        rows.append(
            {
                "timestamp_s": "{0:.3f}".format(timestamp_s),
                "duration_s": "1.000",
                "throughput_kbps": str(throughput_kbps),
                "source_dataset": "synthetic_smoke_diagnostic_only",
            }
        )
        timestamp_s += 1.0
    trace = load_normalized_trace_rows(rows, trace_id=trace_id, source="synthetic_smoke:{0}".format(trace_id))
    metadata = {
        "trace_id": trace_id,
        "dataset_id": "synthetic_smoke_diagnostic_only",
        "leakage_group": trace_id,
        "manifest_missing": False,
        "split_policy": "synthetic_fixed_split",
        "split_reason": "phase4d_synthetic_smoke_fixture",
        "split_key": trace_id,
        "segment_count": 12,
        "sample_count": trace.sample_count,
        "duration_s": trace.duration_s,
        "mean_throughput_kbps": trace.mean_throughput_kbps,
        "min_throughput_kbps": trace.min_throughput_kbps,
        "max_throughput_kbps": trace.max_throughput_kbps,
    }
    return TraceRecord(
        trace=trace,
        split=split,
        source_dataset="synthetic_smoke_diagnostic_only",
        trace_metadata=metadata,
        split_reason="phase4d_synthetic_smoke_fixture",
        leakage_group=trace_id,
        split_key=trace_id,
        manifest_missing=False,
    )


def _external_trace_metadata(
    trace: LoadedTrace,
    csv_path: Path,
    csv_root: Path,
    manifest: Mapping[str, object],
    manifest_path: Path | None,
    segment_duration_s: float,
    split_policy: str,
) -> Mapping[str, object]:
    stats = _trace_stats(trace)
    csv_metadata = _first_sample_metadata(trace)
    dataset_id = _text(manifest.get("dataset_id")) or csv_metadata.get("source_dataset") or csv_path.parent.name
    trace_id = _text(manifest.get("trace_id")) or trace.trace_id
    leakage_group = _text(manifest.get("leakage_group")) or trace_id
    metadata = {
        "trace_id": trace_id,
        "dataset_id": dataset_id,
        "leakage_group": leakage_group,
        "manifest_missing": manifest_path is None,
        "manifest_path": str(manifest_path) if manifest_path is not None else None,
        "csv_path": str(csv_path),
        "csv_relative_path": str(csv_path.relative_to(csv_root)),
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "split_policy": split_policy,
        "split_key": leakage_group or trace_id,
        "segment_count": _segment_count_for_trace(trace, segment_duration_s),
        **stats,
    }

    for field_name in EXTERNAL_TRACE_METADATA_FIELDS:
        if field_name in manifest:
            metadata[field_name] = manifest[field_name]
        elif field_name in csv_metadata:
            metadata[field_name] = csv_metadata[field_name]

    for field_name in ("regime_bucket", "regime"):
        if field_name not in metadata:
            if field_name in manifest:
                metadata[field_name] = manifest[field_name]
            elif field_name in csv_metadata:
                metadata[field_name] = csv_metadata[field_name]

    if metadata["manifest_missing"]:
        metadata["source_url_or_reference"] = metadata.get("source_url_or_reference") or "missing_manifest_conservative_metadata"
        metadata["converter_name"] = metadata.get("converter_name") or "unknown_missing_manifest"
        metadata["converter_version_or_commit"] = metadata.get("converter_version_or_commit") or "unknown"
        metadata["checksum_sha256"] = metadata.get("checksum_sha256") or "unknown_missing_manifest"

    return metadata


def _apply_phase4e1_split(records: Sequence[TraceRecord], seed: int) -> Tuple[TraceRecord, ...]:
    groups = {}
    for record in records:
        key = record.split_key or record.leakage_group or record.trace.trace_id
        groups.setdefault(key, []).append(record)

    dataset_groups = {}
    for split_key, group_records in groups.items():
        dataset_id = _text(group_records[0].trace_metadata.get("dataset_id")) or group_records[0].source_dataset
        dataset_groups.setdefault(dataset_id, []).append((split_key, tuple(group_records)))

    assignments = {}
    reasons = {}
    for dataset_id, grouped_records in sorted(dataset_groups.items()):
        ordered = sorted(
            grouped_records,
            key=lambda item: (
                _group_mean_throughput(item[1]),
                _stable_tiebreaker("{0}:{1}".format(seed, item[0])),
            ),
        )
        if len(ordered) >= 3:
            ood_key = ordered[0][0]
            validation_key = ordered[len(ordered) // 2][0]
            for split_key, _records in ordered:
                if split_key == ood_key:
                    assignments[split_key] = OOD_SPLIT
                    reasons[split_key] = "phase4e1_low_mean_ood_within_dataset:{0}".format(dataset_id)
                elif split_key == validation_key:
                    assignments[split_key] = VALIDATION_SPLIT
                    reasons[split_key] = "phase4e1_median_regime_validation_within_dataset:{0}".format(dataset_id)
                else:
                    assignments[split_key] = TRAIN_SPLIT
                    reasons[split_key] = "phase4e1_remaining_train_within_dataset:{0}".format(dataset_id)
        elif len(ordered) == 2:
            assignments[ordered[0][0]] = TRAIN_SPLIT
            assignments[ordered[1][0]] = VALIDATION_SPLIT
            reasons[ordered[0][0]] = "phase4e1_small_dataset_train:{0}".format(dataset_id)
            reasons[ordered[1][0]] = "phase4e1_small_dataset_validation:{0}".format(dataset_id)
        else:
            assignments[ordered[0][0]] = TRAIN_SPLIT
            reasons[ordered[0][0]] = "phase4e1_single_trace_dataset_train:{0}".format(dataset_id)

    _ensure_required_splits(groups, assignments, reasons, seed, reason_prefix="phase4e1")

    split_records = []
    for record in records:
        key = record.split_key or record.leakage_group or record.trace.trace_id
        split = assignments[key]
        reason = reasons[key]
        metadata = dict(record.trace_metadata)
        metadata["split"] = split
        metadata["split_policy"] = PHASE4E1_SPLIT_POLICY
        metadata["split_reason"] = reason
        metadata["ood_diagnostic_not_for_tuning"] = split == OOD_SPLIT
        split_records.append(replace(record, split=split, split_reason=reason, trace_metadata=metadata))
    return tuple(sorted(split_records, key=lambda record: (record.split, record.source_dataset, record.trace.trace_id)))


def _apply_phase4e2_regime_balanced_split(records: Sequence[TraceRecord], seed: int) -> Tuple[TraceRecord, ...]:
    groups = {}
    for record in records:
        key = record.split_key or record.leakage_group or record.trace.trace_id
        groups.setdefault(key, []).append(record)

    strata = {}
    for split_key, group_records in groups.items():
        first = group_records[0]
        dataset_id = _text(first.trace_metadata.get("dataset_id")) or first.source_dataset or "unknown_dataset"
        regime_bucket = (
            _text(first.trace_metadata.get("regime_bucket"))
            or _text(first.trace_metadata.get("regime"))
            or "unknown_regime"
        )
        strata.setdefault((dataset_id, regime_bucket), []).append((split_key, tuple(group_records)))

    assignments = {}
    reasons = {}

    for (dataset_id, regime_bucket), grouped_records in sorted(strata.items()):
        ordered = sorted(
            grouped_records,
            key=lambda item: _stable_tiebreaker(
                "phase4e2:{0}:{1}:{2}:{3}".format(seed, dataset_id, regime_bucket, item[0])
            ),
        )

        count = len(ordered)
        stratum_label = "{0}/{1}".format(dataset_id, regime_bucket)

        if count >= 3:
            validation_count = max(1, int(round(count * 0.15)))
            ood_count = max(1, int(round(count * 0.15)))

            if validation_count + ood_count >= count:
                validation_count = 1
                ood_count = 1

            for index, (split_key, _records) in enumerate(ordered):
                if index < validation_count:
                    assignments[split_key] = VALIDATION_SPLIT
                    reasons[split_key] = "phase4e2_stratum_balanced_validation:{0}".format(stratum_label)
                elif index < validation_count + ood_count:
                    assignments[split_key] = OOD_SPLIT
                    reasons[split_key] = "phase4e2_stratum_balanced_ood:{0}".format(stratum_label)
                else:
                    assignments[split_key] = TRAIN_SPLIT
                    reasons[split_key] = "phase4e2_stratum_balanced_train:{0}".format(stratum_label)

        elif count == 2:
            assignments[ordered[0][0]] = TRAIN_SPLIT
            assignments[ordered[1][0]] = VALIDATION_SPLIT
            reasons[ordered[0][0]] = "phase4e2_small_stratum_train:{0}".format(stratum_label)
            reasons[ordered[1][0]] = "phase4e2_small_stratum_validation:{0}".format(stratum_label)

        elif count == 1:
            assignments[ordered[0][0]] = TRAIN_SPLIT
            reasons[ordered[0][0]] = "phase4e2_single_trace_stratum_train:{0}".format(stratum_label)

    _ensure_required_splits(groups, assignments, reasons, seed, reason_prefix="phase4e2")
    split_summary = _phase4e2_split_summary(groups, assignments)
    split_limitations = _phase4e2_split_limitations(strata, split_summary)

    split_records = []
    for record in records:
        key = record.split_key or record.leakage_group or record.trace.trace_id
        split = assignments[key]
        reason = reasons[key]

        metadata = dict(record.trace_metadata)
        metadata["split"] = split
        metadata["split_policy"] = PHASE4E2_SPLIT_POLICY
        metadata["split_reason"] = reason
        metadata["ood_diagnostic_not_for_tuning"] = split == OOD_SPLIT
        metadata["phase4e2_split_summary"] = split_summary
        metadata["phase4e2_split_limitations"] = split_limitations

        split_records.append(
            replace(
                record,
                split=split,
                split_reason=reason,
                trace_metadata=metadata,
            )
        )

    return tuple(
        sorted(
            split_records,
            key=lambda record: (record.split, record.source_dataset, record.trace.trace_id),
        )
    )


def _phase4e2_split_summary(groups, assignments) -> Mapping[str, object]:
    summary = {
        split: {
            "trace_group_count": 0,
            "dataset_id_counts": {},
            "regime_bucket_counts": {},
        }
        for split in SPLITS
    }
    for split_key, group_records in groups.items():
        split = assignments[split_key]
        first = group_records[0]
        dataset_id = _text(first.trace_metadata.get("dataset_id")) or first.source_dataset or "unknown_dataset"
        regime_bucket = (
            _text(first.trace_metadata.get("regime_bucket"))
            or _text(first.trace_metadata.get("regime"))
            or "unknown_regime"
        )
        split_entry = summary[split]
        split_entry["trace_group_count"] += 1
        _increment_count(split_entry["dataset_id_counts"], dataset_id)
        _increment_count(split_entry["regime_bucket_counts"], regime_bucket)
    return summary


def _phase4e2_split_limitations(strata, split_summary: Mapping[str, object]) -> Tuple[str, ...]:
    limitations = []
    small_strata = [
        "{0}/{1}:{2}".format(dataset_id, regime_bucket, len(grouped_records))
        for (dataset_id, regime_bucket), grouped_records in sorted(strata.items())
        if len(grouped_records) < 3
    ]
    if small_strata:
        limitations.append(
            "some dataset/regime strata have fewer than 3 trace groups, so perfect train/validation/OOD balance is impossible"
        )
    for split in SPLITS:
        split_entry = split_summary[split]
        if not split_entry["dataset_id_counts"]:
            limitations.append("{0} split is empty".format(split))
    return tuple(limitations)


def _ensure_required_splits(groups, assignments, reasons, seed: int, reason_prefix: str) -> None:
    if len(groups) < 3:
        return
    for required_split in (VALIDATION_SPLIT, OOD_SPLIT):
        if required_split in assignments.values():
            continue
        train_keys = [key for key, split in assignments.items() if split == TRAIN_SPLIT]
        if not train_keys:
            return
        if required_split == OOD_SPLIT:
            chosen = min(
                train_keys,
                key=lambda key: (
                    _group_mean_throughput(groups[key]),
                    _stable_tiebreaker(str(seed) + key),
                ),
            )
            reasons[chosen] = "{0}_global_low_mean_ood_backfill".format(reason_prefix)
        else:
            chosen = sorted(
                train_keys,
                key=lambda key: (
                    _group_mean_throughput(groups[key]),
                    _stable_tiebreaker(str(seed) + key),
                ),
            )[len(train_keys) // 2]
            reasons[chosen] = "{0}_global_validation_backfill".format(reason_prefix)
        assignments[chosen] = required_split


def _build_manifest_index(manifest_root: Path | None) -> Mapping[str, Path]:
    if manifest_root is None:
        return {}
    index = {}
    for path in sorted(manifest_root.rglob("*.json")):
        index.setdefault(path.stem, path)
    return index


def _matching_manifest_path(csv_path: Path, csv_root: Path, manifest_root: Path | None, manifest_index: Mapping[str, Path]) -> Path | None:
    if manifest_root is None:
        return None
    relative_candidate = manifest_root / csv_path.relative_to(csv_root).with_suffix(".json")
    if relative_candidate.is_file():
        return relative_candidate
    return manifest_index.get(csv_path.stem)


def _first_sample_metadata(trace: LoadedTrace) -> Mapping[str, str]:
    if not trace.samples:
        return {}
    return dict(trace.samples[0].metadata)


def _trace_stats(trace: LoadedTrace) -> Mapping[str, object]:
    values = tuple(float(sample.throughput_kbps) for sample in trace.samples)
    mean = trace.mean_throughput_kbps or 0.0
    stdev = _population_stdev(values, mean)
    return {
        "sample_count": trace.sample_count,
        "duration_s": trace.duration_s,
        "mean_throughput_kbps": trace.mean_throughput_kbps,
        "min_throughput_kbps": trace.min_throughput_kbps,
        "max_throughput_kbps": trace.max_throughput_kbps,
        "p05_throughput_kbps": _percentile(values, 0.05),
        "p50_throughput_kbps": _percentile(values, 0.50),
        "p95_throughput_kbps": _percentile(values, 0.95),
        "throughput_cv": (stdev / mean) if mean > 0.0 else None,
        "zero_throughput_ratio": (sum(1 for value in values if value == 0.0) / float(len(values))) if values else 0.0,
    }


def _segment_count_for_trace(trace: LoadedTrace, segment_duration_s: float) -> int:
    try:
        duration = float(trace.duration_s)
        segment_duration = float(segment_duration_s)
    except (TypeError, ValueError):
        return 1
    if not math.isfinite(duration) or not math.isfinite(segment_duration) or segment_duration <= 0.0:
        return 1
    return max(1, int(duration // segment_duration))


def _group_mean_throughput(records: Sequence[TraceRecord]) -> float:
    values = []
    for record in records:
        raw = record.trace_metadata.get("mean_throughput_kbps")
        try:
            value = float(raw)
        except (TypeError, ValueError):
            value = 0.0
        if math.isfinite(value):
            values.append(value)
    return sum(values) / float(len(values)) if values else 0.0


def _stable_tiebreaker(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _increment_count(counts, key: str) -> None:
    counts[key] = counts.get(key, 0) + 1


def _population_stdev(values: Sequence[float], mean: float) -> float:
    if not values:
        return 0.0
    variance = sum((value - mean) * (value - mean) for value in values) / float(len(values))
    return math.sqrt(max(variance, 0.0))


def _percentile(values: Sequence[float], quantile: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = max(0.0, min(1.0, float(quantile))) * (len(ordered) - 1)
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def _text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()
