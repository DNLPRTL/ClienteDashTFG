562 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
A Survey on Bitrate Adaptation Schemes for
Streaming Media Over HTTP
Abdelhak Bentaleb , Member, IEEE, Bayan Taani , Member, IEEE, Ali C. Begen , Senior Member, IEEE,
Christian Timmerer , Senior Member, IEEE, and Roger Zimmermann , Senior Member, IEEE
Abstract—In this survey, we present state-of-the-art bitrate that it will reach 80% by 2021 [1]. This trend poses chal-
adaptation algorithms for HTTP adaptive streaming (HAS). As lengesindeliveringvideoswiththebestQualityofExperience
a key distinction from other streaming approaches, the bitrate
(QoE)overtoday’sInternet,whichwasoriginallydesignedfor
adaptation algorithms in HAS are chiefly executed at each
best-effort, non-real-time data transmission. Around 2005, an
client, i.e., in a distributed manner. The objective of these
algorithms is to ensure a high quality of experience (QoE) elegant yet simple video delivery paradigm was introduced
for viewers in the presence of bandwidth fluctuations due to by Move Networks, which quickly became popular due to its
factors like signal strength, network congestion, network recon- better features and cheaper deployment costs over progres-
vergence events, etc. While such fluctuations are common in
sive download and other proprietary streaming methods. This
public Internet, they can also occur in home networksor even
newparadigm,whichwerefertoasHTTPadaptivestreaming
managed networks where there is often admission control and
QoS tools. Bitrate adaptation algorithms may take factors like (HAS), treated the media content like regular Web contentand
bandwidthestimations,playbackbufferfullness,devicefeatures, delivereditinsmallpiecesoverHTTPprotocol.HASquickly
viewerpreferences,andcontentfeaturesintoaccount,albeitwith became the dominant approach for video streaming due to
differentweights.Sincetheviewer’sQoEneedstobedetermined
its adoption by leading service and content providers. Video
inreal-timeduringplayback,objectivemetricsaregenerallyused
deliveryoverthepublicInternetisalsoreferredtoasover-the-
including number of buffer stalls, duration of startup delay,
frequency and amount of quality oscillations, and video insta- top (OTT) video streaming, since the content or the streaming
bility. By design, the standards for HAS do not mandate any serviceproviderusuallydiffersfromthenetworkprovider.The
particular adaptation algorithm, leaving it to system builders emergence of HAS and new, mostly mobile end-user devices
to innovate and implement their own method. This survey pro-
with high processing and rendering capabilities played a key
videsanoverviewofthedifferentmethodsproposedoverthelast
role in the growth of streaming video traffic.
several years.
In traditional non-HAS IP-based streaming, the client
IndexTerms—Bitrateadaptation,HAS,DASH,adaptivevideo
receivesmediathatistypicallypushedbyamediaserverusing
streaming, ABR schemes.
either connection-oriented protocols such as the Real-time
MessagingProtocol(RTMP/TCP)[2]orconnectionlessproto-
colssuchastheReal-timeTransportProtocol(RTP/UDP)[3].
I. INTRODUCTION
A common protocol to control the media servers in tradi-
VIDEO delivery has evolved to constitute a major frac- tionalstreamingsystems(asshowninFig.1a)istheReal-time
tion of today’s Internet traffic in the last decade thanks Streaming Protocol (RTSP) [4]. RTSP is responsible for set-
to advancements in network technologies, device capabili- ting up a streaming session and keeping the state information
ties, and audio-video compression schemes. Cisco reported during this session, but is not responsible for actual media
in their annual Visual Networking Index that in 2016, 67% delivery, which is the task for a protocol such as RTP. Based
of the global Internet traffic was video, with a projection ontheRTPControlProtocol(RTCP)reportssentbytheclient,
themediaservermayperformrateadaptationanddatadelivery
ManuscriptreceivedDecember21,2017;revisedMay19,2018;accepted
scheduling.Thesecharacteristicsresultincomplexandexpen-
July 19, 2018. Date of publication August 3, 2018; date of current ver-
sion February 22, 2019. This work was supported in part by the National siveservers.Additionalprotocolsorconfigurationsareneeded
Natural Science Foundation of China under Grant 61472266, in part by duringthesessionestablishmentincasenetworkaddresstrans-
the National University of Singapore (Suzhou) Research Institute, and
lation (NAT) devices and firewalls block the control or media
in part by the Austrian Research Promotion Agency (FFG) under the
NextGenerationVideoStreamingProject“PROMETHEUS.”(Corresponding traffic[5].Despiteimplementingthesamebaselineprotocol(s),
author:AbdelhakBentaleb.) media servers from different vendors may behave differently
A. Bentaleb, B. Taani, and R. Zimmermann are with the School
due to optional features or differences in implementation.
of Computing, National University of Singapore, Singapore (e-mail:
bentaleb@comp.nus.edu.sg; bayan@comp.nus.edu.sg; rogerz@comp.nus. Failoversduetoaserverfaultoftencausepresentationglitches
edu.sg). andarerarelyseamlessunlesscertainredundancyschemesare
A.C.BegeniswithNetworkedMedia,OzyeginUniversity,Istanbul34794,
in place. These scalability and vendor dependency issues as
Turkey(e-mail:ali.begen@ozyegin.edu.tr).
C. Timmerer is with the Institute of Information Technology, well as high maintenance costs have resulted in deployment
Alpen-Adria Universität Klagenfurt, 9020 Klagenfurt, Austria, and challenges for protocols like RTSP.
also with Bitmovin Inc., San Francisco, CA 94105 USA (e-mail:
HAS uses HTTP as the application and TCP as the
christian.timmerer@itec.uni-klu.ac.at).
DigitalObjectIdentifier10.1109/COMST.2018.2862938 transport-layer protocol, as illustrated in Fig. 1b, and clients
1553-877X(cid:2)c 2018IEEE.Translationsandcontentminingarepermittedforacademicresearchonly. Personaluseisalsopermitted,butrepublication/
redistributionrequiresIEEEpermission. Seehttp://www.ieee.org/publications_standards/publications/rights/index.htmlformoreinformation.

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 563
TABLEI
DIFFERENCESBETWEENTHETRADITIONALSTREAMINGANDHASSYSTEMS
any state, hence, the client may download segments from dif-
ferent servers without impacting system scalability [7]; and
(4) it does not require a persistent connection between the
client and the server, which improves system scalability and
reduces implementation and deployment costs.
Today, HAS accounts for the majority of Internet video
traffic. It has reached mainstream due to commercial solu-
tions such as Microsoft’s Smooth Streaming [8], Apple’s
HTTP Live Streaming (HLS) [9], Adobe’s HTTP Dynamic
Streaming (HDS) [10], Akamai’s HD [11] and several open-
source solutions. To avoid fragmentation in the market, the
Moving Picture Experts Group (MPEG) together with the
3rd Generation Partnership Project (3GPP) started working
on HTTP streaming of MPEG media and HAS, respectively.
Fig.1. CommunicationintraditionalstreamingandHASsystems.
These efforts eventually resulted in the standardization of
Dynamic Adaptive Streaming over HTTP (DASH) [12].
Unlike proprietary solutions, DASH provides an open spec-
pullthedatafromastandardHTTPserver,whichsimplyhosts
ification for adaptive streaming over HTTP and leaves the
the media content. HAS solutions employ dynamic adapta-
implementation of the adaptation logic to third parties as
tion with respect to varying network conditions to provide a
shown in Fig. 2a, where blue components are specified in the
seamless (or at least smoother) streaming experience. Once a
DASH standard, while red components are left unspecified or
media file (or stream) is ready from a source, it is prepared
specified in other standards. The DASH server is essentially
for streaming before it is published to a standard, off-the-
anHTTPserverthathoststhemediasegments,whicharetyp-
shelf HTTP server. The original file/stream is partitioned into
icallytwototensecondseach,orcouldbeaslongashoursfor
segments (also called chunks) of equi-length playback time.
the entire content duration in presentation time. Each segment
Multiple versions (also called representations) of each seg-
is encoded at multiple bitrate levels and listed in the manifest
mentaregeneratedthatvaryinbitrate/resolution/qualityusing
termed Media Presentation Description (MPD, see Fig. 2b).
an encoder or a transcoder (See Section II-A). Moreover, the
The MPD is an XML document that provides an index for
server generates an index file, which is a manifest that lists
the available media segments at the server. At the client side,
theavailablerepresentationsincludingHTTPuniformresource
DASH implements the bitrate adaptation logic, which issues
locators(URLs)toidentifythesegmentsalongwiththeiravail-
timed requests and downloads segments that are described in
ability times. During a typical HAS session, the client first
theMPDfromtheserverusingHTTP(partial)GETmessages.
receives the manifest that contains the metadata for video,
During download, the DASH client estimates the available
audio, subtitles, and other features, then constantly measures
bandwidthinthenetworkandusesinformationfromtheplay-
certainparameters:availablenetworkbandwidth,bufferstatus,
back buffer to select a suitable bitrate for the next segment to
batteryandCPUlevels,etc.Accordingtotheseparameters,the
be fetched. This behavior is called bitrate switching, where
HAS client repeatedly fetches the most suitable next segment
the client’s goal is to fetch the highest-bitrate segments it can,
among the available representations from the server. Table I
while keeping sufficient data in the playback buffer to avoid
compares the main characteristics of the traditional streaming
video stalls and thus achieve a good QoE trade-off.
and HAS systems.
There are various implementations of DASH players.1 For
HASisaddressingseveralaspectsthatweremajorconcerns
example, dash.js [13] is a JavaScript-based DASH client,
in traditional streaming protocols [2]–[4]: (1) it uses HTTP to
which is the reference client from the DASH Industry Forum.
deliver video segments, which simplifies the traversal through
Another JavaScript-based client is DASH-JS [14], which
NATs and firewalls [6]; (2) at the server side, it uses con-
proposes a simple rate adaptation logic.
ventionalWebserversorcachesavailablewithinthenetworks
A recent survey [15] describes a range of bitrate adaptation
of Internet Service Providers (ISPs) and Content Distribution
(calledalsoAdaptiveBitRate(ABR))schemesandtechniques
Networks (CDNs); (3) a client requests and fetches each seg-
ment independently from others and maintains the playback
session state, whereas the server is not required to maintain 1Inthissurvey,thetermsplayerandclientareusedinterchangeably.

564 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
bitrate adaptation logic within the system and which entities
are involved.
The rest of this survey is organized as follows: Section II
describes background information and definitions. Section III
surveys the bitrate adaptation schemes. Comparisons between
different schemes and a discussion are presented in
Sections IV and V, respectively. Finally, Section VI provides
concluding remarks.
II. BACKGROUNDANDDEFINITIONS
A. Video Coding Standards
InanHASsystem,amediafile(orinthecaseoflivevideo,
a stream comprising chunks of audiovisual data) is encoded
or transcoded into multiple representations. The most widely
used video coding format is currently H.264, also known as
MPEG-4AdvancedVideoCoding(AVC)[18].Thisvideocod-
ing standard was introduced by MPEG in collaboration with
the ITU-T Video Coding Experts Group (VCEG). A client
requesting and downloading segments from possibly different
representations (encoded at different bitrates) seamlessly con-
catenatethesesegmentsinitsplaybackbuffer.Thisresultsina
conforming bitstream that can be processed using a standard
decoder. A common assumption is that each segment starts
with an intra/key frame (i.e., IDR-frame in AVC), in order
for the decoder to process segments independently from each
other.Thismayleadtocodinginefficienciesforshortsegment
durations [19].
Fig.2. DynamicAdaptiveStreamingoverHTTP(DASH).
Scalable Video Coding (SVC) has been introduced as an
extension to AVC [20]. SVC enables splitting a video stream
into multiple bitstreams or layers, where each one of them
for DASH. The authors classified the schemes into three main consists of subsets of video data. It recombines these bit-
categories: client-side, server-side and in-network approaches. streamsubsetsinordertoadditivelyincreasethevideoquality.
They provided a general review of video traffic measurement Typically, SVC allows the video stream to be split into
methods and a set of characterization studies for well-known three different dimensions of quality: temporal, spatial, and
commercial streaming providers like Netflix, YouTube, and quality/Signal-to-Noise Ratio (SNR). In the temporal-based
Akamai, and outlined several open research problems in the technique, the video is encoded at multiple frame rates for
DASH streaming field. Our survey differs in terms of two a given resolution. The base layer has the lowest frame rate,
key aspects: (1) a scheme classification is provided that is whileenhancementlayersincreasetheframerate,whichgrad-
structuredbasedontheuniquefeaturesoftheadaptationlogics ually improves quality. In the spatial-based technique, the
and(2)moreschemesareexaminedandadetailedcomparison video is encoded at multiple spatial resolutions for a given
table is provided. frame rate. In case of the SNR-based technique, the video is
Most state-of-the-art HAS solutions solely integrate the encoded at a single spatial resolution, and the enhancement
bitrate adaptation logic inside the HAS client, since it allows layers improve quality, keeping the resolution constant.
theclienttoselectabitratelevelindependentlyandavoidsthe The H.265 video codec (also known as High Efficiency
requirement of having intelligent devices inside the network Video Coding (HEVC)) was developed to provide approxi-
infrastructure. This represents a key reason why HAS solu- mately twice the encoding efficiency of AVC [21]. Similarly,
tions are used in OTT scenarios. Nevertheless, both industry as an extension to HEVC, Scalable High-efficiency Video
and academia recommend using HAS systems in managed Coding (SHVC) [22] was developed to support scalability.
networks as well [16], [17]. For instance, a client may use Conceptually similar to SVC, it adds extra scalability fea-
feedback reported by a server or the network in bitrate adap- tures such as bit-depth, color gamut, and hybrid scalability. In
tationtoimprovetheoverallQoE,orbyusingIPmulticasting addition, it enhances coding-specific functionalities like Inter-
to simplify the video distribution in the context of connected Layer Prediction (ILP) (optionally encoding the base layer in
TVs. In this survey, we present a classification of state-of- AVC instead of HEVC), and the use of motion-constrained
the-art bitrate adaptation schemes including features, pros, tiles. In both SVC and SHVC, the base layer is always back-
and cons. We classify the schemes into four main categories: wardscompatiblewiththenon-scalableversionoftheencoder
client-based, server-based, network-assisted, and hybrid (See (AVC and HEVC, respectively), thus, only an AVC/HEVC
Fig. 3). The classification is based on the location of the decoder is needed.

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 565
Fig.3. HASadaptationschemeclassification.
Recently,MPEGandVCEGteameduptoworkonVersatile
| Video Coding  |                           | (VVC),  | aiming        | to provide   | almost             | twice the      |     |     |     |     |     |
| ------------- | ------------------------- | ------- | ------------- | ------------ | ------------------ | -------------- | --- | --- | --- | --- | --- |
| encoding      | efficiency                | of      | HEVC. VVC     | specifically |                    | targets appli- |     |     |     |     |     |
| cations and   | servicesusingimmersiveand |         |               |              | high-dynamic-range |                |     |     |     |     |     |
| (HDR) videos. |                           | The     | new standard  | is           | expected           | to become      |     |     |     |     |     |
| available     | in 2020                   | [23].   |               |              |                    |                |     |     |     |     |     |
| Additionally, |                           | royalty | free encoding | formats      |                    | such as VP9    |     |     |     |     |     |
| and AV1       | are increasingly          |         | used          | for HAS,     | and subject        | to var-        |     |     |     |     |     |
Fig.4. HASvideostreamingsessionstates.
| ious evaluations. |      | For          | example, | open-source    | implementations |                |                 |          |            |                    |                    |
| ----------------- | ---- | ------------ | -------- | -------------- | --------------- | -------------- | --------------- | -------- | ---------- | ------------------ | ------------------ |
| of AVC,           | HEVC | and VP9      | have     | been evaluated |                 | in large-scale |                 |          |            |                    |                    |
| video-on-demand   |      | environments |          | [24].          |                 |                |                 |          |            |                    |                    |
|                   |      |              |          |                |                 |                | previous chunk  | is fully | downloaded | (See               | Fig. 4). After the |
|                   |      |              |          |                |                 |                | playback buffer | level    | reaches    | a target threshold | (e.g., 30 sec-     |
B. Common Problems in HTTP Adaptive Streaming onds, however, note that this threshold varies among different
Whilemovingfromaserver-pushtoaclient-pullmodelhas bitrate adaptation schemes or could be increased or decreased
clearbenefits,HASstillfaceschallenges.Knownissuesrelate based on the expected conditions), the client enters the steady
| to the heterogeneous |     | nature | of networks, |     | the increasing | num- |     |     |     |     |     |
| -------------------- | --- | ------ | ------------ | --- | -------------- | ---- | --- | --- | --- | --- | --- |
state.Theobjectiveduringthesteadystateistokeepthebuffer
ber of users, and the growing demand of high-quality content. level above a minimum threshold despite bandwidth fluctua-
WedescribefourmainproblemsthatcanaffectHASsystems: tions or interruptions, in order to avoid buffer underrun or
(1)multi-clientcompetitionandstabilityissues,(2)consistent- stall events. The steady state consists of two activity periods
qualitystreaming,(3)QoEoptimizationandmeasurement,and referred to as ON and OFF. Fundamentally, an HAS client
| (4) inter-destination |     | multimedia |     | synchronization. |     |     |                    |       | T      |              | T            |
| --------------------- | --- | ---------- | --- | ---------------- | --- | --- | ------------------ | ----- | ------ | ------------ | ------------ |
|                       |     |            |     |                  |     |     | requests a segment | every | s time | units, where | s represents |
1) Multi-Client Competition/Stability Issues: Seufert thecontenttimedurationofeachsegment,andthesumofON
et al. [25] have shown that using a centralized management and OFF period durations equals T s. During the ON period,
controller can enhance the overall video quality, while the HAS client downloads the current segment and notes the
improving the viewer QoE. In that regard, a robust HAS achieved throughput value that will be later used in select-
scheme should achieve three main objectives: ing the appropriate bitrate for future segments. After that, the
• Stability: HAS clients should avoid frequent bitrate clienttemporarilybecomesidleintheOFFperiod(SeeFig.4).
switching, which leads to quality oscillations and video As shown in Fig. 5, when a set of HAS clients competes
stalls, which in turn can negatively affect QoE. for the available bandwidth, the per-segment activity periods
• Fairness: Multiple HAS clients competing for available (ON, OFF) of the steady state differ from client to client.
bandwidth should equally share network resources based Depending on the amount of overlap of the ON periods, the
on viewer-, content-, and device characteristics. The clients may at times considerably overestimate the available
fairness desired here does not often result in bandwidth- bandwidth. This potentially causes video instability, quality
fairness. oscillations, bitrate switches, buffer underruns, unfairness and
• High Utilization: While the clients attempt to be stable underutilization, which are collectively referred to as HAS
| and | fair, network |     | resources | should be | used | as efficiently | stability issues. |     |     |     |     |
| --- | ------------- | --- | --------- | --------- | ---- | -------------- | ----------------- | --- | --- | --- | --- |
as possible. Consider, for example, three HAS clients that share a bot-
A streaming session in general consists of two states, the tleneck link. Suppose that these three clients have reached the
T
buffer-filling state and the steady state [26]. The buffer-filling steady state and they request a new segment every s time
stateaimstofilltheplaybackbufferandreachacertainthresh- units. As illustrated in Fig. 5a, if the ON periods of these
old where the playback can be initiated or resumed. In this clients do not overlap during the current segment download,
state, the client requests the next segment as soon as the each client will overestimate the available bandwidth. This

