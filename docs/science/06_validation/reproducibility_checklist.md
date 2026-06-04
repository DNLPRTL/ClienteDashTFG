# Phase 6 Reproducibility Checklist

Status: final Phase 6A2 protocol decision plus Phase 6B/6C/6D readiness gates. Checklist for future readiness/execution only.

## Before Execution

- Confirm clean Git status before run.
- Record exact Git head.
- Freeze controller matrix and controller configs.
- Freeze `media_profile_phase6_v1`.
- Extract, validate, compatibility-check and freeze `media_profile_phase6_v1` outside the repository with `scripts/run_phase6d_media_profile_freeze.py`.
- Complete Phase 6C real dataset materialization outside the repository with `scripts/run_phase6c_trace_materialization.py`.
- Do not manually create source configs, candidate manifests or final manifests.
- Freeze external `phase6_trace_manifest_final.json` after acquisition, extraction, normalization, validation, eligibility audit and freeze.
- Freeze external `media_profile_phase6_v1.json` after MPD extraction, validation, NeuralABR-Lite compatibility check and freeze.
- Confirm the server/VM was used only as MPD/content/media_profile source, not as benchmark network.
- Confirm future benchmark network conditions remain normalized traces through `TraceDrivenNetworkModel`.
- Confirm the media profile records 60 s duration, 4 s segments, 15 segments and the ascending ladder `300/750/1200/1850/2850/4300` kbps when using the provided MPD.
- Confirm real segment sizes were used when `--content-root` or `--base-url` made them available, or that bitrate-estimated sizes are explicitly labeled.
- Confirm NeuralABR-Lite candidate-count compatibility; if only 5 candidates are supported, confirm the common primary subset and diagnostic full ladder are recorded.
- Validate the candidate manifest with `scripts/validate_phase6_trace_manifest.py --strict-final`.
- Run `scripts/audit_phase6_trace_eligibility.py` against the Phase 4 dataset manifest and Phase 6 candidate manifest.
- Confirm no Phase 4 overlap by `trace_id`, `leakage_group`, `checksum_sha256` or `canonical_content_fingerprint`.
- Run `scripts/check_phase6_evaluation_readiness.py` and keep its report with the evidence package.
- Confirm datasets, normalized CSVs, receipts, local manifests, reports, runs, logs, zips and media stay outside Git.
- Confirm `qoe_linear_v1` and `reward_n` are unchanged.
- Confirm `ready_for_phase6c` has not been misread as benchmark authorization.

## Required Future Evidence Package Files

The future evidence package must align with `ubuntu_evidence_package_spec.md` and include:

- `commands_used.sh`;
- `commands_used.ps1`;
- `terminal_transcript.txt`;
- git status before/after;
- git head;
- environment;
- artifact manifest;
- trace manifest audit report;
- trace manifest validation report;
- Phase 6C materialization summary;
- frozen external `phase6_trace_manifest_final.json`;
- Phase 6D media-profile validation report;
- Phase 6D media-profile compatibility report;
- Phase 6D media-profile freeze summary;
- frozen external `media_profile_phase6_v1.json`;
- Phase 6 evaluation readiness report;
- controller matrix summary;
- per-controller trace summary;
- QoE summaries;
- run logs;
- selected segment samples;
- exclusions and gates.

## Review Fields

The package must allow review of:

- controller;
- trace_id;
- split;
- media_profile;
- representation selected by segment;
- bitrate;
- buffer before/after;
- download time;
- rebuffer;
- switching;
- QoE segment/session;
- gates/exclusions;
- exact commands;
- exact commit;
- exact environment.

## After Execution

- Record Git status after run.
- Verify artifact manifest checksums.
- Verify no generated artifacts were committed.
- Verify gates/exclusions are summarized.
- Verify statistical scripts use session/trace as the unit.

## Non-Authorization

This checklist does not execute a benchmark. Phase 6C/6D create external preparation artifacts only. `ready_for_benchmark=false` and `benchmark_authorized=false` remain mandatory.
