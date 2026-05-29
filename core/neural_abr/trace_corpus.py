"""Phase 4E.2 external trace corpus preparation.

This module stages a diagnostic NeuralABR-Lite trace corpus from Phase 3
material. It only writes normalized CSV traces and compact manifests to an
outside-repository output root; raw inputs stay where they are.
"""

from __future__ import annotations

import csv
import hashlib
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence, Tuple

from core.neural_abr.artifacts import prepare_output_dir, read_json, write_json
from core.neural_abr.constants import TRACE_CORPUS_SCHEMA_VERSION
from core.trace_replay.loader import load_normalized_trace_csv, load_normalized_trace_rows
from core.trace_replay.schema import REQUIRED_TRACE_COLUMNS, TRACE_SCHEMA_VERSION


class TraceCorpusError(ValueError):
    """Raised when the Phase 4E.2 corpus cannot be prepared safely."""


@dataclass(frozen=True)
class CorpusCandidate:
    trace_id: str
    dataset_id: str
    leakage_group: str
    source_kind: str
    converter: str
    rows: Tuple[Mapping[str, object], ...]
    manifest: Mapping[str, object]
    source_path: str
    source_fingerprint: str
    source_priority: int


def prepare_phase4e2_trace_corpus(
    phase3_root: object,
    output_root: object,
    max_total_traces: int = 300,
    max_traces_per_dataset: int = 120,
    seed: int = 123,
    overwrite: bool = False,
) -> Mapping[str, object]:
    """Prepare a deterministic, regime-aware Phase 4E.2 trace corpus."""

    if max_total_traces <= 0:
        raise TraceCorpusError("max_total_traces must be positive")
    if max_traces_per_dataset <= 0:
        raise TraceCorpusError("max_traces_per_dataset must be positive")

    phase3_path = Path(phase3_root).expanduser().resolve()
    if not phase3_path.is_dir():
        raise TraceCorpusError("phase3_root does not exist: {0}".format(phase3_path))

    output_path = prepare_output_dir(output_root, overwrite=overwrite, purpose="Phase 4E.2 trace corpus")
    normalized_out = output_path / "normalized"
    manifests_out = output_path / "manifests"
    normalized_out.mkdir(parents=True, exist_ok=True)
    manifests_out.mkdir(parents=True, exist_ok=True)

    candidates, skipped = _collect_candidates(phase3_path)
    selected = _select_balanced_candidates(
        candidates,
        max_total_traces=max_total_traces,
        max_traces_per_dataset=max_traces_per_dataset,
        seed=seed,
    )

    selected_entries = []
    for candidate in selected:
        dataset_slug = _slug(candidate.dataset_id)
        csv_path = normalized_out / dataset_slug / (candidate.trace_id + ".csv")
        manifest_path = manifests_out / dataset_slug / (candidate.trace_id + ".json")
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        _write_normalized_csv(csv_path, candidate.rows)
        manifest = dict(candidate.manifest)
        manifest["output_csv_path"] = str(csv_path)
        manifest["output_manifest_path"] = str(manifest_path)
        write_json(manifest_path, manifest)
        selected_entries.append(
            {
                "trace_id": candidate.trace_id,
                "dataset_id": candidate.dataset_id,
                "leakage_group": candidate.leakage_group,
                "source_kind": candidate.source_kind,
                "regime_bucket": manifest.get("regime_bucket"),
                "csv_path": str(csv_path),
                "manifest_path": str(manifest_path),
            }
        )

    inventory = {
        "schema_version": TRACE_CORPUS_SCHEMA_VERSION,
        "phase": "4E.2",
        "phase3_root": str(phase3_path),
        "output_root": str(output_path),
        "seed": int(seed),
        "max_total_traces": int(max_total_traces),
        "max_traces_per_dataset": int(max_traces_per_dataset),
        "raw_data_copied": False,
        "dry_run_data_used": False,
        "selected": selected_entries,
        "skipped": skipped,
        "candidate_count_before_cap": len(candidates),
        "selected_count": len(selected_entries),
        "skipped_count": len(skipped),
    }
    summary = _build_summary(
        output_path=output_path,
        candidates=candidates,
        selected=selected,
        skipped=skipped,
        seed=seed,
        max_total_traces=max_total_traces,
        max_traces_per_dataset=max_traces_per_dataset,
    )
    write_json(output_path / "phase4e2_trace_inventory.json", inventory)
    write_json(output_path / "phase4e2_trace_corpus_summary.json", summary)
    return {
        "output_root": str(output_path),
        "normalized_root": str(normalized_out),
        "manifest_root": str(manifests_out),
        "inventory": inventory,
        "summary": summary,
    }


