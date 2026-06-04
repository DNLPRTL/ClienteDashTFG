| Buffer |     | Awareness |          |     |     | Neural |     | Adaptive |             | Video |     |     | Streaming |     |     |
| ------ | --- | --------- | -------- | --- | --- | ------ | --- | -------- | ----------- | ----- | --- | --- | --------- | --- | --- |
|        | for |           | Avoiding |     |     | Extra  |     | Buffer   | Consumption |       |     |     |           |     |     |
Tianchi Huang1∗, Chao Zhou2∗, Rui-Xiao Zhang1, Chenglei Wu1, Lifeng Sun2,3,4∗
20092201.3202.93935MOCOFNI/9011.01 :IOD | EEEI 3202© 00.13$/32/2-4143-3053-8-979 | snoitacinummoC retupmoC no ecnerefnoC EEEI - 3202 MOCOFNI EEEI
1Department of Computer Science and Technology, Tsinghua University 2Beijing Kuaishou Technology Co., Ltd.
3BNRist, 4Key
Laboratory of Pervasive Computing (Tsinghua University), Ministry of Education, China
∗Corresponding Authors. {htc19@mails.,sunlf@}tsinghua.edu.cn, zhouchao@kuaishou.com
Abstract—Adaptivevideostreaminghasalreadybeenamajor therealchallengefortoday’sABRalgorithmsbeyondgaining
schemetotransmitvideoswithhighqualityofexperience(QoE). highperformance?Withempiricalanalysis,wehaveobserved
| However,    | the improvement |       | of        | network     | traffics | and        | the         | high          |      |            |       |             |              |          |        |
| ----------- | --------------- | ----- | --------- | ----------- | -------- | ---------- | ----------- | ------------- | ---- | ---------- | ----- | ----------- | ------------ | -------- | ------ |
|             |                 |       |           |             |          |            |             | that existing | ABR  | algorithms |       | immediately |              | download | each   |
| compression | efficiency      |       | of videos | enable      | clients  | to         | accumulate  |               |      |            |       |             |              |          |        |
|             |                 |       |           |             |          |            |             | chunk once    | the  | previous   | chunk | finishes    | downloading, |          | which  |
| too much    | buffer,         | which | might     | cause       | colossal | data waste | if users    |               |      |            |       |             |              |          |        |
|             |                 |       |           |             |          |            |             | often occurs  | huge | data       | waste | if users    | stop         | watching | videos |
| close the   | session         | early | before    | the session | ends.    | In         | this paper, |               |      |            |       |             |              |          |        |
we consider buffer-aware adaptive bitrate (ABR) mechanisms unexpectedly (§II-B). Motivated by the success of conven-
to overcome the above concerns. Formulating the buffer-aware tionalfour-stepABRmodels[7],weconsiderjointlyadjusting
rateadaptationproblemasmulti-objectiveoptimization,wepro-
|                  |     |        |               |     |                |     |          | the maximum | buffer | size | and | the | next chunks’ |     | bitrates to |
| ---------------- | --- | ------ | ------------- | --- | -------------- | --- | -------- | ----------- | ------ | ---- | --- | --- | ------------ | --- | ----------- |
| pose DeepBuffer, |     | a deep | reinforcement |     | learning-based |     | approach |             |        |      |     |     |              |     |             |
tackletheproblem.SuchmaximumbufferpoliciesallowABR
| that jointly | takes | proper | bitrate        | and | controls          | the | maximum |            |         |     |         |        |             |     |          |
| ------------ | ----- | ------ | -------------- | --- | ----------------- | --- | ------- | ---------- | ------- | --- | ------- | ------ | ----------- | --- | -------- |
|              |       |        |                |     |                   |     |         | algorithms | to wait | for | a while | before | downloading |     | the next |
| buffer. To   | deal  | with   | the challenges |     | of learning-based |     | buffer- |            |         |     |         |        |             |     |          |
awareABRcomposition,suchasinfinitepossibleplans,multiple chunk, which can not only diminish the buffer overflow effect
bitrate levels, and complex action space, we design adequate but also avoid unnecessary data wastage (§III-A).
preference-driveninputs,separateactionoutputs,andinventhigh
|                   |            |               |                |         |         |         |            | Following    | the     | aforementioned |     | mechanism,                 |     | we           | model the |
| ----------------- | ---------- | ------------- | -------------- | ------- | ------- | ------- | ---------- | ------------ | ------- | -------------- | --- | -------------------------- | --- | ------------ | --------- |
| sample-efficiency |            | training      | methodologies. |         | We      | train   | DeepBuffer |              |         |                |     |                            |     |              |           |
|                   |            |               |                |         |         |         |            | buffer-aware | rate    | adaptation     | as  | a multi-objective          |     | optimization |           |
| with a broad      | set        | of real-world |                | network | traces  | and     | provide    | a            |         |                |     |                            |     |              |           |
|                   |            |               |                |         |         |         |            | problem.     | Then we | convert        | it  | to the single-optimization |     |              | using     |
| comprehensive     | evaluation |               | in terms       | of      | various | network | scenarios  |              |         |                |     |                            |     |              |           |
and different video types. Experimental results indicate that simple additive weighting (SAW) [17]. We propose Deep-
DeepBufferrivalsoroutperformsrecentheuristicsandlearning- Buffer, a novel buffer-aware learning-based ABR algorithm.
| based ABR   | schemes            | in          | terms | of QoE | while heavily  | reducing    |            | the          |               |          |          |          |            |               |           |
| ----------- | ------------------ | ----------- | ----- | ------ | -------------- | ----------- | ---------- | ------------ | ------------- | -------- | -------- | -------- | ---------- | ------------- | --------- |
|             |                    |             |       |        |                |             |            | DeepBuffer   | trains        | a neural | network  |          | (NN) model | via           | state-of- |
| average     | buffer consumption |             | by    | up to  | 90%. Extensive |             | real-world |              |               |          |          |          |            |               |           |
|             |                    |             |       |        |                |             |            | the-art deep | reinforcement |          | learning | (DRL)    | and        | synchronously |           |
| experiments | further            | demonstrate |       | the    | substantial    | superiority |            | of           |               |          |          |          |            |               |           |
|             |                    |             |       |        |                |             |            | controls     | the maximum   |          | buffer   | and next | chunks’    | bitrate       | (§IV).    |
DeepBuffer.
TomakeDeepBufferpractical,wemakeseveralcontributions,
|     |     | I.  | INTRODUCTION |     |     |     |     |           |      |         |          |         |     |          |         |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --------- | ---- | ------- | -------- | ------- | --- | -------- | ------- |
|     |     |     |              |     |     |     |     | including | NN’s | inputs, | actions, | as well | as  | training | method- |
Video has proven itself to be even more significant than ologies. Firstly, beyond ABR’s conventional metrics such as
beforeduetoperiodsofdistancingandlockdownsforCOVID- playbackstaticsandvideoinformation,wefurtherincorporate
19[1].TheGlobalInternetPhenomenaReport2022[2]shows buffer preference, including current maximum buffer size and
that from Jan. 2021 to June. 2021, the bandwidth traffic buffer weight, into the NN’s input. Here the buffer weight ω
was dominated by streaming video, accounting for 53.72% is allowed to be dynamically adjusted w.r.t users’ preference.
of overall traffic, where YouTube [3], Netflix [4], and Face- For example, ω = 0 means the user aims to achieve the
book [5] video stand for the top three. Unsurprisingly, those highest QoE while paying little attention to the data wastage.
three apps leverage adaptive video streaming for providing Secondly, we design DeepBuffer’s policy network with two
video services to the users, aiming to gain higher quality of outputs to decide bitrate action and max buffer action sepa-
experiences (QoE). rately. Such settings can effectively reduce the action space
Client-based Adaptive bitrate (ABR) (or rate adaptation) for bootstrapping training. Thirdly, considering the diversity
schemes and techniques have been proposed to vary network of video bitrate ladders, we propose a novel bitrate selection
conditions via picking the chunks with different bitrates [6]. policy that can support the videos in the different number
Specifically, recent ABR approaches are motivated by pre- of bitrate levels with various encoded bitrate settings. In
dicting throughput [7], adjusting buffer occupancy [8], [9], detail, we apply a gradient-based action mask behind the
or predefined model-free [10], [11] and model-based [12], final output of the NN’s bitrate selection layer, aiming to
[13], [14] ABR models. Each method, ideally, has its own filter invalid actions that do not exist in the current bitrate
advantages,suchashighQoEperformances[10],stablebuffer ladder (§IV-C). Finally, to train DeepBuffer, we implement a
control abilities [15], robust policies to avoid stall events [9], novel sample-efficiency DRL method called Dual-Clip Phasic
and varying diverse QoE requirements [16]. Policy Gradient (DCPPG). It combines several state-of-the-
Inthispaper,weattempttoask:withthehighercompression art on-policy DRL techniques, such as Dual-clip restriction
efficiency and sufficient bandwidth in the year 2022, what’s algorithm [18] and auxiliary phasic policy method [19].
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore.  Restrictions apply.

