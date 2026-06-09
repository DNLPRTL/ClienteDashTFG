# SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming

## 0. Ficha de archivo

- Archivo fuente: `SODA.pdf`
- Paginas detectadas: 32
- SHA256 PDF: `504299f85012e30a8ddd41af17933d92063acfed5d1acdd2f7958246e62bef2f`
- Texto crudo auxiliar: `raw_text/26_soda_2024_consistent_high_quality_non_neural_abr.txt`
- Texto layout auxiliar: `raw_text_layout/26_soda_2024_consistent_high_quality_non_neural_abr_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:30

## 1. Uso previsto para Fase 4-5 v1

Fuente no-IA fuerte para consistencia, smoothness, deployability y limites de controllers aprendidos. Relevante para Fase 4-5 v1 como referencia de seguridad, calidad estable y comparador conceptual frente a IA.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
SODA: An Adaptive Bitrate Controller for Consistent
High-Quality Video Streaming
Tianyu Chen
University of Massachusetts Amherst
Amherst, MA, USA
tianyuchen@umass.edu
Yiheng Lin
California Institute of Technology
Pasadena, CA, USA
yihengl@caltech.edu
Nicolas Christianson
California Institute of Technology
Pasadena, CA, USA
nchristianson@caltech.edu
Zahaib Akhtar
Amazon Prime Video / NCSU
Sunnyvale, CA, USA
akhtz@amazon.com
Sharath Dharmaji
Amazon Prime Video
Sunnyvale, CA, USA
sharatdr@amazon.com
Mohammad Hajiesmaili
University of Massachusetts Amherst
Amherst, MA, USA
hajiesmaili@cs.umass.edu
Adam Wierman
California Institute of Technology
Pasadena, CA, USA
adamw@caltech.edu
Ramesh K. Sitaraman
University of Massachusetts Amherst
Amherst, MA, USA
ramesh@cs.umass.edu
ABSTRACT
The primary objective of adaptive bitrate (ABR) streaming is to
enhance users’ quality of experience (QoE) by dynamically adjust-
ing the video bitrate in response to changing network conditions.
However, users often find frequent bitrate switching frustrating
due to the resulting inconsistency in visual quality over time, es-
pecially during live streaming when buffer lengths are short. In
this paper, we propose a practical smoothness optimized dynamic
adaptive (SODA) controller that specifically addresses this problem
while remaining deployable. SODA is backed by theoretical guaran-
tees and has shown superior performance in empirical evaluations.
Specifically, our numerical simulations show a 9.55% to 27.8% QoE
improvement and our prototype evaluation shows a 30.4% QoE im-
provement compared to the state-of-the-art baselines. In order to be
widely deployable, SODA performs bitrate horizon planning in poly-
nomial time compared to brute force approaches that suffer from
exponential complexity. To demonstrate its real-world practicality,
we deployed SODA on a wide range of devices within the production
network of Amazon Prime Video. Production experiments show
that SODA reduced bitrate switching by up to 88.8% and increased
average stream viewing duration by up to 5.91% compared to a
fine-tuned production baseline.
CCS CONCEPTS
• Information systems →Multimedia streaming; • Theory of
computation →Online algorithms; Theory and algorithms
for application domains.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0614-1/24/08
https://doi.org/10.1145/3651890.3672260
KEYWORDS
Adaptive bitrate streaming, Smoothed online convex optimization
ACM Reference Format:
Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath
Dharmaji, Mohammad Hajiesmaili, Adam Wierman, and Ramesh K. Sitara-
man. 2024. SODA: An Adaptive Bitrate Controller for Consistent High-
Quality Video Streaming. In ACM SIGCOMM 2024 Conference (ACM SIG-
COMM ’24), August 4–8, 2024, Sydney, NSW, Australia. ACM, New York, NY,
USA, 32 pages. https://doi.org/10.1145/3651890.3672260
1
INTRODUCTION
With the growth of online video streaming, users nowadays stream
videos from a highly diverse set of devices, including laptops, mobile
devices, smart TVs, set-top boxes, game consoles, etc. These devices
span a wide spectrum of hardware capabilities and connect to the
Internet in a multitude of ways, e.g., wireless, cellular, cable, etc. To
ensure a high quality of experience (QoE) across all devices, video
providers utilize adaptive bitrate (ABR) streaming that tailors video
delivery to specific devices and network conditions.
The goal of ABR streaming is to deliver a video at the highest sus-
tainable quality over time-varying network conditions. To achieve
this, a video source is encoded at different bitrates corresponding
to different resolutions, e.g., 720p, 1080p, 1440p, etc. Each encod-
ing is in turn temporally partitioned into a sequence of segments,
e.g., 2 seconds of video content. An ABR controller inside a user’s
video player then selects a suitable bitrate for each segment. Finally,
downloaded segments are stored in a buffer, till they are rendered.
Past studies have shown that a user’s QoE is maximized by de-
livering the video at the highest possible quality with minimal
rebuffering and bitrate switching. It has been shown that a 1% in-
crease in rebuffering time is correlated with a 3-minute reduction in
the viewing duration [7] and frequent bitrate switching is strongly
correlated with a user abandoning the session [21]. Going beyond
correlational studies, the significant causal impact of rebuffering
and other QoE performance metrics on key measures of user behav-
ior was first established in [9]. However, jointly optimizing all three
key components of QoE, i.e., video quality, rebuffering and bitrate
613
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Figure 1: Video stream duration is negatively correlated with
bitrate switching rate. Users watch < 10% of the stream when
bitrate switching rate is > 20%.
switching, is non-trivial as they are locked in a three-way trade-off.
An ideal ABR controller seeks to push the trade-off boundary and
optimize all three QoE components simultaneously.
Between on-demand and live streaming, the latter is more chal-
lenging as the player buffer is restricted to 10 - 20 seconds (to remain
close to actual live action), which is in contrast to 60 - 180 seconds
of buffer in on-demand streaming. Consequently, live streaming
has higher susceptibility to rebuffering and bitrate switching. To
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.5",
  "title": "SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming",
  "author": "Tianyu Chen; Yiheng Lin; Nicolas Christianson; Zahaib Akhtar; Sharath Dharmaji; Mohammad Hajiesmaili; Adam Wierman; Ramesh K. Sitaraman",
  "subject": "-  Information systems  ->  Multimedia streaming.-  Theory of computation  ->  Online algorithms.Theory and algorithms for application domains.",
  "keywords": "Adaptive bitrate streaming, Smoothed online convex optimization",
  "creator": "LaTeX with acmart 2024/04/17 v2.07 Typesetting articles for the Association for Computing Machinery and hyperref 2023-07-08 v7.01b Hypertext links for LaTeX",
  "producer": "pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2023) kpathsea version 6.3.5; modified using iText® Core 8.0.0 (AGPL version) ©2000-2023 Apryse Group NV",
  "creationDate": "D:20240627172014Z",
  "modDate": "D:20240713025550Z",
  "trapped": "",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 1: CCS CONCEPTS
- p. 1: INTRODUCTION
- p. 2: DESIGN GAPS, OPPORTUNITIES, AND
- p. 2: REQUIREMENTS
- p. 4: SODA OVERVIEW
- p. 5: THEORETICAL DESIGN INSIGHTS
- p. 7: IMPLEMENTATION DETAILS
- p. 8: EVALUATION
- p. 11: RELATED WORK
- p. 12: LIMITATIONS AND FUTURE WORK
- p. 12: CONCLUSION
- p. 12: ACKNOWLEDGMENTS
- p. 13: REFERENCES
- p. 15: PROOF OUTLINE
- p. 20: PROOFS OF THE EXPONENTIALLY DECAYING PERTURBATION BOUNDS
- p. 26: PROOFS FOR EXACT PREDICTIONS
- p. 29: PROOFS FOR INEXACT PREDICTIONS
- p. 31: PROOFS FOR EFFICIENT STRUCTURES

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 2: Figure 1: Video stream duration is negatively correlated with
- p. 2: Figure 2: BOLA’s [44] decision boundaries are spaced out for
- p. 3: Table 1: A qualitative summary of our key evaluation findings about SODA as compared to baseline ABR controllers.
- p. 3: Figure 3: A RobustMPC session where the controller intention-
- p. 4: Figure 4: A sample throughput function used to illustrate
- p. 5: Figure 5: SODA’s bitrate decision as a function of buffer level
- p. 6: Figure 6: Illustration of the exponentially decaying perturba-
- p. 6: Theorem 4.1. [Informal] When the predictions of the bandwidth in
- p. 6: Theorem 4.2. [Informal] Suppose the prediction error at each
- p. 7: Theorem 4.3. [Informal] Suppose SODA is given the predictions
- p. 7: Figure 7: We profiled the performance of the two throughput
- p. 7: Algorithm 1: SODA’s efficient approximate optimization
- p. 8: Figure 8: The probability that the bitrate decision produced
- p. 9: Figure 9: The mean throughput of the Puffer, 5G, and 4G datasets are 57.1, 31.3, and 13.0 Mb/s. The mean relative standard
- p. 10: Figure 10: The mean QoE scores, utilities, rebuffering ratios and switching rates of SODA and baseline ABR controllers under
- p. 10: Figure 11: The mean QoE scores for SODA and baseline ABR
- p. 11: Figure 13 shows SODA’s performance relative to the production
- p. 12: Figure 12: The mean QoE scores, utilities, rebuffering ratios, and switching rates from local deployment. SODA again has the
- p. 12: Figure 13: The change in mean viewing durations (higher is
- p. 15: Algorithm 2: SODA (for theoretical analysis)
- p. 17: Figure 14: Illustration of the aggregations of per-step errors. In the figure, {(𝑥∗

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 2: `tial to polynomial, e.g., about 200 iterations max in practice. In`
- p. 3: `over a prediction horizon of 𝐾segments, e.g., 𝐾= 5, which is so`
- p. 4: `level immediately after that time interval. Our objective is to min-`
- p. 4: `tion, e.g., 𝑣(𝑟𝑛) = 1/𝑟𝑛. It is then weighted by the amount of video`
- p. 4: `current bitrate, e.g., 𝑐(𝑟𝑛,𝑟𝑛−1) = (𝑣(𝑟𝑛) −𝑣(𝑟𝑛−1))2.`
- p. 4: `𝑥𝑛= 𝑥𝑛−1 + 𝜔𝑛Δ𝑡`
- p. 4: `−Δ𝑡∈[0,𝑥max],`
- p. 4: `𝜔1 = 4, 𝜔2 = 1, and 𝜔3 = 𝜔4 = 2 Mb/s given Δ𝑡= 1 s. By contrast,`
- p. 4: `duration is also 𝐿= 1 s, if the controller chooses 𝑟1 = 2 Mb/s and`
- p. 4: `𝑟2 = 2.5 Mb/s, then it takes 0.5 and 1 s to download the first and sec-`
- p. 4: `ond segments respectively, resulting in 𝜔1 = 4 and 𝜔2 = 2.5 Mb/s.`
- p. 5: `where ˆ𝜔𝑚|𝑛−1 (𝑚≥𝑛) is the throughput prediction for the 𝑚th`
- p. 5: `𝑥𝑚= 𝑥𝑚−1 +`
- p. 5: `𝑥𝑚∈[0,𝑥max],`
- p. 5: `including bandwidth predictions { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾and the previ-`
- p. 5: `as the inverse of the bitrates (i.e., 𝑢𝜏= 1/𝑟𝜏for all time step 𝜏) and`
- p. 5: `theoretical analysis. Under this property, when { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾`
- p. 6: `tion property: When { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾are fixed, the optimal`
- p. 6: `of 𝑅if cost(ALG) −cost(OPT) ≤𝑅always holds, and ALG achieves a`
- p. 6: `competitive ratio of 𝐶if cost(ALG) ≤𝐶· cost(OPT) always holds.`
- p. 6: `In this section, we set Δ𝑡= 1, R = [𝑟min,𝑟max], and 𝑣(𝑟) =`
- p. 6: `𝑣(𝑟) = log(𝑟max/𝑟), as long as certain regularity conditions hold;`
- p. 6: `window are accurate (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1).`
- p. 6: `future 𝐾steps are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1)`
- p. 6: `and the prediction horizon 𝐾≥𝑂(1), SODA achieves a dynamic`
- p. 6: `constraint boundary, i.e., 0 < 𝑥𝑛< 𝑥max. Further, define E = 𝜌2𝐾𝑁+`
- p. 6: `𝜅=1 𝜌𝜅𝐸𝜅, where 𝐸𝜅is the total squared error for predicting 𝜅steps`
- p. 7: `that satisfy ˆ𝜔𝑛|𝑛−1 = · · · = ˆ𝜔𝑛+𝐾−1|𝑛−1 at an intermediate time step`
- p. 7: `by a feasible monotonic bitrate trajectory with an error of 𝑂 𝐾/√𝛾.`
- p. 7: `min{𝑟∈R : 𝑟≥ˆ𝜔}.`
- p. 7: `1 ←null, obj∗←∞`
- p. 7: `foreach 𝑟1 ∈{𝑟∈R : 𝑟> 𝑟0}`
- p. 7: `2 = null then continue`
- p. 7: `sequences, i.e., it imposes an additional constraint that 𝑟𝑛−1 ≤𝑟𝑛≤`
- p. 7: `. . . ≤𝑟𝑛+𝐾−1 or 𝑟𝑛−1 ≥𝑟𝑛≥. . . ≥𝑟𝑛+𝐾−1. The pseudocode for a`
- p. 8: `able switching cost weight, e.g., below 5% for 𝐾= 4 and a relative`
- p. 8: `session duration, i.e., 𝜌rebuf = 𝑇rebuf/𝑇.`
- p. 8: `minus one, i.e., 𝑝switch = 𝑁switch/(𝑁−1).`
- p. 8: `components, i.e., QoE = ¯𝑣−𝛽· 𝜌rebuf −𝛾· 𝑝switch. In this work,`
- p. 8: `we chose 𝛽= 10 and 𝛾= 1 to reflect the high importance of`
- p. 8: `For all three datasets, we filtered out sessions shorter than 10 min-`
- p. 11: `¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching`
- p. 15: `bitrate (i.e., 𝑢𝑡= 1`
- p. 15: `𝑟𝑡). Recall that we set 𝑣(𝑟) = 1`
- p. 15: `s.t. 𝑥𝜏= 𝑥𝜏−1 + ˆ𝜔𝜏𝑢𝜏−1, for 𝜏= 𝑡, . . . ,𝑡+ 𝑝,`
- p. 15: `0 ≤𝑥𝜏≤𝑥max,`
- p. 15: `, for 𝜏= 𝑡, . . . ,𝑡+ 𝑝,`
- p. 15: `𝑥𝑡−1 = 𝜎𝑡−1,𝑢𝑡−1 = 𝜈𝑡−1.`
- p. 15: `For the terminal costs, we consider two types of functions: (1) The zero function 𝐹= 0, i.e., 𝐹(𝑥,𝑢) = 0 for all 𝑥,𝑢; (2) The indicator function`
- p. 15: `𝐹= I𝜎,𝜈, which is defined as`
- p. 15: `𝐹(𝑥,𝑢) = I𝜎,𝜈(𝑥,𝑢) =`
- p. 15: `if 𝑥= 𝜎,𝑢= 𝜈,`
- p. 15: `1: for 𝑡= 1, 2, . . . , 𝑁do`
- p. 15: `Set 𝑡′ = min{𝑡+ 𝐾−1, 𝑁}.`
- p. 15: `Set terminal cost 𝐹𝑡′ = I𝑥∗,1/ ˆ𝜔𝑡′|𝑡.`
- p. 15: `Set terminal cost 𝐹𝑡′ = 0.`
- p. 15: `Commit 𝑢𝑡= 𝜓𝑡′−1`
- p. 16: `can achieve when exact predictions of all future bandwidth are available at the start of the problem, i.e., cost(OPT) = 𝜄𝑁`
- p. 16: `uniform constants 𝐶> 0, 𝜌∈(0, 1) such that the following inequalities hold:`
- p. 16: `≤𝐶𝜌𝜏−𝑡+1  `
- p. 16: `≤𝐶𝜌𝜏−𝑡+1  `
- p. 16: `Assumption A.1. There exists uniform constants 𝜔max > 𝜔min > 0 such that for any time step 𝑡, we have that 𝜔min ≤𝜔𝑡≤𝜔max holds. We`
- p. 16: `also assume that 𝜔min/𝑟min ≥𝑥max, and 𝜔max/𝑟max −1 ≤−𝛿holds for a fixed constant 𝛿> 0.`
- p. 16: `1 + max{6𝜔min(𝜔min+3),4𝑥max(𝜔min+8𝛾)}`
- p. 16: `min + max{6𝜔min(𝜔min + 3), 4𝑥max(𝜔min + 8𝛾)}`
- p. 17: `𝑡)}𝑡=1,2,... denotes the offline optimal states`
- p. 17: `and control actions, and {(𝑥𝑡,𝑢𝑡)}𝑡=1,2,... denotes the buffer level achieved by SODA. The dashed trajectory from (𝑥𝑡,𝑢𝑡) denotes`
- p. 17: `≤𝐶′𝜌𝜏−𝑡+1  `
- p. 17: `≤𝐶′𝜌𝜏−𝑡+1  `
- p. 17: `𝐶′ = 𝐶(1 + 𝜌)𝑟min + 𝜌`
- p. 17: `Theorem A.3. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Define the weight 𝐶`
- p. 17: `ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾satisfies`
- p. 17: `𝐶1𝜌𝐾−1cost(OPT) = 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 + 𝐶1𝜌𝐾−1 = 1 + 𝑂(𝜌𝐾). Here, the coefficient 𝐶1 is given by`
- p. 18: `𝑡≤16𝜌4𝐾−2 `
- p. 18: `min)𝑏(𝑥∗`
- p. 18: `𝑡=1 and the offline optimal trajectory {(𝑥∗`
- p. 18: `𝑡=1, the aggregated contribution`
- p. 18: `𝑡=1 satisfies that`
- p. 18: `𝑡=1 denotes the offline optimal trajectory.`
- p. 18: `Lemma A.6. Suppose 𝜁≤min{¯𝑥,𝑥max −¯𝑥} is positive number and 𝑥0 ≤¯𝑥+ 𝜁, if the coefficient 𝛽for the buffer cost is sufficiently large such`
- p. 18: `𝑡∈[¯𝑥−𝜁, ¯𝑥+ 𝜁] holds for all time step 𝑡.`
- p. 19: `𝛽tends to +∞, the offline optimal will ignore the distortion/switching cost and select actions so that the buffer level always equal to ¯𝑥.`
- p. 19: `𝑒𝑡≤(𝐶+ 𝐶′)𝜌𝐾`
- p. 19: `Theorem A.8. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Let 𝐷B min{¯𝑥,𝑥max−`
- p. 19: `𝐸(𝑡, 𝐾) + 𝜌𝐾≤`
- p. 19: `where, recall, 𝐸(𝑡, 𝐾) = Í𝑡+𝐾`
- p. 19: `𝜏=𝑡+1 𝜌𝜏−𝑡−1`
- p. 19: `i.e., 0 < 𝑥𝑡< 𝑥max for 𝑡= 1, . . . , 𝑁. Further, SODA achieves a dynamic regret of`
- p. 19: `where E = 𝜌2𝐾𝑁+ Í𝐾`
- p. 19: `𝜅=1 𝜌𝜅𝐸𝜅. Here 𝐸𝜅B Í𝑁`
- p. 19: `E𝑁+ E), since cost(OPT) = 𝑂(𝑁). Intuitively, from the`
- p. 19: `we have that the following inequality holds for all 𝜏∈{𝑡,𝑡+ 1, . . . ,𝑡+ 𝐾−1}:`
- p. 19: `cost and the buffer cost are removed.) This can be viewed as the extreme case when 𝛾tends to +∞so that both 𝛼and 𝛽are negligible. In this`
- p. 20: `((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0) B arg min`
- p. 20: `s.t. 𝑥𝜏= 𝑥𝜏−1 + ˆ𝜔𝑢𝜏−1, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,`
- p. 20: `𝑥𝜏∈[0,𝑥max],𝑢𝜏∈`
- p. 20: `, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,`
- p. 20: `𝑥𝑡−1 = 𝜎𝑡−1,𝑢𝑡−1 = 𝜈𝑡−1.`
- p. 20: `((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0) is monotonically increasing; If 𝜈𝑡−1 = 1/ ˆ𝜔, the optimal solution is 𝑢𝑡= 𝑢𝑡+1 = · · · = 𝑢𝑡+𝐾−1 =`
- p. 20: `𝜈𝑡−1 = 1/ ˆ𝜔.`
- p. 20: `following: If we change the variable of (6) to 𝑎𝑡= 𝑢𝑡−𝑢𝑡−1, which denotes the increments of the control actions, the objective of (6) is a`
- p. 20: `𝜓(𝑦,𝑧; 𝜇,𝑤,𝛿) =`
- p. 20: `s.t. 𝑥𝑡∈[0,𝑥max] ⊆R, ∀0 ≤𝑡≤𝑝,`
- p. 20: `𝑥𝑡−𝑥𝑡−1 ≥−𝛿𝑡, ∀0 ≤𝑡≤𝑝+ 1,`
- p. 20: `𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧,`
- p. 20: `where 𝑦,𝑧∈[0,𝑥max]𝐻−1, 𝜇∈[0,𝑥max]𝑝+1,𝑤∈W𝑝+𝐻,𝛿∈Δ𝑝+2. Here, the objective function (7a) contains the hitting costs 𝑓𝑡(𝑥𝑡; 𝜇𝑡)`
- p. 20: `𝑢𝑡= (𝑥𝑡−𝑥𝑡−1 + 1)/𝜔𝑡,`
- p. 20: `where 𝜔𝑡denotes the bandwidth. The memory length 𝐻= 3. For the hitting cost, we have 𝜇𝑡≡¯𝑥, and`
- p. 20: `𝑓𝑡(𝑥; 𝜇𝑡) = 𝛽𝑏(𝑥) =`
- p. 20: `if 𝑥≤¯𝑥,`
- p. 20: `For the switching cost, we have 𝑤𝑡= (𝜔𝑡,𝜔𝑡−1) and`
- p. 20: `𝑐𝑡(𝑥𝑡:𝑡−2;𝑤𝑡) = 𝜔𝑡𝑢2`
- p. 20: `= (𝑥𝑡−𝑥𝑡−1 + 1)2`
- p. 20: `The first constraint 𝑥𝑡∈[0,𝑥max] of (7) matches the buffer constraint of the video streaming problem exactly.`
- p. 20: `The second constraint 𝑥𝑡−𝑥𝑡−1 ≥−𝛿𝑡corresponds to the constraint that 𝑢𝑡≥`
- p. 20: `we have 𝛿𝑡= 1 −𝜔𝑡`
- p. 20: `𝑟max . By Assumption A.1, we have 𝛿𝑡≥𝛿> 0.`
- p. 21: `1) 𝑓𝑡(·; 𝜇𝑡) : R →R is strongly convex for all𝑡and 𝜇𝑡∈[0,𝑥max]. We further assume there exists two𝑚𝑓-strongly convex and ℓ𝑓-smooth functions`
- p. 21: `(·; 𝜇𝑡) : R →R in C2 such that 𝑓𝑡(𝑥𝑡; 𝜇𝑡) = 𝑓(0)`
- p. 21: `(𝑥𝑡; 𝜇𝑡) for 𝑥𝑡∈[0, 𝜇𝑡] and 𝑓𝑡(𝑥𝑡) = 𝑓(1)`
- p. 21: `(𝑥𝑡; 𝜇𝑡) for 𝑥𝑡∈[𝜇𝑡,𝑥max]. We`
- p. 21: `also assume that for 𝑗= 1, 2, 𝑓(𝑗)`
- p. 21: `satisfies that for all 𝑥𝑡, 𝜇𝑡∈[0,𝑥max],`
- p. 21: `≤𝐿𝑓, and`
- p. 21: `∇𝜇𝑡∇𝑥𝑡𝑓(𝑗)`
- p. 21: `2) 𝑐𝑡(·;𝑤𝑡) : R𝐻→R is convex and ℓ𝑐-smooth for all 𝑡and 𝑤𝑡∈W ⊂R𝑞. 𝑐𝑡(·;𝑤𝑡) is in C2 on [0,𝑥max]𝐻. We also assume that for all`
- p. 21: `𝑤𝑡∈W and feasible 𝑥𝑡:𝑡−𝐻+1, we have`
- p. 21: `∇𝑥𝑡:𝑡−𝐻+1𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)`
- p. 21: `∇𝑤𝑡𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)`
- p. 21: `≤𝐿𝑐, and`
- p. 21: `∇𝑤𝑡∇𝑥𝑡:𝑡−𝐻+1𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)`
- p. 21: `3) We have 𝛿𝑡∈Δ holds for all 𝑡, where Δ is a closed interval on R and is bounded below by some positive constant 𝛿. Denote 𝑑B ⌈𝑥max/𝛿⌉.`
- p. 21: `In the special case of the video streaming problem, Assumption B.1 is satisfied with the parameters 𝑚𝑓= 𝜖𝛽, ℓ𝑓= ℓ𝜇= 𝛽, ℓ𝑐= 2(𝜔min+3)`
- p. 21: `ℓ𝑤= 4𝑥max(𝜔min+8𝛾)`
- p. 21: `Theorem B.1. Under Assumption B.1, if 𝑝≥𝑑, the inequality`
- p. 21: `holds for all 𝑡∈[0, 𝑝] and 𝑦,𝑧∈[𝑥,𝑥]𝐻−1. Here,`
- p. 21: `where ℓB max{𝐻ℓ𝑐, ℓ𝑤} and ¯ℓB max{𝐻ℓ𝑓, ℓ𝜇, ℓ}.`
- p. 21: `ℓ= max{3ℓ𝑐, ℓ𝑤} = max{6𝜔min(𝜔min + 3), 4𝑥max(𝜔min + 8𝛾)}`
- p. 21: `1 + max{6𝜔min(𝜔min+3),4𝑥max(𝜔min+8𝛾)}`
- p. 21: `min + max{6𝜔min(𝜔min + 3), 4𝑥max(𝜔min + 8𝛾)}`
- p. 21: `Discussion about different distortion costs. Note that Assumption B.1 still holds if we replace the distortion cost function 𝑣(𝑟) = 1`
- p. 21: `𝑣(𝑟) = log(𝑟max/𝑟). This is because the new switching cost`
- p. 21: `𝑡(𝑥𝑡:𝑡−2;𝑤𝑡) = 𝜔𝑡𝑢𝑡log(𝑟max𝑢𝑡) + 𝛾(𝑢𝑡−𝑢𝑡−1)2`
- p. 21: `= (𝑥𝑡−𝑥𝑡−1 + 1) log`
- p. 21: `also satisfies Assumption B.1 for any 𝑤𝑡= (𝜔𝑡,𝜔𝑡−1) ∈[𝜔min,𝜔max]2 and feasible 𝑥𝑡:𝑡−2.`
- p. 22: `To show Theorem B.1, we first need to define indicators of active constraints, denoted as 𝜉∈{0, 1}4𝑝+5. Specifically, given the unique optimal`
- p. 22: `solution 𝑥0:𝑝= 𝜓(𝑦,𝑧; 𝜇,𝑤,𝛿) under a tuple of parameters (𝑦,𝑧; 𝜇,𝑤,𝛿), we consider whether the following equality conditions hold:`
- p. 22: `𝜉1,𝑡= 1{𝑥𝑡= 0}, ∀0 ≤𝑡≤𝑝;`
- p. 22: `𝜉2,𝑡= 1{𝑥𝑡= 𝑥max}, ∀0 ≤𝑡≤𝑝;`
- p. 22: `𝜉3,𝑡= 1{𝑥𝑡= 𝜇𝑡}, ∀0 ≤𝑡≤𝑝;`
- p. 22: `𝜉4,𝑡= 1{𝑥𝑡−𝑥𝑡−1 = −𝛿𝑡}, ∀0 ≤𝑡≤𝑝+ 1.`
- p. 22: `And we define indicators of the sides (denoted as 𝜎∈{0, 1}𝑝+1) as the following:`
- p. 22: `𝜎𝑡= 1{𝑥𝑡∈[𝜇𝑡,𝑥max]}, ∀0 ≤𝑡≤𝑝.`
- p. 22: `To simplify the notation, we let 𝜃B (𝜇,𝑤,𝛿) ∈Θ B [0,𝑥max]𝑝+1 × W𝑝+𝐻× Δ𝑝+2. While 𝜓(𝑦,𝑧;𝜃) can decide a unique pair of (𝜉, 𝜎), we`
- p. 22: `ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) =`
- p. 22: `s.t. 𝑥𝑡=`
- p. 22: `if 𝜉1,𝑡= 1`
- p. 22: `if 𝜉2,𝑡= 1`
- p. 22: `if 𝜉3,𝑡= 1`
- p. 22: `, ∀0 ≤𝑡≤𝑝,`
- p. 22: `𝑥𝑡−𝑥𝑡−1 = −𝛿𝑡, if 𝜉4,𝑡= 1, ∀0 ≤𝑡≤𝑝+ 1,`
- p. 22: `𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧.`
- p. 22: `Lemma B.2. Suppose Assumption B.1 holds and 𝑝≥𝑑. For 𝑦,𝑧∈[0,𝑥max]𝐻−1 and 𝜃∈Θ, let 𝜉, 𝜎be the corresponding indicators of active`
- p. 22: `𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) and 𝜄(𝑦,𝑧;𝜃) = ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎).`
- p. 22: `𝜄(𝑦,𝑧;𝜃) ≥ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎)`
- p. 22: `because the optimization problem on the RHS has less constraints. If the inequality holds with equality, we must have𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎)`
- p. 22: `Consider the convex combination 𝜁(𝜂) for 𝜂∈[0, 1] defined as`
- p. 22: `𝜁(𝜂) = (1 −𝜂)𝜓(𝑦,𝑧;𝜃) + 𝜂ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) .`
- p. 22: `Note that 𝜁(𝜂) satisfies all the active constraints and sides as specified by (𝜉, 𝜎) because they are active for all 𝜂∈[0, 1]. Since the constraints`
- p. 22: `of (7) that are not in (𝜉, 𝜎) are inactive at 𝜂= 0, there must exist 𝜂> 0 such that 𝜁(𝜂) is also feasible for (7). 𝜁(𝜂) achieves a strictly smaller`
- p. 22: `objective than 𝜁(0) = 𝜓(𝑦,𝑧;𝜃), which leads to a contradiction.`
- p. 22: `Lemma B.2 establishes that given any feasible tuple of (𝑦,𝑧;𝜃), one can find at least one pair of (𝜉, 𝜎) such that 𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎),`
- p. 22: `while there can be other (𝜉′, 𝜎′) that satisfies 𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉′, 𝜎′).`
- p. 22: `Lemma B.3. Suppose Assumption B.1 holds and 𝑝≥𝑑. If both ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) and ˆ𝜓(𝑦′,𝑧′;𝜃′; 𝜉, 𝜎) exist for 𝑦,𝑧,𝑦′,𝑧′ ∈[0,𝑥max]𝐻−1 and`
- p. 23: `Here, ℓB max{𝐻ℓ𝑐, ℓ𝑤} and ¯ℓB max{𝐻ℓ𝑓, ℓ𝜇, ℓ}.`
- p. 23: `elimination, we get an unconstrained optimization problem with the free variables 𝑥𝑡0,𝑥𝑡1, . . . ,𝑥𝑡𝑞where the indices satisfy 0 ≤𝑡0 < 𝑡1 <`
- p. 23: `. . . < 𝑡𝑞≤𝑝. To simplify the notation, we let 𝑡−1 = −1 and 𝑡𝑞+1 = 𝑝+ 1. For 𝜏that satisfies 𝑡𝑖< 𝜏< 𝑡𝑖+1, we have either 𝑥𝜏= 𝑥𝑡𝑖−Í𝜏`
- p. 23: `𝛾=𝑡𝑖+1 𝛿𝛾`
- p. 23: `or 𝑥𝜏is some constant. Without loss of generality, we can assume 𝑡𝑖+1 ≤𝑡𝑖+ 𝑑+ 𝐻, because otherwise we can find 𝜏∈(𝑡𝑖,𝑡𝑖+1 −𝐻] such`
- p. 23: `𝜏= 0, . . . ,𝑞. We can decompose ˆℎas`
- p. 23: `ˆℎ( ˆ𝑥0:𝑞;𝜁) = ˆℎ𝑎( ˆ𝑥0:𝑞; 𝜇) + ˆℎ𝑏( ˆ𝑥0:𝑞;𝜁),`
- p. 23: `where 𝜁= (𝑦,𝑧,𝜃), ˆℎ𝑎is the sum of the original hitting costs minus 𝑚𝑓`
- p. 23: `ˆ𝑥0:𝑞ˆℎ𝑎( ˆ𝑥0:𝑞; 𝜇) ⪰0, (𝑚𝑓+ 𝐻ℓ𝑐)𝐼⪰∇2`
- p. 23: `We also note that ∇2`
- p. 23: `ˆℎ𝑎( ˆ𝑥0:𝑞; 𝜇) is a diagonal matrix and ∇2`
- p. 23: `where 𝜙(𝑖) denotes the integer 𝑗that satisfies 𝑡𝑗≤𝑖< 𝑡𝑗+1 and`
- p. 23: `Here, ℓB max{𝐻ℓ𝑐, ℓ𝑤} and ¯ℓB max{𝐻ℓ𝑓, ℓ𝜇, ℓ}. For completeness, we give the detailed proof below: Let 𝑒be a vector such that both 𝜁and`
- p. 23: `∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒) = 0.`
- p. 23: `𝑑𝜂𝜓(𝜁+ 𝜂𝑒) = −∇𝑦∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝑦−∇𝑧∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝑧`
- p. 23: `∇𝜇𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝜇𝑡−`
- p. 23: `∇𝑤𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝑤𝑡`
- p. 23: `∇𝛿𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝛿𝑡.`
- p. 24: `𝑅(𝑦) B −∇𝑦∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × (𝐻−1) matrix,`
- p. 24: `𝑅(𝑧) B −∇𝑧∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × (𝐻−1) matrix,`
- p. 24: `𝑅(𝜇𝑡) B −∇𝜇𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × 1 matrix,`
- p. 24: `𝑅(𝑤𝑡) B −∇𝑤𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × 𝑑matrix,`
- p. 24: `𝑅(𝛿𝑡) B −∇𝛿𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × 1 matrix.`
- p. 24: `𝑑𝜃𝜓(𝜁+ 𝜂𝑒) = 𝑀−1 ©­`
- p. 24: `𝑑𝜂𝜓(𝜁+ 𝜂𝑒)𝜏= (𝑀−1)𝜏,0:𝐻−2𝑅(𝑦)`
- p. 24: `Recall that ¯ℓB max{𝐻ℓ𝑐, 𝐻ℓ𝑓, ℓ𝜇, ℓ𝑤}. We know that the norms of`
- p. 24: `Note that 𝑀can be decomposed as 𝑀= 𝑀𝑎+ 𝑀𝑏, where`
- p. 24: `where 𝜌0 := (`
- p. 24: `𝑐𝑜𝑛𝑑(𝑀𝑏) + 1) = 1 −2 ·`
- p. 25: `This finishes the proof of (12). Recall that we have 𝑡𝑖< 𝑡𝑖+1 ≤𝑡𝑖+ 𝑑+ 𝐻. Therefore, (12) implies (10).`
- p. 25: `Lemma B.4. Suppose Assumption B.1 holds and 𝑝≥𝑑. For a pair of (𝜉, 𝜎), if any tuple in the sequence {(𝑦𝑞,𝑧𝑞;𝜃𝑞)}∞`
- p. 25: `𝑞=1 satisfies𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞) =`
- p. 25: `ˆ𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) and lim𝑞→∞(𝑦𝑞,𝑧𝑞,𝜃𝑞) = (𝑦,𝑧,𝜃), then we have`
- p. 25: `𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎).`
- p. 25: `𝑞→∞𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞) = lim`
- p. 25: `ˆ𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎).`
- p. 25: `Since lim𝑞→∞(𝑦𝑞,𝑧𝑞;𝜃𝑞) = (𝑦,𝑧;𝜃), for an arbitrary small positive real number 𝜖, we can find a positive integer 𝑞such that`
- p. 25: `where 𝑑𝑖𝑠𝑡(𝜃,𝜃′) = Í𝑝`
- p. 25: `0:𝑝= 𝑥0:𝑝,𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧.`
- p. 25: `For 𝑡= 0, 1, . . ., if 𝑥′`
- p. 25: `. Then, for 𝑡= 𝑝, 𝑝−1, . . ., if 𝑥′`
- p. 25: `≤(2𝑑+ 1)𝜖.`
- p. 25: `𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞) −𝜄(𝑦,𝑧;𝜃) ≤𝑐0`
- p. 25: `+ 𝜖 ≤(2𝑑+ 2)𝑐0𝜖.`
- p. 25: `ˆ𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) −𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞) ≥−`
- p. 25: `leads to a contradiction with the assumption that ˆ𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) =`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 11 - score 4:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia 6.2.2 Baseline ABR Controllers. In response to the growing interest in learning-based throughput predictors and ABR controllers in the research community, we included two representative learning- based ABR controllers for local deployment on top of the major baseline ABR controllers from numerical simulations: • Fugu [46]: Developed as part of the Puffer project, it features a learning-based stochastic throughput predictor, while its under- lying control algorithm is similar to MPC. • CausalSimRL [60]: A modern implementation of a reinforcement learning (RL)-based ABR controller Pensieve [22].

**Fragmento 2 - p. 2 - score 3:**

We make the following specific contributions: 1) Theoretical Foundations of ABR Controller Design. SODA is the first ABR controller to provably optimize all three key components of QoE, namely, video quality, rebuffering and bi- trate switching. Unlike prior work such as BOLA [36, 44] that use Lyapunov methods to optimize the first two components, we use a new framework based on recent advances in smoothed online convex optimization (SOCO) [13, 25, 26, 33–35, 43] to simultaneously optimize all three QoE components. To enable the application of SOCO, we model the rebuffering minimiza- tion requirement in a novel fashion using the notion of buffer stability. We prove that SODA is near-optimal and achieves QoE within a small factor of the offline optimal QoE (Theorem 4.1).

**Fragmento 3 - p. 4 - score 3:**

• To remain computationally efficient, SODA leverages an efficient approximate solver (see Section A.5 for proof and Algorithm 1 for implementation), that only requires evaluation of monotonic bitrate sequences (Section 4.3), which reduces the computational cost by two orders of magnitude over a brute-force solver. 3 SODA OVERVIEW Given the design gaps, opportunities, and requirements, we set out to design a theoretically sound adaptive bitrate streaming (ABR) controller that minimizes bitrate switching without compromis- ing video quality or increasing rebuffering time, thus providing a smooth viewing experience. To accomplish this, we deviate from the conventional segment-based ABR formulation and derive theo- retical insights from a time-based ABR formulation.

**Fragmento 4 - p. 6 - score 3:**

The formal definition of exponentially decaying perturbation generalizes the intuition above to consider the impact of perturbing any parameters on the entire optimal trajectory (see Definition A.1 in Appendix A). Two metrics that we use to measure SODA’s performance theoret- ically are dynamic regret and competitive ratio, which are standard in the literature of online optimization [25, 28, 33, 49, 54]. Specif- ically, let cost(ALG) denote the total cost incurred by an online algorithm ALG and cost(OPT) denote the offline optimal cost (Equa- tion 1) an agent can incur if it has exact knowledge of all future bandwidth at the beginning. We say ALG achieves a dynamic regret of 𝑅if cost(ALG) −cost(OPT) ≤𝑅always holds, and ALG achieves a competitive ratio of 𝐶if cost(ALG) ≤𝐶· cost(OPT) always holds.

**Fragmento 5 - p. 7 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia minimum possible time. A critical observation underlying the im- plementation of SODA is that it is sufficient to search only for bitrate sequences that are increasing or decreasing monotonically. We provide a theoretical justification in the following theorem. Theorem 4.3. [Informal] Suppose SODA is given the predictions that satisfy ˆ𝜔𝑛|𝑛−1 = · · · = ˆ𝜔𝑛+𝐾−1|𝑛−1 at an intermediate time step 𝑛. Then, the bitrate trajectory solved by SODA can be approximated by a feasible monotonic bitrate trajectory with an error of 𝑂 𝐾/√𝛾. The formal statement of Theorem 4.3 is given in Theorem A.9 in Appendix A.

**Fragmento 6 - p. 12 - score 3:**

SOCO’s switching cost model inspires our design of SODA for video streaming. Our mathematical formulation of adaptive video streaming can be viewed as a specific example of online (optimal) control [54]. Similar to online optimization, online control seeks to design a controller to minimize the total cost incurred over a finite horizon. The theoretical bounds in this paper are most related to works that study how future predictions can improve online controller perfor- mance [39, 47, 49, 52]. Our proofs follow an analytic framework for studying MPC-based algorithms via exponentially decaying pertur- bation bounds [49, 55, 56]. Our work shows that this decay property holds under our model of adaptive video streaming, allowing us to establish performance guarantees for SODA.

**Fragmento 7 - p. 12 - score 3:**

A related work [11] built predictive models for user engagement based on QoE metrics. Our work leverages insights from these works in our ABR controller design. 7.3 Smoothed Online Convex Optimization Our algorithm builds on recent developments in smoothed online convex optimization (SOCO), a variant of online optimization that penalizes switching between consecutive decisions via a “switch- ing cost.” [25, 33, 34]. In recent years, the design and analysis of algorithms for SOCO has received considerable attention, e.g., [14, 25, 31, 32, 34, 37], with optimal online algorithms emerging in vari- ous settings [33, 42, 48, 62] and a variety of applications receiving attention [10, 12, 26, 43, 53, 55, 57].

**Fragmento 8 - p. 15 - score 3:**

Since we will use the indicator terminal cost frequently, we introduce the shorthand ˜𝜓𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1), which denotes ˜𝜓𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; I𝜎𝑡+𝑝,𝜈𝑡+𝑝+1  . We use 𝜄𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 𝐹 to de- note the optimal objective value of the optimization problem (3). The model of SODA that we consider in the theoretical analysis is summarized in Algorithm 2. The major difference from the SODA algorithm discussed in Section 3.3 is that we include the indicator terminal cost (in line 5) so that the last two states in the predictive trajectory are equal to the target buffer level. This terminal constraint is important for our competitive ratio result in Theorem 4.1, for which we need to bound the squared distance between the trajectories of SODA and the offline optimal controller by a part of the offline optimal cost.

**Fragmento 9 - p. 15 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Appendices are supporting material that has not been peer-reviewed. A PROOF OUTLINE In this section, we present an outline of our theoretical analysis for SODA. As we discussed in Section 4, our proof is based on an exponentially decaying perturbation bound that relates the behavior of the solution to the optimization problem defining SODA as a function of problem parameters. This section is organized as follows: We first introduce the modeling of SODA that we use to establish theoretical results in Section A.1. Then, we introduce the exponentially decaying perturbation bound, its implications, and the proof idea in Section A.2.

**Fragmento 10 - p. 17 - score 3:**

 , where the decay factor 𝜌is the same as Theorem A.1, and the constant 𝐶′ is given by 𝐶′ = 𝐶(1 + 𝜌)𝑟min + 𝜌 𝜔min𝑟min𝜌 . Here, 𝐶is the same as Theorem A.1. To establish the exponentially decaying perturbation property, we first reduce the video streaming problem to a more general online optimization problem with memory and inequality constraints. Then, we consider each possible combination of active inequality constraints separately and show that the exponentially decaying perturbation property holds in each case. This only requires considering optimization problems with equality constraints with second-order differentiable objectives. Lastly, we show that the exponential decay properties for these separate cases can be combined to establish the exponential decay property for the original video streaming problem. A.3 Proof Outline for Exact Predictions We provide the formal version of Theorem 4.1 that gives the dynamic regret and competitive ratio for SODA with specific coefficients in Theorem A.3. Theorem A.3. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Define the weight 𝐶 and the decay factor 𝜌to be the same as Theorem A.1, and the coefficient 𝐶′ is given by Corollary A.2. Suppose all predictions are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾satisfies 𝐾≥1 4 ln  16 1 −𝜌·  1 + (𝐶+ 𝐶′)2 1 −𝜌  ·  𝐶2 + (𝐶′)22 /ln  1 𝜌  = 𝑂(1). Here, the coefficients 𝐶,𝐶′ and the decay factor 𝜌are given by Theorem A.1 and Corollary A.2. Then, SODA achieves a dynamic regret of 𝐶1𝜌𝐾−1cost(OPT) = 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 + 𝐶1𝜌𝐾−1 = 1 + 𝑂(𝜌𝐾). Here, the coefficient 𝐶1 is given by 𝐶1 = 8

**Fragmento 11 - p. 19 - score 3:**

𝑟min , where 𝐸(𝑡−1, 𝐾) B Í𝑡+𝐾−1 𝜏=𝑡 𝜌𝜏−𝑡 ˆ𝜔𝜏|𝑡−1 −𝜔𝜏 . Similar to the proof outline for the exact prediction case in Section A.3, we can apply Lemma A.5 to bound the accumulation of past errors. With the help of Lemma A.6 and Lemma A.7, we show our main result for SODA when the predictions of the future bandwidths are inexact in Theorem A.8. We defer the proof of Theorem A.8 to Section D.3. Theorem A.8. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Let 𝐷B min{¯𝑥,𝑥max− ¯𝑥}. Suppose the weight 𝛽, the prediction horizon 𝐾, and the prediction errors satisfy that 𝛽≥ 3 𝜖𝐷·  1 + 4𝛾 𝜔min  ·  1 𝑟min − 1 𝑟max  , and 𝐸(𝑡, 𝐾) + 𝜌𝐾≤ (1 −𝜌)𝐷 3𝐶(1 + 𝐶+ 𝐶′)  1 + 𝑥max + 1 𝑟min − 1 𝑟max  , where, recall, 𝐸(𝑡, 𝐾) = Í𝑡+𝐾 𝜏=𝑡+1 𝜌𝜏−𝑡−1 ˆ𝜔𝜏|𝑡−𝜔𝜏 . Then, the buffer levels in the SODA’s decision trajectory never hits the constraint boundary, i.e., 0 < 𝑥𝑡< 𝑥max for 𝑡= 1, . . . , 𝑁. Further, SODA achieves a dynamic regret of 2  1 + 1 𝑟min + 𝐶+ 𝐶′2  1 + 𝑥max + 1 𝑟min − 1 𝑟max  (1 −𝜌)3/2 · √︁ 4𝛾+ 𝛽+ 𝜔max · √︁ E · cost(OPT)+  1 + 1 𝑟min + 𝐶+ 𝐶′4  1 + 𝑥max + 1 𝑟min − 1 𝑟max 2 (4𝛾+ 𝛽+ 𝜔max) (1 −𝜌)3 · E, where E = 𝜌2𝐾𝑁+ Í𝐾 𝜅=1 𝜌𝜅𝐸𝜅. Here 𝐸𝜅B Í𝑁 𝑡=1 ˆ𝜔𝑡+𝜅|𝑡−𝜔𝑡+𝜅 2. Note that the dynamic regret bound shown in Theorem A.8 is in the order of 𝑂( √ E𝑁+ E), since cost(OPT) = 𝑂(𝑁). Intuitively, from the form of 𝐸𝑡(𝐾), we see that predicting the future bandwidth 𝜔𝜏accurately at time step 𝑡becomes less important as (𝜏−𝑡) increases. A.5 Proof Outline for Efficient Structure In this section, we show that optimal solution of the finite-time optimal control problem solved by SODA can be approximated well by a monotonic sequence of bitrates when the coefficient 𝛾of the switching cost is sufficiently large (see Theorem A.9). Although this result is shown for the continuous variable case, it also provides some insight as to why the efficient approximate solver in Algorithm 1 can provide identical decisions to the brute-force solver with relatively high probabilities, as shown in Figure 8. Theorem A.9. Let ˆ𝜔×𝐾denote the sequence { ˆ𝜔, . . . , ˆ𝜔} with length 𝐾. For any 𝜆> 0, when the coefficient 𝛾is sufficiently large such that 𝛾≥𝐾2 𝜆2

**Fragmento 12 - p. 1 - score 2:**

To demonstrate its real-world practicality, we deployed SODA on a wide range of devices within the production network of Amazon Prime Video. Production experiments show that SODA reduced bitrate switching by up to 88.8% and increased average stream viewing duration by up to 5.91% compared to a fine-tuned production baseline. CCS CONCEPTS • Information systems →Multimedia streaming; • Theory of computation →Online algorithms; Theory and algorithms for application domains. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.

**Fragmento 13 - p. 3 - score 2:**

Past works have shown that RobustMPC incurs 26% more rebuffering events unless paired with a sophisticated throughput predictor [46, 50]. Simi- larly, learning-based controllers like Pensieve tend to degrade in performance when trained for realistic network conditions encountered in the wild [24]. In practice, accurate throughput predictions are hard because of several factors, including (i) de- vice and OS level inefficiencies [18], (ii) stop-start nature of video requests which do not interact well with TCP [8, 18], and (iii) volatile network conditions typical in production networks [1, 5, 45]. To make matters worse, sophisticated throughput predictors are themselves not necessarily accurate [16] and are challenging to deploy due to device level bottlenecks [58].

**Fragmento 14 - p. 3 - score 2:**

streaming, a longer buffer of 120 seconds ensures that bitrate jumps are spaced well apart (up to 20 seconds), however, for live streaming with a buffer of 20 seconds, bitrates fluctuate with small deviations of 1 - 3 seconds in the buffer size. This can cause bitrates to switch frequently. While controllers such as MPC [17] and Pensieve [22] offer respite by explicitly penalizing bitrate switching, these con- trollers suffer from shortcomings of their own: • Model predictive controllers are hard to deploy at scale because they need to solve a non-linear integer programming problem over a prediction horizon of 𝐾segments, e.g., 𝐾= 5, which is so computationally expensive that it is quicker to download a video segment than to obtain a bitrate decision [17, 19].

**Fragmento 15 - p. 3 - score 2:**

Therefore, in-the- wild performance of these controllers remains questionable. Opportunities. Outside of the video streaming literature, the interaction of learning and control has blossomed in recent years, leading to new and exciting approaches to controller designs [39, 47, 49, 52, 54]. However, these new approaches have not yet been applied and evaluated in the context of video streaming where classical model predictive and proportional–integral–derivative control have remained the focus, e.g., [17, 23]. In particular, the area of smoothed online convex optimization (SOCO) has seen multiple breakthroughs in recent years [13, 25, 33, 35], including the development of connections to model predictive controllers [26, 47, 49, 52, 56].

**Fragmento 16 - p. 3 - score 2:**

SOCO provides a systematic framework to balance an objective function with action switching. It thus lends itself well to video streaming, which needs to jointly optimize video quality, sustained playback, and bitrate smoothness. Requirements. Driven by the above design gaps and oppor- tunities, we identify three requirements that SODA should deliver. In particular, SODA should (i) achieve bitrate smoothness without 615

**Fragmento 17 - p. 4 - score 2:**

Let 𝜔𝑛denote the average throughput during the 𝑛th time inter- val, 𝑟𝑛the selected bitrate for that time interval, and 𝑥𝑛the buffer level immediately after that time interval. Our objective is to min- imize the overall cost given as a linear combination of the three QoE components: 𝑁 ∑︁ 𝑛=1  𝑣(𝑟𝑛) · 𝜔𝑛Δ𝑡 𝑟𝑛 + 𝛽· 𝑏(𝑥𝑛) + 𝛾· 𝑐(𝑟𝑛,𝑟𝑛−1)  , (1) where • 𝑣(𝑟𝑛) is the distortion cost, which should be a positive, strictly decreasing, and convex function that models the encoding distor- tion, e.g., 𝑣(𝑟𝑛) = 1/𝑟𝑛. It is then weighted by the amount of video downloaded during that time interval, i.e., 𝜔𝑛Δ𝑡/𝑟𝑛because the controller downloads a variable amount of video during each fixed time interval. Figure 4: A sample throughput function used to illustrate why our time-based formulation is better for analysis.

**Fragmento 18 - p. 4 - score 2:**

• 𝑏(𝑥𝑛) is the buffer cost, which aims to stabilize the buffer level around a target level ¯𝑥, i.e., 𝑏(𝑥𝑛) = ( ( ¯𝑥−𝑥𝑛)2 𝑥𝑛≤¯𝑥 𝜖(𝑥𝑛−¯𝑥)2 𝑥𝑛> ¯𝑥, where 𝜖< 1 is a small constant. Note that we purposely do not model the rebuffering time explicitly to avoid the pitfalls encoun- tered by RobustMPC (Section 2) and as we show later, this helps SODA achieve theoretical performance guarantees (Section 4.2). • 𝑐(𝑟𝑛,𝑟𝑛−1) is the switching cost from the previous bitrate to the current bitrate, e.g., 𝑐(𝑟𝑛,𝑟𝑛−1) = (𝑣(𝑟𝑛) −𝑣(𝑟𝑛−1))2. Coefficients 𝛽and 𝛾are positive weights for the buffer and the switching cost respectively based on user preferences. The choices for the distortion and switching cost functions are flexible.

**Fragmento 19 - p. 5 - score 2:**

It is always assumed that the validity of the throughput prediction is 𝐾Δ𝑡, a fixed value. In gen- eral, a throughput predictor may output a different value for each of the next 𝐾time intervals, i.e., ˆ𝜔𝑛|𝑛−1, ˆ𝜔𝑛+1|𝑛−1, . . . , ˆ𝜔𝑛+𝐾−1|𝑛−1, where ˆ𝜔𝑚|𝑛−1 (𝑚≥𝑛) is the throughput prediction for the 𝑚th time interval given previous download information up until the (𝑛−1)th time interval. In other words, a throughput predictor can output a piecewise constant throughput function for the next 𝐾Δ𝑡 time. In practice, though, a typical throughput predictor outputs a single value that corresponds to a constant throughput function. 3.3 Control Mechanism Inspired by the model predictive control framework, SODA selects a bitrate for each time interval by optimizing over the next 𝐾time intervals and then committing to the bitrate decision for the imme- diate next time interval, i.e., minimizing 𝑛+𝐾−1 ∑︁ 𝑚=𝑛  𝑣(𝑟𝑚) · ˆ𝜔𝑚|𝑛−1Δ𝑡 𝑟𝑚 + 𝛽· 𝑏(𝑥𝑚) + 𝛾· 𝑐(𝑟𝑚,𝑟𝑚−1)  (2a) Figure 5: SODA’s bitrate decision as a function of buffer level and predicted throughput.

**Fragmento 20 - p. 5 - score 2:**

We first analyze these questions theoretically (Section 4) and then present a practical implementation of SODA that answers these concerns (Section 5). 4 THEORETICAL DESIGN INSIGHTS Our design of SODA is motivated by recent theoretical advances at the interface of learning and control [28, 38, 49, 54] and smoothed online convex optimization [25, 33, 55]. In particular, we design SODA to satisfy an exponentially decaying perturbation property that has been shown to ensure efficient and robust use of predictions in model predictive control policies [49, 56]. Intuitively, this property describes the behavior of the solution to the optimization problem defining SODA (Equation 2) as a function of problem parameters, including bandwidth predictions { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾and the previ- ous buffer level/action pair (𝑥𝑛−1,𝑢𝑛−1).

**Fragmento 21 - p. 6 - score 2:**

Fortunately, the exponential decay property that ensures good performance with only a few predictions. More formally, we present a theorem showing that a small prediction horizon is sufficient for SODA to achieve near-optimal performance when the predictions within this window are accurate (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1). Theorem 4.1. [Informal] When the predictions of the bandwidth in future 𝐾steps are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾≥𝑂(1), SODA achieves a dynamic regret of 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 +𝑂(𝜌𝐾), where 𝜌< 1 is the decay factor of the exponentially decaying perturbation property. The formal statement of Theorem 4.1 is given in Theorem A.3 in Appendix A.

**Fragmento 22 - p. 6 - score 2:**

This result implies that SODA’s performance ap- proaches that of the optimal sequence of decisions exponentially fast in the prediction horizon size 𝐾; thus, only a small prediction horizon length is necessary to obtain good performance. 4.2 Inexact Predictions We now relax the exact prediction assumption to prove SODA’s robustness to a certain level of prediction errors thanks to its expo- nentially decaying perturbation property. Theorem 4.2. [Informal] Suppose the prediction error at each step is bounded above. The buffer level of SODA will never hit the constraint boundary, i.e., 0 < 𝑥𝑛< 𝑥max. Further, define E = 𝜌2𝐾𝑁+ Í𝐾 𝜅=1 𝜌𝜅𝐸𝜅, where 𝐸𝜅is the total squared error for predicting 𝜅steps into the future.

**Fragmento 23 - p. 7 - score 2:**

Given the diverse network conditions in the wild, we prefer simple throughput predictors which makes SODA highly deployable since there is no dependence on complex throughput predictors. In practice, we observe that prediction accuracy degrades as the prediction horizon increases (see Figure 7). Therefore, we limit the prediction horizon length to at most 10 s. This is also supported by our finding in Section 4.1 that a longer prediction horizon yields diminishing returns. 5.3 Efficient Approximate Solver At SODA’s core is the predictive optimization problem described in Section 3.3. Unfortunately, solving this problem on the fly is computationally challenging. One may propose enumerating all combinations of discretized throughputs, buffer levels, and previous bitrates in the form of an offline computed lookup table, as is the Figure 7: We profiled the performance of the two throughput predictors shipped with dash.js [64], i.e., moving average predictor and exponential moving average predictor.

**Fragmento 24 - p. 7 - score 2:**

Both predictors have a high mean correlation (around 50%) in the immediate future but a very low mean correlation (around 15%) in the far future. Algorithm 1: SODA’s efficient approximate optimization solver. SearchDown is omitted for brevity due to symmetry. The current buffer level and the previous bitrate are denoted by 𝑥0 and 𝑟0 respectively. function Search( ˆ𝜔,𝑥0,𝑟0, 𝐾) (𝑟∗up, obj∗up) ←SearchUp( ˆ𝜔,𝑥0,𝑟0, 𝐾) (𝑟∗ down, obj∗ down) ←SearchDown( ˆ𝜔,𝑥0,𝑟0, 𝐾) return 𝑟∗up ≠null ∧obj∗up < obj∗ down ? 𝑟∗up : 𝑟∗ down function SearchUp( ˆ𝜔,𝑥0,𝑟0, 𝐾) 𝑟∗ 1 ←null, obj∗←∞ foreach 𝑟1 ∈{𝑟∈R : 𝑟> 𝑟0} 𝑥1 ←𝑥0 + ˆ𝜔Δ𝑡/𝑟1 −Δ𝑡 if 𝑥1 < 0 then continue obj ←𝑣(𝑟1) · ˆ𝜔Δ𝑡/𝑟1 + 𝛽· 𝑏(𝑥1) + 𝛾· 𝑐(𝑟1,𝑟0) if 𝐾> 1 then (𝑟∗ 2, Δobj∗) ←SearchUp( ˆ𝜔,𝑥1,𝑟1, 𝐾−1) if 𝑟∗ 2 = null then continue obj ←obj + Δobj∗ if obj < obj∗then 𝑟∗ 1 ←𝑟1, obj∗←obj return (𝑟∗ 1, obj∗) case in FastMPC [17], however, this is neither flexible nor scalable in practice.

**Fragmento 25 - p. 8 - score 2:**

Empirical results are shown in Figure 8 to validate the near- optimality of bitrate decisions produced by the approximate solver. For each algorithm configuration, we uniformly sample a million situations with different throughputs, buffer levels, and previous bitrates. Then, we count the probability that the bitrate decision produced by the approximate solver is different from that produced by the brute-force solver. The difference is negligible for a reason- able switching cost weight, e.g., below 5% for 𝐾= 4 and a relative switching cost weight of 2. Throughout the evaluation sections, we use this efficient implementation of SODA. 6 EVALUATION To thoroughly evaluate SODA’s performance, we conducted three levels of empirical evaluation: (i) large-scale numerical simulations, (ii) prototype evaluation in Puffer [46], and (iii) production deploy- ment in Amazon Prime Video.

**Fragmento 26 - p. 9 - score 2:**

Additionally, it has low-buffer safety heuristic to reduce rebuffering and a switching avoidance heuristic to mitigate bitrate switching. It is the default ABR con- troller in dash.js. • MPC [17]: One application of model predictive control to adap- tive streaming that models utility, rebuffering time, and bitrate switching, without theoretical guarantees. 6.1.3 QoE Performance. The aggregate statistics for QoE scores and individual QoE components under each network dataset are shown in Figure 10. To better understand how the performance of different ABR controllers react to the intrinsic volatility of network conditions, we split the Puffer dataset into four quarters according to the relative standard deviation of throughput (Q1 represents the most stable network conditions, while Q4 represents the most volatile network conditions).


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 3 - score 5:**

Past works have shown that RobustMPC incurs 26% more rebuffering events unless paired with a sophisticated throughput predictor [46, 50]. Simi- larly, learning-based controllers like Pensieve tend to degrade in performance when trained for realistic network conditions encountered in the wild [24]. In practice, accurate throughput predictions are hard because of several factors, including (i) de- vice and OS level inefficiencies [18], (ii) stop-start nature of video requests which do not interact well with TCP [8, 18], and (iii) volatile network conditions typical in production networks [1, 5, 45]. To make matters worse, sophisticated throughput predictors are themselves not necessarily accurate [16] and are challenging to deploy due to device level bottlenecks [58].

**Fragmento 2 - p. 3 - score 5:**

Notice that beyond 70 seconds, RobustMPC re- peatedly rebuffers but continues to download the highest bitrate (Figure 3 bottom plot), resulting in 29 rebuffering events over 200 seconds. Strikingly, this behavior is in fact the optimal behavior under RobustMPC’s objective function which tolerates rebuffering to prevent bitrate switches. On the surface, this suggests higher rebuffering penalty in the objective function, however, higher penalties only reduce the duration of these tolerable rebuffers but do not eliminate them. Indeed, past work has empirically shown that even a 20× buffering penalty has marginal impact [24]. • Variance in network conditions or throughput prediction errors are not well tolerated by existing controllers.

**Fragmento 3 - p. 4 - score 5:**

This enables us to incorporate throughput predictions into the controller in a prin- cipled way. Taking advantage of recent advancements in smoothed online convex optimization (SOCO), we can theoretically prove that SODA offers a near-optimal quality of experience (QoE) and is robust against throughput prediction errors. 3.1 A Time-Based ABR Formulation Our time-based ABR formulation treats a video stream as a contin- uous flow rather than a discrete sequence of segments. Consider a streaming session that consists of 𝑁time intervals with fixed dura- tion Δ𝑡in terms of clock time (not video time). The controller’s task is to select a bitrate for each time interval from a set of available bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high quality, short rebuffering, and infrequent bitrate switching.

**Fragmento 4 - p. 16 - score 5:**

 . (5) Intuitively, the exponential decay property (Definition A.1) holds if the impact of a perturbation on the initial condition (𝜎𝑡−1,𝜈𝑡−1), prediction ˆ𝜔𝑗, or terminal constraint (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1) on the component 𝑥𝜏in the optimal trajectory decays exponentially with respect to the absolute difference between their corresponding time indices. Due to its importance for the theoretical analysis of MPC-based algorithms, many previous works have established exponentially decaying perturbation bounds for various cases of online optimization with switching costs [49], optimal control with unconstrained dynamics [49, 56], and online optimization in networked systems [55]. In contrast to previous work, however, the video streaming problem (3) that we consider is a constrained optimal control problem. To this point, there has been limited success in establishing exponentially decaying perturbation bounds for general constrained optimal control problems, and existing results that provide sufficient conditions for their validity are difficult to verify [51, 56]. In this work, we leverage the special structure of the video streaming problem to show the exponentially decaying perturbation bound holds in this setting. We require the following assumption about the buffer constraints, bandwidth, and the bitrate range. Assumption A.1. There exists uniform constants 𝜔max > 𝜔min > 0 such that for any time step 𝑡, we have that 𝜔min ≤𝜔𝑡≤𝜔max holds. We also assume that 𝜔min/𝑟min ≥𝑥max, and 𝜔max/𝑟max −1 ≤−𝛿holds for a fixed constant 𝛿> 0. Intuitively, Assumption A.1 guarantees that the controller can always fill up the buffer at the cost of choosing the smallest bitrate or decrease the buffer level by choosing the largest bitrate. As we discussed in Section 4, this assumption is used to eliminate extreme boundary cases in the analysis, but SODA empirically performs well even when Assumption A.1 is not strictly satisfied. Using this assumption, we show the exponentially decaying perturbation property holds for the video streaming problem in Theorem A.1. Theorem A.1. Under Assumption A.1, the exponentially decaying perturbation bound holds with constants 𝜌= ©­­­­ « 1 − 2 1 + √︂ 1 + max

**Fragmento 5 - p. 4 - score 4:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. sacrificing video quality or sustained playback, (ii) be robust against volatile network conditions, and (iii) be easy to deploy in practice. Before delving into the details in the remainder of the paper, we provide a brief overview of how SODA satisfies these requirements: • SODA leverages SOCO to balance the trade-off between video qual- ity, sustained playback without rebuffers, and bitrate smoothness without frequent switches. Importantly, SODA focuses on steer- ing the buffer level towards a target rather than weighing video quality against rebuffering duration (see Section 3.1). • To achieve robustness against throughput variability, SODA is de- signed to satisfy the exponentially decaying perturbation property, which guarantees that SODA never operates too far away from the optimal trajectory in the face of prediction errors (see Section 4.2).

**Fragmento 6 - p. 5 - score 4:**

Our approach is analogous to the use of control barrier functions to ensure safety properties in control systems [30]. • Modeling rebuffering time directly makes the controller vulnera- ble to throughput prediction errors. Under a direct rebuffering objective, as long as the buffer level is above zero, there will be no penalty for the controller, even if the buffer level is dangerously close to 0. As a result, even small throughput prediction errors can lead to unexpected rebuffering. 3.2 Incorporating Throughput Predictions In addition to facilitating theoretical analysis, our time-based formu- lation is crucial to ensuring the validity of throughput predictions over the prediction horizon. An important observation is that bi- trate decisions have no causal impact on how long the throughput predictions are valid for.

**Fragmento 7 - p. 6 - score 4:**

SODA achieves a dynamic regret of 𝑂( √ E𝑁+ E). The formal statement of Theorem 4.2 is given in Theorem A.8 in Appendix A. Theorem 4.2 shows that, if the buffer costs are “steep” and the prediction errors on the bandwidth are relatively small, SODA can achieve a sequence of buffer levels that stay safely away from the boundaries of buffer constraint [0,𝑥max]. The dynamic regret of SODA depends on the magnitude of the prediction errors and the regret improves when the errors become smaller. SODA acquires this guarantee thanks to its maintenance of the buffer near a target level ¯𝑥. In contrast, RobustMPC [17] doesn’t offer the same performance guarantee, thus even small bandwidth prediction errors can cause the video to rebuffer if the buffer level is near zero.

**Fragmento 8 - p. 6 - score 4:**

Thus, we establish a bound on the per-step error that depends on the errors of predicting future bandwidths and the prediction horizon 𝐾(Lemma A.4). On the other hand, we also show that the aggregation of per-step errors does not grow linearly in time because the exponentially decaying perturbation guarantees that the impact of each previous per-step error vanishes exponentially over time (Lemma A.5). We present a proof outline and the detailed proofs in Appendix A. To prove the exponentially decaying perturbation, we require a technical assumption that guarantees the controller can “reach” any desired buffer level by choosing the largest/smallest bitrate (see Assumption A.1 in Appendix A for the formal statement).

**Fragmento 9 - p. 7 - score 4:**

Given the diverse network conditions in the wild, we prefer simple throughput predictors which makes SODA highly deployable since there is no dependence on complex throughput predictors. In practice, we observe that prediction accuracy degrades as the prediction horizon increases (see Figure 7). Therefore, we limit the prediction horizon length to at most 10 s. This is also supported by our finding in Section 4.1 that a longer prediction horizon yields diminishing returns. 5.3 Efficient Approximate Solver At SODA’s core is the predictive optimization problem described in Section 3.3. Unfortunately, solving this problem on the fly is computationally challenging. One may propose enumerating all combinations of discretized throughputs, buffer levels, and previous bitrates in the form of an offline computed lookup table, as is the Figure 7: We profiled the performance of the two throughput predictors shipped with dash.js [64], i.e., moving average predictor and exponential moving average predictor.

**Fragmento 10 - p. 9 - score 4:**

In Section 4.2, we have showed that SODA is robust against prediction errors by design and does not require a sophisti- cated throughput predictor. We now demonstrate this empirically. First, we replaced the throughput predictor used in simulations with a perfect short-term throughput predictor. Next, we gradually introduced more and more white noise to the perfect throughput predictions and observed how different ABR controllers behave accordingly. This experiment was conducted on a random subset of our network datasets with a size of 10,000 sessions. Note that throughput prediction discounts were turned off for all ABR con- trollers to reveal their intrinsic robustness.1 The results are shown in Figure 11, from which we observe that all hybrid ABR controllers that take throughput predictions into account will inevitably be affected by prediction errors to some extent (BOLA is not affected since it is purely buffer-based).

**Fragmento 11 - p. 9 - score 4:**

However, the performance of MPC is tightly coupled with the intrinsic volatility of network conditions. Specifically, MPC suffers a lot in terms of mean rebuffering ratios especially under mobile network conditions. By contrast, SODA does not have this issue since it is robust against prediction errors by design, making it much more suitable for production deployment. 6.1.4 Intrinsic Sensitivity to Prediction Accuracy. In an effort to im- prove throughput prediction accuracy, several prior works have fo- cused on designing more sophisticated throughput predictors such as C2SP [20], Fugu [46], and Xatu [50]. While these throughput pre- dictors may offer higher prediction accuracy, they are complex and difficult to deploy, especially on compute or memory constrained devices [58].

**Fragmento 12 - p. 19 - score 4:**

𝑟min , where 𝐸(𝑡−1, 𝐾) B Í𝑡+𝐾−1 𝜏=𝑡 𝜌𝜏−𝑡 ˆ𝜔𝜏|𝑡−1 −𝜔𝜏 . Similar to the proof outline for the exact prediction case in Section A.3, we can apply Lemma A.5 to bound the accumulation of past errors. With the help of Lemma A.6 and Lemma A.7, we show our main result for SODA when the predictions of the future bandwidths are inexact in Theorem A.8. We defer the proof of Theorem A.8 to Section D.3. Theorem A.8. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Let 𝐷B min{¯𝑥,𝑥max− ¯𝑥}. Suppose the weight 𝛽, the prediction horizon 𝐾, and the prediction errors satisfy that 𝛽≥ 3 𝜖𝐷·  1 + 4𝛾 𝜔min  ·  1 𝑟min − 1 𝑟max  , and 𝐸(𝑡, 𝐾) + 𝜌𝐾≤ (1 −𝜌)𝐷 3𝐶(1 + 𝐶+ 𝐶′)  1 + 𝑥max + 1 𝑟min − 1 𝑟max  , where, recall, 𝐸(𝑡, 𝐾) = Í𝑡+𝐾 𝜏=𝑡+1 𝜌𝜏−𝑡−1 ˆ𝜔𝜏|𝑡−𝜔𝜏 . Then, the buffer levels in the SODA’s decision trajectory never hits the constraint boundary, i.e., 0 < 𝑥𝑡< 𝑥max for 𝑡= 1, . . . , 𝑁. Further, SODA achieves a dynamic regret of 2  1 + 1 𝑟min + 𝐶+ 𝐶′2  1 + 𝑥max + 1 𝑟min − 1 𝑟max  (1 −𝜌)3/2 · √︁ 4𝛾+ 𝛽+ 𝜔max · √︁ E · cost(OPT)+  1 + 1 𝑟min + 𝐶+ 𝐶′4  1 + 𝑥max + 1 𝑟min − 1 𝑟max 2 (4𝛾+ 𝛽+ 𝜔max) (1 −𝜌)3 · E, where E = 𝜌2𝐾𝑁+ Í𝐾 𝜅=1 𝜌𝜅𝐸𝜅. Here 𝐸𝜅B Í𝑁 𝑡=1 ˆ𝜔𝑡+𝜅|𝑡−𝜔𝑡+𝜅 2. Note that the dynamic regret bound shown in Theorem A.8 is in the order of 𝑂( √ E𝑁+ E), since cost(OPT) = 𝑂(𝑁). Intuitively, from the form of 𝐸𝑡(𝐾), we see that predicting the future bandwidth 𝜔𝜏accurately at time step 𝑡becomes less important as (𝜏−𝑡) increases. A.5 Proof Outline for Efficient Structure In this section, we show that optimal solution of the finite-time optimal control problem solved by SODA can be approximated well by a monotonic sequence of bitrates when the coefficient 𝛾of the switching cost is sufficiently large (see Theorem A.9). Although this result is shown for the continuous variable case, it also provides some insight as to why the efficient approximate solver in Algorithm 1 can provide identical decisions to the brute-force solver with relatively high probabilities, as shown in Figure 8. Theorem A.9. Let ˆ𝜔×𝐾denote the sequence { ˆ𝜔, . . . , ˆ𝜔} with length 𝐾. For any 𝜆> 0, when the coefficient 𝛾is sufficiently large such that 𝛾≥𝐾2 𝜆2

**Fragmento 13 - p. 1 - score 3:**

However, users often find frequent bitrate switching frustrating due to the resulting inconsistency in visual quality over time, es- pecially during live streaming when buffer lengths are short. In this paper, we propose a practical smoothness optimized dynamic adaptive (SODA) controller that specifically addresses this problem while remaining deployable. SODA is backed by theoretical guaran- tees and has shown superior performance in empirical evaluations. Specifically, our numerical simulations show a 9.55% to 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE im- provement compared to the state-of-the-art baselines. In order to be widely deployable, SODA performs bitrate horizon planning in poly- nomial time compared to brute force approaches that suffer from exponential complexity.

**Fragmento 14 - p. 1 - score 3:**

To achieve this, a video source is encoded at different bitrates corresponding to different resolutions, e.g., 720p, 1080p, 1440p, etc. Each encod- ing is in turn temporally partitioned into a sequence of segments, e.g., 2 seconds of video content. An ABR controller inside a user’s video player then selects a suitable bitrate for each segment. Finally, downloaded segments are stored in a buffer, till they are rendered. Past studies have shown that a user’s QoE is maximized by de- livering the video at the highest possible quality with minimal rebuffering and bitrate switching. It has been shown that a 1% in- crease in rebuffering time is correlated with a 3-minute reduction in the viewing duration [7] and frequent bitrate switching is strongly correlated with a user abandoning the session [21].

**Fragmento 15 - p. 2 - score 3:**

2) Better QoE Across Empirical Evaluations. We evaluated SODA in three settings: numerical simulations, prototype evalua- tion, and production deployment within Amazon Prime Video serving actual users. Our numerical simulations show a 9.55% to Figure 2: BOLA’s [44] decision boundaries are spaced out for on-demand streaming, but tiny fluctuations in buffer level can cause bitrate switching for live streaming. 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE improvement compared to the state-of-the-art base- lines. Production live streaming experiments in Amazon Prime Video show that SODA reduced bitrate switching by a significant up to 88.8% and increased average stream viewing duration by up to 5.91% (> 5 minutes longer sessions) compared to a fine- tuned production baseline.

**Fragmento 16 - p. 3 - score 3:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 17 - p. 4 - score 3:**

The time-based buffer dynamics are introduced into the opti- mization problem through the following constraint: 𝑥𝑛= 𝑥𝑛−1 + 𝜔𝑛Δ𝑡 𝑟𝑛 −Δ𝑡∈[0,𝑥max], where 𝜔𝑛Δ𝑡/𝑟𝑛accounts for the variable amount of video down- loaded during a time interval and Δ𝑡accounts for the fixed amount of buffer drained during the same time interval. Note that we do not allow the controller to violate the buffer range constraint during the optimization phase when determining the bitrate. Of course, due to throughput prediction errors, this may sometimes be inevitable during the execution phase when applying the bitrate decision. Why a Time-Based Formulation? The time-based formulation allows a cleaner theoretical analysis over a given throughput se- quence (𝜔1, .

**Fragmento 18 - p. 5 - score 3:**

It is always assumed that the validity of the throughput prediction is 𝐾Δ𝑡, a fixed value. In gen- eral, a throughput predictor may output a different value for each of the next 𝐾time intervals, i.e., ˆ𝜔𝑛|𝑛−1, ˆ𝜔𝑛+1|𝑛−1, . . . , ˆ𝜔𝑛+𝐾−1|𝑛−1, where ˆ𝜔𝑚|𝑛−1 (𝑚≥𝑛) is the throughput prediction for the 𝑚th time interval given previous download information up until the (𝑛−1)th time interval. In other words, a throughput predictor can output a piecewise constant throughput function for the next 𝐾Δ𝑡 time. In practice, though, a typical throughput predictor outputs a single value that corresponds to a constant throughput function. 3.3 Control Mechanism Inspired by the model predictive control framework, SODA selects a bitrate for each time interval by optimizing over the next 𝐾time intervals and then committing to the bitrate decision for the imme- diate next time interval, i.e., minimizing 𝑛+𝐾−1 ∑︁ 𝑚=𝑛  𝑣(𝑟𝑚) · ˆ𝜔𝑚|𝑛−1Δ𝑡 𝑟𝑚 + 𝛽· 𝑏(𝑥𝑚) + 𝛾· 𝑐(𝑟𝑚,𝑟𝑚−1)  (2a) Figure 5: SODA’s bitrate decision as a function of buffer level and predicted throughput.

**Fragmento 19 - p. 5 - score 3:**

We first analyze these questions theoretically (Section 4) and then present a practical implementation of SODA that answers these concerns (Section 5). 4 THEORETICAL DESIGN INSIGHTS Our design of SODA is motivated by recent theoretical advances at the interface of learning and control [28, 38, 49, 54] and smoothed online convex optimization [25, 33, 55]. In particular, we design SODA to satisfy an exponentially decaying perturbation property that has been shown to ensure efficient and robust use of predictions in model predictive control policies [49, 56]. Intuitively, this property describes the behavior of the solution to the optimization problem defining SODA (Equation 2) as a function of problem parameters, including bandwidth predictions { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾and the previ- ous buffer level/action pair (𝑥𝑛−1,𝑢𝑛−1).

**Fragmento 20 - p. 6 - score 3:**

The key idea underlying our theoretical analysis is to leverage the exponential decay property to bound (i) the error that SODA incurs at every intermediate time step 𝑛due to its limited prediction power ( ˆ𝜔𝑚|𝑛−1 ≠𝜔𝑚, 𝐾≪𝑁), and (ii) the aggregation of such errors over the whole horizon 𝑁. Specifically, we define the notion of per-step error at a time step 𝑛as the distance between SODA’s buffer/action pair and the optimal buffer/action pair that one could reach with exact predictions of all future bandwidths 𝜔𝑛,𝜔𝑛+1, . . . ,𝜔𝑁given the previous buffer/action pair (𝑥𝑛−1,𝑢𝑛−1) (Definition A.2). Using the principle of optimality, we reformulate the optimal buffer/action pair as an entry of the optimal trajectory from time 𝑛to (𝑛+ 𝐾−1) so that we can directly compare it with SODA’s buffer/action pair under the exponentially decaying perturbation.

**Fragmento 21 - p. 6 - score 3:**

Fortunately, the exponential decay property that ensures good performance with only a few predictions. More formally, we present a theorem showing that a small prediction horizon is sufficient for SODA to achieve near-optimal performance when the predictions within this window are accurate (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1). Theorem 4.1. [Informal] When the predictions of the bandwidth in future 𝐾steps are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾≥𝑂(1), SODA achieves a dynamic regret of 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 +𝑂(𝜌𝐾), where 𝜌< 1 is the decay factor of the exponentially decaying perturbation property. The formal statement of Theorem 4.1 is given in Theorem A.3 in Appendix A.

**Fragmento 22 - p. 7 - score 3:**

5.1 Segment-Based Schema SODA is intrinsically a time-based controller, but in practice, a video must be downloaded segment by segment according to the MPEG- DASH standard. To reconcile with this requirement, we keep the optimization phase as is in the time-based format and empirically set Δ𝑡to be equal to the segment length. This choice is justified by the fact that in the steady state, the download time of a video segment is expected to be close to the segment length or much less than that [29]. To further minimize the likelihood of committing to a bitrate for significantly longer than Δ𝑡, we introduce another heuristic that the controller must select a bitrate no higher than min{𝑟∈R : 𝑟≥ˆ𝜔}. 5.2 Incorporating Predictions Robustly According to Section 4.2, SODA is robust against prediction errors by design as long as there is no systematic bias in prediction er- rors.

**Fragmento 23 - p. 7 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia minimum possible time. A critical observation underlying the im- plementation of SODA is that it is sufficient to search only for bitrate sequences that are increasing or decreasing monotonically. We provide a theoretical justification in the following theorem. Theorem 4.3. [Informal] Suppose SODA is given the predictions that satisfy ˆ𝜔𝑛|𝑛−1 = · · · = ˆ𝜔𝑛+𝐾−1|𝑛−1 at an intermediate time step 𝑛. Then, the bitrate trajectory solved by SODA can be approximated by a feasible monotonic bitrate trajectory with an error of 𝑂 𝐾/√𝛾. The formal statement of Theorem 4.3 is given in Theorem A.9 in Appendix A.

**Fragmento 24 - p. 8 - score 3:**

This funnel approach allowed us to first systematically evaluate SODA against a variety of baselines in a wide range of controlled environments. Later, we narrowed the comparison target to a deployed and fine-tuned ABR controller in production using A/B tests on real user sessions. Performance Metrics. To maintain consistency in terms of perfor- mance metrics with prior works such as [17, 22, 24, 46], a similar definition of QoE is adopted that consists of mean utility, rebuffer- ing ratio, and switching rate. These correspond to the three main desired properties of adaptive bitrate streaming, i.e., high video quality, shorter rebuffering time, and less bitrate switching. All three QoE components are normalized between 0 and 1 for ease of interpretation.

**Fragmento 25 - p. 8 - score 3:**

• 4G Dataset [27]: A 4G network dataset from two major Irish mobile operators under both static and moving scenarios while downloading online content. For all three datasets, we filtered out sessions shorter than 10 min- utes and divided long sessions into consecutive 10-minute sessions, resulting in 230,322 sessions from the Puffer dataset, 88 sessions from the 5G dataset, and 187 sessions from the 4G dataset. Fig- ure 9 illustrates the wide range of network conditions covered by these datasets. In general, the Puffer dataset represents better net- work conditions than the 5G and 4G datasets. The latter have much lower mean throughput and higher variance, thus posing a bigger challenge for ABR controllers.

**Fragmento 26 - p. 8 - score 3:**

To fully exercise our datasets, we considered a high-frame-rate 4K video encoded according to the YouTube recommended settings (1.5, 4, 7.5, 12, 24, and 60 Mb/s) [65] with a segment length of 2 seconds. For the 5G and 4G datasets, we considered the same video with the two highest bitrates removed. Finally, for throughput prediction, we opted for the exponential moving average (EMA) predictor, the default throughput predictor in dash.js. 6.1.2 Baseline ABR Controllers. We compared SODA against the following ABR controllers representative of each of the common ABR controller categories, i.e., throughput-based, buffer-based, and hybrid. They were tuned to our best efforts for our network datasets. 620


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 13 - score 7:**

2016. CS2P: Improving Video Bitrate Selection and Adaptation with Data-Driven Throughput Prediction. In Proceedings of the 2016 ACM SIGCOMM Conference. ACM, New York, NY, USA, (Aug. 2016), 272–285. isbn: 9781450341936. doi: 10.1145/2934872.2934898. [21] Christos George Bampis, Zhi Li, Anush Krishna Moorthy, Ioannis Katsavouni- dis, Anne Aaron, and Alan Conrad Bovik. 2017. Study of Temporal Effects on Subjective Video Quality of Experience. IEEE Transactions on Image Processing, 26, 11, 5217–5231. doi: 10.1109/TIP.2017.2729891. [22] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural Adap- tive Video Streaming with Pensieve. In ACM, (Aug. 2017), 197–210. isbn: 9781450346535. doi: 10.1145/3098822.3098843.

**Fragmento 2 - p. 2 - score 6:**

This work does not raise any ethical issues. 2 DESIGN GAPS, OPPORTUNITIES, AND REQUIREMENTS Design Gaps. Live streaming poses the additional constraint of near real-time delivery which makes bitrate adaptation more chal- lenging than that in on-demand streaming. Figure 2 shows the bitrate selection function of BOLA [36, 40, 44], an ABR controller that is widely deployed by video providers and is part of the refer- ence MPEG-DASH video player [64]. Notice that for on-demand 614

**Fragmento 3 - p. 11 - score 6:**

Takeaways from Production Deployment. The production deployment shows that SODA is practical and can be widely deployed across different device types and network connections. Furthermore, to achieve its significant performance gains, it is sufficient for SODA to use simple sliding window-based throughput predictors. 7 RELATED WORK 7.1 Adaptive Bitrate Streaming Bitrate adaptation has received significant attention from the mul- timedia research community. Buffer-based controllers like BBA [15] and BOLA [36, 44] make bitrate decisions based on buffer occu- pancy, while hybrid controllers like HYB [24], MPC [17] and DYNAMIC [44] combine throughput predictions with buffer occupancy to make decisions.

**Fragmento 4 - p. 19 - score 6:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Intuitively, Lemma A.6 holds because increasing 𝛽makes staying close to the target buffer level more important. In the extreme case that 𝛽tends to +∞, the offline optimal will ignore the distortion/switching cost and select actions so that the buffer level always equal to ¯𝑥. Recall that the per-step error of SODA is defined in Definition A.2. We bound the per-step error in Lemma A.7 and defer its proof to Section D.2. Lemma A.7. When the predictions for the future bandwidth are inexact, the per-step error of SODA satisfies 𝑒𝑡≤(𝐶+ 𝐶′)𝜌𝐾  𝑥max + 1 𝑟min − 1 𝑟max  + (𝐶+ 𝐶′) · 𝐸(𝑡−1, 𝐾) + 𝜔𝑡−ˆ𝜔𝑡|𝑡−1

**Fragmento 5 - p. 5 - score 5:**

However, segment-based controllers such as MPC [17] and Fugu [46] intertwine throughput predictions and bi- trate decisions in non-causal ways. In these designs, the throughput prediction horizon spans shorter periods of clock time when low bitrate is selected compared to when high bitrate is selected. In fact, their underlying assumption about the validity of the throughput prediction horizon can vary by 𝑟max/𝑟min. By contrast, the way we incorporate throughput predictions into SODA does not suffer from this issue. Specifically, just before each time interval, the controller is given access to a (not necessarily accurate) throughput prediction for the next 𝐾time intervals from a black-box throughput predictor.

**Fragmento 6 - p. 11 - score 5:**

SODA belongs to the latter category. There are also learning-based controllers such as Pensive [22] that utilize rein- forcement learning to learn a bitrate selection strategy. Another relevant stream of work focuses on improving the accuracy of throughput predictions, including CS2P [20], Fugu [46], and Xatu [50]. Our work makes no assumption on the quality of throughput predictions and does not require a sophisticated throughput pre- dictor. Past works have also considered upgrading the downloaded segments through replacement [36] which we do not consider in this paper. 7.2 Video Quality of Experience The advent of video content delivery networks [2, 6] in the late 1990’s led to efforts in industry to define and measure quality met- rics for video delivery.

**Fragmento 7 - p. 13 - score 5:**

Advances in Neural Information Processing Systems, 32. [34] Gautam Goel and Adam Wierman. 2019. An Online Algorithm for Smoothed Regression and LQR Control. In Proceedings of the Machine Learning Research. Vol. 89, 2504–2513. http://proceedings.mlr.press/v89/goel19a.html. [35] Ming Shi, Xiaojun Lin, and Lei Jiao. 2019. On the value of look-ahead in com- petitive online convex optimization. Proceedings of the ACM on Measurement and Analysis of Computing Systems, 3, 2, 22. [36] Kevin Spiteri, Ramesh Sitaraman, and Daniel Sparacio. 2019. From Theory to Practice: Improving Bitrate Adaptation in the DASH Reference Player. ACM Transactions on Multimedia Computing, Communications, and Applications, 15, 2s, (Apr. 2019), 1–29.

**Fragmento 8 - p. 14 - score 5:**

2020), 1509–1518. Retrieved Oct. 15, 2021 from. [43] Guanya Shi, Yiheng Lin, Soon-Jo Chung, Yisong Yue, and Adam Wierman. 2020. Online optimization with memory and competitive control. Advances in Neural Information Processing Systems, 33, 20636–20647. [44] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K. Sitaraman. 2020. BOLA: Near- Optimal Bitrate Adaptation for Online Videos. IEEE/ACM Transactions on Net- working, 28, 4, (Aug. 2020), 1698–1711. doi: 10.1109/TNET.2020.2996964. [45] Dongzhu Xu, Anfu Zhou, Xinyu Zhang, Guixian Wang, Xi Liu, Congkai An, Yiming Shi, Liang Liu, and Huadong Ma. 2020. Understanding Operational 5G: A First Measurement Study on Its Coverage, Performance and Energy Consump- tion. In (SIGCOMM ’20).

**Fragmento 9 - p. 17 - score 5:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia (𝑥0,𝑢0) (𝑥∗ 1,𝑢∗ 1) (𝑥∗ 2,𝑢∗ 2) (𝑥∗ 3,𝑢∗ 3) (𝑥∗ 4,𝑢∗ 4) (𝑥1,𝑢1) (𝑥2,𝑢2) (𝑥3,𝑢3) Figure 14: Illustration of the aggregations of per-step errors. In the figure, {(𝑥∗ 𝑡,𝑢∗ 𝑡)}𝑡=1,2,... denotes the offline optimal states and control actions, and {(𝑥𝑡,𝑢𝑡)}𝑡=1,2,... denotes the buffer level achieved by SODA. The dashed trajectory from (𝑥𝑡,𝑢𝑡) denotes the clairvoyant optimal trajectory from (𝑥𝑡,𝑢𝑡). At time 𝑡, the per-step error 𝑒𝑡leads to the deviation of the actual trajectory of SODA with the clairvoyant optimal trajectory. The impact of the per-step error 𝑒1 at a future time step 𝑡is the height of blue area, which decays exponentially fast with respect to 𝑡when exponentially decaying perturbation holds. Therefore, although a per-step error occurs at every time step, the distance between (𝑥𝑡,𝑢𝑡) and (𝑥∗ 𝑡,𝑢∗ 𝑡) is still uniformly bounded. Corollary A.2. Under Assumption A.1, for the control action 𝑢, we also have that 𝜓𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 0 𝑢𝜏−𝜓𝑡+𝑝 𝑡  (𝜎′ 𝑡−1,𝜈′ 𝑡−1); ˆ𝜔′ 𝑡:𝑡+𝑝; 0  𝑢𝜏

**Fragmento 10 - p. 1 - score 4:**

To achieve this, a video source is encoded at different bitrates corresponding to different resolutions, e.g., 720p, 1080p, 1440p, etc. Each encod- ing is in turn temporally partitioned into a sequence of segments, e.g., 2 seconds of video content. An ABR controller inside a user’s video player then selects a suitable bitrate for each segment. Finally, downloaded segments are stored in a buffer, till they are rendered. Past studies have shown that a user’s QoE is maximized by de- livering the video at the highest possible quality with minimal rebuffering and bitrate switching. It has been shown that a 1% in- crease in rebuffering time is correlated with a 3-minute reduction in the viewing duration [7] and frequent bitrate switching is strongly correlated with a user abandoning the session [21].

**Fragmento 11 - p. 2 - score 4:**

ABR controllers deployed in the field need to work on a wide range of client devices, including low-end ones with limited computa- tional resources. Many ABR controllers proposed in the research literature do not meet the efficiency bar for a production de- ployment and are never implemented in practice. We maximized SODA’s runtime and deployment practicality by devising a com- putationally efficient method to search for near-optimal bitrate decisions, which reduced the runtime complexity from exponen- tial to polynomial, e.g., about 200 iterations max in practice. In addition, we made SODA robust against throughput prediction errors by design, thus eliminating the need for sophisticated computationally-intensive throughput predictors.

**Fragmento 12 - p. 4 - score 4:**

This enables us to incorporate throughput predictions into the controller in a prin- cipled way. Taking advantage of recent advancements in smoothed online convex optimization (SOCO), we can theoretically prove that SODA offers a near-optimal quality of experience (QoE) and is robust against throughput prediction errors. 3.1 A Time-Based ABR Formulation Our time-based ABR formulation treats a video stream as a contin- uous flow rather than a discrete sequence of segments. Consider a streaming session that consists of 𝑁time intervals with fixed dura- tion Δ𝑡in terms of clock time (not video time). The controller’s task is to select a bitrate for each time interval from a set of available bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high quality, short rebuffering, and infrequent bitrate switching.

**Fragmento 13 - p. 4 - score 4:**

. . ,𝜔𝑁). For example, consider the throughput function shown in Figure 4. In the time-based formulation, we naturally have 𝜔1 = 4, 𝜔2 = 1, and 𝜔3 = 𝜔4 = 2 Mb/s given Δ𝑡= 1 s. By contrast, in the segment-based formulation, the throughput sequence be- comes dependent on the bitrate sequence. Assuming the segment duration is also 𝐿= 1 s, if the controller chooses 𝑟1 = 2 Mb/s and 𝑟2 = 2.5 Mb/s, then it takes 0.5 and 1 s to download the first and sec- ond segments respectively, resulting in 𝜔1 = 4 and 𝜔2 = 2.5 Mb/s. As such, the segment based formulation gets causally biased due to bitrate selection 𝑟1, ...,𝑟𝑁, which in turn makes it difficult to theoretically analyze the design [61]. Why Not Model Rebuffering Directly?

**Fragmento 14 - p. 5 - score 4:**

It is always assumed that the validity of the throughput prediction is 𝐾Δ𝑡, a fixed value. In gen- eral, a throughput predictor may output a different value for each of the next 𝐾time intervals, i.e., ˆ𝜔𝑛|𝑛−1, ˆ𝜔𝑛+1|𝑛−1, . . . , ˆ𝜔𝑛+𝐾−1|𝑛−1, where ˆ𝜔𝑚|𝑛−1 (𝑚≥𝑛) is the throughput prediction for the 𝑚th time interval given previous download information up until the (𝑛−1)th time interval. In other words, a throughput predictor can output a piecewise constant throughput function for the next 𝐾Δ𝑡 time. In practice, though, a typical throughput predictor outputs a single value that corresponds to a constant throughput function. 3.3 Control Mechanism Inspired by the model predictive control framework, SODA selects a bitrate for each time interval by optimizing over the next 𝐾time intervals and then committing to the bitrate decision for the imme- diate next time interval, i.e., minimizing 𝑛+𝐾−1 ∑︁ 𝑚=𝑛  𝑣(𝑟𝑚) · ˆ𝜔𝑚|𝑛−1Δ𝑡 𝑟𝑚 + 𝛽· 𝑏(𝑥𝑚) + 𝛾· 𝑐(𝑟𝑚,𝑟𝑚−1)  (2a) Figure 5: SODA’s bitrate decision as a function of buffer level and predicted throughput.

**Fragmento 15 - p. 5 - score 4:**

Dark blue to light orange repre- sent low to high bitrate decisions. Notice that SODA becomes more aggressive in selecting higher bitrates as the buffer grows. The rightmost region is blank since SODA makes no downloads to prevent a buffer overflow. subject to 𝑥𝑚= 𝑥𝑚−1 + ˆ𝜔𝑚|𝑛−1Δ𝑡 𝑟𝑚 −Δ𝑡, (2b) 𝑥𝑚∈[0,𝑥max], 𝑟𝑚∈R, (2c) with respect to variables 𝑟𝑛, . . . ,𝑟𝑛+𝐾−1 and then committing to only the first bitrate decision 𝑟𝑛. The behavior of SODA is visualized as a bitrate decision diagram in Figure 5 to provide readers with intuition about how SODA selects bitrates in practice. As discussed in Section 2, solving this optimization problem is computationally expensive, furthermore, it is unclear what predic- tion horizon should be used and how accurate throughput predic- tions must be in order for SODA to perform well.

**Fragmento 16 - p. 11 - score 4:**

However, it switches bitrates 86.3% more often than SODA. Due to the black-box nature of RL-based ABR controllers, it is hard to reason why this is the case. In addition, there exists no straightforward way to tune an RL-based controller in favor of one particular QoE component without a complete retraining. In a production environment, it is highly desirable that the trade-off between different QoE components is tunable. 6.3 Production Deployment We now describe the results from deploying SODA for live streams delivered on Amazon Prime Video. The bitrate ladder for these video streams had the following bitrate rungs {0.2, 0.45, 0.8, 1.2, 1.8, 2, 4, 5, 6.5, 8.0} Mb/s. This range of available bitrates fully exercised SODA’s bitrate adaptation capability as well as tested its runtime feasibility on actual devices.

**Fragmento 17 - p. 16 - score 4:**

 . (5) Intuitively, the exponential decay property (Definition A.1) holds if the impact of a perturbation on the initial condition (𝜎𝑡−1,𝜈𝑡−1), prediction ˆ𝜔𝑗, or terminal constraint (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1) on the component 𝑥𝜏in the optimal trajectory decays exponentially with respect to the absolute difference between their corresponding time indices. Due to its importance for the theoretical analysis of MPC-based algorithms, many previous works have established exponentially decaying perturbation bounds for various cases of online optimization with switching costs [49], optimal control with unconstrained dynamics [49, 56], and online optimization in networked systems [55]. In contrast to previous work, however, the video streaming problem (3) that we consider is a constrained optimal control problem. To this point, there has been limited success in establishing exponentially decaying perturbation bounds for general constrained optimal control problems, and existing results that provide sufficient conditions for their validity are difficult to verify [51, 56]. In this work, we leverage the special structure of the video streaming problem to show the exponentially decaying perturbation bound holds in this setting. We require the following assumption about the buffer constraints, bandwidth, and the bitrate range. Assumption A.1. There exists uniform constants 𝜔max > 𝜔min > 0 such that for any time step 𝑡, we have that 𝜔min ≤𝜔𝑡≤𝜔max holds. We also assume that 𝜔min/𝑟min ≥𝑥max, and 𝜔max/𝑟max −1 ≤−𝛿holds for a fixed constant 𝛿> 0. Intuitively, Assumption A.1 guarantees that the controller can always fill up the buffer at the cost of choosing the smallest bitrate or decrease the buffer level by choosing the largest bitrate. As we discussed in Section 4, this assumption is used to eliminate extreme boundary cases in the analysis, but SODA empirically performs well even when Assumption A.1 is not strictly satisfied. Using this assumption, we show the exponentially decaying perturbation property holds for the video streaming problem in Theorem A.1. Theorem A.1. Under Assumption A.1, the exponentially decaying perturbation bound holds with constants 𝜌= ©­­­­ « 1 − 2 1 + √︂ 1 + max

**Fragmento 18 - p. 1 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming Tianyu Chen University of Massachusetts Amherst Amherst, MA, USA tianyuchen@umass.edu Yiheng Lin California Institute of Technology Pasadena, CA, USA yihengl@caltech.edu Nicolas Christianson California Institute of Technology Pasadena, CA, USA nchristianson@caltech.edu Zahaib Akhtar Amazon Prime Video / NCSU Sunnyvale, CA, USA akhtz@amazon.com Sharath Dharmaji Amazon Prime Video Sunnyvale, CA, USA sharatdr@amazon.com Mohammad Hajiesmaili University of Massachusetts Amherst Amherst, MA, USA hajiesmaili@cs.umass.edu Adam Wierman California Institute of Technology Pasadena, CA, USA adamw@caltech.edu Ramesh K. Sitaraman University of Massachusetts Amherst Amherst, MA, USA ramesh@cs.umass.edu ABSTRACT The primary objective of adaptive bitrate (ABR) streaming is to enhance users’ quality of experience (QoE) by dynamically adjust- ing the video bitrate in response to changing network conditions.

**Fragmento 19 - p. 1 - score 3:**

However, users often find frequent bitrate switching frustrating due to the resulting inconsistency in visual quality over time, es- pecially during live streaming when buffer lengths are short. In this paper, we propose a practical smoothness optimized dynamic adaptive (SODA) controller that specifically addresses this problem while remaining deployable. SODA is backed by theoretical guaran- tees and has shown superior performance in empirical evaluations. Specifically, our numerical simulations show a 9.55% to 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE im- provement compared to the state-of-the-art baselines. In order to be widely deployable, SODA performs bitrate horizon planning in poly- nomial time compared to brute force approaches that suffer from exponential complexity.

**Fragmento 20 - p. 1 - score 3:**

Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s). ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia © 2024 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-0614-1/24/08 https://doi.org/10.1145/3651890.3672260 KEYWORDS Adaptive bitrate streaming, Smoothed online convex optimization ACM Reference Format: Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath Dharmaji, Mohammad Hajiesmaili, Adam Wierman, and Ramesh K. Sitara- man. 2024. SODA: An Adaptive Bitrate Controller for Consistent High- Quality Video Streaming. In ACM SIGCOMM 2024 Conference (ACM SIG- COMM ’24), August 4–8, 2024, Sydney, NSW, Australia.

**Fragmento 21 - p. 2 - score 3:**

To understand the impact of bitrate switching, Figure 1 shows the re- lationship between the viewing percentage of a stream and bitrate switching rate for a sports event on a large-scale video streaming provider. To minimize potential confounders such as rebuffering and low quality, the plot is focused on short-lived sessions (< 25% of stream viewed) with at least HD quality and no rebuffering. The line of best fit shows that users watch < 10% of the stream when bitrate switching rate is > 20%. While our proposed ABR controller works for both on-demand and live streaming, our evaluations use live streams that represents a more challenging use case. Our Contributions. We propose a novel smoothness optimized dynamic adaptive (SODA) controller that provides theoretical QoE guarantees while exhibiting superior empirical performance in simulation, prototype, and production experiments.

**Fragmento 22 - p. 2 - score 3:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 1: Video stream duration is negatively correlated with bitrate switching rate. Users watch < 10% of the stream when bitrate switching rate is > 20%. switching, is non-trivial as they are locked in a three-way trade-off. An ideal ABR controller seeks to push the trade-off boundary and optimize all three QoE components simultaneously. Between on-demand and live streaming, the latter is more chal- lenging as the player buffer is restricted to 10 - 20 seconds (to remain close to actual live action), which is in contrast to 60 - 180 seconds of buffer in on-demand streaming. Consequently, live streaming has higher susceptibility to rebuffering and bitrate switching.

**Fragmento 23 - p. 3 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Table 1: A qualitative summary of our key evaluation findings about SODA as compared to baseline ABR controllers. Controller Theorya Video Quality Rebuffering Time Switching Rate Deployability SODA Q + R + S high short ultra low high HYB [24] none high medium high high BOLA [44] Q + R high short high high Dynamic [36] Q + R high short medium high MPC [17] none high long low low Fugu [46] none high medium low low CausalSimRL [60] none high short high low aQ, R, S stand for theoretical guarantees for quality, rebuffering, and switching respectively. Figure 3: A RobustMPC session where the controller intention- ally rebuffers instead of lowering the bitrate.

**Fragmento 24 - p. 3 - score 3:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 25 - p. 3 - score 3:**

streaming, a longer buffer of 120 seconds ensures that bitrate jumps are spaced well apart (up to 20 seconds), however, for live streaming with a buffer of 20 seconds, bitrates fluctuate with small deviations of 1 - 3 seconds in the buffer size. This can cause bitrates to switch frequently. While controllers such as MPC [17] and Pensieve [22] offer respite by explicitly penalizing bitrate switching, these con- trollers suffer from shortcomings of their own: • Model predictive controllers are hard to deploy at scale because they need to solve a non-linear integer programming problem over a prediction horizon of 𝐾segments, e.g., 𝐾= 5, which is so computationally expensive that it is quicker to download a video segment than to obtain a bitrate decision [17, 19].

**Fragmento 26 - p. 3 - score 3:**

SOCO provides a systematic framework to balance an objective function with action switching. It thus lends itself well to video streaming, which needs to jointly optimize video quality, sustained playback, and bitrate smoothness. Requirements. Driven by the above design gaps and oppor- tunities, we identify three requirements that SODA should deliver. In particular, SODA should (i) achieve bitrate smoothness without 615


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 8 - score 6:**

This funnel approach allowed us to first systematically evaluate SODA against a variety of baselines in a wide range of controlled environments. Later, we narrowed the comparison target to a deployed and fine-tuned ABR controller in production using A/B tests on real user sessions. Performance Metrics. To maintain consistency in terms of perfor- mance metrics with prior works such as [17, 22, 24, 46], a similar definition of QoE is adopted that consists of mean utility, rebuffer- ing ratio, and switching rate. These correspond to the three main desired properties of adaptive bitrate streaming, i.e., high video quality, shorter rebuffering time, and less bitrate switching. All three QoE components are normalized between 0 and 1 for ease of interpretation.

**Fragmento 2 - p. 3 - score 5:**

SOCO provides a systematic framework to balance an objective function with action switching. It thus lends itself well to video streaming, which needs to jointly optimize video quality, sustained playback, and bitrate smoothness. Requirements. Driven by the above design gaps and oppor- tunities, we identify three requirements that SODA should deliver. In particular, SODA should (i) achieve bitrate smoothness without 615

**Fragmento 3 - p. 4 - score 5:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. sacrificing video quality or sustained playback, (ii) be robust against volatile network conditions, and (iii) be easy to deploy in practice. Before delving into the details in the remainder of the paper, we provide a brief overview of how SODA satisfies these requirements: • SODA leverages SOCO to balance the trade-off between video qual- ity, sustained playback without rebuffers, and bitrate smoothness without frequent switches. Importantly, SODA focuses on steer- ing the buffer level towards a target rather than weighing video quality against rebuffering duration (see Section 3.1). • To achieve robustness against throughput variability, SODA is de- signed to satisfy the exponentially decaying perturbation property, which guarantees that SODA never operates too far away from the optimal trajectory in the face of prediction errors (see Section 4.2).

**Fragmento 4 - p. 9 - score 5:**

In general, the more volatile network conditions are, the more the QoE performance of any ABR con- troller degrades, as evidenced by the trend in Figure 10 from left to right. Nonetheless, SODA consistently outperforms baseline ABR controllers under all network conditions. The improvement in terms of mean QoE scores compared to the best baseline across different network datasets ranges from 9.55% to 27.8%, which mainly stems from improvement in terms of smoothness (shorter rebuffering time and less bitrate switching). We discuss the improvement of SODA over each baseline ABR controller below: • SODA vs HYB. HYB is not as robust as SODA under volatile network conditions. In addition, it switches up to 215% more since it does not consider bitrate switching.

**Fragmento 5 - p. 1 - score 4:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming Tianyu Chen University of Massachusetts Amherst Amherst, MA, USA tianyuchen@umass.edu Yiheng Lin California Institute of Technology Pasadena, CA, USA yihengl@caltech.edu Nicolas Christianson California Institute of Technology Pasadena, CA, USA nchristianson@caltech.edu Zahaib Akhtar Amazon Prime Video / NCSU Sunnyvale, CA, USA akhtz@amazon.com Sharath Dharmaji Amazon Prime Video Sunnyvale, CA, USA sharatdr@amazon.com Mohammad Hajiesmaili University of Massachusetts Amherst Amherst, MA, USA hajiesmaili@cs.umass.edu Adam Wierman California Institute of Technology Pasadena, CA, USA adamw@caltech.edu Ramesh K. Sitaraman University of Massachusetts Amherst Amherst, MA, USA ramesh@cs.umass.edu ABSTRACT The primary objective of adaptive bitrate (ABR) streaming is to enhance users’ quality of experience (QoE) by dynamically adjust- ing the video bitrate in response to changing network conditions.

**Fragmento 6 - p. 1 - score 4:**

However, users often find frequent bitrate switching frustrating due to the resulting inconsistency in visual quality over time, es- pecially during live streaming when buffer lengths are short. In this paper, we propose a practical smoothness optimized dynamic adaptive (SODA) controller that specifically addresses this problem while remaining deployable. SODA is backed by theoretical guaran- tees and has shown superior performance in empirical evaluations. Specifically, our numerical simulations show a 9.55% to 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE im- provement compared to the state-of-the-art baselines. In order to be widely deployable, SODA performs bitrate horizon planning in poly- nomial time compared to brute force approaches that suffer from exponential complexity.

**Fragmento 7 - p. 2 - score 4:**

To understand the impact of bitrate switching, Figure 1 shows the re- lationship between the viewing percentage of a stream and bitrate switching rate for a sports event on a large-scale video streaming provider. To minimize potential confounders such as rebuffering and low quality, the plot is focused on short-lived sessions (< 25% of stream viewed) with at least HD quality and no rebuffering. The line of best fit shows that users watch < 10% of the stream when bitrate switching rate is > 20%. While our proposed ABR controller works for both on-demand and live streaming, our evaluations use live streams that represents a more challenging use case. Our Contributions. We propose a novel smoothness optimized dynamic adaptive (SODA) controller that provides theoretical QoE guarantees while exhibiting superior empirical performance in simulation, prototype, and production experiments.

**Fragmento 8 - p. 2 - score 4:**

We make the following specific contributions: 1) Theoretical Foundations of ABR Controller Design. SODA is the first ABR controller to provably optimize all three key components of QoE, namely, video quality, rebuffering and bi- trate switching. Unlike prior work such as BOLA [36, 44] that use Lyapunov methods to optimize the first two components, we use a new framework based on recent advances in smoothed online convex optimization (SOCO) [13, 25, 26, 33–35, 43] to simultaneously optimize all three QoE components. To enable the application of SOCO, we model the rebuffering minimiza- tion requirement in a novel fashion using the notion of buffer stability. We prove that SODA is near-optimal and achieves QoE within a small factor of the offline optimal QoE (Theorem 4.1).

**Fragmento 9 - p. 3 - score 4:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Table 1: A qualitative summary of our key evaluation findings about SODA as compared to baseline ABR controllers. Controller Theorya Video Quality Rebuffering Time Switching Rate Deployability SODA Q + R + S high short ultra low high HYB [24] none high medium high high BOLA [44] Q + R high short high high Dynamic [36] Q + R high short medium high MPC [17] none high long low low Fugu [46] none high medium low low CausalSimRL [60] none high short high low aQ, R, S stand for theoretical guarantees for quality, rebuffering, and switching respectively. Figure 3: A RobustMPC session where the controller intention- ally rebuffers instead of lowering the bitrate.

**Fragmento 10 - p. 4 - score 4:**

This enables us to incorporate throughput predictions into the controller in a prin- cipled way. Taking advantage of recent advancements in smoothed online convex optimization (SOCO), we can theoretically prove that SODA offers a near-optimal quality of experience (QoE) and is robust against throughput prediction errors. 3.1 A Time-Based ABR Formulation Our time-based ABR formulation treats a video stream as a contin- uous flow rather than a discrete sequence of segments. Consider a streaming session that consists of 𝑁time intervals with fixed dura- tion Δ𝑡in terms of clock time (not video time). The controller’s task is to select a bitrate for each time interval from a set of available bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high quality, short rebuffering, and infrequent bitrate switching.

**Fragmento 11 - p. 8 - score 4:**

The precise definitions are as follows: • Mean Utility: Unless otherwise noted, we use the commonly- used logarithmic utility function: ¯𝑣= 1 𝑁 𝑁 ∑︁ 𝑖=1 log(𝑟𝑖/𝑟min) log(𝑟max/𝑟min) . • Rebuffering Ratio: The ratio of the total rebuffering time to the session duration, i.e., 𝜌rebuf = 𝑇rebuf/𝑇. • Switching Rate: Bitrate switch count divided by segment count minus one, i.e., 𝑝switch = 𝑁switch/(𝑁−1). The QoE score is simply a linear combination of the three QoE components, i.e., QoE = ¯𝑣−𝛽· 𝜌rebuf −𝛾· 𝑝switch. In this work, we chose 𝛽= 10 and 𝛾= 1 to reflect the high importance of minimizing rebuffering time. To establish fair comparisons, we report the individual QoE components along with the QoE score.

**Fragmento 12 - p. 9 - score 4:**

Additionally, it has low-buffer safety heuristic to reduce rebuffering and a switching avoidance heuristic to mitigate bitrate switching. It is the default ABR con- troller in dash.js. • MPC [17]: One application of model predictive control to adap- tive streaming that models utility, rebuffering time, and bitrate switching, without theoretical guarantees. 6.1.3 QoE Performance. The aggregate statistics for QoE scores and individual QoE components under each network dataset are shown in Figure 10. To better understand how the performance of different ABR controllers react to the intrinsic volatility of network conditions, we split the Puffer dataset into four quarters according to the relative standard deviation of throughput (Q1 represents the most stable network conditions, while Q4 represents the most volatile network conditions).

**Fragmento 13 - p. 10 - score 4:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 10: The mean QoE scores, utilities, rebuffering ratios and switching rates of SODA and baseline ABR controllers under each network dataset. The Puffer dataset is split into four quarters according the throughput variance (Q1 being lowest while Q4 being highest). SODA has consistently higher mean QoE scores and lower switching rates than all baseline ABR controllers under all network conditions. (Error bars represent 95% confidence intervals.) Figure 11: The mean QoE scores for SODA and baseline ABR controllers under variable amounts of white noise. (The error bars represent 95% confidence intervals.) the idea that a practical deployment of SODA does not require a sophisticated throughput predictor.2 2In practice, we observe that EMA predictor is actually much better than a perfect short-term predictor with 30% white noise because the noise patterns are different, which means that real gap is less than 10%.

**Fragmento 14 - p. 11 - score 4:**

It is trained using CausalSim for the Puffer platform. 6.2.3 QoE Performance. Puffer employs structure similarity index measures (SSIM) [4] to quantify utility, thus to compare fairly us- ing Puffer, we adapt mean utility to normalized mean SSIM, i.e., ¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching rate, and QoE score remain the same. The aggregate statistics or QoE scores and individual QoE components across all sessions are shown in Figure 12. SODA outperforms the best baseline (Fugu) by 30.4% in terms of mean QoE score. More importantly, SODA is the only ABR controller that achieves low mean rebuffering ratio and switching rate simultaneously, which translates to superior smooth- ness of adaptive streaming.

**Fragmento 15 - p. 1 - score 3:**

To achieve this, a video source is encoded at different bitrates corresponding to different resolutions, e.g., 720p, 1080p, 1440p, etc. Each encod- ing is in turn temporally partitioned into a sequence of segments, e.g., 2 seconds of video content. An ABR controller inside a user’s video player then selects a suitable bitrate for each segment. Finally, downloaded segments are stored in a buffer, till they are rendered. Past studies have shown that a user’s QoE is maximized by de- livering the video at the highest possible quality with minimal rebuffering and bitrate switching. It has been shown that a 1% in- crease in rebuffering time is correlated with a 3-minute reduction in the viewing duration [7] and frequent bitrate switching is strongly correlated with a user abandoning the session [21].

**Fragmento 16 - p. 1 - score 3:**

ACM, New York, NY, USA, 32 pages. https://doi.org/10.1145/3651890.3672260 1 INTRODUCTION With the growth of online video streaming, users nowadays stream videos from a highly diverse set of devices, including laptops, mobile devices, smart TVs, set-top boxes, game consoles, etc. These devices span a wide spectrum of hardware capabilities and connect to the Internet in a multitude of ways, e.g., wireless, cellular, cable, etc. To ensure a high quality of experience (QoE) across all devices, video providers utilize adaptive bitrate (ABR) streaming that tailors video delivery to specific devices and network conditions. The goal of ABR streaming is to deliver a video at the highest sus- tainable quality over time-varying network conditions.

**Fragmento 17 - p. 1 - score 3:**

Going beyond correlational studies, the significant causal impact of rebuffering and other QoE performance metrics on key measures of user behav- ior was first established in [9]. However, jointly optimizing all three key components of QoE, i.e., video quality, rebuffering and bitrate 613

**Fragmento 18 - p. 2 - score 3:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 1: Video stream duration is negatively correlated with bitrate switching rate. Users watch < 10% of the stream when bitrate switching rate is > 20%. switching, is non-trivial as they are locked in a three-way trade-off. An ideal ABR controller seeks to push the trade-off boundary and optimize all three QoE components simultaneously. Between on-demand and live streaming, the latter is more chal- lenging as the player buffer is restricted to 10 - 20 seconds (to remain close to actual live action), which is in contrast to 60 - 180 seconds of buffer in on-demand streaming. Consequently, live streaming has higher susceptibility to rebuffering and bitrate switching.

**Fragmento 19 - p. 3 - score 3:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 20 - p. 3 - score 3:**

Notice that beyond 70 seconds, RobustMPC re- peatedly rebuffers but continues to download the highest bitrate (Figure 3 bottom plot), resulting in 29 rebuffering events over 200 seconds. Strikingly, this behavior is in fact the optimal behavior under RobustMPC’s objective function which tolerates rebuffering to prevent bitrate switches. On the surface, this suggests higher rebuffering penalty in the objective function, however, higher penalties only reduce the duration of these tolerable rebuffers but do not eliminate them. Indeed, past work has empirically shown that even a 20× buffering penalty has marginal impact [24]. • Variance in network conditions or throughput prediction errors are not well tolerated by existing controllers.

**Fragmento 21 - p. 4 - score 3:**

• To remain computationally efficient, SODA leverages an efficient approximate solver (see Section A.5 for proof and Algorithm 1 for implementation), that only requires evaluation of monotonic bitrate sequences (Section 4.3), which reduces the computational cost by two orders of magnitude over a brute-force solver. 3 SODA OVERVIEW Given the design gaps, opportunities, and requirements, we set out to design a theoretically sound adaptive bitrate streaming (ABR) controller that minimizes bitrate switching without compromis- ing video quality or increasing rebuffering time, thus providing a smooth viewing experience. To accomplish this, we deviate from the conventional segment-based ABR formulation and derive theo- retical insights from a time-based ABR formulation.

**Fragmento 22 - p. 5 - score 3:**

Our approach is analogous to the use of control barrier functions to ensure safety properties in control systems [30]. • Modeling rebuffering time directly makes the controller vulnera- ble to throughput prediction errors. Under a direct rebuffering objective, as long as the buffer level is above zero, there will be no penalty for the controller, even if the buffer level is dangerously close to 0. As a result, even small throughput prediction errors can lead to unexpected rebuffering. 3.2 Incorporating Throughput Predictions In addition to facilitating theoretical analysis, our time-based formu- lation is crucial to ensuring the validity of throughput predictions over the prediction horizon. An important observation is that bi- trate decisions have no causal impact on how long the throughput predictions are valid for.

**Fragmento 23 - p. 5 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia • Minimizing rebuffering directly is not theoretically tractable be- cause it requires a binary penalty function that yields a non-zero penalty exactly when the buffer is empty. Instead, we employ a smoother penalty function that increases in magnitude when the buffer level falls below a desired target level. When there is a network issue, we start to penalize early when the buffer level decreases below the safe target level and we provide the largest penalty when the buffer level is empty. Using a smooth penalty function enables us to guarantee that SODA’s optimiza- tion is strongly convex, which is key to our theoretical work.

**Fragmento 24 - p. 9 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Figure 9: The mean throughput of the Puffer, 5G, and 4G datasets are 57.1, 31.3, and 13.0 Mb/s. The mean relative standard deviations of throughput of the Puffer, 5G, and 4G dataset are 47.2%, 133%, and 80.6%. • HYB [24]: A heuristic throughput-based ABR controller that se- lects the highest bitrate without rebuffering. • BOLA [36]: A buffer-based ABR controller derived from Lyapunov optimization. It provides theoretical guarantees about utility and rebuffering time only. • Dynamic [44]: A production version of BOLA that dynamically switches between buffer mode and throughput mode in response to changes in network conditions.

**Fragmento 25 - p. 11 - score 3:**

First, notice that SODA consistently improves all the metrics across all device families, reducing the frequency of bitrate switching on set-top boxes by 88.8%. SODA really shines on HTML5 browsers where it reduced the mean rebuffering ratio by up to 53.0% in addition to 81.8% reduction in switching. This is because HTML5 browsers experience more volatility in network conditions compared to smart TVs and set-top boxes and thus present greater opportunity for improvement. Finally, notice that on all three platforms, the average duration of session increased, with 5.91% improvement on set-top boxes. Live streaming sessions for sports events routinely span multiple hours (e.g., 2-hour soccer broadcast, 3.5-hour cricket broadcast), so a 5.91% increase translates to more than 5 minutes duration.

**Fragmento 26 - p. 11 - score 3:**

We highlight comparisons with the new baseline ABR controllers below: • SODA vs MPC & Fugu. MPC and Fugu are grouped together since, apart from the more sophisticated stochastic throughput pre- dictor, Fugu shares a similar underlying control algorithm with MPC. While they both achieve slightly higher mean utilities than SODA and reasonably low mean switching rates, these benefits are overshadowed by worse mean rebuffering ratios (230% and 104% worse respectively). Although Fugu partially mitigates the rebuffering issue due to its stochastic throughput predictor, it is still not robust enough for challenging network conditions. • SODA vs CausalSimRL. CausalSimRL achieves slightly higher mean utility than SODA and a reasonably low mean rebuffering ratio.


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 8 - score 3:**

6.1 Numerical Simulations To perform large-scale numerical simulations, we implemented a highly optimized ABR simulator in C++ derived from Sabre [36]. The simulation accuracy of Sabre has been empirically validated against dash.js [64], the reference player for MPEG-DASH. We configured the simulator to allow a maximum buffer length of 20 seconds to replicate the typical live streaming conditions. 6.1.1 Experimental Setup. Our network dataset consists of about 38,000 hours of throughput traces compiled from the following three public sources: • Puffer Dataset [46]: We downloaded and parsed all throughput traces from the Puffer platform during the time period of January 2023 to June 2023. • 5G Dataset [41]: A 5G network dataset from a major Irish mobile operator under both static and moving scenarios while down- loading online content.

**Fragmento 2 - p. 11 - score 3:**

However, it switches bitrates 86.3% more often than SODA. Due to the black-box nature of RL-based ABR controllers, it is hard to reason why this is the case. In addition, there exists no straightforward way to tune an RL-based controller in favor of one particular QoE component without a complete retraining. In a production environment, it is highly desirable that the trade-off between different QoE components is tunable. 6.3 Production Deployment We now describe the results from deploying SODA for live streams delivered on Amazon Prime Video. The bitrate ladder for these video streams had the following bitrate rungs {0.2, 0.45, 0.8, 1.2, 1.8, 2, 4, 5, 6.5, 8.0} Mb/s. This range of available bitrates fully exercised SODA’s bitrate adaptation capability as well as tested its runtime feasibility on actual devices.

**Fragmento 3 - p. 13 - score 3:**

[23] Yanyuan Qin, Ruofan Jin, Shuai Hao, Krishna R. Pattipati, Feng Qian, Sub- habrata Sen, Bing Wang, and Chaoqun Yue. 2017. A control theoretic approach to ABR video streaming: A fresh look at PID-based rate adaptation. In IEEE INFOCOM 2017 - IEEE Conference on Computer Communications. IEEE, (May 2017), 1–9. isbn: 978-1-5090-5336-0. doi: 10.1109/INFOCOM.2017.8057056. [24] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe: Auto-Tuning Video ABR Algorithms to Network Conditions. In ACM, (Aug. 2018), 44–58. isbn: 9781450355674. doi: 10.1145/3230543.3230558. [25] Niangjun Chen, Gautam Goel, and Adam Wierman. 2018. Smoothed Online Convex Optimization in High Dimensions via Online Balanced Descent.

**Fragmento 4 - p. 16 - score 3:**

 . (5) Intuitively, the exponential decay property (Definition A.1) holds if the impact of a perturbation on the initial condition (𝜎𝑡−1,𝜈𝑡−1), prediction ˆ𝜔𝑗, or terminal constraint (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1) on the component 𝑥𝜏in the optimal trajectory decays exponentially with respect to the absolute difference between their corresponding time indices. Due to its importance for the theoretical analysis of MPC-based algorithms, many previous works have established exponentially decaying perturbation bounds for various cases of online optimization with switching costs [49], optimal control with unconstrained dynamics [49, 56], and online optimization in networked systems [55]. In contrast to previous work, however, the video streaming problem (3) that we consider is a constrained optimal control problem. To this point, there has been limited success in establishing exponentially decaying perturbation bounds for general constrained optimal control problems, and existing results that provide sufficient conditions for their validity are difficult to verify [51, 56]. In this work, we leverage the special structure of the video streaming problem to show the exponentially decaying perturbation bound holds in this setting. We require the following assumption about the buffer constraints, bandwidth, and the bitrate range. Assumption A.1. There exists uniform constants 𝜔max > 𝜔min > 0 such that for any time step 𝑡, we have that 𝜔min ≤𝜔𝑡≤𝜔max holds. We also assume that 𝜔min/𝑟min ≥𝑥max, and 𝜔max/𝑟max −1 ≤−𝛿holds for a fixed constant 𝛿> 0. Intuitively, Assumption A.1 guarantees that the controller can always fill up the buffer at the cost of choosing the smallest bitrate or decrease the buffer level by choosing the largest bitrate. As we discussed in Section 4, this assumption is used to eliminate extreme boundary cases in the analysis, but SODA empirically performs well even when Assumption A.1 is not strictly satisfied. Using this assumption, we show the exponentially decaying perturbation property holds for the video streaming problem in Theorem A.1. Theorem A.1. Under Assumption A.1, the exponentially decaying perturbation bound holds with constants 𝜌= ©­­­­ « 1 − 2 1 + √︂ 1 + max

**Fragmento 5 - p. 1 - score 2:**

ACM, New York, NY, USA, 32 pages. https://doi.org/10.1145/3651890.3672260 1 INTRODUCTION With the growth of online video streaming, users nowadays stream videos from a highly diverse set of devices, including laptops, mobile devices, smart TVs, set-top boxes, game consoles, etc. These devices span a wide spectrum of hardware capabilities and connect to the Internet in a multitude of ways, e.g., wireless, cellular, cable, etc. To ensure a high quality of experience (QoE) across all devices, video providers utilize adaptive bitrate (ABR) streaming that tailors video delivery to specific devices and network conditions. The goal of ABR streaming is to deliver a video at the highest sus- tainable quality over time-varying network conditions.

**Fragmento 6 - p. 2 - score 2:**

We make the following specific contributions: 1) Theoretical Foundations of ABR Controller Design. SODA is the first ABR controller to provably optimize all three key components of QoE, namely, video quality, rebuffering and bi- trate switching. Unlike prior work such as BOLA [36, 44] that use Lyapunov methods to optimize the first two components, we use a new framework based on recent advances in smoothed online convex optimization (SOCO) [13, 25, 26, 33–35, 43] to simultaneously optimize all three QoE components. To enable the application of SOCO, we model the rebuffering minimiza- tion requirement in a novel fashion using the notion of buffer stability. We prove that SODA is near-optimal and achieves QoE within a small factor of the offline optimal QoE (Theorem 4.1).

**Fragmento 7 - p. 2 - score 2:**

This work does not raise any ethical issues. 2 DESIGN GAPS, OPPORTUNITIES, AND REQUIREMENTS Design Gaps. Live streaming poses the additional constraint of near real-time delivery which makes bitrate adaptation more chal- lenging than that in on-demand streaming. Figure 2 shows the bitrate selection function of BOLA [36, 40, 44], an ABR controller that is widely deployed by video providers and is part of the refer- ence MPEG-DASH video player [64]. Notice that for on-demand 614

**Fragmento 8 - p. 3 - score 2:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 9 - p. 3 - score 2:**

Past works have shown that RobustMPC incurs 26% more rebuffering events unless paired with a sophisticated throughput predictor [46, 50]. Simi- larly, learning-based controllers like Pensieve tend to degrade in performance when trained for realistic network conditions encountered in the wild [24]. In practice, accurate throughput predictions are hard because of several factors, including (i) de- vice and OS level inefficiencies [18], (ii) stop-start nature of video requests which do not interact well with TCP [8, 18], and (iii) volatile network conditions typical in production networks [1, 5, 45]. To make matters worse, sophisticated throughput predictors are themselves not necessarily accurate [16] and are challenging to deploy due to device level bottlenecks [58].

**Fragmento 10 - p. 4 - score 2:**

This enables us to incorporate throughput predictions into the controller in a prin- cipled way. Taking advantage of recent advancements in smoothed online convex optimization (SOCO), we can theoretically prove that SODA offers a near-optimal quality of experience (QoE) and is robust against throughput prediction errors. 3.1 A Time-Based ABR Formulation Our time-based ABR formulation treats a video stream as a contin- uous flow rather than a discrete sequence of segments. Consider a streaming session that consists of 𝑁time intervals with fixed dura- tion Δ𝑡in terms of clock time (not video time). The controller’s task is to select a bitrate for each time interval from a set of available bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high quality, short rebuffering, and infrequent bitrate switching.

**Fragmento 11 - p. 6 - score 2:**

The formal definition of exponentially decaying perturbation generalizes the intuition above to consider the impact of perturbing any parameters on the entire optimal trajectory (see Definition A.1 in Appendix A). Two metrics that we use to measure SODA’s performance theoret- ically are dynamic regret and competitive ratio, which are standard in the literature of online optimization [25, 28, 33, 49, 54]. Specif- ically, let cost(ALG) denote the total cost incurred by an online algorithm ALG and cost(OPT) denote the offline optimal cost (Equa- tion 1) an agent can incur if it has exact knowledge of all future bandwidth at the beginning. We say ALG achieves a dynamic regret of 𝑅if cost(ALG) −cost(OPT) ≤𝑅always holds, and ALG achieves a competitive ratio of 𝐶if cost(ALG) ≤𝐶· cost(OPT) always holds.

**Fragmento 12 - p. 9 - score 2:**

However, the performance of MPC is tightly coupled with the intrinsic volatility of network conditions. Specifically, MPC suffers a lot in terms of mean rebuffering ratios especially under mobile network conditions. By contrast, SODA does not have this issue since it is robust against prediction errors by design, making it much more suitable for production deployment. 6.1.4 Intrinsic Sensitivity to Prediction Accuracy. In an effort to im- prove throughput prediction accuracy, several prior works have fo- cused on designing more sophisticated throughput predictors such as C2SP [20], Fugu [46], and Xatu [50]. While these throughput pre- dictors may offer higher prediction accuracy, they are complex and difficult to deploy, especially on compute or memory constrained devices [58].

**Fragmento 13 - p. 10 - score 2:**

To be fair to those learning-based ABR controllers trained specifically for the Puffer platform, we only considered the Puffer dataset. Since the average bitrate of the high- est resolution is only about 2 Mb/s, we take a random subset of the Puffer dataset with a size of 1,000 sessions whose mean throughput is below 2 Mb/s to create challenging scenarios. 622

**Fragmento 14 - p. 11 - score 2:**

It is trained using CausalSim for the Puffer platform. 6.2.3 QoE Performance. Puffer employs structure similarity index measures (SSIM) [4] to quantify utility, thus to compare fairly us- ing Puffer, we adapt mean utility to normalized mean SSIM, i.e., ¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching rate, and QoE score remain the same. The aggregate statistics or QoE scores and individual QoE components across all sessions are shown in Figure 12. SODA outperforms the best baseline (Fugu) by 30.4% in terms of mean QoE score. More importantly, SODA is the only ABR controller that achieves low mean rebuffering ratio and switching rate simultaneously, which translates to superior smooth- ness of adaptive streaming.

**Fragmento 15 - p. 13 - score 2:**

IEEE/ACM Transactions on Networking, 21, 5, (Oct. 2013), 1378–1391. doi: 10.1109/TNET.2 012.2226216. [13] Masoud Badiei, Na Li, and Adam Wierman. 2015. Online convex optimization with ramp constraints. In 2015 54th IEEE Conference on Decision and Control (CDC). IEEE, 6730–6736. [14] Nikhil Bansal, Anupam Gupta, Ravishankar Krishnaswamy, Kirk Pruhs, Kevin Schewior, and Cliff Stein. 2015. A 2-Competitive Algorithm For Online Convex Optimization With Switching Costs. In Approximation, Randomization, and Combinatorial Optimization. Algorithms and Techniques (APPROX/RANDOM 2015) (Leibniz International Proceedings in Informatics (LIPIcs)). Naveen Garg, Klaus Jansen, Anup Rao, and José D. P. Rolim, (Eds.) Vol. 40. Schloss Dagstuhl–Leibniz- Zentrum fuer Informatik, Dagstuhl, Germany, 96–109.

**Fragmento 16 - p. 13 - score 2:**

In Proceedings of the 2012 Internet Measurement Conference (IMC ’12). Boston, Massachusetts, USA, 211–224. isbn: 9781450317054. doi: 10.1145/2398 776.2398799. [10] Minghong Lin, Zhenhua Liu, Adam Wierman, and Lachlan LH Andrew. 2012. Online algorithms for geographical load balancing. In Proceedings of the Inter- national Green Computing Conference (IGCC), 1–10. [11] Athula Balachandran, Vyas Sekar, Aditya Akella, Srinivasan Seshan, Ion Stoica, and Hui Zhang. 2013. Developing a predictive model of quality of experience for internet video. SIGCOMM Comput. Commun. Rev., 43, 4, (Aug. 2013), 339– 350. doi: 10.1145/2534169.2486025. [12] Minghong Lin, Adam Wierman, Lachlan L. H. Andrew, and Eno Thereska. 2013. Dynamic Right-Sizing for Power-Proportional Data Centers.

**Fragmento 17 - p. 13 - score 2:**

Advances in Neural Information Processing Systems, 32. [34] Gautam Goel and Adam Wierman. 2019. An Online Algorithm for Smoothed Regression and LQR Control. In Proceedings of the Machine Learning Research. Vol. 89, 2504–2513. http://proceedings.mlr.press/v89/goel19a.html. [35] Ming Shi, Xiaojun Lin, and Lei Jiao. 2019. On the value of look-ahead in com- petitive online convex optimization. Proceedings of the ACM on Measurement and Analysis of Computing Systems, 3, 2, 22. [36] Kevin Spiteri, Ramesh Sitaraman, and Daniel Sparacio. 2019. From Theory to Practice: Improving Bitrate Adaptation in the DASH Reference Player. ACM Transactions on Multimedia Computing, Communications, and Applications, 15, 2s, (Apr. 2019), 1–29.

**Fragmento 18 - p. 13 - score 2:**

2016. CS2P: Improving Video Bitrate Selection and Adaptation with Data-Driven Throughput Prediction. In Proceedings of the 2016 ACM SIGCOMM Conference. ACM, New York, NY, USA, (Aug. 2016), 272–285. isbn: 9781450341936. doi: 10.1145/2934872.2934898. [21] Christos George Bampis, Zhi Li, Anush Krishna Moorthy, Ioannis Katsavouni- dis, Anne Aaron, and Alan Conrad Bovik. 2017. Study of Temporal Effects on Subjective Video Quality of Experience. IEEE Transactions on Image Processing, 26, 11, 5217–5231. doi: 10.1109/TIP.2017.2729891. [22] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural Adap- tive Video Streaming with Pensieve. In ACM, (Aug. 2017), 197–210. isbn: 9781450346535. doi: 10.1145/3098822.3098843.

**Fragmento 19 - p. 14 - score 2:**

2020), 1509–1518. Retrieved Oct. 15, 2021 from. [43] Guanya Shi, Yiheng Lin, Soon-Jo Chung, Yisong Yue, and Adam Wierman. 2020. Online optimization with memory and competitive control. Advances in Neural Information Processing Systems, 33, 20636–20647. [44] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K. Sitaraman. 2020. BOLA: Near- Optimal Bitrate Adaptation for Online Videos. IEEE/ACM Transactions on Net- working, 28, 4, (Aug. 2020), 1698–1711. doi: 10.1109/TNET.2020.2996964. [45] Dongzhu Xu, Anfu Zhou, Xinyu Zhang, Guixian Wang, Xi Liu, Congkai An, Yiming Shi, Liang Liu, and Huadong Ma. 2020. Understanding Operational 5G: A First Measurement Study on Its Coverage, Performance and Energy Consump- tion. In (SIGCOMM ’20).

**Fragmento 20 - p. 14 - score 2:**

In Interna- tional Conference on Machine Learning. PMLR, 13356–13393. [56] Yiheng Lin, Yang Hu, Guannan Qu, Tongxin Li, and Adam Wierman. 2022. Bounded-Regret MPC via Perturbation Analysis: Prediction Error, Constraints, and Nonlinearity. arXiv preprint arXiv:2210.12312. [57] Weici Pan, Guanya Shi, Yiheng Lin, and Adam Wierman. 2022. Online opti- mization with feedback delay and nonlinear switching cost. Proceedings of the ACM on Measurement and Analysis of Computing Systems, 6, 1, 1–34. [58] Talha Waheed, Ihsan Ayyub Qazi, Zahaib Akhtar, and Zafar Ayyub Qazi. 2022. Coal Not Diamonds: How Memory Pressure Falters Mobile Video QoE. In (CoNEXT ’22). Roma, Italy, 307–320. isbn: 9781450395083. doi: 10.1145/355505 0.3569120.

**Fragmento 21 - p. 15 - score 2:**

Since we will use the indicator terminal cost frequently, we introduce the shorthand ˜𝜓𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1), which denotes ˜𝜓𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; I𝜎𝑡+𝑝,𝜈𝑡+𝑝+1  . We use 𝜄𝑡+𝑝 𝑡  (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 𝐹 to de- note the optimal objective value of the optimization problem (3). The model of SODA that we consider in the theoretical analysis is summarized in Algorithm 2. The major difference from the SODA algorithm discussed in Section 3.3 is that we include the indicator terminal cost (in line 5) so that the last two states in the predictive trajectory are equal to the target buffer level. This terminal constraint is important for our competitive ratio result in Theorem 4.1, for which we need to bound the squared distance between the trajectories of SODA and the offline optimal controller by a part of the offline optimal cost.

**Fragmento 22 - p. 17 - score 2:**

 , where the decay factor 𝜌is the same as Theorem A.1, and the constant 𝐶′ is given by 𝐶′ = 𝐶(1 + 𝜌)𝑟min + 𝜌 𝜔min𝑟min𝜌 . Here, 𝐶is the same as Theorem A.1. To establish the exponentially decaying perturbation property, we first reduce the video streaming problem to a more general online optimization problem with memory and inequality constraints. Then, we consider each possible combination of active inequality constraints separately and show that the exponentially decaying perturbation property holds in each case. This only requires considering optimization problems with equality constraints with second-order differentiable objectives. Lastly, we show that the exponential decay properties for these separate cases can be combined to establish the exponential decay property for the original video streaming problem. A.3 Proof Outline for Exact Predictions We provide the formal version of Theorem 4.1 that gives the dynamic regret and competitive ratio for SODA with specific coefficients in Theorem A.3. Theorem A.3. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Define the weight 𝐶 and the decay factor 𝜌to be the same as Theorem A.1, and the coefficient 𝐶′ is given by Corollary A.2. Suppose all predictions are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾satisfies 𝐾≥1 4 ln  16 1 −𝜌·  1 + (𝐶+ 𝐶′)2 1 −𝜌  ·  𝐶2 + (𝐶′)22 /ln  1 𝜌  = 𝑂(1). Here, the coefficients 𝐶,𝐶′ and the decay factor 𝜌are given by Theorem A.1 and Corollary A.2. Then, SODA achieves a dynamic regret of 𝐶1𝜌𝐾−1cost(OPT) = 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 + 𝐶1𝜌𝐾−1 = 1 + 𝑂(𝜌𝐾). Here, the coefficient 𝐶1 is given by 𝐶1 = 8

**Fragmento 23 - p. 18 - score 2:**

In this section, we show in two steps that SODA’s decision trajectory will not violate the state constraints. First, by increasing the coefficient 𝛽of the buffer cost, one can guarantee that the offline optimal trajectory stays arbitrarily close to the offline optimal trajectory (see Lemma A.6). Then, we show a bound on the per-step error (Definition A.2) which depends on the prediction error (see Lemma A.7). Recall that the exponentially decaying perturbation bounds allow us to bound the distance between the SODA and the offline optimal trajectories. Therefore, we can combine these results to show that under some mild assumptions on the coefficient 𝛽and the prediction errors, SODA will not violate any constraints, and moreover, it also satisfies a dynamic regret bound (see Theorem A.8).

**Fragmento 24 - p. 18 - score 2:**

By combining Lemma A.4 and Lemma A.5, we bound the total squared distance between SODA’s trajectory and the offline optimal trajectory by a part of the offline optimal cost times a coefficient of the order 𝑂(𝜌2𝐾). Since the cost functions for adaptive video streaming are well-conditioned, we can convert the bound on the total squared distance between the two trajectories into the competitive ratio bound and the dynamic regret bound to finish the proof of Theorem A.3. A.4 Proof Outline for Inexact Predictions Compared with the case when all predictions are exact, a major challenge when the predictions are inexact is that one of SODA’s decisions may cause the next state to violate the state constraint.

**Fragmento 25 - p. 22 - score 2:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. B.1 Proof of Theorem B.1 To show Theorem B.1, we first need to define indicators of active constraints, denoted as 𝜉∈{0, 1}4𝑝+5. Specifically, given the unique optimal solution 𝑥0:𝑝= 𝜓(𝑦,𝑧; 𝜇,𝑤,𝛿) under a tuple of parameters (𝑦,𝑧; 𝜇,𝑤,𝛿), we consider whether the following equality conditions hold: 𝜉1,𝑡= 1{𝑥𝑡= 0}, ∀0 ≤𝑡≤𝑝; 𝜉2,𝑡= 1{𝑥𝑡= 𝑥max}, ∀0 ≤𝑡≤𝑝; 𝜉3,𝑡= 1{𝑥𝑡= 𝜇𝑡}, ∀0 ≤𝑡≤𝑝; 𝜉4,𝑡= 1{𝑥𝑡−𝑥𝑡−1 = −𝛿𝑡}, ∀0 ≤𝑡≤𝑝+ 1. And we define indicators of the sides (denoted as 𝜎∈{0, 1}𝑝+1) as the following: 𝜎𝑡= 1{𝑥𝑡∈[𝜇𝑡,𝑥max]}, ∀0 ≤𝑡≤𝑝. To simplify the notation, we let 𝜃B (𝜇,𝑤,𝛿) ∈Θ B [0,𝑥max]𝑝+1 × W𝑝+𝐻× Δ𝑝+2. While 𝜓(𝑦,𝑧;𝜃) can decide a unique pair of (𝜉, 𝜎), we can also define a new equality-constrained optimization problem using (𝑦,𝑧;𝜃) and (𝜉, 𝜎): Definition B.1.

**Fragmento 26 - p. 22 - score 2:**

We define the equality-constrained optimization problem ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) as ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) = arg min 𝑥−𝐻+1:𝑝+𝐻−1 𝑝 ∑︁ 𝑡=0 𝑓(𝜎𝑡) 𝑡 (𝑥𝑡; 𝜇𝑡) + 𝑝+𝐻−1 ∑︁ 𝑡=0 𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡) (9a) s.t. 𝑥𝑡=   0, if 𝜉1,𝑡= 1 𝑥max, if 𝜉2,𝑡= 1 𝜇𝑡, if 𝜉3,𝑡= 1 , ∀0 ≤𝑡≤𝑝, (9b) 𝑥𝑡−𝑥𝑡−1 = −𝛿𝑡, if 𝜉4,𝑡= 1, ∀0 ≤𝑡≤𝑝+ 1, (9c) 𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧. (9d) Note that it is possible that the optimization problem ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) for some parameters and constraint configurations. We use ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎) to denote the optimal value of this optimization problem. The following lemma states that the optimal solution of (7) will not change if we remove all inactive inequality constraints and leave active constraints as equality constraints.


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 8 - score 8:**

• 4G Dataset [27]: A 4G network dataset from two major Irish mobile operators under both static and moving scenarios while downloading online content. For all three datasets, we filtered out sessions shorter than 10 min- utes and divided long sessions into consecutive 10-minute sessions, resulting in 230,322 sessions from the Puffer dataset, 88 sessions from the 5G dataset, and 187 sessions from the 4G dataset. Fig- ure 9 illustrates the wide range of network conditions covered by these datasets. In general, the Puffer dataset represents better net- work conditions than the 5G and 4G datasets. The latter have much lower mean throughput and higher variance, thus posing a bigger challenge for ABR controllers.

**Fragmento 2 - p. 9 - score 7:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Figure 9: The mean throughput of the Puffer, 5G, and 4G datasets are 57.1, 31.3, and 13.0 Mb/s. The mean relative standard deviations of throughput of the Puffer, 5G, and 4G dataset are 47.2%, 133%, and 80.6%. • HYB [24]: A heuristic throughput-based ABR controller that se- lects the highest bitrate without rebuffering. • BOLA [36]: A buffer-based ABR controller derived from Lyapunov optimization. It provides theoretical guarantees about utility and rebuffering time only. • Dynamic [44]: A production version of BOLA that dynamically switches between buffer mode and throughput mode in response to changes in network conditions.

**Fragmento 3 - p. 8 - score 6:**

6.1 Numerical Simulations To perform large-scale numerical simulations, we implemented a highly optimized ABR simulator in C++ derived from Sabre [36]. The simulation accuracy of Sabre has been empirically validated against dash.js [64], the reference player for MPEG-DASH. We configured the simulator to allow a maximum buffer length of 20 seconds to replicate the typical live streaming conditions. 6.1.1 Experimental Setup. Our network dataset consists of about 38,000 hours of throughput traces compiled from the following three public sources: • Puffer Dataset [46]: We downloaded and parsed all throughput traces from the Puffer platform during the time period of January 2023 to June 2023. • 5G Dataset [41]: A 5G network dataset from a major Irish mobile operator under both static and moving scenarios while down- loading online content.

**Fragmento 4 - p. 8 - score 6:**

To fully exercise our datasets, we considered a high-frame-rate 4K video encoded according to the YouTube recommended settings (1.5, 4, 7.5, 12, 24, and 60 Mb/s) [65] with a segment length of 2 seconds. For the 5G and 4G datasets, we considered the same video with the two highest bitrates removed. Finally, for throughput prediction, we opted for the exponential moving average (EMA) predictor, the default throughput predictor in dash.js. 6.1.2 Baseline ABR Controllers. We compared SODA against the following ABR controllers representative of each of the common ABR controller categories, i.e., throughput-based, buffer-based, and hybrid. They were tuned to our best efforts for our network datasets. 620

**Fragmento 5 - p. 10 - score 6:**

6.2 Prototype Evaluation We next present emulation results from our local client-server deployment where we implemented SODA in the Puffer platform [46]. Thanks to Chrome DevTools’ new capability to throttle WebSocket requests [59], we could replay our network datasets directly in Chrome using WebDriver [63]. The results are intended to highlight the robustness of different ABR controllers under actual browser- based playback. For these experiments, we allowed a maximum buffer length of 15 seconds, as set by Puffer. 6.2.1 Experimental Setup. The video source was a news clip en- coded in five different resolutions (426 × 240, 640 × 360, 854 × 480, 1280 × 720, and 1920 × 1080) with a constant rate factor of 26 and a segment length of 2 seconds.

**Fragmento 6 - p. 9 - score 4:**

In Section 4.2, we have showed that SODA is robust against prediction errors by design and does not require a sophisti- cated throughput predictor. We now demonstrate this empirically. First, we replaced the throughput predictor used in simulations with a perfect short-term throughput predictor. Next, we gradually introduced more and more white noise to the perfect throughput predictions and observed how different ABR controllers behave accordingly. This experiment was conducted on a random subset of our network datasets with a size of 10,000 sessions. Note that throughput prediction discounts were turned off for all ABR con- trollers to reveal their intrinsic robustness.1 The results are shown in Figure 11, from which we observe that all hybrid ABR controllers that take throughput predictions into account will inevitably be affected by prediction errors to some extent (BOLA is not affected since it is purely buffer-based).

**Fragmento 7 - p. 10 - score 4:**

To be fair to those learning-based ABR controllers trained specifically for the Puffer platform, we only considered the Puffer dataset. Since the average bitrate of the high- est resolution is only about 2 Mb/s, we take a random subset of the Puffer dataset with a size of 1,000 sessions whose mean throughput is below 2 Mb/s to create challenging scenarios. 622

**Fragmento 8 - p. 13 - score 4:**

In Proceedings of Conference On Learning Theory (COLT), 1574–1594. [26] Yingying Li, Guannan Qu, and Na Li. 2018. Online Optimization with Predic- tions and Switching Costs: Fast Algorithms and the Fundamental Limit. (2018). arXiv: 1801.07780v3 [math.OC]. [27] Darijo Raca, Jason J. Quinlan, Ahmed H. Zahran, and Cormac J. Sreenan. 2018. Beyond Throughput: A 4G LTE Dataset with Channel and Context Metrics. In Proceedings of the 9th ACM Multimedia Systems Conference. ACM, New York, NY, USA, (June 2018), 460–465. isbn: 9781450351928. doi: 10.1145/3204949.3208123. [28] Naman Agarwal, Brian Bullins, Elad Hazan, Sham Kakade, and Karan Singh. 2019. Online control with adversarial disturbances. In International Conference on Machine Learning.

**Fragmento 9 - p. 14 - score 4:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. [40] Emily Marx, Francis Y. Yan, and Keith Winstein. 2020. Implementing BOLA- BASIC on Puffer: Lessons for the use of SSIM in ABR logic, (Nov. 2020). [41] Darijo Raca, Dylan Leahy, Cormac J. Sreenan, and Jason J. Quinlan. 2020. Beyond Throughput, The Next Generation: A 5G Dataset with Channel and Context Metrics. In Proceedings of the 11th ACM Multimedia Systems Conference. ACM, New York, NY, USA, (May 2020), 303–308. isbn: 9781450368452. doi: 10.1145/3339825.3394938. [42] Mark Sellke. 2020. Chasing convex bodies optimally. In Proceedings of the Thirty-First Annual ACM-SIAM Symposium on Discrete Algorithms (SODA ’20). Society for Industrial and Applied Mathematics, USA, (Jan.

**Fragmento 10 - p. 1 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming Tianyu Chen University of Massachusetts Amherst Amherst, MA, USA tianyuchen@umass.edu Yiheng Lin California Institute of Technology Pasadena, CA, USA yihengl@caltech.edu Nicolas Christianson California Institute of Technology Pasadena, CA, USA nchristianson@caltech.edu Zahaib Akhtar Amazon Prime Video / NCSU Sunnyvale, CA, USA akhtz@amazon.com Sharath Dharmaji Amazon Prime Video Sunnyvale, CA, USA sharatdr@amazon.com Mohammad Hajiesmaili University of Massachusetts Amherst Amherst, MA, USA hajiesmaili@cs.umass.edu Adam Wierman California Institute of Technology Pasadena, CA, USA adamw@caltech.edu Ramesh K. Sitaraman University of Massachusetts Amherst Amherst, MA, USA ramesh@cs.umass.edu ABSTRACT The primary objective of adaptive bitrate (ABR) streaming is to enhance users’ quality of experience (QoE) by dynamically adjust- ing the video bitrate in response to changing network conditions.

**Fragmento 11 - p. 2 - score 3:**

To understand the impact of bitrate switching, Figure 1 shows the re- lationship between the viewing percentage of a stream and bitrate switching rate for a sports event on a large-scale video streaming provider. To minimize potential confounders such as rebuffering and low quality, the plot is focused on short-lived sessions (< 25% of stream viewed) with at least HD quality and no rebuffering. The line of best fit shows that users watch < 10% of the stream when bitrate switching rate is > 20%. While our proposed ABR controller works for both on-demand and live streaming, our evaluations use live streams that represents a more challenging use case. Our Contributions. We propose a novel smoothness optimized dynamic adaptive (SODA) controller that provides theoretical QoE guarantees while exhibiting superior empirical performance in simulation, prototype, and production experiments.

**Fragmento 12 - p. 2 - score 3:**

2) Better QoE Across Empirical Evaluations. We evaluated SODA in three settings: numerical simulations, prototype evalua- tion, and production deployment within Amazon Prime Video serving actual users. Our numerical simulations show a 9.55% to Figure 2: BOLA’s [44] decision boundaries are spaced out for on-demand streaming, but tiny fluctuations in buffer level can cause bitrate switching for live streaming. 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE improvement compared to the state-of-the-art base- lines. Production live streaming experiments in Amazon Prime Video show that SODA reduced bitrate switching by a significant up to 88.8% and increased average stream viewing duration by up to 5.91% (> 5 minutes longer sessions) compared to a fine- tuned production baseline.

**Fragmento 13 - p. 9 - score 3:**

Additionally, it has low-buffer safety heuristic to reduce rebuffering and a switching avoidance heuristic to mitigate bitrate switching. It is the default ABR con- troller in dash.js. • MPC [17]: One application of model predictive control to adap- tive streaming that models utility, rebuffering time, and bitrate switching, without theoretical guarantees. 6.1.3 QoE Performance. The aggregate statistics for QoE scores and individual QoE components under each network dataset are shown in Figure 10. To better understand how the performance of different ABR controllers react to the intrinsic volatility of network conditions, we split the Puffer dataset into four quarters according to the relative standard deviation of throughput (Q1 represents the most stable network conditions, while Q4 represents the most volatile network conditions).

**Fragmento 14 - p. 9 - score 3:**

In general, the more volatile network conditions are, the more the QoE performance of any ABR con- troller degrades, as evidenced by the trend in Figure 10 from left to right. Nonetheless, SODA consistently outperforms baseline ABR controllers under all network conditions. The improvement in terms of mean QoE scores compared to the best baseline across different network datasets ranges from 9.55% to 27.8%, which mainly stems from improvement in terms of smoothness (shorter rebuffering time and less bitrate switching). We discuss the improvement of SODA over each baseline ABR controller below: • SODA vs HYB. HYB is not as robust as SODA under volatile network conditions. In addition, it switches up to 215% more since it does not consider bitrate switching.

**Fragmento 15 - p. 10 - score 3:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 10: The mean QoE scores, utilities, rebuffering ratios and switching rates of SODA and baseline ABR controllers under each network dataset. The Puffer dataset is split into four quarters according the throughput variance (Q1 being lowest while Q4 being highest). SODA has consistently higher mean QoE scores and lower switching rates than all baseline ABR controllers under all network conditions. (Error bars represent 95% confidence intervals.) Figure 11: The mean QoE scores for SODA and baseline ABR controllers under variable amounts of white noise. (The error bars represent 95% confidence intervals.) the idea that a practical deployment of SODA does not require a sophisticated throughput predictor.2 2In practice, we observe that EMA predictor is actually much better than a perfect short-term predictor with 30% white noise because the noise patterns are different, which means that real gap is less than 10%.

**Fragmento 16 - p. 11 - score 3:**

Since then the quality of video delivery is a well studied topic with early work on the Akamai Stream Ana- lyzer system which defined metrics such as startup time, rebuffer ratio, bitrate and failures etc and measured these metrics using data derived from video players deployed around the world [3, 66]. Sub- sequently, [7] showed that a 1% increase in rebuffering correlated with a 3-minute reduction in the amount of time users streamed live content. A study on YouTube [21] found that bitrate fluctua- tions strongly correlate with a user abandoning the session. Beyond correlations, the first study [9] to establish a causal relationship between video quality and user behavior used quasi-experimental 623

**Fragmento 17 - p. 14 - score 3:**

[59] Jecelyn Yeen. 2022. What’s New In DevTools (Chrome 99). (Feb. 2022). https: //developer.chrome.com/en/blog/new-in-devtools-99/. [60] A. Alomar, P. Hamadanian, A. Nasr-Esfahany, A. Agarwal, M. Alizadeh, and D. Shah. 2023. CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation. In 1115–1147. isbn: 9781939133335. https://www.usenix.org/confe rence/nsdi23/presentation/alomar. [61] Chandan Bothra, Jianfei Gao, Sanjay Rao, and Bruno Ribeiro. 2023. Veritas: Answering Causal Queries from Video Streaming Traces. In Proceedings of the ACM SIGCOMM 2023 Conference (ACM SIGCOMM ’23). New York, NY, USA, 738–753. doi: 10.1145/3603269.3604828. [62] Nicolas Christianson, Junxuan Shen, and Adam Wierman. 2023. Optimal Robustness- Consistency Tradeoffs for Learning-Augmented Metrical Task Systems.

**Fragmento 18 - p. 1 - score 2:**

To demonstrate its real-world practicality, we deployed SODA on a wide range of devices within the production network of Amazon Prime Video. Production experiments show that SODA reduced bitrate switching by up to 88.8% and increased average stream viewing duration by up to 5.91% compared to a fine-tuned production baseline. CCS CONCEPTS • Information systems →Multimedia streaming; • Theory of computation →Online algorithms; Theory and algorithms for application domains. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.

**Fragmento 19 - p. 1 - score 2:**

ACM, New York, NY, USA, 32 pages. https://doi.org/10.1145/3651890.3672260 1 INTRODUCTION With the growth of online video streaming, users nowadays stream videos from a highly diverse set of devices, including laptops, mobile devices, smart TVs, set-top boxes, game consoles, etc. These devices span a wide spectrum of hardware capabilities and connect to the Internet in a multitude of ways, e.g., wireless, cellular, cable, etc. To ensure a high quality of experience (QoE) across all devices, video providers utilize adaptive bitrate (ABR) streaming that tailors video delivery to specific devices and network conditions. The goal of ABR streaming is to deliver a video at the highest sus- tainable quality over time-varying network conditions.

**Fragmento 20 - p. 2 - score 2:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 1: Video stream duration is negatively correlated with bitrate switching rate. Users watch < 10% of the stream when bitrate switching rate is > 20%. switching, is non-trivial as they are locked in a three-way trade-off. An ideal ABR controller seeks to push the trade-off boundary and optimize all three QoE components simultaneously. Between on-demand and live streaming, the latter is more chal- lenging as the player buffer is restricted to 10 - 20 seconds (to remain close to actual live action), which is in contrast to 60 - 180 seconds of buffer in on-demand streaming. Consequently, live streaming has higher susceptibility to rebuffering and bitrate switching.

**Fragmento 21 - p. 8 - score 2:**

Empirical results are shown in Figure 8 to validate the near- optimality of bitrate decisions produced by the approximate solver. For each algorithm configuration, we uniformly sample a million situations with different throughputs, buffer levels, and previous bitrates. Then, we count the probability that the bitrate decision produced by the approximate solver is different from that produced by the brute-force solver. The difference is negligible for a reason- able switching cost weight, e.g., below 5% for 𝐾= 4 and a relative switching cost weight of 2. Throughout the evaluation sections, we use this efficient implementation of SODA. 6 EVALUATION To thoroughly evaluate SODA’s performance, we conducted three levels of empirical evaluation: (i) large-scale numerical simulations, (ii) prototype evaluation in Puffer [46], and (iii) production deploy- ment in Amazon Prime Video.

**Fragmento 22 - p. 8 - score 2:**

This funnel approach allowed us to first systematically evaluate SODA against a variety of baselines in a wide range of controlled environments. Later, we narrowed the comparison target to a deployed and fine-tuned ABR controller in production using A/B tests on real user sessions. Performance Metrics. To maintain consistency in terms of perfor- mance metrics with prior works such as [17, 22, 24, 46], a similar definition of QoE is adopted that consists of mean utility, rebuffer- ing ratio, and switching rate. These correspond to the three main desired properties of adaptive bitrate streaming, i.e., high video quality, shorter rebuffering time, and less bitrate switching. All three QoE components are normalized between 0 and 1 for ease of interpretation.

**Fragmento 23 - p. 11 - score 2:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia 6.2.2 Baseline ABR Controllers. In response to the growing interest in learning-based throughput predictors and ABR controllers in the research community, we included two representative learning- based ABR controllers for local deployment on top of the major baseline ABR controllers from numerical simulations: • Fugu [46]: Developed as part of the Puffer project, it features a learning-based stochastic throughput predictor, while its under- lying control algorithm is similar to MPC. • CausalSimRL [60]: A modern implementation of a reinforcement learning (RL)-based ABR controller Pensieve [22].

**Fragmento 24 - p. 11 - score 2:**

It is trained using CausalSim for the Puffer platform. 6.2.3 QoE Performance. Puffer employs structure similarity index measures (SSIM) [4] to quantify utility, thus to compare fairly us- ing Puffer, we adapt mean utility to normalized mean SSIM, i.e., ¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching rate, and QoE score remain the same. The aggregate statistics or QoE scores and individual QoE components across all sessions are shown in Figure 12. SODA outperforms the best baseline (Fugu) by 30.4% in terms of mean QoE score. More importantly, SODA is the only ABR controller that achieves low mean rebuffering ratio and switching rate simultaneously, which translates to superior smooth- ness of adaptive streaming.

**Fragmento 25 - p. 12 - score 2:**

ACKNOWLEDGMENTS We thank the anonymous reviewers and our shepherd for their valu- able feedback, as well as colleagues at Amazon Prime Video for their support with the production deployment of SODA. This work was funded by NSF under grants CAREER-204564, CCF-2325956, CNS- 1763617, CNS-1901137, CNS-2102963, CNS-2106299, CNS-2106403, CNS-2106463, CNS-2146814, CPS-2136197, and NGSDI-2105648, as well as an Amazon Research Award. The research of Yiheng Lin was additionally supported by Amazon AI4Science Fellowship and PIMCO Graduate Fellowship in Data Science. 624

**Fragmento 26 - p. 13 - score 2:**

doi: 10.4230/LIPIcs .APPROX-RANDOM.2015.96. [15] Te-Yuan Huang, Ramesh Johari, Nick McKeown, Matthew Trunnell, and Mark Watson. 2015. A Buffer-Based Approach to Rate Adaptation: Evidence from a Large Video Streaming Service. ACM SIGCOMM Computer Communication Review, 44, (Feb. 2015), 187–198, 4, (Feb. 2015). doi: 10.1145/2740070.2626296. [16] Yan Liu and Jack Y. B. Lee. 2015. An Empirical Study of Throughput Prediction in Mobile Data Networks. In 2015 IEEE Global Communications Conference (GLOBECOM), 1–6. doi: 10.1109/GLOCOM.2015.7417858. [17] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A Control- Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP. In Pro- ceedings of the 2015 ACM Conference on Special Interest Group on Data Commu- nication.


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 2 - score 7:**

2) Better QoE Across Empirical Evaluations. We evaluated SODA in three settings: numerical simulations, prototype evalua- tion, and production deployment within Amazon Prime Video serving actual users. Our numerical simulations show a 9.55% to Figure 2: BOLA’s [44] decision boundaries are spaced out for on-demand streaming, but tiny fluctuations in buffer level can cause bitrate switching for live streaming. 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE improvement compared to the state-of-the-art base- lines. Production live streaming experiments in Amazon Prime Video show that SODA reduced bitrate switching by a significant up to 88.8% and increased average stream viewing duration by up to 5.91% (> 5 minutes longer sessions) compared to a fine- tuned production baseline.

**Fragmento 2 - p. 3 - score 7:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Table 1: A qualitative summary of our key evaluation findings about SODA as compared to baseline ABR controllers. Controller Theorya Video Quality Rebuffering Time Switching Rate Deployability SODA Q + R + S high short ultra low high HYB [24] none high medium high high BOLA [44] Q + R high short high high Dynamic [36] Q + R high short medium high MPC [17] none high long low low Fugu [46] none high medium low low CausalSimRL [60] none high short high low aQ, R, S stand for theoretical guarantees for quality, rebuffering, and switching respectively. Figure 3: A RobustMPC session where the controller intention- ally rebuffers instead of lowering the bitrate.

**Fragmento 3 - p. 12 - score 6:**

9 CONCLUSION In this work, we propose a smoothness-optimized dynamic adaptive (SODA) controller that addresses this issue in a theoretically sound way. Thanks to SODA’s robustness against prediction errors and low runtime complexity, it is readily deployable in a wide range of production environments. Through numerical simulations and prototype evaluation, we show that SODA consistently outperforms the state-of-the-art baselines. More importantly, we deployed SODA in a major video streaming provider where SODA significantly re- duced bitrate switching by up to 88.8% compared to a fine-tuned production baseline. SODA’s novel time-based ABR formulation and theoretical insights shed new light on how to achieve consistent high-quality video streaming.

**Fragmento 4 - p. 1 - score 5:**

However, users often find frequent bitrate switching frustrating due to the resulting inconsistency in visual quality over time, es- pecially during live streaming when buffer lengths are short. In this paper, we propose a practical smoothness optimized dynamic adaptive (SODA) controller that specifically addresses this problem while remaining deployable. SODA is backed by theoretical guaran- tees and has shown superior performance in empirical evaluations. Specifically, our numerical simulations show a 9.55% to 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE im- provement compared to the state-of-the-art baselines. In order to be widely deployable, SODA performs bitrate horizon planning in poly- nomial time compared to brute force approaches that suffer from exponential complexity.

**Fragmento 5 - p. 1 - score 5:**

To demonstrate its real-world practicality, we deployed SODA on a wide range of devices within the production network of Amazon Prime Video. Production experiments show that SODA reduced bitrate switching by up to 88.8% and increased average stream viewing duration by up to 5.91% compared to a fine-tuned production baseline. CCS CONCEPTS • Information systems →Multimedia streaming; • Theory of computation →Online algorithms; Theory and algorithms for application domains. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.

**Fragmento 6 - p. 8 - score 5:**

This funnel approach allowed us to first systematically evaluate SODA against a variety of baselines in a wide range of controlled environments. Later, we narrowed the comparison target to a deployed and fine-tuned ABR controller in production using A/B tests on real user sessions. Performance Metrics. To maintain consistency in terms of perfor- mance metrics with prior works such as [17, 22, 24, 46], a similar definition of QoE is adopted that consists of mean utility, rebuffer- ing ratio, and switching rate. These correspond to the three main desired properties of adaptive bitrate streaming, i.e., high video quality, shorter rebuffering time, and less bitrate switching. All three QoE components are normalized between 0 and 1 for ease of interpretation.

**Fragmento 7 - p. 10 - score 5:**

6.2 Prototype Evaluation We next present emulation results from our local client-server deployment where we implemented SODA in the Puffer platform [46]. Thanks to Chrome DevTools’ new capability to throttle WebSocket requests [59], we could replay our network datasets directly in Chrome using WebDriver [63]. The results are intended to highlight the robustness of different ABR controllers under actual browser- based playback. For these experiments, we allowed a maximum buffer length of 15 seconds, as set by Puffer. 6.2.1 Experimental Setup. The video source was a news clip en- coded in five different resolutions (426 × 240, 640 × 360, 854 × 480, 1280 × 720, and 1920 × 1080) with a constant rate factor of 26 and a segment length of 2 seconds.

**Fragmento 8 - p. 11 - score 5:**

The experiment was run on three de- vice families, including (i) desktops/laptops (HTML5 browsers), (ii) smart TVs, and (iii) set-top boxes. On all three platforms, SODA used a simple sliding window-based throughput predictor. All devices were 20 seconds behind live action, so they could accumulate at most 20 seconds of buffer. To compare performance with a pro- duction tuned baseline, we conducted large-scale A/B experiments where customers were randomly assigned SODA or the production baseline controller. The experiment ran for more than 1 week with live streams delivered to more than 10 countries. In total, SODA sessions logged more than 50,000 streaming hours. Figure 13 shows SODA’s performance relative to the production deployed and tuned controller.

**Fragmento 9 - p. 2 - score 4:**

To understand the impact of bitrate switching, Figure 1 shows the re- lationship between the viewing percentage of a stream and bitrate switching rate for a sports event on a large-scale video streaming provider. To minimize potential confounders such as rebuffering and low quality, the plot is focused on short-lived sessions (< 25% of stream viewed) with at least HD quality and no rebuffering. The line of best fit shows that users watch < 10% of the stream when bitrate switching rate is > 20%. While our proposed ABR controller works for both on-demand and live streaming, our evaluations use live streams that represents a more challenging use case. Our Contributions. We propose a novel smoothness optimized dynamic adaptive (SODA) controller that provides theoretical QoE guarantees while exhibiting superior empirical performance in simulation, prototype, and production experiments.

**Fragmento 10 - p. 9 - score 4:**

In Section 4.2, we have showed that SODA is robust against prediction errors by design and does not require a sophisti- cated throughput predictor. We now demonstrate this empirically. First, we replaced the throughput predictor used in simulations with a perfect short-term throughput predictor. Next, we gradually introduced more and more white noise to the perfect throughput predictions and observed how different ABR controllers behave accordingly. This experiment was conducted on a random subset of our network datasets with a size of 10,000 sessions. Note that throughput prediction discounts were turned off for all ABR con- trollers to reveal their intrinsic robustness.1 The results are shown in Figure 11, from which we observe that all hybrid ABR controllers that take throughput predictions into account will inevitably be affected by prediction errors to some extent (BOLA is not affected since it is purely buffer-based).

**Fragmento 11 - p. 9 - score 4:**

In general, the more volatile network conditions are, the more the QoE performance of any ABR con- troller degrades, as evidenced by the trend in Figure 10 from left to right. Nonetheless, SODA consistently outperforms baseline ABR controllers under all network conditions. The improvement in terms of mean QoE scores compared to the best baseline across different network datasets ranges from 9.55% to 27.8%, which mainly stems from improvement in terms of smoothness (shorter rebuffering time and less bitrate switching). We discuss the improvement of SODA over each baseline ABR controller below: • SODA vs HYB. HYB is not as robust as SODA under volatile network conditions. In addition, it switches up to 215% more since it does not consider bitrate switching.

**Fragmento 12 - p. 11 - score 4:**

We highlight comparisons with the new baseline ABR controllers below: • SODA vs MPC & Fugu. MPC and Fugu are grouped together since, apart from the more sophisticated stochastic throughput pre- dictor, Fugu shares a similar underlying control algorithm with MPC. While they both achieve slightly higher mean utilities than SODA and reasonably low mean switching rates, these benefits are overshadowed by worse mean rebuffering ratios (230% and 104% worse respectively). Although Fugu partially mitigates the rebuffering issue due to its stochastic throughput predictor, it is still not robust enough for challenging network conditions. • SODA vs CausalSimRL. CausalSimRL achieves slightly higher mean utility than SODA and a reasonably low mean rebuffering ratio.

**Fragmento 13 - p. 11 - score 4:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia 6.2.2 Baseline ABR Controllers. In response to the growing interest in learning-based throughput predictors and ABR controllers in the research community, we included two representative learning- based ABR controllers for local deployment on top of the major baseline ABR controllers from numerical simulations: • Fugu [46]: Developed as part of the Puffer project, it features a learning-based stochastic throughput predictor, while its under- lying control algorithm is similar to MPC. • CausalSimRL [60]: A modern implementation of a reinforcement learning (RL)-based ABR controller Pensieve [22].

**Fragmento 14 - p. 11 - score 4:**

It is trained using CausalSim for the Puffer platform. 6.2.3 QoE Performance. Puffer employs structure similarity index measures (SSIM) [4] to quantify utility, thus to compare fairly us- ing Puffer, we adapt mean utility to normalized mean SSIM, i.e., ¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching rate, and QoE score remain the same. The aggregate statistics or QoE scores and individual QoE components across all sessions are shown in Figure 12. SODA outperforms the best baseline (Fugu) by 30.4% in terms of mean QoE score. More importantly, SODA is the only ABR controller that achieves low mean rebuffering ratio and switching rate simultaneously, which translates to superior smooth- ness of adaptive streaming.

**Fragmento 15 - p. 11 - score 4:**

Takeaways from Production Deployment. The production deployment shows that SODA is practical and can be widely deployed across different device types and network connections. Furthermore, to achieve its significant performance gains, it is sufficient for SODA to use simple sliding window-based throughput predictors. 7 RELATED WORK 7.1 Adaptive Bitrate Streaming Bitrate adaptation has received significant attention from the mul- timedia research community. Buffer-based controllers like BBA [15] and BOLA [36, 44] make bitrate decisions based on buffer occu- pancy, while hybrid controllers like HYB [24], MPC [17] and DYNAMIC [44] combine throughput predictions with buffer occupancy to make decisions.

**Fragmento 16 - p. 12 - score 4:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 12: The mean QoE scores, utilities, rebuffering ratios, and switching rates from local deployment. SODA again has the highest mean QoE score and unlike all other baselines, simultaneously achieves ultra low mean rebuffering ratio and switching rate. (Error bars represent 95% confidence intervals.) Figure 13: The change in mean viewing durations (higher is better), bitrates (higher is better), rebuffering ratios (lower is better), and switching rates (lower is better) of SODA compared to the production baseline. designs (QEDs) to quantify the causal (adverse) impact of startup delay, rebuffering, and failures on user engagement, abandonment, and repeat viewership.

**Fragmento 17 - p. 13 - score 4:**

ACM, New York, NY, USA, (Aug. 2015), 325–338. isbn: 9781450335423. doi: 10.1145/2785956.2787486. [18] Mojgan Ghasemi, Partha Kanuparthy, Ahmed Mansy, Theophilus Benson, and Jennifer Rexford. 2016. Performance Characterization of a Commercial Video Streaming Service. In Proceedings of the 2016 Internet Measurement Conference. ACM, New York, NY, USA, (Nov. 2016), 499–511. isbn: 9781450345262. doi: 10.1145/2987443.2987481. [19] he1enh. 2016. Reproducing Network Research. (May 2016). https://reproducin gnetworkresearch.wordpress.com/2016/05/30/cs244-16-failed-experiments- with-fastmpc-integrating-rate-based-adaptive-streaming-into-vlc/. [20] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang, Tao Liu, and Bruno Sinopoli.

**Fragmento 18 - p. 2 - score 3:**

See Table 1 for a summary of our key findings about SODA as compared to baseline ABR controllers. 3) Robustness Against Throughput Prediction Errors. Most ABR controllers rely on and are sensitive to predictions of the future network throughput. Our SOCO framework allows us to design robust ABR controllers that are provably robust against prediction errors. Specifically, we show that SODA has the ex- ponentially decaying perturbation property [49, 55, 56], i.e., the future impact of prediction errors decay rapidly over time. A key to our proof methodology is that we shifted from the con- ventional segment-based ABR formulation and adopted a novel time-based perspective. 4) Efficient Implementation for Production Deployment.

**Fragmento 19 - p. 3 - score 3:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 20 - p. 3 - score 3:**

Past works have shown that RobustMPC incurs 26% more rebuffering events unless paired with a sophisticated throughput predictor [46, 50]. Simi- larly, learning-based controllers like Pensieve tend to degrade in performance when trained for realistic network conditions encountered in the wild [24]. In practice, accurate throughput predictions are hard because of several factors, including (i) de- vice and OS level inefficiencies [18], (ii) stop-start nature of video requests which do not interact well with TCP [8, 18], and (iii) volatile network conditions typical in production networks [1, 5, 45]. To make matters worse, sophisticated throughput predictors are themselves not necessarily accurate [16] and are challenging to deploy due to device level bottlenecks [58].

**Fragmento 21 - p. 4 - score 3:**

• To remain computationally efficient, SODA leverages an efficient approximate solver (see Section A.5 for proof and Algorithm 1 for implementation), that only requires evaluation of monotonic bitrate sequences (Section 4.3), which reduces the computational cost by two orders of magnitude over a brute-force solver. 3 SODA OVERVIEW Given the design gaps, opportunities, and requirements, we set out to design a theoretically sound adaptive bitrate streaming (ABR) controller that minimizes bitrate switching without compromis- ing video quality or increasing rebuffering time, thus providing a smooth viewing experience. To accomplish this, we deviate from the conventional segment-based ABR formulation and derive theo- retical insights from a time-based ABR formulation.

**Fragmento 22 - p. 4 - score 3:**

• 𝑏(𝑥𝑛) is the buffer cost, which aims to stabilize the buffer level around a target level ¯𝑥, i.e., 𝑏(𝑥𝑛) = ( ( ¯𝑥−𝑥𝑛)2 𝑥𝑛≤¯𝑥 𝜖(𝑥𝑛−¯𝑥)2 𝑥𝑛> ¯𝑥, where 𝜖< 1 is a small constant. Note that we purposely do not model the rebuffering time explicitly to avoid the pitfalls encoun- tered by RobustMPC (Section 2) and as we show later, this helps SODA achieve theoretical performance guarantees (Section 4.2). • 𝑐(𝑟𝑛,𝑟𝑛−1) is the switching cost from the previous bitrate to the current bitrate, e.g., 𝑐(𝑟𝑛,𝑟𝑛−1) = (𝑣(𝑟𝑛) −𝑣(𝑟𝑛−1))2. Coefficients 𝛽and 𝛾are positive weights for the buffer and the switching cost respectively based on user preferences. The choices for the distortion and switching cost functions are flexible.

**Fragmento 23 - p. 5 - score 3:**

However, segment-based controllers such as MPC [17] and Fugu [46] intertwine throughput predictions and bi- trate decisions in non-causal ways. In these designs, the throughput prediction horizon spans shorter periods of clock time when low bitrate is selected compared to when high bitrate is selected. In fact, their underlying assumption about the validity of the throughput prediction horizon can vary by 𝑟max/𝑟min. By contrast, the way we incorporate throughput predictions into SODA does not suffer from this issue. Specifically, just before each time interval, the controller is given access to a (not necessarily accurate) throughput prediction for the next 𝐾time intervals from a black-box throughput predictor.

**Fragmento 24 - p. 6 - score 3:**

SODA achieves a dynamic regret of 𝑂( √ E𝑁+ E). The formal statement of Theorem 4.2 is given in Theorem A.8 in Appendix A. Theorem 4.2 shows that, if the buffer costs are “steep” and the prediction errors on the bandwidth are relatively small, SODA can achieve a sequence of buffer levels that stay safely away from the boundaries of buffer constraint [0,𝑥max]. The dynamic regret of SODA depends on the magnitude of the prediction errors and the regret improves when the errors become smaller. SODA acquires this guarantee thanks to its maintenance of the buffer near a target level ¯𝑥. In contrast, RobustMPC [17] doesn’t offer the same performance guarantee, thus even small bandwidth prediction errors can cause the video to rebuffer if the buffer level is near zero.

**Fragmento 25 - p. 7 - score 3:**

Both predictors have a high mean correlation (around 50%) in the immediate future but a very low mean correlation (around 15%) in the far future. Algorithm 1: SODA’s efficient approximate optimization solver. SearchDown is omitted for brevity due to symmetry. The current buffer level and the previous bitrate are denoted by 𝑥0 and 𝑟0 respectively. function Search( ˆ𝜔,𝑥0,𝑟0, 𝐾) (𝑟∗up, obj∗up) ←SearchUp( ˆ𝜔,𝑥0,𝑟0, 𝐾) (𝑟∗ down, obj∗ down) ←SearchDown( ˆ𝜔,𝑥0,𝑟0, 𝐾) return 𝑟∗up ≠null ∧obj∗up < obj∗ down ? 𝑟∗up : 𝑟∗ down function SearchUp( ˆ𝜔,𝑥0,𝑟0, 𝐾) 𝑟∗ 1 ←null, obj∗←∞ foreach 𝑟1 ∈{𝑟∈R : 𝑟> 𝑟0} 𝑥1 ←𝑥0 + ˆ𝜔Δ𝑡/𝑟1 −Δ𝑡 if 𝑥1 < 0 then continue obj ←𝑣(𝑟1) · ˆ𝜔Δ𝑡/𝑟1 + 𝛽· 𝑏(𝑥1) + 𝛾· 𝑐(𝑟1,𝑟0) if 𝐾> 1 then (𝑟∗ 2, Δobj∗) ←SearchUp( ˆ𝜔,𝑥1,𝑟1, 𝐾−1) if 𝑟∗ 2 = null then continue obj ←obj + Δobj∗ if obj < obj∗then 𝑟∗ 1 ←𝑟1, obj∗←obj return (𝑟∗ 1, obj∗) case in FastMPC [17], however, this is neither flexible nor scalable in practice.

**Fragmento 26 - p. 8 - score 3:**

Empirical results are shown in Figure 8 to validate the near- optimality of bitrate decisions produced by the approximate solver. For each algorithm configuration, we uniformly sample a million situations with different throughputs, buffer levels, and previous bitrates. Then, we count the probability that the bitrate decision produced by the approximate solver is different from that produced by the brute-force solver. The difference is negligible for a reason- able switching cost weight, e.g., below 5% for 𝐾= 4 and a relative switching cost weight of 2. Throughout the evaluation sections, we use this efficient implementation of SODA. 6 EVALUATION To thoroughly evaluate SODA’s performance, we conducted three levels of empirical evaluation: (i) large-scale numerical simulations, (ii) prototype evaluation in Puffer [46], and (iii) production deploy- ment in Amazon Prime Video.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 2 - score 8:**

2) Better QoE Across Empirical Evaluations. We evaluated SODA in three settings: numerical simulations, prototype evalua- tion, and production deployment within Amazon Prime Video serving actual users. Our numerical simulations show a 9.55% to Figure 2: BOLA’s [44] decision boundaries are spaced out for on-demand streaming, but tiny fluctuations in buffer level can cause bitrate switching for live streaming. 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE improvement compared to the state-of-the-art base- lines. Production live streaming experiments in Amazon Prime Video show that SODA reduced bitrate switching by a significant up to 88.8% and increased average stream viewing duration by up to 5.91% (> 5 minutes longer sessions) compared to a fine- tuned production baseline.

**Fragmento 2 - p. 11 - score 8:**

First, notice that SODA consistently improves all the metrics across all device families, reducing the frequency of bitrate switching on set-top boxes by 88.8%. SODA really shines on HTML5 browsers where it reduced the mean rebuffering ratio by up to 53.0% in addition to 81.8% reduction in switching. This is because HTML5 browsers experience more volatility in network conditions compared to smart TVs and set-top boxes and thus present greater opportunity for improvement. Finally, notice that on all three platforms, the average duration of session increased, with 5.91% improvement on set-top boxes. Live streaming sessions for sports events routinely span multiple hours (e.g., 2-hour soccer broadcast, 3.5-hour cricket broadcast), so a 5.91% increase translates to more than 5 minutes duration.

**Fragmento 3 - p. 12 - score 7:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 12: The mean QoE scores, utilities, rebuffering ratios, and switching rates from local deployment. SODA again has the highest mean QoE score and unlike all other baselines, simultaneously achieves ultra low mean rebuffering ratio and switching rate. (Error bars represent 95% confidence intervals.) Figure 13: The change in mean viewing durations (higher is better), bitrates (higher is better), rebuffering ratios (lower is better), and switching rates (lower is better) of SODA compared to the production baseline. designs (QEDs) to quantify the causal (adverse) impact of startup delay, rebuffering, and failures on user engagement, abandonment, and repeat viewership.

**Fragmento 4 - p. 1 - score 5:**

To demonstrate its real-world practicality, we deployed SODA on a wide range of devices within the production network of Amazon Prime Video. Production experiments show that SODA reduced bitrate switching by up to 88.8% and increased average stream viewing duration by up to 5.91% compared to a fine-tuned production baseline. CCS CONCEPTS • Information systems →Multimedia streaming; • Theory of computation →Online algorithms; Theory and algorithms for application domains. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.

**Fragmento 5 - p. 3 - score 5:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 6 - p. 10 - score 5:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 10: The mean QoE scores, utilities, rebuffering ratios and switching rates of SODA and baseline ABR controllers under each network dataset. The Puffer dataset is split into four quarters according the throughput variance (Q1 being lowest while Q4 being highest). SODA has consistently higher mean QoE scores and lower switching rates than all baseline ABR controllers under all network conditions. (Error bars represent 95% confidence intervals.) Figure 11: The mean QoE scores for SODA and baseline ABR controllers under variable amounts of white noise. (The error bars represent 95% confidence intervals.) the idea that a practical deployment of SODA does not require a sophisticated throughput predictor.2 2In practice, we observe that EMA predictor is actually much better than a perfect short-term predictor with 30% white noise because the noise patterns are different, which means that real gap is less than 10%.

**Fragmento 7 - p. 1 - score 4:**

To achieve this, a video source is encoded at different bitrates corresponding to different resolutions, e.g., 720p, 1080p, 1440p, etc. Each encod- ing is in turn temporally partitioned into a sequence of segments, e.g., 2 seconds of video content. An ABR controller inside a user’s video player then selects a suitable bitrate for each segment. Finally, downloaded segments are stored in a buffer, till they are rendered. Past studies have shown that a user’s QoE is maximized by de- livering the video at the highest possible quality with minimal rebuffering and bitrate switching. It has been shown that a 1% in- crease in rebuffering time is correlated with a 3-minute reduction in the viewing duration [7] and frequent bitrate switching is strongly correlated with a user abandoning the session [21].

**Fragmento 8 - p. 2 - score 4:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 1: Video stream duration is negatively correlated with bitrate switching rate. Users watch < 10% of the stream when bitrate switching rate is > 20%. switching, is non-trivial as they are locked in a three-way trade-off. An ideal ABR controller seeks to push the trade-off boundary and optimize all three QoE components simultaneously. Between on-demand and live streaming, the latter is more chal- lenging as the player buffer is restricted to 10 - 20 seconds (to remain close to actual live action), which is in contrast to 60 - 180 seconds of buffer in on-demand streaming. Consequently, live streaming has higher susceptibility to rebuffering and bitrate switching.

**Fragmento 9 - p. 3 - score 4:**

Notice that beyond 70 seconds, RobustMPC re- peatedly rebuffers but continues to download the highest bitrate (Figure 3 bottom plot), resulting in 29 rebuffering events over 200 seconds. Strikingly, this behavior is in fact the optimal behavior under RobustMPC’s objective function which tolerates rebuffering to prevent bitrate switches. On the surface, this suggests higher rebuffering penalty in the objective function, however, higher penalties only reduce the duration of these tolerable rebuffers but do not eliminate them. Indeed, past work has empirically shown that even a 20× buffering penalty has marginal impact [24]. • Variance in network conditions or throughput prediction errors are not well tolerated by existing controllers.

**Fragmento 10 - p. 7 - score 4:**

A lookup table is specific to a particular set of bitrates, maximum player buffer, segment durations and byte sizes etc. thus needs to be recomputed when any of these quantities change. Fur- thermore, computing this lookup in live streaming is undesirable due to the additional computational and latency overhead it incurs. Instead, we opt for an efficient approximate solver. SODA’s approximate solver is designed to take advantage of the structure of the optimal solution presented in Section 4.3. Instead of searching through all possible bitrate sequences in the prediction horizon, the approximate solver only considers monotonic bitrate sequences, i.e., it imposes an additional constraint that 𝑟𝑛−1 ≤𝑟𝑛≤ .

**Fragmento 11 - p. 9 - score 4:**

• SODA vs BOLA & Dynamic. As mainly buffer-based ABR con- trollers, BOLA and Dynamic are fairly robust against volatile net- work conditions. Dynamic’s performance is what one would ex- pect in a typical production environment. Nonetheless, SODA is able to achieve similar mean utilities without sacrificing mean rebuffering ratios, proving its outstanding robustness as a hybrid ABR controller. Where SODA really shines though is its signifi- cantly lower mean switching rates. Despite Dynamic’s switch- ing avoidance heuristic, SODA cuts down mean switching rates by as much as 70.4%, which demonstrates the superiority of theoretically-sound design. • SODA vs MPC. MPC has high mean utilities and low mean switching rates under stable network conditions (see Puffer (Q1 variance) in Figure 10).

**Fragmento 12 - p. 9 - score 4:**

However, the performance of MPC is tightly coupled with the intrinsic volatility of network conditions. Specifically, MPC suffers a lot in terms of mean rebuffering ratios especially under mobile network conditions. By contrast, SODA does not have this issue since it is robust against prediction errors by design, making it much more suitable for production deployment. 6.1.4 Intrinsic Sensitivity to Prediction Accuracy. In an effort to im- prove throughput prediction accuracy, several prior works have fo- cused on designing more sophisticated throughput predictors such as C2SP [20], Fugu [46], and Xatu [50]. While these throughput pre- dictors may offer higher prediction accuracy, they are complex and difficult to deploy, especially on compute or memory constrained devices [58].

**Fragmento 13 - p. 9 - score 4:**

In general, the more volatile network conditions are, the more the QoE performance of any ABR con- troller degrades, as evidenced by the trend in Figure 10 from left to right. Nonetheless, SODA consistently outperforms baseline ABR controllers under all network conditions. The improvement in terms of mean QoE scores compared to the best baseline across different network datasets ranges from 9.55% to 27.8%, which mainly stems from improvement in terms of smoothness (shorter rebuffering time and less bitrate switching). We discuss the improvement of SODA over each baseline ABR controller below: • SODA vs HYB. HYB is not as robust as SODA under volatile network conditions. In addition, it switches up to 215% more since it does not consider bitrate switching.

**Fragmento 14 - p. 1 - score 3:**

However, users often find frequent bitrate switching frustrating due to the resulting inconsistency in visual quality over time, es- pecially during live streaming when buffer lengths are short. In this paper, we propose a practical smoothness optimized dynamic adaptive (SODA) controller that specifically addresses this problem while remaining deployable. SODA is backed by theoretical guaran- tees and has shown superior performance in empirical evaluations. Specifically, our numerical simulations show a 9.55% to 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE im- provement compared to the state-of-the-art baselines. In order to be widely deployable, SODA performs bitrate horizon planning in poly- nomial time compared to brute force approaches that suffer from exponential complexity.

**Fragmento 15 - p. 2 - score 3:**

ABR controllers deployed in the field need to work on a wide range of client devices, including low-end ones with limited computa- tional resources. Many ABR controllers proposed in the research literature do not meet the efficiency bar for a production de- ployment and are never implemented in practice. We maximized SODA’s runtime and deployment practicality by devising a com- putationally efficient method to search for near-optimal bitrate decisions, which reduced the runtime complexity from exponen- tial to polynomial, e.g., about 200 iterations max in practice. In addition, we made SODA robust against throughput prediction errors by design, thus eliminating the need for sophisticated computationally-intensive throughput predictors.

**Fragmento 16 - p. 4 - score 3:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. sacrificing video quality or sustained playback, (ii) be robust against volatile network conditions, and (iii) be easy to deploy in practice. Before delving into the details in the remainder of the paper, we provide a brief overview of how SODA satisfies these requirements: • SODA leverages SOCO to balance the trade-off between video qual- ity, sustained playback without rebuffers, and bitrate smoothness without frequent switches. Importantly, SODA focuses on steer- ing the buffer level towards a target rather than weighing video quality against rebuffering duration (see Section 3.1). • To achieve robustness against throughput variability, SODA is de- signed to satisfy the exponentially decaying perturbation property, which guarantees that SODA never operates too far away from the optimal trajectory in the face of prediction errors (see Section 4.2).

**Fragmento 17 - p. 7 - score 3:**

5.1 Segment-Based Schema SODA is intrinsically a time-based controller, but in practice, a video must be downloaded segment by segment according to the MPEG- DASH standard. To reconcile with this requirement, we keep the optimization phase as is in the time-based format and empirically set Δ𝑡to be equal to the segment length. This choice is justified by the fact that in the steady state, the download time of a video segment is expected to be close to the segment length or much less than that [29]. To further minimize the likelihood of committing to a bitrate for significantly longer than Δ𝑡, we introduce another heuristic that the controller must select a bitrate no higher than min{𝑟∈R : 𝑟≥ˆ𝜔}. 5.2 Incorporating Predictions Robustly According to Section 4.2, SODA is robust against prediction errors by design as long as there is no systematic bias in prediction er- rors.

**Fragmento 18 - p. 8 - score 3:**

The precise definitions are as follows: • Mean Utility: Unless otherwise noted, we use the commonly- used logarithmic utility function: ¯𝑣= 1 𝑁 𝑁 ∑︁ 𝑖=1 log(𝑟𝑖/𝑟min) log(𝑟max/𝑟min) . • Rebuffering Ratio: The ratio of the total rebuffering time to the session duration, i.e., 𝜌rebuf = 𝑇rebuf/𝑇. • Switching Rate: Bitrate switch count divided by segment count minus one, i.e., 𝑝switch = 𝑁switch/(𝑁−1). The QoE score is simply a linear combination of the three QoE components, i.e., QoE = ¯𝑣−𝛽· 𝜌rebuf −𝛾· 𝑝switch. In this work, we chose 𝛽= 10 and 𝛾= 1 to reflect the high importance of minimizing rebuffering time. To establish fair comparisons, we report the individual QoE components along with the QoE score.

**Fragmento 19 - p. 11 - score 3:**

We highlight comparisons with the new baseline ABR controllers below: • SODA vs MPC & Fugu. MPC and Fugu are grouped together since, apart from the more sophisticated stochastic throughput pre- dictor, Fugu shares a similar underlying control algorithm with MPC. While they both achieve slightly higher mean utilities than SODA and reasonably low mean switching rates, these benefits are overshadowed by worse mean rebuffering ratios (230% and 104% worse respectively). Although Fugu partially mitigates the rebuffering issue due to its stochastic throughput predictor, it is still not robust enough for challenging network conditions. • SODA vs CausalSimRL. CausalSimRL achieves slightly higher mean utility than SODA and a reasonably low mean rebuffering ratio.

**Fragmento 20 - p. 11 - score 3:**

It is trained using CausalSim for the Puffer platform. 6.2.3 QoE Performance. Puffer employs structure similarity index measures (SSIM) [4] to quantify utility, thus to compare fairly us- ing Puffer, we adapt mean utility to normalized mean SSIM, i.e., ¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching rate, and QoE score remain the same. The aggregate statistics or QoE scores and individual QoE components across all sessions are shown in Figure 12. SODA outperforms the best baseline (Fugu) by 30.4% in terms of mean QoE score. More importantly, SODA is the only ABR controller that achieves low mean rebuffering ratio and switching rate simultaneously, which translates to superior smooth- ness of adaptive streaming.

**Fragmento 21 - p. 11 - score 3:**

Since then the quality of video delivery is a well studied topic with early work on the Akamai Stream Ana- lyzer system which defined metrics such as startup time, rebuffer ratio, bitrate and failures etc and measured these metrics using data derived from video players deployed around the world [3, 66]. Sub- sequently, [7] showed that a 1% increase in rebuffering correlated with a 3-minute reduction in the amount of time users streamed live content. A study on YouTube [21] found that bitrate fluctua- tions strongly correlate with a user abandoning the session. Beyond correlations, the first study [9] to establish a causal relationship between video quality and user behavior used quasi-experimental 623

**Fragmento 22 - p. 12 - score 3:**

9 CONCLUSION In this work, we propose a smoothness-optimized dynamic adaptive (SODA) controller that addresses this issue in a theoretically sound way. Thanks to SODA’s robustness against prediction errors and low runtime complexity, it is readily deployable in a wide range of production environments. Through numerical simulations and prototype evaluation, we show that SODA consistently outperforms the state-of-the-art baselines. More importantly, we deployed SODA in a major video streaming provider where SODA significantly re- duced bitrate switching by up to 88.8% compared to a fine-tuned production baseline. SODA’s novel time-based ABR formulation and theoretical insights shed new light on how to achieve consistent high-quality video streaming.

**Fragmento 23 - p. 4 - score 2:**

. . ,𝜔𝑁). For example, consider the throughput function shown in Figure 4. In the time-based formulation, we naturally have 𝜔1 = 4, 𝜔2 = 1, and 𝜔3 = 𝜔4 = 2 Mb/s given Δ𝑡= 1 s. By contrast, in the segment-based formulation, the throughput sequence be- comes dependent on the bitrate sequence. Assuming the segment duration is also 𝐿= 1 s, if the controller chooses 𝑟1 = 2 Mb/s and 𝑟2 = 2.5 Mb/s, then it takes 0.5 and 1 s to download the first and sec- ond segments respectively, resulting in 𝜔1 = 4 and 𝜔2 = 2.5 Mb/s. As such, the segment based formulation gets causally biased due to bitrate selection 𝑟1, ...,𝑟𝑁, which in turn makes it difficult to theoretically analyze the design [61]. Why Not Model Rebuffering Directly?

**Fragmento 24 - p. 7 - score 2:**

Given the diverse network conditions in the wild, we prefer simple throughput predictors which makes SODA highly deployable since there is no dependence on complex throughput predictors. In practice, we observe that prediction accuracy degrades as the prediction horizon increases (see Figure 7). Therefore, we limit the prediction horizon length to at most 10 s. This is also supported by our finding in Section 4.1 that a longer prediction horizon yields diminishing returns. 5.3 Efficient Approximate Solver At SODA’s core is the predictive optimization problem described in Section 3.3. Unfortunately, solving this problem on the fly is computationally challenging. One may propose enumerating all combinations of discretized throughputs, buffer levels, and previous bitrates in the form of an offline computed lookup table, as is the Figure 7: We profiled the performance of the two throughput predictors shipped with dash.js [64], i.e., moving average predictor and exponential moving average predictor.

**Fragmento 25 - p. 8 - score 2:**

Empirical results are shown in Figure 8 to validate the near- optimality of bitrate decisions produced by the approximate solver. For each algorithm configuration, we uniformly sample a million situations with different throughputs, buffer levels, and previous bitrates. Then, we count the probability that the bitrate decision produced by the approximate solver is different from that produced by the brute-force solver. The difference is negligible for a reason- able switching cost weight, e.g., below 5% for 𝐾= 4 and a relative switching cost weight of 2. Throughout the evaluation sections, we use this efficient implementation of SODA. 6 EVALUATION To thoroughly evaluate SODA’s performance, we conducted three levels of empirical evaluation: (i) large-scale numerical simulations, (ii) prototype evaluation in Puffer [46], and (iii) production deploy- ment in Amazon Prime Video.

**Fragmento 26 - p. 8 - score 2:**

6.1 Numerical Simulations To perform large-scale numerical simulations, we implemented a highly optimized ABR simulator in C++ derived from Sabre [36]. The simulation accuracy of Sabre has been empirically validated against dash.js [64], the reference player for MPEG-DASH. We configured the simulator to allow a maximum buffer length of 20 seconds to replicate the typical live streaming conditions. 6.1.1 Experimental Setup. Our network dataset consists of about 38,000 hours of throughput traces compiled from the following three public sources: • Puffer Dataset [46]: We downloaded and parsed all throughput traces from the Puffer platform during the time period of January 2023 to June 2023. • 5G Dataset [41]: A 5G network dataset from a major Irish mobile operator under both static and moving scenarios while down- loading online content.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 12 - score 4:**

8 LIMITATIONS AND FUTURE WORK An emerging genre (but, still a small fraction) of live streaming is ultra-low latency live streams where the delay between the capture of an event and its display to the user is required to be of the order of a few seconds, as opposed to 10 to 20 seconds for the traditional live streams used in our current work. In future work, we would like to study if our SOCO-based strategy can be adapted for ultra- low latency live streams with buffer lengths in the order of a few seconds. The main challenge with ultra-small buffer sizes is that it is harder to prevent rebuffering and bitrate switching in this regime as the ABR controller needs to react to network fluctuations in a significantly shorter amount of time.

**Fragmento 2 - p. 2 - score 3:**

ABR controllers deployed in the field need to work on a wide range of client devices, including low-end ones with limited computa- tional resources. Many ABR controllers proposed in the research literature do not meet the efficiency bar for a production de- ployment and are never implemented in practice. We maximized SODA’s runtime and deployment practicality by devising a com- putationally efficient method to search for near-optimal bitrate decisions, which reduced the runtime complexity from exponen- tial to polynomial, e.g., about 200 iterations max in practice. In addition, we made SODA robust against throughput prediction errors by design, thus eliminating the need for sophisticated computationally-intensive throughput predictors.

**Fragmento 3 - p. 2 - score 3:**

See Table 1 for a summary of our key findings about SODA as compared to baseline ABR controllers. 3) Robustness Against Throughput Prediction Errors. Most ABR controllers rely on and are sensitive to predictions of the future network throughput. Our SOCO framework allows us to design robust ABR controllers that are provably robust against prediction errors. Specifically, we show that SODA has the ex- ponentially decaying perturbation property [49, 55, 56], i.e., the future impact of prediction errors decay rapidly over time. A key to our proof methodology is that we shifted from the con- ventional segment-based ABR formulation and adopted a novel time-based perspective. 4) Efficient Implementation for Production Deployment.

**Fragmento 4 - p. 6 - score 3:**

This result implies that SODA’s performance ap- proaches that of the optimal sequence of decisions exponentially fast in the prediction horizon size 𝐾; thus, only a small prediction horizon length is necessary to obtain good performance. 4.2 Inexact Predictions We now relax the exact prediction assumption to prove SODA’s robustness to a certain level of prediction errors thanks to its expo- nentially decaying perturbation property. Theorem 4.2. [Informal] Suppose the prediction error at each step is bounded above. The buffer level of SODA will never hit the constraint boundary, i.e., 0 < 𝑥𝑛< 𝑥max. Further, define E = 𝜌2𝐾𝑁+ Í𝐾 𝜅=1 𝜌𝜅𝐸𝜅, where 𝐸𝜅is the total squared error for predicting 𝜅steps into the future.

**Fragmento 5 - p. 7 - score 3:**

5.1 Segment-Based Schema SODA is intrinsically a time-based controller, but in practice, a video must be downloaded segment by segment according to the MPEG- DASH standard. To reconcile with this requirement, we keep the optimization phase as is in the time-based format and empirically set Δ𝑡to be equal to the segment length. This choice is justified by the fact that in the steady state, the download time of a video segment is expected to be close to the segment length or much less than that [29]. To further minimize the likelihood of committing to a bitrate for significantly longer than Δ𝑡, we introduce another heuristic that the controller must select a bitrate no higher than min{𝑟∈R : 𝑟≥ˆ𝜔}. 5.2 Incorporating Predictions Robustly According to Section 4.2, SODA is robust against prediction errors by design as long as there is no systematic bias in prediction er- rors.

**Fragmento 6 - p. 7 - score 3:**

A lookup table is specific to a particular set of bitrates, maximum player buffer, segment durations and byte sizes etc. thus needs to be recomputed when any of these quantities change. Fur- thermore, computing this lookup in live streaming is undesirable due to the additional computational and latency overhead it incurs. Instead, we opt for an efficient approximate solver. SODA’s approximate solver is designed to take advantage of the structure of the optimal solution presented in Section 4.3. Instead of searching through all possible bitrate sequences in the prediction horizon, the approximate solver only considers monotonic bitrate sequences, i.e., it imposes an additional constraint that 𝑟𝑛−1 ≤𝑟𝑛≤ .

**Fragmento 7 - p. 8 - score 3:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 8: The probability that the bitrate decision produced by the approximate solver is different from that produced by the brute-force solver quickly converges to 0 as switching cost weight increases. The approximate solver reduces the time complexity from O(|R|𝐾) (exponential in 𝐾) in the case of a brute-force search over all possi- ble bitrate sequences in the prediction horizon down to O  |R|+𝐾 𝐾  (polynomial in 𝐾) and has a space complexity of O(𝐾) only. The time complexity can be further reduced by limiting extreme bitrate switches. In practice, SODA searches through at most around 200 bitrate sequences. According to our production deployment expe- rience, the approximate solver did not impose a runtime burden even on low-end devices such as set-top boxes, which shows that SODA is highly practical.

**Fragmento 8 - p. 9 - score 3:**

However, the performance of MPC is tightly coupled with the intrinsic volatility of network conditions. Specifically, MPC suffers a lot in terms of mean rebuffering ratios especially under mobile network conditions. By contrast, SODA does not have this issue since it is robust against prediction errors by design, making it much more suitable for production deployment. 6.1.4 Intrinsic Sensitivity to Prediction Accuracy. In an effort to im- prove throughput prediction accuracy, several prior works have fo- cused on designing more sophisticated throughput predictors such as C2SP [20], Fugu [46], and Xatu [50]. While these throughput pre- dictors may offer higher prediction accuracy, they are complex and difficult to deploy, especially on compute or memory constrained devices [58].

**Fragmento 9 - p. 1 - score 2:**

However, users often find frequent bitrate switching frustrating due to the resulting inconsistency in visual quality over time, es- pecially during live streaming when buffer lengths are short. In this paper, we propose a practical smoothness optimized dynamic adaptive (SODA) controller that specifically addresses this problem while remaining deployable. SODA is backed by theoretical guaran- tees and has shown superior performance in empirical evaluations. Specifically, our numerical simulations show a 9.55% to 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE im- provement compared to the state-of-the-art baselines. In order to be widely deployable, SODA performs bitrate horizon planning in poly- nomial time compared to brute force approaches that suffer from exponential complexity.

**Fragmento 10 - p. 3 - score 2:**

Workarounds such as pre-computed lookup tables [17] are impractical for live streaming where the video is not available a priori. In a simi- lar vein, learning-based controllers such as Pensieve [22] work optimally when trained specifically for a given set of bitrates, segment duration, network conditions, etc. Given in-the-wild diversity and its evolving nature, ensuring this specificity im- poses a significant operational overhead. Furthermore, even if specifically trained, achieving performance guarantees with these learning-based controllers is shown to be challenging [24]. • Existing ABR controllers naively reduce bitrate switching at the expense of low video quality or more rebuffering. To demonstrate this, Figure 3 shows a RobustMPC session with the exact setup used by [17, 22].

**Fragmento 11 - p. 5 - score 2:**

Our approach is analogous to the use of control barrier functions to ensure safety properties in control systems [30]. • Modeling rebuffering time directly makes the controller vulnera- ble to throughput prediction errors. Under a direct rebuffering objective, as long as the buffer level is above zero, there will be no penalty for the controller, even if the buffer level is dangerously close to 0. As a result, even small throughput prediction errors can lead to unexpected rebuffering. 3.2 Incorporating Throughput Predictions In addition to facilitating theoretical analysis, our time-based formu- lation is crucial to ensuring the validity of throughput predictions over the prediction horizon. An important observation is that bi- trate decisions have no causal impact on how long the throughput predictions are valid for.

**Fragmento 12 - p. 6 - score 2:**

This assumption is used to eliminate extreme boundary cases in the analysis, but we find SODA empirically performs very well even when this assumption is not strictly satisfied. In this section, we set Δ𝑡= 1, R = [𝑟min,𝑟max], and 𝑣(𝑟) = 1/𝑟. Our results can apply to other distortion cost functions, e.g., 𝑣(𝑟) = log(𝑟max/𝑟), as long as certain regularity conditions hold; see Appendix B for a discussion. 4.1 Exact Predictions When the bandwidth predictions are accurate, a small prediction horizon is sufficient for SODA to achieve near-optimal performance. In practice, it is desirable to use a relatively small prediction hori- zon for a predictive controller like SODA because prediction errors grow dramatically as we predict further into the future.

**Fragmento 13 - p. 6 - score 2:**

Fortunately, the exponential decay property that ensures good performance with only a few predictions. More formally, we present a theorem showing that a small prediction horizon is sufficient for SODA to achieve near-optimal performance when the predictions within this window are accurate (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1). Theorem 4.1. [Informal] When the predictions of the bandwidth in future 𝐾steps are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾≥𝑂(1), SODA achieves a dynamic regret of 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 +𝑂(𝜌𝐾), where 𝜌< 1 is the decay factor of the exponentially decaying perturbation property. The formal statement of Theorem 4.1 is given in Theorem A.3 in Appendix A.

**Fragmento 14 - p. 7 - score 2:**

Given the diverse network conditions in the wild, we prefer simple throughput predictors which makes SODA highly deployable since there is no dependence on complex throughput predictors. In practice, we observe that prediction accuracy degrades as the prediction horizon increases (see Figure 7). Therefore, we limit the prediction horizon length to at most 10 s. This is also supported by our finding in Section 4.1 that a longer prediction horizon yields diminishing returns. 5.3 Efficient Approximate Solver At SODA’s core is the predictive optimization problem described in Section 3.3. Unfortunately, solving this problem on the fly is computationally challenging. One may propose enumerating all combinations of discretized throughputs, buffer levels, and previous bitrates in the form of an offline computed lookup table, as is the Figure 7: We profiled the performance of the two throughput predictors shipped with dash.js [64], i.e., moving average predictor and exponential moving average predictor.

**Fragmento 15 - p. 12 - score 2:**

9 CONCLUSION In this work, we propose a smoothness-optimized dynamic adaptive (SODA) controller that addresses this issue in a theoretically sound way. Thanks to SODA’s robustness against prediction errors and low runtime complexity, it is readily deployable in a wide range of production environments. Through numerical simulations and prototype evaluation, we show that SODA consistently outperforms the state-of-the-art baselines. More importantly, we deployed SODA in a major video streaming provider where SODA significantly re- duced bitrate switching by up to 88.8% compared to a fine-tuned production baseline. SODA’s novel time-based ABR formulation and theoretical insights shed new light on how to achieve consistent high-quality video streaming.

**Fragmento 16 - p. 12 - score 2:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 12: The mean QoE scores, utilities, rebuffering ratios, and switching rates from local deployment. SODA again has the highest mean QoE score and unlike all other baselines, simultaneously achieves ultra low mean rebuffering ratio and switching rate. (Error bars represent 95% confidence intervals.) Figure 13: The change in mean viewing durations (higher is better), bitrates (higher is better), rebuffering ratios (lower is better), and switching rates (lower is better) of SODA compared to the production baseline. designs (QEDs) to quantify the causal (adverse) impact of startup delay, rebuffering, and failures on user engagement, abandonment, and repeat viewership.

**Fragmento 17 - p. 19 - score 2:**

𝑟min , where 𝐸(𝑡−1, 𝐾) B Í𝑡+𝐾−1 𝜏=𝑡 𝜌𝜏−𝑡 ˆ𝜔𝜏|𝑡−1 −𝜔𝜏 . Similar to the proof outline for the exact prediction case in Section A.3, we can apply Lemma A.5 to bound the accumulation of past errors. With the help of Lemma A.6 and Lemma A.7, we show our main result for SODA when the predictions of the future bandwidths are inexact in Theorem A.8. We defer the proof of Theorem A.8 to Section D.3. Theorem A.8. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Let 𝐷B min{¯𝑥,𝑥max− ¯𝑥}. Suppose the weight 𝛽, the prediction horizon 𝐾, and the prediction errors satisfy that 𝛽≥ 3 𝜖𝐷·  1 + 4𝛾 𝜔min  ·  1 𝑟min − 1 𝑟max  , and 𝐸(𝑡, 𝐾) + 𝜌𝐾≤ (1 −𝜌)𝐷 3𝐶(1 + 𝐶+ 𝐶′)  1 + 𝑥max + 1 𝑟min − 1 𝑟max  , where, recall, 𝐸(𝑡, 𝐾) = Í𝑡+𝐾 𝜏=𝑡+1 𝜌𝜏−𝑡−1 ˆ𝜔𝜏|𝑡−𝜔𝜏 . Then, the buffer levels in the SODA’s decision trajectory never hits the constraint boundary, i.e., 0 < 𝑥𝑡< 𝑥max for 𝑡= 1, . . . , 𝑁. Further, SODA achieves a dynamic regret of 2  1 + 1 𝑟min + 𝐶+ 𝐶′2  1 + 𝑥max + 1 𝑟min − 1 𝑟max  (1 −𝜌)3/2 · √︁ 4𝛾+ 𝛽+ 𝜔max · √︁ E · cost(OPT)+  1 + 1 𝑟min + 𝐶+ 𝐶′4  1 + 𝑥max + 1 𝑟min − 1 𝑟max 2 (4𝛾+ 𝛽+ 𝜔max) (1 −𝜌)3 · E, where E = 𝜌2𝐾𝑁+ Í𝐾 𝜅=1 𝜌𝜅𝐸𝜅. Here 𝐸𝜅B Í𝑁 𝑡=1 ˆ𝜔𝑡+𝜅|𝑡−𝜔𝑡+𝜅 2. Note that the dynamic regret bound shown in Theorem A.8 is in the order of 𝑂( √ E𝑁+ E), since cost(OPT) = 𝑂(𝑁). Intuitively, from the form of 𝐸𝑡(𝐾), we see that predicting the future bandwidth 𝜔𝜏accurately at time step 𝑡becomes less important as (𝜏−𝑡) increases. A.5 Proof Outline for Efficient Structure In this section, we show that optimal solution of the finite-time optimal control problem solved by SODA can be approximated well by a monotonic sequence of bitrates when the coefficient 𝛾of the switching cost is sufficiently large (see Theorem A.9). Although this result is shown for the continuous variable case, it also provides some insight as to why the efficient approximate solver in Algorithm 1 can provide identical decisions to the brute-force solver with relatively high probabilities, as shown in Figure 8. Theorem A.9. Let ˆ𝜔×𝐾denote the sequence { ˆ𝜔, . . . , ˆ𝜔} with length 𝐾. For any 𝜆> 0, when the coefficient 𝛾is sufficiently large such that 𝛾≥𝐾2 𝜆2

**Fragmento 18 - p. 1 - score 1:**

To demonstrate its real-world practicality, we deployed SODA on a wide range of devices within the production network of Amazon Prime Video. Production experiments show that SODA reduced bitrate switching by up to 88.8% and increased average stream viewing duration by up to 5.91% compared to a fine-tuned production baseline. CCS CONCEPTS • Information systems →Multimedia streaming; • Theory of computation →Online algorithms; Theory and algorithms for application domains. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.

**Fragmento 19 - p. 2 - score 1:**

2) Better QoE Across Empirical Evaluations. We evaluated SODA in three settings: numerical simulations, prototype evalua- tion, and production deployment within Amazon Prime Video serving actual users. Our numerical simulations show a 9.55% to Figure 2: BOLA’s [44] decision boundaries are spaced out for on-demand streaming, but tiny fluctuations in buffer level can cause bitrate switching for live streaming. 27.8% QoE improvement and our prototype evaluation shows a 30.4% QoE improvement compared to the state-of-the-art base- lines. Production live streaming experiments in Amazon Prime Video show that SODA reduced bitrate switching by a significant up to 88.8% and increased average stream viewing duration by up to 5.91% (> 5 minutes longer sessions) compared to a fine- tuned production baseline.

**Fragmento 20 - p. 3 - score 1:**

streaming, a longer buffer of 120 seconds ensures that bitrate jumps are spaced well apart (up to 20 seconds), however, for live streaming with a buffer of 20 seconds, bitrates fluctuate with small deviations of 1 - 3 seconds in the buffer size. This can cause bitrates to switch frequently. While controllers such as MPC [17] and Pensieve [22] offer respite by explicitly penalizing bitrate switching, these con- trollers suffer from shortcomings of their own: • Model predictive controllers are hard to deploy at scale because they need to solve a non-linear integer programming problem over a prediction horizon of 𝐾segments, e.g., 𝐾= 5, which is so computationally expensive that it is quicker to download a video segment than to obtain a bitrate decision [17, 19].

**Fragmento 21 - p. 3 - score 1:**

Notice that beyond 70 seconds, RobustMPC re- peatedly rebuffers but continues to download the highest bitrate (Figure 3 bottom plot), resulting in 29 rebuffering events over 200 seconds. Strikingly, this behavior is in fact the optimal behavior under RobustMPC’s objective function which tolerates rebuffering to prevent bitrate switches. On the surface, this suggests higher rebuffering penalty in the objective function, however, higher penalties only reduce the duration of these tolerable rebuffers but do not eliminate them. Indeed, past work has empirically shown that even a 20× buffering penalty has marginal impact [24]. • Variance in network conditions or throughput prediction errors are not well tolerated by existing controllers.

**Fragmento 22 - p. 4 - score 1:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. sacrificing video quality or sustained playback, (ii) be robust against volatile network conditions, and (iii) be easy to deploy in practice. Before delving into the details in the remainder of the paper, we provide a brief overview of how SODA satisfies these requirements: • SODA leverages SOCO to balance the trade-off between video qual- ity, sustained playback without rebuffers, and bitrate smoothness without frequent switches. Importantly, SODA focuses on steer- ing the buffer level towards a target rather than weighing video quality against rebuffering duration (see Section 3.1). • To achieve robustness against throughput variability, SODA is de- signed to satisfy the exponentially decaying perturbation property, which guarantees that SODA never operates too far away from the optimal trajectory in the face of prediction errors (see Section 4.2).

**Fragmento 23 - p. 4 - score 1:**

This enables us to incorporate throughput predictions into the controller in a prin- cipled way. Taking advantage of recent advancements in smoothed online convex optimization (SOCO), we can theoretically prove that SODA offers a near-optimal quality of experience (QoE) and is robust against throughput prediction errors. 3.1 A Time-Based ABR Formulation Our time-based ABR formulation treats a video stream as a contin- uous flow rather than a discrete sequence of segments. Consider a streaming session that consists of 𝑁time intervals with fixed dura- tion Δ𝑡in terms of clock time (not video time). The controller’s task is to select a bitrate for each time interval from a set of available bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high quality, short rebuffering, and infrequent bitrate switching.

**Fragmento 24 - p. 4 - score 1:**

The time-based buffer dynamics are introduced into the opti- mization problem through the following constraint: 𝑥𝑛= 𝑥𝑛−1 + 𝜔𝑛Δ𝑡 𝑟𝑛 −Δ𝑡∈[0,𝑥max], where 𝜔𝑛Δ𝑡/𝑟𝑛accounts for the variable amount of video down- loaded during a time interval and Δ𝑡accounts for the fixed amount of buffer drained during the same time interval. Note that we do not allow the controller to violate the buffer range constraint during the optimization phase when determining the bitrate. Of course, due to throughput prediction errors, this may sometimes be inevitable during the execution phase when applying the bitrate decision. Why a Time-Based Formulation? The time-based formulation allows a cleaner theoretical analysis over a given throughput se- quence (𝜔1, .

**Fragmento 25 - p. 4 - score 1:**

. . ,𝜔𝑁). For example, consider the throughput function shown in Figure 4. In the time-based formulation, we naturally have 𝜔1 = 4, 𝜔2 = 1, and 𝜔3 = 𝜔4 = 2 Mb/s given Δ𝑡= 1 s. By contrast, in the segment-based formulation, the throughput sequence be- comes dependent on the bitrate sequence. Assuming the segment duration is also 𝐿= 1 s, if the controller chooses 𝑟1 = 2 Mb/s and 𝑟2 = 2.5 Mb/s, then it takes 0.5 and 1 s to download the first and sec- ond segments respectively, resulting in 𝜔1 = 4 and 𝜔2 = 2.5 Mb/s. As such, the segment based formulation gets causally biased due to bitrate selection 𝑟1, ...,𝑟𝑁, which in turn makes it difficult to theoretically analyze the design [61]. Why Not Model Rebuffering Directly?

**Fragmento 26 - p. 5 - score 1:**

Dark blue to light orange repre- sent low to high bitrate decisions. Notice that SODA becomes more aggressive in selecting higher bitrates as the buffer grows. The rightmost region is blank since SODA makes no downloads to prevent a buffer overflow. subject to 𝑥𝑚= 𝑥𝑚−1 + ˆ𝜔𝑚|𝑛−1Δ𝑡 𝑟𝑚 −Δ𝑡, (2b) 𝑥𝑚∈[0,𝑥max], 𝑟𝑚∈R, (2c) with respect to variables 𝑟𝑛, . . . ,𝑟𝑛+𝐾−1 and then committing to only the first bitrate decision 𝑟𝑛. The behavior of SODA is visualized as a bitrate decision diagram in Figure 5 to provide readers with intuition about how SODA selects bitrates in practice. As discussed in Section 2, solving this optimization problem is computationally expensive, furthermore, it is unclear what predic- tion horizon should be used and how accurate throughput predic- tions must be in order for SODA to perform well.


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 4 - score 5:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. sacrificing video quality or sustained playback, (ii) be robust against volatile network conditions, and (iii) be easy to deploy in practice. Before delving into the details in the remainder of the paper, we provide a brief overview of how SODA satisfies these requirements: • SODA leverages SOCO to balance the trade-off between video qual- ity, sustained playback without rebuffers, and bitrate smoothness without frequent switches. Importantly, SODA focuses on steer- ing the buffer level towards a target rather than weighing video quality against rebuffering duration (see Section 3.1). • To achieve robustness against throughput variability, SODA is de- signed to satisfy the exponentially decaying perturbation property, which guarantees that SODA never operates too far away from the optimal trajectory in the face of prediction errors (see Section 4.2).

**Fragmento 2 - p. 5 - score 4:**

Our approach is analogous to the use of control barrier functions to ensure safety properties in control systems [30]. • Modeling rebuffering time directly makes the controller vulnera- ble to throughput prediction errors. Under a direct rebuffering objective, as long as the buffer level is above zero, there will be no penalty for the controller, even if the buffer level is dangerously close to 0. As a result, even small throughput prediction errors can lead to unexpected rebuffering. 3.2 Incorporating Throughput Predictions In addition to facilitating theoretical analysis, our time-based formu- lation is crucial to ensuring the validity of throughput predictions over the prediction horizon. An important observation is that bi- trate decisions have no causal impact on how long the throughput predictions are valid for.

**Fragmento 3 - p. 6 - score 4:**

SODA achieves a dynamic regret of 𝑂( √ E𝑁+ E). The formal statement of Theorem 4.2 is given in Theorem A.8 in Appendix A. Theorem 4.2 shows that, if the buffer costs are “steep” and the prediction errors on the bandwidth are relatively small, SODA can achieve a sequence of buffer levels that stay safely away from the boundaries of buffer constraint [0,𝑥max]. The dynamic regret of SODA depends on the magnitude of the prediction errors and the regret improves when the errors become smaller. SODA acquires this guarantee thanks to its maintenance of the buffer near a target level ¯𝑥. In contrast, RobustMPC [17] doesn’t offer the same performance guarantee, thus even small bandwidth prediction errors can cause the video to rebuffer if the buffer level is near zero.

**Fragmento 4 - p. 7 - score 4:**

Theorem 4.3 shows that the true optimal solution becomes closer to monotonic as the weight 𝛾of switching costs increases. While the theoretical bound can be conservative, we find that even with moderate 𝛾, the (discrete) decision made under the monotonic heuristic is usually identical to the true optimal solution on a real trajectory (see Figure 8). 5 IMPLEMENTATION DETAILS Given the theoretical design insights, we now discuss the practical implementation of the high-level design described in Section 3. There are three practical concerns that require discussion: (i) how to translate the time-based design to the segment-based schema; (ii) how to incorporate throughput predictions robustly; and (iii) how to solve the predictive optimization problem efficiently.

**Fragmento 5 - p. 9 - score 4:**

In general, the more volatile network conditions are, the more the QoE performance of any ABR con- troller degrades, as evidenced by the trend in Figure 10 from left to right. Nonetheless, SODA consistently outperforms baseline ABR controllers under all network conditions. The improvement in terms of mean QoE scores compared to the best baseline across different network datasets ranges from 9.55% to 27.8%, which mainly stems from improvement in terms of smoothness (shorter rebuffering time and less bitrate switching). We discuss the improvement of SODA over each baseline ABR controller below: • SODA vs HYB. HYB is not as robust as SODA under volatile network conditions. In addition, it switches up to 215% more since it does not consider bitrate switching.

**Fragmento 6 - p. 12 - score 4:**

9 CONCLUSION In this work, we propose a smoothness-optimized dynamic adaptive (SODA) controller that addresses this issue in a theoretically sound way. Thanks to SODA’s robustness against prediction errors and low runtime complexity, it is readily deployable in a wide range of production environments. Through numerical simulations and prototype evaluation, we show that SODA consistently outperforms the state-of-the-art baselines. More importantly, we deployed SODA in a major video streaming provider where SODA significantly re- duced bitrate switching by up to 88.8% compared to a fine-tuned production baseline. SODA’s novel time-based ABR formulation and theoretical insights shed new light on how to achieve consistent high-quality video streaming.

**Fragmento 7 - p. 3 - score 3:**

Past works have shown that RobustMPC incurs 26% more rebuffering events unless paired with a sophisticated throughput predictor [46, 50]. Simi- larly, learning-based controllers like Pensieve tend to degrade in performance when trained for realistic network conditions encountered in the wild [24]. In practice, accurate throughput predictions are hard because of several factors, including (i) de- vice and OS level inefficiencies [18], (ii) stop-start nature of video requests which do not interact well with TCP [8, 18], and (iii) volatile network conditions typical in production networks [1, 5, 45]. To make matters worse, sophisticated throughput predictors are themselves not necessarily accurate [16] and are challenging to deploy due to device level bottlenecks [58].

**Fragmento 8 - p. 5 - score 3:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia • Minimizing rebuffering directly is not theoretically tractable be- cause it requires a binary penalty function that yields a non-zero penalty exactly when the buffer is empty. Instead, we employ a smoother penalty function that increases in magnitude when the buffer level falls below a desired target level. When there is a network issue, we start to penalize early when the buffer level decreases below the safe target level and we provide the largest penalty when the buffer level is empty. Using a smooth penalty function enables us to guarantee that SODA’s optimiza- tion is strongly convex, which is key to our theoretical work.

**Fragmento 9 - p. 9 - score 3:**

In Section 4.2, we have showed that SODA is robust against prediction errors by design and does not require a sophisti- cated throughput predictor. We now demonstrate this empirically. First, we replaced the throughput predictor used in simulations with a perfect short-term throughput predictor. Next, we gradually introduced more and more white noise to the perfect throughput predictions and observed how different ABR controllers behave accordingly. This experiment was conducted on a random subset of our network datasets with a size of 10,000 sessions. Note that throughput prediction discounts were turned off for all ABR con- trollers to reveal their intrinsic robustness.1 The results are shown in Figure 11, from which we observe that all hybrid ABR controllers that take throughput predictions into account will inevitably be affected by prediction errors to some extent (BOLA is not affected since it is purely buffer-based).

**Fragmento 10 - p. 9 - score 3:**

Additionally, it has low-buffer safety heuristic to reduce rebuffering and a switching avoidance heuristic to mitigate bitrate switching. It is the default ABR con- troller in dash.js. • MPC [17]: One application of model predictive control to adap- tive streaming that models utility, rebuffering time, and bitrate switching, without theoretical guarantees. 6.1.3 QoE Performance. The aggregate statistics for QoE scores and individual QoE components under each network dataset are shown in Figure 10. To better understand how the performance of different ABR controllers react to the intrinsic volatility of network conditions, we split the Puffer dataset into four quarters according to the relative standard deviation of throughput (Q1 represents the most stable network conditions, while Q4 represents the most volatile network conditions).

**Fragmento 11 - p. 9 - score 3:**

• SODA vs BOLA & Dynamic. As mainly buffer-based ABR con- trollers, BOLA and Dynamic are fairly robust against volatile net- work conditions. Dynamic’s performance is what one would ex- pect in a typical production environment. Nonetheless, SODA is able to achieve similar mean utilities without sacrificing mean rebuffering ratios, proving its outstanding robustness as a hybrid ABR controller. Where SODA really shines though is its signifi- cantly lower mean switching rates. Despite Dynamic’s switch- ing avoidance heuristic, SODA cuts down mean switching rates by as much as 70.4%, which demonstrates the superiority of theoretically-sound design. • SODA vs MPC. MPC has high mean utilities and low mean switching rates under stable network conditions (see Puffer (Q1 variance) in Figure 10).

**Fragmento 12 - p. 9 - score 3:**

Nonetheless, SODA still consistently outperforms all baseline ABR controllers up to a noise level of 50%. For reference, EMA predictor has an empirical noise level of about 30% on the same sessions. More importantly, the QoE degradation of SODA is minimal up to the reference point of EMA predictor, i.e., about 10%, which reinforces 1The ranking between different ABR controllers in this section may be different from that in Figure 10, which reveals that the robustness of certain ABR controllers should be attribute to throughput prediction discounts instead of intrinsic designs. 621

**Fragmento 13 - p. 2 - score 2:**

ABR controllers deployed in the field need to work on a wide range of client devices, including low-end ones with limited computa- tional resources. Many ABR controllers proposed in the research literature do not meet the efficiency bar for a production de- ployment and are never implemented in practice. We maximized SODA’s runtime and deployment practicality by devising a com- putationally efficient method to search for near-optimal bitrate decisions, which reduced the runtime complexity from exponen- tial to polynomial, e.g., about 200 iterations max in practice. In addition, we made SODA robust against throughput prediction errors by design, thus eliminating the need for sophisticated computationally-intensive throughput predictors.

**Fragmento 14 - p. 2 - score 2:**

See Table 1 for a summary of our key findings about SODA as compared to baseline ABR controllers. 3) Robustness Against Throughput Prediction Errors. Most ABR controllers rely on and are sensitive to predictions of the future network throughput. Our SOCO framework allows us to design robust ABR controllers that are provably robust against prediction errors. Specifically, we show that SODA has the ex- ponentially decaying perturbation property [49, 55, 56], i.e., the future impact of prediction errors decay rapidly over time. A key to our proof methodology is that we shifted from the con- ventional segment-based ABR formulation and adopted a novel time-based perspective. 4) Efficient Implementation for Production Deployment.

**Fragmento 15 - p. 3 - score 2:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Table 1: A qualitative summary of our key evaluation findings about SODA as compared to baseline ABR controllers. Controller Theorya Video Quality Rebuffering Time Switching Rate Deployability SODA Q + R + S high short ultra low high HYB [24] none high medium high high BOLA [44] Q + R high short high high Dynamic [36] Q + R high short medium high MPC [17] none high long low low Fugu [46] none high medium low low CausalSimRL [60] none high short high low aQ, R, S stand for theoretical guarantees for quality, rebuffering, and switching respectively. Figure 3: A RobustMPC session where the controller intention- ally rebuffers instead of lowering the bitrate.

**Fragmento 16 - p. 3 - score 2:**

Notice that beyond 70 seconds, RobustMPC re- peatedly rebuffers but continues to download the highest bitrate (Figure 3 bottom plot), resulting in 29 rebuffering events over 200 seconds. Strikingly, this behavior is in fact the optimal behavior under RobustMPC’s objective function which tolerates rebuffering to prevent bitrate switches. On the surface, this suggests higher rebuffering penalty in the objective function, however, higher penalties only reduce the duration of these tolerable rebuffers but do not eliminate them. Indeed, past work has empirically shown that even a 20× buffering penalty has marginal impact [24]. • Variance in network conditions or throughput prediction errors are not well tolerated by existing controllers.

**Fragmento 17 - p. 4 - score 2:**

This enables us to incorporate throughput predictions into the controller in a prin- cipled way. Taking advantage of recent advancements in smoothed online convex optimization (SOCO), we can theoretically prove that SODA offers a near-optimal quality of experience (QoE) and is robust against throughput prediction errors. 3.1 A Time-Based ABR Formulation Our time-based ABR formulation treats a video stream as a contin- uous flow rather than a discrete sequence of segments. Consider a streaming session that consists of 𝑁time intervals with fixed dura- tion Δ𝑡in terms of clock time (not video time). The controller’s task is to select a bitrate for each time interval from a set of available bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high quality, short rebuffering, and infrequent bitrate switching.

**Fragmento 18 - p. 4 - score 2:**

The time-based buffer dynamics are introduced into the opti- mization problem through the following constraint: 𝑥𝑛= 𝑥𝑛−1 + 𝜔𝑛Δ𝑡 𝑟𝑛 −Δ𝑡∈[0,𝑥max], where 𝜔𝑛Δ𝑡/𝑟𝑛accounts for the variable amount of video down- loaded during a time interval and Δ𝑡accounts for the fixed amount of buffer drained during the same time interval. Note that we do not allow the controller to violate the buffer range constraint during the optimization phase when determining the bitrate. Of course, due to throughput prediction errors, this may sometimes be inevitable during the execution phase when applying the bitrate decision. Why a Time-Based Formulation? The time-based formulation allows a cleaner theoretical analysis over a given throughput se- quence (𝜔1, .

**Fragmento 19 - p. 5 - score 2:**

We first analyze these questions theoretically (Section 4) and then present a practical implementation of SODA that answers these concerns (Section 5). 4 THEORETICAL DESIGN INSIGHTS Our design of SODA is motivated by recent theoretical advances at the interface of learning and control [28, 38, 49, 54] and smoothed online convex optimization [25, 33, 55]. In particular, we design SODA to satisfy an exponentially decaying perturbation property that has been shown to ensure efficient and robust use of predictions in model predictive control policies [49, 56]. Intuitively, this property describes the behavior of the solution to the optimization problem defining SODA (Equation 2) as a function of problem parameters, including bandwidth predictions { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾and the previ- ous buffer level/action pair (𝑥𝑛−1,𝑢𝑛−1).

**Fragmento 20 - p. 6 - score 2:**

Thus, we establish a bound on the per-step error that depends on the errors of predicting future bandwidths and the prediction horizon 𝐾(Lemma A.4). On the other hand, we also show that the aggregation of per-step errors does not grow linearly in time because the exponentially decaying perturbation guarantees that the impact of each previous per-step error vanishes exponentially over time (Lemma A.5). We present a proof outline and the detailed proofs in Appendix A. To prove the exponentially decaying perturbation, we require a technical assumption that guarantees the controller can “reach” any desired buffer level by choosing the largest/smallest bitrate (see Assumption A.1 in Appendix A for the formal statement).

**Fragmento 21 - p. 6 - score 2:**

This result implies that SODA’s performance ap- proaches that of the optimal sequence of decisions exponentially fast in the prediction horizon size 𝐾; thus, only a small prediction horizon length is necessary to obtain good performance. 4.2 Inexact Predictions We now relax the exact prediction assumption to prove SODA’s robustness to a certain level of prediction errors thanks to its expo- nentially decaying perturbation property. Theorem 4.2. [Informal] Suppose the prediction error at each step is bounded above. The buffer level of SODA will never hit the constraint boundary, i.e., 0 < 𝑥𝑛< 𝑥max. Further, define E = 𝜌2𝐾𝑁+ Í𝐾 𝜅=1 𝜌𝜅𝐸𝜅, where 𝐸𝜅is the total squared error for predicting 𝜅steps into the future.

**Fragmento 22 - p. 7 - score 2:**

5.1 Segment-Based Schema SODA is intrinsically a time-based controller, but in practice, a video must be downloaded segment by segment according to the MPEG- DASH standard. To reconcile with this requirement, we keep the optimization phase as is in the time-based format and empirically set Δ𝑡to be equal to the segment length. This choice is justified by the fact that in the steady state, the download time of a video segment is expected to be close to the segment length or much less than that [29]. To further minimize the likelihood of committing to a bitrate for significantly longer than Δ𝑡, we introduce another heuristic that the controller must select a bitrate no higher than min{𝑟∈R : 𝑟≥ˆ𝜔}. 5.2 Incorporating Predictions Robustly According to Section 4.2, SODA is robust against prediction errors by design as long as there is no systematic bias in prediction er- rors.

**Fragmento 23 - p. 7 - score 2:**

SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia minimum possible time. A critical observation underlying the im- plementation of SODA is that it is sufficient to search only for bitrate sequences that are increasing or decreasing monotonically. We provide a theoretical justification in the following theorem. Theorem 4.3. [Informal] Suppose SODA is given the predictions that satisfy ˆ𝜔𝑛|𝑛−1 = · · · = ˆ𝜔𝑛+𝐾−1|𝑛−1 at an intermediate time step 𝑛. Then, the bitrate trajectory solved by SODA can be approximated by a feasible monotonic bitrate trajectory with an error of 𝑂 𝐾/√𝛾. The formal statement of Theorem 4.3 is given in Theorem A.9 in Appendix A.

**Fragmento 24 - p. 8 - score 2:**

To fully exercise our datasets, we considered a high-frame-rate 4K video encoded according to the YouTube recommended settings (1.5, 4, 7.5, 12, 24, and 60 Mb/s) [65] with a segment length of 2 seconds. For the 5G and 4G datasets, we considered the same video with the two highest bitrates removed. Finally, for throughput prediction, we opted for the exponential moving average (EMA) predictor, the default throughput predictor in dash.js. 6.1.2 Baseline ABR Controllers. We compared SODA against the following ABR controllers representative of each of the common ABR controller categories, i.e., throughput-based, buffer-based, and hybrid. They were tuned to our best efforts for our network datasets. 620

**Fragmento 25 - p. 9 - score 2:**

However, the performance of MPC is tightly coupled with the intrinsic volatility of network conditions. Specifically, MPC suffers a lot in terms of mean rebuffering ratios especially under mobile network conditions. By contrast, SODA does not have this issue since it is robust against prediction errors by design, making it much more suitable for production deployment. 6.1.4 Intrinsic Sensitivity to Prediction Accuracy. In an effort to im- prove throughput prediction accuracy, several prior works have fo- cused on designing more sophisticated throughput predictors such as C2SP [20], Fugu [46], and Xatu [50]. While these throughput pre- dictors may offer higher prediction accuracy, they are complex and difficult to deploy, especially on compute or memory constrained devices [58].

**Fragmento 26 - p. 10 - score 2:**

ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia Chen et al. Figure 10: The mean QoE scores, utilities, rebuffering ratios and switching rates of SODA and baseline ABR controllers under each network dataset. The Puffer dataset is split into four quarters according the throughput variance (Q1 being lowest while Q4 being highest). SODA has consistently higher mean QoE scores and lower switching rates than all baseline ABR controllers under all network conditions. (Error bars represent 95% confidence intervals.) Figure 11: The mean QoE scores for SODA and baseline ABR controllers under variable amounts of white noise. (The error bars represent 95% confidence intervals.) the idea that a practical deployment of SODA does not require a sophisticated throughput predictor.2 2In practice, we observe that EMA predictor is actually much better than a perfect short-term predictor with 30% white noise because the noise patterns are different, which means that real gap is less than 10%.


## 8. Checklist crudo para Codex / diseno Fase 4-5 v1

- [ ] Extraer exactamente que modelo/algoritmo propone.
- [ ] Extraer features/estado disponibles online y descartar future leakage.
- [ ] Extraer accion/salida y si coincide con representation_index o necesita adaptacion.
- [ ] Extraer reward/QoE/loss y relacion con qoe_linear_v1/rebuffer/smoothness.
- [ ] Extraer datasets/traces/splits y si son comparables a nuestras trazas curadas.
- [ ] Extraer baselines y escenarios donde falla/mejora.
- [ ] Extraer limitaciones y requisitos hardware/dependencias.
- [ ] Decidir si aporta a: nuevo modelo, teacher mejorado, predictor, selector, safety layer, risk-aware guard o solo contexto.


## 9. Texto crudo por pagina

Incluye texto extraido por pagina. Puede contener artefactos de dos columnas, encabezados, pies, referencias o formulas degradadas. Consultar `raw_text_layout/` para extraccion layout completa.


### Pagina 1
```text
SODA: An Adaptive Bitrate Controller for Consistent
High-Quality Video Streaming
Tianyu Chen
University of Massachusetts Amherst
Amherst, MA, USA
tianyuchen@umass.edu
Yiheng Lin
California Institute of Technology
Pasadena, CA, USA
yihengl@caltech.edu
Nicolas Christianson
California Institute of Technology
Pasadena, CA, USA
nchristianson@caltech.edu
Zahaib Akhtar
Amazon Prime Video / NCSU
Sunnyvale, CA, USA
akhtz@amazon.com
Sharath Dharmaji
Amazon Prime Video
Sunnyvale, CA, USA
sharatdr@amazon.com
Mohammad Hajiesmaili
University of Massachusetts Amherst
Amherst, MA, USA
hajiesmaili@cs.umass.edu
Adam Wierman
California Institute of Technology
Pasadena, CA, USA
adamw@caltech.edu
Ramesh K. Sitaraman
University of Massachusetts Amherst
Amherst, MA, USA
ramesh@cs.umass.edu
ABSTRACT
The primary objective of adaptive bitrate (ABR) streaming is to
enhance users’ quality of experience (QoE) by dynamically adjust-
ing the video bitrate in response to changing network conditions.
However, users often find frequent bitrate switching frustrating
due to the resulting inconsistency in visual quality over time, es-
pecially during live streaming when buffer lengths are short. In
this paper, we propose a practical smoothness optimized dynamic
adaptive (SODA) controller that specifically addresses this problem
while remaining deployable. SODA is backed by theoretical guaran-
tees and has shown superior performance in empirical evaluations.
Specifically, our numerical simulations show a 9.55% to 27.8% QoE
improvement and our prototype evaluation shows a 30.4% QoE im-
provement compared to the state-of-the-art baselines. In order to be
widely deployable, SODA performs bitrate horizon planning in poly-
nomial time compared to brute force approaches that suffer from
exponential complexity. To demonstrate its real-world practicality,
we deployed SODA on a wide range of devices within the production
network of Amazon Prime Video. Production experiments show
that SODA reduced bitrate switching by up to 88.8% and increased
average stream viewing duration by up to 5.91% compared to a
fine-tuned production baseline.
CCS CONCEPTS
• Information systems →Multimedia streaming; • Theory of
computation →Online algorithms; Theory and algorithms
for application domains.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0614-1/24/08
https://doi.org/10.1145/3651890.3672260
KEYWORDS
Adaptive bitrate streaming, Smoothed online convex optimization
ACM Reference Format:
Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath
Dharmaji, Mohammad Hajiesmaili, Adam Wierman, and Ramesh K. Sitara-
man. 2024. SODA: An Adaptive Bitrate Controller for Consistent High-
Quality Video Streaming. In ACM SIGCOMM 2024 Conference (ACM SIG-
COMM ’24), August 4–8, 2024, Sydney, NSW, Australia. ACM, New York, NY,
USA, 32 pages. https://doi.org/10.1145/3651890.3672260
1
INTRODUCTION
With the growth of online video streaming, users nowadays stream
videos from a highly diverse set of devices, including laptops, mobile
devices, smart TVs, set-top boxes, game consoles, etc. These devices
span a wide spectrum of hardware capabilities and connect to the
Internet in a multitude of ways, e.g., wireless, cellular, cable, etc. To
ensure a high quality of experience (QoE) across all devices, video
providers utilize adaptive bitrate (ABR) streaming that tailors video
delivery to specific devices and network conditions.
The goal of ABR streaming is to deliver a video at the highest sus-
tainable quality over time-varying network conditions. To achieve
this, a video source is encoded at different bitrates corresponding
to different resolutions, e.g., 720p, 1080p, 1440p, etc. Each encod-
ing is in turn temporally partitioned into a sequence of segments,
e.g., 2 seconds of video content. An ABR controller inside a user’s
video player then selects a suitable bitrate for each segment. Finally,
downloaded segments are stored in a buffer, till they are rendered.
Past studies have shown that a user’s QoE is maximized by de-
livering the video at the highest possible quality with minimal
rebuffering and bitrate switching. It has been shown that a 1% in-
crease in rebuffering time is correlated with a 3-minute reduction in
the viewing duration [7] and frequent bitrate switching is strongly
correlated with a user abandoning the session [21]. Going beyond
correlational studies, the significant causal impact of rebuffering
and other QoE performance metrics on key measures of user behav-
ior was first established in [9]. However, jointly optimizing all three
key components of QoE, i.e., video quality, rebuffering and bitrate
613
```


### Pagina 2
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Figure 1: Video stream duration is negatively correlated with
bitrate switching rate. Users watch < 10% of the stream when
bitrate switching rate is > 20%.
switching, is non-trivial as they are locked in a three-way trade-off.
An ideal ABR controller seeks to push the trade-off boundary and
optimize all three QoE components simultaneously.
Between on-demand and live streaming, the latter is more chal-
lenging as the player buffer is restricted to 10 - 20 seconds (to remain
close to actual live action), which is in contrast to 60 - 180 seconds
of buffer in on-demand streaming. Consequently, live streaming
has higher susceptibility to rebuffering and bitrate switching. To
understand the impact of bitrate switching, Figure 1 shows the re-
lationship between the viewing percentage of a stream and bitrate
switching rate for a sports event on a large-scale video streaming
provider. To minimize potential confounders such as rebuffering
and low quality, the plot is focused on short-lived sessions (< 25%
of stream viewed) with at least HD quality and no rebuffering. The
line of best fit shows that users watch < 10% of the stream when
bitrate switching rate is > 20%. While our proposed ABR controller
works for both on-demand and live streaming, our evaluations use
live streams that represents a more challenging use case.
Our Contributions. We propose a novel smoothness optimized
dynamic adaptive (SODA) controller that provides theoretical QoE
guarantees while exhibiting superior empirical performance in
simulation, prototype, and production experiments. We make the
following specific contributions:
1) Theoretical Foundations of ABR Controller Design. SODA
is the first ABR controller to provably optimize all three key
components of QoE, namely, video quality, rebuffering and bi-
trate switching. Unlike prior work such as BOLA [36, 44] that use
Lyapunov methods to optimize the first two components, we
use a new framework based on recent advances in smoothed
online convex optimization (SOCO) [13, 25, 26, 33–35, 43] to
simultaneously optimize all three QoE components. To enable
the application of SOCO, we model the rebuffering minimiza-
tion requirement in a novel fashion using the notion of buffer
stability. We prove that SODA is near-optimal and achieves QoE
within a small factor of the offline optimal QoE (Theorem 4.1).
2) Better QoE Across Empirical Evaluations. We evaluated
SODA in three settings: numerical simulations, prototype evalua-
tion, and production deployment within Amazon Prime Video
serving actual users. Our numerical simulations show a 9.55% to
Figure 2: BOLA’s [44] decision boundaries are spaced out for
on-demand streaming, but tiny fluctuations in buffer level
can cause bitrate switching for live streaming.
27.8% QoE improvement and our prototype evaluation shows a
30.4% QoE improvement compared to the state-of-the-art base-
lines. Production live streaming experiments in Amazon Prime
Video show that SODA reduced bitrate switching by a significant
up to 88.8% and increased average stream viewing duration by
up to 5.91% (> 5 minutes longer sessions) compared to a fine-
tuned production baseline. See Table 1 for a summary of our key
findings about SODA as compared to baseline ABR controllers.
3) Robustness Against Throughput Prediction Errors. Most
ABR controllers rely on and are sensitive to predictions of the
future network throughput. Our SOCO framework allows us to
design robust ABR controllers that are provably robust against
prediction errors. Specifically, we show that SODA has the ex-
ponentially decaying perturbation property [49, 55, 56], i.e., the
future impact of prediction errors decay rapidly over time. A
key to our proof methodology is that we shifted from the con-
ventional segment-based ABR formulation and adopted a novel
time-based perspective.
4) Efficient Implementation for Production Deployment. ABR
controllers deployed in the field need to work on a wide range
of client devices, including low-end ones with limited computa-
tional resources. Many ABR controllers proposed in the research
literature do not meet the efficiency bar for a production de-
ployment and are never implemented in practice. We maximized
SODA’s runtime and deployment practicality by devising a com-
putationally efficient method to search for near-optimal bitrate
decisions, which reduced the runtime complexity from exponen-
tial to polynomial, e.g., about 200 iterations max in practice. In
addition, we made SODA robust against throughput prediction
errors by design, thus eliminating the need for sophisticated
computationally-intensive throughput predictors.
This work does not raise any ethical issues.
2
DESIGN GAPS, OPPORTUNITIES, AND
REQUIREMENTS
Design Gaps. Live streaming poses the additional constraint of
near real-time delivery which makes bitrate adaptation more chal-
lenging than that in on-demand streaming. Figure 2 shows the
bitrate selection function of BOLA [36, 40, 44], an ABR controller
that is widely deployed by video providers and is part of the refer-
ence MPEG-DASH video player [64]. Notice that for on-demand
614
```


### Pagina 3
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Table 1: A qualitative summary of our key evaluation findings about SODA as compared to baseline ABR controllers.
Controller
Theorya
Video Quality
Rebuffering Time
Switching Rate
Deployability
SODA
Q + R + S
high
short
ultra low
high
HYB [24]
none
high
medium
high
high
BOLA [44]
Q + R
high
short
high
high
Dynamic [36]
Q + R
high
short
medium
high
MPC [17]
none
high
long
low
low
Fugu [46]
none
high
medium
low
low
CausalSimRL [60]
none
high
short
high
low
aQ, R, S stand for theoretical guarantees for quality, rebuffering, and switching respectively.
Figure 3: A RobustMPC session where the controller intention-
ally rebuffers instead of lowering the bitrate.
streaming, a longer buffer of 120 seconds ensures that bitrate jumps
are spaced well apart (up to 20 seconds), however, for live streaming
with a buffer of 20 seconds, bitrates fluctuate with small deviations
of 1 - 3 seconds in the buffer size. This can cause bitrates to switch
frequently. While controllers such as MPC [17] and Pensieve [22]
offer respite by explicitly penalizing bitrate switching, these con-
trollers suffer from shortcomings of their own:
• Model predictive controllers are hard to deploy at scale because
they need to solve a non-linear integer programming problem
over a prediction horizon of 𝐾segments, e.g., 𝐾= 5, which is so
computationally expensive that it is quicker to download a video
segment than to obtain a bitrate decision [17, 19]. Workarounds
such as pre-computed lookup tables [17] are impractical for live
streaming where the video is not available a priori. In a simi-
lar vein, learning-based controllers such as Pensieve [22] work
optimally when trained specifically for a given set of bitrates,
segment duration, network conditions, etc. Given in-the-wild
diversity and its evolving nature, ensuring this specificity im-
poses a significant operational overhead. Furthermore, even if
specifically trained, achieving performance guarantees with these
learning-based controllers is shown to be challenging [24].
• Existing ABR controllers naively reduce bitrate switching at the
expense of low video quality or more rebuffering. To demonstrate
this, Figure 3 shows a RobustMPC session with the exact setup
used by [17, 22]. Notice that beyond 70 seconds, RobustMPC re-
peatedly rebuffers but continues to download the highest bitrate
(Figure 3 bottom plot), resulting in 29 rebuffering events over 200
seconds. Strikingly, this behavior is in fact the optimal behavior
under RobustMPC’s objective function which tolerates rebuffering
to prevent bitrate switches. On the surface, this suggests higher
rebuffering penalty in the objective function, however, higher
penalties only reduce the duration of these tolerable rebuffers but
do not eliminate them. Indeed, past work has empirically shown
that even a 20× buffering penalty has marginal impact [24].
• Variance in network conditions or throughput prediction errors
are not well tolerated by existing controllers. Past works have
shown that RobustMPC incurs 26% more rebuffering events unless
paired with a sophisticated throughput predictor [46, 50]. Simi-
larly, learning-based controllers like Pensieve tend to degrade
in performance when trained for realistic network conditions
encountered in the wild [24]. In practice, accurate throughput
predictions are hard because of several factors, including (i) de-
vice and OS level inefficiencies [18], (ii) stop-start nature of video
requests which do not interact well with TCP [8, 18], and (iii)
volatile network conditions typical in production networks [1, 5,
45]. To make matters worse, sophisticated throughput predictors
are themselves not necessarily accurate [16] and are challenging
to deploy due to device level bottlenecks [58]. Therefore, in-the-
wild performance of these controllers remains questionable.
Opportunities. Outside of the video streaming literature, the
interaction of learning and control has blossomed in recent years,
leading to new and exciting approaches to controller designs [39,
47, 49, 52, 54]. However, these new approaches have not yet been
applied and evaluated in the context of video streaming where
classical model predictive and proportional–integral–derivative
control have remained the focus, e.g., [17, 23]. In particular, the
area of smoothed online convex optimization (SOCO) has seen
multiple breakthroughs in recent years [13, 25, 33, 35], including
the development of connections to model predictive controllers [26,
47, 49, 52, 56]. SOCO provides a systematic framework to balance
an objective function with action switching. It thus lends itself well
to video streaming, which needs to jointly optimize video quality,
sustained playback, and bitrate smoothness.
Requirements. Driven by the above design gaps and oppor-
tunities, we identify three requirements that SODA should deliver.
In particular, SODA should (i) achieve bitrate smoothness without
615
```


### Pagina 4
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
sacrificing video quality or sustained playback, (ii) be robust against
volatile network conditions, and (iii) be easy to deploy in practice.
Before delving into the details in the remainder of the paper, we
provide a brief overview of how SODA satisfies these requirements:
• SODA leverages SOCO to balance the trade-off between video qual-
ity, sustained playback without rebuffers, and bitrate smoothness
without frequent switches. Importantly, SODA focuses on steer-
ing the buffer level towards a target rather than weighing video
quality against rebuffering duration (see Section 3.1).
• To achieve robustness against throughput variability, SODA is de-
signed to satisfy the exponentially decaying perturbation property,
which guarantees that SODA never operates too far away from the
optimal trajectory in the face of prediction errors (see Section 4.2).
• To remain computationally efficient, SODA leverages an efficient
approximate solver (see Section A.5 for proof and Algorithm 1
for implementation), that only requires evaluation of monotonic
bitrate sequences (Section 4.3), which reduces the computational
cost by two orders of magnitude over a brute-force solver.
3
SODA OVERVIEW
Given the design gaps, opportunities, and requirements, we set out
to design a theoretically sound adaptive bitrate streaming (ABR)
controller that minimizes bitrate switching without compromis-
ing video quality or increasing rebuffering time, thus providing a
smooth viewing experience. To accomplish this, we deviate from
the conventional segment-based ABR formulation and derive theo-
retical insights from a time-based ABR formulation. This enables us
to incorporate throughput predictions into the controller in a prin-
cipled way. Taking advantage of recent advancements in smoothed
online convex optimization (SOCO), we can theoretically prove
that SODA offers a near-optimal quality of experience (QoE) and is
robust against throughput prediction errors.
3.1
A Time-Based ABR Formulation
Our time-based ABR formulation treats a video stream as a contin-
uous flow rather than a discrete sequence of segments. Consider a
streaming session that consists of 𝑁time intervals with fixed dura-
tion Δ𝑡in terms of clock time (not video time). The controller’s task
is to select a bitrate for each time interval from a set of available
bitrates R ⊂[𝑟min,𝑟max] to optimize for a combination of high
quality, short rebuffering, and infrequent bitrate switching.
Let 𝜔𝑛denote the average throughput during the 𝑛th time inter-
val, 𝑟𝑛the selected bitrate for that time interval, and 𝑥𝑛the buffer
level immediately after that time interval. Our objective is to min-
imize the overall cost given as a linear combination of the three
QoE components:
𝑁
∑︁
𝑛=1

𝑣(𝑟𝑛) · 𝜔𝑛Δ𝑡
𝑟𝑛
+ 𝛽· 𝑏(𝑥𝑛) + 𝛾· 𝑐(𝑟𝑛,𝑟𝑛−1)

,
(1)
where
• 𝑣(𝑟𝑛) is the distortion cost, which should be a positive, strictly
decreasing, and convex function that models the encoding distor-
tion, e.g., 𝑣(𝑟𝑛) = 1/𝑟𝑛. It is then weighted by the amount of video
downloaded during that time interval, i.e., 𝜔𝑛Δ𝑡/𝑟𝑛because the
controller downloads a variable amount of video during each
fixed time interval.
Figure 4: A sample throughput function used to illustrate
why our time-based formulation is better for analysis.
• 𝑏(𝑥𝑛) is the buffer cost, which aims to stabilize the buffer level
around a target level ¯𝑥, i.e.,
𝑏(𝑥𝑛) =
(
( ¯𝑥−𝑥𝑛)2
𝑥𝑛≤¯𝑥
𝜖(𝑥𝑛−¯𝑥)2
𝑥𝑛> ¯𝑥,
where 𝜖< 1 is a small constant. Note that we purposely do not
model the rebuffering time explicitly to avoid the pitfalls encoun-
tered by RobustMPC (Section 2) and as we show later, this helps
SODA achieve theoretical performance guarantees (Section 4.2).
• 𝑐(𝑟𝑛,𝑟𝑛−1) is the switching cost from the previous bitrate to the
current bitrate, e.g., 𝑐(𝑟𝑛,𝑟𝑛−1) = (𝑣(𝑟𝑛) −𝑣(𝑟𝑛−1))2.
Coefficients 𝛽and 𝛾are positive weights for the buffer and the
switching cost respectively based on user preferences. The choices
for the distortion and switching cost functions are flexible.
The time-based buffer dynamics are introduced into the opti-
mization problem through the following constraint:
𝑥𝑛= 𝑥𝑛−1 + 𝜔𝑛Δ𝑡
𝑟𝑛
−Δ𝑡∈[0,𝑥max],
where 𝜔𝑛Δ𝑡/𝑟𝑛accounts for the variable amount of video down-
loaded during a time interval and Δ𝑡accounts for the fixed amount
of buffer drained during the same time interval. Note that we do not
allow the controller to violate the buffer range constraint during
the optimization phase when determining the bitrate. Of course, due
to throughput prediction errors, this may sometimes be inevitable
during the execution phase when applying the bitrate decision.
Why a Time-Based Formulation? The time-based formulation
allows a cleaner theoretical analysis over a given throughput se-
quence (𝜔1, . . . ,𝜔𝑁). For example, consider the throughput function
shown in Figure 4. In the time-based formulation, we naturally have
𝜔1 = 4, 𝜔2 = 1, and 𝜔3 = 𝜔4 = 2 Mb/s given Δ𝑡= 1 s. By contrast,
in the segment-based formulation, the throughput sequence be-
comes dependent on the bitrate sequence. Assuming the segment
duration is also 𝐿= 1 s, if the controller chooses 𝑟1 = 2 Mb/s and
𝑟2 = 2.5 Mb/s, then it takes 0.5 and 1 s to download the first and sec-
ond segments respectively, resulting in 𝜔1 = 4 and 𝜔2 = 2.5 Mb/s.
As such, the segment based formulation gets causally biased due
to bitrate selection 𝑟1, ...,𝑟𝑁, which in turn makes it difficult to
theoretically analyze the design [61].
Why Not Model Rebuffering Directly? Rebuffering is important to
minimize from a user’s perspective [7, 9]. However, in our optimiza-
tion problem formulation, we did not explicitly model rebuffering
like prior works [17, 46, 50]. Instead, we focus on stabilizing the
buffer level around a target level with a smooth roll-off on both
sides for the following reasons:
616
```


### Pagina 5
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
• Minimizing rebuffering directly is not theoretically tractable be-
cause it requires a binary penalty function that yields a non-zero
penalty exactly when the buffer is empty. Instead, we employ
a smoother penalty function that increases in magnitude when
the buffer level falls below a desired target level. When there
is a network issue, we start to penalize early when the buffer
level decreases below the safe target level and we provide the
largest penalty when the buffer level is empty. Using a smooth
penalty function enables us to guarantee that SODA’s optimiza-
tion is strongly convex, which is key to our theoretical work. Our
approach is analogous to the use of control barrier functions to
ensure safety properties in control systems [30].
• Modeling rebuffering time directly makes the controller vulnera-
ble to throughput prediction errors. Under a direct rebuffering
objective, as long as the buffer level is above zero, there will be no
penalty for the controller, even if the buffer level is dangerously
close to 0. As a result, even small throughput prediction errors
can lead to unexpected rebuffering.
3.2
Incorporating Throughput Predictions
In addition to facilitating theoretical analysis, our time-based formu-
lation is crucial to ensuring the validity of throughput predictions
over the prediction horizon. An important observation is that bi-
trate decisions have no causal impact on how long the throughput
predictions are valid for. However, segment-based controllers such
as MPC [17] and Fugu [46] intertwine throughput predictions and bi-
trate decisions in non-causal ways. In these designs, the throughput
prediction horizon spans shorter periods of clock time when low
bitrate is selected compared to when high bitrate is selected. In fact,
their underlying assumption about the validity of the throughput
prediction horizon can vary by 𝑟max/𝑟min.
By contrast, the way we incorporate throughput predictions into
SODA does not suffer from this issue. Specifically, just before each
time interval, the controller is given access to a (not necessarily
accurate) throughput prediction for the next 𝐾time intervals from
a black-box throughput predictor. It is always assumed that the
validity of the throughput prediction is 𝐾Δ𝑡, a fixed value. In gen-
eral, a throughput predictor may output a different value for each
of the next 𝐾time intervals, i.e., ˆ𝜔𝑛|𝑛−1, ˆ𝜔𝑛+1|𝑛−1, . . . , ˆ𝜔𝑛+𝐾−1|𝑛−1,
where ˆ𝜔𝑚|𝑛−1 (𝑚≥𝑛) is the throughput prediction for the 𝑚th
time interval given previous download information up until the
(𝑛−1)th time interval. In other words, a throughput predictor can
output a piecewise constant throughput function for the next 𝐾Δ𝑡
time. In practice, though, a typical throughput predictor outputs a
single value that corresponds to a constant throughput function.
3.3
Control Mechanism
Inspired by the model predictive control framework, SODA selects a
bitrate for each time interval by optimizing over the next 𝐾time
intervals and then committing to the bitrate decision for the imme-
diate next time interval, i.e., minimizing
𝑛+𝐾−1
∑︁
𝑚=𝑛

𝑣(𝑟𝑚) ·
ˆ𝜔𝑚|𝑛−1Δ𝑡
𝑟𝑚
+ 𝛽· 𝑏(𝑥𝑚) + 𝛾· 𝑐(𝑟𝑚,𝑟𝑚−1)

(2a)
Figure 5: SODA’s bitrate decision as a function of buffer level
and predicted throughput. Dark blue to light orange repre-
sent low to high bitrate decisions. Notice that SODA becomes
more aggressive in selecting higher bitrates as the buffer
grows. The rightmost region is blank since SODA makes no
downloads to prevent a buffer overflow.
subject to
𝑥𝑚= 𝑥𝑚−1 +
ˆ𝜔𝑚|𝑛−1Δ𝑡
𝑟𝑚
−Δ𝑡,
(2b)
𝑥𝑚∈[0,𝑥max],
𝑟𝑚∈R,
(2c)
with respect to variables 𝑟𝑛, . . . ,𝑟𝑛+𝐾−1 and then committing to
only the first bitrate decision 𝑟𝑛. The behavior of SODA is visualized
as a bitrate decision diagram in Figure 5 to provide readers with
intuition about how SODA selects bitrates in practice.
As discussed in Section 2, solving this optimization problem is
computationally expensive, furthermore, it is unclear what predic-
tion horizon should be used and how accurate throughput predic-
tions must be in order for SODA to perform well. We first analyze
these questions theoretically (Section 4) and then present a practical
implementation of SODA that answers these concerns (Section 5).
4
THEORETICAL DESIGN INSIGHTS
Our design of SODA is motivated by recent theoretical advances at
the interface of learning and control [28, 38, 49, 54] and smoothed
online convex optimization [25, 33, 55]. In particular, we design
SODA to satisfy an exponentially decaying perturbation property that
has been shown to ensure efficient and robust use of predictions in
model predictive control policies [49, 56]. Intuitively, this property
describes the behavior of the solution to the optimization problem
defining SODA (Equation 2) as a function of problem parameters,
including bandwidth predictions { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾and the previ-
ous buffer level/action pair (𝑥𝑛−1,𝑢𝑛−1). Here, we define the actions
as the inverse of the bitrates (i.e., 𝑢𝜏= 1/𝑟𝜏for all time step 𝜏) and
do a change of the variables to make the dynamics linear for the
theoretical analysis. Under this property, when { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾
are fixed, the optimal trajectory of (Equation 2) under the initial
617
```


### Pagina 6
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
(𝑥𝑛−1,𝑢𝑛−1) (𝑥𝑛,𝑢𝑛)
(𝑥𝑛+1,𝑢𝑛+1)
(𝑥′
𝑛−1,𝑢′
𝑛−1)
(𝑥′𝑛,𝑢′𝑛)
(𝑥′
𝑛+1,𝑢′
𝑛+1)
Figure 6: Illustration of the exponentially decaying perturba-
tion property: When { ˆ𝜔𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾are fixed, the optimal
trajectories of Equation 2 under different initial buffer/action
pairs converge exponentially toward each other.
buffer/action pair (𝑥′
𝑛−1,𝑢′
𝑛−1) converges exponentially toward the
optimal trajectory under the pair (𝑥𝑛−1,𝑢𝑛−1) (see Figure 6 for
an illustration). On the other hand, when the initial buffer/action
pair is fixed, the impact of perturbing a prediction ˆ𝜔𝑚|𝑛−1 on the
first action 𝑢𝑛decays exponentially with respect to their temporal
distance (𝑚−𝑛). The formal definition of exponentially decaying
perturbation generalizes the intuition above to consider the impact
of perturbing any parameters on the entire optimal trajectory (see
Definition A.1 in Appendix A).
Two metrics that we use to measure SODA’s performance theoret-
ically are dynamic regret and competitive ratio, which are standard
in the literature of online optimization [25, 28, 33, 49, 54]. Specif-
ically, let cost(ALG) denote the total cost incurred by an online
algorithm ALG and cost(OPT) denote the offline optimal cost (Equa-
tion 1) an agent can incur if it has exact knowledge of all future
bandwidth at the beginning. We say ALG achieves a dynamic regret
of 𝑅if cost(ALG) −cost(OPT) ≤𝑅always holds, and ALG achieves a
competitive ratio of 𝐶if cost(ALG) ≤𝐶· cost(OPT) always holds.
The key idea underlying our theoretical analysis is to leverage the
exponential decay property to bound (i) the error that SODA incurs
at every intermediate time step 𝑛due to its limited prediction power
( ˆ𝜔𝑚|𝑛−1 ≠𝜔𝑚, 𝐾≪𝑁), and (ii) the aggregation of such errors over
the whole horizon 𝑁. Specifically, we define the notion of per-step
error at a time step 𝑛as the distance between SODA’s buffer/action
pair and the optimal buffer/action pair that one could reach with
exact predictions of all future bandwidths 𝜔𝑛,𝜔𝑛+1, . . . ,𝜔𝑁given
the previous buffer/action pair (𝑥𝑛−1,𝑢𝑛−1) (Definition A.2). Using
the principle of optimality, we reformulate the optimal buffer/action
pair as an entry of the optimal trajectory from time 𝑛to (𝑛+ 𝐾−1)
so that we can directly compare it with SODA’s buffer/action pair
under the exponentially decaying perturbation. Thus, we establish a
bound on the per-step error that depends on the errors of predicting
future bandwidths and the prediction horizon 𝐾(Lemma A.4). On
the other hand, we also show that the aggregation of per-step
errors does not grow linearly in time because the exponentially
decaying perturbation guarantees that the impact of each previous
per-step error vanishes exponentially over time (Lemma A.5). We
present a proof outline and the detailed proofs in Appendix A.
To prove the exponentially decaying perturbation, we require a
technical assumption that guarantees the controller can “reach”
any desired buffer level by choosing the largest/smallest bitrate
(see Assumption A.1 in Appendix A for the formal statement). This
assumption is used to eliminate extreme boundary cases in the
analysis, but we find SODA empirically performs very well even
when this assumption is not strictly satisfied.
In this section, we set Δ𝑡= 1, R = [𝑟min,𝑟max], and 𝑣(𝑟) =
1/𝑟. Our results can apply to other distortion cost functions, e.g.,
𝑣(𝑟) = log(𝑟max/𝑟), as long as certain regularity conditions hold;
see Appendix B for a discussion.
4.1
Exact Predictions
When the bandwidth predictions are accurate, a small prediction
horizon is sufficient for SODA to achieve near-optimal performance.
In practice, it is desirable to use a relatively small prediction hori-
zon for a predictive controller like SODA because prediction errors
grow dramatically as we predict further into the future. Fortunately,
the exponential decay property that ensures good performance
with only a few predictions. More formally, we present a theorem
showing that a small prediction horizon is sufficient for SODA to
achieve near-optimal performance when the predictions within this
window are accurate (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1).
Theorem 4.1. [Informal] When the predictions of the bandwidth in
future 𝐾steps are exact (i.e., ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1)
and the prediction horizon 𝐾≥𝑂(1), SODA achieves a dynamic
regret of 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 +𝑂(𝜌𝐾), where 𝜌< 1
is the decay factor of the exponentially decaying perturbation property.
The formal statement of Theorem 4.1 is given in Theorem A.3
in Appendix A. This result implies that SODA’s performance ap-
proaches that of the optimal sequence of decisions exponentially
fast in the prediction horizon size 𝐾; thus, only a small prediction
horizon length is necessary to obtain good performance.
4.2
Inexact Predictions
We now relax the exact prediction assumption to prove SODA’s
robustness to a certain level of prediction errors thanks to its expo-
nentially decaying perturbation property.
Theorem 4.2. [Informal] Suppose the prediction error at each
step is bounded above. The buffer level of SODA will never hit the
constraint boundary, i.e., 0 < 𝑥𝑛< 𝑥max. Further, define E = 𝜌2𝐾𝑁+
Í𝐾
𝜅=1 𝜌𝜅𝐸𝜅, where 𝐸𝜅is the total squared error for predicting 𝜅steps
into the future. SODA achieves a dynamic regret of 𝑂(
√
E𝑁+ E).
The formal statement of Theorem 4.2 is given in Theorem A.8 in
Appendix A. Theorem 4.2 shows that, if the buffer costs are “steep”
and the prediction errors on the bandwidth are relatively small,
SODA can achieve a sequence of buffer levels that stay safely away
from the boundaries of buffer constraint [0,𝑥max]. The dynamic
regret of SODA depends on the magnitude of the prediction errors
and the regret improves when the errors become smaller. SODA
acquires this guarantee thanks to its maintenance of the buffer
near a target level ¯𝑥. In contrast, RobustMPC [17] doesn’t offer the
same performance guarantee, thus even small bandwidth prediction
errors can cause the video to rebuffer if the buffer level is near zero.
4.3
Computational Efficiency
Solving the predictive optimization problem to determine the exact
optimal solution can be unrealistic in the application of adaptive
bitrate streaming, where each decision needs to be made in the
618
```


### Pagina 7
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
minimum possible time. A critical observation underlying the im-
plementation of SODA is that it is sufficient to search only for bitrate
sequences that are increasing or decreasing monotonically. We
provide a theoretical justification in the following theorem.
Theorem 4.3. [Informal] Suppose SODA is given the predictions
that satisfy ˆ𝜔𝑛|𝑛−1 = · · · = ˆ𝜔𝑛+𝐾−1|𝑛−1 at an intermediate time step
𝑛. Then, the bitrate trajectory solved by SODA can be approximated
by a feasible monotonic bitrate trajectory with an error of 𝑂 𝐾/√𝛾.
The formal statement of Theorem 4.3 is given in Theorem A.9
in Appendix A. Theorem 4.3 shows that the true optimal solution
becomes closer to monotonic as the weight 𝛾of switching costs
increases. While the theoretical bound can be conservative, we find
that even with moderate 𝛾, the (discrete) decision made under the
monotonic heuristic is usually identical to the true optimal solution
on a real trajectory (see Figure 8).
5
IMPLEMENTATION DETAILS
Given the theoretical design insights, we now discuss the practical
implementation of the high-level design described in Section 3.
There are three practical concerns that require discussion: (i) how
to translate the time-based design to the segment-based schema;
(ii) how to incorporate throughput predictions robustly; and (iii)
how to solve the predictive optimization problem efficiently.
5.1
Segment-Based Schema
SODA is intrinsically a time-based controller, but in practice, a video
must be downloaded segment by segment according to the MPEG-
DASH standard. To reconcile with this requirement, we keep the
optimization phase as is in the time-based format and empirically
set Δ𝑡to be equal to the segment length. This choice is justified
by the fact that in the steady state, the download time of a video
segment is expected to be close to the segment length or much less
than that [29]. To further minimize the likelihood of committing
to a bitrate for significantly longer than Δ𝑡, we introduce another
heuristic that the controller must select a bitrate no higher than
min{𝑟∈R : 𝑟≥ˆ𝜔}.
5.2
Incorporating Predictions Robustly
According to Section 4.2, SODA is robust against prediction errors
by design as long as there is no systematic bias in prediction er-
rors. Given the diverse network conditions in the wild, we prefer
simple throughput predictors which makes SODA highly deployable
since there is no dependence on complex throughput predictors.
In practice, we observe that prediction accuracy degrades as the
prediction horizon increases (see Figure 7). Therefore, we limit the
prediction horizon length to at most 10 s. This is also supported by
our finding in Section 4.1 that a longer prediction horizon yields
diminishing returns.
5.3
Efficient Approximate Solver
At SODA’s core is the predictive optimization problem described
in Section 3.3. Unfortunately, solving this problem on the fly is
computationally challenging. One may propose enumerating all
combinations of discretized throughputs, buffer levels, and previous
bitrates in the form of an offline computed lookup table, as is the
Figure 7: We profiled the performance of the two throughput
predictors shipped with dash.js [64], i.e., moving average
predictor and exponential moving average predictor. Both
predictors have a high mean correlation (around 50%) in the
immediate future but a very low mean correlation (around
15%) in the far future.
Algorithm 1: SODA’s efficient approximate optimization
solver. SearchDown is omitted for brevity due to symmetry.
The current buffer level and the previous bitrate are denoted
by 𝑥0 and 𝑟0 respectively.
function Search( ˆ𝜔,𝑥0,𝑟0, 𝐾)
(𝑟∗up, obj∗up) ←SearchUp( ˆ𝜔,𝑥0,𝑟0, 𝐾)
(𝑟∗
down, obj∗
down) ←SearchDown( ˆ𝜔,𝑥0,𝑟0, 𝐾)
return 𝑟∗up ≠null ∧obj∗up < obj∗
down ? 𝑟∗up : 𝑟∗
down
function SearchUp( ˆ𝜔,𝑥0,𝑟0, 𝐾)
𝑟∗
1 ←null, obj∗←∞
foreach 𝑟1 ∈{𝑟∈R : 𝑟> 𝑟0}
𝑥1 ←𝑥0 + ˆ𝜔Δ𝑡/𝑟1 −Δ𝑡
if 𝑥1 < 0 then continue
obj ←𝑣(𝑟1) · ˆ𝜔Δ𝑡/𝑟1 + 𝛽· 𝑏(𝑥1) + 𝛾· 𝑐(𝑟1,𝑟0)
if 𝐾> 1 then
(𝑟∗
2, Δobj∗) ←SearchUp( ˆ𝜔,𝑥1,𝑟1, 𝐾−1)
if 𝑟∗
2 = null then continue
obj ←obj + Δobj∗
if obj < obj∗then 𝑟∗
1 ←𝑟1, obj∗←obj
return (𝑟∗
1, obj∗)
case in FastMPC [17], however, this is neither flexible nor scalable
in practice. A lookup table is specific to a particular set of bitrates,
maximum player buffer, segment durations and byte sizes etc. thus
needs to be recomputed when any of these quantities change. Fur-
thermore, computing this lookup in live streaming is undesirable
due to the additional computational and latency overhead it incurs.
Instead, we opt for an efficient approximate solver.
SODA’s approximate solver is designed to take advantage of the
structure of the optimal solution presented in Section 4.3. Instead of
searching through all possible bitrate sequences in the prediction
horizon, the approximate solver only considers monotonic bitrate
sequences, i.e., it imposes an additional constraint that 𝑟𝑛−1 ≤𝑟𝑛≤
. . . ≤𝑟𝑛+𝐾−1 or 𝑟𝑛−1 ≥𝑟𝑛≥. . . ≥𝑟𝑛+𝐾−1. The pseudocode for a
recursive implementation is shown in Algorithm 1.
619
```


### Pagina 8
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Figure 8: The probability that the bitrate decision produced
by the approximate solver is different from that produced
by the brute-force solver quickly converges to 0 as switching
cost weight increases.
The approximate solver reduces the time complexity from O(|R|𝐾)
(exponential in 𝐾) in the case of a brute-force search over all possi-
ble bitrate sequences in the prediction horizon down to O
 |R|+𝐾
𝐾

(polynomial in 𝐾) and has a space complexity of O(𝐾) only. The
time complexity can be further reduced by limiting extreme bitrate
switches. In practice, SODA searches through at most around 200
bitrate sequences. According to our production deployment expe-
rience, the approximate solver did not impose a runtime burden
even on low-end devices such as set-top boxes, which shows that
SODA is highly practical.
Empirical results are shown in Figure 8 to validate the near-
optimality of bitrate decisions produced by the approximate solver.
For each algorithm configuration, we uniformly sample a million
situations with different throughputs, buffer levels, and previous
bitrates. Then, we count the probability that the bitrate decision
produced by the approximate solver is different from that produced
by the brute-force solver. The difference is negligible for a reason-
able switching cost weight, e.g., below 5% for 𝐾= 4 and a relative
switching cost weight of 2. Throughout the evaluation sections, we
use this efficient implementation of SODA.
6
EVALUATION
To thoroughly evaluate SODA’s performance, we conducted three
levels of empirical evaluation: (i) large-scale numerical simulations,
(ii) prototype evaluation in Puffer [46], and (iii) production deploy-
ment in Amazon Prime Video. This funnel approach allowed us to
first systematically evaluate SODA against a variety of baselines in
a wide range of controlled environments. Later, we narrowed the
comparison target to a deployed and fine-tuned ABR controller in
production using A/B tests on real user sessions.
Performance Metrics. To maintain consistency in terms of perfor-
mance metrics with prior works such as [17, 22, 24, 46], a similar
definition of QoE is adopted that consists of mean utility, rebuffer-
ing ratio, and switching rate. These correspond to the three main
desired properties of adaptive bitrate streaming, i.e., high video
quality, shorter rebuffering time, and less bitrate switching. All
three QoE components are normalized between 0 and 1 for ease of
interpretation. The precise definitions are as follows:
• Mean Utility: Unless otherwise noted, we use the commonly-
used logarithmic utility function:
¯𝑣= 1
𝑁
𝑁
∑︁
𝑖=1
log(𝑟𝑖/𝑟min)
log(𝑟max/𝑟min) .
• Rebuffering Ratio: The ratio of the total rebuffering time to the
session duration, i.e., 𝜌rebuf = 𝑇rebuf/𝑇.
• Switching Rate: Bitrate switch count divided by segment count
minus one, i.e., 𝑝switch = 𝑁switch/(𝑁−1).
The QoE score is simply a linear combination of the three QoE
components, i.e., QoE = ¯𝑣−𝛽· 𝜌rebuf −𝛾· 𝑝switch. In this work,
we chose 𝛽= 10 and 𝛾= 1 to reflect the high importance of
minimizing rebuffering time. To establish fair comparisons, we
report the individual QoE components along with the QoE score.
6.1
Numerical Simulations
To perform large-scale numerical simulations, we implemented a
highly optimized ABR simulator in C++ derived from Sabre [36].
The simulation accuracy of Sabre has been empirically validated
against dash.js [64], the reference player for MPEG-DASH. We
configured the simulator to allow a maximum buffer length of 20
seconds to replicate the typical live streaming conditions.
6.1.1
Experimental Setup. Our network dataset consists of about
38,000 hours of throughput traces compiled from the following
three public sources:
• Puffer Dataset [46]: We downloaded and parsed all throughput
traces from the Puffer platform during the time period of January
2023 to June 2023.
• 5G Dataset [41]: A 5G network dataset from a major Irish mobile
operator under both static and moving scenarios while down-
loading online content.
• 4G Dataset [27]: A 4G network dataset from two major Irish
mobile operators under both static and moving scenarios while
downloading online content.
For all three datasets, we filtered out sessions shorter than 10 min-
utes and divided long sessions into consecutive 10-minute sessions,
resulting in 230,322 sessions from the Puffer dataset, 88 sessions
from the 5G dataset, and 187 sessions from the 4G dataset. Fig-
ure 9 illustrates the wide range of network conditions covered by
these datasets. In general, the Puffer dataset represents better net-
work conditions than the 5G and 4G datasets. The latter have much
lower mean throughput and higher variance, thus posing a bigger
challenge for ABR controllers.
To fully exercise our datasets, we considered a high-frame-rate
4K video encoded according to the YouTube recommended settings
(1.5, 4, 7.5, 12, 24, and 60 Mb/s) [65] with a segment length of 2
seconds. For the 5G and 4G datasets, we considered the same video
with the two highest bitrates removed. Finally, for throughput
prediction, we opted for the exponential moving average (EMA)
predictor, the default throughput predictor in dash.js.
6.1.2
Baseline ABR Controllers. We compared SODA against the
following ABR controllers representative of each of the common
ABR controller categories, i.e., throughput-based, buffer-based, and
hybrid. They were tuned to our best efforts for our network datasets.
620
```


### Pagina 9
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Figure 9: The mean throughput of the Puffer, 5G, and 4G datasets are 57.1, 31.3, and 13.0 Mb/s. The mean relative standard
deviations of throughput of the Puffer, 5G, and 4G dataset are 47.2%, 133%, and 80.6%.
• HYB [24]: A heuristic throughput-based ABR controller that se-
lects the highest bitrate without rebuffering.
• BOLA [36]: A buffer-based ABR controller derived from Lyapunov
optimization. It provides theoretical guarantees about utility and
rebuffering time only.
• Dynamic [44]: A production version of BOLA that dynamically
switches between buffer mode and throughput mode in response
to changes in network conditions. Additionally, it has low-buffer
safety heuristic to reduce rebuffering and a switching avoidance
heuristic to mitigate bitrate switching. It is the default ABR con-
troller in dash.js.
• MPC [17]: One application of model predictive control to adap-
tive streaming that models utility, rebuffering time, and bitrate
switching, without theoretical guarantees.
6.1.3
QoE Performance. The aggregate statistics for QoE scores
and individual QoE components under each network dataset are
shown in Figure 10. To better understand how the performance of
different ABR controllers react to the intrinsic volatility of network
conditions, we split the Puffer dataset into four quarters according
to the relative standard deviation of throughput (Q1 represents
the most stable network conditions, while Q4 represents the most
volatile network conditions). In general, the more volatile network
conditions are, the more the QoE performance of any ABR con-
troller degrades, as evidenced by the trend in Figure 10 from left
to right. Nonetheless, SODA consistently outperforms baseline ABR
controllers under all network conditions. The improvement in terms
of mean QoE scores compared to the best baseline across different
network datasets ranges from 9.55% to 27.8%, which mainly stems
from improvement in terms of smoothness (shorter rebuffering
time and less bitrate switching). We discuss the improvement of
SODA over each baseline ABR controller below:
• SODA vs HYB. HYB is not as robust as SODA under volatile network
conditions. In addition, it switches up to 215% more since it does
not consider bitrate switching.
• SODA vs BOLA & Dynamic. As mainly buffer-based ABR con-
trollers, BOLA and Dynamic are fairly robust against volatile net-
work conditions. Dynamic’s performance is what one would ex-
pect in a typical production environment. Nonetheless, SODA is
able to achieve similar mean utilities without sacrificing mean
rebuffering ratios, proving its outstanding robustness as a hybrid
ABR controller. Where SODA really shines though is its signifi-
cantly lower mean switching rates. Despite Dynamic’s switch-
ing avoidance heuristic, SODA cuts down mean switching rates
by as much as 70.4%, which demonstrates the superiority of
theoretically-sound design.
• SODA vs MPC. MPC has high mean utilities and low mean switching
rates under stable network conditions (see Puffer (Q1 variance)
in Figure 10). However, the performance of MPC is tightly coupled
with the intrinsic volatility of network conditions. Specifically,
MPC suffers a lot in terms of mean rebuffering ratios especially
under mobile network conditions. By contrast, SODA does not
have this issue since it is robust against prediction errors by
design, making it much more suitable for production deployment.
6.1.4
Intrinsic Sensitivity to Prediction Accuracy. In an effort to im-
prove throughput prediction accuracy, several prior works have fo-
cused on designing more sophisticated throughput predictors such
as C2SP [20], Fugu [46], and Xatu [50]. While these throughput pre-
dictors may offer higher prediction accuracy, they are complex and
difficult to deploy, especially on compute or memory constrained
devices [58]. In Section 4.2, we have showed that SODA is robust
against prediction errors by design and does not require a sophisti-
cated throughput predictor. We now demonstrate this empirically.
First, we replaced the throughput predictor used in simulations
with a perfect short-term throughput predictor. Next, we gradually
introduced more and more white noise to the perfect throughput
predictions and observed how different ABR controllers behave
accordingly. This experiment was conducted on a random subset
of our network datasets with a size of 10,000 sessions. Note that
throughput prediction discounts were turned off for all ABR con-
trollers to reveal their intrinsic robustness.1
The results are shown in Figure 11, from which we observe
that all hybrid ABR controllers that take throughput predictions
into account will inevitably be affected by prediction errors to
some extent (BOLA is not affected since it is purely buffer-based).
Nonetheless, SODA still consistently outperforms all baseline ABR
controllers up to a noise level of 50%. For reference, EMA predictor
has an empirical noise level of about 30% on the same sessions. More
importantly, the QoE degradation of SODA is minimal up to the
reference point of EMA predictor, i.e., about 10%, which reinforces
1The ranking between different ABR controllers in this section may be different from
that in Figure 10, which reveals that the robustness of certain ABR controllers should
be attribute to throughput prediction discounts instead of intrinsic designs.
621
```


### Pagina 10
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Figure 10: The mean QoE scores, utilities, rebuffering ratios and switching rates of SODA and baseline ABR controllers under
each network dataset. The Puffer dataset is split into four quarters according the throughput variance (Q1 being lowest while
Q4 being highest). SODA has consistently higher mean QoE scores and lower switching rates than all baseline ABR controllers
under all network conditions. (Error bars represent 95% confidence intervals.)
Figure 11: The mean QoE scores for SODA and baseline ABR
controllers under variable amounts of white noise. (The error
bars represent 95% confidence intervals.)
the idea that a practical deployment of SODA does not require a
sophisticated throughput predictor.2
2In practice, we observe that EMA predictor is actually much better than a perfect
short-term predictor with 30% white noise because the noise patterns are different,
which means that real gap is less than 10%.
6.2
Prototype Evaluation
We next present emulation results from our local client-server
deployment where we implemented SODA in the Puffer platform [46].
Thanks to Chrome DevTools’ new capability to throttle WebSocket
requests [59], we could replay our network datasets directly in
Chrome using WebDriver [63]. The results are intended to highlight
the robustness of different ABR controllers under actual browser-
based playback. For these experiments, we allowed a maximum
buffer length of 15 seconds, as set by Puffer.
6.2.1
Experimental Setup. The video source was a news clip en-
coded in five different resolutions (426 × 240, 640 × 360, 854 × 480,
1280 × 720, and 1920 × 1080) with a constant rate factor of 26 and
a segment length of 2 seconds. To be fair to those learning-based
ABR controllers trained specifically for the Puffer platform, we only
considered the Puffer dataset. Since the average bitrate of the high-
est resolution is only about 2 Mb/s, we take a random subset of the
Puffer dataset with a size of 1,000 sessions whose mean throughput
is below 2 Mb/s to create challenging scenarios.
622
```


### Pagina 11
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
6.2.2
Baseline ABR Controllers. In response to the growing interest
in learning-based throughput predictors and ABR controllers in
the research community, we included two representative learning-
based ABR controllers for local deployment on top of the major
baseline ABR controllers from numerical simulations:
• Fugu [46]: Developed as part of the Puffer project, it features a
learning-based stochastic throughput predictor, while its under-
lying control algorithm is similar to MPC.
• CausalSimRL [60]: A modern implementation of a reinforcement
learning (RL)-based ABR controller Pensieve [22]. It is trained
using CausalSim for the Puffer platform.
6.2.3
QoE Performance. Puffer employs structure similarity index
measures (SSIM) [4] to quantify utility, thus to compare fairly us-
ing Puffer, we adapt mean utility to normalized mean SSIM, i.e.,
¯𝑣= SSIM/SSIMmax. The definitions of rebuffering ratio, switching
rate, and QoE score remain the same. The aggregate statistics or
QoE scores and individual QoE components across all sessions are
shown in Figure 12. SODA outperforms the best baseline (Fugu) by
30.4% in terms of mean QoE score. More importantly, SODA is the
only ABR controller that achieves low mean rebuffering ratio and
switching rate simultaneously, which translates to superior smooth-
ness of adaptive streaming. We highlight comparisons with the new
baseline ABR controllers below:
• SODA vs MPC & Fugu. MPC and Fugu are grouped together since,
apart from the more sophisticated stochastic throughput pre-
dictor, Fugu shares a similar underlying control algorithm with
MPC. While they both achieve slightly higher mean utilities than
SODA and reasonably low mean switching rates, these benefits
are overshadowed by worse mean rebuffering ratios (230% and
104% worse respectively). Although Fugu partially mitigates the
rebuffering issue due to its stochastic throughput predictor, it is
still not robust enough for challenging network conditions.
• SODA vs CausalSimRL. CausalSimRL achieves slightly higher
mean utility than SODA and a reasonably low mean rebuffering
ratio. However, it switches bitrates 86.3% more often than SODA.
Due to the black-box nature of RL-based ABR controllers, it is
hard to reason why this is the case. In addition, there exists no
straightforward way to tune an RL-based controller in favor of
one particular QoE component without a complete retraining. In
a production environment, it is highly desirable that the trade-off
between different QoE components is tunable.
6.3
Production Deployment
We now describe the results from deploying SODA for live streams
delivered on Amazon Prime Video. The bitrate ladder for these
video streams had the following bitrate rungs {0.2, 0.45, 0.8, 1.2, 1.8,
2, 4, 5, 6.5, 8.0} Mb/s. This range of available bitrates fully exercised
SODA’s bitrate adaptation capability as well as tested its runtime
feasibility on actual devices. The experiment was run on three de-
vice families, including (i) desktops/laptops (HTML5 browsers), (ii)
smart TVs, and (iii) set-top boxes. On all three platforms, SODA used
a simple sliding window-based throughput predictor. All devices
were 20 seconds behind live action, so they could accumulate at
most 20 seconds of buffer. To compare performance with a pro-
duction tuned baseline, we conducted large-scale A/B experiments
where customers were randomly assigned SODA or the production
baseline controller. The experiment ran for more than 1 week with
live streams delivered to more than 10 countries. In total, SODA
sessions logged more than 50,000 streaming hours.
Figure 13 shows SODA’s performance relative to the production
deployed and tuned controller. First, notice that SODA consistently
improves all the metrics across all device families, reducing the
frequency of bitrate switching on set-top boxes by 88.8%. SODA really
shines on HTML5 browsers where it reduced the mean rebuffering
ratio by up to 53.0% in addition to 81.8% reduction in switching.
This is because HTML5 browsers experience more volatility in
network conditions compared to smart TVs and set-top boxes and
thus present greater opportunity for improvement. Finally, notice
that on all three platforms, the average duration of session increased,
with 5.91% improvement on set-top boxes. Live streaming sessions
for sports events routinely span multiple hours (e.g., 2-hour soccer
broadcast, 3.5-hour cricket broadcast), so a 5.91% increase translates
to more than 5 minutes duration.
Takeaways from Production Deployment. The production
deployment shows that SODA is practical and can be widely deployed
across different device types and network connections. Furthermore,
to achieve its significant performance gains, it is sufficient for SODA
to use simple sliding window-based throughput predictors.
7
RELATED WORK
7.1
Adaptive Bitrate Streaming
Bitrate adaptation has received significant attention from the mul-
timedia research community. Buffer-based controllers like BBA [15]
and BOLA [36, 44] make bitrate decisions based on buffer occu-
pancy, while hybrid controllers like HYB [24], MPC [17] and DYNAMIC
[44] combine throughput predictions with buffer occupancy to
make decisions. SODA belongs to the latter category. There are also
learning-based controllers such as Pensive [22] that utilize rein-
forcement learning to learn a bitrate selection strategy. Another
relevant stream of work focuses on improving the accuracy of
throughput predictions, including CS2P [20], Fugu [46], and Xatu
[50]. Our work makes no assumption on the quality of throughput
predictions and does not require a sophisticated throughput pre-
dictor. Past works have also considered upgrading the downloaded
segments through replacement [36] which we do not consider in
this paper.
7.2
Video Quality of Experience
The advent of video content delivery networks [2, 6] in the late
1990’s led to efforts in industry to define and measure quality met-
rics for video delivery. Since then the quality of video delivery is
a well studied topic with early work on the Akamai Stream Ana-
lyzer system which defined metrics such as startup time, rebuffer
ratio, bitrate and failures etc and measured these metrics using data
derived from video players deployed around the world [3, 66]. Sub-
sequently, [7] showed that a 1% increase in rebuffering correlated
with a 3-minute reduction in the amount of time users streamed
live content. A study on YouTube [21] found that bitrate fluctua-
tions strongly correlate with a user abandoning the session. Beyond
correlations, the first study [9] to establish a causal relationship
between video quality and user behavior used quasi-experimental
623
```


### Pagina 12
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Figure 12: The mean QoE scores, utilities, rebuffering ratios, and switching rates from local deployment. SODA again has the
highest mean QoE score and unlike all other baselines, simultaneously achieves ultra low mean rebuffering ratio and switching
rate. (Error bars represent 95% confidence intervals.)
Figure 13: The change in mean viewing durations (higher is
better), bitrates (higher is better), rebuffering ratios (lower is
better), and switching rates (lower is better) of SODA compared
to the production baseline.
designs (QEDs) to quantify the causal (adverse) impact of startup
delay, rebuffering, and failures on user engagement, abandonment,
and repeat viewership. A related work [11] built predictive models
for user engagement based on QoE metrics. Our work leverages
insights from these works in our ABR controller design.
7.3
Smoothed Online Convex Optimization
Our algorithm builds on recent developments in smoothed online
convex optimization (SOCO), a variant of online optimization that
penalizes switching between consecutive decisions via a “switch-
ing cost.” [25, 33, 34]. In recent years, the design and analysis of
algorithms for SOCO has received considerable attention, e.g., [14,
25, 31, 32, 34, 37], with optimal online algorithms emerging in vari-
ous settings [33, 42, 48, 62] and a variety of applications receiving
attention [10, 12, 26, 43, 53, 55, 57]. SOCO’s switching cost model
inspires our design of SODA for video streaming.
Our mathematical formulation of adaptive video streaming can
be viewed as a specific example of online (optimal) control [54].
Similar to online optimization, online control seeks to design a
controller to minimize the total cost incurred over a finite horizon.
The theoretical bounds in this paper are most related to works that
study how future predictions can improve online controller perfor-
mance [39, 47, 49, 52]. Our proofs follow an analytic framework for
studying MPC-based algorithms via exponentially decaying pertur-
bation bounds [49, 55, 56]. Our work shows that this decay property
holds under our model of adaptive video streaming, allowing us to
establish performance guarantees for SODA.
8
LIMITATIONS AND FUTURE WORK
An emerging genre (but, still a small fraction) of live streaming is
ultra-low latency live streams where the delay between the capture
of an event and its display to the user is required to be of the order
of a few seconds, as opposed to 10 to 20 seconds for the traditional
live streams used in our current work. In future work, we would
like to study if our SOCO-based strategy can be adapted for ultra-
low latency live streams with buffer lengths in the order of a few
seconds. The main challenge with ultra-small buffer sizes is that it
is harder to prevent rebuffering and bitrate switching in this regime
as the ABR controller needs to react to network fluctuations in a
significantly shorter amount of time.
9
CONCLUSION
In this work, we propose a smoothness-optimized dynamic adaptive
(SODA) controller that addresses this issue in a theoretically sound
way. Thanks to SODA’s robustness against prediction errors and
low runtime complexity, it is readily deployable in a wide range
of production environments. Through numerical simulations and
prototype evaluation, we show that SODA consistently outperforms
the state-of-the-art baselines. More importantly, we deployed SODA
in a major video streaming provider where SODA significantly re-
duced bitrate switching by up to 88.8% compared to a fine-tuned
production baseline. SODA’s novel time-based ABR formulation and
theoretical insights shed new light on how to achieve consistent
high-quality video streaming.
ACKNOWLEDGMENTS
We thank the anonymous reviewers and our shepherd for their valu-
able feedback, as well as colleagues at Amazon Prime Video for their
support with the production deployment of SODA. This work was
funded by NSF under grants CAREER-204564, CCF-2325956, CNS-
1763617, CNS-1901137, CNS-2102963, CNS-2106299, CNS-2106403,
CNS-2106463, CNS-2146814, CPS-2136197, and NGSDI-2105648, as
well as an Amazon Research Award. The research of Yiheng Lin
was additionally supported by Amazon AI4Science Fellowship and
PIMCO Graduate Fellowship in Data Science.
624
```


### Pagina 13
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
REFERENCES
[1]
Mun Choon Chan and Ramachandran Ramjee. 2002. TCP/IP Performance
over 3G Wireless Links with Rate and Delay Variation. In Proceedings of the
8th Annual International Conference on Mobile Computing and Networking
(MobiCom ’02). Atlanta, Georgia, USA, 71–82. isbn: 158113486X. doi: 10.1145
/570645.570655.
[2]
John Dilley, Bruce M. Maggs, Jay Parikh, Harald Prokop, Ramesh K. Sitaraman,
and William E. Weihl. 2002. Globally Distributed Content Delivery. IEEE Internet
Computing, 6, 5, 50–58.
[3]
R.K. Sitaraman and R.W. Barton. 2003. Method and apparatus for measuring
stream availability, quality and performance. US Patent 7,010,598. (Feb. 2003).
[4]
Z. Wang, A.C. Bovik, H.R. Sheikh, and E.P. Simoncelli. 2004. Image Quality
Assessment: From Error Visibility to Structural Similarity. IEEE Transactions
on Image Processing, 13, (Apr. 2004), 600–612, 4, (Apr. 2004). doi: 10.1109/TIP.2
003.819861.
[5]
Junxian Huang, Qiang Xu, Birjodh Tiwana, Z. Morley Mao, Ming Zhang, and
Paramvir Bahl. 2010. Anatomizing Application Performance Differences on
Smartphones. In Proceedings of the 8th International Conference on Mobile
Systems, Applications, and Services (MobiSys ’10). San Francisco, California,
USA, 165–178. isbn: 9781605589855. doi: 10.1145/1814433.1814452.
[6]
E. Nygren, Ramesh K. Sitaraman, and J. Sun. 2010. The Akamai Network: A
platform for high-performance Internet applications. ACM SIGOPS Operating
Systems Review, 44, 3, 2–19.
[7]
Florin Dobrian, Vyas Sekar, Asad Awan, Ion Stoica, Dilip Joseph, Aditya Gan-
jam, Jibin Zhan, and Hui Zhang. 2011. Understanding the Impact of Video Qual-
ity on User Engagement. In Proceedings of the ACM SIGCOMM 2011 Conference
(SIGCOMM ’11). Toronto, Ontario, Canada, 362–373. isbn: 9781450307970. doi:
10.1145/2018436.2018478.
[8]
Te-Yuan Huang, Nikhil Handigol, Brandon Heller, Nick McKeown, and Ramesh
Johari. 2012. Confused, timid, and unstable. In Proceedings of the 2012 Internet
Measurement Conference. ACM, New York, NY, USA, (Nov. 2012), 225–238. isbn:
9781450317054. doi: 10.1145/2398776.2398800.
[9]
S. Shunmuga Krishnan and Ramesh K. Sitaraman. 2012. Video Stream Qual-
ity Impacts Viewer Behavior: Inferring Causality Using Quasi-Experimental
Designs. In Proceedings of the 2012 Internet Measurement Conference (IMC ’12).
Boston, Massachusetts, USA, 211–224. isbn: 9781450317054. doi: 10.1145/2398
776.2398799.
[10]
Minghong Lin, Zhenhua Liu, Adam Wierman, and Lachlan LH Andrew. 2012.
Online algorithms for geographical load balancing. In Proceedings of the Inter-
national Green Computing Conference (IGCC), 1–10.
[11]
Athula Balachandran, Vyas Sekar, Aditya Akella, Srinivasan Seshan, Ion Stoica,
and Hui Zhang. 2013. Developing a predictive model of quality of experience
for internet video. SIGCOMM Comput. Commun. Rev., 43, 4, (Aug. 2013), 339–
350. doi: 10.1145/2534169.2486025.
[12]
Minghong Lin, Adam Wierman, Lachlan L. H. Andrew, and Eno Thereska.
2013. Dynamic Right-Sizing for Power-Proportional Data Centers. IEEE/ACM
Transactions on Networking, 21, 5, (Oct. 2013), 1378–1391. doi: 10.1109/TNET.2
012.2226216.
[13]
Masoud Badiei, Na Li, and Adam Wierman. 2015. Online convex optimization
with ramp constraints. In 2015 54th IEEE Conference on Decision and Control
(CDC). IEEE, 6730–6736.
[14]
Nikhil Bansal, Anupam Gupta, Ravishankar Krishnaswamy, Kirk Pruhs, Kevin
Schewior, and Cliff Stein. 2015. A 2-Competitive Algorithm For Online Convex
Optimization With Switching Costs. In Approximation, Randomization, and
Combinatorial Optimization. Algorithms and Techniques (APPROX/RANDOM
2015) (Leibniz International Proceedings in Informatics (LIPIcs)). Naveen Garg,
Klaus Jansen, Anup Rao, and José D. P. Rolim, (Eds.) Vol. 40. Schloss Dagstuhl–Leibniz-
Zentrum fuer Informatik, Dagstuhl, Germany, 96–109. doi: 10.4230/LIPIcs
.APPROX-RANDOM.2015.96.
[15]
Te-Yuan Huang, Ramesh Johari, Nick McKeown, Matthew Trunnell, and Mark
Watson. 2015. A Buffer-Based Approach to Rate Adaptation: Evidence from
a Large Video Streaming Service. ACM SIGCOMM Computer Communication
Review, 44, (Feb. 2015), 187–198, 4, (Feb. 2015). doi: 10.1145/2740070.2626296.
[16]
Yan Liu and Jack Y. B. Lee. 2015. An Empirical Study of Throughput Prediction
in Mobile Data Networks. In 2015 IEEE Global Communications Conference
(GLOBECOM), 1–6. doi: 10.1109/GLOCOM.2015.7417858.
[17]
Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli. 2015. A Control-
Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP. In Pro-
ceedings of the 2015 ACM Conference on Special Interest Group on Data Commu-
nication. ACM, New York, NY, USA, (Aug. 2015), 325–338. isbn: 9781450335423.
doi: 10.1145/2785956.2787486.
[18]
Mojgan Ghasemi, Partha Kanuparthy, Ahmed Mansy, Theophilus Benson, and
Jennifer Rexford. 2016. Performance Characterization of a Commercial Video
Streaming Service. In Proceedings of the 2016 Internet Measurement Conference.
ACM, New York, NY, USA, (Nov. 2016), 499–511. isbn: 9781450345262. doi:
10.1145/2987443.2987481.
[19]
he1enh. 2016. Reproducing Network Research. (May 2016). https://reproducin
gnetworkresearch.wordpress.com/2016/05/30/cs244-16-failed-experiments-
with-fastmpc-integrating-rate-based-adaptive-streaming-into-vlc/.
[20]
Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang,
Tao Liu, and Bruno Sinopoli. 2016. CS2P: Improving Video Bitrate Selection
and Adaptation with Data-Driven Throughput Prediction. In Proceedings of
the 2016 ACM SIGCOMM Conference. ACM, New York, NY, USA, (Aug. 2016),
272–285. isbn: 9781450341936. doi: 10.1145/2934872.2934898.
[21]
Christos George Bampis, Zhi Li, Anush Krishna Moorthy, Ioannis Katsavouni-
dis, Anne Aaron, and Alan Conrad Bovik. 2017. Study of Temporal Effects on
Subjective Video Quality of Experience. IEEE Transactions on Image Processing,
26, 11, 5217–5231. doi: 10.1109/TIP.2017.2729891.
[22]
Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. 2017. Neural Adap-
tive Video Streaming with Pensieve. In ACM, (Aug. 2017), 197–210. isbn:
9781450346535. doi: 10.1145/3098822.3098843.
[23]
Yanyuan Qin, Ruofan Jin, Shuai Hao, Krishna R. Pattipati, Feng Qian, Sub-
habrata Sen, Bing Wang, and Chaoqun Yue. 2017. A control theoretic approach
to ABR video streaming: A fresh look at PID-based rate adaptation. In IEEE
INFOCOM 2017 - IEEE Conference on Computer Communications. IEEE, (May
2017), 1–9. isbn: 978-1-5090-5336-0. doi: 10.1109/INFOCOM.2017.8057056.
[24]
Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen,
Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2018. Oboe:
Auto-Tuning Video ABR Algorithms to Network Conditions. In ACM, (Aug.
2018), 44–58. isbn: 9781450355674. doi: 10.1145/3230543.3230558.
[25]
Niangjun Chen, Gautam Goel, and Adam Wierman. 2018. Smoothed Online
Convex Optimization in High Dimensions via Online Balanced Descent. In
Proceedings of Conference On Learning Theory (COLT), 1574–1594.
[26]
Yingying Li, Guannan Qu, and Na Li. 2018. Online Optimization with Predic-
tions and Switching Costs: Fast Algorithms and the Fundamental Limit. (2018).
arXiv: 1801.07780v3 [math.OC].
[27]
Darijo Raca, Jason J. Quinlan, Ahmed H. Zahran, and Cormac J. Sreenan. 2018.
Beyond Throughput: A 4G LTE Dataset with Channel and Context Metrics. In
Proceedings of the 9th ACM Multimedia Systems Conference. ACM, New York, NY,
USA, (June 2018), 460–465. isbn: 9781450351928. doi: 10.1145/3204949.3208123.
[28]
Naman Agarwal, Brian Bullins, Elad Hazan, Sham Kakade, and Karan Singh.
2019. Online control with adversarial disturbances. In International Conference
on Machine Learning. PMLR, 111–119.
[29]
Zahaib Akhtar, Yaguang Li, Ramesh Govindan, Emir Halepovic, Shuai Hao, Yan
Liu, and Subhabrata Sen. 2019. AViC: A Cache for Adaptive Bitrate Video. In
Proceedings of the 15th International Conference on Emerging Networking Exper-
iments And Technologies (CoNEXT ’19). Association for Computing Machinery,
Orlando, Florida, 305–317. isbn: 9781450369985. doi: 10.1145/3359989.3365423.
[30]
Aaron D Ames, Samuel Coogan, Magnus Egerstedt, Gennaro Notomista, Koushil
Sreenath, and Paulo Tabuada. 2019. Control barrier functions: theory and ap-
plications. In 2019 18th European control conference (ECC). IEEE, 3420–3431.
[31]
C.J. Argue, Sébastien Bubeck, Michael B. Cohen, Anupam Gupta, and Yin
Tat Lee. 2019. A Nearly-Linear Bound for Chasing Nested Convex Bodies. In
Proceedings of the 2019 Annual ACM-SIAM Symposium on Discrete Algorithms
(SODA). Proceedings. Society for Industrial and Applied Mathematics, (Jan.
2019), 117–122. doi: 10.1137/1.9781611975482.8.
[32]
Sébastien Bubeck, Bo’az Klartag, Yin Tat Lee, Yuanzhi Li, and Mark Sellke. 2019.
Chasing Nested Convex Bodies Nearly Optimally. In Proceedings of the 2020
ACM-SIAM Symposium on Discrete Algorithms (SODA). Proceedings. Society
for Industrial and Applied Mathematics, (Dec. 2019), 1496–1508. doi: 10.1137/1
.9781611975994.91.
[33]
Gautam Goel, Yiheng Lin, Haoyuan Sun, and Adam Wierman. 2019. Beyond on-
line balanced descent: An optimal algorithm for smoothed online optimization.
Advances in Neural Information Processing Systems, 32.
[34]
Gautam Goel and Adam Wierman. 2019. An Online Algorithm for Smoothed
Regression and LQR Control. In Proceedings of the Machine Learning Research.
Vol. 89, 2504–2513. http://proceedings.mlr.press/v89/goel19a.html.
[35]
Ming Shi, Xiaojun Lin, and Lei Jiao. 2019. On the value of look-ahead in com-
petitive online convex optimization. Proceedings of the ACM on Measurement
and Analysis of Computing Systems, 3, 2, 22.
[36]
Kevin Spiteri, Ramesh Sitaraman, and Daniel Sparacio. 2019. From Theory to
Practice: Improving Bitrate Adaptation in the DASH Reference Player. ACM
Transactions on Multimedia Computing, Communications, and Applications, 15,
2s, (Apr. 2019), 1–29. doi: 10.1145/3336497.
[37]
C. J. Argue, Anupam Gupta, and Guru Guruganesh. 2020. Dimension-Free
Bounds for Chasing Convex Functions. In Proceedings of Thirty Third Conference
on Learning Theory. PMLR, (July 2020), 219–241. Retrieved Feb. 4, 2022 from.
[38]
Sarah Dean, Horia Mania, Nikolai Matni, Benjamin Recht, and Stephen Tu.
2020. On the sample complexity of the linear quadratic regulator. Foundations
of Computational Mathematics, 20, 4, 633–679.
[39]
Yingying Li, Guannan Qu, and Na Li. 2020. Online optimization with predic-
tions and switching costs: Fast algorithms and the fundamental limit. IEEE
Transactions on Automatic Control, 66, 10, 4761–4768.
625
```


### Pagina 14
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
[40]
Emily Marx, Francis Y. Yan, and Keith Winstein. 2020. Implementing BOLA-
BASIC on Puffer: Lessons for the use of SSIM in ABR logic, (Nov. 2020).
[41]
Darijo Raca, Dylan Leahy, Cormac J. Sreenan, and Jason J. Quinlan. 2020.
Beyond Throughput, The Next Generation: A 5G Dataset with Channel and
Context Metrics. In Proceedings of the 11th ACM Multimedia Systems Conference.
ACM, New York, NY, USA, (May 2020), 303–308. isbn: 9781450368452. doi:
10.1145/3339825.3394938.
[42]
Mark Sellke. 2020. Chasing convex bodies optimally. In Proceedings of the
Thirty-First Annual ACM-SIAM Symposium on Discrete Algorithms (SODA ’20).
Society for Industrial and Applied Mathematics, USA, (Jan. 2020), 1509–1518.
Retrieved Oct. 15, 2021 from.
[43]
Guanya Shi, Yiheng Lin, Soon-Jo Chung, Yisong Yue, and Adam Wierman.
2020. Online optimization with memory and competitive control. Advances in
Neural Information Processing Systems, 33, 20636–20647.
[44]
Kevin Spiteri, Rahul Urgaonkar, and Ramesh K. Sitaraman. 2020. BOLA: Near-
Optimal Bitrate Adaptation for Online Videos. IEEE/ACM Transactions on Net-
working, 28, 4, (Aug. 2020), 1698–1711. doi: 10.1109/TNET.2020.2996964.
[45]
Dongzhu Xu, Anfu Zhou, Xinyu Zhang, Guixian Wang, Xi Liu, Congkai An,
Yiming Shi, Liang Liu, and Huadong Ma. 2020. Understanding Operational 5G:
A First Measurement Study on Its Coverage, Performance and Energy Consump-
tion. In (SIGCOMM ’20). Virtual Event, USA, 479–494. isbn: 9781450379557.
doi: 10.1145/3387514.3405882.
[46]
F.Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis, and K.
Winstein. 2020. Learning in Situ: A Randomized Experiment in Video Streaming.
In Proceedings of the 17th USENIX Symposium on Networked Systems Design
and Implementation, NSDI 2020, 495–511. isbn: 9781939133137. https://www.us
enix.org/conference/nsdi20/presentation/yan.
[47]
Chenkai Yu, Guanya Shi, Soon-Jo Chung, Yisong Yue, and Adam Wierman. 2020.
The power of predictions in online control. Advances in Neural Information
Processing Systems, 33, 1994–2004.
[48]
C. J. Argue, Anupam Gupta, Ziye Tang, and Guru Guruganesh. 2021. Chasing
Convex Bodies with Linear Competitive Ratio. Journal of the ACM, 68, 5, 1–10.
doi: 10.1145/3450349.
[49]
Yiheng Lin, Yang Hu, Haoyuan Sun, Guanya Shi, Guannan Qu, and Adam
Wierman. 2021. Perturbation-based Regret Analysis of Predictive Control in
Linear Time Varying Systems. arXiv preprint arXiv:2106.10497.
[50]
Yun Seong Nam, Jianfei Gao, Chandan Bothra, Ehab Ghabashneh, Sanjay Rao,
Bruno Ribeiro, Jibin Zhan, and Hui Zhang. 2021. Xatu: Richer Neural Network
Based Prediction for Video Streaming. Proceedings of the ACM on Measurement
and Analysis of Computing Systems, 5, 3, (Dec. 2021), 1–26. doi: 10.1145/3491056.
[51]
Sungho Shin and Victor M. Zavala. 2021. Controllability and Observability Im-
ply Exponential Decay of Sensitivity in Dynamic Optimization. arXiv preprint
arXiv:2101.06350.
[52]
Runyu Zhang, Yingying Li, and Na Li. 2021. On the regret analysis of online
LQR control with predictions. In 2021 American Control Conference (ACC). IEEE,
697–703.
[53]
Nicolas Christianson, Christopher Yeh, Tongxin Li, Mahdi Torabi Rad, Azarang
Golmohammadi, and Adam Wierman. 2022. Robustifying machine-learned
algorithms for efficient grid operation. In NeurIPS 2022 Workshop on Tackling
Climate Change with Machine Learning. https://www.climatechange.ai/papers
/neurips2022/19.
[54]
Elad Hazan and Karan Singh. 2022. Introduction to online nonstochastic control.
arXiv preprint arXiv:2211.09619.
[55]
Yiheng Lin, Judy Gan, Guannan Qu, Yash Kanoria, and Adam Wierman. 2022.
Decentralized Online Convex Optimization in Networked Systems. In Interna-
tional Conference on Machine Learning. PMLR, 13356–13393.
[56]
Yiheng Lin, Yang Hu, Guannan Qu, Tongxin Li, and Adam Wierman. 2022.
Bounded-Regret MPC via Perturbation Analysis: Prediction Error, Constraints,
and Nonlinearity. arXiv preprint arXiv:2210.12312.
[57]
Weici Pan, Guanya Shi, Yiheng Lin, and Adam Wierman. 2022. Online opti-
mization with feedback delay and nonlinear switching cost. Proceedings of the
ACM on Measurement and Analysis of Computing Systems, 6, 1, 1–34.
[58]
Talha Waheed, Ihsan Ayyub Qazi, Zahaib Akhtar, and Zafar Ayyub Qazi. 2022.
Coal Not Diamonds: How Memory Pressure Falters Mobile Video QoE. In
(CoNEXT ’22). Roma, Italy, 307–320. isbn: 9781450395083. doi: 10.1145/355505
0.3569120.
[59]
Jecelyn Yeen. 2022. What’s New In DevTools (Chrome 99). (Feb. 2022). https:
//developer.chrome.com/en/blog/new-in-devtools-99/.
[60]
A. Alomar, P. Hamadanian, A. Nasr-Esfahany, A. Agarwal, M. Alizadeh, and
D. Shah. 2023. CausalSim: A Causal Framework for Unbiased Trace-Driven
Simulation. In 1115–1147. isbn: 9781939133335. https://www.usenix.org/confe
rence/nsdi23/presentation/alomar.
[61]
Chandan Bothra, Jianfei Gao, Sanjay Rao, and Bruno Ribeiro. 2023. Veritas:
Answering Causal Queries from Video Streaming Traces. In Proceedings of the
ACM SIGCOMM 2023 Conference (ACM SIGCOMM ’23). New York, NY, USA,
738–753. doi: 10.1145/3603269.3604828.
[62]
Nicolas Christianson, Junxuan Shen, and Adam Wierman. 2023. Optimal Robustness-
Consistency Tradeoffs for Learning-Augmented Metrical Task Systems. In
Proceedings of The 26th International Conference on Artificial Intelligence and
Statistics. PMLR, (Apr. 2023), 9377–9399.
[63]
MDN contributors. 2023. WebDriver. (June 2023). https://developer.mozilla.org
/en-US/docs/Web/WebDriver.
[64]
DASH Industry Forum. 2023. dash.js: A Reference Client Implementation for
the Playback of MPEG DASH via JavaScript and Compliant Browsers. https:
//github.com/Dash-Industry-Forum/dash.js.
[65]
YouTube. 2023. YouTube Recommended Upload Encoding Settings. https://sup
port.google.com/youtube/answer/1722171.
[66]
Akamai. [n. d.] Stream Analyzer Service Description. https://groups.cs.umass
.edu/ramesh/wp-content/uploads/sites/3/2023/10/Stream_Analyzer_Service
_Description.pdf. ().
626
```


### Pagina 15
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Appendices are supporting material that has not been peer-reviewed.
A
PROOF OUTLINE
In this section, we present an outline of our theoretical analysis for SODA. As we discussed in Section 4, our proof is based on an exponentially
decaying perturbation bound that relates the behavior of the solution to the optimization problem defining SODA as a function of problem
parameters. This section is organized as follows: We first introduce the modeling of SODA that we use to establish theoretical results in
Section A.1. Then, we introduce the exponentially decaying perturbation bound, its implications, and the proof idea in Section A.2. Next, we
present the outlines for proving SODA’s performance guarantees with the help of exponentially decaying perturbation bounds in Sections A.3
and A.4. Finally, we will discuss some sufficient conditions under which the optimal bitrate sequence can be approximated by a monotonic
sequence in Section A.5.
A.1
Theoretical Problem Setting
We first introduce the notation used to define the performance metrics and the variant of SODA studied in our theoretical analysis. To make
the formulation of the video streaming problem closer to a classic control problem, we define the “control action” 𝑢𝑡as the inverse of the
bitrate (i.e., 𝑢𝑡= 1
𝑟𝑡). Recall that we set 𝑣(𝑟) = 1
𝑟in our theoretical analysis. Thus, we can write down a general form of the optimization
problem solved by SODA and use 𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 𝐹 to denote its optimal solution:
arg min
𝑥𝑡:𝑡+𝑝,𝑢𝑡+1:𝑡+𝑝
𝑡+𝑝
∑︁
𝜏=𝑡
ˆ𝜔𝜏𝑢2
𝜏+ 𝛽
𝑡+𝑝
∑︁
𝜏=𝑡
𝑏(𝑥𝜏) + 𝛾
𝑡+𝑝+1
∑︁
𝜏=𝑡
|𝑢𝜏−𝑢𝜏−1|2 + 𝐹(𝑥𝑡+𝑝,𝑢𝑡+𝑝+1)
(3a)
s.t. 𝑥𝜏= 𝑥𝜏−1 + ˆ𝜔𝜏𝑢𝜏−1, for 𝜏= 𝑡, . . . ,𝑡+ 𝑝,
(3b)
0 ≤𝑥𝜏≤𝑥max,
1
𝑟max
≤𝑢𝜏≤
1
𝑟min
, for 𝜏= 𝑡, . . . ,𝑡+ 𝑝,
(3c)
𝑥𝑡−1 = 𝜎𝑡−1,𝑢𝑡−1 = 𝜈𝑡−1.
(3d)
Here,𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 𝐹 is defined to be a vector that contains the states 𝑥𝑡:𝑡+𝑝and control actions 𝑢𝑡+1:𝑡+𝑝in the optimal solution.
The initial condition (𝜎𝑡−1,𝜈𝑡−1), bandwidth sequence ˆ𝜔𝑡:𝑡+𝑝, and terminal cost function 𝐹are the parameters of the optimization problem.
For the terminal costs, we consider two types of functions: (1) The zero function 𝐹= 0, i.e., 𝐹(𝑥,𝑢) = 0 for all 𝑥,𝑢; (2) The indicator function
𝐹= I𝜎,𝜈, which is defined as
𝐹(𝑥,𝑢) = I𝜎,𝜈(𝑥,𝑢) =
(
0
if 𝑥= 𝜎,𝑢= 𝜈,
+∞
otherwise.
The first type of terminal cost will be used to define the performance metrics (competitive ratio and dynamic regret), and the sec-
ond type will be used in the algorithm design. Since we will use the indicator terminal cost frequently, we introduce the shorthand
˜𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1), which denotes ˜𝜓𝑡+𝑝
𝑡

(𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; I𝜎𝑡+𝑝,𝜈𝑡+𝑝+1

. We use 𝜄𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 𝐹 to de-
note the optimal objective value of the optimization problem (3).
The model of SODA that we consider in the theoretical analysis is summarized in Algorithm 2. The major difference from the SODA
algorithm discussed in Section 3.3 is that we include the indicator terminal cost (in line 5) so that the last two states in the predictive
trajectory are equal to the target buffer level. This terminal constraint is important for our competitive ratio result in Theorem 4.1, for which
we need to bound the squared distance between the trajectories of SODA and the offline optimal controller by a part of the offline optimal cost.
Algorithm 2: SODA (for theoretical analysis)
Require: Prediction horizon 𝐾.
1: for 𝑡= 1, 2, . . . , 𝑁do
2:
Set 𝑡′ = min{𝑡+ 𝐾−1, 𝑁}.
3:
Receive predictions ˆ𝜔𝑡+1:𝑡′|𝑡.
4:
if 𝑡′ < 𝑁then
5:
Set terminal cost 𝐹𝑡′ = I𝑥∗,1/ ˆ𝜔𝑡′|𝑡.
6:
else
7:
Set terminal cost 𝐹𝑡′ = 0.
8:
end if
9:
Commit 𝑢𝑡= 𝜓𝑡′−1
𝑡

(𝑥𝑡−1,𝑢𝑡−1); ˆ𝜔𝑡:𝑡′|𝑡; 𝐹𝑡′

.
10: end for
627
```


### Pagina 16
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Using the notations above, we can formally define the performance metrics we employ: Let cost(OPT) denote the offline optimal cost one
can achieve when exact predictions of all future bandwidth are available at the start of the problem, i.e., cost(OPT) = 𝜄𝑁
1

(𝑥0,𝑢0);𝜔∗
1:𝑁; 0

.
Then,
• Dynamic regret is an upper bound on the difference cost(SODA) −cost(OPT);
• Competitive ratio is an upper bound on the ratio cost(SODA)/cost(OPT).
A.2
Exponentially Decaying Perturbations
Exponentially decaying perturbations is a critical property of the finite-time optimal control problem that our analysis builds upon. We
define this property formally in Definition A.1.
Definition A.1 (Exponentially Decaying Perturbation Bound). We say the exponentially decaying perturbation bound holds if there exists
uniform constants 𝐶> 0, 𝜌∈(0, 1) such that the following inequalities hold:
𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 0
𝑥𝜏−𝜓𝑡+𝑝
𝑡

(𝜎′
𝑡−1,𝜈′
𝑡−1); ˆ𝜔′
𝑡:𝑡+𝑝; 0

𝑥𝜏

≤𝐶𝜌𝜏−𝑡+1  𝜎𝑡−1 −𝜎′
𝑡−1
 +
𝜈𝑡−1 −𝜈′
𝑡−1
 + 𝐶
𝑡+𝑝
∑︁
𝑗=𝑡
𝜌|𝜏−𝑗|  ˆ𝜔𝑗−ˆ𝜔′
𝑗
,
(4)
 ˜𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1)
𝑥𝜏−𝜓𝑡+𝑝
𝑡

(𝜎′
𝑡−1,𝜈′
𝑡−1); ˆ𝜔′
𝑡:𝑡+𝑝; (𝜎′
𝑡+𝑝,𝜈′
𝑡+𝑝+1)

𝑥𝜏

≤𝐶𝜌𝜏−𝑡+1  𝜎𝑡−1 −𝜎′
𝑡−1
 +
𝜈𝑡−1 −𝜈′
𝑡−1
 + 𝐶
𝑡+𝑝
∑︁
𝑗=𝑡
𝜌|𝜏−𝑗|  ˆ𝜔𝑗−ˆ𝜔′
𝑗
 + 𝐶𝜌𝑡+𝑝−𝜏𝜎𝑡+𝑝−𝜎′
𝑡+𝑝
 +
𝜈𝑡+𝑝+1 −𝜈′
𝑡+𝑝+1


.
(5)
Intuitively, the exponential decay property (Definition A.1) holds if the impact of a perturbation on the initial condition (𝜎𝑡−1,𝜈𝑡−1),
prediction ˆ𝜔𝑗, or terminal constraint (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1) on the component 𝑥𝜏in the optimal trajectory decays exponentially with respect to the
absolute difference between their corresponding time indices.
Due to its importance for the theoretical analysis of MPC-based algorithms, many previous works have established exponentially decaying
perturbation bounds for various cases of online optimization with switching costs [49], optimal control with unconstrained dynamics [49,
56], and online optimization in networked systems [55]. In contrast to previous work, however, the video streaming problem (3) that we
consider is a constrained optimal control problem. To this point, there has been limited success in establishing exponentially decaying
perturbation bounds for general constrained optimal control problems, and existing results that provide sufficient conditions for their validity
are difficult to verify [51, 56].
In this work, we leverage the special structure of the video streaming problem to show the exponentially decaying perturbation bound
holds in this setting. We require the following assumption about the buffer constraints, bandwidth, and the bitrate range.
Assumption A.1. There exists uniform constants 𝜔max > 𝜔min > 0 such that for any time step 𝑡, we have that 𝜔min ≤𝜔𝑡≤𝜔max holds. We
also assume that 𝜔min/𝑟min ≥𝑥max, and 𝜔max/𝑟max −1 ≤−𝛿holds for a fixed constant 𝛿> 0.
Intuitively, Assumption A.1 guarantees that the controller can always fill up the buffer at the cost of choosing the smallest bitrate or
decrease the buffer level by choosing the largest bitrate. As we discussed in Section 4, this assumption is used to eliminate extreme boundary
cases in the analysis, but SODA empirically performs well even when Assumption A.1 is not strictly satisfied. Using this assumption, we show
the exponentially decaying perturbation property holds for the video streaming problem in Theorem A.1.
Theorem A.1. Under Assumption A.1, the exponentially decaying perturbation bound holds with constants
𝜌=
©­­­­
«
1 −
2
1 +
√︂
1 + max{6𝜔min(𝜔min+3),4𝑥max(𝜔min+8𝛾)}
𝜔3
min𝜖𝛽
ª®®®®
¬
1
3(3+⌈𝑥max/𝛿⌉)
and
𝐶=
(1 + 𝜔max)

3𝛽𝜔3
min + max{6𝜔min(𝜔min + 3), 4𝑥max(𝜔min + 8𝛾)}

𝜔3
min𝜌3+⌈𝑥max/𝛿⌉
.
While the exponentially decaying property (Definition A.1) bounds the impact of parameter perturbations on the states, we extend the
definition to the control actions and show that this variant holds as a corollary of Theorem A.1.
628
```


### Pagina 17
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
(𝑥0,𝑢0)
(𝑥∗
1,𝑢∗
1)
(𝑥∗
2,𝑢∗
2)
(𝑥∗
3,𝑢∗
3)
(𝑥∗
4,𝑢∗
4)
(𝑥1,𝑢1)
(𝑥2,𝑢2)
(𝑥3,𝑢3)
Figure 14: Illustration of the aggregations of per-step errors. In the figure, {(𝑥∗
𝑡,𝑢∗
𝑡)}𝑡=1,2,... denotes the offline optimal states
and control actions, and {(𝑥𝑡,𝑢𝑡)}𝑡=1,2,... denotes the buffer level achieved by SODA. The dashed trajectory from (𝑥𝑡,𝑢𝑡) denotes
the clairvoyant optimal trajectory from (𝑥𝑡,𝑢𝑡). At time 𝑡, the per-step error 𝑒𝑡leads to the deviation of the actual trajectory of
SODA with the clairvoyant optimal trajectory. The impact of the per-step error 𝑒1 at a future time step 𝑡is the height of blue
area, which decays exponentially fast with respect to 𝑡when exponentially decaying perturbation holds. Therefore, although a
per-step error occurs at every time step, the distance between (𝑥𝑡,𝑢𝑡) and (𝑥∗
𝑡,𝑢∗
𝑡) is still uniformly bounded.
Corollary A.2. Under Assumption A.1, for the control action 𝑢, we also have that
𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; 0
𝑢𝜏−𝜓𝑡+𝑝
𝑡

(𝜎′
𝑡−1,𝜈′
𝑡−1); ˆ𝜔′
𝑡:𝑡+𝑝; 0

𝑢𝜏

≤𝐶′𝜌𝜏−𝑡+1  𝜎𝑡−1 −𝜎′
𝑡−1
 +
𝜈𝑡−1 −𝜈′
𝑡−1
 + 𝐶′
𝑡+𝑝
∑︁
𝑗=𝑡
𝜌|𝜏−𝑗|  ˆ𝜔𝑗−ˆ𝜔′
𝑗
,
 ˜𝜓𝑡+𝑝
𝑡
 (𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔𝑡:𝑡+𝑝; (𝜎𝑡+𝑝,𝜈𝑡+𝑝+1)
𝑢𝜏−𝜓𝑡+𝑝
𝑡

(𝜎′
𝑡−1,𝜈′
𝑡−1); ˆ𝜔′
𝑡:𝑡+𝑝; (𝜎′
𝑡+𝑝,𝜈′
𝑡+𝑝+1)

𝑢𝜏

≤𝐶′𝜌𝜏−𝑡+1  𝜎𝑡−1 −𝜎′
𝑡−1
 +
𝜈𝑡−1 −𝜈′
𝑡−1
 + 𝐶′
𝑡+𝑝
∑︁
𝑗=𝑡
𝜌|𝜏−𝑗|  ˆ𝜔𝑗−ˆ𝜔′
𝑗
 + 𝐶′𝜌𝑡+𝑝−𝜏𝜎𝑡+𝑝−𝜎′
𝑡+𝑝
 +
𝜈𝑡+𝑝+1 −𝜈′
𝑡+𝑝+1


,
where the decay factor 𝜌is the same as Theorem A.1, and the constant 𝐶′ is given by
𝐶′ = 𝐶(1 + 𝜌)𝑟min + 𝜌
𝜔min𝑟min𝜌
.
Here, 𝐶is the same as Theorem A.1.
To establish the exponentially decaying perturbation property, we first reduce the video streaming problem to a more general online
optimization problem with memory and inequality constraints. Then, we consider each possible combination of active inequality constraints
separately and show that the exponentially decaying perturbation property holds in each case. This only requires considering optimization
problems with equality constraints with second-order differentiable objectives. Lastly, we show that the exponential decay properties for
these separate cases can be combined to establish the exponential decay property for the original video streaming problem.
A.3
Proof Outline for Exact Predictions
We provide the formal version of Theorem 4.1 that gives the dynamic regret and competitive ratio for SODA with specific coefficients in
Theorem A.3.
Theorem A.3. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Define the weight 𝐶
and the decay factor 𝜌to be the same as Theorem A.1, and the coefficient 𝐶′ is given by Corollary A.2. Suppose all predictions are exact (i.e.,
ˆ𝜔𝑚|𝑛−1 = 𝜔𝑚for 𝑚= 𝑛, . . . ,𝑛+ 𝐾−1) and the prediction horizon 𝐾satisfies
𝐾≥1
4 ln
 16
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌

·

𝐶2 + (𝐶′)22
/ln
 1
𝜌

= 𝑂(1).
Here, the coefficients 𝐶,𝐶′ and the decay factor 𝜌are given by Theorem A.1 and Corollary A.2. Then, SODA achieves a dynamic regret of
𝐶1𝜌𝐾−1cost(OPT) = 𝑂(𝜌𝐾𝑁) and a competitive ratio of 1 + 𝐶1𝜌𝐾−1 = 1 + 𝑂(𝜌𝐾). Here, the coefficient 𝐶1 is given by
𝐶1 = 8

2(4𝛾+ 𝛽+ 𝜔max) ·
1
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌
 
𝐶2 + (𝐶′)2
·
4 + 𝜔2
min
𝜖𝛽𝜔2
min
!1/2
.
and the notation 𝑂(·) hides polynomial dependence on system parameters 𝜖, 𝛽,𝛾and 𝑑.
629
```


### Pagina 18
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
The proof outline of Theorem A.3 contains two parts: (1) Bounding the per-step error of SODA at each time step when compared against
the hindsight optimal policy; (2) Showing that the past per-step does not accumulate to be unbounded over time.
Bounding the Per-step error. We introduce the concept of per-step error to characterize the decision error of SODA at each time step due
to its limited prediction power. While the prediction power of SODA is limited because it only has exact predictions of future bandwidths
within a finite horizon 𝐾, the idea of per-step error also extends to inexact predictions (Section A.4). We provide the formal definition of the
per-step error in Definition A.2.
Definition A.2. The per-step error of SODA at time step 𝑡(denoted as 𝑒𝑡) is defined as the sum of the difference between the actual state/action
pair of SODA (𝑥𝑡,𝑢𝑡) and the clairvoyant optimal next state from (𝑥𝑡−1,𝑢𝑡−1), i.e.,
𝑒𝑡B
𝑥𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡
 +
𝑢𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝑡

Intuitively, starting from the state/action pair (𝑥𝑡−1,𝑢𝑡−1), we compare the actual next state/action pair (𝑥𝑡,𝑢𝑡) of SODA with the clairvoyant
optimal next state/action a controller would take if it had the exact predictions of all future bandwidths after time step 𝑡. We define the
magnitude of this difference as the per-step error of SODA.
When the predictions of future bandwidths are exact, we leverage the exponentially decaying perturbation property to bound the per-step
error of SODA in Lemma A.4. We defer the proof of Lemma A.4 to Section C.1.
Lemma A.4. When the predictions for the future bandwidth are exact, the per-step error of SODA satisfies
𝑒2
𝑡≤16𝜌4𝐾−2 
𝐶2 + (𝐶′)22 𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+ 8𝜌2𝐾−2 
𝐶2 + (𝐶′)2 (2 + 𝜔2
min)𝑏(𝑥∗
𝑡+𝐾−1) + 2𝑏(𝑥∗
𝑡+𝐾−2)
𝜖𝜔2
min
.
The exponentially decaying coefficients 𝜌4𝐾−2 and 𝜌2𝐾−2 suggest that the per-step error improves exponentially fast as the prediction
horizon 𝐾grows. Although one can simplify the expression by bounding the terms
𝑥𝑡−1 −𝑥∗
𝑡−1
2,
𝑢𝑡−1 −𝑢∗
𝑡−1
2, 𝑏(𝑥∗
𝑡+𝐾−1), and 𝑏(𝑥∗
𝑡+𝐾−2)
with some uniform constants, we keep these terms because the careful treatment is required to show the competitive ratio result.
Bounding the accumulation of past errors. Besides bounding the per-step errors, another important consequence of the exponentially
decaying perturbation bounds is that it guarantees the impact of a previous per-step error decays quickly over time. Therefore, when we
bound the total difference between SODA’s trajectory {(𝑥𝑡,𝑢𝑡)}𝑁
𝑡=1 and the offline optimal trajectory {(𝑥∗
𝑡,𝑢∗
𝑡)}𝑁
𝑡=1, the aggregated contribution
of any per-step error term 𝑒𝜏is up to a constant factor that depends on the decay factor rather than growing linearly with respect to the
total horizon length 𝑁(see Figure 14 for an illustration). We state this result formally in Lemma A.5 and defer its proof to Section C.2.
Lemma A.5. The trajectory of SODA {(𝑥𝑡,𝑢𝑡)}𝑁
𝑡=1 satisfies that
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
≤
1
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌
 𝑁
∑︁
𝑡=1
𝑒2
𝑡,
where {(𝑥∗
𝑡,𝑢∗
𝑡)}𝑁
𝑡=1 denotes the offline optimal trajectory.
By combining Lemma A.4 and Lemma A.5, we bound the total squared distance between SODA’s trajectory and the offline optimal
trajectory by a part of the offline optimal cost times a coefficient of the order 𝑂(𝜌2𝐾). Since the cost functions for adaptive video streaming
are well-conditioned, we can convert the bound on the total squared distance between the two trajectories into the competitive ratio bound
and the dynamic regret bound to finish the proof of Theorem A.3.
A.4
Proof Outline for Inexact Predictions
Compared with the case when all predictions are exact, a major challenge when the predictions are inexact is that one of SODA’s decisions
may cause the next state to violate the state constraint. In this section, we show in two steps that SODA’s decision trajectory will not violate
the state constraints. First, by increasing the coefficient 𝛽of the buffer cost, one can guarantee that the offline optimal trajectory stays
arbitrarily close to the offline optimal trajectory (see Lemma A.6). Then, we show a bound on the per-step error (Definition A.2) which
depends on the prediction error (see Lemma A.7). Recall that the exponentially decaying perturbation bounds allow us to bound the distance
between the SODA and the offline optimal trajectories. Therefore, we can combine these results to show that under some mild assumptions
on the coefficient 𝛽and the prediction errors, SODA will not violate any constraints, and moreover, it also satisfies a dynamic regret bound
(see Theorem A.8).
We first show that for any 𝜁> 0, one can select the coefficient 𝛽to be sufficiently large so that the offline optimal trajectory stays within
a margin of 𝜁around the target buffer level ¯𝑥. We state this result formally in Lemma A.6 and defer its proof to Section D.1.
Lemma A.6. Suppose 𝜁≤min{¯𝑥,𝑥max −¯𝑥} is positive number and 𝑥0 ≤¯𝑥+ 𝜁, if the coefficient 𝛽for the buffer cost is sufficiently large such
that
𝛽≥1
𝜖𝜁·

1 +
4𝛾
𝜔min

·
 1
𝑟min
−
1
𝑟max

.
Then, the offline optimal trajectory satisfies 𝑥∗
𝑡∈[¯𝑥−𝜁, ¯𝑥+ 𝜁] holds for all time step 𝑡.
630
```


### Pagina 19
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Intuitively, Lemma A.6 holds because increasing 𝛽makes staying close to the target buffer level more important. In the extreme case that
𝛽tends to +∞, the offline optimal will ignore the distortion/switching cost and select actions so that the buffer level always equal to ¯𝑥.
Recall that the per-step error of SODA is defined in Definition A.2. We bound the per-step error in Lemma A.7 and defer its proof to
Section D.2.
Lemma A.7. When the predictions for the future bandwidth are inexact, the per-step error of SODA satisfies
𝑒𝑡≤(𝐶+ 𝐶′)𝜌𝐾

𝑥max +
1
𝑟min
−
1
𝑟max

+ (𝐶+ 𝐶′) · 𝐸(𝑡−1, 𝐾) +
𝜔𝑡−ˆ𝜔𝑡|𝑡−1

𝑟min
,
where 𝐸(𝑡−1, 𝐾) B Í𝑡+𝐾−1
𝜏=𝑡
𝜌𝜏−𝑡 ˆ𝜔𝜏|𝑡−1 −𝜔𝜏
.
Similar to the proof outline for the exact prediction case in Section A.3, we can apply Lemma A.5 to bound the accumulation of past errors.
With the help of Lemma A.6 and Lemma A.7, we show our main result for SODA when the predictions of the future bandwidths are inexact
in Theorem A.8. We defer the proof of Theorem A.8 to Section D.3.
Theorem A.8. Under Assumption A.1, consider SODA with the terminal constraints 𝑥𝑡+𝐾−1 = ¯𝑥,𝑟𝑡+𝐾−1 = ˆ𝜔𝑡+𝐾−1|𝑡−1. Let 𝐷B min{¯𝑥,𝑥max−
¯𝑥}. Suppose the weight 𝛽, the prediction horizon 𝐾, and the prediction errors satisfy that
𝛽≥
3
𝜖𝐷·

1 +
4𝛾
𝜔min

·
 1
𝑟min
−
1
𝑟max

, and
𝐸(𝑡, 𝐾) + 𝜌𝐾≤
(1 −𝜌)𝐷
3𝐶(1 + 𝐶+ 𝐶′)

1 + 𝑥max +
1
𝑟min −
1
𝑟max
 ,
where, recall, 𝐸(𝑡, 𝐾) = Í𝑡+𝐾
𝜏=𝑡+1 𝜌𝜏−𝑡−1  ˆ𝜔𝜏|𝑡−𝜔𝜏
 . Then, the buffer levels in the SODA’s decision trajectory never hits the constraint boundary,
i.e., 0 < 𝑥𝑡< 𝑥max for 𝑡= 1, . . . , 𝑁. Further, SODA achieves a dynamic regret of
2

1 +
1
𝑟min + 𝐶+ 𝐶′2 
1 + 𝑥max +
1
𝑟min −
1
𝑟max

(1 −𝜌)3/2
·
√︁
4𝛾+ 𝛽+ 𝜔max ·
√︁
E · cost(OPT)+

1 +
1
𝑟min + 𝐶+ 𝐶′4 
1 + 𝑥max +
1
𝑟min −
1
𝑟max
2
(4𝛾+ 𝛽+ 𝜔max)
(1 −𝜌)3
· E,
where E = 𝜌2𝐾𝑁+ Í𝐾
𝜅=1 𝜌𝜅𝐸𝜅. Here 𝐸𝜅B Í𝑁
𝑡=1
 ˆ𝜔𝑡+𝜅|𝑡−𝜔𝑡+𝜅
2.
Note that the dynamic regret bound shown in Theorem A.8 is in the order of 𝑂(
√
E𝑁+ E), since cost(OPT) = 𝑂(𝑁). Intuitively, from the
form of 𝐸𝑡(𝐾), we see that predicting the future bandwidth 𝜔𝜏accurately at time step 𝑡becomes less important as (𝜏−𝑡) increases.
A.5
Proof Outline for Efficient Structure
In this section, we show that optimal solution of the finite-time optimal control problem solved by SODA can be approximated well by a
monotonic sequence of bitrates when the coefficient 𝛾of the switching cost is sufficiently large (see Theorem A.9). Although this result is
shown for the continuous variable case, it also provides some insight as to why the efficient approximate solver in Algorithm 1 can provide
identical decisions to the brute-force solver with relatively high probabilities, as shown in Figure 8.
Theorem A.9. Let ˆ𝜔×𝐾denote the sequence { ˆ𝜔, . . . , ˆ𝜔} with length 𝐾. For any 𝜆> 0, when the coefficient 𝛾is sufficiently large such that
𝛾≥𝐾2
𝜆2

ˆ𝜔

1
𝑟2
min
−
1
𝑟2max
!
+ 𝛽max{¯𝑥2,𝜖(𝑥max −¯𝑥)2}
!
,
we have that the following inequality holds for all 𝜏∈{𝑡,𝑡+ 1, . . . ,𝑡+ 𝐾−1}:
 ˆ𝜓𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔×𝐾; 0)𝑢𝜏−ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0)𝑢𝜏
 ≤𝜆.
Note that ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0)𝑢𝜏is monotonic by Lemma A.10.
We defer the formal proof of Theorem A.9 to Section E.2. The theoretical insight provided by Theorem A.9 aligns with our empirical result
in Figure 8. Specifically, if we increase the coefficient 𝛾while keeping the prediction horizon 𝐾fixed, the decision made by the efficient
monotonic approximation approach (Algorithm 1) is more likely to be identical with the brute-force solver. On the other hand, if we increase
𝐾and fix 𝛾, it is more challenging for Algorithm 1 to match the decision of the brute-force solver.
To show Theorem A.9, we first consider a setting where the objective function only contains the switching cost terms (i.e., the distortion
cost and the buffer cost are removed.) This can be viewed as the extreme case when 𝛾tends to +∞so that both 𝛼and 𝛽are negligible. In this
scenario, we show the optimal sequence of the inverse bitrates is monotonic. We state this result formally in Lemma A.10 and defer its proof
to Section E.1.
631
```


### Pagina 20
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Lemma A.10. Under the same assumption as Theorem A.9, consider the optimal solution to the optimization problem
ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0) B arg min
𝑢𝑡:𝑡+𝐾−1
𝑡+𝐾−1
∑︁
𝜏=𝑡
𝛾· (𝑢𝑡−𝑢𝑡−1)2
s.t. 𝑥𝜏= 𝑥𝜏−1 + ˆ𝜔𝑢𝜏−1, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑥𝜏∈[0,𝑥max],𝑢𝜏∈

1
𝑟max
,
1
𝑟min

, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑥𝑡−1 = 𝜎𝑡−1,𝑢𝑡−1 = 𝜈𝑡−1.
(6)
The solution satisfies that: If 𝜈𝑡−1 > 1/ ˆ𝜔, then the sequence 𝜈𝑡−1, ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0) is monotonically decreasing; If 𝜈𝑡−1 < 1/ ˆ𝜔, then
the sequence 𝜈𝑡−1, ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0) is monotonically increasing; If 𝜈𝑡−1 = 1/ ˆ𝜔, the optimal solution is 𝑢𝑡= 𝑢𝑡+1 = · · · = 𝑢𝑡+𝐾−1 =
𝜈𝑡−1 = 1/ ˆ𝜔.
The key observation that allows us to generalize Lemma A.10 to the case where the distortion/buffer costs are non-negligible is the
following: If we change the variable of (6) to 𝑎𝑡= 𝑢𝑡−𝑢𝑡−1, which denotes the increments of the control actions, the objective of (6) is a
𝛾-strongly convex function of (𝑎𝑡, . . . ,𝑎𝑡+𝐾−1). Any deviation from the optimal solution of (6) will cause a loss on the total switching costs
that grows with 𝛾. When 𝛾is sufficiently large, a feasible solution cannot use its gain on the distortion/buffer costs to cancel the loss on the
total switching cost if it deviates too much from the optimal solution of (6).
B
PROOFS OF THE EXPONENTIALLY DECAYING PERTURBATION BOUNDS
In this section, we establish the critical exponentially decaying perturbation bounds (Definition A.1). Instead of just focusing on the video
streaming application itself, we establish the perturbation bound for a more general SOCO with memory framework.
Specifically, we consider the following finite-time optimal control problem with memory 𝐻.
𝜓(𝑦,𝑧; 𝜇,𝑤,𝛿) =
arg min
𝑥−𝐻+1:𝑝+𝐻−1
𝑝
∑︁
𝑡=0
𝑓𝑡(𝑥𝑡; 𝜇𝑡) +
𝑝+𝐻−1
∑︁
𝑡=0
𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)
(7a)
s.t. 𝑥𝑡∈[0,𝑥max] ⊆R, ∀0 ≤𝑡≤𝑝,
(7b)
𝑥𝑡−𝑥𝑡−1 ≥−𝛿𝑡, ∀0 ≤𝑡≤𝑝+ 1,
(7c)
𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧,
(7d)
where 𝑦,𝑧∈[0,𝑥max]𝐻−1, 𝜇∈[0,𝑥max]𝑝+1,𝑤∈W𝑝+𝐻,𝛿∈Δ𝑝+2. Here, the objective function (7a) contains the hitting costs 𝑓𝑡(𝑥𝑡; 𝜇𝑡)
(parameterized by 𝜇𝑡) and the switching costs 𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡) (parameterized by 𝑤𝑡). For the constraints, (7b) imposes a box constraint
on each decision variable 𝑥𝑡; (7c) imposes a constraint on how much 𝑥𝑡can decrease at each time step; and (7d) specifies the boundary
conditions of the optimization problem.
In the special case of video streaming, the decision is on the buffer level 𝑥𝑡. Given the buffer levels, the inverse of the bitrate 𝑢𝑡B 1/𝑟𝑡is
uniquely decided by the equation
𝑢𝑡= (𝑥𝑡−𝑥𝑡−1 + 1)/𝜔𝑡,
where 𝜔𝑡denotes the bandwidth. The memory length 𝐻= 3. For the hitting cost, we have 𝜇𝑡≡¯𝑥, and
𝑓𝑡(𝑥; 𝜇𝑡) = 𝛽𝑏(𝑥) =
(
𝛽(𝑥−¯𝑥)2,
if 𝑥≤¯𝑥,
𝜖𝛽(𝑥−¯𝑥)2,
otherwise.
For the switching cost, we have 𝑤𝑡= (𝜔𝑡,𝜔𝑡−1) and
𝑐𝑡(𝑥𝑡:𝑡−2;𝑤𝑡) = 𝜔𝑡𝑢2
𝑡+ 𝛾(𝑢𝑡−𝑢𝑡−1)2
= (𝑥𝑡−𝑥𝑡−1 + 1)2
𝜔𝑡
+ 𝛾(𝜔𝑡−1𝑥𝑡+ 𝜔𝑡𝑥𝑡−2 −(𝜔𝑡+ 𝜔𝑡−1)𝑥𝑡−1 + (𝜔𝑡−1 −𝜔𝑡))2
𝜔2
𝑡𝜔2
𝑡−1
.
The first constraint 𝑥𝑡∈[0,𝑥max] of (7) matches the buffer constraint of the video streaming problem exactly.
The second constraint 𝑥𝑡−𝑥𝑡−1 ≥−𝛿𝑡corresponds to the constraint that 𝑢𝑡≥
1
𝑟max in (3). Thus, when applying (7) to video streaming,
we have 𝛿𝑡= 1 −𝜔𝑡
𝑟max . By Assumption A.1, we have 𝛿𝑡≥𝛿> 0.
Given the relationship between SOCO with memory problem and adaptive video streaming problem, we only need to establish the
exponentially decaying perturbation bound for the more general SOCO with memory problem. To show this perturbation bound, we need
the following assumption about the objective function and constraints:
Assumption B.1. We need the following assumption on the optimization problem (7) for the exponentially decaying perturbation property to
hold:
632
```


### Pagina 21
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
1) 𝑓𝑡(·; 𝜇𝑡) : R →R is strongly convex for all𝑡and 𝜇𝑡∈[0,𝑥max]. We further assume there exists two𝑚𝑓-strongly convex and ℓ𝑓-smooth functions
𝑓(0)
𝑡
(·; 𝜇𝑡), 𝑓(1)
𝑡
(·; 𝜇𝑡) : R →R in C2 such that 𝑓𝑡(𝑥𝑡; 𝜇𝑡) = 𝑓(0)
𝑡
(𝑥𝑡; 𝜇𝑡) for 𝑥𝑡∈[0, 𝜇𝑡] and 𝑓𝑡(𝑥𝑡) = 𝑓(1)
𝑡
(𝑥𝑡; 𝜇𝑡) for 𝑥𝑡∈[𝜇𝑡,𝑥max]. We
also assume that for 𝑗= 1, 2, 𝑓(𝑗)
𝑡
satisfies that for all 𝑥𝑡, 𝜇𝑡∈[0,𝑥max],



∇𝑥𝑡𝑓(𝑗)
𝑡
(𝑥𝑡; 𝜇𝑡)



 +



∇𝜇𝑡𝑓(𝑗)
𝑡
(𝑥𝑡; 𝜇𝑡)



 ≤𝐿𝑓, and



∇𝜇𝑡∇𝑥𝑡𝑓(𝑗)
𝑡
(𝑥𝑡; 𝜇𝑡)



 ≤ℓ𝜇.
2) 𝑐𝑡(·;𝑤𝑡) : R𝐻→R is convex and ℓ𝑐-smooth for all 𝑡and 𝑤𝑡∈W ⊂R𝑞. 𝑐𝑡(·;𝑤𝑡) is in C2 on [0,𝑥max]𝐻. We also assume that for all
𝑤𝑡∈W and feasible 𝑥𝑡:𝑡−𝐻+1, we have


∇𝑥𝑡:𝑡−𝐻+1𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)


 +


∇𝑤𝑡𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)


 ≤𝐿𝑐, and


∇𝑤𝑡∇𝑥𝑡:𝑡−𝐻+1𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)


 ≤ℓ𝑤.
3) We have 𝛿𝑡∈Δ holds for all 𝑡, where Δ is a closed interval on R and is bounded below by some positive constant 𝛿. Denote 𝑑B ⌈𝑥max/𝛿⌉.
In the special case of the video streaming problem, Assumption B.1 is satisfied with the parameters 𝑚𝑓= 𝜖𝛽, ℓ𝑓= ℓ𝜇= 𝛽, ℓ𝑐= 2(𝜔min+3)
𝜔2
min
,
ℓ𝑤= 4𝑥max(𝜔min+8𝛾)
𝜔3
min
. In addition, both 𝐿𝑓and 𝐿𝑐are bounded.
We state the exponentially decaying perturbation bound for the SOCO with memory problem formally in Theorem B.1 and defer its proof
to Appendix B.1.
Theorem B.1. Under Assumption B.1, if 𝑝≥𝑑, the inequality


𝜓(𝑦,𝑧; 𝜇,𝑤,𝛿)𝑡−𝜓(𝑦′,𝑧′; 𝜇′,𝑤′,𝛿′)𝑡


≤𝐶 𝜌𝑡

𝑦−𝑦′

 + 𝜌𝑝−𝑡

𝑧−𝑧′

 + 𝐶©­
«
𝑝
∑︁
𝜏=0
𝜌|𝑡−𝜏| 𝜇𝜏−𝜇′
𝜏
 +
𝑝+𝐻−1
∑︁
𝜏=0
𝜌|𝑡−𝜏|

𝑤𝜏−𝑤′
𝜏


 +
𝑝+1
∑︁
𝜏=0
𝜌|𝑡−𝜏|

𝛿𝜏−𝛿′
𝜏


ª®
¬
(8)
holds for all 𝑡∈[0, 𝑝] and 𝑦,𝑧∈[𝑥,𝑥]𝐻−1. Here,
𝜌=
©­­
«
1 −
2
1 +
√︃
1 + (ℓ/𝑚𝑓)
ª®®
¬
1
𝐻(𝐻+𝑑)
,𝐶=
2ℓ
𝑚𝑓𝜌(𝐻−2) (𝐻+𝑑) ,
where ℓB max{𝐻ℓ𝑐, ℓ𝑤} and ¯ℓB max{𝐻ℓ𝑓, ℓ𝜇, ℓ}.
In the special case of the video streaming, we see that
ℓ= max{3ℓ𝑐, ℓ𝑤} = max{6𝜔min(𝜔min + 3), 4𝑥max(𝜔min + 8𝛾)}
𝜔3
min
.
Therefore, we have
𝜌=
©­­­­
«
1 −
2
1 +
√︂
1 + max{6𝜔min(𝜔min+3),4𝑥max(𝜔min+8𝛾)}
𝜔3
min𝜖𝛽
ª®®®®
¬
1
3(3+⌈𝑥max/𝛿⌉)
.
The coefficient 𝐶is bounded by
𝐶≤
3𝛽𝜔3
min + max{6𝜔min(𝜔min + 3), 4𝑥max(𝜔min + 8𝛾)}
𝜔3
min𝜌3+⌈𝑥max/𝛿⌉
.
Discussion about different distortion costs. Note that Assumption B.1 still holds if we replace the distortion cost function 𝑣(𝑟) = 1
𝑟by
𝑣(𝑟) = log(𝑟max/𝑟). This is because the new switching cost
𝑐′
𝑡(𝑥𝑡:𝑡−2;𝑤𝑡) = 𝜔𝑡𝑢𝑡log(𝑟max𝑢𝑡) + 𝛾(𝑢𝑡−𝑢𝑡−1)2
= (𝑥𝑡−𝑥𝑡−1 + 1) log
𝑟max(𝑥𝑡−𝑥𝑡−1 + 1)
𝜔𝑡

+ 𝛾(𝜔𝑡−1𝑥𝑡+ 𝜔𝑡𝑥𝑡−2 −(𝜔𝑡+ 𝜔𝑡−1)𝑥𝑡−1 + (𝜔𝑡−1 −𝜔𝑡))2
𝜔2
𝑡𝜔2
𝑡−1
also satisfies Assumption B.1 for any 𝑤𝑡= (𝜔𝑡,𝜔𝑡−1) ∈[𝜔min,𝜔max]2 and feasible 𝑥𝑡:𝑡−2.
633
```


### Pagina 22
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
B.1
Proof of Theorem B.1
To show Theorem B.1, we first need to define indicators of active constraints, denoted as 𝜉∈{0, 1}4𝑝+5. Specifically, given the unique optimal
solution 𝑥0:𝑝= 𝜓(𝑦,𝑧; 𝜇,𝑤,𝛿) under a tuple of parameters (𝑦,𝑧; 𝜇,𝑤,𝛿), we consider whether the following equality conditions hold:
𝜉1,𝑡= 1{𝑥𝑡= 0}, ∀0 ≤𝑡≤𝑝;
𝜉2,𝑡= 1{𝑥𝑡= 𝑥max}, ∀0 ≤𝑡≤𝑝;
𝜉3,𝑡= 1{𝑥𝑡= 𝜇𝑡}, ∀0 ≤𝑡≤𝑝;
𝜉4,𝑡= 1{𝑥𝑡−𝑥𝑡−1 = −𝛿𝑡}, ∀0 ≤𝑡≤𝑝+ 1.
And we define indicators of the sides (denoted as 𝜎∈{0, 1}𝑝+1) as the following:
𝜎𝑡= 1{𝑥𝑡∈[𝜇𝑡,𝑥max]}, ∀0 ≤𝑡≤𝑝.
To simplify the notation, we let 𝜃B (𝜇,𝑤,𝛿) ∈Θ B [0,𝑥max]𝑝+1 × W𝑝+𝐻× Δ𝑝+2. While 𝜓(𝑦,𝑧;𝜃) can decide a unique pair of (𝜉, 𝜎), we
can also define a new equality-constrained optimization problem using (𝑦,𝑧;𝜃) and (𝜉, 𝜎):
Definition B.1. We define the equality-constrained optimization problem ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) as
ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) =
arg min
𝑥−𝐻+1:𝑝+𝐻−1
𝑝
∑︁
𝑡=0
𝑓(𝜎𝑡)
𝑡
(𝑥𝑡; 𝜇𝑡) +
𝑝+𝐻−1
∑︁
𝑡=0
𝑐𝑡(𝑥𝑡:𝑡−𝐻+1;𝑤𝑡)
(9a)
s.t. 𝑥𝑡=


0,
if 𝜉1,𝑡= 1
𝑥max,
if 𝜉2,𝑡= 1
𝜇𝑡,
if 𝜉3,𝑡= 1
, ∀0 ≤𝑡≤𝑝,
(9b)
𝑥𝑡−𝑥𝑡−1 = −𝛿𝑡, if 𝜉4,𝑡= 1, ∀0 ≤𝑡≤𝑝+ 1,
(9c)
𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧.
(9d)
Note that it is possible that the optimization problem ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) for some parameters and constraint configurations. We use ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎)
to denote the optimal value of this optimization problem. The following lemma states that the optimal solution of (7) will not change if we
remove all inactive inequality constraints and leave active constraints as equality constraints.
Lemma B.2. Suppose Assumption B.1 holds and 𝑝≥𝑑. For 𝑦,𝑧∈[0,𝑥max]𝐻−1 and 𝜃∈Θ, let 𝜉, 𝜎be the corresponding indicators of active
constraints/sides. Then, we have
𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) and 𝜄(𝑦,𝑧;𝜃) = ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎).
Proof of Lemma B.2. Note that
𝜄(𝑦,𝑧;𝜃) ≥ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎)
because the optimization problem on the RHS has less constraints. If the inequality holds with equality, we must have𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎)
since the optimal solution for the LHS is feasible for the RHS by the assumption on active constraints, and the optimization problem on the
RHS has a unique solution. Otherwise, we must have
𝜓(𝑦,𝑧;𝜃) ≠ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) , and 𝜄(𝑦,𝑧;𝜃) > ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎) .
Consider the convex combination 𝜁(𝜂) for 𝜂∈[0, 1] defined as
𝜁(𝜂) = (1 −𝜂)𝜓(𝑦,𝑧;𝜃) + 𝜂ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) .
Note that 𝜁(𝜂) satisfies all the active constraints and sides as specified by (𝜉, 𝜎) because they are active for all 𝜂∈[0, 1]. Since the constraints
of (7) that are not in (𝜉, 𝜎) are inactive at 𝜂= 0, there must exist 𝜂> 0 such that 𝜁(𝜂) is also feasible for (7). 𝜁(𝜂) achieves a strictly smaller
objective than 𝜁(0) = 𝜓(𝑦,𝑧;𝜃), which leads to a contradiction.
□
Lemma B.2 establishes that given any feasible tuple of (𝑦,𝑧;𝜃), one can find at least one pair of (𝜉, 𝜎) such that 𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎),
while there can be other (𝜉′, 𝜎′) that satisfies 𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉′, 𝜎′).
Lemma B.3. Suppose Assumption B.1 holds and 𝑝≥𝑑. If both ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) and ˆ𝜓(𝑦′,𝑧′;𝜃′; 𝜉, 𝜎) exist for 𝑦,𝑧,𝑦′,𝑧′ ∈[0,𝑥max]𝐻−1 and
(𝜉, 𝜎), then we have



 ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎)𝑡−ˆ𝜓(𝑦′,𝑧′;𝜃′; 𝜉, 𝜎)𝑡



≤𝐶 𝜌𝑡

𝑦−𝑦′

 + 𝜌𝑝−𝑡

𝑧−𝑧′

 + 𝐶©­
«
𝑝
∑︁
𝜏=0
𝜌|𝑡−𝜏| 𝜇𝜏−𝜇′
𝜏
 +
𝑝+𝐻−1
∑︁
𝜏=0
𝜌|𝑡−𝜏|

𝑤𝜏−𝑤′
𝜏


 +
𝑝+1
∑︁
𝜏=0
𝜌|𝑡−𝜏| 𝛿𝜏−𝛿′
𝜏
ª®
¬
,
(10)
634
```


### Pagina 23
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
where
𝜌=
©­­
«
1 −
2
1 +
√︃
1 + (ℓ/𝑚𝑓)
ª®®
¬
1
𝐻(𝐻+𝑑)
,𝐶=
2¯ℓ
𝑚𝑓𝜌(𝐻−2) (𝐻+𝑑) .
Here, ℓB max{𝐻ℓ𝑐, ℓ𝑤} and ¯ℓB max{𝐻ℓ𝑓, ℓ𝜇, ℓ}.
Proof of Lemma B.3. We do a variable change to eliminate all constraints in the equality-constrained optimization problem. After the
elimination, we get an unconstrained optimization problem with the free variables 𝑥𝑡0,𝑥𝑡1, . . . ,𝑥𝑡𝑞where the indices satisfy 0 ≤𝑡0 < 𝑡1 <
. . . < 𝑡𝑞≤𝑝. To simplify the notation, we let 𝑡−1 = −1 and 𝑡𝑞+1 = 𝑝+ 1. For 𝜏that satisfies 𝑡𝑖< 𝜏< 𝑡𝑖+1, we have either 𝑥𝜏= 𝑥𝑡𝑖−Í𝜏
𝛾=𝑡𝑖+1 𝛿𝛾
or 𝑥𝜏is some constant. Without loss of generality, we can assume 𝑡𝑖+1 ≤𝑡𝑖+ 𝑑+ 𝐻, because otherwise we can find 𝜏∈(𝑡𝑖,𝑡𝑖+1 −𝐻] such
that 𝑥𝜏:𝜏+𝐻−1 are constants, which means the free variables after 𝑥𝑡𝑖+1 will not change, regardless of how we perturb 𝑦, and the free variables
before 𝑥𝑡𝑖will not change, regardless of how we perturb 𝑧. Thus, we can decompose the perturbation to the left side and the right side and
derive them separately.
After the change of variable, the objective becomes a function ˆℎof 𝑥𝑡0,𝑥𝑡1, . . . ,𝑥𝑡𝑞. To simplify the notation, we let ˆ𝑥𝜏B 𝑥𝑡𝜏, where
𝜏= 0, . . . ,𝑞. We can decompose ˆℎas
ˆℎ( ˆ𝑥0:𝑞;𝜁) = ˆℎ𝑎( ˆ𝑥0:𝑞; 𝜇) + ˆℎ𝑏( ˆ𝑥0:𝑞;𝜁),
where 𝜁= (𝑦,𝑧,𝜃), ˆℎ𝑎is the sum of the original hitting costs minus 𝑚𝑓
2


ˆ𝑥0:𝑞


2, and ˆℎ𝑏is the sum of the original switching costs plus
𝑚𝑓
2


ˆ𝑥0:𝑞


2. By Assumption B.1, we see that
∇2
ˆ𝑥0:𝑞ˆℎ𝑎( ˆ𝑥0:𝑞; 𝜇) ⪰0, (𝑚𝑓+ 𝐻ℓ𝑐)𝐼⪰∇2
ˆ𝑥0:𝑞ˆℎ𝑏( ˆ𝑥0:𝑞;𝜁) ⪰𝑚𝑓𝐼.
(11)
We also note that ∇2
ˆ𝑥0:𝑞
ˆℎ𝑎( ˆ𝑥0:𝑞; 𝜇) is a diagonal matrix and ∇2
ˆ𝑥0:𝑞
ˆℎ𝑏( ˆ𝑥0:𝑞;𝜁) is a 2𝐻-banded matrix.
We can follow a similar procedure as Theorem 3.1 in [49] to show



 ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎)𝑡𝜏−ˆ𝜓(𝑦′,𝑧′;𝜃′; 𝜉, 𝜎)𝑡𝜏



≤𝐶0

𝜌𝜏
0


𝑦−𝑦′

 + 𝜌𝑞−𝜏
0


𝑧−𝑧′


+ 𝐶0 ©­
«
𝑝
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0
𝜇𝑖−𝜇′
𝑖
 +
𝑝+𝐻−1
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑤𝑖−𝑤′
𝑖


 +
𝑝+1
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝛿𝑖−𝛿′
𝑖


ª®
¬
,
(12)
where 𝜙(𝑖) denotes the integer 𝑗that satisfies 𝑡𝑗≤𝑖< 𝑡𝑗+1 and
𝜌0 =
©­­
«
1 −
2
√︃
1 + (ℓ/𝑚𝑓)
ª®®
¬
1
𝐻
,𝐶0 =
2¯ℓ
𝑚𝑓𝜌𝐻−2
0
.
Here, ℓB max{𝐻ℓ𝑐, ℓ𝑤} and ¯ℓB max{𝐻ℓ𝑓, ℓ𝜇, ℓ}. For completeness, we give the detailed proof below: Let 𝑒be a vector such that both 𝜁and
𝜁+ 𝑒are in Y × Z × Θ. Consider the function
𝜓(𝜁+ 𝜂𝑒) B ˆ𝜓(𝜁+ 𝜂𝑒; 𝜉, 𝜎)𝑡0:𝑞,
which is implicitly determined by the equation
∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒) = 0.
By the implicit function theorem we know that the function 𝜓is differentiable. Taking the derivative with respect to 𝜃gives that
∇2
ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒) 𝑑
𝑑𝜂𝜓(𝜁+ 𝜂𝑒) = −∇𝑦∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝑦−∇𝑧∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝑧
−
𝑝
∑︁
𝑡=0
∇𝜇𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝜇𝑡−
𝑝+𝐻−1
∑︁
𝑡=0
∇𝑤𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝑤𝑡
−
𝑝
∑︁
𝑡=0
∇𝛿𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒)𝑒𝛿𝑡.
635
```


### Pagina 24
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
To simplify the notation, we define
𝑀B ∇2
ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × (𝑞+ 1) matrix,
𝑅(𝑦) B −∇𝑦∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × (𝐻−1) matrix,
𝑅(𝑧) B −∇𝑧∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × (𝐻−1) matrix,
𝑅(𝜇𝑡) B −∇𝜇𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × 1 matrix,
𝑅(𝑤𝑡) B −∇𝑤𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × 𝑑matrix,
𝑅(𝛿𝑡) B −∇𝛿𝑡∇ˆ𝑥0:𝑞ˆℎ(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒), which is a (𝑞+ 1) × 1 matrix.
Hence we can write
𝑑
𝑑𝜃𝜓(𝜁+ 𝜂𝑒) = 𝑀−1 ©­
«
𝑅(𝑦)𝑒𝑦+ 𝑅(𝑧)𝑒𝑧+
𝑝
∑︁
𝑡=0
𝑅(𝜇𝑡)𝑒𝜇𝑡+
𝑝+𝐻−1
∑︁
𝑡=0
𝑅(𝑤𝑡)𝑒𝑤𝑡+
𝑝
∑︁
𝑡=0
𝑅(𝛿𝑡)𝑒𝛿𝑡
ª®
¬
.
Recall that 𝑅(𝑦), 𝑅(𝑧) are (𝑞+ 1) × (𝐻−1) matrices. For 𝑅(𝑦), only the first 𝐻−1 rows are non-zero. For 𝑅(𝑧), only the last 𝐻−1 rows are
non-zero. Hence we see that
𝑑
𝑑𝜂𝜓(𝜁+ 𝜂𝑒)𝜏= (𝑀−1)𝜏,0:𝐻−2𝑅(𝑦)
0:𝐻−2,:𝑒𝑦+ (𝑀−1)𝜏,𝑞−𝐻+2:𝑞𝑅(𝑧)
𝑞−𝐻+2:𝑞,:𝑒𝑧
+
𝑞
∑︁
𝑗=0
𝑡𝑗+1−1
∑︁
𝑖=𝑡𝑗
(𝑀−1)𝜏,𝑗𝑅(𝜇𝑖)
𝑗,: 𝑒𝜇𝑖+
𝑞+1
∑︁
𝑗=0
𝑡𝑗+1−1
∑︁
𝑖=𝑡𝑗
(𝑀−1)𝜏,𝑗−𝐻+1:𝑗+𝐻−1𝑅(𝑤𝑖)
𝑗−𝐻+1:𝑗+𝐻−1,:𝑒𝑤𝑖
+
𝑞
∑︁
𝑗=0
𝑡𝑗+1−1
∑︁
𝑖=𝑡𝑗
(𝑀−1)𝜏,𝑗𝑅(𝛿𝑖)
𝑗,: 𝑒𝛿𝑖.
(13)
Recall that ¯ℓB max{𝐻ℓ𝑐, 𝐻ℓ𝑓, ℓ𝜇, ℓ𝑤}. We know that the norms of
𝑅(𝑦)
0:𝐻−2,:, 𝑅(𝑧)
𝑞−𝐻+2:𝑞,:, 𝑅(𝜇𝑖)
𝑗,: , 𝑅(𝑤𝑖)
𝑗−𝐻+1:𝑗+𝐻−1,:, and 𝑅(𝛿𝑖)
𝑗,:
are all upper bounded by ¯ℓ. Taking norm on both sides of (13) gives




𝑑
𝑑𝜃𝜓(𝜁+ 𝜂𝑒)𝜏




 ≤¯ℓ


(𝑀−1)𝜏,0:𝐻−2




𝑒𝑦


 + ¯ℓ


(𝑀−1)𝜏,𝑞−𝐻+2:𝑞


 ∥𝑒𝑧∥
+ ¯ℓ
𝑞
∑︁
𝑗=0
𝑡𝑗+1−1
∑︁
𝑖=𝑡𝑗


(𝑀−1)𝜏,𝑗




𝑒𝜇𝑖


 + ¯ℓ
𝑞+1
∑︁
𝑗=0
𝑡𝑗+1−1
∑︁
𝑖=𝑡𝑗


(𝑀−1)𝜏,𝑗−𝐻+1:𝑗+𝐻−1




𝑒𝑤𝑖


+ ¯ℓ
𝑞
∑︁
𝑗=0
𝑡𝑗+1−1
∑︁
𝑖=𝑡𝑗


(𝑀−1)𝜏,𝑗




𝑒𝛿𝑖


 .
(14)
Note that 𝑀can be decomposed as 𝑀= 𝑀𝑎+ 𝑀𝑏, where
𝑀𝑎:= ∇2
ˆ𝑥0:𝑞ˆℎ𝑎(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒),
𝑀𝑏:= ∇2
ˆ𝑥0:𝑞ˆℎ𝑏(𝜓(𝜁+ 𝜂𝑒),𝜁+ 𝜂𝑒).
Since 𝑀𝑎is a diagonal (𝑞+ 1) × (𝑞+ 1) matrix and satisfies 𝑀𝑎⪰0, and 𝑀𝑏is 2𝐻-banded and satisfies (𝑚𝑓+ ℓ)𝐼⪰𝑀𝑏⪰𝑚𝑓𝐼, we obtain
the following with Lemma B.1 in [49]:


(𝑀−1)𝜏,0:𝐻−2


 ≤
2
𝑚𝑓
𝜌𝜏−(𝐻−2)
0
,


(𝑀−1)𝜏,𝑞−𝐻+2:𝑞


 ≤
2
𝑚𝑓
𝜌𝑞−𝜏−(𝐻−2)
0


(𝑀−1)𝜏,𝑗


 ≤
2
𝑚𝑓
𝜌|𝜏−𝑗|
0
,


(𝑀−1)𝜏,𝑗−𝐻+1:𝑗+𝐻−1


 ≤
2
𝑚𝑓
𝜌|𝜏−𝑗|−(𝐻−1)
0
,
where 𝜌0 := (
√︁
𝑐𝑜𝑛𝑑(𝑀𝑏) −1)/(
√︁
𝑐𝑜𝑛𝑑(𝑀𝑏) + 1) = 1 −2 ·
√︁
1 + (ℓ/𝜇) + 1
−1
.
Substituting this into (14), we see that




𝑑
𝑑𝜃𝜓(𝜁+ 𝜃𝑒)𝜏




 ≤𝐶0 ©­
«
𝜌𝜏
0


𝑒𝑦


 + 𝜌𝑞−𝜏
0
∥𝑒𝑧∥+
𝑝
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑒𝜇𝑖


 +
𝑝+𝐻−1
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑒𝑤𝑖


 +
𝑝
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑒𝛿𝑖


ª®
¬
.
636
```


### Pagina 25
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Hence we obtain



𝜓(𝜁)𝜏−𝜓(𝜁+ 𝑒)𝜏



 =




∫1
0
𝑑
𝑑𝜂𝜓(𝜁+ 𝜂𝑒)𝜏𝑑𝜂




≤
∫1
0




𝑑
𝑑𝜂𝜓(𝜁+ 𝜂𝑒)𝜏




𝑑𝜂
≤𝐶0 ©­
«
𝜌𝜏
0


𝑒𝑦


 + 𝜌𝑞−𝜏
0
∥𝑒𝑧∥+
𝑝
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑒𝜇𝑖


 +
𝑝+𝐻−1
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑒𝑤𝑖


 +
𝑝
∑︁
𝑖=0
𝜌|𝜙(𝑖)−𝜏|
0


𝑒𝛿𝑖


ª®
¬
.
This finishes the proof of (12). Recall that we have 𝑡𝑖< 𝑡𝑖+1 ≤𝑡𝑖+ 𝑑+ 𝐻. Therefore, (12) implies (10).
□
In the next lemma, we show a continuity property of the “equality-constrained labeling” method.
Lemma B.4. Suppose Assumption B.1 holds and 𝑝≥𝑑. For a pair of (𝜉, 𝜎), if any tuple in the sequence {(𝑦𝑞,𝑧𝑞;𝜃𝑞)}∞
𝑞=1 satisfies𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞) =
ˆ𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) and lim𝑞→∞(𝑦𝑞,𝑧𝑞,𝜃𝑞) = (𝑦,𝑧,𝜃), then we have
𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎).
Proof of Lemma B.4. Note that the perturbation bound in Lemma B.3 also establishes the continuity of the function ˆ𝜓(·, ·; ·; 𝜉, 𝜎).
Therefore, we see that
lim
𝑞→∞𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞) = lim
𝑞→∞
ˆ𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎).
Since the constraint set of (7) is closed, we know ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) is a feasible solution of (7).
For the sake of contradiction, we assume 𝜓(𝑦,𝑧;𝜃) ≠ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎). In this case, since ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎) is feasible for (7), we must have
𝜄(𝑦,𝑧;𝜃) < ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎).
Define the optimality gap as Λ B ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎) −𝜄(𝑦,𝑧;𝜃).
Since lim𝑞→∞(𝑦𝑞,𝑧𝑞;𝜃𝑞) = (𝑦,𝑧;𝜃), for an arbitrary small positive real number 𝜖, we can find a positive integer 𝑞such that


𝑦𝑞−𝑦


 +


𝑧𝑞−𝑧


 + 𝑑𝑖𝑠𝑡(𝜃,𝜃𝑞) < 𝜖,
where 𝑑𝑖𝑠𝑡(𝜃,𝜃′) = Í𝑝
𝑖=0
𝜇𝑖−𝜇′
𝑖
 + Í𝑝+𝐻−1
𝑖=0


𝑤𝑖−𝑤′
𝑖


 + Í𝑝+1
𝑖=0
𝛿𝑖−𝛿′
𝑖
 . Based on 𝑥−𝐻+1:𝑝+𝐻−1 B 𝜓(𝑦,𝑧;𝜃), we construct a feasible solution
𝑥′
−𝐻+1:𝑝+𝐻−1 C 𝑥′ for the optimization problem (7) with parameters (𝑦𝑞,𝑧𝑞;𝜃𝑞) as following: Let 𝑥′
0:𝑝= 𝑥0:𝑝,𝑥−𝐻+1:−1 = 𝑦,𝑥𝑝+1:𝑝+𝐻−1 = 𝑧.
For 𝑡= 0, 1, . . ., if 𝑥′
𝑡−𝑥′
𝑡−1 < −𝛿(𝑞)
𝑡
, we increase 𝑥′
𝑡such that 𝑥′
𝑡= 𝑥′
𝑡−1 −𝛿(𝑞)
𝑡
. Then, for 𝑡= 𝑝, 𝑝−1, . . ., if 𝑥′
𝑡+1 −𝑥′
𝑡< −𝛿(𝑞)
𝑡+1, we decrease 𝑥′
𝑡
such that 𝑥′
𝑡= 𝑥′
𝑡+1 + 𝛿(𝑞)
𝑡+1. Note that this procedure can guarantee that 𝑥′ is a feasible solution for (7), and their distance are upper bounded
by


𝜓(𝑦,𝑧;𝜃) −𝑥′

 ≤(2𝑑+ 1)𝜖.
(15)
Since the objective function of (7) is Lipschitz in (𝑥,𝑦,𝑧,𝜃), by (15), we know there exists some positive constant 𝑐0 such that
𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞) −𝜄(𝑦,𝑧;𝜃) ≤𝑐0
 

𝑥′ −𝜓(𝑦,𝑧;𝜃)


 + 𝜖 ≤(2𝑑+ 2)𝑐0𝜖.
(16)
On the other hand, by Lemma B.3, we see that



 ˆ𝜓(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) −ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎)



 ≤

𝐶
1 −𝜌+ 1

𝜖.
(17)
Since the objective function of (7) is smooth in (𝑥,𝑦,𝑧,𝜃), by (17), we see that
ˆ𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) −ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎)
 ≤𝑐0

𝐶
1 −𝜌+ 2

𝜖.
(18)
Therefore, we see that
ˆ𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) −𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞) ≥−
ˆ𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) −ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎)
 + (ˆ𝜄(𝑦,𝑧;𝜃; 𝜉, 𝜎) −𝜄(𝑦,𝑧;𝜃)) + (𝜄(𝑦,𝑧;𝜃) −𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞))
≥−𝑐0

𝐶
1 −𝜌+ 2

𝜖+ Λ −𝑐0(2𝑑+ 2)𝜖
(19a)
= Λ −𝑐0

𝐶
1 −𝜌+ 2𝑑+ 4

𝜖,
where we used (16) and (18) in (19a). Let 𝜖B 1
2Λ𝑐−1
0

𝐶
1−𝜌+ 2𝑑+ 4
−1
leads to a contradiction with the assumption that ˆ𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞; 𝜉, 𝜎) =
𝜄(𝑦𝑞,𝑧𝑞;𝜃𝑞). Therefore, we have shown that 𝜓(𝑦,𝑧;𝜃) = ˆ𝜓(𝑦,𝑧;𝜃; 𝜉, 𝜎).
□
With the above technical lemmas, we are ready to finish the proof of Theorem B.1.
637
```


### Pagina 26
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Proof of Theorem B.1. Consider the segment ((1 −𝜂)𝑦+ 𝜂𝑦′, (1 −𝜂)𝑧+ 𝜂𝑧′; (1 −𝜂)𝜃+ 𝜂𝜃′) ,𝜂∈[0, 1]. Note that since (1−𝜂)𝜓(𝑦,𝑧;𝜃)+
𝜂𝜓(𝑦′,𝑧′;𝜃′) is a feasible solution for the optimization problem (7) parameterized by
 (1 −𝜂)𝑦+ 𝜂𝑦′, (1 −𝜂)𝑧+ 𝜂𝑧′; (1 −𝜂)𝜃+ 𝜂𝜃′ ,
we know that the corresponding optimization problem is feasible. With some slight abuse of notation, we use (𝜉, 𝜎)(𝜂) ⊆Ξ × Σ to denote
the set of indicators of active constraints and sides such that
𝜓 (1 −𝜂)𝑦+ 𝜂𝑦′, (1 −𝜂)𝑧+ 𝜂𝑧′; (1 −𝜂)𝜃+ 𝜂𝜃′
= ˆ𝜓 (1 −𝜂)𝑦+ 𝜂𝑦′, (1 −𝜂)𝑧+ 𝜂𝑧′; (1 −𝜂)𝜃+ 𝜂𝜃′; 𝜉, 𝜎 , ∀(𝜉, 𝜎) ∈(𝜉, 𝜎)(𝜂).
By Lemma B.2, we know this set is not empty for any 𝜂∈[0, 1].
We can divide the interval [0, 1] into 0 = 𝜂0 < 𝜂1 < . . . < 𝜂𝑞= 1 for some positive integer 𝑞≤25𝑝+6 such that there exists a sequence of
different indicators of active constraints and sides (𝜉, 𝜎)0:𝑞−1 which satisfies
𝜓 (1 −𝜂𝑖)(𝑦,𝑧;𝜃) + 𝜂𝑖(𝑦′,𝑧′;𝜃′) = ˆ𝜓 (1 −𝜂𝑖)(𝑦,𝑧;𝜃) + 𝜂𝑖(𝑦′,𝑧′;𝜃′); (𝜉, 𝜎)𝑖
 ,
𝜓 (1 −𝜂𝑖+1)(𝑦,𝑧;𝜃) + 𝜂𝑖+1(𝑦′,𝑧′;𝜃′) = ˆ𝜓 (1 −𝜂𝑖+1)(𝑦,𝑧;𝜃) + 𝜂𝑖+1(𝑦′,𝑧′;𝜃′); (𝜉, 𝜎)𝑖

for all 0 ≤𝑖≤𝑞−1. Note that this requires (𝜉, 𝜎)(𝜂𝑖) to contain both (𝜉, 𝜎)𝑖−1 and (𝜉, 𝜎)𝑖for 𝑖= 1, . . . ,𝑞−1. To construct the sequence 𝜂0:𝑞
and (𝜉, 𝜎)0:𝑞−1, we first have 𝜂0 = 0 and let (𝜉, 𝜎)0 be any pair (𝜉, 𝜎) ∈(𝜉, 𝜎)(𝜂0) such that
sup{𝜂∈[0, 1] | 𝜓 (1 −𝜂)(𝑦,𝑧;𝜃) + 𝜂(𝑦′,𝑧′;𝜃′) = ˆ𝜓 (1 −𝜂)(𝑦,𝑧;𝜃) + 𝜂(𝑦′,𝑧′;𝜃′); 𝜉, 𝜎} > 0,
and let 𝜂1 be the supremum value above. Since 0 = inf(0, 1] and (𝜉, 𝜎)(𝜂) ⊆Ξ × Σ is nonempty for every 𝜂∈(0, 1], we know such (𝜉, 𝜎)0
exists by Lemma B.4. Suppose we have already constructed 𝜂0:𝑖, (𝜉, 𝜎)0:𝑖−1, and 𝜂𝑖< 1. Then we select (𝜉, 𝜎)𝑖to be any pair (𝜉, 𝜎) such that
sup{𝜂∈[0, 1] | 𝜓 (1 −𝜂)(𝑦,𝑧;𝜃) + 𝜂(𝑦′,𝑧′;𝜃′) = ˆ𝜓 (1 −𝜂)(𝑦,𝑧;𝜃) + 𝜂(𝑦′,𝑧′;𝜃′); 𝜉, 𝜎} > 𝜂𝑖,
and let 𝜂𝑖+1 be the supremum value above. We can repeat this construction and stop when 𝜂𝑖+1 = 1. By the construction, we know all pairs
in the sequence (𝜉, 𝜎)0:𝑖−1 are distinct, thus the construction will terminate in finite time. Hence, we have a finite index 𝑞such that 𝜂𝑞= 1.
By Lemma B.3, we know that


𝜓 (1 −𝜂𝑖)(𝑦,𝑧;𝜃) + 𝜂𝑖(𝑦′,𝑧′;𝜃′)
𝑡−𝜓 (1 −𝜂𝑖+1)(𝑦,𝑧;𝜃) + 𝜂𝑖+1(𝑦′,𝑧′;𝜃′)
𝑡


≤(𝜂𝑖+1 −𝜂𝑖)𝐶 𝜌𝑡

𝑦−𝑦′

 + 𝜌𝑝−𝑡

𝑧−𝑧′

 + (𝜂𝑖+1 −𝜂𝑖)𝐶©­
«
𝑝
∑︁
𝜏=0
𝜌|𝑡−𝜏| 𝜇𝜏−𝜇′
𝜏
 +
𝑝+𝐻−1
∑︁
𝜏=0
𝜌|𝑡−𝜏|

𝑤𝜏−𝑤′
𝜏


 +
𝑝+1
∑︁
𝜏=0
𝜌|𝑡−𝜏|

𝛿𝜏−𝛿′
𝜏


ª®
¬
.
(20)
Summing (20) over 𝑖= 0, 1, . . . ,𝑞−1 finishes the proof.
□
C
PROOFS FOR EXACT PREDICTIONS
C.1
Proof of Lemma A.4
To simplify the notation, we introduce the shorthand
𝑥∗
𝜏|𝑡= 𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝜏,𝑢∗
𝜏|𝑡= 𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝜏, ∀𝜏≥𝑡.
And we use {(𝑥∗
𝑡,𝑢∗
𝑡)}𝑁
𝑡=1 to denote the offline optimal trajectory.
For time step 𝑡< 𝑁−𝐾+ 1, we see that
𝑥𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡

2
≤

𝐶𝜌𝐾𝑥∗
𝑡+𝐾|𝑡−¯𝑥
 + 𝐶𝜌𝐾−1
𝑢∗
𝑡+𝐾−1|𝑡−
1
𝜔𝑡+𝐾−1

2
(21a)
≤

𝐶𝜌𝐾𝑥∗
𝑡+𝐾|𝑡−𝑥∗
𝑡+𝐾
 +
𝑥∗
𝑡+𝐾−¯𝑥


+ 𝐶𝜌𝐾−1
𝑢∗
𝑡+𝐾−1|𝑡−𝑢∗
𝑡+𝐾−1
 +
𝑢∗
𝑡+𝐾−1 −
1
𝜔𝑡+𝐾−1

2
(21b)
≤4𝐶2𝜌2𝐾𝑥∗
𝑡+𝐾|𝑡−𝑥∗
𝑡+𝐾

2
+ 4𝐶2𝜌2𝐾−2 𝑢∗
𝑡+𝐾−1|𝑡−𝑢∗
𝑡+𝐾−1

2
+ 4𝐶2𝜌2𝐾𝑥∗
𝑡+𝐾−1 −¯𝑥
2 +
+ 4𝐶2𝜌2𝐾−2
𝑢∗
𝑡+𝐾−1 −
1
𝜔𝑡+𝐾−1

2
.
(21c)
638
```


### Pagina 27
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
where in (21a), we use
𝑥𝑡= 𝜓𝑡+𝐾−1
𝑡

(𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑡+𝐾−1; ( ¯𝑥,
1
𝜔𝑡+𝐾−1
)

𝑥𝑡
,
𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡= 𝜓𝑡+𝐾−1
𝑡

(𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑡+𝐾−1; (𝑥∗
𝑡+𝐾|𝑡,𝑢∗
𝑡+𝐾−1|𝑡)

𝑥𝑡
,
and the exponentially decaying perturbation bound. We use the triangle inequality in (21b) and rearrange the terms in (21c).
We note that for the first term in (21), we have
𝑥∗
𝑡+𝐾|𝑡−𝑥∗
𝑡+𝐾
 ≤𝐶𝜌𝐾+1  𝑥𝑡−1 −𝑥∗
𝑡−1
 +
𝑢𝑡−1 −𝑢∗
𝑡−1
 .
(22)
For the second term, we have
𝑢∗
𝑡+𝐾−1|𝑡−𝑢∗
𝑡+𝐾−1
 ≤𝐶′𝜌𝐾 𝑥𝑡−1 −𝑥∗
𝑡−1
 +
𝑢𝑡−1 −𝑢∗
𝑡−1
 .
(23)
For the third term, we have
𝑥∗
𝑡+𝐾−¯𝑥
2 ≤1
𝜖𝛽𝑏(𝑥∗
𝑡+𝐾).
(24)
For the last term, we see that
𝑢∗
𝑡+𝐾−1 −
1
𝜔𝑡+𝐾−1

2
≤
(𝑥∗
𝑡+𝐾−1 −𝑥∗
𝑡+𝐾−2)2
𝜔2
𝑡+𝐾−1
≤
2(𝑥∗
𝑡+𝐾−1 −¯𝑥)2 + 2( ¯𝑥−𝑥∗
𝑡+𝐾−2)2
𝜔2
𝑡+𝐾−1
≤
2𝑏(𝑥∗
𝑡+𝐾−1) + 2𝑏(𝑥∗
𝑡+𝐾−2)
𝜖𝛽𝜔2
min
.
(25)
Substituting (22), (23), (24), (25) into (21) gives that
𝑥𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡

2
≤8𝐶4𝜌4𝐾+2 𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+ 8(𝐶′)2𝐶2𝜌4𝐾−2 𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+ 4𝐶2𝜌2𝐾−2 (2 + 𝜔2
min)𝑏(𝑥∗
𝑡+𝐾−1) + 2𝑏(𝑥∗
𝑡+𝐾−2)
𝜖𝛽𝜔2
min
(26)
Similarly, we can obtain that
𝑢𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝑡

2
≤8(𝐶′)2𝐶2𝜌4𝐾+2 𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+ 8(𝐶′)4𝜌4𝐾−2 𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+ 4(𝐶′)2𝜌2𝐾−2 (2 + 𝜔2
min)𝑏(𝑥∗
𝑡+𝐾−1) + 2𝑏(𝑥∗
𝑡+𝐾−2)
𝜖𝛽𝜔2
min
(27)
Therefore, combining (26) and (27) gives that
𝑒2
𝑡≤2
𝑥𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡

2
+ 2
𝑢𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝑡

2
≤16𝜌4𝐾−2 
𝐶2 + (𝐶′)22 𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+ 8𝜌2𝐾−2 
𝐶2 + (𝐶′)2 (2 + 𝜔2
min)𝑏(𝑥∗
𝑡+𝐾−1) + 2𝑏(𝑥∗
𝑡+𝐾−2)
𝜖𝜔2
min
.
C.2
Proof of Lemma A.5
We see the distance between the trajectories of SODA and the offline optimal at an intermediate time step can be bounded by
𝑥𝑡−𝑥∗
𝑡
 +
𝑢𝑡−𝑢∗
𝑡
 =
𝑥𝑡−𝜓𝑁
1 ((𝑥0,𝑢0);𝜔1:𝑁; 0)𝑥𝑡
 +
𝑢𝑡−𝜓𝑁
1 ((𝑥0,𝑢0);𝜔1:𝑁; 0)𝑢𝑡

≤
𝑥𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡
 +
𝑢𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝑡

+
𝑡−1
∑︁
𝜏=1
𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑥𝑡−𝜓𝑁
𝜏+1 ((𝑥𝜏,𝑢𝜏);𝜔𝜏+1:𝑁; 0)𝑥𝑡

+
𝑡−1
∑︁
𝜏=1
𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑢𝑡−𝜓𝑁
𝜏+1 ((𝑥𝜏,𝑢𝜏);𝜔𝜏+1:𝑁; 0)𝑢𝑡

(28a)
≤𝑒𝑡+ (𝐶+ 𝐶′)
𝑡−1
∑︁
𝜏=1
𝜌𝑡−𝜏𝑒𝜏.
(28b)
639
```


### Pagina 28
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
We use the triangle inequality in (28a). In (28b), we note that𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑥𝑡can be written as𝜓𝑁
𝜏+1

(𝑥∗
𝜏|𝜏−1,𝑢∗
𝜏|𝜏−1);𝜔𝜏+1:𝑁; 0

𝑥𝑡
,
where
𝑥∗
𝜏|𝜏−1 = 𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑥𝜏, and 𝑢∗
𝜏|𝜏−1 = 𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑢𝜏.
Thus, we can apply the exponentially decaying perturbation bound and Lemma A.4 to obtain
𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑥𝑡−𝜓𝑁
𝜏+1 ((𝑥𝜏,𝑢𝜏);𝜔𝜏+1:𝑁; 0)𝑥𝑡
 ≤𝐶𝜌𝑡−𝜏𝑒𝜏.
Similarly, we obtain that
𝜓𝑁
𝜏((𝑥𝜏−1,𝑢𝜏−1);𝜔𝜏:𝑁; 0)𝑢𝑡−𝜓𝑁
𝜏+1 ((𝑥𝜏,𝑢𝜏);𝜔𝜏+1:𝑁; 0)𝑢𝑡
 ≤𝐶′𝜌𝑡−𝜏𝑒𝜏.
Therefore, we see that
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2 ≤

1 + (𝐶+ 𝐶′)2
1 −𝜌

𝑡∑︁
𝜏=1
𝜌𝑡−𝜏𝑒2
𝜏.
Summing the above inequality over 𝑡= 1, 2, . . . ,𝑇gives that
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
≤
1
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌
 𝑁
∑︁
𝑡=1
𝑒2
𝑡.
C.3
Proof of Theorem A.3
Combining Lemmas A.4 and A.5, we see that
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
≤
1
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌

· 16𝜌4𝐾−2 
𝐶2 + (𝐶′)22 𝑁
∑︁
𝑡=1
𝑥𝑡−1 −𝑥∗
𝑡−1
2 +
𝑢𝑡−1 −𝑢∗
𝑡−1
2
+
1
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌

· 8𝜌2𝐾−2 
𝐶2 + (𝐶′)2 (4 + 𝜔2
min) Í𝑁
𝑡=1 𝑏(𝑥∗
𝑡)
𝜖𝛽𝜔2
min
.
(29)
Since the prediction horizon 𝐾satisfies
𝐾≥1
4 ln
 16
1 −𝜌·

1 + (𝐶+ 𝐶′)2
1 −𝜌

·

𝐶2 + (𝐶′)22
/ln
 1
𝜌

,
we see that
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
≤16𝜌2𝐾−2
1 −𝜌
·

1 + (𝐶+ 𝐶′)2
1 −𝜌
 
𝐶2 + (𝐶′)2 (4 + 𝜔2
min) Í𝑁
𝑡=1 𝑏(𝑥∗
𝑡)
𝜖𝜔2
min
.
(30)
On the other hand, we also see that for any 𝜂> 0, we have
cost(SODA) =
𝑁
∑︁
𝑡=1
𝜔𝑡𝑢2
𝑡+ 𝑏(𝑥𝑡) + 𝛾(𝑢𝑡−𝑢𝑡−1)2
=
𝑁
∑︁
𝑡=1
𝜔𝑡(𝑢∗
𝑡+ (𝑢𝑡−𝑢∗
𝑡))2 +
𝑁
∑︁
𝑡=1
𝑏(𝑥∗
𝑡+ (𝑥𝑡−𝑥∗
𝑡))
+
𝑁
∑︁
𝑡=1
𝛾(𝑢∗
𝑡−𝑢∗
𝑡−1 + (𝑢𝑡−𝑢∗
𝑡) −(𝑢𝑡−1 −𝑢∗
𝑡−1))2
≤(1 + 𝜂)
𝑁
∑︁
𝑡=1

𝜔𝑡(𝑢∗
𝑡)2 + 𝑏(𝑥∗
𝑡) + 𝛾(𝑢∗
𝑡−𝑢∗
𝑡−1)2
+

1 + 1
𝜂
 𝑁
∑︁
𝑡=1

𝜔𝑡(𝑢∗
𝑡−𝑢𝑡)2 + 𝛽(𝑥∗
𝑡−𝑥𝑡)2 + 2𝛾(𝑢∗
𝑡−𝑢𝑡)2 + 2𝛾(𝑢∗
𝑡−1 −𝑢𝑡−1)2
(31a)
≤(1 + 𝜂)cost(OPT) +

1 + 1
𝜂

(4𝛾+ 𝛽+ 𝜔max)
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
,
(31b)
where we use the quadratic form of the cost functions and the AM-GM inequality in (31a); we use (30) in (31b).
640
```


### Pagina 29
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Substituting (30) into (31) gives that
cost(SODA) −cost(OPT) ≤

𝜂+

1 + 1
𝜂

(4𝛾+ 𝛽+ 𝜔max) · 16𝜌2𝐾−2
1 −𝜌
·

1 + (𝐶+ 𝐶′)2
1 −𝜌
 
𝐶2 + (𝐶′)2
·
4 + 𝜔2
min
𝜖𝛽𝜔2
min
!
cost(OPT).
Letting 𝜂= 4

2(4𝛾+ 𝛽+ 𝜔max) ·
1
1−𝜌·

1 + (𝐶+𝐶′)2
1−𝜌
  𝐶2 + (𝐶′)2 · 4+𝜔2
min
𝜖𝛽𝜔2
min
1/2
finishes the proof.
D
PROOFS FOR INEXACT PREDICTIONS
D.1
Proof of Lemma A.6
Suppose {𝑥𝑡}1≤𝑡≤𝑁is a feasible trajectory of the buffer levels and {𝑥𝑡}𝑡1≤𝑡≤𝑡2 is a sub-trajectory such that 𝑥𝑡1−1 ≥¯𝑥−𝜁, 𝑥𝑡< ¯𝑥−𝜁, ∀𝑡=
𝑡1, . . . ,𝑡2, and 𝑥𝑡2+1 ≥¯𝑥−𝜁where 1 ≤𝑡1 < 𝑡2 < 𝑁.
For 𝜆≥0, consider the trajectory {𝑥′
𝑡(𝜆)}1≤𝑡≤𝑁constructed by
𝑥′
𝑡(𝜆) =
(
𝑥𝑡,
if 𝑡< 𝑡1 or 𝑡> 𝑡2
𝑥𝑡+ 𝜆,
otherwise.
Note that under this construction, {𝑥′
𝑡(0)}1≤𝑡≤𝑁is identical with the original trajectory {𝑥𝑡}1≤𝑡≤𝑁. Let Υ(𝜆) denote the total cost of this
trajectory. For sufficiently small 𝜆≥0, we see that
Υ(𝜆) −Υ(0) = 𝛽
𝑡2
∑︁
𝑡=𝑡1

(𝑥𝑡+ 𝜆−¯𝑥)2 −(𝑥𝑡−¯𝑥)2
+ 𝜔𝑡1

𝑢′
𝑡1 (𝜆)2 −𝑢2
𝑡1

+ 𝜔𝑡2+1

𝑢′
𝑡2+1(𝜆)2 −𝑢2
𝑡2+1

+ 𝛾

(𝑢′
𝑡1 (𝜆) −𝑢𝑡1−1)2 −(𝑢𝑡1 −𝑢𝑡1−1)2
+ 𝛾

(𝑢𝑡1+1 −𝑢′
𝑡1 (𝜆))2 −(𝑢𝑡1+1 −𝑢𝑡1)2
+ 𝛾

(𝑢′
𝑡2+1(𝜆) −𝑢𝑡2)2 −(𝑢𝑡2+1 −𝑢𝑡2)2
+ 𝛾

(𝑢𝑡2+2 −𝑢′
𝑡2+1(𝜆))2 −(𝑢𝑡2+2 −𝑢𝑡2+1)2
,
where 𝑢′
𝑡1 (𝜆) = 𝑢𝑡1 +
𝜆
𝜔𝑡1 and 𝑢′
𝑡2+1(𝜆) = 𝑢𝑡2+1 −
𝜆
𝜔𝑡2+1 .
Therefore, we see that
𝑑
𝑑𝜆Υ(𝜆)
𝜆=0+ =
𝑑
𝑑𝜆(Υ(𝜆) −Υ(0))
𝜆=0+
= 2𝛽
𝑡2
∑︁
𝑡=𝑡1
(𝑥𝑡−¯𝑥) + 2𝑢𝑡1 −2𝑢𝑡2+1 + 2𝛾
𝜔𝑡1
(2𝑢𝑡1 −𝑢𝑡1−1 −𝑢𝑡1+1) +
2𝛾
𝜔𝑡2+1
(−2𝑢𝑡2+1 + 𝑢𝑡2 + 𝑢𝑡2+2)
< −2𝛽𝜁+

2 +
8𝛾
𝜔min
  1
𝑟min
−
1
𝑟max

≤0.
Thus, we know that there exists 𝜆> 0 such that {𝑥′
𝑡(𝜆)}1≤𝑡≤𝑁is feasible and Υ(𝜆) is less than the total cost of {𝑥𝑡}1≤𝑡≤𝑁. Therefore, the
offline optimal trajectory cannot contain a sub-trajectory such that 𝑥𝑡1−1 ≥¯𝑥−𝜁, 𝑥𝑡< ¯𝑥−𝜁, ∀𝑡= 𝑡1, . . . ,𝑡2, and 𝑥𝑡2+1 ≥¯𝑥−𝜁where
1 ≤𝑡1 < 𝑡2 < 𝑁. Using similar techniques, we can extend this claim to include 𝑡2 = 𝑁and/or 𝑡1 = 𝑡2. Thus, the buffer levels in the offline
optimal trajectory do not go below ¯𝑥−𝜁. By symmetry, we can show that the offline optimal trajectory also does not exceed ¯𝑥+ 𝜁.
D.2
Proof of Lemma A.7
To simplify the notation, we introduce the shorthand
𝑥∗
𝜏|𝑡= 𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝜏,𝑢∗
𝜏|𝑡= 𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝜏, ∀𝜏≥𝑡.
And we use {(𝑥∗
𝑡,𝑢∗
𝑡)} to denote the offline optimal trajectory.
For time step 𝑡< 𝑁−𝐾+ 1, we see that
𝑥𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡
 ≤𝐶𝜌𝐾𝑥∗
𝑡+𝐾|𝑡−¯𝑥
 + 𝐶𝜌𝐾−1
𝑢∗
𝑡+𝐾−1|𝑡−
1
𝜔𝑡+𝐾−1
 + 𝐶
𝑡+𝐾−1
∑︁
𝜏=𝑡
𝜌𝜏−𝑡 ˆ𝜔𝜏|𝑡−1 −𝜔𝜏
 +
𝜔𝑡−ˆ𝜔𝑡|𝑡−1

𝑟min
(32a)
≤𝐶𝜌𝐾

𝑥max +
1
𝑟min
−
1
𝑟max

+ 𝐶· 𝐸(𝑡−1, 𝐾) +
𝜔𝑡−ˆ𝜔𝑡|𝑡−1

𝑟min
,
(32b)
641
```


### Pagina 30
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
where in (32a), we use the facts that
𝑥𝑡= 𝜓𝑡+𝐾−1
𝑡

(𝑥𝑡−1,𝑢𝑡−1); ˆ𝜔𝑡:𝑡+𝐾−1|𝑡−1; ( ¯𝑥,
1
𝜔𝑡+𝐾−1
)

𝑥𝑡
+ (𝜔𝑡−ˆ𝜔𝑡|𝑡−1)𝑢𝑡,
𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑥𝑡= 𝜓𝑁
𝑡

(𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑡+𝐾−1; (𝑥∗
𝑡+𝐾|𝑡,𝑢∗
𝑡+𝐾−1|𝑡)

𝑥𝑡
,
and apply the exponentially decaying perturbation bound. In (32b), we apply the worst-case bound for the first two terms and use the
definition of 𝐸𝑡−1(𝐾).
Note that we can show (32) also holds for 𝑡≥𝑁−𝐾+ 1 with the same approach.
Similarly, we can show that
𝑢𝑡−𝜓𝑁
𝑡((𝑥𝑡−1,𝑢𝑡−1);𝜔𝑡:𝑁; 0)𝑢𝑡
 ≤𝐶′𝜌𝐾

𝑥max +
1
𝑟min
−
1
𝑟max

+ 𝐶′ · 𝐸(𝑡−1, 𝐾).
(33)
Combining (32) and (33) finishes the proof of Lemma A.7.
D.3
Proof of Theorem A.8
We first use induction to show that SODA’s entire trajectory satisfies the buffer level constraints strictly. To see this, note that for 𝑡= 1, we
have
𝑥1 −𝑥∗
1
 ≤𝑒1 ≤𝐶𝜌𝐾

𝑥max +
1
𝑟min
−
1
𝑟max

+ 𝐶· 𝐸(𝑡−1, 𝐾) +
𝜔𝑡−ˆ𝜔𝑡|𝑡−1

𝑟min
≤𝐷
3 .
By Lemma A.6, we know that
𝑥∗
1 −¯𝑥
 ≤𝐷
3 . Thus, we have
|𝑥1 −¯𝑥| ≤
𝑥1 −𝑥∗
1
 +
𝑥∗
1 −¯𝑥
 ≤2𝐷
3 .
Therefore, we see that 0 < 𝑥1 < 𝑥max. Supposing that 0 < 𝑥𝜏< 𝑥max holds for 𝜏= 1, . . . ,𝑡−1, we see that
𝑥𝑡−𝑥∗
𝑡
 +
𝑢𝑡−𝑢∗
𝑡
 ≤𝑒𝑡+ (𝐶+ 𝐶′)
𝑡−1
∑︁
𝜏=1
𝜌𝑡−𝜏𝑒𝜏
(34a)
≤(1 + 𝐶+ 𝐶′)2
1 −𝜌

𝑥max +
1
𝑟min
−
1
𝑟max

· 𝜌𝐾+

1 +
1
𝑟min
+ 𝐶+ 𝐶′
2
𝑡∑︁
𝜏=1
𝜌𝑡−𝜏𝐸(𝜏−1, 𝐾),
(34b)
In (34a), we use (28) in the proof of Lemma A.5. We use Lemma A.7 in (34b).
Thus, we obtain that
𝑥∗
𝑡−𝑥𝑡
 ≤𝐷
3 . By Lemma A.6, we see that
|𝑥𝑡−¯𝑥| ≤
𝑥𝑡−𝑥∗
𝑡
 +
𝑥∗
𝑡−¯𝑥
 ≤2𝐷
3 .
Therefore, we have shown that 0 < 𝑥𝑡< 𝑥max holds for all time steps 𝑡by induction.
By (34), we see that
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2 ≤

1 +
1
𝑟min + 𝐶+ 𝐶′4
1 −𝜌

1 + 𝑥max +
1
𝑟min
−
1
𝑟max

·

1
1 −𝜌

𝑥max +
1
𝑟min
−
1
𝑟max

· 𝜌2𝐾+
𝑡∑︁
𝜏=1
𝜌𝑡−𝜏𝐸(𝜏−1, 𝐾)2
!
.
(35)
Therefore, by summing (35) over 𝑡, we obtain that
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
≤

1 +
1
𝑟min + 𝐶+ 𝐶′4
(1 −𝜌)2

1 + 𝑥max +
1
𝑟min
−
1
𝑟max

·
 
𝑥max +
1
𝑟min
−
1
𝑟max

· 𝑁𝜌2𝐾+
𝑁−1
∑︁
𝑡=0
𝐸(𝑡, 𝐾)2
!
.
(36)
642
```


### Pagina 31
```text
SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
By (31), we see that for any 𝜂> 0, we have
cost(SODA) ≤(1 + 𝜂)cost(OPT) +

1 + 1
𝜂

(4𝛾+ 𝛽+ 𝜔max)
𝑁
∑︁
𝑡=1
𝑥𝑡−𝑥∗
𝑡
2 +
𝑢𝑡−𝑢∗
𝑡
2
≤(1 + 𝜂)cost(OPT) +

1 + 1
𝜂

(4𝛾+ 𝛽+ 𝜔max)·

1 +
1
𝑟min + 𝐶+ 𝐶′4
(1 −𝜌)2

1 + 𝑥max +
1
𝑟min
−
1
𝑟max

·
 
𝑥max +
1
𝑟min
−
1
𝑟max

· 𝑁𝜌2𝐾+
𝑁−1
∑︁
𝑡=0
𝐸(𝑡, 𝐾)2
!
.
Note that 𝑁𝜌2𝐾+ Í𝑁−1
𝑡=0 𝐸(𝑡, 𝐾)2 ≤
1
1−𝜌E. Setting
𝜂=

1 +
1
𝑟min + 𝐶+ 𝐶′2 
1 + 𝑥max +
1
𝑟min −
1
𝑟max

(1 −𝜌)3/2
·
√︁
4𝛾+ 𝛽+ 𝜔max ·
√︄
E
cost(OPT)
finishes the proof.
E
PROOFS FOR EFFICIENT STRUCTURES
E.1
Proof of Lemma A.10
We first consider the case when 𝜈𝑡−1 > 1/ ˆ𝜔. To simplify the notation, we use ˇ𝑢𝑡:𝑡+𝐾−1 to denote the sequence of control actions in
ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0).
We first show that ˇ𝑢𝜏≥1/ ˆ𝜔for all 𝜏∈{𝑡, . . . ,𝑡+ 𝐾−1}. For the sake of contradiction, let ˇ𝑢𝑡1 be the first action such that 𝑢𝑡1−1 ≥1/ ˆ𝜔
and ˇ𝑢𝑡1 < 1/ ˆ𝜔. Note that resetting the sequence ˇ𝑢𝑡1:𝑡+𝐾−1 to 𝑢𝑡1 = 𝑢𝑡1+1 = · · · = 𝑢𝑡+𝐾−1 = 1/ ˆ𝜔will strictly decrease the total cost and the
whole sequence remains feasible. This contradicts with the optimality of ˇ𝑢𝑡:𝑡+𝐾−1. Thus, we have ˇ𝑢𝜏≥1/ ˆ𝜔for all 𝜏∈{𝑡, . . . ,𝑡+ 𝐾−1}.
We next show that ˇ𝑢𝜏≤𝜈𝑡−1 for all 𝜏∈{𝑡, . . . ,𝑡+ 𝐾−1}. To see this, for all 𝑢𝜏such that 𝑢𝜏> 𝜈𝑡−1, we can reset them to 𝑢𝜏= 𝜈𝑡−1 to
decrease the total switching cost strictly without violating any feasibility constraints.
Since ˇ𝑢𝜏∈[1/ ˆ𝜔,𝜈𝑡−1] for all 𝜏∈{𝑡, . . . ,𝑡+𝐾−1}, we know that the buffer level sequence is monotonically increasing. Thus, if ˇ𝑢𝑡:𝑡+𝐾−1 is
not monotonically decreasing, we can permute it to make it monotonically decreasing. This change will strictly decrease the total switching
cost without violating any feasibility constraints. Therefore, we have shown Theorem A.10 holds for the case 𝜈𝑡−1 > 1/ ˆ𝜔.
Using similar techniques, we can show Lemma A.10 also holds for the case 𝜈𝑡−1 < 1/ ˆ𝜔and 𝜈𝑡−1 = 1/ ˆ𝜔.
E.2
Proof of Theorem A.9
We can rewrite the optimization problem (6) as
min
𝑎𝑡:𝑡+𝐾−1
𝑡+𝐾−1
∑︁
𝜏=𝑡
𝛾· 𝑎2
𝑡
s.t. 𝑥𝜏= 𝑥𝜏−1 + ˆ𝜔𝑢𝜏−1, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑢𝜏= 𝑢𝜏−1 + 𝑎𝜏, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑥𝜏∈[0,𝑥max],𝑢𝜏∈

1
𝑟max
,
1
𝑟min

, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑥𝑡−1 = 𝜎𝑡−1,𝑢𝑡−1 = 𝜈𝑡−1.
(37)
We use {( ˇ𝑎𝜏, ˇ𝑢𝜏, ˇ𝑥𝜏)}𝜏=𝑡,...,𝑡+𝐾−1 to denote the optimal solution of (37).
643
```


### Pagina 32
```text
ACM SIGCOMM ’24, August 4–8, 2024, Sydney, NSW, Australia
Chen et al.
Similarly, we can rewrite the optimization problem ˆ𝜓𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0) as
min
𝑎𝑡:𝑡+𝐾−1
𝑡+𝐾−1
∑︁
𝜏=𝑡
𝛾· 𝑎2
𝑡+ ˆ𝜔𝑢2
𝑡+ 𝛽𝑏(𝑥𝑡)
s.t. 𝑥𝜏= 𝑥𝜏−1 + ˆ𝜔𝑢𝜏−1, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑢𝜏= 𝑢𝜏−1 + 𝑎𝜏, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑥𝜏∈[0,𝑥max],𝑢𝜏∈

1
𝑟max
,
1
𝑟min

, for 𝜏= 𝑡, . . . ,𝑡+ 𝐾−1,
𝑥𝑡−1 = 𝜎𝑡−1,𝑢𝑡−1 = 𝜈𝑡−1.
(38)
We use {( ˆ𝑎𝜏, ˆ𝑢𝜏, ˆ𝑥𝜏)}𝜏=𝑡,...,𝑡+𝐾−1 to denote the optimal solution of (38).
For the sake of contradiction, we assume there exists 𝜏∈{𝑡,𝑡+ 1, . . . ,𝑡+ 𝐾−1} such that
 ˆ𝜓𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0)𝑢𝜏−ˆ𝜙𝑡+𝐾−1
𝑡
((𝜎𝑡−1,𝜈𝑡−1); ˆ𝜔; 0)𝑢𝜏
 > 𝜆.
By the strongly convexity of the constrained optimization problem (37), we see that
𝑡+𝐾−1
∑︁
𝜏=𝑡
𝛾ˆ𝑎2
𝑡−
𝑡+𝐾−1
∑︁
𝜏=𝑡
𝛾ˇ𝑎2
𝑡≥𝛾
𝑡+𝐾−1
∑︁
𝜏=𝑡
( ˆ𝑎𝑡−ˇ𝑎𝑡)2 > 𝛾𝜆2
𝐾.
(39)
On the other hand, we have that
𝑡+𝐾−1
∑︁
𝜏=𝑡

ˆ𝜔ˆ𝑢2
𝑡+ 𝛽𝑏( ˆ𝑥𝑡)

−
𝑡+𝐾−1
∑︁
𝜏=𝑡

ˆ𝜔ˇ𝑢2
𝑡+ 𝛽𝑏( ˇ𝑥𝑡)

≥𝐾

ˆ𝜔

1
𝑟2max
−
1
𝑟2
min
!
−𝛽max{¯𝑥2,𝜖(𝑥max −¯𝑥)2}
!
By the optimality of {( ˆ𝑎𝜏, ˆ𝑢𝜏, ˆ𝑥𝜏)}𝜏=𝑡,...,𝑡+𝐾−1 in (38), we see that
0 ≥
𝑡+𝐾−1
∑︁
𝜏=𝑡

ˆ𝜔ˆ𝑢2
𝑡+ 𝛽𝑏( ˆ𝑥𝑡) + 𝛾ˆ𝑎2
𝑡

−
𝑡+𝐾−1
∑︁
𝜏=𝑡

ˆ𝜔ˇ𝑢2
𝑡+ 𝛽𝑏( ˇ𝑥𝑡) + 𝛾ˇ𝑎2
𝑡

> 𝛾𝜆2
𝐾
+ 𝐾

ˆ𝜔

1
𝑟2max
−
1
𝑟2
min
!
−𝛽max{¯𝑥2,𝜖(𝑥max −¯𝑥)2}
!
,
which contradicts our assumption that
𝛾≥𝐾2
𝜆2

ˆ𝜔

1
𝑟2
min
−
1
𝑟2max
!
+ 𝛽max{¯𝑥2,𝜖(𝑥max −¯𝑥)2}
!
.
644
```
