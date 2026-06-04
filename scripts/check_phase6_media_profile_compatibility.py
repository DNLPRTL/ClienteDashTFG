from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set


OUTPUT_SCHEMA_VERSION = "phase6_media_profile_compatibility_v1"
REQUIRED_CONTROLLERS = (
    "min_rate",
    "fixed_rate",
    "max_rate",
    "rate_based",
    "bba",
    "bola",
    "mpc",
    "robust_mpc",
    "neural_abr_lite",
)
NEURAL_METADATA_FILES = (
    "bundle_manifest.json",
    "ladder_schema.json",
    "inference_contract.json",
)
COUNT_KEYS = {
    "num_actions",
    "action_count",
    "actions",
    "n_actions",
    "candidate_count",
    "num_candidates",
    "n_candidates",
    "representation_count",
    "num_representations",
    "n_representations",
    "ladder_size",
    "num_quality_levels",
    "n_quality_levels",
    "quality_count",
    "output_dim",
}
LIST_COUNT_KEYS = {
    "representations",
    "ladder",
    "bitrates",
    "bitrate_kbps",
    "bitrate_bps",
    "candidate_bitrates",
    "candidate_bitrates_kbps",
    "candidate_bitrates_bps",
    "actions",
    "action_space",
    "quality_levels",
}


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Check Phase 6D media-profile/controller compatibility.")
    parser.add_argument("--media-profile", required=True, type=Path)
    parser.add_argument("--neural-bundle-root", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    try:
        report = check_media_profile_compatibility(
            media_profile=args.media_profile,
            neural_bundle_root=args.neural_bundle_root,
            strict=args.strict,
        )
        write_json(args.output, report)
    except (OSError, json.JSONDecodeError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6_media_profile_compatibility: {0}".format("PASS" if report["valid"] else "WARN_OR_FAIL"))
    print("output: {0}".format(args.output))
    return 0 if report["valid"] else 2


def check_media_profile_compatibility(
    *,
    media_profile: Path,
    neural_bundle_root: Optional[Path] = None,
    strict: bool = False,
) -> Dict[str, Any]:
    profile = json.loads(media_profile.read_text(encoding="utf-8-sig"))
    errors: List[str] = []
    warnings: List[str] = []
    hard_failures: List[str] = []

    representations = profile.get("representations", [])
    ladder = ladder_summary(representations)
    if not ladder:
        errors.append("representation_ladder_empty")
        hard_failures.append("representation_ladder_empty")
    if not is_ascending(ladder):
        errors.append("representation_ladder_not_ascending")
        hard_failures.append("representation_ladder_not_ascending")

    controller_matrix = [
        {
            "controller": controller,
            "uses_representation_index": True,
            "compatible_with_primary_profile": bool(ladder),
        }
        for controller in REQUIRED_CONTROLLERS
    ]

    neural_report = neural_bundle_report(
        neural_bundle_root=neural_bundle_root,
        representation_count=len(ladder),
        ladder=ladder,
        strict=strict,
        errors=errors,
        warnings=warnings,
        hard_failures=hard_failures,
    )
    primary_recommendation = build_primary_recommendation(ladder, neural_report)

    if primary_recommendation["action"] == "manual_review_required":
        hard_failures.append("no_common_primary_media_profile")
        errors.append("no_common_primary_media_profile")

    return {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "media_profile": str(media_profile),
        "strict": bool(strict),
        "representation_count": len(ladder),
        "representation_ladder": ladder,
        "representation_order": "ascending_bitrate" if is_ascending(ladder) else "invalid",
        "controllers": controller_matrix,
        "neural_abr_lite": neural_report,
        "full_ladder_compatible": neural_report.get("full_ladder_compatible", "unknown"),
        "compatible_primary_profile_available": bool(primary_recommendation["compatible_primary_profile_available"]),
        "primary_recommendation": primary_recommendation,
        "valid": not errors and not hard_failures,
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "hard_failures": sorted(set(hard_failures)),
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6d_freeze_only": True,
    }


def ladder_summary(representations: Any) -> List[Dict[str, Any]]:
    if not isinstance(representations, list):
        return []
    ladder: List[Dict[str, Any]] = []
    for item in representations:
        if not isinstance(item, Mapping):
            continue
        ladder.append(
            {
                "representation_index": int_value(item.get("representation_index"), missing=-1),
                "mpd_representation_id": str(item.get("mpd_representation_id", "")),
                "bitrate_kbps": int_value(item.get("bitrate_kbps"), missing=0),
                "bandwidth_bps": int_value(item.get("bandwidth_bps"), missing=0),
            }
        )
    return ladder


def is_ascending(ladder: Sequence[Mapping[str, Any]]) -> bool:
    if not ladder:
        return False
    indices = [int_value(item.get("representation_index"), missing=-1) for item in ladder]
    bitrates = [int_value(item.get("bitrate_kbps"), missing=0) for item in ladder]
    return indices == list(range(len(ladder))) and all(current > previous for previous, current in zip(bitrates, bitrates[1:]))


def neural_bundle_report(
    *,
    neural_bundle_root: Optional[Path],
    representation_count: int,
    ladder: Sequence[Mapping[str, Any]],
    strict: bool,
    errors: List[str],
    warnings: List[str],
    hard_failures: List[str],
) -> Dict[str, Any]:
    if neural_bundle_root is None:
        warnings.append("bundle_not_checked")
        return {
            "checked": False,
            "bundle_root": None,
            "metadata_files_inspected": [],
            "expected_candidate_counts": [],
            "full_ladder_compatible": "unknown",
            "compatible": "unknown",
            "warning": "bundle_not_checked",
            "notes": [
                "No neural bundle path was provided; Phase 6D does not fail this case.",
            ],
        }

    root = Path(neural_bundle_root)
    inspected: List[Dict[str, Any]] = []
    expected_counts: Set[int] = set()
    missing_files: List[str] = []
    for filename in NEURAL_METADATA_FILES:
        path = root / filename
        if not path.is_file():
            missing_files.append(filename)
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError as exc:
            warnings.append("neural_metadata_json_error:{0}".format(filename))
            inspected.append({"file": str(path), "status": "json_error", "error": str(exc)})
            continue
        counts = infer_candidate_counts(data)
        expected_counts.update(counts)
        inspected.append({"file": str(path), "status": "read", "candidate_counts": sorted(counts)})

    if missing_files:
        warnings.append("neural_metadata_files_missing:{0}".format(",".join(missing_files)))

    if not expected_counts:
        warnings.append("neural_bundle_candidate_count_unknown")
        if strict:
            errors.append("neural_bundle_candidate_count_unknown")
        return {
            "checked": True,
            "bundle_root": str(root),
            "metadata_files_inspected": inspected,
            "metadata_files_missing": missing_files,
            "expected_candidate_counts": [],
            "full_ladder_compatible": "unknown",
            "compatible": "unknown",
            "notes": ["Candidate/action count could not be inferred from JSON metadata."],
        }

    full_compatible = representation_count in expected_counts
    if full_compatible:
        return {
            "checked": True,
            "bundle_root": str(root),
            "metadata_files_inspected": inspected,
            "metadata_files_missing": missing_files,
            "expected_candidate_counts": sorted(expected_counts),
            "full_ladder_compatible": True,
            "compatible": True,
            "notes": ["The neural bundle metadata supports the full MPD-derived ladder."],
        }

    subset_counts = sorted(count for count in expected_counts if 1 < count < representation_count)
    if subset_counts:
        warnings.append("full_ladder_incompatible_but_subset_available")
        selected = subset_counts[-1]
        return {
            "checked": True,
            "bundle_root": str(root),
            "metadata_files_inspected": inspected,
            "metadata_files_missing": missing_files,
            "expected_candidate_counts": sorted(expected_counts),
            "full_ladder_compatible": False,
            "compatible": False,
            "compatible_subset_candidate_count": selected,
            "compatible_subset": ladder[:selected],
            "notes": [
                "The full ladder is not compatible with the neural bundle candidate count.",
                "A common primary profile can be frozen from the MPD-derived low-to-high subset.",
            ],
        }

    hard_failures.append("neural_bundle_candidate_count_incompatible")
    errors.append("neural_bundle_candidate_count_incompatible")
    return {
        "checked": True,
        "bundle_root": str(root),
        "metadata_files_inspected": inspected,
        "metadata_files_missing": missing_files,
        "expected_candidate_counts": sorted(expected_counts),
        "full_ladder_compatible": False,
        "compatible": False,
        "notes": ["No compatible full ladder or common subset was found."],
    }


def build_primary_recommendation(
    ladder: Sequence[Mapping[str, Any]],
    neural_report: Mapping[str, Any],
) -> Dict[str, Any]:
    if not ladder:
        return {
            "action": "manual_review_required",
            "compatible_primary_profile_available": False,
            "reason": "empty_ladder",
        }
    if neural_report.get("checked") is False:
        return {
            "action": "use_full_ladder_unchecked_neural_bundle",
            "compatible_primary_profile_available": True,
            "selected_representation_indices": [item["representation_index"] for item in ladder],
            "selected_mpd_representation_ids": [item["mpd_representation_id"] for item in ladder],
            "selected_bitrate_kbps": [item["bitrate_kbps"] for item in ladder],
            "diagnostic_full_ladder": False,
            "reason": "bundle_not_checked",
        }
    if neural_report.get("full_ladder_compatible") is True:
        return {
            "action": "use_full_ladder",
            "compatible_primary_profile_available": True,
            "selected_representation_indices": [item["representation_index"] for item in ladder],
            "selected_mpd_representation_ids": [item["mpd_representation_id"] for item in ladder],
            "selected_bitrate_kbps": [item["bitrate_kbps"] for item in ladder],
            "diagnostic_full_ladder": False,
            "reason": "full_mpd_ladder_supported",
        }
    if neural_report.get("full_ladder_compatible") == "unknown":
        return {
            "action": "use_full_ladder_unknown_neural_bundle",
            "compatible_primary_profile_available": True,
            "selected_representation_indices": [item["representation_index"] for item in ladder],
            "selected_mpd_representation_ids": [item["mpd_representation_id"] for item in ladder],
            "selected_bitrate_kbps": [item["bitrate_kbps"] for item in ladder],
            "diagnostic_full_ladder": False,
            "reason": "neural_bundle_candidate_count_unknown",
        }
    subset = neural_report.get("compatible_subset")
    if isinstance(subset, list) and subset:
        return {
            "action": "freeze_subset_primary",
            "compatible_primary_profile_available": True,
            "selected_representation_indices": [item["representation_index"] for item in subset],
            "selected_mpd_representation_ids": [item["mpd_representation_id"] for item in subset],
            "selected_bitrate_kbps": [item["bitrate_kbps"] for item in subset],
            "diagnostic_full_ladder": True,
            "reason": "neural_bundle_candidate_count_requires_common_subset",
        }
    return {
        "action": "manual_review_required",
        "compatible_primary_profile_available": False,
        "reason": "no_common_controller_ladder",
    }


def infer_candidate_counts(data: Any) -> Set[int]:
    counts: Set[int] = set()

    def visit(value: Any, key: str = "") -> None:
        normalized_key = key.lower()
        if isinstance(value, Mapping):
            for child_key, child_value in value.items():
                child_key_str = str(child_key)
                if child_key_str.lower() in COUNT_KEYS:
                    maybe_add_count(child_value, counts)
                if child_key_str.lower() in LIST_COUNT_KEYS and isinstance(child_value, list):
                    counts.add(len(child_value))
                visit(child_value, child_key_str)
        elif isinstance(value, list):
            if normalized_key in LIST_COUNT_KEYS:
                counts.add(len(value))
            for item in value:
                visit(item, normalized_key)

    visit(data)
    return {count for count in counts if count > 1}


def maybe_add_count(value: Any, counts: Set[int]) -> None:
    if isinstance(value, bool):
        return
    if isinstance(value, int):
        counts.add(value)
    elif isinstance(value, float) and value.is_integer():
        counts.add(int(value))
    elif isinstance(value, str):
        try:
            counts.add(int(value.strip()))
        except ValueError:
            return
    elif isinstance(value, list):
        counts.add(len(value))


def int_value(value: Any, *, missing: int) -> int:
    if value is None or isinstance(value, bool):
        return missing
    try:
        return int(value)
    except (TypeError, ValueError):
        return missing


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
