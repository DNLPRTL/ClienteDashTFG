from __future__ import annotations

import argparse
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
from collections import deque
from pathlib import Path
from typing import Any, Deque, Dict, List, Mapping, Optional, Sequence

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        resolve_source_ids,
        source_arg_from_ids,
        sources_by_id,
        utc_now,
        write_json,
        write_markdown_report,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        resolve_source_ids,
        source_arg_from_ids,
        sources_by_id,
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
STDOUT_TAIL_LINES = 300


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run automated Phase 6C trace materialization outside the repository.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--phase4-dataset-manifest", required=True, type=Path)
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--sources", default="primary")
    parser.add_argument("--include-lumos", action="store_true")
    parser.add_argument("--include-diagnostic", action="store_true")
    parser.add_argument("--require-lumos", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--clean-derived", action="store_true")
    parser.add_argument("--force-download", action="store_true")
    parser.add_argument("--force-extract", action="store_true")
    parser.add_argument("--progress-every", type=int, default=25)
    parser.add_argument("--step-timeout-s", type=int, default=1800)
    parser.add_argument("--normalize-timeout-s", type=int, default=3600)
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    for flag in ACTION_FLAGS:
        parser.add_argument("--" + flag.replace("_", "-"), action="store_true")
    return parser


def run_materialization(args: argparse.Namespace) -> Dict[str, Any]:
    paths = create_external_layout(args.external_root, allow_repo_output=args.allow_repo_output)
    registry = load_source_registry(args.source_registry)
    source_map = sources_by_id(registry)
    selected_ids = effective_source_ids(args, registry=registry)
    source_arg = source_arg_from_ids(selected_ids)
    actions = selected_actions(args)
    commands: List[List[str]] = []
    steps: List[Dict[str, Any]] = []
    errors: List[str] = []
    notes: List[str] = []

    reference_manifest = paths["manifests"] / "phase4_training_reference_manifest.json"
    candidate_manifest = paths["manifests"] / "phase6_candidate_trace_manifest.json"
    validation_report = paths["reports"] / "phase6_candidate_manifest_validation.json"
    audit_report = paths["audit"] / "phase6_trace_eligibility_audit.json"
    final_manifest = paths["manifests"] / "phase6_trace_manifest_final.json"

    if args.clean_derived:
        clean_derived_outputs(paths, selected_ids, source_map)
        notes.append("clean_derived_completed_for_selected_sources")

    def execute_step(
        name: str,
        command: List[str],
        *,
        expected_output: Optional[Path] = None,
        timeout_s: Optional[int] = None,
        skip_on_existing: bool = True,
    ) -> bool:
        if (
            args.skip_existing
            and skip_on_existing
            and expected_output is not None
            and expected_output.exists()
        ):
            command = python_unbuffered_command(command)
            commands.append(command)
            step = {
                "name": name,
                "command": command,
                "returncode": 0,
                "elapsed_s": 0.0,
                "skipped": True,
                "skip_reason": "existing_output",
                "expected_output": str(expected_output),
                "stdout_tail": [],
                "timed_out": False,
            }
            steps.append(step)
            print("phase6c_materialization: skipped {0}; existing output {1}".format(name, expected_output))
            return True

        run_step(
            name,
            command,
            commands,
            steps,
            errors,
            strict=args.strict,
            log_dir=paths["logs"],
            timeout_s=timeout_s if timeout_s is not None else args.step_timeout_s,
        )
        last = steps[-1]
        return last.get("returncode") == 0 and not last.get("timed_out", False)

    continue_pipeline = True

    if "download" in actions and continue_pipeline:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "download_phase6_trace_sources.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
            "--sources",
            source_arg,
        ]
        if args.require_lumos:
            command.append("--require-lumos")
        if args.force_download:
            command.append("--force-download")
        if args.strict:
            command.append("--strict")
        continue_pipeline = execute_step("download", command, timeout_s=args.step_timeout_s, skip_on_existing=False)

    if "extract" in actions and continue_pipeline:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "extract_phase6_trace_archives.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
            "--sources",
            source_arg,
        ]
        if args.force_extract:
            command.append("--force-extract")
        if args.strict:
            command.append("--strict")
        continue_pipeline = execute_step("extract", command, timeout_s=args.step_timeout_s, skip_on_existing=False)

    if "normalize" in actions and continue_pipeline:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "normalize_phase6_trace_sources.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
            "--sources",
            source_arg,
            "--progress-every",
            str(args.progress_every),
        ]
        if args.clean_derived:
            command.append("--clean-normalized")
        if args.strict:
            command.append("--strict")
        continue_pipeline = execute_step(
            "normalize",
            command,
            expected_output=paths["reports"] / "phase6c_normalization_report.json",
            timeout_s=args.normalize_timeout_s,
            skip_on_existing=not args.clean_derived,
        )

    if "build_reference" in actions and continue_pipeline:
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
        continue_pipeline = execute_step("build_reference", command, expected_output=reference_manifest)

    if "build_candidate" in actions and continue_pipeline:
        command = [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_phase6_candidate_manifest.py"),
            "--external-root",
            str(paths["root"]),
            "--source-registry",
            str(args.source_registry),
            "--sources",
            source_arg,
            "--output",
            str(candidate_manifest),
        ]
        if args.strict:
            command.append("--strict")
        continue_pipeline = execute_step("build_candidate", command, expected_output=candidate_manifest)

    if "validate" in actions and continue_pipeline:
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
        continue_pipeline = execute_step("validate", command, expected_output=validation_report)

    if "audit" in actions and continue_pipeline:
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
        continue_pipeline = execute_step("audit", command, expected_output=audit_report)

    if "freeze" in actions and continue_pipeline:
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
        continue_pipeline = execute_step("freeze", command, expected_output=final_manifest)

    if not continue_pipeline:
        notes.append("pipeline_stopped_after_failed_step")

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
        "source_selection": args.sources,
        "selected_sources": selected_ids,
        "include_lumos": bool(args.include_lumos or args.require_lumos),
        "include_diagnostic": bool(args.include_diagnostic),
        "actions": actions,
        "resume": bool(args.resume),
        "skip_existing": bool(args.skip_existing),
        "clean_derived": bool(args.clean_derived),
        "step_timeout_s": args.step_timeout_s,
        "normalize_timeout_s": args.normalize_timeout_s,
        "stdout_tail_lines": STDOUT_TAIL_LINES,
        "steps": steps,
        "errors": errors,
        "notes": notes,
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


