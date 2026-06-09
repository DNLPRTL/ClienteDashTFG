# Oboe: Auto-tuning Video ABR Algorithms to Network Conditions

## 0. Ficha de archivo

- Archivo fuente: `Oboe.pdf`
- Paginas detectadas: 15
- SHA256 PDF: `ef4b6b7f4c4b8a4f8b151a0c57432ba326d046543ea4bec12e249bc03210d82d`
- Texto crudo auxiliar: `raw_text/31_oboe_2018_auto_tuning_abr_network_conditions.txt`
- Texto layout auxiliar: `raw_text_layout/31_oboe_2018_auto_tuning_abr_network_conditions_layout.txt`
- Fecha de generacion: 2026-06-09T12:33:34

## 1. Uso previsto para Fase 4-5 v1

Fuente clave para auto-tuning por regimen de red. Relevante para Fase 4-5 v1 por especializacion, estimacion de estado de red y motivacion de selectors/guardrails segun throughput/variabilidad.

> Nota de fidelidad: este Markdown es una extraccion tecnica densa para Codex. No es un resumen narrativo ni sustituye al PDF. Para formulas, tablas y figuras criticas, revisar siempre el PDF original.

---

## 2. Identificacion textual de primeras paginas

```text
Oboe: Auto-tuning Video ABR Algorithms to
Network Conditions
Zahaib Akhtar*
University of Southern California
Yun Seong Nam*
Purdue University
Ramesh Govindan
University of Southern California
Sanjay Rao
Purdue University
Jessica Chen
University of Windsor
Ethan Katz-Bassett
Columbia University
Bruno Ribeiro
Purdue University
Jibin Zhan
Conviva
Hui Zhang
Conviva
ABSTRACT
Most content providers are interested in providing good video
delivery QoE for all users, not just on average. State-of-the-art
ABR algorithms like BOLA and MPC rely on parameters that
are sensitive to network conditions, so may perform poorly
for some users and/or videos. In this paper, we propose a
technique called Oboe to auto-tune these parameters to dif-
ferent network conditions. Oboe pre-computes, for a given
ABR algorithm, the best possible parameters for different net-
work conditions, then dynamically adapts the parameters at
run-time for the current network conditions. Using testbed ex-
periments, we show that Oboe significantly improves BOLA,
MPC, and a commercially deployed ABR. Oboe also betters
a recently proposed reinforcement learning based ABR, Pen-
sieve, by 24% on average on a composite QoE metric, in part
because it is able to better specialize ABR behavior across
different network states.
CCS CONCEPTS
• Information systems →Information systems applica-
tions; Multimedia streaming;
KEYWORDS
Video delivery, Adaptive bitrate algorithms
ACM Reference Format:
Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay
Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan,
and Hui Zhang. 2018. Oboe: Auto-tuning Video ABR Algorithms to
* Both authors contributed equally to this paper and can be contacted at following:
zakhtar@usc.edu, nam21@purdue.edu
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
© 2018 Association for Computing Machinery.
ACM ISBN 978-1-4503-5567-4/18/08...$15.00
https://doi.org/10.1145/3230543.3230558
Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018
Conference, August 20–25, 2018, Budapest, Hungary. 15 pages.
https://doi.org/10.1145/3230543.3230558
1
INTRODUCTION
Internet video forms a major fraction of Internet traffic to-
day [13], and delivering high quality of experience (QoE) is
critical since it correlates with user engagement and revenue
[6, 23, 31]. To deliver high quality video across diverse net-
work conditions, most Internet video delivery uses adaptive
bitrate (ABR) algorithms [32, 48, 59], combined with HTTP
chunk-based streaming protocols (e.g., Apple’s HTTP Live
Streaming, Adobe’s HTTP Dynamic Streaming). ABR algo-
rithms (a) chop a video into chunks, each of which is encoded
at a range of bitrates (or qualities); and (b) choose which
bitrate level to fetch a chunk at based on conditions such as
the amount of video the client has buffered and the recent
throughput achieved by the client. Within this general frame-
work, ABR algorithms differ in how bitrate level selection
decisions are made, and these decisions impact metrics such
as the average bitrate or the rebuffering ratio. We call these
QoE metrics, because they have been shown to correlate well
with QoE [23], but other perceptual video quality metrics [2]
may also influence QoE.
ABR algorithm design remains an active research area be-
cause content providers continue to be interested in improving
the performance of video delivery. Current ABR algorithms
perform well on average, but some users can experience poor
delivery performance as measured by the QoE metrics. These
users suffer because ABR algorithms have limited dynamic
range: they do not perform uniformly well across the range of
network conditions seen in practice because their parameters
are sensitive to throughput variability (§2).
Contributions. In this paper, we present the design of
Oboe1 (§3), a system that takes the first step towards
overcoming these hurdles. Oboe improves the dynamic range
of ABR algorithms by automatically tuning ABR behavior to
1In orchestras all instruments tune to the Oboe.
44
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
the current network state of a client connection, specifically
to throughput and throughput variability.
Oboe’s design is based on the observation made by prior
work [17, 35, 38, 52, 60] that TCP connections are well-
modeled as traversing a piecewise-stationary sequence of
network states (§3.1): the connection consists of multiple
non-overlapping segments where each segment is in a distinct
stationary network state. For each possible network state,
Oboe pre-computes, offline, the best parameter configuration
for a given ABR algorithm (§3.2). It does this by subjecting
the algorithm, for each state, to different parameter values,
and picking the one that results in the best performance. Then,
during video playback, Oboe continuously uses a change-
point detection algorithm to detect changes in network state
and selects the parameter identified by the offline analysis as
best for the current state. Thus, if a video session encounters
varying network state during its lifetime, Oboe automatically
specializes the ABR parameter to each state (§3.3).
We have implemented Oboe and demonstrated several as-
pects of its performance through testbed experiments and
```

## 3. Metadatos PDF detectados

```json
{
  "format": "PDF 1.7",
  "title": "Oboe: Auto-tuning Video ABR Algorithms to Network Conditions",
  "author": "Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang",
  "subject": "-  Information systems  ->  Information systems applications; Multimedia streaming; ",
  "keywords": "Video delivery, Adaptive bitrate algorithms",
  "creator": "LaTeX with acmart 2018/04/14 v1.53 Typesetting articles for the Association for Computing Machinery and hyperref 2012/11/06 v6.83m Hypertext links for LaTeX",
  "producer": "pdfTeX-1.40.16; modified using iText® 5.5.9 ©2000-2015 iText Group NV (AGPL-version)",
  "creationDate": "D:20180622124728-04'00'",
  "modDate": "D:20180803093515-04'00'",
  "trapped": "",
  "encryption": null
}
```

## 4. Mapa de secciones detectado

- p. 1: CCS CONCEPTS
- p. 1: INTRODUCTION
- p. 2: BACKGROUND AND MOTIVATION
- p. 4: OBOE DESIGN
- p. 6: EVALUATION
- p. 12: DEPLOYMENT CONSIDERATIONS
- p. 13: DISCUSSION AND FUTURE WORK
- p. 13: RELATED WORK
- p. 13: CONCLUSION
- p. 14: BIBLIOGRAPHY

## 5. Figuras, tablas, algoritmos, ecuaciones o teoremas detectados

- p. 3: Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors
- p. 3: Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces
- p. 3: Figure 1(b) shows that BOLA behaves similarly, with Mod
- p. 4: Figure 3—The logical diagram of the offline pipeline used by Oboe
- p. 6: Figure 4—Logical diagram of Oboe’s online pipeline
- p. 6: algorithm is ready to compute the bitrate decision to be used
- p. 7: Figure 5—A scatter plot of average bitrate and rebuffering ratio between the Virtu-
- p. 8: Figure 6—The percentage improvement in QoE-lin of MPC+Oboe over RobustMPC for the Testbed experiment. The distribution of average bitrate, rebuffering ratio and bitrate
- p. 8: Figure 7—QoE-lin of MPC+Oboe compared to RobustMPC
- p. 8: Figure 6(a) shows the CDF of the percentage improvement
- p. 8: Figure 8—An example session showing how MPC+Oboe is able to outperform Ro-
- p. 8: Figure 8 illustrates, using a single session, why MPC+Oboe
- p. 9: Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and
- p. 9: Figure 10—Validation of our training
- p. 9: Figure 11—QoE-lin of MPC+Oboe
- p. 10: Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d)
- p. 10: Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors
- p. 10: Figure 13 shows CDFs of per-session QoE-lin improve-
- p. 11: Figure 16—Comparing HYB with multiple fixed configurations and HYB+Oboe for various settings
- p. 11: Figure 15 shows the average QoE-lin across the traces
- p. 11: Figure 16(a) and 16(b) compare HYB, HYB+Oboe and
- p. 12: Figure 17—Avg. of avg. bitrate and
- p. 12: Figure 18—Avg. of avg. bitrate and
- p. 12: Figure 19—Comparing prototype Oboe with commercial client side ABR implemen-
- p. 12: Figure 20—Time between consecutive
- p. 12: Figure 21—Variance in bitrate levels

## 6. Lineas con posible contenido matematico/formal

Estas lineas NO son LaTeX verificado. Sirven para localizar formulas, objetivos, restricciones o pseudocodigo que hay que verificar en PDF.

- p. 5: `formance vector 𝑉𝑖=< 𝑣1, 𝑣2, . . . 𝑣𝑚> where each 𝑣𝑘cor-`
- p. 7: `𝑀may be defined as 𝑀= ∑︀𝑁−1`
- p. 7: `QoE-lin(𝑝, 𝑐) = 1`
- p. 7: `that had a maximum bitrate of 4.3 Mbps, we use 𝑝= 4.3 and`
- p. 7: `𝑐= 1 as our default parameters (following previous work that`
- p. 8: `𝑦= 𝑥line indicating close correlation. Given these close`
- p. 10: `implemented in Dash.js, uses a fixed default value of 𝛾=`
- p. 10: `uses 𝛽= 0.25, determined using A/B tests in a large-scale de-`

## 7. Extraccion tecnica por categorias


### 7.1. modelo ia arquitectura algoritmo

Palabras clave usadas: `model, models, neural, architecture, algorithm, policy, agent, actor, critic, actor-critic, DQN, deep Q, Q-learning, PPO, proximal policy, A3C, reinforcement, DRL, deep reinforcement, meta reinforcement, meta-RL, meta learning, MAML, Mamba, state space, SSM, LSTM, policy network, prediction model, Pensieve, SODA, DQNReg, MetaABR, MERINA, Oboe`

**Fragmento 1 - p. 10 - score 6:**

Pens-SelOnce starts with the 0-6 Mbps model, selects either the 0-3 Mbps or 3-6 Mbps model based on the average throughput of the first 5 initial chunks, and does not switch thereafter. Figure 13 shows CDFs of per-session QoE-lin improve- ment of MPC+Oboe over these selectors. MPC+Oboe is able to outperform both Pens-SelMultile and Pens-SelOnce, with average QoE-lin improvements of 14.2% and 24.32% re- spectively. Even though one of the model selection schemes offers some improvements over the 0-6 Mbps Pensieve model, the benefits are modest. We hypothesize that this behavior is due to the dynamic selection of distinct Pensieve models, which can interfere with reinforcement learning’s decision choices, since, during training, the reinforcement learning algorithm assumes there is no such third party intervention.

**Fragmento 2 - p. 2 - score 5:**

We have tried training specialized Pensieve models for different ranges of network throughputs and dynamically switching models based on estimated session throughput. This helps, but a sig- nificant gap between the two approaches still remains (§4.4). While a variety of viable pathways exist to deploying Oboe, we focus on an architecture where Oboe and the entire ABR logic are deployed on the cloud which enables rapid evolution and fine-grain customizability. We show the viability of this architecture with results from a pilot deployment. 2 BACKGROUND AND MOTIVATION The Internet video delivery ecosystem consists of hundreds of content publishers and hundreds of client side applications that stream video content to diverse user devices.

**Fragmento 3 - p. 8 - score 5:**

This results in a rebuffering event 44 seconds into the session (lowest graph shows buffer occupancy with 0 indicating a rebuffering event). In contrast, MPC+Oboe does not incur a rebuffering event and maintains a fixed 𝑑during the initial stable state. At 29 sec, it detects a change in the network state and adapts its discount factor, leading to more conservative bitrate selections. 4.4 Oboe vs. Pensieve Pensieve [39] uses deep reinforcement learning [41, 42], a combination of deep learning with reinforcement learn- ing [50], and has been shown to outperform existing ABRs, including RobustMPC [39] in some settings. Since 51

**Fragmento 4 - p. 9 - score 5:**

Our exper- iments use the Pensieve implementation provided by the authors [11]. Pensieve Re-Training and Validation. Before evaluating Pensieve on our dataset, we retrain Pensieve using the source code on the trace dataset provided by the Pensieve authors [11]. This helps us validate our retraining given that deep reinforcement learning results are not easy to reproduce [29]. We experimented with five different initial entropy weights in the author suggested range of 1 to 5, and linearly reduced their values in a gradual fashion using plateaus, with five different decrease rates until the entropy weight eventually reached 0.1. This rate scheduler follows best-practice [55]. From the trained set of models, we then selected the best performing model (an initial entropy weight of 1 reduced every 800 iterations until it reaches 0.1 over 100K iterations) and compared its performance to the pre-trained Pensieve model provided by the authors.

**Fragmento 5 - p. 13 - score 5:**

It is unclear if Oboe can directly augment Pensieve, since a model learned by reinforcement learning may not interact well with intermediaries such as Oboe. However, combining the benefits of Oboe and Pensieve in other ways is an interesting avenue for future work. 7 RELATED WORK Tuning ABR Algorithm Configurations. The BBA2 algo- rithm [32] tunes its lower reservoir based on buffer occupancy dynamics, while MPC [59] adapts its throughput discount fac- tor based on past prediction errors (§2). In contrast to such ad- hoc heuristics, Oboe selects configuration parameters based on network state, and publisher specifications. The approach is generically applicable to many ABR algorithms. Newer congestion control protocols like BBR [19] estimate network throughput, which if exposed, could benefit Oboe.

**Fragmento 6 - p. 14 - score 5:**

In IEEE International Conference on Distributed Computing Systems, ICDCS, 2005. [39] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. Neural Adaptive Video Streaming with Pensieve. In Proceedings of the ACM Conference on Special Interest Group on Data Communication, SIGCOMM, 2017. [40] Virginia Martín, Julián Cabrera, and Narciso García. Design, Optimization and Evaluation of a Q-learning HTTP Adaptive Streaming Client. IEEE Transactions on Consumer Electronics, 62(4):380–388, 2016. [41] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Ve- ness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidje- land, Georg Ostrovski, et al. Human-level Control Through Deep Reinforcement Learning.

**Fragmento 7 - p. 3 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces throughput prediction errors, a more conservative version, Ro- bustMPC, reduces predicted throughput by a discount factor 1+𝑑, where 𝑑is the maximum error in throughput predictions experienced in the last five chunk downloads. BOLA: Buffer occupancy, selects bitrate by solving an optimization problem. BOLA is a buffer-based algorithm used in Dash.js [7], so it does not employ throughput pre- diction in making bitrate decisions [48].

**Fragmento 8 - p. 6 - score 4:**

Given these sources of uncertainty, Oboe chooses to be safe in its selec- tion of the best configuration for 𝑠. Finally, ReconfEngine configures the ABR algorithm, and the reconfigured ABR algorithm is ready to compute the bitrate decision to be used for the next chunk at this point. 4 EVALUATION In this section, we demonstrate Oboe’s ability to auto-tune three existing algorithms: RobustMPC, BOLA and HYB. We also compare an Oboe-tuned RobustMPC to Pensieve [39]. 4.1 Metrics The performance of a video session depends on multiple fac- tors. Average bitrate and rebuffering ratio were found to have the most impact on user quality of experience [23], though other factors such as changes in bitrates during a session can play a role [23].

**Fragmento 9 - p. 9 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 10—Validation of our training methodology for Pensieve. Figure 11—QoE-lin of MPC+Oboe compared to Pensieve Figure 12—Benefits of specializing Pensieve models. Each curve shows the QoE improvement of MPC+Oboe rela- tive to each Pensieve model. Figure 13—QoE improvement of MPC+Oboe over two ways of dy- namically selecting from specialized Pensieve models. MPC+Oboe outperforms RobustMPC as well, we explore how MPC+Oboe performs relative to Pensieve.

**Fragmento 10 - p. 9 - score 4:**

Figure 10 shows CDFs of QoE-lin for the pretrained (Original) model and the model trained by us (Retrained). The performance distribution of the two models are almost identical over the test traces provided by the Pensieve authors, thereby validating our retraining methodology. Having validated our retraining methodology, we trained Pensieve on our dataset with the same complete strategy described above. For this, we pick 1600 traces randomly from our dataset with average throughput in the 0-6 Mbps range. The number of training traces, the number of iterations per trace, and the range of throughput are similar to [39]. We then compare Pensieve and MPC+Oboe over a separate test set of traces also in the range of 0-6 Mbps (§4.2).

**Fragmento 11 - p. 9 - score 4:**

Figure 12 shows the per session QoE-lin improvement of MPC+Oboe com- pared to Pensieve models trained for 0-3 Mbps (which we refer to as Pens-Specialized) and for 0-6 Mbps. The me- dian QoE-lin improvement with MPC+Oboe over Pens- Specialized is 10.49%, while the median improvement over 52

**Fragmento 12 - p. 10 - score 4:**

It is hard to pinpoint exactly why Pensieve is unable to learn to be more conservative in the 0-3 Mbps range; deep neural network models remain a black box despite efforts by the machine learning community to make these models more transparent [45], and obtaining such understanding may need further advances in interpretable deep learning models. A model selector with Pensieve . One way to improve Pen- sieve’s specialization might be to train different models for different throughput ranges and use the model more suited to the network conditions. To test the efficacy of this ap- proach, we used two models (specialized for 0-3 Mbps and 3-6 Mbps), and tried two different model selectors. Pens- SelMultiple switches models throughout the session, using the average throughput of the past 5 chunks.

**Fragmento 13 - p. 13 - score 4:**

Learning ABR Algorithms. Among ABR algorithms that use Reinforcement Learning and other machine learning tech- niques [20, 21, 39, 40, 53], Pensieve [39] has been shown to perform the best. While Pensieve does not specialize to differ- ent throughput regimes, Oboe performs better by specializing parameter values for each network state independently. Other work in self-tuning. Beyond ABR algorithms, self- tuning approaches have been explored in other contexts. Win- stein et al. [56] used simulations to determine TCP parameters for different settings, while Semke et al. [47] proposed tuning TCP socket buffers to ensure high throughput. More gener- ally, Google Vizier [28] performs such black-box tuning as a service.

**Fragmento 14 - p. 1 - score 3:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 15 - p. 2 - score 3:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the current network state of a client connection, specifically to throughput and throughput variability. Oboe’s design is based on the observation made by prior work [17, 35, 38, 52, 60] that TCP connections are well- modeled as traversing a piecewise-stationary sequence of network states (§3.1): the connection consists of multiple non-overlapping segments where each segment is in a distinct stationary network state. For each possible network state, Oboe pre-computes, offline, the best parameter configuration for a given ABR algorithm (§3.2). It does this by subjecting the algorithm, for each state, to different parameter values, and picking the one that results in the best performance.

**Fragmento 16 - p. 2 - score 3:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 17 - p. 3 - score 3:**

It also models bitrate selection as an optimization problem which it solves for a given value of the buffer. It uses a parameter 𝛾which is a ratio of (i) a minimum buffer threshold, below which it downloads the lowest bitrate and (ii) a target buffer threshold which it tries to maintain. Conceptually 𝛾controls how strongly the ABR should avoid rebuffering [48]. Higher values of 𝛾make the algorithm conservative. HYB: Throughput prediction without lookahead. Selects bitrate using a simple heuristic. An algorithm widely used in production (§5), HYB considers both the predicted throughput and current buffer occupancy (HYB is short for hybrid). For each chunk, HYB picks the highest bitrate that can avoid rebuffering.

**Fragmento 18 - p. 4 - score 3:**

process. Motivated by these observations, Oboe defines network state 𝑠by a tuple < 𝜇𝑠, 𝜎𝑠>, where 𝜇𝑠is the mean and 𝜎𝑠 the standard deviation of the client-perceived throughput in a (stationary) segment of the underlying TCP connection. 3.2 Offline Mapping of Network States To map network states to their optimal ABR configurations, Oboe uses a pipeline (Figure 3) consisting of three compo- nents – the ConfigEvaluator, the VirtualPlayer and the Con- figSelector. The ConfigEvaluator takes a stationary through- put trace as input, which represents a particular network state, and drives the exploration of different ABR configurations over this trace. It does so by using the VirtualPlayer which models the dynamics of an actual video player.

**Fragmento 19 - p. 6 - score 3:**

An alternative approach to changing configurations is to use an exponentially weighted moving average (EWMA) of the mean and standard deviation of throughput samples and to lookup the corresponding configuration. We experimented with such an approach and found its performance unsatisfac- tory. The approach can result in continual and unnecessary reconfigurations, since throughput may vary across samples even when the network is (statistically) stationary. Damping these changes can result in slow reaction times when a recon- figuration is actually beneficial. In contrast, Oboe (i) models the underlying TCP connection as a sequence of states; (ii) does not make changes to the configuration within a given network state; and (iii) only reconfigures when a state change is observed.

**Fragmento 20 - p. 7 - score 3:**

The underlying factors represent concrete application performance that publishers understand how to reason about. Moreover, a unified metric like QoE-lin can obscure important differences. For example, two sessions may have the same QoE-lin but different performance in underlying metrics, leading to varied user experience. So, we also present graphs of these metrics. 4.2 Methodology Implementation. For RobustMPC, we used the imple- mentation available at [11]. Our implementation of BOLA [@bola] is from the Dash.js player. The implementation of HYB is a variant of the algorithm used in a large-scale deployment. These ABR algorithms and Oboe’s online stage (change point detection and ABR reconfiguration) run on the server in our experiments.

**Fragmento 21 - p. 9 - score 3:**

Finally, Figure 11 shows the CDF of QoE-lin for MPC+Oboe and Pensieve, and indicates MPC+Oboe per- forms distributionally better. Analyzing Pensieve performance. To understand where these performance improvements were coming from, we ex- amined the relative performance of these two schemes in the 0-3 Mbps range (i.e., traces having an average throughput be- tween 0-3 Mbps). In this more constrained range of network conditions, we found that MPC+Oboe achieves bigger gains over Pensieve (average QoE-lin improvement in 0-3 Mbps is 46.23%). We hypothesize that this performance difference stems from the fact that Pensieve builds a single model which does not specialize to different throughput ranges. To test this, we trained a separate Pensieve model only with traces that have an average throughput between 0-3 Mbps range and compared it with MPC+Oboe.

**Fragmento 22 - p. 10 - score 3:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d) Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors Pensieve is 19.9%. This indicates specializing the model does improve Pensieve’s performance. Thus, Pensieve’s model is as yet unable to create special- ized versions of itself based on the session characteristics. By contrast, Oboe specializes parameters for every network state and therefore performs better. We have also validated Pensieve’s inability to specialize in several other ways: build- ing a model for the 3-6 Mbps and showing that it performs better with test data in that range compared to a 0-6 Mbps model; checking that a 0-6 Mbps model performs better for data in that range compared to a 0-100 Mbps model; and ensuring that these results hold even when the training set is doubled.

**Fragmento 23 - p. 10 - score 3:**

FCC is a broadband dataset, while HSDPA contains throughput traces collected from video streaming sessions over 3G net- works in Norway using mobile devices. Our comparisons use the traces and a Pensieve model pre-trained for those traces available at [11]. We focus our evaluations on MPC+Oboe and Pensieve, given that Pensieve has been shown to out- perform existing ABR schemes including RobustMPC on 53

**Fragmento 24 - p. 13 - score 3:**

Picking configurations in a manner informed by network state and publisher preferences distin- guishes Oboe’s approach from heuristics used today that do not consider these factors. Oboe significantly improves the performance of BOLA, HYB and RobustMPC; further, for nearly 80% of the sessions in our dataset, Oboe integrated with RobustMPC improves QoE-lin relative to Pensieve and the improvements exceed 20% for 25% of the sessions. Acknowledgments. We thank our shepherd, Mohammad Al- izadeh and the anonymous reviewers for their constructive feedback. We thank Oleg White, Yan Li and Shubo Liu for their assistance obtaining the throughput data and for helpful discussions. This work was funded in part by the National Science Foundation (NSF) Awards CNS-1618921, CNS-1564242, and CNS-1413978; and the ARO, under the U.S.

**Fragmento 25 - p. 15 - score 3:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary [53] Jeroen van der Hooft, Stefano Petrangeli, Maxim Claeys, Jeroen Famaey, and Filip De Turck. A Learning-based Algorithm for Improved Bandwidth-awareness of Adaptive Streaming Clients. In Symposium on Integrated Network Manage- ment, IM, 2015. [54] Li Wei and Eamonn Keogh. Semi-supervised Time Series Classification. In Proceedings of the ACM International Conference on Knowledge Discovery and Data Mining, SIGKDD, 2006. [55] Ronald J Williams and Jing Peng. Function Optimization using Connectionist Reinforcement Learning Algorithms. Connection Science, 3(3):241–268, 1991. [56] Keith Winstein and Hari Balakrishnan. TCP Ex Machina: Computer-generated Congestion Control.

**Fragmento 26 - p. 1 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary © 2018 Association for Computing Machinery. ACM ISBN 978-1-4503-5567-4/18/08...$15.00 https://doi.org/10.1145/3230543.3230558 Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018 Conference, August 20–25, 2018, Budapest, Hungary. 15 pages. https://doi.org/10.1145/3230543.3230558 1 INTRODUCTION Internet video forms a major fraction of Internet traffic to- day [13], and delivering high quality of experience (QoE) is critical since it correlates with user engagement and revenue [6, 23, 31]. To deliver high quality video across diverse net- work conditions, most Internet video delivery uses adaptive bitrate (ABR) algorithms [32, 48, 59], combined with HTTP chunk-based streaming protocols (e.g., Apple’s HTTP Live Streaming, Adobe’s HTTP Dynamic Streaming).


### 7.2. estado inputs features observaciones

Palabras clave usadas: `state, states, input, inputs, feature, features, observation, observations, throughput, bandwidth, buffer, download time, download duration, chunk size, segment size, history, past, remaining, last bitrate, network condition, QoE objective, task, environment, session, forecast, prediction, representation`

**Fragmento 1 - p. 2 - score 6:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 2 - p. 4 - score 6:**

process. Motivated by these observations, Oboe defines network state 𝑠by a tuple < 𝜇𝑠, 𝜎𝑠>, where 𝜇𝑠is the mean and 𝜎𝑠 the standard deviation of the client-perceived throughput in a (stationary) segment of the underlying TCP connection. 3.2 Offline Mapping of Network States To map network states to their optimal ABR configurations, Oboe uses a pipeline (Figure 3) consisting of three compo- nents – the ConfigEvaluator, the VirtualPlayer and the Con- figSelector. The ConfigEvaluator takes a stationary through- put trace as input, which represents a particular network state, and drives the exploration of different ABR configurations over this trace. It does so by using the VirtualPlayer which models the dynamics of an actual video player.

**Fragmento 3 - p. 7 - score 6:**

All our testbed experiments use a client buffer of 2 minutes. Datasets. We use throughput traces from real user sessions collected over a three month period. Each trace contains the in- dividual chunk sizes and their download times for on-demand video sessions from a publisher that serves short (4-6 minute) music videos. We derive throughput by dividing the chunk sizes by their download durations. The traces contain sessions that used desktops with wired connections and also sessions on mobile devices using WiFi or cellular connections. Like previous work [39, 59], we primarily focus on traces that have less than 6 Mbps average throughput, since this is the regime where bitrate switching decisions are likely to have QoE impact.

**Fragmento 4 - p. 12 - score 6:**

In our implementation, a client player periodically reports player state (such as buffer length and current bitrate) and throughput samples to a Oboe cloud server and receives bitrate decisions in return. For 10 player features and two chunk downloads per second, the commu- nication overhead is 6.4 Kbps, negligibly small compared to the size of video chunks. Figures 19(a) and 19(b) compare the performance of this implementation against a client player running HYB over 20K sessions collected during a two-week pilot deployment. Oboe is comparable in performance to the client side player and even improves bitrate slightly (because it was tuned to this publisher’s specification). 55

**Fragmento 5 - p. 3 - score 5:**

Specifically, if 𝑆𝑗(𝑖) denotes the size of chunk 𝑗 encoded at bitrate 𝑖, 𝐵is the predicted throughput based on past samples, and 𝐿the length of the buffer. HYB picks the largest bitrate 𝑖such that 𝑆𝑗(𝑖) 𝐵 < 𝐿× 𝛽. Here, 𝛽can have values between 0 and 1 (higher values represent aggressive ABR behavior). 𝛽can be tuned to offset prediction errors in throughput and to compensate for the greedy nature of the approach which may make it susceptible to future buffering events owing to unexpected throughput dips. 2.2 Ensuring High QoE for All Users Despite widespread deployment, ABR algorithms continue to be an active area of research [32, 34, 39, 48, 51, 59]. This is because, while deployed ABR algorithms work well on average, they do not work uniformly well across all network conditions.

**Fragmento 6 - p. 6 - score 5:**

We focus on online methods, since Oboe identifies change points for an in-progress session and dynam- ically changes configurations. While several techniques exist for change point detection [22, 33, 36, 44, 54, 58], we focus on probabilistic methods [14, 18, 24, 57]. Further, we use a Bayesian online proba- bilistic change-point detector [14] for two reasons. First, in [14], a sequence of observations can be partitioned into non- overlapping states such that the observations are i.i.d. condi- tioned on a given network state 𝑠. This view aligns well with the way we have defined a network state (§3.1). Further, the al- gorithm is fast and requires no prior knowledge about the data stream, matching our scenario.

**Fragmento 7 - p. 7 - score 5:**

Our client runs the Dash.js video player (version 1.2), a reference player implemented in JavaScript by the MPEG-DASH forum [7]. We modified Dash.js to send client player state information (e.g. buffer length, video play state and throughput measurements) to Oboe (§5). This player runs on the Google Chrome browser (version 61) in our experiments. In §5, we show that Oboe can also be run as a cloud service. Testbed setup. Our evaluations measure ABR performance by delivering a video stream (the “EnvivioDash3” video from the MPEG-DASH reference videos [12]) from a video host- ing server to a client, while varying network conditions us- ing throughput traces from real user sessions. We use bi- trates {300, 750, 1200, 1850, 2850, 4300}𝑘𝑏𝑝𝑠with a 4 sec- ond chunk duration and total length of 192 seconds.

**Fragmento 8 - p. 12 - score 5:**

In contrast, Figure 18 shows that RobustMPC is less effective at controlling rebuffering by adjusting its rebuffering penalty when the weight on the rebuffering term is varied between 100 (strictly avoid rebuffering) to 4.3.5 We find that even with a very high rebuffering penalty of 100, RobustMPC causes rebuffering in 11% of the sessions. This shows the benefit of Oboe’s approach which gives direct control over the underly- ing metrics. 4.8 Oboe Overhead Computing the ConfigMap incurs a one-time cost, since the map can be reused across all clients once the it is built. Com- puting the best parameter configuration for one network state takes about 12 seconds on a single core. This task is perfectly parallelizable, so computing 10K network states (§3) will take approximately 3.5 hours to explore with two machines of 48 cores each.

