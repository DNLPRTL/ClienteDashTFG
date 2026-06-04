Adaptive Bitrate with User-level QoE Preference for
Video Streaming
∗ † ∗ ∗‡
Xutong Zuo , Jiayu Yang , Mowei Wang , Yong Cui
∗
Tsinghua University, China
†
Beijing University of Posts and Telecommunications, China
Abstract—Recent years have witnessed tremendous growth of quality levels and selects the bitrate for each chunk according
video streaming applications. To describe users’ expectations to network conditions.
of videos, QoE was proposed, which is critical for content
As a simple observation, users have different preferences
providers. Current video delivery systems optimize QoE with
towards various QoE metrics. When the bandwidth resources
ABR algorithms. However, ABR is usually designed for an
abstract “average user” without considering that QoE varies arelimited,thevideoswillbedistortedwithdifferentlevelsof
with users. In this paper, to investigate the difference in user rebuffering,visualqualityandswitching,etc.Inthiscondition,
preferences, we conduct a user study with 90 subjects and usersusuallyhavedifferenttolerancesfortheabovedistortion
find that the average user can not represent all users. This
types. In this paper, we refer to the tradeoff among these
observationinspiresustoproposeRuyi,avideostreamingsystem
distortion types as user preference. For example, some
that incorporates preference awareness into the QoE model
and the ABR algorithm. Ruyi profiles QoE preference of users users would rather tolerate the rebuffering than watch low
and introduces preference-aware weights over different quality visualqualityvideos,whereassomeusersareontheopposite.
metrics into the QoE model. Based on this QoE model, Ruyi’s However, user preferences have mostly been neglected in
ABR is designed to directly predict the influence on metrics
existing QoE models and ABR algorithms, which may hinder
aftertakingdifferentactions.Withthesepredictedmetrics,Ruyi
the performances. Specifically, most QoE models assume that
chooses the bitrate that maximizes user-specific QoE once the
preference is given. Consequently, Ruyi is scalable to different all users have the same preferences. They calculate the Mean
userpreferenceswithoutre-trainingthelearnedmodelsforeach OpinionScore(MOS)andregarditasthescoreofan“average
user. Simulation results show that Ruyi increases QoE for all user”[3],[4],[10].Althoughsomeworkstakeuserpreferences
users with up to 65.22% improvement. Testbed experimental
into consideration of video images [11], temporal impair-
results show that Ruyi has the highest ratings from subjects.
Index Terms—video streaming, bitrate adaptation, quality of ments, like rebuffering, which are key factors in adaptive
experience, deep learning video streaming are not included. Besides, traditional ABR
algorithms are also agnostic to user preferences, because they
I. INTRODUCTION usually optimize towards a fixed QoE model [5], [7]–[9].
With the emergence of new applications such as video WiththesimpleobservationthatQoEpreferencesvarywith
conferences and 4K videos, the volume of video streaming users, a natural question arises: how different users’ QoE
traffic has increased rapidly in recent years [1]. As reported preferences are? To answer this question, we first conduct a
byCisco,videotrafficcouldmakeupasmuchas82%Internet user study of 90 subjects in Section II-A, followed by the
traffic by 2022 [2]. Meanwhile, user demand on video quality key findings (Section II-B). Notably, we find non-negligible
has been on the rise. In order to increase revenue, content differences among QoE preferences, and thus an average
providers make great efforts to meet users’ expectation with subject can not represent all users.
the limited network resources. Based on the findings in the user study, we argue that
Quality of Experience (QoE) is used to describe user user preferences on QoE should be considered. To achieve
expectationsandhasbeena rapidlyevolvingresearchtopicin this, ABR should optimize for each user with the preference-
adaptive video streaming. Aiming to describe users’ percep- aware QoE model. To achieve this, we propose Ruyi1, a video
tion,manyQoEmodelsareproposed,includinglearning-based streaming system that incorporates user preferences into both
methods [3], [4] and parametric methods [5], [6]. Learning- the QoE model and the ABR algorithm.
based methods can automatically generate the desired models We first profile the unique user preference of video quality
while parametric methods are simple in form and do not and try to improve prediction accuracy of QoE model. For
require much data. With the QoE model as the optimiza- compatibility, Ruyi takes a pragmatic method, which supports
tion objective, Adaptive BitRate (ABR) algorithms have been adaptable changes to the existing QoE models. Particularly,
proposed and make great breakthroughs [5], [7]–[9]. The RuyiisbasedontherepresentativeadditiveQoEmodelswhich
effectiveness of ABR algorithms is attributed to the fact that accountforalargeproportionofexistingQoEmodels[5],[6],
ABRsplitsthevideosintochunks,encodeschunksintoseveral
1Ruyi,whichmeansasyouwishinmandarin,isatalismansymbolizing
‡
YongCuiisthecorrespondingauthor. goodfortune.

[8], [10], [12], [13]. It can consist of some meta metrics (e.g., rate rendered videos generated by Ruyi and other comparison
VMAF, rebuffering, smoothness) and weights over them [5], algorithms. Experimental results show that Ruyi have the
[8], [14]. For Ruyi, we propose preference-aware weights. highest ratings from subjects.
| To estimate | the | weights, | we  | collect | quality | ratings | directly |         |               |     |      |     |     |     |     |
| ----------- | --- | -------- | --- | ------- | ------- | ------- | -------- | ------- | ------------- | --- | ---- | --- | --- | --- | --- |
|             |     |          |     |         |         |         |          | Our key | contributions |     | are: |     |     |     |     |
fromrealuserswithin-labrating.Thesubjectsarerequiredto We conduct a user study of 90 subjects showing that
•
| watch different |     | rendered | videos | distorted | by  | various | network |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------ | --------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
therearenonnegligibledifferencesintermsofpreference
conditions as well as bitrate adaptation algorithms and rate among different users in Section II.
| them. Based          | on  | the ratings, |          | we can         | infer the | weights. | With   |                  |         |     |           |            |         |         |     |
| -------------------- | --- | ------------ | -------- | -------------- | --------- | -------- | ------ | ---------------- | ------- | --- | --------- | ---------- | ------- | ------- | --- |
|                      |     |              |          |                |           |          |        | • We             | profile | the | user      | preference | and     | propose | the |
| the preference-aware |     |              | weights, | the prediction |           | accuracy | of our |                  |         |     |           |            |         |         |     |
|                      |     |              |          |                |           |          |        | preference-aware |         |     | QoE model | in         | Section | III-A.  |     |
QoE model is improved compared to that of the QoE model We propose an ABR algorithm which can deal with
•
| designed | for the | average | user. |     |     |     |     |      |             |     |          |            |       |     |              |
| -------- | ------- | ------- | ----- | --- | --- | --- | --- | ---- | ----------- | --- | -------- | ---------- | ----- | --- | ------------ |
|          |         |         |       |     |     |     |     | user | preferences |     | scalably | in Section | III-B | to  | validate the |
Then we consider to incorporate preference-aware ABR effectiveness of the preference-aware QoE model.
| into a video      | streaming  |              | system.    | However,   |              | existing    | state-of-  |                 |            |             |                |         |             |             |        |
| ----------------- | ---------- | ------------ | ---------- | ---------- | ------------ | ----------- | ---------- | --------------- | ---------- | ----------- | -------------- | ------- | ----------- | ----------- | ------ |
| the-art ABR       | algorithms |              | fail       | to achieve | this.        | Rule-based  | ap-        |                 |            |             |                |         |             |             |        |
|                   |            |              |            |            |              |             |            |                 |            |             | II. MOTIVATION |         |             |             |        |
| proaches          | (e.g.,     | buffer-based |            | approach   | [6], [7]     | and         | rate-based |                 |            |             |                |         |             |             |        |
|                   |            |              |            |            |              |             |            | With            | the simple | observation |                | that    | QoE         | preferences | vary   |
| algorithms        | [15],      | [16])        | inherently | can        | not be       | generalized | over       |                 |            |             |                |         |             |             |        |
|                   |            |              |            |            |              |             |            | with users,     | a          | natural     | question       | arises: | how         | different   | users’ |
| different         | QoE        | preferences, | since      | their      | optimization |             | objectives |                 |            |             |                |         |             |             |        |
|                   |            |              |            |            |              |             |            | QoE preferences |            | are?        | This question  |         | is critical | as diverse  | user   |
| are predetermined |            | and          | fixed      | during     | the design   | phase.      | Data-      |                 |            |             |                |         |             |             |        |
preferencesindicatethenecessityofdesigninguser-levelQoE
drivenmethods(e.g.,MPC[5],Fugu[9]andPensieve[8])can
|             |          |                |                  |          |              |                    |            | models        | and ABR | algorithms. |     | To      | answer | this question, | we      |
| ----------- | -------- | -------------- | ---------------- | -------- | ------------ | ------------------ | ---------- | ------------- | ------- | ----------- | --- | ------- | ------ | -------------- | ------- |
| support     | flexible | QoE objectives |                  | but lack | scalability. |                    | In offline |               |         |             |     |         |        |                |         |
|             |          |                |                  |          |              |                    |            | first conduct | a       | user study  | to  | collect | data   | and then       | do data |
| phase, they | often    | learns         | a representation |          | of           | the state-decision |            |               |         |             |     |         |        |                |         |
mapping (table or neural network) that is optimized for the processing. After that we present key findings from differ-
|     |     |     |     |     |     |     |     | ent perspectives. |     | Notably, | we  | find | non-negligible |     | differences |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | ---- | -------------- | --- | ----------- |
predeterminedQoEobjective.Inonlinephase,thedecisioncan
|                     |          |           |            |            |                 |        |           | among     | QoE preferences, |     | and | thus | an average | user | can not |
| ------------------- | -------- | --------- | ---------- | ---------- | --------------- | ------ | --------- | --------- | ---------------- | --- | --- | ---- | ---------- | ---- | ------- |
| be quickly          | obtained | according |            | to the     | representation. |        | However,  |           |                  |     |     |      |            |      |         |
|                     |          |           |            |            |                 |        |           | represent | all users.       |     |     |      |            |      |         |
| each representation |          | only      | supports   | one        | objective       | unless | recon-    |           |                  |     |     |      |            |      |         |
| structed,           | and thus | it is     | infeasible | to support |                 | a huge | number of |           |                  |     |     |      |            |      |         |
|                     |          |           |            |            |                 |        |           | A. User   | study            |     |     |      |            |      |         |
QoE objectives.
As defined above, user preference refers to the tradeoff Toexplorewhetherusershaveadifferenceintheperception
among different metrics. Nevertheless, the state-of-the-art of video quality, we conduct a user study in this section. We
|             |         |         |     |         |        |         |         | first create | a   | set of distorted |     | videos | and then | recruit | some |
| ----------- | ------- | ------- | --- | ------- | ------ | ------- | ------- | ------------ | --- | ---------------- | --- | ------ | -------- | ------- | ---- |
| data-driven | methods | usually |     | map the | states | and QoE | metrics |              |     |                  |     |        |          |         |      |
intoascalarreward(Pensievebasedonreinforcementlearning subjects at college to watch the videos and rate them.
(RL) [8]) or the best action (MPC [5] or Fugu [9]). The Wecreateavideosetof12sourcevideosrandomlyselected
feedback of the applied bitrate lacks detailed information of from two public video datasets [19], [20] of four content
metrics. For this reason, and inspired by [17], [18], we genres (animation, sports, nature and game) and 7 network
|          |            |          |     |      |             |     |          | throughput | traces | randomly |     | selected | from the | HSDPA | dataset |
| -------- | ---------- | -------- | --- | ---- | ----------- | --- | -------- | ---------- | ------ | -------- | --- | -------- | -------- | ----- | ------- |
| leverage | supervised | learning |     | (SL) | perspective | on  | learning |            |        |          |     |          |          |       |         |
to act, which is superior to RL when temporally vectorial [21] which contains actual cellular traces and is suitable for
feedback is available. Specifically, we directly predict the modelingchallenging,lowbandwidthnetworkconditions.The
influence on each metric of taking different actions with SL chosen traces cover various network behaviors of bandwidth
under different user preferences. Our aim is that when the and variation to cause different video quality distortions. We
|                  |     |     |       |           |     |                  |     | use Traffic-Control |     | [22] | to  | replay | the traces | in Dash.js | [23] |
| ---------------- | --- | --- | ----- | --------- | --- | ---------------- | --- | ------------------- | --- | ---- | --- | ------ | ---------- | ---------- | ---- |
| preference-aware |     | QoE | model | is given, | the | preference-aware |     |                     |     |      |     |        |            |            |      |
ABR algorithm optimizes for a specific user scalably. To and emulate the real streaming process using three ABR
achieve this, Ruyi’s ABR algorithm is trained with multiple algorithms with different behaviours: BB (buffer-based) [7] ,
QoEobjectivesoffline.Intheonlineinferencephase,Ruyican RB(throughput-based)[24]andPensieve(hybrid)[8].Finally,
(12×7×3)
explicitly make bitrate decisions according to the given QoE we get 252 distorted videos.
objective. In this way, the ABR achieves scalability as it is With these distorted videos, we conduct a single-stimulus
independent on user size and thus can be applicable to any continuous quality evaluation study at college using Psy-
number of QoE objectives without re-training. chopy[25]whichautomatestheprocessofplayingvideosand
We integrate Ruyi in our chunk-level simulator and imple- rating. We collect retrospective QoE ratings in range [1,100]
mentRuyionDash.js.Evaluationresultsshowthatpreference- on 1440p 16:9 computer monitors from a total of 90 subjects
aware QoE model can improve the prediction accuracy com- to get the individual overall QoE of each video. Overall, we
90×252
pared with the QoE model designed for the average user. gather = 22680 retrospective ratings for analysis.
Ruyi achieves an improvement of more than 43.52% and More details can be found in Section III-A.
67.20% for half of the users and the users with top 30% Each subject watches and rates the same video set, so we
improvement. As for end-to-end QoE, compared to the state- cancalculatethecorrelationofratingsforeachpairofsubjects
of-the-art algorithms, Ruyi increases QoE for all users with to explore how different subjects feel about the same video.
upto65.22%.Intestbedexperiments,subjectsarerecruitedto For the given 252 videos, each subject has 252 ratings and

