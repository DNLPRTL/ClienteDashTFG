from __future__ import annotations

import argparse
import fnmatch
import html.parser
import shutil
import sys
import urllib.parse
import urllib.request
from http.cookiejar import CookieJar
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        md5_file,
        selected_sources,
        sha256_file,
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
        md5_file,
        selected_sources,
        sha256_file,
        utc_now,
        write_json,
        write_markdown_report,
    )


RECEIPT_SCHEMA_VERSION = "phase6c_download_receipts_v1"
USER_AGENT = "DashClientModular4-Phase6C/1.0"


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Download public Phase 6C trace sources into an external root.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--sources", default="all")
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--require-lumos", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        report = download_phase6_sources(
            external_root=args.external_root,
            sources=args.sources,
            registry_path=args.source_registry,
            require_lumos=args.require_lumos,
            offline=args.offline,
            strict=args.strict,
            allow_repo_output=args.allow_repo_output,
        )
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6c_download: {0}".format("PASS" if report["valid"] else "WARN_OR_FAIL"))
    print("receipts: {0}".format(report["receipts_path"]))
    return 0 if report["valid"] else 2


def download_phase6_sources(
    *,
    external_root: Path,
    sources: str = "all",
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    require_lumos: bool = False,
    offline: bool = False,
    strict: bool = False,
    allow_repo_output: bool = False,
) -> Dict[str, Any]:
    paths = create_external_layout(external_root, allow_repo_output=allow_repo_output)
    registry = load_source_registry(registry_path)
    selected = selected_sources(registry, sources)

    receipts: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []

    for source in selected:
        source_id = source["source_id"]
        try:
            if source_id == "hsdpa_norway":
                source_receipts = download_hsdpa_source(source, paths["archives"], offline=offline)
            else:
                source_receipts = [download_single_source(source, paths["archives"], offline=offline)]
        except Exception as exc:
            source_receipts = [
                base_receipt(source, "failed", error="{0}: {1}".format(exc.__class__.__name__, exc))
            ]
        receipts.extend(source_receipts)

    for receipt in receipts:
        source_id = receipt["source_id"]
        status = receipt["status"]
        if status in ("downloaded", "copied_from_local_file", "already_present"):
            continue
        message = "{0}: {1}".format(source_id, status)
        if receipt.get("error"):
            message = "{0} ({1})".format(message, receipt["error"])
        if should_fail_download_status(source_id, status, strict=strict, require_lumos=require_lumos, sources=sources):
            errors.append(message)
        else:
            warnings.append(message)

    receipt_doc = {
        "schema_version": RECEIPT_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "external_root": str(paths["root"]),
        "registry": str(registry_path),
        "offline": offline,
        "strict": strict,
        "require_lumos": require_lumos,
        "receipts": receipts,
        "errors": errors,
        "warnings": warnings,
    }
    receipts_path = paths["receipts"] / "phase6c_download_receipts.json"
    report_path = paths["reports"] / "phase6c_download_report.md"
    write_json(receipts_path, receipt_doc)
    write_download_report(report_path, receipts, errors, warnings)

    return {
        "valid": not errors,
        "receipts": receipts,
        "errors": errors,
        "warnings": warnings,
        "receipts_path": str(receipts_path),
        "report_path": str(report_path),
    }


def download_single_source(source: Mapping[str, Any], archive_root: Path, *, offline: bool) -> Dict[str, Any]:
    if offline:
        return base_receipt(source, "offline_skipped", error="offline mode enabled")

    source_id = str(source["source_id"])
    target_dir = archive_root / source_id
    target_dir.mkdir(parents=True, exist_ok=True)
    target_name = str(source.get("canonical_file") or "{0}.download".format(source_id))
    target = target_dir / target_name
    urls = [str(url) for url in source.get("urls", [])]
    if not urls:
        return base_receipt(source, "failed", error="no URL configured")

    if source.get("google_drive_file_id") and not is_local_url(urls[0]):
        receipt = download_google_drive(source, target)
    else:
        receipt = download_file_from_urls(source, urls, target)

    if receipt["status"] in ("downloaded", "copied_from_local_file", "already_present"):
        add_hashes_and_verify(source, target, receipt)
    return receipt