**Fragmento 9 - p. 13 - score 5:**

It is unclear if Oboe can directly augment Pensieve, since a model learned by reinforcement learning may not interact well with intermediaries such as Oboe. However, combining the benefits of Oboe and Pensieve in other ways is an interesting avenue for future work. 7 RELATED WORK Tuning ABR Algorithm Configurations. The BBA2 algo- rithm [32] tunes its lower reservoir based on buffer occupancy dynamics, while MPC [59] adapts its throughput discount fac- tor based on past prediction errors (§2). In contrast to such ad- hoc heuristics, Oboe selects configuration parameters based on network state, and publisher specifications. The approach is generically applicable to many ABR algorithms. Newer congestion control protocols like BBR [19] estimate network throughput, which if exposed, could benefit Oboe.

**Fragmento 10 - p. 2 - score 4:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 11 - p. 2 - score 4:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the current network state of a client connection, specifically to throughput and throughput variability. Oboe’s design is based on the observation made by prior work [17, 35, 38, 52, 60] that TCP connections are well- modeled as traversing a piecewise-stationary sequence of network states (§3.1): the connection consists of multiple non-overlapping segments where each segment is in a distinct stationary network state. For each possible network state, Oboe pre-computes, offline, the best parameter configuration for a given ABR algorithm (§3.2). It does this by subjecting the algorithm, for each state, to different parameter values, and picking the one that results in the best performance.

**Fragmento 12 - p. 3 - score 4:**

Figures 1(a) and 1(b) show how the choice of ABR config- uration depends on network conditions. Figure 1(a) shows the bitrate and rebuffering ratio for two client sessions with the HYB algorithm for three different values of its 𝛽parameter, Cons (Conservative), Mod (Moderate), and Aggr (Aggres- sive). The throughput behavior of the two sessions is shown in Figure 1(c). If a publisher prefers to eliminate rebuffering, Mod is suitable for session A, but Cons is better for session B. Figure 1(b) shows that BOLA behaves similarly, with Mod being the preferred setting for session A and Cons for session B, to avoid rebuffering. Figures 2(a) and 2(b) show the difficulty in setting the discount factor with MPC, by comparing the performance of FastMPC (no discount factor), and RobustMPC (discount factor set by local heuristic) for two throughput traces with different characteristics.

**Fragmento 13 - p. 3 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces throughput prediction errors, a more conservative version, Ro- bustMPC, reduces predicted throughput by a discount factor 1+𝑑, where 𝑑is the maximum error in throughput predictions experienced in the last five chunk downloads. BOLA: Buffer occupancy, selects bitrate by solving an optimization problem. BOLA is a buffer-based algorithm used in Dash.js [7], so it does not employ throughput pre- diction in making bitrate decisions [48].

**Fragmento 14 - p. 4 - score 4:**

3 OBOE DESIGN Oboe aims to ensure good QoE for all users by enabling ABR algorithms to perform better across a wide range of network conditions. The configurations of many ABR algorithms are sensitive to network state, specifically to the value and vari- ability of the available throughput between the client and the video server. For example, 𝛽in HYB should be smaller when available throughput is highly variable, while 𝛾in BOLA should be higher. This explains why the algorithms perform differently for different values of parameters on a given client trace (§2.2). However, a line of prior work [17, 35, 38, 52, 60] has observed that network connections are piecewise station- ary: that is, connections can be in one of several distinct states (§3.1), where each state is distinguished by stationarity in the statistical sense (informally, a process is stationary if its sta- tistical properties including mean and variance do not change over time - see [43] for a more formal definition).

**Fragmento 15 - p. 4 - score 4:**

Oboe leverages the piecewise stationarity of network con- nections to address the key challenge of sensitivity of config- urations to network conditions. It does so using a two stage design: (a) an offline stage where it pre-computes the best con- figuration choice for each (stationary) network state (§3.2), and (b) and an online stage, where during a session, it de- tects changes in network state and applies the pre-computed best configuration for the current (stationary) state (§3.3). Oboe can also accommodate publisher specifications such as session type (live vs. video-on-demand, time-to-live re- quirements), bitrate levels or any explicit QoE tradeoffs (e.g., preference between rebuffering and average bitrate) (§3.2), by using these to influence the selection of the best configuration for each (stationary) network state in the offline stage.

**Fragmento 16 - p. 5 - score 4:**

For each state, we generate a synthetic stationary trace. We found that the benefits of finer quantization are marginal. Estimating ABR performance with VirtualPlayer and publisher specifications. Oboe uses VirtualPlayer, a trace- based simulator that mimics the behavior of an actual video player without downloading or rendering actual videos. It takes as input a throughput trace and outputs the QoE performance metrics of a video session for a specified ABR algorithm. We have validated VirtualPlayer in §4.7. In designing VirtualPlayer, we have decoupled ABR logic (Figure 3), so the same implementation of the ABR logic can be used in Oboe’s offline and online stage. Further, this design provides an interface to the ABR designer through which they can easily integrate their ABR algorithm with Oboe without having to know about Oboe’s internals.

**Fragmento 17 - p. 6 - score 4:**

We use the implementation provided in [10] and integrate it with the ChangeDetector. Detecting changes in network state. During a video ses- sion, ChangeDetector is continually fed with a series of obser- vations of the network throughput, which it uses to detect state changes. ChangeDetector calculates throughput and standard deviation by only considering those samples which belong to the current state. To generate inputs to ChangeDetector, one approach is to use each downloaded chunk to obtain a single throughput sample. However, this may be too coarse- grained, and prevent detection of changes in network state that occur during the chunk download. Instead, we use fine grained samples recorded at periodic intervals (tens of mil- liseconds) during the download of each chunk.

**Fragmento 18 - p. 8 - score 4:**

median per chunk change magnitude by 38% (Figure 6(d)). Fi- nally, Figure 7 shows the CDF of QoE-lin for MPC+Oboe and RobustMPC, and indicates MPC+Oboe distributionally performs better. Figure 8 illustrates, using a single session, why MPC+Oboe performs better than RobustMPC. The top graph shows throughput as a function of time, which includes an initial stable state followed by a drop in throughput. The middle graph shows how the discount factor 𝑑of both RobustMPC, and MPC+Oboe vary (the predicted throughput for each system is reduced by a factor of 1 1+𝑑, where 𝑑is shown on the y-axis). During the initial stable state, when prediction errors are low, RobustMPC steadily lowers its discount factor leading to more aggressive bitrate selections (not shown).

**Fragmento 19 - p. 8 - score 4:**

Given these close correlations, we use the VirtualPlayer in §4.7 to explore Oboe’s performance over a larger range of diverse settings and our entire set of traces. 4.3 Oboe with RobustMPC We now demonstrate that Oboe can be used to auto-tune Ro- bustMPC, the best performing variant of the MPC algorithms. The resulting MPC+Oboe uses the best value of the discount parameter 𝑑corresponding to the current network state, re- placing RobustMPC’s online adaptation based on throughput estimates obtained over the past 5 chunks (§2). Figure 6(a) shows the CDF of the percentage improvement in QoE-lin of MPC+Oboe over RobustMPC.4 MPC+Oboe improves QoE-lin for 71% of sessions, with an overall av- erage QoE-lin improvement of 17.62% across all sessions.

**Fragmento 20 - p. 10 - score 4:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d) Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors Pensieve is 19.9%. This indicates specializing the model does improve Pensieve’s performance. Thus, Pensieve’s model is as yet unable to create special- ized versions of itself based on the session characteristics. By contrast, Oboe specializes parameters for every network state and therefore performs better. We have also validated Pensieve’s inability to specialize in several other ways: build- ing a model for the 3-6 Mbps and showing that it performs better with test data in that range compared to a 0-6 Mbps model; checking that a 0-6 Mbps model performs better for data in that range compared to a 0-100 Mbps model; and ensuring that these results hold even when the training set is doubled.

**Fragmento 21 - p. 10 - score 4:**

It is hard to pinpoint exactly why Pensieve is unable to learn to be more conservative in the 0-3 Mbps range; deep neural network models remain a black box despite efforts by the machine learning community to make these models more transparent [45], and obtaining such understanding may need further advances in interpretable deep learning models. A model selector with Pensieve . One way to improve Pen- sieve’s specialization might be to train different models for different throughput ranges and use the model more suited to the network conditions. To test the efficacy of this ap- proach, we used two models (specialized for 0-3 Mbps and 3-6 Mbps), and tried two different model selectors. Pens- SelMultiple switches models throughout the session, using the average throughput of the past 5 chunks.

**Fragmento 22 - p. 13 - score 4:**

While Vizier can potentially be used to implement the offline phase of Oboe, our work identifies underlying principles (such as the piecewise stationarity of available throughput) that forms the basis for the tuning. Video QoE. Several researchers have pointed out that sub-optimal ABR performance can significantly impact user-engagement and hence revenue [16, 37]. Others have looked at quality issues that occur when multiple players start to compete for bandwidth [15, 30, 31, 34] In contrast, Oboe improves the QoE performance of several ABR algorithms across a range of different network conditions by automatically tuning their parameters. 8 CONCLUSION Oboe is a system for automatically tuning ABR algorithms by adapting ABR configurations in realtime to match the current network state.

**Fragmento 23 - p. 1 - score 3:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 24 - p. 2 - score 3:**

2.1 Background on ABR Algorithms ABR algorithms fall in two broad categories: (i) those that use both prediction of network throughput and buffer occu- pancy [34, 51, 59]; and (ii) those that are primarily based on buffer occupancy [32, 48]. Within the above two categories, ABR algorithms can be designed using approaches ranging from heuristics to stochastic optimization. In §4, we discuss a recently proposed ABR algorithm based on a qualitatively different approach, reinforcement learning [39]. MPC: Throughput prediction and buffer occupancy with look-ahead. Selects bitrate by solving an optimization prob- lem. MPC [59] predicts throughput of future chunk down- loads based on throughput samples of recently downloaded chunks, then uses this predicted throughput to select bitrates to optimize a given QoE function (§4) over a look-ahead window of 5 future chunks.

**Fragmento 25 - p. 2 - score 3:**

They may also serve streams of different qualities ranging from HD (high definition) to SD (standard definition). These differ- ences impact how they serve videos. For example, publishers who serve VoD content can use player buffers as large as 4 minutes [32], whereas publishers serving live content may have a time-to-live2 requirement between 15-45 seconds. Sim- ilarly, based on the quality of streams they serve, publishers may use different bitrate levels or chunk sizes. Further, pub- lishers may have different QoE objectives. For example, some may strictly prefer to minimize rebuffering and others may relax their tolerance for rebuffering to prioritize higher bi- trates. We use the term publisher specifications to denote their choice of bitrate levels, chunk sizes, content type, and rebuffering tolerance.

**Fragmento 26 - p. 3 - score 3:**

It also models bitrate selection as an optimization problem which it solves for a given value of the buffer. It uses a parameter 𝛾which is a ratio of (i) a minimum buffer threshold, below which it downloads the lowest bitrate and (ii) a target buffer threshold which it tries to maintain. Conceptually 𝛾controls how strongly the ABR should avoid rebuffering [48]. Higher values of 𝛾make the algorithm conservative. HYB: Throughput prediction without lookahead. Selects bitrate using a simple heuristic. An algorithm widely used in production (§5), HYB considers both the predicted throughput and current buffer occupancy (HYB is short for hybrid). For each chunk, HYB picks the highest bitrate that can avoid rebuffering.


### 7.3. accion decision abr salida

Palabras clave usadas: `action, actions, bitrate, bit rate, quality level, representation, decision, decisions, select, selection, adaptation, output, score, guidance, recommend, priority, policy output, controller, rate adaptation, quality`

**Fragmento 1 - p. 1 - score 6:**

ABR algo- rithms (a) chop a video into chunks, each of which is encoded at a range of bitrates (or qualities); and (b) choose which bitrate level to fetch a chunk at based on conditions such as the amount of video the client has buffered and the recent throughput achieved by the client. Within this general frame- work, ABR algorithms differ in how bitrate level selection decisions are made, and these decisions impact metrics such as the average bitrate or the rebuffering ratio. We call these QoE metrics, because they have been shown to correlate well with QoE [23], but other perceptual video quality metrics [2] may also influence QoE. ABR algorithm design remains an active research area be- cause content providers continue to be interested in improving the performance of video delivery.

**Fragmento 2 - p. 2 - score 4:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 3 - p. 3 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces throughput prediction errors, a more conservative version, Ro- bustMPC, reduces predicted throughput by a discount factor 1+𝑑, where 𝑑is the maximum error in throughput predictions experienced in the last five chunk downloads. BOLA: Buffer occupancy, selects bitrate by solving an optimization problem. BOLA is a buffer-based algorithm used in Dash.js [7], so it does not employ throughput pre- diction in making bitrate decisions [48].

**Fragmento 4 - p. 4 - score 4:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the left graph, although the throughput is generally good, the sudden variations force RobustMPC to make overly conserva- tive bitrate decisions, as well as incur more bitrate switches. (bottom subgraph). In contrast, in Figure 2(b), the quicker and more frequent throughput changes (top subgraph) result in FastMPC experiencing rebuffering (middle subgraph), while RobustMPC does not. This is just one example illustrating the difficulty in picking parameters – in our evaluations (§4), we found that RobustMPC was itself too aggressive when selecting discount factors for some traces. While this section uses synthetic traces for illustrative pur- poses, our evaluations with real traces (§4) more extensively demonstrate the limitations of current approaches with re- spect to selecting parameters and the benefits of automatically tuning ABR parameters to network conditions.

**Fragmento 5 - p. 14 - score 4:**

[49] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang, Tao Liu, and Bruno Sinopoli. CS2P: Improving Video Bitrate Selection and Adapta- tion with Data-Driven Throughput Prediction. In Proceedings of the ACM Con- ference on Special Interest Group on Data Communication, SIGCOMM, 2016. [50] Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press Cambridge, 1998. [51] Guibin Tian and Yong Liu. Towards Agile and Smooth Video Adaptation in Dynamic HTTP Streaming. In the ACM International Conference on Emerging Networking Experiments and Technologies, CoNEXT, 2012. [52] Guillaume Urvoy-Keller. On the Stationarity of TCP Bulk Data Transfers. In Proceedings of the Passive and Active Measurement Conference, PAM, 2005.

**Fragmento 6 - p. 1 - score 3:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary © 2018 Association for Computing Machinery. ACM ISBN 978-1-4503-5567-4/18/08...$15.00 https://doi.org/10.1145/3230543.3230558 Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018 Conference, August 20–25, 2018, Budapest, Hungary. 15 pages. https://doi.org/10.1145/3230543.3230558 1 INTRODUCTION Internet video forms a major fraction of Internet traffic to- day [13], and delivering high quality of experience (QoE) is critical since it correlates with user engagement and revenue [6, 23, 31]. To deliver high quality video across diverse net- work conditions, most Internet video delivery uses adaptive bitrate (ABR) algorithms [32, 48, 59], combined with HTTP chunk-based streaming protocols (e.g., Apple’s HTTP Live Streaming, Adobe’s HTTP Dynamic Streaming).

**Fragmento 7 - p. 2 - score 3:**

Publishers, content delivery networks, and users all seek to improve user quality of experience (QoE). There are many factors that affect QoE including start up latency, the average bitrate for a video session, as well as the rebuffering ratio (the percentage of time playback is stalled because of drained buffer) [23]. Video players improve QoE using adaptive bitrate (ABR) algorithms which select bitrates for each chunk while (1) ensuring the bitrate seen by the user is as high as possible and (2) avoiding rebuffering events at the client. Some ABR algorithms may also try to minimize the number of bitrate switches to make the playback smooth. Content publishers serve different types of content includ- ing VoD (Video on Demand) or Live broadcasts.

**Fragmento 8 - p. 3 - score 3:**

It also models bitrate selection as an optimization problem which it solves for a given value of the buffer. It uses a parameter 𝛾which is a ratio of (i) a minimum buffer threshold, below which it downloads the lowest bitrate and (ii) a target buffer threshold which it tries to maintain. Conceptually 𝛾controls how strongly the ABR should avoid rebuffering [48]. Higher values of 𝛾make the algorithm conservative. HYB: Throughput prediction without lookahead. Selects bitrate using a simple heuristic. An algorithm widely used in production (§5), HYB considers both the predicted throughput and current buffer occupancy (HYB is short for hybrid). For each chunk, HYB picks the highest bitrate that can avoid rebuffering.

**Fragmento 9 - p. 4 - score 3:**

Oboe leverages the piecewise stationarity of network con- nections to address the key challenge of sensitivity of config- urations to network conditions. It does so using a two stage design: (a) an offline stage where it pre-computes the best con- figuration choice for each (stationary) network state (§3.2), and (b) and an online stage, where during a session, it de- tects changes in network state and applies the pre-computed best configuration for the current (stationary) state (§3.3). Oboe can also accommodate publisher specifications such as session type (live vs. video-on-demand, time-to-live re- quirements), bitrate levels or any explicit QoE tradeoffs (e.g., preference between rebuffering and average bitrate) (§3.2), by using these to influence the selection of the best configuration for each (stationary) network state in the offline stage.

**Fragmento 10 - p. 5 - score 3:**

For a given network state 𝑠, ConfigEvaluator sweeps through possible configurations of the ABR algorithm using the VirtualPlayer. For example, the 𝛽parameter in HYB can take values from 0 to 1, so ConfigEvaluator plays the trace for state 𝑠for multiple values of 𝛽(quantized for efficiency, see below) in this range. For each parameter value 𝑐𝑖, VirtualPlayer outputs a per- formance vector 𝑉𝑖=< 𝑣1, 𝑣2, . . . 𝑣𝑚> where each 𝑣𝑘cor- responds to the values achieved by 𝑐𝑖for a QoE metric (e.g., bitrate, rebuffering ratio, and more generally join time and frequency of switching bitrates [23]). This set of performance vectors with the corresponding parameter values are then sent to ConfigSelector for picking the best configuration.

**Fragmento 11 - p. 6 - score 3:**

Given these sources of uncertainty, Oboe chooses to be safe in its selec- tion of the best configuration for 𝑠. Finally, ReconfEngine configures the ABR algorithm, and the reconfigured ABR algorithm is ready to compute the bitrate decision to be used for the next chunk at this point. 4 EVALUATION In this section, we demonstrate Oboe’s ability to auto-tune three existing algorithms: RobustMPC, BOLA and HYB. We also compare an Oboe-tuned RobustMPC to Pensieve [39]. 4.1 Metrics The performance of a video session depends on multiple fac- tors. Average bitrate and rebuffering ratio were found to have the most impact on user quality of experience [23], though other factors such as changes in bitrates during a session can play a role [23].

**Fragmento 12 - p. 7 - score 3:**

All our testbed experiments use a client buffer of 2 minutes. Datasets. We use throughput traces from real user sessions collected over a three month period. Each trace contains the in- dividual chunk sizes and their download times for on-demand video sessions from a publisher that serves short (4-6 minute) music videos. We derive throughput by dividing the chunk sizes by their download durations. The traces contain sessions that used desktops with wired connections and also sessions on mobile devices using WiFi or cellular connections. Like previous work [39, 59], we primarily focus on traces that have less than 6 Mbps average throughput, since this is the regime where bitrate switching decisions are likely to have QoE impact.

**Fragmento 13 - p. 8 - score 3:**

median per chunk change magnitude by 38% (Figure 6(d)). Fi- nally, Figure 7 shows the CDF of QoE-lin for MPC+Oboe and RobustMPC, and indicates MPC+Oboe distributionally performs better. Figure 8 illustrates, using a single session, why MPC+Oboe performs better than RobustMPC. The top graph shows throughput as a function of time, which includes an initial stable state followed by a drop in throughput. The middle graph shows how the discount factor 𝑑of both RobustMPC, and MPC+Oboe vary (the predicted throughput for each system is reduced by a factor of 1 1+𝑑, where 𝑑is shown on the y-axis). During the initial stable state, when prediction errors are low, RobustMPC steadily lowers its discount factor leading to more aggressive bitrate selections (not shown).

**Fragmento 14 - p. 8 - score 3:**

This results in a rebuffering event 44 seconds into the session (lowest graph shows buffer occupancy with 0 indicating a rebuffering event). In contrast, MPC+Oboe does not incur a rebuffering event and maintains a fixed 𝑑during the initial stable state. At 29 sec, it detects a change in the network state and adapts its discount factor, leading to more conservative bitrate selections. 4.4 Oboe vs. Pensieve Pensieve [39] uses deep reinforcement learning [41, 42], a combination of deep learning with reinforcement learn- ing [50], and has been shown to outperform existing ABRs, including RobustMPC [39] in some settings. Since 51

**Fragmento 15 - p. 10 - score 3:**

Pens-SelOnce starts with the 0-6 Mbps model, selects either the 0-3 Mbps or 3-6 Mbps model based on the average throughput of the first 5 initial chunks, and does not switch thereafter. Figure 13 shows CDFs of per-session QoE-lin improve- ment of MPC+Oboe over these selectors. MPC+Oboe is able to outperform both Pens-SelMultile and Pens-SelOnce, with average QoE-lin improvements of 14.2% and 24.32% re- spectively. Even though one of the model selection schemes offers some improvements over the 0-6 Mbps Pensieve model, the benefits are modest. We hypothesize that this behavior is due to the dynamic selection of distinct Pensieve models, which can interfere with reinforcement learning’s decision choices, since, during training, the reinforcement learning algorithm assumes there is no such third party intervention.

**Fragmento 16 - p. 11 - score 3:**

Oboe can improve performance over RobustMPC even when an Ideal(T) prediction method is used for two reasons. First, 𝑇may not match the duration of chunk downloads with RobustMPC, which depends on the exact sequence of bitrates chosen during the look-ahead window. The duration is not known a priori, since RobustMPC itself determines the bitrates based on a provided prediction. Second, the decisions made by RobustMPC are over a small look-ahead window, which may not guarantee optimality over the entire session duration. 4.7 Oboe Across Various Settings In §4.5 we have shown that Oboe outperforms other ABR algorithms when compared to their default configurations. We now explore, for HYB, whether Oboe outperforms all parameter settings of HYB and whether it can tune ABRs based on content type and publisher specifications.

**Fragmento 17 - p. 12 - score 3:**

In our implementation, a client player periodically reports player state (such as buffer length and current bitrate) and throughput samples to a Oboe cloud server and receives bitrate decisions in return. For 10 player features and two chunk downloads per second, the commu- nication overhead is 6.4 Kbps, negligibly small compared to the size of video chunks. Figures 19(a) and 19(b) compare the performance of this implementation against a client player running HYB over 20K sessions collected during a two-week pilot deployment. Oboe is comparable in performance to the client side player and even improves bitrate slightly (because it was tuned to this publisher’s specification). 55

**Fragmento 18 - p. 13 - score 3:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary We expected a cloud implementation would perform worse because of the latency induced by client-server communica- tion. However, we found that most of the bitrate switching decisions occur on timescales much longer than the client- server latencies. Figure 20 shows the CDF of the time interval between consecutive bitrate switches for ABR algorithms in two widely used video players(Adobe’s Flash [3] and Mi- crosoft Smooth Streaming [1]). The figure shows that over 95% of switching decisions occur at intervals higher than 1 second for both players. This suggests that a cloud-based deployment is viable. 6 DISCUSSION AND FUTURE WORK Performance improvements for all sessions.

**Fragmento 19 - p. 14 - score 3:**

Design and Optimisation of a (FA)Q-learning-based HTTP Adaptive Streaming Client. Connection Science, 26(1):25–43, 2014. [22] Frédéric Desobry, Manuel Davy, and Christian Doncarli. An Online Kernel Change Detection Algorithm. IEEE Transactions on Signal Processing, 53(8): 2961–2974, 2005. [23] Florin Dobrian, Vyas Sekar, Asad Awan, Ion Stoica, Dilip Joseph, Aditya Gan- jam, Jibin Zhan, and Hui Zhang. Understanding the Impact of Video Quality on User Engagement. In Proceedings of the ACM Conference on Special Interest Group on Data Communication, SIGCOMM, 2011. [24] Paul Fernhead. Exact and Efficient Bayesian Inference for Multiple Changepoint Problems. Statistics and Computing, 16(2):203–213, 2006. [25] Tobias Flach, Pavlos Papageorge, Andreas Terzis, Luis Pedrosa, Yuchung Cheng, Tayeb Karim, Ethan Katz-Bassett, and Ramesh Govindan.

**Fragmento 20 - p. 14 - score 3:**

Why Should I Trust You?: Explaining the Predictions of Any Classifier. In Proceedings of the ACM International Conference on Knowledge Discovery and Data Mining, SIGKDD, 2016. [46] Haakon Riiser, Paul Vigmostad, Carsten Griwodz, and Pål Halvorsen. Commute Path Bandwidth Traces from 3G Networks: Analysis and Applications. In Pro- ceedings of the ACM Multimedia Systems Conference, MMSys, 2013. [47] Jeffrey Semke, Jamshid Mahdavi, and Matthew Mathis. Automatic TCP Buffer Tuning. In Proceedings of the ACM Conference on Special Interest Group on Data Communication, SIGCOMM, 1998. [48] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K Sitaraman. BOLA: Near-optimal Bitrate Adaptation for Online Videos. In Proceedings of the IEEE International Conference on Computer Communications, INFOCOM, 2016.

**Fragmento 21 - p. 2 - score 2:**

2.1 Background on ABR Algorithms ABR algorithms fall in two broad categories: (i) those that use both prediction of network throughput and buffer occu- pancy [34, 51, 59]; and (ii) those that are primarily based on buffer occupancy [32, 48]. Within the above two categories, ABR algorithms can be designed using approaches ranging from heuristics to stochastic optimization. In §4, we discuss a recently proposed ABR algorithm based on a qualitatively different approach, reinforcement learning [39]. MPC: Throughput prediction and buffer occupancy with look-ahead. Selects bitrate by solving an optimization prob- lem. MPC [59] predicts throughput of future chunk down- loads based on throughput samples of recently downloaded chunks, then uses this predicted throughput to select bitrates to optimize a given QoE function (§4) over a look-ahead window of 5 future chunks.

**Fragmento 22 - p. 2 - score 2:**

They may also serve streams of different qualities ranging from HD (high definition) to SD (standard definition). These differ- ences impact how they serve videos. For example, publishers who serve VoD content can use player buffers as large as 4 minutes [32], whereas publishers serving live content may have a time-to-live2 requirement between 15-45 seconds. Sim- ilarly, based on the quality of streams they serve, publishers may use different bitrate levels or chunk sizes. Further, pub- lishers may have different QoE objectives. For example, some may strictly prefer to minimize rebuffering and others may relax their tolerance for rebuffering to prioritize higher bi- trates. We use the term publisher specifications to denote their choice of bitrate levels, chunk sizes, content type, and rebuffering tolerance.

**Fragmento 23 - p. 4 - score 2:**

The Virtu- alPlayer interfaces with the ABR algorithm implementation and outputs the performance of different configurations of the ABR. Finally, the ConfigSelector compares the performance of different configurations and builds a ConfigMap, which maps a given network state to the best configuration. 47

**Fragmento 24 - p. 5 - score 2:**

The VirtualPlayer also takes into account publisher spec- ifications for bitrate levels, player buffer sizes (determined by time-to-live requirements) and chunk size. These spec- ifications are used by VirtualPlayer when it executes ABR algorithms on the input traces, ensuring that the resulting Con- figMap meets the publisher specifications. Finally, Oboe also allows the publisher to optionally express an explicit QoE tradeoff such as maintaining the rebuffering under a desired threshold 𝑥%. Oboe derives a ConfigMap that meets the re- buffering threshold in a best effort manner. We evaluate the efficacy of this flexibility in §4.7. Building the ConfigMap using ConfigSelector. To build the ConfigMap, the ConfigEvaluator drives the exploration of different configurations for an ABR algorithm.

**Fragmento 25 - p. 5 - score 2:**

ConfigSelector takes the set of performance vectors and determines the best configuration from them using vector dominance. A configuration 𝑐𝑖is said to dominate 𝑐𝑗if 𝑉𝑖 element-wise dominates 𝑉𝑗(i.e., each element of 𝑉𝑖is bet- ter than or equal to the corresponding element of 𝑉𝑗). This step also takes into account any rebuffering tolerance, and ConfigSelector applies this tolerance to select the maximal performance vector. Deferring the selection of the maximal vector for a given rebuffering tolerance to this stage (instead of filtering vectors in the previous step) is beneficial: it mini- mizes recomputation by allowing Oboe to quickly compute a new maximal vector if the publisher changes the rebuffering tolerance.

**Fragmento 26 - p. 6 - score 2:**

Players such as Dash.js already periodically log intermediate throughput samples during a chunk download, so obtaining these sam- ples does not incur any additional overhead. We only need to modify players to report these samples to Oboe. The set of samples are provided to ChangeDetector after the chunk download, and any change in state is only detected at the end of the chunk download. This is acceptable since any action that can be taken by the ABR algorithm (such as a bit rate switch) only impacts subsequent chunks. In the rarer case that an ABR algorithm abandons the download of a chunk that takes too long, the report is sent when the chunk download is abandoned. §4.8 evaluates the overheads of ChangeDetector.


### 7.4. reward qoe objetivo loss

Palabras clave usadas: `reward, QoE, quality of experience, utility, objective, loss, rebuffer, stall, stalling, smoothness, switching, quality variation, bitrate smoothness, video quality, penalty, consistent, consistency, risk, tail, latency`

**Fragmento 1 - p. 2 - score 5:**

Publishers, content delivery networks, and users all seek to improve user quality of experience (QoE). There are many factors that affect QoE including start up latency, the average bitrate for a video session, as well as the rebuffering ratio (the percentage of time playback is stalled because of drained buffer) [23]. Video players improve QoE using adaptive bitrate (ABR) algorithms which select bitrates for each chunk while (1) ensuring the bitrate seen by the user is as high as possible and (2) avoiding rebuffering events at the client. Some ABR algorithms may also try to minimize the number of bitrate switches to make the playback smooth. Content publishers serve different types of content includ- ing VoD (Video on Demand) or Live broadcasts.

**Fragmento 2 - p. 1 - score 3:**

ABR algo- rithms (a) chop a video into chunks, each of which is encoded at a range of bitrates (or qualities); and (b) choose which bitrate level to fetch a chunk at based on conditions such as the amount of video the client has buffered and the recent throughput achieved by the client. Within this general frame- work, ABR algorithms differ in how bitrate level selection decisions are made, and these decisions impact metrics such as the average bitrate or the rebuffering ratio. We call these QoE metrics, because they have been shown to correlate well with QoE [23], but other perceptual video quality metrics [2] may also influence QoE. ABR algorithm design remains an active research area be- cause content providers continue to be interested in improving the performance of video delivery.

**Fragmento 3 - p. 2 - score 3:**

They may also serve streams of different qualities ranging from HD (high definition) to SD (standard definition). These differ- ences impact how they serve videos. For example, publishers who serve VoD content can use player buffers as large as 4 minutes [32], whereas publishers serving live content may have a time-to-live2 requirement between 15-45 seconds. Sim- ilarly, based on the quality of streams they serve, publishers may use different bitrate levels or chunk sizes. Further, pub- lishers may have different QoE objectives. For example, some may strictly prefer to minimize rebuffering and others may relax their tolerance for rebuffering to prioritize higher bi- trates. We use the term publisher specifications to denote their choice of bitrate levels, chunk sizes, content type, and rebuffering tolerance.

**Fragmento 4 - p. 5 - score 3:**

