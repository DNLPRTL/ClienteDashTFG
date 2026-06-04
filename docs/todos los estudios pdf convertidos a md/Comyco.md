1
Quality-aware Neural Adaptive Video Streaming
with Lifelong Imitation Learning
Tianchi Huang, Chao Zhou, Xin Yao, Rui-Xiao Zhang, Chenglei Wu, Bing Yu, Lifeng Sun
Abstract—Existing Adaptive Bitrate (ABR) algorithms pick to generalize the strategies without any presumptions, and
future video chunks’ bitrates via fixed rules or offline trained thus, providing a feasible method to solve the ABR task from
models to ensure good quality of experience (QoE) for Internet
another perspective.
video.Nevertheless,dataanalysisdemonstratesthatagoodABR
While previous work has demonstrated considerable QoE
algorithmisrequiredtocontinuallyandfastupdateforadapting
itself to time-varying network conditions. Therefore, we propose improvement in a different manner, in this study, we attempt
Comyco, a video quality-aware learning-based ABR approach tounderstandwhethercurrentABRmethodshavealreadybeen
thatenormouslyimprovesrecentschemesbyi)pickingthechunk satisfied with nowadays’ network (§II). We, therefore, collect
withhigherperceptualvideoqualitiesratherthanvideobitrates;
alargecorpusofnetworktraces(Kwaidataset)ontheleading
ii) training the policy via imitating expert trajectories given by
video streaming platform Kuaishou [16] (§II-B). The analysis
the expert strategy; iii) employing the lifelong learning method
to continually train the model w.r.t the fresh trace collected by shows that 1) more than 80% of network traces require an
the users. To achieve this, we develop a complete quality-aware adaptive streaming method to ensure high QoE. 2) learning-
lifelong imitation learning-based ABR system, construct quality- based ABR approach (i.e., Pensieve [12]) is often required
basedneuralnetworkarchitecture,collectaquality-drivenvideo
to be trained from scratch for over 4 hours. However, the
dataset, and estimate QoE metrics with video quality features.
networkdistributionhaschangeddramaticallyduringthetime
Using trace-driven and real-world experiments, we demonstrate
Comycoreaches1700×improvementsinthenumberofsamples of training convergence. As a result, the algorithm, trained
requiredand16×speedupinthetrainingtimecomparedwiththe on past network scenarios, may hardly provide comparable
prior work. Meanwhile, Comyco outperforms existing methods, performancesunderthecurrentnetworkcondition.3)asmuch
with the improvements on average QoE of 7.5%-16.79%. More-
as the overall network condition shows different throughput
over, experimental results on continual training also illustrate
distribution at large time intervals, it changes slowly and
thatlifelonglearninghelpsComycofurtherimprovetheaverage
QoEof1.07%-9.81%incomparisontotheofflinetrainedmodel. smoothly with time. Hence, learning-based ABR algorithms
should be updated effectively and efficiently for smoothing
the vibration of network conditions. To achieve this goal, we
Index Terms—Imitation Learning, Quality-aware, Lifelong
Learning, Adaptive Video Streaming. summarize the challenges from the following perspectives:
(cid:46) How to implement a quality-aware ABR system? The
I. INTRODUCTION majority of existing ABR approaches [10], [12], [17] place
less importance on the video quality information, while per-
Recent years have witnessed a tremendous increase in
ceptual video quality is a non-trivial feature for evaluating
the requirements of watching online videos [1]. Adaptive
QoE (§V-A, [18]). Consequently, even though these schemes
bitrate(ABR)streaming,themethodthatdynamicallycontrols
have achieved higher QoE objectives, they may generate the
the video player to download different bitrate video for the
strategy diverging from the actual demand. (§III-A)
next chunk, has become a leading scheme to deliver video
(cid:46)Howtoempowerthetrainingefficiencyforlearning-based
streaming services with high quality of experience (QoE) to
ABR algorithms? Recent Reinforcement Learning (RL)-based
the users [2]. Recently, ABR technologies have been widely
ABR schemes [12], [13] lack the efficiency of both collected
used by YouTube [3], Netflix [4], and iQiyi [5]. Existing
and exploited expert samples, which leads to the inefficient
model-based ABR approaches (§VIII) pick the next chunk’s
training [19]. (§III-B)
video bitrate via only current network status [6], [7], or
(cid:46) How to achieve continual learning for the ABR sys-
buffer occupancy [8], [9], or joint consideration of these two
tem? Learning-based ABR methods should be incrementally
factors [10], [11]. However, such heuristics are usually set up
updated with fresh network traces, and in the meanwhile, the
with presumptions, that fail to work well under unexpected
selected traces should be less but critical enough to represent
networkconditions[12].Thus,severalattempts,i.e.,learning-
bandwidth distributions of the current network. (§III-C)
based ABR algorithms, have been made to adopt reinforce-
We find an opportunity to address the last two issues in
ment learning (RL) [12]–[14] or self-learning method [15]
real-world network environments by leveraging the concept
T.Huang,X.Yao,RXZhang,C.Wu,andL.SunarewiththeDepartment of lifelong imitation learning. On the one hand, imitation
ofComputerScienceandTechonology,TsinghuaUniversity,Beijing,100084,
learning enables the ABR system to achieve fast training. On
China.(e-mail:{htc19,yaox16,zhangrx17,wucl18}@mails.tsinghua.edu.cn,
sunlf@tsinghua.edu.cn) the other hand, a lifelong learning method allows the neural
C. Zhou, and B. Yu, are with Beijing Kuaishou Technology Co., Ltd, network(NN)tocontinuallyintegratetheevolutioninnetwork
Beijing,China.(e-mail:{zhouchao,yubing}@kuaishou.com)
(cid:0) Lifeng Sun, Chao Zhou are the corresponding authors. (e-mail: distributions into the passing time. Meanwhile, quality-aware
sunlf@tsinghua.edu.cn,zhouchao@kuaishou.com) learning-based ABR algorithm is still challenging since the

2
state-of-the-art learning-based scheme [12], [15] lacks almost Playback Buffer
Download
| all the modules |     | of constructing |     | a quality-aware |     | ABR system, |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thatincludes,viableneuralnetworkmodels,feasibleandhigh-
efficiency training methodologies, dedicated video datasets Throughput
| based on | video | quality | metrics, | and quality-based |     | QoE | meth- |     |     |     |         |     |     |     |     |
| -------- | ----- | ------- | -------- | ----------------- | --- | --- | ----- | --- | --- | --- | ------- | --- | --- | --- | --- |
| ods.     |       |         |          |                   |     |     |       |     |     |     | Request |     |     |     |     |
ABR Algorithms
Following this insight, we propose Comyco, a novel video Next chunk’s  bitrate
|               |               |     |           |                |     |             |     |            | Server   |         |          |       |            | Client |               |
| ------------- | ------------- | --- | --------- | -------------- | --- | ----------- | --- | ---------- | -------- | ------- | -------- | ----- | ---------- | ------ | ------------- |
| quality-aware | lifelong      |     | imitation | learning-based |     | ABR system, |     |            |          |         |          |       |            |        |               |
| aiming        | to remarkably |     | improve   | the overall    |     | performance | of  |            |          |         |          |       |            |        |               |
|               |               |     |           |                |     |             |     | Fig. 1. An | overview | of HTTP | adaptive | video | streaming. |        | The system is |
ABR algorithms via tackling the above challenges. Different comprisedofavideoserverandavideoclient.ABR,placedontheclientside,
isanalgorithmthatdeterminesnextchunks’bitratesw.r.tpastthroughputand
frompreviouswork[12],Comycoisquality-awareandmainly
currentbufferoccupancy.
composedoftheinner-loopsystemandtheouter-loopsystem,
| and is equipped |     | with the | following | properties |     | (§IV): |     |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | --------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:46) Comyco aims to select bitrate with high perceptual video proposed method further improve the average QoE of 1.07%-
quality rather than high video bitrate. To achieve this goal, 9.81% compared with the offline fixed model (§VI-B3).
we first integrate the information of video contents, network Meanwhile, we further analyze the performance comparison
|             |       |          |        |      |              |     |     | of Comyco | and | state-of-the-art |     | model-based |     | ABR | approach |
| ----------- | ----- | -------- | ------ | ---- | ------------ | --- | --- | --------- | --- | ---------------- | --- | ----------- | --- | --- | -------- |
| status, and | video | playback | states | into | the Comyco’s | NN  | for |           |     |                  |     |             |     |     |          |
bitrate selection (§IV-A1). Next, we use VMAF [20], a state- RobustMPC [10], and we find that lifelong Comyco can auto-
of-the-artmachinelearning-basedobjectivefull-referenceper- matically adapt to the complicated environment and stochas-
ceptual video quality metric, to measure the video quality. tic property in various network conditions. The comparison
Meanwhile, we propose a linearity quality-based QoE metric between lifelong Comyco and the online optimal policy il-
|     |     |     |     |     |     |     |     | lustrates | that the | proposed | scheme |     | has almost | achieved | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | ------ | --- | ---------- | -------- | --- |
thatachievesthestate-of-artperformanceonWaterlooStream-
ingSQoE-III[21]dataset(§V-A).Finally,wecollectaDASH- near-optimal performance (§VI-B5).
video dataset with various types of videos (§V-B). Contribution. We summarize the contributions as follows:
(cid:46) Comyco utilizes the inner-loop system (§IV-A), which • Using data-driven analysis, we identify the short-comings
leverages imitation learning [22] for training the neural of today’s ABR schemes and propose Comyco, a video
| network | (NN). Since | the | near-optimal | policy | can | be precisely |     |     |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------------ | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
quality-awarelifelonglearning-basedABRsystem,thatsig-
and instantly estimated via the current state in the ABR nificantly ameliorates the weakness of the learning-based
scenario, the collected expert policies can enable the NN for (§III).
|     |     |     |     |     |     |     |     | ABR | schemes | from | several | perspectives |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------- | ------------ | --- | --- | --- |
fast learning. The agent is allowed to explore the environment • Unlikepriorwork,Comycopicksthevideochunkwithhigh
andlearnthepolicyviatheexpertpoliciesgivenbythesolver. perceptual video qualities instead of high video bitrates.
| (cid:46) Comyco | adopts | the | outer-loop | system | (§IV-B) | to achieve |     |             |     |         |                  |     |     |             |        |
| --------------- | ------ | --- | ---------- | ------ | ------- | ---------- | --- | ----------- | --- | ------- | ---------------- | --- | --- | ----------- | ------ |
|                 |        |     |            |        |         |            |     | Experiments |     | results | also demonstrate |     | the | superiority | of our |
continual learning. We consider the process of continuous proposed algorithm (§III-A,§IV).
adaptation to network status as a lifelong learning process. To the best of our knowledge, we are the first to leverage
•
The key idea is to filter out the useful traces collected from imitationlearningtoacceleratethetrainingprocessforABR
the client, and periodically update the NN via the inner- tasks.Resultsshowthatexploringimitationlearningcannot
| loop system | and   | learn | the strategies | using | Learning | without |     |              |     |                |            |     |      |         |             |
| ----------- | ----- | ----- | -------------- | ----- | -------- | ------- | --- | ------------ | --- | -------------- | ---------- | --- | ---- | ------- | ----------- |
|             |       |       |                |       |          |         |     | only achieve |     | sample         | efficiency | but | also | improve | the overall |
| Forgetting  | (LwF) | [23]  | method.        |       |          |         |     | performance  |     | (§IV-A,§VI-A). |            |     |      |         |             |
Furthermore, we evaluate Comyco’s inner-loop and outer- We consider the continuous updating task of ABR as a
•
loop system via trace-driven and real-world experiments. Us- lifelong learning process. Results demonstrate that adopting
ing trace-driven emulation (§VI-A2), we find that Comyco lifelong learning enables the ABR algorithm to effectively
| significantly | accelerates |           | the  | training      | process,   | with     | 1700× |       |               |                         |         |            |     |                |     |
| ------------- | ----------- | --------- | ---- | ------------- | ---------- | -------- | ----- | ----- | ------------- | ----------------------- | ------- | ---------- | --- | -------------- | --- |
|               |             |           |      |               |            |          |       | adapt | the time-vary |                         | network | conditions |     | (§IV-B,§VI-B). |     |
| improvements  | in          | terms     | of a | number        | of samples | required |       |       |               |                         |         |            |     |                |     |
| compared      | to the      | recent    | work | (§VI-A3),     | and 16×    | speedup  | on    |       |               |                         |         |            |     |                |     |
|               |             |           |      |               |            |          |       |       | II.           | BACKGROUNDANDMOTIVATION |         |            |     |                |     |
| the training  | time.       | Comparing |      | with existing | schemes,   | Comyco   |       |       |               |                         |         |            |     |                |     |
Inthissection,webeginbyintroducingABR’sbackground.
| outperforms      | them    | under          | various | network      | conditions | (§VI-A2) |      |                 |          |             |             |           |               |         |            |
| ---------------- | ------- | -------------- | ------- | ------------ | ---------- | -------- | ---- | --------------- | -------- | ----------- | ----------- | --------- | ------------- | ------- | ---------- |
|                  |         |                |         |              |            |          |      | Then we         | analyze  | today’s     | ABR         | services. | Finally,      | we      | highlight  |
| and videos       | (§V-B), | with           | the     | improvements | on         | average  | QoE  |                 |          |             |             |           |               |         |            |
|                  |         |                |         |              |            |          |      | the limitations |          | of strawman | solutions   |           | for ABR       | schemes | with-      |
| of 7.5%-16.79%.  |         | In particular, |         | Comyco       | performs   | better   | than |                 |          |             |             |           |               |         |            |
|                  |         |                |         |              |            |          |      | out lifelong    | learning |             | and present |           | key insights  | that    | lead to    |
| state-of-the-art |         | learning-based |         | approach     | Pensieve   | [12],    | with |                 |          |             |             |           |               |         |            |
|                  |         |                |         |              |            |          |      | implementing    |          | a new ABR   | system      |           | for providing |         | better QoE |
theimprovementsontheaveragevideoqualityof7.37%under
|     |     |     |     |     |     |     |     | to the users | at  | any time. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
thesamerebufferingtime.Further,wereportresultsthathigh-
| light Comyco’s |           | performance |           | with different | hyper-parameters |                |     |        |          |     |     |     |     |     |     |
| -------------- | --------- | ----------- | --------- | -------------- | ---------------- | -------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
|                |           |             |           |                |                  |                |     | A. ABR | Overview |     |     |     |     |     |     |
| and settings   | (§VI-A5). |             | Extensive | results        | over             | the real-world |     |        |          |     |     |     |     |     |     |
network scenarios indicate the superiority of Comyco over Duetotherapiddevelopmentofnetworkservices,watching
existing state-of-the-art approaches (§VI-A6). Moreover, we videos online has already become a common trend. Today,
alsodiscusstheperformanceoftheouter-loopsystem,namely the predominant form for video delivery is adaptive video
lifelong Comyco (§VI-B). Experimental results demonstrate streaming, such as HLS (HTTP Live Streaming) [24] and
that the using outer-loop system can effectively help the DASH [25], which is a method that dynamically selects

