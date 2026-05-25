# Phase 3.5A0 Search Protocol

## Technical question

Which QoE/reward definition and evaluation semantics can be defended for DashClientModular4 before formal controller comparison and before IA/RL work?

## Search goals

The search must identify evidence for:

- quality utility or bitrate utility;
- rebuffering or stalling penalty;
- bitrate switching, quality variation or smoothness penalty;
- startup delay or initial delay;
- perceptual quality metrics such as VMAF;
- distinction between training reward and evaluation metric;
- methodological risks and overclaiming risks;
- practical feasibility for a reproducible Python DASH TFG.

## Source categories

| category | meaning |
| --- | --- |
| mandatory | Must be carded before the Phase 3.5 QoE decision. |
| mandatory technical reference | Must be carded as official implementation/tooling reference, not as the only scientific justification. |
| recommended context | Useful for memory, defense, limitations and future work. |
| optional/deferred | Do not card unless a later decision re-opens the source. |
| rejected | Do not use for this phase. |

## Repository boundary

Raw PDFs, HTML captures, local Markdown captures, datasets, generated CSVs, logs, ZIPs and media files must not be committed.