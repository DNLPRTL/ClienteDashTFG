Beyond Throughput: a 4G LTE Dataset with Channel and
Context Metrics
DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,CormacJ.Sreenan
DepartmentofComputerScience,UniversityCollegeCork,Cork,Ireland
{d.raca,j.quinlan,a.zahran,cjs}@cs.ucc.ie
ABSTRACT 1 INTRODUCTION
Inthispaper,wepresenta4Gtracedatasetcomposedofclient-side Sincethedawnofthefirstwirelesscellularnetworkinlate70’s
cellularkeyperformanceindicators(KPIs)collectedfromtwomajor mobilenetworkevolutionhasexploded,resultingincapabilities
Irishmobileoperators,acrossdifferentmobilitypatterns(static, andservicesbeyondtheoriginalvoicecommunicationdesign.Forty
pedestrian,car,busandtrain).The4Gtracedatasetcontains135 yearslater,mobilehandsetsarepartofoureverydayroutinewith
traces,withanaveragedurationoffifteenminutespertrace,with awidevarietyofuse cases,includingofficerelatedtasks(read-
viewablethroughputrangingfrom0to173Mbit/satagranularity ingandsendingemails,makingappointments),textmessaging,
ofonesamplepersecond.Ourtracesaregeneratedfromawell- webbrowsing,playinggamesand,consumingmultimediacontent.
knownnon-rootedAndroidnetworkmonitoringapplication,G- Mobiledeviceusagehasrisenfrom10%in2011tojustover36%
NetTrackPro.Thistoolenablescapturingvariouschannelrelated by2018[20],withmobiledatatrafficgrowing18xoverthelast
KPIs, context-related metrics, downlink and uplink throughput, fiveyears.Furthermore,cellulardata(4G)accountedfor69%ofall
andalsocell-relatedinformation.Tothebestofourknowledge, mobiletrafficin2016,while3Gaccountedfor24%,whilecellular
thisisthefirstpubliclyavailabledatasetthatcontainsthroughput, speedsgrew3xfromanaverageof2Mbit/sin2015to6.8Mbit/sin
channelandcontextinformationfor4Gnetworks. 2016[5].Withtheseratesexpectedtogrowbyordersofmagnitude
Tosupplementourreal-time4Gproductionnetworkdataset,we whenthenextiterationofthecellularstandard,knownas5G,is
alsoprovideasyntheticdatasetgeneratedfromalarge-scale4G deployedin2020.
ns-3simulationthatincludesonehundredusersrandomlyscat- Howevercurrent4Gdatathroughputratescanfluctuateover
teredacrossaseven-cellcluster.Thepurposeofthisdatasetisto aperiodoffewseconds,dueprimarilytoschedulingdecisionsat
provideadditionalinformation(suchascompetingmetricsforusers thecelltower,andsuddenchangesintheunderlyingradiochannel.
connectedtothesamecell),thusprovidingotherwiseunavailable Thesechangesarecausedbyinter-cellinterference,congestiondue
informationabouttheeNodeBenvironmentandschedulingprin- toanumberofdevicespercell,andlocationofthedevicerela-
ciple,toenduser.Inadditiontothisdataset,wealsoprovidethe tivetothecelledge.Thisthroughputvariationisinherentlyapart
codeandcontextinformationtoallowotherresearcherstogenerate oftheunderlyingcommunicationsystemsincethefirstwireless
theirownsyntheticdatasets. networksandwillbefurtherexacerbatedin5Gduetotechnical
issuessuchasnon-lineofsightandareductioninoveralltrans-
CCSCONCEPTS missiondistance.Thisvariationsinthroughputcanlimittheuser
•Informationsystems→Multimediastreaming;•Networks QualityofExperience(QoE),especiallywhentheycausevisible
→PublicInternet;Wirelessaccessnetworks;Networkmea- degradationinviewablequalityascanoccurwhilestreamingaudio
surement; orvideo.Underlyingnetworkprotocolscanmitigatetheseissues,
suchasTCPwhosedesignreflectsthroughputvariationbyembed-
KEYWORDS dinganexponentialmovingaverage(EWMA)statistictoadaptto
rate-distortion[6].Additionally,adaptationalgorithmsproposed
Dataset,4G,LTE,ns-3,Mobility,throughput,contextinformation,
forHTTPAdaptivestreaming(HAS)[21]canfurthercombatthe
adaptivevideostreaming
challengeofconsistentqualitythroughbufferingandgracefuladap-
ACMReferenceFormat: tationofvideoquality.Oneofthemainhurdlesfortheseadaptation
DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,CormacJ.Sreenan.2018. algorithmsisalackofabroadcellulardatasetthatcapturesthese
BeyondThroughput:a4GLTEDatasetwithChannelandContextMetrics. throughputvariations,especiallywhencombinedwithchannel
InMMSys’18:9thACMMultimediaSystemsConference,June12–15,2018,
andcontextmetrics,onwhichasolutioncanbedesignedandcom-
Amsterdam,Netherlands.ACM,NewYork,NY,USA,6pages.https://doi.
paredwithotherstate-of-artalgorithms.Recently,researchershave
org/10.1145/3204949.3208123
recognisedthisproblem,whichresultedinanumberofdatasets
collectedoverdifferentwirelesstechnologiesandvideocontent
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed datasets[18].
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation Inthispaper,wepresenttwodatasets:thefirstcollectedfrom
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish, real4Gproductionnetworksandthesecondasyntheticdataset
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora generatedfromalarge-scale4Gns-3[2]simulation.Inourpro-
fee.Requestpermissionsfrompermissions@acm.org. ductiondataset,wecollectedtracesfromtwomajorIrishmobile
MMSys’18,June12–15,2018,Amsterdam,Netherlands
operators,withdifferentmobilitypatterns(static,pedestrian,car,
©2018AssociationforComputingMachinery.
ACMISBN978-1-4503-5192-8/18/06...$15.00
https://doi.org/10.1145/3204949.3208123
460

MMSys’18,June12–15,2018,Amsterdam,Netherlands DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,CormacJ.Sreenan
busandtrain).Relativetoourresearchintoadaptivevideostream- mobilitypatterns,foot,bicycle,bus,tram,train,andcar.However,
ing,ourinitialgoalistoprovideastandarddatasetplatformfor allthesetracesfocusonacquiringthroughputvalueswithhigh
comparisonofvariousHASstreamingapproaches.However,in samplegranularity.Eventhoughcollectedinawirelessenviron-
additiontothroughputvalues,wealsocollectedinformationabout ment,noneofthepreviousdatasetscontainanyinformationabout
channelconditionfortheclientinrespecttoservingeNodeBand thecellularchannel.Incomparisontothesepapers,ourdataset
neighbouringcells,GPSpositionsoftheclientandservingeNodeB, includesrepeatedtrailsaswellasone-secondsamplinggranularity
client’sspeed,andhandoverevents.Allofthisinformationallows fromamorediversesetofroutes(bus,pedestrian,trainandcom-
amulti-purposeanalysisbeyondouroriginalHASusecases,such muteroutes)coupledwithbothchannelandcontextmetricsfor
ashandoverprediction,coverageanalysis,mobilitypredictionetc. improvedcellularanddevicefeedback.
Whileinoursyntheticdataset,weutilisealarge-scale4Gns-3simu- In our research, these datasets provide sufficient throughput
lationthatincludes100usersrandomlyscatteredacrossaseven-cell informationtoevaluatetheperformanceofstate-of-artHASalgo-
cluster.Thepurposeofthesyntheticdatasetistoprovideadditional rithmsthatdeterminethestreamedvideoqualityinresponseto
information(competingmetricsforusersconnectedtothesame changesintheoperatingconditions.Thesealgorithmstypically
cell),abstractingeNodeBenvironmentandschedulingprinciples, adoptarate-basedandbuffer-basedstrategy.Rate-basedalgorithms
andultimatelyprovideameansoflarge-scaleevaluationofkeyper- basetheirdecisionforthenextchunkrateonaseriesoftheprevi-
formanceindicatorsinmulti-cellmobilityscenarios.Tothebestof ouslydownloadedchunk’sthroughput,withFESTIVE[10]being
ourknowledge,ourproductiondatasetisthefirstpubliclyavailable awell-knownalgorithmutilisingarate-basedapproach.Buffer-
datasetthatcontainsthroughput,channelandcontextinformation based algorithms map playback buffer levels to the throughput
for4Gnetworks. rateforthenextsegment.BBA-1andBOLA[8,19]areoneofa
Theremainderofthispaperisorganisedasfollows.Section2 numberofalgorithmsthatrelyonthistechnique.However,most
describesrelatedwork.Thedatasetcollectionandcapturedmet- state-of-artalgorithmsuseahybridstrategy,combiningbothrate
ricsareexplainedinSection3,whileSection4exploresstatistical andbuffer-basedmethods[4,28].
traitsoftheproductionandsyntheticdatasetfordifferentmobility Xieetal.[26]recentlyusechannelinformationfromthewire-
patterns.InSection5welayoutpossibleusecases,whileSection6 lesschannelinadditiontothethroughputratetomakeamore
outlinesfutureworkandourconclusion. intelligentdecisionforthenextsegmentquality.Also,anewstrat-
egyemergedrecently,relyingonthroughputforecasting[29]to
2 RELATEDWORK optimiseaqualityselectionofsegments.Asaresult,therearecon-
Previousdatasetsinthisarea,focusedprimarilyonthevariance siderableeffortstoaccuratelypredictthroughputforthenextx
inavailablebandwidthandtypicallyofferedaverylimitedsetof secondsinthefuturebyleveragingthechannelinformationinad-
devicemetrics,suchasvelocity,GPSandsignalstrength.Webegin ditiontothethroughputrate[27],andourownresearch[16].Also,
withBokanietal.[3],whoofferedadataset,collectedfrom3Gand contextinformationsuchasUE’sGPSposition,velocity,eNodeB
4Gnetworks,consistsofthroughputmeasurementsloggedevery GPSpositionanddistancebetweenUEandservingeNodeBcanbe
tenseconds,atimestampforsameandGPScoordinatesoftheuser usedforusermovementpredictionandresourceallocation[22].
deviceitself.Theauthorsutilisedasinglemobilecommutepattern Wangetal.[24]utilisethesemetricsforUEmovementanddirection
inametropolitanscenario,andrepeatedmultipletrailswithinthis predictiontominimisethenumberofhandovers.Forevaluating
pattern,warrantedbytheevidencethatnetworkthroughputcan andcomparingthesenoveltechniques,newdatasetsareneeded
varysignificantlyforthesameroute.Theycollectedalargenumber containinginformationbeyondthroughput,suchasthechannel
ofsamplesacrossthesamepathtogetstatisticallysignificantresults andcontextmetricsprovidedinthedatasetpresentedinthepaper.
onnetworkperformance.However,theirdatasethasalowsampling
3 DATASETCOLLECTION
granularity(tenseconds)andonlycontainsthroughputandavery
limitedsetofdevicevalues. Fortheproductiondatasetcollection,weusetheAndroiddevice
Similarly,Xiaoetal.andLietal.collectedbandwidthtracesover G-NetTrackPromobilenetworkmonitoringtool2.Thistoolenables
3Gand4Gnetworkrespectively[11,25].Inbothpapers,theauthors thecapturingofvariouschannelrelatedkeyperformanceindicators
useMobiNet1,acustomdevelopednon-rootedandroidapplication (KPIs),context-relatedmetrics,downlinkanduplinkthroughput,
fordownloadingcontentusingTCP.Themajorityofbothdatasets andalsocell-relatedinformation.Themainadvantageofthisap-
arecollectedinhigh-speedmobilityenvironments(train)where plication is that it does not require a rooted phone. In contrast
speedscanriseto310kph.Thecontentofthedatasetsconsistsof toG-NetTrack,Liandal.developedanopen-sourcesoftwaretool
informationsuchasapplicationthroughput,signalstrength,de- MobileInsight[12]thatcancaptureradioinformationdirectlyfrom
vicevelocityandeNodeBid.Riiseretal.[17]obtainedbandwidth chipsetsinrealtime.However,thesoftwarerequiresarootedmo-
logsfroma3Gnetworkusingdifferentmobilitypatterns;these bilephoneandworkswithQualcommSoCsonly.Thistoolissimilar
includedtram,train,metro,bus,ferry,andcar.Thedatasetcon- toproprietaryQualcomm’sQXDM3diagnosticsoftware.Whilethe
tainsasamplegranularityintheorderofsecondsandprovides non-rootedaspectofG-NetTrackisbeneficial,thereareanumber
additionalinformationsuchastimestamp,GPScoordinatesofthe oflimitationstotheapplication.Firstly,theminimumgranularity
device, and bandwidth throughput. Also, Hooft et al. [23] used ofcollectedsamplesisonesecond.Havinglow-resolutionKPIs,
thesameapproachforcollecting4Gnetworktracesforanalogous
2http://www.gyokovsolutions.com/
1http://www.wandoujia.com/apps/thu.kejiafan.mobinet 3https://www.qualcomm.com/
461

