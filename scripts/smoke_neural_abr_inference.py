#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.bundle import BundleError
from core.neural_abr.inference import (
    InferenceError,
    load_neural_abr_bundle,
    load_validation_samples,
    run_sample_inference,
    write_inference_reports,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run offline Phase 4F NeuralABR-Lite inference smoke.")
    parser.add_argument("--bundle-dir", required=True)
    parser.add_argument("--dataset-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-samples", type=int, default=512)
    parser.add_argument("--phase", required=True, choices=("phase4f",))
    parser.add_argument(
        "--docs-dir",
        help="Optional docs directory override for tests. Defaults to docs/science/04_neural_abr.",
    )
    args = parser.parse_args(argv)

    if args.max_samples <= 0:
        parser.error("--max-samples must be positive")
    docs_dir = Path(args.docs_dir).resolve() if args.docs_dir else REPO_ROOT / "docs" / "science" / "04_neural_abr"

    try:
        engine = load_neural_abr_bundle(args.bundle_dir)
        samples = load_validation_samples(args.dataset_dir, max_samples=args.max_samples)
        report = run_sample_inference(engine, samples)
        latency_report = write_inference_reports(report, args.output_dir, docs_dir=docs_dir)
    except (BundleError, InferenceError) as exc:
        print("NeuralABR-Lite Phase 4F inference smoke failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1

    print("NeuralABR-Lite Phase 4F inference smoke summary")
    print("status: PASS")
    print("sample_count: {0}".format(report["sample_count"]))
    print("valid_action_rate: {0}".format(report["valid_action_rate"]))
    print("deterministic_rate: {0}".format(report["deterministic_rate"]))
    print("latency_summary: {0}".format(json.dumps(latency_report["latency_summary"], sort_keys=True)))
    print("diagnostic_only: true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
