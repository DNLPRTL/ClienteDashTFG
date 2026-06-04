|     |         |     | A   | Control-Theoretic |               |                 | Approach    |       |     | for      |     |      |     |
| --- | ------- | --- | --- | ----------------- | ------------- | --------------- | ----------- | ----- | --- | -------- | --- | ---- | --- |
|     | Dynamic |     |     | Adaptive          |               | Video           | Streaming   |       |     | over     |     | HTTP |     |
|     |         |     |     | Xiaoqi            | Yin, Abhishek | Jindal,         | Vyas Sekar, | Bruno |     | Sinopoli |     |      |     |
|     |         |     |     |                   |               | Carnegie Mellon | University  |       |     |          |     |      |     |
{yinxiaoqi522, abhishekjindal93}@gmail.com, {vsekar,brunos}@andrew.cmu.edu
| ABSTRACT |     |     |     |     |     |     | 1 Introduction |         |      |             |     |              |           |
| -------- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ---- | ----------- | --- | ------------ | --------- |
|          |     |     |     |     |     |     | Many recent    | studies | have | highlighted |     | the critical | role that |
User-perceivedquality-of-experience(QoE)iscriticalinIn-
ternet video applications as it impacts revenues for content user-perceivedquality-of-experience(QoE)playsinInternet
providersanddeliverysystems.Giventhatthereislittlesup- video applications, as it ultimately affects revenue streams
|      |        |         |     |            |                |         | forcontentproviders[24,35]. |     |     | Specifically,metricssuchas |     |     |     |
| ---- | ------ | ------- | --- | ---------- | -------------- | ------- | --------------------------- | --- | --- | -------------------------- | --- | --- | --- |
| port | in the | network | for | optimizing | such measures, | bottle- |                             |     |     |                            |     |     |     |
neckscouldoccuranywhereinthedeliverysystem. Conse- the duration of rebuffering (i.e., the player’s playout buffer
quently, a robust bitrate adaptation algorithm in client-side doesnot havecontent torender), startup delay(i.e., thelag
|         |             |     |           |      |                  |        | between | the user | clicking | vs. the | time | to begin | rendering), |
| ------- | ----------- | --- | --------- | ---- | ---------------- | ------ | ------- | -------- | -------- | ------- | ---- | -------- | ----------- |
| players | is critical |     | to ensure | good | user experience. | Previ- |         |          |          |         |      |          |             |
theaverageplaybackbitrate,andthevariabilityofthebitrate
| ous | studies | have shown | key | limitations | of state-of-art | com- |     |     |     |     |     |     |     |
| --- | ------- | ---------- | --- | ----------- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
mercial solutions and proposed a range of heuristic fixes. deliveredhaveemergedaskeyfactors.
Despite the emergence of several proposals, there is still a GiventhecomplexInternetvideodeliveryecosystemand
distinct lack of consensus on: (1) How best to design this presenceofdiversebottlenecks,thebitrateadaptationlogic
client-side bitrate adaptation logic (e.g., use rate estimates in the client-side video player becomes critical to optimize
vs. buffer occupancy); (2) How well specific classes of ap- userexperience[16].IntheHTTP-baseddeliverymodelthat
proacheswillperformunderdiverseoperatingregimes(e.g., predominates today [44], videos are typically chunked and
high throughput variability); or (3) How do they actually encoded at different bitrate levels. The goal of an adaptive
balance different QoE objectives (e.g., startup delay vs. re- videoplayeristochoosethebitratelevelforfuturechunks
buffering). Tothisend,thispapermakesthreekeytechnical todeliverthehighestpossibleQoE;e.g.,maximizingbitrate
contributions. First, to bring some rigor to this space, we whileminimizingthelikelihoodofrebufferingandavoiding
developaprincipledcontrol-theoreticmodeltoreasonabout toomanybitrateswitches.
| abroadspectrumofstrategies. |     |     |     | Second,weproposeanovel |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Manyrecenteffortshavepointedoutkeychallengesinde-
modelpredictivecontrolalgorithmthatcanoptimallycom- signingthisadaptationlogic(e.g.,[46,17,32,34])andsev-
binethroughputandbufferoccupancyinformationtooutper- eral proposals have emerged to try and address these chal-
| form | traditional | approaches. |     | Third, | we present | a practical |               |      |           |         |     |               |        |
| ---- | ----------- | ----------- | --- | ------ | ---------- | ----------- | ------------- | ---- | --------- | ------- | --- | ------------- | ------ |
|      |             |             |     |        |            |             | lenges (e.g., | [34, | 17, 33]). | Despite | the | proliferation | of nu- |
implementation in a reference video player to validate our merous algorithms, however, there appears to be a lack of
approachusingrealistictrace-drivenemulations. clarityandconsensusacrossthesesolutionsonseveralfronts;
e.g.,someargueforbetterthroughputestimation[47],while
CCS Concepts others suggest improving chunk scheduling [34]. Some re-
searchersevenargueagainstrate-basedapproachesthatrely
•Informationsystems→Multimediastreaming;•Networks onthroughputestimatesfrompreviouschunkdownloadsand
→Networkprotocoldesign;Applicationlayerprotocols; make the case for buffer-occupancy based algorithms that
maketheirdecisionspurelybasedonbufferoccupancy[33].
Keywords
Inordertounderstandthefundamentaltradeoffsbetween
|     |     |     |     |     |     |     | different | classes | of algorithms |     | (e.g., rate- | vs buffer-based) |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------- | --- | ------------ | ---------------- | --- |
InternetVideo;BitrateAdaptation;DASH;ModelPredictive underdifferentoperatingregimes(e.g.,lowvs.highthrough-
Control
|     |     |     |     |     |     |     | put variability),                             |     | we begin | by formulating |     | the video | bitrate |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | -------- | -------------- | --- | --------- | ------- |
|     |     |     |     |     |     |     | adapdationasastochasticoptimalcontrolproblem. |     |          |                |     |           | Wefor-  |
mallydefinethekeydynamicvariablesinvolvedinthevideo
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonal
|     |     |     |     |     |     |     | adaptation | problem | and | a concrete | objective. | This | frame- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | ---------- | ---------- | ---- | ------ |
orclassroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeor
distributedforprofitorcommercialadvantageandthatcopiesbearthisnotice
workallowsustooutlinethebroaderdesignspaceofcontrol
| andthefullcitationonthefirstpage.  |     |     |     | Copyrightsforcomponentsofthiswork |                             |     |                           |     |     |                           |     |     |     |
| ---------------------------------- | --- | --- | --- | --------------------------------- | --------------------------- | --- | ------------------------- | --- | --- | ------------------------- | --- | --- | --- |
|                                    |     |     |     |                                   |                             |     | algorithmsforthisproblem. |     |     | Weidentifyakeyshortcoming |     |     |     |
| ownedbyothersthanACMmustbehonored. |     |     |     |                                   | Abstractingwithcreditisper- |     |                           |     |     |                           |     |     |     |
mitted. Tocopyotherwise,orrepublish,topostonserversortoredistributeto inexistingapproachesthatrelyexclusivelyonpurerate-or
| lists,requirespriorspecificpermissionand/orafee. |     |     |     |     | Requestpermissionsfrom |     |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
buffer-basedstrategies,andthatmightbepotentiallymissing
permissions@acm.org.
outonstrategiesthatcombinebothsignals.
SIGCOMM’15,August17-21,2015,London,UnitedKingdom
(cid:13)c 2015ACM.ISBN978-1-4503-3542-3/15/08...$15.00 Building on insights from the control-theoretic formula-
DOI:http://dx.doi.org/10.1145/2785956.2787486 tion, we argue that model predictive control (MPC) [22] is
325

a suitable class of algorithms that can optimally combine intermsofmedianQoE.Italsoachievessignificantim-
bothrate-basedandbuffer-basedfeedbacksignals.Atahigh provement(60+%medianQoE)comparedtotheindus-
level, MPC attempts to predict key environment variables tryreferenceplayerdash.js;
over a moving look-ahead horizon and solve an exact opti- 2. Ourfastandlow-overheadimplementationFastMPCre-
| mizationproblembasedontheprediction. |     |     |     |     | MPCisthetech- |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
quiressimilarCPUusageandonly60kBextramemory
nology of choice in a multitude of real world control prob- usagecomparingtootheralgorithms.
| lems[22]. | Inadditiontoitsintuitiveformulation,itcanex- |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
plicitly handle complex control objectives and constraints, Contributionsandroadmap:Insummary,thispapermakes
thefollowingkeycontributions:1
| and has | a set of | well understood |     | tuning | parameters | such as |     |     |     |     |     |     |
| ------- | -------- | --------------- | --- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- |
thepredictionhorizon.Moreover,MPChasotherqualitative • Developmentofaformalcontrol-theoreticmodelofthe
advantages as its development time is much shorter com- bitrateadaptationproblem(Section3);
paredtoadvancedcontrolmethodsanditiseasiertomain-
• DesignofaMPCapproachthatsubsumesexistingrate-
tain, as changing model parameters does not require com- andbuffer-basedstrategies(Section4);
pleteredesign.
|     |     |     |     |     |     |     | • A practical | and fast table | enumeration |     | based | algorithm |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | ----------- | --- | ----- | --------- |
In our context, the MPC approach entails predicting the FastMPC that near-optimally approximates the perfor-
expectedthroughputforthenextfewchunksandusingthis manceofanexactMPCapproach(Section5);
tomakeoptimalbitratedecisionsforQoEmaximization.In-
• Alow-overheadimplementationbasedontheopensource
deed,oursimulationresultsconfirmthatifwecouldrunan
referencevideoplayerdash.js(Section6);
| optimal | MPC algorithm |     | and | the prediction |     | error was low, |     |     |     |     |     |     |
| ------- | ------------- | --- | --- | -------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
• Asystematicevaluationofdifferentclassesofalgorithms
thentheMPCschemecanoutperformtraditionalrate-based
|     |     |     |     |     |     |     | over a | wide range of | operating | parameters | and | realistic |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --------- | ---------- | --- | --------- |
andbuffer-basedstrategies.
traces(Section7)
| In practice, | however, |     | running | a MPC-based |     | algorithm is |     |     |     |     |     |     |
| ------------ | -------- | --- | ------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
WebeginbydiscussingbackgroundonDASHandrelated
| challenging | because | it  | needs | to solve | a non-trivial | discrete |     |     |     |     |     |     |
| ----------- | ------- | --- | ----- | -------- | ------------- | -------- | --- | --- | --- | --- | --- | --- |
workinthenextsection.
| optimization | problem | at  | each | time step. | Even | ignoring the |     |     |     |     |     |     |
| ------------ | ------- | --- | ---- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
computational overhead, there are practical difficulties as 2 Background and Related Work
| we might | need to | bundle | this | solver | logic with | every video |     |     |     |     |     |     |
| -------- | ------- | ------ | ---- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
player or require users to download and install additional We begin with a high-level overview of how HTTP-based
|     |     |     |     |     |     |     | adaptive video | streaming | works, | before describing |     | the key |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------ | ----------------- | --- | ------- |
software. Toaddressthesechallenges,wedevelopasimple-
shortcomingsoftoday’sstate-of-artsolutions.
| yet-efficientFastMPCmechanism. |     |     |     | Conceptually,FastMPC |     |     |          |                    |      |              |     |         |
| ------------------------------ | --- | --- | --- | -------------------- | --- | --- | -------- | ------------------ | ---- | ------------ | --- | ------- |
|                                |     |     |     |                      |     |     | Internet | video technologies | such | as Microsoft |     | Smooth- |
essentiallyfollowsatableenumerationapproach,wherewe
Streaming[13],Apple’sHLS[5],andAdobe’sHDS[2]rely
describetheproblemstate-space,solvethespecificinstances
|     |     |     |     |     |     |     | onHTTP-basedadaptivestreaming. |     |     | Thisclassofprotocols |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | -------------------- | --- | --- |
optimallyoffline,andstoretheoptimalcontroldecisionsfor
isbeingstandardizedundertheumbrellaofDynamicAdap-
| futureonlineuse. |     | Ifimplementednaively,however,thesize |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of this table can induce significant memory overhead and tiveStreamingoverHTTPorDASH[16].InDASHsystems,
|                |     |       |         |        |            |            | each video | consists of multiple | segments | or  | “chunks” | (cor- |
| -------------- | --- | ----- | ------- | ------ | ---------- | ---------- | ---------- | -------------------- | -------- | --- | -------- | ----- |
| startup delays | for | video | players | (e.g., | additional | JavaScript |            |                      |          |     |          |       |
respondingtoafewsecondsofplaytime)andeachchunkis
toload). Fortunately,weshowthatwithasimplevaluebin-
|     |     |     |     |     |     |     | encodedatmultiplediscretebitrates. |     |     | Thechunksfromdif- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | ----------------- | --- | --- |
ningandcompressionstrategy,wecanachievenear-optimal
ferentbitratestreamsarealignedsothatthevideoplayercan
performancewithmanageabletablesizes.
switchtoadifferentbitrateifnecessaryatachunkboundary.
WehaveprototypedourFastMPCbitrateadaptationalgo-
|     |     |     |     |     |     |     | This approach | has several | pragmatic | advantages |     | over cus- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --------- | ---------- | --- | --------- |
rithminanopensourcedynamicadaptivestreamingplayer
tomstreamingprotocolssuchasReal-TimeMessagingPro-
| called dash.js |     | [1]. | Our choice |     | of platform | is a prag- |     |     |     |     |     |     |
| -------------- | --- | ---- | ---------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
tocol(RTMP).TheuseofHTTPenablesproviderstoseam-
| matic one—it | is  | the reference |     | open-source | implementation |     |                          |     |                              |     |     |     |
| ------------ | --- | ------------- | --- | ----------- | -------------- | --- | ------------------------ | --- | ---------------------------- | --- | --- | --- |
|              |     |               |     |             |                |     | lesslybypassmiddleboxes. |     | Furthermore,itcanuseexisting |     |     |     |
fortheMPEG-DASHstandardbasedontheHTML5speci-
|     |     |     |     |     |     |     | commodity | CDN servers | without | requiring | custom | modifi- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------- | --------- | ------ | ------- |
ficationandisactivelysupportedbyleadingindustrypartic-
|            |                                           |     |     |     |     |     | cations. Finally, | by making | the | server stateless, |     | one can |
| ---------- | ----------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --------- | --- | ----------------- | --- | ------- |
| ipants[7]. | Weshowthatourimplementationaddsnegligible |     |     |     |     |     |                   |           |     |                   |     |         |
implementbetterapplication-layerresilienceusingmultiple
| overhead | to the | baseline | dash.js |     | player. | We also show- |     |     |     |     |     |     |
| -------- | ------ | -------- | ------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
serversandCDNs[41,40].
casetheFastMPC-basedplayerinourdemopage[14].
|             |     |            |     |     |           |             | Figure 1 | shows an abstract | model | of the | adaptive | video |
| ----------- | --- | ---------- | --- | --- | --------- | ----------- | -------- | ----------------- | ----- | ------ | -------- | ----- |
| We evaluate | our | algorithms |     | and | prototype | implementa- |          |                   |       |        |          |       |
player. Theplayerusessomeinputs(e.g.,bufferoccupancy
tion using realistic emulation experiments on measured [9, orestimatesofthenetworkthroughput)initsdecisionlogic
10]andsyntheticthroughputvariabilitytraces.Wealsoaug-
tochoosethebitratelevelforthenextchunk(s)tobedown-
menttheseresultswithsimulation-basedsensitivityanalysis
|             |            |     |            |     |               |         | loaded. Inmakingthisdecision, |                    |     | therearemanypotentially |         |      |
| ----------- | ---------- | --- | ---------- | --- | ------------- | ------- | ----------------------------- | ------------------ | --- | ----------------------- | ------- | ---- |
| experiments | to analyze |     | the effect | of  | key operating | parame- |                               |                    |     |                         |         |      |
|             |            |     |            |     |               |         | conflicting                   | QoE considerations | a   | player must             | account | for: |
ters on the performance of different classes of algorithms. (1)minimizingrebufferingeventswheretheplaybackbuffer
Ourkeyfindingsare:
1Anearlyworkshopversionofthepapermadethecasefor
| 1. Our | proposed | MPC | approach | consistently |     | outperforms |                         |     |          |                  |     |     |
| ------ | -------- | --- | -------- | ------------ | --- | ----------- | ----------------------- | --- | -------- | ---------------- | --- | --- |
|        |          |     |          |              |     |             | aMPC-basedapproach[50]. |     | However, | itdidnotprovidea |     |     |
the state-of-art adaptation algorithms by 15% in broad- concretealgorithm,apracticalimplementation,andevalua-
band(FCC)datasetand10%incellular(HSDPA)dataset tionusingrealthroughputtraces.
326

