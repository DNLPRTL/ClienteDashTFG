1
SafeSABR: Risk-Calibrated Adaptive Bitrate
Streaming over Starlink Networks
Hongjun Xie, Jiahang Zhu, Zhiming Shao, Chao Fan, Zenghui Zhang, Genke Yang, and Pengcheng Luo
Abstract—Starlink, as a representative low Earth orbit (LEO)
satellite broadband system, makes high-bitrate video streaming
possible in regions where terrestrial broadband is unavailable.
However, its access links exhibit rapid throughput fluctuations
caused by satellite mobility and handovers. Existing learned
adaptive bitrate (ABR) algorithms can achieve high average
quality of experience (QoE), yet high-bitrate Starlink streaming
exposes severe session-level rebuffering that is not captured by
averageQoEalone.Toaddressit,thispaperproposesSafeSABR,
arisk-calibratedlearnedABRframeworkforStarlinknetworks.
SafeSABRformulatesStarlinkABRasaQoE–severe-risktrade-
offandfollowsathree-stagedesign:behavior-cloningpretraining
learns a high-QoE ABR prior, risk-calibrated reinforcement
learning (RL) fine-tuning reduces severe-tail action tendencies,
and a runtime safety auditor uses safe-capacity lower bounds to
checkpolicy-requestedbitratesbeforeexecution.Experimentson
real Starlink traces compare SafeSABR with online, prediction-
assisted, and learned ABR baselines. Compared with advanced
methods, SafeSABR reduces severe-stall sessions from 22.8% Fig. 1. Illustrative ABR-over-Starlink video delivery scenario. The video
to 7.2% and worst-5% session rebuffering from 54.30 s to server stores multiple encoded versions of the same content, such as 480p,
720p,1080p,4K,and8Krepresentations.Duringplayback,theABRplayer
22.68 s, with a 1.8% QoE cost. Component analyses further
observestheavailablebandwidthandplaybackbuffer,selectsthenextchunk
show that risk-calibrated fine-tuning and safe-capacity auditing
representation,andrequeststheselectedchunkovertheStarlinkaccesspath
reduce unsafe bitrate decisions and downstream severe-session
throughtheuserterminal,satellitenetwork,gateway,andInternet.
rebuffering. These results show that combining risk-calibrated
policy learning with decision-aware safe throughput forecasting
canmovelearnedABRtowardasaferQoE–severe-riskoperating
point under volatile Starlink networks. broadbandaccess.ComparedwithtraditionalsatelliteInternet,
Starlink-likelowEarthorbit(LEO)systemscanprovidehigher
Index Terms—Adaptive bitrate streaming, LEO satellite net-
works,behavior-cloningpretraining,reinforcementlearningfine- access capacity and lower latency, making high-bitrate video
tuning, risk-aware control streaming feasible in rural areas, oceans, airborne platforms,
disasterrecoveryscenarios,andotherregionswhereterrestrial
broadband is unavailable [1]–[3]. In such scenarios, a video
I. INTRODUCTION
service stores multiple encoded versions of the same content,
A. Background and Motivation and an ABR client continuously selects the representation of
ADAPTIVE bitrate (ABR) streaming is a representative thenextvideochunkaccordingtotheplaybackbufferandthe
bandwidth-demanding application enabled by Starlink expected future throughput. A higher-quality representation
improvesvideoqualitywhenthelinkremainsstrong,butitcan
This work was supported by the National Major Science and Technology quickly lead to rebuffering when the available capacity drops.
Project for Intelligent Manufacturing Systems and Robotics of China under Fig. 1 illustrates this ABR-over-Starlink delivery pipeline and
Grant2025ZD1602400.(Correspondingauthor:PengchengLuo.)
the client-side resolution/bitrate selection process.
Hongjun Xie, Chao Fan, Zenghui Zhang, Genke Yang and Pengcheng
Luo are with Ningbo Artificial Intelligence Institute, Shanghai Jiao Tong Starlink access throughput is highly dynamic [4], [5]. Mea-
University, Ningbo 315000, China, and also with the School of Automation
surement studies have shown that user-perceived throughput
and Intelligent Sensing, Shanghai Jiao Tong University, Shanghai 200240,
China, and the Key Laboratory of System Control and Information Pro- can fluctuate over short time scales due to satellite han-
cessing, Ministry of Education of China, Shanghai 200240, China (e-mail: dovers, elevation-angle changes, obstruction, gateway asso-
xiehongjun@sjtu.edu.cn,fchao2025@sjtu.edu.cn,zenghui.zhang@sjtu.edu.cn,
ciation, weather, and traffic load [6]. This volatility changes
gkyang@sjtu.edu.cn,luopeng69131@sjtu.edu.cn).
Hongjun Xie and Pengcheng Luo are also with Shanghai i-Space Orbital the nature of ABR control. In terrestrial broadband or cellular
ComputingInfrastructureTechnologyCo.,Ltd.,Shanghai200235,China. traces, a high recent throughput often provides a useful signal
Jiahang Zhu is with Ningbo Industrial Internet Institute, Ningbo 315000,
for selecting a higher bitrate [7], [8]. In high-bitrate Starlink
China(e-mail:zhujiahang2018@163.com).
Zhiming Shao is with the School of Automation and Intelligent Sens- streaming, however, the same history can become misleading:
ing, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: an ABR client may keep requesting a large chunk just before
zm.shao@sjtu.edu.cn).
the access link drops. The resulting problem is therefore not
The source code of SafeSABR is available at: https://github.com/
luopeng69131/SafeSABR. only how to increase average video quality, but also how
6202
yaM
72
]YS.ssee[
2v06532.5062:viXra

2
Fig.2. ChallengeofABRstreamingovervolatileStarlinkaccesslinks.Handover-inducedthroughputdropsandhistory-averagelagcanmakeanABRclient
maintain an aggressive bitrate after the actual link capacity has decreased. The selected bitrate then drains the playback buffer, creates multiple rebuffering
events,andaccumulatesmorethan10sofsession-levelstall.
to avoid session-level severe rebuffering caused by abrupt severe-tail risk rather than only maximizing mean QoE, and
throughput collapses, as illustrated in Fig. 2. This motivates the predictor must expose a safe-capacity estimate that can be
a Quality of Experience (QoE)–severe-risk view of Starlink checked against the actual bitrate action being requested.
ABR, where a method should be judged not only by mean Motivated by this observation, this paper proposes
QoE but also by the worst-session rebuffering tail and the SafeSABR, a risk-calibrated learned ABR framework for
fraction of sessions with unacceptable cumulative stalls. Starlink streaming with safe-capacity-audited runtime deci-
|                  |                |                |        |              |            |             |          | sions. Following |                 | the         | pretraining–fine-tuning |                       |             | framework   | of          |
| ---------------- | -------------- | -------------- | ------ | ------------ | ---------- | ----------- | -------- | ---------------- | --------------- | ----------- | ----------------------- | --------------------- | ----------- | ----------- | ----------- |
| Existing         | learning-based |                | ABR    | research     |            | mainly      | pursues  |                  |                 |             |                         |                       |             |             |             |
|                  |                |                |        |              |            |             |          | SABR [17],       | SafeSABR        |             | first                   | uses behavior-cloning |             |             | pretraining |
| higher QoE       | by             | improving      | policy | learning,    |            | adaptation, | and      |                  |                 |             |                         |                       |             |             |             |
|                  |                |                |        |              |            |             |          | to obtain        | a high-QoE      |             | ABR                     | prior                 | and then    | performs    | risk-       |
| generalization   |                | across network |        | conditions.  | Genet      | uses        | auto-    |                  |                 |             |                         |                       |             |             |             |
|                  |                |                |        |              |            |             |          | calibrated       | RL fine-tuning, |             | instantiated            |                       | by          | conditional | value-      |
| matic curriculum |                | generation     |        | to expose    | adaptation |             | policies |                  |                 |             |                         |                       |             |             |             |
|                  |                |                |        |              |            |             |          | at-risk proximal |                 | policy      | optimization            |                       | (CVaR-PPO), |             | to reduce   |
| to diverse       | network        | conditions     |        | [9]. Offline | RL         | and         | meta-RL  |                  |                 |             |                         |                       |             |             |             |
|                  |                |                |        |              |            |             |          | severe-tail      | action          | tendencies. |                         | At deployment         |             | time,       | a runtime   |
studiesfurtherimprovebitrateadaptationacrossheterogeneous
|            |                           |       |       |        |                   |     |         | safety auditor | uses    | a safe-capacity |     |        | estimate   | to check | and cor-    |
| ---------- | ------------------------- | ----- | ----- | ------ | ----------------- | --- | ------- | -------------- | ------- | --------------- | --- | ------ | ---------- | -------- | ----------- |
| traces and | tasks                     | [10], | [11], | while  | bitrate-guidance, |     | meta-   |                |         |                 |     |        |            |          |             |
|            |                           |       |       |        |                   |     |         | rect high-risk | bitrate | requests        |     | before | execution. | We       | instantiate |
| learning,  | and information-theoretic |       |       | neural | adaptation        |     | methods |                |         |                 |     |        |            |          |             |
improve cross-condition generalization [12]–[14]. Emerging the safe-capacity input with BG-CFQS [16], which forecasts
|                   |     |            |     |         |      |         |         | Starlink | throughput | lower | bounds | for | risk-aware |     | control. The |
| ----------------- | --- | ---------- | --- | ------- | ---- | ------- | ------- | -------- | ---------- | ----- | ------ | --- | ---------- | --- | ------------ |
| large-model-based |     | networking |     | studies | also | suggest | new op- |          |            |       |        |     |            |     |              |
designfollowsaQoE-orientedpretraining,risk-calibratedfine-
| portunities | for | context-aware |     | control | and | network | adapta- |         |                    |     |            |     |           |     |     |
| ----------- | --- | ------------- | --- | ------- | --- | ------- | ------- | ------- | ------------------ | --- | ---------- | --- | --------- | --- | --- |
|             |     |               |     |         |     |         |         | tuning, | and safety-audited |     | deployment |     | pipeline. |     |     |
tion[15].Thesemethodsshowthepotentialoflearnedcontrol
| for improving                                         |     | ABR performance, |     | but | their | optimization | and |                  |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | ---------------- | --- | --- | ----- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| evaluationarestilllargelydrivenbyhighQoEoraverageper- |     |                  |     |     |       |              |     | B. Contributions |     |     |     |     |     |     |     |
formance. In highly volatile Starlink access links, handover- The main contributions of this paper are summarized as
inducedthroughputdropscanmakealearnedABRpolicykeep
follows:
requestingaggressivehigh-bitratechunks,andasmallnumber
• Weformulatehigh-bitrateStarlinkABRasaQoE–severe-
| of such | decisions | may drain | the | playback | buffer | and | produce |     |     |     |     |     |     |     |     |
| ------- | --------- | --------- | --- | -------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
risktradeoffproblemratherthananaverage-QoEranking
| severe session-level |           | stalls. | The         | remaining |                   | gap is | therefore |          |            |             |     |          |      |           |              |
| -------------------- | --------- | ------- | ----------- | --------- | ----------------- | ------ | --------- | -------- | ---------- | ----------- | --- | -------- | ---- | --------- | ------------ |
|                      |           |         |             |           |                   |        |           | problem. | In         | addition    | to  | average  | QoE, | we        | use session- |
| not simply           | better    | ABR     | adaptation, | but       | a risk-calibrated |        | ABR       |          |            |             |     |          |      |           |              |
|                      |           |         |             |           |                   |        |           | level    | cumulative | rebuffering |     | metrics, |      | including | worst-5%     |
| design that          | preserves | high    | QoE         | while     | explicitly        |        | reducing  |          |            |             |     |          |      |           |              |
sessionrebufferingandthefractionofsessionswithmore
severe-stall risk caused by abrupt Starlink throughput drops. than 10s rebuffering, to expose severe playback failures
Reducing this severe-stall risk requires connecting through- hidden by mean performance.
put prediction with the bitrate action that will be executed. A We develop risk-calibrated policy learning in SafeSABR
•
throughputoverestimationmaybeharmlesswhentheplayback byextendingtheSABRpretraining–fine-tuningparadigm
buffer is large or the selected chunk is small, but the same from average-QoE learning to severe-risk-aware ABR
overestimation can trigger rebuffering when the buffer is low control. Behavior cloning provides a high-QoE ABR
and the requested chunk is large. Therefore, evaluating a prior, while risk-calibrated RL fine-tuning, instantiated
predictor only by point-estimation accuracy is insufficient for by CVaR-PPO, reshapes the learned policy toward lower
StarlinkABR[16].Thepolicymustbecalibratedtowardlower severe-tail risk.

3
Fig.3. OverviewofSafeSABR.SafeSABRaddressesthehigh-bitrateStarlinkABRproblembylearningahigh-QoEpriorthroughbehavior-cloningpretraining,
applyingrisk-calibratedRLfine-tuningwithCVaR-PPO,andauditingunsafebitraterequestswithBG-CFQSsafe-capacityforecastingatruntime.
• Wedesignadecision-awareruntimesafetyauditordriven II. RELATEDWORK
bysafethroughputforecasting.TheauditorconvertsBG- Therelatedliteratureisorganizedalongthreelines.Wefirst
| CFQS safe-capacity |                | lower      | bounds                | into      | ABR             | action-level |                    |      |             |          |             |           |             |           |
| ------------------ | -------------- | ---------- | --------------------- | --------- | --------------- | ------------ | ------------------ | ---- | ----------- | -------- | ----------- | --------- | ----------- | --------- |
|                    |                |            |                       |           |                 |              | review Starlink    |      | measurement |          | and video   | streaming |             | over LEO, |
| feasibility        | checks,        | and        | the predictor-auditor |           |                 | interface    | is                 |      |             |          |             |           |             |           |
|                    |                |            |                       |           |                 |              | which characterize |      | the         | access   | environment |           | considered  | in this   |
| evaluated          | by decision    | violation, |                       | high-risk | overestimation, |              |                    |      |             |          |             |           |             |           |
|                    |                |            |                       |           |                 |              | paper. We          | then | discuss     | Starlink | throughput  |           | prediction, | which     |
| audit rate,        | and downstream |            | severe-session        |           | rebuffering.    |              |                    |      |             |          |             |           |             |           |
iscloselyrelatedtobitratedecisionmakingovervolatilelinks.
| We conduct     | a comprehensive |           |              | evaluation | on          | real-world  |                                                        |             |                |     |          |             |           |        |
| -------------- | --------------- | --------- | ------------ | ---------- | ----------- | ----------- | ------------------------------------------------------ | ----------- | -------------- | --- | -------- | ----------- | --------- | ------ |
| •              |                 |           |              |            |             |             | Finally,wereviewABRalgorithms,includingclassicalonline |             |                |     |          |             |           |        |
| Starlink       | throughput      | traces,   | including    |            | comparisons | with        |                                                        |             |                |     |          |             |           |        |
|                |                 |           |              |            |             |             | methods                                                | and recent  | learning-based |     |          | approaches. |           |        |
| representative | ABR             | baselines | and          | analyses   | of          | robustness, |                                                        |             |                |     |          |             |           |        |
| components,    | and             | runtime   | mechanisms.  |            | The results | show        |                                                        |             |                |     |          |             |           |        |
|                |                 |           |              |            |             |             | A. Starlink                                            | Measurement |                | and | Video    | Streaming   | over      | LEO    |
| that SafeSABR  |                 | reduces   | severe-stall | sessions   |             | from 22.8%  |                                                        |             |                |     |          |             |           |        |
| to 7.2%        | with a          | 1.8%      | QoE cost,    | and        | achieves    | a more      |                                                        |             |                |     |          |             |           |        |
|                |                 |           |              |            |             |             | The rapid                                              | deployment  |                | of  | Starlink | has         | motivated | exten- |
favorable QoE–severe-risk operating point among high- sive measurement studies on LEO satellite broadband. Early
QoE methods. active and browser-side measurements characterized Starlink
throughput,latency,andpacketloss,showingthatcommercial
|     |     |     |     |     |     |     | LEO access | can | provide | broadband-level |     |     | capacity | but with |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --------------- | --- | --- | -------- | -------- |
C. Organization
|     |     |     |     |     |     |     | noticeable | temporal | variability |     | [1], | [2]. End-user |     | and multi- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ----------- | --- | ---- | ------------- | --- | ---------- |
Theremainderofthispaperisorganizedasfollows.Section terminalstudiesfurtherreportedthatperformancevariesacross
II reviews related work on LEO satellite measurement and location, time, terminal status, and application workload [18],
video streaming, Starlink throughput prediction, and ABR [19].TheseresultsestablishStarlinkasaviableaccessnetwork
algorithms. Section III formulates the high-bitrate Starlink forhigh-bitrateapplications,butalsoindicatethatitsdynamics
ABR problem, including the chunk-level decision model, differ from conventional terrestrial broadband.
QoE–severe-risk metrics, and safe-capacity action feasibility. Several studies have further examined the causes and ap-
Section IV presents the SafeSABR framework, including plication impact of such dynamics. Multi-timescale through-
behavior-cloning pretraining, risk-calibrated RL fine-tuning, put measurements reported both short-term fluctuations and
decision-aware safe-capacity prediction, and runtime safety longer-term load patterns [4]. Other works analyzed the role
auditing. Section V describes the experimental setting and of scheduling, obstruction, satellite visibility, handovers, and
evaluates SafeSABR through main comparisons, robustness bent-pipe routing in shaping user-perceived performance [6],
tests,mechanismanalysis,predictor-auditoranalysis,ablation, [7], [20]. For video applications, prior studies have evaluated
and sensitivity studies. Section VI concludes the paper. real-time multimedia services, Dynamic Adaptive Streaming

4
overHTTP(DASH)streaming,andlarge-scalevideobehavior
TABLEI
MAINNOTATIONUSEDINTHEFORMULATIONANDDESIGN.
overStarlink[21]–[23].TheseworksmotivateABRoverLEO
| networks, | but | they mainly | characterize |     | network |     | or application |     |     |     |     |     |     |     |
| --------- | --- | ----------- | ------------ | --- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
behavior.TheydonotdefineaQoE–severe-riskABRobjective Symbol Meaning
|              |     |        |      |            |          |     |               | 𝑡,𝑇,Δ |     | Chunk | index, number | of  | chunks in | a session, and |
| ------------ | --- | ------ | ---- | ---------- | -------- | --- | ------------- | ----- | --- | ----- | ------------- | --- | --------- | -------------- |
| or a learned | ABR | design | that | explicitly | controls |     | session-level |       |     |       |               |     |           |                |
chunkduration.
| rebuffering | tails | under | Starlink | throughput |     | drops. |     |      |     |                                          |     |     |     |     |
| ----------- | ----- | ----- | -------- | ---------- | --- | ------ | --- | ---- | --- | ---------------------------------------- | --- | --- | --- | --- |
|             |       |       |          |            |     |        |     | 𝑠 𝑡, | ℎ 𝑡 | ABRpolicystateandpredictorinputatchunk𝑡. |     |     |     |     |
𝑏 𝐵
|     |     |     |     |     |     |     |     | 𝑡,  | max | Playbackbufferandmaximumbuffersize. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
A, 𝑎
|     |     |     |     |     |     |     |     |     | 𝑡   | Orderedbitrate-actionsetandselectedaction. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
B. Starlink Throughput Prediction 𝑎 min, C𝑡 Lowest bitrate action and feasible candidate set no
higherthantherawrequest.
| Throughput |        | prediction | is  | a natural |          | tool for   | ABR over |         |      |                                |     |     |     |     |
| ---------- | ------ | ---------- | --- | --------- | -------- | ---------- | -------- | ------- | ---- | ------------------------------ | --- | --- | --- | --- |
|            |        |            |     |           |          |            |          | 𝑟(𝑎),𝑆  | 𝑡(𝑎) | Bitrateandchunksizeunderaction |     |     |     | 𝑎.  |
| dynamic    | access | links.     | For | mobile    | adaptive | streaming, | Lu-      | 𝑐 𝑡,𝑐ˆ𝑡 |      |                                |     |     |     |     |
Realizedthroughputandpredictedsafecapacity.
mos shows that decision-tree throughput prediction can be 𝑑 𝑡(𝑎),𝜌 𝑎.
|               |      |        |            |         |         |             |             |        | 𝑡   | Downloadtimeandrebufferingunderaction           |     |     |     |     |
| ------------- | ---- | ------ | ---------- | ------- | ------- | ----------- | ----------- | ------ | --- | ----------------------------------------------- | --- | --- | --- | --- |
|               |      |        |            |         |         |             |             | 𝜇, 𝜂   |     | Rebufferingandbitrate-smoothnesspenaltyweights. |     |     |     |     |
| integrated    | with | ABR    | control    | to      | improve | QoE         | [24], [25]. |        |     |                                                 |     |     |     |     |
|               |      |        |            |         |         |             |             | 𝑞 𝑡,𝑄, | 𝑅   | Per-chunkQoE,session-levelQoE,andsession-level  |     |     |     |     |
| For Starlink, |      | recent | predictors | exploit |         | information | beyond      |        |     |                                                 |     |     |     |     |
rebuffering.
𝜏, 𝜋
a short history of measured throughput. T3P uses terminal StreamingsessionandABRpolicy.
|                       |     |             |     |     |         |     |            | J𝑄, | R𝛽, S𝜌 | ExpectedQoE,tail-rebufferingrisk,andsevere-stall |     |     |     |     |
| --------------------- | --- | ----------- | --- | --- | ------- | --- | ---------- | --- | ------ | ------------------------------------------------ | --- | --- | --- | --- |
| and satellite-context |     | information |     | to  | improve | LEO | throughput |     |        | 0                                                |     |     |     |     |
probability.
| prediction | [7]. | StarNet | further | incorporates |     | satellite-domain |     |     |       |                                                    |     |     |     |     |
| ---------- | ---- | ------- | ------- | ------------ | --- | ---------------- | --- | --- | ----- | -------------------------------------------------- | --- | --- | --- | --- |
|            |      |         |         |              |     |                  |     | 𝛽,𝜌 | 0,VaR | Tail-riskconfidencelevel,severe-stallthreshold,and |     |     |     |     |
knowledge and handover-aware temporal patterns for Starlink value-at-risk.
𝑔,
throughput modeling [6]. Fine-grained burst characterization F𝑡 Bufferguardmarginandpredictedfeasibleactionset.
|     |     |     |     |     |     |     |     | 𝛼,  | 𝜉 𝛼,𝜆 | CVaRconfidencelevel,empiricaltailthreshold,and |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------------------------------------- | --- | --- | --- | --- |
has also been used to model and predict Starlink throughput riskpenaltyweight.
variations [26]. BG-CFQS further studies risk-aware safe D IL, 𝑎 𝐸, 𝑦 𝑡(𝑎) Imitation dataset, expert action label, and one-hot
𝑡
throughput forecasting for Starlink networks and provides expertlabel.
𝑅
|            |             |     |          |           |     |                      |     | L IL, | B, 𝑖 | Imitation | loss, | rollout batch, | and | episode-level re- |
| ---------- | ----------- | --- | -------- | --------- | --- | -------------------- | --- | ----- | ---- | --------- | ----- | -------------- | --- | ----------------- |
| calibrated | lower-bound |     | capacity | estimates |     | for safety-sensitive |     |       |      |           |       |                |     |                   |
bufferinginabatch.
control [16]. These studies show that throughput can be 𝑎 raw, 𝑎 safe Rawpolicyactionandauditedaction.
𝑡 𝑡
|           |      |             |      |                  |     |     |           | 𝑣 𝑡(𝑎),𝑚 |     | Decision-violation |     | indicator | and audit-intervention |     |
| --------- | ---- | ----------- | ---- | ---------------- | --- | --- | --------- | -------- | --- | ------------------ | --- | --------- | ---------------------- | --- |
| predicted | more | effectively | when | network-specific |     |     | structure | is       | 𝑡   |                    |     |           |                        |     |
indicator.
considered.
|            |     |            |           |     |          |        |            | 𝜋 𝜃, | 𝜋 𝐸, 𝜙,Φ | Learnedpolicy,expertpolicy,safe-capacitypredictor, |     |     |     |     |
| ---------- | --- | ---------- | --------- | --- | -------- | ------ | ---------- | ---- | -------- | -------------------------------------------------- | --- | --- | --- | --- |
| Throughput |     | prediction | accuracy, |     | however, | is not | equivalent |      |          |                                                    |     |     |     |     |
andpredictorcandidateset.
| to ABR    | decision | safety.    | A   | point predictor     |     | with     | low average |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | --- | ------------------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| error may | still    | be harmful |     | if it overestimates |     | capacity | when        |     |     |     |     |     |     |     |
theplaybackbufferisloworwhentheselectedchunkislarge.
|     |     |     |     |     |     |     |     | satellite | access | links. Rebuffering |     | is usually |     | included in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------------------ | --- | ---------- | --- | --------------- |
Conversely,aconservativeestimatemayreducerebufferingbut QoE reward, yet expected-QoE optimization can still average
unnecessarily sacrifice video quality. The relevant question is out rare but long stalls. General risk-aware optimization and
notonlywhetherapredictorisaccurate,butwhetheritsoutput safe RL offer tools for tail-risk learning and runtime action
can be used by an ABR controller to reduce unsafe bitrate filtering [31]–[34], but Starlink ABR safety must be tied to
| decisions   | and        | severe-session |         | rebuffering |            | tails. |               |           |           |                    |            |              |            |               |
| ----------- | ---------- | -------------- | ------- | ----------- | ---------- | ------ | ------------- | --------- | --------- | ------------------ | ---------- | ------------ | ---------- | ------------- |
|             |            |                |         |             |            |        |               | chunk     | size,     | requested bitrate, |            | playback     | buffer,    | and predicted |
|             |            |                |         |             |            |        |               | safe      | capacity. | Therefore,         | this paper | focuses      | on         | a complemen-  |
|             |            |                |         |             |            |        |               | tary      | problem:  | how to preserve    |            | the high-QoE | behavior   | learned       |
| C. Adaptive | Bitrate    | Streaming      |         |             |            |        |               |           |           |                    |            |              |            |               |
|             |            |                |         |             |            |        |               | by modern |           | ABR methods        | while      | explicitly   | reducing   | session-      |
| ABR         | algorithms | select         | the     | bitrate     | of each    | video  | chunk         | to        |           |                    |            |              |            |               |
|             |            |                |         |             |            |        |               | level     | severe    | rebuffering        | under      | Starlink     | throughput | volatility.   |
| balance     | video      | quality,       | bitrate | smoothness, |            | and    | rebuffering.  |           |           |                    |            |              |            |               |
| Classical   | online     | methods        | rely    | on          | throughput |        | prediction or |           |           |                    |            |              |            |               |
buffer occupancy, such as Model Predictive Control (MPC)- III. STARLINKABRMODELANDQOE–SEVERE-RISK
based planning and BOLA-style buffer control [27], [28]. OBJECTIVE
Learning-based ABR methods instead train bitrate policies Thissectionformalizesthetwodecisionlinksusedthrough-
| from QoE | feedback. |     | Beyond | early | neural | and | imitation- |         |        |                  |        |            |     |             |
| -------- | --------- | --- | ------ | ----- | ------ | --- | ---------- | ------- | ------ | ---------------- | ------ | ---------- | --- | ----------- |
|          |           |     |        |       |        |     |            | out the | paper. | First, a bitrate | action | determines |     | chunk down- |
learning methods such as Pensieve and Comyco [29], [30], load time, buffer evolution, and rebuffering, which motivates
recent studies have focused on making learned ABR poli- a QoE–severe-risk objective at the session level. Second,
| cies adapt | better | across | diverse |     | network | conditions. | Genet |             |     |               |            |     |         |             |
| ---------- | ------ | ------ | ------- | --- | ------- | ----------- | ----- | ----------- | --- | ------------- | ---------- | --- | ------- | ----------- |
|            |        |        |         |     |         |             |       | a predicted |     | safe capacity | determines |     | whether | a requested |
uses automatic curriculum generation for learning adaptation bitrateisfeasiblebeforeexecution,whichconnectsthroughput
| policies | [9]. Offline | RL  | and | meta-RL | further | improve | bitrate |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | ------- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
forecastingtoABRactionsafety.Foreaseofreading,themain
| decisions | across | heterogeneous |     | traces | and | tasks | [10], [11], |          |     |            |          |     |     |     |
| --------- | ------ | ------------- | --- | ------ | --- | ----- | ----------- | -------- | --- | ---------- | -------- | --- | --- | --- |
|           |        |               |     |        |     |       |             | notation | is  | summarized | in Table | I.  |     |     |
whilebitrateguidance,MetaABR,andMerina+improvecross-
conditiongeneralizationthroughmeta-learningorinformation-
|           |        |            |            |     |                   |     |      | A. Chunk-Level |     | ABR Decision |     |     |     |     |
| --------- | ------ | ---------- | ---------- | --- | ----------------- | --- | ---- | -------------- | --- | ------------ | --- | --- | --- | --- |
| theoretic | neural | adaptation | [12]–[14]. |     | Large-model-based |     | net- |                |     |              |     |     |     |     |
workingsystemssuchasNetLLMalsoindicateabroadertrend We characterize the chunk-level relationship among bitrate
toward context-aware network control [15]. selection, download time, buffer evolution, and rebuffering.
These studies demonstrate the promise of learned ABR for We consider video streaming over a Starlink access link. A
improving QoE and adaptation performance, but they do not videoisdividedintochunksindexedby𝑡,andeachchunkhas
𝑡,
fully address the severe-stall risk created by highly volatile duration Δ. Before downloading chunk the ABR controller

5
observesastate 𝑠 𝑡 thatincludestheplaybackbuffer 𝑏 𝑡,recent Maximizing this expectation alone can hide rare but severe
throughput observations, previous bitrate, remaining chunks, session-level stalls. We therefore define a tail-rebuffering risk
and chunk-size information [17], [29]. The controller selects at confidence level 𝛽:
a A b i i s tra o t r e de a r c e t d io f n ro 𝑎 m 𝑡 ∈ the A lo f w ro e m st a to d t i h s e cr h et i e gh b e i s t t ra b te itr l a a t d e d a e n r, d w 𝑟 h (𝑎 er 𝑡 e ) R𝛽(𝜋) =E 𝜏∼𝜋 (cid:2)𝑅(𝜏) | 𝑅(𝜏) ≥VaR𝛽(𝑅) (cid:3), (7)
denotes the corresponding bitrate.
Let 𝑆 𝑡(𝑎 𝑡) denote the size of chunk 𝑡 under action 𝑎 𝑡, and
whereVaR𝛽(𝑅) isthe 𝛽-quantileofthesession-levelrebuffer-
ingrandomvariable.Wealsodefinetheprobabilityofasevere-
let𝑐 𝑡 denotetherealizedStarlinkthroughputduringthechunk stall session under a stall threshold 𝜌 :
download. The download time is 0
𝑑 𝑡(𝑎 𝑡) = 8𝑆 𝑡
𝑐
(𝑎 𝑡) . (1) S𝜌 0 (𝜋) = 𝜏 P ∼ r 𝜋 (𝑅(𝜏) > 𝜌 0 ). (8)
𝑡
TheQoE–severe-riskviewinthispaperisthereforetopreserve
The factor 8 converts chunk size from bytes to bits. Thus, alargeJ𝑄(𝜋)whilereducingR𝛽(𝜋)andS𝜌 (𝜋).Theconcrete
a larger selected representation 𝑆 𝑡(𝑎 𝑡) or a lower Starlink
finite-test estimators used in the experime
0
nts are given in
throughput 𝑐 𝑡 directly increases the download time and con- Section V. For training-time risk shaping, we use CVaR as
sumes more playback buffer. Rebuffering occurs when the the tail-risk measure. Let 𝑋 denote a rebuffering loss random
download time exceeds the available playback buffer: variable induced by a policy. The CVaR at confidence level 𝛼
𝜌 𝑡 =max(𝑑 𝑡(𝑎 𝑡)−𝑏 𝑡 ,0). (2) is
CVaR𝛼(𝑋) =E[𝑋 | 𝑋 ≥VaR𝛼(𝑋)], (9)
If 𝑑 𝑡(𝑎 𝑡) ≤ 𝑏 𝑡, the chunk is downloaded before the current
buffer is exhausted and 𝜌 𝑡 = 0. Otherwise, the excess down- HereVaR𝛼(𝑋) isthe𝛼-quantileof 𝑋,andCVaRaveragesthe
load time 𝑑 𝑡(𝑎 𝑡) − 𝑏 𝑡 is counted as rebuffering. After the losses no smaller than this quantile.
download, the buffer is updated as
𝑏 𝑡+1 =min{𝐵 max ,max(𝑏 𝑡 −𝑑 𝑡(𝑎 𝑡),0)+Δ}, (3) C. Safe-Capacity Action Feasibility
The inner maximum describes the remaining buffer after We define a predicted feasible-action set that connects the
downloading. The newly downloaded chunk then adds Δ safe-capacity estimate, the current playback buffer, and the
seconds of playable video, and the outer minimum enforces bitrate-action feasibility before execution.
the maximum buffer size 𝐵 . Let 𝑐ˆ𝑡 be a predicted safe-capacity lower bound exposed
max
to the ABR controller for the next chunk download. Given a
buffer guard margin 𝑔, an action is predicted to be feasible
B. QoE and Severe-Risk Metrics
if its estimated download time does not exceed the guarded
We evaluate an ABR policy at the session level by measur- buffer:
i T n h g is bo se th ss i i t o s n a -l c e c v u e m l u v l i a e t w ed c Q ap o t E ure a s nd th i e ts i s m ev p e a r c e t r o e f bu ra ff r e e ri S n t g ar r l i i s n k k . F𝑡(𝑐ˆ𝑡) = (cid:26) 𝑎 ∈ A | 8𝑆 𝑐 𝑡 ˆ ( 𝑡 𝑎) ≤ 𝑏 𝑡 −𝑔 (cid:27) . (10)
throughput drops that may dominate user experience even
The set F𝑡(𝑐ˆ𝑡) is the predicted safe action set. It keeps only
when the expected QoE remains high.
those bitrates whose estimated download time under 𝑐ˆ𝑡 fits
Following common ABR formulations, the per-chunk QoE
within the guarded buffer 𝑏 𝑡 − 𝑔. If 𝑏 𝑡 ≤ 𝑔, the guard
reward is
leaves no positive safe download budget, and the auditor
𝑞 𝑡 = 𝑟(𝑎 𝑡) −𝜇𝜌 𝑡 −𝜂 |𝑟(𝑎 𝑡)−𝑟(𝑎 𝑡−1 )| , (4) falls back to the lowest bitrate action. This feasibility set
1000 1000 connects throughput prediction to ABR control: a capacity
Thefirsttermrewardsvideoquality,withthedivisionby1000 overestimate can incorrectly include an aggressive bitrate in
used to place the bitrate reward on the usual Mbps scale. The F𝑡(𝑐ˆ𝑡), especially when the chunk is large or the buffer is
second term penalizes stall duration with weight 𝜇, and the low.
thirdtermpenalizesbitrateswitchingwithweight𝜂.Therefore, For analysis, we define a decision violation using the
a high-bitrate action is beneficial only when it does not create realized capacity:
excessive rebuffering or quality oscillation. For one streaming
sessionwith𝑇 chunks,wedenotethesession-levelQoEreward 𝑣 𝑡(𝑎) =1
(cid:26) 8𝑆
𝑐
𝑡(𝑎)
> 𝑏 𝑡 −𝑔
(cid:27)
. (11)
𝑄 and cumulative rebuffering 𝑅 by 𝑡
𝑇 𝑇 Here, 1{·} denotes an indicator that returns one when the
∑︁ ∑︁
𝑄 = 𝑞 𝑡 , 𝑅 = 𝜌 𝑡 . (5) condition inside the braces is true and zero otherwise. Thus,
𝑡=1 𝑡=1 𝑣 𝑡(𝑎) = 1 means that the actual download time of action 𝑎
Let 𝜏 denote a random streaming session generated by a exceeds the guarded buffer, while 𝑣 𝑡(𝑎) = 0 means that the
policy 𝜋 under the Starlink throughput process. The expected actionsatisfiestheguarded-bufferconstraintundertherealized
Starlink throughput. This metric is an ex-post safety check:
QoE objective is
it reveals whether an action that may appear feasible under
J𝑄(𝜋) =E 𝜏∼𝜋[𝑄(𝜏)]. (6) prediction would actually be unsafe after execution.

6
Fig. 4. Framework of SafeSABR. The offline part constructs a high-QoE prior through behavior-cloning pretraining, applies risk-calibrated RL fine-tuning
withCVaR-PPO,andcalibratesadecision-awaresafe-capacitypredictor 𝜙 withBG-CFQS,whiletheonlinepartuses 𝜙 toauditthepolicy-requestedaction
beforeexecution.
IV. SAFESABRDESIGN policy avoids random high-bitrate exploration and provides a
useful ABR prior for the subsequent CVaR-PPO update.
SafeSABRimplementstwocomplementaryrisk-controllay-
ers around a learned ABR policy. The training-time layer
Let 𝜋 𝜃(𝑎|𝑠) denote the probability that the learned policy
constructs a policy that starts from a high-QoE behavior- with parameter 𝜃 selects action 𝑎 in state 𝑠, and let 𝜋 𝐸 denote
the expert policy. In our implementation, behavior-cloning
cloning prior and is then calibrated through risk-calibrated
pretraining uses DAgger-style data aggregation [35]: states
RL fine-tuning, instantiated by CVaR-PPO. The deployment-
visited by the current policy are aggregated into an imitation
timelayerusesaBG-CFQSsafe-capacityestimatetoauditthe
dataset D , and the expert provides the corresponding action
policy-requested bitrate before execution. IL
label 𝑎
𝑡
𝐸 =𝜋 𝐸(𝑠 𝑡).
The pretrained policy is obtained by minimizing the cate-
A. Framework Structure
gorical cross-entropy imitation loss
SafeSABR integrates risk-calibrated policy learning and
1 ∑︁ ∑︁
decision-aware runtime auditing through the offline-to-online L
IL
(𝜃) =−
|D |
𝑦 𝑡(𝑎)log𝜋 𝜃(𝑎|𝑠 𝑡), (12)
p
ar
i
t
p
i
e
fa
li
c
n
t
e
s:
s
a
h
n
o
A
w
B
n
R
in
po
F
li
i
c
g
y
.
𝜋
4
𝜃
.
a
T
n
h
d
e
a
o
s
f
a
fl
f
i
e
n
-
e
cap
p
a
a
c
rt
ity
pr
p
o
r
d
e
u
d
c
ic
e
t
s
or
tw
𝜙.
o IL (𝑠𝑡,𝑎
𝑡
𝐸)∈DIL 𝑎∈A
Here, D denotes the aggregated imitation dataset, whose
The policy-training path uses Starlink traces and expert IL
labels to learn high-QoE bitrate behavior through behavior- elements are state-expert-action pairs (𝑠 𝑡 ,𝑎 𝑡 𝐸), and |D IL | is
cloning pretraining. It then performs risk-calibrated RL fine-
the number of such pairs. The term 𝑦 𝑡(𝑎) =1{𝑎 =𝑎
𝑡
𝐸} is the
one-hot expert label over the bitrate ladder A. With this one-
tuning with CVaR-PPO, which penalizes severe rebuffering
hot label, the cross-entropy loss is equivalent to the negative
episodes and moves the policy toward a lower-risk action dis-
log-probability assigned to the expert action. Minimizing L
tributionwhileretainingthebitrate-selectioncapabilitylearned IL
therefore makes the learned policy imitate the expert on the
from the expert. In parallel, the safe-capacity calibration path
states collected in D .
uses Starlink traces to calibrate BG-CFQS and outputs a IL
predictor 𝜙 that provides the safe capacity used by the online Algorithm 1 summarizes the behavior-cloning pretraining
procedure. Following Comyco-style imitation learning [30],
auditor.
[36], the reference expert is implemented as a beam-
DuringonlineABRdecisionmaking,thecurrentABRstate
is sent to the policy to obtain a raw bitrate request 𝑎raw, while search/MPC policy that uses future throughput over a finite
𝑡
the recent history ℎ 𝑡 is sent to the predictor to obtain 𝑐ˆ𝑡. horizon to generate high-QoE action labels for pretraining.
The safety auditor combines these two outputs at the action
level: it keeps the raw request if it satisfies the feasible-action C. Risk-Calibrated RL Fine-Tuning
condition in (10), and otherwise downgrades it to the highest
Behavior cloning learns a high-QoE initial policy, but
feasiblelowerbitrate.Theexecutedactionthendeterminesthe
it does not explicitly control the severe-session rebuffering
download time, QoE, buffer update, and next ABR state.
tail. SafeSABR therefore performs risk-calibrated RL fine-
tuning, instantiated by combining proximal policy optimiza-
B. Behavior-Cloning Pretraining
tion (PPO) [37] with a CVaR tail-risk penalty [31]–[33].
SafeSABR first uses behavior cloning to learn a high-QoE We refer to this instantiation as CVaR-PPO, so that severe
initial policy from a reference ABR expert. This pretrained rebufferingepisodesinfluencethepolicyupdatemoredirectly.

7
Algorithm 1 Behavior-Cloning Pretraining Algorithm 3 Decision-Aware Safe-Capacity Predictor Con-
1: Input:initialpolicy 𝜋 𝜃,expertpolicy 𝜋 𝐸,ABRsimulator struction
2: Input: pretraining iterations 𝑁 pre , rollout steps 𝑇 pre , 1: Input: Starlink trace history, predictor candidates Φ, cal-
epochs 𝐸 ibration traces
pre
3: Initialize imitation dataset D IL ←∅. 2: Input: ABR decision samples and feasibility rule in (10)
4: for 𝑛=1,...,𝑁 pre do 3: for each candidate predictor 𝜙 𝑗 ∈Φ do
5: Roll out 𝜋 𝜃 in the simulator for 𝑇 pre steps and collect 4: Train or calibrate 𝜙 𝑗 on Starlink history.
visited states. 5: Generate safe-capacity estimates 𝑐ˆ 𝑡 (𝑗) = 𝜙 𝑗(ℎ 𝑡) on
6: Query𝜋 𝐸 forexpertactionlabelsonthecollectedstates. calibration traces.
7: Aggregate the labeled pairs into D IL . 6: Build feasible sets F𝑡(𝑐ˆ 𝑡 (𝑗)) according to (10).
8: for 𝑒 =1,...,𝐸 pre do 7: Evaluate decision violations for admitted actions ac-
9: Update 𝜃 by minimizing L IL (𝜃) in (12). cording to (11).
10: end for 8: Evaluate downstream ABR rebuffer risk under this
11: end for predictor.
12: Output: pretrained high-QoE ABR policy 𝜋 𝜃 9: end for
10: Select the predictor 𝜙 according to the desired QoE–
severe-risk operating point.
Algorithm 2 Risk-Calibrated RL Fine-Tuning with CVaR-
11: Output: safe-capacity predictor 𝜙
PPO
1: Input: pretrained policy 𝜋 𝜃, ABR simulator, risk level 𝛼,
weight 𝜆
2: Input: fine-tuning iterations 𝑁 RL , rollout episodes per D. Decision-Aware Safe-Capacity Predictor Interface
batch 𝑀
RL Risk-calibrated RL fine-tuning reduces unsafe action ten-
3: for 𝑛=1,...,𝑁 RL do dencies, but online auditing still requires a capacity value for
4: Roll out 𝜋 𝜃 for 𝑀 RL trace episodes. thenextchunk.SafeSABRusesadecision-awaresafe-capacity
5: C
in
o
g
m
{
p
𝑅
u
𝑖
t
}
e
.
per-chunk rewards {𝑞 𝑡} and episode rebuffer- predictor interface: the predictor exposes one scalar 𝑐ˆ𝑡 that
is consumed by the feasibility set in (10), rather than being
6: Estimate C(cid:155)VaR𝛼(𝑅) by (13).
evaluated only as a standalone throughput forecast:
7: Update 𝜋 𝜃 using PPO with the objective in (14).
8: end for
9: Output: risk-calibrated ABR policy 𝜋 𝜃
𝑐ˆ𝑡 = 𝜙(ℎ 𝑡), (15)
The predictor 𝜙 maps the available history, and Starlink-side
featuresℎ 𝑡 toonescalarcapacityvalueusedbytheauditor[6],
For a rollout batch B containing multiple trace episodes, [16]. A point predictor can set 𝑐ˆ𝑡 to its point forecast,
let 𝑅 𝑖 be the cumulative rebuffering of episode 𝑖 and let |B| while a lower-bound or risk-aware predictor returns a more
be the number of episodes in the batch. The empirical CVaR conservative value intended to reduce harmful overestimation.
penalty is estimated as
The predictor is not judged only by symmetric point error.
Its output is consumed by the feasible action set in (10);
1 ∑︁
C(cid:155)VaR𝛼(𝑅) =𝜉 𝛼+ (1−𝛼)|B| [𝑅 𝑖 −𝜉 𝛼] + , (13) therefore,anoverestimated𝑐ˆ𝑡 canmakeanunsafehigh-bitrate
𝑖∈B action appear feasible. Algorithm 3 summarizes the generic
constructionofthesafe-capacitypredictorusedbySafeSABR.
Here 𝜉 𝛼 is the empirical 𝛼-quantile of episode rebuffering The candidate set can include a point predictor and calibrated
within the rollout batch, and [𝑅 𝑖 − 𝜉 𝛼] + measures how far lower-bound predictors, and the final deployable SafeSABR
episode 𝑖 lies above this tail threshold. Episodes below the
uses BG-CFQS [16] as the risk-aware safe-capacity predictor.
threshold have zero excess term, while high-rebuffer episodes
increase the penalty. The fine-tuning objective is
(cid:34) 𝑇 (cid:35) E. Runtime Safety Auditing
∑︁
𝐽(𝜃) =E 𝜋𝜃 𝑞 𝑡 −𝜆C(cid:155)VaR𝛼(𝑅), (14)
Even after risk-calibrated RL fine-tuning, a learned policy
𝑡=1
can request an unsafe bitrate under abrupt Starlink drops.
ThefirsttermmaximizesexpectedQoEoverrolloutsgenerated Runtime safety auditing is the deployment-time risk-control
by 𝜋 𝜃, while the second term subtracts a penalty for tail layer of SafeSABR: it preserves feasible policy actions and
rebuffering. The weight 𝜆 controls this tradeoff: larger values changes only requests that violate the predicted buffer-safety
make the policy less willing to gain average quality through constraint.
actions that create severe stalls on a small fraction of traces. At deployment time, the learned policy first requests a raw
In implementation, the risk-calibrated fine-tuning stage uses action𝑎raw.SinceAisorderedbybitrate,therelation𝑎 ≤𝑎raw
𝑡 𝑡
PPO-style policy updates [37] with the CVaR tail penalty meansthataction𝑎 correspondstoabitratenohigherthanthe
above. Algorithm 2 summarizes the procedure. requestedbitrate.Thesafetyauditorthencomputesthelargest

8
Algorithm 4 Runtime Safety Auditing
1: Input: policy 𝜋 𝜃, predictor 𝜙, bitrate ladder A
2: Input: ABR state 𝑠 𝑡, recent history ℎ 𝑡, feasibility rule in
(10)
3: Select raw action 𝑎r 𝑡 aw ←argmax𝑎∈A 𝜋 𝜃(𝑎|𝑠 𝑡).
4: Predict safe capacity 𝑐ˆ𝑡 ← 𝜙(ℎ 𝑡).
5: Construct F𝑡(𝑐ˆ𝑡) according to (10).
6: Let C𝑡 ← {𝑎 ∈ F𝑡(𝑐ˆ𝑡) | 𝑎 ≤𝑎r 𝑡 aw}.
7: if C𝑡 is nonempty then
8: Set 𝑎s 𝑡 afe ←maxC𝑡.
9: else
10: Set𝑎s 𝑡 afe ←𝑎 min ,where𝑎 min isthelowestbitrateaction.
11: end if
12: Set 𝑚 𝑡 ←1{𝑎s 𝑡 afe ≠𝑎r 𝑡 aw}.
13: Output: executed action 𝑎s 𝑡 afe and intervention indicator
𝑚
𝑡
Fig.5. Decision-awaresafe-capacitypredictionandruntimesafetyauditing.
SafeSABR reduces severe-session rebuffering while preserv-
ing high QoE. The regional and handover-heavy experiments
action no higher than the request that satisfies the predicted thentestwhetherthisbehaviorremainsvisibleacrossdifferent
feasibility condition: Starlink trace groups and under mobility-induced stress. A
𝑎safe =
(cid:40) max (cid:8)𝑎 ∈ F𝑡(𝑐ˆ𝑡) | 𝑎 ≤𝑎r
𝑡
aw(cid:9), if the set is nonempty, h
ch
ar
a
d
n
-
g
tr
e
a
s
ce
bi
c
tr
a
a
s
t
e
e
s
d
tu
e
d
c
y
isi
f
o
u
n
r
s
the
in
r
s
i
i
l
d
lu
e
st
a
ra
d
te
i
s
ffi
h
c
o
u
w
lt
r
s
u
e
n
ss
ti
i
m
on
e
.
a
F
u
i
d
n
i
a
ti
l
n
ly
g
,
𝑡 𝑎
min
, otherwise,
the predictor-auditor analysis, staged ablation, and sensitiv-
(16) ity study isolate the roles of safe-capacity forecasting, risk-
If the raw request is already feasible, the maximum feasible calibrated RL fine-tuning, runtime auditing, and their key
action no higher than the request is the request itself, so parameters.
the learned decision is preserved. If the request is unsafe,
the auditor searches downward on the ordered bitrate ladder
A. Experimental Setting
and executes the highest lower bitrate that satisfies the buffer
guard. If no action satisfies the guard, the lowest bitrate 𝑎 min 1) Datasets and ABR Task: We evaluate SafeSABR using
isusedasafallback.Thus,theauditoractsasadecision-level therealStarlinkmeasurementdatasets[6].Thedatasetrecords
safety check rather than a blanket bitrate reduction rule. downlink throughput from Starlink terminals across multiple
We also record the intervention indicator regionsandcapturesthesatellite-networkdynamics,including
frequent serving-satellite changes and handovers. These prop-
𝑚 𝑡 =1{𝑎s 𝑡 afe ≠𝑎r 𝑡 aw}, (17) erties make the dataset suitable for evaluating whether ABR
The indicator 𝑚 𝑡 equals one only when the auditor changes algorithms can maintain high QoE without creating severe-
the policy request. Therefore, the average of 𝑚 𝑡 over chunks session stalls under rapid LEO access-link fluctuations.
measures how often deployment-time safety correction is The dataset includes regional measurements from Chicago,
needed. A lower intervention rate under comparable tail risk USA;OSN,Germany;andVictoria,Canada.Weprocessthese
indicatesbetterconsistencybetweenthetrainedpolicyandthe measurements into three regional datasets and denote them
safe-capacity constraint. as US, OSN, and VIC, respectively. For ABR evaluation,
each continuous throughput sequence is converted into SABR
Algorithm 4 summarizes the runtime safety-auditing pro-
replay traces, where each row records time and measured
cedure. Fig. 5 illustrates how the safe-capacity interface and
throughput at 1-s granularity. The ABR simulator then down-
runtime auditor work together. The predictor converts volatile
loads video chunks over these measured Starlink throughput
Starlink throughput forecasts into a safe capacity and the
traces. Table II summarizes the StarNet measurement source,
correspondingfeasiblebitrateset.Theauditorthenpreservesa
processed throughput samples, handover statistics, and trace-
feasiblepolicyrequest,butdownshiftsanunsaferequesttothe
set split. The trace-set split is reported in the format of
highest feasible lower bitrate, protecting the playback buffer
train/calibration/test trace counts.
from severe depletion.
The training split is used to train behavior-cloning and RL
policies. The calibration split is used to select safe-capacity
V. PERFORMANCEEVALUATION
operating points and predictor-auditor parameters. The test
This section evaluates whether SafeSABR improves the split is held out for final reporting. To stress ABR decisions
QoE–severe-riskoperatingpointofhigh-bitrateABRoverreal under high-capacity but volatile satellite access, we use a
Starlink traces. After introducing the experimental setting, the 4K/8K-style high-bitrate ladder and chunk configuration, as
main comparison and operating-point plot examine whether summarized later in Table III.

