ReceivedFebruary5,2019,acceptedFebruary21,2019,dateofcurrentversionMarch25,2019.
DigitalObjectIdentifier10.1109/ACCESS.2019.2901778
QoE Modeling for HTTP Adaptive Video
Streaming—A Survey and Open Challenges
NABAJEETBARMAN ,(Member,IEEE),ANDMARIAG.MARTINI ,(SeniorMember,IEEE)
WirelessandMultimediaNetworkingResearchGroup,FacultyofScience,EngineeringandComputing,SchoolofComputerScienceandMathematics,Kingston
University,LondonKT12EE,U.K.
Correspondingauthor:MariaMartini(m.martini@kingston.ac.uk)
ThisworkwassupportedinpartbytheEuropeanUnion’sHorizon2020ResearchandInnovationProgrammeundertheMarie
Skłodowska-CurieGrantAgreement643072.
ABSTRACT With the recent increased usage of video services, the focus has recently shifted from the
traditionalqualityofservice-basedvideodeliverytoqualityofexperience(QoE)-basedvideodelivery.Over
thepast15years,manyvideoqualityassessmentmetricshavebeenproposedwiththegoaltopredictthe
video quality as perceived by the end user. HTTP adaptive streaming (HAS) has recently gained much
attention and is currently used by the majority of video streaming services, such as Netflix and YouTube.
HAS, using reliable transport protocols, such as TCP, does not suffer from image artifacts due to packet
losses, which are common in traditional streaming technologies. Hence, the QoE models developed for
other streaming technologies alone are not sufficient. Recently, many works have focused on developing
QoEmodelstargetingHAS-basedapplications.Also,therecentlypublishedITU-TRecommendationseries
P.1203proposesaparametricbitstream-basedmodelforthequalityassessmentofprogressivedownloadand
adaptiveaudiovisualstreamingservicesoverareliabletransport.Themaincontributionofthispaperisto
presentacomprehensiveoverviewofrecentandcurrentlyundergoingworksinthefieldofQoEmodeling
forHAS.TheHASQoEmodels,influencefactors,andsubjectivetestmethodologiesarediscussed,aswell
asexistingchallengesandshortcomings.Thesurveycanserveasaguidelineforresearchersinterestedin
QoEmodelingforHASandalsodiscussespossiblefuturework.
INDEXTERMS HTTPadaptivestreaming,QoEmodeling,TCP,videoqualityassessment.
I. INTRODUCTION video formats such as 4K and HDR result in files of enor-
The Cisco Visual Networking Index forecasts an increase mous size and hence call for modern video compression
of Internet traffic, with video alone being 82% of the net standards.Theeffortinthisdirectionresultedintherecently
consumer Internet traffic by 2021[1]. There has been a introduced new video compression standard H.265/MPEG-
considerable amount of work on video delivery over the HEVC, which on an average, for the tested sequences,
Internettomeetthisincreaseddemand.Withthedeployment isshowntoachieve50%highercompressionefficiencythan
of new wireless technologies such as 4G LTE-Advanced, its predecessor H.264/MPEG-AVC[2]–[4]. VP9, a royalty-
theavailableend-userbandwidthhasincreasedconsiderably free encoder developed by Google as a competitor of the
over the recent years and it will further increase with 5G H.265/HEVC encoder, has gained much popularity and is
wireless systems. However, with the emerging video for- supportedbyalmostallbrowsersexceptforSafari.Licensing
mats (e.g., Ultra High Definition (UHD), High Dynamic issues with H.265/HEVC and the aim to develop a more
Range(HDR),LightField)andnewservicessuchasVirtual futuristic royalty-free video codec led to the creation of a
Reality, Social-TV, Cloud Gaming, the available network consortium of industry partners called Alliance for Open
technology will not be able to meet the increased demand Media (AOM).1 The joint efforts of the members of AOM
for high bandwidth for all the users and to satisfy users’ havesincethendrovetothedevelopmentoftheAV1codec2
expectations for any content, any place, any time. The new with the final bitstream specification frozen in early 2018.
The associate editor coordinating the review of this manuscript and
1http://aomedia.org/
approvingitforpublicationwasMartinReisslein. 2https://aomedia.googlesource.com/aom/
2169-3536 2019IEEE.Translationsandcontentminingarepermittedforacademicresearchonly.
VOLUME7,2019 Personaluseisalsopermitted,butrepublication/redistributionrequiresIEEEpermission. 30831
Seehttp://www.ieee.org/publications_standards/publications/rights/index.htmlformoreinformation.

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
RecentstudiescomparingtheperformanceofAV1withx265, Therestofthispaperisorganizedasfollows.Westartwith
x264andlibvpxconsideringon-demandadaptivestreaming abriefintroductiontoQoE,QoEassessmentmethodologies
applications have found it to result in the highest bitrate andthevariousinfluencefactorswhichneedtobetakeninto
savings but at the cost of huge encoding times[5],[6]. The account for QoE model design in Section II. In Section III
applicabilityofsuchencodersforlivestreamingapplications we discuss QoE modeling and how QoE models can be
remainsanopenquestion. classifiedbasedonthetypeofinputinformationtheyrequire.
The advancements in the field of video streaming have ThenwebrieflyintroduceinSectionIVtheHAStechnology.
recently resulted in the rise of both Video-On-Demand SectionVreviewstheexistingworkinthefieldofHASmod-
(VOD) (YouTube, Netflix, Amazon Video, Hulu, etc.) elingandprovidesadetaileddiscussionoftheproposedmod-
and Live (Twitch.Tv, YouTubeGaming) streaming services. els.InSectionVIadetaileddiscussionontheeffectofvarious
Asevident,videostreamingisnotanichemarketanymore, influence factors is presented and in Section VII subjective
and there exist a wide range of options for the consumers testmethodologiesasusedformodelvalidationand/ortesting
to choose from. Hence, as a service provider, it is no more bythemodelproponentsisdiscussedalongwiththeirimpor-
sufficientjusttoprovideaservice,butitisequallyimportant tance, advantage and shortcomings. Section VIII presents a
tomakesurethattheneedsandexpectationsoftheenduser discussion on publicly available HAS based datasets which
of the offered services are met. This has led to the shift canactasavaluableresourceformodeldesignandvalidation
from traditional technical Quality of Service (QoS) based by future researchers. Finally, in Section IX we summarize
assessment (see, e.g.,[7]) to Quality of Experience (QoE) our observations and findings and point out some existing
basedassessment(see,e.g.,[8],[9]). gapsandchallengesforfuturework.
TocorrectlydeterminetheenduserQoEandsubsequently
move towards QoE based control and management, there II. QoE:DEFINITIONANDASSESSMENT
| exists a need | for | the development |     | of reliable |     | and | accurate |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- | --- |
METHODOLOGIES
QoEmodels.Suchmodelsusuallytakeintoaccountvarious A. QoEDEFINITION
networkandapplicationlevelfactors(includingseveralQoS TheEUQualinetcommunity(COSTActionIC1003:‘‘Euro-
factors)andaimatpredictingtheQoEasexperiencedbythe
peanNetworkonQualityofExperienceinMultimediaSys-
| enduser. |             |     |            |     |     |          |     | temsandServices’’)definesQoEas:‘‘QoEisthedegreeof |     |     |     |     |
| -------- | ----------- | --- | ---------- | --- | --- | -------- | --- | ------------------------------------------------- | --- | --- | --- | --- |
| Having   | established | the | importance | of  | QoE | modeling | and |                                                   |     |     |     |     |
delightorannoyanceoftheuserofanapplicationorservice.
consideringthatHTTPAdaptiveStreaming(HAS)isthepre- Itresultsfromthefulfillmentofhisorherexpectationswith
ferredvideostreamingtechnology,wepresentinthispapera respect to the utility and/or enjoyment of the application
reviewofexistingQoEmodelsforHASapplications.While
|     |     |     |     |     |     |     |     | or service | in the | light of | the user’s personality | and current |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ---------------------- | ----------- |
there exist previous surveys, such as by Seufertetal.[10], state’’[12],[13].QoEtakesintoaccounttheenduser’sexpe-
which discuss HAS and related influence factors, and by rienceandlevelofsatisfactionandisofmuchinteresttoboth
Juluri et al.[11], which discuss tools and measurement academic and industrial players in the field of multimedia.
methodologiesforpredictingQoEofonlinevideostreaming Understandingtheendusers’expectationsandexperienceis
services,asurveyofQoEmodelsforHASapplicationsisstill
|     |     |     |     |     |     |     |     | paramount | to the | development | of future services | as well as |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----------- | ------------------ | ---------- |
missing.Towardsthisendwepresentinthispaperareviewof improvementoftheexistingtechnologiesandservices.While
the proposed QoE models for HAS applications. The major traditionallyQoShasbeenusedtomeasuretheeffectiveness
objectivesofthisrevieware: of a service, it fails to take into account end user related
• To classify the existing models and provide the factors (user expectation, environmental factors, etc.). Also,
| reader | with | an overview |     | of different |     | works | so far |     |     |     |     |     |
| ------ | ---- | ----------- | --- | ------------ | --- | ----- | ------ | --- | --- | --- | --- | --- |
QoSislimitedtotelecommunicationservicesandreliesonly
in the field of QoE modeling for HAS applications on technical measurements. QoE on the other hand covers
(SectionV). domainsbeyondtelecommunicationsandismultidisciplinary
Toidentifythedifferentinfluencefactorsasconsidered
| •   |     |     |     |     |     |     |     | in nature, | including | domains | such as psychology, | business, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | ------------------- | --------- |
bythemodelproponentsanddiscusstheirimpactonthe technical,environmental,etc.Figure1illustratestheencap-
modeldesignandperformance(SectionVI).
sulationofQoSandQoE.
| • To present |                 | the different |           | subjective   | test | methodologies |      |     |     |     |     |     |
| ------------ | --------------- | ------------- | --------- | ------------ | ---- | ------------- | ---- | --- | --- | --- | --- | --- |
| used         | for model       | design        | and       | validation.  | We   | discuss       | how  |     |     |     |     |     |
| such         | information     |               | can favor | reproducible |      | research      | and  |     |     |     |     |     |
| steer        | the development |               | of        | models valid | in   | different     | set- |     |     |     |     |     |
tingsandconditions(SectionVII).
| • To present |     | a list | of publicly | available |        | open       | source |     |     |     |     |     |
| ------------ | --- | ------ | ----------- | --------- | ------ | ---------- | ------ | --- | --- | --- | --- | --- |
| datasets     | for | HAS    | QoE model   | design    | and/or | validation |        |     |     |     |     |     |
(SectionVIII).
| • To identify |     | existing | research | gaps | and provide |     | a set of |     |     |     |     |     |
| ------------- | --- | -------- | -------- | ---- | ----------- | --- | -------- | --- | --- | --- | --- | --- |
recommendationsforfuturemodeldesignandvalidation
| (SectionIX). |     |     |     |     |     |     |     | FIGURE1. | QoSandQoEencapsulation. |     |     |              |
| ------------ | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------------- | --- | --- | ------------ |
| 30832        |     |     |     |     |     |     |     |          |                         |     |     | VOLUME7,2019 |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
B. QoEASSESSMENT of influence factors can be evaluated due to constraints in
ITU-T Recommendation P.10/G.100 Amendment 5 defines test duration and assessors. Objective VQA using metrics
QoE assessment as the process of measuring or estimating such as Peak Signal to Noise Ratio (PSNR) and Structural
the QoE for a set of users of an application or a service Similarity(SSIM)index,whilefastandcomparativelyeasier
withadedicatedprocedure,andconsideringtheinfluencing toimplement,donotalwayscorrelatewellwiththeenduser
factors (possibly controlled, measured, or simply collected quality[16],[17]. For two videos of different (perceivable)
andreported)[13].ThemainobjectiveofQoEassessmentis quality,theobjectivemetricmayprovideasimilarscoreand
thedesignofasystemwhichcanidentifythevariousfactors hence does not necessarily reflect the end user’s perceived
and their influence on the end user QoE. Such information quality. Also, many objective metrics require the source
canthenbeusedbythevariousstakeholdersforoptimization sequences, which is not practical in most of the real-world
alongtheprocessofservicedelivery(encodingpipeline,load qualityestimationscenarios.
balancing, resource allocation, etc.) to provide a reasonable Quality metrics such as PSNR and SSIM were initially
QoE to the end user while making optimized usage of the developedandusedforImageQualityAssessment(IQA).For
available resources. Lossy compression is usually required Video Quality Assessment (VQA), they are calculated on a
for multimedia data which need to be transported over the frame-by-frame basis and then the final score is reported as
Internet, to decrease the required bandwidth and transport theaverageoftheindividualscoresoverthefulldurationof
costs. During lossy compression, information is lost, with thevideosequence.Therealsoexistdifferentpoolingmeth-
higher compression ratios resulting in a higher amount of ods to combine the scores such as Minkowski summation,
informationloss.Also,intraditionalstreamingtechnologies, exponentialweighting,etc.Adiscussionoftemporalpooling
transmissionerrorssuchasjitter,delay,packetloss,etc.,lead strategies is out of the scope of this paper and interested
tofurtherartifactswhichareannoyingtotheenduser.Sinceit readerscanreferto[18]foraninterestingcomparisonofthe
isalmostimpossibleformostpracticalapplicationstoprovide poolingmechanismsandtheirperformanceinHASapplica-
aservicewithoutanyartifact,aproperQoEmodel/metriccan tions.
helpquantifying theamountand kindof distortionsandthe Traditional models used for VQA, such as PSNR, SSIM,
magnitudeoftheireffectontheenduserQoE,whichcanthen VQM[19], etc., are not designed for long-term quality pre-
lead to the design of proper strategies to help overcoming dictions.Also,mostofthetraditionalobjectiveVQAmetrics
suchartifacts. were designed for quality estimation of impairments due to
compressionand/orduetopacketlossesetc.,duringthetrans-
missionprocess.Theydonottakeintoaccountimpairments
C. VIDEOQUALITYASSESSMENT(VQA)METHODOLOGIES suchasrebuffering,qualityswitchesetc.,whicharepresent
VQA approaches can be categorized into two main cate- in HAS applications. Therefore, new approaches for QoE
gories:objectiveandsubjective.ObjectiveVQAmethodsare estimation model design are required for HAS applications
mathematical models that aim at providing a quality score which take into account IFs such as rebuffering and quality
which closely resembles the perceived image/video quality. switchingalongwithimpairmentsduetolossyencoding.
SubjectiveVQA,ontheotherhand,triestotakeintoaccount
theuserfeedbackintheformofratingsandtargetstoestimate D. QoEINFLUENCEFACTORS
thevideoqualityasperceivedbytheenduser. AQoEinfluencefactoris‘‘anycharacteristicofauser,sys-
Subjective assessment scores are typically reported as tem,service,application,orcontextwhoseactualstateorset-
MeanOpinionScore(MOS)whichistheaverageoftheopin- tingmayhaveaninfluenceontheQualityofExperiencefor
ionscorescollectedfromtheassessors.Forrepeatabilityand theuser’’[12].AsdefinedinITU-TRec.P.10/G.100Amend-
validation purpose, common guidelines for conducting sub- ment 5, QoE influence factors include the type and char-
jectivetestsareissuedinITU-TRecBT.500andITU-TRec acteristics of the application or service, context of use,
P.910[14],[15]. These recommendations include a detailed the user’s expectations with respect to the application or
descriptionofthetestsettings,methodologyandprocedures serviceandtheirfulfillment,theuser’sculturalbackground,
that need to be followed, including data processing guide- socio-economic issues, psychological profiles, emotional
lines,suchasoutlierdetection,etc. stateoftheuser,andotherfactorswhosenumberwilllikely
The common approach to evaluate an objective quality expandwithfurtherresearch[13].InfluencefactorsonQoE
metric’s performance is to calculate the correlation coeffi- canbegroupedintothefollowingfourcategoriesasdescribed
cientsandMSEvaluesbetweentheMOSscoresestimatedvia bySkorin-KapovandVarela[20].
theobjectiveVQAmetricsandtheactualMOSscoresfrom
subjectiveassessment,forthesamesetoftestsequences. 1) SYSTEMIFs
BothobjectiveandsubjectiveVQAapproacheshaveinher- SystemIFsmostlyconsistofthetechnicalaspectsofquality,
entdrawbacks.WhilesubjectiveVQAprovidesinformation for example, the ones which can be measured using QoS
on the actual quality experienced by the users, it is not basedmeasurementapproaches.Theycoverawiderangeof
suitable for real-world applications. Also, conducting sub- aspectssuchasmediarelated(qualityswitchingevents),net-
jectivetestsincurscostsandtime,andonlyasmallnumber workrelated(wired/wireless/mobile,bandwidth,delay,jitter,
VOLUME7,2019 30833

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
packet loss, etc., resulting in impairments such as tempo- includesQoEoptimizationandcontrol,typicallyperformed
ral interruptions/pauses) or end-user device related (display based on models or measurements. Again, the optimization
resolution, playback capabilities such as supported codecs, process and the parameters controlled will depend on the
formats,etc.). stakeholder and the application type. In this paper, we limit
|     |     |     |     |     |     | our discussion |     | to the first | step, focusing |     | on QoE | Modeling |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | -------------- | --- | ------ | -------- |
2) HUMANIFs forHASapplicationsusingreliabletransportprotocolssuch
asTCPorQuickUDPInternetConnections(QUIC)[25].
HumanorUserIFsincludeaspectswhichrefertotheinfor-
mationabouttheend-userandrelatedaspects.Theseinclude
individualcharacteristicsofausersuchasexpectationsfrom A. IMPORTANCEOFQoEMODELINGFORDIFFERENT
theservice,memoryandrecencyeffects,usagehistoryofthe STAKEHOLDERS
application(e.g.,browsinghistory,frequentlyplayedvideo), QoE modeling is one of the critical steps in the QoE man-
agementprocesschain,astheperformanceoftheQoEmodel
demographicandsocio-economicbackground,physicaland
mentalconstitution(users’emotionalstate),memory,catego- willdecidethereliabilityandaccuracyofthenextstepsalong
rizationandattentionamongmanyothers. QoEbasedmanagement.Wediscussnexttheimportanceof
QoEmodelingfromthepointofviewofvariousstakeholders
| 3) CONTEXTIFs |     |     |     |     |     | inthemultimediastreamingprocesschain. |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
ContextIFsdealwithfactorssuchaslocation,enduserenvi-
ronment (viewing environment, acoustic conditions, etc.), 1) NETWORKPROVIDER
time of the day, type of usage (e.g., just casual browsing, With increasing demand for OTT services, both VOD and
live,thereisatremendouspressureonthenetworkoperators
newlyreleasedepisodeoffavoriteTVshow),timeofservice
consumption(peaktime,offloadtime,etc.) to provide seamless connectivity and high QoE to the end
|     |     |     |     |     |     | users. QoE | models | can help | network | operators |     | identifying |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ------- | --------- | --- | ----------- |
4) CONTENTIFs the various IFs and their respective impact on the end user
QoEandhenceallowthenetworkoperatorstotakenecessary
OneofthemostimportantisthecontentIFswhichaddresses
actions(resourceallocationsuchasnetworkthrottling,load
| the characteristics | of the | content. | The | aspects | in this cat- |     |     |     |     |     |     |     |
| ------------------- | ------ | -------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
egory include information about the content being offered balancing,cachingandnetworkprovisioning)topreventuser
churn.
bytheservice/applicationunderconsideration.Forexample,
| for video, | the content level | IFs | are duration, | video | type and |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | ------------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
2) SERVICEPROVIDER
contentcomplexity(spatialandtemporalcomplexity).
Intoday’shighlycompetitiveenvironmentwithalmostsimi-
larpricingschemes,theserviceprovidercannotrelyonprofit
III. QoEMODELING
|          |            |            |       |      |            | generation | based | solely on | the provision |     | of a | service, but |
| -------- | ---------- | ---------- | ----- | ---- | ---------- | ---------- | ----- | --------- | ------------- | --- | ---- | ------------ |
| Managing | Quality of | Experience | (QoE) | in a | communica- |            |       |           |               |     |      |              |
tion system is a complex task, primarily consisting of three shouldalsotakeintoaccountdifferentfactorswhichmayshift
steps, as shown in Figure 2 and discussed in[21] and[22]. the user base to the competitors. For example, for a service
|            |                   |     |               |     |          | provider | measurable | QoE | factors | such as | viewing | duration |
| ---------- | ----------------- | --- | ------------- | --- | -------- | -------- | ---------- | --- | ------- | ------- | ------- | -------- |
| A key step | in QoE management |     | is the design | of  | QoE mod- |          |            |     |         |         |         |          |
els. ITU-T Recommendation P.1201 defines a QoE model are of huge interest[26]. For advertisement based services,
longerviewingdurationimpliesmoreadvertisement.Onthe
| as ‘‘An algorithm | with | the purpose | of  | estimating | the sub- |     |     |     |     |     |     |     |
| ----------------- | ---- | ----------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
jective (perceived) quality of a media sequence’’[8]. QoE other hand, for subscription based services, shift of even a
models take into account various influence factors and try smaller percentage of viewer base can result in significant
effectonrevenues.OneofthedisadvantagesofHASservices
toestimatetheenduserQoE.QoEmonitoringandmeasure-
ment(s) can be done by any stakeholder and the parameters is the requirement of additional storage space, as multiple
copiesofthesamefilearestoredintheserver.Insuchcases,
measuredwilldependontheapplicationandtheinterestsof
|     |     |     |     |     |     | optimized | encoding | bitrates | can | lead to | huge storage | space |
| --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | --- | ------- | ------------ | ----- |
thestakeholder[23],[24].ThefinalstepinQoEmanagement
savingsfortheOTTproviderwhilealsoreducingthedemand
forrequiredbandwidth.Hence,properQoEmodelscanpro-
|     |     |     |     |     |     | vide an     | insight | into the IFs | and their | impact | on      | the service, |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ------------ | --------- | ------ | ------- | ------------ |
|     |     |     |     |     |     | and in turn | allow   | the service  | provider  |        | to take | appropriate  |
decisions/measurestoensurehighenduserQoE.
3) DEVICEMANUFACTURER
|     |     |     |     |     |     | Nowadays, | most  | of the device      | manufacturers, |                  | such | as Sam- |
| --- | --- | --- | --- | --- | --- | --------- | ----- | ------------------ | -------------- | ---------------- | ---- | ------- |
|     |     |     |     |     |     | sung, LG, | Sony, | etc., are involved |                | in manufacturing |      | of both |
smallscreendevices(mobiles,tablets)andbigscreendevices
(PC/TV).Differentdeviceshavedifferentcapabilitiesandthe
|     |     |     |     |     |     | perceived | quality | depends | on various | factors, | one | of which |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | ---------- | -------- | --- | -------- |
FIGURE2. QoEmanagementprocess. is the device screen size. Also, small screen devices have
| 30834 |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2019 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
different processing capabilities compared to large screen the prediction monotonicity of a model can be evaluated
devices.Hence,goodQoEmodelscanprovideinsighttothe usingtheSpearman’sRankCorrelationCoefficient(SROCC)
device manufacturers, considering the device features (dis- between the predicted and actual subjective rating scores.
playsize,displayresolution,CPU,ram,etc.),onwhatsettings Finally,thepredictionconsistencyofthemodelcanbeeval-
tousesuchthattheQoEoftheendusercanbemaximized. uated using measurements such as the Outlier Ratio (OR).
Also, media-layer models (see Section III-C.1) can be used A low OR value indicates a high consistency of prediction,
forcodeccomparisonandhenceallowdevicemanufacturers withOR=0implyingthatthemodelwillbestabletopredict
toprovideoptimizedencodinganddecodingsupportsoasto theQoE.AgoodQoEmodelshouldprovideinsightonhow
supportthelatestcodecsintheshortestpossibletime.Many theIFsaffecttheQoEoftheenduser.Suchinsightcanhelp
devicemanufacturersarealsointerestedinQoEmodelingfor variousstakeholdersinamoreefficientandoptimizedsystem
| productionofQoEmonitoringsolutionssuchasprobes,QoE |     |     |     |     |     |     | design. |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
estimationmodulesetc.
|     |     |     |     |     |     |     | C. QoEMODELCLASSIFICATION |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
4) ENDUSER Depending on the application area or range of system or
In the end, the user is the king or queen. The success of servicethemodelappliesto,thereexistmanywaystoclassify
a service will depend on the acceptance of the same by modelssuchasbasedonmodelinputparameters,application
users. As mentioned in[22], successful QoE management scope,measurementscope,etc.[22].Whilethereexistmany
will lead to satisfied end users as their requirements and/or approachesforclassificationofmodels,weusetheapproach
expectationswillbemetandhencetheymaybefurtheropen presented by Takahashi et al.[29], similar to the one pre-
toadoptnewandcomplexservices,leadingtogrowthofmore sentedbyRaakeetal.[30]asshowninFigure3.
advancedtechnologies.
| To summarize, | QoE | modeling | can | help | us identify | the |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
variousKeyPerformanceIndicators(KPIs).Theactualappli-
cabilityandperformanceofthemodelwillvarydependingon
thestakeholderasdifferentactorsinvolvedwillfocusondif-
ferentaspects(mostlytheonestheycancontrol).Forexam-
ple,inthecaseofHAS,anetworkprovidermaybeinterested
inrebuffering,qualityswitches,etc.andtheircorresponding
effectonQoEastheyaredirectlyorindirectlyrelatedtothe
| network | QoS parameters | such | as delay, | jitter, | packet | loss, |     |     |     |     |     |     |     |
| ------- | -------------- | ---- | --------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
etc.Acontentprovidermaybeinterestedmoreintheeffect
| of average  | bitrate,        | segment | size, video      | popularity, | etc.,          | for |          |                                                        |     |     |     |     |     |
| ----------- | --------------- | ------- | ---------------- | ----------- | -------------- | --- | -------- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
| example,    | to save storage |         | costs, optimized |             | video caching, |     |          |                                                        |     |     |     |     |     |
| etc. At the | application     | layer,  | the service      | provider    | may            | be  |          |                                                        |     |     |     |     |     |
| interested  | in IFs such     | as      | adaptation       | frequency,  | adaptation     |     |          |                                                        |     |     |     |     |     |
|             |                 |         |                  |             |                |     | FIGURE3. | QoEmodelclassificationforstreamingapplications(adapted |     |     |     |     |     |
magnitude, etc. to take these into account for the design of basedoninputfrom[30]).
theclient’sadaptationalgorithm.
| B. QoEMODELPERFORMANCEEVALUATION |     |     |     |     |     |     | 1) SIGNAL-BASEDMODELS |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
The criteria for the evaluation of the performance of an Signal-based models, also known as pixel-based models or
|     |     |     |     |     |     |     | media-layer | models, | utilize | the | decoded | audio/video | signal |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | --- | ------- | ----------- | ------ |
objectiveQoEmodel,asmentionedinitiallyinVideoQuality
Experts Group (VQEG) FRTV Phase I and later in VQEG to estimate the video quality. Since such models do not use
anycodecspecificinformation,theyarewidelyusedincodec
FRTVPhaseII[27],[28],are:
• PredictionAccuracyItreferstotheabilityofamodelto comparisonandoptimizationofunknownsystems.
predict the subjective rating scores with low error. The Basedontherelationshipbetweentheinputandoutputof
|     |     |     |     |     |     |     | the system, | i.e., | depending | on  | the amount | of source | (refer- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | --- | ---------- | --------- | ------- |
accuracyoftheQoEmodelwillaffecttheapplicability
andeffectivenessoftheQoEmanagementprocess. ence) information required, VQA metrics can be classified
|              |              |           |           |     |            |        | as Full        | Reference | (FR), | Reduced | Reference | (RR) | and No |
| ------------ | ------------ | --------- | --------- | --- | ---------- | ------ | -------------- | --------- | ----- | ------- | --------- | ---- | ------ |
| • Prediction | Monotonicity |           | It refers | to  | the degree | of     |                |           |       |         |           |      |        |
| model’s      | prediction   | agreement | with      | the | relative   | magni- | Reference(NR). |           |       |         |           |      |        |
tudesofthesubjectiveratingscores. (a) FR:Asthenamesuggests,FRmetricsrequiretheavail-
• PredictionConsistencyItreferstotheabilityofamodel ability of full information of the source video. They
tomaintainpredictionaccuracyoverawiderangeoftest are computed based on a frame-by-frame comparison
sequenceswithavarietyofvideoimpairments. between the reference and the distorted image/video.
Thepredictionaccuracyofamodelcanbeevaluatedbyusing Thesourcevideoshouldbeavailableinpristinequal-
thePearsonLinearCorrelationCoefficient(PLCC)between ity (unimpaired and uncompressed) so that there can
the predicted and actual subjective rating scores. Similarly, be a direct comparison (e.g., pixel by pixel) between
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     | 30835 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
the reference and distorted image/video. Due to the used as input to the model. Such models are also relatively
availability of full source information, these metrics computationally inexpensive and can be used for real-time
are usually more accurate than their counterpart (RR QoEmonitoring.Bitstreambasedmodelshaverecentlyfound
or NR metrics) but as such are not suitable for most applicationinthefieldofmultimediastreamingservicessuch
real-worldapplications.Someofthemostwidelyused as ITU-T Rec. P.1202, with ITU-T Rec. P.1203 being the
qualitymetricsinthefieldofimageandVQAareFR mostrecentlyapprovedrecommendationforadaptiveaudio-
metricssuchasMSE,PSNRandSSIM[16]andITU-T visual streaming services over reliable transport[9]. While
Recommendations[31]–[33]. bitstream based models show comparatively higher corre-
(b) RR:RRmetricshaveaccesstolimitedsourceinforma- lation with subjective quality scores, they suffer from the
tion.Duetopartialsourceinformation,theyareusually drawbackthattheyaresuitableforaspecificcodec.Bitstream
less accurate than the FR metrics. Some of the RR models which can minimize their performance reliance on
metricsare[34]–[41]. codec specific parameters such as size of MB, motion vec-
(c) NR: No reference quality metrics do no use any tor size, etc. will prove to be more useful and find wider
source/reference information and try to predict the acceptance.
quality based on the received signal. Commonly used
NR metrics include DIIVINE, BRISQUE, BLIINDS 4) HYBRIDMODELS
andNIQE[42]–[45].Intheabsenceofsourceinforma- Hybrid models are usually the most effective ones as they
tion, such metrics are usually less accurate than their combinetwoormoreofthepreviouslydescribedmodelsand
counterparts,FRandRRmetrics. hencecanusemuchmoreinformationasinputcomparedto
anyofthestandalonemodelsdiscussedpreviously.
2) PARAMETRICMODELS
Parametricmodelsusemeasuredorexpectedpacket/network IV. HTTPADAPTIVEVIDEOSTREAMING
relatedparameterstoestimatethequality.Thesecanbefur- InthispaperwefocusexclusivelyonHTTPAdaptiveStream-
ther classified in packet-layer models and planning models, ing (HAS) applications using reliable delivery mechanisms
describedbelow. such as TCP and QUIC. Reliable transport protocols such
(a) Packet-layer models: Parametric packet-layer mod- as TCP make sure that all data will be delivered correctly
els utilize only information that can be extracted tothedestinationprocesswithoutanyerrors.Thisisusually
from packet headers, such as bitrate, packet loss rate achieved by a connection oriented approach between the
(PLR),framerate,frametype,etc.,andnomediasig- senderandthereceiverwiththereceiveracknowledgingthe
nal information is required. Such models are hence receipt of packets and retransmission of lost or erroneous
non-intrusive in nature and are easily deployable and packets. Some of the most widely used implementations of
computationally very inexpensive (e.g., ITU-T Rec. HASinclude:
P.564 for speech and ITU-T Rec. P.NAMS[8],[46]). • AdobeHTTPDynamicStreaming(HDS)[50]
Due to the absence of any payload information, such • AppleHTTPLiveStreaming(HLS)[51]
modelsarenotsuitableforindividualQoEmonitoring • MicrosoftSmoothStreaming[52]
solutions such as determination of effect of content • DynamicAdaptiveStreamingoverHTTP(DASH)[53].
dependenceonend-userQoE. The first three are proprietary and vendor specific HAS
(a) PlanningModels:Unlikeothermodels,planningmod- implementations while DASH, also commonly known as
els do not require input information from an existing MPEG-DASH, is an open source international standard
service.Suchmodelsestimatethequalitybasedonthe developed by MPEG[54]. The underlying logic is common
qualityplanninginformationavailableduringtheplan- in all these implementations with some differences in the
ningphasefromthenetworksandterminals.Informa- manifestfile,recommendedsegmentsize,etc.
tionsuchasexpectedbitrate,PLR,codectype,etc.are
usedasinputinthiskindofmodels.Suchmodeltype A. CONCEPTOVERVIEW
includes some of the most widely used model in the Figure 4 illustrates the basic concept behind HAS appli-
fieldofvideophoneservices(ITU-TRec.G.1070[47]), cations. The video file is encoded at different representa-
E-model(ITU-TRec.G.107,widelyusednetworktool tion levels (spatial/temporal/quality, see Section IV-B) and
for public switched telephone network (PSTN) and then divided into chunks (also referred to as segments) of
VoiceoverInternetProtocol(VoIP)[48])andforvideo equal durations (often 2, 4 or 10 seconds, but depends on
andaudiostreamingapplications[49]. the standard/implementation) which are then stored on a
server. The reverse process of first segmenting and then
3) BITSTREAMMODELS encoding can also be used, as currently done by most of
Bitstream models take into account the encoded bitstream the Over-the-top (OTT) providers to speed up the encoding
andpacketlayerinformation.Featuressuchasbitrate,frame process. When a first request for the video file is made by
rate,QuantizationParameter(QP),PLR,motionvector,mac- the client, the server sends the corresponding manifest file
roblocksize(MBS),DCTcoefficients,etc.areextractedand (e.g.,.mpdforDASH,.m3u8forHLS)whichconsistsofthe
30836 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
|     |     |     |     |     |     |     | of less | (more) |     | bits per | pixel, | hence | resulting | in  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --- | -------- | ------ | ----- | --------- | --- |
lower(higher)bitratevalues.
|     |     |     |     |     |     |     | The actual      | dimensions  |            | of adaptation |              | will depend |            | on the |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | ---------- | ------------- | ------------ | ----------- | ---------- | ------ |
|     |     |     |     |     |     |     | application     | type        | and        | also on       | the content  | type.       | For        | most   |
|     |     |     |     |     |     |     | content types,  | compression |            | based         | quality      | is          | considered | the    |
|     |     |     |     |     |     |     | most important  |             | dimension. | For           | similar      | bitrate     | values,    | spa-   |
|     |     |     |     |     |     |     | tial resolution | reduction   |            | is perceived  |              | better than | frame      | rate   |
|     |     |     |     |     |     |     | reduction       | (the actual | impact     |               | of upscaling | depends     |            | on the |
|     |     |     |     |     |     |     | specific player |             | used for   | video         | playback     | at          | the end    | user   |
FIGURE4. HASSchematic(Q3,Q2andQ1denotehigh,mediumandlow device), hence resolution is one of the most widely used
qualitylevelrespectively). adaptationdimensions[56].Forsmallerscreensizeddevices
suchasmobile,tablets,etc.,spatialresolutionplaysanimpor-
details about the video file such as video duration, segment tant role in QoE. In general, in HAS, adaptation in multi-
size, available representation levels, codec, etc. The client ple dimensions is perceived better than a single dimension
then requests for video chunks based on its rate adapta- adaptation[57] and hence is widely used by major OTT
| tion logic. | The  | client’s          | rate adaptation |              | logic can | be broadly | providers. |        |          |         |           |     |              |     |
| ----------- | ---- | ----------------- | --------------- | ------------ | --------- | ---------- | ---------- | ------ | -------- | ------- | --------- | --- | ------------ | --- |
|             |      |                   |                 |              |           |            | HAS is     | one of | the most | popular | streaming |     | technologies |     |
| categorized | into | throughput-based, |                 | buffer-based |           | and hybrid |            |        |          |         |           |     |              |     |
approach.Foracomprehensivesurveyoftherateadaptation for video delivery over the Internet, currently used by the
methodsforHAS,wereferthereaderstothesurveypaperof primary OTT providers such as Netflix and YouTube, with
bothtogetherconsistingofmorethan50%ofthetotalpeak
Kuaetal.[55].Figure4illustratestheconceptofstreaming
assumingathroughput-basedrateadaptationmethod.Itcan Internet traffic for fixed access networks in North America
andLatinAmerica[58].ThesuccessofHAScanbeattributed
| be observed | that | the client, | based | on its | network | condition, |     |     |     |     |     |     |     |     |
| ----------- | ---- | ----------- | ----- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
adaptsthequalityofthevideotoprovideasmoothstreaming tothefollowingadvantagesitoffersovertraditionalstream-
| experiencetotheenduser. |     |     |     |     |     |     | ingtechnologies: |         |       |          |            |             |          |        |
| ----------------------- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ----- | -------- | ---------- | ----------- | -------- | ------ |
|                         |     |     |     |     |     |     | 1) Scalability:  |         | Since | HTTP     | based      | progressive | download |        |
|                         |     |     |     |     |     |     | solutions        | already |       | existed, | no special | streaming   |          | server |
B. QUALITYSWITCHINGDIMENSIONS
infrastructureisrequiredallowingforthereuseofexist-
| Videos can | be encoded |     | at different | bitrates | (quality | levels) |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------------ | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
byadjustingany/two/allofthefollowingparameters:spatial inginfrastructure.
|     |     |     |     |     |     |     | 2) Reliability: |     | HAS | uses | reliable | transport | protocols |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---- | -------- | --------- | --------- | --- |
resolution,framerateandQP.Abitratedecreaseusuallyindi-
|     |     |     |     |     |     |     | (mostly | TCP, | recently | QUIC) | with | guaranteed |     | packet |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | -------- | ----- | ---- | ---------- | --- | ------ |
cateslowerqualitybutthereversedoesnotnecessarilyholds
true,i.e.,increasingthebitrateafteracertainthreshold(which delivery and congestion control mechanisms. Hence
networkimpairmentssuchaspacketlossdonotcause
dependsonthevideocontenttype)doesnotnecessarilyresult
in higher (perceived) quality videos. Figure 5 illustrates the any artifacts such as blurring, motion jerkiness, etc.,
asthelost/corruptedpacketsareretransmitted.
| adaptation | dimensions |     | for video | encoding, | described | in the |         |          |      |       |     |            |       |     |
| ---------- | ---------- | --- | --------- | --------- | --------- | ------ | ------- | -------- | ---- | ----- | --- | ---------- | ----- | --- |
|            |            |     |           |           |           |        | 3) Runs | natively | over | HTTP: | HAS | uses HTTP, | which | is  |
following:
firewallfriendlyandavoidsNetworkAddressTransla-
1) SpatialAdaptation:Thevideosareencodedatdifferent
tion(NAT),leadingtoeasieraccesstoHASservicesto
| resolutions, |     | hence | decreasing | the | number | of pixels in |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ---------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
theendusers.
theverticaland/orhorizontaldimensions.
|             |     |             |     |          |            |        | 4) Stateless | protocol: |     | In HAS, | the | server | does not | store |
| ----------- | --- | ----------- | --- | -------- | ---------- | ------ | ------------ | --------- | --- | ------- | --- | ------ | -------- | ----- |
| 2) Temporal |     | Adaptation: | The | temporal | resolution | of the |              |           |     |         |     |        |          |       |
anyinformationrelatedtotheclientand/ortherequests.
| video | is decreased |     | by dropping |     | some of | the frames, |     |     |     |     |     |     |     |     |
| ----- | ------------ | --- | ----------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisisusefulfromanetworkpointofview(e.g.,load
| i.e., | encoding | a lower | number | of  | frames | per second, |     |     |     |     |     |     |     |     |
| ----- | -------- | ------- | ------ | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
balancing)asnoweachrequestistreatedindividually,
hencereducingtheencodedbitrate.
|     |     |     |     |     |     |     | hence | can | be handled | by  | any of | the servers, |     | without |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------- | --- | ------ | ------------ | --- | ------- |
3) CompressionQualityAdaptation(Switching):Increas-
keepingtrackofwhichserverisservingwhichrequest.
| ing | (decreasing) |     | QP values | results | in an | allocation |         |                |     |        |                |     |     |     |
| --- | ------------ | --- | --------- | ------- | ----- | ---------- | ------- | -------------- | --- | ------ | -------------- | --- | --- | --- |
|     |              |     |           |         |       |            | Some of | the challenges |     | in the | implementation |     | of  | HAS |
include:
|     |     |     |     |     |     |     | 1) Increased |     | overhead: | In general, |     | for a good | streaming |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ----------- | --- | ---------- | --------- | --- |
performance,TCPthroughputofapproximatelytwice
ofthevideobitrateisrequired,whichpointstoamajor
drawbackofHASapplications[59].
|     |     |     |     |     |     |     | 2) Increased |             | storage      | and        | encoding        | costs:    | Due      | to the  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------ | ---------- | --------------- | --------- | -------- | ------- |
|     |     |     |     |     |     |     | creation     | of          | multiple     | quality    | representations |           |          | for the |
|     |     |     |     |     |     |     | same         | video/audio |              | content,   | HAS             | solutions | need     | much    |
|     |     |     |     |     |     |     | higher       | storage     | requirements |            | compared        |           | to other | tradi-  |
|     |     |     |     |     |     |     | tional       | streaming   |              | solutions. | While           | the costs | of       | storage |
FIGURE5. Videoqualityswitchingdimensions. haveconsiderablydecreasedovertherecentyears,new
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     |     | 30837 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
videoformatssuchas4kandHDRresultsinhugefile (framefreezingoccurs).Sucheventsinvideostreaming
sizes.Hence,thehighstoragecostsarestillaconcern areusuallyrepresentedbyaloadingsignoraspinning
for OTT providers, especially because a typical OTT wheel,orsometimesjustthecurrentfrozenframe,and
providerincludesmillionsofvideocontents. occurbecauseofthevideopacketsarrivinglate.
3) Quality switching: The rate adaptation algorithm • Total duration of rebuffering: It refers to the combined
switchesvideoqualitydependingonthenetworkcon- lengthofallrebufferingeventsinasinglemediasession.
dition and/or buffer status. While quality switching is Frequency of rebuffering: Frequency of rebuffering
•
animportantfeatureofHASwhichhelpsinminimizing refers to the number of rebuffering events per unit of
| thenumberofstallingevents,frequentqualityswitch- |     |     |     |     |     | time. |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
ingmightresultinincreaseduserannoyance. • Temporal location of rebuffering: Temporal location of
4) Live streaming: During the initial years, HAS was rebufferingindicatesthetimeinstantwhenarebuffering
| exclusively |     | used for VOD/Offline | streaming |     | applica- | eventstarts. |     |     |     |
| ----------- | --- | -------------------- | --------- | --- | -------- | ------------ | --- | --- | --- |
tions. While many services currently use HAS for • Quality switching: Quality switching, also referred to
real-timeapplications,encodingvideosinmultiplerep- as rate adaptation or quality adaptation, refers to the
resentationsinreal-timeremainsabigchallenge. change of quality over the duration of the media
| 5) Fullsegmentdownload:FormostoftheHASapplica- |     |     |     |     |     | playback. |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
tions, full segment download is required before play- • Quality switching frequency: It refers to the rate of
back of the segment can start. Such requirement can changeofthequalityduringthemediaplayback.
leadtoincreasedcasesofstallingeventsduringvideo • Quality switching magnitude: It refers to the ‘‘gap’’
| playback. |     |     |     |     |     | betweenthelevelsofqualityswitching. |     |     |     |
| --------- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
• Down-switching:Qualityswitchingfromahigherqual-
ityleveltoalowerqualitylevel.
V. HASQoEMODELING
Inthissection,wereviewtheworkrelatedtomodelswhich • Up-switching: Quality switching from a lower quality
predict the subjective quality (e.g., MOS) for HAS applica- leveltoahigherqualitylevel.
|              |            |                 |          |     |            | Time on | the highest | layer: Time on | the highest layer |
| ------------ | ---------- | --------------- | -------- | --- | ---------- | ------- | ----------- | -------------- | ----------------- |
| tions. Table | 2 presents | a comprehensive | overview |     | of all the | •       |             |                |                   |
models(26modelsintotal)reviewedinthiswork.Themod- indicates the percentage of time the media playback is
atthehighestquality.
elsareclassifiedintothreecategoriesdependingontheirtype.
ThetabledescribesthevariousIFsconsideredbythemodels, • InitialLoadingDelay:Alsoknownasinitialbuffering,
along with the modeling method and the main observations initial loading delay is the time duration between the
|     |     |     |     |     |     | request for | video playback | by the client | and the actual |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------- | -------------- |
asreportedbythemodelproponents.Itisimportanttonote
thatinthisreviewwelimitthescopeonlytomodelsproposed startofthevideoplayback.
forHASapplications.Foramoregenericoverviewofmodels • Encoding Quality: It refers to the quality of the com-
forQoEprediction,wereferthereadertothesurveypaperby pressedvideo/audiosequenceduetolossofdatafollow-
Julurietal.[11]. ingtheencodingprocess.Thisistypicallyexpressedin
termsofanobjectivequalitymetric(e.g.,PSNR,SSIM,
| We start | in Section | V-A with a | discussion | of  | definitions |     |     |     |     |
| -------- | ---------- | ---------- | ---------- | --- | ----------- | --- | --- | --- | --- |
andterminologyalongwithacommonsetofsymbolssoas VMAF).Someauthorscharacterizetheencodingquality
to have a more comprehensive understanding of the models intermsofbit-rateorQPvalue.
|     |     |     |     |     |     | Primacy | and Recency | Effects: |     |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | -------- | --- |
discussed later in Section V-B. The models are presented • The psychological phe-
and discussed based on their classification as described nomenaaccordingtowhichexperienceswhichoccurred
recently(recency),andexperiencesthatoccurredatthe
inTable2.
verystartofthesession(primacy)affectmoretheexpe-
riencequality.
A. SYMBOLSANDTERMINOLOGY
Table1describestheparametersandcorrespondingsym-
Weintroduceheretheterminologyweuseforthedescription bols used in this review. In addition we use I , I & I
QS ILD RB
of the models: for simplicity and easier comparison of the to denote the impairment due to quality switching, initial
| models | later, our | goal is to use consistent |     | terminology | and |     |     |     |     |
| ------ | ---------- | ------------------------- | --- | ----------- | --- | --- | --- | --- | --- |
loadingdelayandrebufferingrespectively.3
symbolsforallthemodelsdescribed.
| Media | Session: | Media session |     | indicates | video/ |                 |     |     |     |
| ----- | -------- | ------------- | --- | --------- | ------ | --------------- | --- | --- | --- |
| •     |          |               |     |           |        | B. HASQoEMODELS |     |     |     |
audiovisual playback from the start till the end of the Here we present and discuss the QoE models in detail.
| video | and includes | the effects | of initial | loading | delay, |     |     |     |     |
| ----- | ------------ | ----------- | ---------- | ------- | ------ | --- | --- | --- | --- |
Westartwithadiscussionoftheproposedparametricmodels,
rebuffering events and quality switching if any. Hence, followed by a discussion of bitstream and hybrid mod-
inthepresenceofanyoftheseevents,themediasession
|     |     |     |     |     |     | els. We classify | the models | based on | the discussion in |
| --- | --- | --- | --- | --- | --- | ---------------- | ---------- | -------- | ----------------- |
lengthwillbelongerthanthatoftotalvideo/audiovisual
SectionIII-C.
playbacklength.
• Rebuffering:Rebufferingreferstotheeventwhenthere
3IILD,IRBandIQSreferonlytotherespectivetypeofimpairmentandnot
is no data in buffer, hence video playback is stalled necessarilytohowtheyareactuallycalculated
| 30838 |     |     |     |     |     |     |     |     | VOLUME7,2019 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
TABLE1. Summaryofsymbolsusedinthisreview. 1) PARAMETRICMODELS
OneoftheearliestworkstowardsbuildingaQoEmodelfor
HAS applications was presented by Mok et al.[60]. This
model quantifies QoE for HAS applications using network
and application layer QoS parameters. Based on analytical
models, empirical evaluation, and (subsequent) subjective
tests, Mok et al. quantified the predicted MOS as a simple
equationas:
MOS =4.23−0.0672L −0.742L −0.106L (1)
ti fr tr
whereL ,L andL arethelevels(1,2or3correspondingto
ti fr tr
low,mediumandhighlevels)ofinitialloadingdelay(L ),
ILD
rebuffering frequency (R ) and rebuffering duration (R )
N AVG
respectively. The rebuffering frequency is found to be the
main IF. While this work has the advantage of proposing a
simple linear equation mapping application QoS metrics to
QoE, the subjective assessment used to perform the regres-
sion analysis to obtain the proposed model was limited to
only a single video (single content type) rated by 10 users
and limited to a single resolution, which is not realistic
for most HAS applications. An evaluation of the proposed
modelonasubjectivedatabaseofnewdataismissing.Also,
the work assumes constant network bandwidth, Round Trip
Time(RTT)andPacketLossRate(PLR),whichisnotalways
truefortherealnetworksandalsoleavesoutoneofthemajor
IFsofHAS:qualityswitching.Theauthorsconductedfurther
studiestocorrelateQoEwithnetworkQoS,anditisobserved
that the rebuffering frequency increases due to decreased
network throughput by packet loss and RTT. One of the
majoradvantagesofthismodelisthefactthatcontent-related
information is not used, hence the model can be used for
encrypted traffic quality estimation by stakeholders such as
networkproviderofthird-partyOTTs.
An extended version of this model is presented in[61]
which takes into account user actions such as pausing and
forward/backwardsseeking,leadingtoabettermodelfitand
anincreaseinitsexplanatorypower.Videoimpairmentsmay
lead to various user reactions such as pausing the video,
resizing, etc. and hence such factors need to be considered
inthemodeldesignforamorerealisticQoEmodel.Among
all the models reviewed in this paper, this is the only work
whichconsidersuseraction.Basedonthemodel,itisfound
thatwhilesomeuseractionssuchaspauseshowamarginal
effectonthefinalQoE,otheruseractionssuchasswitching
the screen size have no significant impact on the final QoE
score. While the proposed model is an improvement over
the previous model[60] taking into account more content
types, more test subjects and multiple resolutions, it is still
limited by the network parameters taken into consideration
andalsodoesnottakeintoaccountqualityswitchingrelated
impairments.Also,theperformanceevaluationofthemodel
ismissing.
Rodríguezetal.[62]modeltheeffectoflocationofpauses
dependingontheirpositioninthevideo.Theyproposevideo
VOLUME7,2019 30839

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
TABLE2. Overviewofthereviewedmodels.
30840 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
StreamingQualityMetrics(VsQM)as: andI istheeffectofinitialloadingdelayasdefinedin(4).
ILD
Itwasobservedthatthequalityoftheinitialtemporalsegment
|     |     |      |     | (cid:88)R k | L W |     |     |                                                        |     |     |     |     |     |     |
| --- | --- | ---- | --- | ----------- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|     |     |      | =   | N           | i i |     |     | hasagreaterinfluenceontheQoEandforswitchingevents,     |     |     |     |     |     |     |
|     |     | VsQM |     |             |     |     | (2) |                                                        |     |     |     |     |     |     |
|     |     |      |     |             | V   |     |     | thespatialresolutionaffectsthequalitymorethanthetempo- |     |     |     |     |     |     |
|     |     |      |     | i=1         | LS  |     |     |                                                        |     |     |     |     |     |     |
ralresolutions.Themodelisshowntobeoflowcomplexity
| where | k, R , | L, W | and | V are | the number |     | of temporal |     |     |     |     |     |     |     |
| ----- | ------ | ---- | --- | ----- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
N i i LS in terms of processing and energy consumption and hence
segments of a video, number of rebuffering events, average suitablefordevicessuchasmobilephonesandtabletswhich
lengthofthepauses,weightfactorrepresentingthedegreeof
havelimitedpowerandprocessingcapabilities.Theproposed
| degradation | and | length | of each | segment | respectively. |     | Based |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ------- | ------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
parametricmodelusesonlyapplication-levelparametersand
| on the | subjective | scores, | this | is  | then mapped |     | into 5-point |          |              |     |            |              |     |          |
| ------ | ---------- | ------- | ---- | --- | ----------- | --- | ------------ | -------- | ------------ | --- | ---------- | ------------ | --- | -------- |
|        |            |         |      |     |             |     |              | hence is | suitable for | QoE | monitoring | of encrypted |     | traffic, |
MOSscaleas:
specificallyatthenetworkside.Themodelvalidationisdone
(cid:18) k (cid:19) using similar types of patterns as used for model design,
|     |      |     |       | (cid:88)R | L   | W   |     |                                                    |     |     |     |     |     |     |
| --- | ---- | --- | ----- | --------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | VsQM |     | =Cexp |           | N   | i i | (3) |                                                    |     |     |     |     |     |     |
|     |      | MOS |       |           |     |     |     | andalsoconsidersafixednumber(four)ofsegments,hence |     |     |     |     |     |     |
V LS
|     |     |     |     | i=1 |     |     |     | leavinganopenquestionabouttheperformanceofthemodel |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
where C is a constant and all other factors are as defined onunknowndatasetemployingdifferentplayoutpatternsand
in (2). Based on the subjective assessment results, it was ofdifferentvideolength.
Albertietal.[63]presentaparametricQoEmodelwhich
| found | that the | first | segment | has | higher impairment |     | weight |     |     |     |     |     |     |     |
| ----- | -------- | ----- | ------- | --- | ----------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
compared to middle or end segments, based on which the mapstheQoSparameterstoestimateQoEas:
authorsconcludethatthepauses,inthebeginning,aremore
N−1
| important | and | hence | will have | a   | higher impact |     | on the final |     |     |     |          |     |     |     |
| --------- | --- | ----- | --------- | --- | ------------- | --- | ------------ | --- | --- | --- | -------- | --- | --- | --- |
|           |     |       |           |     |               |     |              |     |     | =   | (cid:88) | ki  |     |     |
QoEvalueforstreamingscenarios.Thisisincontradictionto eMOS a i x (6)
i
i=0
otherworkswhichconsidertherecencyeffecttohaveahigh
| impact | on the | QoE. | The authors |     | also propose | some | guide- |     |     |     |     |     |     |     |
| ------ | ------ | ---- | ----------- | --- | ------------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
...x
lines for subjective test assessment methodologies such as where x 0 N−1 are measured values of parameters such
asvideobitrate,framerate,QP,rebufferingfrequency,aver-
consideringlongerdurationsequenceswhichismoretypical
agerebufferingdurationandqualityswitchingrate,whereas
ofHASapplicationsandtoallowmultipleviewingofthetest
|     |     |     |     |     |     |     |     | ...a    | ...k    |     |             |             |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- | ----------- | ----------- | --- | --- |
|     |     |     |     |     |     |     |     | a 0 N−1 | and k 0 | N−1 | are tunable | parameters. |     | The |
sequencesasdesiredbythetestsubjects.
authorsreportthatQoEdegradationduetoencodingquality
| An  | extension |     | of this | model | is  | presented | by  |     |     |     |     |     |     |     |
| --- | --------- | --- | ------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Rodríguez et al.[66]. Here temporal interruptions (number, is on a shorter time interval compared to QoE degradation
|     |     |     |     |     |     |     |     | due to IFs | such as rebuffering |     | and | quality | switching. | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | --- | --- | ------- | ---------- | --- |
locationandlengthoftherebufferingevents)duringavideo
|     |     |     |     |     |     |     |     | model parameter | estimation |     | and design | are done | using | sub- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | --- | ---------- | -------- | ----- | ---- |
session,initialloadingdelayandqualityswitching(number
|     |     |     |     |     |     |     |     | jective tests | consisting | of two | video | sequences | and | taking |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ------ | ----- | --------- | --- | ------ |
andlocation)areconsideredtoproposeanewqualitymetric,
|      |                                             |     |     |     |     |     |     | into account | various | QP, rebuffering |     | and quality | switching |     |
| ---- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --------------- | --- | ----------- | --------- | --- |
| VsQM | .Theeffectofinitialloadingdelayismodeledas: |     |     |     |     |     |     |              |         |                 |     |             |           |     |
DASH
|     |     |           |     |     |     |     |     | factors. | The authors | report | high prediction |     | accuracy | with |
| --- | --- | --------- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | --------------- | --- | -------- | ---- |
|     |     | =5−Bexp(α |     |     | /V  |     |     |          |             |        |                 |     |          |      |
I ILD d L ILD L ) (4) 0.5 MOS difference for the worst case when compared to
|     |     |     |     |     |     |     |     | MOS scores | obtained | by subjective |     | tests. | In the | absence |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------- | --- | ------ | ------ | ------- |
,α,V
| whereL      | ILD   | L andBareinitialbufferingdelay(seconds), |     |             |        |     |          |              |            |     |             |            |     |        |
| ----------- | ----- | ---------------------------------------- | --- | ----------- | ------ | --- | -------- | ------------ | ---------- | --- | ----------- | ---------- | --- | ------ |
|             |       |                                          |     |             |        |     |          | of the model | validation | and | performance | estimation |     | (e.g., |
| exponential | decay | factor,                                  |     | total video | length | and | constant |              |            |     |             |            |     |        |
regardingthecorrelationofthepredictedMOSwiththeactual
respectively.Forqualityswitchingevents,theauthorsobserve
MOS),theactualperformanceofthemodelremainsanopen
thatforthesamefrequencyofrebuffering,comparedtotem-
question.
| poral | resolution | changes, | spatial |     | resolution | changes | have a |     |     |     |     |     |     |     |
| ----- | ---------- | -------- | ------- | --- | ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Hoßfeldetal.[64]investigatetheeffectoffiveIFs:qual-
moresignificanteffectonusers’QoE.ThefinalQoEmodel,
|      |                                     |     |     |     |     |     |     | ity switching | amplitude, | last | quality | level, recency |     | time for |
| ---- | ----------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ---- | ------- | -------------- | --- | -------- |
| VsQM | ,modeledusing5-pointACRMOSscoresis: |     |     |     |     |     |     |               |            |      |         |                |     |          |
DASH the different number of switches, the frequency of quality
switchingandtimeonthehighestqualitylevel.Theauthors
|     |     |     | (cid:20) k | W (cid:18) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | =   |     | (cid:88)   | i          |     |     |     |     |     |     |     |     |     |     |
VsQM DASH Cexp R Ns L i found that quality switching shadows the effect of recency
V
i=1 LS and also recency time (total duration of high-quality play-
|     |     |     | n   |     | m   | (cid:19)(cid:21) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88) (cid:88) back after the last quality switch) does not affect the QoE.
|     |     |     | +   | P R + | Q   | S   | −I (5) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
ji ji li li ILD Also, it was observed that the time on each quality level
j=1 l=1 has a more significant impact than that of the frequency of
whereCisaconstant,i,jandlindicatesthecurrentsegment, rebuffering. Discarding other IFs (based on statistical anal-
ysis),theauthorsproposeasimpleQoEmodel,considering
| temporal | switching |     | type and | spatial | switching | type | respec- |     |     |     |     |     |     |     |
| -------- | --------- | --- | -------- | ------- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
tively,k isthetotalnumberofsegmentsinamediasession, onlytwoIFs,whichtakeintoaccounttheeffectofamplitude
R and L are number and average length of pauses in the (the difference between the two quality levels) and time on
| Ns  | i   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thehighestlevelusinganexponentialrelationshipas:
| same temporal                                    |     | segment, | m   | and n | are number | of  | spatial and |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | -------- | --- | ----- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| temporalresolutionswitchingtypesrespectively,W,P |     |          |     |       |            |     | and         |     |     |     |     |     |     |     |
i ji
|     |     |     |     |     |     |     |     |     | )=0.003e0.06th |     |     | +2.498 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------ | --- | --- |
QliareweightfactorsandS li isthenumberofswitchingtype y(t h (7)
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     |     | 30841 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
where y(t ) is the predicted MOS, and t is the time on the The MSQ is modeled and evaluated in terms of 5-point
h h
highestlevel.Theeffectofswitchingamplitudeisquantified ACR.Theproposedmodelparameterselectionandvalidation
byboundingtheMOSvaluestothequalitylevels.Thepro- areperformedbyusingwelldesignedanddefinedsubjective
posedmodelonlyproposesaparametricequationusingsub- assessment using a total of thirty 1-min audiovisual SRCs
jectivetestresultsusingasinglecontenttypeandconsiders and eleven 3-minute audiovisual source sequences. While,
onlytwoqualitylevelsandlacksperformancevalidation. as discussed by the authors, the test design ‘‘hides’’ the
Lievensetal.[65]proposeaMOSpredictor,PQM,based effectofsourcequalityontheQoE,intermsofthereported
onuserevaluationsas: RMSEandPLCCvalues,theoverallmodelperformancestill
looksquitepromising,especiallyconsideringthefactthatthe
PQM(T) =
T +γ
1
R
(cid:88) Q (cid:104) fidelity (cid:0) t−Fτ (cid:0)∂fide
∂
l
t
ity(t)(cid:1)(cid:1) (cid:105) modeldoesnotuseanymediabitstreaminformation,result-
ALL T inginalowcomplexitymodelwhichissuitableforencrypted
−εαFβ
(cid:0)∂free
∂ z t es(t)
(cid:1)
−Fδ (cid:0)
∂framerate(t)(cid:1)
(8) QoEmonitoring.Theauthorsreportthatthemodelperforms
∂t quite well for video sequences without rebuffering and also
with some specific sequences with rebuffering (where the
whereFτ,Fβ,Fδ,T andR
ALL
arefunctionswhichrepresent
rebufferingoccursatthepointwherethecompressionquality
quality switching, amount of rebuffering events, frame rate,
is worse). This leads to the observation that the amount of
totaldurationoverwhichMOSisevaluatedandtotaltimeof
rebufferingevent,respectively.α,γ andε areconstantsand QoEdegradationduetorebufferingisdependentonthequal-
ity of the video frame where the rebuffering occurs. Hence
Qistheencoder-sideMOSforagivenfidelity(qualitylevel).
resultsfromotherworkswhichtakeintoaccountthetemporal
Based on the subjective assessment using three Full HD
locationofpauses(e.g.,[62])canbeusedtofurtherimprove
(FHD)videosequencesandvariousencodingandrebuffering
uponthiswork.Unlikemostoftheotherworks,Yamagashi
conditions (not described in the paper) the authors observe
andHayashidiscussthelimitationsoftheirworksuchasver-
anincreaseofMOSwithanincreaseinresolutionorbitrate.
ificationofthemodelfortheH.264highprofile(whichisstill
Below a specific bitrate, upscaled lower resolution video is
thepreferredandwidelyusedprofileforTVsets),validation
found tobe ofhigher quality comparedto higherresolution
ofthemodelforsmallscreendevices,performanceevaluation
video encoded at the same bitrate. On the temporal scale,
ofindividualqualityestimationmodules,etc.Futureworkin
no significant difference was found in between 50fps and
thisdirectionmayincludeaddressingtheseshortcomingsand
25 fps video while lower frame rate video (below 25fps)
alsothepossibleinclusionofotherIFssuchasinitialloading
wasratedlowerwiththevideohavingqualitychangesrated
delay,etc.
lower than that of constant quality. Effect of rebuffering
was observed to be non-linear depending on the individual
2) MEDIA-LAYERMODELS
durationofeacheventandfrequencyofrebuffering.Thework
Whilethemostusedvideoqualitymetrics(e.g.,PeakSignal
presents only a parametric equation taking into account the
toNoiseRatio(PSNR),StructuralSimilarity(SSIM),Video
variousIFsbutdoesnotreporttheperformanceofthemodel
Multimethod Assessment Fusion (VMAF)) are in this cate-
usingsubjectiveassessment.
gory,wefocushereonlyonthemetricsspecificallydeveloped
Yamagashi and Hayashi[67] present a quality model
foradaptivestreamingoverHTTP.
whichwassubmittedaspartofthecompetitionfortheITU-T
Takingintoaccountthemulti-segmentandmulti-ratefea-
Rec. 1203. The model follows the framework used in Para-
turesofHASapplications,Wangetal.[68]presenttwoQoE
metric Non-intrusive Assessment of TCP-based multimedia
modelsbasedonregressionandclassification.Usingregres-
Streaming quality (P.NATS) consisting of an audio qual-
sion they propose an evolved PSNR (ePSNR) model based
ity estimation module and video quality estimation module
on average, maximum, minimum and standard deviation of
whichoutputper-secondrespectivequalityscoreswhichare
differentialPSNR(dPSNR),wheredPSNRisdefinedas:
then integrated into per-second audiovisual coding quality
scores in the audiovisual-integration/temporal module. The dPSNR=PSNR−PSNR (11)
ref
overallQoEisdefinedas:
where PSNR is the PSNR of the available highest rate
ref
Q =1+(Q −1)S (9) segment and PSNR is the PSNR of the segment under con-
Overall ST
sideration.ePSNRisthendefinedas:
which integrates the short term (per-second) audio-visual
codingquality,Q ,withotherIFsfactorsas:
ePSNR=[a b c d]×Q(cid:101)+e (12)
ST
−R R /V A/V where a,b,c,d,e are constant values and Q(cid:101) is the vector
S =exp( N )exp(− ALL L )exp(− L ) (10) definedas:
s s s
1 2 3 (cid:20) (cid:21)T
where R N is the number of rebuffering events, R ALL is the Q(cid:101)= mean(q ij ) max(q ij ) min(q ij ) std(q ij ) (13)
j j j j
total length of rebuffering events, A is the average interval
between rebuffering events, V is the length of the content whereq representsthedPSNRoftheith videosceneandjth
L ij
ands ,s ands areconstantswithpositivevalues. videosegment.PleasenotethatT herereferstothetranspose
1 2 3
30842 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
operation. The classification method model uses weighted approximately represents the average quality of the video.
k-nearest neighbor (WkNN) based on segment bitrate and Theinstantaneousqualitiesarethenpooledusingexponential
videosegmentpositiontopredictQoE.Bothmodelsareeval- decay temporal pooling (which takes into account the end
uatedusingsubjectivetestsconsistingoftwovideosusinga user attention memory) to obtain the final QoE estimation.
real-worldLTEnetworktestbed.Bothregressionandclassi- Themodelisshowntobeoflowcomplexityandstablewith
ficationbasedmethodsareshowntoprovidehighcorrelation reasonableperformanceresults.Sincethesubjectivetestsfor
withsubjectiveMOS.Basedonthecorrelationresults,thelast model parameter estimation and subsequent validation are
two segments have been found to have moreeffect than the doneusingonlytwoQPvalues,wewillseelaterthat,inthe
other segments. In terms of PLCC results, the classification presence of multiple resolutions and QP values, the model
basedmodelisfoundtohavehigherperformancecompared performanceisnotthatsatisfactory.
to the regression method, but in terms of complexity the Guoetal.[71]proposeamodelwhichestimatestheoverall
ePSNRmodelisfoundtobeoflowercomplexity. quality using a linear combination of median and minimum
oftheinstantaneousqualityas:
3) BITSTREAMMODELS
|         |                |         |     |           |           |         |         |       |     |           | =αQ       |        | +βQ      |                |      |
| ------- | -------------- | ------- | --- | --------- | --------- | ------- | ------- | ----- | --- | --------- | --------- | ------ | -------- | -------------- | ---- |
|         |                |         |     |           |           |         |         |       |     | Q Overall |           | median | min      |                | (15) |
| Singh   | et al.[69]     | propose | a   | bitstream | model     | for QoE | pre-    |       |     |           |           |        |          |                |      |
| diction | by considering |         | QP  | and       | frequency | (R ),   | average |       | α   | β         |           |        |          |                |      |
|         |                |         |     |           |           | N       |         | where |     | and are   | constants | (0.68  | and 0.33 | respectively), |      |
(R )andmaximumduration(R
AVG MAX )ofrebufferingevents. and Q and Q are the median and minimum of the
|     |     |     |     |     |     |     |     |     | median | min |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Considering H.264/AVC as the encoder, for QP estimation, average quality. The instantaneous quality is obtained from
theauthorsusetheaverageofQPvaluesoverallmacroblocks
|     |     |     |     |     |     |     |     | QP  | values | using the | normalized |     | quality | vs. inverted | nor- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ---------- | --- | ------- | ------------ | ---- |
in all video frames. The playout interruptions are modeled malized quantization stepsize (NQQ) model in[88]. Based
| as a function |     | of R | , R | and R | using | the cumulative |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---- | --- | ----- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
N AVG MAX on this work, the authors also observe that the qualities of
distributionfunction,F(x),ofthedelayas:
|     |     |     |     |     |     |     |     | the | composing | frequency |     | components | of a | non-periodic | QP  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ---------- | ---- | ------------ | --- |
 αx varying video session can be used to estimate the overall
|     |      | ,   |     |     | ≤     |       |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |  |     |     |     | i f x | R AVG |     |     |     |     |     |     |     |     |     |
R q u a l it y o f t h e v id eo . A m o n g a l l t h e se fr eq u e n c y c o m p o n e n t s
|     | A   | VG  | x−R |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
F(x)= AVG ∈(cid:2) (cid:3) (o f t h e i n st a n ta n eo u s qu a li ti es ) , t h e o ne w it h t h e w o r st q u a l it y
|     | ( 1 | − α ) |     | ,   | i f x | R ,R |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | R     | −R  |     |       | AVG  | MAX |     |     |     |     |     |     |     |     |
1, MAX AVG has th eh i g h e s t i m p a c t o n th e fi n al q u a lit y .
otherwise Tr an e t a l . [ 7 2 ] p r e s e nt a Q o E e s t im a t ion model consid-
|     |     |     |     |     |     |     |     | ering | encoded | video | quality | and | quality | variation | as the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ----- | ------- | --- | ------- | --------- | ------ |
(14)
|        |     |      |      |      |     |               |     | IFs. | The quality | of  | the encoded | video | is calculated |     | for each |
| ------ | --- | ---- | ---- | ---- | --- | ------------- | --- | ---- | ----------- | --- | ----------- | ----- | ------------- | --- | -------- |
| whereα | =1− | RAVG | andR | andR |     | aremaximumand |     |      |             |     |             |       |               |     |          |
RMAX MAX AVG segment considering the average QP which is then used to
averagevaluesoftheindividualrebufferingeventsduringthe model the effect of encoding quality and quality variation
videoplayback.Pesudo-randomvaluesdistributeduniformly
usingthehistogramofbinsofsegmentqualitiesandsegment
on[0,1]andtheinversefunctionofF(x)areusedtoobtain
|             |     |              |          |     |        |          |       | quality | gradients | respectively. |     | The | overall | session quality | is  |
| ----------- | --- | ------------ | -------- | --- | ------ | -------- | ----- | ------- | --------- | ------------- | --- | --- | ------- | --------------- | --- |
| the playout |     | interruption | duration |     | values | based on | which |         |           |               |     |     |         |                 |     |
modeledas:
| pauses | of that | duration | are | then inserted |     | in the videos. | The |     |     |     |     |     |     |     |     |
| ------ | ------- | -------- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |         |          |     |               |     |                |     |     |     |     | NSQ |     | 1   |     |     |
authorsobservethatcomparedtovideoqualityduetohigher (cid:88) (cid:88)
|     |     |     |     |     |     |     |     |     | Q   | =   | α   | F + | β   | F   | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
QPvalues,usersaremoresensitivetorebufferingeventswith Overall n Qn m (cid:96)Qm
|        |         |      |        |      |          | R      |         |     |     |     | n=1 | m=−M |     |     |     |
| ------ | ------- | ---- | ------ | ---- | -------- | ------ | ------- | --- | --- | --- | --- | ---- | --- | --- | --- |
| higher | rate of | drop | of QoE | with | increase | in MAX | , which |     |     |     |     |      |     |     |     |
|        |         |      |        |      |          |        |         |     | α   | β   |     |      |     |     |     |
saturatesafteracertainvalue(6-8seconds).Incontrast,initial where and are model parameters, N (= 5 in this
|     |     |     |     |     |     |     |     |     | n   | m   |     |     |     | SQ  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
increaseinQPresultsinslowerQoEdegradationwithrapid work), F and F are number of segment quality bins,
|     |     |     |     |     |     |     |     |     | Qn  | (cid:96)Qm |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
fall in QoE at higher QP values. The 3-layer RNN model frequency of segment quality bins and frequency of quality
is validated using RMSE using subjective test scores. Since gradientbinrespectively.Segmentqualitybinsrepresentthe
themodelusesbitstreamlevelinformation,themodelsuffers encoded video quality while quality gradient bins represent
frominherentdrawbacksofbitstreammodelssuchaslimited quality variations. Model parameter estimation and valida-
scopeofapplicationsandalsolimitedapplicabilitytosingle tion are done using subjective assessment for three videos
codec. The proposed model was evaluated using only four of 74 seconds consisting of 2-second length segments and
contenttypesofshortduration(16secs). ninequalitylevels.Acomparisonwithpreviouslydiscussed
Xue et al.[70] propose a QoE model which com- models[71] and[75] for the given dataset shows a superior
bines instantaneous qualities and cumulative quality taking performance of the proposed model in terms of PLCC and
into account video segment quality, quality switching and Root Mean Square Error (RMSE). As in[78], the authors
rebuffering events. The instantaneous perceptual quality is conclude that the effect of quality up-switching has a neg-
evaluatedusingalinearmodelusingQPvalues,andinstan- ligibleimpactontheoverallQoEcomparedtothatofquality
taneous rebuffering related degradation is modeled as the down-switching.IFssuchasrebufferingevents,initialload-
opposite of the weighted intensity of the interrupted frame. ingdelayandqualityswitchingofstartingqualityvaluesare
Initial loading delay related degradation is assumed to be nottakenintoaccountintheirmodel.Theauthorsalsoassume
constant and is modeled using the initial QP value which that various representations are of the same resolution and
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 30843 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
frame-rate which is the case in many popular HAS applica- 4) HYBRIDMODELS
tionswhichusemulti-resolutionvideorepresentationintheir Vriendt et al.[75] propose the following relationship for
applications. MOSprediction
An extension of the previous model[72] is presented
in[73],wheretheauthors,inadditiontoqualitydegradation M pred =αµ−βσ −γR QS +δ (19)
due to encoding and quality switching, also consider the
where α,β,γ and δ are tunable parameters, and µ,σ and
effect of different initial quality, initial loading delay and
R represent the average of the quality of the chunks,
rebuffering related impairments. The overall QoE is esti- QS
the standard deviation of quality information and frequency
matedas:
of switches respectively. Depending on how the parameter
QoE =I −I −I (17) valuesareestimated,equation(19)canbeusedtoobtainfour
Overall QS RB ILD
different models (bitrate, objective quality (PSNR/SSIM),
where I QS is the impairment factor due to varying quality chunk-MOSandqualitylevel).Thechunk-MOSmodeluses
modeled using the switching amplitude and the initial qual- MOSvaluesassociatedwitheachqualitylevelwhichcanbe
ity value, I RB is the impairment factor due to rebuffering estimatedduringtheparametertuningprocess,asisdonefor
duration, and I ILD is the impairment factor due to initial otherparameters,orcanbeassumedtobeuniformlyspaced
delaymodeledusingalogarithmicfunction.Theauthorsfind betweenamaximumandminimumvalue(whichisequivalent
that the impact of switching amplitude depends not only tothequalitylevelmodel).Theparameterestimationisper-
on switching amplitude but also on the starting quality. For formedbasedonRMSEvaluesusingsubjectiveMOSscores.
example,forequalswitchingamplitude,down-switchingina BasedontheresultsobtainedintermsofRMSE,PLCCand
low-qualityregionisworsethandown-switchinginthehigher SROCCvaluesconsideringmobilephoneandtabletdevices,
qualityregion.Also,rebufferingdurationof0.25secondsor the general chunk-MOS model was found to perform better
less have a negligible effect on the final QoE value, while than others. As discussed by the authors, the results are
rebuffering durations of more than 2 seconds can lead to limitedtoasinglecontenttypeandaparticularratedecision
extremeQoEdegradation. algorithm.
Robitza et al.[74] describe another candidate model for Chenetal.[76]modeltheTimeVaryingSubjectiveQual-
ITU-T Rec P.1203 competition. It follows a similar mod- ity (TVSQ) of HAS rate-adaptive video streams using a
ular approach where the pooled audiovisual per second Hammerstein-Wiener (H-W) model with input and output
scores,representingthemediaquality(Q LT )anddegradation functionsas:
due to initial loading delay (I ) and rebuffering events
ILD 1
(I RB ), are combined to obtain the final Audiovisual MOS u[t]=β 3 +β 4 1+exp(−(β qst[t]+β )) (20)
(MOSAVFinal)valueas: 1 2
and
MOSAVFinal =Q −(I +I ). (18)
LT ILD RB
1
q[t]=γ +γ (21)
The model considers quality variations over time, recency (cid:98) 3 4 1+exp(−(γ v[t]+γ ))
1 2
effect,lengthandlocationofrebufferingeventsandencoding
whereqisthepredictedTVSQ,β andγ aremodelparame-
quality and is designed for sequences up to 5 minutes in (cid:98)
ters,qst istheShortTermSubjectiveQuality(STSQ)andv[t]
length. The authors use simple averaging of the per-second
istheoutputofthelinearfilteroftheform
scores into the final session quality score as other temporal
pooling methods did not seem to provide increased perfor- v[t]=bT(cid:0) u (cid:1) +fT(cid:0) v (cid:1) (22)
t−r:t t−r:t−1(cid:48)
mancegains.Asimilarobservationwasalsoreportedin[18].
Whiletheauthorsclaimthemodeltobevideooraudiocodec where b = (b ,...b )T and f = (f ,...f )T are
0 r 0 r
agnostic, the performance results for the proposed model is model parameters. Temporal distortions such as mosquito
reported only for the mode using full bitstream information effects,jerkiness,etc.,arecapturedusingVideo-RREDSTSQ
(Mode 3), hence leaving an open question about its per- predictor[89]. The proposed model, while achieving good
formance for other modes (Mode 0, Mode 1 and Mode 2). performanceandprovidingvaluableinsightsintotheTVSQ
Parameter selection based on the manual count of quality optimization problem, does not take into account playback
changes and exhaustive brute-force optimization procedure, interruptions such as rebuffering, which limits the model
as used by the authors, may lead to an over-fitting of the application for more realistic cases. Also, the H-W model
model parameters for the given test conditions and hence implementation as used by the authors is not suitable for
the performance of the same for other datasets can help in videosofdifferentdurations[82].
the evaluation ofthe actual performance gains of themodel Shen et al.[77] present a QoE model which takes into
forpossiblereal-worldapplications.Also,themodelperfor- account segment quality, primacy and recency effects and
mance was only evaluated on PC/TV databases and its per- qualityswitching(usingbitratedistribution)asIFs.Eachseg-
formance for mobile video streaming scenario still remains mentofthevideoisassumedtobeofConstantBitrate(CBR)
anopenquestion. andtherespectiveencodedvideoqualityofeachsegmentis
30844 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
calculatedas: events, total rebuffering duration, and video motion content
ofthevideo.Qualityswitchingrelatedimpairmentsaremod-
BR
|     |     | Q   | =γ  |     |     | (23) |                                                  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | Seg | +δ  |     |      | eledusingtheVQM[19]metricbytakingintoaccountboth |     |     |     |     |     |     |     |
MV
encodingrelatedimpairmentsandimpairmentsduetoquality
| where BR | is the | bitrate, | γ,  | δ are constants, |     | and MV is the |     |     |     |     |     |     |     |     |
| -------- | ------ | -------- | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
switching.Basedontheirtests,theauthorsobservethat,fora
motionparametercalculatedas:
fixednumberofrebufferingevents,theimpairmentincreases
|     |     | N   |     |     |     |     | monotonically |     | with the | rebuffering |     | duration, | while | for a |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ----------- | --- | --------- | ----- | ----- |
1 (cid:88)
| MV = |     | std | |y(f,w,h)−y(f |     | −1,w,h)| | (24) |     |     |     |     |     |     |     |     |
| ---- | --- | --- | ------------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
−1 space fixed rebuffering duration, the impairment due to rebuffer-
N
|          |     | f=2 |     |     |     |       | ingfrequencydoesnotincreasemonotonically.Also,higher |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | ----- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| y(f,w,h) |     |     |     |     |     | (w,h) |                                                      |     |     |     |     |     |     |     |
where is the pixel value at position of the frequency of rebuffering leads to higher impairment. While
f −thframe.Theprimacyandrecencyeffectsaremodeled the model was designed and evaluated using 1-minute long
|     |     |     |     |     |     |     | video sequences, |     | a preliminary |     | investigation |     | by the | authors |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------- | --- | ------------- | --- | ------ | ------- |
as:
α β shows that it performs quite well for video sequences of up
|       |        | P   |        | R    | ,   |         |                      |     |     |     |     |     |     |     |
| ----- | ------ | --- | ------ | ---- | --- | ------- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| f(t)= |        |     | +      |      | 0≤t | ≤T (25) | to10minutesduration. |     |     |     |     |     |     |     |
|       | 1+α2t2 |     | 1+β2(t | −T)2 |     |         |                      |     |     |     |     |     |     |     |
|       |        | P   |        | R    |     |         |                      |     |     |     |     |     |     |     |
Garciaetal.[79]presentaninterestingmodularapproach
| α   |     | β   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where P and R correspond to the effect of primacy and of pooling short-term quality models for long-term quality
recencyrespectively.TheoveralladaptivestreamingQoEis estimationwhichthenarecombinedwithrebufferingrelated
givenby:
informationtoobtaintheoverallmediasessionquality.Such
|     |     |     |     | −→−→ |     |      | amodularapproachleavesouttheinterdependencies,leading |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ---- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Q   | =I  | S WT |     | (26) |                                                       |     |     |     |     |     |     |     |
Overall QS easierintegrationanddevelopment.Theproposedmodelcan
−→
where I represents the impact of quality switching, S besummarizedas:
QS
is a vector consisting of the QoE of each segment as esti- Q=Q −I (29)
|                   |     |     | −→                               |     |     |     |         |       |          | LT         | RB  |            |             |     |
| ----------------- | --- | --- | -------------------------------- | --- | --- | --- | ------- | ----- | -------- | ---------- | --- | ---------- | ----------- | --- |
| matedusing(23)and |     |     | W istheweightvectorfortakinginto |     |     |     |         |       |          |            |     |            |             |     |
|                   |     |     |                                  |     |     |     | where Q | LT is | obtained | by pooling |     | short-term | audiovisual |     |
considerationmemoryrelatedfactors(primacyandrecency)
|     |     |     |     |     |     |     | quality | scores | and I | is the | quality | degradation |     | due to |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----- | ------ | ------- | ----------- | --- | ------ |
using (25). The authors observe that at a particular aver- RB
|              |                |        |           |          |              |              | rebuffering.                           | Six  | different | models | are  | used     | to estimate     | the      |
| ------------ | -------------- | ------ | --------- | -------- | ------------ | ------------ | -------------------------------------- | ---- | --------- | ------ | ---- | -------- | --------------- | -------- |
| age bitrate, | down-switching |        |           | achieves | higher       | QoE than up- |                                        |      |           |        |      |          |                 |          |
|              |                |        |           |          |              |              | short-termaudiovisualqualityscores:VQM |      |           |        |      |          | AV isthegeneral |          |
| switching.   | Also,          | video  | sequences | with     | high startup | and end      |                                        |      |           |        |      |          |                 |          |
|              |                |        |           |          |              |              | VQM model,                             | PSNR |           | is the | PSNR | averaged | per             | segment, |
| quality      | receive        | higher | ratings   | due to   | primacy      | and recency  |                                        |      | AV        |        |      |          |                 |          |
DT0istheframe-basedmodelbasedonITU-TRecseries[8],
| effect, with | the | primacy | effect | decreasing | for | long video |         |     |              |     |     |           |     |            |
| ------------ | --- | ------- | ------ | ---------- | --- | ---------- | ------- | --- | ------------ | --- | --- | --------- | --- | ---------- |
|              |     |         |        |            |     |            | DT1 and | DT2 | are variants | of  | DT0 | and Dummy |     | is 5-point |
sequences.BitratedistributionisfoundtobethemajorIF.The
scalequalitylevels.degStaliscalculatedasdefinedinITU-T
modelwasevaluatedusingonlyasinglecontenttypeandalso
|     |     |     |     |     |     |     | Rec series[90]. |     | Irrespective |     | of the | pooling | method | used, |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | ------ | ------- | ------ | ----- |
limitedtothetestconditionswithdifferentaveragebitrates.
theperformanceofshort-termqualitymodelsisfoundtobe
Hencetheperformanceofthemodelforreal-worldapplica-
agoodrepresentativeofthelong-termqualitymodelperfor-
| tions remains |     | an open | question, | mainly | because | the model |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --------- | ------ | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
mance.Itisobservedthatthebestshort-termqualitymodels
doesnottakeintoaccountrebufferingrelatedimpairments.
alsoperformbestforlong-termmodels,withDT2resulting
Liuetal.[78]proposeano-referenceQoEmodelconsider-
inthebestperformanceintermsofRMSEvalues.
ingbothtemporalandspatialqualityandtakingintoaccount
|          |            |        |             |     |             |            | Duanmu    | et al.[80] |       | present | a QoE       | model | (referred | to as    |
| -------- | ---------- | ------ | ----------- | --- | ----------- | ---------- | --------- | ---------- | ----- | ------- | ----------- | ----- | --------- | -------- |
| IFs such | as initial | delay, | rebuffering |     | and quality | switching. |           |            |       |         |             |       |           |          |
|          |            |        |             |     |             |            | Streaming | Quality    | Index | (SQI))  | considering |       | the       | combined |
TheproposedoverallQoEmodelisadaptedfromtheITU-T
effectofinitialloadingdelay,rebufferingandencodingqual-
E-model[48]as:
|      |     |                |     |                  |     |      | ity. The                                            | overall | quality       | is computed |                 | from         | the instantaneous |           |
| ---- | --- | -------------- | --- | ---------------- | --- | ---- | --------------------------------------------------- | ------- | ------------- | ----------- | --------------- | ------------ | ----------------- | --------- |
| −MOS |     | =1+0.035R+7×10 |     | −6R(R−60)(100−R) |     |      |                                                     |         |               |             |                 |              |                   |           |
| DASH |     |                |     |                  |     |      | qualityinamovingaveragefashionwheretheinstantaneous |         |               |             |                 |              |                   |           |
|      |     |                |     |                  |     |      | quality                                             | at each | time unit,    | Q           | , is considered |              | to be             | a linear  |
|      |     |                |     |                  |     | (27) |                                                     |         |               |             | n               |              |                   |           |
|      |     |                |     |                  |     |      | combination                                         | of      | instantaneous |             | video           | presentation |                   | quality P |
n
whereRisestimatedbasedonimpairmentduetoinitialdelay
|     |     |     |     |     |     |     | estimated | at theserver |     | side by | frame-level |     | VQAmodeland |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------- | ----------- | --- | ----------- | --- |
(I ILD ),stalling(I RB )andqualityswitching(I QS )as: impactofrebufferingatindividualframesS as:
n
| R = 100−I |     | −I  | −I          |     |               |           |     |     |     | =P  | +S  | .   |     |      |
| --------- | --- | --- | ----------- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|           | ILD | RB  | QS          |     |               |           |     |     |     | Q n | n n |     |     | (30) |
|           |     | +αI | (cid:112) I | +I  | +β(cid:112) I | ∗I . (28) |     |     |     |     |     |     |     |      |
ILD RB QS RB QS Basedontheassumptionthateachrebufferingeventisaddi-
tiveandindependent,theauthorsmodelthememorydecline
| Here α   | and β | are estimated  |     | using subjective |                | assessment (as |           |           |     |                |     |        |     |         |
| -------- | ----- | -------------- | --- | ---------------- | -------------- | -------------- | --------- | --------- | --- | -------------- | --- | ------ | --- | ------- |
|          |       |                |     |                  |                |                | of memory | retention | due | to rebuffering |     | (based | on  | Hermann |
| 0.15 and | 0.82  | respectively). |     | Based on         | the subjective | assess-        |           |           |     |                |     |        |     |         |
Ebbinghausforgettingcurve[91])as:
| ment, the  | authors | find   | that the  | initial    | loading | delay related  |     |     |     |        |     |     |     |      |
| ---------- | ------- | ------ | --------- | ---------- | ------- | -------------- | --- | --- | --- | ------ | --- | --- | --- | ---- |
| impairment | is      | linear | and hence | is modeled |         | using a linear |     |     |     |        | t   |     |     |      |
|            |         |        |           |            |         |                |     |     | M   | =exp(− |     | )   |     | (31) |
T
| equation. | Impairments |     | due to | rebuffering, | which | are more |     |     |     |     | M   |     |     |     |
| --------- | ----------- | --- | ------ | ------------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
complicatedtoestimateandhavemoredependentvariables, whereM,t andT representmemoryretention,thecurrent
M
aremodeledusingacombinationofanumberofrebuffering time instant and relative strength of memory respectively,
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     |     | 30845 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
whicharethenusedinapiecewisemodeltogetthecollective models discussed here (e.g.,[67],[74]). In terms of content
effect of rebuffering on QoE degradation. The authors find independence, MS-SSIM using ET was found to perform
thatforagivenrebufferingeventatthesametemporalloca- the best in terms of SROCC while STRRED using SVR
tionandofthesameduration,theQoEisinverselyrelatedto performedbestintermsofPLCC.Basedontheresults,itis
the quality of the frame at that same temporal instant. The observedthatthevideoqualitymodelusedfortheprediction
overall QoE value is calculated as the average of the pre- ofcompressedvideoqualityplaysaveryimportantroleinthe
dicted individual QoE scores. An evaluation of the existing QoEpredictionquality.Also,rebufferingdurationisshownto
models(PSNR,SSIM,MS-SSIM,SSIMplus[92],FTW[93], haveasmalleffectwithapossibleexplanationoftheduration
Mok et al.[60], VsQM[62] and Xue et al.[70]) and the neglect effect[99]. Using STRRED as the objective video
proposedSQIusingPSNR,SSIM,SSIMplus,MS-SSIMon qualitymetric,itwasobservedthatforvariouscombinations
the designed database shows that the proposed SQI model, of IFs considered in this study, linear regressors Ridge and
whenusedwithSSIMplusastheVQAmodel,hasthehighest LassoperformedbestintermsofSROCCandPLCC.Interms
performance,withotherSQImodels(SQIwithPSNR,SSIM of prediction monotonicity (median SROCC) and perfor-
and MS-SSIM as VQA) performing better than the other mance(medianPLCC),foradifferentamountoftraining-test
compared models. The presented model is a big step for- datasplit,MS-SSIMperformedthebest(consideringETas
wardtowardsQoEmodelingconsideringbothencodedvideo the learning algorithm). Compared to other models (FTW,
quality and rebuffering related information with reasonable VsQM, PSNR, SSIM, MS-SSIM and SQI), the proposed
performance on the given dataset. Given that the database modelisshowntohavesuperiorperformancewhenusingthe
andIFsconsideredinthisworkaresomewhatlimiteddueto SSIMandMS-SSIMforallregressionmodels.
the short duration of the sequences (only 10 second videos, Similar to their previous work, in[82], Bampis et al.
fixed duration rebuffering events and just two rebuffering present a machine learning based Nonlinear Autoregressive
events at fixed location (start and middle)) which is not NetworkwithExogenousInputs(NARX)modelwhichuses
realistic, the performance of the model on more practical objective metrics for video quality prediction, rebuffering
datasetsremainsanopenquestion.Wewilldiscusslaterhow related information and memory related features for QoE
themodel,whenevaluatedbyotherauthors,doesnotresult prediction.NARXisanolinear-autoregressivemodelwhich
in high performance. The authors publicly released one of assumes a non linear relationship between its output and
the first subjective databases for HAS application scenarios inputs (delayed versions of its output, y t−1 , y t−2 and so
whichconsidersrebuffering. on which helps in modeling the memory effect) along with
BampisandBovik[81]proposeamachinelearning-based exogenousinputsgivenbythevector,u (e.g.,videoencod-
t
framework,VideoATLAS,whichcombinesQoErelatedfea- ing quality, rebuffering information) which can be defined
tures such as objective quality metrics, rebuffering related approximatelyas:
factorsandmemory-relatedfunctionstopredicttheenduser
QoE. Simple regressors combined with main IFs such as y t =F(y t−1 ,y t−2 ,y t−3 ,...,u t ,u t−1 ,u t−1 ,...). (32)
video quality, rebuffering and memory-related effects are As discussed by the authors, the usage of such autoregres-
foundtoprovidegoodresults.Thevideoqualityisevaluated sivemodelsforreal-timeQoEpredictionmayresultinerro-
usingwell-knownimageandvideoqualitymetricsandother neous QoE prediction results due to prediction error propa-
IFs, such as length of each rebuffering event normalized to gation/amplification(asthepredictionscoresarefedbackto
thedurationofeachvideo,thenumberofrebufferingevents, thepredictionengine).Theproposedmodelistrainedusing
number of seconds with normal playback at the maximum the Levenberg-Marquardt algorithm, and QoE prediction is
possible bitrate until the end of the video and time per performedonacontinuoustimescaleandhencecanbeused
videooverwhichabitratedroptookplace,bothnormalized forcontinuousQoEmonitoringsolutions.Basedonthemodel
to the duration of individual video. The calculated features evaluation on LIVE-NFLX database, it is observed that the
are then combined using various learning-based algorithms model performance varies across different playout patterns
(Support Vector Regression (SVR), Random Forest (RF), whichpointtowardstheinstabilityofthemodel.Considering
Gradient Boosting (GB), Extra Trees (ET) and Ridge and only objective VQA metrics, STRRED results in the best
Lasso regression[94]) to provide a single final overall performance compared to PSNR, SSIM, MS-SSIM, NIQE
QoE score. The authors evaluate 6 objective IQA metrics and VMAF while, if rebuffering and memory effects are
(PSNR, PSNRHVS[95], SSIM, MS-SSIM[96], NIQE[43] taken into account, both SSIM and STRRED give the best
and GMSD[97]) and two VQA metrics (VMAF[98] and prediction results. When compared to the earlier proposed
STRRED[89]) on the subjective dataset and it is observed continuousQoEpredictionmodelbyChenetal.[76],consid-
that STRRED gives the highest performance in terms of ering only bitrate related impaired sequences, the proposed
SROCC considering both a subset of the database with no model is shown to have better RMSE and outage rate but
rebufferingandconsideringthewholedataset.Basedonthis worsedynamictimewarping(DTW)[100]distance.Apos-
observationtheauthorsconcludethatIFssuchasrebuffering sibleextensionoftheproposedmodelcanbetoevaluateits
and bitrate changes should be considered jointly and not performance for retrospective QoE prediction using various
separately which contradicts the approach of many other temporalpoolingstrategies.
30846 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
Bampis and Bovik present another model in[83] which degradation due to encoding and rebuffering are mutually
builds upon the previous two models[81],[82] addressing exclusive, the model is divided into two parts: QoE during
one of the significant shortcomings of the two earlier dis- regularplaybackandQoEduringtherebuffering.Theauthors
cussedcontinuous-timequalitypredictionmodels[76],[82]: employSVRforQoEestimationofthevideoduringnormal
instability. The authors propose a new model based on an playback which is trained using Reduced Reference (RR)
augmented NARX approach for continuous QoE prediction metric STRRED[89] and previous time instant QoE value.
taking into account degradation due to compression and The QoE degradation due to rebuffering is modeled using
rate adaptation. In contrast to the previous models where a theIQXhypothesis(exponentialInterdependencyofQoSand
single objective quality metric was used for encoded video QoE[102])as:
quality estimation, here multiple VQA metric outputs are Q(t)=e −λ Q(t −1) (33)
used as inputs for quality prediction which results in supe-
rior performance in comparison to[82]. It is observed that where λ depends on the QoE value just before the onset of
whenVQAmodelsareusedtogether,thepredictionquality rebufferingandQoEvalueattheendofrebuffering.Thepro-
improvessignificantly.Thisisbasedontheobservationthat posed model is designed and validated using well designed
while a single VQA metric alone may not be designed to subjectiveassessment.Atotalof18uncompressedreference
take into account all types of quality impairments, multiple videos covering a wide range of genres and 36 distorted
VQA metrics collectively can better model the distortions, videos are used in the subjective assessment. Based on the
which results in significant increase in prediction accuracy. results of the model performance in terms of PLCC of the
The model performance evaluation is done using the same recencyeffectonoverallQoE,theauthorsconcludethatboth
databaseasusedbyChenetal.[76].Whiletheperformance instantaneousQoEandoverallQoEvaluesdependtoagreat
for the proposed NARX model with multiple VQA inputs extentonthemostrecentexperienceoftheuser.Oneofthe
is quite promising, the model complexity is quite high and significantadvantagesoftheproposedmodelisthat,among
is not suitable for practical applications as it does not take allreviewedworks,thisistheonlyonewhichconsidersUHD
into account QoE degradation due to rebuffering. Model videos.Also,thisisoneofthefirstpubliclyavailabledatabase
performance evaluation and possible enhancements taking consistingofFHDandUHDvideosequenceswhichjointly
into account rebuffering related impairments could be an considers both quality switching and rebuffering distortion
impressivefuturework. on a continuous time scale. While the authors used learn-
All the three models discussed above[81]–[83] are ing based QoE estimation using Video-RRED for standard
designedandevaluatedusingthepartlypublicLIVE-NFLX videoplaybackqualityandexponentialmodelbasedonIQX
database[101]. The LIVE-NFLX database consists of hypothesis for QoE during rebuffering state, they acknowl-
14source videos at FHD resolution encoded using edgethattheredoesnotexistanyparticularreasonfortheir
H.264 using 8 different playout patterns (constant encoding selection which can easily be replaced by other VQA and
at250and500kbps,adaptiveratedropsat66and100kbps, learning algorithm and parametric model respectively. The
two patterns of constant encoding with one rebuffering performanceofsuchmodelindeedwillneedtobeevaluated
event,constantencodingwithtworebufferingeventsandone on the given dataset which can be an exciting future work.
with adaptive rate drops with rebuffering) rated by 56 test Someofthelimitationsofthisworkincludeusageoflimited
subjects. For a more detailed description of the database, test conditions such as only two quality switching patterns,
we refer the reader to the related publication[101]. One whichleavesanopenquestionabouttheperformanceofthe
of the major shortcomings of the previous three models is modelinreal-worldscenarios.
that they are all evaluated using the same database which Ghadiyaram et al.[85] build upon the work of
is designed for low-bitrate applications (considering videos Chen et al. in[76] and their previous work in[103] which
of max 250 kbps bitrate and min 100 kbps) such as video usestheHammerstein-Wiener(H-W)modelforQoEmodel-
streamingovermobilenetworksandhencetheperformance ingasdiscussedpreviouslyinthediscussionoftheworkof
efficiencyandapplicabilityofsuchmodelsforlargerdisplays Chenetal.[76].Inadditiontotherebufferingrelatedimpair-
andhigherbitrateapplications(PC/TV)usingnetworkswith ments(seeTable2),client-sidebuffermodel,scenecriticality
higherthroughputremainsanopenquestion.Also,itcanbe andperceptualqualityIFsarefirstmodeledmathematically.
observedthatthenumberofstallpatternsandrateadaptation Each of these mathematical models is then used to train a
conditions are quite limited and fixed. Also, in the absence SingleInputSingleOutput(SISO)H-Wmodelwithmemory,
of the full database (only three out of total 14 source and thuscapturingthehysteresiseffectsandnon-linearityofthe
respectiveHRCsaremadepublic),acomparativestudyand human behaviour. Depending on the methodology used to
furthermodelimprovementremainchallenging. combinetheindividualH-Wmodeloutputs,twovariantsof
Eswara et al.[84] present a QoE evaluation framework thecontinuous-timeQoEpredictionmodelareproposed.The
and a model for continuous time QoE prediction taking first continuous model, TV-QoE2 uses the model outputs
intoaccountrebufferingfrequency(perminute),rebuffering of the individual H-W model as input to train a Multiple
duration (in seconds), memory effects (recency) and objec- InputSingleOutput(MISO)Wienermodel(avariantofthe
tive video quality metric. Based on the premise that quality Hammerstein-Wiener model without an input non-linearity
VOLUME7,2019 30847

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
block).ThesecondvariantofthecontinuousQoEprediction Section VIII for more details about the databases). Model
model, TV-QoE1, uses SVR instead of the Wiener model. designandevaluationoverthefourpubliclyavailabledatasets
The various model parameters are estimated using training and performance comparison against different state-of-the-
data. In addition to the continuous QoE model, an overall art continuous quality prediction models[82],[84],[103]
QoEmodelisalsoproposedwhichtakesintoaccountnumber, demonstratesasuperiorperformanceoftheproposedmodel.
totalduration,frequencyandrateofrebufferingeventsalong The authors also report that mean and media QoE score
with time since the last rebuffering event and perceptual obtained by pooling the continuous QoE scores correlates
quality score. The proposed model is modular in nature wellwiththereportedoverallQoEscores.
as additional/existing inputs can be added/removed without Duanmuetal.[87]investigateanovelapproachwherethey
changes to the model structure. Also, the model is found to consider an Expectation Confirmation Theory (ECT) based
be computationally efficient for both training and real-time model design to predict the end-user QoE. The proposed
calculations.BothcontinuousQoEpredictionmodelandthe model primarily takes into account the effect of adaptation
overallQoEpredictionmodelaretrainedandevaluatedusing intensity, adaptation type, intrinsic quality and content type
threedifferentpubliclyavailableQoEdatabases([80],[101], IFs on the end user QoE. For a methodological study and
[103],seeTable5).Intermsofthemedianoftheper-frame investigationintotheeffectofqualityadaptations(compres-
correlation and RMSE between actual and predicted QoE sion, spatial and temporal) on end user QoE they designed
score on a continuous time scale, the proposed model is a new and now publicly available dataset which is then
found to outperform the SQI model in[80]. Also among used for model design and evaluation (see Waterloo QoE
the two proposed continuous-time QoE models, TV-QoE- Database (ECT) in Section VIII for more details on the
2 performs slightly better than TV-QoE-1. In general the dataset).Thepost-hocqualityofthenthsegmentQnisdefined
p
globalQoEmodelprovidingtheoverallestimationofquality, as a function of intrinsic spatial quality (QS) and intrinsic
i
while in terms of correlation and RMSE values is found temporalquality(QT)featurerepresentationas:
i
to perform quite well on all the three databases, fails to
Q (n) = f(QS(n)−QS(n−1),QS(n),QT(n)
provide superior performance when compared to SQI[80] Seg i i i i
andVideoATLAS[81]models.Alsointheabsenceoftaking −QT(n−1),QT(n)). (36)
i i
intoaccountqualityswitchingasanIF,theperformanceofthe
The authors observe that the average pooling of the
modelonreal-worldusecasesremainsanopenquestion.
segment-levelpost-hocqualityscorescorrelatewellwiththe
Eswara et al.[86] propose a recurrent neural network
overallQoEscoresandhencetheoverallQoEisgivenby:
(Long Short-Term Memory (LSTM) network) based QoE
prediction model, LSTM-QoE, to predict the time vary-
(cid:88)
Ns
ing QoE. The authors argue that the continuous QoE is a QoE Overall = Q Seg (n) (37)
nonlinear stochastic process which exhibits non-Markovian n=1
temporal dynamics due to the hysteresis effect which can whereN isthetotalnumberofvideosegments.Acompari-
s
be modeled using a network of multi-layered, multi-unit sonofthemodelperformancewithotherstate-of-the-artQoE
LSTMs. The predicted instantaneous QoE, Q(t) is mod- models such as[9],[76],[78] etc. indicates superior perfor-
eledas: manceoftheproposedECT-QoEmodelonthesubjectivetest
dataset.WhiletheinvestigationandpossibleuseofECTfor
Q(t)=LSTMo (x(t),c(t −1)) (34)
l,d QoE prediction with promising results are quite impressive,
where x(t) is the input feature vector, c(t) represent the set the current work is limited in that the dataset used for its
of LSTM cell states in the network, l and d are the number evaluationconsistedofvideosofonly8secondsdurationand
of LSTM layers and number of LSTM units respectively. one quality adaptation and some important factors (such as
LSTM l,d provides two functionalities: LSTM l o ,d for output rebufferingevents)arenotconsidered.Futureassessmenton
QoE prediction and LSTMc for cell state update which is amoreexhaustivedatasetconsideringmorerealisticstream-
l,d
definedas: ingscenarioscanhelpbetterunderstandtheapplicabilityof
suchmodelforQoEevaluation.
c(t)=LSTMc (c(1:t −1),Q(1:t −1)), ∀t >1. (35)
l,d As briefly mentioned earlier, towards building a model
ThreeIFsareconsideredforQoEprediction:STSQ,current for adaptive audiovisual streaming services, ITU-T Rec.
playbackstatusandtotaltimesincethelastrebufferingevent. P.1203,alsoknownasP.NATSwasapprovedandfinalizedin
STSQ, which takes into account the perceptual quality of a Nov.2016[9].TheITU-TRec.P.1203seriesdescribesmodel
video segment, is calculated using traditional VQA metrics algorithms to predict the audiovisual quality of progressive
such as STRRED, NIQE, etc., as was also used in previ- downloadandadaptivestreamingbasedapplicationsconsid-
ously discussed models[82]–[84]. The proposed model is ering reliable transport protocols such as TCP. The model
evaluatedusingfourpubliclyavailableHASdatasets:LIVE proposed in this recommendation series follows a modular
QoE Dataset for HTTP based Video Streaming, LIVE Net- approachwhichconsistsofashort-termaudio-videoquality
flix Video QoE Database, LFOVIA Video QoE Database modelprovidingper-one-secondoutputscoreswhicharethen
and LIVE Mobile Stall Video Database (see Table 5 and integrated along with initial loading delay and rebuffering
30848 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
events IFs, to give an estimate of quality for HAS media wherex ,x ,...,x arethevariousIFs[106].Thereexistlots
1 2 n
sessionbetween10secsto5minutes.Themodelconsistsof ofIFs[10],eachleadingtoincreasedcomplexityofthemodel
three modules, a video module Pv, an audio module Pa and design.
anaudio-visualintegrationmodule,Pq.Theshort-termscores BasedonthelistofmodelsinTable2,wecanobservethat
fromPaandPvareintegratedintothePqmodulealongwith thefocusrecentlyhasshiftedfrominitialparametricmodels
rebufferingrelatedinformation.Dependingontheamountof (whichusuallytriedtomapQoSbasedIFstoQoE)towards
requiredinputinformationtoPvmodule,themodelprovides hybridmodelswhichtakeintoaccountmediasignalsaswell
fourdifferentmodesofoperation:Mode0,Mode1,Mode2 as impairments such as quality switching and rebuffering.
and Mode 3 (in increasing order of complexity). Mode 0 Regarding IFs, we observed that while rebuffering, quality
includes display resolution, frame rate and target and real switchingandencodingrelatedfactorsaretakenintoaccount
bitrate, Mode 1 consists of all of Mode 0 and frame related by most of the models, other IFs such as initial loading
information such as frame type and frame size and Mode 2 delay,recencyandprimacyeffectsanduserengagementare
includes all of Mode 1 and partial bitstream information. considered by only a few of the models. While not all IFs
Mode 3 consists of Mode 1 along with complete bitstream hasasignificantimpactonthefinalQoE,therearestillmany
information. For detailed information about the models and IFswhoseeffectsarenotinvestigatedorhavenotbeentaken
the integration module, we refer the user to the recommen- into consideration for model design. While Moketal.[61]
dation series, P.1203. The recommendation, while indeed found user action such as pause to have a marginal effect
a significant step towards building a QoE model for HAS on QoE, there may exists other user factors, which when
application,initscurrentformsuffersfrommanydrawbacks. considered together, may result in a significant effect on
For example, it assumes a perfect knowledge of buffering the end user QoE. We also observe that with the recent
duration, number of re-buffering events, etc., which is not trend towards the design of hybrid models, the focus has
always practical. The model has been developed and vali- shifted towards additive models where impairments due to
dated using a fixed set of encoding settings using a single variousIFsarecalculatedseparatelyandarethencombined
codec. While adaptive streaming applications such as HAS toobtainthecombinedeffectofalltheimpairmentsasdone
are codec agnostic, the P.NATS model is bitstream-based in[74],[79],[84],amongothers.Suchadditivemodelshave
(exceptformode0),whichmakestheproposedmodel’sper- alsobeenusedinITU-TRec.P.1201(Amd.2)[90]andmore
formancecodecdependent.Sattietal.performedaprelimi- recentlyin[9].Hoßfeldetal.[106]discusshowanadditiveor
naryreal-streamingapplicationanalysisoftheP.1203model amultiplicativemodel,combiningexistingsingle-parameter
forYouTube,Vimeo,AmazonInstantVideoandproprietary QoE models into a multidimensional QoE model, may lead
DASH-basedstreamingframework[104].Theauthorsfound to different results. Hence, such models need to be verified
the overall performance of Mode 0 and Mode 1 to be quite usingindependentsubjectivedatabases.
accurateforH.264codecconfiguration,exceptforthelower Regardingthemodeltype,parametricmodelsarenotthat
qualityrangewherethepredictionswerefoundnottobeso accuratebutareidealforencryptedtrafficmonitoringappli-
precise.Moretestsinreal-worldapplicationsarerequiredto cations. Also, such models can be used at the client-side
better understand the performance of the model and future because of low-complexity. On the other hand, bitstream
development of more accurate and reliable models. A soft- models suffer from the limitation that they are specific to
wareimplementationoftheP.1203ITURechasbeenmade onecodecandhencecannotgeneralizewell,butareusually
publiclyavailablebytheauthorsin[105]whichalsoincludes moreaccuratethanparametricmodels.Usually,hybridmod-
subjective ratings, per condition metadata (bitrates, resolu- els are more precise than parametric, and bitstream models,
tions,initialloadingdelayandrebufferingevents),per-frame butareofhighercomplexityandalsoneedaccesstomedia-
statistics (frame types, sizes) and bitstream level statistics signals,thuslimitingtheirapplicationtoclientorserver-side
(QP values and macroblock types) from four out of the monitoring. Hence depending on the stakeholders involved
total 30 datasets used in the design and validation of the andthedesiredcomplexity,differentmodeltypeneedstobe
recommendation.Duetotheabsenceofthevideosequences developed.
(reference as well as distorted videos), such database is of Also, while most of the models provide only an overall
very limited use for model design and/or validation. For a quality estimation for a media session, some of the models
more exhaustive model, joint work by ITU-T Study Group provide the prediction on a continuous-time scale. Some of
12 and VQEG known as AVHD-AS/P.NATS Phase II is the continuous-time (usually per-sec) models also provide
ongoingwhichaimstowardsbuildingacomprehensivemodel finalsessionqualitywhichisusuallythetemporalaveraging
considering a higher number of codecs (AVC, HEVC and ofcontinuous-timescores.Bothapproacheshavetheiradvan-
VP9), higher frame rate (up to 60 fps), higher resolution tages and disadvantages. Continuous-time models are more
videos(uptoUHD)andawiderrangeofencodingsettings. useful in applications where it is possible to take corrective
actionsbasedontheestimatedinstantaneousquality,suchas
C. SUMMARY
in real-time streaming application where the encoding set-
Onaveryabstractlevel,QoEcanbedescribedas:
tingsandortransmissionparametersmaybeadjustedbased
QoE =f(x ,x ,...,x ) (38) on the estimated QoE of the user. Some continuous-time
1 2 n
VOLUME7,2019 30849

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
predictionQoEmodelscanalsobeusedforrateadaptationin TABLE3. HASmodelsandcorrespondingIFs.
HASapplications,butsuchmodelsareusuallymorecomplex
astheyneedtobecalculatedinreal-time.Ontheotherhand,
| models           | providing | overall | QoE | estimation |        | are more | suited  |     |     |     |     |     |     |
| ---------------- | --------- | ------- | --- | ---------- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- |
| for applications |           | where   | the | prediction | values | can      | be used |     |     |     |     |     |     |
retrospectivelytodesignbettersystems,encodingstrategies,
networkplanningetc.Theyareusuallycomputationallyinex-
| pensive     | as the | parameters |     | gathered  | and        | prediction | values  |     |     |     |     |     |     |
| ----------- | ------ | ---------- | --- | --------- | ---------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
| can usually | be     | gathered   | and | processed | separately |            | and not |     |     |     |     |     |     |
necessarilyattheserver/client/networkside.
VI. DISCUSSIONONTHEIMPACTOF
INFLUENCEFACTORS
InSectionVwepresentedthemodelsalongwiththedescrip-
| tion of | the IFs | considered |     | and how | they | were | taken into |     |     |     |     |     |     |
| ------- | ------- | ---------- | --- | ------- | ---- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
accountinthemodeldesignwhichissummarizedinTable3.
HerewepresentadiscussionoftheIFsandgeneralobserva-
| tions about | their | effect    | on QoE     | as  | described | by the   | models. |     |     |     |     |     |     |
| ----------- | ----- | --------- | ---------- | --- | --------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
| We not      | only  | limit the | discussion |     | to the    | reviewed | models  |     |     |     |     |     |     |
butalsotakeintoaccounttheobservationsreportedbyother
works,soastogetacompleteunderstandingoftheinfluence
| factors | and their | effects. | Here | we  | discuss | the various | IFs |     |     |     |     |     |     |
| ------- | --------- | -------- | ---- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
consideredbythemodelsandtheirrespectiveimportancein
| the QoE   | prediction. |              | Since | the IFs | as considered |           | by models |     |     |     |     |     |     |
| --------- | ----------- | ------------ | ----- | ------- | ------------- | --------- | --------- | --- | --- | --- | --- | --- | --- |
| and their | respective  | observations |       | were    | already       | discussed | in        |     |     |     |     |     |     |
SectionV,herewelimitourdiscussiononlytoeffectsofthe
Whilesomeobservenosignificantaffectofup-switching
IFsandwedonotdescribethemforeachmodelseparately.
|     |     |     |     |     |     |     |     | when compared | to down-switching[72],[77], |     |     |     | others, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------------------- | --- | --- | --- | ------- |
For a more detailed discussion of how the effects of vari- like[108], find that both switching directions have a
| ous IFs | are being | proposed |     | and considered |     | by other | related |     |     |     |     |     |     |
| ------- | --------- | -------- | --- | -------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
considerableimpactonuserQoE.
| works, | we guide | the | reader | to a comprehensive |     |     | survey by |           |                    |      |     |             |       |
| ------ | -------- | --- | ------ | ------------------ | --- | --- | --------- | --------- | ------------------ | ---- | --- | ----------- | ----- |
|        |          |     |        |                    |     |     |           | • Time on | the highest layer: | Time | on  | the highest | layer |
Seufertetal.[10]. indicates the percentage of time the media playback
|     |     |     |     |     |     |     |     | was at the | highest quality. | High | values | of time | on the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ---- | ------ | ------- | ------ |
A. QUALITYSWITCHING highest layer indicate that the media playback was of
ThisisoneofthemaindifferentiatingfeaturesofHAScom-
|     |     |     |     |     |     |     |     | high quality | for a high | percentage |     | of media | playback |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ---------- | --- | -------- | -------- |
paredtoothertraditionalstreamingtechnologiesandiscom-
andhencecanbeusedasanIFformodeldesignasdone
| monly used | by  | HAS | clients | to adapt | the media | playback | to  | in[64]. |     |     |     |     |     |
| ---------- | --- | --- | ------- | -------- | --------- | -------- | --- | ------- | --- | --- | --- | --- | --- |
theanticipated/experiencednetworkconditionsand/orbuffer
status. As the rate adaptation algorithm is not standardized B. REBUFFERING
as part of the MPEG-DASH standard, it varies depending Rebuffering has long been considered as one of major
| on the client’s |     | rate adaptation |     | logic. | While | most | of the rate |                 |              |     |        |     |            |
| --------------- | --- | --------------- | --- | ------ | ----- | ---- | ----------- | --------------- | ------------ | --- | ------ | --- | ---------- |
|                 |     |                 |     |        |       |      |             | IF in streaming | applications | and | should | be  | avoided or |
adaptationtechniquesaimatminimizingrebufferingevents, minimized as much as possible. The rate adaptation
| frequent | quality | switches | may | lead | to annoyance |     | and hence |                     |         |        |              |     |           |
| -------- | ------- | -------- | --- | ---- | ------------ | --- | --------- | ------------------- | ------- | ------ | ------------ | --- | --------- |
|          |         |          |     |      |              |     |           | (quality switching) | feature | of HAS | applications |     | was actu- |
needtobeminimized. ally designed with the major goal of minimizing rebuffer-
• Quality switching frequency: Too frequent quality ing events during media playback. All models except
changesleadstoend-userannoyance.Someofthemod-
|     |     |     |     |     |     |     |     | for[64],[68],[71],[72],[75]–[77],[83] |     |     |     | take into | account |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --------- | ------- |
elssuchas[72]and[79]consideradaptationfrequency oneormorerebufferingrelatedimpairmentsasanIFintheir
| asoneoftheIFsfortheirmodeldesign. |     |     |     |     |     |     |     | modeldesign. |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
Quality switching magnitude: It refers to the ‘‘gap’’ Duration of rebuffering: While the general agreement
| •   |     |     |     |     |     |     |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
between the levels of quality switching. In general, for among researchers is that longer rebuffering duration
down-switching,qualityswitchingoflowermagnitudes, leads to increased annoyance of the end user, there
|     |     |     |     | →   |     |     | →   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i.e.,ingradualsteps(high mediumormedium exists some disagreement when it comes to acceptable
low)isconsideredtobelessannoyingthanthatofhigh level of rebuffering duration. While some researchers
magnitudes(abrupthigh-low)[107]. saythatrebufferingshouldbeavoidedatallcosts,there
• Quality switching direction In terms of the effect exists some who say that in general rebuffering events
of switching direction and their relative importance, ofshorterdurations(e.g.,of0.25seconds[73])arenot
there does not seem to exist a conclusiveagreement. noticeable and hence do not lead to QoE degradation.
| 30850 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2019 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
Durationofrebufferingcanbetakenintoaccountascon- encodedvideoquality.Usingsuchwellestablishedand
sideringtheaveragedurationofallrebufferingeventsas widelyusedmetricsbenefitsfromthepreviousresearch
done in[60] and[67] or taking into account individual workinthefieldofqualityassessment.Oneoftheshort-
rebufferingeventlengthasdonein[74]and[81]. comings of such models is the need of such models to
• Frequency of rebuffering: Highly frequent interrup- haveaccesstothemediasignals,hencemakingthemless
tions are considered annoying and can result in a very suitableforapplicationswherethetrafficisencrypted.
non-pleasant experience for the end user. Some of the
modelssuchas[66],[68],[80],[81]amongothers,con- D. INITIALLOADINGDELAY
siderthefrequencyofrebufferingasanIF. Initial loading delay is usually present in all streaming
• TemporalLocationofRebuffering:Temporallocationof applications and is used by the applications to buffer some
pauses,whilenotasimportantasfrequencyofrebuffer- video bits to minimize rebuffering related impairments.
inganddurationofrebuffering,certainlyplaysarolein The general agreement is that while shorter initial loading
theenduserQoEasapauseduringaninterestingscene delays do not have a significant impact on QoE, with some
isconsideredtobemoreannoyingthanonejustbeforea users actually preferring higher initial loading delay than
scenechange.Themodelsin[62],[66],[74],[80],etc., rebuffering[109],verylonginitialloadingdelaysmayleadto
takeintoaccountlocationofrebufferingasanIFintheir user dis-satisfaction which depends on application type and
model. usage scenario. Initial loading delay is used in models such
as[60],[61],[66],[67],[70],[72],[74],[78],and[80].
C. ENCODINGQUALITY
EncodedqualityplaysanimportantroleintheenduserQoE. E. MEMORYRELATEDFEATURES
For example, higher compression may result in noticeable Memory effects such as primacy and recency have recently
artifacts in the encoded video which results in decreased foundapplicationinthefieldofqualityassessment.Invideo
end-userQoE.Thereexistmanydifferentapproacheswhich streamingapplications,primacyrelatedfactorsmayreferto
canbeusedtoestimatethevideoquality,suchasQP,bitrate, experience due to initial loading delay, starting quality etc.
framerate,resolutionetc.Manyearlierworkshavefocusedon while recency related factors may refer to effects due to
thedesignofQoEmodelsandobjectivemetricstoestimate qualitylevel,rebufferingeventsetc.towardstheendofvideo
theencodedvideoquality.Inparticular,forHASapplications, playback. Only a few of the models directly use memory
the segment quality (in terms of bitrate/QP values) can also related factors. In general, primacy effects are considered
be used to represent the encoded video quality. The type not that important, especially when considering long video
of content plays a vital role in the perceived end-user qual- sequencesasitisbelievedotherfactorswillshadowtheeffect
ity. The actual effect of the various quality switchings (see towards the end[64]. Shen et al.[77] use primacy in their
SectionIV-B)dependonthecontenttype.Forexample,drop- model with the observation that higher quality at the start
pingframeswillhavealessnoticeableeffectonavideowith leadstohigherexperiencequalityratingsbutsincetheyuse
high motion content compared to a video with less motion short-durationsequencesintheirtests,thisobservationvalid-
content. Also, content complexity will decide the quality of ityforlongerdurationsequencesremainsquestionable.The
theencodedmedia.Fewmodelssuchas[77]directlyconsider recency effect is more widely used memory-related factor
contenttypeinformationasanIFintheirmodeldesign.Other with many studies reporting a high correlation between the
useparameterssuchasbitrate,QPetc.orexistingQAmetrics quality towards the end and the score provided by the end
asdiscussedbelow. user[68],[70],[74],[77],[80],[81].
• Bitrate: Bitrate is one of the most commonly used
parameters to estimate the encoded audio/video qual- F. USERENGAGEMENT
ity.Higherbitratevaluesusuallyindicatehigherquality User engagement refers to user actions during the media
videos.Themediaqualitycanbeapproximatedbyusing playback,suchaspause,seekforward/backward,aspectratio
the downloaded bitrate values for a given session. The change (full-screen, etc.) which also influence the final end
modelsin[63],[67],and[77]–[79]usebitratevaluesas userQoE.Intheabsenceofrecommendedpracticesforsuch
anIFintheirmodel. user behavior related measurements, such factors are not
• QP: QP is another commonly used factor to estimate considered in the models reviewed in this paper with the
encoded audio/video quality. Higher QP values result exception of Mok et al.[61], where the authors take into
in higher compression and vice versa, and hence QP accountenduseractionsforthedesignoftheirmodel.Only
values can be used to determine the quality of the fewworkssofarhaveinvestigatedtheuserbehaviorandits
encoded media representation. The models proposed effectontheend-userQoE[110].
in [63], [65], and [69]–[71] use QP values as one of
theIFs. VII. HASQoEMODELS:SUBJECTIVETEST
• Objective Metrics: Many models such as those pro- METHODOLOGIES
posedin[68],[75],[81]–[84]amongothersusealready Table4summarizesthesubjectiveassessmentmethodologies
existingormodifiedIQAorVQAmetricstoestimatethe asusedbythemodelproponentsfortheirmodeldesignand/or
VOLUME7,2019 30851

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
TABLE4. Summaryofsubjectiveevaluationmethodologiesusedbythemodels(D:Duration(seconds),V/AV:Video/Audiovisual),NV:Numberofvideos,
NA:Notavailable.
30852 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
validation.Itcanbeobservedthatformanymodelsthereare Some more recent works have considered higher source
certainfieldswithmissinginformation(markedbyNAinthe resolution formats such as HD [63], [71], [72], [76],
table). The lack of such information might leave the reader FHD[65],[67],[74],[79]andonlyoneworkhasconsidered
withagapinunderstandingtheactualapplicabilityandvalid- UHD sequences[84]. Also, spatial resolution adaptation,
ityoftheproposedmodel(s)forspecificapplicationscenario which consist of encoding the video at a lower resolution
and also limit their reproducibility and comparability with (calledasencodingresolution),isoneofthemostcommonly
other existing models. Hence new works which propose a usedstrategiesforqualityadaptationbyalmostallmajorOTT
modelshouldprovideasmuchinformationaspossibleabout serviceproviderssuchasYouTube,Netflix,AmazonPrime,
the considered conditions for the reader to understand both etc.Whilesomeoftheworkssuchas[66],[67],[74],and[79]
itsadvantagesaswellaslimitationsandalsotheapplicability haveconsideredsuchmultipleresolution-bitratepairencod-
of the model in real-world applications for QoE estimation. ingconditions,manyothersonlyconsiderqualityadaptation
Next,thedifferentindividualfieldsarediscussedindetail. atasingleresolution(byusingdifferentbitrates/QPsettings)
and hence those might not lead to satisfactory performance
A. DISPLAYDEVICEINFORMATION whenusedforqualityevaluationofsuchapplications.
Many studies in the past have found a strong correlation
betweenthedeviceandQoE,withsomeevenreportinghigh E. MODELPERFORMANCEEVALUATION
correlationbetweenthetypeofdisplayandQoE(forthesame As discussed in Section III-B, a performance evaluation of
displaysize)[116].Also,displaysizeisshowntohaveagreat a model for consistency, generality and prediction accuracy
effect on QoE, with impact of higher resolution becoming can be done using Outlier Ratio (OR), Spearman’s Rank
more prominent in displays of larger size. As evident from Correlation Coefficient (SROCC) and Pearson Linear Cor-
Table4,mostofthemodelsdonotmentionthedisplaytype relationCoefficient(PLCC)respectively.Someofthemod-
(mobile/tablet/PC/TV, etc.) and size of the display. Without els lack a complete validation (e.g.,[60],[61],[64],[65]),
such validation of the models for different display size and whichleavesanopenquestionabouttheperformanceofthe
display types, their applicability and performance remain modelsonunknowndatasetsand/orreal-worldapplications.
questionableforreal-worldapplications. Also,acomparisonstudyoftheproposedmodelswithother
existing models is absent in most cases except for a few
B. TESTSEQUENCEDURATION like[81]and[82].
Until recently, model design and validation was performed
using test sequences of 10-15 seconds duration which is F. VIDEO/AUDIOVISUALSEQUENCES
also recommended by ITU-T Recommendations[14],[15]. Some of the proposed models are limited to video only
Short duration sequences for such model design were suffi- (e.g.,[72],[73],[78],[80],[81]), without considering audio
cientastheymostlyonlydealtwithperceptualvideoquality intheirtestsequences.Thisisnottypicalofrealworldscenar-
due to loss of information due to compression, packet loss, ioswheremostofthemediaconsumedisaudiovisual.Also,
errorsduringtransmissionetc.Onthecontrary,shortduration none of the studies so far have included non-synchronized
sequencesarenotsufficientforeffectiveconsiderationofIFs audio-video playback at the end user device. It has been
such as rebuffering, quality switching, primacy and recency foundthataudiovisualqualityestimationismorechallenging
effects,etc.Forpropermodelingoftheseeffectsthesequence than video alone due to the complex nature of HVS with
durationshouldbelonger,possiblybetween3and5minutes, cross-modal interactions measured on an average of 0.5 on
which is the common viewing duration for most watched a5-pointMOSscale[117].
videosstreamedovertheInternet[66],asconsideredbysome
modelsin[67],[74],[76],amongothers. G. CODEC
WhilecurrentlyH.264remainsoneofthemostwidelyused
C. NUMBEROFSOURCEVIDEOS codecs, the limitation of the proposed models to one codec
As discussed earlier in Section VI-C, the effect of com- makesonequestionthefutureapplicabilityofsuchmodels;
pression for a given parameter (e.g., bitrate, QP, framerate) similarlysomemodelsonlyrefertoaparticularapplication.
depends to a great extent on the content complexity. For a For example, many applications like YouTube, etc., support
model to give a stable performance and to be applicable to multiple encoders. Hence a proposed model dependent on
morepracticalscenarios,itneedstobevalidatedfordifferent codecrelatedparameters(e.g.,bitstreambasedmodels)may
contenttypes.Asisevidentfromthetable,someofthemod- result in good performance but will fail for videos encoded
elsweredesignedandvalidatedusingfewsourcesequences usinganothercodecbutstreamedusingthesameapplication.
andhencetheireffectivenessforothercontenttypesremain A possible solution for such applications will be designing
questionable. models which take into account the type of codec used and
thenaccordinglychangingtheparameterstocompensatefor
D. VIDEORESOLUTION thedifferencesbetweenthecodecperformanceorbitstream
Most of the earlier works were limited to low source syntax. An interesting work currently in this direction is
resolution such as CIF[77], and SD[60],[62],[64],[66]. on-going under the joint collaboration of VQEG and ITU
VOLUME7,2019 30853

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
TABLE5. PubliclyavailableHASdatabases.
project called AVHD/P.NATS Phase 2 which includes bit- predictionmodels,intheabsenceofotherimpairments
stream and pixel based models considering three encoders ascommonlyobservedinreal-worldHASbasedappli-
(h.264,h.265andvp9). cations (rebuffering events, etc.) it is quite limited in
scopeforthedesignandvalidationofacomprehensive
VIII. PUBLICLYAVAILABLEHASDATASETS HASQoEmodel.
Based on our discussion so far, it is clear that very few of 2) WaterlooQoEDatabaseconsistsof20uncompressed
theworkshavemadetheirimplementationand/orthedataset HD videos and 60 compressed videos obtained by
public. Recent years have seen tremendous growth in the encoding the videos at three different bitrate levels
field of VQA, one of the main reasons behind which was (500 kbps, 1500 kbps and 3000 kbps) and 60 each
theavailabilityofopensourcedatabasessuchasLIVEVideo by introducing a 5 second stalling event at the start
QualityDatabase[118].Theavailabilityofsuchopensource and middle of the video playback resulting in a total
datasets allows researchers to gain comparable and more of 180 distorted video sequences. While this dataset
generalizableresultsforVQA,QoEpredictionmodeling,etc. includes both stalling and quality switching, as dis-
by providing a baseline for comparing the performance of cussed previously, this is fully realistic as the stalling
newlyproposedmodelsandmetricsagainsttheexistingstate- eventsareoffixeddurationaswellasatfixedlocations
of-the-artmetrics.Wediscussbrieflyinthissectiontheseven (start and middle of video playback). Also, quality
currentlypubliclyavailabledatasetsandtheiradvantagesand adaptation is considered based on only one dimen-
limitations in terms of their suitability for being used as a sion(compression)nottakingintoaccountotheradap-
benchmark for HAS models design and/or validation and tationdimensions(spatialandtemporal).
comparison. These are reported in Table 5 and discussed in 3) LIVE Netflix Video Quality of Experience Database
thefollowing. consists of subjective ratings considering 14 source
1) LIVEQoEDatabaseforHTTPbasedVideoStreaming video contents and 112 distorted video sequences
is one of the first publicly available dataset for mod- obtained by compressing the videos using the
eling continuous time-varying subjective quality. The H.264 encoder and eight different playout patterns
available videos are of 720p resolution and 300 sec- (including rebuffering events). The video dataset is
ondsduration,obtainedbyconcatenatingsmallerdura- limitedtoasingleresolutionof1080pandofdifferent
tion videos. The quality switching is performed only frame rates (24, 25 and 30 fps). One of the notable
using the quality (compression) adaptation dimension shortcomingsofthisdatasetisthatsinceituseseleven
and does not include multiple resolution-bitrate pairs, copyright-protected videos out of a total of 14, only
which is more realistic of the real-world applica- three source videos and the corresponding distorted
tions. While this dataset is very useful for studying videosare providedinthis dataset.While mostofthe
and/or modeling the continuous time quality varying commonly used FR and RR metric values are already
30854 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
provided, such a dataset is not suitable to evaluate both continuous as well as retrospective prediction
customQoEmodels. scores.Additionally,anopen-sourcePythonbasedtool
4) LFOVIA Video QoE Database consists of 18 uncom- calledPsychopy,togenerateanddisplayvisualstimuli
pressed reference videos and 36 distorted video and collect continuous per-frame subjective ratings,
sequences of 120 seconds duration and is the only ismadeavailable.
dataset so far which includes videos of resolution
up to 4K. The dataset considers both rebuffering IX. CONCLUSION,CHALLENGESANDFUTUREWORK
events (rebuffering frequency and rebuffering dura- In this paper, we surveyed the key QoE models for HAS
tion)andqualityswitching(multipleresolution-bitrate applications.Itwasobservedthatrebuffering,qualityswitch-
pairs)whicharerepresentativeofreal-worldconditions ing and encoding related impairments are the most widely
(though the ideal fixed duration up and down switch- consideredIFs.ItisinterestingtonotethatcontextIFssuch
ing may not be too realistic). Such a dataset, which as viewing environment, video popularity, type of usage,
includes both continuous and overall scores, is com- etc. are still not considered by any model except for one
prehensive enough for design/validation of real-world by Mok et al.[61]. It is also observed that most of the
applications. proposed models are limited in several aspects (considered
5) Live Mobile Stall Video Database II, which focuses IFs, performance evaluation, modeling of IFs/model, etc.),
onlyonstallingevents,consistsof24referencevideos withageneralcomprehensiveQoEmodelstillfarawayfrom
and174distortedvideosof720presolutiongenerated being ready. Regarding the effect of various IFs on the end
using 26 different stalling patterns. The dataset pro- userQoE,thereremainsadisagreementintheresearchcom-
vides both continuous as well as retrospective scores. munity on the relationship and importance of a particular
Suchadatasetcanbeusedtostudyandprobablymodel IF on the end user QoE. For example, some of the models
theeffectofstallingonuserQoE,but,intheabsenceof advocatetheusageofmemory-relatedfeatures,whileothers
sequencesandcorrespondingsubjectiveratingstaking ignorethemwiththereasoningthatsuchfactorsdonothave
intoaccountotherIFswhichmayaffectenduserQoE asignificanteffectonthefinalQoE.Moresystematic,well-
intypicalHASbasedapplications,itisnotexhaustive designed,large-scalesubjectivetestsarerequiredtoquantify
enoughfordesignand/orvalidationofQoEmodels. theimpactofvariousIFs,asdonein[108]forquantifyingthe
6) Waterloo QoE Database (ECT) consists of 12 source effectofresolutionswitchingonQoE.
videos8slong,whicharethenfurthersegmentedto4s One of the biggest challenge currently faced by the
segments(referredtoasshortsegments).Theshortseg- research community involved in QoE modeling for HAS
mentsarethenencodedintosevendifferentrepresenta- applications is that it is almost impossible for a single pro-
tionsetsobtainedbyencodingthematdifferentquality, ponent to design and conduct all-inclusive and comprehen-
frame rates and resolution. By concatenating the 4s sivesubjectivetest(s)duetohighcostsandtimeconstraints,
segments,8ssegmentsareobtainedtorepresentdiffer- especiallywhenconsideringthat,whenconsideringmultiple
entadaptationtypes(quality/spatial/temporal).Atotal IFs, the number of possible test conditions is enormous.
of 168 4s short segments and 588 eight sec segments This has been further hindered by the lack of open source
andtheircorrespondingsubjectiveratings(overalland databases. One of the primary reasons behind the progress
continuous (per segment)) are made available in the in the field of quality assessment for image and VQA can
dataset.Thedatasetcanbeusedasabaselinetowards be attributed to the open source databases such as LIVE
studyingtheeffectsofqualityadaptationbutislimited Video Quality Assessment Database[118] which facilitated
in many aspects, such as single adaptation event only design and comparison of many quality metrics. For HAS
andmissingimpactofotherIFs,henceisnotcompre- applications related models, out of the 28 reviewed models,
hensive enough for design and/or validation of HAS onlyfewhavemadetheirdatabasespublic(seeSectionVIII).
models. Thiscallsforaneedfortheresearchcommunitytomove
7) The latest, newly designed, LIVE-NFLX-II Subjective towards reproducible research by making work available
Video QoE Database is one of the most comprehen- in the form of open source databases. As evaluated and
sive databases available till date. The database con- discussed by Tavakoli et al.[107], subjective data gathered
sists of 15 source videos and a total of 420 distorted across different lab contexts provide comparable results.
sequences (using seven mobile network traces and Therefore,thereisaneedforthedesignofamethodological
considering four client adaptation algorithms) but is approachforsubjectivetestassessmentproceduresforHAS
limited in that it considers only one resolution. The applicationssothattheresultsandobservationscanberepro-
encoding bitrates are obtained using the recently pro- duced, reused and compared. There exist several methods
posed Dynamic Optimizer[122]. The use of four dif- to perform subjective assessment, but, to make the results
ferent adaptation algorithms in the database is useful reproducible, a set of standardized methods are published
to investigate the effect of such client-side adapta- by ITU-T in the form of recommendations, which discuss
tion on end user QoE and hence, in the design of a the methodology for deciding various test conditions such
more exhaustive QoE model. The database includes as the selection of proper test sequences, display settings,
VOLUME7,2019 30855

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
testenvironment,etc.[14],[15].Whilesuchstrictadherence shortcomingssuchaspossiblecheatingbyend-userto
to lab-based conditions are not imperative for HAS related receivebetterservice,etc.[21].Network-sidemonitor-
subjectivetests,followingpropersubjectivetestmethodolo- ing, while overcoming these issues, is not that effec-
gies and, even more importantly, reporting the conditions, tive regarding insight into the influence of factors on
canleadtoeasierunderstandingandreuseofresultsbyother QoE[22].
researchers. For a more detailed analysis of subjective test 5) Stakeholder: Depending on the amount and type of
assessmentmethodologiesandsomerelatedopenquestions, information required as input to the model, its mea-
we refer the reader to the work of Tavakoli et al.[107] and surementcanbeintrusiveornon-intrusive.Also,some
Garciaetal.[123]. modelsaredesignedtoworkwithencrypteddata,while
QoE modeling, due to its multi-disciplinary and highly others require access to bitstream or media signals.
subjectivenature,isachallengingtopic,especiallyforHAS Depending on the stakeholder, the requirements will
applicationswheretherearemanyIFsthatneedtobeconsid- vary. For example, a network provider, to monitor
ered. Even though QoE modeling for HAS applications has third-party OTT traffic, may prefer a QoE model that
recentlygainedtheattentionoftheresearchcommunity,there workswithencryptedvideo,assoonerorlater,allvideo
remainseveralopenchallengesandissuessuchas: streaming traffic will be encrypted[124]. Such fac-
1) Multi-factor QoE model design: As discussed in[10], tors need to be taken into consideration during model
there exist lots of influence factors which need to design.
be taken into consideration for the design of a com- 6) QoEbasedmanagement:Individualandjointeffectof
prehensive QoE model. Some IFs, especially context the various IFs need to be evaluated for the design of
relatedones,suchastheeffectofenvironment,purpose appropriate QoE control and management strategies.
of watching the service, etc., are still not considered Such insight can then be used for other applications.
by any model. As discussed in[124], to truly under- For example, the knowledge that frequent quality
stand the user’s QoE, a complete understanding of switching can lead to a decrease of QoE can lead
both streaming technique and implementation details to the design of better rate adaptation algorithms by
of each application is needed. Such detailed informa- theapplicationproviderwhileanetworkoperatorcan
tion can then be used for the design of a more ‘‘real- compensate for quality fluctuations by throttling the
istic’’ QoE model which can also take into account networkthroughput,tolimitthebandwidthfluctuation.
userinitiatedactionssuchasplay,pause,seeking(for- The research community has some exciting challenges
ward/backwards), etc. Future models should consider ahead of them. Faster and better results can be achieved by
takingintoaccountsuchIFsintheirmodeldesign. collaborative efforts and by moving further towards repro-
2) ModelComplexity:Mostoftheworksreviewedinthis ducibleresearch.
paper, with the exception of two (Xue et al.[70] and
Rodríguezetal.[66]),donotprovideanydiscussionon
REFERENCES
themodelcomplexityand/orenergyconsumptionasso-
ciatedtothequalityevaluationbasedonthemodel.The [1] Cisco. (Jun. 2017). Cisco Visual Networking Index: Fore-
cast and Methodology, 2016–2021. [Online]. Available:
useofhighcomplexityQoEmodelsattheclientdevice
https://www.cisco.com/c/en/us/solutions/collateral/service-provider/
can lead to reduced performance of the application visual-networking-index-vni/complete-white-paper-c11-481360.pdf
duetoincreasedconsumptionofpowerandcomputing [2] G.J.Sullivan,J.-R.Ohm,W.-J.Han,andT.Wiegand,‘‘Overviewofthe
highefficiencyvideocoding(HEVC)standard,’’IEEETrans.Circuits
resources.Similarly,forserver-basedmodels,IFsmea-
Syst.VideoTechnol.,vol.22,no.12,pp.1649–1668,Dec.2012.
surementinformation(rebufferingduration,numberof
[3] J.-R. Ohm, G. J. Sullivan, H. Schwarz, T. K. Tan, and T. Wiegand,
quality switches etc.) needs to be sent from the client ‘‘Comparison of the coding efficiency of video coding standards—
to the server to be considered by the model. Hence, includinghighefficiencyvideocoding(HEVC),’’IEEETrans.Circuits
Syst.VideoTechnol.,vol.22,no.12,pp.1669–1684,Dec.2012.
wearguethatstudiesonthecomplexityoftheexisting
[4] F.Bossen,CommonTestConditionsandSoftwareReferenceConfigu-
modelsareneededtohelpunderstandtheirreal-world rations, document JCTVC-L1100, ITU-T/ISO/IEC Joint Collaborative
applicability;similarly,relevantdiscussionsshouldbe TeamonVideoCoding(JCT-VC),Geneva,Switzerland,Jan.2013.
providedbytheproponentsofnewmodels. [5] L.Guo,J.DeCock,andA.Aaron,‘‘Compressionperformancecom-
parisonofx264,x265,LIBVPXandAOMENCforon-demandadap-
3) Subjective test methodology: As discussed in
tive streaming applications,’’ in Proc. Picture Coding Symp. (PCS),
Section VII, there still exists a need for proper sub- SanFrancisco,CA,USA,Jun.2018,pp.26–30.
jectiveassessmentmethodologyforHASapplications, [6] A.Zabrovskiy,C.Feldmann,andC.Timmerer,‘‘Apracticalevaluationof
videocodecsforlarge-scaleHTTPadaptivestreamingservices,’’inProc.
hence research on this aspect is encouraged, for more
25thIEEEInt.Conf.ImageProcess.(ICIP),Athens,Greece,Oct.2018,
scientificandreproducibleresearch. pp.998–1002.
4) Privacy Issues: Another challenge is the decision of [7] AProposedMediaDeliveryIndex(MDI),StandardRFC4445,Apr.2006.
where(client/server/network)todeploythemonitoring [8] ParametricNon-IntrusiveAssessmentofAudiovisualMediaStreaming
tool to acquire the measurements of the IFs consid- Quality,documentITU-TP.1201Recommendation,Oct.2012.
[9] ParametricBitstream-BasedQualityAssessmentofProgressiveDown-
eredbythemodel.Client-sidemonitoringandmanage-
loadandAdaptiveAudiovisualStreamingServicesOverReliableTrans-
ment are an invasion of privacy and also suffer from port,documentP.1203ITU-TRecommendation,Nov.2016.
30856 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
[10] M.Seufert,S.Egger,M.Slanina,T.Zinner,T.Hoßfeld,andP.Tran-Gia, [34] M. G. Martini, B. Villarini, and F. Fiorucci, ‘‘A reduced-reference
‘‘AsurveyonqualityofexperienceofHTTPadaptivestreaming,’’IEEE perceptual image and video quality metric based on edge preserva-
Commun.SurveysTuts.,vol.17,no.1,pp.469–492,1stQuart.,2015. tion,’’EURASIPJ.Adv.SignalProcess.,vol.2012,no.1,p.66,2012.
[11] P. Juluri, V. Tamarapalli, and D. Medhi, ‘‘Measurement of quality of doi:10.1186/1687-6180-2012-66.
experience of video-on-demand services: A survey,’’ IEEE Commun. [35] C. T. E. R. Hewage and M. G. Martini, ‘‘Reduced-reference quality
SurveysTuts.,vol.18,no.1,pp.401–418,1stQuart.,2016. assessmentfor3Dvideocompressionandtransmission,’’IEEETrans.
[12] P.LeCallet,S.Möller,andA.Perkis,‘‘Qualinetwhitepaperondefini- Consum.Electron.,vol.57,no.3,pp.1185–1193,Aug.2011.
tionsofqualityofexperience(2012),’’inProc.Eur.Netw.Qual.Exper. [36] C.T.E.R.HewageandM.G.Martini,‘‘Edge-basedreduced-reference
MultimediaSyst.Services(COSTActionIC),2012. qualitymetricfor3-Dvideocompressionandtransmission,’’IEEEJ.Sel.
[13] Vocabulary for Performance and Quality of Service. Amendment 5: TopicsSignalProcess.,vol.6,no.5,pp.471–482,Sep.2012.
New Definitions for Inclusion in Recommendation, document ITU-T [37] Z.WangandE.P.Simoncelli,‘‘Reduced-referenceimagequalityassess-
P.10/G.100Recommendation,Jul.2016. mentusingawavelet-domainnaturalimagestatisticmodel,’’Proc.SPIE
[14] SubjectiveVideoQualityAssessmentMethodsforMultimediaApplica- Conf.Hum.Vis.Electron.Imag.,vol.5666,pp.149–159,Jan.2005.
tions,documentITU-TP.910Recommendation,Apr.2008. [38] Q.LiandZ.Wang,‘‘Reduced-referenceimagequalityassessmentusing
[15] Methodology for the Subjective Assessment of the Quality of divisivenormalization-basedimagerepresentation,’’IEEEJ.Sel.Topics
Television Pictures, document ITU-T BT.500 Recommendation, SignalProcess.,vol.3,no.2,pp.202–211,Apr.2009.
Jan.2012. [39] L. Ma, S. Li, F. Zhang, and K. N. Ngan, ‘‘Reduced-reference image
[16] Z.Wang,A.C.Bovik,H.R.Sheikh,andE.P.Simoncelli,‘‘Imagequality qualityassessmentusingreorganizedDCT-basedimagerepresentation,’’
assessment:Fromerrorvisibilitytostructuralsimilarity,’’IEEETrans. IEEETrans.Multimedia,vol.13,no.4,pp.824–829,Aug.2011.
ImageProcess.,vol.13,no.4,pp.600–612,Apr.2004. [40] M.Carnec,P.LeCallet,andD.Barba,‘‘Objectivequalityassessmentof
[17] ReferenceAlgorithmforComputingPeakSignaltoNoiseRatioofaPro- colorimagesbasedonagenericperceptualreducedreference,’’Signal
cessedVideoSequenceWithCompensationforConstantSpatialShifts, Process.,ImageCommun.,vol.23,no.4,pp.239–256,Apr.2008.
Constant Temporal Shift, and Constant Luminance Gain and Offset, [41] PerceptualVisualQualityMeasurementTechniquesforMultimediaSer-
documentITU-TJ.340Recommendation,Jun.2010. vices Over Digital Cable Television Networks in the Presence of a
ReducedBandwidthReference,documentITU-TJ.246Recommendation,
[18] M. Seufert, M. Slanina, S. Egger, and M. Kottkamp, ‘‘‘To pool
Aug.2008.
or not to pool’: A comparison of temporal pooling methods for
[42] A.Mittal,A.K.Moorthy,andA.C.Bovik,‘‘No-referenceimagequality
HTTP adaptive video streaming,’’ in Proc. 5th Int. Workshop
assessmentinthespatialdomain,’’IEEETrans.ImageProcess.,vol.21,
Qual. Multimedia Exper. (QoMEX), Klagenfurt, Austria, Jul. 2013,
no.12,pp.4695–4708,Dec.2012.
pp.52–57
[43] A.Mittal,R.Soundararajan,andA.C.Bovik,‘‘Makinga‘Completely
[19] M. H. Pinson and S. Wolf, ‘‘A new standardized method for objec-
Blind’ Image Quality Analyzer,’’ IEEE Signal Process. Lett., vol. 20,
tivelymeasuringvideoquality,’’IEEETrans.Broadcast.,vol.50,no.3,
no.3,pp.209–212,Mar.2013.
pp.312–322,Sep.2004.
[44] M.A.Saad,A.C.Bovik,andC.Charrier,‘‘Blindimagequalityassess-
[20] L. Skorin-Kapov and M. Varela, ‘‘A multi-dimensional view of QoE:
ment:AnaturalscenestatisticsapproachintheDCTdomain,’’IEEE
theARCUmodel,’’inProc.35thInt.Conv.MIPRO,Opatija,Croatia,
Trans.ImageProcess.,vol.21,no.8,pp.3339–3352,Aug.2012.
May2012,pp.662–666.
[45] A.K.MoorthyandA.C.Bovik,‘‘Atwo-stepframeworkforconstructing
[21] T.Hobfeld,R.Schatz,M.Varela,andC.Timmerer,‘‘ChallengesofQoE
blindimagequalityindices,’’IEEESignalProcess.Lett.,vol.17,no.5,
managementforcloudapplications,’’IEEECommun.Mag.,vol.50,no.4,
pp.513–516,May2010.
pp.28–36,Apr.2012.
[46] ConformanceTestingforVoiceOverIPTransmissionQualityAssessment
[22] S. Baraković and L. Skorin-Kapov, ‘‘Survey and challenges of QoE
Models,documentITU-TP.564Recommendation,Nov.2007.
managementissuesinwirelessnetworks,’’J.Comput.Netw.Commun.,
[47] Opinion Model for Video-Telephony Applications, document G.1070
vol.2013,pp.165146:1–165146:28,Dec.2013.
ITU-TRecommendation,Jul.2012.
[23] W.Robitzaetal.,‘‘ChallengesoffuturemultimediaQoEmonitoringfor
[48] TheE-Model:AComputationalModelforUseinTransmissionPlanning,
Internetserviceproviders,’’MultimediaToolsAppl.,vol.76,pp.22243–
documentG.107ITU-TRecommendation,Jun.2015.
22266,Nov.2017.
[49] Opinion Model for Network Planning of video and Audio Streaming
[24] A.Ahmad,L.Atzori,andM.G.Martini,‘‘Qualia:Amultilayersolution
Applications,documentG.1071ITU-TRecommendation,Nov.2016.
forQoEpassivemonitoringattheuserterminal,’’inProc.IEEEInt.Conf.
[50] (2017). Adobe HTTP Dynamic Streaming (HDS). Accessed:
Commun.(ICC),Paris,France,May2017,pp.1–6.
Nov. 17, 2018. [Online]. Available: https://www.adobe.com/devnet/
[25] (2016).QUIC:AUDP-BasedSecureandReliableTransportforHTTP/2.
hds.html
Accessed: Nov. 27, 2018. [Online]. Available: https://tools.ietf.org/
[51] Apple.HTTPLiveStreaming.Accessed:Nov.17,2018.[Online].Avail-
html/draft-tsvwg-quic-protocol-02
able:https://developer.apple.com/streaming/
[26] Y. Chen, K. Wu, and Q. Zhang, ‘‘From QoS to QoE: A tutorial on [52] (2017). Microsoft Silverlight Smooth Streaming. Accessed:
videoqualityassessment,’’IEEECommun.SurveysTuts.,vol.17,no.2, Nov. 17, 2018. [Online]. Available: https://www.microsoft.com/
pp.1126–1165,2ndQuart.,2015. silverlight/smoothstreaming/
[27] VQEG.(2000).VQEGFRTVPhaseIFinalReport.[Online].Available: [53] Information Technology–Dynamic Adaptive Streaming Over HTTP
https://www.its.bldrdoc.gov/vqeg/projects/frtv-phase-i/frtv-phase-i.aspx (DASH)—Part 1: Media Presentation Description and Segment For-
[28] VQEG. (2003). VQEG FRTV Phase II Final Report. [Online]. Avail- mats,StandardISO/IEC23009-1:2014,2017.Accessed:Nov.17,2018.
able: https://www.its.bldrdoc.gov/vqeg/projects/frtv-phase-ii/frtv-phase- [Online].Available:https://www.iso.org/standard/65274.html
ii.aspx [54] I.Sodagar,‘‘TheMPEG-DASHstandardformultimediastreamingover
[29] A.Takahashi,D.Hands,andV.Barriac,‘‘Standardizationactivitiesinthe theInternet,’’IEEEMultimedia,vol.18,no.4,pp.62–67,Apr.2011.
ITUforaQoEassessmentofIPTV,’’IEEECommun.Mag.,vol.46,no.2, [55] J.Kua,G.Armitage,andP.Branch,‘‘Asurveyofrateadaptationtech-
pp.78–84,Feb.2008. niques for dynamic adaptive streaming over HTTP,’’ IEEE Commun.
[30] A.Raakeetal.,‘‘IP-basedmobileandfixednetworkaudiovisualmedia SurveysTuts.,vol.19,no.3,pp.1842–1866,3rdQuart.,2017.
services,’’ IEEE Signal Process. Mag., vol. 28, no. 6, pp. 68–79, [56] N.Cranley,P.Perry,andL.Murphy,‘‘Userperceptionofadaptingvideo
Nov.2011. quality,’’Int.J.Hum.-Comput.Stud.,vol.64,no.8,pp.637–647,2006.
[31] ObjectivePerceptualVideoQualityMeasurementTechniquesforDigital [57] S.Egger,B.Gardlo,M.Seufert,andR.Schatz,‘‘Theimpactofadap-
CableTelevisioninthePresenceofaFullReference,documentJ.144 tation strategies on perceived quality of HTTP adaptive streaming,’’
ITU-TRecommendation,Mar.2001. in Proc. Workshop Design, Qual. Deployment Adapt. Video Stream-
[32] Objective Perceptual Multimedia Video Quality Measurement in the ing, Sydney, NSW, Australia, 2014, pp. 31–36. [Online]. Available:
PresenceofaFullReference,documentITU-TJ.247Recommendation, http://doi.acm.org/10.1145/2676652.2676658
Aug.2008. [58] (2016). Global Internet Phenomena Report: North America and
[33] ObjectivePerceptualMultimediaVideoQualityMeasurementofHDTV Latin America. Accessed: Nov. 14, 2018. [Online]. Available:
forDigitalCableTelevisioninthePresenceofaFullReference,document https://www.sandvine.com/resources/global-internet-phenomena/2016/
ITU-TJ.341Recommendation,Mar.2016. north-america-and-latin-america.html
VOLUME7,2019 30857

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
[59] B.Wang,J.Kurose,P.Shenoy,andD.Towsley,‘‘Multimediastreaming [79] M.N.Garcia,W.Robitza,andA.Raake,‘‘Ontheaccuracyofshort-
viaTCP:Ananalyticperformancestudy,’’ACMTrans.MultimediaCom- termqualitymodelsforlong-termqualityprediction,’’inProc.7thInt.
put.Commun.Appl.,vol.4,no.2,pp.16:1–16:22,May2008.[Online]. WorkshopQual.MultimediaExper.(QoMEX),Pylos,Greece,May2015,
Available:http://doi.acm.org/10.1145/1352012.1352020 pp.1–6.
[60] R.K.P.Mok,E.W.W.Chan,andR.K.C.Chang,‘‘Measuringthequality [80] Z. Duanmu, K. Zeng, K. Ma, A. Rehman, and Z. Wang, ‘‘A quality-
ofexperienceofHTTPvideostreaming,’’inProc.12thIFIP/IEEEInt. of-experience index for streaming video,’’ IEEE J. Sel. Topics Signal
Symp.Integr.Netw.Manage.(IM)Workshops,Dublin,Ireland,May2011, Process.,vol.11,no.1,pp.154–166,Feb.2017.
pp.485–492. [81] C.G.BampisandA.C.Bovik,‘‘Learningtopredictstreamingvideo
[61] R.K.P.Mok,E.W.W.Chan,X.Luo,andR.K.C.Chang,‘‘Inferringthe QoE:Distortions,rebufferingandmemory,’’CoRR,vol.abs/1703.00633,
QoEofHTTPvideostreamingfromuser-viewingactivities,’’inProc.1st Mar.2017.[Online].Available:http://arxiv.org/abs/1703.00633
ACMSIGCOMMWorkshopMeas.UpStack,Toronto,ON,Canada,2011, [82] C.G.Bampis,Z.Li,andA.C.Bovik,‘‘Continuouspredictionofstream-
pp.31–36. ingvideoQoEusingdynamicnetworks,’’IEEESignalProcess.Lett.,
[62] D.Z.Rodríguez,J.Abrahao,D.C.Begazo,R.L.Rosa,andG.Bressan, vol.24,no.7,pp.1083–1087,Jul.2017.
‘‘QualitymetrictoassessvideostreamingserviceoverTCPconsidering [83] C.G.BampisandA.C.Bovik.(2017).‘‘Anaugmentedautoregressive
temporallocationofpauses,’’IEEETrans.ConsumerElectron.,vol.58, approachtoHTTPvideostreamqualityprediction.’’[Online].Available:
no.3,pp.985–992,Aug.2012. https://arxiv.org/abs/1707.02709
[63] C.Albertietal.,‘‘AutomatedQoEevaluationofdynamicadaptivestream- [84] N.Eswaraetal.,‘‘AcontinuousQoEevaluationframeworkforvideo
ingoverHTTP,’’inProc.5thInt.WorkshopQual.MultimediaExper. streamingoverHTTP,’’IEEETrans.CircuitsSyst.VideoTechnol.,vol.28,
(QoMEX),Klagenfurt,Austria,Jul.2013,pp.58–63. no.11,pp.3236–3250,Nov.2018.
[64] T.Hoßfeld,M.Seufert,C.Sieber,andT.Zinner,‘‘Assessingeffectsizes [85] D.Ghadiyaram,J.Pan,andA.C.Bovik,‘‘Learningacontinuous-time
ofinfluencefactorstowardsaQoEmodelforHTTPadaptivestreaming,’’ streamingvideoQoEmodel,’’IEEETrans.ImageProcess.,vol.27,no.5,
inProc.6thInt.WorkshopQual.MultimediaExper.(QoMEX),Singapore, pp.2257–2271,May2018.
Sep.2014,pp.111–116. [86] N.Eswaraetal.,‘‘StreamingvideoQoEmodelingandprediction:Along
[65] J.Lievens,A.Munteanu,D.DeVleeschauwer,andW.VanLeekwijck, short-termmemoryapproach,’’CoRR,vol.abs/1807.07126,Jul.2018.
‘‘PerceptualvideoqualityassessmentinHTTPadaptivestreaming,’’in [Online].Available:https://arxiv.org/abs/1807.07126
Proc.IEEEInt.Conf.Consum.Electron.(ICCE),LasVegas,NV,USA,
[87] Z. Duanmu, K. Ma, and Z. Wang, ‘‘Quality-of-experience for adap-
Jan.2015,pp.72–73.
tive streaming videos: An expectation confirmation theory motivated
[66] D.Z.Rodríguez,R.L.Rosa,E.C.Alfaia,J.I.Abrahão,andG.Bressan,
approach,’’IEEETrans.ImageProcess.,vol.27,no.12,pp.6135–6146,
‘‘VideoqualitymetricforstreamingserviceusingDASHstandard,’’IEEE
Dec.2018.
Trans.Broadcasting,vol.62,no.3,pp.628–639,Sep.2016.
[88] Y.-F.Ou,Y.Xue,andY.Wang,‘‘Q-STAR:Aperceptualvideoquality
[67] K.YamagishiandT.Hayashi,‘‘Parametricquality-estimationmodelfor
model considering impact of spatial, temporal, and amplitude resolu-
adaptive-bitrate-streamingservices,’’IEEETrans.Multimedia,vol.19,
tions,’’ IEEE Trans. Image Process., vol. 23, no. 6, pp. 2473–2486,
no.7,pp.1545–1557,Jul.2017.
Jun.2014.
[68] F.Wang,Z.Fei,J.Wang,Y.Liu,andZ.Wu,‘‘HASQoEpredictionbased
[89] R.SoundararajanandA.C.Bovik,‘‘Videoqualityassessmentbyreduced
ondynamicvideofeatureswithdatamininginLTEnetwork,’’Sci.China
referencespatio-temporalentropicdifferencing,’’IEEETrans.Circuits
Inf.Sci.,vol.60,no.4,pp.042404:1–042404:14,Apr.2017.
Syst.VideoTechnol.,vol.23,no.4,pp.684–694,Apr.2013.
[69] K.D.Singh,Y.Hadjadj-Aoul,andG.Rubino,‘‘Qualityofexperience
[90] Amendment 2: New Appendix III—Use of P.1201 for Non-Adaptive,
estimationforadaptiveHTTP/TCPvideostreamingusingH.264/AVC,’’
ProgressiveDownloadTypeMediaStreaming,documentITU-TP.1201
inProc.IEEEConsumerCommun.Netw.Conf.(CCNC),LasVegas,NV,
Recommendation,Dec.2013.
USA,Jan.2012,pp.127–131
[91] H. Ebbinghaus, Memory: A Contribution to Experimental Psychology
[70] J. Xue, D.-Q. Zhang, H. Yu, and C. W. Chen, ‘‘Assessing quality of
(H.A.Ruger&C.E.Bussenius,Trans.)NewYork,NY,USA:Teachers
experience for adaptive HTTP video streaming,’’ in Proc. IEEE Int.
CollegePress,1913.doi:10.1037/10011-000.
Conf.MultimediaExpoWorkshops(ICMEW),Chengdu,China,Jul.2014,
[92] A. Rehman, K. Zeng, and Z. Wang, ‘‘Display device-adapted
pp.1–6.
video quality-of-experience assessment,’’ Proc. SPIE, vol. 9394,
[71] Z.Guo,Y.Wang,andX.Zhu,‘‘Assessingthevisualeffectofnon-periodic
pp.9394-1–9394-11,Mar.2015.
temporal variation of quantization stepsize in compressed video,’’ in
[93] T.Hoßfeld,M.Seufert,M.Hirth,T.Zinner,P.Tran-Gia,andR.Schatz,
Proc.IEEEInt.Conf.ImageProcess.(ICIP),QuebecCity,QC,Canada,
‘‘QuantificationofYouTubeQoEviacrowdsourcing,’’inProc.IEEEInt.
Sep.2015,pp.3121–3125.
Symp.Multimedia,DanaPoint,CA,USA,Dec.2011,pp.494–499.
[72] H.T.T.Tran,T.Vu,N.P.Ngoc,andT.C.Thang,‘‘Anovelqualitymodel
forHTTPadaptivestreaming,’’inProc.IEEE6thInt.Conf.Commun. [94] Scikit-Learn: Machine Learning in Python. Accessed: Dec. 17, 2018.
Electron.(ICCE),HaLong,Vietnam,Jul.2016,pp.423–428. [Online].Available:http://scikit-learn.org/stable/
[73] H.T.T.Tran,N.P.Ngoc,A.T.Pham,andT.C.Thang,‘‘Amulti-factor [95] N.Ponomarenko,F.Silvestri,K.Egiazarian,J.A.M.Carli,andV.Lukin,
QoEmodelforadaptivestreamingovermobilenetworks,’’inProc.IEEE ‘‘Onbetween-coefficientcontrastmaskingofDCTbasisfunctions,’’in
GlobecomWorkshops(GCWkshps),Washington,DC,USA,Dec.2016, Proc.Int.WorkshopVideoProcess.Qual.Metrics,2007,pp.1–4.
pp.1–6. [96] Z. Wang, E. P. Simoncelli, and A. C. Bovik, ‘‘Multiscale struc-
[74] W.Robitza,M.-N.Garcia,andA.Raake,‘‘AmodularHTTPadaptive turalsimilarityforimagequalityassessment,’’inProc.37thAsilomar
streaming QoE model—Candidate for ITU-T P.1203 (‘P.NATS’),’’ in Conf. Signals, Syst. Comput., Pacific Grove, CA, USA, Nov. 2003,
Proc.9thInt.Conf.Qual.MultimediaExper.(QoMEX),Erfurt,Germany, pp.1398–1402.
May/Jun.2017,pp.1–6. [97] W. Xue, L. Zhang, X. Mou, and A. C. Bovik, ‘‘Gradient magnitude
[75] J. De Vriendt, D. De Vleeschauwer, and D. Robinson, ‘‘Model for similaritydeviation:Ahighlyefficientperceptualimagequalityindex,’’
estimatingQoEofvideodeliveredusingHTTPadaptivestreaming,’’in IEEETrans.ImageProcess.,vol.23,no.2,pp.684–695,Feb.2014.
Proc.IFIP/IEEEInt.Symp.Integr.Netw.Manage.(IM),Ghent,Belgium, [98] Netflix.VMAFDevelopmentKit(VDK1.0.0).Accessed:Nov.12,2018.
May2013,pp.1288–1293. [Online].Available:https://github.com/Netflix/vmaf
[76] C.Chen,L.K.Choi,G.deVeciana,C.Caramanis,R.W.Heath,and [99] D.S.HandsandS.E.Avons,‘‘Recencyanddurationneglectinsubjective
A.C.Bovik,‘‘Modelingthetime–varyingsubjectivequalityofHTTP assessmentoftelevisionpicturequality,’’Appl.Cognit.Psychol.,vol.15,
video streams with rate adaptations,’’ IEEE Trans. Image Process., no.6,pp.639–657,2001.
vol.23,no.5,pp.2206–2221,May2014. [100] D.J.BerndtandJ.Clifford,‘‘Usingdynamictimewarpingtofindpatterns
[77] Y.Shen,Y.Liu,Q.Liu,andD.Yang,‘‘AmethodofQoEevaluation intimeseries,’’inProc.3rdInt.Conf.Knowl.DiscoveryDataMining,
foradaptivestreamingbasedonbitratedistribution,’’inProc.IEEEInt. Seattle,WA,USA:AAAIPress,1994,pp.359–370.[Online].Available:
Conf.Commun.Workshops(ICC),Sydney,NSW,Australia,Jun.2014, http://dl.acm.org/citation.cfm?id=3000850.3000887
pp.551–556. [101] C. G. Bampis, Z. Li, A. K. Moorthy, I. Katsavounidis, A. Aaron,
[78] Y.Liu,S.Dey,F.Ulupinar,M.Luby,andY.Mao,‘‘Derivingandvali- and A. C. Bovik, ‘‘Study of temporal effects on subjective video
datinguserexperiencemodelforDASHvideostreaming,’’IEEETrans. quality of experience,’’ IEEE Trans. Image Process., vol. 26, no. 11,
Broadcast.,vol.61,no.4,pp.651–665,Dec.2015. pp.5217–5231,Nov.2017.
30858 VOLUME7,2019

N.Barman,M.G.Martini:QoEModelingforHTTPAdaptiveVideoStreaming—ASurveyandOpenChallenges
[102] M.Fiedler,T.Hoßfeld,andP.Tran-Gia,‘‘Agenericquantitativerelation- [124] (2016).VideoQualityofExperience:RequirementsandConsiderations
shipbetweenqualityofexperienceandqualityofservice,’’IEEENetw., for Meaningful Insight. Accessed: Nov. 14, 2018. [Online].
vol.24,no.2,pp.36–41,Mar./Apr.2010. Available: https://www.sandvine.com/resources/whitepapers/video-
[103] D.Ghadiyaram,J.Pan,andA.C.Bovik,‘‘Asubjectiveandobjective quality-of-experience.html
studyofstallingeventsinmobilestreamingvideos,’’IEEETrans.Circuits
Syst.VideoTechnol.,vol.29,no.1,pp.183–197,Jan.2019.
[104] S. Satti, C. Schmidmer, M. Obermann, R. Bitto, L. Agarwal, and
M. Keyhl, ‘‘P.1203 evaluation of real OTT video services,’’ in Proc.
9th Int. Conf. Qual. Multimedia Exper. (QoMEX), Erfurt, Germany,
May/Jun.2017,pp.1–3.
[105] W.Robitzaetal.,‘‘HTTPadaptivestreamingQoEestimationwithITU-
TRec.P.1203:Opendatabasesandsoftware,’’inProc.9thACMMul-
timediaSyst.Conf.,Amsterdam,TheNetherlands,2018,pp.466–471.
NABAJEET BARMAN received the B.Tech.
[Online].Available:http://doi.acm.org/10.1145/3204949.3208124
degree in electronics engineering from the
[106] T. Hoßfeld, L. Skorin-Kapov, P. E. Heegaard, M. Varela, and
NationalInstituteofTechnology,Surat,India,with
K.-T.Chen,‘‘OnadditiveandmultiplicativeQoS-QoEmodelsformul-
tipleQoSparameters,’’inProc.5thISCA/DEGAWorkshopPerceptual afocusonwirelessnetworks,andtheM.Sc.degree
Qual.Syst.,Berlin,Germany,2016,pp.44–48. in information technology with specialization in
[107] S. Tavakoli, S. Egger, M. Seufert, R. Schatz, K. Brunnström, and communication engineering and media technol-
N. García, ‘‘Perceptual quality of HTTP adaptive streaming strate- ogy from Universität Stuttgart, Germany. He is
gies:Cross-experimentalanalysisofmulti-laboratoryandcrowdsourced currentlypursuingthePh.D.degreeinqualityof
subjective studies,’’ IEEE J. Sel. Areas Commun., vol. 34, no. 8, experience of gaming video streaming applica-
pp.2141–2153,Aug.2016. tionswithKingstonUniversity.HewaswithBell
[108] A.Asan,W.Robitza,I.H.Mkwawa,L.Sun,E.Ifeachor,andA.Raake, Labs, Stuttgart, Germany, as a part of his internship and master’s thesis.
‘‘ImpactofvideoresolutionchangesonQoEforadaptivevideostream- He is currently a Research Associate with the Wireless Multimedia and
ing,’’inProc.IEEEInt.Conf.MultimediaExpo(ICME),HongKong, Networking Research Group, Kingston University, where he is working
Jul.2017,pp.499–504. onQoE-awarevideocodingstrategiesasapartofMSCAITNQoE-Net.
[109] T. Hoßfeld, S. Egger, R. Schatz, M. Fiedler, K. Masuch, and He is currently a Video Quality Expert Group Board Member as a part
C. Lorentzen, ‘‘Initial delay vs. Interruptions: Between the devil and oftheComputerGraphicsImageryProjectandisalsoinvolvedinITU-T
thedeepbluesea,’’inProc.Int.WorkshopQualityMultimediaExper.,
standardizationactivities.Hisresearchinterestsincludewirelessnetworking,
Jul.2012,pp.1–6.
multimediacommunications,andmachinelearning.
[110] W.Robitza,P.A.Kara,M.G.Martini,andA.Raake,‘‘Ontheexperimen-
talbiasesinuserbehaviorandQoEassessmentinthelab,’’inProc.IEEE
GlobecomWorkshops(GCWkshps),Washington,DC,USA,Dec.2016,
pp.1–6.
[111] WaterlooQoEDatabase.Accessed:Nov.5,2018.[Online].Available:
https://ece.uwaterloo.ca/~zduanmu/jstsp16qoe/
[112] LIVE Netflix Video Quality of Experience Database. Accessed:
Nov. 5, 2018. [Online]. Available: http://live.ece.utexas.edu/research/
MARIAG.MARTINI(SM’07)receivedtheLau-
LIVE_NFLXStudy/nflx_index.html
readegree(summacumlaude)inelectronicengi-
[113] Live Mobile Stall Video Database II. Accessed: Nov. 15, 2018.
neering from the University of Perugia, Italy, in
[Online].Available:http://live.ece.utexas.edu/research/LIVEStallStudy/
liveMobile.html 1998, and the Ph.D. degree in electronics and
[114] LFOVIAVideoQoEDatabase.Accessed:Nov.5,2018.[Online].Avail- computersciencefromtheUniversityofBologna,
able:https://www.iith.ac.in/~lfovia/downloads.html Italy,in2002.SheisaProfessorwiththeFaculty
[115] LIVE QoE Database for HTTP Based Video Streaming. Accessed: ofScience,EngineeringandComputing,Kingston
Nov. 15, 2018. [Online]. Available: http://live.ece.utexas.edu/ University, London, U.K., where she also leads
research/Quality/TVSQ_VQA_database.html the Wireless Multimedia Networking Research
[116] R.SchatzandS.Egger,‘‘Ontheimpactofterminalperformanceand Group. She has led the KU Team in a number
screensizeonQoE,’’inProc.ETSIWorkshopSel.ItemsTelecommun. of national and international research projects, funded by the European
Qual.Matters,Vienna,Austria,Nov.2012,pp.1–26. Commission(e.g.,OPTIMIX,CONCERTO,QoE-NET,andQualinet),U.K.
[117] B.BelmudezandS.Möller,‘‘Audiovisualqualityintegrationforinter- research councils, U.K. Technology Strategy Board / InnovateUK, and
active communications,’’ EURASIP J. Audio, Speech, Music Process., internationalindustries.Shehasauthoredabout150scientificarticles,con-
vol.2013,no.1,p.24,2013. tributions to standardization groups (IEEE, ITU), and several patents on
[118] LIVE Video Quality Assessment Database. Accessed: wirelessvideo.HerresearchinterestsincludeQoE-drivenwirelessmultime-
Nov. 15, 2018. [Online]. Available: http://live.ece.utexas.edu/research diacommunications,decisiontheory,videoqualityassessment,andmedical
/Quality/live_video.html applications.Shechaired/organizedanumberofconferencesandworkshops.
[119] Waterloo QoE Database (ECT). Accessed: Nov. 15, 2018. [Online]. Sheisamemberofinternationalcommitteesandexpertgroups,including
Available:https://ece.uwaterloo.ca/zduanmu/tip2018ectqoe/
theNetWorld2020EuropeanTechnologyPlatformExpertAdvisoryGroup,
[120] C.G.Bampis,Z.Li,I.Katsavounidis,T.-Y.Huang,C.Ekanadham,and
theVideoQualityExpertGroup,andtheIEEEMultimediaCommunications
A.C.Bovik,‘‘Towardsperceptuallyoptimizedend-to-endadaptivevideo
TechnicalCommittee,whereshehasservedastheVice-Chair(2014–2016),
streaming,’’CoRR,vol.abs/1808.03898,Aug.2018.[Online].Available:
astheChair(2012–2014)ofthe3DRendering,Processing,andCommuni-
https://arxiv.org/abs/1808.03898
cationsInterestGroup,andasaKeyMemberoftheQoEandMultimedia
[121] LIVE-NFLX-II Subjective Video QoE Database. Accessed:
StreamingIG.SheisanExpertEvaluatorfortheEuropeanCommission,
Nov. 5, 2018. [Online]. Available: http://live.ece.utexas.edu/research/
EPSRC, and other research funding bodies. She was an Associate Editor
LIVE_NFLX_II/live_nflx_plus.html
[122] Netflix.(Mar.2018).DynamicOptimizer—APerceptualVideoEncoding
oftheIEEETRANSACTIONSONMULTIMEDIA(2014–2018).Shehasalsobeen
OptimizationFramework.Accessed:Nov.15,2018.[Online].Available: aLeadGuestEditoroftheIEEEJSACspecialissueonQoE-awarewireless
https://medium.com/netflix-techblog/dynamic-optimizer-a-perceptual- multimediasystemsandaGuestEditoroftheIEEEJOURNALOFBIOMEDICAL
video-encoding-optimization-framework-e19f1e3a277f ANDHEALTHINFORMATICS,theIEEEMULTIMEDIA,andtheInternationalJournal
[123] M.-N.Garciaetal.,‘‘QualityofexperienceandHTTPadaptivestream- ofTelemedicineandApplications,amongothers.SheiscurrentlyanAsso-
ing:Areviewofsubjectivestudies,’’inProc.6thInt.WorkshopQual. ciateEditoroftheIEEESignalProcessingMagazine.
MultimediaExper.(QoMEX),Singapore,Sep.2014,pp.141–146
VOLUME7,2019 30859