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
PRACTICE_Q: 链路从 100 Mbps 升到 1 Gbps，光在同一介质中的传播速度也变为十倍吗？ || Does upgrading a link from 100 Mbps to 1 Gbps make signals propagate ten times faster in the same medium?
HINT: 区分单位 bit/s 和 m/s。 || Compare units: bits per second versus meters per second.
PRACTICE_A: 不会；串行化速率提升，传播速度主要由介质决定。 || No. Serialization rate increases; propagation speed is governed primarily by the medium.
TRANSFER_Q: 能连通服务器 IP，但浏览器仍无法正确交换网页，除了物理连接还缺什么检查？ || If the server IP is reachable but the browser cannot exchange pages correctly, what should you check beyond physical connectivity?
TRANSFER_A: 进程端口、应用协议、请求格式与响应状态等；网络可达不保证应用协议成功。 || Check process ports, application protocol, request format, and response status. Network reachability does not establish application success.
BRIDGE: 共享网络怎样安排多个用户发送，要先理解电路交换与分组交换。

@@ net02 | 分组交换：共享容量与等待的来源 | Packet switching and statistical multiplexing
CARDS: N013,N014,N015,N016,N017,N018,N019,N020,N021,N022,N023,N024,N095,N096,N097,N098
PREREQ: net01
GOAL: 能解释预留资源与按需共享的取舍，并识别存储转发。
EXPLAIN: 电路交换先预留通信资源，例如固定时隙；即使某时刻没数据，该份额仍被保留。分组交换把消息切成包，多个用户按需共享链路。突发流量通常不同时达到峰值，共享可以更灵活，但同时到达超过输出容量时需要排队。

存储转发表示路由器先收到一个完整分组，再将它发上下一条链路。因此一个分组经过两条链路，需要在每条链路各付一次发送全部比特的时间。但不同分组可以在不同链路同时前进，后面会把这点写成流水线时间轴。

简单统计复用模型还假设用户独立活跃。若每个用户以概率 p 活跃，总活跃数可用二项分布；真实用户可能相关，所以不能把理想概率当作网络无拥塞保证。当前课堂 Q&A 与 Tutorial 中同题的选项字母可能不同，应记判断依据。
RECAP_EN: Circuit switching reserves resources; packet switching shares them on demand and may queue. Store-and-forward waits for a complete packet at each intermediate router.
WORKED_Q: 1 Mbps 链路，每个活跃用户需 100 kbps，预留式可支持多少个同时用户？ || A 1 Mbps link allocates 100 kbps per active user. How many simultaneous reserved-rate users fit?
WORKED_A: 1000/100=10 个。分组共享可接入更多用户，但若同时活跃超过 10，就不能都立即获得该速率。 || Ten users fit. Packet sharing may admit more users, but more than ten simultaneously active users cannot all immediately obtain that rate.
PRACTICE_Q: 三个用户独立地以 0.1 概率活跃，三人同时活跃概率是多少？ || Three users are independently active with probability 0.1 each. What is the probability all three are active?
HINT: 独立事件的联合概率相乘。 || Multiply independent event probabilities.
PRACTICE_A: 概率为 0.1³=0.001。 || The probability is 0.001.
TRANSFER_Q: 如果所有用户都在同一直播开始时活跃，独立模型可能哪里失真？ || What fails in the independence model if all users become active at the start of the same live stream?
TRANSFER_A: 活跃事件相关，联合高负载可能明显更常见。需要观测相关性或使用合适的流量模型。 || Activity is correlated, so simultaneous high load may be much more frequent. Use evidence about correlations or a suitable traffic model.
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
PRACTICE_A: 第一包 6 ms，后面再 3×2=6 ms，总 12 ms。 || The first packet takes 6 ms, followed by three 2 ms intervals, totaling 12 ms.
TRANSFER_Q: 只把包长减半，传播距离不变，首位和末位到达时间分别怎样变？ || If only packet length halves, how do first- and last-bit arrival times change?
TRANSFER_A: 首位约仍在 d/s 到达；末位的发送部分减半，传播部分不变。本例末位变为 3+5=8 ms。 || First-bit arrival stays about d/s. Last-bit serialization halves while propagation is unchanged, giving 8 ms in the worked example.
BRIDGE: 时延描述等多久；吞吐量描述持续交付多快，排队把二者联系起来。

@@ net04 | 容量、吞吐量和排队为什么不能混用 | Capacity, throughput, and queueing
CARDS: N033,N034,N035,N036,N037,N038,N039,N040
PREREQ: net03
GOAL: 能找瓶颈、计算负载，并指出仅凭平均速率推不出什么。
EXPLAIN: 一条路径的持续单流吞吐量受最慢环节约束。在无其他限制的理想模型中，不超过各链路速率的最小值；应用有效吞吐量还要扣开销、重传，并考虑共享和协议窗口。提高非瓶颈链路常常没有效果。

平均包长 L、到达率 a、链路速率 R 给出负载 rho=La/R。它比较输入工作量与服务容量，不直接给出某个包要等多久。两个平均负载相同的流量，一个均匀到达，一个集中突发，可以有完全不同的排队。

