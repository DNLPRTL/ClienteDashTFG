1698 IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020
BOLA: Near-Optimal Bitrate Adaptation
for Online Videos
Kevin Spiteri , Member, IEEE, Rahul Urgaonkar, Senior Member, IEEE,
and Ramesh K. Sitaraman, Fellow, IEEE
Abstract—Modern video players employ complex algorithms news outlets (e.g., CNN), sports organizations (e.g., NFL,
to adapt the bitrate of the video that is shown to the user. MLB), and video subscription services (e.g., Netflix, Hulu).
Bitrate adaptation requires a tradeoff between reducing the Recent research has shown that low-performing videos that
probability that the video freezes (rebuffers) and enhancing the
start slowly, play at lower bitrates, and freeze frequently can
quality of the video. A bitrate that is too high leads to frequent
cause viewers to abandon the videos or watch fewer minutes
rebuffering, while a bitrate that is too low leads to poor video
ofthevideos,significantlydecreasingtheopportunityforgen-
quality. Video providers segment videos into short segments
and encode each segment at multiple bitrates. The video player erating revenue for the video providers [3]–[5], underscoring
adaptively chooses the bitrate of each segment to download, the need for a high-quality user experience.
possibly choosing different bitrates for successive segments. We Providingahigh-qualityexperienceforvideousersrequires
formulate bitrate adaptation as a utility-maximization problem balancing two contrasting requirements. The user would like
and devise an online control algorithm called BOLA that uses
to watch the highest-quality version of the video possible,
Lyapunov optimization to minimize rebuffering and maximize
where video quality can be quantified by the bitrate at which
video quality. We prove that BOLA achieves a time-average
utility that is within an additive term O(1/V) of the optimal the video is encoded. For instance, watching a movie in high
value, foracontrol parameterV relatedtothevideobuffersize. definition(HD) encodedat 2 Mbpsarguablyprovidesa better
Further,unlikepriorwork,BOLAdoesnotrequirepredictionof user experience than watching the same movie in standard
available network bandwidth. We empirically validate BOLA in definition (SD) encoded at a bitrate of 800 kbps. In fact,
a simulated network environment using a collection of network
there is empirical evidence that the user is more engaged
traces. Weshow that BOLA achieves near-optimal utilityand in
and watches longer when the video is presented at a higher
many cases significantly higher utility than current state-of-the-
bitrate. However, it is not always possible for users to watch
art algorithms. Our work has immediate impact on real-world
video players and for the evolving DASH standard for video videos at the highest encoded bitrate, since the bandwidth
transmission.WealsoimplementedanupdatedversionofBOLA available onthe networkconnectionbetweenthe videoplayer
that is now part of the standard reference player dash.js and is on the user’s device and the video server constrains what
used in production by several video providers such as Akamai, bitrates can be watched. In fact, choosing a bitrate that is
BBC, CBS, and Orange. higher than the available network bandwidth1 will lead to
Index Terms—Internet video, video quality, adaptive bitrate video freezes in the middle of the playback, since the rate
streaming, Lyapunov optimization, optimal control. at which the video is being played exceeds the rate at which
the video can be downloaded. Such video freezes are called
I. INTRODUCTION rebuffersandplayingthevideocontinuouslywithoutrebuffers
ONLINEvideosarethe“killer”applicationoftheInternet is a key factor in the QoE perceived by the user [4]. Thus,
balancing the contrasting requirements of playing videos at a
with videos currently accounting for more than half of
highbitratewhileatthesametimeavoidingrebuffersiscentral
the Internet traffic. Video viewership is growing at a torrid
to providing a high-quality video watching experience.
pace and videos are expected to account for more than 85%
ofallInternettrafficwithinafewyears[2].Asallformsoftra-
ditionalmediamigratetotheInternet,videoprovidersfacethe A. Adaptive Bitrate (ABR) Streaming
daunting challenge of providing a good quality of experience
Achieving a high QoE for video streaming is a major
(QoE) for users watching their videos. Video providers are
challenge due to the sheer diversity of video-capable devices
diverseandincludemajormediacompanies(e.g.,NBC,CBS),
that include smartphones, tablets, desktops, and televisions.
Manuscript received December 23, 2018; revised September 14, 2019; Further, the devices themselves can be connected to the
accepted April 25, 2020; approved by IEEE/ACM TRANSACTIONS ON Internet in a multitude of ways, including cable, fiber, DSL,
NETWORKINGEditorS.Rao.DateofpublicationJune8,2020;dateofcurrent WiFiandmobilewireless, eachprovidingdifferentbandwidth
versionAugust18,2020.ThisworkwassupportedinpartbytheNSFunder
characteristics. The need to adjust the video playback to the
GrantCNS-1413998andGrantCNS-1901137.Apreliminary versionofthis
article appeared atINFOCOM2016.(Correspondingauthor:KevinSpiteri.) characteristics of the device and the network has led to the
KevinSpiteriandRameshK.SitaramanarewiththeCollegeofInformation evolution of adaptive bitrate (ABR) streaming that is now
and Computer Sciences, University of Massachusetts at Amherst, Amherst,
the de facto standard for delivering videos on the Internet.
MA01003USA(e-mail:kspiteri@cs.umass.edu; ramesh@cs.umass.edu).
Rahul Urgaonkar is with Amazon Prime Video, Seattle, WA 98109 USA
(e-mail: urgaonka@amazon.com). 1Throughout this paper, we say bandwidth when talking about network
Digital ObjectIdentifier 10.1109/TNET.2020.2996964 throughput andbitrate whentalking aboutencodingquality.
1063-6692©2020IEEE.Personaluseispermitted, butrepublication/redistribution requires IEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.html formoreinformation.

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1699
ABR streaming requires that each video is partitioned into server and the video player is predicted and the predicted
segments, where each segment corresponds to a few seconds value is used to determine the bitrate of the next segment
ofplay.Eachsegmentisthenencodedinanumberofdifferent that is to be downloaded. A complementary approach is a
bitrates to accommodate a range of device types and network buffer-based approach that does not predict the bandwidth,
connectivities. When the user plays a video, the video player but only uses the amount of data that is currently stored
can download each segment at a bitrate that is appropriate in the buffer of the video player. Recently, there has been
for the available bandwidth of the network connection. Thus, empirical evidence that a buffer-based approach has desirable
the player can switch to a segment with a lower bitrate when propertiesthatbandwidth-basedapproacheslackandhasbeen
the available bandwidth is low to avoid rebuffering. If more adopted by Netflix [11]. An intriguing outcome of our work
bandwidth becomes available at a future time, the player can is that the optimal algorithm within our utility maximization
switch back to a higherbitrate to providea richer experience. framework requires only knowledge of the amount of data in
The video player has a buffer that allows it to fetch and the buffer and no estimate of the available bandwidth. Thus,
store segmentsbefore they need to be renderedon the screen. our work provides the first theoretical justification for why
Thus, the video player can tolerate brief network disruptions buffer-basedalgorithmsperformwellinpracticeandaddsnew
without interrupting the playback of the user by using the insightstotheongoingdebate[14]withinthevideostreaming
buffered segments. A large disruption, however, will empty and DASH standards communities of relative efficacy of the
the buffer, resulting in rebuffering. The decision of which two approaches.Further,since ouralgorithmBOLA is buffer-
segments to download at what bitrates is made by a bitrate based, it avoids the overheads of more complex bandwidth
adaptation algorithm within the video player, the design of prediction present in current video player implementations
such algorithms being the primary focus of our work. and is more stable under bandwidth fluctuations. Note that
Several popular implementations of ABR streaming our results imply that the buffer level is a sufficient statistic
exist, including Apple’s HTTP Live Streaming (HLS) [6], that indirectly provides all information about past bandwidth
Microsoft’sLiveSmoothStreaming(Smooth)[7]andAdobe’s variations required for choosing the next bitrate.
Adaptive Streaming (HDS) [8]. Each has its own proprietary We also empirically evaluate BOLA on a wide set of
implementation and slight modifications to the basic ABR network traces that include 12 test cases provided by the
technique described above. A key recent development is DASH industry forum [16] and 85 publicly-available 3G
a unifying open-source standard for ABR streaming called mobilebandwidthtraces[17].Asabenchmarkforcomparison,
MPEG-DASH[9].DASH isbroadlysimilarto theotherABR we develop an optimal offline algorithm that uses dynamic
protocolsandisa particularfocusinourempiricalevaluation. programming and is guaranteed to produce the maximum
achievable time-average utility for any given set of network
B. Our Contributions traces. Unlike BOLA that works in an online fashion, the
offline optimal algorithm makes decision based on perfect
Our primary contribution is a principled approach to the
knowledge of future bandwidth variations. Remarkably, the
design of bitrate adaptation algorithms for ABR streaming.
utilityachievedbyBOLAiswithin84–95%ofofflineoptimal
In particular, we formulate bitrate adaptation as a utility
utility for all the tested traces.
maximizationproblemthatincorporatesboth key components
BesidescomparingBOLA withthe offlineoptimal,we also
of QoE: the average bitrate of the video experienced by the
empirically compared our algorithm with four state-of-the-art
userandthedurationoftherebufferevents.Anincreaseinthe
algorithms proposed in the literature. In all test cases, BOLA
averagebitrateincreasesutility,whereasrebufferingdecreases
achieved a utility that is as good as or better than the best
it.Astrengthofourframeworkisthatutilitycanbedefinedin
state-of-the-art algorithm.
a very general manner, say, depending on the content, video
We also implemented BOLA in dash.js, the open-source
provider, or user device.
standard DASH reference player [18]. Deploying BOLA in
Using Lyapunov optimization, we derive an online bitrate
production required a number of adjustments [19]. Through
adaptation algorithm called BOLA (Buffer Occupancy based
dash.js, BOLA is now being used in production by several
Lyapunov Algorithm) that provably achieves utility that is
majorvideoprovidersanddeliverynetworkssuch asAkamai,
within an additive factor of the maximum possible utility in
BBC, CBS and Orange. BOLA is available as an option to
the large video regime. While numerous bitrate adaptation
commercial video providers who often use the production
algorithms have been proposed [10]–[15] and implemented
dash.jsreference implementationfor building their own video
within video players, our algorithm is the first to provide a
players.Further,asecondalgorithmcalled DYNAMIC[19]is
theoretical guarantee on the achieved utility. Further, BOLA
also available for commercial video providers. DYNAMIC is
providesanexplicitknobforvideoproviderstosettherelative
a hybrid algorithm that uses a simple throughput-estimation
importanceofahighvideoqualityinrelationtotheprobability
approachduringthe start-up phase of the video and then uses
of rebuffering.
BOLA afterwards.Both algorithmscan be evaluatedin a web
While not an explicit part of the Lyapunov optimization
browser by clicking the “Show Options” button in the latest
framework, we also show how BOLA can be adapted to
version of the dash.js reference player found at [18].
avoid frequentbitrate switches duringvideo playback.Bitrate
switches are arguably less annoying than rebuffering, but it
is still of some concern to video providers and users alike if
II. SYSTEMMODEL
such switches occur too frequently. Our system model closely captures how ABR streaming
Most algorithms implemented in practice use a bandwidth- works on the Internet today. We consider a video player that
based approach where the available bandwidth between the downloads a video file from a server over the Internet and

