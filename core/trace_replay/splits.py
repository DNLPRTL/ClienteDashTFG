from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from typing import Iterable, Mapping


SPLIT_NAMES = ("train", "test", "eval")
DEFAULT_SPLIT_SEED = "phase3_rebuild_v1"
DEFAULT_SPLIT_STRATEGY = "stratified_by_semantics_and_leakage_group"


def stable_group_sort_key(group: str, seed: str, namespace: str = "") -> str:
    return hashlib.sha256("{0}|{1}|{2}".format(seed, namespace, group).encode("utf-8")).hexdigest()


def _split_group_names(
    groups: list[str],
    train_ratio: float,
    test_ratio: float,
) -> dict[str, str]:
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


def assign_splits_by_leakage_group(
    entries: Iterable[Mapping[str, object]],
    train_ratio: float = 0.7,
    test_ratio: float = 0.15,
    seed: str = DEFAULT_SPLIT_SEED,
) -> dict[str, str]:
    groups = sorted({str(entry["leakage_group"]) for entry in entries}, key=lambda group: stable_group_sort_key(group, seed))
    return _split_group_names(groups, train_ratio=train_ratio, test_ratio=test_ratio)


def assign_stratified_splits_by_semantics(
    entries: Iterable[Mapping[str, object]],
    train_ratio: float = 0.7,
    test_ratio: float = 0.15,
    seed: str = DEFAULT_SPLIT_SEED,
) -> dict[str, str]:
    groups_by_semantics: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        groups_by_semantics[str(entry["semantics"])].add(str(entry["leakage_group"]))

    split_by_group: dict[str, str] = {}
    for semantics in sorted(groups_by_semantics):
        groups = sorted(
            groups_by_semantics[semantics],
            key=lambda group: stable_group_sort_key(group, seed=seed, namespace=semantics),
        )
        split_by_group.update(_split_group_names(groups, train_ratio=train_ratio, test_ratio=test_ratio))
    return split_by_group


def split_counts(entries: Iterable[Mapping[str, object]]) -> dict[str, int]:
    counts = Counter(str(entry.get("split", "unassigned")) for entry in entries)
    return {name: counts.get(name, 0) for name in SPLIT_NAMES}


def group_counts(entries: Iterable[Mapping[str, object]]) -> dict[str, int]:
    counts = Counter(str(entry["leakage_group"]) for entry in entries)
    return dict(sorted(counts.items()))


def semantics_counts(entries: Iterable[Mapping[str, object]]) -> dict[str, int]:
    counts = Counter(str(entry["semantics"]) for entry in entries)
    return dict(sorted(counts.items()))


def mark_duplicates(entries: Iterable[Mapping[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    seen_source_fingerprint: dict[str, str] = {}
    accepted: list[dict[str, object]] = []
    excluded: list[dict[str, object]] = []

    for raw_entry in entries:
        entry = dict(raw_entry)
        trace_id = str(entry["trace_id"])
        duplicate_key = "{0}|{1}".format(
            entry.get("source_sha256", ""),
            entry.get("content_fingerprint_sha256", ""),
        )

        if duplicate_key and duplicate_key in seen_source_fingerprint:
            entry["excluded_from_final_manifest"] = True
            entry["exclusion_reasons"] = ["duplicate_source_hash_and_normalized_fingerprint:{0}".format(seen_source_fingerprint[duplicate_key])]
            excluded.append(entry)
            continue

        seen_source_fingerprint[duplicate_key] = trace_id
        entry["excluded_from_final_manifest"] = False
        entry["exclusion_reasons"] = []
        accepted.append(entry)

    return accepted, excluded


def build_phase3_trace_manifest(
    conversion_entries: Iterable[Mapping[str, object]],
    seed: str = DEFAULT_SPLIT_SEED,
    train_ratio: float = 0.7,
    test_ratio: float = 0.15,
    artifact_set: str = "smoke",
    split_strategy: str = DEFAULT_SPLIT_STRATEGY,
    puffer_sampling_policy: Mapping[str, object] | None = None,
) -> dict[str, object]:
    accepted, excluded = mark_duplicates(conversion_entries)
    if split_strategy == DEFAULT_SPLIT_STRATEGY:
        split_by_group = assign_stratified_splits_by_semantics(accepted, train_ratio=train_ratio, test_ratio=test_ratio, seed=seed)
    elif split_strategy == "by_leakage_group":
        split_by_group = assign_splits_by_leakage_group(accepted, train_ratio=train_ratio, test_ratio=test_ratio, seed=seed)
    else:
        raise ValueError("unknown split_strategy: {0}".format(split_strategy))

    final_entries: list[dict[str, object]] = []
    for entry in accepted:
        normalized = dict(entry)
        normalized["split"] = split_by_group[str(normalized["leakage_group"])]
        final_entries.append(normalized)

    return {
        "schema_id": "phase3_trace_manifest_final_v1",
        "phase": "phase3_rebuild",
        "artifact_set": artifact_set,
        "normalized_schema_id": "normalized_trace_schema_v1",
        "split_policy": "by_leakage_group",
        "split_strategy": split_strategy,
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
        "puffer_sampling_policy": dict(puffer_sampling_policy or {}),
        "trace_count": len(final_entries),
        "excluded_duplicate_count": len(excluded),
        "split_counts": split_counts(final_entries),
        "semantics_counts": semantics_counts(final_entries),
        "leakage_group_counts": group_counts(final_entries),
        "traces": sorted(final_entries, key=lambda item: str(item["trace_id"])),
        "excluded_duplicates": sorted(excluded, key=lambda item: str(item["trace_id"])),
    }