无限缓冲的常见随机队列模型在接近饱和时等待会急剧上升；有限缓冲则会丢包。加大缓冲区不增加链路速率。Traceroute 每跳显示的是探测往返时间，不能把相邻行相减就当成已验证的单向链路时延。
RECAP_EN: Capacity is an upper bound, throughput is achieved delivery rate, and queueing depends on traffic timing as well as average load. High throughput can coexist with long response delay.
WORKED_Q: 平均 1000 byte，每秒 100 包，1 Mbps 链路，负载是多少？ || For 1,000-byte average packets at 100 packets/s on a 1 Mbps link, compute load.
WORKED_A: 输入 8000×100=800000 bit/s，rho=0.8。不能据此说每个包只等待发送时间的 20%。 || Input load is 800,000 bit/s, so rho=0.8. This does not specify a per-packet waiting time.
PRACTICE_Q: 十对服务器—客户端各传一条流；每对各有独立的 20 Mbps 服务器接入和 10 Mbps 客户端接入，仅共享并均分 50 Mbps 核心链路。单流理想速率是多少？ || Ten server-client pairs each carry one flow, with separate 20 Mbps server and 10 Mbps client access links. Only the 50 Mbps core is shared equally. What is the ideal per-flow rate?
HINT: 比较端点限制与核心份额。 || Compare endpoint rates and the core share.
PRACTICE_A: 每条流的三处上限为 20、10、5 Mbps，因此取最小值 5 Mbps。若十条流还共享同一条 20 Mbps 服务器接入，公平份额将受 20/10=2 Mbps 限制；那是不同题设。 || The three per-flow limits are 20, 10, and 5 Mbps, so the ideal rate is 5 Mbps. If all ten also shared one 20 Mbps server link, equal shares would instead be limited to 2 Mbps.
TRANSFER_Q: 同一路径下载大文件很快，交互请求仍很慢，有矛盾吗？ || Is it contradictory for a path to transfer large files quickly but respond slowly to interactive requests?
TRANSFER_A: 不矛盾；长传输重视持续吞吐量，交互可能被传播、排队和多次 RTT 主导。 || No. Large transfers depend strongly on sustained throughput, while interaction may be dominated by propagation, queueing, and multiple round trips.
BRIDGE: 要说明开销和协议功能来自哪里，需要分层与封装。

@@ net05 | 分层：每层首部回答一个不同的问题 | Layering and encapsulation
CARDS: N041,N042,N043,N044,N045,N046,N047,N048,N049,N050,N051
PREREQ: net01
GOAL: 能把一次应用消息映射到五层职责，并解释安全功能的位置。
EXPLAIN: 应用层定义消息含义；传输层联系进程；网络层跨网络送分组；链路层在本段链路送帧；物理层传信号。发送方逐层加入控制信息，接收方按对应规则解释和去除，这就是封装与解封装。

可以把它看成不同层次的地址与约定：应用问“请求什么”，端口问“哪个进程”，IP 问“目的接口/网络在哪里”，本地链路地址问“这一跳交给谁”。普通路由器转发无需理解最终网页内容，但要处理所在链路帧与 IP 信息。

基础 IP 网络尽力而为，不承诺一定送达；高层可以补可靠交付。加密主要回答“旁人能否读懂”，认证回答“身份或消息来源是否可信”，完整性验证回答“内容是否被改过”；具体机制可组合提供这些属性，单有加密不自动具备全部属性。源 IP 不能代替身份认证。分层是职责模型，不意味着现实设备严格只处理某一层。
RECAP_EN: Each layer adds control information for a distinct service. End-to-end applications depend on lower-layer delivery, but reachability and source addresses do not by themselves establish authentication or confidentiality.
WORKED_Q: 1000 byte 应用数据，三层各加 20 byte 首部，载荷效率是多少？ || A 1,000-byte payload receives three 20-byte headers. What is payload efficiency?
WORKED_A: 总大小 1060 byte，效率 1000/1060≈94.34%，忽略尾部和其他开销。 || Total size is 1,060 bytes, giving about 94.34% payload efficiency, excluding trailers and other overhead.
PRACTICE_Q: HTTP、TCP、IP、Ethernet 分别主要放在哪层？ || Map HTTP, TCP, IP, and Ethernet to the teaching stack.
HINT: 从消息语义逐层走到本地帧。 || Move from message semantics toward local frames.
PRACTICE_A: 应用、传输、网络、链路。 || Application, transport, network, and link layers, respectively.
TRANSFER_Q: 对方发来的包声称源 IP 是学校服务器，能直接证明是该服务器吗？ || Does a packet claiming the university server's source IP prove that identity?
TRANSFER_A: 不能，源地址声明可能被伪造；应依赖相应认证机制。加密与认证也应分别说明。 || No. A claimed source address can be spoofed; use an appropriate authentication mechanism and distinguish it from encryption.
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
PRACTICE_Q: 服务器 IP 已知，怎样区分同一主机上的不同服务进程入口？ || How are different service endpoints on the same server host distinguished?
HINT: 传输层端点不只有 IP。 || A transport endpoint includes more than an IP address.
PRACTICE_A: 还需传输协议和端口等端点信息；端口不是用户身份认证。 || Include transport protocol and port information. A port is not user authentication.
TRANSFER_Q: 能否说“TCP 一定比 UDP 慢”？ || Is TCP necessarily slower than UDP?
TRANSFER_A: 不能脱离任务与条件比较。连接建立、丢包恢复、应用实现、拥塞和所需正确性都会影响完成时间。 || Not without a task and conditions. Setup, recovery, congestion, implementation, and required correctness all affect completion time.
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
TRANSFER_Q: 缓存返回 304，为什么不能把这次请求的网络时间记为零？ || Why is the network time not zero when a cache validation returns 304?
TRANSFER_A: 仍需发验证请求、等待服务器响应；省去的是未变正文传输，非全部通信。 || The validation request and server response still travel; the unchanged body is omitted, not all communication.
BRIDGE: 同样使用应用协议，电子邮件却把发送、存储与读取拆成不同阶段。

@@ net08 | 电子邮件：发送信件与读取信箱是两条流程 | Mail delivery versus mailbox access
CARDS: N111,N112,N113,N114,N115,N116,N117,N118,N119,N120
PREREQ: net06
GOAL: 能追踪邮件从发送到读取，并区分 SMTP 信封与邮件内容。
EXPLAIN: 用户代理把邮件交给邮件服务器，服务器之间用 SMTP 传递；收件人之后通过 IMAP、POP3 或 Webmail 访问邮箱。邮件到达服务器与用户已经阅读不是同一个事件。

SMTP 的 MAIL FROM 与 RCPT TO 构成传输信封，决定投递与退信等路由信息；DATA 里面的 From、To 等头部属于邮件内容。两者可以不同，不能只看显示头就还原全部传输端点。