1700 IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020
plays it back to the user. The video file is segmented into finite first and second moments as well as a finite inverse
segments that are downloaded in succession. The available second moment. Suppose the player starts to download a
bandwidthbetweentheserverandthe playervariesovertime. segment of bitrate index m at time t. Then the time t(cid:2) when
This can be due to reasons such as network congestion and the download finishes satisfies the following:
wireless fading among others. The viewing experience of the (cid:2)
t(cid:2)
user is determined by both the video quality as quantified S m = ω(τ)dτ (2)
by the bitrates of the segments that are played back and the t
playback characteristics such as rebuffering. The objective Let E{ω(t)}=ω avg . Then, E{t(cid:2)−t}=S m /ω avg .
of the player is to maximize a utility associated with the
user’sviewingexperiencewhileadaptingtotime-varying(and III. PROBLEMFORMULATION
possibly unpredictable) changes in the available bandwidth.
We consider two primary performance metrics4 that affect
Video Model: The video file is segmentedinto N segments
theoverallQoEoftheuser:(1)time-averageplaybackquality
indexed as {1,2,...,N} where each segment represents p
which is a function of the bitrates of the segments viewed
secondsof thevideo.Onthe server,each segmentisavailable
by the user and (2) fraction of time spent not rebuffering. To
in M different bitrates where a segment encoded at a higher
formalize these metrics, we consider a time-slotted represen-
bitratehasalargersizeinbitsanditsplaybackprovidesabet-
tation of our system model. The timeline is divided into non-
teruserexperienceandhigherutility.Supposethesize(inbits)
overlapping consecutive slots of variable length and indexed
p of os a e ny th 2 e se u g ti m lit e y nt d e e n ri c v o e d d e b d y at th b e itr u a s t e e r i f n r d o e m x v m ie i w s i S n m gi b t i i t s s g an iv d en su b p y - s b e y c k on ∈ ds { l 1 o , n 2 g , . . W .. e }. a S ss lo u t m k e s t t h a a rt t s t at = tim 0. e A t k tt a h n e d b i e s g T in k n = ing t k o + f 1 e − ac t h k
υ mwherem∈{1,2,...,M}.WLOG,letthesegmentbitrates
slot, the video player makes a
1
control decision on whether it
be non-decreasing in index m. Then, the following holds.
shouldstartdownloadinganewsegment,andifyes,itsbitrate.
υ 1 ≤υ 2 ≤...≤υ M ⇐⇒S 1 ≤S 2 ≤...≤S M . (1) I s f er a ve d r o a w n n d lo t a h d e d d e o c w is n io lo n ad is s m ta a rt d s e, im th m en ed a ia r t e e q ly u .5 es T t h is is se d n o t w t n o lo th ad e
Note that the actual encoding bitrate for bitrate index m is takes T k seconds and is completed at the end of slot k. Note
given by S m /p bits/second. that T k is a random variable whose actual value depends on
Video Player: The video player downloads successive seg- the realization of the ω(t) process as well as the choice of
ments of the video file from the server and plays back the segment bitrate. If the player decides not to download a new
downloaded segments to the user. Each segment must be segment in slot k (for example, when the buffer is full), then
downloaded in its entirety before it can be played back. this slot lasts for a fixed duration of Δ seconds.
We assume that the player sends requests to the server to We define the following indicator variable for each slot k:
⎧
download one segment at a time. Also, the segments are ⎪⎨1
if the player downloads a segment
downloaded in the same order as they are played back. The
video player has a finite buffer of size Q
max
segments3 a m (t k )= ⎪⎩ of bitrate index m in slot k, and (3)
to store the downloaded but yet-to-be-played-back segments. 0 otherwise.
Measuring the buffer in segments is equivalent to measuring (cid:7)
it in seconds since the segment duration p is fixed. If the Then, (cid:7) for all k, we must have M m=1 a m (t k )≤1. Moreover,
buffer is full the player cannot download any new segments when M m=1 a m (t k )=0, then no segments are downloaded.
andwaitsforafixedperiodoftimegivenbyΔsecondsbefore Denote the buffer level (measured in number of segments)
attempting to download a new segment. The segments that at the start of slot k by Q(t k ). The dynamics of this queue
are fully downloaded are played back at a fixed rate of 1/p can be expressed using the following equation:
segments/second without any idling. T (cid:8)M
When sending a download request for a new segment, the Q(t k+1 )=max[Q(t k )− p k,0]+ a m (t k ) (4)
player also specifies the desired bitrate for that segment. This m=1
enablestheplayertotradeofftheoverallvideoqualitywiththe H(cid:7)ere, the arrival value into this queue in slot k is given by
l m h i a k e s e n l a t i s h fi o i x n o e d t d h o e p f l b a u r y e f b f b a e u c r f k f f e o t r r i i m n p g l e a o y th b f a a p t c s k o e . c c N c o u o n r t d s e s, w th t h h a e e t n w si h t z h i e l e e o re e f a t a h c r h e e s s n e e o g gm m se e e g n n - t t slo M m t = k 1 a a n m d (t 0 k ) ot w he h r i w ch is i e s . 1 Th if e a de d p o a w r n tu lo re ad va d l e u c e is i i s on T k is /p ma w d h e ic in h
represents the total number of segments (including fractional
(in bits) can be different depending on its bitrate. Thus, the segments) that could have departed the buffer in slot k. Note
choice of bitrate for a segment impacts its download time. that the actual value of T k is revealed at the end of slot k.
Network Model: The available bandwidth (in bits/second) Alsonotethatasegmentthatisdownloadedinslotkbecomes
betweentheserverandplayerisassumedtovarycontinuously
availableforplaybackonlyfromthenextslot.Weassumethat
in time according to a stationary random process ω(t). We the buffer level is initialized to 0, i.e., Q(t )=0.
1
d p o rop n e o r t tie m s a o k r e p a r n o y ba a b s il s i u ty m d p i t s io tr n ib s u a ti b o o n u o t f k ω no (t w ) in ex g ce th p e tt s h t a a t ti i s t ti h c a a s l Let K N denote the index of the slot in which the Nth (i.e.,
last) segment is downloaded. Also, denote the time at which
theplayerfinishesplayingbackthelastsegmentbyT .Then
2For simplicity, we assume that the segment size (in bits) is Sm for all end
segments ofagivenbitrate indexm.However, ourframework canbeeasily
4We do not include the secondary objective of avoiding frequent bitrate
extended to the case where the segment size for the same bitrate can vary
switches inourformulation, butwedealwithitempirically inSectionV-E.
acrosssegments.
3Itiscommonpractice forvideo players tomeasure thebuffer inseconds
5Anydelaysassociatedwithsendingtherequestcanbeaddedtotheoverall
downloadtime.
ofplayback timeratherthaninbits.

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1701
the first performance metric of interest is the time-average Then, the metrics υ N and s N can be expressed as
expected playback utility υ N which is defined as (cid:9) (cid:7) (cid:7) (cid:10)
υ N =(cid:2)
E (cid:9) (cid:7) K
k=
N
1 E
(cid:7)
{
M
m T =1
a
} m
(t
k
)υ
m
(cid:10)
(5)
υ =(cid:2)
N
l
→
im
∞
υ
N
=
N (cid:9)
l
→
i
(cid:7)
m
∞
E
(cid:7)
K k= N 1
E{
M m
T
=
en
1
d
a
}
m
(cid:10)
(t k )υ m
end lim 1 E KN M a (t )υ
where the numerator denotes the expected total utility across = KN→∞KN k=1 (cid:9) (cid:7) m=1 m (cid:10) k m (7)
all N segments. Note that a segment can only be played lim 1 E KN T
back after it has been downloaded entirely. Thus, T end is KN→∞KN (cid:9) (cid:7) k=1 (cid:7) k (cid:10)
greater than the last segment’s download finish time, i.e., E KN M a (t )p
T en T d he > s t e K co N n + d p T e K rf N o . rmance metric of interest is the expected s =(cid:2) N l → im ∞ s N = N (cid:9) l → im ∞ k=1 E{T m e = nd 1 } (cid:10) m k
(cid:7) (cid:7)
fraction of time s N that is spent not rebuffering and can be lim 1 E KN M a (t )p
interpreted as a measure of the average playback “smooth- = KN→∞KN k= (cid:9) 1 (cid:7) m=1 m (cid:10) k (8)
ness”. This can be calculated by observing that the actual lim 1 E KN T
playback time for all N segments is Np seconds. Thus, the KN→∞KN k=1 k
expected playback smoothne (cid:9) ss s N is given by (cid:10) This follows by noting that the difference between the
(cid:7) (cid:7)
s N =(cid:2) E{ N T p } = E K k= N 1 E{T M m=1 } a m (t k )p (6) e to x t p a e l c d t o e w d n to lo ta a l d p fi la n y is b h ac ti k m fi e n E ish(cid:9) (cid:7) tim K k e = N 1 E T { k T(cid:10)en i d s } u a p n p d er th b e ou e n x d p e e d ct b e y d
end end a finite value due to the finite Q . Specifically, this upper
max
(cid:7)where(cid:7)in the last step we use the relation that Np = bound is given by Q p. Therefore, instead of considering
K k= N 1 M m=1 a m (t k )p. Note that T end ≥ Np (since at most the total playback fi m n a is x h time, we can consider the total
onesegmentcanbe playedbackatanytime), so thats N ≤1. download finish time in the objective when the video size
becomes large.
A. Design Objective
Next,replacethefinitebufferconstraintwitharatestability
We want to design a control algorithm that maximizes the constraint [21]. This constraint only requires that the time-
joint utility υ N +γs N subject to the constraint that Q(t k )≤ average arrival rate into the buffer cannot exceed the time-
Q max for all k. Here, γ >0 is an input weight parameter for average playback rate. This is equivalent to requiring that
prioritizing playback utility versus the playback smoothness. (cid:11) (cid:12) (cid:11) (cid:12)
Thisproblemcanbeformulatedasastochasticoptimization 1 (cid:8)KN (cid:8)M 1 (cid:8)KN
lim E a (t )p ≤ lim E T
p
d
r
y
o
n
b
a
l
m
em
ic
w
pr
it
o
h
g
a
ra
t
m
im
m
e
i
-
n
a
g
ve
(
r
D
ag
P
e
)
o
b
b
a
j
s
e
e
c
d
tiv
ap
e
p
o
r
v
o
e
a
r
c
a
he
fi
s
ni
c
t
a
e
n
ho
b
r
e
iz
u
o
s
n
ed
an
to
d KN→∞K
N
k=1m=1
m k KN→∞K
N
k=1
k
(9)
solve it [20]. However, traditional DP based methods have
two majordisadvantages.First, theyrequireknowledgeof the
The rate stability constraint is a relaxation of the finite
distribution of the ω(t) process which may be hard to obtain.
buffer constraint since any policy that ensures finite buffers
Second, even when such knowledgeis available, the resulting
is always rate stable but not vice versa. Therefore, under this
DPcanhavea verylargestate space.Thisisbecausethestate
relaxation, the optimal time-average utility cannot be smaller
space for this problem under a DP formulation would consist
than the optimal time-average utility with the finite buffer
of not only the timeslot index k and value t k, but also the
constraint.
buffersize Q(t k ). Further,an appropriatediscretizationof the With these relaxations, our performance objective for the
ω(t) process would be required to obtain a tractable solution. bitrate adaptationproblemis to maximizethe jointutility υ+
In order to overcome the above challenges associated with γssubjecttotheratestabilityconstraint(9).Letusdenotethe
traditional DP based methods, we take an alternate approach optimaltime-averageutilityforthisproblembyυ∗+γs∗.This
inthispaper.First, weconsiderthebitrateadaptationproblem
problem fits in the framework of Lyapunov optimization for
inthelimitingregimewhenthevideosizebecomeslarge,i.e.,
renewalsystems[22].Specifically,thisframeworkextendsthe
N →∞. Second, we replace the finite buffer constraint with
originalLyapunovoptimizationtechnique[21]tosystemswith
a rate stability constraint (made precise in the next section).
variable length renewal frames and shows that minimizing a
The reason for making these assumptions is that it results
“drift-plus-penalty” ratio over every frame yields an optimal
in simplifications to the original problem as discussed in the
controlalgorithm.We referto [22]for detailson this method.
next section. This allows us to develop a bitrate adaptation
In the context of our bitrate adaptation problem, the variable
algorithm that does not require any knowledge of the dis-
length slots represent the renewal frames.
tribution of ω(t), yet offers provable theoretical performance
The following characterization can be made about the
guarantees in the large video size regime while satisfying the
optimality of i.i.d. algorithms.
finite buffer constraint. As shown later in Section V-D, with
Lemma 1: Forthebitrateadaptationprobleminthelimiting
slightmodifications,thisalgorithmcanbeusedforfinitesized regime when the video size becomes large, i.e., N → ∞,
videos as well and offersclose to optimal performancein our
there exists a buffer-state-independent stationary algorithm
experiments.
thatmakesi.i.d.controldecisionsineveryslotandsatisfiesthe
ratestabilityconstraintwhileachievingtime-averageutilityno
B. Problem Relaxation smaller than υ∗+γs∗.
Consider the bitrate adaptation problem in the limiting Proof: This follows from Lemma 1 in [22] and uses the
regime when the video size becomes large, i.e., N → ∞. fact that the conditional expectations and conditional second

