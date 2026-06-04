Public Review for
Understanding Quality-of-Experience of
Heuristic-based HTTP Adaptive Bitrate
Algorithms
B. Taraghi, A. Bentaleb, C. Timmerer, R. Zimmermann,
H. Hellwagner
Mostonlinevideostreamingservices, includingmajoronessuchasYouTube
and Netflix, use adaptive streaming over HTTP, which dynamically adapts
the bitrates of the sessions to maximize the quality of experience (QoE)
for different users. Many algorithms have been proposed in the literature,
and some deployed in practice, to perform this dynamic adaptation. It is
crucialfortheresearchcommunitytooccasionallyreflectandcontrastvarious
adaptationalgorithmsagainsteachothertodiscoveropportunitiesforfurther
optimizations.
The authors of this paper contribute to this important issue and offer us a
deeper understanding of these adaptation algorithms. They compare seven
common rate adaptation algorithms, including buffer-based (Bola, BBA0,
and Quetra), throughput-based (Shaka), and Model Predictive Controller
(Fast MPC), using objective and subjective studies. The objective study
utilizes the ITU-T P.1203 QoE model, which calculates a predicted Mean
OpinionScore(MOS)ofavideobasedonthebitrate, framerate, resolution,
frame types, and frame sizes. The subjective study was conducted on a
cloud platform with more than 800 real users (Amazon Mechanical Turks).
Severalrealvideoswereeachencodedinto11representationsandusedinthe
subjectiveandobjectivestudies. Theauthorsalsousedfournetworkprofiles
to capture some of the real-life scenarios.
Thepaperindeedshedslightonunderstandingthecomplexproblemofqual-
ity adaptation in HTTP video streaming. The results should however be
considered as the first step in this direction and should be approached with
a critical eye. A workshop paper is a way to share exciting results with the
community as early as possible. It is also an invitation to further expand
theresults. Typicalfutureworkthatcanbebuiltuponthispaperincludesa
morecomprehensiveevaluation,usingmorenetworkprofiles(maybefromac-
tualdatasets)andamorediversecatalogofvideos(forexamplehigh-motion
videos). Another promising extension to this paper is the evaluation of the
recent learning-based rate adaptation algorithms.
Public review written by
Mohamed Hefeeda
Simon Fraser University, Canada
ACM NOSSDAV 2021
82

Understanding Quality of Experience of Heuristic-based
HTTP Adaptive Bitrate Algorithms
BabakTaraghi AbdelhakBentaleb ChristianTimmerer
babak.taraghi@aau.at bentaleb@comp.nus.edu.sg christian.timmerer@aau.at
ChristianDopplerLaboratoryATHENA DepartmentofComputerScience ChristianDopplerLaboratoryATHENA
InstituteofInformationTechnology(ITEC) SchoolofComputing(SoC) InstituteofInformationTechnology(ITEC)
Alpen-Adria-UniversitätKlagenfurt NationalUniversityofSingapore Alpen-Adria-UniversitätKlagenfurt
Klagenfurt,Austria Singapore Klagenfurt,Austria
RogerZimmermann HermannHellwagner
rogerz@comp.nus.edu.sg hermann.hellwagner@aau.at
DepartmentofComputerScience ChristianDopplerLaboratoryATHENA
SchoolofComputing(SoC) InstituteofInformationTechnology(ITEC)
NationalUniversityofSingapore Alpen-Adria-UniversitätKlagenfurt
Singapore Klagenfurt,Austria
ABSTRACT ACMReferenceFormat:
Adaptivebitrate(ABR)algorithmsplayacrucialroleindeliver- BabakTaraghi,AbdelhakBentaleb,ChristianTimmerer,RogerZimmer-
mann,andHermannHellwagner.2021.UnderstandingQualityofExperi-
ingthehighestpossibleviewer’sQualityofExperience(QoE)in
HTTPAdaptiveStreaming(HAS).Onlinevideostreamingservice
enceofHeuristic-basedHTTPAdaptiveBitrateAlgorithms.InNetwork
andOperatingSystemSupportforDigitalAudioandVideo(NOSSDAV’21),
providersuseHAS–thedominantvideostreamingtechniqueon
September28–October1,2021,Istanbul,Turkey.,7pages.https://doi.org/10.
theInternet–todeliverthebestQoEfortheirusers.Aviewer’sde-
1145/3458306.3458875
lightreliesheavilyonhowtheABRofamediaplayercanadaptthe
stream’squalitytothecurrentnetworkconditions.QoEforvideo
streamingsessionshasbeenassessedinmanyresearchprojects 1 INTRODUCTION
togivebetterinsightintothesignificantqualitymetricssuchas Videotrafficaccountedfor66%ofallmobiledatatrafficin2020,a
startupdelayandstallevents.TheITUTelecommunicationStan- sharethatisforecastedtoincreaseto77%in2026[15].Moreover,in
dardizationSector(ITU-T)P.1203qualityevaluationmodelallows 2020theCOVID-19pandemicskyrocketedthenumberofviewers
toalgorithmicallypredictasubjectiveMeanOpinionScore(MOS) streamingvideoandviewinghours[9].HTTPAdaptiveStreaming
byconsideringvariousqualitymetrics.Subjectiveevaluationis (HAS)isthedominanttechniqueforvideostreamingwithtwo
thebestassessmentmethodforexaminingtheend-useropinion mostcommonlyimplementedmediadeliveryformats,HTTPLive
overavideostreamingsession’sexperiencedquality.Wehavecon- Streaming(HLS)[2]andDynamicAdaptiveStreamingoverHTTP
ductedsubjectiveevaluationswithcrowdsourcedparticipantsand (MPEG-DASH)[23].HAS-basedmediadeliveryformatspartition
evaluatedtheMOSofthesessionsusingtheITU-TP.1203quality avideofileintomultipleaudioandvideosegmentsofthesame
model.Thispaper’smaincontributionistoinvestigatethecorre- duration,oftenbetween2and10seconds.Eachsegmentisencoded
spondenceofsubjectiveandobjectiveevaluationsforwell-known withvariousrepresentations(i.e.,bitratelevelsandresolutions).A
heuristic-basedABRs. playlistfilecalledmanifestprovidestheinformationonavailable
representationsandthesegments’locationstothemediaplayer.The
CCSCONCEPTS criticaldecisionofchoosingtherepresentationforeachsegment
downloadistheprimaryjobofanadaptivebitrate(ABR)algorithm.
•Informationsystems→Informationsystemsapplications;
TherearemanymetricsthatanABRalgorithmcouldtakeinto
•Multimediainformationsystems→Multimediastreaming.
accountwhenmakingsuchadecision,e.g.,buffersize,available
bandwidth,networklatency,oracombinationthereof.
KEYWORDS
Qualityofexperience(QoE)is,bydefinition,themeasureof
HTTPAdaptiveStreaming;ABRAlgorithms;QualityofExperience;
thedelightorannoyanceofacustomer’sexperienceswithaser-
Crowdsourcing;SubjectiveEvaluation;ObjectiveEvaluation;MOS;
vice[10].AnABRalgorithmplaysthepivotalroletoprovidethe
ITU-TP.1203.
bestexperiencetotheend-userofavideostreamingsessionby
choosingasuitablemediarepresentationattherighttime.Selecting
alow-qualityrepresentationideallydecreasesthenumberofstall
events,butthistrade-offisonlyacceptableiftheclientissuffering
fromaterriblenetworkconnection.Inanotherscenario,selecting
This work is licensed under a Creative Commons Attribution International 4.0 License. high-qualityrepresentationswoulddeliverdetailedaudioandvideo
NOSSDAV ’21, September 28–October 1, 2021, Istanbul, Turkey totheclient.Still,stalleventshavemorechancestohappenifthe
© 2021 Copyright held by the owner/author(s).
networkcharacteristicsarenotpredictedaccurately[7].Therefore,
ACM ISBN 978-1-4503-8435-3/21/09.
https://doi.org/10.1145/3458306.3458875 howdelightfulorannoyedanend-userofavideostreamingservice
83

