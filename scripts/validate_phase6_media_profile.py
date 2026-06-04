from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence


OUTPUT_SCHEMA_VERSION = "phase6_media_profile_validation_v1"
RECOGNIZED_PROFILE_SCHEMAS = {
    "phase6_media_profile_extracted_v1",
    "phase6_media_profile_frozen_v1",
}
REAL_SIZE_SOURCES = {"file_size", "http_head"}


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Phase 6D MPD-derived media profile.")
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = validate_media_profile(args.profile, strict=args.strict)
        write_json(args.output, report)
    except (OSError, json.JSONDecodeError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6_media_profile_validation: {0}".format("PASS" if report["valid"] else "ERRORS"))
    print("output: {0}".format(args.output))
    if args.fail_on_error and report["errors"]:
        return 2
    return 0


def validate_media_profile(profile_path: Path, *, strict: bool = False) -> Dict[str, Any]:
    data = json.loads(profile_path.read_text(encoding="utf-8-sig"))
    errors: List[str] = []
    warnings: List[str] = []

    if not isinstance(data, Mapping):
        errors.append("profile root must be a JSON object")
        data = {}

    schema_version = str(data.get("schema_version", ""))
    if schema_version not in RECOGNIZED_PROFILE_SCHEMAS:
        errors.append("unrecognized schema_version: {0}".format(schema_version or "<missing>"))

    if not str(data.get("media_profile_id", "")).strip():
        errors.append("media_profile_id is required")

    segment_duration_s = float_value(data.get("segment_duration_s"))
    segment_count = int_value(data.get("segment_count"))
    mpd_duration_s = float_value(data.get("mpd_duration_s"))
    if segment_duration_s <= 0:
        errors.append("segment_duration_s must be positive")
    if segment_count <= 0:
        errors.append("segment_count must be positive")
    if segment_count and segment_count < 10:
        warnings.append("segment_count_is_small: {0}".format(segment_count))
    if mpd_duration_s and mpd_duration_s <= 60.0:
        warnings.append("media_duration_is_short: {0} seconds".format(format_number(mpd_duration_s)))

    representations = data.get("representations")
    if not isinstance(representations, list):
        errors.append("representations must be a list")
        representations = []
    if len(representations) < 2:
        errors.append("at least 2 representations are required")

    validate_representations(representations, errors)
    validate_segments(data.get("segments"), representations, errors, warnings)

    if data.get("benchmark_authorized") is not False:
        errors.append("benchmark_authorized must be false")
    if data.get("ready_for_benchmark") is not False:
        errors.append("ready_for_benchmark must be false")
    if data.get("vmaf_available") is True:
        errors.append("vmaf_available must remain false unless Phase 6D VMAF artifacts exist")
    if data.get("perceptual_metrics_available") is True:
        errors.append("perceptual_metrics_available must remain false in Phase 6D")

    return {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "profile": str(profile_path),
        "strict": bool(strict),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": {
            "representations": len(representations),
            "segments": len(data.get("segments", [])) if isinstance(data.get("segments"), list) else 0,
            "errors": len(errors),
            "warnings": len(warnings),
        },
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6d_freeze_only": True,
    }


def validate_representations(representations: Sequence[Any], errors: List[str]) -> None:
    indices: List[int] = []
    bitrates: List[int] = []
    for offset, item in enumerate(representations):
        if not isinstance(item, Mapping):
            errors.append("representation {0} must be an object".format(offset))
            continue
        index = int_value(item.get("representation_index"), missing=-1)
        bitrate = int_value(item.get("bitrate_kbps"), missing=0)
        indices.append(index)
        bitrates.append(bitrate)
        if not isinstance(index, int) or index < 0:
            errors.append("representation {0} representation_index must be a non-negative integer".format(offset))
        if bitrate <= 0:
            errors.append("representation {0} bitrate_kbps must be positive".format(offset))
        if not str(item.get("mpd_representation_id", "")).strip():
            errors.append("representation {0} must preserve mpd_representation_id".format(offset))

    expected = list(range(len(representations)))
    if sorted(indices) != expected:
        errors.append("representation_index values must be unique integers starting at 0")

    for previous, current in zip(bitrates, bitrates[1:]):
        if current <= previous:
            errors.append("bitrate_kbps must be strictly increasing in representation order")
            break


def validate_segments(
    segments: Any,
    representations: Sequence[Any],
    errors: List[str],
    warnings: List[str],
) -> None:
    if not isinstance(segments, list):
        errors.append("segments must be a list")
        return

    expected_keys = {
        str(item.get("representation_index"))
        for item in representations
        if isinstance(item, Mapping) and isinstance(item.get("representation_index"), int)
    }
    size_sources_seen = set()

    for offset, segment in enumerate(segments):
        if not isinstance(segment, Mapping):
            errors.append("segment {0} must be an object".format(offset))
            continue
        duration = float_value(segment.get("duration_s"))
        if duration <= 0:
            errors.append("segment {0} duration_s must be positive".format(offset))

        sizes = segment.get("size_bytes_by_representation")
        if not isinstance(sizes, Mapping):
            errors.append("segment {0} missing size_bytes_by_representation".format(offset))
            continue
        if expected_keys and set(str(key) for key in sizes.keys()) != expected_keys:
            errors.append("segment {0} size map must include every representation".format(offset))
        for key, value in sizes.items():
            if int_value(value, missing=0) <= 0:
                errors.append("segment {0} representation {1} size_bytes must be positive".format(offset, key))

        sources = segment.get("size_source_by_representation")
        if isinstance(sources, Mapping):
            size_sources_seen.update(str(value) for value in sources.values())

    if segments and not (size_sources_seen & REAL_SIZE_SOURCES):
        warnings.append("all_segment_sizes_are_estimated")


def float_value(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def int_value(value: Any, *, missing: int = 0) -> int:
    if value is None:
        return missing
    if isinstance(value, bool):
        return missing
    try:
        return int(value)
    except (TypeError, ValueError):
        return missing


def format_number(value: float) -> str:
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return str(value)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
