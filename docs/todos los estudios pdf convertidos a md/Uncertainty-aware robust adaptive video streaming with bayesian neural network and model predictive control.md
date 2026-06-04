Public Review for
Uncertainty-Aware Robust Adaptive
Video Streaming with Bayesian Neural
Network and Model Predictive Control
N. Kan, C. Li, C. Yang, W. Dai, J. Zou, H. Xiong
In HTTP (Hypertext Transfer Protocol ) adaptive streaming, a video clip
is segmented into a sequence of independent-decodable chunks. Each chunk
is then encoded at multiple bitrates for diverse and dynamic network con-
ditions. A streaming client employs an Adaptive BitRate (ABR) algorithm
to determine future chunks’ bitrates to request. ABR algorithms’ objective
is to maximize the Quality-of-Experience (QoE), which depends on multiple
factors, including, but not limited to, rebuffering events, startup delay, high
visual quality, and small quality variance. In the past decade, the design
of ABR algorithms has been a hot research topic. While earlier ABR algo-
rithms were mostly heuristics, some recent ABR algorithms were based on
control theory, such as MPC (Model Predictive Control). The basic MPC-
basedABRalgorithmpredictsthethroughputswhendownloadingthefuture
chunks in a sliding window. It then uses the predicted throughputs to solve
a QoE maximization problem for the next chunk’s optimal bitrate. It is,
therefore, not hard to see that MPC-based ABR algorithms’ performance
relies on throughput prediction accuracy.
Inthispaper, NuowenKanandhiscolleaguesproposedtoleverageBayesian
Neural Network (BNN) to predict the probability distribution of the future
throughputs using the actual throughputs of previously downloaded chunks.
Unlikeotherthroughputpredictionalgorithmsthatonlygivepointestimates,
the BNN predictor learns uncertainty and provides confidence regions on
throughput predictions. The evaluation results show that the confidence re-
gions supplied by the BNN predictor help the MPC-based ABR algorithms
better adapt to dynamic networks and users. The reviewers found that the
idea of predicting confidence regions for future throughputs is inspiring, and
theevaluationsoftheproposedABRalgorithmarepromising. Whileamore
detailed analysis of the confidence regions and more extensive evaluation
results will likely be published in follow-up publications, the authors have
shed light on moving from point estimates to confidence regions. We believe
the presented methodology is also applicable to other latency-sensitive dis-
tributed applications over the best-effort Internet beyond HTTP adaptive
streaming.
Public review written by
Cheng-Hsin Hsu
National Tsing Hua University, Taiwan
ACM NOSSDAV 2021
17