9
TABLEII
SUMMARYOFSTARLINKABRDATASETS.
Item US OSN VIC Total
Location Chicago,USA OSN,Germany Victoria,Canada –
Processedperiod 2024-04-26–2024-05-28 2024-07-13–2024-07-31 2024-07-11–2024-07-28 –
Throughputsamples 1,123,832 613,295 145,053 1,882,180
Traceminutes 41,252 10,221 2,417 53,890
Satellitehandovers 86,808 26,782 7,257 120,847
Trace-setsplit 169/36/36 91/19/20 109/24/23 369/79/79
2) BaselinesandMethodVariants: WecompareSafeSABR (5). Average QoE and mean rebuffering are reported as
with representative online, prediction-assisted, and learned
1 ∑︁ 1 ∑︁
ABR methods. The non-learned online baselines include 𝑄¯ = 𝑄 𝑖 , 𝑅¯ = 𝑅 𝑖 . (18)
|I| |I|
BOLA [28] and RobustMPC [27]. The prediction-assisted 𝑖∈I 𝑖∈I
online baselines include Lumos-MPC [24], [25] and StarNet- To estimate the tail-rebuffering risk in (7) with 𝛽 = 0.95,
MPC [6], which combine throughput prediction with the we report the average cumulative rebuffering of the worst 5%
same MPC decision logic. BOLA makes bitrate decisions sessions:
from buffer occupancy, RobustMPC uses history-based ro- 1 ∑︁
bust throughput estimation with a five-chunk planning hori- 𝑅 worst5 = 𝐾 𝑅 𝑖 , 𝐾 = ⌈0.05|I|⌉. (19)
zon, Lumos-MPC feeds a Lumos-style decision-tree through- 𝑖∈Top𝐾({𝑅𝑗}𝑗∈I)
put predictor into MPC, and StarNet-MPC feeds StarNet Here Top (·) returns the indices of the 𝐾 evaluated sessions
𝐾
point throughput predictions into MPC. The learned base- with the largest cumulative rebuffering values. To estimate
lines include Pensieve [29], Comyco [30], and SABR [17]. the severe-stall probability in (8) with 𝜌 = 10 s, we report
0
Pensieve represents RL-based neural ABR, Comyco repre- the fraction of sessions with more than 10 s cumulative
sents imitation-learning-based ABR, and SABR denotes the rebuffering:
behavior-cloning-pretrained policy with vanilla PPO fine- 1 ∑︁
tuning [37].
𝑆 >10 =
|I|
1{𝑅 𝑖 >10}. (20)
𝑖∈I
For mechanism analysis, we compare several safe-capacity Inexperimentsinvolvingtheruntimeauditor,wealsoreport
predictor variants. StarNet-point denotes the point-throughput the audit intervention rate, i.e., the average value of 𝑚 𝑡 in
forecast produced by the StarNet predictor [6]. StarNet-LB (17), to quantify how often the auditor changes the policy
denotes a calibrated lower-bound (LB) version of StarNet, request. For the predictor-auditor analysis, let D be the
dec
where the point forecast is converted into a conservative safe- decision-evaluation samples and let
𝑎𝜙
be the action admitted
𝑡
capacity estimate on the calibration split. Xgboost-LB uses by predictor 𝜙. The decision-violation rate is
an XGBoost [38] regression model with the same lower-
bound calibration interface. BG-CFQS is the risk-aware safe 𝑉 dec = |D 1 | ∑︁ 𝑣 𝑡(𝑎 𝑡 𝜙 ). (21)
throughput forecasting method proposed in [16]; it provides dec 𝑡∈D
dec
calibrated lower-bound capacity estimates for Starlink control To focus on harmful positive prediction errors in difficult link
andisusedasthedefaultsafe-capacitypredictorinSafeSABR. states, we also report the high-risk overestimation rate over
These variants separate point prediction, lower-bound predic- low-throughput samples:
tion, risk-aware forecasting, and runtime auditing.
1 ∑︁
OverRate
HR
=
|D |
1{𝑐ˆ𝑡 >𝑐 𝑡}, (22)
3) Implementation Details and Hyperparameters: All HR 𝑡∈DHR
learned policies use the same Starlink high-bitrate setting
where D contains samples whose realized throughput be-
HR
unless otherwise specified. Behavior cloning uses a beam-
longs to the lowest 30% of the evaluation set.
searchexpert[30],[36],andPPOisimplementedwithStable-
Baselines3 [39] using a multi-layer perceptron (MLP) policy.
B. Comparison with Advanced ABR Methods
The CVaR penalty is used only during training; all reported
rewards are computed with the original QoE reward in (4). This experiment provides the comparison against repre-
Safe-capacity predictors are calibrated only on the held-out sentative ABR methods and tests the central question of
calibration traces before being evaluated on the test traces. this paper: whether SafeSABR can reduce severe session-
TableIIIsummarizesthemainexperimentalconfigurationand level rebuffering without collapsing average QoE. Table IV
hyperparameters. reports the result as a QoE–severe-risk tradeoff using the
session-level metrics defined above. BOLA and RobustMPC
4) Evaluation Metrics: All final results are reported on the are used as conservative low-risk references, while Lumos-
held-out test traces using finite-sample QoE and severe-risk MPC, StarNet-MPC, Pensieve, Comyco, and SABR represent
metrics. For each evaluated session 𝑖 ∈ I, we compute its high-QoE prediction-assisted or learned baselines. The QoE
session QoE 𝑄 𝑖 and cumulative rebuffering 𝑅 𝑖 according to Cost column is computed only for high-QoE baselines and