| 1702 |     |     |     |     |     |     |     | IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020 |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
moments of the frame length and utility are bounded under Notice that solving this problem does not require any
any algorithm. The full proof is omitted for brevity. knowledge of the ω(t) process. Further, the optimal solution
Note that such a buffer-state-independent stationary algo- depends only on the buffer level Q(t ). That’s why we call
k
rithm is not necessarily feasible for our finite buffer system. ouralgorithmBOLA:BufferOccupancybasedLyapunovAlgo-
Further, calculating it explicitly would require knowledge of rithm.ThesepropertiesofBOLAshouldbecontrastedwiththe
the distribution of ω(t). However, instead of calculating this bandwidth prediction based strategies that have been recently
policyexplicitly,wewilluseitsexistenceandcharacterization proposed for this problem that require explicit prediction of
per Lemma 1 to design an online control algorithm using the the available bandwidth for control decisions.
technique of Lyapunov optimization over renewal frames. The following theorem characterizes the theoretical perfor-
Inthenextsection,wewillpresentthisalgorithmandshow mance guarantees provided by BOLA.
thatitmeetsthefinitebufferconstraintwhileachievingatime- Theorem 1: Suppose BOLA as defined by (11) is imple-
|     |     |     | O(1/Q |     | )   | υ∗+γs∗ |     |     |     |     |     |     |     | 0   | < V ≤ |
| --- | --- | --- | ----- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
average utility that is within of without mented in every slot using a control parameter
|     |     |     |     | max |     |     |     | Qmax−1. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
requiring any knowledge of the distribution of ω(t). Assume Q(0)=0. Then, the following hold.
υM+γp
|     |     |     |     |     |     |     |     | 1)  | The | queue backlog | satisfies | Q(t | k ) ≤ V(υ | M +γp)+1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | --------- | -------- | --- |
IV. BOLA: AN ONLINECONTROL ALGORITHM forallslotsk.Further,thebufferoccupancyinsegments
Q
We first give a high-level intuition of the Lyapunov opti- never exceeds max .
mizationoverrenewalstechnique.Thistechniqueconvertsthe 2) The time-average utility achieved by BOLA satisfies
problem of optimizing the time-average metrics in (7)–(8) p2+Ψ
|                                                         |     |     |     |     |     |     |     |     |     | υBOLA+γsBOLA |     | ≥υ∗+γs∗− |     |      | (12) |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --- | ---- | ---- |
| subjecttothetime-averageconstraintin(9)intoaseriesofper |     |     |     |     |     |     |     |     |     |              |     |          |     | 2p2V |      |
slot optimizationproblems. The problem to be solved in each (cid:13) (cid:14)
slot involves minimizing a ratio of the expected drift-plus- whereΨisanupperboundonE T 2 underanycontrol
k
|     |     |     |     |     |     |     |     |     | algorithm | and | is assumed | to be finite. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ------------- | --- | --- | --- |
penaltyvalueinthatslottotheexpectedlengthoftheslot.As
shown in the Appendix, this can be done without requiring Proof: See the Appendix.
any knowledg(cid:13)e of the distribution of ω(t). (cid:14)The drift term Remarks: The performance bounds in Theorem 1 show a
| consistsofE |     | (Q(t )2−Q(t |     | )2)/2|Q(t |     | )   |     | [O(1/V),O(V)] |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
k+1 k k andservesto utility and backlog tradeoff that is typical
meettheratestabilityconstraint(9).Thepenaltytermconsists of Lyapunovbased controlalgorithmsfor similar utility max-
of the playback utility and playback smoothness received in imization problems. Specifically, the time-average utility of
BOLAiswithinanO(1/V)additivetermoftheoptimalutility
thatslot.Wekeeptheutilityandsmoothnessasseparateterms
even though they can be folded into one metric. This allows and this gap may be made smaller by choosing a larger value
us to tune the relative importance of increasing video bitrate of V. However, the largest feasible value of V is constrained
and reducingrebufferingwithoutchangingthe algorithm.The by the buffer size and there is a linear relation between them.
V >0
| algorithm | uses | a control | parameter |     | to  | allow a | tradeoff |     |     |     |     |     |     |     |     |
| --------- | ---- | --------- | --------- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
between the buffer size and the performance objectives. A. Understanding BOLA With an Example
| We  | now | present the | algorithm. | In  | every | slot k, given | the |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ---------- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WenowpresentasampleruntoillustratehowBOLAworks.
| bufferlevelQ(t |         | )atthestartoftheslot, |         |               |                   |               |     |          |           |                         |                |                |      |          |          |
| -------------- | ------- | --------------------- | ------- | ------------- | ----------------- | ------------- | --- | -------- | --------- | ----------------------- | -------------- | -------------- | ---- | -------- | -------- |
|                |         | k                     |         |               | ouralgorithmmakes |               |     |          |           |                         |                |                |      |          |          |
|                |         |                       |         |               |                   |               |     | We       | slice a   | 99-second               | video          | using 3-second |      | segments | and      |
| a control      |         | decision by           | solving | the following |                   | deterministic |     |          |           |                         |                |                |      |          |          |
|                |         |                       |         |               |                   |               |     | encodeit | at        | five differentbitrates. |                | While          | BOLA | only     | requires |
| optimization   |         | problem. Let          |         |               |                   |               |     |          |           |                         |                |                |      |          |          |
|                |         |                       |         |               |                   |               |     | the      | utilities | to be a                 | non-decreasing | function       |      | of the   | segment  |
| ρ(t            | ,a(t )) |                       |         |               |                   |               |     |          |           |                         |                |                |      |          |          |
⎧k k bitrate, it is natural to consider concave utility functions with
(cid:7)
⎪⎪⎪⎨ 0 M a (t ) d i m i nis h i n g r e tur ns , e .g . ,a 1 M bp s i nc r e as e in s e g m en t b it r a te
|     |     |     |     |     | if  |     | m k |         |           |               |          |                 |          |           |               |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------------- | -------- | --------------- | -------- | --------- | ------------- |
|     |     |     |     |     |     | m=1 |     | li k el | y p r o v | id e s a l ar | g e r ut | ili ty g ai n f | o r t he | u s e r w | h e n t h a t |
=0,
(cid:7) (cid:15) (cid:16) increase is from 0.5 Mbps to 1.5 Mbps than when it is from
=
| ⎪⎪⎪⎩ | M   | a (t ) Vυ | +Vγp−Q(t |     | )   |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m=1 m k m k otherwise. 5 Mbps to 6 Mbps. A natural choice for our example is
(cid:7)
M a (t )S t he l o g a r ith m ic ut ilit y f u n c ti on : l e t υ m = l n ( S m / S ) . P ic k
|     |     | m=1 m | k   | m   |     |     |     |     |           |          |            |                   |            |              | 1          |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | ----------------- | ---------- | ------------ | ---------- |
|     |     |       |     |     |     |     |     | γ = | 5 . 0 / p | a nd V = | 0 .9 3 . T | h e b it r a te s | and u t il | it ie s a re | b e lo w . |
(10)
Thendeterminea(t ) bitr ate (M b ps) 0 . 3 3 1 0 . 6 8 8 1 . 4 2 7 2 . 9 6 2 6 .0 0 0
k bysolvingtheoptimizationproblem:
|           |     |             |         |     |            |     |      |     | S (M b    | ) 0            | . 9 9 3 | 2 . 0 6 4 4 . | 2 8 1 8 | . 8 8 6     | 1 8 .0 0 |
| --------- | --- | ----------- | ------- | --- | ---------- | --- | ---- | --- | --------- | -------------- | ------- | ------------- | ------- | ----------- | -------- |
| Maximize: |     | ρ(t ,a(t    | ))      |     |            |     |      |     | υ         | 0.000          |         | 0.732 1.461   | 2.192   |             | 2.897    |
|           |     | (cid:7) k k |         |     |            |     |      |     |           |                |         |               |         |             |          |
| Subject   |     | to: M a     | (t )≤1, | a   | (t )∈{0,1} |     | (11) |     |           |                |         |               |         |             |          |
|           |     | m=1         | m k     |     | m k        |     |      |     |           |                |         |               |         |             |          |
|           |     |             |         |     |            |     |      | For | any       | slot we choose |         | the segment   | bitrate | to maximize |          |
|           |     |             |         |     |            |     |      | (Vυ | +Vγp−Q)/S |                |         | 1 ≤ m ≤       | M.      |             |          |
The constraints of this problem result in a very simple m m for Fig. 1 shows the
solution structure. Specifically, the optimal solution is given relationshipbetweenthe expressionandthe bufferlevelQ for
m.
by: different The line intersections mark the buffer levels that
1) IfQ(t )>V(υ +γp)forallm∈{1,2,...,M},then correspondtodecisionthresholds.Fig.2summarizesBOLA’s
|     |     | k m |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the no-download option is chosen, i.e., a (t ) = 0 for bitrate choices as a function of the buffer level.
m k
|     | m.  |              |           | T   | =Δ. |     |     | Fig.3showshowBOLAworks.Weuseasyntheticnetwork |     |     |     |     |     |     |     |
| --- | --- | ------------ | --------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | all | Note that in | this case | k   |     |     |     |                                               |     |     |     |     |     |     |     |
2) Else, the optimal solution is to download the next bandwidth profile as shown in Fig. 3(a). We can see the
segmentat bitrate in(cid:15)dex m∗ where m∗ is t(cid:16)he index that feedback loop involving the bitrate in (a) and the buffer level
Vυ +Vγp−Q(t ) /S in (b). BOLA chooses the bitrate based directly on the buffer
|     | maximizesthe | ratio |     | m   |     | k m | among |     |     |     |     |     |     |     |     |
| --- | ------------ | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
all m for which this ratio is positive. levelusing Fig. 2. The bitrate affectsthe downloadtime, thus

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1703
the video player plays out the segments remaining in the
buffer.
B. Choosing Utility and Parameters γ and V
Whilewe chosea logarithmicutilityfunctionfortheexam-
ple,avideoprovidercanuseanyutilityfunctionsatisfying(1).
The utility function might also take into account system
characteristics such as the type of device a viewer is using.
γcorrespondstohowstronglywewanttoavoidrebuffering.
Increasingγ translatesthegraphsinFigs.1and2totheright,
effectively shifting the thresholds higher without changing
their relative distance. BOLA will thus download more low-
Fig.1. Thevalueof(Vυm+Vγp−Q)/Sm fordifferentbitratesdepends
bitrate segments to maintain a larger (and safer) buffer level.
on buffer level. (γp = 5 and V = 0.93.) Note that the buffer level is Qp
Increasing V expands the graphs in Figs. 1 and 2 horizon-
seconds.
tallyabouttheorigin.IfwehaveamaximumbufferlevelQ
max
wewanttoavoiddownloadingunlessthereisenoughspacefor
one full segment on the buffer, that is unless Q≤Q −1.
max
For a given Q max we can set V =(Q max −1)/(υ M +γp).
While we showed how to choose reasonable values for γ
andV,videoprovidersaremorefamiliarwithchoosingbuffer
level targets. A method to derive the parameters from buffer
level targets is included in Section VI-B. Alternatively, video
providers might choose γ and V by employing an approach
such as Oboe [23] to auto-tune the BOLA parameters.
V. IMPLEMENTATIONAND EMPIRICAL EVALUATION
Fig. 2. BOLA’s bitrate choice as function of buffer level. (γp = 5,V = We first implemented a basic version of BOLA, named
0.93.)NotethatthebufferlevelisQpseconds. BOLA-BASIC,directlyfrom(11).Recallthatwhenthebuffer
level is full BOLA does not download a segment but waits
for Δ seconds. Rather than picking an arbitrary value for Δ,
we use a dynamic wait until Q(t k ) ≤ V(υ M + γp). This
has the same effect as picking a fixed but very small Δ,
so the theoretical analysis still holds. We also implemented
other versions of BOLA, namely BOLA-FINITE, BOLA-O,
and BOLA-U, that we describe later in this section.
A. Test Methodology
We simulated all versions of BOLA using the Big Buck
Bunny movie [24]. The 10-minute movie was encoded at 10
different bitrates and sliced in 3-second segments. Although
each quality index has a specified average bitrate, segments
may have variable bitrate (VBR) because of the varying
nature of the movie. We simulate playback times longer
than 10 minutes by repeating the movie. Again we choose a
logarithmic utility function: υ m =ln(S m /S 1 ). Table I shows
the mean and standard deviation of the bitrate and segment
size for each quality index and the respective utility values.
TheDASHIndustryForumprovidesbenchmarksforvarious
aspects of the DASH standard [16]. The benchmarks include
twelve different network profiles. Profiles 1–6 have network
bandwidths ranging from 1.5 to 5 Mbps while profiles 7–12
havebandwidthsrangingfrom1to9Mbps.Differentlatencies
Fig. 3. Sample video download and playback using BOLA. (a) The video
are provided for each bandwidth, where the latency is half
isencodedat5differentbitrates.Thenetworkbandwidthvariesfromhighto
lowandbacktohigh.Thedownloadedsegmentbitrateadaptstothenetwork the round-trip time (RTT). Table II shows the odd-numbered
bandwidth. (b) The buffer level variation triggers bitrate changes when it bandwidth characteristics. Profile 1 spends 30s at each of 5,
crossesthethresholds.
4, 3, 2, 1.5, 2, 3 and 4 Mbps respectively, then starts back at
the top. Even-numbered profiles are similar to the preceding
it indirectly affects the buffer level at the beginning of the odd-numbered profiles but start at the low bandwidth stage.
followingslot.Finally,whenallthesegmentsaredownloaded, For example, profile 2 starts at 1.5 Mbps.

