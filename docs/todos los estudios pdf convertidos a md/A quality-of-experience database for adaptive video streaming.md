154 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
| A Quality-of-Experience |     |     |     |     |     |     | Index | for | Streaming |     |     |     | Video |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | --- | --- | --- | ----- | --- |
ZhengfangDuanmu,StudentMember,IEEE,KaiZeng,KedeMa,StudentMember,IEEE,
AbdulRehman,andZhouWang,Fellow,IEEE
Abstract—With the rapid growth of streaming media applica- Duetotheincreasingpopularityofvideostreamingservices,
tions, there has been a strong demand of quality-of-experience users are continuously raising their expectations on better ser-
(QoE)measurementandQoE-drivenvideodeliverytechnologies.
|     |     |     |     |     |     |     | vices. A | recent | survey | [6] carried | out | to investigate |     | the user |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | ----------- | --- | -------------- | --- | -------- |
Mostexistingmethodsrelyonbitrateandglobalstatisticsofstalling
preferenceonthetypeofvideodeliveryservicesshowsadom-
| events for | QoE | prediction. | This | is problematic |     | for two reasons. |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | ---- | -------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
inatingroleofQoEintheuserchoiceovertheothercategories
First,usingthesamebitratetoencodedifferentvideocontentre-
sultsindrasticallydifferentpresentationquality.Second,theinter- suchascontent,timing,quality,ease-of-use,portability,interac-
actionsbetweenvideopresentationqualityandplaybackstalling tivity,andsharing.Anotherstudy[7]showsthatglobalpremium
| experiences | are | not accounted |     | for. In this | work, | we first | build a |          |          |      |       |         |            |        |
| ----------- | --- | ------------- | --- | ------------ | ----- | -------- | ------- | -------- | -------- | ---- | ----- | ------- | ---------- | ------ |
|             |     |               |     |              |       |          | content | delivery | networks | lost | $2.16 | billion | of revenue | due to |
streamingvideodatabaseandcarryoutasubjectiveuserstudyto
poorqualityvideostreamsin2012andareexpectedtomissout
| investigate | the human |     | responses | to the | combined | effect of | video |     |     |     |     |     |     |     |
| ----------- | --------- | --- | --------- | ------ | -------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
onanastounding$20billionby2017.Thepoorstreamingexpe-
| compression, | initial | buffering, |     | and stalling. | We  | then propose | a   |     |     |     |     |     |     |     |
| ------------ | ------- | ---------- | --- | ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
novelQoEpredictionapproachnamedStreamingQoEIndexthat riencehasbecameamajorthreattothevideoserviceecosystem.
accountsfortheinstantaneousqualitydegradationduetopercep- Therefore,achievingoptimalQoEofendviewershasbeenthe
tualvideopresentationimpairment,theplaybackstallingevents,
centralgoalofmodernvideodeliveryservices.
| and the | instantaneous |     | interactions | between | them. | Experimental |     |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ------------ | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
QoEforHTTPAdaptiveStreaming(HAS)hasbeenarapidly
| results show | that | the proposed |     | model is | in close | agreement | with |     |     |     |     |     |     |     |
| ------------ | ---- | ------------ | --- | -------- | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
evolvingresearchtopicandhasattractedanincreasingamount
| subjective | opinions | and | significantly | outperforms |     | existing | QoE |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ------------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
models. The proposed model provides a highly effective and ef- ofattentionfrombothindustryandacademia.Asthehumansare
ficientmeaningsforQoEpredictioninvideostreamingservices.1 theultimatereceiverofvideosinmostapplications,subjective
evaluationisthemoststraightforwardandreliableapproachto
| Index | Terms—Adaptive |     | bitrate | streaming, |     | quality-of-experi- |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | ------- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ence,objectivequalityassessment,subjectivequalityassessment, evaluate the QoE of streaming videos. A comprehensive sub-
streamingvideo,videostalling. jective user study has several benefits. First, it provides useful
|     |     |     |                 |     |     |     | data to      | study human | behaviors |     | in evaluating |        | perceived | quality      |
| --- | --- | --- | --------------- | --- | --- | --- | ------------ | ----------- | --------- | --- | ------------- | ------ | --------- | ------------ |
|     |     |     | I. INTRODUCTION |     |     |     |              |             |           |     |               |        |           |              |
|     |     |     |                 |     |     |     | of streaming | videos.     | Second,   |     | it supplies   | a test | set       | to evaluate, |
INTHEpastdecade,therehasbeenatremendousgrowthin compareandoptimizestreamingstrategies.Third,itisusefulto
streamingmediaapplications,thankstothefastdevelopment
validateandcomparetheperformanceofexistingobjectiveQoE
ofnetwork.servicesandtheremarkablegrowthofsmartmobile models.Althoughsuchsubjectiveuserstudiesprovidereliable
| devices. | HTTP | Live Streaming |     | (HLS) | [1], Silverlight | Smooth |     |     |     |     |     |     |     |     |
| -------- | ---- | -------------- | --- | ----- | ---------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
evaluations,theyareinconvenient,time-consumingandexpen-
Streaming(MSS)[2],HTTPDynamicStreaming(HDS)[3],and sive.Mostimportantly,theyarenotapplicableinthereal-time
DynamicAdaptiveStreamingoverHTTP(DASH)[4]achieve playback scheduling framework. Therefore, highly accurate,
| decoder-driven |     | rate adaptation |     | by providing |     | video streams | in             |     |           |        |     |           |     |              |
| -------------- | --- | --------------- | --- | ------------ | --- | ------------- | -------------- | --- | --------- | ------ | --- | --------- | --- | ------------ |
|                |     |                 |     |              |     |               | low complexity |     | objective | models | are | desirable | to  | enable effi- |
a variety of bitrates and breaking them into small HTTP file cientdesignofquality-controlandresourceallocationprotocols
segments.Themediainformationofeachsegmentisstoredin
formediadeliverysystems.Overthepastdecade,substantialef-
| a manifest | file, | which | is created | at server | and | transmitted | to  |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | ---------- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
forthasbeenmadetodevelopobjectiveQoEmodels[8]–[22].
clienttoprovidethespecificationandlocationofeachsegment. Most of them are designed for specific applications such as
Throughoutthestreamingprocess,thevideoplayerattheclient
staticvideoqualityassessmentorprogressivevideostreaming.
adaptively switches among the available streams by selecting Furthermore, little work has been done to compare them with
segmentsbasedonplaybackrate,bufferconditionandinstanta-
subjectivedatacomprisingawidevarietyofvideosequences.
neousTCPthroughput[5].
Inthiswork,weaimtodesignanobjectiveQoEmodelthat
|     |     |     |     |     |     |     | accounts | for both | the presentation |     | quality |     | variations | and the |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------------- | --- | ------- | --- | ---------- | ------- |
ManuscriptreceivedMarch8,2016;revisedJuly21,2016;acceptedAugust impact of stalling experience in streaming videos. Our major
29, 2016. Date of publication September 12, 2016; date of current version contributionsarethreefold.First,weconstructavideodatabase
January13,2017. Theguesteditorcoordinatingthereviewofthispaperand dedicatedtothecombinedeffectofinitialbuffering,stallingand
approvingitforpublicationwasDr.L.Skorin-Kapov
|     |     |     |     |     |     |     | video compression |     | on QoE, | which | is  | one of | the first | publicly |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ----- | --- | ------ | --------- | -------- |
TheauthorsarewiththeDepartmentofElectricalandComputerEngineering,
UniversityofWaterloo,Waterloo,ONN2L3G1Canada(e-mail:zduanmu@ available databases of its kind. Second, we investigate the
| uwaterloo.ca; | kzeng@uwaterloo.ca; |     |     | k29ma@uwaterloo.ca; |     | abdul.rehman@ |              |         |       |              |     |         |     |          |
| ------------- | ------------------- | --- | --- | ------------------- | --- | ------------- | ------------ | ------- | ----- | ------------ | --- | ------- | --- | -------- |
|               |                     |     |     |                     |     |               | interactions | between | video | presentation |     | quality | and | playback |
uwaterloo.ca;zhou.wang@uwaterloo.ca).
stalling.Ourexperimentsshowthatthevideopresentationqual-
Colorversionsofoneormoreofthefiguresinthispaperareavailableonline
ityofthefreezingframeexhibitsinterestingrelationship,which
at http://ieeexplore.ieee.org.
DigitalObjectIdentifier10.1109/JSTSP.2016.2608329
|                 |     |          |              |        |     |                        | has not | been observed |     | before, | with the | dissatisfaction |     | level of |
| --------------- | --- | -------- | ------------ | ------ | --- | ---------------------- | ------- | ------------- | --- | ------- | -------- | --------------- | --- | -------- |
| 1The subjective |     | database | is available | online | at  | https://ece.uwaterloo. |         |               |     |         |          |                 |     |          |
thestallingevent.Third,weformulateajointvideostreaming
ca/%7Ezduanmu/jstsp16qoe/.PreliminaryresultsofSectionIIIweresubmit-
tedtothe23rdInternationalConferenceonImageProcessing,USA,2016. QoEmodelthatincorporatesboththevideopresentationquality
1932-4553©2016IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttp://www.ieee.org/publicationsstandards/publications/rights/index.htmlformoreinformation.

