VANDERHOOFTetal.:HTTP/2-BASEDADAPTIVESTREAMINGOFHEVCVIDEOOVER4G/LTENETWORKS 1
HTTP/2-Based Adaptive Streaming of HEVC Video over
4G/LTE Networks
Jeroen van der Hooft, Student Member, IEEE, Stefano Petrangeli, Student Member, IEEE,
Tim Wauters, Member, IEEE, Rafael Huysegems, Patrice Rondao Alface, Senior Member, IEEE,
Tom Bostoen, and Filip De Turck, Senior Member, IEEE
Abstract—In HTTP Adaptive Streaming (HAS), video content Rate adaptation
is temporally divided into multiple segments, each encoded at heuristic
several quality levels. The client can adapt the requested video Request (s,q)
quality to network changes, generally resulting in a smoother Video i j Video
encoding decoding
playback.Unfortunately,livestreamingsolutionsstilloftensuffer Internet
from playout freezes and a large end-to-end delay. By reducing
Video
thesegmentduration,theclientcanuseasmallertemporalbuffer segmentation HAS Server Segment (s,q) HAS Client Buffer
i j
and respond even faster to network changes. However, since
segmentsarerequestedsubsequently,thisapproachissusceptible Figure1. TheconceptofHTTPAdaptiveStreaming.
to high round-trip times. In this letter, we discuss the merits of
an HTTP/2 push-based approach. We present the details of a
conditions. Furthermore, video content is generally encoded
measurement study on the available bandwidth in real 4G/LTE
networks,andanalyzetheinducedbitrateoverheadforHEVC- at variable bit rate, with more bits assigned to scenes with
encodedvideosegmentswithasub-secondduration.Throughan rapid motion. As such, it often takes significantly longer
extensive evaluation with the generated video content, we show to download a segment than initially estimated, increasing
that the proposed approach results in a higher video quality
the chances of buffer starvation. Second, since segments of
(+7.5%) and a lower freeze time (-50.4%), and allows to reduce
multiple seconds are typically used, the end-to-end delay in
the live delay compared to traditional solutions over HTTP/1.1.
current HAS deployments is in the order of tens of seconds.
Index Terms—HTTP Adaptive Streaming, DASH, Quality of
ThisisdetrimentalfortheQoEinlivevideostreaming,where
Experience, HTTP/2, Server Push, 4G/LTE, H.265/HEVC.
the delay should be as low as possible [4].
One solution to these issues is the use of H.265/HEVC, a
video compression standard which was developed to provide
twice the compression efficiency of the previous standard,
I. INTRODUCTION
H.264/AVC [5]. In HEVC, coding units of up to 64x64 pixels
TODAY, more than half of the Internet traffic is generated
are used instead of 16x16, and more intra-picture directions,
by video streaming applications [1]. To meet increasing
finerfractionalmotionvectorsandlargertransformblocksare
requirements,theconceptofHTTPAdaptiveStreaming(HAS)
usedtoachievethisimprovementincompressionperformance.
has recently been introduced. As shown in Figure 1, content
Reducing the encoding bit rate has a significant impact on the
is encoded at different quality levels and temporally divided
QoE, as fewer data needs to be transferred from server to
into segments with a typical length of 2 to 10 seconds. The
client. Another solution is to use segments with a sub-second
client uses a rate adaptation heuristic to decide upon the
duration.Shortersegmentsallowtolimitthemaximumdown-
downloadedqualityforeachsegment,basedoncriteriasuchas
loadtimeofindividualsegmentsandrespondfastertosudden
theperceivedbandwidthandthebufferfilling.Thegoalofthis
changesintheavailablebandwidth.Furthermore,theyallowto
heuristicistooptimizetheuser’sQualityofExperience(QoE),
useasmallerbuffer,whichresultsinapotentialdecreaseofthe
which depends among others on the average video quality,
end-to-end delay in live streaming scenarios. Unfortunately,
the frequency of quality changes and the occurrence of video
sinceeverysegmenthastostartwithanInstantaneousDecoder
freezes. Many heuristics and solutions have been proposed in
Refresh (IDR) frame, a higher bit rate is required to achieve
literature, but we refer to a survey by Seufert et al. for an
the same visual quality. Moreover, since a unique request is
elaborate view on the matter [2].
requiredtoretrieveeverysinglevideosegment,solutionswith
Despite the many advantages of HAS, there are drawbacks
low segment duration are susceptible to high round-trip times
as well. First, playout freezes still occur in 27% of video
(RTT).Thisproblemmainlyarisesinmobilenetworks,where
sessions [3]. Especially in environments with rapid band-
the RTT varies from 33 to 857ms, depending on the network
width changes, the client may fail to adapt to new network
carrier and the type of connection [6].
The contributions of this letter are threefold. First, we
J.vanderHooftisfundedbygrantoftheAgencyforInnovationbyScience
and Technology in Flanders (IWT). The research was performed partially explain an effective means to eliminate RTT cycles in Section
within the iMinds V-FORCE project (130655) and within the EU FP7-NoE II, using the server push feature of the recently standardized
FLAMINGO project (318488). The associate editor coordinating the review
HTTP/2 protocol [7], [8]. This approach allows to effectively
ofthisletterandapprovingitforpublicationwasB.Rong. J.
vanderHooft,S.Petrangeli,T.WautersandF.DeTurckarewithGhentUni- use short video segments, achieving the advantages described
versity-iMinds,DepartmentofInformationTechnology,Technologiepark15, above. Second we present the details of two measurement
B-9052Belgium.E-mail:jeroen.vanderhooft@intec.ugent.be.
studies in Section III. Particularly, we actively measured the
R. Huysegems, P. R. Alface and T. Bostoen are with Nokia - Bell Labs,
Copernicuslaan50,B-2018Antwerp,Belgium. available throughput in real 4G/LTE networks and performed