| 1704 |     |     |     |     |     |     |     | IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020 |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
TABLEI
BITRATESUSEDFORBIGBUCKBUNNYTESTVIDEO
TABLEII
NETWORKPROFILESFORTHEDASHBENCHMARKS
|              |              |              |               |                 |            |           |           | Fig.4. Calculating         | theofflineoptimalutility |                                    |     | upperbound. |     |     |     |
| ------------ | ------------ | ------------ | ------------- | --------------- | ---------- | --------- | --------- | -------------------------- | ------------------------ | ---------------------------------- | --- | ----------- | --- | --- | --- |
| In addition, | we           | also tested  | our           | algorithmsusing |            | a         | set of 86 |                            |                          |                                    |     |             |     |     |     |
| 3G mobile    | bandwidth    | traces       | that          | are publicly    |            | available | [17].     |                            |                          |                                    |     |             |     |     |     |
| One trace    | was excluded | because      |               | it had          | an average | bandwidth |           |                            |                          |                                    |     |             |     |     |     |
| of 80 kbps;  | our          | lowest video | bitrate       |                 | is 230     | kbps.     | Since the |                            |                          |                                    |     |             |     |     |     |
| traces do    | not include  | latency      | measurements, |                 |            | we used   | 50 ms     |                            |                          |                                    |     |             |     |     |     |
|              |              |              |               |                 |            |           |           | Fig.5. Time-averageutility |                          | forγp=5usingprofile1forBOLA-BASIC. |     |             |     |     |     |
latencygivingaRTTof100msthroughout.Thisisthemedian
| RTT measured |     | empirically | in [25]. |     |     |     |     |               |            |     |     |     |     |     |     |
| ------------ | --- | ----------- | -------- | --- | --- | --- | --- | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
|              |     |             |          |     |     |     |     | C. Evaluating | BOLA-BASIC |     |     |     |     |     |     |
Fig.5showsthetime-averageutilityofBOLA-BASICwhen
| B. Computing | an  | Upper | Bound | on the | Maximum | Utility |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ----- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thevideolengthis10,30and120minutes.Wesetγp=5and
InordertoevaluatehowwellBOLAperformsonthetraces, varied V for different buffer sizes. We compared the utility
| it is important |     | to derive | an upper | bound | on  | the maximum |     |               |      |     |         |         |       |           |     |
| --------------- | --- | --------- | -------- | ----- | --- | ----------- | --- | ------------- | ---- | --- | ------- | ------- | ----- | --------- | --- |
|                 |     |           |          |       |     |             |     | of BOLA-BASIC | with | the | offline | optimal | bound | described |     |
utilitythatisobtainablebyanyalgorithmonagiventrace.We
|     |     |     |     |     |     |     |     | in Section | V-B. The | offline | optimal | gave | nearly | the | same |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | ------- | ---- | ------ | --- | ---- |
deriveanofflineoptimalalgorithmthatprovidesthemaximum utility for the different video lengths. BOLA-BASIC only
| achievable     | utility  | using dynamic |         | programming. |          | We      | define   | a                              |              |           |                           |          |        |       |        |
| -------------- | -------- | ------------- | ------- | ------------ | -------- | ------- | -------- | ------------------------------ | ------------ | --------- | ------------------------- | -------- | ------ | ----- | ------ |
|                |          |               |         |              |          |         |          | obtains                        | about 80% of | the       | offline                   | optimal  | bound. | Also, | the    |
| table r(n,t,b) |          | that contains | the     | maximum      |          | utility | possible |                                |              |           |                           |          |        |       |        |
|                |          |               |         |              |          |         |          | utility of                     | BOLA-BASIC   | decreases |                           | slightly | when   | the   | buffer |
| when we        | download | the nth       | segment | and          | finish   | at time | t with   |                                |              |           |                           |          |        |       |        |
|                |          |               |         |              |          |         |          | size is increasedbecauseitmust |              |           | downloadmorelower-bitrate |          |        |       |        |
|                | b.       |               |         |              | r(0,0,0) |         | = 0.     |                                |              |           |                           |          |        |       |        |
buffer level We initialize the table with Let segments during startup before it can reach the buffer levels
| x(n,t,m) | be the   | time to | download | the      | nth segment |     | at bitrate |          |               |                |            |           |            |     |         |
| -------- | -------- | ------- | -------- | -------- | ----------- | --- | ---------- | -------- | ------------- | -------------- | ---------- | --------- | ---------- | --- | ------- |
|          |          |         |          |          |             |     |            | required | to switch to  | higher-bitrate |            | segments. |            | Our | results |
| index m  | starting | at time | t. Note  | that the | dependency  |     | of x on    |          |               |                |            |           |            |     |         |
|          |          |         |          |          |             |     |            | suggests | that there is | room           | to improve |           | BOLA-BASIC |     | that    |
| n        |          |         |          |          |             |     |            | δ.       |               |                |            |           |            |     |         |
is due to VBR. We quantize the time with granularity motivates our next version.
| While some | accuracy                  | is  | lost, we | ensure | the          | final result | will  |             |         |              |     |        |     |     |     |
| ---------- | ------------------------- | --- | -------- | ------ | ------------ | ------------ | ----- | ----------- | ------- | ------------ | --- | ------ | --- | --- | --- |
| still be   | anupperboundbyroundingthe |     |          |        | downloadtime |              | down. |             |         |              |     |        |     |     |     |
|            |                           |     |          |        |              |              |       | D. Adapting | BOLA to | Finite-Sized |     | Videos |     |     |     |
x (n,t,m)=(cid:9)x(n,t,m)/δ(cid:10)·δ
δ
|     |     |     |     |     |     |     |     | BOLA-BASIC | was | derived | under | the | assumption |     | that the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ----- | --- | ---------- | --- | -------- |
We cap the buffer level at b . videos are infinite. Thus, some adaptations are needed for
max
|     |     |     |     |     |     |     |     | BOLA to | work effectively | with | smaller |     | videos. | Motivated | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | ---- | ------- | --- | ------- | --------- | --- |
x(cid:2)(n,t,b,m)=max[x
|     |     |     | δ (n,t,m),b+p−b |     |     |     | ]   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
δ max our initial experiments, we implemented two adaptations to
y(n,t,b,m) BOLA-BASIC to derive a version we call BOLA-FINITE.
| Let |     | be the rebuffering |     | time. |     |     |     |            |         |     |         |     |            |     |         |
| --- | --- | ------------------ | --- | ----- | --- | --- | --- | ---------- | ------- | --- | ------- | --- | ---------- | --- | ------- |
|     |     |                    |     |       |     |     |     | 1) Dynamic | V value | for | startup | and | wind down: |     | A large |
y(n,t,b,m)=max[x(cid:2)(n,t,b,m)−b,0]
|     |     |     |     | δ   |     |     |     | buffer allows | BOLA-BASIC |     | to perform |     | better | but it | has two |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ---------- | --- | ------ | ------ | ------- |
r(n,·,·) r(n−1,·,·) drawbacks.First, ittakeslongertoprimealargebufferduring
| We generate | entries | for |     | from |     | using |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:17) (cid:18) startup. Lower bitrate segments are preferred until the buffer
r(n,t,b)= max r(n−1,t(cid:2),b(cid:2))+υ −γy(n,t(cid:2),b(cid:2),m) level reaches steady state. Second, at some late stage all
m
m,t(cid:2),b(cid:2)
|     |     |     |     |     |     |     |     | downloads | are complete | and | any remaining |     | buffered | video | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------------- | --- | -------- | ----- | --- |
suchthatt=t(cid:2)+x(cid:2)(n,t(cid:2),b(cid:2),m)andb=b(cid:2)−x(cid:2)(n,t(cid:2),b(cid:2),m)+ played out. Any available bandwidth during this period is not
|     |     | δ   |     |     |     | δ   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
y(n,t(cid:2),b(cid:2),m)+p. utilized. Shorteningthis period would result in less unutilized
The dynamic programming algorithm is shown in Fig. 4. available bandwidth.We mitigate these effects by introducing

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1705
forγp=5usingprofile1forBOLA-FINITE
|     |     |     |     |     |     |     |     | Fig.8. Time-average |     | utility |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | --- | --- | --- | --- | --- |
andBOLA-U.
|     |     |     |     |     |     |     |     | Fig.    | 8 shows | the         | time-average | utility  | of   | BOLA-FINITE |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | ------------ | -------- | ---- | ----------- | ------- |
|     |     |     |     |     |     |     |     |         |         |             |              |          |      |             | γp = 5. |
|     |     |     |     |     |     |     |     | for 10, | 30 and  | 120 minutes | of           | playback | time | with        |         |
ComparingwithBOLA-BASICinFig.5,weseethatthetime-
averageutilityismuchclosertotheofflineoptimalbound.The
|     |     |     |     |     |     |     |     | benefit | of the adjustments |     | is also | evident | as  | the buffer | grows |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | ------- | ------- | --- | ---------- | ----- |
Fig.6. TheBOLAAlgorithm. larger, as there is no significant decrease in utility caused by
fillingthebufferwithlow-bitratesegmentsintheearlierstages
|     |     |     |     |     |     |     |     | of the video. |         |              |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | E. Avoiding   | Bitrate | Oscillations |     |     |     |     |     |
BOLA-FINITE’sDownloadAbandonmentHeuristic:misthecurrent While our performanceobjectiveoptimizesplaybackutility
Fig.7.
andS R andplaybacksmoothness,usersarealsosensitivetoexcessive
| segmentbitrate |     | m isthenumberofbitsremaining |     |     | todownload |     | inthe |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------------------------- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
currentsegment. bitrate switching. We discuss three causes of bitrate switches.
|     |     |     |     |     |     |     |     | 1) Bandwidth |        | variation:   | As the   | network | conditionschange, |            |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ------------ | -------- | ------- | ----------------- | ---------- | --- |
|     |     |     |     |     |     |     |     | the player   | varies | the bitrate, | tracking |         | the network       | bandwidth. |     |
VD
a dynamic which corresponds to a dynamic buffer size Suchswitchesareacceptable;theplayerhasnocontrolonthe
QD , shown in lines 2–5 in Fig. 6. BOLA-FINITE does not bandwidth and should adapt to different network conditions.
max
trytofillthewholebuffertoosoonanddoesnottrytomaintain 2)Densebufferthresholds:Eitheralargernumberofbitrate
3p
a fullbuffertoolong.We still needa minimumbuffersize levelsand/orasmallerbuffersizemaypushthethresholdlev-
for the algorithm to work effectively. els closer. If the differences between threshold levels are less
2) Download abandonment: BOLA-BASIC takes control segmentdurationp,
|     |     |     |     |     |     |     |     | than the |     |     | addingone |     | downloadedsegment |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --------- | --- | ----------------- | --- | --- |
decisions just before the download of each segment. Con- to the buffer may push the buffer level over several threshold
sider a scenario where the player is downloading high-bitrate levels at once. This might cause BOLA-FINITE to overshoot
| 6 Mbps segments |     | in good | network | conditions. |     | The network |     |            |           |     |             |      |         |           |       |
| --------------- | --- | ------- | ------- | ----------- | --- | ----------- | --- | ---------- | --------- | --- | ----------- | ---- | ------- | --------- | ----- |
|                 |     |         |         |             |     |             |     | and choose | a bitrate |     | that is too | high | for the | available | band- |
bandwidth suddenly drops to 1 Mbps as the player has just width.Consequently,the segmentdownloadwouldtake much
started a new segment download. The segment will take more than p seconds, leading to excessive buffer depletion,
6p seconds to download, depleting the buffer and possibly causing BOLA-FINITE to switch down its bitrate by more
| causing rebuffering. |     | BOLA-FINITE |     | mitigates |     | this problem |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ----------- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thanonelevel.InsuchascenarioBOLA-FINITEcanoscillate
by monitoring download progress and possibly abandoning a betweenbitrates,evenwhenthe availablebandwidthisstable.
download. Fig. 7 shows how BOLA-FINITE decides whether 3) Bitrate quantization:Having a stable networkbandwidth
| or not to | abandon | the | download. | If a | segment | at bitrate |     |                   |     |            |     |            |     |       |             |
| --------- | ------- | --- | --------- | ---- | ------- | ---------- | --- | ----------------- | --- | ---------- | --- | ---------- | --- | ----- | ----------- |
|           |         |     |           |      |         |            |     | and widely-spaced |     | thresholds |     | still does | not | avoid | all bitrate |
| m         |         |     |           |      |         | S R        |     |                   |     |            |     |            |     |       |             |
index is being downloaded, the remaining size m is less switching. Suppose the bandwidth is 2.0 Mbps and it lies
S
than m. The segment can be abandoned and downloaded between two encoded bitrates of 1.5 and 3.0 Mbps. While
at some bitrate index m(cid:2) subject to 1 ≤ m(cid:2) < m when the player downloads 1.5 Mbps segments, the buffer keeps
| (VDυ +VDγp−Q)/S |     |     | R < (VDυ | +VDγp−Q)/S |     |     | m(cid:2). |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | -------- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
m m m(cid:2) growing. When the buffer crosses the threshold the player
The control idea remains the same, but the current bitrate switchesto3.0Mbps,depletingthebuffer.Afterthebuffergets
m has a smaller corresponding size S R because part of the sufficiently depleted, the player switches back to 1.5 Mbps,
m
| segment | has already | been | downloaded. |     | Fig. 3 | illustrates | a   |         |                |     |                  |     |          |       |        |
| ------- | ----------- | ---- | ----------- | --- | ------ | ----------- | --- | ------- | -------------- | --- | ---------------- | --- | -------- | ----- | ------ |
|         |             |      |             |     |        |             |     | and the | cycle repeats. |     | In this example, |     | a viewer | might | prefer |
scenario where abandonment might help. At 46s a 3 Mbps the video player to stick to the 1.5 Mbps bitrate, sacrificing
segment download starts. Since there is a bandwidth drop at some utility in order to have fewer oscillations. Or, a viewer
thetime,thesegmenttakesalmost9stodownload.Thebuffer mightwanttomaximizeutilityandplaya partofthevideoin
| is depleted | and | BOLA-BASIC | switches | to  | downloading |     | at a |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | -------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
thehigherbitrateof3.0Mbpsatthecostofmoreoscillations.
bitrate of 0.3 Mbps. BOLA-FINITE with abandonment logic WedescribetwovariantsofBOLAbelowtosuiteitherviewer.
would have detected the rapidly depleting buffer and stopped ThefirstvariantthatwecallBOLA-Omitigatesoscillations
| the long | download, | with | the system | only | dropping | to the | 1.4 |                |     |         |         |        |      |         |         |
| -------- | --------- | ---- | ---------- | ---- | -------- | ------ | --- | -------------- | --- | ------- | ------- | ------ | ---- | ------- | ------- |
|          |           |      |            |      |          |        |     | by introducing |     | bitrate | capping | (lines | 7–20 | in Fig. | 6) when |
and 0.7 Mbps downloadbitrates in the low-bandwidthperiod. switchingto a higherbitrate.BOLA-O verifiesthatthe higher

