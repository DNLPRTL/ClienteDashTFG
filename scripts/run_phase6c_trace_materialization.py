from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        utc_now,
        write_json,
        write_markdown_report,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        utc_now,
        write_json,
        write_markdown_report,
    )


REPO_ROOT = Path(__file__).resolve().parents[1]
SUMMARY_SCHEMA_VERSION = "phase6c_materialization_summary_v1"
ACTION_FLAGS = (
    "download",
    "extract",
    "normalize",
    "build_reference",
    "build_candidate",
    "validate",
    "audit",
    "freeze",
)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run automated Phase 6C trace materialization outside the repository.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--phase4-dataset-manifest", required=True, type=Path)
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--sources", default="all")
    parser.add_argument("--require-lumos", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    for flag in ACTION_FLAGS:
        parser.add_argument("--" + flag.replace("_", "-"), action="store_true")
    args = parser.parse_args(argv)

    try:
        summary = run_materialization(args)
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6c_materialization: {0}".format("PASS" if summary["valid"] else "WARN_OR_FAIL"))
    print("summary: {0}".format(summary["summary_json"]))
    return 0 if summary["valid"] else 2


def run_materialization(args: argparse.Namespace) -> Dict[str, Any]:
    paths = create_external_layout(args.external_root, allow_repo_output=args.allow_repo_output)
    actions = selected_actions(args)
    commands: List[List[str]] = []
    steps: List[Dict[str, Any]] = []
    errors: List[str] = []

    reference_manifest = paths["manifests"] / "phase4_training_reference_manifest.json"
    candidate_manifest = paths["manifests"] / "phase6_candidate_trace_manifest.json"
    validation_report = paths["reports"] / "phase6_candidate_manifest_validation.json"
    audit_report = paths["audit"] / "phase6_trace_eligibility_audit.json"
    final_manifest = paths["manifests"] / "phase6_trace_manifest_final.json"

    if "download" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "download_phase6_trace_sources.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
            "--sources",
            args.sources,
        ]
        if args.require_lumos:
            command.append("--require-lumos")
        if args.strict:
            command.append("--strict")
        run_step("download", command, commands, steps, errors, strict=args.strict)

    if "extract" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "extract_phase6_trace_archives.py"),
            "--external-root",
            str(paths["root"]),
        ]
        if args.strict:
            command.append("--strict")
        run_step("extract", command, commands, steps, errors, strict=args.strict)

    if "normalize" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "normalize_phase6_trace_sources.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
        ]
        if args.strict:
            command.append("--strict")
        run_step("normalize", command, commands, steps, errors, strict=args.strict)

    if "build_reference" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_phase6_reference_manifest.py"),
            "--phase4-dataset-manifest",
            str(args.phase4_dataset_manifest),
            "--output",
            str(reference_manifest),
        ]
        if args.strict:
            command.append("--strict")
        run_step("build_reference", command, commands, steps, errors, strict=args.strict)

    if "build_candidate" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_phase6_candidate_manifest.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
            "--output",
            str(candidate_manifest),
            "--include-diagnostic",
        ]
        if args.strict:
            command.append("--strict")
        run_step("build_candidate", command, commands, steps, errors, strict=args.strict)

    if "validate" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "validate_phase6_trace_manifest.py"),
            "--manifest",
            str(candidate_manifest),
            "--output",
            str(validation_report),
            "--strict-final",
            "--fail-on-error",
        ]
        run_step("validate", command, commands, steps, errors, strict=args.strict)

    if "audit" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "audit_phase6_trace_eligibility.py"),
            "--phase4-dataset-manifest",
            str(reference_manifest),
            "--phase6-candidate-manifest",
            str(candidate_manifest),
            "--output",
            str(audit_report),
            "--fail-on-block",
        ]
        run_step("audit", command, commands, steps, errors, strict=args.strict)

    if "freeze" in actions:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "freeze_phase6_trace_manifest.py"),
            "--candidate-manifest",
            str(candidate_manifest),
            "--validation-report",
            str(validation_report),
            "--eligibility-audit-report",
            str(audit_report),
            "--output",
            str(final_manifest),
        ]
        if args.strict:
            command.append("--strict")
        run_step("freeze", command, commands, steps, errors, strict=args.strict)

    commands_sh = paths["reports"] / "commands_used.sh"
    commands_ps1 = paths["reports"] / "commands_used.ps1"
    write_commands(commands_sh, commands, shell="sh")
    write_commands(commands_ps1, commands, shell="ps1")

    summary = {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "external_root": str(paths["root"]),
        "phase4_dataset_manifest": str(args.phase4_dataset_manifest),
        "source_registry": str(args.source_registry),
        "actions": actions,
        "steps": steps,
        "errors": errors,
        "valid": not errors,
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6c_materialization_only": True,
        "outputs": {
            "reference_manifest": str(reference_manifest),
            "candidate_manifest": str(candidate_manifest),
            "validation_report": str(validation_report),
            "eligibility_audit_report": str(audit_report),
            "final_manifest": str(final_manifest),
            "commands_used_sh": str(commands_sh),
            "commands_used_ps1": str(commands_ps1),
        },
    }
    summary_json = paths["reports"] / "phase6c_materialization_summary.json"
    summary_md = paths["reports"] / "phase6c_materialization_summary.md"
    write_json(summary_json, summary)
    write_summary_markdown(summary_md, summary)
    summary["summary_json"] = str(summary_json)
    summary["summary_md"] = str(summary_md)
    return summary