Uncertainty-Aware Robust Adaptive Video Streaming with
Bayesian Neural Network and Model Predictive Control
NuowenKan,ChenglinLi,CaiyiYang,WenruiDai,JunniZou,HongkaiXiong
InstituteofMedia,Information,andNetwork,ShanghaiJiaoTongUniversity,Shanghai200240,China
{kannw_1230,lcl1985,ycy123,daiwenrui,zoujunni,xionghongkai}@sjtu.edu.cn
ABSTRACT 1 INTRODUCTION
Inthispaper,weproposeBayesMPC,anuncertainty-awarerobust Adaptivevideostreamingisapopularsolutiontoaddresstheissue
adaptivebitrate(ABR)algorithmonthebasisofBayesianneural ofqualityofexperience(QoE)degradationcausedbyrebuffering
network(BNN)andmodelpredictivecontrol(MPC).Specifically, events(i.e.,stallingduringplayback)andqualityfluctuationfor
toimprovethecapacityoflearningtransitionprobabilityofthe users whose transmission conditions are constrained and time-
networkthroughput,weadoptaBNN-basedpredictorthatisable varying.Byadoptinganadaptivebitrate(ABR)algorithmatthe
topredictthestatisticaldistributionoffuturethroughputfromthe clientside,thebitrateversionofvideochunkscanadapttothe
pastthroughputbynotonlyconsideringthealeatoricuncertainty dynamicsoftheuser’sthroughputsuchthather/hisQoEisim-
(e.g.,noise),butalsocapturingtheepistemicuncertaintyincurred proved.Ingeneral,representativesofexistingABRalgorithmscan
bylackofadequatetrainingsamples.Wefurthershowthatbyusing beclassifiedintotwomaincategories:machinelearning(ML)-based
thenegativelog-likelihoodlossfunctiontotrainthisBNN-based (especiallydeepreinforcementlearning-based),andnon-ML-based.
throughputpredictor,thegeneralizationerrorcanbeminimized Inparticular,recentlyproposeddeepreinforcementlearning
withtheguaranteeofPAC-Bayesiantheorem.Ratherthanapoint (DRL)-basedABRalgorithms(e.g.,Pensieve[16],D-DASH[7],Hot-
estimate, the learnt uncertainty can contribute to a confidence DASH[18],etc.)outperformtheothertypesofexistingalgorithms,
regionforthefuturethroughput,thelowerboundofwhichthen intermsoftheoveralluserQoE.Theylearnanoptimalmapping
leadstoanuncertainty-awarerobustMPCstrategytomaximizethe betweenthedynamicstatesandbitrateselectionswiththehelpof
worst-caseuserquality-of-experience(QoE)w.r.t.thisconfidence powerfulapproximationcapacityofneuralnetworks.Nevertheless,
region.Finally,experimentalresultsonthreereal-worldnetwork severaldrawbacksoftheseDRL-basedalgorithmscanbefoundin
tracedatasetsvalidatetheefficiencyofboththeproposedBNN- comparisontotheothers.Forinstance,theycanonlyperformwell
basedpredictoranduncertainty-awarerobustMPCstrategy,and inaspecifieddomain,sincetheirparameterscanhardlygeneralize
demonstratethesuperiorperformancecomparedtootherbaselines, toalltheheterogeneousnetworkanduserconditions,suchasthe
intermsofboththeoverallQoEperformanceandgeneralization throughputvariability,differentQoEmetricandbitratesettings
acrossallrangesofheterogeneousnetworkanduserconditions. [1,11].Inaddition,thelearntblack-boxmodelisdifficulttoguar-
anteeasafelyactinpracticeduetothelackofinterpretability.
CCSCONCEPTS Anotherconsiderabledrawbackisthatitishardtoreproducethe
•Informationsystems→Multimediastreaming;•Networks superiorperformanceoftheseDRL-basedalgorithms[1,9].
→Networkresourcesallocation. Incontrast,thoughstrugglingtoachievecompetitiveasymptotic
performanceastheDRL-basedmethods,somenon-ML-basedABR
algorithms(e.g.,Buffer-based[12],BOLA[19],RobustMPC[21],
KEYWORDS
etc.)canadaptacrossallrangesofnetworkanduserconditions,
Rateadaptation,adaptivevideostreaming,Bayesianneuralnetwork
whichisalsoguaranteedwithinterpretability.Forexample,the
(BNN),modelpredictivecontrol(MPC).
bitrateselectiondeterminedbyBOLAdependsonlyonthedynam-
icsofbufferoccupancy,leadingtoaconservativerateadaptation
ACMReferenceFormat:
NuowenKan,ChenglinLi,CaiyiYang,WenruiDai,JunniZou,Hongkai strategythatalwaystendstoavoidtherebufferingevent.While
Xiong.2021.Uncertainty-AwareRobustAdaptiveVideoStreamingwith RobustMPCtakesthebufferdynamicsandthefuturethroughput
BayesianNeuralNetworkandModelPredictiveControl.InWorkshopon predictionintoaccountbyincorporatingthemodelpredictivecon-
NetworkandOperatingSystemSupportforDigitalAudioandVideo(NOSSDAV trol(MPC)-basedframework.ThankstotheMPCsettingofadjust-
’21))(NOSSDAV’21),September28-October1,2021,Istanbul,Turkey.ACM, ingpredictionbias(i.e.,planningmulti-stepsandthenexecuting
NewYork,NY,USA,7pages.https://doi.org/10.1145/3458306.3458872 onestep),RobustMPCcanalwaysachieveastableperformance.
Furthermore,italsobringsanexcitingprospectthatifwecould
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor havelearnedamoreprecisethroughputpredictionmodelthan
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed RobustMPCdid[21],thenitispotentialtodesignanMPC-based
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM ABRalgorithmthatisabletogeneralizetoheterogeneousnetwork
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish, anduserconditionswithasuperiorperformance.
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
Infact,thepredictionaccuracyofenvironmentdynamics,such
fee.Requestpermissionsfrompermissions@acm.org.
NOSSDAV’21,September28-October1,2021,Istanbul,Turkey asthenetworkthroughput,isacriticalingredientinthesuccess
©2021AssociationforComputingMachinery. ofMPCandmodel-basedRLmethods,sinceevenasmallbiasmay
ACMISBN978-1-4503-8435-3/21/09...$15.00
https://doi.org/10.1145/3458306.3458872
18

NOSSDAV’21,September28-October1,2021,Istanbul,Turkey NuowenKan,ChenglinLi,CaiyiYang,WenruiDai,JunniZou,HongkaiXiong
significantlyinfluencetheperformanceoflaterplanning[13].How- BayesMPC
BNN(cid:882)based(cid:3)throughput(cid:3)prediction
ever,theconstructionofanaccuratedynamicmodelsremainsan (cid:1868)(cid:4666)(cid:1823)|(cid:2016)(cid:4667) (cid:2198)(cid:2159)(cid:2193) (cid:3404)(cid:2328)(cid:4666)(cid:2246)(cid:2193),(cid:2252)(cid:2193)(cid:4667)
o sh p o e u n ld pr b o e bl j e o m in , tl s y in c c o e n b si o d t e h re th d e d a u l r e i a n t g or m ic o a d n e d lp e r p e is d t i e c m tio ic n u [ n 5 c ] e . r D ta u i e n t t o y Available(cid:3)bitrat B e u (cid:3)v f e fe rs r i (cid:3) o o n c s cu th p N r a e o n t u w c g y h o p rk u (cid:3) t (cid:2159) P V (cid:2193)a a (cid:2879)s r (cid:2778)t i , a (cid:3)t (cid:2159) t h i (cid:2193) o r(cid:2879)o n (cid:2779)u , a (cid:1710) g l(cid:3) h p , p o (cid:2159) u s (cid:2193) t (cid:2879)t e (cid:2194) rior (cid:1823)(cid:2778) (cid:1823)(cid:2779) (cid:2246) (cid:2252)(cid:2193) (cid:2193) (cid:2172)(cid:2159)(cid:2193)(cid:1488)(cid:2159)(cid:2193),(cid:2238) (cid:3404)(cid:2778)(cid:3398)(cid:2238)
Video(cid:3)client(cid:3)states(cid:3) (cid:2246)(cid:2193),(cid:2252)(cid:2193) (cid:3404)(cid:2188)(cid:4666)(cid:2159)(cid:2193)(cid:2879)(cid:2778),(cid:2159)(cid:2193)(cid:2879)(cid:2779),(cid:1710),(cid:2159)(cid:2193)(cid:2879)(cid:2194)|(cid:1823)(cid:4667)
thelimitationthatavideoclientcanhardlyaccesstotheadequate (cid:2201)(cid:2193)(cid:2879)(cid:2778)(cid:3404) (cid:2159)(cid:2193)(cid:2879)(cid:2778),(cid:2158)(cid:2193)(cid:2879)(cid:2778) (cid:1372)(cid:2201)(cid:2193)(cid:3404)(cid:4666)(cid:2159)(cid:2193),(cid:2158)(cid:2193)(cid:4667)
Lower(cid:3)bound(cid:3)of(cid:3)the(cid:3)future(cid:3)throughput (cid:2159)(cid:2193)(cid:2878)(cid:2202),(cid:2238),(cid:1482)(cid:2202)(cid:1488)(cid:2777):(cid:4666)(cid:2176)(cid:3398)(cid:2778)(cid:4667)
networkinformationexceptforthethroughputmeasuredinthe Chunk(cid:3) Uncertainty(cid:882)aware(cid:3)robust(cid:3)MPC(cid:3)strategy
c st h o u c n h k as d t o ic w f n u l t o u a r d e i n n e g t p w e o r r io k d t , h i r t o i u s g th h e p r u e t fo a r n e d c t h h a u ll s e t n h g e in d g yn to am pr i e c d s i o c f t t t h h e e downloa O d p (cid:3) timal(cid:3)b (cid:2200) itr (cid:2193) (cid:1669) ate(cid:3)version (cid:2200)(cid:2193): (cid:1819) (cid:2193) (cid:1813) (cid:3126) . (cid:2176) (cid:1820) (cid:1801) (cid:3127) . (cid:1824) (cid:2778) (cid:1488) (cid:2201) (cid:2332) (cid:2193)(cid:2878) (cid:3533) (cid:2202)(cid:3404) (cid:2176) (cid:2202)(cid:2880) (cid:2879) (cid:2188) (cid:2777) (cid:2778) (cid:2186)(cid:2207) (cid:2173)(cid:2197) (cid:2201) (cid:2161) (cid:2193)(cid:2878)(cid:2202) (cid:2200) (cid:2879) (cid:2193) (cid:2778) (cid:2878) , (cid:2202) (cid:2200) , (cid:2193) (cid:2158) (cid:2878) (cid:2193) (cid:2202) (cid:2878) (cid:2879) (cid:2202) (cid:2778) (cid:4698) , (cid:2159)(cid:2193)(cid:3126) (cid:2202)(cid:2880)(cid:2159) (cid:2201) (cid:2193) (cid:2193) (cid:3126) (cid:2879) (cid:2202) (cid:2778) ,(cid:2238),(cid:1482) (cid:3404) (cid:2202)(cid:1488) (cid:2201) (cid:2777) (cid:1809) :(cid:4666) (cid:1814) (cid:2176) (cid:1809)(cid:1820) (cid:2879) . (cid:2778)(cid:4667)
adaptivevideostreamingsystem[3,15].Ontheotherhand,when
Figure1:SystemframeworkofBayesMPC.
predictionerroroccursinthenear-futurenetworkthroughput,it
hasbeenfoundin[10,20,21]thattherobustsolutionsthataimto
• Withthecapacityofjointlycapturingtheepistemicandaleatoric
maximizetheworst-caseoutcome,surprisinglyoutperformtheso-
uncertainty,aBNN-basedmodelisadoptedtoimprovethepre-
lutionsthattargetattheaverage-caseperformanceintermsofthe
diction accuracy of the network throughput. Meanwhile, the
averageQoE.Thisisbecausetheworst-caseQoEcorrespondstoa
generalizationerrorofthroughputpredictionisguaranteedto
moreconservative(i.e.,lower)throughputprediction,whichcanef-
beminimizedbyusinganegativelog-likelihoodlossfunction
fectivelyreducetheriskofrebufferingeventwhenhighuncertainty
basedonthetheoremofPAC-Bayesian.
existsintheprediction.Notethattherebufferingeventsusually
• Anuncertainty-awarerobustMPCstrategyisthenproposed
haveahighernegativeinfluenceontheuser’sQoEthanthevideo
toimprovetherobustnessofsolutionsthatareobtainedgiven
qualitydegradation.Throughdegradingthevideoquality,these
thepredictedthroughput.Theuncertaintymeasurementoffu-
robuststrategiescaninsteadenlargethebufferoccupancy,which
turepredictionateachstepexactlyindicateshowconfidentthe
inturnintroducesQoEimprovementstothefollowingchunks.
BNN-basedmodelisforthepredictedthroughput,whichcan
Sinceitisimpossibleinpracticetoexactlypredictthetruevalues
significantlyreducetheriskofrebufferingevents.
offuturenetworkthroughput,wearethereforemotivatedbythe
• WeimplementtheproposedBayesMPCforadaptivevideostream-
frameworkofrobustdecision-makingonthebasisofimprovingthe
ingonthreereal-worldnetworktracedatasets,whichisevalu-
capacityofmodelprediction.Unfortunately,itisstillchallengingto
atedunderdifferentnetworkanduserconditionsandcompared
determinetowhatextentthemodelpredictedthroughputshould
tootherbaselines.TheresultsdemonstratethatBayesMPCout-
beloweredtosacrificeforthealgorithm’srobustness[1].Rather
performstheothercomparisonalgorithmsintermsofboththe
thanmerelyconsideringapointestimateforthefuturethroughput
overallQoEperformanceandthegeneralizationperformance
[10,21],wederiveinsteadaconfidenceregionwithinwhichthetrue
acrossallrangesofheterogeneousnetworkanduserconditions.
throughputmaylocatewithahighprobability.Thisregionthen
varieswiththemodelpredictionconfidence,whichmayenlarge
2 SYSTEMDESIGN
whentheuncertaintyincreasesforthemodelpredictionandvice
versa.Targetingatthelowerboundoftheconfidenceregionof Weconsideratypicaladaptivevideostreamingsystem,wherean
predictionthenpreventsthenegativeimpactthatmaybecaused originalvideoistemporallydividedinto𝐾 chunksattheserver.
whenthetruethroughputisworsethanthepredictedone. Eachchunkhasafixedtimeduration𝐿,andisfurtherencodedinto
Followingtheabovemotivation,inthispaper,weproposea severalqualityversionswithdifferentbitrates.Attheclient,abi-
Bayesianneuralnetwork(BNN)-basedrobustABRalgorithm,named tratecontrollerisemployedforrequestinganoptimalversionfrom
BayesMPC,withtheMPC-basedrateadaptationframeworkthat theseavailabebitrateversionsforeachchunk,soastomaximizethe
jointlytakesintoaccountthebufferoccupancyanddynamicsof user’sQoEunderconstrainednetworkthroughput.Here,wefocus
networkthroughput.TheproposedBayesMPCaimstoachieveboth ondesigningarateadaptationalgorithmforthebitratecontroller
superiorandrobustQoEperformanceforadaptivevideostreaming. toselecttheoptimalchunkversionswithassociatedbitrates.
Specifically,weadoptaBNNtomoreaccuratelymodelthetransi- Wedenoteby𝑟 𝑘 ∈Rtheallocatedbitrateforthe𝑘-thchunk𝑈 𝑘,
tiondynamicsofnetworkthroughputmeasuredattheclientside, whereR = {𝑟 1 ,𝑟 2 ,···,𝑟 𝑀 }isthesetof𝑀 availablebitrates.The
withwhichtheprobabilitydistributionoftheneuralnetwork’s bufferoccupancydynamicsofvideoplayercanberepresentedby
weightparametersarelearnttocapturetheepistemicuncertainty
incurredbylackofadequatetrainingsamples.Inaddition,underthe
𝐵 𝑘+1 =[(𝐵 𝑘 −𝑟 𝑘 𝐿/𝐶 𝑘 )++𝐿], (1)
Gaussiandistributionassumptionforthenoiseintroducedinthe where𝐵 𝑘denotesthebufferoccupancywhenthe𝑘-thchunkiscom-
throughputmeasurement,andbyusingthehistoricalthroughput pletelydownloaded,theterm𝑟 𝑘 𝐿/𝐶 𝑘 representsthetimeduration
record,aprobabilitydistributionratherthanapointestimateofthe spentfordownloadingthe𝑘-thchunkwiththeaveragenetwork
nearfuturethroughputcanbepredictedtomeasurethealeatoric throughput denoted by𝐶 𝑘, and the operation (·)+ = max{·,0}
uncertaintyincurredbynoise.Accordingtothejointconsideration ensures the non-negativity of its output. Note that if the term
ofaboveepistemicandaleatoricuncertaintyforfuturethroughput 𝐵 𝑘 −𝑟 𝑘 𝐿/𝐶 𝑘 isnegative,arebufferingeventwilloccur,sinceinthis
prediction,anuncertainty-awarerobuststrategyisthendesigned casetheclienthasnovideoremaininginthebufferwhilethechunk
forreducingtheriskofrebufferingeventandimprovingtheuser’s 𝑈 𝑘hasnotbeencompletelydownloadedyet.Inaddition,wesimply
QoE.Ourmaincontributionsaresummarizedasfollows. definetheobservedstateoftheadaptivevideostreamingsystemas
𝑠 𝑘 =(𝐶 𝑘 ,𝐵 𝑘 ). (2)
19

Uncertainty-AwareRobustAdaptiveVideoStreamingwith
BayesianNeuralNetworkandModelPredictiveControl NOSSDAV’21,September28-October1,2021,Istanbul,Turkey
oversamplesD𝑚
Tomeasuretheuser’sQoE,weadoptawidelyadoptedmetric 1−𝛿 𝑃 ,wehaveforanyposterior𝑄onH that:
t h a t in c lu d e s t h e t ra d e -o ff b et w e en v i d e o qu a l ity , qu a lit y fl uc tuation (cid:7) (cid:8)
|     |     |     |     |     |     |     |     | L(𝑄,D) | ≤Lˆ(𝑄,D𝑚)+ | 1 𝐷 | (𝑄||𝜋)+ln | 1 +Ψ(𝛽,𝑚) | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --------- | --------- | --- |
a n d r is k o f r e b u ff e ri n g e ve n t sb y li n e a r ly c o m b in in g t he m : 𝛽 𝐾𝐿 𝛿 (6)
𝑃
|     |     |     |         |     |         | (cid:3) | (cid:4) |       |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ------- | ------- | ------- | ----- | --- | --- | --- | --- | --- |
|     |     |     | (cid:2) |     | (cid:2) | 𝑟 𝐿     |         | where |     |     |     |     |     |
QoE(𝑟 ,𝑠 )=𝑑(𝑟 )−𝛼 (cid:2)𝑑(𝑟 )−𝑑(𝑟 ) (cid:2)−𝜆 𝑘 −𝐵 , (cid:7) (cid:6)(cid:8)
|     | 𝑘   | 𝑘   | 𝑘 𝑘 | 𝑘−1 |     | 𝐶   | 𝑘 (3) |            |     |         | (cid:5)           |     |       |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ------- | ----------------- | --- | ----- |
|     |     |     |     |     |     | 𝑘   | +     | Ψ(𝛽,𝑚)=lnE |     | E D𝑚exp | 𝛽 L(ℎ,D)−Lˆ(ℎ,D𝑚) |     | , (7) |
ℎ∼𝜋
| wherethequalitymeasurement𝑑(𝑟 |     |     |     | )   |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑘 canbeanyvideoquality L(𝑄,D)=E ℎ∼𝑄 L(ℎ,D)=E ℎ∼𝑄 E (x,y)∈D 𝑙(ℎ,x,y), (8)
metric(e.g.,PSNRorSSIM),and𝛼and𝜆arenon-negativepenalty Lˆ(𝑄,D𝑚)=E Lˆ(ℎ,D𝑚)=E
|     |     |     |     |     |     |     |     |     | ℎ∼𝑄 |     | ℎ∼𝑄 E | (x,y)∈D𝑚 𝑙(ℎ,x,y). | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------------ | --- |
weightstoensurethetemporalqualitysmoothnessandpenalize
therebufferingdelay,respectively. InEq.(6),L(𝑄,D)representsthegeneralizationerror,whichisthe
expectedpredictionerroroverthedatadistributionDandusually
2.1 BNN-BasedThroughputPrediction unknown.Therefore,wetypicallyusetheempiricalriskLˆ(𝑄,D𝑚)
Topredictthefuturethroughput,asshowninFig.1,weadopta insteadtomeasuretheoverallperformanceoftheprediction.Then
inTheorem1,thoughthegeneralizationerrorL(𝑄,D)isunknown
| Bayesianneuralnetwork(BNN)-basedpredictor,𝑓(𝐶 |     |     |     |     |     |     | ,𝐶 ,···, |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
|                                               |     |     |     |     |     | 𝑘−1 | 𝑘−2      |     |     |     |     |     |     |
𝐶 |w),wherewistheweightparameterofthenetworkwith inpractice,wecanobtaintheupperboundofΨ(𝛽,𝑚)independent
𝑘−𝑙
oftheposterior𝑄,aslongasthelossfunctionisbounded,orinthe
valuessampledfromthelearntprobabilitydistribution(i.e.,the
Bayesianposterior).ThestochasticityofweightwenablestheBNN- formofnegativelog-likelihoodorMSE[8].Therefore,forthefixed
|     |     |     |     |     |     |     |     | 𝜋,D,𝑚and𝛿 | 𝑃,minimizingthePAC-BayesboundinTheorem1is |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------------------------------- | --- | --- | --- | --- |
basedpredictortobeawareofepistemicuncertainty,whichstems
equivalenttofindingtheposterior𝑄thatminimizes
fromthelackofsufficientdatasamplestouniquelyidentifythe
underlying true distribution of dynamic transition [5]. In addi- 𝛽Lˆ(𝑄,D𝑚)+𝐷 (𝑄||𝜋).
|       |            |     |                        |     |         |     |            |     |     |     | 𝐾𝐿  |     | (10) |
| ----- | ---------- | --- | ---------------------- | --- | ------- | --- | ---------- | --- | --- | --- | --- | --- | ---- |
| tion, | to capture | the | aleatoric uncertainty, |     | a range | of  | the user’s |     |     |     |     |     |      |
Replacing𝑄with𝑞(w|𝜃)andusingthenegativelog-likelihoodloss
networkthroughputisconsideredratherthanasingledeterminis-
|     |     |     |     |     |     |     |     | function𝑙(ℎ,x,y) |     | =𝑙 =−log𝑝(y|x,w),thecostfunctioninEq. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------------------- | --- | --- | --- |
ticvaluepoint.Motivatedby[1,20],weassumethattheprobability nll
|                                                    |     |     |     |     |     |     |     | (10)canthenberewrittenasfollows,bysetting𝛽 |     |     |     | =1: |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
| ofnetworkthroughputfollowsaGaussiandistribution𝑝(𝐶 |     |     |     |     |     |     | ) = |                                            |     |     |     |     |     |
𝑘
N(𝜇 ,𝜎 ),whereboththemean𝜇 𝑘andstandarddeviation𝜎 −E w∈𝑞(w|𝜃)log𝑝(𝑌|𝑋,w)+𝐷 (𝑞(w|𝜃)||𝜋(w)),
|     | 𝑘 𝑘 |     |     |     |     |     | 𝑘vary |     |     |     | 𝐾𝐿  |     | (11) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---- |
withtime.Therefore,byconstructingtheBNN-basedpredictoras wherelog𝑝(𝑌|𝑋,w) = E (x,y)∈D𝑚log𝑝(y|x,w).Thisshowsthat
(𝜇 𝑘 ,𝜎 𝑘 ) = 𝑓(𝐶 𝑘−1 ,𝐶 𝑘−2 ,···,𝐶 𝑘−𝑙 |w),wecanpredictthefuture theoptimalPAC-Bayesposteriorofnetworkweightw,givenby
throughputthataccountsforboththeepistemicandaleatoricun-
minimizingthePAC-BayesiangeneralizationboundinTheorem1,
certainty.
coincideswiththevariationalBayesianposteriorlearntfromEq.(5)
| Based | on  | Bayesian | inference, | given | a set of𝑚 | training | data |     |     |     |     |     |     |
| ----- | --- | -------- | ---------- | ----- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
ifthelossfunctionisnegativelog-likelihood.
D𝑚 =(𝑋,𝑌),thepredictivedistributionofafuturetruethrough-
WedefineaGaussianvariationalposterior𝑞(w|𝜃)asin[4]by
|       | yˆ = 𝐶 |              |                  | xˆ      | = ( 𝐶 , | 𝐶 , · | · · , 𝐶 ) |     |     |     |     |     |     |
| ----- | ------ | ------------ | ---------------- | ------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
| p u t | 𝑘      | w i t h t he | p a st th ro u g | h p u t | 𝑘 − 1   | 𝑘− 2  | 𝑘 − 𝑙 i s |     |     |     |     |     |     |
𝑝 ( yˆ |x ) = E 𝑝 (y |xˆ , w ), w=𝜇𝑤+log(1+exp(𝜌𝑤))◦𝜖, 𝜃 =(𝜇𝑤,𝜌𝑤), 𝜖 ∼N(0,I). (12)
| gi v | e n by | ˆ   | 𝑝 (w |D 𝑚 ) | ˆ   | w h e r e th | e B a y | e s i a n p o s t e - |     |     |     |     |     |     |
| ---- | ------ | --- | ----------- | --- | ------------ | ------- | --------------------- | --- | --- | --- | --- | --- | --- |
rior𝑝(w|D𝑚)canbeobtainedbytheBayesianrule:
|     |     |     |     |     |     |     |     | Theparameter𝜃 | canbelearntbybackpropagationaccordingto |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------------------------------- | --- | --- | --- | --- |
𝑝(w|D𝑚)∝𝜋(w)𝑝(𝑌|𝑋,w), Eq.(5),withthegradientscalculatedbythemethodproposedin
(4)
[4].Therefore,giventhenetwork’shistoricalthroughput,theprob-
with𝑝(𝑌|𝑋,w)referredtoasthelikelihoodfunctionandtheBayesian abilitydistributionoffuturethroughput𝑝(𝐶 )=N(𝜇 ,𝜎 )canbe
|                                                        |     |     |     |     |     |     |     |                |         |          |         | 𝑘 𝑘               | 𝑘        |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | ------- | ----------------- | -------- |
| prior𝜋(w)assumedtofollowastandardGaussiandistribution. |     |     |     |     |     |     |     | approximatedby |         |          |         |                   |          |
|                                                        |     |     |     |     |     |     |     |                | (cid:9) | (cid:10) | (cid:9) | (cid:11) (cid:12) | (cid:13) |
U n f o r t u n a t el y, th e t r u e B a ye s i an p o s te ri o r i s n o r m a ll y i ntr a c ta b le 𝑛 𝑛 2
|     |     |     |     |     |     |     |     | 𝜇   | = 1 𝜇 | (𝑖), 𝜎 2 = 1 | 𝜎 (𝑖) | +𝑉𝑎𝑟 𝜇 (𝑖) | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ----- | ---------- | --- |
in pr a c t i c e f o r a n e u r a l n e tw o r k o f a n y p r a c t ic a l s iz e . A g e n e ra l 𝑘 𝑛 𝑘 𝑘 𝑛 𝑘 𝑘 (13)
|     |     |     |     |     |     |     |     |     | 𝑖=1 |     | 𝑖=1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alternativefortheBayesianposteriorcalculationistofindavaria- (cid:12) (cid:13) (cid:12) (cid:13)
|     |     |     |     |     |     |     |     |     | (𝑖),𝜎 | (𝑖) |     | |w(𝑖) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
tionalapproximation,whichlearnsadistribution𝑞(w|𝜃)w.r.t.the 𝜇 =𝑓 𝐶 𝑘−1 ,𝐶 𝑘−2 ,···,𝐶 𝑘−𝑙 ,
𝑘 𝑘
| parameter𝜃 |     | forthenetworkweightw.Weshouldthenminimize |     |     |     |     |     |           |                                            |     |     |     |     |
| ---------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --------- | ------------------------------------------ | --- | --- | --- | --- |
|            |     |                                           |     |     |     |     |     | wherew(𝑖) | denotesthe𝑖-thMonteCarlosampledrawnfromthe |     |     |     |     |
theKullback-Leibler(KL)divergencebetweenthetrueBayesian
posterioranditsvariationalposteriorapproximation[4]: variationalposterior𝑞(w|𝜃)with𝑛beingthetotalnumberofsam-
(cid:5) (cid:6) ples,and𝑉𝑎𝑟(·)representsthevarianceofthesesamples.
| 𝜃★=argmin𝐷 |     |     | 𝑞(w|𝜃)||𝑝(w|D𝑚) |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|            |     | 𝐾𝐿  |                 |     |     |     | (5) |     |     |     |     |     |     |
𝜃
|     |         | (cid:7) |                  |     |                   |     | (cid:8) | 2.2 | Uncertainty-AwareRobustMPCStrategy |     |     |     |     |
| --- | ------- | ------- | ---------------- | --- | ----------------- | --- | ------- | --- | ---------------------------------- | --- | --- | --- | --- |
|     | =argmin | 𝐷       | (𝑞(w|𝜃)||𝜋(w))−E |     | 𝑞(w|𝜃)log𝑝(𝑌|𝑋,w) |     | .       |     |                                    |     |     |     |     |
𝐾𝐿
|     |     | 𝜃   |     |     |     |     |     | Toaddresstheissueoftheerrorbetweenthelearntandtruedy- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
Wewillshowbelowthatbyusingthenegativelog-likelihoodloss namics,webuildanentireconfidenceregionC 𝑘,𝛿 = [𝐶 ,𝐶 𝑘,𝛿 ],
𝑘,𝛿
functiontotrainthisBNN-basedpredictor,thegeneralizationerror whichcontainsthetruevalueoffuturenetworkthroughputwitha
probabilityofatleast1−𝛿:
canbeminimizedwiththeguaranteeofPAC-Bayesiantheorem[8],
whichisslightlyrephrasedhereforoursettings. 𝑃(𝐶 ∈C ) ≥1−𝛿, (14)
𝑘 𝑘,𝛿
Theorem1([2]). GivenadatadistributionD,ahypothesisspace wherewedefinetheconfidencelevelas𝛿 ∈ (0,1).Notethataccord-
H,alossfunction𝑙 :H×X×Y →R,apriordistribution𝜋 over ingtoEq.(1),weonlyneedtoconsiderthenetworkthroughput
H,aconfidencelevel𝛿 ∈ (0,1],and𝛽 >0,withprobabilityatleast whenpredictingthefuturedynamicsofthevideoplayer.
𝑃
20

NOSSDAV’21,September28-October1,2021,Istanbul,Turkey NuowenKan,ChenglinLi,CaiyiYang,WenruiDai,JunniZou,HongkaiXiong
Theuncertainty-awarerobustMPCstrategyisthenformulated throughputmeasurementofthelast𝑙 =10chunksarefedintothe
tomaximizetheworst-caseuserQoEw.r.t.theconfidenceregions network.Andtheoutputlayerofthenetworkcontainstwounits
forthefuture𝑇 steps{C
𝑘,𝛿
,C
𝑘+1,𝛿
,...,C
𝑘+𝑇−1,𝛿
},as thatgenerate(𝜇
𝑘
,𝜎
𝑘
)fortheaveragethroughputpredictionofnext
𝑇(cid:9)−1 chunk𝐶 𝑘withthenumberofMonteCarlosamplesinEq.(13)setas
P1: max min QoE(𝑟 𝑘+𝑡 ,𝑠 𝑘+𝑡 ) (15a) 𝑛=10.Inaddition,theten-foldcross-validationmethodisapplied
𝑟𝑘:𝑘+𝑇−1 ∈R𝐶𝑘+𝑡∈C𝑘+𝑡,𝛿,∀𝑡∈0:(𝑇−1) 𝑡=0 toselectthemodelduringthetrainingtoavoidoverfitting.When
planningintheuncertainty-awarerobustMPC,𝑇 =3futuresteps
s.t. 𝑠 𝑘+𝑡 =𝑓dy(𝑠 𝑘+𝑡−1 ,𝑟 𝑘+𝑡−1 ), 𝑠 𝑘−1 =𝑠 init . (15b) aresimulatedformaximizingthesurrogateobjectiveinEq.(16).
where𝑇 ≥ 1isthelengthofstepsforplaning,and𝑓dy(·)repre-
sentsthetransitionfunctionsofthedynamics,characterizedby 3.1.2 Experimentalsetup. ToevaluateandcomparedifferentABR
Eq.(1)and(13).BysolvingProblemP1,wecanobtainthebitrate algorithms,weleveragethevirtualplayerin[16]thatsimulatesthe
sequence𝑟 𝑘 ★ :𝑘+𝑇−1 afterthe(𝑘-1)-thchunk𝑈 𝑘−1 hasbeendown- processofstreamingavideofromtheservertotheclient,wherethe
loadedcompletely,butonlythesolution𝑟 𝑘 ★ isusedastheoptimal networkconditionscanbevariedbyusingthroughputtracesthat
bitrateversionforrequestingthechunk𝑈 𝑘,asillustratedinFig.1. havebeencollectedfromrealusersessions.Forfairness,weuse
Then,were-plantheoptimalbitratesequence𝑟 𝑘 ★ +1:𝑘+𝑇 afterthe𝑘- thesameenvironmentsettingsforthevirtualplayerasin[16]:the
thchunk𝑈 𝑘 hasbeendownloadedcompletely.Byiterativelydoing availablebitratesetisR ={300,750,1200,1850,2850,4300}kbps,
socanwereducetheimpactofpredictionbias. thechunkdurationissetas𝐿=4seconds,andthetotalnumber
ByrecallingtheQoEmetricinEq.(3),wefindthatQoE(𝑟 𝑘 ,𝑠 𝑘 )is ofvideochunksis48.FortheQoEmetricinEq.(3),wealsoadopt
arampfunctionw.r.t.thethroughput𝐶 𝑘.Consequently,wedefine thesamesettingasin[16]that𝛼 =1,and𝜆=4.3ifalinearvideo
asurrogateobjectivefunctionofP1,as qualitymetric𝑑(𝑟
𝑘
) =𝑟
𝑘
/1000isused,and𝜆=2.66otherwiseif
𝑟𝑘:𝑘 m +𝑇 a − x 1 ∈R (cid:9) 𝑇 𝑡= − 0 1 QoE(𝑟 𝑘+𝑡 ,𝐵 𝑘+𝑡 ) (cid:2) (cid:2) 𝐶𝑘+𝑡=𝐶 𝑘+𝑡,𝛿 ,∀𝑡∈0:(𝑇−1) , (16) t u h s e ed lo .H g- e f r o e r i m na v ft i e d r e , o w q e u r a e l f i e t r y t m o e 𝑄 t 𝑜 ri 𝐸 c 𝑙𝑖 𝑑 𝑛 (𝑟 a 𝑘 n ) d = 𝑄 l 𝑜 o 𝐸 g 𝑙 ( 𝑜 𝑟 𝑔 𝑘 a ) s /l t o h g e ( Q m o in E ( m R e ) t ) ri i c s
basedonthelinearandlog-formvideoqualitymetrics,respectively.
whichisthelowerboundoftheobjectivefunctioninEq.(15a).Since
Besides,thebufferoccupancyislimitedas1minute.
ourBNN-basedthroughputpredictionisuncertainty-aware(i.e.,the
varianceofthepredicteddistributionindicateshowconfidentthe
3.1.3 Baselines. WecompareBayesMPCtothefollowingrepresen-
predictednetworkthroughputis),thissurrogateobjectivefunction
tativeABRalgorithmswithdifferenttypesoffundamentalprinciple.
leadstoaconservativeMPCstrategythatmanagestofindacontrol
1)Rate-based:predictsthefuturethroughputbytheharmonicmean
sequencesuchthatno“badevent”(i.e.,rebuffering)wouldoccur.
ofmeasuredaveragethroughputofthepast5chunks.Itthenselects
Then,whenthechunkofdeterminedoptimalbitrateversionis
themaximumbitrateversionconstrainedbythepredictedthrough-
actuallyrequestedbytheuser,avoidanceofrebufferingeventcanbe
put.2)Buffer-based [12]:selectsthebitrateversionaccordingto
guaranteedwithahighprobabilityeventhoughtherearemoderate
thecurrentbufferoccupancybyusingareservoirof5seconds
errorsinthethroughputprediction.
andacushionof10seconds.3)BOLA[19]:apopularbuffer-based
Ataglance,ouruncertainty-awarerobustMPCstrategymay
algorithminpracticethatusesLyapunovoptimizationtoselect
looklikeareminiscentoftherobustversionof[21].However,the
theoptimalbitrateversionundertheconstraintofbufferoccu-
robustnessoftheconservativestrategyin[21]dependsmainlyon
pancyonly.4)RobustMPC[21]:maximizestheQoEmetricwiththe
howlargethepredictionerrorsmeasuredinthepastdownloading
frameworkofMPCbyobservingthedynamicsofbufferoccupancy
chunksare.Itinessenceamountstoaninaccurateestimationthat
andthroughput.Itusesthesameharmonicmean-basedmethod
usesthepastsampledpredictionuncertaintytoapproximatethe
asinRate-basedalgorithm[14]topredictthethroughput,andthe
currentpredictionuncertainty.Incomparison,theuncertaintyesti-
horizonofplanningisthesameasthatinBayesMPC,i.e.,𝑇 =3.In
matedinourstrategyexactlyderivesfromthecurrentprediction
addition,itlowersthepredictedthroughputbyadiscountfactor
process,includingboththeepistemicandaleatoricuncertaintyes-
1/(1+𝑐) forarobustdecision-making,where𝑐 dependsonthe
timation.Inpractice,ouruncertainty-awarerobustMPCstrategy
maximumvalueamongthepast5predictionerrors.5)Pensieve[16]:
performswellwhenwesimplycalculatetheconfidenceregionby:
thestate-of-the-artABRalgorithmthatusestheDRL-basedmethod
C 𝑘,𝛿 =[𝐶 𝑘,𝛿 ,𝐶 𝑘,𝛿 ]=[𝜇 𝑘 −𝑧 𝛿 𝜎 𝑘 ,𝜇 𝑘 +𝑧 𝛿 𝜎 𝑘 ], (17) (A3C)tolearnanoptimalmappingfromthedynamicsofbuffer
where𝑧
𝛿
>0isacontrolparameterrelatedtotheconfidencelevel occupancy,throughputandchunksizetothebitrateselectionof
𝛿,andasmaller𝛿isachievedbyincreasingthevalueof𝑧 𝛿. thenextchunk.
3 EVALUATION 3.1.4 Datasets. Tosimulatevarioususerandnetworkconditions,
wecollectthreepublicdatasets(3G/HSDPA[17],FCC[6]andOboe
3.1 Methodology
[1])forthemodeltraining,testingandtheevaluationofdifferent
3.1.1 Implementation. ForBayesMPC,weconstructaBNNmodel ABRalgorithms.Foreachdataset,80%tracesarerandomlyselected
containing3fullconnectedlayerswhichareallfollowedbyaReLu asthetrainingsetofBayesMPCandPensieve,whiletherest20%
activationfunction.Eachlayerhas100neuralunits,wherethe tracesareusedasthetestingsetofallABRalgorithms.Themean
probabilitydistribution𝑞(w|𝜃)ofnetworkweightwislearnedvia andvariance(representedas𝑥±𝑣𝑎𝑟(𝑥))ofthethroughputvaluesin
variationalapproximationwithaGaussianprior𝜋(w)=N(0,1). HSDPA,FCCandOboedatasetsare1.612±0.950MBps,1.131±0.440
AstheinputoftheBNN-basedthroughputpredictor,theaverage MBpsand2.602±2.081MBps,respectively.
21