3
1.0
0.8
0.6
0.4
0.2
0.0
0 2 4 6 8 10
Average Throughput (Mbps)
FDC
1.0
0.8
Highest Bitrate for 0.6 HD Videos
0.4
0.2
Day1-Day7
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Prediction Error
(a) CDFofsessionthroughput.
FDC
1.0
0.8
The performance of 0.6 heuristic ABRs
degrades 0.4
0.2
Day-Day7
0.0
0 2 4 6 8 10
Average Throughput
(b) CDFofpredictionerror.
Fig. 2. An overview of Kwai dataset, including the distribution of average
throughput and throughput’s prediction error using popular throughput pre-
dictionmethod[7].
video bitrates according to network conditions and clients’
buffer occupancy. As shown in Figure 1, the traditional video
streaming framework consists of a video player client with
a constrained buffer length and an HTTP-Server or Content
DeliveryNetwork(CDN)[7].Thevideoplayerclientdecodes
and renders video frames from the playback buffer. Once the
streaming service starts, the client fetches the video chunk
from the HTTP Server or CDN in order by an ABR algo-
rithm. Meanwhile, the algorithm, deployed on the client-side,
determinesthenextchunkN andthenextchunkvideoquality
Q via throughput estimation and current buffer utilization.
N
The goal of the ABR algorithm is to provide the video chunk
withhighqualitiesandavoidstallingorrebufferingevents[2].
B. Analysis for Today’s ABR Services
Our work starts with a realistic problem: with the rapid
improvements of today’s network bandwidth, are ABR algo-
rithms still necessary for video streaming services to provide
betterQoEtotheusers?Toanswerthisquestion,werequirea
fresh throughput dataset in large-scale, continuous throughput
measurements, and long session duration. However, revisiting
previously proposed public throughput trace datasets [17],
[26], [27], we observe that such existing datasets lack either
the diversity of throughput traces or the continuous measure-
ment through the entire weeks, which finally unable to use
them directly for research purpose 1. To this end, we collect
a large-scale network bandwidth dataset, namely Kwai, from
the video streaming viewers of Kuaishou [16]. Kuaishou is
a leading video streaming platform in China that has over
300 million users worldwide. The dataset consists of over 86
thousand traces from 9,941 users, 7 days in total (1104 hours
in terms of overall bandwidth time recorded.) from various
networkconditionscollectedinJune2019.Thenweutilizethe
Kwai dataset to implement several experiments for answering
the questions above and dedicate several observations.
(cid:46)Observation1.ExperimentsillustratethatABRalgorithms
are still necessary for 80% of today’s network conditions.
Meanwhile,thestate-of-the-artheuristicmethodMPC(Model
PredictiveControl)[10]onlyperformswellunderalmost40%
of all sessions.
To better investigate the importance of ABR algorithms for
today’s network, we compute average throughput on all the
1It’snotablethatCS2P’snetworkdataset[5]isfitforourwork,butitstill
hasnotbeenpublishedyet(Jan.2020).
FDC 0.95 Train
HSDPA 0.85
Oboe
Kwai
0.75
Kwai Oboe HSDPA
(a) CDFofsessionthroughputondif-
ferentnetworktraces
EoQ
dezilamroN
RobustMPC Pensieve(train in situ)
Pensieve
(b) Normalized QoE on the selected
networkenvironments
Fig.3. Comparingthethroughputdistributionondifferentnetworkdatasets.
We also report normalized QoE on each network dataset. It’s notable that
Pensieve’strainingtimelastsabout8hours.
sessions of the Kwai dataset and report them as the CDF
distributionplotinFigure2.Figure2(a)shows,assumingthat
the highest video bitrate of per chunks is 4.3Mbps 2, we find
that over 80% of sessions require ABR algorithms to adjust
nextchunk’sbitrateforavoidingrebufferingeventsiftheusers
prefer watching the video with the highest bitrates since the
average bandwidth of the client is lower than the chunk with
the highest bitrate. Moreover, recent work [10] demonstrates
that MPC’s performance heavily depends on the throughput
accuracy. If the throughput’s prediction error is over 20%,
MPC will be performed under 85% of optimal QoE. Thus,
we also illustrate the CDF distribution of prediction error in
Figure 2(b), where the prediction error is computed as mean
absolute percentage error (MAPE). Surprisingly, over 60%
of sessions gain a large prediction error (over 20%), which
means, existing heuristics fail to guarantee the performance
of 40% sessions. To this end, we aim to use learning-based
ABRalgorithmratherthanheuristicsforachievingbetterQoE.
(cid:46) Observation2. Measurements show the network distri-
bution will be different if the time gap lasts over 6 hours.
However, the training time of recent learning-based ABR
algorithmsisintherangeof4-23hours[12],[13].Hence,the
learned strategy (trained on previous network distributions)
may perform poorly on current network conditions.
Notethatrecentclient-basedABRsoftentrained[12]orde-
signed [10], [28] once and deployed on the users’ client with-
outanyfurtherchanges.Suchobservationleadstoanothercrit-
ical question: can ABRs tame the complexity of dynamic net-
workconditionswithoutupdating?We,therefore,evaluatethe
performance of existing ABR algorithms (i.e., Pensieve [12],
RobustMPC [10] and Pensieve (train in situ [29])) over dif-
ferent network conditions, including HSDPA, Oboe (§VI-A2)
and Kwai, on the virtual player (§VI-A2). In detail, we train
Pensieveonthetrainingset,providedbytheoriginalPensieve
work [30] and validate it on the various network traces with
the same trained model. In contrast, Pensieve (train in situ)
means we train and validate Pensieve on the same network
condition. Results on Figure 3(b) elaborate that 1) the overall
performance of Pensieve heavily rely on the similarity of
the throughput distribution between the training set and the
validation network environments (see more in Figure 3(a)),
and 2) learning Pensieve in situ always outperforms others
2It’sastandard-settingforHD(1080p)videos[12],[17]

4
| 1.0     |     |      | 1.0     |     |     |            | 1.0     |     |            |     | 1.0     |     |            |     |
| ------- | --- | ---- | ------- | --- | --- | ---------- | ------- | --- | ---------- | --- | ------- | --- | ---------- | --- |
| 0.8     |     |      | 0.8     |     |     |            | 0.8     |     |            |     | 0.8     |     |            |     |
| FDC 0.6 |     |      | FDC 0.6 |     |     |            | FDC 0.6 |     |            |     | FDC 0.6 |     |            |     |
|         |     | Day1 |         |     |     |            |         |     | Day1 16:00 |     |         |     | Day1 20:00 |     |
| 0.4     |     | Day2 | 0.4     |     |     | Day1 04:00 | 0.4     |     | Day2 16:00 |     | 0.4     |     | Day1 21:00 |     |
| 0.2     |     | Day3 | 0.2     |     |     | Day1 10:00 | 0.2     |     | Day3 16:00 |     | 0.2     |     | Day1 22:00 |     |
|         |     | Day4 |         |     |     | Day1 20:00 |         |     | Day4 16:00 |     |         |     | Day1 23:00 |     |
0.0 0 2 4 6 8 10 0.0 0 2 4 6 8 10 0.0 0 2 4 6 8 10 0.0 0 2 4 6 8 10
Average Throughput (Mbps) Average Throughput (Mbps) Average Throughput Average Throughput
(a) Day. (b) Representativetime. (c) Daywithadesignatedtime. (d) Continuoushours.
Fig.4. CDFofsessionthroughputbycontinuousday,representativetime,specifictime,aswellascontinuoustime.
underallconsiderednetworkenvironments.Hence,webelieve imitation learning (§III-B), and how to deploy the system for
that the learning-based ABR algorithm has plenty of room lifelong updating (§III-C).
for improvement, e.g., narrowing the difference between the While previous work attempts to solve the ABR problem
distribution of the training set and testing set. withdifferentmanner(§VIII),existingABRschemestypically
So,doestoday’snetworkemergethesamenetworkdistribu- suffer from several issues. To that end, we summarize the key
tion at different times? Figure 4(a) illustrates the CDF of the challenges as follows:
averagethroughputfromJune1toJune4.Wefindthatthere’s
no obvious difference between the throughput distribution on A. Challenges for Perceptual Video Quality-aware ABRs
| each day. | Thus, we further | discuss | the | throughput | distribution |     |          |         |     |         |      |             |      |         |
| --------- | ---------------- | ------- | --- | ---------- | ------------ | --- | -------- | ------- | --- | ------- | ---- | ----------- | ---- | ------- |
|           |                  |         |     |            |              |     | Previous | popular | ABR | schemes | [5], | [10], [12], | [17] | are of- |
with three representative times on the same day, where the ten evaluated by typical QoE objectives that use the combina-
| time represents | the sleeping |     | time, working |     | time, and | resting |     |     |     |     |     |     |     |     |
| --------------- | ------------ | --- | ------------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionofvideobitrates,rebufferingtimesandvideosmoothness.
time, respectively. Results are shown in Figure 4(b), and we However, such QoE metrics are short-handed because these
can see that the network distribution is strongly correlated forms of parameters neglect the quality of video presenta-
| with human | behavior. | For example, |     | the average | throughput |     |             |            |     |        |            |      |           |      |
| ---------- | --------- | ------------ | --- | ----------- | ---------- | --- | ----------- | ---------- | --- | ------ | ---------- | ---- | --------- | ---- |
|            |           |              |     |             |            |     | tions [31]. | Meanwhile, |     | recent | work [32], | [33] | has found | that |
in the night (20:00) is lower than that in the morning (10:00). perceptualvideoqualityfeaturesplayavitalpartinevaluating
| Technically, | Pensieve | takes over | 4-8 | hours (or | 120-200 | thou- |                 |     |                |     |     |           |           |     |
| ------------ | -------- | ---------- | --- | --------- | ------- | ----- | --------------- | --- | -------------- | --- | --- | --------- | --------- | --- |
|              |          |            |     |           |         |       | the performance |     | of VBR-encoded |     | ABR | streaming | services. |     |
sand iterations) to train a reliable strategy on current network To better understand the difference between the quality-
distributions. Thus, although its training time is rather short aware and the bitrate-aware ABR scheme, we report the
| compared | with other | learning-based |     | ABRs | [15], we | believe |            |           |     |        |             |     |        |       |
| -------- | ---------- | -------------- | --- | ---- | -------- | ------- | ---------- | --------- | --- | ------ | ----------- | --- | ------ | ----- |
|          |            |                |     |      |          |         | trajectory | generated |     | by the | two methods | in  | Figure | 5, in |
that the current strategy, i.e., training a NN from scratch in 4 which the perceptual quality is measured by Video Multi-
hours, doesn’t always satisfy the users’ requirements. Method Assessment Fusion(VMAF) [20], a smart perceptual
| (cid:46) Observation3. | ABR | algorithms | is  | allowed | to be | generated |               |     |            |           |       |     |         |        |
| ---------------------- | --- | ---------- | --- | ------- | ----- | --------- | ------------- | --- | ---------- | --------- | ----- | --- | ------- | ------ |
|                        |     |            |     |         |       |           | video quality |     | assessment | algorithm | based | on  | support | vector |
or updated efficiently within short duration since the band- machine(SVM), which currently stands for the state-of-the-art
widthdistributionevolvesslowlyovertime,asthedistribution
|     |     |     |     |     |     |     | quality assessment |     | metric | [33]. | More information |     | please | refer |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ----- | ---------------- | --- | ------ | ----- |
oftwoadjacenttimepoints(1hour)isapproximatelythesame. to §V-A. Figure 5(a) shows, the bitrate-aware method blindly
Figure4(c)and4(d)elaboratetheCDFofthroughputdistri- selects the video chunk with higher bitrate but neglects the
butionfromanotherperspective,andwecanseethatalthough
|     |     |     |     |     |     |     | corresponding |     | video | quality. | However, | comparing | the | trajec- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | -------- | -------- | --------- | --- | ------- |
thebandwidthdistributionseemsdifferentatthesametimeon toryofbitrate-awarewiththequality-awareapproach,wefind
differentdays(Figure4(c)),buttheconditionsoftwoadjacent
|     |     |     |     |     |     |     | that the | bitrate-aware |     | method | often downloads |     | low-efficiency |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------ | --------------- | --- | -------------- | --- |
time points (1 hour) is approximately the same (Figure 4(d)). chunk. For instance, during the playback time=14, although
To this end, the intuitive idea is to continually train the model the bitrates of the two choices are only one level different,
withashortperiod,whichallowstheABRalgorithmtoupdate
|     |     |     |     |     |     |     | the chunk | of  | higher | bitrates | gains 243.44% |     | (17.59→60.43) |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | -------- | ------------- | --- | ------------- | --- |
dynamicallyinsteadofleveragingfixedparametersorrules.In improvements on the perceptual video quality compared with
| our work, | we set the | training | period | as 1 hour. | In  | detail, we |         |           |     |      |         |        |       |       |
| --------- | ---------- | -------- | ------ | ---------- | --- | ---------- | ------- | --------- | --- | ---- | ------- | ------ | ----- | ----- |
|           |            |          |        |            |     |            | that of | the lower | one | (see | more in | Figure | 5(c), | video |
take 50-55 minutes for collecting network traces and use only chunk 4). Meanwhile, the bitrate-aware method also wastes
5-10 minutes for training the NN (§IV-B3). the buffer on achieving a slight increase in video quality,
| (cid:46) Summary. | Exploring | the | aforementioned |     | opportunities, |     |           |            |     |       |             |          |     |           |
| ----------------- | --------- | --- | -------------- | --- | -------------- | --- | --------- | ---------- | --- | ----- | ----------- | -------- | --- | --------- |
|                   |           |     |                |     |                |     | which may | eventually |     | cause | unnecessary | stalling |     | events in |
however, requires a learning-based ABR scheme with not the future. E.g., during the playback time=100, the bitrate-
onlyachievingoutperformedperformanceswithfastefficiency
|          |                   |     |                  |     |          |     | aware algorithm |     | chooses | the | highest bitrates, |     | but only | gains |
| -------- | ----------------- | --- | ---------------- | --- | -------- | --- | --------------- | --- | ------- | --- | ----------------- | --- | -------- | ----- |
| training | in a short period | but | also continually |     | learning | to  | fit             |     |         |     |                   |     |          |       |
12.13%(89.13→99.97)intermsofthevideoqualitycompared
the variety of network environments. with the quality-aware method (see more in Figure 5(c),
|     |     |     |     |     |     |     | video chunk | 26). | On the | contrary, | the quality-aware |     |     | algorithm |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | --------- | ----------------- | --- | --- | --------- |
III. CHALLENGESANDKEYIDEAS
|     |     |     |     |     |     |     | always | picks | the best-efficient |     | chunk | with | high | perceptual |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------------------ | --- | ----- | ---- | ---- | ---------- |
In this section, on the basis of the aforementioned observa- video quality and preserves the buffer occupancy within an
| tions, we | mainly generalize | three | key | challenges | from | several | allowable | range. |     |     |     |     |     |     |
| --------- | ----------------- | ----- | --- | ---------- | ---- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- |
perspectives, that includes, how to develop a complete video Hence, one of the better solutions is to add video bitrates
quality-based ABR system (§III-A), how to train the NN via as another metric to describe the perceptual video quality.

