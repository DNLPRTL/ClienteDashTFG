#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.export import ExportError, export_neural_abr_bundle


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export a local-only Phase 4F NeuralABR-Lite bundle.")
    parser.add_argument("--dataset-dir", required=True)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--validation-dir", required=True)
    parser.add_argument("--assessment-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--phase", required=True, choices=("phase4f",))
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument(
        "--docs-dir",
        help="Optional docs directory override for tests. Defaults to docs/science/04_neural_abr.",
    )
    args = parser.parse_args(argv)

    docs_dir = Path(args.docs_dir).resolve() if args.docs_dir else REPO_ROOT / "docs" / "science" / "04_neural_abr"
    try:
        result = export_neural_abr_bundle(
            dataset_dir=args.dataset_dir,
            run_dir=args.run_dir,
            validation_dir=args.validation_dir,
            assessment_dir=args.assessment_dir,
            output_dir=args.output_dir,
            phase=args.phase,
            overwrite=args.overwrite,
            docs_dir=docs_dir,
        )
    except ExportError as exc:
        print("NeuralABR-Lite Phase 4F export failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1

    print("NeuralABR-Lite Phase 4F export summary")
    print("status: PASS")
    print("bundle_dir: {0}".format(result.bundle_dir))
    print("source_decision: {0}".format(result.manifest.get("source_decision")))
    print("required_files: {0}".format(json.dumps(result.manifest.get("required_files"), sort_keys=True)))
    print("diagnostic_only: true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
