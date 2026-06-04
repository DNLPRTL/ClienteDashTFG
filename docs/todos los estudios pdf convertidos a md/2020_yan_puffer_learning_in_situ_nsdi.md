Learning in situ: a randomized experiment
in video streaming
Francis Y. Yan and Hudson Ayers, Stanford University; Chenzhi Zhu,
Tsinghua University; Sadjad Fouladi, James Hong, Keyi Zhang, Philip Levis,
and Keith Winstein, Stanford University
https://www.usenix.org/conference/nsdi20/presentation/yan
This paper is included in the Proceedings of the
17th USENIX Symposium on Networked Systems Design
and Implementation (NSDI ’20)
February 25–27, 2020 • Santa Clara, CA, USA
978-1-939133-13-7
Open access to the Proceedings of the
17th USENIX Symposium on Networked
Systems Design and Implementation
(NSDI ’20) is sponsored by

|     |     | Learning | in  | situ: | a randomized |     | experiment | in  | video | streaming |     |     |     |
| --- | --- | -------- | --- | ----- | ------------ | --- | ---------- | --- | ----- | --------- | --- | --- | --- |
ChenzhiZhu†
|     |     | FrancisY.Yan |     |     | HudsonAyers |     |             |     | SadjadFouladi |     |     |     |     |
| --- | --- | ------------ | --- | --- | ----------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- |
|     |     | JamesHong    |     |     | KeyiZhang   |     | PhilipLevis |     | KeithWinstein |     |     |     |     |
StanfordUniversity,†TsinghuaUniversity
|     |     |     | Abstract |     |     |     | Intheacademicliterature,manyrecentABRalgorithmsuse |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
statisticalandmachine-learningmethods[4,25,38–40,46],
| We describe | the | results | ofa randomizedcontrolledtrialof |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichallowalgorithmstoconsidermanyinputsignalsand
video-streamingalgorithmsforbitrateselectionandnetwork
|     |     |     |     |     |     |     | try to perform | well | for | a wide | variety | of clients. | An ABR |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | --- | ------ | ------- | ----------- | ------ |
prediction.Overthelastyear,wehavestreamed38.6years
decisioncandependonrecentthroughput,client-sidebuffer
| of video | to 63,508 | users | across | the Internet. | Sessions | are |     |     |     |     |     |     |     |
| -------- | --------- | ----- | ------ | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
occupancy,delay,theexperienceofclientsonsimilarISPsor
randomizedinblindedfashionamongalgorithms.
typesofconnectivity,etc.Machinelearningcanfindpatterns
Wefoundthatinthisreal-worldsetting,itisdifficultforso-
inseasofdataandisanaturalfitforthisproblemdomain.
phisticatedormachine-learnedcontrolschemestooutperform
However,itisaperenniallessonthattheperformanceof
| a “simple” | scheme | (buffer-basedcontrol),notwithstanding |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
learnedalgorithmsdependsonthedataorenvironmentsused
| goodperformanceinnetworkemulatorsorsimulators. |     |     |     |     |     | We  |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
totrainthem.MLapproachestovideostreamingandother
performedastatisticalanalysisandfoundthattheheavy-tailed
wide-areanetworkingchallengesareoftenhamperedintheir
natureofnetworkanduserbehavior,aswellasthechallenges
|     |     |     |     |     |     |     | access to | good and | representative |     | training | data. | The Inter- |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------------- | --- | -------- | ----- | ---------- |
ofemulatingdiverseInternetpathsduringtraining,present
netiscomplexanddiverse,individualnodesonlyobservea
obstaclesforlearnedalgorithmsinthissetting.
|     |     |     |     |     |     |     | noisy sliverof | the | system | dynamics,and |     | behavioris | often |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------------ | --- | ---------- | ----- |
WethendevelopedanABRalgorithmthatrobustlyoutper-
heavy-tailedandchangeswithtime.Evenwithrepresentative
formedotherschemes,byleveragingdatafromitsdeployment
throughputtraces,accuratelysimulatingoremulatingthedi-
andlimitingthescopeofmachinelearningonlytomaking
versityofInternetpathsrequiresmorethanreplayingsuch
predictionsthatcanbecheckedsoonafter.Thesystemuses
tracesandisbeyondcurrentcapabilities[15,16,31,45].
supervisedlearninginsitu,withdatafromtherealdeployment
Asaresult,theperformanceofalgorithmsinemulatedenvi-
environment,totrainaprobabilisticpredictorofupcoming
ronmentsmaynotgeneralizetotheInternet[7].Forexample,
chunktransmissiontimes.Thismoduletheninformsaclassi-
calcontrolpolicy(modelpredictivecontrol). CS2P’sgainsweremoremodestoverrealnetworksthanin
simulation[40].MeasurementsofPensieve[25]sawnarrower
| To support | further | investigation, |     | we  | are publishing | an  |             |         |       |      |       |             |           |
| ---------- | ------- | -------------- | --- | --- | -------------- | --- | ----------- | ------- | ----- | ---- | ----- | ----------- | --------- |
|            |         |                |     |     |                |     | benefits on | similar | paths | [11] | and a | large-scale | streaming |
archiveofdataandresultseachweek,andwillopenourongo-
|     |     |     |     |     |     |     | service [24]. | Other | learned | algorithms, |     | such | as the Remy |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | ----------- | --- | ---- | ----------- |
ingstudytothecommunity.Wewelcomeotherresearchersto
congestion-controlschemes,havealsoseeninconsistentre-
usethisplatformtodevelopandvalidatenewalgorithmsfor
sultsonrealnetworks,despitegoodresultsinsimulation[45].
bitrateselection,networkprediction,andcongestioncontrol.
Thispaperseekstoanswer:whatdoesittaketocreatea
learnedABRalgorithmthatrobustlyperformswelloverthe
1 Introduction wildInternet?WereportthedesignandfindingsofPuffer1,
|     |     |     |     |     |     |     | an ongoing | research | study | that | operates | a video-streaming |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ----- | ---- | -------- | ----------------- | --- |
VideostreamingisthepredominantInternetapplication,mak- website open to the public. Over the past year, Puffer has
ing up almost three quarters of all traffic [41]. One key al- streamed38.6yearsofvideoto63,508distinctusers,while
| gorithmic | question | in video | streaming |     | is adaptive | bitrate |     |     |     |     |     |     |     |
| --------- | -------- | -------- | --------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
recordingclienttelemetryforanalysis(currentloadisabout
selection,orABR,whichdecidesthecompressionlevelse- 60stream-daysofdataperday).Pufferrandomlyassignseach
lectedforeach“chunk,”orsegment,ofthevideo. ABRal- sessiontooneofasetofABRalgorithms;usersareblinded
gorithms optimize the user’s quality of experience (QoE): totheassignment.Wefind:
more-compressedchunksreducequality,butlargerchunks
maystallplaybackiftheclientcannotdownloadthemintime. 1https://puffer.stanford.edu
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation    495

