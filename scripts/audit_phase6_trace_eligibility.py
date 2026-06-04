from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


SCHEMA_VERSION = "phase6_trace_eligibility_audit_v1"
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
DUPLICATE_FIELDS = ("checksum_sha256", "canonical_content_fingerprint", "trace_id", "leakage_group")
MISSING = "unspecified"


@dataclass(frozen=True)
class TraceRecord:
    role: str
    split: str
    eval_gate: str
    checksum_sha256: str
    canonical_content_fingerprint: str
    trace_id: str
    leakage_group: str
    source_path: str
    record_index: int


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Audit Phase 6 trace eligibility against Phase 4 seen traces.")
    parser.add_argument("--phase4-dataset-manifest", required=True, type=Path)
    parser.add_argument("--phase6-candidate-manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--fail-on-block",
        action="store_true",
        help="Return a non-zero exit code when use_for_phase6_eval is false.",
    )
    args = parser.parse_args(argv)

    phase4_records = load_manifest(args.phase4_dataset_manifest, role="phase4")
    phase6_records = load_manifest(args.phase6_candidate_manifest, role="phase6_candidate")
    report = build_report(
        phase4_records=phase4_records,
        phase6_records=phase6_records,
        phase4_manifest=args.phase4_dataset_manifest,
        phase6_manifest=args.phase6_candidate_manifest,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    status = "PASS" if report["use_for_phase6_eval"] else "BLOCK"
    print("phase6_trace_eligibility: {0}".format(status))
    print("output: {0}".format(args.output))
    if args.fail_on_block and not report["use_for_phase6_eval"]:
        return 2
    return 0


def build_report(
    *,
    phase4_records: Sequence[TraceRecord],
    phase6_records: Sequence[TraceRecord],
    phase4_manifest: Path,
    phase6_manifest: Path,
) -> Dict[str, Any]:
    phase6_eval_records = [record for record in phase6_records if is_phase6_eval_record(record)]
    overlaps = {
        "checksum_sha256": overlap_groups(phase4_records, phase6_eval_records, "checksum_sha256"),
        "canonical_content_fingerprint": overlap_groups(
            phase4_records,
            phase6_eval_records,
            "canonical_content_fingerprint",
        ),
        "trace_id": overlap_groups(phase4_records, phase6_eval_records, "trace_id"),
        "leakage_group": overlap_groups(phase4_records, phase6_eval_records, "leakage_group"),
    }
    internal_duplicates = {
        "phase4": internal_duplicate_report(phase4_records),
        "phase6_candidate": internal_duplicate_report(phase6_records),
    }
    logs_all_specific_duplicates = {
        "phase4": logs_all_specific_duplicate_groups(phase4_records),
        "phase6_candidate": logs_all_specific_duplicate_groups(phase6_records),
        "combined": logs_all_specific_duplicate_groups([*phase4_records, *phase6_records]),
    }

    reasons: List[str] = []
    if overlaps["checksum_sha256"]:
        reasons.append("Phase 6 evaluation split overlaps Phase 4 by checksum_sha256.")
    if overlaps["canonical_content_fingerprint"]:
        reasons.append("Phase 6 evaluation split overlaps Phase 4 by canonical_content_fingerprint.")
    if overlaps["trace_id"]:
        reasons.append("Phase 6 evaluation split overlaps Phase 4 by trace_id.")
    if overlaps["leakage_group"]:
        reasons.append("Phase 6 evaluation split overlaps Phase 4 by leakage_group.")

    phase6_cross_split = internal_duplicates["phase6_candidate"]["cross_split"]
    if phase6_cross_split["checksum_sha256"]:
        reasons.append("Phase 6 candidate has checksum_sha256 duplicates across splits.")
    if phase6_cross_split["canonical_content_fingerprint"]:
        reasons.append("Phase 6 candidate has canonical_content_fingerprint duplicates across splits.")
    if phase6_cross_split["trace_id"]:
        reasons.append("Phase 6 candidate has trace_id duplicates across splits.")
    if phase6_cross_split["leakage_group"]:
        reasons.append("Phase 6 candidate has leakage_group duplicates across splits.")

    phase6_within_split = internal_duplicates["phase6_candidate"]["within_split"]
    if phase6_within_split["checksum_sha256"]:
        reasons.append("Phase 6 candidate has duplicate checksum_sha256 values within a split.")
    if phase6_within_split["canonical_content_fingerprint"]:
        reasons.append("Phase 6 candidate has duplicate canonical_content_fingerprint values within a split.")

    use_for_phase6_eval = not reasons
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "phase4_dataset_manifest": str(phase4_manifest),
        "phase6_candidate_manifest": str(phase6_manifest),
        "rule": (
            "A trace identity used in Phase 4 train/validation/OOD must not enter Phase 6 "
            "evaluation splits for neural_abr_lite. Identity is checked separately by "
            "checksum_sha256, canonical_content_fingerprint, trace_id and leakage_group."
        ),
        "use_for_phase6_eval": use_for_phase6_eval,
        "reasons": reasons,
        "counts": {
            "phase4_records": len(phase4_records),
            "phase6_candidate_records": len(phase6_records),
            "phase6_eval_records": len(phase6_eval_records),
            "phase4_checksums": count_non_empty_unique(phase4_records, "checksum_sha256"),
            "phase6_eval_checksums": count_non_empty_unique(phase6_eval_records, "checksum_sha256"),
            "phase4_content_fingerprints": count_non_empty_unique(
                phase4_records,
                "canonical_content_fingerprint",
            ),
            "phase6_eval_content_fingerprints": count_non_empty_unique(
                phase6_eval_records,
                "canonical_content_fingerprint",
            ),
        },
        "splits": {
            "phase4": split_counts(phase4_records),
            "phase6_candidate": split_counts(phase6_records),
        },
        "overlaps": overlaps,
        "internal_duplicates": internal_duplicates,
        "logs_all_specific_duplicates": logs_all_specific_duplicates,
        "notes": [
            "Phase 4 internal duplicates are reported but do not block eligibility by themselves.",
            "checksum_sha256 and canonical_content_fingerprint are reported as separate identity fields.",
            "Blocked candidates may still be useful for separate classical-baseline diagnostics, not fair IA comparison.",
        ],
    }


