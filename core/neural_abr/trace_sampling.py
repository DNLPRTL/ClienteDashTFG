from __future__ import annotations

import hashlib
import json
import math
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Sequence


PHASE4A_PHASE = "phase4a_plan_de_trazas_para_entrenamiento"
TRACE_WINDOW_INDEX_SCHEMA_ID = "phase4_trace_window_index_v1"
TRAINING_TRACE_PLAN_SCHEMA_ID = "phase4_training_trace_plan_v1"
SAMPLING_AUDIT_SCHEMA_ID = "phase4_sampling_audit_v1"

TRACE_WINDOW_INDEX_FILENAME = "phase4_indice_de_ventanas_de_traza.json"
TRAINING_TRACE_PLAN_FILENAME = "phase4_plan_de_trazas_para_entrenamiento.json"
SAMPLING_AUDIT_FILENAME = "phase4_auditoria_de_seleccion_de_trazas.json"

DEFAULT_SEED = "phase4a_training_trace_sampler_v1"

PROHIBITED_MODEL_FEATURE_FIELDS = (
    "trace_id",
    "dataset_id",
    "source_id",
    "split",
    "source_split",
    "training_plan_role",
    "group_id",
    "leakage_group",
    "semantics",
    "network_condition",
    "synthetic",
    "synthetic_scenario",
    "future_throughput_kbps",
    "future_reward",
    "future_qoe",
    "final_qoe",
    "teacher_action",
    "benchmark_rank",
)


class Phase4TraceSamplingError(ValueError):
    """Raised when a Phase 4A trace plan cannot be built safely."""


@dataclass(frozen=True)
class Phase4SamplingConfig:
    segment_duration_s: float = 4.0
    window_duration_s: float = 120.0
    train_window_count: int = 4096
    validation_window_count: int = 1024
    synthetic_max_fraction: float = 0.15
    dataset_max_fraction: float = 0.30
    semantics_max_fraction: float = 0.35
    difficulty_max_fraction: float = 0.45
    max_windows_per_trace: int = 3
    seed: str = DEFAULT_SEED


def build_phase4_training_trace_artifacts(
    phase3_manifest: Mapping[str, object],
    config: Phase4SamplingConfig | None = None,
    source_manifest_path: str | Path | None = None,
) -> dict[str, dict[str, object]]:
    """Build the three external Phase 4A artifacts from a Phase 3 manifest."""

    active_config = config or Phase4SamplingConfig()
    _validate_config(active_config)
    traces = _validated_phase3_traces(phase3_manifest)

    all_windows, excluded_summary = _build_trace_windows(traces, active_config)
    training_windows = _select_balanced_windows(all_windows, "training", active_config.train_window_count, active_config)
    validation_windows = _select_balanced_windows(
        all_windows,
        "validation",
        active_config.validation_window_count,
        active_config,
    )
    selected_training = training_windows["selected_windows"]
    selected_validation = validation_windows["selected_windows"]

    generated_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    source_manifest = str(source_manifest_path) if source_manifest_path is not None else None
    common_contract = _common_contract(active_config, phase3_manifest, source_manifest, generated_at_utc)

    window_index = {
        **common_contract,
        "schema_id": TRACE_WINDOW_INDEX_SCHEMA_ID,
        "human_readable_name": "Phase 4A trace window index for offline training trace planning",
        "windows_are_model_features": False,
        "window_count": len(all_windows),
        "windows": all_windows,
        "excluded_source_split_summary": excluded_summary,
    }

    training_plan = {
        **common_contract,
        "schema_id": TRAINING_TRACE_PLAN_SCHEMA_ID,
        "human_readable_name": "Phase 4A balanced training and validation trace plan",
        "primary_segment_duration_s": active_config.segment_duration_s,
        "diagnostic_segment_duration_s": 2.0,
        "diagnostic_segment_duration_policy": "2s is diagnostic-only and is not selected by this Phase 4A plan",
        "requested_training_window_count": active_config.train_window_count,
        "requested_validation_window_count": active_config.validation_window_count,
        "training_window_count": len(selected_training),
        "validation_window_count": len(selected_validation),
        "unfilled_requested_training_window_count": max(active_config.train_window_count - len(selected_training), 0),
        "unfilled_requested_validation_window_count": max(
            active_config.validation_window_count - len(selected_validation),
            0,
        ),
        "training_windows": selected_training,
        "validation_windows": selected_validation,
        "model_feature_fields": [],
        "metadata_fields_not_allowed_as_model_features": list(PROHIBITED_MODEL_FEATURE_FIELDS),
    }

    audit = {
        **common_contract,
        "schema_id": SAMPLING_AUDIT_SCHEMA_ID,
        "human_readable_name": "Phase 4A sampling audit for trace balance and leakage checks",
        "candidate_window_summary": _summarize_windows(all_windows),
        "training_selection_summary": _selection_summary(selected_training, active_config.train_window_count, active_config),
        "validation_selection_summary": _selection_summary(
            selected_validation,
            active_config.validation_window_count,
            active_config,
        ),
        "selection_process": {
            "training": training_windows["selection_process"],
            "validation": validation_windows["selection_process"],
        },
        "excluded_source_split_summary": excluded_summary,
        "leakage_check": _leakage_check(selected_training, selected_validation),
        "no_benchmark_policy": _no_benchmark_policy(),
    }

    validate_phase4_training_trace_plan(training_plan, active_config)
    return {
        TRACE_WINDOW_INDEX_FILENAME: window_index,
        TRAINING_TRACE_PLAN_FILENAME: training_plan,
        SAMPLING_AUDIT_FILENAME: audit,
    }