|     |     |     |     |     |     |     |     | timated | available | throughput. |     | However, | as  | shown | in prior |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----------- | --- | -------- | --- | ----- | -------- |
TThhrroouugghhppuutt   Video Player work throughput estimation on top of HTTP suffers from
|     | Throughput |     |     | PPrreeddiiccttoorr |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Prediction significant biases [32], which leads to problems with tradi-
|                  |     |         |     |     |     | GET |     | tional rate-based |     | approaches. |     | Some | solutions | try | to work |
| ---------------- | --- | ------- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | --- | ---- | --------- | --- | ------- |
| BBiittrraattee   |     | Bitrate |     |     |     |     |     |                   |     |             |     |      |           |     |         |
CCoonnttrroolllleerr HHTTTTPP IInntteerrnneett aroundthesebiasesbyeithersmoothingoutthroughputesti-
Chunk
|     |     |     |     |     |     |     |     | mates[47]orchoosingbetterschedulingstrategies[34]. |     |     |     |     |     |     | On  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Buffer
Occupancy theotherhand,recentworkmakesacaseforbuffer-basedal-
BBBuuuffffffeeerrr
|     |     |     |     |     |     |     |     | gorithms[33]. |            | Ratherthanusingthroughputestimates,this |        |           |     |        |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --------------------------------------- | ------ | --------- | --- | ------ | -------- |
|     |     |     |     |     |     |     |     | class of      | algorithms | uses                                    | buffer | occupancy |     | as the | feedback |
QoE
End User signal, and designs mechanisms to keep the buffer occu-
pancyatadesiredlevel,essentiallydiscardinganyavailable
| Figure1: |     | AbstractmodelofDASHplayers |     |     |     |     |     | throughputinformation. |           |          |     |      |             |     |            |
| -------- | --- | -------------------------- | --- | --- | --- | --- | --- | ---------------------- | --------- | -------- | --- | ---- | ----------- | --- | ---------- |
|          |     |                            |     |     |     |     |     | Despite                | the broad | interest | in  | this | topic, what | is  | critically |
isemptyandcannotrenderthevideo;(2)deliveringashigh
lackingtodayisaprincipledunderstandingofbitrateadapta-
| a playback | bitrate        | as  | possible | within | the | throughput | con-      |                  |           |       |                |     |                |        |          |
| ---------- | -------------- | --- | -------- | ------ | --- | ---------- | --------- | ---------------- | --------- | ----- | -------------- | --- | -------------- | ------ | -------- |
|            |                |     |          |        |     |            |           | tion algorithms. |           | Each  | aforementioned |     | solution       | offers | point    |
| straints;  | (3) minimizing |     | startup  | delay  | so  | that the   | user does |                  |           |       |                |     |                |        |          |
|            |                |     |          |        |     |            |           | heuristics       | that work | under | specific       |     | (and implicit) |        | environ- |
notquitwhilewaitingforthevideotoload;and(4)keeping
|     |     |     |     |     |     |     |     | mentalassumptions. |     | Whileeachapproachseeninisolation |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------------------------------- | --- | --- | --- | --- | --- |
theplaybackassmoothaspossiblebyavoidingfrequentor
|     |     |     |     |     |     |     |     | hasbeenshowntooutperformcommercialplayers, |     |     |     |     |     |     | thereis |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- |
largebitratejumps[24,35].
littleefforttosystematicallycomparehowdifferentclasses
| To see | why | these | objectives | are | conflicting, |     | let us con- |     |     |     |     |     |     |     |     |
| ------ | --- | ----- | ---------- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofalgorithmsstackupagainsteachotherorwhichofthese
| sider two | extreme | solutions. |     | A trivial | solution | to  | minimize |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | --- | --------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
technicalcomponentsarecritical,orhowrobustthesealgo-
rebuffering and the startup delay would be to always pick rithmsareacrossdifferentoperatingregimes(e.g.,through-
| the lowest  | bitrate, | but         | it conflicts |         | with the | goal       | of deliver- |               |             |                  |                         |      |         |          |          |
| ----------- | -------- | ----------- | ------------ | ------- | -------- | ---------- | ----------- | ------------- | ----------- | ---------------- | ----------------------- | ---- | ------- | -------- | -------- |
|             |          |             |              |         |          |            |             | putstability, | buffersize, |                  | numberofbitratelevels). |      |         |          | Further- |
| ing high    | bitrate. | Conversely, |              | picking | the      | highest    | available   |               |             |                  |                         |      |         |          |          |
|             |          |             |              |         |          |            |             | more, many    | of          | these algorithms |                         | even | fail to | formally | state    |
| bitrate may | lead     | to many     | rebuffering  |         | events.  | Similarly, | the         |               |             |                  |                         |      |         |          |          |
whatobjectivetheyseektooptimizemakingithardertocon-
| goal of | maintaining |     | a smooth | playback | may | also | conflict if |     |     |     |     |     |     |     |     |
| ------- | ----------- | --- | -------- | -------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ductameaningfulcomparison.
| the optimal    | choice | to      | simultaneously |     | minimize  |          | rebuffering |                 |                                          |      |         |      |             |      |         |
| -------------- | ------ | ------- | -------------- | --- | --------- | -------- | ----------- | --------------- | ---------------------------------------- | ---- | ------- | ---- | ----------- | ---- | ------- |
|                |        |         |                |     |           |          |             | Our first-order |                                          | goal | in this | work | is to bring | some | clarity |
| and maximizing |        | average | bitrate        | is  | to switch | bitrates | for ev-     |                 |                                          |      |         |      |             |      |         |
|                |        |         |                |     |           |          |             | tothisspace.    | Ratherthandesignyetanotherpointsolution, |      |         |      |             |      |         |
erychunk. we start by developing a first-principles approach via con-
| The focus | of  | this | paper is | on client-side |     | adaptation | solu- |             |            |     |         |           |     |           |       |
| --------- | --- | ---- | -------- | -------------- | --- | ---------- | ----- | ----------- | ---------- | --- | ------- | --------- | --- | --------- | ----- |
|           |     |      |          |                |     |            |       | trol theory | to develop | a   | general | framework |     | to reason | about |
tions.Othercomplementaryworkincludestheuseofserver-
classesofalgorithms.Inthenextsection,weusethiscontrol-
sidebitrateswitching(e.g.,[37,18]),TCPchangestoavoid theoretic “lens” to formally define the stochastic optimiza-
| bursts (e.g., | [27]), | and | in-network |     | throughput | management |     |     |     |     |     |     |     |     |     |
| ------------- | ------ | --- | ---------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionthatvideobitrateadaptationalgorithmstrytosolve.
| andcaching(e.g.,[31,45,42]). |             |         |            | Wefocusontheclient-side       |             |        |             |                     |           |            |         |              |          |        |         |
| ---------------------------- | ----------- | ------- | ---------- | ----------------------------- | ----------- | ------ | ----------- | ------------------- | --------- | ---------- | ------- | ------------ | -------- | ------ | ------- |
|                              |             |         |            |                               |             |        |             | 3 Control-Theoretic |           |            |         | Model        |          |        |         |
| problemfortwokeyreasons.     |             |         |            | First,client-sidesolutionsof- |             |        |             |                     |           |            |         |              |          |        |         |
| fer the most                 | immediately |         | deployable |                               | alternative |        | in contrast |                     |           |            |         |              |          |        |         |
|                              |             |         |            |                               |             |        |             | In this section,    |           | we develop | a       | mathematical |          | model  | of the  |
| to solutions                 | that        | require | in-network |                               | support     | (e.g., | [31, 45,    |                     |           |            |         |              |          |        |         |
|                              |             |         |            |                               |             |        |             | HTTP video          | streaming |            | process | and          | formally | define | the bi- |
42]),server-sidesoftwarechanges(e.g.,[37,18]),ormodi- trateadaptationproblem. Thismodelgivesusaframework
ficationstolower-layertransportprotocols(e.g.,[27,28,39,
|           |         |     |        |          |        |      |             | to compare | and | evaluate | existing | algorithms |     | and | serves as |
| --------- | ------- | --- | ------ | -------- | ------ | ---- | ----------- | ---------- | --- | -------- | -------- | ---------- | --- | --- | --------- |
| 29, 36]). | Second, | the | client | is often | in the | best | position to |            |     |          |          |            |     |     |           |
thefoundationforpotentialimprovements.
| quickly   | detect | performance |     | issues   | and respond |             | to dynam- |           |     |           |     |       |     |     |     |
| --------- | ------ | ----------- | --- | -------- | ----------- | ----------- | --------- | --------- | --- | --------- | --- | ----- | --- | --- | --- |
|           |        |             |     |          |             |             |           | 3.1 Video |     | Streaming |     | Model |     |     |     |
| ics. That | said,  | we believe  |     | that the | formal      | foundations | and       |           |     |           |     |       |     |     |     |
algorithmswedevelopcanbeequallyappliedtotheseother Wemodelavideoasasetofconsecutivevideosegmentsor
deploymentscenarios.
|     |     |     |     |     |     |     |     | chunks, | V = {1,2,··· |     | ,K}, eachofwhichcontainsLsec- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ----------------------------- | --- | --- | --- | --- |
Many measurement studies have shown the poor perfor- onds of video. Each chunk is encoded at different bitrates.
manceofstate-of-artvideoplayerswithrespecttotheseQoE Let R be the set of all available bitrate levels. The video
| measures(e.g.,[46, |     |     | 34, 32]). | Thesestudiesshowthatmost |     |     |     |                                 |     |     |     |     |            |     |        |
| ------------------ | --- | --- | --------- | ------------------------ | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ---------- | --- | ------ |
|                    |     |     |           |                          |     |     |     | playercanchoosetodownloadchunkk |     |     |     |     | atbitrateR |     | k ∈ R. |
problems are not artifacts of specific players but manifest Letd (R )bethesizeofchunkkencodedatbitrateR . In
|     |     |     |     |     |     |     |     | k   | k   |     |     |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
acrossallstate-of-artplayerssuchasSmoothStreaming[13], constant bitrate (CBR) case, d (R ) = L×R , while in
|     |     |     |     |     |     |     |     |     |     |     |     | k k |     | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Netflix [11], Adobe OSMF [3], and Akamai HD [4]. For variable bitrate (VBR) case the d ∼ R relationship can
|     |     |     |     |     |     |     |     |     |     |     |     | k   | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
brevity we do not reproduce these results here but refer in- differacrosschunks.
terestedreaderstopriorwork(e.g.,[46,34,32]). The higher bitrate is selected, the higher video quality
Toalleviatetheseproblems,therehavebeenseveralrecent is perceived by the user. Let q(·) : R → R be a non-
+
proposalsintheresearchliterature(e.g.,[47,34,18,33,38]). decreasingfunctionwhichmapsselectedbitrateR k tovideo
Atahighlevel, thesesolutionscanberoughlydividedinto qualityperceivedbyuserq(R ). Notethatq(·)maydepend
k
two categories: (1) rate-based algorithms and (2) buffer- on the video-playing device as well as the content of the
based algorithms. Video players with rate-based methods video. For example, while on HDTV 3Mbps and 1Mbps
essentiallypickthehighestpossiblebitratebasedonthees- may lead to significant difference in user experience, the
327