2 VANDERHOOFTetal.:HTTP/2-BASEDADAPTIVESTREAMINGOFHEVCVIDEOOVER4G/LTENETWORKS
RTT RTT RTT RTT Figure 2, at least one RTT cycle is gained in the reception of
Client
|     | MPD | s   |     |     | s   | s   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n-m+1 n n+1 the first video segment, and multiple RTT cycles are gained
|     |     |     |     | ... |     |     |     | ...        |        |        |        |      |         |     |           |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------ | ------ | ---- | ------- | --- | --------- |
|     |     |     |     |     |     |     |     | during the | buffer | rampup | phase. | Once | the MPD | and | the first |
|     | MPD |     | s   |     | s   |     | s   |            |        |        |        |      |         |     |           |
Server n-m+1 n n+1 m segments are sent, the server periodically pushes a new
|        |     |     |     | r   | r   |     | r   | r       |               |     |               |         |     |              |      |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------------- | ------- | --- | ------------ | ---- |
|        | RTT |     |     | n+1 | n+2 |     | n+3 | n+4     |               |     |               |         |     |              |      |
|        |     |     |     |     |     |     |     | segment | to the client | at  | the specified | quality |     | level. Every | time |
| Client | MPD |     |     |     | q   |     |     |         |               |     |               |         |     |              |      |
j a segment is received, the rate adaptation heuristic determines
|     |     |     | ... |     |     |     |     | ... |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MPD s s s s s themostsuitablevideoqualityandifrequired,arequestissent
| Server |     | n-m+1 |     | n   | n+1 | n+2 | n+3 |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r r r r to change the bit rate of pushed segments. Since the first m
|     |     |     |     | n+1 | n+2 |     | n+3 | n+4 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
segmentsarepushedback-to-backwhentheMPDisrequested,
| Figure | 2. An | example live | video | scenario | for HTTP/1.1 |     | (top) and | HTTP/2 |     |     |     |     |     |     |     |
| ------ | ----- | ------------ | ----- | -------- | ------------ | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
(bottom),wheretheclientrequestsmavailablesegmentstorampupthebuffer.
|     |     |     |     |     |     |     |     | the proposed | approach |     | can significantly |     | reduce | the | client’s |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ----------------- | --- | ------ | --- | -------- |
Ifthelastreleasedsegmenthasindexn,thefirstsegmenttoplayisn−m+1.
|            |                                                 |     |     |     |     |     |     | startup delay | in  | high-RTT | networks. |     | Short | segments | can be |
| ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --------- | --- | ----- | -------- | ------ |
| Notethatri | denotesthereleaseofsegmentiatserverside,whilesi |     |     |     |     |     |     | denotes       |     |          |           |     |       |          |        |
itsrequestfordownloadbytheclient.Furthermore,qualityqj indicatesthat used, as no RTT cycles are lost, further reducing the startup
theservershouldchangethequalityofpushedsegmentsto j. delay. Additionally, since a smaller buffer can be used, the
|             |     |             |     |          |          |     |              | approach | allows | to reduce | the | total end-to-end |     | delay | as well. |
| ----------- | --- | ----------- | --- | -------- | -------- | --- | ------------ | -------- | ------ | --------- | --- | ---------------- | --- | ----- | -------- |
| an analysis | of  | the induced |     | bit rate | overhead | for | short, HEVC- |          |        |           |     |                  |     |       |          |
encoded video segments. Third, detailed results are presented Preliminary evaluations showed that it is important to limit
|            |     |       |              |     |          |     |              | the maximum | number | of  | segments | in  | flight; | if a large | amount |
| ---------- | --- | ----- | ------------ | --- | -------- | --- | ------------ | ----------- | ------ | --- | -------- | --- | ------- | ---------- | ------ |
| in Section |     | IV to | characterize |     | the gain | of  | the proposed |             |        |     |          |     |         |            |        |
push-based approach compared to state-of-the-art HAS over of high-quality segments are queued in the network, e.g. right
HTTP/1.1. Final conclusions are drawn in Section V. afterabandwidthdrop,bufferstarvationatclient-sideislikely
|     |     |                          |     |     |     |     |     | to occur. | An appropriate |     | rule      | of thumb | for                  | the   | maximum |
| --- | --- | ------------------------ | --- | --- | --- | --- | --- | --------- | -------------- | --- | --------- | -------- | -------------------- | ----- | ------- |
|     | II. | HTTP/2PUSH-BASEDAPPROACH |     |     |     |     |     |           |                |     |           |          | (cid:0)RTT(cid:1)+1, |       |         |
|     |     |                          |     |     |     |     |     | number of | segments       | k   | in flight | is ceil  |                      | where | k is    |
seg
In HAS, a video session starts with the client sending a directly proportional to the ratio of the RTT and the segment
|         |         |         |       |              |     |             |        | duration | seg. Indeed, | the | higher | this ratio, | the | more | segments |
| ------- | ------- | ------- | ----- | ------------ | --- | ----------- | ------ | -------- | ------------ | --- | ------ | ----------- | --- | ---- | -------- |
| request | for the | video’s | media | presentation |     | description | (MPD). |          |              |     |        |             |     |      |          |
This file contains information regarding the video segments, should be pushed in order to bridge idle RTT cycles. In our
such as the duration, resolution and available bit rates. Based experimental setup, it will be sufficient to use k=2.
| on the | contents | of  | the MPD, | the | client | then | requests | video |     |     |     |     |     |     |     |
| ------ | -------- | --- | -------- | --- | ------ | ---- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
III. MEASUREMENTSTUDY
| segments    | subsequently, |          | generally |        | ramping  | up    | the buffer | by           |           |     |           |          |     |     |     |
| ----------- | ------------- | -------- | --------- | ------ | -------- | ----- | ---------- | ------------ | --------- | --- | --------- | -------- | --- | --- | --- |
|             |               |          |           |        |          |       |            | A. Available | Bandwidth |     | in 4G/LTE | Networks |     |     |     |
| downloading |               | segments | at the    | lowest | quality. | After | this       | startup      |           |     |           |          |     |     |     |
phase, further decisions regarding the video quality are made To evaluate the proposed approach, we decided to focus on
by the client. The main drawback of this approach is that 4G/LTE networks. In order to provide a realistic evaluation,
wecollectedthroughputmeasurementsin4Gnetworkswithin
| one RTT | cycle | is lost | to download |     | each | segment, | which | has a |     |     |     |     |     |     |     |
| ------- | ----- | ------- | ----------- | --- | ---- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
significantimpactonthestartuptimeandbandwidthutilization the city of Ghent, Belgium, in January and February 2016.
inhigh-RTTnetworks.ThisbehaviorisillustratedinFigure2, We have built a dataset over multiple routes, measuring
for the first phase of a live streaming session. the available bandwidth while downloading a large file over
The HTTP/2 standard was published as an IETF RFC in HTTP. To guarantee appropriate download speeds, we hosted
adedicatedserveriniLab.t’sVirtualWallinfrastructure1,con-
February2015,mainlyfocusingonthereductionoflatencyin
webdelivery[7].Recently,anumberofpaperswerepublished nected through a 100Mb/s Ethernet connection. In this way,
regarding the use of this new protocol in HAS. Wei et al. bandwidthandlatencymeasurementsindicatetheperformance
proposed a k-push approach, in which k segments are sent ofthewireless4Gconnection,withminimalinterferencefrom
per request [9]. In later work, the authors proposed to change thewirednetwork.Asfortheclient,wedevelopedanAndroid
|               |     |       |                  |     |       |     |         | application | which | logs | all required | information, |     | running | on  |
| ------------- | --- | ----- | ---------------- | --- | ----- | --- | ------- | ----------- | ----- | ---- | ------------ | ------------ | --- | ------- | --- |
| the parameter |     | value | of k dynamically |     | based | on  | network | char-       |       |      |              |              |     |         |     |
acteristics [10]. Focus in this research is mainly on reducing a smartphone (Huawei P8 Lite) connected over 4G. Similar
the live latency and the number of GET requests issued by to the collection of 3G throughput traces by Riiser et al.
the client, without considering the impact of freezes or the [12], several properties are logged, among which the GPS
encoding overhead introduced by shorter video segments. In coordinates, the number of bytes received since last datapoint
|     |     |     |     |     |     |     |     | and the | number | of milliseconds |     | since | last | datapoint. | From |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------------- | --- | ----- | ---- | ---------- | ---- |
previouswork,weproposedaschemeinwhichthebaselayer
segments for Scalable Video Coding (SVC) are pushed by the theselasttwoentries,theaveragethroughputcanbeobtained.
server,whileenhancementlayersarepulledbytheclient[11]. Wecollectedthroughputlogsforsixtypesoftransportation:
|     |     |     |     |     |     |     |     | foot, bicycle, | bus, | tram, | train | and | car2. | As an | example, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ----- | ----- | --- | ----- | ----- | -------- |
Althoughasignificantreductionofthefreezetimeisachieved
compared to AVC-based solutions, the encoding overhead Figure 3 shows the selected route in a car and the measured
introduced by inter-layer dependencies makes it unfeasible to bandwidth over time. Lower throughput values are observed
provide more than three quality representations. when connectivity is limited, due to tunnels, large buildings
In the push-based approach [8], the server uses HTTP/2’s and bad coverage in general. Also, the type of transportation
|        |      |         |            |     |        |        |         | and the selected |     | route | have a | strong | impact | on the | available |
| ------ | ---- | ------- | ---------- | --- | ------ | ------ | ------- | ---------------- | --- | ----- | ------ | ------ | ------ | ------ | --------- |
| server | push | to push | m segments |     | to the | client | as soon | as the           |     |       |        |        |        |        |           |
MPD request is received, where m corresponds to the number bandwidth. As an example, the average throughput on a train
of segments that fit into a preferred buffer size defined by the around the city was 22.8Mb/s±14.6Mb/s, while this was
| client. | Since | state-of-the-art |     | heuristics | ramp | up  | the buffer | by  |     |     |     |     |     |     |     |
| ------- | ----- | ---------------- | --- | ---------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
1 http://ilabt.iminds.be/iminds-virtualwall-overview
| downloading |     | segments | at  | the lowest | quality, | it  | makes | sense |     |     |     |     |     |     |     |
| ----------- | --- | -------- | --- | ---------- | -------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
2 TheauthorswouldliketothankT.BaeleandL.Timpermanfortheirkind
to push segments at this quality as well. As illustrated in assistanceduringthedatacollection.