(a) Ratingcorrelation(SRCC)betweensubjects. (b) Probability Distribution Function of (c) SRCCandPLCCbetweensubjectsandtheaver-
|     |     |     | SRCCbetweensubjectpairs. |     |     | agesubject. |     |     |     |     |     |     |
| --- | --- | --- | ------------------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Fig.1. Overviewofratingcorrelation.
|     |     |     |     | subject     | i and     | itself   | (i.e.,          | 1.0), the | largest     | SRCC        | between |         |
| --- | --- | --- | --- | ----------- | --------- | -------- | --------------- | --------- | ----------- | ----------- | ------- | ------- |
|     |     |     |     | other pairs | of        | subjects | is 0.77.        | An        | interesting | observation |         | is      |
|     |     |     |     | that some   | subjects, |          | like Subject16, |           | share       | relatively  |         | similar |
|     |     |     |     | preferences | with      | other    | subjects        | while     | some        | subjects    | are     | not     |
(e.g. Subject5).
|     |     |     |     | We describe  |           | the strength |           | of the    | correlation | using   | the      | fol- |
| --- | --- | --- | --- | ------------ | --------- | ------------ | --------- | --------- | ----------- | ------- | -------- | ---- |
|     |     |     |     | lowing       | guide for | the          | absolute  | value     | of SRCC     | [26]:   | very     | weak |
|     |     |     |     | (SRCC        | < 0.2),   | weak         | (0.2      | ≤ SRCC    |             | < 0.4), | moderate |      |
|     |     |     |     | (0.4≤SRCC    |           | <0.6),       |           | (0.6≤SRCC |             | <0.8)   |          |      |
|     |     |     |     |              |           |              | strong    |           |             |         | and      | very |
|     |     |     |     | strong (SRCC |           | ≥0.8).       | As Figure | 1(b)      | shows,      | almost  | 90%      | of   |
subjectpairshavearankcorrelationbelow0.6,indicatingmost
|     |     |     |     | of subject     | pairs       | are not     | strongly     | correlated. |                | Specifically, |        | only  |
| --- | --- | --- | --- | -------------- | ----------- | ----------- | ------------ | ----------- | -------------- | ------------- | ------ | ----- |
|     |     |     |     | 11% pairs      | of subjects |             | are strongly |             | correlated     | while         | almost | a     |
|     |     |     |     | quarter        | of subjects | are         | weakly       | correlated. |                | The remaining |        | 65%   |
|     |     |     |     | are moderately |             | correlated. |              |             |                |               |        |       |
|     |     |     |     | From           | Figure      | 1(a),       | we observe   |             | that some      | subjects      |        | share |
|     |     |     |     | relatively     | similar     | preferences |              | with        | other subjects |               | while  | some  |
Fig.2. Visualizationofsubjects’ratingsbydividingthevideosintodifferent subjectsarenot.Inordertocharacterizethisdifferenceamong
partsaccordingtothemetriclevels. subjects, we calculate the average SRCC of each subject and
the ranking of these ratings are of concerned. Spearman rank- other subjects, whose distributions are plotted as the blue line
inFigure1(c).Inparticular,mostsubjectsareonlymoderately
| order correlation | coefficient (SRCC) | can be | used to indicate |     |     |     |     |     |     |     |     |     |
| ----------------- | ------------------ | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the correlation of the ranking. We calculate the SRCC for the correlated with others, and no subjects are strongly corre-
subjects’ rating sequences of distorted videos. The higher the lated. For completeness, Pearson linear correlation coefficient
(PLCC)results(i.e.,greenlineinFigure1(c))arealsoshown,
| SRCC, the higher | the correlation | between | the ratings of the |     |     |     |     |     |     |     |     |     |
| ---------------- | --------------- | ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two subjects, the closer the subjects’ perception of the video which have the same trend as SRCC.
quality, and the more similar the preferences of the subjects. Apartfromtheaboveanalysisonoverallratingcorrelations,
Iftherankingoftworatingssequenceisexactlythesame,the we also investigate rating distributions according to different
SRCC is 1.0. The data processing is introduced in III-A, and QoE metrics. Specifically, we divide the distorted videos
only the results are introduced here. according to VMAF and rebuffering. VMAF is divided into 4
|     |     |     |     | levels, and | rebuffering |     | is divided |     | into 3 | levels. | As a | result, |
| --- | --- | --- | --- | ----------- | ----------- | --- | ---------- | --- | ------ | ------- | ---- | ------- |
B. Key findings
|     |     |     |     | these distorted |     | videos | are | divided | into | 12 parts. | Then | for |
| --- | --- | --- | --- | --------------- | --- | ------ | --- | ------- | ---- | --------- | ---- | --- |
(1) Almost 90% of subject pairs are not strongly videos in each part, the corresponding ratings of all subjects
correlated. We first present the SRCC of ratings for each are shown in Figure 2. Apparently, it can be observed that
pair of subjects in Figure 1(a). The color of the small square subject ratings have different distributions in distinct metric
at the intersection of row i and column j represents the levels. This observation is within expectation. Intuitively, for
SRCCbetweensubjectiandsubjectj.HigherSRCCindicates
|     |     |     |     | the videos | with | very | high/low | quality, |     | users | tend to | give |
| --- | --- | --- | --- | ---------- | ---- | ---- | -------- | -------- | --- | ----- | ------- | ---- |
more similar preferences between subjects. Considering the relatively consistent high/low ratings. Contrarily, for videos
symmetryofSRCCheatmap,onlythepartbelowthediagonal withmediumquality,subjectratingsmayhavelargevariances.
isshown.AsshowninFigure1(a),asidefromSRCCbetween AsexemplifiedinFigure2,theboxinthefirstrowandfourth

