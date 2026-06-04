SODA: An Adaptive Bitrate Controller for Consistent
High-Quality Video Streaming
TianyuChen YihengLin NicolasChristianson
UniversityofMassachusettsAmherst CaliforniaInstituteofTechnology CaliforniaInstituteofTechnology
Amherst,MA,USA Pasadena,CA,USA Pasadena,CA,USA
tianyuchen@umass.edu yihengl@caltech.edu nchristianson@caltech.edu
ZahaibAkhtar SharathDharmaji MohammadHajiesmaili
AmazonPrimeVideo/NCSU AmazonPrimeVideo UniversityofMassachusettsAmherst
Sunnyvale,CA,USA Sunnyvale,CA,USA Amherst,MA,USA
akhtz@amazon.com sharatdr@amazon.com hajiesmaili@cs.umass.edu
AdamWierman RameshK.Sitaraman
CaliforniaInstituteofTechnology UniversityofMassachusettsAmherst
Pasadena,CA,USA Amherst,MA,USA
adamw@caltech.edu ramesh@cs.umass.edu
ABSTRACT KEYWORDS
Theprimaryobjectiveofadaptivebitrate(ABR)streamingisto Adaptivebitratestreaming,Smoothedonlineconvexoptimization
enhanceusers’qualityofexperience(QoE)bydynamicallyadjust-
ACMReferenceFormat:
ingthevideobitrateinresponsetochangingnetworkconditions.
TianyuChen,YihengLin,NicolasChristianson,ZahaibAkhtar,Sharath
However,usersoftenfindfrequentbitrateswitchingfrustrating Dharmaji,MohammadHajiesmaili,AdamWierman,andRameshK.Sitara-
duetotheresultinginconsistencyinvisualqualityovertime,es- man.2024.SODA:AnAdaptiveBitrateControllerforConsistentHigh-
peciallyduringlivestreamingwhenbufferlengthsareshort.In QualityVideoStreaming.InACMSIGCOMM2024Conference(ACMSIG-
thispaper,weproposeapracticalsmoothnessoptimizeddynamic COMM’24),August4–8,2024,Sydney,NSW,Australia.ACM,NewYork,NY,
adaptive(SODA)controllerthatspecificallyaddressesthisproblem USA,32pages.https://doi.org/10.1145/3651890.3672260
whileremainingdeployable.SODAisbackedbytheoreticalguaran-
1 INTRODUCTION
teesandhasshownsuperiorperformanceinempiricalevaluations.
Specifically,ournumericalsimulationsshowa9.55%to27.8%QoE Withthegrowthofonlinevideostreaming,usersnowadaysstream
improvementandourprototypeevaluationshowsa30.4%QoEim- videosfromahighlydiversesetofdevices,includinglaptops,mobile
provementcomparedtothestate-of-the-artbaselines.Inordertobe devices,smartTVs,set-topboxes,gameconsoles,etc.Thesedevices
widelydeployable,SODAperformsbitratehorizonplanninginpoly- spanawidespectrumofhardwarecapabilitiesandconnecttothe
nomialtimecomparedtobruteforceapproachesthatsufferfrom Internetinamultitudeofways,e.g.,wireless,cellular,cable,etc.To
exponentialcomplexity.Todemonstrateitsreal-worldpracticality, ensureahighqualityofexperience(QoE)acrossalldevices,video
wedeployedSODAonawiderangeofdeviceswithintheproduction providersutilizeadaptivebitrate(ABR)streamingthattailorsvideo
networkofAmazonPrimeVideo.Productionexperimentsshow deliverytospecificdevicesandnetworkconditions.
thatSODAreducedbitrateswitchingbyupto88.8%andincreased ThegoalofABRstreamingistodeliveravideoatthehighestsus-
averagestreamviewingdurationbyupto5.91%comparedtoa tainablequalityovertime-varyingnetworkconditions.Toachieve
fine-tunedproductionbaseline. this,avideosourceisencodedatdifferentbitratescorresponding
todifferentresolutions,e.g.,720p,1080p,1440p,etc.Eachencod-
CCSCONCEPTS
ingisinturntemporallypartitionedintoasequenceofsegments,
e.g.,2secondsofvideocontent.AnABRcontrollerinsideauser’s
•Informationsystems→Multimediastreaming;•Theoryof
videoplayerthenselectsasuitablebitrateforeachsegment.Finally,
computation→Onlinealgorithms;Theoryandalgorithms
downloadedsegmentsarestoredinabuffer,tilltheyarerendered.
forapplicationdomains.
Paststudieshaveshownthatauser’sQoEismaximizedbyde-
livering the video at the highest possible quality with minimal
rebufferingandbitrateswitching.Ithasbeenshownthata1%in-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor creaseinrebufferingtimeiscorrelatedwitha3-minutereductionin
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed theviewingduration[7]andfrequentbitrateswitchingisstrongly
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
correlatedwithauserabandoningthesession[21].Goingbeyond
onthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored.
Forallotheruses,contacttheowner/author(s). correlationalstudies,thesignificantcausalimpactofrebuffering
ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia andotherQoEperformancemetricsonkeymeasuresofuserbehav-
©2024Copyrightheldbytheowner/author(s). iorwasfirstestablishedin[9].However,jointlyoptimizingallthree
ACMISBN979-8-4007-0614-1/24/08
https://doi.org/10.1145/3651890.3672260 keycomponentsofQoE,i.e.,videoquality,rebufferingandbitrate
613

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
Figure2:BOLA’s[44]decisionboundariesarespacedoutfor
on-demandstreaming,buttinyfluctuationsinbufferlevel
Figure1:Videostreamdurationisnegativelycorrelatedwith cancausebitrateswitchingforlivestreaming.
bitrateswitchingrate.Userswatch<10%ofthestreamwhen
bitrateswitchingrateis>20%.
27.8%QoEimprovementandourprototypeevaluationshowsa
30.4%QoEimprovementcomparedtothestate-of-the-artbase-
lines.ProductionlivestreamingexperimentsinAmazonPrime
switching,isnon-trivialastheyarelockedinathree-waytrade-off.
AnidealABRcontrollerseekstopushthetrade-offboundaryand
VideoshowthatSODAreducedbitrateswitchingbyasignificant
upto88.8%andincreasedaveragestreamviewingdurationby
optimizeallthreeQoEcomponentssimultaneously.
upto5.91%(>5minuteslongersessions)comparedtoafine-
Betweenon-demandandlivestreaming,thelatterismorechal-
tunedproductionbaseline.SeeTable1forasummaryofourkey
lengingastheplayerbufferisrestrictedto10-20seconds(toremain
closetoactualliveaction),whichisincontrastto60-180seconds
findingsaboutSODAascomparedtobaselineABRcontrollers.
ofbufferinon-demandstreaming.Consequently,livestreaming
3) RobustnessAgainstThroughputPredictionErrors.Most
ABRcontrollersrelyonandaresensitivetopredictionsofthe
hashighersusceptibilitytorebufferingandbitrateswitching.To
futurenetworkthroughput.OurSOCOframeworkallowsusto
understandtheimpactofbitrateswitching,Figure1showsthere-
lationshipbetweentheviewingpercentageofastreamandbitrate
designrobustABRcontrollersthatareprovablyrobustagainst
switchingrateforasportseventonalarge-scalevideostreaming
predictionerrors.Specifically,weshowthatSODAhastheex-
provider.Tominimizepotentialconfounderssuchasrebuffering
ponentiallydecayingperturbationproperty[49,55,56],i.e.,the
futureimpactofpredictionerrorsdecayrapidlyovertime.A
andlowquality,theplotisfocusedonshort-livedsessions(<25%
keytoourproofmethodologyisthatweshiftedfromthecon-
ofstreamviewed)withatleastHDqualityandnorebuffering.The
ventionalsegment-basedABRformulationandadoptedanovel
lineofbestfitshowsthatuserswatch<10%ofthestreamwhen
bitrateswitchingrateis>20%.WhileourproposedABRcontroller
time-basedperspective.
worksforbothon-demandandlivestreaming,ourevaluationsuse
4) EfficientImplementationforProductionDeployment.ABR
controllersdeployedinthefieldneedtoworkonawiderange
livestreamsthatrepresentsamorechallengingusecase.
ofclientdevices,includinglow-endoneswithlimitedcomputa-
OurContributions.Weproposeanovelsmoothnessoptimized
tionalresources.ManyABRcontrollersproposedintheresearch
dynamicadaptive(SODA)controllerthatprovidestheoreticalQoE
literaturedonotmeettheefficiencybarforaproductionde-
guarantees while exhibiting superior empirical performance in
ploymentandareneverimplementedinpractice.Wemaximized
simulation,prototype,andproductionexperiments.Wemakethe
followingspecificcontributions:
SODA’sruntimeanddeploymentpracticalitybydevisingacom-
putationallyefficientmethodtosearchfornear-optimalbitrate
1) TheoreticalFoundationsofABRControllerDesign.SODA decisions,whichreducedtheruntimecomplexityfromexponen-
isthefirstABRcontrollertoprovably optimizeallthree key tialtopolynomial,e.g.,about200iterationsmaxinpractice.In
componentsofQoE,namely,videoquality,rebufferingandbi- addition,wemadeSODArobustagainstthroughputprediction
trateswitching.UnlikepriorworksuchasBOLA[36,44]thatuse errorsbydesign,thuseliminatingtheneedforsophisticated
Lyapunovmethodstooptimizethefirsttwocomponents,we computationally-intensivethroughputpredictors.
useanewframeworkbasedonrecentadvancesinsmoothed
Thisworkdoesnotraiseanyethicalissues.
onlineconvexoptimization(SOCO)[13,25,26,33–35,43]to
simultaneouslyoptimizeallthreeQoEcomponents.Toenable
2 DESIGNGAPS,OPPORTUNITIES,AND
theapplicationofSOCO,wemodeltherebufferingminimiza-
tionrequirementinanovelfashionusingthenotionofbuffer REQUIREMENTS
stability.WeprovethatSODAisnear-optimalandachievesQoE DesignGaps.Livestreamingposestheadditionalconstraintof
withinasmallfactoroftheofflineoptimalQoE(Theorem4.1). nearreal-timedeliverywhichmakesbitrateadaptationmorechal-
2) Better QoE Across Empirical Evaluations. We evaluated lenging than that in on-demand streaming. Figure 2 shows the
SODAinthreesettings:numericalsimulations,prototypeevalua- bitrateselectionfunctionof BOLA[36,40,44],anABRcontroller
tion,andproductiondeploymentwithinAmazonPrimeVideo thatiswidelydeployedbyvideoprovidersandispartoftherefer-
servingactualusers.Ournumericalsimulationsshowa9.55%to enceMPEG-DASHvideoplayer[64].Noticethatforon-demand
614

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
Table1:AqualitativesummaryofourkeyevaluationfindingsaboutSODAascomparedtobaselineABRcontrollers.
Controller Theorya VideoQuality RebufferingTime SwitchingRate Deployability
SODA Q+R+S high short ultralow high
HYB[24] none high medium high high
BOLA[44] Q+R high short high high
Dynamic[36] Q+R high short medium high
MPC[17] none high long low low
Fugu[46] none high medium low low
CausalSimRL[60] none high short high low
aQ,R,Sstandfortheoreticalguaranteesforquality,rebuffering,andswitchingrespectively.
usedby[17,22].Noticethatbeyond70seconds,RobustMPCre-
peatedlyrebuffersbutcontinuestodownloadthehighestbitrate
(Figure3bottomplot),resultingin29rebufferingeventsover200
seconds.Strikingly,thisbehaviorisinfacttheoptimalbehavior
underRobustMPC’sobjectivefunctionwhichtoleratesrebuffering
topreventbitrateswitches.Onthesurface,thissuggestshigher
rebufferingpenaltyintheobjectivefunction,however,higher
penaltiesonlyreducethedurationofthesetolerablerebuffersbut
donoteliminatethem.Indeed,pastworkhasempiricallyshown
thatevena20×bufferingpenaltyhasmarginalimpact[24].
• Varianceinnetworkconditionsorthroughputpredictionerrors
arenotwelltoleratedbyexistingcontrollers.Pastworkshave
shownthatRobustMPCincurs26%morerebufferingeventsunless
pairedwithasophisticatedthroughputpredictor[46,50].Simi-
Figure3:ARobustMPCsessionwherethecontrollerintention- larly,learning-basedcontrollerslikePensievetendtodegrade
allyrebuffersinsteadofloweringthebitrate. inperformancewhentrainedforrealisticnetworkconditions
encounteredinthewild[24].Inpractice,accuratethroughput
predictionsarehardbecauseofseveralfactors,including(i)de-
viceandOSlevelinefficiencies[18],(ii)stop-startnatureofvideo
streaming,alongerbufferof120secondsensuresthatbitratejumps
requestswhichdonotinteractwellwithTCP[8,18],and(iii)
arespacedwellapart(upto20seconds),however,forlivestreaming
volatilenetworkconditionstypicalinproductionnetworks[1,5,
withabufferof20seconds,bitratesfluctuatewithsmalldeviations
45].Tomakemattersworse,sophisticatedthroughputpredictors
of1-3secondsinthebuffersize.Thiscancausebitratestoswitch
arethemselvesnotnecessarilyaccurate[16]andarechallenging
frequently.WhilecontrollerssuchasMPC[17]andPensieve[22]
todeployduetodevicelevelbottlenecks[58].Therefore,in-the-
offerrespitebyexplicitlypenalizingbitrateswitching,thesecon-
wildperformanceofthesecontrollersremainsquestionable.
trollerssufferfromshortcomingsoftheirown:
• Modelpredictivecontrollersarehardtodeployatscalebecause Opportunities.Outsideofthevideostreamingliterature,the
theyneedtosolveanon-linearintegerprogrammingproblem interactionoflearningandcontrolhasblossomedinrecentyears,
overapredictionhorizonof𝐾 segments,e.g.,𝐾 =5,whichisso leadingtonewandexcitingapproachestocontrollerdesigns[39,
computationallyexpensivethatitisquickertodownloadavideo 47,49,52,54].However,thesenewapproacheshavenotyetbeen
segmentthantoobtainabitratedecision[17,19].Workarounds applied and evaluated in the context of video streaming where
suchaspre-computedlookuptables[17]areimpracticalforlive classical model predictive and proportional–integral–derivative
streamingwherethevideoisnotavailableapriori.Inasimi- controlhaveremainedthefocus,e.g.,[17,23].Inparticular,the
larvein,learning-basedcontrollerssuchasPensieve[22]work area of smoothed online convex optimization (SOCO) has seen
optimallywhentrainedspecificallyforagivensetofbitrates, multiplebreakthroughsinrecentyears[13,25,33,35],including
segmentduration,networkconditions,etc.Givenin-the-wild thedevelopmentofconnectionstomodelpredictivecontrollers[26,
diversityanditsevolvingnature,ensuringthisspecificityim- 47,49,52,56].SOCOprovidesasystematicframeworktobalance
posesasignificantoperationaloverhead.Furthermore,evenif anobjectivefunctionwithactionswitching.Itthuslendsitselfwell
specificallytrained,achievingperformanceguaranteeswiththese tovideostreaming,whichneedstojointlyoptimizevideoquality,
learning-basedcontrollersisshowntobechallenging[24]. sustainedplayback,andbitratesmoothness.
• ExistingABRcontrollersnaivelyreducebitrateswitchingatthe Requirements.Drivenbytheabovedesigngapsandoppor-
expenseoflowvideoqualityormorerebuffering.Todemonstrate tunities,weidentifythreerequirementsthatSODAshoulddeliver.
this,Figure3showsaRobustMPCsessionwiththeexactsetup Inparticular,SODAshould(i)achievebitratesmoothnesswithout
615

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
sacrificingvideoqualityorsustainedplayback,(ii)berobustagainst
volatilenetworkconditions,and(iii)beeasytodeployinpractice.
Beforedelvingintothedetailsintheremainderofthepaper,we
provideabriefoverviewofhowSODAsatisfiestheserequirements:
• SODAleveragesSOCOtobalancethetrade-off betweenvideoqual-
ity,sustainedplaybackwithoutrebuffers,andbitratesmoothness
withoutfrequentswitches.Importantly,SODAfocusesonsteer-
ingthebufferleveltowardsatargetratherthanweighingvideo
Figure4:Asamplethroughputfunctionusedtoillustrate
qualityagainstrebufferingduration(seeSection3.1).
whyourtime-basedformulationisbetterforanalysis.
• Toachieverobustnessagainstthroughputvariability,SODAisde-
signedtosatisfytheexponentiallydecayingperturbationproperty,
whichguaranteesthatSODAneveroperatestoofarawayfromthe • 𝑏(𝑥 𝑛)isthebuffercost,whichaimstostabilizethebufferlevel
optimaltrajectoryinthefaceofpredictionerrors(seeSection4.2). aroundatargetlevel𝑥¯,i.e.,
• T a
fo
p o
r
p r
i
r e
m
o m x
p
a i
l
m
e
in
m
a c t
e
e o
n
m
t
s
a
o p
t
l
i
u v
o
t e
n
a r
)
t
,
i ( o s
th
e n e
a
a
t
l S l
o
y e
n
c e
l
t ffi
y
io
r
c n
e
ie
q
A n
u
t .
i
5 ,
r
S
e
f
s
o O r D
e
A
v
p
a
r l
l
e o
u
v o
a
e f
t
r
i
a
o
a n g
n
d e
o
s A
f
a
m
l n g
o
o e
n
r ffi i
o
th c
to
i m e
n
n
i
1
c
t 𝑏(𝑥 𝑛)= (cid:40)
𝜖
(𝑥
(
¯
𝑥
−
𝑛
𝑥
−
𝑛
𝑥
)
¯
2
)2 𝑥
𝑥
𝑛
𝑛
>
≤
𝑥
𝑥
¯
¯ ,
bitratesequences(Section4.3),whichreducesthecomputational where𝜖 <1isasmallconstant.Notethatwepurposelydonot
costbytwoordersofmagnitudeoverabrute-forcesolver. modeltherebufferingtimeexplicitlytoavoidthepitfallsencoun-
teredbyRobustMPC(Section2)andasweshowlater,thishelps
3 SODAOVERVIEW SODAachievetheoreticalperformanceguarantees(Section4.2).
Giventhedesigngaps,opportunities,andrequirements,wesetout • 𝑐(𝑟 𝑛 ,𝑟 𝑛−1)istheswitchingcostfromthepreviousbitratetothe
todesignatheoreticallysound adaptivebitratestreaming(ABR) currentbitrate,e.g.,𝑐(𝑟
𝑛
,𝑟 𝑛−1)=(𝑣(𝑟 𝑛)−𝑣(𝑟 𝑛−1))2.
controllerthatminimizesbitrateswitchingwithoutcompromis- Coefficients 𝛽 and𝛾 arepositiveweightsforthebufferandthe
ingvideoqualityorincreasingrebufferingtime,thusprovidinga switchingcostrespectivelybasedonuserpreferences.Thechoices
smoothviewingexperience.Toaccomplishthis,wedeviatefrom forthedistortionandswitchingcostfunctionsareflexible.
theconventionalsegment-basedABRformulationandderivetheo- Thetime-based bufferdynamicsareintroducedintotheopti-
reticalinsightsfromatime-basedABRformulation.Thisenablesus mizationproblemthroughthefollowingconstraint:
toincorporatethroughputpredictionsintothecontrollerinaprin-
𝜔 Δ𝑡
cipledway.Takingadvantageofrecentadvancementsinsmoothed 𝑥 𝑛 =𝑥 𝑛−1+
𝑟
𝑛 −Δ𝑡 ∈ [0,𝑥max],
onlineconvexoptimization(SOCO),wecantheoreticallyprove 𝑛
thatSODAoffersanear-optimalqualityofexperience(QoE)andis
where𝜔
𝑛
Δ𝑡/𝑟
𝑛
accountsforthevariableamountofvideodown-
loadedduringatimeintervalandΔ𝑡accountsforthefixedamount
robustagainstthroughputpredictionerrors.
ofbufferdrainedduringthesametimeinterval.Notethatwedonot
allowthecontrollertoviolatethebufferrangeconstraintduring
3.1 ATime-BasedABRFormulation
theoptimizationphasewhendeterminingthebitrate.Ofcourse,due
Ourtime-basedABRformulationtreatsavideostreamasacontin-
tothroughputpredictionerrors,thismaysometimesbeinevitable
uousflowratherthanadiscretesequenceofsegments.Considera
duringtheexecutionphasewhenapplyingthebitratedecision.
streamingsessionthatconsistsof𝑁 timeintervalswithfixeddura-
tionΔ𝑡intermsofclocktime(notvideotime).Thecontroller’stask WhyaTime-BasedFormulation? Thetime-basedformulation
istoselectabitrateforeachtimeintervalfromasetofavailable allowsacleanertheoreticalanalysisoveragiventhroughputse-
bitratesR ⊂ [𝑟 min ,𝑟max] tooptimizeforacombinationofhigh quence(𝜔1,...,𝜔 𝑁 ).Forexample,considerthethroughputfunction
quality,shortrebuffering,andinfrequentbitrateswitching. showninFigure4.Inthetime-basedformulation,wenaturallyhave
Let𝜔
𝑛
denotetheaveragethroughputduringthe𝑛thtimeinter- 𝜔1=4,𝜔2=1,and𝜔3=𝜔4=2Mb/sgivenΔ𝑡 =1s.Bycontrast,
val,𝑟 theselectedbitrateforthattimeinterval,and𝑥 thebuffer inthesegment-basedformulation,thethroughputsequencebe-
𝑛 𝑛
levelimmediatelyafterthattimeinterval.Ourobjectiveistomin- comesdependentonthebitratesequence.Assumingthesegment
imizetheoverallcostgivenasalinearcombinationofthethree durationisalso𝐿=1s,ifthecontrollerchooses𝑟1 =2Mb/sand
QoEcomponents: 𝑟2=2.5Mb/s,thenittakes0.5and1stodownloadthefirstandsec-
𝑛
∑︁ 𝑁
=1
(cid:18) 𝑣(𝑟 𝑛)· 𝜔
𝑟
𝑛
𝑛
Δ𝑡 +𝛽·𝑏(𝑥 𝑛)+𝛾·𝑐(𝑟 𝑛 ,𝑟 𝑛−1) (cid:19) , (1) A o
to
n s d
b
s
i
u s
t
e c
r
g
a
h
t
m ,
e
t e h
s
n e
e
t
l
s s
e
e
c
r g
t
e
i
m s
o
p
n
e e n c
𝑟
t t
1
i b
,
v
.
a e
..
s l
,
y e
𝑟
, d
𝑁
re f
,
o s
w
r u m l
h
t
i
i u
c
n l
h
g at i
i
i n
n
on 𝜔
tu
g 1
r
e
n
= ts 4
m
c a a
a
n u
k
d s
e
a
s
𝜔 ll
i
2 y
t
= b
d
i
i
2 a
ffi
s .5
c
e
u
d M
l
d
t
b u /
to
s e .
theoreticallyanalyzethedesign[61].
where
• 𝑣(𝑟 𝑛)isthedistortioncost,whichshouldbeapositive,strictly WhyNotModelRebufferingDirectly? Rebufferingisimportantto
decreasing,andconvexfunctionthatmodelstheencodingdistor- minimizefromauser’sperspective[7,9].However,inouroptimiza-
tion,e.g.,𝑣(𝑟 𝑛)=1/𝑟
𝑛
.Itisthenweightedbytheamountofvideo tionproblemformulation,wedidnotexplicitlymodelrebuffering
downloadedduringthattimeinterval,i.e.,𝜔
𝑛
Δ𝑡/𝑟
𝑛
becausethe likepriorworks[17,46,50].Instead,wefocusonstabilizingthe
controllerdownloadsavariable amountofvideoduringeach bufferlevelaroundatargetlevelwithasmoothroll-offonboth
fixedtimeinterval. sidesforthefollowingreasons:
616

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
• Minimizingrebufferingdirectlyisnottheoreticallytractablebe-
causeitrequiresabinarypenaltyfunctionthatyieldsanon-zero
penaltyexactlywhenthebufferisempty.Instead,weemploy
asmootherpenaltyfunctionthatincreasesinmagnitudewhen
thebufferlevelfallsbelowadesiredtargetlevel.Whenthere
isanetworkissue,westarttopenalizeearlywhenthebuffer
leveldecreasesbelowthesafetargetlevelandweprovidethe
largestpenaltywhenthebufferlevelisempty.Usingasmooth
penaltyfunctionenablesustoguaranteethatSODA’soptimiza-
tionisstronglyconvex,whichiskeytoourtheoreticalwork.Our
approachisanalogoustotheuseofcontrolbarrierfunctionsto
ensuresafetypropertiesincontrolsystems[30].
• Modelingrebufferingtimedirectlymakesthecontrollervulnera-
bletothroughputpredictionerrors.Underadirectrebuffering
objective,aslongasthebufferlevelisabovezero,therewillbeno
penaltyforthecontroller,evenifthebufferlevelisdangerously
closeto0.Asaresult,evensmallthroughputpredictionerrors
canleadtounexpectedrebuffering.
3.2 IncorporatingThroughputPredictions Figure5:SODA’sbitratedecisionasafunctionofbufferlevel
Inadditiontofacilitatingtheoreticalanalysis,ourtime-basedformu- andpredictedthroughput.Darkbluetolightorangerepre-
lationiscrucialtoensuringthevalidityofthroughputpredictions sentlowtohighbitratedecisions.NoticethatSODAbecomes
overthepredictionhorizon.Animportantobservationisthatbi- more aggressive in selecting higher bitrates as the buffer
tratedecisionshavenocausalimpactonhowlongthethroughput grows.TherightmostregionisblanksinceSODAmakesno
predictionsarevalidfor.However,segment-basedcontrollerssuch downloadstopreventabufferoverflow.
asMPC[17]andFugu[46]intertwinethroughputpredictionsandbi-
tratedecisionsinnon-causalways.Inthesedesigns,thethroughput
𝜔ˆ Δ𝑡
predictionhorizonspansshorterperiodsofclocktimewhenlow subjectto 𝑥 𝑚 =𝑥 𝑚−1+
𝑚|
𝑟
𝑛−1
−Δ𝑡, (2b)
bitrateisselectedcomparedtowhenhighbitrateisselected.Infact, 𝑚
theirunderlyingassumptionaboutthevalidityofthethroughput 𝑥 𝑚 ∈ [0,𝑥max], 𝑟 𝑚 ∈R, (2c)
predictionhorizoncanvaryby𝑟max/𝑟
min
. withrespecttovariables𝑟
𝑛
,...,𝑟
𝑛+𝐾−1
andthencommittingto
Bycontrast,thewayweincorporatethroughputpredictionsinto onlythefirstbitratedecision𝑟
𝑛
.ThebehaviorofSODAisvisualized
SODAdoesnotsufferfromthisissue.Specifically,justbeforeeach asabitratedecisiondiagraminFigure5toprovidereaderswith
timeinterval,thecontrollerisgivenaccesstoa(notnecessarily intuitionabouthowSODAselectsbitratesinpractice.
accurate)throughputpredictionforthenext𝐾 timeintervalsfrom AsdiscussedinSection2,solvingthisoptimizationproblemis
ablack-boxthroughputpredictor.Itisalwaysassumedthatthe computationallyexpensive,furthermore,itisunclearwhatpredic-
validityofthethroughputpredictionis𝐾Δ𝑡,afixedvalue.Ingen- tionhorizonshouldbeusedandhowaccuratethroughputpredic-
eral,athroughputpredictormayoutputadifferentvalueforeach tionsmustbeinorderforSODAtoperformwell.Wefirstanalyze
ofthenext𝐾timeintervals,i.e.,𝜔ˆ ,𝜔ˆ ,...,𝜔ˆ , thesequestionstheoretically(Section4)andthenpresentapractical
𝑛|𝑛−1 𝑛+1|𝑛−1 𝑛+𝐾−1|𝑛−1
where𝜔ˆ 𝑚|𝑛−1 (𝑚 ≥ 𝑛)isthethroughputpredictionforthe𝑚th implementationof SODAthatanswerstheseconcerns(Section5).
timeintervalgivenpreviousdownloadinformationupuntilthe
(𝑛−1)thtimeinterval.Inotherwords,athroughputpredictorcan 4 THEORETICALDESIGNINSIGHTS
outputapiecewiseconstantthroughputfunctionforthenext𝐾Δ𝑡 OurdesignofSODAismotivatedbyrecenttheoreticaladvancesat
time.Inpractice,though,atypicalthroughputpredictoroutputsa theinterfaceoflearningandcontrol[28,38,49,54]andsmoothed
singlevaluethatcorrespondstoaconstantthroughputfunction. onlineconvexoptimization[25,33,55].Inparticular,wedesign
SODAtosatisfyanexponentiallydecayingperturbationpropertythat
hasbeenshowntoensureefficientandrobustuseofpredictionsin
3.3 ControlMechanism
modelpredictivecontrolpolicies[49,56].Intuitively,thisproperty
Inspiredbythemodelpredictivecontrolframework,SODAselectsa describesthebehaviorofthesolutiontotheoptimizationproblem
bitrateforeachtimeintervalbyoptimizingoverthenext𝐾 time definingSODA(Equation2)asafunctionofproblemparameters,
intervalsandthencommittingtothebitratedecisionfortheimme- includingbandwidthpredictions{𝜔ˆ 𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾 andtheprevi-
diatenexttimeinterval,i.e.,minimizing ousbufferlevel/actionpair(𝑥 𝑛−1,𝑢 𝑛−1).Here,wedefinetheactions
astheinverseofthebitrates(i.e.,𝑢
𝜏
=1/𝑟
𝜏
foralltimestep𝜏)and
𝑛+𝐾−1(cid:18) 𝜔ˆ Δ𝑡 (cid:19) doachangeofthevariablestomakethedynamicslinearforthe
∑︁
𝑣(𝑟 𝑚)·
𝑚|
𝑟
𝑛−1
+𝛽·𝑏(𝑥 𝑚)+𝛾·𝑐(𝑟 𝑚 ,𝑟 𝑚−1) (2a) theoreticalanalysis.Underthisproperty,when{𝜔ˆ 𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾
𝑚=𝑛 𝑚 arefixed,theoptimaltrajectoryof(Equation2)undertheinitial
617

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
(𝑥 ′ ,𝑢 ′ ) analysis,butwefindSODAempiricallyperformsverywelleven
𝑛 −1 𝑛 −1
|     | (𝑥 ′,𝑢 ′) |         |     |     |     | whenthisassumptionisnotstrictlysatisfied. |             |        |         |                 |
| --- | --------- | ------- | --- | --- | --- | ----------------------------------------- | ----------- | ------ | ------- | --------------- |
|     | 𝑛 𝑛       | (𝑥′ ,𝑢′ | )   |     |     |                                           |             |        |         |                 |
|     |           | 𝑛+1 𝑛+1 |     |     |     | In this                                   | section, we | set Δ𝑡 | 1, [𝑟   | ,𝑟max], and𝑣(𝑟) |
|     |           |         |     |     |     |                                           |             | =      | R = min | =               |
1/𝑟.Ourresultscanapplytootherdistortioncostfunctions,e.g.,
(𝑥 𝑛−1,𝑢 𝑛−1) (𝑥 𝑛 ,𝑢 𝑛) (𝑥 𝑛+1,𝑢 𝑛+1) 𝑣(𝑟) =log(𝑟max/𝑟),aslongascertainregularityconditionshold;
seeAppendixBforadiscussion.
4.1 ExactPredictions
Figure6:Illustrationoftheexponentiallydecayingperturba-
tionproperty:When{𝜔ˆ 𝑚|𝑛−1}𝑛≤𝑚<𝑛+𝐾 arefixed,theoptimal Whenthebandwidthpredictionsareaccurate,asmallprediction
horizonissufficientforSODAtoachievenear-optimalperformance.
trajectoriesofEquation2underdifferentinitialbuffer/action
Inpractice,itisdesirabletousearelativelysmallpredictionhori-
pairsconvergeexponentiallytowardeachother.
zonforapredictivecontrollerlikeSODAbecausepredictionerrors
growdramaticallyaswepredictfurtherintothefuture.Fortunately,
theexponentialdecaypropertythatensuresgoodperformance
buffer/actionpair(𝑥 ′ ,𝑢 ′ )convergesexponentiallytowardthe withonlyafewpredictions.Moreformally,wepresentatheorem
𝑛 −1 𝑛 −1
optimal trajectory under the pair (𝑥 𝑛−1,𝑢 𝑛−1) (see Figure 6 for showingthatasmallpredictionhorizonissufficientforSODAto
anillustration).Ontheotherhand,whentheinitialbuffer/action achievenear-optimalperformancewhenthepredictionswithinthis
| pairisfixed,theimpactofperturbingaprediction𝜔ˆ |                                               |     |     |       | onthe |                           |     |         |                      |     |
| ---------------------------------------------- | --------------------------------------------- | --- | --- | ----- | ----- | ------------------------- | --- | ------- | -------------------- | --- |
|                                                |                                               |     |     | 𝑚|𝑛−1 |       | windowareaccurate(i.e.,𝜔ˆ |     | 𝑚|𝑛−1=𝜔 | 𝑚 for𝑚=𝑛,...,𝑛+𝐾−1). |     |
| firstaction𝑢                                   | decaysexponentiallywithrespecttotheirtemporal |     |     |       |       |                           |     |         |                      |     |
𝑛
|     |     |     |     |     |     | Theorem4.1. | [Informal]Whenthepredictionsofthebandwidthin |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------------------------------------------- | --- | --- | --- |
distance(𝑚−𝑛).Theformaldefinitionofexponentiallydecaying
|     |     |     |     |     |     | future𝐾 stepsareexact(i.e.,𝜔ˆ |     | 𝑚|𝑛−1=𝜔 | 𝑚for𝑚=𝑛,...,𝑛+𝐾−1) |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | ------- | ------------------ | --- |
perturbationgeneralizestheintuitionabovetoconsidertheimpact
|                                                           |     |     |     |     |     | andthepredictionhorizon𝐾 |     |     | 𝑂(1),SODAachievesadynamic |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------- | --- |
| ofperturbinganyparametersontheentireoptimaltrajectory(see |     |     |     |     |     |                          |     | ≥   |                           |     |
regretof𝑂(𝜌𝐾𝑁)andacompetitiveratioof1+𝑂(𝜌𝐾),where𝜌
| DefinitionA.1inAppendixA). |     |     |     |     |     |     |     |     |     | <1  |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TwometricsthatweusetomeasureSODA’sperformancetheoret- isthedecayfactoroftheexponentiallydecayingperturbationproperty.
icallyaredynamicregretandcompetitiveratio,whicharestandard TheformalstatementofTheorem4.1isgiveninTheoremA.3
intheliteratureofonlineoptimization[25,28,33,49,54].Specif- inAppendixA.ThisresultimpliesthatSODA’sperformanceap-
| ically, let cost(ALG) | denote | the total | cost incurred | by  | an online |     |     |     |     |     |
| --------------------- | ------ | --------- | ------------- | --- | --------- | --- | --- | --- | --- | --- |
proachesthatoftheoptimalsequenceofdecisionsexponentially
algorithmALGandcost(OPT)denotetheofflineoptimalcost(Equa-
fastinthepredictionhorizonsize𝐾;thus,onlyasmallprediction
tion1)anagentcanincurifithasexactknowledgeofallfuture
horizonlengthisnecessarytoobtaingoodperformance.
bandwidthatthebeginning.WesayALGachievesadynamicregret
of𝑅ifcost(ALG)−cost(OPT) ≤𝑅alwaysholds,andALGachievesa 4.2 InexactPredictions
| competitiveratioof𝐶ifcost(ALG) |     |     | ≤𝐶·cost(OPT)alwaysholds. |     |     |              |           |            |            |                 |
| ------------------------------ | --- | --- | ------------------------ | --- | --- | ------------ | --------- | ---------- | ---------- | --------------- |
|                                |     |     |                          |     |     | We now relax | the exact | prediction | assumption | to prove SODA’s |
Thekeyideaunderlyingourtheoreticalanalysisistoleveragethe
robustnesstoacertainlevelofpredictionerrorsthankstoitsexpo-
exponentialdecaypropertytobound(i)theerrorthatSODAincurs
nentiallydecayingperturbationproperty.
ateveryintermediatetimestep𝑛duetoitslimitedpredictionpower
(𝜔ˆ 𝑚|𝑛−1≠𝜔 𝑚 ,𝐾 ≪𝑁),and(ii)theaggregationofsucherrorsover Theorem 4.2. [Informal] Suppose the prediction error at each
thewholehorizon𝑁.Specifically,wedefinethenotionofper-step stepisboundedabove.Thebufferlevelof SODAwillneverhitthe
erroratatimestep𝑛asthedistancebetweenSODA’sbuffer/action constraintboundary,i.e.,0<𝑥 <𝑥 max.Further,defineE =𝜌2𝐾𝑁+
𝑛
pairandtheoptimalbuffer/actionpairthatonecouldreachwith (cid:205) 𝐾 𝜌𝜅𝐸 𝜅,where𝐸 dicting𝜅steps
|                                        |     |     |                                 |              |       | 𝜅 =1                                         | 𝜅 isthetotalsquarederrorforpre |     |     |         |
| -------------------------------------- | --- | --- | ------------------------------- | ------------ | ----- | -------------------------------------------- | ------------------------------ | --- | --- | ------- |
| exactpredictionsofallfuturebandwidths𝜔 |     |     |                                 | ,𝜔 𝑛+1,...,𝜔 | given |                                              |                                |     |     | √       |
|                                        |     |     | 𝑛                               |              | 𝑁     | intothefuture.SODAachievesadynamicregretof𝑂( |                                |     |     | E𝑁 +E). |
| thepreviousbuffer/actionpair(𝑥         |     |     | 𝑛−1,𝑢 𝑛−1)(DefinitionA.2).Using |              |       |                                              |                                |     |     |         |
TheformalstatementofTheorem4.2isgiveninTheoremA.8in
theprincipleofoptimality,wereformulatetheoptimalbuffer/action
pairasanentryoftheoptimaltrajectoryfromtime𝑛to(𝑛+𝐾−1) AppendixA.Theorem4.2showsthat,ifthebuffercostsare“steep”
sothatwecandirectlycompareitwithSODA’sbuffer/actionpair andthepredictionerrorsonthebandwidtharerelativelysmall,
undertheexponentiallydecayingperturbation.Thus,weestablisha SODAcanachieveasequenceofbufferlevelsthatstaysafelyaway
|     |     |     |     |     |     | fromtheboundariesofbufferconstraint |     |     | [0,𝑥max].Thedynamic |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | ------------------- | --- |
boundontheper-steperrorthatdependsontheerrorsofpredicting
regretofSODAdependsonthemagnitudeofthepredictionerrors
| futurebandwidthsandthepredictionhorizon𝐾 |     |     |     | (LemmaA.4).On |     |                |          |      |                   |          |
| ---------------------------------------- | --- | --- | --- | ------------- | --- | -------------- | -------- | ---- | ----------------- | -------- |
|                                          |     |     |     |               |     | and the regret | improves | when | the errors become | smaller. |
the other hand, we also show that the aggregation of per-step SODA
errorsdoesnotgrowlinearlyintimebecausetheexponentially acquires this guarantee thanks to its maintenance of the buffer
decayingperturbationguaranteesthattheimpactofeachprevious nearatargetlevel𝑥¯.Incontrast,RobustMPC[17]doesn’tofferthe
sameperformanceguarantee,thusevensmallbandwidthprediction
per-steperrorvanishesexponentiallyovertime(LemmaA.5).We
errorscancausethevideotorebufferifthebufferlevelisnearzero.
| present a proof | outline | and the | detailed proofs | in Appendix | A.  |     |     |     |     |     |
| --------------- | ------- | ------- | --------------- | ----------- | --- | --- | --- | --- | --- | --- |
Toprovetheexponentiallydecayingperturbation,werequirea
technicalassumptionthatguaranteesthecontrollercan“reach” 4.3 ComputationalEfficiency
anydesiredbufferlevelbychoosingthelargest/smallestbitrate Solvingthepredictiveoptimizationproblemtodeterminetheexact
(seeAssumptionA.1inAppendixAfortheformalstatement).This optimalsolutioncanbeunrealisticintheapplicationofadaptive
assumptionisusedtoeliminateextremeboundarycasesinthe bitratestreaming,whereeachdecisionneedstobemadeinthe
618

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
minimumpossibletime.Acriticalobservationunderlyingtheim-
plementationofSODAisthatitissufficienttosearchonlyforbitrate
sequences that are increasing or decreasing monotonically. We
provideatheoreticaljustificationinthefollowingtheorem.
Theorem4.3. [Informal]SupposeSODAisgiventhepredictions
thatsatisfy𝜔ˆ 𝑛|𝑛−1=···=𝜔ˆ 𝑛+𝐾−1|𝑛−1atanintermediatetimestep
𝑛.Then,thebitratetrajectorysolvedbySODAcanbeapproximated
byafeasiblemonotonicbitratetrajectorywithanerrorof𝑂(cid:0)𝐾/√
𝛾
(cid:1)
.
TheformalstatementofTheorem4.3isgiveninTheoremA.9
inAppendixA.Theorem4.3showsthatthetrueoptimalsolution Figure7:Weprofiledtheperformanceofthetwothroughput
becomesclosertomonotonicastheweight𝛾 ofswitchingcosts predictorsshippedwithdash.js[64],i.e.,movingaverage
increases.Whilethetheoreticalboundcanbeconservative,wefind predictorandexponentialmovingaveragepredictor.Both
thatevenwithmoderate𝛾,the(discrete)decisionmadeunderthe predictorshaveahighmeancorrelation(around50%)inthe
monotonicheuristicisusuallyidenticaltothetrueoptimalsolution immediatefuturebutaverylowmeancorrelation(around
onarealtrajectory(seeFigure8). 15%)inthefarfuture.
5 IMPLEMENTATIONDETAILS
Giventhetheoreticaldesigninsights,wenowdiscussthepractical Algorithm1:SODA’sefficientapproximateoptimization
implementation of the high-level design described in Section 3. solver.SearchDownisomittedforbrevityduetosymmetry.
Therearethreepracticalconcernsthatrequirediscussion:(i)how Thecurrentbufferlevelandthepreviousbitratearedenoted
totranslatethetime-baseddesigntothesegment-basedschema; by𝑥0 and𝑟0 respectively.
(ii)howtoincorporatethroughputpredictionsrobustly;and(iii)
howtosolvethepredictiveoptimizationproblemefficiently.
functionSearch(𝜔ˆ,𝑥0,𝑟0,𝐾)
(𝑟
u
∗
p
,obj∗ up)←SearchUp(𝜔ˆ,𝑥0,𝑟0,𝐾)
5.1 Segment-BasedSchema
(𝑟
d
∗
own
,obj∗
down
)←SearchDown(𝜔ˆ,𝑥0,𝑟0,𝐾)
return𝑟∗ ≠null∧obj∗ <obj∗ ?𝑟∗ :𝑟∗
SODAisintrinsicallyatime-basedcontroller,butinpractice,avideo up up down up down
mustbedownloadedsegmentbysegmentaccordingtotheMPEG-
functionSearchUp(𝜔ˆ,𝑥0,𝑟0,𝐾)
DASHstandard.Toreconcilewiththisrequirement,wekeepthe
𝑟
1
∗←null,obj∗←∞
optimizationphaseasisinthetime-basedformatandempirically foreach𝑟1 ∈{𝑟 ∈R :𝑟 >𝑟0}
setΔ𝑡 tobeequaltothesegmentlength.Thischoiceisjustified 𝑥1←𝑥0+𝜔ˆΔ𝑡/𝑟1−Δ𝑡
bythefactthatinthesteadystate,thedownloadtimeofavideo if𝑥1 <0thencontinue
segmentisexpectedtobeclosetothesegmentlengthormuchless obj←𝑣(𝑟1)·𝜔ˆΔ𝑡/𝑟1+𝛽·𝑏(𝑥1)+𝛾·𝑐(𝑟1,𝑟0)
thanthat[29].Tofurtherminimizethelikelihoodofcommitting if𝐾 >1then
toabitrateforsignificantlylongerthanΔ𝑡,weintroduceanother (𝑟
2
∗,Δobj∗)←SearchUp(𝜔ˆ,𝑥1,𝑟1,𝐾−1)
heuristicthatthecontrollermustselectabitratenohigherthan if𝑟
2
∗=nullthencontinue
min{𝑟 ∈R :𝑟 ≥𝜔ˆ}. obj←obj+Δobj∗
ifobj<obj∗then𝑟
1
∗←𝑟1,obj∗←obj
5.2 IncorporatingPredictionsRobustly return(𝑟
1
∗,obj∗)
AccordingtoSection4.2,SODAisrobustagainstpredictionerrors
bydesignaslongasthereisnosystematicbiasinpredictioner-
rors.Giventhediversenetworkconditionsinthewild,weprefer
simplethroughputpredictorswhichmakesSODAhighlydeployable caseinFastMPC[17],however,thisisneitherflexiblenorscalable
sincethereisnodependenceoncomplexthroughputpredictors. inpractice.Alookuptableisspecifictoaparticularsetofbitrates,
Inpractice,weobservethatpredictionaccuracydegradesasthe maximumplayerbuffer,segmentdurationsandbytesizesetc.thus
predictionhorizonincreases(seeFigure7).Therefore,welimitthe needstoberecomputedwhenanyofthesequantitieschange.Fur-
predictionhorizonlengthtoatmost10s.Thisisalsosupportedby thermore,computingthislookupinlivestreamingisundesirable
ourfindinginSection4.1thatalongerpredictionhorizonyields duetotheadditionalcomputationalandlatencyoverheaditincurs.
diminishingreturns. Instead,weoptforanefficientapproximatesolver.
SODA’sapproximatesolverisdesignedtotakeadvantageofthe
5.3 EfficientApproximateSolver structureoftheoptimalsolutionpresentedinSection4.3.Insteadof
AtSODA’scoreisthepredictiveoptimizationproblemdescribed searchingthroughallpossiblebitratesequencesintheprediction
inSection3.3.Unfortunately,solvingthisproblemontheflyis horizon,theapproximatesolveronlyconsidersmonotonicbitrate
computationallychallenging.Onemayproposeenumeratingall sequences,i.e.,itimposesanadditionalconstraintthat𝑟 𝑛−1 ≤𝑟 𝑛 ≤
combinationsofdiscretizedthroughputs,bufferlevels,andprevious ... ≤𝑟 𝑛+𝐾−1 or𝑟 𝑛−1 ≥𝑟 𝑛 ≥ ... ≥𝑟 𝑛+𝐾−1 .Thepseudocodefora
bitratesintheformofanofflinecomputedlookuptable,asisthe recursiveimplementationisshowninAlgorithm1.
619

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
• MeanUtility:Unlessotherwisenoted,weusethecommonly-
usedlogarithmicutilityfunction:
𝑁
𝑣¯=
1 ∑︁ log(𝑟 𝑖/𝑟 min)
.
𝑁
𝑖=1
log(𝑟max/𝑟 min)
• RebufferingRatio:Theratioofthetotalrebufferingtimetothe
sessionduration,i.e.,𝜌 rebuf=𝑇 rebuf/𝑇.
• SwitchingRate:Bitrateswitchcountdividedbysegmentcount
minusone,i.e.,𝑝 switch=𝑁 switch/(𝑁 −1).
TheQoEscoreissimplyalinearcombinationofthethreeQoE
Figure8:Theprobabilitythatthebitratedecisionproduced
bytheapproximatesolverisdifferentfromthatproduced components,i.e.,QoE = 𝑣¯−𝛽 ·𝜌 rebuf−𝛾 ·𝑝 switch .Inthiswork,
we chose 𝛽 = 10 and𝛾 = 1 to reflect the high importance of
bythebrute-forcesolverquicklyconvergesto0asswitching
minimizing rebuffering time. To establish fair comparisons, we
costweightincreases.
reporttheindividualQoEcomponentsalongwiththeQoEscore.
6.1 NumericalSimulations
TheapproximatesolverreducesthetimecomplexityfromO(|R|𝐾)
Toperformlarge-scalenumericalsimulations,weimplementeda
(exponentialin𝐾)inthecaseofabrute-forcesearchoverallpossi- highlyoptimizedABRsimulatorinC++derivedfromSabre[36].
blebitratesequencesinthepredictionhorizondowntoO (cid:16) (cid:0)|R|+𝐾(cid:1) (cid:17) ThesimulationaccuracyofSabrehasbeenempiricallyvalidated
𝐾
(polynomialin𝐾)andhasaspacecomplexityofO(𝐾)only.The againstdash.js[64],thereferenceplayerforMPEG-DASH.We
timecomplexitycanbefurtherreducedbylimitingextremebitrate configuredthesimulatortoallowamaximumbufferlengthof20
switches.Inpractice,SODAsearchesthroughatmostaround200 secondstoreplicatethetypicallivestreamingconditions.
bitratesequences.Accordingtoourproductiondeploymentexpe-
6.1.1 ExperimentalSetup. Ournetworkdatasetconsistsofabout
rience,theapproximatesolverdidnotimposearuntimeburden
38,000hoursofthroughputtracescompiledfromthefollowing
evenonlow-enddevicessuchasset-topboxes,whichshowsthat
threepublicsources:
SODAishighlypractical.
Empirical results are shown in Figure 8 to validate the near- • PufferDataset[46]:Wedownloadedandparsedallthroughput
tracesfromthePufferplatformduringthetimeperiodofJanuary
optimalityofbitratedecisionsproducedbytheapproximatesolver.
2023toJune2023.
Foreachalgorithmconfiguration,weuniformlysampleamillion
situationswithdifferentthroughputs,bufferlevels,andprevious • 5GDataset[41]:A5GnetworkdatasetfromamajorIrishmobile
operatorunderbothstaticandmovingscenarioswhiledown-
bitrates.Then,wecounttheprobabilitythatthebitratedecision
loadingonlinecontent.
producedbytheapproximatesolverisdifferentfromthatproduced
bythebrute-forcesolver.Thedifferenceisnegligibleforareason- • 4GDataset[27]:A4GnetworkdatasetfromtwomajorIrish
mobileoperatorsunderbothstaticandmovingscenarioswhile
ableswitchingcostweight,e.g.,below5%for𝐾 =4andarelative
downloadingonlinecontent.
switchingcostweightof2.Throughouttheevaluationsections,we
usethisefficientimplementationof SODA. Forallthreedatasets,wefilteredoutsessionsshorterthan10min-
utesanddividedlongsessionsintoconsecutive10-minutesessions,
resultingin230,322sessionsfromthePufferdataset,88sessions
6 EVALUATION
fromthe5Gdataset,and187sessionsfromthe4Gdataset.Fig-
TothoroughlyevaluateSODA’sperformance,weconductedthree
ure9illustratesthewiderangeofnetworkconditionscoveredby
levelsofempiricalevaluation:(i)large-scalenumericalsimulations,
thesedatasets.Ingeneral,thePufferdatasetrepresentsbetternet-
(ii)prototypeevaluationinPuffer[46],and(iii)productiondeploy-
workconditionsthanthe5Gand4Gdatasets.Thelatterhavemuch
mentinAmazonPrimeVideo.Thisfunnelapproachallowedusto
lowermeanthroughputandhighervariance,thusposingabigger
firstsystematicallyevaluateSODAagainstavarietyofbaselinesin
challengeforABRcontrollers.
awiderangeofcontrolledenvironments.Later,wenarrowedthe
Tofullyexerciseourdatasets,weconsideredahigh-frame-rate
comparisontargettoadeployedandfine-tunedABRcontrollerin
4KvideoencodedaccordingtotheYouTuberecommendedsettings
productionusingA/Btestsonrealusersessions.
(1.5,4,7.5,12,24,and60Mb/s)[65]withasegmentlengthof2
seconds.Forthe5Gand4Gdatasets,weconsideredthesamevideo
PerformanceMetrics. Tomaintainconsistencyintermsofperfor- with the two highest bitrates removed. Finally, for throughput
mancemetricswithpriorworkssuchas[17,22,24,46],asimilar
prediction, we opted for the exponential moving average (EMA)
definitionofQoEisadoptedthatconsistsofmeanutility,rebuffer-
predictor,thedefaultthroughputpredictorindash.js.
ingratio,andswitchingrate.Thesecorrespondtothethreemain
desiredpropertiesofadaptivebitratestreaming,i.e.,highvideo 6.1.2 BaselineABRControllers. WecomparedSODAagainstthe
quality,shorterrebufferingtime,andlessbitrateswitching.All followingABRcontrollersrepresentativeofeachofthecommon
threeQoEcomponentsarenormalizedbetween0and1foreaseof ABRcontrollercategories,i.e.,throughput-based,buffer-based,and
interpretation.Theprecisedefinitionsareasfollows: hybrid.Theyweretunedtoourbesteffortsforournetworkdatasets.
620

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
Figure9:ThemeanthroughputofthePuffer,5G,and4Gdatasetsare57.1,31.3,and13.0Mb/s.Themeanrelativestandard
deviationsofthroughputofthePuffer,5G,and4Gdatasetare47.2%,133%,and80.6%.
• HYB[24]:Aheuristicthroughput-basedABRcontrollerthatse- ABRcontroller.WhereSODAreallyshinesthoughisitssignifi-
lectsthehighestbitratewithoutrebuffering. cantlylowermeanswitchingrates.DespiteDynamic’sswitch-
• BOLA[36]:Abuffer-basedABRcontrollerderivedfromLyapunov ingavoidanceheuristic,SODAcutsdownmeanswitchingrates
optimization.Itprovidestheoreticalguaranteesaboututilityand by as much as 70.4%, which demonstrates the superiority of
rebufferingtimeonly. theoretically-sounddesign.
• Dynamic[44]:Aproductionversionof BOLAthatdynamically • SODAvsMPC.MPChashighmeanutilitiesandlowmeanswitching
switchesbetweenbuffermodeandthroughputmodeinresponse ratesunderstablenetworkconditions(seePuffer(Q1variance)
tochangesinnetworkconditions.Additionally,ithaslow-buffer inFigure10).However,theperformanceofMPCistightlycoupled
safetyheuristictoreducerebufferingandaswitchingavoidance withtheintrinsicvolatilityofnetworkconditions.Specifically,
heuristictomitigatebitrateswitching.ItisthedefaultABRcon- MPCsuffersalotintermsofmeanrebufferingratiosespecially
trollerindash.js. undermobilenetworkconditions.Bycontrast,SODAdoesnot
• MPC[17]:Oneapplicationofmodelpredictivecontroltoadap- have this issue since it is robust against prediction errors by
tivestreamingthatmodelsutility,rebufferingtime,andbitrate design,makingitmuchmoresuitableforproductiondeployment.
switching,withouttheoreticalguarantees.
6.1.4 IntrinsicSensitivitytoPredictionAccuracy. Inanefforttoim-
provethroughputpredictionaccuracy,severalpriorworkshavefo-
6.1.3 QoEPerformance. TheaggregatestatisticsforQoEscores cusedondesigningmoresophisticatedthroughputpredictorssuch
andindividualQoEcomponentsundereachnetworkdatasetare asC2SP[20],Fugu[46],andXatu[50].Whilethesethroughputpre-
showninFigure10.Tobetterunderstandhowtheperformanceof dictorsmayofferhigherpredictionaccuracy,theyarecomplexand
differentABRcontrollersreacttotheintrinsicvolatilityofnetwork difficulttodeploy,especiallyoncomputeormemoryconstrained
conditions,wesplitthePufferdatasetintofourquartersaccording devices[58].InSection4.2,wehaveshowedthatSODAisrobust
totherelativestandarddeviationofthroughput(Q1represents againstpredictionerrorsbydesignanddoesnotrequireasophisti-
themoststablenetworkconditions,whileQ4representsthemost catedthroughputpredictor.Wenowdemonstratethisempirically.
volatilenetworkconditions).Ingeneral,themorevolatilenetwork First,wereplacedthethroughputpredictorusedinsimulations
conditionsare,themoretheQoEperformanceofanyABRcon- withaperfectshort-termthroughputpredictor.Next,wegradually
trollerdegrades,asevidencedbythetrendinFigure10fromleft introducedmoreandmorewhitenoisetotheperfectthroughput
toright.Nonetheless,SODAconsistentlyoutperformsbaselineABR predictionsandobservedhowdifferentABRcontrollersbehave
controllersunderallnetworkconditions.Theimprovementinterms accordingly.Thisexperimentwasconductedonarandomsubset
ofmeanQoEscorescomparedtothebestbaselineacrossdifferent ofournetworkdatasetswithasizeof10,000sessions.Notethat
networkdatasetsrangesfrom9.55%to27.8%,whichmainlystems throughputpredictiondiscountswereturnedoffforallABRcon-
fromimprovementintermsofsmoothness(shorterrebuffering
trollerstorevealtheirintrinsicrobustness.1
timeandlessbitrateswitching).Wediscusstheimprovementof The results are shown in Figure 11, from which we observe
SODAovereachbaselineABRcontrollerbelow: thatallhybridABRcontrollersthattakethroughputpredictions
into account will inevitably be affected by prediction errors to
someextent(BOLAisnotaffectedsinceitispurelybuffer-based).
• SODAvsHYB.HYBisnotasrobustasSODAundervolatilenetwork Nonetheless,SODAstillconsistentlyoutperformsallbaselineABR
conditions.Inaddition,itswitchesupto215%moresinceitdoes
controllersuptoanoiselevelof50%.Forreference,EMApredictor
notconsiderbitrateswitching.
hasanempiricalnoiselevelofabout30%onthesamesessions.More
• SODA vs BOLA & Dynamic. As mainly buffer-based ABR con- importantly,theQoEdegradationof SODAisminimaluptothe
trollers,BOLAandDynamicarefairlyrobustagainstvolatilenet-
referencepointofEMApredictor,i.e.,about10%,whichreinforces
workconditions.Dynamic’sperformanceiswhatonewouldex-
pectinatypicalproductionenvironment.Nonetheless,SODAis
1TherankingbetweendifferentABRcontrollersinthissectionmaybedifferentfrom
abletoachievesimilarmeanutilitieswithoutsacrificingmean
thatinFigure10,whichrevealsthattherobustnessofcertainABRcontrollersshould
rebufferingratios,provingitsoutstandingrobustnessasahybrid beattributetothroughputpredictiondiscountsinsteadofintrinsicdesigns.
621

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
Figure10:ThemeanQoEscores,utilities,rebufferingratiosandswitchingratesofSODAandbaselineABRcontrollersunder
eachnetworkdataset.ThePufferdatasetissplitintofourquartersaccordingthethroughputvariance(Q1beinglowestwhile
Q4beinghighest).SODAhasconsistentlyhighermeanQoEscoresandlowerswitchingratesthanallbaselineABRcontrollers
underallnetworkconditions.(Errorbarsrepresent95%confidenceintervals.)
6.2 PrototypeEvaluation
We next present emulation results from our local client-server
deploymentwhereweimplementedSODAinthePufferplatform[46].
ThankstoChromeDevTools’newcapabilitytothrottleWebSocket
requests [59], we could replay our network datasets directly in
ChromeusingWebDriver[63].Theresultsareintendedtohighlight
therobustnessofdifferentABRcontrollersunderactualbrowser-
basedplayback.Fortheseexperiments,weallowedamaximum
bufferlengthof15seconds,assetbyPuffer.
Figure11:ThemeanQoEscoresforSODAandbaselineABR
controllersundervariableamountsofwhitenoise.(Theerror 6.2.1 ExperimentalSetup. Thevideosourcewasanewsclipen-
barsrepresent95%confidenceintervals.) codedinfivedifferentresolutions(426×240,640×360,854×480,
1280×720,and1920×1080)withaconstantratefactorof26and
asegmentlengthof2seconds.Tobefairtothoselearning-based
theideathatapracticaldeploymentof SODAdoesnot requirea ABRcontrollerstrainedspecificallyforthePufferplatform,weonly
sophisticatedthroughputpredictor.2
consideredthePufferdataset.Sincetheaveragebitrateofthehigh-
estresolutionisonlyabout2Mb/s,wetakearandomsubsetofthe
2Inpractice,weobservethatEMApredictorisactuallymuchbetterthanaperfect
Pufferdatasetwithasizeof1,000sessionswhosemeanthroughput
short-termpredictorwith30%whitenoisebecausethenoisepatternsaredifferent,
whichmeansthatrealgapislessthan10%. isbelow2Mb/stocreatechallengingscenarios.
622

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
6.2.2 BaselineABRControllers. Inresponsetothegrowinginterest wherecustomerswererandomlyassignedSODAortheproduction
inlearning-basedthroughputpredictorsandABRcontrollersin baselinecontroller.Theexperimentranformorethan1weekwith
theresearchcommunity,weincludedtworepresentativelearning- live streams delivered to more than 10 countries. In total, SODA
basedABRcontrollersforlocaldeploymentontopofthemajor sessionsloggedmorethan50,000streaminghours.
baselineABRcontrollersfromnumericalsimulations: Figure13showsSODA’sperformancerelativetotheproduction
• Fugu[46]:DevelopedaspartofthePufferproject,itfeaturesa
deployedandtunedcontroller.First,noticethatSODAconsistently
improvesallthemetricsacrossalldevicefamilies,reducingthe
learning-basedstochasticthroughputpredictor,whileitsunder-
lyingcontrolalgorithmissimilartoMPC.
frequencyofbitrateswitchingonset-topboxesby88.8%.SODAreally
shinesonHTML5browserswhereitreducedthemeanrebuffering
• CausalSimRL[60]:Amodernimplementationofareinforcement
ratiobyupto53.0%inadditionto81.8%reductioninswitching.
learning(RL)-basedABRcontrollerPensieve[22].Itistrained
This is because HTML5 browsers experience more volatility in
usingCausalSimforthePufferplatform.
networkconditionscomparedtosmartTVsandset-topboxesand
6.2.3 QoEPerformance. Pufferemploysstructuresimilarityindex thuspresentgreateropportunityforimprovement.Finally,notice
measures(SSIM)[4]toquantifyutility,thustocomparefairlyus- thatonallthreeplatforms,theaveragedurationofsessionincreased,
ingPuffer,weadaptmeanutilitytonormalizedmeanSSIM,i.e., with5.91%improvementonset-topboxes.Livestreamingsessions
𝑣¯=SSIM/SSIM
max
.Thedefinitionsofrebufferingratio,switching forsportseventsroutinelyspanmultiplehours(e.g.,2-hoursoccer
rate,andQoEscoreremainthesame.Theaggregatestatisticsor broadcast,3.5-hourcricketbroadcast),soa5.91%increasetranslates
QoEscoresandindividualQoEcomponentsacrossallsessionsare tomorethan5minutesduration.
showninFigure12.SODAoutperformsthebestbaseline(Fugu)by TakeawaysfromProductionDeployment.Theproduction
30.4%intermsofmeanQoEscore.Moreimportantly,SODAisthe deploymentshowsthatSODAispracticalandcanbewidelydeployed
onlyABRcontrollerthatachieveslowmeanrebufferingratioand acrossdifferentdevicetypesandnetworkconnections.Furthermore,
switchingratesimultaneously,whichtranslatestosuperiorsmooth- toachieveitssignificantperformancegains,itissufficientforSODA
nessofadaptivestreaming.Wehighlightcomparisonswiththenew tousesimpleslidingwindow-basedthroughputpredictors.
baselineABRcontrollersbelow:
7 RELATEDWORK
• SODAvsMPC&Fugu.MPCandFuguaregroupedtogethersince,
apartfromthemoresophisticatedstochasticthroughputpre- 7.1 AdaptiveBitrateStreaming
dictor,Fugusharesasimilarunderlyingcontrolalgorithmwith Bitrateadaptationhasreceivedsignificantattentionfromthemul-
MPC.Whiletheybothachieveslightlyhighermeanutilitiesthan timediaresearchcommunity.Buffer-basedcontrollerslikeBBA[15]
SODAandreasonablylowmeanswitchingrates,thesebenefits and BOLA [36, 44] make bitrate decisions based on buffer occu-
areovershadowedbyworsemeanrebufferingratios(230%and pancy,whilehybridcontrollerslikeHYB[24],MPC[17]andDYNAMIC
104%worserespectively).AlthoughFugupartiallymitigatesthe [44] combine throughput predictions with buffer occupancy to
rebufferingissueduetoitsstochasticthroughputpredictor,itis makedecisions.SODAbelongstothelattercategory.Therearealso
stillnotrobustenoughforchallengingnetworkconditions. learning-basedcontrollerssuchasPensive[22]thatutilizerein-
• SODA vs CausalSimRL. CausalSimRL achieves slightly higher forcementlearningtolearnabitrateselectionstrategy.Another
meanutilitythanSODAandareasonablylowmeanrebuffering relevant stream of work focuses on improving the accuracy of
ratio.However,itswitchesbitrates86.3%moreoftenthanSODA. throughputpredictions,includingCS2P[20],Fugu[46],andXatu
Duetotheblack-boxnatureofRL-basedABRcontrollers,itis [50].Ourworkmakesnoassumptiononthequalityofthroughput
hardtoreasonwhythisisthecase.Inaddition,thereexistsno predictionsanddoesnotrequireasophisticatedthroughputpre-
straightforwardwaytotuneanRL-basedcontrollerinfavorof dictor.Pastworkshavealsoconsideredupgradingthedownloaded
oneparticularQoEcomponentwithoutacompleteretraining.In segmentsthroughreplacement[36]whichwedonotconsiderin
aproductionenvironment,itishighlydesirablethatthetrade-off thispaper.
betweendifferentQoEcomponentsistunable.
7.2 VideoQualityofExperience
6.3 ProductionDeployment Theadventofvideocontentdeliverynetworks[2,6]inthelate
WenowdescribetheresultsfromdeployingSODAforlivestreams 1990’sledtoeffortsinindustrytodefineandmeasurequalitymet-
deliveredonAmazonPrimeVideo.Thebitrateladderforthese ricsforvideodelivery.Sincethenthequalityofvideodeliveryis
videostreamshadthefollowingbitraterungs{0.2,0.45,0.8,1.2,1.8, awellstudiedtopicwithearlyworkontheAkamaiStreamAna-
2,4,5,6.5,8.0}Mb/s.Thisrangeofavailablebitratesfullyexercised lyzersystemwhichdefinedmetricssuchasstartuptime,rebuffer
SODA’sbitrateadaptationcapabilityaswellastesteditsruntime ratio,bitrateandfailuresetcandmeasuredthesemetricsusingdata
feasibilityonactualdevices.Theexperimentwasrunonthreede- derivedfromvideoplayersdeployedaroundtheworld[3,66].Sub-
vicefamilies,including(i)desktops/laptops(HTML5browsers),(ii) sequently,[7]showedthata1%increaseinrebufferingcorrelated
smartTVs,and(iii)set-topboxes.Onallthreeplatforms,SODAused witha3-minutereductionintheamountoftimeusersstreamed
asimpleslidingwindow-basedthroughputpredictor.Alldevices livecontent.AstudyonYouTube[21]foundthatbitratefluctua-
were20secondsbehindliveaction,sotheycouldaccumulateat tionsstronglycorrelatewithauserabandoningthesession.Beyond
most20secondsofbuffer.Tocompareperformancewithapro- correlations,thefirststudy[9]toestablishacausalrelationship
ductiontunedbaseline,weconductedlarge-scaleA/Bexperiments betweenvideoqualityanduserbehaviorusedquasi-experimental
623

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
Figure12:ThemeanQoEscores,utilities,rebufferingratios,andswitchingratesfromlocaldeployment.SODAagainhasthe
highestmeanQoEscoreandunlikeallotherbaselines,simultaneouslyachievesultralowmeanrebufferingratioandswitching
rate.(Errorbarsrepresent95%confidenceintervals.)
studyingMPC-basedalgorithmsviaexponentiallydecayingpertur-
bationbounds[49,55,56].Ourworkshowsthatthisdecayproperty
holdsunderourmodelofadaptivevideostreaming,allowingusto
establishperformanceguaranteesforSODA.
8 LIMITATIONSANDFUTUREWORK
Anemerginggenre(but,stillasmallfraction)oflivestreamingis
ultra-lowlatencylivestreamswherethedelaybetweenthecapture
ofaneventanditsdisplaytotheuserisrequiredtobeoftheorder
ofafewseconds,asopposedto10to20secondsforthetraditional
livestreamsusedinourcurrentwork.Infuturework,wewould
liketostudyifourSOCO-basedstrategycanbeadaptedforultra-
lowlatencylivestreamswithbufferlengthsintheorderofafew
seconds.Themainchallengewithultra-smallbuffersizesisthatit
Figure13:Thechangeinmeanviewingdurations(higheris
ishardertopreventrebufferingandbitrateswitchinginthisregime
better),bitrates(higherisbetter),rebufferingratios(loweris
astheABRcontrollerneedstoreacttonetworkfluctuationsina
better),andswitchingrates(lowerisbetter)ofSODAcompared
significantlyshorteramountoftime.
totheproductionbaseline.
9 CONCLUSION
designs(QEDs)toquantifythecausal(adverse)impactofstartup Inthiswork,weproposeasmoothness-optimizeddynamicadaptive
delay,rebuffering,andfailuresonuserengagement,abandonment, (SODA)controllerthataddressesthisissueinatheoreticallysound
andrepeatviewership.Arelatedwork[11]builtpredictivemodels way.ThankstoSODA’srobustnessagainstpredictionerrorsand
foruserengagementbasedonQoEmetrics.Ourworkleverages lowruntimecomplexity,itisreadilydeployableinawiderange
insightsfromtheseworksinourABRcontrollerdesign. ofproductionenvironments.Throughnumericalsimulationsand
prototypeevaluation,weshowthatSODAconsistentlyoutperforms
7.3 SmoothedOnlineConvexOptimization
thestate-of-the-artbaselines.Moreimportantly,wedeployedSODA
inamajorvideostreamingproviderwhereSODAsignificantlyre-
Ouralgorithmbuildsonrecentdevelopmentsinsmoothedonline
ducedbitrateswitchingbyupto88.8%comparedtoafine-tuned
convexoptimization(SOCO),avariantofonlineoptimizationthat
productionbaseline.SODA’snoveltime-basedABRformulationand
penalizesswitchingbetweenconsecutivedecisionsviaa“switch-
theoreticalinsightsshednewlightonhowtoachieveconsistent
ingcost.”[25,33,34].Inrecentyears,thedesignandanalysisof
high-qualityvideostreaming.
algorithmsforSOCOhasreceivedconsiderableattention,e.g.,[14,
25,31,32,34,37],withoptimalonlinealgorithmsemerginginvari-
ACKNOWLEDGMENTS
oussettings[33,42,48,62]andavarietyofapplicationsreceiving
Wethanktheanonymousreviewersandourshepherdfortheirvalu-
attention[10,12,26,43,53,55,57].SOCO’sswitchingcostmodel
ablefeedback,aswellascolleaguesatAmazonPrimeVideofortheir
inspiresourdesignof SODAforvideostreaming.
Ourmathematicalformulationofadaptivevideostreamingcan
supportwiththeproductiondeploymentof SODA.Thisworkwas
fundedbyNSFundergrantsCAREER-204564,CCF-2325956,CNS-
beviewedasaspecificexampleofonline(optimal)control[54].
1763617,CNS-1901137,CNS-2102963,CNS-2106299,CNS-2106403,
Similartoonlineoptimization,onlinecontrolseekstodesigna
CNS-2106463,CNS-2146814,CPS-2136197,andNGSDI-2105648,as
controllertominimizethetotalcostincurredoverafinitehorizon.
wellasanAmazonResearchAward.TheresearchofYihengLin
Thetheoreticalboundsinthispaperaremostrelatedtoworksthat
wasadditionallysupportedbyAmazonAI4ScienceFellowshipand
studyhowfuturepredictionscanimproveonlinecontrollerperfor-
PIMCOGraduateFellowshipinDataScience.
mance[39,47,49,52].Ourproofsfollowananalyticframeworkfor
624

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
REFERENCES [19] he1enh.2016.ReproducingNetworkResearch.(May2016).https://reproducin
[1] MunChoonChanandRamachandranRamjee.2002.TCP/IPPerformance gnetworkresearch.wordpress.com/2016/05/30/cs244-16-failed-experiments-
over3GWirelessLinkswithRateandDelayVariation.InProceedingsofthe with-fastmpc-integrating-rate-based-adaptive-streaming-into-vlc/.
[20] YiSun,XiaoqiYin,JunchenJiang,VyasSekar,FuyuanLin,NanshuWang,
8thAnnualInternationalConferenceonMobileComputingandNetworking
(MobiCom’02).Atlanta,Georgia,USA,71–82.isbn:158113486X.doi:10.1145 TaoLiu,andBrunoSinopoli.2016.CS2P:ImprovingVideoBitrateSelection
/570645.570655. andAdaptationwithData-DrivenThroughputPrediction.InProceedingsof
[2] JohnDilley,BruceM.Maggs,JayParikh,HaraldProkop,RameshK.Sitaraman, the2016ACMSIGCOMMConference.ACM,NewYork,NY,USA,(Aug.2016),
andWilliamE.Weihl.2002.GloballyDistributedContentDelivery.IEEEInternet 272–285.isbn:9781450341936.doi:10.1145/2934872.2934898.
Computing,6,5,50–58. [21] ChristosGeorgeBampis,ZhiLi,AnushKrishnaMoorthy,IoannisKatsavouni-
[3] R.K.SitaramanandR.W.Barton.2003.Methodandapparatusformeasuring dis,AnneAaron,andAlanConradBovik.2017.StudyofTemporalEffectson
streamavailability,qualityandperformance.USPatent7,010,598.(Feb.2003). SubjectiveVideoQualityofExperience.IEEETransactionsonImageProcessing,
[4] Z.Wang,A.C.Bovik,H.R.Sheikh,andE.P.Simoncelli.2004.ImageQuality 26,11,5217–5231.doi:10.1109/TIP.2017.2729891.
Assessment:FromErrorVisibilitytoStructuralSimilarity.IEEETransactions [22] HongziMao,RaviNetravali,andMohammadAlizadeh.2017.NeuralAdap-
onImageProcessing,13,(Apr.2004),600–612,4,(Apr.2004).doi:10.1109/TIP.2 tiveVideoStreamingwithPensieve.InACM,(Aug.2017),197–210.isbn:
003.819861. 9781450346535.doi:10.1145/3098822.3098843.
[5] JunxianHuang,QiangXu,BirjodhTiwana,Z.MorleyMao,MingZhang,and [23] YanyuanQin,RuofanJin,ShuaiHao,KrishnaR.Pattipati,FengQian,Sub-
ParamvirBahl.2010.AnatomizingApplicationPerformanceDifferenceson habrataSen,BingWang,andChaoqunYue.2017.Acontroltheoreticapproach
Smartphones.InProceedingsofthe8thInternationalConferenceonMobile toABRvideostreaming:AfreshlookatPID-basedrateadaptation.InIEEE
Systems,Applications,andServices(MobiSys’10).SanFrancisco,California, INFOCOM2017-IEEEConferenceonComputerCommunications.IEEE,(May
USA,165–178.isbn:9781605589855.doi:10.1145/1814433.1814452. 2017),1–9.isbn:978-1-5090-5336-0.doi:10.1109/INFOCOM.2017.8057056.
[6] E.Nygren,RameshK.Sitaraman,andJ.Sun.2010.TheAkamaiNetwork:A [24] ZahaibAkhtar,YunSeongNam,RameshGovindan,SanjayRao,JessicaChen,
platformforhigh-performanceInternetapplications.ACMSIGOPSOperating EthanKatz-Bassett,BrunoRibeiro,JibinZhan,andHuiZhang.2018.Oboe:
SystemsReview,44,3,2–19. Auto-TuningVideoABRAlgorithmstoNetworkConditions.InACM,(Aug.
[7] FlorinDobrian,VyasSekar,AsadAwan,IonStoica,DilipJoseph,AdityaGan- 2018),44–58.isbn:9781450355674.doi:10.1145/3230543.3230558.
jam,JibinZhan,andHuiZhang.2011.UnderstandingtheImpactofVideoQual- [25] NiangjunChen,GautamGoel,andAdamWierman.2018.SmoothedOnline
ityonUserEngagement.InProceedingsoftheACMSIGCOMM2011Conference ConvexOptimizationinHighDimensionsviaOnlineBalancedDescent.In
(SIGCOMM’11).Toronto,Ontario,Canada,362–373.isbn:9781450307970.doi: ProceedingsofConferenceOnLearningTheory(COLT),1574–1594.
10.1145/2018436.2018478. [26] YingyingLi,GuannanQu,andNaLi.2018.OnlineOptimizationwithPredic-
[8] Te-YuanHuang,NikhilHandigol,BrandonHeller,NickMcKeown,andRamesh tionsandSwitchingCosts:FastAlgorithmsandtheFundamentalLimit.(2018).
Johari.2012.Confused,timid,andunstable.InProceedingsofthe2012Internet arXiv:1801.07780v3[math.OC].
MeasurementConference.ACM,NewYork,NY,USA,(Nov.2012),225–238.isbn: [27] DarijoRaca,JasonJ.Quinlan,AhmedH.Zahran,andCormacJ.Sreenan.2018.
9781450317054.doi:10.1145/2398776.2398800. BeyondThroughput:A4GLTEDatasetwithChannelandContextMetrics.In
[9] S.ShunmugaKrishnanandRameshK.Sitaraman.2012.VideoStreamQual- Proceedingsofthe9thACMMultimediaSystemsConference.ACM,NewYork,NY,
ityImpactsViewerBehavior:InferringCausalityUsingQuasi-Experimental USA,(June2018),460–465.isbn:9781450351928.doi:10.1145/3204949.3208123.
Designs.InProceedingsofthe2012InternetMeasurementConference(IMC’12). [28] NamanAgarwal,BrianBullins,EladHazan,ShamKakade,andKaranSingh.
Boston,Massachusetts,USA,211–224.isbn:9781450317054.doi:10.1145/2398 2019.Onlinecontrolwithadversarialdisturbances.InInternationalConference
776.2398799. onMachineLearning.PMLR,111–119.
[10] MinghongLin,ZhenhuaLiu,AdamWierman,andLachlanLHAndrew.2012. [29] ZahaibAkhtar,YaguangLi,RameshGovindan,EmirHalepovic,ShuaiHao,Yan
Onlinealgorithmsforgeographicalloadbalancing.InProceedingsoftheInter- Liu,andSubhabrataSen.2019.AViC:ACacheforAdaptiveBitrateVideo.In
nationalGreenComputingConference(IGCC),1–10. Proceedingsofthe15thInternationalConferenceonEmergingNetworkingExper-
[11] AthulaBalachandran,VyasSekar,AdityaAkella,SrinivasanSeshan,IonStoica, imentsAndTechnologies(CoNEXT’19).AssociationforComputingMachinery,
andHuiZhang.2013.Developingapredictivemodelofqualityofexperience Orlando,Florida,305–317.isbn:9781450369985.doi:10.1145/3359989.3365423.
forinternetvideo.SIGCOMMComput.Commun.Rev.,43,4,(Aug.2013),339– [30] AaronDAmes,SamuelCoogan,MagnusEgerstedt,GennaroNotomista,Koushil
350.doi:10.1145/2534169.2486025. Sreenath,andPauloTabuada.2019.Controlbarrierfunctions:theoryandap-
[12] MinghongLin,AdamWierman,LachlanL.H.Andrew,andEnoThereska. plications.In201918thEuropeancontrolconference(ECC).IEEE,3420–3431.
2013.DynamicRight-SizingforPower-ProportionalDataCenters.IEEE/ACM [31] C.J.Argue,SébastienBubeck,MichaelB.Cohen,AnupamGupta,andYin
TransactionsonNetworking,21,5,(Oct.2013),1378–1391.doi:10.1109/TNET.2 TatLee.2019.ANearly-LinearBoundforChasingNestedConvexBodies.In
012.2226216. Proceedingsofthe2019AnnualACM-SIAMSymposiumonDiscreteAlgorithms
[13] MasoudBadiei,NaLi,andAdamWierman.2015.Onlineconvexoptimization (SODA).Proceedings.SocietyforIndustrialandAppliedMathematics,(Jan.
withrampconstraints.In201554thIEEEConferenceonDecisionandControl 2019),117–122.doi:10.1137/1.9781611975482.8.
(CDC).IEEE,6730–6736. [32] SébastienBubeck,Bo’azKlartag,YinTatLee,YuanzhiLi,andMarkSellke.2019.
[14] NikhilBansal,AnupamGupta,RavishankarKrishnaswamy,KirkPruhs,Kevin ChasingNestedConvexBodiesNearlyOptimally.InProceedingsofthe2020
Schewior,andCliffStein.2015.A2-CompetitiveAlgorithmForOnlineConvex ACM-SIAMSymposiumonDiscreteAlgorithms(SODA).Proceedings.Society
OptimizationWithSwitchingCosts.InApproximation,Randomization,and forIndustrialandAppliedMathematics,(Dec.2019),1496–1508.doi:10.1137/1
.9781611975994.91.
CombinatorialOptimization.AlgorithmsandTechniques(APPROX/RANDOM
2015)(LeibnizInternationalProceedingsinInformatics(LIPIcs)).NaveenGarg, [33] GautamGoel,YihengLin,HaoyuanSun,andAdamWierman.2019.Beyondon-
KlausJansen,AnupRao,andJoséD.P.Rolim,(Eds.)Vol.40.SchlossDagstuhl–Leibniz- linebalanceddescent:Anoptimalalgorithmforsmoothedonlineoptimization.
ZentrumfuerInformatik,Dagstuhl,Germany,96–109.doi:10.4230/LIPIcs AdvancesinNeuralInformationProcessingSystems,32.
.APPROX-RANDOM.2015.96. [34] GautamGoelandAdamWierman.2019.AnOnlineAlgorithmforSmoothed
[15] Te-YuanHuang,RameshJohari,NickMcKeown,MatthewTrunnell,andMark RegressionandLQRControl.InProceedingsoftheMachineLearningResearch.
Watson.2015.ABuffer-BasedApproachtoRateAdaptation:Evidencefrom Vol.89,2504–2513.http://proceedings.mlr.press/v89/goel19a.html.
aLargeVideoStreamingService.ACMSIGCOMMComputerCommunication [35] MingShi,XiaojunLin,andLeiJiao.2019.Onthevalueoflook-aheadincom-
Review,44,(Feb.2015),187–198,4,(Feb.2015).doi:10.1145/2740070.2626296. petitiveonlineconvexoptimization.ProceedingsoftheACMonMeasurement
[16] YanLiuandJackY.B.Lee.2015.AnEmpiricalStudyofThroughputPrediction andAnalysisofComputingSystems,3,2,22.
inMobileDataNetworks.In2015IEEEGlobalCommunicationsConference [36] KevinSpiteri,RameshSitaraman,andDanielSparacio.2019.FromTheoryto
(GLOBECOM),1–6.doi:10.1109/GLOCOM.2015.7417858. Practice:ImprovingBitrateAdaptationintheDASHReferencePlayer.ACM
[17] XiaoqiYin,AbhishekJindal,VyasSekar,andBrunoSinopoli.2015.AControl- TransactionsonMultimediaComputing,Communications,andApplications,15,
TheoreticApproachforDynamicAdaptiveVideoStreamingoverHTTP.InPro- 2s,(Apr.2019),1–29.doi:10.1145/3336497.
[37] C.J.Argue,AnupamGupta,andGuruGuruganesh.2020.Dimension-Free
ceedingsofthe2015ACMConferenceonSpecialInterestGrouponDataCommu-
nication.ACM,NewYork,NY,USA,(Aug.2015),325–338.isbn:9781450335423. BoundsforChasingConvexFunctions.InProceedingsofThirtyThirdConference
doi:10.1145/2785956.2787486. onLearningTheory.PMLR,(July2020),219–241.RetrievedFeb.4,2022from.
[18] MojganGhasemi,ParthaKanuparthy,AhmedMansy,TheophilusBenson,and [38] SarahDean,HoriaMania,NikolaiMatni,BenjaminRecht,andStephenTu.
JenniferRexford.2016.PerformanceCharacterizationofaCommercialVideo 2020.Onthesamplecomplexityofthelinearquadraticregulator.Foundations
StreamingService.InProceedingsofthe2016InternetMeasurementConference. ofComputationalMathematics,20,4,633–679.
ACM,NewYork,NY,USA,(Nov.2016),499–511.isbn:9781450345262.doi: [39] YingyingLi,GuannanQu,andNaLi.2020.Onlineoptimizationwithpredic-
10.1145/2987443.2987481. tionsandswitchingcosts:Fastalgorithmsandthefundamentallimit.IEEE
TransactionsonAutomaticControl,66,10,4761–4768.
625

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
[40] EmilyMarx,FrancisY.Yan,andKeithWinstein.2020.ImplementingBOLA- ProceedingsofThe26thInternationalConferenceonArtificialIntelligenceand
BASIConPuffer:LessonsfortheuseofSSIMinABRlogic,(Nov.2020). Statistics.PMLR,(Apr.2023),9377–9399.
[41] DarijoRaca,DylanLeahy,CormacJ.Sreenan,andJasonJ.Quinlan.2020. [63] MDNcontributors.2023.WebDriver.(June2023).https://developer.mozilla.org
BeyondThroughput,TheNextGeneration:A5GDatasetwithChanneland /en-US/docs/Web/WebDriver.
ContextMetrics.InProceedingsofthe11thACMMultimediaSystemsConference. [64] DASHIndustryForum.2023.dash.js:AReferenceClientImplementationfor
ACM,NewYork,NY,USA,(May2020),303–308.isbn:9781450368452.doi: thePlaybackofMPEGDASHviaJavaScriptandCompliantBrowsers.https:
10.1145/3339825.3394938. //github.com/Dash-Industry-Forum/dash.js.
[42] MarkSellke.2020.Chasingconvexbodiesoptimally.InProceedingsofthe [65] YouTube.2023.YouTubeRecommendedUploadEncodingSettings.https://sup
Thirty-FirstAnnualACM-SIAMSymposiumonDiscreteAlgorithms(SODA’20). port.google.com/youtube/answer/1722171.
SocietyforIndustrialandAppliedMathematics,USA,(Jan.2020),1509–1518. [66] Akamai.[n.d.]StreamAnalyzerServiceDescription.https://groups.cs.umass
RetrievedOct.15,2021from. .edu/ramesh/wp-content/uploads/sites/3/2023/10/Stream_Analyzer_Service
[43] GuanyaShi,YihengLin,Soon-JoChung,YisongYue,andAdamWierman. _Description.pdf.().
2020.Onlineoptimizationwithmemoryandcompetitivecontrol.Advancesin
NeuralInformationProcessingSystems,33,20636–20647.
[44] KevinSpiteri,RahulUrgaonkar,andRameshK.Sitaraman.2020.BOLA:Near-
OptimalBitrateAdaptationforOnlineVideos.IEEE/ACMTransactionsonNet-
working,28,4,(Aug.2020),1698–1711.doi:10.1109/TNET.2020.2996964.
[45] DongzhuXu,AnfuZhou,XinyuZhang,GuixianWang,XiLiu,CongkaiAn,
YimingShi,LiangLiu,andHuadongMa.2020.UnderstandingOperational5G:
AFirstMeasurementStudyonItsCoverage,PerformanceandEnergyConsump-
tion.In(SIGCOMM’20).VirtualEvent,USA,479–494.isbn:9781450379557.
doi:10.1145/3387514.3405882.
[46] F.Y.Yan,H.Ayers,C.Zhu,S.Fouladi,J.Hong,K.Zhang,P.Levis,andK.
Winstein.2020.LearninginSitu:ARandomizedExperimentinVideoStreaming.
InProceedingsofthe17thUSENIXSymposiumonNetworkedSystemsDesign
andImplementation,NSDI2020,495–511.isbn:9781939133137.https://www.us
enix.org/conference/nsdi20/presentation/yan.
[47] ChenkaiYu,GuanyaShi,Soon-JoChung,YisongYue,andAdamWierman.2020.
Thepowerofpredictionsinonlinecontrol.AdvancesinNeuralInformation
ProcessingSystems,33,1994–2004.
[48] C.J.Argue,AnupamGupta,ZiyeTang,andGuruGuruganesh.2021.Chasing
ConvexBodieswithLinearCompetitiveRatio.JournaloftheACM,68,5,1–10.
doi:10.1145/3450349.
[49] YihengLin,YangHu,HaoyuanSun,GuanyaShi,GuannanQu,andAdam
Wierman.2021.Perturbation-basedRegretAnalysisofPredictiveControlin
LinearTimeVaryingSystems.arXivpreprintarXiv:2106.10497.
[50] YunSeongNam,JianfeiGao,ChandanBothra,EhabGhabashneh,SanjayRao,
BrunoRibeiro,JibinZhan,andHuiZhang.2021.Xatu:RicherNeuralNetwork
BasedPredictionforVideoStreaming.ProceedingsoftheACMonMeasurement
andAnalysisofComputingSystems,5,3,(Dec.2021),1–26.doi:10.1145/3491056.
[51] SunghoShinandVictorM.Zavala.2021.ControllabilityandObservabilityIm-
plyExponentialDecayofSensitivityinDynamicOptimization.arXivpreprint
arXiv:2101.06350.
[52] RunyuZhang,YingyingLi,andNaLi.2021.Ontheregretanalysisofonline
LQRcontrolwithpredictions.In2021AmericanControlConference(ACC).IEEE,
697–703.
[53] NicolasChristianson,ChristopherYeh,TongxinLi,MahdiTorabiRad,Azarang
Golmohammadi,andAdamWierman.2022.Robustifyingmachine-learned
algorithmsforefficientgridoperation.InNeurIPS2022WorkshoponTackling
ClimateChangewithMachineLearning.https://www.climatechange.ai/papers
/neurips2022/19.
[54] EladHazanandKaranSingh.2022.Introductiontoonlinenonstochasticcontrol.
arXivpreprintarXiv:2211.09619.
[55] YihengLin,JudyGan,GuannanQu,YashKanoria,andAdamWierman.2022.
DecentralizedOnlineConvexOptimizationinNetworkedSystems.InInterna-
tionalConferenceonMachineLearning.PMLR,13356–13393.
[56] YihengLin,YangHu,GuannanQu,TongxinLi,andAdamWierman.2022.
Bounded-RegretMPCviaPerturbationAnalysis:PredictionError,Constraints,
andNonlinearity.arXivpreprintarXiv:2210.12312.
[57] WeiciPan,GuanyaShi,YihengLin,andAdamWierman.2022.Onlineopti-
mizationwithfeedbackdelayandnonlinearswitchingcost.Proceedingsofthe
ACMonMeasurementandAnalysisofComputingSystems,6,1,1–34.
[58] TalhaWaheed,IhsanAyyubQazi,ZahaibAkhtar,andZafarAyyubQazi.2022.
CoalNotDiamonds:HowMemoryPressureFaltersMobileVideoQoE.In
(CoNEXT’22).Roma,Italy,307–320.isbn:9781450395083.doi:10.1145/355505
0.3569120.
[59] JecelynYeen.2022.What’sNewInDevTools(Chrome99).(Feb.2022).https:
//developer.chrome.com/en/blog/new-in-devtools-99/.
[60] A.Alomar,P.Hamadanian,A.Nasr-Esfahany,A.Agarwal,M.Alizadeh,and
D.Shah.2023.CausalSim:ACausalFrameworkforUnbiasedTrace-Driven
Simulation.In1115–1147.isbn:9781939133335.https://www.usenix.org/confe
rence/nsdi23/presentation/alomar.
[61] ChandanBothra,JianfeiGao,SanjayRao,andBrunoRibeiro.2023.Veritas:
AnsweringCausalQueriesfromVideoStreamingTraces.InProceedingsofthe
ACMSIGCOMM2023Conference(ACMSIGCOMM’23).NewYork,NY,USA,
738–753.doi:10.1145/3603269.3604828.
[62] NicolasChristianson,JunxuanShen,andAdamWierman.2023.OptimalRobustness-
ConsistencyTradeoffsforLearning-AugmentedMetricalTaskSystems.In
626

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
Appendicesaresupportingmaterialthathasnotbeenpeer-reviewed.
A PROOFOUTLINE
Inthissection,wepresentanoutlineofourtheoreticalanalysisforSODA.AswediscussedinSection4,ourproofisbasedonanexponentially
decayingperturbationboundthatrelatesthebehaviorofthesolutiontotheoptimizationproblemdefiningSODAasafunctionofproblem
parameters.Thissectionisorganizedasfollows:Wefirstintroducethemodelingof SODAthatweusetoestablishtheoreticalresultsin
SectionA.1.Then,weintroducetheexponentiallydecayingperturbationbound,itsimplications,andtheproofideainSectionA.2.Next,we
presenttheoutlinesforprovingSODA’sperformanceguaranteeswiththehelpofexponentiallydecayingperturbationboundsinSectionsA.3
andA.4.Finally,wewilldiscusssomesufficientconditionsunderwhichtheoptimalbitratesequencecanbeapproximatedbyamonotonic
sequenceinSectionA.5.
A.1 TheoreticalProblemSetting
WefirstintroducethenotationusedtodefinetheperformancemetricsandthevariantofSODAstudiedinourtheoreticalanalysis.Tomake
theformulationofthevideostreamingproblemclosertoaclassiccontrolproblem,wedefinethe“controlaction”𝑢 astheinverseofthe
𝑡
bitrate(i.e.,𝑢 = 1 ).Recallthatweset𝑣(𝑟)= 1 inourtheoreticalanalysis.Thus,wecanwritedownageneralformoftheoptimization
| 𝑡                          | 𝑟   |     | 𝑟                       |                                      |       |     |     |     |     |     |
| -------------------------- | --- | --- | ----------------------- | ------------------------------------ | ----- | --- | --- | --- | --- | --- |
|                            | 𝑡   |     | 𝑡+𝑝                     |                                      |       |     |     |     |     |     |
| problemsolvedbySODAanduse𝜓 |     |     | (cid:0)(𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ | ;𝐹(cid:1)todenoteitsoptimalsolution: |       |     |     |     |     |     |
|                            |     |     | 𝑡                       | 𝑡:𝑡+𝑝                                |       |     |     |     |     |     |
|                            |     |     | 𝑡+𝑝                     | 𝑡+𝑝                                  | 𝑡+𝑝+1 |     |     |     |     |     |
|                            |     |     | ∑︁                      | 2 ∑︁                                 | ∑︁    |     | 2   |     |     |     |
argmin 𝜔ˆ 𝜏 𝑢 𝜏 +𝛽 𝑏(𝑥 𝜏)+𝛾 |𝑢 𝜏 −𝑢 𝜏−1| +𝐹(𝑥 𝑡+𝑝 ,𝑢 𝑡+𝑝+1) (3a)
𝑥𝑡:𝑡+𝑝,𝑢𝑡+1:𝑡+𝑝𝜏=𝑡
|     |     |     |            | 𝜏=𝑡        | 𝜏=𝑡                    |        |             |     |     |      |
| --- | --- | --- | ---------- | ---------- | ---------------------- | ------ | ----------- | --- | --- | ---- |
|     |     |     | s.t.𝑥 𝜏 =𝑥 | 𝜏−1+𝜔ˆ 𝜏 𝑢 | 𝜏 −1, for𝜏 =𝑡,...,𝑡+𝑝, |        |             |     |     | (3b) |
|     |     |     |            |            | 1                      | 1      |             |     |     |      |
|     |     |     | 0≤𝑥        | 𝜏 ≤𝑥max,   | ≤𝑢 𝜏 ≤                 | , for𝜏 | =𝑡,...,𝑡+𝑝, |     |     | (3c) |
|     |     |     |            | 𝑟max       |                        | 𝑟      |             |     |     |      |
min
|     |     |     | 𝑥 𝑡−1=𝜎 | 𝑡−1,𝑢 𝑡−1=𝜈 | 𝑡−1. |     |     |     |     | (3d) |
| --- | --- | --- | ------- | ----------- | ---- | --- | --- | --- | --- | ---- |
Here,𝜓 𝑡+𝑝 (cid:0)(𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ ;𝐹(cid:1)isdefinedtobeavectorthatcontainsthestates𝑥 andcontrolactions𝑢 intheoptimalsolution.
| 𝑡   |     | 𝑡:𝑡+𝑝 |     |     |     |     | 𝑡:𝑡+𝑝 | 𝑡+1:𝑡+𝑝 |     |     |
| --- | --- | ----- | --- | --- | --- | --- | ----- | ------- | --- | --- |
Theinitialcondition(𝜎 𝑡−1,𝜈 𝑡−1),bandwidthsequence𝜔ˆ 𝑡:𝑡+𝑝 ,andterminalcostfunction𝐹 aretheparametersoftheoptimizationproblem.
Fortheterminalcosts,weconsidertwotypesoffunctions:(1)Thezerofunction𝐹 =0,i.e.,𝐹(𝑥,𝑢)=0forall𝑥,𝑢;(2)Theindicatorfunction
𝐹 =I ,whichisdefinedas
𝜎,𝜈
(cid:40)
|     |     |     |          |           | 0   | if𝑥 =𝜎,𝑢   | =𝜈, |     |     |     |
| --- | --- | --- | -------- | --------- | --- | ---------- | --- | --- | --- | --- |
|     |     |     | 𝐹(𝑥,𝑢)=I | 𝜎,𝜈(𝑥,𝑢)= |     |            |     |     |     |     |
|     |     |     |          |           | +∞  | otherwise. |     |     |     |     |
The first type of terminal cost will be used to define the performance metrics (competitive ratio and dynamic regret), and the sec-
ond type will be used in the algorithm design. Since we will use the indicator terminal cost frequently, we introduce the shorthand
|     |     |     |     |     | (cid:16) |     | (cid:17) |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
𝜓˜ 𝑡+𝑝 (cid:0)(𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ ;(𝜎 ,𝜈 𝑡+𝑝+1)(cid:1),whichdenotes𝜓˜ 𝑡+𝑝 (𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ ;I .Weuse𝜄 𝑡+𝑝 (cid:0)(𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ ;𝐹(cid:1)tode-
| 𝑡   | 𝑡:𝑡+𝑝 | 𝑡+𝑝 |     | 𝑡   |     | 𝑡:𝑡+𝑝 | 𝜎𝑡+𝑝,𝜈𝑡+𝑝+1 | 𝑡   | 𝑡:𝑡+𝑝 |     |
| --- | ----- | --- | --- | --- | --- | ----- | ----------- | --- | ----- | --- |
notetheoptimalobjectivevalueoftheoptimizationproblem(3).
Themodelof SODAthatweconsiderinthetheoreticalanalysisissummarizedinAlgorithm2.ThemajordifferencefromtheSODA
algorithmdiscussedinSection3.3isthatweincludetheindicatorterminalcost(inline5)sothatthelasttwostatesinthepredictive
trajectoryareequaltothetargetbufferlevel.ThisterminalconstraintisimportantforourcompetitiveratioresultinTheorem4.1,forwhich
weneedtoboundthesquareddistancebetweenthetrajectoriesofSODAandtheofflineoptimalcontrollerbyapartoftheofflineoptimalcost.
Algorithm2:SODA(fortheoreticalanalysis)
| Require: Predictionhorizon𝐾. |                |          |              |     |     |     |     |     |     |     |
| ---------------------------- | -------------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| 1: for𝑡 =1,2,...,𝑁           |                | do       |              |     |     |     |     |     |     |     |
| 2: Set𝑡′                     | =min{𝑡+𝐾−1,𝑁}. |          |              |     |     |     |     |     |     |     |
| Receivepredictions𝜔ˆ         |                |          | .            |     |     |     |     |     |     |     |
| 3:                           |                | 𝑡+1:𝑡′|𝑡 |              |     |     |     |     |     |     |     |
| if𝑡′                         | <𝑁             |          |              |     |     |     |     |     |     |     |
| 4:                           | then           |          |              |     |     |     |     |     |     |     |
| 5: Setterminalcost𝐹          |                | 𝑡′       | =I 𝑥∗,1/𝜔ˆ . |     |     |     |     |     |     |     |
𝑡′|𝑡
6: else
| Setterminalcost𝐹 |     |     | =0. |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7:               |     | 𝑡′  |     |     |     |     |     |     |     |     |
8: endif
|            | 𝑡′−1(cid:16) |          |                | (cid:17) |     |     |     |     |     |     |
| ---------- | ------------ | -------- | -------------- | -------- | --- | --- | --- | --- | --- | --- |
| 9: Commit𝑢 | 𝑡 =𝜓         | (𝑥 𝑡−1,𝑢 | 𝑡−1);𝜔ˆ 𝑡:𝑡′|𝑡 | ;𝐹 𝑡′ .  |     |     |     |     |     |     |
𝑡
10: endfor
627

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
Usingthenotationsabove,wecanformallydefinetheperformancemetricsweemploy:Letcost(OPT)denotetheofflineoptimalcostone
𝑁 (cid:16) (cid:17)
canachievewhenexactpredictionsofallfuturebandwidthareavailableatthestartoftheproblem,i.e.,cost(OPT)=𝜄 (𝑥0,𝑢0);𝜔 ∗ ;0 .
|     |     |     |     |     |     |     |     |     |     |     |     | 1 1 :𝑁 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Then,
• Dynamicregretisanupperboundonthedifferencecost(SODA)−cost(OPT);
Competitiveratioisanupperboundontheratiocost(SODA)/cost(OPT).
•
A.2 ExponentiallyDecayingPerturbations
Exponentiallydecayingperturbationsisacriticalpropertyofthefinite-timeoptimalcontrolproblemthatouranalysisbuildsupon.We
definethispropertyformallyinDefinitionA.1.
DefinitionA.1(ExponentiallyDecayingPerturbationBound).
Wesaytheexponentiallydecayingperturbationboundholdsifthereexists
| uniformconstants𝐶 | >0,𝜌 | (0,1)suchthatthefollowinginequalitieshold: |     |     |     |     |     |     |     |     |     |     |
| ----------------- | ---- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∈
|     | (cid:12)     |               |          |            |          |        |          | (cid:12)    |     |     |     |     |
| --- | ------------ | ------------- | -------- | ---------- | -------- | ------ | -------- | ----------- | --- | --- | --- | --- |
|     | (cid:12) 𝑡+𝑝 |               |          | 𝑡+𝑝        | (cid:16) |        | (cid:17) | (cid:12)    |     |     |     |     |
|     | 𝜓 (cid:0)(𝜎  | 𝑡−1,𝜈 𝑡−1);𝜔ˆ | 𝑡:𝑡+𝑝 ;0 | (cid:1) −𝜓 | (𝜎 ′ ,𝜈  | ′ );𝜔ˆ | ′ ;0     |             |     |     |     |     |
|     | (cid:12) 𝑡   |               |          | 𝑥𝜏 𝑡       | 𝑡 −1     | 𝑡 −1   | 𝑡 :𝑡+𝑝   | 𝑥𝜏 (cid:12) |     |     |     |     |
|     | (cid:12)     |               |          |            |          |        |          | (cid:12)    |     |     |     |     |
𝑡+𝑝
|     | ≤𝐶𝜌𝜏−𝑡+1(cid:0)(cid:12) |     | ′ (cid:12) (cid:12) | ′   | (cid:12) (cid:1)+𝐶 ∑︁ | 𝜌|𝜏−𝑗| (cid:12) | −𝜔ˆ′ (cid:12) |     |     |     |     |     |
| --- | ----------------------- | --- | ------------------- | --- | --------------------- | --------------- | ------------- | --- | --- | --- | --- | --- |
(cid:12) 𝜎 𝑡−1−𝜎 (cid:12)+ (cid:12) 𝜈 𝑡−1−𝜈 (cid:12) (cid:12) 𝜔ˆ 𝑗 (cid:12) , (4)
|     |     |     | 𝑡 −1 | 𝑡 −1 |     | (cid:12) | 𝑗 (cid:12) |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | --- | -------- | ---------- | --- | --- | --- | --- | --- |
𝑗=𝑡
|     | (cid:12)                  |               |           |               |     |              |           |             |             |          | (cid:12) |     |
| --- | ------------------------- | ------------- | --------- | ------------- | --- | ------------ | --------- | ----------- | ----------- | -------- | -------- | --- |
|     | (cid:12) 𝜓˜ 𝑡+𝑝 (cid:0)(𝜎 |               |           | 𝑡+𝑝+1)(cid:1) |     | 𝑡+𝑝 (cid:16) | ′ ′       | ′           | ′ ′         | (cid:17) | (cid:12) |     |
|     | (cid:12)                  | 𝑡−1,𝜈 𝑡−1);𝜔ˆ | 𝑡:𝑡+𝑝 ;(𝜎 | 𝑡+𝑝 ,𝜈        | −𝜓  | (𝜎           | ,𝜈        | );𝜔ˆ 𝑡 :𝑡+𝑝 | ;(𝜎 𝑡 +𝑝 ,𝜈 | )        | (cid:12) |     |
|     | (cid:12) 𝑡                |               |           |               | 𝑥𝜏  | 𝑡            | 𝑡 −1 𝑡 −1 |             | 𝑡           | +𝑝+1 𝑥𝜏  | (cid:12) |     |
𝑡+𝑝
|     |     |     |     |     |     | (cid:12) | (cid:12) |     | (cid:16)(cid:12) | (cid:12) | (cid:12) | (cid:12) |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ---------------- | -------- | -------- | -------- |
≤𝐶𝜌𝜏−𝑡+1(cid:0)(cid:12) 𝜎 𝑡−1−𝜎 ′ (cid:12) (cid:12) 𝜈 𝑡−1−𝜈 ′ (cid:12) (cid:1)+𝐶 ∑︁ 𝜌|𝜏−𝑗| 𝜔ˆ −𝜔ˆ′ +𝐶𝜌𝑡+𝑝−𝜏 𝜎 −𝜎 ′ 𝜈 𝑡+𝑝+1−𝜈 ′ (cid:17) . (5)
(cid:12) 𝑡 −1 (cid:12)+ (cid:12) 𝑡 −1 (cid:12) (cid:12) 𝑗 𝑗 (cid:12) (cid:12) 𝑡+𝑝 𝑡 +𝑝 (cid:12) + (cid:12) 𝑡 +𝑝+1 (cid:12)
|     |     |     |     |     |     | (cid:12) | (cid:12) |     | (cid:12) | (cid:12) | (cid:12) | (cid:12) |
| --- | --- | --- | --- | --- | --- | -------- | -------- | --- | -------- | -------- | -------- | -------- |
𝑗=𝑡
Intuitively,theexponentialdecayproperty(DefinitionA.1)holdsiftheimpactofaperturbationontheinitialcondition(𝜎 𝑡−1,𝜈 𝑡−1),
prediction𝜔ˆ ,orterminalconstraint(𝜎 ,𝜈 𝑡+𝑝+1)onthecomponent𝑥 intheoptimaltrajectorydecaysexponentiallywithrespecttothe
|     | 𝑗   |     | 𝑡+𝑝 |     |     |     | 𝜏   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
absolutedifferencebetweentheircorrespondingtimeindices.
DuetoitsimportanceforthetheoreticalanalysisofMPC-basedalgorithms,manypreviousworkshaveestablishedexponentiallydecaying
perturbationboundsforvariouscasesofonlineoptimizationwithswitchingcosts[49],optimalcontrolwithunconstraineddynamics[49,
56],andonlineoptimizationinnetworkedsystems[55].Incontrasttopreviouswork,however,thevideostreamingproblem(3)thatwe
considerisaconstrainedoptimalcontrolproblem.Tothispoint,therehasbeenlimitedsuccessinestablishingexponentiallydecaying
perturbationboundsforgeneralconstrainedoptimalcontrolproblems,andexistingresultsthatprovidesufficientconditionsfortheirvalidity
aredifficulttoverify[51,56].
Inthiswork,weleveragethespecialstructureofthevideostreamingproblemtoshowtheexponentiallydecayingperturbationbound
holdsinthissetting.Werequirethefollowingassumptionaboutthebufferconstraints,bandwidth,andthebitraterange.
Thereexistsuniformconstants𝜔 >𝜔 >0suchthatforanytimestep𝑡,wehavethat𝜔 ≤𝜔 ≤𝜔
| AssumptionA.1. |     |     |     | max | min |     |     |     |     |     | min | 𝑡 maxholds.We |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
alsoassumethat𝜔 /𝑟 ≥𝑥 max,and𝜔 /𝑟 −1≤−𝛿holdsforafixedconstant𝛿 >0.
|     | min min |     | max | max |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Intuitively,AssumptionA.1guaranteesthatthecontrollercanalwaysfillupthebufferatthecostofchoosingthesmallestbitrateor
decreasethebufferlevelbychoosingthelargestbitrate.AswediscussedinSection4,thisassumptionisusedtoeliminateextremeboundary
casesintheanalysis,butSODAempiricallyperformswellevenwhenAssumptionA.1isnotstrictlysatisfied.Usingthisassumption,weshow
theexponentiallydecayingperturbationpropertyholdsforthevideostreamingprobleminTheoremA.1.
TheoremA.1.
UnderAssumptionA.1,theexponentiallydecayingperturbationboundholdswithconstants
1
3(3+⌈𝑥max/𝛿⌉)
|     |     |     | (cid:169) |     |     |     |     |     | (cid:170) |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
|     |     |     | (cid:173) |     |     | 2   |     |     | (cid:174) |     |     |     |
𝜌 = 1−
|     |     |     | (cid:173)    | √︂  |        |           |     |       | (cid:174) |     |     |     |
| --- | --- | --- | ------------ | --- | ------ | --------- | --- | ----- | --------- | --- | --- | --- |
|     |     |     | (cid:173) 1+ | 1+  | max{6𝜔 | (𝜔 +3),4𝑥 | (𝜔  | +8𝛾)} | (cid:174) |     |     |     |
|     |     |     | (cid:173)    |     | min    | min       | max | min   | (cid:174) |     |     |     |
|     |     |     |              |     |        | 𝜔3        | 𝜖𝛽  |       |           |     |     |     |
|     |     |     | (cid:171)    |     |        | min       |     |       | (cid:172) |     |     |     |
and
|     |     |     |      | (cid:16) 3𝛽𝜔3 |         |          |     |        |          | (cid:17) |     |     |
| --- | --- | --- | ---- | ------------- | ------- | -------- | --- | ------ | -------- | -------- | --- | --- |
|     |     |     | (1+𝜔 | )             | +max{6𝜔 |          | (𝜔  | +3),4𝑥 | (𝜔 +8𝛾)} |          |     |     |
|     |     |     |      | max           | min     | min      | min |        | max min  |          |     |     |
|     |     |     | 𝐶 =  |               |         |          |     |        |          | .        |     |     |
|     |     |     |      |               |         | 𝜔3 𝜌3+⌈𝑥 | /𝛿⌉ |        |          |          |     |     |
|     |     |     |      |               |         | min      | max |        |          |          |     |     |
Whiletheexponentiallydecayingproperty(DefinitionA.1)boundstheimpactofparameterperturbationsonthestates,weextendthe
definitiontothecontrolactionsandshowthatthisvariantholdsasacorollaryofTheoremA.1.
628

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
(𝑥3,𝑢3)
(𝑥2,𝑢2)
(𝑥1,𝑢1)
|     | (𝑥0,𝑢0) |     | (𝑥 ∗,𝑢 | ∗)  |     | (𝑥 ∗,𝑢 | ∗)  |     | (𝑥 ∗,𝑢 | ∗)  |     | (𝑥 ∗,𝑢 ∗) |     |
| --- | ------- | --- | ------ | --- | --- | ------ | --- | --- | ------ | --- | --- | --------- | --- |
|     |         |     | 1      | 1   |     | 2 2    |     |     | 3      | 3   |     | 4 4       |     |
Figure14:Illustrationoftheaggregationsofper-steperrors.Inthefigure,{(𝑥 ∗,𝑢 ∗)}𝑡=1,2,...denotestheofflineoptimalstates
𝑡 𝑡
andcontrolactions,and{(𝑥 𝑡 ,𝑢 𝑡)}𝑡=1,2,...denotesthebufferlevelachievedbySODA.Thedashedtrajectoryfrom(𝑥 𝑡 ,𝑢 𝑡)denotes
theclairvoyantoptimaltrajectoryfrom(𝑥 𝑡 ,𝑢 𝑡).Attime𝑡,theper-steperror𝑒 𝑡 leadstothedeviationoftheactualtrajectoryof
SODAwiththeclairvoyantoptimaltrajectory.Theimpactoftheper-steperror𝑒1atafuturetimestep𝑡 istheheightofblue
area,whichdecaysexponentiallyfastwithrespectto𝑡
whenexponentiallydecayingperturbationholds.Therefore,althougha
per-steperroroccursateverytimestep,thedistancebetween(𝑥 ,𝑢 𝑡)and(𝑥 ∗,𝑢 ∗)isstilluniformlybounded.
|     |     |     |     |     |     |     |     | 𝑡   | 𝑡   | 𝑡   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UnderAssumptionA.1,forthecontrolaction𝑢,wealsohavethat
CorollaryA.2.
|     | (cid:12)     |           |         |          |     |            |      |           | (cid:12)          |     |     |     |     |
| --- | ------------ | --------- | ------- | -------- | --- | ---------- | ---- | --------- | ----------------- | --- | --- | --- | --- |
|     | (cid:12) 𝑡+𝑝 | (cid:0)(𝜎 |         | (cid:1)  | 𝑡+𝑝 | (cid:16) ′ | ′    | ′         | (cid:17) (cid:12) |     |     |     |     |
|     | (cid:12) 𝜓   | 𝑡−1,𝜈     | 𝑡−1);𝜔ˆ | 𝑡:𝑡+𝑝 ;0 | −𝜓  | (𝜎 ,𝜈      | );𝜔ˆ | 𝑡 :𝑡+𝑝 ;0 | (cid:12)          |     |     |     |     |
|     | (cid:12) 𝑡   |           |         | 𝑢𝜏       | 𝑡   | 𝑡 −1       | 𝑡 −1 |           | 𝑢𝜏 (cid:12)       |     |     |     |     |
𝑡+𝑝
|     |                          |          |     |                           |      |                       |        | (cid:12)   | (cid:12)   |     |     |     |     |
| --- | ------------------------ | -------- | --- | ------------------------- | ---- | --------------------- | ------ | ---------- | ---------- | --- | --- | --- | --- |
|     | ≤𝐶′𝜌𝜏−𝑡+1(cid:0)(cid:12) | 𝜎 𝑡−1−𝜎  | ′   | (cid:12) (cid:12) 𝜈 𝑡−1−𝜈 | ′    | (cid:12) (cid:1)+𝐶′∑︁ | 𝜌|𝜏−𝑗| | 𝜔ˆ −𝜔ˆ′    | ,          |     |     |     |     |
|     |                          | (cid:12) | 𝑡   | −1 (cid:12)+ (cid:12)     | 𝑡 −1 | (cid:12)              |        | (cid:12) 𝑗 | 𝑗 (cid:12) |     |     |     |     |
|     |                          |          |     |                           |      |                       |        | (cid:12)   | (cid:12)   |     |     |     |     |
𝑗=𝑡
|     | (cid:12)        |                 |         |           |                  |     | (cid:16) |        |           |          | (cid:17) | (cid:12)    |     |
| --- | --------------- | --------------- | ------- | --------- | ---------------- | --- | -------- | ------ | --------- | -------- | -------- | ----------- | --- |
|     | (cid:12) 𝜓˜ 𝑡+𝑝 | (cid:0)(𝜎 𝑡−1,𝜈 | 𝑡−1);𝜔ˆ | ;(𝜎       | ,𝜈 𝑡+𝑝+1)(cid:1) | −𝜓  | 𝑡+𝑝 (𝜎   | ′ ,𝜈 ′ | );𝜔ˆ ′    | ;(𝜎 ′ ,𝜈 | ′        | (cid:12)    |     |
|     | (cid:12) 𝑡      |                 |         | 𝑡:𝑡+𝑝 𝑡+𝑝 |                  | 𝑢𝜏  | 𝑡        | 𝑡 −1 𝑡 | −1 𝑡 :𝑡+𝑝 | 𝑡 +𝑝     | 𝑡 +𝑝+1 ) | (cid:12)    |     |
|     | (cid:12)        |                 |         |           |                  |     |          |        |           |          |          | 𝑢𝜏 (cid:12) |     |
𝑡+𝑝
|     |     |     |     |     |     | (cid:1)+𝐶′∑︁ |     | (cid:12) | (cid:12) | (cid:16)(cid:12) |     | (cid:12) (cid:12) | (cid:12) (cid:17) |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | -------- | ---------------- | --- | ----------------- | ----------------- |
≤𝐶′𝜌𝜏−𝑡+1(cid:0)(cid:12) 𝜎 𝑡−1−𝜎 ′ (cid:12) (cid:12)+ (cid:12) 𝜈 𝑡−1−𝜈 ′ (cid:12) 𝜌|𝜏−𝑗| (cid:12) 𝜔ˆ −𝜔ˆ′ (cid:12) +𝐶′𝜌𝑡+𝑝−𝜏 (cid:12) 𝜎 −𝜎 ′ (cid:12) + (cid:12) 𝜈 𝑡+𝑝+1−𝜈 ′ (cid:12) ,
(cid:12) 𝑡 −1 (cid:12) 𝑡 −1 (cid:12) (cid:12) 𝑗 𝑗 (cid:12) (cid:12) 𝑡+𝑝 𝑡 +𝑝 (cid:12) (cid:12) 𝑡 +𝑝+1 (cid:12)
𝑗=𝑡
wherethedecayfactor𝜌isthesameasTheoremA.1,andtheconstant𝐶′isgivenby
|     |     |     |     |     |     |     | 𝐶(1+𝜌)𝑟 |     | +𝜌  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 𝐶′  |         | min | .   |     |     |     |     |
=
|     |     |     |     |     |     |     | 𝜔   | 𝑟 𝜌 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | min | min |     |     |     |     |     |
Here,𝐶isthesameasTheoremA.1.
Toestablishtheexponentiallydecayingperturbationproperty,wefirstreducethevideostreamingproblemtoamoregeneralonline
optimizationproblemwithmemoryandinequalityconstraints.Then,weconsidereachpossiblecombinationofactiveinequalityconstraints
separatelyandshowthattheexponentiallydecayingperturbationpropertyholdsineachcase.Thisonlyrequiresconsideringoptimization
problemswithequalityconstraintswithsecond-orderdifferentiableobjectives.Lastly,weshowthattheexponentialdecaypropertiesfor
theseseparatecasescanbecombinedtoestablishtheexponentialdecaypropertyfortheoriginalvideostreamingproblem.
A.3 ProofOutlineforExactPredictions
WeprovidetheformalversionofTheorem4.1thatgivesthedynamicregretandcompetitiveratioforSODAwithspecificcoefficientsin
TheoremA.3.
TheoremA.3. UnderAssumptionA.1,considerSODAwiththeterminalconstraints𝑥 𝑡+𝐾−1=𝑥¯,𝑟 𝑡+𝐾−1=𝜔ˆ 𝑡+𝐾−1|𝑡−1.Definetheweight𝐶
tobethesameasTheoremA.1,andthecoefficient𝐶′isgivenbyCorollaryA.2.Supposeallpredictionsareexact(i.e.,
andthedecayfactor𝜌
| 𝜔ˆ 𝑚|𝑛−1=𝜔 | 𝑚 for𝑚=𝑛,...,𝑛+𝐾−1)andthepredictionhorizon𝐾 |     |     |      |             |                          | satisfies |          |                    |                   |        |     |     |
| ---------- | ------------------------------------------- | --- | --- | ---- | ----------- | ------------------------ | --------- | -------- | ------------------ | ----------------- | ------ | --- | --- |
|            |                                             |     |     | 1    | (cid:18) 16 | (cid:18) (𝐶+𝐶′)2(cid:19) |           | (cid:16) | 2(cid:17)2(cid:19) | (cid:18)1(cid:19) |        |     |     |
|            |                                             |     |     | 𝐾 ln |             | 1+                       |           | 𝐶2 +(𝐶′) |                    | /ln               | =𝑂(1). |     |     |
|            |                                             |     |     | ≥    |             | ·                        |           | ·        |                    |                   |        |     |     |
|            |                                             |     |     | 4    | 1−𝜌         | 1−𝜌                      |           |          |                    | 𝜌                 |        |     |     |
Here,thecoefficients𝐶,𝐶′
andthedecayfactor𝜌 aregivenbyTheoremA.1andCorollaryA.2.Then,SODAachievesadynamicregretof
𝐶1𝜌𝐾−1 cost(OPT)=𝑂(𝜌𝐾𝑁)andacompetitiveratioof1+𝐶1𝜌𝐾−1 =1+𝑂(𝜌𝐾).Here,thecoefficient𝐶1isgivenby
|     |     |     |      | (cid:32) |     |      |          | ′)2(cid:19)(cid:16) |     |           | 2      | (cid:33)1/2 |     |
| --- | --- | --- | ---- | -------- | --- | ---- | -------- | ------------------- | --- | --------- | ------ | ----------- | --- |
|     |     |     |      |          |     | 1    | (cid:18) | (𝐶 + 𝐶              |     | 2(cid:17) | 4 + 𝜔  |             |     |
|     |     |     | 𝐶1=8 | 2(4𝛾+𝛽+𝜔 |     | )·   | · 1+     |                     | 𝐶2  | +(𝐶′) ·   | m in   | .           |     |
|     |     |     |      |          | max | 1− 𝜌 |          | 1 − 𝜌               |     |           | 𝜖 𝛽𝜔 2 |             |     |
min
| andthenotation𝑂(·)hidespolynomialdependenceonsystemparameters𝜖,𝛽,𝛾 |     |     |     |     |     |     |     |     | and𝑑. |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
629

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
TheproofoutlineofTheoremA.3containstwoparts:(1)Boundingtheper-steperrorof SODAateachtimestepwhencomparedagainst
thehindsightoptimalpolicy;(2)Showingthatthepastper-stepdoesnotaccumulatetobeunboundedovertime.
BoundingthePer-steperror.Weintroducetheconceptofper-steperrortocharacterizethedecisionerrorof SODAateachtimestepdue
toitslimitedpredictionpower.Whilethepredictionpowerof SODAislimitedbecauseitonlyhasexactpredictionsoffuturebandwidths
withinafinitehorizon𝐾,theideaofper-steperroralsoextendstoinexactpredictions(SectionA.4).Weprovidetheformaldefinitionofthe
per-steperrorinDefinitionA.2.
|     |     |     | SODAattimestep𝑡 |     |     | (denotedas𝑒 |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
DefinitionA.2. Theper-steperrorof 𝑡)isdefinedasthesumofthedifferencebetweentheactualstate/action
|        | SODA(𝑥 ,𝑢 𝑡)andtheclairvoyantoptimalnextstatefrom(𝑥 |     |                        |     |              |     | 𝑡−1,𝑢                       |     |                  |     |                |     |
| ------ | --------------------------------------------------- | --- | ---------------------- | --- | ------------ | --- | --------------------------- | --- | ---------------- | --- | -------------- | --- |
| pairof | 𝑡                                                   |     |                        |     |              |     | 𝑡−1),i.e.,                  |     |                  |     |                |     |
|        |                                                     |     | (cid:12)               | 𝑁   |              |     | (cid:12) (cid:12)           | 𝑁   |                  |     | (cid:12)       |     |
|        |                                                     | 𝑒   | (cid:66) (cid:12) 𝑥 −𝜓 | ((𝑥 | 𝑡−1,𝑢 𝑡−1);𝜔 |     | ;0)𝑥𝑡 (cid:12) + (cid:12) 𝑢 | −𝜓  | ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 |     | ;0)𝑢𝑡 (cid:12) |     |
|        |                                                     | 𝑡   | (cid:12) 𝑡             | 𝑡   |              | 𝑡:𝑁 | (cid:12) (cid:12)           | 𝑡 𝑡 |                  | 𝑡:𝑁 | (cid:12)       |     |
Intuitively,startingfromthestate/actionpair(𝑥 𝑡−1,𝑢 𝑡−1),wecomparetheactualnextstate/actionpair(𝑥 𝑡 ,𝑢 𝑡)ofSODAwiththeclairvoyant
optimalnextstate/actionacontrollerwouldtakeifithadtheexactpredictionsofallfuturebandwidthsaftertimestep𝑡.Wedefinethe
| magnitudeofthisdifferenceastheper-steperrorof |     |     |     |     | SODA. |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Whenthepredictionsoffuturebandwidthsareexact,weleveragetheexponentiallydecayingperturbationpropertytoboundtheper-step
errorof SODAinLemmaA.4.WedefertheproofofLemmaA.4toSectionC.1.
LemmaA.4. Whenthepredictionsforthefuturebandwidthareexact,theper-steperrorof SODAsatisfies
2
≤16𝜌4𝐾−2(cid:16) 2(cid:17)2(cid:16)(cid:12) 2(cid:17) +8𝜌2𝐾−2(cid:16) 2(cid:17) (2+𝜔 )𝑏(𝑥 ∗ )+2𝑏(𝑥 ∗ )
𝑒 2 𝐶2 +(𝐶′) 𝑥 𝑡−1−𝑥 ∗ (cid:12) 2 + (cid:12) 𝑢 𝑡−1−𝑢 ∗ (cid:12) 𝐶2 +(𝐶′) m in 𝑡 + 𝐾 −1 𝑡 +𝐾−2 .
|     | 𝑡   |     | (cid:12) | 𝑡 −1 | (cid:12) (cid:12) | 𝑡   | −1 (cid:12) |     |     |     | 2   |     |
| --- | --- | --- | -------- | ---- | ----------------- | --- | ----------- | --- | --- | --- | --- | --- |
𝜖 𝜔
min
Theexponentiallydecayingcoefficients𝜌4𝐾−2and𝜌2𝐾−2suggestthattheper-steperrorimprovesexponentiallyfastastheprediction
horizon𝐾grows.Althoughonecansimplifytheexpressionbyboundingtheterms(cid:12) (cid:12) 2 ,(cid:12) (cid:12) 2
|     |     |     |     |     |     |     |     | (cid:12) | 𝑥 𝑡−1−𝑥 ∗ | (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 | ∗ (cid:12) ,𝑏(𝑥 ∗ ),and𝑏(𝑥 | ∗ )    |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------------------- | -------------------------- | ------ |
|     |     |     |     |     |     |     |     |          | 𝑡         | −1                        | 𝑡 −1 𝑡 +𝐾−1                | 𝑡 +𝐾−2 |
withsomeuniformconstants,wekeepthesetermsbecausethecarefultreatmentisrequiredtoshowthecompetitiveratioresult.
Boundingtheaccumulationofpasterrors.Besidesboundingtheper-steperrors,anotherimportantconsequenceoftheexponentially
decayingperturbationboundsisthatitguaranteestheimpactofapreviousper-steperrordecaysquicklyovertime.Therefore,whenwe
boundthetotaldifferencebetweenSODA’strajectory{(𝑥 ,𝑢 𝑁 andtheofflineoptimaltrajectory{(𝑥 ∗,𝑢 ∗)} 𝑁 ,theaggregatedcontribution
|     |     |     |     |     | 𝑡   | 𝑡)} 𝑡 =1 |     |     |     | 𝑡   | 𝑡 𝑡 =1 |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------ | --- |
ofanyper-steperrorterm𝑒 𝜏 isuptoaconstantfactorthatdependsonthedecayfactorratherthangrowinglinearlywithrespecttothe
totalhorizonlength𝑁 (seeFigure14foranillustration).WestatethisresultformallyinLemmaA.5anddeferitsprooftoSectionC.2.
|           |                 | SODA{(𝑥 |     | ,𝑢 𝑡)} 𝑁          |                          |              |      |             |                 |      |     |     |
| --------- | --------------- | ------- | --- | ----------------- | ------------------------ | ------------ | ---- | ----------- | --------------- | ---- | --- | --- |
| LemmaA.5. | Thetrajectoryof |         | 𝑡   | 𝑡 =1satisfiesthat |                          |              |      |             |                 |      |     |     |
|           |                 |         | 𝑁   |                   |                          |              |      |             |                 | 𝑁    |     |     |
|           |                 |         | ∑︁  | (cid:16)(cid:12)  |                          | 2(cid:17)    | 1    | (cid:18) (𝐶 | + 𝐶 ′)2(cid:19) | ∑︁   |     |     |
|           |                 |         |     | 𝑥 −𝑥              | ∗(cid:12) 2 + (cid:12) 𝑢 | −𝑢 ∗(cid:12) | ≤    | · 1+        |                 | 𝑒 2, |     |     |
|           |                 |         |     | (cid:12) 𝑡        | 𝑡 (cid:12) (cid:12)      | 𝑡 𝑡 (cid:12) | 1− 𝜌 |             | 1 𝜌             | 𝑡    |     |     |
−
|          |                                                 |     | 𝑡=1 |     |     |     |     |     |     | 𝑡=1 |     |     |
| -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| where{(𝑥 | ∗,𝑢 ∗)} 𝑁 =1denotestheofflineoptimaltrajectory. |     |     |     |     |     |     |     |     |     |     |     |
|          | 𝑡 𝑡 𝑡                                           |     |     |     |     |     |     |     |     |     |     |     |
BycombiningLemmaA.4andLemmaA.5,weboundthetotalsquareddistancebetweenSODA’strajectoryandtheofflineoptimal
trajectorybyapartoftheofflineoptimalcosttimesacoefficientoftheorder𝑂(𝜌2𝐾).Sincethecostfunctionsforadaptivevideostreaming
arewell-conditioned,wecanconverttheboundonthetotalsquareddistancebetweenthetwotrajectoriesintothecompetitiveratiobound
andthedynamicregretboundtofinishtheproofofTheoremA.3.
A.4 ProofOutlineforInexactPredictions
Comparedwiththecasewhenallpredictionsareexact,amajorchallengewhenthepredictionsareinexactisthatoneofSODA’sdecisions
maycausethenextstatetoviolatethestateconstraint.Inthissection,weshowintwostepsthatSODA’sdecisiontrajectorywillnotviolate
thestateconstraints.First,byincreasingthecoefficient𝛽 ofthebuffercost,onecanguaranteethattheofflineoptimaltrajectorystays
arbitrarilyclosetotheofflineoptimaltrajectory(seeLemmaA.6).Then,weshowaboundontheper-steperror(DefinitionA.2)which
dependsonthepredictionerror(seeLemmaA.7).Recallthattheexponentiallydecayingperturbationboundsallowustoboundthedistance
betweentheSODAandtheofflineoptimaltrajectories.Therefore,wecancombinetheseresultstoshowthatundersomemildassumptions
onthecoefficient𝛽andthepredictionerrors,SODAwillnotviolateanyconstraints,andmoreover,italsosatisfiesadynamicregretbound
(seeTheoremA.8).
Wefirstshowthatforany𝜁 >0,onecanselectthecoefficient𝛽tobesufficientlylargesothattheofflineoptimaltrajectorystayswithin
amarginof𝜁 aroundthetargetbufferlevel𝑥¯.WestatethisresultformallyinLemmaA.6anddeferitsprooftoSectionD.1.
LemmaA.6. Suppose𝜁 ≤min{𝑥¯,𝑥 −𝑥¯}ispositivenumberand𝑥0 ≤𝑥¯+𝜁,ifthecoefficient𝛽forthebuffercostissufficientlylargesuch
max
that
|                                            |     |     |     |                                      | 1   | (cid:18) | 4𝛾 (cid:19) (cid:18) | 1       | 1 (cid:19) |     |     |     |
| ------------------------------------------ | --- | --- | --- | ------------------------------------ | --- | -------- | -------------------- | ------- | ---------- | --- | --- | --- |
|                                            |     |     |     |                                      | 𝛽 ≥ | · 1+     | ·                    | −       | .          |     |     |     |
|                                            |     |     |     |                                      | 𝜖𝜁  |          | 𝜔 𝑟                  | 𝑟       |            |     |     |     |
|                                            |     |     |     |                                      |     |          | min                  | min max |            |     |     |     |
| Then,theofflineoptimaltrajectorysatisfies𝑥 |     |     |     | ∗ ∈ [𝑥¯−𝜁,𝑥¯+𝜁]holdsforalltimestep𝑡. |     |          |                      |         |            |     |     |     |
𝑡
630

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
Intuitively,LemmaA.6holdsbecauseincreasing𝛽makesstayingclosetothetargetbufferlevelmoreimportant.Intheextremecasethat
𝛽tendsto+∞,theofflineoptimalwillignorethedistortion/switchingcostandselectactionssothatthebufferlevelalwaysequalto𝑥¯.
Recallthattheper-steperrorof SODAisdefinedinDefinitionA.2.Weboundtheper-steperrorinLemmaA.7anddeferitsproofto
SectionD.2.
LemmaA.7. Whenthepredictionsforthefuturebandwidthareinexact,theper-steperrorof SODAsatisfies
𝑒 𝑡 ≤ (𝐶+𝐶′)𝜌𝐾 (cid:18) 𝑥 max + 𝑟 1 − 𝑟 1 (cid:19) +(𝐶+𝐶′)·𝐸(𝑡−1,𝐾)+ (cid:12) (cid:12) 𝜔 𝑡 − 𝑟 𝜔ˆ 𝑡|𝑡−1 (cid:12) (cid:12) ,
min max min
where𝐸(𝑡−1,𝐾) (cid:66)(cid:205) 𝜏 𝑡+ = 𝐾 𝑡 −1𝜌𝜏−𝑡(cid:12) (cid:12) 𝜔ˆ 𝜏|𝑡−1−𝜔 𝜏 (cid:12) (cid:12).
SimilartotheproofoutlinefortheexactpredictioncaseinSectionA.3,wecanapplyLemmaA.5toboundtheaccumulationofpasterrors.
WiththehelpofLemmaA.6andLemmaA.7,weshowourmainresultforSODAwhenthepredictionsofthefuturebandwidthsareinexact
inTheoremA.8.WedefertheproofofTheoremA.8toSectionD.3.
TheoremA.8. UnderAssumptionA.1,considerSODAwiththeterminalconstraints𝑥 𝑡+𝐾−1=𝑥¯,𝑟 𝑡+𝐾−1=𝜔ˆ 𝑡+𝐾−1|𝑡−1.Let𝐷 (cid:66)min{𝑥¯,𝑥
max
−
𝑥¯}.Supposetheweight𝛽,thepredictionhorizon𝐾,andthepredictionerrorssatisfythat
3 (cid:18) 4𝛾 (cid:19) (cid:18) 1 1 (cid:19)
𝛽 ≥ · 1+ · − , and
𝜖𝐷 𝜔 𝑟 𝑟
min min max
𝐸(𝑡,𝐾)+𝜌𝐾 ≤
(1−𝜌)𝐷
,
3𝐶(1+𝐶+𝐶′) (cid:16) 1+𝑥 + 1 − 1 (cid:17)
max 𝑟 𝑟
min max
where,recall,𝐸(𝑡,𝐾)=(cid:205)
𝜏
𝑡+
=
𝐾
𝑡+1
𝜌𝜏−𝑡−1(cid:12)
(cid:12)
𝜔ˆ
𝜏|𝑡
−𝜔
𝜏
(cid:12)
(cid:12)
.Then,thebufferlevelsintheSODA’sdecisiontrajectoryneverhitstheconstraintboundary,
i.e.,0<𝑥
𝑡
<𝑥 maxfor𝑡 =1,...,𝑁.Further,SODAachievesadynamicregretof
2 (cid:16) 1+ 1 +𝐶+𝐶′ (cid:17)2(cid:16) 1+𝑥 + 1 − 1 (cid:17)
𝑟 min
(1−𝜌)3/2
max 𝑟 min 𝑟 max · √︁4𝛾+𝛽+𝜔
max
· √︁ E·cost(OPT)+
(cid:16) 1+ 1 +𝐶+𝐶′ (cid:17)4(cid:16) 1+𝑥 + 1 − 1 (cid:17)2 (4𝛾+𝛽+𝜔 )
𝑟 max 𝑟 𝑟 max
min min max ·E,
(1−𝜌)3
whereE =𝜌2𝐾𝑁 +(cid:205) 𝜅 𝐾 =1 𝜌𝜅𝐸 𝜅.Here𝐸 𝜅 (cid:66)(cid:205) 𝑡 𝑁 =1 (cid:12) (cid:12) 𝜔ˆ 𝑡+𝜅|𝑡 −𝜔 𝑡+𝜅 (cid:12) (cid:12) 2 .
√
NotethatthedynamicregretboundshowninTheoremA.8isintheorderof𝑂( E𝑁 +E),sincecost(OPT)=𝑂(𝑁).Intuitively,fromthe
formof𝐸 𝑡(𝐾),weseethatpredictingthefuturebandwidth𝜔
𝜏
accuratelyattimestep𝑡 becomeslessimportantas(𝜏−𝑡)increases.
A.5 ProofOutlineforEfficientStructure
Inthissection,weshowthatoptimalsolutionofthefinite-timeoptimalcontrolproblemsolvedbySODAcanbeapproximatedwellbya
monotonicsequenceofbitrateswhenthecoefficient𝛾 oftheswitchingcostissufficientlylarge(seeTheoremA.9).Althoughthisresultis
shownforthecontinuousvariablecase,italsoprovidessomeinsightastowhytheefficientapproximatesolverinAlgorithm1canprovide
identicaldecisionstothebrute-forcesolverwithrelativelyhighprobabilities,asshowninFigure8.
TheoremA.9. Let𝜔ˆ ×𝐾 denotethesequence{𝜔ˆ,...,𝜔ˆ}withlength𝐾.Forany𝜆>0,whenthecoefficient𝛾 issufficientlylargesuchthat
𝐾2 (cid:32) (cid:32) 1 1 (cid:33) (cid:33)
𝛾 ≥ 𝜔ˆ − +𝛽max{𝑥¯2,𝜖(𝑥 −𝑥¯) 2 } ,
𝜆2 𝑟2 𝑟2 max
min max
wehavethatthefollowinginequalityholdsforall𝜏 ∈{𝑡,𝑡+1,...,𝑡+𝐾−1}:
(cid:12) (cid:12) (cid:12) 𝜓ˆ 𝑡 𝑡+𝐾−1 ((𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ ×𝐾 ;0)𝑢𝜏 −𝜙ˆ 𝑡 𝑡+𝐾−1 ((𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0)𝑢𝜏 (cid:12) (cid:12) (cid:12) ≤𝜆.
Notethat𝜙ˆ 𝑡 𝑡+𝐾−1((𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0)𝑢𝜏 ismonotonicbyLemmaA.10.
WedefertheformalproofofTheoremA.9toSectionE.2.ThetheoreticalinsightprovidedbyTheoremA.9alignswithourempiricalresult
inFigure8.Specifically,ifweincreasethecoefficient𝛾 whilekeepingthepredictionhorizon𝐾 fixed,thedecisionmadebytheefficient
monotonicapproximationapproach(Algorithm1)ismorelikelytobeidenticalwiththebrute-forcesolver.Ontheotherhand,ifweincrease
𝐾 andfix𝛾,itismorechallengingforAlgorithm1tomatchthedecisionofthebrute-forcesolver.
ToshowTheoremA.9,wefirstconsiderasettingwheretheobjectivefunctiononlycontainstheswitchingcostterms(i.e.,thedistortion
costandthebuffercostareremoved.)Thiscanbeviewedastheextremecasewhen𝛾 tendsto+∞sothatboth𝛼and𝛽arenegligible.Inthis
scenario,weshowtheoptimalsequenceoftheinversebitratesismonotonic.WestatethisresultformallyinLemmaA.10anddeferitsproof
toSectionE.1.
631

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
LemmaA.10. UnderthesameassumptionasTheoremA.9,considertheoptimalsolutiontotheoptimizationproblem
𝑡+𝐾−1
|     |     | 𝜙ˆ    |     |                  |                |          | ∑︁         |             |                        |                      |     |     |
| --- | --- | ----- | --- | ---------------- | -------------- | -------- | ---------- | ----------- | ---------------------- | -------------------- | --- | --- |
|     |     | 𝑡+𝐾−1 | ((𝜎 | 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0) | (cid:66)argmin |          | 𝛾·(𝑢       | −𝑢          | 𝑡−1) 2                 |                      |     |     |
|     |     | 𝑡     |     |                  |                |          |            | 𝑡           |                        |                      |     |     |
|     |     |       |     |                  |                | 𝑢𝑡:𝑡+𝐾−1 | 𝜏=𝑡        |             |                        |                      |     |     |
|     |     |       |     |                  |                | s.t.𝑥    | =𝑥 𝜏−1+𝜔ˆ𝑢 |             | −1, for𝜏 =𝑡,...,𝑡+𝐾−1, |                      |     |     |
|     |     |       |     |                  |                |          | 𝜏          | 𝜏           |                        |                      |     |     |
|     |     |       |     |                  |                |          |            |             | (cid:20) 1 1           | (cid:21)             |     |     |
|     |     |       |     |                  |                |          | 𝑥 [0,𝑥     | ],𝑢         | ,                      | , for𝜏 =𝑡,...,𝑡+𝐾−1, |     |     |
|     |     |       |     |                  |                |          | 𝜏 ∈        | max         | 𝜏 ∈                    |                      |     |     |
|     |     |       |     |                  |                |          |            |             | 𝑟 max 𝑟 min            |                      |     |     |
|     |     |       |     |                  |                |          | 𝑥 𝑡−1=𝜎    | 𝑡−1,𝑢 𝑡−1=𝜈 | 𝑡−1.                   |                      |     | (6) |
𝑡−1,𝜙ˆ 𝑡+𝐾−1((𝜎
Thesolutionsatisfiesthat:If𝜈 𝑡−1 >1/𝜔ˆ,thenthesequence𝜈 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0)ismonotonicallydecreasing;If𝜈 𝑡−1 <1/𝜔ˆ,then
𝑡
thesequence𝜈 𝑡−1,𝜙ˆ 𝑡+𝐾−1((𝜎 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0)ismonotonicallyincreasing;If𝜈 =1/𝜔ˆ,theoptimalsolutionis𝑢 =𝑢 =···=𝑢 =
|     |     | 𝑡   |     |     |     |     |     |     | 𝑡−1 |     | 𝑡 𝑡+1 | 𝑡+𝐾−1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- |
𝜈 𝑡−1=1/𝜔ˆ.
ThekeyobservationthatallowsustogeneralizeLemmaA.10tothecasewherethedistortion/buffercostsarenon-negligibleisthe
following:Ifwechangethevariableof (6)to𝑎 =𝑢 −𝑢 ,whichdenotestheincrementsofthecontrolactions,theobjectiveof (6)isa
|     |     |     |     |     | 𝑡   | 𝑡 𝑡−1 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
𝛾-stronglyconvexfunctionof(𝑎 ,...,𝑎 𝑡+𝐾−1).Anydeviationfromtheoptimalsolutionof(6)willcausealossonthetotalswitchingcosts
𝑡
thatgrowswith𝛾.When𝛾 issufficientlylarge,afeasiblesolutioncannotuseitsgainonthedistortion/buffercoststocancelthelossonthe
| totalswitchingcostifitdeviatestoomuchfromtheoptimalsolutionof |     |     |     |     |     |     |     | (6). |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
B PROOFSOFTHEEXPONENTIALLYDECAYINGPERTURBATIONBOUNDS
Inthissection,weestablishthecriticalexponentiallydecayingperturbationbounds(DefinitionA.1).Insteadofjustfocusingonthevideo
streamingapplicationitself,weestablishtheperturbationboundforamoregeneralSOCOwithmemoryframework.
Specifically,weconsiderthefollowingfinite-timeoptimalcontrolproblemwithmemory𝐻.
|     |     |     |     |               |     |        | 𝑝   |        | 𝑝+𝐻−1     |         |     |      |
| --- | --- | --- | --- | ------------- | --- | ------ | --- | ------ | --------- | ------- | --- | ---- |
|     |     |     |     |               |     |        | ∑︁  |        | ∑︁        |         |     |      |
|     |     |     |     | 𝜓(𝑦,𝑧;𝜇,𝑤,𝛿)= |     | argmin | 𝑓   | 𝑡(𝑥 ;𝜇 | 𝑡)+ 𝑐 𝑡(𝑥 | ;𝑤 𝑡)   |     | (7a) |
|     |     |     |     |               |     |        |     | 𝑡      |           | 𝑡:𝑡−𝐻+1 |     |      |
𝑥
|     |     |     |     |     |     | −𝐻+1:𝑝+𝐻−1𝑡=0 |               |          | 𝑡=0          |     |     |      |
| --- | --- | --- | --- | --- | --- | ------------- | ------------- | -------- | ------------ | --- | --- | ---- |
|     |     |     |     |     |     |               | s.t.𝑥 𝑡 ∈     | [0,𝑥max] | ⊆R,∀0≤𝑡      | ≤𝑝, |     | (7b) |
|     |     |     |     |     |     |               | 𝑥 −𝑥          | ≥−𝛿      | ,∀0≤𝑡 ≤𝑝+1,  |     |     | (7c) |
|     |     |     |     |     |     |               | 𝑡             | 𝑡−1      | 𝑡            |     |     |      |
|     |     |     |     |     |     |               | 𝑥 −𝐻+1:−1=𝑦,𝑥 |          | 𝑝+1:𝑝+𝐻−1=𝑧, |     |     | (7d) |
[0,𝑥max]𝐻−1,𝜇 [0,𝑥max]𝑝+1,𝑤 W𝑝+𝐻,𝛿 Δ𝑝+2.Here,theobjectivefunction(7a)containsthehittingcosts𝑓
| where𝑦,𝑧 | ∈   |     | ∈   |     | ∈   |     | ∈   |     |     |     |     | 𝑡(𝑥 𝑡 ;𝜇 𝑡) |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
(parameterizedby𝜇 𝑡 )andtheswitchingcosts𝑐 𝑡(𝑥 ;𝑤 𝑡)(parameterizedby𝑤 𝑡 ).Fortheconstraints,(7b)imposesaboxconstraint
𝑡:𝑡−𝐻+1
oneachdecisionvariable𝑥 ;(7c)imposesaconstraintonhowmuch𝑥 candecreaseateachtimestep;and(7d)specifiestheboundary
|     |     |     | 𝑡   |     |     |     |     | 𝑡   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conditionsoftheoptimizationproblem.
Inthespecialcaseofvideostreaming,thedecisionisonthebufferlevel𝑥 .Giventhebufferlevels,theinverseofthebitrate𝑢 (cid:66)1/𝑟 is
|     |     |     |     |     |     |     |     |     | 𝑡   |     |     | 𝑡 𝑡 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
uniquelydecidedbytheequation
|     |     |     |     |     |     | 𝑢   | =(𝑥 −𝑥 | 𝑡−1+1)/𝜔 | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 𝑡 𝑡    |          | 𝑡   |     |     |     |
where𝜔 denotesthebandwidth.Thememorylength𝐻 =3.Forthehittingcost,wehave𝜇 ≡𝑥¯,and
|                             | 𝑡   |     |     |        |         |           |                    |     |            | 𝑡   |     |     |
| --------------------------- | --- | --- | --- | ------ | ------- | --------- | ------------------ | --- | ---------- | --- | --- | --- |
|                             |     |     |     |        |         |           | (cid:40) 𝛽(𝑥−𝑥¯)2, |     | if𝑥 ≤𝑥¯,   |     |     |     |
|                             |     |     |     |        | 𝑓 𝑡(𝑥;𝜇 | 𝑡)=𝛽𝑏(𝑥)= |                    |     |            |     |     |     |
|                             |     |     |     |        |         |           | 𝜖𝛽(𝑥−𝑥¯)2,         |     | otherwise. |     |     |     |
| Fortheswitchingcost,wehave𝑤 |     |     |     | =(𝜔 ,𝜔 | 𝑡−1)and |           |                    |     |            |     |     |     |
𝑡 𝑡
|     |     |     |           |             | 2    |           | 2   |     |     |     |     |     |
| --- | --- | --- | --------- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
|     |     | 𝑐   | 𝑡(𝑥 𝑡:𝑡−2 | ;𝑤 𝑡)=𝜔 𝑡 𝑢 | +𝛾(𝑢 | 𝑡 −𝑢 𝑡−1) |     |     |     |     |     |     |
𝑡
2
|     |     |     |     | (𝑥 𝑡 | −𝑥 𝑡−1+1)2 |     | (𝜔 𝑡−1𝑥 𝑡 | +𝜔 𝑡 𝑥 | 𝑡−2−(𝜔 𝑡 +𝜔 | 𝑡−1)𝑥 𝑡−1+(𝜔 𝑡−1−𝜔 | 𝑡)) |     |
| --- | --- | --- | --- | ---- | ---------- | --- | --------- | ------ | ----------- | ------------------ | --- | --- |
|     |     |     |     | =    |            | +𝛾  |           |        |             |                    | .   |     |
|     |     |     |     |      | 𝜔          |     |           |        | 𝜔 2𝜔 2      |                    |     |     |
|     |     |     |     |      | 𝑡          |     |           |        | 𝑡 𝑡         | −1                 |     |     |
Thefirstconstraint𝑥 𝑡 ∈ [0,𝑥max]of (7)matchesthebufferconstraintofthevideostreamingproblemexactly.
T h e se c o nd c on s t r a i n t𝑥 𝑡 − 𝑥 𝑡− 1 ≥ − 𝛿 𝑡 c or re s p o n d s to th e co nstraintthat𝑢 𝑡 ≥ 1 in(3).Thus,whenapplying(7)tovideostreaming,
|           |       |         |            |                |           |       |       |     | 𝑟m ax |     |     |     |
| --------- | ----- | ------- | ---------- | -------------- | --------- | ----- | ----- | --- | ----- | --- | --- | --- |
| we h a ve | 𝛿 1   | 𝜔 𝑡 . B | y A s su m | p tio n A . 1, | w e h a v | e 𝛿 𝛿 | > 0 . |     |       |     |     |     |
|           | 𝑡 = − | 𝑟       |            |                |           | 𝑡 ≥   |       |     |       |     |     |     |
m a x
GiventherelationshipbetweenSOCOwithmemoryproblemandadaptivevideostreamingproblem,weonlyneedtoestablishthe
exponentiallydecayingperturbationboundforthemoregeneralSOCOwithmemoryproblem.Toshowthisperturbationbound,weneed
thefollowingassumptionabouttheobjectivefunctionandconstraints:
Weneedthefollowingassumptionontheoptimizationproblem(7)fortheexponentiallydecayingperturbationpropertyto
AssumptionB.1.
hold:
632

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
1) 𝑓 𝑡(·;𝜇 𝑡):R→Risstronglyconvexforall𝑡and𝜇 ∈ [0,𝑥 ].Wefurtherassumethereexiststwo𝑚 𝑓-stronglyconvexandℓ 𝑓-smoothfunctions
|     |     |     |     |     |     | 𝑡   | max |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (0) | (1) |     |     |     |     |     | (0) |     |     |     |     | (1) |     |
𝑓 (·;𝜇 𝑡),𝑓 (·;𝜇 𝑡) :R→RinC2 suchthat𝑓 𝑡(𝑥 𝑡 ;𝜇 𝑡) = 𝑓 (𝑥 𝑡 ;𝜇 𝑡)for𝑥 𝑡 ∈ [0,𝜇 𝑡]and𝑓 𝑡(𝑥 𝑡) = 𝑓 (𝑥 𝑡 ;𝜇 𝑡)for𝑥 𝑡 ∈ [𝜇 𝑡 ,𝑥 ].We
| 𝑡   | 𝑡   |     |     |     |     |     | 𝑡   |     |     |     |     | 𝑡   | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(𝑗)
| alsoassumethatfor𝑗 |     | =1,2,𝑓 | 𝑡            | satisfiesthatforall𝑥 |               | 𝑡                | ,𝜇 𝑡 ∈ [0,𝑥 | max ],     |                  |       |       |            |     |
| ------------------ | --- | ------ | ------------ | -------------------- | ------------- | ---------------- | ----------- | ---------- | ---------------- | ----- | ----- | ---------- | --- |
|                    |     |        | (cid:13)     |                      | (cid:13)      | (cid:13)         |             | (cid:13)   | (cid:13)         |       |       | (cid:13)   |     |
|                    |     |        |              | 𝑓 (𝑗) (𝑥             | ;𝜇            | 𝑓                | (𝑗) (𝑥 ;𝜇   | ≤𝐿 ,       |                  | 𝑓 (𝑗) | (𝑥 ;𝜇 | ≤ℓ .       |     |
|                    |     |        | (cid:13) ∇𝑥𝑡 | 𝑡                    | 𝑡 𝑡) (cid:13) | + (cid:13) ∇𝜇𝑡 𝑡 | 𝑡 𝑡)        | (cid:13) 𝑓 | and (cid:13) ∇𝜇𝑡 | ∇𝑥𝑡 𝑡 | 𝑡 𝑡)  | (cid:13) 𝜇 |     |
|                    |     |        | (cid:13)     |                      | (cid:13)      | (cid:13)         |             | (cid:13)   | (cid:13)         |       |       | (cid:13)   |     |
𝑐 𝑡(·;𝑤 : R𝐻 Risconvexandℓ 𝑐-smoothforall𝑡 and𝑤 R𝑞 .𝑐 𝑡(·;𝑤 isinC2 [0,𝑥 ]𝐻
| 2)                 | 𝑡) → |                |     |                   |           |               | 𝑡 ∈             | W ⊂               |         | 𝑡)               | on      | max .Wealsoassumethatforall |     |
| ------------------ | ---- | -------------- | --- | ----------------- | --------- | ------------- | --------------- | ----------------- | ------- | ---------------- | ------- | --------------------------- | --- |
| 𝑤 𝑡 ∈Wandfeasible𝑥 |      | 𝑡:𝑡−𝐻+1,wehave |     |                   |           |               |                 |                   |         |                  |         |                             |     |
|                    |      |                |     | (cid:13)          |           |               | (cid:13)        | (cid:13)          |         | (cid:13)         |         |                             |     |
|                    |      |                |     | (cid:13)∇𝑥𝑡:𝑡−𝐻+1 | 𝑐 𝑡(𝑥     | 𝑡:𝑡−𝐻+1       | ;𝑤 𝑡) (cid:13)+ | (cid:13)∇𝑤𝑡 𝑐 𝑡(𝑥 | 𝑡:𝑡−𝐻+1 | ;𝑤 𝑡) (cid:13)≤𝐿 | 𝑐 , and |                             |     |
|                    |      |                |     | (cid:13)          |           |               |                 | (cid:13)          |         |                  |         |                             |     |
|                    |      |                |     | (cid:13)∇𝑤𝑡       | ∇𝑥𝑡:𝑡−𝐻+1 | 𝑐 𝑡(𝑥 𝑡:𝑡−𝐻+1 | ;𝑤              | 𝑡) (cid:13)≤ℓ 𝑤 . |         |                  |         |                             |     |
3) Wehave𝛿 ∈Δholdsforall𝑡,whereΔisaclosedintervalonRandisboundedbelowbysomepositiveconstant𝛿.Denote𝑑 (cid:66) ⌈𝑥 /𝛿⌉.
|     | 𝑡   |     |     |     |     |     |     |     |     |     |     |     | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2(𝜔 in+3),
Inthespecialcaseofthevideostreamingproblem,AssumptionB.1issatisfiedwiththeparameters𝑚 =𝜖𝛽,ℓ =ℓ 𝜇 =𝛽,ℓ 𝑐 = m
|     |     |     |     |     |     |     |     |     |     |     |     | 𝑓 𝑓 | 𝜔 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
min
| ℓ 4𝑥max | (𝜔 min+8𝛾).Inaddition,both𝐿 |     |     | and𝐿 | arebounded. |     |     |     |     |     |     |     |     |
| ------- | --------------------------- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑤 =     | 3                           |     |     | 𝑓    | 𝑐           |     |     |     |     |     |     |     |     |
𝜔
| WestatetheexponentiallydecayingperturbationboundfortheSOCOwithmemoryproblemformallyinTheoremB.1anddeferitsproof | min |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toAppendixB.1.
| TheoremB.1. | UnderAssumptionB.1,if𝑝 |               |     |                     | ≥𝑑,theinequality |          |     |     |       |     |     |     |     |
| ----------- | ---------------------- | ------------- | --- | ------------------- | ---------------- | -------- | --- | --- | ----- | --- | --- | --- | --- |
|             | (cid:13)               | 𝜓(𝑦,𝑧;𝜇,𝑤,𝛿)𝑡 |     | −𝜓(𝑦′,𝑧′;𝜇′,𝑤′,𝛿′)𝑡 |                  | (cid:13) |     |     |       |     |     |     |     |
|             | (cid:13)               |               |     |                     |                  | (cid:13) |     |     |       |     |     |     |     |
|             |                        |               |     |                     |                  | 𝑝        |     |     | 𝑝+𝐻−1 |     |     | 𝑝+1 |     |
|             |                        |               |     |                     |                  | ∑︁       |     |     | ∑︁    |     |     | ∑︁  |     |
≤𝐶(cid:0)𝜌𝑡(cid:13) 𝑦−𝑦′(cid:13) (cid:13)+𝜌𝑝−𝑡(cid:13) 𝑧−𝑧′(cid:13) (cid:1)+𝐶(cid:169) 𝜌|𝑡−𝜏|(cid:12) 𝜇 −𝜇 ′(cid:12) (cid:12)+ 𝜌|𝑡−𝜏|(cid:13) 𝑤 −𝑤 ′(cid:13) (cid:13)+ 𝜌|𝑡−𝜏|(cid:13) 𝛿 −𝛿 ′(cid:13) (cid:13)(cid:170) (8)
(cid:13) (cid:13) (cid:13) (cid:173) (cid:12) 𝜏 𝜏 (cid:13) 𝜏 𝜏 (cid:13) 𝜏 𝜏 (cid:174)
|     |     |     |     |     |     | 𝜏=0       |     |     | 𝜏=0 |     |     | 𝜏=0       |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --------- | --- |
|     |     |     |     |     |     | (cid:171) |     |     |     |     |     | (cid:172) |     |
[𝑥,𝑥]𝐻−1
| holdsforall𝑡 | ∈ [0,𝑝]and𝑦,𝑧 |     | ∈   | .Here, |     |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
𝐻(𝐻+𝑑)
|                       |     |                          |     |     |              |           | 2   |           |     | 2ℓ          |     |     |     |
| --------------------- | --- | ------------------------ | --- | --- | ------------ | --------- | --- | --------- | --- | ----------- | --- | --- | --- |
|                       |     |                          |     | 𝜌   | (cid:169) 1− |           |     | (cid:170) | ,𝐶  |             | ,   |     |     |
|                       |     |                          |     |     | = (cid:173)  | √︃        |     | (cid:174) | =   | 𝜌(𝐻−2)(𝐻+𝑑) |     |     |     |
|                       |     |                          |     |     | (cid:173)    | 1+ 1+(ℓ/𝑚 | 𝑓)  | (cid:174) | 𝑚 𝑓 |             |     |     |     |
|                       |     |                          |     |     | (cid:171)    |           |     | (cid:172) |     |             |     |     |     |
| whereℓ (cid:66)max{𝐻ℓ |     | ,ℓ 𝑤}andℓ¯(cid:66)max{𝐻ℓ |     |     | ,ℓ ,ℓ}.      |           |     |           |     |             |     |     |     |
|                       | 𝑐   |                          |     |     | 𝑓 𝜇          |           |     |           |     |             |     |     |     |
Inthespecialcaseofthevideostreaming,weseethat
|     |     |     |     |     |     |     | max{6𝜔 | min(𝜔 | 3 ),4𝑥max(𝜔 | min+8𝛾)} |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ----------- | -------- | --- | --- | --- |
min+
|     |     |     |     | ℓ =max{3ℓ |     | 𝑐 ,ℓ 𝑤}= |     |     |     |     |     | .   |     |
| --- | --- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
𝜔 3
min
Therefore,wehave
1
3(3+⌈𝑥max/𝛿⌉)
|     |     |     |     | (cid:169)        |     |                                      |     | 2   |     | (cid:170) |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | ------------------------------------ | --- | --- | --- | --------- | --- | --- | --- |
|     |     |     |     | (cid:173)        |     |                                      |     |     |     | (cid:174) |     |     |     |
|     |     |     |     | 𝜌 = (cid:173) 1− |     |                                      |     |     |     | (cid:174) |     | .   |     |
|     |     |     |     | (cid:173)        |     | √︂ max{6𝜔min(𝜔min+3),4𝑥max(𝜔min+8𝛾)} |     |     |     | (cid:174) |     |     |     |
|     |     |     |     | (cid:173)        | 1+  | 1+                                   |     |     |     | (cid:174) |     |     |     |
𝜔3 𝜖𝛽
min
|     |     |     |     | (cid:171) |     |     |     |     |     | (cid:172) |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
Thecoefficient𝐶isboundedby
|     |     |     |     |     | 3𝛽𝜔 | 3 +max{6𝜔 | min(𝜔 | min+3),4𝑥max(𝜔 |     | min+8𝛾)} |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ----- | -------------- | --- | -------- | --- | --- | --- |
|     |     |     |     | 𝐶   | ≤   | m in      |       |                |     |          | .   |     |     |
|     |     |     |     |     |     |           | 𝜔3    | 𝜌3+⌈𝑥max/𝛿⌉    |     |          |     |     |     |
min
Discussionaboutdifferentdistortioncosts.NotethatAssumptionB.1stillholdsifwereplacethedistortioncostfunction𝑣(𝑟)= 1 by
𝑟
𝑣(𝑟)=log(𝑟max/𝑟).Thisisbecausethenewswitchingcost
|     |     |     | 𝑐 ′(𝑥 | ;𝑤    | 𝑡)=𝜔 | 𝑢 log(𝑟max𝑢 | 𝑡)+𝛾(𝑢 | −𝑢             | 2                |     |     |     |     |
| --- | --- | --- | ----- | ----- | ---- | ----------- | ------ | -------------- | ---------------- | --- | --- | --- | --- |
|     |     |     | 𝑡     | 𝑡:𝑡−2 |      | 𝑡 𝑡         |        | 𝑡              | 𝑡−1)             |     |     |     |     |
|     |     |     |       |       |      |             |        | (cid:18)𝑟max(𝑥 | 𝑥 𝑡−1+1)(cid:19) |     |     |     |     |
𝑡 −
|     |     |     |     |     | =(𝑥 | 𝑡 −𝑥 𝑡−1+1)log |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
𝜔 𝑡
2
|     |     |     |     |     |     | (𝜔 𝑡−1𝑥 | 𝑡 +𝜔 𝑡 𝑥 | 𝑡−2−(𝜔 | 𝑡 +𝜔 𝑡−1)𝑥 | 𝑡−1+(𝜔 | 𝑡−1−𝜔 | 𝑡)) |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | ---------- | ------ | ----- | --- | --- |
+𝛾
𝜔2𝜔2
𝑡 𝑡−1
,𝜔max]2andfeasible𝑥
| alsosatisfiesAssumptionB.1forany𝑤 |     |     |     | 𝑡 =(𝜔 | 𝑡 ,𝜔 | 𝑡−1) ∈ [𝜔 | min |     |     | 𝑡:𝑡−2 . |     |     |     |
| --------------------------------- | --- | --- | --- | ----- | ---- | --------- | --- | --- | --- | ------- | --- | --- | --- |
633

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
B.1 ProofofTheoremB.1
∈{0,1}4𝑝+5.Specifically,giventheuniqueoptimal
ToshowTheoremB.1,wefirstneedtodefineindicatorsofactiveconstraints,denotedas𝜉
solution𝑥0:𝑝 =𝜓(𝑦,𝑧;𝜇,𝑤,𝛿)underatupleofparameters(𝑦,𝑧;𝜇,𝑤,𝛿),weconsiderwhetherthefollowingequalityconditionshold:
|     |     |     | 𝜉1,𝑡 | =1{𝑥 | =0},∀0≤𝑡 | ≤𝑝; |     |     |     |
| --- | --- | --- | ---- | ---- | -------- | --- | --- | --- | --- |
𝑡
|     |     |     | 𝜉2,𝑡 | =1{𝑥 | 𝑡 =𝑥max},∀0≤𝑡 | ≤𝑝;     |       |     |     |
| --- | --- | --- | ---- | ---- | ------------- | ------- | ----- | --- | --- |
|     |     |     | 𝜉3,𝑡 | =1{𝑥 | 𝑡 =𝜇 𝑡},∀0≤𝑡  | ≤𝑝;     |       |     |     |
|     |     |     | 𝜉4,𝑡 | =1{𝑥 | −𝑥 𝑡−1=−𝛿     | 𝑡},∀0≤𝑡 | ≤𝑝+1. |     |     |
𝑡
∈{0,1}𝑝+1)asthefollowing:
Andwedefineindicatorsofthesides(denotedas𝜎
|     |     |     |     | 𝜎 𝑡 =1{𝑥 | 𝑡 ∈ [𝜇 | 𝑡 ,𝑥max]},∀0≤𝑡 | ≤𝑝. |     |     |
| --- | --- | --- | --- | -------- | ------ | -------------- | --- | --- | --- |
Tosimplifythenotation,welet𝜃 (cid:66) (𝜇,𝑤,𝛿) ∈Θ(cid:66) [0,𝑥max]𝑝+1×W𝑝+𝐻 ×Δ𝑝+2.While𝜓(𝑦,𝑧;𝜃)candecideauniquepairof(𝜉,𝜎),we
canalsodefineanewequality-constrainedoptimizationproblemusing(𝑦,𝑧;𝜃)and(𝜉,𝜎):
Wedefinetheequality-constrainedoptimizationproblem𝜓ˆ
| DefinitionB.1. |     |                 |     |                 |     | (𝑦,𝑧;𝜃;𝜉,𝜎)as |         |         |      |
| -------------- | --- | --------------- | --- | --------------- | --- | ------------- | ------- | ------- | ---- |
|                |     |                 |     |                 | 𝑝   |               | 𝑝+𝐻−1   |         |      |
|                |     |                 |     |                 | ∑︁  | (𝜎𝑡)          | ∑︁      |         |      |
|                |     | 𝜓ˆ (𝑦,𝑧;𝜃;𝜉,𝜎)= |     | argmin          |     | 𝑓 (𝑥 ;𝜇 𝑡)+   | 𝑐 𝑡(𝑥   | ;𝑤 𝑡)   | (9a) |
|                |     |                 |     |                 |     | 𝑡 𝑡           |         | 𝑡:𝑡−𝐻+1 |      |
|                |     |                 |     | 𝑥 −𝐻+1:𝑝+𝐻−1𝑡=0 |     |               | 𝑡=0     |         |      |
|                |     |                 |     |                 |     | 𝑥 0, i   | f 𝜉 = 1 |         |      |
1 , 𝑡
|     |     |     |     |     | s.t.𝑥 |               | ,∀0≤𝑡         | ≤𝑝, | (9b) |
| --- | --- | --- | --- | --- | ----- | ------------- | ------------- | --- | ---- |
|     |     |     |     |     | 𝑡 =   | max , i       | f 𝜉 2 , 𝑡 = 1 |     |      |
|     |     |     |     |     |       | 𝜇 , if𝜉3,𝑡 | =1            |     |      |
𝑡

|     |     |     |     |     | 𝑥 −𝑥          | 𝑡−1=−𝛿 | , if𝜉4,𝑡 =1,∀0≤𝑡 | ≤𝑝+1, | (9c) |
| --- | --- | --- | --- | --- | ------------- | ------ | ---------------- | ----- | ---- |
|     |     |     |     |     | 𝑡             | 𝑡      |                  |       |      |
|     |     |     |     |     | 𝑥 −𝐻+1:−1=𝑦,𝑥 |        | 𝑝+1:𝑝+𝐻−1=𝑧.     |       | (9d) |
Notethatitispossiblethattheoptimizationproblem𝜓ˆ
(𝑦,𝑧;𝜃;𝜉,𝜎)forsomeparametersandconstraintconfigurations.Weuse𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎)
todenotetheoptimalvalueofthisoptimizationproblem.Thefollowinglemmastatesthattheoptimalsolutionof (7)willnotchangeifwe
removeallinactiveinequalityconstraintsandleaveactiveconstraintsasequalityconstraints.
|           | SupposeAssumptionB.1holdsand𝑝 |     |     | ≥𝑑.For𝑦,𝑧 |     | [0,𝑥 ]𝐻−1 | and𝜃 ∈Θ,let𝜉,𝜎 |                                      |     |
| --------- | ----------------------------- | --- | --- | --------- | --- | --------- | -------------- | ------------------------------------ | --- |
| LemmaB.2. |                               |     |     |           | ∈   | max       |                | bethecorrespondingindicatorsofactive |     |
constraints/sides.Then,wehave
𝜓(𝑦,𝑧;𝜃)=𝜓ˆ
(𝑦,𝑧;𝜃;𝜉,𝜎)and𝜄(𝑦,𝑧;𝜃)=𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎).
| ProofofLemmaB.2. | Notethat |     |     |          |     |                |     |     |     |
| ---------------- | -------- | --- | --- | -------- | --- | -------------- | --- | --- | --- |
|                  |          |     |     | 𝜄(𝑦,𝑧;𝜃) |     | ≥𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎) |     |     |     |
becausetheoptimizationproblemontheRHShaslessconstraints.Iftheinequalityholdswithequality,wemusthave𝜓(𝑦,𝑧;𝜃)=𝜓ˆ
(𝑦,𝑧;𝜃;𝜉,𝜎)
sincetheoptimalsolutionfortheLHSisfeasiblefortheRHSbytheassumptiononactiveconstraints,andtheoptimizationproblemonthe
RHShasauniquesolution.Otherwise,wemusthave
|                                      |     | 𝜓(𝑦,𝑧;𝜃)≠𝜓ˆ |                | (𝑦,𝑧;𝜃;𝜉,𝜎), |     | and𝜄(𝑦,𝑧;𝜃) | >𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎). |     |     |
| ------------------------------------ | --- | ----------- | -------------- | ------------ | --- | ----------- | --------------- | --- | --- |
| Considertheconvexcombination𝜁(𝜂)for𝜂 |     |             | [0,1]definedas |              |     |             |                 |     |     |
∈
𝜁(𝜂)=(1−𝜂)𝜓(𝑦,𝑧;𝜃)+𝜂𝜓ˆ
(𝑦,𝑧;𝜃;𝜉,𝜎).
Notethat𝜁(𝜂)satisfiesalltheactiveconstraintsandsidesasspecifiedby(𝜉,𝜎)becausetheyareactiveforall𝜂 ∈ [0,1].Sincetheconstraints
of (7)thatarenotin(𝜉,𝜎)areinactiveat𝜂 =0,theremustexist𝜂 >0suchthat𝜁(𝜂)isalsofeasiblefor(7).𝜁(𝜂)achievesastrictlysmaller
| objectivethan𝜁(0)=𝜓(𝑦,𝑧;𝜃),whichleadstoacontradiction. |     |     |     |     |     |     |     |     | □   |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LemmaB.2establishesthatgivenanyfeasibletupleof(𝑦,𝑧;𝜃),onecanfindatleastonepairof(𝜉,𝜎)suchthat𝜓(𝑦,𝑧;𝜃)=𝜓ˆ
(𝑦,𝑧;𝜃;𝜉,𝜎),
| whiletherecanbeother(𝜉′,𝜎′)thatsatisfies𝜓(𝑦,𝑧;𝜃)=𝜓ˆ |     |     |     |             | (𝑦,𝑧;𝜃;𝜉′,𝜎′). |                  |     |     |      |
| --------------------------------------------------- | --- | --- | --- | ----------- | -------------- | ---------------- | --- | --- | ---- |
|                                                     |     |     |     | ≥𝑑.Ifboth𝜓ˆ |                | (𝑦,𝑧;𝜃;𝜉,𝜎)and𝜓ˆ |     |     | ]𝐻−1 |
LemmaB.3. SupposeAssumptionB.1holdsand𝑝 (𝑦′,𝑧′;𝜃′;𝜉,𝜎)existfor𝑦,𝑧,𝑦′,𝑧′ ∈ [0,𝑥 and
max
(𝜉,𝜎),thenwehave
|     | (cid:13) 𝜓ˆ           | −𝜓ˆ (𝑦′,𝑧′;𝜃′;𝜉,𝜎)𝑡 |     | (cid:13) |     |       |     |     |     |
| --- | --------------------- | ------------------- | --- | -------- | --- | ----- | --- | --- | --- |
|     | (cid:13) (𝑦,𝑧;𝜃;𝜉,𝜎)𝑡 |                     |     | (cid:13) |     |       |     |     |     |
|     | (cid:13)              |                     |     | (cid:13) |     |       |     |     |     |
|     |                       |                     |     | 𝑝        |     | 𝑝+𝐻−1 |     | 𝑝+1 |     |
|     |                       |                     |     | ∑︁       |     |       | ∑︁  | ∑︁  |     |
≤𝐶(cid:0)𝜌𝑡(cid:13) 𝑦−𝑦′(cid:13) (cid:13)+𝜌𝑝−𝑡(cid:13) 𝑧−𝑧′(cid:13) (cid:1)+𝐶(cid:169) 𝜌|𝑡−𝜏|(cid:12) 𝜇 −𝜇 ′(cid:12) (cid:12)+ 𝜌|𝑡−𝜏|(cid:13) 𝑤 −𝑤 ′(cid:13) (cid:13)+ 𝜌|𝑡−𝜏|(cid:12) 𝛿 −𝛿 ′(cid:12) (cid:12)(cid:170) , (10)
(cid:13) (cid:13) (cid:13) (cid:173) (cid:12) 𝜏 𝜏 (cid:13) 𝜏 𝜏 (cid:12) 𝜏 𝜏 (cid:174)
|     |     |     |     | 𝜏=0       |     |     | 𝜏=0 | 𝜏=0       |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --------- | --- |
|     |     |     |     | (cid:171) |     |     |     | (cid:172) |     |
634

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
where
1
|        |                |                          |     |     |              |        |     | 𝐻(𝐻+𝑑)    |      | 2ℓ¯         |     |     |     |     |
| ------ | -------------- | ------------------------ | --- | --- | ------------ | ------ | --- | --------- | ---- | ----------- | --- | --- | --- | --- |
|        |                |                          |     |     | (cid:169)    | 2      |     | (cid:170) |      |             |     |     |     |     |
|        |                |                          |     | 𝜌   | = 1−         |        |     |           | ,𝐶 = |             | .   |     |     |     |
|        |                |                          |     |     | (cid:173)    | √︃     |     | (cid:174) | 𝑚    | 𝜌(𝐻−2)(𝐻+𝑑) |     |     |     |     |
|        |                |                          |     |     | (cid:173) 1+ | 1+(ℓ/𝑚 | 𝑓)  | (cid:174) |      | 𝑓           |     |     |     |     |
|        |                |                          |     |     | (cid:171)    |        |     | (cid:172) |      |             |     |     |     |     |
| Here,ℓ | (cid:66)max{𝐻ℓ | ,ℓ 𝑤}andℓ¯(cid:66)max{𝐻ℓ |     |     | ,ℓ ,ℓ}.      |        |     |           |      |             |     |     |     |     |
|        |                | 𝑐                        |     | 𝑓   | 𝜇            |        |     |           |      |             |     |     |     |     |
ProofofLemmaB.3. Wedoavariablechangetoeliminateallconstraintsintheequality-constrainedoptimizationproblem.Afterthe
elimination,wegetanunconstrainedoptimizationproblemwiththefreevariables𝑥 ,𝑥 ,...,𝑥 wheretheindicessatisfy0≤𝑡0 <𝑡1 <
|     |     |     |     |     |     |     |     |     |     | 𝑡0 𝑡1 | 𝑡𝑞  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
...<𝑡 ≤𝑝.Tosimplifythenotation,welet𝑡 −1=−1and𝑡 𝑞+1=𝑝+1.For𝜏thatsatisfies𝑡 <𝜏 <𝑡 ,wehaveeither𝑥 =𝑥 −(cid:205) 𝜏 𝛿
|     | 𝑞   |     |     |     |     |     |     |     |     | 𝑖   |     | 𝑖+1 | 𝜏 𝑡𝑖 | 𝛾 =𝑡𝑖+1 𝛾 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- |
or𝑥 𝜏 issomeconstant.Withoutlossofgenerality,wecanassume𝑡 𝑖+1 ≤𝑡 𝑖 +𝑑+𝐻,becauseotherwisewecanfind𝜏 ∈ (𝑡 𝑖 ,𝑡 𝑖+1−𝐻]such
that𝑥 areconstants,whichmeansthefreevariablesafter𝑥 willnotchange,regardlessofhowweperturb𝑦,andthefreevariables
|     | 𝜏:𝜏+𝐻−1 |     |     |     |     |     | 𝑡𝑖+1 |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
before𝑥 willnotchange,regardlessofhowweperturb𝑧.Thus,wecandecomposetheperturbationtotheleftsideandtherightsideand
𝑡𝑖
derivethemseparately.
Afterthechangeofvariable,theobjectivebecomesafunctionℎˆof𝑥
|     |     |     |     |     |     |     |     | 𝑡0  | ,𝑥 𝑡1 ,...,𝑥 | 𝑡𝑞 .Tosimplifythenotation,welet𝑥ˆ |     |     | 𝜏 (cid:66) 𝑥 𝑡𝜏 | ,where |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------------------------- | --- | --- | --------------- | ------ |
𝜏 =0,...,𝑞.Wecandecomposeℎˆas
|     |            |     |     |     |     | ℎˆ ;𝜁)=ℎˆ |      | ;𝜇)+ℎˆ |                            |      |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --------- | ---- | ------ | -------------------------- | ---- | --- | --- | --- | --- |
|     |            |     |     |     |     | (𝑥ˆ 0:𝑞   | 𝑎(𝑥ˆ | 0:𝑞    | 𝑏(𝑥ˆ 0:𝑞                   | ;𝜁), |     |     |     |     |
|     | (𝑦,𝑧,𝜃),ℎˆ |     |     |     |     |           |      | 𝑚      | (cid:13) (cid:13) 2 ,andℎˆ |      |     |     |     |     |
where𝜁 = 𝑎 isthesumoftheoriginalhittingcostsminus 𝑓 (cid:13) 𝑥ˆ 0:𝑞 (cid:13) 𝑏 isthesumoftheoriginalswitchingcostsplus
2
| 𝑚 𝑓 (cid:13) 𝑥ˆ | (cid:13) 2 .ByAssumptionB.1,weseethat |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2 (cid:13) 0:𝑞 (cid:13)
|     |     |     |     | 2      | ℎˆ       |           |       |        | 2 ℎˆ   |         |         |     |     |      |
| --- | --- | --- | --- | ------ | -------- | --------- | ----- | ------ | ------ | ------- | ------- | --- | --- | ---- |
|     |     |     |     | ∇      | 𝑎(𝑥ˆ 0:𝑞 | ;𝜇) ⪰0,(𝑚 | 𝑓 +𝐻ℓ | 𝑐)𝐼 ⪰∇ | 𝑏(𝑥ˆ   | 0:𝑞 ;𝜁) | ⪰𝑚 𝑓 𝐼. |     |     | (11) |
|     |     |     |     | 𝑥 ˆ0:𝑞 |          |           |       |        | 𝑥 ˆ0:𝑞 |         |         |     |     |      |
Wealsonotethat∇ 2 ℎˆ 𝑎(𝑥ˆ ;𝜇)isadiagonalmatrixand∇ 2 ℎˆ 𝑏(𝑥ˆ ;𝜁)isa2𝐻-bandedmatrix.
|     |     |        | 0:𝑞 |     |     |     |        | 0:𝑞 |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | 𝑥 ˆ0:𝑞 |     |     |     |     | 𝑥 ˆ0:𝑞 |     |     |     |     |     |     |     |
WecanfollowasimilarprocedureasTheorem3.1in[49]toshow
|     | (cid:13) | 𝜓ˆ            | −𝜓ˆ (𝑦′,𝑧′;𝜃′;𝜉,𝜎)𝑡𝜏 |     | (cid:13) |     |     |     |       |     |     |     |     |     |
| --- | -------- | ------------- | -------------------- | --- | -------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     | (cid:13) | (𝑦,𝑧;𝜃;𝜉,𝜎)𝑡𝜏 |                      |     | (cid:13) |     |     |     |       |     |     |     |     |     |
|     | (cid:13) |               |                      |     | (cid:13) |     |     |     |       |     |     |     |     |     |
|     |          |               |                      |     |          | 𝑝   |     |     | 𝑝+𝐻−1 |     |     | 𝑝+1 |     |     |
(cid:16) 𝑞 −𝜏(cid:13) (cid:17) ∑︁ |𝜙(𝑖)−𝜏|(cid:12) ∑︁ |𝜙(𝑖)−𝜏|(cid:13) ∑︁ |𝜙(𝑖)−𝜏|(cid:13)
≤𝐶0 𝜌𝜏 (cid:13) 𝑦−𝑦′(cid:13) (cid:13)+𝜌 𝑧−𝑧′(cid:13) +𝐶0(cid:169) 𝜌 𝜇 −𝜇 ′(cid:12) (cid:12)+ 𝜌 𝑤 −𝑤 ′(cid:13) (cid:13)+ 𝜌 𝛿 −𝛿 ′(cid:13) (cid:13)(cid:170) , (12)
0 (cid:13) 0 (cid:13) (cid:13) (cid:173) 0 (cid:12) 𝑖 𝑖 0 (cid:13) 𝑖 𝑖 0 (cid:13) 𝑖 𝑖 (cid:174)
|                             |     |     |                |     |     | 𝑖=0       |     |     | 𝑖=0 |     |     | 𝑖=0 |           |     |
| --------------------------- | --- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --------- | --- |
|                             |     |     |                |     |     | (cid:171) |     |     |     |     |     |     | (cid:172) |     |
| where𝜙(𝑖)denotestheinteger𝑗 |     |     | thatsatisfies𝑡 |     | ≤𝑖  | <𝑡        | and |     |     |     |     |     |           |     |
|                             |     |     |                |     | 𝑗   | 𝑗+1       |     |     |     |     |     |     |           |     |
1
𝐻
|     |     |     |     |     |     |              | 2      |           |      | 2ℓ¯ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 𝜌0= | (cid:169) 1− |        | (cid:170) | ,𝐶0= | .   |     |     |     |     |
|     |     |     |     |     |     | (cid:173) √︃ |        | (cid:174) |      | 𝐻−2 |     |     |     |     |
|     |     |     |     |     |     | (cid:173)    | 1+(ℓ/𝑚 | (cid:174) | 𝑚    | 𝑓 𝜌 |     |     |     |     |
|     |     |     |     |     |     |              |        | 𝑓)        |      | 0   |     |     |     |     |
|     |     |     |     |     |     | (cid:171)    |        | (cid:172) |      |     |     |     |     |     |
𝑤}andℓ¯(cid:66)max{𝐻ℓ
Here,ℓ (cid:66)max{𝐻ℓ 𝑐 ,ℓ ,ℓ 𝜇 ,ℓ}.Forcompleteness,wegivethedetailedproofbelow:Let𝑒beavectorsuchthatboth𝜁 and
𝑓
𝜁 +𝑒areinY×Z×Θ.Considerthefunction
|     |     |     |     |     |     | 𝜓(𝜁 +𝜂𝑒) | (cid:66)𝜓ˆ | (𝜁 +𝜂𝑒;𝜉,𝜎)𝑡0:𝑞 |     | ,   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | --------------- | --- | --- | --- | --- | --- | --- |
whichisimplicitlydeterminedbytheequation
|     |     |     |     |     |     | ∇𝑥ˆ0:𝑞 | ℎˆ (𝜓(𝜁 | +𝜂𝑒),𝜁 | +𝜂𝑒)=0. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ------- | ------ | ------- | --- | --- | --- | --- | --- |
Bytheimplicitfunctiontheoremweknowthatthefunction𝜓 isdifferentiable.Takingthederivativewithrespectto𝜃 givesthat
𝑑
∇ 2 ℎˆ (𝜓(𝜁 +𝜂𝑒),𝜁 +𝜂𝑒) 𝜓(𝜁 +𝜂𝑒)= −∇𝑦∇𝑥ˆ0:𝑞 ℎˆ (𝜓(𝜁 +𝜂𝑒),𝜁 +𝜂𝑒)𝑒 𝑦−∇𝑧∇𝑥ˆ0:𝑞 ℎˆ (𝜓(𝜁 +𝜂𝑒),𝜁 +𝜂𝑒)𝑒
|     | 𝑥 ˆ0:𝑞 |     |     | 𝑑𝜂  |     |     |           |             |       |       |     |           | 𝑧                 |     |
| --- | ------ | --- | --- | --- | --- | --- | --------- | ----------- | ----- | ----- | --- | --------- | ----------------- | --- |
|     |        |     |     |     |     | 𝑝   |           |             |       | 𝑝+𝐻−1 |     |           |                   |     |
|     |        |     |     |     |     | ∑︁  |           |             |       |       | ∑︁  |           |                   |     |
|     |        |     |     |     | −   | ∇𝜇𝑡 | ∇𝑥ˆ0:𝑞 ℎˆ | (𝜓(𝜁 +𝜂𝑒),𝜁 | +𝜂𝑒)𝑒 | −     | ∇𝑤𝑡 | ∇𝑥ˆ0:𝑞 ℎˆ | (𝜓(𝜁 +𝜂𝑒),𝜁 +𝜂𝑒)𝑒 |     |
|     |        |     |     |     |     |     |           |             |       | 𝜇𝑡    |     |           | 𝑤𝑡                |     |
|     |        |     |     |     |     | 𝑡=0 |           |             |       |       | 𝑡=0 |           |                   |     |
𝑝
|     |     |     |     |     |     | ∑︁  | ℎˆ     | (𝜓(𝜁 +𝜂𝑒),𝜁 | +𝜂𝑒)𝑒 | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     | −   | ∇𝛿𝑡 | ∇𝑥ˆ0:𝑞 |             |       | 𝛿𝑡  |     |     |     |     |
𝑡=0
635

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
Tosimplifythenotation,wedefine
|     |     |     |     | 𝑀 (cid:66)∇ | 2 ℎˆ (𝜓(𝜁 | +𝜂𝑒),𝜁 | +𝜂𝑒),whichisa(𝑞+1)×(𝑞+1)matrix, |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --------- | ------ | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑥ˆ0:𝑞
|     |     |     | 𝑅(𝑦)  |                   |        | ℎˆ      |                                        |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ----------------- | ------ | ------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |       | (cid:66)−∇𝑦∇𝑥ˆ0:𝑞 |        | (𝜓(𝜁    | +𝜂𝑒),𝜁 +𝜂𝑒),whichisa(𝑞+1)×(𝐻−1)matrix, |     |     |     |     |     |     |     |     |
|     |     |     | 𝑅(𝑧)  | (cid:66)−∇𝑧∇𝑥ˆ0:𝑞 |        | ℎˆ (𝜓(𝜁 | +𝜂𝑒),𝜁 +𝜂𝑒),whichisa(𝑞+1)×(𝐻−1)matrix, |     |     |     |     |     |     |     |     |
|     |     |     | 𝑅(𝜇𝑡) |                   |        | ℎˆ      |                                        |     |     |     |     |     |     |     |     |
|     |     |     |       | (cid:66)−∇𝜇𝑡      | ∇𝑥ˆ0:𝑞 | (𝜓(𝜁    | +𝜂𝑒),𝜁 +𝜂𝑒),whichisa(𝑞+1)×1matrix,     |     |     |     |     |     |     |     |     |
ℎˆ
|     |     |     | 𝑅(𝑤𝑡) | (cid:66)−∇𝑤𝑡 | ∇𝑥ˆ0:𝑞 | (𝜓(𝜁    | +𝜂𝑒),𝜁 +𝜂𝑒),whichisa(𝑞+1)×𝑑matrix, |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ------------ | ------ | ------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 𝑅(𝛿𝑡) | (cid:66)−∇𝛿𝑡 |        | ℎˆ (𝜓(𝜁 | +𝜂𝑒),𝜁 +𝜂𝑒),whichisa(𝑞+1)×1matrix. |     |     |     |     |     |     |     |     |
∇𝑥ˆ0:𝑞
Hencewecanwrite
|     |     |     |     |     |     |     | 𝑝   |     | 𝑝+𝐻−1 |     | 𝑝   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
𝑑
|     |     |     | 𝜓(𝜁 | +𝜂𝑒)=𝑀−1(cid:169) | 𝑅(𝑦)𝑒     | 𝑦+𝑅(𝑧)𝑒 | ∑︁  | 𝑅(𝜇𝑡)𝑒 | ∑︁   | 𝑅(𝑤𝑡)𝑒 | ∑︁   | 𝑅(𝛿𝑡)𝑒 | (cid:170) . |     |     |
| --- | --- | --- | --- | ----------------- | --------- | ------- | --- | ------ | ---- | ------ | ---- | ------ | ----------- | --- | --- |
|     |     |     | 𝑑 𝜃 |                   | (cid:173) |         | 𝑧+  |        | 𝜇𝑡 + |        | 𝑤𝑡 + | 𝛿𝑡     | (cid:174)   |     |     |
|     |     |     |     |                   |           |         | 𝑡=0 |        | 𝑡=0  |        | 𝑡=0  |        |             |     |     |
|     |     |     |     |                   | (cid:171) |         |     |        |      |        |      |        | (cid:172)   |     |     |
Recallthat𝑅(𝑦),𝑅(𝑧) are(𝑞+1)×(𝐻−1)matrices.For𝑅(𝑦),onlythefirst𝐻−1rowsarenon-zero.For𝑅(𝑧),onlythelast𝐻−1rowsare
non-zero.Henceweseethat
|     |     | 𝑑   |           |       |          | 𝑦         |           |            | (𝑧   |                |      |            |     |     |     |
| --- | --- | --- | --------- | ----- | -------- | --------- | --------- | ---------- | ---- | -------------- | ---- | ---------- | --- | --- | --- |
|     |     |     | 𝜓(𝜁 +𝜂𝑒)𝜏 | =(𝑀−1 | )𝜏,0:𝐻−2 | 𝑅 ( )     | 𝑒 𝑦+(𝑀−1  | )𝜏,𝑞−𝐻+2:𝑞 | 𝑅 )  | 𝑒              |      |            |     |     |     |
|     |     | 𝑑 𝜂 |           |       |          | 0 : 𝐻     | −2,:      |            | 𝑞 −  | 𝐻+2:𝑞,: 𝑧      |      |            |     |     |     |
|     |     |     |           |       | 𝑞 𝑡𝑗+1−1 |           |           | 𝑞+1𝑡𝑗+1−1  |      |                |      |            |     |     |     |
|     |     |     |           | ∑︁    | ∑︁       |           | 𝜇         | ∑︁ ∑︁      |      |                | (𝑤   |            |     |     |     |
|     |     |     |           | +     |          | (𝑀−1 )𝜏,𝑗 | 𝑅 ( 𝑖)𝑒 + |            | (𝑀−1 | )𝜏,𝑗−𝐻+1:𝑗+𝐻−1 | 𝑅    | 𝑖)         | 𝑒   |     |     |
|     |     |     |           |       |          |           | 𝑗 , : 𝜇𝑖  |            |      |                | 𝑗 −𝐻 | +1:𝑗+𝐻−1,: | 𝑤𝑖  |     |     |
|     |     |     |           | 𝑗=0   | 𝑖=𝑡𝑗     |           |           | 𝑗=0 𝑖=𝑡𝑗   |      |                |      |            |     |     |     |
𝑞 𝑡𝑗+1−1
|     |     |     |     | ∑︁  | ∑︁  |           | 𝛿         |     |     |     |     |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | +   |     | (𝑀−1 )𝜏,𝑗 | 𝑅 ( 𝑖)𝑒 . |     |     |     |     |     |     |     | (13) |
𝑗 , : 𝛿𝑖
𝑗=0 𝑖=𝑡𝑗
| Recallthatℓ¯(cid:66)max{𝐻ℓ |     |     | ,𝐻ℓ ,ℓ ,ℓ | 𝑤}.Weknowthatthenormsof |      |       |              |     |     |          |     |     |     |     |     |
| -------------------------- | --- | --- | --------- | ----------------------- | ---- | ----- | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- |
|                            |     |     | 𝑐 𝑓 𝜇     |                         |      |       |              |     |     |          |     |     |     |     |     |
|                            |     |     |           |                         | 𝑅(𝑦) | ,𝑅(𝑧) | ,𝑅(𝜇𝑖),𝑅(𝑤𝑖) |     |     | and𝑅(𝛿𝑖) |     |     |     |     |     |
,
|                                                |     |     |                    |                      | 0:𝐻−2,:      | 𝑞−𝐻+2:𝑞,: | 𝑗,:                                                         | 𝑗−𝐻+1:𝑗+𝐻−1,:          |           | 𝑗,:                   |     |          |                      |     |     |
| ---------------------------------------------- | --- | --- | ------------------ | -------------------- | ------------ | --------- | ----------------------------------------------------------- | ---------------------- | --------- | --------------------- | --- | -------- | -------------------- | --- | --- |
| areallupperboundedbyℓ¯.Takingnormonbothsidesof |     |     |                    |                      |              |           | (13)gives                                                   |                        |           |                       |     |          |                      |     |     |
|                                                |     |     | (cid:13) 𝑑         | (cid:13)             |              |           |                                                             |                        |           |                       |     |          |                      |     |     |
|                                                |     |     | (cid:13)           | (cid:13) ≤ℓ¯(cid:13) | (cid:13)(𝑀−1 |           | (cid:13) (cid:13) (cid:13) (cid:13)+ℓ¯(cid:13) (cid:13)(𝑀−1 |                        |           | (cid:13)              |     |          |                      |     |     |
|                                                |     |     | (cid:13) 𝜓(𝜁 +𝜂𝑒)𝜏 | (cid:13)             |              | )𝜏,0:𝐻−2  | (cid:13) (cid:13) 𝑒 𝑦                                       | )𝜏,𝑞−𝐻+2:𝑞             |           | (cid:13)∥𝑒 𝑧∥         |     |          |                      |     |     |
|                                                |     |     | (cid:13)𝑑𝜃         | (cid:13)             |              |           |                                                             |                        |           |                       |     |          |                      |     |     |
|                                                |     |     |                    |                      | 𝑞            | 𝑡𝑗+1−1    |                                                             |                        | 𝑞+1𝑡𝑗+1−1 |                       |     |          |                      |     |     |
|                                                |     |     |                    |                      | +ℓ¯∑︁        | ∑︁        | (cid:13) (cid:13)(𝑀−1 (cid:13) (cid:13) 𝑒                   | (cid:13) (cid:13)+ℓ¯∑︁ | ∑︁        | (cid:13) (cid:13)(𝑀−1 |     | (cid:13) | (cid:13) 𝑒 (cid:13)  |     |     |
|                                                |     |     |                    |                      |              |           | )𝜏,𝑗 (cid:13) (cid:13)                                      | 𝜇𝑖                     |           | )𝜏,𝑗−𝐻+1:𝑗+𝐻−1        |     | (cid:13) | (cid:13) 𝑤𝑖 (cid:13) |     |     |
|                                                |     |     |                    |                      | 𝑗=0          | 𝑖=𝑡𝑗      |                                                             |                        | 𝑗=0 𝑖=𝑡𝑗  |                       |     |          |                      |     |     |
|                                                |     |     |                    |                      | 𝑞            | 𝑡𝑗+1−1    |                                                             |                        |           |                       |     |          |                      |     |     |
+ℓ¯∑︁ ∑︁ (cid:13) (cid:13)(𝑀−1 (cid:13) (cid:13) 𝑒 (cid:13) . (14)
|                             |     |     |     |     |       |        | )𝜏,𝑗 (cid:13) (cid:13) | 𝛿𝑖 (cid:13) |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | ----- | ------ | ---------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|                             |     |     |     |     | 𝑗=0   | 𝑖=𝑡𝑗   |                        |             |     |     |     |     |     |     |     |
| Notethat𝑀canbedecomposedas𝑀 |     |     |     |     |       | ,where |                        |             |     |     |     |     |     |     |     |
|                             |     |     |     | =𝑀  | 𝑎+𝑀 𝑏 |        |                        |             |     |     |     |     |     |     |     |
2 ℎˆ
|     |     |     |     |     |     | 𝑀 𝑎 | :=∇ 𝑎(𝜓(𝜁 | +𝜂𝑒),𝜁 | +𝜂𝑒), |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
𝑥 ˆ0:𝑞
|     |     |     |     |     |     | 𝑀   | :=∇ 2 ℎˆ 𝑏(𝜓(𝜁 | +𝜂𝑒),𝜁 | +𝜂𝑒). |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 𝑏   | 𝑥 ˆ0:𝑞         |        |       |     |     |     |     |     |     |
Since𝑀 𝑎 isadiagonal(𝑞+1)×(𝑞+1)matrixandsatisfies𝑀 𝑎 ⪰0,and𝑀 is2𝐻-bandedandsatisfies(𝑚 +ℓ)𝐼 ⪰𝑀 ⪰𝑚 𝐼,weobtain
|     |     |     |     |     |     |     |     | 𝑏   |     |     |     | 𝑓   | 𝑏   | 𝑓   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thefollowingwithLemmaB.1in[49]:
|         |              |         |          | (cid:13) (cid:13)(𝑀−1 |                | (cid:13) 2       | 𝜌𝜏 −(𝐻−2),(cid:13) (cid:13)(𝑀−1 |            |           | (cid:13) 2     | 𝑞 −𝜏−(𝐻−2) |     |     |     |     |
| ------- | ------------ | ------- | -------- | --------------------- | -------------- | ---------------- | ------------------------------- | ---------- | --------- | -------------- | ---------- | --- | --- | --- | --- |
|         |              |         |          |                       | )𝜏,0:𝐻−2       | (cid:13)≤        |                                 | )𝜏,𝑞−𝐻+2:𝑞 |           | (cid:13)≤ 𝜌    |            |     |     |     |     |
|         |              |         |          |                       |                | 𝑚                | 0                               |            |           | 𝑚              | 0          |     |     |     |     |
|         |              |         |          |                       |                | 𝑓                |                                 |            |           | 𝑓              |            |     |     |     |     |
|         |              |         |          | (cid:13) (cid:13)(𝑀−1 | (cid:13)       | 2 |𝜏−𝑗|,(cid:13) | (cid:13)(𝑀−1                    |            | (cid:13)  | 2 |𝜏−𝑗|−(𝐻−1), |            |     |     |     |     |
|         |              |         |          |                       | )𝜏,𝑗 (cid:13)≤ | 𝜌                | )𝜏,𝑗−𝐻+1:𝑗+𝐻−1                  |            | (cid:13)≤ | 𝜌              |            |     |     |     |     |
|         |              |         |          |                       |                | 𝑚 0              |                                 |            |           | 𝑚 0            |            |     |     |     |     |
|         |              |         |          |                       |                | 𝑓                |                                 |            |           | 𝑓              |            |     |     |     |     |
|         |              |         |          |                       |                |                  | (cid:16)√︁1+(ℓ/𝜇)+1             | (cid:17)−1 |           |                |            |     |     |     |     |
| where𝜌0 | :=( √︁𝑐𝑜𝑛𝑑(𝑀 | 𝑏)−1)/( | √︁𝑐𝑜𝑛𝑑(𝑀 |                       | 𝑏)+1)=1−2·     |                  |                                 |            | .         |                |            |     |     |     |     |
Substitutingthisinto(14),weseethat
|     | (cid:13) |     | (cid:13) |     |     |     | 𝑝   |     | 𝑝+ 𝐻−1 |     |     | 𝑝   |     |     |     |
| --- | -------- | --- | -------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
𝑑 𝑞 −𝜏 ∑︁ |𝜙(𝑖)−𝜏|(cid:13) ∑︁ |𝜙(𝑖)−𝜏|(cid:13) ∑︁ |𝜙(𝑖)−𝜏|(cid:13)
(cid:13) 𝜓(𝜁 +𝜃𝑒)𝜏 (cid:13) ≤𝐶0(cid:169) 𝜌𝜏 (cid:13) 𝑒 (cid:13) (cid:13)+𝜌 ∥𝑒 𝑧∥+ 𝜌 𝑒 (cid:13) (cid:13)+ 𝜌 𝑒 (cid:13) (cid:13)+ 𝜌 𝑒 (cid:13) (cid:13)(cid:170) .
(cid:13) (cid:13)𝑑 𝜃 (cid:13) (cid:173) 0 (cid:13) 𝑦 0 0 (cid:13) 𝜇𝑖 0 (cid:13) 𝑤𝑖 0 (cid:13) 𝛿𝑖 (cid:174)
|     |     |     | (cid:13) |           |     |     | 𝑖=0 |     | 𝑖=0 |     |     | 𝑖=0 |     |           |     |
| --- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
|     |     |     |          | (cid:171) |     |     |     |     |     |     |     |     |     | (cid:172) |     |
636

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
Henceweobtain
|     |                |      |                 | (cid:13) ∫ 1 |       | (cid:13)    |     |     |     |     |     |     |     |     |
| --- | -------------- | ---- | --------------- | ------------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:13)       |      | (cid:13)        | (cid:13) 𝑑   |       | (cid:13)    |     |     |     |     |     |     |     |     |
|     | (cid:13) 𝜓(𝜁)𝜏 | −𝜓(𝜁 | +𝑒)𝜏 (cid:13) = | (cid:13) 𝜓(𝜁 | +𝜂𝑒)𝜏 | 𝑑𝜂 (cid:13) |     |     |     |     |     |     |     |     |
|     | (cid:13)       |      | (cid:13)        | (cid:13) 𝑑 𝜂 |       | (cid:13)    |     |     |     |     |     |     |     |     |
0
|     |     |     |     | 1(cid:13)           |       | (cid:13) |                     |     |       |                     |     |                     |     |     |
| --- | --- | --- | --- | ------------------- | ----- | -------- | ------------------- | --- | ----- | ------------------- | --- | ------------------- | --- | --- |
|     |     |     |     | ∫ (cid:13) 𝑑        |       | (cid:13) |                     |     |       |                     |     |                     |     |     |
|     |     |     | ≤   | 𝜓(𝜁                 | +𝜂𝑒)𝜏 | 𝑑𝜂       |                     |     |       |                     |     |                     |     |     |
|     |     |     |     | (cid:13) (cid:13)𝑑𝜂 |       | (cid:13) |                     |     |       |                     |     |                     |     |     |
|     |     |     |     | 0                   |       | (cid:13) |                     |     |       |                     |     |                     |     |     |
|     |     |     |     |                     |       |          | 𝑝                   |     | 𝑝+𝐻−1 |                     |     | 𝑝                   |     |     |
|     |     |     |     |                     | 𝑞 −𝜏  |          | ∑︁ |𝜙(𝑖)−𝜏|(cid:13) |     |       | ∑︁ |𝜙(𝑖)−𝜏|(cid:13) |     | ∑︁ |𝜙(𝑖)−𝜏|(cid:13) |     |     |
≤𝐶0(cid:169) 𝜌𝜏 (cid:13) 𝑒 (cid:13) (cid:13)+𝜌 ∥𝑒 𝑧∥+ 𝜌 𝑒 (cid:13) (cid:13)+ 𝜌 𝑒 (cid:13) (cid:13)+ 𝜌 𝑒 (cid:13) (cid:13)(cid:170) .
|     |     |     |     | (cid:173) 0 (cid:13) 𝑦 | 0   |     | 0   | (cid:13) | 𝜇𝑖  | 0   | (cid:13) 𝑤𝑖 | 0   | (cid:13) 𝛿𝑖 (cid:174) |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- | -------- | --- | --- | ----------- | --- | --------------------- | --- |
|     |     |     |     |                        |     |     | 𝑖=0 |          |     | 𝑖=0 |             | 𝑖=0 |                       |     |
|     |     |     |     | (cid:171)              |     |     |     |          |     |     |             |     | (cid:172)             |     |
Thisfinishestheproofof (12).Recallthatwehave𝑡 𝑖 <𝑡 𝑖+1 ≤𝑡 𝑖 +𝑑+𝐻.Therefore,(12)implies(10). □
Inthenextlemma,weshowacontinuitypropertyofthe“equality-constrainedlabeling”method.
∞
LemmaB.4. SupposeAssumptionB.1holdsand𝑝 ≥𝑑.Forapairof(𝜉,𝜎),ifanytupleinthesequence{(𝑦 𝑞 ,𝑧 𝑞 ;𝜃 𝑞)} =1satisfies𝜓(𝑦 𝑞 ,𝑧 𝑞 ;𝜃 𝑞)=
𝑞
| 𝜓ˆ (𝑦 ,𝑧 | ;𝜃 ;𝜉,𝜎)andlim | 𝑞→∞(𝑦 |     | ,𝑧 ,𝜃 𝑞)=(𝑦,𝑧,𝜃),thenwehave |     |     |     |     |     |     |     |     |     |     |
| -------- | -------------- | ----- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑞        | 𝑞 𝑞            |       | 𝑞   | 𝑞                           |     |     |     |     |     |     |     |     |     |     |
𝜓(𝑦,𝑧;𝜃)=𝜓ˆ
(𝑦,𝑧;𝜃;𝜉,𝜎).
ProofofLemmaB.4. Note that the perturbation bound in Lemma B.3 also establishes the continuity of the function𝜓ˆ (·,·;·;𝜉,𝜎).
Therefore,weseethat
|     |     |     |     |     |          |          | 𝜓ˆ     |             | ;𝜉,𝜎)=𝜓ˆ |              |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | ------ | ----------- | -------- | ------------ | --- | --- | --- | --- |
|     |     |     |     | lim | 𝜓(𝑦 𝑞 ,𝑧 | 𝑞 ;𝜃 𝑞)= | lim (𝑦 | 𝑞 ,𝑧 𝑞 ;𝜃 𝑞 |          | (𝑦,𝑧;𝜃;𝜉,𝜎). |     |     |     |     |
|     |     |     |     | 𝑞→∞ |          | 𝑞→∞      |        |             |          |              |     |     |     |     |
(7)isclosed,weknow𝜓ˆ
| Sincetheconstraintsetof                       |     |     |     |     | (𝑦,𝑧;𝜃;𝜉,𝜎)isafeasiblesolutionof |                                |     |     |     | (7). |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | -------------------------------- | ------------------------------ | --- | --- | --- | ---- | --- | --- | --- | --- |
| Forthesakeofcontradiction,weassume𝜓(𝑦,𝑧;𝜃)≠𝜓ˆ |     |     |     |     |                                  | (𝑦,𝑧;𝜃;𝜉,𝜎).Inthiscase,since𝜓ˆ |     |     |     |      |     |     |     |     |
(𝑦,𝑧;𝜃;𝜉,𝜎)isfeasiblefor(7),wemusthave
|     |     |     |     |     |     | 𝜄(𝑦,𝑧;𝜃) | <𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎). |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
DefinetheoptimalitygapasΛ(cid:66)𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎)−𝜄(𝑦,𝑧;𝜃).
Sincelim 𝑞→∞(𝑦 ,𝑧 ;𝜃 𝑞)=(𝑦,𝑧;𝜃),foranarbitrarysmallpositiverealnumber𝜖,wecanfindapositiveinteger𝑞suchthat
𝑞 𝑞
|     |     |            |           |                 | (cid:13) | 𝑦 𝑞−𝑦(cid:13) (cid:13)+ | (cid:13) 𝑧 𝑞−𝑧(cid:13) | (cid:13)+𝑑𝑖𝑠𝑡(𝜃,𝜃 | 𝑞)  | <𝜖, |     |     |     |     |
| --- | --- | ---------- | --------- | --------------- | -------- | ----------------------- | ---------------------- | ----------------- | --- | --- | --- | --- | --- | --- |
|     |     |            |           |                 | (cid:13) |                         | (cid:13)               |                   |     |     |     |     |     |     |
|     |     | 𝑝 (cid:12) | ′(cid:12) | 𝑝 + 𝐻−1(cid:13) |          | ′(cid:13) 𝑝 +           | 1(cid:12) ′(cid:12)    |                   |     |     |     |     |     |     |
where𝑑𝑖𝑠𝑡(𝜃,𝜃′)=(cid:205) (cid:12) 𝜇 𝑖 −𝜇 (cid:12)+(cid:205) (cid:13) 𝑤 𝑖 −𝑤 (cid:13)+(cid:205) (cid:12) 𝛿 𝑖 −𝛿 (cid:12) .Basedon𝑥 −𝐻+1:𝑝+𝐻−1 (cid:66)𝜓(𝑦,𝑧;𝜃),weconstructafeasiblesolution
|     |     | 𝑖 =0 | 𝑖   | 𝑖 = 0 |     | 𝑖 𝑖 = | 0 𝑖 |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑥 ′ (cid:67)𝑥′fortheoptimizationproblem(7)withparameters(𝑦 ,𝑧 ;𝜃 𝑞)asfollowing:Let𝑥 ′ =𝑥0:𝑝 ,𝑥 −𝐻+1:−1=𝑦,𝑥 𝑝+1:𝑝+𝐻−1=𝑧.
| − 𝐻+1:𝑝+𝐻−1 |     |     |     |     |     |     |     | 𝑞 𝑞 |     |     | 0 :𝑝 |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
For𝑡 =0,1,...,if𝑥 ′−𝑥 ′ <−𝛿 (𝑞),weincrease𝑥 ′suchthat𝑥 ′ =𝑥 ′ −𝛿 (𝑞).Then,for𝑡 =𝑝,𝑝−1,...,if𝑥 ′ −𝑥 ′ <−𝛿 ( 𝑞 ),wedecrease𝑥 ′
|     |     | 𝑡 𝑡 −1 | 𝑡   |     | 𝑡   |     | 𝑡 𝑡 −1 | 𝑡   |     |     |     | 𝑡 +1 𝑡 | 𝑡 + 1 | 𝑡   |
| --- | --- | ------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------ | ----- | --- |
𝑞
suchthat𝑥 ′ =𝑥 ′ +𝛿 ( ).Notethatthisprocedurecanguaranteethat𝑥′isafeasiblesolutionfor(7),andtheirdistanceareupperbounded
|     | 𝑡 𝑡 | +1 𝑡 + 1 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by
|     |     |     |     |     |     | (cid:13) 𝜓(𝑦,𝑧;𝜃)−𝑥′(cid:13) |     | (2𝑑+1)𝜖.  |     |     |     |     |     | (15) |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | (cid:13)                     |     | (cid:13)≤ |     |     |     |     |     |      |
Sincetheobjectivefunctionof (7)isLipschitzin(𝑥,𝑦,𝑧,𝜃),by(15),weknowthereexistssomepositiveconstant𝑐0 suchthat
𝜄(𝑦 ,𝑧 ;𝜃 𝑞)−𝜄(𝑦,𝑧;𝜃) ≤𝑐0 (cid:0)(cid:13) 𝑥′−𝜓(𝑦,𝑧;𝜃) (cid:13) (cid:13)+𝜖(cid:1) ≤ (2𝑑+2)𝑐0𝜖. (16)
|     |     |     |     | 𝑞 𝑞 |     |     | (cid:13) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Ontheotherhand,byLemmaB.3,weseethat
|                             |     |     |                                         | (cid:13) 𝜓ˆ |       | ;𝜉,𝜎)−𝜓ˆ |             |     | (cid:13) (cid:18) | 𝐶 (cid:19) |     |     |     |      |
| --------------------------- | --- | --- | --------------------------------------- | ----------- | ----- | -------- | ----------- | --- | ----------------- | ---------- | --- | --- | --- | ---- |
|                             |     |     |                                         | (cid:13)    | (𝑦 ,𝑧 | ;𝜃       | (𝑦,𝑧;𝜃;𝜉,𝜎) |     | (cid:13) ≤        | +1         | 𝜖.  |     |     | (17) |
|                             |     |     |                                         | (cid:13)    | 𝑞 𝑞   | 𝑞        |             |     | (cid:13) 1        | −𝜌         |     |     |     |      |
| Sincetheobjectivefunctionof |     |     | (7)issmoothin(𝑥,𝑦,𝑧,𝜃),by(17),weseethat |             |       |          |             |     |                   |            |     |     |     |      |
|                             |     |     |                                         |             |       |          |             |     | (cid:18)          | 𝐶 (cid:19) |     |     |     |      |
(cid:12) 𝜄ˆ(𝑦 ,𝑧 ;𝜃 ;𝜉,𝜎)−𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎) (cid:12) (cid:12)≤𝑐0 +2 𝜖. (18)
|     |     |     |     | (cid:12) | 𝑞 𝑞 | 𝑞   |     |     | 1−𝜌 |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore,weseethat
|     |     |     |     | (cid:12) |     |     |     | (cid:12) |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
𝜄ˆ(𝑦 𝑞 ,𝑧 𝑞 ;𝜃 𝑞 ;𝜉,𝜎)−𝜄(𝑦 𝑞 ,𝑧 𝑞 ;𝜃 𝑞) ≥ − 𝜄ˆ(𝑦 𝑞 ,𝑧 𝑞 ;𝜃 𝑞 ;𝜉,𝜎)−𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎) (cid:12)+(𝜄ˆ(𝑦,𝑧;𝜃;𝜉,𝜎)−𝜄(𝑦,𝑧;𝜃))+(𝜄(𝑦,𝑧;𝜃)−𝜄(𝑦 𝑞 ,𝑧 𝑞 ;𝜃 𝑞))
(cid:12)
|     |     |     |     |       | (cid:18) 𝐶 | (cid:19)         |     |     |     |     |     |     |     |       |
| --- | --- | --- | --- | ----- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |     | ≥ −𝑐0 |            | +2 𝜖+Λ−𝑐0(2𝑑+2)𝜖 |     |     |     |     |     |     |     | (19a) |
1−𝜌
|     |     |     |     |       | (cid:18) 𝐶 |       | (cid:19) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | =Λ−𝑐0 |            | +2𝑑+4 | 𝜖,       |     |     |     |     |     |     |     |
1−𝜌
|     |     |     |     |     | −1(cid:16) |     | (cid:17)−1 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
whereweused(16)and(18)in(19a).Let𝜖 (cid:66) 1 Λ𝑐 𝐶 +2𝑑+4 leadstoacontradictionwiththeassumptionthat𝜄ˆ(𝑦 ,𝑧 ;𝜃 ;𝜉,𝜎)=
|     |     |     |     |     | 2 0 | 1 −𝜌 |     |     |     |     |     |     | 𝑞 𝑞 | 𝑞   |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜄(𝑦 ,𝑧 ;𝜃 𝑞).Therefore,wehaveshownthat𝜓(𝑦,𝑧;𝜃)=𝜓ˆ (𝑦,𝑧;𝜃;𝜉,𝜎). □
𝑞 𝑞
Withtheabovetechnicallemmas,wearereadytofinishtheproofofTheoremB.1.
637

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
ProofofTheoremB.1. Considerthesegment((1−𝜂)𝑦+𝜂𝑦′,(1−𝜂)𝑧+𝜂𝑧′;(1−𝜂)𝜃+𝜂𝜃′),𝜂 ∈ [0,1].Notethatsince(1−𝜂)𝜓(𝑦,𝑧;𝜃)+
𝜂𝜓(𝑦′,𝑧′;𝜃′)isafeasiblesolutionfortheoptimizationproblem(7)parameterizedby
(cid:0)(1−𝜂)𝑦+𝜂𝑦′,(1−𝜂)𝑧+𝜂𝑧′;(1−𝜂)𝜃+𝜂𝜃′(cid:1),
weknowthatthecorrespondingoptimizationproblemisfeasible.Withsomeslightabuseofnotation,weuse(𝜉,𝜎)(𝜂) ⊆Ξ×Σtodenote
thesetofindicatorsofactiveconstraintsandsidessuchthat
𝜓 (cid:0)(1−𝜂)𝑦+𝜂𝑦′,(1−𝜂)𝑧+𝜂𝑧′;(1−𝜂)𝜃+𝜂𝜃′(cid:1)
=𝜓ˆ(cid:0)(1−𝜂)𝑦+𝜂𝑦′,(1−𝜂)𝑧+𝜂𝑧′;(1−𝜂)𝜃+𝜂𝜃′;𝜉,𝜎(cid:1),∀(𝜉,𝜎)
∈ (𝜉,𝜎)(𝜂).
| ByLemmaB.2,weknowthissetisnotemptyforany𝜂 |     |     |     |     |     | ∈   | [0,1]. |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
Wecandividetheinterval[0,1]into0=𝜂0 <𝜂1 <...<𝜂 =1forsomepositiveinteger𝑞 ≤25𝑝+6suchthatthereexistsasequenceof
𝑞
| differentindicatorsofactiveconstraintsandsides(𝜉,𝜎)0:𝑞−1 |     |     |             |             |     |                    | whichsatisfies |     |             |                    |          |     |
| -------------------------------------------------------- | --- | --- | ----------- | ----------- | --- | ------------------ | -------------- | --- | ----------- | ------------------ | -------- | --- |
|                                                          |     |     | (cid:0)(1−𝜂 |             |     | 𝑖(𝑦′,𝑧′;𝜃′)(cid:1) | =𝜓ˆ(cid:0)(1−𝜂 |     |             | 𝑖(𝑦′,𝑧′;𝜃′);(𝜉,𝜎)𝑖 | (cid:1), |     |
|                                                          |     |     | 𝜓           | 𝑖)(𝑦,𝑧;𝜃)+𝜂 |     |                    |                |     | 𝑖)(𝑦,𝑧;𝜃)+𝜂 |                    |          |     |
=𝜓ˆ(cid:0)(1−𝜂
|     |     |     | 𝜓 (cid:0)(1−𝜂 | 𝑖+1)(𝑦,𝑧;𝜃)+𝜂 |     | 𝑖+1(𝑦′,𝑧′;𝜃′)(cid:1) |     |     | 𝑖+1)(𝑦,𝑧;𝜃)+𝜂 | 𝑖+1(𝑦′,𝑧′;𝜃′);(𝜉,𝜎)𝑖 | (cid:1) |     |
| --- | --- | --- | ------------- | ------------- | --- | -------------------- | --- | --- | ------------- | -------------------- | ------- | --- |
forall0≤𝑖 ≤𝑞−1.Notethatthisrequires(𝜉,𝜎)(𝜂 𝑖)tocontainboth(𝜉,𝜎)𝑖−1 and(𝜉,𝜎)𝑖 for𝑖 =1,...,𝑞−1.Toconstructthesequence𝜂0:𝑞
| and(𝜉,𝜎)0:𝑞−1 | ,wefirsthave𝜂0=0andlet(𝜉,𝜎)0 |       |         |                                        |     | beanypair(𝜉,𝜎) |     | ∈ (𝜉,𝜎)(𝜂0)suchthat                               |     |     |     |     |
| ------------- | ---------------------------- | ----- | ------- | -------------------------------------- | --- | -------------- | --- | ------------------------------------------------- | --- | --- | --- | --- |
|               |                              |       |         | (cid:0)(1−𝜂)(𝑦,𝑧;𝜃)+𝜂(𝑦′,𝑧′;𝜃′)(cid:1) |     |                |     | =𝜓ˆ(cid:0)(1−𝜂)(𝑦,𝑧;𝜃)+𝜂(𝑦′,𝑧′;𝜃′);𝜉,𝜎(cid:1)}>0, |     |     |     |     |
|               |                              | sup{𝜂 | ∈ [0,1] | |𝜓                                     |     |                |     |                                                   |     |     |     |     |
andlet𝜂1 bethesupremumvalueabove.Since0=inf(0,1]and(𝜉,𝜎)(𝜂) ⊆Ξ×Σisnonemptyforevery𝜂 (0,1],weknowsuch(𝜉,𝜎)0
∈
existsbyLemmaB.4.Supposewehavealreadyconstructed𝜂0:𝑖 ,(𝜉,𝜎)0:𝑖−1 ,and𝜂 𝑖 <1.Thenweselect(𝜉,𝜎)𝑖 tobeanypair(𝜉,𝜎)suchthat
sup{𝜂 [0,1] |𝜓 (cid:0)(1−𝜂)(𝑦,𝑧;𝜃)+𝜂(𝑦′,𝑧′;𝜃′)(cid:1) =𝜓ˆ(cid:0)(1−𝜂)(𝑦,𝑧;𝜃)+𝜂(𝑦′,𝑧′;𝜃′);𝜉,𝜎(cid:1)}>𝜂 ,
|     |     |     | ∈   |     |     |     |     |     |     |     | 𝑖   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andlet𝜂 bethesupremumvalueabove.Wecanrepeatthisconstructionandstopwhen𝜂 𝑖+1=1.Bytheconstruction,weknowallpairs
𝑖+1
inthesequence(𝜉,𝜎)0:𝑖−1 aredistinct,thustheconstructionwillterminateinfinitetime.Hence,wehaveafiniteindex𝑞suchthat𝜂 =1.
𝑞
ByLemmaB.3,weknowthat
| (cid:13) 𝜓 (cid:0)(1−𝜂 | 𝑖)(𝑦,𝑧;𝜃)+𝜂 |     | 𝑖(𝑦′,𝑧′;𝜃′)(cid:1) |     | −𝜓 (cid:0)(1−𝜂 | 𝑖+1)(𝑦,𝑧;𝜃)+𝜂 |     | 𝑖+1(𝑦′,𝑧′;𝜃′)(cid:1) | (cid:13)   |       |     |     |
| ---------------------- | ----------- | --- | ------------------ | --- | -------------- | ------------- | --- | -------------------- | ---------- | ----- | --- | --- |
| (cid:13)               |             |     |                    | 𝑡   |                |               |     |                      | 𝑡 (cid:13) |       |     |     |
|                        |             |     |                    |     |                |               | 𝑝   |                      |            | 𝑝+𝐻−1 | 𝑝+1 |     |
|                        |             |     |                    |     |                |               | ∑︁  |                      |            | ∑︁    | ∑︁  |     |
≤ (𝜂 𝑖+1−𝜂 𝑖)𝐶(cid:0)𝜌𝑡(cid:13) 𝑦−𝑦′(cid:13) (cid:13)+𝜌𝑝−𝑡(cid:13) 𝑧−𝑧′(cid:13) (cid:1)+(𝜂 𝑖+1−𝜂 𝑖)𝐶(cid:169) 𝜌|𝑡−𝜏|(cid:12) 𝜇 −𝜇 ′(cid:12) (cid:12)+ 𝜌|𝑡−𝜏|(cid:13) 𝑤 −𝑤 ′(cid:13) (cid:13)+ 𝜌|𝑡−𝜏|(cid:13) 𝛿 −𝛿 ′(cid:13) (cid:13)(cid:170) . (20)
(cid:13) (cid:13) (cid:13) (cid:173) (cid:12) 𝜏 𝜏 (cid:13) 𝜏 𝜏 (cid:13) 𝜏 𝜏 (cid:174)
|                  |     |                               |     |     |     |     | 𝜏=0       |     |     | 𝜏=0 | 𝜏=0 |           |
| ---------------- | --- | ----------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --------- |
|                  |     |                               |     |     |     |     | (cid:171) |     |     |     |     | (cid:172) |
| Summing(20)over𝑖 |     | =0,1,...,𝑞−1finishestheproof. |     |     |     |     |           |     |     |     |     | □         |
C PROOFSFOREXACTPREDICTIONS
C.1 ProofofLemmaA.4
Tosimplifythenotation,weintroducetheshorthand
|                    |     |     | 𝑥 ∗                                  | =𝜓 𝑁 ((𝑥 | 𝑡−1,𝑢 𝑡−1);𝜔 |     | ;0)𝑥𝜏 ,𝑢 | ∗ =𝜓 𝑁 | ((𝑥 𝑡−1,𝑢 | 𝑡−1);𝜔 ;0)𝑢𝜏 ,∀𝜏 | ≥𝑡. |     |
| ------------------ | --- | --- | ------------------------------------ | -------- | ------------ | --- | -------- | ------ | --------- | ---------------- | --- | --- |
|                    |     |     | 𝜏 |𝑡                                 | 𝑡        |              | 𝑡:𝑁 |          | 𝜏 |𝑡 𝑡 |           | 𝑡:𝑁              |     |     |
| Andweuse{(𝑥∗,𝑢∗)}𝑁 |     |     | todenotetheofflineoptimaltrajectory. |          |              |     |          |        |           |                  |     |     |
𝑡 𝑡 𝑡=1
| Fortimestep𝑡 |     | −𝐾+1,weseethat |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<𝑁
|     |     |     | (cid:12)                  |           |                 |              | (cid:12) 2 |                    |     |                   |                              |       |
| --- | --- | --- | ------------------------- | --------- | --------------- | ------------ | ---------- | ------------------ | --- | ----------------- | ---------------------------- | ----- |
|     |     |     | (cid:12) 𝑥 −𝜓 𝑁           | ((𝑥 𝑡−1,𝑢 | 𝑡−1);𝜔          | ;0)𝑥𝑡        | (cid:12)   |                    |     |                   |                              |       |
|     |     |     | (cid:12) 𝑡 𝑡              |           | 𝑡:𝑁             |              | (cid:12)   |                    |     |                   |                              |       |
|     |     |     | (cid:18)                  |           |                 | (cid:12)     |            | (cid:12) (cid:19)2 |     |                   |                              |       |
|     |     |     | 𝐶𝜌𝐾(cid:12)               |           | (cid:12) +𝐶𝜌𝐾−1 | (cid:12)     |            | 1 (cid:12)         |     |                   |                              |       |
|     |     | ≤   | (cid:12) 𝑥 ∗              | −𝑥¯       | (cid:12)        | (cid:12) 𝑢 ∗ | −          | (cid:12)           |     |                   |                              | (21a) |
|     |     |     | (cid:12) 𝑡                | +𝐾|𝑡      | (cid:12)        | 𝑡 +𝐾−1|𝑡     | 𝜔          |                    |     |                   |                              |       |
|     |     |     |                           |           |                 | (cid:12)     |            | 𝑡+ 𝐾−1 (cid:12)    |     |                   |                              |       |
|     |     |     | (cid:18) (cid:16)(cid:12) |           | (cid:12)        |              | (cid:17)   | (cid:18)(cid:12)   |     | (cid:12) (cid:12) | 1 (cid:12) (cid:19)(cid:19)2 |       |
𝐶𝜌𝐾 (cid:12) 𝑥 ∗ −𝑥 ∗ (cid:12) (cid:12) 𝑥 ∗ −𝑥¯(cid:12) +𝐶𝜌𝐾−1 (cid:12) 𝑢 ∗ −𝑢 ∗ (cid:12) (cid:12) 𝑢 ∗ (cid:12) (21b)
|     |     | ≤               | (cid:12) | 𝑡 +𝐾|𝑡   | 𝑡 +𝐾 (cid:12) + (cid:12)     | 𝑡 +𝐾      | (cid:12)          | (cid:12) 𝑡 +𝐾−1|𝑡 |                          | 𝑡 +𝐾−1 (cid:12) + (cid:12) 𝑡 +𝐾−1 | − (cid:12)        |     |
| --- | --- | --------------- | -------- | -------- | ---------------------------- | --------- | ----------------- | ----------------- | ------------------------ | --------------------------------- | ----------------- | --- |
|     |     |                 |          |          |                              |           |                   |                   |                          | (cid:12)                          | 𝜔 𝑡+ 𝐾−1 (cid:12) |     |
|     |     | ≤4𝐶2𝜌2𝐾(cid:12) |          |          | (cid:12) 2 +4𝐶2𝜌2𝐾−2(cid:12) |           |                   |                   | (cid:12) 2               |                                   |                   |     |
|     |     |                 | (cid:12) | 𝑥 ∗ −𝑥   | ∗ (cid:12)                   |           | (cid:12) 𝑢 ∗      | −𝑢 ∗              | (cid:12) +4𝐶2𝜌2𝐾(cid:12) | 𝑥 ∗ −𝑥¯(cid:12)                   | 2 +               |     |
|     |     |                 | (cid:12) | 𝑡 +𝐾|𝑡   | 𝑡 +𝐾 (cid:12)                |           | (cid:12) 𝑡 +𝐾−1|𝑡 | 𝑡                 | +𝐾−1 (cid:12)            | (cid:12) 𝑡 +𝐾−1                   | (cid:12)          |     |
|     |     |                 |          | (cid:12) |                              | (cid:12)2 |                   |                   |                          |                                   |                   |     |
1
|     |     |     | +4𝐶2𝜌2𝐾−2(cid:12) | 𝑢 ∗             | −     | (cid:12) | .   |     |     |     |     | (21c) |
| --- | --- | --- | ----------------- | --------------- | ----- | -------- | --- | --- | --- | --- | --- | ----- |
|     |     |     |                   | (cid:12) 𝑡 +𝐾−1 | 𝜔     | (cid:12) |     |     |     |     |     |       |
|     |     |     |                   | (cid:12)        | 𝑡+𝐾−1 | (cid:12) |     |     |     |     |     |       |
638

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
wherein(21a),weuse
(cid:18) 1 (cid:19)
𝑥 𝑡 =𝜓 𝑡 𝑡+𝐾−1 (𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑡+𝐾−1 ;(𝑥¯, 𝜔 ) ,
𝑡+𝐾−1 𝑥𝑡
𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑥𝑡 =𝜓 𝑡 𝑡+𝐾−1(cid:16) (𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑡+𝐾−1 ;(𝑥 𝑡 ∗ +𝐾|𝑡 ,𝑢 𝑡 ∗ +𝐾−1|𝑡 ) (cid:17) 𝑥𝑡 ,
andtheexponentiallydecayingperturbationbound.Weusethetriangleinequalityin(21b)andrearrangethetermsin(21c).
Wenotethatforthefirsttermin(21),wehave
(cid:12) (cid:12) (cid:12) 𝑥 𝑡 ∗ +𝐾|𝑡 −𝑥 𝑡 ∗ +𝐾 (cid:12) (cid:12) (cid:12) ≤𝐶𝜌𝐾+1(cid:0)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12)+ (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) (cid:1). (22)
Forthesecondterm,wehave
(cid:12) (cid:12) (cid:12) 𝑢 𝑡 ∗ +𝐾−1|𝑡 −𝑢 𝑡 ∗ +𝐾−1 (cid:12) (cid:12) (cid:12) ≤𝐶′𝜌𝐾 (cid:0)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12)+ (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) (cid:1). (23)
Forthethirdterm,wehave
(cid:12) (cid:12) 𝑥 𝑡 ∗ +𝐾 −𝑥¯(cid:12) (cid:12) 2 ≤ 𝜖 1 𝛽 𝑏(𝑥 𝑡 ∗ +𝐾 ). (24)
Forthelastterm,weseethat
(cid:12) 1 (cid:12)2 (𝑥∗ −𝑥∗ )2 2(𝑥∗ −𝑥¯)2+2(𝑥¯−𝑥∗ )2 2𝑏(𝑥∗ )+2𝑏(𝑥∗ )
(cid:12) (cid:12) (cid:12) 𝑢 𝑡 ∗ +𝐾−1 − 𝜔 𝑡+𝐾−1 (cid:12) (cid:12) (cid:12) ≤ 𝑡+𝐾− 𝜔 1 𝑡 2 +𝐾− 𝑡 1 +𝐾−2 ≤ 𝑡+𝐾−1 𝜔 𝑡 2 +𝐾−1 𝑡+𝐾−2 ≤ 𝑡+𝐾− 𝜖 1 𝛽𝜔 m 2 in 𝑡+𝐾−2 . (25)
Substituting(22),(23),(24),(25)into(21)givesthat
(cid:12) (cid:12) (cid:12) 𝑥 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12) 2 ≤8𝐶4𝜌4𝐾+2(cid:16)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) 2(cid:17) +8(𝐶′) 2𝐶2𝜌4𝐾−2(cid:16)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) 2(cid:17)
(2+𝜔2 )𝑏(𝑥∗ )+2𝑏(𝑥∗ )
+4𝐶2𝜌2𝐾−2 min 𝑡+𝐾−1 𝑡+𝐾−2 (26)
𝜖𝛽𝜔2
min
Similarly,wecanobtainthat
(cid:12) (cid:12) (cid:12) 𝑢 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12) 2 ≤8(𝐶′) 2𝐶2𝜌4𝐾+2(cid:16)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) 2(cid:17) +8(𝐶′) 4𝜌4𝐾−2(cid:16)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) 2(cid:17)
(2+𝜔2 )𝑏(𝑥∗ )+2𝑏(𝑥∗ )
+4(𝐶′) 2𝜌2𝐾−2 min 𝑡+𝐾−1 𝑡+𝐾−2 (27)
𝜖𝛽𝜔2
min
Therefore,combining(26)and(27)givesthat
𝑒 𝑡 2 ≤2 (cid:12) (cid:12) (cid:12) 𝑥 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12) 2 +2 (cid:12) (cid:12) (cid:12) 𝑢 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12) 2
≤16𝜌4𝐾−2(cid:16) 𝐶2 +(𝐶′) 2(cid:17)2(cid:16)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) 2(cid:17) +8𝜌2𝐾−2(cid:16) 𝐶2 +(𝐶′) 2(cid:17) (2+𝜔 m 2 in )𝑏(𝑥 𝑡 ∗ 𝜖 + 𝜔 𝐾 2 −1 )+2𝑏(𝑥 𝑡 ∗ +𝐾−2 ) .
min
C.2 ProofofLemmaA.5
Weseethedistancebetweenthetrajectoriesof SODAandtheofflineoptimalatanintermediatetimestepcanbeboundedby
(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12)+ (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12)= (cid:12) (cid:12) (cid:12) 𝑥 𝑡 −𝜓 1 𝑁 ((𝑥0,𝑢0);𝜔 1:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12) + (cid:12) (cid:12) (cid:12) 𝑢 𝑡 −𝜓 1 𝑁 ((𝑥0,𝑢0);𝜔 1:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12)
≤ (cid:12) (cid:12) (cid:12) 𝑥 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12) + (cid:12) (cid:12) (cid:12) 𝑢 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12)
𝑡−1
+ ∑︁(cid:12) (cid:12) (cid:12) 𝜓 𝜏 𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔 𝜏:𝑁 ;0)𝑥𝑡 −𝜓 𝜏 𝑁 +1 ((𝑥 𝜏 ,𝑢 𝜏);𝜔 𝜏+1:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12)
𝜏=1
𝑡−1
+ ∑︁(cid:12) (cid:12) (cid:12) 𝜓 𝜏 𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔 𝜏:𝑁 ;0)𝑢𝑡 −𝜓 𝜏 𝑁 +1 ((𝑥 𝜏 ,𝑢 𝜏);𝜔 𝜏+1:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12) (28a)
𝜏=1
𝑡−1
≤𝑒
𝑡
+(𝐶+𝐶′) ∑︁ 𝜌𝑡−𝜏𝑒
𝜏
. (28b)
𝜏=1
639

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
Weusethetriangleinequalityin(28a).In(28b),wenotethat𝜓
𝜏
𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔
𝜏:𝑁
;0)𝑥𝑡 canbewrittenas𝜓
𝜏
𝑁
+1
(cid:16) (𝑥
𝜏
∗
|𝜏−1
,𝑢
𝜏
∗
|𝜏−1
);𝜔
𝜏+1:𝑁
;0 (cid:17)
𝑥𝑡
,
where
𝑥
𝜏
∗
|𝜏−1
=𝜓
𝜏
𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔
𝜏:𝑁
;0)𝑥𝜏 , and𝑢
𝜏
∗
|𝜏−1
=𝜓
𝜏
𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔
𝜏:𝑁
;0)𝑢𝜏 .
Thus,wecanapplytheexponentiallydecayingperturbationboundandLemmaA.4toobtain
(cid:12) (cid:12) (cid:12) 𝜓 𝜏 𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔 𝜏:𝑁 ;0)𝑥𝑡 −𝜓 𝜏 𝑁 +1 ((𝑥 𝜏 ,𝑢 𝜏);𝜔 𝜏+1:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12) ≤𝐶𝜌𝑡−𝜏𝑒 𝜏 .
Similarly,weobtainthat
(cid:12) (cid:12) (cid:12) 𝜓 𝜏 𝑁 ((𝑥 𝜏−1,𝑢 𝜏−1);𝜔 𝜏:𝑁 ;0)𝑢𝑡 −𝜓 𝜏 𝑁 +1 ((𝑥 𝜏 ,𝑢 𝜏);𝜔 𝜏+1:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12) ≤𝐶′𝜌𝑡−𝜏𝑒 𝜏 .
Therefore,weseethat
(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2 ≤ (cid:18) 1+ (𝐶 1 + − 𝐶 𝜌 ′)2(cid:19) ∑︁ 𝑡 𝜌𝑡−𝜏𝑒 𝜏 2.
𝜏=1
Summingtheaboveinequalityover𝑡 =1,2,...,𝑇 givesthat
∑︁ 𝑁 (cid:16)(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2(cid:17) ≤ 1− 1 𝜌 · (cid:18) 1+ (𝐶 1 + − 𝐶 𝜌 ′)2(cid:19) ∑︁ 𝑁 𝑒 𝑡 2.
𝑡=1 𝑡=1
C.3 ProofofTheoremA.3
CombiningLemmasA.4andA.5,weseethat
∑︁ 𝑁 (cid:16)(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2(cid:17) ≤ 1− 1 𝜌 · (cid:18) 1+ (𝐶 1 + − 𝐶 𝜌 ′)2(cid:19) ·16𝜌4𝐾−2(cid:16) 𝐶2 +(𝐶′) 2(cid:17)2∑︁ 𝑁 (cid:16)(cid:12) (cid:12) 𝑥 𝑡−1−𝑥 𝑡 ∗ −1 (cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡−1−𝑢 𝑡 ∗ −1 (cid:12) (cid:12) 2(cid:17)
𝑡=1 𝑡=1
+ 1 · (cid:18) 1+ (𝐶+𝐶′)2(cid:19) ·8𝜌2𝐾−2(cid:16) 𝐶2 +(𝐶′) 2(cid:17) (4+𝜔 m 2 in )(cid:205) 𝑡 𝑁 =1 𝑏(𝑥 𝑡 ∗) . (29)
1−𝜌 1−𝜌 𝜖𝛽𝜔2
min
Sincethepredictionhorizon𝐾 satisfies
𝐾 ≥ 1 ln (cid:18) 16 · (cid:18) 1+ (𝐶+𝐶′)2(cid:19) · (cid:16) 𝐶2 +(𝐶′) 2(cid:17)2(cid:19) /ln (cid:18)1(cid:19) ,
4 1−𝜌 1−𝜌 𝜌
weseethat
∑︁ 𝑁 (cid:16)(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2(cid:17) ≤ 16 1 𝜌 − 2𝐾 𝜌 −2 · (cid:18) 1+ (𝐶 1 + − 𝐶 𝜌 ′)2(cid:19)(cid:16) 𝐶2 +(𝐶′) 2(cid:17) (4+𝜔 m 2 i 𝜖 n 𝜔 ) 2 (cid:205) 𝑡 𝑁 =1 𝑏(𝑥 𝑡 ∗) . (30)
𝑡=1 min
Ontheotherhand,wealsoseethatforany𝜂 >0,wehave
𝑁
cost(SODA)= ∑︁ 𝜔 𝑡 𝑢 𝑡 2 +𝑏(𝑥 𝑡)+𝛾(𝑢 𝑡 −𝑢 𝑡−1) 2
𝑡=1
𝑁 𝑁
= ∑︁ 𝜔 𝑡(𝑢 𝑡 ∗+(𝑢 𝑡 −𝑢 𝑡 ∗)) 2 + ∑︁ 𝑏(𝑥 𝑡 ∗+(𝑥 𝑡 −𝑥 𝑡 ∗))
𝑡=1 𝑡=1
𝑁
+ ∑︁ 𝛾(𝑢 𝑡 ∗−𝑢 𝑡 ∗ −1 +(𝑢 𝑡 −𝑢 𝑡 ∗)−(𝑢 𝑡−1−𝑢 𝑡 ∗ −1 )) 2
𝑡=1
𝑁
≤ (1+𝜂) ∑︁(cid:16) 𝜔 𝑡(𝑢 𝑡 ∗) 2 +𝑏(𝑥 𝑡 ∗)+𝛾(𝑢 𝑡 ∗−𝑢 𝑡 ∗ −1 ) 2(cid:17)
𝑡=1
+ (cid:18) 1+ 𝜂 1(cid:19) ∑︁ 𝑁 (cid:16) 𝜔 𝑡(𝑢 𝑡 ∗−𝑢 𝑡) 2 +𝛽(𝑥 𝑡 ∗−𝑥 𝑡) 2 +2𝛾(𝑢 𝑡 ∗−𝑢 𝑡) 2 +2𝛾(𝑢 𝑡 ∗ −1 −𝑢 𝑡−1) 2(cid:17) (31a)
𝑡=1
≤ (1+𝜂)cost(OPT)+ (cid:18) 1+ 𝜂 1(cid:19) (4𝛾+𝛽+𝜔max) ∑︁ 𝑁 (cid:16)(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2(cid:17) , (31b)
𝑡=1
whereweusethequadraticformofthecostfunctionsandtheAM-GMinequalityin(31a);weuse(30)in(31b).
640

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
Substituting(30)into(31)givesthat
cost(SODA)−cost(OPT) ≤ (cid:32) 𝜂+ (cid:18) 1+
𝜂
1(cid:19) (4𝛾+𝛽+𝜔max)· 16
1
𝜌
−
2𝐾
𝜌
−2 · (cid:18) 1+ (𝐶
1
+
−
𝐶
𝜌
′)2(cid:19)(cid:16) 𝐶2 +(𝐶′) 2(cid:17) · 4
𝜖
+
𝛽𝜔
𝜔
2
m 2 in (cid:33) cost(OPT).
min
Letting𝜂 =4 (cid:18) 2(4𝛾+𝛽+𝜔max)·
1−
1
𝜌
· (cid:16) 1+ (𝐶
1
+
−
𝐶
𝜌
′)2(cid:17) (cid:0)𝐶2+(𝐶′)2(cid:1)·
𝜖
4+
𝛽
𝜔
𝜔
m 2
2
in (cid:19)1/2 finishestheproof.
min
D PROOFSFORINEXACTPREDICTIONS
D.1 ProofofLemmaA.6
Suppose{𝑥 𝑡}1≤𝑡≤𝑁 isafeasibletrajectoryofthebufferlevelsand{𝑥 𝑡}𝑡1≤𝑡≤𝑡2 isasub-trajectorysuchthat𝑥 𝑡1−1 ≥𝑥¯−𝜁,𝑥 𝑡 <𝑥¯−𝜁,∀𝑡 =
𝑡1,...,𝑡2 ,and𝑥 𝑡2+1 ≥𝑥¯−𝜁 where1≤𝑡1 <𝑡2 <𝑁.
For𝜆 ≥0,considerthetrajectory{𝑥
𝑡
′(𝜆)}1≤𝑡≤𝑁 constructedby
(cid:40)
𝑥
𝑡
′(𝜆)=
𝑥
𝑥
𝑡
𝑡
,
+𝜆,
i
o
f
t
𝑡
he
<
rw
𝑡1
is
o
e
r
.
𝑡 >𝑡2
Notethatunderthisconstruction,{𝑥
𝑡
′(0)}1≤𝑡≤𝑁 isidenticalwiththeoriginaltrajectory{𝑥 𝑡}1≤𝑡≤𝑁 .LetΥ(𝜆)denotethetotalcostofthis
trajectory.Forsufficientlysmall𝜆 ≥0,weseethat
Υ(𝜆)−Υ(0)=𝛽 ∑︁
𝑡2
(cid:16) (𝑥 𝑡 +𝜆−𝑥¯) 2 −(𝑥 𝑡 −𝑥¯) 2(cid:17) +𝜔 𝑡1 (cid:16) 𝑢 𝑡 ′ 1 (𝜆) 2 −𝑢 𝑡 2 1 (cid:17) +𝜔 𝑡2+1 (cid:16) 𝑢 𝑡 ′ 2+1 (𝜆) 2 −𝑢 𝑡 2 2+1 (cid:17)
𝑡=𝑡1
+𝛾 (cid:16) (𝑢 𝑡 ′ 1 (𝜆)−𝑢 𝑡1−1) 2 −(𝑢 𝑡1 −𝑢 𝑡1−1) 2(cid:17) +𝛾 (cid:16) (𝑢 𝑡1+1−𝑢 𝑡 ′ 1 (𝜆)) 2 −(𝑢 𝑡1+1−𝑢 𝑡1 ) 2(cid:17)
+𝛾 (cid:16) (𝑢 𝑡 ′ 2+1 (𝜆)−𝑢 𝑡2 ) 2 −(𝑢 𝑡2+1−𝑢 𝑡2 ) 2(cid:17) +𝛾 (cid:16) (𝑢 𝑡2+2−𝑢 𝑡 ′ 2+1 (𝜆)) 2 −(𝑢 𝑡2+2−𝑢 𝑡2+1) 2(cid:17) ,
where𝑢 𝑡 ′ 1 (𝜆)=𝑢 𝑡1 + 𝜔 𝜆 𝑡1 and𝑢 𝑡 ′ 2+1 (𝜆)=𝑢 𝑡2+1− 𝜔𝑡 𝜆 2+1 .
Therefore,weseethat
𝑑 (cid:12) 𝑑 (cid:12)
Υ(𝜆) (cid:12) (cid:12) = (Υ(𝜆)−Υ(0)) (cid:12) (cid:12)
𝑑𝜆 (cid:12)𝜆=0+ 𝑑𝜆 (cid:12)𝜆=0+
∑︁
𝑡2
2𝛾 2𝛾
=2𝛽
𝑡=𝑡1
(𝑥 𝑡 −𝑥¯)+2𝑢 𝑡1 −2𝑢 𝑡2+1+
𝜔 𝑡1
(2𝑢 𝑡1 −𝑢 𝑡1−1−𝑢 𝑡1+1)+
𝜔 𝑡2+1
(−2𝑢 𝑡2+1+𝑢 𝑡2 +𝑢 𝑡2+2)
(cid:18) 8𝛾 (cid:19)(cid:18) 1 1 (cid:19)
< −2𝛽𝜁 + 2+ − ≤0.
𝜔
min
𝑟
min
𝑟max
Thus,weknowthatthereexists𝜆>0suchthat{𝑥
𝑡
′(𝜆)}1≤𝑡≤𝑁 isfeasibleandΥ(𝜆)islessthanthetotalcostof{𝑥 𝑡}1≤𝑡≤𝑁 .Therefore,the
offlineoptimaltrajectorycannotcontainasub-trajectorysuchthat𝑥 𝑡1−1 ≥ 𝑥¯−𝜁,𝑥 𝑡 < 𝑥¯−𝜁,∀𝑡 = 𝑡1,...,𝑡2 ,and𝑥 𝑡2+1 ≥ 𝑥¯−𝜁 where
1≤𝑡1 <𝑡2 <𝑁.Usingsimilartechniques,wecanextendthisclaimtoinclude𝑡2=𝑁 and/or𝑡1=𝑡2 .Thus,thebufferlevelsintheoffline
optimaltrajectorydonotgobelow𝑥¯−𝜁.Bysymmetry,wecanshowthattheofflineoptimaltrajectoryalsodoesnotexceed𝑥¯+𝜁.
D.2 ProofofLemmaA.7
Tosimplifythenotation,weintroducetheshorthand
𝑥
𝜏
∗
|𝑡
=𝜓
𝑡
𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔
𝑡:𝑁
;0)𝑥𝜏 ,𝑢
𝜏
∗
|𝑡
=𝜓
𝑡
𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔
𝑡:𝑁
;0)𝑢𝜏 ,∀𝜏 ≥𝑡.
Andweuse{(𝑥∗,𝑢∗)}todenotetheofflineoptimaltrajectory.
𝑡 𝑡
Fortimestep𝑡 <𝑁 −𝐾+1,weseethat
(cid:12) (cid:12) (cid:12) 𝑥 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑥𝑡 (cid:12) (cid:12) (cid:12) ≤𝐶𝜌𝐾(cid:12) (cid:12) (cid:12) 𝑥 𝑡 ∗ +𝐾|𝑡 −𝑥¯ (cid:12) (cid:12) (cid:12) +𝐶𝜌𝐾−1 (cid:12) (cid:12) (cid:12) (cid:12) 𝑢 𝑡 ∗ +𝐾−1|𝑡 − 𝜔 𝑡+ 1 𝐾−1 (cid:12) (cid:12) (cid:12) (cid:12) +𝐶 𝑡+ ∑︁ 𝜏 𝐾 =𝑡 −1 𝜌𝜏−𝑡(cid:12) (cid:12) 𝜔ˆ 𝜏|𝑡−1−𝜔 𝜏 (cid:12) (cid:12)+ (cid:12) (cid:12) 𝜔 𝑡 − 𝑟 m 𝜔ˆ in 𝑡|𝑡−1 (cid:12) (cid:12) (32a)
≤𝐶𝜌𝐾 (cid:18) 𝑥max+ 1 − 1 (cid:19) +𝐶·𝐸(𝑡−1,𝐾)+ (cid:12) (cid:12) 𝜔 𝑡 −𝜔ˆ 𝑡|𝑡−1 (cid:12) (cid:12) , (32b)
𝑟
min
𝑟max 𝑟
min
641

ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia Chenetal.
wherein(32a),weusethefactsthat
(cid:18) 1 (cid:19)
𝑥 𝑡 =𝜓 𝑡 𝑡+𝐾−1 (𝑥 𝑡−1,𝑢 𝑡−1);𝜔ˆ 𝑡:𝑡+𝐾−1|𝑡−1 ;(𝑥¯, 𝜔 ) +(𝜔 𝑡 −𝜔ˆ 𝑡|𝑡−1)𝑢 𝑡 ,
𝑡+𝐾−1 𝑥𝑡
𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑥𝑡 =𝜓 𝑡 𝑁 (cid:16) (𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑡+𝐾−1 ;(𝑥 𝑡 ∗ +𝐾|𝑡 ,𝑢 𝑡 ∗ +𝐾−1|𝑡 ) (cid:17) 𝑥𝑡 ,
andapplytheexponentiallydecayingperturbationbound.In(32b),weapplytheworst-caseboundforthefirsttwotermsandusethe
definitionof𝐸 𝑡−1(𝐾).
Notethatwecanshow(32)alsoholdsfor𝑡 ≥𝑁 −𝐾+1withthesameapproach.
Similarly,wecanshowthat
(cid:12) (cid:12) (cid:12) 𝑢 𝑡 −𝜓 𝑡 𝑁 ((𝑥 𝑡−1,𝑢 𝑡−1);𝜔 𝑡:𝑁 ;0)𝑢𝑡 (cid:12) (cid:12) (cid:12) ≤𝐶′𝜌𝐾 (cid:18) 𝑥max+ 𝑟 m 1 in − 𝑟m 1 ax (cid:19) +𝐶′·𝐸(𝑡−1,𝐾). (33)
Combining(32)and(33)finishestheproofofLemmaA.7.
D.3 ProofofTheoremA.8
WefirstuseinductiontoshowthatSODA’sentiretrajectorysatisfiesthebufferlevelconstraintsstrictly.Toseethis,notethatfor𝑡 =1,we
have
(cid:12) (cid:12) 𝑥1−𝑥 1 ∗(cid:12) (cid:12)≤𝑒1 ≤𝐶𝜌𝐾 (cid:18) 𝑥max+ 𝑟 m 1 in − 𝑟m 1 ax (cid:19) +𝐶·𝐸(𝑡−1,𝐾)+ (cid:12) (cid:12) 𝜔 𝑡 − 𝑟 m 𝜔ˆ in 𝑡|𝑡−1 (cid:12) (cid:12) ≤ 𝐷 3 .
ByLemmaA.6,weknowthat(cid:12) (cid:12) 𝑥 1 ∗−𝑥¯(cid:12) (cid:12)≤ 𝐷 3 .Thus,wehave
2𝐷
|𝑥1−𝑥¯| ≤ (cid:12) (cid:12) 𝑥1−𝑥 1 ∗(cid:12) (cid:12)+ (cid:12) (cid:12) 𝑥 1 ∗−𝑥¯(cid:12) (cid:12)≤ 3 .
Therefore,weseethat0<𝑥1 <𝑥max .Supposingthat0<𝑥
𝜏
<𝑥max holdsfor𝜏 =1,...,𝑡−1,weseethat
𝑡−1
(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12)+ (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12)≤𝑒 𝑡 +(𝐶+𝐶′) ∑︁ 𝜌𝑡−𝜏𝑒 𝜏 (34a)
𝜏=1
≤ (1+𝐶+𝐶′)2 (cid:18) 𝑥max+ 1 − 1 (cid:19) ·𝜌𝐾 + (cid:18) 1+ 1 +𝐶+𝐶′ (cid:19)2 ∑︁ 𝑡 𝜌𝑡−𝜏𝐸(𝜏−1,𝐾), (34b)
1−𝜌 𝑟
min
𝑟max 𝑟
min 𝜏=1
In(34a),weuse(28)intheproofofLemmaA.5.WeuseLemmaA.7in(34b).
Thus,weobtainthat(cid:12) (cid:12) 𝑥 𝑡 ∗−𝑥 𝑡 (cid:12) (cid:12)≤ 𝐷 3 .ByLemmaA.6,weseethat
2𝐷
|𝑥 𝑡 −𝑥¯| ≤ (cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12)+ (cid:12) (cid:12) 𝑥 𝑡 ∗−𝑥¯(cid:12) (cid:12)≤ 3 .
Therefore,wehaveshownthat0<𝑥
𝑡
<𝑥max holdsforalltimesteps𝑡 byinduction.
By(34),weseethat
(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2 ≤ (cid:16) 1+ 𝑟m 1 i 1 n − +𝐶 𝜌 +𝐶′ (cid:17)4 (cid:18) 1+𝑥max+ 𝑟 m 1 in − 𝑟m 1 ax (cid:19) ·
(cid:32) 1 (cid:18) 𝑥max+ 1 − 1 (cid:19) ·𝜌2𝐾 + ∑︁ 𝑡 𝜌𝑡−𝜏𝐸(𝜏−1,𝐾) 2 (cid:33) . (35)
1−𝜌 𝑟
min
𝑟max
𝜏=1
Therefore,bysumming(35)over𝑡,weobtainthat
∑︁ 𝑡 𝑁 =1 (cid:16)(cid:12) (cid:12) 𝑥 𝑡 −𝑥 𝑡 ∗(cid:12) (cid:12) 2 + (cid:12) (cid:12) 𝑢 𝑡 −𝑢 𝑡 ∗(cid:12) (cid:12) 2(cid:17) ≤ (cid:16) 1+ 𝑟m ( 1 1 in − + 𝜌 𝐶 )2 +𝐶′ (cid:17)4 (cid:18) 1+𝑥max+ 𝑟 m 1 in − 𝑟m 1 ax (cid:19) · (cid:32)(cid:18) 𝑥max+ 𝑟 m 1 in − 𝑟m 1 ax (cid:19) ·𝑁𝜌2𝐾 + 𝑁 ∑︁ 𝑡= − 0 1 𝐸(𝑡,𝐾) 2 (cid:33) . (36)
642

SODA:AnAdaptiveBitrateControllerforConsistentHigh-QualityVideoStreaming ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia
| By(31),weseethatforany𝜂 |     |            | >0,wehave |                   |     |          |             |     |                     |             |                              |     |
| ----------------------- | --- | ---------- | --------- | ----------------- | --- | -------- | ----------- | --- | ------------------- | ----------- | ---------------------------- | --- |
|                         |     |            |           |                   |     | (cid:18) | 1(cid:19)   |     | 𝑁                   |             |                              |     |
|                         |     |            |           |                   |     |          |             |     | ∑︁ (cid:16)(cid:12) | ∗(cid:12) 2 | (cid:12) ∗(cid:12) 2(cid:17) |     |
|                         |     | cost(SODA) |           | ≤ (1+𝜂)cost(OPT)+ |     | 1+       | (4𝛾+𝛽+𝜔max) |     | (cid:12) 𝑥 𝑡        | −𝑥 (cid:12) | + (cid:12) 𝑢 𝑡 −𝑢 (cid:12)   |     |
|                         |     |            |           |                   |     |          | 𝜂           |     |                     | 𝑡           | 𝑡                            |     |
𝑡=1
|     |     |     |     |                   |     | (cid:18) | 1(cid:19)    |     |     |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |     | ≤ (1+𝜂)cost(OPT)+ |     | 1+       | (4𝛾+𝛽+𝜔max)· |     |     |     |     |     |
𝜂
(cid:17)4
|     |     |     |     | (cid:16) 1+      | 1 𝐶     | +𝐶′  |          |           |          |     |     |     |
| --- | --- | --- | --- | ---------------- | ------- | ---- | -------- | --------- | -------- | --- | --- | --- |
|     |     |     |     |                  | 𝑟m +    |      | (cid:18) | 1 1       | (cid:19) |     |     |     |
|     |     |     |     |                  | in      |      | 1+𝑥max+  |           |          |     |     |     |
|     |     |     |     |                  | )2      |      |          | −         | ·        |     |     |     |
|     |     |     |     |                  | ( 1 − 𝜌 |      |          | 𝑟 m in 𝑟m | ax       |     |     |     |
|     |     |     |     | (cid:32)(cid:18) |         |      |          | 𝑁 −1      | (cid:33) |     |     |     |
|     |     |     |     |                  | 1       | 1    | (cid:19) | ∑︁        |          |     |     |     |
|     |     |     |     | 𝑥max+            |         | −    | ·𝑁𝜌2𝐾    | + 𝐸(𝑡,𝐾)  | 2 .      |     |     |     |
|     |     |     |     |                  | 𝑟       | 𝑟max |          |           |          |     |     |     |
min
𝑡=0
| Notethat𝑁𝜌2𝐾 | +(cid:205)𝑁−1𝐸(𝑡,𝐾)2 |     |          | 1 E.Setting |                   |         |       |                    |     |     |           |     |
| ------------ | -------------------- | --- | -------- | ----------- | ----------------- | ------- | ----- | ------------------ | --- | --- | --------- | --- |
|              |                      | 𝑡=0 | ≤        | 1−𝜌         |                   |         |       |                    |     |     |           |     |
|              |                      |     | (cid:16) | 1           | (cid:17)2(cid:16) |         | 1     | 1 (cid:17)         |     |     |           |     |
|              |                      |     | 1+       | +𝐶+𝐶′       |                   | 1+𝑥max+ | −     |                    |     | √︄  |           |     |
|              |                      |     |          | 𝑟m in       |                   |         | 𝑟m in | 𝑟m ax √︁4𝛾+𝛽+𝜔max· |     |     | E         |     |
|              |                      |     | 𝜂 =      |             |                   |         |       | ·                  |     |     |           |     |
|              |                      |     |          |             | (1−𝜌)3/2          |         |       |                    |     |     | cost(OPT) |     |
finishestheproof.
E PROOFSFOREFFICIENTSTRUCTURES
E.1 ProofofLemmaA.10
We first consider the case when𝜈 > 1/𝜔ˆ. To simplify the notation, we use𝑢ˇ to denote the sequence of control actions in
|             |                   |     | 𝑡−1 |     |     |     |     |     | 𝑡:𝑡+𝐾−1 |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
| 𝜙ˆ 𝑡+𝐾−1((𝜎 | 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0). |     |     |     |     |     |     |     |         |     |     |     |
𝑡
Wefirstshowthat𝑢ˇ 𝜏 ≥1/𝜔ˆ forall𝜏 ∈{𝑡,...,𝑡+𝐾−1}.Forthesakeofcontradiction,let𝑢ˇ 𝑡1 bethefirstactionsuchthat𝑢 𝑡1−1 ≥1/𝜔ˆ
and𝑢ˇ 𝑡1 <1/𝜔ˆ.Notethatresettingthesequence𝑢ˇ 𝑡1:𝑡+𝐾−1 to𝑢 𝑡1 =𝑢 𝑡1+1=···=𝑢 𝑡+𝐾−1=1/𝜔ˆ willstrictlydecreasethetotalcostandthe
wholesequenceremainsfeasible.Thiscontradictswiththeoptimalityof𝑢ˇ .Thus,wehave𝑢ˇ ≥1/𝜔ˆ forall𝜏 ∈{𝑡,...,𝑡+𝐾−1}.
|     |     |     |     |     |     |     |     | 𝑡:𝑡+𝐾−1 |     |     | 𝜏   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
Wenextshowthat𝑢ˇ ≤𝜈 forall𝜏 ∈{𝑡,...,𝑡+𝐾−1}.Toseethis,forall𝑢 suchthat𝑢 >𝜈 ,wecanresetthemto𝑢 =𝜈 to
|     |     | 𝜏   | 𝑡−1 |     |     |     |     | 𝜏   |     | 𝜏   | 𝑡−1 | 𝜏 𝑡−1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
decreasethetotalswitchingcoststrictlywithoutviolatinganyfeasibilityconstraints.
Since𝑢ˇ 𝜏 ∈ [1/𝜔ˆ,𝜈 𝑡−1]forall𝜏 ∈{𝑡,...,𝑡+𝐾−1},weknowthatthebufferlevelsequenceismonotonicallyincreasing.Thus,if𝑢ˇ 𝑡:𝑡+𝐾−1 is
notmonotonicallydecreasing,wecanpermuteittomakeitmonotonicallydecreasing.Thischangewillstrictlydecreasethetotalswitching
costwithoutviolatinganyfeasibilityconstraints.Therefore,wehaveshownTheoremA.10holdsforthecase𝜈 >1/𝜔ˆ.
𝑡−1
Usingsimilartechniques,wecanshowLemmaA.10alsoholdsforthecase𝜈 <1/𝜔ˆ and𝜈 𝑡−1=1/𝜔ˆ.
𝑡−1
E.2 ProofofTheoremA.9
Wecanrewritetheoptimizationproblem(6)as
𝑡+𝐾−1
|     |     |     |     | ∑︁       |     | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | min      | 𝛾·𝑎 |     |     |     |     |     |     |     |
|     |     |     |     | 𝑎𝑡:𝑡+𝐾−1 |     | 𝑡   |     |     |     |     |     |     |
𝜏=𝑡
|     |     |     |     | s.t.𝑥 | =𝑥 𝜏−1+𝜔ˆ𝑢   | −1,      | for𝜏          | =𝑡,...,𝑡+𝐾−1, |               |     |     |     |
| --- | --- | --- | --- | ----- | ------------ | -------- | ------------- | ------------- | ------------- | --- | --- | --- |
|     |     |     |     | 𝜏     |              | 𝜏        |               |               |               |     |     |     |
|     |     |     |     | 𝑢 𝜏   | =𝑢 𝜏−1+𝑎     | 𝜏 , for𝜏 | =𝑡,...,𝑡+𝐾−1, |               |               |     |     |     |
|     |     |     |     |       |              |          | (cid:20)      | (cid:21)      |               |     |     |     |
|     |     |     |     |       |              |          | 1             | 1             |               |     |     |     |
|     |     |     |     | 𝑥 𝜏   | ∈ [0,𝑥max],𝑢 | 𝜏        | ∈ ,           | , for𝜏        | =𝑡,...,𝑡+𝐾−1, |     |     |     |
|     |     |     |     |       |              |          | 𝑟max          | 𝑟             |               |     |     |     |
min
(37)
|           |                              |     |                              | 𝑥 𝑡−1=𝜎 | 𝑡−1,𝑢 | 𝑡−1=𝜈 | 𝑡−1.  |     |     |     |     |     |
| --------- | ---------------------------- | --- | ---------------------------- | ------- | ----- | ----- | ----- | --- | --- | --- | --- | --- |
| Weuse{(𝑎ˇ | 𝜏 ,𝑢ˇ 𝜏 ,𝑥ˇ 𝜏)}𝜏=𝑡,...,𝑡+𝐾−1 |     | todenotetheoptimalsolutionof |         |       |       | (37). |     |     |     |     |     |
643

| ACMSIGCOMM’24,August4–8,2024,Sydney,NSW,Australia |     |     |     |     |     |     |     |     |     |     |     |     | Chenetal. |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
Similarly,wecanrewritetheoptimizationproblem𝜓ˆ
|     |     |     |     |     |     |     | 𝑡+𝐾−1((𝜎 | 𝑡−1,𝜈 | 𝑡−1);𝜔ˆ;0)as |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ------------ | --- | --- | --- | --- |
𝑡
𝑡+𝐾−1
|     |     |     |     |          | ∑︁  | 2   | 2    |          |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     | min      |     | 𝛾·𝑎 | +𝜔ˆ𝑢 | +𝛽𝑏(𝑥 𝑡) |     |     |     |     |     |
|     |     |     |     | 𝑎𝑡:𝑡+𝐾−1 |     | 𝑡   | 𝑡    |          |     |     |     |     |     |
𝜏=𝑡
|     |     |     |     |     | s.t.𝑥 =𝑥 | 𝜏−1+𝜔ˆ𝑢    | −1,      | for𝜏          | =𝑡,...,𝑡+𝐾−1, |                    |     |     |     |
| --- | --- | --- | --- | --- | -------- | ---------- | -------- | ------------- | ------------- | ------------------ | --- | --- | --- |
|     |     |     |     |     | 𝜏        |            | 𝜏        |               |               |                    |     |     |     |
|     |     |     |     |     | 𝑢 𝜏 =𝑢   | 𝜏−1+𝑎      | 𝜏 , for𝜏 | =𝑡,...,𝑡+𝐾−1, |               |                    |     |     |     |
|     |     |     |     |     |          |            |          | (cid:20)      | (cid:21)      |                    |     |     |     |
|     |     |     |     |     |          |            |          | 1             | 1             |                    |     |     |     |
|     |     |     |     |     | 𝑥 ∈      | [0,𝑥max],𝑢 | ∈        | ,             | ,             | for𝜏 =𝑡,...,𝑡+𝐾−1, |     |     |     |
|     |     |     |     |     | 𝜏        |            | 𝜏        | 𝑟max          | 𝑟             |                    |     |     |     |
min
|                                                |             |                  |     |                              | 𝑥 𝑡−1=𝜎 | 𝑡−1,𝑢              | 𝑡−1=𝜈                      | 𝑡−1.      |     |                    |              |     | (38) |
| ---------------------------------------------- | ----------- | ---------------- | --- | ---------------------------- | ------- | ------------------ | -------------------------- | --------- | --- | ------------------ | ------------ | --- | ---- |
| Weuse{(𝑎ˆ                                      | 𝜏 ,𝑢ˆ 𝜏 ,𝑥ˆ | 𝜏)}𝜏=𝑡,...,𝑡+𝐾−1 |     | todenotetheoptimalsolutionof |         |                    |                            | (38).     |     |                    |              |     |      |
| Forthesakeofcontradiction,weassumethereexists𝜏 |             |                  |     |                              |         |                    | ∈{𝑡,𝑡+1,...,𝑡+𝐾−1}suchthat |           |     |                    |              |     |      |
|                                                |             |                  |     | (cid:12)                     |         |                    |                            |           |     |                    | (cid:12)     |     |      |
|                                                |             |                  |     | (cid:12) 𝜓ˆ 𝑡+𝐾−1            | ((𝜎     | 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0)𝑢𝜏 |                            | −𝜙ˆ 𝑡+𝐾−1 | ((𝜎 | 𝑡−1,𝜈 𝑡−1);𝜔ˆ;0)𝑢𝜏 | (cid:12) >𝜆. |     |      |
|                                                |             |                  |     | (cid:12) 𝑡                   |         |                    |                            | 𝑡         |     |                    | (cid:12)     |     |      |
Bythestronglyconvexityoftheconstrainedoptimizationproblem(37),weseethat
|     |     |     |     |     | 𝑡+ 𝐾−1 |     | 𝑡+ 𝐾−1 | 𝑡+  | 𝐾−1 |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
𝛾 𝜆2
|     |     |     |     |     | ∑︁  | 𝛾𝑎ˆ 2 | ∑︁ 𝛾𝑎ˇ | 2 ≥𝛾 | ∑︁ (𝑎ˆ | −𝑎ˇ 2 > | .   |     | (39) |
| --- | --- | --- | --- | --- | --- | ----- | ------ | ---- | ------ | ------- | --- | --- | ---- |
|     |     |     |     |     |     | 𝑡 −   |        | 𝑡    |        | 𝑡 𝑡)    |     |     |      |
𝐾
|     |     |     |     |     | 𝜏=𝑡 |     | 𝜏=𝑡 |     | 𝜏=𝑡 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ontheotherhand,wehavethat
|     |     | 𝑡+ 𝐾−1 |          |     | 𝑡+ 𝐾−1   |          |     |          | (cid:32) (cid:32) |     | (cid:33) | (cid:33) |     |
| --- | --- | ------ | -------- | --- | -------- | -------- | --- | -------- | ----------------- | --- | -------- | -------- | --- |
|     |     |        | (cid:16) |     | (cid:17) | (cid:16) |     | (cid:17) |                   | 1 1 |          |          |     |
∑︁ 𝜔ˆ𝑢ˆ 2 +𝛽𝑏(𝑥ˆ ∑︁ 𝜔ˆ𝑢ˇ 2 +𝛽𝑏(𝑥ˇ ≥𝐾 𝜔ˆ −𝛽max{𝑥¯2,𝜖(𝑥max−𝑥¯) 2
|     |     |     | 𝑡   | 𝑡)  | −   | 𝑡   |     | 𝑡)  | 𝑟2  | − 𝑟2 |     | }   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
max
|                       |     | 𝜏=𝑡 |                            |     | 𝜏=𝑡              |                   |        |                      |       | min           |           |     |     |
| --------------------- | --- | --- | -------------------------- | --- | ---------------- | ----------------- | ------ | -------------------- | ----- | ------------- | --------- | --- | --- |
| Bytheoptimalityof{(𝑎ˆ |     | 𝜏   | ,𝑢ˆ 𝜏 ,𝑥ˆ 𝜏)}𝜏=𝑡,...,𝑡+𝐾−1 |     | in(38),weseethat |                   |        |                      |       |               |           |     |     |
|                       |     |     |                            |     | 𝑡+𝐾−1            |                   |        |                      | 𝑡+𝐾−1 |               |           |     |     |
|                       |     |     |                            |     | ∑︁               | (cid:16) 2        |        | 2(cid:17)            | ∑︁    | (cid:16) 2    | 2(cid:17) |     |     |
|                       |     |     |                            | 0≥  |                  | 𝜔ˆ𝑢ˆ 𝑡 +𝛽𝑏(𝑥ˆ     | 𝑡)+𝛾𝑎ˆ | 𝑡                    | −     | 𝜔ˆ𝑢ˇ 𝑡 +𝛽𝑏(𝑥ˇ | 𝑡)+𝛾𝑎ˇ 𝑡  |     |     |
|                       |     |     |                            |     | 𝜏=𝑡              |                   |        |                      | 𝜏=𝑡   |               |           |     |     |
|                       |     |     |                            |     | 𝛾𝜆2              | (cid:32) (cid:32) | 1      | 1 (cid:33)           |       |               | (cid:33)  |     |     |
|                       |     |     |                            |     |                  |                   |        | −𝛽max{𝑥¯2,𝜖(𝑥max−𝑥¯) |       |               | 2         |     |     |
|                       |     |     |                            |     | > +𝐾             | 𝜔ˆ                | −      |                      |       |               | } ,       |     |     |
|                       |     |     |                            |     | 𝐾                | 𝑟2                |        | 𝑟2                   |       |               |           |     |     |
|                       |     |     |                            |     |                  |                   | max    | min                  |       |               |           |     |     |
whichcontradictsourassumptionthat
|     |     |     |     |     | 𝐾2  | (cid:32) (cid:32) | 1   | 1 (cid:33)           |     |     | (cid:33) |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | -------------------- | --- | --- | -------- | --- | --- |
|     |     |     |     |     |     |                   |     | +𝛽max{𝑥¯2,𝜖(𝑥max−𝑥¯) |     |     | 2        |     |     |
|     |     |     |     |     | 𝛾 ≥ | 𝜔ˆ                | −   |                      |     |     | } .      |     |     |
|     |     |     |     |     | 𝜆2  | 𝑟2                | 𝑟2  |                      |     |     |          |     |     |
|     |     |     |     |     |     | min               |     | max                  |     |     |          |     |     |
644