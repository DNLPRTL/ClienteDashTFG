from __future__ import annotations

import hashlib
import math
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Mapping, Sequence

from core.phase45_v1.constants import (
    PHASE45_V1_PHASE,
    SAMPLING_AUDIT_SCHEMA_ID,
    SAMPLING_PLAN_SCHEMA_ID,
    THROUGHPUT_BUCKETS,
    no_benchmark_policy,
)
from core.phase45_v1.profiles import DatasetProfile


class Phase45SamplingError(ValueError):
    """Raised when the Phase 4-5 v1 dataset sampler cannot build a safe plan."""


@dataclass(frozen=True)
class SamplingConfig:
    segment_duration_s: float
    window_duration_s: float
    train_window_count: int
    validation_window_count: int
    synthetic_max_fraction: float
    dataset_max_fraction: float
    semantics_max_fraction: float
    max_windows_per_trace: int
    seed: str

    @classmethod
    def from_profile(cls, profile: DatasetProfile) -> "SamplingConfig":
        return cls(
            segment_duration_s=4.0,
            window_duration_s=120.0,
            train_window_count=profile.train_window_count,
            validation_window_count=profile.validation_window_count,
            synthetic_max_fraction=profile.synthetic_max_fraction,
            dataset_max_fraction=profile.dataset_max_fraction,
            semantics_max_fraction=profile.semantics_max_fraction,
            max_windows_per_trace=profile.max_windows_per_trace,
            seed=profile.seed,
        )

    def to_json(self) -> dict[str, object]:
        return {
            "segment_duration_s": self.segment_duration_s,
            "window_duration_s": self.window_duration_s,
            "train_window_count": self.train_window_count,
            "validation_window_count": self.validation_window_count,
            "synthetic_max_fraction": self.synthetic_max_fraction,
            "dataset_max_fraction": self.dataset_max_fraction,
            "semantics_max_fraction": self.semantics_max_fraction,
            "max_windows_per_trace": self.max_windows_per_trace,
            "seed": self.seed,
        }


def build_sampling_artifacts(
    phase3_manifest: Mapping[str, object],
    profile: DatasetProfile,
    *,
    source_manifest_path: object | None = None,
) -> dict[str, object]:
    config = SamplingConfig.from_profile(profile)
    _validate_config(config)
    traces = _validated_phase3_traces(phase3_manifest)
    candidate_windows, excluded_summary = _build_candidate_windows(traces, config)
    training_selection = _select_windows(candidate_windows, "training", config.train_window_count, config)
    validation_selection = _select_windows(candidate_windows, "validation", config.validation_window_count, config)
    training_windows = training_selection["selected_windows"]
    validation_windows = validation_selection["selected_windows"]
    generated_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    common = {
        "schema_id": SAMPLING_PLAN_SCHEMA_ID,
        "phase": PHASE45_V1_PHASE,
        "generated_at_utc": generated_at_utc,
        "profile": profile.to_json(),
        "sampling_policy": config.to_json(),
        "source_manifest_path": str(source_manifest_path) if source_manifest_path is not None else None,
        "source_manifest_schema_id": phase3_manifest.get("schema_id"),
        "source_manifest_artifact_set": phase3_manifest.get("artifact_set"),
        "source_trace_count": phase3_manifest.get("trace_count"),
        "model_feature_fields": [],
        "metadata_fields_are_model_features": False,
        "eval_split_selected": False,
        **no_benchmark_policy(),
    }
    plan = {
        **common,
        "human_readable_name": "Phase 4-5 v1 selected trace windows for SPC/SPBC dataset generation",
        "media_profile_id": "paseo_10min_30fps_4s",
        "segment_count_per_window": int(round(config.window_duration_s / config.segment_duration_s)),
        "requested_training_window_count": config.train_window_count,
        "requested_validation_window_count": config.validation_window_count,
        "training_window_count": len(training_windows),
        "validation_window_count": len(validation_windows),
        "unfilled_requested_training_window_count": max(config.train_window_count - len(training_windows), 0),
        "unfilled_requested_validation_window_count": max(
            config.validation_window_count - len(validation_windows),
            0,
        ),
        "training_windows": training_windows,
        "validation_windows": validation_windows,
    }
    audit = {
        **common,
        "schema_id": SAMPLING_AUDIT_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v1 trace sampling audit",
        "candidate_window_summary": _summarize_windows(candidate_windows),
        "training_selection_summary": _selection_summary(training_windows, config.train_window_count, config),
        "validation_selection_summary": _selection_summary(validation_windows, config.validation_window_count, config),
        "selection_process": {
            "training": training_selection["selection_process"],
            "validation": validation_selection["selection_process"],
        },
        "excluded_source_split_summary": excluded_summary,
        "leakage_check": _leakage_check(training_windows, validation_windows),
        "low_variable_oversampling_policy": {
            "strategy": "weighted_round_robin_by_throughput_bucket_and_variability",
            "throughput_bucket_priority": {
                "lte_1_mbps": 5,
                "1_2_mbps": 4,
                "2_5_mbps": 3,
                "5_20_mbps": 2,
                "gt_20_mbps": 1,
            },
            "variable_trace_bonus": 1,
        },
    }
    validate_sampling_plan(plan, config)
    return {"plan": plan, "audit": audit}


