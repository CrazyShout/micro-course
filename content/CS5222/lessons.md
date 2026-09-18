# CS5222 连续微课主稿

本稿的主线是“一次网页访问经过哪些机制”。串讲与数值变式为 AI 教学补充；来源通过 CARDS 关联到原课件。历史内容维持 Extra Resources 标记。题答的 ` || ` 分隔中文与英文。

@@ net01 | 从一次网页访问认清网络里的角色 | The actors in a web request
CARDS: N001,N002,N003,N004,N005,N006,N007,N008,N009,N010,N011,N012
PREREQ:
GOAL: 能在主机、接入网、路由器与链路图上追踪一条消息。
EXPLAIN: 浏览器和网页服务器是应用所在的端系统。它们通常不直接相连，而是经过接入网、多个路由器和链路。链路携带比特，路由器按规则选择下一段路；Internet 则把很多自治管理的网络连接成可以互通的系统。

先画“主机—接入链路—路由器—其他网络—服务器”。接入技术决定最初怎样连入网络，例如无线共享介质或有线链路，但不单独决定完整端到端表现。链路速率表示每秒可送入多少比特，传播速度表示信号在介质中移动多快，二者不是同一种快。

协议约定消息的格式、发送顺序和收到消息后采取的动作。就像预约服务要知道请求格式与应答含义，应用之间也需要共同规则；只有两台设备都能发送比特，还不足以理解彼此。
RECAP_EN: Hosts run applications; links carry bits; routers forward packets across interconnected networks. A protocol specifies message formats, ordering, and actions, not merely a physical connection.
WORKED_Q: 手机经 Wi-Fi 连路由器，再到远端网站，浏览器程序、无线段和中间转发分别属于什么角色？ || In a phone-to-website path via Wi-Fi and routers, identify the browser, wireless segment, and intermediate forwarding roles.
WORKED_A: 浏览器是端系统应用；Wi-Fi 是接入链路的一部分；路由器负责跨网络转发。服务器是另一端的应用主机。 || The browser is an end-system application, Wi-Fi supplies an access link, routers forward across networks, and the server is the other application host.
PRACTICE_Q: 笔记本经以太网链路、路由器 R、运营商网络访问服务器 S。按顺序指出端系统、接入链路、中间转发设备和另一端系统；哪处运行网页应用？ || A laptop reaches server S through an Ethernet link, router R, and an ISP network. Identify endpoint, access link, forwarding device, other endpoint, and where the web applications run.
HINT: 沿消息行进方向读，每个名称先判断是应用所在设备还是输送路径。 || Follow the message path, distinguishing application hosts from delivery infrastructure.
PRACTICE_A: 笔记本是端系统，以太网是接入链路，R 是转发设备，S 是另一端系统。浏览器在笔记本运行，网页服务在 S 运行；链路本身不运行这两个应用。 || The laptop and S are endpoints, Ethernet the access link, and R a forwarding router. The browser runs on the laptop and the web service on S, not on the link itself.
TRANSFER_Q: 手机成功将数据经路由器送到服务器，但服务器应用不理解请求格式。网络中的输送角色是否因此足以保证网页显示？说明协议还规定什么。 || A phone’s data reaches a server via routers, but the server application cannot understand the request format. Is successful delivery sufficient for a webpage to work? Explain what a protocol must additionally specify.
TRANSFER_A: 不足以。端到端应用还要对消息格式、交互顺序和收到消息后的动作达成一致；路由器完成转发不能替代应用协议的正确处理。 || No. Applications must agree on message format, exchange order, and actions on receipt. Router forwarding does not substitute for correct application-protocol processing.
BRIDGE: 共享网络怎样安排多个用户发送，要先理解电路交换与分组交换。

@@ net02 | 分组交换：共享容量与等待的来源 | Packet switching and statistical multiplexing
CARDS: N013,N014,N015,N016,N017,N018,N019,N020,N021,N022,N023,N024,N095,N096,N097,N098
PREREQ: net01
GOAL: 能比较预留用户数与实际活跃需求，解释分组共享的容量收益与拥塞条件。
EXPLAIN: 电路交换先预留通信资源，例如固定时隙；即使某时刻没数据，该份额仍被保留。分组交换把消息切成包，多个用户按需共享链路。突发流量通常不同时达到峰值，共享可以更灵活，但同时到达超过输出容量时需要排队。

存储转发表示路由器先收到一个完整分组，再将它发上下一条链路。因此一个分组经过两条链路，需要在每条链路各付一次发送全部比特的时间。但不同分组可以在不同链路同时前进，后面会把这点写成流水线时间轴。

算概率时，先把每个用户想成“上传 / 休息”开关。三个人只有八种开关状态：下面“三个人抢 Wi-Fi”会先数一遍，再把这个计数方法写成二项分布。不必第一次见到公式就硬背 35 人的大题。模型要求用户独立且活跃概率相同；真实用户可能一起追直播，所以理想概率不是无拥塞保证。当前课堂 Q&A 与 Tutorial 同题的选项字母可能不同，应记判断依据。
RECAP_EN: Circuit switching reserves resources; packet switching shares them on demand and may queue. Store-and-forward waits for a complete packet at each intermediate router.
WORKED_Q: 1 Mbps 链路，每个活跃用户需 100 kbps，预留式可支持多少个同时用户？ || A 1 Mbps link allocates 100 kbps per active user. How many simultaneous reserved-rate users fit?
WORKED_A: 1000/100=10 个。分组共享可接入更多用户，但若同时活跃超过 10，就不能都立即获得该速率。 || Ten users fit. Packet sharing may admit more users, but more than ten simultaneously active users cannot all immediately obtain that rate.
PRACTICE_Q: 链路 2 Mbps，每个活跃用户需要 250 kbps。预留式最多支持几人？分组共享接入 12 人但只有 5 人活跃时，需求是多少，是否超过容量？ || A 2 Mbps link serves users requiring 250 kbps when active. How many reserved users fit? With 12 packet-sharing users but only five active, what is demand and does it exceed capacity?
HINT: 先把 2 Mbps 换成 2000 kbps，再分别做除法和乘法。 || Convert to 2000 kbps, then divide for reservations and multiply for active demand.
PRACTICE_A: 预留最多 2000/250=8 人；5 人活跃需 1250 kbps，小于 2000。接入用户数不等于同时活跃数；理想平均需求可容纳，不保证每个突发包零排队。 || Eight reserved users fit. Five active users demand 1250 kbps, below 2000. Admitted users need not all be active; fitting average demand does not guarantee zero burst queueing.
TRANSFER_Q: 同一 2 Mbps 链路上 12 个用户因直播同时活跃，每人需 250 kbps。总需求与超出容量是多少？为什么“平时很少一起用”不能保证这次无拥塞？ || On a 2 Mbps link, 12 users simultaneously need 250 kbps each during a live stream. Compute demand and excess, and explain why usually sparse activity does not guarantee no congestion now.
TRANSFER_A: 总需求 3000 kbps，超出 1000 kbps。容量只能送出 2000 kbps，持续超额使队列增长或丢包；这次活动相关，不能把独立低活跃概率当保证。 || Demand is 3000 kbps, exceeding capacity by 1000. Sustained excess grows queues or causes drops; correlated activity invalidates any guarantee based on independent low activity.
BRIDGE: 接下来区分“把包送上链路”和“包沿链路传播”，再画完整时延。

@@ net03 | 时延：数清第一个比特和最后一个比特 | Serialization, propagation, and pipelines
CARDS: N025,N026,N027,N028,N029,N030,N031,N032
PREREQ: net02
GOAL: 能用时间轴推出单包与多包到达时间，避免死套公式。
EXPLAIN: 传输时延 L/R 是把整个包的比特依次放上链路的时间；传播时延 d/s 是已经上链路的信号走到另一端的时间。二者可以重叠：第一比特已在路上时，后面的比特还未发出。忽略其他时延，首位约在 d/s 到达，末位在 L/R+d/s 到达。

一个包经过多条存储转发链路，需要逐段累计发送与传播。多个等长包经过 H 条等速链路时，首包需 H 个发送时段，后续每个包每隔一个时段到达，所以忽略传播等项时总时长为 $(H+P-1)L/R$。等速、等长、连续发送和无额外交叉流量是这条式子的条件。

