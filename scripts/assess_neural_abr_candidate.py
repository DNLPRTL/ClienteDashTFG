#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.artifacts import ensure_outside_repo, write_json
from core.neural_abr.candidate_readiness import (
    assess_candidate_readiness,
    render_candidate_readiness_markdown,
    render_closure_report_markdown,
    render_limitations_markdown,
    render_model_card_markdown,
    render_repair_report_markdown,
    render_validation_report_markdown,
)
from core.neural_abr.constants import PHASE4E2_DECISION_BLOCKED


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Assess NeuralABR-Lite candidate readiness.")
    parser.add_argument("--dataset-dir", required=True)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--validation-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--phase", required=True, choices=("phase4e1", "phase4e2"))
    parser.add_argument(
        "--docs-dir",
        help="Optional docs directory override, primarily for tests. Defaults to docs/science/04_neural_abr.",
    )
    parser.add_argument(
        "--check-repo-hygiene",
        action="store_true",
        help="Explicitly scan the repository for forbidden generated artifacts and protected-path changes.",
    )
    args = parser.parse_args(argv)

    output_dir = ensure_outside_repo(args.output_dir, purpose="candidate assessment output")
    output_dir.mkdir(parents=True, exist_ok=True)
    docs_dir = Path(args.docs_dir).resolve() if args.docs_dir else REPO_ROOT / "docs" / "science" / "04_neural_abr"
    docs_dir.mkdir(parents=True, exist_ok=True)

    first_report = assess_candidate_readiness(
        dataset_dir=args.dataset_dir,
        run_dir=args.run_dir,
        validation_dir=args.validation_dir,
        phase=args.phase,
        docs_dir=docs_dir,
        repo_root=REPO_ROOT,
        check_repo_hygiene=args.check_repo_hygiene,
    )
    _write_docs(first_report, docs_dir, args.phase)
    report = assess_candidate_readiness(
        dataset_dir=args.dataset_dir,
        run_dir=args.run_dir,
        validation_dir=args.validation_dir,
        phase=args.phase,
        docs_dir=docs_dir,
        repo_root=REPO_ROOT,
        check_repo_hygiene=args.check_repo_hygiene,
    )
    _write_outputs(report, output_dir, docs_dir, args.phase)

    print("NeuralABR-Lite candidate readiness summary")
    print("phase: {0}".format(args.phase))
    print("decision: {0}".format(report["decision"]))
    print("dataset_trace_count: {0}".format(report["dataset_summary"]["trace_count"]))
    print("correctness_failures: {0}".format(json.dumps(report["correctness_failures"], sort_keys=True)))
    print("candidate_failures: {0}".format(json.dumps(report["candidate_failures"], sort_keys=True)))
    print("environmental_failures: {0}".format(json.dumps(report["environmental_failures"], sort_keys=True)))
    print("diagnostic_only: true")
    if report["decision"] == PHASE4E2_DECISION_BLOCKED:
        return 1
    return 0


def _write_outputs(report, output_dir: Path, docs_dir: Path, phase: str) -> None:
    write_json(output_dir / "candidate_readiness_report.json", report)
    write_json(output_dir / "{0}_candidate_readiness_report.json".format(phase), report)
    (output_dir / "{0}_candidate_readiness_report.md".format(phase)).write_text(
        render_candidate_readiness_markdown(report),
        encoding="utf-8",
    )
    _write_docs(report, docs_dir, phase)


def _write_docs(report, docs_dir: Path, phase: str) -> None:
    documents = {
        "{0}_candidate_readiness_report.md".format(phase): render_candidate_readiness_markdown(report),
        "{0}_validation_report.md".format(phase): render_validation_report_markdown(report),
        "{0}_model_card.md".format(phase): render_model_card_markdown(report),
        "{0}_open_limitations.md".format(phase): render_limitations_markdown(report),
        "{0}_closure_report.md".format(phase): render_closure_report_markdown(report),
        "{0}_repair_report.md".format(phase): render_repair_report_markdown(report),
    }
    for filename, text in documents.items():
        (docs_dir / filename).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
