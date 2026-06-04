Received24May2025,accepted17June2025,dateofpublication24June2025,dateofcurrentversion3July2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3582850
A Review of Learning-Based Methods for
Adaptive Video Streaming Over HTTP
HALAAMER,MOHAMEDS.HASSAN ,(Member,IEEE),
ANDMAHMOUDH.ISMAIL ,(SeniorMember,IEEE)
DepartmentofElectricalEngineering,AmericanUniversityofSharjah,Sharjah,UnitedArabEmirates
Correspondingauthor:MohamedS.Hassan(mshassan@aus.edu)
TheworkofHalaAmerandMahmoudH.IsmailwassupportedbyAmericanUniversityofSharjahthroughFacultyResearchunderGrant
FRG22-C-E13andGrantFRG23-C-E12.
ABSTRACT Adaptive video streaming offers enhanced Quality of Experience (QoE) by dynamically
adjusting the video quality to match network conditions and device capabilities. However, employing
effective video streaming systems is becoming more challenging as user demands for high quality and
low latency grow. The surge in video traffic is not only straining network resources but also causing a
decline in video quality. To address these challenges, machine learning algorithms leverage data-driven
techniques to optimize video delivery, improve QoE, and reduce network congestion. Although several
surveys exist on the role of machine learning in adaptive streaming, there remains a lack of an up-to-
date review that comprehensively covers the use of machine learning throughout all the stages of video
streamingandexplorespracticaldeploymentchallengesandopportunities.Thissurveyaddressesthisgap
by systematically categorizing and analyzing recent research on learning techniques applied to adaptive
videoencoding,bandwidthoptimization,andqualityadaptation.Emergingtrendsandopenchallengesare
identified,providingresearcherswithtimelyinsightsintohowlearningalgorithmscanbeusedtoshapethe
futureofadaptivestreamingsystems.
INDEXTERMS Adaptivevideostreaming,HTTP,learningmethods.
I. INTRODUCTION between each of these solutions, they share the same basic
Over the past two decades, video traffic has undergone a implementation.
tremendousamountofgrowth.Itnowaccountsformorethan InHTTPadaptivevideostreaming,videosareencodedat
65% of the Internet traffic [1]. This makes it challenging multiplebitratelevels(i.e.differentqualities)anddividedinto
but crucial to ensure optimal Quality-of-Experience (QoE) segmentsthatusuallyrangefrom1to10seconds.Amanifest
for video delivery. These issues motivated the introduction file-knownasaMediaPresentationDescription(MPD)file
of Hypertext Transfer Protocol (HTTP) adaptive streaming for DASH, as shown in Fig. 1- contains information about
(HAS).HAShasbecomethemostwidelyusedprotocolfor the available video representations, as well as the URLs of
videostreamingapplications,withseveralimplementations, each video segment. A video session is then initiated by
such as Microsoft’s Smooth Streaming (MSS), Apple’s the client by requesting the manifest file of a video, and
HTTP Live Streaming (HLS) [2], and Motion Picture an adaptive bitrate (ABR) algorithm is used to select the
Expert’sGroup’s(MPEG)DynamicAdaptiveStreamingover appropriate bitrate level for each video segment. Once the
HTTP (DASH) [3], which is the first international standard adaptationalgorithmdeterminesthebitratelevelofthenext
for adaptive streaming over HTTP that does not specify segment, the client sends to the server an HTTP request for
the adaptation logic. Although there are some differences thecorrespondingsegment.
AlthoughHASisthedominantapproachforvideodelivery
The associate editor coordinating the review of this manuscript and today, several open challenges remain. In the following
approvingitforpublicationwasAlessandroFloris . sections, we explore the technical challenges facing video
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
111134 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
Traditionalstreamingapproachesgenerallyfailtooptimize
|     |     |     |     |     |     |     | bandwidth | usage;  | inefficient |         | quality         | adaptation |     | algorithms |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----------- | ------- | --------------- | ---------- | --- | ---------- |
|     |     |     |     |     |     |     | do not    | account | for         | content | characteristics |            | and | greedily   |
selecthigherbitratesthatdonotalwaysresultinsubstantial
|     |     |     |     |     |     |     | quality | improvements. |     | Additionally, |     | available |     | computing |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------------- | --- | --------- | --- | --------- |
resourcesattheclientorserversideareoftenunder-utilized,
|     |     |     |     |     |     |     | increasing | the | pressure | on  | the | network. | Learning-based |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | --- | -------- | -------------- | --- |
methods,implementingintelligentadaptationandencoding,
|     |     |     |     |     |     |     | super-resolution |     | [6], and | caching, |     | can mitigate |     | these issues |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | -------- | --- | ------------ | --- | ------------ |
byoptimizingtrafficandresourceutilization.Usinghistorical
FIGURE1. DASHframework.
data,learning-basedtechniquescanalsobeusedtoaccurately
|     |     |     |     |     |     |     | predict network |     | conditions |     | [7], [8], | [9] | to further | improve |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --- | --------- | --- | ---------- | ------- |
qualityadaptationdecisions.
| streaming          | over | HTTP      | and | shed light on  | the key | aspects   |     |     |     |     |     |     |     |     |
| ------------------ | ---- | --------- | --- | -------------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| that substantially |      | influence |     | the efficiency | of      | streaming |     |     |     |     |     |     |     |     |
systems.Followingabriefdiscussionofexistingchallenges,
3) VIDEOQUALITYANDQoE
wehighlightthecontributionsinaddressingthesechallenges.
EnsuringhighvideoqualityanddeliveringasatisfactoryQoE
| This survey     | mainly |               | focuses | on current        | machine | learning- |             |           |             |     |             |            |            |           |
| --------------- | ------ | ------------- | ------- | ----------------- | ------- | --------- | ----------- | --------- | ----------- | --- | ----------- | ---------- | ---------- | --------- |
|                 |        |               |         |                   |         |           | remains     | a central | challenge   |     | in video    | streaming. |            | Since QoE |
| based solutions |        | aiming        | to      | enhance the       | overall | streaming |             |           |             |     |             |            |            |           |
|                 |        |               |         |                   |         |           | is used to  | guide     | the quality |     | adaptation  |            | algorithm, | building  |
| experience.     | In     | what follows, |         | we also highlight | the     | structure |             |           |             |     |             |            |            |           |
|                 |        |               |         |                   |         |           | an accurate | QoE       | model       | is  | extensively |            | researched | within    |
andorganizationofthissurvey.
|     |     |     |     |     |     |     | the literature | [10]. | However, |                  | quantifying |       | the user’s | viewing |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | -------- | ---------------- | ----------- | ----- | ---------- | ------- |
|     |     |     |     |     |     |     | experience     | in    | itself   | is a challenging |             | task. | Perception | of      |
A. CHALLENGESINVIDEOSTREAMING differentusersisinfluencedbytheirpreferencesintermsof
1) ENERGYEFFICIENCYINVIDEOSTREAMINGSYSTEMS
bothQoEandcontent.Althoughsubjectivequalitymeasures,
Energy consumption is a growing concern across the such as Mean Opinion Score (MOS), are considered the
| video streaming |     | pipeline, | from | encoding | and transcoding |     |                 |     |           |        |     |           |      |          |
| --------------- | --- | --------- | ---- | -------- | --------------- | --- | --------------- | --- | --------- | ------ | --- | --------- | ---- | -------- |
|                 |     |           |      |          |                 |     | most reflective |     | of users’ | actual |     | opinions, | such | measures |
operations at the server side to decoding and rendering on cannotbeusedforreal-timeQoEmeasurement.Rather,QoE
end-user devices. Viewers watch videos on a variety of is measured in terms of objective metrics, such as visual
devices,rangingfrommobilephonestoHDTVs,eachwith
quality(includingmetricssuchasstructuralsimilarityindex
differentscreenresolutions.Videoencodingthereforeneeds (SSIM),peaksignal-to-noiseratio(PSNR),andvideomulti-
tobeoptimizedtoensurethatviewerscanenjoythehighest
|     |     |     |     |     |     |     | method | assessment | fusion | (VMAF) |     | [11]), | smoothness, | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------ | ------ | --- | ------ | ----------- | --- |
possible quality on their respective devices. As such, HAS stalling duration. However, objective metrics such as PSNR
uses a ‘‘bitrate ladder’’, which refers to a set of bitrate- orSSIMoftenfailtofullycapturethesubjectiveexperience
| resolution | pairs. | As discussed |     | in Section | II, bitrate | ladders |             |              |     |      |          |     |            |         |
| ---------- | ------ | ------------ | --- | ---------- | ----------- | ------- | ----------- | ------------ | --- | ---- | -------- | --- | ---------- | ------- |
|            |        |              |     |            |             |         | of viewers, | particularly |     | when | it comes | to  | perceptual | quality |
determine the quality-bitrate trade-offs in adaptive stream- orusercontentpreferences.Inaddition,traditionalstreaming
| ing. Their | construction |     | can | be computationally |     | expensive, |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
frameworksuseafixedQoEmodelthatlackspersonalization
especially for 4K/8K videos, affecting energy efficiency. and disregards user preferences. This can result in poorer
Due to these encoding demands and limited computational viewing experience as users may prioritize different aspects
resources,somelivevideoplatforms,suchasTwitch,donot
ormetricsofQoE[12].Asaresult,MLisincreasinglybeing
provide multiple representations for all of their users [4], usedtomodelandpredictactualperceivedQoE,allowingfor
| which causes |     | degraded | QoE. | Data centers | and | content |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ---- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
content-awareanduser-centricadaptation.
deliverynetwork(CDN)nodesalsofaceincreasingpressure Therefore, learning techniques provide a wide range
to minimize power consumption while maintaining low- of solutions to improve video streaming, allowing for
| latency, | high-throughput |     | service. | To address | these | issues, |           |               |     |           |     |         |             |     |
| -------- | --------------- | --- | -------- | ---------- | ----- | ------- | --------- | ------------- | --- | --------- | --- | ------- | ----------- | --- |
|          |                 |     |          |            |       |         | efficient | and adaptable |     | encoding, |     | traffic | management, | and |
machine learning (ML) techniques are being proposed for quality adaptation. Compared to heuristic algorithms (e.g.,
energy-awarevideoencodingandqualityadaptation,aiming
|     |     |     |     |     |     |     | throughput-based |     | [13] | and | buffer-based |     | algorithms | [14], |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- | --- | ------------ | --- | ---------- | ----- |
toimproveenergyusagewithoutdegradinguserexperience.
|     |     |     |     |     |     |     | [15]), which | rely | on a | set of | fixed | rules, | ML methods | have |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---- | ------ | ----- | ------ | ---------- | ---- |
consistentlyshownbetterperformanceintheliterature;since
2) BANDWIDTHLIMITATIONS heuristicalgorithmsusepre-definedrulestomakedecisions
Furthermore, adaptive video streaming, while providing and typically optimize only for a specific set of conditions,
improved quality and user experience, can contribute to most of the research shows that they are unable to adapt to
excessive bandwidth consumption and video-related traffic. dynamicorunstableconditions,optimizeformultiplegoals,
Video-related traffic suffers from congestion, high costs, and handle the high-dimensional and non-linear decision
and high energy consumption [5], among other challenges. spaces involved in video streaming [16], [17]. In simulated
Therefore, it is crucial to develop methods for video traffic tests, learning techniques consistently outperform heuristic
optimization. methods across a wide range of tasks. However, recent
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 111135 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
|     |     | FIGURE2. | Surveyorganizationroadmap. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
research [18] illustrates that the performance of learning- Real-world algorithm implementation and evaluation
based algorithms rapidly degrades in real-world scenarios, toolsandplatforms,aswellasbenchmarkdatasetsand
evenbeingoutperformedbysimpleralgorithms,asprovenby algorithms,arealsoprovidedforresearchers’reference.
workslikeFugu[19].Wethereforepresentthissurveypaper A comprehensive overview of learning-based video
•
todiscusstherecentadvances,breakthroughs,andchallenges compressionandbitrateladderpredictiontechniquesis
inmachinelearning-basedvideostreamingtoaidresearchers provided. Bitrate ladder prediction methods are further
inunderstandinganddevelopingMLsolutionsthatcanbridge classified into three main groups: per-title, per-chunk,
thegapbetweensimulationsandreal-worlddeployment. andper-sceneencoding.Allthreemethodsareevaluated
andcomparedintermsofperceptualquality,complexity,
bandwidthefficiency,andencodingtime.
B. CONTRIBUTIONS
|     |     |     |     |     |     |     |     | • In-depth | analysis of learning-based |     | bandwidth |     | opti- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------------- | --- | --------- | --- | ----- |
Thisreviewpapermakesseveralsignificantcontributionsto
|     |     |     |     |     |     |     |     | mization | methods is carried | out. | Different | strategies | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | ---- | --------- | ---------- | --- |
thefieldofadaptivevideostreamingbyfocusingontheuseof
|     |     |     |     |     |     |     |     | reducing | video traffic and | bandwidth | wastage, |     | such as |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --------- | -------- | --- | ------- |
machinelearningtechniques.Itprovidesanextensivereview
intelligentqualityadaptationandencoding,caching,and
andevaluationofthestate-of-the-artlearning-basedmethods
videoqualityenhancement,areexplored.
| for adaptive | video     | streaming |               | applications, |             | including   | video |                  |         |            |            |     |          |
| ------------ | --------- | --------- | ------------- | ------------- | ----------- | ----------- | ----- | ---------------- | ------- | ---------- | ---------- | --- | -------- |
|              |           |           |               |               |             |             |       | • Learning-based | quality | adaptation | algorithms |     | are dis- |
| encoding,    | bandwidth |           | optimization, |               | and quality | adaptation. |       |                  |         |            |            |     |          |
cussedandevaluated.VariousmethodsofQoEmodeling
| Other review |     | papers | [20], | [21] do | not focus | on machine |     |     |     |     |     |     |     |
| ------------ | --- | ------ | ----- | ------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
andpredictionareintroduced,aswellaslearning-based
| learning-based |     | streaming | specifically |     | or only | discuss | select |     |     |     |     |     |     |
| -------------- | --- | --------- | ------------ | --- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
methodsforimprovingthegeneralizabilityofadaptation
| aspects  | of video | streaming |     | systems, | whereas    | this     | survey |             |              |         |            |            |     |
| -------- | -------- | --------- | --- | -------- | ---------- | -------- | ------ | ----------- | ------------ | ------- | ---------- | ---------- | --- |
|          |          |           |     |          |            |          |        | algorithms. | In addition, | quality | adaptation | algorithms |     |
| provides | a more   | holistic  |     | view,    | from video | encoding | to     |             |              |         |            |            |     |
areclassifiedbasedontheirapplication,includingvideo
| transmission |         | and processing. |       | While     | some   | recent | surveys |           |              |             |     |               |     |
| ------------ | ------- | --------------- | ----- | --------- | ------ | ------ | ------- | --------- | ------------ | ----------- | --- | ------------- | --- |
|              |         |                 |       |           |        |        |         | on demand | (VoD), live, | multi-user, | and | content-aware |     |
| have also    | covered | the             | video | streaming | system | in an  | end-to- |           |              |             |     |               |     |
videostreaming.
| end manner | [22], | [23], | they | lack | the inclusion | of essential |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | ---- | ---- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
• Theshortcomingsoflearning-basedstreamingschemes
| resources | for | video | streaming | research, | unlike | our | work. |     |     |     |     |     |     |
| --------- | --- | ----- | --------- | --------- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
areexploredintermsoftheirgeneralizability,real-world
| The main | contributions |     | of  | this | survey can | therefore | be  |              |              |             |     |         |       |
| -------- | ------------- | --- | --- | ---- | ---------- | --------- | --- | ------------ | ------------ | ----------- | --- | ------- | ----- |
|          |               |     |     |      |            |           |     | performance, | and security | challenges. |     | We also | delve |
summarizedasfollows:
|                    |       |     |               |            |           |              |     | into emerging | trends and   | new           | technologies |        | in video |
| ------------------ | ----- | --- | ------------- | ---------- | --------- | ------------ | --- | ------------- | ------------ | ------------- | ------------ | ------ | -------- |
| • State-of-the-art |       |     | learning      | techniques | are       | covered      | for |               |              |               |              |        |          |
|                    |       |     |               |            |           |              |     | streaming     | and identify | possibilities | for          | future | research |
| each               | stage | of  | the streaming |            | pipeline. | In addition, |     |               |              |               |              |        |          |
accordingly.
| the | streaming | process |     | and | its components | are | also |     |     |     |     |     |     |
| --- | --------- | ------- | --- | --- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
explained, providing a basic tutorial and introduction The rest of this survey is organized as illustrated in
tovideostreamingsystemsforresearchersinthefield. Fig. 2. Section II gives an overview of video encoding and
| 111136 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
|     |     |     |     |     |     |     | capabilities, | such | as content-aware |     | encoding | [28], | reduced |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ---------------- | --- | -------- | ----- | ------- | --- |
computationalcomplexity[29],andend-to-endoptimization
|     |     |     |     |     |     |     | of encoding   | pipelines.  |     | However,  | despite | their    | promising  |         |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | --------- | ------- | -------- | ---------- | ------- |
|     |     |     |     |     |     |     | performance,  | integrating |     | learned   | video   | coding   | frameworks |         |
|     |     |     |     |     |     |     | into existing | adaptive    |     | streaming | systems | presents |            | several |
challenges.Thesemodelsoftenhavehighcomputationaland
|     |     |     |     |     |     |     | memory               | requirements, | making        |            | them unable  | to                 | achieve     | real- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ------------- | ------------- | ---------- | ------------ | ------------------ | ----------- | ----- |
|     |     |     |     |     |     |     | time encoding        |               | performance   | [27],      | particularly | in                 | the case    | of    |
|     |     |     |     |     |     |     | neural network-based |               | schemes.      |            | The lack     | of standardization |             |       |
|     |     |     |     |     |     |     | and publicly         | available     | benchmarks    |            | and          | datasets           | for learned |       |
|     |     |     |     |     |     |     | codecs               | also limits   | their         | widespread | adoption     |                    | and hinders |       |
|     |     |     |     |     |     |     | research             | efforts.      | Standardized  |            | testbeds     | and                | lightweight |       |
|     |     |     |     |     |     |     | learned              | codecs        | are therefore |            | needed       | to transition      |             | these |
advancesintoproduction-leveladaptivestreamingsystems.
FIGURE3. Convex-hullconstruction.
|     |     |     |     |     |     |     | Several            | learned | codecs  | have     | been proposed |      | to address |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ------- | ------- | -------- | ------------- | ---- | ---------- | --- |
|     |     |     |     |     |     |     | these limitations. |         | Notable | examples | of            | such | frameworks |     |
ladder prediction techniques using learning-based methods. include DVC [30], which is the first end-to-end neural-
Research on using learning methods to optimize the bitrate enhanced encoding algorithm, now used as a benchmark
and resolution, as well as the encoding configuration. Sec- for other studies in the field. Reference [31] presents a
tionIIIdiscussesbandwidthoptimizationmethods.Methods
|     |     |     |     |     |     |     | comparative | benchmarking |     | study | of several | learned |     | video |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ----- | ---------- | ------- | --- | ----- |
ofreducingbandwidthwastage,suchasvideoenhancement, coding algorithms, including DVC, SSF [32], DCVC [33],
caching, and intelligent adaptation and encoding, are also and DVC-P [34]. The study shows that DCVC achieves
| the focus | of Section | III. | Section | IV presents | an  | outline |          |                 |     |             |     |          |     |        |
| --------- | ---------- | ---- | ------- | ----------- | --- | ------- | -------- | --------------- | --- | ----------- | --- | -------- | --- | ------ |
|           |            |      |         |             |     |         | the best | rate-distortion |     | performance | at  | the cost | of  | having |
of learning-based quality adaptation algorithms. Different the highest complexity, whereas SSF achieves the lowest
| methods | of QoE modeling |     | used | by adaptation | algorithms |     |            |     |           |     |                     |     |      |     |
| ------- | --------------- | --- | ---- | ------------- | ---------- | --- | ---------- | --- | --------- | --- | ------------------- | --- | ---- | --- |
|         |                 |     |      |               |            |     | GPU memory |     | occupancy | and | fastest performance |     | with | the |
are discussed. The implementation of quality adaptation second-best rate-distortion performance. Similarly, Google
algorithmsforvariousapplicationsisalsocovered,including DeepMind’sC3[35]isanotherlearnedvideocodingscheme
| single-user, | multi-user, | VoD, | and | live scenarios. | Section | IV  |     |     |     |     |     |     |     |     |
| ------------ | ----------- | ---- | --- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thattargetscomplexity,achievingsignificantlylowerdecod-
also explores content-aware quality adaptation, as well as ing complexity compared to similar learned frameworks by
| the use | of different | learning | techniques |     | to improve | the |     |     |     |     |     |     |     |     |
| ------- | ------------ | -------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
overfittingasmaller,lesscomplexmodeltoeachvideorather
performance and generalizability of adaptation algorithms. thandevelopingageneralizedencodingmodel.
Finally,SectionVidentifiesemergingtrendsandgapsinthe As research continues to improve the efficiency of
literatureandsuggestsdirectionsforfuturework.
|     |     |     |     |     |     |     | video encoding, |     | another | critical | component | of  | the encoding |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | -------- | --------- | --- | ------------ | --- |
process,bitrateladderconstruction,hasalsoseensignificant
II. VIDEOENCODING
|     |     |     |     |     |     |     | advancements |     | through | machine | learning | techniques. |     | In  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------- | -------- | ----------- | --- | --- |
Traditional hybrid video coding standards like adaptive video streaming, videos are encoded at multiple
H.264/AVC [24] and H.265/HEVC [25] have served as the resolutions and bitrates. The resolution and bitrate pairs,
| backbone | of modern | video | encoding | for | decades. | These |     |     |     |     |     |     |     |     |
| -------- | --------- | ----- | -------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
whichmakeupthebitrateladder,areselectedsuchthatusers
standardsarebasedonblock-basedhybridarchitecturesthat canreceivethebestpossibleviewingexperiencegiventheir
| include | modules for | intra/inter-frame |     | prediction, | exploiting |     |                       |     |     |         |             |     |           |     |
| ------- | ----------- | ----------------- | --- | ----------- | ---------- | --- | --------------------- | --- | --- | ------- | ----------- | --- | --------- | --- |
|         |             |                   |     |             |            |     | device specifications |     | and | network | conditions. |     | Commonly, |     |
the spatial and temporal redundancies of video content, rate-distortion(RD)curvesillustratetherelationshipbetween
transform coding, quantization, and entropy coding. How- the bitrate and the quality for each encoded resolution of a
ever,whilehighlyoptimizedandstandardized,thesesystems
|     |     |     |     |     |     |     | specific | video | sequence. | The | RD curve | for each | resolution |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | --- | -------- | -------- | ---------- | --- |
face growing limitations, particularly with the advent of peaksatacertainbitraterange,inwhichthisresolutionwill
4K/8K video. These systems do not learn from data and have the highest quality out of all the possible resolutions.
must be manually tuned for each content type, resolution, Joining these peaks results in the construction of a convex
or bitrate range. In addition, encoding decisions rely on hull, which indicates the ideal resolution-bitrate pairs as
fixedheuristics,whichdonotcapturesemanticorperceptual
|     |     |     |     |     |     |     | depicted | in Fig. | 3. Constructing |     | the | bitrate | ladder | then |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | --- | --- | ------- | ------ | ---- |
importance of video content. With each new standard, involves determining the cross-points along the RD curves.
compression gains also become harder to achieve without These cross-points are the points along the convex hull
increasing the complexity, making real-time encoding more at which the current resolution must switch to the next
| expensive[26],[27]. |         |          |     |            |               |     | resolution.    |     |               |     |              |      |     |       |
| ------------------- | ------- | -------- | --- | ---------- | ------------- | --- | -------------- | --- | ------------- | --- | ------------ | ---- | --- | ----- |
| Consequently,       | machine | learning |     | techniques | have increas- |     |                |     |               |     |              |      |     |       |
|                     |         |          |     |            |               |     | Traditionally, |     | fixed bitrate |     | ladders were | used | for | video |
inglybeensuggestedtoaddressthechallengesoftraditional encoding, but such approaches are either content-agnostic
encoding frameworks. Learning-based, or learned, video or employ a few fixed ladders based on video genre. They
coding frameworks have the potential to provide enhanced do not take into account the content characteristics of the
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 111137 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
FIGURE4. Typesofladderencodingtechniques.
video, which can often lead to degradation in video quality. real-timestreaming,whichrequiresaquickencodingprocess
For instance, video sequences with detailed textures and toachievesufficientlylowlatency.
dynamic content, such as action movies, require higher To address this challenge, learning techniques can be
encoding bitrates than those with static content, such as used to predict the optimal resolution-bitrate pairs for
talk shows. A one-size-fits-all approach therefore results in each video sequence. Several learning-based solutions have
compression artifacts in scenes with rapid motion and data recently been suggested for bitrate ladder prediction to
wastage when encoding static scenes. Research attempts to tackle the exhaustive encoding process involved in per-
tackle this issue through three main methods: per-title, per- title encoding [38], [39]. Learning techniques have been
scene(orper-shot),andper-chunk(orper-segment)encoding. deployed to this end in practice in an industry setting. For
These methods construct individual encoding ladders for example, Mux’s [40] instant per-title encoding uses deep
each video, scene, or chunk, respectively, based on actual learning(DL)topredictthebitrateladder.Similarly,another
videocontent,makingthemafarmoreeffectivesolutionthan per-titleencodingimplementationisproposedbyBitmovin,
fixedladders.Toexplorethesetechniquesandtestencoding whichanalyzesthecontentofeachvideosequenceanduses
configurations,toolssuchasFFmpeg[36]arewidelyusedin machine learning to predict the optimal encoding param-
bothindustryandresearchforencodingtasks(seeTable3for eters [41]. Recent research in the literature also includes
alistoftoolsandresourcesandTable2fordatasetsdeveloped Silhavyetal.’s[42]designofanML-basedper-titleencoding
forresearchonvideoapplications).Fig.4showsasummary schemethateliminatestheneedforexhaustivetestencodes.
ofthethreeencodingladderconstructiontechniques,which Theirapproachusesseveralsupervisedlearningalgorithms,
arediscussedinfurtherdetailinthissection. includingmulti-layerperceptronaswellassupportvectorand
randomforestregression,topredicttheoptimalbitrateladder.
A. PER-TITLEENCODING Adhuran and Kulupana [43] propose a machine learning-
In order to address the limitations of fixed encoding based approach for per-title encoding that predicts target
ladders,recentresearchattemptstointroducecontent-aware bitrates from the compressed video features. In contrast,
encodingsolutions,suchasNetflix’sper-titleencoding[37], Katsenouetal.[44]usemachinelearningforcontent-aware
which encodes each video sequence at different bitrate and bitrate ladder prediction using extracted features from the
resolution pairs in order to construct the convex hull of uncompressed video sequence. In [38], the authors also use
the rate-distortion curves based on their VMAF perceptual the video’s spatio-temporal features to predict the cross-
video quality metric. The convex hull then determines the over quantization parameters (QPs) using Gaussian process
bitrateladder.However,per-titleencodingcomesatthecost regression,afterwhichonlytwoencodespercross-overpoint
of increased computation; a high number of pre-encodes is are used to determine the bitrate ranges for each target
required to build the bitrate ladder, as each video sequence resolution.Theyexpanduponthisworkin[45]bymodeling
isencodedatallresolutionsandquantizationlevelsexhaus- the relationship between QPs and bitrates across different
tively to determine the optimal encoding configuration. In resolutions to predict the bitrate ladder. Reference [46] also
addition,carryingoutexhaustivepre-encodesisinfeasiblein addresses the issue of latency and energy consumption in
111138 VOLUME13,2025

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
per-titlevideoencoding,proposingLADRE,alatency-aware number of frames between two intra-coding frames within
scheme based on the random forest algorithm. LADRE avideosequence.Inthisway,theideaistofindtheoptimal
selects the encoding resolution based on the target bitrate IPSthatbalancescompressionefficiencywithvideoquality,
andlatency,aswellasthecontentspatiotemporalfeatures.In minimizingtheRD-COSTforscreencontentvideos.
another notable work, Nasiri et al. [47] design an ensemble Another challenge faced by per-title encoding of large
learning scheme for per-title encoding that aggregates the bitrate ladders is that it requires a large amount of storage.
output of multiple machine learning algorithms to compute One notable work that addresses the high cost of per-
the optimized encoding ladder. In case the outputs of the title encoding is developed in [52], based on the fact
algorithms differ, additional test encodings are performed, that it is common for users sharing the same network to
andtheresolutionthatproducesthehighestqualityisselected have devices with a wide range of capabilities, leading to
for each bitrate. This way, the strengths of each type of increasedstoragecostsasmorerepresentationsareprovided
learning algorithm are leveraged while reducing the impact for different types of devices. The authors propose the use
oftheirweaknessesontheoutput.However,theeffectiveness of a scalable scheme, DeepStream, to support all users
of such an approach for live or real-time streaming may while reducing the streaming costs. This scalable scheme
be limited, depending on the computation time required addsacontent-awaresuper-resolutionneuralnetwork-based
by the ML algorithms. This scheme also requires a higher enhancement layer to the existing bitrate ladder for devices
computationalcost. with GPU capabilities. Users with no GPU capabilities
While most of the literature is devoted to adapting the receive the base layer, which is the video bitstream at
resolution and bitrate of the video representations on the the representations available on the bitrate ladder, while
encoding ladder, some works propose the adaptation of users with sufficient computational capabilities receive an
other encoding parameters as well. One such work [48] enhancementlayer,whichincludesboththebaselayeraswell
proposes the use of machine learning for bitrate ladder asasuper-resolutionneuralnetworkforeachrepresentation,
estimation at a lower computational cost. Encoders have compressed using DeepCABAC [53]. Few other works
differentconfigurations,orpresets,thattradeoffcompression addressthisaspectofper-titleencoding,however.
efficiency for compression speed. The fastest preset of an
encoder is the one with the lowest compression efficiency,
andviceversa.In[48],thebitrateladderfortheslow(high- B. PER-SCENEENCODING
efficiency) preset of a given encoder is built by predicting Despite the improvement of per-title approaches over tradi-
its cross-over points using decision tree algorithm, given tional encoding schemes, generating a single bitrate ladder
the cross-over point bitrates of the fast (low-efficiency) for the entire video sequence may still lead to degraded
preset. This approach therefore manages to combine both perceptual quality and bandwidth inefficiency, especially
speed and efficiency for encoding ladder prediction with in videos with dynamic scene changes. This is because
lower computational demands. The authors in [49] propose high complexity scenes require higher bitrate allocation
a similar encoding scheme using random forest regression as compared to low complexity scenes, which can be
butadditionallyintroduceacross-codecapproachthatallows represented at an acceptable visual quality using less bits.
the fast preset configuration of a certain encoder to be used Consequently, using per-title encoding may not only lead
to predict the optimal configuration of another encoder. An to sub-optimal visual quality but to inefficient bandwidth
alternative per-title approach is proposed in [50], which utilization,aswell.
usesimitationlearningtojointlyoptimizetheresolutionand Per-sceneorper-chunkencodingarethemainalternatives
chunkduration,formingtheresolution-duration(RD)ladder. to per-title encoding introduced in the literature [54], [55],
Duringthetranscodingprocess,thisschemeaccountsfornot [56]. Per-scene encoding involves predicting the bitrate
onlythevideocontentbutthenetworkcapacityandstorage ladder for each video scene, which consists of one or
costs as well. By varying the chunk duration based on the more segments. Each video scene consists of a duration of
videocontent,greaterencodingefficiencycanbeachieved. the video throughout which there is no significant change
Similarly, encoding parameters other than bitrate and in content complexity. Therefore, encoding the video on
resolution are also targeted in the literature to account for a per-scene basis results in improved visual quality and
different types of videos. For example, different coding bandwidth efficiency. Such encoding approaches are now
schemes may be required for screen content video, which being practically implemented by some video streaming
referstovideosthatprimarilyconsistofcomputer-generated services, such as Netflix’s per-shot encoder [57]. However,
content,suchastext,graphics,animations,ordesktopscreen an exhaustive approach is still commonly used for bitrate
recordings.Incontrasttotraditionalcamera-capturedvideo, ladder generation, which is addressed in recent research
screencontentvideoshavedistinctcharacteristicslikesharp throughtheuseofmachinelearning.
edges,uniformareas,rapidscenechanges,andsoon,which Naturally, before encoding begins, this method first
traditionalcodingschemesstruggletohandleefficiently.This requires scene detection and analysis, which is approached
challenge motivates thework presented in [51], whichaims in several ways in the literature. Deep Encode [54] is
to dynamically adjust the intra-period size (IPS), i.e., the one implementation proposed by Mueller et al., which
VOLUME13,2025 111139

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
is a learning-based encoding framework that uses feature apre-determined,fixeddurationofvideo,independentofthe
extractiontopredicttheencodingladderforeachscene,thus type of video content. Per-chunk encoding is based on the
reducing bandwidth requirements. FAUST [58] is another assumption that each video segment generally has the same
per-scene encoding solution that uses entropy-based scene contentcomplexitythroughoutitsduration,duetosegments
detectionandaneuralnetworktopredicttheoptimizedbitrate usually being less than 10 seconds long. As such, many
ladder.Anotherapproachusesthediscretecosinetransform works [65] tend to choose per-chunk encoding over per-
(DCT)energyofthefirstgroupofpictures(GOP)fromeach sceneencoding,inordertoskipthescenedetectionstep.One
scene for complexity analysis within a per-scene encoding such approach in [55] also attempts to simplify the content
frameworkforlivestreaming[56]. analysis step. It uses a deep reinforcement learning (DRL)
After scene detection, the bitrate ladder is then encoded framework for per-chunk bitrate ladder prediction based on
in the same way as per-title encoding, but for each scene video content, network capacity, and storage cost (refer to
rather than each video. Several techniques are proposed in Table1forabriefexplanationofrelevantmachinelearning
the literature for the scene encoding step, such as the use methods).However,thecontentofeachsegmentisanalyzed
of recurrent convolutional networks to predict the convex by examining only the I-frame, which may not necessarily
hull [59]. Xing et al. also use a deep learning approach berepresentativeoftheentiresegment,particularlyiflonger
to predict the optimal constant rate factor (CRF) for a segment durations are used. Another recent work on per-
certain target VMAF for each video scene [60]. CRF is chunk encoding is proposed in [66]. The authors design a
an encoding method by which the quality is kept constant deepneuralnetworkthatpredictstheCRFforagiventarget
through adjusting the bitrate based on the video content. VMAFvaluebasedonthevideosegmentfeatures.
Therefore, by adjusting the CRF, both the perceived quality In the case of live streaming, low-latency coding
and compression efficiency can be improved. In another approaches are required to maintain high QoE. As such,
neural network-based approach, [61] makes use of transfer encodingefficiencycanbesacrificedforspeed;forexample,
learning to reuse pre-trained deep neural networks (DNNs), one-pass encoding is often used rather than two-pass
allowing the construction of the bitrate ladder with limited encoding. In one-pass encoding, the encoder processes the
training data. This per-scene scheme predicts the minimum content in one ‘‘pass’’, quickly allocating bitrate based on
bitrate required to achieve the highest quality level on information about the current and past frames. Two-pass
the bitrate ladder, essentially preventing bitrate wastage encoding,ontheotherhand,involvesaninitialpasstoanalyze
with only a slight reduction in quality. In [62], a vision video content over the whole duration, then a second pass
transformer is used instead for bitrate ladder prediction. for bitrate allocation, making it more efficient but slower.
Alternatively, the authors in [63] used machine learning Intuitively, one-pass encoding is more suitable to meet the
classifiers to predict the optimal resolution for each bitrate low-latencyrequirementsoflivestreaming,meaningthatlive
without the need for multiple test encodes. Reference [64] streams are often encoded inefficiently. A recent work that
presentsabenchmarkingstudycomparingdifferenttypesof successfully addresses this problem presents ETPS [39], a
ML techniques for per-scene ladder construction, including two-pass encoding scheme for live streaming that improves
several ML and DL models. Their results show that ML compression efficiency while maintaining the required low
modelsoutperformDLmodels,possiblyduetothesmallsize latency. ETPS uses the spatial and temporal complexity
ofthetrainingdataset,withtheextratreesregressorachieving based on the DCT energy of the first GOP of a segment
thebestperformance. todeterminetheoptimizedCRF.Otherapproachessimilarly
The content-aware nature of these per-scene encoding attempttoimprovetheprocessoflivevideocodingbytaking
approachesresultsinimprovedcodingefficiencyandvisual advantage of other encoding parameters. In order to meet
quality. By constructing a different encoding ladder for stringentlatencyandqualityrequirements,theseapproaches
eachindividualscene,lowcomplexityscenesdonotreceive optimize the video encoding configuration. The authors
unnecessarily high bitrates, while high complexity scenes in [67] analyze the relationship between various encoding
receive sufficient bitrates to achieve a high perceptual parameters (such as the number of frames per second and
quality. However, the time taken for scene detection and encodingspeed)andvideoperceptualquality;theyfindthat
complexity analysis, followed by bitrate ladder prediction, varyingtheencodingconfigurationratherthanjustadjusting
results in added delay for per-scene approaches, which theresolutionorbitratecanachieveacceptablelevelsofboth
may be unacceptable especially in live streaming scenarios. latencyandvideoquality.Basedontheiranalysis,theydesign
Furthermore, the cost of per-scene encoding outweighs the a reinforcement learning (RL)-based scheme for optimizing
benefitsinvideosequenceswithfewscenechanges. encoding configuration in real-time video streaming with a
client-sidesuper-resolutionalgorithmtofurtherimprovethe
videoquality.
C. PER-CHUNKENCODING Bothper-sceneandper-chunkencodingschemesresultin
An alternative approach to per-title and per-scene methods, significant bitrate savings compared to per-title encoding,
per-chunk encoding, involves bitrate ladder prediction on a particularly in video sequences with highly dynamic scene
per-chunk,orper-segment,basis,whereeachchunkissimply changes. Using per-chunk encoding in particular avoids the
111140 VOLUME13,2025

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
TABLE1. Descriptionofrelevantlearningalgorithms.
processofscenedetection,whichresultsinadditionaldelay. bitrate does not necessarily mean increasing the quality;
Itsquickerimplementationmakesper-chunkencodingmore while the quality increases linearly for a specific range of
suitable for live streaming scenarios. On the other hand, bitrates,increasingthebitratefurtheroutsidethelinearrange
scene changes may occur within the duration of the chunk, doesnothaveanoticeableeffectonvideoquality[68].Intyp-
particularlyinvideoswithlongerchunkdurations,leadingto ical adaptive bitrate algorithms, higher bitrates are selected
sub-optimalbitrateusageandperceptualqualityifper-chunk greedily,increasingenergyanddataconsumptionwithoutany
encodingisused. perceivable increase in quality. Turkkan et al. [68] design a
|     |     |     |     |     |     | deep Q-learning | (DQL)-based |           | ABR algorithm, |      | GreenABR,   |
| --- | --- | --- | --- | --- | --- | --------------- | ----------- | --------- | -------------- | ---- | ----------- |
|     |     |     |     |     |     | to address      | this. Their | framework | reduces        | data | consumption |
III. BANDWIDTHOPTIMIZATION
|               |         |             |     |          |             | due to | video streaming | while | maintaining | high | QoE by |
| ------------- | ------- | ----------- | --- | -------- | ----------- | ------ | --------------- | ----- | ----------- | ---- | ------ |
| Video-related | traffic | constitutes | the | majority | of Internet |        |                 |       |             |      |        |
traffic, and as a result, the growing demand for ultra-high- adding an energy penalty to the learning model’s reward.
|            |             |     |            |     | 360◦      | As a result, | GreenABR | manages | to significantly |     | improve |
| ---------- | ----------- | --- | ---------- | --- | --------- | ------------ | -------- | ------- | ---------------- | --- | ------- |
| definition | (UHD) video | and | the advent | of  | streaming |              |          |         |                  |     |         |
hasledtoincreasedbandwidthrequirements.Consequently, bandwidth efficiency and reduce energy consumption com-
efficiently utilizing the available bandwidth has become pared to state-of-the-art algorithms such as Pensieve [16]
whileachievingcomparableQoE.Otherresearch[69]utilizes
| one of the | core challenges | for | video | streaming. | Traditional |     |     |     |     |     |     |
| ---------- | --------------- | --- | ----- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
approaches to video streaming, often relying on fixed measures such as VMAF to ensure the selection of bitrates
|             |             |                 |     |            |             | that result | in an appreciable |     | improvement | in quality. | Such |
| ----------- | ----------- | --------------- | --- | ---------- | ----------- | ----------- | ----------------- | --- | ----------- | ----------- | ---- |
| rules, fail | to adapt to | the variability |     | of network | conditions. |             |                   |     |             |             |      |
Consequently,substantialdatawastageoccursduringperiods perceptual quality-aware streaming approaches ensure that
of ample bandwidth, while sub-optimal quality during high bitrates are not unnecessarily selected without any
visiblevisualimprovement.
networkcongestionreducesusersatisfaction.Toaddressthis
| issue, learning | techniques | have | emerged |     | as an alternative |     |     |     |     |     |     |
| --------------- | ---------- | ---- | ------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
approachtointelligentlyutilizeavailablenetworkbandwidth
2) BUFFER-AWAREQUALITYADAPTATION
andreducedatawastage.Theirabilitytolearnfromhistorical
|          |              |           |         |      |                 | Aside from | perceptual | quality, | another | factor | that can be |
| -------- | ------------ | --------- | ------- | ---- | --------------- | ---------- | ---------- | -------- | ------- | ------ | ----------- |
| patterns | and adapt in | real-time | enables | them | to tailor their |            |            |          |         |        |             |
targetedtooptimizebandwidthusageisthebufferoccupancy.
actions to varying network conditions. This section delves Some works do this through optimizing the pre-fetching
| into the | use of learning-based |     | methods |     | to optimize video |     |     |     |     |     |     |
| -------- | --------------------- | --- | ------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
decision.Greedilyrequestingvideochunksandfillingupthe
streamingtrafficwithoutcompromisingperceptualquality.
|     |     |     |     |     |     | playback | buffer can   | result  | in inefficient | bandwidth | usage.      |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ------- | -------------- | --------- | ----------- |
|     |     |     |     |     |     | Although | pre-fetching | content | can reduce     | the       | risk of re- |
A. INTELLIGENTADAPTATIONANDENCODING bufferingandimprovetheQoE,itcanleadtodatawastageif
1) PERCEPTUALLY-AWAREQUALITYADAPTATION theuserstopswatching.ThisisaddressedinQianetal.’swork
Inadaptivestreaming,videosareencodedatmultiplebitrates on DAM [70]. DAM is a short video streaming framework
which make up the bitrate ladder. A lower bitrate generally forreducingdatawastageduetopre-fetching.ItsDRL-based
correspondstolowervideoquality.However,increasingthe ABR algorithm is responsible for selecting the video chunk
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     | 111141 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
to be downloaded, its bitrate, and the pause time, during the encoding process. ViSOR operates by optimizing the
whichdownloadingispaused.Asimilarapproachisproposed resolution for each target bitrate, given a maximum latency
in [71], which uses multi-agent RL with expert guidance, threshold.Therandomforestalgorithmisusedtopredictthe
dividing the pre-fetching and bitrate decisions between two qualityachievedafterapplyingsuper-resolution,eliminating
differentagentssequentially.Theauthorsin[72]alsoattempt redundant representations that do not improve perceptual
to reduce traffic wastage through buffer management in quality past the JND threshold. In this way, the encoding
theirdesignofatransformer-basedmodelforpredictingthe energy is reduced significantly while remaining within
transmissiontimeofvideodata.Thispredictionisthenused acceptable latency bounds and maintaining the perceptual
to control both the selected chunk quality and waiting time quality. However, such implementations assume that client
betweenchunkdownloads.Thisway,thebufferisnotfilled deviceshaveGPUcapabilitiesandareabletocarryoutreal-
upblindly,whichisparticularlyessentialinthecaseofshort timesuper-resolution,whichiscertainlynotalwaysthecase.
videostreaming. Nonetheless,it isa firststep inthe directionof energy-and
Other research addresses the problem of bandwidth bandwidth-efficientvideocoding.
optimizationthroughbuffermanagement.Inadequatebuffer
| size can | also lead to data | wastage | as  | a result | of viewer |     |     |     |     |     |     |     |     |
| -------- | ----------------- | ------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
B. SUPER-RESOLUTION
abandonment.Whenviewersabandonthevideoearlyorskip
|     |     |     |     |     |     | Super-resolution |     | (SR) | is the | process | of  | enhancing | the |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- | ------ | ------- | --- | --------- | --- |
ahead,thepre-fetcheddatathathasalreadybeendownloaded
|     |     |     |     |     |     | resolution | of  | an image | to construct |     | a high | resolution |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------------ | --- | ------ | ---------- | --- |
iswasted.Tomitigatethisproblem,Huangetal.[73]design
|             |                |           |     |     |            | (HR) image | from  | the           | one of | low resolution |     | (LR). | In the |
| ----------- | -------------- | --------- | --- | --- | ---------- | ---------- | ----- | ------------- | ------ | -------------- | --- | ----- | ------ |
| DeepBuffer, | a buffer-aware | DRL-based |     | ABR | algorithm. |            |       |               |        |                |     |       |        |
|             |                |           |     |     |            | case of    | video | applications, | the    | ‘‘images’’     |     | refer | to the |
DeepBufferselectsboththevideobitrateaswellasthemax-
|     |     |     |     |     |     | video frames | instead. |     | Single-image | super-resolution |     |     | (SISR) |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------ | ---------------- | --- | --- | ------ |
imumbufferoccupancyforthenextsegment.Reference[74]
|     |     |     |     |     |     | involves | reconstructing |     | HR video | frames | on  | an individual |     |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | -------- | ------ | --- | ------------- | --- |
proposesasimilarDRL-basedABRalgorithmspecificallyto
|     |     |     |     |     |     | basis. Video | super-resolution |     |     | (VSR), | on the | other | hand, |
| --- | --- | --- | --- | --- | --- | ------------ | ---------------- | --- | --- | ------ | ------ | ----- | ----- |
improvetheenergyefficiencyofstreamingover5Gnetworks.
|                  |                    |            |            |      |               | also leverages |         | temporal | information      |          | across    | consecutive   |       |
| ---------------- | ------------------ | ---------- | ---------- | ---- | ------------- | -------------- | ------- | -------- | ---------------- | -------- | --------- | ------------- | ----- |
| These approaches | ensure             | that       | the buffer | size | is optimized  |                |         |          |                  |          |           |               |       |
|                  |                    |            |            |      |               | frames to      | improve | the      | super-resolution |          | accuracy. | As            | such, |
| according        | to current network | conditions |            | and, | consequently, |                |         |          |                  |          |           |               |       |
|                  |                    |            |            |      |               | SR techniques  |         | present  | an effective     | solution |           | for improving |       |
bandwidthwastageduetopre-fetchedcontentisreduced.
|     |     |     |     |     |     | visual quality | in  | image | and video | applications. |     | This | means |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --------- | ------------- | --- | ---- | ----- |
thattheycanalsobeleveragedtoreducevideotraffic.Rather
|     |     |     |     |     |     | than requesting |     | high | video bitrates | directly |     | from the | video |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | -------------- | -------- | --- | -------- | ----- |
3) JND-BASEDENCODING
server,SRtechniquescanbeutilizedtoenhancethequality
Asimilarconceptcanbeappliedduringthevideoencoding
|          |               |             |     |            |          | of low-quality |          | chunks | after transmission, |     | thus      | reducing | the     |
| -------- | ------------- | ----------- | --- | ---------- | -------- | -------------- | -------- | ------ | ------------------- | --- | --------- | -------- | ------- |
| stage as | well. Section | II explains | the | principles | of video |                |          |        |                     |     |           |          |         |
|          |               |             |     |            |          | bandwidth      | required |        | for streaming.      | The | potential |          | of this |
codingandbitrateladderconstruction.Here,wealsoprovide
|     |     |     |     |     |     | technique | has motivated |     | a significant | amount |     | of research | in  |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------------- | ------ | --- | ----------- | --- |
abriefoverviewofrecentworksonvideocodingwhichare
recentyears,includingindustry-drivenresearchefforts,such
| targeted | toward reducing | bandwidth | wastage. |     | These works |     |     |     |     |     |     |     |     |
| -------- | --------------- | --------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
asAmazon’sSUPERVEGAN[79].Inthissection,weexplore
| make use | of several methods | to  | achieve | their | goal, such as |           |       |      |           |            |     |      |          |
| -------- | ------------------ | --- | ------- | ----- | ------------- | --------- | ----- | ---- | --------- | ---------- | --- | ---- | -------- |
|          |                    |     |         |       |               | the types | of SR | used | for video | streaming, | as  | well | as their |
theJustNoticeableDifference(JND).JNDisaqualitymetric
drawbacksandchallenges.
thatmeasurestheminimumvisualperceivabledifferenceby
| the human | eye. Some | research | [75] | is dedicated | to JND |     |     |     |     |     |     |     |     |
| --------- | --------- | -------- | ---- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
prediction, which presents another challenge on its own. 1) SINGLE-FRAMESUPER-RESOLUTION(SFSR)
Usingencodingladderswithnoperceivablevisualdifference Several works use SISR for video quality enhancement,
between each quality level leads to data wastage. As such, as described above [80], [81], [82], [83]. In this method,
recentworksaimtodesignJND-awareencodingalgorithms. eachvideoframeisenhancedindividually,soitissometimes
The authors in [76] propose an ML-based per-title alsoreferredtoasper-frameorsingle-frameSR.Well-known
encoding scheme based on JND. This framework uses SISRmodelsoftenusedintheliteratureincludeSRCNN[84],
support vector regression to predict the JND and generates ESPCN [85], RDN [86], RFDN [87], and ESRGAN [88].
an encoding ladder with constant JND intervals. Similarly, When used for video super-resolution, such methods have
another model, MCBE [77], aims to reduce the energy the potential to greatly reduce the bandwidth required for
consumption of adaptive video streaming by optimizing the video streaming. In an earlier work that utilizes SFSR,
bitrateladdersofdifferentvideocodecs.Itemploystheran- Yeo et al. [80] design a content-aware scheme that trains
domforestalgorithmtopredictthevideoquality,represented several SR networks for different genres of video content.
bytheVMAFscore,ofdifferentbitrate-resolutionpairsand Through the use of content-aware SR, their framework
eliminatestheredundantrepresentationsthatdonotenhance achieves significant bandwidth savings while maintaining
perceived video quality beyond a certain JND threshold. perceptualquality.
Another JND-based scheme is ViSOR [78], a video super- While SFSR has a simpler processing pipeline com-
resolution-awareonlineschemethattakesadvantageofclient pared to multi-frame super-resolution, applying a super-
computingcapabilitiestoreducetheenergyconsumptionof resolution model to every frame independently can become
| 111142 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
computationally expensive and resource-intensive for real- use deep neural networks, such as CNNs and transformers,
time video applications, especially on devices with limited whichinvolvenumerousparametersandrequireheavycom-
computational capabilities, such as mobile devices. Recent putationslikematrixmultiplications.Assuch,clientdevices
studies show that SFSR requires significantly more energy areoftenincapableofimplementingreal-timeSR,especially
and computational resources, causing excessive heat dis- those devices that do not have GPU capabilities [95]. The
sipation and shorter battery life on mobile devices [89]. adventofedgecomputinghasprovidedapotentialsolutionto
Furthermore, SFSR fails to leverage temporal dependencies thisissue;edgeservershavefarmoreadvancedcapabilities,
betweenvideoframes,whichcanresultinrepetitivecompu- making them suitable for carrying out computationally
tation,temporalinconsistencies,anddegradedquality.These expensivetaskssuchasSR.
limitationshavemotivatedthedevelopmentofmoreefficient Takingadvantageofedgecomputing,manyrecentworks
reference-basedormulti-frameSRmethodstailoredforvideo implement SR at the edge server [83], [96], [97], [98],
applications. [99], [100], [101], [102]. Reference [96] presents a DRL-
based scheme, in which video enhancement takes place at
the mobile edge computing (MEC) server to reduce the
2) MULTI-FRAMESUPER-RESOLUTION(MFSR)
computationalloadontheclient.Anotherapproachpresented
In contrast to SFSR, many video streaming frameworks
byFilhoandMelo[97]usesSRattheedgeservertoupscale
use multi-frame SR instead [89], [90], [91], [92], which
LRvideosandstorethemalongwiththegeneratedSRvideos.
typically exploits information from multiple frames to
Agenerativeadversarialnetwork(GAN)isusedtoperform
enhanceresolution,therebyimprovingtemporalconsistency
SR in this work. GANs consist of a generative network-
and overall visual quality. Additionally, MFSR exploits
which is trained to generate SR images from LR images
temporal redundancy to reduce computation time, making
and reduce the difference between the SR and HR ground
it more suitable for real-time quality enhancement. For
truthimagesasfaraspossible-andadiscriminator network-
example, NEMO [89] is a well-known SR framework that
whichistrainedtodifferentiatebetweensyntheticSRframes
leveragesinter-framedependenciestoupscaleordinaryvideo
and HR frames. One noteworthy work that leverages edge-
frames based on a set of reconstructed SR frames known
assisted SR is presented in VISCA [98]. VISCA is a joint
as anchor points. Using this scheme, the QoE, as well as
SRandcachingschemethatmakescachingdecisionsbased
the device processing throughput, energy consumption, and
on video popularity and potential SR enhancement. It then
temperature, can be improved and maintained at acceptable
enhances the quality of low quality cached content at the
levels.Similarly,Shenetal.presentPASS-Net[91],another
edgeusingFRVSR[103].Inordertoaccountforavailability
MFSR model for adaptive streaming. PASS-Net is a joint
of edge resources, VISCA’s ABR algorithm selects the
frame prediction and enhancement framework for the cases
next segment resolution and decides whether to retrieve the
of lost frames and received low-resolution frames. Frame
segment from the origin server or edge cache, or to apply
prediction uses previous high-resolution frames in order to
super-resolutiontoaLRversion.
predictlostframes,whileframeenhancementusesreference-
However, such edge-based approaches will naturally
basedsuper-resolution.
increase the demand on the edge server and may waste
In [92], the authors implement and adapt several image
the computational capacity of more high-end devices. As
SR models (EDSR [93], RDN [86], and RCAN [94]) for
such,practicaldeploymentofsuchedge-assistedSRschemes
videoSRandproposealearning-basedensemblemethodthat
remainsscarce.ThisisaddressedinLiuetal.’sworkin[100].
uses the outputs of each SR method. Rather than applying
Their work takes advantage of both edge server and client
SR on a frame-by-frame basis using 3D convolutional
computing resources to perform super-resolution, with a
neural network (CNN), which is computationally intensive,
DRL-basedABRalgorithmthatselectsthevideoresolution,
the authors suggested using 2D CNN on a super image
reconstructed resolution, and client workload share. In their
consisting of concatenated video frames. Another MFSR-
framework, the server uses a large SR model to reconstruct
based scheme [90] named BiSR takes advantage of the fact
videotileswithlowPSNR,whilehighPSNRvideotilesare
thatkeyframesarelargerthannon-keyframes.Itdownscales
reconstructedbyalightweightSRmodelattheclient-side.
and applies SR to only key frames then encodes dependent
non-key frames at a high resolution. Thus, the transmission
overheadisreducedwithoutreducingthequality.BiSRalso
4) LIVESUPER-RESOLUTION
trains several video-specific overfitting neural networks of
Furthermore,super-resolutioncanalsobeusedtoreducethe
differentsizes.
streamingbitrateinlivestreamingscenarioswhileimproving
the video quality. Kim et al. leverage super-resolution for
3) EDGE-ASSISTEDSUPER-RESOLUTION live streaming, in which the video stream’s quality often
Despite the immense potential of SR for simultaneously depends on the streamer’s network conditions. To address
improving video quality and reducing streaming traffic, thisissue,theauthorsdevelopLiveNAS[104],aserver-side
itfacesseveralchallenges,ofwhichperhapsthemostcritical online super-resolution live video framework that enhances
is its high computational requirements. Most SR methods live video quality regardless of the available ingest-side
VOLUME13,2025 111143

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
bandwidth.UsingLiveNAS,livevideostreamsareuploaded enhancement improves the PSNR and reduces computation
at low resolution, and the server-side SR network then time compared to SR. Thus, such methods may prove more
enhancesthevideoframes,resultinginsignificantbandwidth suitableforstreamingondeviceswithlimitedcomputational
savings. Similarly, some works [99], [101] leverage edge capabilities.
computing to implement low-latency SR. In LiveSR [99], Moreover,enhancement-unawareABRframeworkspresent
a low-resolution representation of each video segment is another challenge for SR-assisted streaming schemes. Most
transmittedfromthevideoservertotheedgeservers,where of the current literature designs VSR models independently
the segment is reconstructed at a higher resolution using from the ABR algorithm, where video enhancement is
ESPCN [85]. The video segment is then transcoded into not accounted for during bitrate selection. This results in
multiple qualities to allow ABR selection at the client side, wasted bandwidth, as ABR algorithms may request chunks
resultinginnotablebandwidthsavingsaswellasQoEgains. with unnecessarily high bitrates when SR resources are
available.Therefore,integrationofSRorimageenhancement
5) VIDEOSUPER-RESOLUTIONCHALLENGES with ABR algorithms is essential and has recently received
Although significant strides have been made in the field of more attention in research [83], [102], [106], [107], [109],
super-resolution,videosuper-resolutionstillfacesnumerous [110], [111], [112]. For example, SuperABR [83] is a
challengesthatstandinthewayofwidespreadimplementa- recent edge-based framework combining bitrate adaptation
tion.Device-dependenceisonesuchfactorthatsignificantly withqualityenhancement.Itutilizesaqueue-learning-based
reduces the effectiveness of existing SR techniques. While DRL approach to optimize both the source transmission
several SR models, such as ESPCN [85], are described as resolution and the VSR-reconstructed resolution, thus
low-latency,low-computationmodelswithreal-timeperfor- balancing video quality and resource constraints. However,
mance, it is important to clarify their feasibility on devices such works remain few in the literature, leaving room for
without GPUs, such as mobile phones. SR performance improvementinthedesignofoptimizedenhancement-aware
depends on several factors, including the input resolution. ABRalgorithms.
OnCPU-onlydevices,nearreal-timeSRmaybeachievedfor In addition, despite the proliferation of VSR methods,
low-resolutioninputs.However,forhigher-resolutioninputs, quantifying the effect of SR on enhanced videos remains
real-time SR is often not achievable due to the increased a challenge, with few accurate quantitative measures and
numberofcomputationsrequired. evaluation frameworks. Some recent works have begun to
We illustrate this by using ESPCN to enhance the videos address this gap, such as Reznik et al.’s [113] SR quality
of the Waterloo Streaming QoE Database-III [105] at three evaluation metric, which uses a generalized Westerink-
inputresolutions{144,240,360}p.Weuseanupscalefactor Roufsmodel.Theauthorsin[114]alsodevelopMoViDNN,
of 2 and measure the SR processing time in frames per an evaluation application for video enhancement models on
second (fps). The SR model achieves frame rates of 13.2- mobiledevices.Thisplatformmeasuresvariousperformance
18.5,10.3-12.0,and5.0-6.4fpsatthethreeinputresolutions, metrics, such as the PSNR, SSIM, and execution time,
respectively. It can be seen that even input videos with allowing quality enhancement methods to be evaluated and
resolutions as low as 360p are still unable to achieve real- comparedinasystematicway.
time performance using state-of-the-art SR models without
GPU. This shows the need for SR techniques designed C. CACHING
specifically for CPU-only devices. Recently, NERVE [106] Thefinalbandwidthoptimizationtechniquediscussedinthis
shows great promise in implementing real-time VSR on work is known as caching, a method by which content is
mobile devices. Other techniques are also proposed to copied and stored in a cache for quick retrieval. In order
make SR more accessible for computationally-constrained to reduce the pressure on backhaul networks and minimize
devices, such as early-exit schemes [107], which enable the delay, copies of video content are cached at edge servers to
dynamicadaptationofSRnetworkdepthbasedonavailable bringthemclosertotheenduser.However,edgeservershave
computationalresources,andpeer-to-peer(P2P)approaches, limitedstoragecapabilities.Cachedcontentmustthereforebe
such as that proposed by OASIS [108]. In OASIS, user selectedcorrectlytoensurethatonlypopularvideosthatare
devicessharethecomputationalloadofvideoenhancement. likely to be requested by many users are cached in order to
OASIS’ algorithm jointly selects the video bitrate and SR maximizebandwidthefficiency.
model to be used, then each device is assigned SR tasks. Cachingschemescanbeclassifiedintotwotypes:reactive
Once video chunks are successfully enhanced, they can be and proactive. Traditional reactive caching schemes select
shared with other devices, thus improving the QoE without cachedcontentbasedononlylocalhistoricrequestpatterns.
additionalcomputation. For example, the Least Recently Used (LRU) caching
Alternatively,recentresearch[109],[110]suggeststheuse techniquereplacescachedcontentthathasnotbeenrequested
ofimageenhancementmodelsthattargetartifacts,noise,and for the longest time once the server reaches its storage
compression losses rather than upscaling resolution. Refer- capacity, which might lead to caching unpopular content
ence [109] compares the performance of image enhance- just because it has recently received requests. Another
ment and SR techniques, finding that client-side image reactivecachingschemeistheLeastFrequentlyUsed(LFU)
111144 VOLUME13,2025

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
|     |     |     |     |     |     |     | graphic | variations | are influenced |     | by factors |     | such as | cultural |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------------- | --- | ---------- | --- | ------- | -------- |
differences,regionalevents,andlocalizeduserinterests.For
|     |     |     |     |     |     |     | example,    | sports | highlights | of       | a local     | event | may        | receive  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---------- | -------- | ----------- | ----- | ---------- | -------- |
|     |     |     |     |     |     |     | high demand | in     | a specific | region   | but         | very  | limited    | interest |
|     |     |     |     |     |     |     | elsewhere.  | This   | shows      | the need | for caching |       | techniques | that     |
adapttoregionaldemandpatterns.
Toaddressthisaspect,researchershaveproposedtheuse
ofcachingframeworksthatintegrategeographicinformation.
|     |     |     |     |     |     |     | The authors | of  | [119]         | propose | one such | multi-agent |        | DRL |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | ------- | -------- | ----------- | ------ | --- |
|     |     |     |     |     |     |     | framework   | for | edge caching. |         | Since    | one policy  | cannot | be  |
FIGURE5. Popularityfeaturesusedincachingmechanisms. shared across edges, the authors model each edge as an RL
agent.Thisapproachalsobenefitsfromcooperationbetween
|               |         |              |      |               |            |            | neighboring      | edges,     | which  | have     | similar | content,    |       | so files  |
| ------------- | ------- | ------------ | ---- | ------------- | ---------- | ---------- | ---------------- | ---------- | ------ | -------- | ------- | ----------- | ----- | --------- |
| scheme, which | selects | cached       |      | content based | on         | the number |                  |            |        |          |         |             |       |           |
|               |         |              |      |               |            |            | that are         | not cached | at     | one edge | are     | likely      | to be | available |
| of requests.  | This    | can also     | lead | to caching    | of content | that is    |                  |            |        |          |         |             |       |           |
|               |         |              |      |               |            |            | at a neighboring |            | edge   | cache.   | Another | interesting |       | work is   |
| no longer     | popular | just because |      | it has been   | highly     | requested  |                  |            |        |          |         |             |       |           |
|               |         |              |      |               |            |            | presented        | by Zeng    | et al. | [120],   | which   | proposes    | a     | caching   |
in the past. Therefore, while reactive caching schemes are algorithm that uses users’ spatio-temporal context to track
easytoimplement,theyoftenleadtoresourcewastagedueto
contentdemand.
| their inability     | to  | predict | future    | content popularity. |         | Proactive  |          |       |       |                 |     |     |         |        |
| ------------------- | --- | ------- | --------- | ------------------- | ------- | ---------- | -------- | ----- | ----- | --------------- | --- | --- | ------- | ------ |
|                     |     |         |           |                     |         |            | However, | while | using | spatio-temporal |     |     | context | adds a |
| caching techniques, |     | on      | the other | hand,               | predict | the future |          |       |       |                 |     |     |         |        |
valuabledimensiontocachingdecisions,accuratelytracking
popularityofvideocontentbasedonseveraltypesoffeatures,
|     |     |     |     |     |     |     | user mobility |     | patterns | requires | access | to real-time |     | location |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | -------- | ------ | ------------ | --- | -------- |
asshowninFig.5,thustradingoffeaseofimplementationfor data,whichraisespotentialconcernsaboutprivacyanddata
increasedcache‘‘hitrate’’,whichreferstotherateatwhich
|     |     |     |     |     |     |     | security. | Moreover, | processing |     | and analyzing |     | such | spatio- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | ------------- | --- | ---- | ------- |
videocontentissuccessfullyretrievedfromthecacherather
temporaldatacanbecomputationallyintensive,particularly
thantheoriginserver.Awealthofresearchisdevotedtothe given the recent surge in video streaming traffic. As the
useoflearningtechniquesforpredictionofpopularcontent.
numberofviewersandvideorequestsgrows,thedatasentto
|     |     |     |     |     |     |     | train the | caching | algorithm | also | increases | correspondingly, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | ---- | --------- | ---------------- | --- | --- |
1) CACHINGBASEDONTEMPORALFEATURES
|     |     |     |     |     |     |     | requiring | powerful | hardware |     | at the edge, |     | which | may not |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | --- | ------------ | --- | ----- | ------- |
Intuitively, the most obvious method of predicting content alwaysbefeasible.Thesechallengesareaddressedin[121],
popularityisthroughtheuseofhistoricalstreamingpatterns. which uses federated learning to shift training toward end-
| Based on | past popularity |     | statistics, | the future | popularity | of  |              |      |            |     |             |            |     |        |
| -------- | --------------- | --- | ----------- | ---------- | ---------- | --- | ------------ | ---- | ---------- | --- | ----------- | ---------- | --- | ------ |
|          |                 |     |             |            |            |     | user devices | then | aggregates |     | the trained | parameters |     | at the |
video content can be predicted using learning techniques. server. In addition to reducing the computational strain on
| Some of | the most | popular | learning | methods | used | for this |               |     |               |     |            |          |     |          |
| ------- | -------- | ------- | -------- | ------- | ---- | -------- | ------------- | --- | ------------- | --- | ---------- | -------- | --- | -------- |
|         |          |         |          |         |      |          | edge servers, |     | this approach |     | inherently | enhances |     | privacy, |
task include long short-term memory (LSTM) [115] and asrawuserdataremainsonlocaldevices,andonlythemodel
clusteringalgorithmsfortime-evolvingengagementmetrics, updates are shared with the server. Federated learning thus
suchask-meansandcanopyclustering[116].Alternatively,
providesapromisingsolutiontoscalabilityandprivacyissues
adeeplearningapproachisdescribedin[117],whereLietal. incachingframeworks.
proposeaduelingDQL-basedcachingschemetomaximize
| energy efficiency. |        | Their    | proposed | scheme     | makes       | use of |     |     |     |     |     |     |     |     |
| ------------------ | ------ | -------- | -------- | ---------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| recurrent          | neural | networks | (RNNs)   | to extract | information |        |     |     |     |     |     |     |     |     |
aboutpopularcontentbasedonuserrequests.
3) CACHINGBASEDONUSERSIMILARITY
One drawback of this caching technique is that it Other caching approaches use collaborative filtering [122],
assumes that future popularity trends closely resemble past [123], [124], [125]. This technique, often implemented in
behavior. However, the use of historical trends alone might recommendation systems, uses the similarity between users
overlookemerginguserdemographicsandnewviralcontent. tofilteritems.Inthecontextofvideocaching,thesimilarity
| To address | this, | Mao et | al. present | a caching | scheme | that |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------ | ----------- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
betweenviewerscanbeusedtodeterminethelikelihoodthat
usesonlinereinforcementlearning[118]andre-initializesthe a user will request a specific video content. Content that is
RL agent at regular intervals. Meta-learning is then utilized likely to be highly requested by many users is then deemed
to reduce the convergence time. Mistakes and suboptimal to be popular and can be cached proactively. In [123], the
performance can still be seen during the convergence time historicalrequestpatternsofauseraswellasrequestpatterns
forsuchonlinealgorithms,however.
|     |     |     |     |     |     |     | of similar | users      | are used | to      | predict the | demand  | for | video     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------- | ------- | ----------- | ------- | --- | --------- |
|     |     |     |     |     |     |     | content.   | Similarly, | the      | authors | in [124]    | develop | a   | learning- |
2) CACHINGBASEDONGEOGRAPHICFEATURES based collaborative filtering caching scheme that selects
Ontheotherhand,popularcontentvariesnotjusttemporally cachedcontentbasedonthesimilaritybetweenusers’content
but geographically as well. While temporal variations in preferencesaswellastheirlocation.Huangetal.[125]also
popularity capture how preferences evolve over time, geo- useahybridcollaborativefilteringmodelusingbothspatial
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 111145 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
and temporal content characteristics to improve caching watch streams for the longest duration and with greater
performanceinsmallbasestations. regularity. In case the edge server is facing high traffic,
However, while using collaborative filtering can improve the video content downloaded by loyal viewers can then
cache hit rate, it raises some privacy concerns as it heavily be shared across other viewers within the same region,
relies on user data. In addition, it suffers from cold start thus reducing the server load. Live streaming-related traffic
problems when it comes to new content or new users that is also addressed by Ma et al. [129], leveraging edge
do not yet have any data. Therefore, implementing caching computingtoaggregateclientrequestsforthesamevideo.By
schemesthatrelyentirelyoncollaborativefilteringmaylead processingtheserequestsattheedge,theirapproachreduces
tosub-optimalperformance. redundant transmissions and optimizes delivery efficiency.
|     |     |     |     |     |     |     |     | However, | many | of these | works | have yet | to address | several |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | ----- | -------- | ---------- | ------- |
challengesassociatedwithlivecontentcaching.Forexample,
4) CACHINGBASEDONCONTENTSIMILARITY
|     |     |     |     |     |     |     |     | live video | viewership | is  | often | highly | volatile, | with some |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ----- | ------ | --------- | --------- |
Asimilarapproachthataddressesthechallengeofpredicting
|                |                |          |                  |          |            |      |         | streams      | experiencing | sudden      | spikes       | in  | demand    | due to viral |
| -------------- | -------------- | -------- | ---------------- | -------- | ---------- | ---- | ------- | ------------ | ------------ | ----------- | ------------ | --- | --------- | ------------ |
| the popularity |                | of newly | published        |          | videos     | uses | content |              |              |             |              |     |           |              |
|                |                |          |                  |          |            |      |         | moments      | or external  | events.     | Conventional |     | caching   | methods      |
| similarity     | rather         | than     | user similarity. |          | Since      | most | caching |              |              |             |              |     |           |              |
|                |                |          |                  |          |            |      |         | can struggle | to           | effectively | anticipate   |     | and react | to these     |
| schemes        | use historical |          | request          | patterns | to predict | the  | future  |              |              |             |              |     |           |              |
fluctuations,leadingtoincreasedlatency.
| demand       | for video  | content, | new      | videos        | are often | not     | cached   |                       |     |     |     |     |     |     |
| ------------ | ---------- | -------- | -------- | ------------- | --------- | ------- | -------- | --------------------- | --- | --- | --- | --- | --- | --- |
| efficiently. | To address |          | the lack | of historical |           | request | data for |                       |     |     |     |     |     |     |
|              |            |          |          |               |           |         |          | IV. QUALITYADAPTATION |     |     |     |     |     |     |
newvideos,theauthorsin[126]developanextremelearning
|     |     |     |     |     |     |     |     | Video segments |     | in HAS | are encoded |     | at multiple | quality |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ----------- | --- | ----------- | ------- |
machine-basedschemethatusesvideocontentfeatures,such
|     |     |     |     |     |     |     |     | levels, | so the | video quality | can | be  | quickly | adapted to |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------------- | --- | --- | ------- | ---------- |
asthetitle,tags,ornumberofchannelsubscribers,forpopular
|                     |     |            |     |      |              |     |         | reflect the | changing | network    | conditions. |     | Quality | adaptation    |
| ------------------- | --- | ---------- | --- | ---- | ------------ | --- | ------- | ----------- | -------- | ---------- | ----------- | --- | ------- | ------------- |
| content prediction. |     | Similarly, |     | Doan | et al. [127] | use | a deep- |             |          |            |             |     |         |               |
|                     |     |            |     |      |              |     |         | is carried  | out to   | adaptively | select      | the | quality | level of each |
learningapproachtoextractthecontentfeaturesfromtheraw
|              |         |             |         |            |              |            |       | video segment    | based      | on         | a set of | decision      | parameters     | using         |
| ------------ | ------- | ----------- | ------- | ---------- | ------------ | ---------- | ----- | ---------------- | ---------- | ---------- | -------- | ------------- | -------------- | ------------- |
| video data.  | The     | new video’s |         | popularity | is then      | determined |       |                  |            |            |          |               |                |               |
|              |         |             |         |            |              |            |       | an adaptation    | algorithm. |            | ML-based |               | ABR algorithms | use           |
| by studying  | the     | similarity  | between |            | its features | and        | those |                  |            |            |          |               |                |               |
|              |         |             |         |            |              |            |       | learning         | techniques | to         | predict  | the optimal   |                | quality level |
| of published | videos. | These       | methods |            | are able     | to predict | the   |                  |            |            |          |               |                |               |
|              |         |             |         |            |              |            |       | given a          | QoE model. | This       | section  | provides      |                | an overview   |
| popularity   | of      | new content | while   | avoiding   |              | the cold   | start |                  |            |            |          |               |                |               |
|              |         |             |         |            |              |            |       | of the different |            | QoE models | and      | corresponding |                | learning-     |
problemaswellasinvasionofusers’privacyandtheuseof
|     |     |     |     |     |     |     |     | based ABR | algorithms |     | introduced | in  | the literature. | ABR |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------- | --- | --------------- | --- |
theirinformation.
|     |     |     |     |     |     |     |     | algorithms | are | classified | based | on their | application, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ----- | -------- | ------------ | --- |
However,videocontentfeaturesaloneareoftennotindica-
|     |     |     |     |     |     |     |     | Table 4 | compares | notable | ML-based |     | ABR | algorithms, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | -------- | --- | --- | ----------- |
tiveofpopularity;videoswithsimilarfeaturescanhavevastly
|     |     |     |     |     |     |     |     | highlighting | their | design | considerations |     | such | as multi-user |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ------ | -------------- | --- | ---- | ------------- |
differentengagementlevelsduetounpredictablefactorslike
|     |     |     |     |     |     |     |     | fairness, | content-awareness, |     | latency, | energy-efficiency, |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------ | --- | -------- | ------------------ | --- | --- |
virality,trends,orexternalpromotion.Inaddition,extracting
thelearningtechniquestheyadopt.
| video content |     | features,  | as in | [127], | can require | significant   |     |                             |     |     |     |     |     |     |
| ------------- | --- | ---------- | ----- | ------ | ----------- | ------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
| computational |     | resources, | which | may    | make        | this approach |     |                             |     |     |     |     |     |     |
|               |     |            |       |        |             |               |     | A. QoEMODELINGANDPREDICTION |     |     |     |     |     |     |
impracticalforlarge-scale,real-timeimplementation.
AsexplainedinSectionI-A,QoEmodelsareusedtoquantify
|     |     |     |     |     |     |     |     | viewer streaming |     | experience. | Real-time |     | QoE | measurement |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --------- | --- | --- | ----------- |
5) CACHINGFORLIVESCENARIOS depends on a set of QoE metrics, such as re-buffering
Another application of learning techniques for traffic opti- frequency, smoothness, and average quality. These metrics
mization through caching involves live streaming, a rapidly are measured and updated as the video session progresses,
growingsectorthatimposessignificantbandwidthdemands. and the resulting QoE is calculated at each time step.
Live streaming introduces several new problems to the In learning-based ABR schemes, the measured QoE is then
cachingprocess;beinglatency-sensitive,livestreamsrequire usedtoguidetheABRalgorithm.Sincetheuser’sexperience
continuousupdatesandrapidcachereplacement,increasing depends on the accuracy of QoE measurements, several
thecomputationaloverhead.Moreover,Lietal.[128]study works leverage learning techniques to predict QoE more
| mobile live | streaming |     | behaviors | and | statistics | and conclude |     | accurately. |     |     |     |     |     |     |
| ----------- | --------- | --- | --------- | --- | ---------- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- |
that a large percentage of live video traffic is caused by Some recent works are devoted to utilizing machine
redundant uploads with no viewers. Additionally, they find learning [145], [146], [147] and neural networks [148],
that live viewers tend to belong to the same locality with a [149],[150]topredicttheQoEandprovideamoreaccurate
group of loyal viewers that download the most video data. representationoftheviewer’sperceivedexperience.Learning
Therefore, to reduce the bandwidth wastage, the authors techniques are particularly suited for this aspect of video
proposeEDGEOPT,whichreducestheencodingrateofno- streaming, as real-time, objective QoE modeling presents
viewer, unattractive uploads and uses learning-based pre- a major challenge, with several complex and interrelated
fetching to cache the content of popular streams in each factors that impact users’ subjective experience. Machine
region. They also design a peer-assisted video delivery learning has shown impressive performance in mapping
scheme that takes advantage of loyal viewers who tend to out the relationships between these factors and closely
| 111146 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
TABLE2. Datasetsforvideostreamingresearch.
predicting the QoE compared to subjective measures. More measure, bitrate alone cannot be used as a visual quality
advanced techniques are also being researched, such as metric due to the diversity of chunk complexity. In [155],
QoE forecasting, which predicts the future QoE in order the authors investigate the relationship between chunk
to avoid the likelihood of QoE degradation and give the complexityandquality.TheyfindthatmostABRalgorithms
ABR algorithm more time to restore the QoE to acceptable donotselectsufficientlyhighbitratesforcomplexordynamic
levels. One such interesting implementation is presented by chunks, although achieving higher quality for dynamic
Dinaki et al. in [151]. Compared to other QoE prediction chunksthanstaticonesleadstogreaterQoEgains.Tohandle
schemesthatusemeasuredQoEmetricsthatmaybeoutdated thisissue,theydesignDAVS,aquality-awareapprenticeship
by the time the ABR algorithm reacts, Dinaki et al.’s learning-based (refer to Table 1 for definitions of learning
forecastingschemeimprovesthepredictionaccuracythrough techniques) scheme with a modified QoE function that
the use of bidirectional LSTMs (BiLSTMs). BiLSTMs takes chunk complexity into account, as well as users’
extract the bidirectional temporal dependencies of the QoE preferences. Reference [156] also presents a content-
QoE metrics rather than only using past information for aware QoE metric to guide the client’s bitrate selection,
prediction, thus increasing the model’s accuracy. However, based on video quality, playback fluency, volatility, as well
few works have focused on predicting QoE beyond the as video content features extracted using 3D CNN and
current time step despite its potential to improve ABR LSTM. The authors study the effects of each of these
decision-making. factors on the accuracy of QoE prediction and find that
QoE degradation can also occur due to the misclassifica- the accuracy is highest when a model combining all four
tion of user actions (such as pausing) as streaming events factors is used. However, due to the deep spatial-temporal
(suchasre-buffering).Casasetal.addressthisintheirwork featureextractionandregressionmodel,theirmodelishighly
on DeepCrypt [152], which is a deep learning model for complex.
QoEpredictionthatprovidesinsightintouseractionsthrough OtherQoEpredictionmethodsattempttouseQuality-of-
networktrafficanalysis;itdifferentiatesbetweenuseractions Service(QoS)metricstopredicttheQoE.Mustafaetal.[157]
and streaming events with an accuracy of above 80%. design an ABR algorithm-agnostic, ML-based QoE predic-
Inanotherwork[153],theauthorsusedecisiontreeclassifier tion scheme based on QoS metrics, such as round-trip time
forinferenceofQoEmetricsfromencryptedvideostreams. (RTT), number of packets per segment, and throughput.
AnalternativeapproachispresentedinExQoE[154].Rather Decision tree regression (DTR), multi-linear regression
thanusingobjectivemetricsforQoEprediction,suchasre- (MLR), and random forest regression (RFR) are compared
buffering duration and average bitrate, ExQoE models QoE intermsofpredictionaccuracy,andRFRisfoundtohavethe
basedonusers’exitingbehaviorandmodelstheuser’sexiting highestQoEpredictionaccuracy.Anotherapproachin[158]
probabilitybasedonthevideostallingoccurrences.TheQoE usesaduelingDQN,whichseparatesthestatevaluefunction
model is then used to guide the selection of an appropriate and action advantage function. The adaptation algorithm is
CDNandresolutionusingRL. carried out from the MEC server, where the transmission
Other research focuses on developing QoE models that bandwidthandthebufferoccupancyaretracked.Thevideois
more accurately reflect the characteristics of video content. thentranscodedattheedgeserveratthequalitydetermined
Although most of the literature uses bitrate as a quality bytheadaptationalgorithm.
VOLUME13,2025 111147

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
Also related to QoE modeling, video quality assessment B. QoEOPTIMIZATIONFORVoD
| (VQA) | is an | essential | aspect | that measures |     | the video |               |          |            |     |     |                    |     |
| ----- | ----- | --------- | ------ | ------------- | --- | --------- | ------------- | -------- | ---------- | --- | --- | ------------------ | --- |
|       |       |           |        |               |     |           | Reinforcement | learning | techniques |     | are | used predominantly |     |
streaming quality. As such, it plays an important role in for adaptive bitrate selection. In a reinforcement learning-
QoEmeasurementandABRmodelevaluation.Conventional based scheme, video streaming is modeled as a Markov
VQAmethodsevaluatethevideoqualitywithreferencetoa Decision Process (MDP), in which an agent learns to select
certaingroundtruth,typicallyuncompressedvideo.Theseare thebestpossibleaction(i.e.,thebitrateorqualitylevel)given
| known as | full-reference |     | (FR) methods, |     | the most | popular of |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
acertainstate(i.e.,environmentalfactors,suchasbandwidth
whicharethePSNR,SSIM,andVMAFmetrics.Intuitively, availability). The RL agent then learns a policy by which it
these methods, while effective, are not suitable for cases decideswhichactionswillhavethemostfavorableoutcome,
in which a reference video is unavailable, which inspired as determined by the QoE. During training, this policy is
the development of other VQA methods that use reduced updated with each new experience learned by the agent.
| reference | or no | reference. | Reduced-reference |     |     | VQA (RR- |     |     |     |     |     |     |     |
| --------- | ----- | ---------- | ----------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
AvarietyofRL-basedABRtechniqueshavebeendeveloped
VQA) methods use partial information from the reference recently, particularly for VoD streaming, for several appli-
video,suchasextractedfeatures,ratherthanthefulloriginal. cations, such as conventional VoD streaming [166], energy-
They aim to reduce the amount of required data while still aware streaming [167], and short video streaming [168],
maintaining a level of accuracy. Several such methods have among others. These algorithms are generally evaluated
| been proposed |     | in recent | works. | Reference | [159] | develops a |          |          |        |         |            |     |              |
| ------------- | --- | --------- | ------ | --------- | ----- | ---------- | -------- | -------- | ------ | ------- | ---------- | --- | ------------ |
|               |     |           |        |           |       |            | based on | achieved | visual | quality | (indicated | by  | metrics such |
RR-VQA scheme that uses an LSTM model to predict the asVMAF)andoverallQoE,withrespecttoasetofbaseline
VMAF for multi-stage transcoded videos based on DCT- ABRmodels.Thereareseveralcommonmodelsusedinthe
energy-based features. Similarly, VQ-TIF [160] is another literatureasabenchmark,includingconventional[13],[14],
RR-VQA algorithm that uses LSTMs for quality prediction [15], [169] and learning-based methods [16], [17]. Table 3
| based on | fused | SSIM | and spatiotemporal |     | features. | No- |               |        |          |     |            |     |               |
| -------- | ----- | ---- | ------------------ | --- | --------- | --- | ------------- | ------ | -------- | --- | ---------- | --- | ------------- |
|          |       |      |                    |     |           |     | also provides | a list | of tools | and | frameworks |     | available for |
reference VQA (NR-VQA) methods, on the other hand, video streaming research, particularly in the field of ML.
do not require a reference video at all. They estimate the OtherusefultoolsthatarenotspecifictoML-basedstreaming
| quality of | the | video based | on  | its own | content, | usually by |                |        |          |     |         |          |        |
| ---------- | --- | ----------- | --- | ------- | -------- | ---------- | -------------- | ------ | -------- | --- | ------- | -------- | ------ |
|            |     |             |     |         |          |            | (e.g., dash.js | [170], | Mahimahi |     | network | emulator | [171], |
learningpatternsthatpredictperceptualquality,makingthem FFmpeg [36], DASHEncoder [131]) are not included. Note
| more suitable | for | real-time | applications. |     | The P.1204.3 | qual- |                |        |        |       |               |     |               |
| ------------- | --- | --------- | ------------- | --- | ------------ | ----- | -------------- | ------ | ------ | ----- | ------------- | --- | ------------- |
|               |     |           |               |     |              |       | that the tools | listed | in the | table | are generally |     | customizable, |
ity metric [161] is one such bitstream-based NR-VQA allowing researchers to tailor them to specific deployment
| methodthatcomprisesaparametriccomponent(whichuses |     |           |     |        |           |        | goals.  |            |     |     |           |                |     |
| ------------------------------------------------- | --- | --------- | --- | ------ | --------- | ------ | ------- | ---------- | --- | --- | --------- | -------------- | --- |
| degradation-based                                 |     | modeling) |     | and ML | component | (which |         |            |     |     |           |                |     |
|                                                   |     |           |     |        |           |        | Current | literature | on  | ABR | streaming | overwhelmingly |     |
usesrandomforestregressiontoaccountforthevideospatio- features RL-based implementations. In an interesting work
| temporal | features). | Other | ML-based | NR-VQA | methods | are |           |            |     |        |         |       |          |
| -------- | ---------- | ----- | -------- | ------ | ------- | --- | --------- | ---------- | --- | ------ | ------- | ----- | -------- |
|          |            |       |          |        |         |     | utilizing | DRL [172], | Mu  | et al. | present | AMIS, | an edge- |
also suggested in the literature [162], particularly for user- assisted ABR scheme that combines bitrate and playback
generated content (UGC), such as [163] which proposes speedadaptation.Sincechangesintheplaybackrateareless
that semantic video information plays a role in video noticeable for highly dynamic scenes, AMIS analyzes the
quality assessment. Similarly, the VIDEVAL [164] and SSIMbetweentheframesofeachsegmenttodeterminethe
RAPIQUE [165] models have recently been developed for nature of each segment and the extent to which playback
NR-VQAofUGC. speedcanbealteredimperceptibly.Furthermore,[173]sug-
The approaches described above greatly enhance the gesttheuseofLSTM-CNN-basedRLforbitrateadaptation,
accuracy of QoE prediction compared to heuristic methods, with LSTM to replace the 1D-CNN input layer to better
andconsequently,thequalityadaptationprocessisimproved. extract information from the sequential inputs, such as past
However,itisimportanttonotethatlearningtechniquesoften
throughputandsegmentdownloadrates.Fengetal.[174]also
have greater computational complexity and overhead. In an use an RL-based scheme with proximal policy optimization
end-to-end streaming system, this complexity becomes an (PPO), which is an algorithm that limits the changes to the
| even greater | concern. | Consider |     | only the | client side; | it may |     |     |     |     |     |     |     |
| ------------ | -------- | -------- | --- | -------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
policyandreducesthedifferencebetweentheoldandupdated
comprise several components, including but not limited to policy, thus improving the stability of training. The authors
| throughput | prediction, |     | QoE prediction, |     | video content | anal- |                 |     |               |     |            |     |           |
| ---------- | ----------- | --- | --------------- | --- | ------------- | ----- | --------------- | --- | ------------- | --- | ---------- | --- | --------- |
|            |             |     |                 |     |               |       | in [175] design | a   | DRL algorithm |     | to improve | QoE | in highly |
ysis, quality adaptation, and quality enhancement modules. dynamicnetworkenvironmentsusingdualPPO.
As such, it is essential to consider the complexity of these Similarly,deepQ-learningisabranchofDRLwhichisalso
| algorithms | holistically, |     | rather than | as separate | components, |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ----------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
commonlyusedintheliteratureforqualityadaptation[176],
sincemanyend-userdevicesmaynotbecapableofhandling [177], [178]. In conventional Q-learning, state-action pairs
| the computational |     | load | of all | these tasks | simultaneously, |     |            |              |         |     |            |       |            |
| ----------------- | --- | ---- | ------ | ----------- | --------------- | --- | ---------- | ------------ | ------- | --- | ---------- | ----- | ---------- |
|                   |     |      |        |             |                 |     | are stored | in a tabular | format, |     | along with | their | associated |
shouldtheybetoocomplex.Thisaspectmustbeconsidered Q-values (see Table 1). DQL, on the other hand, uses a
when analyzing the practicality of learning-based schemes neural network to estimate the Q-values instead, making
| for the different |     | modules | of video | streaming, |     | particularly |                  |     |               |     |            |       |            |
| ----------------- | --- | ------- | -------- | ---------- | --- | ------------ | ---------------- | --- | ------------- | --- | ---------- | ----- | ---------- |
|                   |     |         |          |            |     |              | it more suitable |     | for scenarios |     | with large | state | and action |
thosethatutilizedeepneuralnetworkarchitectures. spaces. The advantage of DQL over other RL schemes
| 111148 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
lies in its use of experience replay, in which the neural addressedin[182],whichsuggeststheuseoftransferlearning
network’spastexperienceisstoredwithinareplaymemory. to tackle the highly variable nature of network bandwidth.
Thereplaymemoryisthensampledatrandomfortrainingto Theauthorsalsodesignastreamingactivitymonitortotrack
eliminatethecorrelationbetweenconsecutivesamples.One thenetworkconditionsduringOFFperiodsinwhichtheclient
disadvantageofDQLapproaches,however,istheirtendency doesnotdownloadvideosegments.Thisway,thethroughput
to overestimate the Q-value. To mitigate this issue, [179] can be more accurately predicted based on actual network
implement DQNReg-based rate adaptation. DQNReg is a conditionsratherthanpastsamplescalculatedduringtheON
modified DQL model that avoids overestimation of the Q- period. DeX [186], on the other hand, tackles the issue of
value by adding a weighted penalty to the model’s loss unstable bandwidth differently. While it was developed for
function. As a result, DQNReg achieves faster convergence real-timecommunicationscenariosratherthanHTTP-based
andhigherQoEthanconventionalDQL. streaming, it offers a relevant perspective: it leverages deep
In order to improve the QoE, other works attempt learning for short-term throughput prediction, particularly
to accurately predict ABR decision parameters, such as targetingextremeorabruptbandwidthfluctuations.
bandwidth [74], [180], [181], [182]. The bandwidth is A range of edge-assisted ABR schemes is also proposed
typicallyoneofthemostessentialfactorsindeterminingthe intheliterature[187],[188].Edge-assistedstreamingbrings
bitrate level of the next segment. In the literature, LSTM content to edge servers, close to the client’s end. As such,
networksarecommonlyusedforthroughputprediction[183]. it provides much quicker delivery, as well as higher
In [7], Yoo et al. compare the performance of five machine capabilitiesfortasksthatend-userdevicesmaynotbecapable
learningmodelsinbandwidthpredictionforDASHandfind ofcarryingout.Takingadvantageofthis,recentresearchnow
that LSTM networks provide the most accurate prediction. proposestheuseofedgeresourcestoconcurrentlyimplement
However, despite being relatively the most accurate, their video chunk transmission and transcoding, thus reducing
LSTM model still has a high prediction error. Inaccurate delay [189]. Other computationally intensive tasks are also
throughput prediction can cause ABR algorithms to incor- suggested to be implemented at the edge server, such as
rectly select high video bitrates, resulting in video stalling. quality enhancement and super-resolution [83], [96], [101],
In [8], the authors tackle this issue. They utilize a Bayesian asdiscussedinSectionIII.
neuralnetwork(BNN)topredictthethroughputwhiletaking
the aleatoric (relating to the model output) and epistemic C. MODELGENERALIZABILITY
(relating to the model weights) uncertainty into account. Despite impressive performance shown by learning-based
Based on this uncertainty, the authors build a confidence ABR algorithms in the literature, in reality, ensuring that a
region for the throughput prediction and implement an modelperformsconsistentlyacrossdiversenetworkenviron-
uncertainty-aware scheme that maximizes the worst-case mentsremainsasignificantchallenge.WhileheuristicABR
QoEaccordingly. algorithmscanshowrobustbehaviorinunseenenvironments
Furthermore, [9] presents Yuan et al.’s design of an due to their deterministic nature, learning-based algorithms
attention-based throughput forecasting model, GCA, which often struggle to generalize. This is mainly because RL
uses a gated recurrent unit, convolutional neural network, models are trained within specific environments in which
and attention mechanism to improve the future throughput overfittingmayoccur.Inmachinelearning,overfittingoccurs
prediction. The authors then develop PRIOR, a multi-agent when models learn specific patterns in the training data too
DRL network for bitrate adaptation, and show that using well, leading to performance degradation when faced with
the predicted throughput measurement rather than historic new, unseen conditions outside their training distribution.
throughput records improves QoE. Another recent work Consequently, improving the generalizability of learning-
presents Xatu [184], a neural network-based scheme that based ABR algorithms is a critical area of research that is
improves the prediction accuracy for the download rate beingtackledusingavarietyoftechniques.
of video chunks. Xatu includes not only throughput but While offline learning algorithms may perform well in
also temporal features, such as Time to First Byte (TTFB), environments included in their training, their performance
in chunk download rate estimation. Based on their results, rapidly declines in new environments. In RL-based ABR,
the authors confirm that the use of temporal features aside once the network environment changes, the offline neural
from throughput improves prediction accuracy. In contrast, network must be re-trained once again. The problem of
EnDASH [185] uses random forest algorithm to predict the QoE degradation in learning-based ABR algorithms is
throughput, followed by quality adaptation using DRL, for addressed in several works using online learning methods.
a less complex and computationally intensive approach to For example, the authors in [191] suggest using online
throughputprediction.Theuseoflearningtechniquesinthese RL to update the neural network in real time if the QoE
works can significantly reduce the chance of rebuffering as drops below a predefined threshold. ABRaider [192] is
ABRalgorithmscanpredictchangesinnetworkthroughput another approach that combines offline and online training
inadvanceandreactaccordingly.However,itisimportantto to balance generalizability and adaptability. In its offline
notethatsuchapproachessufferfrominaccuratepredictions phase, a generalized neural network learns to select one of
inthecaseofextremelyunstablenetworkconditions.Thisis five existing ABR algorithms based on expected rewards,
VOLUME13,2025 111149

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
TABLE3. ToolsandapplicationsforML-basedvideostreamingresearch.
while its online phase tunes the model on client-specific allows the RL model to transfer knowledge across different
data, resulting in a specialized model for each client. tasks, so that previous knowledge learned can be used for
However,whilethistwo-stagetrainingimprovesABRaider’s new tasks. To illustrate this concept, MetaABR [197] is
adaptability,itincreasescomputationaloverheadontheclient a meta-learning, RL-based framework for ABR selection
side.Similarly,someworks[193],[194]trainRLmodelson with several actors and a meta-critic that supervises and
pre-classifiednetworkenvironments,basedonfeaturessuch evaluates their actions. The meta-critic learns a high-level
as bandwidth, undergoing additional online training in new policybasedontransferredknowledge.Therefore,MetaABR
networkenvironmentstoavoidQoEdegradation. can adapt to different unseen environments and converge
However, although online learning provides benefits in much faster than other learning-based algorithms. In [198],
termsofgeneralizationandadaptability,itisimportanttonote Huo et al. also propose a meta-learning-based scheme
that continuous training is required, leading to much higher for QoE optimization and personalization that learns the
processing demands. In most cases, the ABR algorithm is individual QoE preferences of each user. A primary policy
deployed on the client device, making these computational learns to select one out of at least three DRL sub-policies
demandsinfeasibleforlow-enddevices.Inaddition,constant for quality adaptation based on user preference. In this
onlineupdatescandestabilizethemodel,especiallyifshort- framework, meta-learning is used to transfer knowledge
termfluctuationsareoveremphasized. across all sub-policies and speed up training. Similarly,
Beyond online learning, other schemes are also used A2BR[199]usesmeta-RLwithatwo-phasetrainingprocess,
across the literature to improve the generalizability of leveraging domain knowledge to improve adaptability to
ABR algorithms through innovative learning methods. For client-specific network conditions. However, despite their
example,theauthorsin[195]implementGenet,acurriculum advantages, meta-learning approaches often require large
learning-based framework (refer to Table 1) to improve trainingdatasetsandcomputationalresources,whichpresents
the performance of RL algorithms in new environments. abarriertotheirpracticaldeployment.
Genet uses rule-based algorithms as a baseline, taking Federated learning is another recent promising solution
advantage of the fact that they generally show stable forABRgeneralizability.Itdiffersfrommeta-learninginits
performance,eveninunseenenvironments.Theperformance focus; meta-learning aims to improve a model’s ability to
gapbetweentheRLandrule-basedalgorithmsisthenusedto quickly adapt to new tasks or environments by leveraging
determinewhichenvironmentsarerewarding,helpingtheRL knowledge from previous tasks. Federated learning, on the
modelsachieveimprovedgeneralization.Anotherstrategyis other hand, trains models across distributed devices or
proposed in [196], which utilizes a hybrid framework that clientswithoutcentralizingdatatoensuredataprivacy.This
includesmultiplebitrateadaptationmethodsandselectsthe is demonstrated in FedABR [200], which trains a global
one that will result in the highest QoE at each segment modelacrossmultipleclientswithoutsharingrawdata,thus
boundary. The method pool consists of a bandwidth-based, ensuring privacy and allowing the creation of personalized
PD-controller based, and RL-based method. While this models for each client. However, federated learning has
approach achieves high rewards, it suffers from unstable its own limitations which inhibit its deployment in real-
bufferoccupancy.Suchalgorithmsthatcombinetheoutputs world systems. Although this approach addresses privacy
of several ABR models during quality adaptation [192], concerns and computational bottlenecks at servers, it relies
[196] are able to take advantage of the strengths of each ontheavailabilityofsufficientcomputationalpoweronend-
model while avoiding their weakness. On the other hand, user devices, which is not always guaranteed. Moreover,
runningseveralABRalgorithmssimultaneouslycanincrease federatedlearningprimarilyfocusesonlearningasingletask
processingrequirements,makingitessentialtoconsiderthe and produces a common global model. In contrast, meta-
computational complexity of each model included in the learning can better adapt to heterogeneity, which makes it
methodpooltoavoidexcessivelyhighcomplexityorlatency. moresuitableinscenarioswherepersonalizationisnecessary.
Selecting a different ABR approach for each segment may
alsoleadtoinconsistentbitratebehavior. D. QoEFAIRNESS
Additionally,manyrecentworkstakeadvantageofmeta- TheaforementionedQoEimprovementmethodsarelimited
learningtoimprovegeneralizability.Theuseofmeta-learning inthattheyeachattempttoimprovetheQoEofasingleclient
111150 VOLUME13,2025

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
FIGURE6. Multi-userframework.
ratherthanprovidingafairQoEandbandwidthdistribution thatdynamicallyallocatesbandwidthusingclients’mobility
toseveralcompetingclientssharinganetwork.Totacklethis profilesandQoEdata.Neuralnetworksareusedtoadaptively
issue, learning techniques are increasingly being leveraged optimize the system parameters, ensuring robustness across
to simultaneously optimize individual QoE and global QoE differentnetworkconditions.Suchcollaborativeapproaches
fairness.Fig.6showsanexampleofamulti-userstreaming combine the benefits of both server- and client-side
system with a single server delivering content to multiple adaptation.
clients. Following a similar framework, Yuan et al. [201] Rather than collaborative client-server approaches, very
suggest a client-server collaborative framework, Multi-User few works use purely client-side adaptation for multi-user
Adaptive Bit-Rate (MUABR), to improve QoE for all users scenarios [205]. On the other hand, many works in the
in multi-user video streaming. In MUABR, each client is literatureutilizeserver-sideadaptationinsteadwhenitcomes
consideredanindependentRLagent.Theclient’sRL-based to multi-user streaming. For example, Mu et al. build upon
ABR algorithm determines the bitrate of the next video theirworkonAMIS[172]withAMIS-MU[206].AMIS-MU
segment, as well as the urgency of the client’s need for consistsofaplaybackadaptationmodule,whichusesserver-
bandwidth allocation, based on factors such as the buffer sideactor-criticRLtooptimizeQoEthroughresolutionand
occupancy and previous segment size. On the server side, playbackspeedadaptation,andaresourceallocationmodule,
bandwidthallocationisdeterminedbyeachclient’surgency whichusesthevaluefunctionoutputofthecriticnetworkto
and the likelihood of rebuffering. Clients with low buffer estimate each client’s need for resources. Some approaches
occupancyandsmallerprevioussegmentsizesareallocated also use edge computing to carry out quality adaptation at
more bandwidth, helping to improve the overall average theedgeserver[207],[208],[209],[210].Theseapproaches
QoE for all users. Altamimi and Shirmohammadi [202] typicallyimplementanRLagentattheedgeserver,whereit
also propose client-server cooperation to ensure fairness observestheglobalandindividualclientstatestomakebitrate
between users sharing a bottleneck while maintaining an decisions.
acceptable individual QoE. An RL agent at the server- However,suchedge-basedapproachesdonottakeadvan-
side specifies the maximum allowable bitrate available to tage of advanced client computation resources. While
each client over a given window of time, while the client server-side multi-user algorithms are useful since servers
carries out the ABR algorithm. The goal of the RL agent have a holistic view of all users as well as the network
is to maximize a social welfare function to ensure fair QoE conditions, they increase the server load, underutilizing
allocation [202]. In [203], Liu et al. propose a federated increasinglypowerfulclientcapabilities.Inaddition,client-
learning-based bandwidth allocation scheme that uses a side algorithms naturally provide more personalization.
client-side DRL algorithm to select the chunk bitrate and However,thelackofcentralizedcontrolmakespurelyclient-
assignaweightrepresentingtheclient’sneedforbandwidth, side algorithms less effective at ensuring fairness. Network
with the server only providing each DRL agent with a congestionisalsodifficulttohandleproactivelyusingclient-
global state that contains information about the QoE of side algorithms, making them far less common in multi-
all clients. Similarly, VSiM [204] is an end-to-end system user streaming scenarios. Balanced, cooperative approaches
VOLUME13,2025 111151

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
that effectively utilize both server and client resources are frameworkthatallowsmultipleparentstotransmitredundant
thereforenecessary. videocontenttoasinglechildviewer,ensuringuninterrupted
|     |     |     |     |     |     | playback        | even | if some     | parents | leave     | the session. | A   | DRL- |
| --- | --- | --- | --- | --- | --- | --------------- | ---- | ----------- | ------- | --------- | ------------ | --- | ---- |
|     |     |     |     |     |     | based scheduler |      | is designed | for     | multiflow | transmission |     | to   |
E. LIVESTREAMING
|     |     |     |     |     |     | adaptively | balance | flow | volumes | and | optimize | the | video |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | ------- | --- | -------- | --- | ----- |
In previous sections, we have generally discussed ABR qualityinreal-time.
algorithms designed for conventional streaming scenarios, Given the more stringent latency requirements of live
i.e., scenarios that are not latency-sensitive. In this section, streaming, accurately predicting the QoE of live videos
we now discuss low-latency algorithms for live streaming requires real-time quality assessment with high precision.
| scenarios. | Due to the | recent | proliferation | of live | content, |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ------ | ------------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Assuch,liveQoEpredictionisanotherchallengethatrecent
particularly user-generated content, several works look into research attempts to address, such as Vega et al.’s [213]
QoE prediction and improvement for such scenarios as design of an unsupervised learning method involving the
well [211], [212], [213]. Live streaming presents several use of Restricted Boltzmann Machines (RBM) for online
unique challenges compared to conventional streaming due live video quality assessment. However, the use of ML
toitsstringentrequirementsforlowlatencyandsynchroniza-
|     |     |     |     |     |     | techniques, | particularly |     | deep learning, |     | remains | a challenge |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | -------------- | --- | ------- | ----------- | --- |
tion. Unlike on-demand streaming, where slight buffering in live scenarios, so there are yet few studies suggesting its
delays can be acceptable, live streaming necessitates real- useforQoEprediction,unlikeVoD-focusedresearch.
timedeliverytomaintainviewerengagement,particularlyin
the case of interactive video, which makes ABR algorithms F. CONTENT-AWAREADAPTATION
forlivestreamingparticularlydifficulttodesign. Video content also plays a role in determining users’
Since maintaining latency within an acceptable range is QoE. Much of the recent research is devoted to devel-
crucial for ensuring high QoE in live streaming, buffer oping adaptation algorithms tailored to viewers’ content
| size is a | key factor to | consider: | excessively | large | buffers |             |        |        |     |        |             |         |     |
| --------- | ------------- | --------- | ----------- | ----- | ------- | ----------- | ------ | ------ | --- | ------ | ----------- | ------- | --- |
|           |               |           |             |       |         | preferences | [228], | [229]. | In  | [229], | the authors | propose |     |
increasedelay,whilebuffersthataretoosmallmighthinder an adaptation scheme that takes into account the user’s
the delivery of high-quality segments. This has motivated preferenceintermsofvideoaffective,oremotional,content
the development of buffer management techniques, such (e.g., joy, sadness, disgust, surprise, fear, and anger). Deep
as TCLiVi [214], which uses DRL to adaptively select learning is used to learn the user’s affective content (AC)
| both the | video bitrate | and target | buffer | size. In | addition, |             |         |      |        |         |          |           |     |
| -------- | ------------- | ---------- | ------ | -------- | --------- | ----------- | ------- | ---- | ------ | ------- | -------- | --------- | --- |
|          |               |            |        |          |           | preferences | offline | from | recent | viewing | history. | Buffering |     |
several other approaches can also be used to reduce the time is then allocated based on AC relevancy, so higher
latency, such as frame skipping [215], [216], [217] and affective segments receive higher quality representations.
playback speed adaptation [217], [218], [219]. The authors The work in [225] also uses content-aware adaptation to
in [215] use an RL framework for live ABR to reduce improve user QoE. However, in this work, video content
| live latency | by using frame | skipping | when | the latency | rises |               |       |          |      |        |        |       |        |
| ------------ | -------------- | -------- | ---- | ----------- | ----- | ------------- | ----- | -------- | ---- | ------ | ------ | ----- | ------ |
|              |                |          |      |             |       | is classified | based | on scene | type | (e.g., | dance, | news, | music, |
above a specified threshold. However, their approach does etc.) rather than emotions. The user’s viewing history is
not guarantee a high QoE, especially when the available used to determine their preferences, and term frequency-
bandwidth is unstable or limited. Similarly, Deeplive [216] inverse document frequency (TF-IDF) is applied to ensure
isaDouble-DQN[220]approachdesignedforlivescenarios that generally common and frequently occurring scenes are
| which uses | frame skipping | to  | reduce latency. | A   | quick-start |              |     |              |         |     |              |     |        |
| ---------- | -------------- | --- | --------------- | --- | ----------- | ------------ | --- | ------------ | ------- | --- | ------------ | --- | ------ |
|            |                |     |                 |     |             | not included | in  | the viewer’s | content |     | preferences. | In  | [228], |
mechanism is also developed to use a rate-based algorithm video content features are extracted by applying a 3D CNN
rather than Deeplive’s learning-based algorithm at the start to 16 frames from each segment. DQL is then used for
ofthevideostream,whenhistoricalstateinformationisnot rate adaptation based on the interestingness of each video
availableyet.Ontheotherhand,theworkin[218]proposesa segment. Another recent RL-based work on content-aware
low-latencyDRLframeworkforselectingvideoqualityand adaptation is presented in [226], which uses the number
playback speed for live streaming. This method maximizes of replay times to determine scene importance. However,
QoE given a live latency target and, rather than skipping this method is not applicable for newly uploaded videos as
frames,slightlyvariestheplaybackspeedtoreducelatency. they would not yet have replay information. An interesting
Alternatively,theapproachin[217]usesactor-criticDRLfor alternativeapproachproposedbyYeetal.usesDRLtodesign
livescenariostocombinebothframeskippingandplayback avisualsensitivity-awareadaptationalgorithm[223].
speedadaptation. Aside from semantic video content, some works also
Live video streaming also benefits from peer-to-peer focus on content complexity. Not all scenes in a video
systems. Recent research introduces such decentralized sequence have the same level of complexity; rather, some
streamingtechniquesinordertoimprovelivestreamquality, scenes are highly complex or dynamic (e.g., action scenes),
reduceserverloads,andtacklehighvideotrafficduringlive whereassomearesimpleorstatic(e.g.,interviews).Although
events.Onenotableworkutilizingthisconceptispresented complex scenes have a larger impact on user QoE, they
in [221], which introduces a P2P system for crowdsourced tend to be requested at lower bitrates by ABR algorithms
live video streaming. This scheme leverages a multiflow thanlesscomplexscenesduetotheirlargersize.Requesting
| 111152 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
TABLE4. Comparisonbetweenqualityadaptationschemes.
higher bitrates for complex scenes would require high approachestomeetthedemandforincreasinglyuser-centric
bandwidth resources, so conventional ABR algorithms do andpersonalizedstreaming.
not favor these scenes. This leads to reduced visual quality, In addition, although complex tasks such as bitrate
as complex scenes require higher bitrate levels to achieve selectionseelimiteduseofshallowandsupervisedlearning
acceptablequality,whereaslow-complexityscenescanreach techniques-duetolabelsparsity,temporaldependencies,and
an acceptable quality even when requested at a low bitrate high-dimensional action spaces- the scalability and robust-
level [230], [231]. This issue is addressed in some recent ness of deep learning methods across real-time scenarios
works, which design content complexity-aware adaptation remain lacking. This is because live streaming demands
schemes[155],[232],[233],[234]. less computationally intensive techniques, leaving heuristic
Although using content-aware adaptation improves QoE, methods or shallow learning as a possible solution in
requestinguser-preferredchunksatahighbitratemightnotbe future ABR research. Similarly, in the case of caching,
possibleiftheyneedtobefetchedatinstantsoflownetwork collaborative filtering and other user-centric methods have
bandwidth. Rather than relying on an unreliable network inspired the use of clustering algorithms to improve cache
connection, pre-fetching can be leveraged for preferred contentprediction.Videoencodingisalsoanotherapplication
chunks,assuggestedbyHotDASH[224].HotDASHusestwo in which the use of shallow learning can provide several
cascaded RL networks, the first of which carries out bitrate benefits.Thisismotivatedbythefactthatvideoencodingis
selection, while the second network makes the decision to a computationally hungry process, calling for less complex
pre-fetch a chunk or not. This method ensures the delivery techniques to reduce its energy and time demands; it also
ofcriticalchunksathighbitrates,althoughthecascadedRL typically involves less complex decision spaces compared
designmayincreasethecomputationalcomplexity. to bitrate selection, making shallow learning more feasible.
Therandomforestanddecisiontreealgorithmsinparticular
have shown great promise in this field, although much
V. POSSIBLERESEARCHDIRECTIONS of previous research has focused on deep learning to the
A. EMERGINGTRENDSANDTECHNOLOGIES exclusion of other alternatives. In the remainder of this
Our study has identified several trends in current adaptive section,wefurtheranalyzerecenttrendsinML-basedvideo
streaming research, such as the popularity of reinforcement streaming.
learning methods, although some RL techniques, such as
Q-learning, have seen less recent interest. However, while 1) ENERGY-EFFICIENTVIDEOENCODING
DRL methods, particularly the A3C method that has been Video coding research has increasingly prioritized energy
usedinPensieve[16],dominatecurrentABRresearch,future efficiency and computational scalability, shifting from the
researchshouldfurtherexploremeta-andfederatedlearning use of computationally intensive exhaustive bitrate ladder
VOLUME13,2025 111153

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
generation, with a greater focus on ML-based solutions. 3) 5GFORLOW-LATENCYSTREAMING
| Particularly, | instead | of  | focusing | solely | on  | bitrate and |                |     |       |          |            |     |              |
| ------------- | ------- | --- | -------- | ------ | --- | ----------- | -------------- | --- | ----- | -------- | ---------- | --- | ------------ |
|               |         |     |          |        |     |             | The deployment |     | of 5G | networks | introduces |     | higher band- |
resolutionadaptation,emergingresearchnowleveragesML width and low latency, which significantly benefit video
todynamicallyselectoptimalencoderconfigurationsacross streaming applications. Features such as network slicing
awiderrangeofparameters,includingencoderpreset,frame (whichallowsisolationofstreamingworkloadsondedicated
rate, and GOP structure. We also observe that per-title virtual network slices), massive MIMO (which increases
| encoding, | previously | more | prevalent, | is  | now being | replaced |          |              |     |                 |     |          |      |
| --------- | ---------- | ---- | ---------- | --- | --------- | -------- | -------- | ------------ | --- | --------------- | --- | -------- | ---- |
|           |            |      |            |     |           |          | spectral | efficiency), | and | millimeter-wave |     | (mmWave) | com- |
byper-chunkandper-shotencodingapproachesduetotheir munication(whichoffershighdataratesovershortdistances)
improved performance in terms of bandwidth utilization. provideresourcesforhigh-throughput,delay-sensitivevideo
Notably, such techniques are being adopted in commercial- streaming. Within this context, machine learning models
gradestreamingsystems[57],showingtheirviabilityinreal- are now increasingly being used to design 5G-based ABR
worlddeployments.
|     |     |     |     |     |     |     | algorithms. | This | is because, |     | despite | their | potential, 5G |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------- | --- | ------- | ----- | ------------- |
However,severalopenareasofresearchremain.Content- networks suffer from several challenges that limit their
aware and, more recently, network-aware models have seen real-life performance, such as signal blockage in mmWave,
growing interest. These methods have the potential to dynamic user mobility, fluctuating link quality, and energy
provide further improvements in bandwidth-efficiency and consumptionatbasestations.ML-basedalgorithmsarethus
| perceptual | quality | by incorporating |     | contextual |     | information |                |     |            |       |        |         |            |
| ---------- | ------- | ---------------- | --- | ---------- | --- | ----------- | -------------- | --- | ---------- | ----- | ------ | ------- | ---------- |
|            |         |                  |     |            |     |             | being proposed |     | to address | these | issues | through | techniques |
aboutboththevideoandtheunderlyingdeliveryconditions. such as proactive adaptation, chunk prefetching, and buffer
Network-awareencoding,forinstance,leveragesknowledge management[74],[222],[235],[236],[237].However,most
| of historical | or  | predicted | network | throughput |     | to proac- |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
currentadaptationalgorithmsarestillnotdesignedtoexploit
tively optimize bitrate ladders or select encoding presets, 5G-specificfeatures.IntegratingABRmodelswithfunctions
minimizingunnecessaryencodesandreducingtransmission such as 5G network prediction remains a largely untapped
| latency.  | However,  | most          | existing | models   | assume   | static or     | area. |     |     |     |     |     |     |
| --------- | --------- | ------------- | -------- | -------- | -------- | ------------- | ----- | --- | --- | --- | --- | --- | --- |
| averaged  | bandwidth | profiles,     |          | limiting | their    | effectiveness |       |     |     |     |     |     |     |
| in highly | dynamic   | environments. |          | Future   | research | should        |       |     |     |     |     |     |     |
explorereal-timenetworkmodelingandpredictionintegrated
with encoder decision logic, in order to allow encoding 4) USERBEHAVIORANALYSIS
parameterstobeadaptedon-the-fly. Whenwatchingvideocontent,viewersdonotalwaysrequire
|     |     |     |     |     |     |     | the highest  | possible | quality | that | their  | network | conditions |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------- | ---- | ------ | ------- | ---------- |
|     |     |     |     |     |     |     | can support. | Often,   | users   | play | videos | in the  | background |
2) PERSONALIZEDVIDEOSTREAMING while doing something else (for example, playing a music
There has been significant headway in accommodating video in another tab or watching a movie on a separate
user preferences in terms of content and QoE in VoD screen while working). Some short videoapplications, such
streaming.Userpreference-awareABRalgorithmsthattailor as TikTok or YouTube Live, also involve scrolling through
content delivery to individual user content preferences videos rapidly, with users often skimming through to find
(for example, based on genre) and QoE preference (by their preferred content without focusing on the videos.
prioritizing one or more QoE metrics over others) have In these cases, a typical quality adaptation algorithm would
been discussed in Section IV. This aligns with ongoing still continue to deliver the video at the highest possible
effortstoensurethatusersreceivethebestpossibleperceived quality,eventhoughtheuserisnotactivelywatching,leading
qualityforvideostreams.RecentstudieshaveexploredRL- to bandwidth wastage. With the development of device
based personalization where policies adapt to user-specific capabilitiesthatenableuserstoplayvideosatahighquality
reward models. In VoD scenarios, where pre-analysis of even while using the device for other tasks, as well as the
videocontentisfeasible,personalizationtechniquessuchas growing popularity of short video applications, streaming
scenecontentanalysisandemotion-basedadaptationcanbe algorithmsthattakeuserbehaviorsintoaccounthaverecently
implementedtoenhanceviewerengagementandsatisfaction. beendevelopedtoimprovebandwidthefficiency.Techniques
However,weobservethatsuchpersonalizedapproachesare to track user engagement and streaming behavior using
comparatively scarce in live scenarios. Due to low-latency ML are gaining attention in research. Recent research
requirements, implementing techniques such as content into short video streaming provides several basic solutions,
analysis or quality enhancement becomes more challenging includingpredictivevideopre-loadingbasedonuserbehavior
inlivescenarios.Assuch,personalizedstreamingremainsa patterns. However, this introduces the question of how
focus mostly in VoD applications. Other challenges include streaming systems can detect and adapt to user engage-
the cold-start problem, in which new users or content with ment levels and interaction patterns in real time without
no prior information inhibit the operation of personalized violating users’ privacy. Future architectures may rely on
streaming systems; privacy risks when analyzing user data; decentralized schemes such as federated models, but these
and the complexity of multi-objective reward design for methods are still in their infancy within the field of video
| personalizeduser-centricQoEmodels. |     |     |     |     |     |     | streaming. |     |     |     |     |     |               |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | ------------- |
| 111154                             |     |     |     |     |     |     |            |     |     |     |     |     | VOLUME13,2025 |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
5) LARGELANGUAGEMODELSFORVIDEOAPPLICATIONS high computational requirements of many ML solutions,
especiallythoseleveragingDNNs.Manydevicesareunable
Recentyearshavewitnessedtheemergenceofseveralsignif-
icantdevelopmentsinartificialintelligence,withseveralnew to implement such computationally demanding and energy-
technologies poised to reshape the landscape of ML-based consumingoperations.Recentresearchhasthereforefocused
videostreaming.Forexample,theadoptionoflargelanguage on providing solutions to reduce the complexity of ML
models (LLMs) in multimedia systems is gaining traction algorithms and make them more scalable, using techniques
suchasearly-exitmodels[81],[107].Anotablerecentstudy
duetotheirexceptionalabilitytogeneralizeacrossdifferent
tasks and environments, perform complex reasoning, and has also proposed the interpretation of DNN models to
integrate multimodal inputs. Research [238] has shown the equivalentdecisiontreemodels,whicharefarlesscomplex,
potential of a single LLM to be applied across several withnearlyidenticalperformance[239].
networking tasks, including adaptive video streaming. This Learning-based algorithms also suffer from an inability
|                     |     |     |      |        |               |     |          | to perform | well | in  | real streaming |     | environments. |     | These |
| ------------------- | --- | --- | ---- | ------ | ------------- | --- | -------- | ---------- | ---- | --- | -------------- | --- | ------------- | --- | ----- |
| would significantly |     | cut | down | on the | computational |     | costs of |            |      |     |                |     |               |     |       |
training multiple neural networks for different tasks, which learning-based algorithms are typically trained and tested
is one of the main challenges obstructing the deployment in simulated environments, which are unable to accurately
of ML methods in practice. However, LLMs face several mimic real-world streaming scenarios. As such, trained
challenges.Highcomputationaloverhead,memorydemands, models show good performance in simulated environments
|     |     |     |     |     |     |     |     | but perform | dismally |     | in real | ones, | making | their practical |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------- | ----- | ------ | --------------- | --- |
andinferencelatencyremainmajorobstaclesthathinderthe
integrationofLLMsinreal-worldsystems.Techniquessuch deployment challenging. Some research has discussed the
asmodelpruningandquantizationarenowbeinginvestigated so-called simulated-real streaming gap [18], illustrating the
toaddressthesechallenges,butLLMsarestillfarfromready lack of adaptability to real-world conditions of learning-
forpracticaldeploymentinvideostreamingapplications. basedalgorithms.ProjectssuchasPuffer[19]haverecently
|     |     |     |     |     |     |     |     | been implemented |          | to               | address | this challenge, |     | yet the | issue    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | ---------------- | ------- | --------------- | --- | ------- | -------- |
|     |     |     |     |     |     |     |     | remains          | for most | state-of-the-art |         | algorithms      |     | due to  | the lack |
6) EDGE-ASSISTEDVIDEOSTREAMING
|     |     |     |     |     |     |     |     | of comprehensive |     | learning-based |     | training |     | platforms | using |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | -------- | --- | --------- | ----- |
Edgecomputingisanothertechnologythatisnowgenerating
real-worlddata.Tobridgethissimulated-realstreaminggap,
immenseinterestinmultimediastreaming.Edgeservershelp
|                 |        |            |                |             |               |         |            | future research |            | should | utilize | testbeds | and     | datasets    | with |
| --------------- | ------ | ---------- | -------------- | ----------- | ------------- | ------- | ---------- | --------------- | ---------- | ------ | ------- | -------- | ------- | ----------- | ---- |
| reduce backhaul |        | congestion |                | and latency |               | as they | are closer |                 |            |        |         |          |         |             |      |
|                 |        |            |                |             |               |         |            | real network    | conditions |        | rather  | than     | relying | on training | and  |
| to end users,   | making |            | them essential |             | for real-time |         | streaming  |                 |            |        |         |          |         |             |      |
evaluationwithinsimulatedenvironments.Inaddition,online
applications.Additionally,theyhavemuchhighercomputing
trainingtechniques,whichallowlearningmodelstobefine-
| capabilities, | allowing |     | them | to carry | out | computationally |     |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ---- | -------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tunedusinglivefeedback,canbeintegratedinlearning-based
intensivetasks,suchastraininglearningmodelsorapplying
streamingsystemstoimprovetheirreal-worldperformance.
videoenhancement.
Inaddition,thelackofend-to-endstreamingframeworksis
| Although | edge-assisted |     | video | streaming |     | has gained | more |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ----- | --------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
anotherchallengethathinderstheintegrationofMLinreal-
| attention      | over the     | past       | decade,      | there | are       | still several | open     |                   |            |         |               |                  |     |             |      |
| -------------- | ------------ | ---------- | ------------ | ----- | --------- | ------------- | -------- | ----------------- | ---------- | ------- | ------------- | ---------------- | --- | ----------- | ---- |
|                |              |            |              |       |           |               |          | world systems.    |            | Aspects | such          | as computational |     | complexity, |      |
| opportunities. | First,       | the        | coordination |       | and       | optimization  | of       |                   |            |         |               |                  |     |             |      |
|                |              |            |              |       |           |               |          | latency,          | and device |         | compatibility | must             | be  | considered  | on   |
| multi-edge     | environments |            | provides     | an    | open      | area of       | research |                   |            |         |               |                  |     |             |      |
|                |              |            |              |       |           |               |          | the system-level, |            | rather  | than          | component-level. |     | We          | have |
| for enhanced   | video        | streaming. |              | For   | instance, | dynamic       | task     |                   |            |         |               |                  |     |             |      |
toucheduponthistopicinSectionIV-A,discussingthelack
| offloading,     | which | determines |     | which     | enhancement |             | or infer- |             |             |               |     |            |        |               |       |
| --------------- | ----- | ---------- | --- | --------- | ----------- | ----------- | --------- | ----------- | ----------- | ------------- | --- | ---------- | ------ | ------------- | ----- |
|                 |       |            |     |           |             |             |           | of research | integrating |               | QoE | prediction | models | with          | other |
| ence operations |       | should     | be  | performed | at          | the client, | edge,     |             |             |               |     |            |        |               |       |
|                 |       |            |     |           |             |             |           | components  | of          | the streaming |     | system.    | More   | comprehensive |       |
orcloud,remainsanopenchallenge.Theschedulingofsuper-
streamingframeworksremainscarceinthecurrentliterature,
| resolution | or VQA | tasks | across | resource-constrained |     |     | edge |     |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | ------ | -------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
withfewexceptionsintheHASdomain[167],[204]andreal-
| devices introduces |     | a new | avenue | for | edge-assisted |     | adaptive |                     |     |     |        |           |     |          |          |
| ------------------ | --- | ----- | ------ | --- | ------------- | --- | -------- | ------------------- | --- | --- | ------ | --------- | --- | -------- | -------- |
|                    |     |       |        |     |               |     |          | time communications |     |     | [240]. | Designing | a   | holistic | pipeline |
streaming.Suchapproachescouldensurethatthecapabilities
thatjointlylearnsencodingdecisions,qualityadaptation,and
| of both | clients     | and | edge servers |         | are utilized | effectively |         |             |       |            |        |               |          |              |     |
| ------- | ----------- | --- | ------------ | ------- | ------------ | ----------- | ------- | ----------- | ----- | ---------- | ------ | ------------- | -------- | ------------ | --- |
|         |             |     |              |         |              |             |         | enhancement | under | real-world |        | constraints   | requires | address-     |     |
| without | overloading |     | the edge     | server, | a            | common      | problem |             |       |            |        |               |          |              |     |
|         |             |     |              |         |              |             |         | ing several | open  | questions. | First, | task-specific |          | optimization |     |
inedge-assistedschemes.Additionally,cooperativecaching
|     |     |     |     |     |     |     |     | must be | balanced | with | overall | QoE | gain. | For instance, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---- | ------- | --- | ----- | ------------- | --- |
acrossmultipleedgenodestooptimizecacheplacementfor
|     |     |     |     |     |     |     |     | ABR policies |     | that overly | prioritize | rebuffering |     | may | reduce |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | ---------- | ----------- | --- | --- | ------ |
bothhigh-demandcontentandenhancementmodelsremains
|     |     |     |     |     |     |     |     | perceptual | quality | when | not | aligned | with | super-resolution |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | --- | ------- | ---- | ---------------- | --- |
underexplored.
|     |     |     |     |     |     |     |     | timing. | Second,    | such | end-to-end | frameworks |         | must       | allow |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ---- | ---------- | ---------- | ------- | ---------- | ----- |
|     |     |     |     |     |     |     |     | modular | retraining | and  | A/B        | testing    | without | retraining | the   |
B. PRACTICALDEPLOYMENTCHALLENGES entire pipeline. Therefore, implementing such frameworks
Despiteremarkableadvancesinthefieldofvideostreaming, requires collaboration across systems and design of multi-
weobservethatthereremainsagapbetweencurrentresearch objective models, where LLMs are now being suggested
practicesandreal-worldstreamingapplications,particularly as a possible solution. The OpenNetLab [241] and Arse-
in the case of machine learning-based frameworks. This nal [242] frameworks, although developed for real-time
manifests in several aspects, such as the impractically communications (RTC), also offer a promising blueprint to
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 111155 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
addressthecriticallackofdedicatedtrainingandevaluation for video encoding, bandwidth optimization, and quality
tools for such streaming setups. They provide an integrated adaptation. It also highlights several promising directions
platform for training, evaluating, and deploying learning- for future research. While impressive advances have been
based congestion control agents in live streaming environ- made in simulated environments, real-world deployment
ments. A similar level of integration is currently missing continues to be hindered by generalization issues and
in HAS-based research. Addressing these challenges could practical constraints of latency, privacy, complexity, and
significantlyacceleratethetrainingandpracticaldeployment energyconsumption.Lookingforward,researchmusttarget
ofend-to-endlearning-basedABRmethods. the design of lightweight, adaptive ML models tailored for
Privacy concerns associated with ML must also be heterogeneousdevicesandthecreationofprivacy-preserving
addressed to make them feasible for real-world imple- architectures for user-centric streaming. Additionally, there
mentation. ML algorithms generally require large amounts is an urgent need for standardized evaluation benchmarks
of data for training, much of which involves user data, and end-to-end frameworks that unify diverse streaming
raisingconcernsaboutprivacy.Althoughprivacy-preserving components. By addressing these challenges, the next
machine learning techniques such as federated learning and generation of learning-based video streaming systems can
differential privacy have shown promise in enabling real- become more intelligent, personalized, and ready for real-
timeuserbehaviorinferencewithoutdirectdataaccess,they worlddeployment.
| remain limited | in   | several       | ways. | First,    | federated | learning |            |     |     |     |     |     |     |
| -------------- | ---- | ------------- | ----- | --------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| suffers from   | high | communication |       | overhead, | which     | can be   | REFERENCES |     |     |     |     |     |     |
problematic in low-bandwidth or mobile settings. Second, [1] (2023).2023GlobalInternetPhenomenaReport.[Online].Available:
ensuring convergence and stability in federated setups is https://www.sandvine.com/global-internet-phenomena-report-2024
|            |          |            |     |          |        |        | [2] HTTP | Live Streaming. | Accessed: | Apr. | 23, 2025. | [Online]. | Available: |
| ---------- | -------- | ---------- | --- | -------- | ------ | ------ | -------- | --------------- | --------- | ---- | --------- | --------- | ---------- |
| an ongoing | research | challenge, |     | as local | models | do not |          |                 |           |      |           |           |            |
https://developer.apple.com/streaming/
| always | converge | to the | same | global | model. | Moreover, |                |     |           |          |       |           |            |
| ------ | -------- | ------ | ---- | ------ | ------ | --------- | -------------- | --- | --------- | -------- | ----- | --------- | ---------- |
|        |          |        |      |        |        |           | [3] MPEG-DASH. |     | Accessed: | Apr. 23, | 2025. | [Online]. | Available: |
https://dashif.org/
| federated | learning | is vulnerable |     | to attacks, | such | as model |     |     |     |     |     |     |     |
| --------- | -------- | ------------- | --- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
[4] TwitchTranscodingOptions.Accessed:Jun.18,2025.[Online].Avail-
reconstruction.Differentialprivacy,amethodbywhichnoise
able:https://help.twitch.tv/s/article/transcoding-options-faq
| is added | to model | parameters |     | to protect | against | attacks, |     |     |     |     |     |     |     |
| -------- | -------- | ---------- | --- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
[5] K.Bilal,S.U.Khan,S.A.Madani,K.Hayat,M.I.Khan,N.Min-Allah,
oftendegradesmodelaccuracyduetothisadditionofnoise, J.Kolodziej,L.Wang,S.Zeadally,andD.Chen,‘‘Asurveyongreen
communicationsusingadaptivelinkrate,’’ClusterComput.,vol.16,no.3,
makingitlesssuitableforfine-grainedtaskssuchasquality
pp.575–589,Sep.2013.
adaptation. Therefore, there is a need for more research [6] R.S.ReshmaandJ.Thomas,‘‘Reviewonvideosuperresolution:Meth-
on privacy-preserving architectures tailored specifically for odsandmetrics,’’inProc.Int.Conf.Control,Commun.Comput.(ICCC),
videostreamingcontexts,withaccurate,secure,andreal-time 2023,pp.1–6.
[7] S.Yoo,G.Kim,M.Kim,Y.Kim,S.Park,andD.Kim,‘‘Machinelearning
performance. basedbandwidthpredictionfordynamicadaptivestreamingoverHTTP,’’
There are several security challenges and vulnerabilities J.Adv.Inf.Technol.Converg.,vol.10,no.2,pp.33–48,Dec.2020.
[8] N.Kan,C.Li,C.Yang,W.Dai,J.Zou,andH.Xiong,‘‘Uncertainty-
| introduced | by ML-based |     | streaming. | Some | of  | the major |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---------- | ---- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
awarerobustadaptivevideostreamingwithBayesianneuralnetworkand
| security | concerns | include | model | inversion | attacks, | which |     |     |     |     |     |     |     |
| -------- | -------- | ------- | ----- | --------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
modelpredictivecontrol,’’inProc.31stACMWorkshopNetw.Operating
can reconstruct private user data from model outputs, Syst.SupportDigit.AudioVideo,Jun.2021,pp.17–24.
|                 |          |           |       |         |            |        | [9] D. Yuan, | Y. Zhang, | W. Zhang,  | X.             | Liu, H.   | Du, and | Q. Zheng,  |
| --------------- | -------- | --------- | ----- | ------- | ---------- | ------ | ------------ | --------- | ---------- | -------------- | --------- | ------- | ---------- |
| and adversarial | attacks, |           | which | can use | defective  | inputs |              |           |            |                |           |         |            |
|                 |          |           |       |         |            |        | ‘‘PRIOR:     | Deep      | reinforced | adaptive video | streaming | with    | attention- |
| to mislead      | ML-based | streaming |       | models. | To address | these  |              |           |            |                |           |         |            |
basedthroughputprediction,’’inProc.32ndWorkshopNetw.Operating
challenges, blockchain technologies have emerged as a Syst.SupportDigit.AudioVideo,Jun.2022,pp.36–42.
[10] T.HoBfeld,M.Varela,P.E.Heegaard,andL.Skorin-Kapov,‘‘Obser-
promisingsolutionforenhancingthesecurity,transparency,
|     |     |     |     |     |     |     | vations | on emerging | aspects | in QoE | modeling | and | their impact |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------- | ------ | -------- | --- | ------------ |
anddecentralizationofMLsystems.Forexample,immutable
|     |     |     |     |     |     |     | on QoE | management,’’ | in  | Proc. 10th | Int. Conf. | Quality | Multimedia |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ---------- | ---------- | ------- | ---------- |
ledgerscanensureintegrityandtraceabilityoftrainingdata Exp.(QoMEX),May2018,pp.1–6.
andmodelupdates,whilesmartcontractscanenforceaccess [11] N. T. Blog. VMAF: The Journey Continues. Accessed: May 20,
2025.[Online].Available:https://netflixtechblog.com/vmaf-the-journey-
| control over | user | data or | encoded | streams. | Consequently, |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------- | ------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
continues-44b51ee9ed12
recentresearch[243],[244]focusesoncombiningblockchain [12] C.Qiao,J.Wang,andY.Liu,‘‘BeyondQoE:Diversityadaptationin
with ML, enabling video streaming platforms to achieve videostreamingattheedge,’’IEEE/ACMTrans.Netw.,vol.29,no.1,
pp.289–302,Feb.2021.
stronger guarantees of data integrity and user privacy, [13] J.Jiang,V.Sekar,andH.Zhang,‘‘Improvingfairness,efficiency,and
especiallyincollaborativeorcrowd-sourcedenvironments. stabilityinHTTP-basedadaptivevideostreamingwithFESTIVE,’’in
|     |     |     |     |     |     |     | Proc. | 8th Int. Conf. | Emerg. | Netw. Experiments |     | Technol., | Dec. 2012, |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | ------ | ----------------- | --- | --------- | ---------- |
pp.97–108.
VI. CONCLUSION
|     |     |     |     |     |     |     | [14] T.-Y. | Huang, R. | Johari, N. | McKeown, | M. Trunnell, | and | M. Watson, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ---------- | -------- | ------------ | --- | ---------- |
This paper provides a comprehensive review of recent ‘‘Abuffer-basedapproachtorateadaptation:Evidencefromalargevideo
streamingservice,’’SIGCOMMComput.Commun.Rev.,vol.44,no.4,
| advancements | in  | the application |     | of machine |     | learning for |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
pp.187–198,2014.
| HTTP adaptive | video | streaming. |     | It examines |     | the chal- |     |     |     |     |     |     |     |
| ------------- | ----- | ---------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[15] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman,‘‘BOLA:Near-optimal
| lenges faced | by existing |     | streaming | systems | and | outlines |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | --------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
bitrateadaptationforonlinevideos,’’IEEE/ACMTrans.Netw.,vol.28,
no.4,pp.1698–1711,Aug.2020.
| the potential | advantages |     | of employing |     | machine | learning |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
[16] H.Mao,R.Netravali,andM.Alizadeh,‘‘Neuraladaptivevideostreaming
| algorithms | to overcome |     | these | obstacles. | The | paper cat- |                  |     |                |     |         |          |            |
| ---------- | ----------- | --- | ----- | ---------- | --- | ---------- | ---------------- | --- | -------------- | --- | ------- | -------- | ---------- |
|            |             |     |       |            |     |            | with pensieve,’’ |     | in Proc. Conf. | ACM | Special | Interest | Group Data |
egorizes and compares machine learning-based methods Commun.,Aug.2017,pp.197–210.
| 111156 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
[17] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,‘‘Comyco: [39] J.Yang,M.Guo,S.Zhao,J.Li,andL.Zhang,‘‘Optimaltranscoding
Quality-aware adaptive video streaming via imitation learning,’’ in resolutionpredictionforefficientper-titlebitrateladderestimation,’’in
Proc.27thACMInt.Conf.Multimedia,Oct.2019,pp.429–437. Proc.DataCompress.Conf.(DCC),Mar.2024,p.597.
[18] L. Jia, C. Zhou, T. Huang, C. Li, and L. Sun, ‘‘Dancing with [40] (2018). Instant Per-Title Encoding. [Online]. Available:
shackles,meetthechallengeofindustrialadaptivestreamingviaoffline https://www.mux.com/blog/instant-per-title-encoding
|     |     |     | Proc. | IEEE Conf. | Comput. | Commun., |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
reinforcement learning,’’ in [41] (2020). Per-Title Encoding. [Online]. Available:
May2024,pp.2169–2178.
https://bitmovin.com/encoding-service/per-title-encoding/
[19] F.Y.Yan,H.Ayers,C.Zhu,S.Fouladi,J.Hong,K.Zhang,P.Levis,
|     |     |     |     |     |     |     | [42] D.Silhavy,C.Krauss,A.Chen,A.-T.Nguyen,C.Müller,S.Arbanowski, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
andK.Winstein,‘‘Learninginsitu:Arandomizedexperimentinvideo
S.Steglich,andL.Bassbouss,‘‘Machinelearningforper-titleencoding,’’
| streaming,’’ | in Proc. | 17th | USENIX | Symp. | Networked Syst. | Design |     |     |     |     |     |     |     |
| ------------ | -------- | ---- | ------ | ----- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
SMPTEMotionImag.J.,vol.131,no.3,pp.42–50,Apr.2022.
Implement.(NSDI),Jan.2019,pp.495–511.
|              |              |     |            |            |         |            | [43] J.AdhuranandG.Kulupana,‘‘Content-awareconvexhullprediction,’’in |     |     |     |     |     |     |
| ------------ | ------------ | --- | ---------- | ---------- | ------- | ---------- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| [20] J. Kua, | G. Armitage, | and | P. Branch, | ‘‘A survey | of rate | adaptation |                                                                      |     |     |     |     |     |     |
techniques for dynamic adaptive streaming over HTTP,’’ IEEE Com- Proc.2ndMile-HighVideoConf.,vol.1,May2023,pp.1–7.
mun.SurveysTuts.,vol.19,no.3,pp.1842–1866,3rdQuart.,2017. [44] A.V.Katsenou,F.Zhang,K.Swanson,M.Afonso,J.Sole,andD.R.Bull,
[21] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann, ‘‘VMAF-based bitrate ladder estimation for adaptive streaming,’’ in
Proc.PictureCodingSymp.(PCS),Jun.2021,pp.1–5.
| ‘‘A | survey on bitrate | adaptation |     | schemes for | streaming media | over |     |     |     |     |     |     |     |
| --- | ----------------- | ---------- | --- | ----------- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
HTTP,’’ IEEE Commun. Surveys Tuts., vol. 21, no. 1, pp.562–585, [45] A. V. Katsenou, J. Sole, and D. R. Bull, ‘‘Efficient bitrate ladder
1stQuart.,2019. construction for content-optimized adaptive video streaming,’’ IEEE
[22] R.Farahani,Z.Azimi,C.Timmerer,andR.Prodan,‘‘TowardsAI-assisted OpenJ.SignalProcess.,vol.2,pp.496–511,2021.
sustainableadaptivevideostreamingsystems:Tutorialandsurvey,’’2024, [46] V.V.Menon,A.Premkumar,P.T.Rajendran,A.Wieckowski,B.Bross,
arXiv:2406.02302. C.Timmerer,andD.Marpe,‘‘Energy-efficientadaptivevideostreaming
[23] L. Peroni and S. Gorinsky, ‘‘An end-to-end pipeline perspective on with latency-aware dynamic resolution encoding,’’ in Proc. 3rd Mile-
videostreaminginbest-effortnetworks:Asurveyandtutorial,’’2024,
HighVideoConf.,Feb.2024,pp.21–27.
arXiv:2403.05192.
|     |     |     |     |     |     |     | [47] F. Nasiri, | W. Hamidouche, |     | L. Morin, | N. Dholland, | and | J.-Y. Aubié, |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | --- | --------- | ------------ | --- | ------------ |
[24] T.Wiegand,G.J.Sullivan,G.Bjøntegaard,andA.Luthra,‘‘Overviewof
|     |     |     |     |     |     |     | ‘‘Ensemble | learning | for | efficient | VVC bitrate | ladder prediction,’’ | in  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --------- | ----------- | -------------------- | --- |
theH.264/AVCvideocodingstandard,’’IEEETrans.CircuitsSyst.Video Proc.10thEur.WorkshopVis.Inf.Process.(EUVIP),Sep.2022,pp.1–6.
Technol.,vol.13,no.7,pp.560–576,Jul.2003.
|     |     |     |     |     |     |     | [48] F. Nasiri, | W. Hamidouche, |     | L. Morin, | N. Dhollande, | and | J.-Y. Aubié, |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | --- | --------- | ------------- | --- | ------------ |
[25] G.J.Sullivan,J.-R.Ohm,W.-J.Han,andT.Wiegand,‘‘Overviewofthe ‘‘Multi-preset video encoder bitrate ladder prediction,’’ in Proc. 2nd
highefficiencyvideocoding(HEVC)standard,’’IEEETrans.Circuits
Int.WorkshopDesign,Dec.2022,pp.8–13.
Syst.VideoTechnol.,vol.22,no.12,pp.1649–1668,Dec.2012.
|     |     |     |     |     |     |     | [49] P.-H. | Wu, V. | Kondratenko, | G.  | Chaudhari, | and I. Katsavounidis, |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | ---------- | --------------------- | --- |
[26] A.Mercat,A.Mäkinen,J.Sainio,A.Lemmetti,M.Viitanen,andJ.Vanne,
‘‘Encodingparameterspredictionforconvexhullvideoencoding,’’in
| ‘‘Comparative | rate-distortion-complexity |     |     | analysis | of VVC and | HEVC |     |     |     |     |     |     |     |
| ------------- | -------------------------- | --- | --- | -------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Proc.PictureCodingSymp.(PCS),Jun.2021,pp.1–5.
videocodecs,’’IEEEAccess,vol.9,pp.67813–67828,2021.
|     |     |     |     |     |     |     | [50] L.Jia,C.Zhou,T.Huang,C.Li,andL.Sun,‘‘RDladder:Resolution- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[27] J.S.Gomes,M.Grellert,F.L.L.Ramos,andS.Bampi,‘‘End-to-end
neuralvideocompression:Areview,’’IEEEOpenJ.CircuitsSyst.,vol.6, duration ladder for VBR-encoded videos via imitation learning,’’ in
| pp.120–134,2025. |     |     |     |     |     |     | Proc.IEEEINFOCOM,May2023,pp.1–10. |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
[28] C. Jia, S. Wang, X. Zhang, S. Wang, J. Liu, S. Pu, and S. Ma, [51] Y.Wu,L.Xie,S.Sun,W.Gao,andY.Yan,‘‘Adaptiveintraperiodsize
‘‘Content-awareconvolutionalneuralnetworkforin-loopfilteringinhigh for deep learning-based screen content video coding,’’ in Proc. IEEE
Int.Conf.MultimediaExpoWorkshops(ICMEW),Jul.2024,pp.1–6.
efficiencyvideocoding,’’IEEETrans.ImageProcess.,vol.28,no.7,
pp.3343–3356,Jul.2019. [52] H. Amirpour, M. Ghanbari, and C. Timmerer, ‘‘DeepStream: Video
[29] T. Li, M. Xu, and X. Deng, ‘‘A deep convolutional neural network streamingenhancementsusingcompresseddeepneuralnetworks,’’IEEE
approachforcomplexityreductiononintra-modeHEVC,’’inProc.IEEE Trans. Circuits Syst. Video Technol., vol. 35, no. 4, pp.3786–3797,
| Int.Conf.MultimediaExpo(ICME),Jul.2017,pp.1255–1260. |     |     |     |     |     |     | Apr.2025. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[30] G. Lu, W. Ouyang, D. Xu, X. Zhang, C. Cai, and Z. Gao, [53] S. Wiedemann, H. Kirchhoffer, S. Matlage, P. Haase, A. Marban,
‘‘DVC: An end-to-end deep video compression framework,’’ in T.Marinc,D.Neumann,T.Nguyen,H.Schwarz,T.Wiegand,D.Marpe,
Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), andW.Samek,‘‘DeepCABAC:Auniversalcompressionalgorithmfor
Jun.2019,pp.10998–11007. deepneuralnetworks,’’IEEEJ.Sel.TopicsSignalProcess.,vol.14,no.4,
[31] W.Gao,S.Sun,H.Zheng,Y.Wu,H.Ye,andY.Zhang,‘‘OpenDMC:An pp.700–714,May2020.
open-sourcelibraryandperformanceevaluationfordeep-learning-based [54] C. Mueller, L. Bassbouss, S. Pham, S. Steglich, S. Wischnowsky,
multi-frame compression,’’ in Proc. 31st ACM Int. Conf. Multimedia, P. Pogrzeba, and T. Buchholz, ‘‘Context-aware video encoding as a
Oct.2023,pp.9685–9688. network-basedmediaprocessing(NBMP)workflow,’’inProc.13thACM
[32] E. Agustsson, D. Minnen, N. Johnston, J. Ball, S. J. Hwang, and MultimediaSyst.Conf.,Jun.2022,pp.293–298.
G.Toderici,‘‘Scale-spaceflowforend-to-endoptimizedvideocompres-
|     |     |     |     |     |     |     | [55] T.Huang,R.-X.Zhang,andL.Sun,‘‘Deepreinforcedbitrateladdersfor |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
sion,’’inProc.IEEE/CVFConf.Comput.Vis.PatternRecognit.(CVPR),
adaptivevideostreaming,’’inProc.31stACMWorkshopNetw.Operating
Jun.2020,pp.8500–8509.
Syst.SupportDigit.AudioVideo,Jul.2021,pp.66–73.
| [33] J. Li, | B. Li, and | Y. Lu, | ‘‘Deep | contextual | video compression,’’ | in  |                                                                |     |     |     |     |     |     |
| ----------- | ---------- | ------ | ------ | ---------- | -------------------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|             |            |        |        |            |                      |     | [56] V.V.Menon,H.Amirpour,C.Feldmann,M.Ghanbari,andC.Timmerer, |     |     |     |     |     |     |
Proc.Adv.NeuralInf.Process.Syst.,Sep.2021,pp.18114–18125.
‘‘OPSE:Onlineper-sceneencodingforadaptivehttplivestreaming,’’in
[34] S.Zhang,M.Mrak,L.Herranz,M.G.Blanch,S.Wan,andF.Yang, Proc.IEEEInt.Conf.MultimediaExpoWorkshops(ICMEW),Jul.2022,
| ‘‘DVC-P: | Deep video | compression |     | with perceptual | optimizations,’’ | in  |     |     |     |     |     |     |     |
| -------- | ---------- | ----------- | --- | --------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.1–4.
| Proc. | Int. Conf. | Vis. Commun. | Image | Process. | (VCIP), Dec. | 2021, |            |               |             |     |            |                |       |
| ----- | ---------- | ------------ | ----- | -------- | ------------ | ----- | ---------- | ------------- | ----------- | --- | ---------- | -------------- | ----- |
|       |            |              |       |          |              |       | [57] N. T. | Blog. Dynamic | Optimizer—A |     | Perceptual | Video Encoding | Opti- |
pp.1–5.
|     |     |     |     |     |     |     | mization | Framework. | Accessed: |     | Apr. 17, 2025. | [Online]. | Avail- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | --- | -------------- | --------- | ------ |
[35] H.Kim,M.Bauer,L.Theis,J.R.Schwarz,andE.Dupont,‘‘C3:High-
able:https://netflixtechblog.com/dynamic-optimizer-a-perceptual-video-
performanceandlow-complexityneuralcompressionfromasingleimage
or video,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., encoding-optimization-framework-e19f1e3a277f
Jan.2023,pp.9347–9358. [58] A.Zabrovskiy,P.Agrawal,C.Timmerer,andR.Prodan,‘‘FAUST:Fast
[36] FFMPEG. Accessed: May 15, 2025. [Online]. Available: per-scene encoding using entropy-based scene detection and machine
learning,’’inProc.30thConf.OpenInnov.Assoc.FRUCT,Oct.2021,
https://ffmpeg.org
pp.292–302.
| [37] J. De | Cock, Z. Li, | M. Manohara, |     | and A. Aaron, | ‘‘Complexity-based |     |                                                                     |     |     |     |     |     |     |
| ---------- | ------------ | ------------ | --- | ------------- | ------------------ | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |              |              |     |               |                    |     | [59] S.Paul,A.Norkin,andA.C.Bovik,‘‘Convexhullpredictionforadaptive |     |     |     |     |     |     |
consistent-qualityencodinginthecloud,’’inProc.IEEEInt.Conf.Image
Process.(ICIP),Aug.2016,pp.1484–1488. videostreamingbyrecurrentlearning,’’2022,arXiv:2206.04877.
[38] A. Katsenou, J. Solé, and D. Bull, ‘‘Content-gnostic bitrate ladder [60] H. Xing, Z. Zhou, J. Wang, H. Shen, D. He, and F. Li, ‘‘Predicting
prediction for adaptive video streaming,’’ in Proc. Picture Coding ratecontroltargetthroughalearningbasedcontentadaptivemodel,’’in
Symp.(PCS),Nov.2019,pp.1–5. Proc.PictureCodingSymp.(PCS),Nov.2019,pp.1–5.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 111157 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
[61] A. Falahati, M. K. Safavi, A. Elahi, F. Pakdaman, and M. Gabbouj, [80] H.Yeo,S.Do,andD.Han,‘‘HowwilldeeplearningchangeInternetvideo
‘‘Efficientbitrateladderconstructionusingtransferlearningandspatio- delivery?’’inProc.16thACMWorkshopHotTopicsNetw.,Nov.2017,
| temporal | features,’’ | in Proc. | 13th | Iranian/3rd | Int. Mach. | Vis. Image | p.57. |     |     |     |     |     |     |     |
| -------- | ----------- | -------- | ---- | ----------- | ---------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Process.Conf.(MVIP),Mar.2024,pp.1–7. [81] H.Yeo,Y.Jung,J.Kim,J.Shin,andD.Han,‘‘Neuraladaptivecontent-
[62] A. Telili, W. Hamidouche, S. A. Fezza, and L. Morin, ‘‘Efficient awareInternetvideodelivery,’’inProc.13thUSENIXConf.Operating
per-shottransformer-basedbitrateladderpredictionforadaptivevideo Syst.DesignImplement.,Oct.2018,pp.645–661.
streaming,’’inProc.IEEEInt.Conf.ImageProcess.(ICIP),Sep.2023, [82] Y.Zhang,Y.Zhang,Y.Wu,Y.Tao,K.Bian,P.Zhou,L.Song,andH.Tuo,
pp.1835–1839. ‘‘Improving quality of experience by adaptive video streaming with
[63] M. Bhat, J.-M. Thiesse, and P. L. Callet, ‘‘A case study of machine super-resolution,’’ in Proc. IEEE Conf. Comput. Commun., Jul. 2020,
| learningclassifiersforreal-timeadaptiveresolutionpredictioninvideo |     |     |     |     |     |     | pp.1957–1966. |     |     |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
coding,’’inProc.IEEEInt.Conf.MultimediaExpo(ICME),Jun.2020, [83] W.Huang,Y.Ran,J.Rao,J.Luo,andS.Chen,‘‘Queue-learning-based
pp.1–6. QoE optimization for super-resolution-assisted adaptive video stream-
[64] A. Telili, W. Hamidouche, S. A. Fezza, and L. Morin, ‘‘Bench- ing,’’inProc.IEEEGlobalCommun.Conf.,Dec.2023,pp.140–145.
markinglearning-basedbitrateladderpredictionmethodsforadaptive [84] C.Dong,C.C.Loy,K.He,andX.Tang,‘‘Imagesuper-resolutionusing
deepconvolutionalnetworks,’’IEEETrans.PatternAnal.Mach.Intell.,
| video       | streaming,’’ | in Proc. | Picture | Coding | Symp. (PCS), | Dec. 2022, |                                  |     |     |     |     |     |     |     |
| ----------- | ------------ | -------- | ------- | ------ | ------------ | ---------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| pp.325–329. |              |          |         |        |              |            | vol.38,no.2,pp.295–307,Feb.2016. |     |     |     |     |     |     |     |
[65] V. V. Menon, J. Zhu, P. T. Rajendran, S. Afzal, K. Schoeffmann, [85] W. Shi, J. Caballero, F. Huszár, J. Totz, A. P. Aitken, R.Bishop,
P.LeCallet, and C. Timmerer, ‘‘Optimal quality and efficiency in D.Rueckert,andZ.Wang,‘‘Real-timesingleimageandvideosuper-
adaptive live streaming with JND-aware low latency encoding,’’ in resolution using an efficient sub-pixel convolutional neural network,’’
Proc.3rdMile-HighVideoConf.,Feb.2024,pp.61–67. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), vol. 2016,
pp.1874–1883,Jun.2016.
| [66] F. Micó-Enguídanos, |                   | W.          | A. Moina-Rivera, |        | J. Gutiérrez-Aguado, | and              |                |           |                     |          |          |            |            |            |
| ------------------------ | ----------------- | ----------- | ---------------- | ------ | -------------------- | ---------------- | -------------- | --------- | ------------------- | -------- | -------- | ---------- | ---------- | ---------- |
|                          |                   |             |                  |        |                      |                  | [86] Y. Zhang, | Y.        | Tian, Y.            | Kong, B. | Zhong,   | and Y. Fu, | ‘‘Residual | dense      |
| M. García-Pineda,        |                   | ‘‘Per-title | and per-segment  |        | CRF                  | estimation using |                |           |                     |          |          |            |            |            |
|                          |                   |             |                  |        |                      |                  | network        | for image | super-resolution,’’ |          | in Proc. | IEEE/CVF   |            | Conf. Com- |
| DNNs                     | for quality-based |             | video coding,’’  | Expert | Syst.                | Appl., vol. 227, |                |           |                     |          |          |            |            |            |
Oct.2023,Art.no.120289. put.Vis.PatternRecognit.,Jun.2018,pp.2472–2481.
[67] S. Huang and J. Xie, ‘‘DAVE: Dynamic adaptive video encoding for [87] J. Liu, J. Tang, and G. Wu, ‘‘Residual feature distillation network
real-time video streaming applications,’’ in Proc. 18th Annu. IEEE for lightweight image super-resolution,’’ in Proc. Comput. Vis.-ECCV
| Int.Conf.Sens.,Jul.2021,pp.1–9. |     |     |     |     |     |     | Workshops,Jan.2020,pp.41–55. |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
[68] B.O.Turkkan,T.Dai,A.Raman,T.Kosar,C.Chen,M.F.Bulut,J.Zola, [88] X. Wang, K. Yu, S. Wu, J. Gu, Y. Liu, C. Dong, Y. Qiao, and
C.C.Loy,‘‘ESRGAN:Enhancedsuper-resolutiongenerativeadversarial
andD.Sow,‘‘GreenABR:Energy-awareadaptivebitratestreamingwith
networks,’’Proc.Eur.Conf.Comput.Vis.(ECCV)workshops,vol.11133,
deepreinforcementlearning,’’inProc.13thACMMultimediaSyst.Conf.,
pp.63–79,Jan.2019.
2022,pp.150–163.
[89] H.Yeo,C.J.Chong,Y.Jung,J.Ye,andD.Han,‘‘NEMO:Enabling
[69] A.Bentaleb,M.Lim,M.N.Akcay,A.C.Begen,andR.Zimmermann,
‘‘Bitrate adaptation and guidance with meta reinforcement learning,’’ neural-enhanced video streaming on commodity mobile devices,’’ in
Proc.26thAnnu.Int.Conf.MobileComput.Netw.(MobiCom),Sep.2020,
| IEEE | Trans. | Mobile Comput., | vol. | 23, | no. 11, pp.10378–10392, |     |     |     |     |     |     |     |     |     |
| ---- | ------ | --------------- | ---- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.363–376.
Nov.2024.
[90] Q.Yu,Q.Li,R.He,G.Tyson,W.Shi,J.Lv,Z.Yuan,P.Zhang,Y.Lan,
| [70] S.-Z. | Qian, | Y. Xie, Z. | Pan, Y. Zhang, | and | T. Lin, | ‘‘DAM: Deep |     |     |     |     |     |     |     |     |
| ---------- | ----- | ---------- | -------------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
andZ.Li,‘‘BiSR:Bidirectionallyoptimizedsuper-resolutionformobile
| reinforcement |     | learning based | preload | algorithm | with | action masking |     |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | ------- | --------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
videostreaming,’’inProc.ACMWebConf.,Apr.2023,pp.3121–3131.
forshortvideostreaming,’’inProc.30thACMInt.Conf.Multimedia,
Oct.2022,pp.7030–7034. [91] W. Shen, W. Bao, G. Zhai, C. L. Wang, J. W. Hu, and Z. Gao,
‘‘Prediction-assistantframesuper-resolutionforvideostreaming,’’2021,
[71] Y. Li, Q. Zheng, Z. Zhang, H. Chen, and Z. Ma, ‘‘Improving ABR arXiv:2103.09455.
performanceforshortvideostreamingusingmulti-agentreinforcement
|     |     |     |     |     |     |     | [92] C. Li, | D. He, | X. Liu, | Y. Ding, | and S. Wen, | ‘‘Adapting | image | super- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------- | -------- | ----------- | ---------- | ----- | ------ |
learningwithexpertguidance,’’inProc.33rdWorkshopNetw.Operating
resolutionstate-of-the-artsandlearningmulti-modelensembleforvideo
Syst.SupportDigit.AudioVideo,May2023,pp.58–64.
super-resolution,’’2019,arXiv:1905.02462.
[72] H.Su,S.Wang,S.Yang,T.Huang,andX.Ren,‘‘Reducingtrafficwastage
|          |           |     |                     |     |                       |      | [93] B. Lim, | S. Son,  | H. Kim,    | S. Nah, | and K.              | M. Lee, | ‘‘Enhanced | deep       |
| -------- | --------- | --- | ------------------- | --- | --------------------- | ---- | ------------ | -------- | ---------- | ------- | ------------------- | ------- | ---------- | ---------- |
| in video | streaming | via | bandwidth-efficient |     | bitrate adaptation,’’ | IEEE |              |          |            |         |                     |         |            |            |
|          |           |     |                     |     |                       |      | residual     | networks | for single | image   | super-resolution,’’ |         | in         | Proc. IEEE |
Trans.MobileComput.,vol.23,no.11,pp.10361–10377,Nov.2024.
Conf.Comput.Vis.PatternRecognit.Workshops(CVPRW),Jul.2017,
[73] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,andL.Sun,‘‘Bufferawareness pp.1132–1140.
neuraladaptivevideostreamingforavoidingextrabufferconsumption,’’ [94] Y.Zhang,K.Li,K.Li,L.Wang,B.Zhong,andY.Fu,‘‘Imagesuper-
inProc.IEEEConf.Comput.Commun.,May2023,pp.1–10.
|     |     |     |     |     |     |     | resolution | using | very | deep residual | channel | attention | networks,’’ | in  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---- | ------------- | ------- | --------- | ----------- | --- |
[74] B. Palit, A. Sen, A. Mondal, A. Zunaid, J. Jayatheerthan, and Proc.Eur.Conf.Comput.Vis.(ECCV),Jan.2018,pp.294–310.
| S. Chakraborty, |     | ‘‘Improving | UE energy | efficiency | through | network- |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --------- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[95] Z.Zhao,L.Song,R.Xie,andX.Yang,‘‘GPUacceleratedhigh-quality
awarevideostreamingover5G,’’IEEETrans.Netw.ServiceManage.,
|     |     |     |     |     |     |     | video/image | super-resolution,’’ |     |     | in Proc. IEEE | Int. | Symp. | Broadband |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | --- | --- | ------------- | ---- | ----- | --------- |
vol.20,no.3,pp.3487–3500,Sep.2023.
MultimediaSyst.Broadcast.(BMSB),Jun.2016,pp.1–4.
| [75] S. Nami, | F.  | Pakdaman, | M. R. Hashemi, |     | S. Shirmohammadi, | and |     |     |     |     |     |     |     |     |
| ------------- | --- | --------- | -------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[96] W.Jing,C.Liu,H.Cai,X.Wen,Z.Lu,Z.Wang,andH.Zhang,‘‘MEC-
M.Gabbouj,‘‘LightweightmultitasklearningforrobustJNDprediction basedsuper-resolutionenhancedadaptivevideostreamingoptimization
using latent space and reconstructed frames,’’ IEEE Trans. Circuits formobilenetworkswithsatellitebackhaul,’’IEEETrans.Netw.Service
Syst.VideoTechnol.,vol.34,no.9,pp.8657–8671,Sep.2024.
Manage.,vol.21,no.3,pp.2977–2991,Jun.2024.
[76] M.Takeuchi,S.Saika,Y.Sakamoto,T.Nagashima,Z.Cheng,K.Kanai, [97] J.D.M.L.FilhoandC.A.V.Melo,‘‘AGANtofightvideo-relatedtraffic
| J. Katto, | B.  | Wei, J. Zengwei, | and | X. Wei, | ‘‘Perceptual | quality driven |           |                     |     |     |            |             |       |      |
| --------- | --- | ---------------- | --- | ------- | ------------ | -------------- | --------- | ------------------- | --- | --- | ---------- | ----------- | ----- | ---- |
|           |     |                  |     |         |              |                | flooding: | Super-resolution,’’ |     | in  | Proc. IEEE | Latin-Amer. | Conf. | Com- |
adaptivevideocodingusingJNDestimation,’’inProc.PictureCoding
mun.(LATINCOM),Nov.2019,pp.1–6.
Symp.(PCS),Jun.2018,pp.179–183.
|     |     |     |     |     |     |     | [98] A. Zhang, | Q.  | Li, Y. Chen, | X.  | Ma, L. | Zou, Y. | Jiang, Z. | Xu, and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------ | ------- | --------- | ------- |
[77] V.V.Menon,R.Farahani,P.T.Rajendran,S.Afzal,K.Schoeffmann,and G.-M.Muntean,‘‘Videosuper-resolutionandcaching—Anedge-assisted
C.Timmerer,‘‘Energy-efficientmulti-codecbitrate-ladderestimationfor adaptive video streaming solution,’’ IEEE Trans. Broadcast., vol. 67,
adaptivevideostreaming,’’inProc.IEEEInt.Conf.Vis.Commun.Image no.4,pp.799–812,Dec.2021.
Process.(VCIP),Dec.2023,pp.1–5.
[99] J.D.M.L.Filho,M.D.S.Coelho,andC.A.V.Melo,‘‘Super-resolution
[78] V.V.Menon,P.T.Rajendran,A.Premkumar,B.Bross,andD.Marpe, onedgecomputingforimprovedadaptiveHTTPlivestreamingdelivery,’’
‘‘Videosuper-resolutionforoptimizedbitrateandgreenonlinestream-
|                                                       |     |     |     |     |     |     | in Proc.    | IEEE | 10th Int. | Conf. | Cloud Netw. | (CloudNet), |     | Nov. 2021, |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --------- | ----- | ----------- | ----------- | --- | ---------- |
| ing,’’inProc.PictureCodingSymp.(PCS),Jun.2024,pp.1–5. |     |     |     |     |     |     | pp.104–110. |      |           |       |             |             |     |            |
[79] S.S.Andrei,N.Shapovalova,andW.Mayol-Cuevas,‘‘SUPERVEGAN: [100] X.Liu,Z.Ke,X.Zhou,T.Qiu,andK.Li,‘‘QoE-orientedadaptivevideo
SuperresolutionvideoenhancementGANforperceptuallyimproving streamingwithedge-clientcollaborativesuper-resolution,’’inProc.IEEE
lowbitratestreams,’’IEEEAccess,vol.9,pp.91160–91174,2021. GlobalCommun.Conf.,Dec.2022,pp.6158–6163.
| 111158 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
[101] J.D.M.LibórioFilho,J.Oliveira,andC.A.V.Melo,‘‘Super-resolution [123] Z.Shi,Y.Zhou,D.Wu,andC.Wang,‘‘PPVC:Onlinelearningtoward
with perceptual quality for improved live streaming delivery on edge optimized video content caching,’’ IEEE/ACM Trans. Netw., vol. 30,
computing,’’Comput.Netw.,vol.248,Jun.2024,Art.no.110463. no.3,pp.1029–1044,Dec.2021.
[102] R. Wu, W. Bao, L. Ge, and B. B. Zhou, ‘‘ASRSR: Adaptive sending [124] G.-E.-L. Gul-E-Laraib, S. K. U. Zaman, T. Maqsood, F. Rehman,
resolution and super-resolution for real-time video streaming,’’ in S.Mustafa,M.A.Khan,N.Gohar,A.D.Algarni,andH.Elmannai,
Proc.19thACMInt.Symp.QoSSecur.WirelessMobileNetw.,Oct.2023, ‘‘Content caching in mobile edge computing based on user location
pp.61–68. and preferences using cosine similarity and collaborative filtering,’’
[103] M. S. M. Sajjadi, R. Vemulapalli, and M. Brown, ‘‘Frame-recurrent Electronics,vol.12,no.2,p.284,Jan.2023.
videosuper-resolution,’’inProc.IEEE/CVFConf.Comput.Vis.Pattern [125] D.Huang,X.Tao,C.Jiang,Y.Li,andJ.Lü,‘‘Latency-efficientvideo
Recognit.,Jun.2018,pp.6626–6634. streaminginmetropolis:Acachingframework,’’inProc.IEEEGlobal
[104] J. Kim, Y. Jung, H. Yeo, J. Ye, and D. Han, ‘‘Neural-enhanced Commun.Conf.,Dec.2017,pp.1–6.
live streaming: Improving live video ingest via online learning,’’ [126] S.M.S.Tanzil,W.Hoiles,andV.Krishnamurthy,‘‘Adaptivescheme
Proc.Annu.Conf.ACMSpecialInterestGroupDataCommun.Appl., for caching YouTube content in a cellular network: Machine learning
Technol.,Archit.,ProtocolsComput.Commun.,pp.107–125,2020. approach,’’IEEEAccess,vol.5,pp.5870–5881,2017.
[105] Z.Duanmu,A.Rehman,andZ.Wang,‘‘Aquality-of-experiencedatabase [127] K.N.Doan,T.VanNguyen,T.Q.S.Quek,andH.Shin,‘‘Content-aware
foradaptivevideostreaming,’’IEEETrans.Broadcast.,vol.64,no.2, proactive caching for backhaul offloading in cellular network,’’ IEEE
pp.474–487,Jun.2018. Trans.WirelessCommun.,vol.17,no.5,pp.3128–3140,May2018.
[106] Z.He,Y.Yang,L.Qiu,K.Park,andY.Yang,‘‘NERVE:Real-timeneural [128] Z.Li,J.Li,Q.Wu,G.Tyson,andG.Xie,‘‘Alarge-scalemeasurement
videorecoveryandenhancementonmobiledevices,’’Proc.ACMNetw., andoptimizationofmobilelivestreamingservices,’’IEEETrans.Mobile
vol.2,no.1,pp.1–19,Mar.2024. Comput.,vol.21,no.11,pp.1–16,Nov.2022.
[107] M.Choi,W.J.Yun,S.B.Son,S.Park,andJ.Kim,‘‘Jointdelay-sensitive [129] X. Ma, Q. Li, L. Zou, J. Peng, J. Zhou, J. Chai, Y. Jiang, and
and power-efficient quality control of dynamic video streaming using G.-M.Muntean,‘‘QAVA:QoE-awareadaptivevideobitrateaggregation
adaptivesuper-resolution,’’IEEETrans.GreenCommun.Netw.,vol.8, for HTTP live streaming based on smart edge computing,’’ IEEE
no.1,pp.103–117,Sep.2023. Trans.Broadcast.,vol.68,no.3,pp.661–676,Sep.2022.
[108] S. Jin, R. Zhu, A. Hassan, X. Zhu, X. Zhang, Z. M. Mao, F. Qian, [130] J.J.QuinlanandC.J.Sreenan,‘‘Multi-profileultrahighdefinition(UHD)
andZ.-L.Zhang,‘‘OASIS:Collaborativeneural-enhancedmobilevideo AVC and HEVC 4K DASH datasets,’’ in Proc. 9th ACM Multimedia
streaming,’’inProc.ACMMultimediaSyst.Conf.,Apr.2024,pp.45–55. Syst.Conf.,Jun.2018,pp.375–380.
[109] S. Wang, J. Yang, and S. Bi, ‘‘Adaptive video streaming in multi-tier [131] S.Lederer,C.Müller,andC.Timmerer,‘‘Dynamicadaptivestreaming
computingnetworks:Jointedgetranscodingandclientenhancement,’’ over HTTP dataset,’’ in Proc. 3rd Multimedia Syst. Conf., Feb. 2012,
IEEETrans.MobileComput.,vol.18,no.6,pp.1–14,Jun.2023. pp.89–94.
[110] J. Yang, Y. Jiang, and S. Wang, ‘‘Enhancement or super-resolution: [132] A. Zabrovskiy, C. Feldmann, and C. Timmerer, ‘‘Multi-codec DASH
Learning-basedadaptivevideostreamingwithclient-sidevideoprocess- dataset,’’ in Proc. 9th ACM Multimedia Syst. Conf., Jun. 2018,
ing,’’inProc.IEEEInt.Conf.Commun.,May2022,pp.739–744. pp.438–443.
[111] Y.Ran,T.Zhang,W.Huang,S.Xia,andJ.Luo,‘‘ISAW:Intelligentsuper- [133] J.J.Quinlan,A.H.Zahran,andC.J.Sreenan,‘‘DatasetsforAVC(H.264)
resolution-assisted adaptive WebRTC video streaming,’’ in Proc. 29th andHEVC(H.265)evaluationofdynamicadaptivestreamingoverHTTP
Annu.Int.Conf.MobileComput.Netw.,Sep.2023,pp.1–3. (DASH),’’inProc.7thInt.Conf.MultimediaSyst.,May2016,pp.1–6.
[112] L.Wang,S.Singh,J.Chakareski,M.Hajiesmaili,andR.K.Sitaraman, [134] H.Wang,I.Katsavounidis,J.Zhou,J.Park,S.Lei,X.Zhou,M.-O.Pun,
‘‘BONES:Near-optimalneural-enhancedvideostreaming,’’Proc.ACM X. Jin, R. Wang, X. Wang, Y. Zhang, J. Huang, S. Kwong, and
Meas.Anal.Comput.Syst.,vol.8,no.2,pp.1–28,May2024. C.-C.-J.Kuo,‘‘VideoSet:Alarge-scalecompressedvideoqualitydataset
[113] Y.Reznik,N.Barman,andP.Wagstrom,‘‘Improvingtheperformanceof basedonJNDmeasurement,’’J.Vis.Commun.ImageRepresent.,vol.46,
Web-streamingbysuper-resolutionupscaling,’’inProc.2ndMile-High pp.292–302,Jul.2017.
VideoConf.,May2023,pp.8–13. [135] Netflix Public Dataset. Accessed: Apr. 23, 2025. [Online]. Available:
[114] E. Çetinkaya, M. Nguyen, and C. Timmerer, ‘‘MoViDNN: A mobile https://github.com/Netflix/vmaf#netflix-public-dataset
platform for evaluating video quality enhancement with deep neural [136] C.G.Bampis,Z.Li,I.Katsavounidis,T.-Y.Huang,C.Ekanadham,and
networks,’’inProc.Int.Conf.MultiMediaModeling,2022,pp.465–472. A.C.Bovik,‘‘Towardsperceptuallyoptimizedend-to-endadaptivevideo
[115] A. Narayanan, S. Verma, E. Ramadan, P. Babaie, and Z.-L. Zhang, streaming,’’2018,arXiv:1808.03898.
‘‘DeepCache:Adeeplearningbasedframeworkforcontentcaching,’’in [137] V. Hosu, F. Hahn, M. Jenadeleh, H. Lin, H. Men, T. Szirányi, S. Li,
Proc.WorkshopNetw.MeetsAIML-NetAI,2018,pp.48–53. and D. Saupe, ‘‘The Konstanz natural video database (KoNViD-1k),’’
[116] S.-R.Yang,Y.-J.Tseng,C.-C.Huang,andW.-C.Lin,‘‘Multi-accessedge inProc.9thInt.Conf.QualityMultimediaExp.(QoMEX),May2017,
computingenhancedvideostreaming:Proof-of-conceptimplementation pp.1–6.
andPrediction/QoEmodels,’’IEEETrans.Veh.Technol.,vol.68,no.2, [138] R.R.RamachandraRao,S.Göring,W.Robitza,B.Feiten,andA.Raake,
pp.1888–1902,Feb.2019. ‘‘AVT-VQDB-UHD-1:AlargescalevideoqualitydatabaseforUHD-1,’’
[117] W.Li,J.Wang,G.Zhang,L.Li,Z.Dang,andS.Li,‘‘Areinforcement inProc.IEEEInt.Symp.Multimedia(ISM),Dec.2019,pp.17–177.
learningbasedsmartcachestrategyforcache-aidedultra-densenetwork,’’ [139] Y.Wang,S.Inguva,andB.Adsumilli,‘‘YouTubeUGCdatasetforvideo
IEEEAccess,vol.7,pp.39390–39401,2019. compressionresearch,’’inProc.IEEE21stInt.WorkshopMultimedia
[118] Y.Mao,S.Zhou,H.Liu,Z.Wang,andW.Zhu,‘‘Dynamicedgecaching SignalProcess.(MMSP),Sep.2019,pp.1–5.
viaonlinemeta-RL,’’inProc.Int.JointConf.NeuralNetw.(IJCNN), [140] T. Xue, B. Chen, J. Wu, D. Wei, and W. T. Freeman, ‘‘Video
Jun.2023,pp.01–10. enhancement with task-oriented flow,’’ Int. J. Comput. Vis., vol. 127,
[119] F.Wang,F.Wang,J.Liu,R.Shea,andL.Sun,‘‘Intelligentvideocaching no.8,pp.1106–1125,Feb.2019.
atnetworkedge:Amulti-agentdeepreinforcementlearningapproach,’’ [141] S.Nah,S.Baik,S.Hong,G.Moon,S.Son,R.Timofte,andK.M.Lee,
inProc.IEEEINFOCOM,Jul.2020,pp.2499–2508. ‘‘NTIRE 2019 challenge on video deblurring and super-resolution:
[120] Y.Zeng,J.Xie,H.Jiang,G.Huang,S.Yi,N.Xiong,andJ.Li,‘‘Smart Dataset and study,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
cachingbasedonuserbehaviorformobileedgecomputing,’’Inf.Sci., Recognit.Workshops(CVPRW),Jun.2019,pp.1996–2005.
vol.503,pp.444–468,Jun.2019. [142] Z.Akhtar,Y.S.Nam,R.Govindan,S.Rao,J.Chen,E.Katz-Bassett,
[121] A. Lekharu, A. Samanta, A. Sur, and M. Patra, ‘‘Content-aware B. Ribeiro, J. Zhan, and H. Zhang, ‘‘Oboe: Auto-tuning video ABR
caching at the mobile edge network using federated learning,’’ IEEE algorithmstonetworkconditions,’’inProc.Conf.ACMSpecialInterest
Trans.Emerg.TopicsComput.Intell.,vol.7,no.4,pp.1–11,Jan.2024. GroupDataCommun.,2018,pp.44–58.
[122] L.Ma,H.Zhang,T.Li,andD.Yuan,‘‘Deeplearningandsocialrela- [143] J.vanderHooft,S.Petrangeli,T.Wauters,R.Huysegems,P.R.Alface,
tionshipbasedcooperativecachingstrategyforD2Dcommunications,’’ T. Bostoen, and F. De Turck, ‘‘HTTP/2-based adaptive streaming of
in Proc. 11th Int. Conf. Wireless Commun. Signal Process. (WCSP), HEVC video over 4G/LTE networks,’’ IEEE Commun. Lett., vol. 20,
Oct.2019,pp.1–6. no.11,pp.2177–2180,Nov.2016.
VOLUME13,2025 111159

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
[144] D. Raca, J. J. Quinlan, A. H. Zahran, and C. J. Sreenan, ‘‘Beyond [164] Z.Tu,Y.Wang,N.Birkbeck,B.Adsumilli,andA.C.Bovik,‘‘UGC-
throughput: A 4G lte dataset with channel and context metrics,’’ in VQA:Benchmarkingblindvideoqualityassessmentforusergenerated
Proc.9thACMMultimediaSyst.Conf.,Jun.2018,pp.460–465. content,’’IEEETrans.ImageProcess.,vol.30,pp.4449–4464,2021.
[145] R.Shalala,R.Dubin,O.Hadar,andA.Dvir,‘‘VideoQoEprediction [165] Z.Tu,X.Yu,Y.Wang,N.Birkbeck,B.Adsumilli,andA.C.Bovik,
based on user profile,’’ in Proc. Int. Conf. Comput., Netw. Com- ‘‘RAPIQUE:Rapidandaccuratevideoqualitypredictionofusergener-
mun.(ICNC),Mar.2018,pp.588–592. atedcontent,’’IEEEOpenJ.SignalProcess.,vol.2,pp.425–440,2021.
[146] D. Minovski, C. Öhlund, K. Mitra, and P. Johansson, ‘‘Analysis and [166] Y.Feng,Y.Wang,H.Liu,L.Cong,andY.Liu,‘‘Adaptivevideostreaming
estimation of video QoE in wireless cellular networks using machine basedonlearningintrinsicreward,’’inProc.IEEEInt.Symp.Broadband
learning,’’inProc.11thInt.Conf.QualityMultimediaExp.(QoMEX), MultimediaSyst.Broadcast.(BMSB),Jun.2022,pp.1–5.
Jun.2019,pp.1–6. [167] J.Luo,F.R.Yu,Q.Chen,andL.Tang,‘‘Adaptivevideostreamingwith
[147] Y.BenYoussef,M.Afif,R.Ksantini,andS.Tabbane,‘‘AnovelQoE edgecachingandvideotranscodingoversoftware-definedmobilenet-
model based on boosting support vector regression,’’ in Proc. IEEE works:Adeepreinforcementlearningapproach,’’IEEETrans.Wireless
WirelessCommun.Netw.Conf.(WCNC),Apr.2018,pp.1–6. Commun.,vol.19,no.3,pp.1577–1592,Mar.2020.
[148] N.Eswara,S.Ashique,A.Panchbhai,S.Chakraborty,H.P.Sethuram, [168] J.GuoandG.Zhang,‘‘Avideo-qualitydrivenstrategyinshortvideo
K. Kuchi, A. Kumar, and S. S. Channappayya, ‘‘Streaming video streaming,’’inProc.4thInt.ACMConf.Model.,Nov.2021,pp.221–228.
QoE modeling and prediction: A long short-term memory approach,’’ [169] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, ‘‘A control-theoretic
IEEETrans.CircuitsSyst.VideoTechnol.,vol.30,no.3,pp.661–673, approach for dynamic adaptive video streaming over HTTP,’’ ACM
Mar.2020. SIGCOMM Comput. Commun. Rev., vol. 45, no. 4, pp.325–338,
[149] T. N. Duc, C. M. Tran, P. X. Tan, and E. Kamioka, ‘‘Bidirectional Sep.2015.
LSTMforcontinuouslypredictingQoEinHTTPadaptivestreaming,’’ [170] Dash Industry Forum. Dash.Js. Accessed: Apr. 17, 2025. [Online].
inProc.2ndInt.Conf.Inf.Sci.Syst.,Mar.2019,pp.156–160. Available:https://github.com/Dash-Industry-Forum/dash.js
[150] L.Liu,H.Hu,Y.Luo,andY.Wen,‘‘Whenwirelessvideostreamingmeets [171] R.Netravali,A.Sivaraman,S.Das,A.Goyal,K.Winstein,J.Mickens,
AI:Adeeplearningapproach,’’IEEEWirelessCommun.,vol.27,no.2, and H. Balakrishnan, ‘‘Mahimahi: Accurate record-and-replay for
pp.127–133,Apr.2020. HTTP,’’inProc.USENIXAnnu.Tech.Conf.,Jul.2015,pp.417–429.
[151] H.Dinaki,S.Shirmohammadi,E.Janulewicz,andD.Côté,‘‘Forecasting [172] P.K.Mu,J.Zheng,T.H.Luan,L.Zhu,M.Dong,andZ.Su,‘‘AMIS:
videoQoEwithdeeplearningfrommultivariatetime-series,’’IEEEOpen Edgecomputingbasedadaptivemobilevideostreaming,’’inProc.IEEE
J.SignalProcess.,vol.2,pp.512–521,2021. INFOCOM,May2021,pp.1–10.
[152] P. Casas, M. Seufert, S. Wassermann, B. Gardlo, N. Wehner, and [173] A.Lekharu,K.Y.Moulii,A.Sur,andA.Sarkar,‘‘Deeplearningbased
R.Schatz,‘‘DeepCrypt–deeplearningforQoEmonitoringandfinger- predictionmodelforadaptivevideostreaming,’’inProc.Int.Conf.Com-
printingofuseractionsinadaptivevideostreaming,’’inProc.IEEE8th mun.Syst.Netw.(COMSNETS),Jan.2020,pp.152–159.
Int.Conf.Netw.Softwarization(NetSoft),Jun.2022,pp.259–263. [174] S.Feng,C.Wang,andX.Jiang,‘‘Adaptivestreamingalgorithmbasedon
[153] M.H.MazharandZ.Shafiq,‘‘Real-timevideoqualityofexperiencemon- reinforcementlearning,’’IOPConf.Ser.,Mater.Sci.Eng.,vol.768,no.7,
itoringforHTTPSandQUIC,’’inProc.IEEEConf.Comput.Commun., Mar.2020,Art.no.072069.
Apr.2018,pp.1331–1339. [175] J.LinandS.Wang,‘‘Improvingrobustnessoflearning-basedadaptive
[154] S.Cheng,H.Hu,X.Zhang,andZ.Guo,‘‘Rebufferingbutnotsuffering: video streaming in wildly fluctuating networks,’’ in Proc. IEEE
Exploringcontinuous-timequantitativeQoEbyuser’sexitingbehaviors,’’ Int.Conf.MultimediaExpo(ICME),Jul.2023,pp.1787–1792.
inProc.IEEEINFOCOM,Apr.2023,pp.1–10. [176] G.F.Yang,W.-T.Lee,andH.-W.Wei,‘‘DeepQ-learningbasedalgorithm
[155] W. Li, J. Huang, S. Wang, C. Wu, S. Liu, and J. Wang, ‘‘An fordynamicadaptivestreamingoverHTTP,’’inProc.Int.Conf.Internet
apprenticeshiplearningapproachforadaptivevideostreamingbasedon Stud.,Feb.2019,pp.1–8.
chunkqualityanduserpreference,’’IEEETrans.Multimedia,vol.25, [177] X. Zuo, J. Yang, M. Wang, and Y. Cui, ‘‘Adaptive bitrate with user-
pp.2488–2502,2023. levelQoEpreferenceforvideostreaming,’’inProc.IEEEINFOCOM,
[156] L.Du,L.Zhuo,J.Li,J.Zhang,X.Li,andH.Zhang,‘‘Videoqualityof May2022,pp.1279–1288.
experiencemetricfordynamicadaptivestreamingservicesusingDASH [178] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella, ‘‘D-DASH:
standardanddeepspatial–temporalrepresentationofvideo,’’Appl.Sci., A deep Q-learning framework for DASH video streaming,’’ IEEE
vol.10,no.5,p.1793,Mar.2020. Trans.Cognit.Commun.Netw.,vol.3,no.4,pp.703–718,Dec.2017.
[157] R.U.Mustafa,S.Ferlin,C.E.Rothenberg,D.Raca,andJ.J.Quinlan, [179] N.A.Hafez,M.S.Hassan,andT.Landolsi,‘‘Reinforcementlearning-
‘‘AsupervisedmachinelearningapproachforDASHvideoQoEpredic- basedrateadaptationindynamicvideostreaming,’’TelecommunSyst,
tionin5Gnetworks,’’inProc.16thACMSymp.QoSSecur.Wireless vol.83,no.4,pp.395–407,Jun.2023.
MobileNetw.,Nov.2020,pp.57–64. [180] J. Liu, J. Li, X. Yang, and M. Sun, ‘‘TPMI: Accurate throughput
[158] J. Yu, H. Wen, G. Pan, S. Zhang, X. Chen, and S. Xu, ‘‘Quality of prediction for better bitrate selection in adaptive video streaming,’’
experienceorientedadaptivevideostreamingforedgeassistedcellular in Proc. 2nd Int. Conf. Sens., Meas., Commun. Internet Things
networks,’’IEEEWirelessCommun.Lett.,vol.11,no.11,pp.2305–2309, Technol.(SMC-IoT),May2023,pp.140–145.
Nov.2022. [181] T. Huu, S. Van Pham, T. N. T. Huong, and H.-C. Le, ‘‘QoE aware
[159] V.V.Menon,R.Farahani,P.T.Rajendran,M.Ghanbari,H.Hellwagner, videostreamingschemeutilizingGRU-basedbandwidthpredictionand
and C. Timmerer, ‘‘Transcoding quality prediction for adaptive video adaptive bitrate selection for heterogeneous mobile networks,’’ IEEE
streaming,’’inProc.2ndMile-HighVideoConf.,May2023,pp.103–109. Access,vol.12,pp.45785–45795,2024.
[160] V. V. Menon, P. T. Rajendran, R. Farahani, K.Schoeffmann, and [182] D. Raca, A. H. Zahran, C. J. Sreenan, R. K. Sinha, E. Halepovic,
C.Timmerer,‘‘Videoqualityassessmentwithtextureinformationfusion and V. Gopalakrishnan, ‘‘Device-based cellular throughput prediction
for streaming applications,’’ in Proc. 3rd Mile-High Video Conf., for video streaming: Lessons from a real-world evaluation,’’ IEEE
Feb.2024,pp.1–6. Trans.Mach.Learn.Commun.Netw.,vol.2,pp.318–334,2024.
[161] R.R.R.Rao,S.Göring,P.List,W.Robitza,B.Feiten,U.Wüstenhagen, [183] A. Biernacki, ‘‘Improving streaming video with deep learning-based
andA.Raake,‘‘Bitstream-basedmodelstandardfor4K/UHD:ITU-T network throughput prediction,’’ Appl. Sci., vol. 12, no. 20, p.10274,
P.1204.3—Model details, evaluation, analysis and open source imple- Oct.2022.
mentation,’’inProc.12thInt.Conf.QualityMultimediaExp.(QoMEX), [184] Y.S.Nam,J.Gao,C.Bothra,E.Ghabashneh,S.Rao,B.Ribeiro,J.Zhan,
May2020,pp.1–6. andH.Zhang,‘‘Xatu:Richerneuralnetworkbasedpredictionforvideo
[162] D.Li,T.Jiang,andM.Jiang,‘‘Qualityassessmentofin-the-wildvideos,’’ streaming,’’Proc.ACMMeas.Anal.Comput.Syst.,vol.5,no.3,pp.1–26,
inProc.27thACMInt.Conf.Multimedia,Oct.2019,pp.2351–2359. Dec.2021.
[163] Y. Wang, J. Ke, H. Talebi, J. G. Yim, N. Birkbeck, B. Adsumilli, [185] A. Mondal, B. Palit, S. Khandelia, N. Pal, J. Jayatheerthan, K. Paul,
P.Milanfar,andF.Yang,‘‘Richfeaturesforperceptualqualityassessment N.Ganguly,andS.Chakraborty,‘‘EnDASH—Amobilityadaptedenergy
of UGC videos,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern efficient ABR video streaming for cellular networks,’’ in Proc. IFIP
Recognit.(CVPR),Jun.2021,pp.13430–13439. Netw.Conf.(Networking),Jun.2020,pp.127–135.
111160 VOLUME13,2025

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
[186] T. Song, P. Garza, M. Meo, and M. M. Munafò, ‘‘DeX: Deep [208] M. Kim and K. Chung, ‘‘Http adaptive streaming scheme based on
learning-basedthroughputpredictionforreal-timecommunicationswith reinforcementlearningwithedgecomputingassistance,’’J.Netw.Com-
emphasis on traffic eXtremes,’’ Comput. Netw., vol. 249, May 2024, put.Appl.,vol.213,Jan.2022,Art.no.103604.
Art.no.110507. [209] G.Xiong,X.Qin,B.Li,R.Singh,andJ.Li,‘‘Index-awarereinforcement
[187] B. Hou, S. Yang, F. A. Kuipers, L. Jiao, and X. Fu, ‘‘EAVS: Edge- learningforadaptivevideostreamingatthewirelessedge,’’inProc.23rd
assistedadaptivevideostreamingwithfine-grainedserverlesspipelines,’’
Int.Symp.Theory,Sep.2022,pp.81–90.
inProc.IEEEConf.Comput.Commun.,May2023,pp.1–10.
|     |     |     |     |     |     |     |     | [210] X.Ma,Q.Li,Y.Jiang,G.-M.Muntean,andL.Zou,‘‘Learning-based |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[188] M. Darwich, K. Khalil, Y. Ismail, and M. Bayoumi, ‘‘Adaptive joint QoE optimization for adaptive video streaming based on smart
video streaming: An AI-driven approach leveraging cloud and edge edge,’’IEEETrans.Netw.ServiceManage.,vol.19,no.2,pp.1789–1806,
| computing,’’inProc.IEEEInt.Conf.Artif.Intell.,Blockchain,Internet |     |     |     |     |     |     |     | Jun.2022. |     |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Things(AIBThings),Sep.2023,pp.1–5. [211] M.Lim,M.N.Akcay,A.Bentaleb,A.C.Begen,andR.Zimmermann,
| [189] Y. Sun, | W. Chen, | G.  | Pan, S. | Zhang, | X. Chen, | and Y. | Wu, ‘‘Joint |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ------- | ------ | -------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
‘‘Whentheygohigh,wegolow:Low-latencylivestreamingindash.js
| bitrate      | transcoding | and       | parallel | cooperative   | transmission | optimization |     |             |                 |      |                |     |       |            |       |
| ------------ | ----------- | --------- | -------- | ------------- | ------------ | ------------ | --- | ----------- | --------------- | ---- | -------------- | --- | ----- | ---------- | ----- |
|              |             |           |          |               |              |              |     | with        | LoL,’’ in Proc. | 11th | ACM Multimedia |     | Syst. | Conf., May | 2020, |
| for adaptive | video       | streaming | in       | edge assisted | cellular     | networks,’’  | in  | pp.321–326. |                 |      |                |     |       |            |       |
Proc.IEEE98thVeh.Technol.Conf.(VTC-Fall),Oct.2023,pp.1–7. [212] M. Hao, J. Yuan, B. Lu, L. Song, R. Xie, and W. Zhang, ‘‘Buffer
[190] J. Bégaint, F. Racapé, S. Feltman, and A. Pushparaja, ‘‘CompressAI: displacement based online learning algorithm for low latency HTTP
APyTorchlibraryandevaluationplatformforend-to-endcompression adaptivestreaming,’’inProc.IEEEInt.Symp.BroadbandMultimedia
research,’’2020,arXiv:2011.03029.
Syst.Broadcast.(BMSB),Aug.2021,pp.1–6.
| [191] J. Kang | and K. | Chung, | ‘‘Online | reinforcement | learning | based | HTTP |                                                                 |     |     |     |     |     |     |     |
| ------------- | ------ | ------ | -------- | ------------- | -------- | ----- | ---- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |        |        |          |               |          |       |      | [213] M.T.Vega,D.C.Mocanu,J.Famaey,S.Stavrou,andA.Liotta,‘‘Deep |     |     |     |     |     |     |     |
adaptivestreamingscheme,’’inProc.13thInt.Conf.Inf.Commun.Tech- learningforqualityassessmentinlivevideostreaming,’’IEEESignal
nol.Converg.(ICTC),Oct.2022,pp.498–503. Process.Lett.,vol.24,no.6,pp.736–740,Jun.2017.
[192] W.Choi,J.Chen,andJ.Yoon,‘‘ABRaider:Multiphasereinforcement [214] L.Cui,D.Su,S.Yang,Z.Wang,andZ.Ming,‘‘TCLiVi:Transmission
| learning | for | environment-adaptive |     | video | streaming,’’ | IEEE | Access, |     |     |     |     |     |     |     |     |
| -------- | --- | -------------------- | --- | ----- | ------------ | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
controlinlivevideostreamingbasedondeepreinforcementlearning,’’
vol.10,pp.53108–53123,2022.
IEEETrans.Multimedia,vol.23,pp.651–663,2021.
[193] J.KangandK.Chung,‘‘HTTPadaptivestreamingframeworkwithonline
|     |     |     |     |     |     |     |     | [215] B. Wei, | H. Song, | Q. N. | Nguyen, | and J. Katto, | ‘‘DASH | live | video |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ----- | ------- | ------------- | ------ | ---- | ----- |
reinforcementlearning,’’Appl.Sci.,vol.12,no.15,p.7423,Jul.2022.
|     |     |     |     |     |     |     |     | streaming | control | using actor-critic |     | reinforcement |     | learning method,’’ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------------ | --- | ------------- | --- | ------------------ | --- |
[194] C. Zhang, J. Yin, Y. Xu, H. Chen, X. Xu, and S. Liu, ‘‘OLNC: MobileNetw.Manage.,vol.418,pp.17–24,Jan.2022.
Onlinelearningofnetworkconditionsforadaptivevideostreaming,’’in [216] Z. Tian, L. Zhao, L. Nie, P. Chen, and S. Chen, ‘‘Deeplive: QoE
Proc.IEEEInt.Symp.BroadbandMultimediaSyst.Broadcast.(BMSB),
|     |     |     |     |     |     |     |     | optimization | for | live video | streaming | through | deep | reinforcement |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --------- | ------- | ---- | ------------- | --- |
Jun.2023,pp.1–6.
learning,’’inProc.IEEE25thInt.Conf.ParallelDistrib.Syst.(ICPADS),
[195] Z.Xia,Y.Zhou,F.Y.Yan,andJ.Jiang,‘‘Genet:Automaticcurriculum
Dec.2019,pp.827–831.
| generation | for | learning | adaptation | in  | networking,’’ | in Proc. | ACM |                                                                    |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ---------- | --- | ------------- | -------- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|            |     |          |            |     |               |          |     | [217] X.Zhang,Y.Hu,andZ.Li,‘‘Livevideostreamingoptimizationbasedon |     |     |     |     |     |     |     |
SIGCOMM2022Conf.,2022,p.397.
deepreinforcementlearning,’’inProc.12thInt.Conf.Mach.Learn.Com-
[196] H. Yuan, X. Hu, J. Hou, X. Wei, and S. Kwong, ‘‘An ensemble rate put.,Feb.2020,pp.116–120.
adaptationframeworkfordynamicadaptivestreamingoverHTTP,’’IEEE
|     |     |     |     |     |     |     |     | [218] I. M. | Ozcelik and | C. Ersoy, | ‘‘ALVS: | Adaptive | live | video streaming |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --------- | ------- | -------- | ---- | --------------- | --- |
Trans.Broadcast.,vol.66,no.2,pp.251–263,Jun.2020.
usingdeepreinforcementlearning,’’J.Netw.Comput.Appl.,vol.205,
[197] W.Li,X.Li,Y.Xu,Y.Yang,andS.Lu,‘‘MetaABR:Ameta-learning
Jun.2022,Art.no.103451.
| approach | on  | adaptative | bitrate | selection | for video | streaming,’’ | IEEE |               |        |                    |     |            |           |      |        |
| -------- | --- | ---------- | ------- | --------- | --------- | ------------ | ---- | ------------- | ------ | ------------------ | --- | ---------- | --------- | ---- | ------ |
|          |     |            |         |           |           |              |      | [219] J. Zhao | and J. | Pan, ‘‘Low-latency |     | live video | streaming | over | a low- |
Trans.MobileComput.,vol.24,no.6,pp.1–17,Jun.2023.
Earth-orbitsatellitenetworkwithDASH,’’Proc.15thACMMultimedia
[198] L.Huo,Z.Wang,M.Xu,Y.Li,Z.Ding,andH.Wang,‘‘Ameta-learning
frameworkforlearningmulti-userpreferencesinQoEoptimizationof Syst.Conf.,vol.15,p.109,Apr.2024.
DASH,’’ IEEE Trans. Circuits Syst. Video Technol., vol. 30, no. 9, [220] H. V. Hasselt, A. Guez, and D. Silver, ‘‘Deep reinforcement learning
withdoubleQ-learning,’’inProc.30thAAAIConf.Artif.Intell.,vol.30,
pp.3210–3225,Sep.2020.
Feb.2016,pp.2094–2100.
| [199] T. Huang, | C.  | Zhou, R.-X. | Zhang, | C.  | Wu, and | L. Sun, | ‘‘Learning |                 |        |          |         |         |        |          |         |
| --------------- | --- | ----------- | ------ | --- | ------- | ------- | ---------- | --------------- | ------ | -------- | ------- | ------- | ------ | -------- | ------- |
|                 |     |             |        |     |         |         |            | [221] H. Zhang, | C. An, | A. Zhou, | Y. Zhu, | W. Sun, | Y. Lu, | J. Chen, | L. Liu, |
tailoredadaptivebitratealgorithmstoheterogeneousnetworkconditions:
H.Ma,andA.Fei,‘‘Venus:EnhancingQoEofcrowdsourcedlivevideo
| A domain-specific |     | priors | and meta-reinforcement |     |     | learning | approach,’’ |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ---------------------- | --- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEEJ.Sel.AreasCommun.,vol.40,no.8,pp.2485–2503,Aug.2022. streaming by exploiting multiflow viewer assistance,’’ in Proc. 30th
[200] Y. Xu, X. Li, Y. Yang, Z. Lin, L. Wang, and W. Li, ‘‘FedABR: A Annu.Int.Conf.MobileComput.Netw.,May2024,pp.170–184.
personalized federated reinforcement learning approach for adaptive [222] W. J. Yun, D. Kwon, M. Choi, J. Kim, G. Caire, and A. F. Molisch,
|       |              |     |            |       |       |                    |     | ‘‘Quality-aware |     | deep reinforcement |     | learning | for | streaming | in  |
| ----- | ------------ | --- | ---------- | ----- | ----- | ------------------ | --- | --------------- | --- | ------------------ | --- | -------- | --- | --------- | --- |
| video | streaming,’’ | in  | Proc. IFIP | Netw. | Conf. | (IFIP Networking), |     |                 |     |                    |     |          |     |           |     |
infrastructure-assistedconnectedvehicles,’’IEEETrans.Veh.Technol.,
Jun.2023,pp.1–9.
vol.71,no.2,pp.2002–2017,Feb.2022.
[201] H.Yuan,H.Lu,L.Meng,andM.Liu,‘‘MUABR:Multi-useradaptive
bitrate algorithm based multi-agent deep reinforcement learning,’’ in [223] Y.Jin,D.Meng,andW.Jiang,‘‘AvisualsensitivityawareABRalgorithm
Proc.IEEEInt.Conf.Commun.,May2022,pp.751–756. for DASH via deep reinforcement learning,’’ACM Trans. Multimedia
[202] S.AltamimiandS.Shirmohammadi,‘‘QoE-fairDASHvideostreaming Comput.Commun.Appl.,vol.20,no.3,pp.1–22,Jun.2023.
using server-side reinforcement learning,’’ ACM Trans. Multimedia [224] S.Sengupta,N.Ganguly,S.Chakraborty,andP.De,‘‘HotDASH:Hotspot
|     |     |     |     |     |     |     |     | aware | adaptive | video streaming | using | deep | reinforcement | learning,’’ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --------------- | ----- | ---- | ------------- | ----------- | --- |
Comput.,Commun.,Appl.,vol.16,no.2s,pp.1–21,Apr.2020.
|     |     |     |     |     |     |     |     | in Proc. | IEEE | 26th Int. Conf. | Netw. | Protocols | (ICNP), | Sep. | 2018, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------------- | ----- | --------- | ------- | ---- | ----- |
[203] Y.Liu,D.Wei,C.Zhang,andW.Li,‘‘Distributedbandwidthallocation
| strategyforQoEfairnessofmultiplevideostreamsinbottlenecklinks,’’ |     |     |     |     |     |     |     | pp.165–175. |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
FutureInternet,vol.14,no.5,p.152,May2022. [225] L. Lu, J. Xiao, W. Ni, H. Du, and D. Zhang, ‘‘Deep-reinforcement-
[204] Y. Yuan, W. Wang, Y. Wang, S. S. Adhatarao, B. Ren, K. Zheng, learning-baseduser-preference-awarerateadaptationforvideostream-
and X. Fu, ‘‘Joint optimization of QoE and fairness for adaptive ing,’’ in Proc. IEEE 23rd Int. Symp. World Wireless, Jun. 2022,
pp.416–424.
| video | streaming | in heterogeneous |     | mobile | environments,’’ |     | IEEE/ACM |     |     |     |     |     |     |     |     |
| ----- | --------- | ---------------- | --- | ------ | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Trans.Netw.,vol.32,no.1,pp.50–64,Jan.2024. [226] W. Choi and J. Yoon, ‘‘CTC: Content-aware tailoring of adaptive
[205] X. Wei, M. Zhou, S. Kwong, H. Yuan, S. Wang, G. Zhu, and video streaming using multi-head critic network,’’ in Proc. 14th
J.Cao,‘‘Reinforcementlearning-basedQoE-orienteddynamicadaptive Int.Conf.UbiquitousFutureNetw.(ICUFN),Jul.2023,pp.709–712.
streamingframework,’’Inf.Sci.,vol.569,pp.786–803,May2021. [227] Y.Sani,D.Raca,J.J.Quinlan,andC.J.Sreenan,‘‘SMASH:Asupervised
[206] P.K.Mu,J.Zheng,T.H.Luan,L.Zhu,Z.Su,andM.Dong,‘‘AMIS- machinelearningapproachtoadaptivevideostreamingoverHTTP,’’in
MU:Edgecomputingbasedadaptivevideostreamingformultiplemobile Proc. 12th Int. Conf. Quality Multimedia Exp. (QoMEX), May 2020,
| users,’’IEEETrans.MobileComput.,vol.23,no.1,pp.1–18,Jan.2024. |     |     |     |     |     |     |     | pp.1–6. |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
[207] J.KangandK.Chung,‘‘Adaptivestreamingschemewithreinforcement [228] G. Gao, L. Dong, H. Zhang, Y. Wen, and W. Zeng, ‘‘Content-aware
learninginedgecomputingenvironments,’’Int.Conf.Inf.Netw.(ICOIN), personalised rate adaptation for adaptive streaming via deep video
vol.2023,pp.128–133,Jan.2023. analysis,’’inProc.IEEEInt.Conf.Commun.(ICC),May2019,pp.1–8.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 111161 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

