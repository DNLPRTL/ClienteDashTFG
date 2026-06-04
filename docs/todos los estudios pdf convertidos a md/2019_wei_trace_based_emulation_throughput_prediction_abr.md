SPECIALSECTIONONMOBILESERVICECOMPUTINGWITHINTERNETOFTHINGS
ReceivedMarch11,2019,acceptedMarch27,2019,dateofpublicationApril4,2019,dateofcurrentversionApril29,2019.
DigitalObjectIdentifier10.1109/ACCESS.2019.2909399
Evaluation of Throughput Prediction for Adaptive
Bitrate Control Using Trace-Based Emulation
BOWEI 1,(StudentMember,IEEE),HANGSONG 2,
SHANGGUANGWANG 3,(SeniorMember,IEEE),KENJIKANAI 1,
ANDJIROKATTO1,(Member,IEEE)
1DepartmentofComputerScienceandCommunicationsEngineering,WasedaUniversity,Tokyo169-8555,Japan
2ResearchInstituteforNanodeviceandBioSystems,HiroshimaUniversity,Higashihiroshima739-8527,Japan
3StateKeyLaboratoryofNetworkingandSwitchingTechnology,BeijingUniversityofPostsandTelecommunications,Beijing210023,China
Correspondingauthor:BoWei(weibo0504@fuji.waseda.jp)
ThisworkwassupportedbytheJSPSKAKENHIunderGrant15H01684.
ABSTRACT DynamicadaptivevideostreamingoverHTTP(DASH)iswidelystudiedandhasbeenadopted
inmodernvideoplayerstoensureuserqualityofexperience(QoE).InDASH,adaptivebitratecontrolisakey
partwhoseultimategoalistomaximizevideobitratewhileminimizingrebuffering.Throughputprediction
playsanimportantroleinhelpingselectthepropervideobitratedynamically.Inthispaper,westudiedthe
influenceofthroughputpredictiononadaptivevideostreaming.Becausethereal-worldnetworkisdynamic,
differentmethodsneedtobetestedwithlarge-scaledeploymentsandanalyzedstatistically.However,thisis
difficultinacademicresearch.Therefore,weestablishedareproducibletrace-basedemulationenvironment,
which enables us to compare different methods quantitatively under the artificially same condition, with
limited experiments. The throughput prediction methods are implemented into DASH to evaluate the
effect on QoE for video streaming. The results indicate that the prediction method using long short-term
memory (LSTM) performs better than the other methods. However, throughput prediction alone is not
enoughtoensurehighQoE.TofurtherimprovetheQoE,weproposedthedecisionmapmethod(DMM),
wherethebufferoccupancyisalsoincorporatedtomakeaselection.Byusingthisdecisionmap,thechoiceof
bitratecanbesmarterthanthatwhenonlypredictioninformationisused.ThetotalQoEisfurtherimproved
by32.1%intheferrytrace,whichshowstheeffectivenessofDMMinfurtherimprovingtheperformance
ofthroughputpredictioninadaptivebitratecontrol.
INDEXTERMS Throughputprediction,adaptivebitratecontrol,QoE,DASH.
I. INTRODUCTION in less chance of promoting commercial contents such as
With the rapid increase of traffic especially in mobile net- advertisements.However,ifthepossiblenetworkthroughput
works,providingvideostreamingwithahighqualityofexpe- is not fully exploited, the video may be streamed with a
rience(QoE)fortheuserbecomesmoreandmoreessential, relativelylowquality,whichmayalsodegradetheuserQoE
as the user QoE is directly related to the service provider’s and decrease the user engagement. Therefore, the adaptive
revenue[1],[2].TomaximizetheQoE,thebasicrequirement bitratecontrolshouldbeinvolvedduringthevideostreaming
isprovidingcontentswithhighervideoquality(orbitrate)and to choose the proper video bitrate dynamically by trading
fewerrebufferingdurations.Asthenetworkconditionisnot off between video quality and rebuffering. Besides regular
alwaysstable,transmittingcontentswithconstantbitratemay video streaming, adaptive control is also essential in other
become problematic. Suppose the highest streaming quality applicationssuchas360-degreevideotransmissioninvirtual
ischosenunderanenvironmentwithinadequatebandwidth, reality(VR)toensurehighQoE[22],[23].
the rebuffering events may occur frequently. Then, the user There exist several adaptive streaming protocols such as
may be upset and may quit the video session, resulting Adobe HTTP Dynamic Streaming [3], Apple HTTP Live
Streaming[4],andMicrosoftSmoothStreaming[5].Inrecent
years,dynamicadaptivevideostreamingoverHTTP(DASH)
The associate editor coordinating the review of this manuscript and
approvingitforpublicationwasShuiguangDeng. hasbeenstudiedworldwideasaunifyingstandard[6].Inthe
2169-3536 2019IEEE.Translationsandcontentminingarepermittedforacademicresearchonly.
51346 Personaluseisalsopermitted,butrepublication/redistributionrequiresIEEEpermission. VOLUME7,2019
Seehttp://www.ieee.org/publications_standards/publications/rights/index.htmlformoreinformation.

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
DASH protocol, the video contents are divided into short withotherinformationforQoEimprovement.Inthispaper,
chunks and encoded at different bitrate levels. Then the we designed and tested a two-dimensional decision map.
client player can request the segment chunks with proper Theresultsdemonstratedthattheconceptofdecisionmapis
bitrate successively and dynamically according to the net- feasibleinimprovingQoE.Inthefuture,wewillincreasethe
work condition. The algorithm for selecting the download dimensionsofthemapandincorporatemoreinformationto
bitrate is called the adaptive bitrate (ABR) algorithm. The optimizethehigh-dimensionaldecisionmap.Thencompare
ABR algorithm employs the network condition logs (such itwithotherABRmethods.
asthroughput,bufferstate,etc.),whicharemonitoredinthe Intherestofthispaper,SectionIIgivesabriefintroduction
client side to decide the bitrate of the later chunks to be oftheDASHsystemandtheimplementationoftrace-based
downloaded. The purpose is to maximize the video quality emulationstructure.SectionIIIdescribesthedifferentpredic-
while reducing rebuffering. There are two kinds of ABR tionmethodsinvolvedintheevaluation.SectionIVpresents
algorithms, the rate-based (RB) methods and buffer-based the evaluation metrics and results. Section V presents the
(BB) methods [7]–[9]. The RB algorithm selects the next DMMandthecorrespondingresults.Finally,theconclusion
downloadingchunkbyestimatingthefuturethroughputwhile andfutureworkarepresentedinSectionVI.
| the BB | algorithm decides | the | selection | based | only | on the |     |     |     |     |     |
| ------ | ----------------- | --- | --------- | ----- | ---- | ------ | --- | --- | --- | --- | --- |
currentbuffer-occupancystatewithoutusinganythroughput II. EMULATIONSYSTEMSTRUCTURE
information.Debateisongoingconcerningwhichtypeisbet- As shown in Fig. 1, the basic DASH system structure con-
ter.TheRBalgorithmmayperformbadlyifthepredictionis sists of an HTTP server and a DASH client side. The video
inaccurate,whiletheBBalgorithmrequirestoomuchbuffer, contentisencodedatdifferentbitratesandisorganizedand
whichcostsextraresourceconsumption.Someresearchhas
|     |     |     |     |     |     |     | stored in | the server. DASH | client communicates |     | with the |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | ------------------- | --- | -------- |
proposedalgorithmsbasedonboththroughputpredictionand content server and plays the video. In the DASH context,
buffer-occupancyinformation[10],[11]. differentbitrateversionsarenamedrepresentations.Thecon-
In the above ABR algorithms, which involve pre- tents are then divided into short chunks so that, for exam-
diction, the throughput prediction method is basically ple, each chunk includes a 2-second video playback time.
| chosen | as the harmonic | mean | of  | the previous |     | several |               |                  |          |           |           |
| ------ | --------------- | ---- | --- | ------------ | --- | ------- | ------------- | ---------------- | -------- | --------- | --------- |
|        |                 |      |     |              |     |         | For different | representations, | although | the video | qualities |
measurements[12]–[14].Theimpactofdifferentthroughput vary, the start time and end time of each chunk are aligned.
prediction is not discussed. In our previous work, we pro- Therefore, the chunks in different representations can be
posed several throughput prediction methods [15], [16]. concatenatedandplayedsmoothlyonlyviathechunkorder,
In this paper, we focus on the influence of throughput pre- therebyenablingthedynamicalchoiceofvideoqualitydur-
dictionontheadaptivecontrolalgorithm.Becauseliterature
|     |     |     |     |     |     |     | ing streaming. | All the information | about | the video | content |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | ----- | --------- | ------- |
discussing this subject is rare, our work may give a deeper and the representation details are written in the Media Pre-
insightintotheeffectofthethroughputprediction. sentation Description (MPD) file. The MPD documents the
To evaluate different methods with limited experimenta- numberofrepresentationsforthevideocontent,theencoding
tion, we established a reproducible trace-based emulation bitrates,theURLsofthechunksandetc.ByparsingtheMPD
environment. By conducting the experiments in the artifi- file,theclientsidecanobtainfullknowledgeofthecontents.
| cially identical | network      | conditions, |            | we observed |     | that the |     |     |     |     |     |
| ---------------- | ------------ | ----------- | ---------- | ----------- | --- | -------- | --- | --- | --- | --- | --- |
| prediction       | method using | long        | short-term | memory      |     | (LSTM)   |     |     |     |     |     |
performsbetterthantheotherpredictionmethods.However,
| the prediction | alone              | is not | enough   | to ensure | high    | QoE.    |     |     |     |     |     |
| -------------- | ------------------ | ------ | -------- | --------- | ------- | ------- | --- | --- | --- | --- | --- |
| We then        | propose a decision | map    | method   | (DMM)     | to      | further |     |     |     |     |     |
| improve        | the performance    | of     | the QoE. | In this   | method, | both    |     |     |     |     |     |
throughputpredictionandbufferoccupancyinformationare
| incorporated. | Results         | indicate | that the         | DMM | method | can    |     |     |     |     |     |
| ------------- | --------------- | -------- | ---------------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
| improve       | the QoE further | by       | taking advantage |     | of the | buffer |     |     |     |     |     |
information.
| This paper | does not | aim at | determining | which | of  | the two |     |     |     |     |     |
| ---------- | -------- | ------ | ----------- | ----- | --- | ------- | --- | --- | --- | --- | --- |
algorithms,RBandBB,isbetterthantheother,neitherdoes
itaimatproposinganalgorithmthatcansurpassotherABR
controlmethods[10],[11].Instead,themaincontributionof
this work is that we evaluated the influence of throughput FIGURE1. TheDASHsystemstructure.
predictionmethodsontheperformanceoftheadaptivevideo
streaming. Then some design guidance for the ABR algo- The DASH client side mainly consists of an MPD parser
rithm can be achieved, thereby giving directions for future module, ABR control module, HTTP client module, video
work. Meanwhile, DMM is proposed as a concept of one buffer,andthemediaplayer.Duringthestreaming,theMPD
series of methods for the first time. This concept is novel, fileisfirstrequestedanddownloadedbytheclientandparsed
which using a map to incorporate throughput prediction togettheinformationaboutthevideocontents.ThentheABR
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     | 51347 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
controlmoduledetermineswhichrepresentationtoselectfor thethroughputbetweentheserverandclient,theresponseof
the next video chunk and communicates the decision to the the HTTP request is manipulated and delayed intentionally.
HTTPclientmodule.TheHTTPclientmodulethengenerates Therefore,fromtheviewpointoftheclientside,thethrough-
a request and communicates with the server to get the cor- putischangingdynamicallybecauseitdoesnotknowwhat
respondingvideochunk.Afterthecompletionofthecurrent happensontheserverside.
chunk,thecontentwillbestoredintothevideobuffer,andthe
ABR control module will repeat the download selection for B. ALGORITHMOFTHETRACE-BASEDSERVER
thenextchunk.Afterenoughvideobufferisfilled,themedia TheprocedureofthemanipulationisasshowninalgorithmI.
playerwillbegintoplaybackthevideo.Themostimportant The throughput trace is prepared in the server side, which
partintheDASHsystemistheABRcontrolmodulewhere can be referred to freely. The trace is stored every second.
theABRalgorithmisimplementedtoensureuserQoE. When the server catches the GET request from the client,
|     |     |     |     |     | it first judges | whether |     | this request | is  | for video | contents | or  |
| --- | --- | --- | --- | --- | --------------- | ------- | --- | ------------ | --- | --------- | -------- | --- |
A. CONCEPTOFTRACE-BASEDSERVER other content such as an html file or JavaScript files. If the
The development of ABR algorithms is still ongoing, and request is for other files, the data are returned to the client
a widely accepted method is not achieved yet. As the net- immediately. When the request for the first segment of the
work in the real world is always dynamic, we cannot eval- videocontentiscaptured,aninitialtimestampt iscreated
init
whichisregardedasabaselineforcalculatingthetimedelay.
| uate the algorithms | under two | identical | network | conditions. |     |     |     |     |     |     |     |     |
| ------------------- | --------- | --------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore,tovalidatetheactualefficiencyofthealgorithms, Whentherequestsforvideocontentsarecaptured,thesizeof
large-scale deployment in a real network environment is therequestedchunkisanalyzed.Normally,thechunkofdata
shouldbesentbacktotheclientimmediately.
| needed via video | streaming | providers. | The | data containing |     |     |     |     |     |     |     |     |
| ---------------- | --------- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
logs from millions of video sessions can then be analyzed However, to shape the throughput according to the des-
statistically.However,itisnotalwayspossibleforacademic ignated trace, the chunk data is divided and transmitted as
researcherstoobtainsuchlarge-scaledata.Asanalternative, pieces with artificial delay intervals dt. After the request
thetrace-basedemulationisemployedforevaluation.Under is coming, the elapsed time from the initial timestamp is
|     |     |     |     |     | calculatedast | =t  | −t  | .Thenthesendingsizeisdetermined |     |     |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
theartificiallyidenticalnetworkconditions,theeffectofdif- 1 init
=f(t)∗dt,wheref(t)isthethroughputvalueattime
| ferentalgorithmscanbecomparedusinglimiteddeployment. |     |     |     |     | byS sent |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Here,wedevelopedatrace-basedserver. t in the prepared trace table and dt is the delay interval. dt
The implementation of our emulation is shown in Fig. 2. ischosenas100mshere.Aftersending,theserverwaitsfor
Thepurposeistoreplicatethethroughputbetweentheserver dt time (or 100 ms here) and then repeats the elapsed time
|                                                    |     |     |     |     | calculation | t = | t −t | and  | sending | size | determination |     |
| -------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | ---- | ---- | ------- | ---- | ------------- | --- |
| andtheclientasthesameasagiventhroughputtrace.Asthe |     |     |     |     |             |     | n−1  | init |         |      |               |     |
networkconditionintherealworldcannotbefullycontrolled, accordingtothenewf(t).Aftersendingthelastpieceofthe
we build a virtual network emulation environment. In this chunk, the delay interval dt should be recalculated because
environment,theserverisbuiltonthesamecomputerasthe more data can be sent within dt. The delay is calculated by
clientusingthelocalhost127.0.0.1.Byusingthelocalhost, S /f(t), where S is the size of the last piece and f(t) is
|     |     |     |     |     | last |     | last |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
thethroughputatthetimesendingthelastpiece.Afterthelast
wecanregardthedelaytimeofthedatatransfertobesmall
enough(<1ms)thatitcanbeignored.Thenode.jsrun-
delay,theendsignaloftheresponseistriggered.Notethatthe
timepackageisusedtobuildtheHTTPserver.Thisstructure tracedataareusuallystoredeverysecondformanydatasets.
Intheimplementation,tisflooredtoanintegersecondasthe
| is chosen because | it gives | full control | of  | the data transfer, |     |     |     |     |     |     |     |     |
| ----------------- | -------- | ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
such as when to respond and what to respond. To constrain unitofmeasurementofthetimestampismilliseconds.
C. DASHCLIENT
|     |     |     |     |     | A JavaScript-based |     | DASH | client, | originally |     | developed | by  |
| --- | --- | --- | --- | --- | ------------------ | --- | ---- | ------- | ---------- | --- | --------- | --- |
ITEC[9],isadoptedinthisstudy.ThedefaultABRcontrol
|     |     |     |     |     | algorithm | in this | client | is rate-based | and | chooses | the | maxi- |
| --- | --- | --- | --- | --- | --------- | ------- | ------ | ------------- | --- | ------- | --- | ----- |
mumbitratebelowthepredictedthroughput.Wemademodi-
ficationstotheoriginalversion.First,wecorrectedthebitrate
switchlogic.Whenthepredictedthroughputissmallerthan
thelowestencodingbitrate,theoriginalversiondoesnotcon-
siderthiscase,andtheselectionisnottriggered.Here,weset
theselectedbitrateasthelowestonewhenencounteringthis
|     |     |     |     |     | case. Second, | the      | buffer | strategy | is modified. |             | The B max | and    |
| --- | --- | --- | --- | --- | ------------- | -------- | ------ | -------- | ------------ | ----------- | --------- | ------ |
|     |     |     |     |     | B are         | set. The | video  | session  | will         | start after | the       | buffer |
start
|     |     |     |     |     | occupancyisfilleduptoB |     |     | .Then,theclientrequestsvideo |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- |
start
|     |     |     |     |     | contents | continuously |     | until the | buffer | occupancy |     | reaches |
| --- | --- | --- | --- | --- | -------- | ------------ | --- | --------- | ------ | --------- | --- | ------- |
B .TheclientwillsendGETrequestswheneverthebuffer
max
FIGURE2. Theimplementationofthetrace-basedemulation. occupancyislowerthanB max .Ifthevideosessionencounters
| 51348 |     |     |     |     |     |     |     |     |     |     | VOLUME7,2019 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
Algorithm1:Trace-BasedServerImplementation
Input:therequestscapturedfromtheclient,
responseinterval:dt,
thepreparedthroughputtracef(t)
| Output:therespondingdataD |     | ,thelastsentdata |     |     |     |     |
| ------------------------- | --- | ---------------- | --- | --- | --- | --- |
sent
D last ,theendsignalofresponserespEnd
1: dt=100ms;
whileaGETrequestcomesdo
2:
3: analyzetherequestandgetthefiletypefiletype;
gettherequestedfilecontentfilecontent;
4:
iffiletype∼=.m4sthen
5:
| 6:  | D =filecontent[1:end]; |     |     |     |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- |
last FIGURE3. Thetraceappliedontheserverside,andthecorresponding
sendrespEnd;
| 7:  |     |     | measuredthroughputsontheclientsideintwotests. |     |     |     |
| --- | --- | --- | --------------------------------------------- | --- | --- | --- |
8: end
else
9:
filetype==.m4sthen
| 10: | ifrequestingfirstchunkthen |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- |
| 11: | recordtheinitialtimestampt | =   |     |     |     |     |
init
getTime();
end
12:
| 13: | n=1;                 |     |     |     |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- |
|     | t =floor(getTime()-t | );  |     |     |     |     |
| 14: | n init               |     |     |     |     |     |
thestartindexofthesendingdata:ST=1;
15:
=dt∗f(t
| 16: | S ); |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- |
sent n
while(ST +S −1)<size(filecontent)do
17: sent
| 18: | D sent =filecontent[ST:S | sent ]; |     |     |     |     |
| --- | ------------------------ | ------- | --- | --- | --- | --- |
|     | ST =ST +S ;              |         |     |     |     |     |
19: sent
|     | n++; |     | FIGURE4. Bufferoccupancyofthetwotests. |     |     |     |
| --- | ---- | --- | -------------------------------------- | --- | --- | --- |
20:
| 21: | t =floor(getTime()-t | );   |     |     |     |     |
| --- | -------------------- | ---- | --- | --- | --- | --- |
|     | n                    | init |     |     |     |     |
|     | S =dt∗f(t );         |      |     |     |     |     |
| 22: | sent n               |      |     |     |     |     |
clientsideintwotests.Ascanbeseen,theresultsofthetwo
| 23: | waitfordt; |     |                                                     |     |     |     |
| --- | ---------- | --- | --------------------------------------------------- | --- | --- | --- |
|     | end        |     | testsarethesame.Additionally,theshapesofthemeasured |     |     |     |
24:
D =filecontent[ST:end]; throughputs at the client side are the same as at the server
| 25: | last |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- |
26: waitforD /f(t ); side.Fig.4showsthebufferoccupancylogsofthetwotests.
last n
sendrespEnd; Ascanbeseen,thebufferoccupancylogsarealsoidentical.
27:
|     |     |     | These results | demonstrate | that our trace-based | emulation is |
| --- | --- | --- | ------------- | ----------- | -------------------- | ------------ |
28: end
| end |     |     | successfulinshapingthethroughputbetweentheserverand |     |     |     |
| --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
29:
client,andtheemulatednetworkconditioncanbereplicated,
therebyallowingustocomparethealgorithmsquantitatively
withlimitedexperiments.
anemptybuffer(freezing),itwillrestartafterrebufferingto
B start .Finally,thebufferoccupancyisrecordedaboutevery III. THROUGHPUTPREDICTIONMETHODOLOGY
100 ms and the throughput measured at the client is also The default throughput estimation method installed in
recordedforoff-lineQoEperformanceanalysis.
|     |     |     | the DASH | client is exponential | weighted | moving average |
| --- | --- | --- | -------- | --------------------- | -------- | -------------- |
(EWMA)[9].Inourpreviousworks[15],[16],[24],wehave
D. TRACE-BASEDEMULATIONVALIDATION proposed and implemented several methods of prediction.
To validate whether the trace-based emulation is success- They are the hybrid model of the autoregressive model and
fully implemented, and the virtual network environment is HMM (Hybrid) [15] and throughput prediction based on
reproducible, the test of video streaming is conducted. The LSTM (TRUST) [16]. We also implemented other meth-
contentusedisBigBuckBunnyanimationvideo.Inthetest, ods such as arithmetic mean (AM) [17], harmonic mean
theadaptivebitrateswitchisdisabled,andtheClientissetto (HM) [17], [25], last sample (LS) [18], moving average
request the content encoded at a constant rate of 515 kbps. (MA)[19],hiddenMarkovmodel(HMM)[18],andstochas-
Fig. 3 shows the results of the trace-based emulation. The ticmodel(Stochastic)[20].Intheemulation,thesemethods
blue staircase plot is the throughput trace used to shape the areusedforprediction.Thebitrateselectionisdecidedbased
sendingsequenceofthedataontheserverside.Theredand onthepredictionresultsusingtherate-basedadaptivecontrol
blackplotsarethethroughputsrecordedandcalculatedonthe algorithm. To compare the effect of these methods, during
| VOLUME7,2019 |     |     |     |     |     | 51349 |
| ------------ | --- | --- | --- | --- | --- | ----- |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
evaluation,onlythepredictionmethodischangedandother
settingsarekeptthesame.
IV. PERFORMANCEEVALUATION
| In this | section,        | the video | streaming  |         | experiments |       | are con- |     |     |     |     |     |
| ------- | --------------- | --------- | ---------- | ------- | ----------- | ----- | -------- | --- | --- | --- | --- | --- |
| ducted  | using different |           | prediction | methods |             | under | the same |     |     |     |     |     |
networkconditionshapedbythetraceontheserverside.The
bufferoccupancylogandthechoiceofbitrateforeachchunk
arerecordedforpostanalysis. FIGURE5. Thethroughputtraceofferry(HSDPA).
| To analyze     |     | the performance |        | of       | each algorithm, |            | the fac- |     |     |     |     |     |
| -------------- | --- | --------------- | ------ | -------- | --------------- | ---------- | -------- | --- | --- | --- | --- | --- |
| tors extracted |     | from the        | buffer | log that | are             | considered | in the   |     |     |     |     |     |
TABLE1. Theresultsofferrytrace.
| QoE calculation, |     | are the | initial | delay | (T  | ), the | number of |     |     |     |     |     |
| ---------------- | --- | ------- | ------- | ----- | --- | ------ | --------- | --- | --- | --- | --- | --- |
init
| rebufferings(N |     | rebuf ),rebufferingduration(T          |     |     |     | rebuf ),theaver- |     |     |     |     |     |     |
| -------------- | --- | -------------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
| agebitrate(R   |     | )andtheswitchofbitrateareextractedfrom |     |     |     |                  |     |     |     |     |     |     |
ave
| the bitrate | choice | log.        | The         | five factors |           | are analyzed | here      |     |     |     |     |     |
| ----------- | ------ | ----------- | ----------- | ------------ | --------- | ------------ | --------- | --- | --- | --- | --- | --- |
| as metrics  | for    | performance | assessment. |              | Moreover, |              | there are |     |     |     |     |     |
variousQoEdefinitionsthattakethefactorswithadifferent
| weight. | Therefore, | using | different | QoE | metrics, | the | perfor- |     |     |     |     |     |
| ------- | ---------- | ----- | --------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- |
mancejudgmentmaychange.AstheofficialQoEdefinition
isnotavailableyet,weusethemostwidelyusedone.Addi-
| tionally, | the formula | used | in  | [11] is | adopted | for calculating |     |     |     |     |     |     |
| --------- | ----------- | ---- | --- | ------- | ------- | --------------- | --- | --- | --- | --- | --- | --- |
theQoEmetric,whichis
N
(cid:88)
| QoE = | q(R | )−µT | −µ    | T      |     |     |     |     |     |     |     |     |
| ----- | --- | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|       |     | n    | rebuf | s init |     |     |     |     |     |     |     |     |
n=1
N−1
(cid:88)
|     |     |     | −   | |q(R |     | )−q(R | )| (1) |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ----- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |      | n+1 |       | n      |     |     |     |     |     |
n=1
| where q(R | ) represents |     | the relationship |     | between |     | bitrate and |     |     |     |     |     |
| --------- | ------------ | --- | ---------------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- |
n
| user-perceivedquality.N |     |     | isthetotalnumberofchunks.T |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rebuf
µ
| and T | are the | total | rebuffering | time | and | initial | delay. |     |     |     |     |     |
| ----- | ------- | ----- | ----------- | ---- | --- | ------- | ------ | --- | --- | --- | --- | --- |
init
andµ arethecorrespondingpenalties.Thelasttermonthe FIGURE6. Thepredictionerrorsofdifferentmethodsinferrytrace.
s
rightstandsforthepenaltyofbitrateswitch.Thelinearform
| q(R ) = | R isconsideredhere.Theµandµ |     |     |     |     | arechosenas |     |     |     |     |     |     |
| ------- | --------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| n       | n                           |     |     |     |     | s           |     |     |     |     |     |     |
themaximumbitrate.
|     |     |     |     |     |     |     |     | in LSTM | is only half | of other methods. | As for | the average |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ----------------- | ------ | ----------- |
Intheevaluation,thevideocontentisencodedinto14ver- bitrate, Stochastic, LS, and EWMA have a relatively high
| sions from | 100 | kbps | to 4000 | kbps. | The total | length | of the |               |      |                  |       |               |
| ---------- | --- | ---- | ------- | ----- | --------- | ------ | ------ | ------------- | ---- | ---------------- | ----- | ------------- |
|            |     |      |         |       |           |        |        | score ranging | from | 1270.8 to 1458.8 | kbps. | This also can |
video is about 598 seconds. Each chunk contains 2-second be observed in Fig.6 that there are more cases when the
video. The B is set to 40 seconds and B is set to predictionislargerthantheactualthroughputinStochastic,
|     | max |     |     |     |     | start |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
6seconds.
|     |     |     |     |     |     |     |     | LS, and         | EWMA, resulting | in aggressive   | choice.     | However,  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------------- | --------------- | ----------- | --------- |
|     |     |     |     |     |     |     |     | this aggressive | choice          | leads to longer | rebuffering | duration. |
A. EVALUATIONINFERRYCASE Amonotonicincreaseinrebufferingtimecanbeobservedin
The throughput traces implemented in the server are Stochastic,LS,andEWMA,wherethevaluesarefrom46.3to
chosen from the Mobile High-Speed Downlink Packet 68.5s.Thisreflectstheinherentcontradictionintheadaptive
Access(HSDPA)opendataset[21].Fig.5showsaselected ratealgorithm,wherethehighlydesiredlargebitratemaylead
trace from the HSDPA dataset. This trace is measured on a to more rebuffering. The LSTM makes a tradeoff between
ferry. As can be seen, there is a period when the network averagebitrateandrebufferingtime,resultinginahighQoE
| conditionisextremelybadandisalmostcutoff. |     |     |     |     |     |     |     | score. |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
TheresultsofdifferentmethodsareshowninTable1.The The log of buffer occupancy using different prediction
prediction errors of different methods are shown in Fig. 6. methods in the ferry trace is shown in Fig. 7. As can be
FromthetotalQoE,theLSTMperformsbestamongallthe seen,thebufferoccupancyoftheStochastic,LS,andEWMA
methods,wheretheQoEisincreasedbyamaximumof87.1% methods is always at a relatively low level. This increases
compared with the HM method. For the individual metric, thelikelihoodoflongerandmorefrequentrebufferingevents.
it can be seen that LSTM makes a conservative choice in EWMAevenhasfiverebufferingevents.Althoughthenum-
theinitialphase,resultinginasmalldelay.Theinitialdelay ber of rebuffering events is not included in (1), the greater
| 51350 |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2019 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
TABLE2. Theresultsofbustrace.
FIGURE7. Thelogofbufferoccupancyusingdifferentprediction
methodsforferrytrace.
FIGURE8. Thethroughputtraceofbus(HSDPA).
FIGURE9. Thepredictionerrorsofdifferentmethodsinbustrace.
numberofeventsmaydamagetheuserexperiencemorewith
thesamerebufferingduration.
| During        | the whole    | session,           | the buffer | occupancy  |                  | is some-    |
| ------------- | ------------ | ------------------ | ---------- | ---------- | ---------------- | ----------- |
| times at      | a relatively | high               | level,     | which      | is approximately |             |
| 30–40s        | in the LSTM  | method.            | For        | these      | periods,         | the bitrate |
| can be        | selected     | more aggressively. |            | Therefore, |                  | although    |
| LSTM performs |              | better than        | other      | prediction | methods          | from        |
theviewpointofthetotalQoE,itcanstillbeimproved.The
predictionaloneisnotenoughtoensureahighQoE.
FIGURE10. Thelogofbufferoccupancyusingdifferentprediction
B. EVALUATIONINBUSCASE methodsforbustrace.
| Fig. 8 shows | another | selected | HSDPA | trace, | which | is mea- |
| ------------ | ------- | -------- | ----- | ------ | ----- | ------- |
suredonabus.Ascanbeseen,theaveragethroughputisrel-
ativelyhigherthanthatintheferrytrace.Theaveragequality thattheaveragebitratefortheLSmethodis4.5%higherthan
of the video transmission should be higher. However, there thatofLSTM.However,thetotalQoEislowerandiscaused
byfrequentchangesofbitrate.
| are still | some sudden | degradations |     | of network |     | conditions, |
| --------- | ----------- | ------------ | --- | ---------- | --- | ----------- |
such as at around 150 s and 350 s. These areas need to be The log of buffer occupancy using different prediction
handledwell;otherwise,itcouldcauserebufferingevents. methodsforthebustraceisshowninFig.10.Ascanbeseen,
thebufferoccupancyofLSTMisalsoatarelativelyhighlevel
| Table | 2 shows | the QoE | results of | different | methods. | The |
| ----- | ------- | ------- | ---------- | --------- | -------- | --- |
prediction errors of different methods are shown in Fig. 9. thatisapproximately30–35s.Thisindicatesthepotentialto
From the total QoE, it can be confirmed that LSTM still furtherimprovetheadaptivebitratecontrolmethodforhigher
performsbestamongothers,wheretheQoEisincreasedby QoEperformance.
| a maximum | of  | 20.5% compared |     | to the | HM method. | The |
| --------- | --- | -------------- | --- | ------ | ---------- | --- |
EMWAmethodhasatendencytobeexcessivelyaggressive. C. EVALUATIONINTRAMCASE
ItisalsoshowninFig.9thatthereare10%predictiondata Fig.11showsanothertracefromatram[21].Ascanbeseen,
are 50% larger than the actual throughput. This aggressive the average throughput is relatively lower than that in ferry
strategygainsthehighestaveragebitrateof2648.4kbpswith trace. There is a period where the network condition is bad
a sacrifice of rebuffering events and time. Except for the butthereisnocutoffofthenetwork.
EMWA method, all methods manage to avoid rebuffering. TheresultsofthedifferentmethodsareshowninTable3.
AsshowninFig.9,theHMandHMMmethodstendtohavea The prediction errors of different methods are shown
conservativeselectionsince17.1%and19.7%predictiondata in Fig. 12. In this case, the LSTM still has a very good
are50%lowerthanactualthroughput,respectively,resulting QoE of 170.9, which is increased by a maximum of 18.9%
inalowQoEscore.TheLSTMmethodachievesahighaver- compared to the HM method. However, the EWMA per-
age bitrate, which results in a high QoE. It can be observed forms best this time with 6.4% higher QoE than LSTM.
VOLUME7,2019 51351

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
FIGURE13. Thelogofbufferoccupancyusingdifferentprediction
FIGURE11. Thethroughputtraceoftram(HSDPA). methodsfortramtrace.
|     |     |     |     | performance | among | other methods | in the ferry and |
| --- | --- | --- | --- | ----------- | ----- | ------------- | ---------------- |
TABLE3. Theresultsoftramtrace.
|     |     |     |     | bus traces. | As shown | in Table 3, | in the tram trace, |
| --- | --- | --- | --- | ----------- | -------- | ----------- | ------------------ |
althoughtheoriginalEWMAperformsbest,theLSTM
|     |     |     |     | still shows | a good QoE, | which | is only 6.0% lower |
| --- | --- | --- | --- | ----------- | ----------- | ----- | ------------------ |
thanthatofEWMA.ExceptforEWMAintramtrace,
LSTMshowstheadvantageoverothermethods
2) Thethroughputpredictionaloneisnotenoughtoensure
|     |     |     |     | a high QoE.        | The buffer | status should | also be taken        |
| --- | --- | --- | --- | ------------------ | ---------- | ------------- | -------------------- |
|     |     |     |     | into consideration | for        | aggressive    | selection to further |
improveQoE.Fig.7,10,and13showthattheaverage
|     |     |     |     | buffer occupancy | of  | LSTM method | is at a relatively |
| --- | --- | --- | --- | ---------------- | --- | ----------- | ------------------ |
60%∼70%
|     |     |     |     | high level, | which is       | about          | of B max . This  |
| --- | --- | --- | --- | ----------- | -------------- | -------------- | ---------------- |
|     |     |     |     | is because  | the rate-based | algorithm      | always chooses   |
|     |     |     |     | the bitrate | lower than     | the prediction | throughput. This |
strategyissafeforavoidingpossiblerebufferingevents.
However,theimagequalitymaybenotgoodenough.
Actually,thebitrateselectioncanbemoreaggressiveif
thebufferoccupancyishigh.Bycomparingtheresults
|     |     |     |     | of the LSTM | and EMWA     | in the     | tram case, it can be |
| --- | --- | --- | --- | ----------- | ------------ | ---------- | -------------------- |
|     |     |     |     | found that  | a good QoE   | is related | to higher average    |
|     |     |     |     | bitrate and | lower buffer | occupancy  | under the same       |
networkconditions.Therefore,additionalinformation
| FIGURE12. Thepredictionerrorsofdifferentmethodsintramtrace. |     |     |     |          |             |            |                   |
| ----------------------------------------------------------- | --- | --- | --- | -------- | ----------- | ---------- | ----------------- |
|                                                             |     |     |     | needs to | be included | in the ABR | method to further |
improvetheQoEperformance.
Thisaggressive strategy wins in achieving the highest aver- Itisalsoimportanttonotethatintheinitialphase,anover-
age bitrate of 716.8 kbps, which is 2.6% higher than that estimation could be disastrous as long waiting time may
of LSTM. It also successfully avoids rebuffering events. annoy the user a lot, and may cause the user to give up the
Although LSTM is not the best, it still outperforms other videosession.Thiswillcauseadramaticlossoftheservice
methods. provider’srevenue.Therefore,intheadaptivestrategydesign,
The log of buffer occupancy using different prediction the selection needs to be conservative in the initial phase to
methodsinthetramtraceisshowninFig.13.Ascanbeseen, establishthestreamingassoonaspossible.
the buffer occupancy during the streaming is at a relatively With the guidance derived from the above discussion,
high level, which means the bitrate selection is somehow anewABRmethodisproposedandevaluatedinthefollow-
| conservative.ThisisconsideredasthereasonthattheLSTM |             |         | ingsections.         |     |     |     |     |
| --------------------------------------------------- | ----------- | ------- | -------------------- | --- | --- | --- | --- |
| is defeated                                         | by the EWMA | method. | As the ABR algorithm |     |     |     |     |
usedhereisrate-based,thechosenbitrateisalwaysbelowthe
V. DECISIONMAPMETHODFORADAPTIVE
prediction. Therefore, the bitrate selection can be improved BITRATECONTROL
whilereducingthebufferoccupancybytakingadvantageof
A. AGGRESSIVEDECISION
thebufferoccupancyinformation. FromtheevaluationresultsandthediscussioninSectionIV,
itisevidentthatthereisaneedtodesignanewadaptivebitrate
D. DISCUSSION controlalgorithmbasednotonlyonthethroughputprediction
Fromtheevaluationresults,itisfoundthat: but also on the buffer occupancy information because the
1) IntheABRcontrol,throughputpredictionusingLSTM rate-basedABRtendstobetooconservative.Ifthethrough-
can contribute to better QoE performance. As shown putisthesameasthebitrate,thebufferoccupancyshouldstay
in Table 1 and 2, the LSTM achieves the best QoE thesamebecausethedownloadedvideodurationcanbalance
| 51352 |     |     |     |     |     |     | VOLUME7,2019 |
| ----- | --- | --- | --- | --- | --- | --- | ------------ |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
|     |     |     |     |     |     | TABLE4. | Theresultsoftramtrace. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ---------------------- | --- | --- | --- | --- | --- | --- |
methodaresetassuggestedinBBA-0in[7].Ascanbeseen,
|     |     |     |     |     |     | from the | viewpoint | of  | the total | QoE, there | seems | to be | no  |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --------- | ---------- | ----- | ----- | --- |
improvementthanevenLSTM.TheQoEscoreis98.9%and
92.9%ofthoseintheLSTMandEWMAmethods.ThisQoE
|               |                                                       |                  |     |                   |     | degradation | is caused | by        | a rebuffering | event      | around | 450         | s.  |
| ------------- | ----------------------------------------------------- | ---------------- | --- | ----------------- | --- | ----------- | --------- | --------- | ------------- | ---------- | ------ | ----------- | --- |
| FIGURE14.     | Theillustrationofthedecisionmapwiththeaggressivearea. |                  |     |                   |     |             |           |           |               |            |        |             |     |
|               |                                                       |                  |     |                   |     | However,    | except    | for the   | rebuffering   | drawback,  |        | the average |     |
| the consuming | time                                                  | for downloading. |     | If the throughput | is  |             |           |           |               |            |        |             |     |
|               |                                                       |                  |     |                   |     | bitrate is  | 14.5%     | and 11.6% | higher        | than those | of     | the LSTM    |     |
lowerthanthebitrate,thebufferoccupancyshoulddecrease andEMWAmethods.
asitconsumesmoretimeindownloading.Whenthecurrent
DMM-Aisindeedanaggressivemethod.However,itcan
buffer occupancy is large, the bitrate can be chosen aggres- beconsideredasa‘‘controlledaggressive’’caseasthebuffer
sively. occupancy is monitored. If the drawback of rebuffering can
Here,weproposeaDMMwithanaggressivemechanism
besolved,theperformanceoftheDMM-Aisexpectedtobe
(DMM-A)foradaptivebitratecontrolincorporatingbothpre- moreoutstanding.
dictionandbufferoccupancyinformationasshowninFig.14.
|                            | x-axis           |                               |           |             | B     |                                                       |     |     |     |     |     |     |     |
| -------------------------- | ---------------- | ----------------------------- | --------- | ----------- | ----- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| In this map,               | the              | is the current                | buffer    | occupancy   | cur   |                                                       |     |     |     |     |     |     |     |
|                            |                  |                               | (cid:49)T |             |       | B. AGGRESSIVEDECISIONWITHCONSERVATIVE                 |     |     |     |     |     |     |     |
| and y-axis                 | is an additional | term                          |           | named extra | down- |                                                       |     |     |     |     |     |     |     |
|                            |                  |                               | DL        |             |       | MECHANISM                                             |     |     |     |     |     |     |     |
| loadingtime(EDT).(cid:49)T |                  | iscalculatedusingthefollowing |           |             |       |                                                       |     |     |     |     |     |     |     |
|                            |                  | DL                            |           |             |       | Asdiscussedintheformersection,itisnecessarytodealwith |     |     |     |     |     |     |     |
equation:
|     |     |     |     |     |     | the possible | rebuffering |     | event | in the DMM-A |     | because | the |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ----- | ------------ | --- | ------- | --- |
(cid:49)T /C aggressive decision is made intentionally. Here, we extend
|     | =[(R | ind+1 | )−1]∗T |     | (2) |           |      |               |     |              |           |     |     |
| --- | ---- | ----- | ------ | --- | --- | --------- | ---- | ------------- | --- | ------------ | --------- | --- | --- |
|     | DL   |       | pred   | seg |     |           |      |               |     |              |           |     |     |
|     |      |       |        |     |     | the DMM-A | with | an additional |     | conservative | mechanism |     | as  |
whereC isthethroughputpredictionusingLSTM,R ind+1 shown in Fig. 15. We name this extended method as DMM
pred
is the bitrate one rank higher than the rate-based choice. because it involves both aggressive and conservative areas.
T seg is the duration of one segment. This term is used to InDMM,besidesthedivisionofnormalandaggressiveareas,
estimatethepossibleextradownloadingtimewhenchoosing the conservative area is added which is shown as blue dots.
the bitrate larger than the throughput prediction. B upper is This area is determined by two thresholds, B con1 and B con2 .
the maximum buffer occupancy and B is a threshold for When the buffer occupancy is within the conservative area,
agg
decidingwhentobeaggressive.(cid:49)T isanotherthreshold no matter what the throughput prediction is, the conserva-
upper
in the EDT axis to judge the aggressive action. The area tiveactionshouldbetakenimmediatelytoavoidrebuffering
shaded with red dots is the aggressive area and that with events. B and B are set to indicate the emergency
|     |     |     |     |     |     |     | con1 | con2 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |      |      | B   |     |     | B   |     |
green dots is the normal area. The aggressive area is where level of the situation. If the cur is lower than con1 but
the buffer occupancy is relatively high and the EDT is not higherthanB ,thebitratewillbechosenasoneranklower
con2
| verylarge. |     |     |     |     |     | thantherate-baseddecision.IftheB |     |     |     | islowerthanB |     |     | ,    |
| ---------- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ------------ | --- | --- | ---- |
|            |     |     |     |     |     |                                  |     |     |     | cur          |     |     | con2 |
Forsimplicityandneutrality,thered-dottedareaisdrawn this is considered an extremely adverse situation; therefore,
as a linear relationship here. The B is chosen as 20 s, the bitrate will be chosen as two ranks lower than the rate-
agg
which is the same as the lower limit of buffer occupancy. baseddecision.Thewholeprocedureofthismethodisshown
is,themoreaggressivethemapis.(cid:49)T
| ThesmallerB |     |     |     |     |       | inAlgorithmII.Here,B |     |     | andB | aresetas10sand5s, |     |     |     |
| ----------- | --- | --- | --- | --- | ----- | -------------------- | --- | --- | ---- | ----------------- | --- | --- | --- |
|             | agg |     |     |     | upper |                      |     |     | con1 | con2              |     |     |     |
is set as 2 s here because we expect one segment time is respectively. It can be expected that rebuffering events can
the largest tolerance for an aggressive decision. The larger be avoided using this conservative mechanism. Meanwhile,
(cid:49)T is, the more aggressive the map is. The boundary this conservative decision will also be applied to the initial
upper
betweennormalandaggressiveareasisalinefrom(B ,0) period when the user starts the video session. It is expected
agg
|     | ,(cid:49)T ).Ifthe((cid:49)T |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to(B upper upper DL ,B cur )fallsintheaggres- that this conservative decision can help reduce initial delay
sive area, the bitrate will be chosen as one rank higher becausethereisnobufferoccupancyatthebeginningandthe
than the rate-based decision. By using this decision map, selectionwillbeconservative.
the choice of bitrate can be more aggressive than the rate- Table5showstheresultsofDMM,comparedwithLSTM,
basedmethod.Itcanbeexpectedthatahigheraveragebitrate EWMA,BB,andDMM-Amethods.Itcanbeseenthat,from
canbeachieved. theviewpointoftotalQoE,theDMMperformsbestamong
Table4showstheresultsofDMM-A,comparedwiththe allthemethods,wheretheQoEisincreasedbyamaximum
LSTM,EWMA,andBBmethods.TheparametersoftheBB of 7.4% compared with EWMA method. Besides the total
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     | 51353 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
Algorithm2:DecisionMapMethodforABR
| Input:throughputprediction:C |     |     | usingLSTM, |     |     |     |     |     |
| ---------------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
pred
currentbufferstate:B
cur
| Output:selectedbitrate:R |         | sel      |              |     |     |     |     |     |
| ------------------------ | ------- | -------- | ------------ | --- | --- | --- | --- | --- |
| setthresholds:B          |         | ,B ,B    | ,(cid:49)T ; |     |     |     |     |     |
| 1:                       |         | agg con1 | con2 upper   |     |     |     |     |     |
| ifC                      | <R      | then     |              |     |     |     |     |     |
| 2: pred                  | min     |          |              |     |     |     |     |     |
| 3: R                     | =R      | ;        |              |     |     |     |     |     |
|                          | sel min |          |              |     |     |     |     |     |
end
4:
5: else
ind=0;initializetheselectedrateindex
6:
| foreachbitrateR |     | inencodingrates{R}do |      |     |     |     |     |     |
| --------------- | --- | -------------------- | ---- | --- | --- | --- | --- | --- |
| 7:              |     | i                    |      |     |     |     |     |     |
|                 | <C  | >R                   |      |     |     |     |     |     |
| 8:              | ifR | &&R                  | then |     |     |     |     |     |
|                 | i   | pred i               | i1   |     |     |     |     |     |
ind=i; FIGURE15. Theillustrationofthedecisionmapmethod(DMM)withboth
9:
aggressiveandconservativeareas.
| 10: | end |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
end
11:
decidewhethertakeconservativestrategy
|         | <=B | &&ind>1then |     |     |     |     |     |     |
| ------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| 12: ifB | cur | con2        |     |     |     |     |     |     |
ind=ind–2;
13:
14: end
| 15: elseif{B |     | <B }&&{B | >B }&&   |     |     |     |     |     |
| ------------ | --- | -------- | -------- | --- | --- | --- | --- | --- |
|              | cur | con1     | cur con2 |     |     |     |     |     |
{ind>0}then
| 16: | ind=ind−1; |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
end
17:
decidewhethertakeaggressivestrategy
−1)∗T FIGURE16. ThelogofbitratestatususingDMMintram.(a)Initialstage,
| 18: (cid:49)T | =(R        | ind+1 /C     | ;             | (b)Badnetworkconditionperiod. |     |     |     |     |
| ------------- | ---------- | ------------ | ------------- | ----------------------------- | --- | --- | --- | --- |
|               | DL         | pred         | seg           |                               |     |     |     |     |
| if{(B         | −B         | /B −B        | )>            |                               |     |     |     |     |
| 19:           | cur        | agg upper    | agg           | Theresultsofbustrace.         |     |     |     |     |
| ((cid:49)T    | /(cid:49)T |              | <R            | TABLE6.                       |     |     |     |     |
|               | DL         | upper )}&&{R | ind max }then |                               |     |     |     |     |
ind=ind+1;
20:
end
21:
| 22: R | =R      |     |     |     |     |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
|       | sel ind |     |     |     |     |     |     |     |
end
23:
TABLE5. Theresultsoftramtrace.
C. DMMPERFORMANCEVERIFICATIONINOTHERTRACES
TheperformanceoftheDMMmethodisalsoverifiedinother
traces:
1) VERIFICATIONINBUSCASE
|     |     |     |     | Table 6 shows | the results      | of DMM, compared | with             | LSTM, |
| --- | --- | --- | --- | ------------- | ---------------- | ---------------- | ---------------- | ----- |
|     |     |     |     | EWMA,         | and BB methods   | for the bus      | trace. It can be | seen  |
|     |     |     |     | that, from    | the viewpoint    | of total QoE,    | the DMM performs |       |
|     |     |     |     | best among    | all the methods, | where the        | QoE is increased | by    |
QoE, the average bitrate is also improved by 9% compared a maximum of 6.8% compared with LSTM method. The
with the EWMA method, which is the best. Furthermore, averagebitrateisalsoimprovedsignificantlyby6.3%com-
|     |     |     |     | pared with | the LSTM | rate-based method. | The initial | delay |
| --- | --- | --- | --- | ---------- | -------- | ------------------ | ----------- | ----- |
theinitialdelayisreducedby0.7sasexpectedthankstothe
conservativeactionatthebeginning. is also reduced by 2.8 seconds thanks to the conservative
As shown in Fig. 16(a), the choice of bitrate is much mechanism.Fromtheseresults,itcanbeconcludedthatthe
lower than the predicted throughput at the initial stage. The DMM can significantly improve the QoE performance in
rebufferingeventisalsoavoidedduringabadnetworkcon- DASHcomparedwithconventionalmethods.
ditionperiod.AsshowninFig.16(b),thechoiceofbitrateis
alsoveryconservativeasthebufferoccupancybecomeslow 2) VERIFICATIONINFERRYCASE
becauseofthebadnetworkcondition.Thisstrategyhelpsthe Table 7 shows the results of DMM, compared with LSTM,
videosessionsurviveandplayonwithoutrebuffering.These EWMA, and BB methods for the ferry trace. As can be
results demonstrate that the DMM method can improve the seen from the viewpoint of total QoE, DMM outperforms
QoEsignificantlyforadaptivevideotransmission. LSTM, which is the best. The QoE is improved by 32.1%.
| 51354 |     |     |     |     |     |     | VOLUME7,2019 |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------ | --- |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
TABLE7. Theresultsofferrytrace. carriedout.Throughtrace-basedemulationinseveraltraces,
itisdemonstratedthattheDMMperformssignificantlybetter
thantheconventionalLSTMmethod.Theaveragebitrateis
|     |     |     |     |     |     |     |     | improved | while | no additional | rebuffering |     | event | is encoun- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ------------- | ----------- | --- | ----- | ---------- |
tered.Meanwhile,theinitialdelayisalsoreduced.TheQoEis
improvedbyamaximumof32.1%comparedwiththeLSTM
methodintheferrytrace.
Forfutureresearch,wewillcontinuetoimprovetheadap-
tivebitratecontrolalgorithmforbetterhandlingofdifferent
Theaveragebitrateisalsoimprovedsignificantlyby17.6% circumstances such as sudden network cutoff. Meanwhile,
compared with the LSTM rate-based method. Meanwhile, wewillincreasethedimensionsofthemapandincorporate
therebufferingtimeisnotincreased. moreinformationtooptimizethehigh-dimensionaldecision
It can be seen that, the QoE score by BB is higher than map. We will also test the performance in more traces and
DMM. This is because the BB chooses a very large buffer deploytheDMMalgorithmintorealnetworkenvironments.
andtheaveragebitrateischosenveryconservatively.Under OthertopicswhichinvolvingABR,suchas360videostream-
the current QoE standard, rebuffering has a greater weight ing,willalsobestudied.
| than the                                          | average | rate. | Therefore, | zero | rebuffering |     | leads to a |            |     |     |     |     |     |     |
| ------------------------------------------------- | ------- | ----- | ---------- | ---- | ----------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- |
| highQoEscore.However,theaveragebitrateismuchlower |         |       |            |      |             |     |            | REFERENCES |     |     |     |     |     |     |
thanothermethods,whichisonly66.3%ofthatintheDMM
|         |                  |     |     |         |         |     |             | [1] F. Dobrian | et  | al., ‘‘Understanding | the     | impact | of video | quality on user |
| ------- | ---------------- | --- | --- | ------- | ------- | --- | ----------- | -------------- | --- | -------------------- | ------- | ------ | -------- | --------------- |
| method. | This degradation |     | in  | average | bitrate | may | result in a |                |     |                      |         |        |          |                 |
|         |                  |     |     |         |         |     |             | engagement,’’  |     | in Proc. ACM         | SIGCOMM | Conf., | Toranto, | ON, Canada,     |
Nov.2011,pp.362–373.
muchlowerimagequalitythatannoystheuserperception.
[2] Y.Liu,S.Dey,F.Ulupinar,M.Luby,andY.Mao,‘‘Derivingandvalidating
ItisexpectedthattheDMMcanalsoreducetherebuffering
userexperiencemodelforDASHvideostreaming,’’IEEETrans.Broad-
events.However,intheferrytrace,thereisaperiodwhenthe cast.,vol.61,no.4,pp.651–665,Dec.2015.
networkissuddenlycutoff.Therefore,evenifthebitrateis [3] Adobe.(2016).AdobeHTTPDynamicStreaming(HDS).[Online].Avail-
chosenasthelowestone,therebufferingeventisnotavoided. able:https://www.adobe.com/devnet/hds.html
[4] Apple.(2016).AppleHTTPLiveStreaming.[Online].Available:https://
Insuchasituation,otherinformationshouldbeconsideredfor developer.apple.com/streaming/
preparationofsuddennetworkcutoff.Forexample,theremay [5] Microsoft. (2016). Microsoft Silverlight Smooth Streaming. [Online].
Available:https://www.microsoft.com/silverlight/smoothstreaming/
beano-signalareaintheferryroute.Basedonthedesignated
|     |     |     |     |     |     |     |     | [6] ISO/IEC. | (2014). | ISO/IEC | 23009-1:2014 |     | Information | Technology: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | ------------ | --- | ----------- | ----------- |
route,wecanexpecttoknowwhenwewillentertheno-signal
|     |     |     |     |     |     |     |     | Dynamic | Adaptive | Streaming | Over | HTTP (DASH) | Part | 1: Media Pre- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------- | ---- | ----------- | ---- | ------------- |
area.Then,thecontentscanbedownloadedmorethanB
|     |     |     |     |     |     |     | max | sentationDescriptionandSegmentFormats.[Online].Available:https:// |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
www.iso.org/standard/65274.html
beforethenetworkiscutoffwhengoingthroughtheno-signal
[7] T.Huang,R.Johari,N.McKeown,M.Trunnel,andM.Watson,‘‘Abuffer-
| area. During | the | no-signal |     | period, | the ABR | can | be stopped |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --- | ------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
basedapproachtorateadaptation:Evidencefromalargevideostreaming
becauseitdoesnotworkinazero-throughputcondition.After service,’’inProc.ACMConf.SIGCOMM,Chicago,IL,USA,Aug.2014,
goingoutofthecutoffarea,theB issetbacktothenormal pp.187–198.
max
oneandtheABRcontrolresumes. [8] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, ‘‘BOLA: Near-optimal
bitrateadaptationforonlinevideos,’’inProc.35thAnnu.IEEEInt.Conf.
Comput.Commun.,SanFrancisco,CA,USA,Apr.2016,pp.1–9.
VI. CONCLUSIONANDFUTUREWORK [9] B.Rainer,S.Lederer,C.Müller,andC.Timmerer,‘‘AseamlessWebinte-
grationofadaptiveHTTPstreaming,’’inProc.IEEEEUSIPCO,Bucharest,
Inthispaper,weevaluatedthroughputpredictionforadaptive
Romania,Aug.2012,pp.1519–1523
| bitrate control |     | via trace-based |     | emulation. |     | The | basic ABR |     |     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[10] H.Mao,R.Netravali,andM.Alizadeh,‘‘Neuraladaptivevideostream-
strategy is a rate-based method. To compare the methods ingwithpensieve,’’inProc.ACMSIGCOMM,LosAngeles,CA,USA,
Aug.2017,pp.197–210.
| quantitatively, |             | a trace-based |      | server | is proposed |            | and built. |              |            |           |     |              |                       |     |
| --------------- | ----------- | ------------- | ---- | ------ | ----------- | ---------- | ---------- | ------------ | ---------- | --------- | --- | ------------ | --------------------- | --- |
|                 |             |               |      |        |             |            |            | [11] X. Yin, | A. Jindal, | V. Sekar, | and | B. Sinopoli, | ‘‘A control-theoretic |     |
| The results     | demonstrate |               | that | this   | server      | can create | repro-     |              |            |           |     |              |                       |     |
approachfordynamicadaptivevideostreamingoverHTTP,’’inProc.ACM
| ducible | emulation | environments |     | according |     | to the | prepared |     |     |     |     |     |     |     |
| ------- | --------- | ------------ | --- | --------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
Conf.SpecialInterestGroupDataCommun.,London,U.K.,Aug.2015,
trace, which allows the evaluation of algorithms effectively pp.325–338.
withlimitedexperimentation.Byacomparisonoftheresults, [12] J. Jiang, V. Sekar, and H. Zhang, ‘‘Improving fairness, efficiency, and
|     |     |     |     |     |     |     |     | stability | in HTTP-based | adaptive | video | streaming | with | FESTIVE,’’ in |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | ----- | --------- | ---- | ------------- |
it is found that the throughput prediction using LSTM can Proc.CoNext,Nice,France,Dec.2012,pp.97–108.
contributetoachievingbetterQoEperformance.TheQoEis [13] Z.Lietal.,‘‘Probeandadapt:RateadaptationforHTTPvideostreamingat
improved by a maximum of 87.1% compared with the HM scale,’’IEEEJ.Sel.AreasCommun.,vol.32,no.4,pp.719–733,Apr.2014.
|     |     |     |     |     |     |     |     | [14] L. De | Cicco, | V. Caldaralo, | V. Palmisano, |     | and S. Mascolo, | ‘‘ELAS- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------- | ------------- | --- | --------------- | ------- |
methodinferrytrace.Meanwhile,thethroughputprediction
TIC:Aclient-sidecontrollerfordynamicadaptivestreamingoverHTTP
aloneisnotenoughtoensurehighQoE.Thereisstillroom (DASH),’’ in Proc.Int. Packet Video Workshop, San Jose, CA, USA,
Dec.2013,pp.1–8
| for further | improvement |     | of  | the QoE | by  | incorporating | the |              |           |              |     |        |                |          |
| ----------- | ----------- | --- | --- | ------- | --- | ------------- | --- | ------------ | --------- | ------------ | --- | ------ | -------------- | -------- |
|             |             |     |     |         |     |               |     | [15] B. Wei, | K. Kanai, | W. Kawakami, |     | and J. | Katto, ‘‘HOAH: | A hybrid |
informationofthebufferoccupancy.
TCPthroughputpredictionwithautoregressivemodelandhiddenMarkov
| We also | proposed |     | a new | ABR | algorithm | named | DMM. |     |     |     |     |     |     |     |
| ------- | -------- | --- | ----- | --- | --------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
modelformobilenetworks,’’IEICETrans.Commun.,vols.E101-B,no.7,
pp.1612–1624,Jan.2018.
| This algorithm |     | incorporates |     | both throughput |     | prediction | and |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[16] B.Wei,W.Kawakami,K.Kanai,J.Katto,andS.Wang,‘‘TRUST:ATCP
| buffer occupancy |     | information |     | to  | make | the decision | of  |     |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
throughputpredictionmethodinmobilenetworks,’’inProc.IEEEGlobal
whether the aggressive or conservative bitrate selection is Commun.Conf.(GLOBECOM),AbuDhabi,UAE,Dec.2018,pp.1–6.
| VOLUME7,2019 |     |     |     |     |     |     |     |     |     |     |     |     |     | 51355 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