| DUANMUetal.:QUALITY-OF-EXPERIENCEINDEXFORSTREAMINGVIDEO |     |     |     |     |     |     |     |     |     |     |     |     | 155 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and the influence of playback stalling. Experiments on the 1) SignalFidelityMeasurement
benchmarkdatabaseshowthattheproposedmodelsignificantly ObjectiveVQAapproachestackletheQoEproblemfrom
outperformsexistingQoEmodels.TheinstantaneousQoEpre- a signal fidelity point of view to provide computational
dictionisidealfortheoptimizationofmediastreamingsystems. modelsthatcanautomaticallypredictvideopresentation
|     |     |             |     |     |     |     | quality. | In practice, | for          | the | sake of   | operational  | conve-       |
| --- | --- | ----------- | --- | --- | --- | --- | -------- | ------------ | ------------ | --- | --------- | ------------ | ------------ |
|     |     |             |     |     |     |     | nience,  | bitrate and  | Quantization |     | Parameter |              | (QP) are of- |
|     | II. | RELATEDWORK |     |     |     |     |          |              |              |     |           |              |              |
|     |     |             |     |     |     |     | ten used | as the       | indicators   | of  | video     | presentation | quality      |
A. SubjectiveQoEStudies
[1]–[4].However,usingthesamebitrateorQPtoencode
differentvideocontentcanleadtodrasticallydifferentvi-
| A significant | number | of subjective |     | QoE studies | have | been |     |     |     |     |     |     |     |
| ------------- | ------ | ------------- | --- | ----------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
conductedtounderstandtheperceptualimpactofdifferenttypes sualquality.Inaddition,differentencodersoperateatthe
samebitrateorQPbutdifferentoperationalorcomplex-
ofimpairmentsonHAS.TwoexcellentsurveysonQoEsubjec-
|     |     |     |     |     |     |     | ity modes | can also | cause | large | quality | variations | in the |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | ----- | ------- | ---------- | ------ |
tivestudycanbefoundin[23]and[24].Hereweonlyprovide
a brief overview: Pastrana et al. [25] made one of the first at- compressedvideostreams.Inordertohaveabetteresti-
|           |             |        |             |     |                 |     | mation  | of the user | perceived |          | QoE, it | is desired | to assess |
| --------- | ----------- | ------ | ----------- | --- | --------------- | --- | ------- | ----------- | --------- | -------- | ------- | ---------- | --------- |
| tempts to | measure the | impact | of stalling | in  | video streaming |     |         |             |           |          |         |            |           |
|           |             |        |             |     |                 |     | the raw | video.      | For this  | purpose, | the     | simplest   | and most  |
services.ThestudyshowedthatQoEisinfluencedbyboththe
durationandthefrequencyofstallingeventsandwasconfirmed widely used VQA measures are the mean squared error
(MSE)andpeaksignal-to-noiseratio(PSNR),whichare
byQietal.[26]andMoorthyetal.[27].Amongthosefindings,
the most important one is that viewers tend to prefer videos easytocalculateandmathematicallyconvenient,butun-
|     |     |     |     |     |     |     | fortunately | do not | correlate |     | well with | perceived | visual |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --------- | --- | --------- | --------- | ------ |
thathavelessnumberoffreezeevents(eveniftheyarerelative
|     |     |     |     |     |     |     | quality | [36]. Research |     | in perceptual |     | VQA | [37], [38] has |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------------- | --- | --- | -------------- |
longer)tovideosthathaveasequenceofshortfreezesthrough
time.Besides,Qietal.[26]alsofoundthatastallingofframe- been drawing significant attention in recent years, ex-
|     |     |     |     |     |     |     | emplified | by the | success | of  | the structural |     | similarity in- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------- | --- | -------------- | --- | -------------- |
leveldurationcouldnotbeperceived,andthushasnoimpacton
QoE. Staelens et al. [28] extended Qi’s research and conclude dex(SSIM)[8],themulti-scalestructuralsimilarityindex
(MS-SSIM)[9],motion-basedvideointegrityevaluation
thatisolatedstallingsuptoapproximately400msisacceptable
|                   |         |        |                   |     |     |           | index (MOVIE) |     | [10], | video | quality | metric | (VQM) [11] |
| ----------------- | ------- | ------ | ----------------- | --- | --- | --------- | ------------- | --- | ----- | ----- | ------- | ------ | ---------- |
| to the end-users. | Moorthy | et al. | [27] investigated |     | the | trade-off |               |     |       |       |         |        |            |
betweenstallingandqualityswitching.Whilemanystudies[29], andSSIMplus[12].State-of-the-artVQAmodelsemploy
humanvisualsystemfeaturesinqualityassessment,and
[30]assumedthatstallingeventsaremoreannoyingthanqual-
ityswitches,theresultsin[27]showedthatfewstallingevents thus provide perceptually more meaningful prediction.
|     |     |     |     |     |     |     | Nevertheless, | all | of these | models |     | are only | applicable |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------ | --- | -------- | ---------- |
arenotyieldingworsequalitythandownwardqualityswitches.
whentheplaybackprocedurecanbeaccuratelycontrolled.
Hoßfeldetal.[31]andSackletal.[32]foundfundamentaldif-
ferencesbetweeninitialdelaysandstalling.Unlikeinitialdelay However, video streaming services, due to network im-
|     |     |     |     |     |     |     | pairments, | may | suffer | from | playback | issues | that could |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ---- | -------- | ------ | ---------- |
whichissomewhatexpectedbytoday’sconsumers,stallingin-
vokesasuddenunexpectedinterruptionanddistortthetemporal significantlydegradeuserQoE.HowmodernVQAmod-
|                  |        |          |              |             |     |        | els can | be used | in the | context | of HAS | is  | still an open |
| ---------------- | ------ | -------- | ------------ | ----------- | --- | ------ | ------- | ------- | ------ | ------- | ------ | --- | ------------- |
| video structure. | Hence, | stalling | is processed | differently |     | by the |         |         |        |         |        |     |               |
problem.
| human sensory | system, | i.e., it | is perceived | much | worse | [33]. |     |     |     |     |     |     |     |
| ------------- | ------- | -------- | ------------ | ---- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Garcia et al. [34] investigated the quality impact of the com- 2) QoEPredictionviaQuality-of-Service(QoS)
Thephilosophybehindthistypeofapproachisthatthere
binedeffectofinitialloading,stalling,andcompressionforhigh
|     |     |     |     |     |     |     | exists an | causal | relationship | between |     | generic | QoS prob- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------------ | ------- | --- | ------- | --------- |
definitionsequences,fromwhichtheyobservedanadditiveim-
pact of stalling and compression on perceived QoE. Besides lems (e.g, loss, delay, jitter, reordering and throughput
limitations)andgenericQoEproblems(e.g.,glitches,arti-
theeffectofvideoimpairmentitself,Seshadrinathanetal.[35]
described a hysteresis effect in a recent study of time-varying factsandexcessivewaitingtime)[39].Therefore,QoEcan
|                |                |     |            |         |            |     | be easily | quantified | once | the | mapping | function | between |
| -------------- | -------------- | --- | ---------- | ------- | ---------- | --- | --------- | ---------- | ---- | --- | ------- | -------- | ------- |
| video quality. | In particular, | an  | unpleasant | viewing | experience |     |           |            |      |     |         |          |         |
QoSandQoEisknown.ThankstothereliabilityofTCP,
inthepasttendstopenalizetheQoEinthefutureandaffectthe
overallQoE. HAS is immune to glitches and artifacts introduced by
packetdrop.Thus,mostexistingresearchinthisdirection
| Based on | these subjective |     | user studies, | one | may | conclude |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | ------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
that: 1) video presentation quality, duration and frequency of are dedicated to stallingexperiencequantification.
Watanabeetal.[13]attempttoquantifystreamingvideo
stallingarethekeyfactorscontributingtowardstheoverallQoE;
QoEbasedonplaybackstallings.Theyobservedaloga-
| 2)Althoughveryshortstallingmaynotbeperceived |     |     |     |     |     | andthus |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
haslittleimpactonQoE,visiblestallingeventscanseverelyde- rithmicrelationshipbetweenthegloballengthofstalling
|     |     |     |     |     |     |     | events and | QoE. | Mok | et al. | [40] associated |     | the length |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --- | ------ | --------------- | --- | ---------- |
gradeQoE;3)Viewersaremuchmoretoleranttoinitialbuffer-
ing than stalling; 4) An unpleasant viewing experience in the and frequency of stalling to QoE with a linear function.
|     |     |     |     |     |     |     | Hoßfeldetal. | [14],[15],[39]demonstratedthesuperior- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------------------------- | --- | --- | --- | --- | --- |
pasttendstopenalizefutureQoE.
|     |     |     |     |     |     |     | ity of exponential |          | mapping | functions  |     | in many              | streaming |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | -------- | ------- | ---------- | --- | -------------------- | --------- |
|     |     |     |     |     |     |     | applications.      | Although |         | the global |     | QoS statistics-based |           |
B. ExistingObjectiveQoEModels
|     |     |     |     |     |     |     | QoE models | are | computationally |     | efficient, |     | they ignore |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | ---------- | --- | ----------- |
The existing QoE models can be roughly categorized as theimportanceoftemporalfactors.Rodriguezetal.[17]
| follows: |     |     |     |     |     |     | considerthepatternofjitterandlocalcontentimportance |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |

156 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
| bysubjectivetrainingofthecontent.Yeganehetal.[18] |     |     |     |     |     |     | TABLEI |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
quantify the stalling experience with a raised cosine INFORMATIONOFREFERENCEVIDEOS
functionandtherecoveryofsatisfactionlevelduringthe
playback state with a linear model. Deepti et al. [19] Index Name FrameRate Description
employ a Hammerstein-Wiener model using the stalling a Animation 25 animation,highmotion
length,thetotalnumberofstallingevents,thetimesince b Biking 50 human,outdoor
the previous stall, and the inverse stalling density as c BirdsOfPrey 30 natural,static
|         |                     |     |               |            |     | d ButterFly | 25  | natural,outdoor     |     |     |
| ------- | ------------------- | --- | ------------- | ---------- | --- | ----------- | --- | ------------------- | --- | --- |
| the key | features to predict | the | instantaneous | experience |     |             |     |                     |     |     |
|         |                     |     |               |            |     | e CloudSea1 | 24  | architecture,static |     |     |
at each moment. The stalling experience quantification f CloudSea2 24 outdoor,highmotion
|               |                  |          |                  |                |     | g CostaRica1 | 25  | natural,static   |     |     |
| ------------- | ---------------- | -------- | ---------------- | -------------- | --- | ------------ | --- | ---------------- | --- | --- |
| approach      | is only adequate | in       | the progressive  | download       |     |              |     |                  |     |     |
|               |                  |          |                  |                |     | h CostaRica2 | 25  | natural,static   |     |     |
| services      | because it is    | unable   | to measure       | the experience |     |              |     |                  |     |     |
|               |                  |          |                  |                |     | i Football1  | 25  | human,highmotion |     |     |
| loss of video | quality.         | However, | in HAS,          | a source video |     |              |     |                  |     |     |
|               |                  |          |                  |                |     | j Football2  | 25  | human,highmotion |     |     |
|               |                  |          |                  |                |     | k Football3  | 25  | human,highmotion |     |     |
| is always     | encoded into     | multiple | representations, | which          |     |              |     |                  |     |     |
|               |                  |          |                  |                |     | l Forest1    | 25  | natural,static   |     |     |
havedifferentpresentationquality.
|     |     |     |     |     |     | m Forest2 | 25  | natural,outdoor |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------------- | --- | --- |
3) HybridApproach
|            |                |              |           |              |     | n MTV          | 25  | human,indoor       |     |     |
| ---------- | -------------- | ------------ | --------- | ------------ | --- | -------------- | --- | ------------------ | --- | --- |
|            |                |              |           |              |     | o Ski          | 30  | outdoor,highmotion |     |     |
| Apparently | both video     | presentation | quality   | and stalling |     |                |     |                    |     |     |
|            |                |              |           |              |     | p Squirrel     | 25  | animation,outdoor  |     |     |
| experience | quantification | capture      | important | aspects      | in  |                |     |                    |     |     |
|            |                |              |           |              |     | q Transformer1 | 24  | human,static       |     |     |
QoE.Unfortunately,veryfewapproachesincorporatethe r Transformer2 24 human,architecture
two aspects into a unified model. Ricardo et al. [22] ap- s Basketball1 25 human,highmotion
|     |     |     |     |     |     | t Basketball2 | 25  | human,highmotion |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------- | --- | --- |
proximatedtheeffectofframedropandimagesharpness
separately,andtooktheproductofthetwotermstopre-
| dict the | overall QoE. Singh | et  | al. [20] tried | to solve this |     |     |     |     |     |     |
| -------- | ------------------ | --- | -------------- | ------------- | --- | --- | --- | --- | --- | --- |
problembytrainingarandomneuralnetwork[41]using
A. VideoDatabaseandSubjectiveUserStudy
QP,frequency,averageandmaximumdurationofstalling
events as input features. Xue et al. [21] estimated the Avideodatabase,namedstreamingvideoQoEdatabase,of20
pristinehigh-qualityvideosofsize1920×1080areselectedto
| video presentation | quality | by  | QP and weighted | the im- |     |     |     |     |     |     |
| ------------------ | ------- | --- | --------------- | ------- | --- | --- | --- | --- | --- | --- |
pact of stalling by packet bit count as an indicator of coverdiversecontent,includinghumans,plants,naturalscenes,
motioncomplexity.Bothalgorithmsdefinevideopresen- architectures and computer-synthesized sceneries. All videos
tationqualityasafunctionofQP,whichhasbeenproven have the length of 10 s [42]. The detailed specifications of
tobeapoorperceptualqualityindicator. those videos are listed in Table I and a screenshot from each
Despite the demonstrated success, most existing QoE pre- video is included in Fig. 1. Using aforementioned sequences
dictorseitherunderestimatetheeffectofperceptualvideopre- as the source, each video is encoded into three bitrate levels
sentation quality or simply equate it to bitrate or QP. More (500Kbps,1500Kbps,3000Kbps)withx264encodertocover
importantly, one common assumption of all these approaches different quality levels. The choices of bitrate levels are based
isthatthereisnointeractionbetweenvideopresentationqual- on commonly-used parameters for transmission of HD videos
ity and stalling experience, which has not been systematically over networks. A 5-s stalling event is simulated at either the
examined. beginning or the middle point of the encoded sequences. The
stallingindicatorwasimplementedasaspinningwheel.Intotal,
|     |     |     |     |     | we obtain  | 200 test samples | that              | include 20 | source videos, | 60   |
| --- | --- | --- | --- | --- | ---------- | ---------------- | ----------------- | ---------- | -------------- | ---- |
|     |     |     |     |     | compressed | videos, 60       | initial buffering | videos,    | and 60         | mid- |
III. SUBJECTIVEQUALITY-OF-EXPERIENCEUSERSTUDYOF
|     | STREAMINGVIDEOS |     |     |     | stallingvideos. |         |            |          |             |     |
| --- | --------------- | --- | --- | --- | --------------- | ------- | ---------- | -------- | ----------- | --- |
|     |                 |     |     |     | The subjective  | testing | experiment | is setup | as a normal | in- |
To the best of our knowledge, current publicly available door home settings with ordinary illumination level, with no
databasesarededicatedtoeithervideopresentationqualitythat reflecting ceiling walls and floors. All videos are displayed at
isaffectedbycompression,channeltransmissionlosses,scaling, theiractualpixelresolutiononanLCDmonitorataresolutionof
2560×1600pixelwithTruecolor(32bit)at60Hz.Themonitor
ortheimpactofstallingintermsofitsoccurringposition,dura-
tion, and frequency. However, QoE of streaming video should iscalibratedinaccordancewiththerecommendationsofITU-T
beajointeffectofthevideopresentationqualityandplayback BT.500 [43]. A customized graphical user interface is used to
stalling.Althoughthecombinedeffectofstallingandvideobi- renderthevideosonthescreenwithrandomorderandtorecord
tratehasbeeninvestigatedbyGarciaetal.[34],thestudysuffers theindividualsubjectratingsonthedatabase.Thestudyadoptsa
from the following problems: (1) the dataset is of insufficient single-stimulusqualityscoringstrategy.Atotalof25na¨ıvesub-
size (6 source sequences); (2) bitrate is not a good indicator jects,including13malesand12femalesagedbetween22and
of video presentation quality as discussed in the Section II-B; 30,participateinthesubjectivetest.Visualacuity(i.e.,Snellen
and (3) the database is not publicly available. Therefore, our test) and color vision (i.e., Ishihara) are confirmed from each
goal is to develop a dedicated database to study the interac- subject before the subjective test. A training session was per-
tion between stalling effect and presentation quality for video formedbeforethedatacollection,duringwhich,4videos(of1.
streaming. pristinequalityvideo,2.500Kbpsencodedvideo,3.videowith

DUANMUetal.:QUALITY-OF-EXPERIENCEINDEXFORSTREAMINGVIDEO 157
Fig.1. Subjectivetestsequences.
initialbuffering,and4.videowithstalling)werepresentedtothe practice,humansareoftenattractedbyvideocontentratherthan
subjects.Weusedthesamemethodstogeneratethevideosused qualityvariations.Buttocollectqualityscores,certaininstruc-
in the training and testing sessions. Therefore, subjects knew tionhastobegiventothesubjectsinordertoobtaintheiropin-
whatdistortiontypeswouldbeexpectedbeforethetestsession, ionsonvideoquality.Ontheotherhand,iftoomuchinstruction
andthuslearningeffectsarekeptminimalinthesubjectiveex- isgiven,thesubjectsmaybeover-educatedtogive“clean”but
periment.Subjectswereinstructedwithsamplevideostojudge unrealisticscores.Inourstudy,togiveuniforminstructiontoall
theoverallvisualqualityconsideringbothpicturedistortionar- subjects, and to investigate the interactions between presenta-
tifactsandvideofreezesasqualitydegradationfactors.Thesub- tionqualityanddelay/stalling,wefinditnecessarytoinformthe
jectsareallowedtomovetheirpositionstogetcloserorfarther subjects about what types of quality degradations they should
away from the screen for better observation. For each subject, expecttosee.Otherthanthat,nofurtherspecificationsaregiven.
thewholestudytakesaboutoneandhalfhour,whichisdivided Sincethebreakbetweensuccessivetestsessionsisconsider-
intothreesessionswithtwo7-minbreaksin-between.Inorderto ablyshort,alignmentonthesubjectivescoresisnotperformed.
minimizetheinfluenceoffatigueeffect,thelengthofasession Inotherwords,rawsubjectivescoresareusedinthesubsequent
was limited to 25 min. The choice of a 100-point continuous analysis. After the subjective user study, two outliers are re-
scaleasopposedtoadiscrete5-pointITU-RAbsoluteCategory movedbasedontheoutlierremovalschemesuggestedin[43].
Scale(ACR)hasadvantages:expandedrange,finerdistinctions The final quality score for each individual image is computed
betweenratings,anddemonstratedpriorefficacy[44]. as the average of subjective scores, namely the mean opinion
Acommondilemmaineverysubjectivevideoqualityexperi- score(MOS),fromallvalidsubjects.ConsideringtheMOSas
mentishowmuchinstructionshouldbegiventothesubjects.In the“groundtruth”,theperformanceofindividualsubjectscan

