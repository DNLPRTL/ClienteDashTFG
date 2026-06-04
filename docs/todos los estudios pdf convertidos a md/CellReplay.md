CellReplay: Towards accurate record-and-replay
for cellular networks
William Sentosa, University of Illinois Urbana-Champaign; Balakrishnan
Chandrasekaran, VU Amsterdam; P. Brighten Godfrey, University of Illinois
Urbana-Champaign and Broadcom; Haitham Hassanieh, EPFL
https://www.usenix.org/conference/nsdi25/presentation/sentosa
This paper is included in the
Proceedings of the 22nd USENIX Symposium on
Networked Systems Design and Implementation.
April 28–30, 2025 • Philadelphia, PA, USA
978-1-939133-46-5
Open access to the Proceedings of the
22nd USENIX Symposium on Networked
Systems Design and Implementation
is sponsored by

CellReplay: Towards accurate record-and-replay for cellular networks
WilliamSentosa†,BalakrishnanChandrasekaran‡,P.BrightenGodfrey†•,HaithamHassanieh⋄
†UniversityofIllinoisUrbana-Champaign,‡VUAmsterdam,•Broadcom,⋄EPFL
Abstract similartoalivenetwork.Simulatorsandemulators,suchas
ns3[28]orLinux’snetem-tc,offervariousoptionsforcon-
The inherent variability of real-world cellular networks
figuringdelay,jitter,bandwidth,packetloss,andmore.While
makesithardtoevaluate,reproduce,anddebugtheperfor-
theycanadjusttheseparameterstoemulatespecificandreal-
manceofnetworkedapplicationsrunningonthesenetworks.
isticconditions,properlytuningthemtoaccuratelyrepresent
A common approach is to record and replay a trace of ob-
thedynamicbehaviorofreal-worldcellularnetworksremains
servedcellularnetworkperformance.However,weshowthat
achallengingandopenproblem.
thestate-of-the-artrecord-and-replaytechniqueproducesem-
Amorerealisticapproachistorecordnetworkperformance
piricallyinaccurateresultsthatcancauseevaluationbias.This
traces(e.g.,latency,bandwidth,orpacketloss)overtimeus-
paperpresentsthedesignandimplementationofCellReplay,
ingpredefinedworkloads(e.g.,RTTprobing)onareal-world
atoolthatrecordsthetime-varyingperformanceofalivecel-
networkandreplaythosetracesinanemulatednetworkfor
lularnetworkintotracesusingpresetworkloadsandfaithfully
thetestedapps.Thismethodallowsforrecordingdifferent
replaystheobservedperformanceforotherworkloadsthrough
tracesundervariousconditions(e.g.,locations)andtesting
anemulatednetworkinterface.Thekeychallengeinachiev-
multipleappsusingsuchrecordedtraces.Record-and-replay
inghighaccuracyistoreplayvaryingnetworkbehaviorina
emulationwaspioneeredbyNobleetal.[27].Morerecently,
waythatcapturesitssensitivitytotheworkload.CellReplay
theMahimahinetworkemulator[25]canalsoreplayrecorded
records network behaviorundertwo predefined workloads
cellularnetworktracesandhasbeeninstrumentalinthedesign
simultaneouslyandinterpolatesuponreplayforotherwork-
andevaluationofseveralnotablenetworkedsystemsandpro-
loads. Across various challenging network conditions,our
tocols(e.g.,[5,14,18,20,24,26,30,31,36,37,39,41,43,45,46]).
evaluationshowsthatreal-worldnetworkedapplications(e.g.,
However,we found that Mahimahi can produce inaccu-
web browsing or video streaming) running on CellReplay
rateresultscomparedtoreal-worldtestsinimportantcases,
achievesimilarperformance(e.g.,pageloadtimeorbitrate
particularlyforlatency-sensitiveandburstyworkloads.For
selection)totheirlivenetworkcounterparts,withsignificantly
instance,inourevaluation,weobservedanaveragebiasof
reducederrorcomparedtothepriormethod.
approximately17.1%inwebpageloadtimes(PLTs)when
1 Introduction comparingMahimahiemulationtorunningtheapplicationin
thesamecommercialcellularenvironmentwherethetraces
Cellularnetworkperformance,includingbandwidthandla- wererecorded.Thiserrorisapersistentunderestimationof
tency,canvarysignificantlyduetofactorssuchaswireless thePLTratherthanjustrandomvariation.Thisissueaffects
interference,environmentalobstructions,andhandovers,es- otherapplicationsaswellandtheerrormayevenbegreater.
peciallyinmobileenvironments[12,13,22,23,34].Thegold Forexample,weobserveda49%errorfor250KBfiledown-
standardforevaluatingapplicationandprotocolperformance loadswhenMahimahiemulatedacommercialVerizon5Gas
oncellularnetworksis,hence,totestthemdirectlyonlive shownin§5.6.
cellularnetworks.However,livetestingistime-consuming,as Thus, despite record-and-replay emulation being practi-
experimentsmustbeconductedacrossmanydifferentnetwork calandwidelyused,itdoesnotsupporthigh-fidelitytesting
conditionsandcanproducedifferentresults—duetodifferent ofnetworkedsystemsandprotocols.Minimizingemulation
signalstrengths,typesofwirelessservice(e.g.,5Gmillime- erroriscrucial,particularlyforwirelessprotocolandapplica-
terwave,5Glow-band,and4G),kindsofinterference,rates tionresearch,whererecord-and-replayemulationsareoften
of mobility,physical locations,etc. Repeating each experi- themostfeasibleevaluationplatform.Theseerrorscouldaf-
mentmultipletimesiscrucialtoensurestatisticallyreliable fectanyevaluationandmayevenalteritsconclusions,aswe
resultsgiventheperformancevariabilityincellularnetworks. demonstratedintheABRalgorithmsusecase(§5.9).There-
Inadditiontobeingtime-consuming,experimentsareoften fore,weasked:Whatiscausingthisemulationerror?And,is
difficulttoreproduce.Alackofcontrolovertheenvironment thereawaytofixittofaithfullyrecordandreplayreal-world
makesitinfeasible,forinstance,tocomparetheeffectsofa cellularnetworkperformance?
protocolchangeunderidenticalnetworkconditions. Ourfirstcontributionistostudyhowtherecord-and-replay
Thus,researchersandappdevelopersoftenturntosimu- methodusedbyMahimahicanresultinpersistentbias(§3).
lationoremulationformuchoftheirevaluation,hopingto Mahimahirecordspacketdeliveryopportunitiesbycontinu-
replicatearepresentativeenvironmentthatyieldsperformance ouslysaturatingthelinkwithpackets(a“saturator”workload)
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation 1169

andnotingwhenpacketsarriveattheendpoint.Itthenreplays trace during longer packet sequences before eventually re-
thistraceasascheduleforwhenthelinkcandeliverpackets turningtothelighttraceafteranidleperiod.Thistechnique
afterdelayingthosepacketsusingafixedpropagationdelay, addressesthetwokeyproblemswithMahimahi’sapproach
foranyworkload. mentionedabove,namelycapturing(1)dynamicRTTsand
However,wefoundthatthismethodcausestwofundamen- (2)bandwidththatdependsonworkload.
talissues.First,itfailstofullycapturenetworkbaselatency WeimplementedCellReplayusinganarchitecturesimilar
changes, which are prevalent in cellular networks. In fact, to Mahimahi—an emulated network interface that can be
ourmeasurementsshowthatMahimahiunderestimatesRTT usedbyunmodifiedapplications.Usingrandomizedtrials,we
by 13.25% and 16.88% across two operators. Second,the evaluatedCellReplay’saccuracybycomparingtheapplication
available bandwidth that a cellular network provides to an performancewhen runningunderCellReplayemulation to
end-to-endconnectiondependssignificantlyonthatconnec- thelivenetworks.Wetestedtwocommercialproviders’5G
tion’s workload1. For example, in our measurement using mid-bandandlow-banddeployments,andcoveredmultiple
Verizon5G,alongtrainwith100back-to-backpacketsexpe- networkconditions,includingnon-idealconditions(e.g.,ina
riences2.6timeshigherdeliveryratethanashorttrainwith crowdedlibrary)andmobility(e.g.,driving).Weevaluated
10packets.Insuchcases,Mahimahi’ssaturator(i.e.,heavy tworeal-worldapplicationtrafficpatterns: randomizedfile
traffic)wouldseeahigherratethanwhatshortertrafficshould downloadsandwebpageloadswithHTTP/1.1andHTTP/2.
experience.Thisdependencybetweencellularnetworkavail- Theseapplicationscoveravarietyofworkloads,rangingfrom
ablebandwidthandworkloadposesafundamentalchallenge periodicsmalltoheavyflowsinfiledownloadstocomplex
forrecord-and-replay because the whole pointis to record interleavedtrafficfromwebpageloads.Additionally,weused
onetrace(whichisnecessarilyrunningoneworkload)and CellReplaytoevaluatethestartupphaseofmultipleadaptive
replaythattrace undera variety ofapplications fortesting. bitrate(ABR)implementationsfor4Kvideostreaming.
Ifavailablebandwidthdependsontheworkload,isfaithful WefindthatCellReplaysubstantiallyreducesemulation
record-and-replayfeasible? error. In web page load tests, CellReplay reduces emula-
Oursecondcontributionistoaddressthesefundamental tion error from 17.1% with Mahimahi to 6.7%, represent-
problems in a record-and-replay system calledCellReplay. ing a 60.8% improvement. For randomized file download
Tosolvetheworkload-dependenceproblem,oneobviousap- tests,CellReplaylowersmeanfiledownloadtimeerrorsfrom
proachwouldbetorecordperformanceundereverypossible 7.9%-49% with Mahimahi to just 0.2%-22.4%. Moreover,
workload.However,thisisimpracticalanddegeneratesinto CellReplayachieveslowererrorwhenreplicatingapplication
simplytestingeveryapplicationdirectlyonthelivenetwork, performanceundernon-idealnetworkconditions,suchasin-
whichiswhatrecord-and-replayemulationistryingtoavoid. side a basement (15.22% error in Mahimahi vs. 5.87% in
Inotherwords,wecanonlyrecordalimitednumberofdiffer- CellReplay)andacrowdedlibrary(22.51%vs.8.47%),and
entworkloads.Anotheroptionwouldbetobuildawhite-box duringusermobility,suchaswalking(14.48%vs.4.13%)and
emulationofproviders’underlyingresourceallocationpoli- driving (13.15% vs. 6.97%). Finally,we demonstrate Cell-
cies;buttheseareproprietaryandvaryacrossproviders,sowe Replay’susefulnessinevaluatingABRalgorithms,asitpre-
seekablack-boxmethodbasedonend-to-endobservations. servestherelativeorderingofABRperformanceandavoids
Theapproachwetakeistorecordjusttworepresentative thebiasesobservedinMahimahi.Wediscusschallengesand
workloads (light and heavy) simultaneously, chosen at ex- futuredirectionsforimprovementin§6.WereleaseCellRe-
tremesontherangeoftrafficpatterns,andtheninterpolate playalongsidewithitsrecordedtracesasanopensourceat
betweenthemduringreplaytoachievehighaccuracyacross https://github.com/williamsentosa95/cellreplay
awiderangeofworkloads.Duringtherecordingphase,we
2 Backgroundandrelatedwork
usetwophones:onerunningaheavysaturatorworkloadand
theotherrunningalightworkload.Thelightworkloadiscali- 2.1 Cellularnetworkrecord-and-replay
bratedtocaptureRTTsandlight-workloadbandwidth,butis Thegoalofrecord-and-replaynetworkemulation(withinthe
nottoolightastocapturethenetwork’stransitionfromlight scopeofthispaper)istoemulatetheend-to-endnetworkper-
toheavybandwidthallocations.Duringreplay,theemulator formanceofanapplicationcommunicatingbetweentwoend-
appliesdelayusingtheRTTtraceandinitiallyreleasespack- points,ensuringperformancesimilartothatofalivenetwork
etsaccordingtothelighttrace. Itthensplicesintheheavy counterpart.Duringtherecordingphase,userequipment(UE)
andtheserversendtrafficaccordingtoapredefinedworkload
1Tobeclear,thiseffectisnotduetoqueuingbehaviorofatraditionallink
(e.g.,sendingpacketsbeyondthelinkbottleneckrate),while
withconstantthroughputandlatency;norisitcausedbyvariationsinwireless
physicalchannelqualityovertime.Althoughcommercialproviders’internal observedperformancemetrics(e.g.,throughput)arelogged.
policiesareproprietaryandopaquetous,theeffectcouldbeexplainedby Thisworkloadshouldbeindependentofthetestedapplica-
aresourceallocationpolicy(e.g.[9])oracarrieraggregationpolicy(as tions,allowingustorecordtracesonceandreusethemfor
observedin [40]) atthe Radio Access Network(RAN) allocating some
multipleapplications,regardlessofwhethertheyareUDP-or
bandwidthforthe client,butobserving the client’s injectedpackets and
dynamicallymodifyingthatprovidedbandwidth. TCP-based.Duringreplay,thistraceisconsumedbyanemu-
1170 22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

latednetworkinterface.Realapplications(e.g.,awebbrowser Record phase
andwebserver)canconnectthroughthisinterface,andtraffic Saturator sends packets Packets are arrived at:
continuously t=46t=38t=30 t=10 t=0
betweentheendpointswillexperienceartificialnetworkcon-
ditions(e.g.,time-varyinglatencyandbandwidth)asifthey 4G/5G Released at the next
were communicating over a cellular network,even though Replay phase Fixed delay PDO: delivery opportunity
Sent at =20 Released at 0, 10, 30, 38, 46 Released
they reside on the same physical host. Our goal is for any t=0 t=20 at t=30
Delay Link
metricsofinterest—includingtransport-levelandapplication- emulator emulator
levelmetricssuchasflowcompletiontimeorwebPLT—to Figure1:AnoverviewofMahimahi’srecord-and-replaytoemulate
closelymatchthoseofthelivenetwork. cellularuplink.
Record-and-replay can be applied to any type of net-
work forrecording and replaying HTTP traffic [25] called
work, but our interest here is on cellular networks. Their
Mahimahi,whichalsoincludedanetworkemulatorderived
performance can be time-varying, vendor-dependent, and
fromCellSim[38]toreplaytime-varyinguplinkanddown-
environment-dependent, making it difficult to generate
linkratesincellularnetworks.Mahimahihassincebecome
conditions—whether in simulators, emulators with hand-
the state-of-the-art record-and-replay emulator for cellular
pickedorevencalibrated[42]parameters,ortestbeds—that
networksandiswidelyusedtoevaluatevariousnetworked
matchreal-worldcomplexity.Thus,record-and-replayises-
applications.
peciallyusefulinsuchenvironments,butitisalsochallenging
WedetailMahimahi’srecord-and-replayapproach2,asit
toexecutewell.
servesasanimportantreferenceforthispaper.Fig.1illus-
Notethatrecord-and-replaydealswithend-to-endcondi-
tratestheprocessfortheuplinkonly,asthesameapproach
tionsanddoesnotrequireanylink-orphysical-layerinfor-
appliestothedownlink.Mahimahirecordstime-varyinglink
mationorsupportfromnetworkoperators.Likepastwork,
ratesusingaSaturator,whichsaturatesboththeuplinkand
wedonotneedtodeterminewhichhopsalongthepathcause
downlinkwithMTU-sizedpackets(e.g.,1500bytes)toen-
certain performance effects. This means that the observed
surethatthebasestationalwayshaspacketstodeliver.The
performance,anditsreplay,mayresultfromacombinationof
endpointthen records the arrivaltime ofeachpacket. Dur-
sources(e.g.,the5GRAN,serviceprovidercore,ortheInter-
ingemulation,Mahimahitreatseacharrivaltimestampasan
nettoaremoteendpoint).However,majorperformancevaria-
opportunity to delivera packet. A sequence of such times-
tionsareexpectedtooriginatefromthecellularnetwork[22].
tampsconstitutesapacketdeliveryopportunity(PDO)trace.
Wesometimesrefertotheobservedperformanceascoming
EachPDOentryrepresentsanopportunitytodeliveranMTU-
fromacellularlink,thepath,orsimplythenetwork;allterms
sizedamountofdata,whichcanbeeitherasingleMTU-sized
areequivalentforourpurposes.
packetormultiplesmallerpacketswhosecombinedsizesadd
2.2 Relatedwork uptotheMTU.Ifnopacketsarequeuedfordeliverywhen
thePDOoccurs,theopportunityislost.Mahimahialsoem-
Network emulators. Popular network emulators, such as ulatestheRTTdelaysonacellularlink,albeitusingafixed
NetEm [16] and dummynet [32],can emulate cellular net-
propagationdelay.Thatdelayisdeterminedbymeasuringthe
works.GoogleChromealsoprovidesconfigurationprofiles
minimumpacketRTT(e.g.,viaICMPping)andhalvingthat
withfixedlatencyandbandwidthforcellularnetworks,such
value.
as "Fast" and "Slow" 3G [3]. Pantheon [42] provides cali-
bratedemulatorsbasedonparameterslikefixedpropagation 3 Liverecord-and-replayishard
delay,bottlenecklinkrate,isochronicity,etc.Theseconfigu-
Why is record-and-replay challenging? Also,why does the
rationsaretunedtomatchpackettracescollectedfromapath
currentstate-of-the-artmethod(i.e.,Mahimahi)failtoaccu-
(includingcellularnetwork)usingvariouscongestioncontrol
ratelyreplicatetheperformanceofnetworkedapplicationson
protocols.iBox[7]extendsthisbyincorporatingcross-traffic.
acellularnetwork?Below,weanswerbothquestionsusing
However,fixedparameters,bydefinition,donotcapturetime-
measurementsandinsightsfromrealcellularnetworks.
varyingeffects,whicharecommonincellularnetworks.
Themeasurementsinthissectionwerecollectedfromtwo
Record-and-replaynetworkemulation.Nobleetal.pio-
commercialcellularnetworks: T-Mobile5Gmid-bandand
neeredtheconceptofrecordingtheend-to-endnetworkchar-
Verizon5Glow-band,usingaSamsungGalaxyS22(SGS)
acteristics of a wireless network and replaying them in an
phonetetheredtoalaptop.Thelaptop,equippedwithanIntel
emulatednetworkin1997[27].However,itisdesignedtoem-
i7CPUand16GBRAM,ranUbuntu20.04andservedasour
ulateWaveLAN,whichdiffersfundamentallyfrommodern
cellularnetworks.Morerecently,NemFi[21]wasintroduced 2ThismethodwasintroducedbyCellSim.Mahimahialsoprovidestraces
asarecord-and-replayemulatorforWiFi.NemFi’sdesignis recordedinCellSim’sapproach,whichhavebeenbeneficialandusedin
specifictoWiFi(e.g.,emulatingframeaggregation)anditis pastwork(e.g.,[20]).Duetoitsusefulness,otherworkhascollectednewer
cellularnetworktracesfollowingCellSim’sapproach(e.g.,[19,26])and
notreadilyapplicabletoemulatingcellularnetworkpaths.
replayedtheminMahimahi.Forsimplicity,throughouttherestofthispaper,
Mahimahi.In2015,Netravalietal.demonstratedaframe- werefertothisrecord-and-replaymethodasMahimahi.
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation 1171