For a given network state 𝑠, ConfigEvaluator sweeps through possible configurations of the ABR algorithm using the VirtualPlayer. For example, the 𝛽parameter in HYB can take values from 0 to 1, so ConfigEvaluator plays the trace for state 𝑠for multiple values of 𝛽(quantized for efficiency, see below) in this range. For each parameter value 𝑐𝑖, VirtualPlayer outputs a per- formance vector 𝑉𝑖=< 𝑣1, 𝑣2, . . . 𝑣𝑚> where each 𝑣𝑘cor- responds to the values achieved by 𝑐𝑖for a QoE metric (e.g., bitrate, rebuffering ratio, and more generally join time and frequency of switching bitrates [23]). This set of performance vectors with the corresponding parameter values are then sent to ConfigSelector for picking the best configuration.

**Fragmento 5 - p. 7 - score 3:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 5—A scatter plot of average bitrate and rebuffering ratio between the Virtu- alPlayer and real Dash.js player and BOLA primarily maximize average bitrate subject to low rebuffering. In contrast, other algorithms [39, 59] have been designed to optimize a QoE metric which is a linear combina- tion of bitrate, rebuffering and bitrate changes (smoothness). With Oboe, our primary evaluation goal is to demonstrate the extent to which it can improve the underlying metrics that an ABR algorithm is designed for. Thus, our evaluations with BOLA and HYB focus on average bitrate and rebuffering, while those with MPC+Oboe focus on the linear combination of QoE (which we refer to as QoE-lin, [59]), defined as follows.

**Fragmento 6 - p. 7 - score 3:**

For a video with 𝑁chunks, let 𝑅𝑖be the bitrate chosen for chunk 𝑖. Then, the magnitude of bitrate changes 𝑀may be defined as 𝑀= ∑︀𝑁−1 𝑖 |𝑅𝑖+1 −𝑅𝑖|. If the ses- sion experiences a total of 𝑇seconds of rebuffering, then, QoE-lin(𝑝, 𝑐) = 1 𝑁*∑︀ 𝑖(𝑅𝑖−𝑝𝑇−𝑐*𝑀), where 𝑝and 𝑐 represent scaling penalties applied to rebuffering and changes in the session. This function may be viewed as the session QoE averaged over the number of chunks. For our videos that had a maximum bitrate of 4.3 Mbps, we use 𝑝= 4.3 and 𝑐= 1 as our default parameters (following previous work that set default rebuffering penalty equal to the maximum bitrate value [39, 59]). Even when an algorithm optimizes a metric such as QoE-lin, it is important to understand the distributions of underlying factors.

**Fragmento 7 - p. 8 - score 3:**

In particular, for 19% of the sessions, QoE-lin improves by more than 20%. For the sessions MPC+Oboe is unable to improve RobustMPC, its performance degradation is mostly under 8%. Figures 6(b), 6(c) and 6(d) show the constituent QoE metrics. While MPC+Oboe achieves distributionally sim- ilar bitrates as RobustMPC as shown in 6(b), it significantly reduces rebuffering across sessions: the number of sessions with rebuffering reduces from 33.2% to 5.3%. Further, it also achieves better playback smoothness by improving the 4The increase in QoE-lin over RobustMPC relative to the absolute QoE-lin value of RobustMPC expressed as a percentage. Figure 8—An example session showing how MPC+Oboe is able to outperform Ro- bustMPC by reconfiguring the discount parameter when a network state change is de- tected.

**Fragmento 8 - p. 1 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary © 2018 Association for Computing Machinery. ACM ISBN 978-1-4503-5567-4/18/08...$15.00 https://doi.org/10.1145/3230543.3230558 Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018 Conference, August 20–25, 2018, Budapest, Hungary. 15 pages. https://doi.org/10.1145/3230543.3230558 1 INTRODUCTION Internet video forms a major fraction of Internet traffic to- day [13], and delivering high quality of experience (QoE) is critical since it correlates with user engagement and revenue [6, 23, 31]. To deliver high quality video across diverse net- work conditions, most Internet video delivery uses adaptive bitrate (ABR) algorithms [32, 48, 59], combined with HTTP chunk-based streaming protocols (e.g., Apple’s HTTP Live Streaming, Adobe’s HTTP Dynamic Streaming).

**Fragmento 9 - p. 2 - score 2:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 10 - p. 2 - score 2:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 11 - p. 4 - score 2:**

Oboe leverages the piecewise stationarity of network con- nections to address the key challenge of sensitivity of config- urations to network conditions. It does so using a two stage design: (a) an offline stage where it pre-computes the best con- figuration choice for each (stationary) network state (§3.2), and (b) and an online stage, where during a session, it de- tects changes in network state and applies the pre-computed best configuration for the current (stationary) state (§3.3). Oboe can also accommodate publisher specifications such as session type (live vs. video-on-demand, time-to-live re- quirements), bitrate levels or any explicit QoE tradeoffs (e.g., preference between rebuffering and average bitrate) (§3.2), by using these to influence the selection of the best configuration for each (stationary) network state in the offline stage.

**Fragmento 12 - p. 5 - score 2:**

The VirtualPlayer also takes into account publisher spec- ifications for bitrate levels, player buffer sizes (determined by time-to-live requirements) and chunk size. These spec- ifications are used by VirtualPlayer when it executes ABR algorithms on the input traces, ensuring that the resulting Con- figMap meets the publisher specifications. Finally, Oboe also allows the publisher to optionally express an explicit QoE tradeoff such as maintaining the rebuffering under a desired threshold 𝑥%. Oboe derives a ConfigMap that meets the re- buffering threshold in a best effort manner. We evaluate the efficacy of this flexibility in §4.7. Building the ConfigMap using ConfigSelector. To build the ConfigMap, the ConfigEvaluator drives the exploration of different configurations for an ABR algorithm.

**Fragmento 13 - p. 6 - score 2:**

Given these sources of uncertainty, Oboe chooses to be safe in its selec- tion of the best configuration for 𝑠. Finally, ReconfEngine configures the ABR algorithm, and the reconfigured ABR algorithm is ready to compute the bitrate decision to be used for the next chunk at this point. 4 EVALUATION In this section, we demonstrate Oboe’s ability to auto-tune three existing algorithms: RobustMPC, BOLA and HYB. We also compare an Oboe-tuned RobustMPC to Pensieve [39]. 4.1 Metrics The performance of a video session depends on multiple fac- tors. Average bitrate and rebuffering ratio were found to have the most impact on user quality of experience [23], though other factors such as changes in bitrates during a session can play a role [23].

**Fragmento 14 - p. 7 - score 2:**

All our testbed experiments use a client buffer of 2 minutes. Datasets. We use throughput traces from real user sessions collected over a three month period. Each trace contains the in- dividual chunk sizes and their download times for on-demand video sessions from a publisher that serves short (4-6 minute) music videos. We derive throughput by dividing the chunk sizes by their download durations. The traces contain sessions that used desktops with wired connections and also sessions on mobile devices using WiFi or cellular connections. Like previous work [39, 59], we primarily focus on traces that have less than 6 Mbps average throughput, since this is the regime where bitrate switching decisions are likely to have QoE impact.

**Fragmento 15 - p. 8 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 6—The percentage improvement in QoE-lin of MPC+Oboe over RobustMPC for the Testbed experiment. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 7—QoE-lin of MPC+Oboe compared to RobustMPC of tracking the performance of the actual ABR algorithms. For instance, Figure 5(a) and 5(b) demonstrates this for the HYB algorithm. The figures shows the correlation for the average bitrate and rebuffering ratio for 100 throughput traces randomly sampled from our dataset using HYB on the VirtualPlayer compared to using an actual Dash.js player. For both metrics, the graph closely tracks the 𝑦= 𝑥line indicating close correlation.

**Fragmento 16 - p. 9 - score 2:**

Comparison with Pensieve. Figure 9(a) shows the CDF of the percentage improvement in QoE-lin for MPC+Oboe over Pensieve. MPC+Oboe outperforms Pensieve for 81% of the sessions, with a QoE-lin improvement of 23.9% in aver- age across all sessions. 25% of the sessions achieve more than 20% QoE-lin improvement. For the sessions MPC+Oboe is unable to improve over Pensieve, the performance differ- ence is mostly less than 5%. Figures 9(b), 9(c) and 9(d) show that MPC+Oboe distributionally outperforms Pensieve with respect to all underlying metrics. It reduces the number of sessions with rebuffering from 10.7% to 5.3%, reduces the median per chunk change magnitude by 43.9%, and improves median and 95th percentile average bitrate by 2.6% and 4.7% respectively.

**Fragmento 17 - p. 9 - score 2:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 10—Validation of our training methodology for Pensieve. Figure 11—QoE-lin of MPC+Oboe compared to Pensieve Figure 12—Benefits of specializing Pensieve models. Each curve shows the QoE improvement of MPC+Oboe rela- tive to each Pensieve model. Figure 13—QoE improvement of MPC+Oboe over two ways of dy- namically selecting from specialized Pensieve models. MPC+Oboe outperforms RobustMPC as well, we explore how MPC+Oboe performs relative to Pensieve.

**Fragmento 18 - p. 10 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d) Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors Pensieve is 19.9%. This indicates specializing the model does improve Pensieve’s performance. Thus, Pensieve’s model is as yet unable to create special- ized versions of itself based on the session characteristics. By contrast, Oboe specializes parameters for every network state and therefore performs better. We have also validated Pensieve’s inability to specialize in several other ways: build- ing a model for the 3-6 Mbps and showing that it performs better with test data in that range compared to a 0-6 Mbps model; checking that a 0-6 Mbps model performs better for data in that range compared to a 0-100 Mbps model; and ensuring that these results hold even when the training set is doubled.

**Fragmento 19 - p. 12 - score 2:**

In contrast, Figure 18 shows that RobustMPC is less effective at controlling rebuffering by adjusting its rebuffering penalty when the weight on the rebuffering term is varied between 100 (strictly avoid rebuffering) to 4.3.5 We find that even with a very high rebuffering penalty of 100, RobustMPC causes rebuffering in 11% of the sessions. This shows the benefit of Oboe’s approach which gives direct control over the underly- ing metrics. 4.8 Oboe Overhead Computing the ConfigMap incurs a one-time cost, since the map can be reused across all clients once the it is built. Com- puting the best parameter configuration for one network state takes about 12 seconds on a single core. This task is perfectly parallelizable, so computing 10K network states (§3) will take approximately 3.5 hours to explore with two machines of 48 cores each.

**Fragmento 20 - p. 12 - score 2:**

We have also analyzed the processing over- head incurred by the ChangeDetector module of Oboe. We measure the time taken by ChangeDetector for every decision 5We used a change penalty of 0 for fair comparison. Figure 19—Comparing prototype Oboe with commercial client side ABR implemen- tation in average bitrate and rebuffering ratio. Figure 20—Time between consecutive bitrate switches for two commercial ABRs Figure 21—Variance in bitrate levels across videos from two content publish- ers. cycle across our experiments, and the measurement indicates that the median processing time of ChangeDetector is around 14 ms. Since each decision is made at a chunk boundary and chunks are 4 seconds, ChangeDetector accounts for less than 0.35% overhead.

**Fragmento 21 - p. 12 - score 2:**

Even for these choices, HYB+Oboe outperforms HYB, demonstrating its ability to adapt to differ- ent publisher specification. Accommodating publisher’s rebuffering tolerance. Oboe allows the publisher to optionally specify explicit rebuffer- ing preferences (§3). ABR algorithms such as RobustMPC which use the QoE-lin function may permit this indirectly by adjusting QoE-lin weights (§2.1). Figure 17 shows the effectiveness of these approaches, showing the average of average bitrates, and the fraction of sessions with rebuffering for HYB+Oboe. As the publisher makes its rebuffering pref- erence stricter (from 2%-0%), HYB+Oboe achieves lower rebuffering ratios close to the target rebuffering tolerance.

**Fragmento 22 - p. 13 - score 2:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary We expected a cloud implementation would perform worse because of the latency induced by client-server communica- tion. However, we found that most of the bitrate switching decisions occur on timescales much longer than the client- server latencies. Figure 20 shows the CDF of the time interval between consecutive bitrate switches for ABR algorithms in two widely used video players(Adobe’s Flash [3] and Mi- crosoft Smooth Streaming [1]). The figure shows that over 95% of switching decisions occur at intervals higher than 1 second for both players. This suggests that a cloud-based deployment is viable. 6 DISCUSSION AND FUTURE WORK Performance improvements for all sessions.

**Fragmento 23 - p. 13 - score 2:**

As our re- sults (e.g., Figure 6(a)) show, Oboe improves the perfor- mance for most but not all sessions relative to the ABR al- gorithm it tunes. For instance, after inspecting the results in §4.3, we have found that MPC+Oboe typically improves performance relative to RobustMPC by reducing rebuffering and/or the magnitude of bitrate changes, but at the expense of slightly lower bitrates. The resulting QoE-lin is improved for most sessions, indicating Oboe does a good job of properly balancing the various factors, but some sessions see lower QoE-lin. More generally, designing an ABR approach that can optimize the performance of all sessions is a hard problem that needs more research. Sharing ConfigMap across videos.

**Fragmento 24 - p. 1 - score 1:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 25 - p. 1 - score 1:**

Oboe: Auto-tuning Video ABR Algorithms to Network Conditions Zahaib Akhtar* University of Southern California Yun Seong Nam* Purdue University Ramesh Govindan University of Southern California Sanjay Rao Purdue University Jessica Chen University of Windsor Ethan Katz-Bassett Columbia University Bruno Ribeiro Purdue University Jibin Zhan Conviva Hui Zhang Conviva ABSTRACT Most content providers are interested in providing good video delivery QoE for all users, not just on average. State-of-the-art ABR algorithms like BOLA and MPC rely on parameters that are sensitive to network conditions, so may perform poorly for some users and/or videos. In this paper, we propose a technique called Oboe to auto-tune these parameters to dif- ferent network conditions.

**Fragmento 26 - p. 1 - score 1:**

Current ABR algorithms perform well on average, but some users can experience poor delivery performance as measured by the QoE metrics. These users suffer because ABR algorithms have limited dynamic range: they do not perform uniformly well across the range of network conditions seen in practice because their parameters are sensitive to throughput variability (§2). Contributions. In this paper, we present the design of Oboe1 (§3), a system that takes the first step towards overcoming these hurdles. Oboe improves the dynamic range of ABR algorithms by automatically tuning ABR behavior to 1In orchestras all instruments tune to the Oboe. 44


### 7.5. entrenamiento optimizacion pipeline

Palabras clave usadas: `training, train, trained, episode, epoch, optimizer, learning rate, loss function, minibatch, clipped, probability ratio, experience, simulation, simulator, emulation, testbed, fine-tuning, pretrain, learning task, meta-training, adaptation, oracle, auto-tuning, offline, online`

**Fragmento 1 - p. 9 - score 4:**

Figure 10 shows CDFs of QoE-lin for the pretrained (Original) model and the model trained by us (Retrained). The performance distribution of the two models are almost identical over the test traces provided by the Pensieve authors, thereby validating our retraining methodology. Having validated our retraining methodology, we trained Pensieve on our dataset with the same complete strategy described above. For this, we pick 1600 traces randomly from our dataset with average throughput in the 0-6 Mbps range. The number of training traces, the number of iterations per trace, and the range of throughput are similar to [39]. We then compare Pensieve and MPC+Oboe over a separate test set of traces also in the range of 0-6 Mbps (§4.2).

**Fragmento 2 - p. 2 - score 3:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 3 - p. 5 - score 3:**

For each state, we generate a synthetic stationary trace. We found that the benefits of finer quantization are marginal. Estimating ABR performance with VirtualPlayer and publisher specifications. Oboe uses VirtualPlayer, a trace- based simulator that mimics the behavior of an actual video player without downloading or rendering actual videos. It takes as input a throughput trace and outputs the QoE performance metrics of a video session for a specified ABR algorithm. We have validated VirtualPlayer in §4.7. In designing VirtualPlayer, we have decoupled ABR logic (Figure 3), so the same implementation of the ABR logic can be used in Oboe’s offline and online stage. Further, this design provides an interface to the ABR designer through which they can easily integrate their ABR algorithm with Oboe without having to know about Oboe’s internals.

**Fragmento 4 - p. 9 - score 3:**

Our exper- iments use the Pensieve implementation provided by the authors [11]. Pensieve Re-Training and Validation. Before evaluating Pensieve on our dataset, we retrain Pensieve using the source code on the trace dataset provided by the Pensieve authors [11]. This helps us validate our retraining given that deep reinforcement learning results are not easy to reproduce [29]. We experimented with five different initial entropy weights in the author suggested range of 1 to 5, and linearly reduced their values in a gradual fashion using plateaus, with five different decrease rates until the entropy weight eventually reached 0.1. This rate scheduler follows best-practice [55]. From the trained set of models, we then selected the best performing model (an initial entropy weight of 1 reduced every 800 iterations until it reaches 0.1 over 100K iterations) and compared its performance to the pre-trained Pensieve model provided by the authors.

**Fragmento 5 - p. 2 - score 2:**

We have tried training specialized Pensieve models for different ranges of network throughputs and dynamically switching models based on estimated session throughput. This helps, but a sig- nificant gap between the two approaches still remains (§4.4). While a variety of viable pathways exist to deploying Oboe, we focus on an architecture where Oboe and the entire ABR logic are deployed on the cloud which enables rapid evolution and fine-grain customizability. We show the viability of this architecture with results from a pilot deployment. 2 BACKGROUND AND MOTIVATION The Internet video delivery ecosystem consists of hundreds of content publishers and hundreds of client side applications that stream video content to diverse user devices.

**Fragmento 6 - p. 4 - score 2:**

Oboe leverages the piecewise stationarity of network con- nections to address the key challenge of sensitivity of config- urations to network conditions. It does so using a two stage design: (a) an offline stage where it pre-computes the best con- figuration choice for each (stationary) network state (§3.2), and (b) and an online stage, where during a session, it de- tects changes in network state and applies the pre-computed best configuration for the current (stationary) state (§3.3). Oboe can also accommodate publisher specifications such as session type (live vs. video-on-demand, time-to-live re- quirements), bitrate levels or any explicit QoE tradeoffs (e.g., preference between rebuffering and average bitrate) (§3.2), by using these to influence the selection of the best configuration for each (stationary) network state in the offline stage.

**Fragmento 7 - p. 5 - score 2:**

3.3 Online ABR Tuning Oboe uses the ConfigMap generated offline, and live through- put measurements from the video player to dynamically change ABR configurations during a video playback. It does this by using an online change point detection algorithm [14]. This algorithm identifies, in an online fashion, if the distribution of the throughput samples has changed significantly, signaling a state transition. When a change point is detected, the algorithm also provides the new state 48

**Fragmento 8 - p. 6 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 4—Logical diagram of Oboe’s online pipeline 𝑠’s mean and standard deviation. Oboe’s ChangeDetector (Figure 4) implements the change point detection algorithm, and the ReconfEngine is responsible for updating the ABR configuration based on a new network state and the ConfigMap. Change point detection algorithms. Such algorithms ana- lyze a time series and check if there are regions in the time series where the underlying distribution of the data changes to a different set of parameters. Offline change-point methods require the full time series to be available, whereas online methods work with a continuous stream of samples as they become available.

**Fragmento 9 - p. 7 - score 2:**

The underlying factors represent concrete application performance that publishers understand how to reason about. Moreover, a unified metric like QoE-lin can obscure important differences. For example, two sessions may have the same QoE-lin but different performance in underlying metrics, leading to varied user experience. So, we also present graphs of these metrics. 4.2 Methodology Implementation. For RobustMPC, we used the imple- mentation available at [11]. Our implementation of BOLA [@bola] is from the Dash.js player. The implementation of HYB is a variant of the algorithm used in a large-scale deployment. These ABR algorithms and Oboe’s online stage (change point detection and ABR reconfiguration) run on the server in our experiments.

**Fragmento 10 - p. 8 - score 2:**

Given these close correlations, we use the VirtualPlayer in §4.7 to explore Oboe’s performance over a larger range of diverse settings and our entire set of traces. 4.3 Oboe with RobustMPC We now demonstrate that Oboe can be used to auto-tune Ro- bustMPC, the best performing variant of the MPC algorithms. The resulting MPC+Oboe uses the best value of the discount parameter 𝑑corresponding to the current network state, re- placing RobustMPC’s online adaptation based on throughput estimates obtained over the past 5 chunks (§2). Figure 6(a) shows the CDF of the percentage improvement in QoE-lin of MPC+Oboe over RobustMPC.4 MPC+Oboe improves QoE-lin for 71% of sessions, with an overall av- erage QoE-lin improvement of 17.62% across all sessions.

**Fragmento 11 - p. 9 - score 2:**

Finally, Figure 11 shows the CDF of QoE-lin for MPC+Oboe and Pensieve, and indicates MPC+Oboe per- forms distributionally better. Analyzing Pensieve performance. To understand where these performance improvements were coming from, we ex- amined the relative performance of these two schemes in the 0-3 Mbps range (i.e., traces having an average throughput be- tween 0-3 Mbps). In this more constrained range of network conditions, we found that MPC+Oboe achieves bigger gains over Pensieve (average QoE-lin improvement in 0-3 Mbps is 46.23%). We hypothesize that this performance difference stems from the fact that Pensieve builds a single model which does not specialize to different throughput ranges. To test this, we trained a separate Pensieve model only with traces that have an average throughput between 0-3 Mbps range and compared it with MPC+Oboe.

**Fragmento 12 - p. 9 - score 2:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 10—Validation of our training methodology for Pensieve. Figure 11—QoE-lin of MPC+Oboe compared to Pensieve Figure 12—Benefits of specializing Pensieve models. Each curve shows the QoE improvement of MPC+Oboe rela- tive to each Pensieve model. Figure 13—QoE improvement of MPC+Oboe over two ways of dy- namically selecting from specialized Pensieve models. MPC+Oboe outperforms RobustMPC as well, we explore how MPC+Oboe performs relative to Pensieve.

**Fragmento 13 - p. 9 - score 2:**

Figure 12 shows the per session QoE-lin improvement of MPC+Oboe com- pared to Pensieve models trained for 0-3 Mbps (which we refer to as Pens-Specialized) and for 0-6 Mbps. The me- dian QoE-lin improvement with MPC+Oboe over Pens- Specialized is 10.49%, while the median improvement over 52

**Fragmento 14 - p. 10 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d) Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors Pensieve is 19.9%. This indicates specializing the model does improve Pensieve’s performance. Thus, Pensieve’s model is as yet unable to create special- ized versions of itself based on the session characteristics. By contrast, Oboe specializes parameters for every network state and therefore performs better. We have also validated Pensieve’s inability to specialize in several other ways: build- ing a model for the 3-6 Mbps and showing that it performs better with test data in that range compared to a 0-6 Mbps model; checking that a 0-6 Mbps model performs better for data in that range compared to a 0-100 Mbps model; and ensuring that these results hold even when the training set is doubled.

**Fragmento 15 - p. 10 - score 2:**

Pens-SelOnce starts with the 0-6 Mbps model, selects either the 0-3 Mbps or 3-6 Mbps model based on the average throughput of the first 5 initial chunks, and does not switch thereafter. Figure 13 shows CDFs of per-session QoE-lin improve- ment of MPC+Oboe over these selectors. MPC+Oboe is able to outperform both Pens-SelMultile and Pens-SelOnce, with average QoE-lin improvements of 14.2% and 24.32% re- spectively. Even though one of the model selection schemes offers some improvements over the 0-6 Mbps Pensieve model, the benefits are modest. We hypothesize that this behavior is due to the dynamic selection of distinct Pensieve models, which can interfere with reinforcement learning’s decision choices, since, during training, the reinforcement learning algorithm assumes there is no such third party intervention.

**Fragmento 16 - p. 10 - score 2:**

FCC is a broadband dataset, while HSDPA contains throughput traces collected from video streaming sessions over 3G net- works in Norway using mobile devices. Our comparisons use the traces and a Pensieve model pre-trained for those traces available at [11]. We focus our evaluations on MPC+Oboe and Pensieve, given that Pensieve has been shown to out- perform existing ABR schemes including RobustMPC on 53

**Fragmento 17 - p. 11 - score 2:**

Our experi- ments were conducted in simulation, using the VirtualPlayer, and the testbed experiment traces (§4.2). Figure 15 shows the average QoE-lin across the traces for RobustMPC and MPC+Oboe using both the default har- monic mean approach and Ideal(T) for different values of T. Although RobustMPC performs better with an ideal predictor, Oboe still provides benefits, achieving an average improve- ment in QoE-lin of 6.34% for Ideal(5) and of 1.8% for Ideal(10), compared to a 16.1% improvement with the har- monic mean estimator. While the magnitude of benefits is smaller with the ideal prediction approach, in practice Oboe will likely result in larger benefits, since even more sophisti- cated schemes [49] cannot achieve the ideal predictions, and the errors are likely to grow with larger T.

**Fragmento 18 - p. 11 - score 2:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 16—Comparing HYB with multiple fixed configurations and HYB+Oboe for various settings these traces. Our results show that MPC+Oboe continues to perform better than RobustMPC on these traces. Further, rela- tive to Pensieve, MPC+Oboe improves QoE-lin by an aver- age of 6.94% across the FCC dataset and 10.92% across the HSDPA dataset. These improvements are more modest than those in Figure 9(a). The vast majority of traces in the FCC and HSDPA set have an average throughput under 3 Mbps (over 95% for FCC and 98% for HSDPA). The results cor- roborate Figure 12 which indicates that MPC+Oboe provides more modest gains over Pensieve when the latter is trained and evaluated on datasets with a narrow throughput range.

**Fragmento 19 - p. 12 - score 2:**

5 DEPLOYMENT CONSIDERATIONS The offline stage of Oboe can be run on the cloud, but several choices exist for the online stage, ranging from embedding the online stage entirely in the client player, or moving some or all of the online stage to the cloud. In our implementation, Oboe’s components run on the server side. This mimics a cloud implementation, which has the benefits of other cloud software: fast update deployment, device independence, etc. [4]. We leave a detailed comparison of these choices to future work, but explore, in this section, the feasibility of running the online stage on the cloud. To this end, we have implemented a restricted version of HYB+Oboe on AWS. This limited version of Oboe imple- ments HYB and incorporates tuning based on publisher speci- fications but not network state.

**Fragmento 20 - p. 14 - score 2:**

Why Should I Trust You?: Explaining the Predictions of Any Classifier. In Proceedings of the ACM International Conference on Knowledge Discovery and Data Mining, SIGKDD, 2016. [46] Haakon Riiser, Paul Vigmostad, Carsten Griwodz, and Pål Halvorsen. Commute Path Bandwidth Traces from 3G Networks: Analysis and Applications. In Pro- ceedings of the ACM Multimedia Systems Conference, MMSys, 2013. [47] Jeffrey Semke, Jamshid Mahdavi, and Matthew Mathis. Automatic TCP Buffer Tuning. In Proceedings of the ACM Conference on Special Interest Group on Data Communication, SIGCOMM, 1998. [48] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K Sitaraman. BOLA: Near-optimal Bitrate Adaptation for Online Videos. In Proceedings of the IEEE International Conference on Computer Communications, INFOCOM, 2016.

**Fragmento 21 - p. 14 - score 2:**

Ana- lyzing Stability in Wide-area Network Performance. ACM SIGMETRICS Perfor- mance Evaluation Review, 25:2–12, 1997. [18] Daniel Barry and John A Hartigan. A Bayesian Analysis for Change Point Prob- lems. Journal of the American Statistical Society, 88(421):309–319, 1993. [19] Neal Cardwell, Yuchung Cheng, C. Stephen Gunn, Soheil Hassas Yeganeh, and Van Jacobson. BBR: Congestion-Based Congestion Control. ACM Queue, 14: 20–53, 2016. [20] Federico Chiariotti, Stefano D’Aronco, Laura Toni, and Pascal Frossard. Online Learning Adaptation Strategy for DASH Clients. In Proceedings of the Interna- tional Conference on Multimedia Systems, MMSys, 2016. [21] Maxim Claeys, Steven Latré, Jeroen Famaey, Tingyao Wu, Werner Van Leek- wijck, and Filip De Turck.

**Fragmento 22 - p. 14 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. BIBLIOGRAPHY [1] Microsoft Smooth Streaming. http://www.iis.net/downloads/microsoft/smooth- streaming. [2] Toward A Practical Perceptual Video Quality Metric. https://medium. com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric- 653f208b9652. [3] Adobe OSMF player. http://www.osmf.org. [4] Oracle: 5 Reasons to Consider SaaS for Your Business Applications. http://www. oracle.com/us/solutions/cloud/saas-business-applications-1945540.pdf. [5] Chrome Remote Interface. https://github.com/cyrus-and/chrome-remote- interface. [6] Cisco: It Came to Me in a Stream. https://www.cisco.com/web/about/ac79/docs/ sp/Online-Video-Consumption_Consumers.pdf.

**Fragmento 23 - p. 14 - score 2:**

[14] Ryan Prescott Adams and David JC MacKay. Bayesian Online Changepoint Detection. In arXiv:0710.3742v1, 2007. [15] Saamer Akhshabi, Lakshmi Anantakrishnan, Ali C Begen, and Constantine Dovrolis. What Happens when HTTP Adaptive Streaming Players Compete for Bandwidth? In the International Workshop on Network and Operating System Support for Digital Audio and Video, NOSSDAV, 2012. [16] Athula Balachandran, Vyas Sekar, Aditya Akella, Srinivasan Seshan, Ion Stoica, and Hui Zhang. Developing a Predictive Model of Quality of Experience for Internet Video. In Proceedings of the ACM Conference on Special Interest Group on Data Communication, SIGCOMM, 2013. [17] Hari Balakrishnan, Mark Stemm, Srinivasan Seshan, and Randy H Katz.

**Fragmento 24 - p. 1 - score 1:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 25 - p. 1 - score 1:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary © 2018 Association for Computing Machinery. ACM ISBN 978-1-4503-5567-4/18/08...$15.00 https://doi.org/10.1145/3230543.3230558 Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018 Conference, August 20–25, 2018, Budapest, Hungary. 15 pages. https://doi.org/10.1145/3230543.3230558 1 INTRODUCTION Internet video forms a major fraction of Internet traffic to- day [13], and delivering high quality of experience (QoE) is critical since it correlates with user engagement and revenue [6, 23, 31]. To deliver high quality video across diverse net- work conditions, most Internet video delivery uses adaptive bitrate (ABR) algorithms [32, 48, 59], combined with HTTP chunk-based streaming protocols (e.g., Apple’s HTTP Live Streaming, Adobe’s HTTP Dynamic Streaming).

**Fragmento 26 - p. 1 - score 1:**

Oboe: Auto-tuning Video ABR Algorithms to Network Conditions Zahaib Akhtar* University of Southern California Yun Seong Nam* Purdue University Ramesh Govindan University of Southern California Sanjay Rao Purdue University Jessica Chen University of Windsor Ethan Katz-Bassett Columbia University Bruno Ribeiro Purdue University Jibin Zhan Conviva Hui Zhang Conviva ABSTRACT Most content providers are interested in providing good video delivery QoE for all users, not just on average. State-of-the-art ABR algorithms like BOLA and MPC rely on parameters that are sensitive to network conditions, so may perform poorly for some users and/or videos. In this paper, we propose a technique called Oboe to auto-tune these parameters to dif- ferent network conditions.


### 7.6. datos trazas datasets origen