POP3 常见下载后删除或保留模式；IMAP 侧重服务器上邮箱状态的同步与管理。Webmail 的浏览器一段通常用 HTTP，后面的服务器邮件传递仍可用 SMTP。协议角色应按哪两个实体在通信来判断。
RECAP_EN: SMTP delivers messages between mail systems; mailbox access is a separate stage. The SMTP envelope and message headers serve different roles and may contain different addresses.
WORKED_Q: 浏览器打开网页邮箱发信，浏览器与网站、邮件服务器与对方邮件服务器分别用什么应用协议角色？ || When sending through webmail, distinguish the browser-to-site and mail-server-to-mail-server protocol roles.
WORKED_A: 浏览器访问 Webmail 使用 HTTP 相关交互；邮件系统对外传递可使用 SMTP。不能因界面是网页就说整个投递过程只用 HTTP。 || Browser access uses HTTP interactions, while mail delivery between servers can use SMTP. A web interface does not make the entire delivery path HTTP-only.
PRACTICE_Q: SMTP 的 RCPT TO 与邮件正文头里的 To 是否必须相同？ || Must SMTP RCPT TO equal the message header's To field?
HINT: 分别是传输信封和内容头。 || One belongs to the transport envelope and the other to message content.
PRACTICE_A: 不必相同，应分别读取它们的证据。 || No; interpret evidence for each separately.
TRANSFER_Q: POP3 已 RETR 一封邮件，能否仅凭这一命令断言服务器已删信？ || Does a POP3 RETR command alone prove that the server deleted the message?
TRANSFER_A: 不能，RETR 是获取内容；删除还涉及 DELE 及会话提交等协议步骤。 || No. RETR retrieves content; deletion involves DELE and the protocol's session update steps.
BRIDGE: 浏览器与邮件服务器都常需要把名称解析为地址，下一节追踪 DNS。

@@ net09 | DNS：沿层级找答案，靠缓存少走路 | DNS resolution and caching
CARDS: N121,N122,N123,N124,N125,N126,N127,N128,N129,N130,N131,N132,N133,N134
PREREQ: net06,net07
GOAL: 能区分本地解析器、根、TLD、权威服务器及递归/迭代。
EXPLAIN: 用户通常把名字交给本地递归解析器，而不是亲自向所有层级查询。解析器可向根询问下一步，再找 TLD，再找该域的权威服务器，直到获得所需记录。根服务器不需要保存互联网所有主机地址，它提供委派方向。

递归请求是“请替我完成解析并回答”；迭代回答可说“去问这个服务器”。这是交互方式，不是服务器名称的同义词。A/AAAA 给 IPv4/IPv6 地址，NS 指定域的权威服务器，MX 指向邮件交换服务器，CNAME 建立别名。一个名称可以对应多个地址，也可能经过别名链，所以域名不等于一台唯一机器。

缓存让后续解析跳过已知步骤，TTL 控制记录可被缓存使用多久。它不会保证记录全球同时刷新。计算 DNS 时间要列出哪些缓存为空、哪些交互串行、每一步 RTT 如何定义。原图与不同文件页码在关联卡片中保留。
RECAP_EN: A recursive resolver follows delegations and caches records. Root, TLD, and authoritative roles are distinct; resolution delay depends on the actual cache state and dependency chain.
WORKED_Q: 主机到本地解析器 RTT=2 ms，三次串行上游交互各 20 ms，无缓存，DNS 共多久？ || With 2 ms host-to-resolver RTT and three sequential 20 ms upstream exchanges, no cache, what is DNS delay?
WORKED_A: 2+3×20=62 ms。这里把主机到解析器的一次往返单独计入，忽略处理等时间。 || The delay is 62 ms, counting the host-resolver exchange once and ignoring processing.
PRACTICE_Q: 本地解析器已有有效最终记录缓存，同样模型下多久？ || If the local resolver already caches the final valid record, how long does it take in this model?
HINT: 不再访问上游层级。 || No upstream exchanges are needed.
PRACTICE_A: 只需本地交互的 2 ms。 || The delay is two milliseconds.
TRANSFER_Q: DNS 完成后还要取小 HTTP 页面，能把 DNS 和 TCP 建连完全并行吗？ || Can DNS resolution and TCP setup to the newly resolved destination always be fully parallelized?
TRANSFER_A: 普通未预知地址的依赖链中不能，先知道目的地址才能向它建连。若有预解析或其他缓存，应明确题设已改变。 || Not in the ordinary dependency chain without a known address. Setup requires the destination; pre-resolution or cached addressing changes the assumptions.
BRIDGE: 回到当前教程，把时延、容量和应用依赖合成完整解题过程。

@@ net10 | 当前教程：先画事件，再计算 | A method for current tutorial problems
CARDS: N071,N072,N073,N074,N075,N076,N077,N078,N079,N080,N081,N082,N083,N084,N085,N099
PREREQ: net02,net03,net04
GOAL: 能独立列出网络数值题的单位、路径、完成事件和忽略项。
EXPLAIN: 每题先写四行：图中几条链路、包或报文多大、从哪个时刻到哪个事件、忽略了哪些项。再把 byte 转 bit、km 转 m，最后才选公式。链路数和路由器数通常差一；每个分组完整到达与整段文件全部到达也不是同一事件。

切包题先求首包经过所有链路的时间，再数后续包到达间隔。若有不等速链路、首部、交叉流量或处理延迟，应按具体时间轴重新分析，不能继续套最简等速式。当前教程图题和官方解的原图都保留在卡片里。

Traceroute 表中的时间是各次探测的往返观测。不同探测可能经历不同排队或返回路径，星号也可能只是未及时收到 ICMP 回复。计算之前先识别每列真正测量的对象。
RECAP_EN: Define path, units, completion event, and ignored costs before calculating. A correct formula with the wrong event or units still answers the wrong question.
WORKED_Q: 8×10^6 bit 经三条 2 Mbps 存储转发链路，整报文与 800 个 10000 bit 包比较，忽略其他开销。 || Compare an 8×10^6-bit message with 800 packets of 10,000 bits over three 2 Mbps store-and-forward links, ignoring other costs.
WORKED_A: 整报文每段 4 s，共 12 s。分包每包每段 0.005 s，流水线总时间 (3+800-1)×0.005=4.01 s。 || The whole message takes 12 s. Packet serialization is 0.005 s, giving a pipeline completion time of 4.01 s.
PRACTICE_Q: 同样网络只发一个 10000 bit 包，需要多久？ || How long does a single 10,000-bit packet take over the same path?
HINT: 没有后续包可流水线重叠。 || There are no following packets to overlap.
PRACTICE_A: 3×0.005=0.015 s，即 15 ms。 || The delay is fifteen milliseconds.
TRANSFER_Q: 分得越小一定越好吗？ || Are smaller packets always better?
TRANSFER_A: 不一定；首部比例、处理开销、协议与链路限制都会产生取舍。前面的公式明确忽略这些项。 || No. Header overhead, processing, protocol behavior, and link constraints introduce trade-offs excluded from the simplified model.
BRIDGE: 当任务变成研究报告，仍要保持“观测支持哪些结论”的意识。