| 1.00 | Norway (2016) |         |     |      | HD bitrate             |     |     | 0.96     |     |     |     | 25               |     |                   |     |
| ---- | ------------- | ------- | --- | ---- | ---------------------- | --- | --- | -------- | --- | --- | --- | ---------------- | --- | ----------------- | --- |
|      | Oboe (2018)   | Max.    |     | 50   | with excellent quality |     |     |          |     |     |     |                  |     | Played over 50%   |     |
|      |               | bitrate |     |      |                        |     |     |          |     |     |     | )%( etaR .gvA 20 |     | Completely played |     |
| 0.75 | Ghent (2019)  |         |     | RSNP |                        |     |     |          |     |     |     |                  |     |                   |     |
| FDC  | 5G (2021)     |         |     | 40   |                        |     |     | FDC 0.60 |     |     |     | 15               |     |                   |     |
0.50
10
|      |     |     |     |     |     | H.264 (2003) | VP8 (2008) |      |     |     |      |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------------ | ---------- | ---- | --- | --- | ---- | --- | --- | --- | --- |
| 0.25 |     |     |     | 30  |     | H.265 (2013) | VP9 (2013) | 0.25 |     |     |      | 5   |     |     |     |
|      |     |     |     |     |     | H.266 (2020) | AV1 (2018) |      |     |     | User |     |     |     |     |
| 0.00 |     |     |     |     |     |              |            | 0.00 |     |     |      | 0   |     |     |     |
0.1 1.0 10.0 100.01000.0 0 6 12 18 24 30 36 42 48 4 6 8 10 12 4 6 8 10 12
Throughput (mbps) Bitrate (mbps) Duration (mins) Duration (mins)
(a) Trafficbandwidth (b) Compressionefficiencyon4K (c) CDFofvideoduration (d) Departureratevs.Norm.buffer
|     |     |     |     | )s( ycnapuccO reffuB 50 | Max. bitrate |     |     | 1.0 |     |     |     | )s( ycnapuccO reffuB | Max. bitrate |     |     |
| --- | --- | --- | --- | ----------------------- | ------------ | --- | --- | --- | --- | --- | --- | -------------------- | ------------ | --- | --- |
)%( etaR erutrapeD .uccO reffuB .mroN EoQ dezilamroN 35 Rate-based
| 20  |     |     | 0.5 | 40  |     |     |              | 0.8 |              |     |              |     |     | Buffer-based |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ------------ | --- | --- | ------------ | --- |
|     |     |     |     |     |     |     |              |     | Max. bitrate |     |              |     |     | RMPC         |     |
|     |     |     |     | 30  |     |     |              |     |              |     |              | 25  |     |              |     |
|     |     |     |     |     |     |     | Rate-based   | 0.6 |              |     | Rate-based   |     |     | Pensieve     |     |
| 10  |     |     | 0.4 | 20  |     |     | Buffer-based |     |              |     | Buffer-based |     |     |              |     |
|     |     |     |     |     |     |     |              | 0.4 |              |     |              | 15  |     |              |     |
|     |     |     |     |     |     |     | RobustMPC    |     |              |     | RobustMPC    |     |     |              |     |
|     |     |     |     | 10  |     |     | Pensieve     | 0.2 |              |     | Pensieve     | 5   |     |              |     |
0
|     | 0 25 | 50 75 | 100 0.3 |     | 0   | 5   | 10 15 |     | 5   | 10  |     | 15  | 5   | 10  | 15  |
| --- | ---- | ----- | ------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Playback Progress (%) Average Throughput (mbps) Average Throughput (mbps) Average Throughput (mbps)
(e) Departureratevs.Norm.buffer (f) Throughputvs.buffer (g) Throughputvs.QoE (h) Optimalbuffer
Fig.1. Thisgroupofpicturesshowsthattheincreasedtrafficbandwidthandeverhighercompressionefficiencyresultinthedatawastageeffect.Theeffect
isbecomingincreasinglyurgentinUGC-likeservices,sinceusersoftenstopwatchingvideosunexpectedly,thenvideodataislostinsuchsessions.
We evaluate DeepBuffer with diverse video content and the ABR algorithm based on various deep learning or RL
several real-world traces collected from various network con- methods, the above schemes seldom consider the data waste
ditions, categorized into slow-network, medium-network, and caused by unnecessary buffer accumulation.
fast-network paths (§V). We first compare DeepBuffer in The data-wastage effect has already been found for about
different buffer weights with state-the-art ABR algorithms in- one decade [3], [22], [23]. Especially, Plissonneau et al. [22]
volvingheuristics,learning-basedandwastage-basedschemes. shows that recent ABR policies may lead to a large number
With trace-driven analysis, DeepBuffer shows its outstanding ofwastedbytesifthebandwidthislargeenough.Whileinthe
abilities in balancing QoE and buffer size, not only outper- past ten years, very little work has focused on solving such
forming existing schemes by 1.8%-34.4% in terms of QoE a dilemma. PSWA [24] is a wastage-based ABR algorithm
over slow-network paths but also heavily reducing the buffer for mobile video streaming. It controls the buffer solely
size up to 90% over fast-network paths. Next, DeepBuffer with the offline trained configure map. Different from PSWA,
illustrates its high generalization abilities to varying multiple DeepBuffer uses an NN-based policy to control both bitrates
videos, where the videos have multiple types, pre-chunked and maximum buffer with all considered metrics (§IV).
| with | different  | bitrate | ladders.   | Finally, | we validate | DeepBuffer |          |               |     |     |     |     |     |     |     |
| ---- | ---------- | ------- | ---------- | -------- | ----------- | ---------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|      |            |         |            |          |             |            |          | B. Motivation |     |     |     |     |     |     |     |
| over | real-world | network | scenarios. |          | Extensive   | results    | indicate |               |     |     |     |     |     |     |     |
the superiority of DeepBuffer against existing state-of-the-art We start by investigating how the buffer size influences
approaches. In summary, our contributions are the following: traditional adaptive video streaming over today’s network
Weshowhowthedatawastageproblemaffectstoday’sABR conditions.Figure1(a)showstheexplosivegrowthinnetwork
•
|            |     |         |          |     |                  |     |          | capacities | in  | the | past five | years. As | shown, | almost | 30× |
| ---------- | --- | ------- | -------- | --- | ---------------- | --- | -------- | ---------- | --- | --- | --------- | --------- | ------ | ------ | --- |
| algorithms |     | and how | to solve | it  | via buffer-aware |     | adaptive |            |     |     |           |           |        |        |     |
improvementsintermsoftheaveragebandwidth,rangingfrom
| video | streaming. | Then | we  | address | challenges | to  | make the |     |     |     |     |     |     |     |     |
| ----- | ---------- | ---- | --- | ------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
DRL-based scheme more practical (§II). 1.2Mbps[25]to300Mbps[26].However,Figure1(b)shows
|            |              |               |     |                 |           |     |            | encoding               | bitrate | vs. | PSNR    | (peak signal-to-noise |     | ratio) | plots |
| ---------- | ------------ | ------------- | --- | --------------- | --------- | --- | ---------- | ---------------------- | ------- | --- | ------- | --------------------- | --- | ------ | ----- |
| • We       | meticulously | design        | the | proper          | mechanism |     | and train  |                        |         |     |         |                       |     |        |       |
|            |              |               |     |                 |           |     |            | for severalgenerations |         |     | ofcodec | of twofamilies        |     | –H.26x | stan- |
| DeepBuffer |              | with tailored |     | NN architecture |           | and | methodolo- |                        |         |     |         |                       |     |        |       |
dards[27],[28],[29]andVPxgroups[30],[31],[32].Weuse
gies (§IV).
|      |                 |     |          |            |     |      |         | a music | video | ([33], | §V-A) | with 4K | resolution. | Surprisingly, |     |
| ---- | --------------- | --- | -------- | ---------- | --- | ---- | ------- | ------- | ----- | ------ | ----- | ------- | ----------- | ------------- | --- |
| • We | comprehensively |     | validate | DeepBuffer |     | with | various |         |       |        |       |         |             |               |     |
videos and network settings, demonstrating multidimen- results indicates that the VP8 [30] and VP9 [31] can provide
excellentqualityatHDbitrates(6Mbps),asthelatestadvanced
| sional | benefits | of  | DeepBuffer | in  | terms of | QoE | and buffer |        |      |        |      |           |           |          |      |
| ------ | -------- | --- | ---------- | --- | -------- | --- | ---------- | ------ | ---- | ------ | ---- | --------- | --------- | -------- | ---- |
|        |          |     |            |     |          |     |            | codecs | such | as AV1 | [32] | and H.266 | [29] even | performs | well |
size (§V).
|     |     |     |     |     |     |     |     | at SD          | bitrates | (1.1Mbps)   |     | [34]. Thus,        | following | the       | growth |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ----------- | --- | ------------------ | --------- | --------- | ------ |
|     |     |     |     |     |     |     |     | of compression |          | efficiency, |     | before ultra-video |           | streaming | like   |
II. BACKGROUNDANDMOTIVATION
|            |     |      |     |     |     |     |     | point-cloud |     | and cloud-gaming |     | becomes | mainstream, |     | conven- |
| ---------- | --- | ---- | --- | --- | --- | --- | --- | ----------- | --- | ---------------- | --- | ------- | ----------- | --- | ------- |
| A. Related |     | Work |     |     |     |     |     |             |     |                  |     |         |             |     |         |
tionaladaptivevideostreamingdoesn’trequirerateadaptation
The history of ABR starts with heuristic methods. FES- logic over such increased traffic bandwidth – we can blindly
TIVE [20] and PANDA [7] make bitrate selection by es- pick the chunk with the highest bitrate throughout the entire
timating future throughput. BBA [8] and BOLA [9] are session, and still, no stall events occur.
proposed to select bitrates w.r.t current buffer sizes. Then While beyond the sufficient bandwidth and better compres-
model-based approaches like MPC [14] leverage an offline sionefficiency,wefindthatmodernABRsheavilysufferfrom
ABR model for making decisions over a horizon. Altough data wastage problems. Specifically, ABRs often obey the
several attempts [10], [12], [21] have been made to optimize “immediate download principle” that immediately downloads
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore.  Restrictions apply.

4.0
2.0
)spbm(
etartiB
60
40
20
0
0 25 50 75 100 125 150 175
Time (s)
)s(
reffuB
5.0
0.0
DeepBuffer Bandwidth
Pensieve Idle Max buffer
(a) Slow-networkpath.
)spbm(
etartiB
60
40
20
0
0 25 50 75 100 125 150 175
Time (s)
)s(
reffuB
10.0
0.0
DeepBuffer Bandwidth
Pensieve Idle Max buffer
(b) Medium-networkpath.
)spbm(
etartiB
60
40
20
0
0 25 50 75 100 125 150 175
Time (s)
)s(
reffuB
DeepBuffer Bandwidth
Pensieve Idle Max buffer
(c) Fast-networkpath.
Fig.2. DeepBufferisbuffer-awarethatnotonlypicksexcellentchunksforavoidingstallingbutalsofocusesonreducingbufferoccupancyinallconsidered
networkenvironments.NotethedifferentbehaviourofDeepBufferindifferenttypesofnetworkconditions,i.e.,slow,mediumandfast.
the next chunk once the previous chunk has been down- as RobustMPC and Pensieve use complex decision policies
loaded[35].Nevertheless,duetotheoveruseofthebuffer,the according to past throughput, buffer, and chunk size, which
client will not properly play all the video chunks downloaded finally ramps down the optimal value slowly.
if users leave prematurely, and eventually, resulting in the Insummary,duetotherapidincreasesintrafficbandwidth,
data wastage [20], [23]. We report user’s measurement on improvements in video compression efficiency, and diversity
Kuaishou [36], which covers over 100,000 unique videos ofuserbehaviors,it’scriticaltodesignapropermechanismfor
with at least 3-minute duration. We find that almost 96% of avoiding data wastage, especially for videos with a duration
videos have a duration of less than 10 minutes and 60% of of 3 to 10 minutes.
videos perform less than 5 minutes (see in Figure 1(c)), while
video completion rates are decreasing as the video duration
III. METHODS
increases (Figure 1(d)), from 12% for 3-minute videos to 5% A. Joint buffer control and rate adaptation
for 12-minute videos. In other words, more than 92% of the
To tackle the observation above, an intuitive idea of avoid-
users have never watched the end of the video. What’s worse,
ing data wastage is to separate the rate adaptation scheme
more than 85% of the viewers have only watched less than
and the download scheduling scheme, just like PANDA [7].
half of the videos. Meanwhile, at the chunk level, Figure 1(e)
Nevertheless, in the previous section (§II-B) we have shown
shows that users will leave at any chunk and it’s not related
that each ABR algorithm has its own optimal scheduling
to the buffer occupancy.
policy. In this work, we propose the concept of buffer-aware
Further, we conduct several experiments to verify the re- adaptive video streaming. Different from recent buffer-based
lationship between Quality of Experience (QoE, typically approaches [8], buffer-aware ABR joints scheduling and rate
QoE lin [14]) and buffer occupancy of four popular ABRs adaptation scheme in one step. We schedule the next chunk’s
over the network with an average bandwidth of 1-15Mbps. download time by controlling the maximum buffer size.
We use an HD video encoded by the maximum bitrate of Figure 2 demonstrates the design principle of buffer-aware
4.3 Mbps [37]. Figure 1(f) shows the average buffer size of adaptive video streaming, which is absolutely different from
each ABR algorithm starts to increase once the bandwidth previous work. In the slow-network path (Figure 2(a)), we do
is larger than the maximum encoded bitrate of the video. nothavetoadjustthemaximumbuffer,astheABRpolicycan
However, the increased buffer size doesn’t actually improve naturallypreserveitsbuffersizewhileprovidinghighQoE.In
QoE. Figure 1(g) shows that most ABR algorithms have the medium-network path (Figure 2(b)), we partially control
achievedtheiroptimalQoEvaluewhenthebandwidthreaches the maximum buffer and keep the current buffer within a
over 1.5× of the highest video bitrate. Hence, the client’s properrangetoavoidunnecessarydatawastageduringtheses-
bufferwillbewastedifthebandwidthissufficientforpicking sion. Such scenario enables the algorithm to make quantizing
the highest bitrates, leading to unnecessary data costs. and scheduling decisions just like PANDA [7]. Alternatively,
To better understand how much buffer ABR algorithms since the bandwidth is quite sufficient in the fast-network
waste in the video on demand (VOD) streaming, we measure path (Figure 2(c)), the maximum buffer controller dominates
the optimal buffer for each ABR scheme over different band- theprocessthatentirelysetsthebufferastheminimumbuffer
widths and report the results curve in Figure 1(h), where the size. Most of the time, the download module is worked in
optimal buffer is the offline minimum buffer for keeping the idle states, receiving intermittent bandwidth information for
optimal QoE score for each chunk. As expected, each algo- estimation. To that end, both ABR policy and buffer control
rithm shows a different optimal buffer under each bandwidth. algorithm is non-trivial for buffer-aware ABR algorithm.
The key reason is the value of the optimal buffer heavily
B. Buffer-aware rate adaptation model
depends on the strategy of ABR algorithms. For example,
heuristics such as rate-based and buffer-based approaches We formally model the buffer-aware ABR. In the typical
eitherneglectoronlyconsiderbufferoccupancy,whichresults ABRvideostreaming,thevideosarepre-chunkedintoaseries
in a relatively stable trend in the choice of the optimal buffer. ofchunks,eachofwhichissegmentedasthesamevideotime
By contrast, model-based and learning-based approaches such of L seconds. Assuming that there are M bitrate levels for a
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore. Restrictions apply.

video with the bitrates of R={R 1 ,R 2 ,...,R M }. Let B t be (cid:608)(cid:3)Set max buffer
Download
the buffer occupancy at the start of downloading chunk t, R
t
represent the selected video bitrate, C as average throughput 0 Max Buffer
t Playback Buffer DeepBuffer
measured, d (·) is the video chunk size for bitrate R .
t t Server
Now,consideringthemaximumbuffersizeB t maxasanother Throughput
policy that can be adjusted for chunk t, we extend the
Chunk Info
traditional process as buffer-aware adaptive video streaming.
The buffer occupancy of the next chunk B can be con- (cid:609) Request next chunk’s bitrate
t+1
cluded as Eq. 1. When the current buffer size has reached Fig. 3. A high-level perspective of DeepBuffer. Different conventional ABR
or “overflowed” Bmax, the player will wait for the buffer to algorithms,buffer-awareABRsbothselectproperbitrateandmanagebuffer.
t
drain to a certain level which the next chunk t+1 could be
Taking the objective function as a reward signal, we
downloaded.
can leverage the state-of-the-art deep reinforcement learn-
(cid:18) (cid:19)
B =min( B − d t (R t ) +L,Bmax). (1) ing(DRL)methodtogenerateABRalgorithmssincetheprob-
t+1 t C t + t lem naturally falls into the scope of DRL. However, directly
By using this mechanism, the video player can “postpone” using the DRL method to solve the problem is impractical.
forawhiletodownloadchunksand,inturn,activelypickthem We have to face several key challenges:
atanytimeinthefuture.Suchoperationsenabletheplayersto ▷ “Infinite” possible objectives. Single-objective optimiza-
maintainthecurrentbufferleveltoavoidunnecessaryplayback tion only provides a single execution plan instead of all
buffer wastage. Further, we formulate the buffer-aware ABR possible Pareto-optimal plans that exhibit the tradeoffs be-
problem as a multi-objective optimization problem, i.e., the tween the different plans. While in our buffer-aware ABR
combination of QoE maximization and buffer minimization setting,thereareinfinitepossiblesetsofplans,whichbecome
problem, listed in Eq. 2, where δu represents the additional intractable. Thus, how to efficiently obtain all the solutions
t
waiting time caused by Round-Trip-Time (RTT), render time, without exploring the whole objective space?
and especially, the maximum buffer threshold. ▷ Varying multiple videos. The buffer control strategy is
highly influenced by the ratio between maximum bitrate and
max (cid:88) QoEN, min (cid:88) B (2) current throughput measured. Unfortunately, recent learning-
R1,...,RN,Ts
t
t Bt max,Ts
t
t based ABR schemes only support one bitrate ladder set-
d (R ) ting [12], [11], or vary all combinations of the ladders that
s.t. u =u + t t +δu , (3)
t+1 t C t only cover the entire DASH video list [10]. Hence, how to
t
1 (cid:90) ut+1−δut help learning-based ABRs tame the videos in such “real” yet
C = C dn, (4)
t u −u −δu n multiple bitrate levels?
t+1 t t ut
(cid:34)(cid:18) (cid:19) (cid:35) ▷Learning policies in complex action spaces.Besides,the
R L
B =min B − t +L−δu ,Bmax , (5) action spaces contain two sub-actions, i.e., bitrate action and
t+1 t C t t
t + maximum buffer action. They perform independently. So how
R t ∈{R 1 ,R 2 ,...,R M }. (6) to let the learned ABR take the two actions effectively?
Puttingthemtogether,wehavetoi)implementsophisticated
Here we consider the buffer-aware ABR composition as
NNarchitectureforfulfillingvariablefeatureinputs,ii)design
the multi-objective optimization problem. In common, multi-
adequate training methodology, and iii) propose a novel DRL
objective optimization problems have no single solutions but
algorithm that can provide greater sample efficiency in com-
a set of so-called Pareto-optimal solutions, which means none
parison to existing algorithms.
of the objective functions can be improved without degrading
some of the other objective values. The set of Pareto-optimal
IV. DEEPBUFFERDESIGN
solutions represents the tradeoffs according to all objective
functions. Solving such multi-objective optimization means To face the challenges above, we present DeepBuffer, a
finding all the possible solutions. novel neural buffer-aware ABR algorithm. The big picture
of DeepBuffer is demonstrated in Figure 3. Upon receiving
C. Challenges for DRL-based approaches
the state representation, DeepBuffer adopts a NN to pick the
We straightforwardly convert multi-objective optimization properbitrate andset the maximum buffer forthe nextchunk.
to single-optimization via the traditional method, namely sim- In this section, we describe DeepBuffer’s NN inputs, outputs,
ple additive weighting (SAW) [17]. The surrogate objective architecture, and training methodology.
function is listed in Eq. 7, in which ω means how much
the function is influenced by the buffer occupancy. Larger ω A. NN overview
indicatesthattheABRpolicypaysmoreattentiontolowerthe State. As shown in Figure 4, for each chunk t, the state input
buffer rather than preserving QoE performance, vice versa. s is defined as: s = {N ,V ,ω}, where N means video
t t t t t
max (cid:88) QoEN −ωB (7) playbackstatics,V t isthevideocontentmetric,andω controls
R1,...,RN,Bt max
t
t t buffer preference metrics.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore. Restrictions apply.