(cid:4)(cid:18)(cid:21)(cid:11)
(cid:3)(cid:14)(cid:2) Preference-aware QoE User-aware Request
(cid:2)(cid:20)(cid:11)(cid:16)(cid:17)(cid:11)(cid:13)(cid:9) Ratings QoEmodeling model ABR
(cid:5)(cid:16)(cid:8)(cid:15)(cid:16) (cid:1)(cid:19)(cid:8)(cid:15)(cid:6)(cid:9)(cid:8) (cid:12)(cid:8)(cid:17)(cid:10)(cid:14)(cid:7)(cid:16) ((cid:2)(cid:4)(cid:3)(cid:8)(cid:5)(cid:7)(cid:6)(cid:1)(cid:1)(cid:9)(cid:10)) ((cid:2)(cid:4)(cid:3)(cid:8)(cid:5)(cid:7)(cid:6)(cid:1)(cid:1)(cid:9)(cid:11)) Chunks
(cid:18)(cid:16)(cid:8)(cid:15)
VideoPlayer VideoServer
Fig.3. ComparisonofRuyiandexistingmethods.
Fig.4. SystemoverviewofRuyi.
columnhasthehighestmeanscore(72)withtheleaststandard
distortedvideos.Furthermore,wesetupsomerejectioncriteria
deviation (11.24). Besides, the box in the third row and third
to get reliable quality ratings. Specifically, we insert a video
column has the largest standard deviation (21.04).
with the highest VMAF and no rebuffering as a reference
(2)Theaverageusercannotrepresentallusers.Existing
video.Ifthesubjectdoesnotgivethisvideothehighestrating,
QoE models and ABR algorithms try to optimize QoE based
then the ratings of this subject will be rejected.
on an average user as Figure 3 shows. Here, we further inves-
Following data collection, we process the collected ratings
tigate whether the average user can represent all users well.
to eliminate biases. First, we analyze the rating sequence
First, we construct an average user whose rating for a video
of each subject and find that the ratings conform to normal
is the average rating of all the subjects. We calculate SRCC
distribution. Then, we apply normalization to the collected
and PLCC between each subject and the average user, whose
ratings to prepare for the following QoE modeling. The
distributions are plotted as the red lines in Figure 1(c). More
ratingsofdifferentsubjectsusuallyfallindifferentranges.For
than 50% of subjects have a relatively low correlation (lower
example,subjectswhoareaccustomedtoratehighlymaygive
than 0.7) with the average user, indicating that the average
all ratings higher than 60. In order to normalize the subject’s
user can not represent all users. This further enhances our
motivation:whenconsideringuserpreference,thereshouldbe
rating in the same range, for the rating sequence x i, we apply
ample room for QoE improvement. To unleash this potential, (x i −x min)×100/(x max −x min) to each rating where x max
we propose the user-aware QoE model and ABR algorithm. and x min represent the maximum and minimum values of a
subject’s rating respectively.
III. RUYI’SDESIGN Encode user sensitivities towards different QoE metrics.
As mentioned above, Ruyi is based on the representative
So far we have shown that user preference is a key factor
additive QoE models. As a result, the perceived QoE of video
for the improvement of user QoE. To boost QoE, we propose
j for user i can be written as:
Ruyi,avideostreamingsystemconsistingoftwocomponents
(Figure 4): Preference-aware QoE model and user-specific QoE ij =w i ·q j , (1)
ABR algorithm. Next we introduce these two components in
Section III-A and Section III-B respectively. where w i represents the preference weights of user i and q j
denotestheQoEmetricsofvideoj.IntheadditiveQoEmodel,
A. Modeling preference-aware QoE overall QoE is the sum of the QoE of all chunks. So we can
write Equation 1 as:
Different from existing average QoE models, we build a
(cid:2)N
specific QoE model for each subject. Apparently, ratings are QoE ij =w i · m k , (2)
neededforeachspecificsubject.Inthiswork,weobtainthese
k=1
ratings based on the measurement study in Section II. The
procedureofourpreference-awareQoEmodelingisdescribed where m k = (v k ,r k ,s k) is the vectorial meta metrics of
as follows. First, we describe the quality control of subject chunkk andN isthenumberofchunksofvideoj.v k,r k and
ratings. After that, we show the data processing of subject s k representtheVMAF,rebufferandqualityswitchforchunk
krespectively.TherangeofVMAFis[0,100]andtherebuffer-
ratings. Finally, we encode user sensitivities towards different
QoE metrics into the preference-aware QoE model. ing is counted in frame numbers. Since w i =(w iv ,w ir ,w is)
represents the QoE model of user i and is the same to all
Quality control of subject ratings. Since the subject
chunks:
ratings may be noisy, we take several principled measures
to control rating quality. First, before the rating process, the (cid:2)N
subjects are required to fill out a questionnaire about QoE QoE ij = (w iv ,w ir ,w is)·(v k ,r k ,s k). (3)
preferences. In this way, subjects are able to get familiar with k=1
the QoE metrics and their preferences. Besides, subjects are Next we present how to infer the weights w i for each
requiredtoratebasedonconsistentcriteria.Togetthesubjects user. Given M rendered videos distorted by different network
familiar with the video quality ranges, two reference videos conditions, we get M ratings of user i, which represent
with the best and worst quality are played. In rating process, the corresponding perceived QoE. With the rating QoE ij
fordifferentsubjects,thedistortedvideosarerandomlyplayed and video metrics (v k ,r k ,s k) known in advance, we can
to eliminate biases caused by the viewing order. To avoid write M equations for each user i, QoE ij = w i ·q j where
subject fatigue in the nearly two-hour rating process, each j = 1,2,...,M. Finally, we can infer w i using the linear
subject can take a five-minute break after rating a third of regression for user i.

