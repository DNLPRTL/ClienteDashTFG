from __future__ import annotations

import csv
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Mapping


DEFAULT_MIN_SAMPLES = 30
DEFAULT_MIN_DURATION_S = 30.0
DEFAULT_MOSTLY_ZERO_THRESHOLD = 0.5
DEFAULT_EXTREME_THROUGHPUT_KBPS = 1_000_000.0


@dataclass(frozen=True)
class TraceQualityPolicy:
    min_samples: int = DEFAULT_MIN_SAMPLES
    min_duration_s: float = DEFAULT_MIN_DURATION_S
    mostly_zero_threshold: float = DEFAULT_MOSTLY_ZERO_THRESHOLD
    extreme_throughput_kbps: float = DEFAULT_EXTREME_THROUGHPUT_KBPS

    def as_dict(self) -> dict[str, float | int | str]:
        return {
            "policy_id": "phase3_trace_quality_policy_v1",
            "min_samples": self.min_samples,
            "min_duration_s": self.min_duration_s,
            "mostly_zero_threshold": self.mostly_zero_threshold,
            "extreme_throughput_kbps": self.extreme_throughput_kbps,
            "exclusion_rule": "exclude only traces with too few samples, too little duration, or all-zero throughput",
            "retention_rule": "keep poor/intermittent network traces when they have enough temporal signal and any positive throughput",
        }


@dataclass(frozen=True)
class TraceQualityAssessment:
    trace_id: str
    dataset_id: str
    semantics: str
    split: str
    row_count: int
    duration_s: float
    throughput_mean_kbps: float
    throughput_max_kbps: float
    zero_fraction: float
    quality_flags: tuple[str, ...]
    exclusion_reasons: tuple[str, ...]
    usable_for_training: bool
    usable_for_eval: bool
    network_condition: str

    def as_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["quality_flags"] = list(self.quality_flags)
        data["exclusion_reasons"] = list(self.exclusion_reasons)
        return data


def assess_trace_quality(
    trace: Mapping[str, object],
    policy: TraceQualityPolicy | None = None,
) -> TraceQualityAssessment:
    policy = policy or TraceQualityPolicy()
    row_count = int(trace["row_count"])
    duration_s = float(trace["duration_s"])
    throughput_mean_kbps = float(trace["throughput_mean_kbps"])
    throughput_max_kbps = float(trace["throughput_max_kbps"])
    zero_fraction = compute_zero_fraction(Path(str(trace["normalized_trace_path"])))

    flags: list[str] = []
    exclusion_reasons: list[str] = []
    if row_count < policy.min_samples:
        flags.append("short_trace_samples")
        exclusion_reasons.append("row_count_lt_{0}".format(policy.min_samples))
    if duration_s < policy.min_duration_s:
        flags.append("short_trace_duration")
        exclusion_reasons.append("duration_s_lt_{0:g}".format(policy.min_duration_s))
    if throughput_max_kbps <= 0 or throughput_mean_kbps <= 0:
        flags.append("all_zero_throughput")
        exclusion_reasons.append("all_zero_throughput")
    if zero_fraction > policy.mostly_zero_threshold:
        flags.append("mostly_zero_intermitent_or_severe_network")
    if throughput_max_kbps > policy.extreme_throughput_kbps:
        flags.append("extreme_throughput_value")
    if throughput_mean_kbps < 1000 and throughput_max_kbps > 0:
        flags.append("low_bandwidth_trace")

    usable = not exclusion_reasons
    return TraceQualityAssessment(
        trace_id=str(trace["trace_id"]),
        dataset_id=str(trace["dataset_id"]),
        semantics=str(trace["semantics"]),
        split=str(trace["split"]),
        row_count=row_count,
        duration_s=duration_s,
        throughput_mean_kbps=throughput_mean_kbps,
        throughput_max_kbps=throughput_max_kbps,
        zero_fraction=zero_fraction,
        quality_flags=tuple(flags),
        exclusion_reasons=tuple(exclusion_reasons),
        usable_for_training=usable,
        usable_for_eval=usable,
        network_condition=_network_condition(flags, usable),
    )