Palabras clave usadas: `dataset, datasets, trace, traces, network trace, bandwidth trace, real-world, FCC, HSDPA, Norway, LTE, 4G, 5G, WiFi, WLAN, Mahimahi, emulation, testbed, Puffer, data, sessions, users, video, chunk, streaming server`

**Fragmento 1 - p. 7 - score 10:**

All our testbed experiments use a client buffer of 2 minutes. Datasets. We use throughput traces from real user sessions collected over a three month period. Each trace contains the in- dividual chunk sizes and their download times for on-demand video sessions from a publisher that serves short (4-6 minute) music videos. We derive throughput by dividing the chunk sizes by their download durations. The traces contain sessions that used desktops with wired connections and also sessions on mobile devices using WiFi or cellular connections. Like previous work [39, 59], we primarily focus on traces that have less than 6 Mbps average throughput, since this is the regime where bitrate switching decisions are likely to have QoE impact.

**Fragmento 2 - p. 10 - score 9:**

FCC is a broadband dataset, while HSDPA contains throughput traces collected from video streaming sessions over 3G net- works in Norway using mobile devices. Our comparisons use the traces and a Pensieve model pre-trained for those traces available at [11]. We focus our evaluations on MPC+Oboe and Pensieve, given that Pensieve has been shown to out- perform existing ABR schemes including RobustMPC on 53

**Fragmento 3 - p. 7 - score 8:**

We filtered out traces which were too short for playing our entire 192 second video, after which we obtained 5K traces from wired desktops and 4K sessions from WiFi or 3G/4G mobile devices. Our testbed experiments use a subset of 571 traces with roughly the same number of traces sampled from each of desktop and mobile clients. VirtualPlayer setup. Recall that Oboe uses the Virtu- alPlayer to obtain a ConfigMap for any ABR algorithm. Since the majority of our results use an actual testbed with the Dash.js player, the benefits of Oboe in our evaluation results already arise despite any inaccuracies in building the ConfigMap on account of using the VirtualPlayer. That said, we have also verified that the VirtualPlayer does a good job 3Available at https://github.com/USC-NSL/Oboe 50

**Fragmento 4 - p. 10 - score 8:**

HYB. The performance of HYB is sensitive to the choice of 𝛽parameter, which HYB+Oboe tunes. In production, HYB uses 𝛽= 0.25, determined using A/B tests in a large-scale de- ployment. Figure 14(c) and 14(d) show CDFs of per session performance improvement of average bitrate and rebuffer- ing ratio over HYB. As with BOLA, HYB+Oboe maintains similar rebuffering ratios as shown in 14(d), but improves bitrates for 98% of sessions with an overall average bitrate improvement of 8.32% in average across all sessions. 4.6 Sensitivity experiments Alternative throughput traces. To understand how Oboe works on throughput datasets beyond those discussed in §4.2, we evaluated Oboe on two other datasets, FCC [8] and HS- DPA [46] that have been used in recent work [39, 59].

**Fragmento 5 - p. 11 - score 7:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 16—Comparing HYB with multiple fixed configurations and HYB+Oboe for various settings these traces. Our results show that MPC+Oboe continues to perform better than RobustMPC on these traces. Further, rela- tive to Pensieve, MPC+Oboe improves QoE-lin by an aver- age of 6.94% across the FCC dataset and 10.92% across the HSDPA dataset. These improvements are more modest than those in Figure 9(a). The vast majority of traces in the FCC and HSDPA set have an average throughput under 3 Mbps (over 95% for FCC and 98% for HSDPA). The results cor- roborate Figure 12 which indicates that MPC+Oboe provides more modest gains over Pensieve when the latter is trained and evaluated on datasets with a narrow throughput range.

**Fragmento 6 - p. 7 - score 6:**

Our client runs the Dash.js video player (version 1.2), a reference player implemented in JavaScript by the MPEG-DASH forum [7]. We modified Dash.js to send client player state information (e.g. buffer length, video play state and throughput measurements) to Oboe (§5). This player runs on the Google Chrome browser (version 61) in our experiments. In §5, we show that Oboe can also be run as a cloud service. Testbed setup. Our evaluations measure ABR performance by delivering a video stream (the “EnvivioDash3” video from the MPEG-DASH reference videos [12]) from a video host- ing server to a client, while varying network conditions us- ing throughput traces from real user sessions. We use bi- trates {300, 750, 1200, 1850, 2850, 4300}𝑘𝑏𝑝𝑠with a 4 sec- ond chunk duration and total length of 192 seconds.

**Fragmento 7 - p. 7 - score 6:**

We focus on this video as it has been used in prior work [39], and we do not consider videos of longer duration because we only have throughput traces available for a video publisher that serves short music videos (as we discuss below). The video is hosted on an Apache server. Both the server and client software run on the same 8-core, 4 Ghz, Intel i7 commodity desktop with 12 GB RAM running Ubuntu 16.04. Between server and client, we emulate different network conditions using the Chrome DevTools API [9]. This allows us to control the upload/download throughput as well as latency using the Chrome-Remote-Interface based on throughput traces [5]. We use 571 throughput traces3 from our dataset (discussed below) for this emulation.

**Fragmento 8 - p. 2 - score 5:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 9 - p. 3 - score 5:**

A key reason for this is that ABR algorithms have parameters (which we henceforth refer to as configurations) that must be set in a manner sensitive to network conditions. ABR algorithms need to run on many different networks, rang- ing from cellular and WiFi networks at one end, to high-speed broadband connections at the other. Given this diversity, net- work conditions can vary significantly. Packet loss conditions can vary by an order of magnitude or more across the globe [25]. Network throughputs can also vary widely: for 90% of traces in a large dataset, the trace’s maximum throughput is more than twice its average throughput. Yet, unfortunately, most ABR algorithms today either employ fixed configura- tions or simple heuristics to adapt these configurations (§2.1).

**Fragmento 10 - p. 4 - score 5:**

We analyze throughput traces using the Augmented Dickey-Fuller (ADF [26]) test, a hypothesis test to check for stationarity in a time series. Our evaluations on a dataset of 15,000 video streaming throughput traces show that 59.5% were non-stationary (see §4.2 for details of the dataset), imply- ing the presence of distinct mean and/or variance in different segments of the traces. However, prior work [17, 35, 38, 52, 60] shows that TCP connection throughput can be modeled as a piecewise sta- tionary process; the connection consists of multiple non- overlapping segments where each segment is stationary and often lasts for tens of seconds or minutes (e.g., Figure 8). Moreover, Zhang et al. [60] show that the throughput in each segment may be modeled as an i.i.d.

**Fragmento 11 - p. 8 - score 5:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 6—The percentage improvement in QoE-lin of MPC+Oboe over RobustMPC for the Testbed experiment. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 7—QoE-lin of MPC+Oboe compared to RobustMPC of tracking the performance of the actual ABR algorithms. For instance, Figure 5(a) and 5(b) demonstrates this for the HYB algorithm. The figures shows the correlation for the average bitrate and rebuffering ratio for 100 throughput traces randomly sampled from our dataset using HYB on the VirtualPlayer compared to using an actual Dash.js player. For both metrics, the graph closely tracks the 𝑦= 𝑥line indicating close correlation.

**Fragmento 12 - p. 14 - score 5:**

Why Should I Trust You?: Explaining the Predictions of Any Classifier. In Proceedings of the ACM International Conference on Knowledge Discovery and Data Mining, SIGKDD, 2016. [46] Haakon Riiser, Paul Vigmostad, Carsten Griwodz, and Pål Halvorsen. Commute Path Bandwidth Traces from 3G Networks: Analysis and Applications. In Pro- ceedings of the ACM Multimedia Systems Conference, MMSys, 2013. [47] Jeffrey Semke, Jamshid Mahdavi, and Matthew Mathis. Automatic TCP Buffer Tuning. In Proceedings of the ACM Conference on Special Interest Group on Data Communication, SIGCOMM, 1998. [48] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K Sitaraman. BOLA: Near-optimal Bitrate Adaptation for Online Videos. In Proceedings of the IEEE International Conference on Computer Communications, INFOCOM, 2016.

**Fragmento 13 - p. 3 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces throughput prediction errors, a more conservative version, Ro- bustMPC, reduces predicted throughput by a discount factor 1+𝑑, where 𝑑is the maximum error in throughput predictions experienced in the last five chunk downloads. BOLA: Buffer occupancy, selects bitrate by solving an optimization problem. BOLA is a buffer-based algorithm used in Dash.js [7], so it does not employ throughput pre- diction in making bitrate decisions [48].

**Fragmento 14 - p. 8 - score 4:**

Given these close correlations, we use the VirtualPlayer in §4.7 to explore Oboe’s performance over a larger range of diverse settings and our entire set of traces. 4.3 Oboe with RobustMPC We now demonstrate that Oboe can be used to auto-tune Ro- bustMPC, the best performing variant of the MPC algorithms. The resulting MPC+Oboe uses the best value of the discount parameter 𝑑corresponding to the current network state, re- placing RobustMPC’s online adaptation based on throughput estimates obtained over the past 5 chunks (§2). Figure 6(a) shows the CDF of the percentage improvement in QoE-lin of MPC+Oboe over RobustMPC.4 MPC+Oboe improves QoE-lin for 71% of sessions, with an overall av- erage QoE-lin improvement of 17.62% across all sessions.

**Fragmento 15 - p. 9 - score 4:**

Figure 10 shows CDFs of QoE-lin for the pretrained (Original) model and the model trained by us (Retrained). The performance distribution of the two models are almost identical over the test traces provided by the Pensieve authors, thereby validating our retraining methodology. Having validated our retraining methodology, we trained Pensieve on our dataset with the same complete strategy described above. For this, we pick 1600 traces randomly from our dataset with average throughput in the 0-6 Mbps range. The number of training traces, the number of iterations per trace, and the range of throughput are similar to [39]. We then compare Pensieve and MPC+Oboe over a separate test set of traces also in the range of 0-6 Mbps (§4.2).

**Fragmento 16 - p. 11 - score 4:**

Figure 16(a) shows that HYB+Oboe outperforms HYB in the sense that there is no fixed configuration for HYB that does better than HYB+Oboe performance. HYB+Oboe improves the average bitrates of the median session by 3.2%, while achieving similar rebuffering ratio. Alternately, it re- duces the 90th percentile rebuffering ratio from 1.9% to 0%, while maintaining similar bitrates. A similar result holds for mobile traces (Figure 16(b)). Thus, even if publishers were to find the best fixed parameter choice for HYB, Oboe would outperform that choice because it dynamically adapts the parameters. Comparison under different publisher specifications. Our results so far are for a VoD (video on demand) setting with a maximum buffer size of 2 minutes.

**Fragmento 17 - p. 2 - score 3:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 18 - p. 2 - score 3:**

Publishers, content delivery networks, and users all seek to improve user quality of experience (QoE). There are many factors that affect QoE including start up latency, the average bitrate for a video session, as well as the rebuffering ratio (the percentage of time playback is stalled because of drained buffer) [23]. Video players improve QoE using adaptive bitrate (ABR) algorithms which select bitrates for each chunk while (1) ensuring the bitrate seen by the user is as high as possible and (2) avoiding rebuffering events at the client. Some ABR algorithms may also try to minimize the number of bitrate switches to make the playback smooth. Content publishers serve different types of content includ- ing VoD (Video on Demand) or Live broadcasts.

**Fragmento 19 - p. 3 - score 3:**

Figures 1(a) and 1(b) show how the choice of ABR config- uration depends on network conditions. Figure 1(a) shows the bitrate and rebuffering ratio for two client sessions with the HYB algorithm for three different values of its 𝛽parameter, Cons (Conservative), Mod (Moderate), and Aggr (Aggres- sive). The throughput behavior of the two sessions is shown in Figure 1(c). If a publisher prefers to eliminate rebuffering, Mod is suitable for session A, but Cons is better for session B. Figure 1(b) shows that BOLA behaves similarly, with Mod being the preferred setting for session A and Cons for session B, to avoid rebuffering. Figures 2(a) and 2(b) show the difficulty in setting the discount factor with MPC, by comparing the performance of FastMPC (no discount factor), and RobustMPC (discount factor set by local heuristic) for two throughput traces with different characteristics.

**Fragmento 20 - p. 4 - score 3:**

3 OBOE DESIGN Oboe aims to ensure good QoE for all users by enabling ABR algorithms to perform better across a wide range of network conditions. The configurations of many ABR algorithms are sensitive to network state, specifically to the value and vari- ability of the available throughput between the client and the video server. For example, 𝛽in HYB should be smaller when available throughput is highly variable, while 𝛾in BOLA should be higher. This explains why the algorithms perform differently for different values of parameters on a given client trace (§2.2). However, a line of prior work [17, 35, 38, 52, 60] has observed that network connections are piecewise station- ary: that is, connections can be in one of several distinct states (§3.1), where each state is distinguished by stationarity in the statistical sense (informally, a process is stationary if its sta- tistical properties including mean and variance do not change over time - see [43] for a more formal definition).

**Fragmento 21 - p. 4 - score 3:**

3.1 Representing Network State Most ABR algorithms today adapt bitrates based on the throughput (more precisely, goodput) achieved by recently Figure 3—The logical diagram of the offline pipeline used by Oboe downloaded chunks. This perceived throughput already ac- counts for network delays and loss-rates, as well as the dy- namics of the underlying transport protocol. The network throughput along a path is not necessarily a stationary process [17, 35, 38, 52, 60]: flows at the bottleneck along a path may change over time resulting in changes to available throughput, or the bottleneck itself may shift [35]. An analysis of the throughput traces used in our evaluations (§4) confirms the lack of stationarity when applied to the en- tire trace.

**Fragmento 22 - p. 5 - score 3:**

The VirtualPlayer also takes into account publisher spec- ifications for bitrate levels, player buffer sizes (determined by time-to-live requirements) and chunk size. These spec- ifications are used by VirtualPlayer when it executes ABR algorithms on the input traces, ensuring that the resulting Con- figMap meets the publisher specifications. Finally, Oboe also allows the publisher to optionally express an explicit QoE tradeoff such as maintaining the rebuffering under a desired threshold 𝑥%. Oboe derives a ConfigMap that meets the re- buffering threshold in a best effort manner. We evaluate the efficacy of this flexibility in §4.7. Building the ConfigMap using ConfigSelector. To build the ConfigMap, the ConfigEvaluator drives the exploration of different configurations for an ABR algorithm.

**Fragmento 23 - p. 9 - score 3:**

Our exper- iments use the Pensieve implementation provided by the authors [11]. Pensieve Re-Training and Validation. Before evaluating Pensieve on our dataset, we retrain Pensieve using the source code on the trace dataset provided by the Pensieve authors [11]. This helps us validate our retraining given that deep reinforcement learning results are not easy to reproduce [29]. We experimented with five different initial entropy weights in the author suggested range of 1 to 5, and linearly reduced their values in a gradual fashion using plateaus, with five different decrease rates until the entropy weight eventually reached 0.1. This rate scheduler follows best-practice [55]. From the trained set of models, we then selected the best performing model (an initial entropy weight of 1 reduced every 800 iterations until it reaches 0.1 over 100K iterations) and compared its performance to the pre-trained Pensieve model provided by the authors.

**Fragmento 24 - p. 11 - score 3:**

Our experi- ments were conducted in simulation, using the VirtualPlayer, and the testbed experiment traces (§4.2). Figure 15 shows the average QoE-lin across the traces for RobustMPC and MPC+Oboe using both the default har- monic mean approach and Ideal(T) for different values of T. Although RobustMPC performs better with an ideal predictor, Oboe still provides benefits, achieving an average improve- ment in QoE-lin of 6.34% for Ideal(5) and of 1.8% for Ideal(10), compared to a 16.1% improvement with the har- monic mean estimator. While the magnitude of benefits is smaller with the ideal prediction approach, in practice Oboe will likely result in larger benefits, since even more sophisti- cated schemes [49] cannot achieve the ideal predictions, and the errors are likely to grow with larger T.

**Fragmento 25 - p. 11 - score 3:**

MPC+Oboe provides larger gains in settings like the traces discussed in §4.2, where only 41% traces are under 3 Mbps and 59% are in the 3-6 Mbps range. Alternative throughput prediction methods. Our experi- ments with RobustMPC rely on throughput prediction based on the harmonic mean of prior throughput samples (follow- ing earlier work [39, 59]), with Oboe tuning the configura- tion to compensate for prediction errors. We next consider if Oboe’s benefits hold if RobustMPC were to have more accurate throughput predictions, potentially by using alter- nate prediction methods [49]. Rather than using a specific prediction technique, we consider an ideal (and unachievable) approach that we denote as Ideal(T), which can exactly predict the average throughput over the next T seconds.

**Fragmento 26 - p. 12 - score 3:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 17—Avg. of avg. bitrate and fraction of sessions with rebuffering for HYB+Oboe and different publisher pref- erences Figure 18—Avg. of avg. bitrate and fraction of sessions with rebuffering for RobustMPC and different publisher preferences depicts performance for live video (which uses a maximum buffer size of 20 seconds to mimic live settings). HYB+Oboe outperforms HYB for this setting, though we note that the bitrate of both approaches degrades relative to the VoD setting since the baseline HYB switches to higher bitrates more conservatively owing to the smaller buffer sizes. Finally, Figure 16(d) depicts performance for higher bi- trate levels ({1002, 1434, 2738, 3585, 4661, 5886}𝑘𝑏𝑝𝑠) and a chunk size of 5 seconds.


### 7.7. evaluacion baselines experimentos

Palabras clave usadas: `evaluation, experiment, experiments, baseline, baselines, compare, comparison, Pensieve, BBA, BOLA, MPC, RobustMPC, FastMPC, A3C, PPO, DQN, SODA, Oboe, MetaABR, results, outperform, ablation, scenario, test`

**Fragmento 1 - p. 2 - score 7:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 2 - p. 6 - score 7:**

Given these sources of uncertainty, Oboe chooses to be safe in its selec- tion of the best configuration for 𝑠. Finally, ReconfEngine configures the ABR algorithm, and the reconfigured ABR algorithm is ready to compute the bitrate decision to be used for the next chunk at this point. 4 EVALUATION In this section, we demonstrate Oboe’s ability to auto-tune three existing algorithms: RobustMPC, BOLA and HYB. We also compare an Oboe-tuned RobustMPC to Pensieve [39]. 4.1 Metrics The performance of a video session depends on multiple fac- tors. Average bitrate and rebuffering ratio were found to have the most impact on user quality of experience [23], though other factors such as changes in bitrates during a session can play a role [23].

**Fragmento 3 - p. 10 - score 7:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d) Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors Pensieve is 19.9%. This indicates specializing the model does improve Pensieve’s performance. Thus, Pensieve’s model is as yet unable to create special- ized versions of itself based on the session characteristics. By contrast, Oboe specializes parameters for every network state and therefore performs better. We have also validated Pensieve’s inability to specialize in several other ways: build- ing a model for the 3-6 Mbps and showing that it performs better with test data in that range compared to a 0-6 Mbps model; checking that a 0-6 Mbps model performs better for data in that range compared to a 0-100 Mbps model; and ensuring that these results hold even when the training set is doubled.

**Fragmento 4 - p. 2 - score 6:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 5 - p. 7 - score 6:**

We filtered out traces which were too short for playing our entire 192 second video, after which we obtained 5K traces from wired desktops and 4K sessions from WiFi or 3G/4G mobile devices. Our testbed experiments use a subset of 571 traces with roughly the same number of traces sampled from each of desktop and mobile clients. VirtualPlayer setup. Recall that Oboe uses the Virtu- alPlayer to obtain a ConfigMap for any ABR algorithm. Since the majority of our results use an actual testbed with the Dash.js player, the benefits of Oboe in our evaluation results already arise despite any inaccuracies in building the ConfigMap on account of using the VirtualPlayer. That said, we have also verified that the VirtualPlayer does a good job 3Available at https://github.com/USC-NSL/Oboe 50

**Fragmento 6 - p. 7 - score 6:**

The underlying factors represent concrete application performance that publishers understand how to reason about. Moreover, a unified metric like QoE-lin can obscure important differences. For example, two sessions may have the same QoE-lin but different performance in underlying metrics, leading to varied user experience. So, we also present graphs of these metrics. 4.2 Methodology Implementation. For RobustMPC, we used the imple- mentation available at [11]. Our implementation of BOLA [@bola] is from the Dash.js player. The implementation of HYB is a variant of the algorithm used in a large-scale deployment. These ABR algorithms and Oboe’s online stage (change point detection and ABR reconfiguration) run on the server in our experiments.

**Fragmento 7 - p. 8 - score 6:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 6—The percentage improvement in QoE-lin of MPC+Oboe over RobustMPC for the Testbed experiment. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 7—QoE-lin of MPC+Oboe compared to RobustMPC of tracking the performance of the actual ABR algorithms. For instance, Figure 5(a) and 5(b) demonstrates this for the HYB algorithm. The figures shows the correlation for the average bitrate and rebuffering ratio for 100 throughput traces randomly sampled from our dataset using HYB on the VirtualPlayer compared to using an actual Dash.js player. For both metrics, the graph closely tracks the 𝑦= 𝑥line indicating close correlation.

**Fragmento 8 - p. 8 - score 6:**

This results in a rebuffering event 44 seconds into the session (lowest graph shows buffer occupancy with 0 indicating a rebuffering event). In contrast, MPC+Oboe does not incur a rebuffering event and maintains a fixed 𝑑during the initial stable state. At 29 sec, it detects a change in the network state and adapts its discount factor, leading to more conservative bitrate selections. 4.4 Oboe vs. Pensieve Pensieve [39] uses deep reinforcement learning [41, 42], a combination of deep learning with reinforcement learn- ing [50], and has been shown to outperform existing ABRs, including RobustMPC [39] in some settings. Since 51

**Fragmento 9 - p. 9 - score 6:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 10—Validation of our training methodology for Pensieve. Figure 11—QoE-lin of MPC+Oboe compared to Pensieve Figure 12—Benefits of specializing Pensieve models. Each curve shows the QoE improvement of MPC+Oboe rela- tive to each Pensieve model. Figure 13—QoE improvement of MPC+Oboe over two ways of dy- namically selecting from specialized Pensieve models. MPC+Oboe outperforms RobustMPC as well, we explore how MPC+Oboe performs relative to Pensieve.

**Fragmento 10 - p. 10 - score 6:**

FCC is a broadband dataset, while HSDPA contains throughput traces collected from video streaming sessions over 3G net- works in Norway using mobile devices. Our comparisons use the traces and a Pensieve model pre-trained for those traces available at [11]. We focus our evaluations on MPC+Oboe and Pensieve, given that Pensieve has been shown to out- perform existing ABR schemes including RobustMPC on 53

**Fragmento 11 - p. 11 - score 6:**

For these experiments, we use the VirtualPlayer described in §3.2. Comparison against all fixed configurations. To explore different fixed configurations, we run HYB with 10 different fixed 𝛽s and compare with HYB+Oboe. We summarize the performance for each configuration by considering the (i) median of the average bitrate and the (ii) 90th percentile of the rebuffering ratio across test traces. In this experiment, we also consider an Oracle which is the best fixed configuration for each throughput trace with respect to two metrics that HYB tries to optimize. Figure 16(a) and 16(b) compare HYB, HYB+Oboe and Oracle over desktop, and mobile traces respectively. While Oracle and HYB+Oboe are depicted as single dots since their performance is uniquely determined, we present a frontier for HYB that shows its performance for different fixed con- figuration.

**Fragmento 12 - p. 11 - score 6:**

Our experi- ments were conducted in simulation, using the VirtualPlayer, and the testbed experiment traces (§4.2). Figure 15 shows the average QoE-lin across the traces for RobustMPC and MPC+Oboe using both the default har- monic mean approach and Ideal(T) for different values of T. Although RobustMPC performs better with an ideal predictor, Oboe still provides benefits, achieving an average improve- ment in QoE-lin of 6.34% for Ideal(5) and of 1.8% for Ideal(10), compared to a 16.1% improvement with the har- monic mean estimator. While the magnitude of benefits is smaller with the ideal prediction approach, in practice Oboe will likely result in larger benefits, since even more sophisti- cated schemes [49] cannot achieve the ideal predictions, and the errors are likely to grow with larger T.

**Fragmento 13 - p. 7 - score 5:**

Our client runs the Dash.js video player (version 1.2), a reference player implemented in JavaScript by the MPEG-DASH forum [7]. We modified Dash.js to send client player state information (e.g. buffer length, video play state and throughput measurements) to Oboe (§5). This player runs on the Google Chrome browser (version 61) in our experiments. In §5, we show that Oboe can also be run as a cloud service. Testbed setup. Our evaluations measure ABR performance by delivering a video stream (the “EnvivioDash3” video from the MPEG-DASH reference videos [12]) from a video host- ing server to a client, while varying network conditions us- ing throughput traces from real user sessions. We use bi- trates {300, 750, 1200, 1850, 2850, 4300}𝑘𝑏𝑝𝑠with a 4 sec- ond chunk duration and total length of 192 seconds.

**Fragmento 14 - p. 9 - score 5:**

Finally, Figure 11 shows the CDF of QoE-lin for MPC+Oboe and Pensieve, and indicates MPC+Oboe per- forms distributionally better. Analyzing Pensieve performance. To understand where these performance improvements were coming from, we ex- amined the relative performance of these two schemes in the 0-3 Mbps range (i.e., traces having an average throughput be- tween 0-3 Mbps). In this more constrained range of network conditions, we found that MPC+Oboe achieves bigger gains over Pensieve (average QoE-lin improvement in 0-3 Mbps is 46.23%). We hypothesize that this performance difference stems from the fact that Pensieve builds a single model which does not specialize to different throughput ranges. To test this, we trained a separate Pensieve model only with traces that have an average throughput between 0-3 Mbps range and compared it with MPC+Oboe.

**Fragmento 15 - p. 9 - score 5:**

Comparison with Pensieve. Figure 9(a) shows the CDF of the percentage improvement in QoE-lin for MPC+Oboe over Pensieve. MPC+Oboe outperforms Pensieve for 81% of the sessions, with a QoE-lin improvement of 23.9% in aver- age across all sessions. 25% of the sessions achieve more than 20% QoE-lin improvement. For the sessions MPC+Oboe is unable to improve over Pensieve, the performance differ- ence is mostly less than 5%. Figures 9(b), 9(c) and 9(d) show that MPC+Oboe distributionally outperforms Pensieve with respect to all underlying metrics. It reduces the number of sessions with rebuffering from 10.7% to 5.3%, reduces the median per chunk change magnitude by 43.9%, and improves median and 95th percentile average bitrate by 2.6% and 4.7% respectively.

**Fragmento 16 - p. 9 - score 5:**

Figure 10 shows CDFs of QoE-lin for the pretrained (Original) model and the model trained by us (Retrained). The performance distribution of the two models are almost identical over the test traces provided by the Pensieve authors, thereby validating our retraining methodology. Having validated our retraining methodology, we trained Pensieve on our dataset with the same complete strategy described above. For this, we pick 1600 traces randomly from our dataset with average throughput in the 0-6 Mbps range. The number of training traces, the number of iterations per trace, and the range of throughput are similar to [39]. We then compare Pensieve and MPC+Oboe over a separate test set of traces also in the range of 0-6 Mbps (§4.2).

**Fragmento 17 - p. 10 - score 5:**

HYB. The performance of HYB is sensitive to the choice of 𝛽parameter, which HYB+Oboe tunes. In production, HYB uses 𝛽= 0.25, determined using A/B tests in a large-scale de- ployment. Figure 14(c) and 14(d) show CDFs of per session performance improvement of average bitrate and rebuffer- ing ratio over HYB. As with BOLA, HYB+Oboe maintains similar rebuffering ratios as shown in 14(d), but improves bitrates for 98% of sessions with an overall average bitrate improvement of 8.32% in average across all sessions. 4.6 Sensitivity experiments Alternative throughput traces. To understand how Oboe works on throughput datasets beyond those discussed in §4.2, we evaluated Oboe on two other datasets, FCC [8] and HS- DPA [46] that have been used in recent work [39, 59].

**Fragmento 18 - p. 11 - score 5:**

Oboe can improve performance over RobustMPC even when an Ideal(T) prediction method is used for two reasons. First, 𝑇may not match the duration of chunk downloads with RobustMPC, which depends on the exact sequence of bitrates chosen during the look-ahead window. The duration is not known a priori, since RobustMPC itself determines the bitrates based on a provided prediction. Second, the decisions made by RobustMPC are over a small look-ahead window, which may not guarantee optimality over the entire session duration. 4.7 Oboe Across Various Settings In §4.5 we have shown that Oboe outperforms other ABR algorithms when compared to their default configurations. We now explore, for HYB, whether Oboe outperforms all parameter settings of HYB and whether it can tune ABRs based on content type and publisher specifications.

**Fragmento 19 - p. 11 - score 5:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 16—Comparing HYB with multiple fixed configurations and HYB+Oboe for various settings these traces. Our results show that MPC+Oboe continues to perform better than RobustMPC on these traces. Further, rela- tive to Pensieve, MPC+Oboe improves QoE-lin by an aver- age of 6.94% across the FCC dataset and 10.92% across the HSDPA dataset. These improvements are more modest than those in Figure 9(a). The vast majority of traces in the FCC and HSDPA set have an average throughput under 3 Mbps (over 95% for FCC and 98% for HSDPA). The results cor- roborate Figure 12 which indicates that MPC+Oboe provides more modest gains over Pensieve when the latter is trained and evaluated on datasets with a narrow throughput range.

**Fragmento 20 - p. 12 - score 5:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 17—Avg. of avg. bitrate and fraction of sessions with rebuffering for HYB+Oboe and different publisher pref- erences Figure 18—Avg. of avg. bitrate and fraction of sessions with rebuffering for RobustMPC and different publisher preferences depicts performance for live video (which uses a maximum buffer size of 20 seconds to mimic live settings). HYB+Oboe outperforms HYB for this setting, though we note that the bitrate of both approaches degrades relative to the VoD setting since the baseline HYB switches to higher bitrates more conservatively owing to the smaller buffer sizes. Finally, Figure 16(d) depicts performance for higher bi- trate levels ({1002, 1434, 2738, 3585, 4661, 5886}𝑘𝑏𝑝𝑠) and a chunk size of 5 seconds.

**Fragmento 21 - p. 13 - score 5:**

Picking configurations in a manner informed by network state and publisher preferences distin- guishes Oboe’s approach from heuristics used today that do not consider these factors. Oboe significantly improves the performance of BOLA, HYB and RobustMPC; further, for nearly 80% of the sessions in our dataset, Oboe integrated with RobustMPC improves QoE-lin relative to Pensieve and the improvements exceed 20% for 25% of the sessions. Acknowledgments. We thank our shepherd, Mohammad Al- izadeh and the anonymous reviewers for their constructive feedback. We thank Oleg White, Yan Li and Shubo Liu for their assistance obtaining the throughput data and for helpful discussions. This work was funded in part by the National Science Foundation (NSF) Awards CNS-1618921, CNS-1564242, and CNS-1413978; and the ARO, under the U.S.

**Fragmento 22 - p. 1 - score 4:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 23 - p. 3 - score 4:**