The determination of waiting time ∆t , also referred as
k
chunkschedulingproblem,isanequallyinterestingandim-
Download & Wait
y c n a 𝐵 𝑘 𝑑 𝑘 𝐶 (𝑅 𝑘 𝑘 ) +Δ𝑡 𝑘 Rebuffer p st o r r e t a a m nt in p g ro [ b 3 l 4 e ] m . i H n o i w m e p v r e o r v , i i n n g t f h a i i s rn p e a s p s e o r f w m e u a lt s i s - u p m la e ye t r ha v t id t e h o e
p u playerimmediatelystartstodownloadchunkk+1assoon
c c 𝐵 𝑘+1 as chunk k is downloaded. The one exception is when the
O
re buffer is full, the player waits for the buffer to reduce to a
ffu levelwhichallowschunkktobeappended. Formally,
B 0 Time
𝑡 𝑘 𝑡 𝑘+1 (cid:32)(cid:18) (cid:19) (cid:33)
d (R )
Start chunk k Start chunk k+1 ∆t = B − k k +L−B (4)
Figure2: Illustrationofbufferdynamics k k C max
k + +
videoqualityin3Mbpsand1Mbpsmaybesimilaronamo-
3.2 QoE Maximization Problem
biledevice;Also,improvingthebitrateof“dynamic”chunks
willresultinmoreQoEgainthanimproving“static”chunks.
TheultimategoalofbitrateadaptationistoimprovetheQoE
Thevideosegmentsaredownloadedintoaplaybackbuffer,
of users in order to achieve higher long-term user engage-
whichcontainsdownloadedbutasyetunviewedvideo. Let
ment[24].OurgoalistoprovideaflexibleQoEmodelrather
B(t) ∈ [0,B ] be the buffer occupancy at time t, i.e.,
max thanafixednotionofQoEasthisisanactiveareaofresearch
theplaytimeofthevideoleftinthebuffer. Thebuffersize
[19]. WhileusersmaydifferintheirspecificQoEfunctions,
B dependsonthepolicyoftheserviceprovider,aswell
max wecanenumeratethekeyelementsofvideoQoEas:
asstoragelimitationsontheplayer. Atypicalplayerbuffer
1. Average Video Quality: The average per-chunk quality
mayholdfewtensofsecondsofvideosegments.
Figure 2 helps illustrate the conceptual operation of the overallchunks: K 1 (cid:80)K k=1 q(R k );
video player. At time t , the video player starts to down- 2. Average Quality Variations: This tracks the magnitude
k
load chunk k. The download time for this chunk will be ofthechangesinthequalityfromonechunktoanother:
d (R )/C ; i.e., it depends on the size of selected chunk 1 (cid:80)K−1|q(R )−q(R )|;
k k k K−1 k=1 k+1 k
with bitrate R k , as well as average download speed C k ex- 3. Rebuffer:Foreachchunkkrebufferingoccursifthedown-
perienced during this download process. Once chunk k is load time d (R )/C is higher than the playout buffer
k k k
completelydownloaded,thevideoplayerwaitsfor∆t k and level when the chunk download started (i.e., B k ). Thus
startstodownloadthenextchunkk+1attimet k+1 . Weas- thetotalrebuffertime3is (cid:80)K (cid:16) dk(Rk) −B (cid:17) .
sumethatthewaitingtime∆t k issmallandwillnotleadto k=1 Ck k +
rebufferingevents. IfwedenotebyC t thenetworkthrough- 4. StartupDelayT s ,assumingT s (cid:28)B max .
putattimet,thenwehave: As users may have different preferences on which of the
four components is more important, we define the QoE of
d (R )
t =t + k k +∆t (1) videosegment1throughK byaweightedsumoftheafore-
k+1 k C k
k mentionedcomponents:
1 (cid:90) tk+1−∆tk
C k = t −t −∆t C t dt. (2) (cid:88) K K (cid:88) −1
k+1 k k tk QoE
1
K = q(R
k
)−λ |q(R
k+1
)−q(R
k
)|
ThebufferoccupancyB(t)evolvesasthechunksarebe- k=1 k=1
ingdownloadedandthevideoisbeingplayed. Specifically, K (cid:18) (cid:19)
the buffer occupancy increases by L seconds after chunk k −µ (cid:88) d k (R k ) −B −µ T (5)
C k s s
isdownloadedanddecreasesastheuserwatchesthevideo.2 k=1 k +
Let B = B(t ) denote the buffer occupancy when the
k k Hereλ,µ,µ arenon-negativeweightingparameterscor-
playerstartstodownloadchunkk. Thebufferdynamicscan s
respondingtovideoqualityvariations,rebufferingtimeand
thenbeformulatedas:
startup delay, respectively. A relatively small λ indicates
thattheuserisnotparticularlyconcernedaboutvideoquality
(cid:32)(cid:18) (cid:19) (cid:33)
d (R ) variability;thelargeλis,themoreeffortismadetoachieve
B = B − k k +L−∆t (3)
k+1 k C k smoother changes of video quality. A large µ, relatively to
k + + the other parameters, indicates that a user is deeply con-
Here,thenotation(x) = max{x,0}ensuresthattheterm cerned about rebuffering. In cases where users prefer low
+
can never be negative. Note that if B k < d k (R k )/C k , the startupdelay,weemployalargeµ s .
buffer becomes empty while the video player is still down- Insummary,thisdefinitionofQoEisquitegeneralasital-
loadingchunkk,leadingtorebuffereventsasshowninFig- lowsustomodelvaryinguserpreferencesondifferentcon-
ure2. tributingfactors.
2The“startup”phasewillbeslightlydifferentastheplayer 3Alternatively,onecanalsoconsiderthenumberofrebuffer-
waitsforsomeamountofbuffertobuildupbeforedraining (cid:16) (cid:17)
thebuffer. ingeventsformulatedas (cid:80)K k=1 1 dk C (R k k) >B k .
328

|     |     |     |      |     |     |     |     |     |     |         |     | D e s i g n   s    | p a c e of  |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------------ | ----------- | --- |
|     | max |     | QoEK |     |     |     | (6) |     |     | Bitrate |     |                    |             |     |
|     |     |     |      | 1   |     |     |     |     |     |         |     | al l  a l g o r it | h m s       |     |
R1,···,RK,Ts
|     |       |                  |        | d (R     | )          |       |          |     |             |     |     |     |              |     |
| --- | ----- | ---------------- | ------ | -------- | ---------- | ----- | -------- | --- | ----------- | --- | --- | --- | ------------ | --- |
|     |       |                  |        | k        | k          |       |          |     |             |     |     |     |              |     |
|     | s.t.  | t                | =t     | +        | +∆t        | ,     | (7)      |     |             |     |     |     | Buffer-based |     |
|     |       | k+1              | k      | C        |            | k     |          |     |             |     |     |     |              |     |
|     |       |                  |        |          | k          |       |          |     |             |     | A3? |     |              |     |
|     |       |                  |        |          |            |       |          |     | Rate-based  |     |     | A2  |              |     |
|     |       |                  | 1      | (cid:90) | tk+1−∆tk   |       |          |     |             |     |     |     |              |     |
|     | C =   |                  |        |          |            | C dt, | (8)      |     |             | A1  |     |     |              |     |
|     | k     |                  |        |          |            | t     |          |     |             |     |     |     | Buffer       |     |
|     |       | t                | −t −∆t |          |            |       |          |     |             |     |     |     |              |     |
|     |       | k+1              | k      | k        | tk         |       |          |     |             |     |     |     | occupancy    |     |
|     |       | (cid:32)(cid:18) |        |          |            |       | (cid:33) |     |             |     |     |     |              |     |
|     |       |                  |        | d (R     | ) (cid:19) |       |          |     | Throughput  |     |     |     |              |     |
|     |       |                  |        | k k      |            |       |          |     | prediction  |     |     |     |              |     |
|     | B k+1 | =                | B k −  |          | +L−∆t      |       | k , (9)  |     |             |     |     |     |              |     |
C
|     |     |     |     | k   | +   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+
|     |       |     |           |     |     |     |      | Figure4:       | Designspaceofalgorithmsforthevideoadap- |                                   |     |     |     |     |
| --- | ----- | --- | --------- | --- | --- | --- | ---- | -------------- | --------------------------------------- | --------------------------------- | --- | --- | --- | --- |
|     | B =T  | ,   | B ∈[0,B   |     | ]   |     | (10) |                |                                         |                                   |     |     |     |     |
|     | 1     | s   | k         | max |     |     |      | tationproblem: |                                         | Mostcurrentapproacheschoosethebi- |     |     |     |     |
|     | R ∈R, |     | ∀k =1,··· | ,K. |     |     | (11) |                |                                         |                                   |     |     |     |     |
k trate as a function of only one variable; e.g., A1 is rate-
based(RB)whileA2isbuffer-based(BB).
| Figure     | 3:  | Formulation |         |     | for    | QoE maximization |            |                                                        |     |     |     |     |     |     |
| ---------- | --- | ----------- | ------- | --- | ------ | ---------------- | ---------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| (QOE_MAXK) |     |             | subject | to  | buffer | and              | throughput |                                                        |     |     |     |     |     |     |
|            |     | 1           |         |     |        |                  |            | ferentalgorithmsperformwithastate-of-artpredictorunder |     |     |     |     |     |     |
dynamics.
avarietyofvariabilityconditions.
Now,differentadaptationalgorithmsessentiallyadoptdif-
| QoEmaximizationproblem: |     |     |     |     | Wearenowreadytoformu- |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
latetheproblemofbitrateadaptationforQoEmaximization ferentfunctionsf(·).Specifically,twomaincategoriesofal-
QOE_MAXK. gorithmsappearintheliterature:rate-based(RB)andbuffer-
| as         | in Figure     | 3, denoted |            | as                            |            | 1 Given   | through- |                                            |     |     |                                  |     |     |     |
| ---------- | ------------- | ---------- | ---------- | ----------------------------- | ---------- | --------- | -------- | ------------------------------------------ | --- | --- | -------------------------------- | --- | --- | --- |
|            |               |            |            |                               |            |           |          | based(BB)algorithms.                       |     |     | RBstrategiesessentiallychoosebi- |     |     |     |
| puttrace{C |               | ,t∈[t      | ,t         | ]}asinput,theoptimizationpro- |            |           |          |                                            |     |     |                                  |     |     |     |
|            |               | t          | 1 K+1      |                               |            |           |          | trateonlybasedonthroughputprediction,i.e., |     |     |                                  |     |     |     |
| vides      | the following |            | as output: |                               | 1) bitrate | decisions | R ,···,  |                                            |     |     |                                  |     |     |     |
1
| R   | ,and2)startuptimeT |     |         | .        |     |               |     |     |     | (cid:16) |               |         | (cid:17) |      |
| --- | ------------------ | --- | ------- | -------- | --- | ------------- | --- | --- | --- | -------- | ------------- | ------- | -------- | ---- |
| K   |                    |     |         | s        |     |               |     |     |     | {Cˆ      |               |         |          |      |
|     |                    |     |         | QOE_MAXK |     |               |     |     | R   | k =f     | t ,t>t k },{R | i ,i<k} | .        | (13) |
|     | Note that          | the | problem |          |     | is formulated | as- |     |     |          |               |         |          |      |
1
sumingthevideoplaybackhasnotstartedatthetimeofthis
|                           |     |     |     |        |     |                      |     | For example,                                   |     | a typical | RB strategy | is to | choose the | maxi- |
| ------------------------- | --- | --- | --- | ------ | --- | -------------------- | --- | ---------------------------------------------- | --- | --------- | ----------- | ----- | ---------- | ----- |
| optimizationsothestart-up |     |     |     | delayT |     | isadecisionvariable. |     |                                                |     |           |             |       |            |       |
|                           |     |     |     |        | s   |                      |     | mumpossiblebitratebelowthepredictedthroughput. |     |           |             |       |            |       |
However,thisQoEmaximizationcanalsotakeplaceduring Ontheotherhand,BBstrategiesadvocatedecisionmak-
| videoplaybackattimet |                                 |     |     | whenthenextchunktodownload |     |     |               |                                       |     |        |     |         |     |      |
| -------------------- | ------------------------------- | --- | --- | -------------------------- | --- | --- | ------------- | ------------------------------------- | --- | ------ | --- | ------- | --- | ---- |
|                      |                                 |     | k0  |                            |     |     |               | ingbasedonlyonbufferoccupancy,namely: |     |        |     |         |     |      |
| isk                  | andthecurrentbufferoccupancyisB |     |     |                            |     |     | . Inthiscase, |                                       |     |        |     |         |     |      |
|                      | 0                               |     |     |                            |     | k0  |               |                                       |     |        |     |         |     |      |
|                      |                                 |     |     |                            |     |     |               |                                       |     | R =f(B | ,{R | ,i<k}), |     | (14) |
we can drop the variable T s and denote the corresponding k k i
steadystateproblemasQOE_MAX_STEADYK.
|     |     |     |     |     |     |     | k0  | whileregardingthroughputvariationsasunmodeleddistur- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
3.3 Classes of Algorithms bances. For example, Huang et al., illustrate one roadmap
fordesigningBBalgorithms[33].
InthissectionwecharacterizeproblemQOE_MAXK and Note, however, that both classes of algorithms are dis-
1
describe existing bitrate adaptation algorithms within this carding possibly useful information as shown in Figure 4.
frameworktounderstandhowtheyrelatetooneanother. Consequently,bothareinprinciplesuboptimal. Ideally,we
TheprobleminFigure3isafinite-horizonstochasticop- want to use both buffer occupancy and throughput predic-
timal control problem. The source of randomness is in the tion, thereby considering a broader design space of bitrate
availablethroughputC .Attimet whentheplayerchooses adaptationstrategies,asshowninEq(12)andalgorithmA3
|     |     |     | t   |     | k   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bitrate R , only the past throughput {C ,t ≤ t } is avail- depictedinFigure4.
|     | k   |     |     |     |     | t   | k   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
able,whilethefuturevalues{C t ,t>t k }arenotknown. 4 Model Predictive Control Approach
|                         | However, | a throughput |     | predictor | can                     | be used | to obtain |     |         |         |     |            |     |     |
| ----------------------- | -------- | ------------ | --- | --------- | ----------------------- | ------- | --------- | --- | ------- | ------- | --- | ---------- | --- | --- |
|                         |          |              |     |           |                         |         |           | for | Optimal | Bitrate |     | Adaptation |     |     |
| predictionsdefinedas{Cˆ |          |              |     | ,t >      | t }. Basedonsuchpredic- |         |           |     |         |         |     |            |     |     |
|                         |          |              |     | t         | k                       |         |           |     |         |         |     |            |     |     |
tionandonbufferoccupancyinformation(whichisinstead Inthissection,wemakeacaseforaModelPredictiveCon-
knownprecisely),thebitratecontrollerselectsbitrateofthe trol (MPC) approach for bitrate adaptation and describe a
nextchunkk: concrete MPC-based workflow that can optimally combine
(cid:16) (cid:17) throughput prediction and buffer occupancy. We also de-
|     | R   | =f  | B ,{Cˆ | ,t>t | },{R | ,i<k} | . (12) |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ---- | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
k k t k i velop a robust MPC approach that can better handle errors
inthroughputpredictionunderhighlyvariablenetworkcon-
|        | The design | of        | effective | throughput |            | predictors | is an inter-   | ditions. |     |      |     |     |     |     |
| ------ | ---------- | --------- | --------- | ---------- | ---------- | ---------- | -------------- | -------- | --- | ---- | --- | --- | --- | --- |
| esting | research   | direction |           | in its     | own right. | In         | this paper, we |          |     |      |     |     |     |     |
|        |            |           |           |            |            |            |                | 4.1      | Why | MPC? |     |     |     |     |
focusonbitrateadaptationalgorithmsonlyandassumethat
predictors are given to us and are characterized in terms of First,weprovidetheintuitionbehindthechoiceofMPCin
their expected prediction errors. Namely, we focus on the oursetting.NotethatwecannotclaimthatMPCisnecessary
design of f(·) and on the effect of the prediction error on ortheoptimalchoiceinthespaceofallpossiblecontrolal-
theperformanceofthecomparedcontrolalgorithms. Inthe gorithms. OurgoalismerelytoarguethatMPCisanatural
followingsections,wewillsystematicallyevaluatehowdif- fitforthebitrateadaptationproblem.
329

