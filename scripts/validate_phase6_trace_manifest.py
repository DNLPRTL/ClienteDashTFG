from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


OUTPUT_SCHEMA_VERSION = "phase6_trace_manifest_validation_v1"
MANIFEST_SCHEMA_VERSION = "phase6_trace_manifest_v1"
TRACE_SCHEMA_VERSION = "normalized_trace_schema_v1"

MISSING = "unspecified"
PHASE6_EVAL_SPLITS = frozenset(
    (
        "validation",
        "val",
        "test",
        "ood",
        "eval",
        "same_family_clean",
        "ood_final",
        "primary_eval",
        "phase6_eval",
    )
)
PHASE6_EVAL_SPLIT_TOKENS = frozenset(("validation", "val", "test", "ood", "eval"))
NON_EVAL_SPLITS = frozenset(("diagnostic_only", "do_not_use_for_eval"))

EVAL_GATE_ALIASES = ("eval_gate", "row_eval_gate", "session_eval_gate", "use_for_eval", "eligibility_gate")
CHECKSUM_ALIASES = (
    "checksum_sha256",
    "sha256",
    "checksum",
    "trace_checksum",
    "checksum_or_source_fingerprint",
)
FINGERPRINT_ALIASES = (
    "canonical_content_fingerprint",
    "content_fingerprint",
    "content_sha256",
    "canonical_sha256",
    "trace_content_fingerprint",
)
SOURCE_ALIASES = (
    "trace_csv",
    "source_path",
    "source_file",
    "relative_path",
    "path",
    "split_key",
    "manifest_path",
    "source_url_or_reference",
)
SCHEMA_NOTE_ALIASES = ("schema_version_note", "schema_documentation", "schema_version_documentation", "schema_note")
DUPLICATE_FIELDS = (
    ("trace_id", "duplicate_ids"),
    ("checksum_sha256", "duplicate_checksums"),
    ("canonical_content_fingerprint", "duplicate_fingerprints"),
    ("leakage_group", "duplicate_leakage_groups"),
)


@dataclass(frozen=True)
class ManifestRecord:
    record_index: int
    trace_id: str
    dataset_family: str
    split: str
    eval_gate: str
    eval_gate_present: bool
    source_ref: str
    schema_version: str
    checksum_sha256: str
    canonical_content_fingerprint: str
    leakage_group: str
    duration_s: str
    sample_count: str
    license_status: str
    exclusion_reason: str
    schema_note: str


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Phase 6 trace manifest without running benchmark code.")
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strict-final", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = validate_manifest(args.manifest, strict_final=args.strict_final)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        print("unexpected validation failure: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6_trace_manifest_validation: {0}".format("PASS" if report["valid"] else "ERRORS"))
    print("output: {0}".format(args.output))
    if args.fail_on_error and report["errors"]:
        return 2
    return 0


def validate_manifest(manifest_path: Path, *, strict_final: bool = False) -> Dict[str, Any]:
    data = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    top_schema_version = normalized_value(data.get("schema_version")) if isinstance(data, Mapping) else ""
    raw_records = list(iter_raw_records(data))
    records = [record_from_raw(index, raw, default_split) for index, (raw, default_split) in enumerate(raw_records)]

    errors: List[str] = []
    warnings: List[str] = []
    missing_required_fields: List[Dict[str, Any]] = []

    if isinstance(data, Mapping):
        if top_schema_version and top_schema_version != MANIFEST_SCHEMA_VERSION:
            warnings.append(
                "manifest schema_version is {0}; expected {1}.".format(
                    top_schema_version,
                    MANIFEST_SCHEMA_VERSION,
                )
            )
        if not top_schema_version:
            warnings.append("manifest schema_version is missing; expected phase6_trace_manifest_v1.")
    else:
        warnings.append("manifest uses a list root; phase6_trace_manifest_v1 mapping root is preferred.")

    eval_records = [record for record in records if is_phase6_eval_record(record)]
    non_eval_records = [record for record in records if not is_phase6_eval_record(record)]

    for record in records:
        if strict_final and is_phase6_eval_record(record):
            validate_strict_eval_record(record, errors, missing_required_fields)
        validate_numeric_fields(record, errors if is_phase6_eval_record(record) else warnings, strict_final=strict_final)
        if not is_phase6_eval_record(record):
            validate_non_eval_record(record, warnings)

    duplicate_reports = build_duplicate_reports(eval_records)
    if strict_final:
        for field, category in DUPLICATE_FIELDS:
            for group in duplicate_reports[category]:
                errors.append(
                    "duplicate {0} among use_for_eval records: {1}.".format(
                        field,
                        group["value"],
                    )
                )

    counts = {
        "records": len(records),
        "eval_records": len(eval_records),
        "non_eval_records": len(non_eval_records),
        "errors": len(errors),
        "warnings": len(warnings),
        "missing_required_fields": len(missing_required_fields),
        "duplicate_ids": len(duplicate_reports["duplicate_ids"]),
        "duplicate_checksums": len(duplicate_reports["duplicate_checksums"]),
        "duplicate_fingerprints": len(duplicate_reports["duplicate_fingerprints"]),
        "duplicate_leakage_groups": len(duplicate_reports["duplicate_leakage_groups"]),
    }

    return {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "manifest": str(manifest_path),
        "strict_final": bool(strict_final),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": counts,
        "split_counts": count_values(records, "split"),
        "gate_counts": gate_counts(records),
        "dataset_family_counts": count_values(records, "dataset_family"),
        "missing_required_fields": missing_required_fields,
        "duplicate_ids": duplicate_reports["duplicate_ids"],
        "duplicate_checksums": duplicate_reports["duplicate_checksums"],
        "duplicate_fingerprints": duplicate_reports["duplicate_fingerprints"],
        "duplicate_leakage_groups": duplicate_reports["duplicate_leakage_groups"],
        "non_eval_records": [public_record(record) for record in non_eval_records],
        "eval_records": [public_record(record) for record in eval_records],
    }


