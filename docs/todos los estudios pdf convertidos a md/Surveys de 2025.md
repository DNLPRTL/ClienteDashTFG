This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
Dateofpublicationxxxx00,0000,dateofcurrentversionxxxx00,0000.
DigitalObjectIdentifier10.1109/ACCESS.2017.DOI
| A Review |     | of    | Learning-Based |           |     |     |      | Methods |      |     | for |     |     |
| -------- | --- | ----- | -------------- | --------- | --- | --- | ---- | ------- | ---- | --- | --- | --- | --- |
| Adaptive |     | Video |                | Streaming |     |     | over |         | HTTP |     |     |     |     |
HALAAMER,MOHAMEDS.HASSANANDMAHMOUDH.ISMAIL(SENIORMEMBER,IEEE)
DepartmentofElectricalEngineering,AmericanUniversityofSharjah,Sharjah,UAE(e-mails:{g00078587,mshassan,mhibrahim}@aus.edu)
Correspondingauthor:MohamedS.Hassan(e-mail:mshassan@aus.edu).
TheworkofHalaAmerandMahmoudH.IsmailissupportedbytheAmericanUniversityofSharjahthroughFacultyResearchGrants
numberFRG22-C-E13andFRG23-C-E12.
ABSTRACT Adaptive video streaming offers enhanced Quality of Experience (QoE) by dynamically
adjustingthevideoqualitytomatchchangingnetworkconditionsanddevicecapabilities,foruninterrupted
and high-quality playback. However, employing effective video streaming systems is becoming more
challenging as user demands for high quality and low latency grow increasingly high. The surge in video
traffic is not only straining network resources but also causing a decline in video quality. To address
thesechallenges,machinelearningalgorithmsleveragedata-driventechniquestooptimizevideodelivery,
improve QoE, and reduce network congestion. Given the critical role of learning algorithms in shaping
the future of adaptive video streaming, a review of these methods is needed. This paper presents a
comprehensivereviewofrecentresearchintotheapplicationoflearningtechniquesforHTTPadaptivevideo
streaming.State-of-the-arttechniquesinthefieldsofadaptivevideoencoding,bandwidthoptimization,and
qualityadaptationaresummarizedandanalyzedintermsoftheirstrengthsandlimitations.
| INDEXTERMS |     | Adaptivevideostreaming,HTTP,learningmethods. |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I. INTRODUCTION segment. A video session is then initiated by the client by
OVERthepasttwodecades,videotraffichasundergone requestingthemanifestfileofavideo,andanadaptivebitrate
|              |     |        |            |        |          |     | (ABR) | algorithm | is used | to select | the | appropriate | bitrate |
| ------------ | --- | ------ | ---------- | ------ | -------- | --- | ----- | --------- | ------- | --------- | --- | ----------- | ------- |
| a tremendous |     | amount | of growth. | It now | accounts | for |       |           |         |           |     |             |         |
levelforeachvideosegment.Oncetheadaptationalgorithm
morethan65%oftheInternettraffic[1].Thismakesitchal-
|             |         |           |              |                       |     |         | determines |        | the bitrate level | of the  | next | segment,          | the client |
| ----------- | ------- | --------- | ------------ | --------------------- | --- | ------- | ---------- | ------ | ----------------- | ------- | ---- | ----------------- | ---------- |
| lenging but | crucial | to ensure | optimal      | Quality-of-Experience |     |         |            |        |                   |         |      |                   |            |
|             |         |           |              |                       |     |         | sends      | to the | server an HTTP    | request | for  | the corresponding |            |
| (QoE) for   | video   | delivery. | These issues | motivated             |     | the in- |            |        |                   |         |      |                   |            |
segment.
| troduction | of Hypertext | Transfer | Protocol |          | (HTTP) | adaptive |     |     |     |     |     |     |     |
| ---------- | ------------ | -------- | -------- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
| streaming  | (HAS).       | HAS has  | become   | the most | widely | used     |     |     |     |     |     |     |     |
AshighlightedinFig.1,whichillustratesaDASHstream-
protocolforvideostreamingapplications,withseveralimple-
ingsystem,themainelementsofHTTP-basedadaptivevideo
| mentations, | such | as Microsoft’s | Smooth | Streaming |     | (MSS), |     |     |     |     |     |     |     |
| ----------- | ---- | -------------- | ------ | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
streamingsystemsaretheserver,thechannel,theclient,and
| Apple’s HTTP |     | Live Streaming | (HLS) | [2], | and Motion | Pic- |                |     |            |       |               |     |           |
| ------------ | --- | -------------- | ----- | ---- | ---------- | ---- | -------------- | --- | ---------- | ----- | ------------- | --- | --------- |
|              |     |                |       |      |            |      | the adaptation |     | algorithm. | Video | files encoded | at  | different |
tureExpert’sGroup’s(MPEG)DynamicAdaptiveStreaming quality levels are stored on the server. The adaptation al-
overHTTP(DASH)[3],whichisthefirstinternationalstan-
|     |     |     |     |     |     |     | gorithm | is  | then used to | select one | of those | representations |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---------- | -------- | --------------- | --- |
dardforadaptivestreamingoverHTTPthatdoesnotspecify
|                |     |                 |       |          |             |     | for each | video | segment. | In general, | the | main goal | of the |
| -------------- | --- | --------------- | ----- | -------- | ----------- | --- | -------- | ----- | -------- | ----------- | --- | --------- | ------ |
| the adaptation |     | logic. Although | there | are some | differences |     |          |       |          |             |     |           |        |
adaptationalgorithmistomaximizetheuser’sQoE.Specifi-
| between | each of | these solutions, | they | share | the same | basic |     |     |     |     |     |     |     |
| ------- | ------- | ---------------- | ---- | ----- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
cally,theadaptationalgorithmchoosesthebestqualitylevel
implementation.
|     |     |     |     |     |     |     | for each | video | segment | or chunk | based | on a set | of decision |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ------- | -------- | ----- | -------- | ----------- |
InHTTPadaptivevideostreaming,videosareencodedat parameters,suchasthechannelquality,clientbufferfullness,
multiple bitrate levels (i.e. different qualities) and divided etc.,whiletheclientisinchargeofrequestingthevideofiles,
into segments that usually range from 1 to 10 seconds. A then playing them back upon their correct reception from
manifest file- known as a Media Presentation Description theserveroverabandwidth-constrainedchannel.Inorderto
(MPD)fileforDASH-containsinformationabouttheavail- judge the quality of the video streaming session, the user’s
ablevideorepresentations,aswellastheURLsofeachvideo QoEismeasuredinreal-time.
| VOLUME4,2016 |     |     |     |     |     |     |     |     |     |     |     |     | 1   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
energyconsumption[5],amongotherchallenges.Therefore,
itiscrucialtodevelopmethodsforvideotrafficoptimization.
|     |     |     |     |     |     | Traditional     | streaming |        | approaches  |          | generally | fail       | to opti-    |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | ------ | ----------- | -------- | --------- | ---------- | ----------- |
|     |     |     |     |     |     | mize bandwidth  |           | usage; | inefficient |          | quality   | adaptation | algo-       |
|     |     |     |     |     |     | rithms greedily |           | select | higher      | bitrates | that      | are        | not optimal |
forthecurrentnetworkconditionsorcontentcharacteristics.
|     |     |     |     |     |     | Additionally,   | available    |                | computing       |          | resources        | at the       | client or   |
| --- | --- | --- | --- | --- | --- | --------------- | ------------ | -------------- | --------------- | -------- | ---------------- | ------------ | ----------- |
|     |     |     |     |     |     | server side     | are          | often          | under-utilized, |          | increasing       | the          | pressure    |
|     |     |     |     |     |     | on the network. |              | Learning-based |                 | methods, |                  | implementing | in-         |
|     |     |     |     |     |     | telligent       | adaptation   | and            | encoding,       |          | super-resolution |              | [6], and    |
|     |     |     |     |     |     | caching,        | can mitigate |                | these           | issues   | by optimizing    |              | traffic and |
FIGURE1. DASHframework. resource utilization. Using historical data, learning-based
|        |           |           |            |               |       | techniques | can     | also be | used    | to accurately |         | predict    | network |
| ------ | --------- | --------- | ---------- | ------------- | ----- | ---------- | ------- | ------- | ------- | ------------- | ------- | ---------- | ------- |
|        |           |           |            |               |       | conditions | [7]–[9] | to      | further | improve       | quality | adaptation | de-     |
| In the | following | sections, | we explore | the technical | chal- |            |         |         |         |               |         |            |         |
cisions.
| lenges facing | video | streaming | over HTTP | and | shed light |     |     |     |     |     |     |     |     |
| ------------- | ----- | --------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
onthekeyaspectsthatsubstantiallyinfluencetheefficiency
3) VideoqualityandQoE
| of streaming | systems. | Following | a brief | discussion | of exist- |     |     |     |     |     |     |     |     |
| ------------ | -------- | --------- | ------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
EnsuringhighvideoqualityanddeliveringasatisfactoryQoE
ing challenges, we highlight the contributions in addressing remains a central challenge in video streaming. Since QoE
thesechallenges.Thissurveymainlyfocusesoncurrentma-
|     |     |     |     |     |     | is used to | guide | the quality |     | adaptation | algorithm, |     | building |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | --- | ---------- | ---------- | --- | -------- |
chinelearning-basedsolutionsaimingtoenhancetheoverall
|     |     |     |     |     |     | an accurate | QoE | model | is  | extensively |     | researched | within |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- | ----------- | --- | ---------- | ------ |
streamingexperience.Inwhatfollows,wealsohighlightthe
|     |     |     |     |     |     | the literature | [10]. | However, |     | quantifying |     | the user’s | view- |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | -------- | --- | ----------- | --- | ---------- | ----- |
structureandorganizationofthissurvey.
|     |     |     |     |     |     | ing experience |       | in itself     | is a | challenging | task.       | Perception | of       |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | ------------- | ---- | ----------- | ----------- | ---------- | -------- |
|     |     |     |     |     |     | different      | users | is influenced |      | by their    | preferences |            | in terms |
A. CHALLENGESINVIDEOSTREAMING
|     |     |     |     |     |     | of both QoE | and | content. | Although |     | subjective | quality | mea- |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | -------- | --- | ---------- | ------- | ---- |
1) Energyefficiencyinvideostreamingsystems sures, such as Mean Opinion Score (MOS), are considered
Energy consumption is a growing concern across the video the most reflective of users’ actual opinions, such measures
streaming pipeline, from encoding and transcoding opera- cannotbeusedforreal-timeQoEmeasurement.Rather,QoE
tions at the server side to decoding and rendering on end- is measured in terms of objective metrics, such as visual
| user devices. | Viewers | watch | videos on a | variety | of devices, |     |     |     |     |     |     |     |     |
| ------------- | ------- | ----- | ----------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
quality(includingmetricssuchasstructuralsimilarityindex
rangingfrommobilephonestoHDTVs,eachwithdifferent (SSIM),peaksignal-to-noiseratio(PSNR),andvideomulti-
screenresolutions.Videoencodingthereforeneedstobeop- method assessment fusion (VMAF) [11]), smoothness, and
timizedtoensurethatviewerscanenjoythehighestpossible stallingduration.However,objectivemetricssuchasVMAF
qualityontheirrespectivedevices.Assuch,HASusesa“bi- orSSIMoftenfailtofullycapturethesubjectiveexperience
trateladder”,whichreferstoasetofbitrate-resolutionpairs.
|     |     |     |     |     |     | of viewers, | particularly |     | when | it comes | to  | perceptual | quality |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ---- | -------- | --- | ---------- | ------- |
Findingtheoptimalbitrateallocationacrosstheladderiscon- oruserpreferences.TraditionalframeworksuseafixedQoE
ventionally carried out using an exhaustive search method, model that usually lacks personalization, as a one-size-fits-
whichrequiresasignificantamountofpower,particularlyfor all approach is used regardless of user preference. This can
high-resolution formats, such as 4K or 8K videos, directly result in poorer viewing experience as users may prioritize
translatingintoincreasedenergyusage.Consequently,dueto
|     |     |     |     |     |     | different | aspects | or metrics |     | of QoE | [12]. | As a result, | ML is |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | --- | ------ | ----- | ------------ | ----- |
limited computationalresources, somelive video platforms, increasinglybeingusedtomodelandpredictactualperceived
such as Twitch, do not provide multiple representations for QoE,allowingforcontent-awareanduser-centricadaptation.
| all of their | users | [4], which | causes degraded |     | QoE. Data |     |     |     |     |     |     |     |     |
| ------------ | ----- | ---------- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore,learningtechniquesprovideawiderangeofso-
centersandcontentdeliverynetwork(CDN)nodesalsoface lutionstoimprovevideostreaming,allowingforefficientand
increasing pressure to minimize power consumption while adaptable encoding, traffic management, and quality adap-
maintaininglow-latency,high-throughputservice.Toaddress tation. Compared to heuristic algorithms (e.g., throughput-
these issues, machine learning (ML) techniques are being based [13] and buffer-based algorithms [14], [15]), which
proposedforenergy-awarevideoencodingandqualityadap-
|     |     |     |     |     |     | rely on a | set of | fixed | rules, | ML methods |     | have | consistently |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | ------ | ---------- | --- | ---- | ------------ |
tation, aiming to improve energy usage without degrading shown better performance in the literature; since heuristic
userexperience. algorithms use pre-defined rules to make decisions and typ-
|     |     |     |     |     |     | ically optimize |     | only | for a specific |     | set of | conditions, | most |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | -------------- | --- | ------ | ----------- | ---- |
2) Bandwidthlimitations of the research shows that they are unable to adapt to dy-
Furthermore,adaptivevideostreaming,whileprovidingim- namic or unstable conditions, optimize for multiple goals,
provedqualityanduserexperience,cancontributetoexces- and handle the high-dimensional and non-linear decision
sivebandwidthconsumptionandvideo-relatedtraffic.Video- spaces involved in video streaming [16], [17]. In simulated
related traffic suffers from congestion, high costs, and high tests, learning techniques consistently outperform heuristic
| 2   |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME4,2016 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
|     |     |     |     | FIGURE2. | Surveyorganizationroadmap. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
methods across a wide range of tasks. However, recent providing a basic tutorial and introduction to video
research [18] illustrates that the performance of learning- streaming systems for researchers in the field. Real-
based algorithms rapidly degrades in real-world scenarios, world algorithm implementation and evaluation tools
even being outperformed by simpler algorithms, as proven andplatforms,aswellasbenchmarkdatasetsandalgo-
by works like Fugu [19]. We therefore present this survey rithms,arealsoprovidedforresearchers’reference.
paper to discuss the recent advances, breakthroughs, and • A comprehensive overview of learning-based video
challengesinmachinelearning-basedvideostreamingtoaid compressionandbitrateladderpredictiontechniquesis
researchers in understanding and developing ML solutions provided. Bitrate ladder prediction methods are further
that can bridge the gap between simulations and real-world classified into three main groups: per-title, per-chunk,
| deployment.      |             |         |             |               |     | andper-sceneencoding.Allthreemethodsareevaluated |          |                   |               |     |           |          |
| ---------------- | ----------- | ------- | ----------- | ------------- | --- | ------------------------------------------------ | -------- | ----------------- | ------------- | --- | --------- | -------- |
|                  |             |         |             |               |     | and compared                                     | in       | terms             | of perceptual |     | quality,  | complex- |
| B. CONTRIBUTIONS |             |         |             |               |     | ity,bandwidthefficiency,andencodingtime.         |          |                   |               |     |           |          |
|                  |             |         |             |               |     | In-depth                                         | analysis | of learning-based |               |     | bandwidth | opti-    |
| This review      | paper makes | several | significant | contributions |     | •                                                |          |                   |               |     |           |          |
to the field of adaptive video streaming by focusing on the mization methods is carried out. Different strategies
|     |     |     |     |     |     | of reducing | video | traffic | and | bandwidth | wastage, | such |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | --- | --------- | -------- | ---- |
useofmachinelearningtechniques.Itprovidesanextensive
review and evaluation of the state-of-the-art learning-based asintelligentqualityadaptationandencoding,caching,
andvideoqualityenhancement,areexplored.
methodsforadaptivevideostreamingapplications,including
|                                                       |     |     |     |     |     | Learning-based |     | quality | adaptation | algorithms |     | are dis- |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ---------- | ---------- | --- | -------- |
| videoencoding,bandwidthoptimization,andqualityadapta- |     |     |     |     |     | •              |     |         |            |            |     |          |
tion.Otherreviewpapers[20],[21]donotfocusonmachine cussed and evaluated. Various methods of QoE model-
|                |           |              |         |         |        | ing and prediction |     | are | introduced, | as  | well as | learning- |
| -------------- | --------- | ------------ | ------- | ------- | ------ | ------------------ | --- | --- | ----------- | --- | ------- | --------- |
| learning-based | streaming | specifically | or only | discuss | select |                    |     |     |             |     |         |           |
aspects of video streaming systems, whereas this survey based methods for improving the generalizability of
|     |     |     |     |     |     | adaptation | algorithms. |     | In addition, |     | quality adaptation |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------ | --- | ------------------ | --- |
providesamoreholisticview,fromvideoencodingtotrans-
|     |     |     |     |     |     | algorithms | are | classified | based | on  | their application, |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ----- | --- | ------------------ | --- |
missionandprocessing.Whilesomerecentsurveyshavealso
coveredthevideostreamingsysteminanend-to-endmanner includingvideoondemand(VoD),live,multi-user,and
content-awarevideostreaming.
| [22], [23], | they lack | the inclusion | of essential |     | resources |     |     |     |     |     |     |     |
| ----------- | --------- | ------------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
for video streaming research, unlike our work. The main • Theshortcomingsoflearning-basedstreamingschemes
|               |                |               |     |            |     | are explored       | in  | terms | of their | generalizability, |     | real-   |
| ------------- | -------------- | ------------- | --- | ---------- | --- | ------------------ | --- | ----- | -------- | ----------------- | --- | ------- |
| contributions | of this survey | can therefore | be  | summarized | as  |                    |     |       |          |                   |     |         |
|               |                |               |     |            |     | world performance, |     | and   | security | challenges.       |     | We also |
follows:
|     |     |     |     |     |     | delve into | emerging | trends | and | new | technologies | in  |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | --- | --- | ------------ | --- |
• State-of-the-artlearningtechniquesarecoveredforeach
|     |     |     |     |     |     | video streaming |     | and | identify | possibilities | for | future |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | -------- | ------------- | --- | ------ |
stageofthestreamingpipeline.Inaddition,thestream-
researchaccordingly.
| ing          | process and | its components | are | also | explained, |     |     |     |     |     |     |     |
| ------------ | ----------- | -------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| VOLUME4,2016 |             |                |     |      |            |     |     |     |     |     |     | 3   |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
|     |     |     |     | encoding          | frameworks. |                  | Learning-based, |           | or         | learned, | video    |
| --- | --- | --- | --- | ----------------- | ----------- | ---------------- | --------------- | --------- | ---------- | -------- | -------- |
|     |     |     |     | coding frameworks |             | have             | the             | potential | to provide |          | enhanced |
|     |     |     |     | capabilities,     | such        | as content-aware |                 |           | encoding   | [28],    | reduced  |
computationalcomplexity[29],andend-to-endoptimization
ofencodingpipelines.Notableexamplesofsuchframeworks
|     |     |     |     | include | DVC [30], | which | is  | the first | end-to-end |     | neural- |
| --- | --- | --- | --- | ------- | --------- | ----- | --- | --------- | ---------- | --- | ------- |
enhancedencodingalgorithm,nowusedasabenchmarkfor
otherstudiesinthefield.[31]presentsacomparativebench-
|     |     |     |     | marking   | study | of several | learned    | video | coding    | algorithms, |       |
| --- | --- | --- | --- | --------- | ----- | ---------- | ---------- | ----- | --------- | ----------- | ----- |
|     |     |     |     | including | DVC,  | SSF        | [32], DCVC |       | [33], and | DVC-P       | [34]. |
ThestudyshowsthatDCVCachievesthebestrate-distortion
|     |     |     |     | performance | at           | the cost | of having  |                 | the highest | complexity,     |     |
| --- | --- | --- | --- | ----------- | ------------ | -------- | ---------- | --------------- | ----------- | --------------- | --- |
|     |     |     |     | whereas     | SSF achieves |          | the lowest | GPU             | memory      | occupancy       |     |
|     |     |     |     | and fastest | performance  |          | with       | the second-best |             | rate-distortion |     |
FIGURE3. Convex-hullconstruction.
|     |     |     |     | performance.  | Similarly, |        | Google | DeepMind’s |              | C3 [35]     | is an- |
| --- | --- | --- | --- | ------------- | ---------- | ------ | ------ | ---------- | ------------ | ----------- | ------ |
|     |     |     |     | other learned | video      | coding | scheme |            | that targets | complexity, |        |
C. ORGANIZATION achievingsignificantlylowerdecodingcomplexitycompared
The rest of this survey is organized as illustrated in Fig. to similar learned frameworks by overfitting a smaller, less
2. Section II gives an overview of video encoding and complexmodeltoeachvideoratherthandevelopingagener-
ladder prediction techniques using learning-based methods. alizedencodingmodel.
Research on using learning methods to optimize the bitrate However, despite their promising performance, integrat-
|                 |            |                             |      | ing learned | video | coding | frameworks |     | into existing |     | adaptive |
| --------------- | ---------- | --------------------------- | ---- | ----------- | ----- | ------ | ---------- | --- | ------------- | --- | -------- |
| and resolution, | as well as | the encoding configuration. | Sec- |             |       |        |            |     |               |     |          |
tionIIIdiscussesbandwidthoptimizationmethods.Methods streamingsystemspresentsseveralchallenges.Thesemodels
ofreducingbandwidthwastage,suchasvideoenhancement, often have high computational and memory requirements,
caching, and intelligent adaptation and encoding, are also making them unable to achieve real-time encoding perfor-
the focus of Section III. Section IV presents an outline mance[27],particularlyinthecaseofneuralnetwork-based
of learning-based quality adaptation algorithms. Different schemes. The lack of standardization and publicly available
methods of QoE modeling used by adaptation algorithms benchmarksanddatasetsforlearnedcodecsalsolimitstheir
are discussed. The implementation of quality adaptation al- widespread adoption and hinders research efforts. Evalua-
gorithms for various applications is also covered, including tion frameworks that allow for the testing and comparison
single-user, multi-user, VoD, and live scenarios. Section IV of learned coding algorithms in realistic environments are
alsoexplorescontent-awarequalityadaptation,aswellasthe thereforenecessary.
use of different learning techniques to improve the perfor- As research continues to improve the efficiency of video
manceandgeneralizabilityofadaptationalgorithms.Finally, encoding, another critical component of the encoding pro-
SectionVidentifiesemergingtrendsandgapsintheliterature cess, bitrate ladder construction, has also seen significant
andsuggestsdirectionsforfuturework. advancementsthroughmachinelearningtechniques.Inadap-
|     |     |     |     | tive video | streaming, |     | videos | are encoded | at  | multiple | reso- |
| --- | --- | --- | --- | ---------- | ---------- | --- | ------ | ----------- | --- | -------- | ----- |
II. VIDEOENCODING lutions and bitrates. The resolution and bitrate pairs, which
Traditional hybrid video coding standards like H.264/AVC make up the bitrate ladder, are selected such that users
[24] and H.265/HEVC [25] have served as the backbone canreceivethebestpossibleviewingexperiencegiventheir
of modern video encoding for decades. These standards device specifications and network conditions. Commonly,
are based on block-based hybrid architectures that include rate-distortion(RD)curvesillustratetherelationshipbetween
modules for intra/inter-frame prediction, exploiting the spa- the bitrate and the quality for each encoded resolution of a
tial and temporal redundancies of video content, transform specific video sequence. The RD curve for each resolution
coding, quantization, and entropy coding. However, while peaks at a certain bitrate range, in which this resolution
highlyoptimizedandstandardized,thesesystemsfacegrow- will have the highest quality out of all the possible reso-
inglimitations,particularlywiththeadventof4K/8Kvideo. lutions. Joining these peaks results in the construction of
Thesesystemsdonotlearnfromdataandmustbemanually a convex hull, which indicates the ideal resolution-bitrate
tuned for each content type, resolution, or bitrate range. In pairs as depicted in Fig. 3. The figure shows example RD
addition, encoding decisions rely on fixed heuristics, which curvesatthreedifferentresolutions,eachofwhichachieves
do not capture semantic or perceptual importance of video different VMAF performance depending on the bitrate. As
content. With each new standard, compression gains also illustrated,byjoiningthepeaksofeachcurve,theconstructed
becomehardertoachievewithoutincreasingthecomplexity, convexhullwillconsequentlybeabletoachievethehighest
makingreal-timeencodingmoreexpensive[26],[27]. possiblequality(orVMAF)withthelowestpossiblebitrate.
Consequently, machine learning techniques have increas- Constructingthebitrateladdertheninvolvesdeterminingthe
inglybeensuggestedtoaddressthechallengesoftraditional cross-pointsalongtheRDcurves.Thesecross-pointsarethe
| 4   |     |     |     |     |     |     |     |     |     | VOLUME4,2016 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
|     |     |     |     |     | FIGURE4. | Typesofladderencodingtechniques. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
points along the convex hull at which the current resolution the rate-distortion curves based on their VMAF perceptual
mustswitchtothenextresolution. video quality metric. The convex hull then determines the
Traditionally, fixed bitrate ladders were used for video bitrateladder.However,per-titleencodingcomesatthecost
encoding,butsuchapproachesareeithercontent-agnosticor of increased computation; a high number of pre-encodes is
|          |           |         |       |          |        |         | required | to build | the bitrate | ladder, | as  | each | video | sequence |
| -------- | --------- | ------- | ----- | -------- | ------ | ------- | -------- | -------- | ----------- | ------- | --- | ---- | ----- | -------- |
| employ a | few fixed | ladders | based | on video | genre. | They do |          |          |             |         |     |      |       |          |
nottakeintoaccountthecontentcharacteristicsofthevideo, isencodedatallresolutionsandquantizationlevelsexhaus-
which can often lead to degradation in video quality. For tively to determine the optimal encoding configuration. In
instance,videosequenceswithdetailedtexturesanddynamic addition,carryingoutexhaustivepre-encodesisinfeasiblein
content, such as action movies, require higher encoding real-timestreaming,whichrequiresaquickencodingprocess
toachievesufficientlylowlatency.
| bitrates than | those | with | static | content, | such as | talk shows. |     |     |     |     |     |     |     |     |
| ------------- | ----- | ---- | ------ | -------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Aone-size-fits-allapproachthereforeresultsincompression
|     |     |     |     |     |     |     | To address | this | challenge, |     | learning | techniques |     | can be |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | --- | -------- | ---------- | --- | ------ |
artifactsinsceneswithrapidmotionanddatawastagewhen
|     |     |     |     |     |     |     | used to | predict | the optimal | resolution-bitrate |     |     | pairs | for each |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | ------------------ | --- | --- | ----- | -------- |
encodingstaticscenes.Researchattemptstotacklethisissue
|         |            |          |     |            |           |          | video sequence. |           | Several | learning-based |        | solutions  |     | have re-  |
| ------- | ---------- | -------- | --- | ---------- | --------- | -------- | --------------- | --------- | ------- | -------------- | ------ | ---------- | --- | --------- |
| through | three main | methods: |     | per-title, | per-scene | (or per- |                 |           |         |                |        |            |     |           |
|         |            |          |     |            |           |          | cently been     | suggested | for     | bitrate        | ladder | prediction |     | to tackle |
shot),andper-chunk(orper-segment)encoding.Thesemeth-
theexhaustiveencodingprocessinvolvedinper-titleencod-
| ods construct | individual |     | encoding | ladders | for | each video, |           |       |          |            |     |           |          |     |
| ------------- | ---------- | --- | -------- | ------- | --- | ----------- | --------- | ----- | -------- | ---------- | --- | --------- | -------- | --- |
|               |            |     |          |         |     |             | ing [38], | [39]. | Learning | techniques |     | have been | deployed | to  |
scene,orchunk,respectively,basedonactualvideocontent,
|     |     |     |     |     |     |     | this end | in practice | in  | an industry |     | setting. | For | example, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ----------- | --- | -------- | --- | -------- |
makingthemafarmoreeffectivesolutionthanfixedladders.
Mux’s[40]instantper-titleencodingusesdeeplearning(DL)
Toexplorethesetechniquesandtestencodingconfigurations,
|            |           |     |          |             |         |          | to predict | the bitrate | ladder. | Similarly, |     | another | per-title | en- |
| ---------- | --------- | --- | -------- | ----------- | ------- | -------- | ---------- | ----------- | ------- | ---------- | --- | ------- | --------- | --- |
| tools such | as FFmpeg |     | [36] are | widely used | in both | industry |            |             |         |            |     |         |           |     |
codingimplementationisproposedbyBitmovin,whichana-
| and research | for       | encoding       | tasks        | (see Table     | 3           | for a list of |            |            |                |            |           |          |            |         |
| ------------ | --------- | -------------- | ------------ | -------------- | ----------- | ------------- | ---------- | ---------- | -------------- | ---------- | --------- | -------- | ---------- | ------- |
|              |           |                |              |                |             |               | lyzes the  | content    | of each        | video      | sequence  | and      | uses       | machine |
| tools and    | resources | and            | Table        | 2 for datasets | developed   | for           |            |            |                |            |           |          |            |         |
|              |           |                |              |                |             |               | learning   | to predict | the            | optimal    | encoding  |          | parameters | [41].   |
| research     | on video  | applications). |              | Figure         | 4 shows     | a summary     |            |            |                |            |           |          |            |         |
|              |           |                |              |                |             |               | Recent     | research   | in the         | literature | also      | includes | Silhavy    | et      |
| of the three | encoding  | ladder         | construction |                | techniques, | which         |            |            |                |            |           |          |            |         |
|              |           |                |              |                |             |               | al.’s [42] | design     | of an ML-based |            | per-title | encoding |            | scheme  |
arediscussedinfurtherdetailinthissection.
|     |     |     |     |     |     |     | that eliminates |     | the need | for exhaustive |     | test | encodes. | Their |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | -------------- | --- | ---- | -------- | ----- |
approachusesseveralsupervisedlearningalgorithms,includ-
A. PER-TITLEENCODING ingmulti-layerperceptronaswellassupportvectorandran-
Recent research attempts to introduce content-aware en- dom forest regression, to predict the optimal bitrate ladder.
coding solutions, such as Netflix’s per-title encoding [37], Adhuran and Kulupana [43] propose a machine learning-
which encodes each video sequence at different bitrate and based approach for per-title encoding that predicts target
resolution pairs in order to construct the convex hull of bitrates from the compressed video features. In contrast,
| VOLUME4,2016 |     |     |     |     |     |     |     |     |     |     |     |     |     | 5   |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
Katsenouetal.[44]usemachinelearningforcontent-aware tent video, which refers to videos that primarily consist of
bitrate ladder prediction using extracted features from the computer-generated content, such as text, graphics, anima-
uncompressed video sequence. In [38], the authors also use tions,ordesktopscreenrecordings.Incontrasttotraditional
the video’s spatio-temporal features to predict the cross- camera-captured video, screen content videos have distinct
over quantization parameters (QPs) using Gaussian process characteristics like sharp edges, uniform areas, rapid scene
regression,afterwhichonlytwoencodespercross-overpoint changes,andsoon,whichtraditionalcodingschemesstrug-
are used to determine the bitrate ranges for each target gle to handle efficiently. This challenge motivates the work
resolution.Theyexpanduponthisworkin[45]bymodeling presentedin[51],whichaimstodynamicallyadjusttheintra-
the relationship between QPs and bitrates across different period size (IPS), i.e., the number of frames between two
resolutions to predict the bitrate ladder. [46] also addresses intra-coding frames within a video sequence. In this way,
theissueoflatencyandenergyconsumptioninper-titlevideo theideaistofindtheoptimalIPSthatbalancescompression
encoding,proposingLADRE,alatency-awareschemebased efficiency with video quality, minimizing the RD-COST for
ontherandomforestalgorithm.LADREselectstheencoding screencontentvideos.
resolution based on the target bitrate and latency, as well Another challenge faced by per-title encoding of large
as the content spatiotemporal features. In another notable bitrate ladders is that it requires a large amount of storage.
work,Nasirietal.[47]designanensemblelearningscheme One notable work that addresses the high cost of per-title
for per-title encoding that aggregates the output of multiple encoding is developed in [52], based on the fact that it is
machine learning algorithms to compute the optimized en- commonforuserssharingthesamenetworktohavedevices
coding ladder. In case the outputs of the algorithms differ, with a wide range of capabilities, leading to increased stor-
additional test encodings are performed, and the resolution age costs as more representations are provided for different
thatproducesthehighestqualityisselectedforeachbitrate. types of devices. The authors propose the use of a scalable
Thisway,thestrengthsofeachtypeoflearningalgorithmare scheme,DeepStream,tosupportalluserswhilereducingthe
leveraged while reducing the impact of their weaknesses on streaming costs. This scalable scheme adds a content-aware
the output. However, the effectiveness of such an approach super-resolutionneuralnetwork-basedenhancementlayerto
forliveorreal-timestreamingmaybelimited,dependingon theexistingbitrateladderfordeviceswithGPUcapabilities.
the computation time required by the ML algorithms. This UserswithnoGPUcapabilitiesreceivethebaselayer,which
schemealsorequiresahighercomputationalcost. isthevideobitstreamattherepresentationsavailableonthe
While most of the literature is devoted to adapting the bitrate ladder, while users with sufficient computational ca-
resolutionandbitratetoconstructtheencodingladder,some pabilitiesreceiveanenhancementlayer,whichincludesboth
worksproposetheadaptationofotherencodingparameters. thebaselayeraswellasasuper-resolutionneuralnetworkfor
Onesuchwork[48]proposestheuseofmachinelearningfor each representation, compressed using DeepCABAC [53].
bitrate ladder estimation at a lower computational cost. En- Few other works address this aspect of per-title encoding,
codershavedifferentconfigurations,orpresets,thattradeoff however.
compression efficiency for compression speed. The fastest
presetofanencoderistheonewiththelowestcompression B. PER-SCENEENCODING
efficiency, and vice versa. In [48], the bitrate ladder for the Despite the improvement of per-title approaches over tradi-
slow (high-efficiency) preset of a given encoder is built by tional encoding schemes, generating a single bitrate ladder
predictingitscross-overpointsusingdecisiontreealgorithm, for the entire video sequence may still lead to degraded
giventhecross-overpointbitratesofthefast(low-efficiency) perceptual quality and bandwidth inefficiency, especially in
preset. This approach therefore manages to combine both videos with dynamic scene changes. This is because high
speed and efficiency for encoding ladder prediction with complexity scenes require higher bitrate allocation as com-
lower computational demands. The authors in [49] propose pared to low complexity scenes, which can be represented
a similar encoding scheme using random forest regression atanacceptablevisualqualityusinglessbits.Consequently,
butadditionallyintroduceacross-codecapproachthatallows using per-title encoding may not only lead to sub-optimal
the fast preset configuration of a certain encoder to be used visualqualitybuttoinefficientbandwidthutilization,aswell.
to predict the optimal configuration of another encoder. An Per-sceneorper-chunkencodingarethemainalternatives
alternative per-title approach is proposed in [50], which to per-title encoding introduced in the literature [54], [55],
usesimitationlearningtojointlyoptimizetheresolutionand [56]. Per-scene encoding involves predicting the bitrate lad-
chunkduration,formingtheresolution-duration(RD)ladder. der for each video scene, which consists of one or more
Duringthetranscodingprocess,thisschemeaccountsfornot segments. Each video scene consists of a duration of the
onlythevideocontentbutthenetworkcapacityandstorage video throughout which there is no significant change in
costs as well. By varying the chunk duration based on the contentcomplexity.Therefore,encodingthevideoonaper-
videocontent,greaterencodingefficiencycanbeachieved. scenebasisresultsinimprovedvisualqualityandbandwidth
Other encoding parameters are also targeted in the liter- efficiency. Such encoding approaches are now being practi-
ature to account for different types of videos. For example, cally implemented by some video streaming services, such
different coding schemes may be required for screen con- as Netflix’s per-shot encoder [57]. However, an exhaustive
6 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
approachisstillcommonlyusedforbitrateladdergeneration, C. PER-CHUNKENCODING
which is addressed in recent research through the use of Per-chunkencoding,ontheotherhand,involvesbitratelad-
machinelearning. der prediction on a per-chunk, or per-segment, basis, where
Naturally, before encoding begins, this method first re- each chunk is simply a pre-determined, fixed duration of
quires scene detection and analysis, which is approached in video, independent of the type of video content. Per-chunk
several ways in the literature. Deep Encode [54] is one im- encoding is based on the assumption that each video seg-
plementationproposedbyMuelleretal.,whichisalearning- ment generally has the same content complexity throughout
based encoding framework that uses feature extraction to its duration, due to segments usually being less than 10
predict the encoding ladder for each scene, thus reducing seconds long. As such, many works [65] tend to choose
bandwidth requirements. FAUST [58] is another per-scene per-chunk encoding over per-scene encoding, in order to
encoding solution that uses entropy-based scene detection skip the scene detection step. One such approach in [55]
andaneuralnetworktopredicttheoptimizedbitrateladder. also attempts to simplify the content analysis step. It uses a
Another approach uses the discrete cosine transform (DCT) deepreinforcementlearning(DRL)frameworkforper-chunk
energyofthefirstgroupofpictures(GOP)fromeachscene bitrate ladder prediction based on video content, network
for complexity analysis within a per-scene encoding frame- capacity, and storage cost. However, the content of each
workforlivestreaming[56]. segment is analyzed by examining only the I-frame, which
After scene detection, the bitrate ladder is then encoded maynot necessarilybe representativeof theentiresegment,
in the same way as per-title encoding, but for each scene particularly if longer segment durations are used. Another
rather than each video. Several techniques are proposed in recentworkonper-chunkencodingisproposedin[66].The
the literature for the scene encoding step, such as the use authors design a deep neural network that predicts the CRF
of recurrent convolutional networks to predict the convex for a given target VMAF value based on the video segment
hull [59]. Xing et al. also use a deep learning approach to features.
predict the optimal constant rate factor (CRF) for a certain In the case of live streaming, low-latency coding ap-
target VMAF for each video scene [60]. CRF is an encod- proachesarerequiredtomaintainhighQoE.Assuch,encod-
ing method by which the quality is kept constant through ingefficiencycanbesacrificedforspeed;forexample,one-
adjusting the bitrate based on the video content. There- passencodingisoftenusedratherthantwo-passencoding.In
fore, by adjusting the CRF, both the perceived quality and one-passencoding,theencoderprocessesthecontentinone
compression efficiency can be improved. In another neural “pass”,quicklyallocatingbitratebasedoninformationabout
network-basedapproach,[61]makesuseoftransferlearning thecurrentandpastframes.Two-passencoding,ontheother
toreusepre-traineddeepneuralnetworks(DNNs),allowing hand, involves an initial pass to analyze video content over
the construction of the bitrate ladder with limited training thewholeduration,thenasecondpassforbitrateallocation,
data. This per-scene scheme predicts the minimum bitrate makingitmoreefficientbutslower.Intuitively,one-passen-
required to achieve the highest quality level on the bitrate codingismoresuitabletomeetthelowlatencyrequirements
ladder, essentially preventing bitrate wastage with only a oflivestreaming,meaningthatlivestreamsareoftenencoded
slight reduction in quality. In [62], a vision transformer is inefficiently. A recent work that successfully addresses this
used instead for bitrate ladder prediction. Alternatively, the problempresentsETPS[39],atwo-passencodingschemefor
authors in [63] used machine learning classifiers to predict live streaming that improves compression efficiency while
the optimal resolution for each bitrate without the need for maintaining the required low latency. ETPS uses the spatial
multiple test encodes. [64] presents a benchmarking study and temporal complexity based on the DCT energy of the
comparing different types of ML techniques for per-scene first GOP of a segment to determine the optimized CRF.
ladder construction, including several ML and DL models. Other approaches similarly attempt to improve the process
Their results show that ML models outperform DL models, of live video coding by taking advantage of other encoding
possiblyduetothesmallsizeofthetrainingdataset,withthe parameters. In order to meet stringent latency and quality
extratreesregressorachievingthebestperformance. requirements,theseapproachesoptimizethevideoencoding
The content-aware nature of these per-scene encoding configuration. The authors in [67] analyze the relationship
approaches results in improved coding efficiency and vi- betweenvariousencodingparameters(suchasthenumberof
sualquality.Byconstructingadifferentencodingladderfor framespersecondandencodingspeed)andvideoperceptual
eachindividualscene,lowcomplexityscenesdonotreceive quality; they find that varying the encoding configuration
unnecessarily high bitrates, while high complexity scenes ratherthanjustadjustingtheresolutionorbitratecanachieve
receivesufficientbitratestoachieveahighperceptualquality. acceptable levels of both latency and video quality. Based
However,thetimetakenforscenedetectionandcomplexity ontheiranalysis,theydesignareinforcementlearning(RL)-
analysis, followed by bitrate ladder prediction, results in basedschemeforoptimizingencodingconfigurationinreal-
added delay for per-scene approaches, which may be unac- time video streaming with a client-side super-resolution al-
ceptableespeciallyinlivestreamingscenarios.Furthermore, gorithmtofurtherimprovethevideoquality.
the cost of per-scene encoding outweighs the benefits in Both per-scene and per-chunk encoding schemes result
videosequenceswithfewscenechanges. insignificantbitratesavingscomparedtoper-titleencoding,
VOLUME4,2016 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
TABLE1. Descriptionofrelevantlearningalgorithms.
|     | Learningalgorithm |     |     |     |     | Briefdescription |     |     |     | Advantages |     | Challenges |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | ---------- | --- | ---------- | --- | --- | --- |
Anagentlearnstotakeactionsinan
|     |     | Reinforcement |     |                                         |     |     |     |     | Solvesmorecomplex  |     |     |                     |     |     |     |
| --- | --- | ------------- | --- | --------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | ------------------- | --- | --- | --- |
|     |     |               |     | environmenttomaximizerewardsbyreceiving |     |     |     |     |                    |     |     | Highcomputationcost |     |     |     |
|     |     | learning      |     |                                         |     |     |     |     | sequentialproblems |     |     |                     |     |     |     |
feedbackthrougharewardsignal
Amodel-freereinforcementlearningalgorithm
Curseofdimensionality,
Q-learning thatlearnsaction-valuefunctions(Q-values) Off-policy,model-free overestimationofQ-values
toevaluatethequalityofactionsinstates
Fasterconvergence,
|     |     | Apprenticeship |     |     | Agentslearnapolicythrough |     |     |     |     |     |     | Dependenceonexpert, |     |     |     |
| --- | --- | -------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
doesnotrequirelarge
|     |     | learning |     |     | observinganexpertdemonstration |     |     |     |     |     |     | limitedexploration |     |     |     |
| --- | --- | -------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
quantitiesoftrainingdata
Trainingisdoneinameaningfulorder,starting
|     |     | Curriculum |     | witheasytasksandevolvingtolearnmore |     |     |     |     |                   |     |     | Designing          |     |     |     |
| --- | --- | ---------- | --- | ----------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | ------------------ | --- | --- | --- |
|     |     | learning   |     |                                     |     |     |     |     | Fasterconvergence |     |     | effectivecurricula |     |     |     |
complextasks,mimickinghumanlearning
Agentslearnfromtheoutputofothertasks, Greateradaptability, Highcomplexity,
Metalearning
generallyreferredtoaslearningtolearn fasterconvergence largetrainingdatasets
Fastertrainingtime,
|     |     | Supervised   |     | Asubsetofmachinelearningalgorithms |                             |     |     |     |                         |     |     |                        |     |     |     |
| --- | --- | ------------ | --- | ---------------------------------- | --------------------------- | --- | --- | --- | ----------------------- | --- | --- | ---------------------- | --- | --- | --- |
|     |     |              |     |                                    |                             |     |     |     | higheraccuracy          |     |     | Complexdatapreparation |     |     |     |
|     |     | learning     |     |                                    | thattrainusinglabeleddata   |     |     |     | thanunsupervisedmethods |     |     |                        |     |     |     |
|     |     |              |     |                                    | Asubsetofmachinelearning    |     |     |     |                         |     |     | Longertrainingtime,    |     |     |     |
|     |     | Unsupervised |     |                                    |                             |     |     |     | Simplerdatapreparation, |     |     |                        |     |     |     |
|     |     |              |     |                                    | algorithmsthatlearnpatterns |     |     |     |                         |     |     | loweraccuracy          |     |     |     |
|     |     | learning     |     |                                    |                             |     |     |     | uncovershiddenpatterns  |     |     |                        |     |     |     |
|     |     |              |     |                                    | andtrainusingunlabeleddata  |     |     |     |                         |     |     | thansupervisedmethods  |     |     |     |
particularly in video sequences with highly dynamic scene while the quality increases linearly for a specific range of
changes. Using per-chunk encoding in particular avoids the bitrates,increasingthebitratefurtheroutsidethelinearrange
processofscenedetection,whichresultsinadditionaldelay. doesnothaveanoticeableeffectonvideoquality[68].Intyp-
Itsquickerimplementationmakesper-chunkencodingmore ical adaptive bitrate algorithms, higher bitrates are selected
suitable for live streaming scenarios. On the other hand, greedily, increasing energy and data consumption without
scene changes may occur within the duration of the chunk, anyperceivableincreaseinquality.Turkkanetal.[68]design
particularlyinvideoswithlongerchunkdurations,leadingto adeepQ-learning(DQL)-basedABRalgorithm,GreenABR,
sub-optimalbitrateusageandperceptualqualityifper-chunk to address this. Their framework reduces data consumption
encodingisused. due to video streaming while maintaining high QoE by
|     |     |     |     |     |     |     |     | adding | an  | energy penalty | to  | the learning | model’s |     | reward. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------- | --- | ------------ | ------- | --- | ------- |
III. BANDWIDTHOPTIMIZATION As a result, GreenABR manages to significantly improve
Video-relatedtrafficconstitutesthemajorityofInternettraf- bandwidth efficiency and reduce energy consumption com-
fic, and as a result, the growing demand for ultra-high- pared to state-of-the-art algorithms such as Pensieve [16]
|            |       |     |           |     |        |         |           | while | achieving | comparable |     | QoE. Other | research | [69] | uti- |
| ---------- | ----- | --- | --------- | --- | ------ | ------- | --------- | ----- | --------- | ---------- | --- | ---------- | -------- | ---- | ---- |
| definition | (UHD) |     | video and | the | advent | of 360° | streaming |       |           |            |     |            |          |      |      |
hasledtoincreasedbandwidthrequirements.Consequently, lizes measures such as VMAF to ensure the selection of
efficientlyutilizingtheavailablebandwidthhasbecomeone bitratesthatresultinanappreciableimprovementinquality.
of the core challenges for video streaming. Traditional ap- Such perceptual quality-aware streaming approaches ensure
proaches to video streaming, often relying on fixed rules, thathighbitratesarenotunnecessarilyselectedwithoutany
fail to adapt to the variability of network conditions. Con- visiblevisualimprovement.
| sequently, |            | substantial | data  | wastage     | occurs | during  | periods     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ----------- | ----- | ----------- | ------ | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of ample   | bandwidth, |             | while | sub-optimal |        | quality | during net- |     |     |     |     |     |     |     |     |
2) Buffer-awarequalityadaptation
work congestion reduces user satisfaction. To address this Aside from perceptual quality, another factor that can be
| issue, | learning | techniques |     | have | emerged | as an | alternative |     |     |     |     |     |     |     |     |
| ------ | -------- | ---------- | --- | ---- | ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
targetedtooptimizebandwidthusageisthebufferoccupancy.
approachtointelligentlyutilizeavailablenetworkbandwidth
|     |     |     |     |     |     |     |     | Some | works | do this | through | optimizing | the | pre-fetching |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ------- | ------- | ---------- | --- | ------------ | --- |
andreducedatawastage.Theirabilitytolearnfromhistorical decision.Greedilyrequestingvideochunksandfillingupthe
| patterns | and | adapt | in real-time | enables |     | them to | tailor their |          |     |                   |     |             |           |     |        |
| -------- | --- | ----- | ------------ | ------- | --- | ------- | ------------ | -------- | --- | ----------------- | --- | ----------- | --------- | --- | ------ |
|          |     |       |              |         |     |         |              | playback |     | buffer can result | in  | inefficient | bandwidth |     | usage. |
actions to varying network conditions. This section delves Although pre-fetching content can reduce the risk of re-
| into | the use | of learning-based |     | methods |     | to optimize | video |           |     |             |          |        |      |         |         |
| ---- | ------- | ----------------- | --- | ------- | --- | ----------- | ----- | --------- | --- | ----------- | -------- | ------ | ---- | ------- | ------- |
|      |         |                   |     |         |     |             |       | buffering |     | and improve | the QoE, | it can | lead | to data | wastage |
streamingtrafficwithoutcompromisingperceptualquality.
|     |     |     |     |     |     |     |     | if the | user | stops watching. |     | This is | addressed   | in        | Qian et |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --------------- | --- | ------- | ----------- | --------- | ------- |
|     |     |     |     |     |     |     |     | al.’s  | work | on DAM [70].    | DAM | is a    | short video | streaming |         |
A. INTELLIGENTADAPTATIONANDENCODING
frameworkforreducingdatawastageduetopre-fetching.Its
1) Perceptually-awarequalityadaptation DRL-based ABR algorithm is responsible for selecting the
Inadaptivestreaming,videosareencodedatmultiplebitrates videochunktobedownloaded,itsbitrate,andthepausetime,
which make up the bitrate ladder. A lower bitrate generally during which downloading is paused. A similar approach is
correspondstolowervideoquality.However,increasingthe proposed in [71], which uses multi-agent RL with expert
bitrate does not necessarily mean increasing the quality; guidance, dividing the pre-fetching and bitrate decisions
| 8   |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME4,2016 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
between two different agents sequentially. The authors in quality past the JND threshold. In this way, the encod-
[72] also attempt to reduce traffic wastage through buffer ing energy is reduced significantly while remaining within
management in their design of a transformer-based model acceptable latency bounds and maintaining the perceptual
for predicting the transmission time of video data. This quality. However, such implementations assume that client
prediction is then used to control both the selected chunk deviceshaveGPUcapabilitiesandareabletocarryoutreal-
quality and waiting time between chunk downloads. This timesuper-resolution,whichiscertainlynotalwaysthecase.
way, the buffer is not filled up blindly, which is particularly Nonetheless, it is a first step in the direction of energy- and
essentialinthecaseofshortvideostreaming. bandwidth-efficientvideocoding.
Other research addresses the problem of bandwidth op-
timization through buffer management. Inadequate buffer B. SUPER-RESOLUTION
size can also lead to data wastage as a result of viewer Super-resolution(SR)istheprocessofenhancingtheresolu-
abandonment.Whenviewersabandonthevideoearlyorskip tion of an image to construct a high resolution (HR) image
ahead,thepre-fetcheddatathathasalreadybeendownloaded from the one of low resolution (LR). In the case of video
is wasted. To mitigate this problem, Huang et al. [73] de- applications,the“images”refertothevideoframesinstead.
signDeepBuffer,abuffer-awareDRL-basedABRalgorithm. Single-image super-resolution (SISR) involves reconstruct-
DeepBufferselectsboththevideobitrateaswellasthemax- ing HR video frames on an individual basis. Video super-
imumbufferoccupancyforthenextsegment.[74]proposes resolution (VSR), on the other hand, also leverages tem-
asimilarDRL-basedABRalgorithmspecificallytoimprove poral information across consecutive frames to improve the
theenergyefficiencyofstreamingover5Gnetworks.These super-resolution accuracy. As such, SR techniques present
approachesensurethatthebuffersizeisoptimizedaccording an effective solution for improving visual quality in image
to current network conditions and, consequently, bandwidth and video applications. This means that they can also be
wastageduetopre-fetchedcontentisreduced. leveragedtoreducevideotraffic.Ratherthanrequestinghigh
video bitrates directly from the video server, SR techniques
3) JND-basedencoding canbeutilizedtoenhancethequalityoflow-qualitychunks
Asimilarconceptcanbeappliedduringthevideoencoding aftertransmission,thusreducingthebandwidthrequiredfor
stage as well. Section II explains the principles of video streaming. The potential of this technique has motivated
codingandbitrateladderconstruction.Here,wealsoprovide a significant amount of research in recent years, including
abriefoverviewofrecentworksonvideocodingwhichare industry-driven researchefforts, suchas Amazon’sSUPER-
targeted toward reducing bandwidth wastage. These works VEGAN [79]. In this section, we explore the types of SR
make use of several methods to achieve their goal, such as used for video streaming, as well as their drawbacks and
theJustNoticeableDifference(JND).JNDisaqualitymetric challenges.
thatmeasurestheminimumvisualperceivabledifferenceby
the human eye. Some research [75] is dedicated to JND 1) Single-framesuper-resolution(SFSR)
prediction, which presents another challenge on its own. Several works use SISR for video quality enhancement, as
Usingencodingladderswithnoperceivablevisualdifference describedabove[80]–[83].Inthismethod,eachvideoframe
between each quality level leads to data wastage. As such, is enhanced individually, so it is sometimes also referred to
recentworksaimtodesignJND-awareencodingalgorithms. as per-frame or single-frame SR. Well-known SISR models
The authors in [76] propose an ML-based per-title en- often used in the literature include SRCNN [84], ESPCN
codingschemebasedonJND.Thisframeworkusessupport [85],RDN[86],RFDN[87],andESRGAN[88].Whenused
vectorregressiontopredicttheJNDandgeneratesanencod- for video super-resolution, such methods have the potential
ing ladder with constant JND intervals. Similarly, another togreatlyreducethebandwidthrequiredforvideostreaming.
model, MCBE [77], aims to reduce the energy consump- In an earlier work that utilizes SFSR, Yeo et al. [80] design
tion of adaptive video streaming by optimizing the bitrate a content-aware scheme that trains several SR networks for
ladders of different video codecs. It employs the random differentgenresofvideocontent.Throughtheuseofcontent-
forest algorithm to predict the video quality, represented by aware SR, their framework achieves significant bandwidth
the VMAF score, of different bitrate-resolution pairs and savingswhilemaintainingperceptualquality.
eliminatestheredundantrepresentationsthatdonotenhance While SFSR has a simpler processing pipeline compared
perceived video quality beyond a certain JND threshold. to multi-frame super-resolution, applying a super-resolution
Another JND-based scheme is ViSOR [78], a video super- model to every frame independently can become computa-
resolution-awareonlineschemethattakesadvantageofclient tionallyexpensiveandresource-intensiveforreal-timevideo
computingcapabilitiestoreducetheenergyconsumptionof applications, especially on devices with limited computa-
the encoding process. ViSOR operates by optimizing the tional capabilities, such as mobile devices. Recent studies
resolution for each target bitrate, given a maximum latency showthatSFSRrequiressignificantlymoreenergyandcom-
threshold.Therandomforestalgorithmisusedtopredictthe putational resources, causing excessive heat dissipation and
qualityachievedafterapplyingsuper-resolution,eliminating shorter battery life on mobile devices [89]. Furthermore,
redundant representations that do not improve perceptual SFSRfailstoleveragetemporaldependenciesbetweenvideo
VOLUME4,2016 9
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
frames,whichcanresultinrepetitivecomputation,temporal Taking advantage of edge computing, many recent works
inconsistencies,anddegradedquality.Theselimitationshave implement SR at the edge server [83], [96]–[102]. [96]
motivatedthedevelopmentofmoreefficientreference-based presentsaDRL-basedscheme,inwhichvideoenhancement
ormulti-frameSRmethodstailoredforvideoapplications. takesplaceatthemobileedgecomputing(MEC)servertore-
ducethecomputationalloadontheclient.Anotherapproach
presentedbyFilhoandMelo[97]usesSRattheedgeserver
2) Multi-framesuper-resolution(MFSR)
toupscaleLRvideosandstorethemalongwiththegenerated
| In contrast | to SFSR, | many | video | streaming |     | frameworks | use |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | ----- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SRvideos.Agenerativeadversarialnetwork(GAN)isused
| multi-frame | SR            | instead      | [89]–[92], | which       | typically |             | exploits |            |              |            |                  |           |           |                 |           |
| ----------- | ------------- | ------------ | ---------- | ----------- | --------- | ----------- | -------- | ---------- | ------------ | ---------- | ---------------- | --------- | --------- | --------------- | --------- |
|             |               |              |            |             |           |             |          | to perform | SR           | in this    | work. GANs       | consist   |           | of a generative |           |
| information | from          | multiple     | frames     | to          | enhance   | resolution, |          |            |              |            |                  |           |           |                 |           |
|             |               |              |            |             |           |             |          | network-   | which        | is trained | to               | generate  | SR images |                 | from LR   |
| thereby     | improving     | temporal     |            | consistency | and       | overall     | visual   |            |              |            |                  |           |           |                 |           |
|             |               |              |            |             |           |             |          | images     | and reduce   | the        | difference       | between   |           | the SR          | and HR    |
| quality.    | Additionally, | MFSR         |            | exploits    | temporal  | redundancy  |          |            |              |            |                  |           |           |                 |           |
|             |               |              |            |             |           |             |          | ground     | truth images | as         | far as           | possible- | and       | a discriminator |           |
| to reduce   | computation   |              | time,      | making      | it more   | suitable    | for      |            |              |            |                  |           |           |                 |           |
|             |               |              |            |             |           |             |          | network-   | which        | is trained | to differentiate |           | between   |                 | synthetic |
| real-time   | quality       | enhancement. |            | For         | example,  | NEMO        | [89]     |            |              |            |                  |           |           |                 |           |
SRframesandHRframes.Onenoteworthyworkthatlever-
| is a well-known |     | SR framework |     | that | leverages | inter-frame |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ---- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
agesedge-assistedSRispresentedinVISCA[98].VISCAis
| dependencies | to  | upscale | ordinary | video | frames | based | on  |     |     |     |     |     |     |     |     |
| ------------ | --- | ------- | -------- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ajointSRandcachingschemethatmakescachingdecisions
| a set of | reconstructed |     | SR frames | known | as  | anchor | points. |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | ----- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedonvideopopularityandpotentialSRenhancement.It
Usingthisscheme,theQoE,aswellasthedeviceprocessing
|             |        |              |     |            |              |            |        | then enhances |       | the quality | of low  | quality  | cached     | content | at         |
| ----------- | ------ | ------------ | --- | ---------- | ------------ | ---------- | ------ | ------------- | ----- | ----------- | ------- | -------- | ---------- | ------- | ---------- |
| throughput, | energy | consumption, |     | and        | temperature, |            | can be |               |       |             |         |          |            |         |            |
|             |        |              |     |            |              |            |        | the edge      | using | FRVSR       | [103].  | In order | to account |         | for avail- |
| improved    | and    | maintained   | at  | acceptable | levels.      | Similarly, |        |               |       |             |         |          |            |         |            |
|             |        |              |     |            |              |            |        | ability of    | edge  | resources,  | VISCA’s | ABR      | algorithm  |         | selects    |
Shenetal.presentPASS-Net[91],anotherMFSRmodelfor
|     |     |     |     |     |     |     |     | the next | segment | resolution | and | decides | whether | to  | retrieve |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---------- | --- | ------- | ------- | --- | -------- |
adaptivestreaming.PASS-Netisajointframepredictionand
thesegmentfromtheoriginserveroredgecache,ortoapply
enhancementframeworkforthecasesoflostframesandre-
super-resolutiontoaLRversion.
ceivedlow-resolutionframes.Framepredictionusesprevious
|     |     |     |     |     |     |     |     | However, | such | edge-based |     | approaches | will | naturally | in- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------- | --- | ---------- | ---- | --------- | --- |
high-resolutionframesinordertopredictlostframes,while
|     |     |     |     |     |     |     |     | crease the | demand | on  | the edge | server | and | may waste | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | -------- | ------ | --- | --------- | --- |
frameenhancementusesreference-basedsuper-resolution.
|          |     |         |           |     |       |         |       | computational |     | capacity | of more | high-end | devices. |     | This is |
| -------- | --- | ------- | --------- | --- | ----- | ------- | ----- | ------------- | --- | -------- | ------- | -------- | -------- | --- | ------- |
| In [92], | the | authors | implement | and | adapt | several | image |               |     |          |         |          |          |     |         |
addressedinLiuetal.’sworkin[100].Theirworktakesad-
| SR models | (EDSR | [93], | RDN | [86], | and RCAN | [94]) | for |     |     |     |     |     |     |     |     |
| --------- | ----- | ----- | --- | ----- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vantageofbothedgeserverandclientcomputingresourcesto
| video SR | and | propose | a learning-based |     | ensemble |     | method |     |     |     |     |     |     |     |     |
| -------- | --- | ------- | ---------------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
performsuper-resolution,withaDRL-basedABRalgorithm
thatusestheoutputsofeachSRmethod.Ratherthanapply-
|                |                     |        |       |                    |         |               |       | that selects | the      | video     | resolution,    | reconstructed |                   | resolution, |          |
| -------------- | ------------------- | ------ | ----- | ------------------ | ------- | ------------- | ----- | ------------ | -------- | --------- | -------------- | ------------- | ----------------- | ----------- | -------- |
| ing SR         | on a frame-by-frame |        |       | basis using        | 3D      | convolutional |       |              |          |           |                |               |                   |             |          |
|                |                     |        |       |                    |         |               |       | and client   | workload | share.    | In             | their         | framework,        | the         | server   |
| neural network |                     | (CNN), | which | is computationally |         | intensive,    |       |              |          |           |                |               |                   |             |          |
|                |                     |        |       |                    |         |               |       | uses a large | SR       | model     | to reconstruct |               | video             | tiles       | with low |
| the authors    | suggested           |        | using | 2D CNN             | on      | a super       | image |              |          |           |                |               |                   |             |          |
|                |                     |        |       |                    |         |               |       | PSNR,        | while    | high PSNR | video          | tiles         | are reconstructed |             | by a     |
| consisting     | of concatenated     |        | video | frames.            | Another |               | MFSR- |              |          |           |                |               |                   |             |          |
lightweightSRmodelattheclient-side.
| based scheme | [90] | named | BiSR | takes | advantage | of  | the fact |     |     |     |     |     |     |     |     |
| ------------ | ---- | ----- | ---- | ----- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
thatkeyframesarelargerthannon-keyframes.Itdownscales
|             |     |         |            |      |         |           |     | 4) Livesuper-resolution |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ---------- | ---- | ------- | --------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
| and applies | SR  | to only | key frames | then | encodes | dependent |     |                         |     |     |     |     |     |     |     |
Furthermore,super-resolutioncanalsobeusedtoreducethe
non-key frames at a high resolution. Thus, the transmission streamingbitrateinlivestreamingscenarioswhileimproving
overheadisreducedwithoutreducingthequality.BiSRalso
|                |                |     |     |             |        |          |     | the video       | quality. | Kim      | et al. | leverage | super-resolution |         | for   |
| -------------- | -------------- | --- | --- | ----------- | ------ | -------- | --- | --------------- | -------- | -------- | ------ | -------- | ---------------- | ------- | ----- |
| trains several | video-specific |     |     | overfitting | neural | networks | of  |                 |          |          |        |          |                  |         |       |
|                |                |     |     |             |        |          |     | live streaming, |          | in which | the    | video    | stream’s         | quality | often |
differentsizes.
|     |     |     |     |     |     |     |     | depends | on the | streamer’s | network | conditions. |     | To  | address |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------- | ------- | ----------- | --- | --- | ------- |
thisissue,theauthorsdevelopLiveNAS[104],aserver-side
3) Edge-assistedsuper-resolution online super-resolution live video framework that enhances
Despite the immense potential of SR for simultaneously live video quality regardless of the available ingest-side
improving video quality and reducing streaming traffic, it bandwidth.UsingLiveNAS,livevideostreamsareuploaded
faces several challenges, of which perhaps the most critical at low resolution, and the server-side SR network then en-
is its high computational requirements. Most SR methods hances the video frames, resulting in significant bandwidth
|          |        |           |      |         |     |               |     | savings. | Similarly, | some | works | [99], | [101] | leverage | edge |
| -------- | ------ | --------- | ---- | ------- | --- | ------------- | --- | -------- | ---------- | ---- | ----- | ----- | ----- | -------- | ---- |
| use deep | neural | networks, | such | as CNNs | and | transformers, |     |          |            |      |       |       |       |          |      |
whichinvolvenumerousparametersandrequireheavycom- computing to implement low-latency SR. In LiveSR [99],
putationslikematrixmultiplications.Assuch,clientdevices a low-resolution representation of each video segment is
areoftenincapableofimplementingreal-timeSR,especially transmittedfromthevideoservertotheedgeservers,where
those devices that do not have GPU capabilities [95]. The the segment is reconstructed at a higher resolution using
|           |      |           |     |          |             |     |          | ESPCN | [85]. | The video | segment | is  | then | transcoded | into |
| --------- | ---- | --------- | --- | -------- | ----------- | --- | -------- | ----- | ----- | --------- | ------- | --- | ---- | ---------- | ---- |
| advent of | edge | computing | has | provided | a potential |     | solution |       |       |           |         |     |      |            |      |
to this issue; edge servers have far more advanced capabili- multiple qualities to allow ABR selection at the client side,
ties, making them suitable for carrying out computationally resultinginnotablebandwidthsavingsaswellasQoEgains.
expensivetaskssuchasSR.
| 10  |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME4,2016 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
5) Videosuper-resolutionchallenges [106], [107], [109]–[112]. For example, SuperABR [83] is
Although significant strides have been made in the field of arecentedge-basedframeworkcombiningbitrateadaptation
super-resolution,videosuper-resolutionstillfacesnumerous withqualityenhancement.Itutilizesaqueue-learning-based
|     |     |     |     |     |     |     |     | DRL approach | to  | optimize | both the | source | transmission |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | -------- | ------ | ------------ | --- |
challengesthatstandinthewayofwidespreadimplementa-
tion.Device-dependenceisonesuchfactorthatsignificantly resolution and the VSR-reconstructed resolution, thus bal-
reduces the effectiveness of existing SR techniques. While ancing video quality and resource constraints. However,
several SR models, such as ESPCN [85], are described as such works remain few in the literature, leaving room for
low-latency, low-computation models with real-time perfor- improvementinthedesignofoptimizedenhancement-aware
ABRalgorithms.
| mance, | it is important |     | to clarify | their | feasibility | on  | devices |     |     |     |     |     |     |     |
| ------ | --------------- | --- | ---------- | ----- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
without GPUs, such as mobile phones. SR performance In addition, despite the proliferation of VSR methods,
dependsonseveralfactors,includingtheinputresolution.On quantifying the effect of SR on enhanced videos remains
|          |          |      |           |     |        |          |     | a challenge, | with | few accurate | quantitative |     | measures | and |
| -------- | -------- | ---- | --------- | --- | ------ | -------- | --- | ------------ | ---- | ------------ | ------------ | --- | -------- | --- |
| CPU-only | devices, | near | real-time | SR  | may be | achieved | for |              |      |              |              |     |          |     |
low-resolutioninputs.However,forhigher-resolutioninputs, evaluation frameworks. Some recent works have begun to
real-time SR is often not achievable due to the increased address this gap, such as Reznik et al.’s [113] SR quality
numberofcomputationsrequired. evaluationmetric,whichusesageneralizedWesterink-Roufs
We illustrate this by using ESPCN to enhance the videos model. The authors in [114] also develop MoViDNN, an
|                 |     |           |     |              |     |       |          | evaluation | application | for | video enhancement |     | models | on  |
| --------------- | --- | --------- | --- | ------------ | --- | ----- | -------- | ---------- | ----------- | --- | ----------------- | --- | ------ | --- |
| of the Waterloo |     | Streaming | QoE | Database-III |     | [105] | at three |            |             |     |                   |     |        |     |
inputresolutions{144,240,360}p.Weuseanupscalefactor mobiledevices.Thisplatformmeasuresvariousperformance
of2andmeasuretheSRprocessingtimeinframespersecond metrics, such as the PSNR, SSIM, and execution time, al-
(fps).TheSRmodelachievesframeratesof13.2-18.5,10.3- lowing quality enhancement methods to be evaluated and
12.0, and 5.0-6.4 fps at the three input resolutions, respec- comparedinasystematicway.
tively.Itcanbeseenthateveninputvideoswithresolutionsas
lowas360parestillunabletoachievereal-timeperformance C. CACHING
using state-of-the-art SR models without GPU. This shows Thefinalbandwidthoptimizationtechniquediscussedinthis
|          |        |            |     |          |              |     |      | work is | known as | caching, | a method | by which | content | is  |
| -------- | ------ | ---------- | --- | -------- | ------------ | --- | ---- | ------- | -------- | -------- | -------- | -------- | ------- | --- |
| the need | for SR | techniques |     | designed | specifically | for | CPU- |         |          |          |          |          |         |     |
only devices. Recently, NERVE [106] shows great promise copied and stored in a cache for quick retrieval. In order
|                 |     |           |     |           |     |          |       | to reduce | the pressure | on  | backhaul networks |     | and minimize |     |
| --------------- | --- | --------- | --- | --------- | --- | -------- | ----- | --------- | ------------ | --- | ----------------- | --- | ------------ | --- |
| in implementing |     | real-time | VSR | on mobile |     | devices. | Other |           |              |     |                   |     |              |     |
techniques are also proposed to make SR more accessible delay, copies of video content are cached at edge servers to
for computationally-constrained devices, such as early-exit bringthemclosertotheenduser.However,edgeservershave
|         |        |       |        |             |            |     |       | limited storage | capabilities. |     | Cached content | must | therefore |     |
| ------- | ------ | ----- | ------ | ----------- | ---------- | --- | ----- | --------------- | ------------- | --- | -------------- | ---- | --------- | --- |
| schemes | [107], | which | enable | the dynamic | adaptation |     | of SR |                 |               |     |                |      |           |     |
network depth based on available computational resources, be selected correctlyto ensure that only popular videosthat
andpeer-to-peer(P2P)approaches,suchasthatproposedby arelikelytoberequestedbymanyusersarecachedinorder
OASIS [108]. In OASIS, user devices share the computa- tomaximizebandwidthefficiency.
tionalloadofvideoenhancement.OASIS’algorithmjointly Cachingschemescanbeclassifiedintotwotypes:reactive
|         |           |         |     |          |     |          |      | and proactive. | Traditional |     | reactive caching | schemes |     | select |
| ------- | --------- | ------- | --- | -------- | --- | -------- | ---- | -------------- | ----------- | --- | ---------------- | ------- | --- | ------ |
| selects | the video | bitrate | and | SR model | to  | be used, | then |                |             |     |                  |         |     |        |
each device is assigned SR tasks. Once video chunks are cachedcontentbasedononlylocalhistoricrequestpatterns.
successfullyenhanced,theycanbesharedwithotherdevices, For example, the Least Recently Used (LRU) caching tech-
niquereplacescachedcontentthathasnotbeenrequestedfor
thusimprovingtheQoEwithoutadditionalcomputation.
Alternatively,recentresearch[109],[110]suggeststheuse thelongesttimeoncetheserverreachesitsstoragecapacity,
whichmightleadtocachingunpopularcontentjustbecause
ofimageenhancementmodelsthattargetartifacts,noise,and
compression losses rather than upscaling resolution. [109] it has recently received requests. Another reactive caching
compares the performance of image enhancement and SR scheme is the Least Frequently Used (LFU) scheme, which
|             |         |      |             |       |             |     |     | selects cached | content | based | on the | number | of requests. |     |
| ----------- | ------- | ---- | ----------- | ----- | ----------- | --- | --- | -------------- | ------- | ----- | ------ | ------ | ------------ | --- |
| techniques, | finding | that | client-side | image | enhancement |     | im- |                |         |       |        |        |              |     |
proves the PSNR and reduces computation time compared This can also lead to caching of content that is no longer
|        |       |              |     |           |      |          |     | popular | just because | it has | been highly | requested |     | in the |
| ------ | ----- | ------------ | --- | --------- | ---- | -------- | --- | ------- | ------------ | ------ | ----------- | --------- | --- | ------ |
| to SR. | Thus, | such methods |     | may prove | more | suitable | for |         |              |        |             |           |     |        |
streamingondeviceswithlimitedcomputationalcapabilities. past. Therefore, while reactive caching schemes are easy
Moreover, enhancement-unaware ABR frameworks to implement, they often lead to resource wastage due to
|         |         |           |     |                 |     |           |     | their inability | to predict | future | content | popularity. | Proactive |     |
| ------- | ------- | --------- | --- | --------------- | --- | --------- | --- | --------------- | ---------- | ------ | ------- | ----------- | --------- | --- |
| present | another | challenge |     | for SR-assisted |     | streaming |     |                 |            |        |         |             |           |     |
schemes. Most of the current literature designs VSR mod- caching techniques, on the other hand, predict the future
els independently from the ABR algorithm, where video popularityofvideocontentbasedonseveraltypesoffeatures,
enhancement is not accounted for during bitrate selection. asshowninFig.5,thustradingoffeaseofimplementationfor
This results in wasted bandwidth, as ABR algorithms may increased cache “hit rate”, which refers to the rate at which
videocontentissuccessfullyretrievedfromthecacherather
| request | chunks | with | unnecessarily | high | bitrates | when | SR  |     |     |     |     |     |     |     |
| ------- | ------ | ---- | ------------- | ---- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
resources are available. Therefore, integration of SR or thantheoriginserver.Awealthofresearchisdevotedtothe
image enhancement with ABR algorithms is essential and useoflearningtechniquesforpredictionofpopularcontent.
hasrecentlyreceivedmoreattentioninresearch[83],[102],
| VOLUME4,2016 |     |     |     |     |     |     |     |     |     |     |     |     |     | 11  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
The authors of [119] propose one such multi-agent DRL
framework for edge caching. Since one policy cannot be
shared across edges, the authors model each edge as an
RL agent. This approach also benefits from cooperation
between neighboring edges, which have similar content, so
filesthatarenotcachedatoneedgearelikelytobeavailable
at a neighboring edge cache. Another interesting work is
presented by Zeng et al. [120], which proposes a caching
algorithm that uses users’ spatio-temporal context to track
contentdemand.
However,whileusingspatio-temporalcontextaddsavalu-
able dimension to caching decisions, accurately tracking
user mobility patterns requires access to real-time location
data,whichraisespotentialconcernsaboutprivacyanddata
security. Moreover, processing and analyzing such spatio-
temporaldatacanbecomputationallyintensive,particularly
FIGURE5. Popularityfeaturesusedincachingmechanisms.
given the recent surge in video streaming traffic. As the
numberofviewersandvideorequestsgrows,thedatasentto
train the caching algorithm also increases correspondingly,
1) Cachingbasedontemporalfeatures
requiring powerful hardware at the edge, which may not
Intuitively, the most obvious method of predicting content
alwaysbefeasible.Thesechallengesareaddressedin[121],
popularityisthroughtheuseofhistoricalstreamingpatterns.
which uses federated learning to shift training toward end-
Based on past popularity statistics, the future popularity of
user devices then aggregates the trained parameters at the
video content can be predicted using learning techniques.
server. In addition to reducing the computational strain on
Some of the most popular learning methods used for this
edge servers, this approach inherently enhances privacy, as
task include long short-term memory (LSTM) [115] and
raw user data remains on local devices, and only the model
clusteringalgorithmsfortime-evolvingengagementmetrics,
updates are shared with the server. Federated learning thus
suchask-meansandcanopyclustering[116].Alternatively,a
provides a promising solution to scalability and privacy is-
deeplearningapproachisdescribedin[117],whereLietal.
suesincachingframeworks.
propose a dueling DQL-based caching scheme to maximize
energy efficiency. Their proposed scheme makes use of re-
3) Cachingbasedonusersimilarity
currentneuralnetworks(RNNs)toextractinformationabout
Other caching approaches use collaborative filtering [122]–
popularcontentbasedonuserrequests.
[125].Thistechnique,oftenimplementedinrecommendation
Onedrawbackofthiscachingtechniqueisthatitassumes
systems, uses the similarity between users to filter items. In
thatfuturepopularitytrendscloselyresemblepastbehavior.
thecontextofvideocaching,thesimilaritybetweenviewers
However, the use of historical trends alone might overlook
can be used to determine the likelihood that a user will
emerging user demographics and new viral content. To ad-
request a specific video content. Content that is likely to be
dress this, Mao et al. present a caching scheme that uses
highlyrequestedbymanyusersisthendeemedtobepopular
online reinforcement learning [118] and re-initializes the
andcanbecachedproactively.In[123],thehistoricalrequest
RL agent at regular intervals. Meta-learning is then utilized
patternsofauseraswellasrequestpatternsofsimilarusers
to reduce the convergence time. Mistakes and suboptimal
are used to predict the demand for video content. Similarly,
performance can still be seen during the convergence time
the authors in [124] develop a learning-based collaborative
forsuchonlinealgorithms,however.
filteringcachingschemethatselectscachedcontentbasedon
the similarity between users’ content preferences as well as
2) Cachingbasedongeographicfeatures their location. Huang et al. [125] also use a hybrid collabo-
Ontheotherhand,popularcontentvariesnotjusttemporally rativefilteringmodelusingbothspatialandtemporalcontent
but geographically as well. While temporal variations in characteristicstoimprovecachingperformanceinsmallbase
popularity capture how preferences evolve over time, geo- stations.
graphic variations are influenced by factors such as cultural However, while using collaborative filtering can improve
differences,regionalevents,andlocalizeduserinterests.For cache hit rate, it raises some privacy concerns as it heavily
example,sportshighlightsofalocaleventmayreceivehigh relies on user data. In addition, it suffers from cold start
demand in a specific region but very limited interest else- problems when it comes to new content or new users that
where.Thisshowstheneedforcachingtechniquesthatadapt do not yet have any data. Therefore, implementing caching
toregionaldemandpatterns. schemesthatrelyentirelyoncollaborativefilteringmaylead
To address this aspect, researchers have proposed the use tosub-optimalperformance.
ofcachingframeworksthatintegrategeographicinformation.
12 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
4) Cachingbasedoncontentsimilarity live content caching. For example, live video viewership is
Asimilarapproachthataddressesthechallengeofpredicting oftenhighlyvolatile,withsomestreamsexperiencingsudden
the popularity of newly published videos uses content simi- spikes in demand due to viral moments or external events.
larityratherthanusersimilarity.Sincemostcachingschemes Conventional caching methods can struggle to effectively
use historical request patterns to predict the future demand anticipateandreacttothesefluctuations,leadingtoincreased
forvideocontent,newvideosareoftennotcachedefficiently. latency.
Toaddressthelackofhistoricalrequestdatafornewvideos,
the authors in [126] develop an extreme learning machine- IV. QUALITYADAPTATION
based scheme that uses video content features, such as the Video segments in HAS are encoded at multiple quality
title, tags, or number of channel subscribers, for popular levels, so the video quality can be quickly adapted to re-
content prediction. Similarly, Doan et al. [127] use a deep- flect the changing network conditions. Quality adaptation
learning approach to extract the content features from the is carried out to adaptively select the quality level of each
raw video data. The new video’s popularity is then deter- video segment based on a set of decision parameters us-
mined by studying the similarity between its features and ing an adaptation algorithm. ML-based ABR algorithms
thoseofpublishedvideos.Thesemethodsareabletopredict use learning techniques to predict the optimal quality level
the popularity of new content while avoiding the cold start given a QoE model. This section provides an overview of
problemaswellasinvasionofusers’privacyandtheuseof the different QoE models and corresponding learning-based
theirinformation. ABRalgorithmsintroducedintheliterature.ABRalgorithms
However, video content features alone are often not in- are classified based on their application, and Table 4 com-
dicativeofpopularity;videoswithsimilarfeaturescanhave paresnotableML-basedABRalgorithms,highlightingtheir
vastly different engagement levels due to unpredictable fac- design considerations such as multi-user fairness, content-
tors like virality, trends, or external promotion. In addition, awareness, latency,energy-efficiency, andthe learningtech-
extracting video content features, as in [127], can require niquestheyadopt.
significant computational resources, which may make this
approach impractical for large-scale, real-time implementa- A. QOEMODELINGANDPREDICTION
tion. AsexplainedinSectionI-A,QoEmodelsareusedtoquantify
viewer streaming experience. Real-time QoE measurement
5) Cachingforlivescenarios depends on a set of QoE metrics, such as re-buffering fre-
Another application of learning techniques for traffic opti- quency, smoothness, and average quality. These metrics are
mization through caching involves live streaming, a rapidly measured and updated as the video session progresses, and
growingsectorthatimposessignificantbandwidthdemands. theresultingQoEiscalculatedateachtimestep.Inlearning-
Live streaming introduces several new problems to the basedABRschemes,themeasuredQoEisthenusedtoguide
cachingprocess;beinglatency-sensitive,livestreamsrequire the ABR algorithm. Since the user’s experience depends on
continuousupdatesandrapidcachereplacement,increasing the accuracy of QoE measurements, several works leverage
thecomputationaloverhead.Moreover,Lietal.[128]study learningtechniquestopredictQoEmoreaccurately.
mobile live streaming behaviors and statistics and conclude Somerecentworksaredevotedtoutilizingmachinelearn-
that a large percentage of live video traffic is caused by ing [145]–[147] and neural networks [148]–[150] to predict
redundant uploads with no viewers. Additionally, they find the QoE and provide a more accurate representation of the
that live viewers tend to belong to the same locality with a viewer’sperceivedexperience.Learningtechniquesarepar-
group of loyal viewers that download the most video data. ticularly suited for this aspect of video streaming, as real-
Therefore, to reduce the bandwidth wastage, the authors time, objective QoE modeling presents a major challenge,
proposeEDGEOPT,whichreducestheencodingrateofno- with several complex and interrelated factors that impact
viewer, unattractive uploads and uses learning-based pre- users’ subjective experience. Machine learning has shown
fetching to cache the content of popular streams in each re- impressive performance in mapping out the relationships
gion.Theyalsodesignapeer-assistedvideodeliveryscheme between these factors and closely predicting the QoE com-
that takes advantage of loyal viewers who tend to watch pared to subjective measures. More advanced techniques
streams for the longest duration and with greater regularity. are also being researched, such as QoE forecasting, which
Incasetheedgeserverisfacinghightraffic,thevideocontent predicts the future QoE in order to avoid the likelihood of
downloadedbyloyalviewerscanthenbesharedacrossother QoE degradation and give the ABR algorithm more time to
viewers within the same region, thus reducing the server restore the QoE to acceptable levels. One such interesting
load.Livestreaming-relatedtrafficisalsoaddressedbyMaet implementationispresentedbyDinakietal.in[151].Com-
al. [129], leveraging edge computing to aggregate client pared to other QoE prediction schemes that use measured
requests for the same video. By processing these requests QoE metrics that may be outdated by the time the ABR
at the edge, their approach reduces redundant transmissions algorithmreacts,Dinakietal.’sforecastingschemeimproves
and optimizes delivery efficiency. However, many of these the prediction accuracy through the use of bidirectional
workshaveyettoaddressseveralchallengesassociatedwith LSTMs(BiLSTMs).BiLSTMsextractthebidirectionaltem-
VOLUME4,2016 13
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
TABLE2. Datasetsforvideostreamingresearch.
Application Dataset Description
[130] AVCandHEVCUHDcontentfrom3videosequences.
[131] AVCHDcontentfrom6videosequences.
Encoding [132] AVC,HEVC,VP9,andAV1UHDcontentfrom10videosequences.
[133] AVCandHEVCHDcontentfrom23videosequences.
VideoSet[134] JND-basedAVCcodedHDcontent.
Subjectiveopinionscoresfor
NetflixPublicDataset[135]
videocontentacrossmultipleresolutions.
Video LIVE-NFLX-II[136] Subjectiveopinionscoresfor420videos.
qualityassessment KoNViD-1k[137] Large-scaleVQAdatasetwith1200videos.
AVT-VQDB-UHD-1[138] UHDVQAdataset.
Youtube-UGC[139] VQAdatasetforuser-generatedcontent.
High-qualitytripletsofvideoframesforinterpolation,
Vimeo-90K[140]
Super-resolution videodenoising,andvideosuper-resolution.
REDS[141] Videodatasetfordeblurringandsuper-resolution.
Oboe[142] TracesfromWiFi,3G,and4Gnetworks.
4G/LTEnetworktracescollectedinBelgiumacross
Belgium[143]
Networktraces differenttypesoftransportation(foot,bicycle,bus,tram,train,andcar).
4GnetworktracescollectedinIrelandacross
UCC[144]
differenttypesoftransportation(static,pedestrian,car,bus,andtrain).
poraldependenciesoftheQoEmetricsratherthanonlyusing volatility, as well as video content features extracted using
past information for prediction, thus increasing the model’s 3D CNN and LSTM. The authors study the effects of each
accuracy. However, few works have focused on predicting of these factors on the accuracy of QoE prediction and find
QoE beyond the current time step despite its potential to thattheaccuracyishighestwhenamodelcombiningallfour
improveABRdecision-making. factors is used. However, due to the deep spatial-temporal
QoE degradation can also occur due to the misclassifica- featureextractionandregressionmodel,theirmodelishighly
tion of user actions (such as pausing) as streaming events complex.
(suchasre-buffering).Casasetal.addressthisintheirwork Other QoE prediction methods attempt to use Quality-
on DeepCrypt [152], which is a deep learning model for of-Service (QoS) metrics to predict the QoE. Mustafa et
QoEpredictionthatprovidesinsightintouseractionsthrough al.[157]designanABRalgorithm-agnostic,ML-basedQoE
networktrafficanalysis;itdifferentiatesbetweenuseractions predictionschemebasedonQoSmetrics,suchasround-trip
and streaming events with an accuracy of above 80%. In time (RTT), number of packets per segment, and through-
another work [153], the authors use decision tree classifier put. Decision tree regression (DTR), multi-linear regression
forinferenceofQoEmetricsfromencryptedvideostreams. (MLR),andrandomforestregression(RFR)arecomparedin
AnalternativeapproachispresentedinExQoE[154].Rather terms of prediction accuracy, and RFR is found to have the
than using objective metrics for QoE prediction, such as highestQoEpredictionaccuracy.Anotherapproachin[158]
re-buffering duration and average bitrate, ExQoE models usesaduelingDQN,whichseparatesthestatevaluefunction
QoEbasedonusers’exitingbehaviorandmodelstheuser’s and action advantage function. The adaptation algorithm is
exiting probability based on the video stalling occurrences. carried out from the MEC server, where the transmission
The QoE model is then used to guide the selection of an bandwidthandthebufferoccupancyaretracked.Thevideois
appropriateCDNandresolutionusingRL. then transcoded at the edge server at the quality determined
Other research focuses on developing QoE models that bytheadaptationalgorithm.
more accurately reflect the characteristics of video content. Also related to QoE modeling, video quality assessment
Althoughmostoftheliteratureusesbitrateasaqualitymea- (VQA)isanessentialaspectthatmeasuresthevideostream-
sure, bitrate alone cannot be used as a visual quality metric ingquality.Assuch,itplaysanimportantroleinQoEmea-
duetothediversityofchunkcomplexity.In[155],theauthors surement and ABR model evaluation. Conventional VQA
investigate the relationship between chunk complexity and methods evaluate the video quality with reference to a cer-
quality. They find that most ABR algorithms do not select tain ground truth, typically uncompressed video. These are
sufficiently high bitrates for complex or dynamic chunks, known as full-reference (FR) methods, the most popular of
although achieving higher quality for dynamic chunks than whicharethePSNR,SSIM,andVMAFmetrics.Intuitively,
static ones leads to greater QoE gains. To handle this issue, these methods, while effective, are not suitable for cases
theydesignDAVS,aquality-awareapprenticeshiplearning- in which a reference video is unavailable, which inspired
based(refertoTable1fordefinitionsoflearningtechniques) the development of other VQA methods that use reduced
schemewithamodifiedQoEfunctionthattakeschunkcom- reference or no reference. Reduced-reference VQA (RR-
plexityintoaccount,aswellasusers’QoEpreferences.[156] VQA) methods use partial information from the reference
alsopresentsacontent-awareQoEmetrictoguidetheclient’s video,suchasextractedfeatures,ratherthanthefulloriginal.
bitrate selection, based on video quality, playback fluency, They aim to reduce the amount of required data while still
14 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
maintaining a level of accuracy. Several such methods have among others. These algorithms are generally evaluated
been proposed in recent works. [159] develops a RR-VQA based on achieved visual quality (indicated by metrics such
scheme that uses an LSTM model to predict the VMAF for asVMAF)andoverallQoE,withrespecttoasetofbaseline
multi-stage transcoded videos based on DCT-energy-based ABRmodels.Thereareseveralcommonmodelsusedinthe
features.Similarly,VQ-TIF[160]isanotherRR-VQAalgo- literatureasabenchmark,includingconventional[13]–[15],
rithmthatusesLSTMsforqualitypredictionbasedonfused [169] and learning-based methods [16], [17]. Table 3 also
SSIMandspatiotemporalfeatures.No-referenceVQA(NR- provides a list of tools and frameworks available for video
VQA)methods,ontheotherhand,donotrequireareference streaming research, particularly in the field of ML. Other
video at all. They estimate the quality of the video based usefultoolsthatarenotspecifictoML-basedstreaming(e.g.,
on its own content, usually by learning patterns that predict dash.js [170], Mahimahi network emulator [171], FFmpeg
perceptual quality, making them more suitable for real-time [36], DASHEncoder [131]) are not included. Note that the
applications. The P.1204.3 quality metric [161] is one such toolslistedinthetablearegenerallycustomizable,allowing
bitstream-based NR-VQA method that comprises a para- researcherstotailorthemtospecificdeploymentgoals.
metriccomponent(whichusesdegradation-basedmodeling) CurrentliteratureonABRstreamingoverwhelminglyfea-
andMLcomponent(whichusesrandomforestregressionto turesRL-basedimplementations.Inaninterestingworkuti-
account for the video spatio-temporal features). Other ML- lizingDRL[172],Muetal.presentAMIS,anedge-assisted
basedNR-VQAmethodsarealsosuggestedintheliterature ABRschemethatcombinesbitrateandplaybackspeedadap-
[162],particularlyforuser-generatedcontent(UGC),suchas tation. Since changes in the playback rate are less notice-
[163]whichproposesthatsemanticvideoinformationplays able for highly dynamic scenes, AMIS analyzes the SSIM
aroleinvideoqualityassessment.Similarly,theVIDEVAL betweentheframesofeachsegmenttodeterminethenature
[164]andRAPIQUE[165]modelshaverecentlybeendevel- ofeachsegmentandtheextenttowhichplaybackspeedcan
opedforNR-VQAofUGC. bealteredimperceptibly.Furthermore,[173]suggesttheuse
The approaches described above greatly enhance the ac- ofLSTM-CNN-basedRLforbitrateadaptation,withLSTM
curacy of QoE prediction compared to heuristic methods, to replace the 1D-CNN input layer to better extract infor-
andconsequently,thequalityadaptationprocessisimproved. mation from the sequential inputs, such as past throughput
However,itisimportanttonotethatlearningtechniquesoften and segment download rates. Feng et al. [174] also use an
have greater computational complexity and overhead. In an RL-basedschemewithproximalpolicyoptimization(PPO),
end-to-end streaming system, this complexity becomes an whichisanalgorithmthatlimitsthechangestothepolicyand
even greater concern. Consider only the client side; it may reduces the difference between the old and updated policy,
comprise several components, including but not limited to thusimprovingthestabilityoftraining.Theauthorsin[175]
throughput prediction, QoE prediction, video content anal- designaDRLalgorithmtoimproveQoEinhighlydynamic
ysis, quality adaptation, and quality enhancement modules. networkenvironmentsusingdualPPO.
As such, it is essential to consider the complexity of these Similarly, deep Q-learning is a branch of DRL which
algorithms holistically, rather than as separate components, is also commonly used in the literature for quality adap-
sincemanyend-userdevicesmaynotbecapableofhandling tation [176]–[178]. In conventional Q-learning, state-action
the computational load of all these tasks simultaneously, pairs are stored in a tabular format, along with their associ-
shouldtheybetoocomplex.Thisaspectmustbeconsidered ated Q-values (see Table 1). DQL, on the other hand, uses
when analyzing the practicality of learning-based schemes a neural network to estimate the Q-values instead, making
for the different modules of video streaming, particularly it more suitable for scenarios with large state and action
thosethatutilizedeepneuralnetworkarchitectures. spaces. The advantage of DQL over other RL schemes lies
initsuseofexperiencereplay,inwhichtheneuralnetwork’s
B. QOEOPTIMIZATIONFORVOD pastexperienceisstoredwithinareplaymemory.Thereplay
Reinforcement learning techniques are used predominantly memoryisthensampledatrandomfortrainingtoeliminate
for adaptive bitrate selection. In a reinforcement learning- thecorrelationbetweenconsecutivesamples.Onedisadvan-
based scheme, video streaming is modeled as a Markov tageofDQLapproaches,however,istheirtendencytoover-
Decision Process (MDP), in which an agent learns to select estimatetheQ-value.Tomitigatethisissue,[179]implement
thebestpossibleaction(i.e.,thebitrateorqualitylevel)given DQNReg-basedrateadaptation.DQNRegisamodifiedDQL
acertainstate(i.e.,environmentalfactors,suchasbandwidth modelthatavoidsoverestimationoftheQ-valuebyaddinga
availability). The RL agent then learns a policy by which it weighted penalty to the model’s loss function. As a result,
decideswhichactionswillhavethemostfavorableoutcome, DQNReg achieves faster convergence and higher QoE than
as determined by the QoE. During training, this policy is conventionalDQL.
updated with each new experience learned by the agent. A InordertoimprovetheQoE,otherworksattempttoaccu-
variety of RL-based ABR techniques have been developed rately predict ABR decision parameters, such as bandwidth
recently, particularly for VoD streaming, for several appli- [74],[180]–[182].Thebandwidthistypicallyoneofthemost
cations, such as conventional VoD streaming [166], energy- essential factors in determining the bitrate level of the next
aware streaming [167], and short video streaming [168], segment. In the literature, LSTM networks are commonly
VOLUME4,2016 15
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
used for throughput prediction [183]. In [7], Yoo et al. proposestheuseofedgeresourcestoconcurrentlyimplement
compare the performance of five machine learning models video chunk transmission and transcoding, thus reducing
inbandwidthpredictionforDASHandfindthatLSTMnet- delay [189]. Other computationally intensive tasks are also
worksprovidethemostaccurateprediction.However,despite suggested to be implemented at the edge server, such as
being relatively the most accurate, their LSTM model still quality enhancement and super-resolution [83], [96], [101],
hasahighpredictionerror.Inaccuratethroughputprediction asdiscussedinSectionIII.
can cause ABR algorithms to incorrectly select high video
bitrates,resultinginvideostalling.In[8],theauthorstackle C. MODELGENERALIZABILITY
this issue. They utilize a Bayesian neural network (BNN) Despite impressive performance shown by learning-based
topredictthethroughputwhiletakingthealeatoric(relating ABR algorithms in the literature, in reality, ensuring that a
to the model output) and epistemic (relating to the model modelperformsconsistentlyacrossdiversenetworkenviron-
weights)uncertaintyintoaccount.Basedonthisuncertainty, mentsremainsasignificantchallenge.WhileheuristicABR
the authors build a confidence region for the throughput algorithmscanshowrobustbehaviorinunseenenvironments
prediction and implement an uncertainty-aware scheme that due to their deterministic nature, learning-based algorithms
maximizestheworst-caseQoEaccordingly. often struggle to generalize. This is mainly because RL
Furthermore, [9] presents Yuan et al.’s design of an models are trained within specific environments in which
attention-based throughput forecasting model, GCA, which overfittingmayoccur.Inmachinelearning,overfittingoccurs
usesagatedrecurrentunit,convolutionalneuralnetwork,and when models learn specific patterns in the training data too
attention mechanism to improve the future throughput pre- well, leading to performance degradation when faced with
diction.TheauthorsthendevelopPRIOR,amulti-agentDRL new, unseen conditions outside their training distribution.
network for bitrate adaptation, and show that using the pre- Consequently, improving the generalizability of learning-
dictedthroughputmeasurementratherthanhistoricthrough- based ABR algorithms is a critical area of research that is
put records improves QoE. Another recent work presents beingtackledusingavarietyoftechniques.
Xatu[184],aneuralnetwork-basedschemethatimprovesthe While offline learning algorithms may perform well in
prediction accuracy for the download rate of video chunks. environments included in their training, their performance
Xatuincludesnotonlythroughputbutalsotemporalfeatures, rapidly declines in new environments. In RL-based ABR,
such as Time to First Byte (TTFB), in chunk download rate once the network environment changes, the offline neural
estimation. Based on their results, the authors confirm that networkmustbere-trainedonceagain.TheproblemofQoE
theuseoftemporalfeaturesasidefromthroughputimproves degradation in learning-based ABR algorithms is addressed
prediction accuracy. In contrast, EnDASH [185] uses ran- inseveralworksusingonlinelearningmethods.Forexample,
dom forest algorithm to predict the throughput, followed the authors in [193] suggest using online RL to update the
by quality adaptation using DRL, for a less complex and neural network in real time if the QoE drops below a pre-
computationallyintensiveapproachtothroughputprediction. defined threshold. ABRaider [194] is another approach that
The use of learning techniques in these works can signifi- combinesofflineandonlinetrainingtobalancegeneralizabil-
cantly reduce the chance of rebuffering as ABR algorithms ityandadaptability.Initsofflinephase,ageneralizedneural
can predict changes in network throughput in advance and networklearnstoselectoneoffiveexistingABRalgorithms
reactaccordingly.However,itisimportanttonotethatsuch based on expected rewards, while its online phase tunes
approaches suffer from inaccurate predictions in the case the model on client-specific data, resulting in a specialized
ofextremelyunstablenetworkconditions.Thisisaddressed modelforeachclient.However,whilethistwo-stagetraining
in [182], which suggests the use of transfer learning to improvesABRaider’sadaptability,itincreasescomputational
tacklethehighlyvariablenatureofnetworkbandwidth.The overhead on the client side. Similarly, some works [195],
authorsalsodesignastreamingactivitymonitortotrackthe [196] train RL models on pre-classified network environ-
network conditions during OFF periods in which the client ments, based on features such as bandwidth, undergoing
doesnotdownloadvideosegments.Thisway,thethroughput additional online training in new network environments to
can be more accurately predicted based on actual network avoidQoEdegradation.
conditionsratherthanpastsamplescalculatedduringtheON However, although online learning provides benefits in
period. DeX [186], on the other hand, tackles the issue of terms of generalization and adaptability, it is important to
unstablebandwidthdifferently;itleveragesdeeplearningfor note that continuous training is required, leading to much
short-termthroughputprediction,withafocusonpredicting higher processing demands. In most cases, the ABR algo-
extremeorsuddennetworkconditions. rithmisdeployedontheclientdevice,makingthesecompu-
A range of edge-assisted ABR schemes is also proposed tationaldemandsinfeasibleforlow-enddevices.Inaddition,
intheliterature[187],[188].Edge-assistedstreamingbrings constantonlineupdatescandestabilizethemodel,especially
content to edge servers, close to the client’s end. As such, ifshort-termfluctuationsareoveremphasized.
itprovidesmuchquickerdelivery,aswellashighercapabil- Beyondonlinelearning,otherschemesarealsousedacross
ities for tasks that end-user devices may not be capable of the literature to improve the generalizability of ABR al-
carrying out. Taking advantage of this, recent research now gorithms through innovative learning methods. For exam-
16 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
TABLE3. ToolsandapplicationsforML-basedvideostreamingresearch.
|     | Application |     | Tool |     | Description      |     |                             | Evaluationmetrics |     |
| --- | ----------- | --- | ---- | --- | ---------------- | --- | --------------------------- | ----------------- | --- |
|     |             |     |      |     | Algorithmlibrary |     | PSNR,MS-SSIM,executiontime, |                   |     |
OpenDMC[31]
|     |     |     |     | fordeeplearning-basedvideocoding. |     |     |     | GPUmemoryoccupancy |     |
| --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ------------------ | --- |
Videoencoding
|     |     |     |     | Trainingandevaluatingend-to-endneural |     |     | PSNR,MS-SSIM,bitrate,rate-distortion |     |     |
| --- | --- | --- | --- | ------------------------------------- | --- | --- | ------------------------------------ | --- | --- |
CompressAI[190]
|     |                  |              |     | imageandvideocompressionmodels. |                        |     |                                            | curves,executiontime     |     |
| --- | ---------------- | ------------ | --- | ------------------------------- | ---------------------- | --- | ------------------------------------------ | ------------------------ | --- |
|     | Videoenhancement |              |     |                                 | Evaluatingvideoquality |     |                                            |                          |     |
|     |                  | MoViDNN[114] |     |                                 | enhancementmodels.     |     |                                            | PSNR,SSIM,processingtime |     |
|     |                  |              |     |                                 | Testing,analyzing,and  |     | Videoquality(bitrate),stalling,framedelay, |                          |     |
Arsenal[191] comparinglearning-basedABR fairness(Jain’sfairnessindex),packetlossrate,
ABR schemesforlivestreaming. receivingthroughput,transmissiondelay
|     |     |     |     |     | Trainingandevaluation |     | Videoquality(VMAF),audioquality |     |     |
| --- | --- | --- | --- | --- | --------------------- | --- | ------------------------------- | --- | --- |
OpenNetLab[192] ofRL-basedABRschemes. (DNSMOS),delay,receiverate,loss
ple, the authors in [197] implement Genet, a curriculum RL with a two-phase training process, leveraging domain
learning-based framework (refer to Table 1) to improve the knowledgetoimproveadaptabilitytoclient-specificnetwork
performance of RL algorithms in new environments. Genet conditions.However,despitetheiradvantages,meta-learning
uses rule-based algorithms as a baseline, taking advantage approaches often require large training datasets and compu-
of the fact that they generally show stable performance, tationalresources,whichpresentsabarriertotheirpractical
| eveninunseenenvironments.Theperformancegapbetween |     |     |     |     |     | deployment. |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
the RL and rule-based algorithms is then used to deter- Federated learning is another recent promising solution
mine which environments are rewarding, helping the RL for ABR generalizability. It differs from meta-learning in
models achieve improved generalization. Another strategy its focus; meta-learning aims to improve a model’s ability
is proposed in [198], which utilizes a hybrid framework to quickly adapt to new tasks or environments by leverag-
thatincludesmultiplebitrateadaptationmethodsandselects ing knowledge from previous tasks. Federated learning, on
the one that will result in the highest QoE at each seg- the other hand, trains models across distributed devices or
| ment | boundary. The method | pool | consists | of  | a bandwidth- |     |     |     |     |
| ---- | -------------------- | ---- | -------- | --- | ------------ | --- | --- | --- | --- |
clientswithoutcentralizingdatatoensuredataprivacy.This
based, PD-controller based, and RL-based method. While is demonstrated in FedABR [202], which trains a global
thisapproachachieveshighrewards,itsuffersfromunstable modelacrossmultipleclientswithoutsharingrawdata,thus
bufferoccupancy.Suchalgorithmsthatcombinetheoutputs ensuring privacy and allowing the creation of personalized
of several ABR models during quality adaptation [194], models for each client. However, federated learning has its
| [198] | are able to take | advantage | of the | strengths | of each |                  |          |                         |         |
| ----- | ---------------- | --------- | ------ | --------- | ------- | ---------------- | -------- | ----------------------- | ------- |
|       |                  |           |        |           |         | own limitations. | Although | this approach addresses | privacy |
model while avoiding their weakness. On the other hand, concerns and computational bottlenecks at servers, it relies
runningseveralABRalgorithmssimultaneouslycanincrease ontheavailabilityofsufficientcomputationalpoweronend-
processing requirements, making it essential to consider the user devices, which is not always guaranteed. Moreover,
computational complexity of each model included in the federatedlearningprimarilyfocusesonlearningasingletask
methodpooltoavoidexcessivelyhighcomplexityorlatency. and produces a common global model. In contrast, meta-
Selecting a different ABR approach for each segment may learning can better adapt to heterogeneity, which makes it
alsoleadtoinconsistentbitratebehavior. more suitable in scenarios where personalization is neces-
| Additionally, | many       | recent works      | take | advantage | of meta- | sary. |     |     |     |
| ------------- | ---------- | ----------------- | ---- | --------- | -------- | ----- | --- | --- | --- |
| learning      | to improve | generalizability. |      | The use   | of meta- |       |     |     |     |
learning allows the RL model to transfer knowledge across D. QOEFAIRNESS
different tasks, so that previous knowledge learned can be The aforementioned QoE improvement methods are limited
usedfornewtasks.Toillustratethisconcept,MetaABR[199] inthattheyeachattempttoimprovetheQoEofasingleclient
is a meta-learning, RL-based framework for ABR selection rather than providing a fair QoE and bandwidth distribution
with several actors and a meta-critic that supervises and toseveralcompetingclientssharinganetwork.Totacklethis
evaluates their actions. The meta-critic learns a high-level issue, learning techniques are increasingly being leveraged
policybasedontransferredknowledge.Therefore,MetaABR to simultaneously optimize individual QoE and global QoE
can adapt to different unseen environments and converge fairness.Fig.6showsanexampleofamulti-userstreaming
much faster than other learning-based algorithms. In [200], system with a single server delivering content to multiple
Huo et al. also propose a meta-learning-based scheme for clients. Following a similar framework, Yuan et al. [203]
QoEoptimizationandpersonalizationthatlearnstheindivid- suggest a client-server collaborative framework, Multi-User
ual QoE preferences of each user. A master policy learns to Adaptive Bit-Rate (MUABR), to improve QoE for all users
select one out of at least three DRL sub-policies for quality in multi-user video streaming. In MUABR, each client is
adaptationbasedonuserpreference.Inthisframework,meta- consideredanindependentRLagent.Theclient’sRL-based
learningisusedtotransferknowledgeacrossallsub-policies ABR algorithm determines the bitrate of the next video
and speed up training. Similarly, A2BR [201] uses meta- segment, as well as the urgency of the client’s need for
| VOLUME4,2016 |     |     |     |     |     |     |     |     | 17  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
FIGURE6. Multi-userframework.
bandwidth allocation, based on factors such as the buffer sideactor-criticRLtooptimizeQoEthroughresolutionand
occupancy and previous segment size. On the server side, playbackspeedadaptation,andaresourceallocationmodule,
bandwidthallocationisdeterminedbyeachclient’surgency whichusesthevaluefunctionoutputofthecriticnetworkto
and the likelihood of rebuffering. Clients with low buffer estimate each client’s need for resources. Some approaches
occupancyandsmallerprevioussegmentsizesareallocated also use edge computing to carry out quality adaptation at
more bandwidth, helping to improve the overall average theedgeserver[209]–[212].Theseapproachestypicallyim-
QoEforallusers.AltamimiandShirmohammadi[204]also plementanRLagentattheedgeserver,whereitobservesthe
proposeclient-servercooperationtoensurefairnessbetween globalandindividualclientstatestomakebitratedecisions.
users sharing a bottleneck while maintaining an acceptable However,suchedge-basedapproachesdonottakeadvan-
individualQoE.AnRLagentattheserver-sidespecifiesthe tageofadvancedclientcomputationresources.Whileserver-
maximum allowable bitrate available to each client over a side multi-user algorithms are useful since servers have a
given window of time, while the client carries out the ABR holistic view of all users as well as the network condi-
algorithm.ThegoaloftheRLagentistomaximizeasocial tions, they increase the server load, underutilizing increas-
welfarefunctiontoensurefairQoEallocation[204].In[205], ingly powerful client capabilities. In addition, client-side
Liu et al. propose a federated learning-based bandwidth algorithmsnaturallyprovidemorepersonalization.However,
allocation scheme that uses a client-side DRL algorithm to the lack of centralized control makes purely client-side al-
selectthechunkbitrateandassignaweightrepresentingthe gorithms less effective at ensuring fairness. Network con-
client’s need for bandwidth, with the server only providing gestion is also difficult to handle proactively using client-
eachDRLagentwithaglobalstatethatcontainsinformation side algorithms, making them far less common in multi-
abouttheQoEofallclients.Similarly,VSiM[206]isanend- user streaming scenarios. Balanced, cooperative approaches
to-end system that dynamically allocates bandwidth using that effectively utilize both server and client resources are
clients’mobilityprofilesandQoEdata.Neuralnetworksare thereforenecessary.
usedtoadaptivelyoptimizethesystemparameters,ensuring
robustnessacrossdifferentnetworkconditions.Suchcollab- E. LIVESTREAMING
orative approaches combine the benefits of both server- and In previous sections, we have generally discussed ABR
client-sideadaptation. algorithms designed for conventional streaming scenarios,
i.e., scenarios that are not latency-sensitive. In this section,
Rather than collaborative client-server approaches, very we now discuss low-latency algorithms for live streaming
few works use purely client-side adaptation for multi-user scenarios. Due to the recent proliferation of live content,
scenarios [207]. On the other hand, many works in the particularly user-generated content, several works look into
literatureutilizeserver-sideadaptationinsteadwhenitcomes QoE prediction and improvement for such scenarios as
to multi-user streaming. For example, Mu et al. build upon well [213]–[215]. Live streaming presents several unique
theirworkonAMIS[172]withAMIS-MU[208].AMIS-MU challenges compared to conventional streaming due to its
consistsofaplaybackadaptationmodule,whichusesserver- stringent requirements for low latency and synchronization.
18 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
Unlike on-demand streaming, where slight buffering delays livevideoqualityassessment.However,theuseofMLtech-
canbeacceptable,livestreamingnecessitatesreal-timedeliv- niques,particularlydeeplearning,remainsachallengeinlive
ery to maintain viewer engagement, particularly in the case scenarios,sothereareyetfewstudiessuggestingitsusefor
of interactive video, which makes ABR algorithms for live QoEprediction,unlikeVoD-focusedresearch.
streaming particularly difficult to design. [191] provides a
comparison of several recent learning-based algorithms for F. CONTENT-AWAREADAPTATION
live streaming across different scenarios, including 3G, 4G, Video content also plays a role in determining users’ QoE.
5G,andWiFienvironments. Much of the recent research is devoted to developing
Since maintaining latency within an acceptable range is adaptation algorithms tailored to viewers’ content prefer-
crucial for ensuring high QoE in live streaming, buffer size ences [231], [230]. In [231], the authors propose an adap-
is a key factor to consider: excessively large buffers in- tationschemethattakesintoaccounttheuser’spreferencein
crease delay, while buffers that are too small might hinder termsofvideoaffective,oremotional,content(e.g.,joy,sad-
the delivery of high-quality segments. This has motivated ness,disgust,surprise,fear,andanger).Deeplearningisused
the development of buffer management techniques, such as tolearntheuser’saffectivecontent(AC)preferencesoffline
TCLiVi[216],whichusesDRLtoadaptivelyselectboththe fromrecentviewinghistory.Bufferingtimeisthenallocated
videobitrateandtargetbuffersize.Inaddition,severalother basedonACrelevancy,sohigheraffectivesegmentsreceive
approaches can also be used to reduce the latency, such as higher quality representations. The work in [227] also uses
frame skipping [217]–[219] and playback speed adaptation content-awareadaptationtoimproveuserQoE.However,in
[219]–[221].Theauthorsin[217]useanRLframeworkfor this work, video content is classified based on scene type
live ABR to reduce live latency by using frame skipping (e.g., dance, news, music, etc.) rather than emotions. The
whenthelatencyrisesaboveaspecifiedthreshold.However, user’sviewinghistoryisusedtodeterminetheirpreferences,
their approach does not guarantee a high QoE, especially and term frequency-inverse document frequency (TF-IDF)
when the available bandwidth is unstable or limited. Simi- is applied to ensure that generally common and frequently
larly, Deeplive [218] is a Double-DQN [222] approach de- occurring scenes are not included in the viewer’s content
signedforlivescenarioswhichusesframeskippingtoreduce preferences.In[230],videocontentfeaturesareextractedby
latency. A quick-start mechanism is also developed to use applying a 3D CNN to 16 frames from each segment. DQL
arate-basedalgorithmratherthanDeeplive’slearning-based is then used for rate adaptation based on the interestingness
algorithm at the start of the video stream, when historical of each video segment. Another recent RL-based work on
stateinformationisnotavailableyet.Ontheotherhand,the content-aware adaptation is presented in [228], which uses
work in [220] proposes a low latency DRL framework for the number of replay times to determine scene importance.
selectingvideoqualityandplaybackspeedforlivestreaming. However, this method is not applicable for newly uploaded
This method maximizes QoE given a live latency target videos as they would not yet have replay information. An
and,ratherthanskippingframes,slightlyvariestheplayback interesting alternative approach proposed by Ye et al. uses
speedtoreducelatency.Alternatively,theapproachin[219] DRL to design a visual sensitivity-aware adaptation algo-
uses actor-critic DRL for live scenarios to combine both rithm[225].
frameskippingandplaybackspeedadaptation. Asidefromsemanticvideocontent,someworksalsofocus
Live video streaming also benefits from peer-to-peer sys- on content complexity. Not all scenes in a video sequence
tems.Recentresearchintroducessuchdecentralizedstream- have the same level of complexity; rather, some scenes are
ingtechniquesinordertoimprovelivestreamquality,reduce highly complex or dynamic (e.g., action scenes), whereas
serverloads,andtacklehighvideotrafficduringliveevents. some are simple or static (e.g., interviews). Although com-
Onenotableworkutilizingthisconceptispresentedin[223], plex scenes have a larger impact on user QoE, they tend to
whichintroducesaP2Psystemforcrowdsourcedlivevideo be requested at lower bitrates by ABR algorithms than less
streaming.Thisschemeleveragesamultiflowframeworkthat complex scenes due to their larger size. Requesting higher
allows multiple parents to transmit redundant video content bitrates for complex scenes would require high bandwidth
to a single child viewer, ensuring uninterrupted playback resources, so conventional ABR algorithms do not favor
evenifsomeparentsleavethesession.ADRL-basedsched- thesescenes.Thisleadstoreducedvisualquality,ascomplex
uler is designed for multiflow transmission to adaptively scenes require higher bitrate levels to achieve acceptable
balanceflowvolumesandoptimizethevideoqualityinreal- quality,whereaslow-complexityscenescanreachanaccept-
time. ablequalityevenwhenrequestedatalowbitratelevel[232],
Given the more stringent latency requirements of live [233]. This issue is addressed in some recent works, which
streaming, accurately predicting the QoE of live videos re- design content complexity-aware adaptation schemes [155],
quires real-time quality assessment with high precision. As [234]–[236].
such, live QoE prediction is another challenge that recent Although using content-aware adaptation improves QoE,
research attempts to address, such as Vega et al.’s [215] requesting user-preferred chunks at a high bitrate might not
design of an unsupervised learning method involving the be possible if they need to be fetched at instants of low
use of Restricted Boltzmann Machines (RBM) for online networkbandwidth.Ratherthanrelyingonanunreliablenet-
VOLUME4,2016 19
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
TABLE4. Comparisonbetweenqualityadaptationschemes.
Multi-
|     |     |        |     |     |        |          |     |     |     | Content- |         | Low- Energy- |       |     |
| --- | --- | ------ | --- | --- | ------ | -------- | --- | --- | --- | -------- | ------- | ------------ | ----- | --- |
|     |     | Papers |     |     | client | Approach |     |     |     |          |         |              |       |     |
|     |     |        |     |     |        |          |     |     |     | aware    | latency |              | aware |     |
fairness
|     |     | [8] |     |     | ×   | Bayesianneuralnetwork |     |     |     | ×   |     | ×   | ×   |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Gatedrecurrentunit(GRU),CNN,
|     |     | [9] |     |     | ×   |     |     |     |     | ×   |     | ×   | ×   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deepreinforcementlearning
|     |     | [129] |     |     | ✓   |     |     |     |     | ×   |     | ✓   | ×   |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[100],[109],[110],[166],[168],
|     | [154],[172]–[175],[193]–[196], |     |     |     | ×   |     |     |     |     | ×   |     | ×   | ×   |     |
| --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[198],[199],[201],[224]
✓
|     |     | [167],[185] |     |     | ×   | Reinforcementlearning |     |     |     | ×   |     | ×   |     |     |
| --- | --- | ----------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[203]–[205],[207],[208],
|     |     |     |     |     | ✓   |     |     |     |     | ×   |     | ×   | ×   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[209]–[212]
|     | [216],[217],[219],[220] |     |     |     | ×   |     |     |     |     | ×   |     | ✓   | ×   |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
✓
|     |     | [81],[225]–[228]  |     |     | ×   |                        |     |     |     |     |     | ×   | ×   |     |
| --- | --- | ----------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | [229]             |     |     | ×   | Supervisedlearning     |     |     |     | ×   |     | ×   | ×   |     |
|     |     |                   |     |     | ×   |                        |     |     |     | ✓   |     | ×   | ×   |     |
|     |     | [155]             |     |     |     | Apprenticeshiplearning |     |     |     |     |     |     |     |     |
|     |     | [158],[176]–[179] |     |     | ×   |                        |     |     |     | ×   |     | ×   | ×   |     |
|     |     | [68]              |     |     | ×   |                        |     |     |     | ×   |     | ×   | ✓   |     |
DeepQ-learning
|     |     | [218] |     |     | ×   |     |     |     |     | ×   |     | ✓   | ×   |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
✓
|     |     | [150],[230] |     |     | ×   |                           |     |     |     |     |     | ×   | ×   |     |
| --- | --- | ----------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | [202]       |     |     | ×   | Federatedlearning         |     |     |     | ×   |     | ×   | ×   |     |
|     |     | [197]       |     |     | ×   | Curriculumlearning        |     |     |     | ×   |     | ×   | ×   |     |
|     |     | [213]       |     |     | ×   | Self-organizingmaps(SOMs) |     |     |     | ×   |     | ✓   | ×   |     |
|     |     | [214]       |     |     | ×   | Gradientascent            |     |     |     | ×   |     | ✓   | ×   |     |
CNN,supportvectormachine(SVM)
|     |     | [231] |     |     | ×   |     |     |     |     | ✓   |     | ×   | ×   |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classifier
workconnection,pre-fetchingcanbeleveragedforpreferred typicallyinvolveslesscomplexdecisionspacescomparedto
chunks, as suggested by HotDASH [226]. HotDASH uses bitrate selection, making supervised learning more feasible.
twocascadedRLnetworks,thefirstofwhichcarriesoutbi- Therandomforestanddecisiontreealgorithmsinparticular
trateselection,whilethesecondnetworkmakesthedecision haveshowngreatpromiseinthisfield.Inthecaseofcaching,
topre-fetchachunkornot.Thismethodensuresthedelivery collaborative filtering and other user-centric methods have
ofcriticalchunksathighbitrates,althoughthecascadedRL inspired the use of clustering algorithms to improve cache
designmayincreasethecomputationalcomplexity. content prediction. In the remainder of this section, we fur-
theranalyzerecenttrendsinML-basedvideostreaming.
V. POSSIBLERESEARCHDIRECTIONS
A. EMERGINGTRENDSANDTECHNOLOGIES
1) Energy-efficientvideoencoding
| Based on | our study, | we  | observe | that | DRL | methods | are |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ------- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
dominantinqualityadaptationresearch,althoughmeta-and
|     |     |     |     |     |     |     |     | Video coding | research | has | increasingly |     | prioritized | energy |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------ | --- | ----------- | ------ |
federated learning are recently also gaining traction. In par- efficiency and computational scalability, shifting from the
| ticular, the | A3C | method has | been | widely | adopted | by  | many |                        |     |           |     |            |         |        |
| ------------ | --- | ---------- | ---- | ------ | ------- | --- | ---- | ---------------------- | --- | --------- | --- | ---------- | ------- | ------ |
|              |     |            |      |        |         |     |      | use of computationally |     | intensive |     | exhaustive | bitrate | ladder |
researchers, following its use in Pensieve [16]. Other RL generation, with a greater focus on ML-based solutions.
algorithms,suchasQ-learning,haveseenlessrecentinterest Particularly, instead of focusing solely on bitrate and reso-
| due to the | greater | success | of methods |     | like A3C | and | PPO |                    |     |          |          |     |           |       |
| ---------- | ------- | ------- | ---------- | --- | -------- | --- | --- | ------------------ | --- | -------- | -------- | --- | --------- | ----- |
|            |         |         |            |     |          |     |     | lution adaptation, |     | emerging | research | now | leverages | ML to |
fordynamicapplicationslikevideostreaming.Contrastingly, dynamically select optimal encoder configurations across a
| we find | limited | use of supervised |     | learning |     | techniques | in  |             |                |     |           |         |         |       |
| ------- | ------- | ----------------- | --- | -------- | --- | ---------- | --- | ----------- | -------------- | --- | --------- | ------- | ------- | ----- |
|         |         |                   |     |          |     |            |     | wider range | of parameters, |     | including | encoder | preset, | frame |
ABRalgorithms,mostlyassignedtotaskslikeQoEinference
|     |     |     |     |     |     |     |     | rate, and | GOP structure. |     | Content- | and | network-aware | en- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | -------- | --- | ------------- | --- |
rather than bitrate selection, which is significantly more coding models have also seen significant interest recently,
complex.However,theresearchondeeplearning-basedlive
|     |     |     |     |     |     |     |     | in order | to provide | further | improvements |     | in  | bandwidth- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | ------------ | --- | --- | ---------- |
streaming is noticeably less substantial. This is because the efficientandperceptualquality.Wealsoobservethatper-title
useofdeeplearningislesseffectiveforlivescenarios,which encoding, previously more prevalent, is now being replaced
| demand | less computationally |     | intensive |     | techniques, | leaving |     |     |     |     |     |     |     |     |
| ------ | -------------------- | --- | --------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
byper-chunkandper-shotencodingapproachesduetotheir
heuristic methods or supervised learning as a possible solu- improved performance in terms of bandwidth utilization.
| tion. Supervised |     | learning | is also | used far | more | extensively |     |          |                 |     |           |         |                |     |
| ---------------- | --- | -------- | ------- | -------- | ---- | ----------- | --- | -------- | --------------- | --- | --------- | ------- | -------------- | --- |
|                  |     |          |         |          |      |             |     | Notably, | such techniques |     | are being | adopted | in commercial- |     |
for bitrate ladder prediction and caching than for quality gradestreamingsystems[57],showingtheirviabilityinreal-
adaptation.Thisismotivatedbythefactthatvideoencoding worlddeployments.
isacomputationallyhungryprocess,callingforlesscomplex
| techniques | to reduce | its energy |     | and time | demands; |     | it also |     |     |     |     |     |              |     |
| ---------- | --------- | ---------- | --- | -------- | -------- | --- | ------- | --- | --- | --- | --- | --- | ------------ | --- |
| 20         |           |            |     |          |          |     |         |     |     |     |     |     | VOLUME4,2016 |     |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
2) Personalizedvideostreaming enableuserstoplayvideosatahighqualityevenwhileusing
There has been significant headway in accommodating user thedeviceforothertasks,aswellasthegrowingpopularity
preferences in terms of content and QoE in VoD streaming. of short video applications, streaming algorithms that take
User preference-aware ABR algorithms that tailor content user behaviors into account have recently been developed
deliverytoindividualusercontentpreferences(forexample, to improve bandwidth efficiency. Techniques to track user
based on genre) and QoE preference (by prioritizing one engagement and streaming behavior using ML are gaining
or more QoE metrics over others) have been discussed in attentioninresearch.Recentresearchintoshortvideostream-
Section IV. This aligns with ongoing efforts to ensure that ing provides several basic solutions, including predictive
users receive the best possible perceived quality for video videopre-loadingbasedonuserbehaviorpatterns.However,
streams. Recent studies have explored RL-based personal- this introduces the question of how streaming systems can
ization where policies adapt to user-specific reward models. detect and adapt to user engagement levels and interaction
In VoD scenarios, where pre-analysis of video content is patternsinrealtimewithoutviolatingusers’privacy.
feasible, personalization techniques such as scene content
analysis and emotion-based adaptation can be implemented 5) Largelanguagemodelsforvideoapplications
toenhanceviewerengagementandsatisfaction.However,we Recentyearshavewitnessedtheemergenceofseveralsignif-
observethatsuchpersonalizedapproachesarecomparatively icantdevelopmentsinartificialintelligence,withseveralnew
scarce in live scenarios. Due to low latency requirements, technologies poised to reshape the landscape of ML-based
implementingtechniquessuchascontentanalysisorquality videostreaming.Forexample,theadoptionoflargelanguage
enhancementbecomesmorechallenginginlivescenarios.As models(LLMs)inmultimediasystemsisgainingtractiondue
such,personalizedstreamingremainsafocusmostlyinVoD totheirexceptionalabilitytogeneralizeacrossdifferenttasks
applications. andenvironments,performcomplexreasoning,andintegrate
multimodalinputs.Research[240]hasshownthepotentialof
3) 5Gforlow-latencystreaming asingleLLMtobeappliedacrossseveralnetworkingtasks,
Thedeploymentof5Gnetworksintroduceshigherbandwidth includingadaptivevideostreaming.Thiswouldsignificantly
and low latency, which significantly benefit video stream- cut down on the computational costs of training multiple
ing applications. Features such as network slicing (which neural networks for different tasks, which is one of the
allowsisolationofstreamingworkloadsondedicatedvirtual main challenges hindering the deployment of ML methods
network slices), massive MIMO (which increases spectral inpractice.
efficiency),andmillimeter-wave(mmWave)communication
(which offers high data rates over short distances) provide 6) Edge-assistedvideostreaming
resourcesforhigh-throughput,delay-sensitivevideostream- Edgecomputingisanothertechnologythatisnowgenerating
ing. Within this context, machine learning models are now immenseinterestinmultimediastreaming.Edgeservershelp
increasinglybeingusedtodesign5G-basedABRalgorithms. reduce backhaul congestion and latency as they are closer
This is because, despite their potential, 5G networks suffer to end users, making them essential for real-time streaming
fromseveralchallengesthatlimittheirreal-lifeperformance, applications.Additionally,theyhavemuchhighercomputing
suchassignalblockageinmmWave,dynamicusermobility, capabilities, allowing them to carry out computationally in-
fluctuating link quality, and energy consumption at base tensive tasks, such as training learning models or applying
stations. ML-based algorithms have thus been proposed to videoenhancement.Somerecentworks,suchas[100],have
address these issues through techniques such as proactive explored the use of a cooperative server-client approach to
adaptation,chunkprefetching,andbuffermanagement[74], streamingbyallocatingdifferenttaskstotheedgeserverand
[224],[237]–[239]. client,basedonboththeircapabilitiesandcurrentload.Such
approaches ensure that the capabilities of both clients and
4) Userbehavioranalysis edgeserversareutilizedeffectivelywithoutoverloadingthe
Whenwatchingvideocontent,viewersdonotalwaysrequire edge server, a common problem in edge-assisted schemes.
thehighestpossiblequalitythattheirnetworkconditionscan Thus,recentyearshaveseenasignificantshiftinfocusfrom
support. Often, users play videos in the background while purelyclient-basedvideostreamingalgorithms.
doingsomethingelse(forexample,playingamusicvideoin
another tab or watching a movie on a separate screen while B. PRACTICALDEPLOYMENTCHALLENGES
working).Someshortvideoapplications,suchasTikTokor Despiteremarkableadvancesinthefieldofvideostreaming,
YouTubeLive,alsoinvolvescrollingthroughvideosrapidly, weobservethatthereremainsagapbetweencurrentresearch
with users often skimming through to find their preferred practicesandreal-worldstreamingapplications,particularly
content without focusing on the videos. In these cases, a in the case of machine learning-based frameworks. This
typical quality adaptation algorithm would still continue to manifests in several aspects, such as the impractically high
deliverthevideoatthehighestpossiblequality,eventhough computational requirements of many ML solutions, espe-
the user is not actively watching, leading to bandwidth cially those leveraging DNNs. Many devices are unable
wastage. With the development of device capabilities that to implement such computationally demanding and energy-
VOLUME4,2016 21
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
consumingoperations.Recentresearchhasthereforefocused crowd-sourcedenvironments.
onprovidingsolutionstoreducethecomplexityofMLalgo-
rithmsandmakethemmorescalable,usingtechniquessuch VI. CONCLUSION
| as early-exit | models | [81], | [107]. | A   | notable | recent | study has |            |          |     |                 |     |        |           |     |
| ------------- | ------ | ----- | ------ | --- | ------- | ------ | --------- | ---------- | -------- | --- | --------------- | --- | ------ | --------- | --- |
|               |        |       |        |     |         |        |           | This paper | provides |     | a comprehensive |     | review | of recent | ad- |
alsoproposedtheinterpretationofDNNmodelstoequivalent vancementsintheapplicationofmachinelearningforHTTP
decisiontreemodels,whicharefarlesscomplex,withnearly adaptivevideostreaming.Itexaminesthechallengesfacedby
identicalperformance[241]. existingstreamingsystemsandoutlinesthepotentialadvan-
Learning-based algorithms also suffer from an inabil- tagesofemployingmachinelearningalgorithmstoovercome
| ity to perform |     | well in | real | streaming | environments. |     | These |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ---- | --------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
theseobstacles.Thepapercategorizesandcomparesmachine
learning-based algorithms are typically trained and tested learning-based methods for encoding ladder prediction, as-
in simulated environments, which are unable to accurately sessing them in terms of bandwidth efficiency, processing
mimicreal-worldstreamingscenarios.Assuch,trainedmod- speed, and visual quality. Additionally, it discusses various
els show good performance in simulated environments but bandwidthoptimizationtechniques,suchassuper-resolution
| perform | dismally | in  | real ones, | making | their | practical | de- |             |          |     |            |     |          |            |     |
| ------- | -------- | --- | ---------- | ------ | ----- | --------- | --- | ----------- | -------- | --- | ---------- | --- | -------- | ---------- | --- |
|         |          |     |            |        |       |           |     | and caching | methods. |     | A thorough |     | overview | of current | ma- |
ployment challenging. Some research has discussed the so- chinelearning-drivenqualityadaptationschemesisalsopro-
called simulated-real streaming gap [18], illustrating the vided,categorizedbytheirrespectiveapplications.Thepaper
lack of adaptability to real-world conditions of learning- concludes by highlighting several promising directions for
basedalgorithms.ProjectssuchasPuffer[19]haverecently future research. Machine learning approaches have consid-
been implemented to address this challenge, yet the issue erable potential to address key challenges in adaptive video
remainsformoststate-of-the-artalgorithmsduetothelackof streaming, and continued research is critical for enhancing
comprehensivelearning-basedtrainingplatformsusingreal- and integrating these algorithms into mainstream streaming
worlddata.
systems.
| In addition, |           | the lack | of end-to-end |     | streaming   | frameworks |          |     |     |     |     |     |     |     |     |
| ------------ | --------- | -------- | ------------- | --- | ----------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| is another   | challenge |          | that hinders  | the | integration |            | of ML in |     |     |     |     |     |     |     |     |
REFERENCES
real-worldsystems.Aspectssuchascomputationalcomplex- [1] “2023 global internet phenomena report,” 2023. [Online]. Available:
ity, latency, and device compatibility must be considered https://www.sandvine.com/global-internet-phenomena-report-2024
on the system-level, rather than component-level. We have [2] “HTTP live streaming.” [Online]. Available:
https://developer.apple.com/streaming/
toucheduponthistopicinSectionIV-A,discussingthelack
[3] “MPEG-DASH.”[Online].Available:https://dashif.org/
of research integrating QoE prediction models with other [4] “Twitch transcoding options.” [Online]. Available:
https://help.twitch.tv/s/article/transcoding-options-faq
| components | of  | the streaming |     | system. | More | comprehensive |     |               |     |       |            |           |       |              |        |
| ---------- | --- | ------------- | --- | ------- | ---- | ------------- | --- | ------------- | --- | ----- | ---------- | --------- | ----- | ------------ | ------ |
|            |     |               |     |         |      |               |     | [5] K. Bilal, | S.  | Khan, | S. Madani, | K. Hayat, | m. i. | Khan, N. Min | Allah, |
streamingframeworksremainscarceinthecurrentliterature,
J.Kołodziej,L.Wang,S.Zeadally,andD.Chen,“Asurveyongreen
withfewexceptions[167],[206],[242].
communicationsusingadaptivelinkrate,”ClusterComputing,vol.16,
092012.
| Privacy | concerns | associated |     | with | ML  | must also | be ad- |              |        |     |            |         |     |             |             |
| ------- | -------- | ---------- | --- | ---- | --- | --------- | ------ | ------------ | ------ | --- | ---------- | ------- | --- | ----------- | ----------- |
|         |          |            |     |      |     |           |        | [6] R. Shiva | Reshma | and | J. Thomas, | “Review | on  | video super | resolution: |
dressedtomakethemfeasibleforreal-worldimplementation.
|     |     |     |     |     |     |     |     | Methods | and | metrics,” | in 2023 | International | Conference | on  | Control, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- | ------- | ------------- | ---------- | --- | -------- |
ML algorithms generally require large amounts of data for CommunicationandComputing(ICCC),2023,pp.1–6.
training,muchofwhichinvolvesuserdata,raisingconcerns [7] S.Yoo,G.Kim,M.Kim,Y.Kim,S.Park,andD.Kim,“Machinelearning
basedbandwidthpredictionfordynamicadaptivestreamingoverHTTP,”
| about privacy. |     | Federated | learning | techniques |     | have | recently |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | -------- | ---------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
JournalofJAITC,vol.10,no.2,pp.33–48,2020.
shownpromiseinachievinghighperformancewhilepreserv- [8] N.Kan,C.Li,C.Yang,W.Dai,J.Zou,andH.Xiong,“Uncertainty-
ing user privacy, but their potential and limitations remain aware robust adaptive video streaming with bayesian neural network
|     |     |     |     |     |     |     |     | and | model | predictive | control,” | in  | Proceedings | of the 31st | ACM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --------- | --- | ----------- | ----------- | --- |
largely unexplored, with few works focusing on their use Workshop on Network and Operating Systems Support for Digital
invideoapplications[121],[202].ML-basedstreamingalso Audio and Video, ser. NOSSDAV ’21. New York, NY, USA:
introduces new security challenges and vulnerabilities that Association for Computing Machinery, 2021, p. 17–24. [Online].
Available:https://doi.org/10.1145/3458306.3458872
mustbeaddressed.Someofthemajorsecurityconcernsin-
|     |     |     |     |     |     |     |     | [9] D. | Yuan, Y. | Zhang, | W. Zhang, | X.  | Liu, H. | Du, and Q. | Zheng, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | --------- | --- | ------- | ---------- | ------ |
cludemodelinversionattacks,whichcanreconstructprivate “PRIOR: Deep reinforced adaptive video streaming with attention-
userdatafrommodeloutputs,andadversarialattacks,which based throughput prediction,” in Proceedings of the 32nd Workshop
|         |            |        |             |         |            |     |           | on     | Network   | and Operating |      | Systems | Support   | for Digital Audio | and        |
| ------- | ---------- | ------ | ----------- | ------- | ---------- | --- | --------- | ------ | --------- | ------------- | ---- | ------- | --------- | ----------------- | ---------- |
| can use | defective  | inputs | to          | mislead | ML-based   |     | streaming |        |           |               |      |         |           |                   |            |
|         |            |        |             |         |            |     |           | Video, | ser.      | NOSSDAV       | ’22. | New     | York, NY, | USA: Association  |            |
| models. | To address | these  | challenges, |         | blockchain |     | technolo- |        |           |               |      |         |           |                   |            |
|         |            |        |             |         |            |     |           | for    | Computing | Machinery,    |      | 2022,   | p. 36–42. | [Online].         | Available: |
https://doi.org/10.1145/3534088.3534348
| gies have | emerged | as  | a promising |     | solution | for | enhancing |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | ----------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[10] T.HoBfeld,M.Varela,P.E.Heegaard,andL.Skorin-Kapov,“Observa-
| the security, | transparency, |     | and | decentralization |     | of  | ML sys- |     |     |     |     |     |     |     |     |
| ------------- | ------------- | --- | --- | ---------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionsonemergingaspectsinQoEmodelingandtheirimpactonQoE
| tems. For | example, | immutable |     | ledgers | can | ensure | integrity |              |     |         |       |               |            |     |            |
| --------- | -------- | --------- | --- | ------- | --- | ------ | --------- | ------------ | --- | ------- | ----- | ------------- | ---------- | --- | ---------- |
|           |          |           |     |         |     |        |           | management,” |     | in 2018 | Tenth | International | Conference | on  | Quality of |
and traceability of training data and model updates, while MultimediaExperience(QoMEX),2018,pp.1–6.
|                 |     |             |     |        |         |      |           | [11] N. | T. Blog, | “VMAF: | The | journey | continues.” | [Online]. | Available: |
| --------------- | --- | ----------- | --- | ------ | ------- | ---- | --------- | ------- | -------- | ------ | --- | ------- | ----------- | --------- | ---------- |
| smart contracts |     | can enforce |     | access | control | over | user data |         |          |        |     |         |             |           |            |
https://netflixtechblog.com/vmaf-the-journey-continues-44b51ee9ed12
or encoded streams. Consequently, recent research [243], [12] C.Qiao,J.Wang,andY.Liu,“BeyondQoE:Diversityadaptationinvideo
[244] focuses on combining blockchain with ML, enabling streamingattheedge,”IEEE/ACMTransactionsonNetworking,vol.29,
videostreamingplatformstoachievestrongerguaranteesof no.1,pp.289–302,2021.
|     |     |     |     |     |     |     |     | [13] J. Jiang, | V.  | Sekar, and | H. Zhang, | “Improving | fairness, | efficiency, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --------- | ---------- | --------- | ----------- | --- |
dataintegrityanduserprivacy,especiallyincollaborativeor stability in HTTP-based adaptive video streaming with FESTIVE,” in
| 22  |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME4,2016 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
Proceedingsofthe8thInternationalConferenceonEmergingNetwork- [32] E. Agustsson, D. Minnen, N. Johnston, J. Ballé, S. J. Hwang, and
ingExperimentsandTechnologies,ser.CoNEXT’12. NewYork,NY, G.Toderici,“Scale-spaceflowforend-to-endoptimizedvideocompres-
USA:AssociationforComputingMachinery,2012,p.97–108. sion,”in2020IEEE/CVFConferenceonComputerVisionandPattern
[14] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,andM.Watson,“A Recognition(CVPR),2020,pp.8500–8509.
buffer-basedapproachtorateadaptation:Evidencefromalargevideo [33] J.Li,B.Li,andY.Lu,“Deepcontextualvideocompression,”Advances
streamingservice,”SIGCOMMComput.Commun.Rev.,vol.44,no.4, inNeuralInformationProcessingSystems,vol.34,pp.18114–18125,
p.187–198,2014. 2021.
[15] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman,“BOLA:Near-optimal [34] S.Zhang,M.Mrak,L.Herranz,M.G.Blanch,S.Wan,andF.Yang,
bitrateadaptationforonlinevideos,”IEEE/ACMTransactionsonNet- “Dvc-p: Deep video compression with perceptual optimizations,” in
working,vol.28,no.4,pp.1698–1711,2020. 2021 International Conference on Visual Communications and Image
[16] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostreaming Processing(VCIP). IEEE,2021,pp.1–5.
withPensieve,”inProceedingsoftheConferenceoftheACMSpecial [35] H.Kim,M.Bauer,L.Theis,J.R.Schwarz,andE.Dupont,“C3:High-
InterestGrouponDataCommunication,ser.SIGCOMM’17. NewYork, performanceandlow-complexityneuralcompressionfromasingleim-
NY,USA:AssociationforComputingMachinery,2017,p.197–210. ageorvideo,”inProceedingsoftheIEEE/CVFConferenceonComputer
[17] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco: VisionandPatternRecognition,2024,pp.9347–9358.
Quality-awareadaptivevideostreamingviaimitationlearning,”inPro- [36] “FFmpeg.”[Online].Available:https://ffmpeg.org
ceedingsofthe27thACMInternationalConferenceonMultimedia,ser. [37] J. De Cock, Z. Li, M. Manohara, and A. Aaron, “Complexity-based
MM’19. NewYork,NY,USA:AssociationforComputingMachinery, consistent-quality encoding in the cloud,” in 2016 IEEE International
2019,p.429–437. ConferenceonImageProcessing(ICIP),2016,pp.1484–1488.
[18] L.Jia,C.Zhou,T.Huang,C.Li,andL.Sun,“Dancingwithshackles, [38] A.V.Katsenou,J.Sole,andD.R.Bull,“Content-gnosticbitrateladder
meet the challenge of industrial adaptive streaming via offline rein- predictionforadaptivevideostreaming,”in2019PictureCodingSympo-
forcementlearning,”inIEEEINFOCOM2024-IEEEConferenceon sium(PCS),2019,pp.1–5.
ComputerCommunications,2024,pp.2169–2178. [39] J.Yang,M.Guo,S.Zhao,J.Li,andL.Zhang,“Optimaltranscoding
[19] F. Y. Yan, H. Ayers, C. Zhu, S. Fouladi, J. Hong, K. Zhang, resolution prediction for efficient per-title bitrate ladder estimation,”
P.Levis,andK.Winstein,“Learninginsitu:arandomizedexperiment 2024.[Online].Available:https://arxiv.org/abs/2401.04405
in video streaming,” in 17th USENIX Symposium on Networked [40] “Instant per-title encoding,” 2018. [Online]. Available:
Systems Design and Implementation (NSDI 20). Santa Clara, CA: https://www.mux.com/blog/instant-per-title-encoding
USENIX Association, Feb. 2020, pp. 495–511. [Online]. Available: [41] “Per-title encoding,” 2020. [Online]. Available:
https://www.usenix.org/conference/nsdi20/presentation/yan https://bitmovin.com/encoding-service/per-title-encoding/
[20] J.Kua,G.Armitage,andP.Branch,“Asurveyofrateadaptationtech- [42] D.Silhavy,C.Krauss,A.Chen,A.-T.Nguyen,C.Müller,S.Arbanowski,
niquesfordynamicadaptivestreamingoverHTTP,”IEEECommunica- S.Steglich,andL.Bassbouss,“Machinelearningforper-titleencoding,”
tionsSurveys&Tutorials,vol.19,no.3,pp.1842–1866,2017. SMPTEMotionImagingJournal,vol.131,no.3,pp.42–50,2022.
[21] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann, [43] J.AdhuranandG.Kulupana,“Content-awareconvexhullprediction,”
“A survey on bitrate adaptation schemes for streaming media over inProceedingsofthe2ndMile-HighVideoConference,ser.MHV’23.
HTTP,”IEEECommunicationsSurveys&Tutorials,vol.21,no.1,pp. NewYork,NY,USA:AssociationforComputingMachinery,2023,p.
562–585,2019. 1–7.[Online].Available:https://doi.org/10.1145/3588444.3590996
[22] R.Farahani,Z.Azimi,C.Timmerer,andR.Prodan,“TowardsAI-assisted [44] A.V.Katsenou,F.Zhang,K.Swanson,M.Afonso,J.Sole,andD.R.
sustainableadaptivevideostreamingsystems:Tutorialandsurvey,”arXiv Bull,“Vmaf-basedbitrateladderestimationforadaptivestreaming,”in
preprintarXiv:2406.02302,2024. 2021PictureCodingSymposium(PCS),2021,pp.1–5.
[23] L.PeroniandS.Gorinsky,“Anend-to-endpipelineperspectiveonvideo [45] A.V.Katsenou,J.Sole,andD.R.Bull,“Efficientbitrateladderconstruc-
streaminginbest-effortnetworks:Asurveyandtutorial,”arXivpreprint tionforcontent-optimizedadaptivevideostreaming,”IEEEOpenJournal
arXiv:2403.05192,2024. ofSignalProcessing,vol.2,pp.496–511,2021.
[24] T.Wiegand,G.Sullivan,G.Bjontegaard,andA.Luthra,“Overviewof [46] V.V.Menon,A.Premkumar,P.T.Rajendran,A.Wieckowski,B.Bross,
theH.264/AVCvideocodingstandard,”IEEETransactionsonCircuits C.Timmerer,andD.Marpe,“Energy-efficientadaptivevideostreaming
andSystemsforVideoTechnology,vol.13,no.7,pp.560–576,2003. with latency-aware dynamic resolution encoding,” in Proceedings of
[25] G.J.Sullivan,J.-R.Ohm,W.-J.Han,andT.Wiegand,“Overviewofthe the3rdMile-HighVideoConference,ser.MHV’24. NewYork,NY,
highefficiencyvideocoding(HEVC)standard,”IEEETransactionson USA:AssociationforComputingMachinery,2024,p.21–27.[Online].
CircuitsandSystemsforVideoTechnology,vol.22,no.12,pp.1649– Available:https://doi.org/10.1145/3638036.3640801
1668,2012. [47] F. Nasiri, W. Hamidouche, L. Morin, N. Dholland, and J.-Y. Aubié,
[26] A. Mercat, A. Mäkinen, J. Sainio, A. Lemmetti, M. Viitanen, and “EnsemblelearningforefficientVVCbitrateladderprediction,”in2022
J.Vanne,“Comparativerate-distortion-complexityanalysisofVVCand 10th European Workshop on Visual Information Processing (EUVIP),
HEVCvideocodecs,”IEEEAccess,vol.9,pp.67813–67828,2021. 2022,pp.1–6.
[27] J.S.Gomes,M.Grellert,F.L.L.Ramos,andS.Bampi,“End-to-end [48] F. Nasiri, W. Hamidouche, L. Morin, N. Dhollande, and J.-Y. Aubié,
neuralvideocompression:Areview,”IEEEOpenJournalofCircuitsand “Multi-presetvideoencoderbitrateladderprediction,”inProceedingsof
Systems,vol.6,pp.120–134,2025. the2ndInternationalWorkshoponDesign,Deployment,andEvaluation
[28] C.Jia,S.Wang,X.Zhang,S.Wang,J.Liu,S.Pu,andS.Ma,“Content- ofNetwork-AssistedVideoStreaming,ser.ViSNext’22. NewYork,
awareconvolutionalneuralnetworkforin-loopfilteringinhighefficiency NY, USA: Association for Computing Machinery, 2022, p. 8–13.
videocoding,”IEEETransactionsonImageProcessing,vol.28,no.7,pp. [Online].Available:https://doi.org/10.1145/3565476.3569643
3343–3356,2019. [49] P.-H. Wu, V. Kondratenko, G. Chaudhari, and I. Katsavounidis, “En-
[29] T. Li, M. Xu, and X. Deng, “A deep convolutional neural network codingparameterspredictionforconvexhullvideoencoding,”in2021
approachforcomplexityreductiononintra-modehevc,”in2017IEEE PictureCodingSymposium(PCS),2021,pp.1–5.
International Conference on Multimedia and Expo (ICME), 2017, pp. [50] L.Jia,C.Zhou,T.Huang,C.Li,andL.Sun,“Rdladder:Resolution-
1255–1260. durationladderforvbr-encodedvideosviaimitationlearning,”inIEEE
[30] G.Lu,W.Ouyang,D.Xu,X.Zhang,C.Cai,andZ.Gao,“DVC:An INFOCOM 2023 - IEEE Conference on Computer Communications,
end-to-enddeepvideocompressionframework,”inProceedingsofthe 2023,pp.1–10.
IEEE/CVFconferenceoncomputervisionandpatternrecognition,2019, [51] Y.Wu,L.Xie,S.Sun,W.Gao,andY.Yan,“Adaptiveintraperiodsize
pp.11006–11015. fordeeplearning-basedscreencontentvideocoding,”in2024IEEEIn-
[31] W.Gao,S.Sun,H.Zheng,Y.Wu,H.Ye,andY.Zhang,“OpenDMC:An ternationalConferenceonMultimediaandExpoWorkshops(ICMEW),
open-sourcelibraryandperformanceevaluationfordeep-learning-based 2024,pp.1–6.
multi-framecompression,”inProceedingsofthe31stACMInternational [52] H. Amirpour, M. Ghanbari, and C. Timmerer, “Deepstream: Video
Conference on Multimedia, ser. MM ’23. New York, NY, USA: streamingenhancementsusingcompresseddeepneuralnetworks,”IEEE
Association for Computing Machinery, 2023, p. 9685–9688. [Online]. Transactions on Circuits and Systems for Video Technology, pp. 1–1,
Available:https://doi.org/10.1145/3581783.3613464 2022.
VOLUME4,2016 23
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
[53] S.Wiedemann,H.Kirchhoffer,S.Matlage,P.Haase,A.Marban,T.Mar- [70] S.-Z. Qian, Y. Xie, Z. Pan, Y. Zhang, and T. Lin, “Dam: Deep
incˇ,D.Neumann,T.Nguyen,H.Schwarz,T.Wiegand,D.Marpe,and reinforcementlearningbasedpreloadalgorithmwithactionmaskingfor
W.Samek,“DeepCABAC:Auniversalcompressionalgorithmfordeep shortvideostreaming,”inProceedingsofthe30thACMInternational
neuralnetworks,”IEEEJournalofSelectedTopicsinSignalProcessing, Conference on Multimedia, ser. MM ’22. New York, NY, USA:
vol.14,no.4,pp.700–714,2020. Association for Computing Machinery, 2022, p. 7030–7034. [Online].
[54] C. Mueller, L. Bassbouss, S. Pham, S. Steglich, S. Wischnowsky, Available:https://doi.org/10.1145/3503161.3551573
P. Pogrzeba, and T. Buchholz, “Context-aware video encoding as a [71] Y. Li, Q. Zheng, Z. Zhang, H. Chen, and Z. Ma, “Improving abr
network-based media processing (NBMP) workflow,” in Proceedings performanceforshortvideostreamingusingmulti-agentreinforcement
of the 13th ACM Multimedia Systems Conference, ser. MMSys ’22. learning with expert guidance,” in Proceedings of the 33rd Workshop
NewYork,NY,USA:AssociationforComputingMachinery,2022,p. on Network and Operating System Support for Digital Audio and
293–298.[Online].Available:https://doi.org/10.1145/3524273.3533250 Video, ser. NOSSDAV ’23. New York, NY, USA: Association
[55] T. Huang, R.-X. Zhang, and L. Sun, “Deep reinforced bitrate ladders for Computing Machinery, 2023, p. 58–64. [Online]. Available:
for adaptive video streaming,” in Proceedings of the 31st ACM https://doi.org/10.1145/3592473.3592564
Workshop on Network and Operating Systems Support for Digital [72] H. Su, S. Wang, S. Yang, T. Huang, and X. Ren, “Reducing traffic
Audio and Video, ser. NOSSDAV ’21. New York, NY, USA: wastageinvideostreamingviabandwidth-efficientbitrateadaptation,”
Association for Computing Machinery, 2021, p. 66–73. [Online]. IEEETransactionsonMobileComputing,vol.23,no.11,pp.10361–
Available:https://doi.org/10.1145/3458306.3458873 10377,2024.
[56] V.V.Menon,H.Amirpour,C.Feldmann,M.Ghanbari,andC.Timmerer, [73] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,andL.Sun,“Bufferawareness
“Opse:Onlineper-sceneencodingforadaptivehttplivestreaming,”in neuraladaptivevideostreamingforavoidingextrabufferconsumption,”
2022 IEEE International Conference on Multimedia and Expo Work- 2023.
shops(ICMEW),2022,pp.1–4. [74] B. Palit, A. Sen, A. Mondal, A. Zunaid, J. Jayatheerthan, and
[57] N.T.Blog,“Dynamicoptimizer—aperceptualvideoencodingopti- S.Chakraborty,“ImprovingUEenergyefficiencythroughnetwork-aware
mization framework,” https://netflixtechblog.com/dynamic-optimizer-a- videostreamingover5G,”IEEETransactionsonNetworkandService
perceptual-video-encoding-optimization-framework-e19f1e3a277f. Management,vol.20,no.3,pp.3487–3500,2023.
[58] A.Zabrovskiy,P.Agrawal,C.Timmerer,andR.Prodan,“Faust:Fast [75] S.Nami,F.Pakdaman,M.R.Hashemi,S.Shirmohammadi,andM.Gab-
per-scene encoding using entropy-based scene detection and machine bouj, “Lightweight multitask learning for robust jnd prediction using
learning,” in 2021 30th Conference of Open Innovations Association latentspaceandreconstructedframes,”IEEETransactionsonCircuits
FRUCT,2021,pp.292–302. andSystemsforVideoTechnology,vol.34,no.9,pp.8657–8671,2024.
[59] S. Paul, A. Norkin, and A. C. Bovik, “Efficient per-shot convex hull [76] M.Takeuchi,S.Saika,Y.Sakamoto,T.Nagashima,Z.Cheng,K.Kanai,
predictionbyrecurrentlearning,”2022. J. Katto, K. Wei, J. Zengwei, and X. Wei, “Perceptual quality driven
[60] H.Xing,Z.Zhou,J.Wang,H.Shen,D.He,andF.Li,“Predictingrate adaptive video coding using jnd estimation,” in 2018 Picture Coding
controltargetthroughalearningbasedcontentadaptivemodel,”in2019 Symposium(PCS),2018,pp.179–183.
PictureCodingSymposium(PCS),2019,pp.1–5. [77] V.V.Menon,R.Farahani,P.T.Rajendran,S.Afzal,K.Schoeffmann,
[61] A. Falahati, M. K. Safavi, A. Elahi, F. Pakdaman, and M. Gabbouj, andC.Timmerer,“Energy-efficientmulti-codecbitrate-ladderestimation
“Efficientbitrateladderconstructionusingtransferlearningandspatio- foradaptivevideostreaming,”in2023IEEEInternationalConferenceon
temporalfeatures,”in202413thIranian/3rdInternationalMachineVi- VisualCommunicationsandImageProcessing(VCIP),2023,pp.1–5.
sionandImageProcessingConference(MVIP),2024,pp.1–7. [78] V.V.Menon,P.T.Rajendran,A.Premkumar,B.Bross,andD.Marpe,
[62] A.Telili,W.Hamidouche,S.A.Fezza,andL.Morin,“Efficientper-shot “Videosuper-resolutionforoptimizedbitrateandgreenonlinestream-
transformer-basedbitrateladderpredictionforadaptivevideostreaming,” ing,”in2024PictureCodingSymposium(PCS),2024,pp.1–5.
in 2023 IEEE International Conference on Image Processing (ICIP), [79] S.S.Andrei,N.Shapovalova,andW.Mayol-Cuevas,“SUPERVEGAN:
2023,pp.1835–1839. Super resolution video enhancement GAN for perceptually improving
[63] M. Bhat, J.-M. Thiesse, and P. Le Callet, “A case study of machine low bitrate streams,” IEEE Access, 2021. [Online]. Available:
learningclassifiersforreal-timeadaptiveresolutionpredictioninvideo https://www.amazon.science/publications/supervegan-super-resolution-
coding,”in2020IEEEInternationalConferenceonMultimediaandExpo video-enhancement-gan-for-perceptually-improving-low-bitrate-streams
(ICME),2020,pp.1–6. [80] H.Yeo,S.Do,andD.Han,“Howwilldeeplearningchangeinternet
[64] A. Telili, W. Hamidouche, S. A. Fezza, and L. Morin, “Benchmark- video delivery?” in Proceedings of the 16th ACM Workshop on
inglearning-basedbitrateladderpredictionmethodsforadaptivevideo Hot Topics in Networks, ser. HotNets-XVI. New York, NY, USA:
streaming,”in2022PictureCodingSymposium(PCS),2022,pp.325– Association for Computing Machinery, 2017, p. 57–64. [Online].
329. Available:https://doi.org/10.1145/3152434.3152440
[65] V. V. Menon, J. Zhu, P. T. Rajendran, S. Afzal, K. Schoeffmann, [81] H.Yeo,Y.Jung,J.Kim,J.Shin,andD.Han,“Neuraladaptivecontent-
P. Le Callet, and C. Timmerer, “Optimal quality and efficiency in awareinternetvideodelivery,”inProceedingsofthe13thUSENIXCon-
adaptive live streaming with jnd-aware low latency encoding,” in ferenceonOperatingSystemsDesignandImplementation,ser.OSDI’18.
Proceedings of the 3rd Mile-High Video Conference, ser. MHV ’24. USA:USENIXAssociation,2018,p.645–661.
NewYork,NY,USA:AssociationforComputingMachinery,2024,p. [82] Y.Zhang,Y.Zhang,Y.Wu,Y.Tao,K.Bian,P.Zhou,L.Song,andH.Tuo,
61–67.[Online].Available:https://doi.org/10.1145/3638036.3640807 “Improvingqualityofexperiencebyadaptivevideostreamingwithsuper-
[66] F. Micó-Enguídanos, W. Moina-Rivera, J. Gutiérrez-Aguado, and resolution,”inIEEEINFOCOM2020-IEEEConferenceonComputer
M. Garcia-Pineda, “Per-title and per-segment CRF estimation Communications,2020,pp.1957–1966.
using DNNs for quality-based video coding,” Expert Systems [83] W.Huang,Y.Ran,J.Rao,J.Luo,andS.Chen,“Queue-learning-based
with Applications, vol. 227, p. 120289, 2023. [Online]. Available: qoeoptimizationforsuper-resolution-assistedadaptivevideostreaming,”
https://www.sciencedirect.com/science/article/pii/S0957417423007911 inGLOBECOM2023-2023IEEEGlobalCommunicationsConference,
[67] S. Huang and J. Xie, “DAVE: Dynamic adaptive video encoding for 2023,pp.140–145.
real-time video streaming applications,” in 2021 18th Annual IEEE [84] C.Dong,C.C.Loy,K.He,andX.Tang,“Imagesuper-resolutionusing
InternationalConferenceonSensing,Communication,andNetworking deep convolutional networks,” IEEE Transactions on Pattern Analysis
(SECON),2021,pp.1–9. andMachineIntelligence,vol.38,no.2,pp.295–307,2016.
[68] B. O. Turkkan, T. Dai, A. Raman, T. Kosar, C. Chen, M. F. [85] W.Shi,J.Caballero,F.Huszár,J.Totz,A.P.Aitken,R.Bishop,D.Rueck-
Bulut, J. Zola, and D. Sow, “Greenabr: Energy-aware adaptive bitrate ert,andZ.Wang,“Real-timesingleimageandvideosuper-resolution
streamingwithdeepreinforcementlearning,”inProceedingsofthe13th usinganefficientsub-pixelconvolutionalneuralnetwork,”in2016IEEE
ACMMultimediaSystemsConference,ser.MMSys’22. NewYork, ConferenceonComputerVisionandPatternRecognition(CVPR),2016,
NY, USA: Association for Computing Machinery, 2022, p. 150–163. pp.1874–1883.
[Online].Available:https://doi.org/10.1145/3524273.3528188 [86] Y.Zhang,Y.Tian,Y.Kong,B.Zhong,andY.Fu,“Residualdensenet-
[69] A.Bentaleb,M.Lim,M.N.Akcay,A.C.Begen,andR.Zimmermann, workforimagesuper-resolution,”inProceedingsoftheIEEEconference
“Bitrate adaptation and guidance with meta reinforcement learning,” oncomputervisionandpatternrecognition,2018,pp.2472–2481.
IEEETransactionsonMobileComputing,vol.23,no.11,pp.10378– [87] J. Liu, J. Tang, and G. Wu, “Residual feature distillation network for
10392,2024. lightweight image super-resolution,” in Computer vision–ECCV 2020
24 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
workshops:Glasgow,UK,August23–28,2020,proceedings,partIII16. Communication,ser.SIGCOMM’20. NewYork,NY,USA:Association
Springer,2020,pp.41–55. for Computing Machinery, 2020, p. 107–125. [Online]. Available:
[88] X. Wang, K. Yu, S. Wu, J. Gu, Y. Liu, C. Dong, Y. Qiao, and https://doi.org/10.1145/3387514.3405856
C.ChangeLoy,“ESRGAN:Enhancedsuper-resolutiongenerativeadver- [105] Z.Duanmu,A.Rehman,andZ.Wang,“Aquality-of-experiencedatabase
sarialnetworks,”inProceedingsoftheEuropeanconferenceoncomputer for adaptive video streaming,” IEEE Transactions on Broadcasting,
vision(ECCV)workshops,2018,pp.0–0. vol.64,no.2,pp.474–487,2018.
| [89] H. Yeo, | C. J. | Chong, | Y. Jung, | J. Ye, | and D. Han, | “Nemo: | Enabling |          |        |          |         |           |          |         |           |
| ------------ | ----- | ------ | -------- | ------ | ----------- | ------ | -------- | -------- | ------ | -------- | ------- | --------- | -------- | ------- | --------- |
|              |       |        |          |        |             |        |          | [106] Z. | He, Y. | Yang, L. | Qiu, K. | Park, and | Y. Yang, | “Nerve: | Real-time |
neural-enhanced video streaming on commodity mobile devices,” in neural video recovery and enhancement on mobile devices,” Proc.
Proceedings of the 26th Annual International Conference on Mobile ACM Netw., vol. 2, no. CoNEXT1, Mar. 2024. [Online]. Available:
Computing and Networking, ser. MobiCom ’20. New York, NY, https://doi.org/10.1145/3649472
USA:AssociationforComputingMachinery,2020.[Online].Available: [107] M.Choi,W.J.Yun,S.B.Son,S.Park,andJ.Kim,“Jointdelay-sensitive
https://doi.org/10.1145/3372224.3419185
|             |        |        |           |         |        |          |           | and      | power-efficient    |     | quality control | of dynamic   |     | video streaming  | using |
| ----------- | ------ | ------ | --------- | ------- | ------ | -------- | --------- | -------- | ------------------ | --- | --------------- | ------------ | --- | ---------------- | ----- |
| [90] Q. Yu, | Q. Li, | R. He, | G. Tyson, | W. Shi, | J. Lv, | Z. Yuan, | P. Zhang, |          |                    |     |                 |              |     |                  |       |
|             |        |        |           |         |        |          |           | adaptive | super-resolution,” |     | IEEE            | Transactions | on  | Green Communica- |       |
Y. Lan, and Z. Li, “Bisr: Bidirectionally optimized super-resolution tionsandNetworking,vol.8,no.1,pp.103–117,2024.
for mobile video streaming,” in Proceedings of the ACM Web [108] S. Jin, R. Zhu, A. Hassan, X. Zhu, X. Zhang, Z. M. Mao, F. Qian,
Conference2023,ser.WWW’23. NewYork,NY,USA:Association and Z.-L. Zhang, “Oasis: Collaborative neural-enhanced mobile video
| for Computing |     | Machinery, | 2023, | p. 3121–3131. |     | [Online]. | Available: |             |     |                |     |          |     |            |         |
| ------------- | --- | ---------- | ----- | ------------- | --- | --------- | ---------- | ----------- | --- | -------------- | --- | -------- | --- | ---------- | ------- |
|               |     |            |       |               |     |           |            | streaming,” |     | in Proceedings | of  | the 15th | ACM | Multimedia | Systems |
https://doi.org/10.1145/3543507.3583519
|     |     |     |     |     |     |     |     | Conference, |     | ser. MMSys | ’24. | New | York, NY, | USA: | Association |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---- | --- | --------- | ---- | ----------- |
[91] W.Shen,W.Bao,G.Zhai,C.L.Wang,J.W.Hu,andZ.Gao,“Prediction- for Computing Machinery, 2024, p. 45–55. [Online]. Available:
assistantframesuper-resolutionforvideostreaming,”2021. https://doi.org/10.1145/3625468.3647610
[92] C. Li, D. He, X. Liu, Y. Ding, and S. Wen, “Adapting image [109] S. Wang, J. Yang, and S. Bi, “Adaptive video streaming in multi-tier
super-resolutionstate-of-the-artsandlearningmulti-modelensemblefor
|       |                    |     |       |                      |     |       |           | computing |     | networks: | Joint edge | transcoding | and | client enhancement,” |     |
| ----- | ------------------ | --- | ----- | -------------------- | --- | ----- | --------- | --------- | --- | --------- | ---------- | ----------- | --- | -------------------- | --- |
| video | super-resolution,” |     | CoRR, | vol. abs/1905.02462, |     | 2019. | [Online]. |           |     |           |            |             |     |                      |     |
IEEETransactionsonMobileComputing,pp.1–14,2023.
Available:http://arxiv.org/abs/1905.02462
|     |     |     |     |     |     |     |     | [110] J. Yang, | Y.  | Jiang, and | S. Wang, | “Enhancement |     | or super-resolution: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | -------- | ------------ | --- | -------------------- | --- |
[93] B.Lim,S.Son,H.Kim,S.Nah,andK.MuLee,“Enhanceddeepresidual
Learning-basedadaptivevideostreamingwithclient-sidevideoprocess-
networksforsingleimagesuper-resolution,”inProceedingsoftheIEEE ing,”inICC2022-IEEEInternationalConferenceonCommunications,
conferenceoncomputervisionandpatternrecognitionworkshops,2017,
2022,pp.739–744.
pp.136–144.
[111] Y.Ran,T.Zhang,W.Huang,S.Xia,andJ.Luo,“isaw:Intelligentsuper-
[94] Y.Zhang,K.Li,K.Li,L.Wang,B.Zhong,andY.Fu,“Imagesuper-
|     |     |     |     |     |     |     |     | resolution-assisted |     | adaptive | webrtc | video | streaming,” | in Proceedings |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | ------ | ----- | ----------- | -------------- | --- |
resolutionusingverydeepresidualchannelattentionnetworks,”inPro-
|     |     |     |     |     |     |     |     | of  | the 29th | Annual | International | Conference | on  | Mobile | Computing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------------- | ---------- | --- | ------ | --------- |
ceedingsoftheEuropeanconferenceoncomputervision(ECCV),2018, and Networking, ser. ACM MobiCom ’23. New York, NY, USA:
pp.286–301.
|     |     |     |     |     |     |     |     | Association |     | for Computing |     | Machinery, | 2023. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ---------- | ----- | --------- | ---------- |
[95] Z.Zhao,L.Song,R.Xie,andX.Yang,“Gpuacceleratedhigh-quality
https://doi.org/10.1145/3570361.3614072
video/imagesuper-resolution,”in2016IEEEInternationalSymposium
[112] L.Wang,S.Singh,J.Chakareski,M.Hajiesmaili,andR.K.Sitaraman,
onBroadbandMultimediaSystemsandBroadcasting(BMSB),2016,pp.
|     |     |     |     |     |     |     |     | “Bones: | Near-optimal |     | neural-enhanced |     | video streaming,” |     | Proc. ACM |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --------------- | --- | ----------------- | --- | --------- |
1–4.
Meas.Anal.Comput.Syst.,vol.8,no.2,May2024.[Online].Available:
[96] W.Jing,C.Liu,H.Cai,X.Wen,Z.Lu,Z.Wang,andH.Zhang,“Mec- https://doi.org/10.1145/3656014
basedsuper-resolutionenhancedadaptivevideostreamingoptimization
[113] Y.Reznik,N.Barman,andP.Wagstrom,“Improvingtheperformance
| for mobile | networks |     | with satellite | backhaul,” |     | IEEE Transactions | on  |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | -------------- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofweb-streamingbysuper-resolutionupscaling,”inProceedingsofthe
NetworkandServiceManagement,vol.21,no.3,pp.2977–2991,2024.
|            |            |       |        |       |          |        |              | 2nd | Mile-High | Video | Conference, | ser. | MHV ’23. | New | York, NY, |
| ---------- | ---------- | ----- | ------ | ----- | -------- | ------ | ------------ | --- | --------- | ----- | ----------- | ---- | -------- | --- | --------- |
| [97] J. da | M. Libório | Filho | and C. | A. V. | Melo, “A | gan to | fight video- |     |           |       |             |      |          |     |           |
USA:AssociationforComputingMachinery,2023,p.8–13.[Online].
relatedtrafficflooding:Super-resolution,”in2019IEEELatin-American Available:https://doi.org/10.1145/3588444.3590997
ConferenceonCommunications(LATINCOM),2019,pp.1–6.
|                |     |        |          |        |         |           |             | [114] E. Çetinkaya, |     | M. Nguyen, | and | C. Timmerer, | “MoViDNN: |     | A Mobile |
| -------------- | --- | ------ | -------- | ------ | ------- | --------- | ----------- | ------------------- | --- | ---------- | --- | ------------ | --------- | --- | -------- |
| [98] A. Zhang, | Q.  | Li, Y. | Chen, X. | Ma, L. | Zou, Y. | Jiang, Z. | Xu, and G.- |                     |     |            |     |              |           |     |          |
PlatformforEvaluatingVideoQualityEnhancementwithDeepNeural
| M. Muntean, |     | “Video | super-resolution |     | and caching—an |     | edge-assisted |            |     |               |           |     |       |                        |     |
| ----------- | --- | ------ | ---------------- | --- | -------------- | --- | ------------- | ---------- | --- | ------------- | --------- | --- | ----- | ---------------------- | --- |
|             |     |        |                  |     |                |     |               | Networks,” |     | in MultiMedia | Modeling. |     | Cham: | Springer International |     |
adaptivevideostreamingsolution,”IEEETransactionsonBroadcasting,
Publishing,2022,pp.465–472.
vol.67,no.4,pp.799–812,2021.
[99] J. D. M. Liborio Filho, M. de Souza Coelho, and C. A. V. Melo, [115] A. Narayanan, S. Verma, E. Ramadan, P. Babaie, and Z.-L.
|                   |            |     |                |      |               |            |           | Zhang,    | “DeepCache: |                | A deep | learning  | based framework |            | for content |
| ----------------- | ---------- | --- | -------------- | ---- | ------------- | ---------- | --------- | --------- | ----------- | -------------- | ------ | --------- | --------------- | ---------- | ----------- |
| “Super-resolution |            | on  | edge computing | for  | improved      | adaptive   | http live |           |             |                |        |           |                 |            |             |
|                   |            |     |                |      |               |            |           | caching,” | in          | Proceedings    | of the | 2018      | Workshop        | on Network | Meets       |
| streaming         | delivery,” | in  | 2021 IEEE      | 10th | International | Conference | on        |           |             |                |        |           |                 |            |             |
|                   |            |     |                |      |               |            |           | AI        | & ML,       | ser. NetAI’18. |        | New York, | NY,             | USA:       | Association |
CloudNetworking(CloudNet),2021,pp.104–110.
|     |     |     |     |     |     |     |     | for | Computing | Machinery, |     | 2018, p. | 48–53. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | ------ | --------- | ---------- |
[100] X.Liu,Z.Ke,X.Zhou,T.Qiu,andK.Li,“Qoe-orientedadaptivevideo
streamingwithedge-clientcollaborativesuper-resolution,”inGLOBE- https://doi.org/10.1145/3229543.3229555
COM2022-2022IEEEGlobalCommunicationsConference,2022,pp. [116] S.-R.Yang,Y.-J.Tseng,C.-C.Huang,andW.-C.Lin,“Multi-accessedge
computingenhancedvideostreaming:Proof-of-conceptimplementation
6158–6163.
andprediction/QoEmodels,”IEEETransactionsonVehicularTechnol-
| [101] J. | da Mata | Liborio | Filho, | J.  | Oliveira, | and | C. A. |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | ------ | --- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ogy,vol.68,no.2,pp.1888–1902,2019.
| Melo, | “Super-resolution |     | with | perceptual | quality |     | for improved |     |     |     |     |     |     |     |     |
| ----- | ----------------- | --- | ---- | ---------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
live streaming delivery on edge computing,” Computer [117] W.Li,J.Wang,G.Zhang,L.Li,Z.Dang,andS.Li,“Areinforcement
Networks, vol. 248, p. 110463, 2024. [Online]. Available: learningbasedsmartcachestrategyforcache-aidedultra-densenetwork,”
IEEEAccess,vol.7,pp.39390–39401,2019.
https://www.sciencedirect.com/science/article/pii/S1389128624002950
[118] Y.Mao,S.Zhou,H.Liu,Z.Wang,andW.Zhu,“Dynamicedgecaching
| [102] R. Wu, | W.  | Bao, L.          | Ge, and | B. B. Zhou,   | “Asrsr: | Adaptive | sending        |     |                  |     |                       |     |       |            |           |
| ------------ | --- | ---------------- | ------- | ------------- | ------- | -------- | -------------- | --- | ---------------- | --- | --------------------- | --- | ----- | ---------- | --------- |
|              |     |                  |         |               |         |          |                | via | online meta-rl,” |     | in 2023 International |     | Joint | Conference | on Neural |
| resolution   | and | super-resolution |         | for real-time |         | video    | streaming,” in |     |                  |     |                       |     |       |            |           |
Proceedings of the 19th ACM International Symposium on QoS and Networks(IJCNN),2023,pp.01–10.
SecurityforWirelessandMobileNetworks,ser.Q2SWinet’23. New [119] F. Wang, F. Wang, J. Liu, R. Shea, and L. Sun, “Intelligent video
York,NY,USA:AssociationforComputingMachinery,2023,p.61–68. caching at network edge: A multi-agent deep reinforcement learning
[Online].Available:https://doi.org/10.1145/3616391.3622763 approach,”inIEEEINFOCOM2020-IEEEConferenceonComputer
Communications,2020,pp.2499–2508.
[103] M.S.Sajjadi,R.Vemulapalli,andM.Brown,“Frame-recurrentvideo
super-resolution,”inProceedingsoftheIEEEconferenceoncomputer [120] Y. Zeng, J. Xie, H. Jiang, G. Huang, S. Yi, N. Xiong, and J. Li,
visionandpatternrecognition,2018,pp.6626–6634. “Smart caching based on user behavior for mobile edge computing,”
[104] J. Kim, Y. Jung, H. Yeo, J. Ye, and D. Han, “Neural- InformationSciences,vol.503,pp.444–468,2019.[Online].Available:
enhanced live streaming: Improving live video ingest via online https://www.sciencedirect.com/science/article/pii/S0020025519305948
learning,” in Proceedings of the Annual Conference of the [121] A.Lekharu,A.Samanta,A.Sur,andM.Patra,“Content-awarecaching
ACM Special Interest Group on Data Communication on the atthemobileedgenetworkusingfederatedlearning,”IEEETransactions
Applications,Technologies,Architectures,andProtocolsforComputer onEmergingTopicsinComputationalIntelligence,pp.1–11,2024.
| VOLUME4,2016 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 25  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
[122] L.Ma,H.Zhang,T.Li,andD.Yuan,“Deeplearningandsocialrela- [141] S. Nah, S. Baik, S. Hong, G. Moon, S. Son, R. Timofte, and K. M.
tionshipbasedcooperativecachingstrategyforD2Dcommunications,” Lee,“NTIRE2019challengeonvideodeblurringandsuper-resolution:
in201911thInternationalConferenceonWirelessCommunicationsand Datasetandstudy,”inCVPRWorkshops,June2019.
SignalProcessing(WCSP),2019,pp.1–6. [142] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-
[123] Z.Shi,Y.Zhou,D.Wu,andC.Wang,“PPVC:Onlinelearningtoward Bassett, B. Ribeiro, J. Zhan, and H. Zhang, “Oboe: Auto-tuning
optimizedvideocontentcaching,”IEEE/ACMTransactionsonNetwork- video ABR algorithms to network conditions,” in Proceedings of
ing,vol.30,no.3,pp.1029–1044,2022. the 2018 Conference of the ACM Special Interest Group on
[124] Gul-E-Laraib, S. K. u. Zaman, T. Maqsood, F. Rehman, S. Mustafa, Data Communication, ser. SIGCOMM ’18. New York, NY, USA:
M.A.Khan,N.Gohar,A.D.Algarni,andH.Elmannai,“Contentcaching Association for Computing Machinery, 2018, p. 44–58. [Online].
inmobileedgecomputingbasedonuserlocationandpreferencesusing Available:https://doi.org/10.1145/3230543.3230558
cosinesimilarityandcollaborativefiltering,”Electronics,vol.12,no.2, [143] J.vanderHooft,S.Petrangeli,T.Wauters,R.Huysegems,P.R.Alface,
2023.[Online].Available:https://www.mdpi.com/2079-9292/12/2/284 T. Bostoen, and F. De Turck, “HTTP/2-based adaptive streaming of
[125] D.Huang,X.Tao,C.Jiang,Y.Li,andJ.Lu,“Latency-efficientvideo HEVC video over 4G/LTE networks,” IEEE Communications Letters,
streaminginmetropolis:Acachingframework,”inGLOBECOM2017- vol.20,no.11,pp.2177–2180,2016.
2017IEEEGlobalCommunicationsConference,2017,pp.1–6. [144] D. Raca, J. J. Quinlan, A. H. Zahran, and C. J. Sreenan,
[126] S. M. S. Tanzil, W. Hoiles, and V. Krishnamurthy, “Adaptive scheme “Beyond throughput: a 4G LTE dataset with channel and context
for caching youtube content in a cellular network: Machine learning metrics,” in Proceedings of the 9th ACM Multimedia Systems
approach,”IEEEAccess,vol.5,pp.5870–5881,2017. Conference, ser. MMSys ’18. New York, NY, USA: Association
[127] K.N.Doan,T.VanNguyen,T.Q.S.Quek,andH.Shin,“Content-aware for Computing Machinery, 2018, p. 460–465. [Online]. Available:
proactive caching for backhaul offloading in cellular network,” IEEE https://doi.org/10.1145/3204949.3208123
Transactions on Wireless Communications, vol. 17, no. 5, pp. 3128– [145] R. Shalala, R. Dubin, O. Hadar, and A. Dvir, “Video qoe prediction
3140,2018. basedonuserprofile,”in2018InternationalConferenceonComputing,
[128] Z.Li,J.Li,Q.Wu,G.Tyson,andG.Xie,“Alarge-scalemeasurement NetworkingandCommunications(ICNC),2018,pp.588–592.
andoptimizationofmobilelivestreamingservices,”IEEETransactions [146] D. Minovski, C. Åhlund, K. Mitra, and P. Johansson, “Analysis and
onMobileComputing,pp.1–16,2022. estimation of video qoe in wireless cellular networks using machine
[129] X.Ma,Q.Li,L.Zou,J.Peng,J.Zhou,J.Chai,Y.Jiang,andG.-M. learning,” in 2019 Eleventh International Conference on Quality of
Muntean,“QAVA:QoE-awareadaptivevideobitrateaggregationforhttp MultimediaExperience(QoMEX),2019,pp.1–6.
livestreamingbasedonsmartedgecomputing,”IEEETransactionson [147] Y.BenYoussef,M.Afif,R.Ksantini,andS.Tabbane,“Anovelqoemodel
Broadcasting,vol.68,no.3,pp.661–676,2022. based on boosting support vector regression,” in 2018 IEEE Wireless
[130] J. J. Quinlan and C. J. Sreenan, “Multi-profile ultra high definition CommunicationsandNetworkingConference(WCNC),2018,pp.1–6.
(UHD)AVCandHEVC4KDASHdatasets,”inProceedingsofthe9th [148] N.Eswara,S.Ashique,A.Panchbhai,S.Chakraborty,H.P.Sethuram,
ACMMultimediaSystemsConference,ser.MMSys’18. NewYork, K. Kuchi, A. Kumar, and S. S. Channappayya, “Streaming video qoe
NY, USA: Association for Computing Machinery, 2018, p. 375–380. modelingandprediction:Alongshort-termmemoryapproach,”IEEE
[Online].Available:https://doi.org/10.1145/3204949.3208130 Transactions on Circuits and Systems for Video Technology, vol. 30,
[131] S.Lederer,C.Müller,andC.Timmerer,“Dynamicadaptivestreaming no.3,pp.661–673,2020.
over HTTP dataset,” in Proceedings of the 3rd Multimedia Systems [149] T. N. Duc, C. M. Tran, P. X. Tan, and E. Kamioka, “Bidirectional
Conference, ser. MMSys ’12. New York, NY, USA: Association lstmforcontinuouslypredictingqoeinHTTPadaptivestreaming,”in
for Computing Machinery, 2012, p. 89–94. [Online]. Available: Proceedingsofthe2ndInternationalConferenceonInformationScience
https://doi.org/10.1145/2155555.2155570 and Systems, ser. ICISS ’19. New York, NY, USA: Association
[132] A. Zabrovskiy, C. Feldmann, and C. Timmerer, “Multi-codec DASH for Computing Machinery, 2019, p. 156–160. [Online]. Available:
dataset,” in Proceedings of the 9th ACM Multimedia Systems https://doi.org/10.1145/3322645.3322687
Conference, ser. MMSys ’18. New York, NY, USA: Association [150] L. Liu, H. Hu, Y. Luo, and Y. Wen, “When wireless video streaming
for Computing Machinery, 2018, p. 438–443. [Online]. Available: meetsai:Adeeplearningapproach,”IEEEWirelessCommunications,
https://doi.org/10.1145/3204949.3208140 vol.27,no.2,pp.127–133,2020.
[133] J. J. Quinlan, A. H. Zahran, and C. J. Sreenan, “Datasets for AVC [151] H.E.Dinaki,S.Shirmohammadi,E.Janulewicz,andD.Côté,“Forecast-
(H.264)andHEVC(H.265)evaluationofdynamicadaptivestreaming ingvideoqoewithdeeplearningfrommultivariatetime-series,”IEEE
overhttp(DASH),”inProceedingsofthe7thInternationalConference OpenJournalofSignalProcessing,vol.2,pp.512–521,2021.
on Multimedia Systems, ser. MMSys ’16. New York, NY, USA: [152] P. Casas, M. Seufert, S. Wassermann, B. Gardlo, N. Wehner, and
Association for Computing Machinery, 2016. [Online]. Available: R.Schatz,“DeepCrypt-deeplearningforqoemonitoringandfinger-
https://doi.org/10.1145/2910017.2910625 printingofuseractionsinadaptivevideostreaming,”in2022IEEE8th
[134] H.Wang,I.Katsavounidis,J.Zhou,J.Park,S.Lei,X.Zhou,M.-O.Pun, InternationalConferenceonNetworkSoftwarization(NetSoft),2022,pp.
X.Jin,R.Wang,X.Wangetal.,“VideoSet:Alarge-scalecompressed 259–263.
video quality dataset based on JND measurement,” Journal of Visual [153] M.H.MazharandZ.Shafiq,“Real-timevideoqualityofexperiencemon-
CommunicationandImageRepresentation,vol.46,pp.292–302,2017. itoringforhttpsandquic,”inIEEEINFOCOM2018-IEEEConference
[135] “Netflixpublicdataset,”https://github.com/Netflix/vmaf#netflix-public- onComputerCommunications,2018,pp.1331–1339.
dataset. [154] S.Cheng,H.Hu,X.Zhang,andZ.Guo,“Rebufferingbutnotsuffering:
[136] C.G.Bampis,Z.Li,I.Katsavounidis,T.-Y.Huang,C.Ekanadham,and Exploringcontinuous-timequantitativeqoebyuser’sexitingbehaviors,”
A.C.Bovik,“Towardsperceptuallyoptimizedend-to-endadaptivevideo inInfocom’23,022023.
streaming,”arXivpreprintarXiv:1808.03898,2018. [155] W.Li,J.Huang,S.Wang,C.Wu,S.Liu,andJ.Wang,“Anapprenticeship
[137] V.Hosu,F.Hahn,M.Jenadeleh,H.Lin,H.Men,T.Szirányi,S.Li,and learningapproachforadaptivevideostreamingbasedonchunkquality
D.Saupe,“TheKonstanznaturalvideodatabase(KoNViD-1k),”in2017 and user preference,” IEEE Transactions on Multimedia, vol. 25, pp.
Ninth International Conference on Quality of Multimedia Experience 2488–2502,2023.
(QoMEX),2017,pp.1–6. [156] L.Du,L.Zhuo,J.Li,J.Zhang,X.Li,andH.Zhang,“Videoqualityof
[138] R.R.RamachandraRao,S.Göring,W.Robitza,B.Feiten,andA.Raake, experiencemetricfordynamicadaptivestreamingservicesusingdash
“AVT-VQDB-UHD-1:AlargescalevideoqualitydatabaseforUHD-1,” standard and deep spatial-temporal representation of video,” Applied
in2019IEEEInternationalSymposiumonMultimedia(ISM),2019,pp. Sciences,vol.10,p.1793,2020.
17–177. [157] R. Ul Mustafa, S. Ferlin, C. Esteve Rothenberg, D. Raca, and
[139] Y.Wang,S.Inguva,andB.Adsumilli,“Youtubeugcdatasetforvideo J. J. Quinlan, “A supervised machine learning approach for dash
compression research,” in 2019 IEEE 21st international workshop on video qoe prediction in 5g networks,” in Proceedings of the 16th
multimediasignalprocessing(MMSP). IEEE,2019,pp.1–5. ACM Symposium on QoS and Security for Wireless and Mobile
[140] T.Xue,B.Chen,J.Wu,D.Wei,andW.T.Freeman,“Videoenhancement Networks, ser. Q2SWinet ’20. New York, NY, USA: Association
withtask-orientedflow,”InternationalJournalofComputerVision,vol. for Computing Machinery, 2020, p. 57–64. [Online]. Available:
127,pp.1106–1125,2019. https://doi.org/10.1145/3416013.3426458
26 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
[158] J. Yu, H. Wen, G. Pan, S. Zhang, X. Chen, and S. Xu, “Quality of [175] J.LinandS.Wang,“Improvingrobustnessoflearning-basedadaptive
experienceorientedadaptivevideostreamingforedgeassistedcellular videostreaminginwildlyfluctuatingnetworks,”in2023IEEEInterna-
networks,”IEEEWirelessCommunicationsLetters,vol.11,no.11,pp. tionalConferenceonMultimediaandExpo(ICME),2023,pp.1787–
2305–2309,2022. 1792.
[159] V.V.Menon,R.Farahani,P.T.Rajendran,M.Ghanbari,H.Hellwagner, [176] G.F.Yang,W.-T.Lee,andH.-W.Wei,“Deepq-learningbasedalgorithm
and C. Timmerer, “Transcoding quality prediction for adaptive fordynamicadaptivestreamingoverHTTP,”inInternationalConference
video streaming,” in Proceedings of the 2nd Mile-High Video onInternetStudies,2019.
Conference, ser. MHV ’23. New York, NY, USA: Association [177] X.Zuo,J.Yang,M.Wang,andY.Cui,“Adaptivebitratewithuser-level
for Computing Machinery, 2023, p. 103–109. [Online]. Available: qoepreferenceforvideostreaming,”inIEEEINFOCOM2022-IEEE
https://doi.org/10.1145/3588444.3591012 ConferenceonComputerCommunications,2022,pp.1279–1288.
[160] V. V. Menon, P. T. Rajendran, R. Farahani, K. Schoeffmann, and [178] M.Gadaleta,F.Chiariotti,M.Rossi,andA.Zanella,“D-dash:Adeep
C. Timmerer, “Video quality assessment with texture information q-learningframeworkfordashvideostreaming,”IEEETransactionson
fusion for streaming applications,” in Proceedings of the 3rd Mile- CognitiveCommunicationsandNetworking,vol.3,no.4,pp.703–718,
High Video Conference, ser. MHV ’24. New York, NY, USA: 2017.
Association for Computing Machinery, 2024, p. 1–6. [Online]. [179] N.A.Hafez,M.S.Hassan,andT.Landolsi,“Reinforcementlearning-
Available:https://doi.org/10.1145/3638036.3640798 basedrateadaptationindynamicvideostreaming,”TelecommunSyst,
[161] R. R. R. Rao, S. Göring, P. List, W. Robitza, B. Feiten, U. Wüsten- vol.83,pp.395–407,2023.
hagen, and A. Raake, “Bitstream-based model standard for 4K/UHD: [180] J.Liu,J.Li,X.Yang,andM.Sun,“Tpmi:Accuratethroughputprediction
ITU-TP.1204.3—modeldetails,evaluation,analysisandopensource for better bitrate selection in adaptive video streaming,” in 2023 2nd
implementation,”in2020TwelfthInternationalConferenceonQuality InternationalConferenceonSensing,Measurement,Communicationand
ofMultimediaExperience(QoMEX),2020,pp.1–6. InternetofThingsTechnologies(SMC-IoT),2023,pp.140–145.
[162] D. Li, T. Jiang, and M. Jiang, “Quality assessment of in-the-wild [181] T.V.Huu,S.VanPham,T.N.T.Huong,andH.-C.Le,“QoEaware
videos,” in Proceedings of the 27th ACM International Conference video streaming scheme utilizing gru-based bandwidth prediction and
on Multimedia, ser. MM ’19. New York, NY, USA: Association adaptive bitrate selection for heterogeneous mobile networks,” IEEE
for Computing Machinery, 2019, p. 2351–2359. [Online]. Available: Access,vol.12,pp.45785–45795,2024.
https://doi.org/10.1145/3343031.3351028 [182] D. Raca, A. H. Zahran, C. J. Sreenan, R. K. Sinha, E. Halepovic,
[163] Y. Wang, J. Ke, H. Talebi, J. G. Yim, N. Birkbeck, B. Adsumilli, andV.Gopalakrishnan,“Device-basedcellularthroughputpredictionfor
P.Milanfar,andF.Yang,“Richfeaturesforperceptualqualityassessment videostreaming:Lessonsfromareal-worldevaluation,”IEEETransac-
ofUGCvideos,”in2021IEEE/CVFConferenceonComputerVisionand tionsonMachineLearninginCommunicationsandNetworking,vol.2,
PatternRecognition(CVPR),2021,pp.13430–13439. pp.318–334,2024.
[164] Z.Tu,Y.Wang,N.Birkbeck,B.Adsumilli,andA.C.Bovik,“UGC- [183] A. Biernacki, “Improving streaming video with deep learning-based
VQA:Benchmarkingblindvideoqualityassessmentforusergenerated networkthroughputprediction,”AppliedSciences,vol.12,no.20,2022.
content,” IEEE Transactions on Image Processing, vol. 30, pp. 4449– [Online].Available:https://www.mdpi.com/2076-3417/12/20/10274
4464,2021. [184] Y. S. Nam, J. Gao, C. Bothra, E. Ghabashneh, S. Rao, B. Ribeiro,
[165] Z.Tu,X.Yu,Y.Wang,N.Birkbeck,B.Adsumilli,andA.C.Bovik, J.Zhan,andH.Zhang,“Xatu:Richerneuralnetworkbasedprediction
“RAPIQUE:Rapidandaccuratevideoqualitypredictionofusergener- for video streaming,” Proc. ACM Meas. Anal. Comput. Syst., vol. 5,
atedcontent,”IEEEOpenJournalofSignalProcessing,vol.2,pp.425– no.3,dec2021.[Online].Available:https://doi.org/10.1145/3491056
440,2021. [185] A. Mondal, B. Palit, S. Khandelia, N. Pal, J. Jayatheerthan, K. Paul,
[166] Y.Feng,Y.Wang,H.Liu,L.Cong,andY.Liu,“Adaptivevideostreaming N.Ganguly,andS.Chakraborty,“Endash-amobilityadaptedenergy
based on learning intrinsic reward,” in 2022 IEEE International Sym- efficientabrvideostreamingforcellularnetworks,”in2020IFIPNet-
posiumonBroadbandMultimediaSystemsandBroadcasting(BMSB), workingConference(Networking),2020,pp.127–135.
2022,pp.1–5. [186] T. Song, P. Garza, M. Meo, and M. M. Munafò,
[167] J. Luo, F. R. Yu, Q. Chen, and L. Tang, “Adaptive video streaming “Dex: Deep learning-based throughput prediction for real-time
withedgecachingandvideotranscodingoversoftware-definedmobile communications with emphasis on traffic extremes,” Computer
networks:Adeepreinforcementlearningapproach,”IEEETransactions Networks, vol. 249, p. 110507, 2024. [Online]. Available:
onWirelessCommunications,vol.19,no.3,pp.1577–1592,2020. https://www.sciencedirect.com/science/article/pii/S1389128624003396
[168] J. Guo and G. Zhang, “A video-quality driven strategy in short [187] B.Hou,S.Yang,F.A.Kuipers,L.Jiao,andX.Fu,“Eavs:Edge-assisted
video streaming,” in Proceedings of the 24th International ACM adaptivevideostreamingwithfine-grainedserverlesspipelines,”inIEEE
Conference on Modeling, Analysis and Simulation of Wireless and INFOCOM 2023 - IEEE Conference on Computer Communications,
MobileSystems,ser.MSWiM’21. NewYork,NY,USA:Association 2023,pp.1–10.
for Computing Machinery, 2021, p. 221–228. [Online]. Available: [188] M. Darwich, K. Khalil, Y. Ismail, and M. Bayoumi, “Adaptive video
https://doi.org/10.1145/3479239.3485701 streaming: An ai-driven approach leveraging cloud and edge comput-
[169] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic ap- ing,”in2023IEEEInternationalConferenceonArtificialIntelligence,
proachfordynamicadaptivevideostreamingoverHTTP,”SIGCOMM Blockchain,andInternetofThings(AIBThings),2023,pp.1–5.
Comput.Commun.Rev.,vol.45,no.4,p.325–338,2015. [189] Y. Sun, W. Chen, G. Pan, S. Zhang, X. Chen, and Y. Wu, “Joint
[170] Dash Industry Forum, “dash.js,” https://github.com/Dash-Industry- bitratetranscodingandparallelcooperativetransmissionoptimizationfor
Forum/dash.js. adaptive video streaming in edge assisted cellular networks,” in 2023
[171] R.Netravali,A.Sivaraman,S.Das,A.Goyal,K.Winstein,J.Mickens, IEEE98thVehicularTechnologyConference(VTC2023-Fall),2023,pp.
andH.Balakrishnan,“Mahimahi:accuraterecord-and-replayforHTTP,” 1–7.
inProceedingsofthe2015USENIXConferenceonUsenixAnnualTech- [190] J. Bégaint, F. Racapé, S. Feltman, and A. Pushparaja, “CompressAI:
nicalConference,ser.USENIXATC’15. USA:USENIXAssociation, a pytorch library and evaluation platform for end-to-end compression
2015,p.417–429. research,”arXivpreprintarXiv:2011.03029,2020.
[172] P.K.Mu,J.Zheng,T.H.Luan,L.Zhu,M.Dong,andZ.Su,“AMIS: [191] H.Zhang,A.Zhou,R.Ma,J.Lu,andH.Ma,“Arsenal:Understanding
Edgecomputingbasedadaptivemobilevideostreaming,”inIEEEIN- learning-basedwirelessvideotransportviain-depthevaluation,”IEEE
FOCOM2021-IEEEConferenceonComputerCommunications,2021, Transactions on Vehicular Technology, vol. 70, no. 10, pp. 10832–
pp.1–10. 10844,2021.
[173] A.Lekharu,K.Y.Moulii,A.Sur,andA.Sarkar,“Deeplearningbased [192] J. Eo, Z. Niu, W. Cheng, F. Y. Yan, R. Gao, J. Kardhashi,
prediction model for adaptive video streaming,” in 2020 International S. Inglis, M. Revow, B.-G. Chun, P. Cheng, and Y. Xiong,
ConferenceonCOMmunicationSystems&NETworkS(COMSNETS), “OpenNetLab: Open platform for RL-based congestion control for
2020,pp.152–159. real-time communications,” in Proceedings of the 6th Asia-Pacific
[174] S.Feng,C.Wang,andX.Jiang,“Adaptivestreamingalgorithmbased Workshop on Networking, ser. APNet ’22. New York, NY, USA:
onreinforcementlearning,”inIOPConferenceSeries:MaterialsScience Association for Computing Machinery, 2023, p. 70–75. [Online].
andEngineering,vol.768,2020. Available:https://doi.org/10.1145/3542637.3542648
VOLUME4,2016 27
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
[193] J. Kang and K. Chung, “Online reinforcement learning based HTTP USA:AssociationforComputingMachinery,2022,p.81–90.[Online].
adaptivestreamingscheme,”in202213thInternationalConferenceonIn- Available:https://doi.org/10.1145/3492866.3549726
formationandCommunicationTechnologyConvergence(ICTC),2022, [212] X.Ma,Q.Li,Y.Jiang,G.-M.Muntean,andL.Zou,“Learning-basedjoint
pp.498–503. QoEoptimizationforadaptivevideostreamingbasedonsmartedge,”
[194] W. Choi, J. Chen, and J. Yoon, “Abraider: Multiphase reinforce- IEEETransactionsonNetworkandServiceManagement,vol.19,no.2,
mentlearningforenvironment-adaptivevideostreaming,”IEEEAccess, pp.1789–1806,2022.
vol.10,pp.53108–53123,2022. [213] M.Lim,M.N.Akcay,A.Bentaleb,A.C.Begen,andR.Zimmermann,
[195] J. Kang and K. Chung, “HTTP adaptive streaming framework with “When they go high, we go low: Low-latency live streaming in
onlinereinforcementlearning,”AppliedSciences,vol.12,no.15,2022. dash.jswithlol,”inProceedingsofthe11thACMMultimediaSystems
[Online].Available:https://www.mdpi.com/2076-3417/12/15/7423 Conference, ser. MMSys ’20. New York, NY, USA: Association
[196] C.Zhang,J.Yin,Y.Xu,H.Chen,XiaozhongXu,andS.Liu,“OLNC: for Computing Machinery, 2020, p. 321–326. [Online]. Available:
Onlinelearningofnetworkconditionsforadaptivevideostreaming,”in https://doi.org/10.1145/3339825.3397043
2023IEEEInternationalSymposiumonBroadbandMultimediaSystems [214] M. Hao, J. Yuan, B. Lu, L. Song, R. Xie, and W. Zhang, “Buffer
andBroadcasting(BMSB),2023,pp.1–6. displacementbasedonlinelearningalgorithmforlowlatencyhttpadap-
[197] Z.Xia,Y.Zhou,F.Y.Yan,andJ.Jiang,“Genet:Automaticcurriculum tivestreaming,”in2021IEEEInternationalSymposiumonBroadband
generationforlearningadaptationinnetworking,”inProceedingsofthe MultimediaSystemsandBroadcasting(BMSB),2021,pp.1–6.
ACMSIGCOMM2022Conference,ser.SIGCOMM’22. NewYork, [215] M.T.Vega,D.C.Mocanu,J.Famaey,S.Stavrou,andA.Liotta,“Deep
NY, USA: Association for Computing Machinery, 2022, p. 397–413. learning for quality assessment in live video streaming,” IEEE Signal
[Online].Available:https://doi.org/10.1145/3544216.3544243 ProcessingLetters,vol.24,no.6,pp.736–740,2017.
[198] H. Yuan, X. Hu, J. Hou, X. Wei, and S. Kwong, “An ensemble rate [216] L.Cui,D.Su,S.Yang,Z.Wang,andZ.Ming,“Tclivi:Transmission
adaptationframeworkfordynamicadaptivestreamingoverHTTP,”IEEE controlinlivevideostreamingbasedondeepreinforcementlearning,”
TransactionsonBroadcasting,vol.66,no.2,pp.251–263,2020. IEEETransactionsonMultimedia,vol.23,pp.651–663,2021.
[199] W. Li, X. Li, Y. Xu, Y. Yang, and S. Lu, “Metaabr: A meta-learning [217] B.Wei,H.Song,Q.N.Nguyen,andJ.Katto,“Dashlivevideostreaming
approach on adaptative bitrate selection for video streaming,” IEEE control using actor-critic reinforcement learning method,” in Mobile
TransactionsonMobileComputing,pp.1–17,2023. NetworksandManagement,C.T.Calafate,X.Chen,andY.Wu,Eds.
[200] L.Huo,Z.Wang,M.Xu,Y.Li,Z.Ding,andH.Wang,“Ameta-learning SpringerInternationalPublishing,2022,pp.17–24.
framework for learning multi-user preferences in qoe optimization of [218] Z.Tian,L.Zhao,L.Nie,P.Chen,andS.Chen,“Deeplive:Qoeopti-
dash,”IEEETransactionsonCircuitsandSystemsforVideoTechnology, mizationforlivevideostreamingthroughdeepreinforcementlearning,”
vol.30,no.9,pp.3210–3225,2020. in2019IEEE25thInternationalConferenceonParallelandDistributed
[201] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, and L. Sun, “Learning tai- Systems(ICPADS),2019,pp.827–831.
loredadaptivebitratealgorithmstoheterogeneousnetworkconditions:A [219] X. Zhang, Y. Hu, and Z. Li, “Live video streaming optimization
domain-specificpriorsandmeta-reinforcementlearningapproach,”IEEE based on deep reinforcement learning,” in Proceedings of the
JournalonSelectedAreasinCommunications,vol.40,no.8,pp.2485– 2020 12th International Conference on Machine Learning and
2503,2022. Computing, ser. ICMLC 2020. New York, NY, USA: Association
[202] Y. Xu, X. Li, Y. Yang, Z. Lin, L. Wang, and W. Li, “Fedabr: A per- for Computing Machinery, 2020, p. 116–120. [Online]. Available:
sonalizedfederatedreinforcementlearningapproachforadaptivevideo https://doi.org/10.1145/3383972.3384058
streaming,” in 2023 IFIP Networking Conference (IFIP Networking), [220] I.M.OzcelikandC.Ersoy,“Alvs:Adaptivelivevideostreamingusing
2023,pp.1–9. deep reinforcement learning,” Journal of Network and Computer
[203] H. Yuan, H. Lu, L. Meng, and M. Liu, “Muabr: Multi-user adaptive Applications, vol. 205, no. C, sep 2022. [Online]. Available:
bitratealgorithmbasedmulti-agentdeepreinforcementlearning,”inICC https://doi.org/10.1016/j.jnca.2022.103451
2022 - IEEE International Conference on Communications, 2022, pp. [221] J. Zhao and J. Pan, “Low-latency live video streaming over a low-
751–756. earth-orbit satellite network with dash,” in Proceedings of the 15th
[204] S. Altamimi and S. Shirmohammadi, “Qoe-fair dash video streaming ACMMultimediaSystemsConference,ser.MMSys’24. NewYork,
using server-side reinforcement learning,” ACM Transactions on NY, USA: Association for Computing Machinery, 2024, p. 109–120.
Multimedia Computing, Communications, and Applications, vol. 16, [Online].Available:https://doi.org/10.1145/3625468.3647616
no.2s,2020.[Online].Available:https://doi.org/10.1145/3397227 [222] H.v.Hasselt,A.Guez,andD.Silver,“Deepreinforcementlearningwith
[205] Y.Liu,D.Wei,C.Zhang,andW.Li,“Distributedbandwidthallocation doubleQ-learning,”inProceedingsoftheThirtiethAAAIConferenceon
strategy for qoe fairness of multiple video streams in bottleneck ArtificialIntelligence,ser.AAAI’16. AAAIPress,2016,p.2094–2100.
links,” Future Internet, vol. 14, no. 5, 2022. [Online]. Available: [223] H. Zhang, C. An, A. Zhou, Y. Zhu, W. Sun, Y. Lu, J. Chen, L. Liu,
https://www.mdpi.com/1999-5903/14/5/152 H.Ma,andA.Fei,“Venus:Enhancingqoeofcrowdsourcedlivevideo
[206] Y.Yuan,W.Wang,Y.Wang,S.S.Adhatarao,B.Ren,K.Zheng,and streaming by exploiting multiflow viewer assistance,” in Proceedings
X.Fu,“JointoptimizationofQoEandfairnessforadaptivevideostream- of the 30th Annual International Conference on Mobile Computing
inginheterogeneousmobileenvironments,”IEEE/ACMTransactionson and Networking, ser. ACM MobiCom ’24. New York, NY, USA:
Networking,vol.32,no.1,pp.50–64,2024. Association for Computing Machinery, 2024, p. 170–184. [Online].
[207] X.Wei,M.Zhou,S.Kwong,H.Yuan,S.Wang,G.Zhu,andJ.Cao, Available:https://doi.org/10.1145/3636534.3649354
“Reinforcementlearning-basedqoe-orienteddynamicadaptivestreaming [224] W. J. Yun, D. Kwon, M. Choi, J. Kim, G. Caire, and A. F.
framework,”InformationSciences,vol.569,pp.786–803,2021. Molisch,“Quality-awaredeepreinforcementlearningforstreamingin
[208] P.K.Mu,J.Zheng,T.H.Luan,L.Zhu,Z.Su,andM.Dong,“AMIS- infrastructure-assistedconnectedvehicles,”IEEETransactionsonVehic-
MU:Edgecomputingbasedadaptivevideostreamingformultiplemobile ularTechnology,vol.71,no.2,pp.2002–2017,2022.
users,”IEEETransactionsonMobileComputing,pp.1–18,2022. [225] J. Ye, M. Dan, and W. Jiang, “A visual sensitivity aware ABR
[209] J.KangandK.Chung,“Adaptivestreamingschemewithreinforcement algorithm for DASH via deep reinforcement learning,” ACM Trans.
learninginedgecomputingenvironments,”in2023InternationalConfer- Multimedia Comput. Commun. Appl., jun 2023. [Online]. Available:
enceonInformationNetworking(ICOIN),2023,pp.128–133. https://doi.org/10.1145/3591108
[210] M. Kim and K. Chung, “Http adaptive streaming scheme [226] S.Sengupta,N.Ganguly,S.Chakraborty,andP.De,“Hotdash:Hotspot
based on reinforcement learning with edge computing awareadaptivevideostreamingusingdeepreinforcementlearning,”in
assistance,” Journal of Network and Computer Applica- 2018IEEE26thInternationalConferenceonNetworkProtocols(ICNP),
tions, vol. 213, p. 103604, 2023. [Online]. Available: 2018,pp.165–175.
https://www.sciencedirect.com/science/article/pii/S1084804523000231 [227] L. Lu, J. Xiao, W. Ni, H. Du, and D. Zhang, “Deep-reinforcement-
[211] G. Xiong, X. Qin, B. Li, R. Singh, and J. Li, “Index-aware learning-baseduser-preference-awarerateadaptationforvideostream-
reinforcement learning for adaptive video streaming at the wireless ing,”in2022IEEE23rdInternationalSymposiumonaWorldofWire-
edge,” in Proceedings of the Twenty-Third International Symposium less,MobileandMultimediaNetworks(WoWMoM),2022,pp.416–424.
on Theory, Algorithmic Foundations, and Protocol Design for Mobile [228] W.ChoiandJ.Yoon,“CTC:Content-awaretailoringofadaptivevideo
NetworksandMobileComputing,ser.MobiHoc’22. NewYork,NY, streamingusingmulti-headcriticnetwork,”in2023FourteenthInterna-
28 VOLUME4,2016
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3582850
H.Ameretal.:AReviewofLearning-BasedMethodsforAdaptiveVideoStreamingoverHTTP
tionalConferenceonUbiquitousandFutureNetworks(ICUFN),2023, HALAAMERreceivedtheB.Sc.degreeinElec-
| pp.709–712. |     |     |     |     |     |     |     |     | tricalEngineeringin2023andiscurrentlypursu- |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
[229] Y.Sani,D.Raca,J.J.Quinlan,andC.J.Sreenan,“SMASH:Asupervised ingtheM.Sc.degreeattheAmericanUniversity
machine learning approach to adaptive video streaming over HTTP,” of Sharjah, Sharjah, UAE. Her current research
in 2020 Twelfth International Conference on Quality of Multimedia interestsfocusontheuseofmachinelearningfor
| Experience(QoMEX),2020,pp.1–6. |     |     |     |     |     |     |     |     | adaptivemultimediastreaming. |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
[230] G.Gao,L.Dong,H.Zhang,Y.Wen,andW.Zeng,“Content-awareper-
sonalisedrateadaptationforadaptivestreamingviadeepvideoanalysis,”
inICC2019-2019IEEEInternationalConferenceonCommunications
(ICC),2019,pp.1–8.
[231] S.Hu,M.Xu,H.Zhang,C.Xiao,andC.Gui,“Affectivecontent-aware
| adaptation | scheme | on qoe            | optimization | of      | adaptive | streaming over  |     |     |     |     |     |     |     |
| ---------- | ------ | ----------------- | ------------ | ------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| HTTP,”     | ACM    | Trans. Multimedia |              | Comput. | Commun.  | Appl., vol. 15, |     |     |     |     |     |     |     |
no.3s,2019.[Online].Available:https://doi.org/10.1145/3328997
[232] Z.Li,A.C.Begen,J.Gahm,Y.Shan,B.Osler,andD.Oran,“Streaming
videooverHTTPwithconsistentquality,”inProceedingsofthe5thACM
| MultimediaSystemsConference,ser.MMSys’14. |     |     |     |     | NewYork,NY,USA: |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
AssociationforComputingMachinery,2014,p.248–258.
MOHAMEDS.HASSANreceivedtheM.Sc.de-
[233] Y.Qin,S.Hao,K.R.Pattipati,F.Qian,S.Sen,B.Wang,andC.Yue, greeinelectricalengineeringfromtheUniversity
“ABRstreamingofVBR-encodedvideos:characterization,challenges, ofPennsylvania,Philadelphia,PA,USA,in2000,
andsolutions,”inProceedingsofthe14thInternationalConferenceon
|          |            |             |     |                   |     |             |     |     | and the | Ph.D. | degree in | electrical | and computer |
| -------- | ---------- | ----------- | --- | ----------------- | --- | ----------- | --- | --- | ------- | ----- | --------- | ---------- | ------------ |
| Emerging | Networking | EXperiments |     | and Technologies, |     | ser. CoNEXT |     |     |         |       |           |            |              |
engineeringfromtheUniversityofArizona,Tuc-
’18. NewYork,NY,USA:AssociationforComputingMachinery,2018,
son,AZ,USA,in2005.HeiscurrentlyaProfessor
p.366–378.
ofelectricalengineeringwiththeAmericanUni-
[234] G.Zhou,R.Wu,M.Hu,Y.Zhou,T.Z.J.Fu,andD.Wu,“Vibra:Neural
adaptivestreamingofVBR-encodedvideos,”inProceedingsofthe31st versity of Sharjah, Sharjah, UAE. In addition to
ACMWorkshoponNetworkandOperatingSystemsSupportforDigital hisworkonelectricvehicles,hehasrecentlybeen
AudioandVideo,ser.NOSSDAV’21. NewYork,NY,USA:Association activelyinvolvedinseveralprojectsacrossfields
forComputingMachinery,2021,p.1–8. such as free-space optical communications, demand response, and smart
[235] H. Amer, M. S. Hassan, and M. H. Ismail, “A content-aware deep q- grids. His primary research interests include multimedia communications
| learning | approach | for adaptive | video | streaming,” | in  | 2024 6th Inter- |     |     |     |     |     |     |     |
| -------- | -------- | ------------ | ----- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
andnetworking,wirelesscommunications,cognitiveradios,resourceallo-
nationalConferenceonCommunications,SignalProcessing,andtheir cation,andtheperformanceevaluationofbothwiredandwirelessnetworks,
Applications(ICCSPA),2024,pp.1–6. withaparticularfocusonnext-generationwirelesssystems.
[236] K.Tang,N.Kan,J.Zou,C.Li,X.Fu,M.Hong,andH.Xiong,“Multi-
| user adaptive |     | video delivery | over | wireless | networks: A | physical layer |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | ---- | -------- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
resource-awaredeepreinforcementlearningapproach,”IEEETransac-
tionsonCircuitsandSystemsforVideoTechnology,vol.31,no.2,pp.
798–815,2021.
[237] X.Hu,A.Ghosh,X.Liu,Z.-L.Zhang,andN.Shroff,“Corel:Constrained
| reinforcement |     | learning for | video | streaming | abr algorithm | design over |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | ----- | --------- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
mmwave5g,”in2023IEEEInternationalWorkshopTechnicalCommit-
teeonCommunicationsQualityandReliability(CQR),2023,pp.1–6. MAHMOUDH.ISMAIL(S’00-M’07-SM’15)re-
[238] S. Wang, J. Lin, and Y. Dai, “Mmvs: Enabling robust adaptive video ceivedtheB.Sc.degree(withhighesthonors)in
streaming for wildly fluctuating and heterogeneous networks,” IEEE Electronics and Electrical Communications En-
|     |     |     |     |     |     |     |     |     | gineering, | the | M.Sc. degree | in Communications |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | ----------------- | --- |
TransactionsonMultimedia,vol.26,pp.11018–11030,2024.
[239] S.-T.Lei,Y.-A.Chen,R.-C.Chen,C.-C.Lo,andC.-Y.Li,“IPA-DASH: EngineeringbothfromCairoUniversity,Egypt,in
IntelligentproactiveadaptationforDASHvideostreamingat5Gnetwork 2000and2002,respectively,andthePh.D.degree
edge,”in2024IEEE35thInternationalSymposiumonPersonal,Indoor inElectricalEngineeringfromTheUniversityof
andMobileRadioCommunications(PIMRC),2024,pp.1–7. Mississippi, MS, USA, in 2006. From August
[240] D. Wu, X. Wang, Y. Qiao, Z. Wang, J. Jiang, S. Cui, and 2000 to August 2002, he was a Research and
| F. Wang, | “Netllm: | Adapting | large | language | models for | networking,” |     |     |     |     |     |     |     |
| -------- | -------- | -------- | ----- | -------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
TeachingAssistantintheDepartmentofElectron-
| in Proceedings |     | of the | ACM | SIGCOMM | 2024 Conference, | ser. |     |     |     |     |     |     |     |
| -------------- | --- | ------ | --- | ------- | ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
icsandElectricalCommunicationsEngineeringatCairoUniversity.From
| ACM       | SIGCOMM    | ’24. | New   | York, NY,   | USA:      | Association for |               |     |                |           |     |            |              |
| --------- | ---------- | ---- | ----- | ----------- | --------- | --------------- | ------------- | --- | -------------- | --------- | --- | ---------- | ------------ |
|           |            |      |       |             |           |                 | 2004 to 2006, | he  | was a Research | Assistant | in  | the Center | for Wireless |
| Computing | Machinery, |      | 2024, | p. 661–678. | [Online]. | Available:      |               |     |                |           |     |            |              |
https://doi.org/10.1145/3651890.3672268 Communications(CWC)attheUniversityofMississippi.Heiscurrently
[241] Z.Meng,M.Wang,J.Bai,M.Xu,H.Mao,andH.Hu,“Interpreting aFullProfessor(onleave)attheDepartmentofElectronicsandElectrical
CommunicationsEngineering,CairoUniversityandaFullProfessoratthe
deeplearning-basednetworkingsystems,”inProceedingsoftheAnnual
|     |     |     |     |     |     |     | American | University | of Sharjah, | Sharjah, | UAE. | He was | also a Systems |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----------- | -------- | ---- | ------ | -------------- |
ConferenceoftheACMSpecialInterestGrouponDataCommunication
|        |               |               |     |                |     |               | Engineering | Consultant | at Newport | Media | Inc. | (now part | of Microchip) |
| ------ | ------------- | ------------- | --- | -------------- | --- | ------------- | ----------- | ---------- | ---------- | ----- | ---- | --------- | ------------- |
| on the | Applications, | Technologies, |     | Architectures, | and | Protocols for |             |            |            |       |      |           |               |
ComputerCommunication,ser.SIGCOMM’20. NewYork,NY,USA: Egypt Design Center in Cairo from 2006 - 2014. His research is in the
Association for Computing Machinery, 2020, p. 154–171. [Online]. general area of wireless communications with emphasis on performance
Available:https://doi.org/10.1145/3387514.3405859 evaluation of next-generation wireless systems and communications over
[242] Y. Li, Z. Zhang, H. Chen, and Z. Ma, “Mamba: Bringing multi- fadingchannels.HeistherecipientoftheUniversityofMississippiSummer
dimensionalabrtowebrtc,”inProceedingsofthe31stACMInternational AssistantshipAwardin2004and2005,TheUniversityofMississippiDis-
ConferenceonMultimedia,2023,pp.9262–9270.
sertationFellowshipAwardin2006,TheUniversityofMississippiGraduate
[243] S.Yuan,Q.Zhou,J.Li,S.Guo,H.Chen,C.Wu,andY.Yang,“Adaptive
AchievementAwardinElectricalEngineeringin2006theBestPaperAward
incentiveandresourceallocationforblockchain-supportededgevideo
presentedatthe10thIEEESymposiumonComputersandCommunications
streamingsystems:Acooperativelearningapproach,”IEEETransactions
(ISCC2005),LaMangadelMarMenor,Spain.
onMobileComputing,vol.24,no.2,pp.539–556,2025.
| [244] K. Lu, | X. Zhang, | T. Zhai, | and | M. Zhou, | “Adaptive | sharding for |     |     |     |     |     |     |     |
| ------------ | --------- | -------- | --- | -------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
UAVnetworks:Adeepreinforcementlearningapproachtoblockchain
| optimization,” |     | Sensors, | vol. 24, | no. 22, | 2024. [Online]. | Available: |     |     |     |     |     |     |     |
| -------------- | --- | -------- | -------- | ------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
https://www.mdpi.com/1424-8220/24/22/7279
| VOLUME4,2016 |     |     |     |     |     |     |     |     |     |     |     |     | 29  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/