def validate_sampling_plan(plan: Mapping[str, object], config: SamplingConfig | None = None) -> dict[str, object]:
    if plan.get("schema_id") != SAMPLING_PLAN_SCHEMA_ID:
        raise Phase45SamplingError("unexpected Phase 4-5 v1 sampling plan schema_id")
    _assert_no_benchmark_flags(plan)
    active_config = config or _config_from_plan(plan)
    _validate_config(active_config)
    training_windows = _require_window_list(plan, "training_windows")
    validation_windows = _require_window_list(plan, "validation_windows")
    selected = training_windows + validation_windows
    if not selected:
        raise Phase45SamplingError("sampling plan has no selected windows")

    seen_window_ids: set[str] = set()
    leakage_group_to_role: dict[str, str] = {}
    for window in selected:
        window_id = str(window.get("window_id"))
        if window_id in seen_window_ids:
            raise Phase45SamplingError("duplicate selected window_id: {0}".format(window_id))
        seen_window_ids.add(window_id)

        source_split = str(window.get("source_split"))
        if source_split == "eval":
            raise Phase45SamplingError("eval split cannot be selected for Phase 4-5 v1 dataset")
        expected_role = "training" if source_split == "train" else "validation"
        if window.get("training_plan_role") != expected_role:
            raise Phase45SamplingError("{0}: source split and role mismatch".format(window_id))

        group = str(window.get("leakage_group"))
        previous_role = leakage_group_to_role.get(group)
        if previous_role is not None and previous_role != expected_role:
            raise Phase45SamplingError("{0}: leakage_group selected across roles".format(group))
        leakage_group_to_role[group] = expected_role

    _assert_fraction_caps(training_windows, active_config.train_window_count, active_config, "training")
    _assert_fraction_caps(validation_windows, active_config.validation_window_count, active_config, "validation")
    return {
        "status": "PASS",
        "training_window_count": len(training_windows),
        "validation_window_count": len(validation_windows),
        "selected_window_count": len(selected),
    }