10
TABLEIII
IMPLEMENTATIONANDHYPERPARAMETERCONFIGURATION.
| Item |     | Value |     |     |     |     |     |     |     |     |
| ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ABRsimulator
| Bitrateladder |     | 3,8,15,30,60,120Mbps |     |     |     |     |     |     |     |     |
| ------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Videosetting 48chunks,4sperchunk,mildvariable-bitratechunk-sizevariation
| Playbackbuffer   |     | Maximumbuffer60s |                        |     |     |     |     |     |     |     |
| ---------------- | --- | ---------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
|                  |     |                  | 𝜇=40,smoothnesspenalty |     |     | 𝜂=1 |     |     |     |     |
| QoErewardweights |     | Rebufferpenalty  |                        |     |     |     |     |     |     |     |
Behavior-cloningpretraining
Expertanddataaggregation Beam-searchexpert,15DAggeriterations,2000rolloutstepsperiteration
Behavior-cloningoptimizer Adam,learningrate10−3,batchsize128,5epochsperDAggeriteration
Behavior-cloningloss Expert-actionnegativelog-likelihood,equivalenttocategoricalcross-entropy;entropycoefficient0
Risk-calibratedRLfine-tuning
PPOimplementation Stable-Baselines3PPOwithMLPpolicy,4parallelenvironments,50ktrainingsteps
PPOrollout/update 𝑛 =512perenvironment,batchsize64,10epochsperupdate
steps
PPOoptimization Learningrate3×10−4, 𝛾=0.99,generalizedadvantageestimation𝜆=0.95,cliprange0.2
PPOregularization Entropycoefficient0,value-losscoefficient0.5,maxgradientnorm0.5
Normalization Rewardnormalizationenabledwithclipping10;observationnormalizationdisabled
𝛼=0.90,penaltyweight𝜆=20,budget0,window512
| CVaR-PPOinstantiation |     | Modecvar_rebuf, |     |     |     |     |     |     |     |     |
| --------------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Predictorandimplementation
Safe-capacitypredictor Inputlength75s,predictionhorizon15s,calibratedonthecalibrationsplit
TABLEIV
QOE–SEVERE-RISKTRADEOFFONSTARLINKTRACES.
Group Method QoE MeanRebuf(s) Worst-5%Rebuf(s) Session >10s(%) QoECost
|     | Conservativeref. | BOLA        | 4108.66 | 1.42  |     | 14.12  |     | 2.5%  | –    |     |
| --- | ---------------- | ----------- | ------- | ----- | --- | ------ | --- | ----- | ---- | --- |
|     | Conservativeref. | RobustMPC   | 4568.16 | 1.74  |     | 16.33  |     | 3.8%  | –    |     |
|     | High-QoEbaseline | Lumos-MPC   | 4660.07 | 8.07  |     | 63.83  |     | 22.8% | 0.6% |     |
|     | High-QoEbaseline | StarNet-MPC | 4684.98 | 5.92  |     | 40.40  |     | 21.5% | 1.2% |     |
|     | High-QoEbaseline | Pensieve    | 4644.89 | 20.49 |     | 134.40 |     | 35.0% | 0.3% |     |
|     | High-QoEbaseline | Comyco      | 4732.19 | 7.38  |     | 39.72  |     | 25.3% | 2.1% |     |
|     | High-QoEbaseline | SABR        | 4715.33 | 7.77  |     | 54.30  |     | 22.8% | 1.8% |     |
|     | Ours             | SafeSABR    | 4630.81 | 2.50  |     | 22.68  |     | 7.2%  | –    |     |
indicatestherelativeQoEdecreaseofSafeSABRwithrespect fraction of sessions with more than 10 s cumulative rebuffer-
to each baseline. ing.Theverticaldashedlineineachpanelmarksthepreferred
The conservative references confirm that rebuffering risk low-risk side, and the red arrow indicates the better direction
can be reduced by choosing lower-quality operating points: along the risk axis.
BOLA and RobustMPC have low severe-stall ratios, but their BOLA and RobustMPC remain on the preferred low-risk
QoE scores are 4108.66 and 4568.16. In contrast, high-QoE side, but they also appear in the lower-QoE region. Lumos-
baselines expose much larger severe session tails. Lumos- MPC, StarNet-MPC, Pensieve, Comyco, and SABR move
MPC, StarNet-MPC, Pensieve, Comyco, and SABR reach upward in QoE, while most of their points fall to the right of
QoE values between 4644.89 and 4732.19, but their worst- the risk boundary, especially in the severe-session-ratio view.
5% session rebuffering ranges from 39.72 s to 134.40 s, and SafeSABR is not the topmost point in QoE, but it moves
21.5%–35.0% of their sessions exceed 10 s of cumulative back toward the preferred side of both risk axes while staying
rebuffering. SafeSABR keeps a comparable QoE level of close to the high-QoE group. This visual pattern supports the
4630.81 while reducing mean rebuffering to 2.50 s, worst- main claim of SafeSABR: it improves the QoE–severe-risk
5% session rebuffering to 22.68 s, and the severe-stall session operating point rather than simply maximizing average QoE
ratioto7.2%.ComparedwithSABR,SafeSABRreducesmean or conservatively lowering bitrate quality.
rebufferingfrom7.77sto2.50sandsevere-stallsessionsfrom
| 22.8%       | to 7.2%, with a 1.8% | QoE cost.        | Thus, the main | value   |               |        |          |         |     |     |
| ----------- | -------------------- | ---------------- | -------------- | ------- | ------------- | ------ | -------- | ------- | --- | --- |
|             |                      |                  |                |         | D. Robustness | Across | Starlink | Regions |     |     |
| of SafeSABR | is not to            | maximize average | QoE, but       | to move |               |        |          |         |     |     |
high-QoE ABR toward a safer severe-risk operating point. This experiment evaluates whether the QoE–severe-risk ad-
|     |     |     |     |     | vantage | of SafeSABR | remains | stable | across different | Starlink |
| --- | --- | --- | --- | --- | ------- | ----------- | ------- | ------ | ---------------- | -------- |
measurementregions.TheUS,OSN,andVICtracegroupsex-
| C. QoE–Severe-Risk | Tradeoff |     |     |     |       |                      |               |     |              |           |
| ------------------ | -------- | --- | --- | --- | ----- | -------------------- | ------------- | --- | ------------ | --------- |
|                    |          |     |     |     | hibit | different throughput | distributions |     | and handover | patterns, |
This experiment examines the operating position of each providing a regional robustness test beyond the aggregate
method in the QoE–severe-risk space. To make the tradeoff result. Fig. 7 reports severe-session metrics separately for
visible, Fig. 6 plots average QoE against two complementary each region. The two heatmaps correspond to the worst-5%
severe-risk estimates: worst-5% session rebuffering and the session rebuffering and severe-stall session ratio, respectively.

