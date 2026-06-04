from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

try:
    from scripts.phase6c_source_registry import Phase6CError, read_json, utc_now, write_json
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import Phase6CError, read_json, utc_now, write_json


OUTPUT_SCHEMA_VERSION = "phase6_trace_manifest_v1"
EXPECTED_PHASE4_COUNT = 210
FINGERPRINT_ALIASES = (
    "canonical_content_fingerprint",
    "content_fingerprint",
    "content_sha256",
    "canonical_sha256",
    "trace_content_fingerprint",
)
CHECKSUM_ALIASES = (
    "checksum_sha256",
    "sha256",
    "checksum",
    "trace_checksum",
    "checksum_or_source_fingerprint",
)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Build the Phase 4 leakage reference manifest for Phase 6 audit.")
    parser.add_argument("--phase4-dataset-manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-nonstandard-count", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = build_reference_manifest(
            phase4_dataset_manifest=args.phase4_dataset_manifest,
            output=args.output,
            strict=args.strict,
            allow_nonstandard_count=args.allow_nonstandard_count,
        )
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6_reference_manifest: {0}".format("PASS" if report["valid"] else "WARN_OR_FAIL"))
    print("output: {0}".format(args.output))
    return 0 if report["valid"] else 2


def build_reference_manifest(
    *,
    phase4_dataset_manifest: Path,
    output: Path,
    strict: bool = False,
    allow_nonstandard_count: bool = False,
) -> Dict[str, Any]:
    data = read_json(phase4_dataset_manifest)
    errors: List[str] = []
    warnings: List[str] = []
    if strict and (not isinstance(data, Mapping) or "trace_records" not in data):
        raise Phase6CError("strict mode requires phase4 manifest to contain trace_records")

    raw_records = list(iter_raw_records(data))
    if strict and len(raw_records) != EXPECTED_PHASE4_COUNT and not allow_nonstandard_count:
        errors.append(
            "expected {0} Phase 4 records, found {1}; pass --allow-nonstandard-count to allow synthetic/nonstandard manifests".format(
                EXPECTED_PHASE4_COUNT,
                len(raw_records),
            )
        )

    records = []
    for index, (raw, default_split) in enumerate(raw_records):
        if not isinstance(raw, Mapping):
            continue
        checksum = normalized_checksum(first_value(raw, CHECKSUM_ALIASES))
        fingerprint = normalized_checksum(first_value(raw, FINGERPRINT_ALIASES))
        notes = []
        if not fingerprint and checksum:
            fingerprint = checksum
            notes.append("canonical_content_fingerprint_inferred_from_checksum_sha256")
        if strict and not checksum:
            errors.append("record {0} missing checksum_sha256".format(index))
        record = {
            "trace_id": normalized_value(first_value(raw, ("trace_id", "id", "trace_name", "name"))),
            "dataset_family": normalized_value(first_value(raw, ("dataset_family", "family", "dataset", "dataset_name", "source_dataset"))),
            "source_dataset": normalized_value(first_value(raw, ("source_dataset", "dataset_family", "dataset", "dataset_name"))),
            "split": normalized_value(first_value(raw, ("split", "phase", "dataset_split")) or default_split or ""),
            "eval_gate": "diagnostic_only",
            "role": "phase4_training_reference",
            "checksum_sha256": checksum,
            "canonical_content_fingerprint": fingerprint,
            "leakage_group": normalized_value(first_value(raw, ("leakage_group", "leakage_id", "source_group"))),
            "source_path": normalized_value(first_value(raw, ("source_path", "source_file", "relative_path", "path", "split_key", "manifest_path"))),
            "sample_count": normalized_value(first_value(raw, ("sample_count", "samples", "num_samples"))),
            "duration_s": normalized_value(first_value(raw, ("duration_s", "duration_seconds"))),
            "phase4_split": normalized_value(first_value(raw, ("split", "phase", "dataset_split")) or default_split or ""),
            "phase4_dataset_manifest": str(phase4_dataset_manifest),
            "used_by_neural_abr_lite_training_reference": True,
            "exclusion_reason": "phase4_training_reference_not_phase6_eval",
        }
        if notes:
            record["notes"] = notes
            warnings.extend("record {0}: {1}".format(index, note) for note in notes)
        records.append({key: value for key, value in record.items() if value not in ("", None)})

    manifest = {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "manifest_role": "phase4_training_reference",
        "generated_at": utc_now(),
        "phase4_dataset_manifest": str(phase4_dataset_manifest),
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "trace_records": records,
        "counts": {
            "records": len(records),
            "expected_phase4_records": EXPECTED_PHASE4_COUNT,
        },
        "warnings": warnings,
    }
    if errors:
        manifest["errors"] = errors
    write_json(output, manifest)
    return {
        "valid": not errors,
        "records": records,
        "errors": errors,
        "warnings": warnings,
        "output": str(output),
    }


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


def first_value(raw: Mapping[str, Any], keys: Sequence[str]) -> Optional[Any]:
    for key in keys:
        value = raw.get(key)
        if value not in (None, ""):
            return value
    return None


def normalized_checksum(value: Optional[Any]) -> str:
    return normalized_value(value).lower()


def normalized_value(value: Optional[Any]) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ",".join(str(item) for item in value)
    return str(value).strip()


if __name__ == "__main__":
    sys.exit(main())
