"""Artifact helpers with Phase 4D repo-hygiene guards."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Iterable, Mapping, Sequence


class ArtifactError(ValueError):
    """Raised when an offline artifact path violates the Phase 4D contract."""


REPO_ROOT = Path(__file__).resolve().parents[2]


def resolve_path(path: object) -> Path:
    return Path(path).expanduser().resolve()


def ensure_outside_repo(path: object, purpose: str = "artifact") -> Path:
    resolved = resolve_path(path)
    repo = REPO_ROOT.resolve()
    if resolved == repo or repo in resolved.parents:
        raise ArtifactError("{0} path must be outside the repository: {1}".format(purpose, resolved))
    return resolved


def prepare_output_dir(path: object, overwrite: bool = False, purpose: str = "artifact") -> Path:
    output_dir = ensure_outside_repo(path, purpose=purpose)
    if output_dir.exists():
        if not output_dir.is_dir():
            raise ArtifactError("{0} path exists and is not a directory: {1}".format(purpose, output_dir))
        if overwrite:
            shutil.rmtree(output_dir)
        elif any(output_dir.iterdir()):
            raise ArtifactError("{0} directory is not empty; pass --overwrite: {1}".format(purpose, output_dir))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def ensure_existing_dir(path: object, purpose: str = "artifact") -> Path:
    resolved = ensure_outside_repo(path, purpose=purpose)
    if not resolved.is_dir():
        raise ArtifactError("{0} directory does not exist: {1}".format(purpose, resolved))
    return resolved


def write_json(path: object, payload: Mapping[str, object]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def read_json(path: object) -> Mapping[str, object]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_jsonl(path: object, rows: Iterable[Mapping[str, object]]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        for row in rows:
            json.dump(row, handle, sort_keys=True)
            handle.write("\n")
    return target


def read_jsonl(path: object) -> Sequence[Mapping[str, object]]:
    rows = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                rows.append(json.loads(text))
            except json.JSONDecodeError as exc:
                raise ArtifactError("{0}: invalid JSONL at line {1}".format(path, line_number)) from exc
    return tuple(rows)