B. Ruyi’s ABR design (cid:20)(cid:28)(cid:41)(cid:42)(cid:39)(cid:36)(cid:40)(cid:13)(cid:1)(cid:35)(cid:28)(cid:41)(cid:24)(cid:1)(cid:19)(cid:37)(cid:16)(cid:1)(cid:35)(cid:28)(cid:41)(cid:39)(cid:32)(cid:26)(cid:40)
Existing ABR algorithms ignore different user preferences,
(cid:14)(cid:28)(cid:40)(cid:41)(cid:1) whichmayhinderQoEimprovement.Tothisend,wepropose (cid:30) (cid:24) (cid:32) (cid:26) (cid:43) (cid:41) (cid:28) (cid:32) (cid:36) (cid:37) (cid:1) (cid:36) (cid:2) (cid:1) (cid:6) (cid:11) (cid:5) (cid:7) (cid:12) (cid:5) (cid:5) (cid:18) (cid:18)
Ruyi’s ABR algorithm in this section. Ruyi leverages the (cid:9)(cid:12)(cid:5)(cid:18) (cid:8)(cid:10)(cid:5)(cid:18)
supervisedlearningperspectiveonlearningtoact.Specifically,
(cid:22)(cid:40)(cid:28)(cid:39)(cid:1)(cid:38)(cid:39)(cid:28)(cid:29)(cid:28)(cid:39)(cid:28)(cid:36)(cid:26)(cid:28)
Ruyi directly predicts the influence on each metric after (cid:15)(cid:34)(cid:32)(cid:28)(cid:36)(cid:41)(cid:4)(cid:40)(cid:32)(cid:27)(cid:28)(cid:1)(cid:36)(cid:28)(cid:41)(cid:44)(cid:37)(cid:39)(cid:33)(cid:1)(cid:24)(cid:36)(cid:27)(cid:1)(cid:43)(cid:32)(cid:27)(cid:28)(cid:37)(cid:1)(cid:38)(cid:34)(cid:24)(cid:45)(cid:28)(cid:39)(cid:1)(cid:35)(cid:28)(cid:24)(cid:40)(cid:42)(cid:39)(cid:28)(cid:35)(cid:28)(cid:36)(cid:41)(cid:40)
takingdifferentactions.Inthisway,Ruyi’sABRcanoptimize
towards given user preferences.
We use a general setting where an agent interacts with an
(cid:19)(cid:42)(cid:24)(cid:34)(cid:32)(cid:41)(cid:45)(cid:2)(cid:23)(cid:3) (cid:20)(cid:28)(cid:25)(cid:42)(cid:29)(cid:29)(cid:28)(cid:39)(cid:32)(cid:36)(cid:30)(cid:2)(cid:20)(cid:14)(cid:3) (cid:21)(cid:44)(cid:32)(cid:41)(cid:26)(cid:31)(cid:2)(cid:21)(cid:3)
environmentlikeinRL.Ateachtimestept,theagentreceives
(cid:17)(cid:28)(cid:41)(cid:24)(cid:1)(cid:19)(cid:37)(cid:16)(cid:1)(cid:17)(cid:28)(cid:41)(cid:39)(cid:32)(cid:26)(cid:40)
the observation o t and chooses an action a t to maximize the
objective.o tconsistsoftwopartss tandm t,wheres tincludes
network conditions as well as video player measurements, m t
represents the meta metrics directly affecting users’ QoE and a t represents the bitrate. After applying the action, the state
of the environment transits to s t+1 and the agent receives the
influences of that action on QoE meta metrics m t which acts
as the temporally vectorial feedback.
With the definition of the preference-aware QoE model
in Section III-A, the total optimization objective of Ruyi
u(m,w) can be expressed as follows:
u(m,w)=w·m, (4)
where w represents the user preference and m =
(cid:4)m t ,...,m t+n (cid:5) represents present and future QoE metrics of
different temporal offsets.
The key design is that we directly predict future measure-
ments,i.e.,metaQoEmetricsm,withaneuralnetworkasour
evaluation function Q(o,a,w). As shown in Figure 5, Ruyi
is designed under the general framework for value function
approximators [27]. We decouple the evaluation and decision
process by explicitly introducing the user preference w into
Ruyi to enable scalability. During training, Ruyi’s ABR grad-
ually learns to make better ABR decisions with preference-
aware QoE objectives. During online inference phase, Ruyi
chooses the best bitrate that maximize an preference-aware
QoE objective according to the linear combination of the
output of evaluation function and the preference w. For
different users with distinct QoE models, we just modify the
corresponding parameters of QoE model without modifying
the ABR logic or retraining the ABR.
1) Evaluation function approximator: Leveraging the con-
cept of Universal Value Function Approximator [27], [28],
we design a customized neural network (valueNet) as our
evaluation function.
Inputs: After the download of each chunk t, Ruyi’s agent
takes state inputs s t = (x t ,τ t ,n t ,v t ,b t ,c t ,l t) to its neural
networks. x t is the network throughput measurements for the
past k video chunks; τ t is the download time of the past
k video chunks, which represents the time interval of the
throughput measurements; n t is a vector of available sizes
for the next video chunk; v t is a vector of available VMAF
values for the next video chunk; b t is the current buffer level;
c t isthenumberofchunksremaininginthevideo;andl t isthe
bitrateatwhichthelastchunkwasdownloaded.Besides,video
…
(cid:2)
(cid:1)(cid:2)
(cid:1)(cid:1)(cid:2)(cid:1) (cid:1)(cid:2)(cid:2)(cid:1) (cid:1)(cid:1)(cid:1) (cid:1)(cid:4)(cid:2)(cid:1) (cid:1) (cid:1)(cid:3) (cid:1)(cid:1)(cid:2)(cid:2) (cid:1)(cid:2)(cid:2)(cid:2) (cid:1)(cid:1)(cid:1) (cid:1)(cid:4)(cid:2)(cid:2)
(cid:3) (cid:1)(cid:1)(cid:1)
(cid:1)(cid:1)(cid:2)(cid:3)(cid:1)(cid:2)(cid:2)(cid:3) (cid:1)(cid:1)(cid:1) (cid:1)(cid:4)(cid:2)(cid:3)
… (cid:4) (cid:2)(cid:1) (cid:3)
Fig.5. ABRframeworkofRuyi.Theinputsareobservations(o),metametrics
(m)anduserpreferences(w).TheoutputQisthepredictionofmetametrics
ondifferentactions.
player measurements of the last downloaded chunk m t are as the second part of the inputs. It includes the VMAF of the
lastdownloadedchunk,therebufferingcausedbydownloading
the last chunk and the quality switch. We also add the user
preference w as input which influences the optimal strategy
and the final evaluation result.
Outputs: In this work, we directly predict the future QoE
metrics.Sinceweneedtomaximizetheuser’slong-termQoE,
weadoptthevalueconcepttomodelthemetametricsi.e.,m.
To explicitly optimize for a given QoE objective, we split the
conventional action value Q(o,a) into several action-metric
values,whichonlymodelthevalueforonemetametric.Thus
we can predict the QoE of each action under any preference
w. Recall that the standard value function is defined as the
expected cumulative discounted reward over all future steps,
denotedasQ ∞.However,sincethenetworkconditionchanges
dynamically,thelong-termuncertaintymayhurttheprediction
accuracy. Thus we use enough short-term value predictions
{Q t |t = 1,2...,n} as the output, where t denotes the look-
ahead step. Combing the above two modifications, the output
of the valueNet is Q(o,a,w) = {Q t(o,a,w)|t = 1,2,..,n},
where n can be adjusted according to the network condition.
Neural network architecture: The predictor Q is a deep
network and the structure is shown in Figure 6. To conduct
feature extraction more efficiently, we use the convolution
layer for the vectorial state input and merge its output with
other scalar state and measurement inputs. For the preference
input w, we use fully-connected layers and merge the output
with other features extracted from state inputs. Then we use
a dueling architecture [29] to enhance the value prediction.
Specifically,wesplit thefeaturesintotwo stream:anexpecta-
tion stream E which predicts the value over this observation
and an action stream A reflects the fine differences between
actions. Finally, the expectation stream E is added to each of
action stream A k where k is the dimension of actions. The
detailed parameters are shown in Section IV.
2) Training and inference: We train the valueNet us-
ing a variant of Deep Q-learning algorithm [30] with the
experience replay technique. The agent interacts with the
environment and collects a set of experiences D where
D ={(o j ,a j ,w j ,f j)}T j=1 . (o j ,w j) is the input of the neural
network and a j indicates the action that we are predicting

control the egress traffic and emulate the network variation.
(cid:3) The weights representing user preference needed by Ruyi’s
(cid:2) (cid:1)(cid:9)(cid:7)(cid:6)(cid:5)(cid:3)(cid:2)(cid:8)(cid:4)
ABR algorithm is configurable for each user at client and can
be re-loaded if updated.
(cid:3)(cid:14)(cid:8)(cid:7)(cid:9)(cid:6)(cid:16)(cid:8)(cid:7)
(cid:1) (cid:2)(cid:17)(cid:13)(cid:8)(cid:6)(cid:16)(cid:5)(cid:16)(cid:9)(cid:12)(cid:11)(cid:4)(cid:16)(cid:14)(cid:8)(cid:5)(cid:10) (cid:10)(cid:8)(cid:16)(cid:5) Parameters setting of Ruyi’s ABR. Here we overview the
(cid:10)(cid:8)(cid:16)(cid:14)(cid:9)(cid:6)(cid:15)
hyperparametersintrainingABRalgorithminRuyi.Ruyiuses
k = 6 past chunks as bandwidth measurements. The look-
(cid:3) ahead step is n=3. There are 3×3=9 neurons of both the
(cid:3)
expectation stream and the action stream representing 3 meta
(cid:1)(cid:6)(cid:16)(cid:9)(cid:12)(cid:11)(cid:4)(cid:16)(cid:14)(cid:8)(cid:5)(cid:10) QoE metrics in 3 time offsets. There are 64 neurons in each
hidden layers. The activation function is Leaky Relu and the
Fig. 6. Neural network structure. Inputs: network states (s), meta metrics
(m)anduserpreferences(w).Toenhanceuserpreference,wiscontactedin learning rate is set to 10−3. These hyperparameters are used
eachneuralnetworklayer. without particularly fine-tuned. We implement Ruyi’s ABR
the subsequential influence for. f j is the label of trajectory j algorithm with TensorFlow [31] and TFLearn [32].
which consists of multiple metric triples where each triple f jt V. EVALUATION
is constructed as follows:
A. Experimental Setup
(cid:3) Networkandvideotraces.AsmentionedinSectionII,we
f jt(a)= m
m
j
j
+
+
1
1
,
+Q t−1(o j+1 ,a,w j+1),
t
t
=
>1
1,
.
(5) r
a
e
n
p
d
la
v
y
ar
t
i
h
a
e
nc
s
e
tre
fr
a
o
m
m
in
H
g
S
v
D
id
P
e
A
o
[
in
21
7
]
t
t
r
o
ac
c
e
o
s
ns
w
tr
i
u
th
ct
v
t
a
h
r
e
io
2
u
5
s
2
b
d
a
i
n
s
d
to
w
r
i
t
d
io
th
n
videos. We train the preference-aware QoE model on a subset
Thedirectoptimizationobjectiveistominimizethefollowing
of 216 videos obtained in the randomly selected 6 network
regression loss:
traces(12sourcevideos,6networktraces,3ABRalgorithms,
(cid:2)T
L(θ)= (cid:6)Q(o j ,a j ,w j)−f j(a(cid:3))(cid:6)2, (6) 216 = 12 × 6 × 3) and test them on the remaining one
network trace with medium average bandwidth, i.e., the rest
j=1
(cid:4) 36 videos (36 = 12 × 1 × 3), to evaluate the accuracy of
where a(cid:3) =argmax a n t=1 f jt(a). preference-awareQoEmodel.Besides,thenetworktracesused
With this objective, we train the valueNet with supervised fortrainingtwolearningABRalgorithms(PensieveandRuyi)
learning to explicitly approximate the future metrics. Then and testing all ABR algorithms are randomly selected from
we can get the best action to maximize the total optimization HSDPAdataset[21].Ourevaluationusethetestvideoselected
objective u(m,w) of our problem. Specifically, in the offline from the LIVE-NFLX-II video dataset [19]. This video is
training, the user preference w for each episode is generated encoded by the H.264/MPEG-4 codec at bitrates in {300,
atrandom.Eachvalueissampleduniformlyfromapredefined 750,1200,1850,2850,4300}kbps(whichcorrespondtovideo
reasonable range. The agent follows an (cid:3)-greedy policy: it levels in {240, 360, 480, 720, 1080, 1440}p).
acts greedily according to the current user preference w with Comparison algorithms. We compare Ruyi with the fol-
probability 1-(cid:3), and selects a random action with probability lowing algorithms with different adaptive strategies:
(cid:3). The value of (cid:3) is initially set to 1 and is decreased during • Buffer-based adaptation (BB) [7] without specific QoE
training according to a fixed schedule. In online phase, Ruyi models:choosesthechunksaccordingtotheclientbuffer.
takes the action that yields the best predicted outcome: • MPC [5] (with the average QoE model): chooses the
(cid:2)n
argmax w(cid:4)· Q t(o,a,w). (7) chunks to maximize the QoE model of the average user
a in our dataset over a horizon of 5 future chunks.
t=1
(cid:4) • Pensieve [8] (with the average QoE model): chooses the
where w(cid:4) · n t=1 Q t(o,a,w) can be treated as a discounted chunks with the pre-trained learning-based ABR algo-
form of the optimization objective Equation (4). rithmtowardstheaverageuser.Were-trainPensievewith
the average QoE model with our collected data.
IV. IMPLEMENTATION
Performance metrics. To show the improvement of QoE
Video system implementation. We implement Ruyi based model when considering user preference, we evaluate the
on DASH.js [23] which is a widely used open source video performance of our model with Pearson’s Coefficient (PLCC)
player. Prominent ABR algorithms, (i.e., BB, MPC and Pen- andSpearman’sCoefficient(SRCC).Besides,weuseQoEand
sieve) are configured and can run in DASH.js. We use a QoE gain (((Q 1 −Q 2)/Q 2)) of one ABR (Q 1) over another
PC (Intel(R) Core(TM) i3-2120 CPU@3.30GHz) as the video (Q 2) to show the efficiency of Ruyi system.
serverandalaptop(ASUS-N551JW)astheclientwhereABR
B. Effectiveness analysis of preference-aware QoE model
algorithms are located. The first time to fetch a new video,
the manifest file is downloaded. We augment it by adding We show the preference-aware weights of all 90 subjects
VMAF of chunks in a new XML field which is used in we recruit (the red points) as well as the average user (the
the following bitrate decision. We use tc [22] on server to blue point) in Figure 7 (derived as Section III-A shows).