def download_file_from_urls(source: Mapping[str, Any], urls: Sequence[str], target: Path) -> Dict[str, Any]:
    errors = []
    for url in urls:
        try:
            if is_local_url(url):
                copy_local_url(url, target)
                return base_receipt(source, "copied_from_local_file", url=url, path=target)
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=60) as response:
                content_type = response.headers.get("Content-Type", "")
                payload = response.read()
            if looks_like_blocked_html(payload, content_type):
                return base_receipt(
                    source,
                    "blocked_by_provider_or_manual_confirmation_required",
                    url=url,
                    error="provider returned HTML login/captcha/confirmation page",
                )
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            return base_receipt(source, "downloaded", url=url, path=target)
        except Exception as exc:
            errors.append("{0}: {1}".format(url, exc))
    return base_receipt(source, "failed", error="; ".join(errors))


def download_google_drive(source: Mapping[str, Any], target: Path) -> Dict[str, Any]:
    file_id = str(source.get("google_drive_file_id", "")).strip()
    if not file_id:
        return base_receipt(source, "failed", error="missing google_drive_file_id")
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(CookieJar()))
    url = "https://drive.google.com/uc?export=download&id={0}".format(urllib.parse.quote(file_id))
    try:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        first = opener.open(request, timeout=60)
        payload = first.read()
        content_type = first.headers.get("Content-Type", "")
        token = google_drive_confirmation_token(payload.decode("utf-8", errors="ignore"), first.headers)
        if token:
            confirm_url = url + "&confirm=" + urllib.parse.quote(token)
            request = urllib.request.Request(confirm_url, headers={"User-Agent": USER_AGENT})
            second = opener.open(request, timeout=60)
            payload = second.read()
            content_type = second.headers.get("Content-Type", "")
        if looks_like_blocked_html(payload, content_type):
            return base_receipt(
                source,
                "blocked_by_provider_or_manual_confirmation_required",
                url=url,
                error="Google Drive returned HTML confirmation/login/captcha page",
            )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        return base_receipt(source, "downloaded", url=url, path=target)
    except Exception as exc:
        return base_receipt(
            source,
            "blocked_by_provider_or_manual_confirmation_required",
            url=url,
            error="{0}: {1}".format(exc.__class__.__name__, exc),
        )


def google_drive_confirmation_token(html: str, headers: Mapping[str, str]) -> str:
    for cookie in headers.get_all("Set-Cookie", []) if hasattr(headers, "get_all") else []:
        if "download_warning" in cookie:
            for part in cookie.split(";"):
                if "download_warning" in part and "=" in part:
                    return part.split("=", 1)[1].strip()
    marker = "confirm="
    if marker in html:
        token = html.split(marker, 1)[1].split("&", 1)[0].split('"', 1)[0]
        return urllib.parse.unquote(token)
    return ""


def download_hsdpa_source(source: Mapping[str, Any], archive_root: Path, *, offline: bool) -> List[Dict[str, Any]]:
    if offline:
        return [base_receipt(source, "offline_skipped", error="offline mode enabled")]
    base_url = str(source.get("source_base_url", "")).strip()
    if not base_url:
        return [base_receipt(source, "failed", error="missing source_base_url")]
    source_id = str(source["source_id"])
    target_root = archive_root / source_id
    target_root.mkdir(parents=True, exist_ok=True)
    pattern = str(source.get("file_pattern", "report.*"))
    urls = discover_hsdpa_report_urls(base_url, pattern)
    if not urls:
        return [base_receipt(source, "failed", error="no report.* files discovered")]

    receipts = []
    for url in urls:
        relative = hsdpa_relative_path(base_url, url)
        target = target_root / relative
        receipt = download_file_from_urls(source, [url], target)
        if receipt["status"] in ("downloaded", "copied_from_local_file", "already_present"):
            add_hashes_and_verify(source, target, receipt)
        receipt["relative_path"] = str(relative).replace("\\", "/")
        receipts.append(receipt)
    return receipts


def discover_hsdpa_report_urls(base_url: str, pattern: str) -> List[str]:
    if is_local_url(base_url):
        local_path = local_path_from_url(base_url)
        if local_path.is_file() and fnmatch.fnmatch(local_path.name, pattern):
            return [local_path.as_uri()]
        urls = []
        for path in sorted(local_path.rglob("*")):
            if path.is_file() and fnmatch.fnmatch(path.name, pattern):
                urls.append(path.as_uri())
        return urls
    return discover_http_listing(base_url, pattern, seen=set())


def discover_http_listing(url: str, pattern: str, *, seen: set[str]) -> List[str]:
    if url in seen:
        return []
    seen.add(url)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        html = response.read().decode("utf-8", errors="ignore")
    parser = LinkParser()
    parser.feed(html)
    found: List[str] = []
    for href in parser.links:
        if href.startswith("?") or href in ("../", "./"):
            continue
        joined = urllib.parse.urljoin(url, href)
        name = Path(urllib.parse.urlparse(joined).path).name
        if href.endswith("/"):
            found.extend(discover_http_listing(joined, pattern, seen=seen))
        elif fnmatch.fnmatch(name, pattern):
            found.append(joined)
    return sorted(set(found))