def _validated_phase3_traces(phase3_manifest: Mapping[str, object]) -> list[Mapping[str, object]]:
    if phase3_manifest.get("schema_id") != "phase3_trace_manifest_final_v1":
        raise Phase45SamplingError("source manifest must be phase3_trace_manifest_final_v1")
    if phase3_manifest.get("benchmark_authorized") is not False:
        raise Phase45SamplingError("source manifest benchmark_authorized must be false")
    traces = phase3_manifest.get("traces")
    if not isinstance(traces, list):
        raise Phase45SamplingError("source manifest traces must be a list")
    if int(phase3_manifest.get("trace_count", -1)) != len(traces):
        raise Phase45SamplingError("source manifest trace_count mismatch")

    group_to_split: dict[str, str] = {}
    for index, trace in enumerate(traces):
        if not isinstance(trace, Mapping):
            raise Phase45SamplingError("trace {0} must be an object".format(index))
        for field in (
            "trace_id",
            "dataset_id",
            "normalized_trace_path",
            "group_id",
            "leakage_group",
            "semantics",
            "split",
            "duration_s",
            "throughput_mean_kbps",
        ):
            if field not in trace:
                raise Phase45SamplingError("trace {0}: missing {1}".format(index, field))
        split = str(trace["split"])
        if split not in {"train", "test", "eval"}:
            raise Phase45SamplingError("{0}: invalid split {1}".format(trace["trace_id"], split))
        group = str(trace["leakage_group"])
        previous_split = group_to_split.get(group)
        if previous_split is not None and previous_split != split:
            raise Phase45SamplingError("{0}: leakage_group spans splits".format(group))
        group_to_split[group] = split
    return traces