@@ net11 | 研究与 QE：从机制解释到可验证结论 | Evidence and explanation in networking
CARDS: N086,N087,N088,N093,N094
PREREQ: net04,net05,net09
GOAL: 能用机制、条件与证据组织英文解释，并规划研究报告。
EXPLAIN: 解释网络问题可以按“现象—可能机制—区分证据—适用边界”展开。例如网页慢可能来自 DNS、建连、服务器、传输或渲染；只测到总时长，无法直接定位哪个机制占主导。先提出能区分原因的测量，再给结论。

研究报告从具体问题出发，阅读原始论文的设定、方法、实验和限制，说明证据支持了什么。课件中的理想模型用来理解机制；真实抓包和实验用来判断具体系统。两者需要对照，不能把模拟条件、旧协议实现或历史统计直接当当前系统事实。

英文口述先定义指标，再说明机制，给一个例子并加适用条件。当前报告的页数、格式与提交要求请看网页“课程信息”中的研究报告说明；这里提供方法练习，不猜测教师尚未发布的安排。
RECAP_EN: Define the metric, explain a mechanism, identify discriminating evidence, and state the scope of the conclusion. A model or measurement answers only the question its assumptions support.
WORKED_Q: 测得某次网页总用时 2 秒，能断言网络带宽不足吗？ || A page takes two seconds to load. Does this establish insufficient network bandwidth?
WORKED_A: 不能。应拆 DNS、连接、首字节等待与正文传输等阶段，并考虑页面依赖与服务器时间。 || No. Separate DNS, connection setup, time to first byte, and content transfer while considering dependencies and server processing.
PRACTICE_Q: 想验证缓存是否降低时延，至少控制哪些条件？ || What should be controlled when testing whether caching reduces latency?
HINT: 比较的请求与状态需可解释。 || Make the compared requests and cache states interpretable.
PRACTICE_A: 相同资源、可说明的缓存状态、网络与服务条件；记录是否命中、是否重新验证和实际传输字节。 || Control resource identity, cache state, and network/server conditions; record hits, revalidation, and transferred bytes.
TRANSFER_Q: 用英文解释为什么一次更快的替代路径测量不证明改路由后普遍更好。 || Explain why a single faster alternate-path measurement does not prove that rerouting always improves performance.
TRANSFER_A: 性能依赖负载、时间、用户和路由政策，迁移流量也会改变负载。 || Performance depends on load, time, users, and routing policy; rerouting traffic can itself change congestion. Broader controlled evidence is needed.
BRIDGE: 后续预习从应用扩展到可靠传输、IP、路由与链路层，再回到完整网页访问。

@@ net12 | P2P 与 socket：资源共享也需要消息边界 | Distribution capacity and socket framing
CARDS: N135,N136,N137,N138,N139,N140,N141,N142,N143,N144,N145,N146,N147,N148
PREREQ: net04,net06,net09
GOAL: 能解释文件分发下界，并理解 TCP 字节流为什么需要应用定界。
EXPLAIN: 客户端—服务器分发 N 份大小 F 的文件，服务器至少上传 NF，最慢客户端至少下载 F，因此时间下界是 max(NF/us,F/dmin)。P2P 让客户端也贡献上传，增加总服务资源，但服务器仍至少要注入一份文件，最慢下载也仍是约束。

理想 P2P 下界为 max(F/us,F/dmin,NF/(us+sum ui))。这些是流体、充分协作等理想条件下的容量分析，不包含节点离线、协议开销或块稀缺问题。DASH 与 CDN 则分别通过适配码率和内容位置缓解应用体验问题。

实现消息协议时，TCP 给的是字节流，一次 send 不保证对应一次 recv。应用要定义长度前缀或分隔符、编码与最大长度，并缓冲不完整消息。UDP 保留数据报边界，但仍要处理丢失等问题。
RECAP_EN: Distribution lower bounds follow server upload, receiver download, and aggregate upload constraints. TCP applications must frame messages independently of send/receive call boundaries.
SYMBOLS: F | 一份文件大小，bit；N | 接收者数量；u_s | 服务器上传速率；u_i | 第 i 个对等节点上传速率；d_min | 最慢接收者下载速率；速率单位 | 所有速率统一为 bit/s
WORKED_Q: F=1 Gbit、N=10、us=100 Mbps、每个 ui=10 Mbps、dmin=50 Mbps，求两种理想下界。 || For F=1 Gbit, N=10, us=100 Mbps, each ui=10 Mbps, and dmin=50 Mbps, find client-server and P2P lower bounds.
WORKED_A: 客户端—服务器 max(100,20)=100 s；P2P max(10,20,10000/200)=50 s。这里 Gbit/Mbps 按十进制换算。 || Client-server requires at least 100 s; P2P requires at least max(10,20,50)=50 s, using decimal units.
PRACTICE_Q: TCP 先收到字符 AB，再收到 C\nD\n，若按换行定界，共得到哪些完整消息？ || TCP delivers AB followed by C\nD\n. With newline framing, which complete messages are reconstructed?
HINT: 第一批字节应先留在缓冲区。 || Retain the first bytes in a buffer.
PRACTICE_A: ABC 和 D 两条，不是 AB 与 C 两条。这里 \n 表示协议中的换行符。 || The complete messages are ABC and D. Here \n denotes the protocol newline delimiter.
TRANSFER_Q: P2P 总上传增加一倍，分发时间一定减半吗？ || Must distribution time halve if aggregate P2P upload doubles?
TRANSFER_A: 不一定，服务器注入和最慢下载可能成为主导限制。应重新比较三个下界。 || No. Server injection or the slowest receiver may dominate. Re-evaluate all three lower bounds.
BRIDGE: 应用想要可靠消息，先看传输层怎样处理损坏、丢失和重复。