H.Ameretal.:ReviewofLearning-BasedMethodsforAdaptiveVideoStreamingOverHTTP
[229] S. Hu, M. Xu, H. Zhang, C. Xiao, and C. Gui, ‘‘Affective content- MOHAMED S. HASSAN (Member, IEEE)
awareadaptationschemeonQoEoptimizationofadaptivestreamingover receivedtheM.Sc.degreeinelectricalengineering
HTTP,’’ACMTrans.MultimediaComput.Commun.Appl.,vol.15,no.3s, fromtheUniversityofPennsylvania,Philadelphia,
| pp.1–18,Nov.2019. |     |     |     |     |     |     |     |     | PA, | USA, in | 2000, and | the | Ph.D. degree |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------------ |
[230] Z.Li,A.C.Begen,J.Gahm,Y.Shan,B.Osler,andD.Oran,‘‘Streaming in electrical and computer engineering from
videooverHTTPwithconsistentquality,’’inProc.5thACMMultimedia
|     |     |     |     |     |     |     |     |     | The | University of | Arizona, | Tucson, | AZ, USA, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ------- | -------- |
Syst.Conf.,Mar.2014,pp.248–258.
in2005.HeiscurrentlyaProfessorofelectrical
[231] Y.Qin,S.Hao,K.R.Pattipati,F.Qian,S.Sen,B.Wang,andC.Yue,
engineeringwithAmericanUniversityofSharjah,
‘‘ABRstreamingofVBR-encodedvideos:Characterization,challenges,
Sharjah,UnitedArabEmirates.Inadditiontohis
| and | solutions,’’ | in Proc. | 14th | Int. Conf. | Emerg. | Netw. | EXperiments |     |     |     |     |     |     |
| --- | ------------ | -------- | ---- | ---------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- | --- |
Technol.,2018,pp.366–378. work on electric vehicles, he has been actively
|                |     |        |              |       |        |        |              | involved in | several projects | across fields, | such | as free-space | optical |
| -------------- | --- | ------ | ------------ | ----- | ------ | ------ | ------------ | ----------- | ---------------- | -------------- | ---- | ------------- | ------- |
| [232] G. Zhou, | R.  | Wu, M. | Hu, Y. Zhou, | T. Z. | J. Fu, | and D. | Wu, ‘‘Vibra: |             |                  |                |      |               |         |
communications,demandresponse,andsmartgrids.Hisprimaryresearch
NeuraladaptivestreamingofVBR-encodedvideos,’’inProc.31stACM
|          |       |           |       |         |        |       |              | interests include | multimedia | communications | and | networking, | wireless |
| -------- | ----- | --------- | ----- | ------- | ------ | ----- | ------------ | ----------------- | ---------- | -------------- | --- | ----------- | -------- |
| Workshop | Netw. | Operating | Syst. | Support | Digit. | Audio | Video, 2021, |                   |            |                |     |             |          |
communications,cognitiveradios,resourceallocation,andtheperformance
pp.1–8.
evaluationofbothwiredandwirelessnetworks,withaparticularfocuson
| [233] H. Amer, | M.  | S. Hassan, | and | M. H. Ismail, | ‘‘A | content-aware | deep |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | ------------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
Q-learning approach for adaptive video streaming,’’ in Proc. 6th next-generationwirelesssystems.
Int.Conf.Commun.,SignalProcess.,Appl.(ICCSPA),Jul.2024,pp.1–6.
| [234] K. Tang, | N.  | Kan, J. | Zou, C. | Li, X. Fu, | M.  | Hong, and | H. Xiong, |     |     |     |     |     |     |
| -------------- | --- | ------- | ------- | ---------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- |
‘‘Multi-useradaptivevideodeliveryoverwirelessnetworks:Aphysical
| layer  | resource-aware |       | deep reinforcement |     | learning | approach,’’ | IEEE        |     |     |     |     |     |     |
| ------ | -------------- | ----- | ------------------ | --- | -------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- |
| Trans. | Circuits       | Syst. | Video Technol.,    |     | vol. 31, | no. 2,      | pp.798–815, |     |     |     |     |     |     |
Mar.2020.
| [235] X. Hu, | A. Ghosh, | X.  | Liu, Z.-L. | Zhang, | and | N. Shroff, | ‘‘COREL: |     |     |     |     |     |     |
| ------------ | --------- | --- | ---------- | ------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
ConstrainedreinforcementlearningforvideostreamingABRalgorithm
designovermmWave5G,’’inProc.IEEEInt.WorkshopTech.Committee
Commun.QualityRel.(CQR),Oct.2023,pp.1–6.
[236] S.Wang,J.Lin,andY.Dai,‘‘MMVS:Enablingrobustadaptivevideo
| streaming | for | wildly fluctuating |     | and heterogeneous |     | networks,’’ | IEEE |     |     |     |     |     |     |
| --------- | --- | ------------------ | --- | ----------------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
Trans.Multimedia,vol.26,pp.11018–11030,2024.
| [237] S.-T. | Lei, Y.-A. | Chen, | R.-C. | Chen, C.-C. | Lo, | and C.-Y. | Li, ‘‘IPA- |     |     |     |     |     |     |
| ----------- | ---------- | ----- | ----- | ----------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
DASH:IntelligentproactiveadaptationforDASHvideostreamingat5G
networkedge,’’inProc.IEEE35thInt.Symp.Pers.,IndoorMobileRadio
Commun.(PIMRC),Sep.2024,pp.1–7.
| [238] D. Wu, | X. Wang, | Y.  | Qiao, Z.       | Wang, J. | Jiang, | S. Cui,           | and F. Wang, |     |     |     |     |     |     |
| ------------ | -------- | --- | -------------- | -------- | ------ | ----------------- | ------------ | --- | --- | --- | --- | --- | --- |
| ‘‘NetLLM:    | Adapting |     | large language |          | models | for networking,’’ | in           |     |     |     |     |     |     |
Proc.ACMSIGCOMMConf.,Jul.2024,pp.661–678.
[239] Z.Meng,M.Wang,J.Bai,M.Xu,H.Mao,andH.Hu,‘‘Interpretingdeep
learning-basednetworkingsystems,’’inProc.Annu.Conf.ACMSpecial
InterestGroupDataCommun.Appl.,Jul.2020,p.154.
| [240] Y. Li, | Z. Zhang, | H.  | Chen, and | Z. Ma, | ‘‘Mamba: | Bringing | multi- |     |     |     |     |     |     |
| ------------ | --------- | --- | --------- | ------ | -------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
dimensionalABRtoWebRTC,’’inProc.31stACMInt.Conf.Multimedia,
| Oct.2023,pp.9262–9270. |     |     |     |     |     |     |     |     | MAHMOUDH.ISMAIL(SeniorMember,IEEE) |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
[241] J. Eo, Z. Niu, W. Cheng, F. Y. Yan, R. Gao, J. Kardhashi, S. Inglis, received the B.Sc. degree (Hons.) in electronics
M.Revow,B.-G.Chun,P.Cheng,andY.Xiong,‘‘OpenNetLab:Open and electrical communications engineering and
theM.Sc.degreeincommunicationsengineering
platformforRL-basedcongestioncontrolforreal-timecommunications,’’
inProc.6thAsia–PacificWorkshopNetw.,Jul.2022,pp.70–75. fromCairoUniversity,Egypt,in2000and2002,
[242] H.Zhang,A.Zhou,R.Ma,J.Lu,andH.Ma,‘‘Arsenal:Understanding respectively, and the Ph.D. degree in electrical
learning-basedwirelessvideotransportviain-depthevaluation,’’IEEE engineering from the University of Mississippi,
Trans.Veh.Technol.,vol.70,no.10,pp.10832–10844,Oct.2021. MS,USA,in2006.FromAugust2000toAugust
[243] S. Yuan, Q. Zhou, J. Li, S. Guo, H. Chen, C. Wu, and Y. Yang, 2002,hewasaResearchandTeachingAssistant
‘‘Adaptive incentive and resource allocation for blockchain-supported withtheDepartmentofElectronicsandElectrical
edgevideostreamingsystems:Acooperativelearningapproach,’’IEEE
CommunicationsEngineering,CairoUniversity.From2004to2006,hewas
Trans.MobileComput.,vol.24,no.2,pp.539–556,Feb.2025.
aResearchAssistantwiththeCenterforWirelessCommunications(CWC),
| [244] K. Lu, | X. Zhang, | T.  | Zhai, and | M. Zhou, | ‘‘Adaptive |     | sharding for |     |     |     |     |     |     |
| ------------ | --------- | --- | --------- | -------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
UniversityofMississippi.HeiscurrentlyaFullProfessor(onleave)with
UAVnetworks:Adeepreinforcementlearningapproachtoblockchain
theDepartmentofElectronicsandElectricalCommunicationsEngineering,
optimization,’’Sensors,vol.24,no.22,p.7279,Nov.2024.
CairoUniversity;andaFullProfessorwithAmericanUniversityofSharjah,
|     |     |     |     |     |     |     |     | Sharjah, United | Arab Emirates. | He was | also | a Systems | Engineering |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ------ | ---- | --------- | ----------- |
ConsultantwithNewportMediaInc.(currentlypartofMicrochip)Egypt
DesignCenter,Cairo,from2006to2014.Hisresearchisinthegeneralarea
|     |     | HALA | AMER | received | the | B.Sc. | degree in |     |     |     |     |     |     |
| --- | --- | ---- | ---- | -------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
ofwirelesscommunications,withanemphasisonperformanceevaluation
electricalengineeringwithAmericanUniversityof
ofnext-generationwirelesssystems.HewasarecipientoftheUniversityof
Sharjah,Sharjah,UnitedArabEmirates,in2023,
wheresheiscurrentlypursuingtheM.Sc.degree. MississippiSummerAssistantshipAward,in2004and2005;theUniversity
Her current research interests focus on the use of Mississippi Dissertation Fellowship Award, in 2006; the University
of machine learning for adaptive multimedia of Mississippi Graduate Achievement Award in Electrical Engineering,
streaming. in2006;andtheBestPaperAwardpresentedattheTenthIEEESymposium
onComputersandCommunications(ISCC2005),LaMangadelMarMenor,
Spain.
| 111162 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |