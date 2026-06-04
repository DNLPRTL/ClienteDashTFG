from __future__ import annotations

import hashlib
from collections import Counter
from typing import Iterable, Mapping


SPLIT_NAMES = ("train", "test", "eval")


def stable_group_sort_key(group: str, seed: str) -> str:
    return hashlib.sha256("{0}|{1}".format(seed, group).encode("utf-8")).hexdigest()


def assign_splits_by_leakage_group(
    entries: Iterable[Mapping[str, object]],
    train_ratio: float = 0.7,
    test_ratio: float = 0.15,
    seed: str = "phase3_rebuild_v1",
) -> dict[str, str]:
    groups = sorted({str(entry["leakage_group"]) for entry in entries}, key=lambda group: stable_group_sort_key(group, seed))
    if not groups:
        return {}

    train_count = round(len(groups) * train_ratio)
    test_count = round(len(groups) * test_ratio)
    if len(groups) >= 3:
        train_count = max(1, min(train_count, len(groups) - 2))
        test_count = max(1, min(test_count, len(groups) - train_count - 1))
    elif len(groups) == 2:
        train_count = 1
        test_count = 1
    else:
        train_count = 1
        test_count = 0

    mapping: dict[str, str] = {}
    for index, group in enumerate(groups):
        if index < train_count:
            mapping[group] = "train"
        elif index < train_count + test_count:
            mapping[group] = "test"
        else:
            mapping[group] = "eval"
    return mapping


def split_counts(entries: Iterable[Mapping[str, object]]) -> dict[str, int]:
    counts = Counter(str(entry.get("split", "unassigned")) for entry in entries)
    return {name: counts.get(name, 0) for name in SPLIT_NAMES}


def group_counts(entries: Iterable[Mapping[str, object]]) -> dict[str, int]:
    counts = Counter(str(entry["leakage_group"]) for entry in entries)
    return dict(sorted(counts.items()))


def mark_duplicates(entries: Iterable[Mapping[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    seen_source_group: dict[str, str] = {}
    seen_content: dict[str, str] = {}
    seen_dataset_group: dict[str, str] = {}
    accepted: list[dict[str, object]] = []
    excluded: list[dict[str, object]] = []

    for raw_entry in entries:
        entry = dict(raw_entry)
        trace_id = str(entry["trace_id"])
        source_group_key = "{0}|{1}".format(entry.get("source_sha256", ""), entry.get("group_id", ""))
        content_key = str(entry.get("content_fingerprint_sha256", ""))
        dataset_group_key = "{0}|{1}".format(entry.get("dataset_id", ""), entry.get("group_id", ""))

        reasons: list[str] = []
        for label, key, seen in (
            ("duplicate_source_hash_group", source_group_key, seen_source_group),
            ("duplicate_normalized_fingerprint", content_key, seen_content),
            ("duplicate_dataset_group", dataset_group_key, seen_dataset_group),
        ):
            if key and key in seen:
                reasons.append("{0}:{1}".format(label, seen[key]))

        if reasons:
            entry["excluded_from_final_manifest"] = True
            entry["exclusion_reasons"] = reasons
            excluded.append(entry)
            continue

        seen_source_group[source_group_key] = trace_id
        seen_content[content_key] = trace_id
        seen_dataset_group[dataset_group_key] = trace_id
        entry["excluded_from_final_manifest"] = False
        entry["exclusion_reasons"] = []
        accepted.append(entry)

    return accepted, excluded


def build_phase3_trace_manifest(
    conversion_entries: Iterable[Mapping[str, object]],
    seed: str = "phase3_rebuild_v1",
    train_ratio: float = 0.7,
    test_ratio: float = 0.15,
) -> dict[str, object]:
    accepted, excluded = mark_duplicates(conversion_entries)
    split_by_group = assign_splits_by_leakage_group(accepted, train_ratio=train_ratio, test_ratio=test_ratio, seed=seed)
    final_entries: list[dict[str, object]] = []
    for entry in accepted:
        normalized = dict(entry)
        normalized["split"] = split_by_group[str(normalized["leakage_group"])]
        final_entries.append(normalized)

    return {
        "schema_id": "phase3_trace_manifest_final_v1",
        "phase": "phase3_rebuild",
        "normalized_schema_id": "normalized_trace_schema_v1",
        "split_policy": "by_leakage_group",
        "split_seed": seed,
        "train_ratio": train_ratio,
        "test_ratio": test_ratio,
        "eval_ratio": max(0.0, 1.0 - train_ratio - test_ratio),
        "ready_for_benchmark": False,
        "benchmark_authorized": False,
        "outputs_are_benchmark_results": False,
        "qoe_claims_authorized": False,
        "controller_visibility_guardrail": (
            "controllers must not receive trace_id, dataset_id, source_id, split, group_id, "
            "leakage_group, OOD flags, or future throughput"
        ),
        "trace_count": len(final_entries),
        "excluded_duplicate_count": len(excluded),
        "split_counts": split_counts(final_entries),
        "leakage_group_counts": group_counts(final_entries),
        "traces": sorted(final_entries, key=lambda item: str(item["trace_id"])),
        "excluded_duplicates": sorted(excluded, key=lambda item: str(item["trace_id"])),
    }
