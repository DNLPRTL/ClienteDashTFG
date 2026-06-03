# Phase 6A0 Open Gaps For Phase 6B/C

Status: open hardening and protocol tasks. No code is changed in this block.

## Hardening Gaps

| Gap | Why it matters | Future action |
| --- | --- | --- |
| `canonical_content_fingerprint` audit support | Phase 6 must block overlap by `trace_id`, `leakage_group` and `checksum_sha256`; future manifests should also support canonical content fingerprints | Harden `scripts/audit_phase6_trace_eligibility.py` in Phase 6B/C if manifests include `canonical_content_fingerprint` |
| Current audit script scope | Current `scripts/audit_phase6_trace_eligibility.py` checks `checksum_sha256`, `trace_id` and `leakage_group`, but does not appear to explicitly parse `canonical_content_fingerprint` | Record as a hardening task; do not modify the script in Phase 6A0 |
| Ghent duplicate materialization | `logs_all` plus per-mobility folders can duplicate traces | Before split, use one source path or deduplicate by checksum/fingerprint |
| Dataset access/license/format | Candidate datasets cannot be evaluated until local-only inspection is complete | Create conversion specs and manifest checks outside Git |
| Lancaster missing source note/card | Lancaster is intended for Phase 6C discussion, but no source card was included in the current wave pack | Do not authorize Lancaster until a source note/card exists |
| ABRBench source/dataset boundary | SABR mentions ABRBench, but ABRBench itself is not materialized or licensed in this block | Treat as deferred until dataset card/access/license/format checks |
| VMAF/P.1203/MOS artifacts | Perceptual claims need media/perceptual artifacts and a metric decision | Keep deferred until artifact-dependent protocol exists |
| Statistical comparison plan | No final ranking/winner can exist without a planned comparison method | Draft Phase 6A2 statistical comparison before benchmark authorization |
| Evidence ZIP procedure | Future run artifacts need a strict external package contract | Use `ubuntu_evidence_package_spec.md` before any execution |

## Protocol Gaps Closed By Phase 6A2

- Controller matrix is frozen in `controller_matrix.md`.
- Trace group policy is frozen in `trace_selection_policy.md`.
- Media profile policy is frozen in `media_profile_decision.md`.
- Metrics and gate semantics are frozen in `metrics_schema.md`.
- Statistical comparison policy is frozen in `statistical_comparison.md`.
- Results table and figure plan is frozen in `results_tables_plan.md`.

## Remaining Readiness Gaps

- Final trace IDs remain open until `phase6_trace_manifest_final.json` exists after eligibility audit.
- HSDPA/Ghent materialization still requires local-only access/license/format checks.
- OOD materialization still requires Raca 4G, Raca 5G and Lumos5G access/license/format checks.
- Lancaster remains unauthorized for primary final evaluation until a source card/source note exists and eligibility audit proves no overlap.
- Evidence package wiring remains future technical readiness work.

## Non-Action In This Block

This block intentionally does not:

- modify `scripts/audit_phase6_trace_eligibility.py`;
- implement benchmark code;
- run benchmark commands;
- generate plots;
- create rankings;
- declare a winner;
- claim QoE improvement.
