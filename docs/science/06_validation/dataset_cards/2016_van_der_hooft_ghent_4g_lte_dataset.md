# Dataset Card: Ghent 4G/LTE Bandwidth Logs

## Identity

- Dataset ID: `2016_van_der_hooft_ghent_4g_lte_dataset`
- Source intake: `phase6a0_wave3_4_md/wave3_trace_dataset_sources/2016_van_der_hooft_ghent_4g_lte_dataset_page_note.md`
- Authors/project: Jeroen van der Hooft et al., Ghent University
- Year: measurements from 2015-12-16 to 2016-02-04; related paper 2016
- Domain: mobile 4G/LTE, Ghent, Belgium
- Phase 6A0 role: first materialization candidate with duplicate guardrail

## Candidate Role

Ghent is a strong first materialization candidate after or alongside HSDPA because it is public, compact, mobile and LTE-oriented.

## Hard Duplicate Rule

Use `logs_all` OR per-mobility folders, but not both unless the materialization is deduplicated by checksum/fingerprint before split.

This rule is mandatory because the intake notes identify both aggregate and per-mobility archives. Path names are not a sufficient trace identity.

## Use Conditions

- Keep raw and normalized data outside the repository.
- Verify access, license/redistribution status and exact file format before conversion.
- Decide whether the source of truth is `logs_all` or per-mobility archives.
- If both are inspected, compute `checksum_sha256` and `canonical_content_fingerprint` before split.
- Block duplicate fingerprints across train/validation/test/OOD.
- Block overlap with Phase 4 by `trace_id`, `leakage_group` and `checksum_sha256`.
- Preserve mobility labels if per-mobility archives are used.

## Split Candidate

Phase 6C candidate for first controlled LTE split after deduplication and format/license checks. Not authorized for Phase 6A0 benchmarking.

## Readiness

Readiness: `candidate_not_materialized`.

Required before use:

- local-only download outside Git;
- duplicate plan for `logs_all` versus mobility archives;
- normalized manifest with checksums/fingerprints;
- Phase 4 overlap audit;
- documented split decision.