T-Mobile Verizon (a) Record (b) Replay with a sparse workload
|     |         |     |      |     |     | 𝑡! 20ms    |     | 40ms 𝑡#    |      | 𝑡!r 20ms                         | 40ms |      |
| --- | ------- | --- | ---- | --- | --- | ---------- | --- | ---------- | ---- | -------------------------------- | ---- | ---- |
|     | 1.0     |     | 1.0  |     |     |            | 𝑡"  |            |      |                                  | 𝑡"   | 𝑡#   |
|     |         |     |      |     |     | Sende r    |     |            | Time | Sende                            |      | Time |
|     | 0.8     |     | 0.8  |     |     |            |     |            |      |                                  |      |      |
|     | FDC 0.6 |     | 0.6  |     |     |            |     |            |      | Apply a fixed prop delay of 20ms |      |      |
|     | 0.4     |     | 0.4  |     |     |            |     |            |      |                                  |      |      |
|     |         |     | Live |     |     |            |     |            |      | Delay emu                        |      |      |
|     | 0.2     |     | 0.2  |     |     | delay=20ms |     | delay=40ms |      |                                  |      |      |
Mahimahi
|     | 0.0 |                 | 0.0   |                 |       |          |     |       |     |                  | Release  based on the PDO |     |
| --- | --- | --------------- | ----- | --------------- | ----- | -------- | --- | ----- | --- | ---------------- | ------------------------- | --- |
|     |     | 40 50           | 60 70 | 40 50           | 60 70 | Live     |     | 20ms  |     |                  |                           |     |
|     |     |                 |       |                 |       | network  |     | gap   |     |                  |                           |     |
|     |     | Packet RTT (ms) |       | Packet RTT (ms) |       |          |     |       |     | Link emu         |                           |     |
|     |     |                 |       |                 |       | Receiver |     |       |     | ReceiverD=20ms ✅ |                           |     |
Figure 2: PacketRTTCDFofMahimahiemulationandlive5G D=40ms✅20ms❌
networks.MahimahiunderestimatestheRTTandfailstocapturethe Figure3:MahimahiPDOapproachfailstocapturethebasedelay
changesforsparseworkload.
RTTdistribution.
client. Theserverwaslocatedwithincloseproximity(<10 propagationdelayapproachmayperformevenworse.
ThisisbecausePDOs,inprinciple,onlypartiallycapture
miles)oftheclient.Weconfirmedthatallresultsremained
|     |     |     |     |     |     | base delay | changes. | Figure | 3   | illustrates | a case | where the |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | --- | ----------- | ------ | --------- |
consistentwhenusingadifferentphonemodel(GooglePixel
| 5). |     |     |     |     |     | packet | base delay | changes | at  | t from | 20ms to | 40ms, and |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | ------- | --- | ------ | ------- | --------- |
2
Mahimahifailstoapplythecorrectdelayforacertainpacket.
3.1 VariabilityinbaseRTT
Notethatbasedelaychangesmayoccasionallyoccurinlive
The base RTT is defined as the round-trip time (RTT) of cellular networks due to factors such as increased retrans-
apacketfromtheclienttotheserverwhenthereisnoself- mission delays caused by a weakened radio signal. In this
inflictedcongestion.Incellularnetworks,thisRTTisexpected illustration,duringtherecordingphase,thefourpacketsde-
tobevariable,aspacketsfrequentlyexperiencedelays(jitter) livered from t to t experience a 20ms base delay, while
1 2
duetolink-layerretransmissions,channelcontention,base packetsfromt 2 tot 3 experiencea40msbasedelay.There-
stationscheduling,anddevicemobility.Emulatingthisvari- ceiverindeedperceivesadelaychangesince,afterreceiving
abilityiscriticalfortestinglatency-sensitiveapplicationssuch fourpackets,itdoesnotreceiveanypacketsfor20msbefore
asVR/ARandremotedriving. receivingthenextset.This20ms“blackout”periodisalso
Mahimahialsoemulatesdelayvariabilitybasedonpacket reflectedinthePDOtraceduringthereplay.
| delivery | traces. | Despite | using a | fixed propagation | delay,it |     |     |     |     |     |     |     |
| -------- | ------- | ------- | ------- | ----------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
APDOblackoutmeansnopacketdelivery.Anypackets
mustholdthepacketuntilitseesaPDObeforereleasingit scheduledfordeliveryduringthisperiodwillbedelayedun-
(Fig.1).However,ourmeasurementssuggestthatitfailsto tilthe nextavailable opportunity. As a result,onlypackets
fullycapturethebaseRTTvariability.Toquantifythiserror, arrivingduringtheblackoutperiod(relativetothelinkemu-
wecomparedthepacketRTTreportedinliveexperimentwith lator)willexperienceadelay,whileotherswillnot.However,
thatofMahimahi.
sparseworkloads,suchasthoseinFig.3b,mayhavepackets
Specifically,weconductedrepeatedpacketRTTtestsand arrivingoutsidetheblackoutperiodandthusnotexperiencing
| Mahimahirecordingsindividuallyoverlivenetworks,follow- |     |     |     |     |     | anydelay. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
ingtherandomizedtrialapproach(§5.3).ThepacketRTTtest Conclusion:FixedpropagationdelayandPDOsareinsuf-
involvesaclientsendinga1400-byteUDPpacket(roughly ficienttomodelcellularnetworkdelayvariability.Therefore,
anMTU-size)every50mstoourechoserverandnotingeach
|     |     |     |     |     |     | we need | to record | packet | RTTs | overtime | through | probing |
| --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ---- | -------- | ------- | ------- |
packet’sRTT.Werepeatedthistest10times,andboththeRTT during the recording phase and apply time-varying delays
| testandMahimahirecordingsessionlasting60seconds.Next, |         |            |            |            |            | duringthereplay. |     |     |     |     |     |     |
| ----------------------------------------------------- | ------- | ---------- | ---------- | ---------- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- |
| we                                                    | ran the | exact same | packet RTT | test under | Mahimahi’s |                  |     |     |     |     |     |     |
3.2 Performancedependsonworkload
emulatedinterface,usingtherecordedtraceandsettingthe
propagationdelaytohalfoftheminimumRTTfromthelive RecallthatMahimahiusesaSaturatortoensurethatthenet-
packetRTTtests. work always has packets ready to send, and so any avail-
Figure2showsthecumulativedistributionfunction(CDF) ablePDOswillbeconsumedandrecorded. Then,asubset
ofthosePDOsisusedwhenreplayinganygivenworkload.
| of  | packet RTTs | on the | live network | and Mahimahi | replay. |     |     |     |     |     |     |     |
| --- | ----------- | ------ | ------------ | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
It indicates that Mahimahi underestimates packet RTT (by AnunderlyingassumptionisthatthesamePDOswouldhave
16.88%and13.25%atthemedianforT-MobileandVerizon, beenavailableforthereplayedworkload.However,ourex-
respectively),anditsdistributiondiffersfromthatofthelive periments on live cellular networks show that the network
network(asseenintheshapeoftheCDFcurve).Thissug- substantially changes the PDOs it provides depending on
gests thatsimplyincreasing Mahimahi’s fixedpropagation the workload. We reached this conclusion upon observing
delay(i.e.,shiftingtheCDFcurvetotheright)doesnotcap- thatshortflowsconsistentlyexperiencelowerbandwidththan
| turethevariability.Notethatthisexperimentwasperformed |     |     |     |     |     | longerflows. |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
understationaryconditionswithastrongsignal,wherenet- To demonstrate this, we conducted live experiments in
workperformanceismorestable.Inamobilescenario,where whichourserverperiodically sentpackettrains to a client.
packetRTTcanvarymoreorevenchange,Mahimahi’sfixed Each train consists of N back-to-back UDP packets, each
1172    22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

T-Mobile Verizon PDOpatternsrecordedbydifferenttrains. Foreachpacket
|     | 80  |     |     | 100 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
noitelpmoc niarT P ∈{P ,...,P } in eachtrain,we calculatedits relative
|     |     |     |     | 90  |     |     |     | i 0 | N−1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)sm( emit
70 80 arrivaltimeast(P)−t(P i 0 ),wheret(·)denotesthereceiver’s
70
observedarrivaltimeofapacket.Wepresentthemeanrel-
|     | 60  |     |     | 60  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
330Mbps 220Mbps ativearrivaltimeasafunctionofpacketsequencenumberi
|     |     |             | Link BW | 50    |         | Link BW |     |                         |     |            |     |     |     |
| --- | --- | ----------- | ------- | ----- | ------- | ------- | --- | ----------------------- | --- | ---------- | --- | --- | --- |
|     | 50  |             |         | 40    |         |         |     | fordifferenttrainsizesN |     | inFigure5. |     |     |     |
|     | 0   | 100 200 300 | 400 500 | 0 100 | 200 300 | 400 500 |     |                         |     |            |     |     |     |
Train size Train size Theseresultsconfirmthatthelink’srate(orPDO)depends
Figure4:Meantraincompletiontime(TCT)ofdifferentsizedtrains ontheworkload.Thenetworkprovidesalowerdeliveryrate
(N),andTCTiftrainsweredeliveredaccordingtotheSaturator’s forthefirstfewpacketsinanytrain(notethatintheseplots,
observedbandwidth.
ahigherslopeindicatesalowerdeliveryrate).Asthetrain
progresses,thedeliveryrateincreases,andtheslopebegins
|     |     | N=200 | N=100 |     | N=10 |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
toapproachthatoftheSaturator.Wealsorepeatedthesame
|     |     | N=150 | N=50 |     | BW line |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
T-Mobile Verizon packettraintestsintheopposite(uplink)directionbutfound
lavirra evitaleR 30 thatthelink’srateremainsuniformregardlessofN (i.e.,it
)sm( emit
10
20 follows a straight line). We suspect that the rate-workload
|     | 5   |     |     | 10  |     |     |     | dependenceinthedownlinkresultsfromtheoperator’spro- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
prietarypacketschedulingimplementation.Forexample,cel-
|     | 0                      |        |         | 0                      |        |         |     |               |        |            |     |        |               |
| --- | ---------------------- | ------ | ------- | ---------------------- | ------ | ------- | --- | ------------- | ------ | ---------- | --- | ------ | ------------- |
|     | 0                      | 50 100 | 150 200 | 0                      | 50 100 | 150 200 |     |               |        |            |     |        |               |
|     |                        |        |         |                        |        |         |     | lular network | packet | scheduling | may | depend | on historical |
|     | Packet sequence number |        |         | Packet sequence number |        |         |     |               |        |            |     |        |               |
applicationtrafficandthecurrentqueuedepthwhenschedul-
| Figure5: | Meanrelativearrivaltimeforeachpacketofdifferent |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ingpackets[9].Thisrate-workloaddependencewasobserved
sized(N)trains.
|                                                 |     |     |     |     |     |     |     | across all     | conditions | tested | in §5,including |     | both peak and |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | ------ | --------------- | --- | ------------- |
| 1400bytes,followedbya100msgap—longenoughtoclear |     |     |     |     |     |     |     | off-peakhours. |            |        |                 |     |               |
outanypacketsfromprevioustrains).WerefertoN asthe Interestingly,T-MobileandVerizonhavedramaticallydif-
trainsize.Eachpacketinatrainistaggedwithatrainnum- ferentimplementations.T-Mobile’sdeliveryrateapproaches
berandasequencenumberreflectingitsorderwithinatrain
theSaturator’srate(slope)asiincreases,mostlyregardless
(P 0 ,...,P N−1 ).Theclientthenrecordseachpacket’sarrival ofN.Verizon’sdeliveryrate,ontheotherhand,asymptotes
time.Additionally,theclientsendsa100-byteACKbackto tosignificantlydifferentvaluesdependingonN,withlarger
(P
the server upon receiving the last packet of a train N−1 ). N approachingtheSaturator’sheavy-workloaddeliveryrate
The train completion time (TCT) is defined as the time at moreclosely.Additionally,inT-Mobile,thefirst50packets
| whichtheserverreceivestheACKminusthetimeitsentP |     |     |     |     |     |     | .   |                                                 |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
|                                                 |     |     |     |     |     |     | 0   | oftrainswithN>50aredeliveredmoreslowlythanthe50 |     |     |     |     |     |
Weperformedthistestwithdifferenttrainsizesfollowingour packetsofthetrainwithN=50,whereasVerizonshowsan
randomizedtrialapproach(§5.3).Eachtestlasted5seconds, invertedbehavior.Thisfurthercomplicatesrecord-and-replay,
andthereare12testswithdifferenttrainsizes(1,10,25,50,
|     |     |     |     |     |     |     |     | as we aim | for a | general | and relatively | accurate | approach |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------- | -------------- | -------- | -------- |
...,500)inonetrial.Werepeatedthistrial50times.Finally, acrossdifferentoperatorsandlocations.
wealsorecordednetworkperformancewiththeSaturator,as
Wealsofoundamoreminorwayinwhichperformance
Mahimahiwould. dependsonworkload:theRTTofapacketvarieswithpacket
| Figure | 4 shows | the mean | TCT | for | each train | size | on T- |           |           |     |           |                |         |
| ------ | ------- | -------- | --- | --- | ---------- | ---- | ----- | --------- | --------- | --- | --------- | -------------- | ------- |
|        |         |          |     |     |            |      |       | length by | an amount | not | explained | by throughput. | For in- |
MobileandVerizon5G.Thedashedblacklinerepresentsthe stance,basedonourmeasurementsonVerizon,theRTTof
TCTifthelinkhadafixedbandwidthequaltothatobserved a 100-byte packet is 6.8ms fasterthan that of a 1400-byte
bytheSaturator(equivalenttothemeanTCTwithMahimahi packet,eventhoughthedifferenceinserializationtimeatthe
replayingtheSaturator).Ifnetworkperformancewereinde- bottlenecklinkrate(60Mbps)shouldhavebeenonly≈0.17
pendentofworkload,thenthemeanbandwidthwouldremain
ms.Thisoutcomealignswithfindingsfromthepriorlatency
the same for all train sizes,and the mean TCT would fol- studyon5G[12]andmaybeattributedtotheadditionaltime
lowalinearfunctionoftheamountofdatabeingdelivered, requiredforreassemblinglargerdatachunks.Duetospace
i.e.,alinearfunctionofN.
|     |     |     | Inparticular,itshouldcoincide |     |     |     |     | constraints,weomitdetailedresults. |     |     |     |     |     |
| --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
withthebandwidthobservedbySaturator.However,theob- Conclusion: Cellular network performance can depend
servedTCTsdonotconformtoastraightlineandgenerally
significantlyontheworkload.Ourobservationsindicatethat
donotmatchtheSaturatorline,withTCTsbeingupto11.5% cellularprovidersallocatedeliveryrates(i.e.,bandwidthor
higherthantheSaturatorinT-Mobileand35.8%higherin PDOs)differentlyforlightandheavyworkloads.TheSatu-
| Verizon. | This | indicates | thatthe | service | experiencedby |     | the |     |     |     |     |     |     |
| -------- | ---- | --------- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ratorforcesthelinkintoitsheaviestworkloadmode,which
trainworkloadsisconsistentlyandsignificantlydifferentthan generallyincreasestheavailablebandwidth.Consequently,
theserviceexperiencedbytheSaturator’sheavyworkload.
usingSaturator’sPDOsforalighterworkloadcanresultin
To better understand these observations, we examined consistentbias(flowscompletefasterthantheyshould).This
thearrivaltimesofpacketswithineachtrain,revealingthe suggeststhatdiverseworkloadsareneededtocapturediffer-
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation    1173

