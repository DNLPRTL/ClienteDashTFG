2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
|     | Quality |        | of       | Experience |     |           | in  | Video |            | Streaming: |     |     |     |     |
| --- | ------- | ------ | -------- | ---------- | --- | --------- | --- | ----- | ---------- | ---------- | --- | --- | --- | --- |
|     |         | Status |          | Quo,       |     | Pitfalls, | and |       | Guidelines |            |     |     |     |     |
|     |         |        | Leonardo | Peroni     |     |           |     |       | Sergey     | Gorinsky   |     |     |     |     |
03372401.4202.15395STENSMOC/9011.01 :IOD | EEEI 4202© 00.13$/42/9-1138-3053-8-979 | )STENSMOC( SkrowTEN & smetsyS noitacinumMOC no ecnerefnoC lanoitanretnI ht61 4202
|     |     | IMDEA | Networks                  | Institute     | and | UC3M |     |     | IMDEA                     | Networks | Institute |     |     |     |
| --- | --- | ----- | ------------------------- | ------------- | --- | ---- | --- | --- | ------------------------- | -------- | --------- | --- | --- | --- |
|     |     |       |                           | Madrid, Spain |     |      |     |     | Madrid,                   |          | Spain     |     |     |     |
|     |     |       | leonardo.peroni@imdea.org |               |     |      |     |     | sergey.gorinsky@imdea.org |          |           |     |     |     |
Abstract—Quality of experience (QoE) becomes both the holy handle varying network conditions and clashing performance
grailandafree-for-allinadaptivebitrate(ABR)videostreaming.
|            |              |             |            |             |            |           | objectives. | When | the               | requested | bitrate   | is too | high,   | the chunk |
| ---------- | ------------ | ----------- | ---------- | ----------- | ---------- | --------- | ----------- | ---- | ----------------- | --------- | --------- | ------ | ------- | --------- |
| On the     | one hand,    | the design, | operation, | and         | evaluation | of ABR    |             |      |                   |           |           |        |         |           |
|            |              |             |            |             |            |           | arrives too | late | for uninterrupted |           | playback, |        | and the | resulting |
| algorithms | increasingly | rely        | on         | QoE. On the | other      | hand, QoE |             |      |                   |           |           |        |         |           |
stallofthevideoattheclientdegradesQoE.Ontheotherhand,
frequentlyreceivesonlycursoryattentioninthissupportingrole,
withmanyofitsimportantaspectstreatedwithinsufficientcare. requesting a low bitrate reduces the video quality and thereby
As a complex subjective notion, QoE is directly measurable hampers QoE too. Although the terminology and discussion
throughsubjectivetests,whichincurevidentoverhead.Whilean
|                 |     |                  |             |                      |     |              | in this paper | are       | for ABR  | streaming, |          | we consider | the      | paper’s  |
| --------------- | --- | ---------------- | ----------- | -------------------- | --- | ------------ | ------------- | --------- | -------- | ---------- | -------- | ----------- | -------- | -------- |
| objective       | QoE | model represents |             | a scalable automated |     | means for    |               |           |          |            |          |             |          |          |
|                 |     |                  |             |                      |     |              | general       | takeaways | as       | being      | relevant | to QoE      | in other | kinds of |
| QoE assessment, |     | QoE models       | proliferate | without              |     | consensus on |               |           |          |            |          |             |          |          |
|                 |     |                  |             |                      |     |              | networked     | computer  | systems. |            |          |             |          |          |
| their goodness  |     | due to numerous  |             | influence factors,   |     | construction |               |           |          |            |          |             |          |          |
methods, and usages. The model proliferation creates a false While appealing as a basis for user-centered system design,
impression that proposing a new QoE model without a proper operation, and evaluation, QoE raises a variety of practical
| validation | is acceptable. | Because   |           | the multifaceted | QoE     | problem     |                   |     |                |     |                  |            |         |       |
| ---------- | -------------- | --------- | --------- | ---------------- | ------- | ----------- | ----------------- | --- | -------------- | --- | ---------------- | ---------- | ------- | ----- |
|            |                |           |           |                  |         |             | complications.    |     | In particular, |     | QoE subjectivity |            | implies | that  |
| involves   | separable      | and often | separated | tasks            | of test | conducting, |                   |     |                |     |                  |            |         |       |
|            |                |           |           |                  |         |             | direct assessment |     | of             | QoE | involves         | subjective | tests   | where |
| model      | building,      | and model | using,    | this separation  |         | of concerns |                   |     |                |     |                  |            |         |       |
humanratersprovidescoresforexperiencespresentedtothem.
| causes | additional | complications. |     | By leveraging | two | large real |     |     |     |     |     |     |     |     |
| ------ | ---------- | -------------- | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
datasets of individual QoE perception, this paper reviews the However, lab-based subjective assessments consume signifi-
statusquoinQoE,identifiesvariouspitfalls,andoffersguidelines cant amounts of time and effort, and online crowdsourcing
| for test | conducting,    | model | building, | and model   | using, | so as     | to           |          |     |              |     |          |      |         |
| -------- | -------------- | ----- | --------- | ----------- | ------ | --------- | ------------ | -------- | --- | ------------ | --- | -------- | ---- | ------- |
|          |                |       |           |             |        |           | alternatives | mitigate |     | the overhead |     | concerns | only | to some |
| foster   | high standards | in    | future    | work on QoE | in     | ABR video |              |          |     |              |     |          |      |         |
|          |                |       |           |             |        |           | extent [6],  | [7].     |     |              |     |          |      |         |
streaming.
|       |             |            |     |            |             |         | The overhead |     | of subjective |     | tests fuels | the | emergence | and |
| ----- | ----------- | ---------- | --- | ---------- | ----------- | ------- | ------------ | --- | ------------- | --- | ----------- | --- | --------- | --- |
| Index | Terms—Video | streaming; |     | quality of | experience; | subjec- |              |     |               |     |             |     |           |     |
tive test; QoE model; scoring scale; interface design; experience wide spread of QoE models. A QoE model automatically de-
selection; value interpretability; range capping; evaluation met- rives QoE from objective influence factors (IFs), such as stall
ric; ABR algorithm.
|     |     |     |     |     |     |     | duration       | and bitrate | changes          |     | across | consecutive | chunks | [8].       |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ---------------- | --- | ------ | ----------- | ------ | ---------- |
|     |     |     |     |     |     |     | Traditionally, |             | the construction |     | of a   | QoE model   |        | presents a |
I. INTRODUCTION series of experiences to a group of raters, averages the raters’
Quality of experience (QoE) plays an important role in individual scores to compute the mean opinion score (MOS)
the design, operation, and evaluation of networked computer of each experience, and approximates QoE as a function
systems that serve humans. Qualinet, a European Cooperation mapping the considered IFs to MOS. The advantage of the
in Science and Technology Action, provides a two-sentence traditional QoE modeling is that only a relatively small group
definition for QoE [1]. This definition, endorsed by the In- ofratersparticipatesinsubjectivetestswhereastheconstructed
ternational Telecommunication Union (ITU) [2] and widely QoE model automates QoE assessment for all users of the
cited in general, distinguishes two pertinent aspects of QoE. application without imposing any subjective-test overhead on
First, QoE captures the overall satisfaction of a user with an a huge majority of them.
application as perceived by this user, i.e., QoE is a subjective Despite offering the scalable automated support for QoE
personal notion. Second, QoE depends on the user’s current assessment, QoE models spawn new difficulties. Human per-
state that has multiple dimensions, e.g., network connectivity, ception of video is complex, and many IFs of different kinds
device type, and application content. arepertinenttoQoE[9]–[13].Besides,practicalconsiderations
This paper studies QoE in adaptive bitrate (ABR) video necessitate that the IFs of a QoE model are measurable by
streaming [3], an application that heavily dominates the In- the entity that uses the QoE model, with these measurements
ternet traffic [4], [5]. The origin server of an ABR streaming being sufficiently accurate and incurring only low overhead.
session partitions the video into chunks and encodes every For example, although research indicates promise of elec-
chunk into multiple representations in the form of bitrate- troencephalographic signals as IFs of QoE [14], a streaming
resolution pairs. The ABR algorithm of each client indepen- provider is unlikely to deploy a large-scale application that
dently requests a representation for the next chunk in order to attacheselectrodestotheusers’scalps.Instead,itistypicalfor
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
558
979-8-3503-8311-9/24/$31.00 ©2024 IEEE

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
an application provider to directly measure stall duration and and arranges the advice in accordance with the classification
estimateavailablenetworkbandwidthbasedonthroughputob- of QoE-related tasks into test conducting, model building,
servations in the client. QoE models also diverge with respect and model using. In recommending the good practices for
to the approximation function that maps the considered IFs to subjectiveassessments,constructionandusageofQoEmodels,
QoE.Forinstance,closed-formexpressionsandlearning-based our overarching aspiration is to foster high standards in future
approachesarebothcommoninQoEmodeling.Consequently, work on QoE in ABR streaming. While we expect the in-
there exist a large number of diverse QoE models. creased awareness and good practices to be the most valuable
The diversity of QoE models also arises due to different for newcomers to the field, this paper serves as a wake-up
usages of the models. Timing and accuracy considerations call for the entire community to acknowledge and address the
might necessitate different models for design, operation, and identified problems.
evaluation of systems. In particular, a complex QoE model
might be suitable for offline design or evaluation but not
II. BACKGROUND
for real-time operation of an ABR algorithm. For example, QoE has its roots in quality of service (QoS), an earlier
whereas the peak signal-to-noise ratio (PSNR) [15] and video notion from packet-switched computer networking. QoS char-
multimethod assessment fusion (VMAF) [16] are metrics of acterizes network performance via such metrics as the trans-
video quality that dramatically differ in their computational mission rate, packet loss, end-to-end delay, and delay jitter
requirements, [17] relies on PSNR to predict video quality provided to applications [21]. Two main features differentiate
during live streaming and leverages VMAF to evaluate the QoE from QoS. First, QoE shifts the focus from objective
actually achieved video quality. system performance to the user’s subjective perception of the
Besides, the multifaceted QoE problem involves separable performance.Second,whileQoSisratheranumbrellatermfor
tasks such as test conducting, model building, and model us- multiple metrics, QoE constitutes a holistic concept capturing
ing. Test conducting performs subjective tests. Model building the user’s overall satisfaction with the application. The evo-
constructs QoE models based on subjective scores. Model lution from network-centered QoS to user-centered QoE not
using utilizes QoE models in system design, operation, or onlyfulfillstheinterestsandneedsofapplicationprovidersbut
evaluation. A single work might handle multiple tasks. For also is relevant to network operators. For example, a network
instance, iQoE [18] both conducts subjective assessments operator might utilize a QoE model as a basis for allocation
and constructs personalized QoE models. Sensei [19] and of link capacities to video streams [22].
Ruyi [20] address all three tasks of test conducting, model InsubjectiveQoEtestsofABRvideostreaming,anexperi-
building, and model using. ARTEMIS [17] neither builds nor ence refers to a sequence of chunks played back by the client
validatesaQoEmodelandinsteadusesanexistingQoEmodel to a rater who provides a score for the experience. When a
toevaluateitsproposalthatdynamicallyconfiguresthebitrate subjective test collects scores for a series of experiences to
ladder of a live ABR streaming session. The separation of support construction of a QoE model, the test also records
concernsindealingwithQoEhasbothpositivesandnegatives. the IF values of each rated experience. To keep the load on
On the one hand, the focus on a single task enables its more the raters manageable, the series of experiences should be
thorough execution. On the other hand, the limited outlook relatively short. [23], [24], [25], and, to a smaller extent, [26]
might derail the overall effort, e.g., when an ABR algorithm select the experiences and their IF values to be representative
uses a QoE model validated for dissimilar settings. of real-world settings.
The importance, complexity, and separation of concerns Thescoringscaleisanimportantelementofsubjectivetest-
put QoE in a precarious position. The widely recognized ing methodologies, including those standardized by ITU [27].
importance of QoE creates expectations to consider QoE in For instance, absolute category rating (ACR) is a popular
ABR video streaming, at least for evaluation if not for design method with a five-level scale where integers from 1 to 5
and operation. However, QoE complexity makes comprehen- constitute bad, poor, fair, good, and excellent levels [28].
sive treatment of QoE difficult. Furthermore, the diversity of Another common scale consists of 100 levels where level
existing QoE models creates a false impression that one may ranges 1-20, 21-40, 41-60, 61-80, and 81-100 correspond to
easilyintroduceanewQoEmodelwithoutapropervalidation. bad, poor, fair, good, and excellent QoE, respectively [18],
Hence, QoE becomes both the holy grail and a free-for-all. [23], [24], [29]. While such discrete absolute scales are the
In this paper, we review the current landscape of QoE in most typical, alternative testing methods employ continuous
ABR video streaming and zoom in on a number of areas scales for scoring an experience, assess QoE degradation
including: (a) scoring scale, interface design, and experi- rather than QoE itself, or perform pairwise comparison of
ence selection for subjective tests, (b) validation, value inter- experiences [27], [30]. According to [31] and [32], usage of
pretability, and capping of the value range in QoE modeling, continuousvs.discretescalesresultsinnosignificantstatistical
(c)mismatchbetweenusageandconstructionofQoEmodels, differences in QoE assessment.
(d)evaluationofQoEmodelsviacorrelationvs.errormetrics, Building a QoE model based on the experiences’ scores
and (e) QoE evaluation of ABR algorithms. We identify and IF values has many methods of different kinds at its
problems afflicting these areas and offer advice on how to disposal. Although classification techniques seem a natural
rectify the situation. Our methodology leverages real data fit for modeling of discrete QoE scores, regression methods
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore. Restrictions apply.
559

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
dominateQoEmodeling.Inthispaper,weconsider10existing secnerrucco fo % 7 secnerrucco fo % 7
|     |     |     |     |     |     |     |     | 6   |     |     | 6   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
QoE models and, for brevity, refer to them with the following 5 5
|               |         |     |         |         |         |       |         | 4   |     |     | 4   |     |     |
| ------------- | ------- | --- | ------- | ------- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
| single-letter | labels: | B   | [33], G | [34], R | [35], S | [36], | V [37], |     |     |     |     |     |     |
|               |         |     |         |         |         |       |         | 3   |     |     | 3   |     |     |
N [38], F [39], A [40], P [41], and L [42]. The first six of 2 2
|                                                       |     |     |     |     |     |     |     | 1                       |     |     | 1                       |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ----------------------- | --- | --- |
| theseQoEmodelsrelyonregressionwithsimilarlineartarget |     |     |     |     |     |     |     | 0                       |     |     | 0                       |     |     |
|                                                       |     |     |     |     |     |     |     | 1 102030405060708090100 |     |     | 1 102030405060708090100 |     |     |
functions and account for video quality with a different IF. Score Score
|            |          |     |     |       |                   |     |     | (a) Waterloo-IV |     | HDTV |     | (b) | iQoE |
| ---------- | -------- | --- | --- | ----- | ----------------- | --- | --- | --------------- | --- | ---- | --- | --- | ---- |
| The target | function | of  | QoE | model | F is exponential. |     | The |                 |     |      |     |     |      |
construction of QoE models A, P, and L relies on machine Fig. 1: Distributions of the individual scores in the datasets.
| learning    | and, specifically |         | and | respectively,   | on  | support | vector |     |     |     |     |     |     |
| ----------- | ----------------- | ------- | --- | --------------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
| regression, | random            | forest, | and | long short-term |     | memory. |        |     |     |     |     |     |     |
When constructed, a QoE model avails itself to various to the five-level ACR scale, the 1-100 scale gives the raters
|          |        |         |            |     |             |     |      | an opportunity | to  | express | their QoE perception |     | with a finer |
| -------- | ------ | ------- | ---------- | --- | ----------- | --- | ---- | -------------- | --- | ------- | -------------------- | --- | ------------ |
| usage in | system | design, | operation, | and | evaluation. | MPC | [33] |                |     |         |                      |     |              |
makes ABR decisions via model predictive control based on granularity, which might make the QoE assessment more
QoE model B (as labeled above). Pensieve [43] is an ABR accurate. On the other hand, the 100 levels increase the
|     |     |     |     |     |     |     |     | raters’ uncertainty |     | about which | specific | level | to choose, and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | -------- | ----- | -------------- |
algorithmthatusesQoEmodelBastheoptimizationobjective
inactor-criticreinforcementlearning.AlthoughBBA[44]and the increased cognitive load on the raters might degrade the
|                |     |      |         |          |        |           |     | assessment | accuracy | due to | hasty or careless |     | decisions. |
| -------------- | --- | ---- | ------- | -------- | ------ | --------- | --- | ---------- | -------- | ------ | ----------------- | --- | ---------- |
| ThroughputRule |     | (TR) | [45] do | not rely | on any | QoE model |     | in         |          |        |                   |     |            |
their design or operation, usage of QoE models to evaluate To analyze how the number of scale levels affects QoE
QoEperformanceofsuchABRalgorithmsiscommonaswell. rating, we consider the distributions of individual scores in
|     |     |      |             |     |     |     |     | the Waterloo-IV |     | and iQoE | datasets. Because |     | the experiences |
| --- | --- | ---- | ----------- | --- | --- | --- | --- | --------------- | --- | -------- | ----------------- | --- | --------------- |
|     |     | III. | METHODOLOGY |     |     |     |     |                 |     |          |                   |     |                 |
chosenbythedatasetsdeliberatelycovertheentire1-100scale
The nine subsequent sections identify and examine prob- to support construction of accurate QoE models, we expect
lems in dealing with QoE by progressively covering the tasks the popularity of the individual scores across the scale to
of test conducting, model building, and model using. In the be smooth if not uniform. With the uniform distribution, the
|          |         |            |                  |     |         |      |      | popularity | of each | score would | be 1%. |     |     |
| -------- | ------- | ---------- | ---------------- | --- | ------- | ---- | ---- | ---------- | ------- | ----------- | ------ | --- | --- |
| process, | we cite | additional | problem-specific |     | related | work | and, |            |         |             |        |     |     |
when needed, utilize the aforementioned QoE models and For the 32 HDTV raters of the Waterloo-IV dataset, Fig-
ABR algorithms. The analysis in each of these sections offers ure 1a depicts the distribution of the score popularity that is
advice on addressing the examined problem. Because our neither uniform nor close to being smooth. Instead, there is a
analyses heavily leverage two large real datasets of QoE small number of scores that spike in popularity compared to
theadjacentscores.Inparticular,thescoreof50dominatesby
| perception | by individual |     | raters | on the | 1-100 scoring | scale, | we  |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------ | ------ | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
now describe these Waterloo-IV and iQoE datasets in more grabbing6.37%ofallscoreoccurrencesandapparentlydraw-
detail. ing attention to itself at the expense of the other scores in the
Waterloo-IV [46] is a dataset with 43,650 individual scores 41-59range.Thenextninepopularscores,indecreasingorder
from lab experiments with 92 raters aged between 18 and of popularity, are 100, 70, 80, 75, 60, 65, 85, 90, and 40 that
|          |           |     |         |       |            |       |        | capture 4.30%, | 3.55%, | 3.14%, | 3.07%, | 2.77%, | 2.70%, 2.69%, |
| -------- | --------- | --- | ------- | ----- | ---------- | ----- | ------ | -------------- | ------ | ------ | ------ | ------ | ------------- |
| 38 years | old, with | 29, | 32, and | 31 of | the raters | using | phone, |                |        |        |        |        |               |
high definition television (HDTV), and ultra HDTV devices, 2.49%, and 2.05% of all score occurrences, respectively. The
respectively. The presented experiences span all combinations results suggest that, in agreement with prototype theory [49],
of two codecs, nine network traces, and five ABR algorithms. the raters form their own new categories of scores where the
13IFscharacterizeeverychunk,whichhasthedurationof4s. prototype of each category is either a score divisible by five
Each experience consists of seven chunks, i.e., the playback or the lowest score of 1. When presented with an experience,
of an experience without stalls takes 28 s. a rater determines a matching new category and reports the
iQoE [47] refers to a dataset with 14,400 individual scores category prototype as the score for the experience.
from online subjective tests with 120 raters aged between 20 Figure 1b plots the 14,400 individual scores in the iQoE
and63yearsold.Amongtheraterswhodisclosetheirviewing dataset. Despite conducting the tests in online rather than lab
device, six and 110 raters claim using a phone and personal settings, the qualitative results are remarkably consistent with
computer, respectively. The iQoE dataset contains 1,000 ex- those for Waterloo-IV. A small number of prototype scores
periences generated via simulations in Park [48] by utilizing gain disproportional attention, spiking high above the nearby
one codec, 102 network traces, and three ABR algorithms. scores.Thescoresof50and100standoutagainbyattracting
Eachexperiencecontainsfourchunkscharacterizedby10IFs. 5.49% and 5.58% of all score occurrences, respectively. The
Becausethechunkdurationissetto2s,eachexperienceplays other five scores exceeding the popularity threshold of 2%
back for 8 s without stalls. are 70, 80, 60, 40, and 90, with them getting 2.67%, 2.66%,
|     |     |     |     |     |     |     |     | 2.57%, 2.42%, | and | 2.10% | of all score | occurrences, | respec- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ------------ | ------------ | ------- |
IV. SCORINGSCALEINSUBJECTIVEASSESSMENTS
|     |     |     |     |     |     |     |     | tively. The | next | four scores | in order of | decreasing | popularity |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------- | ----------- | ---------- | ---------- |
Conducting a subjective test involves selecting a scale for are 65, 85, 95, and 75. Similarly to the findings for Waterloo-
scoring of experiences. The Waterloo-IV and iQoE datasets IV, scores divisible by five emerge as the prototypes of the
described in Section III employ the 1-100 scale. Compared score categories newly formed by the raters.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
560

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
| Our analyses | indicate |     | that 100 | levels | are clearly | excessive |     |     |                           |     |     |     |                         |     |     |
| ------------ | -------- | --- | -------- | ------ | ----------- | --------- | --- | --- | ------------------------- | --- | --- | --- | ----------------------- | --- | --- |
|              |          |     |          |        |             |           |     |     | Realistic IF distribution |     |     |     | Uniform IF distribution |     |     |
for subjective assessment of QoE in ABR streaming, at least 0.20 0.30
0.25
by the factor of five given the popularity of scores divisible ytisneD 0.15 ytisneD
0.20
by five. Raters’ responses in the iQoE post-assessment survey 0.10 0.15
0.10
0.05
support this sentiment. Hence, we align our recommendation 0.05
|     |     |     |     |     |     |     |     | 0.00 |     |     |     | 0.00 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- |
on the scoring scale with the perspective in [31], [32] that 1 2 3 4 5 6 7 8 910111213 0 1 2 3 4 5
|     |     |     |     |     |     |     |     |     | Representation index |     |     |     |     | Stall duration, s |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | ----------------- | --- |
a small number of levels, e.g., five in the ACR scale, are (a) Representation index (b) Stall duration
| sufficient | for efficient | accurate | characterization |     |     | of QoE: |     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | -------- | ---------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Test conducting) Use a scoring scale with a small number Fig.2:Realistic,aspertheiQoEdataset,anduniformselection
|            |         |                |     |        |     |     |     | of IF values | for | tested | experiences. |     |     |     |     |
| ---------- | ------- | -------------- | --- | ------ | --- | --- | --- | ------------ | --- | ------ | ------------ | --- | --- | --- | --- |
| of levels, | such as | the five-level | ACR | scale. |     |     |     |              |     |        |              |     |     |     |     |
V. INTERFACEDESIGNFORSUBJECTIVEASSESSMENTS
|     |     |     |     |     |     |     |     | To examine | experience |     | selection, |     | we utilize | the | iQoE set |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------- | --- | ---------- | --- | -------- |
Theprominencegainedbyscore50intheWaterloo-IVand
iQoE datasets deserves a separate discussion. 50 is by far the of the 1,000 experiences generated through simulations on
|              |       |     |            |     |           |              |     | real network | traces | with | three | ABR | algorithms |     | and a bi- |
| ------------ | ----- | --- | ---------- | --- | --------- | ------------ | --- | ------------ | ------ | ---- | ----- | --- | ---------- | --- | --------- |
| most popular | score | in  | comparison | to  | all other | intermediate |     |              |        |      |       |     |            |     |           |
scores on the 1-100 scale in Figure 1. In the iQoE dataset, trate ladder comprising 13 representations indexed from 1
this outcome might arise partly due to score 50 constituting, to 13. Representation 1 has bitrate 235 Kbps and resolution
|           |        |             |     |         |          |        |        | 320×180. | The bitrate |     | and resolution |     | in representation |     | 13 are |
| --------- | ------ | ----------- | --- | ------- | -------- | ------ | ------ | -------- | ----------- | --- | -------------- | --- | ----------------- | --- | ------ |
| as Figure | 14b in | [18] shows, | the | initial | position | of the | handle |          |             |     |                |     |                   |     |        |
on the slider in each iQoE assessment. Because keeping the 16,800 Kbps and 3,840×2,160, respectively. Figure 2a shows
|     |     |     |     |     |     |     |     | that representations |     | 1,  | 5, and | 13 are | the most | frequent, | with |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------ | ------ | -------- | --------- | ---- |
handleintheinitialpositionbeforesubmittingthescoreof50
is effortless, and the effort to change the score by dragging each of them taking in this realistic experience set a larger
the handle from 50 to 51, 60, or 61 is about the same and share than 15%. Representations 8 through 11 are the least
|                 |     |       |         |          |            |            |     | frequent, | with | their individual |     | shares | in  | the experience | set |
| --------------- | --- | ----- | ------- | -------- | ---------- | ---------- | --- | --------- | ---- | ---------------- | --- | ------ | --- | -------------- | --- |
| not negligible, | it  | seems | logical | that the | popularity | difference |     |           |      |                  |     |        |     |                |     |
between scores 50 and 51 compared to scores 60 and 61 falling below 3%. The plot contrasts this realistic distribution
|                  |         |          |     |         |        |             |     | with the | randomly | uniform |     | sampling | of  | the representation |     |
| ---------------- | ------- | -------- | --- | ------- | ------ | ----------- | --- | -------- | -------- | ------- | --- | -------- | --- | ------------------ | --- |
| is significantly | larger. | Although |     | another | likely | contributor |     | to       |          |         |     |          |     |                    |     |
the dominance of intermediate score 50 is its central role index between 1 and 13. Figure 2a clearly illustrates that the
on the 1-100 scale as the middle point in the ternary QoE randomly uniform selection of values for the representation
|             |         |     |         |        |      |          |     | index gives | unrealistically |     | high | attention | to  | unpopular | repre- |
| ----------- | ------- | --- | ------- | ------ | ---- | -------- | --- | ----------- | --------------- | --- | ---- | --------- | --- | --------- | ------ |
| perspective | between | the | extreme | scores | of 1 | and 100, | our |             |                 |     |      |           |     |           |        |
previous observation highlights the importance of designing sentations 8 through 11 and unrealistically low attention to
|     |     |     |     |     |     |     |     | popular | representations |     | 1, 5, | and 13. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ----- | ------- | --- | --- | --- |
anunbiasedinterfaceforsubjectivetests,e.g.,byrandomizing
the initial position of the handle on the slider in different WechangetheIFofinteresttostalldurationandcompareits
assessments: realistic value distribution in the iQoE experience set against
|       |             |        |     |          |           |     |      | the randomly | uniform |     | sampling | of  | stall duration |     | between 0 |
| ----- | ----------- | ------ | --- | -------- | --------- | --- | ---- | ------------ | ------- | --- | -------- | --- | -------------- | --- | --------- |
| (Test | conducting) | Design | an  | unbiased | interface | for | sub- |              |         |     |          |     |                |     |           |
jective assessments, e.g., a randomized initial position of the and 5 s. Figure 2b plots kernel density estimates for the
slider handle. two alternatives. In the realistic distribution, stall duration
|     |     |     |     |     |     |     |     | is predominantly |     | below | 0.5 | s and | rarely | exceeds | 2 s. Thus, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | --- | ----- | ------ | ------- | ---------- |
VI. EXPERIENCESELECTIONFORSUBJECTIVETESTS
|     |         |               |       |         |               |     |     | the uniform | selection | of            | values | for       | stall duration | substantially |     |
| --- | ------- | ------------- | ----- | ------- | ------------- | --- | --- | ----------- | --------- | ------------- | ------ | --------- | -------------- | ------------- | --- |
|     |         |               |       |         |               |     |     | exaggerates | the       | real stalling |        | behavior. |                |               |     |
| The | outcome | of subjective | tests | depends | significantly |     | on  |             |           |               |        |           |                |               |     |
the experiences presented to the raters and, in particular, on The above analysis illustrates that uniform and other sim-
the IF values of these experiences. Hence, the choice of the plistic approaches to experience selection are unrealistic,
tested experiences and their IF values is an important task. therebyendangeringthevalidityofconductedsubjectivetests.
However, the following three circumstances complicate the Thus, we give the following advice:
task.First,multipleIFscharacterizeanexperience.Second,an (Test conducting) Realistically select experiences for sub-
IFmighthavemanypotentialvalues,e.g.,stalldurationspread jective tests and, in particular, with respect to the IF values
between0and5s.Third,arateriscapableofevaluatingonly across the tested experiences.
| a relatively | short           | series | of experiences. |           |                |     |      |     |     |     |     |     |     |     |     |
| ------------ | --------------- | ------ | --------------- | --------- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| Despite      | the importance, |        | the             | selection | of experiences |     | rou- |     |     |     |     |     |     |     |     |
VII. VALIDATIONOFQOEMODELS
| tinely lacks | in sufficient |     | care. | Specifically, | it  | is common |     | to  |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | ----- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
select values for an IF across the experience series in a Sections IV, V, and VI demonstrate that subjective tests
simplistic manner, such as by drawing the values uniformly require a substantial amount of thoughtfulness in their setup
or randomly from the range of the IF’s possible values. While inordertoappropriatelycollectscoresneededforconstructing
choosing the values for stall duration and frequency in the a QoE model. On the other hand, a QoE model in ABR
randomly uniform fashion, [30] employs other ad-hoc rules streaming is rarely a goal in itself and instead receives an
for video quality. [50] and [51] adopt similar approaches for auxiliary role in the design, operation, or evaluation of ABR
their IFs of video quality and stalling. [52] restricts stalling to algorithms.ThismightbeareasonwhyvariousQoEmodeling
either beginning or middle of experiences. effortsareinsufficientlycareful.Itisnotuncommontopropose
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
561

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
aQoEmodelbasedonabstractconsiderationswithoutaproper
|                                                 |             |     |     |     |     |     | 100    |     |     |     | 100    |     |     |
| ----------------------------------------------- | ----------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------ | --- | --- |
|                                                 |             |     |     |     |     |     | 80     |     |     |     | 80     |     |     |
| experimental                                    | validation. |     |     |     |     |     |        |     |     |     |        |     |     |
|                                                 |             |     |     |     |     |     | SOM 60 |     |     |     | SOM 60 |     |     |
| QoEmodelB[33]isaprominentexampleofthevalidation |             |     |     |     |     |     | 40     |     |     |     | 40     |     |     |
concern. The model employs a linear approximation function 20 20
|     |     |     |     |     |     |     | 1   |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and combines four IFs as a weighted sum with predefined 100 200 300 400 100 200 300 400
|                    |      |            |          |           |          |                |     |              | PSNR sum       |     |           | PSNR sum |      |
| ------------------ | ---- | ---------- | -------- | --------- | -------- | -------------- | --- | ------------ | -------------- | --- | --------- | -------- | ---- |
| weight values.     | [33] | introduces |          | QoE model | B        | without con-   |     |              |                |     |           |          |      |
|                    |      |            |          |           |          |                | (a) | Construction | on Waterloo-IV |     | (b) Usage | on iQoE  | data |
| ducting subjective |      | tests      | and does | not       | validate | its choices of |     |              |                |     |           |          |      |
the linear function and specific IFs. A simple experiment Fig. 3: A regression-based QoE model: (a) values beyond the
only illustrates how three sets of weight values affect the scale and (b) mismatch between usage and construction.
| QoE value    | produced    | by  | the      | model. Because |           | [33] and [43] |      |      |              |          |           |          |       |
| ------------ | ----------- | --- | -------- | -------------- | --------- | ------------- | ---- | ---- | ------------ | -------- | --------- | -------- | ----- |
| leverage QoE | model       | B   | in their | respective     | MPC       | and Pensieve  |      |      |              |          |           |          |       |
|              |             |     |          |                |           |               | even | when | the absolute | increase | is within | the JND, | i.e., |
| algorithms,  | the success |     | of these | pioneering     | QoE-based | ABR           |      |      |              |          |           |          |       |
algorithms heightens attention to this QoE model and inspires meaninglessly small.
numerous attempts to improve it. The improvements by QoE Our discussion in this section highlights dangers of seg-
models G [34], R [35], S [36], V [37], and N [38] primarily regating a constructed QoE model from subjective, humanly
target the usage of the bitrate as a proxy of video quality in interpretable perception of QoE. Hence, we argue for QoE
QoE model B. For example, instead of the bitrate, PSNR and models that support interpretation of their values. Apart from
VMAF characterize video quality in QoE models R and V, the advantages for QoE evaluation of ABR algorithms, the
respectively. However, the above extensions of QoE model B valueinterpretabilityequipsQoEmodelswithotherstrengths,
neitherquestionnorvalidateitsmajorunderlyingassumptions, e.g., their direct applicability as synthetic raters [18]. Besides,
such as the linearity of its approximation function. wecontendthatthevaluesproducedbytheQoEmodelshould
The existence of the prominent family of QoE models that be positive numbers so as to facilitate their mathematical
lack a proper validation leads us to dual recommendations treatment, including meaningful relative comparisons. While
which are both obvious and unfortunately relevant: both desired properties hold for the range of QoE values
alignedwiththefive-levelACRscale,weadvisethefollowing:
| (Model | building) | When | proposing | a   | QoE model, | validate | it  |     |     |     |     |     |     |
| ------ | --------- | ---- | --------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
through subjective tests. (Modelbuilding)ConstructaQoEmodelproducingpositive
(Model using) Use validated QoE models only. interpretablevalues,e.g.,intherangeconsistentwiththefive-
|       |                                  |     |     |     |     |     | level | ACR scale. |     |     |     |     |     |
| ----- | -------------------------------- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
| VIII. | VALUEINTERPRETABILITYOFQOEMODELS |     |     |     |     |     |       |            |     |     |     |     |     |
Lacking validation of a QoE model might have another IX. CAPPINGOFTHEVALUERANGE
| negative side | effect | of  | the model | values | losing | their inter- |     |     |     |     |     |     |     |
| ------------- | ------ | --- | --------- | ------ | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
pretability. Due to the separation from subjective tests and Whereas Sections VII and VIII expose general problems in
theirscoringscale,theQoEmodelislikelytoyieldvaluesthat the construction of QoE models, we now examine specific
defy interpretation by humans. For example, while Figures 8 technical reasons why these problems arise. Even when a
through15in[43]evaluatedifferentABRalgorithmsviathree QoE model aspires to align its value range with a humanly
variantsofQoEmodelB,thevaluesproducedbytheQoE lin interpretable scale, the common reliance on unconstrained re-
andQoE hdvariantsrangefrom−0.5to3andfrom−1to15, gressiondoesnotassuresuchalignment,includingonthedata
respectively, and it remains unclear how these two empirical used to train the regression. We consider the 450 experiences
value ranges relate to the bad, poor, fair, good, and excellent assessed by the 32 HDTV raters in Waterloo-IV and retain
levels of the common scoring scales. onlytheexperiencesdevoidofstalling.Foreaseofexposition,
The disconnection of QoE values from their interpretation we characterize each of the remaining 326 experiences with
also undermines their utility for comparison of different ABR a PSNR sum, a new single IF calculated as the sum of the
|     |     |     |     |     |     |     | PSNR | values | across all | seven | chunks in | the experience. |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ---------- | ----- | --------- | --------------- | --- |
algorithms.AlthoughhighervaluesproducedbyaQoEmodel
typically indicate better quality of experience, the lacking Figure3apresentsascatterplotofthePSNRsumandMOS
interpretability of QoE values translates into lacking inter- for the 326 experiences as blue dots. The graph also depicts
pretabilityoftheirdifferences,e.g.,ofwhetheraQoEincrease as a red line a QoE model constructed on this data via linear
with a new ABR algorithm is not meaningful due to falling regression with the least squares fitting. The solid portion of
withinthejust-noticeabledifference(JND),i.e.,themaximum the line represents the QoE values between 1 and 100, i.e.,
difference imperceptible by a human [53]. within the 1-100 scoring scale of Waterloo-IV. The respective
The above problematic example of QoE model B and its range of the PSNR sum is from 108 to 388. However, four
variants that produce both negative and positive values calls experiences in the training data have a larger PSNR sum than
for a word of caution about reporting only relative changes 388,andtheQoEmodelreturns100.1,102.3,102.3,and104.6
in QoE. Consider an ABR algorithm achieving a positive astheQoEvaluesforthesefourexperiences.Thus,duetothe
QoE value which lies arbitrarily close to zero. If another reliance on the unconstrained regression, the constructed QoE
ABR algorithm surpasses this QoE value by a small amount, model produces values beyond the targeted scale even on the
| the relative | QoE increase |     | might | be 100%, | 1,000%, | or higher | training | dataset. |     |     |     |     |     |
| ------------ | ------------ | --- | ----- | -------- | ------- | --------- | -------- | -------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
562

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
A simple way for a regression-based QoE model to address For instance, [6] and [61] use QoE model P in settings that
the problem of unconstrained regression is to cap the regres- differ from those explicitly assumed in its construction, such
sion output to an intended range of values. For example, [6], as experiences that last less than a minute or contain more
[35], and [54] apply capping to prevent negative values, with than five stalling events.
[6] and QoE model R [35] imposing the nonnegative limit on The mismatch problem becomes graver because many QoE
the outputs of Petrangeli model [55] and QoE model B [33], modelsdonotdescribetheirconstructionsettingsfully,clearly,
respectively.[56]and[57]alignQoEvalueswiththefive-level or at all. For example, QoE models P [41] and L [42]
ACR scale by restraining the values to the range from 1.05 do not publicly release their training modules. Furthermore,
to 4.9 for QoE model P and various models from [40], [52], [42] trains QoE model L on three datasets and only vaguely
[58], [59], respectively. describes the roles played by two of them in the training.
An alternative to the output capping is to use an approxi- Similarly,[55]leavestheconstructionsettingsofitsPetrangeli
mation function with built-in adherence to the intended value model unclear by simply referring to [54] and [62]. Thus,
range. For instance, QoE model L [42] utilizes a hyperbolic even an entity willing to use QoE models appropriately might
tangentfunctiontoguaranteevalueswithintherangebetween be unable to do so because the models do not disclose their
−1and1andthenlinearlytransformstheguaranteedrangeto construction settings.
matchthefive-levelACRscale.[39]configurestheexponential We suggest addressing the problem by quenching its fun-
| function of | QoE model | F   | so that the regression | always | yields |                  |          |                   |             |
| ----------- | --------- | --- | ---------------------- | ------ | ------ | ---------------- | -------- | ----------------- | ----------- |
|             |           |     |                        |        |        | damental source, | i.e., by | using a QoE model | in settings |
values between 1 and 5. [18] creates synthetic raters by covered during its construction. Although there are alternative
| adopting a | sigmoid | function | that assuredly | produces | values |     |     |     |     |
| ---------- | ------- | -------- | -------------- | -------- | ------ | --- | --- | --- | --- |
heuristics,suchasextrapolationornormalizationofIFvalues,
between 1 and 100. [60] guarantees QoE values between 0 these heuristics rely on simplifying assumptions and have ad
and 100 by using a sigmoid function as well. hoc applicability. The following dual advice promotes the
| While not | advocating | a   | specific method | for ensuring | that |                     |           |     |     |
| --------- | ---------- | --- | --------------- | ------------ | ---- | ------------------- | --------- | --- | --- |
|           |            |     |                 |              |      | general fundamental | solution: |     |     |
a QoE model produces values within the targeted range, we (Modelbuilding)AnnotatetheproposedQoEmodelwithits
| view such | assurances | as important | for | the interpretability | of  |              |           |     |     |
| --------- | ---------- | ------------ | --- | -------------------- | --- | ------------ | --------- | --- | --- |
|           |            |              |     |                      |     | construction | settings. |     |     |
the QoE model and make the following recommendation: (Model using) Restrict the usage of QoE models to their
| (Model         | building) | Construct | a QoE         | model that | assuredly |                        |           |     |     |
| -------------- | --------- | --------- | ------------- | ---------- | --------- | ---------------------- | --------- | --- | --- |
|                |           |           |               |            |           | annotated construction | settings. |     |     |
| returns values | in the    | intended  | interpretable | range.     |           |                        |           |     |     |
X. MISMATCHBETWEENUSAGEANDCONSTRUCTION XI. CORRELATIONVS.ERROR
|             |     |        |             |             |       | Evaluation | of QoE models | commonly utilizes | metrics of |
| ----------- | --- | ------ | ----------- | ----------- | ----- | ---------- | ------------- | ----------------- | ---------- |
| Restricting | the | values | produced by | a QoE model | to an |            |               |                   |            |
intendedrangedoesnotensuretheirmeaningfulinterpretation. correlation or error. Both kinds of metrics characterize the
Figure 3b enhances Figure 3a by adding a scatter plot of the relationship between the ground-truth subjective scores and
PSNRsumandMOSforthe43stalling-freeiQoEexperiences values produced by a QoE model. Quantifying the strength
asgreendots,wherethePSNRsumagainreferstothesumof and direction of the relationship between these two variables,
thePSNRvaluesacrossallchunksintheexperience.However, the correlation metrics include Pearson linear correlation co-
unlikeWaterloo-IVwithitsseven-chunkexperiences,theiQoE efficient (PLCC) and Spearman rank correlation coefficient
dataset composes its experiences from four chunks, and the (SRCC), which deal with the two variables’ values and their
PSNRsumacrossthe43stalling-freeiQoEexperiencesvaries ranks, respectively. Both PLCC and SRCC vary from −1
from 67 to 119. Consequently, the linear QoE model trained (perfect negative relationship) through 0 (no relationship) to
ontheWaterloo-IVdata,i.e.,theredlineinFigure3b,returns 1 (perfect positive relationship). On the other hand, mean
values within the intended 1-100 range for only four of the absolute error (MAE) and root-mean-square error (RMSE)
43 experiences. These QoE values are 1.7, 3.8, 4.0, and 4.1, are metrics of error in regression problems and measure
|     |     |     |     |     |     | differences between | the subjective | scores and | values returned |
| --- | --- | --- | --- | --- | --- | ------------------- | -------------- | ---------- | --------------- |
clusteringatthebottomoftherange.Theother39experiences
receive QoE values smaller than 1 and as low as −14.4. Even bytheQoEmodel.WhileMAEtreatsallindividualdifferences
with the regression output capped from below by 1, the QoE equally, RMSE assigns larger weights to larger differences.
model characterizes the 43 experiences with values between Similarly to Section IX, we utilize the 326 stalling-free
1 and 4.1, which is meaninglessly low because the iQoE Waterloo-IV experiences assessed by the 32 HDTV raters.
dataset carefully assembles experiences to cover the entire This time, the only IF is the mean VMAF computed as the
QoE spectrum from bad to excellent levels. average of the VMAF values across all seven chunks in the
The observed problem occurs due to the different settings experience. We apply the Nelder-Mead method [63] to build
duringtheusageandconstructionoftheQoEmodel.Whilethe three regression-based QoE models that employ logarithmic,
training Waterloo-IV data contains seven-chunk experiences linear,andquadraticapproximationfunctions.Specificallyand
with the PSNR sum ranging from 200 to 401, the testing respectively for the logarithmic, linear, and quadratic QoE
iQoE data employs four-chunk experiences with the PSNR models, we aim to minimize MAE, minimize RMSE, and
sum varying from 67 to 119. Unfortunately, the mismatch maximize PLCC with (0, 0), (0, 0), and (2, 2, 1) as the initial
| betweentheusageandconstructionsettingsisnotuncommon. |     |     |     |     |     | simplex. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
563

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
|     |     |             |     |        |     |           |     |     | TABLE           | II: Average | QoE     | performance | of           | ABR algorithms | on      |
| --- | --- | ----------- | --- | ------ | --- | --------- | --- | --- | --------------- | ----------- | ------- | ----------- | ------------ | -------------- | ------- |
|     |     | Logarithmic |     | Linear |     | Quadratic |     |     |                 |             |         |             |              |                |         |
|     |     |             |     |        |     |           |     |     | the Waterloo-IV |             | dataset | according   | to different | QoE            | models. |
| 100 |     |             |     |        | 100 |           |     |     |                 |             |         |             |              |                |         |
|     | 80  |             |     |        | 80  |           |     |     |                 |             |         |             |              |                |         |
|     |     |             |     |        |     |           |     |     |                 | B           | G R     | S V         | N            | F A            | P L     |
| SOM | 60  |             |     | SOM    | 60  |           |     |     |                 |             |         |             |              |                |         |
40 40 Pensieve 37.5859.2262.9561.9354.6054.6066.4858.033.133.97
|              | 20        |              |               |             | 20          |                  |                |       | MPC            | 58.9171.1766.0766.5667.6467.6463.8169.313.933.00 |                |                  |                 |                    |           |
| ------------ | --------- | ------------ | ------------- | ----------- | ----------- | ---------------- | -------------- | ----- | -------------- | ------------------------------------------------ | -------------- | ---------------- | --------------- | ------------------ | --------- |
|              | 1         |              |               |             | 1           |                  |                |       | BBA            | 58.9273.9264.7964.9767.7167.7166.5466.923.464.73 |                |                  |                 |                    |           |
|              | 20        | 40 60        | 80            | 100         | 17.5        | 20.0             | 22.5 25.0 27.5 | 30.0  |                |                                                  |                |                  |                 |                    |           |
|              |           | Mean VMAF    |               |             |             |                  | Mean PSNR      |       |                |                                                  |                |                  |                 |                    |           |
|              |           |              |               |             |             |                  |                |       | TR             | 53.6263.7467.9068.7469.0469.0466.1769.443.883.32 |                |                  |                 |                    |           |
|              | (a) On    | Waterloo-IV  | data          |             |             | (b) On           | iQoE data      |       |                |                                                  |                |                  |                 |                    |           |
|              |           |              |               |             |             |                  |                |       | Increase,%     | 0.02                                             | 3.86 2.77      | 3.28 1.96        | 1.96            | 0.09 0.19 1.2919.1 |           |
| Fig.         | 4: Three  | QoE          | models        | constructed |             | via logarithmic, | linear,        |       |                |                                                  |                |                  |                 |                    |           |
| and          | quadratic | regressions. |               |             |             |                  |                |       |                |                                                  |                |                  |                 |                    |           |
|              |           |              |               |             |             |                  |                |       | Although       | the                                              | above analyses | on               | the Waterloo-IV | and                | iQoE      |
|              |           |              |               |             |             |                  |                |       | data indicate  | that                                             | error          | and correlation  |                 | metrics,           | including |
| TABLE        | I:        | MAE, RMSE,   |               | and PLCC    | performance |                  | of the         | three |                |                                                  |                |                  |                 |                    |           |
|              |           |              |               |             |             |                  |                |       | their MAE,     | RMSE,                                            | and            | PLCC varieties,  |                 | are important      | due       |
| logarithmic, |           | linear,      | and quadratic |             | QoE         | models.          |                |       |                |                                                  |                |                  |                 |                    |           |
|              |           |              |               |             |             |                  |                |       | to quantifying | different                                        |                | relevant aspects | of              | QoE models,        | it is     |
(a) On Waterloo-IV data (b) On iQoE data not unusual for evaluations to omit some of the metrics. For
example,[37],[59],and[64]considercorrelationmetricsonly.
|     | Logarithmic |     | Linear Quadr. |     |     | Logarithmic | Linear | Quadr. |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------------- | --- | --- | ----------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
While[30],[57],and[65]ignoreMAE,[52]excludesRMSE.
| MAE  |     | 14.8 | 15.4 | 26.9      | MAE | 13.4 | 13.3 | 17.2 |                |     |              |      |      |           |     |
| ---- | --- | ---- | ---- | --------- | --- | ---- | ---- | ---- | -------------- | --- | ------------ | ---- | ---- | --------- | --- |
|      |     |      |      |           |     |      |      |      | The evaluation | in  | [42] employs | only | PLCC | and RMSE. |     |
| RMSE |     | 20.5 | 19.5 | 30.2 RMSE |     | 15.8 | 15.9 | 20.7 |                |     |              |      |      |           |     |
Onthequestionwhichmetricstouse,wecallfordiversityof
| PLCC |     | 0.053 | 0.105 0.115 |     | PLCC | 0.108 | 0.103 | 0.112 |               |     |          |                    |     |            |         |
| ---- | --- | ----- | ----------- | --- | ---- | ----- | ----- | ----- | ------------- | --- | -------- | ------------------ | --- | ---------- | ------- |
|      |     |       |             |     |      |       |       |       | perspectives. | In  | spite of | existing arguments |     | that error | metrics |
aresuperiortocorrelationmetricsintheirutilityforevaluation
Figure 4a depicts the three QoE models along with their and understanding of QoE models [29], our position is that
training Waterloo-IV data. All three models perform identi- metrics of both types are pertinent because of their potential
cally with respect to SRCC by achieving the same value of to unveil dissimilar conclusions. For the same reason, we
|        |       |             |     |      |       |     |              |     | advocate | using | multiple | metrics of | the same | type, e.g., | both |
| ------ | ----- | ----------- | --- | ---- | ----- | --- | ------------ | --- | -------- | ----- | -------- | ---------- | -------- | ----------- | ---- |
| 0.184. | Table | I-a reports | the | MAE, | RMSE, | and | PLCC perfor- |     |          |       |          |            |          |             |      |
mance of the three QoE models and, for each of the metrics, MAEandRMSEaserrormetrics.Hence,ourrecommendation
highlights in orange the cell with the best performance. The on metrics is as follows:
resultsrevealthateachofthelogarithmic,linear,andquadratic (Modelbuilding)Fordiversityofperspectives,evaluateQoE
QoE models outperforms the other two counterparts in regard models via metrics of both error and correlation, including
|       |       |            |               |     |           |         |             |        | MAE, RMSE, | and | PLCC. |     |     |     |     |
| ----- | ----- | ---------- | ------------- | --- | --------- | ------- | ----------- | ------ | ---------- | --- | ----- | --- | --- | --- | --- |
| to    | MAE,  | RMSE,      | and PLCC      | by  | providing | the     | best values | of     |            |     |       |     |     |     |     |
| 14.8, | 19.5, | and 0.115, | respectively. |     | On        | the one | hand, it    | is not |            |     |       |     |     |     |     |
XII. QOEEVALUATIONOFABRALGORITHMS
| surprising |     | that the | QoE model | achieving |     | the | best value | for a |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --------- | --------- | --- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
metric is the model constructed to optimize this metric. On Moving the evaluation focus from QoE models to QoE
the other hand, it is remarkable that the performance of this achieved by ABR algorithms, we start by analyzing the usage
QoE model is never the best in regard to the other metrics. ofQoEmodelsforABRevaluation.Weuse945(i.e.,70%)of
We also conduct a similar analysis for the logarithmic, all 1,350 experiences in the Waterloo-IV dataset to train QoE
linear, and quadratic QoE models trained on the 43 stalling- models B, G, R, S, V, N, F, and A, i.e., eight parameterized
freeiQoEexperiencesfromSectionX.TheonlyIFisthemean models from Section II. After the training, these QoE models
PSNR calculated as the average of the PSNR values across produce values predominantly within the 1-100 range. The
all four chunks in the experience. To build the logarithmic training dataset of 945 experiences includes 189 (i.e., 70%)
and linear QoE models, we apply the Nelder-Mead method of the 270 experiences generated with each of Waterloo-
to minimize MAE with (1, 0) as the initial simplex. For the IV’s five ABR algorithms. To test the achieved QoE, we
quadratic QoE model, we strive to maximize PLCC with (2, consider Pensieve, MPC, BBA, and TR as four well-known
0, −1) as the initial simplex. schemes among these five ABR algorithms. For each of the
Figure4bplotsthetrainingiQoEdataandthreeregression- four tested ABR schemes, we evaluate the average QoE over
basedQoEmodels.Again,theSRCCperformanceisthesame the remaining 81 (i.e., 30%) of the 270 experiences generated
across the QoE models, with all three models delivering the with this ABR scheme. We conduct this QoE evaluation by
identicalvalueof0.127.InregardtoMAE,RMSE,andPLCC, separately using each of the 10 QoE models from Section II,
Table I-b confirms the qualitative conclusion reached above including models P and L which return values in the 1-5
forWaterloo-IV:whileeachoftheQoEmodeloutperformsits range. Because QoE models P and L come without public
counterpartsinonemetric,theperformanceofthisQoEmodel trainingmodules,ourevaluationusesthesetwomodelsintheir
is not the best with respect to the other metrics. Our findings publicly released configurations without any retraining.
manifest that the advantage of a QoE model in regard to one Table II reports the QoE performance achieved by the
metric might be misleading and that substantiating the overall four ABR algorithms according to the 10 QoE models. For
goodness of the QoE model necessitates its comprehensive each QoE model, the table highlights in orange and blue the
evaluation via multiple metrics. cell with the best and second-best QoE value, respectively,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
564

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
and shows the relative improvement of the former over the and individual IFs meaningfully complement each other in
| latter in | the bottom | cell. | Table | II  | shows | that TR | provides | QoE | evaluation: |     |     |     |     |
| --------- | ---------- | ----- | ----- | --- | ----- | ------- | -------- | --- | ----------- | --- | --- | --- | --- |
the highest average QoE according to five of the 10 QoE (Model using) To evaluate QoE provided by ABR algo-
models, with the relative QoE improvement over the second- rithms, complement usage of QoE models with appraisal of
| best ABR | algorithm |     | ranging | from | 0.19% | to 3.28%. | BBA | individual | IFs. |     |     |     |     |
| -------- | --------- | --- | ------- | ---- | ----- | --------- | --- | ---------- | ---- | --- | --- | --- | --- |
deliversthehighestQoEaccordingtofourQoEmodels.MPC The constellation of problems that plague objective QoE
providesthebestaverageQoEaccordingtoQoEmodelPonly. evaluation of ABR algorithms brings usage of subjective tests
Pensieve is never on top and ends up being the second-best back into the spotlight. Despite the larger overhead, direct
ABR algorithm according to two of the 10 QoE models. The assessment of QoE via subjective tests is attractive due to its
findingsshowthatthechoiceofaQoEmodelforevaluationof higher accuracy. Although conducting large-scale subjective
ABR algorithms significantly affects which of the algorithms assessments is not always feasible, we strongly recommend
achieves the highest QoE. [66] tunes various ABR algorithms consideringthisoptionforQoEevaluationofABRalgorithms:
for four QoE models and reaches the same conclusion that (Test conducting) Use subjective tests to evaluate QoE
theabilityofanABRalgorithmtooutperformitscounterparts achieved by ABR algorithms.
| depends | on the | QoE model | selected |     | for QoE | evaluation. |     |     |     |     |     |     |     |
| ------- | ------ | --------- | -------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
XIII. CONCLUSIONS
| Nevertheless, |     | a widespread |     | practice | is  | to evaluate | QoE |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
performanceofABRalgorithmsbyusingonlyoneQoEmodel This paper reviewed the current landscape of QoE in ABR
|            |     |            |     |         |     |          |      | video | streaming. | Based | on two large | real datasets | of QoE |
| ---------- | --- | ---------- | --- | ------- | --- | -------- | ---- | ----- | ---------- | ----- | ------------ | ------------- | ------ |
| or a small | set | of similar | QoE | models. | For | example, | [43] |       |            |       |              |               |        |
evaluates QoE under Pensieve vs. other ABR algorithms via perception by individual raters, we identified and examined
variousQoE-relatedpitfallsintestconducting,modelbuilding,
| three similar | variants |     | of QoE | model | B. The | QoE | evaluation |     |     |     |     |     |     |
| ------------- | -------- | --- | ------ | ----- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
of STALLION [67] employs a version of QoE model B and model using. Our analyses also derived the following
that accounts for latency. [68] compares QoE of its Stick guidelines for improving the status quo:
proposal and baseline ABR algorithms by utilizing differently • Test conducting: We recommended scoring scales with
parameterized instances of a single QoE model. a small number of levels (such as the five-level ACR
The concerns about using only one QoE model to evaluate scale),unbiasedinterfacedesign(e.g.,witharandomized
QoE performance of an ABR algorithm get exacerbated when initial position of the slider handle), realistic selection
the design or operation of the evaluated ABR algorithm of IF values across the tested experiences, and usage of
relies on the very same QoE model. Instead of detecting any subjective tests to not only build QoE models but also
systematic error introduced into the ABR algorithm by the evaluate QoE performance of ABR algorithms.
QoEmodel,suchQoEevaluationespousesandexoneratesthe • Model building: Our paper argued that a proposed
biasofthisQoEmodel.Besides,theevaluationgivestheABR QoE model should be validated via subjective tests and
algorithm an unfair advantage in comparison with other ABR annotated with its construction settings, that the QoE
algorithms that do not employ this QoE model in their design modelshouldproducepositiveinterpretablevaluesinthe
and operation. This bias problem afflicts the evaluations in intended range, and that evaluation of the QoE model
|             |     |       |     |     |     |     |     |     | should utilize | metrics | of both error | and correlation | (such |
| ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ------------- | --------------- | ----- |
| [33], [37], | and | [69]. |     |     |     |     |     |     |                |         |               |                 |       |
Given the diversity of existing QoE models and the lack as MAE, RMSE, and PLCC).
of a single, universally accepted QoE model, we argue that Model using: We suggested usage of validated QoE
•
QoEevaluationofABRalgorithmsshouldusemultiplediverse models and only in their annotated construction settings,
QoE models. The alternative perspectives offered by multiple as well as evaluation of ABR algorithms via multiple
QoE models mitigate the biases of individual models and diverse QoE models and individual IFs.
promote comprehensive evaluation of QoE achieved by ABR Thechiefaspirationofthispaperwastoimproveawareness
| algorithms. | Hence, | our | recommendation |     | on  | the usage | of QoE |     |                  |        |                   |     |            |
| ----------- | ------ | --- | -------------- | --- | --- | --------- | ------ | --- | ---------------- | ------ | ----------------- | --- | ---------- |
|             |        |     |                |     |     |           |        | of  | various problems | in the | current treatment | of  | QoE and to |
models for evaluation of ABR algorithms is as follows: indicate a way forward. We hope that our observations will
(Modelusing)EvaluateABRalgorithmsviamultiplediverse help to foster high standards in future work on QoE in ABR
QoE models.
video streaming.
TheshiftfromQoStoQoEaspirestoprovide,amongother
goals, a holistic metric of the user’s overall satisfaction. The ACKNOWLEDGMENTS
lack of consensus on the most appropriate QoE model indi- The following projects support this research:
catesthatthisaspirationstillfallsshortofitsfulfillment.[33], TED2021-131264B-I00 (SocialProbing) funded by:
•
| [43], and    | [70]       | evaluate | QoE         | performance | of             | ABR | algorithms  |     |                                  |       |                        |        |     |
| ------------ | ---------- | -------- | ----------- | ----------- | -------------- | --- | ----------- | --- | -------------------------------- | ----- | ---------------------- | ------ | --- |
|              |            |          |             |             |                |     |             |     | – MCIN/AEI/10.13039/501100011033 |       |                        | and    |     |
| by not       | only using | QoE      | models      | but         | also assessing |     | individual  |     |                                  |       |                        |        |     |
|              |            |          |             |             |                |     |             |     | – European                       | Union | NextGenerationEU/PRTR, |        |     |
| IFs employed |            | by the   | QoE models. |             | Furthermore,   |     | [34], [36], |     |                                  |       |                        |        |     |
|              |            |          |             |             |                |     |             |     | PID2021-128223OA-I00             |       | (GreenEdge)            | funded | by: |
•
| and [71]   | relinquish | QoE           | models | altogether |            | and appraise | QoE          |     |                                  |       |             |           |          |
| ---------- | ---------- | ------------- | ------ | ---------- | ---------- | ------------ | ------------ | --- | -------------------------------- | ----- | ----------- | --------- | -------- |
|            |            |               |        |            |            |              |              |     | – MCIN/AEI/10.13039/501100011033 |       |             | and       |          |
| in the QoS | style      | by evaluating |        | only       | individual |              | IFs. In this |     |                                  |       |             |           |          |
|            |            |               |        |            |            |              |              |     | – European                       | Union | ERDF “A way | of making | Europe”. |
regard,weagainfollowthespiritofcomprehensiveevaluation
| through | diversity | of perspectives |     | and | advise | that QoE | models |     |     |     |     |     |     |
| ------- | --------- | --------------- | --- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore.  Restrictions apply.
565

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
REFERENCES [25] D.Z.Rodr´ıguez,R.L.Rosa,andG.Bressan,“VideoQualityAssessment
in Video Streaming Services Considering User Preference for Video
[1] K.Brunnstro¨metal.,“DefinitionsofQualityofExperience,”Qualinet Content,”inICCE2014.
WhitePaper,2013. [26] D.Ghadiyaram,J.Pan,andA.C.Bovik,“ASubjectiveandObjective
[2] International Telecommunication Union, “Vocabulary for Performance, StudyofStallingEventsinMobileStreamingVideos,”IEEETransac-
QualityofServiceandQualityofExperience,”2017,recommendation tionsonCircuitsandSystemsforVideoTechnology,vol.29,no.1,pp.
P.10/G.100. 183–197,2019.
[3] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann, [27] International Telecommunication Union, “Methodologies for the Sub-
“A Survey on Bitrate Adaptation Schemes for Streaming Media over jectiveAssessmentoftheQualityofTelevisionImages,”2023,recom-
HTTP,” IEEE Communications Surveys and Tutorials, vol. 21, no. 1, mendationBT.500-15.
pp.562–585,2019. [28] ——, “Subjective Video Quality Assessment Methods for Multimedia
[4] Conviva, “Conviva’s State of Streaming Q2 2022,” September 2022, Applications,”2022,recommendationP.910.
Report, https://www.conviva.com/wp-content/uploads/2022/09/Q2-SoS. [29] H. Sheikh, M. Sabir, and A. Bovik, “A Statistical Evaluation of
pdf. Recent Full Reference Image Quality Assessment Algorithms,” IEEE
[5] Sandvine, “The Global Internet Phenomena Report January TransactionsonImageProcessing,vol.15,no.11,pp.3440–3451,2006.
2023,” January 2023, Report, https://www.sandvine.com/
[30] N.Eswara,K.Manasa,A.Kommineni,S.Chakraborty,H.P.Sethuram,
global-internet-phenomena-report-2023.
K. Kuchi, A. Kumar, and S. S. Channappayya, “A Continuous QoE
[6] A. Seufert, F. Wamser, D. Yarish, H. Macdonald, and T. Hoßfeld, EvaluationFrameworkforVideoStreamingOverHTTP,”IEEETrans-
“QoE Models in the Wild: Comparing Video QoE Models Using a actionsonCircuitsandSystemsforVideoTechnology,vol.28,no.11,
CrowdsourcedDataSet,”inQoMEX2021.
pp.3236–3250,2018.
[7] F.Chen,C.Zhang,F.Wang,andJ.Liu,“CrowdsourcedLiveStreaming
[31] Q.Huynh-Thu,M.-N.Garcia,F.Speranza,P.Corriveau,andA.Raake,
OvertheCloud,”inINFOCOM2015.
“Study of Rating Scales for Subjective Quality Assessment of High-
[8] U. Reiter et al., “Factors Influencing Quality of Experience,” in Qual- Definition Video,” IEEE/ACM Transactions on Networking, vol. 57,
ity of Experience: Advanced Concepts, Applications and Methods.
no.1,pp.1–14,2011.
Springer,2014.
[32] T.Tominaga,T.Hayashi,J.Okamoto,andA.Takahashi,“Performance
[9] L.Skorin-Kapov,M.Varela,T.Hoßfeld,andK.-T.Chen,“ASurveyof
Comparisons of Subjective Quality Assessment Methods for Mobile
EmergingConceptsandChallengesforQoEManagementofMultimedia
Video,”inQoMEX2010.
Services,” ACM Transactions on Multimedia Computing, Communica-
[33] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A Control-Theoretic
tions,andApplications,vol.14,no.2s,p.1–29,2018.
Approach for Dynamic Adaptive Video Streaming over HTTP,” in
[10] T. Zhao, Q. Liu, and C. W. Chen, “QoE in Video Transmission: A
SIGCOMM2015.
User Experience-Driven Strategy,” IEEE Communications Surveys &
[34] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman,“BOLA:Near-Optimal
Tutorials,vol.19,no.1,pp.285–302,2017.
BitrateAdaptationforOnlineVideos,”inINFOCOM2016.
[11] P. Juluri, V. Tamarapalli, and D. Medhi, “Measurement of Quality of
[35] I.deFez,R.Belda,andJ.C.Guerri,“NewObjectiveQoEModelsfor
ExperienceofVideo-on-DemandServices:ASurvey,”IEEECommuni-
EvaluatingABRAlgorithmsinDASH,”ComputerCommunications,vol.
cationsSurveys&Tutorials,vol.18,no.1,pp.401–418,2016.
158,pp.126–140,2020.
[12] N. Barman and M. G. Martini, “QoE Modeling for HTTP Adaptive
[36] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis,
VideoStreaming–ASurveyandOpenChallenges,”IEEEAccess,vol.7,
andK.Winstein,“LearninginSitu:ARandomizedExperimentinVideo
pp.30831–30859,2019.
Streaming,”inNSDI2020.
[13] A. A. Barakabitze, N. Barman, A. Ahmad, S. Zadtootaghaj, L. Sun,
[37] T. Huang, C. Zhou, X. Yao, R. X. Zhang, C. Wu, B. Yu, and L. Sun,
M. G. Martini, and L. Atzori, “QoE Management of Multimedia
“Quality-Aware Neural Adaptive Video Streaming with Lifelong Imi-
StreamingServicesinFutureNetworks:ATutorialandSurvey,”IEEE
tationLearning,” IEEEJournal onSelected AreasinCommunications,
CommunicationsSurveys&Tutorials,vol.22,no.1,pp.526–565,2020.
vol.38,no.10,pp.2324–2342,2020.
[14] P.Davis,C.D.Creusere,andJ.Kroger,“EEGandtheHumanPerception
[38] A.Bentaleb,A.C.Begen,andR.Zimmermann,“SDNDASH:Improving
of Video Quality: Impact of Channel Selection on Discrimination,” in
GlobalSIP2013. QoE of HTTP Adaptive Streaming Using Software Defined Network-
ing,”inMM2016.
[15] Q. Huynh-Thu and M. Ghanbari, “Scope of Validity of PSNR in
Image/VideoQualityAssessment,”ElectronicsLetters,vol.44,no.13, [39] T. Hossfeld, R. Schatz, E. Biersack, and L. Plissonneau, “Internet
p.800–801,2008. Video Delivery in YouTube: From Traffic Measurements to Quality of
[16] Z. Li, A. Aaron, I. Katsavounidis, A. Moorthy, and M. Manohara, Experience,”inDataTrafficMonitoringandAnalysis. Springer,2013.
“Toward A Practical Perceptual Video Quality Metric,” 2016, [40] C.G.BampisandA.C.Bovik,“LearningtoPredictStreamingVideo
Netflix Technology Blog. https://medium.com/netflix-techblog/ QoE: Distortions, Rebuffering and Memory,” arXiv, no. 1703.00633,
toward-a-practical-perceptual-video-quality-metric-653f208b9652. 2017.
[17] F.Tashtarian,A.Bentaleb,H.Amirpour,S.Gorinsky,J.Jiang,H.Hell- [41] A.Raake,M.-N.Garcia,W.Robitza,P.List,S.Go¨ring,andB.Feiten,
wagner, and C. Timmerer, “ARTEMIS: Adaptive Bitrate Ladder Opti- “ABitstream-Based,ScalableVideo-QualityModelforHTTPAdaptive
mizationforLiveVideoStreaming,”inNSDI2024. Streaming:ITU-TP.1203.1,”inQoMEX2017.
[18] L.Peroni,S.Gorinsky,F.Tashtarian,andC.Timmerer,“Empowerment [42] H. T. T. Tran, D. V. Nguyen, N. P. Ngoc, and T. C. Thang, “Overall
of Atypical Viewers via Low-Effort Personalized Modeling of Video Quality Prediction for HTTP Adaptive Streaming Using LSTM Net-
StreamingQuality,”inCoNEXT2023. work,”IEEETransactionsonCircuitsandSystemsforVideoTechnology,
[19] X. Zhang, Y. Ou, S. Sen, and J. Jiang, “Sensei: Aligning Video vol.31,no.8,pp.3212–3226,2021.
StreamingQualitywithDynamicUserSensitivity,”inNSDI2021. [43] H. Mao, R. Netravali, and M. Alizadeh, “Neural Adaptive Video
[20] X. Zuo, J. Yang, M. Wang, and Y. Cui, “Adaptive Bitrate with User- StreamingwithPensieve,”inSIGCOMM2017.
LevelQoEPreferenceforVideoStreaming,”inINFOCOM2022. [44] T. Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson,
[21] J. Gozdecki, A. Jajszczyk, and R. Stankiewicz, “Quality of Service “ABuffer-BasedApproachtoRateAdaptation:EvidenceFromaLarge
TerminologyinIPNetworks,”IEEECommunicationsMagazine,vol.41, VideoStreamingService,”inSIGCOMM2014.
no.3,pp.153–159,2003. [45] K.Spiteri,R.K.Sitaraman,andD.Sparacio,“FromTheorytoPractice:
[22] V.Nathan,V.Sivaraman,R.Addanki,M.Khani,P.Goyal,andM.Al- Improving Bitrate Adaptation in the DASH Reference Player,” ACM
izadeh,“End-to-EndTransportforVideoQoEFairness,”inSIGCOMM TransactionsonMultimediaComputing,Communications,andApplica-
2019. tions,vol.15,no.2s,p.1–29,2019.
[23] Z. Duanmu, A. Rehman, and Z. Wang, “A Quality-of-Experience [46] Z. Duanmu, W. Liu, Z. Li, D. Chen, Z. Wang, Y. Wang, and W. Gao,
DatabaseforAdaptiveVideoStreaming,”IEEETransactionsonBroad- “The Waterloo Streaming Quality-of-Experience Database-IV,” IEEE
casting,vol.64,no.2,pp.474–487,2018. Dataport,2020,https://dx.doi.org/10.21227/j15a-8r35.
[24] Z. Duanmu, W. Liu, Z. Li, D. Chen, Z. Wang, Y. Wang, and W. Gao, [47] L.Peroni,S.Gorinsky,F.Tashtarian,andC.Timmerer,“iQoEDataset
“AssessingtheQuality-of-ExperienceofAdaptiveBitrateVideoStream- and Code,” GitHub, 2023, https://github.com/Leo-rojo/iQoE Dataset
ing,”arXiv,no.2008.08804,2020. and Code.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore. Restrictions apply.
566