5
4.3
1.8
)spBM(etartiB Quality-Aware ABR Bitrate-Aware ABR
0.4
0.2
)nim(reffuB
100
50
0 50 100 150
Time(s)
erocS-FAMV
4.3
1.8
(a) Quality-aware ABR picks best-fit bitrates via
thebitrate-qualitycurveoneachchunk.
)spBM(etartiB Quality-Aware ABR Bitrate-Aware ABR
0.4
0.2
)nim(reffuB
100
50
0 50 100 150
Time(s)
erocS-FAMV
2.0
1.5
1.0
0.5
0.0
1 2 3 4
Bitrate(mbps)
(b) Ourapproachcaneffectivelyutilizethebuffer
occupancycomparedwiththeexistingscheme.
)BM(seziS
knuhC
Perceptual quality for
Video Bitrate=1.8mbps
V4 V48
V26 Average
100
75
50
25
0
1 2 3 4
Bitrate(mbps)
erocS
FAMV
Perceptual quality for
Video Bitrate=1.8mbps
V4 V48
V26 Average
(c) The correlation between the bitrate and the
chunksize,aswellasthebitrateandtheVMAF.
Fig. 5. We evaluate quality-aware ABR algorithm and bitrate-aware ABR algorithm with the same video over HSDPA [27] network traces respectively.
Resultsareplottedasthecurvesofselectedbitrate,bufferoccupancyandtheselectedchunk’sVMAF(§V-A,[20])forentiresessions.
Step
noitcA
Expert Trajectory
Supervised Learning
Step
(a) Supervisedlearning
noitcA
the optimal strategy [35]. However, recent work [10]–[12],
[17] has demonstrated that the ABR process can be precisely
emulated by an offline virtual player (§VI-A2) with complete
future network information. What’s more, by taking several
Expert Trajectory
steps ahead, we can further accurately estimate the near-
Imitation Learning
optimal expert policy of any ABR state within an accept-
(b) Imitationlearning able time (§IV-A2). Thus, the intuitive idea is to leverage
supervisedlearningmethodstominimizethelossbetweenthe
Fig.6. TherealtrajectoryontheABRtaskgivenbyimitationlearningand
predicted and the expert policy. Nevertheless, it’s impractical
supervised learning, where the red background means the player occurs the
rebufferingevent. since the off-policy method [35] suffers from compounding
error whenthealgorithmexecutesitspolicy,leadingittodrift
to new and unexpected states [36]. For example, as shown in
Nevertheless, current approaches, especially learning-based
Figure 6(a), in the beginning, supervised learning-based ABR
ABRs[12],lackfundamentalquality-basedsettings,i.e.,archi-
algorithm fetches the bitrate that is consistent with the expert
tectures,metrics,datasets,andsoon.We,therefore,encounter
policy, but when it selects a bitrate with a minor error (after
the first challenge of our work: How to construct a video
the black line), the state may be transited to the situation not
quality-aware ABR system?
included in the dataset, so the algorithm would select another
Our Solution. In this paper, our solution is generally
wrong bitrate. Such compounding errors eventually lead to a
composed of three tasks: 1) We construct Comyco’s NN ar-
continuous rebuffering event (the red area in the figure). As a
chitecture with jointly considering several underlying metrics,
result, supervised-learning methods lack the ability to learn to
i.e, past network features and video content features as well
recover from failures.
asvideoplaybackfeatures(§IV-A1).2)Weproposeaquality-
In this paper, we aim to leverage imitation learning, a
basedQoEmetric(§V-A).3)WecollectavideoqualityDASH
method that closely related to RL and supervised learning, to
dataset which includes various types of videos (§V-B).
learn the strategy from the expert policy samples. Imitation
learning method reproduces desired behavior according to
B. Challenges for Sample Efficiency expert demonstrations [22]. Imitation learning method allows
the NN to explore environments and collect samples (just like
Recent learning-based ABR schemes adopt RL methods to
RL) and learn the policy based on the expert policy (just as
maximize the average QoE objectives. The agent rollouts a
supervisedlearning).Indetail,atstept,thealgorithminfersa
trajectoryandupdatestheNNwithpolicygradients.However,
policy π at ABR state S . It then computes a loss (cid:96) (π ,π∗)
the effect of calculated gradients heavily depends on the t t t t t
w.r.ttheexpertpolicyπ∗.AfterobservingthenextstateS ,
amountandqualityofcollectedexperiences.Inmostcases,the t t+1
the algorithm further provides a different policy π for the
collected samples seldom stand for the optimal policy of the t+1
next step t+1 that will incur another loss (cid:96) (π ,π∗ ).
corresponding states, which leads to a long time to converge t t+1 t+1
Thus, for each π in the class of policies T ∈ {π ,...,π },
to the sub-optimal policy [22], [34]. Thus, we are facing the t 0 t
we can find the policy πˆ through any supervised learning
secondchallenge:ConsideringthecharacteristicofABRtasks,
algorithms (Eq. 1).
can we precisely estimate the optimal direction of gradients
to guide the model for better updating?
Our solution. The key principle of RL-based method is πˆ =argminE s∼dπ [(cid:96) t (π t ,π t ∗)] (1)
π∈T
to maximize reward of each action taken by the agent in
given states per step, since the agent does not really know Figure 6(b) elaborates the principle of imitation learning-

6
Submit Samples Experience Buffer
(§IV-A4)
Client ABR Ne C w l c ie o n m t er Loss (§IV-A3)
Throughput Model Server Instant Solver Expert Virtual Player Rollout Neural Network
Traces Trained (§IV-A2) Action (§VI-A2) (§IV-A1)
Model Collect network traces
Outer-loop System Selected Inner-loop System Periodically updating
(§IV-A) Traces (§IV-B) Request New Model Fig. 8. Inner-loop Training System Work-flow Overview. Training method-
ologiesareavailablein§IV-A4.
Fig. 7. Comyco System Overview. The system is composed of inner-loop
systemandouter-loopsystem.
the video player, placed on the client-side, downloads the
latest NN model from ABR model server for making further
decisions. Once the video session ends, the player collects
based ABR schemes: the algorithm attempts to explore the
the available throughput trace via past download chunk size
strategy in a range near the expert trajectory to avoid com-
and download time. At the same time, the collected trace will
pounding errors. Moreover, Figure 5(b) also shows that the
be submitted to the outer-loop system, which is placed on the
imitationlearningmethodcanalsohelptamingthecomplexity
server-side.Thentheouter-loopsystemwillinstantlycompute
of the ABR task, keeping the buffer occupancy within a low
thegapbetweenthecurrentpolicyandtheoptimalstrategyof
but safe range.
thesubmittedtraceanddeterminewhetherthetraceshouldbe
learned bycurrentNNduringthenexttrainingloop.Next,for
C. Challenges for Lifelong Updating
eachtimeduration,theinner-looptrainingsystem,alsoplaced
Moreover, previous observation shows that recent learning- ontheserver,willbeenabledbytheouter-loopsystem.Itthen
based ABRs fail to deploy in the real-world scenarios since updatestheNNw.r.ttheselectedtracesefficientlyvialifelong
such methods are required to online updating efficiently for imitation learning training method. Finally, the trained model
overcomingthetime-variesofnetworkconditions.Atthesame will be frozen and submitted to the ABR model server. The
time, although we’ve already attempted to leverage imitation serverthenstartswaitingfortherequestofnewcomerplayers.
learning rather than reinforcement learning for fast updating,
such methods still suffer from the large corpus of network A. Inner-loop System Overview
traces on each period, and finally, resulting in the failure of
Comyco’s inner-loop system work-flow is illustrated in
converge within an acceptable time. Hence, we finally list the
Figure 8. The sub-system is mainly composed of a NN, an
third challenge: Based on previously trained model, is there
ABRvirtualplayer,aninstantsolver,andanexperiencereplay
any possibility of incrementally train an ABR algorithm with
buffer. We start by introducing Comyco’s NN architecture.
a succinct yet efficient group of network traces?
Then we explain the basic training methodology. Finally, we
OurSolution.Weconsidertheproblemasastandardcatas-
further illustrate Comyco with a multi-agent framework.
trophicforgettingissue,aphenomenonwhichcanbeobserved
1) NN Architecture Overview: Motivated by the recent
as a dramatic performance degradation when some new tasks
success of no-regret online learning methods [38], Comyco’s
areaddedtoanexistingNNmodel.Totacklethisfundamental
learning agent is allowed to explore the environment via
problem [37], lifelong learning is one of the solutions which
traditional rollout methods. For each epoch t, the agent aims
aims to preserve the performance on previous tasks while
to select the next bitrate via a NN. We now explain the
adapting to new data. Hence, we employ lifelong learning on
detailsoftheagent’sNNincludingitsinputs,outputs,network
theproposedABRsystemforcontinuouslytrainingtheNNto
architecture, and representation.
fit the dynamic changes of networks. Furthermore, in order to
Inputs. We categorize the NN into three parts, network
further reduce the training overhead, we implement a module
features, video content features and video playback fea-
that can dynamically filter the useful network traces from the
tures (S ={C ,M ,F }). Details are described as follows.
k k k k
traces which instantly collected from the clients.
(cid:46) Past Network features. The agent takes past t chunks’
network status vector C = {c ,...,c } into NN,
k k−t−1 k
IV. COMYCOSYSTEMOVERVIEW
where c represents the throughput measured for video
i
In this section, taking the above challenges into account, chunk i. Specifically, c is computed by c = n /d , in
i i r,i i
we propose Comyco, an ABR system that uses the lifelong which n is the downloaded video size of chunk i with
r,i
imitation learning method to update the NN continuously. In selected bitrates r, and d means download time for video
i
detail, as illustrated in Figure 7, Comyco consists of two chunk n .
r,i
sub-systems, i.e., inner-loop training system and outer-loop (cid:46) Video content features. Besides that, we also consider
system. The inner-loop system adopts the imitation learning adding video content features into NN’s inputs for improv-
method to efficiently learn the policy via cloning the behavior ing its abilities on detecting the diversity of video contents.
of the expert strategy. The outer-loop system enables Comyco Indetails,thelearningagentleveragesM ={N ,V }
k k+1 k+1
to keep updating with low extra overhead. It’s notable that to represent video content features. Here N is a vector
k+1
the inner-loop system can be deployed solely if there is thatreflectsthevideosizeforeachbitrateofthenextchunk
no need to continuously update the model. The Comyco’s k+1, and V is a vector which stands for the perceptual
k+1
system workflow is shown as follows: before the video starts, video quality metrics for each bitrate of the next chunk.

7
Past Network Features 1 1 x D 4 - , C 1 N 2 N 8 Flatten G 1 R 28 U k Tr + ip- 1 T , im in e w ( h R ic T h T) δt a k n r d efl v e i c d t e s o th r e en w d a e i r tin ti g m t e i , m a e n s d uc B h m a a s x R i o s un th d e -
Fu V t i u d r e e o C S h iz u e nk 1D1 1 -x D C4 - N, C 1N N 2 N 8 Flatten G 1 R 28 U m fo a r x th b e uff n e e r xt siz c e o . m F p i u n t a a l t l i y o , n. w N e o r t e e fre th sh at th th e e v p ir r t o u b a l l em tim c e an t k+ b 1 e
Future Chunk 1x4, 128
Video Quality GRU solvedwithanyoptimizationalgorithms,suchasmemoization,
128
Video Content Features dynamic programming as well as Hindsight [4]. Ideally, there
GRU
Buffer Size 1 1 x D 4 - , C 1 N 2 N 8 Flatten 128 exists a trade-off between the computation overhead and the
Last Action 1 F 2 C 8 G 1 R 28 U performance. We list the performance comparison of instant
Delay FC solverwithdifferentN in§VI-A5.Inthiswork,wesetN =8.
Chunk 1 F 2 C 8 G 1 R 28 U (cid:335)
Remaining 128
Video Playback Features Next chunk’s bitrate max QoEN (2)
R1,...,RN,Ts
Fig. 9. Comyco’s NN architecture Overview. The NN contains network s.t. t =t + d k (R k ) +δt , (3)
features,videocontentinformation,aswellasplaybackstatus. k+1 k C k
k
1 (cid:90) tk+1−δtk
(cid:46) Video playback features. The last essential feature for de- C k = t −t −δt C t dt, (4)
scribingtheABR’sstateisthecurrentvideoplaybackstatus.
k+
(cid:34)
1
(cid:18)
k k tk
(cid:19) (cid:35)
d (R )
The status is represented as F k = {v k−1 ,B k ,D k ,m k }, B k+1 = B k − k C k +L−δt k , (5)
where v k−1 is the perceptual video quality metric for the k + +
past video chunk selected, B ,D are vectors which stand B =T , (6)
k k 1 s
forpasttchunks’bufferoccupancyanddownloadtime,and B ∈[0,B ],R ∈R,∀k=1,2,...,N. (7)
k max k
m means the normalized video chunk remaining.
k
Outputs. Same as previous work, we consider using discrete
3) Choice of Loss Functions for Comyco: We start by
action space to describe the output. Note that the output is
designing the loss function from the fundamental RL training
an n-dim vector indicating the probability of the bitrate being
methodologies. The goal of the RL-based method is to maxi-
selected under the current ABR state S .
k mize the Bellman Equation, which is equivalent to maximize
NN Representation. As shown in Figure 9, for each input
the value function q (s,a) [35]. Thus, given an expert action
π
type,weuseaproperandspecificmethodtoextracttheunder-
aˆ and the optimal value function q (s,aˆ) = q (s,a), we can
π ∗
lyingfeatures.Specifically,wefirstleverageasingle1D-CNN
update the model via minimizing the gap between the true
layerwithkernel=4,channels=128,stride=1toextractnetwork action probability Aˆ and π, where Aˆ is a one hot encoding
features to a 128-dim layer. We then use two 1D-CNN layers
in terms of aˆ. For more theoretical analysis please refer to
with kernel=1x4, channels=128 to fetch the hidden features
§VII-A. In this paper, we use cross entropy error as the
from the future chunk’s video content matrix. Meanwhile,
loss function. Note that the function can be represented as
we utilize a 1D-CNN or a fully connected layer to extract
any traditional behavioral cloning loss method [22], such as
the useful characteristics from each metric upon the video
Quadratic, LI-loss and Hinge loss function. In addition, we
playbackinputs.TheselectedfeaturesarepassedintoaGated
findthattheothergoalofthelossfunctionistomaximizethe
Recurrent Unit (GRU) [39] layer and outputs as a 128-dims
probabilitiesoftheselectedaction,whilethegoalsignificantly
vector.Finally,theoutputoftheNNisa6-dimsvector,which
reducestheaggressivenessofexploration,andfinally,resulting
represents the probabilities for each bitrate selected. We use
in obtaining the sub-optimal performance. Thus, motivated by
RelU as the active function for each feature extraction layer
the recent work on RL [40], we further add the entropy H
and leverage softmax for the last layer.
of the policy π to the loss function. It can encourage the
2) Instant Solver: Once the sampling module rolls out an
algorithmtoincreasetheexplorationrateintheearlystageand
action a , we aim to design an algorithm to fetch all the
t discourage it in the later stage. The loss function for Comyco
optimal actions aˆ with respect to current state s . Followed
t t is described in Eq 8.
by these thoughts, we further propose the Instant Solver. The
key idea is to choose future chunk k’s bitrate R by taking N
k
steps ahead via an offline virtual player, and solves a specific L =− (cid:88) Aˆlogπ(s,a;θ)+αH(π(s;θ)). (8)
comyco
QoE maximization problem with future network throughput
measured C , in which the future real throughput can be Hereπ(s,a;θ)istherolloutpolicyselectedbytheNN,Aˆis
t
successfully collected under both offline environments and therealactionprobabilityvectorgeneratedbytheexpertactor
real-world network scenarios. Inspired by recent model-based aˆ,H(π(s;θ)representstheentropyofthepolicy,αisahyper-
ABR work [10], we formulate the problem as demonstrated parameter that controls the encouragement of exploration. In
in Eq. 2, denoted as QoEN . In detail, the virtual player thispaper,wesetα=10−3anddiscussL withdifferent
max comyco
consists of a virtual timestamp, a real-world network trace , α in §VI-A5. Recall that L (§IV-B3) will be used to
lifelong
and a video description. At virtual time t , we first calculate taketheplaceofL iftheouter-loopsystemisrequired.
k comyco
download time for chunk k via d (R )/C , where d is the 4) Training Comyco with Experience Replay: Recent off-
k k k k
videochunksizeforbitrateR ,andC isaveragethroughput policy RL-based methods [41] leverage experience replay
k k
measured. We then update B buffer occupancy for chunk buffer to achieve better convergence behavior when training
k+1