1706 IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020
Fig. 9. The time-average utility of BOLA-O and BOLA-U with γp = 5 and a 25-second buffer playing a 30-minute video for the DASH test network
profiles1–12andmobiletraces (3G).BOLAutility iswithin84–95%ofofflineoptimalutility.
Fig.10. TheaveragebitratechangebetweenadjacentsegmentswassmallerforBOLA-OthanforBOLA-U,butsomebitratechangeisneededtoaccurately
trackthenetworkbandwidth.Inourexperiments,asanaverageacrossnetworkprofiles,ELASTICandPANDAtrackedthebandwidthwithsimilaraccuracy
toBOLA-O,whileMPCandPensieve hadmoreoscillations.
Fig. 11. The time-average utility ofBOLA-O, BOLA-U, ELASTIC,PANDA, MPC and Pensieve with γp=5 playing a 30-minute video for the DASH
testnetworkprofiles1–12andmobiletraces(3G).ComparedwithELASTICandPANDA,BOLA-Uhasabout1.75timestheutility oftheotheralgorithms
in roughly half the cases. MPC has a utility between BOLA-O and BOLA-U. Pensieve has a utility between BOLA-O and BOLA-U forprofiles 1–12 but
performsworseforthemobile(3G)traces.
bitrateissustainablebycomparingittothebandwidthasmea- bitrate to be one level higher than the sustainable bandwidth
sured when downloading the previous segment (lines 8–11). (line 17). This allows the player to choose 3 Mbps in the
Since the motive is to limit oscillations rather than to predict example. While BOLA-U does not handle the third type of
future bandwidth, this adaptation does not drop the bitrate to oscillations, it handles the more severe second type.
a lower level than in the previous download (lines 12–13). Looking back at Fig. 8, we see that the added stability of
Continuousdownloadingatabitratelowerthanthebandwidth BOLA-UpaysoffwhenusingasmallbuffersizeandBOLA-U
would cause the bufferto keep growing.BOLA-O avoids this achievesa largerutilitythanBOLA-FINITE.Fig.9showsthe
by allowing the buffer to slip to the appropriate threshold time-average utility of BOLA-O and BOLA-U with γp = 5
before starting the download (line 15). and Q p=25s playing a 30-minute video. The utility lost
max
The secondvariantthatwe call BOLA-U doesnotsacrifice byBOLA-Otoavoidoscillationsisclearlyevident.Inpractice
utility. Excessive buffer growth is avoided by allowing the the lost utility is limited by the distance between encoded

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1707
Fig.12. ComparingBOLAwithELASTIC,PANDA,MPCandPensieveusingrawmetrics:averagebitrate andrebuffer-to-play ratio.BOLA,PANDAand
Pensievedonotrebufferforprofiles1–12.ELASTIChasalmostnorebufferingforprofiles1–6,butithasarebuffer-to-playratiogreaterthan20%forprofiles
7–12.MPChassomerebufferingforalmostallprofiles.Pensievehasnorebufferingforprofiles1–12.But,Penseivehasa24%rebuffer-to-play ratioforthe
mobile(3G)traces, asitisunable toperformwellforbandwidth conditions thataresignificantly different fromitstraining set.
bitrates; if the next lower bitrate level is not far from the performs significantly better for the other profiles that have
network bandwidth, then little utility will be lost. larger bandwidth variations. MPC and Pensieve consistently
We measure oscillations by comparing consecutive seg- obtains a utility between BOLA-O and BOLA-U for profiles
ments.Thechangeinbitratebetweenasegmentandthenextis 1–12, but perform worse for the mobile traces. We repeat the
the absolute difference between bitrates (in Mbps) of the two comparisonusingtheaveragebitrateandrebufferingmetricsin
segments. Fig. 10 shows the bitrate change averaged across Fig.12.Thisgivesaninsightintothestrengthsandweaknesses
all the segments. While BOLA-U has a high average bitrate of the different algorithms.
change because of the quantization, BOLA-O only switches Comparing BOLA-U with ELASTIC: For profiles 1–6,
bitrate because of network bandwidth variations. BOLA-U has approximately the same bitrate as ELASTIC.
ELASTIChasahigherbitrateforprofiles7–12,butthatcomes
F. Comparison With State-of-the-Art Algorithms
ata significantcostin termsofrebuffering.Forthese profiles,
We now compare BOLA with four state-of-the art the ratio of the rebuffering time to the play time is more
algorithms,ELASTIC[12],PANDA[13],MPC[14]andPen- than 20% for ELASTIC, while BOLA-U has no rebuffering.
sieve [15].We use thedefaultdesignparametersin [12]–[15]. Forthe mobiletraces,ELASTIChasmarginallyhigherbitrate
We test both BOLA-O and BOLA-U. Although BOLA per- thanBOLA-Ubuthasa12.0%rebuffer-to-playratiocompared
forms better with larger buffers, we limited the buffer size with BOLA-U’s 3.5%. ELASTIC rebuffers significantly more
to 25s for the tests to ensure fairness. ELASTIC targets a because it does not react in time when the bandwidth drops.
buffer level of 15s but the buffer level varies higher. PANDA Comparing BOLA-U with PANDA: Both algorithms do
targetsaminimumbufferlevelof26s.WeusetheRobustMPC notrebufferforprofiles1–12.Forthemobiletraces,BOLA-U
variant of MPC with a buffer size of 25s. MPC relies on and PANDA have a rebuffer-to-play ratio of 3.5% and 2.6%
bandwidthestimation;weusetheharmonicmeanoverthelast respectively. However, PANDA has significantly lower bitrate
five segment downloads to be consistent with the empirical thanBOLA-U.ThereasonisthatPANDAismoreconservative
evaluation method in [14]. We trained a Pensieve neural and in some cases does not change to a higher bitrate even if
network model for the video with a buffer size of 25s. For it is sustainable.
training Pensieve, we used bandwidth traces generated using Comparing BOLA-U with MPC: Both algorithms have
the tool providedin the Pensieve repositoryas recommended. similar average bitrates but MPC has slightly higher bitrate
Fig. 11 compares the algorithms using each of the 12 for some of the profiles. However, while BOLA-U does not
network profiles and the mobile traces. BOLA-U consistently rebuffer, MPC has some rebuffering for most of the profiles.
performs significantly better than PANDA. While BOLA-U While it is possible to tune the MPC parameters to avoid
and ELASTIC perform similarly for profiles 1–6, BOLA-U that rebuffering,it is not clear how to choose parameters that