def load_manifest(path: Path, *, role: str) -> List[TraceRecord]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    raw_records = list(iter_raw_records(data))
    records: List[TraceRecord] = []
    for index, (raw, default_split) in enumerate(raw_records):
        if not isinstance(raw, Mapping):
            continue
        split = normalized_value(first_value(raw, ("split", "phase", "dataset_split")) or default_split or MISSING)
        records.append(
            TraceRecord(
                role=role,
                split=split,
                eval_gate=normalized_eval_gate(first_value(raw, EVAL_GATE_ALIASES, include_empty=True)),
                checksum_sha256=normalized_checksum(first_value(raw, CHECKSUM_ALIASES)),
                canonical_content_fingerprint=normalized_checksum(first_value(raw, FINGERPRINT_ALIASES)),
                trace_id=normalized_value(first_value(raw, ("trace_id", "id", "trace_name", "name"))),
                leakage_group=normalized_value(first_value(raw, ("leakage_group", "leakage_id", "source_group"))),
                source_path=normalized_path(
                    first_value(
                        raw,
                        (
                            "source_path",
                            "source_file",
                            "relative_path",
                            "path",
                            "split_key",
                            "manifest_path",
                            "source_url_or_reference",
                        ),
                    )
                ),
                record_index=index,
            )
        )
    return records


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


def is_phase6_eval_record(record: TraceRecord) -> bool:
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


def overlap_groups(
    phase4_records: Sequence[TraceRecord],
    phase6_eval_records: Sequence[TraceRecord],
    field: str,
) -> List[Dict[str, Any]]:
    phase4 = group_by_field(phase4_records, field)
    phase6 = group_by_field(phase6_eval_records, field)
    groups = []
    for value in sorted(set(phase4).intersection(phase6)):
        groups.append(
            {
                "value": value,
                "phase4_records": [public_record(record) for record in phase4[value]],
                "phase6_records": [public_record(record) for record in phase6[value]],
            }
        )
    return groups