566 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
Fig.5. IllustrationofthemaincauseofHASstabilityissuesbecauseofdifferentsegmentdownloadpatterns.
Fig.6. Differentinter-stream(ontheleft)andintra-stream(ontheright)scenecomplexitiesleadtodifferentdisplayqualitiesatthesameencodingbitrate
orviceversa.
wouldnotbethecaseiftheONperiodswerepartially(Fig.5b)
or fully (Fig. 5c) overlapping. Many HAS bandwidth estima-
tionalgorithmsusethecurrentsegmentdownloadspeedasan
input. Non-overlapping ON periods lead to overestimating the
fairshareofthebandwidth,andthus,clientsincorrectlyselect
a higher encoding bitrate for the next segment. Downloading
the next segment, which has a higher encoding bitrate, will
take longer, which will cause the initially non-overlapping
ON periods to eventually start overlapping. As the amount
of overlap increases, the clients will have lower bandwidth
estimations and start selecting segments that have a lower
encoding bitrate. These segments will take less time to down-
load, causing the amount of overlap among the ON periods
Fig.7. Illustrationofqualityversusbitratetrade-off.
to procedurally shorten, until the process reverts to its initial
situation. This cycle repeats itself, causing periodic up- and
downshifts in the selected bitrates, leading to unstable video indeliveringmultimediacontenttoviewers.Intraditionalnon-
quality, unfairness, and underutilization [26]–[28]. adaptive streaming, the client streams a video that is typically
2) Consistent-Quality Streaming: Research studies in the available in one bitrate at the server side. If the network con-
field of video quality analysis [29], [30] confirm that the cor- ditionsworsen,thedownloadratemayfallbelowtheplayback
relation between video bitrate and its perceptual quality is rate, which leads to buffer depletion and discontinuous play-
non-linear. Additionally, different video content types have back. With HAS, streamed videos show less buffering and
uniquecharacteristics,e.g.,highandlow-motionscenes,which higher bandwidth utilization compared to traditional stream-
result in different qualities. ing, since the video segments are transcoded into different
In the context of HAS, even if the available bandwidth bitrate levels, and segments are downloaded based on the cur-
stays constant, the delivered video quality may still vary, as rent network conditions and the playout buffer level. Fig. 8
illustrated in Fig. 6, due to unequal video scene complex- illustratestheapplicationcontrolloopofatypicalHASclient.
ity across content: inter-stream and intra-stream differences. This survey focuses on reviewing the adaptation algorithms,
Fig. 7 depicts the non-linear relationship between bitrate and i.e., the part responsible for selecting the next segment(s) to
theStructuralSIMilarityplus(SSIMplus)[31]perceptualqual- download. The application control loop also interacts with a
ity. Generally speaking, it is preferred to stream video with a lower-layercontrolloop(inthiscaseTCPcongestioncontrol),
consistentqualitythanataconsistentbitrate[32],[33],leading which can play a key role in determining the viewer QoE.
to a reduction in perceptual quality oscillations. In a recent survey by Seufert et al. [25], factors influenc-
3) QoEOptimizationandMeasurement: Thechangingcon- ing QoE are categorized as (a) perceptual, directly perceived
ditions of best-effort networks introduce numerous problems by the viewer, and (b) technical, indirectly affecting the

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 567
|     |     |     |     |     |     |     |     | video content |             | simultaneously, |      | while     | keeping  | the             | playback |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --------------- | ---- | --------- | -------- | --------------- | -------- |
|     |     |     |     |     |     |     |     | state of      | each client | the             | same | (playing, | paused). | Moreover,       | it       |
|     |     |     |     |     |     |     |     | becomes       | more        | challenging     | for  | HAS       | streams  | to synchronize, |          |
sinceeachclientadaptivelystreamsdependingontheircurrent
|     |     |     |     |     |     |     |     | network       | conditions.     | This   | problem | is      | called      | Inter-Destination |       |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------- | ------ | ------- | ------- | ----------- | ----------------- | ----- |
|     |     |     |     |     |     |     |     | Multimedia    | Synchronization |        |         | (IDMS). | Typically,  | IDMS              | solu- |
|     |     |     |     |     |     |     |     | tions involve | a               | master | node    | (either | a dedicated | master            | or a  |
peeramongthestreamingclientsinasession)towhichclients
|     |     |     |     |     |     |     |     | synchronize | their | playout | to. | One of | the | earliest | papers in |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | --- | ------ | --- | -------- | --------- |
Fig.8. TheapplicationcontrolloopinatypicalHASclient.
|     |     |     |     |     |     |     |     | this field  | was     | published | by Montagud |            | et al. | [46], | in which   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | ----------- | ---------- | ------ | ----- | ---------- |
|     |     |     |     |     |     |     |     | the authors | discuss | use       | cases       | where IDMS | and    | its   | schemes is |
|     |     |     |     |     |     |     |     | essential.  | Rainer  | et al.    | [47], [48]  | proposed   | an     | IDMS  | architec-  |
QoE. Perceptual factors include the video image quality, ture for DASH by using a distributed control scheme (DCS)
| initial delay, | stalling | duration |     | and frequency, |     | as well | as qual- |             |     |             |     |               |     |             |       |
| -------------- | -------- | -------- | --- | -------------- | --- | ------- | -------- | ----------- | --- | ----------- | --- | ------------- | --- | ----------- | ----- |
|                |          |          |     |                |     |         |          | where peers | can | communicate |     | and negotiate |     | a reference | play- |
ity switching amplitude and frequency. The impact of each back timestamp in each session. The MPD file was altered
of these factors differs depending on the users subjectivity. to include IDMS session objects that enabled session man-
Several studies have shown that most users consider initial agement. In another work [49], Rainer et al. provided a
delays less critical than stalling [34], [35], that longer stalling crowdsourced subjective evaluation to find an asynchronism
| periods | decrease | the | perceived | quality | [36], | and | that fre- |           |          |     |     |                   |     |           |      |
| ------- | -------- | --- | --------- | ------- | ----- | --- | --------- | --------- | -------- | --- | --- | ----------------- | --- | --------- | ---- |
|         |          |     |           |         |       |     |           | threshold | at which | QoE | was | not significantly |     | affected. | They |
quent changes in video quality have a negative impact on found that an asynchronism level of 400 ms was acceptable
the QoE [37]–[39]. The technical factors that influence QoE compared to the synchronous reference case. Synchronization
are the algorithms, parameters, and hardware/software used in in IDMS systems is crucial to the QoE. Dedicated QoE
the video streaming system. Specifically, such factors include models have to be developed that take the visual qual-
encoding parameters, video qualities and segment sizes at ity, user engagement and the synchronization accuracy
| the server | side, | the adaptation |     | logic, | device | capabilities | and | into account. |     |     |     |     |     |     |     |
| ---------- | ----- | -------------- | --- | ------ | ------ | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
contenttypeattheclientside,aswellastheadaptationparam- AfterdescribingthevariousfactorsthataffectInternetvideo
| eters and | the type | of  | environment |     | that the | client | resides in. |           |          |     |          |          |      |          |        |
| --------- | -------- | --- | ----------- | --- | -------- | ------ | ----------- | --------- | -------- | --- | -------- | -------- | ---- | -------- | ------ |
|           |          |     |             |     |          |        |             | streaming | systems, | we  | will now | continue | with | a survey | of the |
All of these factors are challenges to be taken into account existing bitrate adaptation schemes.
| for the | best trade-off |     | between | conflicting |     | goals | (e.g., less |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ------- | ----------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
stalling vs. high encoding bitrate) in order to achieve viewer III. BITRATEADAPTATIONSCHEMES
satisfaction.
|            |           |                 |             |          |              |               |             | We classify        |       | bitrate adaptation |            | schemes         | based   | on     | the entity |
| ---------- | --------- | --------------- | ----------- | -------- | ------------ | ------------- | ----------- | ------------------ | ----- | ------------------ | ---------- | --------------- | ------- | ------ | ---------- |
| One        | major     | challenge       | regarding   |          | video        | streaming     | is the      |                    |       |                    |            |                 |         |        |            |
|            |           |                 |             |          |              |               |             | of the system      | where | the                | logic      | is implemented: |         |        |            |
| lack of    | a unified | quantitative    |             | approach | to           | measure       | the QoE.    |                    |       |                    |            |                 |         |        |            |
|            |           |                 |             |          |              |               |             | • Client-based     |       | adaptation         | (Section   |                 | III-A), |        |            |
| Existing   | HAS       | solutions       | in industry |          | and academia | assess        | their       |                    |       |                    |            |                 |         |        |            |
|            |           |                 |             |          |              |               |             | • Server-based     |       | adaptation         |            | (Section        | III-B), |        |            |
| QoE based  | on        | three           | different   | metrics: |              | (1) Objective | met-        |                    |       |                    |            |                 |         |        |            |
|            |           |                 |             |          |              |               |             | • Network-assisted |       |                    | adaptation | (Section        | III-C), | taking | into       |
| rics, such | as Peak   | Signal-to-Noise |             |          | Ratio        | (PSNR)        | [40], [41], |                    |       |                    |            |                 |         |        |            |
accountexplicitinformationfromwithinthenetwork,and
| Structural  | SIMilarity |           | (SSIM | and    | SSIMplus) |                   | [31], [42], |          |            |             |          |         |         |             |     |
| ----------- | ---------- | --------- | ----- | ------ | --------- | ----------------- | ----------- | -------- | ---------- | ----------- | -------- | ------- | ------- | ----------- | --- |
|             |            |           |       |        |           |                   |             | • Hybrid | adaptation |             | (Section | III-D), | using   | information |     |
| Perceived   | Video      | Quality   |       | (PVQ)  | [43],     | and Statistically |             |          |            |             |          |         |         |             |     |
|             |            |           |       |        |           |                   |             | from     | any        | combination |          | of the  | client, | server(s),  | and |
| Indifferent | Quality    | Variation |       | (SIQV) | [44];     | (2)               | Subjective  |          |            |             |          |         |         |             |     |
network.
| metrics,   | such as        | Mean | Opinion      | Score    | (MOS); | or (3)      | Quality- |                    |     |          |      |               |     |                |     |
| ---------- | -------------- | ---- | ------------ | -------- | ------ | ----------- | -------- | ------------------ | --- | -------- | ---- | ------------- | --- | -------------- | --- |
|            |                |      |              |          |        |             |          | The taxonomy       |     | graph in | Fig. | 3 illustrates | our | classification | of  |
| of-Service | (QoS)-derived  |      | metrics      | such     | as     | the startup | delay,   |                    |     |          |      |               |     |                |     |
|            |                |      |              |          |        |             |          | bitrate adaptation |     | schemes. |      |               |     |                |     |
| average    | video bitrate, |      | quality      | switches | and    | rebuffering | events.  |                    |     |          |      |               |     |                |     |
| Achieving  | high           | QoE  | is difficult | because  |        | trying to   | optimize |                    |     |          |      |               |     |                |     |
each metric may result in conflicts. The complex relation- A. Client-Based Adaptation
ship between these measures and the interplay between the Inrelevantliterature,mostoftheproposedbitrateadaptation
adaptationlogicwithotherapplicationandnetwork-layerdeci- schemes reside at the client side, according to the specifica-
sionscansignificantlyaffecttheQoE.Balachandranetal.[45] tions in the DASH standard [50]. These schemes try to adapt
address these issues and propose a data-driven approach that to bandwidth variations by switching to an appropriate video
uses machine-learning to build a QoE prediction model. They bitrate according to one or more metrics such as the available
| showed | that it | could | enhance | the | user | engagement | when |            |          |        |       |      |      |         |          |
| ------ | ------- | ----- | ------- | --- | ---- | ---------- | ---- | ---------- | -------- | ------ | ----- | ---- | ---- | ------- | -------- |
|        |         |       |         |     |      |            |      | bandwidth, | playback | buffer | size, | etc. | Fig. | 9 shows | a simple |
applied in a CDN. modelofaclient-basedadaptation.Theclientusesoneormore
4) Inter-Destination Multimedia Synchronization: The metrics as input for its bitrate selection algorithm in order
ever-growingdevelopmentofsocialmultimediasitesischang- to choose the appropriate bitrate level for the next segment
ing the way people share content. Apart from online gaming, to be downloaded. These algorithms try to avoid stream-
photo sharing, and instant messaging, online communities are ing problems like video instability, quality oscillations, and
driftingtowardswatchingonlinevideostogetherinasynchro- buffer starvation, while improving viewer QoE. They strive
nizedmanner.Havingmultiplestreamingclientsdistributedin to achieve (i) minimal rebuffering events when the playback
differentgeographicallocationsposeschallengesindelivering buffer depletes, (ii) minimal startup delay especially in case

568 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
|     |     |     |     |     | the adaptive | k-push      | scheme      | proposes          |                  | to increase/decrease |               | k   |
| --- | --- | --- | --- | --- | ------------ | ----------- | ----------- | ----------------- | ---------------- | -------------------- | ------------- | --- |
|     |     |     |     |     | according    | to          | a bandwidth | increase/decrease |                  |                      | while keeping |     |
|     |     |     |     |     | in mind      | the overall | power       | consumption       |                  | in a                 | push cycle.   | In  |
|     |     |     |     |     | the same     | context,    | Miller      | et al.            | [58]             | proposed             | a low-latency |     |
|     |     |     |     |     | prediction   | based       | bitrate     | adaptation        |                  | scheme               | over wireless |     |
|     |     |     |     |     | access links | termed      | LOw-LatencY |                   | Prediction-based |                      | adaPta-       |     |
tion(LOLYPOP),whichleveragesTCPthroughputpredictions
|     |     |     |     |     | on multiple | time | scales | (i.e., 1 | to 10 | seconds) | to achieve | low |
| --- | --- | --- | --- | --- | ----------- | ---- | ------ | -------- | ----- | -------- | ---------- | --- |
Fig.9. Client-basedbitrateadaptation.
|     |     |     |     |     | latency     | and improve | viewer | QoE.      |             |      |                |     |
| --- | --- | --- | --- | --- | ----------- | ----------- | ------ | --------- | ----------- | ---- | -------------- | --- |
|     |     |     |     |     | For the     | specific    | case   | of mobile | clients     | that | are in motion, |     |
|     |     |     |     |     | the network | conditions  |        | are more  | fluctuating | with | respect        | to  |
of live video streaming, (iii) a high overall playback bitrate location and time. Several studies deploy a bandwidth lookup
levelwithrespecttonetworkresources,and(iv)minimalvideo service in a real-life mobile network in order to guide the
| quality oscillations, | which occur | due | to frequent | switching. |           |            |     |       |            |         |            |     |
| --------------------- | ----------- | --- | ----------- | ---------- | --------- | ---------- | --- | ----- | ---------- | ------- | ---------- | --- |
|                       |             |     |             |            | bandwidth | estimation |     | among | the mobile | clients | [59]–[63]. |     |
We further organize the client-based bitrate adaption into However, these frameworks take a spatial point of view of
five classes: (1) available bandwidth-based (Section III-A1), bandwidth fluctuations and pay little attention to the temporal
(2) playback buffer-based (Section III-A2), (3) proprietary factor.GeoStream [64] addresses thisissue and introduces the
solutions (Section III-A3), (4) mixed (Section III-A4), and use of geostatistics to estimate future bandwidth in unknown
| (5) Markov Decision | Process | (MDP)-based | (Section | III-A5). |     |     |     |     |     |     |     |     |
| ------------------- | ------- | ----------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
locations.
1) AvailableBandwidth-BasedAdaptation: Inthisintuitive In general, available bandwidth-based adaptation suffers
type of scheme, the client makes its representation decisions frompoorQoEduetoalackofareliablebandwidthestimation
based on the measured available network bandwidth, which methods, which results in frequent buffer underruns.
is usually calculated as the size of the fetched segment(s) 2) Playback Buffer-Based Adaptation: In this type of
divided by the transfer time. Liu et al. [51] proposed a bitrate scheme, the client uses the playout buffer occupancy as
adaptation algorithm that tries to detect bandwidth fluctua- a criterion to select the next segment bitrate during video
| tions and congestion | using | a smoothed | network | throughput | playback. |     |     |     |     |     |     |     |
| -------------------- | ----- | ---------- | ------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
based on the segment fetch time (SFT), which measures the Mueller et al. [65] were motivated by the limitation of
timestartingfromsendingtheHTTPGETrequesttoreceiving bandwidth-based adaptation when multiple clients competed
the last byte of the segment. Later, the authors extended their for the available bandwidth, specifically in the presence of
work in [52] to include both sequential and parallel segment cache servers. Therefore, the authors proposed a buffer-based
fetching methods in CDNs, by using a metric that compares bitrate adaptation scheme that combines the buffer size with a
the expected segment fetch time (ESFT) with the measured tool-setofclientmetricsforaccuraterateselectionandsmooth
SFT to determine if the selected segment bitrate matches switching. Huang et al. [66] proposed a set of buffer-based
the network capacity. A similar approach was employed by rate selection algorithms, named BBA that aim to maximize
Rainer et al. [14] where the bandwidth estimated for the next the average video quality and avoid unnecessary rebuffering
segment was calculated based on the bitrate observed for the events. However, BBA suffers from QoE degradation dur-
last segment downloaded and the estimated throughput that inglong-termbandwidthfluctuations.BufferOccupancybased
was calculated during the previous estimation. The initializa- Lyapunov Algorithm (BOLA) [67], on the other hand, is an
tionwasbasedonthebandwidthmeasuredwhendownloading onlinecontrolalgorithmthattreatsbitrateadaptationasautil-
the MPD. ity maximization problem. This utility is associated with the
Probe AND Adapt (PANDA) [53] estimates the available averagebitrateandrebufferingtime,whileadaptingtonetwork
bandwidth accurately and tries to eliminate the ON-OFF changestoaccountforbetterQoE.Theauthorsprovidestrong
steady state issue as well as reduce bitrate oscillations when theoretical proof that it is near optimal, design a QoE model
multiple clients share the same bottleneck link. The video that incorporates both the average playback quality and the
adaptation framework for DASH clients in LTE networks, rebufferingtime,andempiricallyshowitsefficiencyusingvar-
piStream [54], enables clients to estimate the available band- ious network traces. BOLA is the buffer-based algorithm that
width based on a resource monitor module that acts as a is implemented and available in the dash.js player.
physical-layer daemon. Andelin et al. [55] integrated SVC Sieber et al. [68], introduced an SVC-based adaptation
with DASH by proposing an algorithm that prefetches base algorithm called Bandwidth Independent Efficient Buffering
layersoffuturesegmentsordownloadsenhancementlayersfor (BIEB). BIEB maximizes video quality based on SVC pri-
existing segments using a bandwidth-sloping-based heuristic. ority while reducing the number of quality oscillations and
In live video streaming, the nature of the live experience avoiding stalls and frequent bitrate switching. BIEB main-
puts stringent constraints on the delay. DASH to Mobile tains a stable buffer occupancy before increasing the quality
(DASH2M) [56] by Xiao et al., is a strategy designed for (enhancement layers). However, BIEB does not take bitrate
mobile streaming clients using HTTP/2 server push and switches or stalls in the QoE model during peak times when
stream termination properties with the goal of enhancing dynamiccrosstrafficoccursinthenetworkintoconsideration.
the QoE as well as reducing the battery consumption of The decision by these algorithms which bitrate to select
the client. An extension of the authors’ previous work [57], largely depends on factors such as estimated network

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 569
throughput, buffer occupancy, and buffer capacity. Yet, these devices, Windows 10 Edge browser [74], and Android 3.0+
algorithms are not informed by a fundamental relationship devices [75].
between these factors and the chosen bitrate. Thus, they do Adobe Open Source Media Framework (OSMF) [10]:
not work consistently in all scenarios. To address this issue, OSMF is a free, open source software framework for robust
Yadav et al. [69] modeled a DASH client as an M/D/1/K adaptive video streaming over HTTP. It was implemented
queue referred to as a QUEuing Theory approach to DASH using ActionScript [76] by Adobe systems with the following
RateAdaptation(QUETRA),whichallowedthemtocalculate objectives: (1) simplify player development where develop-
the expected buffer occupancy given a bitrate choice, network ers could focus on improving the overall viewer experience,
throughput, and buffer capacity. Using this model, the authors (2)offerasetoffeaturesforthird-partyserviceslikerendering,
proposed a simple rate adaptation algorithm and evaluated advertising, and reporting, and (3) simplify third-party devel-
QUETRA under a diverse set of scenarios. They found that opmentsbyenablingecosystempartnerstofocusondelivering
despite its simplicity, QUETRA led to better QoE than the best-in-classservicesinsteadofplayerintegration.OSMFsup-
existing algorithms. ports both live and on-demand video streaming, progressive
In general, buffer-based adaptation schemes suffer from download, sequential and parallel compositions of video, and
many limitations including low overall QoE and instability it adapts to the network variations based on the available
issues, especially in the case of long-term bandwidth fluctua- bandwidth and device processing capabilities.
tions. SVC-based approaches also have limitations related to The three proprietary streaming solutions described above
the complexity of SVC encoding and decoding, processing show efficiency in terms of bitrate adaptation behavior of a
resources and overhead. Some alternative solutions have tried single client in response to bandwidth fluctuations. However,
to tackle these issues using multiple SVC streams, hierarchi- several studies [51], [77]–[80] have shown instability issues
cal encoding with a small number of enhancement layers, and when multiple clients competed for a bottleneck link in a
encoding overhead [70]. sharednetwork.Fromtheseexperimentsthefollowinginsights
3) Proprietary Solutions: In the past, we witnessed were deduced:
many proprietary adaptive streaming solutions and player • The bitrate adaptation heuristics provide suboptimal
implementations such as Microsoft’s Smooth Streaming bitrate decisions as they fail to adapt quickly to rapid
(MSS) [8], Apple’s HTTP Live Streaming (HLS) [9], Adobe’s bandwidth variations. Thus, clients suffer from buffer
HTTP Dynamic Streaming (HDS), and Open Source Media underruns, video instability, quality oscillations, and
Framework (OSMF) [10]. These solutions use different met- unnecessary bitrate switches.
rics in their bitrate adaptation process and are designed to • Theyarenotabletoensureafairviewerexperienceunder
satisfy various business requirements. some circumstances resulting in low efficiency and poor
Microsoft Smooth Streaming (MSS) [8]: In 2008, Microsoft per-viewer QoE.
launched IIS Media Services extension with a new adaptive • The MSS client outperforms the others, since it achieves
video streaming over HTTP feature called Smooth Streaming. the highest playback bitrate, and a low number of bitrate
It was designed to deliver HD videos to viewers. MSS switches during mobile video streaming sessions.
periodically detects network conditions to avoid bandwidth • Based on standard capabilities and features [80], DASH
fluctuations.Itusestheavailablebandwidth,playbackwindow offers nearly everything compared to these proprietary
resolution, and CPU load at the client side as the metrics for formats.
bitrate adaptation. During each streaming session, MSS opens 4) Mixed Adaptation: In this type of scheme, the client
two TCP connections with the server. The first one is used to makes its bitrate selection based on a combination of metrics
delivervideosegments,whilethesecondoneisusedforaudio, includingavailablebandwidth,bufferoccupancy,segmentsize
though the two TCP connections could interchange depend- and/or duration.
ing on the conditions. MSS showed its efficiency in many Other studies have looked at both the available bandwidth
sports events like the Beijing Summer Olympic Games 2008, and buffer occupancy in order to determine the bitrate of the
where TV broadcasters used MSS to provide live streaming next segment. Yin et al. [81] developed a control-theoretic
to 16 million clients [71]. framework that allows the understanding and exploration
Apple HTTP Live Streaming (HLS) [9], [72]: Due to the of the trade-offs between bandwidth-based and buffer-based
popularityofApple’s mobiledevices, HLSisthemostwidely adaptationalgorithmsunderdifferentnetworkbandwidthvari-
used adaptive video streaming system. Apple Inc. imple- ations. The authors designed a practical model-predictive
mented it as part of QuickTime [73] and on iOS devices such controller, FastMPC, that optimally combines both bandwidth
as the iPhone and the iPad. It is designed to support both live and buffer size predictions in order to find an appropriate
andon-demandstreamingbutspecificallytargetsmobileenvi- bitrate for the next segment and maximize QoE. A similar
ronments. The HLS client makes its bitrate decisions based approachwasalsostudiedin[82].Lietal.[32]formulatedthe
on network throughput and device capabilities (e.g., CPU, bitrateselectiondecisionasanoptimizationproblem,whereat
resolution, memory, etc.). In an attempt to better utilize the eachsegmentdownloadingstep,theproposedschemefindsan
available bandwidth, an HLS client can request many seg- appropriate bitrate that ensures a high and consistent quality
ments at the same time. Furthermore, HLS provides a flexible subject to bandwidth fluctuations and without risking a buffer
framework for media encryption. Currently, HLS is natively depletion. Similarly, Sobhani et al. [83] predicted available
supported in the Safari Web browser in both iOS and macOS bandwidth and buffer level using a fuzzy logic mechanism,