B.Weietal.:EvaluationofThroughputPredictionforAdaptiveBitrateControlUsingTrace-BasedEmulation
[17] Y.LiuandJ.Y.B.Lee,‘‘Anempiricalstudyofthroughputpredictionin SHANGGUANG WANG received the Ph.D.
mobiledatanetworks,’’inProc.IEEEGlobalCommun.Conf.(GLOBE- degreefromthe BeijingUniversityofPosts and
COM),SanDiego,CA,USA,Dec.2015,pp.1–6. Telecommunications(BUPT),in2011.
[18] Y. Sun et al., ‘‘Cs2p: Improving video bitrate selection and adaptation HeiscurrentlyaProfessorandtheViceDirector
withdata-driventhroughputprediction,’’inProc.ACMSIGCOMMConf., of the State Key Laboratory of Networking and
Florianopolis,Brazil,Aug.2016,pp.272–285. Switching Technology, BUPT. He has published
[19] Q.He,C.Dovrolis,andM.Ammar,‘‘Onthepredictabilityoflargetransfer
more than 150 papers, and played a key role at
TCP throughput,’’ in Proc. ACM SIGCOMM, Philadelphia, PA, USA,
manyinternationalconferences,suchasGeneral
Aug.2005,pp.145–156.
ChairandPCChair.Hisresearchinterestsinclude
[20] H.Yoshida,K.Satoda,andT.Murase,‘‘Constructingstochasticmodel
servicecomputing,cloudcomputing,andmobile
of TCP throughput on basis of stationarity analysis,’’ in Proc. IEEE
edgecomputing.HeistheEditor-in-ChiefoftheInternationalJournalof
GlobalCommun.Conf.(GLOBECOM),Atlanta,GA,USA,Dec.2013,
pp.1544–1550. WebScience.
[21] HSDPADataset.[Online].Available:http://home.ifi.uio.no/paalh/dataset/
hsdpa-tcp-logs
[22] S. Petrangeli, V. Swaminathan, and M. Hosseini, ‘‘An HTTP/2-based
adaptivestreamingframeworkfor360řvirtualrealityvideos,’’inProc.
25thACMInt.Conf.Multimedia,MountainView,CA,USA,Oct.2017,
pp.306–314
[23] X.Jiang,Y.-H.Chiang,Y.Zhao,andY.Ji,‘‘Plato:Learning-basedadaptive
streamingof360-degreevideos,’’inProc.IEEE43rdConf.LocalComput.
Netw.(LCN),Chicago,IL,USA,Oct.2018,pp.393–400.
[24] K.Kanai,B.Wei,Z.Cheng,M.Takeuchi,andJ.Katto,‘‘Methodsforadap-
tivevideostreamingandpicturequalityassessmenttoimproveQoS/QoE
performances,’’IEICETrans.Commun.,Jan.2019,Art.no.2018ANI0003. KENJIKANAIreceivedtheB.E.,M.E.,andPh.D.
[25] X.K.Zouetal.,‘‘CanAccuratePredictionsImproveVideoStreamingin degrees from Waseda University, Tokyo, Japan,
CellularNetworks?’’inProc.16thInt.WorkshopMobileComput.Syst. in2010,2012,and2015,respectively.
Appl.,SantaFe,NM,USA,Feb.2015,pp.57–62. He is currently an Assistant Professor with
WasedaUniversity.HeisamemberofIEICE,IPSJ
andIEEE.
BOWEIreceivedtheB.E.andM.E.degreesfrom
Tianjin University, Tianjin, China, in 2012 and
2015,respectively.
SheiscurrentlypursuingthePh.D.degreewith
theGraduateSchoolofFundamentalScienceand
Engineering,WasedaUniversity.SheisaStudent
MemberoftheIEICE.
HANGSONGreceivedtheB.S.andM.S.degrees
in electronic science and technology from Tian-
jinUniversity,Tianjin,China,in2012and2015, JIROKATTO receivedtheB.S.,M.E.,andPh.D.
respectively,andthePh.D.degreefromHiroshima degrees from the University of Tokyo, in 1987,
University,Hiroshima,Japan,in2018. 1989,and1992,respectively,allinelectricalengi-
HeiscurrentlyaVisitingResearcherwiththe neering.
Research Institute for Nanodevice and Bio Sys- HejoinedNECCorporation,in1992,andthen
tems(RNBS),HiroshimaUniversity.Hisresearch joinedWasedaUniversity,in1999.Heisamember
interestsincludemicrowaveimaging,microwave ofACM,IEICE,andITE.
breastcancerdetectionsystemdevelopment,sig-
nalprocessing,complexpermittivitiesofbreastcancertissues,andantenna
design.
51356 VOLUME7,2019