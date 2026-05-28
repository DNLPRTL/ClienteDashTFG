# Source card: http_adaptive_streaming_review2025

## Bibliographic data

- Title: HTTP Adaptive Streaming: A Review on Current Advances and Future Challenges
- Authors: Christian Timmerer, Hadi Amirpour, Farzad Tashtarian, Samira Afzal, Amr Rizk, Michael Zink, Hermann Hellwagner
- Year: 2025
- Venue: ACM Transactions on Multimedia Computing, Communications, and Applications, Vol. 21, No. 7, Article 198
- DOI / stable URL: `10.1145/3736306`
- Local PDF: local-only, not committed: `C:\Users\danie\Documents\TFG\_literature\phase4_AI\03_wave3_frontier_surveillance\pdfs\HTTP Adaptive Streaming A Review on Current Advances and Future Challenges.pdf`

## Method family

- Family: survey/review.
- Scope: HAS/DASH foundations, video coding, delivery, consumption, ABR algorithms, QoE, energy efficiency and future challenges.
- Learning type: not an algorithmic paper.

## Relevance to DashClientModular4

### What this source justifies

- DashClientModular4 is correctly scoped as a client-side ABR project within HTTP Adaptive Streaming.
- DASH/HAS separates media representation from adaptation logic; the controller chooses among available representations.
- The memory should discuss QoE, ABR, DASH, energy and future challenges without claiming that Phase 4 solves the full streaming pipeline.

### What this source does NOT justify

- It does not justify any particular neural controller.
- It does not justify using VMAF now.
- It does not justify implementation changes in Phase 4A1.

## Decision impact

- Used for memory/taxonomy, not method selection.
- Supports chapter framing and terminology.
- Implementation consequence:
  - none in A1;
  - cite when explaining DASH/HAS/ABR/QoE context.

## Memory / thesis usage

- Chapter 2: HAS/DASH background.
- Chapter 2/3: QoE and ABR context.
- Future work: energy efficiency, low latency and neural codecs.
