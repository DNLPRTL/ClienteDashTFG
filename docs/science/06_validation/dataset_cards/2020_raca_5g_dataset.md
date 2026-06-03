# Dataset Card: Raca 5G

## Identity

- Dataset ID: `2020_raca_5g_dataset`
- Source intake: `phase6a0_wave3_4_md/wave3_trace_dataset_sources/2020_raca_beyond_throughput_next_generation_5g_dataset.md`
- Title: Beyond Throughput, The Next Generation: A 5G Dataset with Channel and Context Metrics
- Authors: Darijo Raca, Dylan Leahy, Cormac J. Sreenan, Jason J. Quinlan
- Year/venue: 2020, ACM MMSys
- Domain: 5G, channel/context metadata, static and car mobility
- Phase 6A0 role: recommended future/OOD candidate

## Candidate Role

Raca 5G is a future OOD candidate for modern cellular behavior. It should not block first Phase 6 protocol closure and should not be mixed with 3G/4G results without clear labels.

## Use Conditions

- Keep raw and normalized data outside the repository.
- Verify access, license/redistribution status and exact format.
- Separate video-streaming and file-download traces if both are used.
- Separate production-real and synthetic/ns-3 material.
- Do not expose radio KPIs as controller features unless a later fairness spec allows them.
- Add checksum/fingerprint manifest fields before split.

## Split Candidate

Future Phase 6C OOD candidate. Recommended only after access/license/format checks.

## Readiness

Readiness: `future_candidate_requires_checks`.

Open checks:

- access and license;
- trace signal compatibility with the Python trace-driven runner;
- production/synthetic separation;
- OOD report plan.
