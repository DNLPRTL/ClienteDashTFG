#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.trace_replay.converters.puffer import PufferConverter
from core.trace_replay.converters.registry import available_converters, converter_by_id
from core.trace_replay.inventory import build_raw_dataset_inventory, write_raw_dataset_inventory
from core.trace_replay.loader import load_normalized_trace_csv
from core.trace_replay.manifest_validation import validate_phase3_trace_manifest_data
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel, TraceReplayError
from core.trace_replay.splits import build_phase3_trace_manifest


TFG_ROOT = REPO_ROOT.parent
DEFAULT_RAW_ROOT = TFG_ROOT / "dataset en bruto"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run Phase 3 trace closure outside the repository.")
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--artifact-set", default="final")
    parser.add_argument("--hash-mode", choices=("full", "sample", "none"), default="full")
    parser.add_argument("--datasets", nargs="*", choices=available_converters(), default=list(available_converters()))
    parser.add_argument("--puffer-max-sessions", type=int, default=100)
    parser.add_argument("--puffer-min-samples-per-session", type=int, default=30)
    parser.add_argument("--puffer-max-acked-rows", type=int, default=1_000_000)
    parser.add_argument("--puffer-max-sent-rows", type=int, default=2_000_000)
    parser.add_argument("--seed", default="phase3_rebuild_v1")
    parser.add_argument("--train-ratio", type=float, default=0.7)
    parser.add_argument("--test-ratio", type=float, default=0.15)
    parser.add_argument("--clean-derived", action="store_true", help="Remove generated phase3/artifact-set outputs before rebuilding.")
    args = parser.parse_args(argv)

    roots = _external_roots(args.artifact_set)
    if args.clean_derived:
        _clean_derived_roots(roots, args.artifact_set)
    puffer_policy = PufferConverter(
        args.raw_root,
        max_sessions=args.puffer_max_sessions,
        min_samples_per_session=args.puffer_min_samples_per_session,
        max_acked_rows=args.puffer_max_acked_rows,
        max_sent_rows=args.puffer_max_sent_rows,
    ).sampling_policy.as_dict()

    inventory = build_raw_dataset_inventory(args.raw_root, hash_mode=args.hash_mode)
    inventory_path = write_raw_dataset_inventory(inventory, roots["audit"] / "phase3_raw_dataset_inventory.json")

    conversion_manifest = _convert_all(args, roots, puffer_policy)
    conversion_path = roots["manifest"] / "phase3_trace_conversion_manifest.json"
    conversion_path.parent.mkdir(parents=True, exist_ok=True)
    conversion_path.write_text(json.dumps(conversion_manifest, indent=2, sort_keys=True), encoding="utf-8")

    final_manifest = build_phase3_trace_manifest(
        conversion_manifest["traces"],
        seed=args.seed,
        train_ratio=args.train_ratio,
        test_ratio=args.test_ratio,
        artifact_set=args.artifact_set,
        split_strategy="stratified_by_semantics_and_leakage_group",
        puffer_sampling_policy=puffer_policy,
    )
    final_manifest["source_conversion_manifest"] = str(conversion_path)
    final_path = roots["manifest"] / "phase3_trace_manifest_final.json"
    final_path.write_text(json.dumps(final_manifest, indent=2, sort_keys=True), encoding="utf-8")

    validation_summary = validate_phase3_trace_manifest_data(final_manifest)
    replay_summary = _run_replay_smoke(final_manifest, roots["runs"])

    closure_report = {
        "schema_id": "phase3_trace_closure_report_v1",
        "phase": "phase3_rebuild",
        "artifact_set": args.artifact_set,
        "ready_for_benchmark": False,
        "benchmark_authorized": False,
        "outputs_are_benchmark_results": False,
        "inventory_path": str(inventory_path),
        "conversion_manifest_path": str(conversion_path),
        "final_manifest_path": str(final_path),
        "replay_smoke_summary_path": replay_summary["summary_path"],
        "validation_summary": validation_summary,
        "replay_summary": replay_summary,
    }
    closure_path = roots["manifest"] / "phase3_trace_closure_report.json"
    closure_path.write_text(json.dumps(closure_report, indent=2, sort_keys=True), encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "PASS",
                "artifact_set": args.artifact_set,
                "trace_count": final_manifest["trace_count"],
                "split_counts": final_manifest["split_counts"],
                "semantics_counts": final_manifest["semantics_counts"],
                "inventory_path": str(inventory_path),
                "final_manifest_path": str(final_path),
                "closure_report_path": str(closure_path),
                "ready_for_benchmark": False,
                "benchmark_authorized": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _external_roots(artifact_set: str) -> dict[str, Path]:
    return {
        "audit": TFG_ROOT / "auditorias_trazas" / "phase3" / artifact_set,
        "normalized": TFG_ROOT / "datasets_normalizados" / "phase3" / artifact_set,
        "manifest": TFG_ROOT / "manifests_trazas" / "phase3" / artifact_set,
        "runs": TFG_ROOT / "runs_trazas" / "phase3" / artifact_set,
    }


def _clean_derived_roots(roots: dict[str, Path], artifact_set: str) -> None:
    if not artifact_set or artifact_set in {".", ".."}:
        raise ValueError("artifact_set must be a safe non-empty directory name")
    for root in roots.values():
        if root.name != artifact_set:
            raise ValueError("refusing to clean unexpected derived root: {0}".format(root))
        if root.exists():
            shutil.rmtree(root)


def _convert_all(args, roots: dict[str, Path], puffer_policy: dict[str, object]) -> dict[str, object]:
    entries: list[dict[str, object]] = []
    dataset_summaries: list[dict[str, object]] = []
    for dataset_id in args.datasets:
        if dataset_id == PufferConverter.dataset_id:
            converter = PufferConverter(
                args.raw_root,
                max_sessions=args.puffer_max_sessions,
                min_samples_per_session=args.puffer_min_samples_per_session,
                max_acked_rows=args.puffer_max_acked_rows,
                max_sent_rows=args.puffer_max_sent_rows,
            )
        else:
            converter = converter_by_id(dataset_id)(args.raw_root)
        results = converter.convert(normalized_root=roots["normalized"], metadata_root=roots["manifest"])
        manifest_entries = [result.as_manifest_entry() for result in results]
        entries.extend(manifest_entries)
        dataset_summaries.append(
            {
                "dataset_id": dataset_id,
                "converter_id": converter.converter_id,
                "trace_count": len(manifest_entries),
                "semantics": converter.semantics,
            }
        )

    return {
        "schema_id": "phase3_trace_conversion_manifest_v1",
        "phase": "phase3_rebuild",
        "artifact_set": args.artifact_set,
        "normalized_schema_id": "normalized_trace_schema_v1",
        "raw_root": str(args.raw_root),
        "normalized_root": str(roots["normalized"]),
        "manifest_root": str(roots["manifest"]),
        "puffer_sampling_policy": puffer_policy,
        "ready_for_benchmark": False,
        "benchmark_authorized": False,
        "outputs_are_benchmark_results": False,
        "controller_visibility_guardrail": (
            "controllers must not receive trace_id, dataset_id, source_id, split, group_id, "
            "leakage_group, OOD flags, or future throughput"
        ),
        "dataset_summaries": dataset_summaries,
        "trace_count": len(entries),
        "traces": sorted(entries, key=lambda item: str(item["trace_id"])),
    }


def _run_replay_smoke(final_manifest: dict[str, object], runs_root: Path) -> dict[str, object]:
    traces_by_semantics: dict[str, list[dict[str, object]]] = defaultdict(list)
    for trace in final_manifest["traces"]:
        traces_by_semantics[str(trace["semantics"])].append(trace)

    results: list[dict[str, object]] = []
    for semantics in sorted(traces_by_semantics):
        results.append(_try_semantics_replay(semantics, traces_by_semantics[semantics]))

    summary = {
        "schema_id": "phase3_trace_replay_smoke_summary_v1",
        "technical_smoke_only": True,
        "ready_for_benchmark": False,
        "benchmark_authorized": False,
        "outputs_are_benchmark_results": False,
        "segment_size_bytes": 16_000,
        "results": results,
        "success_count": sum(1 for result in results if result["status"] == "PASS"),
        "failure_count": sum(1 for result in results if result["status"] != "PASS"),
    }
    runs_root.mkdir(parents=True, exist_ok=True)
    summary_path = runs_root / "phase3_trace_replay_smoke_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    summary["summary_path"] = str(summary_path)
    return summary


def _try_semantics_replay(semantics: str, traces: list[dict[str, object]]) -> dict[str, object]:
    for trace in sorted(traces, key=lambda item: str(item["trace_id"])):
        try:
            loaded = load_normalized_trace_csv(trace["normalized_trace_path"], trace_id=str(trace["trace_id"]))
            result = TraceDrivenNetworkModel(loaded, end_policy=END_POLICY_LOOP, max_loops=5).download(16_000)
        except TraceReplayError as exc:
            last_error = str(exc)
            continue
        return {
            "status": "PASS",
            "semantics": semantics,
            "trace_id": trace["trace_id"],
            "duration_s": result.duration_s,
            "measured_throughput_kbps": result.measured_throughput_kbps,
            "samples_touched": result.samples_touched,
        }
    return {
        "status": "FAIL",
        "semantics": semantics,
        "error": locals().get("last_error", "no trace candidates"),
    }


if __name__ == "__main__":
    raise SystemExit(main())