1708 IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020
Fig.13. Thetime-averageutilityofBOLA-O,BOLA-U,ELASTIC,PANDA,MPCandPensievewithγp=5playingadifferentvideofor30minutes,using
the DASH test network profiles 1–12 and the mobile traces (3G). Note that Pensieve has negative 3G utility because of excessive rebuffering (the average
rebuffer-to-play ratiois38%).Therawmetricsarealsoprovidedintheplotsabove.
consistently work for different network conditions. Another showed similar results. One example is the video provided
factor that might contribute to MPC rebuffering is the band- with Pensieve. The video has 49 segments with a segment
width estimation. When there is a large drop in bandwidth, durationof4s.Itisencodedatsixbitrates:0.3,0.75,1.2,1.85,
the recommended harmonic mean bandwidth estimator takes 2.85and4.3Mbps.Fig.13showstheutilityandmetricsforthe
a while to react. Even though RobustMPC factors in network same six algorithms with similar conclusions to Figs. 10–12.
estimation error, rebuffering is not totally eliminated. Note that Pensieve fails to perform well on mobile traces
Comparing BOLA-U with Pensieve: For profiles 1–12, again, since it is significantly different from its training set.
Pensieve obtains utility between BOLA-O and BOLA-U, but Thus, from our empirical analysis, we can conclude that
consistently closer to BOLA-U. However, Pensieve has too BOLA achieves higher utility, and performs more consis-
muchrebufferinginthemobiletraces,resultinginmuchworse tentlyacrossdifferentscenariosincomparisonwithELASTIC,
utility for these traces. While the network traces used to train PANDA, MPC and Pensieve. One reason for the consistency
Pensieve included periods with low bandwidth similar to the of BOLA is that it does not have a large number of para-
mobile traces, Pensieve did not learn a model that would meters. BOLA has two design parameters γ and V, which
performwellinrelativelylowbandwidthsituationsinamobile have an intuitive significance as discussed in Section IV-B,
setting.ThispointstoaweaknessinPensieveasitisunableto and an option of whether or not to trade off some utility
adapt to bandwidth conditions that are significantly different to reduce oscillations. Other algorithms have a number of
from the training set. different parameters and tuning the parameters for a partic-
In Fig. 10 we show our results for our secondary metric ular scenario might make the system less suited for other
of bitrate oscillations. BOLA-U does not performwell in this scenarios. Also, BOLA’s ability to abandon a segment during
metric, since it attempts to maximize utility at the cost of a download and start the download at a lower bitrate allows
increased oscillations. Comparing BOLA-O with ELASTIC, BOLA to achieve significantly less rebuffering than the other
PANDA, MPC, and Pensieve, ELASTIC has a lower average algorithms.
change than BOLA-O only in the cases where it has a Note: A number of recent papers compare new algorithms
slow reaction and excessive rebuffering. PANDA has a lower with BOLA. Some of the prior work used the experimental
average change because it is more conservative and in some versionof BOLA in dash.js versions2.0.0–2.5.0that required
casesdoesnotchangeto a higherbitrateevenif thatbitrateis bug fixes. We suggestthata stable versionused in production
sustainable.MPChashigheraveragechangethanBOLA-Ofor (dash.js version 2.6.0 or later) be used for such comparisons
profiles1–12.PensievehassimilaraveragechangetoBOLA-O for a more accurate evaluation of BOLA. Also, dash.js has a
for profiles 1–12. defaultbuffersizeof12s,leadingsomeresearcherstocompare
We also tested the algorithms with more videos to inves- a large-bufferalgorithmwith a small-bufferBOLA. Our work
tigate performance when changing characteristics such as uses the correct BOLA implementation and the same buffer
contenttype,segmentduration,andavailablebitrates.Thetests size for all the compared algorithms.

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1709
VI. DEPLOYMENT When calculating the BOLA parameters from Q
low
and
Q , the previous intuition about γ and V still hold. If
A. The DASH Reference Player max
a video provider chooses a larger Q , γ will be larger
low
After developing a theoretical foundation for BOLA and
and BOLA will give more weight to rebuffering. If a video
testing it by simulation, we deployed BOLA in a production provider chooses a larger Q , V will be larger.
max
setting. Particularly, we implemented BOLA in dash.js, the
open-source standard DASH reference player [18]. Through
dash.js, BOLA is now being used in production by several VII. RELATEDWORK
majorvideoprovidersand deliverynetworkssuch as Akamai, There has been a lot of recent work on bitrate adapta-
BBC,CBSandOrange.Deploymentinproductionpresenteda tion algorithms, much of which is based on estimating the
numberofnewchallengessuchasoperatingwithevensmaller bandwidth of the network connection. FESTIVE [10] uses
buffercapacities,correctlyhandlingeventssuchasauserseek a harmonic bandwidth estimator to predict future bandwidth
to a different point in the video, and tolerating delays caused from past downloads, limiting bitrate change to one level
by the video player unrelated to the network conditions. The between successive segments for stability. Notably, FESTIVE
techniques we implemented to handle these new challenges attemptstofindatradeoffbetweenefficiencyandfairnesswith
are described in [19]. competing downloads. BBA [11] is a buffer-based algorithm.
BOLAhasafewsimilaritiestoBBAbutthemappingfunction
B. BOLA Parameters from buffer level to video bitrate is different. Also, BBA
assumes that the buffer size is large (in the order of minutes),
One deployment challenge involves choosing the BOLA
parameters γ and V. We gave an intuition to pick the para- thereby making it not suitable for short videos. Further, it
doesnotprovideanytheoreticalguaranteesforitsbuffer-based
meters in Section IV-B, but video providersare more familiar
approach. A notable algorithm is ELASTIC [12] that uses
with choosing buffer level targets. For this purpose, we now
discuss how to derive γ and V from intuitive requirements. control theory to adjust the bitrate so as to keep the buffer
occupancy at a constant level. Another notable algorithm is
Consider the following requirements:
1. We want a maximum buffer level Q . PANDA [13] which also estimates the network bandwidth.
max
PANDA dropsthe downloadbitrate assoonaslowbandwidth
2.We wantto downloadatthe highestbitratewhenthe buffer
level is Q . is detected but only increases the bitrate slowly to probe
max
the real capacity when a higher bandwidth is detected. Like
3. We want to download at the lowest bitrate when the buffer
levelislessthanathresholdQ ,andwewanttodownloadat FESTIVE, PANDA trades efficiency for fairness. In [14], an
low
algorithm using model predictive control (MPC) is proposed
ahigherbitratewhenthebufferlevelgoesabovethethreshold.
to optimize a comprehensive set of metrics. In this approach,
Theserequirementsareeasytounderstandforvideoproviders
the bitrate for the current segment is chosen based on a
whomightnotbefamiliarwithBOLA.Infact,videoproviders
usually have some preferred maximum buffer level Q . networkbandwidthpredictionforthe nextfewsegments.But,
max
Further, they might have preference for Q such as 10s as its performancedependsonthe accuracyof sucha prediction.
low
The approach also requires significant offline optimization to
described in [19].
be performed outside of the client for an exhaustive set of
To satisfy requirements 1–2, w(cid:7)e want (11) to switch from
choosing a M = 1 to choosing a m = 0 at the threshold scenarios. Reference [15] presents Pensieve, a reinforcement-
when the buffer level is Q . This happens if learning approach to ABR. A neural network model can be
max
trained for a video using a particularbuffer size, using a QoE
ρ aM=1 = ρ a=0 function for reward. A set of bandwidth traces is used as
V(υ +γp)−Q trainingdata. Unfortunately,a trainedmodeldoesnottransfer
M max = 0 (13)
S easily to a different video or, more importantly, to bandwidth
M
conditions not represented in the training data. Unlike prior
Note thatBOLA satisfies requirement2 and downloadsat the
work, we derive a buffer-based algorithm with theoretical
highest bitrate just before the Q threshold because at that
max guarantees that is simple to implement within the client and
buffer level we get ρ am=1 < ρ aM=1 for m < M. This is
we empirically show its efficacy on extensive network traces.
illustrated in Fig. 1.
In recent work [23], a method called Oboe for auto-tuning
To satisfy requirement 3, we want (11) to switch from
the parameters of BOLA and MPC was presented and shown
choosing a = 1 to choosing a = 1 at the threshold when
1 2 to improve both algorithms. Further, the work showed that
the buffer level is Q . This happens if
low Oboe used in conjunction with traditional ABR algorithms
ρ = ρ performs better than reinforcement-learning based ABR such
a1=1 a2=1
V(υ +γp)−Q V(υ +γp)−Q as Pensieve.
1 low = 2 low (14)
S S
1 2
Solving (13)–(14), we obtain
VIII. CONCLUSION
Q −Q υ Q −αQ We formulated video bitrate adaptation for ABR streaming
V = max low, γp= M low max
υ −α Q −Q as a utility maximization problem and derived BOLA, an
M max low
onlinecontrolalgorithmthatisprovablynear-optimal.Further,
where
we empirically demonstrated the efficacy of BOLA using
S υ −S υ
α= 1 2 2 1. extensivetraces.Inparticular,weshowedthatouronlinealgo-
S −S rithm achieves utility close to the optimal offline algorithm.
2 1