Uncertainty-AwareRobustAdaptiveVideoStreamingwith
BayesianNeuralNetworkandModelPredictiveControl NOSSDAV’21,September28-October1,2021,Istanbul,Turkey
Table1:Comparisonoftherobuststrategies.
Methods RobustMPC CNN-PE BNN-PE BayesMPC(𝑧𝛿=1) BayesMPC(𝑧𝛿=1.2) BayesMPC(𝑧𝛿=1.5) BayesMPC(𝑧𝛿=1.7)
Mismatchprob. 0.1215 0.1303 0.0432 0.0405 0.0254 0.0125 0.0084
| Avg.𝑄𝑜𝐸𝑙𝑖𝑛 | 0.8966 | 0.9283 | 1.0767 | 1.0818 | 1.0888                            | 1.0975                             | 1.0749                        |          |
| ---------- | ------ | ------ | ------ | ------ | --------------------------------- | ---------------------------------- | ----------------------------- | -------- |
|            |        |        |        |        |                                   |                                    | BayesMPC Buffer(cid:882)based | Pensieve |
|            |        |        |        |        | BayesMPC Buffer(cid:882)based     | Pensieve                           |                               |          |
|            |        |        |        |        | Rate(cid:882)based RobustMPC      | BOLA eulav(cid:3)EoQ(cid:3)egarevA | Rate(cid:882)based RobustMPC  | BOLA     |
|            |        |        |        |        | eulav(cid:3)EoQ(cid:3)egarevA 1.4 |                                    | 1                             |          |
|            |        |        |        |        | 1.2                               |                                    | 0.8                           |          |
0.6
|     |     |     |     |     | 1   |     | 0.4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.8
0.2
|     |     |     |     |     | 0.6      |         | 0       |         |
| --- | --- | --- | --- | --- | -------- | ------- | ------- | ------- |
|     |     |     |     |     | QoE_lin  | QoE_log | QoE_lin | QoE_log |
|     |     |     |     |     | (a)HSDPA |         | (b)FCC  |         |
Figure3:ComparisonofaverageQoEonHSDPAandFCC.
|     | (a)HSDPA |     | (b)FCC |     |     |     |     |     |
| --- | -------- | --- | ------ | --- | --- | --- | --- | --- |
methods.Thisisbecausetheconfidenceregionderivedfromour
| Figure2:ConfidenceregionC |     | 𝑘,𝛿 (shadedarea)predictedby |     |     |     |     |     |     |
| ------------------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
uncertainty-awarestrategycanadaptbettertotheheterogeneous
BayesMPC,lowerboundpredictedbyRobustMPC,andtrue
userandnetworkconditionswiththecontributionofcaptured
throughputovertworandomlypickedtraces.
epistemicandaleatoricuncertainty.Inaddition,themismatchprob-
|     |     |     |     | abilityofBayesMPCdecreaseswithanincreasing𝑧 |     |     | 𝛿,whichwould |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- | ------------ | --- |
3.2 Results
resultinamoreandmoreconservativebitrateselectionstrategyto
| 3.2.1 Confidenceregionofthroughputprediction. |     |     | Wefirsttrain |     |     |     |     |     |
| --------------------------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- |
reducetherebufferingriskthatisincurredbythemismatchevents
| ourBNN-basedthroughputpredictorwiththetracesfromtraining |     |     |     | (i.e.,theC |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
𝑘,𝛿 isstillgreaterthanthetruethroughputvalue).How-
| sets of HSDPA | and FCC, | and test the | trained model | in testing |     |     |     |     |
| ------------- | -------- | ------------ | ------------- | ---------- | --- | --- | --- | --- |
ever,thereisatrade-offbetweenthequalitydegradationandthe
set.TovalidatetheQoEimprovementgainedfromourproposed
|     |     |     |     | rebufferingriskreductionwhenwechoosethevalueof𝑧 |     |     |     | 𝛿.Results |
| --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --------- |
BNN-basedthroughputpredictionmethod,wecompareBayesMPC
inTable1suggeststhatthemaximumQoEvaluecanbeachieved
withRobustMPC,CNN-PEandBNN-PE,wherePEstandsforpoint
when𝑧 =1.5andthereforeweusethissettinginthefollowing
𝛿
| estimate of | throughput. These | three comparison | algorithms | all |     |     |     |     |
| ----------- | ----------------- | ---------------- | ---------- | --- | --- | --- | --- | --- |
experiments.InFig.2,wedepicttheconfidenceregionspredicted
usetheheuristicrobuststrategyinRobustMPC(i.e.,thepredicted byBayesMPC(𝑧 =1.5),thelowerboundpredictedbyRobustMPC
| throughputmultipliedwithadiscountfactor1/(1+𝑐),where𝑐is |     |     |     |     | 𝛿   |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
andthetruethroughputovertworandomlypickedtracesfromtest
themaximumpredictionerrorofthepast5predictions).Thesolely
setsofHSDPAandFCC,showingthatourpredictedlowerbound
differencebetweenthemisthatRobustMPCusestheharmonic
isalwayslowerthanthetruethroughputwhileRobustMPCisnot.
meantopredictthethroughput,whileBNN-PEpartiallyusesour
proposed BNN-based predictor (i.e., taking 𝜇 as the predicted 3.2.2 BayesMPCvs.baselineABRalgorithms. Wethencompare
𝑘
throughputandthencalculatingthelowerboundby1/(1+𝑐))and
BayesMPCwithbaselineABRalgorithmsintermsoftheQoEper-
CNN-PEusesaCNN-basedpredictortopredictthethroughputin formanceinvarioususer/networkconditionsanddifferentQoE
asimilarmethod.Forfairness,theCNN-basedpredictoradoptsa metrics.Beforeevaluation,wetrainBayesMPCandPensieveonly
1-DCNNlayerwithkernel=1,channels=128attheinputlayer,
withthetrainingdatasetsofHSDPAandFCC.ThetracesinOboe
andthefollowingarchitectureisthesameasBayesMPC.Itshould areabandonedinthemodeltrainingandonlyusedastheunfamil-
benotedthattheCNN-basedpredictorcannotlearntheepistemic iarnetworkconditionsfortestingthegeneralizationperformance.
uncertaintyduetoitsdeterministicnatureofnetworkweight. Fig.3andFig.4showtheresultsofaverageQoEvalueswith𝑄𝑜𝐸
𝑙𝑖𝑛
| Table1showscomparisonresultsofthemismatchprobability |     |     |     | and𝑄𝑜𝐸 |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- |
𝑙𝑜𝑔metricsettingsforHSDPAandFCCtestdatasets,re-
oftruethroughputvaluebeingsmallerthanthelowerboundof spectively.Specifically,wesimulatethestreamingofasamevideo
predictedthroughput,andtheaverage𝑄𝑜𝐸
𝑙𝑖𝑛valueoverthetest onceoneachtestingtrace,whichiscalledasession.Wethencalcu-
datasetsofHSDPAandFCC.ResultsinColumns2−4validatethe
latetheaverageQoEvalueofvideochunksforeachsession,and
superiorperformanceofBNNinthroughputpredictionascom- depictthecumulativedistributionfunctionofallsessions.
paredtomethodsusingtheharmonicmeanandCNN.TheBNN-PE Throughtheexperimentalresultswecanseeseveralkeypoints
improvestheaverageQoEvaluebyabout20%anddecreasesthe ofBayesMPC.First,wefindthatBayesMPC eithermatcheswith
mismatchprobabilitybyatleast7.8%,comparedtoRobustMPCand orexceedstheperformanceofthebestbaselinealgorithmsunder
CNN-PE.Furthermore,resultsinColumns4−8ofTable1show
differentQoEmetricsettingsandnetworkconditions.Themost
theperformanceofourproposeduncertainty-awarerobuststrat- competitivebaselineisPensieve,whichhasaslightlyworseperfor-
| egywithdifferentchoicesof𝑧 |     |                              |     | mancethanBayesMPCforthe𝑄𝑜𝐸 |     |                            |     |     |
| -------------------------- | --- | ---------------------------- | --- | -------------------------- | --- | -------------------------- | --- | --- |
|                            |     | 𝛿,whichcontrolstherangeofthe |     |                            |     | 𝑙𝑖𝑛metricandHSDPAtraces,as |     |     |
confidenceregion.RecallthatBNN-PEcalculatesthelowerbound showninFigs.3and4(a).Then,fortheothersettingsasshownin
ofpredictedthroughputbasedonestimationofasinglethroughput Figs.3and4(b)-4(d),theperformancegainofBayesMPCoverPen-
value.Incontrast,BayesMPCdeterminestheconfidenceregionof sievebecomesmoresignificant,whichincreasesto5.0%for𝑄𝑜𝐸
𝑙𝑜𝑔
thetruethroughputasinEq.(17)forthenextchunkateachstep metricandHSDPAtraces,andatleast9.0%for𝑄𝑜𝐸 𝑙𝑜𝑔/𝑄𝑜𝐸 𝑙𝑖𝑛met-
ofplanning,andusesthelowerboundC astheconstraintofthe ricandFCCtraces.Inaddition,asthemostpopularnon-ML-based
𝑘,𝛿
surrogateobjectivefunctioninEq.(16).Itcanbeseenthatthepro- ABRalgorithms,BOLAandRobustMPCachievethesimilarperfor-
posedBayesMPCachievesgenerallyasmallermismatchprobability manceinallsettings,whichhoweverisatleast10%and24%lessin
andahigheraverage𝑄𝑜𝐸
𝑙𝑖𝑛ascomparedtotheothercomparison termsoftheQoEperformancethanBayesMPContheHSDPAtraces
22