Strawmansolutions: Aswesawbefore,bitrateadaptation Algorithm1VideoadaptationworkflowusingMPC
| is essentially |     | a stochastic | optimal | control |     | problem. | In this |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | ------- | ------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1: Initialize
respect, there are two candidate well-known control algo- 2: fork =1toK do
rithms:(1)Proportional-integral-derivative(PID)control[25]
3: ifplayerisinstartupphasethen
and(2)MarkovDecisionProcess(MDP)basedcontrol[21].
|     |     |     |     |     |     |     |     | 4:  | Cˆ        | =ThroughputPred(C |     |     |         | )   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | --- | ------- | --- | --- |
|     |     |     |     |     |     |     |     |     | [tk,tk+N] |                   |     |     | [t1,tk] |     |     |
While PID is computationally simpler compared to MPC, (cid:16) (cid:17)
|     |     |     |     |     |     |     |     |     | [R  | ,T ]=f | st  | R ,B | ,Cˆ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- |
it can only serve to stabilize the system and cannot explic- 5: k s m pc k−1 k [tk,tk+N]
itlyoptimizeourQoEobjective. Inaddition,PIDcontrolis 6: StartplaybackafterT seconds
s
designedtoworkincontinuoustimeandstatespaceandus- 7: elseifplaybackhasstartedthen
ingitinahighlydiscretesystemsuchasoursmayresultin 8: Cˆ =ThroughputPred(C )
|     |     |     |     |     |     |     |     |     | [tk,tk+N] |     |     |     | [t1,t | (cid:17)k] |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ----- | ---------- | --- |
performance degradation or instability [25]. Alternatively, (cid:16)
|     |     |     |     |     |     |     |     | 9:  | R   | =f  | R   | ,B ,Cˆ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
with MDP we could consider formulating the throughput k mpc k−1 k [tk,tk+N]
10: endif
| and | buffer | state transition |     | as Markov | processes, |     | and find |     |     |     |     |     |     |     |     |
| --- | ------ | ---------------- | --- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
theoptimalcontrolpolicyusingstandardalgorithmssuchas 11: Download chunk k with bitrate R k , wait till fin-
| value | iteration | or policy | iteration | [21]. | However, |     | this has a | ished |     |     |     |     |     |     |     |
| ----- | --------- | --------- | --------- | ----- | -------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
12: endfor
strongassumptionthatthroughputdynamicsfollowMarkov
| processes |     | and it is unclear |     | if this holds | in  | practice. | We re- |     |     |     |     |     |     |     |     |
| --------- | --- | ----------------- | --- | ------------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
gardthepotentialuseofMDPandanalysisofthethroughput
dynamicsasfuturework(seeSection8). paperisnottodesignapredictionmechanismbuttorely
|                                          |     |               |       |         |           |     |           | on   | existing | approaches. | Naturally, |                 | improving | the      | accu-  |
| ---------------------------------------- | --- | ------------- | ----- | ------- | --------- | --- | --------- | ---- | -------- | ----------- | ---------- | --------------- | --------- | -------- | ------ |
| Case                                     | for | MPC: Ideally, | given | perfect | knowledge |     | of future |      |          |             |            |                 |           |          |        |
|                                          |     |               |       |         |           |     |           | racy | of this  | prediction  | will       | improve         | the gains | achieved |        |
| throughputovertheentirehorizonofavideo[t |     |               |       |         |           | ,t  | ],the     |      |          |             |            |                 |           |          |        |
|                                          |     |               |       |         |           | 1   | K+1       | via  | MPC.     | That said,  | MPC        | can be extended |           | to be    | robust |
optimalbitrateR 1 ,··· ,R K andstartupdelayT s canbecal- toerrorsaswediscussbelow.
culatedinoneshotbysolvingtheoptimizationproblemfor
|     |        |                 |     |     |           |      |         | 2. Optimize: |         | ThisisthecoreoftheMPCalgorithm: |     |              |     |         | Given |
| --- | ------ | --------------- | --- | --- | --------- | ---- | ------- | ------------ | ------- | ------------------------------- | --- | ------------ | --- | ------- | ----- |
| the | entire | video QOE_MAXK. |     | In  | practice, | such | perfect |              |         |                                 |     |              |     |         |       |
|     |        |                 |     | 1   |           |      |         | the          | current | buffer occupancy                |     | B , previous |     | bitrate | R     |
|     |        |                 |     |     |           |      |         |              |         |                                 |     | k            |     |         | k−1   |
informationisnotavailable, makingitdifficulttofindsuch andthroughputpredictionCˆ
|                                           |     |     |     |     |     |     |     |     |     |     |     | [tk,t (cid:16)k+N] | ,findoptimalbitrate |     |          |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------------- | --- | -------- |
| optimalsolutionsusingofflineoptimization. |     |     |     |     |     |     |     |     |     |     |     |                    |                     |     | (cid:17) |
,Cˆ
Whileperfectinformationmaynotbeavailablefortheen- R k .Insteadystate,R k =f mpc R k−1 ,B k ,
[tk,tk+N]
tirefuture,itispossiblethatreasonablyaccuratethroughput
implementedbysolvingQOE_MAX_STEADYk+N−1.
k
predictioncanbeinsteadobtainedforashorthorizontothe Inthestart-upphase,italsooptimizesstart-uptimeT as
s
future [t ,t ]. The intuition here is that network condi- (cid:16) (cid:17)
|     | k   | k+N |     |     |     |     |     | [R  | ,T ] = | fst R | ,B  | ,Cˆ | ,   | implemented |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | ----------- | --- |
tions are reasonably stable on short timescales and usually k s mpc k−1 k [tk,tk+N]
QOE_MAXk+N−1.
donotchangedrasticallyduringashorthorizon(tensofsec- by solving If we ignore practical
k
onds) [51]. Based on this insight, we can run a QoE opti- detailsaboutcomputationaloverhead,wecansimplyuse
mizationusingthepredictioninthishorizon,applythefirst off-the-shelf solvers such as CPLEX to solve these dis-
| bitrateR |     | ,andmovethehorizonforwardto[t |     |     |     |     | ,t ]. |                                                  |     |     |     |     |     |     |     |
| -------- | --- | ----------------------------- | --- | --- | --- | --- | ----- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|          | k   |                               |     |     |     | k+1 | k+N+1 | creteoptimizationproblems.AswewillseeinSection5, |     |     |     |     |     |     |     |
Thisschemeisknownasmodelpredictivecontrol(MPC)or wedonotneedtoexplicitlysolvetheoptimizationprob-
receding horizon control [22]. MPC algorithms are widely lemwithinthevideoplayerinpractice.
usedindifferentdomains,rangingfromindustrialcontrolto
|     |     |     |     |     |     |     |     | 3. Apply: | StarttodownloadchunkkwithR |     |     |     | k   | andmovethe |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------------------- | --- | --- | --- | --- | ---------- | --- |
navigation. The general benefits of MPC are in that MPC horizonforward. Iftheplayerisinstart-upphase, wait
canutilizepredictionstooptimizeacomplexcontrolobjec- forT beforestartingplayback.
s
tiveonlineinadynamicalsystemunderconstraints.
Thisworkflowhasseveralqualitativeadvantagescompared
| 4.2 | Basic | MPC | Algorithm |     |     |     |     |                   |      |               |            |      |                 |         |      |
| --- | ----- | --- | --------- | --- | --- | --- | --- | ----------------- | ---- | ------------- | ---------- | ---- | --------------- | ------- | ---- |
|     |       |     |           |     |     |     |     | with buffer-based |      | (BB),         | rate-based | (RB) | as we           | discuss | be-  |
|     |       |     |           |     |     |     |     | low. First,       | this | MPC algorithm |            | uses | both throughput |         | pre- |
Algorithm1showsahigh-leveloverviewoftheworkflowof
|     |     |                     |     |        |          |     |           | dictionandbufferinformationinaprincipledway. |     |     |     |     |     | Second, |     |
| --- | --- | ------------------- | --- | ------ | -------- | --- | --------- | -------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- |
| MPC | for | bitrate adaptation. |     | In our | context, | the | algorithm |                                              |     |     |     |     |     |         |     |
comparedtopureRBapproaches,MPCsmoothsoutpredic-
| essentially |     | chooses | bitrate | R by | looking | N steps | ahead |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ------- | ---- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
k
|        |            |           |     |            |            |     |          | tion error | at each | step | and is | more robust | to  | prediction | er- |
| ------ | ---------- | --------- | --- | ---------- | ---------- | --- | -------- | ---------- | ------- | ---- | ------ | ----------- | --- | ---------- | --- |
| (i.e., | the moving | horizon), |     | and solves | a specific |     | QoE max- |            |         |      |        |             |     |            |     |
rors. Specifically,byoptimizingseveralchunksoveramov-
imizationproblem(thisdependsonwhethertheplayerisin
inghorizon,largepredictionerrorsforoneparticularchunk
| steadyorstartupphase)withthroughputpredictions{Cˆ |     |     |     |     |     |     | ,t∈ |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|       |         |     |     |                  |     |             |     | will have | lower | impact | on the | performance. |     | Third, | MPC |
| ----- | ------- | --- | --- | ---------------- | --- | ----------- | --- | --------- | ----- | ------ | ------ | ------------ | --- | ------ | --- |
| [t ,t | ]},orCˆ |     | .   | ThefirstbitrateR |     | isappliedby |     |           |       |        |        |              |     |        |     |
k k+N [tk,tk+N] k directly optimizes a formally defined QoE objective, while
| using | feedback | information |     | and the | optimization |     | process is |     |     |     |     |     |     |     |     |
| ----- | -------- | ----------- | --- | ------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
inRBandBBthetradeoffbetweendifferentQoEfactorsis
iteratedateachstepk. notclearlydefinedandthereforecanonlybeaddressedinan
Atiterationk,theplayermaintainsamovinghorizonfrom
adhocqualitativemanner.
chunkktok+N−1andcarriesoutthefollowingthreekey
|     |     |     |     |     |     |     |     | 4.3 | Robust | MPC |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
steps,asshowninAlgorithm1.
Cˆ
1. Predict: Predict throughput [tk,tk+N] for the next N The basic MPC algorithm assumes the existence of an ac-
chunksusingsomethroughputpredictor.Ourgoalinthis curatethroughputpredictor. However,incertainseverenet-
330