8
a function approximator. Inspired by the success of these Trained Inner-loop System
Client
approaches, we also create a sample buffer that can store the Model (§IV-A)
pastexpertstrategiesandallowthealgorithmtorandomlypick Throughput Lifelong Imitation
Trace Learning(§IV-B3)
thesamplefromthebufferduringthetrainingprocess.Wewill
Optimal Estimator Store Useful Throughput Collector
discusstheeffectofutilizingexperiencereplayin§VI-A5.We (§IV-B1) Traces (§IV-B2)
summarize the training procedure in Alg. 1.
Fig.10. Outer-loopTrainingSystemWork-flowOverview.Trainingmethod-
Algorithm 1 Inner-loop Overall Training Procedure ologiesareavailablein§IV-B3.
Require: Training model θ, Instant Solver(§IV-A2).
1: procedure INNER-LOOPTRAINING
2: Initialize π. we leverage an instant solver (§IV-A2) for estimating the
3: Sample Training Batch B ={}. optimal strategy. Specifically, we roll out the best bitrate for
4: Randomly pick trace, video from network (§VI-A2) and each step via maximizing the QoE objective (Eq. 2). In this
video (§V-B) dataset.
work, we also set the future horizon N = 8 since the near-
5: Get State ABR state s t .
optimal policy is well enough for this task [10], [12]. It’s
6: repeat
7: Picks a t according to policy π(s t ;θ). worthnotingthatwecanalsoemployHindsight[4]oranother
8: Expertactionaˆ t =Instant Solver(s t ,trace,video). optimalABRestimator[5]toreplacetheinstantsolverinstead.
(cid:83)
9: B ←B {s t ,aˆ t }.
10: Samples a batch Bˆ ∈B. Q
11: Updates network θ with Bˆ using Eq.8 or Eq.10; E tr = Q tr,θ (9)
12: Produces next ABR state S t+1 according to s t and a t . opt
13: if done then (cid:46) End of the video. 2) Trace Collector: Having computed the normalized QoE
14: Randomly pick trace, video from the network and
metric from the Optimal Estimator, we focus on learning
video dataset.
a proper NN for the current network conditions efficiently.
15: Get State ABR state s t .
16: t←t+1 Ideally,theintuitiveideaistousethewholecollectedtraceto
17: until Converged fine-tunetheoldNN.However,it’simpracticalsincethenum-
berofcollectedtraceissohugethattheNNcannotbetrained
5) Parallel Training: Notably, the training process can be in an allowable time. Moreover, previous analysis shows that
designedasynchronously,whichisquitesuitableforthemulti- thereisnotmuchdifferenceinthenetworkdistributionwithin
agent parallel training framework. Inspired by the multi-agent an hour (§III-B), that means, the trained policy may perform
training method [18], [40], we modify Comyco’s framework well on most traces but eventually fail on some traces. Taking
from single-agent training to asynchronous multi-agent train- such observations into account, our key idea is to pick proper
ing.TheComyco’smulti-agenttrainingconsistsofthreeparts, traces into the Trace Collector, in which the normalized QoE
a central agent with a NN, an experience replay buffer, and a of the trace is lower than the given threshold Thres. The
group of agents with a virtual player and an instant solver. inner-loop system then trains the NN from the network trace
For any ABR state s, the agents use the virtual player to in the Trace Collector. Finally, Comyco generalizes a strategy
emulatetheABRprocessw.r.tcurrentstatesandactionsgiven for the network conditions under the next training period. In
by the NN which placed on the central agent, and collect the this work, we set Thres as 0.8, and the training period as
expertactionaˆthroughtheinstantsolver;theythensubmitthe 1 hour. We further investigate the influence of Thres on the
information containing {s,aˆ} to the experience replay buffer. proposed method in §VI-B7.
The central agent trains the NN by picking the sample batch 3) Loss Function for Lifelong Learning Method: The goal
from the buffer. By default, Comyco uses 12 agents, which is of the lifelong learning [42] is to avoid Catastrophic Forget-
the same number of CPU cores of our PC. ting, that means, the NN works well on the latest task but
suffers from unexpected performance on previous tasks. In
this work, we pick Learning without Forgetting (LwF) [23],
B. Outer-loop System Overview
which uses outputs of the old models as soft targets on
The key idea of the outer-loop sub-system is to reduce the old tasks, as the learning algorithm. LwF enables the lowest
number of training set with guaranteeing the training perfor- computation cost among all the previously proposed schemes
mance as much as possible. We demonstrate the outer-loop and works in the comparable performance in terms of the
lifelonglearningsysteminFigure10.Thesub-systemincludes state-of-the-artapproach[42].Subsequently,weimplementan
several modules, such as the Optimal Estimator (§IV-B1) and LwF-based loss function L to take the place of the
lifelong
theTraceCollector(§IV-B2).Inthissection,weintroducethe loss function L of the inner-loop system for achieving
Comyco
modules and illustrate the training methodologies (§IV-B3). continual learning. The equation is listed in Eq. 10, where
1) Optimal Estimator: Technically, the Optimal Estimator L represents the loss function of Comyco (listed in
Comyco
is a module which can compute the normalized QoE E on a Eq.8),π(s,a;θ )isrolloutpolicyviatheoldNN(previous
tr old
network throughput trace tr, where the trace is collected and network),andπ(s,a;θ)istherolloutpolicyforcurrentNN.It
reported from the client. As suggested by prior work, E is is notable that we refer the old policy π(s,a;θ ) as a value,
tr old
definedastheratiobetweentheQoEperformedbythecurrent which means, it does not provide any gradients for the loss
policy Q and the optimal QoE Q ( Eq. 9). Meanwhile, function. Inspired by prior work [23], we set λ=1. In general,
tr,θ opt

9
TABLEI
PERFOMANCECOMPARISONOFQOEMODELSONWATERLOO
STREAMINGSQOE-III[21]
QoEmodel Type VQA SRCC
Pensieve’s[12] linear - 0.6256
MPC’s[10] linear - 0.7143
(a) VideoBitrate:0.480 (b) SSIM:0.592 (c) VMAF:0.689
Bentaleb’s[28] linear SSIMplus[48] 0.6322
Fig. 11. Correlation comparison of video presentation quality metrics on Duanmu’s[21] linear - 0.7743
the SQoE-III dataset [21]. Results are summarized by Pearson correlation QoEv withCombinedSmooth. linear VMAF[20] 0.7741
coefficient[43].
Comyco’s linear VMAF 0.7870
we demonstrate the training methodology of the outer-loop
system in Alg. 2. As shown, the workflow mainly consists
where N is the total number of chunks during the session,
of three parts, i.e., i) picking necessary network traces via
R represents each chunk’s video bitrate, T reflects the
n n
Optimal Estimator, ii) storing the trace if the normalized QoE
rebuffering time for each chunk n, q(R ) is a function that
n
lower than the threshold, iii) starting learning the algorithm if
mapsthebitrateR tothevideoqualityperceivedbytheuser,
n
the period reaches 1 hour.
[q(R )−q(R )] denotes positive video bitrate smooth-
n+1 n +
ness,meaningswitchthevideochunkfromlowbitratetohigh
(cid:88)
L lifelong =L Comyco +λ π(s;θ old )logπ(s;θ). (10) bitrate and [q(R n+1 )−q(R n )] − is negative smoothness, and
α, β, γ, δ are the parameters to describe their aggressiveness.
Choice of q(R ). Estimating QoE via handcrafted features
n
Algorithm 2 Outer-loop Overall Training Procedure
from the client-side has lasted a long history [33], as sev-
Require: Old model θ , Training model θ
old eral schemes seldom yield a reliable result. Revisiting these
Require: Trace Collector T (§IV-B3), Threshold Thres.
schemes, we find that Video quality assessment (VQA) plays
Require: Optimal Estimator(§IV-B1).
a crucial part in QoE models. Most studies pick video bitrate,
1: procedure OUTER-LOOPTRAINING SSIM or PSNR [45] as the inputs, while such metrics fail to
2: Receive trace from the client. either precisely reflect the visual quality seen by human eyes
3: E tr ← Optimal Estimator(trace). oraccuratelydescribethelatentvideofeatures,resultinginthe
4: if E tr <Thres then failure of characterizingthe video qualities ofthe entire video
5: Store trace into Trace Collector. sessions [31]. To better understand the correlation between
6: if Training period = 1 hour then video presentation quality and QoE metric, we test the corre-
7: Inner-loop Training(T) (§IV-A4) with the loss lation between mean opinion score (MOS) and video quality
function L (Alg.10).
Lifelong assessment (VQA) metrics, including video bitrate, SSIM
8: SubmitthetrainedmodeltotheABRmodelserver. and Video Multimethod Assessment Fusion (VMAF) [20],
under the Waterloo Streaming QoE Database III (SQoE-III).
Here SQoE-III is the largest and most realistic dataset for
V. QOEMETRICSANDVIDEODATASETS
dynamic adaptive streaming over HTTP [21], which consists
Upon constructing Comyco’s NN architecture by consider- ofatotalof450streamingvideoscreatedfromdiversesource
ingvideocontentfeatures,wehaveyetdiscussedhowtotrain contentanddiversedistortionpatterns[21].SSIMisapopular
the NN. Indeed, we lack a video quality-aware QoE model imagequalitymetric[13].VMAFisanobjectivefull-reference
and an ABR video dataset with video quality assessment. In video quality metric that is formulated by Netflix to estimate
this section, we use VMAF to describe the perceptual video subjective video quality. Results are collected with Pearson
quality of our work. We then propose a video quality-aware correlation coefficient [43] as suggested by [46]. As shown
QoE metric under the guidance of the real-world ABR QoE in Figure 11, we can see that VMAF achieves the highest
dataset [21]. Finally, we collect a DASH video dataset with correlation among all candidates, with the improvements in
different VMAF assessments. the coefficient of 16.39%-43.54%. Besides, VMAF is also
a popular scheme with great potential in both academia and
A. QoE Model Setup industry [47]. We, therefore, set q(R )=VMAF(R ).
n n
Motivated by the linear-based QoE metric that is widely QoE Parameters Setup. Recall that the main goal of our
used to evaluate several ABR schemes [10], [12], [17], [28], paper is to propose a feasible ABR system instead of a
[32], [44], we concluded our QoE metric QoE as:
v convincing QoE metric. In this work, we attempt to lever-
N N age linear-regression methods to find the proper parameters.
(cid:88) (cid:88)
QoE v =α q(R n )−β T n Specifically, we randomly divide the SQoE-III database into
n=1 n=1 two parts, 80% of the database for training and 20% testing.
N−1 N−1
(cid:88) (cid:88) We follow the idea by [21] and run the training process
+γ [q(R )−q(R )] −δ [q(R )−q(R )] ,
n+1 n + n+1 n − for 1,000 times to mitigate any bias caused by the division
n=1 n=1
(11) of data. As a result, we set α = 0.8469, β = 28.7959,

10
γ = 0.2979, δ = 1.0610. We take the Spearman correlation the past sequence length k = 8 (as suggested by [12]) and
coefficient (SRCC), as suggested by [21], to evaluate the future 1 video chunk features (as suggested by [10]) into the
performanceofourQoEmodelwithexistingproposedmodels NN. We set the learning rate α = 10−4 and use the Adam
and the median correlation and its corresponding regression optimizer[58]tooptimizethemodel.Formoredetails,please
modelaredemonstratedinTableI.Asshown,theQoE model refer to our repository [59].
v
outperforms recent work. In conclusion, the proposed QoE 2) Experimental Setup: The evaluation system consists of:
model is well enough to evaluate ABR schemes. VirtualPlayer.WedesignafaithfulABRofflinevirtualplayer
Separated smoothness metrics. The reason why we separate totrainComycovianetworktracesandvideodescriptions.The
smoothnessmetricsisthat:duringthepre-experiment,wefind player is written in C++ and Python3.6, with close refering to
thatthereisapositivecorrelationbetweenpositivesmoothness several state-of-the-art open-sourced ABR simulators includ-
and MOS, which means, users will feel satisfied if the video ing Pensieve, Oboe and Sabre [11]. Comparing the executing
quality increases. Extensive analysis shows that the weight time of C++-based instant solver and python-based solver, we
for negative smoothness is 3× higher than that of positive find that using C++ will significantly accelerate the training
smoothness,whichdemystifiesaseverepenaltyondecreasing process, with the improvements of 15,000%.
video qualities. Besides, prior work [33], [49], [50] has also Testbed. Our work consists of two testbeds. Both server and
observed the correlation between the positive smoothness and client run on the 12-core, Intel i7 3.7 GHz CPUs with 32GB
the negative smoothness. Results on Table I also illustrate RAMrunningWindows10.Comycocanbetrainedefficiently
thatComycowithseparatedsmoothnessmetriccaneffectively on both GPU and CPU. The testbed is composed of:
| improve | the performance |     | on  | the SRCC | score | of 3.0%. |                       |     |            |           |     |                  |     |     |
| ------- | --------------- | --- | --- | -------- | ----- | -------- | --------------------- | --- | ---------- | --------- | --- | ---------------- | --- | --- |
|         |                 |     |     |          |       |          | (cid:46) Trace-driven |     | Emulation. | Following |     | the instructions |     | of  |
recentwork[12],[17],weutilizeMahimahi[60]toemulate
B. Video Datasets the network conditions between the client (ChromeV73)
|           |         |         |              |         |                |                  | and ABR             | server                                    | (SimpleHTTPServer |     |     | by Python2.7) |     | via |
| --------- | ------- | ------- | ------------ | ------- | -------------- | ---------------- | ------------------- | ----------------------------------------- | ----------------- | --- | --- | ------------- | --- | --- |
| To better | improve |         | the Comyco’s |         | generalization | ability, we      |                     |                                           |                   |     |     |               |     |     |
|           |         |         |              |         |                |                  | collected           | network                                   | traces.           |     |     |               |     |     |
| propose   | a video | quality | DASH         | dataset | that           | involves movies, |                     |                                           |                   |     |     |               |     |     |
|           |         |         |              |         |                |                  | (cid:46) Real World | Deployment.Detailsareillustratedin§VI-A6. |                   |     |     |               |     |     |
sports,TV-shows,games,newsandMVs.Specifically,wefirst
collectvideoclipswithhighestresolutionfromYouTube[51], Network Trace Datasets. We collect about 3,000 network
|          |        |      |           |     |       |                | traces, totally | 47  | hours, from | public | datasets | for | training | and |
| -------- | ------ | ---- | --------- | --- | ----- | -------------- | --------------- | --- | ----------- | ------ | -------- | --- | -------- | --- |
| then use | FFmpeg | [52] | to encode | the | video | by H.264 codec |                 |     |             |        |          |     |          |     |
testing, including:
andMP4Box[53]todashifyvideosaccordingtotheencoding
|           |       |           |        |      |      |                  | (cid:46) Chunk-level |     | Network | Traces: | including | HSDPA | [27]: | a   |
| --------- | ----- | --------- | ------ | ---- | ---- | ---------------- | -------------------- | --- | ------- | ------- | --------- | ----- | ----- | --- |
| ladder of | video | sequences | ({235, | 375, | 560, | 750, 1050, 1750, |                      |     |         |         |           |       |       |     |
2350, 3000, 4300}kbps) [12], [21], [25]. Each chunk is en- well-known 3G/HSDPA network trace dataset, we use a
coded as 4 seconds. During the trans-coding process, for each slide-windowtoupsamplingthetracesasmentionedbyPen-
video,wemeasureVMAF,VMAF-4KandVMAF-phonemet- sieve (1000 traces, 1s granularity); FCC [26]: a broadband
ricwiththereferenceresolutionof1920×1080respectively.In dataset (1000 traces, 1s granularity); Oboe [61] (428 traces,
1-5sgranularity):atracedatasetcollectedfromwired,WiFi
general,thedatasetcontains86completevideos,with394,551
video chunks and 1,578,204 video quality assessments. The and cellular network connections (only for validation.)
dataset have been published in [54]. (cid:46) SyntheticNetworkTraces:usesaMarkovianmodelwhere
|     |     |     |     |     |     |     | each state | represented |     | an average | throughput |     | in the | afore- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ---------- | ---------- | --- | ------ | ------ |
mentionedrange[12].Wecreatenetworktracesinover1000
|         |          |     | VI. EVALUATION |         |             |            |                |     |              |        |           |         |           |     |
| ------- | -------- | --- | -------------- | ------- | ----------- | ---------- | -------------- | --- | ------------ | ------ | --------- | ------- | --------- | --- |
|         |          |     |                |         |             |            | traces with    | 1s  | granularity. |        |           |         |           |     |
| In this | section, | we  | propose        | several | experiments | to analyze |                |     |              |        |           |         |           |     |
|         |          |     |                |         |             |            | ABR Baselines. |     | In this      | paper, | we select | several | represen- |     |
theperformanceofComyco.WestartbyevaluatingComyco’s
|            |        |       |         |         |            |          | tational ABR | algorithms |         | from various | type | of        | fundamental |     |
| ---------- | ------ | ----- | ------- | ------- | ---------- | -------- | ------------ | ---------- | ------- | ------------ | ---- | --------- | ----------- | --- |
| inner-loop | system | under | various | network | conditions | and com- |              |            |         |              |      |           |             |     |
|            |        |       |         |         |            |          | principles.  | Details    | of each | algorithm    | are  | listed in | §VIII.      |     |
pareitwithpreviouslyproposedABRapproaches(§VI-A).We
then evaluate the outer-loop system over real-world network (cid:46) Rate-based Approach (RB) [7]: uses harmonic mean of
|            |         |     |         |         |              |      | past five | throughputs | measured |     | as future | bandwidth, |     | and |
| ---------- | ------- | --- | ------- | ------- | ------------ | ---- | --------- | ----------- | -------- | --- | --------- | ---------- | --- | --- |
| traces and | compare |     | it with | several | ABR schemes, | such | as        |             |          |     |           |            |     |     |
previously proposed ABR schemes, and outer-loop system picks the next chunks’ bitrate with nearest and lower than
|                |     |          |            |          |     |     | the predicted | bandwidth.                                  |     |     |     |     |     |     |
| -------------- | --- | -------- | ---------- | -------- | --- | --- | ------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
| with different |     | updating | strategies | (§VI-B). |     |     |               |                                             |     |     |     |     |     |     |
|                |     |          |            |          |     |     | (cid:46) BOLA | [9]:turnstheABRproblemintoautilitymaximiza- |     |     |     |     |     |     |
tionproblemandsolveitbyusingtheLyapunovfunction.It
| A. Evaluation |     | for Inner-loop |     | System |     |     |              |              |     |           |     |          |          |     |
| ------------- | --- | -------------- | --- | ------ | --- | --- | ------------ | ------------ | --- | --------- | --- | -------- | -------- | --- |
|               |     |                |     |        |     |     | is a typical | buffer-based |     | approach. | We  | use BOLA | provided |     |
RecallthattheComyco’sinner-loopsystemcanbedeployed by the authors [11].
solely if there is no need to achieve continual learning. In this (cid:46) RobustMPC[10]:inputsthebufferoccupancyandthrough-
experiment, we treat the inner-loop system as Comyco, and put predictions and then maximizes the QoE by solv-
use L comyco as the NN’s loss function. ing an optimization problem. We use C++ to implement
1) Implementation: We use TensorFlow [55] to implement RobustMPC and leverage QoE (§V-A) to optimize the
v
| the training | workflow |     | and utilizing |     | TFlearn | [56] to construct | strategy. |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ------------- | --- | ------- | ----------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
the NN architecture. Besides, we use C++ to implement (cid:46) Pensieve [12]: the state-of-the-art ABR scheme which uti-
the instant solver and the virtual player. Then we leverage lizes Deep Reinforcement Learning (DRL) to pick bitrate
Swig [57] to compile them as a Python class. The NN takes for next video chunks. Pensieve takes the former network

