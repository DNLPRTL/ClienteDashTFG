# Dataset Card: Raca 4G LTE

## Identity

- Dataset ID: `2018_raca_4g_lte_dataset`
- Source intake: `phase6a0_wave3_4_md/wave3_trace_dataset_sources/2018_raca_beyond_throughput_4g_lte_dataset.md`
- Title: Beyond Throughput: a 4G LTE Dataset with Channel and Context Metrics
- Authors: Darijo Raca, Jason J. Quinlan, Ahmed H. Zahran, Cormac J. Sreenan
- Year/venue: 2018, ACM MMSys
- Domain: modern 4G LTE with channel/context metadata
- Phase 6A0 role: recommended future/OOD candidate

## Candidate Role

Raca 4G is useful as a future modern 4G OOD candidate. It includes throughput and richer metadata such as mobility/context. For DashClientModular4, throughput remains the primary trace signal; extra KPIs are metadata unless a later protocol explicitly allows them.

## Use Conditions

- Keep raw and normalized data outside the repository.
- Verify access, license/redistribution status and exact format.
- Separate production-real traces from synthetic/ns-3 material.
- Do not feed channel KPIs to controllers unless runtime availability and protocol fairness are documented.
- Add `trace_id`, `leakage_group`, `checksum_sha256` and future `canonical_content_fingerprint`.
- Report mobility/domain labels if materialized.

## Split Candidate

Future Phase 6C test/OOD candidate after HSDPA/Ghent materialization. Not required for initial protocol closure.

## Readiness

Readiness: `future_candidate_requires_checks`.

Open checks:

- access and license;
- parser feasibility;
- production/synthetic separation;
- checksum/fingerprint manifest;
- OOD split policy.