NOSSDAV’21,September28-October1,2021,Istanbul,Turkey NuowenKan,ChenglinLi,CaiyiYang,WenruiDai,JunniZou,HongkaiXiong
(a) (b) (c) (d)
Figure4:ComparisonoftheQoEperformancewiththelinearandlog-formmetricsettingsonHSDPAandFCC.
0.8
0.6
0.4
0.2
0
Bitrate(cid:3)utility Rebuffering(cid:3)penalty Smoothness(cid:3)penalty
eulav(cid:3)EoQ(cid:3)egarevA BayesMPC Buffer(cid:882)based Pensieve Rate(cid:882)based RobustMPC BOLA
(a)𝑄𝑜𝐸𝑙𝑖𝑛(HSDPA+FCC)
0.8
0.6
0.4
0.2
0
Bitrate(cid:3)utility Rebuffering(cid:3)penalty Smoothness(cid:3)penalty
eulav(cid:3)EoQ(cid:3)egarevA BayesMPC Buffer(cid:882)based Pensieve Rate(cid:882)based RobustMPC BOLA
(a) (b)
Figure 6: Comparison of QoE performance on unfamiliar
tracesfromOboe,withlinearandlog-formmetricsettings.
(b)𝑄𝑜𝐸𝑙𝑜𝑔(HSDPA+FCC) TofurtherexplorethegeneralizationperformanceofBayesMPC
underanunfamiliarnetworkcondition,weevaluatethedifferent
Figure 5: Comparison of individual components of𝑄𝑜𝐸 𝑙𝑖𝑛 ABRalgorithmsonthetracesofOboe,noneofwhichhasbeen
and𝑄𝑜𝐸 𝑙𝑜𝑔overallsessionstestedonFCCandHSDPA. experienced during the training process of BayesMPC and Pen-
sieve. Fig. 6 shows the results of average QoE values achieved
andFCCtraces,respectively.Second,weobservethatBayesMPC
byBayesMPCandotherbaselinealgorithms.Itcanbefoundthat
performsmoresuperiorontracesofFCCthanthoseofHSDPAno
matterwhenthe𝑄𝑜𝐸 𝑙𝑖𝑛or𝑄𝑜𝐸 𝑙𝑜𝑔isused.Theperformancegain BayesMPCstillperformsbestinthetracesofOboealthoughthe
performancegainoverotherbaselinesgetsnarrow.Thisisbecause
ofBayesMPCoverotherbaselinealgorithmsincreasestoatleast
9%onsessionsofFCCfromonly0.05%onsessionsofHSDPA.This
thatthemeanvalueofthethroughputinOboeincreasesto2.6
MBps(from1.6MBpsinHSDPAand1.1MBpsinFCC),sotherisk
showsthatBayesMPCcanadapttodifferentnetworkconditionsno
ofrebufferingeventcanalsobereducedwhenahighbitrateversion
mattertheyarestableorvariable(thevarianceofthroughputvalue
inFCCandHSDPAare0.440and0.950,respectively),whileother ischosennomatterwhichalgorithmisadopted.Comparedwith
theaverageQoEachievedbyRobustMPC,BayesMPCachievesat
baselinealgorithms,suchasPensieve,canhardlylearnageneral-
least5%highervalueswhiletheaverageQoEforPensieveisonly
izedbitrateselectionstrategythatperformsuniformlywellacross
3.4%and1.2%higher,respectively.ThisshowsthatBayesMPChas
therangeofconditionsseenbothinFCCandHSDPA.Althoughit
amorestableperformance(i.e.,bettergeneralizationperformance)
ischallengingtopredictthefuturethroughputinheterogeneous
thanPensieveonuntrained(i.e.,unseen)networkconditions.
networkconditions,BayesMPCcanperformwellthankstoitsmin-
imizedgeneralizationerrorofprediction,whichisguaranteedby 4 CONCLUSION
thePAC-Bayesiantheorem.
Wehaveproposedinthispaperanuncertainty-awarerobustABR
Fig.5showstheaveragevalueofthreeindividualcomponentsin
algorithmforadaptivevideostreaming,calledBayesMPC.ABNN-
differentQoEmetricsoverallsessionstestedonFCCandHSDPA
basedthroughputpredictorwasadoptedtocapturetheepistemic
datasets.Notethattheaveragevalueshowninthehistogramsare
andaleatoricuncertainty,whiletheminimumgeneralizationerror
processedbylog(1.2+𝑣𝑎𝑙𝑢𝑒)forabetterviewing.Althoughthe
ofthroughputpredictionhasbeenguaranteedwithPAC-Bayesian
videoquality(i.e,bitrateutility)ismeasuredbydifferentmetrics,
theorem.Thelearntuncertaintywasusedtobuildaconfidencere-
theoveralltrade-offbetweentheutility,thepenaltyofsmoothness
gionforthefuturethroughput,thelowerboundofwhichwasthen
andrebuffering,whichisachievedbyeachalgorithmissimilar
adoptedtoformulateanuncertainty-awarerobustMPCstrategy.
inFigs.5(a)and5(b).ItcanbenotedthatBayesMPCcanalways
Evaluationsonthreereal-worldnetworktracedatasetshavedemon-
achievetheoptimaltrade-offthatthebitrateutilityismaximized
stratedsuperiorperformanceofBayesMPCoverotherbaselines,in
whilekeepingtherebufferingandsmoothnesspenaltyinarelative
termsofboththeoverallQoEandgeneralizationperformance.
lowlevel,whichisalsosimilarinresultsachievedbyPensieve.
ACKNOWLEDGMENTS
Moreover,theRobustMPCsuffersfrommuchrebufferingpenalty
duetoitsinaccuratethroughputpredictionmethodalthoughitcan ThisworkwassupportedinpartbytheNationalNaturalScience
achieveahighbitrateutility.Incontrast,thereceivedsmoothness FoundationofChinaunderGrants61871267,61931023,61972256
penaltyintheresultsofBOLAandBuffer-basedisoutofcontrol and61971285,andsupportedinpartbyShanghaiRising-StarPro-
thoughtheyachieveagoodperformanceintermsofthebitrate gramunderGrant20QA1404600.
utilityandrebufferingpenalty.
23

