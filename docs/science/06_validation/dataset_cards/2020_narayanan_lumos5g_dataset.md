# Dataset Card: Lumos5G

## Identity

- Dataset ID: `2020_narayanan_lumos5g_dataset`
- Source intake: `phase6a0_wave3_4_md/wave3_trace_dataset_sources/2020_narayanan_lumos5g_mmwave_throughput_dataset.md`
- Title: Lumos5G: Mapping and Predicting Commercial mmWave 5G Throughput
- Authors: Arvind Narayanan, Eman Ramadan, Rishabh Mehta, Xinyue Hu, Qingxu Liu, Rostand A. K. Fezeu, Udhaya Kumar Dayalan, Saurabh Verma, Peiqi Ji, Tao Li, Feng Qian, Zhi-Li Zhang
- Year/venue: 2020, ACM IMC
- Domain: commercial 5G mmWave throughput, mobility/handoff variability
- Phase 6A0 role: recommended future/OOD candidate

## Candidate Role

Lumos5G is a future OOD candidate for high-variance mmWave 5G behavior. Its value is primarily to test robustness under modern cellular variability if access, license and format are manageable.

## Use Conditions

- Keep raw and normalized data outside the repository.
- Verify access, license/redistribution status and exact format.
- Treat as a separate OOD family, not as the same domain as Raca 5G.
- Do not use Lumos5G prediction features as controller inputs.
- Add checksum/fingerprint manifest fields before split.
- Report 5G/mmWave limitations separately from HSDPA/Ghent.

## Split Candidate

Future Phase 6C OOD candidate. Not required for first evaluation path.

## Readiness

Readiness: `future_candidate_requires_checks`.

Open checks:

- public data access;
- license/redistribution status;
- parser feasibility;
- mmWave OOD split policy;
- checksum/fingerprint manifest.