| workconditions, |     | e.g., | incellularnetworksorinprimetime |     |     |     |     |     |             |     |             |     |     |                 |     |
| --------------- | --- | ----- | ------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | --- | --------------- | --- |
|                 |     |       |                                 |     |     |     |     |     | BufferLevel | 1s  | BufferLevel | 2s  |     | BufferLevel 20s |     |
whentheInternetiscongested,suchaccuratepredictorsmay
|     |     |     |     |     |     |     |     |     | PrevBitrate | 350kbps | PrevBitrate | 350kbps | …   | PrevBitrate 3000kbps |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----------- | ------- | --- | -------------------- | --- |
|     |     |     |     |     |     |     |     |     | Throughput  | 350kbps |             |         |     | Throughput 3000kbps  |     |
not be available. For example, if the predictor consistently Throughput 600kbps
| overestimates | the | throughput, |     | it may | induce | high | rebuffer- |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ------ | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Offline Enumeration
ing. Tocounteractthepredictionerror,wedeveloparobust
…
| MPCalgorithm. |     |     |     |     |     |     |     |     | CPLEX |     | CPLEX |     |     | CPLEX |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | ----- | --- |
RobustMPCessentiallyoptimizestheworst-caseQoEas-
| suming | that the  | actual      | throughput | can     | take     | any value | in a   |     |     |     |     |     |     |     |     |
| ------ | --------- | ----------- | ---------- | ------- | -------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| range  | [Cˆ ,Cˆ ] | in contrast | to         | a point | estimate | Cˆ .      | Robust |     |     |     |     |     |     |     |     |
t t t Scenario BufferLevel PrevBitrate Throughput Optimal Bitrate
| MPC entails | solving | the | following | optimization |     | problem | at  |     |     |     |     |         |         |         |     |
| ----------- | ------- | --- | --------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | ------- | ------- | ------- | --- |
|             |         |     |           |              |     |         |     |     | 1   | 1s  |     | 350kbps | 350kbps | 350kbps |     |
timet togetbitrateR =f (R ,B ,[Cˆ,Cˆ]): 2 2s 350kbps 600kbps 600kbps
| k   |     |     | k robustmpc |     | k−1      | k   | t t  |     |        |     |     |          |          |          |     |
| --- | --- | --- | ----------- | --- | -------- | --- | ---- | --- | ------ | --- | --- | -------- | -------- | -------- | --- |
|     |     |     |             |     |          |     |      |     | …      | …   |     | …        | …        | …        |     |
|     |     |     |             |     |          |     |      |     | 50,000 | 20s |     | 3000kbps | 3000kbps | 3000kbps |     |
|     |     | max | min         |     | QoEk+N−1 |     | (15) |     |        |     |     |          |          |          |     |
k
|     | Rk,···,Rk+N−1Ct∈[Cˆ |     |     | t,Cˆ |     |     |     |     |     |     |     | Query Lookup |     |     |     |
| --- | ------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
t]
|     |     | s.t. |                      |     |     |     |      |     |     | Online Bitrate Adaptation |     |     |     |     |     |
| --- | --- | ---- | -------------------- | --- | --- | --- | ---- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
|     |     |      | Constraints(7)to(11) |     |     |     | (16) |     |     |                           |     |     |     |     |     |
Ingeneral,itmaybenon-trivialtosolvesuchamax-min Figure5: “FastMPC”idea: Weenumeratepossiblesce-
robustoptimizationproblem. Inourspecificcase,however, narios and create a table indexing the optimal decision
foreachscenario.
wecanprovethattheworstcasescenariotakesplacewhen
| the throughput |     | is at its | lower | bound | C = | Cˆ. Thus, | the |     |               |           |     |        |          |               |     |
| -------------- | --- | --------- | ----- | ----- | --- | --------- | --- | --- | ------------- | --------- | --- | ------ | -------- | ------------- | --- |
|                |     |           |       |       | t   | t         |     |     |               |           |     |        |          |               |     |
|                |     |           |       |       |     |           |     | •   | Computational | overhead: |     | First, | the high | computational |     |
implementationofrobustMPCisstraightforward.Insteadof
|                             |     |     |     |                        |     |     |     |     | overhead                    | of MPC   | is especially |               | problematic          | for low-end     |     |
| --------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --------------------------- | -------- | ------------- | ------------- | -------------------- | --------------- | --- |
| Cˆ,weusethelowestpossibleCˆ |     |     |     | astheinputtotheregular |     |     |     |     |                             |          |               |               |                      |                 |     |
| t                           |     |     |     | t                      |     |     |     |     | mobile                      | devices, | which         | are projected | to                   | be the dominant |     |
| MPCQoEmaximizationproblem.  |     |     |     | Formally,              |     |     |     |     |                             |          |               |               |                      |                 |     |
|                             |     |     |     |                        |     |     |     |     | videoconsumersgoingforward. |          |               |               | Sincethebitrateadap- |                 |     |
THEOREM 1. TherobustMPCcontrollerisequivalentto tation decision logic is called before the player starts to
the regular MPC taking the lower bound of throughput as downloadeachchunk,excessivedelayinthebitrateadap-
tationlogicwillnegativelyaffecttheQoEoftheplayer.
input,namely,
• Deployment:Sincewedonothaveaclosed-formorcom-
,[Cˆ ,Cˆ
R =f (R ,B ]) binatorial solution for the QoE maximization problem,
|     | k   | robustmpc |     | k−1 | k t | t   |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CPLEXorGurobi).
|     | =f  |     | (R ,B | ,Cˆ) |     |     |     |     | wewillneedtouseasolver(e.g., |                                       |     |     |     |     |     |
| --- | --- | --- | ----- | ---- | --- | --- | --- | --- | ---------------------------- | ------------------------------------- | --- | --- | --- | --- | --- |
|     |     | mpc | k−1   | k    | t   |     |     |     |                              |                                       |     |     |     |     |     |
|     |     |     |       |      |     |     |     |     | However,                     | itmaynotbepossibleforvideoplayerstobe |     |     |     |     |     |
PROOFSKETCH. Conceptually,QoEfunctionQoE(R,C) bundled with such solver capabilities; e.g., licensing is-
canbewrittenasthesumof3terms(g : totalvideoquality, sues may preclude distributing such software or it may
1
| g : total | quality | change, | g : | rebuffer | time), | in which | only |     |                                                     |     |     |     |     |     |     |
| --------- | ------- | ------- | --- | -------- | ------ | -------- | ---- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| 2         |         |         | 3   |          |        |          |      |     | requireadditionalpluginorsoftwareinstallationswhich |     |     |     |     |     |     |
therebuffertimetermdependsonthroughputC. Thus, posessignificantbarrierstoadoption[26].
max min QoE(R,C) From the above discussion, it is evident that the solution
R C∈[C,C] we develop should be lightweight and combinatorial (i.e.,
(cid:32) (cid:33) notsolvingaLPorILPonline). Assuch,inthissection,we
≡max g 1 (R)−λ×g 2 (R)− max µ×g 3 (R,C) address these two key practical issues by developing a fast
R
|     |     |     |     | C∈[C,C] |     |     |     | andlow-overheadFastMPCdesignthatdoesnotrequireany |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
explicitsolvercapabilitiesinthevideoplayer[48].
≡max QoE(R,C)
R
|                                       |          |     |            |     |           |           |     | 5.1 | High-Level |                | Idea | of         | FastMPC     |        |     |
| ------------------------------------- | -------- | --- | ---------- | --- | --------- | --------- | --- | --- | ---------- | -------------- | ---- | ---------- | ----------- | ------ | --- |
| As any                                | decrease | of  | throughput | C   | will lead | to longer | re- |     |            |                |      |            |             |        |     |
| buffertime,theminimumQoEisachievedatC |          |     |            |     |           | =C.       |     |     |            |                |      |            |             |        |     |
|                                       |          |     |            |     |           |           |     | At  | a high     | level, FastMPC |      | algorithms | essentially | follow | a   |
The one potential downside is that robust MPC is more table enumeration approach. Here, we do an offline step
|     |     |     |     |     |     |     |     | of  | enumerating | the | state-space | and | solve | each specific | in- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | ----- | ------------- | --- |
conservativethanregularMPCbyalwaysassumingthelow-
stance. Then,intheonlinestepwejustusethesestoredop-
| est throughput. |     | The degree | of  | conservativeness |     | here | natu- |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ---------------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
rally depends on how loose/tight the lower bound is. In timalcontroldecisionsmappedtothecurrentoperationcon-
|     |     |     |     |     |     |     |     | ditions. | That | is, the | algorithm | will | be reduced | to a simple |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------- | --------- | ---- | ---------- | ----------- | --- |
practice,weusemaximumpredictionerroroverthepastsev-
tablelookupindexedbythekeyvalueclosesttothecurrent
eralchunksasboundsinourimplementationandfindthatit
workswellinpractice(discussedinSection7). stateandtheoutputofthelookupistheoptimalsolutionfor
theselectedconfiguration.
| 5 Using | MPC | in  | Practice |     | — FastMPC |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inoursetting(Figure5),thestate-spaceisdeterminedby
Whilerate-basedandbuffer-basedalgorithmsneedrelatively thefollowingdimensions: (1)currentbufferlevel,(2)previ-
minorcomputations,thechallengewithMPCisthatweneed ousbitrateschosen,and(3)thepredictedthroughputforthe
to solve a discrete optimization problem at each time step. nextN chunks(i.e.,theplanninghorizon). Thus,FastMPC
Therearetwopracticalconcernshere: willentailenumeratingpotentialscenarioscapturingdiffer-
331

ent values for each dimension and solving the optimization and this seemed a natural choice. However, our conversa-
problemsoffline. tions with industry personnel revealed that almost all con-
Unfortunately, directly using this idea will be very inef- tentprovidersareswitchingtoHTML5-basedplayersbased
ficient as we have a high dimensional state space. For in- on the MPEG-DASH standard [16] and thus OSMF (based
stance, if we have 100 possible values for the buffer level, onFlashandwithdecreasingmarketshare)isunlikelytobe
10 possible bitrates, a horizon of size 5, and 1000 possi- aplatformwithreal-worldimpact. HavingchosenaDASH
blethroughputvalues,therewillbe1018 rowsinthetable!4 player, we qualitatively evaluated several implementations
Therearetwoobviousconsequencesofthislargestatespace. of the DASH standard (e.g., [23, 8, 43]). Unfortunately,
First,itmaynotbepracticaltoexplicitlystorethefulltable theserelyeitheroncustomclientsornichevideoplayerplat-
inthememory. Notethatthisisnotjustahypotheticalcon- forms. Giventheseconsiderations,wechosethedash.js
cern. If we need a practical implementation of this table frameworkasitisthereferenceopen-sourceimplementation
lookup in the dash.js player [1] it will mean very high fortheMPEG-DASHstandardandisactivelysupportedby
memory footprint along with large startup delay as the ta- leading industry participants [7]. We believe our prototype
ble needs to be downloaded to the player module. Second, effortswillalsoinformtheevolutionofthesestandardization
it will incur a non-trivial offline computation cost that may efforts.Forinstance,akeyrequirementforanycontrolalgo-
needtobererunastheoperatingconditionschange. rithmsistoknowthesize(inbytes)ofeachvideochunk,but
5.2 Optimizing FastMPC Performance thestandarddoesnotmandatethemanifesttoreportchunk
sizes,whichmaybeakeyshortcomingofthecurrentspeci-
| Next, we | present two | key optimizations |     | to make | the table | fication. |     |     |     |     |     |
| -------- | ----------- | ----------------- | --- | ------- | --------- | --------- | --- | --- | --- | --- | --- |
enumerationapproachtractable.
dash.jsoverview:Tounderstandourimplementationand
Compaction via binning: First, to address the offline ex- modifications,webeginwithsomebriefbackgroundonthe
plorationcost,ourinsightisthatwemaynotneedveryfine- architecture of the dash.js player. The key components
grained values for the buffer and the throughput levels. As arehighlightedinFigure6.
a consequence these values may be suitably coarsened into At a high level, the dash.js implementation separates
aggregate bins. Moreover, with binning we do not need high-levelvideostreamingfunctionalitiesfromlow-levelspe-
| to explicitly | store the | row keys | as these | are directly | com- |     |     |     |     |     |     |
| ------------- | --------- | -------- | -------- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
cificDASHstandardrelatedcomponents.Aswearenotpar-
puted from the bin row indices. The challenge here is to ticularly interested in standard-specific implementation, we
balancethegranularityofbinningandthelossofoptimality leave the code unmodified and only focus on the adaptive
inpractice.Inpractice,wefindthatusing100binsforbuffer streamingrelatedfunctions.
leveland100binsforthroughputpredictionsworkswelland Theclassesandfunctionsthatarekeytobitrateadaptation
yieldsnear-optimalperformance. andvideostreaminglogicareasfollows:
• BufferController:Thisclassprovidesfunctionsto
| Tablecompression: | Oursecondinsightisthatthedecision |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
managebufferlevelsoftheplayerbyrequestingnewseg-
| table learned                        | by the offline                             | computation |     | will have | signifi- |                                       |          |     |              |         |               |
| ------------------------------------ | ------------------------------------------ | ----------- | --- | --------- | -------- | ------------------------------------- | -------- | --- | ------------ | ------- | ------------- |
|                                      |                                            |             |     |           |          | mentsandmakingbitratechangedecisions. |          |     |              |         | Specifically, |
| cantstructure.                       | Specifically,theoptimalsolutionsforseveral |             |     |           |          |                                       |          |     |              |         |               |
|                                      |                                            |             |     |           |          | function                              | validate | is  | periodically | invoked | and calls     |
| similarscenarioswilllikelybethesame. |                                            |             |     | Thus,     | wecanex- |                                       |          |     |              |         |               |
getPlaybackQualityfunctioninAbrController
ploitthisstructureinconjunctionwiththebinningstrategyto
|     |     |     |     |     |     | classtofindoptimalbitrate. |     |     | Italsomaintainsavariable |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ------------------------ | --- | --- |
exploreasimplelosslesscompressionstrategyusingarun-
|                 |          |              |         |     |         | bufferLevel |     | to record | the current | buffer | occupancy |
| --------------- | -------- | ------------ | ------- | --- | ------- | ----------- | --- | --------- | ----------- | ------ | --------- |
| length encoding | to store | the decision | vector. | The | optimal |             |     |           |             |        |           |
oftheplayer,whichcanbeusedforbitratedecisions.
| decision | can then be retrieved | online | using | binary | search. |                  |     |      |                |     |                  |
| -------- | --------------------- | ------ | ----- | ------ | ------- | ---------------- | --- | ---- | -------------- | --- | ---------------- |
|          |                       |        |       |        |         | • AbrController: |     | This | class contains |     | the core bitrate |
Inpractice,weseethatwithcompressionthetableoccupies
|     |     |     |     |     |     | adaptationlogic. |     | Intheoriginaldash.jsimplementa- |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------------- | --- | --- | --- |
lessthan60kBwith100binsforbufferlevels,100binsfor
tion, arule-baseddecisionlogicisemployedtofindthe
throughputpredictionsand5bitratelevels.
bitrate.Specifically,DownloadRatioRuleselectsbi-
6 Implementation trate based on the “download ratio” (play time of last
chunkdividedbyitsdownloadtime);Ontheotherhand,
Inthissection,wedescribeourimplementationoftheMPC
approachinthedash.jsframework. InsufficientBufferRulechoosesbitratedepend-
Ourimplementation
ingonwhetherthebufferlevelhasreachedalowerlimit
isbasedonthedash.jsmasterbranch(v1.2.0release)as
recentlytoavoidrebuffers.Prioritiesareassignedtoeach
| itwasthestableversionatthetimeofdevelopment. |     |     |     |     | Webe- |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
lievethatourimplementationcanbeeasilyadaptedtofuture ruletoresolveconflictsandmakefinalbitratedecisions.
versions as we require minimal modifications (≈ 800 lines Modifications and extensions: We observed two imple-
ofJavaScript). Formoreinformationonthesourcecodeand mentationdetailsindash.jsthatwereproblematic. First,
demopleasevisitourdemopage[14]. thecodeperiodicallycallsthevalidatefunctiontocheck
thestatusofthebufferandcallfunctionsinAbrController
| Choiceofplayer: | Manyprioradaptivebitrateplayerswere |      |           |     |             |           |         |                 |           |             |             |
| --------------- | ----------------------------------- | ---- | --------- | --- | ----------- | --------- | ------- | --------------- | --------- | ----------- | ----------- |
|                 |                                     |      |           |     |             | to decide | if the  | current bitrate | should    | be changed. | Note        |
| prototyped      | using the Adobe                     | OSMF | framework |     | [34, 3, 12] |           |         |                 |           |             |             |
|                 |                                     |      |           |     |             | that this | implies | the bitrate     | decisions | are not     | always made |
4100bufferlevels×10bitrates×1000throughput1values
|     |     |     |     |     |     | at chunk | boundaries, | which | may lead | to delay | of execution |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | ----- | -------- | -------- | ------------ |
×···×1000throughput5values=1018entries. ofbitratedecisions,orevenredownloadingpreviouschunks.
332

3Mbps, to avoid trivial cases where picking the maxi-
Rule-Based
BufferController AbrController Decision Logic mumbitrateisalwaystheoptimalsolution.
2. Mobiledataset(HSDPA)[10]: TheHSDPAdatasetcon-
logging validate getPlaybackQuality FastMPC
sists of 30min of continuous 1s measurement of video
RB, BB, FESTIVE
streaming throughput of a moving device in Telenor’s
ThroughputPredictor
3G/HSDPAmobilewirelessnetworkinNorway.Weran-
Original dash.js Additional class/function domlypick1000throughputtracesfromthefulldataset.
Figure6:dash.jscodestructureandourmodifications 3. Syntheticdataset: Finallywealsouseasyntheticdataset
tosupplementtheaforementioneddatasets.Thethrough-
Second,thedash.jsdownloadsmultiplechunksinparal-
put is based on some hidden state S ∈ S modeling
lel even though chunks that are earlier in the video stream t
the number of users sharing a bottleneck link. The ac-
shouldideallybeprioritized.
tual throughput C follows a Gaussian distribution with
t
To address these concerns, we changed the bitrate de-
meanm andvarianceσ2,giventhevalueofhiddenstate
cision and chunk download process in dash.js code by s s
S =s. Wevaryboththestatetransitionprobabilityma-
making two key changes to BufferController class: t
trixaswellastheparametersm ,σ2togeneratetraces.
1) bitrate decisions are made at the start of each chunk, 2) s s
Figure7showsthethroughputcharacteristicsofallthree
chunk download is completely sequential, i.e., no concur-
datasets. Amongthreedatasets, throughputisthemoststa-
rentdownloadsofmultiplechunksareallowed. Thisallows
ble in broadband network and the most variable in mobile
abasicimplementationframeworkwhichisconsistentwith
network. Inotherwords,theHSPDAdatasetisagoodstress
ourmodelandotherproposedalgorithms.
test for our MPC approach that assumes the throughput is
With these fixes, we implemented different bitrate adap-
predictableonshorttimescales.
tationalgorithms(e.g.,FastMPC,BB,RB)byreplacingthe
Videoparameters:Weusethe“Envivio”videofromDASH-
original rule-based bitrate adaptation logic by our own im-
264 JavaScript reference client test page [6] which is 260s
plementation. TheFastMPCimplementationhasastaticta-
long, consisting of 65 4s chunks. The video is encoded by
ble that is used to index control decisions. We also imple-
H.264/MPEG-4 AVC codec in the following bitrate levels:
mentedaharmonicmeanbasedthroughputpredictionscheme
R = {350kbps,600kbps,1000kbps,2000kbps,3000kbps}.
basedonpriorwork[34],aswellasadditionalloggingfunc-
tions in the BufferController class to record a com- This is consistent with the requirement for YouTube video
bitratelevelsfor240p,360p,480p,720pand1080prespec-
plete log of the state of the player, including buffer level,
tively [15]. We set the buffer size to B = 30s. We as-
bitrates,rebuffertime,predicted/actualthroughput. max
sumeq(·)isanidentityfunction. AsadefaultQoEfunction,
7 Evaluation weusetheweightsλ = 1,µ = µ = 3000,meaning1-sec
s
rebuffer/start-uptimereceivesthesamepenaltyasreducing
In this section, we compare our approach against existing
thebitrateofachunkby3000kbps. Wealsorunsensitivity
rate- and buffer-based approaches using a combination of
experimentsthatvarytheQoEweights.
realplayerandsimulationexperiments. Wealsopresentmi-
crobenchmarks on the CPU and memory overhead of our 7.1.2 AlgorithmsandMetrics
FastMPCimplementation.
Adaptationalgorithms:Determiningtheoptimalalgorithm
7.1 Setup
within each class is difficult as it involves optimizing over
Webeginbydescribingkeyparameters:(1)throughputvari- an infinite-dimensional functional space. To this end, we
ability traces; (2) video-specific parameters; (3) configura- choose a widely adopted function form for each class of
tionsforvariousadaptationalgorithms;and(4)definitionof algorithms from prior work, and optimize the free param-
anormalizedQoEmetricthatweusethroughoutthissection. eters by empirical simulations based on a training dataset
containing100throughputtracesrandomlypickedacrossall
7.1.1 InputParameters
datasets. Weevaluatethefollowingalgorithms:
Throughputtraces: Ourgoalistoevaluatevariousbitrate 1. RB: The bitrate is picked as the maximum available bi-
adaptationapproachesusingrealisticnetworkvariabilitycon- tratewhichislessthanp=1timesthroughputprediction
ditions. Giventhepaucityoflarge-scalesustainedthrough- usingharmonicmeanofpast5chunks;
putmeasurementsoverseveraltensofseconds,however,we 2. BB:WeemploythefunctionsuggestedbyHuangetal[33],
useacombinationofexistingdatasetsandsyntheticmodels: where bitrate R k is chosen to be the maximum avail-
1. Broadbanddataset(FCC)[9]:TheFCCdatasetconsists ablebitratewhichislessthanr k =f(B k )withreservoir
ofmorethan1millionsetsofthroughputmeasurements, r =5sandcushionc=10s.
where each set contains six data points each represent- 3. FastMPC: We use a look-ahead horizon h = 5 with
ing average throughput during a 5s interval. We extract throughput predictions using harmonic mean of past 5
throughputtracesofthesameserverandclientIPaddress chunks; We use 100 bins for throughput prediction and
and concatenate these to match the length of the video. 100binsforbufferlevel.WealsoevaluatetheexactMPC
Forexperimentswerandomlypick1000oftheconcate- withperfectthroughputpredictionforthenext5chunks
nated traces whose average throughput is between 0 to insimulations(denotedasMPC-OPT).
333