Fig.7. QoEmodelsofallusers,whichareexpressed Fig.8. Differencesofthepreference-aware Fig.9. QoEpredictionaccuracyimprovementwhen
bypreference-awareweights.Thebluepointrepresent weightsbetweentheaverageuserandotherusers.comparing preference-aware QoE model to the av-
theaverageuserandredpointsrepresentallotherusers. erageQoEmodel.
Apparently, it can be observed that the average QoE model network traces. From left to right are the QoE for all users,
is located in the center of other models. This observation is the improvement top 50% users, top 15% users and top 5%
within expectation. Besides, we observe that the QoE model users.Fortop5%users,comparedtoBB,MPCandPensieve,
varies with users and it is hard to divide them into several Ruyi achieves improvements of 26.3%, 24.7%, and 18.2%
categories. This result indicates that preference-aware QoE respectively.Moreover,theaverageperformanceimprovement
improvement is needed and that the average user can not decreases with the number of users increases. The reason is
represent all users. What’s more, we show the difference of that some users who are close to the average user have less
the three weights between each user and the average user improvement than users who are far from the average user.
in Figure 8. We observe that, compared with the average For all users, compared to the baseline BB, Ruyi has 10.6%
user, other users show the largest difference in the rebuffer QoE improvement on average.
weight and the smallest difference in the VMAF weight. It Figure 10(b) provides more detailed results which shows
| indicates | that       | users show | the | largest  | preference |     | variety | in                |      |              |         |         |          |      |          |
| --------- | ---------- | ---------- | --- | -------- | ---------- | --- | ------- | ----------------- | ---- | ------------ | ------- | ------- | -------- | ---- | -------- |
|           |            |            |     |          |            |     |         | the distributions |      | of QoE       | gains   | for all | users.   | Ruyi | achieves |
| rebuffer  | perception | while      | the | smallest | in VMAF.   |     |         |                   |      |              |         |         |          |      |          |
|           |            |            |     |          |            |     |         | a positive        | gain | on all users | whereas | MPC     | achieves | a    | positive |
Then,wepresenttheimprovementofQoEmodelprediction gainon33.3%users.ForRuyi,allusersachieveaperformance
| accuracy  | of the     | subjects | in               | Figure    | 9. We        | calculate | SRCC     |             |           |               |       |            |          |              |          |
| --------- | ---------- | -------- | ---------------- | --------- | ------------ | --------- | -------- | ----------- | --------- | ------------- | ----- | ---------- | -------- | ------------ | -------- |
|           |            |          |                  |           |              |           |          | improvement |           | of more       | than  | 4% whereas | Pensieve |              | achieves |
| and PLCC  | to measure |          | the increase,    |           | and they     | show      | the same |             |           |               |       |            |          |              |          |
|           |            |          |                  |           |              |           |          | that on     | 55.6%     | users. What’s |       | more,      | Ruyi     | obtains over | 10%      |
| trend. We | use        | SRCC     | in the           | following | description. |           | For each |             |           |               |       |            |          |              |          |
|           |            |          |                  |           |              |           |          | QoE gains   | on        | about 17.8%   | users | with       | up to    | 65.22%.      | We also  |
| subject,  | we test    | the      | preference-aware |           | QoE          | model     | and the  |             |           |               |       |            |          |              |          |
|           |            |          |                  |           |              |           |          | present     | that Ruyi | can reach     | a     | wide range | of       | performance  | by       |
average model on the test dataset of 36 videos. For the flexible adjusting the user’s preference in Figure 10(c). We
| test video | sequences, |     | we get | the scores | predicted |     | with the |        |           |          |       |     |        |     |           |
| ---------- | ---------- | --- | ------ | ---------- | --------- | --- | -------- | ------ | --------- | -------- | ----- | --- | ------ | --- | --------- |
|            |            |     |        |            |           |     |          | choose | 4 example | subjects | whose | QoE | models | are | different |
preference-awareQoEmodelandcalculatetheSRCCofthese
|     |     |     |     |     |         |     |     | (Ruyi 1, | Ruyi | 2, Ruyi | and Ruyi | for | Subject2, | 59, | 85 and |
| --- | --- | --- | --- | --- | ------- | --- | --- | -------- | ---- | ------- | -------- | --- | --------- | --- | ------ |
|     |     |     |     |     | i (SRCC |     |     |          |      | 3       |          | 4   |           |     |        |
scores and the ratings of subjects i). We get the 41 respectively) and run experiments on 1 example testing
| SRCC of | average | model | in  | the same | way  | (SRCC  | a). Then |         |        |                |     |         |      |           |     |
| ------- | ------- | ----- | --- | -------- | ---- | ------ | -------- | ------- | ------ | -------------- | --- | ------- | ---- | --------- | --- |
|         |         |       |     |          |      |        |          | network | trace. | The preference |     | weights | over | different | QoE |
|         |         |       |     |          | SRCC | − SRCC |          |         |        |                |     |         |      |           |     |
the difference can be calculated as i a and metrics of the 4 subjects are (0.33, -0.92, -0.46), (0.40, -
| presented | in Figure | 9    | to show | the     | QoE | model  | prediction |              |        |            |        |            |         |        |         |
| --------- | --------- | ---- | ------- | ------- | --- | ------ | ---------- | ------------ | ------ | ---------- | ------ | ---------- | ------- | ------ | ------- |
|           |           |      |         |         |     |        |            | 0.60, 0.32), | (0.55, | -0.41,     | -0.27) | and (0.65, | -0.34,  | 0.15). | Other   |
| accuracy. | Compared  | with | the     | average | QoE | model, | using the  |              |        |            |        |            |         |        |         |
|           |           |      |         |         |     |        |            | comparison   | ABR    | algorithms |        | optimize   | towards | the    | average |
preference-aware QoE model brings an increase of more than user and can reach only one result point shown as red points
| 43.52% | and 67.20% |     | of QoE | model | prediction | accuracy | for |           |        |            |     |          |       |        |          |
| ------ | ---------- | --- | ------ | ----- | ---------- | -------- | --- | --------- | ------ | ---------- | --- | -------- | ----- | ------ | -------- |
|        |            |     |        |       |            |          |     | in Figure | 10(c). | Meanwhile, |     | Ruyi can | reach | a wide | range as |
half of the users and the top 30% users (the top 30% of users long as the user preferences are given.
| most impacted). |        | The | results | show | the effectiveness |     | of user- |          |            |     |          |            |          |         |         |
| --------------- | ------ | --- | ------- | ---- | ----------------- | --- | -------- | -------- | ---------- | --- | -------- | ---------- | -------- | ------- | ------- |
|                 |        |     |         |      |                   |     |          | QoE      | breakdown. | To  | better   | understand |          | the QoE | gains   |
| aware QoE       | model. |     |         |      |                   |     |          |          |            |     |          |            |          |         |         |
|                 |        |     |         |      |                   |     |          | obtained | by Ruyi,   | we  | analyzed | the        | achieved | meta    | metrics |
C. End-to-end QoE evaluation for each user. Specifically, we present the preference-aware
|             |     |      |      |           |            |     |         | weights | of each | user | and the | achieved | QoE | metrics, | i.e., |
| ----------- | --- | ---- | ---- | --------- | ---------- | --- | ------- | ------- | ------- | ---- | ------- | -------- | --- | -------- | ----- |
| We evaluate |     | Ruyi | with | other ABR | algorithms |     | in both |         |         |      |         |          |     |          |       |
simulation environment and DASH.js. VMAF, the rebuffering time and switches of VMAF, in
|     |     |     |     |     |     |     |     | Figure 11. | Each | dot in | the figure | represents |     | a user | and the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | ---------- | ---------- | --- | ------ | ------- |
1) Simulation:
Overall QoE gains. We present the overall QoE and QoE value is the average of metric on all testing traces.
gains in Figure 10. We find that Ruyi outperforms other As shown in Figure 11, there is an approximate linear rela-
algorithmswhichequippedwiththeaverageQoEmodel(MPC tionship between the achieved VMAF and the VMAF weight
and Pensieve) and without QoE models (BB). Figure 10(a) of different users. The larger the VMAF weight is, the more
showstheQoEofRuyi,BB,MPCandPensieveacrossalltest the users care about VMAF and the larger the value achieved

