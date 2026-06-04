Beyond Throughput, The Next Generation:
A 5G Dataset with Channel and Context Metrics
DarijoRaca DylanLeahy,CormacJ.Sreenan
FacultyofElectricalEngineering,UniversityofSarajevo, JasonJ.Quinlan
Sarajevo,BiH SchoolofComputerScience&InformationTechnology,
draca@etf.unsa.ba UniversityCollegeCork,Ireland
{cjs,j.quinlan}@cs.ucc.ie
ABSTRACT June8–11,2020,Istanbul,Turkey.ACM,NewYork,NY,USA,6pages.https:
Inthispaper,wepresenta5Gtracedatasetcollectedfromamajor //doi.org/10.1145/3339825.3394938
Irishmobileoperator.Thedatasetisgeneratedfromtwomobil-
itypatterns(staticandcar),andacrosstwoapplicationpatterns 1 INTRODUCTION
(videostreamingandfiledownload).Thedatasetiscomposedof
Fromthefirst-generation,voice-only,mobilecellularcommunica-
client-sidecellularkeyperformanceindicators(KPIs)comprisedof
tionsystemstothecurrentfourthgenerationsystem(4G-Long
channel-relatedmetrics,context-relatedmetrics,cell-relatedmet-
TermEvolution-LTE),developmenthasprogressedatasteadypace.
ricsandthroughputinformation.Thesemetricsaregeneratedfrom
Whilethisevolutionistypicallyfuelledbyservicesandapplications
awell-knownnon-rootedAndroidnetworkmonitoringapplica-
utilisingthenetwork,thecurrentbandwidthdemandsonthe4G
tion,G-NetTrackPro.Tothebestofourknowledge,thisisthe
networkwereneveranticipated[1].Applicationsutilisingsocial
firstpubliclyavailabledatasetthatcontainsthroughput,channel
media,gaming,andrecentadvancesinAugmented/VirtualReality,
andcontextinformationfor5Gnetworks.Tosupplementourreal-
haveacceleratedthedemandsforthenext,fifthgeneration(5G),of
time5Gproductionnetworkdataset,wealsoprovidea5Glarge
thecellularcommunicationstandard.5Gholdsthepromiseofvastly
scalemulti-cellns-3simulationframework.Theavailabilityofthe
improvedconnectivity:highdatarates(10xincreasecomparedto
5G/mmwavemoduleforthens-3mmwavenetworksimulatorpro-
“traditional”4Gnetwork)andlowlatency(10xlowercomparedto
videsanopportunitytoimproveourunderstandingofthedynamic
a4Gnetwork).Inadditiontothehighrates(around1Gbps)and
reasoningforadaptiveclientsin5Gmulti-cellwirelessscenarios.
lowlatency(1ms),5Gprovidesconnectivityfortensofthousands
Thepurposeofourframeworkistoprovideadditionalinformation
ofdevicesinordertosupportfutureInternetofThings(IoT)and
(suchascompetingmetricsforusersconnectedtothesamecell),
InternetofVehicle(IoV)paradigms.Theseenhancementsrequire
thusprovidingotherwiseunavailableinformationaboutthebase
novelsolutionsincorenetworkarchitectureandradiointerface
station(eNodeBoreNB)environmentandschedulingprinciple,
design[6].
toenduser.Ourframeworkpermitsotherresearcherstoinvesti-
Thetwomostsignificantfactorsdrivingthedevelopmentofnext
gatethisinteractionthroughthegenerationoftheirownsynthetic
generationcellularstandardsistherapidincreaseinthenumberof
datasets.
connecteddevicesandtheunrivalledriseinmultimediatraffic,and
asadirectresulttheirincreasedthroughputdemands.Predictions
CCSCONCEPTS
forthenumberofconnecteddevicesby2025vary.Thelargestpre-
•Informationsystems→Multimediastreaming;•Networks dictionbeingthatthenumberofconnectedIoTdevicesisexpected
→PublicInternet;Wirelessaccessnetworks. toreach75.44billion[2].Attheheartofthisgrowthinthroughput
demandisvideotraffic,carriedthroughdifferentapplications,from
KEYWORDS VideoonDemand,livestreamingand360-degreevideo.Current
streamingplatformsutilisetheHTTPadaptivestreaming(HAS)
Dataset,5G,NR,Mobility,throughput,contextinformation,adap-
technique[18]forvideodelivery.HASallowsgracefuladaptation
tivevideostreaming,mmwave
ofvideoqualityduringtheplaybackthroughthesegmentationof
ACMReferenceFormat: videocontent.Newvideocompressionstandards(H.265/HEVC)
DarijoRaca,DylanLeahy,CormacJ.Sreenan,andJasonJ.Quinlan.2020. andultra-highdefinitionresolutions(e.g.,8K)havehighbandwidth
BeyondThroughput,TheNextGeneration:A5GDatasetwithChanneland
requirements[13].Theserequirementsarefurtherexacerbatedin
ContextMetrics.In11thACMMultimediaSystemsConference(MMSys’20),
360-degreevideos.Forexample,24K360-degreevideowith120
frame-per-secondcanconsumeseveralGbps.However,highband-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
widthdemandisnottheonlyconstraint.Usercanchangefield-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation of-viewatanytime.Forausertonotexperiencemotionsickness,
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM latencyduringthetransitionneedstobelessthan20ms[19].While
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
5G can sustain these demands, it is yet to be proven that high-
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. ratelow-latencycanbeconsistentlysupportedinrealnetworks.
MMSys’20,June8–11,2020,Istanbul,Turkey Tosupportanalysisofvideoperformances,newdatasetscontain-
©2020AssociationforComputingMachinery.
ingbandwidthandlatencyinformationcollectedinproduction5G
ACMISBN978-1-4503-6845-2/20/06...$15.00
https://doi.org/10.1145/3339825.3394938 networksareneeded.
303