def effective_source_ids(args: argparse.Namespace, *, registry: Optional[Mapping[str, Any]] = None) -> List[str]:
    loaded = registry if registry is not None else load_source_registry(args.source_registry)
    return resolve_source_ids(
        loaded,
        source_spec=getattr(args, "sources", "primary"),
        include_lumos=bool(getattr(args, "include_lumos", False) or getattr(args, "require_lumos", False)),
        include_diagnostic=bool(getattr(args, "include_diagnostic", False)),
    )


def clean_derived_outputs(
    paths: Mapping[str, Path],
    selected_ids: Sequence[str],
    source_map: Mapping[str, Mapping[str, Any]],
) -> None:
    for source_id in selected_ids:
        source = source_map.get(source_id, {})
        dataset_family = str(source.get("dataset_family", source_id))
        for path in (
            paths["normalized"] / dataset_family,
            paths["manifests"] / "per_trace" / dataset_family,
        ):
            if path.exists():
                shutil.rmtree(path)

    for path in (
        paths["manifests"] / "phase6_candidate_trace_manifest.json",
        paths["manifests"] / "phase6_trace_manifest_final.json",
        paths["reports"] / "phase6_candidate_manifest_validation.json",
        paths["reports"] / "phase6c_normalization_progress.json",
        paths["reports"] / "phase6c_normalization_report.json",
        paths["reports"] / "phase6c_normalization_report.md",
        paths["reports"] / "phase6c_materialization_summary.json",
        paths["reports"] / "phase6c_materialization_summary.md",
        paths["audit"] / "phase6_trace_eligibility_audit.json",
    ):
        if path.exists():
            path.unlink()


