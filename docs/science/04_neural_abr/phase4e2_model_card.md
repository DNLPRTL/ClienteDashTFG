# Phase 4E.2 Model Card

Model: NeuralABR-Lite Candidate Scorer.

Training method: CPU-first behavior cloning from `robust_mpc` teacher labels over valid MPD representation candidates.

- Decision: `PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F`
- Device: `cpu`
- Epochs: `20`
- Batch size: `32`
- Trace count: `210`
- Dataset families: `{'ghent_4g_lte_bandwidth_logs': 85, 'hsdpa_norway_mmsys2013': 5, 'lancaster_abr_throughput_traces': 120}`
- Regime buckets: `{'high_mixed': 17, 'high_stable': 17, 'high_variable': 17, 'low_mixed': 17, 'low_variable': 1, 'mid_mixed': 22, 'mid_stable': 17, 'mid_variable': 17, 'very_high_mixed': 81, 'very_high_variable': 4}`

The model is not registered in DashClientModular4 and has not been benchmarked against deployed controllers.