@@ net13 | 可靠传输：为什么 ACK、序号、定时器缺一不可 | Reliability and sliding windows
CARDS: N149,N150,N151,N152,N153,N154,N155,N156,N157,N158,N159,N160,N161,N162,N163,N164,N165,N166
PREREQ: net03,net05,net06
GOAL: 能解释每个机制解决的失败场景，并比较停等、GBN 与 SR。
EXPLAIN: 校验和帮助检测损坏，却不保证检测一切错误，也不负责重传。ACK 告诉发送者接收进展；如果 ACK 丢了，发送者可能重发已送达数据，所以接收者还需要序号识别重复。数据或 ACK 完全丢失时，定时器让发送者最终再尝试。

停等每发一包就等确认。这里 RTT 专指往返传播时间，另忽略处理、排队与 ACK 发送时间；一个周期是发送数据所需的 L/R 加往返传播，所以 $U=(L/R)/(RTT+L/R)$。若题目给的是“开始发送到收到 ACK”的完整周期，就不能再加一遍 L/R。窗口允许多个包在途，减少长距离链路上“发一下、等很久”的空档。

基础 GBN 丢弃失序包并重复累计确认；超时时重传从最早未确认包开始、所有已发送但未确认的包，不包含窗口内尚未发送的位置。SR 缓存失序包、分别确认，仅对相应未确认包触发重传。常见等长发送/接收窗口的 SR 要求序号空间至少为窗口的两倍，并假定旧副本不会无限存活；这不是对任意长期旧包都安全的保证。
RECAP_EN: Checksums, ACKs, sequence numbers, and timers address different failure modes. Pipelining fills the path; GBN and SR trade retransmission work against receiver state and sequence-space requirements.
WORKED_Q: R=1 Gbps、L=8000 bit、RTT=30 ms，理想停等利用率与吞吐量是多少？ || For R=1 Gbps, L=8000 bits, and RTT=30 ms, find ideal stop-and-wait utilization and throughput.
WORKED_A: 发送时间 0.008 ms；U=0.008/30.008≈0.0002666，即 0.02666%；吞吐量约 0.2666 Mbps。 || Serialization is 0.008 ms. Utilization is about 0.0002666, or 0.02666%, giving roughly 0.2666 Mbps throughput.
PRACTICE_Q: 发送 0、1、2、3，1 丢失且不乱序，GBN 与 SR 接收端怎样处理 2、3？ || Packets 0,1,2,3 are sent, 1 is lost, and there is no reordering. How do GBN and SR handle 2 and 3?
HINT: 区分丢弃乱序与缓存乱序。 || Contrast discarding and buffering out-of-order packets.
PRACTICE_A: 基础 GBN 丢弃它们并重复确认最后连续收到的包；SR 缓存并分别确认，等待 1 补齐。 || Basic GBN discards them and repeats its cumulative ACK; SR buffers and acknowledges them individually, awaiting packet 1.
TRANSFER_Q: 只有 ACK、没有序号，为什么 ACK 丢失后可能向应用重复交付？ || Why can ACK loss cause duplicate application delivery if there are ACKs but no sequence identifiers?
TRANSFER_A: 发送者重传时，接收方无法分辨是新内容还是已收内容的副本。 || On retransmission, the receiver cannot distinguish new data from a duplicate of already delivered data.
BRIDGE: TCP 将这些思想用于可靠有序字节流，并加入连接与流量状态。

@@ net14 | TCP：用字节编号描述接收进度 | TCP sequence space and flow control
CARDS: N167,N168,N169,N170,N171,N172,N173,N174,N175,N176,N177
PREREQ: net13
GOAL: 能从字节范围推 ACK，并解释流量控制、定时器与握手。
EXPLAIN: TCP 数据序号按字节计数。把接收想成按页拼好一本书：即使第 3 页先到了，第 2 页的缺口仍存在。累计 ACK 表示下一期待的字节号，不是最近见过的最大序号。后面的字节可以缓存，但只要前面有缺口，累计 ACK 就停在缺口起点，有序字节流也不能把这段后的内容提前交给应用。

RTT 会波动，重传超时既要参考平滑均值，也要留给波动的余量。对有歧义的重传样本还需谨慎测量。课程数值题可能采用指定更新顺序，不能混用不同公式约定。

流量控制用接收窗口 rwnd 保护接收端缓冲；拥塞窗口 cwnd 保护网络，发送者受两者较小值约束，还要扣除已在途数据。握手同步连接状态与初始序号，关闭两个方向可以分开完成。教材简化模型用于理解，具体实现细节需单独确认。
RECAP_EN: TCP acknowledges a contiguous byte prefix by naming the next expected byte. Receiver flow control and network congestion control impose separate limits on outstanding data.
DEMO: tcp
WORKED_Q: 已按序收到至字节 999，接着收到 seq=1000、长 500 byte 的数据段，ACK 是多少？ || Bytes through 999 are contiguous, then a segment starts at 1000 with 500 data bytes. What ACK follows?
WORKED_A: 新段覆盖 1000–1499，下一期待 1500，ACK=1500；假设没有 SYN/FIN 等额外序号消耗。 || The segment covers bytes 1000–1499, so ACK=1500, assuming no extra SYN/FIN sequence-space consumption.
PRACTICE_Q: cwnd=12 kB、rwnd=8 kB，已有 5 kB 在途，简化模型还允许发送多少？ || With cwnd=12 kB, rwnd=8 kB, and 5 kB in flight, how much more may be sent under the simplified rule?
HINT: 先取窗口较小值，再扣在途。 || Take the smaller window, then subtract outstanding data.
PRACTICE_A: 还可发送 min(12,8)-5=3 kB。 || Three kB may be sent.
TRANSFER_Q: 已收 0–535 和 900–1000，中间缺失，累计 ACK 为何不是 1001？ || With bytes 0–535 and 900–1000 received, why isn't the cumulative ACK 1001?
TRANSFER_A: 连续前缀到 535，下一期待 536；ACK=536。后段到达不代表中间字节已交付。 || The contiguous prefix ends at 535, so ACK=536. Later bytes do not fill the gap.
BRIDGE: 接收者装得下，不代表网络送得动；接下来解释拥塞窗口怎样变化。