Uncertainty-AwareRobustAdaptiveVideoStreamingwith
BayesianNeuralNetworkandModelPredictiveControl NOSSDAV’21,September28-October1,2021,Istanbul,Turkey
REFERENCES NetworkandOperatingSystemsSupportforDigitalAudioandVideo.NewYork,
[1] ZahaibAkhtar,YunSeongNam,RameshGovindan,SanjayRao,JessicaChen, NY,USA,7–13.
EthanKatz-Bassett,BrunoRibeiro,JibinZhan,andHuiZhang.2018. Oboe: [12] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMark
Auto-TuningVideoABRAlgorithmstoNetworkConditions.InProceedingsof Watson.2014. ABuffer-BasedApproachtoRateAdaptation:Evidencefrom
the2018ConferenceoftheACMSpecialInterestGrouponDataCommunication. aLargeVideoStreamingService.InProceedingsoftheConferenceoftheACM
NewYork,NY,USA,44–58. SpecialInterestGrouponDataCommunication.NewYork,NY,USA,187–198.
[2] PierreAlquier,JamesRidgway,andNicolasChopin.2016.OnthePropertiesof [13] MichaelJanner,JustinFu,MarvinZhang,andSergeyLevine.2019. Whento
VariationalApproximationsofGibbsPosteriors. JournalofMachineLearning TrustYourModel:Model-BasedPolicyOptimization. arXiv:1906.08253[cs.LG]
Research17,236(2016),1–41. [14] JunchenJiang,VyasSekar,andHuiZhang.2014. ImprovingFairness,Effi-
[3] AbdelhakBentaleb,ChristianTimmerer,AliC.Begen,andRogerZimmermann. ciency,andStabilityinHTTP-BasedAdaptiveVideoStreamingWithFESTIVE.
2019.BandwidthPredictioninLow-LatencyChunkedStreaming.InProceedings IEEE/ACMTransactionsonNetworking22,1(Feb2014),326–340.
ofthe29thACMWorkshoponNetworkandOperatingSystemsSupportforDigital [15] ZhiLi,XiaoqingZhu,JoshuaGahm,RongPan,HaoHu,AliC.Begen,andDavid
AudioandVideo.NewYork,NY,USA,7–13. Oran.2014.ProbeandAdapt:RateAdaptationforHTTPVideoStreamingAt
[4] CharlesBlundell,JulienCornebise,KorayKavukcuoglu,andDaanWierstra.2015. Scale.IEEEJournalonSelectedAreasinCommunications32,4(2014),719–733.
WeightUncertaintyinNeuralNetwork.InProceedingsofthe32ndInternational [16] HongziMao,RaviNetravali,andMohammadAlizadeh.2017.NeuralAdaptive
ConferenceonMachineLearning,Vol.37.1613–1622. VideoStreamingwithPensieve.InProceedingsoftheConferenceoftheACM
[5] KurtlandChua,RobertoCalandra,RowanMcAllister,andSergeyLevine.2018. SpecialInterestGrouponDataCommunication.NewYork,NY,USA,197–210.
DeepReinforcementLearninginaHandfulofTrialsUsingProbabilisticDynamics [17] HaakonRiiser,PaulVigmostad,CarstenGriwodz,andPålHalvorsen.2013.Com-
Models.InAdvancesinNeuralInformationProcessingSystems.RedHook,NY, mutePathBandwidthTracesfrom3GNetworks:AnalysisandApplications.In
USA,4759–4770. Proceedingsofthe4thACMMultimediaSystemsConference.NewYork,NY,USA,
[6] FederalCommunicationsCommission.[n.d.]. RawData-MeasuringBroad- 114–118.
bandAmerica.(2016).https://www.fcc.gov/reports-research/reports/measuring- [18] Satadal.Sengupta,NiloyGanguly,SandipChakraborty,andPradiptaDe.2018.
broadband-america/raw-data-measuring-broadband-america-2016. HotDASH:HotspotAwareAdaptiveVideoStreamingUsingDeepReinforcement
[7] MatteoGadaleta,FedericoChiariotti,MicheleRossi,andAndreaZanella.2017. Learning.In2018IEEE26thInternationalConferenceonNetworkProtocols(ICNP).
D-DASH:ADeepQ-LearningFrameworkforDASHVideoStreaming. IEEE 165–175.
TransactionsonCognitiveCommunicationsandNetworking3,4(2017),703–718. [19] KevinSpiteri,RahulUrgaonkar,andRameshSitaraman.2016. BOLA:Near-
[8] PascalGermain,FrancisBach,AlexandreLacoste,andSimonLacoste-Julien. OptimalBitrateAdaptationforOnlineVideos.InProceedingsofthe35thAnnual
2016.PAC-BayesianTheoryMeetsBayesianInference.InAdvancesinNeural IEEEInternationalConferenceonComputerCommunications.1–9.
InformationProcessingSystems,Vol.29.1884–1892. [20] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,Tao
[9] PeterHenderson,RiashatIslam,PhilipBachman,JoellePineau,DoinaPre- Liu,andBrunoSinopoli.2016. CS2P:ImprovingVideoBitrateSelectionand
cup, and David Meger. 2019. Deep Reinforcement Learning that Matters. AdaptationwithData-DrivenThroughputPrediction.InProceedingsoftheCon-
arXiv:1709.06560[cs.LG] ferenceoftheACMSpecialInterestGrouponDataCommunication.NewYork,NY,
[10] TianchiHuangandLifengSun.2020.DeepMPC:AMixtureABRApproachvia USA,272–285.
DeepLearningandMPC.InProceedingsofthe2020IEEEInternationalConference [21] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.AControl-
onImageProcessing(ICIP).1231–1235. TheoreticApproachforDynamicAdaptiveVideoStreamingoverHTTP.In
[11] TianchiHuang,Rui-XiaoZhang,andLifengSun.2020.Self-PlayReinforcement Proceedingsofthe2015ACMConferenceonSpecialInterestGrouponDataCom-
LearningforVideoTransmission.InProceedingsofthe30thACMWorkshopon munication.NewYork,NY,USA,325–338.
24