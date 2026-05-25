# QoE Terms Crosswalk

Status: draft scaffold.

| local term | possible paper terms | meaning | unit candidate | decision status |
| --- | --- | --- | --- | --- |
| quality_utility | bitrate, quality, utility, video quality, VMAF | positive contribution of selected representation quality | TBD | pending |
| rebuffering | stalling, freezing, playback interruption, buffer underrun | playback interruption after startup | seconds / ratio / events | pending |
| smoothness | bitrate switching, quality variation, quality change | penalty for changing delivered quality across segments | kbps, Mbps utility, VMAF points | pending |
| startup_delay | initial delay, startup latency, join time | time until playback starts | seconds | pending |
| perceptual_quality | VMAF, PSNR, SSIM, MOS proxy | content-aware or perceptual quality estimate | metric-specific | pending |
| failure_handling | incomplete session, runtime error, abort | non-comparable run/session states | gates/reasons | pending |
| evaluation_gate | use_for_eval, diagnostic_only, do_not_use_for_eval | controls whether an artifact can be used in evaluation | categorical | pending |
| training_reward | reward, RL objective, scalar feedback | candidate future IA reward | scalar per segment | pending |