Figures 1(a) and 1(b) show how the choice of ABR config- uration depends on network conditions. Figure 1(a) shows the bitrate and rebuffering ratio for two client sessions with the HYB algorithm for three different values of its 𝛽parameter, Cons (Conservative), Mod (Moderate), and Aggr (Aggres- sive). The throughput behavior of the two sessions is shown in Figure 1(c). If a publisher prefers to eliminate rebuffering, Mod is suitable for session A, but Cons is better for session B. Figure 1(b) shows that BOLA behaves similarly, with Mod being the preferred setting for session A and Cons for session B, to avoid rebuffering. Figures 2(a) and 2(b) show the difficulty in setting the discount factor with MPC, by comparing the performance of FastMPC (no discount factor), and RobustMPC (discount factor set by local heuristic) for two throughput traces with different characteristics.

**Fragmento 24 - p. 4 - score 4:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the left graph, although the throughput is generally good, the sudden variations force RobustMPC to make overly conserva- tive bitrate decisions, as well as incur more bitrate switches. (bottom subgraph). In contrast, in Figure 2(b), the quicker and more frequent throughput changes (top subgraph) result in FastMPC experiencing rebuffering (middle subgraph), while RobustMPC does not. This is just one example illustrating the difficulty in picking parameters – in our evaluations (§4), we found that RobustMPC was itself too aggressive when selecting discount factors for some traces. While this section uses synthetic traces for illustrative pur- poses, our evaluations with real traces (§4) more extensively demonstrate the limitations of current approaches with re- spect to selecting parameters and the benefits of automatically tuning ABR parameters to network conditions.

**Fragmento 25 - p. 7 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 5—A scatter plot of average bitrate and rebuffering ratio between the Virtu- alPlayer and real Dash.js player and BOLA primarily maximize average bitrate subject to low rebuffering. In contrast, other algorithms [39, 59] have been designed to optimize a QoE metric which is a linear combina- tion of bitrate, rebuffering and bitrate changes (smoothness). With Oboe, our primary evaluation goal is to demonstrate the extent to which it can improve the underlying metrics that an ABR algorithm is designed for. Thus, our evaluations with BOLA and HYB focus on average bitrate and rebuffering, while those with MPC+Oboe focus on the linear combination of QoE (which we refer to as QoE-lin, [59]), defined as follows.

**Fragmento 26 - p. 8 - score 4:**

In particular, for 19% of the sessions, QoE-lin improves by more than 20%. For the sessions MPC+Oboe is unable to improve RobustMPC, its performance degradation is mostly under 8%. Figures 6(b), 6(c) and 6(d) show the constituent QoE metrics. While MPC+Oboe achieves distributionally sim- ilar bitrates as RobustMPC as shown in 6(b), it significantly reduces rebuffering across sessions: the number of sessions with rebuffering reduces from 33.2% to 5.3%. Further, it also achieves better playback smoothness by improving the 4The increase in QoE-lin over RobustMPC relative to the absolute QoE-lin value of RobustMPC expressed as a percentage. Figure 8—An example session showing how MPC+Oboe is able to outperform Ro- bustMPC by reconfiguring the discount parameter when a network state change is de- tected.


### 7.8. resultados numericos metricas

Palabras clave usadas: `improvement, improve, gain, reduce, reduction, %, QoE gain, higher, lower, average, median, percentile, stall time, latency, overhead, accuracy, significant, p95, p99, score, ratio, duration`

**Fragmento 1 - p. 9 - score 7:**

Comparison with Pensieve. Figure 9(a) shows the CDF of the percentage improvement in QoE-lin for MPC+Oboe over Pensieve. MPC+Oboe outperforms Pensieve for 81% of the sessions, with a QoE-lin improvement of 23.9% in aver- age across all sessions. 25% of the sessions achieve more than 20% QoE-lin improvement. For the sessions MPC+Oboe is unable to improve over Pensieve, the performance differ- ence is mostly less than 5%. Figures 9(b), 9(c) and 9(d) show that MPC+Oboe distributionally outperforms Pensieve with respect to all underlying metrics. It reduces the number of sessions with rebuffering from 10.7% to 5.3%, reduces the median per chunk change magnitude by 43.9%, and improves median and 95th percentile average bitrate by 2.6% and 4.7% respectively.

**Fragmento 2 - p. 11 - score 6:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 16—Comparing HYB with multiple fixed configurations and HYB+Oboe for various settings these traces. Our results show that MPC+Oboe continues to perform better than RobustMPC on these traces. Further, rela- tive to Pensieve, MPC+Oboe improves QoE-lin by an aver- age of 6.94% across the FCC dataset and 10.92% across the HSDPA dataset. These improvements are more modest than those in Figure 9(a). The vast majority of traces in the FCC and HSDPA set have an average throughput under 3 Mbps (over 95% for FCC and 98% for HSDPA). The results cor- roborate Figure 12 which indicates that MPC+Oboe provides more modest gains over Pensieve when the latter is trained and evaluated on datasets with a narrow throughput range.

**Fragmento 3 - p. 11 - score 6:**

Figure 16(a) shows that HYB+Oboe outperforms HYB in the sense that there is no fixed configuration for HYB that does better than HYB+Oboe performance. HYB+Oboe improves the average bitrates of the median session by 3.2%, while achieving similar rebuffering ratio. Alternately, it re- duces the 90th percentile rebuffering ratio from 1.9% to 0%, while maintaining similar bitrates. A similar result holds for mobile traces (Figure 16(b)). Thus, even if publishers were to find the best fixed parameter choice for HYB, Oboe would outperform that choice because it dynamically adapts the parameters. Comparison under different publisher specifications. Our results so far are for a VoD (video on demand) setting with a maximum buffer size of 2 minutes.

**Fragmento 4 - p. 2 - score 5:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 5 - p. 9 - score 5:**

Finally, Figure 11 shows the CDF of QoE-lin for MPC+Oboe and Pensieve, and indicates MPC+Oboe per- forms distributionally better. Analyzing Pensieve performance. To understand where these performance improvements were coming from, we ex- amined the relative performance of these two schemes in the 0-3 Mbps range (i.e., traces having an average throughput be- tween 0-3 Mbps). In this more constrained range of network conditions, we found that MPC+Oboe achieves bigger gains over Pensieve (average QoE-lin improvement in 0-3 Mbps is 46.23%). We hypothesize that this performance difference stems from the fact that Pensieve builds a single model which does not specialize to different throughput ranges. To test this, we trained a separate Pensieve model only with traces that have an average throughput between 0-3 Mbps range and compared it with MPC+Oboe.

**Fragmento 6 - p. 10 - score 5:**

4.5 Oboe with other ABR Algorithms Oboe can also improve other existing ABR algorithms such as BOLA and HYB, which are designed to maximize average bitrate while minimizing rebuffering. BOLA. BOLA+Oboe tunes 𝛾(§2), which determines how much the algorithm strives to avoid rebuffering. BOLA, as implemented in Dash.js, uses a fixed default value of 𝛾= −10.28. Figure 14(a) and 14(b) show CDFs of per session performance improvement over BOLA with respect to av- erage bitrate and rebuffering ratio. BOLA+Oboe maintains the rebuffering ratio of BOLA while improving average bi- trates for more than 83% of sessions with an overall increase of 7.2% in average across all sessions. For sessions where BOLA+Oboe does not outperform BOLA, its degradation is less than 3.1%.

**Fragmento 7 - p. 10 - score 5:**

HYB. The performance of HYB is sensitive to the choice of 𝛽parameter, which HYB+Oboe tunes. In production, HYB uses 𝛽= 0.25, determined using A/B tests in a large-scale de- ployment. Figure 14(c) and 14(d) show CDFs of per session performance improvement of average bitrate and rebuffer- ing ratio over HYB. As with BOLA, HYB+Oboe maintains similar rebuffering ratios as shown in 14(d), but improves bitrates for 98% of sessions with an overall average bitrate improvement of 8.32% in average across all sessions. 4.6 Sensitivity experiments Alternative throughput traces. To understand how Oboe works on throughput datasets beyond those discussed in §4.2, we evaluated Oboe on two other datasets, FCC [8] and HS- DPA [46] that have been used in recent work [39, 59].

**Fragmento 8 - p. 11 - score 5:**

For these experiments, we use the VirtualPlayer described in §3.2. Comparison against all fixed configurations. To explore different fixed configurations, we run HYB with 10 different fixed 𝛽s and compare with HYB+Oboe. We summarize the performance for each configuration by considering the (i) median of the average bitrate and the (ii) 90th percentile of the rebuffering ratio across test traces. In this experiment, we also consider an Oracle which is the best fixed configuration for each throughput trace with respect to two metrics that HYB tries to optimize. Figure 16(a) and 16(b) compare HYB, HYB+Oboe and Oracle over desktop, and mobile traces respectively. While Oracle and HYB+Oboe are depicted as single dots since their performance is uniquely determined, we present a frontier for HYB that shows its performance for different fixed con- figuration.

**Fragmento 9 - p. 12 - score 5:**

We have also analyzed the processing over- head incurred by the ChangeDetector module of Oboe. We measure the time taken by ChangeDetector for every decision 5We used a change penalty of 0 for fair comparison. Figure 19—Comparing prototype Oboe with commercial client side ABR implemen- tation in average bitrate and rebuffering ratio. Figure 20—Time between consecutive bitrate switches for two commercial ABRs Figure 21—Variance in bitrate levels across videos from two content publish- ers. cycle across our experiments, and the measurement indicates that the median processing time of ChangeDetector is around 14 ms. Since each decision is made at a chunk boundary and chunks are 4 seconds, ChangeDetector accounts for less than 0.35% overhead.

**Fragmento 10 - p. 13 - score 5:**

Picking configurations in a manner informed by network state and publisher preferences distin- guishes Oboe’s approach from heuristics used today that do not consider these factors. Oboe significantly improves the performance of BOLA, HYB and RobustMPC; further, for nearly 80% of the sessions in our dataset, Oboe integrated with RobustMPC improves QoE-lin relative to Pensieve and the improvements exceed 20% for 25% of the sessions. Acknowledgments. We thank our shepherd, Mohammad Al- izadeh and the anonymous reviewers for their constructive feedback. We thank Oleg White, Yan Li and Shubo Liu for their assistance obtaining the throughput data and for helpful discussions. This work was funded in part by the National Science Foundation (NSF) Awards CNS-1618921, CNS-1564242, and CNS-1413978; and the ARO, under the U.S.

**Fragmento 11 - p. 13 - score 5:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary We expected a cloud implementation would perform worse because of the latency induced by client-server communica- tion. However, we found that most of the bitrate switching decisions occur on timescales much longer than the client- server latencies. Figure 20 shows the CDF of the time interval between consecutive bitrate switches for ABR algorithms in two widely used video players(Adobe’s Flash [3] and Mi- crosoft Smooth Streaming [1]). The figure shows that over 95% of switching decisions occur at intervals higher than 1 second for both players. This suggests that a cloud-based deployment is viable. 6 DISCUSSION AND FUTURE WORK Performance improvements for all sessions.

**Fragmento 12 - p. 1 - score 4:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 13 - p. 2 - score 4:**

Publishers, content delivery networks, and users all seek to improve user quality of experience (QoE). There are many factors that affect QoE including start up latency, the average bitrate for a video session, as well as the rebuffering ratio (the percentage of time playback is stalled because of drained buffer) [23]. Video players improve QoE using adaptive bitrate (ABR) algorithms which select bitrates for each chunk while (1) ensuring the bitrate seen by the user is as high as possible and (2) avoiding rebuffering events at the client. Some ABR algorithms may also try to minimize the number of bitrate switches to make the playback smooth. Content publishers serve different types of content includ- ing VoD (Video on Demand) or Live broadcasts.

**Fragmento 14 - p. 3 - score 4:**

A key reason for this is that ABR algorithms have parameters (which we henceforth refer to as configurations) that must be set in a manner sensitive to network conditions. ABR algorithms need to run on many different networks, rang- ing from cellular and WiFi networks at one end, to high-speed broadband connections at the other. Given this diversity, net- work conditions can vary significantly. Packet loss conditions can vary by an order of magnitude or more across the globe [25]. Network throughputs can also vary widely: for 90% of traces in a large dataset, the trace’s maximum throughput is more than twice its average throughput. Yet, unfortunately, most ABR algorithms today either employ fixed configura- tions or simple heuristics to adapt these configurations (§2.1).

**Fragmento 15 - p. 8 - score 4:**

In particular, for 19% of the sessions, QoE-lin improves by more than 20%. For the sessions MPC+Oboe is unable to improve RobustMPC, its performance degradation is mostly under 8%. Figures 6(b), 6(c) and 6(d) show the constituent QoE metrics. While MPC+Oboe achieves distributionally sim- ilar bitrates as RobustMPC as shown in 6(b), it significantly reduces rebuffering across sessions: the number of sessions with rebuffering reduces from 33.2% to 5.3%. Further, it also achieves better playback smoothness by improving the 4The increase in QoE-lin over RobustMPC relative to the absolute QoE-lin value of RobustMPC expressed as a percentage. Figure 8—An example session showing how MPC+Oboe is able to outperform Ro- bustMPC by reconfiguring the discount parameter when a network state change is de- tected.

**Fragmento 16 - p. 8 - score 4:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 6—The percentage improvement in QoE-lin of MPC+Oboe over RobustMPC for the Testbed experiment. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 7—QoE-lin of MPC+Oboe compared to RobustMPC of tracking the performance of the actual ABR algorithms. For instance, Figure 5(a) and 5(b) demonstrates this for the HYB algorithm. The figures shows the correlation for the average bitrate and rebuffering ratio for 100 throughput traces randomly sampled from our dataset using HYB on the VirtualPlayer compared to using an actual Dash.js player. For both metrics, the graph closely tracks the 𝑦= 𝑥line indicating close correlation.

**Fragmento 17 - p. 8 - score 4:**

median per chunk change magnitude by 38% (Figure 6(d)). Fi- nally, Figure 7 shows the CDF of QoE-lin for MPC+Oboe and RobustMPC, and indicates MPC+Oboe distributionally performs better. Figure 8 illustrates, using a single session, why MPC+Oboe performs better than RobustMPC. The top graph shows throughput as a function of time, which includes an initial stable state followed by a drop in throughput. The middle graph shows how the discount factor 𝑑of both RobustMPC, and MPC+Oboe vary (the predicted throughput for each system is reduced by a factor of 1 1+𝑑, where 𝑑is shown on the y-axis). During the initial stable state, when prediction errors are low, RobustMPC steadily lowers its discount factor leading to more aggressive bitrate selections (not shown).

**Fragmento 18 - p. 9 - score 4:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and bitrate change magnitude for the schemes is also shown. Figure 10—Validation of our training methodology for Pensieve. Figure 11—QoE-lin of MPC+Oboe compared to Pensieve Figure 12—Benefits of specializing Pensieve models. Each curve shows the QoE improvement of MPC+Oboe rela- tive to each Pensieve model. Figure 13—QoE improvement of MPC+Oboe over two ways of dy- namically selecting from specialized Pensieve models. MPC+Oboe outperforms RobustMPC as well, we explore how MPC+Oboe performs relative to Pensieve.

**Fragmento 19 - p. 9 - score 4:**

Figure 12 shows the per session QoE-lin improvement of MPC+Oboe com- pared to Pensieve models trained for 0-3 Mbps (which we refer to as Pens-Specialized) and for 0-6 Mbps. The me- dian QoE-lin improvement with MPC+Oboe over Pens- Specialized is 10.49%, while the median improvement over 52

**Fragmento 20 - p. 10 - score 4:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d) Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors Pensieve is 19.9%. This indicates specializing the model does improve Pensieve’s performance. Thus, Pensieve’s model is as yet unable to create special- ized versions of itself based on the session characteristics. By contrast, Oboe specializes parameters for every network state and therefore performs better. We have also validated Pensieve’s inability to specialize in several other ways: build- ing a model for the 3-6 Mbps and showing that it performs better with test data in that range compared to a 0-6 Mbps model; checking that a 0-6 Mbps model performs better for data in that range compared to a 0-100 Mbps model; and ensuring that these results hold even when the training set is doubled.

**Fragmento 21 - p. 10 - score 4:**

Pens-SelOnce starts with the 0-6 Mbps model, selects either the 0-3 Mbps or 3-6 Mbps model based on the average throughput of the first 5 initial chunks, and does not switch thereafter. Figure 13 shows CDFs of per-session QoE-lin improve- ment of MPC+Oboe over these selectors. MPC+Oboe is able to outperform both Pens-SelMultile and Pens-SelOnce, with average QoE-lin improvements of 14.2% and 24.32% re- spectively. Even though one of the model selection schemes offers some improvements over the 0-6 Mbps Pensieve model, the benefits are modest. We hypothesize that this behavior is due to the dynamic selection of distinct Pensieve models, which can interfere with reinforcement learning’s decision choices, since, during training, the reinforcement learning algorithm assumes there is no such third party intervention.

**Fragmento 22 - p. 11 - score 4:**

Our experi- ments were conducted in simulation, using the VirtualPlayer, and the testbed experiment traces (§4.2). Figure 15 shows the average QoE-lin across the traces for RobustMPC and MPC+Oboe using both the default har- monic mean approach and Ideal(T) for different values of T. Although RobustMPC performs better with an ideal predictor, Oboe still provides benefits, achieving an average improve- ment in QoE-lin of 6.34% for Ideal(5) and of 1.8% for Ideal(10), compared to a 16.1% improvement with the har- monic mean estimator. While the magnitude of benefits is smaller with the ideal prediction approach, in practice Oboe will likely result in larger benefits, since even more sophisti- cated schemes [49] cannot achieve the ideal predictions, and the errors are likely to grow with larger T.

**Fragmento 23 - p. 12 - score 4:**

Even for these choices, HYB+Oboe outperforms HYB, demonstrating its ability to adapt to differ- ent publisher specification. Accommodating publisher’s rebuffering tolerance. Oboe allows the publisher to optionally specify explicit rebuffer- ing preferences (§3). ABR algorithms such as RobustMPC which use the QoE-lin function may permit this indirectly by adjusting QoE-lin weights (§2.1). Figure 17 shows the effectiveness of these approaches, showing the average of average bitrates, and the fraction of sessions with rebuffering for HYB+Oboe. As the publisher makes its rebuffering pref- erence stricter (from 2%-0%), HYB+Oboe achieves lower rebuffering ratios close to the target rebuffering tolerance.

**Fragmento 24 - p. 7 - score 3:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 5—A scatter plot of average bitrate and rebuffering ratio between the Virtu- alPlayer and real Dash.js player and BOLA primarily maximize average bitrate subject to low rebuffering. In contrast, other algorithms [39, 59] have been designed to optimize a QoE metric which is a linear combina- tion of bitrate, rebuffering and bitrate changes (smoothness). With Oboe, our primary evaluation goal is to demonstrate the extent to which it can improve the underlying metrics that an ABR algorithm is designed for. Thus, our evaluations with BOLA and HYB focus on average bitrate and rebuffering, while those with MPC+Oboe focus on the linear combination of QoE (which we refer to as QoE-lin, [59]), defined as follows.

**Fragmento 25 - p. 7 - score 3:**

We focus on this video as it has been used in prior work [39], and we do not consider videos of longer duration because we only have throughput traces available for a video publisher that serves short music videos (as we discuss below). The video is hosted on an Apache server. Both the server and client software run on the same 8-core, 4 Ghz, Intel i7 commodity desktop with 12 GB RAM running Ubuntu 16.04. Between server and client, we emulate different network conditions using the Chrome DevTools API [9]. This allows us to control the upload/download throughput as well as latency using the Chrome-Remote-Interface based on throughput traces [5]. We use 571 throughput traces3 from our dataset (discussed below) for this emulation.

**Fragmento 26 - p. 7 - score 3:**

All our testbed experiments use a client buffer of 2 minutes. Datasets. We use throughput traces from real user sessions collected over a three month period. Each trace contains the in- dividual chunk sizes and their download times for on-demand video sessions from a publisher that serves short (4-6 minute) music videos. We derive throughput by dividing the chunk sizes by their download durations. The traces contain sessions that used desktops with wired connections and also sessions on mobile devices using WiFi or cellular connections. Like previous work [39, 59], we primarily focus on traces that have less than 6 Mbps average throughput, since this is the regime where bitrate switching decisions are likely to have QoE impact.


### 7.9. limitaciones riesgos coste

Palabras clave usadas: `limitation, limitations, future work, challenge, challenges, overhead, complexity, compute, GPU, CPU, deployment, real-world, generalization, out-of-distribution, OOD, unstable, fail, bias, sensitive, prediction error, horizon, scalability`

**Fragmento 1 - p. 4 - score 3:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the left graph, although the throughput is generally good, the sudden variations force RobustMPC to make overly conserva- tive bitrate decisions, as well as incur more bitrate switches. (bottom subgraph). In contrast, in Figure 2(b), the quicker and more frequent throughput changes (top subgraph) result in FastMPC experiencing rebuffering (middle subgraph), while RobustMPC does not. This is just one example illustrating the difficulty in picking parameters – in our evaluations (§4), we found that RobustMPC was itself too aggressive when selecting discount factors for some traces. While this section uses synthetic traces for illustrative pur- poses, our evaluations with real traces (§4) more extensively demonstrate the limitations of current approaches with re- spect to selecting parameters and the benefits of automatically tuning ABR parameters to network conditions.

**Fragmento 2 - p. 1 - score 2:**

Oboe: Auto-tuning Video ABR Algorithms to Network Conditions Zahaib Akhtar* University of Southern California Yun Seong Nam* Purdue University Ramesh Govindan University of Southern California Sanjay Rao Purdue University Jessica Chen University of Windsor Ethan Katz-Bassett Columbia University Bruno Ribeiro Purdue University Jibin Zhan Conviva Hui Zhang Conviva ABSTRACT Most content providers are interested in providing good video delivery QoE for all users, not just on average. State-of-the-art ABR algorithms like BOLA and MPC rely on parameters that are sensitive to network conditions, so may perform poorly for some users and/or videos. In this paper, we propose a technique called Oboe to auto-tune these parameters to dif- ferent network conditions.

**Fragmento 3 - p. 3 - score 2:**

Specifically, if 𝑆𝑗(𝑖) denotes the size of chunk 𝑗 encoded at bitrate 𝑖, 𝐵is the predicted throughput based on past samples, and 𝐿the length of the buffer. HYB picks the largest bitrate 𝑖such that 𝑆𝑗(𝑖) 𝐵 < 𝐿× 𝛽. Here, 𝛽can have values between 0 and 1 (higher values represent aggressive ABR behavior). 𝛽can be tuned to offset prediction errors in throughput and to compensate for the greedy nature of the approach which may make it susceptible to future buffering events owing to unexpected throughput dips. 2.2 Ensuring High QoE for All Users Despite widespread deployment, ABR algorithms continue to be an active area of research [32, 34, 39, 48, 51, 59]. This is because, while deployed ABR algorithms work well on average, they do not work uniformly well across all network conditions.

**Fragmento 4 - p. 4 - score 2:**

3 OBOE DESIGN Oboe aims to ensure good QoE for all users by enabling ABR algorithms to perform better across a wide range of network conditions. The configurations of many ABR algorithms are sensitive to network state, specifically to the value and vari- ability of the available throughput between the client and the video server. For example, 𝛽in HYB should be smaller when available throughput is highly variable, while 𝛾in BOLA should be higher. This explains why the algorithms perform differently for different values of parameters on a given client trace (§2.2). However, a line of prior work [17, 35, 38, 52, 60] has observed that network connections are piecewise station- ary: that is, connections can be in one of several distinct states (§3.1), where each state is distinguished by stationarity in the statistical sense (informally, a process is stationary if its sta- tistical properties including mean and variance do not change over time - see [43] for a more formal definition).

**Fragmento 5 - p. 4 - score 2:**

Oboe leverages the piecewise stationarity of network con- nections to address the key challenge of sensitivity of config- urations to network conditions. It does so using a two stage design: (a) an offline stage where it pre-computes the best con- figuration choice for each (stationary) network state (§3.2), and (b) and an online stage, where during a session, it de- tects changes in network state and applies the pre-computed best configuration for the current (stationary) state (§3.3). Oboe can also accommodate publisher specifications such as session type (live vs. video-on-demand, time-to-live re- quirements), bitrate levels or any explicit QoE tradeoffs (e.g., preference between rebuffering and average bitrate) (§3.2), by using these to influence the selection of the best configuration for each (stationary) network state in the offline stage.

**Fragmento 6 - p. 12 - score 2:**

5 DEPLOYMENT CONSIDERATIONS The offline stage of Oboe can be run on the cloud, but several choices exist for the online stage, ranging from embedding the online stage entirely in the client player, or moving some or all of the online stage to the cloud. In our implementation, Oboe’s components run on the server side. This mimics a cloud implementation, which has the benefits of other cloud software: fast update deployment, device independence, etc. [4]. We leave a detailed comparison of these choices to future work, but explore, in this section, the feasibility of running the online stage on the cloud. To this end, we have implemented a restricted version of HYB+Oboe on AWS. This limited version of Oboe imple- ments HYB and incorporates tuning based on publisher speci- fications but not network state.

**Fragmento 7 - p. 12 - score 2:**

In our implementation, a client player periodically reports player state (such as buffer length and current bitrate) and throughput samples to a Oboe cloud server and receives bitrate decisions in return. For 10 player features and two chunk downloads per second, the commu- nication overhead is 6.4 Kbps, negligibly small compared to the size of video chunks. Figures 19(a) and 19(b) compare the performance of this implementation against a client player running HYB over 20K sessions collected during a two-week pilot deployment. Oboe is comparable in performance to the client side player and even improves bitrate slightly (because it was tuned to this publisher’s specification). 55

**Fragmento 8 - p. 13 - score 2:**

It is unclear if Oboe can directly augment Pensieve, since a model learned by reinforcement learning may not interact well with intermediaries such as Oboe. However, combining the benefits of Oboe and Pensieve in other ways is an interesting avenue for future work. 7 RELATED WORK Tuning ABR Algorithm Configurations. The BBA2 algo- rithm [32] tunes its lower reservoir based on buffer occupancy dynamics, while MPC [59] adapts its throughput discount fac- tor based on past prediction errors (§2). In contrast to such ad- hoc heuristics, Oboe selects configuration parameters based on network state, and publisher specifications. The approach is generically applicable to many ABR algorithms. Newer congestion control protocols like BBR [19] estimate network throughput, which if exposed, could benefit Oboe.

**Fragmento 9 - p. 13 - score 2:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary We expected a cloud implementation would perform worse because of the latency induced by client-server communica- tion. However, we found that most of the bitrate switching decisions occur on timescales much longer than the client- server latencies. Figure 20 shows the CDF of the time interval between consecutive bitrate switches for ABR algorithms in two widely used video players(Adobe’s Flash [3] and Mi- crosoft Smooth Streaming [1]). The figure shows that over 95% of switching decisions occur at intervals higher than 1 second for both players. This suggests that a cloud-based deployment is viable. 6 DISCUSSION AND FUTURE WORK Performance improvements for all sessions.

**Fragmento 10 - p. 1 - score 1:**

Oboe pre-computes, for a given ABR algorithm, the best possible parameters for different net- work conditions, then dynamically adapts the parameters at run-time for the current network conditions. Using testbed ex- periments, we show that Oboe significantly improves BOLA, MPC, and a commercially deployed ABR. Oboe also betters a recently proposed reinforcement learning based ABR, Pen- sieve, by 24% on average on a composite QoE metric, in part because it is able to better specialize ABR behavior across different network states. CCS CONCEPTS • Information systems →Information systems applica- tions; Multimedia streaming; KEYWORDS Video delivery, Adaptive bitrate algorithms ACM Reference Format: Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, and Hui Zhang.

**Fragmento 11 - p. 1 - score 1:**

Current ABR algorithms perform well on average, but some users can experience poor delivery performance as measured by the QoE metrics. These users suffer because ABR algorithms have limited dynamic range: they do not perform uniformly well across the range of network conditions seen in practice because their parameters are sensitive to throughput variability (§2). Contributions. In this paper, we present the design of Oboe1 (§3), a system that takes the first step towards overcoming these hurdles. Oboe improves the dynamic range of ABR algorithms by automatically tuning ABR behavior to 1In orchestras all instruments tune to the Oboe. 44

**Fragmento 12 - p. 2 - score 1:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 13 - p. 2 - score 1:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the current network state of a client connection, specifically to throughput and throughput variability. Oboe’s design is based on the observation made by prior work [17, 35, 38, 52, 60] that TCP connections are well- modeled as traversing a piecewise-stationary sequence of network states (§3.1): the connection consists of multiple non-overlapping segments where each segment is in a distinct stationary network state. For each possible network state, Oboe pre-computes, offline, the best parameter configuration for a given ABR algorithm (§3.2). It does this by subjecting the algorithm, for each state, to different parameter values, and picking the one that results in the best performance.

**Fragmento 14 - p. 2 - score 1:**

We have tried training specialized Pensieve models for different ranges of network throughputs and dynamically switching models based on estimated session throughput. This helps, but a sig- nificant gap between the two approaches still remains (§4.4). While a variety of viable pathways exist to deploying Oboe, we focus on an architecture where Oboe and the entire ABR logic are deployed on the cloud which enables rapid evolution and fine-grain customizability. We show the viability of this architecture with results from a pilot deployment. 2 BACKGROUND AND MOTIVATION The Internet video delivery ecosystem consists of hundreds of content publishers and hundreds of client side applications that stream video content to diverse user devices.

**Fragmento 15 - p. 3 - score 1:**

A key reason for this is that ABR algorithms have parameters (which we henceforth refer to as configurations) that must be set in a manner sensitive to network conditions. ABR algorithms need to run on many different networks, rang- ing from cellular and WiFi networks at one end, to high-speed broadband connections at the other. Given this diversity, net- work conditions can vary significantly. Packet loss conditions can vary by an order of magnitude or more across the globe [25]. Network throughputs can also vary widely: for 90% of traces in a large dataset, the trace’s maximum throughput is more than twice its average throughput. Yet, unfortunately, most ABR algorithms today either employ fixed configura- tions or simple heuristics to adapt these configurations (§2.1).

**Fragmento 16 - p. 3 - score 1:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces throughput prediction errors, a more conservative version, Ro- bustMPC, reduces predicted throughput by a discount factor 1+𝑑, where 𝑑is the maximum error in throughput predictions experienced in the last five chunk downloads. BOLA: Buffer occupancy, selects bitrate by solving an optimization problem. BOLA is a buffer-based algorithm used in Dash.js [7], so it does not employ throughput pre- diction in making bitrate decisions [48].

**Fragmento 17 - p. 4 - score 1:**

3.1 Representing Network State Most ABR algorithms today adapt bitrates based on the throughput (more precisely, goodput) achieved by recently Figure 3—The logical diagram of the offline pipeline used by Oboe downloaded chunks. This perceived throughput already ac- counts for network delays and loss-rates, as well as the dy- namics of the underlying transport protocol. The network throughput along a path is not necessarily a stationary process [17, 35, 38, 52, 60]: flows at the bottleneck along a path may change over time resulting in changes to available throughput, or the bottleneck itself may shift [35]. An analysis of the throughput traces used in our evaluations (§4) confirms the lack of stationarity when applied to the en- tire trace.

**Fragmento 18 - p. 5 - score 1:**

At the end of this stage, Oboe obtains the Con- figMap, a complete mapping of each network state to its corresponding optimal ABR configuration. Two optimizations can be used to quicken the rate of ex- ploration of the ConfigEvaluator. The first is to quantize the parameter sweep, so that configurations are evaluated at a coarser granularity. This trades off some performance for lower computational complexity. The second optimization is based on the observation that there is generally a monotonic relationship between parameter values and the performance. For instance, for HYB (§2.1), the rebuffering ratio and av- erage bitrate are monotonically non-decreasing with the pa- rameter 𝛽. Based on this observation, we can instead use an 𝑂(log 𝑛) binary search of the configuration space instead of doing a full 𝑂(𝑛) sweep of all configurations.

