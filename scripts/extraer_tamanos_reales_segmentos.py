#!/usr/bin/env python3
"""Extrae el peso REAL (VBR) de cada segmento DASH desde el servidor de contenidos.

Motivacion
----------
El entrenamiento y el planner Neural-MPC asumian CBR (tamano = bitrate * duracion).
El cliente real reproduce MPDs VBR: el segmento N pesa distinto cada vez. Este
script construye la tabla fiel `segmento N -> bytes` por representacion, leyendo el
`Content-Length` real de cada `.m4s` del servidor. Esa tabla alimentara despues
(1) el simulador/dataset de entrenamiento y (2) el modelo de descarga del planner.

Solo lee por HTTP (HEAD; GET de respaldo si falta Content-Length). No descarga el
contenido completo salvo que un servidor no exponga el tamano por HEAD.

Salida
------
Un JSON por perfil de medio en `media_profiles/segment_sizes/<media_profile_id>.json`
con metadatos del MPD + tamanos reales por segmento + evidencia VBR (CV y real/CBR).

Se ejecuta en la VM cliente Ubuntu (es la que alcanza el servidor 192.168.1.132).
Imprime al final una linea compacta para pegar.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

SCHEMA_ID = "media_profile_segment_sizes_v1"

# Perfiles de medio canonicos del TFG: SOLO versiones de 4 s (las de 2 s se obvian).
DEFAULT_MPD_PATHS = (
    "Blender_Sunflower_10min_30fps/4sec/Blender_Sunflower_10min_30fps_simple_4s.mpd",
    "Blender_Sunflower_10min_60fps/4sec/Blender_Sunflower_10min_60fps_simple_4s.mpd",
    "Blender_Sunflower_1min_30fps/4sec/Blender_Sunflower_1min_30fps_simple_4s.mpd",
    "Blender_Sunflower_1min_60fps/4sec/Blender_Sunflower_1min_60fps_simple_4s.mpd",
    "Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd",
    "Paseo_Almunecar_10min_60fps/4sec/Paseo_Almunecar_10min_60fps_simple_4s.mpd",
    "Paseo_Almunecar_1min_30fps/4sec/Paseo_Almunecar_1min_30fps_simple_4s.mpd",
    "Paseo_Almunecar_1min_60fps/4sec/Paseo_Almunecar_1min_60fps_simple_4s.mpd",
)

DEFAULT_BASE_URL = "http://192.168.1.132/dash"


class ExtractionError(RuntimeError):
    pass


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def _find_first(root: ET.Element, name: str) -> ET.Element | None:
    for el in root.iter():
        if _local(el.tag) == name:
            return el
    return None


def _find_all(root: ET.Element, name: str) -> list[ET.Element]:
    return [el for el in root.iter() if _local(el.tag) == name]


def parse_iso8601_duration_s(text: str) -> float:
    if not text:
        raise ExtractionError("duracion ISO8601 vacia")
    m = re.fullmatch(
        r"P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:([\d.]+)S)?)?",
        text.strip(),
    )
    if not m:
        raise ExtractionError("duracion ISO8601 no parseable: {0}".format(text))
    years, months, days, hours, minutes, seconds = m.groups()
    total = 0.0
    total += float(days or 0) * 86400.0
    total += float(hours or 0) * 3600.0
    total += float(minutes or 0) * 60.0
    total += float(seconds or 0)
    # years/months no aplican a duracion de presentacion de estos MPD
    return total


def parse_frame_rate(text: str | None) -> tuple[str, float | None]:
    if not text:
        return "", None
    text = text.strip()
    if "/" in text:
        num, den = text.split("/", 1)
        try:
            return text, float(num) / float(den)
        except (ValueError, ZeroDivisionError):
            return text, None
    try:
        return text, float(text)
    except ValueError:
        return text, None


def _http_size(url: str, timeout: float, retries: int = 2) -> int | None:
    """Devuelve bytes del recurso. None si 404. Lanza si error persistente != 404."""
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                length = resp.headers.get("Content-Length")
                if length is not None:
                    return int(length)
                # HEAD sin Content-Length: respaldo GET (lee y descarta)
            req_get = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req_get, timeout=timeout) as resp:
                data = resp.read()
                return len(data)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            last_err = err
        except Exception as err:  # noqa: BLE001 - red puede fallar de varias formas
            last_err = err
        time.sleep(0.4 * (attempt + 1))
    raise ExtractionError("fallo HTTP persistente en {0}: {1}".format(url, last_err))


def _stats(values: list[int]) -> dict[str, float]:
    if not values:
        return {"mean": 0.0, "min": 0.0, "max": 0.0, "std": 0.0, "cv": 0.0}
    n = len(values)
    mean = sum(values) / n
    var = sum((v - mean) ** 2 for v in values) / n
    std = math.sqrt(var)
    return {
        "mean": mean,
        "min": float(min(values)),
        "max": float(max(values)),
        "std": std,
        "cv": (std / mean) if mean > 0 else 0.0,
    }


def media_profile_id_from_mpd_path(mpd_path: str) -> str:
    # ej: Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd
    base = os.path.basename(mpd_path)
    name = base[:-4] if base.lower().endswith(".mpd") else base
    name = name.replace("_simple", "").lower()
    return name


def extract_profile(mpd_url: str, *, timeout: float, segment_cap_margin: int) -> dict:
    with urllib.request.urlopen(mpd_url, timeout=timeout) as resp:
        xml_bytes = resp.read()
    root = ET.fromstring(xml_bytes)

    mpd_dir = mpd_url.rsplit("/", 1)[0] + "/"

    pres_attr = root.get("mediaPresentationDuration")
    presentation_duration_s = parse_iso8601_duration_s(pres_attr) if pres_attr else 0.0

    template = _find_first(root, "SegmentTemplate")
    if template is None:
        raise ExtractionError("MPD sin SegmentTemplate: {0}".format(mpd_url))
    media_tmpl = template.get("media")
    init_tmpl = template.get("initialization")
    timescale = float(template.get("timescale") or "1")
    seg_duration_units = float(template.get("duration") or "0")
    start_number = int(template.get("startNumber") or "1")
    if seg_duration_units <= 0 or timescale <= 0:
        raise ExtractionError("SegmentTemplate sin duration/timescale validos")
    segment_duration_s = seg_duration_units / timescale

    expected_count = (
        int(math.ceil(presentation_duration_s / segment_duration_s))
        if presentation_duration_s > 0
        else 0
    )
    hard_cap = (expected_count + segment_cap_margin) if expected_count else 100000

    # Recoger representations y AdaptationSet (resolucion puede estar en cualquiera).
    adaptation = _find_first(root, "AdaptationSet")
    reps_raw = _find_all(root, "Representation")
    if not reps_raw:
        raise ExtractionError("MPD sin Representations: {0}".format(mpd_url))

    parsed_reps = []
    for rep in reps_raw:
        bandwidth = int(rep.get("bandwidth"))
        width = rep.get("width") or (adaptation.get("width") if adaptation is not None else None)
        height = rep.get("height") or (adaptation.get("height") if adaptation is not None else None)
        fr_raw = rep.get("frameRate") or (adaptation.get("frameRate") if adaptation is not None else None)
        fr_text, fr_num = parse_frame_rate(fr_raw)
        parsed_reps.append(
            {
                "bandwidth_bps": bandwidth,
                "width": int(width) if width else None,
                "height": int(height) if height else None,
                "frame_rate": fr_text,
                "frame_rate_num": fr_num,
                "codecs": rep.get("codecs") or "",
            }
        )

    # Orden ascendente por bitrate -> representation_index 0 = mas bajo (accion 0).
    parsed_reps.sort(key=lambda r: r["bandwidth_bps"])

    representations = []
    total_segments_probed = 0
    for index, rep in enumerate(parsed_reps):
        bandwidth = rep["bandwidth_bps"]
        init_url = mpd_dir + init_tmpl.replace("$Bandwidth$", str(bandwidth))
        init_bytes = _http_size(init_url, timeout)

        segment_bytes: list[int] = []
        number = start_number
        while number < start_number + hard_cap:
            seg_url = mpd_dir + media_tmpl.replace("$Bandwidth$", str(bandwidth)).replace(
                "$Number$", str(number)
            )
            size = _http_size(seg_url, timeout)
            if size is None:
                break  # 404 -> fin de la serie
            segment_bytes.append(size)
            number += 1
            total_segments_probed += 1

        stats = _stats(segment_bytes)
        cbr_nominal_bytes = bandwidth * segment_duration_s / 8.0
        real_vs_cbr = (stats["mean"] / cbr_nominal_bytes) if cbr_nominal_bytes > 0 else 0.0
        representations.append(
            {
                "representation_index": index,
                "bandwidth_bps": bandwidth,
                "width": rep["width"],
                "height": rep["height"],
                "frame_rate": rep["frame_rate"],
                "frame_rate_num": rep["frame_rate_num"],
                "codecs": rep["codecs"],
                "init_bytes": init_bytes,
                "segment_count": len(segment_bytes),
                "segment_bytes": segment_bytes,
                "segment_bytes_mean": stats["mean"],
                "segment_bytes_min": stats["min"],
                "segment_bytes_max": stats["max"],
                "segment_bytes_cv": stats["cv"],
                "cbr_nominal_bytes": cbr_nominal_bytes,
                "real_mean_vs_cbr_ratio": real_vs_cbr,
            }
        )

    seg_counts = {r["segment_count"] for r in representations}
    segment_count = max((r["segment_count"] for r in representations), default=0)
    vbr_cv_max = max((r["segment_bytes_cv"] for r in representations), default=0.0)

    return {
        "schema_id": SCHEMA_ID,
        "media_profile_id": media_profile_id_from_mpd_path(mpd_url),
        "mpd_url": mpd_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "media_presentation_duration_s": presentation_duration_s,
        "segment_duration_s": segment_duration_s,
        "start_number": start_number,
        "expected_segment_count": expected_count,
        "segment_count": segment_count,
        "representation_count": len(representations),
        "vbr_cv_max": vbr_cv_max,
        "representations": representations,
        "_total_segments_probed": total_segments_probed,
        "_segment_count_consistent": len(seg_counts) == 1,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extrae tamanos reales VBR de segmentos DASH.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Base del servidor DASH.")
    parser.add_argument("--mpd-url", action="append", default=None, help="URL completa de un MPD (repetible).")
    parser.add_argument("--all", action="store_true", help="Usar los 8 perfiles 4s por defecto.")
    parser.add_argument("--out-dir", default=None, help="Directorio de salida (por defecto media_profiles/segment_sizes).")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--segment-cap-margin", type=int, default=8)
    args = parser.parse_args(argv)

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = args.out_dir or os.path.join(repo_root, "media_profiles", "segment_sizes")
    os.makedirs(out_dir, exist_ok=True)

    if args.mpd_url:
        mpd_urls = list(args.mpd_url)
    else:  # por defecto (incluido --all), el set completo de 8 perfiles 4s
        base = args.base_url.rstrip("/")
        mpd_urls = ["{0}/{1}".format(base, path) for path in DEFAULT_MPD_PATHS]

    ok = 0
    failed = 0
    total_probed = 0
    for mpd_url in mpd_urls:
        try:
            profile = extract_profile(
                mpd_url, timeout=args.timeout, segment_cap_margin=args.segment_cap_margin
            )
        except Exception as err:  # noqa: BLE001
            failed += 1
            print("media_profile_FAIL mpd={0} error={1}".format(mpd_url, err), flush=True)
            continue
        out_path = os.path.join(out_dir, profile["media_profile_id"] + ".json")
        with open(out_path, "w", encoding="utf-8") as handle:
            json.dump(profile, handle, ensure_ascii=False, indent=2)
        ok += 1
        total_probed += profile["_total_segments_probed"]
        top = profile["representations"][-1]
        print(
            "media_profile={mp} reps={r} segs={s} segdur={d:.3f} "
            "vbr_cv_max={cv:.3f} real_vs_cbr_top={rc:.3f} consistent={c} OK".format(
                mp=profile["media_profile_id"],
                r=profile["representation_count"],
                s=profile["segment_count"],
                d=profile["segment_duration_s"],
                cv=profile["vbr_cv_max"],
                rc=top["real_mean_vs_cbr_ratio"],
                c=profile["_segment_count_consistent"],
            ),
            flush=True,
        )

    status = "OK" if failed == 0 and ok > 0 else "REVIEW"
    print(
        "SEGMENT_SIZE_EXTRACTION status={st} profiles_ok={ok} profiles_failed={fail} "
        "segments_probed={sp} out_dir={od}".format(
            st=status, ok=ok, fail=failed, sp=total_probed,
            od=os.path.relpath(out_dir, repo_root),
        ),
        flush=True,
    )
    return 0 if status == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
