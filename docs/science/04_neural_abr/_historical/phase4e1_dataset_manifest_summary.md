# Phase 4E.1 dataset manifest summary

## Dataset

Path:

```text
C:\Users\danie\Documents\TFG\_datasets\phase4_AI\neural_abr_lite\phase4E1_external_trace_smoke_TEST
```

Manifest:

```text
dataset_manifest.json
```

Schema:

```text
neural_abr_lite_dataset_v1
```

## Split policy

Policy:

```text
phase4e1_trace_level_regime_v1
```

Seed:

```text
123
```

The split unit is `leakage_group` when present, otherwise `trace_id`. No rows from the same trace or leakage group are split across train, validation and OOD diagnostic.

## Split summary

| split | traces | samples | source datasets |
|---|---:|---:|---|
| train | 9 | 1367 | ghent, hsdpa, lancaster |
| validation | 3 | 407 | ghent, hsdpa, lancaster |
| ood_diagnostic | 3 | 427 | ghent, hsdpa, lancaster |

OOD diagnostic is explicitly marked as not for tuning.

## Trace IDs

Train:

```text
ghent_4g_lte_bandwidth_logs_logs_all_report_bicycle_0001_log_e58bb097
ghent_4g_lte_bandwidth_logs_logs_all_report_bicycle_0002_log_0fc8f080
ghent_4g_lte_bandwidth_logs_logs_all_report_bus_0002_log_a9235bda
hsdpa_norway_mmsys2013_routes_bus_ljansbakken_oslo_report_2010_09_28_1407cest_17362475
hsdpa_norway_mmsys2013_routes_bus_ljansbakken_oslo_report_2010_09_29_0852cest_d6bd999a
hsdpa_norway_mmsys2013_routes_bus_ljansbakken_oslo_report_2010_09_29_1622cest_26dfcdd4
lancaster_abr_throughput_traces_abr_throughput_traces_0_txt_f420c487
lancaster_abr_throughput_traces_abr_throughput_traces_1000_txt_c79138cf
lancaster_abr_throughput_traces_abr_throughput_traces_10_txt_74ab52b4
```

Validation:

```text
ghent_4g_lte_bandwidth_logs_logs_all_report_bus_0001_log_792e4965
hsdpa_norway_mmsys2013_routes_bus_ljansbakken_oslo_report_2010_09_29_1823cest_e2cd8771
lancaster_abr_throughput_traces_abr_throughput_traces_100_txt_ed10edb6
```

OOD diagnostic:

```text
ghent_4g_lte_bandwidth_logs_logs_all_report_bus_0003_log_5908b5e1
hsdpa_norway_mmsys2013_routes_bus_ljansbakken_oslo_report_2010_09_29_1628cest_3cc528db
lancaster_abr_throughput_traces_abr_throughput_traces_1_txt_bcafb8a5
```

## Ladder and teacher

- Representation ladder: 300, 750, 1200, 1850, 2850 kbps.
- Segment duration: 4.0 seconds.
- Segment count: per trace, based on trace duration.
- Teacher: `robust_mpc`.
- Reward context: `qoe_linear_v1 / reward_n`.

## Label distribution

| split | label distribution |
|---|---|
| train | `{"0": 38, "1": 36, "2": 95, "3": 163, "4": 1035}` |
| validation | `{"0": 12, "1": 9, "2": 36, "3": 19, "4": 331}` |
| ood_diagnostic | `{"0": 18, "1": 14, "2": 36, "3": 63, "4": 296}` |

## Leakage gates

Dataset validation passed:

- trace-level split disjoint: true;
- leakage-group split disjoint: true;
- normalization not fit during dataset build;
- teacher labels not model inputs;
- future throughput/download time not model inputs;
- legacy dry-runs not used.