**Fragmento 19 - p. 5 - score 1:**

ConfigSelector takes the set of performance vectors and determines the best configuration from them using vector dominance. A configuration 𝑐𝑖is said to dominate 𝑐𝑗if 𝑉𝑖 element-wise dominates 𝑉𝑗(i.e., each element of 𝑉𝑖is bet- ter than or equal to the corresponding element of 𝑉𝑗). This step also takes into account any rebuffering tolerance, and ConfigSelector applies this tolerance to select the maximal performance vector. Deferring the selection of the maximal vector for a given rebuffering tolerance to this stage (instead of filtering vectors in the previous step) is beneficial: it mini- mizes recomputation by allowing Oboe to quickly compute a new maximal vector if the publisher changes the rebuffering tolerance.

**Fragmento 20 - p. 6 - score 1:**

Reconfiguring ABR Algorithm. When a change in the net- work state is detected, the ChangeDetector signals the change and the new network state 𝑠to the ReconfEngine. The Recon- fEngine then searches a neighborhood of radius 𝑟in the Con- figMap to select the configuration to use for state 𝑠. Specifi- cally, if state 𝑠is a point in a 2-dimensional space of average throughput and standard deviation of throughput, then it picks the most conservative ABR configuration within a search ra- dius 𝑟around 𝑠. It does this for two reasons. First, because Oboe quantizes the network states, it might not have precom- puted the best configuration for 𝑠. Second, the estimated new network state 𝑠may have some error, for example, due to inefficiencies in the client download stack [27].

**Fragmento 21 - p. 6 - score 1:**

Given these sources of uncertainty, Oboe chooses to be safe in its selec- tion of the best configuration for 𝑠. Finally, ReconfEngine configures the ABR algorithm, and the reconfigured ABR algorithm is ready to compute the bitrate decision to be used for the next chunk at this point. 4 EVALUATION In this section, we demonstrate Oboe’s ability to auto-tune three existing algorithms: RobustMPC, BOLA and HYB. We also compare an Oboe-tuned RobustMPC to Pensieve [39]. 4.1 Metrics The performance of a video session depends on multiple fac- tors. Average bitrate and rebuffering ratio were found to have the most impact on user quality of experience [23], though other factors such as changes in bitrates during a session can play a role [23].

**Fragmento 22 - p. 6 - score 1:**

Players such as Dash.js already periodically log intermediate throughput samples during a chunk download, so obtaining these sam- ples does not incur any additional overhead. We only need to modify players to report these samples to Oboe. The set of samples are provided to ChangeDetector after the chunk download, and any change in state is only detected at the end of the chunk download. This is acceptable since any action that can be taken by the ABR algorithm (such as a bit rate switch) only impacts subsequent chunks. In the rarer case that an ABR algorithm abandons the download of a chunk that takes too long, the report is sent when the chunk download is abandoned. §4.8 evaluates the overheads of ChangeDetector.

**Fragmento 23 - p. 7 - score 1:**

We filtered out traces which were too short for playing our entire 192 second video, after which we obtained 5K traces from wired desktops and 4K sessions from WiFi or 3G/4G mobile devices. Our testbed experiments use a subset of 571 traces with roughly the same number of traces sampled from each of desktop and mobile clients. VirtualPlayer setup. Recall that Oboe uses the Virtu- alPlayer to obtain a ConfigMap for any ABR algorithm. Since the majority of our results use an actual testbed with the Dash.js player, the benefits of Oboe in our evaluation results already arise despite any inaccuracies in building the ConfigMap on account of using the VirtualPlayer. That said, we have also verified that the VirtualPlayer does a good job 3Available at https://github.com/USC-NSL/Oboe 50

**Fragmento 24 - p. 7 - score 1:**

The underlying factors represent concrete application performance that publishers understand how to reason about. Moreover, a unified metric like QoE-lin can obscure important differences. For example, two sessions may have the same QoE-lin but different performance in underlying metrics, leading to varied user experience. So, we also present graphs of these metrics. 4.2 Methodology Implementation. For RobustMPC, we used the imple- mentation available at [11]. Our implementation of BOLA [@bola] is from the Dash.js player. The implementation of HYB is a variant of the algorithm used in a large-scale deployment. These ABR algorithms and Oboe’s online stage (change point detection and ABR reconfiguration) run on the server in our experiments.

**Fragmento 25 - p. 8 - score 1:**

median per chunk change magnitude by 38% (Figure 6(d)). Fi- nally, Figure 7 shows the CDF of QoE-lin for MPC+Oboe and RobustMPC, and indicates MPC+Oboe distributionally performs better. Figure 8 illustrates, using a single session, why MPC+Oboe performs better than RobustMPC. The top graph shows throughput as a function of time, which includes an initial stable state followed by a drop in throughput. The middle graph shows how the discount factor 𝑑of both RobustMPC, and MPC+Oboe vary (the predicted throughput for each system is reduced by a factor of 1 1+𝑑, where 𝑑is shown on the y-axis). During the initial stable state, when prediction errors are low, RobustMPC steadily lowers its discount factor leading to more aggressive bitrate selections (not shown).

**Fragmento 26 - p. 10 - score 1:**

HYB. The performance of HYB is sensitive to the choice of 𝛽parameter, which HYB+Oboe tunes. In production, HYB uses 𝛽= 0.25, determined using A/B tests in a large-scale de- ployment. Figure 14(c) and 14(d) show CDFs of per session performance improvement of average bitrate and rebuffer- ing ratio over HYB. As with BOLA, HYB+Oboe maintains similar rebuffering ratios as shown in 14(d), but improves bitrates for 98% of sessions with an overall average bitrate improvement of 8.32% in average across all sessions. 4.6 Sensitivity experiments Alternative throughput traces. To understand how Oboe works on throughput datasets beyond those discussed in §4.2, we evaluated Oboe on two other datasets, FCC [8] and HS- DPA [46] that have been used in recent work [39, 59].


### 7.10. ideas fase45 v1 controller defendible

Palabras clave usadas: `risk, safe, safety, robust, conservative, fallback, uncertainty, capacity, lower bound, tail, severe, low buffer, volatile, variable, fluctuation, drop, zero, consistent, smoothness, auto-tuning, regime, cluster, guidance, hybrid, generalization, environment-aware, prediction, selector`

**Fragmento 1 - p. 3 - score 3:**

It also models bitrate selection as an optimization problem which it solves for a given value of the buffer. It uses a parameter 𝛾which is a ratio of (i) a minimum buffer threshold, below which it downloads the lowest bitrate and (ii) a target buffer threshold which it tries to maintain. Conceptually 𝛾controls how strongly the ABR should avoid rebuffering [48]. Higher values of 𝛾make the algorithm conservative. HYB: Throughput prediction without lookahead. Selects bitrate using a simple heuristic. An algorithm widely used in production (§5), HYB considers both the predicted throughput and current buffer occupancy (HYB is short for hybrid). For each chunk, HYB picks the highest bitrate that can avoid rebuffering.

**Fragmento 2 - p. 6 - score 3:**

Given these sources of uncertainty, Oboe chooses to be safe in its selec- tion of the best configuration for 𝑠. Finally, ReconfEngine configures the ABR algorithm, and the reconfigured ABR algorithm is ready to compute the bitrate decision to be used for the next chunk at this point. 4 EVALUATION In this section, we demonstrate Oboe’s ability to auto-tune three existing algorithms: RobustMPC, BOLA and HYB. We also compare an Oboe-tuned RobustMPC to Pensieve [39]. 4.1 Metrics The performance of a video session depends on multiple fac- tors. Average bitrate and rebuffering ratio were found to have the most impact on user quality of experience [23], though other factors such as changes in bitrates during a session can play a role [23].

**Fragmento 3 - p. 8 - score 3:**

median per chunk change magnitude by 38% (Figure 6(d)). Fi- nally, Figure 7 shows the CDF of QoE-lin for MPC+Oboe and RobustMPC, and indicates MPC+Oboe distributionally performs better. Figure 8 illustrates, using a single session, why MPC+Oboe performs better than RobustMPC. The top graph shows throughput as a function of time, which includes an initial stable state followed by a drop in throughput. The middle graph shows how the discount factor 𝑑of both RobustMPC, and MPC+Oboe vary (the predicted throughput for each system is reduced by a factor of 1 1+𝑑, where 𝑑is shown on the y-axis). During the initial stable state, when prediction errors are low, RobustMPC steadily lowers its discount factor leading to more aggressive bitrate selections (not shown).

**Fragmento 4 - p. 3 - score 2:**

Figures 1(a) and 1(b) show how the choice of ABR config- uration depends on network conditions. Figure 1(a) shows the bitrate and rebuffering ratio for two client sessions with the HYB algorithm for three different values of its 𝛽parameter, Cons (Conservative), Mod (Moderate), and Aggr (Aggres- sive). The throughput behavior of the two sessions is shown in Figure 1(c). If a publisher prefers to eliminate rebuffering, Mod is suitable for session A, but Cons is better for session B. Figure 1(b) shows that BOLA behaves similarly, with Mod being the preferred setting for session A and Cons for session B, to avoid rebuffering. Figures 2(a) and 2(b) show the difficulty in setting the discount factor with MPC, by comparing the performance of FastMPC (no discount factor), and RobustMPC (discount factor set by local heuristic) for two throughput traces with different characteristics.

**Fragmento 5 - p. 3 - score 2:**

Oboe SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces throughput prediction errors, a more conservative version, Ro- bustMPC, reduces predicted throughput by a discount factor 1+𝑑, where 𝑑is the maximum error in throughput predictions experienced in the last five chunk downloads. BOLA: Buffer occupancy, selects bitrate by solving an optimization problem. BOLA is a buffer-based algorithm used in Dash.js [7], so it does not employ throughput pre- diction in making bitrate decisions [48].

**Fragmento 6 - p. 8 - score 2:**

In particular, for 19% of the sessions, QoE-lin improves by more than 20%. For the sessions MPC+Oboe is unable to improve RobustMPC, its performance degradation is mostly under 8%. Figures 6(b), 6(c) and 6(d) show the constituent QoE metrics. While MPC+Oboe achieves distributionally sim- ilar bitrates as RobustMPC as shown in 6(b), it significantly reduces rebuffering across sessions: the number of sessions with rebuffering reduces from 33.2% to 5.3%. Further, it also achieves better playback smoothness by improving the 4The increase in QoE-lin over RobustMPC relative to the absolute QoE-lin value of RobustMPC expressed as a percentage. Figure 8—An example session showing how MPC+Oboe is able to outperform Ro- bustMPC by reconfiguring the discount parameter when a network state change is de- tected.

**Fragmento 7 - p. 8 - score 2:**

This results in a rebuffering event 44 seconds into the session (lowest graph shows buffer occupancy with 0 indicating a rebuffering event). In contrast, MPC+Oboe does not incur a rebuffering event and maintains a fixed 𝑑during the initial stable state. At 29 sec, it detects a change in the network state and adapts its discount factor, leading to more conservative bitrate selections. 4.4 Oboe vs. Pensieve Pensieve [39] uses deep reinforcement learning [41, 42], a combination of deep learning with reinforcement learn- ing [50], and has been shown to outperform existing ABRs, including RobustMPC [39] in some settings. Since 51

**Fragmento 8 - p. 10 - score 2:**

It is hard to pinpoint exactly why Pensieve is unable to learn to be more conservative in the 0-3 Mbps range; deep neural network models remain a black box despite efforts by the machine learning community to make these models more transparent [45], and obtaining such understanding may need further advances in interpretable deep learning models. A model selector with Pensieve . One way to improve Pen- sieve’s specialization might be to train different models for different throughput ranges and use the model more suited to the network conditions. To test the efficacy of this ap- proach, we used two models (specialized for 0-3 Mbps and 3-6 Mbps), and tried two different model selectors. Pens- SelMultiple switches models throughout the session, using the average throughput of the past 5 chunks.

**Fragmento 9 - p. 11 - score 2:**

Oboe can improve performance over RobustMPC even when an Ideal(T) prediction method is used for two reasons. First, 𝑇may not match the duration of chunk downloads with RobustMPC, which depends on the exact sequence of bitrates chosen during the look-ahead window. The duration is not known a priori, since RobustMPC itself determines the bitrates based on a provided prediction. Second, the decisions made by RobustMPC are over a small look-ahead window, which may not guarantee optimality over the entire session duration. 4.7 Oboe Across Various Settings In §4.5 we have shown that Oboe outperforms other ABR algorithms when compared to their default configurations. We now explore, for HYB, whether Oboe outperforms all parameter settings of HYB and whether it can tune ABRs based on content type and publisher specifications.

**Fragmento 10 - p. 11 - score 2:**

Our experi- ments were conducted in simulation, using the VirtualPlayer, and the testbed experiment traces (§4.2). Figure 15 shows the average QoE-lin across the traces for RobustMPC and MPC+Oboe using both the default har- monic mean approach and Ideal(T) for different values of T. Although RobustMPC performs better with an ideal predictor, Oboe still provides benefits, achieving an average improve- ment in QoE-lin of 6.34% for Ideal(5) and of 1.8% for Ideal(10), compared to a 16.1% improvement with the har- monic mean estimator. While the magnitude of benefits is smaller with the ideal prediction approach, in practice Oboe will likely result in larger benefits, since even more sophisti- cated schemes [49] cannot achieve the ideal predictions, and the errors are likely to grow with larger T.

**Fragmento 11 - p. 11 - score 2:**

MPC+Oboe provides larger gains in settings like the traces discussed in §4.2, where only 41% traces are under 3 Mbps and 59% are in the 3-6 Mbps range. Alternative throughput prediction methods. Our experi- ments with RobustMPC rely on throughput prediction based on the harmonic mean of prior throughput samples (follow- ing earlier work [39, 59]), with Oboe tuning the configura- tion to compensate for prediction errors. We next consider if Oboe’s benefits hold if RobustMPC were to have more accurate throughput predictions, potentially by using alter- nate prediction methods [49]. Rather than using a specific prediction technique, we consider an ideal (and unachievable) approach that we denote as Ideal(T), which can exactly predict the average throughput over the next T seconds.

**Fragmento 12 - p. 12 - score 2:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. Figure 17—Avg. of avg. bitrate and fraction of sessions with rebuffering for HYB+Oboe and different publisher pref- erences Figure 18—Avg. of avg. bitrate and fraction of sessions with rebuffering for RobustMPC and different publisher preferences depicts performance for live video (which uses a maximum buffer size of 20 seconds to mimic live settings). HYB+Oboe outperforms HYB for this setting, though we note that the bitrate of both approaches degrades relative to the VoD setting since the baseline HYB switches to higher bitrates more conservatively owing to the smaller buffer sizes. Finally, Figure 16(d) depicts performance for higher bi- trate levels ({1002, 1434, 2738, 3585, 4661, 5886}𝑘𝑏𝑝𝑠) and a chunk size of 5 seconds.

**Fragmento 13 - p. 1 - score 1:**

Oboe: Auto-tuning Video ABR Algorithms to Network Conditions Zahaib Akhtar* University of Southern California Yun Seong Nam* Purdue University Ramesh Govindan University of Southern California Sanjay Rao Purdue University Jessica Chen University of Windsor Ethan Katz-Bassett Columbia University Bruno Ribeiro Purdue University Jibin Zhan Conviva Hui Zhang Conviva ABSTRACT Most content providers are interested in providing good video delivery QoE for all users, not just on average. State-of-the-art ABR algorithms like BOLA and MPC rely on parameters that are sensitive to network conditions, so may perform poorly for some users and/or videos. In this paper, we propose a technique called Oboe to auto-tune these parameters to dif- ferent network conditions.

**Fragmento 14 - p. 1 - score 1:**

2018. Oboe: Auto-tuning Video ABR Algorithms to * Both authors contributed equally to this paper and can be contacted at following: zakhtar@usc.edu, nam21@purdue.edu Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

**Fragmento 15 - p. 2 - score 1:**

Then, during video playback, Oboe continuously uses a change- point detection algorithm to detect changes in network state and selects the parameter identified by the offline analysis as best for the current state. Thus, if a video session encounters varying network state during its lifetime, Oboe automatically specializes the ABR parameter to each state (§3.3). We have implemented Oboe and demonstrated several as- pects of its performance through testbed experiments and trace driven simulations. First, Oboe significantly improves performance of QoE metrics for three qualitatively different ABR algorithms, one that makes bitrate switching decisions on buffer occupancy alone (BOLA) [48], another that uses both throughput and buffer occupancy (HYB, a widely de- ployed algorithm), and a third that also optimizes decisions across a finite lookahead horizon (RobustMPC) [59].

**Fragmento 16 - p. 2 - score 1:**

2.1 Background on ABR Algorithms ABR algorithms fall in two broad categories: (i) those that use both prediction of network throughput and buffer occu- pancy [34, 51, 59]; and (ii) those that are primarily based on buffer occupancy [32, 48]. Within the above two categories, ABR algorithms can be designed using approaches ranging from heuristics to stochastic optimization. In §4, we discuss a recently proposed ABR algorithm based on a qualitatively different approach, reinforcement learning [39]. MPC: Throughput prediction and buffer occupancy with look-ahead. Selects bitrate by solving an optimization prob- lem. MPC [59] predicts throughput of future chunk down- loads based on throughput samples of recently downloaded chunks, then uses this predicted throughput to select bitrates to optimize a given QoE function (§4) over a look-ahead window of 5 future chunks.

**Fragmento 17 - p. 2 - score 1:**

In each of these cases, Oboe results in significant improvement. For instance, Oboe reduces sessions with rebuffering from 33.3% to 5.3% relative to RobustMPC while also significantly im- proving a composite QoE metric. Oboe, when applied to RobustMPC, also performs signifi- cantly better than a newly proposed approach called Pensieve that learns, from real traces (using reinforcement learning), how to adapt to a variety of network conditions. For nearly 80% of the sessions in our dataset, Oboe improves the same composite metric, with benefits exceeding 20% for 25% of the traces. Compared to Oboe, which can specialize parameters to individual network states, Pensieve is unable to special- ize across the entire range of network throughputs.

**Fragmento 18 - p. 3 - score 1:**

Specifically, if 𝑆𝑗(𝑖) denotes the size of chunk 𝑗 encoded at bitrate 𝑖, 𝐵is the predicted throughput based on past samples, and 𝐿the length of the buffer. HYB picks the largest bitrate 𝑖such that 𝑆𝑗(𝑖) 𝐵 < 𝐿× 𝛽. Here, 𝛽can have values between 0 and 1 (higher values represent aggressive ABR behavior). 𝛽can be tuned to offset prediction errors in throughput and to compensate for the greedy nature of the approach which may make it susceptible to future buffering events owing to unexpected throughput dips. 2.2 Ensuring High QoE for All Users Despite widespread deployment, ABR algorithms continue to be an active area of research [32, 34, 39, 48, 51, 59]. This is because, while deployed ABR algorithms work well on average, they do not work uniformly well across all network conditions.

**Fragmento 19 - p. 3 - score 1:**

In each figure, the top subgraphs show the available throughput (green curve) and the through- put estimate of FastMPC (red) and RobustMPC (blue). For 46

**Fragmento 20 - p. 4 - score 1:**

3 OBOE DESIGN Oboe aims to ensure good QoE for all users by enabling ABR algorithms to perform better across a wide range of network conditions. The configurations of many ABR algorithms are sensitive to network state, specifically to the value and vari- ability of the available throughput between the client and the video server. For example, 𝛽in HYB should be smaller when available throughput is highly variable, while 𝛾in BOLA should be higher. This explains why the algorithms perform differently for different values of parameters on a given client trace (§2.2). However, a line of prior work [17, 35, 38, 52, 60] has observed that network connections are piecewise station- ary: that is, connections can be in one of several distinct states (§3.1), where each state is distinguished by stationarity in the statistical sense (informally, a process is stationary if its sta- tistical properties including mean and variance do not change over time - see [43] for a more formal definition).

**Fragmento 21 - p. 4 - score 1:**

SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary Z. Akhtar et al. the left graph, although the throughput is generally good, the sudden variations force RobustMPC to make overly conserva- tive bitrate decisions, as well as incur more bitrate switches. (bottom subgraph). In contrast, in Figure 2(b), the quicker and more frequent throughput changes (top subgraph) result in FastMPC experiencing rebuffering (middle subgraph), while RobustMPC does not. This is just one example illustrating the difficulty in picking parameters – in our evaluations (§4), we found that RobustMPC was itself too aggressive when selecting discount factors for some traces. While this section uses synthetic traces for illustrative pur- poses, our evaluations with real traces (§4) more extensively demonstrate the limitations of current approaches with re- spect to selecting parameters and the benefits of automatically tuning ABR parameters to network conditions.

**Fragmento 22 - p. 4 - score 1:**

We analyze throughput traces using the Augmented Dickey-Fuller (ADF [26]) test, a hypothesis test to check for stationarity in a time series. Our evaluations on a dataset of 15,000 video streaming throughput traces show that 59.5% were non-stationary (see §4.2 for details of the dataset), imply- ing the presence of distinct mean and/or variance in different segments of the traces. However, prior work [17, 35, 38, 52, 60] shows that TCP connection throughput can be modeled as a piecewise sta- tionary process; the connection consists of multiple non- overlapping segments where each segment is stationary and often lasts for tens of seconds or minutes (e.g., Figure 8). Moreover, Zhang et al. [60] show that the throughput in each segment may be modeled as an i.i.d.

**Fragmento 23 - p. 4 - score 1:**

process. Motivated by these observations, Oboe defines network state 𝑠by a tuple < 𝜇𝑠, 𝜎𝑠>, where 𝜇𝑠is the mean and 𝜎𝑠 the standard deviation of the client-perceived throughput in a (stationary) segment of the underlying TCP connection. 3.2 Offline Mapping of Network States To map network states to their optimal ABR configurations, Oboe uses a pipeline (Figure 3) consisting of three compo- nents – the ConfigEvaluator, the VirtualPlayer and the Con- figSelector. The ConfigEvaluator takes a stationary through- put trace as input, which represents a particular network state, and drives the exploration of different ABR configurations over this trace. It does so by using the VirtualPlayer which models the dynamics of an actual video player.

**Fragmento 24 - p. 4 - score 1:**

The Virtu- alPlayer interfaces with the ABR algorithm implementation and outputs the performance of different configurations of the ABR. Finally, the ConfigSelector compares the performance of different configurations and builds a ConfigMap, which maps a given network state to the best configuration. 47

**Fragmento 25 - p. 5 - score 1:**

The VirtualPlayer also takes into account publisher spec- ifications for bitrate levels, player buffer sizes (determined by time-to-live requirements) and chunk size. These spec- ifications are used by VirtualPlayer when it executes ABR algorithms on the input traces, ensuring that the resulting Con- figMap meets the publisher specifications. Finally, Oboe also allows the publisher to optionally express an explicit QoE tradeoff such as maintaining the rebuffering under a desired threshold 𝑥%. Oboe derives a ConfigMap that meets the re- buffering threshold in a best effort manner. We evaluate the efficacy of this flexibility in §4.7. Building the ConfigMap using ConfigSelector. To build the ConfigMap, the ConfigEvaluator drives the exploration of different configurations for an ABR algorithm.

**Fragmento 26 - p. 5 - score 1:**

For a given network state 𝑠, ConfigEvaluator sweeps through possible configurations of the ABR algorithm using the VirtualPlayer. For example, the 𝛽parameter in HYB can take values from 0 to 1, so ConfigEvaluator plays the trace for state 𝑠for multiple values of 𝛽(quantized for efficiency, see below) in this range. For each parameter value 𝑐𝑖, VirtualPlayer outputs a per- formance vector 𝑉𝑖=< 𝑣1, 𝑣2, . . . 𝑣𝑚> where each 𝑣𝑘cor- responds to the values achieved by 𝑐𝑖for a QoE metric (e.g., bitrate, rebuffering ratio, and more generally join time and frequency of switching bitrates [23]). This set of performance vectors with the corresponding parameter values are then sent to ConfigSelector for picking the best configuration.


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
Oboe: Auto-tuning Video ABR Algorithms to
Network Conditions
Zahaib Akhtar*
University of Southern California
Yun Seong Nam*
Purdue University
Ramesh Govindan
University of Southern California
Sanjay Rao
Purdue University
Jessica Chen
University of Windsor
Ethan Katz-Bassett
Columbia University
Bruno Ribeiro
Purdue University
Jibin Zhan
Conviva
Hui Zhang
Conviva
ABSTRACT
Most content providers are interested in providing good video
delivery QoE for all users, not just on average. State-of-the-art
ABR algorithms like BOLA and MPC rely on parameters that
are sensitive to network conditions, so may perform poorly
for some users and/or videos. In this paper, we propose a
technique called Oboe to auto-tune these parameters to dif-
ferent network conditions. Oboe pre-computes, for a given
ABR algorithm, the best possible parameters for different net-
work conditions, then dynamically adapts the parameters at
run-time for the current network conditions. Using testbed ex-
periments, we show that Oboe significantly improves BOLA,
MPC, and a commercially deployed ABR. Oboe also betters
a recently proposed reinforcement learning based ABR, Pen-
sieve, by 24% on average on a composite QoE metric, in part
because it is able to better specialize ABR behavior across
different network states.
CCS CONCEPTS
• Information systems →Information systems applica-
tions; Multimedia streaming;
KEYWORDS
Video delivery, Adaptive bitrate algorithms
ACM Reference Format:
Zahaib Akhtar*, Yun Seong Nam*, Ramesh Govindan, Sanjay
Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan,
and Hui Zhang. 2018. Oboe: Auto-tuning Video ABR Algorithms to
* Both authors contributed equally to this paper and can be contacted at following:
zakhtar@usc.edu, nam21@purdue.edu
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
© 2018 Association for Computing Machinery.
ACM ISBN 978-1-4503-5567-4/18/08...$15.00
https://doi.org/10.1145/3230543.3230558
Network Conditions. In SIGCOMM ’18: ACM SIGCOMM 2018
Conference, August 20–25, 2018, Budapest, Hungary. 15 pages.
https://doi.org/10.1145/3230543.3230558
1
INTRODUCTION
Internet video forms a major fraction of Internet traffic to-
day [13], and delivering high quality of experience (QoE) is
critical since it correlates with user engagement and revenue
[6, 23, 31]. To deliver high quality video across diverse net-
work conditions, most Internet video delivery uses adaptive
bitrate (ABR) algorithms [32, 48, 59], combined with HTTP
chunk-based streaming protocols (e.g., Apple’s HTTP Live
Streaming, Adobe’s HTTP Dynamic Streaming). ABR algo-
rithms (a) chop a video into chunks, each of which is encoded
at a range of bitrates (or qualities); and (b) choose which
bitrate level to fetch a chunk at based on conditions such as
the amount of video the client has buffered and the recent
throughput achieved by the client. Within this general frame-
work, ABR algorithms differ in how bitrate level selection
decisions are made, and these decisions impact metrics such
as the average bitrate or the rebuffering ratio. We call these
QoE metrics, because they have been shown to correlate well
with QoE [23], but other perceptual video quality metrics [2]
may also influence QoE.
ABR algorithm design remains an active research area be-
cause content providers continue to be interested in improving
the performance of video delivery. Current ABR algorithms
perform well on average, but some users can experience poor
delivery performance as measured by the QoE metrics. These
users suffer because ABR algorithms have limited dynamic
range: they do not perform uniformly well across the range of
network conditions seen in practice because their parameters
are sensitive to throughput variability (§2).
Contributions. In this paper, we present the design of
Oboe1 (§3), a system that takes the first step towards
overcoming these hurdles. Oboe improves the dynamic range
of ABR algorithms by automatically tuning ABR behavior to
1In orchestras all instruments tune to the Oboe.
44
```


### Pagina 2
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
the current network state of a client connection, specifically
to throughput and throughput variability.
Oboe’s design is based on the observation made by prior
work [17, 35, 38, 52, 60] that TCP connections are well-
modeled as traversing a piecewise-stationary sequence of
network states (§3.1): the connection consists of multiple
non-overlapping segments where each segment is in a distinct
stationary network state. For each possible network state,
Oboe pre-computes, offline, the best parameter configuration
for a given ABR algorithm (§3.2). It does this by subjecting
the algorithm, for each state, to different parameter values,
and picking the one that results in the best performance. Then,
during video playback, Oboe continuously uses a change-
point detection algorithm to detect changes in network state
and selects the parameter identified by the offline analysis as
best for the current state. Thus, if a video session encounters
varying network state during its lifetime, Oboe automatically
specializes the ABR parameter to each state (§3.3).
We have implemented Oboe and demonstrated several as-
pects of its performance through testbed experiments and
trace driven simulations. First, Oboe significantly improves
performance of QoE metrics for three qualitatively different
ABR algorithms, one that makes bitrate switching decisions
on buffer occupancy alone (BOLA) [48], another that uses
both throughput and buffer occupancy (HYB, a widely de-
ployed algorithm), and a third that also optimizes decisions
across a finite lookahead horizon (RobustMPC) [59]. In each
of these cases, Oboe results in significant improvement. For
instance, Oboe reduces sessions with rebuffering from 33.3%
to 5.3% relative to RobustMPC while also significantly im-
proving a composite QoE metric.
Oboe, when applied to RobustMPC, also performs signifi-
cantly better than a newly proposed approach called Pensieve
that learns, from real traces (using reinforcement learning),
how to adapt to a variety of network conditions. For nearly
80% of the sessions in our dataset, Oboe improves the same
composite metric, with benefits exceeding 20% for 25% of the
traces. Compared to Oboe, which can specialize parameters
to individual network states, Pensieve is unable to special-
ize across the entire range of network throughputs. We have
tried training specialized Pensieve models for different ranges
of network throughputs and dynamically switching models
based on estimated session throughput. This helps, but a sig-
nificant gap between the two approaches still remains (§4.4).
While a variety of viable pathways exist to deploying Oboe,
we focus on an architecture where Oboe and the entire ABR
logic are deployed on the cloud which enables rapid evolution
and fine-grain customizability. We show the viability of this
architecture with results from a pilot deployment.
2
BACKGROUND AND MOTIVATION
The Internet video delivery ecosystem consists of hundreds
of content publishers and hundreds of client side applications
that stream video content to diverse user devices. Publishers,
content delivery networks, and users all seek to improve user
quality of experience (QoE). There are many factors that
affect QoE including start up latency, the average bitrate for a
video session, as well as the rebuffering ratio (the percentage
of time playback is stalled because of drained buffer) [23].
Video players improve QoE using adaptive bitrate (ABR)
algorithms which select bitrates for each chunk while (1)
ensuring the bitrate seen by the user is as high as possible
and (2) avoiding rebuffering events at the client. Some ABR
algorithms may also try to minimize the number of bitrate
switches to make the playback smooth.
Content publishers serve different types of content includ-
ing VoD (Video on Demand) or Live broadcasts. They may
also serve streams of different qualities ranging from HD
(high definition) to SD (standard definition). These differ-
ences impact how they serve videos. For example, publishers
who serve VoD content can use player buffers as large as 4
minutes [32], whereas publishers serving live content may
have a time-to-live2 requirement between 15-45 seconds. Sim-
ilarly, based on the quality of streams they serve, publishers
may use different bitrate levels or chunk sizes. Further, pub-
lishers may have different QoE objectives. For example, some
may strictly prefer to minimize rebuffering and others may
relax their tolerance for rebuffering to prioritize higher bi-
trates. We use the term publisher specifications to denote
their choice of bitrate levels, chunk sizes, content type, and
rebuffering tolerance.
2.1
Background on ABR Algorithms
ABR algorithms fall in two broad categories: (i) those that
use both prediction of network throughput and buffer occu-
pancy [34, 51, 59]; and (ii) those that are primarily based on
buffer occupancy [32, 48]. Within the above two categories,
ABR algorithms can be designed using approaches ranging
from heuristics to stochastic optimization. In §4, we discuss
a recently proposed ABR algorithm based on a qualitatively
different approach, reinforcement learning [39].
MPC: Throughput prediction and buffer occupancy with
look-ahead. Selects bitrate by solving an optimization prob-
lem. MPC [59] predicts throughput of future chunk down-
loads based on throughput samples of recently downloaded
chunks, then uses this predicted throughput to select bitrates
to optimize a given QoE function (§4) over a look-ahead
window of 5 future chunks. The aggressive version of the
algorithm (FastMPC) directly uses a throughput estimate ob-
tained using a harmonic mean predictor. To compensate for
2For live content, the time between the event and its broadcast to users. This bounds
the maximum buffer that a player streaming a live event can build.
45
```


