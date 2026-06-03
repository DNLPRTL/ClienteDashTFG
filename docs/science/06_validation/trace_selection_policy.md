# Phase 6 Trace Selection Policy

Status: final Phase 6A2 protocol decision. No trace IDs are frozen in this document.

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

Do not invent trace IDs in protocol documents. The final manifest must be produced only after eligibility audit and must include enough identity fields to block overlap with Phase 4.

## Required Eligibility Keys

Phase 6 final traces must be blocked against Phase 4 by:

- `trace_id`;
- `leakage_group`;
- `checksum_sha256`;
- `canonical_content_fingerprint` when present in manifests.

## Recommended Evaluation Groups

| Group | Candidate datasets | Authorization condition |
| --- | --- | --- |
| `same_family_clean` | HSDPA/Ghent | Allowed only for traces with no overlap with Phase 4 by `trace_id`, `leakage_group`, `checksum_sha256` or `canonical_content_fingerprint`. |
| `OOD_final` | Raca 4G, Raca 5G, Lumos5G | Subject to access, license, format, conversion and eligibility checks. |
| `Lancaster` | Lancaster ABR throughput traces | Not authorized for primary final evaluation unless a source card/source note is added and eligibility audit proves no overlap; otherwise excluded or `diagnostic_only`. |

## Ghent Duplicate Rule

Use `logs_all` OR per-mobility folders, not both, unless deduplicated by checksum/fingerprint before split.

## Gate Outcomes

- `use_for_eval`: trace/session rows are eligible for final statistical summaries.
- `diagnostic_only`: retained for inspection or debugging, excluded from final evaluation tables.
- `do_not_use_for_eval`: excluded from final evaluation and diagnostic claims.

## Non-Authorization

This policy does not download datasets, create manifests, execute runs, or generate results.