11
Fig.6. QoE–severe-riskoperatingpointsonStarlinktraces.
Fig.7. RobustnessacrossStarlinkregions.
Darker cells indicate larger severe-session risk, so a robust whichcoverstheplaybackwindowusedbythe48-chunkABR
method should remain lighter across regions rather than only evaluation. Within each StarNet region, the top 30% traces by
performing well on the aggregate test set. handover count are labeled handover-heavy, with large one-
The US trace group is the hardest case for all high-QoE secondthroughputdropsusedonlytobreakties.Thisproduces
methods, but SafeSABR still keeps the worst-5% session 24 handover-heavy traces, with 11 from US, 6 from OSN,
rebuffering at 29.5 s, compared with 48.1 s for StarNet-MPC, and 7 from VIC. In Fig. 8, each line connects the normal and
43.5 s for Comyco, and 64.7 s for SABR. On OSN and VIC, handover-heavy results of the same method, so a rightward
SafeSABRfurtherreducesworst-5%sessionrebufferingto2.1 shift indicates that handover-heavy periods amplify playback
sand15.7s,respectively.Thesevere-stallsessionratiofollows risk.
thesametrend:SafeSABRhas12.0%,0.0%,and5.8%severe-
The handover-heavy traces contain 17.2 handovers on aver-
stallsessionsonUS,OSN,andVIC,lowerthanthehigh-QoE
age during the 300-s window, compared with 14.6 for normal
baselines in every region. This indicates that the SafeSABR
traces, and this stress subset increases playback risk for all
gain is not tied to a single regional trace group.
high-QoE baselines. For example, StarNet-MPC mean re-
bufferingrisesfrom4.61sto8.92s,andSABRrisesfrom6.25
E. Stress Test on Handover-Heavy Traces
s to 11.25 s. The severe-stall session ratio also increases from
ThisexperimentevaluatesSafeSABRunderStarlinkmobil- 14.5% to 37.5% for StarNet-MPC, from 17.6% to 34.7% for
ity stress by focusing on handover-heavy traces. The goal is SABR,andfrom4.8%to12.5%forSafeSABR.Onhandover-
to examine how frequently serving-satellite changes amplify heavy traces, SafeSABR keeps mean rebuffering at 3.95 s,
severe-session rebuffering and whether the proposed risk- worst-5% session rebuffering at 24.22 s, and severe-stall
calibrated control remains effective in these difficult periods. sessionsat12.5%.Incontrast,StarNet-MPC,Comyco,SABR,
We construct the stress subset from the Starlink han- and Pensieve reach 37.5%, 33.3%, 34.7%, and 48.6% severe-
dover metadata. For each test trace, we count serving-satellite stall sessions, respectively. This shows that the SafeSABR
changes during the first 300 s of the measurement sequence, advantage becomes more relevant under Starlink-specific han-

12
Fig.8. Stresstestonhandover-heavyStarlinktraces.
dover stress.
F. Hard-Trace Mechanism Case Study
The aggregate results show that SafeSABR reduces severe-
sessionstalls,buttheydonotshowwhenthedeployment-time
safetylayerchangesabitratedecisioninsideasession.There-
fore, this case study inspects one hard Starlink trace in which
the risk-calibrated policy still requests aggressive bitrates dur-
ing throughput drops and frequent serving-satellite handovers.
Fig. 9 summarizes the mechanism in three steps: panel (a)
compares the measured throughput with the BG-CFQS safe-
capacityestimateusedbytheauditor,panel(b)showshowthe
auditor maps policy-requested bitrates to SafeSABR-executed
bitrates, and panel (c) compares cumulative rebuffering with
and without runtime auditing.
Reading the three panels together shows that the auditor
is not active throughout the session. It changes the requested
action only when the requested bitrate remains high while the
BG-CFQSsafe-capacityestimatefalls.Theseselectivecorrec-
tions reduce the executed bitrate before the severe-stall region
showninpanel(c),preventingthelargecumulativerebuffering
jump that appears when SafeSABR is used without runtime
auditing. On this trace, cumulative rebuffering decreases from
31.375 s to 2.884 s, while the total QoE increases from
1389.00 to 2566.63 because avoiding the long stall outweighs
the temporary bitrate reductions. This example explains the
mechanism behind the aggregate results: SafeSABR does not
obtain safety by uniformly lowering bitrate quality, but by
auditing high-risk decisions under difficult Starlink states.
G. Predictor and Safety Auditor Analysis
Fig.9. MechanismcasestudyonarepresentativehardStarlinktrace.
This experiment evaluates whether safe-capacity prediction
provides useful decision information for the runtime auditor.
Insteadoftestingstandalonethroughputpredictionaccuracy,it predictor input to the auditor is changed. The two decision-
measures whether different predictor interfaces reduce unsafe side metric columns measure predictor risk through decision
bitrateadmissionsanddownstreamsevere-sessionrebuffering. violation and high-risk overestimation, while the remaining
Table V compares four predictor interfaces under the same metriccolumnsreportdownstreamABRrebufferingandaudit
ABR control pipeline. To isolate the effect of safe-capacity frequency. A useful safe-capacity predictor should reduce
prediction, all rows use the same SafeSABR policy before decision violations and high-risk overestimation, and this
runtime auditing and the same auditing rule, while only the reduction should translate into lower severe-session playback

