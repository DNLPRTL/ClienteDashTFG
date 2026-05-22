"""Run a controlled Phase 3.4C trace-driven dry-run."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.controller.registry import CONTROLLER_REGISTRY
from core.trace_replay.controller_adapter import ControllerAdapterError, ExistingControllerAdapter
from core.trace_replay.dry_run import (
    TraceDryRunConfig,
    TraceDryRunError,
    build_representations_from_kbps,
    run_trace_dry_run,
    write_trace_dry_run_artifacts,
)
from core.trace_replay.loader import TraceLoadError, load_normalized_trace_csv


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Run a non-benchmark Phase 3.4C controlled trace dry-run."
    )
    parser.add_argument("--trace-csv", required=True)
    parser.add_argument("--controller", required=True, choices=sorted(CONTROLLER_REGISTRY))
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--segment-count", required=True, type=int)
    parser.add_argument("--segment-duration-s", required=True, type=float)
    parser.add_argument("--representation-kbps", required=True)
    parser.add_argument("--end-policy", default="loop", choices=["fail", "loop"])
    parser.add_argument("--max-loops", default=3, type=int)
    parser.add_argument("--initial-buffer-s", default=0.0, type=float)
    parser.add_argument("--startup-buffer-s", default=0.0, type=float)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    try:
        output_dir = _resolve_output_dir(args.output_dir)
        _check_output_dir(output_dir, overwrite=args.overwrite)
        representation_values = _parse_representation_kbps(args.representation_kbps)
        representations = build_representations_from_kbps(representation_values)
        loaded_trace = load_normalized_trace_csv(args.trace_csv)
        controller_adapter = ExistingControllerAdapter(args.controller)
        config = TraceDryRunConfig(
            segment_duration_s=args.segment_duration_s,
            segment_count=args.segment_count,
            representations=representations,
            initial_buffer_s=args.initial_buffer_s,
            startup_buffer_s=args.startup_buffer_s,
            end_policy=args.end_policy,
            max_loops=args.max_loops,
        )
        result = run_trace_dry_run(loaded_trace, controller_adapter, config)
        artifacts = write_trace_dry_run_artifacts(result, output_dir)
        _validate_artifacts(artifacts)
    except (ControllerAdapterError, TraceDryRunError, TraceLoadError, OSError, ValueError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("trace_id: {0}".format(result.trace_id))
    print("controller: {0}".format(result.controller_name))
    print("segment_count: {0}".format(result.segment_count))
    print("total_rebuffer_s: {0:.6f}".format(result.total_rebuffer_s))
    print("output_dir: {0}".format(output_dir))
    return 0


def _parse_representation_kbps(raw_value):
    parts = [part.strip() for part in str(raw_value).split(",")]
    values = []
    for part in parts:
        if not part:
            raise ValueError("representation-kbps contains an empty value")
        values.append(float(part))
    return values


def _resolve_output_dir(output_dir):
    if output_dir is None or not str(output_dir).strip():
        raise ValueError("output-dir is required")
    return Path(output_dir)


def _check_output_dir(output_dir: Path, overwrite: bool) -> None:
    if not output_dir.exists():
        return
    if not output_dir.is_dir():
        raise ValueError("output-dir exists and is not a directory: {0}".format(output_dir))
    if overwrite:
        return
    if any(output_dir.iterdir()):
        raise ValueError("output-dir is not empty; pass --overwrite to replace dry-run artifact files")


def _validate_artifacts(artifacts) -> None:
    required = ("manifest", "segments", "summary")
    missing = []
    for key in required:
        path = artifacts.get(key)
        if path is None or not Path(path).is_file():
            missing.append(key)
    if missing:
        raise ValueError("missing dry-run artifacts: {0}".format(", ".join(missing)))


if __name__ == "__main__":
    sys.exit(main())
