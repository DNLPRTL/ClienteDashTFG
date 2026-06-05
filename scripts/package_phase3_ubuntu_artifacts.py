#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
TFG_ROOT = REPO_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.trace_replay.manifest_validation import validate_phase3_trace_manifest_data


DEFAULT_PAYLOAD_ROOT = TFG_ROOT / "ubuntu_phase3_ready_for_TFGv1"
DEFAULT_ZIP_PATH = TFG_ROOT / "ubuntu_phase3_ready_for_TFGv1.zip"
DEFAULT_LINUX_ROOT = "/home/daniel/TFG"
PHASE3_MANIFESTS = (
    "phase3_trace_manifest_final.json",
    "phase3_trace_manifest_curated.json",
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Package Phase 3 external artifacts with Ubuntu absolute paths.")
    parser.add_argument("--payload-root", type=Path, default=DEFAULT_PAYLOAD_ROOT)
    parser.add_argument("--zip-path", type=Path, default=DEFAULT_ZIP_PATH)
    parser.add_argument("--linux-root", default=DEFAULT_LINUX_ROOT)
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args(argv)

    payload = args.payload_root
    if args.clean and payload.exists():
        _assert_under_tfg(payload)
        shutil.rmtree(payload)
    payload.mkdir(parents=True, exist_ok=True)
    _copy_payload(TFG_ROOT, payload)
    rewrite_summary = _rewrite_paths(payload, windows_root=str(TFG_ROOT), linux_root=args.linux_root)
    validation_summary = _validate_payload_manifests(payload, linux_root=args.linux_root)
    _write_zip(payload, args.zip_path)
    print(
        json.dumps(
            {
                "status": "PASS",
                "payload_root": str(payload),
                "zip_path": str(args.zip_path),
                "zip_size_bytes": args.zip_path.stat().st_size,
                "rewrite_summary": rewrite_summary,
                "validation_summary": validation_summary,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def _copy_payload(source_root: Path, payload: Path) -> None:
    copy_specs = (
        (source_root / "datasets_normalizados" / "phase3" / "final", payload / "datasets_normalizados" / "phase3" / "final"),
        (source_root / "manifests_trazas" / "phase3" / "final", payload / "manifests_trazas" / "phase3" / "final"),
        (source_root / "auditorias_trazas" / "phase3" / "final", payload / "auditorias_trazas" / "phase3" / "final"),
        (source_root / "runs_trazas", payload / "runs_trazas"),
    )
    for source, target in copy_specs:
        if not source.exists():
            continue
        if target.exists():
            shutil.rmtree(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)


def _rewrite_paths(payload: Path, windows_root: str, linux_root: str) -> dict[str, object]:
    windows_variants = (windows_root, windows_root.replace("\\", "/"))
    changed_files = 0
    changed_strings = 0

    def rewrite_obj(obj):
        nonlocal changed_strings
        if isinstance(obj, dict):
            return {key: rewrite_obj(value) for key, value in obj.items()}
        if isinstance(obj, list):
            return [rewrite_obj(value) for value in obj]
        if isinstance(obj, str):
            original = obj
            for variant in windows_variants:
                obj = obj.replace(variant, linux_root)
            if obj != original:
                changed_strings += 1
                obj = obj.replace("\\", "/")
            return obj
        return obj

    for path in payload.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        rewritten = rewrite_obj(data)
        if rewritten != data:
            changed_files += 1
            path.write_text(json.dumps(rewritten, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for suffix in (".md", ".txt"):
        for path in payload.rglob("*{0}".format(suffix)):
            text = path.read_text(encoding="utf-8", errors="replace")
            new_text = text
            for variant in windows_variants:
                new_text = new_text.replace(variant, linux_root)
            if new_text != text:
                changed_files += 1
                changed_strings += 1
                path.write_text(new_text.replace("\\", "/"), encoding="utf-8")
    offenders = _find_windows_path_offenders(payload, windows_root)
    if offenders:
        raise RuntimeError("Windows paths remain in payload: {0}".format("; ".join(offenders[:10])))
    return {"changed_files": changed_files, "changed_strings": changed_strings}


def _validate_payload_manifests(payload: Path, linux_root: str) -> list[dict[str, object]]:
    results = []
    manifest_root = payload / "manifests_trazas" / "phase3" / "final"
    for name in PHASE3_MANIFESTS:
        path = manifest_root / name
        manifest = json.loads(path.read_text(encoding="utf-8"))
        localized = _localize_paths(manifest, linux_root=linux_root, payload=payload)
        summary = validate_phase3_trace_manifest_data(localized)
        summary["manifest"] = name
        results.append(summary)
    return results


def _localize_paths(obj, linux_root: str, payload: Path):
    if isinstance(obj, dict):
        return {key: _localize_paths(value, linux_root, payload) for key, value in obj.items()}
    if isinstance(obj, list):
        return [_localize_paths(value, linux_root, payload) for value in obj]
    if isinstance(obj, str) and linux_root in obj:
        return obj.replace(linux_root, payload.as_posix())
    return obj


def _write_zip(payload: Path, zip_path: Path) -> None:
    if zip_path.exists():
        _assert_under_tfg(zip_path)
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(payload.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(payload))


def _find_windows_path_offenders(payload: Path, windows_root: str) -> list[str]:
    offenders = []
    needles = (windows_root, windows_root.replace("\\", "/"))
    for path in payload.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".json", ".md", ".txt", ".csv"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if any(needle in text for needle in needles):
            offenders.append(str(path))
    return offenders


def _assert_under_tfg(path: Path) -> None:
    resolved = path.resolve()
    root = TFG_ROOT.resolve()
    if not str(resolved).startswith(str(root)):
        raise ValueError("refusing to mutate outside TFG root: {0}".format(resolved))


if __name__ == "__main__":
    raise SystemExit(main())
