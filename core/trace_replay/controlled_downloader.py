from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Optional

from core.trace_replay.loader import LoadedTrace, TraceLoadError, TraceSample, load_normalized_trace_csv, load_normalized_trace_rows
from core.trace_replay.network_model import END_POLICY_FAIL, TraceDrivenNetworkModel


perf_now = time.perf_counter


class TraceControlledDownloader:
    """Downloader wrapper that delays segment delivery with a normalized trace.

    The wrapped downloader still fetches bytes from the configured DASH server.
    Only the timing exposed to the player is controlled by the trace model.
    """

    def __init__(
        self,
        base_downloader,
        trace_csv_path: str | Path,
        *,
        window_start_s: float = 0.0,
        window_duration_s: Optional[float] = None,
        end_policy: str = END_POLICY_FAIL,
        max_loops: int = 0,
        sleep: bool = True,
    ) -> None:
        if not trace_csv_path:
            raise TraceLoadError("trace_csv_path is required for TraceControlledDownloader")
        self.base_downloader = base_downloader
        self.trace_csv_path = str(trace_csv_path)
        self.window_start_s = float(window_start_s or 0.0)
        self.window_duration_s = None if window_duration_s is None else float(window_duration_s)
        self.sleep = bool(sleep)
        self.on_event = None

        if hasattr(self.base_downloader, "on_event"):
            self.base_downloader.on_event = None

        loaded = load_normalized_trace_csv(self.trace_csv_path)
        self.loaded_trace = clip_loaded_trace_window(
            loaded,
            window_start_s=self.window_start_s,
            window_duration_s=self.window_duration_s,
        )
        self.network_model = TraceDrivenNetworkModel(
            self.loaded_trace,
            end_policy=end_policy,
            max_loops=int(max_loops),
        )
        self._replay_wall_start_s = perf_now()

    def download(self, url, byte_range=None, timeout=10, callback=None, save_path=None, **kwargs):
        request_wall_start_s = perf_now()
        replay_start_s = max(0.0, request_wall_start_s - self._replay_wall_start_s)
        data, raw_info = self.base_downloader.download(
            url,
            byte_range=byte_range,
            timeout=timeout,
            callback=None,
            save_path=save_path,
            **kwargs,
        )
        raw_info = dict(raw_info or {})
        actual_elapsed_s = max(0.0, perf_now() - request_wall_start_s)
        if not data:
            error_info = dict(raw_info)
            error_info.update(
                {
                    "trace_replay_enabled": True,
                    "trace_replay_window_start_s": self.window_start_s,
                    "trace_replay_window_duration_s": self.window_duration_s,
                }
            )
            self._emit("error", error_info)
            if callback:
                _safe_callback(callback, data, error_info)
            return data, error_info

        result = self.network_model.download(len(data), start_time_s=replay_start_s)
        remaining_sleep_s = result.duration_s - actual_elapsed_s
        if self.sleep and remaining_sleep_s > 0:
            time.sleep(remaining_sleep_s)

        info = dict(raw_info)
        info.update(
            {
                "elapsed_total": float(result.duration_s),
                "elapsed_payload": float(result.duration_s),
                "size": int(len(data)),
                "bytes_downloaded": int(len(data)),
                "trace_replay_enabled": True,
                "trace_replay_window_start_s": self.window_start_s,
                "trace_replay_window_duration_s": self.window_duration_s,
                "trace_replay_start_time_s": float(result.start_time_s),
                "trace_replay_end_time_s": float(result.end_time_s),
                "trace_replay_trace_time_start_s": float(result.trace_time_start_s),
                "trace_replay_trace_time_end_s": float(result.trace_time_end_s),
                "trace_replay_measured_throughput_kbps": float(result.measured_throughput_kbps),
                "trace_replay_samples_touched": int(result.samples_touched),
                "trace_replay_end_policy": str(result.end_policy),
            }
        )
        if callback:
            _safe_callback(callback, data, info)
        self._emit("complete", info)
        return data, info

    def download_async(self, url, byte_range=None, timeout=10, callback=None, save_path=None, **kwargs):
        import threading

        thread = threading.Thread(
            target=self.download,
            args=(url, byte_range, timeout, callback, save_path),
            kwargs=kwargs,
            daemon=True,
        )
        thread.start()
        return thread

    def download_multiple(self, urls, max_workers=4, **kwargs):
        from concurrent.futures import ThreadPoolExecutor

        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self.download, url, **kwargs) for url in urls]
            for future in futures:
                results.append(future.result())
        return results

    def get_file_size(self, url, timeout=10):
        return self.base_downloader.get_file_size(url, timeout=timeout)

    def _emit(self, event: str, info: dict[str, Any]) -> None:
        try:
            if callable(self.on_event):
                self.on_event(event, info)
        except Exception:
            pass


def clip_loaded_trace_window(
    loaded_trace: LoadedTrace,
    *,
    window_start_s: float = 0.0,
    window_duration_s: Optional[float] = None,
) -> LoadedTrace:
    start_s = float(window_start_s or 0.0)
    if start_s < 0:
        raise TraceLoadError("window_start_s must be >= 0")
    if window_duration_s is not None and float(window_duration_s) <= 0:
        raise TraceLoadError("window_duration_s must be > 0")
    end_s = None if window_duration_s is None else start_s + float(window_duration_s)

    rows = []
    for sample in loaded_trace.samples:
        clipped = _clip_sample(sample, start_s=start_s, end_s=end_s)
        if clipped is None:
            continue
        rows.append(
            {
                "timestamp_s": clipped.timestamp_s,
                "duration_s": clipped.duration_s,
                "throughput_kbps": clipped.throughput_kbps,
            }
        )
    if not rows:
        raise TraceLoadError("trace window has no samples")
    suffix = "window_{0:g}".format(start_s)
    if window_duration_s is not None:
        suffix += "_{0:g}s".format(float(window_duration_s))
    return load_normalized_trace_rows(rows, trace_id="{0}:{1}".format(loaded_trace.trace_id, suffix))


def _clip_sample(sample: TraceSample, *, start_s: float, end_s: Optional[float]) -> Optional[TraceSample]:
    sample_start_s = float(sample.timestamp_s)
    sample_end_s = sample_start_s + float(sample.duration_s)
    overlap_start_s = max(sample_start_s, start_s)
    overlap_end_s = sample_end_s if end_s is None else min(sample_end_s, end_s)
    if overlap_end_s <= overlap_start_s:
        return None
    return TraceSample(
        timestamp_s=overlap_start_s - start_s,
        duration_s=overlap_end_s - overlap_start_s,
        throughput_kbps=float(sample.throughput_kbps),
    )


def _safe_callback(callback, data, info) -> None:
    try:
        callback(data, info)
    except Exception:
        pass
