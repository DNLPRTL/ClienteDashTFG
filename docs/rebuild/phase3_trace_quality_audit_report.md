# Phase 3 Trace Quality Audit Report

Date: 2026-06-04

## Verdict

Quality audit status: PASS.

The original final manifest remains preserved. A curated manifest was generated to remove traces that do not provide useful temporal signal for training/evaluation. No raw data or normalized CSV was deleted.

Use this curated manifest for future training/evaluation preparation:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
```

The full quality audit is:

```text
C:\Users\danie\Documents\TFG\auditorias_trazas\phase3\final\phase3_trace_quality_audit.json
```

## Quality Policy

Excluded only if at least one of these applies:

```text
row_count < 30
duration_s < 30
throughput is all zero
```

Kept with flags, not excluded:

```text
mostly_zero_intermitent_or_severe_network
low_bandwidth_trace
extreme_throughput_value
```

This preserves bad or intermittent network traces when they contain enough temporal signal and at least some positive throughput.

## Results

Input final traces:

```text
5957
```

Curated traces:

```text
5744
```

Excluded as not useful:

```text
213
```

Curated split counts:

```text
train=4005
test=866
eval=873
```

Curated semantics counts:

```text
active_fixed_broadband_download_test=4174
active_mobile_speedtest=438
available_bandwidth=917
observed_application_traffic=122
real_streaming_delivery_rate=93
```

Quality exclusions:

```text
row_count_lt_30=211
duration_s_lt_30=106
all_zero_throughput=4
```

These counts overlap because a trace can be both short and all-zero.

Kept difficult traces:

```text
severe_or_intermittent_network=40
low_bandwidth_network=169
high_or_extreme_throughput_network=107
```

## Examples

Excluded all-zero FCC trace:

```text
trace_id=trace_fcc_measuring_broadband_america_unit_24767549_curr_httpgetmt_csv_103d70b99f6d
row_count=1
duration_s=0.001
throughput_mean_kbps=0
throughput_max_kbps=0
zero_fraction=1.0
```

Excluded short Roma trace:

```text
trace_id=trace_roma_4g_nbiot_5g_nsa_speedtest_campaign_21_op2_ow_segment_0199_throughput_tests_d0bc72a75716
row_count=5
duration_s=5.433
throughput_mean_kbps=0
throughput_max_kbps=0
zero_fraction=1.0
```

Kept severe/intermittent network traces are marked with:

```text
network_condition=severe_or_intermittent_network
quality_flags=["mostly_zero_intermitent_or_severe_network"]
```

## Commands

```powershell
python scripts\audit_phase3_trace_quality.py
python scripts\validate_phase3_trace_manifest.py --manifest "C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json"
```

Validation result:

```text
status=PASS
ready_for_benchmark=false
benchmark_authorized=false
```

## Guardrails

The curated manifest is still not a benchmark result and does not authorize training, ranking or QoE claims by itself. It is the recommended trace input for the next training/evaluation preparation step.
