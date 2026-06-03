# Dataset Card: Norway HSDPA / MMSys 2013

## Identity

- Dataset ID: `2013_riiser_hsdpa_norway_dataset`
- Source intake: `phase6a0_wave3_4_md/wave3_trace_dataset_sources/2013_riiser_hsdpa_norway_dataset_page_note.md`
- Authors/project: Haakon Riiser, Paul Vigmostad, Carsten Griwodz, Pal Halvorsen
- Year: 2013 paper; tests from 2010-09-13 to 2011-04-21
- Domain: mobile 3G/HSDPA, Norway
- Phase 6A0 role: first materialization candidate

## Candidate Role

HSDPA Norway is a first candidate for real trace materialization because it is public, compact and close to mobile HTTP adaptive streaming. It should be used to exercise conversion, normalization and split/audit discipline before broader OOD work.

## Use Conditions

- Keep raw and normalized data outside the repository.
- Verify access, license/redistribution status and exact file format before conversion.
- Add `trace_id`, `leakage_group`, `checksum_sha256` and, when available, `canonical_content_fingerprint` to any future manifest.
- Treat the domain as historical 3G/HSDPA; do not overclaim modern 4G/5G behavior.
- Block any trace that overlaps Phase 4 by trace ID, leakage group or checksum.

## Split Candidate

Phase 6C candidate for first controlled split after format/license checks. Not authorized for Phase 6A0 benchmarking.

## Readiness

Readiness: `candidate_not_materialized`.

Required before use:

- local-only download outside Git;
- format/unit inspection;
- conversion spec;
- manifest with checksums/fingerprints;
- Phase 4 overlap audit;
- documented split decision.