@@ net15 | 拥塞控制：试探可用容量，响应拥塞 | Congestion windows and feedback
CARDS: N178,N179,N180,N181,N182,N183,N184
PREREQ: net04,net14
GOAL: 能解释慢启动、加性增长和乘性减少，并说明教材模型边界。
EXPLAIN: 发送者通常不知道路径当前能承受多少流量，需要根据确认、丢包或显式拥塞信号调整在途数据。经典慢启动在适当假设下每 RTT 近似翻倍；名字描述相对于立即大窗口发送的起步方式，并非线性慢增长。

拥塞避免常用近似每 RTT 增加一 MSS 的加性增长；拥塞事件后缩小窗口。Tahoe、Reno 对三次重复 ACK 与超时的处理不同，Reno 的快速恢复还有临时窗口膨胀。答图题时先识别采用的协议版本、事件和观察时刻，再谈窗口数值。

窗口除 RTT 可以估计受窗口限制的发送率。在理想稳定 AIMD 锯齿中，窗口由 W/2 增到 W，平均约 3W/4。这个近似不是所有 TCP 的普遍公式。按连接公平也不等于按用户公平，一个用户可能开很多连接。
RECAP_EN: Congestion control adapts sending to network feedback, distinct from receiver flow control. Classic textbook window trajectories depend on protocol version and event timing.
WORKED_Q: 经典锯齿最大窗口 64 kB、RTT=0.1 s，按 3W/4 近似平均吞吐量。 || With maximum window 64 kB and RTT=0.1 s, estimate mean throughput using the classic 3W/4 approximation.
WORKED_A: 平均窗口 48 kB，吞吐量 480 kB/s；十进制单位下为 3.84 Mbps。 || Mean window is 48 kB, giving 480 kB/s or 3.84 Mbps with decimal units.
PRACTICE_Q: 理想慢启动从 1 MSS 起，前四轮窗口是什么？ || Ideal slow start begins at one MSS. What are the first four round windows?
HINT: 每轮近似翻倍，假设未遇阈值或丢包。 || Double each round, assuming no threshold or loss event intervenes.
PRACTICE_A: 前四轮分别为 1、2、4、8 MSS。 || The windows are 1,2,4,8 MSS.
TRANSFER_Q: 同样每连接平均分配带宽，A 开十条连接、B 开一条，能称为用户公平吗？ || If bandwidth is equal per connection but A opens ten connections and B one, is allocation user-fair?
TRANSFER_A: 不自动公平，A 可能获得十份、B 一份；公平的对象与衡量方式需要明确。 || Not automatically. A may obtain ten shares and B one; define the entity and metric for fairness.
BRIDGE: 端到端传输依赖 IP 跨网转发，下一节解释地址、前缀与分片。

@@ net16 | IP：前缀决定下一跳，MTU 决定装多大 | Addressing, forwarding, and fragmentation
CARDS: N185,N186,N187,N188,N189,N190,N191,N192,N193,N194,N195,N196,N197,N198,N199,N200,N201,N202
PREREQ: net03,net05
GOAL: 能手算子网范围与 IPv4 分片，并区分路由和逐包转发。
EXPLAIN: 转发是按已有表把当前分组送到下一接口；路由是形成和更新这些路径信息。最长前缀匹配选择对目的地址描述最具体的条目，例如 /24 优先于同样匹配的 /16。IP 地址通常关联接口，不应机械等同整台设备或用户身份。

IPv4 前缀 /p 表示前 p 位固定，其余位可变化；普通子网常保留网络与广播地址，但 /31、/32 等需要不同规则。DHCP 可分配地址并提供网关与 DNS 等配置；NAT 可改写地址与端口并记录映射状态。

MTU 是本条链路能装下的最大 IP 数据报大小，包含 IP 首部。允许 IPv4 分片时，把原载荷切片，每片另有首部；除末片外，数据长度须为 8 byte 的倍数，因为 offset 按原载荷中的 8 byte 块计位置。MF=1 表示后面还有片，0 表示最后一片。基本 IPv4 在最终目的端重组；IPv6 路由器不执行这种分片，需由源端采用相应机制。
RECAP_EN: Forwarding applies a table; routing builds it. Prefixes aggregate destinations, while MTU constrains datagram size. IPv4 fragment offsets count eight-byte blocks of original payload.
WORKED_Q: 4000 byte IPv4 数据报，20 byte 首部，MTU=1500，可分片且无选项，给出分片。 || Fragment a 4000-byte IPv4 datagram with a 20-byte header over MTU 1500, with fragmentation allowed and no options.
WORKED_A: 原载荷 3980；前两片各 1480 byte 数据，最后 1020。总长为 1500、1500、1040；offset 为 0、185、370；MF 为 1、1、0。 || Payload is 3980 bytes. Data lengths are 1480,1480,1020; total lengths 1500,1500,1040; offsets 0,185,370; MF bits 1,1,0.
PRACTICE_Q: 192.0.2.130/26 的网络和广播地址是什么？ || Find the network and broadcast addresses for 192.0.2.130/26.
HINT: /26 每个块包含 64 个地址。 || A /26 block contains 64 addresses.
PRACTICE_A: 落在 128–191 块，网络 192.0.2.128，广播 192.0.2.191。 || It lies in block 128–191: network 192.0.2.128 and broadcast 192.0.2.191.
TRANSFER_Q: 同时匹配 10.0.0.0/8、10.1.0.0/16、10.1.2.0/24，目的 10.1.2.99 选哪个？ || Which route matches 10.1.2.99 when /8, /16, and /24 routes as listed all match?
TRANSFER_A: 选 /24，因前缀最长，不是因为它在表里先出现或数字最大。 || Select 10.1.2.0/24, the longest matching prefix, not simply the first or numerically largest entry.
BRIDGE: 转发表从哪里来，需要路由算法与自治系统政策来解释。

