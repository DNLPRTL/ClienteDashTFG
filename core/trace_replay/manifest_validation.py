from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Mapping

from core.trace_replay.converters.common import sha256_file
from core.trace_replay.validation import validate_normalized_trace_csv


class Phase3ManifestValidationError(ValueError):
    """Raised when a Phase 3 final trace manifest is not closure-valid."""


REQUIRED_MANIFEST_FIELDS = (
    "schema_id",
    "phase",
    "artifact_set",
    "normalized_schema_id",
    "split_strategy",
    "ready_for_benchmark",
    "benchmark_authorized",
    "outputs_are_benchmark_results",
    "trace_count",
    "split_counts",
    "semantics_counts",
    "traces",
)

REQUIRED_TRACE_FIELDS = (
    "trace_id",
    "dataset_id",
    "converter_id",
    "normalized_trace_path",
    "metadata_path",
    "source_path",
    "source_sha256",
    "group_id",
    "leakage_group",
    "semantics",
    "split",
    "row_count",
    "duration_s",
    "throughput_min_kbps",
    "throughput_mean_kbps",
    "throughput_max_kbps",
    "content_fingerprint_sha256",
)


def validate_phase3_trace_manifest_data(
    manifest: Mapping[str, object],
    verify_source_hash: bool = False,
) -> dict[str, object]:
    _require_fields(manifest, REQUIRED_MANIFEST_FIELDS, "manifest")
    if manifest["schema_id"] != "phase3_trace_manifest_final_v1":
        raise Phase3ManifestValidationError("unexpected schema_id: {0}".format(manifest["schema_id"]))
    if manifest["phase"] != "phase3_rebuild":
        raise Phase3ManifestValidationError("unexpected phase: {0}".format(manifest["phase"]))
    if manifest["normalized_schema_id"] != "normalized_trace_schema_v1":
        raise Phase3ManifestValidationError("unexpected normalized_schema_id: {0}".format(manifest["normalized_schema_id"]))
    for flag in ("ready_for_benchmark", "benchmark_authorized", "outputs_are_benchmark_results"):
        if manifest.get(flag) is not False:
            raise Phase3ManifestValidationError("{0} must be false".format(flag))

    traces = manifest.get("traces")
    if not isinstance(traces, list):
        raise Phase3ManifestValidationError("traces must be a list")
    if int(manifest["trace_count"]) != len(traces):
        raise Phase3ManifestValidationError("trace_count does not match traces length")

    split_by_group: dict[str, str] = {}
    split_counter: Counter[str] = Counter()
    semantics_counter: Counter[str] = Counter()
    seen_trace_ids: set[str] = set()
    seen_source_fingerprints: dict[str, str] = {}

    for index, trace in enumerate(traces):
        if not isinstance(trace, Mapping):
            raise Phase3ManifestValidationError("trace {0} must be an object".format(index))
        _require_fields(trace, REQUIRED_TRACE_FIELDS, "trace {0}".format(index))

        trace_id = str(trace["trace_id"])
        if trace_id in seen_trace_ids:
            raise Phase3ManifestValidationError("duplicate trace_id: {0}".format(trace_id))
        seen_trace_ids.add(trace_id)

        split = str(trace["split"])
        if split not in {"train", "test", "eval"}:
            raise Phase3ManifestValidationError("{0}: invalid split {1}".format(trace_id, split))
        group = str(trace["leakage_group"])
        previous_split = split_by_group.get(group)
        if previous_split is not None and previous_split != split:
            raise Phase3ManifestValidationError("{0}: leakage_group spans splits".format(group))
        split_by_group[group] = split

        duplicate_key = "{0}|{1}".format(trace["source_sha256"], trace["content_fingerprint_sha256"])
        previous_trace = seen_source_fingerprints.get(duplicate_key)
        if previous_trace is not None:
            raise Phase3ManifestValidationError(
                "{0}: duplicate source hash and normalized fingerprint with {1}".format(trace_id, previous_trace)
            )
        seen_source_fingerprints[duplicate_key] = trace_id

        try:
            stats = validate_normalized_trace_csv(trace["normalized_trace_path"])
        except OSError as exc:
            raise Phase3ManifestValidationError("{0}: normalized_trace_path missing".format(trace_id)) from exc
        if stats.content_fingerprint_sha256 != trace["content_fingerprint_sha256"]:
            raise Phase3ManifestValidationError("{0}: content_fingerprint_sha256 mismatch".format(trace_id))
        if stats.row_count != int(trace["row_count"]):
            raise Phase3ManifestValidationError("{0}: row_count mismatch".format(trace_id))
        _assert_close(trace_id, "duration_s", stats.duration_s, float(trace["duration_s"]))
        _assert_close(trace_id, "throughput_min_kbps", stats.throughput_min_kbps, float(trace["throughput_min_kbps"]))
        _assert_close(trace_id, "throughput_mean_kbps", stats.throughput_mean_kbps, float(trace["throughput_mean_kbps"]))
        _assert_close(trace_id, "throughput_max_kbps", stats.throughput_max_kbps, float(trace["throughput_max_kbps"]))

        if not Path(str(trace["metadata_path"])).is_file():
            raise Phase3ManifestValidationError("{0}: metadata_path missing".format(trace_id))
        if verify_source_hash:
            _verify_source_hash(trace_id, str(trace["source_path"]), str(trace["source_sha256"]))

        split_counter[split] += 1
        semantics_counter[str(trace["semantics"])] += 1

    expected_split_counts = {name: split_counter.get(name, 0) for name in ("train", "test", "eval")}
    if dict(manifest["split_counts"]) != expected_split_counts:
        raise Phase3ManifestValidationError("split_counts mismatch")
    if dict(manifest["semantics_counts"]) != dict(sorted(semantics_counter.items())):
        raise Phase3ManifestValidationError("semantics_counts mismatch")

    return {
        "schema_id": manifest["schema_id"],
        "artifact_set": manifest["artifact_set"],
        "trace_count": len(traces),
        "split_counts": expected_split_counts,
        "semantics_counts": dict(sorted(semantics_counter.items())),
        "ready_for_benchmark": manifest["ready_for_benchmark"],
        "benchmark_authorized": manifest["benchmark_authorized"],
    }


