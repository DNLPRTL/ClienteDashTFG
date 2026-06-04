Received13July2025,accepted30July2025,dateofpublication8August2025,dateofcurrentversion12September2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3597058
QoE-Driven Adaptive Video Streaming:
Architectures, Techniques, and Future Research
Challenges Toward 6G Networks
MONERALSADER1,(Member,IEEE),ALCARDOALEXBARAKABITZE2,3,(Member,IEEE),
ANDIS-HAKAMKWAWA4,(Member,IEEE)
1CollegeofComputingandInformatics,SaudiElectronicUniversity,Riyadh13316,SaudiArabia
2SchoolofComputerScienceandInformationTechnology,UniversityCollegeCork,Cork,T12K8AFIreland
3DepartmentsofInformaticsandIT,SUA,Morogoro,Tanzania
4SchoolofEngineering,ComputingandMathematics,UniversityofPlymouth,PL48AAPlymouth,U.K.
Correspondingauthors:AlcardoAlexBarakabitze(alcardo.barakabitze@ucc.ie)andMonerAlsader(m.alsader@seu.edu.sa)
ThisworkwassupportedinpartbytheCollegeofComputingandInformatics,SaudiElectronicsUniversity;inpartbyEuropeanUnion’s
Horizon2020ResearchandInnovationProgramundertheMarieSkłodowska-CurieunderGrant801522;inpartbytheScience
FoundationIrelandandco-fundedbyEuropeanRegionalDevelopmentFundthroughtheCentreforDigitalContentPlatformResearch
(ADAPT)CentreforDigitalContentTechnologyunderGrant13/RC/2106;andinpartbytheRoyalAcademyofEngineering,U.K.,
throughtheDistinguishedInternationalAssociatesProgramRound4:2024-2025.
ABSTRACT The paper provides a survey of architectures and techniques for QoE-driven adaptive video
streaming services based on two (2) classifications: client-based video streaming, and delivery-based
video rate adaptation. The paper presents in-depth review of QoE- driven network softwarization and
virtualization approaches using SDN, NFV, and MEC, leveraging AI/ML techniques and cloud/edge
computingarchitectures.Additionally,thepaperprovidesareviewofQoE-drivenvideostreaminginvarious
aspectsincluding6G-basedMetaverseforMulti-UserExtendedReality(MER),holographictelepresence,
personalized media, Internet of Senses (IoS), Industrial Internet of Things (IIoT) and video coding
compressionstandards.Moreover,thepaperprovidehighlightsonmultimediastreaminginnewverticalsand
next-generationmobiletechnologiesbyputtingemphasisin6Gandbeyondfactories,education,socialand
entertainment,automotiveandhealthcare.Finally,thepaperpresentconcretechallengesandfutureresearch
directions in emerging applications, video standards and new business cases towards 6G networks. This
paperaimstoguideandinspirethemultimediaandnetworkingresearchcommunitybothinacademiaand
industrytowarddevelopinginnovativesolutionsformonitoring,managing,andoptimizingperformancein
future6Gnetworks.
INDEXTERMS Metaverse,videoQoE,multimediastreamingservices,networkslicing,SDN/NFV,5G/6G,
industrialIoT,networksoftwarization,networkmanagement,holographicstreaming,AR/VR.
I. INTRODUCTION high-qualityvideosourcesaswellasrobustassurancesfrom
Forecasts suggest that by 2026, the global count of 5G networkoperatorsregardingoptimalnetworkservicequality.
subscribersisexpectedtosurpass2.5billion,withstreaming For streaming service providers, accurately and efficiently
services accounting for over 70% of the total service monitoring the video Quality of Experience (QoE) of their
traffic[1].Thisexpansioninthetelecommunicationsmarket subscribers is crucial. The monitoring and management is
isaccompaniedbyasignificantshiftinconsumerpreferences essential for these providers to expand their customer base
and demands, especially in the streaming services sector. andachievesignificantbenefits[2].
The demand for video streaming services necessitates
A. MOTIVATIONANDOPENQUESTIONS
The associate editor coordinating the review of this manuscript and Therapidgrowthinmultimediacontentconsumption,driven
approvingitforpublicationwasJadNasreddine . by the proliferation of mobile devices and high-speed
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
157408 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
internet,motivatestheneedformoreefficientstreamingsolu- numeroussurveysfocusingonQualityofExperience(QoE)-
tions.TheshifttowardsUHDcontent,AR/VRapplications, driven solutions [2], [3], [6], [7], [8], [9], [10], [11]. These
and live streaming services requires innovations in network surveys cover various aspects of streaming architectures,
infrastructuretohandletheincreaseddemand.Additionally, deliverymechanisms,andQoEmodeling.However,acritical
asuserexpectationsforseamlessandhigh-qualitystreaming reviewrevealsthatmanyoftheseworkssufferfromlimited
experiences rise, there is a strong motivation to improve scope, fragmented perspectives, or a lack of alignment
adaptive streaming techniques, reduce latency, and ensure with the emerging needs of 6G networks and immersive
consistentQoSacrossdiversenetworkenvironments[2],[3], multimediaapplications.
[4]. The evolution of network infrastructure technologies For instance, Huang et al. [11] present a focused survey
(SDN,NFV,MECandOpen-RAN),particularly5Gandthe on video streaming in next-generation vehicular networks.
upcoming6G,presentsanopportunitytorethinkmultimedia Their work examines video processing technologies, wire-
streaming architectures and solutions. The challenge lies in less communications, and network strategies that optimize
leveraging these advanced networks to deliver richer, more streaming under vehicular dynamics. While valuable for
immersive video experiences while maintaining efficiency automotive use cases, the study is context-specific and
and scalability. The need for real-time video interaction in does not generalize well to other 6G-driven multimedia
applications like video gaming, remote video collaboration, verticals. Moreover, it lacks an analytical taxonomy that
andtelemedicinefurtherdrivesresearchintoreducinglatency linksvehicularstreamingwithmulti-layerQoEoptimization
andenhancingstreamingreliability[5]. frameworks,andomitsdiscussionsonnetworksoftwarization
As we enter a new era of delivering next-generation technologies like SDN/NFV or Vehicular Edge Computing
multimedia services through 6G networks, several critical (VEC).
questions must be addressed to realize the full potential In contrast, Barakabitze et al. [3] provide an early but
of these systems [3], [5]. (a) What is the current state detailed survey on QoE management frameworks, with
of QoE-driven adaptive video streaming, particularly in a focus on software-defined networking (SDN), network
leveraging AI/ML, SDN/NFV, and cloud or multi-access functionvirtualization(NFV),multi-accessedgecomputing
edge computing technologies within the context of 6G (MEC),andimmersiveapplications.Theauthorsalsoexplore
architectures? (b) How can future softwarized 6G networks network support for augmented/virtual reality (AR/VR),
become service-aware and facilitate intelligent monitoring, mulsemedia, and cloud gaming. However, a key limitation
QoE optimization, and resource management that adapts of this study is its lack of explicit alignment with the
holisticallytouserdemands,datacontentcharacteristics,and evolving 5G and 6G multimedia ecosystems. For example,
dynamic network conditions? (c) What are the emerging next-generationvideocompressiontechniques,ultra-reliable
trends and state-of-the-art solutions in QoE-driven video low-latency communications (URLLC), and distributed AI
streaming for the metaverse, especially in applications such for personalized QoE management are not addressed. Fur-
as multi-user extended reality, holographic telepresence, thermore, while the survey touches on edge intelligence,
next-generation video compression standards, personalized it does not present a unified taxonomy for hybrid AI-based
media, and the Internet of Senses (IoS), all over 6G- and rule-based adaptation techniques under future network
enabledplatforms?(d)Whatarethefutureresearchdirections architectures.
and unresolved challenges in multimedia streaming for AnotherimportantcontributionisfromBarakabitzeetal.
immersivemediaexperiences,next-generationverticals,and [2], [12], who explore QoE provisioning mechanisms in
cloud/edge-based 3D streaming architectures within 6G softwarized 5G/6G networks. This work delves deeper into
ecosystems? theimplicationsofnetworkprogrammabilityandedge/cloud-
Furthermore, the integration of 6G with the Industrial native computing for end-user QoE. Nevertheless, it pri-
InternetofThings(IIoT)introducesadditionalopportunities marily concentrates on architectural enablers rather than
and complexities. 6G is expected to support ultra-reliable cross-layer adaptation techniques, multi-modal immersive
low-latency communication, massive machine-type com- services, or content-aware QoE estimation methods needed
munication, and enhanced mobile broadband, which are for future Metaverse and IoS environments. Nabajeet and
essential for real-time immersive media streaming, remote Maria[8]offerasurveyonQoEmodelingforHTTPAdaptive
industrialoperations,andcollaborativedigitaltwinenviron- Streaming (HAS), with an emphasis on subjective testing
ments.InvestigatinghowQoEcanbeeffectivelymanagedin and user-centric evaluation techniques. While this work is
suchdiverseanddynamicenvironments—particularlywhen methodologically sound, it lacks a broader architectural
intersecting with critical industrial applications—remains a perspectiveanddoesnotincorporaterecentadvancesinedge-
keyresearchfrontier. assistedHAS,AI-basedanalytics,ornetwork-assistedABR
(adaptivebitrate)algorithmsthatareincreasinglyrelevantin
5G/6Gdeployments.
B. RELATEDWORK Petrangeli et al. [9] provide a comprehensive review
To address several pressing challenges in adaptive video of QoE-aware adaptive streaming, particularly focusing
streaming, both academia and industry have produced on network- and server-assisted solutions, application-layer
VOLUME13,2025 157409

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
transportprotocols,andend-userperception.Yet,theirstudy efforts,andtheirrelevancetoQoEmanagementinemerging
does not reflect on dynamic resource allocation using AI, 6Ginfrastructures—areas.
| next-gen | encoding | standards |     | (e.g., | VVC, | AV1, | H.266), |     |     |     |     |     |     |     |     |
| -------- | -------- | --------- | --- | ------ | ---- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
orholographicand3Dmediastreaming,whichareessential
C. SCOPEANDCONTRIBUTIONSOFTHISPAPER
for interactive immersive experiences anticipated in the 6G Themainobjectiveofthisworkistoprovideacomprehensive
era.Similarly,Abdelhaketal.[13]proposeacategorization survey of taxonomy technologies, architectures and future
| of bitrate | adaptation |     | strategies | into | client-based, |     | server- |            |                |     |           |     |          |         |     |
| ---------- | ---------- | --- | ---------- | ---- | ------------- | --- | ------- | ---------- | -------------- | --- | --------- | --- | -------- | ------- | --- |
|            |            |     |            |      |               |     |         | challenges | for multimedia |     | streaming |     | services | towards | 6G  |
based, network-based, and server-network-assisted types. networks.Thecontributionsofthisworkconsistsoffour(4)
| While their | taxonomy |     | is practical |     | and widely |     | referenced, |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ------------ | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
parts.
itlacksincorporationofemerginghybridmodels(i.e.,AI+
|             |      |             |            |                |            |            |           | • The first   | part             | presents |              | a comprehensive |             | survey    | of    |
| ----------- | ---- | ----------- | ---------- | -------------- | ---------- | ---------- | --------- | ------------- | ---------------- | -------- | ------------ | --------------- | ----------- | --------- | ----- |
| heuristic), | does | not explore |            | QoE-predictive |            | feedback   | loops,    |               |                  |          |              |                 |             |           |       |
|             |      |             |            |                |            |            |           | architectures |                  | and      | techniques   | for             | QoE-driven  |           | adap- |
| and does    | not  | provide     | actionable |                | insights   | into       | streaming |               |                  |          |              |                 |             |           |       |
|             |      |             |            |                |            |            |           | tive video    | streaming        |          | services,    |                 | categorized | into      | two   |
| challenges  | in   | 6G-enabled  | verticals  |                | like smart | healthcare | or        |               |                  |          |              |                 |             |           |       |
|             |      |             |            |                |            |            |           | main          | classifications: |          | client-based |                 | video       | streaming | and   |
collaborativerobotics.
delivery-basedvideorateadaptation.Withintheclient-
| Vega       | et al. | [14] focus | on      | machine | learning-driven |     | QoE          |                   |           |     |               |      |          |               |     |
| ---------- | ------ | ---------- | ------- | ------- | --------------- | --- | ------------ | ----------------- | --------- | --- | ------------- | ---- | -------- | ------------- | --- |
|            |        |            |         |         |                 |     |              | based             | category, | we  | examine       | four | specific | approaches:   |     |
| prediction | and    | control    | models. | Their   | survey          | is  | particularly |                   |           |     |               |      |          |               |     |
|            |        |            |         |         |                 |     |              | throughput-based, |           |     | buffer-based, |      | caching  | and prefetch- |     |
relevantforpredictiveanalyticsbutofferslimiteddiscussion
|                   |               |                   |              |               |                   |          |            | ing, and        | hybrid   | methods.    |                | Additionally, |                | we provide    | an    |
| ----------------- | ------------- | ----------------- | ------------ | ------------- | ----------------- | -------- | ---------- | --------------- | -------- | ----------- | -------------- | ------------- | -------------- | ------------- | ----- |
| on system         | architecture, |                   | real-time    |               | learning          | at       | the edge,  |                 |          |             |                |               |                |               |       |
|                   |               |                   |              |               |                   |          |            | in-depth        | review   | of          | three types    | of            | delivery-based |               | video |
| or integration    |               | into cross-domain |              | orchestration |                   |          | frameworks |                 |          |             |                |               |                |               |       |
|                   |               |                   |              |               |                   |          |            | rate adaptation |          | techniques: |                | (1)           | bitrate        | guidance      | and   |
| like SDN/NFV/MEC. |               |                   | Furthermore, |               | their             | emphasis | remains    |                 |          |             |                |               |                |               |       |
|                   |               |                   |              |               |                   |          |            | bandwidth       | shaping, |             | (2) in-network |               | video          | optimization, |       |
| on ML             | models        | without           | adequate     |               | contextualization |          | for        |                 |          |             |                |               |                |               |       |
and(3)transport-layervideooptimizationinMultiPath
| ultra-dense, | latency-sensitive |     |     | 6G use | cases. | Aroussi | and |     |     |     |     |     |     |     |     |
| ------------ | ----------------- | --- | --- | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TCP(MPTCP)-assistednetworks.
Mellouk[10]provideataxonomyofmachinelearning-based
|     |     |     |     |     |     |     |     | • The second |     | part | provides | an  | in-depth | review | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | -------- | --- | -------- | ------ | --- |
correlationmodelsforQoEbutsufferfromoutdatedassump-
|           |      |             |     |        |      |               |     | QoE-driven |     | network | softwarization |     | and | virtualization |     |
| --------- | ---- | ----------- | --- | ------ | ---- | ------------- | --- | ---------- | --- | ------- | -------------- | --- | --- | -------------- | --- |
| tions and | lack | discussions | on  | modern | deep | reinforcement |     |            |     |         |                |     |     |                |     |
approaches,includingSDN,NFV,andMEC,leveraging
| learning, | federated | learning, |     | or edge | inference, | all | of which |       |            |     |                |     |           |           |     |
| --------- | --------- | --------- | --- | ------- | ---------- | --- | -------- | ----- | ---------- | --- | -------------- | --- | --------- | --------- | --- |
|           |           |           |     |         |            |     |          | AI/ML | techniques |     | and cloud/edge |     | computing | architec- |     |
arekeytoscalableQoEoptimizationin6Gnetworks.Lastly,
tures.
| Sanaei | and Mostafavi |     | [15] review |     | SDN-based |     | frameworks |             |      |          |     |               |     |          |     |
| ------ | ------------- | --- | ----------- | --- | --------- | --- | ---------- | ----------- | ---- | -------- | --- | ------------- | --- | -------- | --- |
|        |               |     |             |     |           |     |            | • The third | part | presents | a   | comprehensive |     | overview | of  |
formultimediadelivery.Theirworkcontributestotheunder-
|          |                    |     |     |            |          |     |           | emerging | trends | and | technologies |     | shaping | multimedia |     |
| -------- | ------------------ | --- | --- | ---------- | -------- | --- | --------- | -------- | ------ | --- | ------------ | --- | ------- | ---------- | --- |
| standing | of programmability |     |     | in content | delivery |     | networks. |          |        |     |              |     |         |            |     |
servicesin6Gnetworks.Itexploresthetransformation
| However,         | it does | not     | address       | multi-cloud |     | orchestration,   |     |         |       |                 |     |         |          |             |         |
| ---------------- | ------- | ------- | ------------- | ----------- | --- | ---------------- | --- | ------- | ----- | --------------- | --- | ------- | -------- | ----------- | ------- |
|                  |         |         |               |             |     |                  |     | of DASH | video | streaming       |     | through | enhanced |             | service |
| blockchain-based |         | content | traceability, |             | or  | security/privacy |     |         |       |                 |     |         |          |             |         |
|                  |         |         |               |             |     |                  |     | quality | and   | business-driven |     | models, | the      | integration | of      |
concernsinreal-timeQoEmonitoring.
|          |        |      |     |         |          |            |     | advanced   | multimedia |     | formats      | such | as holographic |             | and |
| -------- | ------ | ---- | --- | ------- | -------- | ---------- | --- | ---------- | ---------- | --- | ------------ | ---- | -------------- | ----------- | --- |
| Our work | builds | upon | and | expands | existing | literature | by  |            |            |     |              |      |                |             |     |
|          |        |      |     |         |          |            |     | volumetric | content,   |     | personalized |      | media,         | theInternet | of  |
offeringaholisticandforward-lookingperspectiveonQoE-
|                 |     |           |               |              |        |             |           | Senses         | (IoS), | Industrial | Internet   |          | of Things | (IIoT),and |        |
| --------------- | --- | --------- | ------------- | ------------ | ------ | ----------- | --------- | -------------- | ------ | ---------- | ---------- | -------- | --------- | ---------- | ------ |
| driven adaptive |     | video     | streaming     | tailored     |        | to 6G       | networks. |                |        |            |            |          |           |            |        |
|                 |     |           |               |              |        |             |           | the enablement |        | of         | multi-user | extended |           | reality    | in the |
| Specifically,   | We  | integrate | architectural |              | trends |             | (SDN/NFV, |                |        |            |            |          |           |            |        |
|                 |     |           |               |              |        |             |           | 6G-powered     |        | metaverse. |            | The role | of        | blockchain | is     |
| MEC, ICN),      | QoE | modeling, |               | AI/ML-driven |        | prediction, | and       |                |        |            |            |          |           |            |        |
examinedforsecureanddecentralizedvideostreaming
| adaptation     | strategies |                  | within | a unified | framework. |     | Unlike     |               |     |       |     |                   |     |           |     |
| -------------- | ---------- | ---------------- | ------ | --------- | ---------- | --- | ---------- | ------------- | --- | ----- | --- | ----------------- | --- | --------- | --- |
|                |            |                  |        |           |            |     |            | transactions, |     | while | new | video compression |     | standards |     |
| prior surveys, |            | we contextualize |        | these     | within     | 6G  | multimedia |               |     |       |     |                   |     |           |     |
likeVVCandAI-drivencodecsarehighlightedfortheir
| verticals | (e.g., | Metaverse, | IoS, | XR, | autonomous |     | systems). |     |     |     |     |     |     |     |     |
| --------- | ------ | ---------- | ---- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
potentialtosupportultra-HDandimmersivemedia.
| We introduce |     | a hybrid | taxonomy | where |     | our proposed | tax- |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | -------- | ----- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
• Thefourthpartpresentsconcretechallengesandfuture
| onomy | distinguishes |     | between | client-based, |     | network-based, |     |          |            |     |             |     |                        |     |     |
| ----- | ------------- | --- | ------- | ------------- | --- | -------------- | --- | -------- | ---------- | --- | ----------- | --- | ---------------------- | --- | --- |
|       |               |     |         |               |     |                |     | research | directions |     | in emerging |     | applications/verticals |     |     |
AI-assisted,andhybridAI-rule-basedadaptationmodels,and
andnewbusinesscasestowards6Gnetworks.
| maps them | to  | corresponding |     | network | layers | and | functional |     |     |     |     |     |     |     |     |
| --------- | --- | ------------- | --- | ------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Webelievethatthisworkwillbeacatalystforthemultimedia
| components, | addressing |     | the | fragmented | taxonomies |     | in past |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | ---------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
work.Weidentifyunderexploredareassuchasreal-timeQoE and future networks research community from academia
optimization for holographic streaming, sustainable media and industry towards implementing novel approaches
|           |                        |     |     |      |           |     |            | regarding QoE | monitoring, |     | management, |     | and | performance |     |
| --------- | ---------------------- | --- | --- | ---- | --------- | --- | ---------- | ------------- | ----------- | --- | ----------- | --- | --- | ----------- | --- |
| delivery, | and privacy-preserving |     |     | edge | learning, |     | which have |               |             |     |             |     |     |             |     |
been overlooked in existing surveys. Moreover, we include optimizationinfuture6Gnetworks.
| comparative | analysis |     | tables | that summarizes |     | performance, |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ------ | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
applicability,andarchitecturalcomplexityofdifferentstrate- D. PAPERSTRUCTUREANDORGANIZATION
gies,fillingagapinpriorworkwhichoftenlackedstructured The structure of this paper is as follows. Section II reviews
comparisons. Our paper incorporate standardization and the state-of-the-art solutions for QoE-driven adaptive video
project trends where we discuss ongoing international streamingservices.SectionIIIdiscussesnetworksoftwariza-
initiatives(e.g.,Hexa-X,6GIC),IEEE/3GPPstandardization tionandvirtualizationapproachesthatareQoE-driven,with
| 157410 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE1. Asummaryofrelatedsurveypapers.
TABLE2. Listofcommonlyusedacronymsinthispaper.
a focus on AI/ML, cloud/edge computing, and SDN/NFV II. ATAXONOMY,ARCHITECTURESANDDESCRIPTION
architectures. Section IV outlines emerging trends and OFTECHNIQUESFORQOE-DRIVENADAPTIVEVIDEO
technologies in multimedia services for 6G networks. The STREAMING
key challenges and potential future research directions Thissectionprovidesacomprehensivesurveyoftaxonomy,
are addressed in Section V. Finally, Section VI provides architectures, and description of techniques for QoE-driven
concluding remarks. The overall structure and organization adaptive video streaming based on two (2) classifications:
of the paper are illustrated in Fig. 1, and Table 2 lists the client-based video streaming, and delivery-based video rate
acronymsfrequentlyusedthroughoutthepaper. adaptationasindicatedinFig.2.
VOLUME13,2025 157411

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
| FIGURE1. | Astructureandorganizationofthispaper. |     |     |     |     |     |             |            |           |        |          |             |           |
| -------- | ------------------------------------- | --- | --- | --- | --- | --- | ----------- | ---------- | --------- | ------ | -------- | ----------- | --------- |
|          |                                       |     |     |     |     |     | the expense | of         | others.   | While  | FESTIVE  | improves    | stability |
|          |                                       |     |     |     |     |     | by 50%,     | efficiency | by        | nearly | 10%, and | fairness    | by 40%,   |
|          |                                       |     |     |     |     |     | it does     | not ensure | bandwidth |        | fairness | for diverse | DASH      |
clientsusingthesameaccessnetwork.Yietal.[23]propose
aprediction-basedadaptationtechniquethatusesthroughput
predictiontoenhancevideoqualityforendusers.Theauthors
employaHiddenMarkovChain,adata-drivenmodel,topre-
dictbothinitialandmid-streamingthroughput.Experimental
|     |     |     |     |     |     |     | results [23] | show | that | the CS2P | method | outperforms | other |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---- | -------- | ------ | ----------- | ----- |
availablemethods,achievinga50%improvementinstartand
midstreamthroughputprediction.
Milleretal.[25]introduceLow-LatencyPrediction-Based
|     |     |     |     |     |     |     | Adaptation      | (LOLYPOP), |              | which     | calculates   | the         | probability |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ------------ | --------- | ------------ | ----------- | ----------- |
|     |     |     |     |     |     |     | of exceeding    |            | the playback |           | deadline     | for various | video       |
|     |     |     |     |     |     |     | representations |            | and selects  |           | the one with | the highest | bitrate     |
|     |     |     |     |     |     |     | that can        | still meet | the          | deadline. | To achieve   | this,       | LOLYPOP     |
FIGURE2. ClassificationsofQoE-drivenadaptivevideostreaminginthe
scopeofthispaper. utilizesTCPthroughputpredictionsovermultipletimescales
|     |     |     |     |     |     |     | (ranging | from | 1 to | 10 seconds) | along | with | an estimate |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---- | ----------- | ----- | ---- | ----------- |
A. CLIENT-BASEDVIDEOSTREAMING of the relative prediction error distribution. In low-latency
1) THROUGHPUT-BASEDVIDEOSTREAMING scenarios, traditional bandwidth prediction methods may
Throughput-based video streaming enhances the user expe- not be suitable due to shorter time intervals between
|                       |     |           |       |         |     |         | chunks. | Bentaleb | et  | al. [24] | address | the challenges | of  |
| --------------------- | --- | --------- | ----- | ------- | --- | ------- | ------- | -------- | --- | -------- | ------- | -------------- | --- |
| rience by dynamically |     | adjusting | video | quality | and | bitrate |         |          |     |          |         |                |     |
based on real-time network conditions, thereby ensuring bandwidth prediction in chunked streaming, such as the
smooth playback and minimizing buffering. As network limited observation window, rapid fluctuations in network
performance improves, the streaming client can request conditions, and the need for accurate predictions to ensure
higher-quality video segments; conversely, it downgrades smooth streaming. They present ABR for chunked transfer
|             |                 |     |              |     |       |         | encoding | as an | effective | adaptation | scheme | for | live video |
| ----------- | --------------- | --- | ------------ | --- | ----- | ------- | -------- | ----- | --------- | ---------- | ------ | --- | ---------- |
| the quality | when conditions |     | deteriorate, | as  | shown | in pre- |          |       |           |            |        |     |            |
vious studies [20], [21], [22], [23], [24]. To address these streaming, considering the idle time between consecutive
limitations, Junchen et al. [21] introduced FESTIVE— chunks.ExperimentalresultsshowthatACTEachievesahigh
a Fair, Efficient, and Stable adapTIVE video streaming bandwidthmeasurementaccuracyof96%,leadingtoa65%
Environment.Thisapproachaimstoenhancetherobustness reductioninstallsanda49%increaseinQoE.
|     |     |     |     |     |     |     | Some | studies | [26] | highlight | the sub-optimal |     | performance |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ---- | --------- | --------------- | --- | ----------- |
anduserexperienceofstreamingservicesbytacklingcritical
issues of fairness, efficiency, and stability in media content ofthroughput-basedapproachesforadaptingvideostreaming
| delivery. |     |     |     |     |     |     | whenmultipleplayersshareacommonaccessnetwork.The |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
FESTIVEensuresthatallvideostreamingusersreceivea inefficiency of these throughput-based algorithms is further
fairshareofavailableresources,suchasnetworkbandwidth, exacerbated in the presence of cache servers. As a result,
abuffer-basedapproachhasbeenproposedasanalternative
| preventing | any single | user from | monopolizing |     | resources | at  |     |     |     |     |     |     |               |
| ---------- | ---------- | --------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | ------------- |
| 157412     |            |           |              |     |           |     |     |     |     |     |     |     | VOLUME13,2025 |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
|     |     |     |     | reservoir      | range,     | the client     | requests     |               | the lowest  | or           | highest  |
| --- | --- | --- | --- | -------------- | ---------- | -------------- | ------------ | ------------- | ----------- | ------------ | -------- |
|     |     |     |     | video quality, |            | respectively.  |              | Various       | strategies, | including    |          |
|     |     |     |     | optimizing     | buffer     | size,          | pre-fetching |               | content,    | prioritizing |          |
|     |     |     |     | video segments |            | for buffering, |              | and adjusting |             | playback     | rates    |
|     |     |     |     | based on       | buffer     | occupancy      |              | and network   |             | conditions,  | are      |
|     |     |     |     | used to        | reduce     | rebuffering    |              | events.       | The results | show         | that     |
|     |     |     |     | buffer-based   | adaptation |                | (BBA)        | reduces       | the         | video        | stalling |
ratioto10-20%comparedtothestandardadaptivealgorithm
usedbyNetflix.
|     |     |     |     | The Lyapunov |             | Algorithm |         | based     | on Buffer  | Occupancy     |        |
| --- | --- | --- | --- | ------------ | ----------- | --------- | ------- | --------- | ---------- | ------------- | ------ |
|     |     |     |     | (BOLA)       | [29]        | monitors  | buffer  | occupancy |            | (defined      | as the |
|     |     |     |     | amount       | of buffered | video     | content | available |            | for playback) |        |
|     |     |     |     | to maintain  | an          | adequate  | buffer  | level,    | preventing | rebuffering   |        |
FIGURE3. Buffer-basedDASHVideoStreaming.
|     |     |     |     | while optimizing |         | video   | quality.    | It dynamically |       | selects | the     |
| --- | --- | --- | --- | ---------------- | ------- | ------- | ----------- | -------------- | ----- | ------- | ------- |
|     |     |     |     | appropriate      | bitrate | for     | video       | segments       | based | on      | current |
|     |     |     |     | buffer levels    | and     | network | conditions. |                | BOLA  | employs | Lya-    |
punovoptimization,amathematicaltechniqueforcontrolling
|     |     |     |     | dynamic | systems, | to  | make | bitrate | adaptation | decisions, |     |
| --- | --- | --- | --- | ------- | -------- | --- | ---- | ------- | ---------- | ---------- | --- |
balancingthegoalofmaximizingvideoqualitywithensuring
bufferstability.
Bebenetal.[30]proposetheAdaptationandBufferMan-
|     |     |     |     | agement | Algorithm | (ABMA+), |     | a buffer-based |     | adaptation |     |
| --- | --- | --- | --- | ------- | --------- | -------- | --- | -------------- | --- | ---------- | --- |
algorithmthatusesstallingprobabilitytoadjustvideobitrate.
|     |     |     |     | ABMA+        | dynamically |         | adapts     | the video | bitrate    | based      | on  |
| --- | --- | --- | --- | ------------ | ----------- | ------- | ---------- | --------- | ---------- | ---------- | --- |
|     |     |     |     | fluctuations | in          | network | conditions |           | and buffer | occupancy, |     |
|     |     |     |     | aiming       | to optimize | the     | balance    | between   | video      | quality    | and |
FIGURE4. AQoEcontrolframeworkattheAPtodynamicallyallocate
|     |     |     |     | buffer delay, |     | thereby | improving | the | viewer’s | streaming |     |
| --- | --- | --- | --- | ------------- | --- | ------- | --------- | --- | -------- | --------- | --- |
bandwidthforeachDASHclientbasedontheirreal-timestreaming
performancefeedback[27]. experience. The algorithm incorporates a robust buffer
|     |     |     |     | management | component |     | to effectively |     | use buffer | resources |     |
| --- | --- | --- | --- | ---------- | --------- | --- | -------------- | --- | ---------- | --------- | --- |
andmakesbitrateadaptationdecisionstopreventunderflow
| method for estimating | available resources, | as discussed | in  |     |     |     |     |     |     |     |     |
| --------------------- | -------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andminimizerebuffering.Experimentalresultsdemonstrate
SectionII-A2. thatABMA+canefficientlyadaptvideobitrateandreduce
|                               |     |     |     | switching                 | frequency, |     | although | it introduces |     | overhead | and |
| ----------------------------- | --- | --- | --- | ------------------------- | ---------- | --- | -------- | ------------- | --- | -------- | --- |
| 2) BUFFER-BASEDVIDEOSTREAMING |     |     |     | implementationcomplexity. |            |     |          |               |     |          |     |
Thebuffer-basedvideostreamingapproach,showninFig.3, Yadav et al. [31] developed QUETRA, a buffer-based
focusesonmanagingabufferofvideodataontheclientside bitrate adaptation algorithm that estimates the buffer occu-
toensuresmoothplaybackandminimizeinterruptionscaused pancy based on the current bitrate, calculated through-
by fluctuations in network conditions. The buffer stores a ABMA+
|     |     |     |     | put, and | the buffer | level. | Like |     |     | [30], QUETRA |     |
| --- | --- | --- | --- | -------- | ---------- | ------ | ---- | --- | --- | ------------ | --- |
certain amount of video data ahead of playback, enabling requires pre-computed buffer occupancy for implementing
theclienttosmoothoutvariationsinthroughputandprevent thealgorithm.ExperimentalresultsdemonstratedQUETRA’s
disruptions. This method allows monitoring of delay, buffer efficiency in ensuring stable video delivery despite its
QoE metrics, and bitrate variations from the HTTP server, simplicity. Liu et al. [32] introduced BBA+, an ABR
as demonstrated in previous studies [28], [29], [30], [31], algorithmthatiterativelyadjuststhemappingbetweenbitrate
[32],[33].Fig.4illustratestheQoEcontrolframeworkatthe andbufferoccupancybasedonnetworkthroughput.Results
Access Point (AP), which continuously monitors real-time showed that BBA+ effectively improves average bitrate
streaming performance feedback from DASH clients and whilereducingrebuffering.Huangetal.[33]proposedStick,
dynamically adjusts bandwidth allocation to ensure optimal an ABR algorithm combining a conventional buffer-based
streamingqualityforeachuser. approachwithdeeplearningtechniques.
Huangetal.[28]investigatestrategiesusedbyaprominent Stick uses deep reinforcement learning (DRL) to train a
video streaming service to minimize rebuffering events neuralnetworkandmaximizetheQoEmetricacrossvarious
throughbuffermanagementtechniques.Thisapproachrelies parameters.Thenetworkoutputsthebuffer-bound,regulating
onthebufferleveltodeterminetherequestedvideoquality. the buffer-based approach. The results indicate that Stick
The authors define two thresholds, Bmin and Bmax, and outperforms Pensieve by 3.5% to 9.41%, while reducing
three buffer occupancy levels: reservoir (B < Bmin), upper overheadby88%.Tooptimizeperformance,scalability,and
reservoir (B > Bmax), and cushion (Bmin < B < Bmax). user experience,different streaming technologies anddeliv-
If the buffer occupancy falls within the reservoir or upper ery methods, such as peer-to-peer (P2P) and client-server
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     | 157413 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE3. Comparisonofclient-basedanddelivery-basedvideorateadaptationstrategies.
architectures, can be combined for efficient content deliv- to enhance the end-client’s QoE. Notably, the look-up
ery, as discussed in section II-A3. However, buffer-based table for online use is generated by performing offline
streaming poses challenges, including (a) increased latency, computations for the optimization problem to maximize
(b) higher memory and processing demands. Larger buffers efficiency. Both PANDA and MPC-based methods embody
can introduce a startup delay before video playback, a sig- hybrid characteristics—PANDA through heuristic probing
nificantissueforlivestreamingandinteractiveapplications. andbufferawareness,andMPCthroughmodel-basedpredic-
Additionally,buffer-basedstreamingrequiresmorememory tionandofflinecomputation.PANDAexcelsinadaptability
andprocessingpower,whichcanbeproblematicforresource- and simplicity, making it suitable for real-time, resource-
constrained devices [36]. Table 8 provides a summary of constrained environments, while MPC offers a theoretically
client-basedvideostreamingapproachesfor6Gnetworks. grounded, QoE-optimized framework that can potentially
outperformsimplerschemesunderpredictableconditions.
3) HYBRID-BASEDVIDEOSTREAMING The authors in [38] determine the optimal bitrate for
Themostcommonlyhybrid-basedvideostreamingapproach video segments by considering factors such as buffer
includesPANDA[37],Julurietal.[38],Farahanietal.[18], level, throughput measurements, and segment sizes. SARA
[39],and[40]. incorporatesthesegmentsizesfromtheMPDfiletoprovide
The throughput estimation is further enhanced by Probe anaccuratethroughputestimate,aswellasthesegmentsize
And Adapt (PANDA) [37], which focuses on dynamically and Weighted Harmonic Mean (WHM). The buffer level is
adjusting the video streaming bitrate by continuously mon- alsofactoredinbySARAtoadjusttherequiredbitrate.Initial
itoring user behavior and network conditions, while mim- evaluationsofSARAdemonstrateditseffectivenessinusing
icking the application layer’s congestion control behavior. segmentsizetoprovideaccuratethroughputestimations.
Thealgorithmgraduallyincreasesvideoqualityandsharply A recent study in [43] explores the relationship between
decreases it based on predicted throughput. Future segment chunksize,scenecomplexity,andchunkquality.Theresults
requests are then scheduled according to the buffer level. show that even when a segment is encoded at a higher
It has been shown that, compared to traditional algorithms, bitrate, its quality diminishes as the segment size increases.
PANDAcanreduceinstabilitybyover75%.However,there Toaddressthis,theauthorsdevelopedanABRrateadaptation
isnoclearguidelineontheoptimalnumberofbitrateswitches algorithm based on control theory, called CAVA (Control-
duringalgorithmimplementation[13].Buildingonprevious theoreticAdaptionforVBR-basedABRstreaming).During
approaches,Yinetal.[41] developedamathematicalmodel implementation,CAVAfollowsthreecoreABRdesignprin-
aimedatmaximizingtheend-client’sperceivedQoEusinga ciples and employs Proportional-Integral-Derivative (PID)
predictivecontrolmodel-basedmethod(MPC).Themethod control concepts. Additionally, CAVA significantly reduces
consists of three components: prediction, optimization, and rebuffering by up to 95% and quality variation by up to
application, which together determine the ideal bitrate 48%. These techniques reflect a broader trend in video
157414 VOLUME13,2025

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE4. Asummaryofthebuffer-basedstreamingchallengesrelatedtothetrade-offbetweenbuffersizeandlatency.
TABLE5. Comparativeanalysisofthroughput-basedandbuffer-basedadaptivevideostreamingsolutions.
streaming research, moving beyond simplistic throughput game theory. The proposed algorithm demonstrates strong
modelstoembracemulti-metric,feedback-driven,andQoE- performance, outperforming its competitors by 62% in
aware strategies. SARA contributes precision in bitrate quality stability and 38.5% in average QoE. To adapt to
estimation,whileCAVAexcelsincontrol-drivenadaptation, current network conditions, Akhtar et al. [44] propose
andbothoffervaluablelessonsforthefuturedevelopmentof heuristic-specificparametersthatcanbeadjustedinrealtime.
intelligentABRsystems. Oboeisbuiltonapre-computedConfMaptoidentifyoptimal
Bentaleb et al. [39] introduce a game theory-based ABR configurations for a given ABR technique. Experimental
(GTA) that models the ABR decision process as a bargain- results show that Oboe significantly improves client-based
ing and consensus problem, leveraging the capabilities of adaptationtechniquessuchasBOLA[29]andFastMPC[41].
VOLUME13,2025 157415

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE6. Asummaryofclient-basedvideostreamingapproaches.
| Ibrahim | et               | al. [40] | propose | a       | multi-IP | camera-based |        |     |     |     |     |     |
| ------- | ---------------- | -------- | ------- | ------- | -------- | ------------ | ------ | --- | --- | --- | --- | --- |
| method  | for distributing |          | video   | signals | across   | multiple     | levels |     |     |     |     |     |
usingahybridclient/serverandpeer-to-peerapproach.This
| method          | consists      | of four    | functions: |          | (a)     | receiving | linked    |     |     |     |     |     |
| --------------- | ------------- | ---------- | ---------- | -------- | ------- | --------- | --------- | --- | --- | --- | --- | --- |
| camera          | transmissions |            | at the     | central  | server, | (b)       | assisting |     |     |     |     |     |
| clients/servers |               | in viewing | the        | received | video   | signals,  | (c)       |     |     |     |     |     |
receivingvideosignalsfromtheupperlevel,and(d)enabling
| multiple     | clients          | to view       | the | video     | signals | received | from   |     |     |     |     |     |
| ------------ | ---------------- | ------------- | --- | --------- | ------- | -------- | ------ | --- | --- | --- | --- | --- |
| level three. | Li               | [45] develops |     | a hybrid  | visual  | saliency | and    |     |     |     |     |     |
| hierarchical | clustering-based |               |     | 3D tiling | scheme  | that     | better |     |     |     |     |     |
alignswiththeuser’sfieldofview(FoV)involumetricvideo
| streaming.     | The | authors          | build | a QoE     | model | with volumetric |     |     |     |     |     |     |
| -------------- | --- | ---------------- | ----- | --------- | ----- | --------------- | --- | --- | --- | --- | --- | --- |
| video features | as  | the optimization |       | objective |       | and introduce   | a   |     |     |     |     |     |
reconstructedversionthatallowsuserstobypassthedecoding
process,thusreducingdecodingoverhead.
|                  |          |          |            |               |           |              |      | FIGURE5. AreferencearchitectureforSAND. |                |         |                 |      |
| ---------------- | -------- | -------- | ---------- | ------------- | --------- | ------------ | ---- | --------------------------------------- | -------------- | ------- | --------------- | ---- |
| To strike        | a        | balance  | between    | communication |           | and          | com- |                                         |                |         |                 |      |
| puting resources |          | while    | maximizing |               | QoE,      | the authors  | also |                                         |                |         |                 |      |
| propose          | a hybrid | resource | allocation |               | strategy. | Furthermore, |      |                                         |                |         |                 |      |
|                  |          |          |            |               |           |              |      | quality. Despite                        | the successful | aspects | of client-based | rate |
Farahanietal.[18]presentRICHTER’smulti-layerarchitec-
ture,whichconsiderspeer,edge,andCDNserverresourcesto adaptationforHASvideostreaming,suchasitsdecentralized
andpull-basednature,itmaynotfullyaddressthischallenge.
fulfillpeerrequests.TheauthorsproposeanOnlineLearning
(OL) approach utilizing an unsupervised Self-Organizing The following subsections review existing research efforts
Map (SOM) to address the temporal complexity problem thathavebeenimplementedatvariouslevels,specificallythe
|        |              |        |     |            |     |          |      | server and network | levels. | Table 7 provides | a   | summary of |
| ------ | ------------ | ------ | --- | ---------- | --- | -------- | ---- | ------------------ | ------- | ---------------- | --- | ---------- |
| of the | optimization | model. |     | The method |     | performs | well |                    |         |                  |     |            |
in large-scale environments when group-based decisions delivery-basedvideorateadaptationfor6Gnetworks.
| for video | segment | requests |     | are made | instead | of  | handling |     |     |     |     |     |
| --------- | ------- | -------- | --- | -------- | ------- | --- | -------- | --- | --- | --- | --- | --- |
individual requests. These techniques (Bentaleb et al. [39], 1) BITRATEGUIDANCEANDBANDWIDTHSHAPING:THE
Ibrahimetal.[40],Zahaibetal.[44])representahybridiza-
CASEOFSAND
tiontrendinadaptivevideostreaming,wherecontroltheory, The Server And Network Assisted DASH (SAND) [46]
| AI, saliency | modeling, |     | and game            | theory | are | used to      | handle |                    |              |           |          |              |
| ------------ | --------- | --- | ------------------- | ------ | --- | ------------ | ------ | ------------------ | ------------ | --------- | -------- | ------------ |
|              |           |     |                     |        |     |              |        | provides operators | and service  | providers | with     | standardized |
| the growing  | demands   |     | of personalization, |        |     | scalability, | and    |                    |              |           |          |              |
|              |           |     |                     |        |     |              |        | messaging          | and exchange | protocols | designed | to optimize  |
efficiency. While each approach introduces domain-specific network capacity and enhance the streaming experience.
| innovations, | future | research |     | must address |     | their | real-time |          |                    |         |      |         |
| ------------ | ------ | -------- | --- | ------------ | --- | ----- | --------- | -------- | ------------------ | ------- | ---- | ------- |
|              |        |          |     |              |     |       |           | By using | messages exchanged | between | DASH | clients |
feasibility, generalizability, and interoperability to build and network elements, SAND improves streaming session
| robust, intelligent |     | streaming |     | systems | that adapt | seamlessly |     |     |     |     |     |     |
| ------------------- | --- | --------- | --- | ------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
efficiencyandcontentdelivery.Thesemessagesofferinsights
acrossdiversenetworkandusercontexts.
|     |     |     |     |     |     |     |     | into the performance | and status | of DASH | clients, | as well |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ---------- | ------- | -------- | ------- |
astheoperationalcharacteristicsofservers,proxies,caches,
B. DELIVERY-BASEDVIDEORATEADAPTATION and CDNs. Figure 5 illustrates the communication patterns
Pure client-based adaptation alone may not be sufficient to between DASH clients and a SAND-enabled HTTP server
| ensure equitable |     | video | distribution | among |     | users with | high | (DANE). |     |     |     |               |
| ---------------- | --- | ----- | ------------ | ----- | --- | ---------- | ---- | ------- | --- | --- | --- | ------------- |
| 157416           |     |       |              |       |     |            |      |         |     |     |     | VOLUME13,2025 |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
Aligned with the SAND approach, Petrangeli et al. [35] mobile network operators and video content providers.
introduced a rate adaptation mechanism that ensures equal With this approach, the network operator can inform
bandwidth distribution among multiple clients. The authors service providers about network conditions, allowing them
implemented a system of coordination proxies within the to proactively cache the requested video segments. The
network, which periodically calculates available bandwidth proposed architecture utilizes the Self-Similar Least-Action
andallocatesitfairlyamongclients.Thisensureseachclient Walk (SLAW) model to predict user mobility during video
receives a fair signal for bitrate adjustments, performance, streamingsessions.
and status updates. The results showed that this approach Samain et al. [52] present an in-network component that
improvedqualityby20%andfairnessby80%comparedto aidsclientsinselectingtheoptimalbitrateandmitigatesthe
existingmethods. negative effects of using video cache servers on client-side
Kleinrouweler et al. [47] proposed a DASH-aware net- bitrate adaptation. Video cache servers may misestimate
working architecture based on SDN, designed to deliver client-side bandwidth, reducing QoE. The authors also
stable, high-quality video to end users. In this setup, the employ the SAND mechanism to guide clients in selecting
SDN controller acts as an external agent, providing each the appropriate bitrate. Ozcelik and Ersoy [34] introduce
videostreamingclientwiththeoptimalmaximumbitrate.The CSASD, a chunk-size aware SDN-based architecture that
network-based agent employs two mechanisms—explicit provides DASH players with bitrate recommendations to
and implicit adaptation assistance—to guide DASH players maintain fair QoE while preventing network underutiliza-
toward the best bitrate. The explicit adaptation assistance tion. Instead of using bandwidth slicing, which can lead
involves dynamically assigning network resources to each to scalability issues, CSASD adjusts the desired video
client to deliver the target bitrate. Experimental results in bitrate levels asynchronously by continuously monitoring
a WiFi environment showed that this method increased the background traffic. This approach helps avoid buffer stalls
received video bitrate and reduced the frequency of quality and network underutilization. CSASD outperforms purely
switching. client-based methods, improving the average video bitrate
Cofano et al. [48] conducted an extensive investigation by 90% and reducing fluctuations in video quality by
into the design of video control planes, focusing on various over84%.
network-assisted strategies, including several SDN-based Guillen et al. [53] introduce SAND/3, a QoE control
streaming techniques that rely on communication between techniquefordynamicadaptivestreamingoverHTTP/3and
the network and video streaming applications. The authors SDN. As shown in Fig. 6, SAND/3 combines user, device,
developed a visual control plane to ensure that concurrent service,andnetwork-leveldata,whicharemanagedbythree
video streams from different client devices maintain equal modules. The User module collects and stores end-user
video quality. Two methods were compared to determine identificationinformation,alongwiththedevicesconnected
the optimal approach in an SDN network: (1) bandwidth to it, in a repository known as the User Profile, which is
reservation, which allocates a specific bandwidth slice to a populated by data obtained from a third-party service (e.g.,
video flow (or group of flows), and (2) bitrate guidance, Netflix).
which calculates the video bitrate using a centralized
algorithmrunninginanetworkelement,withthevideoclient
enforcing it. The authors also combined both bandwidth
reservationandbitrateguidanceapproaches,resultinginthe
best outcomes in terms of fairness in video quality among
users.
Bentaleb et al. [49] propose SDNDASH, which dynami-
callyallocatesnetworkresourcesanddirectseachstreaming
clienttotheoptimalbitrateforthenextrequestedchunk.With
SDNDASH,theexternalvideoqualityengineenhanceseach
client’s QoE. Experimental results show that SDNDASH
improvesfinalvideoqualitybyupto30%comparedtoother
existingmethods.
An SDN-based Adaptive Bit Rate (SABR) architec-
ture [50] has been proposed to monitor the network paths
betweentheaccessnetworkandCDNcaches.Inadditionto FIGURE6. AnoverviewofSAND/3architecture[53].
providing information about the available bitrate levels for
therequestedvideooncacheservers,SABRsuppliesDASH The network module handles traffic engineering by
players with network details. SABR allows HAS players to directing packets along the best available paths in terms of
selecttheirbitrateusingatimeseriesforecastingtechnique. qualityofservice.TheNetworkMonitorsub-modulecontin-
Similarly, Liotou et al. [51] introduce a HAS QoE-based uously monitors the network’s status by collecting statistics
SDNarchitecturedesignedtofacilitatecooperationbetween from each component, thereby enhancing the estimation of
VOLUME13,2025 157417

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE7. Asummaryofdelivery-basedvideorateadaptationapproaches.
availableresources.TheQoEManagersub-modulesuggests Su and Maw [68] present an SDN traffic engineering
the optimal settings for video transmission, which are frameworkforefficientlyreroutingvideostreamingtrafficto
managedbytheTransportHandlersub-module.Thisprocess reducepacketlossandincreasevideobitrates.Theproposed
takes place in the application module, based on the user system uses least-cost path rerouting instead of the ONOS
profile, specific service policies, and the current network controller’s default reactive forwarding routing and can
conditions. It is worth noting that the Transport Handler calculate current link utilization across network paths. The
sub-module establishes the transport connection using the approach is validated using the Mininet network emula-
QUICprotocol. tionenvironmentandOpenFlowtechnologies.Experimental
results show that optimizing video streaming bitrates and
2) INNETWORKVIDEOOPTIMISATION minimizingpacketlosssignificantlyimprovesperformance.
a: TRAFFICRE-ROUTINGVIDEOSTREAMING
Traffic rerouting involves redirecting data to alternative b: PROXY-BASEDVIDEOSTREAMING
networkpathstoenhanceperformanceandensurecontinuous Proxy-based video streaming uses proxy servers to enhance
streaming. Key research in traffic rerouting includes works and optimize the delivery of video content to end
by [59], [60], [61], [62], [63], [64], [65], [66], and [67]. users. In this context, Georgopoulosetal.[69] propose an
In[60],theauthorsproposeasegment-awarevideostreaming OpenFlow-assisted QoE Fairness Framework (QFF), which
routingmechanismusingSDN,accountingforheterogeneous aims to fairly maximize the QoE for multiple competing
DASH clients. They consider various parameters, such as clients in a shared wireless network. The QFF approach
videobitrate,networkperformance,videosegment,andpath leverages OpenFlow to support vendor-neutral network
length,toselecttheoptimalroutingmethodforvideoflows management and active resource allocation. The framework
from the server to the DASH clients. Dobrijevic et al. [61] consists of several components, including optimization and
introduceaQoE-centricflowroutingapproachutilizingQoE utility functions. The Optimization Function utilizes the
estimation models. Meanwhile, Bouten et al. [62] present a models provided by the Utility Function to determine the
dynamicserverselectionmethodthatidentifiesandchooses optimal set of bitrates that ensures QoE fairness across all
thebestserverbasedonitsnetworkcharacteristicstodeliver DASHclientsinthenetwork.
high-qualityvideotoendusers.Al-Jawadetal.[63]propose
LearnQoS, an approach based on Reinforcement Learning c: VIDEOSTREAMPRIORITIZATION
(RL)andPolicy-BasedNetworkManagement(PBNM)that Video stream prioritization optimizes network resources to
optimizesQoS/QoEusingSDN.LearnQoSleveragesPBNM ensure that high-priority video streams receive the required
to manage traffic engineering and handle QoS/QoE policy bandwidthandlowlatencyforoptimalperformance.Topre-
violationsduringmultimediadeliverytoendusers. vent delays, Petrangeli et al. [70] introduced a centralized
Khalid et al. [66] introduce DANOS, a Device-Aware SDN-basedstructurethatprioritizesspecificvideosegments
Network-assisted Optimal Streaming service, designed for for delivery. Their approach estimates the end user’s buffer
inter-domain adaptive video bitrate streaming in software- level using only OpenFlow statistics from network nodes.
defined environments. DANOS delivers high-quality and Additionally, a machine learning engine at the control level
consistent video based on end users’ device capabilities, processesdatagatheredfromthenetworknodes.Compared
ISP/CDN network limits, and subscription quality levels. to traditional HAS heuristics, this method reduces freezing
To ensure fair service differentiation in DASH applications, times without significantly affecting the performance of
theauthorsin[67]proposeanSDN-drivenQoEoptimization cross-traffic applications. Recent video traffic prioritization
model that determines the optimal video streaming path for studies include the Application Prioritization Engine (APE)
DASHclientpackets.ThisarchitectureensuresQoEfairness framework,whichenhancesuserexperiencebydynamically
forDASHclientswithinthesameserviceclass. allocating bandwidth to different smartphone applications.
157418 VOLUME13,2025

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
FIGURE7. QoEoptimizationandcontroloversoftwarized5Gnetworks.Globaloptimization/predictionsystemcanusevariousQoE
strategiesforoptimizingABRvideostreamingincluding:feedbackcontrol,videorateadaptation,resourceallocationsand
throughputprediction.
APE prioritizes real-time traffic over concurrent best-effort mobile devices to analyze path utilization, TCP throughput,
traffic,improvingtheend-userexperience[71].Furthermore, handshake latency, video streaming bitrate, and web page
| the authors   | in [72]   | propose | a          | strategy | that prioritizes | traffic | loadtime. |          |         |     |                   |     |               |     |
| ------------- | --------- | ------- | ---------- | -------- | ---------------- | ------- | --------- | -------- | ------- | --- | ----------------- | --- | ------------- | --- |
|               |           |         |            |          |                  |         | Cao et    | al. [77] | propose |     | a learning-driven |     | latency-aware |     |
| at the user’s | terminal, |         | addressing | the      | first bottleneck | in the  |           |          |         |     |                   |     |               |     |
system,regardlessoftheaccessnetwork. MPTCP approah that can mitigate the out-of-order packet
arrivalandreceivebufferblockingproblemsassociatedwith
|     |     |     |     |     |     |     | the network | heterogeneity |     |     | in the | industrial | Internet | [77]. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --- | ------ | ---------- | -------- | ----- |
3) TRANSPORTLEVELVIDEOOPTIMIZATIONIN
Throughanovelmultiexpertlearning-enabledforwarddelay
MPTCP-ASSISTEDNETWORKS
|     |     |     |     |     |     |     | estimator, | the | proposed | approach |     | reliably | computes | the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | -------- | --- | -------- | -------- | --- |
Transport-levelvideooptimizationinSDN-assistednetworks
|     |     |     |     |     |     |     | forward | delay | of each | MPTCP | path | and assigns |     | application |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | ----- | ---- | ----------- | --- | ----------- |
leveragesSDNprinciplestoimprovevideostreamingperfor-
datatovariouspathsbasedontheirestimatedforwarddelay
manceandefficiency.MPTCPatthetransportlayeraimsto
boostoverallthroughputforstreamingclients[56],[73],[74]. differences.Usingapromisingmultipathmanagerenabledby
reinforcementlearning,thetechniquedynamicallyregulates
| Barakabitze | et     | al. [56] | introduce | a QoE-aware |            | SDN-based |                  |             |     |         |           |           |               |     |
| ----------- | ------ | -------- | --------- | ----------- | ---------- | --------- | ---------------- | ----------- | --- | ------- | --------- | --------- | ------------- | --- |
|             |        |          |           |             |            |           | path consumption |             | and | selects | the       | best path | collection    | for |
| MPTCP/SR    | system | for      | 5G        | networks,   | optimizing | network   |                  |             |     |         |           |           |               |     |
|             |        |          |           |             |            |           | bandwidth        | aggregation |     | and     | multipath |           | transmission. | The |
resourceusageanddynamicallymanagingMPTCPsubflows.
employcrowdsourcedprobingonparticipants’phonestodo
Wuetal.[74]presenttheADMITtechnique,whichimproves
mobile-basedvideostreamingservicesbyreducingdistortion passive measurements in order to record end-user QoE via
|         |                |     |         |       |            |       | multipath | in the | presence |     | of fluctuating |     | network | circum-     |
| ------- | -------------- | --- | ------- | ----- | ---------- | ----- | --------- | ------ | -------- | --- | -------------- | --- | ------- | ----------- |
| through | quality-driven |     | Forward | Error | Correction | (FEC) |           |        |          |     |                |     |         |             |
|         |                |     |         |       |            |       | stances.  | For a  | duration | of  | five months,   |     | Mohan   | et al. [76] |
coding,rateallocation,andcongestioncontrol.
|     |     |     |     |     |     |     | conduct | a measurement |     |     | investigation |     | of MPTCP | over |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --- | ------------- | --- | -------- | ---- |
ToaddressthecurrentMPTCPissues,suchashead-of-line
|                     |               |      |            |            |            |                | multi-carrier | LTER      |            | connections | in        | typical     | daily      | working    |
| ------------------- | ------------- | ---- | ---------- | ---------- | ---------- | -------------- | ------------- | --------- | ---------- | ----------- | --------- | ----------- | ---------- | ---------- |
| blocking,           | in multimedia |      | content    | transport, |            | Corbillonetal. |               |           |            |             |           |             |            |            |
|                     |               |      |            |            |            |                | mobility      | scenarios | of         | mobile      | services. | The         | authors    | gather     |
| [75] examine        | various       |      | scenarios  | for        | DASH       | over MPTCP     |               |           |            |             |           |             |            |            |
|                     |               |      |            |            |            |                | information   | both      | in         | the wild    | and       | in a        | controlled | setting    |
| to assess           | its benefits  |      | for mobile | video      | streaming. | Their          |               |           |            |             |           |             |            |            |
|                     |               |      |            |            |            |                | throughout    | a         | five-month |             | period.   | The primary |            | goal is to |
| results demonstrate |               | that | MPTCP      | can        | provide    | high QoE for   |               |           |            |             |           |             |            |            |
|                     |               |      |            |            |            |                | comprehend    | how       | MPTCP      |             | affects   | last-mile   | video      | quality,   |
users,evenwhennetworkbandwidthfluctuatessignificantly,
workloadforvideoapplications,andmobility.
| especially | when | the primary |     | path is | highly | reliable. The |     |     |     |     |     |     |     |     |
| ---------- | ---- | ----------- | --- | ------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
authorsalsonotethatMPTCPperformswellwhenutilizing
| tworouteswithstablebandwidths. |     |     |     |     |     |     | C. SUMMARYANDLESSONLEARNED |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
MPTCP can be beneficial when the bandwidth of the Most of these techniques focus on improving QoE by
secondary path is limited. Additionally, when both paths addressingbitrateadaptations,resourceallocations,anduser-
have stable and sufficient bandwidth, MPTCP can support centric optimizations. QoE streaming techniques such as
higher video bitrates without causing delays in quality gametheory,hybridclustering,andonlinelearninghighlight
switchingorstartup.ToenhanceMPTCPandenableadaptive theintegrationofadvancedcomputingparadigmsintovideo
videostreamingwithuser-preferredinterfaces,Mohanetal. streaming solutions. These efforts cater to the growing
[76] conduct a measurements-driven study on multipath in demand for seamless and high-quality video experiences.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 157419 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE8. AcomparativeanalysisbetweenSDN/NFV-basedandMPTCP-baseddeliveryapproaches.
TABLE9. AsummaryofQoE-drivennetworksoftwarization/virtualization,cloud/edgeandAI/MLarchitectures.
Novel methodologies (e.g., hybrid resource allocation and QoE-drivennetworksoftwarization/virtualization,cloud/edge
multi-layer architectures) demonstrate the importance of andAI/MLarchitectures.
| balancing computational | and             | network resources | to ensure |     |     |     |     |
| ----------------------- | --------------- | ----------------- | --------- | --- | --- | --- | --- |
| system scalability      | and resilience. | However, issues   | such as   |     |     |     |     |
A. QOE-DRIVENOPTIMIZATIONANDCONTROLOVER
| decoding overhead, | new bitrate | switching guidelines, | and |     |     |     |     |
| ------------------ | ----------- | --------------------- | --- | --- | --- | --- | --- |
SOFTWARIZED5GNETWORKS
| real-time adaptability | remain | challenges that require | further |                  |             |             |           |
| ---------------------- | ------ | ----------------------- | ------- | ---------------- | ----------- | ----------- | --------- |
|                        |        |                         |         | QoE optimization | and control | can involve | QoE-aware |
investigations.
|     |     |     |     | network orchestration, | where     | SDN and      | NFV dynamically  |
| --- | --- | --- | --- | ---------------------- | --------- | ------------ | ---------------- |
|     |     |     |     | manage network         | resources | and services | according to QoE |
III. QoE-DRIVENNETWORKSOFTWARIZATIONAND requirements. This allows network functions to be instanti-
VIRTUALIZATION:AI/ML,CLOUD/EDGECOMPUTING ated, scaled, and migrated in real-time to adapt to changing
|     |     |     |     | multimedia traffic | patterns | and video quality | demands (see |
| --- | --- | --- | --- | ------------------ | -------- | ----------------- | ------------ |
ANDSDN/NFVARCHITECTURES
ThissectionprovidesQoE-drivennetworksoftwarizationand Fig. 7). Furthermore, QoE-driven optimization algorithms
virtualizationwithafocusonAI/ML,cloud/edgecomputing can allocate resources such as bandwidth, computing, and
andSDN/NFVarchitectures.Table9presentsasummaryof radioresources,prioritizingcriticalapplicationsandservices
| 157420 |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | ------------- |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE10. AsummaryofQoE-drivenAI/MLvideostreaming.
thatenhanceuserexperience.Thisensuresefficientresource network adaptation applies intelligent resource allocation
utilization while meeting QoE targets. Additionally, QoE- and auto-configuration rules to adjust network parameters
drivenoptimizationandcontrolmaysupportnetworkslicing, andmanagecapacityinreal-time,ensuringaconsistentand
enablingthecreationofvirtualizednetworkinstancestailored high-qualityuserexperience.
to specific applications or user groups [3]. QoE-driven resourcemanagement.
networkslicingguaranteesthateachsliceisoptimizedforthe
needsoftheassociatedapplications,ensuringahigh-quality B. AI/MLQoE-DRIVENVIDEOSTREAMING
user experience [2]. Moreover, AI/ML techniques can be The deployment of AI/ML-based QoE optimization tech-
employed in QoE optimization to analyze data, predict user niques for video streaming in next-generation networks
behavior, and proactively enhance network performance. involves utilizing advanced algorithms to improve user
AI-drivenoptimizationalgorithmscanadjustnetworkconfig- satisfaction by dynamically adapting streaming parameters
urationsandparametersinreal-timetomaximizeQoEwhile accordingtocurrentnetworkconditionsanduserpreferences,
minimizingoperationalcosts. ashighlightedinrecentstudies[95],[96],[97].Asummary
Recent works for QoE optimization and control of video oftheAI/MLalgorithmsusedforvideostreamingisprovided
streaming on 5G softwarized networks include the 5G-QoE inTable10.
models[85],[86],[87].QoEpredictionmodelsofUHDvideo In [96], the authors propose a framework that leverages
streaming services’ perceived QoE over a practical multi- reinforcement learning (RL) to determine video represen-
tenanted 5G mobile edge network testbed is proposed by tation at the DASH client. The DASH controller performs
Nightingale et al. [85]. The authors highlight that 5G-QoE online learning to track the system’s temporal behavior
should include self-optimization capabilities that support and employs an algorithm that optimizes video quality
scalable H.265 4K/8K/12K or 360◦ video applications to for the end user. The method is built on a Markov
transmit QoE-aware UHD video services. Fei et al. [86] Decision Process (MDP) framework, which selects the best
introduceanobjectiveQoEevaluationmethodologybasedon video representation while minimizing buffering events and
networktransmissionmetricsaswellasasubjectiveVRQoE variations in video quality. Zhou and Lin [95] introduce
evaluationapproach. mDASH, a Markov decision-based rate adaptation strategy
The integration of QoE into heterogeneous 6G and for dynamic HTTP streaming applications. The proposed
future networks (HetNets) follows multiple key phases, greedy algorithm optimizes QoE under fluctuating wireless
asillustratedinFig.8.TheprocessbeginswithPhase1:QoE- channel conditions by considering key parameters such as
related data collection, which involves gathering real-time bufferoverflowsandunderflows,bufferoccupancy,playback
QoS metrics, user feedback (MOS), and application-level quality,videoamplitude,andthefrequencyofrateswitching.
performance data from the HetNet environment. Phase 2: In another approach, Mao et al. [97] present Pensieve,
QoE prediction uses this data for machine learning-based asystemthattrainsadaptivebitrate(ABR)algorithmsusing
analysis and real-time QoE assessment, enabling proactive RL methods. It utilizes incentive signals based on previous
optimization[89].InPhase3:network-widequalitymapping, adaptation decisions, and client-side video players use a
QoE data is used to identify and prioritize critical areas in trainedneuralnetworkmodeltoselectfuturevideosegments
the network for multimedia streaming. Phase 4: dynamic basedonreal-timeobservations.
VOLUME13,2025 157421

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
FIGURE8. QoEoptimizationandcontroltechniquesbasedontheQoEmetricsinheterogeneous5Gnetworks[88].
Gadaleta et al. [98] introduce D-DASH, a QoE opti- Tiyuntsong, developed by Huang et al. [102], is a self-
mization framework that integrates deep learning and play reinforcement learning algorithm that incorporates a
reinforcement learning techniques to improve the end-user Generative Adversarial Network (GAN) to enhance ABR
experience.D-DASHoptimizesQoEbytakingintoaccount videostreaming.In[103],authorsintroduceFugu,acontin-
factors such as freezing/rebuffering events and fluctuations uouslearningmechanismdesignedtoimprovevideobitrate
in video quality. In [99], a fuzzy logic controller (FLC) selectioninmediastreamingservices.Fugulearnsfromuser
is proposed to dynamically adjust the bitrate of DASH input and predicts QoE with high accuracy using a trained
video streams by analyzing the client’s buffer size and neural network. It decides whether to download the next
predicted network throughput. By modifying the policy for videosegmentbasedoninternalTCPstatisticsandhistorical
selecting subsequent video bitrates, the FLC effectively performancedata.
reduces ON-OFF switching during playback through buffer While AI/ML technologies enhance threat detection and
dynamicsandreal-timethroughputobservations. enable automated security responses, they also introduce
Thestudy[100]explorestheuseofreinforcementlearning new risks such as adversarial attacks, where models are
(RL) at the client side. An agent is trained to learn optimal manipulatedthroughpoisoningorevasiontechniques[104].
configurationparametersundervaryingnetworkconditions. Moreover, AI-based decision-making in SDN/NFV envi-
The selection process considers bandwidth characteristics ronments raises data privacy concerns, as centralized or
with the goal of reducing average buffer fill times. The cloud-based AI systems may handle sensitive traffic and
agent employs a reward function to evaluate outcomes metadata,increasingvulnerabilitytocyberespionage[105].
after each action, improving decision-making over time. To address these challenges, it is critical to implement
Sieber et al. [101] propose HASBRAIN, a framework for zero-trust architectures, secure AI model training protocols,
training machine learning-based adaptation algorithms for encrypted communications, and anomaly-based intrusion
HTTP Adaptive Streaming (HAS). Leveraging deep rein- detectionsystemstoprotecttheintegrityandresilienceofAI-
forcement learning, HASBRAIN minimizes video quality enabledSDN/NFVnetworks[106].
switches,particularlyinmobileenvironmentswithfrequently Notably, AI prediction models can evaluate real-time
changingthroughput. networkconditionsanddynamicallyadjustvideobitratesto
QARC selects future video bitrates by analyzing histor- balance video quality and smooth playback. For instance,
ical download data and current network states. Similarly, if the available bandwidth decreases, AI can automatically
157422 VOLUME13,2025

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
switch to a lower resolution stream to prevent buffering. and AI/ML-based QoE prediction algorithms. This com-
Additionally, AI/ML-based prediction and management prehensive framework enables network operators deploying
models can learn user preferences such as favored video DASHservicestomanageQoS/QoEandresourceallocation
quality or content interaction patterns at various times of effectively, ensuring high-quality experiences for premium
thedayallowingforapersonalizedandoptimizedstreaming users while maintaining overall service performance. Addi-
experience,asthoroughlydetailed. tionally,similartoframeworksproposedin[3],operatorsmay
|     |     |     |     |     |     |     |     | directly | communicate |     | with user | equipment |     | (UEs) to lower |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --------- | --------- | --- | -------------- |
C. AQoE-DRIVENMANAGEMENTARCHITECTURESOVER videobitrateswhennecessary,helpingbalancenetworkload
| MULTI-ACCESSCLOUD/EDGESOFTWARIZED5G |     |     |     |     |     |     |     | withina5Gcell. |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
NETWORKS
A QoE-driven management framework for multi-access D. SUMMARYANDLESSONLEARNED
cloud/edge softwarized 5G networks—illustrated in Fig. 9 Table 10 provides a summary of AI/ML algorithms applied
leverages SDN, NFV, MEC, and ICN technologies to to video streaming, while Table 9 outlines key QoE-driven
help service providers and network operators enhance approaches in network softwarization/virtualization, cloud
andedgecomputing,andAI/MLarchitectures.Thissection
| the end-user | video | streaming |     | experience | while | ensuring |     |     |     |     |     |     |     |     |
| ------------ | ----- | --------- | --- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
efficient utilization of network resources. To improve QoE examinesstrategiescenteredonQualityofExperience(QoE)
for high-resolution streaming (4K/8K/12K or 360◦), the formanagingmultimediastreamingacrossadvancednetwork
framework facilitates the exchange of real-time streaming infrastructures. By leveraging AI/ML techniques—such as
parameters, environmental conditions, Quality of Physical reinforcementlearninganddeeplearningitbecomespossible
Experience (QoPE) or user feedback, and status messages to dynamically optimize streaming parameters, thereby
between users, networks, and DASH-Aware Network Ele- improving user experience even under fluctuating network
ments (DANE). The QoPE measures the user’s perception conditions.Thepresentedframeworksandarchitecturesoffer
and satisfaction derived from interacting with a physical a clear direction for achieving ultra-low latency and high-
environment or service. This can encompass a wide range quality video delivery in 6G networks. The integration of
of factors, including comfort, usability, aesthetics, and the edgeintelligenceandAI-basedmanagementwillbeessential
overallemotionalresponseevokedbytheexperience.Some inrealizingtheseadvancements.
| factors     | that affect | QoPE      | include | brain    | cognition, |        | body |                                      |     |     |     |     |     |     |
| ----------- | ----------- | --------- | ------- | -------- | ---------- | ------ | ---- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
|             |             |           |         |          |            |        |      | IV. EMERGINGTRENDSANDTECHNOLOGIESFOR |     |     |     |     |     |     |
| physiology, | and         | gestures. | Machine | Learning |            | equips | DANE |                                      |     |     |     |     |     |     |
withessentialknowledgeandintelligenceregardingDASH, MULTIMEDIA6GNETWORKS
includinginsightsintoDASHclients,servers,MECcaches, This section discusses the potential impact of 6G net-
|     |     |     |     |     |     |     |     | works on | QoE | monitoring |     | and management. |     | We provide |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --- | --------------- | --- | ---------- |
andCDNs,tooptimizevideostreamingperformance.
|     |     |     |     |     |     |     |     | a comprehensive |     | discussion |     | on technologies |     | like edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --- | --------------- | --- | --------- |
DASHclientscaninformDASH-AwareNetworkElements
|     |     |     |     |     |     |     |     | computing, | AI/ML-based |     | optimization, |     | ultra-low | latency |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------- | --- | --------- | ------- |
(DANEs)abouttheirrequiredoperatingbandwidth,thetype
|           |         |           |         |        |     |         |         | communication, |     | immersive | media | formats, |     | 6G multimedia |
| --------- | ------- | --------- | ------- | ------ | --- | ------- | ------- | -------------- | --- | --------- | ----- | -------- | --- | ------------- |
| of device | in use, | streaming | context | (e.g., | on  | a train | or in a |                |     |           |       |          |     |               |
projects/initiativesetc.,andhowtheycouldimproveQoE.
stadium),QoPErequirements,anddesiredvideoquality(as
| shown by | the | colored | dotted arrows |     | in Fig. | 5). In | return, |                               |     |     |     |     |     |     |
| -------- | --- | ------- | ------------- | --- | ------- | ------ | ------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
|          |     |         |               |     |         |        |         | A. THEROLEOF6GNETWORKSFORDASH |     |     |     |     |     |     |
DANEscancommunicatewithDASHclientsregardingvideo
VIDEOS:TECHNOLOGIES,SERVICEQUALITYAND
| segment | availability, | network | throughput, |     | and | the | caching |     |     |     |     |     |     |     |
| ------- | ------------- | ------- | ----------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
BUSINESSREQUIREMENTS
| status of | segments | stored | in either    | the | DANE | or the       | MEC |           |       |          |        |            |             |          |
| --------- | -------- | ------ | ------------ | --- | ---- | ------------ | --- | --------- | ----- | -------- | ------ | ---------- | ----------- | -------- |
|           |          |        |              |     |      |              |     | The role  | of 6G | networks | in     | delivering | Dynamic     | Adaptive |
| server,   | enabling | a fair | distribution | of  | QoE. | For example, |     |           |       |          |        |            |             |          |
|           |          |        |              |     |      |              |     | Streaming | over  | HTTP     | (DASH) | videos     | encompasses | several  |
topreventtheoveruseorunderuseofresources,DANEscan
keyaspects,includingadvancedtechnologies,improvedser-
| allocate | available | bandwidth | among |     | DASH clients |     | sharing |     |     |     |     |     |     |     |
| -------- | --------- | --------- | ----- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
vicequality,andspecificbusinessrequirementsasdescribed
| the same | network | information |     | according | to their | individual |     |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
below:
needs.
Withthiscoordination,DASHclientscanquicklyretrieve
|     |     |     |     |     |     |     |     | 1) HIGHDATARATESANDTHROUGHPUT |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
cached video content from the MEC server, significantly 6Gnetworksareexpectedtoprovidesignificantlyhigherdata
| reducing | download | times | a critical | factor | in  | achieving | low |     |     |     |     |     |     |     |
| -------- | -------- | ----- | ---------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ratesandthroughputcomparedtopreviousgenerations.This
| latency | in 6G | networks. | To further | enhance |     | user QoE, | the |            |          |          |     |                 |     |              |
| ------- | ----- | --------- | ---------- | ------- | --- | --------- | --- | ---------- | -------- | -------- | --- | --------------- | --- | ------------ |
|         |       |           |            |         |     |           |     | allows for | seamless | delivery |     | of high-quality |     | DASH videos, |
server can implement bitrate recommendations, bandwidth eveninultra-high-definition(UHD)andimmersiveformats.
| slice selection |     | strategies, | and | intelligent | network/service |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Improveddataratesin6Gwillcontributetoreducedbuffering
management and orchestration mechanisms across soft- times, minimized latency, and enhanced video streaming
| warized | 6G infrastructure. |     | It can | also | feed QoE | data | to the |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | ------ | ---- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
experiencesforend-users[107].
SDNcontrollerforimproveddecision-making.
The system can dynamically determine minimum and 2) LOWLATENCYANDEDGECOMPUTING
maximum bitrate thresholds for each client by applying 6Gnetworksaredesignedtoofferultra-lowlatency,enabling
buffer-filling strategies that ensure an adequate buffer level, real-time interactions. Edge computing, integrated with 6G,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 157423 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
QoE-drivenmanagementofmultimediaservicesovermulti-accesscloud/edgesoftwarizedandvirtualized5Gnetworks.
FIGURE9.
| FIGURE10. | Enhancingimmersiveandinteractivemultimediaservices |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
over6Gnetworks.
| facilitates | processing | closer | to      | the end-user, |             | optimizing |     |     |     |     |     |     |     |
| ----------- | ---------- | ------ | ------- | ------------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| DASH video  | delivery.  | Low    | latency | in            | 6G networks | will       |     |     |     |     |     |     |     |
ensureminimaldelaysinvideostarttimesandresponsiveness
|     |     |     |     |     |     |     | FIGURE11. | Futuretechnologiesthatwillenablemultimediastreaming |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------------------- | --- | --- | --- | --- | --- |
over6Gnetworks.
| during adaptive |     | streaming, | providing | a smoother |     | and more |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
enjoyableuserexperience[2].
3) MASSIVECONNECTIVITYANDDEVICEDENSITY slice can be tailored to the unique requirements of specific
| 6G networks | will | support | a massive |     | number | of con- |          |                  |     |          |     |                    |     |
| ----------- | ---- | ------- | --------- | --- | ------ | ------- | -------- | ---------------- | --- | -------- | --- | ------------------ | --- |
|             |      |         |           |     |        |         | services | or applications, |     | allowing | for | optimized resource |     |
nected devices simultaneously. This is crucial for handling usage and delivering customized performance, security, and
the increasing demand for video content across various reliability [5]. 6G introduces network slicing, allowing the
devices[2].Theabilitytoaccommodateahighdevicedensity
|     |     |     |     |     |     |     | creation | of virtualized, | customizable |     | network | segments | tai- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ------------ | --- | ------- | -------- | ---- |
ensures that users can access DASH videos concurrently loredtospecificservices,includingDASHvideostreaming.
| without degradation |     | in service | quality, | meeting |     | the require- |     |     |     |     |     |     |     |
| ------------------- | --- | ---------- | -------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Networkslicingenablestheallocationofdedicatedresources
mentsofcrowdedenvironments[108]. for DASH video services, ensuring consistent, high-quality
streamingexperiencesforusersover6Gnetworks[109].
4) AIANDMACHINELEARNINGINTEGRATION
6Gnetworksleverageartificialintelligence(AI)andmachine
learning (ML) for network optimization, content delivery B. MULTIMEDIASTREAMINGANDFUTURE
TECHNOLOGIESOVER6GNETWORKS
prediction,anduserbehavioranalysis.AI-drivenalgorithms
|     |     |     |     |     |     |     | Fig. 11 | indicates | different | technologies |     | (intelligentiza- |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --------- | ------------ | --- | ---------------- | --- |
enhancetheefficiencyofDASHvideodeliverybypredicting
|            |              |            |     |            |            |          | tion (pervasive |                | AI/ML, | big data   | analytics), | cloudification |     |
| ---------- | ------------ | ---------- | --- | ---------- | ---------- | -------- | --------------- | -------------- | ------ | ---------- | ----------- | -------------- | --- |
| user’s QoE | preferences, | optimizing |     | network    | resources, | and      |                 |                |        |            |             |                |     |
|            |              |            |     |            |            |          | (O-RAN),        | softwarization |        | (SDN/NFV), | quantum     | communi-       |     |
| adapting   | to dynamic   | network    |     | conditions | for        | improved |                 |                |        |            |             |                |     |
streamingquality[107]. cations, terahertz band communications, Internet of Nano-
|     |     |     |     |     |     |     | Things) | that will | enable | multimedia | streaming | in the | era of |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ---------- | --------- | ------ | ------ |
6Gnetworks[2],[110].
5) NETWORKSLICINGFORCUSTOMIZEDSERVICES
Network slicing is a technique that enables a single phys- These technologies will play a vital role in support-
ical network infrastructure to be partitioned into multiple ing interactive applications such as live streaming, online
independent virtual networks, known as ‘‘slices.’’ Each gaming, and remote collaboration, where low latency is
| 157424 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
essentialtomaintainingahigh-qualityuserexperience[111].
AdvancedalgorithmsandAI-driventechniqueswilldynami-
callyoptimizevideostreamingparameterstodeliverthebest
| possible  | viewing   | experience |           | tailored | to each   | user.   | As video |     |     |     |     |     |     |     |
| --------- | --------- | ---------- | --------- | -------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| streaming | continues |            | to expand | across   | different | sectors | and      |     |     |     |     |     |     |     |
usecases,6Gnetworkswillincorporatestrongersecurityand
| privacy | protections | to  | safeguard | user | data, | preserve | content |     |     |     |     |     |     |     |
| ------- | ----------- | --- | --------- | ---- | ----- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
integrity,andsecurenetworkinfrastructures.Thesemeasures
| will include | end-to-end |     | encryption, |     | robust | authentication |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ----------- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mechanisms,andprivacy-preservingtechnologies[111].
| Mingming           |     | et al. [112] | propose              |     | a QoE-aware | multi-path    |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | -------------------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| video transmission |     |              | and multi-connection |     |             | framework     | for |     |     |     |     |     |     |     |
| 5G/6G-based        |     | network      | architectures,       |     | aimed       | at maximizing |     |     |     |     |     |     |     |     |
userviewingexperience.Inthisapproach,anSDNcontroller
| is employed | with     | access      | to  | relevant    | network | data,          | enabling |     |     |     |     |     |     |     |
| ----------- | -------- | ----------- | --- | ----------- | ------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| efficient   | resource | utilization |     | and dynamic |         | path switching | in       |     |     |     |     |     |     |     |
wirednetworks.ThisleadstosignificantQoEimprovements
|     |     |     |     |     |     |     |     | FIGURE12. | 6Gkeytechnologiesandtheirrolesforthemulti-user |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
withoutrequiringadditionalnetworkresources[112].
extendedrealitystreamingservices.
| In pursuit |             | of greener | solutions, |     | Hoßfeld        | et  | al. [113] |     |     |     |     |     |     |     |
| ---------- | ----------- | ---------- | ---------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| explore    | the balance |            | between    | QoE | sustainability |     | and CO2   |     |     |     |     |     |     |     |
emissionsincurrentandfuture6Gnetworks.Theirstudyalso
|             |        |            |            |          |          |         |            | Furthermore,  |       | it is worth  | emphasizing |          | that multimedia     |     |
| ----------- | ------ | ---------- | ---------- | -------- | -------- | ------- | ---------- | ------------- | ----- | ------------ | ----------- | -------- | ------------------- | --- |
| considers   | the    | influence  | of ‘‘green |          | users,’’ | who are | willing    |               |       |              |             |          |                     |     |
|             |        |            |            |          |          |         |            | streaming     | in 6G | networks     | is          | expected | to transform        | how |
| to tolerate | minor  | reductions |            | in video | quality  | in      | exchange   |               |       |              |             |          |                     |     |
|             |        |            |            |          |          |         |            | users consume |       | and interact | with        | digital  | content. Leveraging |     |
| for lower   | carbon | emissions, |            | aligning | with     | the     | transition |               |       |              |             |          |                     |     |
toward eco-friendly network and service infrastructures AI and machine learning, 6G will enable the prediction of
userbehavior,analysisofnetworkconditions,andreal-time
poweredbygreenenergy.HenriqueandPrasad[114]outline
|             |         |     |         |           |     |                 |     | adaptation | of streaming |     | parameters | to  | ensure optimal | QoE. |
| ----------- | ------- | --- | ------- | --------- | --- | --------------- | --- | ---------- | ------------ | --- | ---------- | --- | -------------- | ---- |
| a strategic | roadmap |     | for the | evolution | of  | next-generation |     |            |              |     |            |     |                |      |
Withitspromiseofseamlessconnectivity,ultra-lowlatency,
| multimedia | streaming |     | services | in  | the era | of 6G. | Mean- |     |     |     |     |     |     |     |
| ---------- | --------- | --- | -------- | --- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
andsuperiorvideoquality,6Gispoisedtoredefinethefuture
| while, the | authors | of  | [115] | introduce | ALIVE—a |     | latency- |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ----- | --------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ofdigitalmediaconsumptionandcommunication[2].
| and cost-aware |            | hybrid | P2P-CDN |            | framework | designed     | for  |     |     |     |     |     |     |     |
| -------------- | ---------- | ------ | ------- | ---------- | --------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
| live video     | streaming. |        | ALIVE   | integrates |           | cutting-edge | net- |     |     |     |     |     |     |     |
working paradigms, including edge computing and NFV, C. 6G-BASEDMETAVERSEFORMULTI-USEREXTENDED
REALITYSTREAMING
| along with | advanced |     | video | technologies |     | such | as HTTP |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | ------------ | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
Adaptive Streaming (HAS), video super-resolution, and The Metaverse is emerging as the next evolution of the
distributed video transcoding, to efficiently fulfill peer traditional mobile Internet, offering a fully immersive,
streaming requests while maintaining acceptable latency global virtual environment that facilitates social interaction,
andQoE. collaborativework,andmulti-userengagement.1 Tosupport
|             |     |        |               |     |          |             |     | eXtended | Reality | (XR)—a | collective | term | for technologies |     |
| ----------- | --- | ------ | ------------- | --- | -------- | ----------- | --- | -------- | ------- | ------ | ---------- | ---- | ---------------- | --- |
| Barakabitze |     | et al. | [116] present |     | QoESoft, | a QoE-aware |     |          |         |        |            |      |                  |     |
SDN/NFVarchitecturedesignedtoenhancevideostreaming spanning the reality–virtuality spectrum, including VR,
services by improving end-user Quality of Experience AR, and Mixed Reality (MR). The Metaverse relies on
(QoE) through dynamic management of link and switch the integration of several foundational technologies includ-
resources in 5G/6G networks. Within this architecture, the ing the Internet of Things (IoT), Internet of Everything
|         |           |     |     |             |     |                 |     | (IoE), Open | Radio | Access | Networks |     | (Open RAN), | Multi- |
| ------- | --------- | --- | --- | ----------- | --- | --------------- | --- | ----------- | ----- | ------ | -------- | --- | ----------- | ------ |
| authors | introduce | two | key | components: |     | the QoE-sdnFlow |     |             |       |        |          |     |             |        |
Monitor and QoE-sdnFlow Manager, which operate within access Edge Computing (MEC), AI, and cloud-native
SDN/NFV environments to monitor and optimize the uti- infrastructures[117].
|          |            |     |           |           |     |            |      | With the | advent | of 6G | networks, | these | technologies | will |
| -------- | ---------- | --- | --------- | --------- | --- | ---------- | ---- | -------- | ------ | ----- | --------- | ----- | ------------ | ---- |
| lization | of network |     | and media | resources |     | associated | with |          |        |       |           |       |              |      |
virtual links and nodes. Additionally, the paper offers befurtherempoweredbyultra-high-speedconnectivity,ultra-
lowlatency,andpervasiveintelligenceattheedge,enabling
| preliminary | evaluations |     | of  | video | quality | in relation | to  |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
virtual network survivability and provides an economic seamless, high-fidelity XR experiences. Applications such
analysis focused on maximizing profits for OTT providers as VR-based online education and multi-user gaming—
|          |       |                |     |           |     |          |      | where many |     | users simultaneously |     | experience |     | the same |
| -------- | ----- | -------------- | --- | --------- | --- | -------- | ---- | ---------- | --- | -------------------- | --- | ---------- | --- | -------- |
| and ISPs | while | simultaneously |     | improving |     | customer | QoE. |            |     |                      |     |            |     |          |
Experimental results demonstrate that QoESoft signifi- volumetriccontent—willbecomeincreasinglysophisticated
| cantly outperforms |          | baseline |     | methods      | in  | metrics  | such as  |     |     |     |     |     |     |     |
| ------------------ | -------- | -------- | --- | ------------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| switch             | and link | resource |     | utilization, |     | low live | latency, |     |     |     |     |     |     |     |
1Multi-userXRcollaborationreferstobringingtogethergroupsofpeople
| bitrate adaptation, |     | startup | delays, |     | video | quality, | and stall |            |             |         |           |              |                 |     |
| ------------------- | --- | ------- | ------- | --- | ----- | -------- | --------- | ---------- | ----------- | ------- | --------- | ------------ | --------------- | --- |
|                     |     |         |         |     |       |          |           | for remote | activities, | such as | meetings, | conferences, | design reviews, | and |
durations. classroomsessionsthroughtheuseofXRdevicesandtechnologies[117].
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 157425 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
and engaging, surpassing the limitations of single-user XR LossFair(OPLF),andtheBarrierFunction(BF)arethethree
interactions. schedulersthattheauthorsuse.WhiletheOPLFenhancesthe
Fig. 12 indicates key technologies and their roles for the network’sperformancewithregardtopacketlossrate,theBF
multi-userextendedrealitystreamingservicein6Gnetworks. ensuresthattherequiredvideobitrateismet.
360◦
Blockchainwillenablestransparentanddecentralizeddigital During video transmission, the packet latency is
proofsofownership,valuetransfer,collectibility,accessibil- reducedusingtheEXPrule[123].Theproposed5Gscheduler
ity,governance,andinteroperabilityintheMetaverse.While can serve as a starting point for creating cutting-edge
AI will enable users to build incredibly realistic avatars reinforcement learning techniques that can figure out and
and have multilingual accessibility [118], IoT will allow forecastend-usersatisfactionwithQoSandQoEforvarious
Metaversetomapdatafromreallifeandtranslatetheminto traffic types of video content. It is important to note that
VR[117]. the Actor-Critic (AC) methods achieve improved QoS/QoE
6G-enabled edge intelligence presents transformative performance if BF, OPLF, and EXP scheduling policies
opportunities for the IoE, enabling seamless connectivity are coupled for various video content types at varying
between people, devices, and cloud infrastructures anytime TransmissionTimeIntervals(TTI)oflessthan1ms.
andanywherethroughEdgeAI.IntheMetaverse,QoS/QoE
|         |           |     |      |                 |     |     |          | D. THEROLEOFBLOCKCHAININMETAVERSEVIDEO |     |     |     |     |     |     |
| ------- | --------- | --- | ---- | --------------- | --- | --- | -------- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
| will be | redefined | by  | both | visual fidelity |     | and | physical |                                        |     |     |     |     |     |     |
interactionparameters,particularlythroughVRsystemsthat STREAMINGTRANSACTIONS
TheintegrationofblockchaintechnologyinMetaverse-based
mayrequirevideobitratesofupto1Gbpstosupportlifelike
streamingexperiences. video streaming addresses security, decentralization, micro-
|            |      |           |         |     |               |     |        | payments, | and        | content     | ownership. |         | In traditional | video   |
| ---------- | ---- | --------- | ------- | --- | ------------- | --- | ------ | --------- | ---------- | ----------- | ---------- | ------- | -------------- | ------- |
| Widespread |      | adoption  | of MDs, | AR  | glasses,      | and | haptic |           |            |             |            |         |                |         |
|            |      |           |         |     |               |     |        | streaming | platforms, | centralized |            | service | providers      | control |
| gloves has | made | immersive | access  | to  | the Metaverse |     | more   |           |            |             |            |         |                |         |
feasible,butitalsointroducesstringentrequirements,suchas datadistribution,contentmonetization,anduserinteractions.
However,blockchainfacilitatestrustless,peer-to-peer(P2P)
motion-to-photon(MTP)latencyoflessthan20milliseconds
tomaintainfluidusermovementinvirtualenvironments.Fur- streaming, eliminating intermediaries and ensuring fair
thermore,real-timetransmissionandhighlyreliablefeedback compensation for content creators [124], [125]. One of
|           |           |             |     |              |         |          |     | the primary | use | cases | of blockchain |     | in Metaverse | video |
| --------- | --------- | ----------- | --- | ------------ | ------- | -------- | --- | ----------- | --- | ----- | ------------- | --- | ------------ | ----- |
| of haptic | data will | be critical |     | for ensuring | control | accuracy |     |             |     |       |               |     |              |       |
and tactile responsiveness, especially in latency-sensitive streaming is decentralized content distribution networks
|     |     |     |     |     |     |     |     | (dCDNs). | Blockchain-based |     | dCDNs, |     | combined | with dis- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------ | --- | -------- | --------- |
applicationslikeimmersivegamingandultra-high-resolution
videostreaming(e.g.,8K/12K)over6Gnetworks. tributed ledger technology (DLT), enhance content delivery
The convergence of 6G and MEC will ensure ubiqui- efficiency,reducelatency,andoptimizebandwidthutilization
|                   |     |     |           |        |          |     |       | by incentivizing |     | nodes | to share | storage |     | and processing |
| ----------------- | --- | --- | --------- | ------ | -------- | --- | ----- | ---------------- | --- | ----- | -------- | ------- | --- | -------------- |
| tous connectivity |     | and | computing | power, | enabling |     | heavy |                  |     |       |          |         |     |                |
processing tasks to be offloaded to edge servers. This power [126], [127]. This model reduces reliance on cen-
|              |                |     |     |                |     |           |     | tralized | cloud | providers | and ensures |     | resilient, | censorship- |
| ------------ | -------------- | --- | --- | -------------- | --- | --------- | --- | -------- | ----- | --------- | ----------- | --- | ---------- | ----------- |
| will support | data-intensive |     | and | time-sensitive |     | Metaverse |     |          |       |           |             |     |            |             |
applications while maintaining high QoS and QoE for resistantvideostreaming.Additionally,smartcontractsplay
end users. Fengetal. [119] propose a QoE fairness-based acrucialroleinautomatingtransactionsinMetaversevideo
streaming.Throughtoken-basedmicropayments,viewerscan
| resource | allocation | framework |     | for wireless |     | VR in | digital |     |     |     |     |     |     |     |
| -------- | ---------- | --------- | --- | ------------ | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
twinenvironments.Theyintroducealinearweightingmodel pay for content on-demand, ensuring fair compensation for
|                |     |     |                      |     |     |     |         | streamers | without | relying | on third-party |     | payment | gateways, |
| -------------- | --- | --- | -------------------- | --- | --- | --- | ------- | --------- | ------- | ------- | -------------- | --- | ------- | --------- |
| that optimizes | QoE | for | the worst-performing |     |     | HMD | clients |           |         |         |                |     |         |           |
by balancing service delay, video quality, and energy [128].Moreover,non-fungibletokens(NFTs)enablecontent
efficiency. Pan et al. [120] present a cross-layer optimiza- ownership authentication, rights management, and revenue-
|                   |     |               |     |          |              |     |      | sharing | models, | allowing | creators | to  | monetize | their work |
| ----------------- | --- | ------------- | --- | -------- | ------------ | --- | ---- | ------- | ------- | -------- | -------- | --- | -------- | ---------- |
| tion architecture |     | for real-time |     | XR video | transmission |     | that |         |         |          |          |     |          |            |
enhances user QoE using a transformer-based proximal transparently[129],[130].
|                     |     |           |     |              |     |       |         | Blockchain | also | enhances | privacy |     | and security | in video |
| ------------------- | --- | --------- | --- | ------------ | --- | ----- | ------- | ---------- | ---- | -------- | ------- | --- | ------------ | -------- |
| policy optimization |     | algorithm |     | for adaptive |     | video | bitrate |            |      |          |         |     |              |          |
management. Additionally, Yuetal. [121] propose a 6G- streaming by enabling zero-knowledge proofs (ZKPs) and
based Metaverse architecture designed for dynamic and decentralized identity management (DID). These mecha-
nismsallowuserstoauthenticateandstreamcontentwithout
| deterministic | multi-user |     | XR services. |     | Their | system, | named |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------------ | --- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
PRECISENESS,isanAI-drivenorchestratorthatefficiently exposing personal data to centralized entities [131], [132].
|            |     |          |            |               |     |           |     | By leveraging |     | blockchain, | Metaverse |     | streaming | platforms |
| ---------- | --- | -------- | ---------- | ------------- | --- | --------- | --- | ------------- | --- | ----------- | --------- | --- | --------- | --------- |
| provisions | XR  | services | to deliver | high-quality, |     | immersive |     |               |     |             |           |     |           |           |
multi-userexperiences. can prevent piracy, ensure transparent royalty distribution,
Comsa et al. [122] present the idea of a Reinforcement andestablishimmutabledigitalrightsforcontentcreators.
360◦
| Learning | (RL)-based | architecture |     | called |     | MULTIPLE |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------------ | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
SENSORIAL MEDIA (MULSEMEDIA) that can offer end E. 6G-DRIVENHOLOGRAPHICTELEPRESENCE,
PERSONALIZEDMEDIA,INTERNETOFSENSES(IoS)AND
usersin5GsystemsgoodQoS/QoE.A5Gradioscheduleris
360◦
suggested to broadcast multimedia contents according INDUSTRIALIoT
to factors like users, channel circumstances, and 360◦ 6G-driven holographic telepresence, personalized media,
mobility.TheEXPonential(EXP)rule,OpportunisticPacket industrial IoT and the Internet of Senses (IoS) represent
| 157426 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE11. Asummaryofemergingtrendsandtechnologiesformultimedia6Gnetworks.
the next frontier in immersive video communication and valuation [137]. The simulation indicates that the proposed
media experiences. It allows people to interact in real-time architecture achieves 92% optimal social welfare at a 37%
through3Dholograms,creatingasenseofphysicalpresence auctioninformationexchangecostforanMLP-basedactor.
|             |      |           |        |                     |     |       | Anmulwar | et  | al. [135] | introduce | HoloSync, |     | an edge- |
| ----------- | ---- | --------- | ------ | ------------------- | --- | ----- | -------- | --- | --------- | --------- | --------- | --- | -------- |
| even across | vast | distances | [133], | [134]. Personalized |     | media |          |     |           |           |           |     |          |
will leverage AI and 6G’s ultra-high bandwidth to deliver computing-based framework that can achieve a controllable
contenttailoredinreal-timetoindividualpreferences,moods, frame synchronisation performances for multi-source holo-
and contexts, offering a hyper-personalized entertainment graphic multimedia teleportation applications in future 6G
experience. The Internet of Senses (IoS) goes beyond systems. The authors presents experiments on a real system
traditionalmediabyintegratingallfivehumansenses(sight, with the HoloSync mechanism while considering frame
hearing, touch, taste, and smell) into digital experiences, synchronisationperformancesinspecificnetworkscenarios.
creatingafullyimmersiveenvironmentwhereuserscanfeel, Peixeiro et al. [138] provides a holographic data coding
smell, or even taste virtual content. This will revolutionize strategiesalongwithbenchmarkingandextensionofHEVC
industries like video entertainment, education, and remote With adapted transforms. Huang et al. [139] examines the
collaboration. Table 11 indicates a summary of emerging mostrecentmethodsfortransmittingholographicpointvideo
trendsandtechnologiesformultimedia6Gnetworks. cloud footage and emphasizes the significant difficulties
|     |     |     |     |     |     |     | in providing | such        | immersive | services.  | The         | authors | also  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --------- | ---------- | ----------- | ------- | ----- |
|     |     |     |     |     |     |     | present      | a prototype | of an     | AI-powered | holographic |         | video |
1) MULTIMEDIASTREAMINGINHOLOGRAPHIC
|     |     |     |     |     |     |     | communication |     | system and | provide | important | experimental |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------- | --------- | ------------ | --- |
TELEPRESENCE
findingstoassessitsfunctionality.
Holographictelepresence,enabledby6G’sultra-high-speed
|                 |     |                |      |       |          |          | It is     | important | to mention     | that | holographic     |     | video as  |
| --------------- | --- | -------------- | ---- | ----- | -------- | -------- | --------- | --------- | -------------- | ---- | --------------- | --- | --------- |
| and low-latency |     | connectivity,  | will | allow | for the  | seamless |           |           |                |      |                 |     |           |
|                 |     |                |      |       |          |          | indicated | in Fig.   | 13, as opposed |      | to conventional |     | VR, 360◦, |
| transmission    | of  | 3D holographic |      | video | contents | in real- |           |           |                |      |                 |     |           |
andother3-DoFvideos,offersusersanimmersivesixdegrees
| time. This | means | that users | can experience |     | live | multimedia |     |     |     |     |     |     |     |
| ---------- | ----- | ---------- | -------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
offreedom(6-DoF)watchingexperience.Userswillbeable
streamingevents,concerts,orvideomeetingsasiftheywere
towalkaroundanobjectinacircleandseeitfrombothabove
physicallypresent,enhancingtheimmersionandengagement
|                  |     |                  |        |            |           |          | and below  | using | 6-DoF films. | A        | new method   | called | tensor  |
| ---------------- | --- | ---------------- | ------ | ---------- | --------- | -------- | ---------- | ----- | ------------ | -------- | ------------ | ------ | ------- |
| of multimedia    |     | streaming [135]. | Duan   | et         | al. [136] | presents |            |       |              |          |              |        |         |
|                  |     |                  |        |            |           |          | holography | could | enable the   | creation | of holograms |        | for VR, |
| key technologies |     | that will        | enable | multimedia |           | semantic |            |       |              |          |              |        |         |
3Dprinting,medicalimaging,andmore.IntegratingAIwith
| communications |     | over 6G | systems | including |     | holographic |          |            |       |      |                   |     |          |
| -------------- | --- | ------- | ------- | --------- | --- | ----------- | -------- | ---------- | ----- | ---- | ----------------- | --- | -------- |
|                |     |         |         |           |     |             | hologram | technology | could | also | create a powerful |     | synergy, |
videoprojection,whichinvolvesemanticencoding/decoding,
offeringnewdimensionsofinteractivityandrealism.
| end-to-end      | semantic | communication    |     |             | systems, | semantic     |     |     |     |     |     |     |     |
| --------------- | -------- | ---------------- | --- | ----------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| representation, |          | and transmission |     | of semantic |          | information. |     |     |     |     |     |     |     |
Zhang et al. [137] presents a learning-based actor-critic- 2) PERSONALIZEDVIDEO-BASEDSTREAMING
based deep reinforcement learning (DRL) architecture for Personalized video-based streaming takes multimedia
matchingdemandandsupplyofholographicdigitaltwinover streamingtothenextlevelbytailoringcontenttoindividual
immersive communications. The architecture consists of a preferencesandcontexts[140].Forexample,videostreaming
marketplace for HDT services, and leverage a formulated platforms today dynamically adjust recommendations or
Double Dutch Auction (DDA) strategy for optimizing the adjust content (e.g., switching between audio, video, or VR
matching and pricing based on both user and provider formats) depending on user preferences, time of day,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 157427 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
|     |     |     |     |     |     | FIGURE14. | InternetofSensesandmetaversetosupportmultisensory |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
mediaandsemanticcommunications[144].
|     |     |     |     |     |     | the digital | experience | [143]. | Through | IoS-enabled |     | devices |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------ | ------- | ----------- | --- | ------- |
FIGURE13. HolographicVideoCommunicationswithanimmersivesix and interfaces, users will not only see and hear multimedia
degreesoffreedom(6-DoF)viewingexperience. content but also feel, taste, and smell virtual environments.
|     |     |     |     |     |     | This immersive    |     | technology | will open       | up  | new         | possibilities |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | --------------- | --- | ----------- | ------------- |
|     |     |     |     |     |     | for storytelling, |     | gaming,    | and interactive |     | experiences | in            |
orenvironmentalconditions.Personalizedmediawillevolve multimediastreamingin6Gnetworks.Throughthecreation
|        |                 |     |       |        |               | of a completely |     | immersive | environment |     | that breaks | down |
| ------ | --------------- | --- | ----- | ------ | ------------- | --------------- | --- | --------- | ----------- | --- | ----------- | ---- |
| beyond | recommendations | to  | offer | deeply | immersive and |                 |     |           |             |     |             |      |
user-specific media experiences, potentially using VR/AR, traditionalboundaries,theIoSconceptasindicatedinFig.14
holographicdisplays,andevensensory-basedcontent[140]. ispoisedtotransformdigitalinteractions.
This level of personalization improves user satisfaction TheIoSoffersamoreengagingcyberworldwherevirtual
and retention on multimedia streaming platforms [141]. encountersareasrichandmulti-dimensionalastherealworld
|            |                 |           |     |     |                   | by fusing | sensory | experiences—such |     | as  | Internet | of Sight, |
| ---------- | --------------- | --------- | --- | --- | ----------------- | --------- | ------- | ---------------- | --- | --- | -------- | --------- |
| Ahn et al. | [141] introduce | a dynamic |     | and | super-ersonalized |           |         |                  |     |     |          |           |
media ecosystem driven by generative AI video generators Internet of Sound, Internet of Touch, Internet of Smell, and
which shift part of the content creation onto the receiver. Internet of Taste—with the digital domain [144]. The next
Instead of sending encoded video data of fully finished frontiers in IoS through 6G and current technologies that
programs, the authors introduce a semantic process into the are powering immersive multi-sensory media are explored
|           |              |                  |     |         |            | in [144]. | This | investigation | involves |     | a comparison | of  |
| --------- | ------------ | ---------------- | --- | ------- | ---------- | --------- | ---- | ------------- | -------- | --- | ------------ | --- |
| framework | that enables | the distribution |     | network | to deliver |           |      |               |          |     |              |     |
multimedia service elements that prompt the content pro- traditional immersive media streaming with a suggested
ducer.Thenextsectionprovidesadescriptionofmultimedia use case that makes use of generative AI-enabled semantic
streamingQoEinIoS. communication. Joda et al. [145] provide details on how
Personalizedvideo-basedstreamingservices,whichtailor 6G technology, together with newly developing AI/ML and
content based on user preferences, present several ethical semantic communications paradigms, may be able to meet
concerns that need to be addressed. One major issue is the needs of IoS use cases. It is important to mention
privacy, as these services rely on extensive data collection, that IoS has the potential to revolutionize multimedia
including viewing habits and personal information, poten- communications by integrating human sensory experiences
tially leading to breaches of user privacy if not handled intodigitalinteractions.
| responsibly | [142]. Additionally, |     | the | algorithms | used for |     |     |     |     |     |     |     |
| ----------- | -------------------- | --- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
content recommendations can reinforce biases and limit 4) THEREAL-TIMEVIDEOSTREAMINGFOR6GINDUSTRIAL
| the diversity | of content | available, |     | as they | may prioritize |     |     |     |     |     |     |     |
| ------------- | ---------- | ---------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
INTERNETOFTHINGS(IIoT)
popular genres or opinions, excluding less mainstream The evolution of the Industrial Internet of Things (IIoT)
voices. This can lead to the formation of echo chambers, into the 6G era is driven by the need for ultra-reliable,
| where users | are exposed | mainly |     | to content | that aligns |             |               |     |         |     |               |      |
| ----------- | ----------- | ------ | --- | ---------- | ----------- | ----------- | ------------- | --- | ------- | --- | ------------- | ---- |
|             |             |        |     |            |             | low-latency | communication |     | (URLLC) |     | and real-time | data |
withtheirexistingviews,reducingcriticalengagementwith streaming. Advanced video streaming frameworks in 6G
diverseperspectives[142].Furthermore,themanipulationof
IIoTintegrateedgecomputing,AI,andblockchaintoensure
userchoices,subtlenudgestowardsspecificcontent,andthe secure,high-speed,andefficientdatatransmission.Research
lackoftransparencyregardingdatacollectionpracticesraise by Zhang et al. [146] highlights the role of AI-driven
| concerns | about the erosion | of  | user autonomy |     | and informed |                |     |               |      |       |     |          |
| -------- | ----------------- | --- | ------------- | --- | ------------ | -------------- | --- | ------------- | ---- | ----- | --- | -------- |
|          |                   |     |               |     |              | edge computing |     | in optimizing | data | flows | and | reducing |
consent. These ethical issues underscore the need for more latency in IIoT environments, allowing real-time adaptive
| transparent, | fair, and responsible |     | practices |     | in personalized |     |     |     |     |     |     |     |
| ------------ | --------------------- | --- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
streamingsolutions.Similarly,Zhangetal.[146]proposean
contentrecommendationsystems. energy-efficient federated learning approach that enhances
|     |     |     |     |     |     | data processing |     | capabilities | while | ensuring | minimal | energy |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | ----- | -------- | ------- | ------ |
3) MULTIMEDIASTREAMINGINIoS consumptionforIIoTnodes.Moreover,ahybrid6G-enabled
The 6G-driven Internet of Senses (IoS) further will enrich network slicing approach has been suggested by Kim et al.
multimedia streaming by incorporating human senses into [147], where network resources are dynamically allocated
| 157428 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE12. Asummaryofvideocodingstandards,maintechniquesandimpactsonvideostreaming.
based on real-time streaming requirements, ensuring robust codecs. New video compression standards in 6G networks
connectivity and minimal transmission delays in industrial will leverage AI and ML techniques in video codecs to
settings. better adapt to the complexity of video content, resulting in
Further advancements in IIoT real-time streaming focus improvedcompressionperformanceandreducedbandwidth
on integrating blockchain to enhance data integrity and requirements.Thecompressionstandardsover6Gnetworks
prevent cyber threats. According to Wang et al. [148], will also perceptual video coding techniques that focus on
a blockchain-based Quality of Service (QoS) framework optimizing compression efficiency based on human visual
ensurestamper-proofdatatransmissionforindustrialapplica- perception taking into account perceptual characteristics
tions,effectivelysecuringIIoTstreamsagainstunauthorized (e.g.,visualacuity,colorsensitivity,andmotionperception)
modifications.Additionally,researchbyAhmedetal.[149] resultinginhigherperceivedqualityatlowerbitrates[152].
360◦
emphasizestheroleofsemanticcommunicationin6G-based Moreover, VVC provides discrete sub-pictures for
IIoT, where intelligent algorithms optimize data compres- video tiled streaming applications, allowing for greater
sion and transmission efficiency, reducing overhead while resolution for the visible section of the 360◦ video. A per-
maintaining real-time streaming reliability. Future research formancecomparisonofH.265,VVC,andEVCintermsof
directions suggest combining terahertz (THz) communica- codingimprovementsandcomputingcomplexityisgivenby
tion with AI-driven predictive analytics to further enhance Grois et al. [153]. The findings show that when encoding
IIoTreal-timestreamingcapabilities,ensuringdeterministic 4K/2160p entertainment video (such as VoD), EVC offers
performanceformission-criticalapplicationsinIndustry5.0. bandwidth reductions of about 30% when compared to
|     |     |     |     |     |     |     | HEVC, while | VVC offers        | bitrate    | savings | of      | roughly 40%. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | ---------- | ------- | ------- | ------------ |
|     |     |     |     |     |     |     | Using a     | layer referencing | technique, |         | HoangVa | et al. [154] |
F. NEWVIDEOCOMPRESSIONSTANDARDSTOWARDS6G
NETWORKS present a VVC-based quality scalability strategy that pro-
The emerging applications and use cases in 6G networks vides improved compression efficiency by combining the
decodedinformationfromthebaseandenhancementlayers
| require new | video | compression |     | standards | that | will offer |     |     |     |     |     |     |
| ----------- | ----- | ----------- | --- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
advanced capabilities compared to the video codecs in use to generate a new enhancement layer coding reference.
AperformanceevaluationcomparisonofVP9,VVC,HEVC,
today(H.265/MPEG-4AVC,GoogleVP9,MPEGDynamic
Adaptive Streaming over HTTP (MPEG-DASH and others) AVI, and H.264 encoders for low-latency video services
[2],[3].VersatileVideoCoding(VVC)orH.266,registered and applications is proposed by Esakki et al. [155] When
|          |                |     |               |     |         |        | compared | to the most | pertinent | benchmarks |     | in the video |
| -------- | -------------- | --- | ------------- | --- | ------- | ------ | -------- | ----------- | --------- | ---------- | --- | ------------ |
| as ITU-T | Recommendation |     | H.266|ISO/IEC |     | 23090-3 | is the |          |             |           |            |     |              |
latest video compression standard developed by the Joint coding industry standards, VVC gives the best compression
|     |     |     |     |     |     |     | performance | while VP9 | offers | average | bit-rate | overhead. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------ | ------- | -------- | --------- |
VideoExpertsTeam(JVET)oftheITU-TandMPEGofthe
ISO/IEC.Itofferssignificantimprovementsincompression Becauseofitsunparalleledapplicationadaptability,theVVC
efficiency compared to its predecessors, such as HEVC standardwillbothconcludethelasttenyearsofvideocoding
|           |          |                |         |       |           |               | standardization | and improve |     | the state | of the | art in video |
| --------- | -------- | -------------- | ------- | ----- | --------- | ------------- | --------------- | ----------- | --- | --------- | ------ | ------------ |
| (H.265),  | enabling | higher-quality |         | video | streaming | at lower      |                 |             |     |           |        |              |
| bitrates. | VVC is   | expected       | to play | a key | role      | in delivering | compression.    |             |     |           |        |              |
Fig.15showsdifferentapplicationareasofVVCin6Gand
| ultra-high-definition |     | video | content | in  | 6G networks | and |     |     |     |     |     |     |
| --------------------- | --- | ----- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
beyond [2], [150]. Table 12 presents a summary of video beyondnetworkssuchasimmersiveXRandtelepresenceand
coding standards, main techniques and impacts on video extremelylowlatencycloudgamingetc.
streaming.
KeyfeaturesofH.266/VVCinclude:operatingwith64× G. INTEGRATIONOFAIANDFUTUREVIDEOCODING
×
| 64 sample | size transforms |     | and block | sizes | of  | up to 128 | TRENDS |     |     |     |     |     |
| --------- | --------------- | --- | --------- | ----- | --- | --------- | ------ | --- | --- | --- | --- | --- |
128 pixels [151], reduction in bitrate of around 40% for AIisplayingatransformativeroleintheevolutionofvideo
existing HD and 4K/8K video services that are deployed compressionfor6G.AI-drivencodecs,suchasNeuralVideo
usingHEVC(atthesamevisualquality),support6G-driven Coding(NVC)[156],usedeeplearningmodelstooptimize
low-delay video coding and immersive video, and achieve compression by predicting patterns, reconstructing data
thehighestcompressionefficiencycomparedtoothervideo efficiently,andadaptingtovaryingnetworkconditions.These
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 157429 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
|     |     |     |     |     |     |     | to define | QoE | metrics | or models | explicitly |     | embedded | in its |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --------- | ---------- | --- | -------- | ------ |
reasoningcomponents.Theuseofmobilenodesforcoverage
adaptationisparticularlybeneficialformultimediacontinuity
|     |     |     |     |     |     |     | in dynamic | and | mission-critical |     | environments, |     | e.g., | drone |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | ------------- | --- | ----- | ----- |
surveillanceorautonomousdriving.
|     |     |     |     |     |     |     | The 6G        | BRAINS2  |            | project | proposes     | a multi-agent |      | Deep     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ---------- | ------- | ------------ | ------------- | ---- | -------- |
|     |     |     |     |     |     |     | Reinforcement |          | Learning   | (DRL)   | architecture |               | that | performs |
|     |     |     |     |     |     |     | real-time     | resource | allocation |         | over         | new spectrum  |      | domains  |
includingTHzandopticalwirelesscommunications(OWC).
|           |                                                   |     |     |     |     |     | It innovates | in  | AI-based | End-to-End |     | (E2E) | directional | net- |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ---------- | --- | ----- | ----------- | ---- |
| FIGURE15. | DifferentapplicationareasofVVCinfuture6Gnetworks. |     |     |     |     |     |              |     |          |            |     |       |             |      |
workslicing,optimizedforultra-densenetworksandlatency-
|     |     |     |     |     |     |     | sensitive      | applications. |        | The focus | on           | massive | machine-type |      |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | ------ | --------- | ------------ | ------- | ------------ | ---- |
|     |     |     |     |     |     |     | communications |               | (mMTC) |           | and adaptive |         | spectrum     | man- |
AI-enhancedmethodspromisedynamicbitrateadjustments, agement makes it highly relevant for large-scale video
personalizedcontentdelivery,andenhancederrorresilience,
|     |     |     |     |     |     |     | streaming | and | IoT media | applications. |     | 6G  | BRAINS | has |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------------- | --- | --- | ------ | --- |
crucialforsupportingdiverseapplicationsliketelemedicine,
|     |     |     |     |     |     |     | strong QoE-centric |     | design | goals, | explicitly |     | embedding | AI- |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------ | ---------- | --- | --------- | --- |
smart cities, and autonomous vehicles in 6G scenarios. driven QoS/QoE guarantees in slice orchestration. The
| Furthermore, | future | trends | in video | compression |     | standards |         |         |             |          |     |               |     |          |
| ------------ | ------ | ------ | -------- | ----------- | --- | --------- | ------- | ------- | ----------- | -------- | --- | ------------- | --- | -------- |
|              |        |        |          |             |     |           | novelty | lies in | multi-agent | learning |     | coordination, |     | which is |
are focusing on energy efficiency [157] and sustainability particularly powerful in managing the unpredictable traffic
to align with the green computing goals of 6G. These ofvideo-centricappslikeAR/VR.Thechallengeremainsin
| standards | aim to | minimize | the | environmental |     | footprint |             |               |     |          |         |      |               |     |
| --------- | ------ | -------- | --- | ------------- | --- | --------- | ----------- | ------------- | --- | -------- | ------- | ---- | ------------- | --- |
|           |        |          |     |               |     |           | translating | reinforcement |     | learning | outputs | into | interpretable |     |
of video transmission while catering to the increasing QoE models, especially under constrained computational
| global demand | for | rich media | content. |     | This is | achieved by |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | -------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
environments.
reducingcomputationalcomplexityandadoptingdistributed RISE-6GintroducestheuseofReconfigurableIntelligent
processingtechniques[156]. Surfaces (RIS) to dynamically control wireless propagation
| Another | notable | advancement |     | is the MPEG |     | - Omnidirec- |              |        |     |               |      |      |       |           |
| ------- | ------- | ----------- | --- | ----------- | --- | ------------ | ------------ | ------ | --- | ------------- | ---- | ---- | ----- | --------- |
|         |         |             |     |             |     |              | environments | [159]. |     | The project’s | main | goal | is to | create an |
tional Media Format (OMAF), which supports immersive energy-efficient, programmable communication infrastruc-
andinteractiveexperiences.OMAFv2introducesserver-side
turethatcanadapttothehighlyvariableservicerequirements
| dynamic | adaptation, | ensuring |     | seamless | delivery | of 360- |           |           |     |           |            |     |            |     |
| ------- | ----------- | -------- | --- | -------- | -------- | ------- | --------- | --------- | --- | --------- | ---------- | --- | ---------- | --- |
|         |             |          |     |          |          |         | of future | networks, |     | including | multimedia |     | streaming. | The |
degreeandmulti-viewvideoinvaryingnetworkconditions. architecture minimizes connect-compute network reconfig-
Thisalignswith6G’semphasisonultra-reliablelow-latency
|     |     |     |     |     |     |     | uration | costs while |     | enabling | agile | deployment | of  | service |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | -------- | ----- | ---------- | --- | ------- |
communication (URLLC) and enhanced mobile broadband flows. The RISE-6G project indirectly enhances QoE by
(eMBB).
|     |     |     |     |     |     |     | reducing            | latency, | improving |               | throughput, |            | and   | mitigating |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | -------- | --------- | ------------- | ----------- | ---------- | ----- | ---------- |
|     |     |     |     |     |     |     | signal degradation. |          |           | It represents |             | a paradigm | shift | from       |
H. 6GMULTIMEDIASTREAMINGPROJECTS/INITIATIVES network adaptation to environment adaptation. However,
Theacademiaandindustryarecurrentlyleadingininvesting QoE models need to be co-developed with RIS deployment
inresearchanddevelopmenteffortsfocusedon6Gmultime- strategies to optimize media path reliability in real-time,
diastreamingcapabilities.ThedynamiccoverageExtension especiallyformobileorimmersiveservices.
and Distributed Intelligence for human centric applications The 6G-XR project addresses extended reality (XR) and
withassuredsecurity,privacy,andTrust(DEDICAT-6G)has real-timeholographiccommunication,whichareexpectedto
beeninitiatedtoaddresstechniquestoachieveandmaintain be among the most demanding multimedia services in 6G.
an efficient dynamic connectivity and intelligent placement The project leverages cloud-native architectures and edge
| of computation | in  | the mobile | network. |     | The project | designs |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | -------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
computingtomeetstringentlatencyandbandwidthrequire-
anddevelopnewapproachesfordynamiccoverageextension ments. Fig. 18 (referred) highlights its layered deployment
throughtheexploitationofnovelterminalsandmobileclient fromcorecloudtoedgenodestooptimizecontentdelivery.
nodessuchassmartconnectedcars,robots,anddrones. This project places QoE at the center of its architectural
DEDICAT-6G[158]focusesonprovidingmechanismsto vision. XR and holography demand seamless rendering,
realize and ensure trusted information exchange between synchronization, and ultra-low latency. 6G-XR correctly
parties (video service providers), devices and sub-systems. identifiesedgeintelligenceandadaptivecontentplacementas
Moreover,theprojectprovideintelligentsystemcomponents enablers.ThechallengeliesindefiningholisticQoEmetrics
forreasoningonidentificationofpatternsindicatingsecurity, forXR,includingmotion-to-photonlatency,depthaccuracy,
privacy, and trust issues to enable their timely prevention. and user immersion, which are currently underexplored in
WhileDEDICAT-6Gemphasizessecurityandtrust,itsdirect standardQoEframeworks.
| impact on       | multimedia | QoE      | is           | implicit—reliable, |            | secure,  |     |     |     |     |     |     |     |     |
| --------------- | ---------- | -------- | ------------ | ------------------ | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| and dynamically |            | extended | connectivity |                    | inherently | supports |     |     |     |     |     |     |     |     |
2https://5g-ppp.eu/6g-brains/
| consistent | video delivery. |     | However, | further | work | is needed |     |     |     |     |     |     |               |     |
| ---------- | --------------- | --- | -------- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
| 157430     |                 |     |          |         |      |           |     |     |     |     |     |     | VOLUME13,2025 |     |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE13. Asummaryof6Gmultimediastreamingprojects/initiatives.
FIGURE16. TimelineofSmartNetworksandServicesJointUndertaking(SNSJU)toimplement6GEUprojects.
FLECON-6G introduces a flexible and open architecture approach anticipates high-density multimedia transmission
designed to integrate diverse networks into an intelligent needs in 3D mobility environments. The emphasis on
‘‘networkofnetworks.’’TheUNITY-6Gfocusesoncreating mobility,connectivity,and3Dtopologiesisnovel,especially
a sustainable, AI-native framework for 6G infrastruc- in vertical spaces (e.g., drones, in-flight services). While
ture, enabling scalability and efficiency for diverse use promising,NexaSphereneedstoaddresshowQoEcontinuity
cases, including real-time media. Both projects propose ismaintainedacrossheterogeneous,fast-movingnodes,and
system-levelintelligenceandadaptability,whicharecrucial howopticallinksmanagevideodegradationundermobility.
for resilient multimedia streaming in hybrid environments. Acompletelistoftheseprojectsisavailableat[160].
However, they remain high-level architectural frameworks, It is worth noting that these projects demonstrate the
andapplication-specificQoEmodels,suchasthoseforvideo growingconvergencebetweenAI,networkprogrammability,
orXR,needmoreconcreteintegrationandvalidation. and immersive multimedia in 6G. While all introduce
The NexaSphere explores a multi-connected 3D network advanced architectures, their treatment of QoE varies in
modelthatintegratesradioandoptical-wirelesstechnologies specificityanddepth.Projectslike6GBRAINSand6G-XR
toserveaeronautics,automotive,andsmartcitysectors.This present direct, model-driven QoE frameworks, while others
VOLUME13,2025 157431

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
like RISE-6G and DEDICAT-6G lay the groundwork for intelligent, and latency-sensitive multimedia applications.
infrastructure-levelQoEimprovements.Futureeffortsshould In current 5G standards (Release 15–18) [165], 3GPP has
align these architectural innovations with standardized and already introduced mechanisms for QoS Class Identifiers
user-centricQoEmetricstoensuremeasurableimprovements (QCI), 5QI (5G QoS Indicators), and network slicing, all
in6Gmultimediastreaming. of which provide the technical foundation for QoE-aware
|     |     |     |     |     |     | resource   | allocation | and | traffic differentiation |     | in video and      |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ----------------------- | --- | ----------------- |
|     |     |     |     |     |     | multimedia | delivery.  |     | These indicators        |     | are essential for |
I. STANDARDIZATIONANDREGULATORYPERSPECTIVES mappingservice-levelrequirements—suchasbitrate,latency,
FORQoEINMULTIMEDIATOWARDS6GNETWORKS jitter, and packet loss—onto network capabilities, thereby
| The evolution | of  | multimedia | services | towards | 6G networks |     |     |     |     |     |     |
| ------------- | --- | ---------- | -------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
influencingtheend-user’sperceivedquality.
brings the need for robust standardization and regulatory As we move toward 6G, 3GPP is expected to extend
frameworks to ensure consistent QoE across heterogeneous these frameworks to accommodate new classes of mul-
platforms, devices, and user contexts. Multiple standardiza- timedia, including holographic communication, immersive
tionbodies—includingtheInternationalTelecommunication XR, multisensory streaming, and digital twin interactions.
| Union | (ITU-T), | the IEEE, | the 3rd | Generation | Partner- |                |     |              |      |          |             |
| ----- | -------- | --------- | ------- | ---------- | -------- | -------------- | --- | ------------ | ---- | -------- | ----------- |
|       |          |           |         |            |          | This expansion |     | will require | more | granular | QoE metrics |
ship Project (3GPP), and various specialist groups such and real-time analytics, integrated within the 6G system
as The Video Quality Experts Group Immersive Media architecture through AI/ML-based service orchestration.
Group (VQEG-IMG) — have played a significant role in 3GPPisalsofocusingonService-BasedArchitecture(SBA)
establishing QoE metrics, methodologies, and compliance enhancementsandPolicyControlFunctions(PCF)tosupport
| benchmarks | for | multimedia | delivery. | ITU-T | Study Group |           |          |       |             |         |             |
| ---------- | --- | ---------- | --------- | ----- | ----------- | --------- | -------- | ----- | ----------- | ------- | ----------- |
|            |     |            |           |       |             | real-time | feedback | loops | that adjust | quality | dynamically |
12 has been instrumental in defining objective and subjec- based on user context, device type, and application priority.
tive quality models for multimedia applications, including Furthermore,theintegrationofapplication-layermetricsinto
RecommendationsP.910,P.1203,andG.107,whichaddress network control policies is a growing area of research and
audiovisualqualityandend-usersatisfactioninstreamingand standardizationwithin3GPPStudyGroups(SA2,SA5,and
conversationalservices[161]. RAN).ThisincludesthedefinitionofstandardizedAPIsfor
IEEE, through several working groups such as IEEE media session quality reporting and QoE-aware admission
P1918.1 (Tactile Internet) and IEEE 802.1CB (Time- controlmechanisms.Theseinitiativeswillbevitalinenabling
SensitiveNetworking),hascontributedtothestandardization multi-stakeholder QoE assurance, where telecom operators,
of ultra-reliable and low-latency communication required service providers, and application developers collaborate to
for real-time immersive multimedia in 6G environments. deliverconsistentqualityacrossservices[2].
These working groups emphasize end-to-end performance In the 6G era, 3GPP’s regulatory perspective will also
monitoringandtrafficmanagementpolicies,whichareessen- likely emphasize ethics, trust, and privacy, particularly for
| tial for | maintaining | high | QoE in applications |     | such as AR, |     |     |     |     |     |     |
| -------- | ----------- | ---- | ------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
AI-drivenmultimediaapplications,ensuringthatQoEisnot
holography, and cloud gaming [162]. Similarly, the Moving only about technical performance but also user dignity and
Picture Experts (MPEG) Group has introduced standards transparency. The regulatory bodies are expected to enforce
like MPEG-DASH and VVC to support adaptive bitrate interoperability guidelines and cross-domain compliance
streaming and ultra-high-definition media delivery, offering frameworksthatensureQoEcontinuityacrossnetworkslices,
codec-leveloptimizationstrategiestomaintainvisualquality
|     |     |     |     |     |     | devices, | and media | types. | Standardization |     | will likely shift |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --------------- | --- | ----------------- |
acrossdynamicnetworkconditions[163]. towards AI-enhanced metrics, real-time QoE analytics, and
The VQEG and the European QUALINET network have edge-assistedmonitoringtoreflectthecontextualandadap-
advanced methodologies for objective QoE modeling and tive nature of 6G applications. A coordinated effort among
benchmarking. The VQEG’s-IMG has led initiatives to IEEE,ITU-T,3GPP,MPEG,VQEG,andQUALINETwillbe
evaluate360Â◦video,volumetriccontent,andmulti-sensory
essentialincreatingunifiedQoEstandardsforimmersiveand
experiences through hybrid models combining network, interactive media, addressing the ethical, performance, and
application,andperceptualparameters[164].QUALINET’s accessibilityrequirementsofthenext-generationmultimedia
| white papers | and          | standardization | efforts              | have   | outlined key | ecosystem. |     |     |     |     |     |
| ------------ | ------------ | --------------- | -------------------- | ------ | ------------ | ---------- | --- | --- | --- | --- | --- |
| dimensions   | of           | QoE for         | emerging multimedia, |        | supporting   |            |     |     |     |     |     |
| multi-layer  | optimization |                 | and user-centric     | design | principles.  |            |     |     |     |     |     |
These contributions are particularly critical as multimedia J. SUMMARYANDLESSONLEARNED
traffic becomes increasingly intelligent, immersive, and Table 13 provides a summary of 6G multimedia streaming
sensitivetolatencyandpersonalizationin6Gnetworks. projects/initiatives. Emerging trends in multimedia 6G net-
The 3GPP plays a critical role in the standardization of worksaresettoredefinedigitalexperienceswithcutting-edge
mobile broadband technologies, including those related to technologies. Table 12 presents a summary of video coding
QoE for multimedia services. As the telecommunications standards,maintechniquesandimpactsonvideostreaming.
industry transitions from 5G to 6G, 3GPP’s regulatory and This section indicates that 6G-based Metaverse will enable
technical contributions are shaping the future of immersive, real-time,multi-userXRstreamingthroughultra-lowlatency
| 157432 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
andmassivebandwidthtoenhancevirtualcollaborationand
| immersive | environments |     | [166]. | Holographic |     | telepresence, |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------ | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
supportedby6G’sultra-reliablelow-latencycommunication
| (URLLC), | will | revolutionize |     | remote | interactions | with real- |     |     |     |     |     |     |     |     |
| -------- | ---- | ------------- | --- | ------ | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
time3Dhologramsforapplicationslikevirtualmeetingsand
| telemedicine. | Advanced        |     | video   | compression |               | standards, such |     |     |     |     |     |     |     |     |
| ------------- | --------------- | --- | ------- | ----------- | ------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| as VVC        | and AI-enhanced |     | codecs, |             | will optimize | bandwidth       |     |     |     |     |     |     |     |     |
usage,enablinghigh-resolutioncontentstreamingupto16K.
Furthermore,multimediaintheIoSwilldelivermultisensory
experiences,includingtouchandsmell,whilethe6G-driven
| Internet            | of Smart | Systems        | (IoSS) | will       | integrate | AI and IoT |     |     |     |     |     |     |     |     |
| ------------------- | -------- | -------------- | ------ | ---------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| for context-aware,  |          | adaptive       |        | multimedia | services  | in smart   |     |     |     |     |     |     |     |     |
| cities, healthcare, |          | transportation |        | and        | logistics | [167] and  |     |     |     |     |     |     |     |     |
agriculture[3],[168].
|     |     |     |     |     |     |     | FIGURE17. | Thechallengeofimmersivemediaexperienceinfuture |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
V. FUTURECHALLENGESANDRESEARCHDIRECTIONS
networks.
A. EMERGINGAPPLICATIONS,VIDEOSTANDARDSAND
NEWBUSINESSCASES virtualenvironments,areexpectedtobecomeprevalentinthis
next-generationnetworklandscape[2],[172].
1) FUTUREVIDEOCOMPRESSIONSTANDARDSTOWARDS
6GNETWORKS To ensure a seamless and enhanced user experience,
With the rise of immersive video formats like VR and AR, research in QoS/QoE should be a primary focus for immer-
6G networks will require advanced compression standards sivemediain6Gnetworks.Advancementsaimedatimprov-
capable of efficiently handling complex content such as ing key dimensions—such as sound quality, visual fidelity,
|     |     |     |     |     |     |     | and intuitive | user | interaction—are |     | essential, | particularly |     | in  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --------------- | --- | ---------- | ------------ | --- | --- |
360-degreeandvolumetricvideos,whichpresentsignificant
spatialandtemporalchallenges[2].Tosupportstreamingon XR applications over 6G and beyond systems [175]. This
resource-constraineddeviceslikesmartphonesandIoTgad- willrequiretheintegrationofheterogeneouscomputing(e.g.,
gets,thesestandardswillemphasizelow-complexitycoding parallel and distributed processing), cognitive technologies
techniquestoreducecomputationaldemands.Advancements poweredbyAI/ML,andthedevelopmentofnewimmersive
|          |             |     |      |     |           |                | 3D media | platforms | capable |     | of optimizing |     | QoE metrics |     |
| -------- | ----------- | --- | ---- | --- | --------- | -------------- | -------- | --------- | ------- | --- | ------------- | --- | ----------- | --- |
| in video | compression |     | will | be  | essential | for delivering |          |           |         |     |               |     |             |     |
high-quality content across diverse 6G applications while and monitoring parameters across both infrastructure and
meeting evolving user QoE expectations [152]. A com- application layers [2]. Furthermore, novel algorithms must
|            |        |     |          |           |     |                | be developed | to compress |     | ultra-high-definition |     |     | video | (e.g., |
| ---------- | ------ | --- | -------- | --------- | --- | -------------- | ------------ | ----------- | --- | --------------------- | --- | --- | ----- | ------ |
| prehensive | review | of  | encoding | standards |     | is provided by |              |             |     |                       |     |     |       |        |
Huangetal.in[11]. 8K, 16K) and immersive media (e.g., VR/AR), ensuring
|     |     |     |     |     |     |     | high quality | is       | maintained | while       | significantly |         | reducing |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ---------- | ----------- | ------------- | ------- | -------- | --- |
|     |     |     |     |     |     |     | bandwidth    | demands. | In         | the context | of            | dynamic | network  |     |
2) IMMERSIVEMEDIAEXPERIENCEIN6GNETWORKS slicing,bothacademiaandindustryshouldexploremethods
|           |       |              |     |          |     |                   | for real-time | allocation |     | of network | slices | tailored |     | to the |
| --------- | ----- | ------------ | --- | -------- | --- | ----------------- | ------------- | ---------- | --- | ---------- | ------ | -------- | --- | ------ |
| As future | media | technologies |     | continue | to  | evolve, massively |               |            |     |            |        |          |     |        |
interactiveliveeventsanddigitaltwinswillbeprevalentinthe specific requirements of immersive applications, thereby
eraof6Gnetworks.Enhancedremotemultiplayere-gaming ensuring optimal QoS. Additionally, intelligent resource
andextendedremoteparticipationtowardsperceivedphysical management frameworks should be designed to prioritize
presence will be among immersive technologies in 6G immersive media traffic while maintaining overall network
systems. With 3D augmented communication, the digital efficiencyandstability[176].
experiences is getting more immersive, starting with XR AI-driven mechanisms should be developed to anticipate
and evolving toward holographic communication in future network conditions and user behavior, allowing proactive
networks. media delivery adjustments for a seamless experience.
Fully immersive experiences in 6G and beyond will Research into new protocols and encryption methods is
requirestringentstandardsacrossthethreepillarsofimmer- essential to secure immersive media transmission and safe-
sion: intuitive interaction, high-quality audio, and visual guard user privacy. Efficient techniques for compressing,
fidelity [2], [3]. As illustrated in Fig. 17, such experiences transmitting,andrenderingholographicand3Dcontentover
aimtoengagemultiplehumansenses—sight,hearing,smell, 6G should also be explored. As 6G networks move toward
taste,andimagination—duringeventslikelivesports,travel, sustainability,energy-efficientalgorithmsandhardwaremust
or concerts. However, achieving full immersion remains be investigated to minimize power consumption in immer-
challengingduetoperformance,power,andcostlimitations sive streaming. Additionally, new QoE metrics tailored to
of devices in 6G-era systems [169]. Tele-immersive (TI) immersive media should be defined, alongside optimization
applications, enabling real-time, multi-user participation in strategiestoenhanceusersatisfaction[177].
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 157433 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
TABLE14. Challenges,opportunitiesandresearchdirectionsofmultimediastreamingtowards6Gnetworks.
| FIGURE18. | Thechallengesofstreamingover6Gcloud/edgenetworks. |     |     |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
B. ETHICALANDPRIVACYIMPLICATIONS/ISSUESOF reached, challenging transparency and accountability in AI
| AI/MLINQoE |     |     |     | systems[179].      |                   |              |      |
| ---------- | --- | --- | --- | ------------------ | ----------------- | ------------ | ---- |
|            |     |     |     | Privacy is another | critical concern, | as QoE-aware | mul- |
AI/MLinQoEraisessignificantethicalandprivacyconcerns.
Theseincludepotentialbiasanddiscrimination,dataprivacy timedia services increasingly depend on large volumes of
and security, lack of transparency, and the erosion of user data, often collected without explicit consent. Many
user autonomy [178]. Algorithmic bias can lead to unfair AI/ML systems used in video streaming or adaptive bitrate
treatmentofcertaingroups,whilethevastamountofpersonal algorithms access sensitive contextual information, such as
deviceusage,geolocation,andviewinghabits,topersonalize
| data collected | for QoE analysis | poses risks | to privacy and |     |     |     |     |
| -------------- | ---------------- | ----------- | -------------- | --- | --- | --- | --- |
security. Furthermore, the complexity of AI systems can delivery. This raises risks of data misuse, surveillance,
make it difficult to understand how they make decisions, and breaches, particularly in the absence of robust data
impactingaccountabilityandtrust.AI-drivenQoEoptimiza- governanceframeworks.Moreover,thelackofstandardized
tion relies on user data, including behavioral patterns and ethical guidelines for AI deployment in multimedia appli-
preferences,whichcanintroduceimplicitbiasesintotraining cations further complicates compliance with global privacy
datasets.Suchbiasesmayleadtounequalqualitydeliveryor regulations like GDPR or CCPA [180]. As AI continues
contentprioritizationacrossdemographicgroups,potentially to evolve in multimedia QoE, addressing these ethical and
privacychallengesisessentialtoensureusertrust,regulatory
reinforcingsocialdisparities.Furthermore,opaquedecision-
making models, such as deep neural networks, make it compliance, and equitable access to high-quality digital
| difficult to | interpret how or | why certain QoE | outcomes are | experiences. |     |               |     |
| ------------ | ---------------- | --------------- | ------------ | ------------ | --- | ------------- | --- |
| 157434       |                  |                 |              |              |     | VOLUME13,2025 |     |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
| Future      | trends | and research |               | in AI | ethics,      | privacy, | and      |     |     |     |     |     |     |     |
| ----------- | ------ | ------------ | ------------- | ----- | ------------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| fairness    | within | the context  | of multimedia |       | QoE          | will     | increas- |     |     |     |     |     |     |     |
| ingly focus | on     | developing   | transparent,  |       | accountable, |          | and      |     |     |     |     |     |     |     |
user-centricsystemsthatrespectindividualrights.Emerging
| areas include      |     | explainable | AI       | (XAI) | for QoE          | decisions, |        |     |     |     |     |     |     |     |
| ------------------ | --- | ----------- | -------- | ----- | ---------------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| privacy-preserving |     | machine     | learning |       | (e.g., federated |            | learn- |     |     |     |     |     |     |     |
ing)toprotectuserdata,andalgorithmicauditingframeworks
| that detect | and | mitigate | bias in | multimedia | systems. |     | Future |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------- | ---------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
researchshouldalsoexplorepolicy-drivendesignthataligns
withinternationaldataprotectionlaws(e.g.,GDPR),aswell FIGURE19. Futuremultimediastreaminginnewverticalmarketsinthe
as interdisciplinary approaches combining AI, human- eraof6Gandbeyondnetwork.
| computer | interaction, | and | digital | ethics. | Building |     | standard |         |              |       |     |          |                  |     |
| -------- | ------------ | --- | ------- | ------- | -------- | --- | -------- | ------- | ------------ | ----- | --- | -------- | ---------------- | --- |
|          |              |     |         |         |          |     |          | provide | foundational | tools | for | building | this intelligent | 6G  |
benchmarksforethicalAIinmultimediaQoEandfostering
inclusive datasets will be essential to ensure equitable and infrastructure[111],[182].
trustworthyexperiencesinnext-generationnetworks.
|     |     |     |     |     |     |     |     | D. MULTIMEDIASTREAMINGINNEWVERTICALSAND |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
C. 3DSTREAMINGCLOUD/EDGEMULTIMEDIA NEXT-GENERATIONMOBILETECHNOLOGIES
|     |     |     |     |     |     |     |     | Next-generation |     | mobile | technologies, |     | especially | 6G, will |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ------------- | --- | ---------- | -------- |
STREAMINGIN6GNETWORKS
Streaming platforms like YouTube, Netflix, and VUDU transform digital interaction by enabling advanced applica-
now offer a range of 3D video content via subscription tionsacrossmultiplesectors[108].Network2030envisions
services [11]. However, delivering 3D multi-view video qualitativecommunicationserviceslikeholographiccommu-
remains a challenge for future mobile Internet due to high nications, digital teleportation, and tactile interactions with
|              |     |                 |     |            |     |        |       | high reliability | and | near-zero | packet | loss | [110]. The | rise of |
| ------------ | --- | --------------- | --- | ---------- | --- | ------ | ----- | ---------------- | --- | --------- | ------ | ---- | ---------- | ------- |
| data demands |     | and sensitivity |     | to latency | and | packet | loss. |                  |     |           |        |      |            |         |
As we transition to 6G, it is essential to explore the space-basedInternetvialow-earthorbit(LEO)satelliteswill
impact of IP mobility management on 3D video streaming helpreducelatencytoaround30ms,furtherenhancingglobal
|     |     |     |     |     |     |     |     | connectivity | [108]. | Holographic |     | media | and full-sensory |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | --- | ----- | ---------------- | --- |
performance[2].
Innovative 3D cloud/edge computing models should be immersive experiences are expected to unlock new market
opportunities[108].
| investigated | for | applications | such | as  | Video | Game | as a 3D |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ---- | --- | ----- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
Service (VGaa3DS) and Video Streaming as a 3D Service Emergingtechnologiessuchasfederatednetworks,dense
(VSaa3DS) [2]. Research should also focus on optimizing edge deployments, and 3D networking will be crucial in
|         |          |            |     |          |             |     |       | meeting | the demands | of  | future | multimedia | services | [108]. |
| ------- | -------- | ---------- | --- | -------- | ----------- | --- | ----- | ------- | ----------- | --- | ------ | ---------- | -------- | ------ |
| network | resource | allocation | to  | meet the | performance |     | needs |         |             |     |        |            |          |        |
of 3D multimedia services over 6G. Additionally, open As shown in Fig. 19, innovations in 6G will impact
|     |     |     |     |     |     |     |     | various | verticals—education, |     |     | healthcare, | manufacturing, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------------- | --- | --- | ----------- | -------------- | --- |
interfacesmustbedevelopedtoallowverticalindustriesand
thirdpartiestomanage6Ginfrastructure.Relevantinitiatives entertainment—spurring the development of new industries
include SPACEPORT and VRTogether, with SPACEPORT likeholoportation,digitalavatars,andautonomousfactories.
|          |          |       |        |               |     |     |         | These services | will | require | precise, | high-performance |     | fea- |
| -------- | -------- | ----- | ------ | ------------- | --- | --- | ------- | -------------- | ---- | ------- | -------- | ---------------- | --- | ---- |
| offering | a unique | media | server | for capturing |     | and | stream- |                |      |         |          |                  |     |      |
ing 3D volumetric video, enabling immersive experiences tures including real-time holography and haptic feedback.
beyondtraditionalVR. The scalability of 6G will be critical to support immersive
Network slicing in 6G offers the flexibility to allocate media and an expanding array of devices, each demanding
dedicated resources for 3D streaming, ensuring the high ultra-highdataratesandminimallatency[183].
| bandwidth | and | ultra-low | latency | required |     | for immersive |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | ------- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
applications [173]. It also enables scalability, supporting a E. SUMMARYANDLESSONLEARNED
growing number of users, devices, and use cases across Table14providesasummaryofchallenges,opportunitiesand
diverseenvironments—urban,remote,ormobile.As6Gnet- researchdirectionsofmultimediastreamingtowards6Gnet-
works evolve, slicing will be pivotal in delivering seamless, works.Theevolutionof6GandNetwork2030presentstrans-
high-quality3Dcontent[181]. formativeopportunities,suchasholographiccommunication,
To support this, future 3D networking architectures must tactileinteractions,anddigitalteleportation,revolutionizing
enable flexible formation of virtual network functions sectors like education [184], healthcare [185], and man-
(VNFs) and services tailored to specific requirements. ufacturing. However, these advancements face significant
AI/ML-drivennetworkintelligencewillfacilitateon-demand challenges, including achieving ultra-reliable, low-latency
composition of modular VFs, allowing full service cus- communication, zero packet loss, and scalability for dense
tomization. A SDN/NFV-based orchestration system is devicenetworks.Lessonslearnedemphasizetheimportance
essential to manage VNFs, build slices, and interface of advanced resource allocation, robust infrastructure, and
with external entities equipped with adequate communica- collaborative efforts to meet the unique requirements of
tion, computing, and caching (3C) resources. Open-source multimedia streaming and vertical market integration in the
platformslikeOSM,ONAP,Akraino,Acumos,andO-RAN eraof6Gandbeyond.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 157435 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
VI. CONCLUSION [9] S. Petrangeli, J. V. D. Hooft, T. Wauters, and F. D. Turck, ‘‘Quality
We provide state-of-the-art solutions for QoE-driven adap- ofexperience-centricmanagementofadaptivevideostreamingservices:
|            |           |     |          |       |     |       |             | Status | and challenges,’’ |     | ACM Trans. | Multimedia | Comput., | Commun., |
| ---------- | --------- | --- | -------- | ----- | --- | ----- | ----------- | ------ | ----------------- | --- | ---------- | ---------- | -------- | -------- |
| tive video | streaming |     | services | based | on  | three | classifica- |        |                   |     |            |            |          |          |
Appl.,vol.14,pp.2–28,May2018.
| tions: client-based, |               | server-based, |     | and     | the in-network-based |       |         |                 |             |             |     |             |                |                |
| -------------------- | ------------- | ------------- | --- | ------- | -------------------- | ----- | ------- | --------------- | ----------- | ----------- | --- | ----------- | -------------- | -------------- |
|                      |               |               |     |         |                      |       |         | [10] S. Aroussi | and         | A. Mellouk, |     | ‘‘Survey on | machine        | learning-based |
|                      |               |               |     |         |                      |       |         | QoE-QoS         | correlation | models,’’   | in  | Proc. Int.  | Conf. Comput., | Manage.        |
| approaches.          | Additionally, |               | we  | present | the                  | video | stream- |                 |             |             |     |             |                |                |
Telecommun.(ComManTel),Apr.2014,pp.200–204.
| ing QoE | in softwarized |     | 5G  | networks | using | SDN/NFV, |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | -------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[11] C.-J.Huang,H.-W.Cheng,Y.-H.Lien,andM.-E.Jian,‘‘Asurveyon
| cloud/edge | computing, |     | ML and | AI  | techniques. | In  | addition, |       |           |                     |     |           |             |              |
| ---------- | ---------- | --- | ------ | --- | ----------- | --- | --------- | ----- | --------- | ------------------- | --- | --------- | ----------- | ------------ |
|            |            |     |        |     |             |     |           | video | streaming | for next-generation |     | vehicular | networks,’’ | Electronics, |
vol.13,no.3,p.649,Feb.2024.
| this work | provides | emerging |     | trends | and | technologies | for |            |              |     |           |        |        |                |
| --------- | -------- | -------- | --- | ------ | --- | ------------ | --- | ---------- | ------------ | --- | --------- | ------ | ------ | -------------- |
|           |          |          |     |        |     |              |     | [12] A. A. | Barakabitze, | M.  | Liyanage, | and A. | Hines, | ‘‘QoESoft: QoE |
multimedia6Gnetworks,includingmetaverseformulti-user
managementarchitectureforsoftwarized5Gnetworks,’’inProc.IEEE
XR,QoE-drivenvideostreamingin6G-drivenholographic Int.Conf.Commun.Workshops,Jun.2020,pp.1–6.
[13] A.Bentaleb,B.Taani,A.C.Begen,C.Timmerer,andR.Zimmermann,
telepresence,personalizedmediaandIoS,newvideocoding
|           |     |                         |     |     |      |            |     | ‘‘A survey | on   | bitrate adaptation |         | schemes for | streaming | media over     |
| --------- | --- | ----------------------- | --- | --- | ---- | ---------- | --- | ---------- | ---- | ------------------ | ------- | ----------- | --------- | -------------- |
| standards | and | 6G initiatives/projects |     |     | that | are paving | the |            |      |                    |         |             |           |                |
|           |     |                         |     |     |      |            |     | HTTP,’’    | IEEE | Commun.            | Surveys | Tuts., vol. | 21, no.   | 1, pp.562–585, |
way to improve the QoE of the end user in future 1stQuart.,2019.
networks. Moreover, we present concrete challenges and [14] M. Torres Vega, C. Perra, F. De Turck, and A. Liotta, ‘‘A review
|     |     |     |     |     |     |     |     | of predictive | quality | of  | experience | management | in  | video streaming |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | ---------- | ---------- | --- | --------------- |
future research directions in regard to 6G networks such services,’’IEEETrans.Broadcast.,vol.64,no.2,pp.432–445,Jun.2018.
as (a) new video compression standards and 3D streaming [15] M. Sanaei and S. Mostafavi, ‘‘Multimedia delivery techniques over
cloud/edgemultimediastreaming.Finally,thepaperprovide software-definednetworks:Asurvey,’’inProc.5thInt.Conf.WebRes.
(ICWR),Apr.2019,pp.105–110.
highlights on multimedia streaming in new verticals and [16] C. T. E. R. Hewage, A. Ahmad, T. Mallikarachchi, N. Barman,
next-generation mobile technologies putting an emphasis andM.G.Martini,‘‘Measuring,modelingandintegratingtime-varying
on 6G and beyond factories, education, social and enter- video quality in end-to-end multimedia service delivery: A review
|           |            |     |                 |     |      |       |           | and open | challenges,’’ |     | IEEE | Access, vol. | 10, | pp.60267–60293, |
| --------- | ---------- | --- | --------------- | --- | ---- | ----- | --------- | -------- | ------------- | --- | ---- | ------------ | --- | --------------- |
| tainment, | automotive |     | and healthcare. |     | This | paper | will be a | 2022.    |               |     |      |              |     |                 |
vehicleforthemultimediaandnetworksresearchcommunity [17] M.M.Nasralla,S.B.A.Khattak,I.UrRehman,andM.Iqbal,‘‘Exploring
theroleof6Gtechnologyinenhancingqualityofexperienceform-health
| from academia |     | and industry |     | towards | implementing |     | novel |            |               |     |                 |     |           |                   |
| ------------- | --- | ------------ | --- | ------- | ------------ | --- | ----- | ---------- | ------------- | --- | --------------- | --- | --------- | ----------------- |
|               |     |              |     |         |              |     |       | multimedia | applications: |     | A comprehensive |     | survey,’’ | Sensors, vol. 23, |
approaches regarding QoE monitoring, management, and no.13,p.5882,Jun.2023.
performanceoptimizationinfuture6Gnetworks. [18] R.Farahani,A.Bentaleb,E.Etinkaya,C.Timmerer,R.Zimmermann,and
H.Hellwagner,‘‘Hybridp2p-cdnarchitectureforlivevideostreaming:
Anonlinelearningapproach,’’inProc.IEEEGlobalCommun.Conf.,
| ACKNOWLEDGMENT |     |              |          |          |           |             |           | Mar.2022,pp.1911–1917. |               |              |           |               |            |                |
| -------------- | --- | ------------ | -------- | -------- | --------- | ----------- | --------- | ---------------------- | ------------- | ------------ | --------- | ------------- | ---------- | -------------- |
|                |     |              |          |          |           |             |           | [19] M. S.             | Anwar,        | A. Choi,     | S. Ahmad, | K. Aurangzeb, |            | A. A. Laghari, |
| The authors    | are | very         | grateful | to the   | Reviewers |             | for their |                        |               |              |           |               |            |                |
|                |     |              |          |          |           |             |           | T.R.Gadekallu,         |               | and A.       | Hines,    | ‘‘A moving    | metaverse: | QoE chal-      |
| appropriate    | and | constructive |          | comments | and       | suggestions | to        |                        |               |              |           |               |            |                |
|                |     |              |          |          |           |             |           | lenges                 | and standards | requirements |           | for immersive | media      | consumption    |
improvethiswork.
|     |     |     |     |     |     |     |     | in autonomous |     | vehicles,’’ | Appl. | Soft Comput., | vol. | 159, Jul. 2024, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ----- | ------------- | ---- | --------------- |
Art.no.111577.
[20] C.Liu,I.Bouazizi,andM.Gabbouj,‘‘RateadaptationforadaptiveHTTP
REFERENCES
streaming,’’inProc.2ndAnnu.ACMConf.MultimediaSyst.,Feb.2011,
| [1] A.BarakabitzeandA.Hines,‘‘MultimediaQoE-drivenservicesdelivery |     |     |     |     |     |     |     | pp.169–174.    |           |     |           |             |           |             |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | --------- | ----------- | --------- | ----------- |
|                                                                    |     |     |     |     |     |     |     | [21] J. Jiang, | V. Sekar, | and | H. Zhang, | ‘‘Improving | fairness, | efficiency, |
toward6Gandbeyondnetwork,’’inMultimediaStreaminginSDN/NFV
and5GNetworks:MachineLearningforManagingBigDataStreaming. and stability in HTTP-based adaptive video streaming with
USA:IEEE,2023,pp.185–201,doi:10.1002/9781119800828.ch11. festive,’’ IEEE/ACM Trans. Netw., vol. 22, no. 1, pp.326–340,
| [2] A. A. | Barakabitze | and | R. Walshe, | ‘‘SDN | and | NFV for | QoE-driven | Feb.2014. |     |     |     |     |     |     |
| --------- | ----------- | --- | ---------- | ----- | --- | ------- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
[22] S.Akhshabi,A.C.Begen,andC.Dovrolis,‘‘Anexperimentalevaluation
| multimedia |     | services | delivery: | The road | towards | 6G  | and beyond |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --------- | -------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
networks,’’Comput.Netw.,vol.214,Sep.2022,Art.no.109133. of rate-adaptation algorithms in adaptive streaming over HTTP,’’
[3] A. A. Barakabitze, N. Barman, A. Ahmad, S. Zadtootaghaj, L. Sun, Methodology,vol.27,no.4,pp.271–287,Apr.2012.
M. G. Martini, and L. Atzori, ‘‘QoE management of multimedia [23] Y.Sun,X.Yin,J.Jiang,V.Sekar,F.Lin,N.Wang,T.Liu,andB.Sinopoli,
streaming services in future networks: A tutorial and survey,’’ IEEE ‘‘CS2P:Improvingvideobitrateselectionandadaptationwithdata-driven
|     |     |     |     |     |     |     |     | throughput | prediction,’’ |     | in Proc. | ACM SIGCOMM | Conf., | Aug. 2016, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | -------- | ----------- | ------ | ---------- |
Commun.SurveysTuts.,vol.22,no.1,pp.526–565,1stQuart.,2020.
| [4] C. Ge, | N. Wang, | G.  | Foster, | and M. Wilson, | ‘‘Toward |     | QoE-assured | pp.272–285. |     |     |     |     |     |     |
| ---------- | -------- | --- | ------- | -------------- | -------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- |
4Kvideo-on-demanddeliverythroughmobileedgevirtualizationwith [24] A.Bentaleb,C.Timmerer,A.C.Begen,andR.Zimmermann,‘‘Band-
adaptive prefetching,’’ IEEE Trans. Multimedia, vol. 19, no. 10, widthpredictioninlow-latencychunkedstreaming,’’inProc.29thACM
WorkshopNetw.OperatingSyst.SupportDigit.AudioVideo,Jun.2019,
pp.2222–2237,Oct.2017.
| [5] A.A.Barakabitze,A.Ahmad,R.Mijumbi,andA.Hines,‘‘5Gnetwork |     |     |     |     |     |     |     | pp.7–13. |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
slicingusingSDNandNFV:Asurveyoftaxonomy,architecturesand [25] K. Miller, A.-K. Al-Tamimi, and A. Wolisz, ‘‘QoE-based low-delay
futurechallenges,’’Comput.Netw.,vol.167,pp.1–40,Feb.2020. livestreamingusingthroughputpredictions,’’ACMTrans.Multimedia
[6] R.R.R.Rao,S.Göring,P.List,W.Robitza,B.Feiten,U.Wüstenhagen, Comput.,Commun.,Appl.,vol.13,no.1,pp.1–24,Feb.2017.
|     |           |                   |     |       |          |             |      | [26] S. Akhshabi, | L.  | Anantakrishnan, |     | A. C. | Begen, and | C. Dovrolis, |
| --- | --------- | ----------------- | --- | ----- | -------- | ----------- | ---- | ----------------- | --- | --------------- | --- | ----- | ---------- | ------------ |
| and | A. Raake, | ‘‘Bitstream-based |     | model | standard | for 4K/UHD: | ITU- |                   |     |                 |     |       |            |              |
T P.1204.3—Model details, evaluation, analysis and open source ‘‘What happens when HTTP adaptive streaming players compete for
implementation,’’ in Proc. 12th Int. Conf. Quality Multimedia Exper., bandwidth?’’inProc.22ndInt.workshopNetw.OperatingSyst.Support
| May2020,pp.1–6. |     |     |     |     |     |     |     | Digit.AudioVideo,Jun.2012,pp.9–14. |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
[27] Y.Yuan,S.Lin,andG.Zhou,‘‘QoEcontrolfordynamicadaptivevideo
[7] A.Raake,S.Borer,S.M.Satti,J.Gustafsson,R.R.R.Rao,S.Medagli,
P. List, S. Goring, D. Lindero, W. Robitza, G. Heikkila, S. Broom, streaming over HTTP at access point,’’ in Proc. IEEE Int. Conf. Ind.
C.Schmidmer,B.Feiten,U.Wustenhagen,T.Wittmann,M.Obermann, Internet(ICII),Nov.2019,pp.268–277.
and R. Bitto, ‘‘Multi-model standard for Bitstream-, pixel-based and [28] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,andM.A.Watson,
|        |       |         |            |            |       |           |      | ‘‘Using | the buffer | to avoid | rebuffers: | Evidence | from | a large video |
| ------ | ----- | ------- | ---------- | ---------- | ----- | --------- | ---- | ------- | ---------- | -------- | ---------- | -------- | ---- | ------------- |
| hybrid | video | quality | assessment | of UHD/4K: | ITU-T | P.1204,’’ | IEEE |         |            |          |            |          |      |               |
streamingservice,’’inProc.ACMConf.SIGCOMM,2014,pp.187–198.
Access,vol.8,pp.1–27,2020.
[8] N. Barman and M. G. Martini, ‘‘QoE modeling for HTTP adaptive [29] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman,‘‘BOLA:Near-optimal
videostreaming—Asurveyandopenchallenges,’’IEEEAccess,vol.7, bitrateadaptationforonlinevideos,’’inProc.35thAnnu.IEEEInt.Conf.
| pp.30831–30859,2019. |     |     |     |     |     |     |     | Comput.Commun.,Apr.2016,pp.1–9. |     |     |     |     |     |               |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- |
| 157436               |     |     |     |     |     |     |     |                                 |     |     |     |     |     | VOLUME13,2025 |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
[30] A. Beben, P. Wiśniewski, J. M. Batalla, and P. Krawiec, ‘‘ABMA+: [51] E.Liotou,K.Samdanis,E.Pateromichelakis,N.Passas,andL.Merakos,
Lightweight and efficient algorithm for http adaptive streaming,’’ ‘‘QoE-SDN APP: A rate-guided QoE-aware SDN-APP for HTTP
in Proc. 7th Int. Conf. Multimedia Syst., no. 2. Association for adaptivevideostreaming,’’IEEEJ.Sel.AreasCommun.,vol.36,no.3,
Computing Machinery, May 2016, pp. 1–11. [Online]. Available: pp.598–615,Mar.2018.
https://doi.org/10.1145/2910017.2910596 [52] J.Samain,G.Carofiglio,M.Tortelli,andD.Rossi,‘‘Asimpleyeteffective
[31] P.K.Yadav,A.Shafiei,andW.T.Ooi,‘‘QUETRA:Aqueuingtheory network-assisted signal for enhanced dash quality of experience,’’ in
approach to DASH rate adaptation,’’ in Proc. 25th ACM Int. Conf. Proc.28thACMSIGMMWorkshopNetw.OperatingSyst.SupportDigital
Multimedia,Oct.2017,pp.1130–1138. AudioVideo,2018,pp.55–60.
[32] J.Liu,Z.Liu,J.Huang,W.Jiang,andJ.Wang,‘‘Abuffer-basedadaptive [53] L. Guillen, S. Izumi, T. Abe, and T. Suganuma, ‘‘SAND/3: SDN-
bitrateapproachinwirelessnetworkswithiterativecorrection,’’IEEE assistednovelQoEcontrolmethodfordynamicadaptivestreamingover
WirelessCommun.Lett.,vol.11,no.8,pp.1644–1648,Aug.2022. HTTP/3,’’Electronics,vol.8,no.8,p.864,Aug.2019.
[33] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,‘‘Stick: [54] (Dec. 2018). Guidelines for Implementation: DASH-IF SAND Inter-
Aharmoniousfusionofbuffer-basedandlearning-basedapproachfor operability.Accessed:22-.[Online].Available:https://dashif.org/docs/
adaptivestreaming,’’inProc.IEEEConf.Comput.Commun.,Jul.2020, DASH-IF-SAND-IOP-v1.0.pdf//
pp.1967–1976. [55] M. Mrad, U. S. Suryahatmaja, A. O. Elsayed, H. Fathallah, and
[34] I. M. Ozcelik and C. Ersoy, ‘‘Chunk duration-aware SDN-assisted A.Gharbi,‘‘Heuristicsolutionstooptimizethetrafficroutinginspace
DASH,’’ ACM Trans. Multimedia Comput., Commun., Appl., vol. 15, divisionmultiplexingnetworks,’’J.Eng.Res.,vol.2024,pp.2307–1877,
no.3,pp.1–22,Aug.2019. May2024.
[35] S. Petrangeli, N. Bouten, E. Dejonghe, J. Famaey, P. Leroux, and [56] A.A.Barakabitze,L.Sun,I.-H.Mkwawa,andE.Ifeachor,‘‘AnovelQoE-
F.DeTurck,‘‘DesignandevaluationofaDASH-compliantsecondscreen centricSDN-basedmultipathroutingapproachformultimediaservices
videoplayerforliveeventsinmobilescenarios,’’inProc.IFIP/IEEE over5Gnetworks,’’inProc.IEEEInt.Conf.Commun.(ICC),May2018,
Int.Symp.Integr.Netw.Manage.(IM),Ottawa,ON,Canada,May2015, pp.1–7.
pp.894–897. [57] A.A.Barakabitze,L.Sun,I.-H.Mkwawa,andE.Ifeachor,‘‘Multipath
[36] Y. Li, X. Zhang, S. Wang, and S. Ma, ‘‘A fuzzy-based adaptation protectionsanddynamiclinkrecoveryinsoftwarized5Gnetworksusing
controllerforlowlatencylivevideostreaming,’’inProc.IEEEInt.Conf. segmentrouting,’’inProc.IEEEGlobecomWorkshops(GCWkshps),
ImageProcess.(ICIP),Sep.2021,pp.2169–2173. Dec.2019,pp.1–6.
[37] Z.Li,X.Zhu,J.Gahm,R.Pan,H.Hu,A.C.Begen,andD.Oran,‘‘Probe [58] A.A.Pranata,T.S.Jun,andD.S.Kim,‘‘Overheadreductionschemefor
andadapt:RateadaptationforHTTPvideostreamingatscale,’’IEEEJ. SDN-baseddatacenternetworks,’’Comput.StandardsInterfaces,vol.63,
Sel.AreasCommun.,vol.32,no.4,pp.719–733,Apr.2014. pp.1–15,Mar.2019.
[38] P. Juluri, V. Tamarapalli, and D. Medhi, ‘‘SARA: Segment aware [59] H.E.Egilmez,S.T.Dane,K.T.Bagci,andA.M.Tekalp,‘‘OpenQoS:
rateadaptationalgorithmfordynamicadaptivestreamingoverHTTP,’’ AnOpenFlowcontrollerdesignformultimediadeliverywithend-to-end
in Proc. IEEE Int. Conf. Commun. Workshop (ICCW), Jun. 2015, quality of service over software-defined networks,’’ in Proc. Asia–
pp.1765–1770. Pacific Signal Inf. Process. Assoc. Annu. Summit Conf., Dec. 2012,
[39] A.Bentaleb,A.C.Begen,S.Harous,andR.Zimmermann,‘‘Wanttoplay pp.1–8.
DASH?’’inProc.9thACMMultimediaSyst.Conf.,Jun.2018,pp.13–26. [60] C.Cetinkaya,E.Karayer,M.Sayit,andC.Hellge,‘‘SDNforsegment
[40] I. M. Ibrahim, S. R. M. Zeebaree, H. M. Yasin, M. A. M. Sadeeq, basedflowroutingofDASH,’’inProc.IEEE4thInt.Conf.Consum.
H.M.Shukur, and A. Alkhayyat, ‘‘Hybrid client/server peer to peer Electron.Berlin(ICCE-Berlin),Sep.2014,pp.74–77.
multitiervideostreaming,’’inProc.Int.Conf.Adv.Comput.Appl.(ACA), [61] O. Dobrijevic, M. Santl, and M. Matijasevic, ‘‘Ant colony optimiza-
Jul.2021,pp.84–89. tion for QoE-centric flow routing in software-defined networks,’’ in
[41] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, ‘‘A control-theoretic Proc. 11th Int. Conf. Netw. Service Manage. (CNSM), Nov. 2015,
approach for dynamic adaptive video streaming over HTTP,’’ ACM pp.274–278.
SIGCOMM Comput. Commun. Rev., vol. 45, no. 4, pp.325–338, [62] N. Bouten, M. Claeys, B. Van Poecke, S. Latré, and F. De Turck,
Sep.2015. ‘‘Dynamic server selection strategy for multi-server HTTP adaptive
[42] M. Banafaa, I. Shayea, J. Din, M. Hadri Azmi, A. Alashbi, Y. streaming services,’’ in Proc. 12th Int. Conf. Netw. Service Manage.
Ibrahim Daradkeh, and A. Alhammadi, ‘‘6G mobile communication (CNSM),Oct.2016,pp.82–90.
technology:Requirements,targets,applications,challenges,advantages, [63] A.Al-Jawad,P.Shah,O.Gemikonakli,andR.Trestian,‘‘LearnQoS:A
andopportunities,’’AlexandriaEng.J.,vol.64,pp.245–274,Feb.2023. learningapproachforoptimizingQoSovermultimedia-basedSDNs,’’in
[43] Y.Qin,S.Hao,K.R.Pattipati,F.Qian,S.Sen,B.Wang,andC.Yue, Proc.IEEEInt.Symp.BroadbandMultimediaSyst.Broadcast.(BMSB),
‘‘ABRstreamingofVBR-encodedvideos:Characterization,challenges, Jun.2018,pp.1–6.
andsolutions,’’inProc.14thInt.Conf.Emerg.Netw.Exp.Technol.,2018, [64] G.Calvigioni,R.Aparicio-Pardo,L.Sassatelli,J.Leguay,P.Medagliani,
pp.366–378. andS.Paris,‘‘Qualityofexperience-basedroutingofvideotrafficfor
[44] Z.Akhtar,Y.S.Nam,R.Govindan,S.Rao,J.Chen,E.Katz-Bassett, overlay and ISP networks,’’ in Proc. IEEE Conf. Comput. Commun.,
B.Ribeiro,J.Zhan,andH.Zhang,‘‘Oboe,’’inProc.Conf.ACMSpecial Apr.2018,pp.935–943.
InterestGroupDataCommun.,2018,pp.44–58. [65] X.Huang,T.Yuan,G.Qiao,andY.Ren,‘‘Deepreinforcementlearning
[45] J.Li,C.Zhang,Z.Liu,R.Hong,andH.Hu,‘‘Optimalvolumetricvideo for multimedia traffic control in software defined networking,’’ IEEE
streamingwithhybridsaliencybasedtiling,’’IEEETrans.Multimedia, Netw.,vol.32,no.6,pp.35–41,Nov.2018.
vol.25,pp.2939–2953,2023. [66] A. Khalid, A. H. Zahran, and C. J. Sreenan, ‘‘An SDN-based
[46] Information Technology—Dynamic Adaptive Streaming Over HTTP device-aware live video service for inter-domain adaptive bitrate
(DASH)—Part5:ServerandNetworkAssistedDASH(SAND).Standard. streaming,’’ in Proc. 10th ACM Multimedia Syst. Conf., Jun. 2019,
International Organization for Standardization., Standard ISO/IEC pp.121–132.
23009-5:2017.,2017. [67] M. Sayit, C. Cetinkaya, H. U. Yildiz, and B. Tavli, ‘‘DASH-
[47] J.W.Kleinrouweler,S.Cabrero,andP.Cesar,‘‘Deliveringstablehigh- QoS: A scalable network layer service differentiation architecture
quality video: An SDN architecture with DASH assisting network for DASH over SDN,’’ Comput. Netw., vol. 154, pp.12–25,
elements,’’ in Proc. 7th Int. Conf. Multimedia Syst., May 2016, May2019.
pp.1–10. [68] H.M.SuandA.H.Maw,‘‘Effectivetrafficreroutingforvideostreaming
[48] G.Cofano,L.D.Cicco,T.Zinner,A.Nguyen-Ngoc,P.Tran-Gia,and insoftwaredefinednetworking,’’inProc.IEEEConf.Comput.Appl.,
S. Mascolo, ‘‘Design and performance evaluation of network-assisted Feb.2023,pp.423–428.
controlstrategiesforHTTPadaptivestreaming,’’ACMTrans.Multimedia [69] P. Georgopoulos, Y. Elkhatib, M. Broadbent, M. Mu, and N. Race,
Comput.,Commun.,Appl.,vol.13,no.3s,pp.1–24,Aug.2017. ‘‘Towardsnetwork-wideQoEfairnessusingopenflow-assistedadaptive
[49] A.Bentaleb,A.C.Begen,andR.Zimmermann,‘‘SDNDASH:Improving videostreaming,’’inProc.ACMSIGCOMMWorkshopFutureHuman-
QoEofHTTPadaptivestreamingusingsoftwaredefinednetworking,’’in CentricMultimediaNetw.,Aug.2013,pp.15–20.
Proc.24thACMInt.Conf.Multimedia,Oct.2016,pp.1296–1305. [70] S. Petrangeli, T. Wu, T. Wauters, R. Huysegems, T. Bostoen, and
[50] D.Bhat,A.Rizk,M.Zink,andR.Steinmetz,‘‘Networkassistedcontent F.DeTurck,‘‘Amachinelearning-basedframeworkforpreventingvideo
distribution for adaptive bitrate video streaming,’’ in Proc. 8th ACM freezesinHTTPadaptivestreaming,’’J.Netw.Comput.Appl.,vol.94,
MultimediaSyst.Conf.,Jun.2017,pp.62–75. pp.78–92,Sep.2017.
VOLUME13,2025 157437

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
[71] M. R. Kanagarathinam, K. M. Sivalingam, and G. K. Choudhary, [90] A. Barakabitze and A. Hines, ‘‘QoE management of multimedia
‘‘Applicationprioritizationengineforenhancingreal-timeperformance services using machine learning in SDN/NFV 5G networks,’’ in
in smartphones,’’ IEEE Trans. Netw. Service Manage., vol. 21, no. 1, MultimediaStreaminginSDN/NFVand5GNetworks:MachineLearn-
pp.773–788,Feb.2024. ing for Managing Big Data Streaming. IEEE, 2023, pp.73–97, doi:
[72] I.Bridova,P.Brida,J.Papan,andO.Krejcar,‘‘Newadvancedapproach 10.1002/9781119800828.ch5.
fordataflowsprioritizationatanoutputofauserterminal,’’IEEEAccess, [91] A.Ahmad,A.B.Mansoor,A.A.Barakabitze,A.Hines,L.Atzori,andR.
vol.10,pp.60887–60903,2022. Walshe,‘‘Supervised-learning-basedQoEpredictionofvideostreaming
[73] A. A. Barakabitze, I.-H. Mkwawa, L. Sun, and E. Ifeachor, ‘‘Quali- infuturenetworks:Atutorialwithcomparativestudy,’’IEEECommun.
tySDN:ImprovingvideoqualityusingMPTCPandsegmentroutingin Mag.,vol.59,no.11,pp.88–94,Nov.2021.
SDN/NFV,’’inProc.4thIEEEConf.Netw.SoftwarizationWorkshops [92] A.A.Barakabitze,T.Xiaoheng,andG.Tan,‘‘Asurveyonnaming,name
(NetSoft),Jun.2018,pp.182–186. resolutionanddataroutingininformationcentricnetworking(ICN),’’
[74] J. Wu, C. Yuen, B. Cheng, M. Wang, and J. Chen, ‘‘Streaming high- Int.J.Adv.Res.Comput.Commun.Eng.,vol.3,no.10,pp.8322–8327,
quality mobile video with multipath TCP in heterogeneous wireless Oct.2014.
networks,’’IEEETrans.MobileComput.,vol.15,no.9,pp.2345–2361, [93] A.BarakabitzeandA.Hines,‘‘Networksoftwarizationandvirtualization
Sep.2016. in future networks: The promise of SDN, NFV, MEC, and fog/cloud
[75] C.James,E.Halepovic,M.Wang,R.Jana,andN.K.Shankaranarayanan, computing,’’inMultimediaStreaminginSDN/NFVand5GNetworks:
‘‘Is multipath TCP (MPTCP) beneficial for video streaming over Machine Learning for Managing Big Data Streaming. IEEE, 2023,
DASH?’’inProc.IEEE24thInt.Symp.Model.,Anal.Simul.Comput. pp.99–118,doi:10.1002/9781119800828.ch6.
Telecommun.Syst.(MASCOTS),Sep.2016,pp.331–336. [94] A.BarakabitzeandA.Hines,‘‘Managementofmultimediaservicesin
[76] N.Mohan,T.Shreedhar,A.Zavodovski,J.Kangasharju,andS.K.Kaul, emergingarchitecturesusingbigdataanalytics:MEC,ICN,andfog/cloud
‘‘Istwogreaterthanone?:AnalyzingmultipathTCPoverdual-LTEinthe computing,’’inMultimediaStreaminginSDN/NFVand5GNetworks:
wild,’’2019,arXiv:1909.02601. Machine Learning for Managing Big Data Streaming. IEEE, 2023,
[77] Y. Cao, R. Ji, L. Ji, G. Lei, H. Wang, and X. Shao, ‘‘l2-MPTCP: A pp.119–132,doi:10.1002/9781119800828.ch7.
learning-drivenlatency-awaremultipathtransportschemeforindustrial [95] C. Zhou, C.-W. Lin, and Z. Guo, ‘‘MDASH: A Markov
internetapplications,’’IEEETrans.IndustrialInformat.,vol.18,no.12, decision-based rate adaptation approach for dynamic HTTP
pp.8456–8466,Dec.2022. streaming,’’ IEEE Trans. Multimedia, vol. 18, no. 4, pp.738–751,
[78] A.A.Barakabitze,I.-H.Mkwawa,A.Hines,L.Sun,andE.Ifeachor, Apr.2016.
‘‘QoEMultiSDN:ManagementofmultimediaservicesusingMPTCP/SR [96] F.Chiariotti,S.D’Aronco,L.Toni,andP.Frossard,‘‘Onlinelearning
in softwarized and virtualized networks,’’ IEEE Access, pp.1–10, adaptationstrategyforDASHclients,’’inProc.7thInt.Conf.Multimedia
2020. Syst.,May2016,pp.1–12.
[79] A. T. Da Silva, R. P. S. Clerici, F. E. R. Cesen, M. T. Islam, [97] H.Mao,R.Netravali,andM.Alizadeh,‘‘Neuraladaptivevideostreaming
and C.E.Rothenberg, ‘‘Programmable network testbed for QoS/QoE with pensieve,’’ in Proc. Conf. ACM Special Interest Group Data
assessmentofholographicmediadelivery,’’inProc.IEEEConf.Netw. Commun.,Aug.2017,pp.197–210.
Function Virtualization Softw. Defined Netw. (NFV-SDN), Nov. 2024, [98] M. Gadaleta, F. Chiariotti, M. Rossi, and A. Zanella, ‘‘D-DASH:
pp.1–2. A deep Q-learning framework for DASH video streaming,’’
[80] F.S.DantasSilva,E.Neto,C.Santos,T.Almeida,I.Silva,andA.V.Neto, IEEE Trans. Cognit. Commun. Netw., vol. 3, no. 4, pp.703–718,
‘‘Evolvingfastinnovationinnext-generationnetworkingthroughflexible Dec.2017.
andcustomizedsoftwarizationandslicingcapabilities,’’inProc.IEEE [99] A. Sobhani, A. Yassine, and S. Shirmohammadi, ‘‘A fuzzy-based
Conf.Netw.FunctionVirtualizationSoftw.DefinedNetw.(NFV-SDN), rate adaptation controller for DASH,’’ in Proc. 25th ACM Work-
Nov.2020,pp.188–193. shop Netw. Operating Syst. Support Digit. Audio Video, Mar. 2015,
[81] F. S. D. Silva et al., ‘‘Proactive ML-assisted and quality-driven slice pp.31–36.
applicationservicemanagementtokeepQoEin5Gmobilenetworks,’’ [100] J.vanderHooft,S.Petrangeli,M.Claeys,J.Famaey,andF.DeTurck,‘‘A
inProc.IEEEConf.Netw.FunctionVirtualizationSoftw.DefinedNetw. learning-basedalgorithmforimprovedbandwidth-awarenessofadaptive
(NFV-SDN),Nov.2023,pp.182–184. streamingclients,’’inProc.IFIP/IEEEInt.Symp.Integr.Netw.Manage.
[82] M.T.IslamandC.E.Rothenberg,‘‘QoEevaluationforemergingmedia (IM),May2015,pp.131–138.
applications:Network-levelanalysisandtrafficmodeling,’’inProc.IEEE [101] C.Sieber,K.Hagn,C.Moldovan,T.Hoßfeld,andW.Kellerer,‘‘Towards
Conf.Netw.FunctionVirtualizationSoftw.DefinedNetw.(NFV-SDN), machinelearning-basedoptimalHAS,’’2018,arXiv:1808.08065.
Nov.2024,pp.217–220. [102] T.Huang,X.Yao,C.Wu,R.-X.Zhang,Z.Pang,andL.Sun,‘‘Tiyuntsong:
[83] D. Li, Z. Wang, R. Zhao, H. Zhang, Z. Yin, N. Cheng, and J. Liu, Aself-playreinforcementlearningapproachforABRvideostreaming,’’
‘‘Dynamic SFC deployment for SDN/NFV-based satellite-terrestrial 2018,arXiv:1811.06166.
integratedvehicularnetworks,’’IEEETrans.Veh.Technol.,earlyaccess, [103] F.Y.Yan,H.Ayers,C.Zhu,S.Fouladi,J.Hong,K.Zhang,P.Levis,
Jul.7,2025,doi:10.1109/TVT.2025.3586653. andK.Winstein,‘‘Learninginsitu:Arandomizedexperimentinvideo
[84] F. E. Subhan, A. Yaqoob, C. H. Muntean, and G.-M. Muntean, streaming,’’2019,arXiv:1906.01113.
‘‘A survey on artificial intelligence techniques for improved rich [104] B. Biggio, I. Corona, D. Maiorca, B. Nelson, N. Šrndić, P. Laskov,
media content delivery in a 5G and beyond network slicing con- G.Giacinto,andF.Roli,‘‘Evasionattacksagainstmachinelearningat
text,’’ IEEE Commun. Surveys Tuts., vol. 27, no. 2, pp.1427–1487, test time,’’ in Proc. Joint Eur. Conf. Mach. Learn. Knowl. Discovery
Apr.2025. Databases.USA:IEEE,2013,pp.387–402.
[85] J.Nightingale,P.Salva-Garcia,J.M.A.Calero,andQ.Wang,‘‘5G-QoE: [105] N.B.Truong,K.Sun,G.Wang,andF.Guitton,‘‘Ai-basednetworkthreat
QoE modelling for ultra-HD video streaming in 5G networks,’’IEEE detectioninSDN/NFV:Asurvey,’’IEEECommun.SurveysTuts.,vol.21,
Trans.Broadcast.,vol.64,no.2,pp.621–634,Jun.2018. no.4,pp.3681–3715,Apr.2019.
[86] Z. Fei, F. Wang, J. Wang, and X. Xie, ‘‘QoE evaluation methods for [106] A.Mukherjee,Q.Wu,J.Shao,andY.T.Hou,‘‘Securityandprivacyinai-
360-degreeVRvideotransmission,’’IEEEJ.Sel.TopicsSignalProcess., enablednetworking:Challengesandopportunities,’’IEEENetw.,vol.34,
vol.14,no.1,pp.78–88,Jan.2020. no.3,pp.199–207,Mar.2020.
[87] S. Schwarzmann, C. C. Marquezan, M. Bosk, H. Liu, R. Trivisonno, [107] A.Bang,K.K.Kamal,P.Joshi,andK.Bhatia,‘‘6G:Thenextgiantleap
andT.Zinner,‘‘EstimatingvideostreamingQoEinthe5Garchitecture forAIandML,’’Proc.Comput.Sci.,vol.218,pp.310–317,Jan.2023.
using machine learning,’’ in Proc. ACM SIGCOMM, Oct. 2019, [108] R. Li, ‘‘Network 2030: A blueprint of technology, applications and
pp.7–12. 2399 market drivers towards the year 2030 and beyond,’’ ITU,
[88] M.H.H.Omar,K.P.Justin,K.W.M.Jonathan,T.S.D.Wendkouni,and Tech.Rep.,May2019.[Online].Available:https://www.itu.int/en/ITU-
S.O.Pr,‘‘UsingQoEmetricasadecisioncriterioninmultimediahetero- T/focusgroups/net2030/Documents/white_Paper.pdf
geneousnetworkoptimization:Challengesandresearchperspectives,’’J. [109] A.BarakabitzeandA.Hines,MultimediaStreamingServicesDeliveryin
Comput.Netw.Commun.,vol.2024,Feb.2024,Art.no.7864757. 2030andBeyondNetworks,2023,pp.203–220.
[89] A.E.Al-Issa,A.Bentaleb,A.A.Barakabitze,T.Zinner,andB.Ghita, [110] M.Z.Chowdhury,M.Shahjalal,S.Ahmed,andY.M.Jang,‘‘6Gwireless
‘‘Bandwidth prediction schemes for defining bitrate levels in SDN- communicationsystems:Applications,requirements,technologies,chal-
enabled adaptive streaming,’’ in Proc. 15th Int. Conf. Netw. Service lenges,andresearchdirections,’’IEEEOpenJ.Commun.Soc.,vol.1,
Manage.(CNSM),Oct.2019,pp.1–7. pp.957–975,2020.
157438 VOLUME13,2025

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
[111] M.Abdel-Basset,L.Abdel-Fatah,K.A.Eldrandaly,andN.M.Abdel- [132] C.LiuandY.Ma,‘‘Blockchain-basedprivacyprotectioninmetaverse
Aziz, ‘‘Enhanced computational intelligence algorithm for coverage streaming: The role of zero-knowledge proofs,’’ IEEE J. Sel. Areas
optimizationof6Gnon-terrestrialnetworksin3Dspace,’’IEEEAccess, Commun.,vol.41,no.2,pp.67–82,Feb.2023.
vol.9,pp.70419–70429,2021. [133] A. Clemm, M. T. Vega, H. K. Ravuri, T. Wauters, and F. D. Turck,
[112] Z.Mingming,M.Medvetskyi,M.Beshley,andH.Beshley,‘‘QoE-aware ‘‘Towardtrulyimmersiveholographic-typecommunication:Challenges
fusiontechniqueofmulti-pathvideotransmissionandmulti-connection and solutions,’’ IEEE Commun. Mag., vol. 58, no. 1, pp.93–99,
| forsoftware-defined5G/6Gnetworks,’’inProc.IEEE5thInt.Conf.Adv. |     |     |     | Jan.2020. |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
Inf.Commun.Technol.(AICT),Nov.2023,pp.52–57. [134] A.ElEssaili,S.Thorson,A.Jude,J.C.Ewert,N.Tyudina,H.Caltenco,
[113] T.Hoßfeld,M.Varela,L.Skorin-Kapov,andP.E.Heegaard,‘‘Agreener L. Litwic, and B. Burman, ‘‘Holographic communication in 5G
experience: Trade-offs between QoE and CO2 emissions in today’s networks,’’EricssonTechnol.Rev.,vol.2022,no.5,pp.2–11,May2022.
and6Gnetworks,’’IEEECommun.Mag.,vol.61,no.9,pp.178–184, [135] S. Anmulwar, N. Wang, V. S. H. Huynh, S. Bryant, J. Yang, and
Sep.2023. R.R.Tafazolli, ‘‘HoloSync: Frame synchronisation for multi-source
[114] P. S. Rufino Henrique and R. Prasad, ‘‘The road for 6G multimedia holographicteleportationapplications,’’IEEETrans.Multimedia,vol.25,
pp.6245–6257,2023.
| applications,’’ | in Proc. 23rd | Int. Symp. Wireless | Pers. Multimedia |     |     |     |     |
| --------------- | ------------- | ------------------- | ---------------- | --- | --- | --- | --- |
Commun.(WPMC),Oct.2020,pp.1–6. [136] Y.Duan,Q.Du,X.Fang,Z.Xie,Z.Qin,X.Tao,C.Pan,andG.Liu,
[115] S.Clayman,E.Karakıs,M.Tüker,E.Ak,B.Canberk,andM.Sayıt, ‘‘Multimediasemanticcommunications:Representation,encodingand
‘‘Dynamic packet content construction and processing for end-to- transmission,’’IEEENetw.,vol.37,no.1,pp.44–50,Jan.2023.
end streaming in 6G,’’ in Proc. IEEE 28th Int. Workshop Comput. [137] X. Zhang, M. Xu, R. Tan, and D. Niyato, ‘‘Learning-based auc-
Aided Model. Design Commun. Links Netw. (CAMAD), Nov. 2023, tion for matching demand and supply of holographic digital twin
pp.25–30. over immersive communications,’’ IEEE Trans. Multimedia, vol. 26,
[116] A.A.Barakabitze,I.-H.Mkwawa,A.Hines,andR.Walshe,‘‘QoE-aware pp.5884–5896,2024.
dynamic resource management in future softwarized and virtualized [138] J. P. Peixeiro, C. Brites, J. Ascenso, and F. Pereira, ‘‘Holographic
|     |     |     |     | data coding: Benchmarking | and | extending HEVC | with adapted |
| --- | --- | --- | --- | ------------------------- | --- | -------------- | ------------ |
networks,’’IEEEAccess,vol.11,pp.93310–93330,2023.
[117] L.U.Khan,W.Saad,Z.Han,E.Hossain,andC.S.Hong,‘‘Federated transforms,’’ IEEE Trans. Multimedia, vol. 20, no. 2, pp.282–297,
| learningforInternetofThings:Recentadvances,taxonomy,andopen |     |     |     | Feb.2018. |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
challenges,’’IEEECommun.SurveysTuts.,vol.23,no.3,pp.1759–1799, [139] Y. Huang, Y. Zhu, X. Qiao, X. Su, S. Dustdar, and P. Zhang,
|     |     |     |     | ‘‘Toward holographic | video communications: | A promising | AI- |
| --- | --- | --- | --- | -------------------- | --------------------- | ----------- | --- |
3rdQuart.,2021.
[118] M.Zawish,F.A.Dharejo,S.A.Khowaja,S.Raza,S.Davy,K.Dev,and driven solution,’’ IEEE Commun. Mag., vol. 60, no. 11, pp.82–88,
| P.Bellavista,‘‘AIand6Gintothemetaverse:Fundamentals,challenges |     |     |     | Nov.2022. |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
and future research trends,’’ IEEE Open J. Commun. Soc., vol. 5, [140] W. Jiang, ‘‘Media personalized recommendation system based on
pp.730–778,2024. network algorithm,’’ in Proc. IEEE 6th Adv. Inf. Technol., Electron.
[119] J. Feng, L. Liu, X. Hou, Q. Pei, and C. Wu, ‘‘QoE fairness Autom.ControlConf.(IAEAC),Oct.2022,pp.2061–2066.
resource allocation in digital twin-enabled wireless virtual reality [141] S. Ahn, H.-J. Yim, Y. Lee, and S.-I. Park, ‘‘Dynamic and super-
systems,’’IEEEJ.Sel.AreasCommun.,vol.41,no.11,pp.3355–3368, personalizedmediaecosystemdrivenbygenerativeAI:Unpredictable
Nov.2023. playsneverrepeatingthesame,’’IEEETrans.Broadcast.,vol.70,no.3,
[120] G.Pan,S.Xu,S.Zhang,X.Chen,andY.Sun,‘‘Qualityofexperience pp.980–994,Sep.2024.
orientedcross-layeroptimizationforreal-timeXRvideotransmission,’’ [142] K.Sorbán,‘‘Exploringtheethicalimplicationsofpersonalizedcontent
IEEETrans.CircuitsSyst.VideoTechnol.,vol.34,no.8,pp.7742–7755, recommendations in streaming services,’’ Univ. Public Service, Inst.
Aug.2024. Inf.Society,Budapest,Hungary,Tech.Rep.,2023.[Online].Available:
[121] H. Yu, M. Shokrnezhad, T. Taleb, R. Li, and J. Song, ‘‘Toward 6G- https://doi.org/10.22503/inftars.XXI.2021.2.5
based metaverse: Supporting highly-dynamic deterministic multi-user [143] K. Cömert and M. Akkaş, ‘‘Internet of Senses–potential applications
extended reality services,’’ IEEE Netw., vol. 37, no. 4, pp.30–38, andimplications,’’J.SoftComput.Artif.Intell.,vol.4,no.2,pp.48–54,
| Jul.2023. |     |     |     | Jan.2024. |     |     |     |
| --------- | --- | --- | --- | --------- | --- | --- | --- |
‘‘360◦
[122] I.-S. Comsa, R. Trestian, and G. Ghinea, mulsemedia experi- [144] N. Sehad, L. Bariah, W. Hamidouche, H. Hellaoui, R. Jäntti, and
enceovernextgenerationwirelessnetworks–Areinforcementlearning M.Debbah, ‘‘Generative AI for immersive communication: The next
approach,’’inProc.10thInt.Conf.QualityMultimediaExper.(QoMEX), frontierinInternet-of-Sensesthrough6G,’’IEEECommun.Mag.,vol.63,
| Sardinia,Italy,May2018,pp.1–6. |     |     |     | no.2,pp.1–12,Feb.2025. |     |     |     |
| ------------------------------ | --- | --- | --- | ---------------------- | --- | --- | --- |
[123] I.-S. Comşa, R. Trestian, G.-M. Muntean, and G. Ghinea, ‘‘5MART: [145] R.Joda,M.Elsayed,H.Abou-Zeid,R.Atawia,A.B.Sediq,G.Boudreau,
M.Erol-Kantarci,andL.Hanzo,‘‘TheInternetofSenses:Buildingon
| A 5G SMART | scheduling framework | for optimizing | QoS through |     |     |     |     |
| ---------- | -------------------- | -------------- | ----------- | --- | --- | --- | --- |
reinforcementlearning,’’IEEETrans.Netw.ServiceManage.,vol.17, semanticcommunicationsandedgeintelligence,’’IEEENetw.,vol.37,
| no.2,pp.1110–1124,Jun.2020. |     |     |     | no.3,pp.68–75,May2023. |     |     |     |
| --------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
[124] Y. Liu and X. Zhang, ‘‘lockchain for secure video streaming in the [146] X.Zhang,Y.Liu,andW.Chen,‘‘AI-drivenedgecomputingforreal-time
metaverse:Asurvey,’’IEEETrans.Netw.ServiceManage.,vol.23,no.4, streamingin6GIIoT,’’IEEETrans.IndustrialInform.,vol.19,no.4,
| pp.320–1298,Apr.2021. |     |     |     | pp.3456–3469,Apr.2023. |     |     |     |
| --------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
[125] F.Wang,J.Li,andH.Zhang,‘‘Decentralizedstreamingplatformsinthe [147] S. Kim, T. Park, and J. Lee, ‘‘Dynamic network slicing for real-time
metaverse:Blockchain-baseddcdns,’’IEEETrans.Multimedia,vol.25, streaming in 6G IIoT,’’ IEEE Commun. Surveys Tuts., vol. 25, no. 1,
| pp.512–527,2022. |     |     |     | pp.102–120,Jan.2023. |     |     |     |
| ---------------- | --- | --- | --- | -------------------- | --- | --- | --- |
[126] M. Xu and Z. Chen, ‘‘Blockchain-enabled streaming economy in the [148] X.Wang,Y.Zhang,andB.Lin,‘‘Blockchain-basedQoSframeworkfor
metaverse,’’ACMTrans.MultimediaComput.,Commun.,Appl.,vol.18, secureIIoTstreamingin6G,’’IEEETrans.DependableSecureComput.,
| no.1,pp.1–19,2022. |     |     |     | vol.20,no.3,pp.578–590,Mar.2023. |     |     |     |
| ------------------ | --- | --- | --- | -------------------------------- | --- | --- | --- |
[127] K. Zhang, L. Zhao, and Y. Wang, ‘‘Blockchain and distributed video [149] M. Ahmed, R. Khan, and Z. Abbas, ‘‘Semantic communication for
efficient6GIIoTstreaming,’’IEEETrans.WirelessCommun.,vol.23,
streaming:Challengesandopportunities,’’IEEEInternetThingsJ.,vol.8,
| no.3,pp.1087–1102,Mar.2021. |     |     |     | no.2,pp.456–472,Feb.2024. |     |     |     |
| --------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- |
[128] Y. Dai, W. Sun, and H. Zhao, ‘‘Blockchain-powered smart contracts [150] Y.-W. Huang, C.-W. Hsu, C.-Y. Chen, T.-D. Chuang, S.-T. Hsiang,
for video monetization in the metaverse,’’ IEEE Trans. Netw. Service C.-C.Chen,M.-S.Chiang,C.-Y.Lai,C.-M.Tsai,Y.-C.Su,Z.-Y.Lin,
Manage.,vol.20,no.1,pp.112–129,Jan.2023. Y.-L.Hsiao,O.Chubach,Y.-C.Lin,andS.-M.Lei,‘‘AVVCproposal
[129] X. Wang and B. Hu, ‘‘Nfts in metaverse video streaming: Digital withquaternarytreeplusbinary-ternarytreecodingblockstructureand
ownership and monetization,’’ J. Blockchain Res., vol. 5, no. 4, advancedcodingtechniques,’’IEEETrans.CircuitsSyst.VideoTechnol.,
| pp.87–101,2021. |     |     |     | vol.30,no.5,pp.1311–1325,May2020. |     |     |     |
| --------------- | --- | --- | --- | --------------------------------- | --- | --- | --- |
[130] D.KimandS.Park,‘‘Metaversecontentmonetizationusingblockchain [151] R. Sjoberg, J. Strom, L. Litwic, and K. Andersson, ‘‘Versatile video
|     |     |     |     | coding explained—The | future of video | in a 5G world,’’ | Ericsson |
| --- | --- | --- | --- | -------------------- | --------------- | ---------------- | -------- |
andnfts,’’IEEEAccess,vol.10,pp.32719–32733,2022.
[131] J.Sun,T.Yang,andX.Liu,‘‘Securedecentralizedvideostreamingin Technol.Rev.,vol.2020,no.10,pp.2–12,Oct.2020.[Online].Available:
themetaverse:Blockchainandzero-knowledgeproofs,’’IEEETrans.Inf. https://www.ericsson.com/4a92d7/assets/local/reports-papers/ericsson-
ForensicsSecurity,vol.17,no.6,pp.1504–1519,Jun.2022. technology-review/docs/2020/versatile-video-coding-explained.pdf
| VOLUME13,2025 |     |     |     |     |     |     | 157439 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
[152] B. Bross, J. Chen, J.-R. Ohm, G. J. Sullivan, and Y.-K. Wang, [173] X.-T.Chen,Y.Li,J.-H.Fan,andR.Wang,‘‘RGAM:Anovelnetwork
‘‘DevelopmentsininternationalvideocodingstandardizationafterAVC, architecturefor3Dpointcloudsemanticsegmentationinindoorscenes,’’
withanoverviewofversatilevideocoding(VVC),’’Proc.IEEE,vol.109, Inf.Sci.,vol.571,pp.87–103,Sep.2021.
no.9,pp.1463–1493,Sep.2021. [174] S.H.S.Rezaei,M.Modarressi,M.Daneshtalab,andS.Roshanisefat,
[153] D.Grois,A.Giladi,K.Choi,M.W.Park,Y.Piao,M.Park,andK.P.Choi, ‘‘Athree-dimensionalnetworks-on-chiparchitecturewithdynamicbuffer
‘‘Performance comparison of emerging EVC and VVC video coding sharing,’’inProc.24thEuromicroInt.Conf.Parallel,Distrib.,Network-
standardswithHEVCandAV1,’’SMPTEMotionImag.J.,vol.130,no.4, BasedProcess.(PDP),Feb.2016,pp.771–776.
pp.1–12,May2021. [175] S.Jain,A.B.Gandhi,S.Mehla,R.Aggarwal,andT.Kwatra,‘‘Virtual
[154] X.HoangVan,S.NguyenQuang,andF.Pereira,‘‘Versatilevideocoding drive:ImmersiveVR-controlledcarwithreal-timeinteractionandlive
basedqualityscalabilitywithjointlayerreference,’’IEEESignalProcess. videofeed,’’inProc.Int.Conf.Comput.Intell.Comput.Appl.(ICCICA),
Lett.,vol.27,pp.2079–2083,2020. May2024,pp.519–525.
[155] G. Esakki, A. S. Panayides, V. Jalta, and M. S. Pattichis, ‘‘Adaptive [176] A. Barakabitze and A. Hines, Emerging Applications and Services in
video encoding for different video codecs,’’ IEEE Access, vol. 9, Future5GNetworks.USA:Wiley,2023,pp.133–145.
pp.68720–68736,2021. [177] A. Barakabitze and A. Hines, 5G Network Slicing Management
[156] C. Jia, X. Hang, W. Liu, S. Wang, and S. Ma, ‘‘FPX-NVC: An ArchitecturesandImplementationsforMultimedia.USA:PubMed,2023,
FPGA-acceleratedP-framebasedneuralvideocodingsystem,’’inProc. pp.147–165.
IEEE Int. Conf. Vis. Commun. Image Process. (VCIP), Dec. 2022, [178] M.G.Hanna,L.Pantanowitz,B.Jackson,O.Palmer,S.Visweswaran,
p.1. J. Pantanowitz, M. Deebajah, and H. H. Rashidi, ‘‘Ethical and bias
[157] A. Aliouat, N. Kouadria, M. Maimour, S. Harize, and N. Dogh- considerations in artificial intelligence/machine learning,’’ Modern
mane,‘‘Region-of-interestbasedvideocodingstrategyforrate/energy- Pathol.,vol.38,no.3,Mar.2025,Art.no.100686.
constrainedsmartsurveillancesystemsusingWMSNs,’’AdHocNetw., [179] T. Li, Y. Xu, Y. Yang, and D. Liu, ‘‘Responsible AI for multimedia:
vol.140,Mar.2023,Art.no.103076. Research challenges and future directions,’’ IEEE Trans. Multimedia,
[158] DEDICAT 6G: Dynamic Coverage Extension and Distributed Intelli- vol.24,pp.2691–2705,2022.
genceforHumanCentricApplicationsWithAssuredSecurity,Privacy, [180] W. Liu, H. Yu, and Z. Guo, ‘‘Privacy-preserving personalized QoE
andTrust:From5GTo6G.Accessed:May22,2021.[Online].Available: modeling for video streaming using federated learning,’’ IEEE Trans.
https://5g-ppp.eu/dedicat-6g// Multimedia,vol.25,pp.1124–1136,2023.
[159] A.A.BarakabitzeandM.A.Ali,‘‘Behaviorandtechniquesforimproving [181] A.BarakabitzeandA.Hines,MultimediaStreamingServicesOverthe
performance of OFDM systems for wireless communications,’’ Int. Internet.Honolulu,HI,USA:IEEE,2023,pp.57–71.
J. Adv. Res. Comput. Commun. Eng., vol. 4, no. 1, pp.237–241, [182] T.Korikawa,C.Takasaki,K.Hattori,andH.Oowada,‘‘Time-topology
Jan.2015. routingin3Dnetworks,’’inProc.Int.Conf.Comput.,Netw.Commun.
[160] W.Mohr,A.Kaloxylos,K.Trichias,andC.Willcock,‘‘TheEuropean (ICNC).Wiley,Feb.2023,pp.348–352.
vision for 6G smart networks and services,’’ IEEE Commun. Mag., [183] A.BarakabitzeandA.Hines,QoEManagementofMultimediaService
vol.62,no.4,pp.10–12,Apr.2024. Challengesin5GNetworks.Switzerland:MDPI,2023,pp.167–183.
[161] ITU-T Study Group. (2020). ITU-T Recommendations on Quality of [184] M. Oubibi, A. Fute, D. Kangwa, A. A. Barakabitze, and M. A.
Experience (QoE). [Online]. Available: https://www.itu.int/en/ITU-T/ Adarkwah, ‘‘Interactive technologies in online teacher education in
studygroups/2020-2024/12 africa: A systematic review 2014–2024,’’ Educ. Sci., vol. 14, no. 11,
[162] N. Promwongsa, A. Ebrahimzadeh, D. Naboulsi, S. Kianpisheh, F. p.1188,Oct.2024.
Belqasmi,R.Glitho,N.Crespi,andO.Alfandi,‘‘Acomprehensivesurvey [185] J. Jonathan and A. A. Barakabitze, ‘‘ML technologies for diagnosing
of the tactile internet: State-of-the-art and research directions,’’ IEEE andtreatmentoftuberculosis:Asurvey,’’HealthTechnol.,vol.13,no.1,
Commun.Surv.Tut.,vol.23,no.1,pp.472–523,1stQuart.,2021,doi: pp.17–33,Jan.2023.
10.1109/COMST.2020.3025995.
[163] T.Stockhammer,‘‘Dynamicadaptivestreamingoverhttp:Standardsand
designprinciples,’’ACMMMSys,pp.133–144,2019.
[164] R. M. Huber and C. Keimel, ‘‘Subjective and objective assessment
of immersive media: VQEG-img developments,’’ IEEE Trans. Image
Process.,vol.30,pp.4860–4872,2021.
[165] System Architecture for the 5G System, document TS 23.501, 3rd
GenerationPartnershipProject(3GPP),2023.[Online].Available:https://
www.3gpp.org/DynaReport/23501.htm
[166] HuaweiTechnologies:VirtualReality/AugmentedRealityWhitePaper.
Accessed:Jun.13,2019.[Online].Available:https://www-file.huawei.
com/-/media/CORPORATE/PDF/ilab/vr-ar-en.pdf/
[167] S. A. Nchimbi, M. Kisangiri, M. A. Dida, and A. A. Barakabitze,
‘‘Design a services architecture for mobile-based agro-goods trans-
port and commerce system,’’ Mobile Inf. Syst., vol. 2022, pp.1–11,
Jan.2022.
[168] M.F.Juma,K.G.Fue,A.A.Barakabitze,N.Nicodemus,M.M.Magesa,
F. T. M. Kilima, and C. A. Sanga, ‘‘Understanding crowdsourcing of MONER ALSADER (Member, IEEE) received
agriculturalmarketinformationinapilotstudy:Promises,problemsand thebachelor’sdegreeintelecommunicationsand
possibilities (3Ps),’’ Int. J. Technol. Diffusion, vol. 8, no. 4, pp.1–16, network engineering and the M.Sc. degree in
2017. computer networking from the University of
[169] S.Gül,D.Podborski,J.Son,G.S.Bhullar,T.Buchholz,T.Schierl,and
Bedfordshire,andthePh.D.degreefromCranfield
C.Hellge,‘‘Cloudrendering-basedvolumetricvideostreamingsystem
University. He researched power management
formixedrealityservices,’’2020,arXiv:2003.02526.
for energy harvesting at Cranfield University.
[170] G.Caruso,F.S.Nucci,S.Rizou,J.Magen,G.Agapiou,P.Trakadas,and
HeiscurrentlyanAssistantProfessorwithSaudi
O.P.Gordo,‘‘Embedding5Gsolutionsenablingnewbusinessscenarios
ElectronicUniversity.Heisanexpertinthefieldof
in media and entertainment industry,’’ in Proc. IEEE 2nd 5G World
Forum,Apr.2020,pp.460–464. telecommunicationandnetworking.Hisresearch
[171] M.Z.Chowdhuryetal.,‘‘6Gwirelesscommunicationsystems:Applica- interestsincludepowermanagementforenergy,structurehealthmonitoring,
tions,requirements,technologies,challenges,andresearchdirections,’’ andwirelesssensornetworks,anichethatdemandsmeticulousdesignand
IEEEACCESS,vol.1,pp.957–975,2019. analysis. He holds several professional certifications and is a member of
[172] I.F.Akyildiz,A.Kak,andS.Nie,‘‘6Gandbeyond:Thefutureofwireless esteemed organizations, such as IET, SCE, and the Royal Aeronautical
communications systems,’’ IEEE Access, vol. 8, pp.133995–134030, Society.Beyondhisprofessionallife,hehasbeenactiveinextracurricular
2020. activities,holdingleadershippositionsinvariousclubsandsocieties.
157440 VOLUME13,2025

M.Alsaderetal.:QoE-DrivenAdaptiveVideoStreaming:Architectures,Techniques,andFutureResearchChallenges
ALCARDO ALEX BARAKABITZE (Member, IS-HAKA MKWAWA (Member,IEEE)received
IEEE) received the Ph.D. degree in computer thePh.D.degreeincomputingfromtheUniversity
science from the University of Plymouth, U.K., of Bradford, U.K., in 2004. He is currently
in2020. a Lecturer of computer systems and networks
HewasaVisitingResearcherwiththeDepart- with the School of Engineering, Computing and
ment of Electrical and Electronics Engineering, Mathematics,UniversityofPlymouth,U.K.Heis
University of Cagliari, Italy, and the ITU-T- also an Honorary Lecturer of computing with
Standardization Department, in 2016 and 2017, theDepartmentofComputerScience,University
respectively. He was a Distinguished Interna- of Liverpool, and a Visiting Professor with the
tional Associate with the Royal Academy of College of Computer Science and Information
Engineering, U.K., from 2024 to 2025. He is currently a Research Engineering, Sudan University of Science and Technology. He holds a
Fellow with the University College Cork (UCC), Ireland. He has over research track record of publications in the top international journals
70publicationsininternationalpeer-reviewedconferencesandjournalswith and conferences. His publications include ‘‘Guide to Voice and Video
2066citationsandanH-indexof17(asofFebruary2024).Hisresearch Over IP: For Fixed and Mobile Networks (Springer, 2013),’’ a book
interestsareAI/ML,telecommunicationsystemsandnetworkmanagement, and 14 book chapters. His research interests include wireless networks,
multimedia streaming QoE, 5G/6, and ICT4D. He was a member of multimediacommunication,QoEmanagementandcontrol,next-generation
ACM, in 2022. He served as the Technical Committee Chair for several internet,analyticalmodeling,cloudcomputing,andbigdata.Heservedas
national/international conferences, including IEEE ICC, IEEE QoMEX, acommitteememberforvariousprofessionalconferences/workshopsand
IEEEGlobeCom,andACMMMSys.Heisareviewerforvariousjournals anindependentexternalmemberofdegreeapprovalsforB.Sc.andM.Sc.
andservesontechnicalprogramcommitteesofleadingconferencesfocusing computernetworkingprograms.
onhisresearchareas.
VOLUME13,2025 157441