@@ net17 | 路由：局部下一步怎样形成整条路径 | Shortest paths and routing policy
CARDS: N203,N204,N205,N206,N207,N208,N209,N210,N211,N212,N213,N214,N215,N216
PREREQ: net16
GOAL: 能手推 Dijkstra 与距离向量更新，并区分最短路与互联网政策。
EXPLAIN: 链路状态方法让节点获得拓扑信息，再计算路径。Dijkstra 在非负边权下，每次选未确定节点中暂定距离最小者；它的距离已不会被绕远的未确定路径改善，然后松弛相邻边。前驱用于还原路径，转发表则需要从源开始的第一跳，两者不一定同一个节点。

距离向量只与邻居交换到目的地的估计，更新为 $D_x(y)=\min_v[c(x,v)+D_v(y)]$。它像比较“先去哪个邻居，再接邻居所知的后半程”。坏消息传播可能缓慢，并出现计数到无穷。

互联网分为自治系统，内部可用 OSPF 等协议，跨系统 BGP 还受政策和路径属性约束。AS-PATH 帮助检测 AS 级环路；不能把 BGP 说成全互联网统一跑 Dijkstra。路由选择中的“最好”取决于所用目标。
RECAP_EN: Dijkstra fixes shortest distances from topology under nonnegative costs; distance vector composes neighbor estimates. Internet routing also uses administrative policy, so shortest distance is not the universal objective.
WORKED_Q: 无向边 AB=2、AC=5、BC=1、BD=4、CD=1，从 A 求到 D 的最短路径。 || For undirected edges AB=2, AC=5, BC=1, BD=4, CD=1, find the shortest path from A to D.
WORKED_A: 初始 B=2、C=5；确定 B 后 C 降为 3，D=6；确定 C 后 D 降为 4。路径 A-B-C-D，下一跳为 B，D 的前驱为 C。 || After B is fixed at 2, C becomes 3 and D 6; fixing C improves D to 4. The path is A-B-C-D, with next hop B and predecessor of D equal to C.
PRACTICE_Q: 经邻居 A 的本地代价 2、后程 6；经 B 为 5、1，选谁？ || A neighbor route costs 2+6 via A; another costs 5+1 via B. Which is selected?
HINT: 比较整条组合代价。 || Compare total path costs.
PRACTICE_A: 选 B，总代价 6，小于 A 的 8。 || Choose B at cost 6 rather than 8.
TRANSFER_Q: 某个 BGP 路径跳数更短，为什么仍可能不被选中？ || Why might BGP reject a path with fewer AS hops?
TRANSFER_A: 路由政策和其他优先属性可能先于 AS 路径长度发挥作用；需要具体政策才能判断。 || Routing policy and other preferred attributes may take precedence over AS-path length; inspect the applicable policy.
BRIDGE: 选好下一跳后，还要在本段链路交付帧并处理共享介质与错误。

@@ net18 | 链路层：发现错误与争用信道是两类问题 | Error detection and shared-medium access
CARDS: N217,N218,N219,N220,N221,N222,N223,N224,N225,N226,N227,N228,N229,N230
PREREQ: net02,net05
GOAL: 能解释校验、CRC 与随机接入分别解决什么问题。
EXPLAIN: 链路层把数据交给本段邻居。差错检测增加冗余，判断传输是否破坏内容；纠错还需利用冗余恢复数据。偶校验能检测奇数个翻转，但两位同时翻转可能不被发现。二维校验将行列信息结合，单数据位出错时可由行列交点定位。

CRC 把位串当二元多项式，用 XOR 做除法而不是十进制减法。生成式最高次数为 r 时，数据后补 r 个零再求余，将 r 位余数接回原数据。接收端检查整串能否被生成式整除；检出能力依赖生成式和错误模式，不等于能纠正任意 r 个错位。

共享介质还要决定谁在何时发。理想时隙 ALOHA 中，N 个有包待发的节点独立以 p 在槽首发送，一槽只容一包且碰撞均失败，则成功概率为 $Np(1-p)^{N-1}$。像多人同时抢答，太少人尝试会空场，太多人一起说又听不清；这个类比对应空闲、成功、碰撞三种结果，不适用于所有真实无线接收机制。
RECAP_EN: Error detection protects content; medium access coordinates senders. CRC uses binary polynomial arithmetic, while ALOHA success requires exactly one independent transmission in a slot.
WORKED_Q: 数据 1101，生成式 1011，求 CRC 码字。 || Encode data 1101 with CRC generator 1011.
WORKED_A: r=3；1101000 XOR 1011000 得 0110000，再 XOR 0101100 得 0011100，再 XOR 0010110 得 0001010，再 XOR 0001011 得 0000001。余数 001，码字 1101001。 || Degree r=3. XOR long division of 1101000 by 1011 yields remainder 001, so the transmitted codeword is 1101001.
PRACTICE_Q: 四个节点各以 1/4 发送，每槽成功概率是多少？ || Four nodes each transmit with probability 1/4. What is slot success probability?
HINT: 四选一成功者，其余三人不发。 || Choose one sender and require the other three to remain silent.
PRACTICE_A: 成功概率为 4×(1/4)×(3/4)³=27/64≈0.421875。 || The success probability is 27/64≈0.421875.
TRANSFER_Q: 单比特偶校验为何会漏掉两个翻转？ || Why can a single even-parity bit miss two flipped bits?
TRANSFER_A: 两次翻转使奇偶性改变两次又回原值，校验关系仍可能成立。 || Two flips change parity twice, restoring the original parity relation.
BRIDGE: 历史教程把这些机制组合起来，下一节练习先辨认事件和状态，再读数字。

@@ net19 | 往年教程：把状态画出来再答题 | Historical protocol and calculation clinic
CARDS: N231,N232,N233,N234,N235,N236,N237,N238,N239,N240,N241,N242,N243,N244,N245,N246,N247,N248,N249,N250,N251,N252,N253,N254,N255,N256,N257,N258,N259
PREREQ: net07,net09,net13,net15,net16,net17,net18
GOAL: 能用事件表追踪包、ACK、窗口与交换机学习，不靠记图形答案。
EXPLAIN: HTTP/DNS 题画依赖时间轴；GBN/SR/TCP 题画发送与接收两列，逐行写“哪个事件—收到什么—状态怎样变—发什么 ACK”。Reno 图先标重复 ACK、超时与门限，再读窗口。不同教程约定的 RTT 更新顺序也要按题明确，不能从记忆混入另一版本。