Playback Statics Action the probabilities of bitrate action πa and maximum buffer
Conv-1D Mask θ
Past throughput Conv-1D F F Bitrate action π θ b. The critic network outputs the value of the current
C C Action
Past download time F F C C sta ▷ te A V c θ t v o . rnetwork.TheDeepBuffer’sactornetworkincludes
Buffer occupancy FC C F M Ac a t x io b n uffer bitrate action, max buffer action, and the auxiliary value.
All three actions and value uses a shared network to extract
Conv-1D
Last video quality F Auxiliary features from the given state. In detail, the actor’s shared
FC C Value network adopts three 1D-convolution (Conv-1D) layers with
Video chunk remain FC Actor featurenumber=128,kernelsize=1toextractthefeaturesfrom
Conv-1D throughput, download time, and bitrate levels. The rest of the
Video Info Conv-1D metrics are passed to five fully-connected (FC) layers with
Video bitrate levels FC the same shape of 128 neurons. The resulted features are
FC F concentrated into a shared vector. For outputting the bitrate
Value
Buffer Preference FC C action, we use another FC layer with 128 neurons to down-
Maximum buffer Conv-1D sample the result of the shared network. The result of the
layer then passes to an FC layer with the neuron number of
FC
Buffer weight |A|, which is the maximum dimension of the bitrate action.
FC Critic
No active functions are applied. Here we treat the output
Fig.4. DeepBuffer’sNNarchitecture.Therearetwoactionspacesintheactor as m. Due to the variable video bitrates and video count,
network.Anauxiliaryvalueisgivenforacceleratingthetrainingprocess. we then apply an action mask to filter invalid actions. The
mask can be implicitly estimated from video content features
▷ Video playback statics N . We take four critical metrics V ={v0,...,vi,v|A|}becausewehavealreadysettheinvalid
t t t t t
for describing the video playback status. The metric includes indices to -1 w.r.t the bitrate level. Assuming I(·) as a binary
indicator, a can be sampled from the probability:
past bitrate selected q , current buffer occupancy b . Mean- t
t t
while, it also contains two sequences, i.e., past k chunks’ I(vi >0)emi
a ∼ t . (9)
throughput measured C t = {c t−k+1 ,...,c t } and download i (cid:80) I(vj >0)emj
j∈|A| t
time m = {m ,...,m }. All the metrics have been
t t−k+1 t
Note that the standard backpropagation of the gradient in
normalized within a proper range. We set k=8 [10].
the NN still holds [39]. For representing the maximum buffer
▷ Video information V . DeepBuffer directly takes the
t
action,wetakean|B|-dimvectorwithSoftmaxfunctionafter
average bitrate of each bitrate level as the video information.
another feature down-sampling layer with 128 neurons, in
Different from previous work, we collect numerous “real
which |B| is the count.
videos” as the video set but instantly generate the “fresh
Moreover, we output a single scalar named auxiliary value.
video” with the video generator during training. The videos
The auxiliary value is used purely to train representations for
are chunked as four seconds [10], [38], [12]. Details of the
the policy. It will be optimized by the auxiliary loss during
video generator please check §V-A.
the auxiliary phase.
▷Buffer metric ω. Inpractice,usersandcontentproviders
▷Critic network.Weimplementacriticnetworktooutput
mayhavedifferentrequirementsforbalancingQoEandbuffer.
a value, which learns an estimate of the accumulate re-
Forinstance,someproviderspreferhighQoEserviceswithout
ward(i.e.,totalvalue)andhelpsimprovethetotalperformance
considering the buffer wastage (i.e., ω = 0), while others
of the actor network.
prefer fixing the maximum buffer size into a lower value to
limit the overall bandwidth cost (i.e., ω =1). To express such B. Policy optimization with DCPPG
applicationrequirements,wetakethecurrentmaximumbuffer
We have to construct a more sample-efficient DRL algo-
occupancy Bmax and buffer weight ω into the state.
t rithm to tame the complexity of the buffer-aware ABR task
Actions. With the state s , the agent synchronously takes
t sincethealgorithmcontrolstwoactionswithavariableaction
two actions, i.e., a and b , in which a is the next chunk’s
t t t space and a fixed action space. Inspired by the recent success
selectedvideobitrateandb reflectsthenextchunk’s“relative”
t of auxiliary learning [19], we propose a novel DRL algo-
maximum buffer size (seconds). The maximum buffer size is
rithm, namely Dual-Clip Phasic Policy Gradient (DCPPG).
updated as Eq. 8. We discuss DeepBuffer with different types
The DCPPG’s training process is mainly composed of the
of action spaces in §V-E.
policy phase and the auxiliary phase.
During the policy phase, we separately update the actor
Bmax =Bmax+b ,b∈{−10,−5,0,5,10}(seconds). (8) network and the critic network. In detail, the loss function
t t−1 t
of the DeepBuffer’s actor network is trained by Dual-Clip
Reward. We set Eq. 7 as the DeepBuffer’s reward function.
Proximal Policy Optimization (Dual-PPO) [18], computed as
Note the function is dynamically parameterized by the buffer LPolicy (Eq. 10):
weight during training. Such settings enable agents to better
understand the correlation between the strategy and the re-
LPolicy =Eˆ[I(Aˆ <0)max(LPPO,cAˆ )+I(Aˆ ≥0)LPPO] (10)
quirement. t t t t
Architecture. The DeepBuffer’s NN is composed of an actor Here I(·) is a binary indicator function, LPPO (Eq. 11) can
network θ and a critic network θ . The actor network outputs be viewed as the surrogate loss function of the vanilla PPO,
v
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore. Restrictions apply.

