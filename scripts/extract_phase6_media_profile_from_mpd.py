from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


OUTPUT_SCHEMA_VERSION = "phase6_media_profile_extracted_v1"
DEFAULT_PROFILE_ID = "media_profile_phase6_v1"
SIZE_POLICIES = ("bitrate_estimate", "file_size", "http_head")


class Phase6DMediaProfileError(RuntimeError):
    pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Extract a Phase 6D media profile from a real MPEG-DASH MPD.")
    parser.add_argument("--mpd", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--content-root", type=Path)
    parser.add_argument("--base-url")
    parser.add_argument("--profile-id", default=DEFAULT_PROFILE_ID)
    parser.add_argument("--prefer-real-segment-sizes", action="store_true")
    parser.add_argument("--size-policy", choices=SIZE_POLICIES, default="bitrate_estimate")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    try:
        profile = extract_media_profile(
            mpd=args.mpd,
            output=args.output,
            content_root=args.content_root,
            base_url=args.base_url,
            profile_id=args.profile_id,
            prefer_real_segment_sizes=args.prefer_real_segment_sizes,
            size_policy=args.size_policy,
            strict=args.strict,
        )
    except (OSError, ET.ParseError, Phase6DMediaProfileError) as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2

    print("phase6_media_profile_extract: PASS")
    print("output: {0}".format(args.output))
    print("representations: {0}".format(len(profile["representations"])))
    print("segments: {0}".format(profile["segment_count"]))
    return 0


def extract_media_profile(
    *,
    mpd: str,
    output: Path,
    content_root: Optional[Path] = None,
    base_url: Optional[str] = None,
    profile_id: str = DEFAULT_PROFILE_ID,
    prefer_real_segment_sizes: bool = False,
    size_policy: str = "bitrate_estimate",
    strict: bool = False,
) -> Dict[str, Any]:
    if size_policy not in SIZE_POLICIES:
        raise Phase6DMediaProfileError("unsupported size_policy: {0}".format(size_policy))

    effective_size_policy = choose_size_policy(
        size_policy=size_policy,
        prefer_real_segment_sizes=prefer_real_segment_sizes,
        content_root=content_root,
        base_url=base_url,
    )
    source_mpd, xml_text = read_mpd(mpd)
    profile = build_profile_from_mpd_xml(
        xml_text,
        source_mpd=source_mpd,
        profile_id=profile_id,
        content_root=content_root,
        base_url=base_url,
        size_policy=effective_size_policy,
        requested_size_policy=size_policy,
        prefer_real_segment_sizes=prefer_real_segment_sizes,
        strict=strict,
    )
    write_json(output, profile)
    return profile


def build_profile_from_mpd_xml(
    xml_text: str,
    *,
    source_mpd: str,
    profile_id: str,
    content_root: Optional[Path],
    base_url: Optional[str],
    size_policy: str,
    requested_size_policy: str,
    prefer_real_segment_sizes: bool,
    strict: bool,
) -> Dict[str, Any]:
    root = ET.fromstring(xml_text)
    if local_name(root.tag) != "MPD":
        raise Phase6DMediaProfileError("root XML element must be MPD")

    periods = elements_by_local_name(root, "Period")
    if not periods:
        raise Phase6DMediaProfileError("MPD has no Period")
    period = periods[0]

    mpd_duration_s = duration_from_attrs(root, period)
    if mpd_duration_s <= 0:
        raise Phase6DMediaProfileError("MPD duration must be positive")

    adaptation_set = select_video_adaptation_set(period)
    segment_template = nearest_segment_template(adaptation_set, None)
    representations = elements_by_local_name(adaptation_set, "Representation")
    if not representations:
        raise Phase6DMediaProfileError("selected AdaptationSet has no Representation")

    parsed_representations: List[Dict[str, Any]] = []
    representation_templates: Dict[str, Dict[str, Any]] = {}
    for representation in representations:
        template = nearest_segment_template(representation, segment_template)
        parsed_template = parse_segment_template(template)
        if not parsed_template["duration"]:
            raise Phase6DMediaProfileError("SegmentTemplate duration is required")
        if not parsed_template["timescale"]:
            raise Phase6DMediaProfileError("SegmentTemplate timescale is required")
        rep = parse_representation(representation, adaptation_set)
        parsed_representations.append(rep)
        representation_templates[rep["mpd_representation_id"]] = parsed_template

    parsed_representations.sort(key=lambda item: (item["bitrate_kbps"], item["bandwidth_bps"], item["mpd_representation_id"]))
    for index, representation in enumerate(parsed_representations):
        representation["representation_index"] = index

    first_template = representation_templates[parsed_representations[0]["mpd_representation_id"]]
    segment_duration_s = float(first_template["duration"]) / float(first_template["timescale"])
    if segment_duration_s <= 0:
        raise Phase6DMediaProfileError("computed segment_duration_s must be positive")

    for template in representation_templates.values():
        current = float(template["duration"]) / float(template["timescale"])
        if abs(current - segment_duration_s) > 1e-9 and strict:
            raise Phase6DMediaProfileError("strict mode requires a common SegmentTemplate duration")

    segment_count = compute_segment_count(mpd_duration_s, segment_duration_s)
    if segment_count <= 0:
        raise Phase6DMediaProfileError("computed segment_count must be positive")

    segments = build_segments(
        representations=parsed_representations,
        templates=representation_templates,
        segment_count=segment_count,
        segment_duration_s=segment_duration_s,
        mpd_duration_s=mpd_duration_s,
        content_root=content_root,
        base_url=base_url,
        size_policy=size_policy,
    )

    template_summary = dict(first_template)
    template_summary["segment_duration_s"] = round_float(segment_duration_s)
    profile: Dict[str, Any] = {
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "media_profile_id": profile_id,
        "source_mpd": source_mpd,
        "extracted_at": utc_now(),
        "mpd_duration_s": round_float(mpd_duration_s),
        "segment_duration_s": round_float(segment_duration_s),
        "segment_count": segment_count,
        "representations": parsed_representations,
        "segments": segments,
        "segment_template": template_summary,
        "size_policy": size_policy,
        "requested_size_policy": requested_size_policy,
        "prefer_real_segment_sizes": bool(prefer_real_segment_sizes),
        "size_source_counts": count_size_sources(segments),
        "representation_order": "ascending_bitrate",
        "benchmark_authorized": False,
        "ready_for_benchmark": False,
        "phase6d_freeze_only": True,
        "vmaf_available": False,
        "perceptual_metrics_available": False,
    }
    profile["checksum_sha256"] = sha256_json(profile)
    return profile


def choose_size_policy(
    *,
    size_policy: str,
    prefer_real_segment_sizes: bool,
    content_root: Optional[Path],
    base_url: Optional[str],
) -> str:
    if size_policy == "bitrate_estimate" and content_root is not None:
        return "file_size"
    if prefer_real_segment_sizes and size_policy == "bitrate_estimate":
        if content_root is not None:
            return "file_size"
        if base_url:
            return "http_head"
    return size_policy


def read_mpd(mpd: str) -> Tuple[str, str]:
    if is_url(mpd):
        with urllib.request.urlopen(mpd, timeout=20) as response:
            payload = response.read()
        return mpd, payload.decode("utf-8-sig")
    path = Path(mpd)
    return str(path), path.read_text(encoding="utf-8-sig")


def is_url(value: str) -> bool:
    scheme = urllib.parse.urlparse(value).scheme.lower()
    return scheme in ("http", "https")


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def elements_by_local_name(root: ET.Element, name: str) -> List[ET.Element]:
    return [element for element in root.iter() if local_name(element.tag) == name]


def direct_children_by_local_name(root: ET.Element, name: str) -> List[ET.Element]:
    return [element for element in list(root) if local_name(element.tag) == name]


def select_video_adaptation_set(period: ET.Element) -> ET.Element:
    adaptation_sets = direct_children_by_local_name(period, "AdaptationSet")
    if not adaptation_sets:
        raise Phase6DMediaProfileError("Period has no AdaptationSet")

    for adaptation_set in adaptation_sets:
        mime_type = str(adaptation_set.attrib.get("mimeType", "")).lower()
        content_type = str(adaptation_set.attrib.get("contentType", "")).lower()
        if "video" in mime_type or content_type == "video":
            return adaptation_set
    return adaptation_sets[0]


def nearest_segment_template(element: ET.Element, fallback: Optional[ET.Element]) -> ET.Element:
    templates = direct_children_by_local_name(element, "SegmentTemplate")
    if templates:
        return templates[0]
    if fallback is not None:
        return fallback
    raise Phase6DMediaProfileError("SegmentTemplate is required")


def duration_from_attrs(root: ET.Element, period: ET.Element) -> float:
    for element, attr in ((period, "duration"), (root, "mediaPresentationDuration")):
        value = element.attrib.get(attr)
        if value:
            return parse_iso8601_duration(value)
    return 0.0


def parse_iso8601_duration(value: str) -> float:
    pattern = re.compile(
        r"^P"
        r"(?:(?P<days>[0-9]+(?:\.[0-9]+)?)D)?"
        r"(?:T"
        r"(?:(?P<hours>[0-9]+(?:\.[0-9]+)?)H)?"
        r"(?:(?P<minutes>[0-9]+(?:\.[0-9]+)?)M)?"
        r"(?:(?P<seconds>[0-9]+(?:\.[0-9]+)?)S)?"
        r")?$"
    )
    match = pattern.match(value.strip())
    if not match:
        raise Phase6DMediaProfileError("unsupported ISO-8601 duration: {0}".format(value))
    days = float(match.group("days") or 0)
    hours = float(match.group("hours") or 0)
    minutes = float(match.group("minutes") or 0)
    seconds = float(match.group("seconds") or 0)
    return days * 86400 + hours * 3600 + minutes * 60 + seconds


def parse_segment_template(element: ET.Element) -> Dict[str, Any]:
    return {
        "timescale": int_value(element.attrib.get("timescale"), default=1),
        "duration": int_value(element.attrib.get("duration"), default=0),
        "start_number": int_value(element.attrib.get("startNumber"), default=1),
        "media": str(element.attrib.get("media", "")),
        "initialization": str(element.attrib.get("initialization", "")),
    }


def parse_representation(representation: ET.Element, adaptation_set: ET.Element) -> Dict[str, Any]:
    bandwidth = int_value(representation.attrib.get("bandwidth"), default=0)
    if bandwidth <= 0:
        raise Phase6DMediaProfileError("Representation bandwidth must be positive")
    rep_id = str(representation.attrib.get("id", "")).strip()
    if not rep_id:
        raise Phase6DMediaProfileError("Representation id is required")
    return {
        "representation_index": -1,
        "mpd_representation_id": rep_id,
        "bandwidth_bps": bandwidth,
        "bitrate_kbps": int(round(bandwidth / 1000.0)),
        "width": optional_int(representation.attrib.get("width") or adaptation_set.attrib.get("width")),
        "height": optional_int(representation.attrib.get("height") or adaptation_set.attrib.get("height")),
        "frame_rate": str(representation.attrib.get("frameRate") or adaptation_set.attrib.get("frameRate") or ""),
        "codecs": str(representation.attrib.get("codecs") or adaptation_set.attrib.get("codecs") or ""),
    }


def int_value(value: Optional[str], *, default: int) -> int:
    if value in (None, ""):
        return default
    return int(str(value))


def optional_int(value: Optional[str]) -> Optional[int]:
    if value in (None, ""):
        return None
    return int(str(value))


def compute_segment_count(duration_s: float, segment_duration_s: float) -> int:
    ratio = duration_s / segment_duration_s
    rounded = round(ratio)
    if abs(ratio - rounded) < 1e-9:
        return int(rounded)
    return int(math.ceil(ratio))


def build_segments(
    *,
    representations: Sequence[Mapping[str, Any]],
    templates: Mapping[str, Mapping[str, Any]],
    segment_count: int,
    segment_duration_s: float,
    mpd_duration_s: float,
    content_root: Optional[Path],
    base_url: Optional[str],
    size_policy: str,
) -> List[Dict[str, Any]]:
    segments: List[Dict[str, Any]] = []
    for segment_index in range(segment_count):
        remaining = max(mpd_duration_s - segment_index * segment_duration_s, 0.0)
        duration_s = min(segment_duration_s, remaining) if remaining else segment_duration_s
        segment: Dict[str, Any] = {
            "segment_index": segment_index,
            "segment_number": None,
            "duration_s": round_float(duration_s),
            "media_path_by_representation": {},
            "initialization_path_by_representation": {},
            "size_bytes_by_representation": {},
            "size_source_by_representation": {},
        }
        for representation in representations:
            rep_index = int(representation["representation_index"])
            rep_key = str(rep_index)
            template = templates[str(representation["mpd_representation_id"])]
            segment_number = int(template["start_number"]) + segment_index
            media_path = expand_segment_template(
                str(template["media"]),
                bandwidth_bps=int(representation["bandwidth_bps"]),
                number=segment_number,
            )
            init_path = expand_segment_template(
                str(template["initialization"]),
                bandwidth_bps=int(representation["bandwidth_bps"]),
                number=segment_number,
            )
            size_bytes, size_source = segment_size(
                relative_media_path=media_path,
                representation=representation,
                duration_s=duration_s,
                content_root=content_root,
                base_url=base_url,
                size_policy=size_policy,
            )
            segment["segment_number"] = segment_number
            segment["media_path_by_representation"][rep_key] = media_path
            segment["initialization_path_by_representation"][rep_key] = init_path
            segment["size_bytes_by_representation"][rep_key] = size_bytes
            segment["size_source_by_representation"][rep_key] = size_source
        segments.append(segment)
    return segments


def expand_segment_template(template: str, *, bandwidth_bps: int, number: int) -> str:
    expanded = template.replace("$Bandwidth$", str(bandwidth_bps))

    def replace_number(match: re.Match[str]) -> str:
        fmt = match.group("fmt")
        if not fmt:
            return str(number)
        width_match = re.search(r"%0?([0-9]+)d", fmt)
        if width_match:
            return str(number).zfill(int(width_match.group(1)))
        return str(number)

    return re.sub(r"\$Number(?P<fmt>%0?[0-9]+d)?\$", replace_number, expanded)


def segment_size(
    *,
    relative_media_path: str,
    representation: Mapping[str, Any],
    duration_s: float,
    content_root: Optional[Path],
    base_url: Optional[str],
    size_policy: str,
) -> Tuple[int, str]:
    estimate = bitrate_estimated_size(int(representation["bitrate_kbps"]), duration_s)
    if size_policy == "file_size":
        if content_root is not None:
            path = content_root / Path(relative_media_path.replace("/", "/"))
            if path.is_file():
                return path.stat().st_size, "file_size"
        return estimate, "missing_estimated"
    if size_policy == "http_head":
        if base_url:
            size = http_content_length(base_url, relative_media_path)
            if size is not None and size > 0:
                return size, "http_head"
        return estimate, "missing_estimated"
    return estimate, "bitrate_estimate"


def bitrate_estimated_size(bitrate_kbps: int, duration_s: float) -> int:
    return int(round((bitrate_kbps * 1000.0 / 8.0) * duration_s))


def http_content_length(base_url: str, relative_media_path: str) -> Optional[int]:
    url = urllib.parse.urljoin(ensure_trailing_slash(base_url), relative_media_path.replace("\\", "/"))
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            length = response.headers.get("content-length")
    except Exception:
        return None
    if not length:
        return None
    try:
        return int(length)
    except ValueError:
        return None


def ensure_trailing_slash(value: str) -> str:
    return value if value.endswith("/") else value + "/"


def count_size_sources(segments: Sequence[Mapping[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for segment in segments:
        sources = segment.get("size_source_by_representation", {})
        if isinstance(sources, Mapping):
            for source in sources.values():
                key = str(source)
                counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def sha256_json(data: Mapping[str, Any]) -> str:
    payload = json.dumps(data, indent=2, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def round_float(value: float) -> float:
    rounded = round(value, 6)
    if abs(rounded - round(rounded)) < 1e-9:
        return float(round(rounded))
    return rounded


if __name__ == "__main__":
    sys.exit(main())