11
1.0
| 1.0 |     |          |     |     |     |          |               | Comyco |     | RobustMPC | Rate-based |     | Pensieve |     | BOLA |
| --- | --- | -------- | --- | --- | --- | -------- | ------------- | ------ | --- | --------- | ---------- | --- | -------- | --- | ---- |
| 0.8 |     |          |     | 0.8 |     |          | eulaV egarevA | 6      |     |           |            |     |          |     |      |
| 0.6 |     | Comyco   |     | 0.6 |     |          |               |        |     |           |            |     |          |     |      |
| FDC |     |          |     | FDC |     |          |               | 4      |     |           |            |     |          |     |      |
| 0.4 |     | BOLA     |     |     |     | BOLA     |               |        |     |           |            |     |          |     |      |
|     |     | Pensieve |     | 0.4 |     | Pensieve |               |        |     |           |            |     |          |     |      |
2
| 0.2 |     | Rate-based |     | 0.2 |     | Rate-based |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | RobustMPC  |     |     |     | RobustMPC  |     |     |     |     |     |     |     |     |     |
| 0.0 |     |            |     | 0.0 |     |            |     | 0   |     |     |     |     |     |     |     |
20 30 40 50 60 70 80 20 0 20 40 60 80 Average Rebuffer Positive Negative Average
Average QoE QoE Improvement(%) Quality Time Smoothness Smoothness QoE
1.0
| 1.0 |     |     |     |     |     |     |     | Comyco |     | RobustMPC | Rate-based |     | Pensieve |     | BOLA |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | ---------- | --- | -------- | --- | ---- |
6
| 0.8     |     |            |     | 0.8     |     |            | eulaV egarevA |     |     |     |     |     |     |     |     |
| ------- | --- | ---------- | --- | ------- | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| FDC 0.6 |     | Comyco     |     | FDC 0.6 |     |            |               | 4   |     |     |     |     |     |     |     |
| 0.4     |     | BOLA       |     | 0.4     |     | BOLA       |               |     |     |     |     |     |     |     |     |
|         |     | Pensieve   |     |         |     | Pensieve   |               |     |     |     |     |     |     |     |     |
| 0.2     |     | Rate-based |     |         |     | Rate-based |               | 2   |     |     |     |     |     |     |     |
0.2
|     |     | RobustMPC |     |     |     | RobustMPC |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0 |     |           |     | 0.0 |     |           |     | 0   |     |     |     |     |     |     |     |
20 30 40 50 60 70 80 20 0 20 40 60 80 Average Rebuffer Positive Negative Average
Average QoE QoE Improvement(%) Quality Time Smoothness Smoothness QoE
Fig.12. ComparingComycowithexistingABRapproachesundertheHSDPAandFCCnetworktraces.ResultsareillustratedwithCDFdistributions,QoE
improvementcurvesandthecomparisonofseveralunderlyingmetrics(§V-A).
50 50 FCC dataset. What’s more, we also report the performance of
48 48 underlying metrics including average video quality (VMAF),
| 46  |     |     |     | 46  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
draweR 44 draweR rebuffering time, positive and negative smoothness, as well as
44
42 42 QoE. We find that Comyco is well performed on the average
|     |     | Comyco |     |     | Comyco |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
40 Pensieve@VMAF 40 Pensieve@VMAF qualitymetric,whichimproves6.84%-15.64%comparedwith
|     |                | RobustMPC           |     |                  | RobustMPC            |     |        |         |            |     |              |      |          |                |     |
| --- | -------------- | ------------------- | --- | ---------------- | -------------------- | --- | ------ | ------- | ---------- | --- | ------------ | ---- | -------- | -------------- | --- |
| 38  |                | Supervised Learning |     | 38               | Supervised Learning  |     |        |         |            |     |              |      |          |                |     |
|     |                |                     |     |                  |                      |     | other  | ABRs.   | Moreover,  |     | Comyco is    | able | to avoid | rebuffering    |     |
| 360 | 2 4            | 6                   | 8   | 0 2              | 4                    | 6 8 | 10     |         |            |     |              |      |          |                |     |
|     | Epochs(x10000) |                     |     |                  | Training Time(Hours) |     | and    | bitrate | changes.   |     |              |      |          |                |     |
|     | (a) Epochs     |                     |     | (b) TrainingTime |                      |     |        |         |            |     |              |      |          |                |     |
|     |                |                     |     |                  |                      |     | Sample |         | Efficiency | of  | ABR Schemes. |      | Figure   | 13 illustrates |     |
Fig. 13. Comparing the performance of Comyco with Pensieve and Super- the average QoE of learning-based ABR schemes under the
vised learning-based method under the HSDPA dataset. Comyco is able to HSDPA network traces. We validate the performance of two
achievethehighestperformancewithsignificantgainsinsampleefficiency.
|             |           |                |            |                |     |             | schemes      |             | respectively | during       | the training   |             | process.      | Results      | are |
| ----------- | --------- | -------------- | ---------- | -------------- | --- | ----------- | ------------ | ----------- | ------------ | ------------ | -------------- | ----------- | ------------- | ------------ | --- |
|             |           |                |            |                |     |             | shown        | with        | two          | perspectives | including      |             | Epoch-Average |              | QoE |
|             |           |                |            |                |     |             | and          | Training    | time-Average |              | QoE.           | As expected |               | (§III-B),    | we  |
| status as   | states    | and reinforces |            | itself through | the | interaction |              |             |              |              |                |             |               |              |     |
|             |           |                |            |                |     |             | observe      |             | that the     | supervised   | learning-based |             | method        | fails        | to  |
| with the    | faithful  | offline        | simulator. | We             | use | the scheme  |              |             |              |              |                |             |               |              |     |
|             |           |                |            |                |     |             | find         | a strategy, |              | which        | thereby leads  | to          | poor          | performance. |     |
| implemented | by        | the authors    | [30]       | but retrain    | the | model for   |              |             |              |              |                |             |               |              |     |
|             |           |                |            |                |     |             | Furthermore, |             | we           | see about    | 1700x          | improvement |               | in terms     | of  |
| our work    | (§VI-A3). |                |            |                |     |             |              |             |              |              |                |             |               |              |     |
|             |           |                |            |                |     |             | the          | number      | of samples   |              | required and   | about       | 16x           | improvement  |     |
| 3) Comyco   | vs.       | ABR schemes:   |            | In this part,  | we  | attempt     | to           |             |              |              |                |             |               |              |     |
|             |           |                |            |                |     |             | in           | terms       | of training  | time         | required.      | It makes    | sense         | since        | the |
compare the performance of Comyco with the recent ABR training the agent with a model-free RL-based method [35] is
schemes under several network traces via the trace-driven difficult. The agent is required to learn a latent representation
| virtual player. | The | details | of  | selected ABR | baselines | are |          |     |        |                |            |     |           |             |     |
| --------------- | --- | ------- | --- | ------------ | --------- | --- | -------- | --- | ------ | -------------- | ---------- | --- | --------- | ----------- | --- |
|                 |     |         |     |              |           |     | together |     | with a | control policy | to perform |     | the task, | as general- |     |
describedin§VI-A2.WeuseEnvivoDash3,awidelyused[10], izing a feasible encoder via a continuous reward signal is not
[12],[17],[44]referencevideoclip[25]andQoE tomeasure onlyextremelysampleinefficientbutalsopronetosuboptimal
v
the ABR performance. convergence. Meanwhile, achieving high sample efficiency is
(cid:46) Pensieve Re-training. We retrain Pensieve via our essential since the equilibria of learning-based methods are
| (§VI-A2), |     |     |     | (§IV-A1) |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
datasets NN architectures and QoE met- not always Pareto efficient in offline-training tasks, e.g., fast
rics (§V-A). Followed by recent work [17], our experiments generating ABR algorithms for personalized QoE or specific
use different entropy weights in the range of 5.0 to 0.1 videos, new NN architecture exploration. Moreover, the key
and dynamically decrease the weight every 1000 iterations. issue of RL-based ABR scheme (e.g., Pensieve) is to neglect
The training time takes about 8 hours and we show that exogenous inputs (e.g. future throughput measured) when
| Pensieve | outperforms | RobustMPC, |     | with | an overall | average |            |     |        |           |           |           |     |          |     |
| -------- | ----------- | ---------- | --- | ---- | ---------- | ------- | ---------- | --- | ------ | --------- | --------- | --------- | --- | -------- | --- |
|          |             |            |     |      |            |         | estimating |     | policy | gradient, | since the | advantage |     | function | may |
QoE improvement of 3.5% across all sessions. be overestimated or underestimated. On the contrary, in our
Comycovs.ExistingABRs.Figure12showsthecomparison work, Comyco considers the future throughput as the latent
of QoE metrics for existing ABR schemes (§VI-A2). Comyco feature. As a result, imitation learning-based ABR approach
outperforms recent ABRs, with the improvements on average Comyco outperforms Rl-based ABRs. Same conclusions and
QoEof7.5%-17.99%acrosstheHSDPAdatasetand4.85%- proofspleaserefertoRL-basedinputvariancealgorithms[34].
16.79% across the FCC dataset. Especially, Besides, we also 4) Comyco with Multiple Videos: To better understand
show the CDF of the percentage of improvements in QoE how Comyco performs on various videos, we randomly pick
for Comyco over existing schemes. Comyco surpasses state- videos from different video types (§V-B) and utilize Oboe
of-the-art ABR approach Pensieve for 91% of the sessions network traces [17] to evaluate the QoE performances of
v
across the HSDPA dataset and 78% of the sessions across the the proposed methods. Oboe network traces have diverse

12
80
75
70
65
60
55
50
Games Movies Music News Sports
EoQ
egarevA
Comyco RobustMPC Rate-based Pensieve BOLA TABLEIV
MODELSIZEANDCOSTCOMPARISONOFDIFFERENTABRS.
RB BB Quetra RMPC Pensieve
Comyco
[7] [8] [62] [10] [12]
Size(MB) 0.003 0.003 0.005 0.013 2.6 2.4
Time(MS) 461 278 588 10854 3090 2593
Fig.14. ComparingComycowithexistingABRapproachesundertheOboe
networktracesandvarioustypesofvideos.
80
TABLEII
COMYCOWITHDIFFERENTN ANDREPLAYSTRATEGIES. 70
α=0.001/N 5 6 7 8 9
60
ReplayOff 0.883 0.893 0.917 0.932 0.942
ReplayOn 0.911 0.921 0.937 0.946 0.960
TimeSpan(Opt.Off)(ms) 1.56 8.74 58.44 389.68 2604.46 50
4G Public Wifi International
network conditions, which bring more challenges for us to
improvetheperformance.Figure14illustratesthecomparison
ofQoEmetricsforstate-of-the-artABRschemesundervarious
video types. We find that Comyco generalizes well under
all considered video scenarios, with the improvements on
average QoE of 2.7%-23.3% compared with model-based
ABR schemes and 2.8%-13.85% compared with Pensieve.
Specifically, Comyco can provide high-quality ABR services
under movies, news, and sports, which are all the scenarios
with frequent scene switches. We also find that Comyco fails
to demonstrate overwhelming performance in serving music
videos. It is really an interesting topic and we will discuss it
in future work.
5) Ablation Study: In this section, we set up several ex-
periments that aim to provide a thorough understanding of
Comyco, including its hyper-parameters and overhead. It is
worthnotingthatwehavecomputedtheoffline-optimalresults
via dynamic programming and complete network status [12]
before the experiment and treated it as a baseline.
Comparison of Different Future Step N. We report normal-
ized QoE and raw time span of Comyco with different N and
replay experience strategy in Table II. Results are collected
undertheOboedataset[17].Asshown,wefindthatexperience
replaycaneffectivelyhelpComycolearnbetter.Recallthatthe
instantsolverisonlyusedinthetrainingprocess,andComyco
will inference solely on the client side during the validation
process. Meanwhile, despite the outstanding performance of
Comyco with N=9, such scheme lacks the algorithmic ef-
ficiency and can hardly be deployed in practice. Thus, we
choose N=8 for harmonizing the performance and the cost.
Comyco with Different α. Further, we compare the normal-
izedQoEofComycowithdifferentαundertheOboedataset.
TABLEIII
COMYCOWITHDIFFERENTα.
α 0.1 0.01 0.001 0.0001 0
N=4 0.883 0.895 0.904 0.881 0.867
EoQ
egarevA
RobustMPC Pensieve Comyco
Fig.15. ComparingComycowithPensieveandRobustMPCunderthereal-
worldnetworkconditions.WetakeQoE=60asbaselines.
AslistedinTableIII,weconfirmthatα=0.001representsthe
best parameters for our work. Meanwhile, results also prove
the effectiveness of utilizing entropy loss (§IV-A3).
ComycoOverhead.Wecalculate[63]thenumberoffloating-
point operations (FLOPs) of Comyco and find that Comyco
has the computation of 229 Kflops, which is only 0.15% of
the light-weighted neural network ShuffleNet V2 [64] (146
Mflops). At the same time, we also discuss the model size
and time span of several representative ABR algorithms in
Table IV, in which the time span represents the total time
taken by the algorithm to execute about 7,000 times. The
experiment is done on the 12-core, Intel i7 CPUs with 32GB
RAM. As shown, the average execution time of Comyco on
thelaptopisonly0.4ms,yieldinganacceptableresult.Hence,
we believe that Comyco can be successfully deployed on the
PC and laptop, or even, on the mobile.
6) Comyco In the Real World: We establish a full-system
implementation to evaluate Comyco in the wild. The system
mainlyconsistsofavideoplayer,anABRserverandanHTTP
content server. On the server-side, we deploy an HTTP video
content Server. On the client-side, we modify Dash.js [25]
to implement our video player client and we use Chrome
to watch the video. Moreover, we implement Comyco as
a service on the ABR server. We evaluate the performance
of proposed schemes under various network conditions in-
cluding 4G/LTE network (from Beijing to Qingdao), WiFi
network (from Tsinghua’s public WiFi to Qingdao) and inter-
TABLEV
REAL-WORLDNETWORKMEASUREMENT.
RTT Avg.Throughput Network Std.Throughput
(ms) (KB/s)
4G 65.91 325.23 53.72
WiFi 15.58 292.98 27.65
Inter. 193.3 420.15 266.9