def compute_zero_fraction(path: Path) -> float:
    rows = 0
    zeros = 0
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows += 1
            if float(row["throughput_kbps"]) == 0.0:
                zeros += 1
    if rows == 0:
        return 1.0
    return zeros / rows


def build_quality_audit(
    manifest: Mapping[str, object],
    policy: TraceQualityPolicy | None = None,
) -> tuple[dict[str, object], dict[str, object]]:
    policy = policy or TraceQualityPolicy()
    kept_traces: list[dict[str, object]] = []
    excluded_traces: list[dict[str, object]] = []
    assessments: list[dict[str, object]] = []
    flag_counts: Counter[str] = Counter()
    exclusion_counts: Counter[str] = Counter()

    for trace in manifest["traces"]:
        assessment = assess_trace_quality(trace, policy=policy)
        assessment_dict = assessment.as_dict()
        assessments.append(assessment_dict)
        flag_counts.update(assessment.quality_flags)
        exclusion_counts.update(assessment.exclusion_reasons)
        enriched_trace = dict(trace)
        enriched_trace.update(
            {
                "quality_flags": list(assessment.quality_flags),
                "zero_fraction": assessment.zero_fraction,
                "usable_for_training": assessment.usable_for_training,
                "usable_for_eval": assessment.usable_for_eval,
                "network_condition": assessment.network_condition,
            }
        )
        if assessment.usable_for_training and assessment.usable_for_eval:
            kept_traces.append(enriched_trace)
        else:
            enriched_trace["quality_exclusion_reasons"] = list(assessment.exclusion_reasons)
            excluded_traces.append(enriched_trace)

    audit = {
        "schema_id": "phase3_trace_quality_audit_v1",
        "source_manifest_trace_count": len(manifest["traces"]),
        "quality_policy": policy.as_dict(),
        "kept_trace_count": len(kept_traces),
        "excluded_trace_count": len(excluded_traces),
        "quality_flag_counts": dict(sorted(flag_counts.items())),
        "quality_exclusion_counts": dict(sorted(exclusion_counts.items())),
        "assessments": assessments,
    }
    curated_manifest = build_curated_manifest(manifest, kept_traces, excluded_traces, audit)
    return audit, curated_manifest


def build_curated_manifest(
    manifest: Mapping[str, object],
    kept_traces: Iterable[Mapping[str, object]],
    excluded_traces: Iterable[Mapping[str, object]],
    audit: Mapping[str, object],
) -> dict[str, object]:
    kept = [dict(trace) for trace in kept_traces]
    excluded = [dict(trace) for trace in excluded_traces]
    split_counts = _counter_dict((trace["split"] for trace in kept), ("train", "test", "eval"))
    semantics_counts = _counter_dict(trace["semantics"] for trace in kept)
    curated = dict(manifest)
    curated.update(
        {
            "artifact_set": "{0}_quality_curated".format(manifest.get("artifact_set", "final")),
            "quality_curated": True,
            "quality_policy": audit["quality_policy"],
            "source_manifest_trace_count": len(manifest["traces"]),
            "trace_count": len(kept),
            "quality_excluded_count": len(excluded),
            "split_counts": split_counts,
            "semantics_counts": semantics_counts,
            "traces": sorted(kept, key=lambda item: str(item["trace_id"])),
            "quality_excluded_traces": sorted(excluded, key=lambda item: str(item["trace_id"])),
        }
    )
    return curated


def _counter_dict(values: Iterable[object], required_keys: tuple[str, ...] = ()) -> dict[str, int]:
    counts = Counter(str(value) for value in values)
    output = {key: counts.get(key, 0) for key in required_keys}
    for key in sorted(counts):
        if key not in output:
            output[key] = counts[key]
    return output


def _network_condition(flags: Iterable[str], usable: bool) -> str:
    flag_set = set(flags)
    if not usable:
        return "no_useful_signal"
    if "mostly_zero_intermitent_or_severe_network" in flag_set:
        return "severe_or_intermittent_network"
    if "low_bandwidth_trace" in flag_set:
        return "low_bandwidth_network"
    if "extreme_throughput_value" in flag_set:
        return "high_or_extreme_throughput_network"
    return "usable_network_trace"