570 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
whichisusedtoselectasuitablebitrate.However,thesealgo- video, while minimizing the number of quality switches. For
rithms only ensure a consistent quality at each client without startup, SQUAD follows a conservative approach of fetching
taking the fairness and content type/properties into account more low-quality segments in order to alleviate any inaccura-
when many clients compete for the available bandwidth. cies in future bandwidth estimations which could result from
ELASTIC [84] is a fEedback Linearization Adaptive a single low-quality segment estimation. Later, the algorithm
STreamIng Controller, based on feedback control theory [85], uses the spectrum, which is the variation of the average seg-
that generates a long-lived TCP flow and avoids the ON-OFF ment bitrates, and the buffer level to choose the next segment
steady state behavior which leads to bandwidth overestima- bitrate. Havey et al. [92] designed a multi-path solution for
tions. ELASTIC was introduced to ensure bandwidth fairness rate adaptation in wireless networks. The authors avoided the
between competing clients based on network feedback assis- problems of TCP congestion control by implementing a sim-
tance,butwithouttakingtheviewerQoEintoconsideration.In ilar logic at the application layer. Parallel TCP streams have
addition, it ignores quality oscillations in its bitrate decisions. been proven to increase the throughput compared to single
Thus, both during bandwidth fluctuations and in fixed band- TCP streaming. However, this incurs extra request/response
width environments, ELASTIC may produce a high number overhead and imposes changes on the application stack.
of bitrate switches resulting in poor QoE. Other studies incorporate more metrics for bitrate selec-
Miller et al. [86] presented a bitrate adaptation algorithm tion like the current segment quality, size and download time.
that uses the current buffer occupancy level, estimated avail- SARA [93] is a Segment-Aware Rate Adaptation algorithm
able bandwidth, and average bitrate of the different bitrate thatisbasedonthesegmentsizevariation,theavailableband-
levelsfromtheMPDasmetricsinitsbitrateselection.Itaims width estimate, and the buffer occupancy. Since HTTP uses
to (i) accurately estimate the available bandwidth and avoid TCP,thethroughputofasegmentisdependentonthefilesize,
bandwidth overestimation, and (ii) maximize the bitrate while and thus, the authors propose to enhance the typical MPD file
minimizingstartupdelay,numberofstalls,qualityoscillations, to include the size of every segment. For each new segment
andplaybackinterruptions.Thealgorithmchangesitsbehavior download,theclientdecidesthenewsegmentqualitybasedon
based on the current buffer level. It can improve the fairness theestimatedbandwidth(whichisassessedusingthesegment
between competing clients, but it does not take any metric size) and the current status of the buffer.
of viewer satisfaction into account. Furthermore, in a shared ABMA+ [94] is a lightweight adaptation algorithm that
networkenvironment,clientscansufferfromvideoinstability, selects the highest segment representation based on the esti-
stallsandqualityoscillationsevenwhenclientsreachthehigh- mated probability of video rebuffering. It makes use of
est quality level. This is due to the lack of bitrate decisions buffer maps, which define the playout buffer capacity that
which consider viewer QoE. is required under certain conditions to satisfy a rebuffer-
Jiang et al. [87] studied the limitations of video players ing threshold and to avoid heavy online calculations. The
when a large number of clients shared the same network authors defined five QoE metrics to evaluate ABMA+ and
by providing an experimental study that identified the main compared it with BBA and Rate-Based Algorithm (RBA),
factors in bitrate selection. The authors introduced FESTIVE which are explained in detail in [94]. The authors showed
(Fair,EfficientandStableadapTIVEalgorithm),abitrateadap- that ABMA+ can efficiently adapt the video representations
tation algorithm that aims to improve efficiency, fairness and to the network conditions, while minimizing frequent qual-
stability. FESTIVE contains (a) a bandwidth estimator mod- ity switches. Bentaleb et al. [95] discussed the shortcomings
ule,(b)abitrateselectionandupdatemethodthattriestoavoid of the existing client-based schemes. To sidestep these draw-
unfairness of stateless bitrate selection2 by making the player backs, the authors leveraged a game theory [96] framework
stateful, and (c) a randomized scheduler that incorporates the and developed the GTA (Game Theory Adaptive bitrate)
buffersizetoschedulethedownloadofthenextsegment. For scheme. GTA uses a cooperative game in coalition formand
the same purpose, Throughput-Friendly DASH TFDASH [88] then formulates the bitrate selection problem as a bargaining
uses a logarithmic-increase-multiplicative-decrease (LIMD) process and consensus mechanism. Thus, the DASH clients
based bandwidth probing algorithm to estimate the avail- can create an agreement among themselves and achieve their
able bandwidth and a dual-threshold buffer for the bitrate QoE objectives. GTA improves the viewer QoE and video
adaptation. stability without increasing the stall rate or startup delay.
Tian and Liu [89] offered algorithms that aim to balance 5) MDP-Based Adaptation: In Markov Decision Process
bandwidthutilizationandsmoothnessinDASHinbothsingle- (MDP)-based adaptation, the video streaming process is for-
and multi-CDN scenarios. Using the buffered video time as mulated as a finite MDP to be able to make adaptation deci-
a feedback signal, the client is able to adapt the video rate sions under fluctuating network conditions. Xing et al. [97]
accordingtotheavailablebandwidth,whichisestimatedusing proposed a real-time best-action search algorithm over
the support vector regress (SVR) [90] algorithm. Spectrum- multiple access networks that aims to produce smooth and
based QUality ADaptation (SQUAD) [91] is a lightweight high-qualityvideoplaybacks.TheauthorsusedbothBluetooth
bitrate adaptation algorithm that uses the available bandwidth and WiFi links to simultaneously download video segments.
and buffer information to increase the average bitrate of a In each state, the MDP was formulated so the rate adapta-
tion agent takes the buffer level, SVC layer index, Bluetooth
2Statelessbitrateselectionreferstoselectingthehighestbitratelowerthan traffic, available bandwidth, and the index of each segment
theavailablebandwidth. fetchedas inputs. The reward function is designed to consider

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 571
the average playback quality, interruption rate, and playback
smoothness. However, this scheme shows limitations during
user mobility which negatively affect the viewer QoE. The
mobility problem was addressed by Bokani et al. [98] who
modeled the bitrate adaptation logic as an MDP problem
in vehicular environments. A three-variant of Reinforcement
Learning (RL)-based algorithms were introduced. These algo-
rithms take advantage of the historical bandwidth samples to
build an accurate bandwidth estimation model.
Another noteworthy work is Petrangeli et al. [99]. The Fig.10. Server-basedbitrateadaptation.
authorstackledtheproblemofQoEandfairnesswhenmultiple
clients compete at a bottleneck link and they proposed a
multi-agent RL-based bitrate adaptation scheme that uses a performance in terms of stalls, and thus, ensure an acceptable
centralmanagerinchargeofcollectingQoEstatistics(segment level of viewer QoE. However, they may suffer from instabil-
bitrate) and coordination between the competing clients. The ity,unfairness,andunderutilizationwhenthenumberofclients
developedalgorithmensuresafairQoEdistributionamongthe increases, probably because such factors are not taken into
competing clients and improves viewer QoE, while avoiding account in the MDP models and due to clients’ decentralized
suboptimal decisions. However, this model does not con- ON-OFF patterns.
sider stalls and quality switches which can lead to rebuffering
events.Unlike[99],Chiariottietal.[100]developedanMDP- B. Server-Based Adaptation
based online bitrate adaption algorithm for DASH clients that
Server-based schemes use a bitrate shaping method at the
aimed to select the optimal representation, maximizing the
server side and do not require any cooperation from the client
long-term expected reward (QoE). This reward function was
(see Fig. 10). Thus, the switching between the bitrates is
calculatedfromacombinationofqualityoscillations,segment
implicitly controlled by the bitrate shaper. The client still
quality, and stalls experienced by the client. The authors used
makes its own decisions, but the decisions are more or less
RLtogatherinformationonthenetworkenvironmentthrough
determined by the shaping method on the server.
experience to approach an optimal solution. To avoid slow
Traffic shaping methods have been deployed
convergence and suboptimal solutions caused during the RL
in [106] and [107] where the authors analyzed instabil-
process, the authors exploited a parallel learning technique.
ity and unfairness issues in the presence of multiple HAS
Zhou et al. [101] tackled a similar problem by propos-
players competing for the available bandwidth. These studies
ing mDASH to improve viewer satisfaction during long-term
proposed a traffic shaping method that can be deployed at a
bandwidth variations. The authors first formulated the bitrate
home gateway to improve fairness, stability and convergence
adaptation logic as an MDP optimization problem where the
delay [107], and to eliminate the OFF periods during the
buffer size, bandwidth conditions, and bitrate stability were
steady states (the root cause of the instability problem) [106].
taken as Markov state variables. They subsequently solved
Toimprovetheliveexperience,Dettietal.[108]proposeda
this problem by proposing a low-complexity greedy subop-
tracker-assistedadaptation strategyinthepresenceofnetwork
timal algorithm. Compared to previous MDP-based studies,
caches. The proposed architecture consists of clients com-
Pensieve[102]andDeepQ-LearningDASH(D-DASH)[103]
municating with a server through a shared proxy and a
were proposed to improve accuracy and speed of bitrate deci-
server having a tracker functionality that manages the clients’
sion estimations using Deep Reinforcement Learning (Deep
statuses and helps them share knowledge about their sta-
RL) [104]. Pensieve [102]3 is a framework that is built based
tuses. De Cicco et al. [109] proposed a feedback control
on observations collected by DASH clients (i.e., throughput
theory-based algorithm called Quality Adaptation Controller
estimation and buffer occupancy) across large video stream-
(QAC). QAC aims to control the size of the server send-
ing experiments. It does not rely on pre-programmed models
ing buffer in order to adjust and select the most appropriate
or assumptions about the environment, but, in fact, gradually
bitrate level for each DASH player. It aims to maintain the
learns the best policy for bitrate decisions through observa-
playback buffer occupancy of each player as stable as pos-
tion and experience. D-DASH [103] combines deep learning
sible and to match bitrate level decisions with the available
and reinforcement learning mechanisms to improve the QoE
bandwidth. Bruneau-Queyreix et al. [110] developed the MS-
forDASH,andachievesagoodtrade-offbetweenpolicyopti-
Stream system, a multiple-source adaptive streaming solution
mality and convergence speed during the decision process. In
toimproveviewer QoE,wheretheclientfetchesthesegments
particular, it uses mixed learning architectures including feed-
(divided into a set of subsegments and stored in the servers)
forward and recurrent deep neural networks with advanced
from multiple MS-Stream servers.
strategies.Bothsolutions[102],[103]performadequatelyand
The server-based bitrate adaptation schemes produce high
present the benefits of incorporating Deep RL with ABR
overhead on the server side with a high complexity,4 espe-
heuristics in the bitrate decision process. The proposed MDP-
cially when the number of clients increases. These schemes
based schemes yield a significant improvement in the overall
4Theserverneedstostoreandmaintaintheinformationforeachclientto
3ApensieveisadeviceusedinHarryPotter[105]toreviewmemories. performbitrateadaptation.

572 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
|     |     |     |     |     |     |     |     | HTTP and    | HTTPS           | traffic.     | It consists    | of                  | an event-based |              | buffer  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ------------ | -------------- | ------------------- | -------------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | emulator    | module          | and          | an automated   | training            |                | online       | classi- |
|     |     |     |     |     |     |     |     | fier that   | are responsible |              | for accurately | tracking/predicting |                |              | the     |
|     |     |     |     |     |     |     |     | client’s    | buffer          | conditions   | and TCP/IP     | packet-level        |                | traffic      | clas-   |
|     |     |     |     |     |     |     |     | sification, | respectively.   |              | For the        | same                | aim and        | inspired     | by      |
|     |     |     |     |     |     |     |     | the Network | Utility         | Maximization |                | (NUM)               | [115]          | framework,   |         |
|     |     |     |     |     |     |     |     | D’Aronco    | et              | al. [116]    | proposed       | a distributed       |                | price-based, |         |
Fig.11. Network-assistedbitrateadaptation. network-assisted HAS system for multiple concurrent HAS
|     |     |     |     |     |     |     |     | clients sharing |     | a common   | bottleneck. | The    | proposed   |     | solution |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ----------- | ------ | ---------- | --- | -------- |
|     |     |     |     |     |     |     |     | introduces      | the | definition | of a price  | (i.e., | a function | of  | the seg- |
also need modifications to the MPD [108] or a custom server ment download times that are captured by the HAS clients),
softwaretoimplementthebitrateadaptationlogic[106]–[109].
|                    |               |            |                |            |              |                   |          | which is      | inspired   | by a            | congestion  | control             | algorithm.  |              | Then,  |
| ------------------ | ------------- | ---------- | -------------- | ---------- | ------------ | ----------------- | -------- | ------------- | ---------- | --------------- | ----------- | ------------------- | ----------- | ------------ | ------ |
| This may           | be perceived  |            | as a violation |            | of the       | DASH              | standard |               |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | using the     | price      | information,    | a           | central coordinator |             | assists      | the    |
| design principles, |               | namely     | that           | the server |              | should be         | a stan-  |               |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | clients in    | their      | decisions       | to maximize | overall             | user        | satisfaction |        |
| dard HTTP          | server,       | and        | that the       | bitrate    | adaptation   | algorithm         |          |               |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | and QoE       | fairness.  |                 |             |                     |             |              |        |
| should,            | consequently, |            | run at         | the client | side.        | The server        | and      |               |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | To alleviate  |            | overhead-caused |             | network             | performance |              | degra- |
| network-assistance |               | approach   | [16],          | [111]      | can          | be an alternative |          |               |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | dation,       | Petrangeli | et al.          | [117]       | tried to            | avoid       | fairness     | issues |
| solution,          | where         | in-network | entities       | and        | servers      | aid the           | client   |               |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | when multiple |            | HAS clients     | consume     | video               | at          | the same     | time   |
| in its bitrate     | decisions.    |            | This approach  |            | is discussed | in                | detail   | in            |            |                 |             |                     |             |              |        |
|                    |               |            |                |            |              |                   |          | and compete   |            | for shared      | network     | resources           | by          | proposing    | a      |
Section III-D2.
|                     |     |            |     |     |     |     |     | QoE-driven | in-network |            | bitrate  | adaptation | algorithm  |             | named |
| ------------------- | --- | ---------- | --- | --- | --- | --- | --- | ---------- | ---------- | ---------- | -------- | ---------- | ---------- | ----------- | ----- |
|                     |     |            |     |     |     |     |     | FINEAS     | (Fair      | In-Network | Enhanced | Adaptive   |            | Streaming). | To    |
| C. Network-Assisted |     | Adaptation |     |     |     |     |     |            |            |            |          |            |            |             |       |
|                     |     |            |     |     |     |     |     | achieve    | fairness,  | FINEAS     | uses     | in-network | components |             | such  |
The network-assisted approach depicted in Fig. 11 allows as proxies that offer information about network conditions
the HAS clients to take in-network decisions during the like currently available bandwidthand suggestions about the
bitrate adaptation process into consideration. This happens by best bitrate. Each client may use these suggestions as a cri-
collecting measurements about the network conditionswhile terion for bitrate selection. FINEAS shows good performance
informing the clients on the suitable bitrates to be selected. in homogeneous systems but in the real world, heterogeneous
The in-network process needs a special component (e.g., devices with different characteristics exist. Thus, sharing the
agent/proxy deployed in the network) to monitor the network bandwidth equally among competing clients may result in
status and conditions. It offers network-level information that high QoE on some devices but low QoE on others. In [118],
allows the HAS clients to efficiently use network resources. Network Optimization for Video Adaptation (NOVA) was
QoE-aware DASH (QDASH) [112] is a proxy between the proposed to fairly maximize viewer QoE while avoiding
clients and the streaming server that aims to avoid video unnecessarybitrateswitchinginaheterogeneousenvironment.
oscillations by ensuring a gradual change in bitrate levels The authors formulated the multi-client competition issue as
usingintegratedintermediatelevels,whichcanleadtoabetter an optimization problem subject to buffer occupancy, network
QoE. QDASH consists of a QDASH-abw module to mea- conditions and delivery cost. Thereafter, NOVA tries to find
sure the bandwidth and a QDASH-qoe module that assists theoptimalbitrateforeachclient.NOVAconsistsoftwomain
the client in choosing a suitable bitrate that can support the elements: bandwidth allocation and quality adaptation. While
current network conditions and buffer occupancy. However, NOVA achieves good QoE compared to traditional DASH
it generates significant overhead in the network, especially systems, the efficiency of the proposed architecture relies on
with increasing client numbers. This overhead may eventu- strong statistical assumptions such as stationary ergodicity,
ally lead to network congestion in itself, resulting in a low whichmaynegatively impacttheconvergence timeduringthe
QoE. Similarly, Bouten et al. [113] tackled the problem of search for optimal decisions [119].
multiple DASH clients competing for the available bandwidth Many studies [120]–[127] have proposed bitrate adapta-
byproposingaQoE-drivenin-networkoptimizationsystemfor tion schemes to improve viewer QoE in cellular networks.
adaptive video streaming. The proposed system consists of a AVIS [120] is a network-based radio resource allocation
set of agents deployed along the path between the clients and framework designed for adaptive video flows in cellular
streaming server, where they play the role of proxies. These networks. It can optimally allocate resources for each client
networkagentsperiodicallymeasureandmonitortheavailable (separating DASH flows from others) and ensure fairness and
bandwidth along the path using packet sampling techniques stability between them while maintaining high resource uti-
and solve an optimization problem to determine the optimal lization. Similarly, Kleinrouweler et al. [122] installed HTTP
bitrate for the next segments to be downloaded. This infor- proxies at the network gateways that evenly allocated the
mation is then sent to the clients. However, similar to [112], available bandwidth between the streaming clients. The proxy
it can generate significant overhead and is not resilient to re-writes client requests that demand a bitrate higher than the
agent failures. To reduce buffer underrun events and improve onedesignatedbytheproxy,andalsoaddsanHTTPheaderto
the client’s viewing experience, Krishnamoorthi et al. [114] theresponseinformingtheclientofthechange.Thestreaming
presented BUFFEST, a classification framework for real- process was modeled as an MDP, where each state repre-
time prediction of the client’s buffer conditions from both sents the number of active clients and the transitions between

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 573
the states are linked to starting and stopping the players. To performing traffic classification, helping clients in their deci-
account for stability, the number of switches relates to the sions, and applying resource allocation according to the Q-R
frequency of transitions between the MDP states. In contrast, function. Motivated by the fact that TCP connections are
ElEssailietal.[121]developedaQoEoptimizerandresource well-modeled as traversing a piecewise-stationary sequence
manager framework that can dynamically find the optimal of network states [130], Akhtar et al. [131] designed Oboe
bitrateforasubjecttowirelesschannel conditions,bufferlev- which allows the automatic tuning of configuration param-
els, and achievable QoE. It allocates the required bandwidth eters to different network conditions for an ABR scheme.
for each client based on its QoE unlike [120], [122] where Consequently, these configuration parameters are applied at
all clients receive an equal share of the allocated bandwidth, run-time to match the current network state. The proposed
which does not necessarily mean that all the clients enjoy a system significantly improves the bitrate decision of client-
good experience due to intrinsic differences across the device basedadaptationschemeslikeBOLA[67]andFastMPC[81],
capabilities. and it offers a 24% on average better viewer QoE compared
In the same context, the Rebuffering Aware Gradient to Pensieve [102].
Algorithm (RAGA) [123] is a cross-layer buffer-aware wire- Other approaches incorporate OpenFlow-enabled solutions
less resource allocation algorithm that considers only the with HAS. Georgopoulos et al. [132] proposed an OpenFlow-
playback buffer size during the bitrate selection process. It based in-network caching service, named OpenCache, that
makes use of DASH’s standardized user feedback from the leverages software defined networking (SDN) to optimize
buffer, both its level and rate of level changes. The same video-on-demand DASH streams. OpenCache uses SDN to
authors later proposed a new architecture to enhance the provide cache-as-a-service (CaaS) for media content and
QoE in LTE networks [124]. The architecture consists of aims to alleviate last mile scalability issues by pushing the
a Video Aware Controller (VAC) at the network core that DASH segments as close to the client as possible without
acts as a central intelligence unit for translating the video requiring any modifications in the delivery method, and to
qualities and buffer levels into QoS parameters. The authors improve network resource utilization and QoE for the view-
also proposed a new algorithm that computes the dynamic ers. Additionally, it can provide network and DASH clients’
Maximum Bit Rate (dynamic-MBR) for each client based on measurements that help CDN providers to enhance content
its buffer level obtained from the feedback. Han et al. [125] placement and delivery mechanisms. Cofano et al. [133]
proposed Multi-path DASH (MP-DASH), a multi-path frame- investigated video quality fairness (VQF) for cases in which
work with awareness of the network interface preferences of multiple heterogeneous adaptive streaming players share the
the clients. It aims to improve multi-path TCP (MPTCP) to same bottleneck link. The authors proposed a Video Control
support DASH considering the user network interface prefer- Plane (VCP) that enforces a video quality management policy
ences, thus enhancing the efficiency of video delivery without to ensure fairness. VCP was implemented on top of an SDN
sacrificingviewerQoE.MP-DASHconsistsoftwomaincom- controller as a network controller application and consists of
ponents including the MP-DASH scheduler and the video threenetwork-assistedstreamingapproaches:bandwidthreser-
adapter. The scheduler takes user interface preferences, seg- vation, bitrate guidance and hybrid between bitrate guidance,
ment size and its delivery time from the DASH client into andbandwidthreservation.Bhatetal.[134]designedanSDN-
consideration. Based on this, it decides the best way to fetch assisted architecture for HAS systems, termed SABR. This
the segment over multiple paths. The video adapter is a method leverages SDN capabilities to assistand manage HAS
lightweightadd-ontoexistingclient-basedadaptationschemes players and it collects various information such as available
to be multi-path friendlier, being responsible for handling the bandwidth and client states to guide player bitrate decisions.
interaction between the bitrate adaptation scheme, and the Seema et al. [135] developed a DASH-based video platform
MP-DASH scheduler. for miniaturized devices including sensors, called Wireless
To reduce video instability, QoE unfairness and stalls in Video Sensor Node Platform DASH (WVSNP-DASH). The
cellular networks, Yan et al. [126] designed Prius as a frame- proposedplatformusesanalternativeapproachtosegmentthe
work that consists of a hybrid edge cloud and a client-based video to be convenient for miniaturized wireless devices and
adaptation scheme. Similarly, Zahran et al. [127] proposed sensors.Itutilizesaspecificnamingsyntax(basedonasimpli-
a Stall-aware Pacing (SAP) traffic management solution for fied Backus-Naur Form [136]) for video segments such that
DASH clients. It aims to reduce video stalls while main- each segment is an independently playable file that embeds
taining a consistent QoE when multiple DASH clients with essential metadata required for video playout in its name. In
diverse channel conditions compete for resources. SAP lever- this way, the client can play the segment without requiring
ages both network and client state information to optimize to download the manifest file and initial segments. WVSNP-
theper-playerQoE.LeveragingMachineLearning(ML)[128] DASH is designed based on core elements of HTML5 (e.g.,
mechanisms, De Grazia et al. [129] developed a multi-stage HTML5 File System). Also, it can encapsulate any con-
MLcognitiveapproachforDASHwhenmultipleclientscom- tainer, codec and DRM that are supported by a Web browser.
pete for the available bandwidth in a shared channel. The However, this paper does not analyze the overhead introduced
proposed solution incorporates unsupervised and supervised by WVSNP-DASH, i.e., the new data embedded in each seg-
ML to comprehend the Quality-Rate (Q-R) relationship. The ment which may significantly impact the network efficiency
authors deployed a cognitive HTTP proxy (CHP) that was andlifetime.ForbitrateadaptationschemesoverInformation-
responsibleforcontrollingthevideotraffictowardstheclients, Centric Networking (ICN), Lederer et al. [137] investigated