def _collect_candidates(phase3_root: Path) -> Tuple[Tuple[CorpusCandidate, ...], list[Mapping[str, object]]]:
    skipped: list[Mapping[str, object]] = []
    candidates: list[CorpusCandidate] = []

    existing_source_names: set[str] = set()
    normalized_root = phase3_root / "_normalized" / "schema_v1" / "phase3_4a_smoke"
    manifest_root = phase3_root / "_manifests" / "phase3_4a_conversion_smoke"
    if normalized_root.is_dir():
        for csv_path in sorted(normalized_root.rglob("*.csv")):
            candidate = _candidate_from_existing_normalized(csv_path, normalized_root, manifest_root, skipped)
            if candidate is not None:
                candidates.append(candidate)
                _remember_existing_source_names(candidate.manifest, existing_source_names)
    else:
        skipped.append(_skip_entry(normalized_root, "existing_normalized_root_missing", "existing_normalized_csv"))

    expanded_root = phase3_root / "_expanded_phase3_4a"
    if expanded_root.is_dir():
        for raw_path in sorted(path for path in expanded_root.rglob("*") if path.is_file()):
            if _is_forbidden_phase3_source(raw_path):
                skipped.append(_skip_entry(raw_path, "forbidden_phase3_runtime_or_dry_run_source", "expanded_raw"))
                continue
            if raw_path.name.lower() in existing_source_names:
                skipped.append(_skip_entry(raw_path, "already_represented_by_existing_normalized_trace", "expanded_raw"))
                continue
            candidate = _candidate_from_expanded_raw(raw_path, expanded_root, skipped)
            if candidate is not None:
                candidates.append(candidate)
    else:
        skipped.append(_skip_entry(expanded_root, "expanded_raw_root_missing", "expanded_raw"))

    return tuple(candidates), skipped


def _candidate_from_existing_normalized(
    csv_path: Path,
    csv_root: Path,
    manifest_root: Path,
    skipped: list[Mapping[str, object]],
) -> CorpusCandidate | None:
    manifest_path = _matching_manifest(csv_path, csv_root, manifest_root)
    manifest = read_json(manifest_path) if manifest_path is not None else {}
    try:
        trace_id = _text(manifest.get("trace_id")) or csv_path.stem
        trace = load_normalized_trace_csv(csv_path, trace_id=trace_id, strict=True)
    except Exception as exc:  # noqa: BLE001 - inventory needs the safe skip reason.
        skipped.append(_skip_entry(csv_path, "invalid_existing_normalized_trace:{0}".format(exc), "existing_normalized_csv"))
        return None

    rows = _required_rows_from_trace(trace.samples)
    stats = _stats_from_rows(rows)
    dataset_id = _text(manifest.get("dataset_id")) or _text(manifest.get("source_dataset")) or csv_path.parent.name
    leakage_group = _text(manifest.get("leakage_group")) or trace_id
    source_fingerprint = _text(manifest.get("checksum_sha256")) or _fingerprint_file(csv_path)
    merged_manifest = _build_manifest(
        trace_id=trace_id,
        dataset_id=dataset_id,
        leakage_group=leakage_group,
        sample_count=trace.sample_count,
        source_kind="existing_normalized_csv",
        converter=_text(manifest.get("converter")) or _text(manifest.get("converter_name")) or "phase3_normalized_reuse",
        stats=stats,
        source_path=str(csv_path),
        source_fingerprint=source_fingerprint,
        inherited_manifest=manifest,
    )
    return CorpusCandidate(
        trace_id=trace_id,
        dataset_id=dataset_id,
        leakage_group=leakage_group,
        source_kind="existing_normalized_csv",
        converter=str(merged_manifest["converter"]),
        rows=rows,
        manifest=merged_manifest,
        source_path=str(csv_path),
        source_fingerprint=source_fingerprint,
        source_priority=0,
    )


