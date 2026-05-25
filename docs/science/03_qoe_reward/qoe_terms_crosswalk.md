# QoE Terms Crosswalk

Status: distilled_phase3_5a1 evidence draft. This file normalizes terminology for Phase 3.5A2; it does not close a metric contract.

| local term | possible paper terms | meaning | unit candidate | decision status |
| --- | --- | --- | --- | --- |
| quality_utility | bitrate, video quality, quality, utility, VMAF, PSNR, SSIM | positive contribution of delivered representation quality or perceptual quality | kbps/Mbps, utility units, VMAF points or model-specific score | candidate term for A2 |
| rebuffering | stalling, freezing, playback interruption, buffer underrun | playback interruption after playback has started | seconds, ratio, event count | strong candidate term for A2 |
| smoothness | bitrate switching, quality variation, quality change, instability | penalty for changes in delivered quality across adjacent segments/chunks | abs utility delta, kbps/Mbps delta, VMAF-point delta | strong candidate term for A2 |
| startup_delay | initial delay, startup latency, join time | time until playback starts before the first rendered media | seconds | should be considered in A2; report-only if not measured homogeneously |
| perceptual_quality | VMAF, PSNR, SSIM, MOS proxy, signal fidelity, objective VQA | content-aware quality estimate or subjective-quality proxy | metric-specific; VMAF commonly 0-100 | likely secondary/deferred unless artifacts exist |
| training_reward | scalar reward, RL objective, ABR reward, controller objective | scalar feedback used by a learning controller or by an optimizer | reward units per segment/chunk or per run | future IA/RL term only; not opened in A1 |
| evaluation_metric | QoE score, average QoE per chunk, run-level QoE, evaluation objective | score used to summarize comparable runs for later evaluation | per-run scalar, per-chunk average, component table | candidate term for A2 |
| evaluation_gate | use_for_eval, diagnostic_only, do_not_use_for_eval, valid run, invalid run | categorical policy that decides whether an artifact is comparable | categorical gate and reason code | likely candidate for A2 gate policy |
| failure_handling | incomplete session, runtime error, failed run, non-comparable run, aborted session | treatment of artifacts that cannot be compared fairly | categorical state plus diagnostic reason | gate candidate, not hidden numeric QoE in A1 |
| latency | live latency, end-to-end delay, glass-to-glass delay, playback latency | delay relevant to live or low-latency streaming settings | seconds | deferred unless the A2 scope includes live/low-latency telemetry |

## Normalization notes

- `quality_utility` may be bitrate-derived in the current telemetry, log-derived for sensitivity, or perceptual if VMAF-like artifacts are available later.
- `rebuffering` and `stalling` are treated as equivalent local terms for playback interruption after startup.
- `startup_delay` is kept separate from `rebuffering` because the evidence distinguishes expected initial wait from unexpected playback interruption.
- `training_reward` and `evaluation_metric` may share formula families, but A2 must name the role explicitly.
- `evaluation_gate` and `failure_handling` exist to keep incomplete or failed artifacts out of numeric comparisons unless a later policy justifies another treatment.