13
TABLEV
PREDICTORANDSAFETY-AUDITORANALYSISUNDERTHESAMEPRE-AUDITSAFESABRPOLICY.
Predictor Dec.Viol. OverRateHR MeanRebuf(s) Worst-5%Rebuf(s) AuditRate
|     |     | StarNet-point |     | 26.6% |     | 75.5% | 3.10 |     | 26.16 |     | 3.1% |     |     |     |
| --- | --- | ------------- | --- | ----- | --- | ----- | ---- | --- | ----- | --- | ---- | --- | --- | --- |
|     |     | StarNet-LB    |     | 21.6% |     | 70.3% | 2.85 |     | 24.24 |     | 3.5% |     |     |     |
|     |     | Xgboost-LB    |     | 21.4% |     | 73.6% | 2.95 |     | 24.98 |     | 3.2% |     |     |     |
|     |     | BG-CFQS       |     | 20.5% |     | 69.3% | 2.50 |     | 22.68 |     | 4.3% |     |     |     |
TABLEVI
ABLATIONOFSAFESABRDESIGNSTAGESUSINGSESSION-LEVELSEVERE-RISKMETRICS.
|     |     |     | Components |     |     |     |     |     |     | Metrics |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
BehaviorCloning Risk-calibratedFine-tuning SafetyAuditor QoE MeanRebuf(s) Worst-5%Rebuf(s) Session >10s(%)
✓
|     |     |     |     | –   |     | –   | 4738.33 | 8.88 |     |     | 49.32 |     | 28.7% |      |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | --- | ----- | --- | ----- | ---- |
|     | ✓   |     |     | ✓   |     |     |         |      |     |     |       |     |       |      |
|     |     |     |     |     |     | –   | 4683.64 | 4.74 |     |     | 30.14 |     | 17.3% |      |
|     | ✓   |     |     | –   |     | ✓   | 4657.80 | 3.15 |     |     | 29.67 |     |       | 9.7% |
|     | ✓   |     |     | ✓   |     | ✓   | 4630.81 | 2.50 |     |     | 22.68 |     | 7.2%  |      |
risk without requiring excessive audit intervention. I. Sensitivity to Risk and Auditing Parameters
StarNet-point has the highest decision violation rate and This experiment analyzes the two risk-control parameters
high-risk overestimation rate, showing that point prediction is that determine the SafeSABR operating point: the CVaR
not sufficient for safety-critical ABR decisions. StarNet-LB penalty weight in risk-calibrated RL fine-tuning and the mar-
lowers both rates by exposing the auditor to a conservative gin used by the runtime auditor. Table VII separates the
| capacity | estimate. | Xgboost-LB |     | has a similar |     | average decision |          |      |             |     |           |       |        |          |
| -------- | --------- | ---------- | --- | ------------- | --- | ---------------- | -------- | ---- | ----------- | --- | --------- | ----- | ------ | -------- |
|          |           |            |     |               |     |                  | analysis | into | two blocks. |     | The first | block | varies | the CVaR |
violation rate to StarNet-LB, but its larger high-risk overes- penaltyweightwithoutruntimeauditing,isolatingtheeffectof
timation rate leaves a larger severe-session tail. BG-CFQS training-time risk calibration. The second block fixes 𝜆 = 20
| gives | the lowest | decision | violation, | high-risk |     | overestimation, |            |     |         |         |     |         |           |            |
| ----- | ---------- | -------- | ---------- | --------- | --- | --------------- | ---------- | --- | ------- | ------- | --- | ------- | --------- | ---------- |
|       |            |          |            |           |     |                 | and varies | the | BG-CFQS | auditor |     | margin, | isolating | the effect |
meanrebuffering,andworst-5%sessionrebufferingamongthe of deployment-time action auditing. Each block is compared
| compared | predictors. | Its | audit | rate is only | 4.3%, | and the | QoE      |               |     |                 |     |             |     |      |
| -------- | ----------- | --- | ----- | ------------ | ----- | ------- | -------- | ------------- | --- | --------------- | --- | ----------- | --- | ---- |
|          |             |     |       |              |       |         | with its | corresponding |     | no-risk-control |     | or no-audit |     | row. |
scores of the predictor variants remain within a narrow range Withoutruntimeauditing,increasingtheCVaRpenaltyfrom
of 4619.18–4630.81. Therefore, the gain is not obtained by 𝜆 = 0 to 𝜆 = 20 reduces worst-5% session rebuffering
| crudely | lowering | bitrate | quality; | it comes | from | using | a safer    |     |          |       |        |     |              |         |
| ------- | -------- | ------- | -------- | -------- | ---- | ----- | ---------- | --- | -------- | ----- | ------ | --- | ------------ | ------- |
|         |          |         |          |          |      |       | from 54.30 | s   | to 30.14 | s and | lowers | the | severe-stall | session |
predictor-auditor interface for ABR decisions. ratio from 22.8% to 17.3%, with a small QoE decrease. A
𝜆 =
|              |            |                   |            |                |                 |                 | larger      | penalty        | 40           | further     | lowers    | the        | severe-stall | ratio       |
| ------------ | ---------- | ----------------- | ---------- | -------------- | --------------- | --------------- | ----------- | -------------- | ------------ | ----------- | --------- | ---------- | ------------ | ----------- |
|              |            |                   |            |                |                 |                 | to 16.5%,   | but            | it does      | not         | improve   | the        | mean or      | worst-5%    |
|              |            |                   |            |                |                 |                 | rebuffering | over           | 𝜆 =          | 20. After   | fixing    | 𝜆 =        | 20, the      | BG-CFQS     |
| H. Ablation  |            | Study of SafeSABR |            |                |                 |                 |             |                |              |             |           |            |              |             |
|              |            |                   |            |                |                 |                 | auditor     | gives          | similar      | severe-risk |           | reductions | across       | margins     |
|              |            |                   |            |                |                 |                 | 𝑚 = 0.90,   | 0.95,          | and          | 1.00.       | All three | audited    | settings     | reduce      |
| This         | experiment | quantifies        |            | the            | contribution    | of              | each        |                |              |             |           |            |              |             |
|              |            |                   |            |                |                 |                 | worst-5%    | session        | rebuffering  |             | from      | 30.14      | s to         | about 22–23 |
| SafeSABR     | design     | stage             | to QoE     | preservation   |                 | and severe-risk |             |                |              |             |           |            |              |             |
|              |            |                   |            |                |                 |                 | s and       | reduce         | severe-stall | sessions    |           | from       | 17.3%        | to 8.0% or  |
| reduction.   | We         | construct         | controlled | configurations |                 | by enabling     |             |                |              |             |           |            |              |             |
|              |            |                   |            |                |                 |                 | lower,      | while auditing |              | only        | 3.8%–4.3% | of         | chunks.      | The final   |
| or disabling |            | behavior-cloning  |            | pretraining,   | risk-calibrated |                 | RL          |                |              |             |           |            |              |             |
𝑚 =0.90
fine-tuning, and the Safety Auditor. In Table VI, checkmarks setting is selected because it gives the lowest mean
|          |       |            |     |         |         |                | rebuffering | and         | severe-stall |          | session  | ratio    | among | the audited |
| -------- | ----- | ---------- | --- | ------- | ------- | -------------- | ----------- | ----------- | ------------ | -------- | -------- | -------- | ----- | ----------- |
| indicate | which | components | are | enabled | in each | configuration. |             |             |              |          |          |          |       |             |
|          |       |            |     |         |         |                | settings,   | not because |              | it is an | isolated | optimum. |       |             |
Behavior-cloninggivesthehighestQoE,butitleaves28.7%
| of sessions | with | more | than 10 | s of | cumulative | rebuffering. |     |     |     |     |     |     |     |     |
| ----------- | ---- | ---- | ------- | ---- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Adding risk-calibrated RL fine-tuning reduces mean rebuffer- VI. CONCLUSION
ing from 8.88 s to 4.74 s and lowers the severe-stall session This paper presented SafeSABR, a risk-calibrated
ratio from 28.7% to 17.3%, showing the effect of training- prediction-control framework for adaptive bitrate streaming
timeriskcalibrationbeforeanyruntimecorrection.Addingthe over Starlink networks. We formulated high-bitrate Starlink
SafetyAuditorwithoutrisk-calibratedfine-tuningalsoreduces ABR as a QoE–severe-risk tradeoff problem and used
severe stalls, but the full SafeSABR configuration gives the session-level metrics to expose severe rebuffering that
lowest mean rebuffering, worst-5% session rebuffering, and can be hidden by average QoE. SafeSABR combines
severe-stall session ratio. This result supports the intended behavior-cloning pretraining for a high-QoE ABR prior,
divisionoflabor:behaviorcloningprovidesahigh-QoEprior, risk-calibrated RL fine-tuning with CVaR-PPO for reducing
risk-calibrated RL fine-tuning performs training-time calibra- severe-tail action tendencies, and a BG-CFQS-driven runtime
tion, and the runtime auditor corrects residual unsafe bitrate safety auditor for correcting unsafe bitrate requests at
requests. deployment time. Experiments on real Starlink network