def _candidate_from_expanded_raw(
    raw_path: Path,
    expanded_root: Path,
    skipped: list[Mapping[str, object]],
) -> CorpusCandidate | None:
    try:
        relative = raw_path.relative_to(expanded_root)
    except ValueError:
        relative = raw_path.name
    relative_parts = Path(relative).parts if not isinstance(relative, str) else (relative,)
    dataset_id = relative_parts[0] if relative_parts else raw_path.parent.name

    try:
        rows, metadata = _parse_expanded_raw(raw_path, dataset_id)
        trace = load_normalized_trace_rows(rows, trace_id="<candidate>", source=str(raw_path), strict=True)
    except Exception as exc:  # noqa: BLE001 - unsupported formats are inventory entries.
        skipped.append(_skip_entry(raw_path, "expanded_raw_not_safely_parseable:{0}".format(exc), "expanded_raw"))
        return None

    source_fingerprint = _fingerprint_file(raw_path)
    raw_stem = _slug("_".join(str(part) for part in relative_parts))
    trace_id = "{0}_{1}".format(_slug(dataset_id), raw_stem)
    trace_id = "{0}_{1}".format(trace_id[:180].rstrip("_"), source_fingerprint[:8])
    leakage_group = "{0}:{1}".format(dataset_id, str(Path(relative)).replace("\\", "/"))
    stats = _stats_from_rows(rows)
    manifest = _build_manifest(
        trace_id=trace_id,
        dataset_id=dataset_id,
        leakage_group=leakage_group,
        sample_count=trace.sample_count,
        source_kind="expanded_raw_converted",
        converter=str(metadata["converter"]),
        stats=stats,
        source_path=str(raw_path),
        source_fingerprint=source_fingerprint,
        inherited_manifest=metadata,
    )
    return CorpusCandidate(
        trace_id=trace_id,
        dataset_id=dataset_id,
        leakage_group=leakage_group,
        source_kind="expanded_raw_converted",
        converter=str(manifest["converter"]),
        rows=rows,
        manifest=manifest,
        source_path=str(raw_path),
        source_fingerprint=source_fingerprint,
        source_priority=1,
    )


def _parse_expanded_raw(path: Path, dataset_id: str) -> Tuple[Tuple[Mapping[str, object], ...], Mapping[str, object]]:
    if dataset_id == "ghent_4g_lte_bandwidth_logs" and path.suffix.lower() == ".log":
        return _parse_ghent_log(path)
    if dataset_id == "lancaster_abr_throughput_traces" and path.suffix.lower() == ".txt":
        return _parse_lancaster_txt(path)
    raise TraceCorpusError("unsupported expanded raw format for dataset {0}".format(dataset_id))


def _parse_ghent_log(path: Path) -> Tuple[Tuple[Mapping[str, object], ...], Mapping[str, object]]:
    rows = []
    first_elapsed_ms = None
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            parts = text.split()
            if len(parts) != 6:
                raise TraceCorpusError("line {0}: expected 6 whitespace columns".format(line_number))
            try:
                source_timestamp_ms = float(parts[0])
                elapsed_ms = float(parts[1])
                latitude = float(parts[2])
                longitude = float(parts[3])
                delivered_bytes = float(parts[4])
                interval_ms = float(parts[5])
            except ValueError as exc:
                raise TraceCorpusError("line {0}: non-numeric field".format(line_number)) from exc
            if not all(math.isfinite(value) for value in (source_timestamp_ms, elapsed_ms, latitude, longitude, delivered_bytes, interval_ms)):
                raise TraceCorpusError("line {0}: non-finite field".format(line_number))
            if interval_ms <= 0.0 or delivered_bytes < 0.0:
                raise TraceCorpusError("line {0}: invalid interval or byte count".format(line_number))
            if first_elapsed_ms is None:
                first_elapsed_ms = elapsed_ms
            throughput_kbps = delivered_bytes * 8.0 / interval_ms
            rows.append(
                {
                    "timestamp_s": (elapsed_ms - first_elapsed_ms) / 1000.0,
                    "duration_s": interval_ms / 1000.0,
                    "throughput_kbps": throughput_kbps,
                }
            )
    if len(rows) < 2:
        raise TraceCorpusError("expected at least two samples")
    return tuple(rows), {
        "converter": "phase4e2_ghent_4g_lte_bandwidth_logs_safe_v1",
        "source_dataset": "ghent_4g_lte_bandwidth_logs",
        "network_tags": ["LTE", "4G"],
        "mobility_tags": [_mobility_from_ghent_path(path)],
        "scenario_tags": [path.parent.name],
        "source_file": str(path.name),
        "notes": "Converted from six-column Ghent bandwidth log: bytes per interval_ms to kbps.",
    }