574 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
the possibilities of integrating HAS over ICN. The authors HTTP REST API
highlightedusecasesandscenarios,namelyNetflix-likevideo
|            |              |       |       |       |          |           |     | HAS Server | HHAASS  CClliieennttss |     |     |
| ---------- | ------------ | ----- | ----- | ----- | -------- | --------- | --- | ---------- | ---------------------- | --- | --- |
| streaming, | peer-to-peer | (P2P) | uses, | video | sharing, | and IPTV. |     |            |                        |     |     |
Application
|     |     |     |     |     |     |     | Layer |     |     |     | A p p l i c a t io n  |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --------------------- |
Additionally,theauthorspresentedavailabletoolsandtestbeds C o n t r o ll e rs
| toevaluate | HAS over | ICN,and         | highlighted |     | several  | challenges |     |     |     |     |     |
| ---------- | -------- | --------------- | ----------- | --- | -------- | ---------- | --- | --- | --- | --- | --- |
| and open   | issues.  | Further details | of          | the | HAS over | ICN archi- |     |     |     |     |     |
Policies
| tecture | can be found | in RFC | 7933 | [138]. | The | performance |     |     |     |     |     |
| ------- | ------------ | ------ | ---- | ------ | --- | ----------- | --- | --- | --- | --- | --- |
of DASH over ICN is examined by Rainer et al. [139]. The SDN Network  SDN Controller
Management
| authors | analyzed the | performance |     | gap between |     | different ICN- |     |     |     |     |     |
| ------- | ------------ | ----------- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- |
based forwarding strategies with their theoretical optimum at OpenFlow
thenetworklevelandvariousclient-basedadaptationschemes
Network Layer and
| at the application |     | level. They | derived | the | theoretical | optimum |     |     |     |     |     |
| ------------------ | --- | ----------- | ------- | --- | ----------- | ------- | --- | --- | --- | --- | --- |
Forwarding Devices
| bound by        | formulating     | the concurrent |     | streaming    |     | clients in ICN |     |     |     |     |     |
| --------------- | --------------- | -------------- | --- | ------------ | --- | -------------- | --- | --- | --- | --- | --- |
| as a fractional | Multi-Commodity |                |     | Flow Problem |     | (MCFP) with    |     |     |     |     |     |
Fig.12. ArchitectureforSDN-basedbitrateadaptation.
| and without | caching, | showing | that | HAS | performance | can be |     |     |     |     |     |
| ----------- | -------- | ------- | ---- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
improvedbybenefitingfromICNmulti-pathandcachingcapa-
bilities.Petrangelietal.[140]focusedoncombiningHASand 1) SDN-Based Adaptation: Two key insights of integrating
SVC over ICN networks. They used SVC mainly for the fol- SDN [143], [144] within an adaptive video streaming system
| lowing | reasons: (i) | SVC allows | to  | fully | exploit | the benefits of | are as follows: |     |     |     |     |
| ------ | ------------ | ---------- | --- | ----- | ------- | --------------- | --------------- | --- | --- | --- | --- |
ICN while avoiding suboptimal bitrate selections, (ii) it helps • SDN allows for network resource control and moni-
the clients to mitigate bandwidth overestimation, and (iii) the toring capabilitiesand thus simplifying network resource
layered structure of SVC enables the benefits from ICN’s programming and deployment.
multi-path capabilities Xu et al. [141] proposed EcoMD, an • Pure client-driven bitrate adaptation algorithms show
ICN-based cost-efficient multimedia content delivery solution their limitations when a set of DASH clients compete
forvehicularadhocnetworks(VANETs)toreducethecostof in a shared network environment and when the network
video delivery in highly dynamic VANETs. The authors first size grows, resulting in issues such as video instabil-
analyzed two essential factors, namely content mobility and ity, quality oscillations, buffer underruns, unfairness, and
supply-demand balance. Then they formulated the cost asso- underutilization.Theseissuesarelargelyduetoalackof
ciated with video delivery as a Mixed Integer Programming coordination among the clients, which could be ensured
(MIP) optimization problem. Finally, they proposed three by a central mechanism that has the global network view
adaptiveheuristicsolutionstosolvetheoptimizationproblem: in a manageable network environment (e.g., a last mile
(1) priority-based path selection, (2) least-required sources likecampusnetwork).Withacentralcoordinatorandthe
maintaining, and (3) on-demand in-path caching enhance- integrationofsuchcoordinationinformation,theseissues
ment. Similarly, Detti et al. [142] proposed an ICN-based can be avoided and viewer satisfaction can be improved.
P2P streaming application for live HAS systems over cellular Fig. 12 depicts SDN-based bitrate adaptation, where the
networks. The main insight of this work is to show the pos- network resources and competing clients are controlled and
sibility of exploiting ICN capabilities to provide a good HAS monitored by a central component in the control plane, more
service and achieve a simplified deployment process. In the precisely the SDN controller.
application, the HAS clients (or peers) construct a P2P one- Georgopoulos et al. [145] proposed an SDN-assisted QoE
hop mesh network that enables cooperative downloading of Fairness Framework (QFF), which sought to optimize QoE
the same live video. These clients use their cellular network by ensuring video quality fairness among multiple competing
interfaces to connect to the HAS server and are connected to DASHclientsinthelastmile.Theproposedframeworklever-
each other through proximity WiFi channels. ages OpenFlow to monitor the quality of the video streams
In general, the presented ICN-based solutions use heuristic and allocate/manage resources in the network.
information (collected from the requested content) to perform The same authors later proposed an improvement of QFF
the caching decision by a special node. Some of these solu- by introducing the SDN-based in-network QoE measurement
tions produce a large number of redundant copies, and thus, framework IQMF [146], which acts as a proxy and aims to
impact storage resources. Providing efficient content manage- provide per-client transparent monitoring of QoE during the
ment,ensuringhighcacheperformance,anddesigningarobust videosession,andsubsequentlyoffersitsfeedbacktonetwork
HAS delivery system over ICN are still open issues. and content providers through a well defined API. IQMF was
|           |            |     |     |     |     |     | proposed        | due to the fact | that traditional network-level |       | metrics     |
| --------- | ---------- | --- | --- | --- | --- | --- | --------------- | --------------- | ------------------------------ | ----- | ----------- |
|           |            |     |     |     |     |     | like bandwidth, | packet          | loss, jitter, and end-to-end   |       | delay could |
| D. Hybrid | Adaptation |     |     |     |     |     |                 |                 |                                |       |             |
|           |            |     |     |     |     |     | not provide     | an estimation   | of video quality.              | Both, | QFF and     |
In hybrid bitrate adaptation, many networking entities col- IQMF take only two metrics into account, device resolution
laboratetogetherandcollectusefulinformationaboutnetwork and available bandwidth, without considering the buffer level.
conditions that can help HAS clients in their bitrate selec- Thus, clients may be subject to buffer starvation.
tion. This type of technique consists of SDN-based and Nam et al. [147] proposed an SDN-based application that
server-and-network-assisted adaptations. aims to manage network resources while monitoring network

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 575
conditions and client feedback (QoE metrics), when multiple affect the ABR decisions, namely: (i) the difficulty to sup-
clients compete for a shared capacity. The SDN application port large-scale deployments of HAS players, (ii) non-trivial
dynamically reroutes the video flows using the Multiprotocol communication overhead, and (iii) limited support for system
Label Switching (MPLS) traffic engineering mechanism over heterogeneity. The latter is an online reinforcement learn-
SDN when QoE requirements are violated (during buffer ing (RL) QoE optimization framework for SDN-enabled HAS
underrun events, for instance). Such an approach can improve systems. The proposed framework consists of three phases.
the overall QoE by selecting the best path to the server. First, it groups the HAS players into a set of disjoint clusters
However, the authors do not describe the time effect of based on a perceptual quality index. Second, it formulates the
dynamic path changes during the streaming session. This bitrate selection as a Partially Observable Markov Decision
problemwasaddressedbyWangetal.[148]throughthedevel- Process. Third, it implements an online Q-learning algorithm
opment of GENI Cinema (GC), an SDN-assisted service for tosolvetheQoEoptimizationproblemandfindinparallelthe
live video streaming. GC aims to provide online live educa- optimal bitrate decision for each cluster.
tionalvideostreamingamongmanycampusesusingtheGENI To improve the viewer QoE in the context of HAS in
SDN-based network resource infrastructure. Steaming clients hybridfibercoax(HFC)networkenvironments,anSDN-based
canuploadand/orwatchonlinevideosviaapublicsharedWeb bandwidth broker solution [154] termed BMS (Bandwidth
portal, and the GC service is able to monitor and manage the Management Solution) was developed. BMS formulates the
video flows and resources over one or multiple routes dynam- bitrate decisions as a convex optimization problem, which
ically using SDN features. The GC service has been shown to reliesonaconcavenetworkutilitymaximization(NUM)func-
provide scalable, stable, and fair live video streaming. tion.BMSisproposedtomeetper-sessionandper-groupQoE
Petrangeli et al. [149] proposed an SDN-based frame- objectives. Thus, BMS is able to avoid common HAS issues
work that aimed to reduce video freezes caused by sudden like video instability, unfair and unequal quality distribution,
bandwidth fluctuation by applying a prioritization technique and network resource underutilization.
during the segment delivery process. The SDN controller Lai et al. [155] proposed an SDN-based manager in 5G
represents the main component of the proposed framework, OpenFlow-enabled wireless networks for HLS services. The
where it is responsible to collect the network status infor- manager aims to allocate a suitable on-demand network
mation such as bandwidth changes, latency, and statuses of resource (e.g., bandwidth) that improves the QoE taking into
the HAS clients. Based on this information, the controller consideration the media segment perceptual quality and client
decides whether a segment has to be prioritized or not in buffer size during bitrate selection. However, the authors
order to alleviate video freezing at the client. In the same consider neither the radio characteristics that exhibit sudden
context, Kleinrouweler et al. [150] described an SDN-based bandwidthfluctuationsnorthehandoversituationsduetouser
network architecture for DASH that aims to ensure stable mobility.
and high quality video delivery, while avoiding the mismatch All theses studies as well as C3 [156], CFA [157],
between the TCP mechanism and the dynamic bursty nature CS2P [158], Pytheas [159] share a common characteristic,
of DASH traffic. The proposed architecture consists of three which is that there exists a central controller to control,
layers: SDN network application controllers, SDN network manage and monitor HAS traffic. However, these solutions
management, and programmable network infrastructure. The do not scale well and support system heterogeneity. They
SDN network application helps the set of competing DASH also generate additional overhead that can affect the network
clients in their bitrate selection, while the SDN network man- performance.
agement uses a dynamic queue-based mechanism for QoS 2) Server and Network-Assisted Adaptation: Thomas
provisioning. However, the proposed architecture does not et al. [16], [111], [160] were motivated by the fact that
consider device heterogeneity, which is important for deter- the client-driven approach of DASH left less control to
miningthefairshareofavailablebandwidthandQoEfairness. the network and service providers, which introduced new
To address these issues, Bentaleb et al. [151] proposed a new challenges for them in service differentiation, and proposed
end-to-end SDN-based resource allocation and management the Server and Network-assisted DASH (SAND) architec-
architecture for HAScalled SDNDASH. The proposed archi- ture. SAND is a control plane that offers asynchronous
tecture leverages SDN capabilities to manage and allocate client-to-network, network-to-client, and network-to-network
networkresourcesforeachclientbasedonitsQoE.Itconsists communications. SAND allows to collect metrics and status
of the three layers application, control, and network, as well information from different entities in the system including
as six core entities within those layers: DASH server, DASH the clients and to send feedback to the clients and DASH-
clients,SDN-basedexternalapplication,SDNcontroller,SDN- aware Network Elements (DANE) including the servers,
basedinternalapplication,andforwardingdevices.SDNDASH caches and other network entities along the media path. This
formulates the QoE maximization and optimal decision for feedback is used by the clients to assist in the bitrate adap-
bothbitrateandnetworkresourceallocationasamaximization tation and by the DANEs to improve media delivery. To
optimization problem, leading to significant improvements in enable the communication between the clients and DANEs,
per-client QoE while avoiding HAS stability issues. For the SAND defines the following interfaces to carry various types
same context, SDNHAS [152] and ORL-SDN [153] were of messages:
developed. The former was proposed to resolve three lim- • Client-to-Metrics-Server and Client-to-DANE Interfaces
itations that were not addressed in SDNDASH and could carry the metrics and status messages, respectively.

576 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
• DANE-to-DANEInterfacecarriestheparametersenhanc- • The client-based adaptation schemes show a
ing delivery messages. good performance given certain environments and
• DANE-to-Client Interface carries the parameters enhanc- circumstances. They are suited for large-scale deploy-
ing reception messages. mentsand they require modifications only on the client
TheSANDarchitectureisprimarilybasedonfeedbackfrom side. However, most of these schemes suffer under
the clients (e.g., QoE metrics) and the network (e.g., available network-bottleneck conditions (i.e., they are not globally
bandwidth). This kind of architecture is not easy to imple- optimal). Reason for this is the lack of a central element
ment, and hence, only few works have tackled this problem that guides the players in their bitrate decisions.
yet. Unsurprisingly, SDN is one of the main enablers for the • The server-based adaptation schemes provide the advan-
SAND architecture [151], [161]. Further details on the SAND tage of central control. However, these schemes may
architecture and messages can be found in ISO/IEC 23009-5, introduce a high complexity on the server and produce
which was published by MPEG in early 2017. additional overhead, which may harm the network effi-
ciency.Additionally,theseschemesneedmodificationsin
|     | IV. COMPARISONBETWEENBITRATE |     |     |     |     |     |                  |            |       |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | ---------------- | ---------- | ----- | --- | --- | --- |
|     |                              |     |     |     |     | the | manifests and/or | the server | side. |     |     |     |
ADAPTATIONSCHEMES
|     |     |     |     |     |     | • The | network-assisted | adaptation | schemes | aim | to have | a   |
| --- | --- | --- | --- | --- | --- | ----- | ---------------- | ---------- | ------- | --- | ------- | --- |
Eachadaptationschemeproposesdistinctcriteriaforbitrate general view of the network, which helps the clients in
decisions, where they work only under indirect or implicit their bitrate decisions. These schemes are suitable for
assumptions and specific scenarios, and focuses on a specific small-to-large networks and show a high performance in
deployment or different network characteristics. Currently, improving the viewer QoE. A similar observation can
there is a lack of general consistent frameworks that can be made for hybrid schemes. However, the real-world
formally evaluate and compare different bitrate adaptation deployment of both scheme classes remains challeng-
schemes, and test and verify the efficiency of their compo- ing as they introduce some overhead that may harm the
nents.Onlyafewalgorithmsformallydescribewhatobjective network performance and since they require additional
they want to optimize, making an effective comparison nigh entities in the network.
impossible. In this part, we provide a feature comparison It might be of interest to note that Table II provides only
between various state-of-the-art bitrate adaptation schemes in a feature comparison between the different schemes, such as
each category from the taxonomy in Fig. 3. Table II summa- the heuristics, experimentation parameters and collected met-
rizes this comparison for each surveyed paper in terms of the rics. A performance comparison is difficult for mainly three
following aspects: reasons: (i) the unavailability of source codes, (ii) the lack
• Heuristic(s): The measurements and values that the of a unified QoE framework and metrics to evaluate these
algorithm bases its download decision on {BW: avail- schemes, and (iii) because every scheme has its own param-
able bandwidth, Buffer: buffer occupancy, SDT: segment eters and assumptions, and may have been designed for a
downloadtime,DC:devicecapabilities,CPU:CPUload, specific environment and settings.
| QT: perceptual |     | quality, | PA: proxy | assistance, | CA: cen- |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
tral entity assistance, SDN or SDN-app: SDN assistance, V. DISCUSSION
| Seg-size:     | segment       | size,         | Seg-quality:    | segment  | quality,        |                   |              |               |          |             |           |     |
| ------------- | ------------- | ------------- | --------------- | -------- | --------------- | ----------------- | ------------ | ------------- | -------- | ----------- | --------- | --- |
|               |               |               |                 |          |                 | In this           | section, we  | discuss       | emerging | HAS trends, | namely    |     |
| Seg-schedule: |               | segment       | scheduling}.    |          |                 |                   |              |               |          |             |           |     |
|               |               |               |                 |          |                 | (A) HAS           | and scalable | video         | coding   | (SVC), (B)  | advanced  |     |
| • Fairness:   | Describes     |               | the algorithm’s | fairness | between         |                   |              |               |          |             |           |     |
|               |               |               |                 |          |                 | transport         | options such | as HTTP/2     | and      | Quick UDP   | Internet  |     |
| multiple      | clients       | that share    | the network.    | Some     | algorithms      |                   |              |               |          |             |           |     |
|               |               |               |                 |          |                 | Connections       | (QUIC),      | (C) immersive | media    | streaming,  | specif-   |     |
| equally       | share         | the bandwidth | among           | the      | clients, indi-  |                   |              |               |          |             |           |     |
|               |               |               |                 |          |                 | ically 360-degree | video        | streaming,    | and      | (D) HAS     | datasets. |     |
| cated         | by BW, others | share         | the bandwidth   |          | based on either |                   |              |               |          |             |           |     |
| perceptual    | quality       | or            | QoE, indicated  | by       | QT and QoE,     |                   |              |               |          |             |           |     |
|               |               |               |                 |          |                 | A. HAS            | and Scalable | Video Coding  | (SVC)    |             |           |     |
respectively.
• QoE:Doesthealgorithmsupportandintegrateoneofthe In most state-of-the-art adaptive streaming systems, non-
objective QoE models? scalable video coding (i.e., AVC, HEVC, VP9/AV1) is widely
• Number of clients: Single indicates one client only, relied upon due to its coding efficiency, ease of implemen-
multiple(few) indicates less than 10 clients, and tation, and widespread adoption. However, scalable video
multiple(many) indicates more than 10 clients. coding has multiple benefits such as resiliency to packet
• QoE optimization: Does the algorithm propose a QoE losses and better adaptability to device capabilities (e.g., if
model and aim to optimize it? a device is not capable of decoding high-quality videos,
• Content type: Live or video-on-demand (VoD). it can choose to decode lower layers only). Many stud-
• Heterogeneity: Does the algorithm take heterogeneous ies [55], [68], [162], [163] have shown benefits of using SVC
devices into account in its experimental testing? in HAS rather than AVC [30]: (1) it allows HAS to support
• SVC support: Does the adaptation algorithm support the heterogeneous clients, (2) it reduces storage and networking
streaming of SVC-encoded video? costs, and (3) it enables CDNs and caches to be used more
• BG traffic: Does the paper include background traffic in efficiently, e.g., by prioritizing the base layer and providing
their experimental tests? enhancement layers only when network resources are avail-
From Table II, we can deduce the following outcomes: able.Fig.13depictsSVC-basedHASwhereeachsegmentcan

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 577
IIELBAT
SEMEHCSNOITATPADAETARTIBDEYEVRUSEHTNEEWTEBNOSIRAPMOCERUTAEF