四项节点时延还包括处理与排队。每次解题都先声明完成事件：首位、整包、全部包或应用响应。若事件不同，即使同一张网络图也会得到不同答案。
SYMBOLS: L | 包长，bit；R | 链路速率，bit/s；d | 距离，m；s | 传播速度，m/s；H | 链路数；P | 分组数
RECAP_EN: Serialization puts all bits onto a link; propagation moves bits through the medium. Define the completion event before adding delays, and derive pipeline timing from overlapping transmissions.
DEMO: delay
WORKED_Q: 1500 byte，2 Mbps，1000 km，传播速度 2×10^8 m/s，末位何时到达？ || For 1500 bytes, 2 Mbps, 1000 km, and propagation speed 2×10^8 m/s, when does the last bit arrive?
WORKED_A: 包长 12000 bit，发送时间 6 ms；距离 10^6 m，传播 5 ms；末位 11 ms 到达，首位约 5 ms 到达，忽略处理与排队。 || Serialization takes 6 ms and propagation 5 ms. The last bit arrives after 11 ms and the first after about 5 ms, ignoring processing and queueing.
PRACTICE_Q: 三条等速链路、四个包，每包发送需 2 ms，忽略其余时延，总时间多少？ || Four packets cross three equal-rate links, taking 2 ms per packet per link. Ignoring other delays, find completion time.
HINT: 先算第一包，然后数后面三个到达间隔。 || Compute the first packet's arrival, then three additional arrival intervals.
PRACTICE_A: 先画发送时段：第一包在三条链路依次占 0–2、2–4、4–6 ms，于 6 ms 到达。第二、三、四包每隔 2 ms 到达，为 8、10、12 ms。总 12 ms；三个路由阶段可处理不同包，不能算成 3×4×2=24 ms。 || Packet 1 uses successive links during 0–2,2–4,4–6 ms, arriving at 6. Packets 2,3,4 then arrive at 8,10,12 ms. Different packets occupy different links concurrently, so total time is 12 rather than 24 ms.
TRANSFER_Q: 单链路包长 1500 byte、速率 2 Mbps、距离 1000 km、传播速度 2×10^8 m/s，忽略处理排队。只将包长减半，独立算首位与末位到达时间，并解释哪项不变。 || For one link with packet length 1500 bytes, rate 2 Mbps, distance 1000 km and propagation speed 2×10^8 m/s, ignore processing and queues. Halve only the packet length and compute first- and last-bit arrival times.
TRANSFER_A: 首位约仍在 d/s 到达；末位的发送部分减半，传播部分不变。本例末位变为 3+5=8 ms。 || First-bit arrival stays about d/s. Last-bit serialization halves while propagation is unchanged, giving 8 ms in the worked example.
BRIDGE: 时延描述等多久；吞吐量描述持续交付多快，排队把二者联系起来。

@@ net04 | 容量、吞吐量和排队为什么不能混用 | Capacity, throughput, and queueing
CARDS: N033,N034,N035,N036,N037,N038,N039,N040
PREREQ: net03
GOAL: 能计算输入负载并由到达事件解释排队；瓶颈与共享吞吐量见补充单元。
EXPLAIN: 一条路径的持续单流吞吐量受最慢环节约束。在无其他限制的理想模型中，不超过各链路速率的最小值；应用有效吞吐量还要扣开销、重传，并考虑共享和协议窗口。提高非瓶颈链路常常没有效果。

平均包长 L、到达率 a、链路速率 R 给出负载 rho=La/R。它比较输入工作量与服务容量，不直接给出某个包要等多久。两个平均负载相同的流量，一个均匀到达，一个集中突发，可以有完全不同的排队。

无限缓冲的常见随机队列模型在接近饱和时等待会急剧上升；有限缓冲则会丢包。加大缓冲区不增加链路速率。Traceroute 每跳显示的是探测往返时间，不能把相邻行相减就当成已验证的单向链路时延。
RECAP_EN: Capacity is an upper bound, throughput is achieved delivery rate, and queueing depends on traffic timing as well as average load. High throughput can coexist with long response delay.
WORKED_Q: 平均 1000 byte，每秒 100 包，1 Mbps 链路，负载是多少？ || For 1,000-byte average packets at 100 packets/s on a 1 Mbps link, compute load.
WORKED_A: 输入 8000×100=800000 bit/s，rho=0.8。不能据此说每个包只等待发送时间的 20%。 || Input load is 800,000 bit/s, so rho=0.8. This does not specify a per-packet waiting time.
PRACTICE_Q: 平均包长 1000 byte、到达率 100 包/秒保持不变，链路速率改为 2 Mbps。计算输入速率与负载 rho，能否由 rho 唯一得出平均排队时延？ || Keep average packets at 1000 bytes and arrivals at 100/s, but use a 2 Mbps link. Compute input rate and rho; does rho uniquely determine mean queueing delay?
HINT: 输入是 bit/秒；rho 是输入除以服务速率，不是等待秒数。 || Input has units bit/s; rho is input divided by service rate, not a waiting time.
PRACTICE_A: 输入仍为 1000×8×100=800000 bit/s，rho=0.4。不能唯一确定时延，还需要到达时间模式、包长与缓冲等假设。 || Input remains 800000 bit/s, hence rho=0.4. Delay additionally depends on arrival timing, packet sizes, buffering, and other model assumptions.
TRANSFER_Q: 每包发送 1 ms，队列初始为空，每 8 ms 重复一次四包到达。模式 A 到达 0、2、4、6 ms；模式 B 四包都在 0 ms 到达。分别求负载和平均排队时间（不含自身发送）。 || Each packet takes 1 ms, the queue starts empty, and four arrivals repeat every 8 ms. Pattern A arrives at 0,2,4,6 ms; pattern B sends all four at time zero. Find load and mean queueing time excluding own transmission.
TRANSFER_A: 两种每 8 ms 都需服务 4 ms，rho=0.5。A 四包各等 0，平均 0；B 等待 0、1、2、3 ms，平均 1.5 ms。相同负载不等于相同排队。 || Both require 4 ms service per 8 ms, giving rho=0.5. A has zero waiting; B waits 0,1,2,3 ms, averaging 1.5 ms. Equal load does not imply equal delay.
BRIDGE: 要说明开销和协议功能来自哪里，需要分层与封装。

@@ net05 | 分层：每层首部回答一个不同的问题 | Layering and encapsulation
CARDS: N041,N042,N043,N044,N045,N046,N047,N048,N049,N050,N051
PREREQ: net01
GOAL: 能按应用—传输—网络—链路的封装顺序追踪消息，并计算载荷与首部开销。
EXPLAIN: 应用层定义消息含义；传输层联系进程；网络层跨网络送分组；链路层在本段链路送帧；物理层传信号。发送方逐层加入控制信息，接收方按对应规则解释和去除，这就是封装与解封装。

可以把它看成不同层次的地址与约定：应用问“请求什么”，端口问“哪个进程”，IP 问“目的接口/网络在哪里”，本地链路地址问“这一跳交给谁”。普通路由器转发无需理解最终网页内容，但要处理所在链路帧与 IP 信息。

基础 IP 网络尽力而为，不承诺一定送达；高层可以补可靠交付。加密主要回答“旁人能否读懂”，认证回答“身份或消息来源是否可信”，完整性验证回答“内容是否被改过”；具体机制可组合提供这些属性，单有加密不自动具备全部属性。源 IP 不能代替身份认证。分层是职责模型，不意味着现实设备严格只处理某一层。
RECAP_EN: Each layer adds control information for a distinct service. End-to-end applications depend on lower-layer delivery, but reachability and source addresses do not by themselves establish authentication or confidentiality.
WORKED_Q: 1000 byte HTTP 应用数据交给 TCP、IP、Ethernet，题设每层都加 20 byte 首部，不计尾部。写出四层职责和最终大小、应用载荷效率。 || Pass 1000 bytes of HTTP data through TCP, IP and Ethernet, each adding a 20-byte header in this model and no trailer. Identify layer roles, final size and application-payload efficiency.
WORKED_A: HTTP 属应用层；TCP 提供进程间传输；IP 负责跨网寻址与转发；Ethernet 完成本段链路交付。大小依次 1000→1020→1040→1060 byte；效率 1000/1060≈94.34%。这些 20 byte 是题设教学值，不是所有真实 Ethernet 首部的固定大小。 || HTTP is application, TCP transport, IP network, and Ethernet link layer. Sizes become 1000,1020,1040,1060 bytes, yielding 94.34% payload efficiency. The 20-byte values are this exercise’s assumptions, not a universal Ethernet header size.
PRACTICE_Q: 同一教学封装模型，每层首部 20 byte、无尾部，应用数据改为 500 byte。逐层补出大小和效率。 || With the same three 20-byte headers and no trailer, use 500 bytes of application data. Compute each size and payload efficiency.
HINT: 每次增加 20；效率的分母是最终发送大小。 || Add 20 at each step; divide payload by final transmitted size.
PRACTICE_A: 500→520→540→560 byte；效率 500/560≈89.29%。固定首部下，小消息的开销占比更高。 || Sizes are 500,520,540,560 bytes; efficiency is about 89.29%. With fixed headers, smaller messages devote a larger fraction to overhead.
TRANSFER_Q: 一个路由器将 IP 数据报从链路 A 转到链路 B。假设无 NAT、无 IP 分片，原链路帧的目的 MAC 是路由器，下一段目的 MAC 应指谁？应用数据是否应增加一个新的 HTTP 首部？ || A router forwards an IP datagram from link A to link B without NAT or fragmentation. Its incoming destination MAC names the router. Whom should the next link destination identify, and should the router add another HTTP header?
TRANSFER_A: 下一段 MAC 应标识该段下一跳接口，路由器更换本地链路封装。它不作为这次 HTTP 应用的终点，不应额外加 HTTP 首部；IP 中某些转发字段可更新，但原端到端应用载荷仍保留。 || The next frame targets the next-hop interface on link B. The router replaces link framing, rather than adding an HTTP header. Forwarding fields in IP may change, but the end-to-end application payload is retained.
BRIDGE: 应用通过 socket 使用传输服务，但仍要定义自己的消息协议。

@@ net06 | 应用与 socket：进程需要什么服务 | Applications and transport services
CARDS: N052,N053,N054,N055,N056,N057,N058,N059,N060,N061,N062,N063,N064,N065
PREREQ: net04,net05
GOAL: 能根据应用需求讨论可靠性、速率与时延，而不机械选 TCP/UDP。
EXPLAIN: 客户端—服务器架构由持续服务的一方响应请求；P2P 允许节点同时提供与消费资源。架构回答角色怎样组织，传输协议回答进程间怎样交付数据，二者不能互相替代。

Socket 是应用与传输服务之间的接口。IP 与端口帮助定位进程端点，但不会自动定义业务消息格式。TCP 提供可靠有序字节流，UDP 保留数据报边界却不自行提供 TCP 那套可靠机制。应用可以在 UDP 上增加重传、排序等逻辑，所以“某应用用 UDP”不能推出它没有任何可靠性。

实时语音和文件下载的错误代价不同：过晚的语音片段可能不再有用，文件少一个字节却可能不完整。先列需求，再讨论协议提供什么、应用还需补什么。TCP 本身也不保证固定吞吐量或时延上界。
RECAP_EN: Application architecture and transport service are separate choices. Select mechanisms from delivery, timing, and throughput requirements, and distinguish built-in transport guarantees from application-added behavior.
WORKED_Q: 文件下载与实时通话对“迟到但最终正确”的数据通常有何不同？ || How do file download and live conversation differ in their treatment of late but correct data?
WORKED_A: 文件通常需要完整正确内容，适当等待可接受；实时语音过晚的数据可能已失去播放价值。具体容忍度仍由应用设计决定。 || A file generally requires complete correct content and can tolerate some delay; very late voice data may no longer be useful. Exact tolerance depends on the application.
PRACTICE_Q: 远程备份文件要求每个字节最终正确；在线语音的一段声音若晚 5 秒就失去播放价值。分别写出主要可靠性/时延需求，说明为什么不能只按平均速率选协议。 || A backup needs every byte eventually correct; a voice segment arriving five seconds late is useless. State the key reliability and delay needs and why average rate alone cannot select a protocol.
HINT: 问“允许缺失吗”“迟到还有效吗”，再谈可靠机制与缓冲。 || Ask whether omissions are allowed and late data remains useful before selecting recovery and buffering.
PRACTICE_A: 备份强调完整性和可靠完成，语音强调及时播放且可能容忍部分丢失。相同速率下，重传等待、抖动和应用缓冲仍影响效果；协议选择需要具体设计。 || Backup prioritizes integrity and reliable completion; voice prioritizes timeliness and may tolerate some loss. At equal rate, recovery delay, jitter, and buffering can still differ; protocol choice requires an application design.
TRANSFER_Q: 控制命令要求 100 ms 内送达且不能重复执行。仅说“UDP 延迟低，所以选 UDP”遗漏了哪些需求？给出判断框架，不假设某协议自动满足全部要求。 || A control command must arrive within 100 ms and must not execute twice. What is missing from “choose UDP because it is low-latency”? Give a decision framework without assuming a transport automatically meets every requirement.
TRANSFER_A: 要检查丢失时重试能否赶上时限、如何编号与去重、应用收到后如何确认执行、拥塞及网络条件。UDP 不自动提供可靠或恰好一次执行，TCP 也不自动保证 100 ms 或应用只执行一次。 || Check deadline-compatible retries, identifiers and deduplication, execution acknowledgments, and network/congestion conditions. UDP alone guarantees neither reliability nor exactly-once execution; TCP alone guarantees neither the deadline nor exactly-once application execution.
BRIDGE: HTTP 把应用请求与响应具体化；其时延需要连同传输连接来分析。

@@ net07 | HTTP：沿依赖顺序数 RTT | HTTP timing, persistence, and caching
CARDS: N066,N067,N068,N069,N100,N101,N102,N103,N104,N105,N106,N107,N108,N109,N110
PREREQ: net03,net06
GOAL: 能画出 TCP 建连、基础页面、附属对象与缓存命中的依赖。
EXPLAIN: 浏览器先得到基础 HTML，才知道其中还引用哪些对象。非持久 HTTP 在简化模型中每个对象新建 TCP 连接：一个 RTT 建连，一个 RTT 请求与首批响应，再加对象发送时间。这个 2RTT 是课堂模型，需要忽略 DNS、TLS、慢启动等项才可直接使用。

持久连接像保留一条已接通的电话线，省去的是反复接通的成本；没有流水线时仍逐个请求等待。流水线和并行连接又会改变批次。先画“基础页完成 → 得知两个对象 → 发起对象请求”，再数哪些可以同时发生，避免把“每个对象两 RTT”套到所有场景。

Cookie 让无状态请求携带可关联的状态标记；缓存减少重复传输。条件 GET 在验证未修改时可收到 304，减少响应正文，但验证往返仍存在。缓存命中率只能用于明确区分本地与远端时延的模型。这里的 HTTP/1.x 时序不能无条件外推为所有现代版本行为。
RECAP_EN: HTTP completion time follows dependency order. Persistent connections, parallelism, and caching change different costs; a 304 response saves body transfer but still requires validation communication.
WORKED_Q: DNS 已完成，基础 HTML 和两个对象都很小，RTT=50 ms。串行非持久与一条无流水线持久连接各多久？ || DNS is done. A tiny base HTML and two tiny objects use RTT=50 ms. Compare serial nonpersistent HTTP with one persistent, non-pipelined connection.
WORKED_A: 非持久三个对象各 2RTT，共 6RTT=300 ms。持久连接一次建连 RTT，加三次请求 RTT，共 4RTT=200 ms。假设无 TLS 且传输时间可忽略。 || Nonpersistent HTTP takes 6 RTTs, or 300 ms. Persistent non-pipelined HTTP takes one setup RTT plus three request RTTs, or 200 ms, under the stated simplified assumptions.
PRACTICE_Q: 同样条件下，基础页面取回后两条新非持久连接同时取两个对象，共多少 RTT？ || Under the same assumptions, fetch both embedded objects over two parallel new connections after the base page arrives. How many RTTs in total?
HINT: 基础页 2 RTT，后一批对象同时完成。 || The base page costs 2 RTTs; the parallel object batch completes together.
PRACTICE_A: 2+2=4 RTT，即 200 ms。 || Four RTTs, or 200 ms.
TRANSFER_Q: DNS 已完成且持久 TCP 连接已建好，RTT=50 ms。缓存中的小页面需要条件验证，服务器返回 304；忽略处理、发送时间和 TLS。此次验证至少占几个 RTT？省掉了什么、没省掉什么？ || DNS is complete and a persistent TCP connection is open with RTT 50 ms. A cached tiny page requires conditional validation and receives 304. Ignore processing, serialization and TLS. How many RTTs does validation take, and what is saved?
TRANSFER_A: 该模型一次请求与响应占 1 RTT=50 ms。省去未修改页面的正文传输，仍须发验证请求和等响应；若还需建连，应另加建连时间。 || One request/response takes 1 RTT=50 ms. The unchanged body is not retransmitted, but the validation exchange remains; opening a connection, if needed, would add separate time.
BRIDGE: 同样使用应用协议，电子邮件却把发送、存储与读取拆成不同阶段。

@@ net08 | 电子邮件：发送信件与读取信箱是两条流程 | Mail delivery versus mailbox access
CARDS: N111,N112,N113,N114,N115,N116,N117,N118,N119,N120
PREREQ: net06
GOAL: 能按发送界面、服务器投递、收件读取追踪邮件协议；信封与邮件头见补充单元。
EXPLAIN: 用户代理把邮件交给邮件服务器，服务器之间用 SMTP 传递；收件人之后通过 IMAP、POP3 或 Webmail 访问邮箱。邮件到达服务器与用户已经阅读不是同一个事件。

SMTP 的 MAIL FROM 与 RCPT TO 构成传输信封，决定投递与退信等路由信息；DATA 里面的 From、To 等头部属于邮件内容。两者可以不同，不能只看显示头就还原全部传输端点。

POP3 常见下载后删除或保留模式；IMAP 侧重服务器上邮箱状态的同步与管理。Webmail 的浏览器一段通常用 HTTP，后面的服务器邮件传递仍可用 SMTP。协议角色应按哪两个实体在通信来判断。
RECAP_EN: SMTP delivers messages between mail systems; mailbox access is a separate stage. The SMTP envelope and message headers serve different roles and may contain different addresses.
WORKED_Q: 浏览器打开网页邮箱发信，浏览器与网站、邮件服务器与对方邮件服务器分别用什么应用协议角色？ || When sending through webmail, distinguish the browser-to-site and mail-server-to-mail-server protocol roles.
WORKED_A: 浏览器访问 Webmail 使用 HTTP 相关交互；邮件系统对外传递可使用 SMTP。不能因界面是网页就说整个投递过程只用 HTTP。 || Browser access uses HTTP interactions, while mail delivery between servers can use SMTP. A web interface does not make the entire delivery path HTTP-only.
PRACTICE_Q: Alice 用网页邮箱向 Bob 发信；Bob 用本地邮件客户端通过 IMAP 读取。依次填入 Alice浏览器→网页邮箱、发送邮件服务器→接收邮件服务器、Bob客户端→邮箱服务器 的应用协议。 || Alice sends from webmail and Bob reads using a local IMAP client. Fill the protocols for browser→webmail, sending→receiving mail server, and Bob’s client→mailbox server.
HINT: 区分网页界面、服务器间投递和收件访问三段。 || Separate the web interface, inter-server delivery, and mailbox access.
PRACTICE_A: 依次为 HTTP/HTTPS、SMTP、IMAP。三段功能不同，用户看到网页不意味着整个邮件路径只用 HTTP。 || The roles are HTTP/HTTPS, SMTP, and IMAP, respectively. A web interface does not make the entire delivery path HTTP.
TRANSFER_Q: 将 Bob 的读取方式也改为网页邮箱。发送服务器到接收服务器仍使用 SMTP。画出三段协议，并说明 Bob 浏览器是否因此直接发送 IMAP 命令。 || Bob now reads through webmail; inter-server delivery still uses SMTP. Identify the three protocol legs and say whether Bob’s browser must directly issue IMAP commands.
TRANSFER_A: Alice浏览器→网页服务是 HTTP/HTTPS；邮件服务器间为 SMTP；Bob浏览器→网页服务是 HTTP/HTTPS。浏览器不必直接使用 IMAP；网页服务后台如何访问邮箱是另一段实现，不能凭界面推断。 || Both browser–webmail legs use HTTP/HTTPS, while inter-server delivery uses SMTP. Bob’s browser need not issue IMAP; backend mailbox access is a separate implementation detail not established by the interface.
BRIDGE: 浏览器与邮件服务器都常需要把名称解析为地址，下一节追踪 DNS。

@@ net09 | DNS：沿层级找答案，靠缓存少走路 | DNS resolution and caching
CARDS: N121,N122,N123,N124,N125,N126,N127,N128,N129,N130,N131,N132,N133,N134
PREREQ: net06,net07
GOAL: 能区分本地解析器、根、TLD、权威服务器及递归/迭代。
EXPLAIN: 用户通常把名字交给本地递归解析器，而不是亲自向所有层级查询。解析器可向根询问下一步，再找 TLD，再找该域的权威服务器，直到获得所需记录。根服务器不需要保存互联网所有主机地址，它提供委派方向。

递归请求是“请替我完成解析并回答”；迭代回答可说“去问这个服务器”。这是交互方式，不是服务器名称的同义词。A/AAAA 给 IPv4/IPv6 地址，NS 指定域的权威服务器，MX 指向邮件交换服务器，CNAME 建立别名。一个名称可以对应多个地址，也可能经过别名链，所以域名不等于一台唯一机器。

缓存让后续解析跳过已知步骤，TTL 控制记录可被缓存使用多久。它不会保证记录全球同时刷新。计算 DNS 时间要列出哪些缓存为空、哪些交互串行、每一步 RTT 如何定义。原图与不同文件页码在关联卡片中保留。
RECAP_EN: A recursive resolver follows delegations and caches records. Root, TLD, and authoritative roles are distinct; resolution delay depends on the actual cache state and dependency chain.
WORKED_Q: 主机向本地递归解析器查一个域名，RTT=2 ms。无相关缓存，解析器依次问根、TLD、权威服务器，三个串行上游交互各 20 ms。列出各自返回的角色，并算总时延。 || A host queries a local recursive resolver in a 2 ms RTT. With no relevant cache, the resolver queries root, TLD, and authoritative servers sequentially, each taking 20 ms. Describe their answer roles and total delay.
WORKED_A: 主机要求解析器完成解析；根给 TLD 委派方向，TLD 给权威服务器方向，权威服务器给所需最终记录（本简化场景）。三次上游往返串行嵌在主机一次等待内，总 2+20+20+20=62 ms；忽略处理、别名链等。 || The host asks the resolver to finish resolution. Root refers toward TLD, TLD toward authority, and the authority supplies the final record in this simplified case. Upstream exchanges occur sequentially within the host’s wait, giving 2+3×20=62 ms, ignoring processing and alias chains.
PRACTICE_Q: 主机到本地解析器 RTT=2 ms，解析器已有该域名的有效最终 A 记录。还需要问根、TLD、权威服务器吗？同一模型下用时多少？ || Host-to-resolver RTT is 2 ms and the resolver caches a valid final A record. Are root, TLD and authoritative queries needed, and what is delay in the same model?
HINT: 不再访问上游层级。 || No upstream exchanges are needed.
PRACTICE_A: 只需本地交互的 2 ms。 || The delay is two milliseconds.
TRANSFER_Q: 主机到解析器 RTT=2 ms；缓存中只有可直接访问的正确 TLD 服务器地址，没有域的权威委派或最终记录。TLD 和权威交互各 20 ms，串行且无别名。跳过哪步，总时间多少？ || Host-to-resolver RTT is 2 ms. Only the usable address of the correct TLD server is cached, not the domain’s authoritative delegation or final record. TLD and authoritative exchanges each take 20 ms sequentially, with no aliases. What is skipped and what is total delay?
TRANSFER_A: 跳过根查询，但仍需 TLD 获取权威委派，再问权威取得记录。总 2+20+20=42 ms；缓存了一个中间方向不等于已有最终答案。 || Skip the root query but still ask TLD for the authoritative delegation and authority for the record. Total is 42 ms; an intermediate referral is not a final-answer cache hit.
BRIDGE: 回到当前教程，把时延、容量和应用依赖合成完整解题过程。

@@ net10 | 当前教程：先画事件，再计算 | A method for current tutorial problems
CARDS: N071,N072,N073,N074,N075,N076,N077,N078,N079,N080,N081,N082,N083,N084,N085,N099
PREREQ: net02,net03,net04
GOAL: 能独立列出网络数值题的单位、路径、完成事件和忽略项。
EXPLAIN: 每题先写四行：图中几条链路、包或报文多大、从哪个时刻到哪个事件、忽略了哪些项。再把 byte 转 bit、km 转 m，最后才选公式。链路数和路由器数通常差一；每个分组完整到达与整段文件全部到达也不是同一事件。

切包题先求首包经过所有链路的时间，再数后续包到达间隔。若有不等速链路、首部、交叉流量或处理延迟，应按具体时间轴重新分析，不能继续套最简等速式。图题的正面给出原图或按原条件重绘的示意，题干同时写清必要条件；不要只记选项字母。

Traceroute 表中的时间是各次探测的往返观测。不同探测可能经历不同排队或返回路径，星号也可能只是未及时收到 ICMP 回复。计算之前先识别每列真正测量的对象。
RECAP_EN: Define path, units, completion event, and ignored costs before calculating. A correct formula with the wrong event or units still answers the wrong question.
WORKED_Q: 8×10^6 bit 经三条 2 Mbps 存储转发链路，整报文与 800 个 10000 bit 包比较，忽略其他开销。 || Compare an 8×10^6-bit message with 800 packets of 10,000 bits over three 2 Mbps store-and-forward links, ignoring other costs.
WORKED_A: 整报文每段 4 s，共 12 s。分包每包每段 0.005 s，流水线总时间 (3+800-1)×0.005=4.01 s。 || The whole message takes 12 s. Packet serialization is 0.005 s, giving a pipeline completion time of 4.01 s.
PRACTICE_Q: 同样网络只发一个 10000 bit 包，需要多久？ || How long does a single 10,000-bit packet take over the same path?
HINT: 没有后续包可流水线重叠。 || There are no following packets to overlap.
PRACTICE_A: 3×0.005=0.015 s，即 15 ms。 || The delay is fifteen milliseconds.
TRANSFER_Q: 三条等速 2 Mbps 存储转发链路传 800 个包，每包载荷 10000 bit，另加 100 bit 首部，忽略传播与处理。独立算流水线总时间；与忽略首部的 4.01 s 比较。 || Three equal 2 Mbps store-and-forward links carry 800 packets, each with 10000 payload bits plus 100 header bits. Ignore propagation and processing. Find pipeline completion time and compare with 4.01 s when headers are omitted.
TRANSFER_A: 每包发送 (10000+100)/(2×10⁶)=0.00505 s；总 (3+800−1)×0.00505=4.0501 s。首部使结果增加 0.0401 s，说明原先越小越快的直觉依赖忽略开销。 || Each packet takes 0.00505 s, so total time is 802×0.00505=4.0501 s, an increase of 0.0401 s. The simpler packetization comparison depends on its overhead assumptions.
BRIDGE: 当任务变成研究报告，仍要保持“观测支持哪些结论”的意识。

@@ net11 | 研究与 QE：从机制解释到可验证结论 | Evidence and explanation in networking
CARDS: N086,N087,N088,N093,N094
PREREQ: net04,net05,net09
GOAL: 能用英文区分测量现象与因果结论，并设计有控制条件的网络比较。
EXPLAIN: 解释网络问题可以按“现象—可能机制—区分证据—适用边界”展开。例如网页慢可能来自 DNS、建连、服务器、传输或渲染；只测到总时长，无法直接定位哪个机制占主导。先提出能区分原因的测量，再给结论。

研究报告从具体问题出发，阅读原始论文的设定、方法、实验和限制，说明证据支持了什么。课件中的理想模型用来理解机制；真实抓包和实验用来判断具体系统。两者需要对照，不能把模拟条件、旧协议实现或历史统计直接当当前系统事实。

英文口述先定义指标，再说明机制，给一个例子并加适用条件。当前报告的页数、格式与提交要求请看网页“课程信息”中的研究报告说明；这里提供方法练习，不猜测教师尚未发布的安排。
RECAP_EN: Define the metric, explain a mechanism, identify discriminating evidence, and state the scope of the conclusion. A model or measurement answers only the question its assumptions support.
WORKED_Q: 一次网页访问用了 2 秒。用三句英文写：能观察到什么、还不能断言什么、接下来要拆分测量什么。 || A page load took two seconds. Write three English sentences stating the observation, an unsupported causal claim, and the measurements needed next.
WORKED_A: 示范：“The measured page-load time is two seconds. This observation alone does not show that insufficient bandwidth caused the delay. I would separate DNS, connection setup, server waiting time, and body transfer under a stated cache condition.” 三句分别是观测、边界、检验。 || The measured page-load time is two seconds. This observation alone does not show that insufficient bandwidth caused the delay. I would separate DNS, connection setup, server waiting time, and body transfer under a stated cache condition.
PRACTICE_Q: 访问同一资源：冷缓存测到 200 ms，热缓存 80 ms，但两次网络负载未知。用英文补全：The warm run was …; this does not yet prove …; I would control …。 || The same resource takes 200 ms cold and 80 ms warm, but network load differs or is unknown. Complete: The warm run was …; this does not yet prove …; I would control … .
HINT: 先报告观察差异，再区分缓存作用与其他变化，最后提出控制和重复。 || Report the difference, separate cache effects from other changes, and propose controls and repetition.
PRACTICE_A: “The warm run was 120 ms faster. This does not yet prove that caching alone caused the improvement. I would control the resource, network and server conditions, record cache hits or revalidation, and repeat both conditions.” || The warm run was 120 ms faster. This does not yet prove that caching alone caused the improvement. I would control the resource, network and server conditions, record cache hits or revalidation, and repeat both conditions.
TRANSFER_Q: 替代路径只在夜里测一次，比白天测的原路径快。独立用三句英文解释为何不能保证改路由后普遍更好，并给一个更公平的比较方案。 || An alternative route measured once at night beats the original route measured during daytime. Explain in three English sentences why this does not guarantee a general improvement and propose a fairer comparison.
TRANSFER_A: 可答：“The observations confound route choice with time and load. Moving traffic can also change congestion, so the result need not generalize. I would compare repeated measurements under matched time, traffic and endpoint conditions, report variation, and state the routing-policy assumptions.” 评分看混杂因素、负载变化、可比较方案三个要点。 || The observations confound route choice with time and load. Moving traffic can also change congestion, so the result need not generalize. I would compare repeated measurements under matched time, traffic and endpoint conditions, report variation, and state the routing-policy assumptions.
BRIDGE: 后续预习从应用扩展到可靠传输、IP、路由与链路层，再回到完整网页访问。

@@ net12 | P2P 与 socket：资源共享也需要消息边界 | Distribution capacity and socket framing
CARDS: N135,N136,N137,N138,N139,N140,N141,N142,N143,N144,N145,N146,N147,N148
PREREQ: net04,net06,net09
GOAL: 能分开计算服务器注入、最慢下载与总上传下界；TCP 应用定界见补充单元。
EXPLAIN: 客户端—服务器分发 N 份大小 F 的文件，服务器至少上传 NF，最慢客户端至少下载 F，因此时间下界是 max(NF/us,F/dmin)。P2P 让客户端也贡献上传，增加总服务资源，但服务器仍至少要注入一份文件，最慢下载也仍是约束。

理想 P2P 下界为 max(F/us,F/dmin,NF/(us+sum ui))。这些是流体、充分协作等理想条件下的容量分析，不包含节点离线、协议开销或块稀缺问题。DASH 与 CDN 则分别通过适配码率和内容位置缓解应用体验问题。

实现消息协议时，TCP 给的是字节流，一次 send 不保证对应一次 recv。应用要定义长度前缀或分隔符、编码与最大长度，并缓冲不完整消息。UDP 保留数据报边界，但仍要处理丢失等问题。
RECAP_EN: Distribution lower bounds follow server upload, receiver download, and aggregate upload constraints. TCP applications must frame messages independently of send/receive call boundaries.
SYMBOLS: F | 一份文件大小，bit；N | 接收者数量；u_s | 服务器上传速率；u_i | 第 i 个对等节点上传速率；d_min | 最慢接收者下载速率；速率单位 | 所有速率统一为 bit/s
WORKED_Q: F=1 Gbit、N=10、us=100 Mbps、每个 ui=10 Mbps、dmin=50 Mbps，求两种理想下界。 || For F=1 Gbit, N=10, us=100 Mbps, each ui=10 Mbps, and dmin=50 Mbps, find client-server and P2P lower bounds.
WORKED_A: 客户端—服务器 max(100,20)=100 s；P2P max(10,20,10000/200)=50 s。这里 Gbit/Mbps 按十进制换算。 || Client-server requires at least 100 s; P2P requires at least max(10,20,50)=50 s, using decimal units.
PRACTICE_Q: F=1 Gbit、N=10、服务器上传 us=100 Mbps、最慢下载 dmin=50 Mbps，每个对等节点上传由 10 提高到 30 Mbps。求新的 P2P 理想下界 max(F/us,F/dmin,NF/(us+Σui))。 || For F=1 Gbit,N=10,server upload 100 Mbps and slowest download 50 Mbps, raise each peer upload from 10 to 30 Mbps. Compute the new P2P lower bound max(F/us,F/dmin,NF/(us+Σui)).
HINT: 先按十进制把 F 换成 1000 Mbit，再分别算三个限制。 || Convert F to 1000 Mbit, then calculate the three constraints separately.
PRACTICE_A: 服务器注入 1000/100=10 s；最慢下载 1000/50=20 s；总上传限制 10000/(100+10×30)=25 s。因此理想下界 25 s，不是承诺真实实现恰好达到。 || The constraints are 10 s,20 s,and 10000/400=25 s. The lower bound is 25 s, not a guarantee that a real system attains it.
TRANSFER_Q: 仍为 F=1 Gbit、N=10、us=100 Mbps、dmin=50 Mbps，若每个对等节点上传升至 90 Mbps，下界是多少？相对各 30 Mbps 的 25 s，为何没有缩成三分之一？ || Keep F=1 Gbit,N=10,us=100 Mbps,dmin=50 Mbps and raise each peer upload to 90 Mbps. Compute the bound and explain why it is not one third of the 25 s bound with 30 Mbps peers.
TRANSFER_A: 三个限制为 10、20、10000/(100+900)=10 s，最大值 20 s。现在最慢下载限制主导，提高总上传不能突破它。 || The limits are 10,20,and 10 seconds, so the bound is 20 seconds. The slowest download now dominates, preventing a threefold reduction.
BRIDGE: 应用想要可靠消息，先看传输层怎样处理损坏、丢失和重复。

@@ net13 | 可靠传输：为什么 ACK、序号、定时器缺一不可 | Reliability and sliding windows
CARDS: N149,N150,N151,N152,N153,N154,N155,N156,N157,N158,N159,N160,N161,N162,N163,N164,N165,N166
PREREQ: net03,net05,net06
GOAL: 能用丢包事件逐步追踪基础 GBN 与 SR 的接收、确认与重传差别。
EXPLAIN: 校验和帮助检测损坏，却不保证检测一切错误，也不负责重传。ACK 告诉发送者接收进展；如果 ACK 丢了，发送者可能重发已送达数据，所以接收者还需要序号识别重复。数据或 ACK 完全丢失时，定时器让发送者最终再尝试。

停等每发一包就等确认。这里 RTT 专指往返传播时间，另忽略处理、排队与 ACK 发送时间；一个周期是发送数据所需的 L/R 加往返传播，所以 $U=(L/R)/(RTT+L/R)$。若题目给的是“开始发送到收到 ACK”的完整周期，就不能再加一遍 L/R。窗口允许多个包在途，减少长距离链路上“发一下、等很久”的空档。

基础 GBN 丢弃失序包并重复累计确认；超时时重传从最早未确认包开始、所有已发送但未确认的包，不包含窗口内尚未发送的位置。SR 缓存失序包、分别确认，仅对相应未确认包触发重传。常见等长发送/接收窗口的 SR 要求序号空间至少为窗口的两倍，并假定旧副本不会无限存活；这不是对任意长期旧包都安全的保证。
RECAP_EN: Checksums, ACKs, sequence numbers, and timers address different failure modes. Pipelining fills the path; GBN and SR trade retransmission work against receiver state and sequence-space requirements.
WORKED_Q: 序号为包编号。依次发 0、1、2、3，只有 1 丢失，0/2/3 按发送顺序到达；ACK 不丢，尚未超时。GBN 采用“ACK k 表示截至 k 连续收到”，SR 单独确认。列出收到 0、2、3 后的接收行为。 || Packet numbers are 0,1,2,3. Only packet 1 is lost; 0,2,3 arrive in order, ACKs are delivered, and no timeout has occurred. GBN ACK k acknowledges all packets through k; SR acknowledges individually. Trace arrivals 0,2,3.
WORKED_A: GBN：收 0 交付并 ACK0；收 2、3 因缺 1 都丢弃，分别重复 ACK0。SR：收 0 交付并 ACK0；收 2 缓存并 ACK2，收 3 缓存并 ACK3，仍等 1 才连续交付后续数据。 || GBN delivers 0 and ACKs 0; it discards 2 and 3 and repeats ACK0. SR delivers 0, then buffers and individually ACKs 2 and 3 while waiting for 1 before contiguous delivery.
PRACTICE_Q: 接续同一完整条件：发 0–3、1 丢失、2/3 到达、各 ACK 成功；发送者的 1 超时，尚未发送其他包。GBN 与 SR 分别重传哪些包？ || Continue the stated event: packets 0–3 were sent, 1 lost, 2 and 3 arrived, their relevant ACKs were delivered, no further packets sent, and 1 times out. What does each sender retransmit?
HINT: 区分“已发送但未累计确认”和“对应未单独确认”的集合。 || Distinguish the cumulatively unacknowledged set from the individually unacknowledged packet.
PRACTICE_A: GBN 重传 1、2、3，因为都未累计确认；SR 只重传 1，因为 2、3 的 ACK 已到。不要把窗口中还没发送的位置算进重传集合。 || GBN retransmits 1,2,3; SR retransmits only 1 because 2 and 3 were individually acknowledged. Unsent window positions are not retransmissions.
TRANSFER_Q: 独立变式：包 0、1 已连续收到并确认；发出的 2、3、4 中只有 3 丢失，2 和 4 按序到达，ACK 不丢。写出 GBN/SR 对 4 的行为，以及 3 超时后的重传集合。 || Variation: 0 and 1 were received and acknowledged; among sent packets 2,3,4 only 3 is lost, while 2 and 4 arrive in order and ACKs are delivered. Describe each protocol’s response to 4 and retransmissions when 3 times out.
TRANSFER_A: 收 2 后连续前缀到 2。GBN 丢弃 4 并重复 ACK2，超时重传 3、4；SR 缓存 4 并 ACK4，超时仅重传 3。到达的乱序包是否保留，直接改变后续重传集合。 || The contiguous prefix reaches 2. GBN discards 4, repeats ACK2, and later retransmits 3 and 4. SR buffers and ACKs 4, then retransmits only 3. Keeping out-of-order data changes what must be retransmitted.
BRIDGE: TCP 将这些思想用于可靠有序字节流，并加入连接与流量状态。