14
TABLEVII
SENSITIVITYTORISK-TRAININGANDRUNTIMEAUDITINGPARAMETERS.
Parameter Setting QoE MeanRebuf(s) Worst-5%Rebuf(s) Session >10s(%) AuditRate
CVaRweight 𝜆=0 4715.33 7.77 54.30 22.8% –
CVaRweight 𝜆=10 4710.56 6.30 35.80 20.3% –
CVaRweight 𝜆=20 4683.64 4.74 30.14 17.3% –
CVaRweight 𝜆=40 4674.43 5.03 34.76 16.5% –
Auditormargin Noaudit 4683.64 4.74 30.14 17.3% 0.0%
Auditormargin 𝑚=0.90 4630.81 2.50 22.68 7.2% 4.3%
Auditormargin 𝑚=0.95 4638.40 2.54 22.57 8.0% 4.0%
Auditormargin 𝑚=1.00 4638.62 2.61 22.41 7.6% 3.8%
traces show that SafeSABR reduces severe-stall sessions [13] W. Li, X. Li, Y. Xu, Y. Yang, and S. Lu, “Metaabr: A meta-learning
from 22.8% for SABR to 7.2%, with a 1.8% QoE cost. approach on adaptative bitrate selection for video streaming,” IEEE
TransactionsonMobileComputing,vol.23,no.3,pp.2422–2437,2023.
Predictor-auditor, ablation, and sensitivity analyses further
[14] N.Kan,C.Li,Y.Jiang,W.Dai,J.Zou,H.Xiong,andL.Toni,“Merina+:
support the complementary roles of risk-calibrated RL Improving generalization for neural video adaptation via information-
fine-tuning, decision-aware safe-capacity prediction, and theoretic meta-reinforcement learning,” IEEE Transactions on Circuits
andSystemsforVideoTechnology,2025.
runtime auditing. These results support using risk-calibrated
[15] D. Wu, X. Wang, Y. Qiao, Z. Wang, J. Jiang, S. Cui, and F. Wang,
learned control, safe-capacity auditing, and QoE–severe-risk “Netllm:Adaptinglargelanguagemodelsfornetworking,”inProceed-
evaluation together for high-bitrate ABR over volatile LEO ingsoftheACMSIGCOMM2024Conference,2024,pp.661–678.
[16] H. Xie, C. Zhang, P. Luo, Z. Zhang, G. Yang, X. Zhang, and B.-H.
satellite links. Future work will explore how large language
Soong,“Risk-awaresafethroughputforecastingforstarlinknetworks,”
model-based artificial intelligence agents can assist Starlink 2026.[Online].Available:https://arxiv.org/abs/2605.09508
ABR systems by interpreting network context, coordinating [17] P. Luo, Y. Zhao, B. Zhang, G. Yang, B.-H. Soong, and C. Yuen,
“SABR: A stable adaptive bitrate framework using behavior cloning
prediction-control modules, and adapting safety policies
pretraining and reinforcement learning fine-tuning,” arXiv preprint
across heterogeneous application scenarios. arXiv:2509.10486,2025.
[18] S. Ma, Y. C. Chou, H. Zhao, L. Chen, X. Ma, and J. Liu, “Network
characteristicsofLEOsatelliteconstellations:Astarlink-basedmeasure-
REFERENCES mentfromendusers,”inIEEEINFOCOM2023-IEEEConferenceon
ComputerCommunications,2023,pp.1–10.
[1] F. Michel, M. Trevisan, D. Giordano, and O. Bonaventure, “A first [19] N. Mohan, A. E. Ferguson, H. Cech, R. Bose, P. R. Renatin, M. K.
lookatstarlinkperformance,”inProceedingsofthe22ndACMInternet Marina, and J. Ott, “A multifaceted look at starlink performance,” in
MeasurementConference,2022,pp.130–136. ProceedingsoftheACMWebConference2024,2024,pp.2723–2734.
[2] M. M. Kassem, A. Raman, D. Perino, and N. Sastry, “A browser-side [20] H. B. Tanveer, M. Puchol, R. Singh, A. Bianchi, and R. Nithyanand,
viewofstarlinkconnectivity,”inProceedingsofthe22ndACMInternet “Makingsenseofconstellations:Methodologiesforunderstandingstar-
MeasurementConference,2022,pp.151–158. link’s scheduling algorithms,” in Companion of the 19th International
[3] K.Chen,C.Qi,C.-X.Wang,andG.Y.Li,“Beamtrainingandtracking Conference on Emerging Networking EXperiments and Technologies,
for extremely large-scale MIMO communications,” IEEE Transactions 2023,pp.37–43.
onWirelessCommunications,vol.23,no.5,pp.5048–5062,May2024. [21] H.Zhao,H.Fang,F.Wang,andJ.Liu,“Realtimemultimediaservices
[4] J. Garcia, S. Sundberg, G. Caso, and A. Brunstrom, “Multi-timescale overstarlink:Arealitycheck,”inProceedingsofthe33rdWorkshopon
evaluation of starlink throughput,” in Proceedings of the 1st ACM Network and Operating System Support for Digital Audio and Video,
WorkshoponLEONetworkingandCommunication,2023,pp.31–36. 2023,pp.43–49.
[5] K.Chen,C.Qi,andO.A.Dobre,“DBRAA:Sub-6GHzandmillimeter [22] J.ZhaoandJ.Pan,“Low-latencylivevideostreamingoveralow-earth-
wavedual-bandreconfigurableantennaarrayforISAC,”IEEETransac- orbit satellite network with DASH,” in Proceedings of the 15th ACM
tionsonCommunications,vol.73,no.10,pp.9830–9845,Oct.2025. MultimediaSystemsConference,2024,pp.109–120.
[6] Z.Liu,F.-X.G.Reidys,S.Tanveer,andD.Vasisht,“Vivisectingstarlink [23] L. Izhikevich, R. Enghardt, T.-Y. Huang, and R. Teixeira, “A global
throughput:Measurementandprediction,”ProceedingsoftheACMon perspective on the past, present, and future of video streaming over
Networking,vol.3,no.CoNEXT4,pp.1–23,2025. starlink,” Proceedings of the ACM on Measurement and Analysis of
[7] S. Tiwari, S. Bhushan, A. Taneja, M. M. Kassem, C. Luo, C. Zhou, ComputingSystems,vol.8,no.3,pp.1–22,2024.
Z. He, A. Raman, N. Sastry, L. Qiu, and D. Bhattacherjee, “T3P: [24] G. Lv, Q. Wu, W. Wang, Z. Li, and G. Xie, “Lumos: Towards better
Demystifying low-earth orbit satellite broadband,” arXiv preprint videostreamingQoEthroughaccuratethroughputprediction,”inIEEE
arXiv:2310.11835,2023. INFOCOM 2022 - IEEE Conference on Computer Communications.
[8] K.Chen,C.Qi,J.Huang,O.A.Dobre,andG.Y.Li,“Near-fieldcommu- IEEE,2022,pp.650–659.
nications for extremely large-scale MIMO: A beamspace perspective,” [25] G.Lv,Q.Wu,Q.Tan,W.Wang,Z.Li,andG.Xie,“Accuratethroughput
IEEE Communications Magazine, vol. 63, no. 5, pp. 166–172, May prediction for improving QoE in mobile adaptive streaming,” IEEE
2025. TransactionsonMobileComputing,vol.23,no.5,pp.5799–5817,2024.
[9] Z.Xia,Y.Zhou,F.Y.Yan,andJ.Jiang,“Genet:Automaticcurriculum [26] J.Garcia,M.Beckerle,S.Sundberg,andA.Brunstrom,“Modelingand
generationforlearningadaptationinnetworking,”inProceedingsofthe predictingstarlinkthroughputwithfine-grainedburstcharacterization,”
ACMSIGCOMM2022Conference,2022,pp.397–413. ComputerCommunications,vol.234,p.108090,2025.
[10] L. Yi, Y. Qin, and R. Huang, “Optimizing adaptive video streaming: [27] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
Offlinereinforcementlearningandmeta-learningindiversenetworks,” approach for dynamic adaptive video streaming over HTTP,” in Pro-
IEEETransactionsonMultimedia,2025. ceedings of the 2015 ACM Conference on Special Interest Group on
[11] A.Bentaleb,M.Lim,M.N.Akcay,A.C.Begen,andR.Zimmermann, DataCommunication,2015,pp.325–338.
“Metareinforcementlearningforrateadaptation,”inIEEEINFOCOM [28] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
2023-IEEE Conference on Computer Communications. IEEE, 2023, bitrate adaptation for online videos,” IEEE/ACM Transactions on Net-
pp.1–10. working,vol.28,no.4,pp.1698–1711,2020.
[12] ——,“Bitrateadaptationandguidancewithmetareinforcementlearn- [29] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream-
ing,” IEEE Transactions on Mobile Computing, vol. 23, no. 11, pp. ingwithpensieve,”inProceedingsoftheConferenceoftheACMSpecial
10378–10392,2024. InterestGrouponDataCommunication,2017,pp.197–210.

