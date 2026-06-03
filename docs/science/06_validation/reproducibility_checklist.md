# Phase 6 Reproducibility Checklist

Status: final Phase 6A2 protocol decision. Checklist for future readiness/execution only.

## Before Execution

- Confirm clean Git status before run.
- Record exact Git head.
- Freeze controller matrix and controller configs.
- Freeze `media_profile_phase6_v1`.
- Freeze `phase6_trace_manifest_final.json` after eligibility audit.
- Confirm no Phase 4 overlap by `trace_id`, `leakage_group`, `checksum_sha256` or `canonical_content_fingerprint` when available.
- Confirm datasets, runs, logs, zips, CSVs and media stay outside Git.
- Confirm `qoe_linear_v1` and `reward_n` are unchanged.

## Required Future Evidence Package Files

The future evidence package must align with `ubuntu_evidence_package_spec.md` and include:

- `commands_used.sh`;
- `terminal_transcript.txt`;
- git status before/after;
- git head;
- environment;
- artifact manifest;
- trace manifest audit report;
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

This checklist does not execute a benchmark and does not create artifacts.