|     | 1   |     |           |     |     | 1   |     |     |           |     |     | 1   |     |           |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --------- | --- |
| 0.8 |     |     |           |     | 0.8 |     |     |     |           |     |     | 0.8 |     |           |     |
| 0.6 |     |     |           |     | 0.6 |     |     |     |           |     |     | 0.6 |     |           |     |
| FDC |     |     |           |     | FDC |     |     |     |           |     | FDC |     |     |           |     |
| 0.4 |     |     | FCC       |     | 0.4 |     |     |     | FCC       |     |     | 0.4 |     | FCC       |     |
|     |     |     | HSDPA     |     |     |     |     |     | HSDPA     |     |     |     |     | HSDPA     |     |
| 0.2 |     |     | Synthetic |     | 0.2 |     |     |     | Synthetic |     |     | 0.2 |     | Synthetic |     |
|     | 0   |     |           |     |     | 0   |     |     |           |     |     | 0   |     |           |     |
0 1000 2000 3000 4000 5000 0 500 1000 1500 2000 −0.1 0 0.1 0.2 0.3 0.4
Mean Throughput (kbps) Standard Deviation of Throughput (kbps) Average Percentage Prediction Error
|         |           |                |     |     | Figure7: |                 | Characteristicsofdatasets |     |     |     |     |                     |                |     |     |
| ------- | --------- | -------------- | --- | --- | -------- | --------------- | ------------------------- | --- | --- | --- | --- | ------------------- | -------------- | --- | --- |
|         | 1         |                |     |     |          | 1               |                           |     |     |     |     | 1                   |                |     |     |
|         |           |                |     |     |          |                 |                           |     |     |     |     |                     |                |     |     |
|         | RB        |                |     |     |          | RB              |                           |     |     |     |     | RB                  |                |     |     |
| 0.8     |           |                |     |     | 0.8      |                 |                           |     |     |     |     | 0.8                 |                |     |     |
|         | BB        |                |     |     |          | BB              |                           |     |     |     |     | BB                  |                |     |     |
|         | FastMPC   |                |     |     |          | FastMPC         |                           |     |     |     |     | FastMPC             |                |     |     |
| FDC 0.6 | RobustMPC |                |     |     | FDC 0.6  | RobustMPC       |                           |     |     |     | FDC | 0.6 RobustMPC       |                |     |     |
|         | dash.js   |                |     |     |          | dash.js         |                           |     |     |     |     | dash.js             |                |     |     |
| 0.4     | FESTIVE   |                |     |     | 0.4      | FESTIVE         |                           |     |     |     |     | 0.4 FESTIVE         |                |     |     |
| 0.2     |           |                |     |     | 0.2      |                 |                           |     |     |     |     | 0.2                 |                |     |     |
|         | 0         |                |     |     |          | 0               |                           |     |     |     |     | 0                   |                |     |     |
|         | −0.5      | 0              | 0.5 | 1   |          | −0.5            |                           | 0   | 0.5 |     | 1   | −0.5                | 0              | 0.5 | 1   |
|         |           | Normalized QoE |     |     |          |                 | Normalized QoE            |     |     |     |     |                     | Normalized QoE |     |     |
|         |           | (a)FCCdataset  |     |     |          | (b)HSDPAdataset |                           |     |     |     |     | (c)Syntheticdataset |                |     |     |
Figure8: Realexperimentresultswithdifferentthroughputtraces
4. RobustMPC:Weassumethatthethroughputlowerbound NormalizedQoEmetric:WedefineanormalizedQoEmet-
|     | Cˆ  | Cˆ  |     | Cˆ  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is = /(1+err), where is obtained using har- ricasfollows.Foragiventhroughputtrace{C t ,t∈[t 1 ,t K+1 ]},
|     | t   | t   |     | t   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
monicmeanofpast5chunks,whilepredictionerrorerr theofflineoptimalQoE,denotedbyQoE(OPT),isthemax-
is the maximum absolute percentage error of the past 5 imum QoE that can be achieved with perfect knowledge of
|     |     |     |     |     |     |     |     | future | throughputs |     | over | the entire | horizon. | It can | be cal- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ---- | ---------- | -------- | ------ | ------- |
chunks.
|     |     |     |     |     |     |     |     |     |     |     |     | QOE_MAXK |     | 6   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
5. dash.js: The original implementation adopts a rule- culated by solving problem and provides
1
|                                                     |         |          |          |       |            |     |     | a     | theoretical                          | upper | bound | of achievable | QoE. | On  | the other |
| --------------------------------------------------- | ------- | -------- | -------- | ----- | ---------- | --- | --- | ----- | ------------------------------------ | ----- | ----- | ------------- | ---- | --- | --------- |
| based                                               | bitrate | decision | logic as | shown | in Section | 6.  | We  |       |                                      |       |       |               |      |     |           |
|                                                     |         |          |          |       |            |     |     | hand, | arealonlinealgorithmAselectsbitrateR |       |       |               |      |     | basedon   |
| keeptheoriginalbitrateadaptationlogicunmodified,but |         |          |          |       |            |     |     |       |                                      |       |       |               |      | k   |           |
currentthroughputpredictions{Cˆ
disable the multi-chunk downloading and allow the bi- ,t > t }withoutknow-
|     |     |     |     |     |     |     |     |     |     |     |     |     | t   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tratetoswitchonlyatchunkboundaries.5 ingtheentirefuture. WedenotetheonlineQoEachievedby
algorithmAbyQoE(A)anddefinenormalizedQoEofA(n-
| 6. FESTIVE[34]: |     | Thisrate-basedalgorithmbalancesboth |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
efficiency and stability, and incorporates fairness across QoE(A))foranalgorithmAas: n-QoE(A)= QoE(A) .
QoE(OPT)
playersbutthatisnotaconcerninthispaper.Weassume
|       |     |              |         |             |     |             |     | 7.2 | Real | Player |     | Evaluation |     |     |     |
| ----- | --- | ------------ | ------- | ----------- | --- | ----------- | --- | --- | ---- | ------ | --- | ---------- | --- | --- | --- |
| there | is  | no wait time | between | consecutive |     | chunk down- |     |     |      |        |     |            |     |     |     |
loads,andimplementFESTIVEwithouttherandomized First,wepresentemulationswiththerealplayersetupcom-
| chunkscheduling. |     | Notethatthisdoesnotnegativelyim- |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
paringourFastMPCapproachagainstseveralpriorapproaches.
pact the player QoE in single player case. Specifically, Ourbasicexperimentsetupconsistsoftwocomputers(Ubuntu
FESTIVE calculates the efficiency score depending on 12.04LTS)witha100Mbpsdirectnetworkconnectionemu-
p=1timesthroughputpredictionsusingharmonicmean
latingavideoclientandserver.ThevideoclientisaGoogle-
ofpast5chunks,aswellasastabilityscoreasafunction Chromewebbrowserforlinux(version39)withV8JavaScript
of the bitrate switches in the past 5 chunks. The bitrate enginewhilethevideoserverisasimpleHTTPserverbased
ischosentominimizestabilityscoreplusα = 12times on node.js (version 0.10.32). We use the linux tc tool
efficiencyscore. tothrottlethethroughputofthelinkbetweentwocomputers
|            |     |            |           |     |        |     |      | accordingtothethroughputtracesemployed. |     |     |     |     |     | WeuseEmu- |     |
| ---------- | --- | ---------- | --------- | --- | ------ | --- | ---- | --------------------------------------- | --- | --- | --- | --- | --- | --------- | --- |
| Throughput |     | predictor: | Note that | RB, | *-MPC, | and | FES- |                                         |     |     |     |     |     |           |     |
lab[49]tocarryoutseveralsuchexperimentsinparallel.
| TIVE | need | a good throughput | predictor. |     | Developing |     | good |     |     |     |     |     |     |     |     |
| ---- | ---- | ----------------- | ---------- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
predictorsfordifferentscenariosisoutsidethescopeofthe Figure8showtheCDFofnormalizedQoEoverthethree
paper. Buildingoninsightsfrompriorwork,weusethehar- sets of throughput traces. First, we see that existing algo-
rithmsachieveonly60-70%ofoptimalQoEconfirmingthat
monicmeanoftheobservedthroughputofthelast5chunks
because it is robust to outliers in per-chunk estimates [34]. thereisstilllargeroomtoimprovevideoQoE.Second,Ro-
WerevisitthisissueinSection8. bustMPC outperforms non-MPC algorithms in all datasets
|     |     |     |     |     |     |     |     | with | an  | improvement |     | in median | normalized | QoE | of 15%, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----------- | --- | --------- | ---------- | --- | ------- |
5This enables a consistent comparison of the algorithms 10%, and 5% in the FCC, HSDPA, and Synthetic datasets
| rather | than | conflate it with | other | artifacts | because | of  | paral- |     |     |     |     |     |     |     |     |
| ------ | ---- | ---------------- | ----- | --------- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
leldownloads. Wealsotestedtheoriginaldash.jswith- 6To make it tractable to compute this offline optimal,
outanymodification, butitsperformanceisworsethanour we assume it can pick bitrates from a continuous range
| modifiedversion(notshown). |     |     |     |     |     |     |     | [R  | ,R  | ].  |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                            |     |     |     |     |     |     |     |     | min | max |     |     |     |     |     |
334

| 1   |     |     |     |     |     | 1   |     |     |     |     | 1   |     |         |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
| 0.8 |     |     |     |     |     | 0.8 |     |     |     | 0.8 |     |     |         |     |
| 0.6 |     |     |     |     |     | 0.6 |     |     |     | 0.6 |     |     | RB      |     |
| FDC |     |     |     |     | FDC |     |     |     |     | FDC |     |     | BB      |     |
| 0.4 |     |     |     |     |     | 0.4 |     |     |     | 0.4 |     |     | FastMPC |     |
RobustMPC
| 0.2 |     |     |     |     |     | 0.2 |     |     |     | 0.2 |     |     | dash.js |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
FESTIVE
| 0   |     |     |     |     |     | 0   |     |     |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 500 1000 1500 2000 2500 3000 0 500 1000 1500 0 5 10 15 20 25 30
Average Bitrate (kbps) Average Bitrate Change (kbps/chunk) Total Rebuffer Time (s)
|     |     |     |     |     | Figure9: | DetailedperformanceforFCCdataset |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   |     |     |     |     |          | 1                                |     |     |     |     | 1   |     |     |     |