def run_step(
    name: str,
    command: List[str],
    commands: List[List[str]],
    steps: List[Dict[str, Any]],
    errors: List[str],
    *,
    strict: bool,
    log_dir: Path,
    timeout_s: int = 1800,
    tail_lines: int = STDOUT_TAIL_LINES,
) -> None:
    del strict  # Subprocess failures are recorded in the summary so timeout reports survive.
    command = python_unbuffered_command(command)
    commands.append(command)
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "phase6c_{0}.log".format(safe_step_name(name))

    print("")
    print("=" * 90)
    print("PHASE 6C STEP START:", name)
    print("COMMAND:", " ".join(str(part) for part in command))
    print("LOG:", log_path)
    print("=" * 90)
    sys.stdout.flush()

    start = time.monotonic()
    output_tail: Deque[str] = deque(maxlen=tail_lines)
    timed_out = False
    interrupted = False
    returncode = 0
    done_marker = object()
    output_queue: "queue.Queue[Any]" = queue.Queue()

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )

    def reader() -> None:
        assert process.stdout is not None
        for line in process.stdout:
            output_queue.put(line)
        output_queue.put(done_marker)

    reader_thread = threading.Thread(target=reader, name="phase6c-{0}-reader".format(name), daemon=True)
    reader_thread.start()

    with log_path.open("w", encoding="utf-8", newline="\n") as log:
        log.write("PHASE 6C STEP START: {0}\n".format(name))
        log.write("COMMAND: {0}\n\n".format(" ".join(str(part) for part in command)))
        log.flush()
        try:
            while True:
                if timeout_s > 0 and time.monotonic() - start > timeout_s:
                    timed_out = True
                    terminate_process(process)
                    break
                try:
                    item = output_queue.get(timeout=0.1)
                except queue.Empty:
                    if process.poll() is not None and not reader_thread.is_alive():
                        break
                    continue
                if item is done_marker:
                    break
                line = str(item).rstrip("\r\n")
                output_tail.append(line)
                print(line)
                log.write(line + "\n")
                log.flush()
                sys.stdout.flush()
        except KeyboardInterrupt:
            interrupted = True
            terminate_process(process)
            raise
        finally:
            if not timed_out and not interrupted:
                returncode = process.wait()
            else:
                returncode = process.returncode if process.returncode is not None else -9
            reader_thread.join(timeout=1)
            if process.stdout is not None:
                process.stdout.close()
            drain_output_queue(output_queue, done_marker, output_tail, log)
            elapsed_s = round(time.monotonic() - start, 3)
            log.write("\nPHASE 6C STEP END: {0} exit {1} elapsed_s {2}\n".format(name, returncode, elapsed_s))
            if timed_out:
                log.write("TIMEOUT after {0} seconds\n".format(timeout_s))

    step = {
        "name": name,
        "command": command,
        "returncode": returncode,
        "elapsed_s": elapsed_s,
        "timeout_s": timeout_s,
        "timed_out": timed_out,
        "log_path": str(log_path),
        "stdout_tail": list(output_tail),
        "stderr": "",
    }
    steps.append(step)

    print("=" * 90)
    print("PHASE 6C STEP END:", name, "exit", returncode, "elapsed_s", elapsed_s)
    if timed_out:
        print("PHASE 6C STEP TIMEOUT:", name, "timeout_s", timeout_s)
    print("=" * 90)
    sys.stdout.flush()

    if timed_out:
        errors.append("{0} timed out after {1} seconds".format(name, timeout_s))
    elif returncode != 0:
        errors.append("{0} failed with exit code {1}".format(name, returncode))


def python_unbuffered_command(command: Sequence[str]) -> List[str]:
    normalized = [str(part) for part in command]
    if not normalized:
        return []
    executable = Path(normalized[0]).name.lower()
    if executable.startswith("python") and "-u" not in normalized[1:3]:
        return [normalized[0], "-u", *normalized[1:]]
    if Path(normalized[0]).resolve() == Path(sys.executable).resolve() and "-u" not in normalized[1:3]:
        return [normalized[0], "-u", *normalized[1:]]
    return normalized


def terminate_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def drain_output_queue(
    output_queue: "queue.Queue[Any]",
    done_marker: object,
    output_tail: Deque[str],
    log: Any,
) -> None:
    while True:
        try:
            item = output_queue.get_nowait()
        except queue.Empty:
            break
        if item is done_marker:
            continue
        line = str(item).rstrip("\r\n")
        output_tail.append(line)
        print(line)
        log.write(line + "\n")


def safe_step_name(name: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", name.lower()).strip("_") or "step"


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
        "- selected_sources: `{0}`".format(",".join(summary.get("selected_sources", []))),
        "- stdout_tail_lines: `{0}`".format(summary.get("stdout_tail_lines", STDOUT_TAIL_LINES)),
        "",
        "## Steps",
        "",
    ]
    for step in summary["steps"]:
        status = "skipped" if step.get("skipped") else "exit `{0}`".format(step.get("returncode", ""))
        lines.append("- `{0}`: {1}, elapsed `{2}` seconds".format(step["name"], status, step.get("elapsed_s", 0)))
        if step.get("log_path"):
            lines.append("  log: `{0}`".format(step["log_path"]))
    if summary["errors"]:
        lines.extend(["", "## Errors", ""])
        lines.extend("- {0}".format(error) for error in summary["errors"])
    if summary.get("notes"):
        lines.extend(["", "## Notes", ""])
        lines.extend("- {0}".format(note) for note in summary["notes"])
    write_markdown_report(path, "Phase 6C Materialization Summary", lines)


if __name__ == "__main__":
    sys.exit(main())