Inourreal-worldsetting,sophisticatedalgorithmsbased Resultsofprimaryexperiment(Jan.26–Aug.7&Aug.30–Oct.16,2019)
on control theory [46] or reinforcement learning [25] Algorithm Timestalled MeanSSIM SSIMvariation Meanduration
(lowerisbetter) (higherisbetter) (lowerisbetter) (timeonsite)
didnotoutperformsimplebuffer-basedcontrol[18].We
Fugu 0.13% 16.64dB 0.74dB 33.6min
foundthatmore-sophisticatedalgorithmsdonotnecessarily
MPC-HM[46] 0.22% 16.61dB 0.79dB 30.8min
beatasimpler,olderalgorithm.Theneweralgorithmswere
BBA[18] 0.19% 16.56dB 1.11dB 32.1min
developedandevaluatedusingthroughputtracesthatmaynot Pensieve[25] 0.17% 16.26dB 1.05dB 31.6min
havecapturedenoughoftheInternet’sheavytailsandother RobustMPC-HM 0.12% 16.01dB 0.98dB 31.0min
dynamicswhenreplayedinsimulationoremulation.Training
them on more-representative traces doesn’t necessarily re- Figure1:Inaneight-monthrandomizedcontrolledtrialwith
versethis:weretrainedonealgorithmusingthroughputtraces blinded assignment, the Fugu scheme outperformed other
drawnfromPuffer(insteadofitsoriginalsetoftraces)and ABR algorithms. The primary analysis includes 637,189
evaluateditalsoonPuffer,buttheresultsweresimilar(§5.3). streams played by 54,612 client IP addresses (13.1 client-
yearsintotal).UncertaintiesareshowninFigures9and11.
Statisticalmarginsoferrorinquantifyingalgorithmper-
formanceareconsiderable.PriorworkonABRalgorithms
hasclaimedbenefitsof10–15%[46],3.2–14%[40],or12– work[25,37,44].Onewaytoachieverepresentativetraining
25%[25],basedonthroughputtracesorreal-worldexperi- istolearn in place(in situ)on theactualdeploymentenvi-
mentslastinghoursordays.However,wefoundthattheem- ronment,assuming the scheme can befeasiblytrainedthis
piricalvariabilityandheavytailsofthroughputevolutionand wayandthedeploymentiswidelyenoughusedtoexercisea
rebufferingcreatestatisticalmarginsofuncertaintythatmake broadrangeofscenarios.3Theapproachwedescribehereis
itchallengingtodetectrealeffectsofthismagnitude.Even onlyastepinthisdirection,butwebelievePuffer’sresults
withayearofexperienceperscheme,a20%improvementin
suggestthatlearnedsystemswillbenefitbyaddressingthe
rebufferingratiowouldbestatisticallyindistinguishable,i.e., challengeof“howwillwegetenoughrepresentativescenar-
belowthethresholdofdetectionwith95%confidence.These iosfortraining—whatisenough,andhowdowekeepthem
uncertaintiesaffectthedesignspaceofmachine-learningap- representativeovertime?”asafirst-classconsideration.
proachesthatcanpracticallybedeployed[13,26].
WeintendtooperatePufferasan“openresearch”project
Itispossibletorobustlyoutperformexistingschemesby aslongasfeasible.Weinvitetheresearchcommunitytotrain
combiningclassicalcontrolwithanMLpredictortrained and test new algorithms on randomized subsets of its traf-
insituonrealdata.WedescribeFugu,adata-drivenABR fic,gainingfeedbackonreal-worldperformancewithquanti-
algorithm thatcombines severaltechniques. Fugu is based fieduncertainty.Alongwiththispaper,wearepublishingan
onMPC(modelpredictivecontrol)[46],aclassicalcontrol archiveofdataandresultsbacktothebeginningof2019on
policy,butreplacesitsthroughputpredictorwithadeepneural thePufferwebsite,withnewdataandresultspostedweekly.
networktrainedusingsupervisedlearningondatarecordedin Inthenextfewsections,wediscussthebackgroundand
situ(inplace),meaningfromFugu’sactualdeploymentenvi- relatedworkonthisproblem(§2),thedesignofourblinded
ronment,Puffer.Thepredictorhassomeuncommonfeatures: randomized experiment (§3) and the Fugu algorithm (§4),
itpredictstransmissiontimegivenachunk’sfilesize(vs.esti- withexperimentalresults in Section 5,anda discussion of
matingthroughput),itoutputsaprobabilitydistribution(vs.a results and limitations in Section 6. In the appendices,we
pointestimate),anditconsiderslow-levelcongestion-control provideastandardizeddiagramoftheexperimentalflowfor
statisticsamongitsinputsignals.Ablationstudies(§4.2)find theprimaryanalysisanddescribethedatawearereleasing.
eachofthesefeaturestobenecessarytoFugu’sperformance.
In a controlled experiment during most of 2019, Fugu
2 Backgroundandrelatedwork
outperformed existing techniques—including the simple
algorithm—in stall ratio (with one exception), video qual-
Thebasicproblemofadaptivevideostreaminghasbeenthe
ity,andthe variability ofvideo quality (Figure 1). The im-
subjectofmuchacademicwork;foragoodoverview,werefer
provementsweresignificantbothstatisticallyand,perhaps,
thereadertoYinetal.[46].Webrieflyoutlinetheproblem
practically:userswhowererandomlyassignedtoFugu(in
here.Aservicewishestoserveapre-recordedorlivevideo
blindedfashion)chosetocontinuestreamingfor5–9%longer,
stream to a broad array of clients over the Internet. Each
onaverage,thanusersassignedtotheotherABRalgorithms.2
client’s connection has a different and unpredictable time-
Our results suggest that, as in other domains, good and varyingperformance.Becausetherearemanyclients,itisnot
representativetrainingisthekeychallengeforrobustperfor- feasiblefortheservicetoadjusttheencoderconfigurationin
manceoflearnednetworkingalgorithms,asomewhatdiffer- realtimetoaccommodateanyoneclient.
entpointofviewfromthegeneralizabilityargumentsinprior
3Evencollectingtracesfromadeploymentenvironmentandreplaying
2Thiseffectwasdrivensolelybyusersstreamingmorethan3hoursof theminasimulatororemulatortotrainacontrolpolicy—asistypically
video;wedonotfullyunderstandit. necessaryinreinforcementlearning—isnotwhatwemeanby“insitu.”
496 17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Instead,the service encodes the video into a handful of 3
alternativecompressedversions.Eachrepresentstheoriginal
2.8
video but at a different quality,target bitrate,orresolution.
Clientsessionschoosefromthislimitedmenu.Theservice 2.6
encodes the different versions in a way that allows clients
2.4
toswitchmidstreamasnecessary: itdividesthevideointo
0 40 80 120 160 200
chunks,typically2–6secondseach,andencodeseachversion
ofeachchunkindependently,soitcanbedecodedwithout
accesstoanyotherchunks.Thisgivesclientstheopportunity
toswitchbetweendifferentversionsateachchunkboundary.
Thedifferentalternativesaregenerallyreferredtoasdifferent
“bitrates,” althoughstreaming services today generally use
“variablebitrate”(VBR)encoding[32],wherewithineach
alternativestream,thechunksvaryincompressedsize[47].
Choosing which chunks to fetch. Algorithms that select
which alternative version of each chunk to fetch and play,
given uncertain future throughput, are known as adaptive
bitrate(ABR)schemes.Theseschemesfetchchunks,accu-
mulatingtheminaplaybackbuffer,whileplayingthevideoat
thesametime.Theplayheadadvancesanddrainsthebufferat
asteadyrate,1s/s,butchunksarriveatirregularintervalsdic-
tatedbythevaryingnetworkthroughputandthecompressed
sizeofeachchunk.Ifthebufferunderflows,playbackmust
stallwhiletheclient“rebuffers”:fetchingmorechunksbefore
resumingplayback.ThegoalofanABRalgorithmistypically
framedaschoosingtheoptimalsequenceofchunkstofetch
orreplace [38],given recentexperience andguesses about
the future,to minimize startup time and presence of stalls,
maximizethequalityofchunksplayedback,andminimize
variationinqualityovertime(especiallyabruptchangesin
quality).Theimportancetradeoffforthesefactorsiscaptured
inaQoEmetric;severalstudieshavecalibratedQoEmetrics
againsthumanbehaviororopinion[6,12,21].
Adaptivebitrateselection.Researchershaveproducedalit-
eratureofABRschemes,including“rate-based”approaches
that focus on matching the video bitrate to the network
throughput[20,23,27],“buffer-based”algorithmsthatsteer
thedurationoftheplaybackbuffer[18,38,39],andcontrol-
theoreticschemesthattrytomaximizeexpectedQoEover
a receding horizon,given the upcoming chunk sizes and a
predictionofthefuturethroughput.
ModelPredictiveControl(MPC),FastMPC,andRobust-
MPC[46]fallintothelastcategory.Theycomprisetwomod-
ules:athroughputpredictorthatinformsapredictivemodel
ofwhatwillhappentothebufferoccupancyandQoEinthe
nearfuture,dependingonwhichchunksitfetches,withwhat
quality andsizes. MPC uses the modelto plan a sequence
ofchunksoveralimitedhorizon(e.g.,thenext5–8chunks)
tomaximizetheexpectedQoE.WeimplementedMPCand
RobustMPCforPuffer,usingthesamepredictorasthepaper:
theharmonicmeanofthelastfivethroughputsamples.
CS2P[40]andOboe-tunedRobustMPC[4]arerelatedto
MPC;theyconstitutebetterthroughputpredictorsthatinform
)spbM(
tuphguorhT
2.8
2.4
2.0
1.6
Epoch
(a)CS2Pexamplesession(Fig-
ure4afrom[40])
)spbM(
tuphguorhT
0 50 100 150 200
Epoch
(b) TypicalPuffersession with
similarmeanthroughput
Figure2:PufferhasnotobservedCS2P’sdiscretethroughput
states.(Epochsare6secondsinbothplots.)
thesamecontrolstrategy(MPC).Thesethroughputpredictors
weretrainedonrealdatasetsthatrecordedtheevolutionof
throughputovertimewithinasession.CS2Pclustersusersby
similarityandmodelstheirevolvingthroughputasaMarko-
vianprocesswithasmallnumberofdiscretestates;Oboeuses
asimilarmodeltodetectwhenthenetworkpathhaschanged
state.Inourdataset,wehavenotobservedCS2PandOboe’s
observationofdiscretethroughputstates(Figure2).
Fugufitsinthissamecategoryofalgorithms.Italsouses
MPCasthecontrolstrategy,informedbyanetworkpredic-
tortrainedonrealdata.Thiscomponent,whichwecallthe
TransmissionTimePredictor(TTP),incorporatesanumber
ofuncommonfeatures,noneofwhichcanclaimnoveltyon
its own. The TTP explicitlypredicts the transmission time
ofachunkwithgivensizeandisn’ta“throughput”predictor
perse.Athroughputpredictormodelsthetransmissiontime
ofachunkasscalinglinearlywithsize,butitiswellknown
thatobservedthroughputvarieswithfilesize[7,32,47],in
partbecauseoftheeffectsofcongestioncontrolandbecause
chunksofdifferentsizesexperiencedifferenttimeintervals
ofthepath’svaryingcapacity.Toourknowledge,Fuguisthe
firsttousethisfactoperationallyaspartofacontrolpolicy.
Fugu’spredictorisalsoprobabilistic:itoutputsnotasingle
predictedtransmissiontime,butaprobabilitydistributionon
possibleoutcomes.Theuseofuncertaintyinmodelpredictive
controlhasalonghistory[36],buttoourknowledgeFugu
is the first to use stochastic MPC in this context. Finally,
Fugu’spredictorisaneuralnetwork,whichletsitconsider
an array ofdiverse signals thatrelate to transmission time,
includingrawcongestion-controlstatisticsfromthesender-
sideTCPimplementation[17,42].Wefoundthatseveralof
thesesignals(RTT,CWND,etc.)benefitABRdecisions(§5).
Pensieve[25]isanABRschemealsobasedonadeepneu-
ralnetwork.UnlikeFugu,Pensieveusestheneuralnetwork
notsimplytomakepredictionsbuttomakedecisionsabout
whichchunkstosend.Thisaffectsthetypeoflearningused
totrainthealgorithm.WhileCS2PandFugu’sTTPcanbe
trainedwithsupervisedlearning(topredictchunktransmis-
siontimesrecordedfrompastdata),ittakesmorethandatato
trainaschemethatmakesdecisions;oneneedstrainingenvi-
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation 497

|     | 5500 kbps |     |     | 18                |     |     |     |     |      |     | Fugu |        |     |
| --- | --------- | --- | --- | ----------------- | --- | --- | --- | --- | ---- | --- | ---- | ------ | --- |
|     | 200 kbps  |     |     | )Bd( MISS egarevA |     |     |     |     | 16.6 |     |      |        |     |
|     | 6         |     |     | 16                |     |     |     |     |      |     |      | MPC-HM |     |
BBA
| )BM( eziS |     |     |     | 14  |     |     |     |     |                   | Higher quality per byte |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------------- | --- | --- | --- |
|           | 4   |     |     |     |     |     |     |     | )Bd( MISS egarevA |                         |     |     |     |
|           |     |     |     | 12  |     |     |     |     | 16.4              |                         |     |     |     |
10
2
|     |     |     |     | 8   |     |     | 5500 kbps |     |      |     |     | Pensieve |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --- | --- | -------- | --- |
|     |     |     |     |     |     |     | 200 kbps  |     | 16.2 |     |     |          |     |
|     | 0   |     |     | 6   |     |     |           |     |      |     |     |          |     |
|     | 1   | 2   | 3   |     | 1   | 2   | 3         |     |      |     |     |          |     |
RobustMPC-HM
|     |              | Chunk number |       |             | Chunk number |      |        |     | 16  |     |     |     |     |
| --- | ------------ | ------------ | ----- | ----------- | ------------ | ---- | ------ | --- | --- | --- | --- | --- | --- |
| (a) | VBR encoding | lets         | chunk | (b) Picture | quality      | also | varies |     |     |     |     |     |     |
sizevarywithinastream[47]. withVBRencoding[32]. 4 4.1 4.2 4.3 4.4
Average bitrate (Mbit/s)
Figure3:Variationsinpicturequalityandchunksizewithin Figure4:OnPuffer,schemesthatmaximizeaverageSSIM
eachstreamsuggestabenefitfromchoosingchunksbasedon (MPC-HM, RobustMPC-HM, and Fugu) delivered higher
SSIMandsize,ratherthanaveragebitrate(legend). qualityvideoperbytesent,vs.thosethatmaximizebitrate
directly(Pensieve)ortheSSIMofeachchunk(BBA).
ronmentsthatrespondtoaseriesofdecisionsandjudgetheir
consequences.Thisisknownasreinforcementlearning(RL). in the event of lost transport-stream packets on either sub-
Generallyspeaking,RLtechniquesexpectasetoftrainingen- stream.Videochunksare2.002secondslong,reflectingthe
vironmentsthatcanexerciseacontrolpolicythrougharange 1/1001factorforNTSCframerates. Audiochunksare4.8
ofsituationsandactions[3],andneedtobeabletoobserve secondslong.Videoisde-interlacedwithffmpegtoproduce
adetectabledifferenceinperformancebyslightlyvaryinga a“canonical”1080p60or720p60sourceforcompression.
controlaction. Systems thatare challenging to simulate or Puffer encodes each video chunk in ten different H.264
thathavetoomuchnoisepresentdifficulties[13,26]. versions,usinglibx264inveryfastmode.Theencodings
rangefrom240p60videowithconstantratefactor(CRF)of
26(about200kbps)to1080p60videowithCRFof20(about
3 Puffer:anongoinglivestudyofABR
5,500kbps).AudiochunksareencodedintheOpusformat.
Pufferthenusesffmpegtocalculateeachencodedchunk’s
| To  | understand | the challenges |     | of video | streaming | and | mea- |     |     |     |     |     |     |
| --- | ---------- | -------------- | --- | -------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- |
SSIM[43],ameasureofvideoquality,relativetothecanoni-
| sure | the behaviorofABR |     | schemes,we |     | builtPuffer,a |     | free, |     |     |     |     |     |     |
| ---- | ----------------- | --- | ---------- | --- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
calsource.Thisinformationisusedbytheobjectivefunction
publiclyaccessiblewebsitethatlive-streamssixover-the-air
ofBBA,MPC,RobustMPC,andFugu,andforourevalua-
commercialtelevisionchannels.Pufferoperatesasarandom-
tion.Inpractice,therelationshipbetweenbitrateandquality
izedcontrolledtrial;sessionsarerandomlyassignedtoone
ofa setofABR orcongestion-controlschemes. The study varieschunk-by-chunk(Figure3),anduserscannotperceive
compressedchunksizesdirectly—onlywhatisshownonthe
participantsincludeanymemberofthepublicwhowishesto
screen.ABRschemesthatmaximizebitratedonotnecessarily
participate.Usersareblindedtoalgorithmassignment,and
seeacommensuratebenefitinpicturequality(Figure4).
werecordclienttelemetryonvideoqualityandplayback.A
|     |     |     |     |     |     |     |     | Encoding | six channels |     | in ten | versions | each (60 streams |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ------ | -------- | ---------------- |
StanfordInstitutionalReviewBoarddeterminedthatPuffer
doesnotconstitutehumansubjectsresearch. total)withlibx264consumesabout48coresofanIntelx86-
|     |     |     |     |     |     |     |     | 64 2.7 GHz | CPU | in steady | state. | Calculating | the SSIM of |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------ | ----------- | ----------- |
Ourreasoningforstreaminglivetelevisionwastocollect
eachencodedchunkconsumesanadditional18cores.
| data | from | enough participants |     | and | network | paths to | draw |     |     |     |     |     |     |
| ---- | ---- | ------------------- | --- | --- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
robustconclusionsabouttheperformanceofalgorithmsfor
| ABR | control | and network | prediction. |     | Live television |     | is an |                               |     |     |     |     |     |
| --- | ------- | ----------- | ----------- | --- | --------------- | --- | ----- | ----------------------------- | --- | --- | --- | --- | --- |
|     |         |             |             |     |                 |     |       | 3.2 Servingchunkstothebrowser |     |     |     |     |     |
evergreensourceofpopularcontentthathadnotbeenbroadly
availableforfreeontheInternet.Ourstudybenefits,inpart, TomakeitfeasibletodeployandtestarbitraryABRschemes,
fromalawthatallowsnonprofitorganizationstoretransmit Pufferusesa“dumb”player(usingtheHTML5<video>tag
over-the-airtelevisionsignalswithoutcharge[1].Here,we andtheJavaScriptMedia SourceExtensions)on the client
describedetailsofthesystem,experiment,andanalysis. side,andplacestheABRschemeattheserver.Wehavea48-
coreserverwith10GbpsEthernetinadatacenteratStanford.
ThebrowseropensaWebSocket(TLS/TCP)connectionto
3.1 Back-end:decoding,encoding,SSIM
adaemonontheserver.Eachdaemonisconfiguredwitha
Puffer receives six television channels using a VHF/UHF differentTCPcongestioncontrol(fortheprimaryanalysis,
antenna andan ATSC demodulator,whichoutputs MPEG- weusedBBR[9])andABRscheme.Someschemesaremore
2 transport streams in UDP. We wrote software to decode efficientlyimplementedthanothers;onaveragetheCPUload
a stream to chunks ofraw decodedvideo andaudio,main- fromservingclienttraffic(includingTLS,TCP,andABR)
tainingsynchronization(byinsertingblackfieldsorsilence) is about 5% of an Intel x86-64 2.7 GHz core per stream.
498    17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Algorithm Control Predictor Optimizationgoal Howtrained
BBA classical(linearcontrol) n/a +SSIMs.t.bitrate<limit n/a
MPC-HM classical(MPC) classical(HM) +SSIM,–stalls,–∆SSIM n/a
RobustMPC-HM classical(robustMPC) classical(HM) +SSIM,–stalls,–∆SSIM n/a
Pensieve learned(DNN) n/a +bitrate,–stalls,–∆bitrate reinforcementlearninginsimulation
Fugu classical(MPC) learned(DNN) +SSIM,–stalls,–∆SSIM supervisedlearninginsitu
Figure5:Distinguishingfeaturesofalgorithmsusedintheprimaryexperiment.HM=harmonicmeanoflastfivethroughput
samples.MPC=modelpredictivecontrol.DNN=deepneuralnetwork.
Sessionsarerandomlyassignedtoservingdaemons.Users trainingdata,weusedtheauthors’providedscripttogenerate
canswitchchannelswithoutbreakingtheirTCPconnection 1000simulatedvideosastrainingvideos,andacombination
andmayhavemany“streams”withineachsession. oftheFCCandNorwaytraceslinkedtointhePensievecode-
Pufferisnotaclient-sideDASH[28](DynamicAdaptive baseastrainingtraces.
StreamingoverHTTP)system.LikeDASH,though,Pufferis
anABRsystemstreamingchunkedvideooveraTCPconnec- 3.4 ThePufferexperiment
tion,andrunsthesameABRalgorithmsthatDASHsystems
canrun.Wedon’texpectthisarchitecturetoreplaceclient- Torecruitparticipants,wepurchasedGoogleandRedditads
sideABR(whichcanbeservedbyCDNedgenodes),butwe forkeywordssuchas“livetv”and“tvstreaming”andpaid
expectitsconclusionstotranslatetoABRschemesbroadly. peopleonAmazonMechanicalTurktousePuffer.Wewere
ThePufferwebsiteworksintheChrome,Firefox,Edge,and alsofeaturedinpressarticles.Popularprograms(e.g.the2019
Operabrowsers,includingonAndroidphones,butdoesnot and2020SuperBowls,theOscars,WorldCup,and“Bachelor
playintheSafaribrowseroroniOS(whichlacksupportfor inParadise”)broughtlargespikes(>20×)overbaselineload.
theMediaSourceExtensionsorOpusaudio). Ourcurrentaverageloadisabout60concurrentstreams.
BetweenJan.26,2019andFeb.2,2020,wehavestreamed
38.6 years ofvideo to 63,508 registeredstudy participants
3.3 HostingarbitraryABRschemes
using111,231uniqueIPaddresses.Abouteightmonthsof
We implemented buffer-based control (BBA), MPC, Ro- that period was spent on the “primary experiment,” a ran-
bustMPC,andFugu in back-enddaemonsthatservevideo domizedtrialcomparingFuguwithotheralgorithms:MPC,
chunksovertheWebSocket.WeuseSSIMintheobjective RobustMPC,Pensieve,andBBA(asummaryoffeaturesis
functions foreach of these schemes. ForBBA,we use the in Figure 5). This periodsaw a totalof314,577 streaming
formula in the original paper [18] to decide the maximum sessions,and1,904,316individualstreams.Anexperimental-
chunksize,andsubjecttothisconstraint,thechunkwiththe flowdiagraminthestandardizedCONSORTformat[35]is
highestSSIMisselectedtostream.Wealsochoosereservoir intheappendix(FigureA1).
valuesconsistentwithour15-secondmaximumbuffer. Werecordclienttelemetryastime-seriesdata,detailingthe
sizeandSSIMofeveryvideochunk,thetimetodelivereach
DeployingPensieveforlivestreaming.Weusethereleased
chunktotheclient,thebuffersizeandrebufferingeventsat
Pensievecode(writteninPythonwithTensorFlow)directly.
theclient,theTCPstatisticsontheserver,andtheidentityof
WhenaclientisassignedtoPensieve,PufferspawnsaPython
theABRandcongestion-controlschemes.Afulldescription
subprocessrunningPensieve’smulti-videomodel.
ofthedataisinAppendixB.
We contacted the Pensieve authors to request advice on
deployingthealgorithminalive,multi-video,real-worldset- Metricsandstatisticaluncertainty.Wegroupthetimese-
ting.Theauthorsrecommendedthatweusealonger-running riesbyuserstreamtocalculateasetofsummaryfigures:the
trainingandthatwetunetheentropyparameterwhentraining total time between the first and last recorded events of the
themulti-videoneuralnetwork.Wewroteanautomatedtool stream,thestartuptime,thetotalwatchtimebetweenthefirst
to train 6 different models with various entropy reduction andlastsuccessfullyplayedportionofthestream,thetotal
schemes.Wetestedthesemanuallyoverafewrealnetworks, timethevideoisstalledforrebuffering,theaverageSSIM,
thenselectedthemodelwiththebestperformance.Wemod- andthechunk-by-chunkvariationinSSIM.Theratiobetween
ifiedthePensievecode(andconfirmedwiththeauthors)so “totaltimestalled”and“totalwatchtime”isknownasthere-
thatitdoesnotexpectthevideotoendbeforeauser’ssession bufferingratioorstallratio,andiswidelyusedtosummarize
completes.WewerenotabletomodifyPensievetooptimize theperformanceofstreamingvideosystems[22].
SSIM;itconsiderstheaveragebitrateofeachPufferstream. Weobserveconsiderableheavy-tailedbehaviorinmostof
Weadjustedthevideochunklengthto2.002secondsandthe thesestatistics.Watchtimesareskewed(Figure11),andwhile
bufferthresholdto15secondstoreflectourparameters.For the risk of rebuffering is important to any ABR algorithm,
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation 499

actualrebufferingisararephenomenon.Ofthe637,189eli-
giblestreamsconsideredfortheprimaryanalysisacrossall
fiveABRschemes,only24,328(4%)ofthosestreamshad
anystalls,mirroringcommercialservices[22].
Theseskeweddistributionscreatemoreroomfortheplay
ofchancetocorruptthebottom-linestatisticssummarizinga
scheme’sperformance—eventwoidenticalschemeswillsee
considerablevariationinaverageperformanceuntilasubstan-
tialamountofdataisassembled.Inthisstudy,weworkedto
quantifythestatisticaluncertaintythatcanbeattributedtothe
playofchanceinassigningsessionstoABRalgorithms.We
calculateconfidenceintervalsonrebufferingratiowiththe
bootstrapmethod[14],simulatingstreamsdrawnempirically
fromeachscheme’sobserveddistributionofrebufferingratio
as a function of stream duration. We calculate confidence
intervals on average SSIM using the formula forweighted
standarderror,weightingeachstreambyitsduration.
Thesepracticesresultinsubstantialconfidenceintervals:
withatleast2.5yearsofdataforeachscheme,thewidthofthe
95%confidenceintervalonascheme’sstallratioisbetween
±13%and±21%ofthemeanvalue.Thisiscomparableto
themagnitudeofthetotalbenefitreportedbysomeacademic
workthatusedmuchshorterreal-worldexperiments. Even
arecentstudyofaPensieve-likeschemeonFacebook[24],
encompassing30millionstreams,didnotdetectachangein
rebufferingratiooutsidethelevelofstatisticalnoise.
We conclude that considerations of uncertainty in real-
worldlearningandexperimentation,especiallygivenuncon-
trolleddatafromtheInternetwithrealusers,deservefurther
study. Strategies to import real-world data into repeatable
emulators [45] or reduce their variance [26] will likely be
helpfulinproducingrobustlearnednetworkingalgorithms.
4 Fugu:designandimplementation
Fuguisacontrolalgorithmforbitrateselection,designedto
befeasiblytrainedinplace(insitu)onarealdeploymentenvi-
ronment.Itconsistsofaclassicalcontroller(modelpredictive
control,thesameasinMPC-HM),informedbyanonlinear
predictorthatcanbetrainedwithsupervisedlearning.
Figure6showsFugu’shigh-leveldesign.Fugurunsonthe
server,makingiteasytoupdateitsmodelandaggregateper-
formancedataacrossclientsovertime.Clientssendnecessary
telemetry,suchasbufferlevels,totheserver.
Puffer
Data Aggregation
Video Server
update state bitrate
model update selection
Transmission Time
MPC Controller
Predictor
gniniart
yliad
model-based
control
Thecontroller,describedinSection4.4,makesdecisions
by following a classical control algorithm to optimize an
objectiveQoEfunction(§4.1)basedonpredictionsforhow
longeachchunkwouldtaketotransmit.Thesepredictionsare
providedbytheTransmissionTimePredictor(TTP)(§4.2),
aneuralnetworkthatestimatesaprobabilitydistributionfor
thetransmissiontimeofaproposedchunkwithgivensize.
4.1 Objectivefunction
ForeachvideochunkK,Fuguhasaselectionofversionsof i
this chunkto choose from,Ks,eachwitha differentsize s.
i
Aswithpriorapproaches,FuguquantifiestheQoEofeach
chunkasalinearcombinationofvideoquality,videoquality
variation,andstalltime[46].Unlikesomepriorapproaches,
whichusetheaveragecompressedbitrateofeachencoding
settingasaproxyforimagequality,Fuguoptimizesapercep-
tualmeasureofpicturequality—inourcase,SSIM.Thishas
beenshowntocorrelatewithhumanopinionsofQoE[12].
Weemphasizethatweusetheexactsameobjectivefunction
inourversionofMPCandRobustMPCaswell.
LetQ(K)bethevideoqualityofachunkK,T(K)betheun-
certaintransmissiontimeofK,andB bethecurrentplayback i
buffersize.Following[46],FugudefinestheQoEobtained
bysendingKs(giventhepreviouslysentchunkK )as i i−1
QoE(Ks,K )=Q(Ks)−λ|Q(Ks)−Q(K )|
i i−1 i i i−1 (1)
−µ·max{T(Ks)−B,0},
i i
where max{T(Ks)−B,0} describes the stall time experi-
i i
encedbysendingKs,andλandµareconfigurationconstants
i
forhowmuchtoweightvideoqualityvariationandrebuffer-
ing.FuguplansatrajectoryofsizessofthefutureH chunks
tomaximizetheirexpectedtotalQoE.
4.2 TransmissionTimePredictor(TTP)
OnceFugudecideswhichchunkfromKs tosend,twopor-
i
tionsoftheQoEbecomeknown:thevideoqualityandvideo
qualityvariation.Theremaininguncertaintyisthestalltime.
Theserverknowsthecurrentplaybackbuffersize,sowhatit
needstoknowisthetransmissiontime:howlongwillittake
fortheclienttoreceivethechunk?Givenanoraclethatre-
portsthetransmissiontimeofanychunk,theMPCcontroller
cancomputetheoptimalplantomaximizeQoE.
Fuguusesatrainedneural-networktransmission-timepre-
dictortoapproximatetheoracle.Foreachchunkinthefixed
H-step horizon,we train a separate predictor. E.g.,if opti-
mizingforthetotalQoEofthenextfivechunks,fiveneural
networksaretrained.Thisletsusparallelizetraining.
EachTTPnetworkforthefuturesteph∈{0,...,H−1}
takesasinputavectorof:
1. sizesofpastt chunksK ,...,K ,
i−t i−1
Figure6:OverviewofFugu
2. actualtransmissiontimesofpastt chunks:T ,...,T ,
i−t i−1
500 17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

wherePr[Tˆ(Ks)=t]istheprobabilitypredictedbyTTPfor
3. internalTCPstatistics(Linuxtcp_infostructure),
i i
sizesofaproposedchunkKs thetransmissiontimeofK stobet ,andB canbederived
|     | 4.  |     |     |     | .   |     |     |     |     | i   | i   | i+1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i+h
|     |     |            |         |     |         |            |        | bysystemdynamics[46]givenanenumerated(discretized)t. |     |     |     |     | i   |
| --- | --- | ---------- | ------- | --- | ------- | ---------- | ------ | ---------------------------------------------------- | --- | --- | --- | --- | --- |
| The | TCP | statistics | include | the | current | congestion | window |                                                      |     |     |     |     |     |
Thecontrollercomputestheoptimaltrajectorybysolvingthe
size, the number of unacknowledged packets in flight, the abovevalueiterationwithdynamicprogramming(DP).To
| smoothed |     | RTT | estimate, | the minimum |     | RTT, and | the TCP |                                                   |     |     |     |     |        |
| -------- | --- | --- | --------- | ----------- | --- | -------- | ------- | ------------------------------------------------- | --- | --- | --- | --- | ------ |
|          |     |     |           |             |     |          |         | maketheDPcomputationalfeasible,italsodiscretizesB |     |     |     |     | i into |
estimatedthroughput(tcpi_delivery_rate).
|     |       |            |      |      |          |           |      | bins anduses | forwardrecursion |     | withmemoization |     | to only |
| --- | ----- | ---------- | ---- | ---- | -------- | --------- | ---- | ------------ | ---------------- | --- | --------------- | --- | ------- |
|     | Prior | approaches | have | used | Harmonic | Mean (HM) | [46] |              |                  |     |                 |     |         |
computeforrelevantstates.
oraHiddenMarkovModel(HMM)[40]topredictasingle
throughputfortheentirelookaheadhorizonirrespectiveofthe
sizeofchunktosend.Incontrast,theTTPacknowledgesthe 4.5 Implementation
factthatobservedthroughputvarieswithchunksize[7,32,47]
bytakingthesizeofproposedchunkKs TTP takes as input the past t = 8 chunks, and outputs a
asanexplicitinput.
i+h probability distribution over 21 bins of transmission time:
Inaddition,itoutputsadiscretizedprobabilitydistributionof
predictedtransmissiontimeTˆ(Ks ). [0,0.25),[0.25,0.75),[0.75,1.25),...,[9.75,∞),with0.5sec-
i+h
ondsasthebinsizeexceptforthefirstandthelastbins.TTP
isafullyconnectedneuralnetwork,withtwohiddenlayers
4.3 TrainingtheTTP
|     |     |     |     |     |     |     |     | with 64 neurons | each. | We tested | different | TTPs | with vari- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | --------- | --------- | ---- | ---------- |
ousnumbersofhiddenlayersandneurons,andfoundsimilar
Wesamplefromtherealusagedatacollectedbyanyscheme
running on Puffer and feed individual user streams to the traininglossesacrossarangeofconditionsforeach.Weim-
plementedTTPandthetraininginPyTorch,butweloadthe
| TTP | as  | training | input. For | the | TTP network | in  | the future |     |     |     |     |     |     |
| --- | --- | -------- | ---------- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
trainedmodelinC++whenrunningontheproductionserver
| step | h,each | user | stream | contains | a chunk-by-chunk |     | series |     |     |     |     |     |     |
| ---- | ------ | ---- | ------ | -------- | ---------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
of(a)theinput4-vectorwiththelastelementtobesizeof forperformance.AforwardpassofTTP’sneuralnetworkin
C++imposesminimaloverheadperchunk(lessthan0.3ms
| theactuallysentchunkK |     |          | i+h | ,and,(b)theactualtransmission |     |              |     |            |             |        |        |         |            |
| --------------------- | --- | -------- | --- | ----------------------------- | --- | ------------ | --- | ---------- | ----------- | ------ | ------ | ------- | ---------- |
|                       |     |          |     |                               |     |              |     | on average | on a recent | x86-64 | core). | The MPC | controller |
| time                  | T   | ofchunkK |     | as desiredoutput;             |     | the sequence | is  |            |             |        |        |         |            |
|                       | i+h |          | i+h |                               |     |              |     |            |             |        |        |         |            |
shuffledtoremovecorrelation.Itisworthnotingthatunlike optimizesoverH=5futuresteps(about10seconds).Weset
λ=1andµ=100tobalancetheconflictinggoalsinQoE.
priorwork[25,40]thatlearnedfromthroughputtraces,TTP
istraineddirectlyonrealchunk-by-chunkdata. Eachretrainingtakesabout6hoursona48-coreserver.
|     | WetraintheTTPwithstandardsupervisedlearning: |     |     |     |     |     | the |     |     |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trainingminimizesthecross-entropylossbetweentheoutput
4.6 AblationstudyofTTPfeatures
probabilitydistributionandthediscretizedactualtransmission
timeusingstochasticgradientdescent. Weperformedanablationstudytoassesstheimpactofthe
WeretraintheTTPeveryday,usingtrainingdatacollected TTP’sfeatures(Figure7). Theprediction accuracyismea-
overtheprior14days,toavoidtheeffectsofdatasetshiftand suredusingmeansquarederror(MSE)betweenthepredicted
catastrophicforgetting[33,34].Withinthe14-daywindow,we transmissiontimeandtheactual(absolute,unbinned)value.
weightmorerecentdaysmoreheavily.Theweightsfromthe FortheTTPthatoutputsaprobabilitydistribution,wecom-
previousday’smodelareloadedtowarm-starttheretraining. putetheexpectedtransmissiontimebyweightingthemedian
|     |                       |     |     |     |     |     |     | valueofeachbinwiththecorrespondingprobability. |                    |     |     |             | Here      |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | ------------------ | --- | --- | ----------- | --------- |
| 4.4 | Model-basedcontroller |     |     |     |     |     |     | arethemorenotableresults:                      |                    |     |     |             |           |
|     |                       |     |     |     |     |     |     | Use of low-level                               | congestion-control |     |     | statistics. | The TTP’s |
OurMPCcontroller(usedforMPC-HM,RobustMPC-HM,
|     |     |     |     |     |     |     |     | nature as | a DNN lets | it consider | a variety | of  | noisy inputs, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----------- | --------- | --- | ------------- |
andFugu)isastochasticoptimalcontrollerthatmaximizes
includinglow-levelcongestion-controlstatistics.Wefeedthe
theexpectedcumulativeQoEinEquation1withreplanning.It
kernel’stcp_infostructuretotheTTP,andfindthatseveral
queriesTTPforpredictionsoftransmissiontimeandoutputsa
planKs,Ks ,...,Ks of these fields contribute positively to the TTP’s accuracy,
byvalueiteration[8].Aftersending
|     | i   | i+1 | i+H−1 |     |     |     |     | especiallytheRTT,CWND,andnumberofpacketsinflight |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
Ks,thecontrollerobservesandupdatestheinputvectorpassed
|     | i   |     |     |     |     |     |     | (Figure 7). | Althoughclient-side |     | ABR | systems | cannottypi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- | --- | --- | ------- | ----------- |
intoTTP,andreplansagainforthenextchunk.
callyaccessthisstructuredirectorybecausethestatisticslive
|     | GiventhecurrentplaybackbufferlevelB |     |     |     |     | i andthelastsent |     |     |     |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
onthesender,theseresultsshouldmotivatethecommunica-
| chunkK |        | ,letv∗(B,K |         | )denotethemaximumexpected |        |        |           |                                                  |     |     |     |     |     |
| ------ | ------ | ---------- | ------- | ------------------------- | ------ | ------ | --------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|        |        | i−1        | i i i−1 |                           |        |        |           | tionofricherdatatoABRalgorithmswherevertheylive. |     |     |     |     |     |
| sum    | of QoE | that       | can be  | achieved                  | in the | H-step | lookahead |                                                  |     |     |     |     |     |
horizon.Wehavevalueiterationasfollows: Transmission-time prediction. The TTP explicitlyconsid-
(cid:110) ers the size of a proposed chunk, rather than predicting
|     | v∗(B,K |           | ∑Pr[Tˆ(Ks)=t]· |     |     |     |     |                                                    |     |     |                  |     |     |
| --- | ------ | --------- | -------------- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | ---------------- | --- | --- |
|     | i      | i−1 )=max |                |     | i   |     |     |                                                    |     |     |                  |     |     |
|     | i      |           | K s            |     | i   |     |     | throughputandthenmodelingtransmissiontimeasscaling |     |     |                  |     |     |
|     |        |           | i ti           |     |     |     |     |                                                    |     |     |                  |     |     |
|     |        |           |                |     |     |     |     | linearlywithchunksize[7,32,47].                    |     |     | WecomparedtheTTP |     |     |
(cid:111)
(QoE(K s,K )+v∗ (B ,K s)) , withanequivalentthroughputpredictorthatisagnostictothe
|     |     |     |     | i   | i−1 | i+1 i+1 | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation    501

16.45
16.4
16.35
16.3
0.2 0.18 0.16 0.14 0.12
Figure7:AblationstudyofFugu’sTransmissionTimePre-
dictor(TTP).RemovinganyoftheTTP’sinputsreducedits
abilitytopredictthetransmissiontimeofavideochunk.A
non-probabilisticTTP(“PointEstimate”)andonethatpre-
dictsthroughputwithoutregardtochunksize(“Throughput
Predictor”)bothperformedmarkedlyworse.TCPstatistics
(RTT,CWND,packetsinflight)alsoprovedhelpful.
chunk’ssize(keepingeverythingelseunchanged).TheTTP’s
predictionsweremuchmoreaccurate(Figure7).
Predictionwithuncertainty.TheTTPoutputsaprobability
distributionoftransmissiontimes.Thisallowsforbetterdeci-
sionmakingcomparedwithasinglepointestimatewithout
uncertainty. Weevaluatedtheexpectedaccuracyofaprob-
abilistic TTP vs. a point-estimate version that outputs the
median value of the most-probable bin, and found an im-
provementinpredictionaccuracywiththeformer(Figure7).
To measure the end-to-end benefits of a probabilistic TTP,
wedeployedbothversionsonPufferinAugust2019andcol-
lected39stream-daysofdata.Itperformedmuchworsethan
normal Fugu: the rebuffering ratio was 5× worse,without
significantimprovementinSSIM(datanotshown).
Useofneuralnetwork.Wefoundasignificantbenefitfrom
usingadeepneuralnetworkinthisapplication,comparedwith
alinear-regressionmodelthatwastrainedthesameway.The
lattermodelperformedmuchworseonpredictionaccuracy
(Figure7).WealsodeployeditonPufferandcollected448
stream-daysofdatainAug.–Oct.2019;itsrebufferingratio
was2.5×worse(datanotshown).
Dailyretraining.Toevaluateourpracticeofretrainingthe
TTP each day,we conducted a randomized comparison of
several“out-of-date”versionsoftheTTPonPufferbetween
Aug.7andAug.30,2019,andbetweenOct.16,2019and
Jan.2,2020.WecomparedvintagesoftheTTPthathadbeen
trainedinFebruary,March,April,andMay2019,alongside
theTTPthatisretrainedeachday. (Weemphasizethatthe
olderTTPvintageswerealsolearnedinsituontwoweeksof
datafromtheactualdeploymentenvironment—theyaresim-
plyearlierversionsofthesamepredictor.)Somewhattoour
)Bd(
MISS
egarevA
490,596 streams
10.7 stream-years
Fugu-Mar
Fugu-Feb
Fugu
Fugu-May
QoE
Fugu-Apr
Better
Time spent stalled (%)
Figure8:Fugu,whichisretrainedeveryday,didnotoutper-
formolderversionsofitselfthatweretrainedupto11months
earlier.Ourpracticeofdailyretrainingappearstobeoverkill.
surpriseanddisappointment,wewerenotabletodocument
abenefitfromdailyretraining(Figure8). Thismayreflect
a lack of dynamism in the Pufferuserbase,orthe fact that
once“enough”dataisavailabletoputthepredictorthrough
its paces,more-recent data is not necessarily beneficial,or
some other reason. We suspect the older predictors might
becomestaleatsomepointinthefuture,butforthemoment,
ourpracticeofdailyretrainingappearstobeoverkill.
5 Experimentalresults
WenowpresentfindingsfromourexperimentswiththePuffer
study, including the evaluation of Fugu. Our main results
areshowninFigure9.Insummary,weconductedaparallel-
group,blinded-assignment,randomizedcontrolledtrialoffive
ABR schemes between Jan. 26 and Aug. 7, and between
Aug.30andOct.16,2019.Thedatainclude13.1stream-years
ofdatasplitacrossfivealgorithms,countingallstreamsthat
playedatleast4secondsofvideo.Astandardizeddiagramof
theexperimentalflowisavailableintheappendix(FigureA1).
Wefoundthatsimple“buffer-based”control(BBA)per-
formssurprisinglywell,despiteitsstatusasafrequentlyout-
performedresearchbaseline.Theonlyschemetoconsistently
outperformBBAinbothstallsandqualitywasFugu,butonly
whenallfeaturesoftheTTPwereused.Ifweremovetheprob-
abilistic“fuzzy”natureofFugu’spredictions,orthe“depth”
oftheneuralnetwork,orthepredictionoftransmissiontime
asafunctionofchunksize(andnotsimplythroughput),Fugu
forfeitsitsadvantage(§4.6).Fugualsooutperformedother
schemesintermsofSSIMvariability(Figure1).Onacold
starttoanewsession,priorwork[19,40]suggestedaneed
for session clustering to determine the quality of the first
chunk.TTPprovidesanalternativeapproach:low-levelTCP
statisticsareavailableassoonasthe(HTTP/WebSocket,TLS,
TCP)connectionisestablishedandallowFugutobeginsafely
atahigherquality(Figure10).
We conclude that robustly beating “simple” algorithms
withmachinelearningmaybesurprisinglydifficult,notwith-
502 17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Primaryexperiment(637,189streams,13.1stream-years) Slownetworkpaths(126,465streams,1.8stream-years)
15
Fugu
| MPC-HM |     |     | MPC-HM | Fugu |
| ------ | --- | --- | ------ | ---- |
16.6
BBA
|                   |     | 14.5              | BBA |     |
| ----------------- | --- | ----------------- | --- | --- |
| )Bd( MISS egarevA |     | )Bd( MISS egarevA |     |     |
16.4
14
Pensieve
RobustMPC-HM
| 16.2 E  |              |      | E       |          |
| ------- | ------------ | ---- | ------- | -------- |
| Qo      |              |      | Qo      |          |
| Better  |              | 13.5 | Better  |          |
|         | RobustMPC-HM |      |         | Pensieve |
16
13
| 0.24 0.2               | 0.16 0.12 |     | 1.2 1                  | 0.8 0.6 |
| ---------------------- | --------- | --- | ---------------------- | ------- |
| Time spent stalled (%) |           |     | Time spent stalled (%) |         |
Figure9:Mainresults.Inablindedrandomizedcontrolledtrialthatincluded13.1yearsofvideostreamedto54,612clientIP
addressesoveraneight-monthperiod,Fugureducedthefractionoftimespentstalled(exceptwithrespecttoRobustMPC-HM),
increasedSSIM,andreducedSSIMvariationwithineachstream(tabulardatainFigure1).“Slow”networkpathshaveaverage
throughputlessthan6Mbit/s;followingpriorwork[25,46],thesepathsaremorelikelytorequirenontrivialbitrate-adaptation
logic.Suchstreamsaccountedfor14%ofoverallviewingtimeand83%ofstalls.Errorbarsshow95%confidenceintervals.
| 11.2 |     | 1   |     |     |
| ---- | --- | --- | --- | --- |
Fugu
)Bd( MISS knuhc-tsrfi egarevA
0.1
11 QoE
Better
FDCC
0.01
| 10.8 |     |     | Fugu (mean 33.6 ± 0.9) |     |
| ---- | --- | --- | ---------------------- | --- |
Pensieve
MPC-HM (mean 30.8 ± 0.8)
0.001
|     | MPC-HM |     | RobustMPC-HM (mean 31.0 ± 0.8) |     |
| --- | ------ | --- | ------------------------------ | --- |
Pensieve (mean 31.6 ± 0.8)
10.6 BBA
|                   | RobustMPC-HM |           | BBA (mean 32.1 ± 0.8)                |      |
| ----------------- | ------------ | --------- | ------------------------------------ | ---- |
| 0.44              | 0.43 0.42    | 0.0001 10 | 100                                  | 1000 |
| Startup delay (s) |              |           | Total time on video player (minutes) |      |
Figure10:Onacoldstart,Fugu’sabilitytobootstrapABR Figure11:UsersrandomlyassignedtoFuguchosetoremain
decisionsfromTCPstatistics(e.g.,RTT)boostsinitialquality. onthePuffervideoplayerabout5%–9%longer,onaverage,
thanthoseassignedtootherschemes.Userswereblindedto
theassignment.Legendshows95%confidenceintervalson
standingpromisingresultsincontainedenvironmentssuchas theaveragetime-on-siteinminutes.
simulatorsandemulators.Thegainsthatlearnedalgorithms
haveinoptimizationorsmarterdecisionmakingmaycomeat
atradeoffinbrittlenessorsensitivitytoheavy-tailedbehavior. industryandmightbeincreasedbydeliveringbetter-quality
videowithfewerstalls,butwesimplydonotknowenough
aboutwhatisdrivingthisphenomenon.
5.1 Fuguusersstreamedforlonger
Weobservedsignificantdifferencesinthesessiondurations 5.2 Thebenefitsoflearninginsitu
ofusersacrossalgorithms(Figure11).Userswhosesessions
wereassignedtoFuguchosetoremainonthePuffervideo EachoftheABRalgorithmswedeployedhasbeenevaluated
playerabout5–9%longer,onaverage,thanthoseassignedto in emulation in priorwork [25,46]. Notably,the results in
otherschemes.Userswereblindedtotheassignment,andwe thoseworksarequalitativelydifferentfromsomeofthereal
believetheexperimentwascarefullyexecutednotto“leak” worldresultswehaveseenhere—forexample,buffer-based
detailsoftheunderlyingscheme(MPCandFuguevenshare controlmatchingoroutperformingMPC-HMandPensieve.
mostoftheircodebase).Theaveragedifferencewasdriven To investigate this further,we constructed an emulation
solelybytheupper4%tailofviewershipduration(sessions environmentsimilartothatusedin[25].Thisinvolvedrun-
lasting more than 3 hours)—viewers assigned to Fugu are ningthePuffermediaserverlocally,andlaunchingheadless
muchmorelikelytokeepstreamingbeyondthispoint,even Chrome clients inside mahimahi [30] shells to connect to
asthedistributionsarenearlyidenticaluntilthen. theserver.Eachmahimahishellimposeda40msend-to-end
Time-on-site is a figure of merit in the video-streaming delayontrafficoriginatinginsideitandlimitedthedownlink
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation    503

| 15     |     |     |      | 17                |     |        |          |     | 1.0 |     |     |     |     |
| ------ | --- | --- | ---- | ----------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
| MPC-HM |     |     | Fugu |                   |     |        |          |     |     |     |     |     |     |
|        |     |     |      | 44,326 streams    |     |        | Fugu     |     |     |     |     |     |     |
|        |     |     |      | 0.9 stream-years  |     | MPC-HM |          |     |     |     |     |     |     |
| 14.5   |     | BBA |      |                   |     |        | BBA      |     |     |     |     |     |     |
|        |     |     |      | 16.5              |     |        |          |     | 0.8 |     |     |     |     |
|        |     |     |      | )Bd( MISS egarevA |     |        | Pensieve |     |     |     |     |     |     |
)Bd( MISS egarevA
| 14      |     |              |     |      |                        |              |     |     | 0.6 |     |     |               |     |
| ------- | --- | ------------ | --- | ---- | ---------------------- | ------------ | --- | --- | --- | --- | --- | ------------- | --- |
|         |     |              |     | 16   | QoE                    | RobustMPC-HM |     |     | FDC |     |     |               |     |
|         |     | RobustMPC-HM |     |      | Better                 |              |     |     |     |     |     |               |     |
| 13.5    | QoE |              |     |      |                        |              |     |     | 0.4 |     |     |               |     |
| Better  |     |              |     | 15.5 |                        |              |     |     |     |     |     |               |     |
| 13      |     |              |     |      |                        |              |     |     | 0.2 |     |     |               |     |
|         |     |              |     |      | Emulation-trained Fugu |              |     |     |     |     |     | Puffer traces |     |
|         |     | Pensieve     |     |      |                        |              |     |     |     |     |     | FCC traces    |     |
15
| 12.5 |             |          |     |     |         |     |         |     | 0.0 |     |      |     |     |
| ---- | ----------- | -------- | --- | --- | ------- | --- | ------- | --- | --- | --- | ---- | --- | --- |
| 1.5  | 1.25 1 0.75 | 0.5 0.25 | 0   |     | 0.5 0.4 | 0.3 | 0.2 0.1 |     | 0.1 |     | 1 10 | 100 |     |
Time spent stalled (%) Time spent stalled (%) Throughput (Mbps)
Figure12:Left:performanceinemulation,runinmahimahi[30]usingtheFCCtraces[10],followingthemethodofPen-
sieve[25].Middle:DuringJan.26–Apr.2,2019,werandomizedsessionstoasetofalgorithmsincluding“emulation-trained
Fugu.”ForFugu,traininginemulationdidnotgeneralizetothedeploymentenvironment.Inaddition,emulationresults(left)are
notindicativeofreal-worldperformance.Right:comparisonofthroughputdistributionofFCCtracesandofrealPuffersessions.
capacity over time to match the capacity recorded in a set behaviorsaswellasuserbehaviors,suchaswatchduration).
ofFCCbroadbandnetworktraces[10].AsinthePensieve Reinforcement learning (RL) schemes such as Pensieve
evaluation,uplinkspeedsinallshellswerecappedat12Mbps.
maybeataparticulardisadvantagefromthisphenomenon.
Withinthistestsetup,weautomated12clientstorepeatedly
Unlikesupervisedlearningschemesthatcanlearnfromtrain-
connecttothemediaserver,whichwouldplaya10minute ing“data,”RLtypicallyrequiresatrainingenvironment to
cliprecordedonNBCovereachnetworktraceinthedataset.
|     |     |     |     |     |     |     | respond | to a sequence |     | of control | decisions | and | decide on |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ---------- | --------- | --- | --------- |
EachclientwasassignedtoadifferentABRalgorithm,and theappropriateconsequencesandreward.Thatenvironment
| played the | 10 minute | video repeatedly |     | over more | than | 15  |     |     |     |     |     |     |     |
| ---------- | --------- | ---------------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
couldbereallifeinsteadofasimulator,butthelevelofsta-
hoursofFCCtraces.ResultsareshowninFigure12.
|     |     |     |     |     |     |     | tisticalnoise | we  | observe | wouldmake | this | type | oflearning |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --------- | ---- | ---- | ---------- |
We trained a version of Fugu in this emulation environ- extremelysloworrequireanextremelybroaddeploymentof
menttoevaluateitsperformance.Comparedwiththeinsitu
algorithmsintraining.RLreliesonbeingabletoslightlyvary
Fugu—orwitheveryotherABRscheme—thereal-worldper-
acontrolactionanddetectachangeintheresultingreward.
formanceofemulation-trainedFuguwashorrible(Figure12,
|                |         |       |          |                |     |     | By ourcalculations,the |     |     | variability | ofinputs | is  | suchthatit |
| -------------- | ------- | ----- | -------- | -------------- | --- | --- | ---------------------- | --- | --- | ----------- | -------- | --- | ---------- |
| middle panel). | Looking | atthe | otherABR | schemes,almost |     |     |                        |     |     |             |          |     |            |
takesabout2stream-yearsofdatatoreliablydistinguishtwo
eachofthem lies somewhere along the SSIM/stallfrontier ABR schemes whose innate “true” performance differs by
inemulation(leftsideoffigure),withPensieverebuffering
15%.TomakeRLpractical,futureworkmayneedtoexplore
theleastandMPCdeliveringthehighestqualityvideo.Inthe
techniquestoreducethisvariability[26]orconstructmore
realexperiment(middleoffigure),weseeamoremuddled
faithfulsimulatorsandemulatorsthatmodeltailbehaviors
picture,withadifferentqualitativearrangementofschemes.
andcaptureadditionaldynamicsoftherealInternetthatare
notrepresentedinthroughputtraces(e.g.varyingRTT,cross
5.3 RemarksonPensieveandRLforABR traffic,interactionbetweenthroughputandchunksize[7]).
Second,mostoftheevaluationofPensieveintheoriginal
TheoriginalPensievepaper[25]demonstratedthatPensieve
|     |     |     |     |     |     |     | paper focused |     | on training | and | evaluating | Pensieve | using a |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ---------- | -------- | ------- |
outperformedMPC-HM,RobustMPC-HM,andBBAinboth
emulation-based tests and in video streaming tests on low singletestvideo.Asaresult,thestatespacethatmodelhad
|     |     |     |     |     |     |     | to explore | was | inherently | more | limited. | Evaluation | of the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ---- | -------- | ---------- | ------ |
andhigh-speedreal-worldnetworks.Ourresultsdiffer;we
Pensieve“multi-videomodel”—whichwehavetouseforour
believethemismatchmayhaveoccurredforseveralreasons.
experimentalsetting—wasmorelimited.Ourresultsaremore
| First, we | have found | that simulation-based |     | training | and |     |     |     |     |     |     |     |     |
| --------- | ---------- | --------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consistentwitharecentlarge-scalestudyofaPensieve-multi-
| testing do | not capture | the vagaries | of the | real-world | paths |     |     |     |     |     |     |     |     |
| ---------- | ----------- | ------------ | ------ | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
seeninthePufferstudy.Unlikereal-worldrandomizedtrials, video-likeschemeon30millionstreamsatFacebook[24].
trace-basedemulatorsandsimulatorsallowexperimentersto Third,therightsideofFigure12showsthatthedistribution
limitstatisticaluncertaintybyrunningdifferentalgorithms ofthroughputsintheFCCtracesdiffersmarkedlyfromthose
onthesameconditions,eliminatingtheeffectoftheplayof on Puffer. This datasetshiftcouldhave harmedthe perfor-
chanceingivingdifferentalgorithmsadifferentdistribution manceofPensieve,whichwastrainedontheFCCtraces.In
ofwatchtimes,networkbehaviors,etc.However,itisdifficult responsetoreviewerfeedback,wetrainedaversionofPen-
to characterize the systematic uncertainty that comes from sieveonthroughputtracesrandomlysampledfromrealPuffer
selectingasetoftracesthatmayomitthevariabilityorheavy- video sessions. This is essentiallyas close to a “learnedin
tailednatureofarealdeploymentexperience(bothnetwork situ”versionofPensieveaswethinkwecanachieve,butis
504    17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

Allsessions
16.6
16.5
16.4
16.3
0.6 0.45 0.3 0.15
)Bd(
MISS
egarevA
Slownetworkpaths(<6Mbit/s)
244,028 streams
3.8 stream-years BBA Fugu 14.5
14
Pensieve Pensieve (Puffer traces)
13.5
QoE
Better
13
5 4 3 2 1
Time spent stalled (%)
)Bd(
MISS
egarevA
33,817 streams BBA
0.5 stream-years Fugu
QoE
Better
Pensieve Pensieve (Puffer traces)
Time spent stalled (%)
Figure13:DuringJan.2–Feb.2,2020,weevaluatedaversionofPensievethatwastrainedonacollectionofnetworktraces
drawnrandomlyfromactualPuffersessions.ThisimproveditsperformancecomparedwiththeoriginalPensieve,buttheoverall
resultswerebroadlysimilar.
notquitethesame(§5.3).Wecompared“PensieveonPuffer experimentalfindingsoutsidetherealworld—arealworld
traces”withtheoriginalPensieve,BBA,andFugubetween whose behavior is noisy and takes lots of time to measure
Jan.2andFeb.2,2020(Figure13).Theresultswerebroadly precisely. Thatmaybeanunsatisfyingconclusion,andwe
similar;thenewPensieveachievedbetterperformance,but doubtitwillbethefinalwordonthistopic.Perhapsitwill
wasstillsignificantlyworsethanBBAandFugu.Theresults becomepossibletomodelenoughofthevagariesofthereal
deservefurtherstudy;theysuggestthattherepresentativeness Internet“insilico”toenablethedevelopmentofrobustcontrol
oftrainingdataisnottheendofthestorywhenitcomestothe strategieswithoutextensivereal-worldexperiments.
real-worldperformanceofRLschemestrainedinsimulation. ItisalsounknowntowhatdegreePuffer’sresults—which
Finally,PensieveoptimizesaQoEmetriccenteredaround areaboutasingleserverinauniversitydatacenter,sendingto
bitrate as a proxy for video quality. We did not alter this clientsacrossourentirecountryoverthewide-areaInternet—
and leave the discussion to Section 6. Figure 4 shows that generalizetoadifferentserveratadifferentinstitution,much
Pensievewasthe#2schemeintermsofbitrate(belowBBA) lessthemoretypicalpathsbetweenauseronanaccessnet-
intheprimaryanalysis.Weemphasizethatourfindingsdo workandtheirnearestCDNedgenode.Wedon’tknowfor
notindicatethatPensievecannotbeausefulABRalgorithm, sureifthepre-trainedFugumodelwouldworkinadifferent
especiallyinascenariowheresimilar,pre-recordedvideois location,orwhethertraininganewFugubasedondatafrom
playedoverafamiliarsetofknownnetworks. thatlocationwouldyieldcomparableresults.Ourresultsshow
thatlearninginsituworks,butwedon’tknowhowspecific
6 Limitations thesitusneedstobe.AndwhileweexpectthatFugucouldbe
implementedinthecontextofclient-sideABR(especiallyif
ThedesignofthePufferexperimentandtheFugusystemare
theserveriswillingtoshareitstcp_infostatisticswiththe
subjecttoimportantlimitationsthatmayaffecttheirperfor- client),wehaven’tdemonstratedthis.
manceandgeneralizability. Althoughwebelievethatpastresearchpapersmayhave
underestimatedtheuncertaintiesinreal-worldmeasurements
withrealisticInternetpathsandusers,wealsomaybeguilty
6.1 Limitationsoftheexperiments
ofunderestimatingourownuncertaintiesoremphasizingun-
Our randomized controlled trial represents a rigorous, but certainties that are only relevant to small ormedium-sized
necessarily“blackbox,”studyofABRalgorithmsforvideo academicstudies,suchasours,andirrelevanttotheindustry.
streaming. We don’tknowthe true distribution ofnetwork ThecurrentloadonPufferisabout60concurrentstreamson
pathsandthroughput-generatingprocesses;wedon’tknow average,meaningwecollectabout60stream-daysofdataper
theparticipantsorwhythedistributioninwatchtimesdiffers day.Ourprimaryanalysiscoversabout2.6stream-yearsof
byassignedalgorithm;wedon’tknowhowtoemulatethese dataperschemecollectedoveraneight-monthperiod,andwas
behaviorsaccuratelyinacontrolledenvironment. sufficienttomeasureitsperformancemetricstowithinabout
Wehavesupplementedthisblack-boxworkwithablation ±15%(95%CI).Bycontrast,weunderstandYouTubehas
analysestorelatethereal-worldperformanceofFugutothe anaverageloadofmorethan60millionconcurrentstreams
l2accuracyofitspredictor,andhavestudiedvariousablated atanygiventime.Weimaginetheconsiderationsofconduct-
versions of Fugu in deployment. However,ultimately part ingdata-drivenexperimentsatthislevelmaybecompletely
of the reason forthis paperis that we cannot replicate the different—perhapslessaboutstatisticaluncertainty,andmore
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation 505

aboutsystematicuncertaintiesandthedifficultiesofrunning thewildInternet,withitsvariabilityandheavy-taileddistri-
experimentsandaccumulatingsomuchdata. butions. Itremainsachallengingproblemtogathertheap-
Some of Fugu’s performance (and that of MPC, Ro- propriatetrainingdata(orinthecaseofRLsystems,training
bustMPC,andBBA)relativetoPensievemaybeduetothe environments)toproperlylearnandvalidatesuchsystems.
fact that these four schemes received more information as Inthispaper,weasked:whatdoesittaketocreatealearned
theyran—namely,theSSIMofeachpossibleversionofeach ABRalgorithmthatrobustlyperformswelloverthewildInter-
futurechunk—thandidPensieve.Itispossiblethatan“SSIM- net?Ineffect,ourbestansweristocheat:trainthealgorithm
aware”Pensievemightperformbetter.Theloadofcalculating insituondatafromtherealdeploymentenvironment,anduse
SSIMforeachencodedchunkisnotinsignificant—aboutan analgorithmwhosestructureissophisticatedenough(aneural
extra40%ontopofencodingthevideo. network)andyetalsosimpleenough(apredictoramenableto
supervisedlearningondata,informingaclassicalcontroller)
tobenefitfromthatkindoftraining.
6.2 LimitationsofFugu
Overthelastyear,wehavestreamed38.6yearsofvideo
to63,508usersacrosstheInternet.Sessionsarerandomized
Thereisasensethatdata-drivenalgorithmsthatmore“heav-
in blinded fashion among algorithms,and client telemetry
ily”squeezeoutperformancegainsmayalsoputthemselves
is recorded for analysis. The Fugu algorithm robustly out-
atrisktobrittlenesswhenadeploymentenvironmentdrifts
performedotherschemes,bothsimpleandsophisticated,on
fromonewherethealgorithmwastrained.Inthatsense,itis
objectivemeasures(SSIM,stalltime,SSIMvariability)and
hardtosaywhetherFugu’sperformancemightdecaycatas-
increasedthedurationthatuserschosetocontinuestreaming.
trophicallysomeday. Wetriedandfailedtodemonstratea
WehavefoundthePufferapproachapowerfultoolfornet-
quantitativebenefitfromdailyretrainingover“out-of-date”
workingresearch—itisfulfillingtobeableto“measure,then
vintages,butatthesametime,wecannotbesurethatsome
build”[5]toiteraterapidlyonnewideasandgainfeedback.
surprisingdetailtomorrow—e.g.,anewuserfromanunfa-
Accordingly,weareopeningPufferasan“openresearch”plat-
miliarnetwork—won’tsendFuguintoatailspinbeforeitcan
form.Alongwiththispaper,wearepublishingourfullarchive
beretrained.Ayearofdataonagrowinguserbasesuggests,
ofdataandresultsonthePufferwebsite.Thesystemposts
butdoesn’tguarantee,robustnesstoachangingenvironment.
newdataeachweek,alongwithasummaryofresultsfrom
Fugudoesnotconsiderseveralissuesthatotherresearch
theongoingexperiments,withconfidenceintervalssimilarto
has concerned itself with—e.g., being able to “replace”
thoseinthispaper.(TheformatisdescribedinAppendixB.)
already-downloadedchunksinthebufferwithhigherquality
Weredactedsomefieldsfromthepublicarchivetoprotect
versions[38],oroptimizingthejointQoEofmultipleclients
participants’privacy(e.g.,IPaddress)butarewillingtowork
whoshareacongestionbottleneck[29].
withresearchers on access to these fields in an aggregated
FuguisnottiedastightlytotheTCPorcongestioncontrol
fashion.PufferandFuguarealsoopen-sourcesoftware,as
asitmightbe—forexample,Fugucouldwaittosendachunk
aretheanalysistoolsusedtopreparetheresultsinthispaper.
untiltheTCPsendertellsitthatthereisasufficientcongestion
We plan to operate Puffer as long as feasible and invite
windowformostofthechunk(orthewholechunk)tobesent
researchers to train and validate new algorithms for ABR
immediately. Otherwise,itmight choose to waitandmake
control,networkandthroughputprediction,andcongestion
abetter-informeddecisionlater.Fugudoesnotschedulethe
control on its traffic. We are eagerto collaborate with and
transmissionofchunks—itwillalwayssendthenextchunk
learnfromthecommunity’sideasonhowtodesignanddeploy
aslongastheclienthasroominitsplaybackbuffer.
robustlearnedsystemsfortheInternet.
7 Conclusion Acknowledgments
Machine-learnedsystemsincomputernetworkingsometimes We are greatly indebted to Emily Marx, who joined this
describethemselvesasachievingnear-“optimal”performance, projectaftertheoriginalsubmissionofthispaper,foundand
based on results in a contained or modeled version of the correctedbugsinouranalysistools,andperformedthefinal
problem[25,37,39].Suchapproachesarenotlimitedtothe dataanalysis. Wethankourshepherd,VyasSekar,andthe
academiccommunity:inearly2020,amajorvideo-streaming ACM SIGCOMM and USENIX NSDI reviewers for their
company announced a $5,000 prize for the best low-delay helpfulfeedback.Wearegratefulforconversationswithand
ABRscheme,inwhichcandidateswillbeevaluatedinanet- feedbackfromDanfeiXu,T.Y.Huang,HongziMao,Michael
worksimulatorthatfollowsatraceofvaryingthroughput[2]. Schapira,andNilsKrahnstoever,andwethanktheparticipants
Inthispaper,wesuggestthattheseeffortscanbenefitfrom inthePufferresearchstudy,withoutwhomtheseexperiments
consideringabroadernotionofperformanceandoptimality. couldnothavebeenconducted.Thisworkwassupportedby
Good,orevennear-optimal,performanceinasimulatoror NSFgrantCNS-1909212andbyGoogle,Huawei,VMware,
emulatordoesnotnecessarilypredictgoodperformanceover Dropbox,Facebook,andtheStanfordPlatformLab.
506 17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

References [13] Gabriel Dulac-Arnold, Daniel Mankowitz, and Todd
Hester. Challengesofreal-worldreinforcementlearning.
| [1] Locast: | Non-profitretransmission |     |     | ofbroadcasttelevi- |     |     |     |     |     |
| ----------- | ------------------------ | --- | --- | ------------------ | --- | --- | --- | --- | --- |
InICML2019WorkshopRL4RealLife,2019.
| sion,June | 2018. | https://news.locast.org/app/uploads/ |     |     |     |     |     |     |     |
| --------- | ----- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
2018/11/Locast-White-Paper.pdf. [14] BradleyEfronandRobertTibshirani.Bootstrapmethods
forstandarderrors,confidenceintervals,andothermea-
[2] MMSys’20/TwitchGrandChallengeonAdaptationAl- suresofstatisticalaccuracy. Statisticalscience,pages
| gorithmsforNear-SecondLatency,January2020. |     |     |     |     | https: |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
54–75,1986.
//2020.acmmmsys.org/lll_challenge.php.
|     |     |     |     |     | [15] | SallyFloydandEddieKohler. |     | Internetresearchneeds |     |
| --- | --- | --- | --- | --- | ---- | ------------------------- | --- | --------------------- | --- |
[3] AlekhAgarwal,NanJiang,andShamM.Kakade. Lec- bettermodels. ACMSIGCOMMComputerCommuni-
turenotesonthetheoryofreinforcementlearning. 2019. cationReview,33(1):29–34,2003.
[4] Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, [16] SallyFloydandVernPaxson. Difficultiesinsimulating
SanjayRao,JessicaChen,EthanKatz-Bassett,Bruno theinternet. IEEE/ACMTransactionsonNetworking,
Ribeiro, Jibin Zhan, and Hui Zhang. Oboe: Auto- 9(4):392–403,2001.
| tuning video | ABR | algorithms | to  | network conditions. |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ------------------- | --- | --- | --- | --- | --- |
[17] SadjadFouladi,JohnEmmons,EmreOrbay,Catherine
InProceedingsofthe2018ConferenceoftheACMSIG-
|     |     |     |     |     |     | Wu,RiadS.Wahby,andKeithWinstein. |     | Salsify:Low- |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | ------------ | --- |
COMM,pages44–58,2018.
|     |     |     |     |     |     | latency network | video through | tighter integration | be- |
| --- | --- | --- | --- | --- | --- | --------------- | ------------- | ------------------- | --- |
[5] RemziArpaci-Dusseau. Measure,thenbuild(USENIX tweenavideocodecandatransportprotocol. In15th
ATC2019keynote). Renton,WA,July2019.USENIX USENIXSymposiumonNetworkedSystemsDesignand
| Association. |     |     |     |     |     | Implementation(NSDI18),pages267–282,2018. |     |     |     |
| ------------ | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
[6] AthulaBalachandran,VyasSekar,AdityaAkella,Srini- [18] Te-Yuan Huang, Ramesh Johari, Nick McKeown,
vasanSeshan,IonStoica,andHuiZhang. Developing MatthewTrunnell,andMarkWatson. Abuffer-based
a predictive model of quality of experience for Inter- approachtorateadaptation:Evidencefromalargevideo
netvideo. ACMSIGCOMMComputerCommunication streamingservice. InProceedingsofthe2014Confer-
enceoftheACMSIGCOMM,pages187–198,2014.
Review,43(4):339–350,2013.
[19] JunchenJiang,VyasSekar,HenryMilner,DavisShep-
[7] MihovilBartulovic,JunchenJiang,SivaramanBalakr-
ishnan,VyasSekar,andBrunoSinopoli. Biasesindata- herd, Ion Stoica, and Hui Zhang. CFA: A practical
drivennetworking,andwhattodoaboutthem. InPro- predictionsystemforvideoQoEoptimization. In13th
USENIXSymposiumonNetworkedSystemsDesignand
ceedingsofthe16thACMWorkshoponHotTopicsin
Networks,pages192–198,2017. Implementation(NSDI16),pages137–150,2016.
[8] RichardBellman. AMarkoviandecisionprocess. Jour- [20] JunchenJiang,VyasSekar,andHuiZhang. Improving
fairness,efficiency,andstabilityinHTTP-basedadap-
| nal of mathematics |     | and | mechanics, | pages | 679–684, |                                  |                        |                |      |
| ------------------ | --- | --- | ---------- | ----- | -------- | -------------------------------- | ---------------------- | -------------- | ---- |
| 1957.              |     |     |            |       |          | tive video                       | streaming withFESTIVE. | In Proceedings |      |
|                    |     |     |            |       |          | ofthe 8thInternationalConference |                        | on emerging    | Net- |
[9] Neal Cardwell, Yuchung Cheng, C. Stephen Gunn, workingEXperimentsandTechnologies,pages97–108,
| Soheil | Hassas Yeganeh, |     | and Van | Jacobson. | BBR: |     |     |     |     |
| ------ | --------------- | --- | ------- | --------- | ---- | --- | --- | --- | --- |
2012.
| Congestion-based |     | congestion | control. | ACM | Queue, |     |     |     |     |
| ---------------- | --- | ---------- | -------- | --- | ------ | --- | --- | --- | --- |
14(5):20–53,2016. [21] S. Shunmuga Krishnan and Ramesh K. Sitaraman.
Videostreamqualityimpactsviewerbehavior:Inferring
[10] Federal Communications Commission. Measuring causalityusingquasi-experimentaldesigns. IEEE/ACM
Broadband America. https://www.fcc.gov/general/ TransactionsonNetworking,21(6):2001–2014,2013.
measuring-broadband-america.
[22] AdamLangley,AlistairRiddoch,AlyssaWilk,Antonio
[11] Paul Crews and Hudson Ayers. CS 244 ’18: Vicente,CharlesKrasic,DanZhang,FanYang,Fedor
| Recreating | and | extending | Pensieve, | 2018. | https: |           |                      |             |         |
| ---------- | --- | --------- | --------- | ----- | ------ | --------- | -------------------- | ----------- | ------- |
|            |     |           |           |       |        | Kouranov, | Ian Swett, Janardhan | Iyengar, et | al. The |
//reproducingnetworkresearch.wordpress.com/2018/ QUICtransportprotocol:DesignandInternet-scalede-
07/16/cs-244-18-recreating-and-extending-pensieve/. ployment. InProceedingsofthe2017Conferenceofthe
ACMSIGCOMM,pages183–196,2017.
| [12] Zhengfang | Duanmu, | Kai | Zeng, | Kede Ma, | Abdul |     |     |     |     |
| -------------- | ------- | --- | ----- | -------- | ----- | --- | --- | --- | --- |
Rehman,andZhouWang.Aquality-of-experienceindex [23] Zhi Li,Xiaoqing Zhu,Joshua Gahm,Rong Pan,Hao
forstreamingvideo. IEEEJournalofSelectedTopicsin Hu,Ali C. Begen,andDavidOran. Probe andadapt:
SignalProcessing,11(1):154–166,2016. Rate adaptation for HTTP video streaming at scale.
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation    507

IEEE Journal on Selected Areas in Communications, [33] AnthonyRobins. Catastrophicforgetting,rehearsaland
32(4):719–733,2014. pseudorehearsal. Connection Science,7(2):123–146,
1995.
| [24] Hongzi | Mao,Shannon |     | Chen,Drew |     | Dimmery,Shaun |     |     |     |     |     |     |
| ----------- | ----------- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Singh,DrewBlaisdell,YuandongTian,MohammadAl- [34] StéphaneRoss,GeoffreyGordon,andDrewBagnell. A
| izadeh,andEytanBakshy. |     |     | Real-worldvideoadaptation |     |     |     |           |              |          |                |         |
| ---------------------- | --- | --- | ------------------------- | --- | --- | --- | --------- | ------------ | -------- | -------------- | ------- |
|                        |     |     |                           |     |     |     | reduction | of imitation | learning | and structured | predic- |
withreinforcementlearning. InICML2019Workshop tion to no-regret online learning. In Proceedings of
RL4RealLife,2019. the Fourteenth International Conference on Artificial
IntelligenceandStatistics,pages627–635,2011.
[25] HongziMao,RaviNetravali,andMohammadAlizadeh.
Neural adaptive video streaming with Pensieve. In [35] KennethF.Schulz,DouglasG.Altman,andDavidMo-
Proceedingsofthe2017ConferenceoftheACMSIG-
|     |     |     |     |     |     |     | her. CONSORT |     | 2010 statement: | updated | guidelines |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | ------- | ---------- |
COMM,pages197–210.ACM,2017. for reporting parallel group randomised trials. BMC
medicine,8(1):18,2010.
[26] HongziMao,ShaileshhBojjaVenkatakrishnan,Malte
| Schwarzkopf,andMohammadAlizadeh. |     |     |     |     | Variancere- |      |                                       |     |     |     |         |
| -------------------------------- | --- | --- | --- | --- | ----------- | ---- | ------------------------------------- | --- | --- | --- | ------- |
|                                  |     |     |     |     |             | [36] | AlexanderT.SchwarmandMichaelNikolaou. |     |     |     | Chance- |
ductionforreinforcementlearningininput-drivenen-
|             |                                     |     |     |     |     |     | constrainedmodelpredictivecontrol. |     |     | AIChEJournal, |     |
| ----------- | ----------------------------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | ------------- | --- |
| vironments. | InInternationalConferenceonLearning |     |     |     |     |     |                                    |     |     |               |     |
45(8):1743–1752,1999.
Representations,2019.
[37] AnirudhSivaraman,KeithWinstein,PratikshaThaker,
[27] RickyK.P.Mok,XiapuLuo,EdmondW.W.Chan,and
|         |                                        |        |        |             |     |      | andHariBalakrishnan. |               | Anexperimentalstudyofthe |                |       |
| ------- | -------------------------------------- | ------ | ------ | ----------- | --- | ---- | -------------------- | ------------- | ------------------------ | -------------- | ----- |
| Rocky   | K.C.                                   | Chang. | QDASH: | a QoE-aware |     | DASH |                      |               |                          |                |       |
|         |                                        |        |        |             |     |      | learnability         | of congestion | control.                 | In Proceedings | of    |
| system. | InProceedingsofthe3rdMultimediaSystems |        |        |             |     |      |                      |               |                          |                |       |
|         |                                        |        |        |             |     |      | the 2014             | Conference    | of the                   | ACM SIGCOMM,   | pages |
Conference,pages11–22,2012.
479–490,2014.
[28] DynamicadaptivestreamingoverHTTP(DASH)—Part
[38] KevinSpiteri,RameshSitaraman,andDanielSparacio.
1:Mediapresentationdescriptionandsegmentformats,
Fromtheorytopractice:Improvingbitrateadaptation
| April2012. | ISO/IEC23009-1(http://standards.iso.org/ |     |     |     |     |     |             |           |         |                |       |
| ---------- | ---------------------------------------- | --- | --- | --- | --- | --- | ----------- | --------- | ------- | -------------- | ----- |
|            |                                          |     |     |     |     |     | in the DASH | reference | player. | In Proceedings | ofthe |
ittf/PubliclyAvailableStandards).
9thACMMultimediaSystemsConference,MMSys’18,
pages123–137,NewYork,NY,USA,2018.ACM.
[29] VikramNathan,VibhaalakshmiSivaraman,Ravichan-
draAddanki,MehrdadKhani,PrateeshGoyal,andMo-
[39] KevinSpiteri,RahulUrgaonkar,andRameshK.Sitara-
| hammadAlizadeh. |     | End-to-endtransportforvideoqoe |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
man. BOLA:Near-optimalbitrateadaptationforonline
| fairness. | In Proceedings |     | ofthe | ACM | SpecialInterest |     |     |     |     |     |     |
| --------- | -------------- | --- | ----- | --- | --------------- | --- | --- | --- | --- | --- | --- |
GrouponDataCommunication,SIGCOMM’19,page videos. InINFOCOM2016-The35thAnnualIEEEIn-
ternationalConferenceonComputerCommunications,
408–423,NewYork,NY,USA,2019.Associationfor
IEEE,pages1–9.IEEE,2016.
ComputingMachinery.
[40] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,Fuyuan
| [30] Ravi | Netravali, | Anirudh |     | Sivaraman, | Somak | Das, |     |     |     |     |     |
| --------- | ---------- | ------- | --- | ---------- | ----- | ---- | --- | --- | --- | --- | --- |
Ameesh Goyal, Keith Winstein, James Mickens, and Lin,NanshuWang,TaoLiu,andBrunoSinopoli. CS2P:
Hari Balakrishnan. Mahimahi: Accurate record-and- Improvingvideobitrateselectionandadaptationwith
|                |     |                             |     |     |     |     | data-driven | throughputprediction. |     | In Proceedings | of  |
| -------------- | --- | --------------------------- | --- | --- | --- | --- | ----------- | --------------------- | --- | -------------- | --- |
| replayforHTTP. |     | In2015USENIXAnnualTechnical |     |     |     |     |             |                       |     |                |     |
Conference(USENIXATC15),pages417–429,2015. the 2016 Conference of the ACM SIGCOMM, pages
272–285,2016.
| [31] Vern | Paxson | and Sally | Floyd. | Why | we don’t | know |     |     |     |     |     |
| --------- | ------ | --------- | ------ | --- | -------- | ---- | --- | --- | --- | --- | --- |
how to simulate the Internet. In Proceedings of the [41] Cisco Systems. Cisco Visual Networking Index:
29thconferenceonWintersimulation,pages1037–1044, Forecast and trends, 2017–2022, November 2018.
https://www.cisco.com/c/en/us/solutions/collateral/
1997.
service-provider/visual-networking-index-vni/
[32] Yanyuan Qin, Shuai Hao, Krishna R. Pattipati, Feng white-paper-c11-741490.pdf.
Qian,SubhabrataSen,BingWang,andChaoqunYue.
ABRstreamingofVBR-encodedvideos:characteriza- [42] GuibinTianandYongLiu. Towardsagileandsmooth
tion,challenges,andsolutions. InProceedingsofthe videoadaptationindynamicHTTPstreaming. InPro-
14thInternationalConferenceonemergingNetworking ceedingsofthe8thInternationalConferenceonemerg-
EXperimentsandTechnologies,pages366–378.ACM, ingNetworkingEXperimentsandTechnologies,pages
| 2018. |     |     |     |     |     |     | 109–120,2012. |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
508    17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

[43] Zhou Wang, Alan C. Bovik, Hamid R. Sheikh, and
Eero P. Simoncelli. Image quality assessment: from
errorvisibilitytostructuralsimilarity. IEEETransac-
tionsonImageProcessing,13(4):600–612,2004.
[44] KeithWinsteinandHariBalakrishnan.TCPexMachina:
Computer-generatedcongestioncontrol. Proceedingsof
the2013ConferenceoftheACMSIGCOMM,43(4):123–
134,2013.
[45] FrancisY.Yan,JestinMa,GregD.Hill,DeeptiRagha-
van,RiadS.Wahby,PhilipLevis,andKeithWinstein.
Pantheon:thetraininggroundforInternetcongestion-
controlresearch. In 2018 USENIX AnnualTechnical
Conference(USENIXATC18),pages731–743,Boston,
MA,2018.USENIXAssociation.
[46] Xiaoqi Yin,Abhishek Jindal,Vyas Sekar,and Bruno
Sinopoli. A control-theoretic approach for dynamic
adaptivevideostreamingoverHTTP. InProceedings
ofthe2015ConferenceoftheACMSIGCOMM,pages
325–338,2015.
[47] TongZhang,FengyuanRen,WenxueCheng,Xiaohui
Luo, Ran Shu, and Xiaolan Liu. Modeling and ana-
lyzingtheinfluenceofchunksizevariationonbitrate
adaptationinDASH. InIEEEINFOCOM2017-IEEE
ConferenceonComputerCommunications,pages1–9.
IEEE,2017.
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation 509

dna,9102,7.guA–62.naJdoirepehtgniruddeniatbo,)9dna1serugiF(stluseryramirpehtrofwofllatnemirepxefo]53[margaidelyts-TROSNOC:1AerugiF gnignahctub,noisseswenastratsgnidaoleR”.smaerts“ynamniatnocyamdnareyalpoedivreffuPehtottisivenostneserper”noisses“A.9102,61.tcO–03.guA
s4 naht ssel emit hctaw dah 900,761 ◦ redoced oediv wols a morf dellats 53 ◦ deredisnoc erew smaerts 878,421
|     | dengissa erew snoisses 452,94 dedulcxe erew smaerts 573,761 |  detacnurt erew smaerts 585,3 |     |
| --- | ----------------------------------------------------------- | ----------------------------- | --- |
tcatnoc fo ssol a fo esuaceb
atad fo sraey-tneilc 7.2
|     | smaerts 352,292 gniyalp nigeb ton did 033 ◦ atad yrotcidartnoc tnes 1 ◦ |     |     |
| --- | ----------------------------------------------------------------------- | --- | --- |
ABB
 rof smhtirogla latnemirepxe dengissa erew smaerts 272,433 ◦
s4 naht ssel emit hctaw dah 474,851 ◦ redoced oediv wols a morf dellats 52 ◦
| dedulcxe erew snoisses 149,96 | dedulcxe erew smaerts 978,851 | deredisnoc erew smaerts 408,421                            |     |
| ----------------------------- | ----------------------------- | ---------------------------------------------------------- | --- |
|                               | dengissa erew snoisses 918,74 |  detacnurt erew smaerts 755,3 tcatnoc fo ssol a fo esuaceb |     |
atad fo sraey-tneilc 0.4 atad fo sraey-tneilc 5.2
CIBUC dengissa erew smaerts 499,201 ◦
| smaerts 662,734 | smaerts 386,382 gniyalp nigeb ton did 083 ◦ |     |     |
| --------------- | ------------------------------------------- | --- | --- |
eveisneP
noitarud yduts eht fo snoitrop ◦
noitazimodnar tnewrednu snoisses 775,413
s4 naht ssel emit hctaw dah 784,661 ◦ redoced oediv wols a morf dellats 29 ◦
deredisnoc erew smaerts 135,621 deredisnoc erew smaerts 981,736
|     | dengissa erew snoisses 915,84 dedulcxe erew smaerts 297,661 |  detacnurt erew smaerts 723,3 | .smhtiroglaRBArosnoitcennocPCTegnahctonseoddnamaertswenastratsylnoslennahc |
| --- | ----------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------- |
tcatnoc fo ssol a fo esuaceb
atad fo sraey-tneilc 2.71 atad fo sraey-tneilc 1.31 putrats ni tneps syad-tneilc 2.1 ◦ gniyalp tneps sraey-tneilc 1.31 ◦
atad fo sraey-tneilc 5.2 dellats tneps syad-tneilc 9.7 ◦
| smaerts 613,409,1 sPI euqinu 710,96 | MH-CPMtsuboR smaerts 323,392 |     |     |
| ----------------------------------- | ---------------------------- | --- | --- |
gniyalp nigeb ton did 312 ◦
s4 naht ssel emit hctaw dah 306,561 ◦ redoced oediv wols a morf dellats 65 ◦
deredisnoc erew smaerts 553,821
|     | dengissa erew snoisses 480,94 dedulcxe erew smaerts 681,661 |  detacnurt erew smaerts 085,3 |     |
| --- | ----------------------------------------------------------- | ----------------------------- | --- |
tcatnoc fo ssol a fo esuaceb
atad fo sraey-tneilc 6.2
smaerts 145,492 gniyalp nigeb ton did 725 ◦
MH-CPM
margaidwofllairtdezimodnaR
s4 naht ssel emit hctaw dah 081,071 ◦ redoced oediv wols a morf dellats 46 ◦ deredisnoc erew smaerts 126,231
|     | dengissa erew snoisses 069,94 dedulcxe erew smaerts 926,071 |  detacnurt erew smaerts 018,3 |     |
| --- | ----------------------------------------------------------- | ----------------------------- | --- |
tcatnoc fo ssol a fo esuaceb
atad fo sraey-tneilc 8.2
smaerts 052,303 gniyalp nigeb ton did 583 ◦
uguF
A
510    17th USENIX Symposium on Networked Systems Design and Implementation USENIX Association

B Descriptionofopendata video_acked collects a data point every time a Puffer
serverreceivesavideochunkacknowledgementfromaclient.
The open data we are releasing comprise different Eachdatapointcanbematchedtoadatapointinvideo_sent
“measurements”—eachmeasurementcontainsadifferentset usingvideo_ts(ifthechunkiseveracknowledged)andused
oftime-seriesdatacollectedonPufferservers.Belowwehigh- tocalculatethetransmissiontimeofthechunk—difference
lighttheformatofinterestingfieldsinthreemeasurements
betweenthetimestampsinthetwodatapoints.Specifically,
that are essential for analysis: video_sent,video_acked, eachdatapointinvideo_ackedcontains:
andclient_buffer.
• time:timestampwhenthechunkisacknowledged
video_sentcollectsadatapointeverytimeaPufferserver
session_id
•
sendsavideochunktoaclient.Eachdatapointcontains:
• expt_id
• time:timestampwhenthechunkissent
• channel
• session_id:uniqueIDforthevideosession
• video_ts
• expt_id:uniqueIDtoidentifytheexperimentalgroup;
expt_idcanbeusedasakeytoretrievetheexperimen- client_buffercollectsclient-sideinformationreported
toPufferserversonaregularintervalandwhencertainevents
talsetting(e.g.,ABR,congestioncontrol)whensending
thechunk,inanotherfileweareproviding. occur.Eachdatapointcontains:
• channel:TVchannelname • time:timestampwhentheclientmessageisreceived
| • video_ts:uniquepresentationtimestampofthechunk   |     |     | • session_id |     |     |
| -------------------------------------------------- | --- | --- | ------------ | --- | --- |
| • format:encodingsettingsofthechunk,includingreso- |     |     | • expt_id    |     |     |
| lutionandconstantratefactor(CRF)                   |     |     | • channel    |     |     |
• size:sizeofthechunk • event:eventtype,e.g.,wasthistriggeredbyaregular
• ssim_index:SSIMofthechunk reporteveryquartersecond,orbecausetheclientstalled
| • cwnd:congestionwindowsize(tcpi_snd_cwnd) |     |     | orbeganplaying. |     |     |
| ------------------------------------------ | --- | --- | --------------- | --- | --- |
• in_flight: number of unacknowledged packets in • buffer:playbackbuffersize
flight (tcpi_unacked - tcpi_sacked - tcpi_lost + • cum_rebuf: cumulative rebuffer time in the current
| tcpi_retrans) |     |     | stream |     |     |
| ------------- | --- | --- | ------ | --- | --- |
• min_rtt:minimumRTT(tcpi_min_rtt) Between Jan. 26, 2019 and Feb. 2, 2020, we collected
• rtt:smoothedRTTestimate(tcpi_rtt) 675,839,652 data points in video_sent,677,956,279 data
| • delivery_rate:     | estimate | of TCP throughput | video_acked,   |                   |                |
| -------------------- | -------- | ----------------- | -------------- | ----------------- | -------------- |
|                      |          |                   | points in      | and 4,622,575,336 | data points in |
| (tcpi_delivery_rate) |          |                   | client_buffer. |                   |                |
USENIX Association 17th USENIX Symposium on Networked Systems Design and Implementation    511