| 0.8 |     |     |     |     |     | 0.8 |     |     |     | 0.8 |     |     |         |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
| 0.6 |     |     |     |     |     | 0.6 |     |     |     | 0.6 |     |     | RB      |     |
| FDC |     |     |     |     | FDC |     |     |     |     | FDC |     |     | BB      |     |
| 0.4 |     |     |     |     |     | 0.4 |     |     |     | 0.4 |     |     | FastMPC |     |
RobustMPC
| 0.2 |     |     |     |     |     | 0.2 |     |     |     | 0.2 |     |     | dash.js |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
FESTIVE
| 0   |     |     |     |     |     | 0   |     |     |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 500 1000 1500 2000 2500 3000 0 500 1000 1500 0   5 10 15 20 25 30
Average Bitrate (kbps) Average Bitrate Change (kbps/chunk) Total Rebuffer Time (s)
|     |     |     |     | Figure10: |     | DetailedperformanceforHSDPAdataset |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
respectively. Third, weseesignificantimprovement(60+% Doingacross-datasetanalysis,weseethatthetaildistri-
mediannormalizedQoE)comparedwiththeoriginaldash.js butionsoftheoverallQoEshowdifferentcharacteristics. In
player. Finally,weseethatthebasicFastMPCismoresen- the FCC result, only 1% users experience normalized QoE
sitive to prediction errors than RobustMPC. While there is <0whileinHSPDAthisoccursin10%ofallcases.7 Again,
no difference between Fast- and RobustMPC on FCC and themainreasonisthatthehighvariabilityofmobilenetwork
Synthetic results, the difference is especially visible in the induceslongrebufferingwhichaffectstheoverallQoE.
HSPDAresultwhereregularFastMPCsuffersandpresents Finally,eventhoughFESTIVEisarate-basedalgorithm,
nogainsversusRBandBB. it performs slightly worse than regular RB in our datasets
becauseitputsahigherweightonstabilityandswitchesup
| To better | understand |     | the | impact of | prediction | error, | Fig- |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --------- | ---------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
ure7showstheCDFofper-sessionaveragepercentagepre- bitrateslowlyevenwhentheavailablethroughputisincreas-
diction errors for the datasets. In FCC dataset, the average ing.8 Ontheotherhand,thedash.jsheuristicrule-based
errorofourharmonicmeanthroughputpredictorislessthan adaptation achieves low rebuffer time, but incurs many un-
|           |          |     |          |                |     |            |     | necessary | switches. | Thus, | its overall | QoE | is significantly |     |
| --------- | -------- | --- | -------- | -------------- | --- | ---------- | --- | --------- | --------- | ----- | ----------- | --- | ---------------- | --- |
| 5%, while | in HSPDA |     | dataset, | the worst-case |     | prediction | er- |           |           |       |             |     |                  |     |
rorcanbeashighas40%.Wealsoobservethatthepredictor worsethanallalgorithms.
over-estimatesthetruethroughputformorethan20%ofthe 7.3 Sensitivity Analysis
| time in | HSPDA | dataset | which | leads | to significant | rebuffer- |     |     |     |     |     |     |     |     |
| ------- | ----- | ------- | ----- | ----- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Forsensitivityanalysisweevaluatedifferentalgorithmsus-
| ing. As | such,      | inaccurate | prediction |                 | can ruin | the decision |          |                                |     |     |     |                     |     |     |
| ------- | ---------- | ---------- | ---------- | --------------- | -------- | ------------ | -------- | ------------------------------ | --- | --- | --- | ------------------- | --- | --- |
|         |            |            |            |                 |          |              |          | ingacustomsimulationframework. |     |     |     | Asbefore,thesimula- |     |     |
| making  | of regular | FastMPC,   |            | while RobustMPC |          | is           | less af- |                                |     |     |     |                     |     |     |
fected as it incorporates prediction error to avoid choosing tiontakesasinputathroughputtraceandmodelsthevideo
|     |     |     |     |     |     |     |     | download/playback |     | process | and the | buffer | dynamics. | At  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ------- | ------ | --------- | --- |
bitratetooaggressivelywhenpredictionsareinaccurate.
|                                   |         |            |         |            |                 |               |       | time t                                        | when the    | bitrate    | of chunk        | k is needed, | the            | simula- |
| --------------------------------- | ------- | ---------- | ------- | ---------- | --------------- | ------------- | ----- | --------------------------------------------- | ----------- | ---------- | --------------- | ------------ | -------------- | ------- |
| The earlier                       |         | normalized | QoE     | result     | shows           | the aggregate |       | k                                             |             |            |                 |              |                |         |
|                                   |         |            |         |            |                 |               |       | tion calls                                    | the bitrate | controller | embedded        |              | with different | al-     |
| combinationofdifferentQoEfactors. |         |            |         |            | Next,wezoominon |               |       |                                               |             |            |                 |              |                |         |
|                                   |         |            |         |            |                 |               |       | gorithms                                      | to get      | R . Using  | this framework, |              | we study       | the     |
| the individual                    |         | quality    | factors | to explain | the             | QoE improve-  |       |                                               |             | k          |                 |              |                |         |
|                                   |         |            |         |            |                 |               |       | sensitivityoftheapproachestokeyfactorssuchas: |             |            |                 |              | (1)pre-        |         |
| ments in                          | Figures | 9 and      | 10.     | In the     | FCC dataset,    | all           | algo- |                                               |             |            |                 |              |                |         |
dictionerror,(2)choiceofQoEfunction,(3)playoutbuffer
| rithms achieve |     | similarly | low | rebuffer | time as | throughput | is  |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
size,(4)numberofbitratelevels,and(5)startupdelay.
| predictable. | The | performance |     | difference | essentially |     | stems |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ---------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
from reducing unnecessary bitrate switches. RobustMPC, Throughputprediction:Here,wewanttostudytheimpact
FastMPC and BB achieve similar average bitrates, but Ro- ofpredictionerrorofgeneralpredictorsratherthananalyze
|         |      |       |         |           |        |       |     | aparticularone(e.g.,harmonicmean). |     |     |     | Tothisend,weuse |     |     |
| ------- | ---- | ----- | ------- | --------- | ------ | ----- | --- | ---------------------------------- | --- | --- | --- | --------------- | --- | --- |
| bustMPC | uses | fewer | bitrate | switches. | In the | HSPDA | re- |                                    |     |     |     |                 |     |     |
theaverageerrorleveltocharacterizetheperformanceofa
| sult, rebuffer | time | becomes |     | a more important |     | issue. | While |     |     |     |     |     |     |     |
| -------------- | ---- | ------- | --- | ---------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
FastMPCachievessimilaraveragebitrateandfewerswitches throughputpredictorandmodelthepredictionoutputasbe-
comparingtoBB,itsuffersfromlargerebuffertime. Onthe ingacombinationofthetruethroughputwithaddedrandom
|             |           |     |          |             |     |               |     | noiseaccordingtotheaverageerrorlevel. |     |     |     |     | Figure11ashows |     |
| ----------- | --------- | --- | -------- | ----------- | --- | ------------- | --- | ------------------------------------- | --- | --- | --- | --- | -------------- | --- |
| other hand, | RobustMPC |     | achieves | significant |     | less rebuffer |     |                                       |     |     |     |     |                |     |
time but at a slightly lower average bitrate: Zero rebuffer 7TheQoEcanbenegativewhenrebuffertimeistoolongor
| in 65% | of all | cases, | versus | 40% for | BB and | FastMPC. | As  |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
therearetoomanyswitches.
a result, RobustMPC still outperforms other algorithms in 8This is not a flaw, but a deliberate choice for achieving
| overallQoE. |     |     |     |     |     |     |     | multi-playerfairness[34]. |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
335

| 1   |     |     |     |     | 1   |     |     |   1 |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MPC−OPT
| 0.95       |     |     |     |       | 0.9 |     | FastMPC |       |     |     |     |       |     |     |
| ---------- | --- | --- | --- | ----- | --- | --- | ------- | ----- | --- | --- | --- | ----- | --- | --- |
|            |     |     |     |       | 0.8 |     | BB RB   | 0.8   |     |     |     | 0.9   |     |     |
| 0.9        |     |     |     |       | 0.7 |     |         |       |     |     |     |       |     |     |
|            |     |     |     |       |     |     |         | 0.6   |     |     |     | 0.8   |     |     |
| EoQ−n 0.85 |     |     |     | EoQ−n | 0.6 |     |         | EoQ−n |     |     |     | EoQ−n |     |     |
0.5
0.8
|      |     |     |     |     | 0.4 |     |     | 0.4 |     |         |     | 0.7   |     |         |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- | --- | ------- |
| 0.75 |     |     |     |     | 0.3 |     |     |     |     | MPC−OPT |     |       |     |         |
|      | MPC |     |     |     |     |     |     |     |     | FastMPC |     |       |     | MPC−OPT |
|      | BB  |     |     |     | 0.2 |     |     | 0.2 |     | BB      |     | 0.6   |     | FastMPC |
| 0.7  | RB  |     |     |     |     |     |     |     |     | RB      |     |       |     | BB      |
|      |     |     |     |     | 0.1 |     |     |     |     |         |     |       |     | RB      |
| 0.65 |     |     |     |     | 0   |     |     | 0   |     |         |     | 0.5   |     |         |
0.1 0.2 0.3 0.4 0.5 Balanced Avoid Instability Avoid Rebuffering 10 20 30 40 50 2 4 6 8 10
Prediction Error QoE Preference Buffer Size (s) Startup Time (s)
(a)Predictionerror (b)QoEpreferences (c)Buffersize (d)Startuptime
|     |     |     |     | Figure11: |     | Sensitivityanalysisvs.operatingconditions |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
how the throughput prediction errors influence the perfor- inthebufferatthestart-upphasemakingiteasiertomanage
mance of bitrate adaptation algorithms. As expected, BB rebufferingevents.
isunaffectedasitdoesnotuseanythroughputinformation.
|     |     |     |     |     |     |     |     | Bitrate | levels: | We also | study | how number | of  | bitrate levels |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ----- | ---------- | --- | -------------- |
When throughput predictions are accurate, MPC has larger influencestheperformance(notshown).WithBBandMPC,
| advantage | over | BB algorithms. |     | As  | prediction | error | grows |     |     |     |     |     |     |     |
| --------- | ---- | -------------- | --- | --- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
wecanachievebetterperformanceusingfiner-grainedsetof
| beyond | 25%, | MPC can | be  | even worse | than | BB. | This sug- |         |         |      |              |     |             |       |
| ------ | ---- | ------- | --- | ---------- | ---- | --- | --------- | ------- | ------- | ---- | ------------ | --- | ----------- | ----- |
|        |      |         |     |            |      |     |           | bitrate | levels. | With | RB, however, | the | performance | of RB |
geststhatiftheactualpredictionerrorisverylarge,thenthe first improves as we add more bitrate levels, but decreases
| video | player | should drop | RB  | or MPC | and | use pure | BB  | al- |     |     |     |     |     |     |
| ----- | ------ | ----------- | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
whentherearetoomanybitratelevels.ThereasonisthatRB
| gorithms. | IncontrastwithregularMPC,robustMPCisless |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
startschangingbitratemorefrequently,leadingtoincreased
affectedbypredictionerrorasittakesintopossibleerrorinto
|     |     |     |     |     |     |     |     | bitrateinstability. |     | OnecaveatwithMPCisthatfiner-grained |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------------------------------- | --- | --- | --- | --- |
accountandmaximizestheworstcaseQoE. bitrate levels also require more discretization levels for the
Users’ QoE preferences: We compared the performance FastMPCimplementation. Understandingthistradeoffisan
of the algorithms under 3 sets of QoE weights, “Balanced” interestingdirectionforfuturework.
(λ = 1,µ = µ s = 3000), “Avoid Instability” (λ = 3,µ = 7.4 MPC Configuration and Overhead
| µ =3000),“AvoidRebuffering”(λ=1,µ=µ |     |     |     |     |     |     | =6000). |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| s                                   |     |     |     |     |     |     | s       |     |     |     |     |     |     |     |
AsshowninFigure11b,asusersputmorepenaltyweightsto Overhead: As discussed earlier, FastMPC might increase
bitrateinstability,theMPCalgorithmsshowmoreadvantage playeroverheadrelativetoBBandRBstylealgorithms. We
overRBandBB.ThisisbecauseMPCalgorithmsexplicitly compare the CPU and memory usage of our implementa-
model the bitrate vs. bitrate instability tradeoff in the QoE tion of FastMPC, BB, and RB algorithm with the default
function,whileRBandBBdosoinad-hocways. However, dash.js player. We find that FastMPC, BB, and RB all
whenrebufferingtimeisamoreimportantfactor,BBalgo- consumesimilaramountofCPU,whileFastMPCusesonly
rithmsperformsimilarlywithFastMPCalgorithmsbecause 60kBmorememory(notshown).
| of two | key | reasons. | First, BB | algorithms |     | keep | a minimum |         |                 |     |        |      |            |         |
| ------ | --- | -------- | --------- | ---------- | --- | ---- | --------- | ------- | --------------- | --- | ------ | ---- | ---------- | ------- |
|        |     |          |           |            |     |      |           | FastMPC | discretization: |     | Recall | that | the number | of dis- |
buffer level so that the player has a better chance surviv- cretizationlevelsisanimportantdesignparameterforFastMPC.
ing low throughput with less/no rebuffering time. Second, More discretization levels increase FastMPC performance
whileMPCalgorithmsdoagoodjobwithperfectthrough-
butrequiremoreplayermemoryandmayalsoincreasestartup
| put prediction, |     | they | can suffer | from | long | rebuffering | time |        |          |      |             |     |          |          |
| --------------- | --- | ---- | ---------- | ---- | ---- | ----------- | ---- | ------ | -------- | ---- | ----------- | --- | -------- | -------- |
|                 |     |      |            |      |      |             |      | delay. | We study | this | performance | vs. | overhead | tradeoff |
sinceharmonicmeanpredictorisimperfect. Assuch,MPC in Figure 12a and Table 1. From Figure 12a, we see that
canbeimprovedbymaintainingaminimumbufferleveland
|     |     |     |     |     |     |     |     | more | discretization | levels | imply | larger | performance | gains |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ------ | ----- | ------ | ----------- | ----- |
employingamoreaccuratepredictor.
forFastMPCbuttheimprovementshowsdiminishingreturn;
e.g.,FastMPCachieves90%ofoptimalQoEwith100levels
| Buffer | size       | and startup | delay: |        | Figure | 11c analyzes |      | the   |            |        |          |          |           |         |
| ------ | ---------- | ----------- | ------ | ------ | ------ | ------------ | ---- | ----- | ---------- | ------ | -------- | -------- | --------- | ------- |
|        |            |             |        |        |        |              |      | while | this drops | to 70% | if there | are only | 5 levels. | Second, |
| impact | of playout | buffer      | size.  | First, | when   | buffer       | size | is    |            |        |          |          |           |         |
small (<25s in play time), increasing buffer size improves the gain vs. discretization level also has some dependency
the performance of all algorithms. A larger buffer protects onthethroughputpredictorespeciallywithverycoarsedis-
|     |     |     |     |     |     |     |     | cretization. | Table1showsthatwhilethememoryoverhead |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------------------------- | --- | --- | --- | --- | --- |
theplayeragainstrebufferingeventsandalsoprovidesmore
| degreesoffreedomtooptimizeperformance. |     |     |     |     |     | Asbuffersize    |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| reachesacertainlevel(25sofplaytime),   |     |     |     |     |     | theperformances |     |     |     |     |     |     |     |     |
ExtraJavaScriptcodesize
ofallalgorithmsstayconstantevenbuffersizeisfurtherin-
Discretizationlevels
creased. Finally, RB is the least affected by buffer size be- Fulltable Runlengthcoding
causeitdoesnotconsiderbufferlevelinitsdecisionlogic.
|     |     |     |     |     |     |     |     |     | 50  |     | 25.0kB |     | 19.1kB |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- |
Whileourapproachoptimizesstartupdelayautomatically,
|     |     |     |     |     |     |     |     |     | 100 |     | 100kB |     | 56.4kB |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- |
weanalyzehowoverallQoE(exceptthestartupdelayterm)
|             |     |                |            |     |                 |          |         |     | 200 |     | 400kB  |     | 141kB |     |
| ----------- | --- | -------------- | ---------- | --- | --------------- | -------- | ------- | --- | --- | --- | ------ | --- | ----- | --- |
| is affected |     | if the startup | delay      | is  | fixed.          | As shown | in Fig- |     |     |     |        |     |       |     |
|             |     |                |            |     |                 |          |         |     | 500 |     | 2.50MB |     | 451kB |     |
| ure 11d,    | as  | startup time   | increases, |     | the performance |          | of      | all |     |     |        |     |       |     |
algorithmsimproves,astheplayeraccumulatesmorevideo Table1: FastMPCtablesize
336