entPDOs,butchoosing the rightrepresentative workloads (a) Send U packets (c) Construct uplink light PDOs
t=0 t=25 t=23 t=20
remainschallenging.
4 CellReplay t=40t=42 t=45t=47 t=51 4G/5G t=20
(d) Note RTT and downlink light PDOs (b) Send back D packets
4.1 Designoverview
Collected Time Delay Uplink Light PDOs Time Delay Downlink Light PDOs
At a high level, we want to solve the problems of captur- traces: 0 20 0 3 5 0 20 0 2 5 7 11
ingtime-varyingbaseRTT(§3.1)andworkload-dependent
Figure6:Packettrainworkloadalongsidewithitsrecordedbase
performance(§3.2)inbothrecordandreplay.
delayandlightPDOtracesforuplinkanddownlink.
Webeginwiththelatterproblem(§3.2).Toachievehighly
accurateemulation,anobvioussolutionistorecordperfor- arethenusedtoemulatethenetworkduringreplay.Thefol-
manceunderdifferentworkloads.However,recordingevery lowingsubsectionsdetaileachofthesecomponents:record
possibleworkloadisimpracticalanddegeneratesintosimply (§4.2)andreplay(§4.3),beforereturningtocalibration(§4.4),
testingtheappsdirectlyonthelivenetwork.Wealsoaimfor whichisbestunderstoodafterseeingtherestofthedesign.
therecordedworkloadtobeindependentofthetestedapps
4.2 Recordingnetworktraces
(§2.1). Therefore,we can only record a limited numberof
differentworkloads. There are three time-series metrics we want to record: (1)
From§3,weobservethatshortandcontinuoustrafficare basedelay,(2)lightPDOs,and(3)heavyPDOs.
handleddifferently,whilemedium-lengthflowsexhibitper- BasedelayandlightPDOs.Thebasedelaytraceshould
formancesomewherebetweentheextremes.Inspiredbythis reflectthenetwork’sround-triptime(RTT)withoutanyqueue-
observation,ourkeyapproachistorecordtwoworkloadscho- ingdelaysintroducedbytheworkloaditself.Ideally,thistrace
senattheextremepointsonthespectrumoftrafficpatterns: would be captured by periodically measuring the RTTs of
(1) Packet train probing to capture link PDOs under short smallpackets.Theone-waybasedelaycanbeestimatedby
andbursty load(lightPDOs),and(2) Saturator to capture halvingtheRTT.
PDOs under heavy continuous load (heavy PDOs). These LightPDOscanbecapturedbyperiodicallysendingalim-
workloadscapturetheessentialbehavioroflinkratedifferen- itednumberofback-to-backpackets,i.e.,apackettrain,in
tiationunderlightandheavyflows.Weusedtwophonesto both the uplink and the downlink. The number of packets
recordbothtracessimultaneouslyandshowinourevaluation shouldbesmallenoughtocapturethenetwork’slightwork-
thatinterferencebetweenthemislimitedinpractice. loadbehaviorandideallysomeofthetransitiontomoderate
Duringreplay,weleveragebothPDOstomatchthepro- workload,withoutpushingthenetworkintoheavyworkload
videdworkload.Whentheapplicationundertestbeginssend- mode.Inparticular,thetrainshouldbeshortenoughtoavoid
ingpackets,weinitiallyreleasethefirstsequenceofpackets “warmingup”thenetworkforthefollowingtrain.Asaresult,
according to the light PDOs and then transition to heavy boththebasedelaytraceandlightPDOssharesimilarrequire-
PDOsasthepacketsequencelengthens.Afteracertaingap ments. We can collect both simultaneously using a packet
intheworkload,wereturntothelightPDOtrace. train probing workload on a single device. This workload
Returningtotheproblemoftime-varyingRTT(§3.1),we usesMTU-sizedpackets,asasignificantamountoftrafficis
designthepackettrainstoavoidinflatingqueues,sothatit stillrequiredtocapturethetransitionpointbetweenlightand
givesusagoodmeasurementofbaseRTT.Thepackettrain heavymodes.
probingservesadualpurpose:torecordchangingbaseRTTs Figure6providesanexampleofhowthisprocessworks.
(foranyworkload)andPDOsforshorterpacketsequences. In every G ms,(a) the client sends U back-to-back MTU-
Finally,theeffectivenessoftheabovedesigndependson sizedpackets to the server. Upon receiving the firstpacket
parameter choices. For example,a too-small train will not ofthetrain,(b)theserversendsbackDback-to-backMTU-
capture the network’s light workload behavior completely, sizedpackets.Theserveralso(c)recordseachpacket’sarrival
forcing us to go to the heavy PDO trace too soon; if the withinthattrainandusesittocalculatetheuplinklightPDOs
trainsaretoolarge,wecannotsamplefrequentlyasnetwork asthearrivaltimeofeachpacketminusthearrivaltimeofthe
performance may then resemble that of a heavy workload, firstpacket(since,duringreplay,thebasedelaywillbeadded).
andthereisariskofinflatingbaseRTTmeasurementsdueto Whentheclientreceivesthecorrespondingdownlinktrain,
congestion.Thus,beforerecording,weconductacalibration (d)itinfersthecurrentbaseRTTasthereceipttimeofthe
phasetodeterminetrainsize,traingaps,andotherparameters firstdownlinkpacketminusthesendtimeofthefirstuplink
thatwillyieldtheleasterror. packet(withinthattrain).Itthencalculatesthedownlinklight
In summary, CellReplay has three components. When PDOsbasedonpacketarrivaltimes,justastheserverdid.
recordingnetworktracesinaspecificenvironment,wefirst HeavyPDOs.TheheavyPDOsarecollectedusingaSatu-
performanautomatedcalibrationofparametersinthaten- rator(similartoMahimahi)thatsaturatesthelinkwithpackets
vironment,andthen startrecording live traces byrunning beyonditsbottleneckrate,effectively“requesting”thelinkto
packettrainprobingandSaturatorinparallel.Thesetraces remaininmaxbandwidthmode.Inpractice,wedevelopedour
1174 22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Time Delay Light PDOs Heavy PDOs Table1:Parameterssetincalibrationphase(§4.4).
0 20 0 3 5 0 1 2 3 4 5 6 7 … 37 38 39 40 41 …
Parameter Definition
50 30 0 2 3
Packet P arrived at U Numberofpacketsperuplinktrain
• Temp base delay = 22
t=10, and triggered • Temp PDOs = 32 35 37 38 39 40 41 … D Numberofpacketsperdownlinktrain
an active state Gmin Lowerboundofgapbetweentrains(milliseconds)
Figure 7: TemporarybasedelayandPDOsconstructedwhena F Fallbacktimertoreturntoinactivestate
CellReplayfirstentersanactivestate. comp(s) Delaycompensationfors-bytepackets
B Bottleneckbuffersizeinbytes
ownSaturatortool,whichsendsMTU-sizedpacketsinboth
theuplinkanddownlinkatfixeduploadanddownloadrates,
ReplaythensavesDELAY andconstructstemporaryPDOs
eliminatingtheneedfortwophonesasinMahimahi’sSatura-
(TempPDO)byaddingeveryPDOentryinLightPDOwith
tor[38].Weoverestimated(by25%)themaxlinkbandwidth
t+DELAY.Itthenconcatenatesthesewiththesuffixofthe
measuredusinganexistingbandwidthtestapplicationlike
heavyPDOs,startingfromt+DELAY+max(LightPDO)+1.
iperforspeedtest.Weconfirmedthatthereportedthroughput
Thesystemisnowdoneenteringtheactivestate.
fromourSaturatorissimilartoUDPiperf.
Aslongasthesystemremainsintheactivestate,packets
However,runningbothSaturatorandpackettrainprobing
areinitiallydelayedbyDELAY plusasize-baseddelaycom-
onasingledeviceisnotfeasible,astheSaturatorwillover-
pensation comp(size(P)). As discussedin §3.2,base delay
loadthequeue,leadingtotwoissues:inflatingthebasedelay
maydependonpacketsize;thespecificadjustmentcomp(·)
measurementandkeepingthelinkinmaximumbandwidth
isdeterminedduringcalibration.DELAY andTempPDOre-
state.Onesolutionistoruntheseworkloadsinseparatetri- mainunchangedunlessthesystementersaninactivestate3.
als,which may be permissible under stationary conditions
Afterapacketisdelayed,itiseitherplacedinaPDOqueueor
but is less ideal undermobility. Alternatively,we chose to
droppedifthequeueexceedsBbytes.Packetsaredequeued
performtheseworkloadsonseparateidenticalphonesplaced
accordingtothetimescheduleinTempPDOusingbyte-wise
in close proximity. This is possible since most (if not all)
dequeueing.ThisprocessmirrorsMahimahi’sPDOreplay,
cellularnetworkprovidersemployuser-separatedqueues[38]
with CellReplay using the temporary (concatenated) PDO
suchthattheSaturatortrafficwillnotinflatethepackettrain
trace.Asaresult,earlypacketsintheactivestatewillexperi-
probingmeasurementresults.Beyondtheknownseparation
encelightPDOs,whilelaterpacketswillexperienceheavy
ofqueues,weconfirmedthatlightvs.heavybandwidthallo-
PDOs.OnceF millisecondspasswithoutanypacketsinthe
cationisalsoseparatedonbothVerizonandT-Mobile:when
PDOqueue,CellReplayreturnstotheinactivestate.Anyfu-
onephonerunstheSaturator,theotherphonerunningpacket
turearrivingpacketwillthentriggertheproceduretoreenter
trainprobingstillexperienceslight-workloadservice.
theactivestate,asdescribedabove.
Notethatthetwo-phonemethodisnotwithoutlimitations.
Thephonesmaynotalwaysconnecttothesamebasestation 4.4 ParameterCalibration
allthetime,especiallyinamobileenvironmentwherehand-
WedescribehowtoselectvaluesfortheparametersinTable1.
offscouldoccurslightlydifferently.Weleavethisdiscrepancy
TheparametersU,D,G ,F,andcomp(s)areexclusiveto
min
forfuturework.
CellReplayandarecalibratedineverynewenvironmentbe-
forerecordingtraces.Thisprocessisautomated.Bisastan-
4.3 Replayingnetworktraces
dardnetworkemulationparameter,derivedusingaclassical
CellReplaytakesinputtracesofbasedelay,lightPDOs,and max-minapproach[11].Fordetails,see§A.3.
heavyPDOsovertimetoemulatenetworkperformancein SettingUandD.Weprofilethenetworktodeterminea
avirtualinterface.Atahighlevel,CellReplayfirstappliesa packettrainsizethatprovidesthebestoverallapproximation
basedelaytoeachpacketbasedonthedelaytrace,adjusts
ofthenetworkacrossothersizes.Wefirstconductrandom-
thedelayforanylatencyoffsetfrompacket-sizecalibration
izedexperimentswithdifferentpackettrainsizes(thesame
(§4.4),andthenreleasespacketsaccordingtoeitherthelight
as §3.2)using a fixedtrain gapthatisconservativelylarge
orheavyPDOs.
enoughtoensurethelinkreturnstoitslight-workloadstate.
In moredetail,CellReplayoperatesin twostates: active
andinactive.Initially,CellReplayisintheinactivestateuntil 3ReplayingbaseRTTchangesduringtheactiveperiodcouldleadto
itreceivesapacketatsometimet,relativetothestartofthe double-counting,asPDOtracesalreadycapturesomeRTTchangesinthe
formofgapsbetweenPDOs. Whilethismightseemcounterintuitiveto
emulation.ThiseventtriggersCellReplaytoentertheactive
ourgoalofemulatingtime-varyingbasedelay,theissuediscussedin§3.1
state,whichinvolvespreparationasshowninFigure7.Cell- onlyariseswhenthereisagapintheworkloadpacketsthatemptiesthe
Replaysearchesforthemostrecentbasedelay(DELAY)and queue.However,insuchcases,CellReplayhasanopportunitytore-enterthe
lightPDOs(LightPDO)wherethetimestampis≤t. Since inactivestateandselectanotherbaseRTT.Althoughthereisaslightchance
thattheworkloadgapisshorterthantheinactive-statetimerF,Fistypically
the trace is sampled per G, linear interpolation is used to
small(e.g.,5milliseconds),sowedidnotfindthistobeamajorproblemin
assignDELAY topacketsarrivingbetweentwosamples.Cell- practice.
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation 1175