### Pagina 3
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Figure 1—Performance of ABR algorithms using different configurations for two sessions with different throughput behaviors
Figure 2—Illustrating how policy for setting discount factors in MPC impacts performance for different traces
throughput prediction errors, a more conservative version, Ro-
bustMPC, reduces predicted throughput by a discount factor
1+𝑑, where 𝑑is the maximum error in throughput predictions
experienced in the last five chunk downloads.
BOLA: Buffer occupancy, selects bitrate by solving an
optimization problem. BOLA is a buffer-based algorithm
used in Dash.js [7], so it does not employ throughput pre-
diction in making bitrate decisions [48]. It also models bitrate
selection as an optimization problem which it solves for a
given value of the buffer. It uses a parameter 𝛾which is a ratio
of (i) a minimum buffer threshold, below which it downloads
the lowest bitrate and (ii) a target buffer threshold which it
tries to maintain. Conceptually 𝛾controls how strongly the
ABR should avoid rebuffering [48]. Higher values of 𝛾make
the algorithm conservative.
HYB: Throughput prediction without lookahead. Selects
bitrate using a simple heuristic. An algorithm widely used in
production (§5), HYB considers both the predicted throughput
and current buffer occupancy (HYB is short for hybrid). For
each chunk, HYB picks the highest bitrate that can avoid
rebuffering. Specifically, if 𝑆𝑗(𝑖) denotes the size of chunk 𝑗
encoded at bitrate 𝑖, 𝐵is the predicted throughput based on
past samples, and 𝐿the length of the buffer. HYB picks the
largest bitrate 𝑖such that 𝑆𝑗(𝑖)
𝐵
< 𝐿× 𝛽. Here, 𝛽can have
values between 0 and 1 (higher values represent aggressive
ABR behavior). 𝛽can be tuned to offset prediction errors in
throughput and to compensate for the greedy nature of the
approach which may make it susceptible to future buffering
events owing to unexpected throughput dips.
2.2
Ensuring High QoE for All Users
Despite widespread deployment, ABR algorithms continue
to be an active area of research [32, 34, 39, 48, 51, 59]. This
is because, while deployed ABR algorithms work well on
average, they do not work uniformly well across all network
conditions. A key reason for this is that ABR algorithms have
parameters (which we henceforth refer to as configurations)
that must be set in a manner sensitive to network conditions.
ABR algorithms need to run on many different networks, rang-
ing from cellular and WiFi networks at one end, to high-speed
broadband connections at the other. Given this diversity, net-
work conditions can vary significantly. Packet loss conditions
can vary by an order of magnitude or more across the globe
[25]. Network throughputs can also vary widely: for 90% of
traces in a large dataset, the trace’s maximum throughput is
more than twice its average throughput. Yet, unfortunately,
most ABR algorithms today either employ fixed configura-
tions or simple heuristics to adapt these configurations (§2.1).
Figures 1(a) and 1(b) show how the choice of ABR config-
uration depends on network conditions. Figure 1(a) shows the
bitrate and rebuffering ratio for two client sessions with the
HYB algorithm for three different values of its 𝛽parameter,
Cons (Conservative), Mod (Moderate), and Aggr (Aggres-
sive). The throughput behavior of the two sessions is shown
in Figure 1(c). If a publisher prefers to eliminate rebuffering,
Mod is suitable for session A, but Cons is better for session B.
Figure 1(b) shows that BOLA behaves similarly, with Mod
being the preferred setting for session A and Cons for session
B, to avoid rebuffering.
Figures 2(a) and 2(b) show the difficulty in setting the
discount factor with MPC, by comparing the performance
of FastMPC (no discount factor), and RobustMPC (discount
factor set by local heuristic) for two throughput traces with
different characteristics. In each figure, the top subgraphs
show the available throughput (green curve) and the through-
put estimate of FastMPC (red) and RobustMPC (blue). For
46
```


### Pagina 4
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
the left graph, although the throughput is generally good, the
sudden variations force RobustMPC to make overly conserva-
tive bitrate decisions, as well as incur more bitrate switches.
(bottom subgraph). In contrast, in Figure 2(b), the quicker and
more frequent throughput changes (top subgraph) result in
FastMPC experiencing rebuffering (middle subgraph), while
RobustMPC does not. This is just one example illustrating
the difficulty in picking parameters – in our evaluations (§4),
we found that RobustMPC was itself too aggressive when
selecting discount factors for some traces.
While this section uses synthetic traces for illustrative pur-
poses, our evaluations with real traces (§4) more extensively
demonstrate the limitations of current approaches with re-
spect to selecting parameters and the benefits of automatically
tuning ABR parameters to network conditions.
3
OBOE DESIGN
Oboe aims to ensure good QoE for all users by enabling ABR
algorithms to perform better across a wide range of network
conditions. The configurations of many ABR algorithms are
sensitive to network state, specifically to the value and vari-
ability of the available throughput between the client and the
video server. For example, 𝛽in HYB should be smaller when
available throughput is highly variable, while 𝛾in BOLA
should be higher. This explains why the algorithms perform
differently for different values of parameters on a given client
trace (§2.2). However, a line of prior work [17, 35, 38, 52, 60]
has observed that network connections are piecewise station-
ary: that is, connections can be in one of several distinct states
(§3.1), where each state is distinguished by stationarity in the
statistical sense (informally, a process is stationary if its sta-
tistical properties including mean and variance do not change
over time - see [43] for a more formal definition).
Oboe leverages the piecewise stationarity of network con-
nections to address the key challenge of sensitivity of config-
urations to network conditions. It does so using a two stage
design: (a) an offline stage where it pre-computes the best con-
figuration choice for each (stationary) network state (§3.2),
and (b) and an online stage, where during a session, it de-
tects changes in network state and applies the pre-computed
best configuration for the current (stationary) state (§3.3).
Oboe can also accommodate publisher specifications such
as session type (live vs. video-on-demand, time-to-live re-
quirements), bitrate levels or any explicit QoE tradeoffs (e.g.,
preference between rebuffering and average bitrate) (§3.2), by
using these to influence the selection of the best configuration
for each (stationary) network state in the offline stage.
3.1
Representing Network State
Most ABR algorithms today adapt bitrates based on the
throughput (more precisely, goodput) achieved by recently
Figure 3—The logical diagram of the offline pipeline used by Oboe
downloaded chunks. This perceived throughput already ac-
counts for network delays and loss-rates, as well as the dy-
namics of the underlying transport protocol.
The network throughput along a path is not necessarily a
stationary process [17, 35, 38, 52, 60]: flows at the bottleneck
along a path may change over time resulting in changes to
available throughput, or the bottleneck itself may shift [35].
An analysis of the throughput traces used in our evaluations
(§4) confirms the lack of stationarity when applied to the en-
tire trace. We analyze throughput traces using the Augmented
Dickey-Fuller (ADF [26]) test, a hypothesis test to check for
stationarity in a time series. Our evaluations on a dataset of
15,000 video streaming throughput traces show that 59.5%
were non-stationary (see §4.2 for details of the dataset), imply-
ing the presence of distinct mean and/or variance in different
segments of the traces.
However, prior work [17, 35, 38, 52, 60] shows that TCP
connection throughput can be modeled as a piecewise sta-
tionary process; the connection consists of multiple non-
overlapping segments where each segment is stationary and
often lasts for tens of seconds or minutes (e.g., Figure 8).
Moreover, Zhang et al. [60] show that the throughput in each
segment may be modeled as an i.i.d. process.
Motivated by these observations, Oboe defines network
state 𝑠by a tuple < 𝜇𝑠, 𝜎𝑠>, where 𝜇𝑠is the mean and 𝜎𝑠
the standard deviation of the client-perceived throughput in a
(stationary) segment of the underlying TCP connection.
3.2
Offline Mapping of Network States
To map network states to their optimal ABR configurations,
Oboe uses a pipeline (Figure 3) consisting of three compo-
nents – the ConfigEvaluator, the VirtualPlayer and the Con-
figSelector. The ConfigEvaluator takes a stationary through-
put trace as input, which represents a particular network state,
and drives the exploration of different ABR configurations
over this trace. It does so by using the VirtualPlayer which
models the dynamics of an actual video player. The Virtu-
alPlayer interfaces with the ABR algorithm implementation
and outputs the performance of different configurations of the
ABR. Finally, the ConfigSelector compares the performance
of different configurations and builds a ConfigMap, which
maps a given network state to the best configuration.
47
```


### Pagina 5
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Generating throughput traces for ConfigEvaluator. To
explore configuration space of an ABR algorithm on each net-
work state 𝑠, ConfigEvaluator needs a stationary throughput
trace to represent 𝑠. To generate such a trace, we explored two
different approaches. In one approach, we extracted stationary
segments from real traces using offline change point detec-
tion ([10], described in §3.3). Change points capture points
where the distribution changes. However, because we are not
guaranteed coverage (i.e., not all states might be observable
in real traces), we also explored a second approach which
involved generating a synthetic trace for each 𝑠with 𝑠’s mean
and standard deviation, assuming a Gaussian distribution for
the throughput samples. This was motivated by Dinda et al.
[38] who showed that the throughput of TCP flows of the
same size in a given stationary segment may be modeled as
a Gaussian distribution (also see §3.1). More recent work
also shows that TCP throughput is well modeled as a Markov
process, each of whose states may be modeled as a Gaussian
distribution [49]. We found that Oboe with synthetic traces
performed comparably to stationary segments from real traces.
So, ConfigEvaluator uses synthetic traces.
Specifically, ConfigEvaluator quantizes both mean and
standard deviation of throughput using a quantum (in our
experiments, of 50 Kbps), resulting in states (in our experi-
ments, 10,000), spread over a two dimensional space (in our
experiments, 0.05-10 Mbps) of throughput and standard devi-
ation. For each state, we generate a synthetic stationary trace.
We found that the benefits of finer quantization are marginal.
Estimating ABR performance with VirtualPlayer and
publisher specifications. Oboe uses VirtualPlayer, a trace-
based simulator that mimics the behavior of an actual video
player without downloading or rendering actual videos.
It takes as input a throughput trace and outputs the QoE
performance metrics of a video session for a specified
ABR algorithm. We have validated VirtualPlayer in §4.7.
In designing VirtualPlayer, we have decoupled ABR logic
(Figure 3), so the same implementation of the ABR logic
can be used in Oboe’s offline and online stage. Further, this
design provides an interface to the ABR designer through
which they can easily integrate their ABR algorithm with
Oboe without having to know about Oboe’s internals.
The VirtualPlayer also takes into account publisher spec-
ifications for bitrate levels, player buffer sizes (determined
by time-to-live requirements) and chunk size. These spec-
ifications are used by VirtualPlayer when it executes ABR
algorithms on the input traces, ensuring that the resulting Con-
figMap meets the publisher specifications. Finally, Oboe also
allows the publisher to optionally express an explicit QoE
tradeoff such as maintaining the rebuffering under a desired
threshold 𝑥%. Oboe derives a ConfigMap that meets the re-
buffering threshold in a best effort manner. We evaluate the
efficacy of this flexibility in §4.7.
Building the ConfigMap using ConfigSelector. To build
the ConfigMap, the ConfigEvaluator drives the exploration of
different configurations for an ABR algorithm. For a given
network state 𝑠, ConfigEvaluator sweeps through possible
configurations of the ABR algorithm using the VirtualPlayer.
For example, the 𝛽parameter in HYB can take values from 0
to 1, so ConfigEvaluator plays the trace for state 𝑠for multiple
values of 𝛽(quantized for efficiency, see below) in this range.
For each parameter value 𝑐𝑖, VirtualPlayer outputs a per-
formance vector 𝑉𝑖=< 𝑣1, 𝑣2, . . . 𝑣𝑚> where each 𝑣𝑘cor-
responds to the values achieved by 𝑐𝑖for a QoE metric (e.g.,
bitrate, rebuffering ratio, and more generally join time and
frequency of switching bitrates [23]). This set of performance
vectors with the corresponding parameter values are then sent
to ConfigSelector for picking the best configuration.
ConfigSelector takes the set of performance vectors and
determines the best configuration from them using vector
dominance. A configuration 𝑐𝑖is said to dominate 𝑐𝑗if 𝑉𝑖
element-wise dominates 𝑉𝑗(i.e., each element of 𝑉𝑖is bet-
ter than or equal to the corresponding element of 𝑉𝑗). This
step also takes into account any rebuffering tolerance, and
ConfigSelector applies this tolerance to select the maximal
performance vector. Deferring the selection of the maximal
vector for a given rebuffering tolerance to this stage (instead
of filtering vectors in the previous step) is beneficial: it mini-
mizes recomputation by allowing Oboe to quickly compute a
new maximal vector if the publisher changes the rebuffering
tolerance. At the end of this stage, Oboe obtains the Con-
figMap, a complete mapping of each network state to its
corresponding optimal ABR configuration.
Two optimizations can be used to quicken the rate of ex-
ploration of the ConfigEvaluator. The first is to quantize the
parameter sweep, so that configurations are evaluated at a
coarser granularity. This trades off some performance for
lower computational complexity. The second optimization is
based on the observation that there is generally a monotonic
relationship between parameter values and the performance.
For instance, for HYB (§2.1), the rebuffering ratio and av-
erage bitrate are monotonically non-decreasing with the pa-
rameter 𝛽. Based on this observation, we can instead use an
𝑂(log 𝑛) binary search of the configuration space instead of
doing a full 𝑂(𝑛) sweep of all configurations.
3.3
Online ABR Tuning
Oboe uses the ConfigMap generated offline, and live through-
put measurements from the video player to dynamically
change ABR configurations during a video playback. It does
this by using an online change point detection algorithm
[14]. This algorithm identifies, in an online fashion, if
the distribution of the throughput samples has changed
significantly, signaling a state transition. When a change
point is detected, the algorithm also provides the new state
48
```


### Pagina 6
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
Figure 4—Logical diagram of Oboe’s online pipeline
𝑠’s mean and standard deviation. Oboe’s ChangeDetector
(Figure 4) implements the change point detection algorithm,
and the ReconfEngine is responsible for updating the
ABR configuration based on a new network state and the
ConfigMap.
Change point detection algorithms. Such algorithms ana-
lyze a time series and check if there are regions in the time
series where the underlying distribution of the data changes
to a different set of parameters. Offline change-point methods
require the full time series to be available, whereas online
methods work with a continuous stream of samples as they
become available. We focus on online methods, since Oboe
identifies change points for an in-progress session and dynam-
ically changes configurations.
While several techniques exist for change point detection
[22, 33, 36, 44, 54, 58], we focus on probabilistic methods
[14, 18, 24, 57]. Further, we use a Bayesian online proba-
bilistic change-point detector [14] for two reasons. First, in
[14], a sequence of observations can be partitioned into non-
overlapping states such that the observations are i.i.d. condi-
tioned on a given network state 𝑠. This view aligns well with
the way we have defined a network state (§3.1). Further, the al-
gorithm is fast and requires no prior knowledge about the data
stream, matching our scenario. We use the implementation
provided in [10] and integrate it with the ChangeDetector.
Detecting changes in network state. During a video ses-
sion, ChangeDetector is continually fed with a series of obser-
vations of the network throughput, which it uses to detect state
changes. ChangeDetector calculates throughput and standard
deviation by only considering those samples which belong
to the current state. To generate inputs to ChangeDetector,
one approach is to use each downloaded chunk to obtain a
single throughput sample. However, this may be too coarse-
grained, and prevent detection of changes in network state
that occur during the chunk download. Instead, we use fine
grained samples recorded at periodic intervals (tens of mil-
liseconds) during the download of each chunk. Players such
as Dash.js already periodically log intermediate throughput
samples during a chunk download, so obtaining these sam-
ples does not incur any additional overhead. We only need
to modify players to report these samples to Oboe. The set
of samples are provided to ChangeDetector after the chunk
download, and any change in state is only detected at the end
of the chunk download. This is acceptable since any action
that can be taken by the ABR algorithm (such as a bit rate
switch) only impacts subsequent chunks. In the rarer case that
an ABR algorithm abandons the download of a chunk that
takes too long, the report is sent when the chunk download is
abandoned. §4.8 evaluates the overheads of ChangeDetector.
An alternative approach to changing configurations is to
use an exponentially weighted moving average (EWMA) of
the mean and standard deviation of throughput samples and
to lookup the corresponding configuration. We experimented
with such an approach and found its performance unsatisfac-
tory. The approach can result in continual and unnecessary
reconfigurations, since throughput may vary across samples
even when the network is (statistically) stationary. Damping
these changes can result in slow reaction times when a recon-
figuration is actually beneficial. In contrast, Oboe (i) models
the underlying TCP connection as a sequence of states; (ii)
does not make changes to the configuration within a given
network state; and (iii) only reconfigures when a state change
is observed.
Reconfiguring ABR Algorithm. When a change in the net-
work state is detected, the ChangeDetector signals the change
and the new network state 𝑠to the ReconfEngine. The Recon-
fEngine then searches a neighborhood of radius 𝑟in the Con-
figMap to select the configuration to use for state 𝑠. Specifi-
cally, if state 𝑠is a point in a 2-dimensional space of average
throughput and standard deviation of throughput, then it picks
the most conservative ABR configuration within a search ra-
dius 𝑟around 𝑠. It does this for two reasons. First, because
Oboe quantizes the network states, it might not have precom-
puted the best configuration for 𝑠. Second, the estimated new
network state 𝑠may have some error, for example, due to
inefficiencies in the client download stack [27]. Given these
sources of uncertainty, Oboe chooses to be safe in its selec-
tion of the best configuration for 𝑠. Finally, ReconfEngine
configures the ABR algorithm, and the reconfigured ABR
algorithm is ready to compute the bitrate decision to be used
for the next chunk at this point.
4
EVALUATION
In this section, we demonstrate Oboe’s ability to auto-tune
three existing algorithms: RobustMPC, BOLA and HYB. We
also compare an Oboe-tuned RobustMPC to Pensieve [39].
4.1
Metrics
The performance of a video session depends on multiple fac-
tors. Average bitrate and rebuffering ratio were found to have
the most impact on user quality of experience [23], though
other factors such as changes in bitrates during a session can
play a role [23]. There is no consensus on how to best cap-
ture a user’s QoE. Consequently, ABR algorithms today are
designed to optimize different metrics. For instance, HYB
49
```


### Pagina 7
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Figure 5—A scatter plot of average bitrate and rebuffering ratio between the Virtu-
alPlayer and real Dash.js player
and BOLA primarily maximize average bitrate subject to low
rebuffering. In contrast, other algorithms [39, 59] have been
designed to optimize a QoE metric which is a linear combina-
tion of bitrate, rebuffering and bitrate changes (smoothness).
With Oboe, our primary evaluation goal is to demonstrate
the extent to which it can improve the underlying metrics that
an ABR algorithm is designed for. Thus, our evaluations with
BOLA and HYB focus on average bitrate and rebuffering,
while those with MPC+Oboe focus on the linear combination
of QoE (which we refer to as QoE-lin, [59]), defined as
follows. For a video with 𝑁chunks, let 𝑅𝑖be the bitrate
chosen for chunk 𝑖. Then, the magnitude of bitrate changes
𝑀may be defined as 𝑀= ∑︀𝑁−1
𝑖
|𝑅𝑖+1 −𝑅𝑖|. If the ses-
sion experiences a total of 𝑇seconds of rebuffering, then,
QoE-lin(𝑝, 𝑐) = 1
𝑁*∑︀
𝑖(𝑅𝑖−𝑝𝑇−𝑐*𝑀), where 𝑝and 𝑐
represent scaling penalties applied to rebuffering and changes
in the session. This function may be viewed as the session
QoE averaged over the number of chunks. For our videos
that had a maximum bitrate of 4.3 Mbps, we use 𝑝= 4.3 and
𝑐= 1 as our default parameters (following previous work that
set default rebuffering penalty equal to the maximum bitrate
value [39, 59]).
Even when an algorithm optimizes a metric such as
QoE-lin, it is important to understand the distributions of
underlying factors. The underlying factors represent concrete
application performance that publishers understand how to
reason about. Moreover, a unified metric like QoE-lin can
obscure important differences. For example, two sessions
may have the same QoE-lin but different performance in
underlying metrics, leading to varied user experience. So, we
also present graphs of these metrics.
4.2
Methodology
Implementation. For RobustMPC, we used the imple-
mentation available at [11]. Our implementation of BOLA
[@bola] is from the Dash.js player. The implementation
of HYB is a variant of the algorithm used in a large-scale
deployment. These ABR algorithms and Oboe’s online stage
(change point detection and ABR reconfiguration) run on
the server in our experiments. Our client runs the Dash.js
video player (version 1.2), a reference player implemented
in JavaScript by the MPEG-DASH forum [7]. We modified
Dash.js to send client player state information (e.g. buffer
length, video play state and throughput measurements) to
Oboe (§5). This player runs on the Google Chrome browser
(version 61) in our experiments. In §5, we show that Oboe
can also be run as a cloud service.
Testbed setup. Our evaluations measure ABR performance
by delivering a video stream (the “EnvivioDash3” video from
the MPEG-DASH reference videos [12]) from a video host-
ing server to a client, while varying network conditions us-
ing throughput traces from real user sessions. We use bi-
trates {300, 750, 1200, 1850, 2850, 4300}𝑘𝑏𝑝𝑠with a 4 sec-
ond chunk duration and total length of 192 seconds. We focus
on this video as it has been used in prior work [39], and we
do not consider videos of longer duration because we only
have throughput traces available for a video publisher that
serves short music videos (as we discuss below). The video
is hosted on an Apache server. Both the server and client
software run on the same 8-core, 4 Ghz, Intel i7 commodity
desktop with 12 GB RAM running Ubuntu 16.04. Between
server and client, we emulate different network conditions
using the Chrome DevTools API [9]. This allows us to control
the upload/download throughput as well as latency using the
Chrome-Remote-Interface based on throughput traces [5]. We
use 571 throughput traces3 from our dataset (discussed below)
for this emulation. All our testbed experiments use a client
buffer of 2 minutes.
Datasets. We use throughput traces from real user sessions
collected over a three month period. Each trace contains the in-
dividual chunk sizes and their download times for on-demand
video sessions from a publisher that serves short (4-6 minute)
music videos. We derive throughput by dividing the chunk
sizes by their download durations. The traces contain sessions
that used desktops with wired connections and also sessions
on mobile devices using WiFi or cellular connections. Like
previous work [39, 59], we primarily focus on traces that
have less than 6 Mbps average throughput, since this is the
regime where bitrate switching decisions are likely to have
QoE impact. We filtered out traces which were too short for
playing our entire 192 second video, after which we obtained
5K traces from wired desktops and 4K sessions from WiFi or
3G/4G mobile devices. Our testbed experiments use a subset
of 571 traces with roughly the same number of traces sampled
from each of desktop and mobile clients.
VirtualPlayer setup. Recall that Oboe uses the Virtu-
alPlayer to obtain a ConfigMap for any ABR algorithm.
Since the majority of our results use an actual testbed with
the Dash.js player, the benefits of Oboe in our evaluation
results already arise despite any inaccuracies in building the
ConfigMap on account of using the VirtualPlayer. That said,
we have also verified that the VirtualPlayer does a good job
3Available at https://github.com/USC-NSL/Oboe
50
```


### Pagina 8
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
Figure 6—The percentage improvement in QoE-lin of MPC+Oboe over RobustMPC for the Testbed experiment. The distribution of average bitrate, rebuffering ratio and bitrate
change magnitude for the schemes is also shown.
Figure 7—QoE-lin of MPC+Oboe compared to RobustMPC
of tracking the performance of the actual ABR algorithms.
For instance, Figure 5(a) and 5(b) demonstrates this for the
HYB algorithm. The figures shows the correlation for the
average bitrate and rebuffering ratio for 100 throughput
traces randomly sampled from our dataset using HYB
on the VirtualPlayer compared to using an actual Dash.js
player. For both metrics, the graph closely tracks the
𝑦= 𝑥line indicating close correlation. Given these close
correlations, we use the VirtualPlayer in §4.7 to explore
Oboe’s performance over a larger range of diverse settings
and our entire set of traces.
4.3
Oboe with RobustMPC
We now demonstrate that Oboe can be used to auto-tune Ro-
bustMPC, the best performing variant of the MPC algorithms.
The resulting MPC+Oboe uses the best value of the discount
parameter 𝑑corresponding to the current network state, re-
placing RobustMPC’s online adaptation based on throughput
estimates obtained over the past 5 chunks (§2).
Figure 6(a) shows the CDF of the percentage improvement
in QoE-lin of MPC+Oboe over RobustMPC.4 MPC+Oboe
improves QoE-lin for 71% of sessions, with an overall av-
erage QoE-lin improvement of 17.62% across all sessions.
In particular, for 19% of the sessions, QoE-lin improves
by more than 20%. For the sessions MPC+Oboe is unable to
improve RobustMPC, its performance degradation is mostly
under 8%. Figures 6(b), 6(c) and 6(d) show the constituent
QoE metrics. While MPC+Oboe achieves distributionally sim-
ilar bitrates as RobustMPC as shown in 6(b), it significantly
reduces rebuffering across sessions: the number of sessions
with rebuffering reduces from 33.2% to 5.3%. Further, it
also achieves better playback smoothness by improving the
4The increase in QoE-lin over RobustMPC relative to the absolute QoE-lin value
of RobustMPC expressed as a percentage.
Figure 8—An example session showing how MPC+Oboe is able to outperform Ro-
bustMPC by reconfiguring the discount parameter when a network state change is de-
tected.
median per chunk change magnitude by 38% (Figure 6(d)). Fi-
nally, Figure 7 shows the CDF of QoE-lin for MPC+Oboe
and RobustMPC, and indicates MPC+Oboe distributionally
performs better.
Figure 8 illustrates, using a single session, why MPC+Oboe
performs better than RobustMPC. The top graph shows
throughput as a function of time, which includes an initial
stable state followed by a drop in throughput. The middle
graph shows how the discount factor 𝑑of both RobustMPC,
and MPC+Oboe vary (the predicted throughput for each
system is reduced by a factor of
1
1+𝑑, where 𝑑is shown on
the y-axis). During the initial stable state, when prediction
errors are low, RobustMPC steadily lowers its discount factor
leading to more aggressive bitrate selections (not shown).
This results in a rebuffering event 44 seconds into the session
(lowest graph shows buffer occupancy with 0 indicating a
rebuffering event). In contrast, MPC+Oboe does not incur a
rebuffering event and maintains a fixed 𝑑during the initial
stable state. At 29 sec, it detects a change in the network state
and adapts its discount factor, leading to more conservative
bitrate selections.
4.4
Oboe vs. Pensieve
Pensieve [39] uses deep reinforcement learning [41, 42],
a combination of deep learning with reinforcement learn-
ing [50], and has been shown to outperform existing
ABRs, including RobustMPC [39] in some settings. Since
51
```