def write_phase4_training_trace_artifacts(
    output_root: str | Path,
    artifacts: Mapping[str, Mapping[str, object]],
) -> dict[str, str]:
    output_dir = Path(output_root)
    output_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}
    for filename in (TRACE_WINDOW_INDEX_FILENAME, TRAINING_TRACE_PLAN_FILENAME, SAMPLING_AUDIT_FILENAME):
        if filename not in artifacts:
            raise Phase4TraceSamplingError("missing artifact: {0}".format(filename))
        path = output_dir / filename
        path.write_text(json.dumps(artifacts[filename], indent=2, sort_keys=True), encoding="utf-8")
        written[filename] = str(path)
    return written


def validate_phase4_training_trace_plan(
    training_plan: Mapping[str, object],
    config: Phase4SamplingConfig | None = None,
) -> dict[str, object]:
    active_config = config or _config_from_plan(training_plan)
    _validate_config(active_config)
    if training_plan.get("schema_id") != TRAINING_TRACE_PLAN_SCHEMA_ID:
        raise Phase4TraceSamplingError("unexpected training plan schema_id")
    _assert_no_benchmark_flags(training_plan)

    training_windows = _require_window_list(training_plan, "training_windows")
    validation_windows = _require_window_list(training_plan, "validation_windows")
    selected = training_windows + validation_windows
    if not selected:
        raise Phase4TraceSamplingError("training plan has no selected windows")

    seen_window_ids: set[str] = set()
    group_to_split: dict[str, str] = {}
    for window in selected:
        window_id = str(window.get("window_id"))
        if window_id in seen_window_ids:
            raise Phase4TraceSamplingError("duplicate selected window_id: {0}".format(window_id))
        seen_window_ids.add(window_id)

        source_split = str(window.get("source_split"))
        if source_split == "eval":
            raise Phase4TraceSamplingError("eval split cannot be selected for Phase 4A training plan")
        expected_role = "training" if source_split == "train" else "validation"
        if window.get("training_plan_role") != expected_role:
            raise Phase4TraceSamplingError("{0}: source split and plan role mismatch".format(window_id))

        leakage_group = str(window.get("leakage_group"))
        previous_split = group_to_split.get(leakage_group)
        if previous_split is not None and previous_split != source_split:
            raise Phase4TraceSamplingError("{0}: leakage_group selected across splits".format(leakage_group))
        group_to_split[leakage_group] = source_split

    model_feature_fields = set(str(field) for field in training_plan.get("model_feature_fields", ()))
    forbidden = model_feature_fields.intersection(PROHIBITED_MODEL_FEATURE_FIELDS)
    if forbidden:
        raise Phase4TraceSamplingError(
            "prohibited metadata fields exposed as model features: {0}".format(", ".join(sorted(forbidden)))
        )

    _assert_selection_caps(training_windows, active_config.train_window_count, active_config, "training")
    _assert_selection_caps(validation_windows, active_config.validation_window_count, active_config, "validation")
    return {
        "status": "PASS",
        "training_window_count": len(training_windows),
        "validation_window_count": len(validation_windows),
        "selected_window_count": len(selected),
    }


def load_phase4_training_trace_plan(path: str | Path) -> dict[str, object]:
    plan_path = Path(path)
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    validate_phase4_training_trace_plan(plan)
    return plan


def _validated_phase3_traces(phase3_manifest: Mapping[str, object]) -> list[Mapping[str, object]]:
    if phase3_manifest.get("schema_id") != "phase3_trace_manifest_final_v1":
        raise Phase4TraceSamplingError("source manifest must be phase3_trace_manifest_final_v1")
    if phase3_manifest.get("benchmark_authorized") is not False:
        raise Phase4TraceSamplingError("source manifest benchmark_authorized must be false")
    traces = phase3_manifest.get("traces")
    if not isinstance(traces, list):
        raise Phase4TraceSamplingError("source manifest traces must be a list")
    if int(phase3_manifest.get("trace_count", -1)) != len(traces):
        raise Phase4TraceSamplingError("source manifest trace_count mismatch")

    group_to_split: dict[str, str] = {}
    for index, trace in enumerate(traces):
        if not isinstance(trace, Mapping):
            raise Phase4TraceSamplingError("trace {0} must be an object".format(index))
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
                raise Phase4TraceSamplingError("trace {0}: missing {1}".format(index, field))
        split = str(trace["split"])
        if split not in {"train", "test", "eval"}:
            raise Phase4TraceSamplingError("{0}: invalid split {1}".format(trace["trace_id"], split))
        group = str(trace["leakage_group"])
        previous_split = group_to_split.get(group)
        if previous_split is not None and previous_split != split:
            raise Phase4TraceSamplingError("{0}: leakage_group spans splits".format(group))
        group_to_split[group] = split
    return traces


