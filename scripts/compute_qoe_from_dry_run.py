"""Compute Phase 3.5C QoE artifacts from one dry-run artifact directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.evaluation.artifacts import QoEArtifactError, compute_qoe_artifacts_from_dry_run


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Compute non-benchmark Phase 3.5C QoE artifacts from one dry-run directory."
    )
    parser.add_argument("--dry-run-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--expected-segment-count", type=int)
    parser.add_argument("--min-bitrate-kbps", type=float)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    try:
        result = compute_qoe_artifacts_from_dry_run(
            dry_run_dir=args.dry_run_dir,
            output_dir=args.output_dir,
            expected_segment_count=args.expected_segment_count,
            min_bitrate_kbps=args.min_bitrate_kbps,
            overwrite=args.overwrite,
        )
    except (OSError, QoEArtifactError, ValueError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    summary = result.summary
    print("dry_run_dir: {0}".format(Path(args.dry_run_dir)))
    print("output_dir: {0}".format(result.output_dir))
    print("trace_id: {0}".format(summary["trace_id"]))
    print("controller_name: {0}".format(summary["controller_name"]))
    print("qoe_linear_mean: {0}".format(summary["qoe_linear_mean"]))
    print("session_eval_gate: {0}".format(summary["session_eval_gate"]))
    print("outputs_are_benchmark_results=false")
    print("no_final_ranking=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