1710 IEEE/ACMTRANSACTIONSONNETWORKING,VOL.28,NO.4,AUGUST2020
We showed that our algorithm performs better than state-of- In both cases, D(t k ) is bounded by
the-art algorithms in a number of different test scenarios. We (cid:11) (cid:12)
a D l A so S i H mp re le fe m re e n n c te e d p B la O ye L r A [1 i 8 n ]. da T s h h r . o js u , g t h he da o s p h e . n js - , so B u O rc L e A sta is nd n a o r w d D(t k )≤ p2 2 + p2 Ψ −Q(t k )E T p k− (cid:8)M a m (t k )|Q(t k ) (15)
beingusedinproductionbyseveralmajorvideoprovidersand m= (cid:13) 1 (cid:14)
delivery networks such as Akamai, BBC, CBS and Orange. where Ψ is an upper bound on E T2 under any control
k
algorithm and is assumed to be finite.
Following the methodology of the Lyapunov optimization
ACKNOWLEDGMENT
technique,wesubtractV ×reward termfrombothsidesofthe
The authors would like to thank Daniel Sparacio and Will above to get
Law of Akamai for their key insights on real-world player (cid:11) (cid:12)
(cid:8)M
implementations. Further, Daniel was instrumental in helping
D(t )−VE a (t )(υ +γp)|Q(t )
them implement BOLA in the DASH reference player. k m k m k
m=1 (cid:11) (cid:12)
p2+Ψ T (cid:8)M
APPENDIX ≤ 2p2 −Q(t k )E p k − a m (t k )|Q(t k )
PROOF ORTHEOREM1 (cid:11) m=1 (cid:12)
(cid:8)M
Q
Q
(
(
W t
0
k
)
e )
=
fi ≤ rs
0
t V
.
s
N
( h υ
o
o M
w
w +
s
p
u
a
p
γ rt
p
p
o
1 )
s
+
e
us
i
i 1
t
ng
h
h
o
o i
l
n l
d
d d
s
s u
f
c f
o
t o i
r
r o
s
n k
o
.
m
N =
e
ot 1
k
e
.
s t
W
h in a c
e
t e t
w
h Q e
il
(
l
b t
s
1 o
h
) u
o
n =
w
d −VE m=1 a m (t k )(υ m +γp)|Q(t k ) (16)
that it will also hold for k+1. We have two cases. Letusdenotethecontroldecisions(andresultingslotlengths)
Case 1: Q(t k )≤V(υ M +γp) under our control algorithm by the superscript BOLA while
From the queueing equation (4), it follows that the maximum those underthe stationarypolicyof Lemma1 by STAT.Since
that Q(t k ) can increase in slot k is by 1. This implies that BOLA greedily maximizes over a frame, it ensures that
Q(t
k+1
)≤V(υ
M
+γp)+1. (cid:11)
(cid:8)M
(cid:12)
Case 2: V(υ M +γp)<Q(t k )≤V(υ M +γp)+1 E aBOLA(t )(Q(t )−V(υ +γp))|Q(t )
We have Q(t k ) > V(υ m +γp) for all m ∈ {1,2,...,M} m=1 m (cid:11) k k m k (cid:12)
(using (1)). It follows from the structure of optimal solution
(cid:8)M
to (11) that BOLA will choose the no-download option in ≤ η×E aSTAT(t )(Q(t )−V(υ +γp))|Q(t )
this case. As a result, Q(t k ) cannotincreaseand we have that m=1 m k k m k
Q(t
k+1
)≤V(υ
M
+γp)+1.
(17)
Q(t k ) denotes the total number of segments in the buffer.
This can be at most Q max using the relation where η = E{T k BOLA|Q(t k) } . To see this, compare the ratio on
V ≤
Q
max
−1
.
thelefthand E s { i T d k S e T a A b T o |Q v ( e t k w ) } iththeobjectivei(cid:13)n(11)whileno(cid:14)ting
υ M +γp th (cid:7) at we can express the denominatoras E T k BOLA|Q(t k ) =
In part 2, we show the bound in (12) using the technique c ( an M m b = e 1 m a i B m n O im LA iz ( e t d k ) w S i m th ) o / u ω t a r v e g q . u I i t ri s n h g ou k l n d o b w e le n d o g te e d o t f ha ω tthi . s T ra h t e io n
ofLyapounovoptimizationovervariablesize frames[21].We avg
we use (17) to express (16) as
first define a Lyapunov function L(Q(t k )) as (cid:11) (cid:12)
(cid:8)M
1
L(Q(t k ))= 2 Q2(t k ) DBOLA(t k )−VE aB m OLA(t k )(υ m +γp)|Q(t k )
m=(cid:11)1 (cid:12)
and define the per-slot conditional Lyapunov drift D(t k ) as p2+Ψ TBOLA (cid:8)M
≤ −Q(t )E k −η aSTAT(t )|Q(t )
D(t k )=(cid:2) E{L(Q(t k+1 ))−L(Q(t k ))|Q(t k )}.
2p2
(cid:11)
k p
m=1
m
(cid:12)
k k
(cid:8)M
We use the queueing equation (4), to bound D(t k ). We −VηE aS m TAT(t k )(υ m +γp)|Q(t k )
considertwo cases for (4): Q(t k )≤T k /p and Q(t k )>T k /p. m=1
In the first case we have
Substituting the time-average values for the stationary policy
(cid:11) (cid:19) (cid:20) (cid:12)
1 (cid:8)M 2 1 we get
D(t )=E a (t ) − Q2(t )|Q(t ) . (cid:11) (cid:12)
k 2 m k 2 k k (cid:8)M
m=1 DBOLA(t )−VE aBOLA(t )(υ +γp)|Q(t )
k m k m k
In the second case we have m=1
(cid:11) (cid:19) (cid:20) p2+Ψ (cid:17) 1 (cid:18) (cid:13) (cid:14)
D(t k )=E 2 1 T p k − m (cid:8)M =1 a m (cid:19) (t k ) 2 (cid:20) (cid:12) ≤ − 2 V p ( 2 υ∗+ − γ Q s ( ∗ t ) k E ) (cid:13) p T k − BO r L S A T | A Q T (t k E ) (cid:14) T k BOLA|Q(t k ) (18)
T (cid:8)M
−Q(t ) k − a (t ) |Q(t ) where rSTAT denotes the expected arrival rate under the
k p m k k stationarypolicyandcannotexceed1/psince itis ratestable.
m=1