@@ net14 | TCP：用字节编号描述接收进度 | TCP sequence space and flow control
CARDS: N167,N168,N169,N170,N171,N172,N173,N174,N175,N176,N177
PREREQ: net13
GOAL: 能从字节范围和缺口推累计 ACK；接收与拥塞窗口限额见补充单元。
EXPLAIN: TCP 数据序号按字节计数。把接收想成按页拼好一本书：即使第 3 页先到了，第 2 页的缺口仍存在。累计 ACK 表示下一期待的字节号，不是最近见过的最大序号。后面的字节可以缓存，但只要前面有缺口，累计 ACK 就停在缺口起点，有序字节流也不能把这段后的内容提前交给应用。

RTT 会波动，重传超时既要参考平滑均值，也要留给波动的余量。对有歧义的重传样本还需谨慎测量。课程数值题可能采用指定更新顺序，不能混用不同公式约定。

流量控制用接收窗口 rwnd 保护接收端缓冲；拥塞窗口 cwnd 保护网络，发送者受两者较小值约束，还要扣除已在途数据。握手同步连接状态与初始序号，关闭两个方向可以分开完成。教材简化模型用于理解，具体实现细节需单独确认。
RECAP_EN: TCP acknowledges a contiguous byte prefix by naming the next expected byte. Receiver flow control and network congestion control impose separate limits on outstanding data.
DEMO: tcp
WORKED_Q: 已按序收到至字节 999，接着收到 seq=1000、长 500 byte 的数据段，ACK 是多少？ || Bytes through 999 are contiguous, then a segment starts at 1000 with 500 data bytes. What ACK follows?
WORKED_A: 新段覆盖 1000–1499，下一期待 1500，ACK=1500；假设没有 SYN/FIN 等额外序号消耗。 || The segment covers bytes 1000–1499, so ACK=1500, assuming no extra SYN/FIN sequence-space consumption.
PRACTICE_Q: 已经连续收到字节 0–1499，之后收到 seq=1500、长度 300 byte 的数据段，无 SYN/FIN。补出最后一字节编号和下一累计 ACK。 || Bytes 0–1499 have arrived contiguously. A segment starts at 1500 and carries 300 data bytes, with no SYN/FIN. Find its last byte and next cumulative ACK.
HINT: 最后编号为起点+长度−1；ACK 是下一期待编号。 || The final byte is start+length−1; ACK names the next expected byte.
PRACTICE_A: 末字节为 1500+300−1=1799；下一期待 1800，所以 ACK1800。 || The last byte is 1799, so the next expected byte and ACK are 1800.
TRANSFER_Q: 已连续收到字节 0–535，后来收到 900–1000；再收到 536–899，接收方保留了原乱序段。前后两次累计 ACK 分别是多少？无 SYN/FIN。 || Bytes 0–535 arrived contiguously, followed by 900–1000, then 536–899. The receiver retained the out-of-order segment. What are the ACKs after the latter two arrivals, with no SYN/FIN?
TRANSFER_A: 收到 900–1000 后仍缺 536，ACK536；补齐 536–899 后，已缓存后段接上，连续范围变 0–1000，所以 ACK1001。ACK 看连续前缀，不仅看最近段的终点。 || The first gap remains 536 after the out-of-order segment, so ACK536. Filling 536–899 connects the buffered tail, making the contiguous prefix end at 1000, hence ACK1001.
BRIDGE: 接收者装得下，不代表网络送得动；接下来解释拥塞窗口怎样变化。

@@ net15 | 拥塞控制：试探可用容量，响应拥塞 | Congestion windows and feedback
CARDS: N178,N179,N180,N181,N182,N183,N184
PREREQ: net04,net14
GOAL: 能在明确的理想 TCP 教学模型中追踪慢启动、加性增长与丢包后的窗口变化。
EXPLAIN: 发送者通常不知道路径当前能承受多少流量，需要根据确认、丢包或显式拥塞信号调整在途数据。经典慢启动在适当假设下每 RTT 近似翻倍；名字描述相对于立即大窗口发送的起步方式，并非线性慢增长。

拥塞避免常用近似每 RTT 增加一 MSS 的加性增长；拥塞事件后缩小窗口。Tahoe、Reno 对三次重复 ACK 与超时的处理不同，Reno 的快速恢复还有临时窗口膨胀。答图题时先识别采用的协议版本、事件和观察时刻，再谈窗口数值。

窗口除 RTT 可以估计受窗口限制的发送率。在理想稳定 AIMD 锯齿中，窗口由 W/2 增到 W，平均约 3W/4。这个近似不是所有 TCP 的普遍公式。按连接公平也不等于按用户公平，一个用户可能开很多连接。
RECAP_EN: Congestion control adapts sending to network feedback, distinct from receiver flow control. Classic textbook window trajectories depend on protocol version and event timing.
WORKED_Q: 教学模型以 MSS 为单位：每轮开始记录 cwnd，初始 1，阈值 4；无丢包时若 cwnd<4，下一轮翻倍但最多到 4，达到阈值后每轮加 1。列前五轮窗口。 || In an idealized model measured in MSS, record cwnd at each round’s start. Begin at 1 with threshold 4; below threshold double up to 4, then add 1 per round. With no loss, list the first five windows.
WORKED_A: 第 1 轮 1；收到足够 ACK 后第 2 轮 2；第 3 轮 4 达阈值；之后加性增长，第 4、5 轮为 5、6。序列 1,2,4,5,6；这套按轮更新是假定足够 ACK 的课堂模型。 || Windows are 1,2,4,5,6. The first two updates double up to the threshold; subsequent updates add one. This round-based model assumes acknowledgments permit the stated growth.
PRACTICE_Q: 使用同一按轮规则，但初始 cwnd=2、阈值=8、无丢包。列前五轮。 || Use the same round-based rule with initial cwnd=2 and threshold 8, with no loss. List five rounds.
HINT: 先翻倍到阈值，再切换为每轮加 1。 || Double to threshold, then add one per round.
PRACTICE_A: 依次为 2,4,8,9,10 MSS。达到 8 后不再继续翻倍到 16。 || The windows are 2,4,8,9,10 MSS; reaching 8 changes the rule instead of doubling to 16.
TRANSFER_Q: cwnd=8 MSS 时发生丢包。按此题简化模型，三次重复 ACK 后跳过快速恢复细节、直接从 cwnd=4、阈值4进入拥塞避免；超时后从 cwnd=1、阈值4进入慢启动。分别列事件后的四轮窗口。 || At cwnd=8 MSS, compare this simplified model: after triple duplicate ACKs, omit fast-recovery details and resume at cwnd=4,threshold=4; after timeout restart at cwnd=1,threshold=4. List the next four rounds in each case.
TRANSFER_A: 重复 ACK 路径为 4,5,6,7；超时路径为 1,2,4,5。二者恢复阶段不同。这里只验证题设更新规则，不能把省略快速恢复的数字套到任意真实 TCP 实现。 || Duplicate-ACK recovery gives 4,5,6,7; timeout recovery gives 1,2,4,5. These follow the stated simplified rules and should not be imposed on arbitrary TCP implementations.
BRIDGE: 端到端传输依赖 IP 跨网转发，下一节解释地址、前缀与分片。

@@ net16 | IP：前缀决定下一跳，MTU 决定装多大 | Addressing, forwarding, and fragmentation
CARDS: N185,N186,N187,N188,N189,N190,N191,N192,N193,N194,N195,N196,N197,N198,N199,N200,N201,N202,N284,N285
PREREQ: net03,net05
GOAL: 能由二进制前缀计算普通 IPv4 子网范围和可用主机数；转发与分片分别练习。
EXPLAIN: 转发是按已有表把当前分组送到下一接口；路由是形成和更新这些路径信息。最长前缀匹配选择对目的地址描述最具体的条目，例如 /24 优先于同样匹配的 /16。IP 地址通常关联接口，不应机械等同整台设备或用户身份。

IPv4 前缀 /p 表示前 p 位固定，其余位可变化；普通子网常保留网络与广播地址，但 /31、/32 等需要不同规则。DHCP 可分配地址并提供网关与 DNS 等配置；NAT 可改写地址与端口并记录映射状态。