(cid:26)(cid:33)(cid:30)((cid:3) (cid:23)(cid:42)(cid:30)(cid:38)(cid:38)(cid:23)(cid:3)(cid:26)(cid:42)(cid:30)((cid:23) (cid:26)(cid:38)(cid:3)(cid:34)(cid:23)(cid:26)(cid:18) sen value (U orD,foruplink ordownlink,respectively,in
|     | (cid:9)(cid:11) | Error for N=200 |     | (cid:5)(cid:39)(cid:33)(cid:4)(cid:3)((cid:26)(cid:31)(cid:25)(cid:23)(cid:36)(cid:3)((cid:39)(cid:23) (cid:3)(cid:26)(cid:29)((cid:3)(cid:27)(cid:35) (cid:9)(cid:6) |     |     |     |     |     |     |     |     |
| --- | --------------- | --------------- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)(cid:39)(cid:33)(cid:4)(cid:3)(cid:26)(cid:33)(cid:30)((cid:3) (cid:23)(cid:42)(cid:30)(cid:38)(cid:38)(cid:23) (cid:9)(cid:6) E r ro r  separate experiments) and vary the gap g. We begin with
| (cid:26)(cid:42)(cid:30)((cid:23) (cid:26)(cid:38)(cid:3)(cid:34)(cid:23)(cid:26)(cid:18) | Error                    | f o r  |     | (cid:8)(cid:11) |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------------------------------------- | ------------------------ | ------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                                                           | (cid:8)(cid:11) for N=50 |        |     | (cid:8)(cid:6)  |     |     |     |     |     |     |     |     |
(cid:8)(cid:6) N=25 a conservatively large gap (as in the previous experiment)
(cid:7)(cid:11)
(cid:7)(cid:11) and test gaps of decreasing size; in our implementation,
|     | (cid:7)(cid:6) |     |     | (cid:7)(cid:6) |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:17)(cid:30)(cid:28)(cid:29)((cid:3)(cid:21)(cid:15)(cid:20)(cid:39)(cid:3)(cid:35)(cid:27)(cid:3)(cid:19)(cid:14)(cid:7)(cid:6)(cid:6) g∈100,90,80,...,10 ms. Let r (g) denote the mean rel-
(cid:11) (cid:16)(cid:26)(cid:23)(cid:42)(cid:43)(cid:3)(cid:21)(cid:15)(cid:20)(cid:39) (cid:11) last
(cid:6)
(cid:6) ativearrivaltimeofthelastpacketintrainswithgapg.Intu-
|     | (cid:6) | (cid:11)(cid:6) (cid:7)(cid:6)(cid:6) (cid:7)(cid:11)(cid:6) | (cid:8)(cid:6)(cid:6) | (cid:6) (cid:8)(cid:6) | (cid:10)(cid:6) (cid:12)(cid:6) (cid:13)(cid:6) (cid:7)(cid:6)(cid:6) |     |     |     |     |     |     |     |
| --- | ------- | ------------------------------------------------------------ | --------------------- | ---------------------- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
(cid:21)(cid:23)(cid:25)(cid:31)(cid:26)((cid:3)(cid:39)(cid:26)(cid:37))(cid:26)(cid:34)(cid:25)(cid:26)(cid:3)(cid:34))(cid:33)(cid:24)(cid:26)(cid:38)(cid:3)(cid:4)(cid:3)(cid:3)(cid:5) 𝒊 (cid:22)(cid:38)(cid:23)(cid:30)(cid:34)(cid:3)(cid:28)(cid:23)(cid:36)(cid:3)(cid:4)(cid:33)(cid:39)(cid:5) itively,asgdecreasestoatoo-smallsize,thelinkwillbegin
|     |     | (a) |     |     | (b) |         |                                  |     |     |     |        |           |
| --- | --- | --- | --- | --- | --- | ------- | -------------------------------- | --- | --- | --- | ------ | --------- |
|     |     |     |     |     |     | staying | in itsheavy-workloadmode,causing |     |     |     | r last | (g)to de- |
Figure8:(a)Estimatingerrorifa100-sizedtrainisusedtoestimate
|     |     |     |     |     |     | crease. We | set G | as the | smallest | g for which |     | r (g) is |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ------ | -------- | ----------- | --- | -------- |
{25,50,200}-sizedtrains.(b)Gminischosenasthesmallesttrain min last
within20%ofitsvaluewiththeconservativelylargegap,i.e.,
gapthatresultsinperformancesimilartoalargetraingap(i.e.,
r last (100ms).IntheexampleofFig.8(b),CellReplayselects
30ms).
G =30ms.
min
Inourimplementation,weusea100msgap,andthesetof InferringF.RecallthatF determineshowlongCellRe-
trainsizesweconsideris{5,25,50,75,...,X}whereX is play’semulatedlinkremainsidleintheactivestatebefore
chosensuchthattheresultingmeansendingrate(including transitioningbacktotheinactivestate.WederiveF usingthe
gapsbetweentrains)ishalfofthebottleneckthroughput. samedatacollectedtoselectG min ,whichinvolvescalculating
Afterrunningfor10trials,wecomputeR (i)foreachtrain the difference between G and the time required for the
|                                                      |     |     |     |     | N   |                                   |         |     | min         |      |               |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------- | ------- | --- | ----------- | ---- | ------------- | --- |
|                                                      |     |     |     |     |     | queuetoclear,whichisobservableasr |         |     |             | (G   | ).Fordetails, |     |
| size,whichrepresentsthemeanrelativearrivaltimeofthe  |     |     |     |     |     |                                   |         |     |             | last | min           |     |
| i-thpacketinanN-packettrain.Therelativearrivaltimeis |     |     |     |     |     | see§A.2.                          |         |     |             |      |               |     |
|                                                      |     |     |     |     |     | Inferring                         | comp(). | We  | profile how | RTT  | is affected   | by  |
thepacket’sarrivaltimeminusthatofthefirstpacketinits
train. R essentially represents the mean lightPDOs ofan packetsizebysendingrandomlysizedpacketsbetween{100,
N
N-sizedtrain.WefurtherdefineR∗(i)astheestimatedmean 200,...,1400}bytesevery50mstoareceiverthatresponds
N
arrivaltimeofthei-thpacketinreplaymode,assumingwe witha100-byteACK.WethenmeasuretheRTTdifference
choose to record trains of size N. More specifically,recall forapacketsizeofscomparedtotheRTTof1400-bytepack-
thatduringreplay,wefollowlightPDOsbeforesplicingin etsandmodelthisdifferenceascomp(s).Wedescribethisin
the heavy PDOs; therefore, R∗(i) = R (i) for i ≤ N, and moredetailin§A.1.
|                   |     |                                | N   |     | N   |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| otherwise,R∗(i)=R |     | (N)+heavy(i−N),whereheavy(x)is |     |     |     |     |     |     |     |     |     |     |
|                   |     | N N                            |     |     |     |     |     |     |     |     |     |     |
5 Evaluation
thedeliverydelayofxpacketsbasedonthemeanthroughput
oftheheavyworkload.
|     |     |     |     |     |     | Our goal | is to evaluate | the | accuracy | of CellReplay’s |     | emu- |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | -------- | --------------- | --- | ---- |
ThepurposeofR∗
(i)istohelpuscalculatetheestimation lation in replicating application performance compared to
N
| error | of R | (N) (i.e., the | mean | relative | arrival time of the |                  |              |     |         |         |            |     |
| ----- | ---- | -------------- | ---- | -------- | ------------------- | ---------------- | ------------ | --- | ------- | ------- | ---------- | --- |
|       | N    |                |      |          |                     | its live network | counterpart. |     | We also | compare | CellReplay |     |
lastpacketofanN-packettrain)foreveryothertrainsizeN
withMahimahi[25].WeimplementedCellReplayrecordtool
thatwehavetested.LetLbethetrainsizeusedtoestimate inJavaandPython3tosendandreceiveUDPpackets.We
theerrorforothertrains.Fig.8(a)showstheestimationerror
extendedtheMahimahishelltosupportCellReplayreplay,
whenusingL=100.ThebluelineisR∗
(i),whichrepresents allowingunmodifiedapplicationstoruninsidetheshelland
100
thePDOsbasedontheconcatenationofmeanlightandheavy experiencetheemulatednetworkconditionsinducedbyCell-
| PDOs.IfweusethattoestimateR |     |     |     | (N)ofothertrainsN∈ |     |                                  |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------------ | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
|                             |     |     |     | N                  |     | Replay.Formoredetails,referto§B. |     |     |     |     |     |     |
{25,50,200},thepredictionwillresultinsomeerror(shown TheevaluationincludesexperimentsthattestCellReplay’s
| in red). | For | each train | size L,we | compute | the mean error |     |     |     |     |     |     |     |
| -------- | --- | ---------- | --------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
accuracyacross(1)differentnetworkedapplications,includ-
overalltestedtrainsizes,andourchosentrainsizeistheL ingwebbrowsingandrandomfiletransfersusingTCP,(2)dif-
that yields the smallest mean error. We conduct the entire ferentcellularprovidersandtechnologies,includingT-Mobile,
procedureintwodirections(uplinkanddownlink)separately
|     |     |     |     |     |     | Verizon,5G | mid-band,and5G |     | low-band,and(3) |     |     | different |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | --------------- | --- | --- | --------- |
tochoosethetrainlengthsU andD. environmentalconditions,suchasgoodsignalstrength,weak
| FindingG |     | .IfthetraingapGistoosmall,thelinkwill |     |     |     |                                        |     |     |     |     |                |     |
| -------- | --- | ------------------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | -------------- | --- |
|          |     | min                                   |     |     |     | signalstrength,crowdedareas,andvarious |     |     |     |     | mobilitylevels |     |
not have enough time to reset to its light-workload mode (stationary,walking,anddriving).Forfulldetailsontheenvi-
before the next train arrives. We typically set G=50 ms ronmentsandtheircalibrationparameters,referto§C.Finally,
forstationaryconditionsandG=100msformobilecondi-
wepresentausecaseofusingCellReplayandMahimahito
tions.However,incertainenvironments,thismaynotbelarge evaluateABRalgorithms.
| enough.WethusaimtofindG |     |     |     | ,thesmallestvalueatwhich |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
min
5.1 Experimentalsetup
thelinkhasenoughtimetoreturntoitslight-workloadmode,
ensuringthatourchosenGisatleastthatvalue. Wedesignedtwotestsetups:alivenetworkandanemulation
Weconductanotherrandomizedexperiment,thistimetest- testsetup,asshowninFigure9.Thelivenetworktestsetup
ingdifferenttraingaps.Again,wesendsequencesoftrains; was used forrunning application tests on the live network.
however, in this case, we fix the train length at our cho- Duringthetests,wetetheredalaptoptophonesconnected
1176    22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

eachforlandingandinternalpagescorrespondingtothe10th,
Internet
|          |     |         |     |     |           |     | 30th,50th,70th,and90th |     |     | percentilesofthedistribution. |     |     |     | We  |
| -------- | --- | ------- | --- | --- | --------- | --- | ---------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
| La p t o | p   | U S B   |     |     | S e r v e | r   |                        |     |     |                               |     |     |     |     |
tet h e re d 4G/5G use ’L-ID’ and’I-ID’ to referto an individuallanding and
| C li e n | t  Tunnel |     |     | Tunnel | S e r v e | r   |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
App App internalpage,respectively. ’ID’ is a numberindicating the
Phone
orderbasedonpagesize,wherelowervaluesrepresentsmaller
Live network test setup
pagesizes.Referto§Dfortheexactlistofpagesandtheir
| Laptop     |     |               | High-speed  |     |     | Server     | pagecomposition). |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | ----------- | --- | --- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| C li e nt  | E   | m u la t e d  | Ethernet    |     |     | Se r v er  |                   |     |     |     |     |     |     |     |
A p p Tunnel in te r fa c e Tunnel A p p WeutilizedMahimahi’sHTTPrecord-and-replayframe-
|     |     |     |     |     |     |     | work [25] | to replay | these | pages,ensuring |     | that | the | fetched |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----- | -------------- | --- | ---- | --- | ------- |
Emulation test setup
contentforagivenpageremainedconsistentacrossalltrials.
Figure9:Livenetworkandemulationapplicationtestsetup.
|          |              |     |            |             |         |     | First,we | recorded | all | HTTP | requests | and responses |     | using |
| -------- | ------------ | --- | ---------- | ----------- | ------- | --- | -------- | -------- | --- | ---- | -------- | ------------- | --- | ----- |
| to 5G or | 4G networks. |     | The client | application | (e.g.,a | web |          |          |     |      |          |               |     |       |
mitmproxy[2],followingMahimahi’srecordformat,while
browser)andtheapplicationserver(e.g.,awebserver)com-
loadingawebpageusingaheadlessChromiumbrowser.Next,
municateviaaUDPtunnel(basedon[42]).Wedeployedour
weusedMahimahi’sReplayShelltoservetheresponsesover
| server(i.e.,the | remote | endpoint) |     | in the same | geographical |     |     |     |     |     |     |     |     |     |
| --------------- | ------ | --------- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theHTTP/1.1(usingApache2)orHTTP/2(usingh2ofrom
area–within10milesofthephones–tominimizethenetwork
the[47]extension).
pathlengthand,consequently,reducethelikelihoodofexpe-
Inourtestsetup(Fig.9),ReplayShellwasdeployedonour
riencingcongestionoverlongpaths.Wealsousedasimilar
|     |     |     |     |     |     |     | server,while | the | laptop | ran | a headless | Chromium |     | browser |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | ---------- | -------- | --- | ------- |
setup,albeitwithoutatunnel,torecordthecellularnetwork
torepeatedlyfetchawebpage.Weclearedthebrowserand
tracesusingUDPtraffic.However,insteadofasinglephone,
DNScachesbeforeeveryweb-pagefetch,andweusedTCP
weusedtwoidenticalphonestoseparatelyperformpacket
|     |     |     |     |     |     |     | Cubic, the | default | TCP | implementation |     | on  | Linux, | for this |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | -------------- | --- | --- | ------ | -------- |
trainprobingandtheSaturatorworkload.
test.Lastly,wemeasuredpage-loadtime(PLT),basedonthe
Weusedtheemulationtestsetuptotestapplicationsunder
onLoadevent[29],astheapplicationperformancemetric.
anemulatednetworkinterfacethatemployedeitherCellRe-
Randomfiledownloadtest.Forthistest,weimplemented
play’sorMahimahi’sreplayapproach.Althoughthissetup
|            |             |         |         |      |     |           | a client  | that sends | download |         | requests | (each  | fewer     | than 10 |
| ---------- | ----------- | ------- | ------- | ---- | --- | --------- | --------- | ---------- | -------- | ------- | -------- | ------ | --------- | ------- |
| is similar | to the live | network | test,we | made | two | modifica- |           |            |          |         |          |        |           |         |
|            |             |         |         |      |     |           | bytes) to | a server.  | Each     | request | selects  | a file | uniformly | at      |
tions:(1)wereplacedtheUSB-tetheredinterfacewithadi-
|     |     |     |     |     |     |     | random | from a | list of | files of | varying | sizes,and | the | server |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------- | -------- | ------- | --------- | --- | ------ |
recthigh-speedEthernetconnectiontoourserverviaasingle
|     |     |     |     |     |     |     | delivers | the corresponding |     | file | data. | After | completing | the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | ---- | ----- | ----- | ---------- | --- |
switch,and(2)weranthetunnelinsideeitherCellReplay’sor
|     |     |     |     |     |     |     | transfer,the | client | then | sleeps | for 50ms | before | requesting |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ---- | ------ | -------- | ------ | ---------- | --- |
Mahimahi’sreplaynetwork-emulationshell,whichemulates
anotherfile.WeimplementedtheclientandserverinPython
thenetworkusingrecordedtraces.Thesameclientandserver
andusedTCPSockets.Wemeasuredthefiledownloadtimeas
deviceswereusedforrecordandreplay.
theturnaroundtimebetweenwhentheclientsendsitsrequest
End-pointspecifications.WeusedtwoSamsungGalaxy
andwhenitreceivestherequestedfile.
S22(SGS)andtwoGooglePixel5(Pixel)phonesfortesting.
AdaptivevideostreamingoverHTTP.Weranaclient-
WehadanunlimiteddataplanfrombothT-MobileandVeri-
serversetupfrom[4,20],whichincludesmultipleadaptive
zon.Sinceweobservednoperformancedifferencebetween
bitrate(ABR)streamingimplementations.However,instead
theSGSandPixelacrossdifferentoperators,weconnected
ofusingthe2Kvideofromthatsetup,ourserverhostsa250-
ourSGSdevicestoT-MobileandourPixeldevicestoVer-
|                     |     |                                |     |     |     |     | second-longAVC4Kvideo(indoor |     |     |     |     | soccerfrom[35])with |     |     |
| ------------------- | --- | ------------------------------ | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | ------------------- | --- | --- |
| izonforconvenience. |     | Thelaptopinoursetupsfeaturedan |     |     |     |     |                              |     |     |     |     |                     |     |     |
a4-secondchunkdurationencodedwith12bitratesof[100,
IntelCorei7CPU,16GBRAM,anda512GBSSD,running
|     |     |     |     |     |     |     | 200, 375, | 550, | 750, 1000, | 1500, | 3000, | 5800, | 7500, | 12000, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---------- | ----- | ----- | ----- | ----- | ------ |
Ubuntu20.04.
17000].WeusedaChromiumbrowsertorunthevideoplayer.
5.2 ApplicationsunderTest
| We testedCellReplay’s |     |     | fidelityusing | two | real-worldappli- |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.3 Methodology
| cations: | (a) web-page | loads,which |     | exhibit | complex | traffic |     |     |     |     |     |     |     |     |
| -------- | ------------ | ----------- | --- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
patternsandrepresentthemostpopularapplicationtypeon Randomizedtrials.Whenevaluatinganetworkedsystem’s
mobiledevices,and(b)randomfiledownloads,whichhave performanceontheCellReplayemulatedinterfaceversusthe
simplertrafficpatternsbutinvolvelarge-sizedflows. livenetwork,wemustaccountforcellularnetworkvariability.
Webpageloadtest.OurclientranaChromiumbrowser Thus,allourexperimentsusedrandomizedtrials.Eachexper-
to loada webpage from ourserver. To generate the listof imentcomprisedmultipletrials,witheachtrialconsistingof
webpagesforourtesting,webeganbyrandomlyselecting multipletestsandrecordingsessions.Atestinvolvedrunning
200internalandlandingpagesfromtheHisparlist[6].Using anapplication(e.g.,loadingawebpage)onalivenetwork,
Chromium,we loaded all pages and recorded each page’s whilearecordingsession(e.g.,CellReplayrecord)gathered
total size of the compressed web objects. We then sorted atraceofthelivenetwork.Thetestsandrecordingsessions
the pages based on this total size and selected five pages ranforthesameduration,andwerandomizedthesequence
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation    1177

of tests and sessions within each trial. We then compared Fortrainslongerthan75packetsonT-Mobileand100packets
theapplication’sperformance(acrossmultipletests)onthe onVerizon,CellReplayachieveslowerinterpolationerrors
livenetworktothatontheemulatednetworktocalculatethe thanMahimahi’ssingle(heavy)PDOapproach,reducinger-
emulationaccuracy. rorsfrom26.68%to6.44%onT-Mobileandfrom43.24%
Calculatingtheemulationaccuracy.Wequantifiedem- to 7.74% on Verizon fora train size of 200. CellReplay ’s
ulation errorusing the normalized difference between two interpolationerrorsforlongertrainshighlightanopportunity
distributionsofapplicationperformance:onefromthelive forfutureimprovement.
networkandtheotherfrom theemulation. Tomeasure the When running these experiments, the primary phone
differencebetweenthesedistributions,weusedEarthMover’s recorded the base delay while the secondary continuously
Distance(EMD)[33],definedas:EMD(L,T)=
(cid:82)+∞|L(x)−
sentpackets;theresults,hence,suggestthatthetwo-phone
−∞
T(x)|dx,whereLandT arethecumulativedistributionfunc- setuphadminimalinterference.
tions(CDFs)oftheobservedapplicationperformanceonthe
5.5 Webbrowsingtest
liveandemulatednetworks,respectively.AlowerEMDvalue
indicatesahigh-fidelityemulation,meaningtheperformance WeevaluatedCellReplay’saccuracyforthewebbrowsingby
distributionsaremoresimilar.Finally,wecalculatedtheemu- fetchingbothlandingandinternalpages(listedinTable3)
lationdistributionerrorbydividingtheEMDwiththemean usingHTTP/1.1andHTTP/2.Asbefore,weconductedthese
(performance)valuefromthelivenetworktests. testsunder“good”networkconditions,withtheUEsplaced
Otherdetails.Ineachnewnetworkenvironment(ornet- nearawindow.Foreachoperator,weconductedfourexper-
workoperator),wefirstperformedacalibration. Torecord iments,witheachrandomizedexperimentconsisting of10
CellReplaytraces,weusedonephone(primary)forpacket trials.Eachtrialincludedfetchingfivepagesusingthelive
trainprobingandtheother(secondary)forrunningtheSatura- networkandtworecordingsessions–oneforCellReplayand
tor.Theprimaryphonewasalsousedforcalibration,testing theotherforMahimahi.Eachtestandrecordingsessionlasted
applications on the live network,and recording Mahimahi for60s.Intotal,wespentapproximately9.33hconducting
traces using our own Saturator. For propagation delay,we theseexperiments.
providedMahimahiwiththeminimumbasedelayobserved CellReplay outperforms Mahimahi across all page load
fromthepackettrainworkload.Duringdatacollection,both tests(Figure11).Itachievesanemulationdistributionerror
phones (UEs) were heldtogetherata close distance (≈12 between1.2%-17.7%,withameanerrorof6.7%.Incontrast,
inches).Wealsoconfirmedthatbothprobingdeviceswere Mahimahi has errors ranging from 4.5% to 42.6%,with a
attached to the same cell in all tests,except in the driving mean errorof17.1%. On average,CellReplay reduces em-
case. ulationerrorby60.8%forweb-browsingappscomparedto
Mahimahi.Pageloadtrafficistypicallydominatedbysmall
5.4 Microbenchmarks
objecttransfers,whicharesensitivetoRTTandcategorizedas
WefirstevaluatedhowaccuratelyCellReplayemulatesthe lighttraffic.Mahimahi’sunderestimationofRTTandoveres-
time-varyingbaseRTTandthenon-uniformdeliveryrateina timationofPDOsfromtheSaturatorleadtosignificanterrors
cellularnetwork.WeconductedpacketRTTandpackettrain forsmallflows(see§5.6).AllMahimahi’serrorsstemfrom
tests(referto§3.1and§3.2)asseparateexperiments.Each underestimatingallPLTs,withameanPLTof2637mscom-
experimentconsistedof30randomizedtrials,witheachtrial paredto2918msinrealnetworks.Meanwhile,CellReplay
including two record sessions (CellReplay and Mahimahi) accuratelycapturesthenetworkRTTandprovidesabetter
alongsidepacketRTTandpackettraintests.Thesessions(as representationofrealavailablebandwidthforthesetransfers,
wellastests)lastedfor10s.Alltestswereperformedunder althoughsomeerrorstillpersists.
“good”networkconditions,i.e.,UEswereheldstationarynear Below,weexaminetwodimensionstohighlightCellRe-
awindow. play’sedgeoverMahimahi.
First, CellReplay accurately records RTT changes over Across different operators. CellReplay maintains low
time,withtheCDFofpacketRTTscloselyoverlappingwith meanerrorsforbothoperators:6.4%onT-Mobileand7.1%
thelivenetwork(Figure10).Asexpected,Mahimahipersis- onVerizon.Mahimahihasameanerrorof13.2%onT-Mobile
tently underestimates RTT (e.g.,median RTT is underesti- andanevenhigher21%onVerizon.Mahimahi’spoorperfor-
matedby16.88%onT-Mobileand13.25%onVerizon)and manceonVerizonisexpected:Verizontendstoassignsmall
producesanRTTdistributionthatdeviatesfromthelivenet- bandwidthforsmallfiletransfers(see§5.6),andpageloads
work.Second,CellReplaycapturesthenon-linearityintrain primarilyinvolvefetchingsmallobjects.
completiontimesastrainsizeincreasesmoreaccuratelythan Acrossdifferentprotocols.CellReplayperformswellon
Mahimahi,thankstoitslightandheavyPDOsapproach.The bothHTTP/1.1andHTTP/2,withmeanerrorsof5.8%and
packettrainexperimentdemonstratesCellReplay’sinterpola- 7.7%,respectivelyIn contrast,Mahimahi shows poorerac-
tionerrorwhenusingapre-definedtrainsize(e.g.,75packets curacy, with a mean error of 12.6% on HTTP/1.1 and an
forT-Mobile)forworkloadsrangingfrom1to200packets. even higher 21.6% on HTTP/2. The multiplexing behav-
1178 22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

T-Mobile Verizon T-Mobile HTTP/1.1 T-Mobile HTTP/2 T-Mobile Verizon
|         |             |                |                   | 45           |            | 45  |     | )sm( emit daolnwoD 80 |                   | 100  |                 |     |
| ------- | ----------- | -------------- | ----------------- | ------------ | ---------- | --- | --- | --------------------- | ----------------- | ---- | --------------- | --- |
| 1.0     |             | 1.0            |                   |              |            |     |     |                       | Live              | 90   | Live            |     |
| 0.8     |             | 0.8            |                   | 40           | CellReplay | 40  |     | 70                    | CellReplay        | 80   | CellReplay      |     |
|         |             |                |                   | 35           | Mahimahi   | 35  |     |                       | Mahimahi          | 70   | Mahimahi        |     |
| FDC 0.6 |             | 0.6            |                   | )%( rorrE 30 |            | 30  |     | 60                    |                   | 60   |                 |     |
| 0.4     |             | 0.4            |                   | 25           |            | 25  |     |                       |                   | 50   |                 |     |
|         |             | Live           |                   | 20           |            | 20  |     | 50                    |                   |      |                 |     |
| 0.2     |             | CellReplay 0.2 |                   | 15           |            | 15  |     |                       |                   | 40   |                 |     |
|         |             | Mahimahi       |                   | 10           |            | 10  |     | 40                    | 0 50 100150200250 | 30 0 | 50 100150200250 |     |
| 0.0     |             | 0.0            |                   |              |            |     |     |                       | File size (KB)    |      | File size (KB)  |     |
|         | 30 40 50 60 | 70 80 90 30    | 40 50 60 70 80 90 |              | 5          | 5   |     |                       |                   |      |                 |     |
Packet RTT (ms) Packet RTT (ms) 0 0 Figure12:Meansmallfiledownloadtimes
|                               | T-Mobile      |     | Verizon |              | L1L2L3L4L5I1I2I3I4I5 | L1L2L3L4L5I1I2I3I4I5 |     |                    |         |     |         |     |
| ----------------------------- | ------------- | --- | ------- | ------------ | -------------------- | -------------------- | --- | ------------------ | ------- | --- | ------- | --- |
| )sm( emit noitelpmoc niarT 90 |               | 90  |         |              |                      |                      |     |                    |         |     |         |     |
|                               | L i v e       |     |         |              | Verizon HTTP/1.1     | Verizon HTTP/2       |     | alongwithits95%CI. |         |     |         |     |
| 80                            | C e l lReplay | 80  |         | 45           |                      | 45                   |     |                    |         |     |         |     |
|                               |               |     |         | 40           |                      | 40                   |     |                    |         |     |         |     |
| 70                            | Mahimahi      | 70  |         | 35           |                      | 35                   |     |                    | Walking |     | Driving |     |
| 60                            |               | 60  |         | )%( rorrE 30 |                      | 30                   |     | 25                 |         | 25  |         |     |
CellReplay
| 50  |            | 50      |                  | 25  |     | 25  |     | 20           |     | 20  |     | Mahimahi |
| --- | ---------- | ------- | ---------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | -------- |
| 40  |            | 40      |                  | 20  |     | 20  |     | )%( rorrE 15 |     | 15  |     |          |
|     |            |         |                  | 15  |     | 15  |     |              |     |     |     |          |
|     | 0 50 100   | 150 200 | 0 50 100 150 200 | 10  |     | 10  |     | 10           |     | 10  |     |          |
|     | Train size |         | Train size       |     | 5   | 5   |     | 5            |     | 5   |     |          |
|     |            |         |                  |     | 0   | 0   |     |              |     |     |     |          |
Figure 10: The CDF ofRTTs (above) and L1L2L3L4L5I1I2I3I4I5 L1L2L3L4L5I1I2I3I4I5 0 0
|     |     |     |     |     |     |     |     |     | L1 L3 L5 | 1KB | L1 L3 | L5 1KB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | ------ |
meanTCTs(below)fromthepacketRTTand Figure11:Emulationdistributionerroracross
Figure13:Emulationdistributionerrorof
packet train tests,respectively,run on both differentweb-pageloadtestswithHTTP/1.1and threewebPLTsand1KBfiledownloadtime
| livenetworkandemulations. |     |     |     | HTTP/2. |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
undermobility.
ior of HTTP/2 may lead to a more complex traffic pattern tionerrorof9.14%for1MBdownloadsand6.54%for10MB
comparedto HTTP/1.1,leading to more frequentmedium- downloadsacrossbothproviders.Incomparison,Mahimahi
sizedflows.Asaresult,CellReplayoftenusesaninterpolated producessignificantlyhighererrorsof23.35%and17.06%,
PDO,increasingtheerror.ForMahimahi,theissueiseven respectively,forthesamefilesizes.Surprisingly,Mahimahi’s
morepronounced,asitalwaysappliestheheavyrate,signifi- errorincreasesfurtherfor10MBfiles,despiteexpectations
cantlyunderestimatingflowcompletiontimes.Consequently, thatlargefiletransferswouldbedominatedbyheavyPDOs
bothmethodsexperiencehighererrorsforHTTP/2thanfor (i.e.,theSaturatorrate).WesuspectthatMahimahi’sinaccu-
| HTTP/1.1. |     |     |     |     |     | racystemsfromacombinationofbaseRTTunderestimation |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
andavailablebandwidthoverestimation.Referto§E.3forthe
5.6 Randomfiledownloadstest
fullresults,includingmeanfiledownloadtimesfor1MBand
10MBfilesandtheirrespectivedistributionemulationerrors.
TofurtherevaluateCellReplay’saccuracy,weconductedran-
domizedfiledownloadtestswithsmall-sizedfiles(1KBto
5.7 Interpolationeffectiveness
250KB)andmedium-sizedfiles(1MBand10MB)onboth
T-MobileandVerizon.Unliketheweb-pageloads,download WeevaluatedtheimpactofCellReplay’sPDOinterpolation
testsarenotaffectedbynon-network-relatedcomputations onemulationaccuracybycomparingittotwovariants:Cell-
(e.g.,JavaScriptparsing).Additionally,unlikethepackettrain Replay with only light PDOs (CellReplay-light) and Cell-
test,whichsends fixedtrain sizes overtime,the download ReplaywithonlyheavyPDOs(CellReplay-heavy)forweb
testisfullyrandom:theclientselectseachfilerandomlyfrom pageloadingandfiledownloads.CellReplay-heavyresem-
a predefined list. This live experiment consisted of 20 ran- blesMahimahibutincorporatesvariablebasedelayanddelay
domized trials, each including: two test workloads (small compensationbasedonpacketsize.CellReplay-lightdoesnot
| and | medium | file downloads) | and two | recording | sessions |     |     |     |     |     |     |     |
| --- | ------ | --------------- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
transitiontoheavyPDOswhenthelightPDOsend;instead,
(MahimahiandCellReplay).Eachtestandrecordingsession itrestartsfromthebeginning.WeusedT-MobileandVerizon
ranfor60s,resultinginatotalexperimentdurationof80min traces,as in §5.5 and §5.6,and reported the average error
pernetworkoperator.Alltestswereconductedunder“good” acrossbothoperators.
networkconditions. Figure 14 presents the results. For web browsing,
Small-sizedfiles.Figure12showsthefiledownloadtimes CellReplay-lightperforms similarly to CellReplay within-
forsizesbetween1KBand250KB.Consistentwiththeob- terpolation(i.e,ourCellReplay)andbeatsCellReplay-heavy,
servationin§5.4,downloadtimesdonotconformtoastraight
|     |     |     |     |     |     | as web browsing | is  | a mostly | light | workload. | Forthe | 1KB |
| --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ----- | --------- | ------ | --- |
line.Mahimahisignificantlyunderestimates(mean)download download, all three versions perform similarly since RTT
times,witherrorsrangingfrom8.4%to20.7%onT-Mobile dominatesperformanceandbandwidthislesscritical.Asthe
and7.9%to49%onVerizon.CellReplaymanagestocapture workloadincreasesto10KB,100KB,and1MB,bandwidth
andemulatethenon-uniformbandwidthavailabilitywithits becomes a more significant component of download time,
lightandheavyPDOs,resultinginsignificantlylowermean butCellReplay-heavy’semulationofbandwidthisinaccurate
download time errors: 0.5%-3.5% on T-Mobile and 0.2%- inthisregime,leadingittohavehighererrors.However,at
22.4%onVerizon.CellReplay’serrorincreaseswithlarger 10MB,CellReplay-heavy’serrordecreasesastheworkload
filesizes(e.g.,250KBonVerizon)asitmustinterpolateonce startstoresembletheSaturator.Meanwhile,CellReplay-light
packetsequencelengthsexceedacertainthreshold. excelsforsmallerdownloads(10KBand100KB)butstrug-
Medium-sizedfiles.CellReplayachievesameandistribu- gleswithlargerfiles(1MBand10MB).Thissuggeststhat
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation    1179

|     | 40        |                  |     |                                 |     |     |     |                     | (a) Chunk bitrate selection |      |     |      | (b) Est. bandwidth used by RB |     |     |
| --- | --------- | ---------------- | --- | ------------------------------- | --- | --- | --- | ------------------- | --------------------------- | ---- | --- | ---- | ----------------------------- | --- | --- |
|     |           | Mahimahi         |     | CellReplay-light                |     |     |     | )spbM( etartib naeM | 20                          |      |     | 1.00 |                               |     |     |
|     | 35        |                  |     |                                 |     |     |     |                     | BB                          | BOLA | RB  |      |                               |     |     |
|     | 30        | CellReplay-heavy |     | CellReplay (with interpolation) |     |     |     |                     |                             |      |     |      |                               |     |     |
|     | )%( rorrE |                  |     |                                 |     |     |     |                     | 15                          |      |     | 0.75 |                               |     |     |
25
|     | 20  |     |     |     |     |     |     |     |     |     |     | FDC 0.50 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
10
|     | 15  |     |     |     |     |     |     |     |     |     |     |      |     |     | Live       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---------- |
|     | 10  |     |     |     |     |     |     |     | 5   |     |     | 0.25 |     |     | CellReplay |
|     | 5   |     |     |     |     |     |     |     |     |     |     |      |     |     | Mahimahi   |
|     | 0   |     |     |     |     |     |     |     | 0   |     |     | 0.00 |     |     |            |
HTTP1 HTTP2 1KB 10KB 100KB 1MB 10MB Live CellReplay Mahimahi 0 20 40 60 80
Measured est. bandiwdth (Mbps)
Figure 14:
EmulationdistributionerrorofCellReplaywithand
Figure15:(a)MeanABRbitrateselectionresult.Mahimahishows
withoutlightandheavyPDOsinterpolation.
positivebiastoBOLA.(b)ReportedestimatedbandwidthfromRB.
neitherlightnorheavyPDOsalonecanaccuratelyemulate
improvementstemsfromCellReplay’sabilitytocapturemore
thecharacteristicsofthewirelesschannel.
performancevariabilitythanMahimahi,asindicatedbythe
Notably,thevariablebasedelayanddelaycompensation
shapeoftheCDFcurve,whichisclosertothelivenetwork’s
| in  | CellReplay-heavy |     | reduce | error | to 11.67%,compared |     | to  |       |          |     |           |       |         |     |         |
| --- | ---------------- | --- | ------ | ----- | ------------------ | --- | --- | ----- | -------- | --- | --------- | ----- | ------- | --- | ------- |
|     |                  |     |        |       |                    |     |     | curve | compared | to  | Mahimahi. | Refer | to §E.2 | for | the CDF |
Mahimahi’s18.77%.Theerrorisfurtherreducedbyincorpo-
curvefor1KBdownloadandL3pageloadtimes.
ratingPDOinterpolation,asinourfullCellReplaysystem,
|     |     |     |     |     |     |     |     |     | Additionally,we |     | tested | CellReplay | in a | basement | and a |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ---------- | ---- | -------- | ----- |
bringingtheerrordownto5.68%.Theseresultsconfirmthat
crowdedlibrary.Inbothconditions,CellReplayproducedsig-
interpolatingbetweenlightandheavyPDOssignificantlyim-
nificantlylowererrorcomparedtoMahimahi,withanemula-
provesemulationaccuracy.
tiondistributionerrorof5.74%(vs.15.22%)inthebasement
5.8 Mobilityandothernetworkconditions and8.47%(vs.22.51%)inthecrowdedlibrary.RefertoE.1
formoredetails.
WealsoevaluatedCellReplay’saccuracyunderlowandmod-
erate mobility. Forlow mobility,a userwalkedthroughan 5.9 Usecase:evaluatingABRalgorithms
officecorridorinaloopwhilecarryingtheUE(connectedto
|     |     |     |     |     |     |     |     | Finally,we | demonstrate |     | a   | common | application | for | record- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | ------ | ----------- | --- | ------- |
Verizon).Formoderatemobility,theuserdrovearoundauni-
|     |     |     |     |     |     |     |     | and-replay | emulation: |     | evaluating |     | ABR algorithms |     | for 4K |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------- | --- | -------------- | --- | ------ |
versitycampusinaloopwiththeUE(connectedtoT-Mobile).
videostreaming.ABRalgorithmsarereactive,meaningtheir
Wefollowedafixedpathwhilewalkingordrivinginaloop
bitrateselectionforvideochunkdownloadscanbeinfluenced
toensureconsistentcomparisonsacrosstrials.Onaverage,a
directly(rate-based)orindirectly(buffer-based)byobserved
looptook75swhilewalkingand220swhiledriving.
|     |           |     |        |             |           |     |          | networkperformance. |     |     | Thus,accuratelyemulating |     |     |     | network |
| --- | --------- | --- | ------ | ----------- | --------- | --- | -------- | ------------------- | --- | --- | ------------------------ | --- | --- | --- | ------- |
|     | To reduce | the | number | of tests,we | performed |     | web page |                     |     |     |                          |     |     |     |         |
conditionsiscrucialtoavoidbiasinalgorithmevaluation.
load tests using only three HTTP/1.1 landing pages – L1, WecomparedthreeABRalgorithms6from[4]runningon
L3,andL5,whichrepresentsmall,medium,andlargeweb
Verizon5Gunder“good”networkconditionsusingCellRe-
pages(§5.2),respectively.Wealsotestedrepeated1KBfile
playandMahimahiemulation:(1)Buffer-based(BB)and(2)
| downloads. |     | To minimize |     | variance,we | limited | each | trial to |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | ----------- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
BOLA,whichmakebitratedecisionsbasedonbufferoccu-
twolivetestsandtworecordings.Weconductedtwoseparate
pancy,and(3)Rate-based(RB),whichestimatesthroughput
experiments:thefirst,with1KBfiledownloadandL3,andthe
|     |     |     |     |     |     |     |     | from | past chunk | download |     | times | to select | the next | bitrate. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | -------- | --- | ----- | --------- | -------- | -------- |
second,withL1andL5.Weconducted10trialsforwalking
|     |     |     |     |     |     |     |     | Given | the highdownload |     | bandwidthreported |     |     | by  | Saturator |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | ----------------- | --- | --- | --- | --------- |
experimentsand5trialsfordrivingexperiments.Calibration
(270Mbps),allthreealgorithmseventuallyselectthehighest
| was | performedonly |     | once | atthe starting |     | point. | In total,we |                                               |     |     |     |     |     |     |      |
| --- | ------------- | --- | ---- | -------------- | --- | ------ | ----------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|     |               |     |      |                |     |        |             | bitrate(17Mbps)anddonotexperiencerebuffering. |     |     |     |     |     |     | How- |
spent1.67hwalkingand2.45hdrivingaroundtheloop.
ever,theirstartupphase[17]behaviordiffers,sowefocused
Figure13showstheemulationdistributionerrorforCell-
onbitrateselectionforthefirst10chunksasourQoEmetric.
| Replay | and | Mahimahi. | Network |     | conditions | are | more vari- |     |     |     |     |     |     |     |     |
| ------ | --- | --------- | ------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Weconducted10randomizedtrials,eachwiththreetestwork-
ableunderdriving,whichmayalsointroducepacketdrop,
loads(streamingvideousingthreeABRs)andtworecording
| afactorthatCellReplaydoesnotcapture4. |     |     |     |     |     | Weindeedcon- |     |     |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sessions(MahimahiandCellReplay).Eachtestandrecording
firmedthatdrivingtriggeredatleasttwohandovers5,anda
sessionlastedfor30s.
fewpacketsweredroppedduringcertainperiodsofrecord-
Figure15apresentsthemeanbitrateresults.Asexpected,
| ing. | Consequently,CellReplay’s |      |          | accuracy |         | suffers | more un-     |          |         |     |          |         |              |     |            |
| ---- | ------------------------- | ---- | -------- | -------- | ------- | ------- | ------------ | -------- | ------- | --- | -------- | ------- | ------------ | --- | ---------- |
|      |                           |      |          |          |         |         |              | Mahimahi | reports |     | a higher | bitrate | than Live-5G |     | across all |
| der  | driving                   | than | walking. | However, | despite |         | this limita- |          |         |     |          |         |              |     |            |
threeABRs,withanaverageoverestimationof17.73%,com-
| tions, | CellReplay |     | still provides | a   | noticeable | improvement |     |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | -------------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
paredto5.89%onCellReplay.Thisalignswithourfindings
(1.8times)overMahimahiinbothmobilityscenarios.This
thatMahimahitendstooverestimatenetworkperformance,
4ThisreferstothedropinIPpackets.CellReplaycanstillcapturethe leading to inflated application performance. But,more im-
effectsofthehandoverprocessthroughtheincreaseinthebaselatencyand portantly,thisalsoaffectsprotocolevaluation.Mahimahi’s
PDOblackoutandemulateitaccordingly.
5Therewereabriefperiod(<1second)whenthetwodeviceswere 6ThissetupalsoincludesMPC[44]andPensieve[20],butthesewerenot
connectedtodifferentbasestationsduetothehandoverswerenotdoneat tested,asMPCrequiresmodifyingthehardcodedMPCtable,andPensieve
| thesametime. |     |     |     |     |     |     |     | requiresretraining. |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
1180    22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

resultssuggestthatRBandBOLAarethebestprotocols,with In the future, we will be able to use a single phone with
BOLAsignificantlyoutperformingBBby30.43%.However, Dual-SIMDual-Active(DSDA)modem[1]forrecording,as
inrealityinthisenvironment,BOLAperformssignificantly DSDAallowssimultaneoustraffictransmissionacrosstwo
worsethanRBandissimilartoBB.CellReplay’sresultsare SIMs.Eachoftheseareasrepresentsanopportunityforfuture
muchmorealignedwiththelivenetwork.Thisdiscrepancyis improvement.Wenote,however,thatourevaluationresults
largelyduetoMahimahi’soverestimationofavailableband- accountfortheerrorscausedbytheseinaccuracies.
width,particularlyforsmallerinitialchunks,causingABRs Improving CellReplay interpolation accuracy. A
toquicklyconvergetothehighestbitrate.InFigure15b,we straightforwardapproachistogatheradditionaldatapoints
presentthemeasuredbandwidthestimationfromRB,which forinterpolation.However,sinceweneedtorecorddatasi-
shows that Mahimahi overestimates bandwidth by 44.38% multaneously(e.g.,whilewalkingordriving),wearelimited
in the median, compared to 7.96% on CellReplay. Unlike to running only a few workloads with a few phones. An-
Mahimahi,CellReplaydoesnotsufferfromthisbiasandpro- otherviableapproachistoleverageMLtomodelcomplex,
videsmoreaccuraterelativeperformanceofABRsduetoits workload-dependentnetworkperformanceandproviders’re-
duallightandheavyrateapproach. sourceallocationpolicies.WecantrainanMLmodelbased
onrecordedworkloadandperformancetracestopredictnet-
6 Discussionandfuturework
work performance (e.g., PDOs) for a given test workload.
However,thisapproachmayrequireextensivedatacollection
WediscussCellReplay’susecases,limitations,andplansfor
tocaptureRANschedulingbehavior,increasingtherecording
futureimprovements.
effortandmakingittime-consuming.
Usecases.Asshownin§5.9,CellReplaycanbeusedto
Adding more cellular network specific features. Cell-
evaluatenewapplicationsandprotocolsoncellularnetworks
Replay couldbe improvedby explicitly emulating cellular
andprovidemoreaccurateemulationofrealnetworkperfor-
network-specificfeatures,especiallythosethataffectapplica-
mancecomparedtothestate-of-the-artapproach.CellReplay
tionperformance.Theseincluderadioresourcecontrol(RRC)
issuperiorforlatency-sensitiveapplications,asitcanemu-
delays,handover,andotherrelevantfactors.
latebasedelayvariability,andapplicationswithvariableflow
sizes,asitcanemulatethebandwidth-workloaddependency. Otherlimitations.CellReplayprobesUDPtraffictorecord
Adaptiveapplications(e.g.,ABR)thatreacttonetworkmea- networktraces,meaningitcannotcapturetheeffectsofnet-
surementwillalsoreceivemoreaccurateperformanceresults workdiscriminationbasedonIPprotocoltypes,suchasfrom
withCellReplay. TCPmiddleboxintervention[8].
Wealsoprovidetracesthatresearchersanddeveloperscan
7 Conclusion
usefortestingonCellReplay. Whilerecordingtraceswith
CellReplay requires a bit more effort than Mahimahi due Thispaperexposesthedifficultyofaccuraterecord-and-replay
to the use of two phones, this is a minor issue, as once a emulationandpresentsCellReplay,whichmorefaithfullycap-
diversesetoftracesisrecorded,userscaneasilyreplaythem turesreal-worldcellularnetworkperformancecharacteristics.
withoutthephones(justasinMahimahi).SinceCellReplay’s CellReplay’sapproachofdual-workloadrecordingandinter-
implementation is based on Mahimahi’s shell,unmodified polatedreplayprovidesthecommunitywithamoreaccurate
applicationscaneasilyuseCellReplayemulatedinterface. platformforevaluatingresearchincellularenvironments.We
InaccuraciesinCellReplay.Whilewehavemadesignif- alsohopethisworkinspiresthecommunitytoexplorefuture
icant progress in faithfully replaying cellularperformance, designsthatcanmakerecord-and-replayemulationevenmore
CellReplayinvolvesseveralsimplificationsandassumptions: faithfultolivedeployments.
(1) CellReplay does not record and replay random packet
Acknowledgements:Wesincerelythankourshepherd,Kyle
losses(althoughitdropspacketswhenthequeueoverflows
Jamieson,and the anonymous reviewers for their valuable
andcanbemanuallyconfiguredforasetrandomdroprate).
suggestions. We also thank Keith Winstein forhelpful dis-
Wenotice,however,thatcellularlinksunderstationarycondi-
cussionsonMahimahiandCellSim.Additionally,wethank
tionsarerobusttorandompacketdrops(e.g.,duetopacket
QinjunJiang,SamYuan,andPradnyanKhodke,whohelped
corruption)duetolink-layerretransmission[22].However,
drivethecarwhiletheauthorconductedexperiments.This
packetdropsaremorefrequentduringhandoversinmobil-
projectwassupportedbygiftsfromT-MobileandCisco,and
ity [15]. (2) CellReplay uses fixed calibration parameters
agrantfromtheIBM-IllinoisDiscoveryAcceleratorInstitute.
beforeeachrecordingsession.Amoreadaptiveselectionof
parameterscouldhelpwhennetworkconditionschangedur-
ing recording. (3) CellReplay’s two-phone setuphas some References
weaknesses.Undermobility,bothphonesmayconnecttodif-
ferentbasestationsandreportdifferentperformances.More- [1] Two birds, one stone: Unleashing the full potential
over,althoughwedidnotobservemajorinterference,greater for simultaneous 5g cellular connections, thanks
interferencemayoccurwithotherprovidersandconditions. to our new qualcomm dsda gen 2 with dual data.
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation 1181

https://www.qualcomm.com/news/onq/2023/05/ [12] RostandAKFezeu,EmanRamadan,WeiYe,Benjamin
unleashing-full-potential-for-simultaneous- Minneci,JackXie,ArvindNarayanan,AhmadHassan,
5g-cellular-connections-qualcomm-dsda-gen-
FengQian,Zhi-LiZhang,JaideepChandrashekar,etal.
2-with-dual-data,2023. [LastaccessedonFeb17, Anin-depthmeasurementanalysisof5gmmwavephy
| 2025]. |     |     |     |     |     | latency  | and        | its impact | on  | end-to-end |     | delay. In      | Inter- |
| ------ | --- | --- | --- | --- | --- | -------- | ---------- | ---------- | --- | ---------- | --- | -------------- | ------ |
|        |     |     |     |     |     | national | Conference |            | on  | Passive    | and | Active Network |        |
https://mitmproxy.org,
[2] mitmproxy. 2024. [Last Measurement,pages284–312.Springer,2023.
accessedonMay8,2024].
|             |          |            |     |          |     | [13] Moinak | Ghoshal, |     | Imran | Khan, | Z Jonny | Kong, | Phuc |
| ----------- | -------- | ---------- | --- | -------- | --- | ----------- | -------- | --- | ----- | ----- | ------- | ----- | ---- |
| [3] Network | features | reference. |     | https:// |     |             |          |     |       |       |         |       |      |
Dinh,JiayiMeng,YCharlieHu,andDimitriosKout-
developer.chrome.com/docs/devtools/network/
|                               |     |     |       |     |       | sonikolas. |                                     | Performance |     | of cellular |     | networks | on the |
| ----------------------------- | --- | --- | ----- | --- | ----- | ---------- | ----------------------------------- | ----------- | --- | ----------- | --- | -------- | ------ |
| reference#throttling-profile, |     |     | 2024. |     | [Last |            |                                     |             |     |             |     |          |        |
|                               |     |     |       |     |       | wheels.    | InProceedingsofthe2023ACMonInternet |             |     |             |     |          |        |
accessedonMay8,2024].
MeasurementConference,pages678–695,2023.
| [4] Pensieve.  |     | https://github.com/hongzimao/ |     |     |     |                                                     |     |     |     |     |     |             |     |
| -------------- | --- | ----------------------------- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
|                |     |                               |     |     |     | [14] PrateeshGoyal,AnupAgarwal,RaviNetravali,Moham- |     |     |     |     |     |             |     |
| pensieve,2024. |     | [LastaccessedonSept17,2024].  |     |     |     |                                                     |     |     |     |     |     |             |     |
|                |     |                               |     |     |     | madAlizadeh,andHariBalakrishnan.                    |     |     |     |     |     | {ABC}:Asim- |     |
pleexplicitcongestioncontrollerforwirelessnetworks.
[5] SoheilAbbasloo,Chen-YuYen,andHJonathanChao.
In17thUSENIXSymposiumonNetworkedSystemsDe-
| Wanna                        | make | your tcp scheme | great for        | cellular | net- |      |                    |     |     |       |      |                |     |
| ---------------------------- | ---- | --------------- | ---------------- | -------- | ---- | ---- | ------------------ | --- | --- | ----- | ---- | -------------- | --- |
|                              |      |                 |                  |          |      | sign | and Implementation |     |     | (NSDI | 20), | pages 353–372, |     |
| works?letmachinesdoitforyou! |      |                 | IEEEJournalonSe- |          |      |      |                    |     |     |       |      |                |     |
2020.
lectedAreasinCommunications,39(1):265–279,2020.
[6] WaqarAqeel,BalakrishnanChandrasekaran,AnjaFeld- [15] AhmadHassan,ArvindNarayanan,AnlanZhang,Wei
Ye,RuiyangZhu,ShuoweiJin,JasonCarpenter,ZMor-
| mann,andBruce |     | M Maggs. | On landing | andinternal |     |                                 |     |     |     |     |     |                |     |
| ------------- | --- | -------- | ---------- | ----------- | --- | ------------------------------- | --- | --- | --- | --- | --- | -------------- | --- |
|               |     |          |            |             |     | leyMao,FengQian,andZhi-LiZhang. |     |     |     |     |     | Vivisectingmo- |     |
webpages:Thestrangecaseofjekyllandhydeinweb
performancemeasurement. InProceedingsoftheACM bilitymanagementin5gcellularnetworks. InProceed-
|     |     |     |     |     |     | ings | ofthe | ACM | SIGCOMM | 2022 | Conference,pages |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ------- | ---- | ---------------- | --- | --- |
InternetMeasurementConference(IMC),2020.
86–100,2022.
[7] SachinAshok,ShubhamTiwari,NagarajanNatarajan,
VenkataNPadmanabhan,andSundararajanSellaman- [16] Stephen Hemminger et al. Network emulation with
|        |                                           |     |     |     |     | netem. | InLinuxconfau,volume5,page2005,2005. |     |     |     |     |     |     |
| ------ | ----------------------------------------- | --- | --- | --- | --- | ------ | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| ickam. | Data-drivennetworkpathsimulationwithibox. |     |     |     |     |        |                                      |     |     |     |     |     |     |
ProceedingsoftheACMonMeasurementandAnalysis
|     |     |     |     |     |     | [17] Te-Yuan |     | Huang, | Ramesh | Johari, | Nick | McKeown, |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------ | ------- | ---- | -------- | --- |
ofComputingSystems,6(1):1–26,2022.
MatthewTrunnell,andMarkWatson.Abuffer-basedap-
proachtorateadaptation:Evidencefromalargevideo
[8] ArjunBalasingam,ManuBansal,RakeshMisra,Kanthi
Nagaraj,RahulTandra,SachinKatti,andAaronSchul- streaming service. In Proceedings of the 2014 ACM
conferenceonSIGCOMM,pages187–198,2014.
| man. Detectingiflteisthebottleneckwithbursttracker. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
InThe25thAnnualInternationalConferenceonMobile
|     |     |     |     |     |     | [18] NikhilKansal,MuraliRamanujam,andRaviNetravali. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ComputingandNetworking,pages1–15,2019.
|     |     |     |     |     |     | Alohamora: |     | Reviving | HTTP/2 |     | push | and preload | by  |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------ | --- | ---- | ----------- | --- |
[9] Francesco Capozzi, Giuseppe Piro, Luigi Alfredo adapting policies on the fly. In 18thUSENIX Sympo-
Grieco,GennaroBoggia,andPietroCamarda.Downlink siumonNetworkedSystemsDesignandImplementation
packetschedulinginltecellularnetworks:Keydesign (NSDI21),pages269–287.USENIXAssociation,April
2021.
| issuesandasurvey. |     | IEEEcommunicationssurveys& |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tutorials,15(2):678–700,2012.
|     |     |     |     |     |     | [19] Gerui | Lv, | Qinghua | Wu, | Yanmei | Liu, | Zhenyu | Li, |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | ------ | ---- | ------ | --- |
[10] StanleyCFChan,KMChan,KeLiu,andJackYBLee. QingyueTan,FurongYang,WentaoChen,YunfeiMa,
|     |     |     |     |     |     | Hongyu | Guo, | Ying | Chen, | et al. | Chorus: | Coordinat- |     |
| --- | --- | --- | --- | --- | --- | ------ | ---- | ---- | ----- | ------ | ------- | ---------- | --- |
Onqueuelengthandlinkbuffersizeestimationin3g/4g
mobiledatanetworks. IEEETransactionson Mobile ing mobile multipath scheduling and adaptive video
Computing,13(6):1298–1311,2013. streaming. InProceedingsofthe30thAnnualInterna-
tionalConferenceonMobileComputingandNetwork-
| [11] Mark Claypool, |     | Robert Kinicki, | Mingzhe | Li, | James |     |     |     |     |     |     |     |     |
| ------------------- | --- | --------------- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ing,pages246–262,2024.
Nichols,andHuahuiWu.Inferringqueuesizesinaccess
networks by active measurement. In Passive andAc- [20] HongziMao,RaviNetravali,andMohammadAlizadeh.
tiveNetworkMeasurement:5thInternationalWorkshop, Neuraladaptivevideostreamingwithpensieve. InPro-
PAM2004,AntibesJuan-les-Pins,France,April19-20, ceedingsoftheconferenceoftheACMspecialinterest
2004.Proceedings5,pages227–236.Springer,2004. groupondatacommunication,pages197–210,2017.
1182    22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

[21] AbhishekKumarMishra,SaraAyoubi,GiulioGrassi, [31] DevdeepRay,JackKosaian,KVRashmi,andSrinivasan
andRenataTeixeira. Nemfi:Record-and-replaytoemu- Seshan. Vantage: optimizing video upload for time-
latewifi. ACMSIGCOMMComputerCommunication shiftedviewingofsociallivestreams. InProceedings
Review,51(3):2–8,2021. oftheACMSpecialInterestGrouponDataCommuni-
cation,pages380–393.2019.
| [22] Arvind | Narayanan,Eman |     |     | Ramadan,Jason |     | Carpenter, |     |     |     |     |     |     |     |
| ----------- | -------------- | --- | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[32] LuigiRizzo.Dummynet:asimpleapproachtotheevalu-
| QingxuLiu,YuLiu,FengQian,andZhi-LiZhang. |     |     |     |     |     | A   |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
firstlookatcommercial5gperformanceonsmartphones. ationofnetworkprotocols. ACMSIGCOMMComputer
InProceedingsofTheWebConference2020,pages894– CommunicationReview,27(1):31–41,1997.
905,2020.
|     |     |     |     |     |     |     | [33] Yossi | Rubner, | Carlo | Tomasi, | and Leonidas |     | J Guibas. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | ------- | ------------ | --- | --------- |
[23] Arvind Narayanan, Eman Ramadan, Rishabh Mehta, A metric for distributions with applications to image
|     |     |     |     |     |     |     | databases. |     | In Sixth | international | conference |     | on com- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------------- | ---------- | --- | ------- |
XinyueHu,QingxuLiu,RostandAKFezeu,UdhayaKu-
putervision(IEEECat.No.98CH36271),pages59–66.
| marDayalan,SaurabhVerma,PeiqiJi,TaoLi,etal. |             |     |             |        |     | Lu-      |              |          |     |              |     |                 |     |
| ------------------------------------------- | ----------- | --- | ----------- | ------ | --- | -------- | ------------ | -------- | --- | ------------ | --- | --------------- | --- |
| mos5g:Mappingandpredictingcommercialmmwave  |             |     |             |        |     |          | IEEE,1998.   |          |     |              |     |                 |     |
| 5g                                          | throughput. | In  | Proceedings | of the | ACM | Internet |              |          |     |              |     |                 |     |
|                                             |             |     |             |        |     |          | [34] William | Sentosa, |     | Balakrishnan |     | Chandrasekaran, |     |
MeasurementConference,pages176–193,2020.
|           |            |        |         |       |          |     | P. Brighten |           | Godfrey, | Haitham      | Hassanieh, | and          | Bruce |
| --------- | ---------- | ------ | ------- | ----- | -------- | --- | ----------- | --------- | -------- | ------------ | ---------- | ------------ | ----- |
|           |            |        |         |       |          |     | Maggs.      | DChannel: |          | Accelerating | mobile     | applications |       |
| [24] Ravi | Netravali, | Vikram | Nathan, | James | Mickens, | and |             |           |          |              |            |              |       |
withparallelhigh-bandwidthandlow-latencychannels.
| Hari | Balakrishnan. |     | Vesper: | Measuring |     | Time-to- |     |     |     |     |     |     |     |
| ---- | ------------- | --- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Interactivity forweb pages. In 15th USENIX Sympo- In 20th USENIX Symposium on Networked Systems
DesignandImplementation(NSDI23),pages419–436,
siumonNetworkedSystemsDesignandImplementation
Boston,MA,April2023.USENIXAssociation.
| (NSDI | 18), | pages 217–231, |     | Renton, | WA, April | 2018. |     |     |     |     |     |     |     |
| ----- | ---- | -------------- | --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
USENIXAssociation. [35] BabakTaraghi,HadiAmirpour,andChristianTimmerer.
Multi-codecultrahighdefinition8kmpeg-dashdataset.
| [25] Ravi | Netravali, | Anirudh |           | Sivaraman, | Somak    | Das, |                |     |       |         |            |     |         |
| --------- | ---------- | ------- | --------- | ---------- | -------- | ---- | -------------- | --- | ----- | ------- | ---------- | --- | ------- |
|           |            |         |           |            |          |      | In Proceedings |     | ofthe | 13thACM | Multimedia |     | Systems |
| Ameesh    | Goyal,     | Keith   | Winstein, | James      | Mickens, | and  |                |     |       |         |            |     |         |
Conference,pages216–220,2022.
| HariBalakrishnan. |            |         | Mahimahi:accurate{Record-and- |               |     |          |                      |                                               |                               |             |         |     |          |
| ----------------- | ---------- | ------- | ----------------------------- | ------------- | --- | -------- | -------------------- | --------------------------------------------- | ----------------------------- | ----------- | ------- | --- | -------- |
| Replay}for{HTTP}. |            |         | In2015USENIXAnnualTech-       |               |     |          |                      |                                               |                               |             |         |     |          |
|                   |            |         |                               |               |     |          | [36] Bo Wang,Mingwei |                                               |                               | Xu,Fengyuan | Ren,and |     | Jianping |
| nical             | Conference | (USENIX |                               | ATC 15),pages |     | 417–429, |                      |                                               |                               |             |         |     |          |
|                   |            |         |                               |               |     |          | Wu.                  | Improvingrobustnessofdashagainstunpredictable |                               |             |         |     |          |
| 2015.             |            |         |                               |               |     |          | networkvariations.   |                                               | IEEETransactionsonMultimedia, |             |         |     |          |
24:323–337,2021.
[26] YunzheNi,ZhilongZheng,XianshangLin,FengyuGao,
Xuan Zeng, Yirui Liu, Tao Xu, Hua Wang, Zhidong [37] ShiboWang,ShusenYang,HailiangLi,XiaodanZhang,
Zhang,SenlangDu,etal. Cellfusion:Multipathvehicle- ChenZhou,ChenrenXu,FengQian,NanbinWang,and
| to-cloud | video | streaming | with | network | coding | in the |         |     |            |                 |     |        |      |
| -------- | ----- | --------- | ---- | ------- | ------ | ------ | ------- | --- | ---------- | --------------- | --- | ------ | ---- |
|          |       |           |      |         |        |        | Zongben | Xu. | Salientvr: | saliency-driven |     | mobile | 360- |
wild. In Proceedings of the ACM SIGCOMM 2023 degreevideostreamingwithgazeinformation. InPro-
Conference,pages668–683,2023. ceedingsofthe28thAnnualInternationalConference
onMobileComputingAndNetworking,pages542–555,
| [27] Brian | D Noble, | Mahadev |     | Satyanarayanan, |     | Giao T |     |     |     |     |     |     |     |
| ---------- | -------- | ------- | --- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
2022.
| Nguyen,andRandyHKatz. |     |     |     | Trace-basedmobilenet- |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
work emulation. In Proceedings of the ACM SIG- [38] KeithWinstein,AnirudhSivaraman,andHariBalakrish-
COMM’97 conference on Applications, technologies, nan. Stochasticforecastsachievehighthroughputand
architectures,andprotocolsforcomputercommunica- lowdelayovercellularnetworks. In10thUSENIXSym-
tion,pages51–61,1997. posiumonNetworkedSystemsDesignandImplemen-
tation(NSDI13),pages459–471,Lombard,IL,April
[28] NS-3. NS-3NetworkSimulator. https://www.nsnam. 2013.USENIXAssociation.
| org/,2023. |     | [Lastaccessed:September20,2023]. |     |     |     |     |              |     |          |           |     |           |       |
| ---------- | --- | -------------------------------- | --- | --- | --- | --- | ------------ | --- | -------- | --------- | --- | --------- | ----- |
|            |     |                                  |     |     |     |     | [39] Yaxiong | Xie | and Kyle | Jamieson. |     | Ng-scope: | Fine- |
[29] JanOdvarko. Har1.2spec,2007. grainedtelemetryfornextgcellularnetworks. Proceed-
ingsoftheACMonMeasurementandAnalysisofCom-
[30] MuraliRamanujam,HelenChen,ShaghayeghMardani,
putingSystems,6(1):1–26,2022.
| andRaviNetravali. |     |     | Floo:automatic,lightweightmem- |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oizationforfastermobileapps. InProceedingsofthe [40] Yaxiong Xie, Fan Yi, and Kyle Jamieson. Pbe-cc:
20thAnnualInternationalConferenceonMobileSys- Congestioncontrolviaendpoint-centric,physical-layer
tems,ApplicationsandServices,pages168–182,2022. bandwidthmeasurements. InProceedingsoftheAnnual
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation    1183

conferenceoftheACMSpecialInterestGrouponData time(5minutesforourcase),wecalculatedthemeanRTT
Communicationontheapplications,technologies,ar- foreachpacketsizex,denotedasµ .Thecompensationdelay
x
chitectures,andprotocolsforcomputercommunication, for a packet size s,or comp(s),is computed as follows. If
| pages451–464,2020. |           |             |        |               |            |        | s<100,comp(s)=µ                                  |     |              | −µ          | .Otherwise,comp(s)=(1−   |         |         |
| ------------------ | --------- | ----------- | ------ | ------------- | ---------- | ------ | ------------------------------------------------ | --- | ------------ | ----------- | ------------------------ | ------- | ------- |
|                    |           |             |        |               |            |        |                                                  |     |              | 100         | 1400                     |         |         |
|                    |           |             |        |               |            |        | α)µ                                              | +αµ | −µ whereiand |             | jarethetestedpacketsizes |         |         |
|                    |           |             |        |               |            |        |                                                  | i   | j 1400       |             |                          |         |         |
| [41] Francis       | Y.        | Yan, Hudson | Ayers, | Chenzhi       | Zhu,       | Sadjad |                                                  |     |              |             |                          |         |         |
|                    |           |             |        |               |            |        | immediatelylessthanandgreaterthans,respectively. |     |              |             |                          |         | The     |
| Fouladi,           | James     | Hong,       | Keyi   | Zhang, Philip | Levis,     | and    |                                                  |     |              |             |                          |         |         |
|                    |           |             |        |               |            |        | parameter                                        |     | α is set     | to linearly | interpolate              | between | the two |
| Keith              | Winstein. | Learning    |        | in situ: a    | randomized | ex-    |                                                  |     |              |             |                          |         |         |
observedmeans,i.e.,α=(s−i)/(j−i).Thecompensation
| perimentinvideostreaming. |     |     |     | In17thUSENIXSympo- |     |     |     |        |             |           |         |         |             |
| ------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | ------ | ----------- | --------- | ------- | ------- | ----------- |
|                           |     |     |     |                    |     |     | is  | always | relative to | 1400-byte | packets | because | that is the |
siumonNetworkedSystemsDesignandImplementation sizeusedtomeasurebaseRTT.Thisprocedureisrepeated
(NSDI20),pages495–511,SantaClara,CA,February
separatelyforuplinkanddownlinkmeasurements,withsender
2020.USENIXAssociation.
andreceiverrolesswapped.
[42] FrancisYYan,JestinMa,GregDHill,DeeptiRagha-
A.2 InferringF:derivation
| van,Riad |     | S Wahby,PhilipLevis,andKeithWinstein. |     |     |     |     |        |     |                  |     |            |              |        |
| -------- | --- | ------------------------------------- | --- | --- | --- | --- | ------ | --- | ---------------- | --- | ---------- | ------------ | ------ |
|          |     |                                       |     |     |     |     | Assume |     | that internally, | the | bottleneck | link remains | in its |
Pantheon:thetraininggroundforinternetcongestion-
|                  |     |     |             |                 |     |     | heavy-workload |     | state | while | it has queued | packets | to send, |
| ---------------- | --- | --- | ----------- | --------------- | --- | --- | -------------- | --- | ----- | ----- | ------------- | ------- | -------- |
| controlresearch. |     | In  | 2018 USENIX | AnnualTechnical |     |     |                |     |       |       |               |         |          |
andthenonceitremainsidleforsometimeF,itreturnstothe
Conference(USENIXATC18),pages731–743,2018.
|     |     |     |     |     |     |     | light-workloadstate.WiththegapofG |     |     |     |     | ,thisstatechangeis |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | ------------------ | --- |
min
[43] Hyunho Yeo,Youngmok Jung,Jaehong Kim,Jinwoo justbarelyreached.Thus,wehaveS+G min ≈Q+F,whereS
Shin,andDongsuHan. Neuraladaptivecontent-aware isthetimethesendertakestosendthetrain,G isthetimeit
min
internetvideodelivery. In13thUSENIXSymposiumon waitsbeforebeginningthenexttrain,andQisthetimeforthe
OperatingSystemsDesignandImplementation(OSDI linktoentirelyclearthepackettrainoutofitsqueue.Since
|                                                  |     |     |     |     |     |     | S andG |     | are bothtimedin |     | userspace,S | is  | close to zero. |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ | --- | --------------- | --- | ----------- | --- | -------------- |
| 18),pages645–661,2018.usingnetworktraceforvideo. |     |     |     |     |     |     |        | min |                 |     |             |     |                |
Furthermore,becausewehaveassumedthelinkofinterest
[44] Xiaoqi Yin,Abhishek Jindal,Vyas Sekar,and Bruno isthebottleneck,Qisobservableatthereceiverasthetime
| Sinopoli. |     | A control-theoretic |     | approach | for | dynamic |     |     |     |     |     |     |     |
| --------- | --- | ------------------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
betweenreceivingthefirstandlastpacketsofthetrain,i.e.,
| adaptivevideostreamingoverhttp. |     |     |     | InProceedingsof |     |     |      |     |                       |     |     |     |          |
| ------------------------------- | --- | --- | --- | --------------- | --- | --- | ---- | --- | --------------------- | --- | --- | --- | -------- |
|                                 |     |     |     |                 |     |     | r    | (G  | ).Thus,wecanestimateF |     | =G  | −r  | (G ).In  |
|                                 |     |     |     |                 |     |     | last | min |                       |     |     | min | last min |
the2015ACMConferenceonSpecialInterestGroupon Figure8b,theG is30ms,anditsr (g )is23.23ms.
|     |     |     |     |     |     |     |     |     | min |     | last | min |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
DataCommunication,pages325–338,2015.
|     |     |     |     |     |     |     | Thus,wecomputeF |     |     | =6.77ms(androunditto7mswhen |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------------------------- | --- | --- | --- |
settingtheparameter).
| [45] Danfu                             | Yuan, | Yuanhong |     | Zhang, Weizhan |     | Zhang, |     |             |     |     |     |     |     |
| -------------------------------------- | ----- | -------- | --- | -------------- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- |
| XunchengLiu,HaipengDu,andQinghuaZheng. |       |          |     |                |     | Prior: | A.3 | InferringB. |     |     |     |     |     |
deepreinforcedadaptivevideostreamingwithattention-
Weuseaclassicalmax-minapproach[11]toinferthebottle-
basedthroughputprediction.InProceedingsofthe32nd
neckbuffersizeusingthedifferencebetweentheminimum
WorkshoponNetworkandOperatingSystemsSupport
andmaximumRTTofpacketsunderheavyload.Specifically,
forDigitalAudioandVideo,pages36–42,2022.
weruniperfandmonitoritwithtcpdump.Thebuffersizeis
[46] BoZhang,ThiagoTeixeira,andYuriyReznik. Perfor- calculatedas(RTT max −RTT min )·C,whereCistheobserved
linkcapacity[10].
| manceoflow-latencyhttp-basedstreamingplayers. |     |     |     |     |     | In  |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proceedingsofthe12thACMMultimediaSystemsCon-
B CellReplayimplementation
ference,pages356–362,2021.
|              |             |             |                |        |             |           | CellReplay’s |      | record    | client     | is implemented       | in       | Java to ease  |
| ------------ | ----------- | ----------- | -------------- | ------ | ----------- | --------- | ------------ | ---- | --------- | ---------- | -------------------- | -------- | ------------- |
| [47] Torsten |             | Zimmermann, | Benedikt       |        | Wolters,    | Oliver    |              |      |           |            |                      |          |               |
|              |             |             |                |        |             |           | porting      | into | Android.  | Meanwhile, | the                  | record   | server is im- |
| Hohlfeld,    |             | and Klaus   | Wehrle.        | Is the | web         | ready for |              |      |           |            |                      |          |               |
|              |             |             |                |        |             |           | plemented    |      | in Python | 3. The     | client accepts       | workload | con-          |
| http/2       | serverpush? |             | In Proceedings |        | of the 14th | ACM       |              |      |           |            |                      |          |               |
|              |             |             |                |        |             |           | figurations  |      | as user   | inputs,    | which are determined |          | from the      |
ConferenceonEmergingNetworkingExperimentsand
automatedcalibrationperformedseparately.Theseconfigura-
Technologies(CoNEXT),2018.
tionsarethensenttotheCellReplayserver.Forpackettrain
|     |     |     |     |     |     |     | workloads,the |     | usermust |     | input: the numberof |     | packets per |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --- | ------------------- | --- | ----------- |
A Calibrationdetails uplinkanddownlinktrain,andthegapbetweentrains.Satu-
ratorworkloadrequiresthemaximumuploadanddownload
A.1 Inferringcomp():derivation
bandwidth,whichcanbedeterminedusingotherbandwidth
We examine the impact of packet size on RTT by sending probingtools(e.g.,speedtest.comoriperf).Bothclientand
packetswithsizessampleduniformlyatrandomfrom{100, serversend1400-byteUDPpacketsviaasocket.
200,...,1400}bytesevery50mstoareceiverthatrepliesto CellReplay’sreplayisbuiltontopoftheMahimahishell,
eachwitha100-byteACK.Afterrunningforaconfigurable extendingallofMahimahi’scorefunctionality.Thisincludes
1184    22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Table2:Alltestedconditionsthatincludesstationary,walking,anddrivingscenarios.WetestedT-Mobile(TM)andVerizon(VZ)
networksunder5Gmidband(MB)andlowband(LB).WealsoshowedtheusedCellReplayconfigurations.
|     | Name            |     | Description                  |     |     |     | Op. | Net.type | CellReplayconfig   |     |     |     |     |
| --- | --------------- | --- | ---------------------------- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | --- | --- |
|     |                 |     |                              |     |     |     | TM  | 5GMB     | U=25,D=75,G=50,F=5 |     |     |     |     |
|     | stationary-good |     | UEswereinanofficenearawindow |     |     |     |     |          |                    |     |     |     |     |
(cid:28)(cid:29)(cid:38)(cid:37)(cid:36)((cid:34)(cid:3)(cid:4)(cid:27)(cid:33)(cid:43)(cid:36)2)((cid:5)
|     |                    |     |                   |     |     |                       | VZ  | 5GLB | U=10,D=100,G=50F=7  |                       |     |     |     |
| --- | ------------------ | --- | ----------------- | --- | --- | --------------------- | --- | ---- | ------------------- | --------------------- | --- | --- | --- |
|     |                    |     | UEswereinacrowded |     |     | (cid:9)(cid:7)(cid:8) |     |      |                     | (cid:9)(cid:7)(cid:8) |     |     |     |
|     | stationary-crowded |     |                   |     |     |                       | VZ  | 5GLB | U=25,D=100,G=50,F=7 |                       |     |     |     |
libraryduringrushhours
|     |     |     |     |     |     | (cid:8)(cid:7)(cid:16) |     |     |     | (cid:8)(cid:7)(cid:16) |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
UEswereinabasement
|     | stationary-weak |                                                                                                           |                                   |     |     |                                                 | TM                                                                                                                               | 5GLB                             | U=25,D=75,G=50,F=5                                                                                                      |                        |                                                                                                                  |                                                |                                                 |
| --- | --------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------- | --- | --- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------- |
|     |                 |                                                                                                           | ofabuildingwithnowindow           |     |     | (cid:20)(cid:19)(cid:18) (cid:8)(cid:7)(cid:14) |                                                                                                                                  |                                  |                                                                                                                         | (cid:8)(cid:7)(cid:14) |                                                                                                                  |                                                |                                                 |
|     |                 |                                                                                                           | Userwaswalkingthroughanoffice     |     |     | (cid:8)(cid:7)(cid:12)                          |                                                                                                                                  |                                  | (cid:22)(cid:36).(cid:33)                                                                                               | (cid:8)(cid:7)(cid:12) |                                                                                                                  |                                                |                                                 |
|     | walking         |                                                                                                           |                                   |     |     |                                                 | VZ                                                                                                                               | 5GLB                             | U=10,D=50,G=100,F=7                                                                                                     |                        |                                                                                                                  |                                                |                                                 |
|     |                 |                                                                                                           | corridorinaloopwhileholdingtheUEs |     |     |                                                 |                                                                                                                                  |                                  | (cid:18)(cid:33)(cid:38)(cid:38)(cid:25)(cid:33)(cid:42)(cid:38)(cid:29)1                                               |                        |                                                                                                                  |                                                |                                                 |
|     |                 |                                                                                                           |                                   |     |     | (cid:8)(cid:7)(cid:10)                          |                                                                                                                                  |                                  |                                                                                                                         | (cid:8)(cid:7)(cid:10) |                                                                                                                  |                                                |                                                 |
|     |                 |                                                                                                           | UEswaswiththeuserdrivingin        |     |     |                                                 |                                                                                                                                  |                                  | (cid:23)(cid:29)(cid:35)(cid:36)(cid:39)(cid:29)(cid:35)(cid:36)                                                        |                        |                                                                                                                  |                                                |                                                 |
|     | driving         |                                                                                                           |                                   |     |     |                                                 | TM                                                                                                                               | 5GMB                             | U=10,D=75,G=100,F=5                                                                                                     |                        |                                                                                                                  |                                                |                                                 |
|     |                 |                                                                                                           | alooparoundtheuniversityarea      |     |     | (cid:8)(cid:7)(cid:8)                           |                                                                                                                                  |                                  |                                                                                                                         | (cid:8)(cid:7)(cid:8)  |                                                                                                                  |                                                |                                                 |
|     |                 |                                                                                                           |                                   |     |     |                                                 | (cid:10)(cid:13) (cid:11)(cid:8)                                                                                                 | (cid:11)(cid:13) (cid:12)(cid:8) | (cid:12)(cid:13) (cid:13)(cid:8) (cid:13)(cid:13)                                                                       | (cid:14)(cid:8)        | (cid:10)(cid:7)(cid:14) (cid:10)(cid:7)(cid:16)                                                                  | (cid:11)(cid:7)(cid:8) (cid:11)(cid:7)(cid:10) | (cid:11)(cid:7)(cid:12) (cid:11)(cid:7)(cid:14) |
|     |                 |                                                                                                           |                                   |     |     |                                                 | (cid:9)(cid:21)(cid:17)(cid:3) )(cid:47)((cid:38))(cid:29) (cid:3)-(cid:36)(cid:39)(cid:33)(cid:3)(cid:4)(cid:39)(cid:44)(cid:5) |                                  |                                                                                                                         |                        |  (cid:43))(cid:42)(cid:30))0(cid:7)(cid:31))(cid:39)(cid:3)(cid:24)(cid:22)(cid:26)(cid:3)(cid:4)(cid:44)(cid:5) |                                                |                                                 |
|     |                 | (cid:28)(cid:29)(cid:38)(cid:37)(cid:36)((cid:34)(cid:3)(cid:4)(cid:27)(cid:33)(cid:43)(cid:36)2)((cid:5) |                                   |     |     |                                                 |                                                                                                                                  |                                  | (cid:19)(cid:43)(cid:36).(cid:36)((cid:34)(cid:3)(cid:4)(cid:26)(cid:6)(cid:23))(cid:30)(cid:36)(cid:38)(cid:33)(cid:5) |                        |                                                                                                                  |                                                |                                                 |
(cid:9)(cid:7)(cid:8) (cid:9)(cid:7)(cid:8) (cid:9)(cid:7)(cid:8) (cid:9)(cid:7)(cid:8)
(cid:8)(cid:7)(cid:16) (cid:8)(cid:7)(cid:16) (cid:8)(cid:7)(cid:16) (cid:8)(cid:7)(cid:16)
(cid:20)(cid:19)(cid:18) (cid:8)(cid:7)(cid:14) (cid:8)(cid:7)(cid:14) (cid:20)(cid:19)(cid:18) (cid:8)(cid:7)(cid:14) (cid:8)(cid:7)(cid:14)
(cid:8)(cid:7)(cid:12) (cid:22)(cid:36).(cid:33) (cid:8)(cid:7)(cid:12) (cid:8)(cid:7)(cid:12) (cid:8)(cid:7)(cid:12)
(cid:18)(cid:33)(cid:38)(cid:38)(cid:25)(cid:33)(cid:42)(cid:38)(cid:29)1
(cid:8)(cid:7)(cid:10) (cid:8)(cid:7)(cid:10) (cid:8)(cid:7)(cid:10) (cid:8)(cid:7)(cid:10)
(cid:23)(cid:29)(cid:35)(cid:36)(cid:39)(cid:29)(cid:35)(cid:36)
(cid:8)(cid:7)(cid:8) (cid:8)(cid:7)(cid:8) (cid:8)(cid:7)(cid:8) (cid:8)(cid:7)(cid:8)
(cid:10)(cid:13) (cid:11)(cid:8) (cid:11)(cid:13) (cid:12)(cid:8) (cid:12)(cid:13) (cid:13)(cid:8) (cid:13)(cid:13) (cid:14)(cid:8) (cid:10)(cid:7)(cid:14) (cid:10)(cid:7)(cid:16) (cid:11)(cid:7)(cid:8) (cid:11)(cid:7)(cid:10) (cid:11)(cid:7)(cid:12) (cid:11)(cid:7)(cid:14) (cid:11)(cid:8) (cid:11)(cid:13) (cid:12)(cid:8) (cid:12)(cid:13) (cid:13)(cid:8) (cid:13)(cid:13) (cid:14)(cid:8) (cid:14)(cid:13) (cid:15)(cid:8) (cid:10)(cid:7)(cid:14) (cid:10)(cid:7)(cid:16) (cid:11)(cid:7)(cid:8) (cid:11)(cid:7)(cid:10) (cid:11)(cid:7)(cid:12) (cid:11)(cid:7)(cid:14)
(cid:9)(cid:21)(cid:17)(cid:3) )(cid:47)((cid:38))(cid:29) (cid:3)-(cid:36)(cid:39)(cid:33)(cid:3)(cid:4)(cid:39)(cid:44)(cid:5)  (cid:43))(cid:42)(cid:30))0(cid:7)(cid:31))(cid:39)(cid:3)(cid:24)(cid:22)(cid:26)(cid:3)(cid:4)(cid:44)(cid:5) (cid:9)(cid:21)(cid:17)(cid:3) )(cid:47)((cid:38))(cid:29) (cid:3)-(cid:36)(cid:39)(cid:33)(cid:3)(cid:4)(cid:39)(cid:44)(cid:5)  (cid:43))(cid:42)(cid:30))0(cid:7)(cid:31))(cid:39)(cid:3)(cid:24)(cid:22)(cid:26)(cid:3)(cid:4)(cid:44)(cid:5)
CellReplaymana(cid:19)ge(cid:43)s(cid:36).t(cid:36)o(c(cid:34)a(cid:3)(cid:4)p(cid:26)t(cid:6)u(cid:23)re)m(cid:30)(cid:36)o(cid:38)(cid:33)re(cid:5)applicationperformancevariabilityundermobilitycomparedtoMahimahi.WecuttheCDF
Figure16:
| graphasthetailistoolong. (cid:9)(cid:7)(cid:8) |                                     |     | (cid:9)(cid:7)(cid:8)  |     |           |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | ----------------------------------- | --- | ---------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| (cid:8)(cid:7)(cid:16)                         |                                     |     | (cid:8)(cid:7)(cid:16) |     |           |     |     |     |     |     |     |     |     |
| the ability                                    | to run unmodifiedapplications,orthe |     |                        |     | option to |     |     |     |     |     |     |     |     |
Table3:Listofwebpagesusedfortestingalongwithdetails
| nesttheshellwithanotherMahimahishell,suchastheHTTP (cid:20)(cid:19)(cid:18) (cid:8)(cid:7)(cid:14) |                |     | (cid:8)(cid:7)(cid:14)      |          |        |                |             |              |      |              |            |       |              |
| -------------------------------------------------------------------------------------------------- | -------------- | --- | --------------------------- | -------- | ------ | -------------- | ----------- | ------------ | ---- | ------------ | ---------- | ----- | ------------ |
|                                                                                                    |                |     |                             |          |        |                | on the page | composition, |      | including    | the number |       | of objects   |
| (cid:8)(cid:7)(cid:12)                                                                             |                |     | sh(cid:8)e(cid:7)l(cid:12)l |          |        |                |             |              |      |              |            |       |              |
| ReplayShell.                                                                                       | The CellReplay |     | accepts                     | the base | delay, |                |             |              |      |              |            |       |              |
|                                                                                                    |                |     |                             |          |        | (“#objs.”),and |             | the          | mean | (“avg. sz.”) | and        | total | (“tot. sz.”) |
lightPDOtrace,andheavyPDO(cid:8)t(cid:7)r(cid:10)aceasinputs.Similarto (cid:8)(cid:7)(cid:10)
compressedobjectsizes(bothinKB).“PT”indicatespage
theMahimahinetworkemulators(cid:8)h(cid:7)e(cid:8)ll,CellReplaycontrolsa (cid:8)(cid:7)(cid:8)
type.
| virtualnetworkdevice(TUN)andcap(cid:10)tu(cid:7)(cid:14)re(cid:10)s(cid:7)(cid:16)all(cid:11)I(cid:7)P(cid:8) (cid:11)(cid:8) (cid:11)(cid:13) | (cid:12)(cid:8) (cid:12)(cid:13) (cid:13)(cid:8) (cid:13)(cid:13) | (cid:14)(cid:8) (cid:14)(cid:13) | (cid:15)(cid:8) |     | d(cid:11)a(cid:7)t(cid:10)ag(cid:11)r(cid:7)a(cid:12)m(cid:11)s(cid:7)(cid:14) |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------- | --------------- | --- | ------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
fromanunmodifiedapplicationrunning (cid:9)(cid:21)(cid:17)(cid:3) )(cid:47)((cid:38))(cid:29) (cid:3)-(cid:36)(cid:39)(cid:33)(cid:3)(cid:4)(cid:39)(cid:44)(cid:5)   i (cid:43) n ) s (cid:42) i (cid:30) d ) e 0(cid:7) t (cid:31) h ) e (cid:39)(cid:3) s (cid:24) h (cid:22)(cid:26) e (cid:3) l (cid:4) l (cid:44) . (cid:5) It PT ID URL #objs. avg.sz. tot.sz.
thendelayseachpacketbeforesendingittoanotherinterface, L1 bing.com 2 205.53 411.06
| suchasloopbackorEthernet. |     |     |     |     |     |     | L2      |               |     |     | 36  | 24.66  | 887.64  |
| ------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --- | --- | ------ | ------- |
|                           |     |     |     |     |     |     | gnidnaL | microsoft.com |     |     |     |        |         |
|                           |     |     |     |     |     |     |         |               |     |     |     | 22.15  | 1683.49 |
| C Experimentalconditions  |     |     |     |     |     |     | L3      | dropbox.com   |     |     | 76  |        |         |
|                           |     |     |     |     |     |     | L4      | glassdoor.com |     |     | 64  | 43.23  | 2766.46 |
|                           |     |     |     |     |     |     | L5      | discord.com   |     |     | 37  | 172.86 | 6395.86 |
TheenvironmentsusedforevaluationarelistedinTable2.
|     |     |     |     |     |     |     | I1  | en.wikipedia.org/wiki/Naivety |     |     | 19  | 13.51 | 256.64 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ----- | ------ |
D Testedwebpageslist
|     |     |     |     |     |     |     | lanretnI I2 | box.com/about-us  |     |     | 48  | 14.39 | 690.95  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | --- | --- | --- | ----- | ------- |
|     |     |     |     |     |     |     | I3          | etsy.com/payments |     |     | 50  | 28.92 | 1446.22 |
Thelistofwebpagesusedfortestinganditsdetailsonpage
|     |     |     |     |     |     |     | I4  | youtube.com/user/ESPN |     |     | 44  | 56.88 | 2502.53 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ----- | ------- |
compositionisdetailedinTable3
|     |     |     |     |     |     |     | I5  | colubrina.tumblr.com |     |     | 69  | 116.57 | 8043.10 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ------ | ------- |
E Moreevaluationresults tothe10th,50th,and90thpercentilesoftheHTTP/1.1landing
pages.Wetestedrandomfiledownloadswithsizesranging
E.1 Non-idealnetworkconditions
from1KBto10MB.Theexperimentwassplitintotwoparts:
| We evaluated | CellReplay’s | accuracy | under | two | challeng- |     |     |     |     |     |     |     |     |
| ------------ | ------------ | -------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
oneforweb-pageloadsandtheotherforfiledownloads.Each
ing network conditions. In this first condition, labeled as partconsistedof10randomizedtrials.Inthefirstpart,each
‘stationary-weak’,UEsconnectedtoT-Mobilewereplaced trialincludedloading three pages andtwo recordsessions,
| in a windowless | basementinside |     | a building. | In the | second |     |     |     |     |     |     |     |     |
| --------------- | -------------- | --- | ----------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
whilethesecondparthadonerandomfiledownloadtestand
condition,labeledas‘stationary-crowded’,weplacedthe tworecordsessionspertrial.Everytestandrecordsession
UEs(connectedtoVerizon)inalibraryduringcrowdedor lasted 60s. The total experiment time under each network
rush hours. Both web-page loads and file downloads were conditionwas80minutes.
testedundertheseconditions.Toreducethenumberoftests
andminimizevariance,weonlyselectedpagescorresponding Per Figure 17, across the two network conditions and
USENIX Association 22nd USENIX Symposium on Networked Systems Design and Implementation    1185