def validate_phase3_trace_manifest_file(path: str | Path, verify_source_hash: bool = False) -> dict[str, object]:
    import json

    manifest_path = Path(path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    summary = validate_phase3_trace_manifest_data(manifest, verify_source_hash=verify_source_hash)
    summary["manifest_path"] = str(manifest_path)
    return summary


def _require_fields(mapping: Mapping[str, object], fields: tuple[str, ...], label: str) -> None:
    missing = [field for field in fields if field not in mapping]
    if missing:
        raise Phase3ManifestValidationError("{0}: missing fields {1}".format(label, ", ".join(missing)))


def _assert_close(trace_id: str, field: str, actual: float, expected: float) -> None:
    if abs(actual - expected) > 1e-6:
        raise Phase3ManifestValidationError("{0}: {1} mismatch".format(trace_id, field))


def _verify_source_hash(trace_id: str, source_path: str, expected_hash: str) -> None:
    source_parts = source_path.split(";")
    expected_parts = expected_hash.split("+")
    if len(source_parts) != len(expected_parts):
        raise Phase3ManifestValidationError("{0}: source hash shape mismatch".format(trace_id))
    actual_parts = []
    for source in source_parts:
        path = Path(source)
        if not path.is_file():
            raise Phase3ManifestValidationError("{0}: source_path missing: {1}".format(trace_id, path))
        actual_parts.append(sha256_file(path))
    actual_hash = "+".join(actual_parts)
    if actual_hash != expected_hash:
        raise Phase3ManifestValidationError("{0}: source_sha256 mismatch".format(trace_id))
