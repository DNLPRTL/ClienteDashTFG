#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.trace_replay.converters.registry import available_converters, converter_by_id

TFG_ROOT = REPO_ROOT.parent
DEFAULT_RAW_ROOT = TFG_ROOT / "dataset en bruto"
DEFAULT_NORMALIZED_ROOT = TFG_ROOT / "datasets_normalizados" / "phase3"
DEFAULT_MANIFEST_ROOT = TFG_ROOT / "manifests_trazas" / "phase3"
DEFAULT_CONVERSION_MANIFEST = DEFAULT_MANIFEST_ROOT / "phase3_trace_conversion_manifest.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 3C normalize raw trace datasets into schema_v1 CSVs.")
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT)
    parser.add_argument("--normalized-root", type=Path, default=DEFAULT_NORMALIZED_ROOT)
    parser.add_argument("--manifest-root", type=Path, default=DEFAULT_MANIFEST_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_CONVERSION_MANIFEST)
    parser.add_argument("--datasets", nargs="*", choices=available_converters(), default=list(available_converters()))
    parser.add_argument("--max-traces-per-dataset", type=int, default=None)
    args = parser.parse_args(argv)

    entries: list[dict[str, object]] = []
    dataset_summaries: list[dict[str, object]] = []
    for dataset_id in args.datasets:
        converter = converter_by_id(dataset_id)(args.raw_root)
        results = converter.convert(
            normalized_root=args.normalized_root,
            metadata_root=args.manifest_root,
            max_traces=args.max_traces_per_dataset,
        )
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

    manifest = {
        "schema_id": "phase3_trace_conversion_manifest_v1",
        "phase": "phase3_rebuild",
        "normalized_schema_id": "normalized_trace_schema_v1",
        "raw_root": str(args.raw_root),
        "normalized_root": str(args.normalized_root),
        "manifest_root": str(args.manifest_root),
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
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    print(
        json.dumps(
            {
                "schema_id": manifest["schema_id"],
                "trace_count": manifest["trace_count"],
                "output": str(args.output),
                "datasets": dataset_summaries,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