1L 3L 5L BK1 BK01 BK001 BM1 BM01
35
30
25
20
15
10
5
0
)%(
rorrE
Stationary-weak (T-Mobile)
CellReplay
Mahimahi
1L 3L 5L BK1 BK01 BK001 BM1 BM01
Stationary-crowded (Verizon)
35
30
25
20
15
10
5
0
Figure17:ThewebPLTandfiledownloademulationdistribution
errorwhentestingundernon-idealstationarycases.
Table 4: Mean file downloadtime (in ms) ofmedium-sized
fileswithitsemulationdistributionerror.
1MB 10MB
eliboM-T Live 142.52 1056
CellReplay 135.88(7.82%) 978.18(8.19%)
Mahimahi 117.68(20.17%) 847.45(20.44%)
nozireV
Live 155.18 1069.25
CellReplay 135.68(10.46%) 974.98(4.88%)
Mahimahi 106.63(26.5%) 762.3(23.67%)
providers, CellReplay has an average distribution error of
5.96% for web-page loads and 7.9% for file downloads.
Mahimahi, in contrast, has mean distribution errors of
13.63%and22.02%forthesameapplications,respectively.
Evenunderchallengingconditions(stationary-weakand
stationary-crowded),CellReplaystilloffersarespectable
errorrateandoutperformsMahimahi.
E.2 Experimentsundermobility
Figure16demonstratesCellReplay’sabilitytocaptureappli-
cationperformanceundermobilityscenariosmoreaccurately
thanMahimahi.
E.3 Medium-sizedfiledownloadtest
Table 4 shows the mean file download time alongside its
distribution emulation errorforCellReplayandMahimahi,
comparedtothelivenetworks.
F Ethics
WenotethatCellReplaycannotbeusedtocollectotherusers’
packets; it only collects traces of its own user. Moreover,
traces collected by CellReplay do not contain any private
information.Hence,webelieveourworkdoesnotraiseany
ethicalconcerns.
1186 22nd USENIX Symposium on Networked Systems Design and Implementation USENIX Association