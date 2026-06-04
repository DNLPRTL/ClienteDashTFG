from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        read_json,
        sources_by_id,
        utc_now,
        write_json,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        read_json,
        sources_by_id,
        utc_now,
        write_json,
    )


OUTPUT_SCHEMA_VERSION = "phase6_trace_manifest_v1"
TRACE_SCHEMA_VERSION = "normalized_trace_schema_v1"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Build the Phase 6 candidate trace manifest from normalized outputs.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--include-diagnostic", action="store_true", help="Accepted for compatibility; diagnostics are included by default.")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        report = build_candidate_manifest(
            external_root=args.external_root,
            output=args.output,
            registry_path=args.source_registry,
            strict=args.strict,
            include_diagnostic=True,
            allow_repo_output=args.allow_repo_output,
        )
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6_candidate_manifest: {0}".format("PASS" if report["valid"] else "WARN_OR_FAIL"))
    print("output: {0}".format(args.output))
    return 0 if report["valid"] else 2


def build_candidate_manifest(
    *,
    external_root: Path,
    output: Path,
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    strict: bool = False,
    include_diagnostic: bool = True,
    allow_repo_output: bool = False,
) -> Dict[str, Any]:
    paths = create_external_layout(external_root, allow_repo_output=allow_repo_output)
    registry = load_source_registry(registry_path)
    source_map = sources_by_id(registry)
    records: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []

    for metadata_path in sorted((paths["manifests"] / "per_trace").rglob("*.json")):
        metadata = read_json(metadata_path)
        if metadata.get("dataset_family") == "lancaster_abr_throughput_traces" and metadata.get("eval_gate") == "use_for_eval":
            errors.append("Lancaster must not appear as use_for_eval in Phase 6C.")
        record = candidate_record_from_metadata(metadata, source_map)
        if record["eval_gate"] != "use_for_eval" and not include_diagnostic:
            continue
        if record.get("dataset_family") == "lancaster_abr_throughput_traces" and record.get("eval_gate") == "use_for_eval":
            errors.append("Lancaster must not appear as use_for_eval in Phase 6C.")
        records.append(record)

    use_for_eval = [record for record in records if record.get("eval_gate") == "use_for_eval"]
    raca_eval = [record for record in use_for_eval if record.get("dataset_family") in ("raca_4g_lte", "raca_5g")]
    if not any(record.get("dataset_family") == "lumos5g" for record in records):
        warnings.append("lumos5g_absent_or_not_normalized")
    if strict and not use_for_eval:
        errors.append("strict mode requires at least one primary OOD use_for_eval trace.")
    if strict and not raca_eval:
        errors.append("strict mode requires at least one Raca 4G or Raca 5G use_for_eval trace.")

    for record in use_for_eval:
        for field in ("checksum_sha256", "canonical_content_fingerprint", "leakage_group"):
            if not record.get(field):
                errors.append("use_for_eval trace {0} missing {1}.".format(record.get("trace_id", "<unknown>"), field))

    duplicate_fingerprints = duplicate_values(use_for_eval, "canonical_content_fingerprint")
    for fingerprint, grouped in duplicate_fingerprints.items():
        errors.append(
            "duplicate canonical_content_fingerprint among use_for_eval records: {0} ({1})".format(
                fingerprint,
                ", ".join(record.get("trace_id", "") for record in grouped),
            )
        )

    manifest = {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "manifest_role": "phase6_candidate_trace_manifest",
        "generated_at": utc_now(),
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6c_materialization_only": True,
        "trace_records": records,
        "counts": {
            "records": len(records),
            "use_for_eval": len(use_for_eval),
            "diagnostic_only": sum(1 for record in records if record.get("eval_gate") == "diagnostic_only"),
            "do_not_use_for_eval": sum(1 for record in records if record.get("eval_gate") == "do_not_use_for_eval"),
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


def candidate_record_from_metadata(metadata: Mapping[str, Any], source_map: Mapping[str, Mapping[str, Any]]) -> Dict[str, Any]:
    source_id = str(metadata.get("source_id") or metadata.get("dataset_family") or "")
    source = source_map.get(source_id, {})
    dataset_family = str(metadata.get("dataset_family") or source.get("dataset_family") or source_id)
    split = str(metadata.get("split") or source.get("split") or "")
    eval_gate = str(metadata.get("eval_gate") or source.get("eval_gate") or "")
    if dataset_family in ("ghent_4g_lte", "hsdpa_norway") and eval_gate == "use_for_eval":
        eval_gate = "diagnostic_only"
        split = split or "same_family_candidate"
    if dataset_family == "lancaster_abr_throughput_traces":
        eval_gate = "do_not_use_for_eval"
        split = "excluded"
    record = {
        "trace_id": metadata.get("trace_id", ""),
        "dataset_family": dataset_family,
        "source_dataset": metadata.get("source_dataset") or source.get("source_dataset") or dataset_family,
        "split": split,
        "eval_gate": eval_gate,
        "trace_csv": metadata.get("trace_csv", ""),
        "source_file": metadata.get("source_file", ""),
        "schema_version": metadata.get("schema_version", TRACE_SCHEMA_VERSION),
        "checksum_sha256": metadata.get("checksum_sha256", ""),
        "canonical_content_fingerprint": metadata.get("canonical_content_fingerprint", ""),
        "leakage_group": metadata.get("leakage_group", ""),
        "duration_s": metadata.get("duration_s", ""),
        "sample_count": metadata.get("sample_count", ""),
        "license_status": metadata.get("license_status") or source.get("license_status", ""),
        "acquisition_status": metadata.get("acquisition_status", "acquired"),
        "normalization_status": metadata.get("normalization_status", "normalized"),
        "exclusion_reason": metadata.get("exclusion_reason", ""),
    }
    if record["eval_gate"] == "diagnostic_only" and not record["exclusion_reason"]:
        record["exclusion_reason"] = "same_family_diagnostic_not_primary_eval"
    if record["eval_gate"] == "do_not_use_for_eval" and not record["exclusion_reason"]:
        record["exclusion_reason"] = source.get("exclusion_reason", "not_authorized_for_phase6c_eval")
    return {key: value for key, value in record.items() if value not in (None, "")}


def duplicate_values(records: Sequence[Mapping[str, Any]], field: str) -> Dict[str, List[Mapping[str, Any]]]:
    grouped: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for record in records:
        value = str(record.get(field, ""))
        if value:
            grouped[value].append(record)
    return {value: grouped_records for value, grouped_records in grouped.items() if len(grouped_records) > 1}


if __name__ == "__main__":
    sys.exit(main())