def record_from_raw(index: int, raw: Mapping[str, Any], default_split: Optional[str]) -> ManifestRecord:
    split = normalized_value(first_value(raw, ("split", "phase", "dataset_split")) or default_split or "")
    return ManifestRecord(
        record_index=index,
        trace_id=normalized_value(first_value(raw, ("trace_id", "id", "trace_name", "name"))),
        dataset_family=normalized_value(first_value(raw, ("dataset_family", "family", "dataset", "dataset_name"))),
        split=split,
        eval_gate=normalized_eval_gate(first_value(raw, EVAL_GATE_ALIASES, include_empty=True)),
        eval_gate_present=any(key in raw for key in EVAL_GATE_ALIASES),
        source_ref=normalized_path(first_value(raw, SOURCE_ALIASES)),
        schema_version=normalized_value(first_value(raw, ("schema_version", "trace_schema_version"))),
        checksum_sha256=normalized_checksum(first_value(raw, CHECKSUM_ALIASES)),
        canonical_content_fingerprint=normalized_checksum(first_value(raw, FINGERPRINT_ALIASES)),
        leakage_group=normalized_value(first_value(raw, ("leakage_group", "leakage_id", "source_group"))),
        duration_s=normalized_value(first_value(raw, ("duration_s", "duration_seconds"))),
        sample_count=normalized_value(first_value(raw, ("sample_count", "samples", "num_samples"))),
        license_status=normalized_value(first_value(raw, ("license_status", "license", "license_gate"))),
        exclusion_reason=normalized_value(first_value(raw, ("exclusion_reason", "exclude_reason", "gate_reason"))),
        schema_note=normalized_value(first_value(raw, SCHEMA_NOTE_ALIASES)),
    )


def validate_strict_eval_record(
    record: ManifestRecord,
    errors: List[str],
    missing_required_fields: List[Dict[str, Any]],
) -> None:
    required = (
        ("trace_id", record.trace_id),
        ("dataset_family", record.dataset_family),
        ("split", record.split),
        ("eval_gate", record.eval_gate if record.eval_gate_present else ""),
        ("trace_csv_or_source_path", record.source_ref),
        ("checksum_sha256", record.checksum_sha256),
        ("canonical_content_fingerprint", record.canonical_content_fingerprint),
        ("leakage_group", record.leakage_group),
        ("schema_version", record.schema_version),
    )
    for field, value in required:
        if not value:
            missing_required_fields.append({"record_index": record.record_index, "field": field})
            errors.append("record {0} missing required field {1}.".format(record.record_index, field))

    if record.eval_gate != "use_for_eval":
        errors.append("record {0} eval_gate must be use_for_eval in strict-final mode.".format(record.record_index))

    if record.schema_version and record.schema_version != TRACE_SCHEMA_VERSION and not record.schema_note:
        errors.append(
            "record {0} schema_version is {1}; expected {2} or an explicit schema note.".format(
                record.record_index,
                record.schema_version,
                TRACE_SCHEMA_VERSION,
            )
        )

    if record.exclusion_reason:
        errors.append("record {0} use_for_eval has non-empty exclusion_reason.".format(record.record_index))


def validate_non_eval_record(record: ManifestRecord, warnings: List[str]) -> None:
    if record.eval_gate == "do_not_use_for_eval" and not record.exclusion_reason:
        warnings.append("record {0} do_not_use_for_eval should include exclusion_reason.".format(record.record_index))
    if not record.trace_id and not record.source_ref and not record.checksum_sha256 and not record.canonical_content_fingerprint:
        warnings.append("record {0} non-eval record lacks traceability identity fields.".format(record.record_index))