(a) OverallQoEofusers. (b) QoEgainsoverBBofdifferentusers. (c) Ruyi achieves a wide range of video quality
flexibly.
|                  |        |          |          |                |         | Fig.10.          | OverallperformanceofRuyi.      |     |     |     |        |     |     |
| ---------------- | ------ | -------- | -------- | -------------- | ------- | ---------------- | ------------------------------ | --- | --- | --- | ------ | --- | --- |
|                  |        | (a) VMAF |          |                |         |                  | (b) Rebuffering                |     |     | (c) | Switch |     |     |
|                  |        |          |          |                | Fig.11. |                  | QoEbreakdownofRuyiforallusers. |     |     |     |        |     |     |
| by the algorithm |        | is. The  | achieved | average        | VMAF    |                  | across all                     |     |     |     |        |     |     |
| test traces      | ranges | from     | 47 to    | 53. Similarly, |         | for rebuffering, |                                |     |     |     |        |     |     |
whentheweightislessthan0,thegreatertheabsolutevalueof
theweight,thelessusersprefertherebuffering.Consequently,
| the resulted | rebuffering  |                 | time          | is smaller.     | Switching    |          | shows the  |     |     |     |     |     |     |
| ------------ | ------------ | --------------- | ------------- | --------------- | ------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| similar      | results      | as rebuffering. |               | Besides,        | we find      | the      | difference |     |     |     |     |     |     |
| between      | the achieved |                 | VMAF          | values          | of users     | is less  | than that  |     |     |     |     |     |     |
| of the other | two          | metrics,        | i.e.,         | the rebuffering |              | and the  | switch.    |     |     |     |     |     |     |
| This result  | also         | corresponds     |               | to Figure       | 8, where     | the      | weight     |     |     |     |     |     |     |
| difference   | of VMAF      |                 | for different | users           | is the       | smallest | among      |     |     |     |     |     |     |
| the three    | metrics.     | Figure          | 11 directly   |                 | proves that  | Ruyi     | has the    |     |     |     |     |     |     |
| ability to   | optimize     | towards         | different     |                 | preferences. |          |            |     |     |     |     |     |     |
Bandwidth savings. To investigate bandwidth savings, we Fig.12. QoEv.s.bandwidthusage.
| present | the QoE | obtained | with | unit | bandwidth | (denoted | as  |     |     |     |     |     |     |
| ------- | ------- | -------- | ---- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
QoE/BW)inFigure12.Foreachnetworktrace,wecalculate
|        |          |      |          |     |             |     |           | selected traces   | of HSDPA       | dataset. We | replay  | the      | videos with |
| ------ | -------- | ---- | -------- | --- | ----------- | --- | --------- | ----------------- | -------------- | ----------- | ------- | -------- | ----------- |
| QoE/BW | for each | user | and then | get | the average | of  | all users |                   |                |             |         |          |             |
|        |          |      |          |     |             |     |           | all the evaluated | ABR algorithms | and         | get the | resulted | videos.     |
on that network trace. For all testing network traces, we For the resulted videos, we analyze them and calculate the
| show the | differences |     | between | QoE/BW | for Ruyi | and | the best |                   |      |               |      |       |         |
| -------- | ----------- | --- | ------- | ------ | -------- | --- | -------- | ----------------- | ---- | ------------- | ---- | ----- | ------- |
|          |             |     |         |        |          |     |          | VMAF, rebuffering | time | and switches. | With | these | metrics |
performingcomparisonalgorithmPensieveinFigure12.Ruyi and user QoE models, we calculate the QoE and show the
outperformsPensieve(differences>0)inabout72.3%traces.
|     |     |     |     |     |     |     |     | normalized | QoE (obtained | with Ruyi | as the | standard) | for two |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --------- | ------ | --------- | ------- |
TheaverageQoE/BWacrossalltestingnetworktracesofRuyi
|     |     |     |     |     |     |     |     | typical example | users: User | 30 and User | 41  | in Figure | 13(a). |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | ----------- | --- | --------- | ------ |
and Pensieve are 0.408 and 0.376. That means Ruyi saves User 30 is more sensitive to rebuffering events, while user 41
| 8.51% bandwidth |     | when | achieving | the | same QoE | as  | Pensieve. |                   |         |                 |        |       |       |
| --------------- | --- | ---- | --------- | --- | -------- | --- | --------- | ----------------- | ------- | --------------- | ------ | ----- | ----- |
|                 |     |      |           |     |          |     |           | is more sensitive | to high | visual quality. | Figure | 13(a) | shows |
Furthermore,wecalculatetheaverageQoE/BWofthebaseline
|        |           |          |        |           |     |          |     | that Ruyi | performs the best. | For User    | 30, Pensieve |     | performs |
| ------ | --------- | -------- | ------ | --------- | --- | -------- | --- | --------- | ------------------ | ----------- | ------------ | --- | -------- |
| BB and | find Ruyi | achieves | 20.35% | bandwidth |     | savings. |     |           |                    |             |              |     |          |
|        |           |          |        |           |     |          |     | the worst | due to the longest | rebuffering | time.        | For | User 41, |
2) Testbed Experiment: BB performs the worst due to the lowest VMAF value. This
We evaluate Ruyi and other ABR algorithms on Dash.js. resultshowsthattheABRwithoutspecificQoEmodelsorthe
The network condition is set by tc [22] with the random ABRwithanaverageQoEmodelisnotsufficientandwillnot

|     |                |     |     |     |     |              |     | effective        | method     | to maintain      |            | the buffer   | occupancy  |            | at a safety |
| --- | -------------- | --- | --- | --- | --- | ------------ | --- | ---------------- | ---------- | ---------------- | ---------- | ------------ | ---------- | ---------- | ----------- |
|     |                |     |     |     |     |              |     | range. After     | that,      | ABR              | algorithms |              | which      | combine    | these two   |
|     |                |     |     |     |     |              |     | techniques       | [5],       | [9], [16]        | are        | proposed.    |            | MPC [5]    | employs     |
|     |                |     |     |     |     |              |     | model predictive |            | control          | algorithms |              | that use   | both       | throughput  |
|     |                |     |     |     |     |              |     | estimates        | and        | buffer occupancy |            | information. |            | However,   | MPC         |
|     |                |     |     |     |     |              |     | relies heavily   |            | on accurate      |            | throughput   | estimates  |            | which are   |
|     |                |     |     |     |     |              |     | not always       | available. |                  | Fugu       | [9] is       | proposed   | to improve | the         |
|     |                |     |     |     |     |              |     | performance      | of         | bitrate          | adaptation |              | which      | is based   | on MPC      |
|     |                |     |     |     |     |              |     | but replaces     | its        | throughput       |            | predictor    | with       | a deep     | neural      |
|     |                |     |     |     |     |              |     | network.         | A separate |                  | line of    | work         | is to      | leverage   | RL [43]–    |
|     |                |     |     |     |     |              |     | [46]. These      | schemes    |                  | apply      | RL in        | a “tabular | form”,     | which       |
| (a) | NormalizedQoE. |     |     |     | (b) | Userratings. |     |                  |            |                  |            |              |            |            |             |
|     |                |     |     |     |     |              |     | stores the       | value      | function         | for        | all states   | and        | actions    | explicitly. |
Fig.13. PerformanceofRuyiinDash.js. Pensieve[8]leveragesthedeepRLmethodthatrepresentsthe
|     |     |     |     |     |     |     |     | ABR algorithms |     | as a | neural | network. | This | allows | Pensieve |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------ | -------- | ---- | ------ | -------- |
consistentlyperformwelltowardsvarioususerpreferences.On
average, Ruyi achieves 1.69 times the QoE of Pensieve over to optimize its policy for different network characteristics and
QoEmetricsfromexperience.However,Pensieveistrainedto
| the two | users | (2.23 times | on  | User30, | 1.16 | times | on User41). |     |     |     |     |     |     |     |     |
| ------- | ----- | ----------- | --- | ------- | ---- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
InadditiontotheQoEcalculatedwiththepreference-aware optimizeforapredefinedQoEobjectiveandcannotadjustfor
|             |      |          |          |     |        |                   |            | different      | objectives | online. | MPC    | and  | Pensieve | are | objective- |
| ----------- | ---- | -------- | -------- | --- | ------ | ----------------- | ---------- | -------------- | ---------- | ------- | ------ | ---- | -------- | --- | ---------- |
| QoE models  | and  | the meta | metrics, |     | we let | the corresponding |            |                |            |         |        |      |          |     |            |
|             |      |          |          |     |        |                   |            | based methods, |            | and a   | recent | work | combines | BB  | and RL     |
| users watch | four | videos   | out of   | the | above  | resulted          | videos and |                |            |         |        |      |          |     |            |
rate in five scales. The four videos are generated with a same enabling the objective awareness [47]. We leave the extension
|     |     |     |     |     |     |     |     | of these | works | to support | multi-objective |     |     | as our future | work. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | --------------- | --- | --- | ------------- | ----- |
networktraceandfourevaluatedABRalgorithms.Theratings
are presented in Figure 13(b) which show the same trend as VII. DISCUSSION
the calculated QoE. Influence of content. Regardless of whether user preferences
|     |     | VI. | RELATEDWORK |     |     |     |     |                 |     |       |         |       |       |        |           |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --------------- | --- | ----- | ------- | ----- | ----- | ------ | --------- |
|     |     |     |             |     |     |     |     | are considered, |     | video | content | has a | great | impact | on QoE of |
Video QoE models. Video QoE models has two general users. If the user is interested in the video content, or if the
categories:visualqualityassessment(VQA)whichfocuseson video content is enjoyable, then the user’s tolerance for poor
pixel-level perception of users and QoE models considering qualitywillbehigher.Apreviousworkdoesbitrateadaptation
|                   |     |            |     |                 |     |     |         | with the | consideration |     | of video | content | [48] | for QoE | models |
| ----------------- | --- | ---------- | --- | --------------- | --- | --- | ------- | -------- | ------------- | --- | -------- | ------- | ---- | ------- | ------ |
| streaming-related |     | distortion |     | and perception. |     | VQA | methods |          |               |     |          |         |      |         |        |
include traditional models (e.g. QP [33], PSNR [34], SSIM in additive form. Our work is orthogonal and complementary
[35]) and data-driven models (e.g. VMAF [36], DeepVQA to this, allowing for more fine-grained user-specific bitrate
|                 |     |                   |     |     |        |     |              | adaptive | control. | Furthermore, |     | other | dimensions, |     | such as the |
| --------------- | --- | ----------------- | --- | --- | ------ | --- | ------------ | -------- | -------- | ------------ | --- | ----- | ----------- | --- | ----------- |
| [37]). Besides, |     | streaming-related |     | QoE | models |     | for adaptive |          |          |              |     |       |             |     |             |
streaming videos attract many research efforts. The earliest device, the energy, and the type of videos, considered in user
onesstartwithonlyrebufferingbeingconsideredwhicharenot preference-aware bitrate adaptation are left as future work.
accurate to model user QoE in adaptive streaming [38], [39]. Inapplicable situations. For the form of QoE models which
| After that, | average | bitrate | is  | complemented |     | to  | improve the |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | --- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
arenotadditivewithseveralpresetmetametrics,suchasend-
predictionaccuracyandtheQoEisrepresentedastheweighted to-end learning based QoE models, Ruyi is not applicable
sum of the average bitrate and the rebuffering where the due to the design of directly predicting the impact of current
| trade-off | weights | should | be determined |     | [40], | [41]. | Motivated |         |          |         |        |         |          |     |             |
| --------- | ------- | ------ | ------------- | --- | ----- | ----- | --------- | ------- | -------- | ------- | ------ | ------- | -------- | --- | ----------- |
|           |         |        |               |     |       |       |           | actions | on those | metrics | in the | future. | Instead, | if  | the metrics |
by observations that frequent quality switches degrade users’ that affect the users’ experience are clear, Ruyi will perform
| QoE [42], | some | models | take | quality | switching |     | into account |           |       |            |     |       |        |         |            |
| --------- | ---- | ------ | ---- | ------- | --------- | --- | ------------ | --------- | ----- | ---------- | --- | ----- | ------ | ------- | ---------- |
|           |      |        |      |         |           |     |              | well with | these | QoE models |     | which | occupy | a large | proportion |
[5], [6]. As bitrate is inadequate to model visual perception, and are widely used in modern ABR systems.
| many works | suggest    | to         | replace | the            | average | bitrate  | by video |           |         |                |            |                 |             |     |              |
| ---------- | ---------- | ---------- | ------- | -------------- | ------- | -------- | -------- | --------- | ------- | -------------- | ---------- | --------------- | ----------- | --- | ------------ |
|            |            |            |         |                |         |          |          |           |         | VIII.          | CONCLUSION |                 |             |     |              |
| quality    | assessment | models     | [12],   | [13].          | Thus,   | we       | use VMAF |           |         |                |            |                 |             |     |              |
|            |            |            |         |                |         |          |          | In this   | paper,  | we investigate |            | the differences |             | in  | user prefer- |
| instead    | of bitrate | to improve |         | the prediction |         | accuracy | of the   |           |         |                |            |                 |             |     |              |
|            |            |            |         |                |         |          |          | ences. We | conduct | a user         | study      | with            | 90 subjects | and | find that    |
QoEmodel.Inadditiontotheabovemodels,machinelearning
|          |         |         |                |           |          |        |          | the average | user  | can not   | represent | all  | users.       | Then | we propose |
| -------- | ------- | ------- | -------------- | --------- | -------- | ------ | -------- | ----------- | ----- | --------- | --------- | ---- | ------------ | ---- | ---------- |
| are also | used to | model   | QoE            | [3], [4]. | However, | these  | learning |             |       |           |           |      |              |      |            |
|          |         |         |                |           |          |        |          | Ruyi, a     | video | streaming | system    | that | incorporates |      | preference |
| models   | usually | overfit | the subjective |           | opinion  | scores | and the  |             |       |           |           |      |              |      |            |
performance is affected by the limited users’ scores. awareness into both the QoE model and the ABR algorithm.
|           |               |              |             |     |            |          |                | Our simulation |         | results        | show | that, Ruyi | increases |           | QoE for all |
| --------- | ------------- | ------------ | ----------- | --- | ---------- | -------- | -------------- | -------------- | ------- | -------------- | ---- | ---------- | --------- | --------- | ----------- |
| Adaptive  | bitrate       | (ABR)        | algorithms. |     | The        | earliest | ABR al-        |                |         |                |      |            |           |           |             |
|           |               |              |             |     |            |          |                | users. In      | testbed | experiments,   |      | results    | show      | that Ruyi | has the     |
| gorithms  | can           | be primarily | grouped     |     | into       | two      | classes: rate- |                |         |                |      |            |           |           |             |
|           |               |              |             |     |            |          |                | highest        | ratings | from subjects. |      |            |           |           |             |
| based and | buffer-based. |              | Rate-based  |     | algorithms | [15],    | [16] are       |                |         |                |      |            |           |           |             |
IX. ACKNOWLEDGEMENT
| hindered | by the | biases | present | when | estimating |     | available |     |     |     |     |     |     |     |     |
| -------- | ------ | ------ | ------- | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
bandwidth on top of HTTP. Buffer-based approaches [6], This work was supported by National Key R&D Program
[7] solely consider the client’s playback buffer occupancy of China Grant (No. 2018YFB1802202) and NSFC (No.
when deciding the bitrates. BB [7] leverages a simple but 6213000078 and No. 61872211).