BeyondThroughput:a4GLTEDatasetwithChannelandContextMetrics MMSys’18,June12–15,2018,Amsterdam,Netherlands
e.g.,canincreasepredictionerrorasreportedin[16].Secondly, SNR:valueforsignal-to-noiseratio(dB).
•
the tool uses the standard Android library (telephony class) for CQI: valueforCQIofamobiledevice.CQIisafeedback
•
reportingchannelmetrics.Implementationofthesecallbackfunc- providedbyUEtoeNodeB.Itindicatesdataratethatcould
tionsdependsonthemanufacturerofthemobilesystemonachip betransmittedoverachannel(highestMCSwithaBLER
(SoC)chipsets.Also,notallparametersarereportedfordifferent probabilitylessthan10%),asthefunctionofSINRandUE’s
cellulartechnologies(2G/3G/4G).Forourdataset,wetestmobile receivercharacteristics.BasedonUE’spredictionofthechan-
devicesfromthreemajormobilechipsetsmanufactures,Qualcomm nel,eNodeBselectsanappropriatemodulationschemeand
(Snapdragon),Samsung(Exynos)andHuawei(Kirin).Ultimately, codingrate.
themobiledevicechosenisaSamsungJ5,whichprovidesameans DL_bitrate:downloadratemeasuredatthedevice(applica-
•
ofcapturingall4GnetworkmetricKPIs. tionlayer)(kbit/s)
Forourproductiondataset,wecollected135tracesforvarious UL_bitrate:uplinkratemeasuredatthedevice(application
•
mobilitypatternsacrosstwomajorIrishoperators,withdifferent layer)(kbit/s)
datalimitcaps.Thefirstprovider(operatorA)givesunlimited4G State:stateofthedownloadprocess.Ithastwovalues,either
•
data,whilethesecondprovider(operatorB)offersonly15GBper I(idle,notdownloading)orD(downloading)
month. However, the second operator provides 60GB on social NRxRSRQ&NRxRSRP:RSRQandRSRPvaluesfortheneigh-
•
mediaincludingYoutubestreaming.Forthefirstmobileoperator, bouringcell.
wecontinuouslydownloadafile(connection-oriented,TCP)with Cell_Longitude&Cell_Latitude:GPScoordinatesofserving
anaveragedurationof15minutespertrace(withafive-second • eNodeB.WeuseOpenCellid4,thelargestcommunityopen
pauseafterthedownloadcompletes).Weusethesameapproach databaseprovidingGPScoordinatesofcelltowers.
forthesecondoperator,butoncethedatacapisreached,weextend Distance: distancebetweentheservingcellandmobilede-
•
theapproachbydownloadingcontentfromYoutube.Wegenerate viceinmetres.
aURLforthevideofromYoutubetoexploitthehigherdatacapfor Weperform4Gmeasurementtrials(unlessotherwisestated)across
socialmedia.Foreachtrial,regardlessofmeasurementapproach, sixdifferentmobilitypatternssummarisedinTable1.
weuselargefile(>50MB)toallowtheTCPsendingwindowto
rampuptothemaximumsize.Asstated,everysampleislogged Table1:MobilityPatterns
withone-secondgranularity.Asaresult,averagetracedurationis
Type Summary
15minutes. Static Statictrials(indoor)
Toprovideacomparisonbetweenoperators,weperformmea- PedestrianWalkingtrialsaroundCorkcity,Ireland
surementstrialsforbothoperatorsatthesametime(weusethe Bus Trialsincludeurbanandsuburbancases
samemobiledevicemodeltolimittheimpactofdevicehardware Car Trialsincludeurbanandsuburbanscenarios
onthroughputrateandchannelmetrics).Thissubsetoftracesper- Train TravellingbetweenCork-Dublin(240km)
mitscomparisonofmobileoperatorsperformancesacrossdifferent andCork-Farranfore(75km).Combination
of3Gand4G.
parameters(throughputandchannelKPIs).Competingtestsuse
thesamedownloadapproachforbothcellularoperators(fileor
videodownload). 4 DATASETOVERVIEW
ThefollowingoutlinesthevariousKPIswithinourproduction
ProductionDatasetInthissection,wegiveashortoverviewofour
dataset:
dataset.Wecategoriseourtracesascommutetracesaswecollected
Timestamp:timestampofsample
• themajorityoftracesduringmorningandeveninghourswhile
LongitudeandLatitude:GPScoordinatesofmobiledevice
• goingfromhometoworkandback,andbeginwithanoverviewof
Velocity:velocityinkphofmobiledevice
• ourtracemodels:
Operatorname:cellularoperatorname(anonymised)
• StaticAsthenameimplies,thesetraceswerecollectedindoors
CellId:Servingcellformobiledevice
• withmobiledevicesbeingstationary.Thisscenariorepresentshow
NetworkMode:mobilecommunicationstandard(2G/3G/4G)
• peopletypicallytendtousetheirsmartdevices.However,thiscase
RSRQ: valueforRSRQ.RSRQRepresentsaratiobetween
• hastheleastappealasthethroughputisquitestablewithrelatively
RSRP and Received Signal Strength Indicator (RSSI). Sig-
lowvariations.
nalstrength(signalquality)ismeasuredacrossallresource
PedestrianOutdoortraceswhilewalkingaroundCorkcitycentre
elements(RE),includinginterferencefromallsources(dB).
using a number of different routes. Characteristics of collected
RSRP:valueforRSRP.RSRPRepresentsanaveragepower
• traces(averagerateandstandarddeviation)aresimilartothestatic
overcell-specificreferencesymbolscarriedinsidedistinct
casewithslightlymorevariationduetochannelconditionand
RE.RSRPisusedformeasuringcellsignalstrength/coverage
handovers.
andthereforecellselection(dBm).
BusBustracesusingpublictransportaroundCorkcity.Wegath-
RSSI:valueforRSSI.RSSIrepresentsareceivedpower(wide-
• eredtracesduringweekdaysandattheweekendstocapturediffer-
band)includingaservingcellandinterferenceandnoise
entcongestionpatterns.
fromothersources.RSRQ,RSRPandRSSIareusedformea-
Car Car traces over the city and suburban routes. This sub-
suringcellstrength/coverageandthereforecellselection
categoryofourdatasetcontainsthemosttraces.
(handover)(dBm).
4https://opencellid.org/
462