|     |     |     |     |     |     |     | Throughputprediction: |     |     | Asobservedbyotherresearchers, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ----------------------------- | --- | --- | --- |
FastMPC + Perfect Prediction 0.95   betterthroughputpredictioncanimprovevideoperformance
FastMPC + Harmonic Mean
| 1   |     |     |   0.94 |     |     |     |                                                    |          |       |       |            |        |         |
| --- | --- | --- | ------ | --- | --- | --- | -------------------------------------------------- | -------- | ----- | ----- | ---------- | ------ | ------- |
|     |     |     |        |     |     |     | in cellular                                        | networks | [52]. | A key | limitation | of our | work is |
| 0.8 |     |     | 0.93   |     |     |     | thatwedonothaveaccuratealgorithmsforthroughputpre- |          |       |       |            |        |         |
EoQ−n 0.92 dictionandtheliteratureissurprisinglyscarceanddated[30,
EoQ−n 0.6
0.91
51,20]. Twointerestingdirectionsoffutureworkareinus-
| 0.4 |     |     | 0.9 |     |     |                  |                                                  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | MPC, Error = 10% | ingcrowdsourcedapproachesbasedonmeasurementsfrom |     |     |     |     |     |     |
| 0.2 |     |     |     |     |     | MPC, Error = 15% |                                                  |     |     |     |     |     |     |
0.89 MPC, Error = 20% other clients [41] and developing a better understanding of
| 0   |     |     | 0.88 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5 10 50 100 500 2 3 4 5 6 7 8 9 throughputpredictabilityandstabilityinthewild.
|                   | FastMPC Discretization Levels |     |     | Look−Ahead Horizon (chunk) |     |     |     |     |     |     |     |     |     |
| ----------------- | ----------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (a)Discretization |                               |     |     | (b)Look-aheadhorizon       |     |     |     |     |     |     |     |     |     |
9 Conclusions
| Figure12: | MPCconfigurationparameters |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ourpaperwasmotivatedbyrecentdebatessurroundingthe
|     |     |     |     |     |     |     | design of | dynamic | adaptive | streaming | over | HTTP | (DASH) |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------- | --------- | ---- | ---- | ------ |
increaseswithmorelevels,thesimplecompressionscheme algorithms. Tobringsomerigortothisspace,wedeveloped
wediscussedearliercanreducethememoryoverheadespe-
|     |     |     |     |     |     |     | a control-theoretic |     | problem | formulation | that | allowed | us to |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | ----------- | ---- | ------- | ----- |
ciallywhennumberoflevelsislarge. Forinstance,with100 explore the design space systematically and evaluate quan-
levelsthecompressionrateis0.5whilewith500levelsitcan titativelydifferentclassesofsolutionsthroughwell-defined
reducethetablesizeby82%.Evenwith500levels,thetable
|     |     |     |     |     |     |     | QoE metrics. |     | With the | key insights | that a | broader | design |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------ | ------ | ------- | ------ |
sizeisquitereasonablylow. space is available compared to existing solutions, we de-
signedandimplementedamodelpredictivecontrolapproach
Look-aheadhorizon:Figure12bshowshowplanninghori-
tooptimallycombinebufferoccupancyandthroughputpre-
| zon impacts | the performance |     | of MPC | algorithms. |     | As the |          |          |             |     |             |     |        |
| ----------- | --------------- | --- | ------ | ----------- | --- | ------ | -------- | -------- | ----------- | --- | ----------- | --- | ------ |
|             |                 |     |        |             |     |        | dictions | in order | to maximize | the | user’s QoE. | We  | demon- |
look-aheadhorizonincreases,MPCperformancesgrowand
stratedapracticalimplementationofMPCusingthedash.js
| stay stable       | since more | information                       |     | of future | throughput | is  |           |       |         |                  |            |     |       |
| ----------------- | ---------- | --------------------------------- | --- | --------- | ---------- | --- | --------- | ----- | ------- | ---------------- | ---------- | --- | ----- |
|                   |            |                                   |     |           |            |     | reference | video | player. | Our trace-driven | emulations |     | using |
| takenintoaccount. |            | However,aswelookfurtherintothefu- |     |           |            |     |           |       |         |                  |            |     |       |
ture, prediction accuracy can reduce. The performance of realistic throughput variability traces confirmed the advan-
tagesoverstateoftheartsolutionsinawiderangeofoper-
MPCcanevendropifthehorizonistoolarge.
atingconditionswithnegligibleincreaseincomputationand
7.5 Summary of Results memory requirements. As future work, we plan to incor-
|     |     |     |     |     |     |     | porate more | accurate | throughput | predictions |     | and | explicitly |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---------- | ----------- | --- | --- | ---------- |
Ourmainfindingsaresummarizedasfollows:
capturemulti-playerinteractions.
1. RobustMPCoutperformsexistingalgorithmsinbothbroad-
band(FCC)andcellular(HSDPA)datasets,whileregular Acknowledgments
| FastMPC | does not | show | advantage | in  | cellular | network |           |     |           |         |                 |     |         |
| ------- | -------- | ---- | --------- | --- | -------- | ------- | --------- | --- | --------- | ------- | --------------- | --- | ------- |
|         |          |      |           |     |          |         | This work | was | supported | in part | by the National |     | Science |
duetohighthroughputinstability;
FoundationunderawardsECCS-0925964andCNS-1345305.
| 2. Our implementation |           | of FastMPC |              | algorithm | incurs | very   |                       |     |                             |                |     |         |        |
| --------------------- | --------- | ---------- | ------------ | --------- | ------ | ------ | --------------------- | --- | --------------------------- | -------------- | --- | ------- | ------ |
|                       |           |            |              |           |        |        | We thank              | our | shepherd                    | Keith Winstein | for | helping | us im- |
| low overhead:         | near-zero |            | CPU overhead |           | and 60 | kB in- |                       |     |                             |                |     |         |        |
|                       |           |            |              |           |        |        | provethefinalversion. |     | WethankAdityaGanjamandDavid |                |     |         |        |
creaseinmemoryusagecomparedtooriginaldash.js;
|     |     |     |     |     |     |     | Oran for | useful | discussions | regarding | industry | player | plat- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --------- | -------- | ------ | ----- |
3. SensitivityanalysisshowsthatFastMPChasadvantages
formsthatinformedourimplementation.
| over | BB and RB | in wide | parameter | ranges. | However, |     |     |     |     |     |     |     |     |
| ---- | --------- | ------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
thereisstillroomforimprovementbyincreasingFastMPC
10 References
| discretization | granularity |     | and employing |     | more | accurate |     |     |     |     |     |     |     |
| -------------- | ----------- | --- | ------------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
throughputpredictors.
[1] Dash-Industry-Forum,dash.js.
8 Discussion https://github.com/Dash-Industry-Forum/dash.js/wiki.
[2] AdobeHTTPDynamicStreaming.
Beforeconcluding,werevisittwooutstandingissues. www.adobe.com/products/hds-dynamic-streaming.html.
[3] AdobeOSMFplayer.http://www.osmf.org.
Multi-player effects: In this paper, we focused purely on [4] AkamaiHDnetwork.www.akamai.com/hdnetwork.
improving the design of a single video player. A natural [5] Apple’sHTTPLiveStreaming.
https://developer.apple.com/streaming/.
| question | is to extend | these insights |     | to multiple | players | and |     |     |     |     |     |     |     |
| -------- | ------------ | -------------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
interactionwithcrosstraffic[34,32].Tofullyconsidermulti- [6] DASH-264JavaScriptreferenceclientlandingpage1.4.0.
player interaction and fairness, we can extend our control- http://dashif.org/reference/players/javascript/1.4.0/samples/
theoreticmodeltoexplicitlyconsiderafairnessterminthe dash-if-reference-player/index.html.
[7] DASHIndustryForummembers.http://dashif.org/members/.
| QoE function | and model | the | effects | of TCP | on throughput |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[8] DASHVLCplugin.
| allocation. | For instance, | we  | might | be able | to reason | about |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ----- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
http://www-itec.uni-klu.ac.at/dash/?page_id=10.
| fairness | from the perspective |     | of game | theory | or distributed |     |     |     |     |     |     |     |     |
| -------- | -------------------- | --- | ------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[9] FCCdataset.
controltheoryinthiscontext.Thisisaninterestingdirection https://www.fcc.gov/measuring-broadband-america.
| forfutureresearch. |     |     |     |     |     |     | Accessed:2014-12-01. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
337

[10] HSDPAdataset. EvidencefromaLargeVideoStreamingService.InProc.
http://home.ifi.uio.no/paalh/dataset/hsdpa-tcp-logs. ACMSIGCOMM,2014.
Accessed:2014-12-01. [34] J.Jiang,V.Sekar,andH.Zhang.ImprovingFairness,
[11] Netflix.http://www.netflix.com/. Efficiency,andStabilityinHTTP-basedAdaptiveVideo
[12] OSMF2.0releasecode.http: StreamingwithFESTIVE.InProc.CoNext,2012.
//sourceforge.net/projects/osmf.adobe/files/latest/download. [35] S.S.KrishnanandR.K.Sitaraman.VideoStreamQuality
[13] SmoothStreamingprotocol. ImpactsViewerBehavior:InferringCausalityusing
http://go.microsoft.com/?linkid=9682896. Quasi-ExperimentalDesigns.InProc.IMC,2012.
[14] ThedemopageforourMPC-basedbitrateadaptation. [36] R.Kuschnig,I.Kofler,andH.Hellwagner.Evaluationof
http://users.ece.cmu.edu/~vsekar/mpcdash.html. HTTP-basedRequest-ResponseStreamsforInternetVideo
[15] YouTubeliveencodersettings,bitratesandresolutions. Streaming.MultimediaSystems,pages245–256,2011.
https://support.google.com/youtube/answer/2853702?hl=en. [37] L.DeCicco,S.Mascolo,andV.Palmisano.Feedback
[16] I.Sodagar. TheMPEG-DASHStandardforMultimedia ControlforAdaptiveLiveVideoStreaming.InProc.ofACM
StreamingOvertheInternet.IEEEMultimedia,2011. MultimediaSystemsConference,2011.
[17] S.Akhshabi,L.Anantakrishnan,C.Dovrolis,andA.C. [38] Z.Li,X.Zhu,J.Gahm,R.Pan,H.Hu,A.Begen,and
Begen.WhatHappenswhenHTTPAdaptiveStreaming D.Oran.ProbeandAdapt:RateAdaptationforHTTPVideo
PlayersCompeteforBandwidth?InProc.NOSSDAV,2012. StreamingatScale.SelectedAreasinCommunications,
[18] S.Akhshabi,L.Ananthakrishnan,A.Begen,and
IEEEJournalon,32(4):719–733,2014.
C.Dovrolis. Server-BasedTrafficShapingforStabilizing [39] C.Liu,I.Bouazizi,andM.Gabbouj.ParallelAdaptive
OscillatingAdaptiveStreamingPlayers.InProc.ACM HTTPMediaStreaming.InProc.ICCCN,2011.
SIGMMNOSSDAV,2013. [40] H.Liu,Y.Wang,Y.R.Yang,A.Tian,andH.Wang.
[19] A.Balachandran,V.Sekar,A.Akella,S.Seshan,I.Stoica, OptimizingCostandPerformanceforContentMultihoming.
andH.Zhang.DevelopingaPredictiveModelofQualityof InProc.ACMSIGCOMM,2012.
ExperienceforInternetVideo.InProc.ACMSIGCOMM, [41] X.Liu,F.Dobrian,H.Milner,J.Jiang,V.Sekar,I.Stoica,
2013. andH.Zhang.ACaseforaCoordinatedInternetVideo
[20] H.Balakrishnan,M.Stemm,S.Seshan,andR.H.Katz. ControlPlane.InProc.ACMSIGCOMM,2012.
AnalyzingStabilityinWideAreaNetworkPerformance.In [42] R.K.P.Mok,X.Luo,E.W.W.Chan,andR.K.C.Chang.
Proc.ACMSIGMETRICS,1997. QDASH:AQoE-awareDASHsystem.InProc.MMSys,
[21] D.P.Bertsekas,D.P.Bertsekas,D.P.Bertsekas,andD.P. 2012.
Bertsekas.DynamicProgrammingandOptimalControl, [43] C.Mueller,S.Lederer,J.Poecher,andC.Timmerer.Libdash
volume1.AthenaScientificBelmont,MA,1995. -AnOpenSourceSoftwareLibraryfortheMPEG-DASH
[22] E.F.CamachoandC.B.Alba.ModelPredictiveControl. Standard.InProc.ICME,2013.
Springer,2013. [44] L.Popa,A.Ghodsi,andI.Stoica.HTTPastheNarrowWaist
[23] L.D.Cicco,V.Caldaralo,V.Palmisano,andS.Mascolo. oftheFutureInternet.InProc.HotNets,2010.
TAPAS:aToolforrApidPrototypingofAdaptiveStreaming [45] R.RejaieandJ.Kangasharju.Mocha:AQualityAdaptive
algorithms.InProc.CoNextVideoNextworkshop,2014. MultimediaProxyCacheforInternetStreaming.InProc.
[24] F.Dobrian,V.Sekar,A.Awan,I.Stoica,D.A.Joseph, NOSSDAV,2001.
A.Ganjam,J.Zhan,andH.Zhang.Understandingthe [46] S.Akhshabi,A.Begen,C.Dovrolis.AnExperimental
ImpactofVideoQualityonUserEngagement.InProc.ACM EvaluationofRateAdaptationAlgorithmsinAdaptive
SIGCOMM,2011. StreamingoverHTTP.InProc.MMSys,2011.
[25] G.F.Franklin,J.D.Powell,andM.L.Workman.Digital [47] G.TianandY.Li.TowardsAgileandSmoothVideo
ControlofDynamicSystems,volume3.Addison-wesley AdaptioninDynamicHTTPStreaming.InProc.CoNext,
MenloPark,1998. 2012.
[26] A.Ganjam,F.Siddiqui,J.Zhan,X.Liu,I.Stoica,J.Jiang, [48] Y.WangandS.Boyd.FastModelPredictiveControlusing
V.Sekar,andH.Zhang.C3:Internet-ScaleControlPlanefor OnlineOptimization.ControlSystemsTechnology,IEEE
VideoQualityOptimization.InProc.NSDI,2015. Transactionson,18(2):267–278,2010.
[27] M.Ghobadi,Y.Cheng,A.Jain,andM.Mathis.Trickle:Rate [49] B.White,J.Lepreau,L.Stoller,R.Ricci,S.Guruprasad,
LimitingYouTubeVideoStreaming.InProc.USENIXATC, M.Newbold,M.Hibler,C.Barb,andA.Joglekar.An
2012. IntegratedExperimentalEnvironmentforDistributed
[28] S.Gouache,G.Bichot,A.Bsila,andC.Howson.Distributed SystemsandNetworks.Proc.OSDI,2002.
andAdaptiveHTTPStreaming.InProc.ICME,2011. [50] X.Yin,V.Sekar,andB.Sinopoli.TowardaPrincipled
[29] D.Havey,R.Chertov,andK.Almeroth.ReceiverDriven FrameworktoDesignDynamicAdaptiveStreaming
RateAdaptationforWirelessMultimediaApplications.In AlgorithmsoverHTTP.InProc.ACMSIGCOMMHotNets,
Proc.MMSys,2012. 2014.
[30] Q.He,C.Dovrolis,andM.Ammar.OnthePredictabilityof [51] Y.ZhangandN.Duffield.OntheConstancyofInternetPath
LargeTransferTCPThroughput.InProc.ACMSIGCOMM, Properties.InIMW,2001.
2005. [52] X.K.Zou,J.Erman,V.Gopalakrishnan,E.Halepovic,
[31] R.HoudailleandS.Gouache.ShapingHTTPAdaptive R.Jana,X.Jin,J.Rexford,andR.K.Sinha.CanAccurate
StreamsforaBetterUserExperience.InProc.MMSys,2012. PredictionsImproveVideoStreaminginCellularNetworks?
[32] T.-Y.Huang,N.Handigol,B.Heller,N.McKeown,and
InProc.ACMHotMobile,2015.
R.Johari.Confused,Timid,andUnstable:PickingaVideo
StreamingRateisHard.InProc.IMC,2012.
[33] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,and
M.Watson.ABuffer-BasedApproachtoRateAdaptation:
338