MTU 是本条链路能装下的最大 IP 数据报大小，包含 IP 首部。允许 IPv4 分片时，把原载荷切片，每片另有首部；除末片外，数据长度须为 8 byte 的倍数，因为 offset 按原载荷中的 8 byte 块计位置。MF=1 表示后面还有片，0 表示最后一片。基本 IPv4 在最终目的端重组；IPv6 路由器不执行这种分片，需由源端采用相应机制。
RECAP_EN: Forwarding applies a table; routing builds it. Prefixes aggregate destinations, while MTU constrains datagram size. IPv4 fragment offsets count eight-byte blocks of original payload.
WORKED_Q: 求 192.0.2.130/26 的网络、广播和普通可用主机范围。IPv4 共32位，每个十进制字节8位；本题采用保留网络/广播的普通子网规则。 || Find network, broadcast, and ordinary usable host range for 192.0.2.130/26. IPv4 has 32 bits, eight per octet; reserve network and broadcast addresses in this exercise.
WORKED_A: 主机位 32−26=6，所以一块有 2⁶=64 地址。前三字节固定，末字节以 0、64、128、192 为块起点；130 在 128–191。也可写 130=10000010₂，保留前两位 10：主机位全0给128，全1给191。网络 .128、广播 .191，可用 .129–.190，共62个。 || There are six host bits, hence 64 addresses per block. Last-octet blocks start at 0,64,128,192, and 130 lies in 128–191. In binary 130=10000010; retain prefix 10, set host bits to all zeros or ones to obtain 128 or 191. Hosts are .129–.190, totaling 62.
PRACTICE_Q: 用同样普通子网规则求 192.0.2.77/27 的网络、广播、可用范围与数量。先补 32−27，再找包含77的块。 || Find network, broadcast, usable range and count for 192.0.2.77/27 under the same ordinary rule. Start with 32−27 and locate the block containing 77.
HINT: 5个主机位给每块32个地址，块边界按32递增。 || Five host bits give blocks of 32, with boundaries in multiples of 32.
PRACTICE_A: 32−27=5，2⁵=32；77 在64–95。网络 .64、广播 .95、可用 .65–.94，共30个。 || Five host bits give 32 addresses. The block is 64–95, so network .64, broadcast .95, usable .65–.94, count 30.
TRANSFER_Q: 一个普通 IPv4 子网需至少50台主机，候选 /26 与 /27 中选最小足够的地址块，并给出包含192.0.2.77的网络/广播地址。说明为何另一个不够。 || A normal IPv4 subnet needs at least 50 hosts. Choose the smallest sufficient block from /26 and /27, and find its network/broadcast addresses containing 192.0.2.77. Explain why the other fails.
TRANSFER_A: /27 只有2⁵−2=30个可用，/26有2⁶−2=62个，因此选/26。77落在64–127块，网络192.0.2.64、广播192.0.2.127。/31和/32等特殊规则不在本题假设内。 || /27 has 30 usable hosts and /26 has 62, so choose /26. The containing block is .64–.127: network 192.0.2.64 and broadcast 192.0.2.127. Special /31 and /32 conventions are outside this exercise.
BRIDGE: 转发表从哪里来，需要路由算法与自治系统政策来解释。

@@ net17 | 路由：局部下一步怎样形成整条路径 | Shortest paths and routing policy
CARDS: N203,N204,N205,N206,N207,N208,N209,N210,N211,N212,N213,N214,N215,N216
PREREQ: net16
GOAL: 能逐步执行非负边权Dijkstra并在边代价变化后更新路径；距离向量见补充单元。
EXPLAIN: 链路状态方法让节点获得拓扑信息，再计算路径。Dijkstra 在非负边权下，每次选未确定节点中暂定距离最小者；它的距离已不会被绕远的未确定路径改善，然后松弛相邻边。前驱用于还原路径，转发表则需要从源开始的第一跳，两者不一定同一个节点。

距离向量只与邻居交换到目的地的估计，更新为 $D_x(y)=\min_v[c(x,v)+D_v(y)]$。它像比较“先去哪个邻居，再接邻居所知的后半程”。坏消息传播可能缓慢，并出现计数到无穷。

互联网分为自治系统，内部可用 OSPF 等协议，跨系统 BGP 还受政策和路径属性约束。AS-PATH 帮助检测 AS 级环路；不能把 BGP 说成全互联网统一跑 Dijkstra。路由选择中的“最好”取决于所用目标。
RECAP_EN: Dijkstra fixes shortest distances from topology under nonnegative costs; distance vector composes neighbor estimates. Internet routing also uses administrative policy, so shortest distance is not the universal objective.
WORKED_Q: 无向边 AB=2、AC=5、BC=1、BD=4、CD=1，从 A 求到 D 的最短路径。 || For undirected edges AB=2, AC=5, BC=1, BD=4, CD=1, find the shortest path from A to D.
WORKED_A: 初始 B=2、C=5；确定 B 后 C 降为 3，D=6；确定 C 后 D 降为 4。路径 A-B-C-D，下一跳为 B，D 的前驱为 C。 || After B is fixed at 2, C becomes 3 and D 6; fixing C improves D to 4. The path is A-B-C-D, with next hop B and predecessor of D equal to C.
PRACTICE_Q: 无向非负边 AB=1、AC=4、BC=1、BD=5、CD=2。从A运行Dijkstra，先确定B，补出C/D暂定距离，再完成到D的路径和下一跳。 || For undirected nonnegative edges AB=1,AC=4,BC=1,BD=5,CD=2, run Dijkstra from A. After fixing B, update C,D and finish the path and next hop to D.
HINT: 经B给C的候选是1+1；随后比较经C到D的路径。 || Via B, C receives candidate 1+1; then compare the route to D via C.
PRACTICE_A: 初始B=1、C=4；确定B后C=2、D=6；确定C后D=min(6,2+2)=4。路径A–B–C–D，A到D下一跳为B。 || Initially B=1,C=4. Fixing B gives C=2,D=6; fixing C gives D=4. Path A–B–C–D has next hop B.
TRANSFER_Q: 无向边 AB=2、AC=3、BD=1、CD=1、BC=4。从A独立求到D的最短路径、距离、下一跳、D前驱。随后把BD代价增至5，重新计算。 || For undirected edges AB=2,AC=3,BD=1,CD=1,BC=4, find A’s shortest path to D, distance, next hop, and D’s predecessor. Then raise BD to 5 and recompute.
TRANSFER_A: 原先经B到D为3，经C为4，选A–B–D：距离3、下一跳B、D前驱B。修改后经B为7，经C仍4，选A–C–D：距离4、下一跳C、前驱C。路径必须随边权更新，不能沿用旧答案。 || Initially A–B–D costs 3 versus 4 via C, so next hop and D’s predecessor are B. After the change, via B costs 7 while A–C–D costs 4; both next hop and predecessor become C. Recompute when edge weights change.
BRIDGE: 选好下一跳后，还要在本段链路交付帧并处理共享介质与错误。

@@ net18 | 链路层：发现错误与争用信道是两类问题 | Error detection and shared-medium access
CARDS: N217,N218,N219,N220,N221,N222,N223,N224,N225,N226,N227,N228,N229,N230,N282,N283
PREREQ: net02,net05
GOAL: 能用XOR长除法构造并检查CRC码字；偶校验和ALOHA使用独立练习单元。
EXPLAIN: 链路层把数据交给本段邻居。差错检测增加冗余，判断传输是否破坏内容；纠错还需利用冗余恢复数据。偶校验能检测奇数个翻转，但两位同时翻转可能不被发现。二维校验将行列信息结合，单数据位出错时可由行列交点定位。

CRC 把位串当二元多项式，用 XOR 做除法而不是十进制减法。 XOR 对相同位给 0、不同位给 1；每次把生成式的最高 1 对齐到当前余串最高 1 再做 XOR。生成式最高次数为 r 时，数据后补 r 个零再求余，将 r 位余数接回原数据。接收端检查整串能否被生成式整除；检出能力依赖生成式和错误模式，不等于能纠正任意 r 个错位。

共享介质还要决定谁在何时发。理想时隙 ALOHA 中，N 个有包待发的节点独立以 p 在槽首发送，一槽只容一包且碰撞均失败，则成功概率为 $Np(1-p)^{N-1}$。像多人同时抢答，太少人尝试会空场，太多人一起说又听不清；这个类比对应空闲、成功、碰撞三种结果，不适用于所有真实无线接收机制。
RECAP_EN: Error detection protects content; medium access coordinates senders. CRC uses binary polynomial arithmetic, while ALOHA success requires exactly one independent transmission in a slot.
WORKED_Q: 数据 1101，生成式 1011，求 CRC 码字。 || Encode data 1101 with CRC generator 1011.
WORKED_A: r=3；1101000 XOR 1011000 得 0110000，再 XOR 0101100 得 0011100，再 XOR 0010110 得 0001010，再 XOR 0001011 得 0000001。余数 001，码字 1101001。 || Degree r=3. XOR long division of 1101000 by 1011 yields remainder 001, so the transmitted codeword is 1101001.
PRACTICE_Q: 数据位110，CRC生成式1011（次数r=3），用模二XOR长除法编码。先补3个零，再求余数和发送码字。 || Encode data 110 using CRC generator 1011 of degree 3. Append three zeros, divide by XOR, then give remainder and codeword.
HINT: 110000 XOR 101100=011100；把生成式最高位与余下最高1对齐继续。 || Begin 110000 XOR 101100=011100; keep aligning the generator’s leading one with the remainder’s leading one.
PRACTICE_A: 011100 XOR 010110=001010；再 XOR 001011=000001。余数001，发送110001；用1011检查整串余数为0。 || Continue 011100 XOR 010110=001010, then XOR 001011=000001. The remainder is 001 and codeword 110001, which divides with zero remainder.
TRANSFER_Q: 数据101、生成式1011，独立计算CRC码字。若传输时最后一位翻转，接收端得到什么位串、余数是多少，能否检出？ || Independently encode data 101 using generator 1011. If the final transmitted bit flips, find the received bits and remainder and say whether the error is detected.
TRANSFER_A: 101000 XOR 101100=000100，余数100，码字101100。末位翻转得到101101；除以1011余数001，所以检出。余数0只表示没有检出，并不证明所有可能错误都不存在。 || The division 101000 XOR 101100 leaves remainder 100, giving codeword 101100. Flipping its last bit gives 101101 and remainder 001, so the error is detected. A zero remainder would mean no detected error, not proof of no possible error.
BRIDGE: 历史教程把这些机制组合起来，下一节练习先辨认事件和状态，再读数字。

