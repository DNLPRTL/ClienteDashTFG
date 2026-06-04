from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

try:
    from scripts.check_phase6_media_profile_compatibility import check_media_profile_compatibility
    from scripts.extract_phase6_media_profile_from_mpd import DEFAULT_PROFILE_ID, SIZE_POLICIES, extract_media_profile
    from scripts.freeze_phase6_media_profile import freeze_media_profile
    from scripts.phase6c_source_registry import Phase6CError, refuse_repo_path, utc_now, write_markdown_report
    from scripts.validate_phase6_media_profile import validate_media_profile
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from check_phase6_media_profile_compatibility import check_media_profile_compatibility
    from extract_phase6_media_profile_from_mpd import DEFAULT_PROFILE_ID, SIZE_POLICIES, extract_media_profile
    from freeze_phase6_media_profile import freeze_media_profile
    from phase6c_source_registry import Phase6CError, refuse_repo_path, utc_now, write_markdown_report
    from validate_phase6_media_profile import validate_media_profile


SUMMARY_SCHEMA_VERSION = "phase6d_media_profile_freeze_summary_v1"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        summary = run_phase6d_media_profile_freeze(args)
    except (OSError, json.JSONDecodeError, Phase6CError, RuntimeError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2

    print("phase6d_media_profile_freeze: {0}".format("PASS" if summary["valid"] else "WARN_OR_FAIL"))
    print("summary: {0}".format(summary["outputs"]["summary_json"]))
    print("media_profile: {0}".format(summary["outputs"]["frozen_media_profile"]))
    return 0 if summary["valid"] else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Phase 6D MPD-derived media profile extraction, validation and freeze.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--mpd", required=True)
    parser.add_argument("--content-root", type=Path)
    parser.add_argument("--base-url")
    parser.add_argument("--neural-bundle-root", type=Path)
    parser.add_argument("--prefer-real-segment-sizes", action="store_true")
    parser.add_argument("--size-policy", choices=SIZE_POLICIES, default="bitrate_estimate")
    parser.add_argument("--profile-id", default=DEFAULT_PROFILE_ID)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    return parser


def run_phase6d_media_profile_freeze(args: argparse.Namespace) -> Dict[str, Any]:
    paths = create_phase6d_layout(args.external_root, allow_repo_output=args.allow_repo_output)
    extracted_profile = paths["media_profiles"] / "{0}_extracted.json".format(args.profile_id)
    frozen_profile = paths["media_profiles"] / "{0}.json".format(args.profile_id)
    validation_report = paths["reports"] / "phase6d_media_profile_validation.json"
    compatibility_report = paths["reports"] / "phase6d_media_profile_compatibility.json"
    summary_json = paths["reports"] / "phase6d_media_profile_freeze_summary.json"
    summary_md = paths["reports"] / "phase6d_media_profile_freeze_summary.md"
    commands_ps1 = paths["reports"] / "commands_used.ps1"
    commands_sh = paths["reports"] / "commands_used.sh"
    log_path = paths["logs"] / "phase6d_media_profile_freeze.log"

    commands = build_commands(args, extracted_profile, frozen_profile, validation_report, compatibility_report)
    steps: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []

    try:
        extracted = extract_media_profile(
            mpd=args.mpd,
            output=extracted_profile,
            content_root=args.content_root,
            base_url=args.base_url,
            profile_id=args.profile_id,
            prefer_real_segment_sizes=args.prefer_real_segment_sizes,
            size_policy=args.size_policy,
            strict=args.strict,
        )
        steps.append(step_record("extract", "ok", extracted_profile))

        validation = validate_media_profile(extracted_profile, strict=args.strict)
        write_json(validation_report, validation)
        warnings.extend(validation.get("warnings", []))
        steps.append(step_record("validate", "ok" if validation["valid"] else "fail", validation_report))

        compatibility = check_media_profile_compatibility(
            media_profile=extracted_profile,
            neural_bundle_root=args.neural_bundle_root,
            strict=args.strict,
        )
        write_json(compatibility_report, compatibility)
        warnings.extend(compatibility.get("warnings", []))
        steps.append(step_record("compatibility", "ok" if compatibility["valid"] else "fail", compatibility_report))

        freeze = freeze_media_profile(
            extracted_profile=extracted_profile,
            validation_report=validation_report,
            compatibility_report=compatibility_report,
            output=frozen_profile,
            strict=args.strict,
        )
        steps.append(step_record("freeze", "ok", frozen_profile))
    except Exception as exc:
        errors.append(str(exc))

    write_commands(commands_ps1, commands, shell="ps1")
    write_commands(commands_sh, commands, shell="sh")

    valid = not errors and all(step["status"] == "ok" for step in steps)
    summary = {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "external_root": str(paths["root"]),
        "mpd": args.mpd,
        "content_root": str(args.content_root) if args.content_root else None,
        "base_url": args.base_url,
        "neural_bundle_root": str(args.neural_bundle_root) if args.neural_bundle_root else None,
        "profile_id": args.profile_id,
        "size_policy": args.size_policy,
        "prefer_real_segment_sizes": bool(args.prefer_real_segment_sizes),
        "strict": bool(args.strict),
        "steps": steps,
        "errors": errors,
        "warnings": sorted(set(warnings)),
        "valid": bool(valid),
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6d_freeze_only": True,
        "server_role": "mpd_content_media_profile_source_not_benchmark_network",
        "benchmark_network_source": "normalized_traces_via_TraceDrivenNetworkModel",
        "outputs": {
            "extracted_media_profile": str(extracted_profile),
            "frozen_media_profile": str(frozen_profile),
            "validation_report": str(validation_report),
            "compatibility_report": str(compatibility_report),
            "summary_json": str(summary_json),
            "summary_md": str(summary_md),
            "commands_used_ps1": str(commands_ps1),
            "commands_used_sh": str(commands_sh),
            "log": str(log_path),
        },
    }
    write_json(summary_json, summary)
    write_summary_markdown(summary_md, summary)
    write_log(log_path, summary)
    return summary


def create_phase6d_layout(external_root: Path, *, allow_repo_output: bool = False) -> Dict[str, Path]:
    root = Path(external_root).expanduser().resolve()
    if not allow_repo_output:
        refuse_repo_path(root)
    paths = {"root": root}
    for name in ("media_profiles", "reports", "logs"):
        path = root / name
        path.mkdir(parents=True, exist_ok=True)
        paths[name] = path
    return paths


def build_commands(
    args: argparse.Namespace,
    extracted_profile: Path,
    frozen_profile: Path,
    validation_report: Path,
    compatibility_report: Path,
) -> List[List[str]]:
    extract = [
        sys.executable,
        "scripts/extract_phase6_media_profile_from_mpd.py",
        "--mpd",
        args.mpd,
        "--output",
        str(extracted_profile),
        "--profile-id",
        args.profile_id,
        "--size-policy",
        args.size_policy,
    ]
    if args.content_root:
        extract.extend(["--content-root", str(args.content_root)])
    if args.base_url:
        extract.extend(["--base-url", args.base_url])
    if args.prefer_real_segment_sizes:
        extract.append("--prefer-real-segment-sizes")
    if args.strict:
        extract.append("--strict")

    validate = [
        sys.executable,
        "scripts/validate_phase6_media_profile.py",
        "--profile",
        str(extracted_profile),
        "--output",
        str(validation_report),
        "--fail-on-error",
    ]
    if args.strict:
        validate.append("--strict")

    compatibility = [
        sys.executable,
        "scripts/check_phase6_media_profile_compatibility.py",
        "--media-profile",
        str(extracted_profile),
        "--output",
        str(compatibility_report),
    ]
    if args.neural_bundle_root:
        compatibility.extend(["--neural-bundle-root", str(args.neural_bundle_root)])
    if args.strict:
        compatibility.append("--strict")

    freeze = [
        sys.executable,
        "scripts/freeze_phase6_media_profile.py",
        "--extracted-profile",
        str(extracted_profile),
        "--validation-report",
        str(validation_report),
        "--compatibility-report",
        str(compatibility_report),
        "--output",
        str(frozen_profile),
    ]
    if args.strict:
        freeze.append("--strict")

    return [extract, validate, compatibility, freeze]


def step_record(name: str, status: str, output: Path) -> Dict[str, Any]:
    return {"name": name, "status": status, "output": str(output), "exists": output.is_file()}


def write_commands(path: Path, commands: Sequence[Sequence[str]], *, shell: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if shell == "ps1":
        lines = ["# Phase 6D media-profile freeze commands. Benchmark is not authorized."]
        lines.extend(" ".join(powershell_quote(str(part)) for part in command) for command in commands)
    else:
        lines = ["#!/usr/bin/env sh", "# Phase 6D media-profile freeze commands. Benchmark is not authorized."]
        lines.extend(" ".join(sh_quote(str(part)) for part in command) for command in commands)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary_markdown(path: Path, summary: Mapping[str, Any]) -> None:
    lines = [
        "Phase 6D media profile freeze summary. This is not benchmark evidence.",
        "",
        "- valid: `{0}`".format(str(summary["valid"]).lower()),
        "- ready_for_benchmark: `false`",
        "- benchmark_authorized: `false`",
        "- profile_id: `{0}`".format(summary["profile_id"]),
        "- server_role: MPD/content/media_profile source, not benchmark network",
        "- benchmark_network_source: normalized traces via TraceDrivenNetworkModel",
        "",
        "## Outputs",
        "",
    ]
    for key, value in summary["outputs"].items():
        lines.append("- `{0}`: `{1}`".format(key, value))
    if summary["warnings"]:
        lines.extend(["", "## Warnings", ""])
        lines.extend("- {0}".format(item) for item in summary["warnings"])
    if summary["errors"]:
        lines.extend(["", "## Errors", ""])
        lines.extend("- {0}".format(item) for item in summary["errors"])
    write_markdown_report(path, "Phase 6D Media Profile Freeze Summary", lines)


def write_log(path: Path, summary: Mapping[str, Any]) -> None:
    lines = [
        "Phase 6D media profile freeze",
        "valid: {0}".format(summary["valid"]),
        "ready_for_benchmark: false",
        "benchmark_authorized: false",
    ]
    for step in summary["steps"]:
        lines.append("{0}: {1} -> {2}".format(step["name"], step["status"], step["output"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def re_safe(value: str) -> bool:
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.\\/:")
    return bool(value) and all(char in allowed for char in value)


def sh_quote(value: str) -> str:
    if re_safe(value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"


def powershell_quote(value: str) -> str:
    if re_safe(value):
        return value
    return "'" + value.replace("'", "''") + "'"


if __name__ == "__main__":
    sys.exit(main())