578 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
|     |     |     |     |     |     |     | Fig.14.          | HASusingHTTP/1.1versusthek-pushmethodusingHTTP/2. |                 |              |           |            |            |             |        |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------------------------------------- | --------------- | ------------ | --------- | ---------- | ---------- | ----------- | ------ |
|     |     |     |     |     |     |     | with advanced    |                                                   | features        | such         | as frame  | exchange,  |            | request     | pri-   |
|     |     |     |     |     |     |     | oritization,     | header                                            | field           | compression, |           | and        | server     | push.       | A      |
|     |     |     |     |     |     |     | first evaluation |                                                   | has been        | conducted    |           | by Mueller |            | et al.      | [169], |
|     |     |     |     |     |     |     | which shows      | that                                              | HTTP/2          | can          | achieve   | a          | similar    | performance |        |
|     |     |     |     |     |     |     | compared         | to HTTP/1.1                                       |                 | (with        | pipelined | persistent |            | connections |        |
|     |     |     |     |     |     |     | enabled).        | Wei                                               | and Swaminathan |              | [57]      | used       | the HTTP/2 |             | server |
pushfeatureandintroducedk-pushtoreducebothlivelatency
|     |     |     |     |     |     |     | and the    | number  | of       | segment    | requests. | In     | k-push,  | the        | client |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | ---------- | --------- | ------ | -------- | ---------- | ------ |
|     |     |     |     |     |     |     | sends one  | request | to       | the server | every     | k      | segments | indicating |        |
|     |     |     |     |     |     |     | the number | of      | segments | (k)        | to be     | pushed | to the   | client.    | The    |
Fig.13. AVC-basedvs.SVC-basedHAS.
|          |        |           |            |         |              |     | server responds |            | by   | pushing    | each | segment         | consecutively |           | as  |
| -------- | ------ | --------- | ---------- | ------- | ------------ | --- | --------------- | ---------- | ---- | ---------- | ---- | --------------- | ------------- | --------- | --- |
|          |        |           |            |         |              |     | soon as         | it becomes |      | available, | but  | all at          | the same      | requested |     |
|          |        |           |            |         |              |     | bitrate level   | (see       | Fig. | 14). Xiao  | et   | al. [172]       | further       | evaluated |     |
| be split | into a | subset of | bitstreams | instead | of different |     | bitrate         |            |      |            |      |                 |               |           |     |
|          |        |           |            |         |              |     | the k-push      | scheme     | and  | showed     | that | it deteriorated |               | network   |     |
levels,andthus,thevideosegmentscanbeencodedatdifferent
|     |     |     |     |     |     |     | adaptability, | since | its | gains | diminish | as  | k increases |     | and it |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | ----- | -------- | --- | ----------- | --- | ------ |
SVCqualities(temporal,spatial,SNR).Usingthismechanism,
|                 |          |               |            |               |             |              | led to the  | “over-push” |               | problem     | where     | network         |                    | resources   | are  |
| --------------- | -------- | ------------- | ---------- | ------------- | ----------- | ------------ | ----------- | ----------- | ------------- | ----------- | --------- | --------------- | ------------------ | ----------- | ---- |
| a HAS client    | can      | incrementally |            | improve       | the quality | of           | a seg-      |             |               |             |           |                 |                    |             |      |
|                 |          |               |            |               |             |              | wasted      | due to      | video         | abandonment |           | by the          | viewers.           | Thus,       | the  |
| ment by         | fetching | additional    | bitstreams |               | or layers   | depending    |             |             |               |             |           |                 |                    |             |      |
|                 |          |               |            |               |             |              | authors     | proposed    | adaptive-push |             | to        | overcome        | k-push’s           |             | lim- |
| on the dynamics |          | of the        | available  | bandwidth.    |             | One key      | dif-        |             |               |             |           |                 |                    |             |      |
|                 |          |               |            |               |             |              | itations,   | which       | uses          | the same    | principle |                 | as its             | predecessor |      |
| ference         | when     | using SVC     | with       | DASH          | is that     | a client     | may         |             |               |             |           |                 |                    |             |      |
|                 |          |               |            |               |             |              | but selects | k           | adaptively.   | In          | both      | k-push          | and adaptive-push, |             |      |
| have to         | download | multiple      | segments   | (i.e.,        | base        | and enhance- |             |             |               |             |           |                 |                    |             |      |
|                 |          |               |            |               |             |              | the client  | can         | implement     | various     |           | rate adaptation |                    | algorithms. |      |
| ment layers)    | for      | one playback  |            | epoch, unlike |             | in the case  | of          |             |               |             |           |                 |                    |             |      |
Cherifetal.[173]alsousedHTTP/2serverpushtoimplement
non-scalablevideo.DayanandaandSwaminathan[164]inves-
afaststartupwheresegmentswereinitiallypushedtotheclient
| tigated the  | gain     | of SHVC | in              | HAS, and       | they  | found        | that it        |            |           |        |          |           |             |        |       |
| ------------ | -------- | ------- | --------------- | -------------- | ----- | ------------ | -------------- | ---------- | --------- | ------ | -------- | --------- | ----------- | ------ | ----- |
|              |          |         |                 |                |       |              | upon receiving |            | a request | for    | the MPD. | As        | the         | client | would |
| could result | in       | bitrate | savings         | but at the     | price | of increased |                |            |           |        |          |           |             |        |       |
|              |          |         |                 |                |       |              | typically      | be unaware |           | of the | initial  | bandwidth | conditions, |        | the   |
| encoding     | overhead | due     | to scalability. | Interestingly, |       | MPEG’s       |                |            |           |        |          |           |             |        |       |
authorssuggestedusingaWebSocketconnectionoverHTTP/2
| exploration | towards | a   | future video | coding | format | with | capa- |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | ------------ | ------ | ------ | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
toexchangevariousstatusmessagesincludingbandwidthesti-
| bilities beyond |          | HEVC     | initially | suggested      | having | scalability | as      |              |     |          |             |     |                 |     |      |
| --------------- | -------- | -------- | --------- | -------------- | ------ | ----------- | ------- | ------------ | --- | -------- | ----------- | --- | --------------- | --- | ---- |
|                 |          |          |           |                |        |             | mation  | information. |     | Finally, | an overview |     | of HTTP/2-based |     |      |
| a built-in      | feature, | but that | has       | been withdrawn |        | from the    | final   |              |     |          |             |     |                 |     |      |
|                 |          |          |           |                |        |             | methods | to improve   |     | the live | experience  |     | of HAS          | has | been |
callforproposals[165],andthus,isnotconsideredinVersatile
|              |     |             |     |     |     |     | presented            | in [174], |     | which        | includes | (1)        | stream | termination,    |     |
| ------------ | --- | ----------- | --- | --- | --- | --- | -------------------- | --------- | --- | ------------ | -------- | ---------- | ------ | --------------- | --- |
| Video Coding |     | (VVC) [23]. |     |     |     |     |                      |           |     |              |          |            |        |                 |     |
|              |     |             |     |     |     |     | (2) request/response |           |     | multiplexing |          | and stream |        | prioritization, |     |
and(3)serverpush.ItprovidesadetailedanalysisofHTTP/2-
B. HTTP/2 and QUIC-Based Streaming based QoE-improvement methods including a comprehensive
| Google | initially | developed | SPDY | [166], | which | eventually | evaluation. |     |     |     |     |     |     |     |     |
| ------ | --------- | --------- | ---- | ------ | ----- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
led to the specification of HTTP/2 [167], and also devel- 2) QUIC: QUIC is a UDP-based secure transport
oped QUIC [168], which, with HTTP/2, addresses the latency layer protocol that aims to speed up the connections,
and head-of-line (HOL) blocking issues that were inherent to reduce latencies, enable congestion and flow control, allow
HTTP/1.1 over TCP. Both HTTP/2 and QUIC may have an multiple (multiplexed/pipelined) data connections (e.g., HTTP
impact on the HAS performance [79], [169]–[171]. request/response)overthesameUDPconnectionwithoutHOL
1) HTTP/2: HTTP/2 is used over a single persistent TCP blocking, and UDP connection migration with Forward Error
connection (with pipelining support) between the client and Correction (FEC). QUIC has been evaluated in the context of
server comprising multiple streams in a full duplex model HAS by Timmerer and Bertoni [170] and the results show a

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 579
similaradaptation performanceofHTTP/2over TCP,HTTP/2 be addressed by the server push feature of HTTP/2 as sug-
over SSL, HTTP/1.1 over QUIC and SPDY over QUIC. The gested in [180]. A number of open issues are also discussed
experimental results reported that QUIC introduces around by Graf et al. [179] ranging from encoding/streaming issues
10% more overhead than TCP at low bitrates. Also, the band- to QoE.
width utilization decreases when the round-trip time (RTT) 3) Standardization: Several standardization bodies and
increases,butitremainshighandstablearound87%.Asimilar industryforums have startedworking towards achieving inter-
evaluationwasconductedbyBhatetal.[171],whichrevealed operability between different VR systems. An overview is
that bitrate adaptation schemes deployed on top of QUIC do provided in [181]. MPEG’s efforts to standardize the storage
not show a performance increase unless the existing schemes and delivery formats for 360-degree video content is specified
are properly adjusted to be used in conjunction with QUIC. intheOmnidirectionalMediaFormat(OMAF)standard[182].
OtherevaluationsofQUIChavefocusedongenerictrafficpat- OMAF describes the content processing architecture, projec-
ternssuchasregularWebsites[175],[176]withoutproviding tion and packaging formats, streaming approaches and DASH
details on HAS. integration of 360-degree videos [183].
D. HAS Datasets
C. Immersive Media Streaming In the past, a great number of DASH datasets has emerged.
Immersive media streaming and specifically virtual reality The first DASH dataset was released by Lederer et al. [19]
(VR)/360-degree video streaming is nowadays gaining sig- and comprises various genres (i.e., animation, sport, movie),
nificant attention from both academia and industry due to encoded using up to 20 representations (up to 1080p resolu-
the increasing availability of 360-degree cameras and head tion), and different segment lengths (i.e., 1, 2, 4, 6, 10, and
mounted displays (HMD). VR applications range from 3D 15 seconds). Additionally, for some representations per frame
video gaming to 360-degree video streaming and teleimmer- PSNR values are provided. Initial evaluations of the dataset
sion.Inthissurvey,wehighlighttheuseofHASin360-degree providerecommendationsforanoptimalsegmentlengthbased
video streaming. on the coding efficiency (i.e., 4s) and the influence of enabled
versus disabled persistent connections.
1) Characteristics of 360-Degree Videos: 360-degree
A distributed DASH dataset has been released by
videos are recorded using multiple specialized high-resolution
Lederer et al. [184], which distributes the dataset across
cameras that capture a sphere around the user. The resulting
multiple locations and utilizes multiple BaseURL elements
video is typically stitched and mapped onto a 2D plane using
within the media presentation description (MPD). It can be
variousprojectionformatsduetoalackofcodingtoolsforthe
used to simulate different content distribution network (CDN)
spherical domain. At the client side, the 2D plane is mapped
locations and bitstream switching across multiple CDNs.
backonasurfacemeshandrenderedbasedonthedevicecapa-
Le Feuvre et al. [185] provide an ultra high definition
bilities. Characteristically, they allow users to freely navigate
(UHD) HEVC DASH dataset targeting UHD services (i.e.,
within the media presentation but only a fraction of the actual
resolutions up to 3840x2160, framerate up to 60 fps, and up
contentispresentedtotheuseratanygivenpointintime.This
to 10 bpp) using HEVC, which is the major difference com-
isreferredtoastheviewport,orfieldofview.Consideringthe
pared to previously proposed datasets. Kreuzberger et al. [30]
highresolutionnatureofthefullsphericalcontent,theamount
provides a DASH dataset focusing on scalable video coding
ofdatatobestreamedmaybesignificantlyhigherthantheone
(SVC)andexperimentingwithin-networkadaptationinnamed
for conventional, non-360-degree videos.
data networks and information-centric networking, respec-
2) Adaptive Streaming Challenges: Most adaptive stream-
tively. Unfortunately, support for SVC in end user devices is
ing schemes for 360-degree videos merely adopt traditional
stilllimited.Quinlanetal.[186]proposeadatasetcomprising
non-360-degreevideodeliveryschemes.Theentire360-degree
AVC and HEVC for the evaluation of DASH systems.
scene is adaptively delivered without taking the user’s view-
Finally, Zabrovskiy et al. [187] provide a multi-codec
port into account. For example, the content outside the user’s
DASH dataset comprising multiple state-of-the-art as well as
current viewport is delivered at the same quality as the con-
emerging video codecs, i.e., AVC, HEVC, VP9, and AV1
tent within the user’s viewport, wasting bandwidth, and thus,
to enable interoperability testing and allow for experiment-
network resources. Viewport-adaptive [177] and tile-based
ing with adaptation strategies of DASH clients supporting
adaptive streaming techniques [178], [179] are currently sug-
multiple video codecs. A similar dataset is provided by
gested in the literature to overcome this disadvantage. The
Quinlan and Sreenan [188] focusing on AVC and HEVC for
former provides pre-encoded versions of a given viewport
UHD (4K) resolutions.
based on the user’s device orientation, which requires addi-
tional content versions to be prepared, stored, and distributed
within the delivery network. The latter uses the tiling feature
VI. CONCLUSION
available in modern video codecs (e.g., in HEVC, VP9, and Since the emergence of HTTP adaptive streaming (HAS),
AV1) that enables spatial segmentation of videos. Each tile many bitrate adaption schemes have been proposed. Each is
can beprojected indifferentrepresentations toallow forqual- tryingtoaddresscertainHAS-relatedproblemsandstrivingto
ity adaptation. However, requesting each tileindividually may achieve a set of goals. In fact, most state-of-the-art schemes
increase the number of requests tremendously, which could share a common main objective, which is to improve viewer