### Pagina 9
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Figure 9—The percentage improvement in QoE-lin of MPC+Oboe over Pensieve for the 0-6 Mbps throughput region. The distribution of average bitrate, rebuffering ratio and
bitrate change magnitude for the schemes is also shown.
Figure 10—Validation of our training
methodology for Pensieve.
Figure 11—QoE-lin of MPC+Oboe
compared to Pensieve
Figure
12—Benefits
of
specializing
Pensieve models. Each curve shows the
QoE improvement of MPC+Oboe rela-
tive to each Pensieve model.
Figure
13—QoE
improvement
of
MPC+Oboe over two ways of dy-
namically selecting from specialized
Pensieve models.
MPC+Oboe outperforms RobustMPC as well, we explore
how MPC+Oboe performs relative to Pensieve. Our exper-
iments use the Pensieve implementation provided by the
authors [11].
Pensieve Re-Training and Validation. Before evaluating
Pensieve on our dataset, we retrain Pensieve using the source
code on the trace dataset provided by the Pensieve authors
[11]. This helps us validate our retraining given that deep
reinforcement learning results are not easy to reproduce [29].
We experimented with five different initial entropy weights
in the author suggested range of 1 to 5, and linearly reduced
their values in a gradual fashion using plateaus, with five
different decrease rates until the entropy weight eventually
reached 0.1. This rate scheduler follows best-practice [55].
From the trained set of models, we then selected the best
performing model (an initial entropy weight of 1 reduced
every 800 iterations until it reaches 0.1 over 100K iterations)
and compared its performance to the pre-trained Pensieve
model provided by the authors. Figure 10 shows CDFs of
QoE-lin for the pretrained (Original) model and the model
trained by us (Retrained). The performance distribution of the
two models are almost identical over the test traces provided
by the Pensieve authors, thereby validating our retraining
methodology.
Having validated our retraining methodology, we trained
Pensieve on our dataset with the same complete strategy
described above. For this, we pick 1600 traces randomly from
our dataset with average throughput in the 0-6 Mbps range.
The number of training traces, the number of iterations per
trace, and the range of throughput are similar to [39]. We then
compare Pensieve and MPC+Oboe over a separate test set of
traces also in the range of 0-6 Mbps (§4.2).
Comparison with Pensieve. Figure 9(a) shows the CDF of
the percentage improvement in QoE-lin for MPC+Oboe
over Pensieve. MPC+Oboe outperforms Pensieve for 81% of
the sessions, with a QoE-lin improvement of 23.9% in aver-
age across all sessions. 25% of the sessions achieve more than
20% QoE-lin improvement. For the sessions MPC+Oboe
is unable to improve over Pensieve, the performance differ-
ence is mostly less than 5%. Figures 9(b), 9(c) and 9(d) show
that MPC+Oboe distributionally outperforms Pensieve with
respect to all underlying metrics. It reduces the number of
sessions with rebuffering from 10.7% to 5.3%, reduces the
median per chunk change magnitude by 43.9%, and improves
median and 95th percentile average bitrate by 2.6% and 4.7%
respectively. Finally, Figure 11 shows the CDF of QoE-lin
for MPC+Oboe and Pensieve, and indicates MPC+Oboe per-
forms distributionally better.
Analyzing Pensieve performance. To understand where
these performance improvements were coming from, we ex-
amined the relative performance of these two schemes in the
0-3 Mbps range (i.e., traces having an average throughput be-
tween 0-3 Mbps). In this more constrained range of network
conditions, we found that MPC+Oboe achieves bigger gains
over Pensieve (average QoE-lin improvement in 0-3 Mbps
is 46.23%). We hypothesize that this performance difference
stems from the fact that Pensieve builds a single model which
does not specialize to different throughput ranges.
To test this, we trained a separate Pensieve model only with
traces that have an average throughput between 0-3 Mbps
range and compared it with MPC+Oboe. Figure 12 shows
the per session QoE-lin improvement of MPC+Oboe com-
pared to Pensieve models trained for 0-3 Mbps (which we
refer to as Pens-Specialized) and for 0-6 Mbps. The me-
dian QoE-lin improvement with MPC+Oboe over Pens-
Specialized is 10.49%, while the median improvement over
52
```


### Pagina 10
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
Figure 14—Percentage improvement in bitrate and rebuffering of BOLA+Oboe over BOLA (a),(b) and HYB+Oboe over HYB (c), (d)
Figure 15—Average QoE-lin of MPC+Oboe with various throughput predictors
Pensieve is 19.9%. This indicates specializing the model does
improve Pensieve’s performance.
Thus, Pensieve’s model is as yet unable to create special-
ized versions of itself based on the session characteristics.
By contrast, Oboe specializes parameters for every network
state and therefore performs better. We have also validated
Pensieve’s inability to specialize in several other ways: build-
ing a model for the 3-6 Mbps and showing that it performs
better with test data in that range compared to a 0-6 Mbps
model; checking that a 0-6 Mbps model performs better for
data in that range compared to a 0-100 Mbps model; and
ensuring that these results hold even when the training set is
doubled. It is hard to pinpoint exactly why Pensieve is unable
to learn to be more conservative in the 0-3 Mbps range; deep
neural network models remain a black box despite efforts by
the machine learning community to make these models more
transparent [45], and obtaining such understanding may need
further advances in interpretable deep learning models.
A model selector with Pensieve . One way to improve Pen-
sieve’s specialization might be to train different models for
different throughput ranges and use the model more suited
to the network conditions. To test the efficacy of this ap-
proach, we used two models (specialized for 0-3 Mbps and
3-6 Mbps), and tried two different model selectors. Pens-
SelMultiple switches models throughout the session, using
the average throughput of the past 5 chunks. Pens-SelOnce
starts with the 0-6 Mbps model, selects either the 0-3 Mbps
or 3-6 Mbps model based on the average throughput of the
first 5 initial chunks, and does not switch thereafter.
Figure 13 shows CDFs of per-session QoE-lin improve-
ment of MPC+Oboe over these selectors. MPC+Oboe is able
to outperform both Pens-SelMultile and Pens-SelOnce, with
average QoE-lin improvements of 14.2% and 24.32% re-
spectively. Even though one of the model selection schemes
offers some improvements over the 0-6 Mbps Pensieve model,
the benefits are modest. We hypothesize that this behavior
is due to the dynamic selection of distinct Pensieve models,
which can interfere with reinforcement learning’s decision
choices, since, during training, the reinforcement learning
algorithm assumes there is no such third party intervention.
4.5
Oboe with other ABR Algorithms
Oboe can also improve other existing ABR algorithms such
as BOLA and HYB, which are designed to maximize average
bitrate while minimizing rebuffering.
BOLA. BOLA+Oboe tunes 𝛾(§2), which determines how
much the algorithm strives to avoid rebuffering. BOLA, as
implemented in Dash.js, uses a fixed default value of 𝛾=
−10.28. Figure 14(a) and 14(b) show CDFs of per session
performance improvement over BOLA with respect to av-
erage bitrate and rebuffering ratio. BOLA+Oboe maintains
the rebuffering ratio of BOLA while improving average bi-
trates for more than 83% of sessions with an overall increase
of 7.2% in average across all sessions. For sessions where
BOLA+Oboe does not outperform BOLA, its degradation is
less than 3.1%.
HYB. The performance of HYB is sensitive to the choice
of 𝛽parameter, which HYB+Oboe tunes. In production, HYB
uses 𝛽= 0.25, determined using A/B tests in a large-scale de-
ployment. Figure 14(c) and 14(d) show CDFs of per session
performance improvement of average bitrate and rebuffer-
ing ratio over HYB. As with BOLA, HYB+Oboe maintains
similar rebuffering ratios as shown in 14(d), but improves
bitrates for 98% of sessions with an overall average bitrate
improvement of 8.32% in average across all sessions.
4.6
Sensitivity experiments
Alternative throughput traces. To understand how Oboe
works on throughput datasets beyond those discussed in §4.2,
we evaluated Oboe on two other datasets, FCC [8] and HS-
DPA [46] that have been used in recent work [39, 59]. FCC
is a broadband dataset, while HSDPA contains throughput
traces collected from video streaming sessions over 3G net-
works in Norway using mobile devices. Our comparisons use
the traces and a Pensieve model pre-trained for those traces
available at [11]. We focus our evaluations on MPC+Oboe
and Pensieve, given that Pensieve has been shown to out-
perform existing ABR schemes including RobustMPC on
53
```


### Pagina 11
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Figure 16—Comparing HYB with multiple fixed configurations and HYB+Oboe for various settings
these traces. Our results show that MPC+Oboe continues to
perform better than RobustMPC on these traces. Further, rela-
tive to Pensieve, MPC+Oboe improves QoE-lin by an aver-
age of 6.94% across the FCC dataset and 10.92% across the
HSDPA dataset. These improvements are more modest than
those in Figure 9(a). The vast majority of traces in the FCC
and HSDPA set have an average throughput under 3 Mbps
(over 95% for FCC and 98% for HSDPA). The results cor-
roborate Figure 12 which indicates that MPC+Oboe provides
more modest gains over Pensieve when the latter is trained
and evaluated on datasets with a narrow throughput range.
MPC+Oboe provides larger gains in settings like the traces
discussed in §4.2, where only 41% traces are under 3 Mbps
and 59% are in the 3-6 Mbps range.
Alternative throughput prediction methods. Our experi-
ments with RobustMPC rely on throughput prediction based
on the harmonic mean of prior throughput samples (follow-
ing earlier work [39, 59]), with Oboe tuning the configura-
tion to compensate for prediction errors. We next consider
if Oboe’s benefits hold if RobustMPC were to have more
accurate throughput predictions, potentially by using alter-
nate prediction methods [49]. Rather than using a specific
prediction technique, we consider an ideal (and unachievable)
approach that we denote as Ideal(T), which can exactly predict
the average throughput over the next T seconds. Our experi-
ments were conducted in simulation, using the VirtualPlayer,
and the testbed experiment traces (§4.2).
Figure 15 shows the average QoE-lin across the traces
for RobustMPC and MPC+Oboe using both the default har-
monic mean approach and Ideal(T) for different values of T.
Although RobustMPC performs better with an ideal predictor,
Oboe still provides benefits, achieving an average improve-
ment in QoE-lin of 6.34% for Ideal(5) and of 1.8% for
Ideal(10), compared to a 16.1% improvement with the har-
monic mean estimator. While the magnitude of benefits is
smaller with the ideal prediction approach, in practice Oboe
will likely result in larger benefits, since even more sophisti-
cated schemes [49] cannot achieve the ideal predictions, and
the errors are likely to grow with larger T.
Oboe can improve performance over RobustMPC even
when an Ideal(T) prediction method is used for two reasons.
First, 𝑇may not match the duration of chunk downloads
with RobustMPC, which depends on the exact sequence of
bitrates chosen during the look-ahead window. The duration
is not known a priori, since RobustMPC itself determines the
bitrates based on a provided prediction. Second, the decisions
made by RobustMPC are over a small look-ahead window,
which may not guarantee optimality over the entire session
duration.
4.7
Oboe Across Various Settings
In §4.5 we have shown that Oboe outperforms other ABR
algorithms when compared to their default configurations.
We now explore, for HYB, whether Oboe outperforms all
parameter settings of HYB and whether it can tune ABRs
based on content type and publisher specifications. For these
experiments, we use the VirtualPlayer described in §3.2.
Comparison against all fixed configurations. To explore
different fixed configurations, we run HYB with 10 different
fixed 𝛽s and compare with HYB+Oboe. We summarize the
performance for each configuration by considering the (i)
median of the average bitrate and the (ii) 90th percentile of
the rebuffering ratio across test traces. In this experiment, we
also consider an Oracle which is the best fixed configuration
for each throughput trace with respect to two metrics that
HYB tries to optimize.
Figure 16(a) and 16(b) compare HYB, HYB+Oboe and
Oracle over desktop, and mobile traces respectively. While
Oracle and HYB+Oboe are depicted as single dots since their
performance is uniquely determined, we present a frontier
for HYB that shows its performance for different fixed con-
figuration. Figure 16(a) shows that HYB+Oboe outperforms
HYB in the sense that there is no fixed configuration for HYB
that does better than HYB+Oboe performance. HYB+Oboe
improves the average bitrates of the median session by 3.2%,
while achieving similar rebuffering ratio. Alternately, it re-
duces the 90th percentile rebuffering ratio from 1.9% to 0%,
while maintaining similar bitrates. A similar result holds for
mobile traces (Figure 16(b)). Thus, even if publishers were
to find the best fixed parameter choice for HYB, Oboe would
outperform that choice because it dynamically adapts the
parameters.
Comparison under different publisher specifications.
Our results so far are for a VoD (video on demand) setting
with a maximum buffer size of 2 minutes. Figure 16(c)
54
```


### Pagina 12
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
Figure 17—Avg. of avg. bitrate and
fraction of sessions with rebuffering for
HYB+Oboe and different publisher pref-
erences
Figure 18—Avg. of avg. bitrate and
fraction of sessions with rebuffering
for RobustMPC and different publisher
preferences
depicts performance for live video (which uses a maximum
buffer size of 20 seconds to mimic live settings). HYB+Oboe
outperforms HYB for this setting, though we note that the
bitrate of both approaches degrades relative to the VoD
setting since the baseline HYB switches to higher bitrates
more conservatively owing to the smaller buffer sizes.
Finally, Figure 16(d) depicts performance for higher bi-
trate levels ({1002, 1434, 2738, 3585, 4661, 5886}𝑘𝑏𝑝𝑠) and
a chunk size of 5 seconds. Even for these choices, HYB+Oboe
outperforms HYB, demonstrating its ability to adapt to differ-
ent publisher specification.
Accommodating publisher’s rebuffering tolerance. Oboe
allows the publisher to optionally specify explicit rebuffer-
ing preferences (§3). ABR algorithms such as RobustMPC
which use the QoE-lin function may permit this indirectly
by adjusting QoE-lin weights (§2.1). Figure 17 shows the
effectiveness of these approaches, showing the average of
average bitrates, and the fraction of sessions with rebuffering
for HYB+Oboe. As the publisher makes its rebuffering pref-
erence stricter (from 2%-0%), HYB+Oboe achieves lower
rebuffering ratios close to the target rebuffering tolerance. In
contrast, Figure 18 shows that RobustMPC is less effective
at controlling rebuffering by adjusting its rebuffering penalty
when the weight on the rebuffering term is varied between
100 (strictly avoid rebuffering) to 4.3.5 We find that even with
a very high rebuffering penalty of 100, RobustMPC causes
rebuffering in 11% of the sessions. This shows the benefit of
Oboe’s approach which gives direct control over the underly-
ing metrics.
4.8
Oboe Overhead
Computing the ConfigMap incurs a one-time cost, since the
map can be reused across all clients once the it is built. Com-
puting the best parameter configuration for one network state
takes about 12 seconds on a single core. This task is perfectly
parallelizable, so computing 10K network states (§3) will
take approximately 3.5 hours to explore with two machines
of 48 cores each. We have also analyzed the processing over-
head incurred by the ChangeDetector module of Oboe. We
measure the time taken by ChangeDetector for every decision
5We used a change penalty of 0 for fair comparison.
Figure 19—Comparing prototype Oboe with commercial client side ABR implemen-
tation in average bitrate and rebuffering ratio.
Figure 20—Time between consecutive
bitrate switches for two commercial
ABRs
Figure 21—Variance in bitrate levels
across videos from two content publish-
ers.
cycle across our experiments, and the measurement indicates
that the median processing time of ChangeDetector is around
14 ms. Since each decision is made at a chunk boundary and
chunks are 4 seconds, ChangeDetector accounts for less than
0.35% overhead.
5
DEPLOYMENT CONSIDERATIONS
The offline stage of Oboe can be run on the cloud, but several
choices exist for the online stage, ranging from embedding
the online stage entirely in the client player, or moving some
or all of the online stage to the cloud. In our implementation,
Oboe’s components run on the server side. This mimics a
cloud implementation, which has the benefits of other cloud
software: fast update deployment, device independence, etc.
[4]. We leave a detailed comparison of these choices to future
work, but explore, in this section, the feasibility of running
the online stage on the cloud.
To this end, we have implemented a restricted version of
HYB+Oboe on AWS. This limited version of Oboe imple-
ments HYB and incorporates tuning based on publisher speci-
fications but not network state. In our implementation, a client
player periodically reports player state (such as buffer length
and current bitrate) and throughput samples to a Oboe cloud
server and receives bitrate decisions in return. For 10 player
features and two chunk downloads per second, the commu-
nication overhead is 6.4 Kbps, negligibly small compared to
the size of video chunks. Figures 19(a) and 19(b) compare the
performance of this implementation against a client player
running HYB over 20K sessions collected during a two-week
pilot deployment. Oboe is comparable in performance to the
client side player and even improves bitrate slightly (because
it was tuned to this publisher’s specification).
55
```


### Pagina 13
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
We expected a cloud implementation would perform worse
because of the latency induced by client-server communica-
tion. However, we found that most of the bitrate switching
decisions occur on timescales much longer than the client-
server latencies. Figure 20 shows the CDF of the time interval
between consecutive bitrate switches for ABR algorithms in
two widely used video players(Adobe’s Flash [3] and Mi-
crosoft Smooth Streaming [1]). The figure shows that over
95% of switching decisions occur at intervals higher than
1 second for both players. This suggests that a cloud-based
deployment is viable.
6
DISCUSSION AND FUTURE WORK
Performance improvements for all sessions. As our re-
sults (e.g., Figure 6(a)) show, Oboe improves the perfor-
mance for most but not all sessions relative to the ABR al-
gorithm it tunes. For instance, after inspecting the results
in §4.3, we have found that MPC+Oboe typically improves
performance relative to RobustMPC by reducing rebuffering
and/or the magnitude of bitrate changes, but at the expense of
slightly lower bitrates. The resulting QoE-lin is improved
for most sessions, indicating Oboe does a good job of properly
balancing the various factors, but some sessions see lower
QoE-lin. More generally, designing an ABR approach that
can optimize the performance of all sessions is a hard problem
that needs more research.
Sharing ConfigMap across videos. Oboe need not per-
form offline precomputation for each individual video, as
it can use a single ConfigMap for a class of videos that follow
a similar bitrate encoding scheme. Figure 21 shows that two
popular video publishers use similar encoding schemes across
two thousand videos each. Publisher 1 uses 7 distinct bitrate
levels, and the coefficient of variance across bitrates within
each level is only 0.13, while Publisher2, uses 10 distinct
bitrate levels, and the coefficient of variance across bitrates
within each level is only 0.067. This indicates the potential to
share a single ConfigMap across videos.
Generality of Oboe. While we have shown that Oboe can
tune a variety of configuration parameters across several ABR
algorithms, whether Oboe can tune all algorithms and all pa-
rameters is an open question. It is unclear if Oboe can directly
augment Pensieve, since a model learned by reinforcement
learning may not interact well with intermediaries such as
Oboe. However, combining the benefits of Oboe and Pensieve
in other ways is an interesting avenue for future work.
7
RELATED WORK
Tuning ABR Algorithm Configurations. The BBA2 algo-
rithm [32] tunes its lower reservoir based on buffer occupancy
dynamics, while MPC [59] adapts its throughput discount fac-
tor based on past prediction errors (§2). In contrast to such ad-
hoc heuristics, Oboe selects configuration parameters based
on network state, and publisher specifications. The approach
is generically applicable to many ABR algorithms. Newer
congestion control protocols like BBR [19] estimate network
throughput, which if exposed, could benefit Oboe.
Learning ABR Algorithms. Among ABR algorithms that
use Reinforcement Learning and other machine learning tech-
niques [20, 21, 39, 40, 53], Pensieve [39] has been shown to
perform the best. While Pensieve does not specialize to differ-
ent throughput regimes, Oboe performs better by specializing
parameter values for each network state independently.
Other work in self-tuning. Beyond ABR algorithms, self-
tuning approaches have been explored in other contexts. Win-
stein et al. [56] used simulations to determine TCP parameters
for different settings, while Semke et al. [47] proposed tuning
TCP socket buffers to ensure high throughput. More gener-
ally, Google Vizier [28] performs such black-box tuning as
a service. While Vizier can potentially be used to implement
the offline phase of Oboe, our work identifies underlying
principles (such as the piecewise stationarity of available
throughput) that forms the basis for the tuning.
Video QoE. Several researchers have pointed out that
sub-optimal ABR performance can significantly impact
user-engagement and hence revenue [16, 37]. Others have
looked at quality issues that occur when multiple players
start to compete for bandwidth [15, 30, 31, 34] In contrast,
Oboe improves the QoE performance of several ABR
algorithms across a range of different network conditions by
automatically tuning their parameters.
8
CONCLUSION
Oboe is a system for automatically tuning ABR algorithms
by adapting ABR configurations in realtime to match the
current network state. Picking configurations in a manner
informed by network state and publisher preferences distin-
guishes Oboe’s approach from heuristics used today that do
not consider these factors. Oboe significantly improves the
performance of BOLA, HYB and RobustMPC; further, for
nearly 80% of the sessions in our dataset, Oboe integrated
with RobustMPC improves QoE-lin relative to Pensieve
and the improvements exceed 20% for 25% of the sessions.
Acknowledgments. We thank our shepherd, Mohammad Al-
izadeh and the anonymous reviewers for their constructive
feedback. We thank Oleg White, Yan Li and Shubo Liu
for their assistance obtaining the throughput data and for
helpful discussions. This work was funded in part by the
National Science Foundation (NSF) Awards CNS-1618921,
CNS-1564242, and CNS-1413978; and the ARO, under the
U.S. Army Research Laboratory award W911NF-09-2-0053.
Any opinions, findings and conclusions or recommendations
expressed in this material are those of the authors and do not
necessarily reflect the views of NSF or ARO.
56
```


### Pagina 14
```text
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
Z. Akhtar et al.
BIBLIOGRAPHY
[1] Microsoft Smooth Streaming. http://www.iis.net/downloads/microsoft/smooth-
streaming.
[2] Toward A Practical Perceptual Video Quality Metric.
https://medium.
com/netflix-techblog/toward-a-practical-perceptual-video-quality-metric-
653f208b9652.
[3] Adobe OSMF player. http://www.osmf.org.
[4] Oracle: 5 Reasons to Consider SaaS for Your Business Applications. http://www.
oracle.com/us/solutions/cloud/saas-business-applications-1945540.pdf.
[5] Chrome Remote Interface.
https://github.com/cyrus-and/chrome-remote-
interface.
[6] Cisco: It Came to Me in a Stream. https://www.cisco.com/web/about/ac79/docs/
sp/Online-Video-Consumption_Consumers.pdf.
[7] DASH Industry Forum. https://github.com/Dash-Industry-Forum/dash.js.
[8] Federal Communications Commission. Raw Data - Measuring Broadband Amer-
ica.
www.fcc.gov/reports-research/reports/measuring-broadband-america/raw-
data-measuring-broadband-america-2016.
[9] Google-Chrome: Chrome DevTools Protocol. https://chromedevtools.github.io/
devtools-protocol/tot/Network/.
[10] Bayesian
Changepoint
Detection.
https://github.com/hildensia/bayesian_
changepoint_detection.
[11] Pensieve. https://github.com/hongzimao/pensieve.
[12] DASH Industry Forum. https://dash.akamaized.net/envivio/EnvivioDash3.
[13] Sandvine: Global Internet phenomena report .
https://www.sandvine.com/
downloads/general/global-internet-phenomena/2014/2h-2014-global-internet-
phenomena-report.pdf.
[14] Ryan Prescott Adams and David JC MacKay.
Bayesian Online Changepoint
Detection. In arXiv:0710.3742v1, 2007.
[15] Saamer Akhshabi, Lakshmi Anantakrishnan, Ali C Begen, and Constantine
Dovrolis. What Happens when HTTP Adaptive Streaming Players Compete for
Bandwidth? In the International Workshop on Network and Operating System
Support for Digital Audio and Video, NOSSDAV, 2012.
[16] Athula Balachandran, Vyas Sekar, Aditya Akella, Srinivasan Seshan, Ion Stoica,
and Hui Zhang. Developing a Predictive Model of Quality of Experience for
Internet Video. In Proceedings of the ACM Conference on Special Interest Group
on Data Communication, SIGCOMM, 2013.
[17] Hari Balakrishnan, Mark Stemm, Srinivasan Seshan, and Randy H Katz. Ana-
lyzing Stability in Wide-area Network Performance. ACM SIGMETRICS Perfor-
mance Evaluation Review, 25:2–12, 1997.
[18] Daniel Barry and John A Hartigan. A Bayesian Analysis for Change Point Prob-
lems. Journal of the American Statistical Society, 88(421):309–319, 1993.
[19] Neal Cardwell, Yuchung Cheng, C. Stephen Gunn, Soheil Hassas Yeganeh, and
Van Jacobson. BBR: Congestion-Based Congestion Control. ACM Queue, 14:
20–53, 2016.
[20] Federico Chiariotti, Stefano D’Aronco, Laura Toni, and Pascal Frossard. Online
Learning Adaptation Strategy for DASH Clients. In Proceedings of the Interna-
tional Conference on Multimedia Systems, MMSys, 2016.
[21] Maxim Claeys, Steven Latré, Jeroen Famaey, Tingyao Wu, Werner Van Leek-
wijck, and Filip De Turck. Design and Optimisation of a (FA)Q-learning-based
HTTP Adaptive Streaming Client. Connection Science, 26(1):25–43, 2014.
[22] Frédéric Desobry, Manuel Davy, and Christian Doncarli.
An Online Kernel
Change Detection Algorithm. IEEE Transactions on Signal Processing, 53(8):
2961–2974, 2005.
[23] Florin Dobrian, Vyas Sekar, Asad Awan, Ion Stoica, Dilip Joseph, Aditya Gan-
jam, Jibin Zhan, and Hui Zhang. Understanding the Impact of Video Quality on
User Engagement. In Proceedings of the ACM Conference on Special Interest
Group on Data Communication, SIGCOMM, 2011.
[24] Paul Fernhead. Exact and Efficient Bayesian Inference for Multiple Changepoint
Problems. Statistics and Computing, 16(2):203–213, 2006.
[25] Tobias Flach, Pavlos Papageorge, Andreas Terzis, Luis Pedrosa, Yuchung Cheng,
Tayeb Karim, Ethan Katz-Bassett, and Ramesh Govindan.
An Internet-Wide
Analysis of Traffic Policing. In Proceedings of the ACM Conference on Special
Interest Group on Data Communication, SIGCOMM, 2016.
[26] Wayne A Fuller. Introduction to Statistical Time Series. John Wiley and Sons,
1976.
[27] Mojgan Ghasemi, Partha Kanuparthy, Ahmed Mansy, Theophilus Benson, and
Jennifer Rexford. Performance Characterization of a Commercial Video Stream-
ing Service. In Proceedings of the ACM Conference on Internet Measurement
Conference, IMC, 2016.
[28] Daniel Golovin, Benjamin Solnik, Subhodeep Moitra, Greg Kochanski, John
Karro, and D. Sculley. Google Vizier: A Service for Black-Box Optimization.
In Proceedings of the ACM International Conference on Knowledge Discovery
and Data Mining, SIGKDD, 2017.
[29] Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup,
and David Meger. Deep Reinforcement Learning that Matters. In Proceedings of
the Association for Advancement of Artificial Intelligence, AAAI, 2018.
[30] Rémi Houdaille and Stéphane Gouache. Shaping HTTP Adaptive Streams for a
Better User Experience. In Proceedings of the Multimedia Systems Conference,
MMSys, 2012.
[31] Te-Yuan Huang, Nikhil Handigol, Brandon Heller, Nick McKeown, and Ramesh
Johari. Confused, Timid, and Unstable: Picking a Video Streaming Rate is Hard.
In Proceedings of the ACM Conference on Internet Measurement Conference,
IMC, 2012.
[32] Te-Yuan Huang, Ramesh Johari, Nick McKeown, Matthew Trunnell, and Mark
Watson. A Buffer-based Approach to Rate Adaptation: Evidence from a Large
Video Streaming Service. In Proceedings of the ACM Conference on Special
Interest Group on Data Communication, SIGCOMM, 2014.
[33] Daniel R. Jeske, Veronica Montes De Oca, Wolfgang Bischoff, and Mazda Mar-
vasti. Cusum Techniques for Timeslot Sequences with Applications to Network
Surveillance. Computational Statistics and Data Analysis, 53:4332–4344, 2009.
[34] Junchen Jiang, Vyas Sekar, and Hui Zhang. Improving Fairness, Efficiency, and
Stability in HTTP-based Adaptive Video Streaming with FESTIVE. In Proceed-
ings of the ACM International Conference on Emerging Networking Experiments
and Technologies, CoNEXT, 2012.
[35] James Jobin, Michalis Faloutsos, Satish K Tripathi, and Srikanth V Krishna-
murthy. Understanding the Effects of Hotspots in Wireless Cellular Networks.
In Proceedings of the Conference of the IEEE Computer and Communications
Societies, INFOCOM, 2004.
[36] Eamonn J. Keogh, Selina Chu, David Hart, and Michael J. Pazzani. An Online
Algorithm for Segmenting Time Series. In Proceedings of the IEEE International
Conference on Data Mining, ICDM, 2001.
[37] S. Shunmuga Krishnan and Ramesh K. Sitaraman. Video Stream Quality Im-
pacts Viewer Behavior: Inferring Causality Using Quasi-experimental Designs.
In Proceedings of the ACM Conference on Internet Measurement Conference,
IMC, 2012.
[38] Dong Lu, Yi Qiao, Peter A Dinda, and Fabian E Bustamante. Characterizing and
Predicting TCP Throughput on the Wide Area Network. In IEEE International
Conference on Distributed Computing Systems, ICDCS, 2005.
[39] Hongzi Mao, Ravi Netravali, and Mohammad Alizadeh. Neural Adaptive Video
Streaming with Pensieve. In Proceedings of the ACM Conference on Special
Interest Group on Data Communication, SIGCOMM, 2017.
[40] Virginia Martín, Julián Cabrera, and Narciso García. Design, Optimization and
Evaluation of a Q-learning HTTP Adaptive Streaming Client. IEEE Transactions
on Consumer Electronics, 62(4):380–388, 2016.
[41] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Ve-
ness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidje-
land, Georg Ostrovski, et al. Human-level Control Through Deep Reinforcement
Learning. Nature, 518(7540):529–533, 2015.
[42] Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Tim-
othy Lillicrap, Tim Harley, David Silver, and Koray Kavukcuoglu. Asynchronous
Methods for Deep Reinforcement Learning. In Proceedings of the International
Conference on Machine Learning, ICML, 2016.
[43] Hossein Pishro-Nik.
Introduction to Probability, Statistics and Random Pro-
cesses. Kappa Research, 2014.
[44] Thanawin Rakthanmanon, Eamonn J. Keogh, Stefano Lonardi, and Scott Evans.
Time Series Epenthesis: Clustering Time Series Streams Requires Ignoring Some
Data. In Proceedings of the International Conference on Data Mining, ICML,
2011.
[45] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Why Should I Trust
You?: Explaining the Predictions of Any Classifier. In Proceedings of the ACM
International Conference on Knowledge Discovery and Data Mining, SIGKDD,
2016.
[46] Haakon Riiser, Paul Vigmostad, Carsten Griwodz, and Pål Halvorsen. Commute
Path Bandwidth Traces from 3G Networks: Analysis and Applications. In Pro-
ceedings of the ACM Multimedia Systems Conference, MMSys, 2013.
[47] Jeffrey Semke, Jamshid Mahdavi, and Matthew Mathis. Automatic TCP Buffer
Tuning. In Proceedings of the ACM Conference on Special Interest Group on
Data Communication, SIGCOMM, 1998.
[48] Kevin Spiteri, Rahul Urgaonkar, and Ramesh K Sitaraman. BOLA: Near-optimal
Bitrate Adaptation for Online Videos. In Proceedings of the IEEE International
Conference on Computer Communications, INFOCOM, 2016.
[49] Yi Sun, Xiaoqi Yin, Junchen Jiang, Vyas Sekar, Fuyuan Lin, Nanshu Wang, Tao
Liu, and Bruno Sinopoli. CS2P: Improving Video Bitrate Selection and Adapta-
tion with Data-Driven Throughput Prediction. In Proceedings of the ACM Con-
ference on Special Interest Group on Data Communication, SIGCOMM, 2016.
[50] Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction.
MIT press Cambridge, 1998.
[51] Guibin Tian and Yong Liu.
Towards Agile and Smooth Video Adaptation in
Dynamic HTTP Streaming. In the ACM International Conference on Emerging
Networking Experiments and Technologies, CoNEXT, 2012.
[52] Guillaume Urvoy-Keller. On the Stationarity of TCP Bulk Data Transfers. In
Proceedings of the Passive and Active Measurement Conference, PAM, 2005.
57
```


### Pagina 15
```text
Oboe
SIGCOMM ’18, August 20–25, 2018, Budapest, Hungary
[53] Jeroen van der Hooft, Stefano Petrangeli, Maxim Claeys, Jeroen Famaey, and
Filip De Turck. A Learning-based Algorithm for Improved Bandwidth-awareness
of Adaptive Streaming Clients. In Symposium on Integrated Network Manage-
ment, IM, 2015.
[54] Li Wei and Eamonn Keogh.
Semi-supervised Time Series Classification.
In
Proceedings of the ACM International Conference on Knowledge Discovery and
Data Mining, SIGKDD, 2006.
[55] Ronald J Williams and Jing Peng. Function Optimization using Connectionist
Reinforcement Learning Algorithms. Connection Science, 3(3):241–268, 1991.
[56] Keith Winstein and Hari Balakrishnan. TCP Ex Machina: Computer-generated
Congestion Control. In Proceedings of the ACM Conference on Special Interest
Group on Data Communication, SIGCOMM, 2013.
[57] Xuan Xiang and Kevin Murphy. Modelling Changing Dependency Structure in
Multivariate Time Series.
In Proceedings of the International Conference on
Data Mining, ICML, 2007.
[58] Kenji Yamanishi and Jun-ichi Takeuchi. A Unifying Framework for Detecting
Outliers and Change Points from Non-stationary Time Series Data. In Proceed-
ings of the ACM International Conference on Knowledge Discovery and Data
Mining, SIGKDD, 2002.
[59] Xiaoqi Yin, Abhishek Jindal, Vyas Sekar, and Bruno Sinopoli.
A Control-
Theoretic Approach for Dynamic Adaptive Video Streaming over HTTP.
In
Proceedings of the ACM Conference on Special Interest Group on Data Com-
munication, SIGCOMM, 2015.
[60] Yin Zhang and Nick Duffield. On the Constancy of Internet Path Properties. In
Proceedings of the ACM SIGCOMM Workshop on Internet Measurement, 2001.
58
```