VANDERHOOFTetal.:HTTP/2-BASEDADAPTIVESTREAMINGOFHEVCVIDEOOVER4G/LTENETWORKS 3
|     |     |     |  100 |     |     |     |     |     |  40 |                 |     |                  |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | --- | --- |
|     |     |     |      |     | 1 2 | 3   |     |     |     |  SD - 0.3 Mb/s  |     |  FHD - 5.2 Mb/s  |     |     |
|     |     |     |      |     |     |     |     |     |     |  HD - 1.0 Mb/s  |     |  4K - 10.9 Mb/s  |     |     |
 80
|     |     | ]s/bM[ tuphguorhT |     |     |     |     |     |     |  30 |  FHD - 2.3 Mb/s  |     |  4K - 21.4 Mb/s  |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------------- | --- | --- |
]s/bM[ etar tiB
 60
 20
 40
 10
 20
|     |     |     |  0  |      |          |      |      |     |  0    |     |            |     |      |     |
| --- | --- | --- | --- | ---- | -------- | ---- | ---- | --- | ----- | --- | ---------- | --- | ---- | --- |
|     |     |     |  0  |  100 |  200     |  300 |  400 |     |  8 16 |  30 |  60        |     |  120 |     |
|     |     |     |     |      | Time [s] |      |      |     |       |     | GOP length |     |      |     |
Figure3. Acartravellingfromnorthtosouth(left),alongwiththemeasured Figure 4. Obtained video bit rates for the different quality representations
throughput(right).Whentravellingfrom(1)to(2),largetownhousesonthe andaGOPlengthof8,16,30,60and120frames.
rightsideimpedetheclient’sconnection.Arrivingat(2),theclientswitches
toanewantennawithbettercoverage.Onceanopenareaisreachedin(3) OpenCL acceleration was able to encode the FHD content in
andanewantennaisagainselected,throughputimprovessignificantly. real-time, with frame rates ranging from 63 FPS (GOP 8) to
33.9Mb/s±15.8Mb/s in a car driving on the ring road. The 68FPS(GOP120).Forthe4Krepresentationshowever,frame
measured bandwidth ranged from 0Mb/s (connection inter- rates ranged from 21 FPS (GOP 8) to 24 FPS (GOP 120).
|         |         |         |         |      |         |         |     | Faster software | HEVC | encoders | were | reported | recently | to be |
| ------- | ------- | ------- | ------- | ---- | ------- | ------- | --- | --------------- | ---- | -------- | ---- | -------- | -------- | ----- |
| rupted) | through | 111Mb/s | (higher | than | 100Mb/s | because | of  |                 |      |          |      |          |          |       |
network queuing), with an average of 30.3Mb/s±16.7Mb/s. abletoencode4Kinreal-timeonsimilarCPUplatforms[14].
| The complete | dataset, |     | which | consists | of 40 | traces and | covers |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ----- | -------- | ----- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
5 hours of monitoring, has been made available online [13]. IV. EVALUATION
|     |     |     |     |     |     |     |     | A. Experimental | Setup |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | --- | --- | --- | --- | --- |
B. HEVC-Encoded Video To allow a fair comparison of the proposed approach with
In this research, we decided to focus on HEVC because of traditional HAS, a network topology is emulated using the
its promising compression efficiency. Since our intention is to MiniNet framework4. It consists of a single client, streaming
|     |     |     |     |     |     |     |     | the encoded | video from | a dedicated |     | Jetty web | server5. | A new |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ----------- | --- | --------- | -------- | ----- |
usevideosegmentswithasub-secondduration,itisimportant
to analyze the induced encoding overhead. The considered request handler is defined, which processes the client’s GET
video sequence in our analysis and evaluation is Netflix’s El requestsusingaspecificquerytostartthepushingofsegments
Fuente, which has a total length of 476 seconds and a frame atagivenqualityrepresentation.Theclientisimplementedon
rate of 60FPS. The video is encoded using HEVC, providing top of the libdash library6, the official reference software of
six quality levels at nominal bitrates of 0.3, 1.0, 2.3, 5.2, the MPEG-DASH standard. We provided support for HTTP/2
usingthenghttp2library7,andimplementedtherequiredlogic
| 10.9 and | 21.4Mb/s, |     | with a | spatial | resolution | ranging | from |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------ | ------- | ---------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
540p to 2160p video. Using the x265 encoder3, the video to asynchronously handle pushed video segments. Client-side
is segmented using five segment durations: 133, 267, 500, rateadaptationisbasedontheFINEASheuristicbyPetrangeli
1000 and 2000ms. To allow each segment to be decoded et al. [15]. This heuristic estimates the segments’ download
independently, every segment starts with an IDR frame and time to achieve a target buffer filling level, resulting both in
the Group Of Pictures (GOP) length is set to 8, 16, 30, 60 a higher video quality and a lower amount of playout freezes
and 120 frames respectively. To assess the impact of shorter compared to state-of-the-art solutions. To avoid an excessive
GOP lengths on the compression performance, the encodings amount of quality switches for short segments, the client is
fordifferentsegmentdurationshavebeensettotargetthesame only allowed to increase the quality every 2s. The collected
visualqualityandallowasubsequentoverheadintheachieved 4Gtracesforsame-typevehiclesaremergedtogether,inorder
nominalbitrate.Torealizethis,wehaveselectedtheConstant to obtain 30 unique bandwidth traces with a minimal length
Rate Factor (CRF) rate control implemented in the x265 of 494s and an average bandwidth of 30.3Mb/s±16.8Mb/s.
Usingtrafficcontrolcommandtcfortrafficshaping,theclient
| encoder. | The obtained |     | encodings | for | the same | nominal | rates |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
but different segment durations, have the same visual quality, canstream30episodesofthevideowithadifferentbandwidth
measured in terms of Peak-Signal-to-Noise-Ratio (PSNR), patternforeveryepisode.Alowerthresholdof50kb/sisused,
with deviations smaller than 0.233dB. Compared to a GOP in order to guarantee correct packet scheduling with tc. The
length of 120 frames, the average over-head is 6.3%, 9.2%, bandwidth at server-side is fixed at 100Mb/s, same as in the
|     |     |     |     |     |     |     |     | measurement | study. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
29.3%and60.5%foraGOPlengthof60,30,16and8frames
| respectively. | Figure | 4   | shows | the obtained | bit | rates of | the six |     |     |     |     |     |     |     |
| ------------- | ------ | --- | ----- | ------------ | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
quality representations, with a clear increase for segments B. Obtained Results
with a sub-second duration. In the next section, the proposed First, the performance of traditional HAS and the push-
approach will be evaluated for a segment duration of 500ms. based approach are evaluated for increasing values for the
| This allows | to reduce |     | the buffer | size | to the | order of | seconds |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | ---- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
RTT,withaninitialbuffersizeof10s.Notethatwhenplayout
and increase video quality in high-RTT networks, while the freezes occur, the buffer is expanded as to hold all segments
overhead is limited to 9.2%. released at server-side. Figure 5 shows that for HTTP/1.1,
As for the encoding time, using a multicore platform with the video quality, averaged out over all segments - 0 for the
| Intel Core | i7 CPUs | and | an Nvidia | GTX | 980 | GPU, x265 | with |                       |     |     |     |                                 |     |     |
| ---------- | ------- | --- | --------- | --- | --- | --------- | ---- | --------------------- | --- | --- | --- | ------------------------------- | --- | --- |
|            |         |     |           |     |     |           |      | 4 http://mininet.org/ |     |     |     | 5 http://www.eclipse.org/jetty/ |     |     |
3 http://x265.org 6 https://github.com/bitmovin/libdash 7 https://nghttp2.org/

4 VANDERHOOFTetal.:HTTP/2-BASEDADAPTIVESTREAMINGOFHEVCVIDEOOVER4G/LTENETWORKS
 5 HTTP Buffer[s]VideoqualityQualityswitchesFreezetime[s]Startupdelay[s]
|     |     |     |     |     |     |     | HTTP/1.1 | 10 4.919±0.132 |     | 49.633±6.663 | 9.817±4.988 |     | 2.408±0.052 |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------------ | ----------- | --- | ----------- | --- |
 4 HTTP/1.1 6 4.754±0.140 64.333±7.254 15.190±5.204 2.405±0.047
ytilauq oediv egarevA HTTP/2 10 5.288±0.111 52.067±9.766 4.867±3.361 1.806±0.085
|     |     |     |     |     |     |     | HTTP/2 | 6 5.270±0.11760.233±10.600 |     |     | 8.977±4.363 |     | 1.799±0.084 |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------------------- | --- | --- | ----------- | --- | ----------- | --- |
 3
TableI
 2
PERFORMANCESUMMARYFORANRTTOF300ms.AVERAGEVALUES
AREREPORTED,ALONGWITHTHE95%CONFIDENCEINTERVALS.
 1  HTTP/1.1 - GOP 120
 HTTP/1.1 - GOP 30
|     |     |  HTTP/2    - GOP 30 |     |     |     |     |     |     | V.  | CONCLUSIONS |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
 0
|     |  0  |  100 |  200 |  300 |  400 |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Round-trip time [ms] Inthisletter,wediscussedanHTTP/2push-basedapproach
Figure 5. Impact of the RTT on the video quality, both for HTTP/1.1 and for HTTP Adaptive Streaming (HAS) which enables the use
HTTP/2withaninitialbuffersizeof10seconds. of video segments with a sub-second duration in mobile,
 6  50 high round-trip time networks. We quantified the encoding
|     |     | Quality HTTP/1.1   | Freezes HTTP/1.1 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Quality HTTP/2 Freezes HTTP/2 overhead for short HEVC-encoded segments, and determined
|     |  5  |     |     |  40 | ]s[ emit ezeerf egarevA |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ytilauq oediv egarevA
|     |     |     |     |     |     |     | that the | segment | duration | should | not be | lower than | 500ms | to  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ------ | ------ | ---------- | ----- | --- |
 4
|     |     |     |     |  30 |     |     | limit the | overhead | to 9.2%. | We  | also performed |     | measurements |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | --- | -------------- | --- | ------------ | --- |
 3
|     |     |     |     |     |     |     | for the available |     | bandwidth | in  | real 4G/LTE | networks |     | within |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | --- | ----------- | -------- | --- | ------ |
 20
 2
|     |     |     |     |     |     |     | the city | of Ghent, | Belgium, |     | and created | a   | dataset | which |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | --- | ----------- | --- | ------- | ----- |
 1  10 has been made available online. Using the encoded content
 0  0 and collected throughput traces in an extensive evaluation,
|     |  2  |  4  |  6  8 |  10 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Buffer size [s] we showed that the presented approach results in a higher
Figure6. Impactofthebuffersizeonthevideoqualityandfreezetime,both video quality (+7.5%) and a lower freeze time (−50.4%), and
forHTTP/1.1(GOP120)andHTTP/2(GOP30)withanRTTof300ms.
|                |            |       |                   |                       |     |         | allows to  | reduce  | the live | delay      | compared   | to                  | solutions | over |
| -------------- | ---------- | ----- | ----------------- | --------------------- | --- | ------- | ---------- | ------- | -------- | ---------- | ---------- | ------------------- | --------- | ---- |
|                |            |       |                   |                       |     |         | HTTP/1.1.  | Future  | work     | will focus | on further |                     | improving | the  |
| lowest quality | level,     | 5 for | the highest       | - drops significantly |     | for     |            |         |          |            |            |                     |           |      |
|                |            |       |                   |                       |     |         | user’s QoE | through | HTTP/2   | features   | such       | as request/response |           |      |
| higher RTTs,   | regardless |       | whether a segment | duration              |     | of 2000 |            |         |          |            |            |                     |           |      |
or500msisused.Thevideoqualityfortheproposedapproach multiplexing and stream prioritization, on reducing the en-
|             |     |              |          |         |           |     | coding overhead |     | for short | video | segments | and | on adaptively |     |
| ----------- | --- | ------------ | -------- | ------- | --------- | --- | --------------- | --- | --------- | ----- | -------- | --- | ------------- | --- |
| over HTTP/2 | is  | not impacted | however, | because | bandwidth |     |                 |     |           |       |          |     |               |     |
utilization is maximized by actively pushing segments from changing the segment duration based on network conditions.
server to client. Short segments can thus effectively be used, REFERENCES
| which is | not true | for traditional | HAS | over HTTP/1.1. |     |     |                                                                |     |     |     |     |     |     |     |
| -------- | -------- | --------------- | --- | -------------- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          |          |                 |     |                |     |     | [1] SandvineIncorporated,“GlobalInternetPhenomenaReport,”2016. |     |     |     |     |     |     |     |
In a second set of experiments, performance is evaluated [2] M.Seufertetal.,“ASurveyonQualityofExperienceofHTTPAdaptive
as a function of the initial buffer size, for an RTT of 300ms. Streaming,”IEEECommunicationsSurveysTutorials,vol.17,no.1,pp.
| Figure 6 | shows | that, while | the video | quality | over HTTP/1.1 |     | 469–492,2015.                              |     |     |     |     |     |     |     |
| -------- | ----- | ----------- | --------- | ------- | ------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|          |       |             |           |         |               |     | [3] Conviva,“ViewerExperienceReport,”2015. |     |     |     |     |     |     |     |
increases for larger values of the buffer size, it is more or less [4] T.Lohmaretal.,“DynamicAdaptiveHTTPStreamingofLiveContent,”
constant for the push-based approach. Despite an encoding in IEEE International Symposium on a World of Wireless, Mobile and
overhead of 9.2%, the average quality is significantly higher MultimediaNetworks,2011,pp.1–8.
|     |     |     |     |     |     |     | [5] G. J. | Sullivan | et al., “Overview | of  | the High | Efficiency | Video | Coding |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----------------- | --- | -------- | ---------- | ----- | ------ |
becauseofbetterbandwidthutilization.Asforthefreezetime, (HEVC) Standard,” IEEE Trans. on Circuits and Systems for Video
a clear decrease is observed for higher buffer sizes, because Technology,vol.22,no.12,pp.1649–1668,2012.
|           |        |                |         |             |             |     | [6] OpenSignal,“IConnect4GCoverageMaps,”2014.[Online].Available: |     |     |     |     |     |     |     |
| --------- | ------ | -------------- | ------- | ----------- | ----------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| a playout | freeze | is less likely | if more | content can | be buffered |     |                                                                  |     |     |     |     |     |     |     |
http://opensignal.com/networks/usa/iconnect-4g-coverage
| at client-side. | More | importantly | however, | the | freeze time | for |               |     |                 |          |          |         |     |         |
| --------------- | ---- | ----------- | -------- | --- | ----------- | --- | ------------- | --- | --------------- | -------- | -------- | ------- | --- | ------- |
|                 |      |             |          |     |             |     | [7] M. Belshe | et  | al., “Hypertext | Transfer | Protocol | Version |     | 2,” RFC |
the proposed approach is always lower than for traditional Editor, Tech. Rep. Internet-Draft, 2015. [Online]. Available: https:
//datatracker.ietf.org/doc/draft-ietf-httpbis-http2/
| HAS, because | the         | client    | can respond    | faster to | changes | in the   |                  |         |                       |             |                 |            |             |          |
| ------------ | ----------- | --------- | -------------- | --------- | ------- | -------- | ---------------- | ------- | --------------------- | ----------- | --------------- | ---------- | ----------- | -------- |
|              |             |           |                |           |         |          | [8] R. Huysegems |         | et al., “HTTP/2-Based |             | Methods         | to Improve |             | the Live |
| available    | bandwidth   | or buffer | fulling.       |           |         |          |                  |         |                       |             |                 |            |             |          |
|              |             |           |                |           |         |          | Experience       | of      | Adaptive              | Streaming,” | in ACM          | Multimedia | Conference, |          |
| The most     | relevant    | results   | are summarized | in        | Table   | I. For a | 2015,pp.541–550. |         |                       |             |                 |            |             |          |
|              |             |           |                |           |         |          | [9] S. Wei       | et al., | “Low Latency          | Live        | Video Streaming |            | over HTTP   | 2.0,”    |
| standard     | buffer size | of 10s,   | the proposed   | approach  | results | in       |                  |         |                       |             |                 |            |             |          |
inACMNetworkandOperatingSystemSupportonDigitalAudioand
(+7.5%),
a significantly higher video quality a lower freeze VideoWorkshop,2014,pp.37:37–37:42.
time (−50.4%) and a lower startup delay (−25.0%) compared [10] M.Xiaoetal.,“EvaluatingandImprovingPush-BasedVideoStreaming
to traditional HAS. Focusing on a reduction of the live delay, withHTTP/2,”inACMInternationalWorkshoponNetworkandOper-
atingSystemsSupportforDigitalAudioandVideo,2016,pp.3:1–3:6.
a smaller buffer size of 6s with pull-based HAS results in a [11] J. van der Hooft et al., “An HTTP/2 Push-Based Approach for SVC
significantly lower video quality (−3.4%) and a higher freeze Adaptive Streaming,” in IEEE/IFIP Network Operations and Manage-
time (+54.7%), compared to a buffer size of 10s. However, mentSymposium,2016,pp.104–111.
|     |     |     |     |     |     |     | [12] H.Riiseretal.,“CommutePathBandwidthTracesfrom3GNetworks: |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
comparing results for the push-based approach and a buffer AnalysisandApplications,”inACMConferenceonMultimediaSystems,
size of 6s, with traditional HAS and a buffer size of 10s, 2013,pp.114–118.
(+7.1%) [13] J. van der Hooft et al., “4G/LTE Bandwidth Logs,” 2016. [Online].
| a higher | video | quality | and | a lower | startup | delay |     |     |     |     |     |     |     |     |
| -------- | ----- | ------- | --- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Available:http://users.ugent.be/~jvdrhoof/dataset-4g/
| (−25.3%) | are obtained, |     | while differences | for | the freeze | time |            |      |            |                     |     |            |           |     |
| -------- | ------------- | --- | ----------------- | --- | ---------- | ---- | ---------- | ---- | ---------- | ------------------- | --- | ---------- | --------- | --- |
|          |               |     |                   |     |            |      | [14] T. K. | Heng | et al., “A | Highly Parallelized |     | H.265/HEVC | Real-Time |     |
are not statistically significant (two-tailed Wilcoxon signed- UHD Software Encoder,” in IEEE International Conference on Image
|            | p=0.82). |      |            |              |          |     | Processing,2014,pp.1213–1217. |     |                     |     |                 |           |     |          |
| ---------- | -------- | ---- | ---------- | ------------ | -------- | --- | ----------------------------- | --- | ------------------- | --- | --------------- | --------- | --- | -------- |
| rank test, |          | This | shows that | the proposed | approach |     |                               |     |                     |     |                 |           |     |          |
|            |          |      |            |              |          |     | [15] S. Petrangeli            |     | et al., “QoE-driven |     | Rate Adaptation | Heuristic |     | for Fair |
allowstheclienttofollowthelivesignalmoreclosely,without
|     |     |     |     |     |     |     | Adaptive | Video | Streaming,” | ACM | Trans. on | Multimedia | Computing, |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----------- | --- | --------- | ---------- | ---------- | --- |
CommunicationsandApplications,vol.12,no.2,pp.28:1–28:24,2015.
| losing performance |     | on other | metrics. |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |