from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence


OUTPUT_SCHEMA_VERSION = "phase6_media_profile_frozen_v1"


class Phase6DMediaProfileFreezeError(RuntimeError):
    pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Freeze a Phase 6D MPD-derived media profile.")
    parser.add_argument("--extracted-profile", required=True, type=Path)
    parser.add_argument("--validation-report", required=True, type=Path)
    parser.add_argument("--compatibility-report", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = freeze_media_profile(
            extracted_profile=args.extracted_profile,
            validation_report=args.validation_report,
            compatibility_report=args.compatibility_report,
            output=args.output,
            strict=args.strict,
        )
    except (OSError, json.JSONDecodeError, Phase6DMediaProfileFreezeError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2

    print("phase6_media_profile_freeze: PASS")
    print("output: {0}".format(report["output"]))
    return 0


def freeze_media_profile(
    *,
    extracted_profile: Path,
    validation_report: Path,
    compatibility_report: Path,
    output: Path,
    strict: bool = False,
) -> Dict[str, Any]:
    profile = read_json(extracted_profile)
    validation = read_json(validation_report)
    compatibility = read_json(compatibility_report)

    errors: List[str] = []
    if validation.get("valid") is not True:
        errors.append("validation_report valid must be true")
    hard_failures = compatibility.get("hard_failures", [])
    if hard_failures:
        errors.append("compatibility_report has hard failures: {0}".format(", ".join(str(item) for item in hard_failures)))
    if compatibility.get("compatible_primary_profile_available") is not True:
        errors.append("compatibility_report must expose a common primary media profile")
    if strict and compatibility.get("errors"):
        errors.append("strict mode rejects compatibility errors: {0}".format(", ".join(str(item) for item in compatibility.get("errors", []))))
    if errors:
        raise Phase6DMediaProfileFreezeError("; ".join(errors))

    recommendation = compatibility.get("primary_recommendation", {})
    if not isinstance(recommendation, Mapping):
        recommendation = {}

    source_checksum = str(profile.get("checksum_sha256", ""))
    if recommendation.get("action") == "freeze_subset_primary":
        frozen = subset_primary_profile(profile, recommendation)
        primary_mode = "mpd_derived_compatible_subset"
    else:
        frozen = dict(profile)
        primary_mode = "full_mpd_ladder"

    source_schema_version = str(profile.get("schema_version", ""))
    frozen["schema_version"] = OUTPUT_SCHEMA_VERSION
    frozen["source_schema_version"] = source_schema_version
    frozen["profile_role"] = "phase6_media_profile_final"
    frozen["primary_profile_mode"] = primary_mode
    frozen["primary_profile_recommendation"] = dict(recommendation)
    frozen["freeze_metadata"] = {
        "frozen_at": utc_now(),
        "frozen_by_script": "scripts/freeze_phase6_media_profile.py",
        "source_extracted_profile": str(extracted_profile),
        "source_validation_report": str(validation_report),
        "source_compatibility_report": str(compatibility_report),
        "source_extracted_profile_checksum_sha256": source_checksum,
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6d_freeze_only": True,
    }
    frozen["benchmark_authorized"] = False
    frozen["ready_for_benchmark"] = False
    frozen["phase6d_freeze_only"] = True
    frozen["vmaf_available"] = False
    frozen["perceptual_metrics_available"] = False
    frozen["checksum_sha256"] = sha256_json(without_keys(frozen, {"checksum_sha256", "frozen_profile_sha256"}))
    frozen["frozen_profile_sha256"] = sha256_json(without_keys(frozen, {"frozen_profile_sha256"}))

    write_json(output, frozen)
    return {
        "output": str(output),
        "representations": len(frozen.get("representations", [])),
        "primary_profile_mode": primary_mode,
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
    }


def subset_primary_profile(profile: Mapping[str, Any], recommendation: Mapping[str, Any]) -> Dict[str, Any]:
    selected_indices = [int(item) for item in recommendation.get("selected_representation_indices", [])]
    if len(selected_indices) < 2:
        raise Phase6DMediaProfileFreezeError("subset recommendation must select at least 2 representations")

    source_representations = profile.get("representations", [])
    if not isinstance(source_representations, list):
        raise Phase6DMediaProfileFreezeError("profile representations must be a list")

    by_index = {
        int(item.get("representation_index")): item
        for item in source_representations
        if isinstance(item, Mapping) and item.get("representation_index") is not None
    }
    missing = [index for index in selected_indices if index not in by_index]
    if missing:
        raise Phase6DMediaProfileFreezeError("subset recommendation references missing representation indices: {0}".format(missing))

    old_to_new = {old_index: new_index for new_index, old_index in enumerate(selected_indices)}
    representations = []
    for old_index in selected_indices:
        item = dict(by_index[old_index])
        item["source_representation_index"] = old_index
        item["representation_index"] = old_to_new[old_index]
        representations.append(item)

    frozen = dict(profile)
    frozen["representations"] = representations
    frozen["primary_representation_count"] = len(representations)
    frozen["primary_source_representation_indices"] = selected_indices
    frozen["primary_source_mpd_representation_ids"] = [item.get("mpd_representation_id", "") for item in representations]
    frozen["primary_source_bitrate_kbps"] = [item.get("bitrate_kbps") for item in representations]
    frozen["diagnostic_profiles"] = [
        {
            "profile_role": "diagnostic_full_mpd_ladder",
            "reason": "Full MPD-derived ladder retained externally because the neural bundle did not support it as primary.",
            "profile": dict(profile),
        }
    ]
    frozen["segments"] = subset_segments(profile.get("segments", []), old_to_new)
    frozen["size_source_counts"] = count_size_sources(frozen["segments"])
    return frozen


def subset_segments(segments: Any, old_to_new: Mapping[int, int]) -> List[Dict[str, Any]]:
    if not isinstance(segments, list):
        raise Phase6DMediaProfileFreezeError("profile segments must be a list")
    remapped = []
    map_fields = (
        "media_path_by_representation",
        "initialization_path_by_representation",
        "size_bytes_by_representation",
        "size_source_by_representation",
    )
    for segment in segments:
        if not isinstance(segment, Mapping):
            raise Phase6DMediaProfileFreezeError("profile segment must be an object")
        new_segment = dict(segment)
        for field in map_fields:
            old_map = segment.get(field, {})
            if not isinstance(old_map, Mapping):
                old_map = {}
            new_segment[field] = {
                str(new_index): old_map.get(str(old_index))
                for old_index, new_index in sorted(old_to_new.items(), key=lambda item: item[1])
            }
        remapped.append(new_segment)
    return remapped


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def sha256_json(data: Mapping[str, Any]) -> str:
    return hashlib.sha256(json.dumps(data, indent=2, sort_keys=True).encode("utf-8")).hexdigest()


def without_keys(data: Mapping[str, Any], keys: set[str]) -> Dict[str, Any]:
    return {key: value for key, value in data.items() if key not in keys}


def count_size_sources(segments: Sequence[Mapping[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for segment in segments:
        sources = segment.get("size_source_by_representation", {})
        if isinstance(sources, Mapping):
            for source in sources.values():
                key = str(source)
                counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    sys.exit(main())