def hsdpa_relative_path(base_url: str, url: str) -> Path:
    if is_local_url(base_url) and is_local_url(url):
        try:
            return local_path_from_url(url).relative_to(local_path_from_url(base_url))
        except ValueError:
            return Path(local_path_from_url(url).name)
    base_path = urllib.parse.urlparse(base_url).path
    url_path = urllib.parse.urlparse(url).path
    relative = url_path[len(base_path):].lstrip("/") if url_path.startswith(base_path) else Path(url_path).name
    return Path(relative)


def add_hashes_and_verify(source: Mapping[str, Any], target: Path, receipt: Dict[str, Any]) -> None:
    receipt["path"] = str(target)
    receipt["size_bytes"] = target.stat().st_size
    receipt["sha256"] = sha256_file(target)
    md5 = md5_file(target)
    receipt["md5"] = md5
    expected_md5 = str(source.get("expected_hashes", {}).get("md5", "")).lower()
    if expected_md5:
        receipt["expected_md5"] = expected_md5
        if md5.lower() != expected_md5:
            receipt["status"] = "checksum_mismatch"
            receipt["error"] = "md5 mismatch: expected {0}, got {1}".format(expected_md5, md5)


def base_receipt(
    source: Mapping[str, Any],
    status: str,
    *,
    url: str = "",
    path: Optional[Path] = None,
    error: str = "",
) -> Dict[str, Any]:
    receipt = {
        "source_id": source.get("source_id", ""),
        "dataset_family": source.get("dataset_family", ""),
        "role": source.get("role", ""),
        "status": status,
        "acquisition_status": status,
        "url": url,
        "path": str(path) if path else "",
        "generated_at": utc_now(),
    }
    if error:
        receipt["error"] = error
    return receipt


def should_fail_download_status(
    source_id: str,
    status: str,
    *,
    strict: bool,
    require_lumos: bool,
    sources: str,
) -> bool:
    if status in ("downloaded", "copied_from_local_file", "already_present"):
        return False
    if source_id == "lumos5g":
        return require_lumos
    if source_id in ("raca_4g_lte", "raca_5g"):
        return strict
    explicitly_selected = sources != "all" and source_id in {item.strip() for item in sources.split(",")}
    return strict and explicitly_selected


def copy_local_url(url: str, target: Path) -> None:
    local_path = local_path_from_url(url)
    if local_path.is_dir():
        raise Phase6CError("local URL points to a directory, expected file: {0}".format(url))
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(local_path, target)


def local_path_from_url(url: str) -> Path:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme == "file":
        return Path(urllib.request.url2pathname(parsed.path)).resolve()
    return Path(url).resolve()


def is_local_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return parsed.scheme == "file" or (not parsed.scheme and Path(url).exists())


def looks_like_blocked_html(payload: bytes, content_type: str = "") -> bool:
    prefix = payload[:4096].decode("utf-8", errors="ignore").lower()
    if "text/html" in content_type.lower() and (
        "captcha" in prefix or "login" in prefix or "confirm" in prefix or "<html" in prefix
    ):
        return True
    return prefix.lstrip().startswith("<!doctype html") or prefix.lstrip().startswith("<html")


def write_download_report(path: Path, receipts: Sequence[Mapping[str, Any]], errors: Sequence[str], warnings: Sequence[str]) -> None:
    lines = [
        "Phase 6C download report. This is acquisition metadata only, not benchmark evidence.",
        "",
        "- errors: {0}".format(len(errors)),
        "- warnings: {0}".format(len(warnings)),
        "- downloaded_or_copied: {0}".format(
            sum(1 for receipt in receipts if receipt.get("status") in ("downloaded", "copied_from_local_file", "already_present"))
        ),
        "",
        "## Sources",
        "",
    ]
    for receipt in receipts:
        lines.append("- `{0}`: `{1}`".format(receipt.get("source_id", ""), receipt.get("status", "")))
    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend("- {0}".format(error) for error in errors)
    if warnings:
        lines.extend(["", "## Warnings", ""])
        lines.extend("- {0}".format(warning) for warning in warnings)
    write_markdown_report(path, "Phase 6C Download Report", lines)


if __name__ == "__main__":
    sys.exit(main())