def selected_actions(args: argparse.Namespace) -> List[str]:
    chosen = [flag for flag in ACTION_FLAGS if getattr(args, flag)]
    if chosen:
        return chosen
    return list(ACTION_FLAGS)


def run_step(
    name: str,
    command: List[str],
    commands: List[List[str]],
    steps: List[Dict[str, Any]],
    errors: List[str],
    *,
    strict: bool,
) -> None:
    commands.append(command)
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    step = {
        "name": name,
        "command": command,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }
    steps.append(step)
    if result.returncode != 0:
        message = "{0} failed with exit code {1}".format(name, result.returncode)
        errors.append(message)
        if strict:
            raise Phase6CError(message + (": " + result.stderr.strip() if result.stderr.strip() else ""))


def write_commands(path: Path, commands: Sequence[Sequence[str]], *, shell: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if shell == "ps1":
        lines = ["# Phase 6C commands. Benchmark is not authorized."]
        lines.extend(" ".join(powershell_quote(part) for part in command) for command in commands)
    else:
        lines = ["#!/usr/bin/env sh", "# Phase 6C commands. Benchmark is not authorized."]
        lines.extend(" ".join(sh_quote(part) for part in command) for command in commands)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sh_quote(value: str) -> str:
    if re_safe(value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"


def powershell_quote(value: str) -> str:
    if re_safe(value):
        return value
    return "'" + value.replace("'", "''") + "'"


def re_safe(value: str) -> bool:
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.\\/:")
    return bool(value) and all(char in allowed for char in value)


def write_summary_markdown(path: Path, summary: Mapping[str, Any]) -> None:
    lines = [
        "Phase 6C automated materialization summary. This is not benchmark evidence.",
        "",
        "- valid: `{0}`".format(str(summary["valid"]).lower()),
        "- ready_for_benchmark: `false`",
        "- benchmark_authorized: `false`",
        "- external_root: `{0}`".format(summary["external_root"]),
        "",
        "## Steps",
        "",
    ]
    for step in summary["steps"]:
        lines.append("- `{0}`: exit `{1}`".format(step["name"], step["returncode"]))
    if summary["errors"]:
        lines.extend(["", "## Errors", ""])
        lines.extend("- {0}".format(error) for error in summary["errors"])
    write_markdown_report(path, "Phase 6C Materialization Summary", lines)


if __name__ == "__main__":
    sys.exit(main())
