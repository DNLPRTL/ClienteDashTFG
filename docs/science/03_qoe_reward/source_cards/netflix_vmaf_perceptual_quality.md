# Source card - netflixVmaf

Status: distilled_phase3_5a1

## Identity

| field | value |
| --- | --- |
| source id | QOE-M08 |
| title | VMAF official Netflix repository reference |
| authors | Netflix |
| year | 2026 access |
| venue | official technical source |
| DOI or URL | https://github.com/Netflix/vmaf |
| local source file | 08_netflix_vmaf_reference_source.md |
| source type | Official technical source |
| triage status | mandatory technical reference |
| distillation basis | Phase 3.5A1 evidence pack; raw source kept outside repository |

## Why this source matters for Phase 3.5

- It is the official technical reference for VMAF and libvmaf.
- It explains practical tooling requirements for perceptual-quality measurement.
- It helps document why VMAF is artifact-dependent and should not be silently inferred from bitrate-only telemetry.

## QoE / reward terms found

| term | present? | description | units | notes |
| --- | --- | --- | --- | --- |
| quality utility | yes | VMAF can provide a perceptual quality score. | VMAF score/model output | Only if required video artifacts exist. |
| rebuffering or stalling | no | VMAF does not measure playback interruptions. | not applicable | Needs separate telemetry terms. |
| switching or smoothness | indirect | Smoothness could be computed from per-segment VMAF changes, but VMAF itself is not a switch penalty. | VMAF-point delta if artifacts exist | Not available from current bitrate-only path. |
| startup delay | no | Startup delay is outside VMAF. | not applicable | Use separate telemetry. |
| perceptual quality or VMAF | strong yes | Official reference for VMAF, libvmaf, Python wrapper and FFmpeg integration. | VMAF score, model-dependent | Strong technical source, not peer-reviewed QoE formula. |
| latency | no | VMAF does not measure latency. | not applicable | Defer live-latency metrics. |
| failure or incomplete session handling | not addressed directly | Does not define run comparability gates. | categorical gate needed locally | A2 should define local gate policy. |

## Exact formula or model

- VMAF is treated here as an official perceptual-quality model/tooling reference, not as a complete ABR QoE formula.
- The relevant practical model requirement is comparison between reference and distorted video through supported tooling such as libvmaf/FFmpeg.

## Weights and parameters

- VMAF uses model/tool parameters outside the current A1 scope.
- No DashClientModular4 QoE weights are selected here.

## What is optimized

- Nothing in DashClientModular4 is optimized by this source in A1.
- VMAF is a measurement/tooling reference, not a controller objective by itself.

## What is measured or reported

- Perceptual video quality under the requirements of the VMAF tooling path.
- It does not report rebuffering, startup, smoothness or failure handling without external telemetry.

## Evaluation context

| field | value |
| --- | --- |
| VoD/live/low-latency | video-quality analysis context |
| simulator/emulator/real deployment | technical tooling reference |
| traces/datasets | requires reference/distorted video artifacts rather than throughput traces alone |
| baselines | not a controller baseline source |

## What it justifies for DashClientModular4

- VMAF can be cited as a perceptual-quality candidate only if artifacts and tooling are present.
- A1 should not add video-quality analysis dependencies.
- A2 should mark perceptual quality as secondary/deferred unless a reproducible artifact contract exists.

## What it does not justify

- It is not a peer-reviewed QoE paper for the whole ABR metric.
- It does not justify VMAF as a primary metric if the pipeline does not produce per-segment VMAF.
- It does not justify adding libvmaf or FFmpeg analysis work in A1.

## Practical decision candidate

- Use for `qoe_perceptual_candidate` requirements and defer unless artifacts exist.

## Use in memory

| chapter/asset | use |
| --- | --- |
| Chapter 2 | Technical reference for VMAF/perceptual quality |
| Chapter 6 | Explain why perceptual metrics require reference/distorted artifacts |
| Tables | Evidence matrix row for VMAF requirements |
| Figures | Perceptual artifact branch in telemetry-to-QoE mapping |
| Defense | Explain why VMAF is not available from bitrate telemetry alone |
| Bibliography | Add as official technical source if cited |