def _parse_lancaster_txt(path: Path) -> Tuple[Tuple[Mapping[str, object], ...], Mapping[str, object]]:
    points = []
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            parts = text.split()
            if len(parts) != 2:
                raise TraceCorpusError("line {0}: expected 2 whitespace columns".format(line_number))
            try:
                timestamp_s = float(parts[0])
                throughput_kbps = float(parts[1])
            except ValueError as exc:
                raise TraceCorpusError("line {0}: non-numeric field".format(line_number)) from exc
            if not math.isfinite(timestamp_s) or not math.isfinite(throughput_kbps):
                raise TraceCorpusError("line {0}: non-finite field".format(line_number))
            if throughput_kbps < 0.0:
                raise TraceCorpusError("line {0}: negative throughput".format(line_number))
            points.append((timestamp_s, throughput_kbps))
    if len(points) < 2:
        raise TraceCorpusError("expected at least two samples")
    points.sort(key=lambda item: item[0])
    deltas = [points[index + 1][0] - points[index][0] for index in range(len(points) - 1)]
    if any(delta <= 0.0 or not math.isfinite(delta) for delta in deltas):
        raise TraceCorpusError("timestamps must be strictly increasing")
    fallback_duration = _median(deltas)
    first_timestamp = points[0][0]
    rows = []
    for index, (timestamp_s, throughput_kbps) in enumerate(points):
        duration_s = deltas[index] if index < len(deltas) else fallback_duration
        rows.append(
            {
                "timestamp_s": timestamp_s - first_timestamp,
                "duration_s": duration_s,
                "throughput_kbps": throughput_kbps,
            }
        )
    return tuple(rows), {
        "converter": "phase4e2_lancaster_abr_throughput_safe_v1",
        "source_dataset": "lancaster_abr_throughput_traces",
        "network_tags": ["HAS", "throughput_trace"],
        "mobility_tags": ["unknown"],
        "scenario_tags": [path.parent.name],
        "source_file": str(path.name),
        "notes": "Converted from timestamp/throughput rows; duration uses next timestamp delta.",
    }


def _select_balanced_candidates(
    candidates: Sequence[CorpusCandidate],
    max_total_traces: int,
    max_traces_per_dataset: int,
    seed: int,
) -> Tuple[CorpusCandidate, ...]:
    by_dataset: dict[str, list[CorpusCandidate]] = {}
    for candidate in candidates:
        by_dataset.setdefault(candidate.dataset_id, []).append(candidate)

    capped_by_dataset: dict[str, list[CorpusCandidate]] = {}
    for dataset_id, dataset_candidates in sorted(by_dataset.items()):
        by_regime: dict[str, list[CorpusCandidate]] = {}
        for candidate in dataset_candidates:
            regime = str(candidate.manifest.get("regime_bucket", "unknown"))
            by_regime.setdefault(regime, []).append(candidate)
        for regime_candidates in by_regime.values():
            regime_candidates.sort(key=lambda item: (item.source_priority, _stable_key(seed, item.trace_id)))

        selected_for_dataset: list[CorpusCandidate] = []
        regime_names = sorted(by_regime)
        while len(selected_for_dataset) < max_traces_per_dataset:
            added = False
            for regime_name in regime_names:
                regime_candidates = by_regime[regime_name]
                if not regime_candidates:
                    continue
                selected_for_dataset.append(regime_candidates.pop(0))
                added = True
                if len(selected_for_dataset) >= max_traces_per_dataset:
                    break
            if not added:
                break
        capped_by_dataset[dataset_id] = selected_for_dataset

    selected: list[CorpusCandidate] = []
    dataset_names = sorted(capped_by_dataset)
    while len(selected) < max_total_traces:
        added = False
        for dataset_id in dataset_names:
            dataset_candidates = capped_by_dataset[dataset_id]
            if not dataset_candidates:
                continue
            selected.append(dataset_candidates.pop(0))
            added = True
            if len(selected) >= max_total_traces:
                break
        if not added:
            break
    return tuple(selected)