def _build_candidate_windows(
    traces: Sequence[Mapping[str, object]],
    config: SamplingConfig,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    windows: list[dict[str, object]] = []
    excluded_counts: Counter[str] = Counter()
    excluded_by_split: Counter[str] = Counter()
    eval_eligible_windows = 0
    eval_eligible_traces = 0

    for trace in traces:
        split = str(trace["split"])
        possible_windows = _window_count_for_trace(trace, config)
        if split == "eval":
            if possible_windows > 0:
                eval_eligible_traces += 1
                eval_eligible_windows += possible_windows
            excluded_counts["eval_split_reserved_for_phase6_or_future_eval"] += 1
            excluded_by_split[split] += 1
            continue

        role = "training" if split == "train" else "validation"
        if not _trace_allowed_for_role(trace, role):
            excluded_counts["source_trace_not_allowed_for_{0}".format(role)] += 1
            excluded_by_split[split] += 1
            continue
        if possible_windows <= 0:
            excluded_counts["trace_shorter_than_window_duration"] += 1
            excluded_by_split[split] += 1
            continue
        for sequence_index in range(possible_windows):
            windows.append(_window_record(trace, role, sequence_index, possible_windows, config))

    windows.sort(key=lambda item: str(item["window_id"]))
    return windows, {
        "excluded_trace_counts_by_reason": dict(sorted(excluded_counts.items())),
        "excluded_trace_counts_by_source_split": dict(sorted(excluded_by_split.items())),
        "eval_split_reserved_for_future_evaluation": True,
        "eval_eligible_trace_count": eval_eligible_traces,
        "eval_eligible_window_count": eval_eligible_windows,
    }


def _select_windows(
    windows: Sequence[Mapping[str, object]],
    role: str,
    target_count: int,
    config: SamplingConfig,
) -> dict[str, object]:
    role_windows = [dict(window) for window in windows if window.get("training_plan_role") == role]
    rng = random.Random("{0}:{1}".format(config.seed, role))
    grouped: dict[tuple[str, str, str, str], list[dict[str, object]]] = defaultdict(list)
    for window in role_windows:
        grouped[_selection_group_key(window)].append(window)
    for group_windows in grouped.values():
        rng.shuffle(group_windows)

    active_keys = []
    for key in sorted(grouped):
        weight = _selection_weight_for_key(key)
        active_keys.extend([key] * weight)
    rng.shuffle(active_keys)

    selected: list[dict[str, object]] = []
    rejected_counts: Counter[str] = Counter()
    counters = _SelectionCounters()
    while active_keys and len(selected) < target_count:
        next_active_keys: list[tuple[str, str, str, str]] = []
        seen_this_round: set[tuple[str, str, str, str]] = set()
        for key in active_keys:
            if key in seen_this_round and not grouped[key]:
                continue
            seen_this_round.add(key)
            candidates = grouped[key]
            if not candidates:
                continue
            window = candidates.pop()
            rejection = _quota_rejection_reason(window, counters, target_count, config)
            if rejection is None:
                selected.append(window)
                counters.add(window)
                if len(selected) >= target_count:
                    break
            else:
                rejected_counts[rejection] += 1
            if candidates:
                next_active_keys.extend([key] * _selection_weight_for_key(key))
        active_keys = next_active_keys
        rng.shuffle(active_keys)

    selected.sort(key=lambda item: str(item["window_id"]))
    return {
        "selected_windows": selected,
        "selection_process": {
            "candidate_count": len(role_windows),
            "target_count": target_count,
            "selected_count": len(selected),
            "unfilled_target_count": max(target_count - len(selected), 0),
            "selection_key": "weighted_round_robin_by_dataset_semantics_throughput_bucket_variability",
            "rejected_counts_by_reason": dict(sorted(rejected_counts.items())),
        },
    }


@dataclass
class _SelectionCounters:
    total: int = 0
    synthetic: int = 0
    by_dataset: Counter[str] | None = None
    by_semantics: Counter[str] | None = None
    by_trace: Counter[str] | None = None

    def __post_init__(self) -> None:
        self.by_dataset = Counter()
        self.by_semantics = Counter()
        self.by_trace = Counter()

    def add(self, window: Mapping[str, object]) -> None:
        self.total += 1
        if window.get("synthetic") is True:
            self.synthetic += 1
        self.by_dataset[str(window["dataset_id"])] += 1
        self.by_semantics[str(window["semantics"])] += 1
        self.by_trace[str(window["trace_id"])] += 1


def _quota_rejection_reason(
    window: Mapping[str, object],
    counters: _SelectionCounters,
    target_count: int,
    config: SamplingConfig,
) -> str | None:
    if counters.by_trace[str(window["trace_id"])] >= config.max_windows_per_trace:
        return "max_windows_per_trace_reached"
    if window.get("synthetic") is True and counters.synthetic >= _quota_limit(target_count, config.synthetic_max_fraction):
        return "synthetic_max_fraction_reached"
    dataset_id = str(window["dataset_id"])
    if counters.by_dataset[dataset_id] >= _quota_limit(target_count, config.dataset_max_fraction):
        return "dataset_max_fraction_reached"
    semantics = str(window["semantics"])
    if counters.by_semantics[semantics] >= _quota_limit(target_count, config.semantics_max_fraction):
        return "semantics_max_fraction_reached"
    return None


def _window_record(
    trace: Mapping[str, object],
    role: str,
    sequence_index: int,
    trace_window_count: int,
    config: SamplingConfig,
) -> dict[str, object]:
    start_s = float(sequence_index) * config.window_duration_s
    end_s = start_s + config.window_duration_s
    mean_kbps = float(trace["throughput_mean_kbps"])
    synthetic = _is_synthetic_trace(trace)
    network_condition = _string_or_unknown(trace.get("network_condition"))
    return {
        "window_id": _window_id(str(trace["trace_id"]), sequence_index, config),
        "trace_id": str(trace["trace_id"]),
        "dataset_id": str(trace["dataset_id"]),
        "semantics": str(trace["semantics"]),
        "source_split": str(trace["split"]),
        "training_plan_role": role,
        "group_id": str(trace["group_id"]),
        "leakage_group": str(trace["leakage_group"]),
        "normalized_trace_path": str(trace["normalized_trace_path"]),
        "metadata_path": str(trace.get("metadata_path", "")),
        "window_sequence_index": sequence_index,
        "window_start_s": round(start_s, 6),
        "window_end_s": round(end_s, 6),
        "window_duration_s": round(config.window_duration_s, 6),
        "segment_duration_s": round(config.segment_duration_s, 6),
        "segment_count": int(round(config.window_duration_s / config.segment_duration_s)),
        "trace_window_count": trace_window_count,
        "trace_duration_s": round(float(trace["duration_s"]), 6),
        "throughput_min_kbps": round(float(trace.get("throughput_min_kbps", 0.0)), 6),
        "throughput_mean_kbps": round(mean_kbps, 6),
        "throughput_max_kbps": round(float(trace.get("throughput_max_kbps", 0.0)), 6),
        "throughput_bucket": throughput_bucket(mean_kbps),
        "variability_bucket": variability_bucket(trace),
        "zero_fraction": round(float(trace.get("zero_fraction", 0.0) or 0.0), 6),
        "network_condition": network_condition,
        "synthetic": synthetic,
        "synthetic_scenario": network_condition if synthetic else None,
    }


def throughput_bucket(mean_kbps: float) -> str:
    value = float(mean_kbps)
    if value <= 1000.0:
        return "lte_1_mbps"
    if value <= 2000.0:
        return "1_2_mbps"
    if value <= 5000.0:
        return "2_5_mbps"
    if value <= 20000.0:
        return "5_20_mbps"
    return "gt_20_mbps"


def variability_bucket(trace: Mapping[str, object]) -> str:
    zero_fraction = float(trace.get("zero_fraction", 0.0) or 0.0)
    if zero_fraction >= 0.10:
        return "zero_or_outage_heavy"
    mean = max(float(trace.get("throughput_mean_kbps", 0.0) or 0.0), 1.0)
    minimum = float(trace.get("throughput_min_kbps", 0.0) or 0.0)
    maximum = float(trace.get("throughput_max_kbps", 0.0) or 0.0)
    if maximum / mean >= 3.0 or minimum / mean <= 0.35:
        return "high_variability"
    return "stable_or_moderate"


def _selection_group_key(window: Mapping[str, object]) -> tuple[str, str, str, str]:
    return (
        str(window["dataset_id"]),
        str(window["semantics"]),
        str(window["throughput_bucket"]),
        str(window["variability_bucket"]),
    )


def _selection_weight_for_key(key: tuple[str, str, str, str]) -> int:
    bucket = key[2]
    variability = key[3]
    bucket_weight = {
        "lte_1_mbps": 5,
        "1_2_mbps": 4,
        "2_5_mbps": 3,
        "5_20_mbps": 2,
        "gt_20_mbps": 1,
    }.get(bucket, 1)
    variable_bonus = 1 if variability in {"zero_or_outage_heavy", "high_variability"} else 0
    return max(1, bucket_weight + variable_bonus)


def _trace_allowed_for_role(trace: Mapping[str, object], role: str) -> bool:
    if role == "training":
        return trace.get("usable_for_training", True) is not False
    if role == "validation":
        return trace.get("usable_for_eval", True) is not False
    return False


def _window_count_for_trace(trace: Mapping[str, object], config: SamplingConfig) -> int:
    try:
        duration_s = float(trace["duration_s"])
    except (TypeError, ValueError) as exc:
        raise Phase45SamplingError("{0}: invalid duration_s".format(trace.get("trace_id"))) from exc
    if duration_s < config.window_duration_s:
        return 0
    return int(math.floor((duration_s + 1e-9) / config.window_duration_s))


def _validate_config(config: SamplingConfig) -> None:
    for field, value in (("segment_duration_s", config.segment_duration_s), ("window_duration_s", config.window_duration_s)):
        if isinstance(value, bool) or not math.isfinite(float(value)) or float(value) <= 0.0:
            raise Phase45SamplingError("{0} must be positive".format(field))
    if abs((config.window_duration_s / config.segment_duration_s) - round(config.window_duration_s / config.segment_duration_s)) > 1e-9:
        raise Phase45SamplingError("window_duration_s must be an exact multiple of segment_duration_s")
    for field, value in (
        ("train_window_count", config.train_window_count),
        ("validation_window_count", config.validation_window_count),
        ("max_windows_per_trace", config.max_windows_per_trace),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise Phase45SamplingError("{0} must be a positive integer".format(field))
    for field, value in (
        ("synthetic_max_fraction", config.synthetic_max_fraction),
        ("dataset_max_fraction", config.dataset_max_fraction),
        ("semantics_max_fraction", config.semantics_max_fraction),
    ):
        if isinstance(value, bool) or not math.isfinite(float(value)) or not 0.0 < float(value) <= 1.0:
            raise Phase45SamplingError("{0} must be in (0, 1]".format(field))
    if not str(config.seed).strip():
        raise Phase45SamplingError("seed must not be empty")


def _config_from_plan(plan: Mapping[str, object]) -> SamplingConfig:
    policy = plan.get("sampling_policy")
    if not isinstance(policy, Mapping):
        raise Phase45SamplingError("sampling plan missing sampling_policy")
    return SamplingConfig(
        segment_duration_s=float(policy["segment_duration_s"]),
        window_duration_s=float(policy["window_duration_s"]),
        train_window_count=int(policy["train_window_count"]),
        validation_window_count=int(policy["validation_window_count"]),
        synthetic_max_fraction=float(policy["synthetic_max_fraction"]),
        dataset_max_fraction=float(policy["dataset_max_fraction"]),
        semantics_max_fraction=float(policy["semantics_max_fraction"]),
        max_windows_per_trace=int(policy["max_windows_per_trace"]),
        seed=str(policy["seed"]),
    )


def _require_window_list(plan: Mapping[str, object], field: str) -> list[Mapping[str, object]]:
    raw = plan.get(field)
    if not isinstance(raw, list):
        raise Phase45SamplingError("{0} must be a list".format(field))
    for index, item in enumerate(raw):
        if not isinstance(item, Mapping):
            raise Phase45SamplingError("{0}[{1}] must be an object".format(field, index))
    return raw


def _assert_fraction_caps(
    windows: Sequence[Mapping[str, object]],
    target_count: int,
    config: SamplingConfig,
    role: str,
) -> None:
    if not windows:
        raise Phase45SamplingError("{0}: no selected windows".format(role))
    counts = _count_windows(windows)
    checks = _quota_checks(counts, target_count, config)
    failed = [name for name, check in checks.items() if check["status"] != "PASS"]
    if failed:
        raise Phase45SamplingError("{0}: failed quota checks {1}".format(role, ", ".join(failed)))


def _quota_checks(counts: Mapping[str, object], target_count: int, config: SamplingConfig) -> dict[str, dict[str, object]]:
    return {
        "synthetic_max_fraction": _fraction_check(int(counts["synthetic_count"]), target_count, config.synthetic_max_fraction),
        "dataset_max_fraction": _max_counter_fraction_check(counts["by_dataset"], target_count, config.dataset_max_fraction),
        "semantics_max_fraction": _max_counter_fraction_check(counts["by_semantics"], target_count, config.semantics_max_fraction),
    }


def _fraction_check(count: int, target_count: int, max_fraction: float) -> dict[str, object]:
    limit = _quota_limit(target_count, max_fraction)
    return {
        "status": "PASS" if count <= limit else "FAIL",
        "count": count,
        "limit": limit,
        "max_fraction": max_fraction,
        "observed_fraction_of_target": round(float(count) / float(target_count), 6) if target_count else 0.0,
    }


def _max_counter_fraction_check(counter_data: object, target_count: int, max_fraction: float) -> dict[str, object]:
    counter = Counter(counter_data or {})
    if not counter:
        return _fraction_check(0, target_count, max_fraction)
    name, count = counter.most_common(1)[0]
    result = _fraction_check(count, target_count, max_fraction)
    result["largest_bucket"] = name
    return result


def _count_windows(windows: Sequence[Mapping[str, object]]) -> dict[str, object]:
    by_dataset = Counter(str(window["dataset_id"]) for window in windows)
    by_semantics = Counter(str(window["semantics"]) for window in windows)
    by_throughput_bucket = Counter(str(window["throughput_bucket"]) for window in windows)
    by_variability_bucket = Counter(str(window["variability_bucket"]) for window in windows)
    return {
        "total_count": len(windows),
        "synthetic_count": sum(1 for window in windows if window.get("synthetic") is True),
        "real_trace_count": sum(1 for window in windows if window.get("synthetic") is not True),
        "by_dataset": dict(sorted(by_dataset.items())),
        "by_semantics": dict(sorted(by_semantics.items())),
        "by_throughput_bucket": {bucket: by_throughput_bucket.get(bucket, 0) for bucket in THROUGHPUT_BUCKETS},
        "by_variability_bucket": dict(sorted(by_variability_bucket.items())),
    }


def _selection_summary(
    windows: Sequence[Mapping[str, object]],
    target_count: int,
    config: SamplingConfig,
) -> dict[str, object]:
    counts = _count_windows(windows)
    return {
        "target_count": target_count,
        "selected_count": len(windows),
        "unfilled_target_count": max(target_count - len(windows), 0),
        "counts": counts,
        "quota_checks": _quota_checks(counts, target_count, config),
    }


def _summarize_windows(windows: Sequence[Mapping[str, object]]) -> dict[str, object]:
    by_role = Counter(str(window["training_plan_role"]) for window in windows)
    by_source_split = Counter(str(window["source_split"]) for window in windows)
    by_bucket = Counter(str(window["throughput_bucket"]) for window in windows)
    by_variability = Counter(str(window["variability_bucket"]) for window in windows)
    return {
        "total_candidate_window_count": len(windows),
        "by_training_plan_role": dict(sorted(by_role.items())),
        "by_source_split": dict(sorted(by_source_split.items())),
        "by_throughput_bucket": {bucket: by_bucket.get(bucket, 0) for bucket in THROUGHPUT_BUCKETS},
        "by_variability_bucket": dict(sorted(by_variability.items())),
    }


def _leakage_check(
    training_windows: Sequence[Mapping[str, object]],
    validation_windows: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    group_to_role: dict[str, str] = {}
    conflicts: list[str] = []
    for role, windows in (("training", training_windows), ("validation", validation_windows)):
        for window in windows:
            group = str(window["leakage_group"])
            previous_role = group_to_role.get(group)
            if previous_role is not None and previous_role != role:
                conflicts.append(group)
            group_to_role[group] = role
    return {
        "status": "PASS" if not conflicts else "FAIL",
        "checked_leakage_group_count": len(group_to_role),
        "conflicting_leakage_groups": sorted(set(conflicts)),
        "eval_split_selected": False,
    }


def _quota_limit(target_count: int, fraction: float) -> int:
    return max(1, int(math.ceil(float(target_count) * float(fraction))))


def _window_id(trace_id: str, sequence_index: int, config: SamplingConfig) -> str:
    digest = hashlib.sha256(
        "{0}|{1}|{2}|{3}".format(trace_id, sequence_index, config.window_duration_s, config.segment_duration_s).encode(
            "utf-8"
        )
    ).hexdigest()[:12]
    start_s = int(round(sequence_index * config.window_duration_s))
    return "{0}__phase45v1_start_{1:06d}s__{2}".format(_safe_id(trace_id), start_s, digest)


def _safe_id(value: str) -> str:
    chars = [char if char.isalnum() or char in {"-", "_"} else "_" for char in str(value)]
    text = "".join(chars).strip("_")
    return (text[:80].rstrip("_") or "trace")


def _string_or_unknown(value: object) -> str:
    text = "" if value is None else str(value).strip()
    return text or "unknown"


def _is_synthetic_trace(trace: Mapping[str, object]) -> bool:
    return trace.get("synthetic") is True or str(trace.get("dataset_id")) == "synthetic_controlled_network"


def _assert_no_benchmark_flags(mapping: Mapping[str, object]) -> None:
    for flag, expected in no_benchmark_policy().items():
        if mapping.get(flag) is not expected:
            raise Phase45SamplingError("{0} must be {1}".format(flag, expected))