158 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
Fig.3. SSIMplusofstallingframesversusMOSdrop.
acrossdifferentvideopresentationqualitywhenastallingevent
occursinthemiddleofthesequences.
Fig. 3 shows a scatter plot of the instantaneous quality of
the freezing frame predicted by SSIMplus [12] and the MOS
degradation for both initial delay and playback stalling. It can
beobserved thatforthestallingatthesametemporalinstance
andofthesameduration,humansubjectstendtogiveahigher
penaltytothevideowithahigherinstantaneousvideopresen-
tation quality at the freezing frame. We further performed a
statistical significance test as follows. Denoting the SSIMplus
score of the initial buffered/stalling frame, and the MOS drop
of the test video with initial buffering/stalling as random vari-
ablesX1/X2 andY1/Y2,wespecifythenullhypothesesH1/H2
Fig.2. PLCCandSRCCbetweenindividualsubjectratingandMOS.Right- as tha√t X1/X2 is uncorrelated with Y1/Y2. The test statistic is
mostcolumn:Performanceofanaveragesubject. t= r N−2 ,wherer andN arethecorrelationcoefficient and
1−r2
thenumberofsamples,respectively.Theresultingteststatistic
beevaluatedbycalculatingthecorrelationcoefficientbetween isusedtocomputetheP-valuesbyreferringtoat-distribution
individualsubjectratingsandMOSvaluesforeachimageset, with N −2 degrees of freedom. Since the P-values (6.32 ×
andthenaveragingthecorrelationcoefficientsofallimagesets. 10−8 for initial buffering and 6.87 × 10−13 for stalling) are
The Pearson linear correlation coefficient (PLCC) and Spear- muchsmallerthanthesignificancelevel0.05,werejectthenull
man’srand-ordercorrelationcoefficient(SRCC)areemployed hypothesesinfavorofthealternatives.Theresultssuggestthat
as comparison criteria, whose range is from 0 to 1 and higher thereissufficientevidenceatthe0.05significanceleveltocon-
values indicate better performance. They can be computed for cludethatthereisalinearrelationshipinthepopulationbetween
each subject and their values for all subject are depicted in the SSIMplus score (estimation of the presentation quality) of
Fig.2.Itcanbeseenthateachindividualsubjectperformswell theinitialbuffered/stallingframeandtheQoEdrop.Thisphe-
intermsofpredictingMOSs.Theaverageperformanceacross nomenonwasnotobservedinpreviousstudies.Oneexplanation
all individual subjects is also given in the rightmost column maybethatthereisahigherviewerexpectationwhenthevideo
in Fig. 2. This provides a general idea about the performance presentationqualityishigh,andthustheinterruptioncausedby
ofanaveragesubject.Therefore,weconcludethatconsiderable stallingmakethemfeelmorefrustrated.
agreementisobservedamongdifferentsubjectsontheperceived
qualityofthetestvideosequences.
C. PerformanceofExistingObjectiveQoEModels
Usingtheabovedatabase,wetesttheperformanceoffourex-
B. SubjectiveDataAnalysis
istingVQAmodels,includingPSNR,SSIM[8],MS-SSIM[9]
One of the main objectives of this subjective experiment is andSSIMplus [12]and fourstate-of-the-artQoEmodels [15],
to investigate whether the impact of the stalling events are in- [17],[21],[40].TheimplementationsfortheVQAmodelsare
dependent of the video presentation quality. If the answer is obtainedfromtheoriginalauthorsandweimplementfourQoE
yes,thenregardless ofthevideo presentation quality,stallings models since they are not publicly available. For the purpose
willhavethesameimpactontheoverallQoEscores.Assuming of fairness, all models are tested using their default parame-
anadditiverelationshipbetweenstallingandvideopresentation tersettings.InordertocomparetheperformanceofVQAand
qualityasin[34],weareexpectinganearconstantMOSdrop stalling-basedQoEmodels,thequalityofvideowithoutstalling

| DUANMUetal.:QUALITY-OF-EXPERIENCEINDEXFORSTREAMINGVIDEO |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 159 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLEII
COMPARISONOFTHEEXISTINGQOEMETHODS
|     |     |     |     |     |     | Stalling |     |     |     |     | Presentationquality |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
QoEmodels Regressionfunction Influencingfactors Regressionfunction Influencingfactors
| FTW[15]   |     |     | exponential |     |     |     | stallinglength,#ofstalling |     |     |     | N/A |     |     | N/A |     |
| --------- | --- | --- | ----------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mok’s[40] |     |     | linear      |     |     |     | stallinglength,            |     |     |     | N/A |     |     | N/A |     |
stallingfrequency,
initialbufferinglength
VsQM[17] exponential averagestallinglengthpersegment, N/A N/A
#ofstallingpersegment,
periodpersegment
| Xue’s[21] |     |     | logarithmic |     |     |     | stallinglength, |     |     |     | linear |     |     | QP  |     |
| --------- | --- | --- | ----------- | --- | --- | --- | --------------- | --- | --- | --- | ------ | --- | --- | --- | --- |
#ofstalling,
bitcountofthestallingsegment
|     |     |     |     |     |     |     |     | of video | presentation | quality | in QoE | should | not | be underesti- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ------- | ------ | ------ | --- | ------------- | --- |
mated.Second,eventhoughmodernVQAmodelscannotcap-
turetheexperiencelossofstalling,mostofthemperformsrea-
|     |     |     |     |     |     |     |     | sonably well | on the | streaming | video | QoE | database. | These | ob- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | ----- | --- | --------- | ----- | --- |
servationssuggestahybridmodelthatequipsVQAmethodsas
|     |     |     |     |     |     |     |     | the video | quality | predictor | would | be more | promising |     | in QoE |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | ----- | ------- | --------- | --- | ------ |
estimation.
IV. OBJECTIVEQUALITY-OF-EXPERIENCEMODELOF
STREAMINGVIDEOS
Motivatedbytheobservationandanalysisprovidedinthepre-
vioussection,wedevelopaunifiedQoEpredictionmodelnamed
StreamingQoEIndex(SQI)byincorporatingthevideopresen-
|     |     |     |     |     |     |     |     | tation quality | and | the impact | of  | initial | buffering | and | stalling |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ------- | --------- | --- | -------- |
Fig.4. SQIatdifferentnumberofstallingevents. events. In particular, we consider QoE as a combined experi-
enceofvideopresentationquality,stallingexperienceandtheir
interaction.
| are estimated |          | by VQA  | and the | result     | is applied | to  | the same  |     |     |     |     |     |     |     |     |
| ------------- | -------- | ------- | ------- | ---------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| video with    | stalling | events. | For     | the hybrid | model      | in  | [21], the |     |     |     |     |     |     |     |     |
model parameter c is not given in the original paper. We set A. VideoPresentationQuality
c=0.05suchthatthemodelachievesitsoptimalperformance
Foreachframeinthestreamingvideo,itsinstantaneousvideo
onthecurrentdatabase.AcomparisonofthefourQoEmodels
|          |          |           |          |     |              |     |             | presentationqualityP |     | n canbeestimatedattheserversidebya |     |     |     |     |     |
| -------- | -------- | --------- | -------- | --- | ------------ | --- | ----------- | -------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
| is shown | in Table | II. Three | criteria |     | are employed |     | for perfor- |                      |     |                                    |     |     |     |     |     |
frame-levelVQAmodelbeforetransmission
manceevaluationbycomparingMOSandobjectiveQoE.Some
|     |     |     |     |     |     |     |     |     |     |     | =V(X | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
of the criteria are included in previous tests carried out by the P n n ,R n (1)
video quality experts group [45]. Other criteria are adopted in whereX andR arethen-thframeofthestreamingvideoand
|     |     |     |     |     |     |     |     |     | n n |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
previousstudy[46].Theseevaluationcriteriaare:1)PLCCafter pristinequalityvideo,andV(·)isafullreferenceVQAoperator.
| a nonlinear | modified | logistic | mapping |     | between | the | subjective |              |         |       |     |      |            |     |        |
| ----------- | -------- | -------- | ------- | --- | ------- | --- | ---------- | ------------ | ------- | ----- | --- | ---- | ---------- | --- | ------ |
|             |          |          |         |     |         |     |            | The computed | quality | score | V(X | ,R ) | can either | be  | embed- |
n n
| and objective |     | scores [46]; | 2)  | SRCC; | 3) Mean | absolute | error |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | ----- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
dedintothemanifestfilethatdescribesthespecificationsofthe
(MAE)afterthenon-linearmapping.Amongtheabovemetrics,
|     |     |     |     |     |     |     |     | video, or | carried | in the | metadata | of the | video container. |     | Cur- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | -------- | ------ | ---------------- | --- | ---- |
PLCC and MAE are adopted to evaluate prediction accuracy, rently,thedevelopmentofthenext-generationISObasemedia
andSRCCisemployedtoassesspredictionmonotonicity[45].
fileformatthatincorporatestime-varyingvideoqualitymetricis
| A better | objective | VQA | measure | should | have | higher | PLCC |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------- | ------ | ---- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ongoing[47].Themanifestormetadatafileistransmittedtothe
andSRCCwhilelowerMAEvalues.Figs.6–8summarizethe clientsidesuchthatitsinformationisavailabletotheclient.In
| evaluation | results, | which | is somewhat |     | disappointing |     | because |     |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | ----------- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
commonlyusedstreamingprotocolssuchasMPEG-DASH,the
state-of-the-art QoE models do not seem to provide adequate partiallydecodedframewillnotbesentforrendering,andthus
| predictions | ofperceived |     | qualityofstreamingvideos.Even |     |     |     | the |     |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
viewerswillseethelastsuccessfullydecodedframeduringthe
modelwiththebestperformanceisonlymoderatelycorrelated
stallinginterval.Thus,forastallingmomentnintheinterrup-
with subjective scores. These test results also provide some tionperiod[i,j],thevideopresentationqualityattheinstance,
| useful insights |     | regarding | the general |     | approaches | used | in QoE |                                               |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ----------- | --- | ---------- | ---- | ------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |           |             |     |            |      |        | P ,isthesameasthequalityofthelastdecodedframe |     |     |     |     |     |     |     |
n
| models.                                                | First, | the hybrid | model | [21] | significantly | outperforms |     |     |     |     |      |      |     |     |     |
| ------------------------------------------------------ | ------ | ---------- | ----- | ---- | ------------- | ----------- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
|                                                        |        |            |       |      |               |             |     |     |     |     | P =P | i−1. |     |     |     |
| QoS-QoEcorrelationmodels.Thissuggeststhattheimportance |        |            |       |      |               |             |     |     |     |     | n    |      |     |     | (2) |