def _build_manifest(
    trace_id: str,
    dataset_id: str,
    leakage_group: str,
    sample_count: int,
    source_kind: str,
    converter: str,
    stats: Mapping[str, object],
    source_path: str,
    source_fingerprint: str,
    inherited_manifest: Mapping[str, object],
) -> Mapping[str, object]:
    cv = float(stats.get("coefficient_of_variation") or 0.0)
    mean = float(stats.get("mean_throughput_kbps") or 0.0)
    regime_bucket = _regime_bucket(mean, cv)
    manifest = {
        "schema_version": "phase4e2_trace_manifest_v1",
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "phase": "4E.2",
        "trace_id": trace_id,
        "dataset_id": dataset_id,
        "source_dataset": dataset_id,
        "leakage_group": leakage_group,
        "sample_count": int(sample_count),
        "source_kind": source_kind,
        "converter": converter,
        "converter_name": converter,
        "converter_version_or_commit": "phase4e2_local",
        "mean_throughput_kbps": stats["mean_throughput_kbps"],
        "min_throughput_kbps": stats["min_throughput_kbps"],
        "max_throughput_kbps": stats["max_throughput_kbps"],
        "coefficient_of_variation": cv,
        "throughput_cv": cv,
        "regime_bucket": regime_bucket,
        "checksum_or_source_fingerprint": source_fingerprint,
        "checksum_sha256": source_fingerprint,
        "source_path": source_path,
        "source_file": inherited_manifest.get("source_file") or source_path,
        "source_url_or_reference": inherited_manifest.get("source_url_or_reference") or "Phase 3 local trace material",
        "mobility_tags": inherited_manifest.get("mobility_tags") or [],
        "network_tags": inherited_manifest.get("network_tags") or [],
        "scenario_tags": inherited_manifest.get("scenario_tags") or [],
        "normalized_local_path_policy": "outside repo",
        "raw_local_path_policy": "outside repo",
        "diagnostic_only": True,
        "not_benchmark": True,
        "dry_run_data_used": False,
    }
    for key in ("duration_s", "nominal_granularity_s", "notes", "license", "dataset_card_path"):
        if key in inherited_manifest:
            manifest[key] = inherited_manifest[key]
    return manifest


def _build_summary(
    output_path: Path,
    candidates: Sequence[CorpusCandidate],
    selected: Sequence[CorpusCandidate],
    skipped: Sequence[Mapping[str, object]],
    seed: int,
    max_total_traces: int,
    max_traces_per_dataset: int,
) -> Mapping[str, object]:
    return {
        "schema_version": TRACE_CORPUS_SCHEMA_VERSION,
        "phase": "4E.2",
        "output_root": str(output_path),
        "seed": int(seed),
        "max_total_traces": int(max_total_traces),
        "max_traces_per_dataset": int(max_traces_per_dataset),
        "candidate_count_before_cap": len(candidates),
        "selected_trace_count": len(selected),
        "skipped_count": len(skipped),
        "dataset_id_counts": _counts(candidate.dataset_id for candidate in selected),
        "regime_bucket_counts": _counts(str(candidate.manifest.get("regime_bucket", "unknown")) for candidate in selected),
        "source_kind_counts": _counts(candidate.source_kind for candidate in selected),
        "dataset_id_family_count": len(set(candidate.dataset_id for candidate in selected)),
        "regime_bucket_count": len(set(str(candidate.manifest.get("regime_bucket", "unknown")) for candidate in selected)),
        "raw_data_copied": False,
        "dry_run_data_used": False,
        "claim_boundary": "diagnostic corpus preparation only; not a formal benchmark",
    }