MMSys’20,June8–11,2020,Istanbul,Turkey DarijoRaca,DylanLeahy,CormacJ.Sreenan,andJasonJ.Quinlan
In this paper, we present two datasets: the first is a produc- Androiddevices.TheapplicationisinstalledonaSamsungS105G
tiondatasetcollectedfromamobileoperator’s5Gnetworkand Androiddevice.G-NetTrackPropermitsthecollectionofmultiple
the second is a synthetic dataset generated from a large-scale channel-relatedmetrics,context-relatedmetrics,cell-relatedmet-
multi-cell5G/mmwavens-3[3]framework.Ourproductiondataset ricsandthroughputinformation(uplinkanddownlink)usingthe
is analagous to our previously published dataset from 4G net- standardAndroidlibrary.G-NetTrackProworksacrossarangeof
works[16].WecollectedtracesfromamajorIrishoperatorwithtwo Androiddevicesanddoesnotrequirerootedprivileges.Someof
mobilitypatterns,drivingandstatic.Furthermore,weextendour thelimitationsincludeminimumone-secondgranularityforthe
downloadstrategybeyondfiledownload,runningthesamescenar- channelmetrics(thislimitationcomesfromtheAndroidAPIitself)
ioswhilestreamingvideocontentusingAmazonPrimeandNetflix andanon-unifiedcapabilityofmeasuringallthemetricsacross
streamingservices.Theintentisnottomeasurevideostreamingap- thedifferentmobile“systemonachip”(SoC)chipsetsmanufac-
plicationperformanceovera5Gnetwork,buttorecordthevariance turers.Implementationofcallbackmethodsforreportingchannel
inchannelconditionsduetothevideostreaming.Inadditionto valuesdependsontheSoCmanufacturer.Luckily,SamsungS10
throughputvalues,thedatasetcontainsinformationaboutlatency, 5G(withExynoschipset)providesameansofcapturingallthe5G
channelconditions(e.g.,signalstrength),userlocation(i.e.,GPS channelmetrics(note:atthetimeofcollection,wewerelimitedby
coordinates)andmore(seeSection4fordetails).Tothebestofour thechoiceof5GsupportedmobiledevicessupportedbytheIrish
knowledge,thisisthefirstpubliclyavailabledatasetthatcontains mobileoperatorusedforthedatasetgeneration).
throughput,channelandcontextinformationfor5Gnetworks. Ourproductiondataset2consistsof83traces,withatotaldura-
Theremainderofthispaperisorganisedasfollows.Section2 tionof3142minutes.ThemobileplanofferedbytheIrishmobile
describesrelatedwork.The5Gproductiondatasetcollectionand operatorincludesafairuselimitof80GBdatapermonth,before
recordedmetricsareexplainedinSection3,whileSection4explores thedownloadrateisreduced.Thestrategyforcollectingthe5G
statistical traits of the production dataset for different mobility dataisasfollows;foreachcombinationofapplication(filedown-
patterns.InSection5,wepresentour5G/ns-3simulationframework load,Netflix,AmazonPrime)andmobilitypattern(static,driving),
andofferdetailsonconfiguration,structureandillustratesample werunexperimentsuntilalldataisconsumedpermonth.This
outputsofthesyntheticdataset.InSection6weoutlinepossible leadstoalimitednumberoftraces.Forexample,weonlycapture
usecases,whileSection7concludesthepaper. fourbandwidthtracesinastaticscenariowithlargefiledownload.
However,thetotalnumberofminutesforthestaticscenariois
2 RELATEDWORK 160minutes.Thisisintuitive,asfiledownloadcaseproducesthe
Priorrelateddatasetswerecollectedusing3Gand4Gnetworktech- highestthroughputvaluesandconsumesdataveryquickly.These
nologies[4,10,16,17,20,21].Thesedatasetsfocusonthroughput largedurationtracescanbesplitintoshorterperiods,depending
informationloggedinarangeoftimescales(fromonetoseveral ontheneedsofanexperiment(typically,mostofthevideo-related
seconds), and across various mobility patterns, including static, experimentsconsideredintheliteratureutiliseuptofiveminutes
pedestrian,bus,train,ferryandcar.Throughputinformationcan ofbandwidthtraces).
bebeneficialwhenevaluatingtheperformanceattheapplication Forthefiledownloadtrial,weusealargefile(>200MB)toallow
layer,suchasrequiredbyHASalgorithmsinvideostreamingduring the TCP sendingwindowto ramp up tothe maximum size. As
theoptimisationofvideodeliveryinrate-based[9],buffer-based[7], stated,everysampleisloggedwithone-secondgranularity.For
andhybrid[5]schemes.Someofthesedatasets[4]werecollected NetflixandAmazonPrimewestreamanimated(circa200m)and
multipletimesoverthesameroutetogetstatisticallysignificant live-action(circa400m)videocontent,whilerunningG-NetTrack
results(asthenetworkthroughputcanvarysignificantlyoverthe Proapplicationinthebackgroundcollectingbandwidthandchannel
sameroute).Inadditiontothroughputperformance[10,16,21], samples.
somedatasetscontaininformationaboutthechannel(e.g.,signal Thefollowingmetricsareincludedinourproductiondataset:
strength),context(e.g.,GPSofthedevice,devicevelocity,eNBsID), • Timestamp:timestampofsample
whichcanbebeneficialwhenevaluatingmobilitypatternsduring • LongitudeandLatitude:GPScoordinatesofmobiledevice
handover.Therearealsomanyvideostreamingapproachesthat • Velocity:velocityinKilometres/hofmobiledevice
leverageinformationbeyondthroughputtomakemoreintelligent • Operatorname:cellularoperatorname(anonymised)
decisionsforthenextchunkqualityinimprovingvideoQualityof • CellId:Servingcellformobiledevice
Experience(QoE)[14,22,23].Recently,Narayananetal.[12]con- • NetworkMode:mobilecommunicationstandard(2G/3G/4G/5G)
ductedthefirst5GmeasurementstudyofVerizon’s5Gnetworkin • DL_bitrateandUL_bitrate:download/uplinkratemeasured
theU.S.Theauthorscollectedthroughputandlatencyinformation atthedevice(applicationlayer)(kbps)
only,comparingtheirresultswithVerizon’s4Gnetwork.Theirlog • State:stateofthedownloadprocess.Ithastwovalues,either
dataset,whichwasnotreleased,consistsofUElocationandIP,plus I(idle,notdownloading)orD(downloading)
eNBIDandsignalstrength. • 𝑃𝑖𝑛𝑔 𝑎𝑣𝑔,𝑃𝑖𝑛𝑔 𝑚𝑖𝑛,𝑃𝑖𝑛𝑔 𝑚𝑎𝑥,𝑃𝑖𝑛𝑔 𝑠𝑡𝑑,𝑃𝑖𝑛𝑔 𝑙𝑜𝑠𝑠:pingstatistics
(average,minimum,maximum,standarddeviationandloss)
3 PRODUCTIONDATASETGENERATION • SNR:valueforsignal-to-noiseratio(dB).
• RSRQ:RepresentsaratiobetweenRSRPandReceivedSignal
Forthecollectionofthe5Gproductiondatasetweutiliseversion
18.7oftheG-NetTrackPromobilenetworkmonitoringtool1for Strength Indicator (RSSI). Signal strength (signal quality)
1http://www.gyokovsolutions.com/ 2https://github.com/uccmisl/5Gdataset.git
304