160 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
Fig.6. PLCCofQoEmodelsonstreamingvideoQoEdatabase.
Fig.7. SRCCofQoEmodelsonstreamingvideoQoEdatabase.
B. StallingExperienceQuantification
Tosimplifytheformulation,weassumetheinfluenceofeach
stallingeventisindependentandadditive.Assuch,wecanana-
lyzeeachstallingeventseparatelyandcomputetheoveralleffect
Fig. 5. An illustrative example of and channel responses at each frame. by aggregating them. Note that each stalling event divides the
(a)Videopresentationqualityofthestaticvideoateachframe.‘*’indicatesthe
streamingsessiontimelineintothreenon-overlappingintervals,
positionofstalling.(b)Videopresentationqualityofthestreamingvideoduring
playbackateachframe.‘*’indicatesthepositionofstallingand‘o’indicates i.e.,thetimeintervalsbeforethestalling,duringthestalling,and
thepositionofrecovery.(c)QoEdropduetoeachstallingeventsateachframe. afterthestalling.Wewilldiscussthethreeintervalsseparately
ThesolidcurveshowstheQoEdropduetoinitialbufferingandthedashed
becausetheimpactofthestallingeventoneachoftheintervals
curveshowstheQoEdropduetoplaybackstalling.(d)OverallQoEateach
timeinstanceduringplayback. aredifferent.

| DUANMUetal.:QUALITY-OF-EXPERIENCEINDEXFORSTREAMINGVIDEO |     |     |     |     |     |     |     |     |     |     |     | 161 |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toestimatetheimpactofeachstallingeventontheQoE
Sk(t)=
|     |     |     |     |     | ⎧   | (cid:8) | (cid:2) | (cid:8) | (cid:9)(cid:3)(cid:9) |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | --------------------- | --- | --- | --- |
−
|     |     |     |     |     | ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ |         |         | t f     | i                        |     |         | +     |
| --- | --- | --- | --- | --- | ---------- | ------- | ------- | ------- | ------------------------ | --- | ------- | ----- |
|     |     |     |     |     | P          | −1+exp  | −       |         | k                        |     | i k ≤t≤ | ik lk |
|     |     |     |     |     | ik −1      |         |         | T       |                          |     | f       | f     |
|     |     |     |     |     |            | (cid:8) | (cid:2) | (cid:8) | (cid:9) 0(cid:3) (cid:9) |     |         |       |
l
|     |     |     |     |     | P   | − 1 + | ex p − | k   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- |
ik − 1
|     |     |     |     |     | (cid:8) | (cid:2) (cid:8) |     | T (cid:9)0 | (cid:3)(cid:9) |     |     |     |
| --- | --- | --- | --- | --- | ------- | --------------- | --- | ---------- | -------------- | --- | --- | --- |
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
|     |     |     |     |     |       | tf  | − i | −l  |     |     |     |         |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ------- |
|     |     |     |     |     | · e x | p − | k   | k   |     |     |     | ik + lk |
t>
|     |     |     |     |     |     |     | T 1 |     |     |     |           | f   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
|     |     |     |     |     | 0   |     |     |     |     |     | otherwise |     |
(4)
|     |     |     |     |     | where f | is the frame | rate | in frames/second, |     |     | and T0, | T1 and |
| --- | --- | --- | --- | --- | ------- | ------------ | ---- | ----------------- | --- | --- | ------- | ------ |
Sk(t)representtherateofdissatisfaction,therelativestrength
ofmemoryandtheexperienceofthek-thstallingeventattime
|     |     |     |     |     | t,respectively.P |     | −1,thescalingcoefficientofthedecayfunc- |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
ik
|     |     |     |     |     | tion,has   | twofunctions:1)    |     | itreflects | theviewer |        | expectation   | to  |
| --- | --- | --- | --- | --- | ---------- | ------------------ | --- | ---------- | --------- | ------ | ------------- | --- |
|     |     |     |     |     | the future | video presentation |     | quality,   |           | and 2) | it normalizes | the |
stallingeffecttothesamescaleofVQAkernel.Thisformula-
| Fig.8. | MAEofQoEmodelsonstreamingvideoQoEdatabase. |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionisqualitativelyconsistentwiththerelationshipbetweenthe
twoQoEfactorsdiscussedintheprevioussection.Inaddition,
|     |     |     |     |     | since the | impact of | initial | buffering | and | stalling | are | different, |
| --- | --- | --- | --- | --- | --------- | --------- | ------- | --------- | --- | -------- | --- | ---------- |
First,weassignzeropenaltytotheframesbeforethestalling wehavetwosetsofparameters:{Tinit,Tinit}forinitialdelay
|     |     |     |     |     |     |     |     |     | 0   | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
occurswhenpeoplehavenotexperiencedanyinterruption.Sec- and{T0,T1 }forotherplaybackstallings,respectively.Wealso
ond, as a playback stalling starts, the level of dissatisfaction assumetheinitialexpectationP0 isaconstant.Inthisway,the
increases as the stalling goes on till playback resumes. The initialbufferingtimeisproportionaltothecumulatedexperience
| studyontheimpactofwaitingtimeonuserexperienceinqueu- |     |     |     |     | loss. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ingservices[48]hasalonghistoryfrombothaneconomicand The instant QoE drop due to stalling events is computed by
| a psychological | perspective, | and has been | recently | extended |     |     |     |     |     |     |     |     |
| --------------- | ------------ | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
aggregatingtheQoEdropcausedbyeachstallingeventandis
| toquantifytherelationshipbetweenQoEandQoSinadaptive |                       |               |             |               | givenby |     |     |     |     |     |     |     |
| --------------------------------------------------- | --------------------- | ------------- | ----------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| streaming                                           | [39]. The exponential | decay         | function    | has been suc- |         |     |     |     |     |     |     |     |
| cessfully used                                      | in previous           | studies [14], | [15], [39]. | The use of    |         |     |     |     |     |     |     |     |
(cid:10)N
exponential decay assumes an existence of QoE loss satura- S(t)= Sk(t) (5)
tiontothenumberandlengthofstalling,andlowtoleranceto
k=1
| jitters comparing | to the other | commonly | used | utility function |     |     |     |     |     |     |     |     |
| ----------------- | ------------ | -------- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
suchaslogarithmandsigmoid.HereweapproximatetheQoE whereN isthetotalnumberofstallingevents.
lossduetoastallingeventwithanexponentialdecayfunction
|     |     |     |     |     | An important | fact | we  | have learned |     | from | the previous | sub- |
| --- | --- | --- | --- | --- | ------------ | ---- | --- | ------------ | --- | ---- | ------------ | ---- |
similar to [14], [15], [39]. Third, QoE also depends on a be- jective study [27] is that the frequency of stalling negatively
haviouralhysteresis“aftereffect”[35].Inparticular,aprevious correlates with QoE for a streaming video of constant quality,
unpleasantviewingexperiencecausedbyastallingeventtends sufficientlength,andafixedtotallengthofstallingL.Although
to penalize the QoE in the future and thus affects the overall not explicitly defined in the expression, it can be shown that
QoE.Theextentofdissatisfactionstartstofadeoutatthemo-
|     |     |     |     |     | the effect | of stalling | frequency |     | can | be captured | by  | the pro- |
| --- | --- | --- | --- | --- | ---------- | ----------- | --------- | --- | --- | ----------- | --- | -------- |
mentofplaybackrecoverybecauseobserversstarttoforgetthe posedmodelwithadeliberateparameterselection.Toseethat,
annoyance. To model the decline of memory retention of the we first adopt the aforementioned test condition in [27] and
=C,whereC
bufferingevent,weemploytheHermannEbbinghausforgetting assumeP isapositiveconstant.Then,theend-
n
curve[49] of-process QoE of the proposed model is fully determined by
experiencelossofstalling,whichbecomesafunctionofstalling
(cid:2) (cid:3)
frequencyonly.WhenthetotallengthofstallingLisfixedand
t
M =exp − (3) assumeequallengthofeachindividualstall,thenthelengthof
T
eachstallisL/N,andthestallingfrequencyisinversepropor-
|     |     |     |     |     | tional to | the total | number | of stalls | N.  | Thus, | we only | need to |
| --- | --- | --- | --- | --- | --------- | --------- | ------ | --------- | --- | ----- | ------- | ------- |
checkwhetherthecumulatedQoEdropoveralltime
| whereM | isthememoryretention,T | istherelativestrengthof |     |     |     |     |     |     |     |     |     |     |
| ------ | ---------------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
memory,andtisthetimeinstance.
(cid:11)
|     |     |     |     | +l  |     |     | ∞   |     |     | L   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Assume that the k-th stalling event locates at [i k , i k k ], G(N)= S(t)dt, = =1,2,...,N
|                                                        |     |     |     |     |     |     |     | forl |     | ,k  |     | (6) |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
| wherel isthelengthofstall,apiecewisemodelisconstructed |     |     |     |     |     |     |     |      | k   | N   |     |     |
| k                                                      |     |     |     |     |     | −∞  |     |      |     |     |     |     |

162 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
ismonotonicallydecreasingwithrespecttoN.Bysubstituting TABLEIII
| (4)and(5)into(6),wecansimplifytheexpressionas |     |         |     |                  |                 |         |     |     |     | SQIPARAMETERS |     |     |     |     |
| --------------------------------------------- | --- | ------- | --- | ---------------- | --------------- | ------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
|                                               |     | (cid:2) |     | (cid:12) (cid:8) | (cid:9)(cid:13) | (cid:3) |     |     |     |               |     |     |     |     |
L
| G(N)=C(T1 |     | −T0 ) | Nexp | −   | −N  | −CL |     | Parameter |     |     | Description |     |     |     |
| --------- | --- | ----- | ---- | --- | --- | --- | --- | --------- | --- | --- | ----------- | --- | --- | --- |
NT0
|     |     |     |     |             |         |     |     | T0  | rateofdissatisfactioninstallingevent |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | ------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|     |     |     |     | ≥1,T0 >0,T1 | >0,L>0. |     |     | T1  | strengthofmemoryinstallingevent      |     |     |     |     |     |
forN
|     |     |     |     |     |     |     |     | T i n i t | r a t e  | o f di s sa ti sf | ac t i on in i n i ti | a l b u ff e ri ng   | e v e nt |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----------------- | --------------------- | -------------------- | -------- | --- |
|     |     |     |     |     |     | (7) |     | 0         |          |                   |                       |                      |          |     |
|     |     |     |     |     |     |     |     | T i n i t | s tr e n | g th o f m e      | m o r y in in i ti a  | l b u f fe r in g ev | e n t    |     |
1
|                 |     |     |                          |     |     |       |     | P0  | expectationoninitialqualityofthevideo |     |     |     |     |     |
| --------------- | --- | --- | ------------------------ | --- | --- | ----- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
| Letg(x)=xexp{−( |     | L   | )}−x,itisnothardtoverify |     |     | dg(x) |     |     |                                       |     |     |     |     |     |
<
|                                        |     | x T 0 |                              |     |      | d x    |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | ----- | ---------------------------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,∀x≥1.Therefore,t                     |     | h e   | modelisabletoimplicitlyaccou |     |      | n tfor |     |     |     |     |     |     |     |     |
| theeffectofstallingfrequencyaslongasT1 |     |       |                              |     | >T0. |        |     |     |     |     |     |     |     |     |
D. ImplementationDetails
| In addition, | we  | have | also learned | from | previous | subjective |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | ------------ | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
study [14] that the impact of stalling tends to saturate with Throughout the paper, the proposed SQI uses the following
|     |     |     |     |     |     |     |     |     | init | =2, | init =0.5, |     | =1, | =1.2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---------- | --- | --- | ---- |
the increase of the number of stalling events at a constant parameter settings: T 0 T 1 T0 T1
quality setting. Interestingly, with the independent and addi- and P0 =0.8·|(V(·)|, where |V(·)| is the dynamic range of
tive assumption, SQI is still able to predict that the overall adoptedVQAkernel,e.g.PSNRrangesfrom0toinfinity(inthe
QoEhasanexponential-likeresponseforeachadditionstalling actualcomputation,wesettherangeofPSNRto0–50);SSIM
event. To understand this, let us denote the video presenta- andMS-SSIMrangefrom−1to1;andSSIMplusrangesfrom
tion quality of each frame/segment, the length of static video 0to100.Thesevaluesaresomewhatarbitrary,butwefindthat
in seconds, the duration of each stalling events, the number inourcurrentexperiments,theperformanceoftheSQIisfairly
P T, T N, insensitivetovariationsofT init,T init,T0 andT1 atleastwithin
| of stalling | events, | and the | overall | QoE by | n , | s , and |     |     |     | 0   | 1   |     |     |     |
| ----------- | ------- | ------- | ------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Q, respectively. In [14], the authors performed their subjec- an order of magnitude of the parameter values. P0 is rather
tive study with a constant quality setting, i.e., P =P. Ac- insensitivefrom0.5|(V(·)|(Xue’s[21]selection)to|(V(·)|.The
n
cording to (2), the video presentation quality that caused by parametersaresummarizedintheTableIII.Notethattheinitial
thestallingevents changes fromP =P,∀n∈[0,T]toP = bufferingparametersdonothavetosatisfythestallingfrequency
|     |     |     |     | n   |     | n   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P,∀n∈[0,T +NT ].Accordingto(5),theoverallstallingex- becauseitcannotoccurmorethanonceinonesession.Inreal-
s
|     | NSk(T | ),∀k | ∈[1,N]. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
perience is Thus, the overall QoE can worldapplications,theproposedschememayincludetwostep
s
berepresentedasQ= (T+NTs )P+NSk (Ts ) computationsontheclientside.First,stallingeventsaredetected
|     |     |     | +   |      | .WeplotQwithre- |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | T   | NT s |                 |     |     |     |     |     |     |     |     |     |
spect to N on a 5-point abso lu te ca tegory rating (ACR) scale in the video player. A straightforward way to detect stalling
in Fig. 4, where it can be observed that the influence of each events is to inspect the player progress every x milliseconds,
e.g.50.Iftheplayerhasnotadvancedasmuchasitisexpected
additionalstallingeventfollowsanexponential-likedecreasing
patterninSQI. to, then we can infer a stalling has occurred. By taking the
|     |     |     |     |     |     |     | difference | between | the | expected | progress | and actual | progress, |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | -------- | -------- | ---------- | --------- | --- |
Inreal-worldapplications,tomeasuretheimpactofstalling
atindividualframes,weconvertthecontinuousfunctionin(5) thedurationandfrequencyofstallingcanbemeasuredreliably.
intoitsdiscreteformbysamplingthefunctionateachdiscrete Inthesecondstep,whichisonlynecessaryintheapplications
thatrequireanend-of-processscore,isthecomputationofthe
timeinstancen:
|     |     |     | (cid:8) | (cid:9) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
QoEcumulation.Bothstepsdemandminimumcomputationand
n
S =S . (8) can be updated in real time. Moreover, the instantaneous QoE
n
f
|               |     |     |     |     |     |     | prediction      | is        | a valuable | property   | for many | applications |           | such |
| ------------- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ---------- | ---------- | -------- | ------------ | --------- | ---- |
|               |     |     |     |     |     |     | as live         | streaming | quality    | monitoring | and      | adaptive     | streaming |      |
| C. OverallQoE |     |     |     |     |     |     | decisionmaking. |           |            |            |          |              |           |      |
TheinstantaneousQoEateachtimeunitninthestreaming
sessioncanberepresentedastheaggregationofthetwochannels V. VALIDATION
|     |     |     | =P  | +S  |     |     | Tothebestofourknowledge,thereisnoothersubject-rated |           |       |          |      |                    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --------- | ----- | -------- | ---- | ------------------ | --- | --- |
|     |     | Q   | n n | n . |     | (9) |                                                     |           |       |          |      |                    |     |     |
|     |     |     |     |     |     |     | publicly                                            | available | video | database | that | have a combination |     | of  |
Inpractice,oneusuallyrequiresasingleend-of-processQoE compression distortion, initial buffering, and stalling events.
measure.WeusethemeanvalueofthepredictedQoEoverthe Thus, we validate SQI model using the streaming video QoE
wholeplaybackdurationtoevaluatetheoverallQoE.Toreduce databasedescribedinSectionIIIandcompareitsperformance
thememoryusage,theend-of-processQoEcanbecomputedin againsteightexistingobjective QoE models.Among theeight
amovingaveragefashion
QoEmodels,fourVQAalgorithmsincludingPSNR,SSIM[8],
|     |     |     |        |     |     |     | MS-SSIM[9]andSSIMplus[12],areemployed |     |     |     |     |     | astheframe- |     |
| --- | --- | --- | ------ | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
|     |     |     | (n−1)A | +Q  |     |     |                                       |     |     |     |     |     |             |     |
= n−1 n level video presentation quality measures. They also provide
|     |     | A n |     |     |     | (10) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
n
|     |     |     |     |     |     |     | useful | baseline | comparisons. |     | PLCC, SRCC | and | MAE are | cal- |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------------ | --- | ---------- | --- | ------- | ---- |
where A is the cumulative QoE up to the n-th time instance culated to evaluate the performance of all QoE models. The
n
in the streaming session. An example of each channel and the performance comparison results are provided in Figs. 6–8, re-
finaloutputofthemodelisillustratedinFig.5. spectively.Itcanbeseenthattheproposedmethoddeliversthe

DUANMUetal.:QUALITY-OF-EXPERIENCEINDEXFORSTREAMINGVIDEO 163
Fig.9. PredictedQoEversusMOS.
bestperformanceinpredictingsubjectiveQoEonthestreaming models. It is obvious that a higher compactness in the scatter
video QoE database with both compression and frame-freeze plotsisachievedbyapplyingtheproposedmodel,whichadds
impairment. properpenaltiesforinitialbufferingandstallinginadditionto
Fig.9showsthescatterplotsoftheMOSpredictionresultsfor the presentation quality impairment. Second, the best perfor-
eachQoEmodel.TheexistingQoEmodels,presentationVQA manceisobtainedbycombiningtheproposedmethodwiththe
quality with and without incorporating the proposed methods SSIMplus[12]VQAmodel.
are listed in the first, second and third columns, respectively. Toascertain thattheimprovement of theproposed model is
We have two observations here. First, the proposed SQI mod- statistically significant, we carry out a statistical significance
els significantly outperform their baseline presentation VQA analysis by following the approach introduced in [46]. First, a

164 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
TABLEIV
STATISTICALSIGNIFICANCEMATRIXBASEDONF-STATISTICSONTHESTREAMINGVIDEOQOEDATABASE
FTW Mok’s VsQM Xue’s PSNR SSIM MS-SSIM SSIMplus SQI- SQI- SQI- SQI-
[15] [40] [17] [21] [8] [9] [12] PSNR SSIM MS-SSIM SSIMplus
FTW[15] - - - 0 0 0 0 0 0 0 0 0
Mok’s[40] - - - 0 0 0 0 0 0 0 0 0
VsQM[17] - - - 0 0 0 0 0 0 0 0 0
Xue’s [21] 1 1 1 - 1 - - - 1 0 0 0
PSNR 1 1 1 0 - 0 0 0 - 0 0 0
SSIM[8] 1 1 1 - 1 - - - 1 0 - 0
MS-SSIM[9] 1 1 1 - 1 - - - 1 0 0 0
SSIMplus[12] 1 1 1 - 1 - - - 1 0 - 0
SQI-PSNR 1 1 1 0 - 0 0 0 - 0 0 0
SQI-SSIM 1 1 1 1 1 1 1 1 1 - - -
SQI-MS-SSIM 1 1 1 1 1 - 1 - 1 - - -
SQI-SSIMplus 1 1 1 1 1 1 1 1 1 - - -
Asymbol“1”meansthattheperformanceoftherowmodelisstatisticallybetterthanthatofthecolumnmodel,asymbol“0”meansthattherowmodelis
statisticallyworse,asymbol“-”meansthattherowandcolumnmodelsarestatisticallyindistinguishable.
nonlinear regression function is applied to map the objective furtherbycapturingtheinteractionsbetweenvideopresentation
qualityscorestopredictthesubjectivescores.Weobservethat qualityandtheimpactofstalling.
thepredictionresidualsallhavezero-mean,andthusthemodel
withlowervarianceisgenerallyconsideredbetterthantheone VI. CONCLUSIONSANDFUTUREWORK
with higher variance. We conduct a hypothesis testing using
We have presented a subjective study to understand human
F-statistics.Sincethenumberofsamplesexceeds50,theGaus-
visualQoEofstreamingvideoandproposedanobjectivemodel
sian assumption of the residuals approximately hold based on
to characterize the perceptual QoE. Our work represents one
the central limit theorem [50]. The test statistic is the ratio of
ofthefirstattemptstobridgethegapbetweenthepresentation
variances. The null hypothesis is that the prediction residuals
VQAandstalling-centricmodelsinQoEprediction.Thesubjec-
from one quality model come from the same distribution and
tive experiment reveals some interesting relationship between
are statistically indistinguishable (with 95% confidence) from
theimpactofstallingandtheinstantaneouspresentationquality.
the residuals from another model. After comparing every pos-
TheexperimentsalsodemonstratethattheproposedSQImodel
sible pairs of objective models, the results are summarized in
issimpleinexpressionandeffectiveinperformance.
Table IV, where a symbol ‘1’ means the row model performs
Futureresearchmaybecarriedoutinmanydirections.First,
significantlybetterthanthecolumnmodel,asymbol‘0’means
although we have tried our best to construct a database that
theopposite,andasymbol‘-’indicatesthattherowandcolumn
compriseasmanycontenttypeaspossible,theexperimentisby
models are statistically indistinguishable. It can be observed
no means exhaustive. A comprehensive subject-rated database
thatmostexistingQoEmodelsarestatisticallyindistinguishable
thatconsistsofmorecontenttypes,stallingpatternsandvideo
fromeachother,whiletheproposedmodelisstatisticallybetter
quality variations is desired to better understand the behaviors
thanallothermethodsonthestreamingvideoQoEdatabase.
ofhuman viewers and toexamine theperformance of existing
ItcanbeobservedfromtheexperimentsthattheQoS-based
objectiveQoEmethods.Second,howtoquantifytheinfluence
QoEmodels[15],[17],[40]donotperformwellonthedatabase.
ofthesemanticsofstallingposition,andhowtoincorporateit
The major reason is that QoS-based models (i.e., FTW [15],
intoQoEmodelsshouldbestudied.Third,howtoquantifythe
Mok’s[40],andVsQM[17]),donottakethepresentationqual-
quality switching experience and itspossible interactions with
ity of the videos into consideration except for their bitrates. A
other QoE influencing factors needs to be exploited. Fourth,
common“mistake”istoequatebitratewithquality,orassume
how to integrate the QoE model into the adaptive streaming
a constant bitrate implies a constant presentation quality. This
decisionmakingengineforoptimalplaybackcontrolisanother
ishighlyproblematicbecausevideoscodedatthesamebitrate
challengingproblemthatisworthfurtherinvestigations.
butofdifferentcontentcouldhavedrasticallydifferentpresen-
tationquality.ThisisoftenthemostdominantQoEfactor,and
in many cases all other factors (such as stalling) become only REFERENCES
secondary. Indeed, this is quite apparent from our test results,
[1] Apple Inc., “HTTP live streaming technical overview 2013,” [On-
where even PSNR, a very crude presentation quality measure line]. Available: https://developer.apple.com/library/ios/documentation/
thatdoesnottakeintoaccountanyinitialbufferingorstallingat networkinginternet/conceptual/streamingmediaguide/Introduction/Introd
uction.html,AccessedFeb.15,2015.
all, performs significantly better than QoS-based methods that
[2] A. Zambelli, “Smooth streaming technical overview,” [Online].
ignore presentation quality. By contrast, the proposed method Available:http://www.iis.net/learn/media/on-demand-smooth-streaming/
not only builds upon the most advanced presentation quality smoothstreamingtechnical-overview,AccessedFeb.15,2015.
[3] Adobe Systems Inc., “HTTP dynamic streaming 2013,” [Online].
model(e.g.,SSIMplus,whichhasbeenshowntobemuchbet-
Available:http://www.adobe.com/products/hds-dynamic-streaming.html,
ter than PSNR and other VQA measures), but moves one step AccessedFeb.15,2015.

DUANMUetal.:QUALITY-OF-EXPERIENCEINDEXFORSTREAMINGVIDEO 165
[4] DASHIndustryForum,“ForpromotionofMPEG-DASH2013,”[Online]. [27] A. K. Moorthy, L. K. Choi, A. C. Bovik, and G. De Veciana, “Video
Available:http://dashif.org,AccessedFeb.12,2015. qualityassessmentonmobiledevices:Subjective,behavioralandobjective
[5] T.Stockhammer,“Dynamicadaptivestreamingoverhttp–:Standardsand studies,”IEEEJ.Sel.TopicsSignalProcess.,vol.6,no.6,pp.652–671,
designprinciples,”inProc.ACMConf.MultimediaSyst.,2011,pp.133– Oct.2012.
144. [28] N.Staelens etal.,“AssessingqualityofexperienceofIPTVandvideo
[6] “Cisco IBSG Youth Focus Group, Cisco IBSG youth sur- ondemandservicesinreal-lifeenvironments,”IEEETrans.Broadcast.,
vey,”[Online].Available:http://www.cisco.com/c/dam/en_us/about/ac79/ vol.56,no.4,pp.458–466,Dec.2010.
docs/ppt/Video_Disruption_SP_Strategies_IBSG.pdf,AccessedJan.12, [29] A.Floris,L.Atzori,G.Ginesu,andD.Giusto,“QoEassessmentofmul-
2015. timediavideoconsumptionontabletdevices,”inProc.IEEEGlobecom
[7] Conviva Inc., “Viewer experience report,” 2013. [Online]. Available: Workshops,Dec.2012,pp.1329–1334.
http://www.conviva.com/conviva-customer-survey-reports/ott-beyond-en [30] L.Atzori,A.Floris,G.Ginesu,andD.D.Giusto,“Qualityperception
tertainment-csr/,AccessedJan.15,2015. whenstreamingvideoontabletdevices,”J.VisualCommun.ImageRep-
[8] Z.Wang,A.Bovik,H.Sheikh,andE.Simoncelli,“Imagequalityassess- resentation,vol.25,no.3,pp.586–595,Apr.2014.
ment:Fromerrorvisibilitytostructuralsimilarity,”IEEETrans.Image [31] T.Hoßfeld,S.Egger,R.Schatz,M.Fiedler,K.Masuch,andC.Lorentzen,
Process.,vol.13,no.4,pp.600–612,Apr.2004. “Initialdelayversusinterruptions:Betweenthedevilandthedeepblue
[9] Z.Wang,E.P.Simoncelli,andA.C.Bovik,“Multiscalestructuralsimilar- sea,”inProc.IEEEInt.Conf.QualityMultimediaExpo.,Jul.2012,pp.
ityforimagequalityassessment,”inProc.IEEEAsilomarConf.Signals, 1–6.
Syst.Comput.,Nov.2003,vol.2,pp.1398–1402. [32] A.Sackl,S.Egger,andR.Schatz,“Where’sthemusic?comparingthe
[10] K. Seshadrinathan and A. Bovik, “Motion tuned spatio-temporal qual- QoEimpactoftemporalimpairmentsbetweenmusicandvideostream-
ityassessmentofnaturalvideos,”IEEETrans.ImageProcess.,vol.19, ing,” in Proc. IEEE Int. Conf. Quality Multimedia Expo., Jul. 2013,
no.2,pp.335–350,Feb.2010. pp.64–69.
[11] M. Pinson and S. Wolf, “A new standardized method for objectively [33] E.SebastianandR.Alexander,QualityandQualityofExperience.New
measuring video quality,” IEEE Trans. Broadcasting, vol. 50, no. 3, York,NY,USA:Springer-Verlag,Jan.2014.
pp.312–322,Sep.2004. [34] M.Garcia,D.Dytko,andA.Raake,“Qualityimpactduetoinitialloading,
[12] A. Rehman, K. Zeng, and Z. Wang, “Display device-adapted video stalling,andvideobitrateinprogressivedownloadvideoservices,”inProc.
Quality-of-Experienceassessment,”inProc.SPIE,Feb.2015,vol.9394, IEEEInt.Conf.MultimediaExpo.,Sep.2014,pp.129–134.
pp.939406–939406. [35] K. Seshadrinathan and A. Bovik, “Temporal hysteresis model of time
[13] K. Watanabe, J. Okamoto, and T. Kurita, “Objective video quality as- varyingsubjectivevideoquality,”inProc.IEEEInt.Conf.Acoust.,Speech,
sessmentmethodforevaluatingeffectsoffreezedistortioninarbitrary SignalProcess.,May2011,pp.1153–1156.
videoscenes,”inProc.Electron.Imag.Int.Soc.Opt.Photon.,Jan.2007, [36] Z.WangandA.C.Bovik,“Meansquarederror:Loveitorleaveit?a
pp.64940–64940. newlookatsignalfidelitymeasures,”IEEESignalProcess.Mag.,vol.26,
[14] T.Hoßfeld,M.Seufert,M.Hirth,T.Zinner,P.Tran-Gia,andR.Schatz, no.1,pp.98–117,Jan.2009.
“QuantificationofYouTubeQoEviacrowdsourcing,”inProc.IEEEInt. [37] Z.Wang,H.R.Sheikh,andA.C.Bovik,“Objectivevideoqualityassess-
Sym.Multimedia,Dec.2011,pp.494–499. ment,”inTheHandbookofVideoDatabases:DesignandApplications.
[15] T.Hoßfeld,R.Schatz,E.Biersack,andL.Plissonneau,“Internetvideo BocaRaton,FL,USA:CRCPress,Sep.2003.
deliveryinYouTube:Fromtrafficmeasurementstoqualityofexperience,” [38] Z.WangandA.C.Bovik,“Modernimagequalityassessment,”Synthesis
inDataTrafficMonitoringAnal.,Jan.2013,pp.264–301. LecturesImage,Video,MultimediaProcess.,vol.2,no.1,pp.1–156,Dec.
[16] O. Oyman and S. Singh, “Quality of experience for HTTP adaptive 2006.
streamingservices,”IEEEComm.Mag.,vol.50,no.4,pp.20–27,Apr. [39] M.Fiedler,T.Hoßfeld,andP.Tran-Gia,“Agenericquantitativerelation-
2012. shipbetweenqualityofexperienceandqualityofservice,”IEEENetw.,
[17] D.Rodriguez,J.Abrahao,D.Begazo,R.Rosa,andG.Bressan,“Quality vol.24,no.2,pp.36–41,Mar.2010.
metrictoassessvideostreamingserviceoverTCPconsideringtemporal [40] R.Mok,E.Chan,andR.Chang,“Measuringthequalityofexperienceof
location of pauses,” IEEE Trans. Consumer Electron., vol. 58, no. 3, HTTPvideostreaming,”inProc.IFIP/IEEEInt.Symp.IntegratedNetw.
pp.985–992,Aug.2012. Manage.,May2011,pp.485–492.
[18] H.Yeganeh,R.Kordasiewicz,M.Gallant,D.Ghadiyaram,andA.Bovik, [41] E.Gelenbe,“Randomneuralnetworkswithnegativeandpositivesignals
“DeliveryqualityscoremodelforInternetvideo,”inProc.IEEEInt.Conf. andproductformsolution,”NeuralComput.,vol.1,no.4,pp.502–510,
ImageProc.,Oct.2014,pp.2007–2011. Aug.1989.
[19] D. Ghadiyaram, J. Pan, and A. C. Bovik, “A time-varying subjective [42] P.Fro¨hlich,S.Egger,R.Schatz,M.Mu¨hlegger,K.Masuch,andB.Gardlo,
qualitymodelformobilestreamingvideoswithstallingevents,”inProc. “QoEin10s:Areshortvideocliplengthssufficientforqualityofexpe-
SPIE,Sep.2015,vol.9599,pp.959911–959911. rienceassessment?”inProc.IEEEInt.Conf.QualityMultimediaExpo.,
[20] K. D. Singh, Y. Hadjadj-Aoul, and G. Rubino, “Quality of experience Jul.2012,pp.242–247.
estimationforadaptiveHTTP/TCPvideostreamingusingH.264/AVC,” [43] ITU-R BT.500-12, “Recommendation: Methodology for the subjective
inProc.IEEEInt.Conf.Consum.Commun.Netw.,Jan.2012,pp.127– assessmentofthequalityoftelevisionpictures,”Nov.1993.
131. [44] K. Seshadrinathan, R. Soundararajan, A. C. Bovik, and L. K. Cor-
[21] J. Xue, D.-Q. Zhang, H. Yu, and C. W. Chen, “Assessing quality of mack,“Studyofsubjectiveandobjectivequalityassessmentofvideo,”
experienceforadaptiveHTTPvideostreaming,”inProc.IEEEInt.Conf. IEEE Trans. Image Process., vol. 19, no. 6, pp. 1427–1441, Jun.
MultimediaExpo.,Jul.2014,pp.1–6. 2010.
[22] R. R. Pastrana-Vidal and J.-C. Gicquel, “A no-reference video quality [45] VQEG,“Finalreportfromthevideoqualityexpertsgrouponthevalidation
metric based on a human assessment model,” in Proc. Int. Workshop ofobjectivemodelsofvideoqualityassessment,”Apr.2000.[Online].
VideoProcess.QualityMetricsConsum.Electron.,Jan.2007. Available:http://www.vqeg.org/
[23] M. Seufert, S. Egger, M. Slanina, T. Zinner, T. Hobfeld, and P. Tran- [46] H.R.Sheikh,M.F.Sabir,andA.C.Bovik,“Astatisticalevaluationof
Gia, “A survey on quality of experience of HTTP adaptive stream- recentfullreferenceimagequalityassessmentalgorithms,”IEEETrans.
ing,” IEEE Commun. Surveys Tut., vol. 17, no. 1, pp. 469–492, Sep. ImageProcess.,vol.15,no.11,pp.3440–3451,Nov.2006.
2014. [47] InformationtechnologyMPEGsystemstechnologies:Carriageoftimed
[24] M.-N.Garcia etal.,“QualityofexperienceandHTTPadaptivestream- metadatametricsofmediainISObasemediafileformat,ISO/IEC23001-
ing: A review of subjective studies,” in Proc. IEEE Int. Conf. Quality 10,Sep.2015.
MultimediaExp.,Sep.2014,pp.141–146. [48] P.Kumar,M.U. Kalwani, andM.Dada, “Theimpactofwaiting time
[25] R.R.Pastrana-Vidal,J.C.Gicquel,C.Colomes,andH.Cherifi,“Sporadic guaranteesoncustomers’waitingexperiences,”MarketingSci.,vol.16,
framedroppingimpactonqualityperception,”inProc.SPIE,Jan.2004, no.4,pp.295–314,Nov.1997.
vol.5292,pp.182–193. [49] H. Ebbinghaus, Memory: A Contribution to Experimental Psychology.
[26] Y.QiandM.Dai,“Theeffectofframefreezingandframeskippingon NewYork,NY,USA:Teacherscollege,ColumbiaUniversity,Oct.1913.
videoquality,”inProc.IEEEInt.Conf.Intell.Inform.HidingMultimedia [50] D.C.Montgomery,AppliedStatisticsandProbabilityforEngineers,6th
SignalProcess.,Dec.2006,pp.423–426. ed.NewYork,NY,USA:Wiley,2013.

166 IEEEJOURNALOFSELECTEDTOPICSINSIGNALPROCESSING,VOL.11,NO.1,FEBRUARY2017
ZhengfangDuanmu(S’15)receivedtheB.A.Scde- AbdulRehmanreceivedtheMastersdegreeincom-
gree in electrical and computer engineering from municationsengineeringfromTechnicalUniversity
theUniversityofWaterloo,Waterloo,ON,Canada, Munich,Germany,andthePh.D.degreeininforma-
in 2015, where he is currently working toward the tionandcommunicationsystemsfromtheUniversity
M.A.Scdegreeinelectricalandcomputerengineer- of Waterloo, Canada. He is currently the President
ing. His research interest lies in perceptual image & CEO of SSIMWave, a company, he co-founded
processingandqualityofexperience. in2013,dedicatedtodeliveringexcellenceinvisual
quality-of-experience.Heleadsthedevelopmentof
SSIMWavesstate-of-the-artvideoQoEmeasurement
andoptimizationproductsgearedtowardsthemedia,
communication,andentertainmentindustry.Hisre-
searchinterestsincludeimageandvideoprocessing,codingandqualityassess-
ment,andmultimediacommunications.
KaiZengreceivedthePh.D.degreeinelectricaland
ZhouWang(S’99–M’02–SM’12–F’14)receivedthe
computerengineeringfromUniversityofWaterloo,
Ph.D.degreefromtheUniversityofTexasatAustin,
Waterloo,ON,Canada,in2013,whereheiscurrently
Austin, TX, USA, in 2001. He is currently a Pro-
aPost-DoctoralFellow.Hisresearchinterestsinclude
fessorintheDepartmentofElectricalandComputer
computationalvideoandimagecommunicationand
Engineering,UniversityofWaterloo,Canada.Hisre-
processing.Dr.ZengreceivedtheIEEESignalPro-
search interests include image processing, coding,
cessingSocietystudenttravelgrantin2010and2012,
and quality assessment; computational vision and
andtheprestigious2013ChineseGovernmentAward
pattern analysis; multimedia communications; and
forOutstandingStudentsAbroad.
biomedicalsignalprocessing.Hehasmorethan100
publicationsinthesefieldswithmorethan30000ci-
tations(GoogleScholar).Dr.WangservesasaSenior
AreaEditorofIEEETRANSACTIONSONIMAGEPROCESSING(2015-present),and
anAssociateEditorofIEEETRANSACTIONSONCIRCUITSANDSYSTEMSFOR
VIDEO TECHNOLOGY (2016-present). Previously, he served as a Member of
IEEEMultimediaSignalProcessingTechnicalCommittee(2013–2015),anAs-
sociateEditorofIEEETRANSACTIONSONIMAGEPROCESSING(2009–2014),
KedeMa(S’13)receivedtheB.E.degreefromthe
Pattern Recognition (2006-present) and IEEE SIGNAL PROCESSING LETTERS
University of Science and Technology of China,
(2006–2010),andaGuestEditorofIEEEJOURNALOFSELECTEDTOPICSIN
Hefei,China,in2012,andtheM.A.Sc.degreefrom
SIGNALPROCESSING(2013–2014and2007–2009),EURASIPJournalofImage
theUniversityofWaterloo,Waterloo,ON,Canada,
andVideoProcessing(2009–2010),andSignal,ImageandVideoProcessing
where he is currently working toward the Ph.D.
(2011–2013).HeisaFellowofCanadianAcademyofEngineering,andhavere-
degree in electrical and computer engineering. His
ceivedthe2015PrimetimeEngineeringEmmyAward,the2014NSERCE.W.R.
researchinterestliesinperceptualimageprocessing.
SteacieMemorialFellowshipAward,the2013IEEESignalProcessingMaga-
zineBestPaperAward,the2009IEEESignalProcessingSocietyBestPaper
Award,the2009OntarioEarlyResearcherAward,andtheICIP2008IBMBest
StudentPaperAward(asSeniorAuthor).