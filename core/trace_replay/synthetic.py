from __future__ import annotations

import hashlib
import json
import math
import random
import shutil
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

from core.trace_replay.converters.base import ConversionResult
from core.trace_replay.converters.common import sha256_file, stable_id, write_normalized_csv
from core.trace_replay.splits import stable_group_sort_key


SYNTHETIC_DATASET_ID = "synthetic_controlled_network"
SYNTHETIC_GENERATOR_ID = "phase3_synthetic_controlled_network_v1"
SYNTHETIC_SEMANTICS = "synthetic_available_bandwidth"
SYNTHETIC_INTENDED_USE = "controlled_train_test_eval"
DEFAULT_SYNTHETIC_SEED = "phase3_synthetic_controlled_v1"
DEFAULT_SYNTHETIC_TRACE_DURATION_S = 300
DEFAULT_SYNTHETIC_SAMPLE_DURATION_S = 1.0
DEFAULT_SYNTHETIC_COUNT_PER_SCENARIO = 128


SCENARIO_IDS = (
    "synthetic_perfect_high",
    "synthetic_stable_low",
    "synthetic_sudden_drop",
    "synthetic_sudden_recovery",
    "synthetic_mobile_variable",
    "synthetic_periodic_oscillation",
    "synthetic_stall_trap",
    "synthetic_high_jitter",
)


@dataclass(frozen=True)
class SyntheticTraceSourceSpec:
    schema_id: str
    dataset_id: str
    generator_id: str
    synthetic: bool
    synthetic_scenario: str
    trace_index: int
    generator_seed: str
    duration_s: int
    sample_duration_s: float
    row_count: int
    intended_use: str
    parameters: dict[str, object]


def scenario_ids() -> tuple[str, ...]:
    return SCENARIO_IDS


def generate_synthetic_trace_rows(
    scenario_id: str,
    trace_index: int,
    duration_s: int = DEFAULT_SYNTHETIC_TRACE_DURATION_S,
    sample_duration_s: float = DEFAULT_SYNTHETIC_SAMPLE_DURATION_S,
    seed: str = DEFAULT_SYNTHETIC_SEED,
) -> tuple[list[dict[str, float]], SyntheticTraceSourceSpec]:
    _validate_generation_inputs(scenario_id, trace_index, duration_s, sample_duration_s)
    row_count = int(round(duration_s / sample_duration_s))
    rng = _scenario_rng(seed, scenario_id, trace_index)
    values, parameters = _scenario_values(scenario_id, row_count, rng)
    rows = [
        {
            "timestamp_s": float(index) * sample_duration_s,
            "duration_s": sample_duration_s,
            "throughput_kbps": _clamp(float(value), 0.0, 25000.0),
        }
        for index, value in enumerate(values)
    ]
    source_spec = SyntheticTraceSourceSpec(
        schema_id="synthetic_trace_source_spec_v1",
        dataset_id=SYNTHETIC_DATASET_ID,
        generator_id=SYNTHETIC_GENERATOR_ID,
        synthetic=True,
        synthetic_scenario=scenario_id,
        trace_index=trace_index,
        generator_seed=seed,
        duration_s=duration_s,
        sample_duration_s=sample_duration_s,
        row_count=row_count,
        intended_use=SYNTHETIC_INTENDED_USE,
        parameters=parameters,
    )
    return rows, source_spec


def generate_synthetic_trace_set(
    normalized_root: str | Path,
    metadata_root: str | Path,
    count_per_scenario: int = DEFAULT_SYNTHETIC_COUNT_PER_SCENARIO,
    duration_s: int = DEFAULT_SYNTHETIC_TRACE_DURATION_S,
    sample_duration_s: float = DEFAULT_SYNTHETIC_SAMPLE_DURATION_S,
    seed: str = DEFAULT_SYNTHETIC_SEED,
    train_ratio: float = 0.7,
    test_ratio: float = 0.15,
    clean: bool = False,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    if count_per_scenario <= 0:
        raise ValueError("count_per_scenario must be > 0")
    normalized_base = Path(normalized_root) / "schema_v1" / SYNTHETIC_DATASET_ID
    metadata_base = Path(metadata_root) / "traces" / SYNTHETIC_DATASET_ID
    source_base = Path(metadata_root) / "synthetic_sources" / SYNTHETIC_DATASET_ID
    if clean:
        for target in (normalized_base, metadata_base, source_base):
            _clean_generated_dir(target)

    entries: list[dict[str, object]] = []
    for scenario_id in SCENARIO_IDS:
        scenario_entries: list[dict[str, object]] = []
        for trace_index in range(count_per_scenario):
            rows, source_spec = generate_synthetic_trace_rows(
                scenario_id=scenario_id,
                trace_index=trace_index,
                duration_s=duration_s,
                sample_duration_s=sample_duration_s,
                seed=seed,
            )
            scenario_slug = scenario_id.replace("synthetic_", "")
            group_id = "{0}:{1}:{2:04d}".format(SYNTHETIC_DATASET_ID, scenario_id, trace_index)
            leakage_group = group_id
            trace_id = stable_id(
                SYNTHETIC_DATASET_ID,
                scenario_slug,
                "{0:04d}".format(trace_index),
                seed,
                prefix="trace",
            )
            source_path = source_base / scenario_id / "{0}.json".format(trace_id)
            source_path.parent.mkdir(parents=True, exist_ok=True)
            source_path.write_text(
                json.dumps(asdict(source_spec), indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            normalized_path = normalized_base / scenario_id / "{0}.csv".format(trace_id)
            stats = write_normalized_csv(rows, normalized_path)
            metadata_path = metadata_base / scenario_id / "{0}.json".format(trace_id)
            result = ConversionResult(
                trace_id=trace_id,
                dataset_id=SYNTHETIC_DATASET_ID,
                converter_id=SYNTHETIC_GENERATOR_ID,
                normalized_trace_path=str(normalized_path),
                metadata_path=str(metadata_path),
                source_path=str(source_path),
                source_sha256=sha256_file(source_path),
                group_id=group_id,
                leakage_group=leakage_group,
                semantics=SYNTHETIC_SEMANTICS,
                row_count=int(stats["row_count"]),
                duration_s=float(stats["duration_s"]),
                throughput_min_kbps=float(stats["throughput_min_kbps"]),
                throughput_mean_kbps=float(stats["throughput_mean_kbps"]),
                throughput_max_kbps=float(stats["throughput_max_kbps"]),
                content_fingerprint_sha256=str(stats["content_fingerprint_sha256"]),
                parse_warnings=(),
            )
            entry = result.as_manifest_entry()
            entry.update(
                {
                    "synthetic": True,
                    "synthetic_scenario": scenario_id,
                    "generator_seed": seed,
                    "generator_version": SYNTHETIC_GENERATOR_ID,
                    "intended_use": SYNTHETIC_INTENDED_USE,
                    "sample_duration_s": sample_duration_s,
                }
            )
            scenario_entries.append(entry)
        _assign_scenario_splits(scenario_entries, train_ratio=train_ratio, test_ratio=test_ratio, seed=seed)
        for entry in scenario_entries:
            metadata_path = Path(str(entry["metadata_path"]))
            metadata_path.parent.mkdir(parents=True, exist_ok=True)
            metadata_path.write_text(json.dumps(entry, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        entries.extend(scenario_entries)

    report = {
        "schema_id": "phase3_synthetic_trace_generation_report_v1",
        "dataset_id": SYNTHETIC_DATASET_ID,
        "generator_id": SYNTHETIC_GENERATOR_ID,
        "semantics": SYNTHETIC_SEMANTICS,
        "synthetic": True,
        "seed": seed,
        "duration_s": duration_s,
        "sample_duration_s": sample_duration_s,
        "count_per_scenario": count_per_scenario,
        "trace_count": len(entries),
        "scenario_counts": dict(sorted(Counter(entry["synthetic_scenario"] for entry in entries).items())),
        "split_counts": _counter_dict(entry["split"] for entry in entries),
        "split_counts_by_scenario": _split_counts_by_scenario(entries),
        "normalized_root": str(normalized_base),
        "metadata_root": str(metadata_base),
        "source_root": str(source_base),
        "ready_for_benchmark": False,
        "benchmark_authorized": False,
        "outputs_are_benchmark_results": False,
    }
    return sorted(entries, key=lambda item: str(item["trace_id"])), report


def merge_synthetic_entries_into_manifest(
    base_manifest: dict[str, object],
    synthetic_entries: Sequence[dict[str, object]],
    artifact_set: str = "final_with_synthetic_controlled",
) -> dict[str, object]:
    real_traces = [
        dict(trace)
        for trace in base_manifest["traces"]
        if str(trace.get("dataset_id")) != SYNTHETIC_DATASET_ID
    ]
    merged_traces = real_traces + [dict(trace) for trace in synthetic_entries]
    split_counts = _counter_dict(trace["split"] for trace in merged_traces)
    semantics_counts = _counter_dict(trace["semantics"] for trace in merged_traces)
    leakage_group_counts = _counter_dict(trace["leakage_group"] for trace in merged_traces)
    scenario_counts = _counter_dict(trace["synthetic_scenario"] for trace in synthetic_entries)
    merged = dict(base_manifest)
    merged.update(
        {
            "artifact_set": artifact_set,
            "synthetic_addendum": {
                "dataset_id": SYNTHETIC_DATASET_ID,
                "generator_id": SYNTHETIC_GENERATOR_ID,
                "semantics": SYNTHETIC_SEMANTICS,
                "synthetic": True,
                "trace_count": len(synthetic_entries),
                "scenario_counts": scenario_counts,
                "split_counts": _counter_dict(trace["split"] for trace in synthetic_entries),
                "intended_use": SYNTHETIC_INTENDED_USE,
                "real_world_generalization_claims_authorized": False,
                "must_report_separately_from_real_traces": True,
            },
            "trace_count": len(merged_traces),
            "split_counts": split_counts,
            "semantics_counts": semantics_counts,
            "leakage_group_counts": leakage_group_counts,
            "traces": sorted(merged_traces, key=lambda item: str(item["trace_id"])),
        }
    )
    return merged


def _scenario_values(scenario_id: str, row_count: int, rng: random.Random) -> tuple[list[float], dict[str, object]]:
    if scenario_id == "synthetic_perfect_high":
        base = rng.uniform(9000.0, 12000.0)
        return [base] * row_count, {"base_kbps": base}
    if scenario_id == "synthetic_stable_low":
        base = rng.uniform(450.0, 900.0)
        return [base] * row_count, {"base_kbps": base}
    if scenario_id == "synthetic_sudden_drop":
        high = rng.uniform(7000.0, 10000.0)
        low = rng.uniform(350.0, 900.0)
        drop_at = rng.randint(max(10, row_count // 4), max(11, (row_count * 3) // 4))
        return [high if index < drop_at else low for index in range(row_count)], {
            "high_kbps": high,
            "low_kbps": low,
            "drop_at_s": drop_at,
        }
    if scenario_id == "synthetic_sudden_recovery":
        low = rng.uniform(350.0, 900.0)
        high = rng.uniform(6000.0, 10000.0)
        recovery_at = rng.randint(max(10, row_count // 4), max(11, (row_count * 3) // 4))
        return [low if index < recovery_at else high for index in range(row_count)], {
            "low_kbps": low,
            "high_kbps": high,
            "recovery_at_s": recovery_at,
        }
    if scenario_id == "synthetic_mobile_variable":
        return _markovian_mobile_values(row_count, rng)
    if scenario_id == "synthetic_periodic_oscillation":
        low = rng.uniform(600.0, 1200.0)
        high = rng.uniform(6500.0, 9500.0)
        period = rng.randint(24, 60)
        values = []
        for index in range(row_count):
            wave = (math.sin((2.0 * math.pi * index) / period) + 1.0) / 2.0
            values.append(low + (high - low) * wave)
        return values, {"low_kbps": low, "high_kbps": high, "period_s": period}
    if scenario_id == "synthetic_stall_trap":
        base = rng.uniform(4000.0, 4200.0)
        values = [_clamp(rng.gauss(base, 35.0), 3800.0, 4290.0) for _ in range(row_count)]
        return values, {"base_kbps": base, "target_representation_kbps": 4300}
    if scenario_id == "synthetic_high_jitter":
        base = rng.uniform(3800.0, 5500.0)
        values = []
        for _ in range(row_count):
            draw = rng.gauss(base, base * 0.55)
            if rng.random() < 0.08:
                draw *= rng.uniform(0.12, 0.35)
            elif rng.random() < 0.08:
                draw *= rng.uniform(1.8, 2.8)
            values.append(_clamp(draw, 100.0, 14000.0))
        return values, {"base_kbps": base, "jitter_model": "gaussian_with_spikes_and_drops"}
    raise ValueError("unknown synthetic scenario: {0}".format(scenario_id))


def _markovian_mobile_values(row_count: int, rng: random.Random) -> tuple[list[float], dict[str, object]]:
    states = {
        "low": (350.0, 1200.0),
        "medium": (1500.0, 3800.0),
        "high": (4500.0, 8500.0),
        "burst": (9000.0, 13000.0),
    }
    transitions = {
        "low": (("low", 0.55), ("medium", 0.35), ("high", 0.08), ("burst", 0.02)),
        "medium": (("low", 0.18), ("medium", 0.52), ("high", 0.25), ("burst", 0.05)),
        "high": (("low", 0.07), ("medium", 0.22), ("high", 0.55), ("burst", 0.16)),
        "burst": (("low", 0.10), ("medium", 0.20), ("high", 0.45), ("burst", 0.25)),
    }
    current = rng.choice(tuple(states))
    observed_states = []
    values = []
    for _ in range(row_count):
        current = _choose_state(rng, transitions[current])
        observed_states.append(current)
        low, high = states[current]
        values.append(rng.uniform(low, high))
    return values, {
        "model": "markovian_state_average_throughput",
        "states": states,
        "transition_probabilities": transitions,
        "observed_state_counts": dict(sorted(Counter(observed_states).items())),
    }


def _choose_state(rng: random.Random, transitions: Sequence[tuple[str, float]]) -> str:
    draw = rng.random()
    cumulative = 0.0
    for state, probability in transitions:
        cumulative += probability
        if draw <= cumulative:
            return state
    return transitions[-1][0]


def _assign_scenario_splits(
    entries: list[dict[str, object]],
    train_ratio: float,
    test_ratio: float,
    seed: str,
) -> None:
    groups = sorted(
        {str(entry["leakage_group"]) for entry in entries},
        key=lambda group: stable_group_sort_key(group, seed=seed, namespace=SYNTHETIC_SEMANTICS),
    )
    train_count = round(len(groups) * train_ratio)
    test_count = round(len(groups) * test_ratio)
    if len(groups) >= 3:
        train_count = max(1, min(train_count, len(groups) - 2))
        test_count = max(1, min(test_count, len(groups) - train_count - 1))
    group_to_split = {}
    for index, group in enumerate(groups):
        if index < train_count:
            group_to_split[group] = "train"
        elif index < train_count + test_count:
            group_to_split[group] = "test"
        else:
            group_to_split[group] = "eval"
    for entry in entries:
        entry["split"] = group_to_split[str(entry["leakage_group"])]


def _counter_dict(values: Iterable[object]) -> dict[str, int]:
    return dict(sorted(Counter(str(value) for value in values).items()))


def _split_counts_by_scenario(entries: Sequence[dict[str, object]]) -> dict[str, dict[str, int]]:
    output = {}
    for scenario_id in SCENARIO_IDS:
        scenario_entries = [entry for entry in entries if entry["synthetic_scenario"] == scenario_id]
        output[scenario_id] = _counter_dict(entry["split"] for entry in scenario_entries)
    return output


def _scenario_rng(seed: str, scenario_id: str, trace_index: int) -> random.Random:
    material = "{0}|{1}|{2}".format(seed, scenario_id, trace_index)
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()
    return random.Random(int(digest[:16], 16))


def _validate_generation_inputs(
    scenario_id: str,
    trace_index: int,
    duration_s: int,
    sample_duration_s: float,
) -> None:
    if scenario_id not in SCENARIO_IDS:
        raise ValueError("unknown synthetic scenario: {0}".format(scenario_id))
    if trace_index < 0:
        raise ValueError("trace_index must be >= 0")
    if duration_s <= 0:
        raise ValueError("duration_s must be > 0")
    if sample_duration_s <= 0:
        raise ValueError("sample_duration_s must be > 0")
    row_count = duration_s / sample_duration_s
    if abs(row_count - round(row_count)) > 1e-9:
        raise ValueError("duration_s must be divisible by sample_duration_s")


def _clean_generated_dir(target: Path) -> None:
    if target.exists():
        if target.name != SYNTHETIC_DATASET_ID and target.parent.name != SYNTHETIC_DATASET_ID:
            raise ValueError("refusing to clean unexpected synthetic target: {0}".format(target))
        shutil.rmtree(target)


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))