REFERENCES
|     |     |     |     |     |     |     |     | [24] C.Liu,I.Bouazizi,andM.Gabbouj,“Rateadaptationforadaptivehttp |     |                |     |            |        |     |               |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | -------------- | --- | ---------- | ------ | --- | ------------- |
|     |     |     |     |     |     |     |     | streaming,”                                                       |     | in Proceedings | of  | the second | annual | ACM | conference on |
Multimediasystems,2011,pp.169–174.
[1] B.Han,F.Qian,L.Ji,andV.Gopalakrishnan,“Mp-dash:Adaptivevideo
streamingoverpreference-awaremultipath,”inProceedingsofthe12th [25] J. W. Peirce, “Psychopy—psychophysics software in python,” Journal
CoNEXT,2016,pp.129–143. ofneurosciencemethods,vol.162,no.1-2,pp.8–13,2007.
[2] “Cisco annual internet report (2018–2023) white paper.” [26] J.Fowler,L.Cohen,andP.Jarvis,Practicalstatisticsforfieldbiology.
JohnWiley&Sons,2013.
https://www.cisco.com/c/en/us/solutions/collateral/executive-
|     |     |     |     |     |     |     |     | [27] T. Schaul, |     | D. Horgan, | K. Gregor, | and | D.  | Silver, “Universal | value |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ---------- | --- | --- | ------------------ | ----- |
perspectives/annual-internet-report/white-paper-c11-741490.html.
[3] W. Robitza, M.-N. Garcia, and A. Raake, “A modular http adaptive functionapproximators,”inICML,2015,pp.1312–1320.
streamingqoemodel—candidateforitu-tp.1203(“p.nats”),”in2017 [28] A.DosovitskiyandV.Koltun,“Learningtoactbypredictingthefuture,”
ICLR,2017.
| NinthQoMEX. |     | IEEE,2017,pp.1–6. |     |     |     |     |     |                                                                 |     |     |     |     |     |     |     |
| ----------- | --- | ----------------- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|             |     |                   |     |     |     |     |     | [29] Z.Wang,T.Schaul,M.Hessel,H.Hasselt,M.Lanctot,andN.Freitas, |     |     |     |     |     |     |     |
[4] N.Eswara,S.Ashique,A.Panchbhai,S.Chakraborty,H.P.Sethuram,
|           |                 |        |                  |     |            |            |           | “Dueling | network                 | architectures |     | for deep | reinforcement |     | learning,” in |
| --------- | --------------- | ------ | ---------------- | --- | ---------- | ---------- | --------- | -------- | ----------------------- | ------------- | --- | -------- | ------------- | --- | ------------- |
| K. Kuchi, | A. Kumar,       | and S. | S. Channappayya, |     | “Streaming |            | video qoe |          |                         |               |     |          |               |     |               |
|           |                 |        |                  |     |            |            |           | ICML.    | PMLR,2016,pp.1995–2003. |               |     |          |               |     |               |
| modeling  | and prediction: | A      | long short-term  |     | memory     | approach,” | IEEE      |          |                         |               |     |          |               |     |               |
TCSVT,vol.30,no.3,pp.661–673,2019. [30] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
|             |            |           |        |           |                      |     |     | Bellemare, | A.           | Graves, | M. Riedmiller, |         | A. K. | Fidjeland,    | G. Ostrovski |
| ----------- | ---------- | --------- | ------ | --------- | -------------------- | --- | --- | ---------- | ------------ | ------- | -------------- | ------- | ----- | ------------- | ------------ |
| [5] X. Yin, | A. Jindal, | V. Sekar, | and B. | Sinopoli, | “A control-theoretic |     | ap- |            |              |         |                |         |       |               |              |
|             |            |           |        |           |                      |     |     | et al.,    | “Human-level |         | control        | through | deep  | reinforcement | learning,”   |
proachfordynamicadaptivevideostreamingoverhttp,”inProceedings
Nature,vol.518,no.7540,pp.529–533,2015.
ofthe2015ACMSIGCOMM,2015,pp.325–338.
|                 |               |     |        |               |        |              |     | [31] M.Abadi,P.Barham,J.Chen,Z.Chen,A.Davis,J.Dean,M.Devin, |     |     |     |     |     |     |     |
| --------------- | ------------- | --- | ------ | ------------- | ------ | ------------ | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| [6] K. Spiteri, | R. Urgaonkar, |     | and R. | K. Sitaraman, | “Bola: | Near-optimal |     |                                                             |     |     |     |     |     |     |     |
bitrate adaptation for online videos,” in INFOCOM 2016-The 35th S.Ghemawat,G.Irving,M.Isardetal.,“Tensorflow:Asystemforlarge-
scalemachinelearning,”in12thUSENIXOSDI’16,2016,pp.265–283.
| Annual | IEEE International |     | Conference | on  | Computer | Communications, |     |                |      |          |         |           |                |     |                 |
| ------ | ------------------ | --- | ---------- | --- | -------- | --------------- | --- | -------------- | ---- | -------- | ------- | --------- | -------------- | --- | --------------- |
|        |                    |     |            |     |          |                 |     | [32] “Tflearn: | Deep | learning | library | featuring | a higher-level |     | api for tensor- |
| IEEE.  | IEEE,2016,pp.1–9.  |     |            |     |          |                 |     |                |      |          |         |           |                |     |                 |
flow,2017,”http://tflearn.org/.
| [7] T.-Y.       | Huang, R. | Johari, N. | McKeown, | M.          | Trunnell, | and M. | Watson, |               |                 |     |     |      |           |       |            |
| --------------- | --------- | ---------- | -------- | ----------- | --------- | ------ | ------- | ------------- | --------------- | --- | --- | ---- | --------- | ----- | ---------- |
|                 |           |            |          |             |           |        |         | [33] H. ITU-T | RECOMMENDATION, |     |     | “264 | “advanced | video | coding for |
| “A buffer-based |           | approach   | to rate  | adaptation: | Evidence  | from   | a large |               |                 |     |     |      |           |       |            |
genericaudiovisualservices”,”2003.
video streaming service,” in Proceedings of the 2014 ACM conference [34] A. Hore and D. Ziou, “Image quality metrics: Psnr vs. ssim,” in 2010
onSIGCOMM,2014,pp.187–198.
|     |     |     |     |     |     |     |     | 20thinternationalconferenceonpatternrecognition. |     |     |     |     |     | IEEE,2010,pp. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- |
[8] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream-
2366–2369.
ingwithpensieve,”inProceedingsofthe2017ACMSIGCOMM,2017,
|     |     |     |     |     |     |     |     | [35] Z. Wang, | A.  | C. Bovik, | H. R. | Sheikh, | and E. | P. Simoncelli, | “Image |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ----- | ------- | ------ | -------------- | ------ |
pp.197–210.
|     |     |     |     |     |     |     |     | quality | assessment: | from | error | visibility | to structural | similarity,” | IEEE |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ---- | ----- | ---------- | ------------- | ------------ | ---- |
[9] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis, transactionsonimageprocessing,vol.13,no.4,pp.600–612,2004.
| and K. | Winstein,“Learning |     | in situ: | a randomizedexperiment |     |     | in video |             |     |             |     |     |            |     |          |
| ------ | ------------------ | --- | -------- | ---------------------- | --- | --- | -------- | ----------- | --- | ----------- | --- | --- | ---------- | --- | -------- |
|        |                    |     |          |                        |     |     |          | [36] “Video |     | multimethod |     |     | assessment |     | fusion.” |
streaming,”inNSDI20,2020,pp.495–511.
https://github.com/Netflix/vmaf.
[10] Z.Duanmu,W.Liu,D.Chen,Z.Li,Z.Wang,Y.Wang,andW.Gao,“A
|                  |     |                       |     |       |     |          |           | [37] W.   | Kim, J. | Kim, S.         | Ahn, J. | Kim, and | S. Lee,     | “Deep | video quality |
| ---------------- | --- | --------------------- | --- | ----- | --- | -------- | --------- | --------- | ------- | --------------- | ------- | -------- | ----------- | ----- | ------------- |
| knowledge-driven |     | quality-of-experience |     | model | for | adaptive | streaming |           |         |                 |         |          |             |       |               |
|                  |     |                       |     |       |     |          |           | assessor: | From    | spatio-temporal |         | visual   | sensitivity | to a  | convolutional |
videos,”arXivpreprintarXiv:1911.07944,2019. neuralaggregationnetwork,”inECCV,2018,pp.219–234.
[11] Y. Zhu, A. Hanjalic, and J. A. Redi, “Qoe prediction for enriched [38] K. Watanabe, J. Okamoto, and T. Kurita, “Objective video quality
| assessment | of individual | video | viewing | experience,” |     | in Proceedings |     | of  |     |     |     |     |     |     |     |
| ---------- | ------------- | ----- | ------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assessmentmethodforevaluatingeffectsoffreezedistortioninarbitrary
the24thACMMM,2016,pp.801–810.
videoscenes,”inImageQualityandSystemPerformanceIV,vol.6494.
[12] A.Bentaleb,A.C.Begen,andR.Zimmermann,“Sdndash:Improving
InternationalSocietyforOpticsandPhotonics,2007,p.64940P.
qoe of http adaptive streaming using software defined networking,” in [39] R.K.Mok,X.Luo,E.W.Chan,andR.K.Chang,“Qdash:aqoe-aware
Proceedingsofthe24thACMinternationalconferenceonMultimedia, dashsystem,”inProceedingsofthe3rdMMSys,2012,pp.11–22.
2016,pp.1296–1305.
|     |     |     |     |     |     |     |     | [40] X.Liu,F.Dobrian,H.Milner,J.Jiang,V.Sekar,I.Stoica,andH.Zhang, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
[13] Z.Duanmu,K.Zeng,K.Ma,A.Rehman,andZ.Wang,“Aquality-of-
“Acaseforacoordinatedinternetvideocontrolplane,”inProceedings
experienceindexforstreamingvideo,”IEEEJournalofSelectedTopics oftheACMSIGCOMM2012,2012,pp.359–370.
inSignalProcessing,vol.11,no.1,pp.154–166,2016. [41] J.Xue,D.-Q.Zhang,H.Yu,andC.W.Chen,“Assessingqualityofex-
[14] Y.Zhu,S.C.Guntuku,W.Lin,G.Ghinea,andJ.A.Redi,“Measuring perienceforadaptivehttpvideostreaming,”in2014IEEEInternational
individualvideoqoe:Asurvey,andproposalforfuturedirectionsusing ConferenceonMultimediaandExpoWorkshops(ICMEW). IEEE,2014,
socialmedia,”TOMM,2018.
pp.1–6.
[15] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and [42] P.Ni,R.Eg,A.Eichhorn,C.Griwodz,andP.Halvorsen,“Flickereffects
stabilityinhttp-basedadaptivevideostreamingwithfestive,”IEEE/ACM inadaptivevideostreamingtohandhelddevices,”inProceedingsofthe
TransactionsonNetworking(TON),vol.22,no.1,pp.326–340,2014. 19thACMinternationalconferenceonMultimedia,2011,pp.463–472.
[16] Y. Sun, X. Yin, J. Jiang, V. Sekar, F. Lin, N. Wang, T. Liu, and [43] F. Chiariotti, S. D’Aronco, L. Toni, and P. Frossard, “Online learning
B. Sinopoli, “Cs2p: Improving video bitrate selection and adaptation adaptationstrategyfordashclients,”in7thMMSys. ACM,2016,p.8.
with data-driven throughput prediction,” in Proceedings of the 2016 [44] M. Claeys, S. Latre´, J. Famaey, T. Wu, V. Leekwijck, D. Turck et al.,
ACMSIGCOMMConference. ACM,2016,pp.272–285. “Designofaq-learning-basedclientqualityselectionalgorithmforhttp
[17] D. M. Roijers, P. Vamplew, S. Whiteson, and R. Dazeley, “A survey adaptive video streaming,” in Proceedings of the 2013 Workshop on
of multi-objective sequential decision-making,” Journal of Artificial Adaptive and Learning Agents (ALA), Saint Paul (Minn.), USA, 2013,
| IntelligenceResearch,vol.48,pp.67–113,2013. |     |     |     |     |     |     |     | pp.30–37. |         |            |            |     |        |                |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | ---------- | --- | ------ | -------------- | --- |
|                                             |     |     |     |     |     |     |     | [45] M.   | Claeys, | S. Latre´, | J. Famaey, | T.  | Wu, W. | Van Leekwijck, | and |
[18] M.I.JordanandD.E.Rumelhart,“Forwardmodels:Supervisedlearning
with a distal teacher,” Cognitive science, vol. 16, no. 3, pp. 307–354, F. De Turck, “Design and optimisation of a (fa) q-learning-based http
1992. adaptivestreamingclient,”ConnectionScience,vol.26,no.1,pp.25–43,
| [19] C. G. | Bampis, Z. | Li, I. Katsavounidis, |     | T.-Y. | Huang, | C. Ekanadham, |     | 2014. |     |     |     |     |     |     |     |
| ---------- | ---------- | --------------------- | --- | ----- | ------ | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
andA.C.Bovik,“Towardsperceptuallyoptimizedend-to-endadaptive [46] J.vanderHooft,S.Petrangeli,M.Claeys,J.Famaey,andF.DeTurck,
“Alearning-basedalgorithmforimprovedbandwidth-awarenessofadap-
videostreaming,”arXivpreprintarXiv:1808.03898,2018.
[20] Y.Wang,S.Inguva,andB.Adsumilli,“Youtubeugcdatasetforvideo tivestreamingclients,”in IntegratedNetworkManagement(IM),2015
compression research,” in 2019 IEEE 21st International Workshop on IFIP/IEEEInternationalSymposiumon. IEEE,2015,pp.131–138.
MultimediaSignalProcessing(MMSP). IEEE,2019,pp.1–5. [47] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick:
[21] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute A harmonious fusion of buffer-based and learning-based approach for
|                                |     |             |              |                      |          |                    |     | adaptive                | streaming,” | in  | IEEE | INFOCOM                 | 2020-IEEE |     | Conference on |
| ------------------------------ | --- | ----------- | ------------ | -------------------- | -------- | ------------------ | --- | ----------------------- | ----------- | --- | ---- | ----------------------- | --------- | --- | ------------- |
| path bandwidth                 |     | traces from | 3g networks: |                      | analysis | and applications,” |     |                         |             |     |      |                         |           |     |               |
|                                |     |             |              |                      |          |                    |     | ComputerCommunications. |             |     |      | IEEE,2020,pp.1967–1976. |           |     |               |
| inProceedingsofthe4thACMMMSys. |     |             |              | ACM,2013,pp.114–118. |          |                    |     |                         |             |     |      |                         |           |     |               |
[22] “tc: Linux advanced routing and traffic control.” http: [48] X.Zhang,Y.Ou,S.Sen,andJ.Jiang,“Sensei:Aligningvideostreaming
//lartc.org/lartc.html. qualitywithdynamicusersensitivity,”NSDI,2021.
[23] “Dash.js,”https://github.com/Dash-Industry-Forum/dash.js/wiki.