580 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
QoE.Inthissurvey,weexaminedasetofwell-knownschemes operatingregimes(i.e.,differentnetworkenvironments,chunk
and heuristics for their applicability. sizes, content types, etc.), and may require parameter tuning.
Firstly,weclassifiedthebitrateadaptationschemesintofour A common set of test conditions might reveal significantly
main categories, namely, client-based, server-based, network- different results than the ones reported in the original papers.
assistedandhybrid.Inaclient-basedscheme,theclientstrives In the broad area of adaptive streaming, there are many open
to optimize the viewer QoE individually and considers one of challenges and issues that need more attention:
the many heuristics based on the available bandwidth, play- • Understanding the main factors that degrade the viewer
back buffer size, segment size, and duration. Server-based QoE through subjective and objective tests; then, design-
schemes, in contrast, do not require any cooperation from the ing a standardized QoE function.
clients, and they use a server traffic shaping mechanism. In • Designing placement algorithms for CDN, proxies and
network-assisted schemes, the clients use information coming SDN controllers.
fromin-networkdevices,likeproxies,togetherwiththeirown • Understanding the trade-off between content-aware
observations for bitrate adaptation. Finally, the hybrid solu- encoding versus content-aware streaming (generating
tions consist of many entities like clients, central managers, variable bitrate encoded segments is easy, but streaming
| servers, | and network | devices |     | that | are involved | in  | the bitrate | them | is not). |     |     |     |     |     |
| -------- | ----------- | ------- | --- | ---- | ------------ | --- | ----------- | ---- | -------- | --- | --- | --- | --- | --- |
decision process. • Designing a robust solution that achieves fair resource
Secondly, we offered a description of each scheme by pre- sharing among concurrent HAS clients when they com-
senting the problems they are trying to solve, their goals, pete in a bottleneck network.
•
findings, main components and critical acclaims. Although Understandingmulti-pathbenefitsandaddingitscapabil-
the described schemes in each category provide noteworthy ities to HAS delivery systems.
benefits and efficiency in some specific network characteris- • Studying the interaction between HAS and non-HAS
tics,manysharedchallengesexistineverycategory,especially traffic, and its impact on the QoE.
when multiple clients compete for the shared bandwidth: • Mixing client-based and hybrid solutions without intro-
• Client-based schemes likely suffer from HAS stability ducing extra overhead.
issuesandQoEvariationsduetotheHAS’ON-OFFpat- • Providing a solution to deliver 360-degree videos that
tern. These issues are aggravated when the number of reducesbandwidthconsumptionwhilenothamperingthe
| geographically-distributed |     |     |     | clients | keeps | growing. |     | QoE. |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ------- | ----- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- |
• Server-based schemes introduce overhead and complex- • Leveraging machine learning and deep learning tech-
ity, limiting the system scalability with the increasing niques to analyze and classify encrypted HAS traffic,
number of clients. which can help monitor and mitigate QoE impairments.
• Network-assistedandhybridadaptationschemesusecen-
| tralized | entities | to  | assist | the | clients in | their | decisions, |     |     |     |     |     |     |     |
| -------- | -------- | --- | ------ | --- | ---------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ACKNOWLEDGMENT
| improve |     | the viewer | QoE, | and | avoid | HAS | scalability |     |     |     |     |     |     |     |
| ------- | --- | ---------- | ---- | --- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
issues.However,theyaredifficulttodeployoverthefully The authors would like to thank Prof. Saad Harous for his
| decentralizednatureofreal-worldnetworkinfrastructures |      |                |     |                |             |              |       | valuable feedback. |     |     |     |     |     |     |
| ----------------------------------------------------- | ---- | -------------- | --- | -------------- | ----------- | ------------ | ----- | ------------------ | --- | --- | --- | --- | --- | --- |
| and                                                   | they | do not support |     | large-scale    | deployments |              | where |                    |     |     |     |     |     |     |
| many                                                  | HAS  | players        | are | geographically |             | distributed. |       |                    |     |     |     |     |     |     |
REFERENCES
| Thirdly, | we       | provided | a comparison |     | between        | the | surveyed |            |                   |        |          |                  |     |       |
| -------- | -------- | -------- | ------------ | --- | -------------- | --- | -------- | ---------- | ----------------- | ------ | -------- | ---------------- | --- | ----- |
| schemes  | in terms | of a     | set of       | QoE | and networking |     | aspects. |            |                   |        |          |                  |     |       |
|          |          |          |              |     |                |     |          | [1] “Cisco | visual networking | index: | Forecast | and methodology, |     | 2016– |
2021,”SanJose,CA,USA,CiscoSyst.,Inc.,WhitePaper,2017.
| Our comparison |       | may help  | researchers |     | in the     | area of   | adaptive |               |                           |      |           |           |           |            |
| -------------- | ----- | --------- | ----------- | --- | ---------- | --------- | -------- | ------------- | ------------------------- | ---- | --------- | --------- | --------- | ---------- |
|                |       |           |             |     |            |           |          | [2] Real-Time | Messaging Protocol(RTMP), |      |           | Adobe,    | San Jose, | CA,        |
| streaming      | where | it offers | a general   |     | consistent | framework | that     |               |                           |      |           |           |           |            |
|                |       |           |             |     |            |           |          | USA,          | 2014. Accessed:           | Nov. | 21, 2017. | [Online]. |           | Available: |
canformallyevaluateandcomparedifferentbitrateadaptation http://www.adobe.com/devnet/rtmp.html
logic categories, and test the efficiency of their components. [3] V.Jacobson,R.Frederick,S.Casner,andH.Schulzrinne.(2014).Real-
|          |              |     |            |     |           |            |     | Time Transport | Protocol | (RTP). Accessed: |     | Nov. 21, | 2017. | [Online]. |
| -------- | ------------ | --- | ---------- | --- | --------- | ---------- | --- | -------------- | -------- | ---------------- | --- | -------- | ----- | --------- |
| Finally, | we concluded |     | the survey | by  | a general | discussion | on  |                |          |                  |     |          |       |           |
Available:https://www.ietf.org/rfc/rfc3550.txt
the recent developments in HAS systems, such as the use of [4] H. Schulzrinne. (2016). Real Time Streaming Protocol
HTTP/2 and QUIC as well as HAS of VR content. Version 2.0. Accessed: Nov. 21, 2017. [Online]. Available:
In general, certain limitations still exist when conducting a https://tools.ietf.org/html/rfc7826
[5] J.Goldberg,M.Westerlund,andT.Zeng.(2014).ANetworkAddress
comprehensive survey. The lack of standardized benchmarks Translator (NAT) Traversal Mechanism for Media Controlled by the
and frameworks (i.e., datasets, test conditions and QoE met- Real-Time Streaming Protocol (RTSP). Accessed: Nov. 21, 2017.
[Online].Available:https://tools.ietf.org/html/rfc7825
| rics) makes | any      | performance |             | comparison | a               | difficult | task. For    |              |                     |            |         |           |            |            |
| ----------- | -------- | ----------- | ----------- | ---------- | --------------- | --------- | ------------ | ------------ | ------------------- | ---------- | ------- | --------- | ---------- | ---------- |
|             |          |             |             |            |                 |           |              | [6] L. Popa, | A. Ghodsi, and      | I. Stoica, | “HTTP   | as        | the narrow | waist      |
| example,    | a fair   | comparison  |             | between    | client-based    |           | adaptation   |              |                     |            |         |           |            |            |
|             |          |             |             |            |                 |           |              | of the       | future Internet,”   | in Proc.   | 9th ACM | SIGCOMM   |            | Workshop   |
| schemes     | in terms | of          | performance |            | (i.e., resource |           | utilization) |              |                     |            |         |           |            |            |
|             |          |             |             |            |                 |           |              | Hot Topics   | Netw. (Hotnets-IX), | 2010,      | pp.1–6. | [Online]. |            | Available: |
http://doi.acm.org/10.1145/1868447.1868453
| and QoE | (i.e., | video stalls, | stabilization, |     | quality | oscillations), |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------- | -------------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[7] X.Liuetal.,“AcaseforacoordinatedInternetvideocontrolplane,”in
| requires | that they | undergo | similar |     | experimentation |     | configura- |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ------- | --- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Proc.ACMSIGCOMMConf.Appl.Technol.Archit.ProtocolsComput.
tion, including a unified bandwidth trace, certain networking Commun. (SIGCOMM), 2012, pp.359–370. [Online]. Available:
setups and similar device capabilities. The surveyed schemes http://doi.acm.org/10.1145/2342356.2342431
|          |         |      |       |         |             |     |          | [8] Microsoft | Smooth Streaming, | Microsoft, | Redmond,   |                     | WA, USA, | 2015. |
| -------- | ------- | ---- | ----- | ------- | ----------- | --- | -------- | ------------- | ----------------- | ---------- | ---------- | ------------------- | -------- | ----- |
| may have | perform | well | under | certain | conditions, | but | they all |               |                   |            |            |                     |          |       |
|          |         |      |       |         |             |     |          | Accessed:     | Nov. 21, 2017.    | [Online].  | Available: | http://www.iis.net/ |          |       |
use various heuristics that broadly relate to specific settings, downloads/microsoft/smooth-streaming

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 581
[9] Apple HTTP Live Streaming, Apple, Cupertino, CA, USA, [31] Z. Duanmu, K. Zeng, K. Ma, A. Rehman, and Z. Wang, “A quality-
2015. Accessed: Nov. 21, 2017. [Online]. Available: of-experience index for streaming video,” IEEE J. Sel. Topics Signal
https://developer.apple.com/streaming/ Process.,vol.11,no.1,pp.154–166,Feb.2017.
[10] Adobe HTTP Dynamic Streaming, Adobe, San Jose, CA, [32] Z.Lietal.,“StreamingvideooverHTTPwithconsistentquality,”in
USA, 2015. Accessed: Nov. 21, 2017. [Online]. Available: Proc. 5th ACM Multimedia Syst. Conf. (MMSys), 2014, pp.248–258.
http://www.adobe.com/products/hds-dynamic-streaming.html [Online].Available:http://doi.acm.org/10.1145/2557642.2557658
[11] Akamai. (2015). Akamai HD. Accessed: Nov. 21, 2017. [Online]. [33] L. Yu, T. Tillo, and J. Xiao, “QoE-driven dynamic adaptive video
Available: https://www.akamai.com/us/en/resources/live-video- streaming strategy with future information,” IEEE Trans. Broadcast.,
| streaming.jsp |     |     |     |     |     |     | vol.63,no.3,pp.523–534,Sep.2017. |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[12] C. Timmerer. (2012). HTTP Streaming of MPEG [34] T. Hossfeld et al., “Initial delay vs. interruptions: Between the devil
Media. Accessed: Nov. 21, 2017. [Online]. Available: and thedeep bluesea,” inProc. 4thInt. WorkshopQual. Multimedia
https://multimediacommunication.blogspot.co.at/2010/05/http- Exp.,Jul.2012,pp.1–6.
streaming-of-mpeg-media.html [35] T.DePessemier,K.DeMoor,W.Joseph,L.DeMarez,andL.Martens,
| [13] Dash | Industry  | Forum. | (2017).  | DASH-264 | JavaScript | Reference  |              |               |           |                |       |               |      |            |
| --------- | --------- | ------ | -------- | -------- | ---------- | ---------- | ------------ | ------------- | --------- | -------------- | ----- | ------------- | ---- | ---------- |
|           |           |        |          |          |            |            | “Quantifying | the           | influence | of rebuffering |       | interruptions | on   | the user’s |
| Client.   | Accessed: |        | Nov. 21, | 2017.    | [Online].  | Available: |              |               |           |                |       |               |      |            |
|           |           |        |          |          |            |            | quality      | of experience | during    | mobile         | video | watching,”    | IEEE | Trans.     |
http://dashif.org/reference/players/javascript/index.html Broadcast.,vol.59,no.1,pp.47–61,Mar.2013.
[14] B.Rainer,S.Lederer,C.Müller,andC.Timmerer,“AseamlessWeb [36] Y. Qi and M. Dai, “The effect of frame freezing and frame skipping
integration of adaptive HTTP streaming,” in Proc. 20th Eur. Signal on video quality,” in Proc. Int. Conf. Intell. Inf. Hiding Multimedia,
Process.Conf.(EUSIPCO),Aug.2012,pp.1519–1523.
Dec.2006,pp.423–426.
[15] J.Kua,G.Armitage,andP.Branch,“Asurveyofrateadaptationtech-
|        |             |          |           |      |        |              | [37] D. C. Robinson, |     | Y. Jutras, | and V. | Craciun, | “Subjective | video | quality |
| ------ | ----------- | -------- | --------- | ---- | ------ | ------------ | -------------------- | --- | ---------- | ------ | -------- | ----------- | ----- | ------- |
| niques | for dynamic | adaptive | streaming | over | HTTP,” | IEEE Commun. |                      |     |            |        |          |             |       |         |
assessmentofHTTPadaptivestreamingtechnologies,”BellLab.Tech.
SurveysTuts.,vol.19,no.3,pp.1842–1866,3rdQuart.,2017.
J.,vol.16,no.4,pp.5–23,Mar.2012,doi:10.1002/bltj.20531.
[16] E. Thomas, M. O. van Deventer, T. Stockhammer, A. C. Begen, [38] R.HambergandH.deRidder,“Time-varyingimagequality:Modeling
and J. Famaey, “Enhancing MPEG DASH performance via server the relation between instantaneous and overall quality,” SMPTE J.,
| and network | assistance,” |     | SMPTE | Motion | Imag. J., | vol. 126, no. 1, |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ----- | ------ | --------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.108,no.11,pp.802–811,Nov.1999.
pp.22–27,2017.
|               |                     |     |     |        |            |             | [39] N. Cranley, | P.        | Perry, and | L. Murphy,       |     | “User perception |      | of adapt-  |
| ------------- | ------------------- | --- | --- | ------ | ---------- | ----------- | ---------------- | --------- | ---------- | ---------------- | --- | ---------------- | ---- | ---------- |
| [17] X. Wang, | “Network-assistance |     | and | server | management | in adaptive |                  |           |            |                  |     |                  |      |            |
|               |                     |     |     |        |            |             | ing video        | quality,” | Int.       | J. Human–Comput. |     | Stud.,           | vol. | 64, no. 8, |
streamingontheInternet,”inProc.W3CWebTVWorkshop,Munich,
pp.637–647,2006.[Online].Available:http://www.sciencedirect.com/
Germany, 2014. [Online]. Available: https://www.w3.org/2013/10/tv- science/article/pii/S1071581905002028
workshop/papers/webtv4_submission_17.pdf
|     |     |     |     |     |     |     | [40] A. Hore | and D. | Ziou, “Image | quality | metrics: | PSNR | vs. | SSIM,” in |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ------------ | ------- | -------- | ---- | --- | --------- |
[18] T.Wiegand,G.J.Sullivan,G.Bjontegaard,andA.Luthra,“Overview
Proc.20thInt.Conf.PatternRecognit.,Aug.2010,pp.2366–2369.
oftheH.264/AVCvideocodingstandard,”IEEETrans.CircuitsSyst.
|     |     |     |     |     |     |     | [41] Q. Huynh-Thu |     | and M. | Ghanbari, | “Scope | of validity | of  | PSNR in |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | --------- | ------ | ----------- | --- | ------- |
VideoTechnol.,vol.13,no.7,pp.560–576,Jul.2003.
|                  |     |            |     |              |     |                | image/video | quality | assessment,” |     | Electron. | Lett., | vol. | 44, no. 13, |
| ---------------- | --- | ---------- | --- | ------------ | --- | -------------- | ----------- | ------- | ------------ | --- | --------- | ------ | ---- | ----------- |
| [19] S. Lederer, |     | C. Müller, | and | C. Timmerer, |     | “Dynamic adap- |             |         |              |     |           |        |      |             |
pp.800–801,Jun.2008.
| tive | streaming | over HTTP | dataset,” |     | in Proc. | 3rd Multimedia |     |     |     |     |     |     |     |     |
| ---- | --------- | --------- | --------- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Syst. Conf. (MMSys), 2012, pp.89–94. [Online]. Available: [42] A. Rehman, K. Zeng, and Z. Wang, “Display device-adapted video
http://doi.acm.org/10.1145/2155555.2155570 quality-of-experienceassessment,”inProc.SPIEHumanVis.Electron.
Imag.,vol.9394.SanFrancisco,CA,USA,2015,Art.no.939406.
| [20] H. Schwarz, | D.  | Marpe, | and T. Wiegand, |     | “Overview | of the scalable |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | --------------- | --- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[43] K.urRehmanLaghari,O.Issa,F.Speranza,andT.H.Falk,“Quality-
| video | coding | extension | of the | H.264/AVC | standard,” | IEEE Trans. |               |            |     |           |           |           |     |             |
| ----- | ------ | --------- | ------ | --------- | ---------- | ----------- | ------------- | ---------- | --- | --------- | --------- | --------- | --- | ----------- |
|       |        |           |        |           |            |             | of-experience | perception |     | for video | streaming | services: |     | Preliminary |
CircuitsSyst.VideoTechnol.,vol.17,no.9,pp.1103–1120,Sep.2007.
subjectiveandobjectiveresults,”inProc.Asia–Pac.SignalInf.Process.
[21] G.J.Sullivan,J.-R.Ohm,W.-J.Han,andT.Wiegand,“Overviewofthe
highefficiencyvideocoding(HEVC)standard,”IEEETrans.Circuits Assoc.Annu.SummitConf.,Dec.2012,pp.1–9.
Syst.VideoTechnol.,vol.22,no.12,pp.1649–1668,Dec.2012. [44] B. Rainer, S. Petscharnig, C. Timmerer, and H. Hellwagner,
|     |     |     |     |     |     |     | “Statistically | indifferent |     | quality | variation: | An approach |     | for reduc- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | ------- | ---------- | ----------- | --- | ---------- |
[22] J.M.Boyce,Y.Ye,J.Chen,andA.K.Ramasubramonian,“Overview
|                    |          |            |          |             |            |                 | ing multimedia |      | distribution       | cost | for adaptive | video   | streaming      | ser- |
| ------------------ | -------- | ---------- | -------- | ----------- | ---------- | --------------- | -------------- | ---- | ------------------ | ---- | ------------ | ------- | -------------- | ---- |
| of SHVC:           | Scalable | extensions | of       | the high    | efficiency | video coding    |                |      |                    |      |              |         |                |      |
|                    |          |            |          |             |            |                 | vices,”        | IEEE | Trans. Multimedia, |      | vol.         | 19, no. | 4, pp.849–860, |      |
| standard,”         | IEEE     | Trans.     | Circuits | Syst. Video | Technol.,  | vol. 26, no. 1, |                |      |                    |      |              |         |                |      |
| pp.20–34,Jan.2016. |          |            |          |             |            |                 | Apr.2017.      |      |                    |      |              |         |                |      |
[23] C. Timmerer, “MPEG column: 122nd MPEG meeting in San Diego, [45] A. Balachandran et al., “Developing a predictive model of quality of
CA,USA,”SIGMultimediaRec.,vol.10,no.2,p.6,Jun.2018. experience for Internet video,” ACM SIGCOMM Comput. Commun.
|     |     |     |     |     |     |     | Rev., vol. | 43, | no. 4, pp.339–350, |     | Aug. | 2013. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------ | --- | ---- | ----- | --------- | ---------- |
[24] J.DeCock,A.Mavlankar,A.Moorthy,andA.Aaron,“Alarge-scale
http://doi.acm.org/10.1145/2534169.2486025
videocodeccomparisonofx264,x265andlibvpxforpracticalVOD
|                |     |             |      |           |        |                | [46] M. Montagud, |     | F. Boronat, | H. Stokking, |     | and R. | van Brandenburg, |     |
| -------------- | --- | ----------- | ---- | --------- | ------ | -------------- | ----------------- | --- | ----------- | ------------ | --- | ------ | ---------------- | --- |
| applications,” | in  | Proc. SPIE, | vol. | 9971. San | Diego, | CA, USA, 2016, |                   |     |             |              |     |        |                  |     |
Art.no.997116. “Inter-destination multimedia synchronization: Schemes, use cases
[25] M.Seufertetal.,“AsurveyonqualityofexperienceofHTTPadaptive and standardization,” Multimedia Syst., vol. 18, no. 6, pp.459–482,
| streaming,”IEEECommun.SurveysTuts.,vol.17,no.1,pp.469–492, |     |     |     |     |     |     | 2012.          |     |              |     |                 |     |                   |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | --------------- | --- | ----------------- | --- |
|                                                            |     |     |     |     |     |     | [47] B. Rainer | and | C. Timmerer, |     | “Self-organized |     | inter-destination |     |
1stQuart.,2015.
|                   |     |                   |     |       |        |                  | multimedia | synchronization |     | for | adaptive | media | streaming,” | in  |
| ----------------- | --- | ----------------- | --- | ----- | ------ | ---------------- | ---------- | --------------- | --- | --- | -------- | ----- | ----------- | --- |
| [26] S. Akhshabi, |     | S. Narayanaswamy, |     | A. C. | Begen, | and C. Dovrolis, |            |                 |     |     |          |       |             |     |
“An experimental evaluation of rate-adaptive video players Proc. 22nd ACM Int. Conf. Multimedia (MM), 2014, pp.327–336.
over HTTP,” Signal Process. Image Commun., vol. 27, no. 4, [Online].Available:http://doi.acm.org/10.1145/2647868.2654938
pp.271–287,2012.[Online].Available:http://www.sciencedirect.com/ [48] B.Rainer,S.Petscharnig,andC.Timmerer,“Mergeandforward:Self-
science/article/pii/S0923596511001159 organized inter-destination multimedia synchronization,” in Proc. 6th
|                   |     |                    |     |       |        |                  | ACM Multimedia |     | Syst. Conf. | (MMSys), |     | 2015, pp.77–80. |     | [Online]. |
| ----------------- | --- | ------------------ | --- | ----- | ------ | ---------------- | -------------- | --- | ----------- | -------- | --- | --------------- | --- | --------- |
| [27] S. Akhshabi, |     | L. Anantakrishnan, |     | A. C. | Begen, | and C. Dovrolis, |                |     |             |          |     |                 |     |           |
Available:http://doi.acm.org/10.1145/2713168.2713185
| “What | happens | when HTTP | adaptive | streaming | players | compete for |     |     |     |     |     |     |     |     |
| ----- | ------- | --------- | -------- | --------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
bandwidth?” in Proc. 22nd Int. Workshop Netw. Oper. Syst. Support [49] B. Rainer, S. Petscharnig, C. Timmerer, and H. Hellwagner, “Is
Digit. Audio Video (NOSSDAV), 2012, pp.9–14. [Online]. Available: one second enough? Evaluating QoE for inter-destination multimedia
http://doi.acm.org/10.1145/2229087.2229092 synchronization using human computation and crowdsourcing,” in
[28] S. Bae, D. Jang, and K. Park, “Why Is HTTP adaptive streaming so Proc. 7th Int. Workshop Qual. Multimedia Exp. (QoMEX), 2015,
pp.1–6.
hard?”inProc.6thAsia–Pac.WorkshopSyst.(APSys),2015,pp.1–12.
[Online].Available:http://doi.acm.org/10.1145/2797022.2797031 [50] T. Stockhammer, “Dynamic adaptive streaming over HTTP:
[29] G. Cermak, M. Pinson, and S. Wolf, “The relationship among video Standards and design principles,” in Proc. 2nd Annu. ACM Conf.
quality,screenresolution,andbitrate,”IEEETrans.Broadcast.,vol.57, Multimedia Syst. (MMSys), 2011, pp.133–144. [Online]. Available:
no.2,pp.258–262,Jun.2011. http://doi.acm.org/10.1145/1943552.1943572
[30] C.Kreuzberger,D.Posch,andH.Hellwagner,“Ascalablevideocoding [51] C. Liu, I. Bouazizi, and M. Gabbouj, “Rate adaptation for
datasetandtoolchainfordynamicadaptivestreamingoverHTTP,”in adaptive HTTP streaming,” in Proc. 2nd Annu. ACM Conf.
Proc. 6th ACM Multimedia Syst. Conf. (MMSys), 2015, pp.213–218. Multimedia Syst. (MMSys), 2011, pp.169–174. [Online]. Available:
[Online].Available:http://doi.acm.org/10.1145/2713168.2713193 http://doi.acm.org/10.1145/1943552.1943575