BeyondThroughput,TheNextGeneration:
A5GDatasetwithChannelandContextMetrics MMSys’20,June8–11,2020,Istanbul,Turkey
is measured across all resource elements (RE), including throughputduringtimeintervalthe(𝑡,𝑡+1).Thenvariationrange
interferencefromallsources(dB).
isdefinedastheinterval[𝑅𝐿,𝑅𝐻],where𝑅𝐿
representsa10
𝑡ℎ
per-
• RSRP:valueforRSRP.RSRPRepresentsanaveragepower centileof𝑅,andanalogously𝑅𝐻 a90 𝑡ℎ percentileof𝑅 [8].This
overcell-specificreferencesymbolscarriedinsidedistinct rangedefinesboundarieswhere80%ofmeasuredthroughputlies.
RE.RSRPisusedformeasuringcellsignalstrength/coverage Table3showsperformancemetricsforthe4Gand5G.Asex-
andthereforecellselection(dBm). pected,5Gallowshigherrates,witha50%increasefortheaverage
• RSSI:valueforRSSI.RSSIrepresentsareceivedpower(wide- throughputforthestaticscenario.Thisobservationisfurthersup-
band)includingaservingcellandinterferenceandnoise portedbyvariationrange,wheretheupperlimitforthroughput
fromothersources.RSRQ,RSRPandRSSIareusedformea- is202Mbpsforthe5G,almost3xhigherthanthatof4G.However,
suringcellstrength/coverageandthereforecellselection thisdifferenceislessevidentinthecaseofthecarscenario.The
(handover)(dBm). averagethroughputincreasedby27%for5Gcomparedto4G.The
• CQI:valueforChannelQualityIndictator(CQI)ofamobile mainreasonfor“minor”improvementislackof5Gbasestations
device. CQI is a feedback provided by UE to the eNB. It acrossalldrivingroutes,forcingthedevicetouse4G.However,
indicatesdataratethatcouldbetransmittedoverachannel evenwiththislimit,upperlimitforvariationrangeisstillalmost
(highestMCSwithaBLERprobabilitylessthan10%),asthe 2xhigherfor5Gthan4G.Whilethementionedmetricsgavetheex-
functionofSINRandUE’sreceivercharacteristics.Basedon pectedperformance,theinterestingvaluesarepeakratesthatwere
UE’spredictionofthechannel,eNBselectsanappropriate observedduringthecollection.Inthecaseofthestaticscenario,the
modulationschemeandcodingrate. maximumobserved5Gthroughputis333Mbps.Thisisanincrease
• NRxRSRQ&NRxRSRP:RSRQandRSRPvaluesfortheneigh- of3xtimescomparedtothesame4Gscenario(peakrate97Mbps).
bouringcell. Thedifferenceisevenmoreevidentforthedrivingscenario,where
Thesemetricsallowmulti-purposeanalysisincludingacompar- the5G-supporteddeviceachievedarateof532Mbps,5xtimeslarger
isonofdifferentHASapproaches,handoverprediction,coverage than4G(peakrate108Mbps).
analysis,mobilitypredictionetc.Table1summarisesthemobility
patternsusedtogeneratethedataset: 4.2 Filedownloadvs.streaming
Table4showsacomparisonbetweenperformancemetricsfordiffer-
Table1:MobilityPatterns
entapplicationtypes.Intuitively,continuousfiledownloadhasthe
Type Summary highestaveragethroughputandvariationrange.NetflixandAma-
StaticStatictrials(indoorandincarscenarios) zonPrimeconsumesignificantlylessbandwidth,asseeninFigure1,
Car Trialsincludeurbanandsuburbanscenarios andisaconsequenceofapplicationbehaviour.Figure1 depictsa
boxplotillustratestherelationshipbetweenCQIandapplication
In conjunction with the different mobility patterns, different throughputandshowstherangeofthroughputvaluesforeachCQI
downloadapproachesweretaken,andthesearesummarisedin separately.Overall,weobserveanincreasingtrendinthroughput
Table2: proportionaltoCQI.However,therangeofthroughputvaluesoscil-
latessignificantlyforeachCQI.ForAmazonPrime,lowerbitrates
Table2:ApplicationPatterns resultinsimilarthroughputratesacrossallCQIvalues.Streaming
servicesdownloadsegmentsonlyduringtheONphase(bufferfill-
Type Summary
ing).Also,bandwidthdemandislimitedbythemaximumquality
FileDownload Continuouslargefiledownload
Netflix Netflixserviceproviderstreamedvideocontent ofencodedvideocontent.Overall,Netflixconsumessignificantly
AmazonPrimeAmazonPrimeserviceproviderstreamingvideocontent morebandwidththanAmazonPrimeforbothmobilitypatterns,
asaresultofthehigherencodingqualityandthuslargersegment
sizes.Next,weanalysethecollectedtraceslatencyperformance.For
4 PRODUCTIONDATASETOVERVIEW thestaticanddrivingscenarios,theaveragelatencyis75and90ms,
Thissectiongivesashortoverviewoftheproductiondatasetforthe respectively.Thisperformanceismuchhigherthanthetargeted
aforementionedmobilityandapplicationspatterns.Themajority 1ms,whichisexpectedtobeachievedasthetechnologymatures.
ofthecaseswerecollectedduringthemorningandeveninghours
andcanbefurtherclassifiedascommutetraces. 5 5G/MMWAVESIMULATIONFRAMEWORK
In[16],wepresentedourpreviousworkwhichcontainedbotha
4.1 4Gvs.5G
productionandsynthetic4Gtracedatasetcomposedofclient-side
We start by comparing the throughput of traces collected over cellularkeyperformanceindicators(KPIs).Thesyntheticdataset
the4Gand5Gtechnologies.For4G,weuseourpreviouslycol- wasgeneratedfromalarge-scale4Gns-3simulationthatincludes
lecteddataset[16].Toofferafaircomparison,weonlycompare onehundredusersrandomlyscatteredacrossaseven-cellcluster.
tracesfromthesamemobileoperatorandwiththesamemobility Thissyntheticdatasetwasbeneficialinthatitprovidesadditionalin-
patterns.Furthermore,onlythescenariowithfiledownloadiscom- formationthatisnotavailableintheproductiondataset,specifically
paredacrosstwomobiletechnologies.Weuseaveragethroughput aboutthebasestation(eNodeBoreNB)environmentsuchasnum-
andvariationrangeasperformancemetrics.Variationrangeisa berofuserscompetingatcellandchoiceofschedulingdiscipline.
percentile-wisemeasureofvariation.Let’sdefine𝑅asapplication Ourworkon4Gpriorusedtheopen-sourceNS-3LENAproject[3].
305