MMSys’18,June12–15,2018,Amsterdam,Netherlands DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,CormacJ.Sreenan
|     | 45                  |     |            | 90                  |     |     |     |            | 70                  |     |     |            |
| --- | ------------------- | --- | ---------- | ------------------- | --- | --- | --- | ---------- | ------------------- | --- | --- | ---------- |
|     |                     |     | Operator A |                     |     |     |     | Operator A |                     |     |     | Operator A |
|     | 40                  |     | Operator B | 80                  |     |     |     | Operator B | 60                  |     |     | Operator B |
|     | )s/tibM( tuphguorhT |     |            | )s/tibM( tuphguorhT |     |     |     |            | )s/tibM( tuphguorhT |     |     |            |
|     | 35                  |     |            | 70                  |     |     |     |            |                     |     |     |            |
|     | 30                  |     |            | 60                  |     |     |     |            | 50                  |     |     |            |
|     | 25                  |     |            | 50                  |     |     |     |            | 40                  |     |     |            |
|     | 20                  |     |            | 40                  |     |     |     |            | 30                  |     |     |            |
|     | 15                  |     |            | 30                  |     |     |     |            |                     |     |     |            |
20
|     | 10  |     |     | 20  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 5   |     |     | 10  |     |     |     |     | 10  |     |     |     |
|     | 00  |     |     |     | 00  |     |     |     | 00  |     |     |     |
20 40 60 80 100 120 140 20 40 60 80 100 120 140 20 40 60 80 100 120 140
|     |     | Seconds (s) |     |     |     | Seconds (s) |     |     |     |        | Seconds (s) |     |
| --- | --- | ----------- | --- | --- | --- | ----------- | --- | --- | --- | ------ | ----------- | --- |
|     |     | (a)Static   |     |     |     | (b)Bus      |     |     |     | (c)Car |             |     |
Figure1:Time-seriesofapplicationthroughputfordifferentmobilitypatternsandmobileoperators
Table2:AverageandVariationRangeofApplicationThroughput(Mbit/s)acrossdifferentmobilitypatternsandmobileoper-
ators
MobilityPatterns
|     |     | Operator     | Static               |     | Pedestrian     |     | Bus                 |               | Car            | Train         |            |     |
| --- | --- | ------------ | -------------------- | --- | -------------- | --- | ------------------- | ------------- | -------------- | ------------- | ---------- | --- |
|     |     |              | Avg.Var.Range        |     | Avg.Var.Range  |     | Avg.Var.Range       | Avg.Var.Range |                | Avg.Var.Range |            |     |
|     |     | A            | 5.3 (0.9,9.3)        |     | 9.9 (0.4,28.0) |     | 8.0 (0.08,20.3)11.4 |               | (0.92,27.9)4.7 |               | (0,11.3)   |     |
|     |     | B            | 42.6 (21.3,77.2)18.2 |     | (5.6,34.2)     |     | 13.5 (2.0,29.1)     | 22.3          | (3.2,49.1)     | 6.6           | (0.3,16.5) |     |
|     |     | Num.Traces   | 15                   |     | 31             |     | 16                  |               | 53             |               | 20         |     |
|     |     | TraceDur.(m) | 254                  |     | 560            |     | 180                 |               | 1265           |               | 650        |     |
TrainWhileourgoalistocollect4Gtraces,amajorityofthe rangeofthroughputvaluesforeachCQIseparately.Overall,we
traintracesareamixtureof3Gand4Gforbothoperators,dueto canobserveanincreasingtrendinthroughputproportionaltoCQI.
theavailabilityof4Gwithinmajorurbanareasonly. However,therangeofthroughputvaluesoscillatessignificantly
WenowprovideamoredetailedoverviewoftheThroughput, foreachCQI.Furthermore,foroperatorA,theaveragethroughput
ChannelandContextinformationprovidedinourdataset: ofCQIequals14islowerthanthethroughputforCQI15.Asimi-
Throughput Figure 1 illustrates a time-series of application larobservationholdsforoperatorBaswell.Finally,thisresultis
throughputforbothnetworkoperatorsacrossdifferentmobility strengthenedevenmorewiththecalculationofcorrelationbetween
patternsetups(weshowrandomlyselectedcompetingtraces).Fur- throughputandCQI,yieldingarelativelylowcorrelationcoeffi-
thermore,Table2depictsaverageapplicationthroughputandvari- cientof0.6and0.38,foroperatorAandB,respectively.However,
ationincludingthenumberoftracesandtotaltracedurationacross thiscorrelationisevenlowerforothercases;inparticularforthe
alltracesfordifferentmobilitypatterncategoriesandtwomobility staticcasewherethecorrelationcoefficientequals0.35.CQIiscal-
operators.Bydefinition,variationrangeisapercentile-wisemea- culatedonthemobiledevice(basedonwirelesschannelcondition)
sureofvariation.Let’sdefineRasapplicationthroughputduring andrepresentsthemaximumratethedevicecanreceivewithlow
timeintervalthe(t,t+1).Thenwecandefinevariationrangeas error.However,actualrate(numberofallocatedresourcesblocks
theinterval[RL,RH],whereRL representsa10th percentileofR, perframe)isassignedbyeNodeB(scheduler).Manyfactorscan
andanalogouslyRH a90th percentileofR[9].Thisrangedefines influenceeNodeBdecision,includingthenumberofusers,other
usersthroughputdemand,theirCQIsvalues,etc.
boundarieswhere80%ofmeasuredthroughputlies.Fromtheval-
uesshowninTable2,operatorBhasasignificantlyhigheraverage
thanoperatorAforallmobilitypatterncases.Therecouldbedif-
|     |     |     |     |     |     |     | 80  |     |     |     | 120 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ferentreasonsforthisobservationincludingbettercoverage,and
70
operator’sinternaltrafficpolicy(e.g.,trafficlimitationandshap- )s/tibM( tuphguorhT 60 )s/tibM( tuphguorhT 100
|     |     |     |     |     |     |     | 50  |     |     |     | 80  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing).Lookingateachcaseindividually,therearedifferentchanges
|                                                       |     |     |     |     |     |     | 40  |     |     |     | 60  |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| inaveragevalueandvariationrangedependingontheoperator |     |     |     |     |     |     | 30  |     |     |     |     |     |
40
| itself,e.g.,forA,astaticcasehassignificantlyloweraveragethan |     |     |     |     |     |     | 20  |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thepedestriancase.Arationaleforthisresultcouldbeincover- 10 20
| agediscrepancyforindoorandoutdoorscenarios.Wenotethat |     |     |     |     |     |     | 0   |           |           |              | 0     |                            |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | ----- | -------------------------- |
|                                                       |     |     |     |     |     |     |     | 0 1 2 3 4 | 5 6 7 8 9 | 101112131415 | 0 1 2 | 3 4 5 6 7 8 9 101112131415 |
|                                                       |     |     |     |     |     |     |     |           | CQI       |              |       | CQI                        |
experimentsrunindoorhaveaweakersignalin90%ofcases.
|     |     |     |     |     |     |     |     | (a)OperatorA |     |     |     | (b)OperatorB |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ------------ |
ChannelMeasuredthroughputisacombinationoftheeNodeB
environment(load,schedulerpolicy),wirelesschannelcharacteris- Figure2:BoxplotofCQIvsapplicationthroughputforboth
ticsandmobiledevicereceivercapabilities.Additionalinformation networkoperators(car)
aboutthechannelenvironmentinadditiontothroughputvalues
canincreaseaccuracyandgranularity,pavingawaytomoreaccu- Context Ourdatasetprovidesadditionalcontextinformation
rateprediction.InFigure2,weanalysethisrelationshipandshow suchasdevice’sGPSpositionsandvelocity.Figure3showsaran-
boxplotofCQIagainstapplicationthroughput.Boxplotshowsthe domisedselectedtrainroutefromourdataset.Weprovideestimated
463

BeyondThroughput:a4GLTEDatasetwithChannelandContextMetrics MMSys’18,June12–15,2018,Amsterdam,Netherlands
Table3:AverageandVariationRangeofdevicevelocity(kph)acrossdifferentmobilitypatternsandmobileoperators
MobilityPatterns
Operator Pedestrian Bus Car Train
Avg.Var.Range Avg.Var.Range Avg.Var.Range Avg.Var.Range
A 2.4 (0.0,4.0) 17.2 (0.0,34.0) 23.7 (0.0,54.0) 60.6 (0.0,109.4)
B 1.5 (0.0,3.0) 10.7 (0.0,30.0) 35.1 (0.0,56.0) 53.9 (0.0,114.0)
GPScoordinatesofservingeNodeBsanddistancebetweenthem randomlyscatteredacrossaseven-cellcluster.Everyuserhasa
usingHaversineformula. constantmovingspeed(80kph)andusesGauss-Markovmobility
modelformovementemulation.Halfofthedevicesaredownload-
ingat32Mbit/srate,andtheotherhalfareuploadingat2Mbit/s
rate.WeuseUDPinsteadofTCPasthetransportprotocol.Amoti-
vationforthisdecisionisaremovalofanyadaptationmechanisms
fromtheclient.
1.0
0.8
0.6
Figure3:GPScoordinateforthetrainmobilitypattern 0.4
0.2
Additionally,Table3showsaverageandvariationrangeofdevice 0.0
velocityacrossdifferentmobilitypatternsandnetworkoperators.
0.20 10 20 30 40 50
Intuitively,speedincreasesaswemovefromstatic(notshown)to Time Lag (s)
pedestrianandfinallytrainscenario.Asimilarobservationholdsfor
variationrangeaswell.Velocityvaluesarealikeforbothnetwork
operatorsasthesamephones/patternswereusedforbothoperators.
CaveatsThisproductiondatasetcontainsaconsiderableamount
ofinformation.However,thereareanumberoflimitations.Firstly,
oursamplinggranularityisonlyonesecond.Thislimitationisdue
toG-NetTrackandtheGooglechannelAPI.Evenwithdirectaccess
totheAPI,granularitydoesnotsignificantlyincrease[27].Sec-
ondly,notallrecordshaveallvalues.Themostprominentexample
representsRSSI,whichdoesn’tgetloggedforeverysample.Sim-
ilarly,forgeo-locationsofeNodeB,weuseopencell.orgdatabase.
Unfortunately,thisdatabasedoesn’tcontainGPScoordinatesfor
alleNodeBs.Oneapproachweusetodealwithmissingdatais
imputationmethods[14].
SyntheticDatasetTosupplementourreal-time4Gproduction
network dataset, we also provide a synthetic dataset generated
from a large-scale 4G ns-3 simulation. As pointed out, our pro-
ductiondatasethasmediumsamplegranularityandonlycontains
informationgatheredattheclient.Asanalternative,weprovide
simulationtracesthathavehighgranularity(250ms)andcomple-
mentthesimulationtraceswithnetwork-sidemeasurements.These
additionalpiecesofinformationcanonlybecollectedatthenet-
work/operator,whichinpractice,isaponderoustask.Weprovide
additionalinformationsuchascompetingmetricsforuserscon-
nectedtothesamecell,leveragingeNodeBschedulingprinciples,
andultimatelyprovideameansoflarge-scaleevaluationofkey
performanceindicatorsinmulti-cellmobilityscenarios.
Duetospacelimitation,weprovideabriefoverviewofoursyn-
theticdataset,withfulldetailsoftraceoutput,simulationtestbed,
andassociatedcodeandsetuplocatedatourwebsite5 andfrom
the Zenodo research data repository6. In our synthetic dataset,
weutilisealarge-scale4Gns-3simulationthatincludes100users
5http://www.cs.ucc.ie/misl/research/datasets/ivid_4g_lte_dataset/
6https://doi.org/10.5281/zenodo.1219679
tneciffeoC
noitalerrocotuA
1.0
0.8
0.6
0.4
0.2
0.00 10 20 30 40 50
Time Lag (s)
(a)Simulation
tneciffeoC
noitalerrocotuA
(b)Realcase(car)
Figure4:Theautocorrelationcoefficientofthroughput
Interestingly,ifwecompareautocorrelationcoefficientofthrough-
putfordifferenttimelagsbetweensimulationandtherealcasewe
concludethatsimulationthroughputexhibitsmorerandomness,
asdepictedinFigure4.Thisresultisintuitiveassimulationuses
pseudo-randomgeneratorssoonecanexpectthisresult.
5 POSSIBLEUSE-CASES
Inthissection,weoutlinesomeofthepossibleuse-casesforthe
dataset.WestartwithHASalgorithms,whereourdatasetenables
thecomparisonofdifferentalgorithmstrategiesdependingonthe
informationtheyrequireforoptimisationofchunkselection.Most
algorithmscalculateonthroughputsamplesonly,withsomeof
themrequiringfinergranularitythanchunkduration.However,
goingbeyondthroughputrequirement,newstrategiesmandate
channel and context information, allowing them to make more
accuratethroughputprediction.TheproliferationofCommercial
VirtualReality(VR)technologyisincreasingdownloaddemands
and is a distinct candidate for evaluation using our dataset. Al-
thoughVRtypicallyusesprogressivedownload,itisexpectedthat
VRwillswitchtoHASmechanisminthenearfuture[15].This
switchwillresultintheneedfordesigningnewadaptationalgo-
rithmssuitableforVRspecificneeds(adaptingthequalitylevelof
tiles).
Anotheruse-casewouldbehandoveranalysisandprediction.
Handover procedure is crucial in cellular networks as it allows
continuousconnectionacrossdifferenteNodeBs.Therearevarious
mechanismsandapproachesforhandoverprediction[1,7,13].To
benefittheseapproaches,ourdatasetcontainsinformationabout
handovereventsandalsoinformationaboutGPSpositionofcurrent
cellanddevice,channelmetricsforservingandtheneighbouring
cell.Finally,generatingnewbandwidthtracesbasedontheexisting
464

MMSys’18,June12–15,2018,Amsterdam,Netherlands DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,CormacJ.Sreenan
traces is a very interesting and demanding challenge, as multi-
265–276.
dimensionalstatisticalanalysisisneededoverallavailableKPIs. [10] J.Jiang,V.Sekar,andH.Zhang.2014.ImprovingFairness,Efficiency,andStability
Forthistask,oneapproachcouldbeleveragingmachinelearning inHTTP-BasedAdaptiveVideoStreamingWithFestive.IEEE/ACMTransactions
techniques.Asaresult,alargenumberofrealistictraceswould
onNetworking22,1(Feb2014),326–340. https://doi.org/10.1109/TNET.2013.
2291681
begeneratedandthusrelievingresearchersofmanuallycollecting [11] L.Li,K.Xu,D.Wang,C.Peng,Q.Xiao,andR.Mijumbi.2015.Ameasurement
vastamountsofnetworktraces,whichcanbeaverytedioustask. studyonTCPbehaviorsinHSPA+networksonhigh-speedrails.In2015IEEE
ConferenceonComputerCommunications(INFOCOM).2731–2739. https://doi.
org/10.1109/INFOCOM.2015.7218665
6 CONCLUSION [12] Y.Li,C.Peng,Z.Yuan,J.Li,H.Deng,andT.Wang.2016.Mobileinsight:Extracting
andAnalyzingCellularNetworkInformationonSmartphones.InProceedingsof
Inthispaper,wepresentbothproductionandsynthetic4Gtrace
the22NdAnnualInternationalConferenceonMobileComputingandNetworking
dataset,withlowbandwidththroughputsamplinggranularity,and (MobiCom’16).202–215.
invaluable client-side cellular channel and context information, [13] W.Luo,X.Fang,M.Cheng,andX.Zhou.2011.Anoptimizedhandovertrigger
schemeinLTEsystemsforhigh-speedrailway.InProceedingsoftheFifthIn-
fromadiversesetofroutesacrosstwomobileoperators(produc- ternationalWorkshoponSignalDesignandItsApplicationsinCommunications.
tion)andalargerangeofclientsinamulti-cellcluster(synthetic). 193–196. https://doi.org/10.1109/IWSDA.2011.6159423
[14] R.Mazumder,T.Hastie,andR.Tibshirani.2010.SpectralRegularizationAlgo-
Thethroughputvaluesofbothdatasetspermitdetailedanalysis
rithmsforLearningLargeIncompleteMatrices. J.Mach.Learn.Res.11(Aug.
withrespecttooscillationinthetransmissionmedium,whilethe 2010),2287–2322.
channelandcontextmetricsoftheproductiondatasetfarexceed [15] F.Qian,L.Ji,B.Han,andV.Gopalakrishnan.2016.Optimizing360VideoDelivery
overCellularNetworks.InProceedingsofthe5thWorkshoponAllThingsCellular:
theoriginalgoalofthedatasetwithrespecttoHASevaluationfor
Operations,ApplicationsandChallenges(ATC’16).ACM,NewYork,NY,USA,
throughputprediction. 1–6. https://doi.org/10.1145/2980055.2980056
Weprovideahigh-leveloverviewofthedatasetwhichprovides [16] D.Raca,A.H.Zahran,C.J.Sreenan,R.K.Sinha,E.Halepovic,R.Jana,andV.
Gopalakrishnan.2017.BacktotheFuture:ThroughputPredictionForCellular
insightintodifferentmobilitypatternsacrossbothmobileoperators, NetworksUsingRadioKPIs.InProceedingsofthe4thACMWorkshoponHot
withrespecttoapplicationthroughput,averageandvariationin TopicsinWireless(HotWireless’17).37–41.
[17] H.Riiser,P.Vigmostad,C.Griwodz,andtitle=CommutePathBandwidthTraces
bandwidth,andchannelandcontextmetrics.Wealsoillustratea
from3GNetworks:AnalysisandApplicationsbooktitle=Proceedingsofthe
numberofpossibleusecasesforthedataset.Tothebestofour 4thACMMultimediaSystemsConferenceseries=MMSys’13year=2013isbn
knowledge,thisisthefirstpubliclyavailabledatasetthatcontains =978-1-4503-1894-5location=Oslo,Norwaypages=114–118numpages=5
http://doi.acm.org/10.1145/2483977.2483991doi=10.1145/2483977.2483991acmid
throughput,channelandcontextinformationforreal-timeanalysis
=2483991publisher=ACMaddress=NewYork,NY,USAkeywords=3G,
ofaproduction4Gnetwork. adaptivestreaming,bandwidthtraces,bitrateadaption,fluctuatingbandwidth,
mobileinternet,wirelessHalvorsen,P.[n.d.].
[18] Y.Sani,A.Mauthe,andC.Edwards.2017.AdaptiveBitrateSelection:ASurvey.
ACKNOWLEDGEMENTS
IEEECommunicationsSurveysTutorials19,4(Fourthquarter2017),2985–3014.
TheauthorsacknowledgethesupportofScienceFoundationIreland https://doi.org/10.1109/COMST.2017.2725241
[19] K.Spiteri,R.Urgaonkar,andR.K.Sitaraman.2016.BOLA:Near-optimalbitrate
(SFI)underResearchGrant13/IA/1892.WealsothankNoelBourke adaptationforonlinevideos.InIEEEINFOCOM2016-The35thAnnualIEEE
andYusufSanifortheirinvaluablehelpwiththedatasetcollection. InternationalConferenceonComputerCommunications.1–9.https://doi.org/10.
1109/INFOCOM.2016.7524428
[20] Statista. 2016. Number of smartphone users worldwide from
REFERENCES
2014 to 2020. (2016). https://www.statista.com/statistics/330695/
[1] I.M.Bălan,B.Sas,T.Jansen,I.Moerman,K.Spaey,andP.Demeester.2011. number-of-smartphone-users-worldwide/
Anenhancedweightedperformance-basedhandoverparameteroptimization [21] T.Stockhammer.2011.DynamicAdaptiveStreamingoverHTTP–:Standards
algorithmforLTEnetworks.EURASIPJournalonWirelessCommunicationsand andDesignPrinciples.InProceedingsoftheSecondAnnualACMConferenceon
Networking2011,1(17Sep2011),98. https://doi.org/10.1186/1687-1499-2011-98 MultimediaSystems(MMSys’11).133–144.
[2] N.Baldo,M.Miozzo,M.Requena-Esteso,andJ.Nin-Guerrero.2011.AnOpen [22] D.Stynes,K.N.Brown,andC.J.Sreenan.2016. Aprobabilisticapproachto
SourceProduct-orientedLTENetworkSimulatorBasedonNs-3.InProceedings usermobilitypredictionforwirelessservices.In2016InternationalWireless
ofthe14thACMInternationalConferenceonModeling,AnalysisandSimulationof CommunicationsandMobileComputingConference(IWCMC).120–125. https:
WirelessandMobileSystems(MSWiM’11).293–298. //doi.org/10.1109/IWCMC.2016.7577044
[3] A.Bokani,M.Hassan,S.S.Kanhere,J.Yao,andG.Zhong.2016.Comprehensive [23] J.vanderHooft,S.Petrangeli,T.Wauters,R.Huysegems,P.R.Alface,T.Bostoen,
MobileBandwidthTracesfromVehicularNetworks.InProceedingsofthe7th andF.DeTurck.2016.HTTP/2-BasedAdaptiveStreamingofHEVCVideoOver
InternationalConferenceonMultimediaSystems(MMSys’16).Article44,6pages. 4G/LTENetworks.IEEECommunicationsLetters20,11(2016),2177–2180.
[4] L.DeCicco,V.Caldaralo,V.Palmisano,andS.Mascolo.2013.ELASTIC:AClient- [24] H-L.Wang,S-J.Kao,C-Y.Hsiao,andF-M.Chang.2014. Amovingdirection
SideControllerforDynamicAdaptiveStreamingoverHTTP(DASH).In2013 prediction-assistedhandoverschemeinLTEnetworks. EURASIPJournalon
20thInternationalPacketVideoWorkshop.1–8. https://doi.org/10.1109/PV.2013. WirelessCommunicationsandNetworking2014,1(15Nov2014),190. https:
6691442 //doi.org/10.1186/1687-1499-2014-190
[5] Cisco. 2017. Cisco Visual Networking Index: Global Mobile Data Traf- [25] Q.Xiao,K.Xu,D.Wang,L.Li,andY.Zhong.2014.TCPPerformanceoverMobile
fic Forecast Update, 2016–2021. (2017). https://www.cisco.com/c/en/ NetworksinHigh-SpeedMobilityScenarios.In2014IEEE22ndInternational
us/solutions/collateral/service-provider/visual-networking-index-vni/ ConferenceonNetworkProtocols.281–286. https://doi.org/10.1109/ICNP.2014.49
mobile-white-paper-c11-520862.html [26] X.Xie,X.Zhang,S.Kumar,andL.E.Li.2015.piStream:PhysicalLayerInformed
[6] B.A.Forouzan.2002.TCP/IPProtocolSuite(2ed.).McGraw-Hill,Inc.,NewYork, AdaptiveVideoStreamingoverLTE.InProceedingsofthe21stAnnualInternational
NY,USA. ConferenceonMobileComputingandNetworking(MobiCom’15).413–425.
[7] H.Ge,X.Wen,W.Zheng,Z.Lu,andB.Wang.2009. AHistory-BasedHan- [27] C.Yue,R.Jin,K.Suh,Y.Qin,B.Wang,andW.Wei.2017.LinkForecast:Cellu-
doverPredictionforLTESystems.In2009InternationalSymposiumonComputer larLinkBandwidthPredictioninLTENetworks.IEEETransactionsonMobile
NetworkandMultimediaTechnology.1–4.https://doi.org/10.1109/CNMT.2009. ComputingPP,99(2017),1–1. https://doi.org/10.1109/TMC.2017.2756937
5374706 [28] A.H.Zahran,D.Raca,andC.Sreenan.2018.ARBITER+:AdaptiveRate-Based
[8] T.Huang,R.Johari,N.McKeown,M.Trunnell,andM.Watson.2014.ABuffer- InTElligentHTTPStReamingAlgorithmforMobileNetworks.IEEETransactions
basedApproachtoRateAdaptation:EvidencefromaLargeVideoStreaming onMobileComputing(2018),1–1. https://doi.org/10.1109/TMC.2018.2825384
Service.InProceedingsofthe2014ACMConferenceonSIGCOMM(SIGCOMM’14). [29] X.K.Zou,J.Erman,V.Gopalakrishnan,E.Halepovic,R.Jana,X.Jin,J.Rexford,
187–198. andR.K.Sinha.2015. CanAccuratePredictionsImproveVideoStreamingin
[9] M.JainandC.Dovrolis.2005.End-to-endEstimationoftheAvailableBandwidth CellularNetworks?.InProceedingsofthe16thInternationalWorkshoponMobile
VariationRange.InProceedingsofthe2005ACMSIGMETRICSInternationalCon- ComputingSystemsandApplications(HotMobile’15).57–62.
ferenceonMeasurementandModelingofComputerSystems(SIGMETRICS’05).
465