@@ net19 | 往年教程：把状态画出来再答题 | Historical protocol and calculation clinic
CARDS: N231,N232,N233,N234,N235,N236,N237,N238,N239,N240,N241,N242,N243,N244,N245,N246,N247,N248,N249,N250,N251,N252,N253,N254,N255,N256,N257,N258,N259
PREREQ: net07,net09,net13,net15,net16,net17,net18
GOAL: 能按帧到达事件更新交换机MAC表，并区分已知单播、未知泛洪和同端口过滤。
EXPLAIN: HTTP/DNS 题画依赖时间轴；GBN/SR/TCP 题画发送与接收两列，逐行写“哪个事件—收到什么—状态怎样变—发什么 ACK”。Reno 图先标重复 ACK、超时与门限，再读窗口。不同教程约定的 RTT 更新顺序也要按题明确，不能从记忆混入另一版本。

子网分配先确定块大小和对齐边界，再检查地址区间不重叠；Dijkstra 平局可有多个选点顺序，但要验证最终距离。交换机从收到帧的源地址学习入端口，对未知目的泛洪；因此一个不是最终目的的分支也可能学到源地址。它不会仅凭发出帧就学到目的地址。

这些 29 张题覆盖多个专题，是综合练习入口。先完成相应机制课，再分专题独立作答。原图、原题单位和教材模型均在关联卡片中，不能跳过图形条件直接背数字。
RECAP_EN: Use event tables for protocol state, aligned intervals for subnets, and explicit invariants for graph algorithms. Historical numerical solutions depend on the stated model and diagram.
WORKED_Q: 一台交换机有端口1/2/3，初始MAC表为空，均属同一LAN。先在端口1收到A→G帧，再在端口3收到G→A帧。每步写学习到的表项和转发端口。 || A switch has ports 1,2,3 on one LAN and an empty MAC table. It receives A→G on port 1, then G→A on port 3. Trace learned entries and outgoing ports.
WORKED_A: 第一步只从源学习A→1；G未知，向2、3泛洪。第二步学习G→3；查目的A已知在1，只向1转发。表为A→1、G→3；不能从第一帧的目的字段提前学到G位置。 || First learn A→1 from the source; unknown G floods to 2 and 3. Then learn G→3; known A causes forwarding only to 1. The table is A→1,G→3. The first frame’s destination cannot reveal G’s port.
PRACTICE_Q: 端口1/2/3同一LAN，当前表A→1、G→3。在端口2收到B→A，然后端口1收到A→B。依次写表项和转发。 || With table A→1,G→3 on one LAN, receive B→A on port 2, then A→B on port 1. Trace learning and forwarding.
HINT: 每次先更新源地址，再查目的；目的已经知道时只发对应端口。 || Update source learning first, then look up the destination; known destinations use one port.
PRACTICE_A: 先学B→2，B→A只发1；再确认A→1，A→B只发2。表有A→1、B→2、G→3。 || Learn B→2 and forward the first frame to 1. Refresh A→1 and forward the second to 2. Entries are A→1,B→2,G→3.
TRANSFER_Q: 同一LAN的交换机表中A→1、B→2；现在A移动，在端口3发A→B；随后端口2收到B→B的帧。分别怎样更新与转发？假设没有安全限制。 || A switch knows A→1,B→2 on one LAN. A moves and sends A→B into port 3; then B→B arrives on port 2. Trace learning and forwarding, with no security restrictions.
TRANSFER_A: 第一帧把A更新为3，查B→2并只发端口2。第二帧确认B→2，目的也在入端口2，不向其他端口转发（过滤）。学习依据当前源帧，旧表项不是永远有效。 || The first frame updates A→3 and forwards to 2. The second refreshes B→2; destination and ingress coincide, so it is filtered rather than forwarded elsewhere. Source learning can update stale locations.
BRIDGE: 最后用完整网页访问串起 DHCP、ARP、DNS、TCP 与 HTTP，并保留实验取证习惯。

@@ net20 | 端到端串联：从空缓存到拿到网页 | From empty caches to a fetched page
CARDS: N260,N261,N262,N263,N264,N265,N266,N267,N268,N269,N270,N271,N272,N273,N274,N275,N276,N277,N278,N279,N280,N281
PREREQ: net09,net14,net16,net18
RELATED: net19
GOAL: 能在明确IPv4场景中串起地址配置、下一跳解析、DNS、TCP和HTTP，并说明缓存改变哪些步骤。
EXPLAIN: 在 IPv4 以太网、用 DHCP 获取配置、缓存为空、访问远端明文 HTTP 的教学场景中，先取得地址、掩码、默认网关与 DNS 配置。接着为 DNS 查询找到本地下一跳：DNS 服务器在同一子网，就 ARP 查它；在远端，就 ARP 查网关。ARP 用已知 IPv4 地址获得本地链路地址，不是在全网寻找远端主机。

DNS 返回网站地址后，主机向远端网站建立 TCP 连接，再交换 HTTP 请求与响应；若网关 MAC 已缓存，便不必重复 ARP。第一跳帧发给网关，而 IP 目的仍是网站主机。每经过路由器，链路帧重新组织；无 NAT 等改写时，IP 目的仍指向最终主机。先想清“最终找谁”和“这一步交给谁”，就不会混淆两种地址。

抓包先区分帧、IP 数据报、TCP 载荷与应用消息。HTTP 请求到响应的间隔还含服务器处理等成本，不能直接叫纯网络 RTT；TCP 的 ACK 时间样本也可能含接收端延迟确认，重传还会造成配对歧义。旧 SSL/TLS 字段按实际版本解释。编程项目需另测消息定界、部分接收与断连；这里的教学链条不代表已经运行了真实实验。
RECAP_EN: A complete fetch combines configuration, local next-hop resolution, DNS, transport setup, and application exchange. Link-layer destinations change hop by hop, while end-to-end roles remain distinct.
WORKED_Q: IPv4以太网主机刚启动，配置和缓存均为空；使用远端DNS和远端HTTP网站，经默认网关、无NAT。用简化协议顺序说明怎样从启动走到网页响应，特别指出DNS查询也需要下一跳MAC。 || An IPv4 Ethernet host starts with no configuration or caches. It uses remote DNS and HTTP servers through a default gateway, without NAT. Outline the simplified sequence from startup to response, including the next-hop MAC needed for DNS.
WORKED_A: 先DHCP获得IP/掩码/网关/DNS配置；因DNS在远端，ARP解析本LAN网关MAC，再发送DNS查询并获得网站IP。随后向网站建立TCP，再发HTTP请求并收响应。首跳帧目的为网关MAC，IP目的分别是DNS或网站服务器；每跳更换链路封装。 || DHCP supplies IP, mask, gateway and DNS configuration. ARP resolves the gateway MAC before remote DNS queries; DNS yields the website IP. Then establish TCP and exchange HTTP. First-hop frame destination is the gateway MAC while IP destination names DNS or web server; link framing changes at each hop.
PRACTICE_Q: 主机已有有效IP/掩码/网关/DNS配置和网关ARP缓存，但没有网站DNS缓存、没有TCP连接。DNS和网站都在远端。哪些前述步骤可跳过，哪些仍需做？ || The host has valid configuration and a gateway ARP entry, but no website DNS record or TCP connection. Both servers are remote. Which steps can be skipped and which remain?
HINT: 按配置、MAC、域名地址、传输连接四种状态分别检查。 || Check configuration, next-hop MAC, name record, and connection state separately.
PRACTICE_A: 可跳过此次DHCP获取与网关ARP查询；仍需DNS解析、TCP建连和HTTP交换。已有MAC不等于已有域名答案，也不等于已建立TCP。 || Skip new DHCP acquisition and gateway ARP resolution; perform DNS, TCP setup and HTTP. A cached MAC is neither a cached name answer nor an open TCP connection.
TRANSFER_Q: 主机配置有效，网站IP已缓存，但该网站现在与主机同一子网，ARP缓存为空、TCP未连接；IPv4以太网，无代理、无NAT。独立列必要步骤。ARP解析完成后，首个发往网站的IP包及承载它的以太网帧，其目的IP与目的MAC分别指向谁？ || Configuration and website IP cache are valid; the website is now on the same IPv4 Ethernet subnet, ARP cache empty and TCP closed, with no proxy or NAT. List the required steps. After ARP resolution, identify the destination IP of the first website IP packet and the destination MAC of its enclosing Ethernet frame.
TRANSFER_A: 不需本次DHCP或DNS；ARP解析网站主机本身的MAC，再TCP建连并HTTP交换。发往网站的IP包目的IP和承载它的帧目的MAC都指向网站主机，不经默认网关；ARP广播本身不是该IP数据包。 || No new DHCP or DNS is needed. ARP resolves the website host’s MAC, followed by TCP and HTTP. For the website IP packet, both IP and enclosing frame destination identify that host rather than the gateway; the ARP broadcast is a separate exchange.
BRIDGE: 再回到最初的网页图，用英文逐层讲完整条路径；哪一段说不清，就回该微课补机制，然后用相关卡片检索。