13
75
70
65 60
55
50 0 2 4 6 8 10 12
Time (Hour)
EoQ
egarevA
75
70 65
Lifelong Comyco Retrain-50
Fine-tune-50 Comyco-offline 60
0 2 4 6 8 10 12
Time (Hour)
Fig.16. ComparingComycowithseveralbase-
lines under Kwai dataset. Results are reported
withQoEcurvesoneachduration.
EoQ
egarevA
75
70
65 60
Lifelong Comyco Retrain-300 55
Fine-tune-300 50
45 0 2 4 6 8 10 12
Time (Hour)
Fig. 17. Comparison of Comyco and online-
optimalunderKwaidataset.Resultsarereported
withQoEcurvesoneachduration.
EoQ
egarevA
Lifelong Comyco
Lifelong Comyco without LwF
Fig. 18. Comparing the QoE of Comyco with
the one without using LwF method. Results are
collectedundertheKwaidataset.
national link (from Singapore to Beijing). Table V illustrates (cid:46) RobustMPC [10]:picksthebitratebythemodelpredictive
network status, where µ is the average throughput measured control method. As mentioned before, we also adopt C++
and σ represents standard deviation from the average. For to implement RobustMPC and leverage QoE (§V-A) to
v
each round, we randomly pick a scheme from candidates optimize the strategy.
and summarize the bitrate selected and rebuffering time for (cid:46) Comyco Offline Training (Comyco-offline): offline
each chunk. Each experiment takes about 2 hours. Figure 15 trains Comyco with inner-loop system’s network trace
showstheaverageQoEresultsforeachschemeunderdifferent dataset (§VI-A2). Note that we didn’t further tune the NN
network conditions. It’s clear that Comyco also outperforms model once Comyco’s model has been trained (§VI-A5).
previous state-of-the-art ABR schemes and it improves the Testing Methodology. Like previous experiments, we use
average QoE of 4.57%-9.93% compared with Pensieve and of QoE (§V-A)toevaluateeachscheme.Foreachdurationt,we
v
6.43%-9.46% compared with RobustMPC. train the baselines on the network throughput traces with the
range of t-th to t+1-th hour in the Kwai dataset, and validate
them on the network dataset within t+1-th to t+2-th hour.
B. Evaluation for Outer-loop System
In order to evaluate the fast convergence, we set the default
1) Implementation: We adopt C++ to implement the Op-
training epoch as 50. The training time lasts about 5 minutes
timal Estimator, and uses Python to construct the Trace Col-
onourdevice(§VI-A2),andweevaluatethetracesof12hours
lector. Note that the inner-loop system uses L (§10),
lifelong in one day. Furthermore, we also set training models in 300
ratherthanL (§8),totraintheNN,sincetheouter-loop
comyco epochs (Fine-tine-300 and Retrain-300) as strong baselines
system enables Comyco to achieve continual learning.
to better understand the gap between the proposed strategies
2) Experimental Setup: Considering the goal is to evaluate
and online-optimal policies. In this experiment, we treat the
the effectiveness of lifelong learning rather than the perfor-
Comyco with outer-loop system as lifelong Comyco.
mance of ABR streaming, we adopt virtual player (§VI-A2
3) Comparison of Different Outer-loop Strategies: Fig-
to validate the outer-loop system via trace-driven emulation.
ure 16 shows the average QoE curves of lifelong Comyco
Technically, unlike inner-loop system evaluation, we list net-
and other baselines on the Kwai dataset. We can see that
work trace dataset and baselines as follows:
lifelong Comyco always rivals or outperforms other ap-
Network Trace Dataset.Asdescribedbefore,thesub-system
proaches. Specifically, lifelong Comyco performs better than
is required to evaluate on continuous network throughput
theComyco-offlinescheme,withtheimprovementsonaverage
dataset. To that end, we utilize the large-scale network band-
QoEof1.07%-9.81%.Anotherobservationofthisexperiment
width dataset Kwai. The dataset contains over 860,000 traces,
demonstratestheweaknessoftheretrainandthefine-tuneap-
collected from about 10,000 unique users, totally 7 days from
proach:ifthenetworksituationchangesdramatically(seetime
various network conditions, including wired, WiFi, cellular
0 to time 2 in Figure 16), such algorithms will not be able to
network, and so forth (§III-B).
providereliableQoEtotheusers.Besides,fine-tune-50works
Baselines. In this work, we pick several representative outer-
wellwhenthenetworkdistributionchangessteadily(fromtime
loop system in different strategies as baselines.
4-7) since the training set and the validation set are almost in
(cid:46) Fine-tuning for 50 epochs (Fine-tune-50): for each period the same distribution.
t, we tune the trained model on the t-th hours’ network 4) lifelong Comyco vs. Comyco without LwF: In this ex-
traces for 50 epochs, lasting about 5 minutes for learning. periment,wevalidatetheeffectivenessoftheLwFmethod.As
(cid:46) Fine-tuning for 300 epochs (Fine-tune-300): we fine-tune shown in Figure 18, comparing the overall QoE performance
the trained model on network traces for 300 epochs for of lifelong Comyco and Comyco without LwF, we observe
each time period. Note that the training time lasts over 30 that lifelong Comyco improves the average QoE by 1.51%-
minutes, which is impractical in practice. 21.41% compared with the other methods. It makes sense
(cid:46) Re-train Comyco in 50 epochs (Retrain-50): for each since lifelong Comyco trains the NN with joint considering
duration t, we train Comyco on network traces in the range the previous network status and current network observed,
of t-th hours from scratch. whereas the other one diverges.
(cid:46) Re-train Comyco in 300 epochs (Retrain-300): we retrain 5) lifelong Comyco vs. Online Optimal: To better under-
Comyco for about 300 epochs since Comyco will be effi- standthegapbetweenlifelongComycoandonlineoptimal,we
cientlyconvergedwithanacceptableresults.Recallthatthe set up an experiment to evaluate the performance of lifelong
training time lasts over half of the time duration. Comyco, Fine-tune-300 as well as Retrain-300 (§VI-B2).

14
75
70
65 60
55 50
0 2 4 6 8 10 12
Time (Hour)
EoQ
egarevA
75
70 65 Lifelong Comyco 60
RobustMPC 55
50
0 2 4 6 8 10 12
Time (Hour)
Fig. 19. Comparison of Comyco and state-of-
the-artmodel-basedalgorithmRobustMPCunder
Kwaidataset.ResultsarealsoreportedwithQoE
curvesoneachduration.
EoQ egarevA 70 65
Thres=0.80 Thres=0.95 Thres=0.90 60
1 2 3 4 5 6 7
Day
Fig. 20. Comparing the QoE of Comyco with
the one without using LwF method. Results are
collectedundertheKwaidataset.
EoQ egarevA
Lifelong Comyco Comyco-Offline
Fig.21. ComparingtheperformanceofComyco
andComyco-Offlineperformsovermultipledays.
Results are collected over the same video description and VII. DISCUSSION
network traces. As illustrated in Figure 17, we show that
A. Theoretical Analysis
lifelong Comyco almost reaches the online optimal across
the entire session, with the decreases of only 0.02%-3.34% In this work, the Comyco’s inner-loop method (§IV-A4)
compared with Fine-tune-300, and 0.12%-3.33% in terms of can be defined as a no-regret algorithm because it produces
Retrain-300. In particular, we also find that lifelong Comyco a sequence of policies π ,π ,...,π such that the average
1 2 N
performsbetterthan16%ofthesessionsonFine-tune-300and regret w.r.t the best policy in hindsight goes to 0 as N goes
Retrain-300, where the QoE performance slightly increases to ∞: 1 (cid:80)N (cid:96) (π ) − min 1 (cid:80)N (cid:96) (π) ≤ γ , for
N i=1 i i π∈Π N i=1 i N
with the range of 0.17% to 1.53%. Such a conclusion also lim γ =0.Here(cid:96) representsanystronglyconvexsur-
N→∞ N n
proves the effectiveness of the lifelong learning method. rogatelosslossfunctions,suchasmeansquareerrorandcross
6) lifelongComycovs.RobustMPC: Besides,wealsocom- entropy error. The loss function (cid:96) is allowed to be optimized
n
pare the performance of lifelong Comyco with the current byanyoptimizationalgorithm(e.g.,Adam).Thus,inspiredby
state-of-the-art model-based approach RobustMPC. Results thepriorwork[38],letπˆ denotethepolicythatminimizesthe
i
are illustrated as QoE curves in Figure 19. As expected, we observed loss, we have to bound the total variation distance
can find that lifelong Comyco stands for the better scheme, between the distribution of states encountered by πˆ and π as
i i
outperformingRobustMPConaverageQoEof0.12%-5.70%. follows:
Ingeneral,suchobservationsprovethatagoodABRalgorithm
Lemma VII.1. ||d −d || ≤2β T.
is required to update dynamically for fitting the changes of πi πˆi 1 i
real-world network conditions [17].
Proof. Let dπ denote the average distribution of states if we
7) lifelong Comyco with Different Threshold Thres:
followpolicyπ forT steps,dreflectsthedistributionofstates
In this experiment, we aim to understand the influence of
over T steps conditioned on π picking expert’s policy π∗ at
thresholdThresforComyco.Indetail,weusethreethreshold i
least once over T steps, β represents the probability of π
candidates,involving{0.8,0.9,0.95}.Weevaluatethelifelong i
selecting π∗. We have:
Comyco with the proposed threshold on the same network
environmentsrespectively.ResultsareplottedinFigure20.As
||d −d ||
shown, we see that Thres=0.8 represents the best parameter πi πˆi 1
= ||(1−β )Td +(1−(1−β )T)d−d ||
of lifelong Comyco. Especially, Thres=0.8 works well in i πˆi i πˆi 1
time 2, while the other scheme fails to achieve a good result. = [1−(1−β i )T]||d−d πˆi || 1
It is notable that the choice of the value strongly depends on ≤ 2[1−(1−β )T]
i
the current task.
≤ 2[1−(1−β T)]
i
8) Evaluating lifelong Comyco Throughout the Entire Ses-
≤ 2β T.
sion: Finally, we discuss the behavior of lifelong Comyco i
and Comyco-Offline over multiple days. Recall that once the
Notice that in Comyco, β is NOT a fixed value and is
i
Comyco-Offline has been trained, the model is not allowed
strongly correlated with the entropy H(·) of the policy π :
θ
to be fine-tuned with any methods (we can also call this
β ∝H(·).Hence,it’scriticaltosettheproperentropyweight
i
zero-shot learning). Result in Figure 21 illustrates that the
α in the Comyco’s loss function (§VI-A5).
lifelong Comyco can always keep the performance within a
stable range. In contrast, Comyco-Offline sometimes fails to Let (cid:15) = min 1 (cid:80)N E [(cid:96)(s,π)] the loss of the
perform well on some days (e.g., the 4-th day) since it cannot N π∈Π N i=1 s∼dπi
best policy in hindsight after N iterations and let (cid:96) be an
max
adapt to time-vary network environments. In general, lifelong
upper bound on the loss and state s s.t. d (s)>0. We have:
Comyco improves the average QoE by 2.3%-4.2% compared
πˆi
with Comyco-Offline. Note that this is rather not a minor Theorem VII.1. For Comyco, there exists a policy πˆ ∈πˆ 1:N
improvement because it is difficult to improve the average s.t. E s∼dπˆ [(cid:96)(s,πˆ)] ≤ (cid:15) N +γ N + 2(cid:96) N max[n β +T (cid:80)N i=nβ+1 β i ],
performance of the huge dataset. For example, CS2P [5] for γ N the average regret of πˆ 1:N .
increased the QoE by 3.2% compared with MPC [10], and
ABRL [65] improved the video quality by 1.6% compared Proof. As mentioned before, Lemma VII.1 implies that
with Pensieve. E [(cid:96) (s,πˆ )]≤E [(cid:96) (s,πˆ )]+2(cid:96) min(1,β T).
s∼dπˆi i i s∼dπi i i max i