SPITERIetal.: BOLA:NEAR-OPTIMALBITRATEADAPTATIONFORONLINEVIDEOS 1711
Thus we have [19] K. Spiteri, R. Sitaraman, and D. Sparacio, “From theory to practice:
|     |     |     | (cid:11) |     |     |     |     | (cid:12) |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ImprovingbitrateadaptationintheDASHreferenceplayer,”ACMTrans.
(cid:8)M
|         |      |     |     |          |     |          |     |     | Multimedia         | Comput. Commun.     | Appl., | vol. 15,    | no. 2s, | p.67:1–67:29, |         |
| ------- | ---- | --- | --- | -------- | --- | -------- | --- | --- | ------------------ | ------------------- | ------ | ----------- | ------- | ------------- | ------- |
| DBOLA(t | )−VE |     |     | aB OLA(t | )(υ | +γp)|Q(t |     | )   | 2019.              |                     |        |             |         |               |         |
|         | k    |     |     | m        | k   | m        | k   |     |                    |                     |        |             |         |               |         |
|         |      |     |     |          |     |          |     |     | [20] D. Bertsekas, | Dynamic Programming |        | and Optimal |         | Control,      | vol. 1. |
m=1
p2+Ψ (cid:13) (cid:14) Belmont, MA,USA:AthenaScientific, 1995.
≤ −V(υ∗+γs∗)E T BOLA|Q(t ) (19) [21] M . J. N e e l y , “ S t oc h a s ti c ne t w o r k o p ti m i z a t io n w i th a pp li c a ti on t o
|     |     | 2p2 |     |     |     | k   | k   |     |            |                            |              | S y n t h . | L e ctu re s | Co m m u | n . N etw . |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------------- | ------------ | ----------- | ------------ | -------- | ----------- |
|     |     |     |     |     |     |     |     |     | co mm un i | c a t io n a n d q u e u e | ing s y s te | m s ,”      |              |          | ,           |
vol.3,no.1,pp.1–211,Jan.2010.
Taking conditional expectation of both sides and summing [22] M.J.Neely,“Dynamicoptimizationandlearningforrenewalsystems,”
k ∈{1,2,...,K }, IEEETrans.Autom.Control, vol.58,no.1,pp.32–46,Jan.2013.
| over |     |     | N   | we get |     |     |     |     |                                                                 |     |     |     |     |     |     |
| ---- | --- | --- | --- | ------ | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|      |     |     |     |        |     |     |     |     | [23] Z.Akhtaretal.,“Oboe:Auto-tuningvideoABRalgorithmstonetwork |     |     |     |     |     |     |
(cid:11) (cid:12) conditions,”inProc.Conf.ACMSpecialInterestGroupDataCommun.,
(cid:8)KN (cid:8)M
| (cid:13) |     | (cid:14) |     |     |         |     |     |      | Aug.2018,pp.44–58. |     |     |     |     |     |     |
| -------- | --- | -------- | --- | --- | ------- | --- | --- | ---- | ------------------ | --- | --- | --- | --- | --- | --- |
| E L(Q(t  |     | ))       | −VE |     | aBOLA(t |     | )(υ | +γp) |                    |     |     |     |     |     |     |
KN+1 m k m [24] Big Buck Bunny Movie. Accessed: Jul. 31, 2015. [Online]. Available:
|     |     |     |     | k=1m=1 |     |     |     |     | https://peach.blender.org/ |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
(cid:11) (cid:12)
(cid:8)KN [25] P. Romirer-Maierhofer, F. Ricciato, A. D’Alconzo, R. Franzan, and
(p2+Ψ)K W.Karner,“Network-widemeasurementsofTCPRTTin3G,”inTraffic
|     | ≤   |     | N −V(υ∗+γs∗)E |     |     |     | TBOLA | (20) |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
2p2 k Monitoring andAnalysis.Berlin,Germany:Springer, 2009,pp.17–25.
k=1
|     |     |     |     | (cid:9) (cid:7) |     | (cid:10) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
KN
| Dividing | both | sides  | by  | VE        | TBOLA    |     | and taking | the |     |              |         |                                |             |     |          |
| -------- | ---- | ------ | --- | --------- | -------- | --- | ---------- | --- | --- | ------------ | ------- | ------------------------------ | ----------- | --- | -------- |
|          |      |        |     |           | k=1 k    |     |            |     |     |              |         |                                |             |     |          |
|          | N →∞ |        |     |           |          |     |            |     |     |              |         |                                |             |     |          |
| limit    | as   | yields |     | the bound | in (12). |     |            |     |     |              |         |                                |             |     |          |
|          |      |        |     |           |          |     |            |     |     | KevinSpiteri |         | (Member,IEEE)receivedtheB.Eng. |             |     |          |
|          |      |        |     |           |          |     |            |     |     | degree       | (Hons.) | in electrical                  | engineering |     | from the |
|          |      |        |     |           |          |     |            |     |     | University   | of      | Malta, Msida,                  | Malta,      | and | the M.S. |
REFERENCES
|        |          |               |     |        |               |        |              |     |     | degree  | in electrical | andcomputer | engineering |      | from  |
| ------ | -------- | ------------- | --- | ------ | ------------- | ------ | ------------ | --- | --- | ------- | ------------- | ----------- | ----------- | ---- | ----- |
|        |          |               |     |        |               |        |              |     |     | Oakland | University,   | Rochester,  | MI,         | USA. | He is |
| [1] K. | Spiteri, | R. Urgaonkar, |     | and R. | K. Sitaraman, | “BOLA: | Near-optimal |     |     |         |               |             |             |      |       |
currentlypursuingthePh.D.degreewiththeCollege
bitrateadaptationforonlinevideos,”inProc.35thAnnu.IEEEInt.Conf. of Information and Computer Sciences, University
Comput.Commun.(INFOCOM),Apr.2016,pp.1–9.
|            |           |     |       |        |            |            |              |     |     | of Massachusetts |                  | at Amherst, | Amherst,   | MA, | USA.  |
| ---------- | --------- | --- | ----- | ------ | ---------- | ---------- | ------------ | --- | --- | ---------------- | ---------------- | ----------- | ---------- | --- | ----- |
| [2] Cisco. | (2019).   |     | Cisco | Visual | Networking | Index:     | Forecast     | and |     |                  |                  |             |            |     |       |
|            |           |     |       |        |            |            |              |     |     | His research     | interest         | includes    | algorithms | for | video |
| Trends,    | 2017–2022 |     | White | Paper. | [Online].  | Available: | https://www. |     |     |                  |                  |             |            |     |       |
|            |           |     |       |        |            |            |              |     |     | delivery         | overtheInternet. |             |            |     |       |
cisco.com/c/en/us/solutions/collateral/service-provider/visual-
networking-index-vni/white-paper-c11-741490.html
et al.,
| [3] F.       | Dobrian     |                                       | “Understanding |            | the impact              | of video | quality | on user   |     |     |     |     |     |     |     |
| ------------ | ----------- | ------------------------------------- | -------------- | ---------- | ----------------------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| engagement,” |             | inProc.ACMSIGCOMMConf.,2011,pp.91–99. |                |            |                         |          |         |           |     |     |     |     |     |     |     |
| [4] S.       | S. Krishnan | and                                   | R. K.          | Sitaraman, | “Video                  | stream   | quality | impacts   |     |     |     |     |     |     |     |
| viewer       | behavior:   |                                       | Inferring      | causality  | usingquasi-experimental |          |         | designs,” |     |     |     |     |     |     |     |
inProc.ACMConf.InternetMeas.Conf.(IMC),2012,pp.211–224. RahulUrgaonkar(SeniorMember,IEEE)received
|                    |     |     |                      |     |                           |     |     |     |     | the bachelor’s |     | degree from | IIT Bombay |     | and the |
| ------------------ | --- | --- | -------------------- | --- | ------------------------- | --- | --- | --- | --- | -------------- | --- | ----------- | ---------- | --- | ------- |
| [5] R.K.Sitaraman, |     |     | “Networkperformance: |     | Doesitreallymattertousers |     |     |     |     |                |     |             |            |     |         |
andbyhowmuch?”inProc.COMSNETS,2013,pp.1–10. master’s and Ph.D. degrees from the University of
[6] AppleHTTPLiveStreaming.Accessed:Sep.25,2014.[Online].Avail- Southern California, all in electrical engineering.
able: https://developer.apple.com/resources/http-streaming/ He was with IBM Research, where he was a Task
[7] MicrosoftSmoothStreaming.Accessed:Sep.25,2014.[Online].Avail- Leader with the U.S. Army Research Laboratory
(ARL)fundedNetworkScienceCollaborativeTech-
able: http://www.iis.net/downloads/microsoft/smooth-streaming
|           |      |         |            |     |           |      |           |           |     | nologyAlliance |     | (NSCTA)Program.Hewasalsoa |     |     |     |
| --------- | ---- | ------- | ---------- | --- | --------- | ---- | --------- | --------- | --- | -------------- | --- | ------------------------- | --- | --- | --- |
| [8] Adobe | HTTP | Dynamic | Streaming. |     | Accessed: | Sep. | 25, 2014. | [Online]. |     |                |     |                           |     |     |     |
Available: http://www.adobe.com/products/hds-dynamic-streaming.html PrimaryResearcherwiththeU.S./U.K.International
[9] T. Stockhammer, “Dynamic adaptive streaming over HTTP–standards TechnologyAlliance(ITA)researchprograms.Heis
anddesignprinciples,” inProc.ACMMMSys,2011,pp.133–144. currently aSenior Research Scientist with Amazon
PrimeVideo(PV),whereheworksonoptimizingPV’svideodeliverysystems.
| [10] J. | Jiang,    | V. Sekar,     | and | H. Zhang, | “Improving |           | fairness, | efficiency, |                        |                    |     |               |           |        |     |
| ------- | --------- | ------------- | --- | --------- | ---------- | --------- | --------- | ----------- | ---------------------- | ------------------ | --- | ------------- | --------- | ------ | --- |
|         |           |               |     |           |            |           |           |             | His research interests | include stochastic |     | optimization, | algorithm | design | and |
| and     | stability | in HTTP-based |     | adaptive  | video      | streaming | with      | festive,”   |                        |                    |     |               |           |        |     |
IEEE/ACMTrans.Netw.,vol.22,no.1,pp.326–340,Feb.2014. control theory with applications to communication networks, and cloud-
| [11] T.-Y. | Huang, | R.  | Johari, | N. McKeown, | M.  | Trunnell, | and | M. Watson, | computingsystems. |     |     |     |     |     |     |
| ---------- | ------ | --- | ------- | ----------- | --- | --------- | --- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- |
“Abuffer-basedapproachtorateadaptation:Evidencefromalargevideo
streamingservice,”inProc.ACMConf.SIGCOMM,2014,pp.187–198.
| [12] L. | De Cicco,   | V.         | Caldaralo, | V.          | Palmisano, | and S.    | Mascolo, | “Elastic: |     |     |     |     |     |     |     |
| ------- | ----------- | ---------- | ---------- | ----------- | ---------- | --------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| A       | client-side | controller |            | for dynamic | adaptive   | streaming |          | over HTTP |     |     |     |     |     |     |     |
(DASH),”inProc.PacketVideoWorkshop(PV),2013,pp.1–8.
RameshK.Sitaraman(Fellow,IEEE)receivedthe
[13] Z.Lietal.,“Probeandadapt:RateadaptationforHTTPvideostreaming
|     |     |     |     |     |     |     |     |     |     | B.Tech. | degree | from IIT Madras, | Chennai, |     | and the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------------- | -------- | --- | ------- |
at scale,” IEEE J. Sel. Areas Commun., vol. 32, no. 4, pp.719–733, Ph.D. degree in computer science from Princeton
| Apr.2014. |     |     |     |     |     |     |     |     |     | University. | He  | is currently | a Professor |     | with the |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ----------- | --- | -------- |
[14] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic CollegeofInformationandComputerSciences,Uni-
| approach |     | for dynamic | adaptive | video | streaming | over | HTTP,” | in Proc. |     |         |                  |     |          |     |          |
| -------- | --- | ----------- | -------- | ----- | --------- | ---- | ------ | -------- | --- | ------- | ---------------- | --- | -------- | --- | -------- |
|          |     |             |          |       |           |      |        |          |     | versity | of Massachusetts | at  | Amherst. | His | research |
ACMSIGCOMM,2015,pp.325–338.
focusesonInternet-scaledistributedsystems,includ-
[15] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream- ing algorithms, architectures, performance, energy
ing with pensieve,” in Proc. Conf. ACM Special Interest Group Data efficiency, security, and economics. As a princi-
Commun.,Aug.2017,pp.197–210. pal architect, he helped create the Akamai Content
[16] DASH Industry Forum. (Jan. 2014). Guidelines for Implementa- Delivery Network (CDN), the world’s first major
| tion: | DASH-AVC/264 |     | Test | Cases | and Vectors. |     | [Online]. | Available: |                    |            |             |             |              |          |     |
| ----- | ------------ | --- | ---- | ----- | ------------ | --- | --------- | ---------- | ------------------ | ---------- | ----------- | ----------- | ------------ | -------- | --- |
|       |              |     |      |       |              |     |           |            | CDN that currently | delivers a | significant | fraction of | the Internet | traffic. | He  |
http://dashif.org/guidelines/ retains a part-time role as the Akamai’s Chief Consulting Scientist. He is a
[17] H.Riiser,P.Vigmostad,C.Griwodz,andP.Halvorsen,“Commutepath Fellow of the ACM. He was a recipient of the inaugural ACM SIGCOMM
bandwidthtracesfrom3Gnetworks:Analysisandapplications,”inProc. Networking Systems Award for his work on the Akamai CDN, the DASH-
4thACMMultimedia Syst.Conf.(MMSys),2013,pp.114–118. IF Excellence in DASH Award for his work on ABR algorithms, the NSF
[18] DASH Reference Client. Accessed: Jun. 28, 2019. [Online]. Available: CAREERAward,theCollegeofNaturalSciencesOutstandingTeacherAward,
https://reference.dashif.org/dash.js/ andtheUMassDistinguished Teaching Award.