def validate_numeric_fields(record: ManifestRecord, messages: List[str], *, strict_final: bool) -> None:
    if record.duration_s and not is_positive_number(record.duration_s):
        level = "record {0} duration_s must be positive when present.".format(record.record_index)
        messages.append(level)
    if record.sample_count and not is_positive_number(record.sample_count):
        level = "record {0} sample_count must be positive when present.".format(record.record_index)
        messages.append(level)


def build_duplicate_reports(records: Sequence[ManifestRecord]) -> Dict[str, List[Dict[str, Any]]]:
    return {
        category: duplicate_groups(records, field)
        for field, category in DUPLICATE_FIELDS
    }


def duplicate_groups(records: Sequence[ManifestRecord], field: str) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[ManifestRecord]] = defaultdict(list)
    for record in records:
        value = getattr(record, field)
        if value:
            grouped[value].append(record)

    groups = []
    for value, grouped_records in sorted(grouped.items()):
        if len(grouped_records) > 1:
            groups.append(
                {
                    "value": value,
                    "records": [public_record(record) for record in grouped_records],
                }
            )
    return groups


def iter_raw_records(data: Any, default_split: Optional[str] = None) -> Iterable[Tuple[Mapping[str, Any], Optional[str]]]:
    if isinstance(data, list):
        for item in data:
            if isinstance(item, Mapping):
                yield item, default_split
        return

    if not isinstance(data, Mapping):
        return

    for key in ("trace_records", "records", "traces", "items"):
        value = data.get(key)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, Mapping):
                    yield item, default_split
            return

    splits = data.get("splits")
    if isinstance(splits, Mapping):
        for split_name, split_value in splits.items():
            if isinstance(split_value, list):
                for item in split_value:
                    if isinstance(item, Mapping):
                        yield item, str(split_name)
            elif isinstance(split_value, Mapping):
                for key in ("trace_records", "records", "traces", "items"):
                    nested = split_value.get(key)
                    if isinstance(nested, list):
                        for item in nested:
                            if isinstance(item, Mapping):
                                yield item, str(split_name)


def first_value(raw: Mapping[str, Any], keys: Sequence[str], *, include_empty: bool = False) -> Optional[Any]:
    for key in keys:
        if key not in raw:
            continue
        value = raw.get(key)
        if include_empty or value not in (None, ""):
            return value
    return None


def normalized_checksum(value: Optional[Any]) -> str:
    return normalized_value(value).lower()


def normalized_value(value: Optional[Any]) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple)):
        return ",".join(str(item) for item in value)
    return str(value).strip()


def normalized_path(value: Optional[Any]) -> str:
    return normalized_value(value).replace("\\", "/")


def normalized_eval_gate(value: Optional[Any]) -> str:
    raw = normalized_value(value).lower()
    if raw in ("use_for_eval", "use", "eval", "true", "yes", "1"):
        return "use_for_eval"
    if raw in ("diagnostic_only", "diagnostic", "diag"):
        return "diagnostic_only"
    if raw in ("do_not_use_for_eval", "do-not-use-for-eval", "excluded", "exclude", "false", "no", "0"):
        return "do_not_use_for_eval"
    return raw


def is_phase6_eval_record(record: ManifestRecord) -> bool:
    if record.eval_gate == "use_for_eval":
        return True
    if record.eval_gate in ("diagnostic_only", "do_not_use_for_eval"):
        return False
    return is_phase6_eval_split(record.split)


def is_phase6_eval_split(split: str) -> bool:
    normalized = normalized_split_name(split)
    if normalized in ("", MISSING):
        return True
    if normalized in NON_EVAL_SPLITS:
        return False
    if normalized in PHASE6_EVAL_SPLITS:
        return True
    tokens = set(re.split(r"[^a-z0-9]+", normalized))
    return bool(tokens & PHASE6_EVAL_SPLIT_TOKENS)


def normalized_split_name(split: str) -> str:
    return normalized_value(split).lower().replace("-", "_").replace(" ", "_")


def is_positive_number(value: str) -> bool:
    try:
        return float(value) > 0
    except ValueError:
        return False


def count_values(records: Sequence[ManifestRecord], field: str) -> Dict[str, int]:
    counts: Counter[str] = Counter(getattr(record, field) or MISSING for record in records)
    return dict(sorted(counts.items()))


def gate_counts(records: Sequence[ManifestRecord]) -> Dict[str, int]:
    counts: Counter[str] = Counter(record.eval_gate or MISSING for record in records)
    return dict(sorted(counts.items()))


def public_record(record: ManifestRecord) -> Dict[str, Any]:
    data = asdict(record)
    return {key: value for key, value in data.items() if value not in ("", None, False)}


if __name__ == "__main__":
    sys.exit(main())
