# Phase 6 Trace Manifest Schema

Status: Phase 6B readiness contract. No trace IDs are frozen by this document.

Canonical manifest schema version:

```text
phase6_trace_manifest_v1
```

The manifest is a structural input for eligibility and readiness checks. It is not a benchmark result, does not contain rankings, and does not authorize execution.

## Accepted Containers

The Phase 6 scripts accept the same checked-in JSON container shapes:

- `trace_records`
- `records`
- `traces`
- `items`
- `splits`

`splits` may map a split name to a list of records, or to an object containing one of the list keys above. When a record omits `split`, the surrounding split key is used.

## Record Fields

Phase 6B validators inspect these fields:

| Field | Purpose |
| --- | --- |
| `trace_id` | Stable local trace identifier. |
| `dataset_family` | Dataset family or source group. |
| `split` | Phase 6 split or gate-oriented split group. |
| `eval_gate` | Eligibility gate. |
| `trace_csv` or `source_path` | Traceability pointer to local material outside Git. |
| `schema_version` | Normalized trace row schema, expected as `normalized_trace_schema_v1` for final eval records. |
| `checksum_sha256` | Byte-level checksum identity. |
| `canonical_content_fingerprint` | Canonical content identity after path/source normalization when available. |
| `leakage_group` | Group identity used to block same-source leakage. |
| `duration_s` | Optional positive duration. |
| `sample_count` | Optional positive sample count. |
| `license_status` | Access/license status. |
| `exclusion_reason` | Required rationale for `do_not_use_for_eval` records. |

## Aliases

`eval_gate` aliases:

- `eval_gate`
- `row_eval_gate`
- `session_eval_gate`
- `use_for_eval`
- `eligibility_gate`

`canonical_content_fingerprint` aliases:

- `canonical_content_fingerprint`
- `content_fingerprint`
- `content_sha256`
- `canonical_sha256`
- `trace_content_fingerprint`

`checksum_sha256` remains separate from `canonical_content_fingerprint`. Phase 6B reports both fields independently and does not replace one with the other.

## Gates

- `use_for_eval`: eligible for future Phase 6 final summaries after all checks pass.
- `diagnostic_only`: retained for audit/debug context, excluded from final evaluation.
- `do_not_use_for_eval`: excluded from evaluation and diagnostic claims.

If `eval_gate` is present, `use_for_eval` makes the record an evaluation record, while `diagnostic_only` and `do_not_use_for_eval` exclude it. Empty or unknown gate values fall back to split heuristics.

If `eval_gate` is absent, these splits are treated as evaluation splits:

- `validation`
- `val`
- `test`
- `ood`
- `eval`
- `same_family_clean`
- `ood_final`
- `primary_eval`
- `phase6_eval`

`diagnostic_only` and `do_not_use_for_eval` are not evaluation splits unless `eval_gate` explicitly says `use_for_eval`.

## Strict Final Requirements

For `use_for_eval` records, strict final validation requires:

- `trace_id`
- `dataset_family`
- `split`
- `eval_gate=use_for_eval`
- `trace_csv` or `source_path`
- `checksum_sha256`
- `canonical_content_fingerprint`
- `leakage_group`
- `schema_version=normalized_trace_schema_v1`, unless a schema note documents the exception
- positive `duration_s` if present
- positive `sample_count` if present
- empty `exclusion_reason`

Duplicate `trace_id`, `checksum_sha256`, `canonical_content_fingerprint` or `leakage_group` values among `use_for_eval` records are strict-final errors.

## Phase Boundary

Final Phase 6 trace IDs are still not frozen. They become frozen only when the post-Phase 6C external materialization produces:

```text
phase6_trace_manifest_final.json
```

Phase 6B validates schema readiness and audit readiness only. Phase 6C is the next phase for real dataset materialization outside the repository.
