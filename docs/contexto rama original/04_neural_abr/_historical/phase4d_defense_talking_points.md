# Phase 4D defense talking points

- Phase 4D implements an offline pipeline, not a neural controller integrated into the DASH client.
- The selected method remains NeuralABR-Lite Candidate Scorer: a small shared MLP trained by behavior cloning.
- The action is always `representation_index` inside the MPD ladder; there is no raw bitrate or continuous action.
- The teacher is `robust_mpc` primary and `mpc` secondary. The bounded oracle is diagnostic-only and not used as a training source.
- The model input contains only pre-decision context and candidate metadata. Teacher labels, rewards, trace IDs, split labels, source datasets, future throughput, and future download times are not model inputs.
- Trace replay reuses `normalized_trace_schema_v1` and the existing Phase 3 network model instead of inventing a new raw trace format.
- Normalization is fitted on train samples only. Validation and OOD samples cause fit to fail.
- The model is CPU-first PyTorch with a tiny MLP, deterministic seed setup, and no Ray/RLlib, Stable-Baselines, TensorFlow, gymnasium, pandas, scikit-learn, CUDA, ROCm, DirectML, WSL, transformer, MoE, or PPO requirement.
- The synthetic smoke proves that the pipeline can build, validate, train for one epoch, and run offline sanity checks. It does not prove final QoE superiority.
- OOD is reported separately as diagnostic-only. It is not hidden and not used to tune normalization.
- Generated datasets, checkpoints, logs, and validation reports stay outside the repository.
- Phase 5 client integration remains blocked until later Phase 4 export/inference and acceptance gates explicitly allow it.