MMSys’20,June8–11,2020,Istanbul,Turkey DarijoRaca,DylanLeahy,CormacJ.Sreenan,andJasonJ.Quinlan
Table3:Average/VariationRangeofApplicationThroughput(Mbps)acrossdifferentmobilitypatternsandnetworktechnolo-
gies(filedownloadscenarioonly)
MobilityPatterns
|     |     | NetworkTechnology |     |     |                   |     | Static  |              |               |            | Car     |              |     |
| --- | --- | ----------------- | --- | --- | ----------------- | --- | ------- | ------------ | ------------- | ---------- | ------- | ------------ | --- |
|     |     |                   |     |     | Avg.Var.Range     |     | #Traces | TraceDur.(m) | Avg.Var.Range |            | #Traces | TraceDur.(m) |     |
|     |     | 5G                |     |     | 66.9 (22.0,202.5) |     | 5       | 260          | 28.5          | (3.0,88.5) | 16      | 459          |     |
|     |     | 4G                |     |     | 42.6 (21.3,77.2)  |     | 5       | 39           | 22.3          | (3.2,49.1) | 12      | 290          |     |
Table4:Average/VariationRangeofApplicationThroughput(Mbps)acrossdifferentmobilitypatternsandapplicationtypes
MobilityPatterns
|     |     | Application  |     |               |              | Static  |              |     |                 |     | Car                  |     |     |
| --- | --- | ------------ | --- | ------------- | ------------ | ------- | ------------ | --- | --------------- | --- | -------------------- | --- | --- |
|     |     |              |     | Avg.Var.Range |              | #Traces | TraceDur.(m) |     | Avg.Var.Range   |     | #Traces TraceDur.(m) |     |     |
|     |     | Filedownload |     | 66.9          | (22.0,202.5) |         | 5            | 260 | 28.5 (3.0,88.5) |     | 16                   | 459 |     |
|     |     | Netflix      |     | 13.7          | (0.5,31.1)   |         | 10           | 576 | 7.5 (0.4,19.9)  |     | 23                   | 637 |     |
|     |     | AmazonPrime  |     | 6.9           | (0.3,11.2)   |         | 8            | 582 | 1.3 (0.3,2.7)   |     | 21                   | 628 |     |
|     |     |              |     |               | 35           |         |              |     |                 |     | 4.0                  |     |     |
70
3.5
| 60                  |     |     |     |     | 30               |     |     |     |     |                  |     |     |     |
| ------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
|                     |     |     |     |     | 25               |     |     |     |     |                  | 3.0 |     |     |
| )spbM(tuphguorhT 50 |     |     |     |     | )spbM(tuphguorhT |     |     |     |     | )spbM(tuphguorhT |     |     |     |
2.5
| 40  |     |     |     |     | 20  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.0
| 30  |     |     |     |     | 15  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.5
| 20  |     |     |     |     | 10  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.0
| 10  |     |     |     |     | 5   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.5
0
|     |     |     |     |     | 0   |     |     |     |     |     | 0.0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
|     |                 | CQIIndex |     |     |     |     |            | CQIIndex |     |     |     | CQIIndex       |     |
| --- | --------------- | -------- | --- | --- | --- | --- | ---------- | -------- | --- | --- | --- | -------------- | --- |
|     | (a)FileDownload |          |     |     |     |     | (b)Netflix |          |     |     |     | (c)AmazonPrime |     |
Figure1:BoxplotofCQIvsapplicationthroughputforacrossdifferentapplicationtypes(driving)
Forthecurrent5Gworkwealsobuilduponapublishedfull-stack start_mmwave.pyusesseveralconfigurableflags,asshownin
simulationinfrastructureofthens-3mmwavemodule[11]. Listing1,totakeuserinputdirectlyfromthecommandline.These
Ourcontributionistobuilduponsaid4Gand5Gsimulationmod- inputscanbedisplayedwhenexecutingthescriptwiththe-hflag.
elsandcreateaflexibleandhighlycustomisable5G/mmwave[11] Theuserinput,asdefinedinTable5,isconfigurablethroughthis
ns-3 simulation framework, which generates a trace dataset of script.Thisscriptalsoconfiguresthesimulationenvironmentby
KPIsacrossnumerous5GUEsandeNBs.Exampleoutputincludes removingoldlogfiles,thatmayinterferewiththesimulation,and
time-serieschannelqualityindicators:CQI/SNR/RSRP/RSRQas outputstheuser-providedvariablestothecommandlineinterface
wellasthroughputratesforthedifferentevaluationscenarios.The beforecallingtheexecution.Whilethesimulationisexecuting,
frameworkproducesdataforadefinednumberof5Gbasestations thisscriptwillrepeatedlyscantodeterminewhenthesimulator
andclients,typicallyinaLineOfSight(LOS)levelenvironment. processbeginsloggingandreadscurrentsimTimefromaspecial
The5Gsimulationframeworkandgenerateddatasetprovidesa logfile,timelog.txt,andoutputsthecurrentsimTime.Additionally,
uniquemechanismtoviewtherelationshipofthechannelquality thescriptcallsauxiliaryscriptsappropriatetohandlesaidlogging.
indicatorsbetweenthenetwork(s)andtheclient(s)inalarge-scale
| 5G simulation. | All | code3, build | and | usage | instructions4 | for | our |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Listing1:PythonTestTemplate
5G/mmwavens-3simulationframeworkareavailableonline. 1#pythonstart_mmwave.py−ue%s−enb%s−t%s−src%s
−log%s−x%s−y%s−z%s
2
| 5.1 FrameworkConfiguration |     |     |     |     |     |     |     |     | −xVel%s−yVel%s−zVel%s−i%s |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- |
3
Table5illustratesthesimulationinputconfigurationfields,cat-
egorisedbywhereinthecodethesefieldsareconfigured,anda Inordertogeneratethroughputandend-to-endlatencyinfor-
defaultvalueanddescriptionforeach.Foreaseofuse,apython2 mation,aremotehostisintroducedtothesimulation.Thisremote
script,start_mmwave.pyisprovidedtoinitiateexecution.Thisscript nodeactsasthedestinationforpacketsgeneratedbytheUEand
handlesuserinputandredirectsns-3commandlineoutputtoa thesourceofpacketsthateachUEreceives.Theintentionforusing
thisremotenodeistobehaveasapseudo-Internetserver.
dedicatedloggingfilesystemforsubsequentparsingoncethesim-
| ulationcompletes. |     |     |     |     |     |     |     | 5.2 | SimulatingMobilityandHandover |      |            |                    |          |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | ---- | ---------- | ------------------ | -------- |
|                   |     |     |     |     |     |     |     | The | simulation                    | area | hosts many | UE nodes scattered | randomly |
3https://doi.org/10.5281/zenodo.3751194
4https://github.com/uccmisl/5Gdataset.git throughout. The number of UEs is configurable by the user, as
306

BeyondThroughput,TheNextGeneration:
A5GDatasetwithChannelandContextMetrics MMSys’20,June8–11,2020,Istanbul,Turkey
Table5:ns-35G/mmWaveConfigurableAttributesandSimulationDefaultValues
| Field    | Script | ConfigVia.Description                                          |     |     |
| -------- | ------ | -------------------------------------------------------------- | --- | --- |
| simTime  | -t     | Terminal Default1.0seconds.Lengthoftimetorunthesimulation.     |     |     |
| numUe    | -ue    | Terminal Default1.ThenumberofUEtosimulate.                     |     |     |
| numEnb   | -enb   | Terminal Default1.ThenumberofeNBtosimulate.                    |     |     |
| maxX     | -x     | Terminal Default100.ThesizeofthesimulationspacealongtheX-axis. |     |     |
| maxY     | -y     | Terminal Default100.ThesizeofthesimulationspacealongtheY-axis. |     |     |
| maxZ     | -z     | Terminal Default100.ThesizeofthesimulationspacealongtheZ-axis. |     |     |
| maxXVel  | -xVel  | Terminal Default100.ThemaximumvelocityofUEalongtheX-axis.      |     |     |
| maxYVel  | -yVel  | Terminal Default100.ThemaximumvelocityofUEalongtheY-axis.      |     |     |
| maxZVel  | -zVel  | Terminal Default0.ThemaximumvelocityofUEalongtheZ-axis.        |     |     |
| interval | -i     | Terminal Thetimeintervalinthecompleteddatasets.                |     |     |
|          | -src   | Terminal ThedirectorylocationoftheNS3wafexecutable.            |     |     |
|          | -log   | Terminal Thedirectorytostorelogs.                              |     |     |
minX notdefined Source Default0.AssumedtobeirrelevantduetotheabilitytoconfiguremaxXeasily.
| minY | notdefined | Source Default0.AssumedtobeirrelevantduetoconfiguremaxYeasily. |     |     |
| ---- | ---------- | -------------------------------------------------------------- | --- | --- |
minZ notdefined Source Default0.MmWavemoduledoesnotsupportundergroundsimulation(yet).
DataRate notdefined Source Defaultvalueconformstotheexpected/promissoryvalueof5G/mmWave.Adjustmentrarelyrequired.
LinkDelaynotdefined Source Defaultvalueconformstotheexpected/promissoryvalueof5G/mmWave.Adjustmentrarelyrequired.
|     | 𝑛∈{5,7,8,9},⌈ | √𝑛⌉=1,1∗1 | 5.3 | SimulationEvaluationandDataset |
| --- | ------------- | --------- | --- | ------------------------------ |
|     | eNB           | eNB       | eNB | Structure                      |
Inordertotestthefunctionalityandconfigurationsofourproposed
frameworkseveraltestcasesimulations,asdetailedinFig3,areused
tovalidateourdesignandimplementation.Thesetestsareexecuted
multipletimesoverasinglesimulatedsecond.Runningoverasingle
secondwithanintervalof0.1gives100entriesfortheuplinkand
|     | eNB | eNB | eNB |     |
| --- | --- | --- | --- | --- |
»»» » downlink of each UE and eNB. This setting produces adequate
dataforthesakeofcomparisonwhileremainingwithinreasonable
|     |     | UE  | runtimes.Thegeneratedoutputlogsaregatheredandsavedas |     |
| --- | --- | --- | ---------------------------------------------------- | --- |
numerousUEandeNBdatasetsinafoldercalled“mmwave_log”.
WhencomparedtheselogsproducethesamestructureforallUEs
andeNBs.Figure4illustratesanexampleofthesampleoutput.
|     | eNB | eNB | eNB |     |
| --- | --- | --- | --- | --- |
Toprovideeaseofuse,wealsoofferanUbuntu19.10VirtualBox
VMcontainingallrequireddependenciesandour5Gframework5.
Figure2:20ScatteredUEsandMobility,eNBlayoutfor𝑛 ∈
{5,7,8,9},ArrowsDenotingMobility UsernameandpasswordfortheprovidedVMis“godashbed”.
6 USECASE
Theproductiondatasetandtheoutputofthesimulationframework
arebothexceptionallyadaptivebydesign,allowinguserstocapture
avarietyofscenarios.Thus,thereareawideassortmentofpotential
usesforthegenerateddata.Thesepotentialusesextendtoindus-
triesandfieldssuchasmachinelearning,networking,researchand
development.DetailedexamplesarepresentedinTable6.
Figure3:SampleTestCases
7 CONCLUSION
Inthispaper,wepresenta5Gtracedatasetcollectedfromamajor
ismaximumvelocity.Thesimulationrandomlyselectsvaluesbe-
Irishmobileoperator,andalarge-scalemulti-cell5G/mmwavesim-
| tween the | minimum (no | movement) and maximum | velocity to |     |
| --------- | ----------- | --------------------- | ----------- | --- |
ulationframework.The5Gdatasetiscomposedofclient-sidekey
assigntoeachUE.ThetravelpathoftheUEsfollowtheGaussian
performanceindicators,andillustratesthevarianceinthroughput
Mobilitymodelandwillchangedirectionwhenencounteringthe
demandinbothclientstreamingandfiledownloadscenarios.The
boundsofthesimulationarea.Atrandomintervals,UEvelocity
5Gframeworkoffersamechanismtoinvestigatelargescaledeploy-
willchangetoanotherrandomlygeneratedvelocity.UEsinitially
mentsofmobiledevicesinamulti-cell5Genvironment.Tothebest
connecttotheclosesteNB.Fromhere,astheymovethroughoutthe
ofourknowledge,thisisthefirstpubliclyavailabledatasetthat
simulationarea,theywillconnectviahandovertowhichevereNB
containsthroughput,channelandcontextinformationforreal-time
providesthemwiththebestconnectionatanygiventime.This
environmentisvisualisedinFigure2. 5http://cs1dev.ucc.ie/misl/5Gframework/5G-ns3-ubuntu19.10.zip
307

MMSys’20,June8–11,2020,Istanbul,Turkey DarijoRaca,DylanLeahy,CormacJ.Sreenan,andJasonJ.Quinlan
Table6:ProposedUseCases
Industry/Field Use Explanation
MachineLearning PredictiveModels Analysingdatasetstorevealpredictednetworkperformance[14,22,23].
DistributionAnalysis Revealingdistributionsandcorrelationsbetweenunderlyinglow-levelstatistics.
GenerativeModels Analysisofdatasetcouldbeusedtotrainagenerativemodeltoproducenewdata.
Networking Prototyping Prototypingtheperformanceofproposed5G/mmWavenetworktopologies[21].
Training Educatingwould-be5G/mmWavenetworkengineersontheunderlyingconceptsof5G/mmWave.
Research Experimentation Providingasimulatedenvironmentinwhichtoconductexperiments[11,15].
ResultConfirmation Confirmingpublishedresultsofotherresearchers5G/mmWaveprojects[12].
Development Software/HardwareTestingByintroducingcustombehaviourrepresentativeofnewsoftware/hardwareintothesimulation.
[3] NicolaBaldoetal.2011.AnOpenSourceProduct-orientedLTENetworkSimula-
torBasedonNs-3.InProceedingsofthe14thACMInternationalConferenceon
Modeling,AnalysisandSimulationofWirelessandMobileSystems(MSWiM’11).
[4] AyubBokanietal.2016.ComprehensiveMobileBandwidthTracesfromVehicular
Networks.InProceedingsofthe7thInternationalConferenceonMultimediaSystems
(MMSys’16).ACM,Article44,6pages.
[5] L.DeCiccoetal.2013.ELASTIC:AClient-SideControllerforDynamicAdaptive
StreamingoverHTTP(DASH).InIEEEInternationalPacketVideoWorkshop.
[6] M.Cosovicetal.2017.5GMobileCellularNetworks:EnablingDistributedState
EstimationforSmartGrids.IEEECommunicationsMagazine55,10(Oct2017),
62–69. https://doi.org/10.1109/MCOM.2017.1700155
[7] T.-Y.Huangetal.2014.ABuffer-basedApproachtoRateAdaptation:Evidence
fromaLargeVideoStreamingService.InSIGCOMM.ACM.
[8] ManishJainetal.[n.d.].End-to-endEstimationoftheAvailableBandwidthVaria-
tionRange.InProceedingsofthe2005ACMSIGMETRICSInternationalConference
onMeasurementandModelingofComputerSystems(SIGMETRICS’05).12.
[9] J.Jiangetal.2014.ImprovingFairness,Efficiency,andStabilityinHTTP-Based
AdaptiveVideoStreamingWithFestive.IEEE/ACMTransactionsonNetworking
22,1(Feb2014).
[10] L.Lietal.2015.AmeasurementstudyonTCPbehaviorsinHSPA+networkson
high-speedrails.In2015IEEEConferenceonComputerCommunications(INFO-
COM).2731–2739. https://doi.org/10.1109/INFOCOM.2015.7218665
[11] MarcoMezzavillaetal.2018.End-to-EndSimulationof5GmmWaveNetworks.
https://ieeexplore.ieee.org/document/8344116
[12] ArvindNarayananetal.2019. AFirstMeasurementStudyofCommercial
mmWave5GPerformanceonSmartphones. arXiv:cs.NI/1909.07532
[13] J.Nightingaleetal.2018.5G-QoE:QoEModellingforUltra-HDVideoStreaming
in5GNetworks.IEEETransactionsonBroadcasting64,2(June2018),621–634.
https://doi.org/10.1109/TBC.2018.2816786
[14] DarijoRacaetal.2019. EmpoweringVideoPlayersinCellular:Throughput
PredictionfromRadioNetworkMeasurements.InProceedingsofthe10thACM
MultimediaSystemsConference(MMSys’19).AssociationforComputingMachin-
ery,NewYork,NY,USA,201–212. https://doi.org/10.1145/3304109.3306233
[15] DarijoRaca,MaëlleManifacier,andJasonJ.Quinlan.2020. goDASH-GO
Figure4:Sample5G/mmwaveoutput
acceleratedHASframeworkforrapidprototyping.InProceedingsofthe12th
InternationalConferenceonQualityofMultimediaExperience(QoMEX’20).
analysisofaproduction5Gnetwork.Asthens-3cellularmodel
[16] DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,andCormacJ.Sreenan.2018.
evolvestoincludesub-6Ghzvariations,infutureworkwewould BeyondThroughput:A4GLTEDatasetwithChannelandContextMetrics.In
plantoextendoursimulationframeworktocombinebothmmwave 9thACMMultimediaSystemsConference(MMSys’18).460–465.
[17] HaakonRiiseretal.2013.CommutePathBandwidthTracesfrom3GNetworks:
andsub-6Ghz,asthiscombinationissuggestedinreal-worldnext
AnalysisandApplications.InProceedingsofthe4thACMMultimediaSystems
generation5Gnetworks. Conference(MMSys’13).ACM,114–118.
[18] T.Stockhammer.2011.DynamicAdaptiveStreamingoverHTTP–Standardsand
DesignPrinciples.InMMSys’11ProceedingsofthesecondannualACMconference
ACKNOWLEDGMENTS
onMultimediasystems.NewYork,133.
Thispublicationhasemanatedfromresearchconductedwiththe [19] LiyangSunetal.2018.Multi-PathMulti-Tier360-DegreeVideoStreamingin5G
Networks.InProceedingsofthe9thACMMultimediaSystemsConference(MMSys
financialsupportofScienceFoundationIreland(SFI)underGrant ’18).AssociationforComputingMachinery,NewYork,NY,USA,162–173.
13/IA/1892,andisco-fundedundertheEuropeanRegionalDevel- [20] J.vanderHooftetal.2016.HTTP/2-BasedAdaptiveStreamingofHEVCVideo
Over4G/LTENetworks.IEEECommunicationsLetters20,11(2016),2177–2180.
opmentFundunderSFIGrant13/RC/2077.WealsothankAndrew
[21] Q.Xiaoetal.2014.TCPPerformanceoverMobileNetworksinHigh-SpeedMo-
NashandKieranHorganfortheirinvaluableassistanceinevaluat- bilityScenarios.In2014IEEE22ndInternationalConferenceonNetworkProtocols.
ingthe5G/mmwavemodule. 281–286. https://doi.org/10.1109/ICNP.2014.49
[22] XiufengXieetal.2015. piStream:PhysicalLayerInformedAdaptiveVideo
StreamingoverLTE.InProceedingsofthe21stAnnualInternationalConference
REFERENCES onMobileComputingandNetworking(MobiCom’15).ACM,413–425.
[23] C.Yueetal.2017. LinkForecast:CellularLinkBandwidthPredictioninLTE
[1] M.Agiwaletal.2016.NextGeneration5GWirelessNetworks:AComprehensive
Networks.IEEETransactionsonMobileComputing(2017).
Survey.IEEECommunicationsSurveysTutorials18,3(2016),1617–1655.
[2] TanweerAlam.2018. AReliableCommunicationFrameworkandItsUsein
InternetofThings(IoT).
308