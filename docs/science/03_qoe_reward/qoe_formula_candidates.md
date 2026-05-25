# QoE Formula Candidates

Status: candidates only. No final formula is closed in Phase 3.5A0.

## Candidate families

| candidate | description | expected role | status |
| --- | --- | --- | --- |
| qoe_linear_candidate | quality utility based on bitrate minus rebuffering and switching penalties | likely primary or baseline candidate | pending evidence |
| qoe_log_candidate | log or concave quality utility minus penalties | sensitivity or alternative candidate | pending evidence |
| qoe_perceptual_candidate | VMAF or perceptual utility minus penalties | likely deferred or secondary unless practical inputs exist | pending evidence |
| startup_penalty_candidate | explicit startup delay penalty term | report-only or optional penalty candidate | pending evidence |
| failure_gate_candidate | use gates for incomplete/invalid sessions instead of numeric punishment | likely artifact policy candidate | pending evidence |

## Non-decision

This file must not be used as implementation input until Phase 3.5A2 closes qoe_selection.md and reward_definition.md.