def internal_duplicate_report(records: Sequence[TraceRecord]) -> Dict[str, Any]:
    return {
        "within_split": {
            field: duplicate_groups_within_split(records, field)
            for field in DUPLICATE_FIELDS
        },
        "cross_split": {
            field: duplicate_groups_cross_split(records, field)
            for field in DUPLICATE_FIELDS
        },
    }


def duplicate_groups_within_split(records: Sequence[TraceRecord], field: str) -> List[Dict[str, Any]]:
    by_split: Dict[str, Dict[str, List[TraceRecord]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        value = getattr(record, field)
        if value:
            by_split[record.split][value].append(record)

    groups = []
    for split, values in sorted(by_split.items()):
        for value, grouped_records in sorted(values.items()):
            if len(grouped_records) > 1:
                groups.append(
                    {
                        "split": split,
                        "value": value,
                        "records": [public_record(record) for record in grouped_records],
                    }
                )
    return groups


def duplicate_groups_cross_split(records: Sequence[TraceRecord], field: str) -> List[Dict[str, Any]]:
    grouped = group_by_field(records, field)
    groups = []
    for value, grouped_records in sorted(grouped.items()):
        splits = sorted({record.split for record in grouped_records})
        if len(splits) > 1:
            groups.append(
                {
                    "value": value,
                    "splits": splits,
                    "records": [public_record(record) for record in grouped_records],
                }
            )
    return groups


def logs_all_specific_duplicate_groups(records: Sequence[TraceRecord]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str], List[TraceRecord]] = defaultdict(list)
    for record in records:
        identity_kind, content_identity = content_identity_for_ghent_grouping(record)
        if content_identity:
            grouped[(identity_kind, content_identity)].append(record)

    groups = []
    for (identity_kind, content_identity), grouped_records in sorted(grouped.items()):
        classes = {ghent_log_class(record.source_path) for record in grouped_records}
        if "logs_all" in classes and "specific" in classes:
            group = {
                "content_identity": content_identity,
                "identity_kind": identity_kind,
                "records": [public_record(record) for record in grouped_records],
            }
            checksum_values = sorted({record.checksum_sha256 for record in grouped_records if record.checksum_sha256})
            fingerprint_values = sorted(
                {
                    record.canonical_content_fingerprint
                    for record in grouped_records
                    if record.canonical_content_fingerprint
                }
            )
            if identity_kind == "checksum_sha256":
                group["checksum_sha256"] = content_identity
            if checksum_values:
                group["checksum_sha256_values"] = checksum_values
            if fingerprint_values:
                group["canonical_content_fingerprint_values"] = fingerprint_values
            groups.append(group)
    return groups


def content_identity_for_ghent_grouping(record: TraceRecord) -> Tuple[str, str]:
    if record.canonical_content_fingerprint:
        return "canonical_content_fingerprint", record.canonical_content_fingerprint
    return "checksum_sha256", record.checksum_sha256


def ghent_log_class(source_path: str) -> str:
    path = source_path.lower().replace("\\", "/")
    if "/logs_all/" in path or "logs_all/" in path:
        return "logs_all"
    if any(token in path for token in ("/logs_bus/", "/logs_car/", "/logs_foot/", "/logs_train/", "/logs_tram/")):
        return "specific"
    return "other"


def group_by_field(records: Sequence[TraceRecord], field: str) -> Dict[str, List[TraceRecord]]:
    grouped: Dict[str, List[TraceRecord]] = defaultdict(list)
    for record in records:
        value = getattr(record, field)
        if value:
            grouped[value].append(record)
    return dict(grouped)


def count_non_empty_unique(records: Sequence[TraceRecord], field: str) -> int:
    return len({getattr(record, field) for record in records if getattr(record, field)})


def split_counts(records: Sequence[TraceRecord]) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for record in records:
        counts[record.split] += 1
    return dict(sorted(counts.items()))


def public_record(record: TraceRecord) -> Dict[str, Any]:
    data = asdict(record)
    return {key: value for key, value in data.items() if value not in ("", None)}


if __name__ == "__main__":
    sys.exit(main())