def _write_normalized_csv(path: Path, rows: Sequence[Mapping[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(REQUIRED_TRACE_COLUMNS))
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "timestamp_s": _format_float(row["timestamp_s"]),
                    "duration_s": _format_float(row["duration_s"]),
                    "throughput_kbps": _format_float(row["throughput_kbps"]),
                }
            )


def _required_rows_from_trace(samples) -> Tuple[Mapping[str, object], ...]:
    return tuple(
        {
            "timestamp_s": sample.timestamp_s,
            "duration_s": sample.duration_s,
            "throughput_kbps": sample.throughput_kbps,
        }
        for sample in samples
    )


def _stats_from_rows(rows: Sequence[Mapping[str, object]]) -> Mapping[str, object]:
    throughputs = [float(row["throughput_kbps"]) for row in rows]
    mean = sum(throughputs) / float(len(throughputs)) if throughputs else 0.0
    variance = sum((value - mean) * (value - mean) for value in throughputs) / float(len(throughputs)) if throughputs else 0.0
    stdev = math.sqrt(max(variance, 0.0))
    return {
        "mean_throughput_kbps": mean,
        "min_throughput_kbps": min(throughputs) if throughputs else 0.0,
        "max_throughput_kbps": max(throughputs) if throughputs else 0.0,
        "coefficient_of_variation": (stdev / mean) if mean > 0.0 else 0.0,
    }


def _regime_bucket(mean_throughput_kbps: float, coefficient_of_variation: float) -> str:
    if mean_throughput_kbps < 1000.0:
        level = "low"
    elif mean_throughput_kbps < 3000.0:
        level = "mid"
    elif mean_throughput_kbps < 10000.0:
        level = "high"
    else:
        level = "very_high"

    if coefficient_of_variation >= 0.75:
        stability = "variable"
    elif coefficient_of_variation <= 0.15:
        stability = "stable"
    else:
        stability = "mixed"
    return "{0}_{1}".format(level, stability)


def _matching_manifest(csv_path: Path, csv_root: Path, manifest_root: Path) -> Path | None:
    if not manifest_root.is_dir():
        return None
    relative_candidate = manifest_root / csv_path.relative_to(csv_root).with_suffix(".json")
    if relative_candidate.is_file():
        return relative_candidate
    by_stem = tuple(manifest_root.rglob(csv_path.with_suffix(".json").name))
    return by_stem[0] if by_stem else None


def _remember_existing_source_names(manifest: Mapping[str, object], names: set[str]) -> None:
    for key in ("source_path", "source_file"):
        value = _text(manifest.get(key))
        if value:
            names.add(Path(value.replace("::", "/")).name.lower())


def _is_forbidden_phase3_source(path: Path) -> bool:
    text = str(path).lower().replace("\\", "/")
    forbidden_parts = ("/_runs/", "dry_run", "dry-run", "controller_runtime", "benchmark", "smoke_qoe")
    return any(part in text for part in forbidden_parts)


def _skip_entry(path: object, reason: str, source_kind: str) -> Mapping[str, object]:
    return {
        "path": str(path),
        "reason": reason,
        "source_kind": source_kind,
    }


def _fingerprint_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _stable_key(seed: int, text: str) -> str:
    return hashlib.sha256("{0}:{1}".format(seed, text).encode("utf-8")).hexdigest()


def _counts(values: Iterable[str]) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[str(value)] = counts.get(str(value), 0) + 1
    return dict(sorted(counts.items()))


def _format_float(value: object) -> str:
    return "{0:.9g}".format(float(value))


def _median(values: Sequence[float]) -> float:
    ordered = sorted(values)
    midpoint = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[midpoint]
    return (ordered[midpoint - 1] + ordered[midpoint]) / 2.0


def _mobility_from_ghent_path(path: Path) -> str:
    match = re.search(r"report_([a-zA-Z]+)_", path.name)
    if match:
        return match.group(1).lower()
    parent = path.parent.name.lower()
    if parent.startswith("logs_"):
        return parent[5:]
    return "unknown"


def _slug(value: object) -> str:
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(value).strip())
    text = text.strip("._")
    return text or "trace"


def _text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()