子网分配先确定块大小和对齐边界，再检查地址区间不重叠；Dijkstra 平局可有多个选点顺序，但要验证最终距离。交换机从收到帧的源地址学习入端口，对未知目的泛洪；因此一个不是最终目的的分支也可能学到源地址。它不会仅凭发出帧就学到目的地址。

这些 29 张题覆盖多个专题，是综合练习入口。先完成相应机制课，再分专题独立作答。原图、原题单位和教材模型均在关联卡片中，不能跳过图形条件直接背数字。
RECAP_EN: Use event tables for protocol state, aligned intervals for subnets, and explicit invariants for graph algorithms. Historical numerical solutions depend on the stated model and diagram.
WORKED_Q: 普通 IPv4 子网分别需 106 与 14 台主机，各至少要什么前缀？ || What minimum subnet sizes serve 106 and 14 hosts under ordinary IPv4 network/broadcast reservations?
WORKED_A: 106 需 7 位主机位，2^7-2=126，对应 /25；14 需 4 位，2^4-2=14，对应 /28。分配时还需对齐且避开已占区间。 || 106 hosts require /25 with 126 usable addresses; 14 require /28 with 14 usable addresses. Allocation must also align blocks and avoid occupied ranges.
PRACTICE_Q: 初始空交换表收到 A 发往未知 G 的帧，先学到谁？ || An empty switch table receives a frame from A to unknown G. Which address is learned first?
HINT: 学习依据是收到的源地址和入端口。 || Learning uses the source address and ingress port.
PRACTICE_A: 学到 A 对应入端口；对未知 G 向除入端口外的相关端口泛洪。 || It learns A on the ingress port and floods the unknown destination on applicable other ports.
TRANSFER_Q: 为什么已学到 A 不等于已学到 G？ || Why does learning A not imply learning G?
TRANSFER_A: 目的字段不告诉交换机 G 从哪个入端口发来；需要观察来自 G 的帧才能按源学习建立该映射。 || The destination field does not reveal G's ingress port. A source-learning entry for G requires observing a frame from G.
BRIDGE: 最后用完整网页访问串起 DHCP、ARP、DNS、TCP 与 HTTP，并保留实验取证习惯。

@@ net20 | 端到端串联：从空缓存到拿到网页 | From empty caches to a fetched page
CARDS: N260,N261,N262,N263,N264,N265,N266,N267,N268,N269,N270,N271,N272,N273,N274,N275,N276,N277,N278,N279
PREREQ: net09,net14,net16,net18
RELATED: net19
GOAL: 能从主机初始配置追到网页响应，并说明每步需要什么证据。
EXPLAIN: 在 IPv4 以太网、用 DHCP 获取配置、缓存为空、访问远端明文 HTTP 的教学场景中，先取得地址、掩码、默认网关与 DNS 配置。接着为 DNS 查询找到本地下一跳：DNS 服务器在同一子网，就 ARP 查它；在远端，就 ARP 查网关。ARP 用已知 IPv4 地址获得本地链路地址，不是在全网寻找远端主机。

DNS 返回网站地址后，主机向远端网站建立 TCP 连接，再交换 HTTP 请求与响应；若网关 MAC 已缓存，便不必重复 ARP。第一跳帧发给网关，而 IP 目的仍是网站主机。每经过路由器，链路帧重新组织；无 NAT 等改写时，IP 目的仍指向最终主机。先想清“最终找谁”和“这一步交给谁”，就不会混淆两种地址。

抓包先区分帧、IP 数据报、TCP 载荷与应用消息。HTTP 请求到响应的间隔还含服务器处理等成本，不能直接叫纯网络 RTT；TCP 的 ACK 时间样本也可能含接收端延迟确认，重传还会造成配对歧义。旧 SSL/TLS 字段按实际版本解释。编程项目需另测消息定界、部分接收与断连；这里的教学链条不代表已经运行了真实实验。
RECAP_EN: A complete fetch combines configuration, local next-hop resolution, DNS, transport setup, and application exchange. Link-layer destinations change hop by hop, while end-to-end roles remain distinct.
WORKED_Q: A 向远端 B 发 IP 包，本地以太网第一跳的目的 IP 和目的 MAC 各指向谁？假设经默认网关、无 NAT。 || A sends to remote B through its default gateway, without NAT. Whom do the destination IP and first-hop destination MAC identify?
WORKED_A: IP 目的为 B，帧的 MAC 目的为网关在 A 所在链路的接口。A 通常 ARP 查询网关地址，不是直接查询远端 B 的 MAC。 || Destination IP identifies B; destination MAC identifies the gateway's local interface. A resolves the gateway's MAC, not remote B's MAC.
PRACTICE_Q: B 改成同子网主机，第一跳 MAC 目的怎样变化？ || If B instead belongs to the same subnet, how does the first-hop MAC destination change?
HINT: 无需经过默认网关。 || No default-gateway hop is required.
PRACTICE_A: 通过本地 ARP 获得 B 的 MAC，帧直接发给 B；IP 目的仍为 B。 || Resolve B's local MAC and send the frame to B; the IP destination remains B.
TRANSFER_Q: 仅有 HTTP 请求文本，没有抓包的 IP 首部，能确定客户端 IP 吗？ || Can you determine the client's IP from HTTP request text alone without packet IP headers or other verified evidence?
TRANSFER_A: 不能；Host 指示请求的网站主机，不是客户端 IP。需要对应网络层证据，代理字段还应另行验证其来源。 || No. Host identifies the requested server authority, not the client IP. Obtain network-layer evidence and separately validate any proxy-provided fields.
BRIDGE: 再回到最初的网页图，用英文逐层讲完整条路径；哪一段说不清，就回该微课补机制，然后用相关卡片检索。