15
1.0
0.8
0.6
0.4
0.2
0.0
30 40 50 60 70 80
Average QoE
FDC
Sun et al. [5] assume that throughput factors can be ef-
ficiently captured by Hidden-Markov-Model (HMM), then
they optimize the model on the cloud with huge amounts
Comyco
of data. Oboe [17] attempts to place a dictionary, mapping
Comyco-PiTree
RobustMPC the throughput status {average throughput µ, throughput
BOLA variance σ} to the optimized traditional ABRs’ ( [9], [10])
Supervised
parameters, on the cloud for assisting traditional algorithms
to achieve higher performances in different network condi-
tions. Meanwhile, deploying ABRs on the cloud has also
Fig.22. ComparingtheQoEofComyco-PitreewiththetrainedComycoand
RobustMPC.ResultsarecollectedundertheHSDPAdataset. been considered in the industry. Thomas et al. [71], [72]
proposed the Server and Network-assisted DASH (SAND)
architecture to overcome the fact that the client-driven ap-
min E [(cid:96)(s,πˆ)]
πˆ∈πˆ1:N s∼dπˆ proachofDASHleftlesscontroltothenetworkandservice
≤ N 1 (cid:80)N i=1 E s∼dπˆi ((cid:96)(s,πˆ i )) providers.RESA[73]employsalearning-basedABRproxy
≤ 1 (cid:80)N [E ((cid:96)(s,πˆ ))+2(cid:96) min(1,β T)] to make a suitable decision for each client. To this end,
N i=1 s∼dπi i max i
≤ γ
N
+ 2(cid:96)
N
max[n
β
+ (cid:80)N
i=nβ+1
β
i
T]+min
π∈Π
(cid:80)N
i=1
(cid:96)
i
(π) w
ed
e
ge
be
i
l
s
ie
a
v
l
e
so
th
a
a
p
t
r
d
a
e
c
p
ti
l
c
o
a
y
l
in
w
g
ay
an
fo
A
r
B
to
R
da
s
y
e
’
r
s
vi
d
c
e
e
v
o
ic
n
e
t
a
h
n
e
d
s
n
er
e
v
tw
er
o
o
rk
r
= γ
N
+(cid:15)
N
+ 2(cid:96)
N
max[n
β
+ (cid:80)N
i=nβ+1
β
i
T]
environments.
Under an error reduction assumption that for any input
distribution, there is some policy π ∈ Π that achieves sur- VIII. RELATEDWORK
rogate loss of (cid:15), which implies we are guaranteed to find a A. ABR schemes
policy πˆ that achieves (cid:15) under H(·) → 0. In Comyco, the
Client-based ABR algorithms [2] are mainly organized into
policy’sentropyisallowedtodecreaseeffectivelyviathecross
two types: model-based and learning-based. The model-based
entropy method. Moreover, many no-regret algorithms (e.g.,
algorithmusesheuristicstoconstructamodel,asthelearning-
DAgger [38]) guarantee that if β is chosen to be the form
i based method adopts deep learning to generalize a strategy
of (1 − α)i−1, in which α is a constant hyper-parameter,
from tabular rasa.
then the method need at least O˜(T) iterations to make γ
N Model-based. The development of ABR algorithms begins
negligible.
withtheideaofpredictingthroughput.PANDA[6]predictsthe
future throughput for eliminating the ON-OFF steady issue.
B. Practical Implementation
FESTIVE [7] estimates future throughput via the harmonic
Learning-based ABR algorithms are struggling with its mean of the throughput measured for the past chunk down-
deployability. Specifically, Pensieve [12] is deployed on the loads. However, due to the lack of throughput estimation
server to avoid high computational costs on the client-side. method currently, these approaches still result in poor ABR
However, in practice, most ABR algorithms are executed in performance. Meanwhile, most video client leverages a play-
thefront-endtoaverttheextralatencyconnectingtotheback- back buffer to store the video content downloaded from the
end[66],[67].Thus,suchABRpolicyframeworks([12],[17]) servertemporarily.BBA[8]proposesalinearcriterionthresh-
aretheoreticallyeffectivebutimpractical[65].Inthispaper,as old to control the available playback buffer size. BOLA [9]
muchasthisworkisNOTfocusedonthedeployableproblem turns the ABR problem into a utility maximization problem
oflearning-basedABRalgorithms,westillgivesomepractical and solve it by using the Lyapunov function. However, the
ideas for implementation. buffer-based approach fails to tackle the long-term bandwidth
• We argue that deploying the model on the client is imprac- fluctuation problem. Hence, mixed model-based approaches,
tical since the computational cost is rather small for today’s e.g., MPC [10], select bitrate for the next chunk by adjusting
mobile (§VI-A5). What’s more, the user will optionally its throughput discount factor based on past prediction errors
download the small-sized model, where the model size is and estimating its playback buffer size. Nevertheless, these
even 50% smaller than the lowest video chunk size (by approachesrequirecarefultuningbecausetheyrelyonparam-
Tensorflow.js [68]). eters that are quite sensitive to network conditions, resulting
• SeveralpracticalABRschemes(i.e.,PiTree[69],LIME[70] in poor performance in unexpected network environments.
and ABRL [65]) have been proposed to distill the NN What’smore,Akhtaretal.[17]proposeanauto-tuningmethod
to a practical decision tree, an interpretable tabular, or a to improve model-based ABR’s performance.
linear-based formula. Such schemes are also acceptable for Learning-based: Several attempts have been made to opti-
appending into the Comyco system. For example, we use mize the ABR algorithm based on the RL method due to the
PiTree [69] to distill the trained Comyco to a decision tree difficulty of tuning mixed approaches for handling different
model and show the CDF results on Figure 22, where the network conditions. Pensieve [12] is a system that leverages
results are collected under the HSDPA dataset. We can see RL to select bitrate for future video chunks. D-DASH [13]
that Comyco-Pitree decreases the model size of about 97% usestheDeepQ-learningmethodtoperformacomprehensive
with preserving the overall performance. evaluation. Tiyuntsong optimizes itself towards a rule or a
• Recent years have also seen several schemes that deploy specific reward via the competition with two agents under the
the ABR algorithm as a service on the cloud. For example, same network condition [15].

16
In general, existing ABR algorithms seldom consider the ACKNOWLEDGEMENT
timevaryofnetworkstatus.Inparticular,learning-basedABR
We thank the anonymous reviewer for the valuable feed-
schemes fail to tackle the sample efficiency problem.
back. This work was supported by the National Key R&D
ProgramofChina(No.2018YFB1003703),NSFCunderGrant
B. Imitation Learning meets Networking
61521002, Beijing Key Lab of Networked Multimedia, and
Imitation learning [74], [75] is the process by which an Kuaishou-Tsinghua Joint Project (No. 20192000456). This
agent tries to learn how to perform a certain task using paperextends[80]byaddinglifelonglearningmethodswhich
informationgeneratedbyanother,oftenmoreexpertagentper- significantlyimproveslearning-basedABRalgorithmstowork
forming that same task. Till now, imitation learning has been in practice.
widely used in various fields including networking scheduling
andnetworkcongestioncontrolschemes.Tangetal.[76]pro- REFERENCES
poseareal-timedeeplearning-basedintelligentnetworktraffic
[1] Cisco, “Cisco visual networking index: Forecast and
control method to represent the considered Wireless Mesh methodology, 2016-2021,” 2017. [Online]. Available:
Network(WMN)backboneviaimitationlearning.Indigo[77] https://www.cisco.com/c/dam/en/us/solutions/collateral/service-
provider/visual-networking-index-vni/complete-white-paper-c11-
uses DAgger [38] to train a congestion-control NN scheme in
481360.pdf
the offline network emulator. [2] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann,
“Asurveyonbitrateadaptationschemesforstreamingmediaoverhttp,”
C. Lifelong learning methods IEEECommunicationsSurveys&Tutorials,2018.
[3] M. Licciardello, M. Gru¨ner, and A. Singla, “Understanding video
Lifelong learning (or namely continual learning and incre- streaming algorithms in the wild,” arXiv preprint arXiv:2001.02951,
mental learning) has become one of the research hotspots 2020.
[4] T.-Y. Huang, C. Ekanadham, A. J. Berglund, and Z. Li, “Hindsight:
for tackling catastrophic forgetting problem. Recently, several Evaluate video bitrate adaptation at scale,” in Proceedings of the
approaches have been proposed to extend the loss function 10th ACM Multimedia Systems Conference, ser. MMSys ’19. New
York, NY, USA: ACM, 2019, pp. 86–97. [Online]. Available:
with additional terms for guaranteeing the performance on
http://doi.acm.org/10.1145/3304109.3306219
previous tasks, e.g., Learning without Forgetting (LwF) [23] [5] Y. Sun and et al., “Cs2p: Improving video bitrate selection and adap-
uses outputs of the old models as soft targets of old tasks. tation with data-driven throughput prediction,” in SIGCOMM 2016.
ACM,2016,pp.272–285.
These soft targets are considered as a substitute for the
[6] Z. Li, X. Zhu, J. Gahm, R. Pan, H. Hu, A. C. Begen, and D. Oran,
data of previous tasks, which cannot be accessed in lifelong “Probe and adapt: Rate adaptation for http video streaming at scale,”
learning settings. Another kind of lifelong learning methods IEEEJournalonSelectedAreasinCommunications,vol.32,no.4,pp.
719–733,2014.
estimatetheimportanceofmodelparameterswithspecifically
[7] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and
designed mechanisms and apply an individual penalty for stability in http-based adaptive video streaming with festive,” TON,
each previous task, including Elastic Weights Consolidation vol.22,no.1,pp.326–340,2014.
[8] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,andM.Watson,“A
(EWC) [78], Synaptic Intelligence (SI) and Memory Aware
buffer-based approach to rate adaptation: Evidence from a large video
Synaptic (MAS) [79]. However, such lifelong learning meth- streamingservice,”ACMSIGCOMMComputerCommunicationReview,
vol.44,no.4,pp.187–198,2015.
odsusuallysufferfromakeyissue:onemethodthatperforms
[9] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal
well in some experimental settings may fail in others [37]. bitrateadaptationforonlinevideos,”inINFOCOM2016,IEEE. IEEE,
2016,pp.1–9.
IX. CONCLUSION [10] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
approach for dynamic adaptive video streaming over http,” in ACM
In this work, we propose Comyco, a learning-based ABR SIGCOMMComputerCommunicationReview. ACM,2015,pp.325–
system which aim to thoroughly improve the performance 338.
[11] K.Spiteri,R.Sitaraman,andD.Sparacio,“Fromtheorytopractice:im-
of learning-based algorithm. In general, Comyco makes the
provingbitrateadaptationinthedashreferenceplayer,”inProceedings
contributions as follows: First, we construct Comyco as a ofthe9thMMSys. ACM,2018,pp.123–137.
video quality-based ABR system, including its NN architec- [12] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream-
ing with pensieve,” in Proceedings of the 2017 ACM SIGCOMM
tures, datasets and QoE metrics. With trace-driven emulation
Conference. ACM,2017,pp.197–210.
and real-world deployment. Second, to overcome the sample [13] M.Gadaleta,F.Chiariotti,M.Rossi,andA.Zanella,“D-dash:Adeep
inefficiency problem, we leverage imitation learning method q-learningframeworkfordashvideostreaming,”IEEETransactionson
CognitiveCommunicationsandNetworking,vol.3,no.4,pp.703–718,
to guide the algorithm to explore and exploit the better
Dec2017.
policy rather than stochastic sampling. Third, through data- [14] S.Sengupta,N.Ganguly,S.Chakraborty,andP.De,“Hotdash:Hotspot
drivenanalysiswefindComycoshouldbeupdatedcontinually awareadaptivevideostreamingusingdeepreinforcementlearning,”in
2018IEEE26thInternationalConferenceonNetworkProtocols(ICNP).
over time. Thus, we present lifelong learning-based Comyco,
IEEE,2018,pp.165–175.
aiming to improve its adaption on network status. Massive of [15] T.Huang,X.Yao,C.Wu,R.-X.Zhang,andL.Sun,“Tiyuntsong:Aself-
experimentalresultsshowthatComycosignificantlyimproves play reinforcement learning approach for abr video streaming,” arXiv
preprintarXiv:1811.06166,2018.
the performance, effectively accelerates the training process, [16] “Kuaishou,”2019.[Online].Available:https://www.kuaishou.com
and achieves lifelong training on the entire session. [17] Z.Akhtarandetal.,“Oboe:auto-tuningvideoabralgorithmstonetwork
conditions,”inSIGCOMM2018. ACM,2018,pp.44–58.
Additional research will focus on i) applying exogenous
[18] T.Huang,R.-X.Zhang,C.Zhou,andL.Sun,“Qarc:Videoqualityaware
features(i.e.,date,hour,etc)intotheNN,ii)deployingfeasible ratecontrolforreal-timevideostreamingbasedondeepreinforcement
personalized Comyco framework, iii) demystifying the key learning,”in2018ACMMultimediaConferenceonMultimediaConfer-
ence. ACM,2018,pp.1208–1216.
principle of Comyco, as well as iv) developing a practical
[19] R.Mendonca,A.Gupta,R.Kralev,P.Abbeel,S.Levine,andC.Finn,
scheme for low latency live streaming scenario. “Guidedmeta-policysearch,”arXivpreprintarXiv:1904.00956,2019.