582 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
[52] C. Liu, I. Bouazizi, M. M. Hannuksela, and M. Gabbouj, “Rate [71] C. Mueller. (2015). Microsoft Smooth Streaming. Accessed:
adaptationfordynamicadaptivestreamingoverHTTPincontentdis- Nov. 21, 2017. [Online]. Available: https://bitmovin.com/microsoft-
tribution network,” Signal Process. Image Commun., vol. 27, no. 4, smooth-streaming-mss/
pp.288–311,2012.[Online].Available:http://www.sciencedirect.com/ [72] R. Pantos and W. May. (2017). HTTP Live Streaming. Accessed:
science/article/pii/S0923596511001135 Dec.20,2017.[Online].Available:https://www.ietf.org/rfc/rfc8216.txt
[53] Z.Lietal.,“Probeandadapt:RateadaptationforHTTPvideostream- [73] Apple. (2016). QuickTime. Accessed: Nov. 21, 2017. [Online].
ingatscale,”IEEEJ.Sel.AreasCommun.,vol.32,no.4,pp.719–733, Available:http://www.apple.com/sg/quicktime/
Apr.2014. [74] (2015).SimplifiedAdaptiveVideoStreaming:AnnouncingSupportfor
[54] X.Xie,X.Zhang,S.Kumar,andL.E.Li,“piStream:Physicallayer HLS and DASH in Windows 10. Accessed: Dec. 20, 2017. [Online].
informedadaptivevideostreamingoverLTE,”inProc.21stAnnu.Int. Available:https://goo.gl/gZM3mQ
Conf.MobileComput.Netw.(MobiCom),2015,pp.413–425.[Online]. [75] Supported Media Formats | Android Developers. Accessed:
Available:http://doi.acm.org/10.1145/2789168.2790118 Dec. 20, 2017. [Online]. Available: https://developer.android.com/
[55] T. Andelin, V. Chetty, D. Harbaugh, S. Warnick, and D. Zappala, guide/topics/media/media-formats.html
“Quality selection for dynamic adaptive streaming over HTTP [76] ActionScript, Adobe, San Jose, CA, USA, 2016. Accessed:
with scalable video coding,” in Proc. 3rd Multimedia Syst. Nov. 21, 2017. [Online]. Available: http://www.adobe.com/
Conf. (MMSys), 2012, pp.149–154. [Online]. Available: devnet/actionscript.html
http://doi.acm.org/10.1145/2155555.2155580 [77] T. Cloonan and J. Allen, “Competitive analysis of adaptive video
streaming implementations,” in Proc. SCTE Cable-Tec Expo Tech.
[56] M. Xiao, V. Swaminathan, S. Wei, and S. Chen, “DASH2M:
Workshop,2011,pp.1–34.
ExploringHTTP/2forInternetstreamingtomobiledevices,”inProc.
[78] D.Wu,Y.T.Hou,W.Zhu,Y.-Q.Zhang,andJ.M.Peha,“Streaming
ACM Multimedia Conf. (MM), 2016, pp.22–31. [Online]. Available:
video over the Internet: Approaches and directions,” IEEE Trans.
http://doi.acm.org/10.1145/2964284.2964313
CircuitsSyst.VideoTechnol.,vol.11,no.3,pp.282–300,Mar.2001.
[57] S. Wei and V. Swaminathan, “Low latency live video stream-
[79] C. Müller, S. Lederer, and C. Timmerer, “An evaluation of dynamic
ing over HTTP 2.0,” in Proc. Netw. Oper. Syst. Support
adaptive streaming over HTTP in vehicular environments,” in Proc.
Digit. Audio Video Workshop, 2014, p.37. [Online]. Available:
ACM4thWorkshopMobileVideo(MoVid),2012,pp.37–42.[Online].
http://doi.acm.org/10.1145/2578260.2578277
Available:http://doi.acm.org/10.1145/2151677.2151686
[58] K. Miller, A.-K. Al-Tamimi, and A. Wolisz, “QoE-based low-delay [80] Bitmovin. (2015). MPEG-DASH vs. Commercial Players. Accessed:
livestreamingusingthroughputpredictions,”ACMTrans.Multimedia Nov.21,2017.[Online].Available:http://www.goo.gl/TmazZ8
Comput.Commun.Appl.,vol.13,no.1,pp.1–4,Oct.2016.[Online]. [81] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-
Available:http://doi.acm.org/10.1145/2990505 theoretic approach for dynamic adaptive video streaming over
[59] J. Hao, R. Zimmermann, and H. Ma, “GTube: Geo-predictive HTTP,” SIGCOMM Comput. Commun. Rev., vol. 45, no. 4,
video streaming over HTTP in mobile environments,” in Proc. 5th pp.325–338, Aug. 2015. [Online]. Available: http://doi.acm.org/
ACM Multimedia Syst. Conf. (MMSys), 2014, pp.259–270. [Online]. 10.1145/2829988.2787486
Available:http://doi.acm.org/10.1145/2557642.2557647 [82] C.Zhou,X.Zhang,L.Huo,andZ.Guo,“Acontrol-theoreticapproach
[60] H. Riiser, H. S. Bergsaker, P. Vigmostad, P. Halvorsen, and torateadaptationfordynamicHTTPstreaming,”inProc.Vis.Commun.
C. Griwodz, “A comparison of quality scheduling in commercial ImageProcess.,Nov.2012,pp.1–6.
adaptive HTTP streaming solutions on a 3G network,” in Proc. 4th [83] A.Sobhani,A.Yassine,andS.Shirmohammadi,“Avideobitrateadap-
WorkshopMobileVideo(MoVid),2012,pp.25–30.[Online].Available: tationandpredictionmechanismforHTTPadaptivestreaming,”ACM
http://doi.acm.org/10.1145/2151677.2151684 Trans. Multimedia Comput. Commun. Appl., vol. 13, no. 2, p. 18,
[61] J.Yao,S.S.Kanhere,andM.Hassan,“ImprovingQoSinhigh-speed Mar.2017.[Online].Available:http://doi.acm.org/10.1145/3052822
mobilityusingbandwidthmaps,”IEEETrans.MobileComput.,vol.11, [84] L.DeCicco,V.Caldaralo,V.Palmisano,andS.Mascolo,“ELASTIC:
no.4,pp.603–617,Apr.2012. A client-side controller for dynamic adaptive streaming over HTTP
[62] J. Yao, S. S. Kanhere, I. Hossain, and M. Hassan, “Empirical eval- (DASH),” in Proc. 20th Int. Packet Video Workshop, Dec. 2013,
uation of HTTP adaptive streaming under vehicular mobility,” in pp.1–8.
NETWORKING 2011, J. Domingo-Pascual, P. Manzoni, S. Palazzo, [85] J.C.Doyle,B.A.Francis,andA.R.Tannenbaum,FeedbackControl
A. Pont, and C. Scoglio, Eds. Heidelberg, Germany: Springer, 2011, Theory.NewYork,NY,USA:Macmillan,2013.
pp.92–105. [86] K.Miller,E.Quacchio,G.Gennari,andA.Wolisz,“Adaptationalgo-
[63] V.Singh,J.Ott,andI.D.D.Curcio,“Predictivebufferingforstreaming rithm for adaptive streaming over HTTP,” in Proc. 19th Int. Packet
videoin3Gnetworks,”inProc.IEEEInt.Symp.WorldWirelessMobile VideoWorkshop(PV),May2012,pp.173–178.
MultimediaNetw.(WoWMoM),Jun.2012,pp.1–10. [87] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, effi-
[64] B.TaaniandR.Zimmermann,“Spatio-temporalanalysisofbandwidth ciency, and stability in HTTP-based adaptive video streaming
maps for geo-predictive video streaming in mobile environments,” in with FESTIVE,” in Proc. ACM 8th Int. Conf. Emerg. Netw.
Proc. ACM Multimedia Conf. (MM), 2016, pp.888–897. [Online]. Exp. Technol. (CoNEXT), 2012, pp.97–108. [Online]. Available:
Available:http://doi.acm.org/10.1145/2964284.2964333 http://doi.acm.org/10.1145/2413176.2413189
[88] C.Zhou,C.Lin,X.Zhang,andZ.Guo,“TFDASH:Afairness,stability,
[65] C.Mueller,S.Lederer,R.Grandl,andC.Timmerer,“Oscillationcom-
and efficiency aware rate control approach for multiple clients over
pensatingdynamicadaptivestreamingoverHTTP,”inProc.IEEEInt.
DASH,” IEEE Trans. Circuits Syst. Video Technol., to be published,
Conf.MultimediaExpo(ICME),Jun.2015,pp.1–6.
doi:10.1109/TCSVT.2017.2771246.
[66] T.-Y. Huang, R. Johari, N. McKeown, M. Trunnell, and M. Watson,
[89] G. Tian and Y. Liu, “Towards agile and smooth video adaptation in
“A buffer-based approach to rate adaptation: Evidence from a
dynamicHTTPstreaming,”inProc.ACM8thInt.Conf.Emerg.Netw.
large video streaming service,” SIGCOMM Comput. Commun. Rev.,
Exp. Technol. (CoNEXT), 2012, pp.109–120. [Online]. Available:
vol. 44, no. 4, pp.187–198, Aug. 2014. [Online]. Available:
http://doi.acm.org/10.1145/2413176.2413190
http://doi.acm.org/10.1145/2740070.2626296
[90] A. J. Smola and B. Schölkopf, “A tutorial on support vector regres-
[67] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman,“BOLA:Near-optimal sion,” Stat. Comput., vol. 14, no. 3, pp.199–222, Aug. 2004,
bitrate adaptation for online videos,” in Proc. IEEE INFOCOM 35th doi:10.1023/B:STCO.0000035301.49549.88.
Annu.Int.Conf.Comput.Commun.,Apr.2016,pp.1–9. [91] C. Wang, A. Rizk, and M. Zink, “SQUAD: A spectrum-based qual-
[68] C. Sieber, T. Hoßfeld, T. Zinner, P. Tran-Gia, and C. Timmerer, ity adaptation for dynamic adaptive streaming over HTTP,” in Proc.
“Implementation and user-centric comparison of a novel adaptation ACM 7th Int. Conf. Multimedia Syst. (MMSys), 2016, p.1. [Online].
logic for DASH with SVC,” in Proc. IFIP/IEEE Int. Symp. Integr. Available:http://doi.acm.org/10.1145/2910017.2910593
Netw.Manag.(IM),May2013,pp.1318–1323. [92] D. Havey, R. Chertov, and K. Almeroth, “Receiver driven rate
[69] P. K. Yadav, A. Shafiei, and W. T. Ooi, “QUETRA: A queu- adaptation for wireless multimedia applications,” in Proc. ACM
ing theory approach to DASH rate adaptation,” in Proc. ACM 3rd Multimedia Syst. Conf. (MMSys), 2012, pp.155–166. [Online].
Multimedia Conf. (MM), 2017, pp.1130–1138. [Online]. Available: Available:http://doi.acm.org/10.1145/2155555.2155582
http://doi.acm.org/10.1145/3123266.3123390 [93] P.Juluri,V.Tamarapalli,andD.Medhi,“SARA:Segmentawarerate
[70] R. Huysegems, B. De Vleeschauwer, T. Wu, and W. Van Leekwijck, adaptation algorithm for dynamic adaptive streaming over HTTP,”
“SVC-based HTTP adaptive streaming,” Bell Labs Tech. J., vol. 16, in Proc. IEEE Int. Conf. Commun. Workshop (ICCW), Jun. 2015,
no.4,pp.25–41,Mar.2012. pp.1765–1770.

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 583
[94] A. Beben, P. Wis´niewski, J. M. Batalla, and P. Krawiec, “ABMA+: [115] D.P.PalomarandM.Chiang,“Atutorialondecompositionmethodsfor
Lightweight and efficient algorithm for HTTP adaptive streaming,” network utility maximization,” IEEE J. Sel. Areas Commun., vol. 24,
in Proc. ACM 7th Int. Conf. Multimedia Syst. (MMSys), 2016, p.2. no.8,pp.1439–1451,Aug.2006.
[Online].Available:http://doi.acm.org/10.1145/2910017.2910596 [116] S. D’Aronco, L. Toni, and P. Frossard, “Price-based controller for
[95] A.Bentaleb,A.C.Begen,R.Zimmermann,andS.Harous,“Wantto utility-aware HTTP adaptive streaming,” IEEE MultiMedia, vol. 24,
play DASH? A game theoretic approach for adaptive streaming over no.2,pp.20–29,Apr./Jun.2017.
HTTP,”inProc.ACMMMSys,2018,pp.13–26. [117] S.Petrangeli,J.Famaey,M.Claeys,S.Latré,andF.DeTurck,“QoE-
[96] R. B. Myerson, Game Theory. New York, NY, USA: Harvard Univ. drivenrateadaptationheuristicforfairadaptivevideostreaming,”ACM
Press,2013. Trans.MultimediaComput.Commun.Appl.,vol.12,no.2,p.28,2016.
[97] M. Xing, S. Xiang, and L. Cai, “A real-time adaptive algorithm for [118] V. Joseph and G. de Veciana, “NOVA: QoE-driven optimization of
videostreamingovermultiplewirelessaccessnetworks,”IEEEJ.Sel. DASH-based video delivery in networks,” in Proc. IEEE INFOCOM
AreasCommun.,vol.32,no.4,pp.795–805,Apr.2014. Conf.Comput.Commun.,Apr.2014,pp.82–90.
[98] A. Bokani, M. Hassan, S. Kanhere, and X. Zhu, “Optimizing HTTP- [119] R.M.GrayandR.Gray,Probability,RandomProcesses,andErgodic
basedadaptivestreaminginvehicularenvironmentusingMarkovdeci- Properties.NewYork,NY,USA:Springer,1988.
sionprocess,”IEEETrans.Multimedia,vol.17,no.12,pp.2297–2309, [120] J. Chen, R. Mahindra, M. A. Khojastepour, S. Rangarajan, and
Dec.2015. M. Chiang, “A scheduling framework for adaptive video delivery
[99] S. Petrangeli, M. Claeys, S. Latré, J. Famaey, and F. De Turck, over cellular networks,” in Proc. ACM 19th Annu. Int. Conf. Mobile
“A multi-agent Q-learning-based framework for achieving fairness in Comput. Netw. (MobiCom), 2013, pp.389–400. [Online]. Available:
HTTPadaptivestreaming,”inProc.IEEENetw.Oper.Manag.Symp. http://doi.acm.org/10.1145/2500423.2500433
(NOMS),May2014,pp.1–9. [121] A. El Essaili et al., “Quality-of-experience driven adaptive HTTP
[100] F. Chiariotti, S. D’Aronco, L. Toni, and P. Frossard, “Online learn- mediadelivery,”inProc.IEEEInt.Conf.Commun.(ICC),Jun.2013,
ing adaptation strategy for DASH clients,” in Proc. ACM 7th Int. pp.2480–2485.
Conf. Multimedia Syst. (MMSys), 2016, p.8. [Online]. Available: [122] J. W. Kleinrouweler, S. Cabrero, R. van der Mei, and P. Cesar,
http://doi.acm.org/10.1145/2910017.2910603 “Modeling stability and bitrate of network-assisted HTTP adaptive
[101] C.Zhou,C.-W.Lin,andZ.Guo,“mDASH:AMarkovdecision-based streaming players,” in Proc. 27th Int. Teletraffic Congr. (ITC), 2015,
rate adaptation approach for dynamic HTTP streaming,” IEEE Trans. pp.177–184,doi:10.1109/ITC.2015.28
Multimedia,vol.18,no.4,pp.738–751,Apr.2016. [123] V. Ramamurthi and O. Oyman, “Video-QoE aware radio resource
[102] H. Mao, R. Netravali, and M. Alizadeh, “Neural adaptive video allocation for HTTP adaptive streaming,” in Proc. IEEE Int. Conf.
streamingwithPensieve,”inProc.Conf.ACMSpecialInterestGroup Commun.(ICC),Jun.2014,pp.1076–1081.
DataCommun.(SIGCOMM),2017,pp.197–210.[Online].Available: [124] V.Ramamurthi,O.Oyman,andJ.Foerster,“Video-QoEawareresource
http://doi.acm.org/10.1145/3098822.3098843 management at network core,” in Proc. IEEE Glob. Commun. Conf.,
[103] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella, “D-DASH: A Dec.2014,pp.1418–1423.
deepQ-learningframeworkforDASHvideostreaming,”IEEETrans. [125] B. Han, F. Qian, L. Ji, V. Gopalakrishnan, and N. Bedminster,
Cogn.Commun.Netw.,vol.3,no.4,pp.703–718,Dec.2017. “MP-DASH: Adaptive video streaming over preference-aware
[104] Y. Li, “Deep reinforcement learning: An overview,” CoRR, multipath,” in Proc. ACM 12th Int. Conf. Emerg. Netw. Exp.
vol. abs/1701.07274, 2017. [Online]. Available: http://arxiv.org/ Technol. (CoNEXT), 2016, pp.129–143. [Online]. Available:
abs/1701.07274 http://doi.acm.org/10.1145/2999572.2999606
[105] J. K. Rowling, Harry Potter and the Goblet of Fire. London, U.K.: [126] Z. Yan, J. Xue, and C. W. Chen, “Prius: Hybrid edge cloud and
Bloomsbury,2000. client adaptation for HTTP adaptive streaming in cellular networks,”
[106] S. Akhshabi, L. Anantakrishnan, C. Dovrolis, and A. C. Begen, IEEETrans.CircuitsSyst.VideoTechnol.,vol.27,no.1,pp.209–222,
“Server-basedtrafficshapingforstabilizingoscillatingadaptivestream- Jan.2017.
ingplayers,”inProc.23rdACMWorkshopNetw.Oper.Syst.Support [127] A.H.Zahran,J.J.Quinlan,K.K.Ramakrishnan,andC.J.Sreenan,
Digit.AudioVideo(NOSSDAV),2013,pp.19–24.[Online].Available: “SAP: Stall-aware pacing for improved DASH video experi-
http://doi.acm.org/10.1145/2460782.2460786 ence in cellular networks,” in Proc. 8th ACM Multimedia
[107] R. Houdaille and S. Gouache, “Shaping HTTP adaptive streams Syst. Conf. (MMSys), 2017, pp.13–26. [Online]. Available:
for a better user experience,” in Proc. ACM 3rd Multimedia http://doi.acm.org/10.1145/3083187.3083199
Syst. Conf. (MMSys), 2012, pp.1–9. [Online]. Available: [128] T.T.T.NguyenandG.Armitage,“AsurveyoftechniquesforInternet
http://doi.acm.org/10.1145/2155555.2155557 trafficclassificationusingmachinelearning,”IEEECommun.Surveys
[108] A.Detti,B.Ricci,andN.Blefari-Melazzi,“Tracker-assistedrateadap- Tuts.,vol.10,no.4,pp.56–76,4thQuart.,2008.
tationforMPEGDASHlivestreaming,”inProc.IEEEINFOCOM35th [129] M. D. F. De Grazia et al., “QoE multi-stage machine learning for
Annu.IEEEInt.Conf.Comput.Commun.,Apr.2016,pp.1–9. dynamicvideostreaming,”IEEETrans.Cogn.Commun.Netw.,vol.4,
[109] L. De Cicco, S. Mascolo, and V. Palmisano, “Feedback control no.1,pp.146–161,Mar.2018.
for adaptive live video streaming,” in Proc. 2nd Annu. ACM Conf. [130] G. Urvoy-Keller, “On the stationarity of TCP bulk data transfers,”
Multimedia Syst. (MMSys), 2011, pp.145–156. [Online]. Available: in Proc. 6th Int. Conf. Passive Active Netw. Meas. (PAM), 2005,
http://doi.acm.org/10.1145/1943552.1943573 pp.27–40,doi:10.1007/978-3-540-31966-5_3.
[110] J. Bruneau-Queyreix, M. Lacaud, D. Negru, J. M. Batalla, and [131] Z. Akhtar et al., “Oboe: Auto-tuning video ABR algorithms to
E. Borcoci, “MS-stream: A multiple-source adaptive streaming solu- network conditions,” in Proc. SIGCOMM Comput. Commun. Rev.,
tionenhancingconsumer’sperceivedquality,”inProc.14thIEEEAnnu. Aug. 2018. [Online]. Available: https://engineering.purdue.edu/∼isl/
Consum.Commun.Netw.Conf.(CCNC),Jan.2017,pp.427–434. papers/sigcomm18-final128.pdf
[111] E.Thomasetal.,“Applicationsanddeploymentsofserverandnetwork [132] P. Georgopoulos, M. Broadbent, A. Farshad, B. Plattner, and
assistedDASH(SAND),”inProc.Int.Broadcast.Conv.Conf.(IBC), N. Race, “Using software defined networking to enhance the deliv-
Amsterdam,TheNetherlands,2016,p.22. ery of video-on-demand,” Comput. Commun., vol. 69, pp.79–87,
[112] R. K. P. Mok, X. Luo, E. W. W. Chan, and R. K. C. Chang, Sep. 2015. [Online]. Available: http://www.sciencedirect.com/
“QDASH: A QoE-aware DASH system,” in Proc. ACM 3rd science/article/pii/S0140366415002315
MultimediaSyst.Conf.(MMSys),2012,pp.11–22.[Online].Available: [133] G. Cofano et al., “Design and experimental evaluation of network-
http://doi.acm.org/10.1145/2155555.2155558 assisted strategies for HTTP adaptive streaming,” in Proc. ACM 7th
[113] N. Bouten et al., “QoE-driven in-network optimization for adap- Int.Conf.MultimediaSyst.(MMSys),2016,p.3.[Online].Available:
tive video streaming based on packet sampling measurements,” http://doi.acm.org/10.1145/2910017.2910597
Comput. Netw., vol. 81, pp.96–115, Apr. 2015. [Online]. Available: [134] D.Bhat,A.Rizk,M.Zink,andR.Steinmetz,“Networkassistedcontent
http://www.sciencedirect.com/science/article/pii/S1389128615000468 distribution for adaptive bitrate video streaming,” in Proc. 8th ACM
[114] V. Krishnamoorthi, N. Carlsson, E. Halepovic, and E. Petajan, MultimediaSyst.Conf.(MMSys),2017,pp.62–75.[Online].Available:
“BUFFEST: Predicting buffer conditions and real-time require- http://doi.acm.org/10.1145/3083187.3083196
ments of HTTP(S) adaptive streaming clients,” in Proc. 8th ACM [135] A. Seema, L. Schwoebel, T. Shah, J. Morgan, and M. Reisslein,
MultimediaSyst.Conf.(MMSys),2017,pp.76–87.[Online].Available: “WVSNP-DASH: Name-based segmented video streaming,” IEEE
http://doi.acm.org/10.1145/3083187.3083193 Trans.Broadcast.,vol.61,no.3,pp.346–355,Sep.2015.