NOSSDAV’21,September28–October1,2021,Istanbul,Turkey BabakTaraghi,AbdelhakBentaleb,ChristianTimmerer,RogerZimmermann,andHermannHellwagner
couldbe,isdirectlyrelatedtohowwelltheABRalgorithmperforms Table1:ABRLadderofVideoSequences.
underdifferentnetworkconditions.
Therearemanystudiesonthetopicofsubjectiveandobjective RepresentationIndex Resolution Bitrate(kbps)
QoEevaluation[13,16,34].Nevertheless,thesestudieswerecon-
1 320x240 235
ductedwithalimitednumberofparticipantsforthesubjective 2 384x288 375
evaluationsphase.Thereforetheresultsarealsonarrowanddonot 3 512x384 560
presentaclearpictureofanABRperformance’simpactonQoE 4 512x384 750
metrics.Incontrast,thispaperhasstudiedtheQoEanditsmetrics 5 640x480 1050
6 720x480 1750
(e.g.,selectedbitrate,stallevents,bitrateswitches,andstartupde-
7 1280x720 2350
lay)fromtwodifferentapproaches,whichgivesacomprehensive
8 1280x720 3000
insightintoABRalgorithms’performance.First,wehaveconducted 9 1920x1080 4300
224experimentswithvarioustestsequencesandvaryingnetwork 10 1920x1080 5800
conditionsusingsevenwell-knownheuristic-basedABRalgorithms. 11 1920x1080 7000
Second,wehaveconductedanextensivecrowdsourcedsubjective
qualityevaluationwith835participantsoverthesameexperiments
Weusedtwodifferentpartswith2minutesdurationfromeach
toprovideacomparativeanalysisoftheresults.
selectedtestsequencetoextendthedatasetvarieties.Eachvideo
Theremainderofthispaperisorganizedasfollows.Section2
wasencodedintoelevenrepresentationsusingtheencodingABR
coversadetaileddescriptionofthesetupwehaveusedtoconduct
ladderhighlightedinTable1.Thechoicesofbitratelevelsanden-
theobjectiveevaluation,thearchitectureanddesignofoursub-
codingconfigurationswerebasedonNetflix’srecommendation[22]
jectiveevaluationportal,theABRalgorithmsandmediaplayers
andApple’srecommendation[21]whichispresentedin[14].As
westudied,andthevideosequences’characteristicsalongsidethe
proposedin[14],wefollowedStreamroot’sencodingconfigura-
networkprofilesthatwehavedesignedtoconducttheexperiments.
tionrecommendation[4]toremovescenecutsandlimittheGoP
Section3highlightsourfindingsandresultsfromtheevaluations.
size.Twosecondssegmentsarewidelyusedinthedevelopmentof
Itmainlypresentsinvestigativestudyresultstogiveabetterun-
ABRs[27,43].
derstandingoftheheuristic-basedABRalgorithms’performance.
Section4summarizesrelatedwork,andSection5concludesthe
2.2 ABRAlgorithmsandMediaPlayers
paperwithpossiblefutureworkitems.
Inthelasttenyears,therehavebeenseveralstudiesinABRalgo-
2 EVALUATIONSETUP rithms–atvarioussophisticationlevels–thatusemultipleheuris-
ticssuchasthroughputprediction,bufferoccupancy,orhybrid.
Wehaveconductedbothobjectiveandsubjectiveevaluationsto
ThesealgorithmsformulatetheABRdecisionswithinmathemati-
studyvariousinfluentialQoEmetricssuchasstartupdelay,video
calframeworks(e.g.,gametheory,queuingtheory)orusevarious
quality,andstallevents.Thissectiondescribesvideosequences’
learning-basedtechniquestoperformABRdecisions.Here,weonly
characteristicsandnetworkprofilesforbandwidthshapingbetween
investigateafewexamples,andtheinterestedreadersareencour-
theclientandtheserver.Next,webrieflydescribesevenheuristic-
agedtoreadmoredetailsin[8].TherearesevenABRalgorithms
basedABRalgorithmsandthemediaplayersweusedtoexecute
andtwomediaplayersintotalusedfortheevaluations:dash.js
theassessments.Ourtestbedarchitecturewillbedescribedindetail,
v3.1.3[11](Dynamic)andShakav3.0.4 [17](Throughput-based)
followingourobjectiveandsubjectiveevaluationstudies’setups.
mediaplayersdefaultABRalgorithmsplusBBA0[20],BOLA[36],
Elastic[12],FastMPC[42],andQuetra[40].AllotherABRshave
2.1 VideoSequences
beenintegratedwithdash.jsreferenceplayer[11].Inthissection,
Wehaveselectedthefollowingopensourcemoviesasusedin[27] webrieflyrevieweachalgorithmasfollows:
fortheobjectiveandsubjectiveevaluationsandusedtheFFmpeg1
• dash.js[11]:dash.jsimplementsahybridABRalgorithmcalled
softwaretoencodeandpackagetheDASHcontentfollowingthe
Dynamic as default, a combination of throughput-based and
ABRladderinTable1.
BOLAalgorithms.Atthebeginningofastreamingsession,Dy-
(1) Sintel,theDurianOpenMovieProject2 namicstartsbyinvokingthroughput-basedtoselectthebitrate
(2) Valkaama3 basedonthroughputprediction.Oncethecurrentbufferlevel
(3) BigBuckBunny4 reaches10secondsorabove,Dynamictriggersaneventtoswitch
(4) TearsofSteel5 theABRalgorithmtoBOLA.Itswitchesbackagaintothethroughput-
Theabovevideosequencesareencodedandpackagedwiththe basedalgorithmwhenthebufferlevelfallsbelow10seconds.
followingparameters:AACforaudiocoding,AVC/H.264(x264)for • Shaka[17]:Shakaimplementsasimplethroughput-basedal-
videocoding,segmentdurationof2seconds,andgroup-of-pictures gorithmthatusesthroughputheuristicswithanExponential
(GoP)lengthof24frames,MP4segmenttype,andDASHformat. WeightedMovingAverage(EWMA)smoothingfunctiontoper-
formABRdecisions.
1https://ffmpeg.org,accessedNov.21,2020. • BBA0[20]:Itisabuffer-basedABRalgorithmthatusesthecur-
2https://durian.blender.org,accessedNov.21,2020. rentbufferoccupancytoselectthebitrateforthenextsegmentto
3http://www.valkaama.com,accessedNov.21,2020.
bedownloaded.Thisalgorithm’skeyelementisthebuffer-bitrate
4https://peach.blender.org,accessedNov.21,2020.
5https://mango.blender.org,accessedNov.21,2020. mapfunction,whichindicatesadiscretebijectiverelationfrom
84

UnderstandingQualityofExperienceofHeuristic-basedHTTPAdaptiveBitrateAlgorithms NOSSDAV’21,September28–October1,2021,Istanbul,Turkey
bufferleveltovideobitrate.Itusesareservoirthatallowsselect-
ingthelowestpossiblebitrateifthecurrentbufferoccupancy
8000
goesbelowthedefinedreservoirtoavoidstallevents.Atstartup, 7000
BBA0selectsthelowestvideobitrateasdefaulttospeedupthe 6000
rendering. When the buffer occupancy exceeds the reservoir 5000
volume,theplayerwillswitchtovideosegmentswithahigher 4000
3000
bitrate.Ittriestomaintainthebufferatsafelevels(betweenthe
2000
reservoirandmaximumbufferthreshold).
1000
• BOLA[36]:Itisabuffer-basedABRalgorithmthatformulates
ABRdecisionsasautilitymaximizationfunctionusingLyapunov
optimization.
• Elastic[12]ItisahybridABRthatusesfeedbackcontroltheory
thatgeneratesalong-livedTransportControlProtocol(TCP)
flowformoreaccuratethroughputpredictions,thus,betterABR
decisions.
• FastMPC[42]:ItisahybridABRalgorithmthatusesaModel
PredictiveControl(MPC)approach.TheMPCmodeltakesbuffer
occupancyobservationsandharmonicmeanthroughputpredic-
tionstoselectthebitrate,maximizingagivenQoEmetricovera
horizonoffivefuturesegments.
• Quetra[40]:Itisabuffer-basedABRthatformulatesABRdeci-
sionsasaqueuingtheorymodel,whichcalculatestheexpected
bufferoccupancygivenabitratechoice,networkthroughput,
andbuffercapacity.
2.3 NetworkProfiles
Wehavedesignedfournetworkprofilestoshapethetotalband-
widthcapacitybetweenthestreamingserverandtheplayer.Our
networkprofilescoverthecommonnetworkconnectionscenarios.
(i)RampUp,inwhichtheavailablebandwidthwillbeincreasedwith
anintervaloftensecondsstartingfrom372kbpsupuntil7170kbps
fortwominutes.(ii)RampDown,inwhichtheavailablebandwidth
willbedecreasedwithanintervaloftensecondsstartingfrom7170
kbpsdownto372kbpsfortwominutes.(iii)Fluctuation,inwhich
theavailablebandwidthwillbeswitchedcontinuouslybetween
theupperbound(7170kbps)andthelowerbound(372kbps)with
anintervaloftensecondsandoveraperiodoftwominutes.(iv)
Stable,inwhichtheavailablebandwidthwillbeconstantandsetto
3770kbpsfortwominutes.Figure1depictsthetimeseriesofthe
considerednetworkprofiles.Asproposedin[39],weenforceanet-
worklatencyof80millisecondsbetweentheclientandtheserver
tocoverabroadrangeofapplicationscenarios.Itcorrespondsto
whatcanbeobservedwithinTCP-basedlong-distancefixed-line
connectionsorreasonablemobilenetworks.
2.4 ObjectiveEvaluation
WeareusingCAdViSE6[38]asourtestbedtoconducttheobjective
evaluations.CAdViSEprovidesacloud-basedplatformtoevaluate
multipleABRalgorithmsormediaplayersundervariousnetwork
conditions.Forthisproject,wehaveaddednewfunctionalitiesto
CAdViSEthatmakethestreamingsessionsreproducible.Bystoring
theclientrequestsandmediaplayerevents7 assessionlogs,we
canreproducethesamestreamingsession,includingthestartup
delayandstallevents.Eachstreamingsessionthatwerefertoas
6https://github.com/cd-athena/CAdViSE,accessedApr.1,2021.
7https://html.spec.whatwg.org/multipage/media.html,accessedDec.7,2020.
01 02 03 04 05 06 07 08 09 001 011 021
Ramp Down Ramp Up Fluctuation Stable
8000
7000
6000
5000
4000
3000
2000
1000
kbp
s
s econd kbp
se
s cond
102030405060708090 100 110 120
Figure1:NetworkProfilesUsedintheExperiments.
anexperimentwillstoreitslogsinaDynamoDB 8table.Oncethe
experimentisfinishedforaparticularABRalgorithmormedia
playerwithaspecificnetworkshape,werunascript9thatfetches
thesessionlogsandstitchesthesegmentstogether.Weareusing
FFmpegtoconcatenatethevideoandaudiosegments.Usingthe
samesoftware,wecancuttheexactrequireddurationofafake
stallvideoandinjectitbetweentheactualvideosegments.When
theaudiovisualfilesarecombined,weuseITU-TP.1203Standalone
Implementation 10 [32,33]toextractaJSONfileasafeedtothe
P.1203model.Wethenadjustthestalldurationandalsothede-
finedresolutionintheproducedJSONfile.TheJSONfilewillbe
passedtothemodeltoretrievetheMeanOpinionScore(MOS).The
currentimplementationallowsustoconsiderallthestallevents
withadurationofmorethan0.001seconds.Anotherstepinthis
applicationistoconcatenatetheaudiovisualfiles(audioandvideo
files)usingFFmpegtohaveafinalmp4filereadyforthesubjective
evaluationphase.
2.5 SubjectiveEvaluation
Using Serverless Architecture 11 and AWS Lambda 12 we have de-
velopedaHAS-basedsubjectiveevaluationportal.Theportalis
implementedbasedonthedefinedstandardinITU-TP.910[25]
andthebestpracticesproposedin[18].Thissubsectiondescribes
thearchitecture,procedures,andmeasurementswedesignedto
conductsubjectiveevaluations.Wehavedevelopedacustomweb
mediaplayerbyleveragingtheHTML5mediaelement 13features.
WeuseAmazonMechanicalTurk 14(MTurk)toconductoursub-
jectiveevaluation.MTurkisacrowdsourcingwebsitetohirere-
motelylocatedcrowd-workerstoperformdiscreteon-demandtasks.
WesharethelinktooursubjectiveevaluationportalontheMTurk
platform.Whentheportal’smainentrypointisinvokedbybrows-
ingawebaddress,anAWSlambdafunctionwillreturntherequired
libraries,HTML,andJavaScriptfiles.Afterreadingtheinstruction,
theuserentersanidentitynumber(MTurkworkerid),creatinga
databaserecord.Next,theserverwillprepareamanifestfilespecific
totheuser.Outof224testsequencesproducedintheobjective
8https://docs.aws.amazon.com/dynamodb,accessedDec.7,2020.
9https://github.com/cd-athena/HASClipStitcher,accessedMar.30,2021.
10https://github.com/itu-p1203/itu-p1203,accessedDec.7,2020.
11https://www.serverless.com,accessedDec.7,2020.
12https://docs.aws.amazon.com/lambda,accessedDec.7,2020.
13https://w3.org/TR/2011/WD-html5-20110113/video.html,accessedDec.7,2020.
14https://www.mturk.com,accessedDec.8,2020.
85

NOSSDAV’21,September28–October1,2021,Istanbul,Turkey BabakTaraghi,AbdelhakBentaleb,ChristianTimmerer,RogerZimmermann,andHermannHellwagner
90
75 60
45
30
15
0
FastMPC Elastic BBA0 Quetra BOLA dash.js Shaka
Fluctuation 73.23 5.85 7.95 10.88 28.46 41.40 52.25
Ramp Down 30.63 8.35 6.18 10.33 11.29 21.29 34.90
Ramp Up 17.18 0.00 0.19 0.00 4.13 4.55 13.39
Stable 12.84 0.16 0.00 0.00 4.20 4.26 20.12
LLATS
.GVA
)DNOCES(
12
10 8
6
4
2
0
FastMPC Elastic BBA0 Quetra BOLA dash.js Shaka
Fluctuation 5.48 5.36 5.48 5.36 5.56 5.50 5.28
Ramp Down 5.56 5.29 5.41 5.43 5.57 5.54 5.40
Ramp Up 7.22 6.37 6.56 6.78 7.48 7.51 9.65
Stable 5.65 5.46 5.40 5.42 5.62 5.65 5.65
PUTRATS
.GVA
)DNOCES(
Figure2:Avg.StallDuration(left)andAvg.VideoStartupDelay(right).
evaluationphaseanduploadedtoanAWSS3 15 bucket,asetof predictionsintherangeof1to5.Outoffouravailablemodesinthis
10randomizedandprioritizedtestsequenceswillbeselectedand QoEmodel,weusedMode1inourevaluations,whichincludesbi-
lockedfor30minutesinthedatabaseandthenpresentedinthe trate,framerate,andresolution,plusframetypes,andframesizes
manifestfiletobeconsumedbythemediaplayer.Theprioritization incalculatingthepredictedMOS.ObjectiveMOSinFigures3,4,5,
algorithmworksbasedontotalvotesandthenumberofnotexpired and6showtheaveragevaluefromO46attributes(representing
requestedlocksforthatspecifictestsequence.Thecustommedia theoverallqualityscore)oftheP.1203modelachievedbydifferent
playerparsesthemanifestfileandstartsdownloadingthetestse- ABRs in various network profiles. The error bars represent the
quencesfromtheAWSS3bucket.Whenthefirsttestsequenceis 95%ConfidenceIntervals(CI)17forbothsubjectiveandobjective
fullydownloadedtotheclientbrowser,theplaybackstarts. MOS.Asnetworkprofilesarechallenging,theresultsshowninthe
Tostorethetestsequenceswithinthesubject’sdevice(i.e.,web mentionedfiguresarenotgoinguptothehighestpossibleQoE
browser),weuseIndexedDB 16.Whilethefirsttestsequenceisbeing score(5).Theaveragesofstalleventsdurationandvideostartup
played,theother9testsequenceswillstillbedownloadedinthe delayforeachABRalgorithmpernetworkprofileareshownin
backgroundwithoutinterruptingthecurrentplayback.Whenthe Figure2,whichcorrelatestotheobjectiveMOSlevelsshownin
playbackstopsandthevideoplayedsuccessfully(fortwominutes), Figures3,4,5,and6.Forinstance,inthefluctuationnetworkprofile,
adialogboxwillpopupandaskavideocontent-relatedquestion, BBA0andElasticABRalgorithmswiththehighestobjectiveMOS
i.e.,areliabilityquestion,toensurethatweonlycountthesubject’s alsohavethelowestaveragedurationforstallevents.Ascanbe
voteifshe/hehasactuallyobservedthevideo.Next,theuserwill observedinFigure2,theramp-upnetworkprofilepresentedin
beaskedtocastavoteonascaleof1to5,where1representsthe Figure1hasthehigheststartupdelaybecausetheshapednetwork,
worstexperienceand5standsforanexcellentexperience.These- inthiscase,startsfromthelowestavailablebandwidth.Inthefluc-
lectedscorewillbestoredinthedatabaseviaanotherAWSlambda tuationprofile,wecanseethattheFastMPC,dash.js,andShaka
functionbyclickingthesubmitbutton.Onceasubjectcastshis/her ABRalgorithmssufferfromwrongbandwidthestimation,leading
voteforatestsequence,thatexperimentidwillberemovedfrom tosub-optimalABRdecisionsand,therefore,highstallduration
thelockedarrayandstoredinthevotesarraymappedtothevoted andbadQoE.Incontrasttobuffer-basedABRslikeBBA0orQuetra,
scorealongsidetheanswertothereliabilityquestion.Attheend whichuseonlythebufferleveltoadapttonetworkconditions,the
oftheevaluationsession,wegenerateacompletioncode.Only ElasticABRalgorithmachievesthelowestaveragestallduration.
thosecrowd-workerswhocanprovidethecompletioncodewillbe Itutilizesarobustbandwidthestimatorthattrackstheavailable
compensated.Thesubjectiveevaluationportalwillaskthesubjects bandwidthefficiently.Asaresult,ElastictakessuitableABRde-
toscore10testsequences.Eachtestsequenceistwominutes,there- cisionsthatmaximizetheQoE.WealsonotethatobjectiveMOS
fore20minutesintotal.Plus,10minutesforreadingtheinstruction valuesforalltheABRsareprettylowinthefluctuationnetwork
anddownloadingthefirsttestsequenceaddsupto30minutes.If profileasthemodelpenalizesmuchforstallevents.
theuserstakemorethan30minutestocasttheirvotes,theycannot SubjectiveEvaluations:Thesetupforsubjectiveevaluations
becompensated,andalso,theirprovidedscorewillnotbecounted hasbeendescribedindetailinSection2.5.UsingtheMTurkplat-
inthefinalresults. form,wewereabletohave835participantsinoursubjectiveeval-
uationphase.Outofwhich,780participantshadatleastonevote
3 RESULTSANDFINDINGS withthecorrectanswertothecontent-relatedreliabilityquestion
andmanagedtocasttheirvotesbeforethesubmissiontimeout.
Thissectiondescribesourfindingsandresultsfromtheobjective
Wehavegathered5723votesintotal,outofwhich4704proved
andsubjectiveevaluationsandthecorrelationsandcontradictions
reliable(accordingtoreliabilityresponsesandothermeasurements
betweenthesetwoaspectsofvideostreamingassessment.
describedinSection2.5),whichcounts21votesforeachexperi-
ObjectiveEvaluations:Wehaveconductedtheobjectiveeval-
ment.Figures3,4,5,and6showtheaverageMOSforeachABR
uationwiththesetupdescribedinSection2.4.UsingtheITU-T
algorithmwithadifferentnetworkprofile.Tobetterunderstand
P.1203QoEmodel[32],wecalculateapredictedMOSofavideo
howthevoteshavebeendistributedamongdifferentABRalgo-
streamingsession.Thementionedmodelprovidesintegralquality
rithmswithvaryingnetworkprofiles,weputthenumberofvotes
15https://docs.aws.amazon.com/s3,accessedDec.7,2020.
16https://www.w3.org/TR/IndexedDB-2,accessedDec.7,2020. 17http://www.stat.yale.edu/Courses/1997-98/101/confint.htm,accessedDec.14,2020.
86

UnderstandingQualityofExperienceofHeuristic-basedHTTPAdaptiveBitrateAlgorithms NOSSDAV’21,September28–October1,2021,Istanbul,Turkey
Pearson's Correlation Coefficient 0.94 Pearson's Correlation Coefficient 0.84
| 5.00    |      |      |      |      |      |      |      | 5.00  |        |           |      |      |      |      |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ------ | --------- | ---- | ---- | ---- | ---- |
| 4 . 5 0 |      |      |      |      |      |      |      | 4 . 5 | 0      |           |      |      |      |      |
|         |      |      |      |      |      |      |      |       |        | 3.87 3.98 |      | 3.80 |      |      |
| 4 . 0 0 | 3.62 | 3.73 | 3.65 |      | 3.68 |      | 3.73 | 4 . 0 | 0 3.66 |           | 3.67 |      |      | 3.67 |
|         |      |      |      | 3.45 |      | 3.41 |      |       |        | 3.13      |      |      |      | 3.34 |
| 3.50    |      |      |      |      |      |      |      | 3.50  | 2.93   |           |      | 3.07 |      |      |
|         |      |      |      |      | 2.84 |      | 2.79 |       |        |           |      |      |      |      |
| 3.00    | 2.56 | 2.67 | 2.63 |      |      |      |      | 3.00  | 2.64   |           |      |      |      | 2.70 |
| 2.50    |      |      |      | 2.26 |      | 2.26 |      | 2.50  |        |           | 2.24 |      | 2.26 |      |
| 2.00    |      |      |      |      |      |      |      | 2.00  |        |           |      |      |      |      |
| 1.50    |      |      |      |      |      |      |      | 1.50  |        |           |      |      |      |      |
| 1.00    |      |      |      |      |      |      |      | 1.00  |        |           |      |      |      |      |
BBA0 BOLA dash.js Elastic FastMPC Quetra Shaka BBA0 BOLA dash.js Elastic FastMPC Quetra Shaka
|     |     |     | Objective MOS | Subjective MOS |     |     |     |     |     | Objective MOS |     | Subjective MOS |     |     |
| --- | --- | --- | ------------- | -------------- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | --- |
Figure3:Avg.QoEofABRsinRampUpNetworkProfile. Figure6:Avg.QoEofABRswithStableNetworkProfile.
Pearson's Correlation Coefficient 0.90 Stable Network Profile Ramp Down Network Profile
| 5.00 |      |      |      |      |      |      |      |              | 80  |     |              | 80  |     |     |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------------ | --- | --- | ------------ | --- | --- | --- |
| 4.50 |      |      |      |      |      |      |      | rebmuN setoV | 60  |     | rebmuN setoV | 60  |     |     |
| 4.00 |      | 3.65 |      |      |      |      |      |              | 40  |     |              | 40  |     |     |
|      | 3.48 |      | 3.48 |      | 3.48 |      | 3.45 |              |     |     |              |     |     |     |
|      |      |      |      | 3.26 |      | 3.26 |      |              | 20  |     |              | 20  |     |     |
3.50
| 3.00 |      | 2.43 | 2.33 |      |      |      |      |     | 0                  |     |     | 0   |                    |       |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | ------------------ | --- | --- | --- | ------------------ | ----- |
|      | 2.33 |      |      |      | 2.48 |      | 2.35 |     | 1 2                | 3 4 | 5   | 1   | 2                  | 3 4 5 |
| 2.50 |      |      |      | 2.00 |      | 2.00 |      |     | Mean Opinion Score |     |     |     | Mean Opinion Score |       |
2.00
|      |      |      |               |                |         |        |       |              | Ramp Up Network Profile |     |              | Fluctuation Network Profile |     |     |
| ---- | ---- | ---- | ------------- | -------------- | ------- | ------ | ----- | ------------ | ----------------------- | --- | ------------ | --------------------------- | --- | --- |
| 1.50 |      |      |               |                |         |        |       |              | 80                      |     |              | 80                          |     |     |
| 1.00 |      |      |               |                |         |        |       | rebmuN setoV | 60                      |     | rebmuN setoV | 60                          |     |     |
|      | BBA0 | BOLA | dash.js       | Elastic        | FastMPC | Quetra | Shaka |              |                         |     |              |                             |     |     |
|      |      |      |               |                |         |        |       |              | 40                      |     |              | 40                          |     |     |
|      |      |      | Objective MOS | Subjective MOS |         |        |       |              |                         |     |              |                             |     |     |
|      |      |      |               |                |         |        |       |              | 20                      |     |              | 20                          |     |     |
|      |      |      |               |                |         |        |       |              | 0                       |     |              | 0                           |     |     |
Figure4:Avg.QoEofABRsinRampDownNetworkProfile. 1 2 3 4 5 1 2 3 4 5
|     |     |     |     |     |     |     |     |     | Mean Opinion Score |                |      |         | Mean Opinion Score |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | -------------- | ---- | ------- | ------------------ | ----- |
|     |     |     |     |     |     |     |     |     | FastMPC            | Quetra Elastic | BBA0 | dash.js | BOLA               | Shaka |
Pearson's Correlation Coefficient 0.52
| 5.00 |     |     |     |     |     |     |     |     | Figure7:DistributionofSubjectiveMOSforABRs. |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
4.50
4.00
|      | 3.39 | 3.21 | 3.29 |      |      |      | 3.30 |     |     |     |     |     |     |     |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
| 3.50 |      |      |      | 3.12 | 3.10 | 3.08 |      |     |     |     |     |     |     |     |
theramp-upnetworkprofilethanitscompetitors.Thementioned
3.00
2.22 scenariocouldalsobeobservedinFigure5.Wehavecalculatedthe
| 2.50 |     |     | 1.99 | 2.07 |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.86 1.91 1.98 1.98 Pearsoncorrelationcoefficient18valuesforeachnetworkprofile
2.00
betweenthesubjectiveandobjectiveresults,showninthetopright
1.50
cornerofFigures3,4,5,and6.ThehigherthePearsoncorrelation
1.00
coefficientvalue,thebetterthesetwosetsofresultsarerelatedto
|     | BBA0 | BOLA | dash.js | Elastic | FastMPC | Quetra | Shaka |     |     |     |     |     |     |     |
| --- | ---- | ---- | ------- | ------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Objective MOS Subjective MOS eachotherintermsofstrengthanddirectionoflinearrelationships.
Pearson’scorrelationcoefficienthasarangeof-1to1.Inallcases,
wecanseeastrongcorrelationwithacoefficientvaluegreaterthan
Figure5:Avg.QoEofABRsinFluctuationNetworkProfile.
0.5.Adiscrepancyobservedbetweenthesubjectiveandobjective
evaluationresultscanbeseeninFigures3,4,5,and6wherethe
foreachABRalgorithmscoreinfourdiagramsshowninFigure7. subjectiveMOSisalmostalwayshigherthantheobjectiveMOS
Thenetworkprofiles’effectsonhowABRalgorithmsmakedeci- by one score. The discrepancy gets more unexpected when we
sionsaboutselectingtherepresentationsthatdirectlyinfluencethe seethatthecorrelationremainsperfectevenwiththisdifference.
participants’perceivedQoEareshowninFigure7. Theauthorsassumethatthisapparentdifferencecouldresultfrom
havingawidevarietyofparticipantsfromdifferentgeographical
| Correlations |     | and | Contradictions: |     | Looking | at Figure | 7 can |     |     |     |     |     |     |     |
| ------------ | --- | --- | --------------- | --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
giveaclearinsightintohowtheABRalgorithmsperformwith locations in which Internet connections differ from each other;
differentnetworkprofilescomparedtoeachother.Forexample, therefore, their expectations from delightful or annoying video
Shakamediaplayervotesareaccumulatedaroundthesecondscore streamingsessionsvarycomparedtowhatITU-TP.1203QoEmodel
| onourscaleof1to5,whichshowsweakperformanceforthis |     |     |     |     |     |     |     | haspredicted. |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
specificmediaplayerwithafluctuationnetworkprofile.Incontrast,
the same media player shows more robust performance within 18https://libguides.library.kent.edu/SPSS/PearsonCorr,accessedDec.13,2020.
87

NOSSDAV’21,September28–October1,2021,Istanbul,Turkey BabakTaraghi,AbdelhakBentaleb,ChristianTimmerer,RogerZimmermann,andHermannHellwagner
4 RELATEDWORK Buffer-basedABR.Usingonlybufferoccupancyheuristicstoper-
Wedividethissectionintotwoparts:QoEevaluationandABR formABRdecisions,BBA0[20],BOLA[36],andQuetra[40]were
algorithms. proposed.BBA0usesabuffer-ratemapfunctiontochoosethebi-
trate,adapttonetworkresourcevariations,andavoidstallevents.
BOLA formulates the bitrate decision as a utility maximization
4.1 QoEEvaluation
problembasedonLyapunovtheory.Itderivesanonlinecontrol
TherehavebeenseveralsurveysaboutQoEevaluationandhow
algorithmthatusesonlybufferoccupancy.Quetrausesaqueuing
toconductsubjectiveandobjectivetests[1,3,31,35].Here,we
theorymodeltoformulateABRdecisionstokeepthebufferwithin
listafewofthesetechniques.Barakovićetal.[3]didasurveyand
asaferegion.
investigationoverthestate-of-the-artresearchactivitiescovering
HybridABR.ThisABRalgorithmclassusesvariousheuristics
thefieldofQoEmanagement.Theirstudy’sprimaryfocusison
suchasthroughput,buffer,andlatencyintheirABRformulation
wirelessnetworksandaddressingthreemanagementaspects:QoE
model.Benefitingfromgameandconsensustheories,Bentalebet
modeling,monitoringandmeasurement,andadaptationandopti-
al.[5,6]developedagametheoryABRscheme(GTA)forDASHsys-
mization.Moreover,theyprovidedanin-depthdiscussiononthe
tems.GTAusesbandwidthprediction(PANDA[28]andCS2P[37])
keyelements,andchallengesresearchersdealwithinthisarea.
andbufferleveltoformulateABRdecisionsasabargainingandcon-
AnothercomprehensivesurveyinQoE’sareafocusingonHAS
sensusmechanism,wheretheplayersformanagreementamong
techniquesispresentedin[35]bySeufertetal.inwhichauthors’
themselves.DeCiccoetal.[12]proposedafeedbacklinearization
maincontributionistoinvestigateworksrelatedtoQoEfromthe
adaptivestreamingcontroller(Elastic)thatleveragesfeedbackcon-
human-computerinteractionandnetworkingdomain.Subjective
troltheoryandtheHarmonicalgorithmtoprovideahighlevel
studiesthatcovertheQoEaspectofadaptationdimensionsand
offairnessandbandwidthutilization.Yinetal.[42]developedan
strategiesarestudied.TechnicalinfluencefactorsofHASareiden-
MPCalgorithmcombiningavailablebandwidthmeasurements(har-
tifiedalongsideopenissuesandconflictingresults.Mitraetal.[31]
monicmean[26])andbufferoccupancytoperformABRdecisions.
didanextensivestudyonhowQoEmeasurementscouldhelpvideo
Learning-basedABR.ThisclassofABRalgorithmsusesoneof
streaming,VoiceoverIP(VoIP),andvideogamingend-usersin
the learning rules that consider multiple heuristics as input to
availingpersonalizedservicesfromserviceproviders.Theyhave
learningthebestbitratetoselect.Maoetal.[30]developedadeep
exploredthestrengthsandshortcomingsofexistingtechniques
reinforcementlearningABRscheme,termedPensieve,thatgradu-
inQoEassessments.AlreshoodiandWoods[1]investigatedsome
allylearnsthebestpolicyforABRdecisionsthroughobservations
currentcorrelationmodelsbriefly.Theyhavestudiedcorrelation
(i.e.,networkconditionsandplayerQoEmetrics)andexperience.
modelsthatattempttomapQualityofService(QoS)toQualityof
Inthesamecontext,Yanetal.[41]developedFugu,anABRthat
Experience(QoE)formultimediaservices.Authorsclaimthatmost
usessupervisedlearninginsitu,withdatafromrealdeployment
oftheexistingqualitymodelsformultimediaprovideonlyapartial
environments,totrainaprobabilisticpredictorofupcomingseg-
solutionforpredictingtheactualQoEfromagivenQoS.
menttransmissiontimes.ThismoduletheninformsanMPCcontrol
policytoperformABRdecisions.Tianchietal.[19]designedStick,
4.2 ABRAlgorithms anABRalgorithmthatcombinesadeepreinforcementlearning
Existingclient-drivenABRalgorithms[8]canbeclassifiedintofour techniquewiththetraditionalbuffer-basedapproach.Itaimsto
maincategoriesbasedontheheuristicsandmechanismsusedto trainaneuralnetwork,whichoutputssuitablebufferboundsto
performABRdecisions:(𝑖)throughput-based,(𝑖𝑖)buffer-based,(𝑖𝑖𝑖) controlabuffer-basedABRtomaximizeQoE.
hybrid,or(𝑖𝑣)learning-based.ABRsin(𝑖to𝑖𝑖𝑖)useheuristicssuch
asthroughput,buffer,andmixed,respectively,andformulatethe
ABRdecisionsasmathematicalrulesorapproximationstomaxi- 5 CONCLUSIONSANDFUTUREWORK
mizeQoE.Incontrast,ABRsin(𝑖𝑣)trytolearnfromthesystem Inthisstudy,weasked,“howdoheuristic-basedABRalgorithms
environmentandfindsuitablepoliciesbasedonpastplayerstatus, performunderdifferentnetworkconditions?”Toexplorethisques-
henceadaptingtothesystemdynamics. tion,wehaveconductedextensivecrowdsourcedsubjectiveevalu-
Throughput-basedABR.Thisclassofalgorithmsusesthrough- ationsthataimtoprovideanunderstandingofhowwellasetof
putpredictionheuristicsasaninputtoperformABRdecisions. heuristics-basedABRalgorithmsperformwithdifferentnetwork
Li et al. [28] developed the Probe AND Adapt (PANDA) bitrate profiles.Theseevaluationsthenhavebeencomparedtoobjectiveas-
adaptationsolution,whichtriestoaddressthebandwidthoveresti- sessmentswiththeITU-TP.1203QoEmodel.Wehavestudiedhow
mationproblemwhenmultipleDASHplayerscompeteatanetwork wellanumberofknownABRalgorithmsmakebitratedecisions
bottleneck.Thisisachievedbyprobingthenetworkduringoffpe- withdifferentnetworkprofiles,ramp-up,ramp-down,fluctuating,
riodstomeasurethefair-sharebandwidthaccurately.Similarly, andstable.Wehaveexaminedthecorrelationsandcontradictions
Festive[26]triestoaddressthesameproblemasPANDA.Ituses betweentheABRalgorithms’subjectiveandobjectiveevaluations.
aharmonicmeanalgorithmthatconsiderstwentymeasurement Asfuturework,wesuggestadeeperinvestigationintothediffer-
samplestopredicttheavailablebandwidthandperformABRde- encesorcontradictionsshowninsubjectiveandobjectiveevalu-
cisions.Manglaetal.[29]designedabandwidthprediction-aware ationsintheresultsandfindingsinSection3.InvestigatingABR
ABRschemecalledCrystalBallformobileDASH.CrystalBallaims algorithms’performancefromsubjectiveandobjectiveevaluation
toimprovetheviewerQoEwhileprovidinglong-termhorizonpre- perspectivesusingtherecommendationsfromITU-TP.1401[24]is
dictionsandmitigatingpredictionerrors. anothersuggesteddirectionforfuturework.
88

UnderstandingQualityofExperienceofHeuristic-basedHTTPAdaptiveBitrateAlgorithms NOSSDAV’21,September28–October1,2021,Istanbul,Turkey
ACKNOWLEDGMENTS com/library/content/technotes/tn2224/_index.html
|     |     |     |     |     |     | [22] NetflixInc.2015.Per-TitleEncodeOptimization. |     |     |     | RetrievedNov21,2020from |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | ----------------------- | --- |
ThefinancialsupportoftheAustrianFederalMinistryforDigi-
http://techblog.netflix.com/2015/12/per-title-encode-optimization.html
talandEconomicAffairs,theNationalFoundationforResearch, [23] ISO/IEC.2014.23009-1:2014–DynamicadaptivestreamingoverHTTP(DASH)
–Part1:Mediapresentationdescriptionandsegmentformats.https://www.iso.
TechnologyandDevelopment,andtheChristianDopplerResearch
org/standard/65274.html.
Associationisgratefullyacknowledged.ChristianDopplerLabora-
|     |     |     |     |     |     | [24] PITU-T.2020. | Methods,metricsandproceduresforstatisticalevaluation, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | ----------------------------------------------------- | --- | --- | --- | --- |
toryATHENA:https://athena.itec.aau.at/.Thisresearchhasbeen qualificationandcomparisonofobjectivequalitypredictionmodels(P.1401).
http://handle.itu.int/11.1002/1000/14159.ITU-TRecommendation(2020).
supported in part by the Singapore Ministry of Education Aca- [25] PITU-TRecommendation.1999.Subjectivevideoqualityassessmentmethods
demicResearchFundTier2underMOE’sofficialgrantnumber formultimediaapplications.Internationaltelecommunicationunion(1999).
MOE2018-T2-1-103. [26] JunchenJiang,VyasSekar,andHuiZhang.2012.Improvingfairness,efficiency,
andstabilityinhttp-basedadaptivevideostreamingwithfestive.InProceed-
ingsofthe8thInternationalConferenceonEmergingnetworkingexperimentsand
| REFERENCES    |                            |                     |                 |                   |                                | technologies.97–108.                                            |     |     |     |     |         |
| ------------- | -------------------------- | ------------------- | --------------- | ----------------- | ------------------------------ | --------------------------------------------------------------- | --- | --- | --- | --- | ------- |
|               |                            |                     |                 |                   |                                | [27] StefanLederer,ChristopherMüller,andChristianTimmerer.2012. |     |     |     |     | Dynamic |
| [ 1 ] M o h a | m m e d A l r e sh o o d i | a n d J o h n W o o | d s . 2 0 1 3 . | S u r v e y o n Q | o E \ Q o S c o rr e l a t ion |                                                                 |     |     |     |     |         |
m o d e l s f o r m u l t i m e d i a s e r v i c e s. ( 2 0 1 3 ) . a d a p tiv e s t r e a m i n g o v e r H TTPdataset.InProceedingsofthe3rdmultimedia
|                 |                           | a rX i                 | v p r e p r in t    | a r X iv : 1 3 0 6. 0  | 2 2 1                           | sy s t em | s C o n f e r en c e .8 | 9 – 9 4 . |     |     |     |
| --------------- | ------------------------- | ---------------------- | ------------------- | ---------------------- | ------------------------------- | --------- | ----------------------- | --------- | --- | --- | --- |
| [ 2 ] A p p l e | . 2 0 1 6 . H T T P L i v | e S t r e a m in g . h | t t p s : / / d e v | e l o p e r .a p p l e | . c o m / s t r e a m i n g / . |           |                         |           |     |     |     |
[28] ZhiLi,XiaoqingZhu,JoshuaGahm,RongPan,HaoHu,AliCBegen,andDavid
[3] SabinaBarakovićandLeaSkorin-Kapov.2013. SurveyandchallengesofQoE Oran.2014.Probeandadapt:RateadaptationforHTTPvideostreamingatscale.
| m a na | g e m e n t i ss u e s in | w ir e l essnetworks. | JournalofComputerNetworksand |     |     |            |                      |               |                    |                           |                  |
| ------ | ------------------------- | --------------------- | ---------------------------- | --- | --- | ---------- | -------------------- | ------------- | ------------------ | ------------------------- | ---------------- |
|        |                           |                       |                              |     |     | I E E E Jo | ur n a l o n Se l ec | t ed A re a s | i n C o m m u n ic | a ti o n s 32 , 4 (2 01 4 | ),7 1 9 – 7 3 3. |
Co m m u n ic a t io n s 2 0 13 (2 01 3 ) . [29] T a r un M a n g l a ,N a w a n ol T h e e r a- A m p o rn p u n t , M o st a fa A m m a r, E l le n Zegura,
[4] EricaBeavers.2014.HowtoEncodeMulti-BitrateVideosinMPEG-DASHforMSE
|          |                           |                     |               |                      |                             | andSaurabhBagchi.2016. |     | Videothroughacrystalball:Effectofbandwidth |     |     |     |
| -------- | ------------------------- | ------------------- | ------------- | -------------------- | --------------------------- | ---------------------- | --- | ------------------------------------------ | --- | --- | --- |
| B a s ed | M ed i a P la y e r s . R | e tr i e v ed N o v | 2 1 , 2 0 2 0 | fr o m h tt p s : // | b l o g . s tr e amroot.io/ |                        |     |                                            |     |     |     |
predictionqualityonadaptivestreaminginmobileenvironments.InProceedings
en c o de -m u l ti -b it r a t e -v id e o s - m pe g -d a s h - m s e -b a s ed- m e d i a - p l a y e r s / ofthe8thInternationalWorkshoponMobileVideo.1–6.
[5] AbdelhakBentaleb,AliCBegen,SaadHarous,andRogerZimmermann.2018.
[30] HongziMao,RaviNetravali,andMohammadAlizadeh.2017.Neuraladaptive
WanttoplayDASH?Agametheoreticapproachforadaptivestreamingover v id e o s tr e a m i ng w it h pe n s iev e . In
H T T P .I n e. 1 3 – 2 6 . P r o ce e d i n g s o f th eConferenceoftheACMSpecial
P r o ce ed in g so f th e 9 th A C M M ul ti m ed ia S ys te m s C on fe re n c In te r es t G r o u p on D a ta C o m m u n ic a t io n . 1 9 7 – 2 1 0 .
| [6] Ab d e lh | a k B e n ta le b, A li | C B e g en , S aad | H a r ou s, | an d R o g er | Z im m e r m a n n . 2 0 19. |     |     |     |     |     |     |
| ------------- | ----------------------- | ------------------ | ----------- | ------------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
G am e o f St r e a m i n g P la y e r s: I s C on s e n su s V i a b le o r a n I l lu s io n ? [31] KaranMitra,ArkadyZaslavsky,andChristerÅhlund.2014. QoEmodelling,
|     |     |     |     |     | A C M T ra n s a c ti o n s | m e a s u | r e m e n t a n d pr e | d ic tio n : | A r e v i e w .a |     | (2 0 1 4 ) . |
| --- | --- | --- | --- | --- | --------------------------- | --------- | ---------------------- | ------------ | ---------------- | --- | ------------ |
o n M ul t im e d i a C o m p u t in g , C o m m u n i ca ti on s , a n d A p p li c a ti o n s 15 , 2 s(2 0 1 9) , 1 – 3 0 . r X i v p r e pr i n t a r X i v :1 4 1 0 .6 9 5 2
|     |     |     |     |     |     | [32] Al e x a | n d e r R a a k e ,M a | r ie -N e ig e | G a r c i a ,W e r | n e r R o b it z a , P e t e r | L i st , S t e ve G ö r i n g, |
| --- | --- | --- | --- | --- | --- | ------------- | ---------------------- | -------------- | ------------------ | ------------------------------ | ------------------------------ |
[7] AbdelhakBentaleb,AliCBegen,andRogerZimmermann.2016. SDNDASH: andBernhardFeiten.2017.Abitstream-based,scalablevideo-qualitymodelfor
ImprovingQoEofHTTPadaptivestreamingusingsoftwaredefinednetworking.
|     |     |     |     |     |     | H T T P | ad ap ti v e st re a | m in g : I T U | - T P . 1 20 3 .1 . | I n N in t h I n t e rn at i | o n a l C o n f e r e n c e o n |
| --- | --- | --- | --- | --- | --- | ------- | -------------------- | -------------- | ------------------- | ---------------------------- | ------------------------------- |
In P r oceedingsofthe24thACMInternationalConferenceonMultimedia.1296–
1 30 5 . Qu a li ty of M u l tim e d ia E x p er i en c e ( Q o M E X ) . I EE E , E rf u r t . h t t p :/ / ie e e x p l o r e .i e e e.
org/document/7965631/
[8] AbdelhakBentaleb,BayanTaani,AliCBegen,ChristianTimmerer,andRoger
[33] WernerRobitza,SteveGöring,AlexanderRaake,DavidLindegren,Gunnar
Zimmermann.2018.Asurveyonbitrateadaptationschemesforstreamingmedia Heikkilä,JörgenGustafsson,PeterList,BernhardFeiten,UlfWüstenhagen,Marie-
overHTTP.IEEECommunicationsSurveys&Tutorials21,1(2018),562–585.
|     |     |     |     |     |     | NeigeGarcia,KazuhisaYamagishi,andSimonBroom.2018. |     |     |     |     | HTTPAdaptive |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | ------------ |
[9] Bitmovin.2020.2020VideoDeveloperReport.https://go.bitmovin.com/video-
developer-report-2020. StreamingQoEEstimationwithITU-TRec.P.1203–OpenDatabasesandSoft-
ware.In9thACMMultimediaSystemsConference.Amsterdam.
[10] KjellBrunnström,SergioArielBeker,KatrienDeMoor,AnnDooms,Sebastian
|     |     |     |     |     |     | [34] Kalpana | Seshadrinathan, | Rajiv | Soundararajan, | Alan Conrad | Bovik, and |
| --- | --- | --- | --- | --- | --- | ------------ | --------------- | ----- | -------------- | ----------- | ---------- |
Egger,Marie-NeigeGarcia,TobiasHossfeld,SatuJumisko-Pyykkö,Christian LawrenceKCormack.2010.Studyofsubjectiveandobjectivequalityassessment
Keimel,Mohamed-ChakerLarabi,etal.2013.Qualinetwhitepaperondefinitions
ofvideo.IEEETransactionsonImageProcessing19,6(2010),1427–1441.
ofqualityofexperience.(2013).
[11] DASH-IF.2020.dash.js.[Online]Available:https://reference.dashif.org/dash.js/. [35] MichaelSeufert,SebastianEgger,MartinSlanina,ThomasZinner,TobiasHoßfeld,
andPhuocTran-Gia.2014.AsurveyonqualityofexperienceofHTTPadaptive
[12] LucaDeCicco,VitoCaldaralo,VittorioPalmisano,andSaverioMascolo.2013.
streaming.IEEECommunicationsSurveys&Tutorials17,1(2014),469–492.
Elastic:aclient-sidecontrollerfordynamicadaptivestreamingoverHTTP [36] KevinSpiteri,RahulUrgaonkar,andRameshKSitaraman.2020.BOLA:Near-
| ( D A SH | ) . In 2 0 1 3 2 0t h I nt | e rn a tio n al P a | c k e t V id e o | W o r k sh o p . I | E E E ,1 –8 . |     |     |     |     |     |     |
| -------- | -------------------------- | ------------------- | ---------------- | ------------------ | ------------- | --- | --- | --- | --- | --- | --- |
optimalbitrateadaptationforonlinevideos.IEEE/ACMTransactionsonNetwork-
| [13] Z h en gf | a n g D u a n m u , W | e n ta o L iu , Z h | u o r a n L i ,D | i q i C h e n , | Z h o u W a ng,Yizhou |     |     |     |     |     |     |
| -------------- | --------------------- | ------------------- | ---------------- | --------------- | --------------------- | --- | --- | --- | --- | --- | --- |
Wang,andWenGao.2020. AssessingtheQuality-of-ExperienceofAdaptive ing28,4(2020),1698–1711.
[37] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,Tao
BitrateVideoStreaming.arXivpreprintarXiv:2008.08804(2020).
|     |     |     |     |     |     | Liu,andBrunoSinopoli.2016. |     |     | CS2P:Improvingvideobitrateselectionand |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | -------------------------------------- | --- | --- |
[14] ZhengfangDuanmu,AbdulRehman,andZhouWang.2018. AQuality-of- a d a p ta t i o n w i t h d a t a - d r iv e n t h r o u g h p u t p re d ic tio n . I n
E x p e r ien ce D a ta b as e fo r A d a p ti v e VideoStreaming.IEEETransactionsonBroad- P r o ce ed in g s o f th e 20 1 6
|           |                         |                   |     |     |     | A C M | S I G C O M M C o n f | e r e n c e . 2 7 | 2 – 2 8 5 . |     |     |
| --------- | ----------------------- | ----------------- | --- | --- | --- | ----- | --------------------- | ----------------- | ----------- | --- | --- |
| ca s ti n | g 64 ,2 ( Ju n e 2 01 8 | ), 47 4 – 4 8 7 . |     |     |     |       |                       |                   |             |     |     |
[15] Ericsson. 2020. Ericsson Mobility Report. https://www.ericsson.com/ [38] B a b ak T a r a g h i , A n a t o l i y Z a b r o v s k i y , C h ri st ia n T im m e r e r, a n d H er m a n n H e llw a g -
ner.2020.CAdViSE:cloud-basedadaptivevideostreamingevaluationframework
4adc87/assets/local/mobility-report/documents/2020/november-2020-ericsson-
fortheautomatedtestingofmediaplayers.InProceedingsofthe11thACMMulti-
mobility-report.pdf. mediaSystemsConference.349–352. https://doi.org/10.1145/3339825.3393581
| [16] DeeptiGhadiyaram,JanicePan,andAlanCBovik.2017. |     |     |     |     | Asubjectiveand |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
[39] ChristianTimmerer,MatteoMaiero,andBenjaminRainer.2016.Whichadapta-
objectivestudyofstallingeventsinmobilestreamingvideos.IEEETransactions
2 9 , 1 ( 2 0 1 7 ) , 1 8 3 – 1 97 . tionlogic?AnobjectiveandsubjectiveperformanceevaluationofHTTP-based
o n C ir c u it s a n d S y s te m s f o r V id e o T e ch n o l o g y adaptivemediastreamingsystems.arXivpreprintarXiv:1606.00341(2016).
| [17] G oo g le | . 2 0 2 0 . Sh a k a P la | y e r . [O n l in e ] A | v a i la b le : h | t tp s : // g i t h u | b .c o m / google/shaka- |     |     |     |     |     |     |
| -------------- | ------------------------- | ----------------------- | ----------------- | --------------------- | ------------------------ | --- | --- | --- | --- | --- | --- |
player. [40] PraveenKumarYadav,ArashShafiei,andWeiTsangOoi.2017. Quetra:A
queuingtheoryapproachtoDASHrateadaptation.InProceedingsofthe25th
[18] TobiasHossfeld,ChristianKeimel,MatthiasHirth,BrunoGardlo,JulianHabigt,
ACMInternationalConferenceonMultimedia.1130–1138.
KlausDiepold,andPhuocTran-Gia.2013.BestpracticesforQoEcrowdtesting: [41] FrancisYYan,HudsonAyers,ChenzhiZhu,SadjadFouladi,JamesHong,Keyi
| QoEassessmentwithcrowdsourcing. |     |     | IEEETransactionsonMultimedia16,2 |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhang,PhilipLevis,andKeithWinstein.2020.Learninginsitu:arandomized
(2013),541–558.
[19] TianchiHuang,ChaoZhou,Rui-XiaoZhang,ChengleiWu,XinYao,andLifeng experimentinvideostreaming.In17th{USENIX}SymposiumonNetworked
SystemsDesignandImplementation({NSDI}20).495–511.
| Sun.2020. | Stick:AHarmoniousFusionofBuffer-basedandLearning-based |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[42] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.Acontrol-
A p p r o a c h f o r A d a p t i v e S t r e a m i n g . I n I E E E I N FO C O M 20 2 0- IE E E C o n f e re n ce o n t h e or e ti c ap p ro a ch for d y n a m ic ad ap t i ve v id e o st r e a m i n g overHTTP.InProceed-
|     |     | . I E E E , 1 9 6 | 7 – 1 9 7 6 . |     |     |     |     |     |     |     |     |
| --- | --- | ----------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
C o m p u t e r C o m m u n i c a t io n s in g s o f t he 2 01 5 A CM C o n fe r en ce on S I G C O M M . 3 2 5 – 3 3 8 .
| [20] Te - Y u | a n H u a n g , R a m e s | h J o h a ri , N i c k | M c K e o w | n, M a tth e w | T ru n n e ll , a n d M a r k |     |     |     |     |     |     |
| ------------- | ------------------------- | ---------------------- | ----------- | -------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
Watson.2014.Abuffer-basedapproachtorateadaptation:Evidencefromalarge [43] AlexZambelli.2009. SmoothStreamingTechnicalOverview. RetrievedNov
21,2020fromhttps://docs.microsoft.com/en-us/iis/media/on-demand-smooth-
videostreamingservice.InProceedingsofthe2014ACMConferenceonSIGCOMM.
streaming/smooth-streaming-technical-overview
| [21] AppleInc.2016.   | BestpracticesforcreatinganddeployingHTTPlivestreaming |                                                 |     |     |     |     |     |     |     |     |     |
| --------------------- | ----------------------------------------------------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mediaforappledevices. |                                                       | RetrievedNov21,2020fromhttps://developer.apple. |     |     |     |     |     |     |     |     |     |
89