2024 16th International Conference on COMmunication Systems & NETworkS (COMSNETS)
[48] H. Mao et al., “Park: An Open Platform for Learning-Augmented [60] A. V. Ivchenko, P. A. Kononyuk, A. V. Dvorkovich, and L. A. An-
ComputerSystems,”inNeurIPS2019. tiufrieva, “Study on the Assessment of the Quality of Experience of
[49] E.Rosch,“PrinciplesofCategorization,”inCognitionandCategoriza- StreamingVideo,”inSYNCHROINFO2020.
tion. LawrenceErlbaum,1978. [61] B. Taraghi, M. Nguyen, H. Amirpour, and C. Timmerer, “Intense: In-
[50] A. K. Moorthy, L. K. Choi, A. C. Bovik, and G. de Veciana, “Video DepthStudiesonStallEventsandQualitySwitchesandTheirImpacton
QualityAssessmentonMobileDevices:Subjective,BehavioralandOb- theQualityofExperienceinHTTPAdaptiveStreaming,”IEEEAccess,
jectiveStudies,”IEEEJournalofSelectedTopicsinSignalProcessing, vol.9,pp.118087–118098,2021.
vol.6,no.6,pp.652–671,2012. [62] J. De Vriendt, D. De Vleeschauwer, and D. Robinson, “Model for
[51] C. Chen, L. K. Choi, G. de Veciana, C. Caramanis, R. W. Heath, and EstimatingQoEofVideoDeliveredUsingHTTPAdaptiveStreaming,”
A.C.Bovik,“ModelingtheTime–VaryingSubjectiveQualityofHTTP inIM2013.
Video Streams With Rate Adaptations,” IEEE Transactions on Image [63] F.GaoandL.Han,“ImplementingtheNelder-MeadSimplexAlgorithm
Processing,vol.23,no.5,pp.2206–2221,2014. with Adaptive Parameters,” Computational Optimization and Applica-
[52] Z. Duanmu, K. Zeng, K. Ma, A. Rehman, and Z. Wang, “A Quality- tions,vol.51,pp.259–277,2012.
of-Experience Index for Streaming Video,” IEEE Journal of Selected [64] Z.Duanmu,W.Liu,D.Chen,Z.Li,Z.Wang,Y.Wang,andW.Gao,“A
TopicsinSignalProcessing,vol.11,no.1,pp.154–166,2017. BayesianQuality-of-ExperienceModelforAdaptiveStreamingVideos,”
[53] J. Y. Lin, L. Jin, S. Hu, I. Katsavounidis, Z. Li, A. Aaron, and C.- ACM Transactions on Multimedia Computing, Communications, and
C. J. Kuo, “Experimental Design and Analysis of JND Test on Coded Applications,vol.18,no.3s,pp.1–24,2023.
Image/Video,”SPIEApplicationsofDigitalImageProcessingXXXVIII, [65] N.Eswara,S.Ashique,A.Panchbhai,S.Chakraborty,H.P.Sethuram,
vol.9599,pp.324–334,2015. K.Kuchi,A.Kumar,andS.S.Channappayya,“StreamingVideoQoE
[54] M. Claeys, S. Latre´, J. Famaey, T. Wu, W. Van Leekwijck, and F. D. ModelingandPrediction:ALongShort-TermMemoryApproach,”IEEE
Turck, “Design and Optimisation of a (FA)Q-Learning-Based HTTP Transactions on Circuits and Systems for Video Technology, vol. 30,
Adaptive Streaming Client,” Connection Science, vol. 26, no. 1, pp. no.3,pp.661–673,2020.
25–43,2014. [66] Y.LiuandJ.Y.B.Lee,“AUnifiedFrameworkforAutomaticQuality-
[55] S.Petrangeli,J.Famaey,M.Claeys,S.Latre´,andF.DeTurck,“QoE- of-ExperienceOptimizationinMobileVideoStreaming,”inINFOCOM
Driven Rate Adaptation Heuristic for Fair Adaptive Video Streaming,” 2016.
ACM Transactions on Multimedia Computing, Communications, and [67] C.Gutterman,B.Fridman,T.Gilliland,Y.Hu,andG.Zussman,“STAL-
Applications,vol.12,no.2,pp.1–24,2015. LION:VideoAdaptationAlgorithmforLow-LatencyVideoStreaming,”
[56] H.Bermu´dez-Orozco,J.-M.Martinez-Caro,R.Sanchez-Iborra,J.Arcin- inMMsys2020.
iegas, and M.-D. Cano, “Live Video-Streaming Evaluation Using the [68] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Stick:A
ITU-TP.1203QoEModelinLTENetworks,”ComputerNetworks,vol. HarmoniousFusionofBuffer-BasedandLearning-BasedApproachfor
165,2019. AdaptiveStreaming,”inINFOCOM2020.
[57] D.Nguyen,N.PhamNgoc,andT.C.Thang,“QoEModelsforAdaptive [69] B. Alt, T. Ballard, R. Steinmetz, H. Koeppl, and A. Rizk, “CBA:
Streaming:AComprehensiveEvaluation,”FutureInternet,vol.14,no.5, Contextual Quality Adaptation for Adaptive Bitrate Video Streaming,”
2022. inINFOCOM2019.
[58] Y. Liu, S. Dey, F. Ulupinar, M. Luby, and Y. Mao, “Deriving and [70] Z.Akhtar,S.Rao,B.Ribeiro,Y.S.Nam,J.Chen,J.Zhan,R.Govin-
ValidatingUserExperienceModelforDASHVideoStreaming,”IEEE dan, E. Katz-Bassett, and H. Zhang, “Oboe: Auto-Tuning Video ABR
TransactionsonBroadcasting,vol.61,no.4,pp.651–665,2015. AlgorithmstoNetworkConditions,”inSIGCOMM2018.
[59] Z.Duanmu,W.Liu,D.Chen,Z.Li,,Z.Wang,Y.Wang,andW.Gao,“A [71] C.Wang,A.Rizk,andM.Zink,“SQUAD:ASpectrum-BasedQuality
Knowledge-Driven Quality-of-Experience Model for Adaptive Stream- Adaptation for Dynamic Adaptive Streaming over HTTP,” in MMSys
ingVideos,”arXiv,no.1911.07944,2019. 2016.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 25,2026 at 04:28:21 UTC from IEEE Xplore. Restrictions apply.
567