584 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.21,NO.1,FIRSTQUARTER2019
[136] D.E.Knuth,“Backusnormalformvs.BackusNaurform,”Commun. [156] A. Ganjam et al., “C3: Internet-scale control plane for video quality
ACM, vol. 7, no. 12, pp.735–736, Dec. 1964. [Online]. Available: optimization,” in Proc. 12th USENIX Symp. Netw. Syst. Design
http://doi.acm.org/10.1145/355588.365140 Implement.(NSDI),Oakland,CA,USA,2015,pp.131–144.[Online].
[137] S. Lederer, C. Mueller, C. Timmerer, and H. Hellwagner, “Adaptive Available: https://www.usenix.org/conference/nsdi15/technical-
multimedia streaming in information-centric networks,” IEEE Netw., sessions/presentation/ganjam
vol.28,no.6,pp.91–96,Nov.2014. [157] J. Jiang et al., “CFA: A practical prediction system for
[138] C. Westphal et al., “Adaptive video streaming over information- video QoE optimization,” in Proc. 13th USENIX Symp. Netw.
centric networking (ICN), Internet Eng. Task Force, Fremont, Syst. Design Implement. (NSDI), Santa Clara, CA, USA,
CA, USA, Rep. RFC 7933, Aug. 2016. [Online]. Available: 2016, pp.137–150. [Online]. Available: https://www.usenix.org/
http://www.ietf.org/rfc/rfc7933.txt conference/nsdi16/technical-sessions/presentation/jiang
[139] B.Rainer,D.Posch,andH.Hellwagner,“Investigatingtheperformance [158] Y. Sun et al., “CS2P: Improving video bitrate selection and adap-
ofpull-baseddynamicadaptivestreaminginNDN,”IEEEJ.Sel.Areas tation with data-driven throughput prediction,” in Proc. ACM
Commun.,vol.34,no.8,pp.2130–2140,Aug.2016. SIGCOMM Conf. (SIGCOMM), 2016, pp.272–285. [Online].
[140] S.Petrangeli,N.Bouten,M.Claeys,andF.D.Turck,“TowardsSVC- Available:http://doi.acm.org/10.1145/2934872.2934898
based adaptive streaming in information centric networks,” in Proc. [159] J. Jiang, S. Sun, V. Sekar, and H. Zhang, “Pytheas: Enabling
IEEE Int. Conf. Multimedia Expo Workshops (ICMEW), Jun. 2015, data-driven quality of experience optimization using group-based
pp.1–6.
|              |          |       |            |           |     |               | exploration-exploitation,” |                   |     | in Proc. | 14th    | USENIX | Symp. | Netw. |
| ------------ | -------- | ----- | ---------- | --------- | --- | ------------- | -------------------------- | ----------------- | --- | -------- | ------- | ------ | ----- | ----- |
| [141] C. Xu, | W. Quan, | A. V. | Vasilakos, | H. Zhang, | and | G.-M.Muntean, |                            |                   |     |          |         |        |       |       |
|              |          |       |            |           |     |               | Syst.                      | Design Implement. |     | (NSDI),  | Boston, | MA,    | USA,  | 2017, |
“Information-centric cost-efficient optimization for multimedia con- pp.393–406. [Online]. Available: https://www.usenix.org/
tent delivery in mobile vehicular networks,” Comput. Commun., conference/nsdi17/technical-sessions/presentation/jiang
vol. 99, pp.93–106, Feb. 2017. [Online]. Available: http:// [160] E. Thomas, M. van Deventer, T. Stockhammer, A. C. Begen, and
www.sciencedirect.com/science/article/pii/S0140366416302729
|     |     |     |     |     |     |     | J. Famaey, | “Enhancing |     | MPEG DASH | performance |     | via server | and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --------- | ----------- | --- | ---------- | --- |
[142] A.Detti,B.Ricci,andN.Blefari-Melazzi,“Mobilepeer-to-peervideo
|     |     |     |     |     |     |     | network | assistance,” | in  | Proc. Int. | Broadcast. | Conv. | (IBC) | Conf., |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------- | ---------- | ----- | ----- | ------ |
streamingoverinformation-centricnetworks,”Comput.Netw.,vol.81, Amsterdam,TheNetherlands,2015,pp.48–53.
pp.272–288,Apr.2015,doi:10.1016/j.comnet.2015.02.018. [161] J.W.Kleinrouweler,B.Meixner,andP.Cesar,“Improvingvideoqual-
[143] D. Kreutz et al., “Software-defined networking: A comprehensive ityincrowdednetworksusingaDANE,”inProc.27thWorkshopNetw.
survey,”Proc.IEEE,vol.103,no.1,pp.14–76,Jan.2015.
Oper.Syst.SupportDigit.AudioVideo(NOSSDAV),2017,pp.73–78.
[144] J.Yang,K.Zhu,Y.Ran,W.Cai,andE.Yang,“Jointadmissioncontrol
[Online].Available:http://doi.acm.org/10.1145/3083165.3083167
androutingviaapproximatedynamicprogrammingforstreamingvideo
[162] J.Famaeyetal.,“OnthemeritsofSVC-basedHTTPadaptivestream-
over software-defined networking,” IEEE Trans. Multimedia, vol. 19, ing,”inProc.IFIP/IEEEInt.Symp.Integr.Netw.Manag.(IM),Ghent,
| no.3,pp.619–631,Mar.2017. |              |              |           |            |                   |                 | Belgium,May2013,pp.419–426. |          |                 |            |                |           |          |          |
| ------------------------- | ------------ | ------------ | --------- | ---------- | ----------------- | --------------- | --------------------------- | -------- | --------------- | ---------- | -------------- | --------- | -------- | -------- |
| [145] P. Georgopoulos,    |              | Y. Elkhatib, | M.        | Broadbent, | M. Mu,            | and N. Race,    |                             |          |                 |            |                |           |          |          |
|                           |              |              |           |            |                   |                 | [163] Y. Sanchez            | et al.,  | “Efficient      | HTTP-based |                | streaming | using    | scalable |
| “Towards                  | network-wide | QoE          | fairness  | using      | OpenFlow-assisted | adap-           |                             |          |                 |            |                |           |          |          |
|                           |              |              |           |            |                   |                 | video                       | coding,” | Signal Process. |            | Image Commun., |           | vol. 27, | no. 4,   |
| tive video                | streaming,”  | in           | Proc. ACM | SIGCOMM    |                   | Workshop Future |                             |          |                 |            |                |           |          |          |
pp.329–342,2012.[Online].Available:http://www.sciencedirect.com/
HumanCentricMultimediaNetw.(FhMN),2013,pp.15–20.[Online]. science/article/pii/S0923596511001147
Available:http://doi.acm.org/10.1145/2491172.2491181 [164] U.S.M.DayanandaandV.Swaminathan,“Investigatingscalablehigh
| [146] A. Farshad, | P.  | Georgopoulos, | M.  | Broadbent, | M. Mu, | and N. Race, |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | ---------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
efficiencyvideocodingforHTTPstreaming,”inProc.IEEEInt.Conf.
“LeveragingSDNtoprovideanin-networkQoEmeasurementframe-
MultimediaExpoWorkshops(ICMEW),Jun.2015,pp.1–6.
work,”inProc.IEEEConf.Comput.Commun.Workshops(INFOCOM
|     |     |     |     |     |     |     | [165] C. Timmerer, | “MPEG | Column: |     | 120th MPEG | meeting | in  | Macau, |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ----- | ------- | --- | ---------- | ------- | --- | ------ |
WKSHPS),Apr.2015,pp.239–244.
|     |     |     |     |     |     |     | China,” | SIGMultimedia | Rec., | vol. | 9, no. 3, | p. 4, Jan. | 2018. | [Online]. |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ----- | ---- | --------- | ---------- | ----- | --------- |
[147] H. Nam, K.-H. Kim, J. Y. Kim, and H. Schulzrinne, “Towards QoE- Available:http://doi.acm.org/10.1145/3178422.3178426
| aware | video streaming | using | SDN,” | in Proc. | IEEE | Glob. Commun. |                 |        |       |              |           |           |            |     |
| ----- | --------------- | ----- | ----- | -------- | ---- | ------------- | --------------- | ------ | ----- | ------------ | --------- | --------- | ---------- | --- |
|       |                 |       |       |          |      |               | [166] M. Belshe | and R. | Peon. | (2012). SPDY | Protocol. | [Online]. | Available: |     |
Conf.,Austin,TX,USA,Dec.2014,pp.1317–1322.
https://www.chromium.org/spdy/spdy-whitepaper
[148] Q.Wangetal.,“GENICinema:AnSDN-assistedscalablelivevideo
|           |           |          |      |      |            |                  | [167] M. Belshe, | M.  | Thomson, | and | R. Peon. | (2015). | Hypertext |     |
| --------- | --------- | -------- | ---- | ---- | ---------- | ---------------- | ---------------- | --- | -------- | --- | -------- | ------- | --------- | --- |
| streaming | service,” | in Proc. | IEEE | 22nd | Int. Conf. | Netw. Protocols, |                  |     |          |     |          |         |           |     |
Oct.2014,pp.529–532. Transfer Protocol Version 2 (HTTP/2). [Online]. Available:
[149] S. Petrangeli, T. Wauters, R. Huysegems, T. Bostoen, and https://tools.ietf.org/html/rfc7540
[168] J.IyengarandM.Thomson.(2017).QUIC:AUDP-BasedMultiplexed
| F. De | Turck,        | “Software-defined |               | network-based |             | prioritization | to         |            |           |     |          |                 |            |     |
| ----- | ------------- | ----------------- | ------------- | ------------- | ----------- | -------------- | ---------- | ---------- | --------- | --- | -------- | --------------- | ---------- | --- |
|       |               |                   |               |               |             |                | and Secure | Transport. | Accessed: |     | Dec. 18, | 2017. [Online]. | Available: |     |
| avoid | video freezes | in                | HTTP adaptive |               | streaming,” | Int. J. Netw.  |            |            |           |     |          |                 |            |     |
https://tools.ietf.org/html/draft-ietf-quic-transport-08
| Manag., | vol. | 26, no. 4, | pp.248–268, |     | 2016. [Online]. | Available: |     |     |     |     |     |     |     |     |
| ------- | ---- | ---------- | ----------- | --- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://onlinelibrary.wiley.com/doi/abs/10.1002/nem.1931 [169] C. Mueller, S. Lederer, C. Timmerer, and H. Hellwagner, “Dynamic
[150] J.W.Kleinrouweler,S.Cabrero,andP.Cesar,“Deliveringstablehigh- Adaptive Streaming over HTTP/2.0,” in Proc. IEEE Int. Conf.
MultimediaExpo(ICME),Jul.2013,pp.1–6.
| quality    | video: | An SDN         | architecture | with       | DASH  | assisting network |                   |     |             |           |     |           |         |         |
| ---------- | ------ | -------------- | ------------ | ---------- | ----- | ----------------- | ----------------- | --- | ----------- | --------- | --- | --------- | ------- | ------- |
|            |        |                |              |            |       |                   | [170] C. Timmerer | and | A. Bertoni, | “Advanced |     | transport | options | for the |
| elements,” | in     | Proc. 7th Int. | Conf.        | Multimedia | Syst. | (MMSys), 2016,    |                   |     |             |           |     |           |         |         |
dynamicadaptivestreamingoverHTTP,”CoRR,vol.abs/1606.00264,
p.4.[Online].Available:http://doi.acm.org/10.1145/2910017.2910599
[151] A. Bentaleb, A. C. Begen, and R. Zimmermann, “SDNDASH: 2016.[Online].Available:http://arxiv.org/abs/1606.00264
Improving QoE of HTTP adaptive streaming using software [171] D. Bhat, A. Rizk, and M. Zink, “Not so QUIC: A performance
defined networking,” in Proc. ACM Multimedia Conf. (MM), study of DASH over QUIC,” in Proc. 27th Workshop Netw. Oper.
Syst.SupportDigit.AudioVideo,2017,pp.13–18.[Online].Available:
| 2016, | pp.1296–1305. |     | [Online]. | Available: |     | http://doi.acm.org/ |     |     |     |     |     |     |     |     |
| ----- | ------------- | --- | --------- | ---------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
http://doi.acm.org/10.1145/3083165.3083175
10.1145/2964284.2964332
[152] A.Bentaleb,A.C.Begen,R.Zimmermann,andS.Harous,“SDNHAS: [172] M. Xiao, V. Swaminathan, S. Wei, and S. Chen, “Evaluating
An SDN-Enabled Architecture to Optimize QoE in HTTP Adaptive and improving push based video streaming with HTTP/2,” in
Streaming,”IEEETrans.Multimedia,vol.19,no.10,pp.2136–2151, Proc. 26th Int. Workshop Netw. Oper. Syst. Support Digit.
|     |     |     |     |     |     |     | Audio | Video (NOSSDAV), |     | 2016, | pp.1–6. | [Online]. | Available: |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | ----- | ------- | --------- | ---------- | --- |
Oct.2017.
http://doi.acm.org/10.1145/2910642.2910652
| [153] A. Bentaleb, |     | A. C. Begen, | and | R. Zimmermann, |     | “ORL-SDN: |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Online reinforcement learning for SDN-enabled HTTP adap- [173] W. Cherif, Y. Fablet, E. Nassor, J. Taquet, and Y. Fujimori, “DASH
tive streaming,” ACM Trans. Multimedia Comput. Commun. fast start using HTTP/2,” in Proc. 25th ACM Workshop Netw. Oper.
Appl., vol. 14, no. 3, pp.1–28, Aug. 2018. [Online]. Available: Syst.SupportDigit.AudioVideo,2015,pp.25–30.[Online].Available:
http://doi.acm.org/10.1145/3219752,doi:10.1145/3219752. http://doi.acm.org/10.1145/2736084.2736088
|                    |     |           |        |             |            |       | [174] R. Huysegems |     | et al., | “HTTP/2-based | methods |     | to improve | the |
| ------------------ | --- | --------- | ------ | ----------- | ---------- | ----- | ------------------ | --- | ------- | ------------- | ------- | --- | ---------- | --- |
| [154] A. Bentaleb, | A.  | C. Begen, | and R. | Zimmermann, | “QoE-aware | band- |                    |     |         |               |         |     |            |     |
width broker for HTTP adaptive streaming flows in an SDN-enabled live experience of adaptive streaming,” in Proc. 23rd ACM
HFC network,” IEEE Trans. Broadcast., vol. 64, no. 2, pp.575–589, Int. Conf. Multimedia, 2015, pp.541–550. [Online]. Available:
| Jun.2018. |     |     |     |     |     |     | http://doi.acm.org/10.1145/2733373.2806264s |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[155] C.-F. Lai, R.-H. Hwang, H.-C. Chao, M. M. Hassan, and A. Alamri, [175] G. Carlucci, L. De Cicco, and S. Mascolo, “HTTP over UDP:
“A buffer-aware HTTP live streaming approach for SDN-enabled An experimental investigation of QUIC,” in Proc. 30th Annu.
5G wireless networks,” IEEE Netw., vol. 29, no. 1, pp.49–55, ACM Symp. Appl. Comput., 2015, pp.609–614. [Online]. Available:
| Jan./Feb.2015. |     |     |     |     |     |     | http://doi.acm.org/10.1145/2695664.2695706 |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |

BENTALEBetal.:SURVEYONBITRATEADAPTATIONSCHEMESFORSTREAMINGMEDIAOVERHTTP 585
[176] R. Netravali et al., “Mahimahi: Accurate record-and-replay for Bayan Taani receivedtheB.Sc.degreeinnetwork
HTTP,” in Proc. USENIX Annu. Tech. Conf. (USENIX ATC), 2015, engineeringandsecurityfromtheJordanUniversity
pp.417–429. [Online]. Available: https://www.usenix.org/conference/ of Science and Technology, Irbid, Jordan, in 2014.
atc15/technical-session/presentation/netravali She is currently pursuing the Ph.D. degree in
[177] X. Corbillon, G. Simon, A. Devlic, and J. Chakareski, “Viewport- computer science with the National University of
adaptivenavigable360-degreevideodelivery,”inProc.IEEEInt.Conf. Singapore,Singapore.Herresearchinterestsinclude
Commun.(ICC),May2017,pp.1–7,doi:10.1109/ICC.2017.7996611. multimedia systems and communications, adaptive
[178] R.Ghaznavi-Youvalarietal.,“ComparisonofHEVCcodingschemes videostreaming,andvirtualreality.
| for tile-based |     | viewport-adaptive |     | streaming | of omnidirectional | video,” |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --------- | ------------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
inProc.IEEE19thInt.WorkshopMultimediaSignalProcess.(MMSP),
Oct.2017,pp.1–6.
| [179] M. Graf, | C.       | Timmerer, | and C.             | Mueller, | “Towards | bandwidth effi- |     |     |     |     |     |     |     |
| -------------- | -------- | --------- | ------------------ | -------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| cient          | adaptive | streaming | of omnidirectional |          | video    | over HTTP:      |     |     |     |     |     |     |     |
Design, implementation, and evaluation,” in Proc. 8th ACM Ali C. Begen (S’98–M’07–SM’12) received the
Multimedia Syst. Conf., 2017, pp.261–271. [Online]. Available: Ph.D.degreeinelectricalandcomputerengineering
http://doi.acm.org/10.1145/3083187.3084016 fromGeorgiaTech.HejoinedtheComputerScience
| [180] S. Petrangeli, |     | V. Swaminathan, |     | M. Hosseini, | and | F. De Turck, |     |             |     |         |             |         |        |
| -------------------- | --- | --------------- | --- | ------------ | --- | ------------ | --- | ----------- | --- | ------- | ----------- | ------- | ------ |
|                      |     |                 |     |              |     |              |     | Department, |     | Ozyegin | University, | Turkey. | He was |
“Improving virtual reality streaming using HTTP/2,” in Proc. 8th a Research and Development Engineer with Cisco,
ACMMultimediaSyst.Conf.,2017,pp.225–228.[Online].Available: wherehedesignedanddevelopedalgorithms,proto-
http://doi.acm.org/10.1145/3083187.3083224 cols,products,andsolutionsintheserviceprovider
[181] C. Timmerer, “Immersive media delivery: Overview of ongoingstan- andenterprisevideodomains.Inadditiontoteach-
| dardization |     | activities,” IEEE | Commun. | Stand. | Mag., | vol. 1, no. | 4,  |     |     |     |     |     |     |
| ----------- | --- | ----------------- | ------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ingandresearch,heprovidesconsultingservicesto
pp.71–74,Dec.2017. industrial, legal, and academic institutions through
[182] B. Choi, Y.-K. Wang, M. M. Hannuksela, Y. Lim, and A. Murtaza, Networked Media, a company he co-founded. He
Information Technology—Coded Representation of Immersive Media wasarecipientofnumberofscholarlyandindustryawards.Hehaseditorial
(MPEG-I)—Part2:OmnidirectionalMediaFormat,ISO/IECStandard positions in prestigious magazines and journals in the field. He is a Senior
FDIS23090-2,Dec.2017.
MemberofACM.In2016,hewaselectedasaDistinguishedLecturerbythe
[183] D.Podborskietal.,“VirtualrealityandDASH,”inProc.Int.Broadcast. IEEECommunicationsSociety.Furtherinformationonhisprojects,publica-
Conv.(IBC)Conf.,2017,pp.1–11. tions, talks, teaching, standards, and professional activities can be found at
| [184] S. Lederer |     | et al., “Distributed |          | DASH dataset,” | in          | Proc. 4th ACM | http://ali.begen.net. |     |     |     |     |     |     |
| ---------------- | --- | -------------------- | -------- | -------------- | ----------- | ------------- | --------------------- | --- | --- | --- | --- | --- | --- |
| Multimedia       |     | Syst. Conf.          | (MMSys), | 2013,          | pp.131–135. | [Online].     |                       |     |     |     |     |     |     |
Available:http://doi.acm.org/10.1145/2483977.2483994
[185] J.LeFeuvre,J.-M.Thiesse,M.Parmentier,M.Raulet,andC.Daguet,
| “Ultra | high | definition HEVC | DASH | data | set,” in | Proc. 5th ACM |     |     |     |     |     |     |     |
| ------ | ---- | --------------- | ---- | ---- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
MultimediaSyst.Conf.(MMSys),2014,pp.7–12.[Online].Available: Christian Timmerer (M’08–SM’16) is an
http://doi.acm.org/10.1145/2557642.2563672 Associate Professor with Alpen-Adria-Universität
[186] J. J. Quinlan, A. H. Zahran, and C. J. Sreenan, “Datasets for Klagenfurt,Klagenfurt,Austria.HeisaCo-Founder
AVC (H.264) and HEVC (H.265) evaluation of dynamic adap- of Bitmovin Inc., San Francsico, CA, USA,
tive streaming over HTTP (DASH),” in Proc. 7th Int. Conf. as well as the CIO and the Head of Research
Multimedia Syst. (MMSys), 2016, pp.1–6. [Online]. Available: and Standardization. He has co-authored seven
http://doi.acm.org/10.1145/2910017.2910625 patents and over 190 publications in workshops,
[187] A. Zabrovskiy, C. Feldmann, and C. Timmerer, “Multi- conferences, journals, and book chapters. He
codec DASH dataset,” in Proc. 9th ACM Multimedia Syst. participated in several EC-funded projects, notably
Conf. (MMSys), 2018, pp.438–443. [Online]. Available: DANAE, ENTHRONE, P2P-Next, ALICANTE,
http://doi.acm.org/10.1145/3204949.3208140 SocialSensor, ICoSOLE, and the COST Action
| [188] J. J. | Quinlan | and C. J. | Sreenan, | “Multi-profile |     | ultra high defini- |                  |         |              |     |          |      |             |
| ----------- | ------- | --------- | -------- | -------------- | --- | ------------------ | ---------------- | ------- | ------------ | --- | -------- | ---- | ----------- |
|             |         |           |          |                |     |                    | IC1003 QUALINET. | He also | participated | in  | ISO/MPEG | work | for several |
tion (UHD) AVC and HEVC 4K DASH datasets,” in Proc. 9th years,notablyintheareas ofMPEG-21,MPEG-M, MPEG-V, andMPEG-
ACM Multimedia Syst. Conf. (MMSys), 2018, pp.375–380. [Online]. DASH.Hisresearchinterestsincludeimmersivemultimediacommunications,
Available:http://doi.acm.org/10.1145/3204949.3208130 streaming, adaptation, and quality of experience. He was the General Chair
|     |     |     |     |     |     |     | of WIAMIS 2008, | QoMEX 2013, | ACM | MMSys | 2016, | and | Packet Video |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | --- | ----- | ----- | --- | ------------ |
2018.Furtherinformationcanbefoundathttp://blog.timmerer.com.
|     |     |     |     |     |     |     |     | Roger    | Zimmermann  |         | (M’93–SM’07) |      | received the  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------- | ------------ | ---- | ------------- |
|     |     |     |     |     |     |     |     | M.S.     | and Ph.D.   | degrees | from         | the  | University of |
|     |     |     |     |     |     |     |     | Southern | California, |         | Los Angeles, | USA, | in 1994       |
and1998,respectively.HeiscurrentlyanAssociate
ProfessorwiththeDepartmentofComputerScience,
|     |     | Abdelhak | Bentaleb | received |     | the M.S. degree |     |     |     |     |     |     |     |
| --- | --- | -------- | -------- | -------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
in computing (network and multimedia) from NationalUniversityofSingapore(NUS),Singapore,
Mohamed El Bachir El Ibrahimi University, Bordj where he is also the Deputy Director with the
BouArréridj,Algeria,in2011.Heiscurrentlypur- SmartSystemsInstitute,andco-directedtheCentre
suing the Ph.D. degree in computer science with of Social Media Innovations for Communities. He
|     |     |            |     |            |          |            |     | has co-authored |     | a book, | seven | patents, | and over |
| --- | --- | ---------- | --- | ---------- | -------- | ---------- | --- | --------------- | --- | ------- | ----- | -------- | -------- |
|     |     | the School | of  | Computing, | National | University | of  |                 |     |         |       |          |          |
Singapore,Singapore.Hisresearchinterestsinclude 200 conference publications, journal articles, and
multimedia systems and communication, video book chapters. His research interests include streaming media architectures,
streamingarchitectures,contentdelivery,distributed distributed systems, mobile and geo-referenced video management, collab-
computing,computernetworksandprotocols,wire- orative environments, spatio-temporal information management, and mobile
location-basedservices.HeisaDistinguishedMemberoftheACM.Further
lesscommunications,andmobilenetworks.Further
informationcanbefoundathttps://www.comp.nus.edu.sg/∼bentaleb/. informationcanbefoundathttp://www.comp.nus.edu.sg/∼rogerz/.