def _build_trace_windows(
    traces: Sequence[Mapping[str, object]],
    config: Phase4SamplingConfig,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    windows: list[dict[str, object]] = []
    excluded_counts: Counter[str] = Counter()
    excluded_by_split: Counter[str] = Counter()
    eval_eligible_windows = 0
    eval_eligible_traces = 0

    for trace in traces:
        split = str(trace["split"])
        if split == "eval":
            possible_windows = _window_count_for_trace(trace, config)
            if possible_windows > 0:
                eval_eligible_traces += 1
                eval_eligible_windows += possible_windows
            excluded_counts["eval_split_reserved_for_future_evaluation"] += 1
            excluded_by_split[split] += 1
            continue

        role = "training" if split == "train" else "validation"
        if not _trace_allowed_for_role(trace, role):
            excluded_counts["source_trace_not_allowed_for_{0}".format(role)] += 1
            excluded_by_split[split] += 1
            continue

        trace_window_count = _window_count_for_trace(trace, config)
        if trace_window_count <= 0:
            excluded_counts["trace_shorter_than_window_duration"] += 1
            excluded_by_split[split] += 1
            continue
        for sequence_index in range(trace_window_count):
            windows.append(_window_record(trace, role, sequence_index, trace_window_count, config))

    windows.sort(key=lambda item: str(item["window_id"]))
    return windows, {
        "excluded_trace_counts_by_reason": dict(sorted(excluded_counts.items())),
        "excluded_trace_counts_by_source_split": dict(sorted(excluded_by_split.items())),
        "eval_split_reserved_for_future_evaluation": True,
        "eval_eligible_trace_count": eval_eligible_traces,
        "eval_eligible_window_count": eval_eligible_windows,
    }


def _trace_allowed_for_role(trace: Mapping[str, object], role: str) -> bool:
    if role == "training":
        return trace.get("usable_for_training", True) is not False
    if role == "validation":
        return trace.get("usable_for_eval", True) is not False
    return False


def _window_count_for_trace(trace: Mapping[str, object], config: Phase4SamplingConfig) -> int:
    try:
        duration_s = float(trace["duration_s"])
    except (TypeError, ValueError) as exc:
        raise Phase4TraceSamplingError("{0}: invalid duration_s".format(trace.get("trace_id"))) from exc
    if duration_s < config.window_duration_s:
        return 0
    return int(math.floor((duration_s + 1e-9) / config.window_duration_s))


def _window_record(
    trace: Mapping[str, object],
    role: str,
    sequence_index: int,
    trace_window_count: int,
    config: Phase4SamplingConfig,
) -> dict[str, object]:
    start_s = sequence_index * config.window_duration_s
    end_s = start_s + config.window_duration_s
    synthetic = _is_synthetic_trace(trace)
    network_condition = _string_or_unknown(trace.get("network_condition"))
    synthetic_scenario = network_condition if synthetic else None
    trace_id = str(trace["trace_id"])
    return {
        "window_id": _window_id(trace_id, sequence_index, config),
        "trace_id": trace_id,
        "dataset_id": str(trace["dataset_id"]),
        "semantics": str(trace["semantics"]),
        "source_split": str(trace["split"]),
        "training_plan_role": role,
        "group_id": str(trace["group_id"]),
        "leakage_group": str(trace["leakage_group"]),
        "normalized_trace_path": str(trace["normalized_trace_path"]),
        "metadata_path": str(trace.get("metadata_path", "")),
        "window_sequence_index": sequence_index,
        "window_start_s": _round_seconds(start_s),
        "window_end_s": _round_seconds(end_s),
        "window_duration_s": _round_seconds(config.window_duration_s),
        "segment_duration_s": _round_seconds(config.segment_duration_s),
        "segment_count": int(round(config.window_duration_s / config.segment_duration_s)),
        "trace_window_count": trace_window_count,
        "trace_duration_s": _round_seconds(float(trace["duration_s"])),
        "throughput_mean_kbps": _round_float(float(trace["throughput_mean_kbps"])),
        "throughput_min_kbps": _round_float(float(trace.get("throughput_min_kbps", 0.0))),
        "throughput_max_kbps": _round_float(float(trace.get("throughput_max_kbps", 0.0))),
        "zero_fraction": _round_float(float(trace.get("zero_fraction", 0.0) or 0.0)),
        "difficulty_bucket": _difficulty_bucket(trace),
        "network_condition": network_condition,
        "synthetic": synthetic,
        "synthetic_scenario": synthetic_scenario,
    }


def _select_balanced_windows(
    windows: Sequence[Mapping[str, object]],
    role: str,
    target_count: int,
    config: Phase4SamplingConfig,
) -> dict[str, object]:
    role_windows = [dict(window) for window in windows if window.get("training_plan_role") == role]
    if target_count <= 0:
        return {
            "selected_windows": [],
            "selection_process": {
                "candidate_count": len(role_windows),
                "target_count": target_count,
                "selected_count": 0,
                "rejected_counts_by_reason": {},
            },
        }

    rng = random.Random("{0}:{1}".format(config.seed, role))
    grouped: dict[tuple[str, str, str, str], list[dict[str, object]]] = defaultdict(list)
    for window in role_windows:
        grouped[_selection_group_key(window)].append(window)
    for group_windows in grouped.values():
        rng.shuffle(group_windows)
    active_keys = sorted(grouped)
    rng.shuffle(active_keys)

    selected: list[dict[str, object]] = []
    rejected_counts: Counter[str] = Counter()
    counters = _SelectionCounters()

    while active_keys and len(selected) < target_count:
        next_active_keys: list[tuple[str, str, str, str]] = []
        for key in active_keys:
            candidates = grouped[key]
            if not candidates:
                continue
            window = candidates.pop()
            rejection_reason = _quota_rejection_reason(window, counters, target_count, config)
            if rejection_reason is None:
                selected.append(window)
                counters.add(window)
                if len(selected) >= target_count:
                    break
            else:
                rejected_counts[rejection_reason] += 1
            if candidates:
                next_active_keys.append(key)
        active_keys = next_active_keys

    selected.sort(key=lambda item: str(item["window_id"]))
    return {
        "selected_windows": selected,
        "selection_process": {
            "candidate_count": len(role_windows),
            "target_count": target_count,
            "selected_count": len(selected),
            "unfilled_target_count": max(target_count - len(selected), 0),
            "selection_key": "round_robin_by_semantics_dataset_difficulty_and_synthetic_scenario",
            "rejected_counts_by_reason": dict(sorted(rejected_counts.items())),
        },
    }


@dataclass
class _SelectionCounters:
    total: int = 0
    synthetic: int = 0
    by_dataset: Counter[str] | None = None
    by_semantics: Counter[str] | None = None
    by_difficulty: Counter[str] | None = None
    by_trace: Counter[str] | None = None

    def __post_init__(self) -> None:
        self.by_dataset = Counter()
        self.by_semantics = Counter()
        self.by_difficulty = Counter()
        self.by_trace = Counter()

    def add(self, window: Mapping[str, object]) -> None:
        self.total += 1
        if window.get("synthetic") is True:
            self.synthetic += 1
        self.by_dataset[str(window["dataset_id"])] += 1
        self.by_semantics[str(window["semantics"])] += 1
        self.by_difficulty[str(window["difficulty_bucket"])] += 1
        self.by_trace[str(window["trace_id"])] += 1


def _quota_rejection_reason(
    window: Mapping[str, object],
    counters: _SelectionCounters,
    target_count: int,
    config: Phase4SamplingConfig,
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
    difficulty = str(window["difficulty_bucket"])
    if counters.by_difficulty[difficulty] >= _quota_limit(target_count, config.difficulty_max_fraction):
        return "difficulty_max_fraction_reached"
    return None


def _quota_limit(target_count: int, fraction: float) -> int:
    return max(1, int(math.ceil(float(target_count) * float(fraction))))


def _assert_selection_caps(
    windows: Sequence[Mapping[str, object]],
    target_count: int,
    config: Phase4SamplingConfig,
    label: str,
) -> None:
    if not windows:
        raise Phase4TraceSamplingError("{0}: no selected windows".format(label))
    counts = _count_selected_windows(windows)
    checks = _quota_checks(counts, target_count, config)
    failed = [name for name, item in checks.items() if item["status"] != "PASS"]
    if failed:
        raise Phase4TraceSamplingError("{0}: failed quota checks {1}".format(label, ", ".join(failed)))


def _quota_checks(counts: Mapping[str, object], target_count: int, config: Phase4SamplingConfig) -> dict[str, object]:
    return {
        "synthetic_max_fraction": _fraction_check(
            int(counts["synthetic_count"]),
            target_count,
            config.synthetic_max_fraction,
        ),
        "dataset_max_fraction": _max_counter_fraction_check(
            counts["by_dataset"],
            target_count,
            config.dataset_max_fraction,
        ),
        "semantics_max_fraction": _max_counter_fraction_check(
            counts["by_semantics"],
            target_count,
            config.semantics_max_fraction,
        ),
        "difficulty_max_fraction": _max_counter_fraction_check(
            counts["by_difficulty"],
            target_count,
            config.difficulty_max_fraction,
        ),
    }


def _fraction_check(count: int, target_count: int, max_fraction: float) -> dict[str, object]:
    limit = _quota_limit(target_count, max_fraction)
    return {
        "status": "PASS" if count <= limit else "FAIL",
        "count": count,
        "limit": limit,
        "max_fraction": max_fraction,
        "observed_fraction_of_target": _round_float(count / target_count if target_count else 0.0),
    }


def _max_counter_fraction_check(counter_data: object, target_count: int, max_fraction: float) -> dict[str, object]:
    counter = Counter(counter_data or {})
    if not counter:
        return _fraction_check(0, target_count, max_fraction)
    name, count = counter.most_common(1)[0]
    check = _fraction_check(count, target_count, max_fraction)
    check["largest_bucket"] = name
    return check


def _count_selected_windows(windows: Sequence[Mapping[str, object]]) -> dict[str, object]:
    by_dataset = Counter(str(window["dataset_id"]) for window in windows)
    by_semantics = Counter(str(window["semantics"]) for window in windows)
    by_difficulty = Counter(str(window["difficulty_bucket"]) for window in windows)
    by_network_condition = Counter(str(window["network_condition"]) for window in windows)
    by_synthetic_scenario = Counter(
        str(window["synthetic_scenario"]) for window in windows if window.get("synthetic") is True
    )
    return {
        "total_count": len(windows),
        "synthetic_count": sum(1 for window in windows if window.get("synthetic") is True),
        "real_trace_count": sum(1 for window in windows if window.get("synthetic") is not True),
        "by_dataset": dict(sorted(by_dataset.items())),
        "by_semantics": dict(sorted(by_semantics.items())),
        "by_difficulty": dict(sorted(by_difficulty.items())),
        "by_network_condition": dict(sorted(by_network_condition.items())),
        "by_synthetic_scenario": dict(sorted(by_synthetic_scenario.items())),
    }


def _selection_summary(
    selected_windows: Sequence[Mapping[str, object]],
    target_count: int,
    config: Phase4SamplingConfig,
) -> dict[str, object]:
    counts = _count_selected_windows(selected_windows)
    return {
        "target_count": target_count,
        "selected_count": len(selected_windows),
        "unfilled_target_count": max(target_count - len(selected_windows), 0),
        "counts": counts,
        "quota_checks": _quota_checks(counts, target_count, config),
    }


def _summarize_windows(windows: Sequence[Mapping[str, object]]) -> dict[str, object]:
    by_role = Counter(str(window["training_plan_role"]) for window in windows)
    by_source_split = Counter(str(window["source_split"]) for window in windows)
    by_dataset = Counter(str(window["dataset_id"]) for window in windows)
    by_semantics = Counter(str(window["semantics"]) for window in windows)
    by_difficulty = Counter(str(window["difficulty_bucket"]) for window in windows)
    return {
        "total_candidate_window_count": len(windows),
        "by_training_plan_role": dict(sorted(by_role.items())),
        "by_source_split": dict(sorted(by_source_split.items())),
        "by_dataset": dict(sorted(by_dataset.items())),
        "by_semantics": dict(sorted(by_semantics.items())),
        "by_difficulty": dict(sorted(by_difficulty.items())),
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
            previous = group_to_role.get(group)
            if previous is not None and previous != role:
                conflicts.append(group)
            group_to_role[group] = role
    return {
        "status": "PASS" if not conflicts else "FAIL",
        "checked_leakage_group_count": len(group_to_role),
        "conflicting_leakage_groups": sorted(set(conflicts)),
        "eval_split_selected": False,
    }


def _common_contract(
    config: Phase4SamplingConfig,
    phase3_manifest: Mapping[str, object],
    source_manifest_path: str | None,
    generated_at_utc: str,
) -> dict[str, object]:
    return {
        "phase": PHASE4A_PHASE,
        "generated_at_utc": generated_at_utc,
        "source_phase3_manifest_path": source_manifest_path,
        "source_phase3_schema_id": phase3_manifest.get("schema_id"),
        "source_phase3_artifact_set": phase3_manifest.get("artifact_set"),
        "source_phase3_trace_count": phase3_manifest.get("trace_count"),
        "source_phase3_split_counts": phase3_manifest.get("split_counts"),
        "source_phase3_semantics_counts": phase3_manifest.get("semantics_counts"),
        "sampling_policy": _config_to_dict(config),
        "segment_duration_policy": {
            "primary_segment_duration_s": config.segment_duration_s,
            "primary_reason": "4s is the Phase 4A primary target for stable CPU-first offline training",
            "diagnostic_only_segment_duration_s": 2.0,
        },
        "model_input_policy": {
            "plan_artifacts_are_model_inputs": False,
            "metadata_fields_not_allowed_as_model_features": list(PROHIBITED_MODEL_FEATURE_FIELDS),
        },
        **_no_benchmark_policy(),
    }


def _config_to_dict(config: Phase4SamplingConfig) -> dict[str, object]:
    return {
        "segment_duration_s": config.segment_duration_s,
        "window_duration_s": config.window_duration_s,
        "train_window_count": config.train_window_count,
        "validation_window_count": config.validation_window_count,
        "synthetic_max_fraction": config.synthetic_max_fraction,
        "dataset_max_fraction": config.dataset_max_fraction,
        "semantics_max_fraction": config.semantics_max_fraction,
        "difficulty_max_fraction": config.difficulty_max_fraction,
        "max_windows_per_trace": config.max_windows_per_trace,
        "seed": config.seed,
    }


def _config_from_plan(plan: Mapping[str, object]) -> Phase4SamplingConfig:
    policy = plan.get("sampling_policy")
    if not isinstance(policy, Mapping):
        raise Phase4TraceSamplingError("training plan missing sampling_policy")
    return Phase4SamplingConfig(
        segment_duration_s=float(policy["segment_duration_s"]),
        window_duration_s=float(policy["window_duration_s"]),
        train_window_count=int(policy["train_window_count"]),
        validation_window_count=int(policy["validation_window_count"]),
        synthetic_max_fraction=float(policy["synthetic_max_fraction"]),
        dataset_max_fraction=float(policy["dataset_max_fraction"]),
        semantics_max_fraction=float(policy["semantics_max_fraction"]),
        difficulty_max_fraction=float(policy["difficulty_max_fraction"]),
        max_windows_per_trace=int(policy["max_windows_per_trace"]),
        seed=str(policy["seed"]),
    )


def _no_benchmark_policy() -> dict[str, object]:
    return {
        "benchmark_performed": False,
        "outputs_are_benchmark_results": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": False,
        "qoe_claims_authorized": False,
    }


def _assert_no_benchmark_flags(mapping: Mapping[str, object]) -> None:
    for flag, expected in _no_benchmark_policy().items():
        if mapping.get(flag) is not expected:
            raise Phase4TraceSamplingError("{0} must be {1}".format(flag, expected))


def _require_window_list(plan: Mapping[str, object], field: str) -> list[Mapping[str, object]]:
    value = plan.get(field)
    if not isinstance(value, list):
        raise Phase4TraceSamplingError("{0} must be a list".format(field))
    for index, item in enumerate(value):
        if not isinstance(item, Mapping):
            raise Phase4TraceSamplingError("{0}[{1}] must be an object".format(field, index))
    return value


def _validate_config(config: Phase4SamplingConfig) -> None:
    for field, value in (
        ("segment_duration_s", config.segment_duration_s),
        ("window_duration_s", config.window_duration_s),
    ):
        if isinstance(value, bool) or not math.isfinite(float(value)) or float(value) <= 0:
            raise Phase4TraceSamplingError("{0} must be positive".format(field))
    segment_ratio = config.window_duration_s / config.segment_duration_s
    if abs(segment_ratio - round(segment_ratio)) > 1e-9:
        raise Phase4TraceSamplingError("window_duration_s must be an exact multiple of segment_duration_s")
    for field, value in (
        ("train_window_count", config.train_window_count),
        ("validation_window_count", config.validation_window_count),
        ("max_windows_per_trace", config.max_windows_per_trace),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise Phase4TraceSamplingError("{0} must be a positive integer".format(field))
    for field, value in (
        ("synthetic_max_fraction", config.synthetic_max_fraction),
        ("dataset_max_fraction", config.dataset_max_fraction),
        ("semantics_max_fraction", config.semantics_max_fraction),
        ("difficulty_max_fraction", config.difficulty_max_fraction),
    ):
        if isinstance(value, bool) or not math.isfinite(float(value)) or not 0.0 < float(value) <= 1.0:
            raise Phase4TraceSamplingError("{0} must be in (0, 1]".format(field))
    if not str(config.seed):
        raise Phase4TraceSamplingError("seed must not be empty")


def _selection_group_key(window: Mapping[str, object]) -> tuple[str, str, str, str]:
    synthetic_scenario = str(window["synthetic_scenario"]) if window.get("synthetic_scenario") is not None else "real_trace"
    return (
        str(window["semantics"]),
        str(window["dataset_id"]),
        str(window["difficulty_bucket"]),
        synthetic_scenario,
    )


def _difficulty_bucket(trace: Mapping[str, object]) -> str:
    zero_fraction = float(trace.get("zero_fraction", 0.0) or 0.0)
    throughput_mean_kbps = float(trace["throughput_mean_kbps"])
    if zero_fraction >= 0.10:
        return "intermittent_or_zero_heavy"
    if throughput_mean_kbps < 750.0:
        return "very_low_capacity"
    if throughput_mean_kbps < 1850.0:
        return "low_capacity"
    if throughput_mean_kbps < 4300.0:
        return "medium_capacity"
    return "high_capacity"


def _is_synthetic_trace(trace: Mapping[str, object]) -> bool:
    return trace.get("synthetic") is True or str(trace.get("dataset_id")) == "synthetic_controlled_network"


def _window_id(trace_id: str, sequence_index: int, config: Phase4SamplingConfig) -> str:
    readable = _safe_id(trace_id)
    digest = hashlib.sha256(
        "{0}|{1}|{2}|{3}".format(trace_id, sequence_index, config.window_duration_s, config.segment_duration_s).encode(
            "utf-8"
        )
    ).hexdigest()[:12]
    start_s = int(round(sequence_index * config.window_duration_s))
    duration_s = int(round(config.window_duration_s))
    return "{0}__window_start_{1:06d}s_duration_{2:03d}s__{3}".format(readable, start_s, duration_s, digest)


def _safe_id(value: str) -> str:
    chars = []
    for char in value:
        if char.isalnum() or char in ("-", "_"):
            chars.append(char)
        else:
            chars.append("_")
    safe = "".join(chars).strip("_")
    if len(safe) > 80:
        safe = safe[:80].rstrip("_")
    return safe or "trace"


def _string_or_unknown(value: object) -> str:
    if value is None:
        return "unknown"
    text = str(value).strip()
    return text if text else "unknown"


def _round_seconds(value: float) -> float:
    return round(float(value), 6)


def _round_float(value: float) -> float:
    return round(float(value), 6)
