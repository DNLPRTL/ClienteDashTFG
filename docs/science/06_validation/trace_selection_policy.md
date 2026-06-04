# Phase 6 Trace Selection Policy

Status: final Phase 6A2 protocol decision plus Phase 6B readiness hardening. No trace IDs are frozen in this document.

## Phase 4E2 Historical Usage

Phase 4E2 used traces from these dataset families:

| Dataset family | Phase 4E2 trace count |
| --- | ---: |
| `ghent_4g_lte_bandwidth_logs` | 85 |
| `hsdpa_norway_mmsys2013` | 5 |
| `lancaster_abr_throughput_traces` | 120 |

These counts are historical leakage context, not Phase 6 evaluation evidence.

## Final Trace Freeze Rule

Final Phase 6 trace IDs must be frozen only by:

```text
phase6_trace_manifest_final.json
```

Do not invent trace IDs in protocol documents. The final manifest must be produced only after Phase 6C real dataset materialization outside the repository and eligibility audit. It must include enough identity fields to block overlap with Phase 4.

## Required Eligibility Keys

Phase 6 final traces must be blocked against Phase 4 by:

- `trace_id`;
- `leakage_group`;
- `checksum_sha256`;
- `canonical_content_fingerprint`.

Phase 6B closes the audit gap for `canonical_content_fingerprint`. `checksum_sha256` and `canonical_content_fingerprint` are separate identity fields and both must be reported when available.

## Recommended Evaluation Groups

| Group | Candidate datasets | Authorization condition |
| --- | --- | --- |
| `same_family_clean` | HSDPA/Ghent | Allowed only for traces with no overlap with Phase 4 by `trace_id`, `leakage_group`, `checksum_sha256` or `canonical_content_fingerprint`. |
| `OOD_final` | Raca 4G, Raca 5G, Lumos5G | Subject to access, license, format, conversion and eligibility checks. |
| `Lancaster` | Lancaster ABR throughput traces | Excluded from primary final evaluation unless a source card/source note is added and eligibility audit proves no overlap; otherwise excluded or `diagnostic_only`. |

## Ghent Duplicate Rule

Use `logs_all` OR per-mobility folders, not both, unless deduplicated by checksum/fingerprint before split. If both source forms appear during inspection, grouping must prefer `canonical_content_fingerprint` when present and fall back to `checksum_sha256`.

## Gate Outcomes

- `use_for_eval`: trace/session rows are eligible for final statistical summaries.
- `diagnostic_only`: retained for inspection or debugging, excluded from final evaluation tables.
- `do_not_use_for_eval`: excluded from final evaluation and diagnostic claims.

If `eval_gate` is present, it dominates split-name heuristics. `use_for_eval` marks a record as evaluation material; `diagnostic_only` and `do_not_use_for_eval` exclude it. Empty or unknown gate values fall back to split heuristics.

`same_family_clean`, `ood_final`, `primary_eval` and `phase6_eval` are evaluation splits when `eval_gate` is absent. `diagnostic_only` and `do_not_use_for_eval` are not evaluation splits unless `eval_gate` explicitly says `use_for_eval`.

## Non-Authorization

This policy does not download datasets, create final manifests, execute runs, or generate results. `ready_for_phase6c` is not `ready_for_benchmark`, and `benchmark_authorized` remains false in Phase 6B.
