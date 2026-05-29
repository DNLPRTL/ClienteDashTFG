#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.trace_corpus import prepare_phase4e2_trace_corpus


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare a Phase 4E.2 external trace corpus for NeuralABR-Lite.")
    parser.add_argument("--phase3-root", required=True, help="Local Phase 3 trace replay root outside the repository.")
    parser.add_argument("--output-root", required=True, help="Output corpus root outside the repository.")
    parser.add_argument("--max-total-traces", type=int, default=300)
    parser.add_argument("--max-traces-per-dataset", type=int, default=120)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    result = prepare_phase4e2_trace_corpus(
        phase3_root=args.phase3_root,
        output_root=args.output_root,
        max_total_traces=args.max_total_traces,
        max_traces_per_dataset=args.max_traces_per_dataset,
        seed=args.seed,
        overwrite=args.overwrite,
    )
    summary = result["summary"]
    print("Phase 4E.2 trace corpus preparation summary")
    print("output_root: {0}".format(result["output_root"]))
    print("normalized_root: {0}".format(result["normalized_root"]))
    print("manifest_root: {0}".format(result["manifest_root"]))
    print("selected_trace_count: {0}".format(summary["selected_trace_count"]))
    print("dataset_id_counts: {0}".format(json.dumps(summary["dataset_id_counts"], sort_keys=True)))
    print("regime_bucket_counts: {0}".format(json.dumps(summary["regime_bucket_counts"], sort_keys=True)))
    print("skipped_count: {0}".format(summary["skipped_count"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