17
[20] R. Rassool, “Vmaf reproducibility: Validating a perceptual practical [45] A.HoreandD.Ziou,“Imagequalitymetrics:Psnrvs.ssim,”pp.2366–
video quality metric,” in Broadband Multimedia Systems and Broad- 2369,2010.
casting(BMSB),2017IEEEInternationalSymposiumon. IEEE,2017, [46] T. Abar, A. B. Letaifa, and S. El Asmi, “Machine learning based
pp.1–2. qoe prediction in sdn networks,” in 2017 13th International Wireless
[21] Z.Duanmu,A.Rehman,andZ.Wang,“Aquality-of-experiencedatabase CommunicationsandMobileComputingConference(IWCMC). IEEE,
for adaptive video streaming,” IEEE Transactions on Broadcasting, 2017,pp.1395–1400.
vol.64,no.2,pp.474–487,June2018. [47] A. Aaron, Z. Li, M. Manohara, J. Y. Lin, E. C.-H. Wu, and C.-C. J.
[22] T. Osa, J. Pajarinen, G. Neumann, J. A. Bagnell, P. Abbeel, J. Peters Kuo, “Challenges in cloud based ingest and encoding for high quality
et al., “An algorithmic perspective on imitation learning,” Foundations streaming media,” in 2015 IEEE International Conference on Image
andTrends(cid:13)R inRobotics,vol.7,no.1-2,pp.1–179,2018. Processing(ICIP). IEEE,2015,pp.1732–1736.
[23] Z.LiandD.Hoiem,“Learningwithoutforgetting,”IEEETransactions [48] A. Rehman, K. Zeng, and Z. Wang, “Display device-adapted video
onPatternAnalysisandMachineIntelligence,2017. quality-of-experience assessment,” in Human Vision and Electronic
[24] “Httplivestreaming,”https://developer.apple.com/streaming/,2019. ImagingXX,vol.9394. InternationalSocietyforOpticsandPhotonics,
[25] “Dashindustryforum—catalyzingtheadoptionofmpeg-dash,”2019. 2015,p.939406.
[Online].Available:https://dashif.org/ [49] Z.Duanmu,W.Liu,D.Chen,Z.Li,Z.Wang,Y.Wang,andW.Gao,“A
[26] M. F. B. Report, “Raw data measuring broadband america 2016,” knowledge-driven quality-of-experience model for adaptive streaming
https://www.fcc.gov/reports-research/reports/measuring-broadband- videos,”arXivpreprintarXiv:1911.07944,2019.
america/raw-data-measuring-broadband-america-2016, 2016, [Online; [50] A.RehmanandZ.Wang,“Perceptualexperienceoftime-varyingvideo
accessed19-July-2016]. quality,”in2013FifthInternationalWorkshoponQualityofMultimedia
[27] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute Experience(QoMEX). IEEE,2013,pp.218–223.
pathbandwidthtracesfrom3gnetworks:analysisandapplications,”in [51] “Youtube,”2019.[Online].Available:https://www.youtube.com
Proceedings of the 4th ACM Multimedia Systems Conference. ACM, [52] FFmpeg,“Ffmpeg.”[Online].Available:http://ffmpeg.org/
2013,pp.114–118. [53] GPAC,“Mp4box.”[Online].Available:https://gpac.wp.imt.fr/mp4box/
[28] A.Bentaleb,A.C.Begen,andR.Zimmermann,“Sdndash:Improving [54] T. Huang, “Comyco video description dataset,” https://github.com/
qoe of http adaptive streaming using software defined networking,” in godka/Comyco-Video-Description-Dataset/,2020.
ProceedingsofACMMultiMedia2016. ACM,2016,pp.1296–1305. [55] M.Abadi,P.Barham,J.Chen,Z.Chen,A.Davis,J.Dean,M.Devin,
[29] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis, S. Ghemawat, G. Irving, M. Isard et al., “Tensorflow: A system for
and K. Winstein,“Learning in situ: a randomizedexperiment in video large-scalemachinelearning.”inOSDI,vol.16,2016,pp.265–283.
streaming,” in 17th {USENIX} Symposium on Networked Systems De- [56] Y. Tang, “Tf. learn: Tensorflow’s high-level module for distributed
signandImplementation({NSDI}20),2019. machinelearning,”arXivpreprintarXiv:1612.04251,2016.
[30] Mao, “hongzimao/pensieve,” Jul 2017. [Online]. Available: https: [57] D.M.Beazleyetal.,“Swig:Aneasytousetoolforintegratingscripting
//github.com/hongzimao/pensieve languageswithcandc++.”inTcl/TkWorkshop,1996,p.43.
[31] Z. Wang, “Video qoe: Presentation quality vs. [58] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
playback smoothness,” Jul 2017. [Online]. Avail- arXivpreprintarXiv:1412.6980,2014.
able: https://www.ssimwave.com/science-of-seeing/video-quality-of- [59] T.Huang,“Comyco,”https://github.com/thu-media/comyco/,2020.
experience-presentation-quality-vs-playback-smoothness/ [60] R.Netravali,A.Sivaraman,S.Das,A.Goyal,K.Winstein,J.Mickens,
[32] Y.Qin,S.Hao,K.R.Pattipati,F.Qian,S.Sen,B.Wang,andC.Yue, andH.Balakrishnan,“Mahimahi:accuraterecord-and-replayforhttp,”
“Abrstreamingofvbr-encodedvideos:characterization,challenges,and pp.417–429,2015.
solutions,”inProceedingsofCoNeXT2018. ACM,2018,pp.366–378. [61] Usc-Nsl, “Usc-nsl/oboe,” Oct 2018. [Online]. Available: https://github.
[33] Z. Duanmu, K. Ma, and Z. Wang, “Quality-of-experience of adaptive com/USC-NSL/Oboe
videostreaming:Exploringthespaceofadaptations,”inProceedingsof [62] P. K. Yadav, A. Shafiei, and W. T. Ooi, “Quetra: A queuing theory
the 25th ACM international conference on Multimedia. ACM, 2017, approach to dash rate adaptation,” in Proceedings of the 25th ACM
pp.1752–1760. internationalconferenceonMultimedia,2017,pp.1130–1138.
[34] H. Mao, S. B. Venkatakrishnan, M. Schwarzkopf, and M. Alizadeh, [63] P. Molchanov, S. Tyree, T. Karras, T. Aila, and J. Kautz, “Pruning
“Variancereductionforreinforcementlearningininput-drivenenviron- convolutional neural networks for resource efficient inference,” arXiv
ments,”internationalconferenceonlearningrepresentations,2019. preprintarXiv:1611.06440,2016.
[35] R.S.SuttonandA.G.Barto,Reinforcementlearning:Anintroduction. [64] N. Ma, X. Zhang, H.-T. Zheng, and J. Sun, “Shufflenet v2: Practical
MITpress,2018. guidelines for efficient cnn architecture design,” in Proceedings of the
[36] M.Laskey,J.Lee,R.Fox,A.Dragan,andK.Goldberg,“Dart:Noisein- EuropeanConferenceonComputerVision(ECCV),2018,pp.116–131.
jectionforrobustimitationlearning,”arXivpreprintarXiv:1703.09327, [65] H.Mao,S.Chen,D.Dimmery,S.Singh,D.Blaisdell,Y.Tian,M.Al-
2017. izadeh,andE.Bakshy,“Real-worldvideoadaptationwithreinforcement
[37] R. Kemker, M. McClure, A. Abitino, T. L. Hayes, and C. Kanan, learning,”inICML2019Workshop,2019.
“Measuringcatastrophicforgettinginneuralnetworks,”inThirty-second [66] S.Akhshabi,A.C.Begen,andC.Dovrolis,“Anexperimentalevaluation
AAAIconferenceonartificialintelligence,2018. of rate-adaptation algorithms in adaptive streaming over http,” in Pro-
[38] S.Ross,G.Gordon,andD.Bagnell,“Areductionofimitationlearning ceedingsofthesecondannualACMconferenceonMultimediasystems.
and structured prediction to no-regret online learning,” in Proceedings ACM,2011,pp.157–168.
ofthefourteenthinternationalconferenceonartificialintelligenceand [67] I.Sodagar,“Thempeg-dashstandardformultimediastreamingoverthe
statistics,2011,pp.627–635. internet,”IEEEmultimedia,vol.18,no.4,pp.62–67,2011.
[39] J.Chung,C.Gulcehre,K.Cho,andY.Bengio,“Empiricalevaluationof [68] D. Smilkov, N. Thorat, Y. Assogba, A. Yuan, N. Kreeger, P. Yu,
gatedrecurrentneuralnetworksonsequencemodeling,”arXiv:Neural K.Zhang,S.Cai,E.Nielsen,D.Soergeletal.,“Tensorflow.js:Machine
andEvolutionaryComputing,2014. learning for the web and beyond,” arXiv preprint arXiv:1901.05350,
[40] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley, 2019.
D.Silver,andK.Kavukcuoglu,“Asynchronousmethodsfordeeprein- [69] Z.Meng,J.Chen,Y.Guo,andM.Xu,“Pitree:Practicalimplementation
forcementlearning,”inInternationalConferenceonMachineLearning, of abr algorithms using decision trees,” in 2019 ACM Multimedia
2016,pp.1928–1937. ConferenceonMultimediaConference. ACM,2019.
[41] V.Mnih,K.Kavukcuoglu,D.Silver,A.Graves,I.Antonoglou,D.Wier- [70] A.Dethise,M.Canini,andS.Kandula,“Crackingopentheblackbox:
stra, and M. Riedmiller, “Playing atari with deep reinforcement learn- What observations can tell us about reinforcement learning agents,” in
ing,”arXivpreprintarXiv:1312.5602,2013. Proceedingsofthe2019WorkshoponNetworkMeetsAI&ML. ACM,
[42] X.Yao,T.Huang,C.Wu,R.-X.Zhang,andL.Sun,“Adversarialfeature 2019,pp.29–36.
alignment: Avoid catastrophic forgetting in incremental task lifelong [71] E. Thomas, M. van Deventer, T. Stockhammer, A. C. Begen, and
learning,”Neuralcomputation,vol.31,no.11,pp.2266–2291,2019. J.Famaey,“Enhancingmpegdashperformanceviaserverandnetwork
[43] J. Benesty, J. Chen, Y. Huang, and I. Cohen, “Pearson correlation assistance,”2015.
coefficient,”inNoisereductioninspeechprocessing. Springer,2009, [72] E. Thomas, M. van Deventer, T. Stockhammer, A. C. Begen, M.-L.
pp.1–4. Champel,andO.Oyman,“Applicationsanddeploymentsofserverand
[44] P.G.Pereira,A.Schmidt,andT.Herfet,“Cross-layereffectsontraining networkassisteddash(sand),”2016.
neural algorithms for video streaming,” in Proceedings of the 28th [73] Y.Wang,H.Wang,J.Shang,andH.Tuo,“Resa:Areal-timeevaluation
ACM SIGMM Workshop on Network and Operating Systems Support systemforabr,”in2019IEEEInternationalConferenceonMultimedia
forDigitalAudioandVideo. ACM,2018,pp.43–48. andExpo(ICME). IEEE,2019,pp.1846–1851.

18
[74] A.Hussein,M.M.Gaber,E.Elyan,andC.Jayne,“Imitationlearning:A Rui-Xiao Zhang received his B.E degree in Elec-
surveyoflearningmethods,”ACMComputingSurveys(CSUR),vol.50, tronicEngineeringDepartmentinTsinghuaUniver-
no.2,p.21,2017. sity in 2017. Currently, he is pursuing his Ph.D
[75] F. Torabi, G. Warnell, and P. Stone, “Recent advances in imitation candidate in Department of Computer Science and
PLACE
learningfromobservation,”arXivpreprintarXiv:1905.13566,2019. Technology, Tsinghua University, China. His re-
| [76] | F. Tang, | B. Mao, | Z. M. | Fadlullah, | N. Kato, | O.  | Akashi, | T. Inoue, | PHOTO |                  |     |        |         |         |          |
| ---- | -------- | ------- | ----- | ---------- | -------- | --- | ------- | --------- | ----- | ---------------- | --- | ------ | ------- | ------- | -------- |
|      |          |         |       |            |          |     |         |           |       | search interests | lie | in the | area of | content | delivery |
and K. Mizutani, “On removing routing protocol from future wireless HERE networks,theoptimizationofmultimediastreaming
networks: A real-time deep learning approach for intelligent traffic and reinforcement learning. He received Best Stu-
control,” IEEE Wireless Communications, vol. 25, no. 1, pp. 154–160, dent Paper Awards presented by ACM Multimedia
February2018.
System2019Workshop.
[77] F.Y.Yan,J.Ma,G.D.Hill,D.Raghavan,R.S.Wahby,P.Levis,and
|     | K. Winstein,       | “Pantheon: | the     | training | ground | for       | internet | congestion- |     |     |     |     |     |     |     |
| --- | ------------------ | ---------- | ------- | -------- | ------ | --------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     | control research,” |            | in 2018 | {USENIX} | Annual | Technical |          | Conference  |     |     |     |     |     |     |     |
({USENIX}{ATC}18),2018,pp.731–743.
| [78] | J. Kirkpatrick,     | R.        | Pascanu,     | N. Rabinowitz, |             | J. Veness, | G.                | Desjardins, |     |     |     |     |     |     |     |
| ---- | ------------------- | --------- | ------------ | -------------- | ----------- | ---------- | ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|      | A. A. Rusu,         | K. Milan, | J.           | Quan,          | T. Ramalho, | A.         | Grabska-Barwinska |             |     |     |     |     |     |     |     |
|      | et al., “Overcoming |           | catastrophic |                | forgetting  | in neural  | networks,”        | Pro-        |     |     |     |     |     |     |     |
ceedingsofthenationalacademyofsciences,p.201611835,2017.
|     |     |     |     |     |     |     |     |     |     | Chenglei | Wu received | the | Master | degrees | in Ts- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------ | ------- | ------ |
[79] R.Aljundi,F.Babiloni,M.Elhoseiny,M.Rohrbach,andT.Tuytelaars,
|     |     |     |     |     |     |     |     |     |     | inghua University. |     | He is currently |     | a Ph.D with | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------------- | --- | ----------- | --- |
“Memoryawaresynapses:Learningwhat(not)toforget,”inProceedings
|     |                 |            |     |             |     |        |         |           |     | Computer | Science | and Technology |     | Department | of  |
| --- | --------------- | ---------- | --- | ----------- | --- | ------ | ------- | --------- | --- | -------- | ------- | -------------- | --- | ---------- | --- |
|     | of the European | Conference |     | on Computer |     | Vision | (ECCV), | 2018, pp. |     |          |         |                |     |            |     |
TsinghuaUniversity.Hisresearchinterestsfocuson
|     | 139–154. |     |     |     |     |     |     |     | PLACE |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[80] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco: 360 video streaming, adaptive video streaming and
|     |               |          |       |           |     |           |            |       | PHOTO | routing. |     |     |     |     |     |
| --- | ------------- | -------- | ----- | --------- | --- | --------- | ---------- | ----- | ----- | -------- | --- | --- | --- | --- | --- |
|     | Quality-aware | adaptive | video | streaming | via | imitation | learning,” | arXiv |       |          |     |     |     |     |     |
HERE
preprintarXiv:1908.02270,2019.
|     |     |     | Tianchi | Huang | received | his | M.E degree | in the |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | ----- | -------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
DepartmentofComputerScienceandTechnologyin
GuizhouUniversityin2018.CurrentlyheisaPh.D
studentintheDepartmentofComputerScienceand
PLACE
TechnologyatTsinghuaUniversity,advisedbyProf. Bing Yu , the leader of the audio and video
PHOTO
LifengSun.Hisresearchworkfocusesonthemul- technology of Kuaishou, graduated from Tsinghua
HERE timedia network streaming, including transmitting University, has many years of experience in the
streams,andedge-assistedcontentdelivery.Hehas video and streaming media industry. He is good at
been the reviewer for IEEE TRANSACTIONS ON PLACE usingadvancedInternettechnologyanddata-driven
PHOTO
VEHICULARTECHNOLOGYandIEEETRANS- conceptstooptimizethesystemforprovidingusers
|     |     |     | ACTIONSONMULTIMEDIA. |     |     |     |     |     | HERE |     |     |     |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
withthebestQoE.PriortojoiningKuaishou,heled
videotechnologyandinfrastructureteamsatmulti-
nationalcompaniessuchasHuluandFreeWheel.
|     |     |     | Chao Zhou | receivedhisPh.D.degreefromtheIn- |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stituteofComputerScienceandTechnology,Peking
|     |       |     | University,  | Beijing,   | China,   | in         | 2014. He     | has been   |     |            |             |      |          |            |         |
| --- | ----- | --- | ------------ | ---------- | -------- | ---------- | ------------ | ---------- | --- | ---------- | ----------- | ---- | -------- | ---------- | ------- |
|     |       |     | with Beijing | Kuaishou   |          | Technology | Co.,         | Ltd. as an |     |            |             |      |          |            |         |
|     | PLACE |     | Algorithm    | Scientist. | Before   | joining    | Kuaishou,    | he         |     |            |             |      |          |            |         |
|     | PHOTO |     |              |            |          |            |              |            |     | Lifeng Sun | received    | the  | B.S and  | Ph.D       | degrees |
|     |       |     | was a        | Senior     | Research | Engineer   | with         | the Media  |     |            |             |      |          |            |         |
|     | HERE  |     |              |            |          |            |              |            |     | in system  | engineering | from | National | University | of      |
|     |       |     | Technology   | Lab,       | CRI,     | Huawei     | Technologies | CO.,       |     |            |             |      |          |            |         |
LTD, Beijing, China. Dr. Zhou’s research interests Defense Technology, Changsha, Hunan, China, in
includeHTTPvideostreaming,jointsource-channel 1995 and 2000, respectively. He joined Tsinghua
|     |     |     |         |                |     |                |     |          | PLACE | University                                 | since | 2001. He | is currently | a Professor |     |
| --- | --- | --- | ------- | -------------- | --- | -------------- | --- | -------- | ----- | ------------------------------------------ | ----- | -------- | ------------ | ----------- | --- |
|     |     |     | coding, | and multimedia |     | communications |     | and pro- |       |                                            |       |          |              |             |     |
|     |     |     |         |                |     |                |     |          | PHOTO | withtheComputerScienceandTechnologyDepart- |       |          |              |             |     |
cessing.HehasbeenthereviewerforIEEETRANS-
|     |     |     |     |     |     |     |     |     | HERE | mentofTsinghuaUniversity,Beijing. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------------------------------- | --- | --- | --- | --- | --- |
ACTIONSONCIRCUITSANDSYSTEMSFORVIDEOTECHNOLOGY,
IEEETRANSACTIONSONMULTIMEDIA,IEEETRANSACTIONSON Dr.Sun’sresearchinterestsincludetheareaofnet-
WIRELESSCOMMUNICATIONandsoon.HereceivedBestPaperAward workedmultimedia,videostreaming,3D/multiview
videocoding,multimediacloudcomputing,andso-
presentedbyIEEEVCIP2015,andBestStudentPaperAwardspresentedby
cialmedia.
IEEEVCIP2012.
APPENDIXA
SUMMARYOFSTATISTICSFROMTHEDATASET
XinYaoiscurrentlyaPh.D.candidateintheDepart-
ment of Computer Science and Technology at Ts- Type DatasetName
inghuaUniversity,advisedbyProf.LifengSun.He NetworkTraces FCC[27],HSDPA[26],Oboe[61]
receivedhisbachelor’sdegreefromtheDepartment
|     |       |     |             |         |     |            |     |             | LifelongTrainingTraces |     |     | Kwai(§II) |     |     |     |
| --- | ----- | --- | ----------- | ------- | --- | ---------- | --- | ----------- | ---------------------- | --- | --- | --------- | --- | --- | --- |
|     | PLACE |     | of Computer | Science | and | Technology |     | at Tsinghua |                        |     |     |           |     |     |     |
PHOTO University in 2016. His research interests focus on VideoDescriptionDatasets CVDD[54]
HERE
federated learning, lifelong/continual learning, and QoEDatabaseforABR SQoEIII[21]
transferlearning.