15
[30] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco:
Quality-aware adaptive video streaming via imitation learning,” in
Proceedingsofthe27thACMInternationalConferenceonMultimedia,
2019,pp.429–437.
[31] R. T. Rockafellar and S. Uryasev, “Optimization of conditional value-
at-risk,”JournalofRisk,vol.2,no.3,pp.21–41,2000.
[32] Y. Chow, A. Tamar, S. Mannor, and M. Pavone, “Risk-sensitive and
robust decision-making: A CVaR optimization approach,” in Advances
inNeuralInformationProcessingSystems,vol.28,2015.
[33] Y. Chow, M. Ghavamzadeh, L. Janson, and M. Pavone, “Risk-
constrainedreinforcementlearningwithpercentileriskcriteria,”Journal
ofMachineLearningResearch,vol.18,no.167,pp.1–51,2018.
[34] M. Alshiekh, R. Bloem, R. Ehlers, B. Könighofer, S. Niekum, and
U. Topcu, “Safe reinforcement learning via shielding,” in Proceedings
oftheAAAIConferenceonArtificialIntelligence,vol.32,no.1,2018,
pp.2669–2678.
[35] S. Ross, G. J. Gordon, and J. A. Bagnell, “A reduction of imitation
learning and structured prediction to no-regret online learning,” in
Proceedings of the Fourteenth International Conference on Artificial
IntelligenceandStatistics,2011,pp.627–635.
[36] T. Huang, C. Zhou, X. Yao, R.-X. Zhang, C. Wu, B. Yu, and L. Sun,
“Quality-awareneuraladaptivevideostreamingwithlifelongimitation
learning,”IEEEJournalonSelectedAreasinCommunications,vol.38,
no.10,pp.2324–2342,2020.
[37] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Prox-
imalpolicyoptimizationalgorithms,”arXivpreprintarXiv:1707.06347,
2017.
[38] T. Chen and C. Guestrin, “Xgboost: A scalable tree boosting system,”
in Proceedings of the 22nd acm sigkdd international conference on
knowledgediscoveryanddatamining,2016,pp.785–794.
[39] A.Raffin,A.Hill,A.Gleave,A.Kanervisto,M.Ernestus,andN.Dor-
mann,“Stable-baselines3:Reliablereinforcementlearningimplementa-
tions,”Journalofmachinelearningresearch,vol.22,no.268,pp.1–8,
2021.