ρ(π ) (Eq. 12) reflects the joint probability ratio of πa and Algorithm 1 DeepBuffer Training Process
θ θ
πb, Aˆ (Eq. 13) is the advantage function that is learned by import random
θ t network_pool = load_trace()
bootstrapping from the current estimate of the value function,
while not converge:
andγ=0.99representsthediscountedfactor.Briefly,theDual- #Phase 1: randomize environments
clip PPO algorithm adopts a double-clip method to restrict #video count
count = random.choice([2, 3, 4, 5, 6])
the step size of the policy iteration and update the NN by
#randomize bitrate ladders: 100-7000kbps
minimizingtheclippedsurrogateobjective.ϵandcarehyper- video = sorted(random.uniform(100, 7000, count))
parameters that control how to clip the gradient. By default, size = video_generator(video) (§V-A)
#randomly pick a network trace
we set ϵ=0.2, c=3 [18].
n_info = random.choice(network_pool)
LPPO =min (cid:104) ρ(π θ )Aˆ t ,clip (cid:0) ρ(π θ ),1±ϵ (cid:1) Aˆ t (cid:105) (11) # ω ra = nd r o a m n i d z o e m. b u u n f i f f e o r rm w ( e 0 i , gh 1 t )
#Phase 2: rollout policy
πa(a |s ) πb(b |s ) #array: state, bitrate, buffer, reward
ρ(π θ )= πa θ (a t |s t ) · πb θ (b t |s t ) (12) S, A, B, R = rollout(video, size, ω, n_info)
θold t t θold t t #Phase 3: training with DCPPG
for _ in range(N ):
policy
Aˆ t =r t +γV θv (s t+1 )−V θv (s t ) (13) π
o
a
ld
, Op π t
o
b
l
i
d
mi = ze pr θ e , di θ c v t( a S c ) cording to Lπ(Eq.14)
θ v M ar o e re u o p v d e a r t , e t d he b p y a m ra i m ni e m te i r z s in o g ft t h h e e D er e r e o p r B o u f ff A e ˆ r t ’ . scriticnetwork λ fo + r = _ T α r ( i a H n in ta r r θ a g , n et g θ − e v ( H N u θ a s ( u i s x t n ) ) g ) : # Lj U oi p n d t a ( t E e q. e 1 n 5 t ) r , op π y o a ld w , ei a g n h d t π o b ld .
(cid:104) (cid:105)
∇Lπ =−∇ LPolicy(πa,πb,Aˆ )+λH (s ) +∇ [A ]2. (14)
θ θ θ t θ t θv t
pick a trace from the network dataset. Finally, we randomize
We summarize the loss function Lπ in Eq. 14. In addition,
the weight ω to demonstrate the buffer requirement.
we add the entropy of all the policies H (s ) into the loss
θ t Phase 2: rollout policy. In this phase, we encapsulate the
function to encourage exploration feedback, where λ is the
buffer-aware ABR-process into a gym-like [41] environment,
entropy weight. Considering that on-policy RL is sensitive to
which allows the agent to learn the policy effectively.
the entropy weight [38], we adjust the entropy weight λ to
Phase 3: training with DCPPG. The actor network and
minimize the gap between the current entropy and the target
the critic network are repeatedly and iteratively optimized by
entropy H . Here, we set H =0.1 [40].
target target different objective functions in the policy phase and auxiliary
During the auxiliary phase, we further optimize the actor
networkaccordingtothejointobjectivefunctionLjointwhich phase.Herenotethattheoldpoliciesofbitrateπ
o
a
ld
andbuffer
includes behavioral cloning loss and an arbitrary auxiliary πb should be estimated again just before the auxiliary phase
old
value loss: starts. Now we briefly introduce the role of each hyperparam-
Ljoint =Eˆ (cid:104) KL (cid:0) πa (s ),πa(s ) (cid:1) +KL (cid:16) πb (s ),πb(s ) (cid:17)(cid:105) eter. N policy is the number of policy updates performed in
t θold t θ t θold t θ t each policy phase. N controls the sample reuse during the
(cid:20) (cid:21) aux
+Eˆ t 2 1 [V targ (s t )−V θ (s t )]2 . t a h u e xi o li r a ig ry in p a h l a P s P e. G W p e ap s e e r t N [1 p 9 o ] l . icy =5, N aux =6 with consistent of
(15)
Here KL(·) is the behavioral cloning loss, representing
the KL-divergence between the original policy (i.e., πa , V. EVALUATION
θold
πb ) and the updated policy (i.e., πa, πb). Please note that
θold θ θ A. Methodology
the original policy here is the policy after the ending of the
previous policy phase and just right before the beginning of ExperimentalSetup.Weemploytrace-drivensimulationwith
auxiliary phase. The rest part of Eq. 15 is an auxiliary value virtual player [42] and real-world evaluation (§V-F). We
functionthatminimizesthegapbetweentargetvalueV (s ) modifytheplayertoenablemaximumbufferadjustment.Each
targ t
and the auxiliary value V (s ), in which the target value is experiment runs for all segments in the video emulated over
θ t
estimated by the combination of reward for the current state network traces.
s t and the value of the critic network for the next state s t+1 : Video generator. We propose a video generator that enables
V (s )=r +γV (s ). diversevideoswithdifferentencodingbitratesduringtraining.
targ t t θv t+1
Specifically, we select 86 videos from YouTube, which in-
C. Training methodology
volvesmovies,sports,games,news,andMVs,andencodethe
Alg. 1 presents the main phases for training DeepBuffer. video by H.264 codec according to the nine fixed bitrates and
Phase 1: randomizing environments. The first phase segmentitinto4-secondchunks.Duringtraining,werandomly
proposes a randomized environment generator that fully con- initialize a bitrate ladder with the bitrate range from 100 to
siders the diversity requirements in terms of video bitrates, 7000 kbps in 2-6 levels. Then the video size can be estimated
network information, buffer weights, etc. Specifically, we first by the piece-wise linear-regression method – It’s simple yet
randomlyinitializethe“freshvideos”withthevideogenerator, effective,astheproposedgeneratorperformsatleast15,000×
as each video contains 2-6 bitrate levels. Next, we uniformly acceleration with an accuracy of 98.83%.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore. Restrictions apply.

|     |     |     | )spbm( etartiB 1.2 |     |     |     | )spbm( etartiB 1.2 |     |     |     | 1.00 |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | ------------------ | --- | --- | --- | ---- | --- | --- | --- |
1.00
| EoQ  |     |     |     |     |     |     |     |     |     |     | EoQ 0.75 |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
| 0.75 |     |     | 1.0 |     |     |     | 1.0 |     |     |     |          |     |     |     |
DeepBuffer-0.1 BBA Pensieve DeepBuffer-0.1 BBA Pensieve D e e p B u f f e r - 0 . 1 B B A P e n s ie v e 0.50 DeepBuffer Pensieve-w
0.50 DeepBuffer-0.6 RobustMPC Comyco DeepBuffer-0.6 RobustMPC Comyco D e e p B u f f e r - 0 . 6 Ro b ustMPC C o m y c o
DeepBuffer-0.9 BOLA Fugu 0.8 DeepBuffer-0.9 BOLA Fugu 0.8 DeepBuffer-0.9 BOLA Fugu 0.25 RobustMPC-w PSWA
18 16 14 12 10 8 3.25 3.00 2.75 2.50 2.25 2.00 0.30 0.25 0.20 0.15 0.10 16 14 12 10 8 6
Average Buffer (s) Time Spent on Stall (%) Smoothness (mbps) Average Buffer (s)
(a) Buffervs.QoE (b) Stallvs.Bitrate (c) Smoothnessvs.Bitrate (d) DeepBufferwithdifferentω
Fig.5. ComparingDeepBufferwithrecentABRalgorithmsontheQoE lin overtheHSDPAdataset.Errorbarsshow95%confidenceintervals.
Video Test Sets. We adopt three video sets with different that takes Pensieve as the basic ABR algorithm and uses a
types of bitrate ladders for testing. i) EnvivioDash3 [37]: the learned policy to control the maximum buffer. The policy is
DASH.js[43]referencevideowhichisencodedbysixbitrates trainedviamaximizingEq.7.viii)RobustMPC-ω:aheuristic
intherangeof{0.3,0.75,1.2,1.85,2.85,4.3}Mbps.ii)Tears that considers all the possible bitrate-buffer action pairs and
ofSteel[44]:ashortsciencefictionfilmencodedas{0.35,0.6, maximizesQoEoverahorizonoffuturefivechunkslikeMPC.
1,2,3}Mbps.iii)WADADA[33]:aK-popmusicvideo(MV) This scheme can be regarded as the upper bound of heuris-
proposed by Kep1er. The video is encoded as {0.4, 1, 3, tics to deal with the buffer-aware adaptive video streaming
6}Mbps. All videos are encoded by the H.264 codec [27]. problem. ix) PSWA [24]: a closest scheme compared with
Network Trace Datasets. We use Puffer public dataset [13], DeepBuffer. PSWA is the wastage-based ABR scheme that
which involves over 50,000 network traces, for training. adjusts the buffer via a configured map, in which the map is
Meanwhile, we organize recent public datasets into three pre-trained based on the epsilon-constraint method [48] and
categories for testing: i) slow-network paths (≤6Mbps), in- only takes past throughput as the input.
cluding HSDPA [25] and FCC [45]; ii) medium-network Implementation. DeepBuffer’s training tools are built with
paths (≤100Mbps), containing Oboe [38] and FCC-18 [46]; TensorFlow 2.8.1 [49]. We set |A|=6 (i.e. max. six bitrate
iii) fast-network paths (>100Mbps), 5G [26]. levels), |B|=5, learning rate α = 10−4, and train the model
QoEMetrics.Inthispaper,weemploytwoQoEmetrics.The
|     |     |     |     |     |     |     | with QoE | . Note, | §V-D | shows | QoE | results. |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---- | ----- | --- | -------- | --- | --- |
firstisQoE [14],[38],[10],[13],thevanillalinearmapping lin itu
lin
function:
|     |                 |     |          |          |       |     | B. DeepBuffer |     | vs. existing | ABR | algorithms |     |     |     |
| --- | --------------- | --- | -------- | -------- | ----- | --- | ------------- | --- | ------------ | --- | ---------- | --- | --- | --- |
|     | N               |     | N        | N−1      |       |     |               |     |              |     |            |     |     |     |
|     | (cid:88)        |     | (cid:88) | (cid:88) |       |     |               |     |              |     |            |     |     |     |
| QoE | = q(R )−maxq(R) |     | T        | − |q(R   | )−q(R | )|, |               |     |              |     |            |     |     |     |
lin n n n+1 n Inthispart,weleveragetrace-drivensimulationtocompare
n=1 n=1 n=1 the performance of DeepBuffer against several existing ABR
(16)
where N is the total number of chunks, R means the chunk algorithms over various kinds of network types, including
n
n’s video bitrate, T is the rebuffering time, maxq(R) means slow-network(HSDPA[25]),medium-network(FCC-18[46]),
n
|             |            |             |         |     |                   |     | and fast-network |     | (5G | [26]) | paths. During | the | experiment, | we  |
| ----------- | ---------- | ----------- | ------- | --- | ----------------- | --- | ---------------- | --- | --- | ----- | ------------- | --- | ----------- | --- |
| the maximum | bitrate of | the bitrate | ladder, | q(R | n ) is a function |     |                  |     |     |       |               |     |             |     |
that maps the bitrate R to the quality perceived by the only utilize the same trained model and set ω =0.1,0.6,0.9,
n
|            |            |         |         |                |       |     | i.e., DeepBuffer-ω. |     | Results |     | are tested | over the | Envivio | video |
| ---------- | ---------- | ------- | ------- | -------------- | ----- | --- | ------------------- | --- | ------- | --- | ---------- | -------- | ------- | ----- |
| user. Here | we set q(R | n ) = R | n since | it effectively | helps | us  |                     |     |         |     |            |          |         |       |
analyze several underlying QoS metrics, such as bitrate, stall, setandsummarizedasQoE lin (§V-A).WediscussDeepBuffer
and smoothness. Ideally, we can use any form of perceptual with different ω in §V-C.
Slow-networkpaths.InFigure5(a),DeepBuffer-0.1achieves
| measurement, | such as SSIM | [13] | and | VMAF | [12], [21]. |     |     |     |     |     |     |     |     |     |
| ------------ | ------------ | ---- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The second is QoE , which is calculated by ITU-T the best scheme on the slow-path network condition, with
itu
Rec P.1203 [47]. We select QoE since it’s a parametric the improvements on average QoE of 1.8% (Comyco) -
itu
bitstream-based quality assessment standard. 34.4% (BBA) compared with existing ABRs. Meanwhile, we
ABR Baselines. In this work, we select several repre- find that DeepBuffer-0.6 and DeepBuffer-0.9 not only gain
|             |                |     |      |         |         |      | acceptable | overall | performance |     | but | also reduce | the | average |
| ----------- | -------------- | --- | ---- | ------- | ------- | ---- | ---------- | ------- | ----------- | --- | --- | ----------- | --- | ------- |
| sentational | ABR algorithms |     | from | various | type of | fun- |            |         |             |     |     |             |     |         |
damental principles. For recent heuristics, we select the buffersize.Asshown,DeepBuffer-0.6rivalsBOLAandFugu
following ABR algorithms, marked as blue: i) Buffer- on average QoE but heavily decreases 23.9% on BOLA
based Approach (BBA) [8]: a vanilla buffer-based ap- and 39.6% on Fugu, respectively. Meanwhile, DeepBuffer-0.9
proach; ii) BOLA [9]: the standard ABR scheme which improves 21.8% on QoE compared with BBA, and it reduces
|            |             |     |              |           |      | Ro- | 11.6% on | buffer | size. |     |     |     |     |     |
| ---------- | ----------- | --- | ------------ | --------- | ---- | --- | -------- | ------ | ----- | --- | --- | --- | --- | --- |
| solves the | ABR problem | by  | the Lyapunov | function; | iii) |     |          |        |       |     |     |     |     |     |
bustMPC (RMPC)[14]:amodel-basedmethodbypredicting Moreover, we report the detailed metrics on slow-network
key environment variables over a moving look-ahead horizon. paths in Figure 5(b) and Figure 5(c). The results contain
Learning-based ABR baselines includes (marked as various critical metrics, such as average bitrate, stalling ratio,
gray):iv)Pensieve [10]:thevanillaDRL-basedABRscheme. and average bitrate change (i.e., smoothness). Note the right
Weusethepre-trainedmodel;v)Comyco[12]:aquality-aware top region of the figures is the desired operation region for
imitation learning-based ABR scheme. We retrain it with any scheme. As shown, we claim that DeepBuffer’s superior
QoE ; vi) Fugu [13]: a hybrid ABR algorithm that adopts performance is due to its better understanding of the shape of
lin
deep neural network (DNN) to predict the download time for the Pareto frontier, since DeepBuffer with various ω always
the next chunk and uses vanilla MPC to make decisions. performs in a Pareto optimum state when no bitrate or stall
In addition, we also consider prior wastage-based ABRs changes can make one individual better off without making
as the baselines, including vii) Pensieve-ω: a hybrid scheme at least one other individual worse off. Similarly, DeepBuffer
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore.  Restrictions apply.

|     |     | )spbm( etartiB |     |     | )spbm( etartiB |     |     |     |     |
| --- | --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- |
| 3   |     | 3.0            |     |     | 3.0            |     | 3.0 |     |     |
| EoQ |     |                |     |     |                |     | EoQ |     |     |
| 2   |     |                |     |     |                |     | 2.5 |     |     |
DeepBuffer-0.1 BBA Pensieve 2.5 DeepBuffer-0.1 BBA Pensieve 2.5 DeepBuffer-0.1 BBA Pensieve DeepBuffer Pensieve-w
DeepBuffer-0.6 RobustMPC Comyco DeepBuffer-0.6 RobustMPC Comyco DeepBuffer-0.6 RobustMPC Comyco 2.0
1 DeepBuffer-0.9 BOLA Fugu 2.0 DeepBuffer-0.9 BOLA Fugu 2.0 DeepBuffer-0.9 BOLA Fugu RobustMPC-w PSWA
50 40 30 20 10 1.2 1.0 0.8 0.6 0.25 0.20 0.15 0.10 1.5 25 20 15 10 5
Average Buffer (s) Time Spent on Stall (%) Smoothness (mbps) Average Buffer (s)
(a) Buffervs.QoE (b) Stallvs.Bitrate (c) Smoothnessvs.Bitrate (d) DeepBufferwithdifferentω
Fig.6. ComparingDeepBufferwithrecentABRalgorithmsontheQoE lin .ResultsarecollectedontheFCC-18dataset.
|     |     | )spbm( etartiB 4.0 |     |     | )spbm( etartiB 4.0 |     | 4.5 |     |     |
| --- | --- | ------------------ | --- | --- | ------------------ | --- | --- | --- | --- |
4
| EoQ |     |     |     |     |     |     | EoQ 4.0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
| 3   |     | 3.5 |     |     | 3.5 |     |         |     |     |
DeepBuffer-0.1 BBA Pensieve DeepBuffer-0.1 BBA Pensieve DeepBuffer-0.1 BBA Pensieve 3.5 DeepBuffer Pensieve-w
2 DeepBuffer-0.6 RobustMPC Comyco 3.0 DeepBuffer-0.6 RobustMPC Comyco 3.0 DeepBuffer-0.6 RobustMPC Comyco
DeepBuffer-0.9 BOLA Fugu DeepBuffer-0.9 BOLA Fugu DeepBuffer-0.9 BOLA Fugu 3.0 RobustMPC-w PSWA
50 40 30 20 10 0.30 0.25 0.20 0.15 0.10 0.05 0.25 0.20 0.15 0.10 40 30 20 10
Average Buffer (s) Time Spent on Stall (%) Smoothness (mbps) Average Buffer (s)
(a) Buffervs.QoE (b) Stallvs.Bitrate (c) Smoothnessvs.Bitrate (d) DeepBufferwithdifferentω
Fig.7. ComparingDeepBufferwithrecentABRalgorithmsontheQoE lin .ResultsarecollectedontheLumos-5Gdataset.
also maintains its competitiveness in terms of the smoothness In turn, we see that Pensieve-ω fails to handle such diverse
metric, which stands for the Top-2 scheme when ω=0.1. requirements on the buffer weight. That’s because Pensieve-
Medium-network paths. We analyze the behavior of Deep- ω only adjusts the maximum buffer action solely, and it
Buffer and baselines over the FCC-18 network dataset. The doesn’t jointly consider the comprehensive effect brought by
dataset contains various network conditions, which can be buffer and bitrate action. Same observation can be resulted in
viewed as nowadays’ network. From Figure 6(a), we ob- medium-path(Figure6(d)andfast-networkpaths(Figure7(d))
serve that existing learning-based approaches suffer from data as well. Furthermore, RobustMPC-ω does consider both bi-
wastage,whichoftenleveragesanadditional1.5×(Pensieve), trate selection and buffer adjustment. It behaves better than
1.7× (Fugu), and 2.8× (Comyco) on buffer size compared Pensieve-ω inslowand medium-networkpaths,butits perfor-
with DeepBuffer for achieving similar results on QoE. By mance degrades heavily when the throughput predictions are
contrast, comparing DeepBuffer with recent heuristics such incorrect in fast-path network scenario (Figure 7(d), [50]). In
asBBAandBOLA,wecanseethatDeepBuffer-0.1improves particular,comparingDeepBufferwithPSWA,weobservethat
the average QoE by 13.6% on BOLA and 22.7% on BBA DeepBuffer can generalize to different network environments,
with almost the same average buffer occupancy. The only with the improvements on average QoE values within 17.4%-
exception is RobustMPC: it performs almost equal to Deep- 31.3%onslow-networkpaths,6.5%-7.0%onmedium-network
Buffer,obtainingtheTop-3schemeinmedium-networkpaths. paths, and 5.1% on fast-network paths respectively. In the
Meanwhile, through analyzing the detailed results plotted in meantime,comparedwithPSWA,DeepBufferstartssavingthe
buffersizewhenω=0.4ontheslow-networkpaths.Wereason
| Figure 6(b) | and Figure 6(c), | we find | that DeepBuffer | with all |     |     |     |     |     |
| ----------- | ---------------- | ------- | --------------- | -------- | --- | --- | --- | --- | --- |
considered weights can reach higher bitrate but fewer bitrate that PSWA controls the maximum buffer by only considering
changescomparedtobaselines,whiletheyworkslightlyworse averagethroughput,whichnotonlylacksthefeatureselection
in terms of stalling ratio, with the relative degradation of but also neglects the influence on bitrate actions.
| 0.07% (ω=0.1)-0.2% | (ω=0.9) | compared | with Comyco. |     |     |     |     |     |     |
| ------------------ | ------- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
Fast-networkpaths.Figure7showstheresultsfromperform- D. DeepBuffer with different bitrate ladders
ing ABR algorithms on the 5G dataset. Here we illustrate the To validate the generalization of DeepBuffer, we conduct
huge data waste of prior work in Figure 7(a). We reason that an experiment to test ABR schemes with two kinds of videos
|                |         |               |           |               | encoded | by various bitrate | ladder settings | and report | the |
| -------------- | ------- | ------------- | --------- | ------------- | ------- | ------------------ | --------------- | ---------- | --- |
| in the current | network | scenario, the | bandwidth | is sufficient |         |                    |                 |            |     |
for ABRs to pick chunks with the highest bitrate, while main results in Table I. The selected video sets are Tears
such schemes lack buffer control strategies like DeepBuffer, of Steel (ToS) [44], a short movie, and WA DA DA [33],
immediately downloading the chunk once the previous down- a music video. We take DeepBuffer with ω=0, 0.5, and 0.7
load process ends. In contrast, DeepBuffer picks the proper for comparison. We don’t compare Comyco and Pensieve in
|              |            |                |           |            | this part | since they are | not naturally designed | to vary | such |
| ------------ | ---------- | -------------- | --------- | ---------- | --------- | -------------- | ---------------------- | ------- | ---- |
| bitrate with | preserving | current buffer | occupancy | via buffer |           |                |                        |         |      |
action (§IV-A), significantly reducing the average buffer size multiple videos. Different from the previous experiment, we
by 90.7% – an impressive number. adoptO.46score[47],whichisthemediasessionqualityscore
|               |                   |         |     |     | in QoE itu    | [51], to evaluate | QoE. Previous | work demonstrates  |     |
| ------------- | ----------------- | ------- | --- | --- | ------------- | ----------------- | ------------- | ------------------ | --- |
| C. DeepBuffer | vs. wastage-based | schemes |     |     |               |                   |               |                    |     |
|               |                   |         |     |     | that compared | with QoE          | , QoE         | can better reflect | the |
lin itu
We vary a set of buffer weights ω, sweeping from 0 to 1, subjective quality evaluation of ABR.
to investigate the impact that each has on QoE and buffer As expected, DeepBuffer maintains good QoE on two
|     |     |     |     | lin |     |     |     | itu |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
size. The wastage-based ABR algorithm includes Pensieve- different kinds of videos. Among them, DeepBuffer-0, the
ω, RobustMPC-ω, and PSWA. Results show DeepBuffer’s scheme without considering the buffer sizes, ranks first in
outstanding generalization ability. Figure 5(d) indicates that three network-video pairs, as it performs only 0.5% less
DeepBufferoutperformsotherschemesonslow-networkpaths than the best scheme on average QoE in the ToS-Oboe
itu
since it reaches the highest QoE with the same buffer size. scenario. Meanwhile, DeepBuffer-0.5 can balance the QoE itu
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore.  Restrictions apply.

TABLEI
ResultsofDeepBufferwithdifferentvideosonFCCandOboedataset.QoEmetricsarecomputedasQoEitu [47].
1st FCC[45] Oboe[38] FCC[45] Oboe[38]
2nd QoEitu (↑) Buffer(s)(↓) QoEitu (↑) Buffer(s)(↓) QoEitu (↑) Buffer(s)(↓) QoEitu (↑) Buffer(s)(↓)
BOLA 2.62±0.78 21.73±10.31 3.53±0.76 38.23±17.82 3.14±0.67 18.83±5.07 3.82±0.69 23.65±5.59
RMPC 2.84±0.61 18.32±10.93 3.68±0.71 33.56±19.79 3.31±0.57 23.04±9.72 3.93±0.62 21.98±8.83
Fugu 2.88±0.63 17.46±12.41 3.68±0.70 34.11±20.86 WA 3.25±0.58 25.33±14.18 3.89±0.63 24.79±10.68
ToS PSWA 2.64±0.48 10.89±3.40 3.40±0.71 10.30±4.02 DA 3.10±0.49 14.12±4.62 3.67±0.63 11.75±4.38
[44] DB-0 2.89±0.58 22.83±5.92 3.66±0.68 25.75±7.50 DA 3.33±0.61 28.09±6.37 3.94±0.60 25.96±7.38
DB-0.5 2.78±0.65 9.84±4.81 3.57±0.82 13.18±5.49 [33] 3.32±0.64 16.10±3.38 3.94±0.64 16.07±3.82
DB-0.7 2.78±0.51 6.73±3.73 3.44±0.79 8.95±4.27 3.11±0.64 9.10±4.69 3.80±0.73 11.73±5.05
1.00
0.75
0.50
0.25
0.00
0 25 50 75 100 125 150 175 200
Epochs
EoQ
.mroN
1.00
0.75 DCPPG
Dual-PPO 0.50
PPO 0.25
A2C
0.00
0 50 100 150 200 250 300 350 400
Epochs
(a) “Sweeping”on-policyRLs
EoQ
.mroN
1.0
DeepBuffer 0.8
Split actor network
Continuous buffer 0.6
0.4
0.2
(b) Actionspacedesign
0.0
Fig.8. ComparingDeepBufferwithothersettings. QoE Buffer QoE Buffer QoE Buffer
performanceandbufferoccupancyoverallconsideredscenar-
ios. Especially compared with traditional ABR algorithms, it
achieves the best QoE value while saving at least 36.7% itu
on buffer size in the WA DA DA-Oboe scenario. Moreover,
DeepBuffer-0.7 surpasses PSWA over all scenarios, with the
improvements on average QoE up to 5%, as well as the
itu
significant decrease in average buffer occupancy up to 61.8%.
E. Ablation studies
Different RL methods. We compare DCPPG (§IV-B) with
on-policy methods over a basic environment to prove its
sample efficiency. Applying such a “complex” DRL method
is not gilding the lily since Figure 8(a) shows the rapid learn-
ing efficiency of DCPPG. Technically, DCPPG rivals Dual-
PPO [18], and it improves the normalized QoE by 5.46%-
17.81% compared with PPO [52] and A2C [53].
Design of action space. Moreover, we compare different
designs of the action space, such as combined bitrate and
buffer space (i.e., |A|×|B|), and continuous buffer actions.
Figure 8(b) indicates that DeepBuffer with separated discrete
action space gains the best performance on normalized QoE.
F. Real-world experiment
Finally, we conducted an experiment to validate how Deep-
Buffer performs in the wild. Specifically, we custom a new
ABR rule on Dash.js [43] and play the video on Chrome
V100. Note the client’s buffer size can be easily adjusted by
Dash.js API. The considered network scenarios cover 4G sce-
narioscollectedinBeijingSubway,publicWiFiscenarios,and
5G scenarios. Figure 9 reports the average QoE value and
lin
buffersizeforeachschemeoverdifferentnetworkconditions.
Error bars span one standard deviation from the average. We
reveal that DeepBuffer-0.1 outperforms existing schemes in
terms of normalized QoE over all scenarios. In particular,
DeepBuffer-0.1 improves QoE by 4.7%-55.5% in comparison
to PSWA, RobustMPC, and Pensieve over metro networks.
Meanwhile,italsoreachessmallbuffersizes,savingupto9×
eulaV
dezilamroN
PSWA RobustMPC Pensieve DeepBuffer-0.1
Public WiFi Metro (4G) 5G
Fig.9. ComparingDeepBufferwithrecentABRsinthereal-world.
TABLEII
DeepBuffermeetscongestioncontrolalgorithms
CCAs Metric Reno[55] Cubic[56] BBR[57]
DeepBuffer-0.1 nQoE/Buffer 0.52/0.15 0.57/0.10 0.81/0.08
in terms of average buffer. Moreover, Table II demystifies the
influenceofleveragingdifferentkindsofcongestioncontrolal-
gorithms(CCA)onDeepBuffer.Resultsaresummarizedasthe
normalized QoE (nQoE) and buffer size. As shown, AIMD-
based schemes such as Reno and Cubic suffer from slow start
effects, leading to a low estimated bandwidth. In contrast,
pacing-based schemes like BBR performs much better than
AIMD-basedones.Thus,wearguethatavailablethroughputis
notindependentofABRalgorithms.Itcanbefurtherestimated
by other critical features such as downloading chunks and
CCAs[54].Wewilldiscussthisinterestingtopicinthefuture.
VI. CONCLUSION
In this paper, we considered leveraging buffer-aware adap-
tive video streaming to overcome the increased data-wastage
problem caused by sufficient bandwidth resources and limited
bitrate improvements on videos. Modeling the task as multi-
objectiveoptimization,weproposedDeepBuffer,aDRL-based
buffer-aware ABR scheme that considers varying multiple
bitrateladders,WehaveconstructedDeepBuffer’strainingsys-
tem, including its NN architectures and methodologies. Using
a comprehensive trace-driven comparison of prior work and
real-world deployment, we have illustrated that DeepBuffer
can preserve the performance while reducing the buffer size
by up to 90%, significantly restraining the data waste.
AcknowledgementWethankNuowenKanforhisfruitfuldis-
cussions and valuable feedback. This work was supported by
NSFC under Grant 61936011, Beijing Key Lab of Networked
Multimedia, and the Kuaishou-Tsinghua Joint Project.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore. Restrictions apply.

REFERENCES [29] B. Bross, Y.-K. Wang, Y. Ye, S. Liu, J. Chen, G. J. Sullivan, and J.-
R. Ohm, “Overview of the versatile video coding (vvc) standard and
[1] Sandvine,“2020covid-19phenomenaspotlightreport,”2020.[Online]. itsapplications,”IEEETransactionsonCircuitsandSystemsforVideo
Available:https://www.sandvine.com/phenomena Technology,vol.31,no.10,pp.3736–3764,2021.
[2] ——, “The global internet phenomena report january 2022,” 2022. [30] J.Bankoski,P.Wilkins,andY.Xu,“Technicaloverviewofvp8,anopen
[Online].Available:https://www.sandvine.com/phenomena sourcevideocodecfortheweb,”in2011IEEEInternationalConference
[3] A.Mondal,S.Sengupta,B.R.Reddy,M.Koundinya,C.Govindarajan, onMultimediaandExpo. IEEE,2011,pp.1–6.
P.De,N.Ganguly,andS.Chakraborty,“Candidwithyoutube:Adaptive [31] D.Mukherjee,J.Bankoski,A.Grange,J.Han,J.Koleszar,P.Wilkins,
streamingbehaviorandimplicationsondataconsumption,”inProceed- Y. Xu, and R. Bultje, “The latest open-source video codec vp9-an
ingsofthe27thWorkshoponNetworkandOperatingSystemsSupport overview andpreliminary results,” in2013 PictureCoding Symposium
forDigitalAudioandVideo,2017,pp.19–24. (PCS). IEEE,2013,pp.390–393.
[4] T.-Y. Huang, C. Ekanadham, A. J. Berglund, and Z. Li, “Hindsight: [32] Y. Chen, D. Murherjee, J. Han, A. Grange, Y. Xu, Z. Liu, S. Parker,
Evaluate video bitrate adaptation at scale,” in Proceedings of the 10th C.Chen,H.Su,U.Joshietal.,“Anoverviewofcorecodingtoolsinthe
ACMMultimediaSystemsConference,2019,pp.86–97. av1 video codec,” in 2018 Picture Coding Symposium (PCS). IEEE,
[5] H.Mao,S.Chen,D.Dimmery,S.Singh,D.Blaisdell,Y.Tian,M.Al- 2018,pp.41–45.
izadeh,andE.Bakshy,“Real-worldvideoadaptationwithreinforcement [33] Kep1er,“Wadada,”https://www.youtube.com/watch?v=n0j5NPptyM0,
learning,”arXivpreprintarXiv:2008.12858,2020. 2022.
[6] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann, [34] A.Francis,“4kvideoatsdbitrateswithav1,”https://bitmovin.com/av1-
“Asurveyonbitrateadaptationschemesforstreamingmediaoverhttp,” 4k-video-sd-bitrates/,2022.
IEEECommunicationsSurveys&Tutorials,2018. [35] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari,
[7] Z. Li, X. Zhu, J. Gahm, R. Pan, H. Hu, A. C. Begen, and D. Oran, “Confused,timid,andunstable:pickingavideostreamingrateishard,”
“Probe and adapt: Rate adaptation for http video streaming at scale,” inIMC2012,2012,pp.225–238.
IEEEJASC,vol.32,no.4,pp.719–733,2014. [36] K. Technology, “Announcement of the results for the year ended
[8] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,andM.Watson,“A december31,2021,”https://www.kuaishou.com,2022.
buffer-based approach to rate adaptation: Evidence from a large video [37] “Enviviodash3,” https://dash.akamaized.net/envivio/EnvivioDash3/,
streamingservice,”SIGCOMM2014,vol.44,no.4,pp.187–198,2014. 2016.
[9] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “Bola: Near-optimal [38] Z.Akhtar,Y.S.Nam,R.Govindanetal.,“Oboe:auto-tuningvideoabr
bitrate adaptation for online videos,” IEEE/ACM Transactions on Net- algorithmstonetworkconditions,”inSIGCOMM2018,2018.
working,vol.28,no.4,pp.1698–1711,2020. [39] S.HuangandS.Ontan˜o´n,“Acloserlookatinvalidactionmaskingin
[10] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream- policygradientalgorithms,”arXivpreprintarXiv:2006.14171,2020.
ingwithpensieve,”inSIGCOMM2017,2017. [40] J. Li, S. Koyamada, Q. Ye, G. Liu, C. Wang, R. Yang, L. Zhao,
[11] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: T. Qin, T.-Y. Liu, and H.-W. Hon, “Suphx: Mastering mahjong with
A harmonious fusion of buffer-based and learning-based approach for deepreinforcementlearning,”arXivpreprintarXiv:2003.13590,2020.
adaptive streaming,” in IEEE INFOCOM 2020-IEEE Conference on [41] G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schul-
ComputerCommunications. IEEE,2020,pp.1967–1976. man, J. Tang, and W. Zaremba, “Openai gym,” arXiv preprint
[12] T. Huang, C. Zhou, R.-X. Zhang et al., “Comyco: Quality-aware arXiv:1606.01540,2016.
adaptive video streaming via imitation learning,” in ACM Multimedia [42] H.Mao,P.Negi,A.Narayan,H.Wang,J.Yang,H.Wang,R.Marcus,
2019,2019,pp.429–437. R.Addanki,M.Khani,S.Heetal.,“Park:Anopenplatformforlearning
[13] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, P. Levis, augmentedcomputersystems,”inNIPS2019,2019.
and K. Winstein,“Learning in situ: a randomizedexperiment in video [43] DASH,“Dash,”2019.[Online].Available:https://dashif.org/
streaming,” in 17th {USENIX} Symposium on Networked Systems De- [44] O.Movie,“Tearsofsteel,”https://mango.blender.org/,2013.
signandImplementation({NSDI}20),2020,pp.495–511. [45] M. F. B. Report, “Raw data measuring broadband america 2016,”
[14] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic https://www.fcc.gov/,2016,[Online;accessed19-July-2016].
approachfordynamicadaptivevideostreamingoverhttp,”inSIGCOMM [46] Z.Meng,Y.Guo,Y.Shen,J.Chen,C.Zhou,M.Wang,J.Zhang,M.Xu,
2015. ACM,2015,pp.325–338. C.Sun,andH.Hu,“Practicallydeployingheavyweightadaptivebitrate
[15] P. K. Yadav, A. Shafiei, and W. T. Ooi, “Quetra: A queuing theory algorithms with teacher-student learning,” IEEE/ACM Transactions on
approach to dash rate adaptation,” in Proceedings of the 25th ACM Networking,vol.29,no.2,pp.723–736,2021.
internationalconferenceonMultimedia,2017,pp.1130–1138. [47] W.Robitza,S.Go¨ring,A.Raake,D.Lindegren,G.Heikkila¨,J.Gustafs-
[16] T. Huang, R. Zhang, and L. Sun, “Zwei: A self-play reinforcement son, P. List, B. Feiten, U. Wu¨stenhagen, M.-N. Garcia, K. Yamagishi,
learningframeworkforvideotransmissionservices,”IEEETransactions andS.Broom,“HTTPAdaptiveStreamingQoEEstimationwithITU-T
onMultimedia,2021. Rec.P.1203–OpenDatabasesandSoftware,”in9thACMMultimedia
[17] K. Deb, “Multi-objective optimization,” in Search methodologies. SystemsConference,Amsterdam,2018.
Springer,2014,pp.403–449. [48] M. Laumanns, L. Thiele, and E. Zitzler, “An adaptive scheme to
[18] D.Ye,Z.Liu,M.Sun,B.Shi,P.Zhao,H.Wu,H.Yu,S.Yang,X.Wu, generate the pareto front based on the epsilon-constraint method,” in
Q. Guo et al., “Mastering complex control in moba games with deep DagstuhlSeminarProceedings. SchlossDagstuhl-Leibniz-Zentrumfu¨r
reinforcementlearning,”arXivpreprintarXiv:1912.09729,2019. Informatik,2005.
[19] K. Cobbe, J. Hilton, O. Klimov, and J. Schulman, “Phasic policy [49] M.Abadi,P.Barham,J.Chen,Z.Chen,A.Davis,J.Dean,M.Devin,
gradient,”arXivpreprintarXiv:2009.04416,2020. S. Ghemawat, G. Irving, M. Isard et al., “Tensorflow: A system for
[20] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and large-scalemachinelearning.”inOSDI,vol.16,2016,pp.265–283.
stability in http-based adaptive video streaming with festive,” TON, [50] A.Narayanan,X.Zhang,R.Zhu,A.Hassan,S.Jin,X.Zhu,X.Zhang,
vol.22,no.1,pp.326–340,2014. D.Rybkin,Z.Yang,Z.M.Maoetal.,“Avariegatedlookat5ginthe
[21] X.Zuo,Y.Jiayu,M.Wang,andY.Cui,“Adaptivebitratewithuser-level wild:performance,power,andqoeimplications,”inProceedingsofthe
qoe preference for video streaming,” in IEEE INFOCOM 2022-IEEE 2021ACMSIGCOMM2021Conference,2021,pp.610–625.
ConferenceonComputerCommunications. IEEE,2022,pp.1–10. [51] O. ITU, “Series p: Telephone transmission quality, telephone installa-
[22] L. Plissonneau, E. Biersack, and P. Juluri, “Analyzing the impact of tions, local line networks methods for objective and subjective assess-
youtubedeliverypoliciesonuserexperience,”in201224thInternational mentofquality.”
TeletrafficCongress(ITC24). IEEE,2012,pp.1–8. [52] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,“Prox-
[23] A. Finamore, M. Mellia, M. M. Munafo, R. Torres, and S. G. Rao, imalpolicyoptimizationalgorithms,”arXivpreprintarXiv:1707.06347,
“Youtube everywhere: Impact of device and infrastructure synergies 2017.
on user experience,” in Proceedings of the 2011 ACM SIGCOMM [53] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley,
conferenceonInternetmeasurementconference,2011,pp.345–360. D.Silver,andK.Kavukcuoglu,“Asynchronousmethodsfordeeprein-
[24] G.Zhang,K.Liu,H.Hu,V.Aggarwal,andJ.Y.Lee,“Post-streaming forcementlearning,”inInternationalConferenceonMachineLearning,
wastage analysis–a data wastage aware framework in mobile video 2016,pp.1928–1937.
streaming,” IEEE Transactions on Mobile Computing, vol. 22, no. 1, [54] A.Alomar,P.Hamadanian,A.Nasr-Esfahany,A.Agarwal,M.Alizadeh,
pp.389–401,2021. and D. Shah, “Causalsim: Toward a causal data-driven simulator for
[25] H. Riiser, P. Vigmostad, C. Griwodz, and P. Halvorsen, “Commute networkprotocols,”arXivpreprintarXiv:2201.01811,2022.
pathbandwidthtracesfrom3gnetworks:analysisandapplications,”in [55] G.R.WrightandW.R.Stevens,TCP/IPIllustrated,Volume2(paper-
Proceedings of the 4th ACM Multimedia Systems Conference. ACM, back):TheImplementation. Addison-WesleyProfessional,1995.
2013,pp.114–118. [56] S. Ha, I. Rhee, and L. Xu, “Cubic: a new tcp-friendly high-speed tcp
[26] A.Narayanan,E.Ramadan,R.Mehtaetal.,“Lumos5g:Mappingand variant,” ACM SIGOPS operating systems review, vol. 42, no. 5, pp.
predictingcommercialmmwave5gthroughput,”inIMC20,NewYork, 64–74,2008.
NY,USA,2020. [57] N.Cardwell,Y.Cheng,S.H.Yeganeh,I.Swett,V.Vasiliev,P.Jha,Y.Se-
[27] T.Wiegand,G.J.Sullivan,G.Bjontegaard,andA.Luthra,“Overview ung, M. Mathis, and V. Jacobson, “Bbrv2: A model-based congestion
oftheh.264/avcvideocodingstandard,”IEEETransactionsoncircuits control,”inPresentationinICCRGatIETF104thmeeting,2019.
andsystemsforvideotechnology,vol.13,no.7,pp.560–576,2003.
[28] G.J.Sullivan,J.-R.Ohm,W.-J.Han,andT.Wiegand,“Overviewofthe
highefficiencyvideocoding(hevc)standard,”TSCVT,2012.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on June 01,2026 at 10:51:26 UTC from IEEE Xplore. Restrictions apply.