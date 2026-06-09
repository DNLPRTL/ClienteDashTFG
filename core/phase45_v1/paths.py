from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


class Phase45PathError(ValueError):
    """Raised when an external Phase 4-5 v1 path cannot be resolved."""


@dataclass(frozen=True)
class PathRewriteRule:
    source_prefix: str
    target_prefix: str

    def apply(self, value: str) -> str:
        source = self.source_prefix.rstrip("/\\")
        target = self.target_prefix.rstrip("/\\")
        text = str(value)
        if text == source:
            return target
        if text.startswith(source + "/") or text.startswith(source + "\\"):
            suffix = text[len(source) :].lstrip("/\\")
            return str(Path(target) / Path(*suffix.replace("\\", "/").split("/")))
        return text

    def to_json(self) -> dict[str, object]:
        return {"source_prefix": self.source_prefix, "target_prefix": self.target_prefix}


def parse_rewrite_rule(value: str) -> PathRewriteRule:
    if "=" not in str(value):
        raise Phase45PathError("trace path rewrite must have OLD=NEW format")
    source, target = str(value).split("=", 1)
    source = source.strip()
    target = target.strip()
    if not source or not target:
        raise Phase45PathError("trace path rewrite OLD and NEW must be non-empty")
    return PathRewriteRule(source_prefix=source, target_prefix=str(Path(target).expanduser()))


def parse_rewrite_rules(values: Iterable[str]) -> tuple[PathRewriteRule, ...]:
    return tuple(parse_rewrite_rule(value) for value in values)


def default_trace_path_rewrites(tfg_root: Path) -> tuple[PathRewriteRule, ...]:
    root = Path(tfg_root).expanduser()
    rules: list[PathRewriteRule] = []
    if os.name == "nt":
        rules.append(PathRewriteRule("/home/daniel/TFG", str(root)))
        rules.append(PathRewriteRule("/home/danie/TFG", str(root)))
    else:
        home_tfg = Path.home() / "TFG"
        for linux_home in (Path("/home/daniel/TFG"), Path("/home/danie/TFG")):
            if linux_home != home_tfg and not linux_home.exists():
                rules.append(PathRewriteRule(linux_home.as_posix(), home_tfg.as_posix()))
    return tuple(rules)


def resolve_external_trace_path(raw_path: object, rules: Sequence[PathRewriteRule]) -> Path:
    text = str(raw_path)
    rewritten = text
    for rule in rules:
        next_value = rule.apply(rewritten)
        if next_value != rewritten:
            rewritten = next_value
            break
    return Path(rewritten).expanduser()
